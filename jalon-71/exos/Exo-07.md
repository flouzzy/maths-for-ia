# Exercice 7 : Astuce de l'intégrale de Dirichlet $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

On se propose de calculer l'intégrale de Dirichlet $I = \int_0^{+\infty} \frac{\sin x}{x} dx$ à l'aide du théorème de Fubini.
1. Justifier l'identité $\frac{1}{x} = \int_0^{+\infty} e^{-xt} dt$ pour $x > 0$.
2. Écrire $I$ comme une intégrale double, puis, en justifiant le changement d'ordre, calculer $I$.

## Correction

**1. Identité préliminaire :**
Pour tout $x > 0$, l'intégrale impropre $\int_0^{+\infty} e^{-xt} dt$ est convergente :
$$ \int_0^{+\infty} e^{-xt} dt = \left[ \frac{e^{-xt}}{-x} \right]_0^{+\infty} = 0 - \left(-\frac{1}{x}\right) = \frac{1}{x} $$

**2. Application de Fubini-Tonelli :**
On écrit $I = \lim_{R \to +\infty} \int_0^R \frac{\sin x}{x} dx$ (l'intégrale de Dirichlet est semi-convergente, elle n'est pas absolument convergente sur $[0, +\infty[$).
Cependant, pour appliquer Fubini de manière standard, on doit s'assurer de l'intégrabilité absolue. Considérons l'intégrale sur le domaine fini $[0, R] \times [0, +\infty[$.
Soit $f(x,t) = e^{-xt} \sin x$. Montrons que $f$ est intégrable sur $[0, R] \times \mathbb{R}_+$.
$$ \int_0^R \left( \int_0^{+\infty} |e^{-xt} \sin x| dt \right) dx = \int_0^R |\sin x| \left( \int_0^{+\infty} e^{-xt} dt \right) dx = \int_0^R \frac{|\sin x|}{x} dx $$
Cette dernière intégrale est finie car $\frac{|\sin x|}{x} \to 1$ en $x=0$ (elle se prolonge par continuité).
L'hypothèse d'intégrabilité absolue du théorème de Fubini est vérifiée sur ce domaine restreint.
On peut intervertir les intégrales pour l'intégrale sur $x \in [0, R]$ :
$$ \int_0^R \frac{\sin x}{x} dx = \int_0^R \left( \int_0^{+\infty} e^{-xt} \sin x \, dt \right) dx = \int_0^{+\infty} \left( \int_0^R e^{-xt} \sin x \, dx \right) dt $$
Calculons d'abord $\int_0^{+\infty} e^{-xt} \sin x dx$.
En intégrant par parties deux fois, ou en utilisant $\text{Im}(e^{(i-t)x})$, on trouve une primitive :
$$ \int_0^{+\infty} e^{-xt} \sin x dx = \frac{1}{1+t^2} $$
On doit faire attention avec le $R$. L'intégrale exacte est $\left[ \frac{e^{-xt}(-t \sin x - \cos x)}{1+t^2} \right]_0^R$.
En passant à la limite $R \to +\infty$, le terme de bord s'annule car $e^{-Rt} \to 0$ pour $t>0$.
La justification précise utilise le théorème de convergence dominée pour passer la limite sous l'intégrale en $t$.
On obtient :
$$ I = \int_0^{+\infty} \frac{1}{1+t^2} dt = \left[ \arctan(t) \right]_0^{+\infty} = \frac{\pi}{2} $$
