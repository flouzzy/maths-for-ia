# Exercice 7 : Série de Diracs (Peigne de Dirac)

\subsection*{Exercice 7 : Série de Diracs (Peigne de Dirac) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

**Énoncé :**
Montrer que la somme formelle $T = \sum_{k=-\infty}^{+\infty} \delta_k$ définit bien une distribution. Quel est son ordre ?

**Démonstration pas à pas :**
1. **Définition de l'action :** Pour $\phi \in \mathcal{D}(\mathbb{R})$, le support de $\phi$ est compact, disons inclus dans $[-R, R]$.
   La somme devient $\langle T, \phi \rangle = \sum_{k=-\infty}^{+\infty} \phi(k)$.
   Comme $\phi(k) = 0$ pour $|k| > R$, cette somme est en réalité finie, donc elle a un sens et est bien définie.
2. **Linéarité et Continuité :** Soit un compact $K$. Le nombre d'entiers dans $K$ est majoré par la longueur de $K$ plus 1, disons $N_K$.
   $$ |\langle T, \phi \rangle| \le \sum_{k \in K} |\phi(k)| \le N_K \sup_{x \in K} |\phi(x)| $$
   Cette inégalité prouve la continuité séquentielle.
3. **Ordre :** L'inégalité fait intervenir uniquement la borne supérieure de $\phi$ sur le compact $K$ (la dérivée d'ordre 0). L'ordre du peigne de Dirac est donc 0. $\blacksquare$
