---
uuid: "jalon-111"
title: "Applications différentiables et Fibré tangent"
year: 3
trimester: 10
tags:
  - math/geometrie
  - ia/abstraction
prev: "[[Jalon 110 (Variétés différentielles abstraites).md]]"
next: "[[Jalon 112 (Champs de vecteurs).md]]"
---

# Jalon 111 : Applications différentiables et Fibré tangent

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous soyez un pilote d'avion (un point $x$ sur une variété $M$).
    - Votre avion a une direction et une vitesse à chaque instant : c'est votre **vecteur tangent**.
    - L'ensemble de toutes les directions possibles pour décoller de votre piste actuelle forme l'**Espace Tangent** (une plaque plate qui effleure le sol courbe).
    - Maintenant, imaginez qu'un portail magique (une **application $f$**) vous transporte instantanément sur une autre planète (une autre variété $N$).
    - L'**Application Tangente ($df_x$)**, c'est ce qui arrive à votre vitesse pendant le téléportation : si vous alliez vers le Nord à 100 km/h sur Terre, vers où et à quelle vitesse irez-vous sur la nouvelle planète après avoir traversé le portail ?
- **Le "Pourquoi on a inventé ça" :** Pour pouvoir faire de la physique (calculer des forces, des énergies) sur des surfaces courbes. On a besoin de savoir comment les vecteurs (vitesses, gradients) se transforment quand on change de point de vue ou d'espace.
- **Visualisation :** Une forêt de flèches. À chaque point de la surface courbe, on plante une flèche qui indique une direction possible. Le **Fibré Tangent** est la collection complète de toutes ces flèches.

## 2. Formalisation & Rigueur Académique

### A. Applications Différentiables

Soient $M$ and $N$ deux variétés différentielles de dimensions $m$ and $n$.

> **Définition 1 (Différentiabilité) :**
> Une application $f : M \to N$ est dite **différentiable** en $x \in M$ si pour toute carte $(U, \phi)$ de $M$ contenant $x$ et toute carte $(V, \psi)$ de $N$ contenant $f(x)$, l'application locale suivante est différentiable au sens classique dans $\mathbb{R}^m \to \mathbb{R}^n$ :
> $$\hat{f} = \psi \circ f \circ \phi^{-1} : \phi(U \cap f^{-1}(V)) \subset \mathbb{R}^m \to \mathbb{R}^n$$

### B. Espace Tangent et Dérivations

Il existe plusieurs manières de définir l'espace tangent $T_x M$. La plus moderne est celle des **dérivations**.

> **Définition 2 (Vecteur tangent) :**
> Un vecteur tangent $v$ en $x \in M$ est une application linéaire $v : \mathcal{C}^\infty(M) \to \mathbb{R}$ qui vérifie la règle de Leibniz (la dérivée d'un produit) :
> $$v(gh) = v(g)h(x) + g(x)v(h)$$
> L'espace de ces vecteurs est l'**espace tangent** $T_x M$. Sa dimension est celle de la variété.

### C. Application Linéaire Tangente (Push-forward)

> **Définition 3 (Différentielle) :**
> Pour $f : M \to N$ différentiable, l'application tangente $df_x : T_x M \to T_{f(x)} N$ est définie par :
> $$\forall v \in T_x M, \forall h \in \mathcal{C}^\infty(N), \quad (df_x(v))(h) = v(h \circ f)$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Indépendance de la différentielle par rapport aux cartes

Montrons que la définition de la différentielle est cohérente même si on change de système de coordonnées.

1. **Localisation :** Soit $v \in T_x M$. Dans une carte $\phi = (x_1, \dots, x_m)$, $v$ s'écrit comme une combinaison de dérivées partielles : $v = \sum v_i \frac{\partial}{\partial x_i}$.
2. **Action de f :** L'image $w = df_x(v)$ agit sur une fonction $h$ de $N$.
3. **Calcul en coordonnées :** En utilisant une carte $\psi = (y_1, \dots, y_n)$ sur $N$ :
   $w(h) = v(h \circ \psi^{-1} \circ \psi \circ f) = v(\hat{h} \circ \hat{f})$ où $\hat{f}$ est l'expression locale de $f$.
4. **Règle de la chaîne :** Par la règle de la chaîne dans $\mathbb{R}^m$ (Jalon 46) :
   $\frac{\partial (\hat{h} \circ \hat{f})}{\partial x_i} = \sum_{j=1}^n \frac{\partial \hat{h}}{\partial y_j} \cdot \frac{\partial \hat{f}_j}{\partial x_i}$.
5. **Conclusion :** Les composantes de $w$ dans la base $(\frac{\partial}{\partial y_j})$ sont $w_j = \sum_i \frac{\partial \hat{f}_j}{\partial x_i} v_i$.
   Cela correspond exactement au produit par la **matrice jacobienne** de l'expression locale. Comme le changement de carte est lui-même un difféomorphisme, la structure linéaire est préservée.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Tangente de l'exponentielle complexe
**Énoncé :** Soit $f : \mathbb{R} \to S^1$ définie par $f(t) = e^{it}$. Calculer $df_t(1)$.
**Correction Détaillée :**
1. $T_t \mathbb{R}$ est engendré par la dérivée standard $d/dt$.
2. On applique $f$ : $df_t(d/dt)$ est le vecteur vitesse de la courbe $\gamma(t) = (\cos t, \sin t)$.
3. $\gamma'(t) = (-\sin t, \cos t)$.
4. **Résultat :** Le vecteur tangent en $f(t)$ est le vecteur $(-y, x)$ de $\mathbb{R}^2$, qui est bien tangent au cercle.

### Exercice 2 : Niveau Avancé (Le Fibré Tangent)
**Énoncé :** Montrer que $TM = \bigcup_{x \in M} T_x M$ a une structure de variété de dimension $2 \times \dim M$.
**Correction Détaillée :**
Pour chaque carte $(U, \phi)$ de $M$, on construit une carte $(TU, \Phi)$ de $TM$. Si $\phi(x) = (x_1, \dots, x_m)$, alors un vecteur $v \in T_x M$ est donné par ses composantes $(v_1, \dots, v_m)$. On pose $\Phi(x, v) = (x_1, \dots, x_m, v_1, \dots, v_m)$. Les changements de cartes sur $M$ induisent des changements de cartes lisses sur $TM$ (via la Jacobienne).

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Le **Geometric Deep Learning** étend les réseaux de neurones aux variétés. Le calcul des gradients sur ces réseaux nécessite de transporter les vecteurs d'un espace tangent à un autre.
- **Example Concret :**
    - **Riemannian Gradient Descent :** Pour optimiser une fonction sur une variété (ex: trouver la meilleure rotation), on calcule le gradient classique, puis on le projette sur l'**Espace Tangent** de la variété. On fait ensuite un petit pas dans cette direction avant de "revenir" sur la variété (opération de rétraction).
    - **Equivariant CNNs :** Si on veut qu'une IA reconnaisse un objet peu importe sa rotation, on utilise des couches dont la différentielle (le tangent map) commute avec l'action du groupe de rotation.
    - **Neural ODEs on Manifolds :** On définit l'évolution de l'état caché comme un champ de vecteurs sur le **Fibré Tangent**. Le réseau apprend à choisir la "vitesse" optimale à chaque point de la variété des représentations.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 110 (Variétés différentielles abstraites).md]], [[Jalon 46 (Matrice jacobienne et Règle de la chaîne).md]]
- **Concepts Futurs dépendants :** [[Jalon 112 (Champs de vecteurs).md]], [[Jalon 116 (Variétés riemanniennes).md]]
