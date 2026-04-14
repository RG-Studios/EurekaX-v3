import json
from datetime import datetime
from pathlib import Path
from uuid import uuid4

DEFAULT_MEMORY_FILE = "eurekax_insights.json"


def store_insight(hypothesis, t1, t2, d1, d2, scores, memory_file: str = DEFAULT_MEMORY_FILE):
    insight = {
        "id": str(uuid4()),
        "timestamp": datetime.now().isoformat(),
        "hypothesis": hypothesis,
        "topic_1": t1,
        "topic_2": t2,
        "domain_1": d1,
        "domain_2": d2,
        "novelty": scores["novelty"],
        "feasibility": scores["feasibility"],
        "score": scores["final"],
        "verdict": scores["verdict"],
    }

    file_path = Path(memory_file)
    if not file_path.exists():
        file_path.write_text(json.dumps([insight], indent=2), encoding="utf-8")
        return

    raw = file_path.read_text(encoding="utf-8").strip()
    loaded = json.loads(raw) if raw else []
    if isinstance(loaded, list):
        data = loaded
    elif isinstance(loaded, dict):
        data = [loaded]
    else:
        data = []
    data.append(insight)
    file_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
