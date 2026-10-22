# Exercice 6

**Difficulté :** $\star\star\star\☆☆$

**Énoncé :**
Soit $E$ un espace normé et $a \in E$ un vecteur non nul. On définit la forme linéaire $f : \mathbb{K} \to E$ par $f(\lambda) = \lambda a$. Montrer que $f$ est continue et calculer sa norme d'opérateur $\|f\|_{\mathcal{L}(\mathbb{K}, E)}$.

**Correction Détaillée :**
1. **Continuité :** Pour tout scalaire $\lambda \in \mathbb{K}$ muni de la valeur absolue usuelle $|\lambda|$ (qui est sa norme) :
   $$ \|f(\lambda)\|_E = \|\lambda a\|_E = |\lambda| \|a\|_E. $$
2. On a donc $\|f(\lambda)\|_E \le C |\lambda|$ avec la constante $C = \|a\|_E$. L'opérateur est donc continu.
3. **Calcul de la norme :** Par définition de la norme d'opérateur :
   $$ \|f\| = \sup_{\lambda \neq 0} \frac{\|f(\lambda)\|_E}{|\lambda|} = \sup_{\lambda \neq 0} \frac{|\lambda| \|a\|_E}{|\lambda|} = \sup_{\lambda \neq 0} \|a\|_E = \|a\|_E. $$
4. La norme de l'opérateur est exactement la norme du vecteur $a$.
