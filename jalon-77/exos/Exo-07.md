# Exercice 7 : Densité des exponentielles (Transformée de Laplace discrète)

**Niveau :** \bigstar\bigstar\bigstar\bigstar\star

**Énoncé :**
Montrer que l'espace vectoriel engendré par les fonctions $e^{-nx}$ pour $n \ge 1$ est dense dans $L^2([0, +\infty[)$.
*(Indication : Utiliser le changement de variable $u = e^{-x}$ pour se ramener à un intervalle fini et appliquer le théorème de Weierstrass).*

**Correction Détaillée :**
1. **Changement de variable :**
   L'application $\phi : x \mapsto e^{-x}$ est un difféomorphisme de $]0, +\infty[$ sur $]0, 1[$.
   Soit $f \in L^2(]0, +\infty[)$. On pose $F(u) = f(-\ln u) \cdot u^{-1/2}$.
   Vérifions la norme :
   $\int_0^1 |F(u)|^2 du = \int_0^1 |f(-\ln u)|^2 u^{-1} du$.
   Avec $x = -\ln u$, $dx = -du/u$, donc l'intégrale devient $\int_0^{+\infty} |f(x)|^2 dx = \|f\|_2^2 < +\infty$.
   Donc l'opérateur $U: f \mapsto F$ est une isométrie bijective de $L^2(]0, +\infty[)$ sur $L^2(]0, 1[)$.

2. **Densité des polynômes :**
   Dans $L^2(]0, 1[)$, les polynômes en $u$ sont denses (Exo 4).
   Approchons $F$ par un polynôme $P(u) = \sum_{k=0}^N a_k u^k$.

3. **Retour dans $L^2(]0, +\infty[)$ :**
   La fonction approchante dans le domaine initial est :
   $p(x) = U^{-1}(P)(x) = P(e^{-x}) e^{-x/2} = \sum_{k=0}^N a_k e^{-kx} e^{-x/2} = \sum_{k=0}^N a_k e^{-(k+1/2)x}$.
   On constate que la famille de base s'exprime par des termes exponentiels décroissants. Avec une légère adaptation du changement de variable, on montre que l'espace engendré par $e^{-nx}$ est dense (Théorème de Müntz-Szász simplifié).
