# Exercice 10 : Application : Processus markoviens de décision (Bellman optimal)
**Niveau :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
On étudie l'opérateur d'optimalité de Bellman $\mathcal{B} : \mathbb{R}^S \to \mathbb{R}^S$ défini par $(\mathcal{B}V)(s) = \max_a \sum_{s'} P(s'|s,a)[R(s,a,s') + \gamma V(s')]$ avec $\gamma \in (0, 1)$.
Montrer qu'il est $\gamma$-contractant pour la norme $\|\cdot\|_\infty$.

**Démonstration pas à pas :**
1. Fixons $s \in S$. Soit $V, U$ deux vecteurs. Sans perte de généralité, supposons $(\mathcal{B}V)(s) \ge (\mathcal{B}U)(s)$.
2. Soit $a^*$ l'action maximisant $\mathcal{B}V$ en $s$. On a $(\mathcal{B}V)(s) = \sum P(s'|s,a^*)[R + \gamma V(s')]$.
3. On a $(\mathcal{B}U)(s) \ge \sum P(s'|s,a^*)[R + \gamma U(s')]$ (car l'action $a^*$ n'est pas forcément optimale pour $U$, mais l'inégalité est large par définition du max).
4. Soustrayons :
   $0 \leq (\mathcal{B}V)(s) - (\mathcal{B}U)(s) \leq \sum P(s'|s,a^*) \gamma (V(s') - U(s'))$.
5. On majore trivialement $V(s') - U(s')$ par la norme infinie $\|V - U\|_\infty$.
6. L'opérateur probabiliste somme à 1 sur $s'$, donc $\sum P(s'|s,a^*) = 1$.
7. Ainsi, $|(\mathcal{B}V)(s) - (\mathcal{B}U)(s)| \leq \gamma \|V - U\|_\infty$.
8. En prenant le supremum sur $s$, on a $\|\mathcal{B}V - \mathcal{B}U\|_\infty \leq \gamma \|V - U\|_\infty$.
   Comme $\mathbb{R}^S$ muni de la norme uniforme est complet et $\gamma < 1$, l'opérateur de Bellman possède un unique point fixe, la fonction de valeur optimale, atteinte de façon géométrique par Value Iteration.
