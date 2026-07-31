---
uuid: "jalon-134"
title: "Complexité des classes de fonctions"
year: 3
trimester: 12
tags:
  - math/probabilites
  - ia/theorie-apprentissage
prev: "[[Jalon 133 (Modele PAC).md]]"
next: "[[Jalon 135 (Complexite de Rademacher).md]]"
---

# Complexité des classes de fonctions

## 1. Présentation du concept clé

**La Métaphore :** Imagine que tu sois un recruteur de talents qui doit engager un spécialiste pour prédire si un film va plaire au public. Tu as deux candidats : le premier n'utilise qu'une seule règle très simple ("si le film a des explosions, ça marche"). Le second a un livre de règles complexe avec un million de critères ("si le film a des explosions, mais que l'acteur principal a les cheveux roux et qu'il pleut dans la scène 4...").

Si tu leur donnes une liste de 10 films récents pour tester leurs compétences, le second candidat pourrait avoir tout bon juste par hasard, parce que ses règles sont tellement flexibles qu'il peut toujours trouver une combinaison qui correspond parfaitement aux 10 exemples. Par contre, si le premier candidat réussit, c'est probablement parce que sa règle simple est vraiment robuste.

En apprentissage automatique, le "candidat" est notre modèle (ou algorithme), et ses "règles" forment ce qu'on appelle une *classe de fonctions*. Si la classe de fonctions est trop riche ou trop "complexe" (comme le deuxième candidat), elle va mémoriser parfaitement les exemples d'entraînement (c'est le *surapprentissage* ou *overfitting*), mais elle se trompera lamentablement sur de nouveaux films.

**Le "Pourquoi on a inventé ça" :** Dans le Jalon précédent (Modèle PAC), nous avons vu comment borner l'erreur d'un modèle lorsque notre classe de fonctions (notre ensemble de règles) est finie. Mais dans la vraie vie, les réseaux de neurones ou les arbres de décision utilisent des classes de fonctions *infinies* ! Comment garantir qu'ils vont généraliser et ne pas juste mémoriser les données ? Les mathématiciens ont dû inventer des moyens de mesurer la "taille" ou la "complexité" d'un ensemble infini de fonctions, en regardant comment ces fonctions se comportent collectivement sur un échantillon de données.

**Visualisation :** Imagine un nuage de points rouges et bleus sur une feuille. Si tu ne peux tracer que des lignes droites pour les séparer (faible complexité), tu n'as pas beaucoup de choix. Si tu peux tracer n'importe quel gribouillis arbitraire (haute complexité), tu peux parfaitement entourer chaque point rouge, mais ton gribouillis n'aura aucun sens logique pour les nouveaux points. La théorie de la complexité mesure exactement à quel point tes gribouillis sont autorisés à être tortueux.

## 2. Formalisation

Le cadre formel bascule dans l'analyse de processus empiriques. Nous cherchons à contrôler l'écart maximal (le *supremum*) entre le risque empirique et le risque réel sur l'ensemble complet d'une classe de fonctions $\mathcal{H}$.

### A. Définitions Formelles

Soit $\mathcal{Z} = \mathcal{X} \times \mathcal{Y}$ un espace probabilisable muni d'une tribu. Soit $\mathbb{P}$ une mesure de probabilité inconnue sur $\mathcal{Z}$.
Soit un échantillon $S = (Z_1, \dots, Z_n) = ((X_1, Y_1), \dots, (X_n, Y_n))$ composé de $n$ variables aléatoires indépendantes et identiquement distribuées (i.i.d.) selon $\mathbb{P}$.

Soit $\mathcal{H}$ une classe de fonctions (l'espace des hypothèses), où chaque $h \in \mathcal{H}$ est une fonction mesurable $h : \mathcal{X} \to \mathcal{Y}$.
Soit $\ell : \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}^+$ une fonction de perte mesurable.
On définit la classe de fonctions de perte induite $\mathcal{F} = \{ f_h : z = (x,y) \mapsto \ell(h(x), y) \mid h \in \mathcal{H} \}$.

Pour une fonction $f \in \mathcal{F}$, on définit :
- **L'espérance vraie (ou Risque réel) :** $\mathbb{E}[f] = \int_{\mathcal{Z}} f(z) d\mathbb{P}(z)$
- **La mesure empirique (ou Risque empirique) :** $\mathbb{E}_n[f] = \frac{1}{n} \sum_{i=1}^n f(Z_i)$

Le cœur de la théorie de l'apprentissage réside dans le contrôle du **processus empirique indexé par $\mathcal{F}$**, défini pour chaque $f \in \mathcal{F}$ par :
$$ (\mathbb{E}_n - \mathbb{E})[f] = \frac{1}{n} \sum_{i=1}^n f(Z_i) - \mathbb{E}[f] $$

L'objet central d'étude est l'écart maximal uniforme sur toute la classe de fonctions :
$$ \Delta_n(\mathcal{F}) = \sup_{f \in \mathcal{F}} \left( \mathbb{E}[f] - \mathbb{E}_n[f] \right) $$

**Définition (Nombres de recouvrement / Covering Numbers) :**
Soit $(T, d)$ un espace métrique et $\epsilon > 0$. Un ensemble $C \subseteq T$ est un $\epsilon$-recouvrement de $T$ si pour tout $x \in T$, il existe $c \in C$ tel que $d(x, c) \leq \epsilon$.
Le nombre de recouvrement $\mathcal{N}(T, d, \epsilon)$ est le cardinal minimal d'un $\epsilon$-recouvrement de $T$.

Pour une classe de fonctions $\mathcal{F}$ et un échantillon fixe $S = (z_1, \dots, z_n)$, on définit la pseudo-métrique empirique $L_1$ :
$$ d_{L_1(S)}(f, g) = \frac{1}{n} \sum_{i=1}^n |f(z_i) - g(z_i)| $$
Le nombre de recouvrement empirique est $\mathcal{N}(\mathcal{F}, d_{L_1(S)}, \epsilon)$.

### B. Théorèmes, Propositions & Lemmes

> **Théorème de l'Inégalité de McDiarmid (1989) :**
> Soient $Z_1, \dots, Z_n$ des variables aléatoires indépendantes à valeurs dans $\mathcal{Z}$.
> Soit $\Phi : \mathcal{Z}^n \to \mathbb{R}$ une fonction satisfaisant la propriété des différences bornées : il existe des constantes $c_1, \dots, c_n > 0$ telles que pour tout $i \in \{1, \dots, n\}$ et pour tous $z_1, \dots, z_n, z_i' \in \mathcal{Z}$,
> $$ \left| \Phi(z_1, \dots, z_i, \dots, z_n) - \Phi(z_1, \dots, z_i', \dots, z_n) \right| \leq c_i $$
> Alors, pour tout $\epsilon > 0$,
> $$ \mathbb{P}\left( \Phi(Z_1, \dots, Z_n) - \mathbb{E}[\Phi(Z_1, \dots, Z_n)] \geq \epsilon \right) \leq \exp\left( - \frac{2\epsilon^2}{\sum_{i=1}^n c_i^2} \right) $$

> **Lemme (Concentration du Supremum du Processus Empirique) :**
> Supposons que pour tout $f \in \mathcal{F}$ et tout $z \in \mathcal{Z}$, on ait $0 \leq f(z) \leq M$.
> Posons $\Phi(S) = \sup_{f \in \mathcal{F}} \left( \mathbb{E}[f] - \mathbb{E}_n[f] \right)$.
> Alors, pour tout $\epsilon > 0$,
> $$ \mathbb{P}\left( \Phi(S) - \mathbb{E}_S[\Phi(S)] \geq \epsilon \right) \leq \exp\left( - \frac{2n\epsilon^2}{M^2} \right) $$

## 3. Démonstrations

### Démonstration du Lemme : Concentration du Supremum du Processus Empirique

Cette démonstration repose sur l'application rigoureuse de l'inégalité de McDiarmid à la fonction supremum du processus empirique.

1. **Initialisation / Cadre :**
   Nous définissons la fonction $\Phi$ appliquée à notre échantillon $S = (Z_1, \dots, Z_n)$ :
   $$ \Phi(z_1, \dots, z_n) = \sup_{f \in \mathcal{F}} \left( \mathbb{E}[f] - \frac{1}{n} \sum_{j=1}^n f(z_j) \right) $$
   Notre but est de vérifier que $\Phi$ satisfait la propriété des différences bornées de McDiarmid.

2. **Étape 1 : Perturbation d'un élément de l'échantillon**
   Soit $i \in \{1, \dots, n\}$. Considérons l'échantillon $S$ et l'échantillon perturbé $S'$ différant uniquement par la $i$-ème coordonnée, remplacée par $z_i'$.
   Nous devons majorer la différence $\Phi(S) - \Phi(S')$.
   Soit $\epsilon' > 0$. Par définition de la borne supérieure, il existe une fonction $f^* \in \mathcal{F}$ (dépendant potentiellement de $S$) telle que :
   $$ \Phi(S) \leq \mathbb{E}[f^*] - \frac{1}{n} \sum_{j=1}^n f^*(z_j) + \epsilon' $$

3. **Étape 2 : Majoration de la différence par le haut**
   Puisque $\Phi(S')$ est le supremum sur toute la classe $\mathcal{F}$, nous avons nécessairement l'inégalité pour la fonction spécifique $f^*$ évaluée sur $S'$ :
   $$ \Phi(S') \geq \mathbb{E}[f^*] - \left( \frac{1}{n} \sum_{j=1, j \neq i}^n f^*(z_j) + \frac{1}{n} f^*(z_i') \right) $$
   Soustrayons cette inégalité de la précédente :
   $$ \Phi(S) - \Phi(S') \leq \left( \mathbb{E}[f^*] - \frac{1}{n} \sum_{j=1}^n f^*(z_j) + \epsilon' \right) - \left( \mathbb{E}[f^*] - \frac{1}{n} \sum_{j=1, j \neq i}^n f^*(z_j) - \frac{1}{n} f^*(z_i') \right) $$
   En distribuant le signe moins et en annulant les termes communs (les $\mathbb{E}[f^*]$ et les sommes pour $j \neq i$) :
   $$ \Phi(S) - \Phi(S') \leq \frac{1}{n} f^*(z_i') - \frac{1}{n} f^*(z_i) + \epsilon' $$

4. **Étape 3 : Application de la borne uniforme**
   Puisque nous savons par hypothèse que pour toute fonction $f \in \mathcal{F}$ et tout $z \in \mathcal{Z}$, les valeurs sont bornées dans $[0, M]$, nous avons :
   $$ f^*(z_i') \leq M \quad \text{et} \quad f^*(z_i) \geq 0 $$
   Donc la différence maximale est :
   $$ f^*(z_i') - f^*(z_i) \leq M $$
   Ce qui implique :
   $$ \Phi(S) - \Phi(S') \leq \frac{M}{n} + \epsilon' $$
   Cette inégalité étant vraie pour tout $\epsilon' > 0$, en faisant tendre $\epsilon'$ vers $0$, on obtient la borne stricte :
   $$ \Phi(S) - \Phi(S') \leq \frac{M}{n} $$

5. **Étape 4 : Symétrie et conclusion sur les différences bornées**
   Par un raisonnement strictement symétrique (en échangeant les rôles de $S$ et $S'$), on trouve également :
   $$ \Phi(S') - \Phi(S) \leq \frac{M}{n} $$
   Par conséquent, la valeur absolue de la différence est bornée :
   $$ \left| \Phi(z_1, \dots, z_n) - \Phi(z_1, \dots, z_i', \dots, z_n) \right| \leq \frac{M}{n} $$
   La fonction $\Phi$ satisfait donc la propriété des différences bornées avec les constantes $c_i = \frac{M}{n}$ pour tout $i \in \{1, \dots, n\}$.

6. **Conclusion : Application du Théorème de McDiarmid**
   On calcule la somme des carrés des constantes :
   $$ \sum_{i=1}^n c_i^2 = \sum_{i=1}^n \left( \frac{M}{n} \right)^2 = n \cdot \frac{M^2}{n^2} = \frac{M^2}{n} $$
   L'application directe de l'inégalité de McDiarmid donne donc :
   $$ \mathbb{P}\left( \Phi(S) - \mathbb{E}_S[\Phi(S)] \geq \epsilon \right) \leq \exp\left( - \frac{2\epsilon^2}{\sum_{i=1}^n c_i^2} \right) = \exp\left( - \frac{2\epsilon^2}{\frac{M^2}{n}} \right) = \exp\left( - \frac{2n\epsilon^2}{M^2} \right) $$
   La concentration exponentielle autour de l'espérance est rigoureusement établie.

## 4. Exercices d'Application

### Exercice 1 : Borne de l'Union pour une Classe Finie

**Énoncé :**
Soit $\mathcal{F} = \{f_1, \dots, f_k\}$ une classe *finie* de fonctions à valeurs dans $[0, 1]$. En utilisant l'inégalité de Hoeffding (un cas particulier de McDiarmid pour des sommes de v.a. indépendantes) et la borne de l'union (Boole), démontrez avec une rigueur absolue que pour tout $\delta > 0$, avec une probabilité d'au moins $1 - \delta$ sur le tirage de l'échantillon $S$ de taille $n$, on a :
$$ \sup_{f \in \mathcal{F}} \left( \mathbb{E}[f] - \mathbb{E}_n[f] \right) \leq \sqrt{\frac{\ln(k) + \ln(1/\delta)}{2n}} $$

**Correction Détaillée :**
* *Analyse de l'énoncé :* Le problème demande de lier l'erreur sur une classe finie à la taille de la classe $k$. L'outil clé est de borner la probabilité d'un "mauvais" événement (l'écart est grand) pour au moins une fonction de la classe.
* *Résolution pas-à-pas :*
  1. Fixons une fonction spécifique $f_j \in \mathcal{F}$. Les variables aléatoires $U_i = f_j(Z_i)$ sont i.i.d. et à valeurs dans $[0, 1]$.
  2. Leur espérance est $\mathbb{E}[U_1] = \mathbb{E}[f_j]$ et leur moyenne empirique est $\frac{1}{n} \sum_{i=1}^n U_i = \mathbb{E}_n[f_j]$.
  3. L'inégalité de Hoeffding classique stipule que pour toute variable aléatoire $U$ à valeurs dans $[a, b]$, $\mathbb{P}\left(\mathbb{E}[U] - \frac{1}{n}\sum U_i \geq \epsilon\right) \leq \exp\left(-\frac{2n\epsilon^2}{(b-a)^2}\right)$.
  4. Ici, $a=0, b=1$. Donc pour la fonction $f_j$ fixe :
     $$ \mathbb{P}\left( \mathbb{E}[f_j] - \mathbb{E}_n[f_j] \geq \epsilon \right) \leq \exp(-2n\epsilon^2) $$
  5. Nous cherchons à évaluer la probabilité que le supremum sur toute la classe dépasse $\epsilon$. Le supremum dépasse $\epsilon$ si et seulement si *au moins une* fonction $f_j$ dépasse $\epsilon$.
     $$ \mathbb{P}\left( \sup_{f \in \mathcal{F}} (\mathbb{E}[f] - \mathbb{E}_n[f]) \geq \epsilon \right) = \mathbb{P}\left( \bigcup_{j=1}^k \left\lbrace \mathbb{E}[f_j] - \mathbb{E}_n[f_j] \geq \epsilon \right\rbrace \right) $$
  6. Par l'inégalité de Boole (ou borne de l'union), la probabilité d'une union est majorée par la somme des probabilités :
     $$ \mathbb{P}\left( \bigcup_{j=1}^k \left\lbrace \mathbb{E}[f_j] - \mathbb{E}_n[f_j] \geq \epsilon \right\rbrace \right) \leq \sum_{j=1}^k \mathbb{P}\left( \mathbb{E}[f_j] - \mathbb{E}_n[f_j] \geq \epsilon \right) $$
  7. En utilisant la majoration issue de Hoeffding pour chaque terme :
     $$ \mathbb{P}\left( \sup_{f \in \mathcal{F}} (\mathbb{E}[f] - \mathbb{E}_n[f]) \geq \epsilon \right) \leq \sum_{j=1}^k \exp(-2n\epsilon^2) = k \exp(-2n\epsilon^2) $$
  8. Nous voulons que cette probabilité d'échec soit inférieure à un seuil $\delta > 0$. Posons :
     $$ k \exp(-2n\epsilon^2) = \delta $$
  9. Isolons $\epsilon$ algébriquement :
     $$ \exp(-2n\epsilon^2) = \frac{\delta}{k} $$
     $$ -2n\epsilon^2 = \ln\left(\frac{\delta}{k}\right) = - \ln\left(\frac{k}{\delta}\right) = - (\ln(k) + \ln(1/\delta)) $$
     $$ \epsilon^2 = \frac{\ln(k) + \ln(1/\delta)}{2n} $$
     $$ \epsilon = \sqrt{\frac{\ln(k) + \ln(1/\delta)}{2n}} $$
  10. Ainsi, la probabilité que l'écart dépasse cette valeur spécifique de $\epsilon$ est exactement $\delta$. Donc, avec une probabilité de $1 - \delta$, le supremum est majoré par ce $\epsilon$, ce qui conclut la preuve formelle.

### Exercice 2 : Discrétisation via les Nombres de Recouvrement (Inspiré Master Recherche)

**Énoncé :**
Soit $\mathcal{F}$ une classe *infinie* de fonctions à valeurs dans $[0, 1]$. Supposons qu'il existe un espace métrique sur $\mathcal{F}$ muni d'une distance de supremum absolue $d_\infty(f, g) = \sup_{z \in \mathcal{Z}} |f(z) - g(z)|$.
Montrez rigoureusement que si l'on dispose d'un $\frac{\epsilon}{4}$-recouvrement de $\mathcal{F}$ de taille finie $N = \mathcal{N}(\mathcal{F}, d_\infty, \epsilon/4)$, alors on peut borner la probabilité d'un grand écart du supremum empirique par une borne d'union sur ce recouvrement.

**Correction Détaillée :**
* *Analyse de l'énoncé :* C'est la transition cruciale vers les classes infinies. L'idée est d'approximer la classe infinie par une classe finie (le recouvrement) et de montrer que l'erreur d'approximation est négligeable devant la concentration.
* *Résolution pas-à-pas :*
  1. Soit $\mathcal{C} = \{c_1, \dots, c_N\}$ un $\frac{\epsilon}{4}$-recouvrement de $\mathcal{F}$.
     Cela signifie que par définition, pour toute fonction $f \in \mathcal{F}$, il existe une fonction $c_f \in \mathcal{C}$ telle que $d_\infty(f, c_f) = \sup_z |f(z) - c_f(z)| \leq \frac{\epsilon}{4}$.
  2. Considérons l'écart fondamental que nous voulons borner pour une fonction $f \in \mathcal{F}$ arbitraire :
     $$ \mathbb{E}[f] - \mathbb{E}_n[f] $$
  3. Insérons la fonction approximante $c_f$ en ajoutant et soustrayant stratégiquement (astuce de l'inégalité triangulaire algébrique) :
     $$ \mathbb{E}[f] - \mathbb{E}_n[f] = \left( \mathbb{E}[f] - \mathbb{E}[c_f] \right) + \left( \mathbb{E}[c_f] - \mathbb{E}_n[c_f] \right) + \left( \mathbb{E}_n[c_f] - \mathbb{E}_n[f] \right) $$
  4. Nous pouvons majorer le premier et le troisième terme en utilisant la propriété du recouvrement infinitésimal :
     - Pour le premier terme :
       $$ \mathbb{E}[f] - \mathbb{E}[c_f] = \mathbb{E}[f - c_f] \leq \mathbb{E}[|f - c_f|] \leq \mathbb{E}\left[ \sup_z |f(z) - c_f(z)| \right] \leq \frac{\epsilon}{4} $$
     - Pour le troisième terme :
       $$ \mathbb{E}_n[c_f] - \mathbb{E}_n[f] = \frac{1}{n} \sum_{i=1}^n (c_f(Z_i) - f(Z_i)) \leq \frac{1}{n} \sum_{i=1}^n |c_f(Z_i) - f(Z_i)| \leq \frac{1}{n} \sum_{i=1}^n \left( \sup_z |c_f(z) - f(z)| \right) \leq \frac{1}{n} \sum_{i=1}^n \frac{\epsilon}{4} = \frac{\epsilon}{4} $$
  5. En injectant ces majorations dans l'égalité de l'étape 3 :
     $$ \mathbb{E}[f] - \mathbb{E}_n[f] \leq \frac{\epsilon}{4} + \left( \mathbb{E}[c_f] - \mathbb{E}_n[c_f] \right) + \frac{\epsilon}{4} = \frac{\epsilon}{2} + \left( \mathbb{E}[c_f] - \mathbb{E}_n[c_f] \right) $$
  6. Cette majoration est valable pour toute fonction $f \in \mathcal{F}$. Prenons le supremum sur $\mathcal{F}$ des deux côtés. Puisque pour chaque $f$, $c_f$ est un élément du recouvrement $\mathcal{C}$ :
     $$ \sup_{f \in \mathcal{F}} \left( \mathbb{E}[f] - \mathbb{E}_n[f] \right) \leq \frac{\epsilon}{2} + \sup_{c \in \mathcal{C}} \left( \mathbb{E}[c] - \mathbb{E}_n[c] \right) $$
  7. Évaluons maintenant la probabilité que le supremum sur la classe infinie $\mathcal{F}$ dépasse $\epsilon$ :
     $$ \mathbb{P}\left( \sup_{f \in \mathcal{F}} \left( \mathbb{E}[f] - \mathbb{E}_n[f] \right) \geq \epsilon \right) \leq \mathbb{P}\left( \frac{\epsilon}{2} + \sup_{c \in \mathcal{C}} \left( \mathbb{E}[c] - \mathbb{E}_n[c] \right) \geq \epsilon \right) $$
     $$ = \mathbb{P}\left( \sup_{c \in \mathcal{C}} \left( \mathbb{E}[c] - \mathbb{E}_n[c] \right) \geq \frac{\epsilon}{2} \right) $$
  8. La magie opère : nous avons réduit le problème d'un supremum sur un ensemble *infini* ($\mathcal{F}$) à un supremum sur un ensemble *fini* ($\mathcal{C}$) de taille $N$. Nous pouvons maintenant appliquer la borne de l'union vue dans l'Exercice 1 pour l'ensemble $\mathcal{C}$ et le seuil $\frac{\epsilon}{2}$ :
     $$ \mathbb{P}\left( \sup_{c \in \mathcal{C}} \left( \mathbb{E}[c] - \mathbb{E}_n[c] \right) \geq \frac{\epsilon}{2} \right) \leq \sum_{i=1}^N \mathbb{P}\left( \mathbb{E}[c_i] - \mathbb{E}_n[c_i] \geq \frac{\epsilon}{2} \right) \leq N \exp\left(-2n\left(\frac{\epsilon}{2}\right)^2\right) $$
     $$ = \mathcal{N}(\mathcal{F}, d_\infty, \epsilon/4) \cdot \exp\left( - \frac{n\epsilon^2}{2} \right) $$
  9. L'erreur de généralisation sur la classe infinie est ainsi rigoureusement contrôlée par la "capacité volumique" (le nombre de recouvrement) de la classe.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** En apprentissage profond (Deep Learning), les réseaux de neurones définissent des classes de fonctions $\mathcal{H}$ d'une complexité gigantesque (des milliards de paramètres). Si la capacité de cette classe est mal régulée, le supremum du processus empirique explosera, indiquant que le réseau peut avoir une erreur nulle à l'entraînement ($\mathbb{E}_n[f] = 0$) mais une erreur désastreuse en production ($\mathbb{E}[f]$ grand). Les mathématiques des processus empiriques fournissent le cadre théorique strict pour comprendre pourquoi des techniques comme la régularisation $L_2$, le Dropout, ou l'arrêt précoce (Early Stopping) fonctionnent : elles limitent artificiellement la complexité ou le "volume" effectif (les nombres de recouvrement) de la classe des fonctions explorées par l'optimiseur.
- **Exemple Concret :** Pour prouver les garanties théoriques des Support Vector Machines (SVM), on utilise la complexité des hyperplans séparateurs avec une marge maximale. La marge impose une restriction géométrique sévère sur la classe de fonctions, ce qui fait chuter de manière drastique les nombres de recouvrement empirique. On utilise alors ces inégalités de concentration pour prouver que, malgré une dimension de caractéristiques infinie (comme dans le "Kernel Trick" RKHS), l'algorithme est PAC-apprenable et garantit une erreur réelle faible en s'appuyant rigoureusement sur la théorie développée dans ce jalon.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 133 (Modele PAC)]], [[Jalon 91 (Inegalites de concentration)]], [[Jalon 89 (Lemmes de Borel-Cantelli)]]
- **Concepts Futurs dépendants :** [[Jalon 135 (Complexite de Rademacher)]], [[Jalon 136 (Theorie de Vapnik-Chervonenkis)]]
