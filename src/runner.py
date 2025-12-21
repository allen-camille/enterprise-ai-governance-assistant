from pathlib import Path

def load_system_prompt() -> str:
    prompt_path = Path("prompts/system_prompt.txt")
    return prompt_path.read_text(encoding="utf-8")

def main():
    system_prompt = load_system_prompt()
    print("Systemprompt laddad OK.")
    print("-----")
    print(system_prompt)

if __name__ == "__main__":
    main()
