---
uuid: "jalon-82"
title: "Introduction aux distributions de Schwartz"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 81 (Transformée de Fourier dans L2).md]]"
next: "[[Jalon 83 (Dérivation au sens des distributions).md]]"
---

# Jalon 82 : Introduction aux distributions de Schwartz

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous soyez dans le noir complet. Vous ne pouvez pas voir les objets, mais vous avez des **capteurs** (des lampes de poche très précises).
    - Un **objet classique** (une fonction), c'est quelque chose que vous pouvez voir point par point.
    - Une **Distribution**, c'est un objet invisible que vous ne pouvez connaître qu'en envoyant un rayon de lumière dessus (une **fonction test**) et en mesurant l'ombre qu'il projette.
    - Le **Dirac** ($\delta_0$) est l'exemple ultime : ce n'est pas une fonction (car elle devrait être infinie en 0 et nulle ailleurs), c'est un "micro" qui n'écoute qu'au point zéro. Si vous chantez devant ce micro, il ne retiendra que la note exacte que vous avez chantée à l'instant zéro.
- **Le "Pourquoi on a inventé ça" :** Laurent Schwartz a réalisé que certaines fonctions physiques (comme une force d'impact instantanée ou une charge ponctuelle) ne peuvent pas être décrites par des fonctions mathématiques classiques sans créer des paradoxes. La théorie des distributions permet de manipuler ces "objets généralisés" avec la même rigueur que des nombres.
- **Visualisation :** Un pic infiniment haut et infiniment fin. On ne peut pas dessiner ses points, mais on sait que l'aire totale sous le pic vaut exactement 1.

## 2. Formalisation & Rigueur Académique

### A. L'Espace des fonctions tests $\mathcal{D}(\mathbb{R})$

Pour définir une distribution, on a besoin de "fonctions sondes" très régulières.

> **Définition 1 (Espace $\mathcal{D}(\mathbb{R})$) :**
> L'espace $\mathcal{D}(\mathbb{R})$ (ou $\mathcal{C}_c^\infty(\mathbb{R})$) est l'ensemble des fonctions $\phi : \mathbb{R} \to \mathbb{C}$ qui sont :
> 1. **Infiniment dérivables** ($\mathcal{C}^\infty$).
> 2. **À support compact** (elles sont nulles en dehors d'un intervalle borné).

### B. Définition d'une Distribution

> **Définition 2 (Distribution) :**
> Une **distribution** sur $\mathbb{R}$ est une forme linéaire continue sur $\mathcal{D}(\mathbb{R})$. L'ensemble des distributions est noté $\mathcal{D}'(\mathbb{R})$.
> Si $T \in \mathcal{D}'(\mathbb{R})$, on note $\langle T, \phi \rangle$ la valeur (le nombre complexe) que renvoie la distribution quand on lui donne la fonction test $\phi$.

### C. Distributions Régulières et Singulières

1. **Distributions régulières :** Toute fonction $f \in L^1_{loc}(\mathbb{R})$ définit une distribution $T_f$ par :
   $$\langle T_f, \phi \rangle = \int_{-\infty}^{+\infty} f(x) \phi(x) dx$$
2. **Distributions singulières :** Ce sont celles qui ne peuvent pas s'écrire sous forme d'intégrale avec une fonction. L'exemple le plus célèbre est la **masse de Dirac** en $a$ :
   $$\langle \delta_a, \phi \rangle = \phi(a)$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : $\delta_0$ n'est pas une distribution régulière

Montrons par l'absurde qu'il n'existe aucune fonction $f \in L^1_{loc}$ telle que $\phi(0) = \int f(x) \phi(x) dx$ pour tout $\phi \in \mathcal{D}$.

1. **Choix d'une suite de fonctions tests :** Soit $\phi_n$ une suite de fonctions tests telles que $0 \le \phi_n \le 1$, $\phi_n(0) = 1$ et dont le support se contracte vers $\{0\}$ (largeur $1/n$).
2. **Calcul de la limite à gauche :** Par définition de $\delta_0$, $\langle \delta_0, \phi_n \rangle = \phi_n(0) = 1$ pour tout $n$. Donc la limite est 1.
3. **Calcul de la limite à droite (si $f$ existait) :**
   $\langle T_f, \phi_n \rangle = \int_{-1/n}^{1/n} f(x) \phi_n(x) dx$.
   On a $|\langle T_f, \phi_n \rangle| \le \int_{-1/n}^{1/n} |f(x)| dx$.
4. **Utilisation de la théorie de la mesure :** Comme $f \in L^1_{loc}$, l'intégrale sur un ensemble dont la mesure tend vers 0 doit tendre vers 0 (continuité absolue de l'intégrale).
5. **Conclusion :** On aurait $1 = 0$, ce qui est absurde. $\delta_0$ est donc un objet d'une nature nouvelle, plus riche que les fonctions.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : La fonction de Heaviside
**Énoncé :** Soit $H(x) = 1$ si $x > 0$ et $0$ sinon. Calculer sa distribution associée appliquée à une fonction test $\phi$.
**Correction Détaillée :**
$\langle T_H, \phi \rangle = \int_{-\infty}^{+\infty} H(x) \phi(x) dx = \int_0^{+\infty} \phi(x) dx$.
C'est une distribution régulière car $H$ est localement intégrable.

### Exercice 2 : Niveau Avancé (Convergence de distributions)
**Énoncé :** Soit $f_n = n \mathbf{1}_{[0, 1/n]}$. Montrer que $T_{f_n} \to \delta_0$ au sens des distributions.
**Correction Détaillée :**
Pour toute fonction test $\phi$ :
$\langle T_{f_n}, \phi \rangle = n \int_0^{1/n} \phi(x) dx$.
Par le théorème de la moyenne, il existe $c_n \in [0, 1/n]$ tel que l'intégrale vaille $\frac{1}{n} \phi(c_n)$.
Donc $\langle T_{f_n}, \phi \rangle = n \cdot \frac{1}{n} \phi(c_n) = \phi(c_n)$.
Quand $n \to \infty$, $c_n \to 0$. Par continuité de $\phi$, $\phi(c_n) \to \phi(0) = \langle \delta_0, \phi \rangle$.
L'approximation de l'impact par des fonctions de plus en plus brèves et hautes converge vers le Dirac.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, nous travaillons souvent avec des **mesures empiriques**. La distribution d'un jeu de données $\{x_i\}$ est une somme de Diracs : $\hat{p}(x) = \frac{1}{N} \sum \delta(x - x_i)$. C'est une distribution au sens de Schwartz.
- **Example Concret :**
    - **Perte NLL (Negative Log Likelihood) :** Quand nous calculons la perte sur un échantillon discret, nous calculons en fait l'intégrale de notre modèle par rapport à cette distribution de Diracs.
    - **Calcul du Gradient sur des données discrètes :** Pour optimiser un modèle sur des points précis, on utilise le fait que la dérivée d'une distribution existe toujours (Jalon 83). Cela permet de définir le gradient de l'erreur même là où les données sont "pointues".
    - **Impulses dans les RNNs :** Pour modéliser des entrées soudaines (événements), on utilise des fonctions impulsions qui sont des approximations de distributions de Schwartz.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 77 (Densité des fonctions simples).md]], [[Jalon 61 (Insuffisances de l'intégrale de Riemann).md]]
- **Concepts Futurs dépendants :** [[Jalon 83 (Dérivation au sens des distributions).md]], [[Jalon 85 (Axiomes de Kolmogorov).md]]
