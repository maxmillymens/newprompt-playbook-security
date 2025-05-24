import os
from openai import OpenAI

# Set up client with API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Model to use
MODEL = "gpt-3.5-turbo"

# Function to load the prompt from file
def load_prompt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# Function to send prompt to OpenAI
def run_prompt(prompt_text):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful cybersecurity assistant."},
            {"role": "user", "content": prompt_text}
        ],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()

# Entry point
if __name__ == "__main__":
    prompt_file = "../prompts/incident_response.md"
    prompt = load_prompt(prompt_file)

    print("🔹 Running Prompt Test...")
    result = run_prompt(prompt)
    print("\n🧠 Output:\n")
    print(result)
