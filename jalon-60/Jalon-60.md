---
uuid: "jalon-60"
title: "Livrable IA T5 : Preuve du théorème d'approximation universelle"
year: 2
trimester: 5
tags:
  - math/analyse
  - ia/theorie
prev: "[[Jalon 59 (Topologie des espaces de fonctions).md]]"
next: "[[Jalon 61 (Insuffisances de l'intégrale de Riemann).md]]"
---

# Jalon 60 : Livrable IA T5 : Preuve du théorème d'approximation universelle

## 1. Genèse et ancrage physique de l'approximation fonctionnelle

L'ambition première de l'intelligence artificielle symbolique s'est heurtée à une barrière géométrique fondamentale : l'incapacité des modèles linéaires, tels que le perceptron initial, à séparer des classes non linéairement séparables, à l'image du célèbre problème du XOR. Cette limitation topologique a plongé le domaine dans une stase conceptuelle. La résolution de cette impasse n'est pas venue de l'ingénierie, mais de l'analyse fonctionnelle la plus pure.

Historiquement, le besoin d'approcher des fonctions complexes par des combinaisons linéaires de fonctions simples trouve ses racines dans les travaux de Joseph Fourier et de Karl Weierstrass (avec le théorème d'approximation de Weierstrass par des polynômes). Toutefois, l'architecture des réseaux de neurones artificiels exigeait une autre forme de base fonctionnelle : des compositions de transformations affines suivies d'une fonction scalaire non linéaire, dite fonction d'activation.

En 1989, George Cybenko, suivi par Kurt Hornik en 1991, a établi un résultat monumental : sous des conditions très souples sur la fonction d'activation, une seule couche cachée composée d'un nombre fini de neurones suffit pour approcher uniformément toute fonction continue sur un domaine compact de $\mathbb{R}^n$. Ce théorème d'approximation universelle agit comme le socle d'existence des réseaux de neurones. Il garantit que l'espace des fonctions modélisables par de tels réseaux est dense dans l'espace des fonctions continues, justifiant ainsi théoriquement la quête d'optimisation (qui consiste à trouver les bons paramètres) puisque l'on sait de façon absolue qu'une configuration satisfaisante existe.

## 2. Définitions topologiques et théorèmes d'approximation

Pour asseoir cette théorie, il convient de définir rigoureusement le cadre topologique dans lequel nous mesurons la "proximité" entre la fonction cible et le réseau de neurones.

### A. Espace des fonctions continues et densité

Soit $K \subset \mathbb{R}^n$ un ensemble compact. L'espace fonctionnel cible est l'espace de Banach $C(K, \mathbb{R})$ des fonctions continues de $K$ dans $\mathbb{R}$, muni de la norme de la convergence uniforme :
$$ \|f\|_{\infty} = \sup_{x \in K} |f(x)| $$

Un sous-ensemble $\mathcal{M} \subset C(K, \mathbb{R})$ est dit dense dans $C(K, \mathbb{R})$ si, pour toute fonction $f \in C(K, \mathbb{R})$ et pour tout $\epsilon > 0$, il existe une fonction $g \in \mathcal{M}$ telle que :
$$ \|f - g\|_{\infty} < \epsilon $$

### B. L'espace des réseaux de neurones à une couche cachée

Soit $\sigma : \mathbb{R} \to \mathbb{R}$ une fonction donnée, appelée **fonction d'activation**. L'ensemble des fonctions réalisables par un réseau de neurones de type "feedforward" à une seule couche cachée, avec $N$ neurones, des poids $w_i \in \mathbb{R}^n$, des biais $b_i \in \mathbb{R}$ et des poids de sortie $\alpha_i \in \mathbb{R}$, est défini par l'espace vectoriel engendré :

$$ \Sigma_n(\sigma) = \left\lbrace x \mapsto \sum_{i=1}^N \alpha_i \sigma(w_i \cdot x + b_i) \ \middle| \ N \in \mathbb{N}, \alpha_i, b_i \in \mathbb{R}, w_i \in \mathbb{R}^n \right\rbrace $$

### C. Théorème d'Approximation Universelle de Cybenko (1989)

**Énoncé formel :**
Soit $\sigma : \mathbb{R} \to \mathbb{R}$ une fonction continue, sigmoïdale, c'est-à-dire vérifiant :
$$ \lim_{t \to -\infty} \sigma(t) = 0 \quad \text{et} \quad \lim_{t \to +\infty} \sigma(t) = 1 $$
Alors, pour tout sous-ensemble compact $K \subset \mathbb{R}^n$, le sous-espace $\Sigma_n(\sigma)$ est dense dans $C(K, \mathbb{R})$.

**Exemple concret immédiat : Approximation d'une fonction échelon**

Considérons $n=1$, $K = [-2, 2]$, et la fonction cible $f(x)$ qui vaut $0$ sur $[-2, 0)$ et $1$ sur $[0, 2]$. Bien que $f$ présente une discontinuité en $0$, nous l'approchons par des fonctions continues. Fixons $\sigma(t) = \frac{1}{1 + e^{-t}}$.
Regardons ce qui se produit si l'on prend un seul neurone ($N=1$) avec un poids $w$ grand, par exemple $g(x) = \sigma(wx) = \frac{1}{1 + e^{-wx}}$.
- Pour $x = -0.1$ et $w = 100$ : $g(-0.1) = \frac{1}{1 + e^{10}} \approx 4.5 \times 10^{-5}$, très proche de $f(-0.1) = 0$.
- Pour $x = 0.1$ et $w = 100$ : $g(0.1) = \frac{1}{1 + e^{-10}} \approx 0.99995$, très proche de $f(0.1) = 1$.
- En $x = 0$, $g(0) = \frac{1}{1+1} = 0.5$.
En augmentant le poids géométrique $w$, la pente de la sigmoïde à l'origine augmente, et l'écart maximal $\|f - g\|_{\infty}$ (sauf au voisinage infinitésimal de la discontinuité) devient arbitrairement petit. Par une combinaison linéaire (soustraction) de deux telles sigmoïdes décalées par un biais $b$, on peut construire une fonction indicatrice (fonction créneau) très précise sur un intervalle arbitraire.

### D. Cas pathologique : Activation polynomiale

Si la fonction d'activation $\sigma(t)$ est un polynôme de degré $d$, alors toute fonction $g \in \Sigma_n(\sigma)$ est nécessairement un polynôme de degré au plus $d$. Dans $C(K, \mathbb{R})$, l'ensemble des polynômes de degré au plus $d$ forme un sous-espace vectoriel de dimension finie, qui est toujours fermé et strictement inclus dans l'espace de dimension infinie $C(K, \mathbb{R})$. Par conséquent, l'adhérence de $\Sigma_n(\sigma)$ n'est pas l'espace tout entier. Les fonctions d'activation polynomiales ne peuvent donc pas agir comme des approximateurs universels, ce qui explique physiquement pourquoi la non-linéarité des réseaux de neurones ne doit pas être un polynôme global.

## 3. Démonstration fondamentale par l'Analyse Fonctionnelle

La preuve originelle de Cybenko mobilise la théorie de la mesure et l'analyse fonctionnelle de haut vol. Nous allons l'articuler rigoureusement.

La structure de la preuve repose sur une réduction par l'absurde à l'aide des corollaires du théorème de Hahn-Banach et du théorème de représentation de Riesz-Markov-Kakutani.

**Lemme 1 (Propriété discriminatoire) :**
Une fonction $\sigma$ est dite discriminatoire si, pour toute mesure de Radon finie et signée $\mu$ sur un compact $K \subset \mathbb{R}^n$, l'annulation de l'intégrale suivante pour tout $w \in \mathbb{R}^n, b \in \mathbb{R}$ :
$$ \int_K \sigma(w \cdot x + b) \, d\mu(x) = 0 $$
implique que la mesure $\mu$ est identiquement nulle ($\mu = 0$).

**Lemme 2 (Toute fonction sigmoïdale continue est discriminatoire) :**
*Démonstration du Lemme 2 :*
Soit $\sigma$ une fonction sigmoïdale continue. Supposons qu'il existe une mesure signée $\mu$ telle que $\int_K \sigma(w \cdot x + b) \, d\mu(x) = 0$ pour tous $w, b$.
Fixons un vecteur directionnel $w_0 \in \mathbb{R}^n$ et un scalaire $\theta \in \mathbb{R}$. Considérons la suite de fonctions $h_\lambda(x) = \sigma(\lambda(w_0 \cdot x + \theta) + \phi)$ où on laisse $\lambda \to +\infty$.
Comme $\sigma(t) \to 1$ pour $t \to +\infty$ et $\sigma(t) \to 0$ pour $t \to -\infty$, pour un $\phi$ correctement ajusté, la fonction $h_\lambda(x)$ converge ponctuellement vers la fonction indicatrice du demi-espace $H = \left\lbrace x \in K \mid w_0 \cdot x + \theta > 0 \right\rbrace$.
Par le théorème de convergence dominée de Lebesgue, puisque $\sigma$ est bornée par construction et que $\mu$ est de masse finie totale :
$$ \lim_{\lambda \to +\infty} \int_K \sigma(\lambda(w_0 \cdot x + \theta) + \phi) \, d\mu(x) = \int_K \mathbf{1}_{\{w_0 \cdot x + \theta > 0\}}(x) \, d\mu(x) = \mu(H) $$
Or, par hypothèse de départ sur $\mu$, l'intégrale pré-limite est nulle pour tout $\lambda$. On en déduit que $\mu(H) = 0$ pour tout demi-espace ouvert $H$. Or, l'ensemble des demi-espaces engendre la tribu borélienne de $K$. Une mesure signée nulle sur tous les demi-espaces est nécessairement la mesure nulle (en utilisant les propriétés de la transformée de Fourier de la mesure). Donc $\mu = 0$.

**Démonstration du Théorème d'Approximation Universelle :**

Supposons par l'absurde que $\Sigma_n(\sigma)$ n'est pas dense dans $C(K, \mathbb{R})$.
Puisque $\Sigma_n(\sigma)$ est un sous-espace vectoriel, sa clôture topologique $\overline{\Sigma_n(\sigma)}$ est un sous-espace fermé strictement inclus dans $C(K, \mathbb{R})$.
Par le corollaire du **Théorème de Hahn-Banach** analytique (séparation des convexes fermés), il existe une forme linéaire continue non nulle $L \in C(K, \mathbb{R})^*$ telle que $L$ s'annule sur tout l'espace $\overline{\Sigma_n(\sigma)}$.
En particulier, pour toute fonction de base de la forme $g_{w,b}(x) = \sigma(w \cdot x + b)$, on a :
$$ L(\sigma(w \cdot (\cdot) + b)) = 0 $$
Le **Théorème de représentation de Riesz-Markov-Kakutani** caractérise le dual topologique de $C(K, \mathbb{R})$. Il stipule que toute forme linéaire continue $L$ peut être représentée de manière unique par l'intégration par rapport à une mesure de Radon finie et signée $\mu$ sur $K$. Ainsi :
$$ L(f) = \int_K f(x) \, d\mu(x) \quad \forall f \in C(K, \mathbb{R}) $$
L'annulation de $L$ sur les générateurs du réseau donne la condition :
$$ \int_K \sigma(w \cdot x + b) \, d\mu(x) = 0 \quad \forall w \in \mathbb{R}^n, \forall b \in \mathbb{R} $$
Or, par le Lemme 2, $\sigma$ est discriminatoire, ce qui force la mesure $\mu$ à être la mesure nulle.
Si $\mu = 0$, alors la fonctionnelle $L$ est l'opérateur nul, $L = 0$.
Cela contredit l'existence stipulée par Hahn-Banach d'une forme linéaire non nulle.
Cette contradiction ruine notre hypothèse initiale. Par conséquent, $\Sigma_n(\sigma)$ est dense dans $C(K, \mathbb{R})$.

## 4. Répercussions en Topologie et Architecture des Réseaux

Bien que la preuve de Cybenko soit d'une pureté mathématique frappante, elle s'avère non constructive. Le théorème garantit l'existence d'une certaine largeur de couche $N$, mais ce nombre $N$ croît de manière exponentielle avec la dimension de l'espace d'entrée $n$ (le fameux fléau de la dimension).

Dans les architectures neuronales modernes, la profondeur (nombre de couches successives) pallie ce défaut de la largeur exponentielle. Des théorèmes ultérieurs ont montré que des fonctions présentant certaines topologies hiérarchiques ou compositionnelles, typiques du traitement d'image ou du traitement du langage naturel, peuvent être approximées par des réseaux profonds avec un nombre polynomial de neurones, là où un réseau à une seule couche cachée exigerait un nombre exponentiel de neurones pour atteindre une approximation équivalente.

C'est l'essence géométrique de la théorie de la complexité des modèles en apprentissage automatique profond : la profondeur permet de replier l'espace des entrées de manière compacte, optimisant ainsi drastiquement la dimensionnalité requise pour modéliser des invariants physiques et sémantiques.
