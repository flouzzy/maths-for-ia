---
title: "Exercice 3 : Limite et Coordonnées Polaires"
difficulty: $\bigstar\bigstar\bigstar\star\star$
---

# Exercice 3 : Limite et Coordonnées Polaires

## Énoncé

Montrer que la fonction suivante est prolongeable par continuité en $(0,0)$ :
$$ h(x, y) = \frac{x^3 + y^3}{x^2 + y^2} $$
Quelle valeur doit-on assigner à $h(0,0)$ ?

## Solution détaillée

1. **Identification de la méthode** :
   L'expression $x^2 + y^2$ au dénominateur suggère fortement un passage en coordonnées polaires pour évaluer la limite en $(0,0)$.

2. **Passage en coordonnées polaires** :
   Posons $x = r \cos \theta$ et $y = r \sin \theta$.
   Le point $(x,y)$ tend vers $(0,0)$ si et seulement si le rayon $r$ tend vers $0^+$, indépendamment de l'angle $\theta$.
   Substituons dans $h(x,y)$ :
   $$ h(r \cos \theta, r \sin \theta) = \frac{(r \cos \theta)^3 + (r \sin \theta)^3}{(r \cos \theta)^2 + (r \sin \theta)^2} $$
   $$ h(r \cos \theta, r \sin \theta) = \frac{r^3 \cos^3 \theta + r^3 \sin^3 \theta}{r^2 (\cos^2 \theta + \sin^2 \theta)} $$

3. **Simplification** :
   En utilisant l'identité fondamentale $\cos^2 \theta + \sin^2 \theta = 1$, on obtient :
   $$ h(r \cos \theta, r \sin \theta) = \frac{r^3 (\cos^3 \theta + \sin^3 \theta)}{r^2} = r (\cos^3 \theta + \sin^3 \theta) $$

4. **Majoration indépendante de $\theta$** :
   Nous devons majorer l'expression absolue pour appliquer le théorème des gendarmes.
   $$ |h(r \cos \theta, r \sin \theta)| = |r (\cos^3 \theta + \sin^3 \theta)| $$
   $$ |h(r \cos \theta, r \sin \theta)| = r |\cos^3 \theta + \sin^3 \theta| $$

   En utilisant l'inégalité triangulaire et le fait que $|\cos \theta| \leq 1$ et $|\sin \theta| \leq 1$ :
   $$ |\cos^3 \theta + \sin^3 \theta| \leq |\cos \theta|^3 + |\sin \theta|^3 \leq 1^3 + 1^3 = 2 $$

   Ainsi, on a la majoration uniforme par rapport à $\theta$ :
   $$ 0 \leq |h(r \cos \theta, r \sin \theta)| \leq 2r $$

5. **Conclusion par encadrement** :
   Comme $\lim_{r \to 0^+} 2r = 0$, le théorème d'encadrement donne :
   $$ \lim_{r \to 0^+} |h(r \cos \theta, r \sin \theta)| = 0 $$
   Ce qui signifie que la limite de $h(x,y)$ en $(0,0)$ existe et vaut $0$.
   La fonction est donc prolongeable par continuité en posant $h(0,0) = 0$.
