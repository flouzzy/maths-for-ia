---
uuid: "exo-7-3"
title: "Exo 3 - Jalon 7"
---

Mes chers étudiants,

Nous poursuivons notre exploration des fondements de l'algèbre linéaire avec cet exercice qui vous invite à manipuler les concepts d'espaces vectoriels abstraits, de familles libres, génératrices et de bases. La clarté et la rigueur de votre raisonnement seront primordiales.

---

### Énoncé de l'Exercice 3

Soit $\mathcal{M}_2(\mathbb{R})$ l'ensemble des matrices carrées d'ordre 2 à coefficients réels. Nous savons que $\mathcal{M}_2(\mathbb{R})$ est un $\mathbb{R}$-espace vectoriel muni de l'addition matricielle et de la multiplication par un scalaire réel.

Considérons l'ensemble $E$ défini comme suit :
$$E = \left\{ M \in \mathcal{M}_2(\mathbb{R}) \mid \text{Tr}(M) = 0 \right\}$$
où $\text{Tr}(M)$ désigne la trace de la matrice $M$.

**Question 1 :** Démontrer que $E$ est un sous-espace vectoriel de $\mathcal{M}_2(\mathbb{R})$.

**Question 2 :** Soit $S$ la famille de matrices suivante :
$$S = \left\{ M_1, M_2, M_3 \right\} = \left\{ \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \right\}$$
**a)** La famille $S$ est-elle une famille génératrice de $E$ ? Justifier votre réponse de manière exhaustive.
**b)** La famille $S$ est-elle une famille libre dans $E$ ? Justifier votre réponse de manière exhaustive.
**c)** La famille $S$ est-elle une base de $E$ ? Si oui, quelle est la dimension de $E$ ?

---

### Correction Détaillée de l'Exercice 3

Nous allons aborder chaque question avec la plus grande précision, en explicitant chaque étape du raisonnement et de chaque calcul.

**Nature des objets :**
*   $\mathbb{R}$ est le corps des nombres réels.
*   $\mathcal{M}_2(\mathbb{R})$ est l'ensemble des matrices carrées d'ordre 2 à coefficients dans $\mathbb{R}$.
*   $E$ est un sous-ensemble de $\mathcal{M}_2(\mathbb{R})$.
*   $M_1, M_2, M_3$ sont des matrices spécifiques appartenant à $\mathcal{M}_2(\mathbb{R})$.
*   $S$ est une famille de matrices.

---

**Question 1 : Démontrer que $E$ est un sous-espace vectoriel de $\mathcal{M}_2(\mathbb{R})$.**

Pour démontrer que $E$ est un sous-espace vectoriel de $\mathcal{M}_2(\mathbb{R})$, nous devons vérifier trois conditions fondamentales :
1.  $E$ est non vide, c'est-à-dire qu'il contient le vecteur nul de $\mathcal{M}_2(\mathbb{R})$.
2.  $E$ est stable par l'addition vectorielle.
3.  $E$ est stable par la multiplication par un scalaire.

**Étape 1 : Vérifier que $E$ est non vide.**
Le vecteur nul de $\mathcal{M}_2(\mathbb{R})$ est la matrice nulle, notée $0_{\mathcal{M}_2(\mathbb{R})}$, qui est donnée par :
$$0_{\mathcal{M}_2(\mathbb{R})} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$$
Calculons la trace de cette matrice :
$$\text{Tr}(0_{\mathcal{M}_2(\mathbb{R})}) = 0 + 0 = 0$$
Puisque la trace de la matrice nulle est 0, la matrice nulle appartient à l'ensemble $E$.
Donc, $E$ est non vide.

**Étape 2 : Vérifier que $E$ est stable par l'addition vectorielle.**
Soient $A$ et $B$ deux matrices quelconques appartenant à $E$.
Par définition de $E$, cela signifie que $\text{Tr}(A) = 0$ et $\text{Tr}(B) = 0$.
Nous devons montrer que leur somme $A+B$ appartient également à $E$, c'est-à-dire que $\text{Tr}(A+B) = 0$.
Nous utilisons la propriété de linéarité de la trace, qui stipule que pour toutes matrices $A, B \in \mathcal{M}_2(\mathbb{R})$, $\text{Tr}(A+B) = \text{Tr}(A) + \text{Tr}(B)$.
En appliquant cette propriété :
$$\text{Tr}(A+B) = \text{Tr}(A) + \text{Tr}(B)$$
Puisque $A \in E$ et $B \in E$, nous avons $\text{Tr}(A) = 0$ et $\text{Tr}(B) = 0$.
Donc :
$$\text{Tr}(A+B) = 0 + 0 = 0$$
La trace de la matrice $A+B$ est 0, ce qui signifie que $A+B \in E$.
Donc, $E$ est stable par l'addition vectorielle.

**Étape 3 : Vérifier que $E$ est stable par la multiplication par un scalaire.**
Soit $A$ une matrice quelconque appartenant à $E$, et soit $\lambda$ un scalaire réel quelconque (c'est-à-dire $\lambda \in \mathbb{R}$).
Par définition de $E$, nous avons $\text{Tr}(A) = 0$.
Nous devons montrer que le produit scalaire $\lambda A$ appartient également à $E$, c'est-à-dire que $\text{Tr}(\lambda A) = 0$.
Nous utilisons la propriété de linéarité de la trace, qui stipule que pour toute matrice $A \in \mathcal{M}_2(\mathbb{R})$ et tout scalaire $\lambda \in \mathbb{R}$, $\text{Tr}(\lambda A) = \lambda \text{Tr}(A)$.
En appliquant cette propriété :
$$\text{Tr}(\lambda A) = \lambda \text{Tr}(A)$$
Puisque $A \in E$, nous avons $\text{Tr}(A) = 0$.
Donc :
$$\text{Tr}(\lambda A) = \lambda \cdot 0 = 0$$
La trace de la matrice $\lambda A$ est 0, ce qui signifie que $\lambda A \in E$.
Donc, $E$ est stable par la multiplication par un scalaire.

**Conclusion de la Question 1 :**
Puisque les trois conditions sont satisfaites, nous pouvons conclure que $E$ est un sous-espace vectoriel de $\mathcal{M}_2(\mathbb{R})$.

---

**Question 2 : Analyse de la famille $S = \left\{ M_1, M_2, M_3 \right\}$.**

Nous avons $M_1 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, $M_2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $M_3 = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$.
Vérifions d'abord que ces matrices appartiennent bien à $E$ :
*   $\text{Tr}(M_1) = 1 + (-1) = 0$. Donc $M_1 \in E$.
*   $\text{Tr}(M_2) = 0 + 0 = 0$. Donc $M_2 \in E$.
*   $\text{Tr}(M_3) = 0 + 0 = 0$. Donc $M_3 \in E$.
La famille $S$ est donc bien une famille de vecteurs de $E$.

**Question 2a) : La famille $S$ est-elle une famille génératrice de $E$ ?**

Une famille $S = \{M_1, M_2, M_3\}$ est génératrice de $E$ si tout vecteur $M$ de $E$ peut s'écrire comme une combinaison linéaire des vecteurs de $S$.
Soit $M$ une matrice quelconque appartenant à $E$. Par définition de $E$, $M$ est une matrice de $\mathcal{M}_2(\mathbb{R})$ dont la trace est nulle.
Une matrice $M \in \mathcal{M}_2(\mathbb{R})$ s'écrit sous la forme :
$$M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$
La condition $\text{Tr}(M) = 0$ implique $a+d=0$, ce qui signifie $d = -a$.
Ainsi, toute matrice $M \in E$ peut s'écécrire sous la forme :
$$M = \begin{pmatrix} a & b \\ c & -a \end{pmatrix}$$
où $a, b, c$ sont des nombres réels.

Nous cherchons à savoir s'il existe des scalaires réels $\alpha, \beta, \gamma \in \mathbb{R}$ tels que $M = \alpha M_1 + \beta M_2 + \gamma M_3$.
Substituons les expressions des matrices :
$$\begin{pmatrix} a & b \\ c & -a \end{pmatrix} = \alpha \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} + \beta \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} + \gamma \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$$
Effectuons la multiplication par les scalaires :
$$\begin{pmatrix} a & b \\ c & -a \end{pmatrix} = \begin{pmatrix} \alpha & 0 \\ 0 & -\alpha \end{pmatrix} + \begin{pmatrix} 0 & \beta \\ 0 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ \gamma & 0 \end{pmatrix}$$
Effectuons l'addition des matrices :
$$\begin{pmatrix} a & b \\ c & -a \end{pmatrix} = \begin{pmatrix} \alpha+0+0 & 0+\beta+0 \\ 0+0+\gamma & -\alpha+0+0 \end{pmatrix}$$
$$\begin{pmatrix} a & b \\ c & -a \end{pmatrix} = \begin{pmatrix} \alpha & \beta \\ \gamma & -\alpha \end{pmatrix}$$
Par identification des coefficients matriciels, nous obtenons le système d'équations suivant :
1.  $a = \alpha$
2.  $b = \beta$
3.  $c = \gamma$
4.  $-a = -\alpha$

La quatrième équation, $-a = -\alpha$, est redondante car elle est équivalente à $a = \alpha$, qui est déjà donnée par la première équation.
Ce système nous donne directement les valeurs des scalaires $\alpha, \beta, \gamma$ en fonction des coefficients $a, b, c$ de la matrice $M$.
Pour toute matrice $M = \begin{pmatrix} a & b \\ c & -a \end{pmatrix}$ dans $E$, nous pouvons trouver les scalaires $\alpha=a$, $\beta=b$, $\gamma=c$ tels que $M = a M_1 + b M_2 + c M_3$.
Puisque nous avons pu exprimer une matrice $M$ quelconque de $E$ comme une combinaison linéaire des matrices de $S$, la famille $S$ est une famille génératrice de $E$.

**Conclusion de la Question 2a) :**
Oui, la famille $S$ est une famille génératrice de $E$.

---

**Question 2b) : La famille $S$ est-elle une famille libre dans $E$ ?**

Une famille $S = \{M_1, M_2, M_3\}$ est libre si la seule combinaison linéaire de ses vecteurs qui est égale au vecteur nul est celle où tous les scalaires sont nuls.
Considérons une combinaison linéaire des matrices de $S$ égale à la matrice nulle $0_{\mathcal{M}_2(\mathbb{R})}$ :
$$\alpha M_1 + \beta M_2 + \gamma M_3 = 0_{\mathcal{M}_2(\mathbb{R})}$$
où $\alpha, \beta, \gamma$ sont des scalaires réels.
Substituons les expressions des matrices :
$$\alpha \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} + \beta \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} + \gamma \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$$
Effectuons la multiplication par les scalaires et l'addition des matrices, comme précédemment :
$$\begin{pmatrix} \alpha & \beta \\ \gamma & -\alpha \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$$
Par identification des coefficients matriciels, nous obtenons le système d'équations suivant :
1.  $\alpha = 0$
2.  $\beta = 0$
3.  $\gamma = 0$
4.  $-\alpha = 0$

Ce système d'équations a une unique solution : $\alpha = 0$, $\beta = 0$, $\gamma = 0$.
Puisque la seule combinaison linéaire des matrices de $S$ qui donne la matrice nulle est celle où tous les scalaires sont nuls, la famille $S$ est une famille libre dans $E$.

**Conclusion de la Question 2b) :**
Oui, la famille $S$ est une famille libre dans $E$.

---

**Question 2c) : La famille $S$ est-elle une base de $E$ ? Si oui, quelle est la dimension de $E$ ?**

Une famille de vecteurs est une base d'un espace vectoriel si et seulement si elle est à la fois une famille génératrice de cet espace et une famille libre dans cet espace.
D'après la Question 2a), nous avons démontré que la famille $S$ est une famille génératrice de $E$.
D'après la Question 2b), nous avons démontré que la famille $S$ est une famille libre dans $E$.
Puisque la famille $S$ satisfait ces deux conditions, elle est une base de $E$.

La dimension d'un espace vectoriel est le nombre de vecteurs dans n'importe quelle base de cet espace.
La famille $S$ contient 3 vecteurs ($M_1, M_2, M_3$).
Par conséquent, la dimension de l'espace vectoriel $E$ est 3.

**Conclusion de la Question 2c) :**
Oui, la famille $S$ est une base de $E$. La dimension de $E$ est 3.

---

J'espère que cette correction détaillée vous aura permis de saisir toutes les nuances de cet exercice. La rigueur est la clé de la maîtrise de l'algèbre linéaire.
