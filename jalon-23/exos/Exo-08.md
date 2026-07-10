# Exercice 8 : Critère de Cauchy-Hadamard

**Énoncé :**
En utilisant la formule de Cauchy-Hadamard, déterminer le rayon de convergence de $\sum_{n=1}^{+\infty} \left(1 + \frac{1}{n}\right)^{n^2} z^n$.

**Démonstration à blanc :**
La formule de Cauchy-Hadamard donne le rayon $R$ via :
$$ \frac{1}{R} = \limsup_{n \to +\infty} \sqrt[n]{|a_n|} $$
Ici, $a_n = \left(1 + \frac{1}{n}\right)^{n^2}$.
Calculons la racine $n$-ième de $|a_n|$ :
$$ \sqrt[n]{|a_n|} = \left( \left(1 + \frac{1}{n}\right)^{n^2} \right)^{1/n} = \left(1 + \frac{1}{n}\right)^{n^2/n} = \left(1 + \frac{1}{n}\right)^n $$
Étudions la limite de cette expression lorsque $n \to +\infty$.
On sait que $\left(1 + \frac{1}{n}\right)^n = \exp\left( n \ln\left(1 + \frac{1}{n}\right) \right)$.
En utilisant le développement limité $\ln(1+u) = u + o(u)$ en $0$ :
$$ n \ln\left(1 + \frac{1}{n}\right) = n \left( \frac{1}{n} + o\left(\frac{1}{n}\right) \right) = 1 + o(1) $$
Ainsi, la limite de $n \ln\left(1 + \frac{1}{n}\right)$ est 1.
Par continuité de l'exponentielle, $\lim_{n \to +\infty} \left(1 + \frac{1}{n}\right)^n = e^1 = e$.
La limite supérieure est en fait une limite classique, d'où $\frac{1}{R} = e$.
Le rayon de convergence est donc $R = \frac{1}{e}$.
