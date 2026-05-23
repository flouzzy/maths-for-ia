import os
import glob
import time
import sys
import re
from google import genai
from google.genai import types

# Récupération sécurisée du client Gemini API
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

# Le modèle recommandé pour un équilibre entre rapidité, fenêtres de contexte et qualité
MODEL_ID = 'gemini-2.5-flash'

def get_jalon_files():
    # Trouve tous les fichiers de Jalons
    files = glob.glob("Jalon *.md") + glob.glob("Jalons *.md")
    return sorted(files)

def parse_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraction sécurisée des informations de navigation
    parts = content.split('---\n')
    if len(parts) > 1:
        # Check if the first part is YAML frontmatter
        if content.startswith('---'):
            main_content = "---\n".join(parts[:-1]).strip()
        else:
            main_content = "---\n".join(parts[:-1]).strip()

        nav_links = parts[-1].strip()
        if not ("**Précédent**" in nav_links or "**Suivant**" in nav_links):
            main_content = content
            nav_links = ""
    else:
        main_content = content
        nav_links = ""

    lines = main_content.split('\n')
    title = lines[0].replace('# ', '') if lines and lines[0].startswith('# ') else os.path.basename(filepath).replace('.md', '')

    # Nettoyage rapide du titre pour le prompt
    title_clean = re.sub(r'Jalon \d+ \((.*?)\)', r'\1', title)
    title_clean = title_clean.replace("Jalon ", "").strip()

    return main_content, nav_links, title_clean

def generate_enriched_content(title, original_content, filepath):
    # Extraction du numéro de jalon depuis le nom du fichier pour le YAML
    match_num = re.search(r'Jalon\w* (\d+)', os.path.basename(filepath))
    jalon_num = match_num.group(1) if match_num else "0"

    prompt = f"""Tu es un Professeur Émérite de Mathématiques (niveau ENS / École Polytechnique / MIT) et un expert en Intelligence Artificielle.
Ta mission est de métamorphoser un jalon d'apprentissage brut en un module de cours magistral d'excellence absolue.

Voici le concept à traiter :
- Titre : {title}
- Numéro de Jalon : {jalon_num}
- Description initiale : {original_content}

---

### CONTRAINTES DE FORMATAGE ABSOLUES :
1. Renvoie DIRECTEMENT le bloc Markdown complet, sans introduction superflue ni salutations ("Voici le fichier...", "Bonjour...").
2. Utilise la syntaxe LaTeX standard : $...$ pour les mathématiques en ligne et $$...$$ pour les équations en bloc.
3. Rédige l'intégralité du contenu en français.

---

### STRUCTURE UNIVERSELLE STRICTE À RESPECTER :

```markdown
---
uuid: "jalon-{jalon_num}"
title: "{title}"
tags:
  - math/fondations
  - ia/theorie
---

# Jalon {jalon_num} : {title}

## 1. L'Intuition Première (Niveau 12 ans)
*Cette section doit rendre le concept physique, visuel ou métaphorique sans formalisme complexe.*
- **La Métaphore :** [Développer une analogie concrète ou une image mentale capturant l'essence du concept]
- **Le "Pourquoi on a inventé ça" :** [Expliquer le problème historique ou conceptuel résolu par ce concept]
- **Visualisation :** [Décrire ce qu'on verrait si on cartographiait cette idée]

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence des classes préparatoires MP / ENS / MIT.*

### A. Définitions Formelles
[Donner toutes les définitions de manière ultra-exhaustive. Spécifier systématiquement la nature de tous les objets : corps $\\mathbb{{K}}$, espaces $E$, etc.]

### B. Théorèmes, Propositions & Lemmes
> **Théorème Fondamental :**
> Soient [Hypothèses explicites et restrictives]. Alors :
> $$[Équation ou propriété formelle]$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Règle d'or : INTERDICTION ABSOLUE d'écrire "par une récurrence immédiate" ou "le calcul se fait sans peine". Écris CHAQUE ligne de calcul intermédiaire, chaque interversion de symbole, chaque majoration.*

### Démonstration Pivot
1. **Initialisation / Cadre :** [Poser la stratégie de preuve]
2. **Développement :** [Explications textuelles précises combinées aux lignes micro-calculatoires successives]

## 4. Exercices d'Application & Pratique de Concours
*Proposer au moins 2 exercices progressifs : un calculatoire direct, un extrait ou inspiré de grands concours (X/ENS/MIT) corrigé sans aucune ellipse.*

### Exercice 1 : [Titre]
**Énoncé :** [...]
**Correction Détaillée :** [...]

### Exercice 2 : [Titre - Niveau Avancé X/ENS]
**Énoncé :** [...]
**Correction Détaillée :** [...]

## 5. Alignement & Point d'Ancrage IA
*Expliquer comment ce concept s'articule explicitement dans les architectures IA modernes (Transformers, optimisation, GANs, embeddings, etc.).*
- **Le Pont Théorique :** [Explication du lien]
- **Exemple Concret :** [Cas d'usage précis algorithmique ou architectural]
```"""

    max_retries = 10
    retry_delay = 60

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.3, # Température basse pour maximiser la rigueur mathématique
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

        # On vérifie si le fichier possède déjà la nouvelle structure YAML pour éviter de le refaire
        with open(filepath, 'r', encoding='utf-8') as f:
            first_lines = "".join([f.readline() for _ in range(5)])
            if "uuid: \"jalon-" in first_lines:
                print(f"  -> Le fichier {filepath} possède déjà la nouvelle structure YAML. Ignoré.")
                sys.stdout.flush()
                continue

        # Fallback de taille au cas où
        if os.path.getsize(filepath) > 15000:
            print(f"  -> Le fichier {filepath} semble déjà enrichi. Ignoré.")
            sys.stdout.flush()
            continue

        original_content, nav_links, title = parse_file(filepath)

        enriched_text = generate_enriched_content(title, original_content, filepath)

        if enriched_text:
            # Nettoyage des balises de code Markdown parasites si le modèle en ajoute
            clean_text = enriched_text
            if clean_text.startswith("```markdown"):
                clean_text = clean_text[11:]
            if clean_text.endswith("```"):
                clean_text = clean_text[:-3]
            clean_text = clean_text.strip()

            new_content = clean_text + "\n\n"
            if nav_links:
                new_content += "---\n" + nav_links + "\n"

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"  -> Succès: fichier enrichi et sauvegardé {filepath}")
        else:
            print(f"  -> Échec: impossible d'enrichir {filepath}")
        sys.stdout.flush()

        # Modération des requêtes pour préserver le quota standard
        time.sleep(5)

    print("Processus d'enrichissement terminé avec succès.")

if __name__ == "__main__":
    main()
