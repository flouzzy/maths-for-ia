---
title: "Exercice 02 : Intégrale par rapport à la mesure de comptage"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 02 : Intégrale par rapport à la mesure de comptage

**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

Soit $\mathbb{N}$ muni de la tribu discrète $\mathcal{P}(\mathbb{N})$ et de la mesure de comptage $\mu(A) = \text{Card}(A)$. Soit $f : \mathbb{N} \to \mathbb{R}_+$ définie par $f(n) = \frac{1}{2^n}$. Calculer l'intégrale de $f$ par rapport à $\mu$ par approximation de fonctions simples.

---

## Correction détaillée

1. **Suite de fonctions simples :**
On considère les fonctions $s_N(n) = \sum_{k=0}^N \frac{1}{2^k} \mathbf{1}_{\{k\}}(n)$.
Chaque $s_N$ est une fonction simple, car elle ne prend qu'un nombre fini de valeurs non nulles (pour $n \le N$). De plus, la suite $(s_N)$ est positive, croissante et converge ponctuellement vers $f$.

2. **Intégrale des fonctions simples :**
Pour un $N$ fixé, l'intégrale est :
$$ \int_{\mathbb{N}} s_N \, d\mu = \sum_{k=0}^N \frac{1}{2^k} \mu(\{k\}) $$
La mesure de comptage d'un singleton est 1, donc $\mu(\{k\}) = 1$. D'où :
$$ \int_{\mathbb{N}} s_N \, d\mu = \sum_{k=0}^N \frac{1}{2^k} $$

3. **Passage au supremum (limite) :**
Ceci est une somme géométrique de raison $1/2$.
Par définition de l'intégrale de Lebesgue pour $f$ (comme borne supérieure des intégrales des fonctions simples majorées par $f$) :
$$ \int_{\mathbb{N}} f \, d\mu = \lim_{N \to \infty} \sum_{k=0}^N \frac{1}{2^k} = \frac{1}{1 - 1/2} = 2 $$
