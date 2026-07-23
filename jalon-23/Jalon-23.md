---
uuid: "jalon-23"
title: "Séries entières, calcul du rayon de convergence (règle de d'Alembert-Cauchy) et propriétés de la somme"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/modelisation-analytique
prev: "[[Jalon-22.md]]"
next: "[[Jalon-24.md]]"
---
# Jalon 23 : Séries entières, calcul du rayon de convergence et propriétés de la somme

## 1. Intuition et genèse du concept

Historiquement, l'étude des séries entières est née d'un désir profond : celui d'étendre la puissance et la maniabilité des polynômes à des objets analytiques beaucoup plus complexes. Dès le XVIIe siècle, des esprits comme Isaac Newton, James Gregory et Colin Maclaurin se heurtent à la difficulté d'évaluer des fonctions transcendantes telles que le sinus, le logarithme ou l'exponentielle. Ces fonctions échappent aux opérations arithmétiques fondamentales (addition, soustraction, multiplication, division).

La révélation consista à se demander s'il était possible de représenter ces courbes mystérieuses localement par une superposition infinie de fonctions puissances. C'est l'essence même de l'approximation de Taylor portée à l'infini. Au lieu de se contenter d'une tangente (une droite locale) ou d'une parabole osculatrice, les mathématiciens ont forgé un outil qui épouse parfaitement la courbe sur un certain domaine, un domaine de validité.

Cependant, sommer une infinité de termes n'est jamais anodin. Le spectre de la divergence rôde. Contrairement à un polynôme qui peut être évalué paisiblement sur toute la droite réelle ou le plan complexe, une série de puissances peut violemment diverger si l'on s'éloigne trop de son centre de développement. Cette contrainte spatiale fait émerger une figure géométrique fondamentale : le disque de convergence. Imaginez un phare situé à l'origine du plan complexe, balayant l'espace environnant : à l'intérieur du faisceau lumineux (le disque ouvert), la fonction est parfaitement définie, infiniment dérivable, lisse et structurée. En dehors, ce sont les ténèbres de la divergence grossière. Sur la frontière même du faisceau, le cercle d'incertitude, la situation requiert des analyses d'une grande finesse analytique.

## 2. Formalisation et structures algébriques

### 2.1. Définition canonique d'une série entière

**A. Énoncé Symbolique Strict**
Soit $\mathbb{K}$ le corps des réels $\mathbb{R}$ ou des complexes $\mathbb{C}$. On appelle série entière de la variable $z \in \mathbb{K}$ centrée en l'origine, toute série de fonctions de la forme $\sum_{n \geq 0} a_n z^n$, où $(a_n)_{n \in \mathbb{N}}$ est une suite d'éléments de $\mathbb{K}$.

**B. Anatomie et Typage Chirurgical**
- $\mathbb{K} \in \{\mathbb{R}, \mathbb{C}\}$ désigne le corps de base muni de sa valeur absolue usuelle (ou de son module).
- $z \in \mathbb{K}$ est la variable de la fonction. L'étude est de nature locale, souvent au voisinage de $0$.
- $(a_n)_{n \in \mathbb{N}} \in \mathbb{K}^{\mathbb{N}}$ constitue la suite des coefficients de la série entière. C'est l'unique paramètre définissant la série.
- $\sum_{n \geq 0} a_n z^n$ dénote, pour un $z$ fixé, la série numérique de terme général $u_n = a_n z^n$. Le but est d'étudier l'ensemble des $z$ pour lesquels la suite des sommes partielles $S_N(z) = \sum_{n=0}^{N} a_n z^n$ converge dans $\mathbb{K}$.

**C. Exemples de Validation**
- $\sum_{n \geq 0} 1 \cdot z^n$. C'est la série géométrique, où $a_n = 1$ pour tout $n \in \mathbb{N}$.
- $\sum_{n \geq 0} 0 \cdot z^n = 0$. La série nulle converge pour tout $z \in \mathbb{K}$.

**D. Cas Pathologiques et Contre-exemples**
La série entière $\sum_{n \geq 0} n! z^n$ (où $a_n = n!$). La factorielle croît à une vitesse vertigineuse, supérieure à toute croissance géométrique.

### 2.2. Le Lemme fondamental d'Abel

Ce lemme est la pierre angulaire de la théorie. Il relie une propriété de bornitude locale à une propriété de convergence absolue globale sur un disque.

**A. Énoncé Symbolique Strict**
Soit $\sum_{n \geq 0} a_n z^n$ une série entière. S'il existe un scalaire $z_0 \in \mathbb{K}^*$ tel que la suite numérique $(a_n z_0^n)_{n \in \mathbb{N}}$ soit bornée, alors :
Pour tout $z \in \mathbb{K}$ tel que $|z| < |z_0|$, la série $\sum_{n \geq 0} a_n z^n$ est absolument convergente.
De surcroît, pour tout réel $r$ tel que $0 < r < |z_0|$, la série converge normalement sur le disque fermé $\overline{D}(0, r) = \{z \in \mathbb{K} \mid |z| \leq r\}$.

**B. Anatomie et Typage Chirurgical**
- $z_0 \in \mathbb{K}^*$ est un point non nul servant de jalon.
- L'hypothèse "$(a_n z_0^n)_{n \in \mathbb{N}}$ bornée" s'écrit formellement : $\exists M > 0, \forall n \in \mathbb{N}, |a_n z_0^n| \leq M$.
- La conclusion est dichotomique : convergence ponctuelle absolue sur le disque ouvert $D(0, |z_0|)$, et convergence uniforme (normale) sur tout compact (les disques fermés de rayon $r < |z_0|$).

**C. Exemples de Validation**
Prenons la série $\sum z^n / n$. Pour $z_0 = 1$, le terme général est $1/n$ qui est borné (par $1$). Donc la série converge absolument pour tout $z$ tel que $|z| < 1$.

**D. Cas Pathologiques**
Le lemme ne garantit rien pour $|z| = |z_0|$. Dans l'exemple précédent avec $z_0 = 1$, la série diverge en $z=1$ (série harmonique) mais converge conditionnellement en $z=-1$ (critère spécial des séries alternées).

### 2.3. L'existence du Rayon de Convergence

**A. Énoncé Symbolique Strict**
Pour toute série entière $\sum a_n z^n$, il existe un unique élément $R \in \mathbb{R}^+ \cup \{+\infty\}$ appelé rayon de convergence, tel que :
1. $\forall z \in \mathbb{K}, |z| < R \implies \sum a_n z^n$ converge absolument.
2. $\forall z \in \mathbb{K}, |z| > R \implies \sum a_n z^n$ diverge grossièrement (le terme général ne tend pas vers $0$).

On a la formule explicite : $R = \sup \{ r \in \mathbb{R}^+ \mid (a_n r^n)_{n \in \mathbb{N}} \text{ est bornée} \}$.

**B. Anatomie et Typage Chirurgical**
- $R$ est un suprémum dans l'ensemble des réels positifs achevé. Il quantifie la portée du "faisceau" de convergence.
- L'ensemble $E = \{ r \geq 0 \mid (a_n r^n) \text{ est bornée} \}$ contient toujours au moins $0$ (car pour $r=0$, $(a_n 0^n)$ est nulle pour $n>0$, donc bornée). L'ensemble est non vide, son supremum dans $\overline{\mathbb{R}}$ existe toujours.

### 2.4. Le calcul du Rayon par la Règle de d'Alembert

**A. Énoncé Symbolique Strict**
Soit $\sum a_n z^n$ une série entière telle que, pour $n$ suffisamment grand, $a_n \neq 0$.
Si le quotient $\left| \frac{a_{n+1}}{a_n} \right|$ admet une limite $L \in \mathbb{R}^+ \cup \{+\infty\}$ lorsque $n \to +\infty$, alors le rayon de convergence $R$ est donné par $R = \frac{1}{L}$ (avec les conventions usuelles $1/0 = +\infty$ et $1/+\infty = 0$).

**B. Anatomie et Typage Chirurgical**
- $a_n \neq 0$ pour assurer l'existence du dénominateur.
- La limite $L$ mesure la vitesse asymptotique de croissance du rapport des coefficients.
- La règle n'est qu'une condition suffisante. Si le rapport ne possède pas de limite, il faut utiliser la règle de Cauchy (faisant intervenir la racine n-ième, $\limsup |a_n|^{1/n}$).

## 3. Démonstrations pas-à-pas

### 3.1. Preuve détaillée du Lemme d'Abel

Procédons par une construction rigoureuse.
Soit $\sum a_n z^n$ une série entière.
Supposons l'existence d'un $z_0 \in \mathbb{K}^*$ et d'un réel $M > 0$ tels que $\forall n \in \mathbb{N}, |a_n z_0^n| \leq M$.

Soit $z \in \mathbb{K}$ tel que $|z| < |z_0|$. Notre objectif est de prouver la convergence absolue de la série en $z$.
Isolons le terme de la série et forçons l'apparition du terme borné. Pour tout $n \in \mathbb{N}$ :
$$|a_n z^n| = |a_n| \cdot |z|^n$$
En multipliant et divisant par la quantité non nulle $|z_0|^n$ :
$$|a_n z^n| = |a_n| \cdot |z_0|^n \cdot \frac{|z|^n}{|z_0|^n}$$
Ce qui s'écrit :
$$|a_n z^n| = |a_n z_0^n| \cdot \left| \frac{z}{z_0} \right|^n$$
Nous savons, par l'hypothèse de bornitude, que $|a_n z_0^n| \leq M$. On obtient l'inégalité de majoration :
$$|a_n z^n| \leq M \cdot \left| \frac{z}{z_0} \right|^n$$
Posons $q = \left| \frac{z}{z_0} \right|$. Puisque $|z| < |z_0|$ par hypothèse, nous avons un scalaire $q$ tel que $0 \leq q < 1$.
La série géométrique de terme général $M q^n$ est donc convergente, car sa raison $q$ appartient à l'intervalle $[0, 1[$.
Par le théorème de comparaison pour les séries à termes réels positifs, la série $\sum |a_n z^n|$ converge nécessairement.
La série $\sum a_n z^n$ est donc absolument convergente pour $|z| < |z_0|$.

Maintenant, montrons la convergence normale sur un disque fermé $\overline{D}(0, r)$ où $0 < r < |z_0|$.
Soit $z \in \overline{D}(0, r)$. On a $|z| \leq r$.
Reprenons la majoration établie précédemment pour le terme général :
$$|a_n z^n| = |a_n| \cdot |z|^n \leq |a_n| \cdot r^n$$
En réappliquant l'astuce de multiplication et division par $|z_0|^n$ :
$$|a_n| \cdot r^n = |a_n z_0^n| \cdot \left( \frac{r}{|z_0|} \right)^n \leq M \cdot \left( \frac{r}{|z_0|} \right)^n$$
La norme uniforme de la fonction $u_n : z \mapsto a_n z^n$ sur le disque $\overline{D}(0, r)$ vérifie :
$$||u_n||_{\infty, \overline{D}(0, r)} \leq M \cdot \left( \frac{r}{|z_0|} \right)^n$$
Or, $r < |z_0| \implies \frac{r}{|z_0|} < 1$.
La série numérique de terme général majorant $M \left( \frac{r}{|z_0|} \right)^n$ est une série géométrique de raison strictement inférieure à 1. Elle converge.
Par définition, la série de fonctions $\sum u_n$ converge normalement sur $\overline{D}(0, r)$. La démonstration est achevée.

### 3.2. Preuve de la Règle de d'Alembert pour le Rayon

Soit la série entière $\sum a_n z^n$ avec $a_n \neq 0$ au voisinage de l'infini et $\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = L$.
Pour un $z \in \mathbb{K} \setminus \{0\}$ fixé, considérons la série numérique de terme général $v_n = |a_n z^n|$.
Calculons le rapport successif pour appliquer le critère de d'Alembert usuel sur les séries numériques :
$$\frac{v_{n+1}}{v_n} = \frac{|a_{n+1} z^{n+1}|}{|a_n z^n|} = \left| \frac{a_{n+1}}{a_n} \right| \cdot |z|$$
Par hypothèse sur la limite $L$, nous avons :
$$\lim_{n \to \infty} \frac{v_{n+1}}{v_n} = L \cdot |z|$$
Analysons les trois cas imposés par la limite du critère de d'Alembert :
Cas 1 : $L \in ]0, +\infty[$.
Si $L \cdot |z| < 1$, c'est-à-dire si $|z| < \frac{1}{L}$, alors par le critère de d'Alembert, la série $\sum v_n = \sum |a_n z^n|$ converge.
Si $L \cdot |z| > 1$, c'est-à-dire si $|z| > \frac{1}{L}$, le rapport $\frac{v_{n+1}}{v_n}$ devient strictement supérieur à $1$ pour $n$ assez grand. La suite $(v_n)$ ne peut converger vers $0$, violant la condition nécessaire de convergence. La série diverge.
Ceci correspond très exactement à la définition du rayon de convergence $R$. Nous concluons que $R = \frac{1}{L}$.

Cas 2 : $L = 0$.
Pour tout $z \in \mathbb{K}$, $L \cdot |z| = 0 < 1$. La série $\sum |a_n z^n|$ converge pour tout $z$. Le domaine de convergence est $\mathbb{K}$ tout entier. Par définition, le rayon est $R = +\infty = \frac{1}{0^+}$.

Cas 3 : $L = +\infty$.
Pour tout $z \in \mathbb{K}^*$, la limite du rapport est $+\infty > 1$. La série diverge grossièrement partout en dehors de l'origine $z=0$. Le rayon est donc $R = 0 = \frac{1}{+\infty}$.
La démonstration est intégralement clôturée.

## 4. Propriétés Analytiques de la Somme

Sur le disque ouvert de convergence, la somme d'une série entière jouit de propriétés de régularité remarquables.

**A. Énoncé Symbolique Strict**
Soit $\sum a_n z^n$ de rayon $R > 0$. La fonction somme $S(z) = \sum_{n=0}^{+\infty} a_n z^n$ est continue sur le disque ouvert de convergence $D(0, R)$.
De plus, si la variable est réelle ($x \in ]-R, R[$), la fonction somme $S(x)$ est de classe $C^\infty$ sur $]-R, R[$. Sa dérivée première est obtenue par dérivation terme à terme :
$$S'(x) = \sum_{n=1}^{+\infty} n a_n x^{n-1}$$
Et le rayon de convergence de la série dérivée est identique à $R$.

**B. Anatomie et Typage Chirurgical**
- La continuité découle directement de la convergence normale (et donc uniforme) sur tout compact $\overline{D}(0, r)$ pour $r < R$, le terme général étant lui-même continu.
- La dérivation terme à terme est le privilège des séries de fonctions régulières. Elle traduit l'inversion des limites entre l'opérateur de sommation infinie et l'opérateur de dérivation.
