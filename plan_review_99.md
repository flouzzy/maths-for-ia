1. **Target Identification:** Identify `jalon-99` as the next incomplete milestone in `Tableau de bord.md` and `README.md`.
2. **File Cleanup and Preparation:**
    - Read `jalon-99/Jalon 99 (Théorème de Hahn-Banach).md`.
    - Apply cleanup rules: remove meta-titles (like 'La Métaphore :', 'Le Pourquoi on a inventé ça :', 'Visualisation :'), ensure 'Zéro Ellipse' (exhaustive mathematical rigor), and add concrete examples after theorems.
    - Rename the main file to the standard format `Jalon-99.md`.
3. **Content Enrichment (Exercises and TPs):**
    - Generate 10 markdown files for exercises (`jalon-99/exos/Exo-01.md` to `Exo-10.md`) with progressive difficulty using `\bigstar` inside inline math `$ $`. Ensure rigorous, step-by-step corrections.
    - Generate 5 markdown files for TPs (`jalon-99/tp/TP-01.md` to `TP-05.md`) containing pure Python code without LaTeX symbols inside the `lstlisting` environment.
4. **LaTeX Master File Assembly (`jalon-99.tex`):**
    - Create a Python script to assemble `Jalon-99.md`, the exercises, and the TPs into a single LaTeX file (`jalon-99.tex`).
    - The script must apply all technical locks:
        - Handle Markdown-to-LaTeX conversion for sections (avoid manual numbering).
        - Manage formatting (bold, italic) carefully protecting math mode.
        - Ensure unescaped ampersands (`&`) and French accents outside math mode are handled correctly, and that underscores/carets outside code blocks are wrapped in `$ $`.
        - Add at least 1-2 native TikZ vector graphics to illustrate concepts (e.g., separation of convex sets by a hyperplane).
5. **Compilation and Validation:**
    - Compile `jalon-99.tex` using `pdflatex` to generate `jalon-99-polycopie.pdf`.
    - Verify that no compilation errors occur and that the resulting PDF is correct.
6. **Update Tracking Files:**
    - Update `Tableau de bord.md` to mark Jalon 99 as complete (e.g., `[x]`) and append `🔥 **Enrichi** *(10 Exos + 5 TP)*`. Ensure the link points to the new file name `jalon-99/Jalon-99.md`.
    - Append an audit log entry in `README.md` under `## 📝 Historique & Avancement`.
7. **Pre-commit Steps:**
    - Call `pre_commit_instructions` and follow its instructions to ensure proper testing, verification, review, and reflection are done.
