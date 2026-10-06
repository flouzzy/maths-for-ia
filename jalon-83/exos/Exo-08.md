# Exercice 8 : Dérivée de la valeur principale  \quad $\bigstar\bigstar\bigstar\bigstar\star$


## Énoncé
On définit la distribution $\text{vp}\left(\frac{1}{x}\right)$ (Valeur Principale de Cauchy) pour toute $\phi \in \mathcal{D}(\mathbb{R})$ par :
$$ \langle \text{vp}\left(\frac{1}{x}\right), \phi \rangle = \lim_{\epsilon \to 0^+} \int_{|x|>\epsilon} \frac{\phi(x)}{x} dx $$
Montrer que la dérivée au sens des distributions de la fonction $f(x) = \ln|x|$ (qui est localement intégrable) est exactement $\text{vp}\left(\frac{1}{x}\right)$.

## Correction
Soit $\phi \in \mathcal{D}(\mathbb{R})$.
Par définition de la dérivée distributionnelle :
$$ \langle (\ln|x|)', \phi \rangle = - \langle \ln|x|, \phi' \rangle = - \int_{\mathbb{R}} \ln|x| \phi'(x) dx $$
L'intégrale est convergente car $\ln|x|$ est localement intégrable et $\phi'$ est à support compact.
On peut l'écrire comme une limite :
$$ - \lim_{\epsilon \to 0^+} \left( \int_{-\infty}^{-\epsilon} \ln(-x) \phi'(x) dx + \int_{\epsilon}^{+\infty} \ln(x) \phi'(x) dx \right) $$
Appliquons une intégration par parties sur chaque morceau.
Pour l'intégrale sur $]\epsilon, +\infty[$ :
$$ \int_{\epsilon}^{+\infty} \ln(x) \phi'(x) dx = [\ln(x)\phi(x)]_{\epsilon}^{+\infty} - \int_{\epsilon}^{+\infty} \frac{1}{x} \phi(x) dx $$
$$ = 0 - \ln(\epsilon)\phi(\epsilon) - \int_{\epsilon}^{+\infty} \frac{\phi(x)}{x} dx $$
Pour l'intégrale sur $]-\infty, -\epsilon[$ :
$$ \int_{-\infty}^{-\epsilon} \ln(-x) \phi'(x) dx = [\ln(-x)\phi(x)]_{-\infty}^{-\epsilon} - \int_{-\infty}^{-\epsilon} \frac{-1}{-x} \phi(x) dx $$
$$ = \ln(\epsilon)\phi(-\epsilon) - 0 - \int_{-\infty}^{-\epsilon} \frac{\phi(x)}{x} dx $$

En sommant les deux contributions avec le signe moins de départ :
$$ \langle (\ln|x|)', \phi \rangle = - \lim_{\epsilon \to 0^+} \left( \ln(\epsilon)\phi(-\epsilon) - \ln(\epsilon)\phi(\epsilon) - \int_{|x|>\epsilon} \frac{\phi(x)}{x} dx \right) $$
$$ = \lim_{\epsilon \to 0^+} \left( \ln(\epsilon)(\phi(\epsilon) - \phi(-\epsilon)) + \int_{|x|>\epsilon} \frac{\phi(x)}{x} dx \right) $$
Or, comme $\phi$ est différentiable en $0$ (car $C^\infty$), par la formule de Taylor :
$\phi(\epsilon) - \phi(-\epsilon) \approx 2\epsilon \phi'(0)$ pour $\epsilon$ petit.
Donc le terme $\ln(\epsilon)(\phi(\epsilon) - \phi(-\epsilon)) \sim 2\epsilon \ln(\epsilon) \phi'(0)$.
Or $\lim_{\epsilon \to 0^+} \epsilon \ln(\epsilon) = 0$.
Ainsi, le terme de bord disparaît à la limite.
Il reste :
$$ \langle (\ln|x|)', \phi \rangle = \lim_{\epsilon \to 0^+} \int_{|x|>\epsilon} \frac{\phi(x)}{x} dx = \langle \text{vp}\left(\frac{1}{x}\right), \phi \rangle $$
Ce qui démontre rigoureusement le résultat escompté.
