\subsection*{Exercice 8 : Distribution issue du logarithme \quad $\bigstar\bigstar\bigstar\bigstar\star$}

On note $f(x) = \ln|x|$.
1. Montrer que $f \in L^1_{loc}(\mathbb{R})$. En déduire que $T_f$ est une distribution.
2. (Préparation au jalon suivant) Si l'on calculait formellement $\langle T_f', \phi \rangle = - \langle T_f, \phi' \rangle$, quelle distribution singulière reconnaîtrait-on ?

**Correction Détaillée :**
1. La fonction logarithme est mesurable. Son seul point de singularité est $0$. Étudions l'intégrabilité locale en $0$.
Il s'agit de voir si l'intégrale $\int_{-\epsilon}^{\epsilon} |\ln|x|| dx$ converge pour $\epsilon > 0$.
Par symétrie, l'intégrale vaut $2 \int_0^{\epsilon} (-\ln(x)) dx$.
Une primitive de $\ln(x)$ est $x \ln(x) - x$.
En évaluant de $\delta > 0$ à $\epsilon$ puis en passant à la limite $\delta \to 0^+$ :
$\lim_{\delta \to 0^+} [\delta \ln(\delta) - \delta] = 0$. (Croissance comparée usuelle).
L'intégrale vaut donc $2(\epsilon - \epsilon\ln(\epsilon))$, ce qui est fini.
Ainsi, $f$ est localement intégrable et $T_f$ est une distribution bien définie (régulière).
2. Calculons $-\langle T_f, \phi' \rangle$ :
$-\langle T_f, \phi' \rangle = - \int_{-\infty}^{+\infty} \ln|x| \phi'(x) dx = - \lim_{\epsilon \to 0^+} \left( \int_{-\infty}^{-\epsilon} \ln(-x) \phi'(x) dx + \int_{\epsilon}^{+\infty} \ln(x) \phi'(x) dx \right)$
Intégrons par parties sur les domaines ne contenant pas 0. Le terme de bord à l'infini s'annule car $\phi$ est à support compact.
$- \left[ \ln(-x)\phi(x) \right]_{-\infty}^{-\epsilon} + \int_{-\infty}^{-\epsilon} \frac{\phi(x)}{x} dx - \left[ \ln(x)\phi(x) \right]_{\epsilon}^{+\infty} + \int_{\epsilon}^{+\infty} \frac{\phi(x)}{x} dx$
$- \ln(\epsilon)\phi(-\epsilon) + \ln(\epsilon)\phi(\epsilon) + \int_{|x| > \epsilon} \frac{\phi(x)}{x} dx$
Le terme de bord s'écrit $\ln(\epsilon)(\phi(\epsilon) - \phi(-\epsilon))$. Or $\phi(\epsilon) - \phi(-\epsilon) \sim 2\epsilon \phi'(0)$ quand $\epsilon \to 0$.
Donc $\ln(\epsilon) \times 2\epsilon \phi'(0) \to 0$ par croissance comparée.
Il reste l'intégrale, qui, à la limite, n'est autre que la définition de la valeur principale.
On trouve ainsi formellement que la dérivée du logarithme au sens des distributions est $\text{vp}(1/x)$. $\blacksquare$
