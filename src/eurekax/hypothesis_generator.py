import random

from .data import KNOWLEDGE_BASE


def generate_hypotheses(n: int = 5):
    ideas = []
    domains = list(KNOWLEDGE_BASE.keys())
    for _ in range(n):
        d1, d2 = random.sample(domains, 2)
        t1 = random.choice(KNOWLEDGE_BASE[d1])
        t2 = random.choice(KNOWLEDGE_BASE[d2])
        hypothesis = f"Can we apply '{t1}' from {d1} to solve '{t2}' in {d2}?"
        ideas.append((hypothesis, t1, t2, d1, d2))
    return ideas
