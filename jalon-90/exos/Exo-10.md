---
uuid: "jalon-90-exo-10"
title: "Un contre-exemple topologique profond"
---

# Exercice 10 : Un contre-exemple topologique profond (Difficulté $\bigstar\bigstar\bigstar\bigstar\bigstar$)

La convergence en probabilité définit une structure topologique sur l'espace des variables aléatoires (quotienté par l'égalité presque sûre).
Montrer qu'il est possible de construire une distance $d$ sur cet espace telle que $X_n \xrightarrow{\mathbb{P}} X \iff \lim_{n \to \infty} d(X_n, X) = 0$.

## Correction Pas-à-Pas

1. **Construction de la distance :**
   Considérons la fonction suivante pour deux variables aléatoires $X$ et $Y$ :
   $$ d(X, Y) = \mathbb{E}\left[ \frac{|X - Y|}{1 + |X - Y|} \right] $$
   Montrons d'abord qu'il s'agit bien d'une distance (métrique) sur l'espace des variables aléatoires.
   - *Séparation :* $d(X, Y) = 0 \iff \mathbb{E}[ \dots ] = 0$. Comme la quantité intégrée est positive et continue en l'écart, l'espérance est nulle si et seulement si $\frac{|X - Y|}{1 + |X - Y|} = 0$ presque sûrement. Cela équivaut à $|X - Y| = 0$ p.s., soit $X = Y$ p.s.
   - *Symétrie :* Évidente par symétrie de la valeur absolue : $d(X, Y) = d(Y, X)$.
   - *Inégalité triangulaire :* Considérons la fonction scalaire $h(x) = \frac{x}{1+x}$ pour $x \geq 0$. Sa dérivée est $h'(x) = \frac{1}{(1+x)^2} > 0$, donc $h$ est croissante. De plus, $h(a+b) = \frac{a+b}{1+a+b} = \frac{a}{1+a+b} + \frac{b}{1+a+b} \leq \frac{a}{1+a} + \frac{b}{1+b} = h(a) + h(b)$.
     En appliquant cette propriété sous-additive avec $a = |X - Z|$ et $b = |Z - Y|$ :
     $$ |X - Y| \leq |X - Z| + |Z - Y| $$
     $$ h(|X - Y|) \leq h(|X - Z| + |Z - Y|) \leq h(|X - Z|) + h(|Z - Y|) $$
     En prenant l'espérance (la linéarité préserve l'inégalité) :
     $$ \mathbb{E}[h(|X - Y|)] \leq \mathbb{E}[h(|X - Z|)] + \mathbb{E}[h(|Z - Y|)] $$
     Soit $d(X, Y) \leq d(X, Z) + d(Z, Y)$. La distance est validée.

2. **Preuve de l'équivalence ($\impliedby$) :**
   Supposons $\lim_{n \to \infty} d(X_n, X) = 0$. Nous voulons montrer $X_n \xrightarrow{\mathbb{P}} X$.
   Fixons $\epsilon > 0$.
   La fonction scalaire $h(x) = \frac{x}{1+x}$ est croissante. Sur l'événement $A_n = \{ |X_n - X| > \epsilon \}$, nous avons :
   $$ h(|X_n - X|) > h(\epsilon) = \frac{\epsilon}{1+\epsilon} $$
   Par l'inégalité de Markov classique appliquée à la variable bornée $Z = h(|X_n - X|)$ :
   $$ \mathbb{P}\left(|X_n - X| > \epsilon\right) = \mathbb{P}\left(h(|X_n - X|) > h(\epsilon)\right) \leq \frac{\mathbb{E}[h(|X_n - X|)]}{h(\epsilon)} = \frac{d(X_n, X)}{\frac{\epsilon}{1+\epsilon}} $$
   Puisque $d(X_n, X) \to 0$, la borne supérieure de la probabilité tend vers $0$.
   Ainsi, $\lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) = 0$, soit la convergence en probabilité.

3. **Preuve de l'équivalence ($\implies$) :**
   Supposons $X_n \xrightarrow{\mathbb{P}} X$. Nous voulons montrer $d(X_n, X) \to 0$.
   Fixons $\eta > 0$.
   Décomposons l'espérance de la distance sur deux événements, conditionnés par un seuil $\delta > 0$ à choisir :
   $E_1 = \{ |X_n - X| \leq \delta \}$ et $E_2 = \{ |X_n - X| > \delta \}$.
   $$ d(X_n, X) = \mathbb{E}\left[ \frac{|X_n - X|}{1 + |X_n - X|} \mathbf{1}_{E_1} \right] + \mathbb{E}\left[ \frac{|X_n - X|}{1 + |X_n - X|} \mathbf{1}_{E_2} \right] $$
   - Sur $E_1$, l'argument de l'espérance est majoré par $\frac{\delta}{1+\delta} \leq \delta$. Donc la première intégrale est $\leq \delta \mathbb{P}(E_1) \leq \delta$.
   - Sur $E_2$, on utilise la majoration brute $\frac{x}{1+x} \leq 1$. Donc la seconde intégrale est $\leq 1 \cdot \mathbb{P}(E_2) = \mathbb{P}(|X_n - X| > \delta)$.

   Ainsi, $d(X_n, X) \leq \delta + \mathbb{P}(|X_n - X| > \delta)$.
   Choisissons $\delta = \eta / 2$.
   Par l'hypothèse de convergence en probabilité, $\lim_{n \to \infty} \mathbb{P}(|X_n - X| > \eta / 2) = 0$.
   Il existe un entier $N$ tel que pour tout $n \geq N$, $\mathbb{P}(|X_n - X| > \eta / 2) < \eta / 2$.
   Pour ces $n \geq N$ :
   $$ d(X_n, X) \leq \frac{\eta}{2} + \frac{\eta}{2} = \eta $$
   Puisque $\eta$ est arbitraire, la limite de la distance est bien $0$.
   L'équivalence topologique est ainsi démontrée.
   $\blacksquare$

