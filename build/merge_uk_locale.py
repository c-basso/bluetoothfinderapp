#!/usr/bin/env python3
# Merge uk_locale.UK into uk.json (structure from pl.json).
import json
from pathlib import Path

B = Path(__file__).parent
pl = json.loads((B / "pl.json").read_text(encoding="utf-8"))
from uk_locale import UK  # noqa: E402

out = json.loads(json.dumps(pl))
for k, v in UK.items():
    if k in ("app_info", "footer", "final_cta") and isinstance(v, dict) and isinstance(
        out.get(k), dict
    ):
        out[k] = {**out[k], **v}
    else:
        out[k] = v

(B / "uk.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("Wrote uk.json", (B / "uk.json").stat().st_size)
