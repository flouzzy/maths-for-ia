# Exercice 7 : Espace $L^2$ (★★★★☆)

**Énoncé :**
Soit $L^2([0, 1])$. Démontrer l'inégalité de Cauchy-Schwarz pour les fonctions $f, g \in L^2([0, 1])$ en considérant le polynôme $P(t) = \|tf + g\|^2$ pour $t \in \mathbb{R}$.

**Correction Détaillée :**
*Analyse de l'énoncé :* C'est la méthode classique de démonstration. On développe le carré de la norme en fonction du produit scalaire, et on utilise le fait que c'est un trinôme du second degré toujours positif.

*Résolution pas-à-pas :*
Soit $t \in \mathbb{R}$. Par définition d'une norme, on a toujours $\|tf + g\|^2 \ge 0$.
Développons cette expression via les propriétés du produit scalaire :
$$ P(t) = \langle tf + g, tf + g \rangle $$
Par bilinéarité (on suppose ici des espaces réels pour simplifier, le cas complexe se traite de manière analogue avec des précautions sur la partie réelle) :
$$ P(t) = t^2\langle f, f \rangle + t\langle f, g \rangle + t\langle g, f \rangle + \langle g, g \rangle $$
Par symétrie $\langle f, g \rangle = \langle g, f \rangle$, donc :
$$ P(t) = \|f\|^2 t^2 + 2\langle f, g \rangle t + \|g\|^2 $$

Ce polynôme en $t$ est du second degré (si $\|f\| \neq 0$) et est toujours $\ge 0$.
Par conséquent, son discriminant réduit $\Delta'$ doit être négatif ou nul.
$$ \Delta' = \text{moitié du coefficient de } t \text{ au carré} - a \cdot c $$
$$ \Delta' = (\langle f, g \rangle)^2 - \|f\|^2 \|g\|^2 $$
Comme $\Delta' \le 0$ :
$$ (\langle f, g \rangle)^2 \le \|f\|^2 \|g\|^2 $$
En prenant la racine carrée, on obtient l'inégalité de Cauchy-Schwarz :
$$ |\langle f, g \rangle| \le \|f\| \cdot \|g\| $$

(Si $f=0$, l'inégalité est trivialement $0 \le 0$).
