---
uuid: "jalon-8"
title: "Applications linéaires, noyau (ker), image (Im) et démonstration du théorème du rang"
year: 1
trimester: 1
tags:
  - math/algebre-lineaire
  - ia/transformation-lineaire
prev: "[[Jalon 7 (Espaces vectoriels abstraits).md]]"
next: "[[Jalon 9 (Calcul matriciel).md]]"
---

# Jalon 8 : Applications linéaires, noyau ($\ker$), image ($\text{Im}$) et démonstration du théorème du rang

## 1. L'Intuition Première (Niveau 12 ans)
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez une machine à étirer ou à faire tourner de la pâte à modeler. 
  - L'**Application Linéaire**, c'est une machine respectueuse : si vous doublez la quantité de pâte au départ, vous aurez le double à l'arrivée. Si vous mettez deux morceaux de couleurs différentes, le résultat sera le même que si vous les aviez traités séparément puis mélangés.
  - Le **Noyau ($\ker$)**, c'est la "poubelle" de la machine : ce sont tous les morceaux de pâte qui finissent écrasés en un tout petit point (zéro) après le passage dans la machine.
  - L'**Image ($\text{Im}$)**, c'est l'ensemble de toutes les formes que la machine est capable de fabriquer.
  - Le **Théorème du Rang**, c'est la loi de conservation : la complexité totale de votre pâte au départ est égale à la somme de ce qui a été écrasé (Noyau) et de ce qui a été transformé (Image).
- **Le "Pourquoi on a inventé ça" :** La plupart des phénomènes physiques simples sont linéaires. En IA, transformer une image ou un texte revient souvent à appliquer une suite de ces machines. Savoir ce qui est "perdu" (le noyau) est vital.
- **Visualisation :** Imaginez projeter l'ombre d'un cube 3D sur une feuille 2D. L'ombre est l'**Image** (2D). La direction de la lumière qui "écrase" la profondeur est le **Noyau** (1D). $3 = 1 + 2$. C'est le théorème du rang !

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soient $E$ et $F$ deux $\mathbb{K}$-espaces vectoriels.
1. **Application Linéaire ($f : E \to F$) :** Une application vérifiant :
   - $\forall x, y \in E, f(x + y) = f(x) + f(y)$ (Additivité).
   - $\forall \lambda \in \mathbb{K}, \forall x \in E, f(\lambda \cdot x) = \lambda \cdot f(x)$ (Homogénéité).
   L'ensemble des applications linéaires de $E$ dans $F$ est noté $\mathcal{L}(E, F)$.

2. **Noyau ($\ker f$) :** $\ker f = \{ x \in E \mid f(x) = 0_F \}$. C'est un sous-espace vectoriel de $E$.
3. **Image ($\text{Im } f$) :** $\text{Im } f = f(E) = \{ f(x) \mid x \in E \}$. C'est un sous-espace vectoriel de $F$.
4. **Rang ($\text{rg } f$) :** On appelle rang de $f$ la dimension de son image : $\text{rg } f = \dim(\text{Im } f)$.

### B. Théorèmes, Propositions & Lemmes
> **Caractérisation de l'injectivité :**
> $f$ est injective $\iff \ker f = \{ 0_E \}$.

> **Théorème du Rang (Théorème Fondamental) :**
> Soit $E$ un espace vectoriel de dimension finie. Pour toute application linéaire $f : E \to F$, on a :
> $$\dim E = \dim(\ker f) + \text{rg}(f)$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Théorème du Rang
Soit $f \in \mathcal{L}(E, F)$ avec $\dim E = n$.

1. **Initialisation / Cadre :** 
   - Soit $p = \dim(\ker f)$. 
   - Soit $(e_1, ..., e_p)$ une base de $\ker f$.
   - D'après le théorème de la base incomplète, on peut compléter cette famille en une base de $E$ : $\mathcal{B} = (e_1, ..., e_p, e_{p+1}, ..., e_n)$.
   - Nous voulons montrer que $(f(e_{p+1}), ..., f(e_n))$ est une base de $\text{Im } f$. Si c'est le cas, alors $\dim(\text{Im } f) = n - p$, ce qui prouvera $n = p + (n-p)$.

2. **Étape 1 : Montrons que la famille est génératrice de $\text{Im } f$**
   Soit $y \in \text{Im } f$. Par définition, il existe $x \in E$ tel que $y = f(x)$.
   Comme $\mathcal{B}$ est une base de $E$, $x = \sum_{i=1}^n \lambda_i e_i$.
   Par linéarité de $f$ :
   $y = f(\sum_{i=1}^n \lambda_i e_i) = \sum_{i=1}^n \lambda_i f(e_i)$.
   Or, pour $i \in \{1, ..., p\}$, $e_i \in \ker f \implies f(e_i) = 0_F$.
   L'égalité devient : $y = \sum_{i=p+1}^n \lambda_i f(e_i)$.
   La famille est donc génératrice.

3. **Étape 2 : Montrons que la famille est libre**
   Supposons $\sum_{i=p+1}^n \mu_i f(e_i) = 0_F$.
   Par linéarité : $f(\sum_{i=p+1}^n \mu_i e_i) = 0_F$.
   Cela signifie que le vecteur $v = \sum_{i=p+1}^n \mu_i e_i$ appartient à $\ker f$.
   Comme $(e_1, ..., e_p)$ est une base de $\ker f$, il existe des scalaires $(\alpha_1, ..., \alpha_p)$ tels que :
   $\sum_{i=p+1}^n \mu_i e_i = \sum_{j=1}^p \alpha_j e_j$.
   En regroupant tout d'un côté : $\sum_{j=1}^p (-\alpha_j) e_j + \sum_{i=p+1}^n \mu_i e_i = 0_E$.
   Comme $\mathcal{B}$ est une base de $E$, elle est libre, donc tous les coefficients sont nuls.
   En particulier, $\forall i \in \{p+1, ..., n\}, \mu_i = 0$.
   La famille est donc libre.

4. **Conclusion :** $(f(e_{p+1}), ..., f(e_n))$ est une base de $\text{Im } f$. Son cardinal est $n - p$.
   Ainsi, $\text{rg}(f) = \dim E - \dim(\ker f)$.

## 4. Exercices d'Application & Pratique de Concours
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application Directe (Noyau et Image)
**Énoncé :** Soit $f : \mathbb{R}^3 \to \mathbb{R}^2$ définie par $f(x,y,z) = (x+y, y+z)$. Déterminer $\ker f$ et $\text{rg } f$.
**Correction Détaillée :**
1. **Noyau :** Résolvons $f(x,y,z) = (0,0)$.
   - $x+y = 0 \implies x = -y$
   - $y+z = 0 \implies z = -y$
   - Donc $\ker f = \{ (-y, y, -y) \mid y \in \mathbb{R} \} = \text{Vect}((-1, 1, -1))$.
   - $\dim(\ker f) = 1$.
2. **Théorème du rang :** $\dim \mathbb{R}^3 = \dim(\ker f) + \text{rg } f \implies 3 = 1 + \text{rg } f$.
   - $\text{rg } f = 2$.
**Conclusion :** Le noyau est une droite vectorielle et l'image est l'espace $\mathbb{R}^2$ tout entier (car $\dim(\text{Im } f) = \dim \mathbb{R}^2$).

### Exercice 2 : Niveau Avancé (Projecteurs)
**Énoncé :** Soit $p \in \mathcal{L}(E)$ tel que $p \circ p = p$. Démontrer que $E = \ker p \oplus \text{Im } p$.
**Correction Détaillée :**
1. **Analyse :** On doit montrer que pour tout $x \in E$, il existe un unique couple $(y, z) \in \ker p \times \text{Im } p$ tel que $x = y + z$.
2. **Existence (Analyse-Synthèse) :** Écrivons $x = (x - p(x)) + p(x)$.
   - Posons $z = p(x)$. Par définition, $z \in \text{Im } p$.
   - Posons $y = x - p(x)$. Calculons $p(y) = p(x - p(x)) = p(x) - p(p(x)) = p(x) - p(x) = 0$. Donc $y \in \ker p$.
   - L'existence est prouvée.
3. **Somme directe (Intersection) :** Soit $u \in \ker p \cap \text{Im } p$.
   - $u \in \ker p \implies p(u) = 0$.
   - $u \in \text{Im } p \implies \exists v \in E, u = p(v)$.
   - Alors $p(u) = p(p(v)) = p(v) = u$.
   - Comme $p(u) = 0$, on en déduit $u = 0$. L'intersection est réduite à $\{0\}$.
**Conclusion :** $E = \ker p \oplus \text{Im } p$.

## 5. Ancrage & Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** Les couches denses (Dense Layers / Linear Layers) des réseaux de neurones sont des applications affines (Linéaire + Translation).
- **Exemple Concret :** Dans la **réduction de dimension** et la **Compression de Réseaux**, on cherche à savoir si une couche linéaire a un gros **Noyau**. Si $\dim(\ker f)$ est grand, cela signifie que beaucoup de combinaisons d'entrées sont "oubliées" par le réseau. Le **Rang** de la matrice de poids d'une couche détermine la "capacité expressive" de cette couche. Un réseau "Low-Rank" est plus rapide à entraîner et moins sujet au sur-apprentissage (Overfitting).

## 6. Liens Sémantiques & Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon 7 (Espaces vectoriels abstraits)]]
- **Concepts Futurs dépendants :** [[Jalon 9 (Calcul matriciel)]], [[Jalon 30 (Trigonalisation d'endomorphismes et décomposition de Dunford.)]], [[Jalon 46 (Matrice jacobienne)]]
