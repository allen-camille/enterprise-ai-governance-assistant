import os
from datetime import datetime
from openai import AzureOpenAI
from dotenv import load_dotenv

# --- Ladda miljövariabler ---
load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

DEPLOYMENT_NAME = "gpt-4.1"  # eller exakt ditt deployment-namn

# --- Läs systemprompt ---
with open("prompts/system_prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

# --- Initiera historik ---
messages = [{"role": "system", "content": system_prompt}]


def render_alt2(history_messages):
    """Genererar Alternativ 2: sammanfattning + statusbild för beslutsfattare."""
    now_local = datetime.now().strftime("%Y-%m-%d %H:%M (lokal tid)")

    alt2_instruction = f"""
Du ska skapa en STATUSBILD för beslutsfattare baserat ENBART på chatthistoriken.

Krav:
- Inkludera alltid dessa tre rader först:
  Status per:
  Informationskälla:
  Bedömd informationsnivå:

- Sätt:
  Status per: {now_local}
  Informationskälla: Användaruppgift
  Bedömd informationsnivå: Otillräcklig för riskklassning

- Struktur efter det:
  STATUSBILD – INCIDENT
  1. Bekräftade fakta
  2. Kända osäkerheter
  3. Öppna punkter

Regler:
- Gör inga rekommendationer och fatta inga beslut.
- Om info saknas: skriv tydligt att den saknas.
- Håll det kort, tydligt och “executive-friendly”.
"""

    temp_messages = history_messages + [{"role": "user", "content": alt2_instruction}]

    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=temp_messages,
        temperature=0.0,
    )
    return response.choices[0].message.content


print("Chat startad (Azure OpenAI med historik).")
print("Skriv 'exit' för att avsluta. Skriv 'alt2' för statusbild/sammanfattning.\n")

while True:
    user_input = input("Du: ").strip()
    cmd = user_input.lower()

    if cmd == "exit":
        print("Avslutar.")
        break

    # Alternativ 2: statusbild för beslutsfattare
    if cmd == "alt2":
        alt2_text = render_alt2(messages)
        print("\nAI (ALT2):")
        print(alt2_text)
        print()
        # Valfritt: spara alt2 i historiken
        messages.append({"role": "assistant", "content": alt2_text})
        continue

    # Vanlig chat: lägg till användarens meddelande i historiken
    messages.append({"role": "user", "content": user_input})

    # Anropa modellen med HELA historiken
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=messages,
        temperature=0.0,
    )

    assistant_reply = response.choices[0].message.content

    # Lägg till AI-svaret i historiken
    messages.append({"role": "assistant", "content": assistant_reply})

    print("\nAI:")
    print(assistant_reply)
    print()

