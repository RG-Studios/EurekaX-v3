from hypothesis_generator import generate_hypotheses
from scoring_engine import score_hypotheses
from memory import store_insight
import json

def run_engine(num_ideas=5):
    print("🚀 EurekaX v3 – Autonomous Discovery Engine (TF-IDF Edition)\n")

    ideas = generate_hypotheses(num_ideas)
    scored = []

    for idea in ideas:
        hypothesis, t1, t2, d1, d2 = idea
        scores = score_hypotheses(t1, t2)
        score = scores["final"]
        verdict = scores["verdict"]

        if verdict != "Rejected":
            store_insight(hypothesis, t1, t2, d1, d2, scores)
        scored.append((hypothesis, scores))

        print(f"\n🧠 {hypothesis}")
        print(f"📈 Novelty: {scores['novelty']:.3f}")
        print(f"🔬 Feasibility: {scores['feasibility']:.3f}")
        print(f"📊 Final Score: {scores['final']:.3f}")
        print(f"🏆 Verdict: {verdict}")

if __name__ == "__main__":
    run_engine(num_ideas=5)
