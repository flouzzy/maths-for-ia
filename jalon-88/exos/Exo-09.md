# Exercice 9

\subsection*{Exercice 9 : Indépendance conditionnelle \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

**Énoncé :**
Deux événements $A$ et $B$ sont dits conditionnellement indépendants sachant $C$ (avec $P(C)>0$) si $P(A \cap B \mid C) = P(A \mid C) P(B \mid C)$.
Montrer par un contre-exemple que l'indépendance conditionnelle sachant $C$ n'implique pas l'indépendance (inconditionnelle) de $A$ et $B$.

**Correction :**
1. Construisons un modèle probabiliste. Considérons deux pièces de monnaie :
   - Pièce 1 : truquée, donne Pile (P) avec probabilité $p_1 = 0.9$.
   - Pièce 2 : truquée, donne Pile (P) avec probabilité $p_2 = 0.1$.
2. L'expérience est la suivante : on choisit une pièce au hasard (probabilité 1/2 pour chaque), puis on lance cette *même* pièce deux fois de suite.
3. Soit l'événement $C$ = "La pièce 1 est choisie". Donc $P(C) = 1/2$.
   L'événement $C^c$ = "La pièce 2 est choisie". $P(C^c) = 1/2$.
4. Soit $A$ = "Le 1er lancer donne Pile" et $B$ = "Le 2e lancer donne Pile".
5. Sachant $C$, les deux lancers proviennent de la même pièce de probabilité 0.9. Les lancers physiques sont indépendants, donc :
   $P(A \mid C) = 0.9$, $P(B \mid C) = 0.9$, et $P(A \cap B \mid C) = 0.9 \times 0.9 = 0.81$.
   Donc $P(A \cap B \mid C) = P(A \mid C)P(B \mid C)$. $A$ et $B$ sont conditionnellement indépendants sachant $C$.
   (De même sachant $C^c$ : $P(A \mid C^c)=0.1$, $P(B \mid C^c)=0.1$, $P(A \cap B \mid C^c)=0.01$, indépendance conditionnelle vérifiée).
6. Regardons l'indépendance inconditionnelle. Par la loi des probabilités totales :
   $P(A) = P(A \mid C)P(C) + P(A \mid C^c)P(C^c) = 0.9(0.5) + 0.1(0.5) = 0.45 + 0.05 = 0.5$.
   $P(B) = 0.5$ de la même manière.
   Donc $P(A)P(B) = 0.5 \times 0.5 = 0.25$.
7. Calculons $P(A \cap B)$ :
   $P(A \cap B) = P(A \cap B \mid C)P(C) + P(A \cap B \mid C^c)P(C^c) = (0.81)(0.5) + (0.01)(0.5) = 0.405 + 0.005 = 0.41$.
8. On constate que $P(A \cap B) = 0.41 \neq 0.25 = P(A)P(B)$.
9. Conclusion : $A$ et $B$ ne sont *pas* indépendants. L'incertitude sur l'origine du modèle (quelle pièce a été choisie) crée une dépendance forte entre les observations. C'est le principe des variables latentes en Machine Learning.
