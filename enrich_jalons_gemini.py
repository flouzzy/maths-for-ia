import os
import glob
import time
import sys
from google import genai
from google.genai import types

# Assurez-vous que la clé API est bien définie dans votre environnement :
# export GOOGLE_API_KEY="votre_cle_api"
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

# Le modèle recommandé pour un équilibre entre rapidité et qualité
MODEL_ID = 'gemini-2.5-flash'

def get_jalon_files():
    # Trouve tous les fichiers de Jalons
    files = glob.glob("Jalon *.md") + glob.glob("Jalons *.md")
    return sorted(files)

def parse_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraction des liens de navigation en bas du fichier original
    parts = content.split('---\n')

    if len(parts) > 1:
        main_content = "---\n".join(parts[:-1]).strip()
        nav_links = parts[-1].strip()
    else:
        main_content = content
        nav_links = ""

    lines = main_content.split('\n')
    title = lines[0].replace('# ', '') if lines and lines[0].startswith('# ') else os.path.basename(filepath).replace('.md', '')

    return main_content, nav_links, title

def generate_enriched_content(title, original_content):
    prompt = f"""Tu es un professeur de mathématiques exceptionnel, capable d'expliquer les concepts les plus avancés à la fois avec une simplicité enfantine et une rigueur de niveau recherche.

Voici le concept mathématique à détailler (Jalon du cours) :
Titre : {title}
Contexte et description originale :
{original_content}

Ta mission :
Détailler ce cours de manière ultra exhaustive pour qu'il permette au lecteur de passer d'un niveau Bac S à un niveau Master de Mathématiques (niveau X, ENS, MIT).

Contraintes absolues :
1. L'introduction doit rendre le concept compréhensible même par un enfant de 12 ans (métaphores, intuition visuelle).
2. Ne sacrifie AUCUNE rigueur mathématique dans le corps du texte.
3. Sois ULTRA exhaustif.
4. Inclus obligatoirement :
   - Des définitions formelles.
   - Des théorèmes importants avec leurs hypothèses précises.
   - Des démonstrations RIGOUREUSES et PAS À PAS (ne saute aucune étape, "il n'y a pas de petite explication").
   - Des exercices d'application corrigés en détail.
5. Utilise le format Markdown avec la syntaxe LaTeX classique pour les mathématiques (utilises $...$ pour les maths en ligne et $$...$$ pour les équations en bloc).
6. Le ton doit être pédagogique, encourageant, mais d'une exigence académique absolue.

Rédige le contenu complet de ce cours en français. Ne réécris pas le titre principal (je l'ajouterai)."""

    max_retries = 10
    retry_delay = 60  # On attend 1 minute en cas de quota dépassé

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.7,
                )
            )
            return response.text
        except Exception as e:
            error_msg = str(e)
            if "RESOURCE_EXHAUSTED" in error_msg or "429" in error_msg:
                print(f"Limite d'API atteinte (Rate Limit). Attente de {retry_delay}s... (Essai {attempt+1}/{max_retries})")
                sys.stdout.flush()
                time.sleep(retry_delay)
            else:
                print(f"Erreur lors de la génération de contenu pour {title}: {e}")
                return None

    print(f"Échec après {max_retries} tentatives pour le jalon {title}.")
    return None

def main():
    if not os.environ.get("GOOGLE_API_KEY"):
        print("Erreur: La variable d'environnement GOOGLE_API_KEY n'est pas définie.")
        sys.exit(1)

    print("Démarrage du processus d'enrichissement...")
    sys.stdout.flush()
    files = get_jalon_files()
    print(f"{len(files)} fichiers trouvés.")
    sys.stdout.flush()

    for i, filepath in enumerate(files):
        print(f"Traitement {i+1}/{len(files)}: {filepath}")
        sys.stdout.flush()

        # On ignore les fichiers déjà enrichis (ceux qui dépassent ~3000 octets)
        if os.path.getsize(filepath) > 5000:
            print(f"  -> Le fichier {filepath} semble déjà enrichi (taille {os.path.getsize(filepath)} octets). Ignoré.")
            sys.stdout.flush()
            continue

        original_content, nav_links, title = parse_file(filepath)

        enriched_text = generate_enriched_content(title, original_content)

        if enriched_text:
            new_content = f"# {title}\n\n"
            new_content += enriched_text.strip() + "\n\n"
            if nav_links:
                new_content += "---\n" + nav_links + "\n"

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"  -> Succès: fichier enrichi et sauvegardé {filepath}")
        else:
            print(f"  -> Échec: impossible d'enrichir {filepath}")
        sys.stdout.flush()

        # Pause de base pour éviter de spammer l'API
        time.sleep(5)

    print("Processus d'enrichissement terminé avec succès.")

if __name__ == "__main__":
    main()
