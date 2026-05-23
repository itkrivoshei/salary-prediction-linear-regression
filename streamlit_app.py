from __future__ import annotations

import sys
from pathlib import Path
from runpy import run_module

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.append(str(SRC))

if __name__ == "__main__":
    run_module("app", run_name="__main__")
