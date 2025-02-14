"""
CLI entrypoint for codemate.
"""

import argparse
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Codemate: LLM-powered software developer assistant."
    )
    parser.add_argument(
        "action",
        choices=["refactor", "explain", "document", "setup"],
        help="Action that the assistant should take.",
    )
    parser.add_argument(
        "source_file", type=Path, help="Path to the source file to work on."
    )
    # parser.add_argument('--from_line')
    # parser.add_argument('--to_line')
    # parser.add_argument('--inplace')
    args = parser.parse_args()

    print(f"Selected option {args.action} on file {args.source_file}")
