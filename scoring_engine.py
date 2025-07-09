import random
from embeddings import calculate_novelty

def simulate_feasibility(t1, t2):
    keywords = ["optimization", "learning", "control", "decision", "model"]
    match_count = sum(k in t1.lower() + t2.lower() for k in keywords)
    return round(0.4 + 0.1 * match_count + random.uniform(0.0, 0.3), 3)

def score_hypotheses(t1, t2):
    novelty = calculate_novelty(t1, t2)
    feasibility = simulate_feasibility(t1, t2)
    final_score = round((novelty * 0.6 + feasibility * 0.4), 3)

    if final_score >= 0.75:
        verdict = "Breakthrough"
    elif final_score >= 0.6:
        verdict = "Promising"
    elif final_score >= 0.4:
        verdict = "Uncertain"
    else:
        verdict = "Rejected"

    return {
        "novelty": novelty,
        "feasibility": feasibility,
        "final": final_score,
        "verdict": verdict
    }
