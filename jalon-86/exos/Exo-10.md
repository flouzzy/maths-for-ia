# Exercice 0

## Exercice 10 : Génération de loi par inversion (Théorème fondamental de simulation) $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $F : \mathbb{R} \to [0, 1]$ une fonction de répartition stricte croissante et continue.
Soit $U$ une variable aléatoire suivant une loi uniforme sur $[0, 1]$.
On définit une nouvelle variable aléatoire $X$ par $X = F^{-1}(U)$, où $F^{-1}$ est la fonction réciproque de $F$.
Démontrer que la fonction de répartition de la variable $X$ est exactement $F$.
*C'est le théorème de la transformée inverse, massivement utilisé en IA pour générer n'importe quelle loi à partir d'un générateur pseudo-aléatoire uniforme.*

### Correction pas à pas

1. **Existence de la fonction réciproque**
   Puisque $F$ est continue et strictement croissante, elle est bijective de $\mathbb{R}$ vers $]0, 1[$. Elle admet donc une fonction réciproque $F^{-1} : ]0, 1[ \to \mathbb{R}$ qui est elle-même continue et strictement croissante.
   Puisque $F^{-1}$ est continue, c'est une fonction mesurable. La composition d'une V.A. ($U$) par une fonction mesurable ($F^{-1}$) est bien une variable aléatoire ($X$).

2. **Calcul de la fonction de répartition de $X$**
   Soit $x \in \mathbb{R}$. Par définition de la fonction de répartition de $X$ :
   $F_X(x) = \mathbb{P}(X \leq x)$.
   Substituons $X$ par sa définition :
   $F_X(x) = \mathbb{P}(F^{-1}(U) \leq x)$.

3. **Application de la fonction croissante $F$**
   Puisque la fonction $F$ est strictement croissante, appliquer $F$ aux deux membres d'une inégalité en préserve le sens :
   $a \leq b \iff F(a) \leq F(b)$.
   En appliquant $F$ dans l'événement probabiliste :
   $F^{-1}(U) \leq x \iff F(F^{-1}(U)) \leq F(x) \iff U \leq F(x)$.
   Donc l'événement $\{ F^{-1}(U) \leq x \}$ est strictement identique à l'événement $\{ U \leq F(x) \}$.
   On en déduit :
   $F_X(x) = \mathbb{P}(U \leq F(x))$.

4. **Propriété de la loi uniforme**
   Par hypothèse, $U$ suit une loi uniforme $\mathcal{U}([0, 1])$.
   La fonction de répartition d'une loi uniforme sur $[0, 1]$ pour une valeur $y \in [0, 1]$ est simplement $\mathbb{P}(U \leq y) = y$.
   Ici, la valeur à évaluer est $y = F(x)$. Comme $F$ prend ses valeurs dans $[0, 1]$, on a bien $F(x) \in [0, 1]$.
   Donc, $\mathbb{P}(U \leq F(x)) = F(x)$.

5. **Conclusion**
   On a prouvé que pour tout $x \in \mathbb{R}$, $F_X(x) = F(x)$.
   La variable aléatoire simulée $X$ possède exactement la loi cible désirée.
