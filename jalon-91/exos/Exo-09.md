# Exercice 9 : Dimension VC et Bornes PAC de Hoeffding

$\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
En apprentissage statistique, on évalue un classifieur binaire $h$ sur $n$ données. L'erreur empirique est $\hat{R}(h) = \frac{1}{n} \sum_{i=1}^n \mathbf{1}_{h(X_i) \neq Y_i}$, et l'erreur de généralisation (vraie) est $R(h) = \mathbb{P}(h(X) \neq Y)$.
On sait par Hoeffding que pour un classifieur fixé, $\mathbb{P}(|\hat{R}(h) - R(h)| \ge \epsilon) \le 2\exp(-2n\epsilon^2)$.
Soit $\mathcal{H}$ un espace d'hypothèses de taille finie $|\mathcal{H}|$.
En utilisant la borne de l'union (Boole), montrer que pour garantir que l'erreur entre $\hat{R}(h)$ et $R(h)$ pour **tous** les classifieurs de $\mathcal{H}$ soit strictement inférieure à $\epsilon$ avec une probabilité au moins $1 - \delta$, il suffit d'avoir :
$$ n \ge \frac{1}{2\epsilon^2} \ln\left(\frac{2|\mathcal{H}|}{\delta}\right) $$

**Correction :**
Nous voulons borner la probabilité de l'événement indésirable ("bad event") : au moins un classifieur $h \in \mathcal{H}$ s'écarte de plus de $\epsilon$ entre son erreur empirique et son erreur réelle.
Soit cet événement $A = \bigcup_{h \in \mathcal{H}} \{ |\hat{R}(h) - R(h)| \ge \epsilon \}$.
Par l'inégalité de Boole (sous-additivité) :
$$ \mathbb{P}(A) = \mathbb{P}\left( \bigcup_{h \in \mathcal{H}} \{ |\hat{R}(h) - R(h)| \ge \epsilon \} \right) \le \sum_{h \in \mathcal{H}} \mathbb{P}(|\hat{R}(h) - R(h)| \ge \epsilon) $$
Chaque terme de la somme se majore par l'inégalité de Hoeffding :
$$ \mathbb{P}(|\hat{R}(h) - R(h)| \ge \epsilon) \le 2\exp(-2n\epsilon^2) $$
Puisque la somme comporte $|\mathcal{H}|$ termes identiques :
$$ \mathbb{P}(A) \le |\mathcal{H}| \times 2\exp(-2n\epsilon^2) $$
Nous voulons que la probabilité de réussite soit au moins $1 - \delta$, ce qui revient à exiger que la probabilité de l'événement indésirable $\mathbb{P}(A)$ soit au plus $\delta$ :
$$ 2 |\mathcal{H}| \exp(-2n\epsilon^2) \le \delta $$
Isolons $n$ :
$$ \exp(-2n\epsilon^2) \le \frac{\delta}{2|\mathcal{H}|} $$
En prenant le logarithme népérien des deux côtés :
$$ -2n\epsilon^2 \le \ln\left( \frac{\delta}{2|\mathcal{H}|} \right) $$
Puisque $\ln(1/x) = -\ln(x)$, on obtient :
$$ -2n\epsilon^2 \le -\ln\left( \frac{2|\mathcal{H}|}{\delta} \right) $$
En divisant par $-2\epsilon^2$ (ce qui inverse le sens de l'inégalité) :
$$ n \ge \frac{1}{2\epsilon^2} \ln\left(\frac{2|\mathcal{H}|}{\delta}\right) $$
La démonstration est terminée. Cela illustre comment la taille de l'espace des modèles impacte logarithmiquement la quantité de données $n$ requise pour apprendre.
