---
uuid: "jalon-45"
title: "Différentiabilité et Gradient"
year: 1
trimester: 4
tags:
  - math/analyse
  - ia/optimisation
prev: "[[Jalon 44 (Fonctions de plusieurs variables).md]]"
next: "[[Jalon 46 (Matrice jacobienne).md]]"
---

# Jalon 45 : Différentiabilité et Gradient

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous êtes aveugle et que vous vous tenez sur le flanc d'une montagne. Vous voulez savoir comment le terrain "penche" autour de vous.
    - Les **dérivées partielles**, c'est tâter le terrain uniquement vers le Nord/Sud ou uniquement vers l'Est/Ouest.
    - Le **gradient**, c'est la direction exacte dans laquelle la pente est la plus raide. C'est comme une flèche posée au sol qui vous dit : "Si tu veux monter le plus vite possible, va par là".
    - La **différentiabilité**, c'est la garantie que le terrain est lisse (comme une nappe de soie) et pas cassé ou pointu comme du verre brisé. Si c'est lisse, vous pouvez poser une plaque de bois (le plan tangent) qui touche parfaitement le sol sous vos pieds.
- **Le "Pourquoi on a inventé ça" :** Pour optimiser. Si on veut trouver le point le plus bas d'une vallée (le minimum d'une erreur), on a besoin de savoir dans quelle direction descendre. Le gradient est la boussole de toute l'intelligence artificielle.
- **Visualisation :** Un plan incliné qui effleure une surface courbe en un point unique. Le gradient est un vecteur dans le plan horizontal qui pointe vers le haut de la pente.

## 2. Formalisation

### A. Définitions Formelles

Soit $f : U \to \mathbb{R}$ une fonction définie sur un ouvert $U \subset \mathbb{R}^n$.

> **Définition 1 (Différentiabilité) :**
> On dit que $f$ est **différentiable** en $a \in U$ s'il existe une application linéaire $L : \mathbb{R}^n \to \mathbb{R}$ telle que :
> $$f(a + h) = f(a) + L(h) + \|h\| \epsilon(h)$$
> avec $\lim_{h \to 0} \epsilon(h) = 0$. L'application linéaire $L$ est unique, on l'appelle la **différentielle** de $f$ en $a$, notée $df_a$.

> **Définition 2 (Dérivées partielles) :**
> On appelle $i$-ème dérivée partielle de $f$ en $a$ la limite (si elle existe) :
> $$\frac{\partial f}{\partial x_i}(a) = \lim_{t \to 0} \frac{f(a + t e_i) - f(a)}{t}$$
> où $e_i$ est le $i$-ème vecteur de la base canonique.

> **Définition 3 (Gradient) :**
> Si $f$ est différentiable en $a$, le **gradient** de $f$ en $a$ est le vecteur :
> $$\nabla f(a) = \left( \frac{\partial f}{\partial x_1}(a), \dots, \frac{\partial f}{\partial x_n}(a) \right)^T$$
> On a alors la relation fondamentale : $df_a(h) = \langle \nabla f(a), h \rangle$.

### B. Théorèmes Fondamentaux

> **Théorème (Condition nécessaire) :**
> Si $f$ est différentiable en $a$, alors $f$ est continue en $a$, et toutes ses dérivées partielles existent en $a$.

> **Théorème (Condition suffisante - Classe $\mathcal{C}^1$) :**
> Si toutes les dérivées partielles de $f$ existent et sont **continues** au voisinage de $a$, alors $f$ est différentiable en $a$. On dit que $f$ est de classe $\mathcal{C}^1$.

## 3. Démonstrations

### Démonstration : Différentiabilité $\implies$ Continuité

1. **Cadre :** Supposons $f$ différentiable en $a$.
2. **Écriture du développement :**
   $f(a+h) = f(a) + df_a(h) + \|h\|\epsilon(h)$.
3. **Passage à la limite :**
   - Comme $df_a$ est une application linéaire en dimension finie, elle est continue, donc $\lim_{h \to 0} df_a(h) = df_a(0) = 0$.
   - Par définition, $\lim_{h \to 0} \|h\|\epsilon(h) = 0 \times 0 = 0$.
4. **Conclusion :**
   $\lim_{h \to 0} f(a+h) = f(a)$. Donc $f$ est continue en $a$.

### Lien avec la direction de plus forte pente

Soit $u$ un vecteur unitaire ($\|u\|=1$). La dérivée de $f$ dans la direction $u$ est $D_u f(a) = df_a(u) = \langle \nabla f(a), u \rangle$.
Par l'inégalité de Cauchy-Schwarz :
$$| \langle \nabla f(a), u \rangle | \le \|\nabla f(a)\| \cdot \|u\| = \|\nabla f(a)\|$$
L'égalité est atteinte quand $u$ est colinéaire à $\nabla f(a)$.
**Conclusion :** La variation de $f$ est maximale quand on se déplace dans la direction du gradient.

## 4. Exercices d'Application

### Exercice 1 : Calcul de différentielle et gradient
**Énoncé :** Soit $f(x, y) = x^2 + 3xy + e^y$. Calculer le gradient en tout point et la différentielle au point $(1, 0)$.
**Correction Détaillée :**
1. **Dérivées partielles :**
   - $\frac{\partial f}{\partial x} = 2x + 3y$.
   - $\frac{\partial f}{\partial y} = 3x + e^y$.
2. **Gradient :** $\nabla f(x, y) = (2x + 3y, 3x + e^y)^T$.
3. **Au point $(1, 0)$ :** $\nabla f(1, 0) = (2(1) + 3(0), 3(1) + e^0)^T = (2, 4)^T$.
4. **Différentielle :** $df_{(1,0)}(h_1, h_2) = 2h_1 + 4h_2$.

### Exercice 2 : Niveau Avancé (Fonction non différentiable)
**Énoncé :** Étudier la différentiabilité en $(0, 0)$ de $f(x, y) = \sqrt{x^2 + y^2}$.
**Correction Détaillée :**
1. **Continuité :** $f$ est continue (norme euclidienne).
2. **Dérivées partielles :** $\frac{f(t, 0) - f(0, 0)}{t} = \frac{\sqrt{t^2}}{t} = \frac{|t|}{t}$. Cette limite n'existe pas en 0 (elle vaut 1 à droite, -1 à gauche).
3. **Conclusion :** Comme les dérivées partielles n'existent pas, la fonction ne peut pas être différentiable en $(0, 0)$. (Géométriquement, c'est un cône avec une pointe).

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Le **Gradient Descent** (Descente de Gradient) est l'algorithme qui permet d'ajuster les poids $\theta$ d'un modèle pour minimiser la perte $L(\theta)$.
- **Exemple Concret :**
    - **Backpropagation :** Pour calculer le gradient d'un réseau complexe, on utilise la "Chain Rule" (Règle de la chaîne, Jalon 46), qui est la manière de composer les différentielles. Le gradient nous indique comment modifier chaque poids $w_{ij}$ pour réduire l'erreur globale.
    - **Direction de descente :** On met à jour les poids par la formule $\theta \leftarrow \theta - \eta \nabla L(\theta)$. Le signe "moins" indique qu'on va dans la direction opposée au gradient pour **descendre** vers le minimum. $\eta$ (le learning rate) est la taille du pas que l'on fait dans cette direction.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 44 (Fonctions de plusieurs variables).md]], [[Jalon-8.md]]
- **Concepts Futurs dépendants :** [[Jalon 46 (Matrice jacobienne).md]], [[Jalon 128 (Flots de gradient).md]]
