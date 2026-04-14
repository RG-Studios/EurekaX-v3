from .hypothesis_generator import generate_hypotheses
from .memory import store_insight
from .scoring_engine import score_hypotheses


def run_engine(num_ideas: int = 5, memory_file: str = "eurekax_insights.json", verbose: bool = True):
    if verbose:
        print("🚀 EurekaX v3 – Autonomous Discovery Engine (TF-IDF Edition)\n")

    ideas = generate_hypotheses(num_ideas)
    results = []

    for idea in ideas:
        hypothesis, t1, t2, d1, d2 = idea
        scores = score_hypotheses(t1, t2)
        verdict = scores["verdict"]

        if verdict != "Rejected":
            store_insight(hypothesis, t1, t2, d1, d2, scores, memory_file=memory_file)

        if verbose:
            print(f"\n🧠 {hypothesis}")
            print(f"📈 Novelty: {scores['novelty']:.3f}")
            print(f"🔬 Feasibility: {scores['feasibility']:.3f}")
            print(f"📊 Final Score: {scores['final']:.3f}")
            print(f"🏆 Verdict: {verdict}")

        results.append(
            {
                "hypothesis": hypothesis,
                "topic_1": t1,
                "topic_2": t2,
                "domain_1": d1,
                "domain_2": d2,
                "scores": scores,
            }
        )

    return results
