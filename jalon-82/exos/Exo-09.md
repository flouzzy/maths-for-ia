\subsection*{Exercice 9 : Égalité de distributions : vp et partie réelle \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

Soit $\epsilon > 0$ et $f_\epsilon(x) = \frac{1}{x + i\epsilon}$.
Montrer que, au sens des distributions (c'est-à-dire la limite de l'action de $f_\epsilon$ sur une fonction test quand $\epsilon \to 0^+$) :
$\lim_{\epsilon \to 0^+} \frac{1}{x + i\epsilon} = \text{vp}\left(\frac{1}{x}\right) - i \pi \delta_0$
(C'est l'identité de Sokhotski-Plemelj).

**Correction Détaillée :**
Séparons la partie réelle et la partie imaginaire de $f_\epsilon$ :
$\frac{1}{x + i\epsilon} = \frac{x - i\epsilon}{x^2 + \epsilon^2} = \frac{x}{x^2 + \epsilon^2} - i \frac{\epsilon}{x^2 + \epsilon^2}$
Soit $\phi \in \mathcal{D}(\mathbb{R})$.
Partie imaginaire : $-\int_{-\infty}^{+\infty} \frac{\epsilon}{x^2 + \epsilon^2} \phi(x) dx$.
On reconnaît une approximation de l'identité proportionnelle au noyau de Poisson (cf. Ex 5).
Posons $y = x/\epsilon$. L'intégrale devient $-\int_{-\infty}^{+\infty} \frac{\epsilon}{\epsilon^2 y^2 + \epsilon^2} \phi(\epsilon y) \epsilon dy = - \int_{-\infty}^{+\infty} \frac{1}{y^2 + 1} \phi(\epsilon y) dy$.
Par convergence dominée (la fonction est dominée par $C/(1+y^2)$ et $\phi(\epsilon y) \to \phi(0)$), l'intégrale tend vers $-\int_{-\infty}^{+\infty} \frac{1}{y^2+1} \phi(0) dy = -\pi \phi(0) = \langle -i\pi \delta_0, \phi \rangle$.
Partie réelle : $\int_{-\infty}^{+\infty} \frac{x}{x^2 + \epsilon^2} \phi(x) dx$.
Le terme $\frac{x}{x^2 + \epsilon^2}$ est impair. On peut donc injecter $\phi(0)$ en remarquant que son intégrale avec une fonction impaire sur un domaine symétrique est nulle :
$\int_{-\infty}^{+\infty} \frac{x}{x^2 + \epsilon^2} (\phi(x) - \phi(0)) dx$.
La fonction $\psi(x) = (\phi(x)-\phi(0))/x$ est lisse et à support compact (prolongeable en 0).
L'intégrale s'écrit $\int_{-\infty}^{+\infty} \frac{x^2}{x^2+\epsilon^2} \psi(x) dx$.
Quand $\epsilon \to 0^+$, l'intégrande converge vers $\psi(x)$ presque partout et est dominé.
La limite est donc $\int_{-\infty}^{+\infty} \psi(x) dx = \int_{-\infty}^{+\infty} \frac{\phi(x)-\phi(0)}{x} dx$, qui est l'expression équivalente de $\text{vp}(1/x)$ démontrée dans l'exercice 7.
La combinaison des deux parties donne la relation de Sokhotski-Plemelj. $\blacksquare$
