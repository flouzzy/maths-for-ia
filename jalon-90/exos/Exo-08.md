\subsection*{Exercice 8 : La méthode Delta \quad $\bigstar\bigstar\bigstar\bigstar\star$}

Soit $(X_n)$ une suite de variables aléatoires telle que $\sqrt{n}(X_n - \mu) \xrightarrow{\mathcal{L}} \mathcal{N}(0, \sigma^2)$.
Soit $g : \mathbb{R} \to \mathbb{R}$ une fonction dérivable en $\mu$ avec $g'(\mu) \neq 0$.
Montrer que $\sqrt{n}(g(X_n) - g(\mu)) \xrightarrow{\mathcal{L}} \mathcal{N}(0, (g'(\mu)\sigma)^2)$.

**Correction :**
La dérivabilité de $g$ en $\mu$ permet d'écrire le développement limité d'ordre 1 :
$g(x) = g(\mu) + (x - \mu)g'(\mu) + (x - \mu)\varepsilon(x - \mu)$, où $\lim_{x \to \mu} \varepsilon(x - \mu) = 0$.
En substituant la variable aléatoire $X_n$ à $x$, on obtient :
$g(X_n) - g(\mu) = (X_n - \mu) g'(\mu) + (X_n - \mu) \varepsilon(X_n - \mu)$.
Multiplions l'équation par $\sqrt{n}$ :
$\sqrt{n}(g(X_n) - g(\mu)) = \sqrt{n}(X_n - \mu) g'(\mu) + \sqrt{n}(X_n - \mu) \varepsilon(X_n - \mu)$.
Par hypothèse, le terme $\sqrt{n}(X_n - \mu)$ converge en loi vers $Z \sim \mathcal{N}(0, \sigma^2)$.
La constante $g'(\mu)$ multipliant $Z$ donne une convergence en loi du premier terme vers $g'(\mu)Z \sim \mathcal{N}(0, (g'(\mu)\sigma)^2)$.
Il reste à montrer que le second terme tend vers 0 en probabilité.
Puisque $\sqrt{n}(X_n - \mu) \xrightarrow{\mathcal{L}} Z$, la suite est tendue (uniformément bornée en probabilité, $O_P(1)$).
De plus, la convergence en loi vers une limite fixe finie implique que $X_n \xrightarrow{\mathbb{P}} \mu$.
Par continuité de $\varepsilon$, $\varepsilon(X_n - \mu) \xrightarrow{\mathbb{P}} 0$ ($o_P(1)$).
Le produit d'un terme $O_P(1)$ par un terme $o_P(1)$ converge en probabilité vers 0 (Slutsky).
Ainsi, le second terme disparaît à la limite, et la convergence finale est assurée.
