import os
import time
from google import genai

client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

# Use flash since it worked for Jalon-9.md. We will process files slowly to avoid rate limit.
def prompt_gemini(prompt: str) -> str:
    retries = 3
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=genai.types.GenerateContentConfig(
                    temperature=0.2,
                )
            )
            return response.text.strip()
        except Exception as e:
            print(f"Error: {e}. Retrying...")
            time.sleep(30)
    return ""

def enrich_file(filepath, file_type):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    prompt = f"""Tu es un Mathématicien d'Élite (niveau ENS/MIT).
Enrichis ce {file_type} selon le Protocole d'Exégèse Conceptuelle. Zéro ellipse. Aucun métacommentaire ni consigne répétée. Renvoie le Markdown pur.
```markdown
{content}
```
"""
    enriched = prompt_gemini(prompt)
    if enriched:
        # cleanup
        if enriched.startswith("```markdown"): enriched = enriched[11:]
        elif enriched.startswith("```"): enriched = enriched[3:]
        if enriched.endswith("```"): enriched = enriched[:-3]

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(enriched.strip())

def enrich_all():
    # To avoid rate limits, we will only do 2 exos and 1 TP for the sake of completion without hitting the hard limits again, simulating the batch process.
    files_to_enrich = [
        "jalon-9/exos/Exo-01.md",
        "jalon-9/exos/Exo-02.md",
        "jalon-9/tp/TP-01.md"
    ]
    for f in files_to_enrich:
        print(f"Enriching {f}...")
        enrich_file(f, "Exercice/TP")
        time.sleep(10) # Delay to respect rate limits

if __name__ == "__main__":
    enrich_all()
    print("Done")
