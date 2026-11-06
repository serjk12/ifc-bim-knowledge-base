#!/usr/bin/env python3
"""Helper for the IFC/BIM knowledge base: validate, stats, filter, export.

Records live in research_raw/**/*.jsonl (one JSON object per line).
Schema: see _meta/SPEC.md.

Usage (from anywhere):
  python tools/kb.py validate [PATH ...]          # check JSONL files (default: all research_raw)
  python tools/kb.py stats [--md] [PATH ...]      # counts by lang/kind/topic/persona/intent/type/source
  python tools/kb.py filter [--kind real|synthetic] [--lang ru] [--topic coordinates_georef]
                            [--persona bim_coordinator] [--intent troubleshoot_export] [--type model_task]
                            [--text REGEX] [--limit 60] [--format brief|jsonl|md] [PATH ...]
  python tools/kb.py export                       # write exports/*.jsonl, *.csv, stats.md
"""
import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "research_raw"
EXPORTS = ROOT / "exports"

LIST_FIELDS = ("topics", "software", "context_given", "inspired_by")
DIMENSIONS = ("lang", "kind", "type", "persona", "intent", "topics", "source_type", "tone", "ifc_version")


def rel(p):
    try:
        return str(Path(p).resolve().relative_to(ROOT)).replace("\\", "/")
    except Exception:
        return str(p)


def _visible(p, base=None):
    # skip folders starting with "_" (e.g. research_raw/_smoke) below the searched base folder
    try:
        parts = Path(p).resolve().relative_to(Path(base or RAW).resolve()).parts
    except Exception:
        return True
    return not any(x.startswith("_") for x in parts[:-1])


def iter_files(paths, pattern="*.jsonl"):
    if not paths:
        yield from (p for p in sorted(RAW.rglob(pattern)) if _visible(p))
        return
    for f in paths:
        p = Path(f)
        if not p.is_absolute() and not p.exists():
            p = ROOT / f
        if p.is_dir():
            yield from (q for q in sorted(p.rglob(pattern)) if _visible(q, p))
        elif p.exists():
            yield p


def load(paths=None):
    recs, errors = [], []
    for f in iter_files(paths):
        try:
            text = f.read_text(encoding="utf-8-sig")
        except Exception as e:
            errors.append((rel(f), 0, f"read error: {e}"))
            continue
        for i, line in enumerate(text.splitlines(), 1):
            s = line.strip()
            if not s:
                continue
            try:
                r = json.loads(s)
                if not isinstance(r, dict):
                    raise ValueError("line is not a JSON object")
            except Exception as e:
                errors.append((rel(f), i, str(e)[:160]))
                continue
            for k in LIST_FIELDS:
                v = r.get(k)
                if isinstance(v, str):
                    r[k] = [x.strip() for x in v.split(",") if x.strip()]
            r["raw_file"] = rel(f)
            r["_line"] = i
            recs.append(r)
    return recs, errors


def problems(r):
    out = []
    kind = r.get("kind")
    if kind not in ("real", "synthetic"):
        out.append("kind must be 'real' or 'synthetic'")
    if not r.get("id"):
        out.append("missing id")
    if not r.get("lang"):
        out.append("missing lang")
    if kind == "real":
        if not (r.get("question_paraphrase") or r.get("title_original")):
            out.append("real record needs question_paraphrase or title_original")
        if not str(r.get("source_url", "")).startswith("http"):
            out.append("real record needs http(s) source_url")
    if kind == "synthetic" and not r.get("prompt"):
        out.append("synthetic record needs prompt")
    if not isinstance(r.get("topics", []), list):
        out.append("topics must be a list")
    return out


def cmd_validate(a):
    recs, errors = load(a.paths)
    bad = 0
    for f, i, e in errors:
        print(f"PARSE  {f}:{i}  {e}")
    seen = {}
    for r in recs:
        p = problems(r)
        if p:
            bad += 1
            print(f"FIELD  {r['raw_file']}:{r['_line']}  id={r.get('id')}  " + "; ".join(p))
        rid = r.get("id")
        if rid:
            if rid in seen:
                print(f"DUPID  {rid}  {seen[rid]}  and  {r['raw_file']}:{r['_line']}")
            else:
                seen[rid] = f"{r['raw_file']}:{r['_line']}"
    print(f"\nrecords={len(recs)} parse_errors={len(errors)} field_problems={bad}")
    return 1 if errors else 0


def counts(recs, dim):
    c = Counter()
    for r in recs:
        v = r.get(dim)
        if isinstance(v, list):
            for x in v:
                c[str(x)] += 1
        elif v not in (None, ""):
            c[str(v)] += 1
        else:
            c["(empty)"] += 1
    return c


def cmd_stats(a):
    recs, errors = load(a.paths)
    recs = [r for r in recs if match(r, a)]
    files = Counter(r["raw_file"] for r in recs)
    lines = [f"# Coverage stats", "", f"- records: **{len(recs)}** "
             f"(real: {sum(1 for r in recs if r.get('kind') == 'real')}, "
             f"synthetic: {sum(1 for r in recs if r.get('kind') == 'synthetic')})",
             f"- files: {len(files)}; parse errors: {len(errors)}", ""]
    for dim in DIMENSIONS:
        c = counts(recs, dim)
        lines += [f"## {dim}", "", "| value | count |", "|---|---|"]
        lines += [f"| {k} | {v} |" for k, v in c.most_common()]
        lines.append("")
    lines += ["## records per file", "", "| file | count |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in sorted(files.items())]
    print("\n".join(lines))
    return 0


def match(r, a):
    if a.kind and r.get("kind") != a.kind:
        return False
    if a.lang and r.get("lang") not in a.lang:
        return False
    if a.persona and r.get("persona") not in a.persona:
        return False
    if a.intent and r.get("intent") not in a.intent:
        return False
    if a.type and r.get("type") not in a.type:
        return False
    if a.topic and not set(a.topic) & set(r.get("topics") or []):
        return False
    if a.text:
        blob = " ".join(str(r.get(k, "")) for k in
                        ("title_original", "question_paraphrase", "prompt", "gloss_en", "answer_summary", "phrasing_notes"))
        if not re.search(a.text, blob, re.I):
            return False
    return True


def _cut(s, n=260):
    s = str(s or "").replace("\n", " ")
    return s if len(s) <= n else s[: n - 1] + "…"


def brief(r):
    body = _cut(r.get("question_paraphrase") or r.get("prompt") or "")
    title = _cut(r.get("title_original") or "", 140)
    head = f"[{r.get('id')}] ({r.get('lang')}/{r.get('kind')}/{r.get('persona')}/{r.get('intent')})"
    gloss = f"  EN: {_cut(r['gloss_en'], 200)}" if r.get("gloss_en") and r.get("lang") != "en" else ""
    url = r.get("source_url") or ""
    extra = ""
    if r.get("kind") == "real" and r.get("answer_summary"):
        extra = f"  ANSWER: {_cut(r['answer_summary'], 180)}"
    if r.get("kind") == "synthetic" and r.get("expected_behavior"):
        extra = f"  EXPECT: {_cut(r['expected_behavior'], 180)}"
    return f"{head} {title} | {body}{gloss}{extra} {url}".strip()


def cmd_filter(a):
    recs, _ = load(a.paths)
    hits = [r for r in recs if match(r, a)]
    print(f"# {len(hits)} matching records (showing {a.offset}..{a.offset + a.limit})")
    for r in hits[a.offset: a.offset + a.limit]:
        if a.format == "jsonl":
            print(json.dumps({k: v for k, v in r.items() if k != "_line"}, ensure_ascii=False))
        elif a.format == "md":
            print(f"- **{r.get('title_original') or r.get('id')}** ({r.get('lang')}) — "
                  f"{r.get('question_paraphrase') or r.get('prompt')} [source]({r.get('source_url', '')})")
        else:
            print(brief(r))
    return 0


def norm(s):
    return re.sub(r"\W+", " ", str(s or "").lower()).strip()


CSV_COLS_REAL = ["id", "lang", "type", "persona", "intent", "topics", "title_original", "question_paraphrase",
                 "gloss_en", "context_given", "software", "ifc_version", "tone", "phrasing_notes",
                 "answer_summary", "source_url", "source_type", "year", "raw_file"]
CSV_COLS_SYN = ["id", "lang", "type", "persona", "intent", "topics", "difficulty", "needs_file", "prompt",
                "gloss_en", "expected_behavior", "tone", "inspired_by", "raw_file"]


def write_csv(path, rows, cols):
    with open(path, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in rows:
            w.writerow(["; ".join(map(str, r.get(c))) if isinstance(r.get(c), list) else r.get(c, "") for c in cols])


def cmd_export(a):
    recs, errors = load(None)
    EXPORTS.mkdir(exist_ok=True)
    real, syn, seen_r, seen_s = [], [], set(), set()
    for r in recs:
        if problems(r):
            continue
        r = {k: v for k, v in r.items() if k != "_line"}
        if r["kind"] == "real":
            key = (r.get("source_url", "").split("#")[0].rstrip("/"), norm(r.get("question_paraphrase") or r.get("title_original"))[:80])
            if key in seen_r:
                continue
            seen_r.add(key)
            real.append(r)
        else:
            key = norm(r.get("prompt"))[:160]
            if key in seen_s:
                continue
            seen_s.add(key)
            syn.append(r)
    for name, rows in (("real_questions", real), ("synthetic_prompts", syn)):
        with open(EXPORTS / f"{name}.jsonl", "w", encoding="utf-8", newline="\n") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    write_csv(EXPORTS / "real_questions.csv", real, CSV_COLS_REAL)
    write_csv(EXPORTS / "synthetic_prompts.csv", syn, CSV_COLS_SYN)
    print(f"exported real={len(real)} synthetic={len(syn)} (skipped parse errors: {len(errors)})")
    return 0


def cmd_sections(a):
    """Print one section (by heading substring) from every MD report under research_raw (or given paths)."""
    pat = re.compile(r"^(#{1,3})\s+(.*)$")
    chunks = []
    for f in iter_files(a.paths, "*.md"):
        try:
            lines = f.read_text(encoding="utf-8-sig").splitlines()
        except Exception:
            continue
        grab, level, buf = False, 0, []
        for ln in lines:
            m = pat.match(ln)
            if m:
                if grab and len(m.group(1)) <= level:
                    break
                if not grab and a.heading.lower() in m.group(2).lower():
                    grab, level = True, len(m.group(1))
                    continue
            if grab:
                buf.append(ln)
        text = "\n".join(buf).strip()
        if text:
            chunks.append(f"=== {rel(f)} ===\n{text}\n")
    out = "\n".join(chunks)
    print(f"# {len(chunks)} sections, {len(out)} chars total (showing chars {a.offset}..{a.offset + a.max_chars})")
    print(out[a.offset: a.offset + a.max_chars])
    return 0


def add_filters(p):
    p.add_argument("paths", nargs="*")
    p.add_argument("--kind", choices=["real", "synthetic"])
    for opt in ("lang", "topic", "persona", "intent", "type"):
        p.add_argument(f"--{opt}", action="append")
    p.add_argument("--text")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate"); v.add_argument("paths", nargs="*")
    s = sub.add_parser("stats"); add_filters(s); s.add_argument("--md", action="store_true")
    f = sub.add_parser("filter"); add_filters(f)
    f.add_argument("--limit", type=int, default=60); f.add_argument("--offset", type=int, default=0)
    f.add_argument("--format", choices=["brief", "jsonl", "md"], default="brief")
    sc = sub.add_parser("sections"); sc.add_argument("heading"); sc.add_argument("paths", nargs="*")
    sc.add_argument("--max-chars", type=int, default=60000); sc.add_argument("--offset", type=int, default=0)
    sub.add_parser("export")
    a = ap.parse_args()
    return {"validate": cmd_validate, "stats": cmd_stats, "filter": cmd_filter, "export": cmd_export,
            "sections": cmd_sections}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
