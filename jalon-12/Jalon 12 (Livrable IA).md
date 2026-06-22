---
uuid: "jalon-12"
title: "Livrable IA T1 : Conception théorique d'un moteur de recherche sémantique par similarité cosinus (dualité et géométrie des espaces de plongement) et résolution d'un problème d'algèbre de l'X"
year: 1
trimester: 1
tags:
  - math/synthese
  - ia/recherche-semantique
prev: "[[Jalon 11 (Formes linéaires).md]]"
next: "[[Jalon 13 (Structure de R).md]]"
---
# Jalon 12 : Livrable IA T1 : Conception théorique d'un moteur de recherche sémantique par similarité cosinus (dualité et géométrie des espaces de plongement) et résolution d'un problème d'algèbre de l'X

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez que vous voulez ranger des milliers de livres dans une bibliothèque géante, mais pas par ordre alphabétique. Vous les rangez par "sens". Les livres qui parlent de "Chiens" sont proches de ceux qui parlent de "Loups", mais loin de ceux qui parlent de "Recettes de cuisine". Pour trouver un livre, vous n'utilisez pas de mots-clés exacts, vous lancez un petit drone (votre requête) qui va se poser là où le sens est le plus proche. La **similarité cosinus**, c'est l'outil qui mesure l'angle entre le drone et les livres : plus l'angle est petit, plus ils "regardent" dans la même direction sémantique.
- **Le "Pourquoi on a inventé ça" :** Les ordinateurs ne comprennent pas le sens des mots, ils ne voient que des suites de lettres. Pour faire une recherche intelligente (sémantique), on doit transformer les mots en listes de nombres (vecteurs) dans un espace où la géométrie reflète le sens.
- **Visualisation :** Imaginez des flèches partant de l'origine dans un espace à 3 dimensions (en réalité, il y en a des centaines). Une flèche "Roi" et une flèche "Reine" seront presque confondues. L'angle entre elles est minuscule. C'est ce qu'on appelle la proximité sémantique.

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $E = \mathbb{R}^d$ l'espace des plongements (embeddings) de dimension $d$.
1. **Similarité Cosinus :** Pour deux vecteurs non nuls $u, v \in E$, la similarité cosinus est définie par :
   $$S_C(u, v) = \frac{\langle u, v \rangle}{\|u\| \|v\|} = \cos(\theta)$$
   où $\langle \cdot, \cdot \rangle$ est le produit scalaire usuel et $\| \cdot \|$ la norme euclidienne.
2. **Espace de Plongement :** Un espace vectoriel où chaque entité (mot, document) est représentée par un vecteur $v$ tel que les relations sémantiques sont préservées par des opérations linéaires (ex: $v_{\text{roi}} - v_{\text{homme}} + v_{\text{femme}} \approx v_{\text{reine}}$).
3. **Dualité et Projection :** Une requête $q$ peut être vue comme une forme linéaire $\phi_q(x) = \langle q, x \rangle$ agissant sur la base de données. Maximiser la similarité revient à chercher le vecteur $x$ qui maximise cette forme linéaire sous contrainte de norme.

### B. Théorèmes, Propositions & Lemmes
> **Inégalité de Cauchy-Schwarz (Conséquence directe) :**
> Pour tous $u, v \in \mathbb{R}^d$ :
> $$| \langle u, v \rangle | \le \|u\| \|v\|$$
> L'égalité a lieu si et seulement si $u$ et $v$ sont colinéaires. Cela garantit que $S_C(u, v) \in [-1, 1]$.

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Invariance de la similarité cosinus par homothétie
Montrons que si on amplifie le signal d'un vecteur (multiplication par $\alpha > 0$), la similarité avec un autre vecteur reste inchangée. C'est crucial car la recherche sémantique ne doit dépendre que de la direction (le sens) et non de la norme (la longueur du texte).

1. **Initialisation / Cadre :** Soient $u, v \in \mathbb{R}^d \setminus \{0\}$ et $\alpha \in \mathbb{R}$ tel que $\alpha > 0$. Posons $u' = \alpha u$.

2. **Étape 1 : Calcul du produit scalaire modifié**
   $\langle u', v \rangle = \langle \alpha u, v \rangle$.
   Par linéarité à gauche du produit scalaire :
   $$\langle u', v \rangle = \alpha \langle u, v \rangle$$

3. **Étape 2 : Calcul de la norme modifiée**
   $\|u'\| = \sqrt{\langle \alpha u, \alpha u \rangle}$.
   $\|u'\| = \sqrt{\alpha^2 \langle u, u \rangle} = |\alpha| \sqrt{\langle u, u \rangle}$.
   Comme $\alpha > 0$, $|\alpha| = \alpha$.
   $$\|u'\| = \alpha \|u\|$$

4. **Étape 3 : Calcul de la similarité cosinus de $(u', v)$**
   $S_C(u', v) = \frac{\langle u', v \rangle}{\|u'\| \|v\|}$
   Substituons les résultats des étapes 1 et 2 :
   $S_C(u', v) = \frac{\alpha \langle u, v \rangle}{(\alpha \|u\|) \|v\|}$
   En simplifiant par $\alpha$ (puisque $\alpha \neq 0$) :
   $S_C(u', v) = \frac{\langle u, v \rangle}{\|u\| \|v\|} = S_C(u, v)$.

5. **Conclusion :** La similarité cosinus est invariante par multiplication par un scalaire positif. Cela démontre géométriquement pourquoi cette mesure est robuste à la variation de fréquence des mots dans un document.

## 4. Exercices d'Application
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application IA (Calcul de distance sémantique)
**Énoncé :** Soient trois documents représentés par des vecteurs de dimension 3 :
$Q$ (Requête) $= (1, 1, 0)$, $D_1$ (Spam) $= (2, 2, 0)$, $D_2$ (Info) $= (0, 1, 1)$.
Lequel des deux documents est le plus "proche" de la requête selon la similarité cosinus ?
**Correction Détaillée :**
1. **Normes :**
   - $\|Q\| = \sqrt{1^2 + 1^2 + 0^2} = \sqrt{2}$.
   - $\|D_1\| = \sqrt{2^2 + 2^2 + 0^2} = \sqrt{8} = 2\sqrt{2}$.
   - $\|D_2\| = \sqrt{0^2 + 1^2 + 1^2} = \sqrt{2}$.
2. **Produits Scalaires :**
   - $\langle Q, D_1 \rangle = (1 \times 2) + (1 \times 2) + (0 \times 0) = 4$.
   - $\langle Q, D_2 \rangle = (1 \times 0) + (1 \times 1) + (0 \times 1) = 1$.
3. **Similarités :**
   - $S_C(Q, D_1) = \frac{4}{\sqrt{2} \times 2\sqrt{2}} = \frac{4}{2 \times 2} = 1$. (Angle de 0°)
   - $S_C(Q, D_2) = \frac{1}{\sqrt{2} \times \sqrt{2}} = \frac{1}{2} = 0.5$. (Angle de 60°)
**Conclusion :** $D_1$ est le document le plus proche (parfaite corrélation).

### Exercice 2 : Problème d'Algèbre (Inspiré de l'X)
**Énoncé :** Soit $E$ un espace vectoriel de dimension $n$ et $H_1, ..., H_p$ des hyperplans. Montrer que $\dim (\bigcap_{i=1}^p H_i) \ge n - p$.
**Correction Détaillée :**
1. Chaque hyperplan $H_i$ est le noyau d'une forme linéaire $\phi_i \in E^*$.
2. L'intersection $\bigcap H_i$ est le noyau de l'application linéaire $\Phi : E \to \mathbb{K}^p$ définie par $\Phi(x) = (\phi_1(x), ..., \phi_p(x))$.
3. Par le théorème du rang : $\dim E = \dim(\ker \Phi) + \text{rg}(\Phi)$.
4. L'image de $\Phi$ est un sous-espace de $\mathbb{K}^p$, donc sa dimension est au plus $p$. Ainsi, $\text{rg}(\Phi) \le p$.
5. On en déduit : $\dim(\ker \Phi) = \dim E - \text{rg}(\Phi) \ge n - p$.
**Conclusion :** L'intersection de $p$ hyperplans est de dimension au moins $n-p$.

## 5. Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** Ce jalon réalise la synthèse entre l'**Algèbre Linéaire Abstraite** (hyperplans, dualité) et l'**Ingénierie des Données**.
- **Exemple Concret :** Dans les **Bases de Données Vectorielles** (comme Pinecone, Milvus ou FAISS), on stocke des millions de vecteurs de haute dimension. Pour répondre à une requête en millisecondes, on utilise des structures d'**Indexation Spatiale** qui partitionnent l'espace par des **Hyperplans de séparation**. Le calcul de similarité cosinus est l'opération atomique effectuée des milliards de fois par jour pour alimenter ChatGPT, les moteurs de recherche et les systèmes de traduction.

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon-8]], [[Jalon 9 (Calcul matriciel)]], [[Jalon 11 (Formes linéaires)]]
- **Concepts Futurs dépendants :** [[Jalon 13 (Structure de R)]], [[Jalon 26 (Espaces euclidiens)]], [[Jalon 60 (Livrable IA)]]
