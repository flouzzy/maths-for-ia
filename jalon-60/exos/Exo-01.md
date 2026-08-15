# Exercice 1 : Approximation d'une constante $\bigstar$
On considère le cube $I_1 = [0,1]$ et la fonction d'activation sigmoïde $\sigma(t) = \frac{1}{1+e^{-t}}$.
Soit $f(x) = 3$ pour tout $x \in I_1$.
Construire explicitement une fonction $G(x) = \alpha \sigma(wx + b)$ telle que $\|f - G\|_\infty < 0.01$.

\textbf{Correction détaillée}
On cherche $G(x) = \alpha \sigma(wx + b)$.
Posons $w = 0$, la fonction devient constante par rapport à $x$ : $G(x) = \alpha \sigma(b)$.
On veut approcher la valeur 3. Si on choisit $b$ très grand, par exemple $b = 10$, on a $\sigma(10) = \frac{1}{1+e^{-10}} \approx 0.9999546$.
Pour que $G(x) = 3$, il faut choisir $\alpha = \frac{3}{\sigma(10)} = 3(1+e^{-10}) \approx 3.000136$.
Ainsi, avec $w=0, b=10, \alpha = 3(1+e^{-10})$, on a $G(x) = 3$ exactement pour tout $x \in [0,1]$.
L'erreur est rigoureusement nulle, ce qui satisfait $\|f - G\|_\infty < 0.01$.
