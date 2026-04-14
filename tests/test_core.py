import json
import tempfile
import unittest
from pathlib import Path

from eurekax.hypothesis_generator import generate_hypotheses
from eurekax.memory import store_insight
from eurekax.scoring_engine import score_hypotheses


class TestEurekaXCore(unittest.TestCase):
    def test_generate_hypotheses_count_and_domain_pairing(self):
        ideas = generate_hypotheses(4)
        self.assertEqual(len(ideas), 4)
        for hypothesis, t1, t2, d1, d2 in ideas:
            self.assertTrue(hypothesis)
            self.assertTrue(t1)
            self.assertTrue(t2)
            self.assertNotEqual(d1, d2)

    def test_score_hypotheses_has_expected_keys_and_ranges(self):
        scores = score_hypotheses(
            "transformers for text understanding",
            "brain-inspired decision systems",
        )
        self.assertIn("novelty", scores)
        self.assertIn("feasibility", scores)
        self.assertIn("final", scores)
        self.assertIn("verdict", scores)
        self.assertGreaterEqual(scores["novelty"], 0.0)
        self.assertLessEqual(scores["novelty"], 1.0)
        self.assertGreaterEqual(scores["final"], 0.0)
        self.assertLessEqual(scores["final"], 1.0)

    def test_store_insight_appends_records(self):
        with tempfile.TemporaryDirectory() as tmp:
            memory_file = Path(tmp) / "insights.json"
            scores = {"novelty": 0.8, "feasibility": 0.7, "final": 0.76, "verdict": "Breakthrough"}
            store_insight("h1", "t1", "t2", "d1", "d2", scores, memory_file=str(memory_file))
            store_insight("h2", "t3", "t4", "d3", "d4", scores, memory_file=str(memory_file))
            data = json.loads(memory_file.read_text(encoding="utf-8"))
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]["hypothesis"], "h1")
            self.assertEqual(data[1]["hypothesis"], "h2")


if __name__ == "__main__":
    unittest.main()
