# Exercice 2 : Famille d'Opérateurs Intégraux
$\bigstar\star\star\star\star$
**Énoncé :**
Soit $E = \mathcal{C}([0,1], \mathbb{R})$ muni de la norme $\|f\|_{\infty} = \sup_{t \in [0,1]} |f(t)|$.
Soit $(k_n)_{n \in \mathbb{N}}$ une suite de fonctions continues de $[0,1]$ dans $\mathbb{R}$.
Pour tout $n$, on définit $T_n : E \to \mathbb{R}$ par $T_n(f) = \int_0^1 k_n(t) f(t) dt$.
Montrer que si $\forall f \in E, \sup_n |T_n(f)| < \infty$, alors $\sup_n \int_0^1 |k_n(t)| dt < \infty$.

**Correction :**
1. Chaque $T_n$ est une forme linéaire sur $E$.
2. Montrons la continuité de $T_n$ :
   $|T_n(f)| = \left| \int_0^1 k_n(t) f(t) dt \right| \le \int_0^1 |k_n(t)| |f(t)| dt \le \|f\|_{\infty} \int_0^1 |k_n(t)| dt$.
   Donc $T_n$ est continue, et $\|T_n\| \le \int_0^1 |k_n(t)| dt$.
3. Montrons l'égalité $\|T_n\| = \int_0^1 |k_n(t)| dt$ :
   Pour un $\epsilon > 0$, il existe une fonction continue $g_\epsilon$ approchant la fonction signe de $k_n(t)$, c'est-à-dire telle que $g_\epsilon(t) k_n(t) \approx |k_n(t)|$, avec $\|g_\epsilon\|_{\infty} \le 1$.
   En prenant le sup sur ces fonctions de norme $\le 1$, on obtient exactement $\|T_n\| = \int_0^1 |k_n(t)| dt$.
4. Application du principe de la borne uniforme :
   $E = \mathcal{C}([0,1], \mathbb{R})$ est complet. La famille $(T_n)$ est constituée d'opérateurs linéaires continus ponctuellement bornés.
   Donc par le théorème de Banach-Steinhaus, $\sup_n \|T_n\| < \infty$.
5. Conclusion :
   Puisque $\|T_n\| = \int_0^1 |k_n(t)| dt$, il en résulte que $\sup_n \int_0^1 |k_n(t)| dt < \infty$.