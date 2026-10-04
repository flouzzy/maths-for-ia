# Exercice 8 : La Partie Finie d'Hadamard (Ordre supérieur)
Difficulté : $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
L'intégrale $\int_0^\infty \frac{\varphi(x)}{x^{3/2}}dx$ diverge fortement en 0.
Jacques Hadamard a inventé une procédure pour extraire la partie finie d'une telle intégrale divergente.
On définit la distribution $Pf(x_{+}^{-3/2})$ par son action sur $\varphi \in \mathcal{D}(\mathbb{R})$ :
$$ \langle Pf(x_{+}^{-3/2}), \varphi \rangle = \lim_{\epsilon \to 0^+} \left( \int_\epsilon^\infty \frac{\varphi(x)}{x^{3/2}} dx - \frac{2\varphi(0)}{\sqrt{\epsilon}} \right) $$
Démontrez rigoureusement que cette limite existe bien pour toute fonction $\varphi \in \mathcal{D}(\mathbb{R})$. On effectuera une intégration par parties pour s'en convaincre.

**Correction Détaillée :**
1. **Isoler la singularité et intégration par parties :**
   Considérons l'intégrale tronquée sur $[\epsilon, R]$, où le support de $\varphi$ est dans $[-R, R]$.
   $$ I_\epsilon = \int_\epsilon^\infty \frac{\varphi(x)}{x^{3/2}} dx = \int_\epsilon^R x^{-3/2} \varphi(x) dx $$
   Effectuons une intégration par parties formelle.
   On pose : $u(x) = \varphi(x) \implies u'(x) = \varphi'(x)$
   Et : $v'(x) = x^{-3/2} \implies v(x) = \frac{x^{-1/2}}{-1/2} = -2x^{-1/2} = \frac{-2}{\sqrt{x}}$

   La formule d'intégration par parties $\int u v' = [uv] - \int u' v$ donne :
   $$ \int_\epsilon^R x^{-3/2} \varphi(x) dx = \left[ -2\frac{\varphi(x)}{\sqrt{x}} \right]_\epsilon^R - \int_\epsilon^R \left( \frac{-2}{\sqrt{x}} \right) \varphi'(x) dx $$

2. **Évaluation du terme tout intégré :**
   Puisque $\varphi$ est à support compact, pour un $R$ suffisamment grand, $\varphi(R) = 0$.
   Donc la valeur en la borne supérieure est nulle.
   La valeur en la borne inférieure $\epsilon$ est : $-\left( -2\frac{\varphi(\epsilon)}{\sqrt{\epsilon}} \right) = 2\frac{\varphi(\epsilon)}{\sqrt{\epsilon}}$.
   L'égalité devient :
   $$ \int_\epsilon^\infty \frac{\varphi(x)}{x^{3/2}} dx = \frac{2\varphi(\epsilon)}{\sqrt{\epsilon}} + 2\int_\epsilon^\infty \frac{\varphi'(x)}{\sqrt{x}} dx $$

3. **Réinjection dans l'expression de la définition :**
   Remplaçons cette forme dans la définition d'Hadamard de la Partie Finie :
   $$ \text{Expression} = \left( \frac{2\varphi(\epsilon)}{\sqrt{\epsilon}} + 2\int_\epsilon^\infty \frac{\varphi'(x)}{\sqrt{x}} dx \right) - \frac{2\varphi(0)}{\sqrt{\epsilon}} $$
   $$ \text{Expression} = \frac{2(\varphi(\epsilon) - \varphi(0))}{\sqrt{\epsilon}} + 2\int_\epsilon^\infty \frac{\varphi'(x)}{\sqrt{x}} dx $$

4. **Passage à la limite $\epsilon \to 0^+$ :**
   Analysons les deux termes séparément.
   *   **Le terme de bord :** D'après le théorème des accroissements finis, $\varphi(\epsilon) - \varphi(0) = \epsilon \varphi'(c_\epsilon)$ avec $0 < c_\epsilon < \epsilon$.
       Donc $\frac{2(\varphi(\epsilon) - \varphi(0))}{\sqrt{\epsilon}} = \frac{2\epsilon \varphi'(c_\epsilon)}{\sqrt{\epsilon}} = 2\sqrt{\epsilon}\varphi'(c_\epsilon)$.
       Comme $\varphi'$ est bornée sur le compact, ce terme tend vers $2 \cdot 0 \cdot \varphi'(0) = 0$ quand $\epsilon \to 0$.
   *   **Le terme intégral :** La fonction intégrande est $\frac{\varphi'(x)}{\sqrt{x}}$.
       Au voisinage de 0, elle se comporte comme $\frac{constante}{x^{1/2}}$. C'est une intégrale de Riemann convergente (car $1/2 < 1$).
       L'intégrale généralisée $\int_0^\infty \frac{\varphi'(x)}{\sqrt{x}} dx$ est donc parfaitement définie et convergente.

5. **Conclusion :**
   La limite existe bien et vaut :
   $$ \langle Pf(x_{+}^{-3/2}), \varphi \rangle = 2\int_0^\infty \frac{\varphi'(x)}{\sqrt{x}} dx $$
   La procédure de soustraction divergente de Hadamard a mathématiquement "soigné" la singularité forte d'ordre 3/2 en la ramenant à une singularité intégrable d'ordre 1/2 en faisant peser le poids de la dérivation sur la fonction test.
