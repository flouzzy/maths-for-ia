# Exercice 9 : Théorème de la borne de l'union (Indépendance et Inégalités) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**

Soit une suite d'événements $(A_n)_{n \geq 1}$ mutuellement indépendants dans un espace de probabilité.
On suppose que pour tout $n \geq 1$, $\mathbb{P}(A_n) = p$ où $p \in ]0, 1[$.
Soit $B_N = \bigcup_{n=1}^N A_n$ l'événement consistant à ce qu'au moins l'un des événements $A_1, \dots, A_N$ se produise.
1. Exprimer rigoureusement la probabilité $\mathbb{P}(B_N)$ en fonction de $N$ et $p$.
2. Déterminer la limite de $\mathbb{P}(B_N)$ lorsque $N$ tend vers l'infini. Conclure géométriquement.

**Correction Détaillée :**

1. **Expression de la probabilité de l'union :**
   - Calculer directement la probabilité de l'union d'événements non disjoints est complexe (formule du crible de Poincaré : $\mathbb{P}(\bigcup A_i) = \sum \mathbb{P}(A_i) - \sum \mathbb{P}(A_i \cap A_j) + \dots$).
   - L'astuce fondamentale consiste à passer par le complémentaire.
   - Par les lois de De Morgan, le complémentaire d'une union est l'intersection des complémentaires :
     $$ (B_N)^c = \left( \bigcup_{n=1}^N A_n \right)^c = \bigcap_{n=1}^N A_n^c $$
   - L'événement $(B_N)^c$ signifie qu'"aucun des événements $A_n$ ne se produit".
   - Puisque les événements $(A_n)$ sont mutuellement indépendants, le théorème démontré dans l'exercice 3 assure que leurs complémentaires $(A_n^c)$ le sont également.
   - Par définition de l'indépendance mutuelle, la probabilité de l'intersection est égale au produit des probabilités :
     $$ \mathbb{P}((B_N)^c) = \mathbb{P}\left(\bigcap_{n=1}^N A_n^c\right) = \prod_{n=1}^N \mathbb{P}(A_n^c) $$
   - La probabilité de chaque complémentaire est $\mathbb{P}(A_n^c) = 1 - \mathbb{P}(A_n) = 1 - p$.
   - Le produit contient $N$ facteurs identiques :
     $$ \mathbb{P}((B_N)^c) = \prod_{n=1}^N (1 - p) = (1 - p)^N $$
   - Enfin, on repasse à l'événement direct par l'axiome des complémentaires ($\mathbb{P}(B_N) = 1 - \mathbb{P}((B_N)^c)$) :
     $$ \mathbb{P}(B_N) = 1 - (1 - p)^N $$
2. **Passage à la limite :**
   - Nous cherchons $\lim_{N \to +\infty} \mathbb{P}(B_N) = \lim_{N \to +\infty} \left( 1 - (1 - p)^N \right)$.
   - Puisque la probabilité d'occurrence $p$ est strictement comprise entre $0$ et $1$ ($p \in ]0, 1[$), le terme $1 - p$ est également strictement compris entre $0$ et $1$.
   - La suite géométrique de raison $q = 1 - p$ (avec $|q| < 1$) converge vers $0$ lorsque la puissance $N$ tend vers l'infini : $\lim_{N \to +\infty} (1 - p)^N = 0$.
   - Par conséquent, la limite cherchée est :
     $$ \lim_{N \to +\infty} \mathbb{P}(B_N) = 1 - 0 = 1 $$
   - **Conclusion géométrique et probabiliste :** Peu importe à quel point la probabilité individuelle $p$ d'un événement est infime (tant qu'elle n'est pas strictement nulle), si l'on répète l'expérience un très grand nombre de fois de manière indépendante, la probabilité qu'au moins une de ces tentatives réussisse converge inéluctablement vers la certitude absolue ($1$). C'est un principe fondamental derrière la théorie des miracles statistiques et de l'entropie.
