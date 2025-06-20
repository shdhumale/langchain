import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

def main() -> None:
    """
    Initializes the Google Generative AI model, sends a prompt,
    and prints the response.
    """
    # Load environment variables from .env file if available
    load_dotenv()

    # Get your Google API key from environment variables
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        raise ValueError(
            "Google API key not found. Set the GOOGLE_API_KEY environment variable "
            "or ensure it's in your .env file."
        )

    # Initialize the Gemini model
    # Note: "gemini-2.5-flash-preview-05-20" is an unusual model name.
    # Please ensure this is a valid model ID.
    # Common models include "gemini-1.5-flash-latest", "gemini-1.5-pro-latest",
    # or preview models like "gemini-1.5-flash-preview-0514".
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-preview-05-20",
        google_api_key=google_api_key,
        temperature=0.7,
        max_output_tokens=512,  # Corrected parameter name from max_tokens
    )

    # Define a conversation
    messages = [
        ("system", "You are a helpful assistant that speaks like a pirate."),
        ("human", "What be the capital o' France, me hearty?"),
    ]

    # Invoke the model and print the response
    try:
        response = llm.invoke(messages)
        print("Gemini Response:", response.content)
    except Exception as e:
        print(f"An error occurred while invoking the model: {e}")

if __name__ == "__main__":
    main()