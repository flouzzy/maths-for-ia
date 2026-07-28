---
uuid: "jalon-38-exo-08"
title: "Exercice 8 : Dérivation sous le signe intégral (avant-goût)"
tags:
  - math/analyse
  - ia/calcul-differentiel
---

# Exercice 8

**Difficulté :** ★★★★☆

**Énoncé :**
Soit $F(x) = \int_0^{x^2} e^{t^2} \, dt$. Calculer $F'(x)$ pour tout $x \in \mathbb{R}$.

**Correction détaillée :**
1. Posons $f(t) = e^{t^2}$. La fonction $f$ est continue sur $\mathbb{R}$.
2. Par le premier théorème fondamental de l'analyse, la fonction $\Phi(u) = \int_0^u e^{t^2} \, dt$ est la primitive de $f$ qui s'annule en $0$.
3. En particulier, la fonction $\Phi$ est dérivable sur $\mathbb{R}$ et $\forall u \in \mathbb{R}, \Phi'(u) = f(u) = e^{u^2}$.
4. Or, par définition de notre fonction $F$, on remarque que pour tout $x \in \mathbb{R}$ :
$$ F(x) = \int_0^{x^2} e^{t^2} \, dt = \Phi(x^2) $$
5. La fonction $F$ est donc la composition de deux fonctions dérivables : la fonction $x \mapsto x^2$ (notons-la $g(x) = x^2$) et la fonction $\Phi$. Donc $F = \Phi \circ g$.
6. Par le théorème de dérivation des fonctions composées, $( \Phi \circ g )'(x) = g'(x) \cdot \Phi'(g(x))$.
7. On calcule la dérivée de $g$ : $g'(x) = 2x$.
8. On remplace par l'expression de $\Phi'$ établie à l'étape 3 : $\Phi'(g(x)) = \Phi'(x^2) = e^{(x^2)^2} = e^{x^4}$.
9. En effectuant le produit, on obtient le résultat final :
$$ F'(x) = 2x e^{x^4} $$
$\blacksquare$
