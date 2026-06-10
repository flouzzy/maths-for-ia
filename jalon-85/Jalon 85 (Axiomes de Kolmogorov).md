---
uuid: "jalon-85"
title: "Axiomes de Kolmogorov"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/abstraction
prev: "[[Jalon 84 (Livrable IA).md]]"
next: "[[Jalon 86 (Variables aléatoires vues comme des applications mesurables).md]]"
---

# Jalon 85 : Axiomes de Kolmogorov

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous ayez un gâteau géant qui représente tout ce qui peut arriver dans le futur (l'univers $\Omega$).
    - Le gâteau entier pèse exactement **1 kilo** (la probabilité totale est 1).
    - Vous découpez le gâteau en tranches. Chaque tranche est un événement (ex: "il va pleuvoir").
    - Le poids d'une tranche, c'est sa probabilité.
    - Les **Axiomes de Kolmogorov**, ce sont les règles d'hygiène pour découper ce gâteau :
        1. Une tranche ne peut pas avoir un poids négatif.
        2. Si vous n'avez pas de tranche, vous n'avez pas de poids ($\emptyset$).
        3. Si vous regroupez des tranches qui ne se touchent pas, le poids total est la somme des poids de chaque tranche.
- **Le "Pourquoi on a inventé ça" :** Avant 1933, les probabilités étaient un peu floues. Andreï Kolmogorov a réalisé qu'une probabilité n'est rien d'autre qu'une **mesure** (comme une longueur ou une aire) appliquée à un espace de possibilités. Cela a permis de donner aux statistiques la même rigueur que la géométrie ou l'algèbre.
- **Visualisation :** Un cercle ($\Omega$) rempli de zones colorées. La probabilité d'une zone est son aire par rapport à l'aire totale du cercle.

## 2. Formalisation

### A. L'Espace de Probabilité

Soit $\Omega$ un ensemble appelé **univers** (l'ensemble des résultats possibles).

> **Définition 1 (Espace de Probabilité) :**
> Un espace de probabilité est un triplet $(\Omega, \mathcal{F}, P)$ où :
> 1. **$\mathcal{F}$** est une tribu sur $\Omega$ (le catalogue des événements mesurables).
> 2. **$P$** est une mesure sur $(\Omega, \mathcal{F})$ vérifiant la condition de normalisation :
>    $$P(\Omega) = 1$$

### B. Les Axiomes de Kolmogorov

Une application $P : \mathcal{F} \to [0, 1]$ est une probabilité si :
1. **Positivité :** $\forall A \in \mathcal{F}, P(A) \ge 0$.
2. **Masse totale :** $P(\Omega) = 1$.
3. **$\sigma$-additivité :** Pour toute suite d'événements $(A_n)$ **incompatibles** (disjoints deux à deux) :
   $$P\left( \bigcup_{n=1}^\infty A_n \right) = \sum_{n=1}^\infty P(A_n)$$

### C. Propriétés Fondamentales

> **Théorème :**
> - $P(\emptyset) = 0$.
> - $P(A^c) = 1 - P(A)$.
> - **Additivité :** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
> - **Continuité monotone :** Si $A_n \uparrow A$, alors $P(A_n) \to P(A)$.

## 3. Démonstrations

### Démonstration : Formule de l'union $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

1. **Décomposition en ensembles disjoints :**
   On peut écrire l'union comme la réunion de trois zones disjointes :
   $A \cup B = (A \setminus (A \cap B)) \cup (B \setminus (A \cap B)) \cup (A \cap B)$.
2. **Utilisation de l'additivité simple :**
   $P(A \cup B) = P(A \setminus (A \cap B)) + P(B \setminus (A \cap B)) + P(A \cap B)$.
3. **Relation avec les ensembles complets :**
   On sait que $A = (A \setminus (A \cap B)) \cup (A \cap B)$, donc $P(A) = P(A \setminus (A \cap B)) + P(A \cap B)$.
   D'où $P(A \setminus (A \cap B)) = P(A) - P(A \cap B)$.
4. **Substitution :**
   $P(A \cup B) = [P(A) - P(A \cap B)] + [P(B) - P(A \cap B)] + P(A \cap B)$.
5. **Conclusion :**
   $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.

## 4. Exercices d'Application

### Exercice 1 : Événements presque sûrs
**Énoncé :** On dit qu'un événement est presque sûr si $P(A)=1$. Montrer que l'intersection dénombrable d'événements presque sûrs est encore presque sûre.
**Correction Détaillée :**
1. Soit $(A_n)$ tels que $P(A_n)=1$. Alors $P(A_n^c) = 0$.
2. On veut $P(\cap A_n)$. Passons au complémentaire : $(\cap A_n)^c = \cup A_n^c$.
3. Par $\sigma$-sous-additivité : $P(\cup A_n^c) \le \sum P(A_n^c) = \sum 0 = 0$.
4. Comme la probabilité est positive, $P(\cup A_n^c) = 0$.
5. Donc $P(\cap A_n) = 1 - 0 = 1$.
**Application :** En IA, si on a une infinité de contraintes qui sont chacune respectées avec probabilité 1, alors elles sont toutes respectées en même temps avec probabilité 1.

### Exercice 2 : Niveau Avancé (Inégalité de Boole-Bonferroni)
**Énoncé :** Montrer que $P(\cup_{i=1}^n A_i) \ge \sum P(A_i) - (n-1)$.
**Correction Détaillée :**
C'est une borne utile quand les probabilités sont très proches de 1. On l'obtient par récurrence ou en passant par les complémentaires et en utilisant l'inégalité de Boole $\sum P(A_i^c) \ge P(\cup A_i^c)$.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** L'IA moderne est **Probabiliste**. Un réseau de neurones ne prédit pas un résultat, il prédit une mesure de probabilité (via Softmax). Les axiomes de Kolmogorov garantissent que cette sortie est mathématiquement valide.
- **Example Concret :**
    - **Calibration des modèles :** On veut qu'un modèle qui annonce "90%" ait raison exactement 9 fois sur 10. Les axiomes de probabilité permettent de définir des métriques de calibration (Brier Score) pour vérifier cette cohérence.
    - **Gestion du Risque :** Dans les systèmes critiques (santé, voiture autonome), on calcule la probabilité de défaillance. Comme cette probabilité doit être minuscule, on utilise les propriétés de continuité de Kolmogorov pour estimer les risques extrêmes à partir de données limitées.
    - **Bayesian Neural Networks :** Au lieu d'avoir des poids fixes, on a une distribution de probabilité sur les poids. L'inférence consiste à manipuler ces mesures sur l'espace des paramètres.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 63 (Définition axiomatique d'une mesure).md]], [[Jalon 62 (Algèbres).md]]
- **Concepts Futurs dépendants :** [[Jalon 86 (Variables aléatoires vues comme des applications mesurables).md]], [[Jalon 133 (Modèle PAC).md]]
