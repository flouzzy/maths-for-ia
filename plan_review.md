The plan is to apply the "Protocole d'Exégèse Conceptuelle" to `jalon-21` (Suites de fonctions).
1. Read the target Jalon: `jalon-21/Jalon-21.md`, all exercises `jalon-21/exos/Exo-*.md`, and all TP `jalon-21/tp/TP-*.md`.
2. Rewrite `jalon-21/Jalon-21.md` with:
   - Part 1: "Intuition et genèse du concept" (Thurston-like narrative).
   - Part 2: "Formalisation et structures algébriques" (Definitions, precise typing).
   - Part 3: "Démonstrations pas-à-pas" (Zero ellipse).
3. Update `jalon-21/exos/*.md` and `jalon-21/tp/*.md` as needed. The instructions mention to "éradiquer le survol théorique" and rewrite the exercises to ensure they are exhaustive and without ellipses. Given the memory, I should use regex substitution or targeted rewriting to eliminate meta-commentary, but I should probably just rebuild a full LaTeX file from the markdown contents as instructed for the compilation phase. Wait, the instructions say to "pratiquer un refactoring en profondeur directement dans les fichiers Markdown sources". So I need to write a Python script that uses `google.genai` to rewrite the MD files to be extremely exhaustive and rigorous, but since API usage is tricky due to quotas, I might write a script that does surgical replacements of certain parts, or if I have to use Gemini, I should chunk it. Wait, memory says "The google.genai module is not pre-installed... fallback to fully hardcoded content generation scripts to avoid ModuleNotFoundError". I'll hardcode the content for Jalon 21.
4. After updating `.md` files, write a script to compile `jalon-21.tex` combining:
   - Part 1: Intuition (from Jalon-21.md)
   - Part 2: Formalisation (from Jalon-21.md)
   - Part 3: Demonstrations (from Jalon-21.md)
   - Part 4: Exercices d'application (from exos/*.md)
   - Part 5: Travaux pratiques (from tp/*.md)
   - Ensure native TikZ is included.
   - Clean up undefined macros, escape python code in `\begin{lstlisting}`, replace `.md` headers with LaTeX sections.
5. Compile `jalon-21.tex` to `jalon-21/jalon-21-polycopie.pdf` using `pdflatex`.
6. Update `README.md` and `Tableau de bord.md` with the new Audit history.
   Format for README.md & Tableau de bord.md:
   `### 2026-07-17-audit`
   `- [[#2026-07-17-audit|2026-07-17]] : [Audit & Weekly Compilation] - Jalon 21 - Suites de fonctions. Fichiers Obsidian .md nettoyés et enrichis, intégration des schémas TikZ vectoriels et génération du polycopié PDF d'étude. Statut : Validé et Fixé.`
7. Complete pre-commit steps.
8. Submit.
