# Exercice 7 : Cas d'égalité dans l'inégalité de Hölder

**Difficulté :** ★★★★☆


## Énoncé
Soient $p, q \in ]1, \infty[$ des exposants conjugués. Déterminer les conditions nécessaires et suffisantes sur $f \in L^p$ et $g \in L^q$ pour que $\|fg\|_1 = \|f\|_p \|g\|_q$.

## Correction Détaillée
La preuve de l'inégalité de Hölder repose fondamentalement sur le lemme de Young. Pour que l'inégalité globale soit une égalité, l'inégalité ponctuelle de Young doit être une égalité presque partout (p.p.).
Rappelons que pour les fonctions normalisées $u = |f|/\|f\|_p$ et $v = |g|/\|g\|_q$, l'égalité dans le lemme de Young $uv = \frac{u^p}{p} + \frac{v^q}{q}$ a lieu si et seulement si $u^p = v^q$.
En remplaçant $u$ et $v$ par leurs expressions :
$$ \frac{|f(x)|^p}{\|f\|_p^p} = \frac{|g(x)|^q}{\|g\|_q^q} \quad \text{p.p.} $$
Ceci implique qu'il existe une constante $c > 0$ telle que $|f(x)|^p = c |g(x)|^q$ presque partout (avec $c = \|f\|_p^p / \|g\|_q^q$).
De plus, dans la preuve de Hölder, nous avons utilisé l'inégalité ponctuelle $|f(x)g(x)| \le |f(x)||g(x)|$, qui n'est une égalité que si $f(x)g(x)$ a un argument (un signe) constant p.p. sur le support commun.
En résumé, l'égalité dans Hölder se produit si et seulement si :
1. $|f|^p$ et $|g|^q$ sont proportionnelles presque partout.
2. $\text{sgn}(f(x)g(x))$ est constant presque partout où le produit est non nul.
