---
title: "Exercice 9 : Lemme de Grönwall"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 9 : Lemme de Grönwall

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soient $f, g$ deux fonctions continues de $\mathbb{R}_+$ dans $\mathbb{R}_+$. On suppose qu'il existe une constante $C \ge 0$ telle que pour tout $t \ge 0$ :
$$f(t) \le C + \int_0^t f(s) g(s) ds$$
Montrer que pour tout $t \ge 0$, $f(t) \le C \exp\left( \int_0^t g(s) ds \right)$.
*(Indication : introduire la fonction $H(t) = C + \int_0^t f(s) g(s) ds$ et dériver).*

**Correction détaillée :**
1. **Définition de la fonction auxiliaire :**
   Soit $H(t) = C + \int_0^t f(s) g(s) ds$. Par le Théorème Fondamental de l'Analyse, $H$ est dérivable et $H'(t) = f(t)g(t)$.
2. **Utilisation de l'hypothèse :**
   L'hypothèse se réécrit : pour tout $t \ge 0$, $f(t) \le H(t)$.
   Comme $g(t) \ge 0$, on peut multiplier cette inégalité par $g(t)$ sans en changer le sens :
   $f(t)g(t) \le H(t)g(t)$, soit $H'(t) \le H(t)g(t)$.
3. **Mise sous forme d'équation différentielle :**
   $H'(t) - g(t)H(t) \le 0$.
   On multiplie par le "facteur intégrant" $e^{-G(t)}$ où $G(t) = \int_0^t g(s) ds$. Comme l'exponentielle est strictement positive, l'inégalité est préservée :
   $H'(t) e^{-G(t)} - g(t) e^{-G(t)} H(t) \le 0$.
4. **Dérivée d'un produit :**
   Le membre de gauche est exactement la dérivée de $t \mapsto H(t)e^{-G(t)}$.
   Donc $\frac{d}{dt} \left( H(t)e^{-G(t)} \right) \le 0$.
5. **Intégration :**
   La fonction $H(t)e^{-G(t)}$ est décroissante sur $\mathbb{R}_+$. Par conséquent, pour tout $t \ge 0$ :
   $H(t)e^{-G(t)} \le H(0)e^{-G(0)}$.
   Or $H(0) = C + \int_0^0 f(s)g(s)ds = C$, et $G(0) = 0 \implies e^{-G(0)} = 1$.
   On a donc $H(t)e^{-G(t)} \le C$, d'où $H(t) \le C e^{G(t)}$.
6. **Conclusion :**
   Comme $f(t) \le H(t)$, on en conclut par transitivité que :
   $f(t) \le C \exp\left( \int_0^t g(s) ds \right)$.
   *Ce lemme est un outil central pour prouver l'unicité dans le théorème de Cauchy-Lipschitz.*
