---
title: "Exercice 10 : Preuve du lemme d'existence d'un vecteur propre à travers le polynôme minimal"
difficulty: 5
---

# Exercice 10 : Lemme d'existence d'un vecteur et polynôme minimal (★★★★★)

## Énoncé

Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension finie $n \ge 1$. Soit $u \in \mathcal{L}(E)$.
Soit $\pi_u(X)$ le polynôme minimal de $u$.
L'objectif est de démontrer qu'il existe un vecteur $x_0 \in E$ tel que le polynôme minimal local de $x_0$ par rapport à $u$ (c'est-à-dire le générateur unitaire de l'idéal $I_{x_0} = \{ P \in \mathbb{K}[X] \mid P(u)(x_0) = 0_E \}$) soit exactement égal à $\pi_u(X)$.

*On supposera ici, pour simplifier la preuve de ce théorème fondamental, que le polynôme minimal de $u$ est de la forme $\pi_u(X) = P_1(X)^{\alpha_1} P_2(X)^{\alpha_2}$ où $P_1, P_2$ sont irréductibles distincts (le cas général se déduit par récurrence sur le nombre de facteurs premiers).*

## Solution Rigoureuse

Cet exercice est un classique d'algèbre exigeant une maîtrise parfaite des polynômes et du lemme des noyaux.
Pour tout vecteur $x \in E$, on note $\pi_{x, u}$ le générateur unitaire de l'idéal $\{ P \mid P(u)(x) = 0_E \}$. Cet idéal contient $\pi_u$ car $\pi_u(u)(x) = 0_E(x) = 0_E$. Donc $\pi_{x, u}$ divise toujours $\pi_u$. L'enjeu est de trouver un vecteur où l'égalité est stricte.

### Étape 1 : Vecteur maximal pour une puissance de polynôme irréductible
Supposons d'abord que $\pi_u(X) = P_1(X)^{\alpha_1}$.
Par définition du polynôme minimal, il est le polynôme annulateur de degré minimal. Ainsi, le polynôme $P_1(X)^{\alpha_1 - 1}$ n'est PAS un polynôme annulateur de $u$.
Cela signifie formellement qu'il existe un vecteur $y \in E$ tel que :
$$P_1(u)^{\alpha_1 - 1}(y) \neq 0_E$$
Considérons ce vecteur $y$. Son polynôme annulateur local $\pi_{y, u}$ doit diviser le polynôme minimal global $P_1(X)^{\alpha_1}$. Puisque $P_1$ est irréductible, les diviseurs unitaires sont exactement les $P_1(X)^k$ pour $0 \le k \le \alpha_1$.
Or, $\pi_{y, u}$ ne peut pas diviser $P_1(X)^{\alpha_1 - 1}$, sinon on aurait $P_1(u)^{\alpha_1 - 1}(y) = 0_E$, ce qui contredit la définition de $y$.
L'unique puissance possible pour $\pi_{y, u}$ est donc $\alpha_1$.
Ainsi, il existe un vecteur $y$ tel que $\pi_{y, u} = P_1(X)^{\alpha_1}$.

### Étape 2 : Construction par somme directe (Lemme des noyaux)
Revenons au cas $\pi_u(X) = P_1(X)^{\alpha_1} P_2(X)^{\alpha_2}$.
D'après le théorème de décomposition des noyaux (Bézout), puisque $P_1^{\alpha_1}$ et $P_2^{\alpha_2}$ sont premiers entre eux, l'espace se décompose en somme directe :
$$E = \ker(P_1(u)^{\alpha_1}) \oplus \ker(P_2(u)^{\alpha_2})$$
Soit $E_1 = \ker(P_1(u)^{\alpha_1})$ et $E_2 = \ker(P_2(u)^{\alpha_2})$.
L'endomorphisme induit $u_1 = u_{|E_1}$ a pour polynôme annulateur $P_1(X)^{\alpha_1}$. En réalité, c'est son polynôme minimal, car si c'était une puissance inférieure, ce facteur abaisserait le polynôme minimal global.
Par l'Étape 1, appliquée à $u_1$ sur l'espace $E_1$, il existe $x_1 \in E_1$ tel que $\pi_{x_1, u_1} = P_1(X)^{\alpha_1}$.
De même, il existe $x_2 \in E_2$ tel que $\pi_{x_2, u_2} = P_2(X)^{\alpha_2}$.

### Étape 3 : Indépendance et produit
Considérons le vecteur défini par la somme $x_0 = x_1 + x_2$.
Déterminons son polynôme minimal local $\pi_{x_0, u}$.
Soit un polynôme $Q \in \mathbb{K}[X]$ tel que $Q(u)(x_0) = 0_E$.
$$Q(u)(x_1 + x_2) = Q(u)(x_1) + Q(u)(x_2) = 0_E$$
Comme $E_1$ et $E_2$ sont stables par $u$, ils sont stables par $Q(u)$. Donc $Q(u)(x_1) \in E_1$ et $Q(u)(x_2) \in E_2$.
L'équation s'écrit comme la nullité d'une somme de deux vecteurs appartenant à des sous-espaces en somme directe. L'unique solution est que chaque composante soit nulle :
$$Q(u)(x_1) = 0_E \quad \text{et} \quad Q(u)(x_2) = 0_E$$
La première condition implique que le polynôme minimal local de $x_1$ divise $Q$. Donc $P_1^{\alpha_1}$ divise $Q$.
La seconde condition implique que $P_2^{\alpha_2}$ divise $Q$.
Puisque $P_1^{\alpha_1}$ et $P_2^{\alpha_2}$ sont premiers entre eux, leur produit divise $Q$.
Donc $P_1^{\alpha_1} P_2^{\alpha_2}$ divise $Q$, ce qui signifie que $\pi_u$ divise $Q$.
Puisque $\pi_u$ est lui-même annulateur de tout vecteur (dont $x_0$), le générateur unitaire de l'idéal est exactement $\pi_u$.
On a rigoureusement construit un vecteur $x_0 = x_1 + x_2$ dont le polynôme minimal local est le polynôme minimal global. $\blacksquare$
