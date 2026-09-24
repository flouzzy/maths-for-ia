## Exercice 9 : Problème de complétude et densité \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
L'espace vectoriel des fonctions continues à support compact $C_c(\mathbb{R})$, muni de la norme $\| \cdot \|_1$, est-il un espace de Banach (complet) ? Justifier rigoureusement à l'aide de la notion de densité.

**Correction :**
La réponse est **non**.
Par définition de la complétude, un espace métrique est complet si et seulement si toute suite de Cauchy y converge vers une limite appartenant à cet espace.
Si $C_c(\mathbb{R})$ était complet pour la norme $L^1$, alors étant donné qu'il est dense dans $L^1(\mathbb{R})$, il devrait coïncider avec $L^1(\mathbb{R})$.
Or, il est facile de trouver des fonctions qui sont dans $L^1(\mathbb{R})$ mais qui ne sont pas dans $C_c(\mathbb{R})$.

Prenons un exemple explicite de suite de Cauchy dans $C_c(\mathbb{R})$ qui ne converge pas dans $C_c(\mathbb{R})$.
Considérons la fonction porte $f = \mathbf{1}_{[0,1]}$, qui est dans $L^1$ mais discontinue, donc $f \notin C_c(\mathbb{R})$.
Construisons une suite de fonctions $g_n \in C_c(\mathbb{R})$ définies comme dans l'Exercice 1, telles que $\| f - g_n \|_1 \to 0$.
Puisque la suite $(g_n)$ converge vers $f$ dans $L^1$, c'est obligatoirement une suite de Cauchy pour la norme $L^1$.
Supposons par l'absurde que $C_c(\mathbb{R})$ soit complet. Alors la suite de Cauchy $(g_n)$ devrait avoir une limite $g \in C_c(\mathbb{R})$ telle que $\| g_n - g \|_1 \to 0$.
Par unicité de la limite dans un espace normé (ou par l'inégalité triangulaire $\| f - g \|_1 \le \| f - g_n \|_1 + \| g_n - g \|_1 \to 0$), nous aurions $\| f - g \|_1 = 0$.
Cela implique que $f = g$ presque partout.
Or $g$ est continue. Mais $f$ a une discontinuité de saut indélébile en $0$ et en $1$ : elle ne peut être égale presque partout à aucune fonction continue.
C'est une contradiction. Donc $C_c(\mathbb{R})$ muni de la norme $\| \cdot \|_1$ n'est pas complet.
$L^1(\mathbb{R})$ est précisément le complété de $C_c(\mathbb{R})$ pour cette norme.
