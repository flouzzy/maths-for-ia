---
uuid: "jalon-89"
title: "Lemmes de Borel-Cantelli"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/asymptotique
prev: "[[Jalon 88 (Indépendance d'événements).md]]"
next: "[[Jalon 90 (Les modes de convergence).md]]"
---

# Jalon 89 : Lemmes de Borel-Cantelli

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous lanciez une pièce de monnaie tous les jours, pour l'éternité.
    - La question est : allez-vous voir "Pile" apparaître une infinité de fois ?
    - Les **Lemmes de Borel-Cantelli** répondent à cette question en regardant uniquement la somme de vos chances chaque jour.
    - Si la somme de toutes vos chances de gagner est finie (le total est un nombre, ex: 10), alors vous finirez par arrêter de gagner. La chance finira par "s'épuiser".
    - Si la somme est infinie (le total n'a pas de limite) ET que chaque tentative est indépendante, alors vous gagnerez une infinité de fois, c'est **presque sûr**.
- **Le "Pourquoi on a inventé ça" :** En mathématiques, on veut savoir ce qui se passe "à la fin des temps" (à l'infini). Borel-Cantelli est l'outil qui permet de dire si un événement rare va finir par se produire ou s'il va disparaître pour toujours. C'est la base de la **loi du zéro-un** : à l'infini, soit un événement n'arrive plus jamais, soit il arrive tout le temps. Il n'y a pas de milieu.
- **Visualisation :** Une file d'attente infinie de lampes. Si on additionne la probabilité que chaque lampe s'allume, Borel-Cantelli nous dit si nous verrons un clignotement éternel ou si tout finira par s'éteindre.

## 2. Formalisation

Soit $(\Omega, \mathcal{F}, P)$ un espace de probabilité et $(A_n)_{n \in \mathbb{N}}$ une suite d'événements.

### A. L'événement "Infiniment Souvent"

On s'intéresse à l'ensemble des résultats qui appartiennent à une infinité de $A_n$.

> **Définition (Limite supérieure d'événements) :**
> On note $A_{\infty} = \limsup_{n \to \infty} A_n = \bigcap_{n=0}^\infty \bigcup_{k=n}^\infty A_k$.
> $A_{\infty}$ est l'événement : "les événements $A_n$ se réalisent pour une infinité d'indices $n$".

### B. Premier Lemme (Cas général)

> **Théorème 1 :**
> Si la série des probabilités converge :
> $$\sum_{n=0}^\infty P(A_n) < +\infty \implies P(\limsup_{n \to \infty} A_n) = 0$$
> (Presque sûrement, seuls un nombre fini de $A_n$ se réalisent).

### C. Second Lemme (Cas indépendant)

> **Théorème 2 :**
> Si les événements $(A_n)$ sont **indépendants** :
> $$\sum_{n=0}^\infty P(A_n) = +\infty \implies P(\limsup_{n \to \infty} A_n) = 1$$
> (Presque sûrement, une infinité de $A_n$ se réalisent).

## 3. Démonstrations

### Démonstration du Premier Lemme

1. **Expression de la probabilité :** Par définition, $\limsup A_n = \bigcap_{n} B_n$ où $B_n = \bigcup_{k \ge n} A_k$.
2. **Décroissance :** La suite $(B_n)$ est une suite décroissante d'événements ($B_{n+1} \subset B_n$).
3. **Continuité de la mesure :** D'après le Jalon 63 : $P(\limsup A_n) = \lim_{n \to \infty} P(B_n)$.
4. **Majoration par sous-additivité :** Pour tout $n$ :
   $$P(B_n) = P\left( \bigcup_{k=n}^\infty A_k \right) \le \sum_{k=n}^\infty P(A_k)$$
5. **Reste d'une série convergente :** Comme la série $\sum P(A_k)$ converge, son reste $R_n = \sum_{k=n}^\infty P(A_k)$ tend vers 0 quand $n \to \infty$.
6. **Conclusion :** $0 \le P(\limsup A_n) \le \lim R_n = 0$. Donc $P(\limsup A_n) = 0$.

## 4. Exercices d'Application

### Exercice 1 : Le paradoxe du singe savant
**Énoncé :** Un singe tape au hasard sur une machine à écrire. On considère $A_n$ l'événement "le singe tape les oeuvres de Shakespeare entre le caractère $n$ et $n+K$". Montrer qu'il finira par les taper avec probabilité 1.
**Correction Détaillée :**
1. La probabilité $p$ de taper Shakespeare sur un bloc de $K$ caractères est strictement positive (même si elle est minuscule : $p = (1/\text{touches})^K$).
2. On découpe le temps en blocs disjoints et indépendants de taille $K$.
3. La série $\sum P(A_{nK}) = \sum p$ diverge car c'est une somme infinie de la même constante $p > 0$.
4. Par le second lemme de Borel-Cantelli (indépendance des blocs), le singe tapera Shakespeare une infinité de fois presque sûrement.

### Exercice 2 : Niveau Avancé (Convergence de variables)
**Énoncé :** Soit $X_n$ une suite de V.A. telles que $P(|X_n| > \epsilon) \le 1/n^2$. Montrer que $X_n \to 0$ presque sûrement.
**Correction Détaillée :**
Soit $A_n = \{ |X_n| > \epsilon \}$. On a $\sum P(A_n) \le \sum 1/n^2 < \infty$.
Par le premier lemme, $P(\limsup A_n) = 0$.
Cela signifie que pour presque tout $\omega$, il n'y a qu'un nombre fini de $n$ tels que $|X_n(\omega)| > \epsilon$.
Donc $|X_n(\omega)| \le \epsilon$ pour tout $n$ assez grand.
C'est la définition de la convergence presque sûre (Jalon 90).

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Borel-Cantelli est l'outil technique pour prouver la **Convergence Presque Sûre** des algorithmes stochastiques (comme SGD ou Adam).
- **Example Concret :**
    - **Exploration en Reinforcement Learning :** On veut que l'agent visite tous les états possibles une infinité de fois pour être sûr de trouver l'optimal. Si la stratégie d'exploration (ex: $\epsilon$-greedy) décroît trop vite, la série des probabilités d'exploration pourrait converger, et l'agent arrêterait d'explorer prématurément. Borel-Cantelli aide à régler la décroissance de $\epsilon$ pour garantir une exploration éternelle.
    - **Stabilité des réseaux de neurones profonds :** On étudie la probabilité que les gradients "explosent" ou "disparaissent" à une couche $n$ donnée. Si cette probabilité décroît assez vite quand on ajoute des couches, le premier lemme nous garantit que pour un réseau donné, le problème ne se produira qu'un nombre fini de fois (donc sur un nombre fini de couches), assurant la viabilité des modèles très profonds.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 88 (Indépendance d'événements et de variables aléatoires).md]], [[Jalon 63 (Définition axiomatique d'une mesure).md]]
- **Concepts Futurs dépendants :** [[Jalon 90 (Les modes de convergence).md]], [[Jalon 92 (Démonstration rigoureuse de la loi forte des grands nombres.).md]]
