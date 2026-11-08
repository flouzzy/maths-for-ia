# Exercice 09

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Théorème Central Limite Linéaire.
Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires i.i.d., centrées ($\mathbb{E}[X_1] = 0$) et de variance unitaire ($\text{Var}(X_1) = 1$).
On forme la somme normalisée : $Z_n = \frac{1}{\sqrt{n}} \sum_{i=1}^n X_i$.
En admettant le théorème de Lévy sur les fonctions caractéristiques, démontrez pas à pas que $Z_n$ converge en loi vers la distribution normale standard $\mathcal{N}(0, 1)$.

**Correction :**

La démonstration repose sur l'analyse fine du développement limité des fonctions caractéristiques (transformées de Fourier).

**1. Fonction caractéristique de $X_1$ :**
Notons $\varphi_X(t) = \mathbb{E}[e^{itX_1}]$ la fonction caractéristique d'une des variables.
Puisque $X_1$ possède des moments finis jusqu'à l'ordre 2, sa fonction caractéristique admet un développement limité de Taylor-Young à l'ordre 2 au voisinage de l'origine ($t=0$) :
$$ \varphi_X(t) = \mathbb{E}[1] + it\mathbb{E}[X_1] + \frac{(it)^2}{2}\mathbb{E}[X_1^2] + o(t^2) $$
Introduisons nos hypothèses fortes :
- L'espérance est nulle : $\mathbb{E}[X_1] = 0$.
- La variable étant centrée, son moment d'ordre 2 s'identifie à la variance, qui est unitaire : $\mathbb{E}[X_1^2] = 1$.
En substituant, le développement se simplifie drastiquement :
$$ \varphi_X(t) = 1 + 0 - \frac{t^2}{2} + o(t^2) $$

**2. Fonction caractéristique de la somme :**
Posons $S_n = \sum_{i=1}^n X_i$. Par stricte indépendance des variables aléatoires, l'espérance du produit des exponentielles se factorise en produit des espérances. La fonction caractéristique de la somme est le produit des fonctions caractéristiques individuelles :
$$ \varphi_{S_n}(t) = \mathbb{E}\left[e^{it(X_1 + \dots + X_n)}\right] = \prod_{i=1}^n \mathbb{E}[e^{itX_i}] = \left( \varphi_X(t) \right)^n $$

**3. Fonction caractéristique de la somme normalisée $Z_n$ :**
La variable qui nous intéresse est rescalée par le facteur $1/\sqrt{n}$. Par propriété élémentaire de la transformée de Fourier, le changement d'échelle s'applique à l'argument :
$$ \varphi_{Z_n}(t) = \varphi_{S_n/\sqrt{n}}(t) = \varphi_{S_n}\left(\frac{t}{\sqrt{n}}\right) = \left( \varphi_X\left(\frac{t}{\sqrt{n}}\right) \right)^n $$

**4. Analyse asymptotique :**
Fixons $t \in \mathbb{R}$. Lorsque $n$ tend vers l'infini, l'argument $t/\sqrt{n}$ tend invariablement vers $0$. Nous sommes donc parfaitement légitimés à injecter cet argument dans notre développement limité local :
$$ \varphi_X\left(\frac{t}{\sqrt{n}}\right) = 1 - \frac{1}{2} \left(\frac{t}{\sqrt{n}}\right)^2 + o\left( \left(\frac{t}{\sqrt{n}}\right)^2 \right) $$
$$ \varphi_X\left(\frac{t}{\sqrt{n}}\right) = 1 - \frac{t^2}{2n} + o\left(\frac{1}{n}\right) $$
Élevons ce terme à la puissance $n$ pour obtenir la fonction caractéristique complète de $Z_n$ :
$$ \varphi_{Z_n}(t) = \left( 1 - \frac{t^2}{2n} + o\left(\frac{1}{n}\right) \right)^n $$

Appliquons le passage au logarithme (ou le lemme classique sur les limites des suites du type $(1 + c/n)^n$) pour traiter cette forme indéterminée $1^\infty$.
Rappelons la limite fondamentale de l'analyse : $\lim_{n \to \infty} (1 + \frac{x_n}{n})^n = e^x$ dès lors que la suite réelle $x_n \to x$.
Ici, $x_n = -\frac{t^2}{2} + n \cdot o(\frac{1}{n})$. Par définition du petit $o$, la quantité $n \cdot o(1/n)$ tend vers $0$. Donc $x_n \to -t^2/2$.
Le passage à la limite devient trivial :
$$ \lim_{n \to \infty} \varphi_{Z_n}(t) = e^{-t^2/2} $$

**5. Conclusion via le théorème de continuité :**
Nous reconnaissons l'expression $e^{-t^2/2}$ comme étant la fonction caractéristique exacte d'une variable suivant la loi normale standard $\mathcal{N}(0, 1)$.
Le théorème de continuité de Paul Lévy stipule qu'une convergence simple des fonctions caractéristiques vers une fonction continue en zéro (ce qui est notre cas) équivaut à la convergence en loi de la suite de variables aléatoires vers la distribution associée.
Nous concluons donc avec une absolue certitude que :
$$ Z_n \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1) $$
