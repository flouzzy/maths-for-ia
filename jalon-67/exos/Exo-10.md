---
uuid: "exo-67-10"
title: "Exercice 10 : Généralisation avec une borne inférieure"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 10 : Généralisation avec une borne inférieure ($\bigstar\bigstar\bigstar\bigstar\bigstar$)

## Énoncé

Soit $(f_n)$ une suite croissante de fonctions mesurables (pas nécessairement positives) telle qu'il existe une fonction intégrable $g$ vérifiant $f_1 \ge g$. Démontrer que le TCM s'applique toujours.

## Corrigé Rigoureux

1. **Translation pour retrouver la positivité :** On définit $h_n = f_n - g$.
2. **Propriétés de $h_n$ :**
   - $h_n$ est mesurable.
   - $h_n \ge f_1 - g \ge 0$, donc la suite $(h_n)$ est formée de fonctions positives.
   - $h_{n+1} - h_n = f_{n+1} - f_n \ge 0$, donc la suite $(h_n)$ est croissante.
3. **Beppo Levi sur $h_n$ :** Le théorème s'applique pour $h_n$ : $\lim_n \int h_n d\mu = \int \lim_n h_n d\mu$.
4. **Retour aux $f_n$ :**
   $\lim_n \int (f_n - g) d\mu = \int \lim_n (f_n - g) d\mu$
   Puisque $g$ est intégrable ($\int |g| d\mu < \infty$), on peut séparer les intégrales :
   $\lim_n (\int f_n d\mu - \int g d\mu) = \int (\lim_n f_n) d\mu - \int g d\mu$
   En ajoutant $\int g d\mu$ de chaque côté (ce qui est légitime car la valeur est finie), on obtient :
   $\lim_n \int f_n d\mu = \int \lim_n f_n d\mu$.
Ceci prouve que la condition $f_n \ge 0$ peut être relâchée à "$f_n$ est minorée par une fonction intégrable".
