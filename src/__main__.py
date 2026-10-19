import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Natural language to function call")
    parser.add_argument(
        "--functions_definition",
        type=Path,
        default=Path("data/input/functions_definition.json"),
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/input/function_calling_tests.json"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/output/function_calling_results.json"),
    )
    args = parser.parse_args()
    print(args) #replace once the pipeline exists


if __name__ == "__main__":
    main()
