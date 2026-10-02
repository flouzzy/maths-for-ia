# Exercice 2 : La fonction Signe

\subsection*{Exercice 2 : La fonction Signe \quad $\bigstar\bigstar\star\star\star$}

**Énoncé :**
Soit $\text{sgn}(x) = 1$ si $x > 0$, $-1$ si $x < 0$ et $0$ si $x = 0$. Expliciter la distribution associée $T_{\text{sgn}}$. L'exprimer en fonction de la distribution de Heaviside $T_H$.

**Démonstration pas à pas :**
1. **Intégrabilité locale :** La fonction signe est bornée par 1, donc localement intégrable.
2. **Action sur $\phi$ :** Pour $\phi \in \mathcal{D}(\mathbb{R})$ :
   $$ \langle T_{\text{sgn}}, \phi \rangle = \int_{-\infty}^{0} (-1)\phi(x) dx + \int_{0}^{+\infty} (1)\phi(x) dx $$
3. **Lien avec $H$ :** On remarque que $\text{sgn}(x) = 2H(x) - 1$ pour tout $x \ne 0$ (qui est de mesure de Lebesgue nulle).
   L'action devient donc :
   $$ \langle T_{\text{sgn}}, \phi \rangle = \int_{-\infty}^{+\infty} (2H(x) - 1)\phi(x) dx = 2\langle T_H, \phi \rangle - \int_{-\infty}^{+\infty} \phi(x) dx $$
   On reconnait l'action de la distribution constante égale à 1 : $\langle T_1, \phi \rangle = \int \phi(x) dx$.
   Donc $T_{\text{sgn}} = 2T_H - T_1$. $\blacksquare$
