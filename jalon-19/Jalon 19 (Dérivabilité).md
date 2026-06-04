---
uuid: "jalon-19"
title: "Dérivabilité, théorème de Rolle, théorème des accroissements finis et prolongement de la dérivée"
year: 1
trimester: 2
tags:
  - math/analyse
  - ia/optimisation-locale
prev: "[[Jalon 18 (Continuité des fonctions d'une variable réelle).md]]"
next: "[[Jalon 20 (Dérivées successives).md]]"
---

# Jalon 19 : Dérivabilité, théorème de Rolle, théorème des accroissements finis et prolongement de la dérivée

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez que vous conduisez une voiture. Votre compteur de vitesse vous indique votre vitesse à chaque seconde précise. La **Dérivée**, c'est exactement cette vitesse instantanée. Si la courbe est votre trajet, la dérivée est l'inclinaison de la route sous vos pneus.
  - Le **Théorème de Rolle**, c'est comme dire : si vous partez de chez vous, faites un tour, et revenez exactement à la même altitude, il y a forcément eu un moment pendant votre trajet où vous étiez sur un replat (vitesse verticale nulle).
  - Le **Théorème des Accroissements Finis (TAF)**, c'est la version routière : si vous avez parcouru 100 km en 1 heure, il y a eu au moins un instant précis où votre compteur affichait exactement 100 km/h.
- **Le "Pourquoi on a inventé ça" :** La continuité nous dit qu'on peut dessiner sans lever le crayon. La dérivabilité nous dit qu'on peut dessiner sans faire d'angles pointus. C'est l'outil suprême pour trouver les sommets (maxima) et les vallées (minima) d'une fonction.
- **Visualisation :** Imaginez zoomer sur une courbe. Si elle est dérivable, plus vous zoomez, plus la courbe ressemble à une ligne droite (la tangente).

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $I$ un intervalle ouvert et $f : I \to \mathbb{R}$.
1. **Dérivabilité en un point :** $f$ est dérivable en $x_0 \in I$ si le taux d'accroissement admet une limite finie quand $h \to 0$ :
   $$f'(x_0) = \lim_{h \to 0} \frac{f(x_0+h) - f(x_0)}{h}$$
2. **Interprétation Géométrique :** $f'(x_0)$ est la pente de la tangente à la courbe de $f$ au point $(x_0, f(x_0))$.
3. **Classe $C^1$ :** $f$ est de classe $C^1$ sur $I$ si elle est dérivable sur $I$ et si sa dérivée $f'$ est continue sur $I$.

### B. Théorèmes, Propositions & Lemmes
> **Théorème de Rolle :**
> Soit $f$ continue sur $[a, b]$ et dérivable sur $]a, b[$.
> Si $f(a) = f(b)$, alors il existe $c \in ]a, b[$ tel que $f'(c) = 0$.

> **Théorème des Accroissements Finis (TAF) :**
> Soit $f$ continue sur $[a, b]$ et dérivable sur $]a, b[$. Alors il existe $c \in ]a, b[$ tel que :
> $$f(b) - f(a) = f'(c)(b - a)$$

> **Inégalité des Accroissements Finis :**
> Si $|f'(x)| \le M$ pour tout $x \in I$, alors $|f(b) - f(a)| \le M|b - a|$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Théorème des Accroissements Finis
Soit $f$ vérifiant les hypothèses du TAF sur $[a, b]$.

1. **Initialisation / Cadre :** 
   L'idée est de se ramener au théorème de Rolle. Pour cela, on définit une fonction auxiliaire $g$ qui "redresse" la courbe pour que ses extrémités soient à la même altitude.
   Soit $\lambda$ le coefficient directeur de la corde reliant $(a, f(a))$ à $(b, f(b))$ :
   $$\lambda = \frac{f(b) - f(a)}{b - a}$$
   Posons la fonction $g(x) = f(x) - \lambda (x - a)$.

2. **Étape 1 : Vérification des hypothèses de Rolle pour $g$**
   - $g$ est continue sur $[a, b]$ comme somme de fonctions continues.
   - $g$ est dérivable sur $]a, b[$ comme somme de fonctions dérivables.
   Calculons les valeurs aux bornes :
   - $g(a) = f(a) - \lambda(a - a) = f(a)$.
   - $g(b) = f(b) - \lambda(b - a) = f(b) - \frac{f(b) - f(a)}{b - a} \times (b - a)$.
     $g(b) = f(b) - (f(b) - f(a)) = f(a)$.
   - On a donc $g(a) = g(b)$.

3. **Étape 2 : Application du théorème de Rolle**
   D'après le théorème de Rolle appliqué à $g$, il existe un réel $c \in ]a, b[$ tel que $g'(c) = 0$.

4. **Étape 3 : Retour à la fonction $f$**
   Calculons la dérivée de $g$ :
   $g'(x) = f'(x) - \lambda$.
   En $c$ : $g'(c) = f'(c) - \lambda = 0$.
   Ceci implique $f'(c) = \lambda$.
   Substituons la valeur de $\lambda$ :
   $$f'(c) = \frac{f(b) - f(a)}{b - a}$$

5. **Conclusion :**
   En multipliant par $(b-a)$, on obtient l'égalité recherchée :
   $f(b) - f(a) = f'(c)(b - a)$.
   Le théorème est démontré.

## 4. Exercices d'Application & Pratique de Concours
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application de l'Inégalité des Accroissements Finis
**Énoncé :** Démontrer que pour tous réels $x$ et $y$, $|\sin(x) - \sin(y)| \le |x - y|$.
**Correction Détaillée :**
1. Soit $f(t) = \sin(t)$. $f$ est dérivable sur $\mathbb{R}$.
2. Calculons la dérivée : $f'(t) = \cos(t)$.
3. On sait que pour tout réel $t$, $|\cos(t)| \le 1$.
4. Appliquons l'inégalité des accroissements finis à $f$ entre $x$ et $y$.
5. On a $|f(x) - f(y)| \le (\sup |f'|) \cdot |x - y|$.
6. En remplaçant : $|\sin(x) - \sin(y)| \le 1 \cdot |x - y|$.
**Conclusion :** La fonction sinus est 1-lipschitzienne sur $\mathbb{R}$.

### Exercice 2 : Niveau Avancé (Théorème de Darboux)
**Énoncé :** Soit $f$ dérivable sur $[a, b]$. Montrer que si $f'(a) < y < f'(b)$, alors il existe $c \in ]a, b[$ tel que $f'(c) = y$. (La dérivée vérifie le TVI, même si elle n'est pas continue).
**Correction Détaillée :**
1. Considérons $g(x) = f(x) - yx$. $g$ est dérivable sur $[a, b]$ et $g'(x) = f'(x) - y$.
2. On a $g'(a) = f'(a) - y < 0$ et $g'(b) = f'(b) - y > 0$.
3. Comme $g$ est dérivable sur $[a, b]$, elle est continue. D'après le théorème de Weierstrass, $g$ admet un minimum sur le segment $[a, b]$.
4. Étudions le bord : Comme $g'(a) < 0$, la fonction $g$ est localement décroissante à droite de $a$. Donc le minimum ne peut pas être en $a$.
5. Comme $g'(b) > 0$, la fonction $g$ est localement croissante à gauche de $b$. Donc le minimum ne peut pas être en $b$.
6. Le minimum est donc atteint en un point $c \in ]a, b[$.
7. Comme $c$ est un extremum local dans un ouvert, la dérivée y est nulle : $g'(c) = 0$.
8. $f'(c) - y = 0 \implies f'(c) = y$.
**Conclusion :** La propriété des valeurs intermédiaires est vérifiée par toute fonction dérivée.

## 5. Ancrage & Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** La dérivabilité est la pierre angulaire de l'**Optimisation par Gradient**. La pente nous indique dans quelle direction modifier les poids pour descendre vers l'erreur minimale.
- **Exemple Concret :** Dans la **Rétropropagation (Backpropagation)**, on calcule des dérivées partielles. Le fait que les fonctions d'activation (comme ReLU, GELU ou Sigmoïde) soient presque partout dérivables permet d'utiliser le TAF pour analyser la stabilité du réseau. Par exemple, pour éviter l'**Explosion du Gradient**, on s'assure que la norme de la dérivée (le "gain" de la couche) reste bornée, souvent en utilisant l'inégalité des accroissements finis pour prouver que la transformation est contractante.

## 6. Liens Sémantiques & Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon 18 (Continuité des fonctions d'une variable réelle)]]
- **Concepts Futurs dépendants :** [[Jalon 20 (Dérivées successives)]], [[Jalon 45 (Différentiabilité)]], [[Jalon 128 (Flots de gradient)]]
