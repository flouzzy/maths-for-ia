---
uuid: "jalon-40-exo-03"
title: "Exercice 3 : Calcul par dérivation paramétrique (Intégrale de Dirichlet)"
difficulty: "$\star\star\star\circ\circ$"
---

# Exercice 3 : Calcul par dérivation paramétrique (Intégrale de Dirichlet) ($\star\star\star\circ\circ$)

On pose $F(x) = \int_0^{+\infty} \frac{\sin(t)}{t} e^{-xt} \, \mathrm{d}t$ pour $x > 0$.

1. Prouver que $F$ est dérivable sur $]0, +\infty[$.
2. Calculer $F'(x)$ explicitement.
3. En déduire la valeur de $F(x)$.
4. (Admis: prolongement par continuité en 0) En déduire $\int_0^{+\infty} \frac{\sin(t)}{t} \mathrm{d}t$.

**Correction détaillée :**
1. **Dérivabilité :** Soit $f(x,t) = \frac{\sin(t)}{t} e^{-xt}$. $\frac{\partial f}{\partial x}(x,t) = -\sin(t) e^{-xt}$.
   Pour un compact $[a, +\infty[$ avec $a > 0$, $|\frac{\partial f}{\partial x}(x,t)| = |\sin(t)| e^{-xt} \leq e^{-at}$. La fonction $\psi(t) = e^{-at}$ est intégrable sur $[0, +\infty[$. D'où la classe $\mathcal{C}^1$ sur $]0, +\infty[$.
2. **Calcul :** $F'(x) = -\int_0^{+\infty} \sin(t) e^{-xt} \, \mathrm{d}t$. Intégrons par parties deux fois ou utilisons la partie imaginaire de $e^{(i-x)t}$ :
   $\int_0^{+\infty} e^{(-x+i)t} \, \mathrm{d}t = \left[ \frac{e^{(-x+i)t}}{-x+i} \right]_0^{+\infty} = 0 - \frac{1}{-x+i} = \frac{x+i}{x^2+1}$. La partie imaginaire est $\frac{1}{x^2+1}$. Donc $F'(x) = -\frac{1}{x^2+1}$.
3. **Valeur de F :** Par intégration usuelle, $F(x) = -\arctan(x) + C$. Pour déterminer $C$, on cherche la limite quand $x \to +\infty$. Comme $|F(x)| \leq \int_0^{+\infty} e^{-xt} \mathrm{d}t = \frac{1}{x} \to 0$, $F(x) \to 0$. De plus, $-\arctan(x) \to -\frac{\pi}{2}$. Donc $C = \frac{\pi}{2}$.
   $F(x) = \frac{\pi}{2} - \arctan(x)$.
4. En prolongeant par continuité en $x=0$, $F(0) = \frac{\pi}{2}$, soit $\int_0^{+\infty} \frac{\sin(t)}{t} \mathrm{d}t = \frac{\pi}{2}$.
