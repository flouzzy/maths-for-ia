# Exercice 8 : L'inégalité de log-Somme $\quad \bigstar\bigstar\bigstar\bigstar\bigstar$

\textbf{Énoncé :}
Soient $a_1, ..., a_n$ et $b_1, ..., b_n$ des nombres strictement positifs.
Prouver l'inégalité de log-somme : $\sum a_i \ln\left(\frac{a_i}{b_i}\right) \ge \left(\sum a_i\right) \ln\left( \frac{\sum a_i}{\sum b_i} \right)$.

\textbf{Correction :}
On pose $f(x) = x \ln(x)$. $f''(x) = 1/x > 0$, donc $f$ est strictement convexe sur $\mathbb{R}^{+*}$.
Posons $\alpha_i = \frac{b_i}{\sum b_j}$ (ce sont des probabilités, $\sum \alpha_i = 1$).
Posons $x_i = \frac{a_i}{b_i}$.
Par l'inégalité de Jensen discrète : $\sum \alpha_i f(x_i) \ge f(\sum \alpha_i x_i)$.
Calculons $\sum \alpha_i x_i = \sum \frac{b_i}{\sum b_j} \frac{a_i}{b_i} = \frac{\sum a_i}{\sum b_i}$.
Donc $f(\sum \alpha_i x_i) = \frac{\sum a_i}{\sum b_i} \ln\left( \frac{\sum a_i}{\sum b_i} \right)$.
Calculons $\sum \alpha_i f(x_i) = \sum \frac{b_i}{\sum b_j} \frac{a_i}{b_i} \ln\left(\frac{a_i}{b_i}\right) = \frac{1}{\sum b_j} \sum a_i \ln\left(\frac{a_i}{b_i}\right)$.
En réinjectant dans l'inégalité, et en multipliant par $\sum b_j$ :
$\sum a_i \ln\left(\frac{a_i}{b_i}\right) \ge \left(\sum a_i\right) \ln\left( \frac{\sum a_i}{\sum b_i} \right)$.
