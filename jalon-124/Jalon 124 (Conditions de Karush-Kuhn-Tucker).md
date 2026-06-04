---
uuid: "jalon-124"
title: "Conditions de Karush-Kuhn-Tucker (KKT)"
year: 3
trimester: 11
tags:
  - math/optimisation
  - ia/fondations
prev: "[[Jalon 123 (Problèmes d'optimisation sous contraintes).md]]"
next: "[[Jalon 125 (Opérateurs proximaux).md]]"
---

# Jalon 124 : Conditions de Karush-Kuhn-Tucker (KKT)

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous poussiez un gros carton (l'objectif à minimiser) vers un coin de la pièce.
    - Tant que le carton est au milieu, vous pouvez le pousser librement.
    - Mais à un moment, le carton touche le mur (une **contrainte**). Vous continuez à pousser, mais le mur repousse le carton avec une force exactement opposée à la vôtre.
    - L'équilibre parfait est atteint quand votre poussée et la résistance des murs s'annulent.
    - Les **Conditions KKT**, c'est la liste de vérification pour s'assurer que vous êtes bien à cet équilibre :
        1. Les forces s'annulent (**Stationnarité**).
        2. Le carton est bien dans la pièce (**Admissibilité primale**).
        3. Le mur ne vous "aspire" pas, il ne fait que repousser (**Admissibilité duale**).
        4. Si le carton ne touche pas un mur, ce mur ne pousse pas (**Écart complémentaire**).
- **Le "Pourquoi on a inventé ça" :** Pour transformer un problème d'optimisation avec des "barrières" (inégalités) en un simple système d'équations à résoudre. C'est le couteau suisse de l'optimisation moderne.
- **Visualisation :** Le gradient de la fonction objectif pointant vers l'extérieur de la zone autorisée, exactement compensé par une combinaison des gradients des contraintes.

## 2. Formalisation & Rigueur Académique

Soit le problème d'optimisation (Primal) défini au Jalon 123 :
$\min f_0(x)$ s.t. $f_i(x) \le 0$ ($i=1 \dots m$) and $h_j(x) = 0$ ($j=1 \dots p$).

### A. Les 4 Conditions KKT

Un point $x^*$ (primal) et des multiplicateurs $(\lambda^*, \nu^*)$ (duaux) vérifient les conditions KKT si :

1. **Stationnarité :** Le gradient du Lagrangien est nul en $x^*$.
   $$\nabla f_0(x^*) + \sum_{i=1}^m \lambda_i^* \nabla f_i(x^*) + \sum_{j=1}^p \nu_j^* \nabla h_j(x^*) = 0$$
2. **Admissibilité Primale :** Les contraintes sont respectées.
   $$f_i(x^*) \le 0 \quad \text{et} \quad h_j(x^*) = 0$$
3. **Admissibilité Duale :** Les forces de rappel des inégalités sont positives.
   $$\lambda_i^* \ge 0$$
4. **Écart Complémentaire (Complementary Slackness) :**
   $$\lambda_i^* f_i(x^*) = 0 \quad \text{pour tout } i$$
   Cela signifie que soit la contrainte est **active** ($f_i=0$), soit le multiplicateur est **nul** ($\lambda_i=0$).

### B. Importance de la Convexité

> **Théorème :**
> - **Nécessité :** Pour un problème quelconque, si $x^*$ est optimal et que les contraintes sont "qualifiées" (ex: Slater), alors les conditions KKT sont nécessaires.
> - **Suffisance :** Si le problème est **convexe** (fonctions $f_0, f_i$ convexes et $h_j$ affines), alors les conditions KKT sont **suffisantes** pour garantir l'optimalité globale.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Pourquoi la slackness est-elle nulle à l'optimum ?

Supposons que la dualité forte soit vérifiée ($f_0(x^*) = g(\lambda^*, \nu^*)$).

1. **Définition de g :** $g(\lambda^*, \nu^*) = \inf_x \mathcal{L}(x, \lambda^*, \nu^*)$.
2. **Inégalité :** Par définition de l'infimum :
   $g(\lambda^*, \nu^*) \le \mathcal{L}(x^*, \lambda^*, \nu^*) = f_0(x^*) + \sum \lambda_i^* f_i(x^*) + \sum \nu_j^* h_j(x^*)$.
3. **Utilisation des contraintes :** Comme $x^*$ est admissible, $h_j(x^*)=0$ et $f_i(x^*) \le 0$. Comme $\lambda_i^* \ge 0$, alors $\lambda_i^* f_i(x^*) \le 0$.
4. **Simplification :** On a donc $g(\lambda^*, \nu^*) \le f_0(x^*) + \text{termes négatifs} \le f_0(x^*)$.
5. **Égalité :** Comme on a supposé la dualité forte ($g = f_0$), toutes les inégalités ci-dessus doivent être des **égalités**.
6. **Conclusion :** Pour que $f_0(x^*) + \sum \lambda_i^* f_i(x^*) = f_0(x^*)$, il faut impérativement que la somme soit nulle. Comme chaque terme est négatif, chaque terme doit être nul : $\lambda_i^* f_i(x^*) = 0$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Minimisation sous contrainte de demi-plan
**Énoncé :** Minimiser $f(x, y) = x^2 + y^2$ sous la contrainte $x+y \ge 2$.
**Correction Détaillée :**
1. **Réécriture :** $f_1(x, y) = 2 - x - y \le 0$.
2. **KKT 1 (Stationnarité) :** $\nabla f + \lambda \nabla f_1 = 0 \implies (2x, 2y) + \lambda(-1, -1) = 0 \implies 2x = \lambda, 2y = \lambda$. Donc $x=y$.
3. **KKT 4 (Slackness) :** $\lambda(2 - x - y) = 0$.
   - Si $\lambda = 0$, alors $x=0, y=0$. Mais $0+0 \ge 2$ est faux. Admissibilité primale violée.
   - Donc $2-x-y = 0 \implies 2x = 2 \implies x=1, y=1$.
4. **Vérification :** $\lambda = 2x = 2 \ge 0$. Toutes les conditions sont remplies.
**Résultat :** Le minimum est $(1, 1)$.

### Exercice 2 : Niveau Avancé (Interprétation de $\lambda$)
**Énoncé :** Montrer que $\lambda_i^*$ représente la sensibilité de la valeur optimale par rapport à une petite variation de la contrainte (Shadow Price).
**Correction Détaillée :**
C'est le théorème de l'enveloppe. Si on remplace $f_i \le 0$ par $f_i \le \epsilon$, on montre que $\frac{d f_0^*}{d\epsilon} = -\lambda_i^*$. C'est fondamental en économie et pour le réglage des hyperparamètres en IA.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Les conditions KKT sont la "recette de fabrication" des **algorithmes d'optimisation duale**.
- **Example Concret :**
    - **Support Vector Machines (SVM) :** Les conditions KKT pour les SVM révèlent que le vecteur de poids $w$ est une somme pondérée $\sum \lambda_i y_i x_i$. La condition de slackness dit que $\lambda_i > 0$ uniquement pour les points sur la marge (les **Vecteurs Supports**). Le modèle final ne dépend donc que d'une petite fraction des données.
    - **Calcul de l'Incertitude :** Dans les modèles avec contraintes de confiance, les KKT permettent de calculer comment l'incertitude sur les données se propage vers l'incertitude sur la décision optimale.
    - **Régularisation par le dual :** Certains modèles de vision utilisent des contraintes géométriques dures. On les entraîne en utilisant des couches "KKT" qui résolvent un petit problème d'optimisation à l'intérieur même du réseau de neurones.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 123 (Problèmes d'optimisation sous contraintes).md]], [[Jalon 122 (Notion de sous-gradient).md]]
- **Concepts Futurs dépendants :** [[Jalon 125 (Opérateurs proximaux).md]], [[Jalon 127 (Démonstration du théorème du représentant dans les RKHS).md]]
