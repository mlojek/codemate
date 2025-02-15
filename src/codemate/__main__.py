"""
CLI entrypoint for codemate.
"""

import argparse
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain.llms.openai import OpenAI
from langchain.schema import HumanMessage
from langchain_openai import ChatOpenAI

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
    parser.add_argument(
        "--from_line", help="The line number in the source file to start from."
    )
    parser.add_argument(
        "--to_line", help="The line number in the source file to end at."
    )
    parser.add_argument(
        "--inplace",
        action="store_true",
        help="If used the result will be pasted into the source file instead of the console.",
    )
    args = parser.parse_args()

    print(f"Selected option {args.action} on file {args.source_file}")

    # read the configfile
    status = load_dotenv(Path.home() / ".codemate")
    print(status)
    print(os.getenv("MESSAGE"))

    # create prompt template and llm instance
    # fav_llm in config, flag to select llm

    # llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv('OPENAI_API_KEY'))
    from langchain.schema import HumanMessage
    from langchain_google_genai import ChatGoogleGenerativeAI

    # Set up Gemini model in LangChain
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro", google_api_key=os.getenv("GEMINI_API_KEY")
    )
    response = llm.invoke([HumanMessage(content="Hello, what's your name?")])
    print(response.content)

    # read the source file
    # prompt the llm
    # append the result to the source file
