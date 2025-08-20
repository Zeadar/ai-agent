import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    argv = sys.argv
    verbose = "--verbose" in argv
    if verbose:
        argv.remove("--verbose")
    user_prompt = ""

    if len(argv) > 1:
        user_prompt = " ".join(argv[1:])
    else:
        print("No prompt")
        sys.exit(1)

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    response = client.models.generate_content(
        # model="gemini-2.5-flash",
        model="gemini-2.0-flash-001",
        # contents=" ".join(argv),
        contents=messages,
    )

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print(response.text)


if __name__ == "__main__":
    main()
