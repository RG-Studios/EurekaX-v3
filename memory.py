import json
import os
from uuid import uuid4
from datetime import datetime

MEMORY_FILE = "eurekax_insights.json"

def store_insight(hypothesis, t1, t2, d1, d2, scores):
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
        "verdict": scores["verdict"]
    }

    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump([insight], f, indent=2)
    else:
        with open(MEMORY_FILE, "r+") as f:
            data = json.load(f)
            data.append(insight)
            f.seek(0)
            json.dump(data, f, indent=2)
