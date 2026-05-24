---
uuid: "jalon-94"
title: "Théorème central limite (TCL)"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/asymptotique
prev: "[[Jalon 93 (Fonctions caractéristiques).md]]"
next: "[[Jalon 95 (Vecteurs gaussiens).md]]"
---

# Jalon 94 : Théorème central limite (TCL)

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous demandiez à 1000 personnes de lancer chacune un dé et de noter le résultat.
    - Chaque personne a un résultat imprévisible entre 1 et 6 (une loi uniforme).
    - Maintenant, faites la moyenne de ces 1000 lancers.
    - Le **Théorème Central Limite** dit que si vous répétez cette expérience (1000 nouveaux lancers) plein de fois, la liste de vos moyennes dessinera toujours, absolument toujours, une **courbe en cloche** (une loi Normale).
    - Peu importe que le dé soit truqué ou que la loi de départ soit bizarre : dès qu'on additionne beaucoup de petits phénomènes indépendants, le résultat global devient "Normal". C'est l'ordre qui naît du chaos.
- **Le "Pourquoi on a inventé ça" :** C'est le théorème le plus important des statistiques. Il permet de transformer n'importe quel problème inconnu en un problème de loi Normale, que l'on sait parfaitement résoudre. C'est grâce à lui qu'on peut calculer des marges d'erreur dans les sondages ou les tests médicaux.
- **Visualisation :** La planche de Galton. Des billes tombent à travers des clous et s'éparpillent au hasard. À la fin, elles forment toujours une cloche parfaite au fond de la boîte.

## 2. Formalisation & Rigueur Académique

Soit $(X_n)_{n \in \mathbb{N}^*}$ une suite de variables aléatoires I.I.D. de moyenne $\mu$ et de variance $\sigma^2 > 0$ finie.
On note $S_n = \sum_{i=1}^n X_i$ and $\bar{X}_n = S_n / n$.

### A. Énoncé du TCL (Lindeberg-Lévy)

> **Théorème (Théorème Central Limite) :**
> La variable centrée réduite $Z_n$ converge **en loi** vers une loi normale centrée réduite :
> $$Z_n = \frac{S_n - n\mu}{\sigma \sqrt{n}} = \sqrt{n} \left( \frac{\bar{X}_n - \mu}{\sigma} \right) \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1)$$
> En d'autres termes, pour tous $a < b$ :
> $$\lim_{n \to \infty} P(a \le Z_n \le b) = \int_a^b \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx$$

### B. Vitesse de convergence

Le théorème de Berry-Esseen précise que l'erreur d'approximation est de l'ordre de $1/\sqrt{n}$. Plus on a de données, plus la cloche est parfaite.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration via les fonctions caractéristiques

Supposons sans perte de généralité que $\mu = 0$ and $\sigma = 1$. On veut montrer que $\phi_{Z_n}(t) \to e^{-t^2/2}$.

1. **Expression de Zn :** $Z_n = \frac{1}{\sqrt{n}} \sum_{i=1}^n X_i$.
2. **Fonction caractéristique de Zn :**
   $\phi_{Z_n}(t) = \mathbb{E}[e^{it \frac{1}{\sqrt{n}} \sum X_i}] = \phi_{\sum X_i} (t/\sqrt{n})$.
   Par indépendance (Jalon 93) : $\phi_{Z_n}(t) = [ \phi_X(t/\sqrt{n}) ]^n$.
3. **Développement limité de $\phi_X$ :**
   Comme $\mathbb{E}[X]=0$ and $\mathbb{E}[X^2]=1$, d'après le théorème des moments (Jalon 93) :
   $\phi_X(u) = \phi_X(0) + u \phi_X'(0) + \frac{u^2}{2} \phi_X''(0) + o(u^2)$.
   $\phi_X(u) = 1 + u(i \cdot 0) + \frac{u^2}{2} (i^2 \cdot 1) + o(u^2) = 1 - \frac{u^2}{2} + o(u^2)$.
4. **Substitution :** Posons $u = t/\sqrt{n}$.
   $\phi_{Z_n}(t) = \left( 1 - \frac{t^2}{2n} + o(t^2/n) \right)^n$.
5. **Passage à la limite :**
   On utilise la propriété $\lim_{n \to \infty} (1 + \frac{z}{n})^n = e^z$.
   Ici $z = -t^2/2$.
   $\lim_{n \to \infty} \phi_{Z_n}(t) = e^{-t^2/2}$.
6. **Conclusion :** La limite des fonctions caractéristiques est celle de la loi $\mathcal{N}(0, 1)$. Par le théorème de continuité de Lévy, $Z_n \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1)$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Approximation d'une loi Binomiale
**Énoncé :** On lance $100$ fois une pièce équilibrée. Quelle est la probabilité d'obtenir entre $45$ et $55$ "Pile" ?
**Correction Détaillée :**
1. $X_i \sim \mathcal{B}(0.5)$. $\mu = 0.5$, $\sigma = \sqrt{0.5 \times 0.5} = 0.5$.
2. $n=100$. $S_{100}$ suit une loi $\mathcal{B}(100, 0.5)$.
3. On cherche $P(45 \le S_{100} \le 55)$.
4. Centrage réduit : $Z_{100} = \frac{S_{100} - 50}{0.5 \times \sqrt{100}} = \frac{S_{100} - 50}{5}$.
5. L'intervalle $[45, 55]$ devient $[-1, 1]$ pour $Z_{100}$.
6. Par le TCL : $P \approx P(-1 \le \mathcal{N}(0, 1) \le 1) \approx 0.68$.
(La valeur exacte par calcul binomial est $0.72$, l'écart est dû à la faible valeur de $n$).

### Exercice 2 : Niveau Avancé (Somme de variables de Poisson)
**Énoncé :** Soit $X_n \sim \mathcal{P}(n)$. Montrer que $\frac{X_n - n}{\sqrt{n}} \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1)$.
**Correction Détaillée :**
On remarque qu'une loi $\mathcal{P}(n)$ est la somme de $n$ variables indépendantes de loi $\mathcal{P}(1)$. Le résultat est une application directe du TCL.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Le TCL est la raison pour laquelle la **Loi Normale** est le modèle par défaut pour le bruit en IA.
- **Example Concret :**
    - **Initialisation des poids (Xavier/He Initialization) :** Pour éviter que les activations d'un réseau n'explosent, on initialise les poids avec une variance $1/n$. Comme la sortie d'un neurone est une somme pondérée d'entrées, le TCL garantit que cette sortie suivra une loi Normale, dont on peut contrôler la dispersion.
    - **Diffusion Models :** Ces modèles (DALL-E, Stable Diffusion) ajoutent progressivement du bruit à une image jusqu'à ce qu'elle devienne une purée de pixels. Le TCL garantit que ce bruit accumulé converge vers une distribution Gaussienne parfaite, ce qui simplifie énormément les calculs de reconstruction (Reverse Diffusion).
    - **Estimation d'incertitude :** Dans les systèmes de recommandation, on estime la confiance d'une prédiction en supposant que l'erreur résiduelle est Gaussienne (justifié par le TCL si l'erreur vient de multiples facteurs).

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 93 (Fonctions caractéristiques).md]], [[Jalon 92 (Loi forte des grands nombres (LFGN)).md]]
- **Concepts Futurs dépendants :** [[Jalon 95 (Vecteurs gaussiens).md]], [[Jalon 138 (Inégalités de concentration avancées).md]]
