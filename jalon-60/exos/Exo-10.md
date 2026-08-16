---
title: "Exercice 10 : Séparation par la Profondeur (Depth Separation)"
difficulty: $\bigstar\bigstar\bigstar\bigstar\bigstar$
---

# Exercice 10 : Séparation par la Profondeur (Depth Separation)

## Énoncé

Soit la fonction en "dents de scie" $f(x)$ définie sur $[0,1]$ par la répétition de $M$ triangles (hauteur 1).
Montrez qu'un réseau profond de $L$ couches avec $k$ neurones par couche (utilisant ReLU) peut construire une fonction en dents de scie avec un nombre de "pics" qui croît exponentiellement avec $L$. Déduisez-en pourquoi les réseaux profonds sont exponentiellement plus expressifs que les réseaux à une seule couche.

## Correction Rigoureuse

**Étape 1 : L'opérateur de pliage de base**
Considérons l'opérateur $g(x) = 2\sigma(x) - 4\sigma(x - 0.5) + 2\sigma(x - 1)$ sur $[0, 1]$.
Cette fonction $g$ (qui utilise 3 neurones) prend un intervalle $[0, 1]$, monte à $1$ en $x=0.5$, puis redescend à $0$ en $x=1$.
Elle plie l'espace en deux : à la fois $[0, 0.5]$ et $[0.5, 1]$ sont mappés sur $[0, 1]$. C'est un pic unique.

**Étape 2 : Composition (Profondeur)**
Composons $g$ avec elle-même.
$g(g(x))$ : Puisque $g$ a généré une montée puis une descente, la recomposition va générer un pic complet sur la phase de montée, et un autre sur la phase de descente. On obtient 2 pics.
Par récurrence, l'itération $g^{\circ L}(x) = g(g(\dots(x)))$ génère $2^{L-1}$ pics.

**Étape 3 : Comptage des neurones**
Chaque application de $g$ requiert une couche de largeur constante (par exemple 3 neurones).
Pour une profondeur $L$, nous avons utilisé environ $3L$ neurones et généré $N_{pics} = 2^{L-1}$ dents de scie.

**Étape 4 : Comparaison avec un réseau shallow (peu profond)**
Un réseau avec une seule couche cachée, de la forme $G(x) = \sum_{i=1}^N \alpha_i \sigma(w_i x + b_i)$, crée au plus un changement de pente par neurone.
Pour générer $2^{L-1}$ pics (qui nécessitent au minimum $2 \times 2^{L-1}$ changements de pente), un réseau *shallow* nécessitera au moins $N \approx 2^L$ neurones.

**Étape 5 : Conclusion**
Le réseau profond nécessite $\mathcal{O}(L)$ paramètres, alors que le réseau plat requiert $\mathcal{O}(2^L)$ paramètres pour représenter exactement la même fonction oscillante. L'efficacité spatiale croît de manière exponentielle avec la profondeur. $\blacksquare$
