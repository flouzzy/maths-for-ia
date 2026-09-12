---
uuid: "jalon-69"
title: "Théorème de convergence dominée (TCD)"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]]"
next: "[[Jalon 70 (Espaces mesurés produits).md]]"
---
# Jalon 69 : Théorème de convergence dominée (TCD)

## 1. Présentation du concept clé

Le théorème de convergence dominée (TCD) de Lebesgue est sans doute le résultat le plus emblématique et le plus utilisé de toute la théorie de la mesure. Il offre une réponse définitive et élégante au problème de l'interversion de la limite et de l'intégrale. La théorie de Riemann exigeait une convergence uniforme, une condition souvent trop rigide. Lebesgue a démontré que si toute l'agitation des fonctions $f_n$ est contenue en valeur absolue sous une enveloppe intégrable $g$, alors l'interversion est valide.
## 2. Formalisation

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### A. Énoncé du Théorème de Lebesgue

> **Théorème de Convergence Dominée (TCD) :**
> Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables (à valeurs réelles ou complexes).
> Supposons que :
> 1. **Convergence simple :** La suite $(f_n)$ converge presque partout vers une fonction $f$.
> 2. **Domination :** Il existe une fonction $g : X \to [0, +\infty]$ **intégrable** ($\int g d\mu < +\infty$) telle que :
>    $$\forall n \in \mathbb{N}, \quad |f_n| \le g \text{ p.p.}$$
> Alors :
> - $f$ est intégrable.
> - $\lim_{n \to \infty} \int_X f_n d\mu = \int_X f d\mu$.
> - $\lim_{n \to \infty} \int_X |f_n - f| d\mu = 0$ (Convergence dans $L^1$).

## 3. Démonstrations

### Démonstration du TCD (via le Lemme de Fatou)

1. **Intégrabilité de f :** Comme $|f_n| \le g$ p.p., en passant à la limite, on a $|f| \le g$ p.p. Par croissance de l'intégrale, $\int |f| \le \int g < \infty$. Donc $f$ est intégrable.
2. **Utilisation du Lemme de Fatou (Jalon 68) sur des fonctions positives :**
   Considérons la suite $h_n = g + f_n$. Comme $|f_n| \le g$, on a $h_n \ge 0$.
   $$\int \liminf h_n \le \liminf \int h_n$$
   $$\int (g + f) \le \liminf \int (g + f_n)$$
   Par linéarité (car $\int g$ est finie) : $\int g + \int f \le \int g + \liminf \int f_n$.
   D'où : $\int f \le \liminf \int f_n$.
3. **Deuxième application de Fatou :**
   Considérons la suite $k_n = g - f_n \ge 0$.
   $$\int \liminf k_n \le \liminf \int k_n$$
   $$\int (g - f) \le \liminf \int (g - f_n) = \int g - \limsup \int f_n$$
   D'où : $-\int f \le - \limsup \int f_n \implies \limsup \int f_n \le \int f$.
4. **Conclusion :**
   On a $\limsup \int f_n \le \int f \le \liminf \int f_n$.
   Comme $\liminf \le \limsup$, toutes ces valeurs sont égales. L'intégrale converge.

## 4. Exercices d'Application

### Exercice 1 : Calcul de limite d'intégrale
**Énoncé :** Calculer $\lim_{n \to \infty} \int_0^{+\infty} \frac{n \sin(x/n)}{x(1+x^2)} dx$.
**Correction Détaillée :**
1. **Convergence simple :** On sait que $\sin(u) \sim u$ au voisinage de 0.
   $n \sin(x/n) = n [x/n + o(1/n)] = x + o(1)$.
   La limite simple est $f(x) = \frac{x}{x(1+x^2)} = \frac{1}{1+x^2}$.
2. **Domination :** On utilise l'inégalité $|\sin(u)| \le |u|$.
   $|f_n(x)| = \left| \frac{n \sin(x/n)}{x(1+x^2)} \right| \le \frac{n (x/n)}{x(1+x^2)} = \frac{1}{1+x^2}$.
   La fonction $g(x) = \frac{1}{1+x^2}$ est intégrable sur $[0, +\infty[$ (primitive $\arctan$).
3. **Application :** Par TCD, la limite est $\int_0^{+\infty} \frac{1}{1+x^2} dx = [\arctan(x)]_0^{+\infty} = \pi/2$.

### Exercice 2 : Niveau Avancé (Dérivation sous le signe somme)
**Énoncé :** Retrouver la règle de Leibniz (Jalon 40) à l'aide du TCD.
**Correction Détaillée :**
On écrit le taux d'accroissement $\frac{F(x+h)-F(x)}{h} = \int \frac{f(x+h, t)-f(x, t)}{h} dt$. D'après le théorème des accroissements finis, le terme sous l'intégrale est égal à $\frac{\partial f}{\partial x}(c, t)$. Si cette dérivée est dominée par une fonction intégrable, on applique le TCD pour passer à la limite $h \to 0$.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Le TCD est la garantie mathématique que nos **Espérances** se comportent bien. En apprentissage statistique, il justifie la convergence de la fonction de perte empirique vers la fonction de perte théorique.
- **Example Concret :**
    - **Convergence du Gradient Stochastique (SGD) :** Pour prouver que le gradient calculé sur des données converge vers le vrai gradient du risque, on utilise le TCD. La condition de "domination" revient à dire que la variance de nos gradients ne doit pas exploser.
    - **Robustesse des VAE :** Dans les Variational Auto-Encoders, on maximise l'ELBO. Le passage du gradient à travers l'intégrale de la distribution latente (Reparameterization Trick) est validé par le TCD.
    - **Loi des Grands Nombres :** La preuve de certaines versions de la loi forte des grands nombres utilise des arguments de convergence dominée pour traiter les moments d'ordre supérieur.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 68 (Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque).md]], [[Jalon 40 (Intégrales dépendant d'un paramètre).md]]
- **Concepts Futurs dépendants :** [[Jalon 75 (Preuve de la complétude des espaces Lp).md]], [[Jalon 80 (Transformée de Fourier dans L1).md]]
