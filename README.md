# EurekaX v3

EurekaX v3 is an autonomous cross-domain discovery engine that generates, scores, and stores hypothesis ideas across scientific and technical domains.

## Overview

The engine combines domain topics, estimates novelty using TF-IDF cosine similarity, simulates feasibility, and ranks each idea using a weighted score.

Core capabilities:
- Cross-domain hypothesis generation
- Novelty scoring from semantic distance
- Feasibility simulation from keyword heuristics
- Verdict classification (`Breakthrough`, `Promising`, `Uncertain`, `Rejected`)
- Persistent JSON memory for accepted insights

## Enterprise-Oriented Project Structure

```text
EurekaX-v3/
├── src/
│   └── eurekax/
│       ├── __init__.py
│       ├── cli.py
│       ├── data.py
│       ├── embeddings.py
│       ├── engine.py
│       ├── hypothesis_generator.py
│       ├── memory.py
│       └── scoring_engine.py
├── tests/
│   └── test_core.py
├── main.py
├── pyproject.toml
├── requirements.txt
└── .gitignore
```

This layout separates source code, tests, and runtime entrypoints to support maintainability and team-scale development.
`eurekax_insights.json` is generated/updated at runtime by the memory layer.

## Architecture

1. **Hypothesis Generator** selects two different domains and composes a candidate hypothesis.
2. **Novelty Engine** computes TF-IDF vectors for paired topics and converts similarity to novelty.
3. **Scoring Engine** blends novelty and feasibility into a final score.
4. **Memory Layer** stores non-rejected insights as structured JSON records.
5. **CLI/Entrypoint** drives execution for local runs and automation.

## Installation

### Option A: quick install

```bash
pip install -r requirements.txt
```

### Option B: package install (recommended)

```bash
pip install -e .
```

## Usage

### Run legacy entrypoint

```bash
python main.py
```

### Run package CLI

```bash
python -m eurekax.cli --num-ideas 5
```

Or, after editable install:

```bash
eurekax --num-ideas 5 --memory-file eurekax_insights.json
```

### CLI options

- `--num-ideas` number of hypotheses to generate
- `--memory-file` output JSON file for accepted insights
- `--quiet` suppress console output

## Testing

Run unit tests with:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p "test_*.py" -v
```

## Output Format

Accepted insights are appended to `eurekax_insights.json` with:
- unique ID
- timestamp
- source domains/topics
- novelty, feasibility, final score
- verdict

## Roadmap

- Replace heuristic feasibility with model-driven estimation
- Add configurable domain packs and plugin-based data sources
- Add CI workflows, linting, and release automation
- Add API service layer for remote execution
