# Exercice 10 : Résolution de l'équation $-u'' = \delta_0$  \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$


## Énoncé
Dans le cadre de l'électrostatique (ou de la corde vibrante), le potentiel (ou le déplacement) $u$ créé par une charge ponctuelle (ou une force concentrée) à l'origine satisfait l'équation différentielle au sens des distributions :
$$ -u'' = \delta_0 $$
Trouver la solution générale de cette équation dans $\mathcal{D}'(\mathbb{R})$.

## Correction
On cherche $u \in \mathcal{D}'(\mathbb{R})$ telle que $u'' = -\delta_0$.
Soit $H$ la fonction de Heaviside. On sait que $H' = \delta_0$ (Exercice 1 ou démonstration du cours).
Donc l'équation s'écrit :
$$ u'' = -H' $$
Ceci implique que $(u' + H)' = 0$.
D'après l'exercice 6, la dérivée d'une distribution est nulle si et seulement si cette distribution est constante.
Il existe donc une constante $A \in \mathbb{R}$ telle que :
$$ u' + H = A \implies u' = -H + A $$
On cherche maintenant $u$.
Trouvons une primitive de $H$. La fonction rampe définie par $R(x) = x \mathbf{1}_{x>0}$ (ou $R(x) = \max(0,x)$, la fonction ReLU) a pour dérivée faible $H(x)$.
En effet, pour $x>0$, $R'(x)=1$, et pour $x<0$, $R'(x)=0$, avec $R$ continue en 0 (pas de saut). Donc $R' = H$.
L'équation devient :
$$ u' = -R' + A $$
Soit $(u + R - Ax)' = 0$.
De nouveau, cela implique qu'il existe une constante $B \in \mathbb{R}$ telle que :
$$ u + R - Ax = B $$
Ainsi, la solution générale est :
$$ u(x) = -R(x) + Ax + B = -x \mathbf{1}_{x>0} + Ax + B $$
En termes physiques, $u(x)$ est une fonction affine par morceaux. La "pointe" de la fonction en $x=0$ traduit l'action de la source ponctuelle (le Dirac).
