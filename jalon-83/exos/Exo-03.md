---
uuid: jalon-83-exo-03
title: "Exercice 03 - Dérivation des distributions"
---

# Exercice 03 $\bigstar\bigstar\star\star\star$

**Énoncé :**
Sans utiliser la formule des sauts, calculer la dérivée distributionnelle de $f(x) = \ln|x|$ sur $\mathbb{R}$.
1. Vérifier d'abord que $f \in L^1_{loc}(\mathbb{R})$.
2. Pour toute fonction test $\phi \in \mathcal{D}(\mathbb{R})$, évaluer $\langle f', \phi \rangle = - \langle f, \phi' \rangle$ en utilisant l'intégrale de Lebesgue et le passage à la limite (Valeur Principale de Cauchy).
3. Conclure sur l'expression de $f'$.

**Correction pas à pas :**
1. La fonction $\ln|x|$ présente une singularité en 0. Sur un compact $[-R, R]$, l'intégrale $\int_{-R}^R |\ln|x|| dx = 2 \int_0^R (-\ln(x)) dx$ (si $R \le 1$). Une primitive de $-\ln(x)$ est $-x\ln(x) + x$. La limite en 0 est $0$. L'intégrale est donc finie. Ainsi $f \in L^1_{loc}(\mathbb{R})$ et définit une distribution.

2. Soit $\phi \in \mathcal{D}(\mathbb{R})$. Par définition de la dérivée distributionnelle :
$$ \langle f', \phi \rangle = - \int_{\mathbb{R}} \ln|x| \phi'(x) \, dx $$
Comme $\ln|x|$ est singulière en 0, on isole la singularité en introduisant un paramètre $\epsilon > 0$ :
$$ = - \lim_{\epsilon \to 0^+} \left( \int_{-\infty}^{-\epsilon} \ln(-x) \phi'(x) \, dx + \int_{\epsilon}^{+\infty} \ln(x) \phi'(x) \, dx \right) $$
Intégrons par parties sur ces intervalles où la fonction est lisse :
$$ \int_{-\infty}^{-\epsilon} \ln(-x) \phi'(x) \, dx = [\ln(-x)\phi(x)]_{-\infty}^{-\epsilon} - \int_{-\infty}^{-\epsilon} \frac{1}{x} \phi(x) \, dx = \ln(\epsilon)\phi(-\epsilon) - \int_{-\infty}^{-\epsilon} \frac{\phi(x)}{x} \, dx $$
$$ \int_{\epsilon}^{+\infty} \ln(x) \phi'(x) \, dx = [\ln(x)\phi(x)]_{\epsilon}^{+\infty} - \int_{\epsilon}^{+\infty} \frac{1}{x} \phi(x) \, dx = -\ln(\epsilon)\phi(\epsilon) - \int_{\epsilon}^{+\infty} \frac{\phi(x)}{x} \, dx $$
En combinant les deux, on obtient :
$$ \langle f', \phi \rangle = \lim_{\epsilon \to 0^+} \left( \ln(\epsilon) (\phi(\epsilon) - \phi(-\epsilon)) + \int_{|x| > \epsilon} \frac{\phi(x)}{x} \, dx \right) $$
Comme $\phi$ est dérivable en 0, $\phi(\epsilon) - \phi(-\epsilon) \sim 2\epsilon \phi'(0)$.
Donc $\ln(\epsilon) (\phi(\epsilon) - \phi(-\epsilon)) \sim 2\epsilon\ln(\epsilon)\phi'(0)$.
La limite de $2\epsilon\ln(\epsilon)$ quand $\epsilon \to 0^+$ est 0.

3. Il reste donc :
$$ \langle f', \phi \rangle = \lim_{\epsilon \to 0^+} \int_{|x| > \epsilon} \frac{\phi(x)}{x} \, dx $$
C'est par définition l'action de la distribution "Valeur Principale de $1/x$", notée $vp(1/x)$.
On conclut que $(\ln|x|)' = vp(1/x)$ au sens des distributions. $\blacksquare$
