#!/usr/bin/env python3
# Merge tr_locale.TR into tr.json (structure from pl.json).
import json
from pathlib import Path

B = Path(__file__).parent
pl = json.loads((B / "pl.json").read_text(encoding="utf-8"))
from tr_locale import TR  # noqa: E402

out = json.loads(json.dumps(pl))
for k, v in TR.items():
    if k in ("app_info", "footer", "final_cta") and isinstance(v, dict) and isinstance(
        out.get(k), dict
    ):
        out[k] = {**out[k], **v}
    else:
        out[k] = v

(B / "tr.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Wrote tr.json", (B / "tr.json").stat().st_size)
