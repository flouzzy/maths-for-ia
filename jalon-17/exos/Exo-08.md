---
title: "Exercice 8 : Convergence absolue vs Séries de Maclaurin"
difficulty: ★★★★☆
---
# Exercice 8 : Convergence absolue vs Séries de Maclaurin

## Énoncé
Déterminer la nature de la série de terme général $u_n = \ln(1 + \frac{(-1)^n}{\sqrt{n}})$.

## Correction

1. **Développement limité :**
   On utilise le DL usuel de $\ln(1+x)$ au voisinage de 0 pour obtenir un développement asymptotique du terme général :
   $u_n = \ln(1 + \frac{(-1)^n}{\sqrt{n}}) = \frac{(-1)^n}{\sqrt{n}} - \frac{1}{2}(\frac{(-1)^n}{\sqrt{n}})^2 + O(\frac{1}{n^{3/2}}) = \frac{(-1)^n}{\sqrt{n}} - \frac{1}{2n} + O(\frac{1}{n^{3/2}})$.
2. **Analyse des termes :**
   - La série $\sum \frac{(-1)^n}{\sqrt{n}}$ converge (critère des séries alternées).
   - La série $\sum -\frac{1}{2n}$ diverge (proportionnelle à la série harmonique).
   - La série $\sum O(\frac{1}{n^{3/2}})$ converge absolument (série de Riemann d'exposant $3/2 > 1$).
3. **Conclusion :**
   La série $\sum u_n$ s'écrit comme la somme d'une série convergente, d'une série divergente et d'une série convergente.
   Par linéarité, la série $\sum u_n$ diverge vers $-\infty$.
   *(Remarque : cet exercice met en garde contre l'utilisation hâtive du critère des équivalents pour les séries dont les termes ne gardent pas un signe constant, car $u_n \sim \frac{(-1)^n}{\sqrt{n}}$ qui est le terme général d'une série convergente).*.
