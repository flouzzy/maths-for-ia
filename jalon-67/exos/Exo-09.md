# Exercice 9 : Limite d'une suite impliquant le binôme de Newton
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

### Énoncé

Soit $I_n = \int_0^1 n \left(1 - x^n\right) \ln(1/x) dx$. Montrer que $\lim_{n \to \infty} I_n = +\infty$. (Indication : on ne peut pas utiliser la convergence dominée ici).

---
### Correction détaillée

1. Posons $f_n(x) = n \left(1 - x^n\right) \ln(1/x)$. Les fonctions sont positives sur $]0, 1[$.
2. Étudions la monotonie de la suite $(f_n)$. Considérons la fonction $g(t) = t(1-x^t)$ pour $t \in \mathbb{R}^+$ (ici $t$ remplace $n$, à $x \in ]0, 1[$ fixé).
   Dérivons par rapport à $t$ : $g'(t) = (1-x^t) + t(-x^t \ln x) = 1 - x^t(1 + t\ln x)$.
   Posons $h(t) = x^t(1 + t\ln x)$. A-t-on $h(t) \le 1$ ?
   L'inégalité $e^u \ge 1 + u$ (pour tout $u \in \mathbb{R}$) appliquée à $u = -t\ln(x) > 0$ donne $e^{-t\ln x} \ge 1 - t\ln x$, soit $x^{-t} \ge 1 - t\ln x$. En multipliant par $x^t > 0$, on obtient $1 \ge x^t(1 - t\ln x)$. Attendez, il y a une subtilité de signe (ici $x<1$ donc $\ln x < 0$).
   Une analyse plus fine (ou la formule $1-x^n = (1-x)(1+x+...+x^{n-1})$) montre que la fonction $n \mapsto n(1-x^n)$ n'est pas trivialement monotone pour tout $x$.
   Essayons une autre approche.
3. Calculons explicitement $I_n$ car les intégrales sont calculables.
   $$I_n = n \int_0^1 (1 - x^n) (-\ln x) dx$$
   Par linéarité : $I_n = n \int_0^1 (-\ln x) dx - n \int_0^1 x^n (-\ln x) dx$.
   On sait que $\int_0^1 (-\ln x) dx = 1$.
   Calculons $\int_0^1 -x^n \ln x dx$ par IPP : on l'a fait dans l'exercice précédent, cela vaut $\frac{1}{(n+1)^2}$.
   Donc $I_n = n(1 - \frac{1}{(n+1)^2}) = n - \frac{n}{(n+1)^2}$.
4. Lorsque $n \to +\infty$, le terme $n$ diverge vers $+\infty$ et $\frac{n}{(n+1)^2}$ tend vers 0. Donc $\lim_{n \to \infty} I_n = +\infty$.
5. Que se passe-t-il si on applique le TCM ?
   La limite ponctuelle de $f_n(x)$ est $+\infty$ pour tout $x \in ]0, 1[$ car $x^n \to 0$ donc $1-x^n \to 1$, d'où $f_n(x) \sim n \ln(1/x) \to +\infty$.
   L'intégrale de la limite est $\int_0^1 (+\infty) dx = +\infty$.
   La limite des intégrales est aussi $+\infty$. Le TCM (Beppo Levi généralisé) reste cohérent, même si la fonction limite prend des valeurs infinies, tant que la monotonie est globalement respectée ou que la positivité des intégrales maintient la divergence.
