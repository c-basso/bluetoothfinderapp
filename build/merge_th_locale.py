#!/usr/bin/env python3
# Merge th_locale.TH into th.json (structure from pl.json).
import json
from pathlib import Path

B = Path(__file__).parent
pl = json.loads((B / "pl.json").read_text(encoding="utf-8"))
from th_locale import TH  # noqa: E402

out = json.loads(json.dumps(pl))
for k, v in TH.items():
    if k in ("app_info", "footer", "final_cta") and isinstance(v, dict) and isinstance(
        out.get(k), dict
    ):
        out[k] = {**out[k], **v}
    else:
        out[k] = v

(B / "th.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Wrote th.json", (B / "th.json").stat().st_size)
