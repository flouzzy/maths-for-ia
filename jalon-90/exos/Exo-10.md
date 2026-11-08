# Exercice 10

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Théorème de Slutsky (Cas Particulier par l'analyse).
Soient deux suites de variables aléatoires $(X_n)$ et $(Y_n)$ définies sur le même espace probabilisé.
On suppose que $X_n \xrightarrow{\mathcal{L}} X$ (convergence en loi) et $Y_n \xrightarrow{\mathbb{P}} c$ (convergence en probabilité vers une constante stricte $c$).
Démontrez de manière totalement rigoureuse, en utilisant l'espérance des fonctions continues et bornées, que la somme $(X_n + Y_n)$ converge en loi vers $(X + c)$.

**Correction :**

La définition analytique de la convergence en loi (Portmanteau) stipule que pour toute fonction $f : \mathbb{R} \to \mathbb{R}$ continue et bornée, l'espérance de l'image de la suite converge vers l'espérance de l'image de la limite.
Nous devons donc montrer l'objectif suivant :
$$ \lim_{n \to \infty} \mathbb{E}[f(X_n + Y_n)] = \mathbb{E}[f(X + c)] $$
Soit $f$ une fonction continue et bornée. Notons $M = \sup_{x \in \mathbb{R}} |f(x)|$.
Pour des raisons techniques de contrôle, supposer $f$ uniformément continue simplifie drastiquement la preuve. L'extension à toute fonction continue bornée se fait ensuite par densité ou par restriction aux compacts (tension des mesures). Adoptons l'hypothèse d'uniforme continuité.

**1. Stratégie de décomposition par inégalité triangulaire :**
Évaluons l'écart absolu entre les espérances. Nous introduisons le terme relais croisé $\mathbb{E}[f(X_n + c)]$ via l'inégalité triangulaire :
$$ \left| \mathbb{E}[f(X_n + Y_n)] - \mathbb{E}[f(X + c)] \right| = \left| \mathbb{E}[f(X_n + Y_n)] - \mathbb{E}[f(X_n + c)] + \mathbb{E}[f(X_n + c)] - \mathbb{E}[f(X + c)] \right| $$
$$ \le \left| \mathbb{E}[f(X_n + Y_n) - f(X_n + c)] \right| + \left| \mathbb{E}[f(X_n + c)] - \mathbb{E}[f(X + c)] \right| $$
Par l'inégalité fondamentale $\left| \mathbb{E}[Z] \right| \le \mathbb{E}[|Z|]$, nous majorons le premier terme :
$$ \Delta_n \le \underbrace{\mathbb{E}\left[ \left| f(X_n + Y_n) - f(X_n + c) \right| \right]}_{\text{Terme 1}} + \underbrace{\left| \mathbb{E}[f(X_n + c)] - \mathbb{E}[f(X + c)] \right|}_{\text{Terme 2}} $$

**2. Annihilation du Terme 2 (Convergence en loi pure) :**
Définissons la fonction auxiliaire $g(x) = f(x + c)$. Puisque $f$ est continue et bornée, sa translatée $g$ hérite instantanément de ces deux propriétés sur $\mathbb{R}$.
Par l'hypothèse stricte que $X_n \xrightarrow{\mathcal{L}} X$, la caractérisation analytique nous assure que :
$$ \lim_{n \to \infty} \mathbb{E}[g(X_n)] = \mathbb{E}[g(X)] $$
Ce qui se traduit littéralement par :
$$ \lim_{n \to \infty} \left| \mathbb{E}[f(X_n + c)] - \mathbb{E}[f(X + c)] \right| = 0 $$
Le Terme 2 s'évanouit asymptotiquement.

**3. Annihilation du Terme 1 (Convergence en probabilité) :**
Analysons le Terme 1. Fixons un seuil de tolérance $\varepsilon > 0$ arbitraire.
Par l'hypothèse d'uniforme continuité de la fonction $f$, il existe un rayon protecteur $\delta > 0$ tel que pour tout couple $(a, b) \in \mathbb{R}^2$, la contrainte de proximité $|a - b| < \delta$ force la proximité des images $|f(a) - f(b)| < \varepsilon$.

Posons $a = X_n(\omega) + Y_n(\omega)$ et $b = X_n(\omega) + c$. La distance entre les antécédents est exactement l'écart résiduel : $|a - b| = |Y_n(\omega) - c|$.
Nous partitionnons l'espace fondamental $\Omega$ selon la réalisation de l'événement de proximité $\{|Y_n - c| < \delta\}$ et son événement complémentaire.
Décomposons l'espérance par la loi des probabilités totales généralisées (indicateurs) :
$$ \mathbb{E}\left[ \left| f(X_n + Y_n) - f(X_n + c) \right| \right] = \mathbb{E}\left[ |f(\dots)| \cdot \mathbf{1}_{\{|Y_n - c| < \delta\}} \right] + \mathbb{E}\left[ |f(\dots)| \cdot \mathbf{1}_{\{|Y_n - c| \ge \delta\}} \right] $$

Sur le premier domaine (où la proximité est acquise), l'uniforme continuité garantit brutalement que la différence des images est majorée par $\varepsilon$.
Sur le second domaine, nous ne contrôlons pas les antécédents, mais nous utilisons la borne absolue de la fonction : $|f(X_n+Y_n) - f(X_n+c)| \le |f(X_n+Y_n)| + |f(X_n+c)| \le 2M$.
Injectons ces majorations uniformes dans l'espérance :
$$ \mathbb{E}\left[ \left| f(X_n + Y_n) - f(X_n + c) \right| \right] \le \varepsilon \cdot \mathbb{P}(|Y_n - c| < \delta) + 2M \cdot \mathbb{P}(|Y_n - c| \ge \delta) $$

Il est temps de tirer parti de la convergence en probabilité. Par hypothèse $Y_n \xrightarrow{\mathbb{P}} c$, ce qui signifie précisément que pour notre $\delta > 0$ constant :
$$ \lim_{n \to \infty} \mathbb{P}(|Y_n - c| \ge \delta) = 0 $$
Le terme minoritaire $\mathbb{P}(|Y_n - c| < \delta)$ est, bien sûr, majoré par 1.
En passant à la limite supérieure (limsup) sur l'ensemble de la majoration, le terme en $2M$ disparaît :
$$ \limsup_{n \to \infty} \mathbb{E}\left[ \left| f(X_n + Y_n) - f(X_n + c) \right| \right] \le \varepsilon \cdot 1 + 2M \cdot 0 = \varepsilon $$
Cette majoration finale étant valable pour tout $\varepsilon > 0$ aussi infime soit-il, la limite supérieure est nécessairement nulle :
$$ \lim_{n \to \infty} \mathbb{E}\left[ \left| f(X_n + Y_n) - f(X_n + c) \right| \right] = 0 $$

**Conclusion finale :**
Le Terme 1 et le Terme 2 tendant séparément vers 0, la somme (par l'inégalité triangulaire) assure que la différence globale d'espérance s'annule :
$$ \lim_{n \to \infty} \mathbb{E}[f(X_n + Y_n)] = \mathbb{E}[f(X + c)] $$
Cette équation prouve, avec une absolue rigueur analytique, la convergence en loi du couple combiné :
$$ X_n + Y_n \xrightarrow{\mathcal{L}} X + c $$
Ce théorème, cœur réacteur de l'inférence statistique asymptotique, permet de manipuler les limites stochastiques presque comme de l'algèbre classique, tant que l'un des termes converge vers un pôle déterministe.
