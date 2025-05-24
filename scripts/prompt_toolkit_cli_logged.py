import os
import openai
from datetime import datetime

# Set up API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

import json

with open("../prompts/manifest.json", "r") as f:
    manifest = json.load(f)

print("📚 Prompt Engineering Toolkit CLI")
print("Select a prompt to run:\n")

for i, item in enumerate(manifest, start=1):
    print(f"[{i}] {item['name']}")

choice = int(input("\nEnter choice: ")) - 1
prompt_file = f"../prompts/{manifest[choice]['file']}"


def load_prompt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Prompt file not found: {file_path}")
        return None

def run_prompt(prompt_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful cybersecurity assistant."},
                {"role": "user", "content": prompt_text}
            ],
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

def save_output(prompt_name, content):
    os.makedirs("../logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"../logs/{prompt_name.lower().replace(' ', '_')}_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"📁 Output saved to: {filename}")

def save_json_log(prompt_name, prompt_text, response_text, model="gpt-3.5-turbo"):
    log_data = {
        "prompt_name": prompt_name,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "model": model,
        "prompt_text": prompt_text,
        "response": response_text
    }
    filename = f"../logs/{prompt_name.lower().replace(' ', '_')}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=4)

def main():
    print("🧠 Prompt Engineering Toolkit CLI")
    print("Select a prompt to run:\n")
    for i, item in enumerate(manifest, start=1):
        print(f"[{i}] {item['name']}")

    try:
        choice = int(input("\nEnter choice: ")) - 1
        selected = manifest[choice]
    except (ValueError, IndexError):
        print("❌ Invalid selection.")
        return

    title = selected['name']
    path = f"../prompts/{selected['file']}"

    print(f"\n📄 Loading '{title}'...\n")
    prompt = load_prompt(path)

    if prompt:
        print("🚀 Sending prompt to OpenAI...\n")
        output = run_prompt(prompt)
        print("\n✅ Output:\n")
        print(output)
        save_output(title, output)
        save_json_log(title, prompt, output)

if __name__ == "__main__":
    main()
