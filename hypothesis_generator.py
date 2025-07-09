import random

knowledge_base = {
    "AI": [
        "transformers for text understanding",
        "reinforcement learning for robotics",
        "generative models for simulation"
    ],
    "Aerospace": [
        "satellite attitude dynamics",
        "multi-stage rocket propulsion",
        "hypersonic aerodynamic testing"
    ],
    "Neuroscience": [
        "synaptic plasticity in learning",
        "neuron firing signal processing",
        "brain-inspired decision systems"
    ],
    "Quantum Computing": [
        "qubit entanglement simulation",
        "superposition for optimization",
        "quantum tunneling in computation"
    ]
}

def generate_hypotheses(n=5):
    ideas = []
    for _ in range(n):
        d1, d2 = random.sample(list(knowledge_base.keys()), 2)
        t1 = random.choice(knowledge_base[d1])
        t2 = random.choice(knowledge_base[d2])
        hypothesis = f"Can we apply '{t1}' from {d1} to solve '{t2}' in {d2}?"
        ideas.append((hypothesis, t1, t2, d1, d2))
    return ideas
