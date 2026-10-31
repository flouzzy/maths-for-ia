### Exercice 7 (Jalon 104) - Bases Hilbertiennes

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

Soit $H$ un espace de Hilbert séparable sur $\mathbb{C}$. On dispose d'une base hilbertienne (orthonormale complète) $\mathcal{B} = \{e_n\}_{n \in \mathbb{Z}}$ de $H$.

Pour tout entier $k \in \mathbb{Z}$, on définit une nouvelle famille de vecteurs $\mathcal{F}_k = \{f_n^{(k)}\}_{n \in \mathbb{Z}}$ par la relation suivante :
$$ f_n^{(k)} = \frac{1}{\sqrt{2}} e_n + \frac{1}{\sqrt{2}} e_{n+k} $$

1.  Déterminez la ou les conditions sur l'entier $k$ pour que la famille $\mathcal{F}_k$ forme un système orthonormal.
2.  Pour la ou les valeurs de $k$ pour lesquelles $\mathcal{F}_k$ est un système orthonormal, déterminez si $\mathcal{F}_k$ constitue une base hilbertienne de $H$. Justifiez rigoureusement votre réponse.

---

### Correction de l'Exercice 7

Cher étudiant, votre compréhension des bases hilbertiennes doit être irréprochable. Abordons cet exercice avec la rigueur nécessaire.

**Partie 1 : Conditions pour que $\mathcal{F}_k$ soit un système orthonormal.**

Pour que la famille $\mathcal{F}_k = \{f_n^{(k)}\}_{n \in \mathbb{Z}}$ soit un système orthonormal, il est nécessaire et suffisant que, pour tout $n, m \in \mathbb{Z}$, l'on ait $\langle f_n^{(k)}, f_m^{(k)} \rangle = \delta_{nm}$, où $\delta_{nm}$ est le symbole de Kronecker (égal à 1 si $n=m$ et 0 sinon).

Calculons le produit scalaire $\langle f_n^{(k)}, f_m^{(k)} \rangle$ :
$$ \langle f_n^{(k)}, f_m^{(k)} \rangle = \left\langle \frac{1}{\sqrt{2}} e_n + \frac{1}{\sqrt{2}} e_{n+k}, \frac{1}{\sqrt{2}} e_m + \frac{1}{\sqrt{2}} e_{m+k} \right\rangle $$
Par bilinéarité de l'opération de produit scalaire (linéarité par rapport au premier argument et anti-linéarité par rapport au second argument) :
$$ = \frac{1}{\sqrt{2}} \overline{\left(\frac{1}{\sqrt{2}}\right)} \langle e_n + e_{n+k}, e_m + e_{m+k} \rangle $$
$$ = \frac{1}{2} \left( \langle e_n, e_m \rangle + \langle e_n, e_{m+k} \rangle + \langle e_{n+k}, e_m \rangle + \langle e_{n+k}, e_{m+k} \rangle \right) $$
Puisque $\mathcal{B} = \{e_n\}_{n \in \mathbb{Z}}$ est une base orthonormale, nous avons $\langle e_i, e_j \rangle = \delta_{ij}$ pour tous $i, j \in \mathbb{Z}$. Substituons cette propriété dans l'expression :
$$ = \frac{1}{2} \left( \delta_{nm} + \delta_{n,m+k} + \delta_{n+k,m} + \delta_{n+k,m+k} \right) $$
Nous devons égaler cette expression à $\delta_{nm}$. Analysons deux cas distincts : $n=m$ et $n \neq m$.

**Cas 1 : $n=m$.**
Dans ce cas, $\delta_{nm} = \delta_{nn} = 1$. L'équation du produit scalaire devient :
$$ \frac{1}{2} \left( \delta_{nn} + \delta_{n,n+k} + \delta_{n+k,n} + \delta_{n+k,n+k} \right) = 1 $$
En utilisant les propriétés de $\delta_{ij}$, nous avons $\delta_{nn}=1$ et $\delta_{n+k,n+k}=1$. De plus, le symbole de Kronecker est symétrique, donc $\delta_{n,n+k} = \delta_{n+k,n}$. L'expression se simplifie en :
$$ \frac{1}{2} \left( 1 + \delta_{n,n+k} + \delta_{n,n+k} + 1 \right) = 1 $$
$$ \frac{1}{2} \left( 2 + 2\delta_{n,n+k} \right) = 1 $$
$$ 1 + \delta_{n,n+k} = 1 $$
Pour que cette égalité soit vérifiée, il est nécessaire que $\delta_{n,n+k} = 0$.
Le terme $\delta_{n,n+k}$ est égal à 1 si $n = n+k$, ce qui implique $k=0$. Dans tous les autres cas, il est égal à 0.
Par conséquent, pour que $\delta_{n,n+k} = 0$, il est impératif que $k \neq 0$.

**Cas 2 : $n \neq m$.**
Dans ce cas, $\delta_{nm} = 0$. L'équation du produit scalaire devient :
$$ \frac{1}{2} \left( \delta_{nm} + \delta_{n,m+k} + \delta_{n+k,m} + \delta_{n+k,m+k} \right) = 0 $$
Puisque $n \neq m$, $\delta_{nm}=0$. De plus, comme nous avons déjà établi la condition nécessaire $k \neq 0$, il s'ensuit que si $n \neq m$, alors $n+k \neq m+k$. Par conséquent, $\delta_{n+k,m+k}=0$.
L'équation se réduit donc à :
$$ \frac{1}{2} \left( 0 + \delta_{n,m+k} + \delta_{n+k,m} + 0 \right) = 0 $$
$$ \delta_{n,m+k} + \delta_{n+k,m} = 0 $$
Pour qu'une somme de termes non négatifs (les symboles de Kronecker sont uniquement 0 ou 1) soit nulle, chaque terme doit être nul individuellement. Ainsi, nous devons avoir :
1.  $\delta_{n,m+k} = 0$ pour tout $n \neq m$. Cela signifie que l'index $n$ ne peut pas être égal à $m+k$ pour tout $n \neq m$. Cela est équivalent à dire que $m \neq n-k$ pour tout $n \neq m$.
2.  $\delta_{n+k,m} = 0$ pour tout $n \neq m$. Cela signifie que l'index $n+k$ ne peut pas être égal à $m$ pour tout $n \neq m$. Cela est équivalent à dire que $m \neq n+k$ pour tout $n \neq m$.

En résumé, pour que $\mathcal{F}_k$ soit un système orthonormal, il faut que $k \neq 0$, ET pour tout couple d'entiers $n, m$ distincts ($n \neq m$), on doit avoir $m \neq n-k$ ET $m \neq n+k$.

Cependant, étant donné que $k$ est un entier non nul, et que $n$ et $m$ peuvent prendre n'importe quelle valeur entière, nous pouvons toujours choisir $m$ de sorte que l'une de ces conditions soit violée.
Considérons par exemple un entier $n \in \mathbb{Z}$ quelconque et un entier $k \neq 0$.
Si nous choisissons $m = n-k$, alors $m \neq n$ car $k \neq 0$.
Pour ce choix de $m$, le premier terme $\delta_{n,m+k}$ devient $\delta_{n,(n-k)+k} = \delta_{n,n} = 1$.
Le second terme $\delta_{n+k,m}$ devient $\delta_{n+k,n-k}$. Puisque $k \neq 0$, $n+k \neq n-k$, donc ce terme est $\delta_{n+k,n-k}=0$.
Ainsi, pour $n \neq m$ (avec $m=n-k$), la somme $\delta_{n,m+k} + \delta_{n+k,m}$ devient $1+0=1$.
Cette somme est égale à $1$, et non à $0$. Par conséquent, la condition $\delta_{n,m+k} + \delta_{n+k,m} = 0$ n'est pas satisfaite pour un tel choix de $m$.
Cela signifie que pour tout entier $k \neq 0$, nous pouvons toujours trouver des indices $n \neq m$ pour lesquels le produit scalaire $\langle f_n^{(k)}, f_m^{(k)} \rangle \neq 0$. Plus précisément, nous avons trouvé $\langle f_n^{(k)}, f_{n-k}^{(k)} \rangle = 1/2 \cdot (1+0+0+0) = 1/2 \neq 0$.

**Conclusion de la Partie 1 :**
Il n'existe aucune valeur entière de $k$ pour laquelle la famille $\mathcal{F}_k$ forme un système orthonormal.

**Partie 2 : Détermination si $\mathcal{F}_k$ constitue une base hilbertienne.**

La question demande de déterminer si $\mathcal{F}_k$ est une base hilbertienne pour la ou les valeurs de $k$ pour lesquelles elle est un système orthonormal.

Puisque, comme démontré en Partie 1, il n'existe aucune valeur entière de $k$ pour laquelle $\mathcal{F}_k$ forme un système orthonormal, il n'y a aucune valeur de $k$ à considérer pour cette deuxième partie. Par conséquent, il n'existe aucune famille $\mathcal{F}_k$ de ce type qui puisse être une base hilbertienne de $H$. Un système non orthonormal ne peut pas être une base hilbertienne.

Votre rigueur dans la vérification de chaque condition est essentielle. L'absence de solution, ou l'établissement qu'une propriété n'est jamais vérifiée sous les conditions données, est un résultat mathématique valide et instructif.