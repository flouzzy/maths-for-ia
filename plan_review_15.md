1. **Localiser le Curseur de Relecture :**
   - Identifier via `README.md` et `Tableau de bord.md` que le Jalon précédent audité est le Jalon 14.
   - Le prochain jalon à auditer est **Jalon 15** ("Sous-suites, valeurs d'adhérence et preuve par séparation du théorème de Bolzano-Weierstrass").
2. **Exécuter le Protocole d'Audit & Enrichissement (.md) :**
   - Éradiquer le méta-commentaire (le bavardage IA, instructions de prompt) dans `jalon-15/Jalon-15.md` en supprimant les lignes en italique explicatives et en nettoyant les en-têtes inutiles.
   - Analyser qu'aucune "ellipse mathématique" (ex: "il est trivial", "laissé au lecteur") n'est présente dans les TPs et Exos du Jalon 15.
   - Refactoriser le contenu Markdown du Jalon 15 pour appliquer le Protocole d'Exégèse Conceptuelle: genèse narrative, énoncé et typage chirurgicaux, exemples et cas pathologiques.
3. **Compiler le Polycopié de Cours LaTeX :**
   - Modifier `compile_tex.py` pour produire un fichier source unique `jalon-15/jalon-15.tex` en s'assurant que le titre est correct (`Structure de R, axiome de la borne supérieure et propriété d'Archimède` ou le titre propre à Jalon 15).
   - Intégrer les sections de Cours, d'Exercices et de TPs.
   - Introduire un schéma TikZ vectoriel décrivant le théorème de Bolzano-Weierstrass ou l'extraction de sous-suites.
   - Compiler le code final en un fichier `jalon-15/jalon-15-polycopie.pdf` à l'aide de pdflatex.
4. **Mettre à jour le Tableau de Bord :**
   - Ajouter l'entrée datée de l'audit pour le Jalon 15 dans le `README.md` et le `Tableau de bord.md` dans l'ancre appropriée.
5. **Compléter les vérifications de pré-commit :**
   - Lancer les tests
   - Appeler request_code_review
   - Initier l'enregistrement mémoire
