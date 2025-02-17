"""
CLI entrypoint for codemate.
"""

import argparse
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain.schema import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Codemate: LLM-powered software developer assistant.",
        prog="python -m codemate",
    )
    parser.add_argument(
        "action",
        choices=["refactor", "explain", "document", "insert"],
        help="Action that the assistant should take.",
    )
    parser.add_argument(
        "source_file", type=Path, help="Path to the source file to work on."
    )
    parser.add_argument(
        "--from_line",
        type=int,
        default=0,
        help="The line number (starting from 0) in the source file to start from.",
    )
    parser.add_argument(
        "--to_line",
        type=int,
        default=-1,
        help="The line number (starting from 0) in the source file to end before.",
    )
    parser.add_argument(
        "--api",
        choices=["gemini", "openai"],
        default="gemini",
        help="Which LLM API to use.",
    )
    parser.add_argument("--model", type=str, help="Name of LLM to use.")
    parser.add_argument(
        "--inplace",
        action="store_true",
        help="If used the result will be pasted into the source file instead of the console.",
    )
    args = parser.parse_args()

    # read the configfile
    assert load_dotenv(
        Path.home() / ".codemate"
    ), "Could not find ~/.codemate config file."

    # create llm instance
    match args.api:
        case "gemini":
            model_name = args.model or os.getenv("GEMINI_FAV_MODEL", "gemini-1.5-pro")
            llm = ChatGoogleGenerativeAI(
                model=model_name, google_api_key=os.getenv("GEMINI_API_KEY")
            )
        case "openai":
            model_name = args.model or os.getenv("OPENAI_FAV_MODEL", "gpt-4o")
            llm = ChatOpenAI(model=model_name, api_key=os.getenv("OPENAI_API_KEY"))

    # read the source file
    with open(args.source_file, "r", encoding="utf-8") as file_handle:
        source_file_content = file_handle.read().splitlines()

    # create prompt template
    system_message_template = PromptTemplate.from_template(
        "You are a bot that performs operations on source code. "
        "Your task is to {detailed_instruction} the source code. "
        "You shall return only source code.",
    )

    instructions = {
        "refactor": "refactor",
        "document": "add docstrings and typehints to",
        "explain": "add explaination comments to",
        "insert": "add code according to the comments",
    }

    messages = [
        SystemMessage(
            content=system_message_template.format(
                detailed_instruction=instructions[args.action]
            )
        ),
        HumanMessage(content=source_file_content[args.from_line : args.to_line]),
    ]

    # prompt the llm
    llm_response = llm.invoke(messages)

    # remove markdown code block artifacts
    llm_response_split = [
        line for line in llm_response.content.splitlines() if not line.startswith("```")
    ]

    # append the result to the source file
    if args.inplace:
        source_file_new_content = (
            source_file_content[: args.from_line]
            + llm_response_split
            + source_file_content[args.to_line :]
        )
        with open(args.source_file, "w", encoding="utf-8") as file_handle:
            file_handle.write("\n".join(source_file_new_content))
    else:
        print("\n".join(llm_response_split))
