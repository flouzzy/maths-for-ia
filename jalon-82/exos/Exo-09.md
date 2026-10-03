\subsection*{Exercice 9 : Translater une distribution \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

**Énoncé :**
Soit la distribution $T$ et un réel $b$. Définir rigoureusement la distribution translatée $\tau_b T$ et vérifier que $\tau_b \delta_0 = \delta_b$.

**Correction :**
Si $f$ est une fonction localement intégrable, sa translatée est $f(x-b)$. L'action de la distribution régulière associée est :
$$\langle T_{f(\cdot - b)}, \phi \rangle = \int_{-\infty}^{+\infty} f(x-b) \phi(x) dx$$
Faisons le changement de variable $y = x - b \implies x = y + b, dx = dy$.
$$\langle T_{f(\cdot - b)}, \phi \rangle = \int_{-\infty}^{+\infty} f(y) \phi(y+b) dy = \langle T_f, \phi(\cdot + b) \rangle$$
On utilise cette propriété pour définir la translation de n'importe quelle distribution. On définit la distribution $\tau_b T$ par :
$$\langle \tau_b T, \phi \rangle = \langle T, \tau_{-b} \phi \rangle = \langle T, x \mapsto \phi(x+b) \rangle$$
Appliquons cette définition à la distribution de Dirac en $0$, $\delta_0$.
$$\langle \tau_b \delta_0, \phi \rangle = \langle \delta_0, x \mapsto \phi(x+b) \rangle$$
L'action de $\delta_0$ est d'évaluer la fonction test en $x=0$ :
$$= \phi(0+b) = \phi(b)$$
Or, $\phi(b)$ est exactement la définition de l'action de $\delta_b$ sur $\phi$.
$$\langle \tau_b \delta_0, \phi \rangle = \langle \delta_b, \phi \rangle$$
L'égalité est vraie pour toute fonction $\phi$, d'où $\tau_b \delta_0 = \delta_b$.
