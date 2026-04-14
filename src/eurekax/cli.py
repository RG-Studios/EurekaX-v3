import argparse

from .engine import run_engine


def build_parser():
    parser = argparse.ArgumentParser(
        prog="eurekax",
        description="EurekaX v3 - Autonomous cross-domain hypothesis discovery engine",
    )
    parser.add_argument(
        "--num-ideas",
        type=int,
        default=5,
        help="Number of hypotheses to generate (default: 5)",
    )
    parser.add_argument(
        "--memory-file",
        default="eurekax_insights.json",
        help="Path to JSON file where accepted insights are stored",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress console output and only execute generation/scoring pipeline",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    run_engine(
        num_ideas=args.num_ideas,
        memory_file=args.memory_file,
        verbose=not args.quiet,
    )


if __name__ == "__main__":
    main()
