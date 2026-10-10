# Exercice 02 : Indépendance de tirages avec et sans remise
Difficulté : $\bigstar\star\star\star\star$

**Énoncé :**
Une urne contient 4 boules rouges et 6 boules bleues. On tire deux boules successivement.
Soit $R_1$ l'événement « la première boule est rouge » et $R_2$ l'événement « la deuxième boule est rouge ».
1. Les événements $R_1$ et $R_2$ sont-ils indépendants si le tirage se fait avec remise ?
2. Les événements $R_1$ et $R_2$ sont-ils indépendants si le tirage se fait sans remise ?

**Correction :**
1. **Avec remise :**
La composition de l'urne est identique pour le second tirage.
$\mathbb{P}(R_1) = \frac{4}{10} = 0,4$.
$\mathbb{P}(R_2) = \frac{4}{10} = 0,4$ (par symétrie ou en utilisant la formule des probabilités totales).
L'événement $R_1 \cap R_2$ signifie tirer rouge puis rouge. La probabilité est $\frac{4}{10} \times \frac{4}{10} = 0,16$.
Or $\mathbb{P}(R_1)\mathbb{P}(R_2) = 0,4 \times 0,4 = 0,16$. Les événements sont **indépendants**.

2. **Sans remise :**
$\mathbb{P}(R_1) = \frac{4}{10} = 0,4$.
Si la première est rouge, l'urne contient 3 rouges et 6 bleues. Donc $\mathbb{P}(R_2 | R_1) = \frac{3}{9} = \frac{1}{3}$.
$\mathbb{P}(R_1 \cap R_2) = \mathbb{P}(R_1) \mathbb{P}(R_2 | R_1) = \frac{4}{10} \times \frac{3}{9} = \frac{12}{90} = \frac{2}{15} \approx 0,133$.
Calculons $\mathbb{P}(R_2)$ par la loi des probabilités totales :
$\mathbb{P}(R_2) = \mathbb{P}(R_2|R_1)\mathbb{P}(R_1) + \mathbb{P}(R_2|B_1)\mathbb{P}(B_1) = \frac{3}{9} \times \frac{4}{10} + \frac{4}{9} \times \frac{6}{10} = \frac{12+24}{90} = \frac{36}{90} = 0,4$.
Le produit $\mathbb{P}(R_1)\mathbb{P}(R_2) = 0,4 \times 0,4 = 0,16 = \frac{4}{25}$.
Or $\frac{2}{15} \neq \frac{4}{25}$ (car $50 \neq 60$).
Les événements ne sont **pas indépendants**. Sans remise, le premier tirage affecte le second.
