---
title: "Exercice 8 : Limite d'une espérance paramétrée (IA)"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 8 : Limite d'une espérance paramétrée (IA)

## Énoncé

En apprentissage statistique, on évalue le risque empirique perturbé : $\mathcal{R}_\epsilon = \int_X L(x) e^{-\epsilon |x|} dx$, où la perte $L$ est mesurable et positive.
Montrer rigoureusement que lorsque la perturbation tend vers zéro ($\epsilon \to 0^+$ par valeurs discrètes $\epsilon_n \to 0$), le risque perturbé converge vers le risque vrai $\mathcal{R}_0 = \int_X L(x) dx$.

## Correction

1. **Définition de la suite fonctionnelle :**
Soit une suite de perturbations $\epsilon_n > 0$ qui décroît strictement vers 0 (par exemple $\epsilon_n = 1/n$).
Posons $f_n(x) = L(x) e^{-\epsilon_n |x|}$.
Puisque $L(x) \ge 0$ et l'exponentielle est positive, la suite est de fonctions mesurables positives.

2. **Analyse de monotonie :**
Puisque la suite $(\epsilon_n)$ est décroissante, pour un $x$ donné, la quantité $-\epsilon_n |x|$ est croissante.
L'exponentielle étant strictement croissante, la quantité $e^{-\epsilon_n |x|}$ est croissante.
Comme $L(x) \ge 0$, le produit $f_n(x) = L(x) e^{-\epsilon_n |x|}$ est croissant en $n$.

3. **Limite ponctuelle :**
Fixons $x$. Quand $n \to \infty$, $\epsilon_n \to 0$.
Par continuité de l'exponentielle en 0, $e^{-\epsilon_n |x|} \to e^0 = 1$.
Donc $f_n(x)$ converge simplement vers $f(x) = L(x) \times 1 = L(x)$.

4. **Application de Beppo Levi :**
Toutes les conditions du TCM sont remplies. On en déduit l'interversion de la limite et de l'intégrale :
$$ \lim_{n \to \infty} \mathcal{R}_{\epsilon_n} = \lim_{n \to \infty} \int_X f_n(x) dx = \int_X \lim_{n \to \infty} f_n(x) dx = \int_X L(x) dx = \mathcal{R}_0 $$
Cette preuve simple mais inattaquable garantit qu'optimiser un modèle régularisé par Tikhonov ou Decay Limit avec un coefficient s'évanouissant donne asymptotiquement le même comportement que le modèle non régularisé.
