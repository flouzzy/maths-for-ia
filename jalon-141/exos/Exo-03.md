Mes chers étudiants,

Nous abordons aujourd'hui un exercice fondamental qui nous permettra de consolider notre compréhension des classes de Vapnik-Chervonenkis (VC), un concept pivot dans la théorie de l'apprentissage statistique et l'analyse des processus empiriques. Ces classes sont au cœur des théorèmes de Glivenko-Cantelli généralisés, garantissant la convergence uniforme des processus empiriques pour des familles de fonctions suffisamment "simples".

L'exercice que je vous propose est conçu pour être une première incursion dans la manipulation de ces définitions. Sa difficulté est modérée, mais il exige une rigueur absolue dans l'application des définitions.

---

# Exercice 3/10 - Jalon 141 : Classes de Vapnik-Chervonenkis (VC) et Shattering

**Thème :** Théorèmes de Glivenko-Cantelli généralisés pour les classes de fonctions VC.
**Difficulté :** 3/10

---

## Énoncé Rigoureux et Formel

Soit $\mathcal{X}$ un ensemble fini de points, défini comme $\mathcal{X} = \{x_1, x_2, x_3\}$.
Considérons une classe $\mathcal{F}$ de fonctions indicatrices $f: \mathcal{X} \to \{0, 1\}$, où chaque fonction $f$ est de la forme $\mathbb{I}_{S}$ pour un certain sous-ensemble $S \subseteq \mathcal{X}$.
La classe $\mathcal{F}$ est donnée par :
$$ \mathcal{F} = \{ \mathbb{I}_{\{x_1\}}, \mathbb{I}_{\{x_2\}}, \mathbb{I}_{\{x_3\}}, \mathbb{I}_{\{x_1, x_2\}} \} $$
où $\mathbb{I}_{S}(x) = 1$ si $x \in S$ et $\mathbb{I}_{S}(x) = 0$ si $x \notin S$.

Nous allons explorer la notion de "shattering" et la dimension VC pour cette classe spécifique.

---

### Partie A : Définition du Shattering

Soit $A \subseteq \mathcal{X}$ un sous-ensemble fini.
Donnez la définition formelle d'un sous-ensemble $A$ qui est "shattered" (brisé) par la classe $\mathcal{F}$.

---

### Partie B : Vérification du Shattering

Considérons le sous-ensemble $A_0 = \{x_1, x_2\} \subseteq \mathcal{X}$.
Le sous-ensemble $A_0$ est-il shattered par la classe $\mathcal{F}$ ? Justifiez votre réponse en listant explicitement toutes les dichotomies possibles sur $A_0$ et en vérifiant si elles peuvent être réalisées par des fonctions de $\mathcal{F}$.

---

### Partie C : Détermination de la Dimension VC

Quelle est la dimension VC (VC-dimension) de la classe $\mathcal{F}$ ? Justifiez votre réponse en vous basant sur la définition de la dimension VC et les résultats de la Partie B (et, si nécessaire, en considérant d'autres sous-ensembles de $\mathcal{X}$).

---

## Analyse Détaillée

Chers étudiants, cet exercice est une occasion de manipuler les définitions fondamentales de la théorie VC. Il ne s'agit pas de prouver un théorème complexe, mais d'appliquer avec rigueur les concepts de "shattering" et de dimension VC à un cas concret et de petite taille.

### Partie A : Définition du Shattering

La notion de "shattering" est centrale. Un ensemble est brisé par une classe de fonctions si cette classe est suffisamment riche pour "séparer" ses points de toutes les manières possibles. Formellement, cela signifie que pour tout sous-ensemble de l'ensemble brisé, il existe une fonction dans la classe qui assigne 1 à tous les points de ce sous-ensemble et 0 à tous les autres points de l'ensemble brisé. C'est une condition forte de expressivité de la classe de fonctions.

### Partie B : Vérification du Shattering

Pour vérifier si un sous-ensemble $A_0$ est shattered, nous devons suivre une procédure systématique :
1.  **Identifier $A_0$ :** Nous avons $A_0 = \{x_1, x_2\}$.
2.  **Lister toutes les dichotomies :** Une dichotomie sur $A_0$ est une partition de $A_0$ en deux sous-ensembles, l'un où la fonction prend la valeur 1, l'autre où elle prend la valeur 0. Pour un ensemble de taille $|A_0|$, il y a $2^{|A_0|}$ dichotomies possibles. Ici, $|A_0|=2$, donc il y aura $2^2 = 4$ dichotomies.
3.  **Vérifier la réalisabilité :** Pour chaque dichotomie, nous devons parcourir la classe $\mathcal{F}$ et déterminer s'il existe au moins une fonction $f \in \mathcal{F}$ telle que l'action de $f$ sur $A_0$ corresponde exactement à cette dichotomie.
    *   Si *toutes* les $2^{|A_0|}$ dichotomies peuvent être réalisées par au moins une fonction de $\mathcal{F}$, alors $A_0$ est shattered.
    *   Si au moins une dichotomie *ne peut pas* être réalisée par une fonction de $\mathcal{F}$, alors $A_0$ n'est pas shattered.

### Partie C : Détermination de la Dimension VC

La dimension VC d'une classe de fonctions $\mathcal{F}$, notée $\text{VCdim}(\mathcal{F})$, est définie comme la taille maximale d'un sous-ensemble fini de $\mathcal{X}$ qui peut être shattered par $\mathcal{F}$.
1.  **Utiliser les résultats de la Partie B :** Si $A_0$ n'est pas shattered, cela nous donne une borne supérieure pour la dimension VC.
2.  **Examiner d'autres sous-ensembles :** Nous devrons considérer des sous-ensembles de taille inférieure à $|A_0|$ (dans ce cas, des sous-ensembles de taille 1) pour voir s'ils sont shattered.
3.  **Conclure :** La dimension VC sera la plus grande taille $k$ pour laquelle il existe au moins un sous-ensemble de $\mathcal{X}$ de taille $k$ qui est shattered par $\mathcal{F}$. Si aucun ensemble de taille $k$ n'est shattered, mais qu'au moins un ensemble de taille $k-1$ l'est, alors la dimension VC est $k-1$.

Soyez méticuleux dans vos vérifications. Chaque étape doit être explicitée sans aucune ellipse mathématique.

---

## Correction Pas-à-Pas

### Partie A : Définition du Shattering

Soit $\mathcal{X}$ un ensemble fondamental et $\mathcal{F}$ une classe de fonctions $f: \mathcal{X} \to \{0, 1\}$.
Soit $A \subseteq \mathcal{X}$ un sous-ensemble fini de points, avec $|A| = k$.
L'ensemble $A$ est dit **shattered** (brisé) par la classe $\mathcal{F}$ si, pour toute partition possible de $A$ en deux sous-ensembles disjoints $A_1$ et $A_0$ (tels que $A_1 \cup A_0 = A$ et $A_1 \cap A_0 = \emptyset$), il existe au moins une fonction $f \in \mathcal{F}$ telle que :
$$ \forall x \in A_1, f(x) = 1 \quad \text{et} \quad \forall x \in A_0, f(x) = 0 $$
De manière équivalente, $A$ est shattered par $\mathcal{F}$ si la projection de $\mathcal{F}$ sur $A$, notée $\mathcal{F}|_A = \{ (f(x))_{x \in A} \mid f \in \mathcal{F} \}$, contient toutes les $2^{|A|}$ fonctions possibles de $A$ vers $\{0, 1\}$. Autrement dit, $\mathcal{F}|_A = \{0, 1\}^A$.

### Partie B : Vérification du Shattering

Considérons le sous-ensemble $A_0 = \{x_1, x_2\} \subseteq \mathcal{X}$.
La taille de $A_0$ est $|A_0| = 2$. Par conséquent, il y a $2^{|A_0|} = 2^2 = 4$ dichotomies possibles sur $A_0$.
Nous allons lister ces dichotomies et vérifier si chacune d'elles peut être réalisée par une fonction $f \in \mathcal{F}$.

Les 4 dichotomies possibles sur $A_0 = \{x_1, x_2\}$ sont :

1.  **Dichotomie 1 :** $f(x_1) = 0, f(x_2) = 0$.
    *   Nous cherchons une fonction $f \in \mathcal{F}$ telle que $f(x_1)=0$ et $f(x_2)=0$.
    *   Vérifions les fonctions dans $\mathcal{F}$:
        *   $\mathbb{I}_{\{x_1\}}$ : $\mathbb{I}_{\{x_1\}}(x_1)=1$, $\mathbb{I}_{\{x_1\}}(x_2)=0$. Ne correspond pas.
        *   $\mathbb{I}_{\{x_2\}}$ : $\mathbb{I}_{\{x_2\}}(x_1)=0$, $\mathbb{I}_{\{x_2\}}(x_2)=1$. Ne correspond pas.
        *   $\mathbb{I}_{\{x_3\}}$ : $\mathbb{I}_{\{x_3\}}(x_1)=0$, $\mathbb{I}_{\{x_3\}}(x_2)=0$. **Ceci correspond !**
        *   $\mathbb{I}_{\{x_1, x_2\}}$ : $\mathbb{I}_{\{x_1, x_2\}}(x_1)=1$, $\mathbb{I}_{\{x_1, x_2\}}(x_2)=1$. Ne correspond pas.
    *   Conclusion pour Dichotomie 1 : Oui, elle est réalisée par $\mathbb{I}_{\{x_3\}}$.

2.  **Dichotomie 2 :** $f(x_1) = 1, f(x_2) = 0$.
    *   Nous cherchons une fonction $f \in \mathcal{F}$ telle que $f(x_1)=1$ et $f(x_2)=0$.
    *   Vérifions les fonctions dans $\mathcal{F}$:
        *   $\mathbb{I}_{\{x_1\}}$ : $\mathbb{I}_{\{x_1\}}(x_1)=1$, $\mathbb{I}_{\{x_1\}}(x_2)=0$. **Ceci correspond !**
        *   $\mathbb{I}_{\{x_2\}}$ : $\mathbb{I}_{\{x_2\}}(x_1)=0$, $\mathbb{I}_{\{x_2\}}(x_2)=1$. Ne correspond pas.
        *   $\mathbb{I}_{\{x_3\}}$ : $\mathbb{I}_{\{x_3\}}(x_1)=0$, $\mathbb{I}_{\{x_3\}}(x_2)=0$. Ne correspond pas.
        *   $\mathbb{I}_{\{x_1, x_2\}}$ : $\mathbb{I}_{\{x_1, x_2\}}(x_1)=1$, $\mathbb{I}_{\{x_1, x_2\}}(x_2)=1$. Ne correspond pas.
    *   Conclusion pour Dichotomie 2 : Oui, elle est réalisée par $\mathbb{I}_{\{x_1\}}$.

3.  **Dichotomie 3 :** $f(x_1) = 0, f(x_2) = 1$.
    *   Nous cherchons une fonction $f \in \mathcal{F}$ telle que $f(x_1)=0$ et $f(x_2)=1$.
    *   Vérifions les fonctions dans $\mathcal{F}$:
        *   $\mathbb{I}_{\{x_1\}}$ : $\mathbb{I}_{\{x_1\}}(x_1)=1$, $\mathbb{I}_{\{x_1\}}(x_2)=0$. Ne correspond pas.
        *   $\mathbb{I}_{\{x_2\}}$ : $\mathbb{I}_{\{x_2\}}(x_1)=0$, $\mathbb{I}_{\{x_2\}}(x_2)=1$. **Ceci correspond !**
        *   $\mathbb{I}_{\{x_3\}}$ : $\mathbb{I}_{\{x_3\}}(x_1)=0$, $\mathbb{I}_{\{x_3\}}(x_2)=0$. Ne correspond pas.
        *   $\mathbb{I}_{\{x_1, x_2\}}$ : $\mathbb{I}_{\{x_1, x_2\}}(x_1)=1$, $\mathbb{I}_{\{x_1, x_2\}}(x_2)=1$. Ne correspond pas.
    *   Conclusion pour Dichotomie 3 : Oui, elle est réalisée par $\mathbb{I}_{\{x_2\}}$.

4.  **Dichotomie 4 :** $f(x_1) = 1, f(x_2) = 1$.
    *   Nous cherchons une fonction $f \in \mathcal{F}$ telle que $f(x_1)=1$ et $f(x_2)=1$.
    *   Vérifions les fonctions dans $\mathcal{F}$:
        *   $\mathbb{I}_{\{x_1\}}$ : $\mathbb{I}_{\{x_1\}}(x_1)=1$, $\mathbb{I}_{\{x_1\}}(x_2)=0$. Ne correspond pas.
        *   $\mathbb{I}_{\{x_2\}}$ : $\mathbb{I}_{\{x_2\}}(x_1)=0$, $\mathbb{I}_{\{x_2\}}(x_2)=1$. Ne correspond pas.
        *   $\mathbb{I}_{\{x_3\}}$ : $\mathbb{I}_{\{x_3\}}(x_1)=0$, $\mathbb{I}_{\{x_3\}}(x_2)=0$. Ne correspond pas.
        *   $\mathbb{I}_{\{x_1, x_2\}}$ : $\mathbb{I}_{\{x_1, x_2\}}(x_1)=1$, $\mathbb{I}_{\{x_1, x_2\}}(x_2)=1$. **Ceci correspond !**
    *   Conclusion pour Dichotomie 4 : Oui, elle est réalisée par $\mathbb{I}_{\{x_1, x_2\}}$.

Puisque toutes les 4 dichotomies possibles sur $A_0 = \{x_1, x_2\}$ peuvent être réalisées par au moins une fonction de la classe $\mathcal{F}$, nous pouvons conclure que :

**Le sous-ensemble $A_0 = \{x_1, x_2\}$ est shattered par la classe $\mathcal{F}$.**

### Partie C : Détermination de la Dimension VC

La dimension VC de la classe $\mathcal{F}$, notée $\text{VCdim}(\mathcal{F})$, est la taille maximale $k$ d'un sous-ensemble $A \subseteq \mathcal{X}$ tel qu'il existe au moins un $A$ de taille $k$ qui est shattered par $\mathcal{F}$.

1.  **Sous-ensembles de taille $k=2$ :**
    *   D'après la Partie B, nous avons montré que le sous-ensemble $A_0 = \{x_1, x_2\}$ de taille 2 est shattered par $\mathcal{F}$.
    *   Considérons d'autres sous-ensembles de taille 2 :
        *   $A_1 = \{x_1, x_3\}$ :
            *   Dichotomie $(f(x_1)=0, f(x_3)=1)$ : Réalisée par $\mathbb{I}_{\{x_3\}}$.
            *   Dichotomie $(f(x_1)=1, f(x_3)=0)$ : Réalisée par $\mathbb{I}_{\{x_1\}}$.
            *   Dichotomie $(f(x_1)=0, f(x_3)=0)$ : Réalisée par $\mathbb{I}_{\{x_2\}}$.
            *   Dichotomie $(f(x_1)=1, f(x_3)=1)$ : Aucune fonction dans $\mathcal{F}$ ne réalise cela. $\mathbb{I}_{\{x_1, x_2\}}$ donne $(1,0)$, $\mathbb{I}_{\{x_1\}}$ donne $(1,0)$, etc. Il n'y a pas de fonction $f \in \mathcal{F}$ telle que $f(x_1)=1$ et $f(x_3)=1$.
            *   Donc, $A_1 = \{x_1, x_3\}$ n'est pas shattered.
        *   $A_2 = \{x_2, x_3\}$ :
            *   Dichotomie $(f(x_2)=1, f(x_3)=1)$ : Aucune fonction dans $\mathcal{F}$ ne réalise cela.
            *   Donc, $A_2 = \{x_2, x_3\}$ n'est pas shattered.

    *   Puisque $A_0 = \{x_1, x_2\}$ est shattered, nous savons que $\text{VCdim}(\mathcal{F}) \ge 2$.

2.  **Sous-ensembles de taille $k=3$ :**
    *   Le seul sous-ensemble de taille 3 est $\mathcal{X} = \{x_1, x_2, x_3\}$.
    *   Il y a $2^3 = 8$ dichotomies possibles sur $\mathcal{X}$.
    *   Considérons la dichotomie $(f(x_1)=1, f(x_2)=1, f(x_3)=1)$.
        *   Nous cherchons une fonction $f \in \mathcal{F}$ telle que $f(x_1)=1, f(x_2)=1, f(x_3)=1$.
        *   $\mathbb{I}_{\{x_1\}}$ : $(1,0,0)$
        *   $\mathbb{I}_{\{x_2\}}$ : $(0,1,0)$
        *   $\mathbb{I}_{\{x_3\}}$ : $(0,0,1)$
        *   $\mathbb{I}_{\{x_1, x_2\}}$ : $(1,1,0)$
        *   Aucune fonction dans $\mathcal{F}$ ne réalise la dichotomie $(1,1,1)$.
    *   Par conséquent, $\mathcal{X}$ n'est pas shattered par $\mathcal{F}$.
    *   Cela implique que la dimension VC ne peut pas être 3 (ni plus).

3.  **Conclusion :**
    Nous avons trouvé un sous-ensemble de taille 2 ($A_0 = \{x_1, x_2\}$) qui est shattered par $\mathcal{F}$.
    Nous avons montré qu'aucun sous-ensemble de taille 3 (en l'occurrence, $\mathcal{X}$ lui-même) n'est shattered par $\mathcal{F}$.
    Par définition, la dimension VC est la taille maximale d'un ensemble shattered.

Donc, la dimension VC de la classe $\mathcal{F}$ est $\text{VCdim}(\mathcal{F}) = 2$.

---

J'espère que cette exploration détaillée vous a permis de saisir la mécanique de ces définitions. La rigueur dans l'application est la clé de la compréhension en mathématiques.
