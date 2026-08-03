---
title: "Exercice 5 : Limite non triviale avec majoration fine"
difficulty: $\bigstar\bigstar\bigstar\star\star$
---

# Exercice 5 : Limite non triviale avec majoration fine

## Énoncé

Montrer que $\lim_{(x,y) \to (0,0)} f(x, y) = 0$ où la fonction $f$ est définie par :
$$ f(x, y) = x \ln(x^2 + y^2) $$

## Solution détaillée

1. **Problématique** :
   En $(0,0)$, la fonction présente une forme indéterminée du type $0 \times (-\infty)$.
   Le passage en polaires est recommandé pour traiter l'expression $x^2+y^2$.

2. **Passage en coordonnées polaires** :
   Posons $x = r \cos \theta$ et $y = r \sin \theta$.
   Pour $r > 0$, on a $x^2 + y^2 = r^2$.
   L'expression devient :
   $$ f(r \cos \theta, r \sin \theta) = (r \cos \theta) \ln(r^2) $$
   En utilisant les propriétés des logarithmes ($\ln(r^2) = 2 \ln r$ pour $r>0$) :
   $$ f(r \cos \theta, r \sin \theta) = r \cos \theta \cdot 2 \ln r = 2r \ln(r) \cos \theta $$

3. **Recherche de majoration uniforme** :
   Prenons la valeur absolue de l'expression :
   $$ |f(r \cos \theta, r \sin \theta)| = |2r \ln(r) \cos \theta| $$

   Puisque $|\cos \theta| \leq 1$ pour tout angle $\theta$, on peut majorer indépendamment de la trajectoire :
   $$ |f(r \cos \theta, r \sin \theta)| \leq |2r \ln r| $$
   $$ |f(r \cos \theta, r \sin \theta)| \leq 2 |r \ln r| $$

4. **Conclusion par la limite unidimensionnelle de référence** :
   Nous sommes ramenés à une limite classique d'analyse réelle en 1D : les croissances comparées.
   On sait que $\lim_{r \to 0^+} r \ln r = 0$.
   Par conséquent, $\lim_{r \to 0^+} 2|r \ln r| = 0$.

   Par le théorème d'encadrement, puisque :
   $$ 0 \leq |f(x, y)| \leq 2\sqrt{x^2+y^2} |\ln(\sqrt{x^2+y^2})| \xrightarrow{(x,y)\to(0,0)} 0 $$
   Nous avons bien démontré que $\lim_{(x,y) \to (0,0)} x \ln(x^2 + y^2) = 0$.
