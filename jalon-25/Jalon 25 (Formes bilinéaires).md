---
uuid: "jalon-25"
title: "Formes bilinéaires, formes sesquilinieaires, produit scalaire et inégalité de Cauchy-Schwarz"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/similarite
prev: "[[Jalon-24.md]]"
next: "[[Jalon 26 (Espaces euclidiens).md]]"
---

# Jalon 25 : Formes bilinéaires, formes sesquilinieaires, produit scalaire et inégalité de Cauchy-Schwarz

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez que vous soyez un évaluateur de compatibilité pour un site de rencontre. Un vecteur $x$, c'est le profil d'une personne (ses goûts, son âge, etc.). Une **Forme Bilinéaire**, c'est une règle de calcul qui prend DEUX profils et qui donne un score de compatibilité (un nombre). 
  - Le **Produit Scalaire**, c'est le score parfait : il est positif si les gens se ressemblent, nul s'ils n'ont rien en commun, et maximal si c'est la même personne.
  - L'**Inégalité de Cauchy-Schwarz**, c'est la limite de la ressemblance : elle dit que le score de compatibilité entre deux personnes ne peut jamais dépasser le produit de leur "charisme" individuel (leur norme).
- **Le "Pourquoi on a inventé ça" :** On a besoin de mesurer des angles et des longueurs dans des espaces qui ne sont pas forcément le monde réel en 3D. Le produit scalaire est l'outil universel pour définir la notion de "proximité" et de "direction" dans n'importe quel ensemble de données.
- **Visualisation :** Imaginez projeter un vecteur sur un autre. La longueur de l'ombre portée dépend de la "ressemblance" des deux vecteurs. Le produit scalaire est la mesure de cette ombre.

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $E$ un $\mathbb{K}$-espace vectoriel.
1. **Forme Bilinéaire :** Une application $B : E \times E \to \mathbb{K}$ est bilinéaire si elle est linéaire par rapport à chaque argument :
   - $B(\lambda x + \mu y, z) = \lambda B(x, z) + \mu B(y, z)$
   - $B(x, \lambda y + \mu z) = \lambda B(x, y) + \mu B(x, z)$
2. **Forme Sesquilinéaire (pour $\mathbb{K} = \mathbb{C}$) :** Linéaire à droite et semi-linéaire à gauche : $B(\lambda x, y) = \bar{\lambda} B(x, y)$.
3. **Produit Scalaire :** Une forme bilinéaire symétrique (ou sesquilinéaire hermitienne) $f$ est un produit scalaire si elle est :
   - **Positive :** $\forall x \in E, f(x, x) \ge 0$.
   - **Définie :** $f(x, x) = 0 \iff x = 0_E$.
   On le note généralement $\langle x, y \rangle$ ou $(x \mid y)$.
4. **Norme associée :** $\|x\| = \sqrt{\langle x, x \rangle}$.

### B. Théorèmes, Propositions & Lemmes
> **Inégalité de Cauchy-Schwarz (Fondamentale) :**
> Soit $\langle \cdot, \cdot \rangle$ un produit scalaire sur $E$. Pour tous $x, y \in E$ :
> $$| \langle x, y \rangle | \le \|x\| \cdot \|y\|$$
> L'égalité a lieu si et seulement si $(x, y)$ est une famille liée.

> **Inégalité Minkowski (Triangulaire) :**
> $$\|x + y\| \le \|x\| + \|y\|$$

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : L'Inégalité de Cauchy-Schwarz (Cas réel)
Soit $\langle \cdot, \cdot \rangle$ un produit scalaire réel sur $E$.

1. **Initialisation / Cadre :** Soient $x, y \in E$. 
   - Si $y = 0$, l'inégalité $0 \le 0$ est triviale.
   - Supposons $y \neq 0$. Considérons la fonction $P(\lambda)$ définie pour tout $\lambda \in \mathbb{R}$ par :
     $$P(\lambda) = \|x + \lambda y\|^2$$

2. **Étape 1 : Développement du trinôme**
   Par définition de la norme et bilinéarité :
   $P(\lambda) = \langle x + \lambda y, x + \lambda y \rangle$
   $P(\lambda) = \langle x, x \rangle + \langle x, \lambda y \rangle + \langle \lambda y, x \rangle + \langle \lambda y, \lambda y \rangle$
   En utilisant la symétrie et l'homogénéité :
   $P(\lambda) = \|x\|^2 + 2\lambda \langle x, y \rangle + \lambda^2 \|y\|^2$.

3. **Étape 2 : Analyse du signe**
   Puisqu'un carré est toujours positif (positivité du produit scalaire), on a :
   $$\forall \lambda \in \mathbb{R}, P(\lambda) \ge 0$$
   $P(\lambda)$ est un trinôme du second degré en $\lambda$ de la forme $A\lambda^2 + B\lambda + C$ avec :
   - $A = \|y\|^2$
   - $B = 2\langle x, y \rangle$
   - $C = \|x\|^2$

4. **Étape 3 : Calcul du discriminant**
   Un trinôme du second degré qui garde un signe constant (positif ici) possède un discriminant $\Delta$ négatif ou nul.
   $\Delta = B^2 - 4AC$
   $\Delta = (2\langle x, y \rangle)^2 - 4 \|y\|^2 \|x\|^2$
   $\Delta = 4 \langle x, y \rangle^2 - 4 \|x\|^2 \|y\|^2$.

5. **Étape 4 : Conclusion de l'inégalité**
   $\Delta \le 0 \implies 4 \langle x, y \rangle^2 \le 4 \|x\|^2 \|y\|^2$.
   En simplifiant par 4 :
   $\langle x, y \rangle^2 \le \|x\|^2 \|y\|^2$.
   En passant à la racine carrée :
   $$| \langle x, y \rangle | \le \|x\| \cdot \|y\|$$

6. **Conclusion :** L'inégalité de Cauchy-Schwarz est démontrée.

## 4. Exercices d'Application
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Produit scalaire de fonctions
**Énoncé :** Sur $E = C([0, 1], \mathbb{R})$, on définit $\langle f, g \rangle = \int_0^1 f(t)g(t)dt$. Vérifier que c'est un produit scalaire.
**Correction Détaillée :**
1. **Bilinéarité & Symétrie :** Immédiates par linéarité et commutativité de l'intégrale.
2. **Positivité :** $\langle f, f \rangle = \int_0^1 f(t)^2 dt$. Comme $f(t)^2 \ge 0$, l'intégrale d'une fonction positive est positive.
3. **Caractère Défini :** Supposons $\int_0^1 f(t)^2 dt = 0$.
   - $f^2$ est une fonction continue et positive sur $[0, 1]$.
   - Si l'intégrale d'une fonction continue positive est nulle, alors la fonction est identiquement nulle.
   - $\forall t \in [0, 1], f(t)^2 = 0 \implies f(t) = 0$.
**Conclusion :** C'est bien un produit scalaire.

### Exercice 2 : Niveau Avancé (Application de Cauchy-Schwarz)
**Énoncé :** Soient $a_1, ..., a_n$ des réels strictement positifs. Montrer que $(\sum_{i=1}^n a_i) (\sum_{i=1}^n \frac{1}{a_i}) \ge n^2$.
**Correction Détaillée :**
1. Utilisons le produit scalaire canonique sur $\mathbb{R}^n$ : $\langle x, y \rangle = \sum x_i y_i$.
2. Posons les vecteurs $u$ et $v$ suivants :
   - $u = (\sqrt{a_1}, \sqrt{a_2}, ..., \sqrt{a_n})$
   - $v = (\frac{1}{\sqrt{a_1}}, \frac{1}{\sqrt{a_2}}, ..., \frac{1}{\sqrt{a_n}})$
3. Calculons leurs normes :
   - $\|u\|^2 = \sum (\sqrt{a_i})^2 = \sum a_i$.
   - $\|v\|^2 = \sum (\frac{1}{\sqrt{a_i}})^2 = \sum \frac{1}{a_i}$.
4. Calculons le produit scalaire :
   - $\langle u, v \rangle = \sum (\sqrt{a_i} \cdot \frac{1}{\sqrt{a_i}}) = \sum 1 = n$.
5. Appliquons Cauchy-Schwarz : $\langle u, v \rangle^2 \le \|u\|^2 \|v\|^2$.
6. $n^2 \le (\sum a_i) (\sum \frac{1}{a_i})$.
**Conclusion :** L'inégalité est démontrée.

## 5. Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** Le produit scalaire est l'opération de base qui définit la **Similarité** entre deux vecteurs de données.
- **Exemple Concret :** Dans le **Mécanisme d'Attention (Transformers)** de GPT-4 ou BERT, on calcule des scores d'attention en faisant des produits scalaires entre des vecteurs de "Requête" (Query) et de "Clé" (Key) : $\text{Score} = Q \cdot K^T$. Plus le produit scalaire est élevé, plus le modèle "porte attention" à un mot spécifique dans une phrase. L'inégalité de Cauchy-Schwarz garantit que ces scores peuvent être normalisés (via Softmax) pour former une distribution de probabilité cohérente, évitant ainsi que certaines connexions ne dominent de manière aberrante.

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon-7.md|Jalon 7 (Espaces vectoriels abstraits)]], [[Jalon 9 (Calcul matriciel)]]
- **Concepts Futurs dépendants :** [[Jalon 26 (Espaces euclidiens)]], [[Jalon 33 (Formes quadratiques)]], [[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L^2)]], [[Jalon 126 (Noyaux définis positifs)]]
