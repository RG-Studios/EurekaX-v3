from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from eurekax.engine import run_engine

if __name__ == "__main__":
    run_engine(num_ideas=5)
