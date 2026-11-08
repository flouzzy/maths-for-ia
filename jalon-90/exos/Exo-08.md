# Exercice 08

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(X_n)$ une suite de variables aléatoires indépendantes et identiquement distribuées, de loi normale $\mathcal{N}(0, 1)$.
Posons $M_n = \max(X_1, X_2, \dots, X_n)$.
Démontrez de manière rigoureuse que $M_n \xrightarrow{\mathbb{P}} +\infty$.
*Indication : Montrez que pour tout $A \in \mathbb{R}$, $\mathbb{P}(M_n \le A) \to 0$.*

**Correction :**

Par définition, dire qu'une suite de variables aléatoires converge en probabilité vers l'infini positif signifie que pour tout seuil $A \in \mathbb{R}$ arbitrairement grand, la probabilité que la variable dépasse ce seuil tend vers 1 (ou, de façon équivalente, la probabilité qu'elle y reste inférieure tend vers 0) :
$$ \lim_{n \to \infty} \mathbb{P}(M_n \le A) = 0 $$

Soit $A \in \mathbb{R}$ un réel arbitraire.
L'événement $\{M_n \le A\}$ signifie que le maximum du n-uplet est inférieur ou égal à $A$. Ceci équivaut strictement au fait que **chaque** variable composant le n-uplet est individuellement inférieure ou égale à $A$.
L'événement s'écrit formellement comme l'intersection :
$$ \{M_n \le A\} = \bigcap_{i=1}^n \{X_i \le A\} $$

Exploitons l'hypothèse structurelle d'indépendance de la suite $(X_n)$. La probabilité de l'intersection d'événements indépendants est égale au produit des probabilités :
$$ \mathbb{P}(M_n \le A) = \mathbb{P}\left(\bigcap_{i=1}^n \{X_i \le A\}\right) = \prod_{i=1}^n \mathbb{P}(X_i \le A) $$

Introduisons l'hypothèse selon laquelle les variables sont identiquement distribuées (loi $\mathcal{N}(0, 1)$). Appelons $F$ la fonction de répartition de la loi normale centrée réduite : $F(A) = \mathbb{P}(X_1 \le A)$.
Le produit devient la puissance $n$-ième :
$$ \mathbb{P}(M_n \le A) = \left( \mathbb{P}(X_1 \le A) \right)^n = (F(A))^n $$

Analysons analytiquement cette quantité. La loi normale est supportée sur $\mathbb{R}$ tout entier, ce qui implique que pour tout $A \in \mathbb{R}$, sa fonction de répartition vérifie l'inégalité stricte :
$$ 0 < F(A) < 1 $$
Posons $q = F(A)$. Nous sommes en présence d'une simple suite géométrique $(q^n)$ de raison $q \in ]0, 1[$.
D'après les théorèmes fondamentaux de l'analyse réelle sur les suites géométriques :
$$ \lim_{n \to \infty} q^n = 0 $$

Par substitution, nous avons rigoureusement prouvé que pour tout $A \in \mathbb{R}$ :
$$ \lim_{n \to \infty} \mathbb{P}(M_n \le A) = \lim_{n \to \infty} (F(A))^n = 0 $$

Ce résultat démontre formellement que la masse de probabilité du maximum de $n$ gaussiennes indépendantes se décale inéluctablement vers $+\infty$ lorsque la taille de l'échantillon croît indéfiniment. On écrit $M_n \xrightarrow{\mathbb{P}} +\infty$.
