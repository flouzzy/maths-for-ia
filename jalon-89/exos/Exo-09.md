# Exercice 9 : Indépendance conditionnelle et lancers successifs

$\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Un joueur lance un dé équilibré à 6 faces. S'il obtient 6, il gagne la partie. S'il ne gagne pas, il relance. Cependant, à l'étape $n$, on lui ajoute une pénalité : il ne gagne que si le résultat est 6, et il doit tirer à nouveau une pièce biaisée qui tombe sur face avec probabilité $\frac{1}{n^2}$. Si la pièce est pile, son 6 est annulé.
Montrer qu'il finira presque sûrement par gagner définitivement si on ignore la pièce, mais avec la pièce l'analyse asymptotique change. Soit $A_n$ l'événement "Gagner à l'étape $n$". Est-ce qu'il gagne infiniment souvent ?

**Correction :**
Modélisons de manière précise : on effectue une suite infinie d'essais pour tester la limite. On suppose qu'on joue une infinité de fois.
Soit $D_n$ l'événement "Le dé donne 6 à l'étape $n$". On a $\mathbb{P}(D_n) = 1/6$.
Soit $F_n$ l'événement "La pièce tombe sur Face à l'étape $n$". On a $\mathbb{P}(F_n) = 1/n^2$.
L'événement "Gagner à l'étape $n$" est $A_n = D_n \cap F_n$.
Puisque le lancer de dé et de pièce sont indépendants :
$$ \mathbb{P}(A_n) = \mathbb{P}(D_n) \mathbb{P}(F_n) = \frac{1}{6} \times \frac{1}{n^2} = \frac{1}{6n^2} $$
La série de ces probabilités est :
$$ \sum_{n=1}^\infty \mathbb{P}(A_n) = \frac{1}{6} \sum_{n=1}^\infty \frac{1}{n^2} < +\infty $$
Puisque la série converge, le premier lemme de Borel-Cantelli implique que $\mathbb{P}(\limsup A_n) = 0$.
Ainsi, il ne gagnera qu'un nombre fini de fois. La pénalité annule ses victoires infinies.
