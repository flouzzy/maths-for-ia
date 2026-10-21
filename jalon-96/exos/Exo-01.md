Dans le cadre de l'apprentissage automatique, et plus spécifiquement pour l'évaluation de la performance des modèles de langage, il est fondamental de comprendre comment mesurer la divergence entre une distribution de probabilité réelle et celle estimée par un modèle. Cet exercice vous propose d'explorer ces concepts à travers un exemple simplifié de prédiction de mot.

Considérons un vocabulaire très réduit V = \{"le", "chat", "dort"\}. Nous nous intéressons à la prédiction du prochain mot suivant la séquence "Le chat". Après une analyse approfondie d'un corpus linguistique, la *distribution de probabilité réelle* P des mots suivants est établie comme suit :
*   $P(\text{"dort"}) = 0.7$
*   $P(\text{"le"}) = 0.2$
*   $P(\text{"chat"}) = 0.1$

Un modèle de langage, suite à son entraînement initial, produit la *distribution de probabilité prédite* Q pour le même contexte :
*   $Q(\text{"dort"}) = 0.6$
*   $Q(\text{"le"}) = 0.3$
*   $Q(\text{"chat"}) = 0.1$

Nous utiliserons le logarithme naturel (base $e$) pour tous les calculs. Pour faciliter les calculs numériques, nous vous donnerons quelques valeurs approximatives si nécessaire, mais il est attendu que vous montriez toutes les étapes détaillées.

Niveau de difficulté : $\bigstar\star\star\star\star$

\vspace{0.5cm}

\textbf{Partie 1 : Entropie de Shannon (H(P))}

1.1. Rappelez la formule de l'entropie de Shannon pour une variable aléatoire discrète $X$ prenant des valeurs $x_i$ avec des probabilités $P(x_i)$.

1.2. Calculez l'entropie de Shannon de la distribution réelle P, notée $H(P)$. Arrondissez votre résultat final à quatre décimales. Expliquez ce que cette valeur représente dans le contexte de notre scénario.
(Les valeurs numériques utiles : $\ln(0.7) \approx -0.35667$, $\ln(0.2) \approx -1.60944$, $\ln(0.1) \approx -2.30259$)

\vspace{0.5cm}

\textbf{Partie 2 : Entropie Croisée (H(P, Q))}

2.1. Rappelez la formule de l'entropie croisée entre deux distributions de probabilité discrètes P et Q.

2.2. Calculez l'entropie croisée $H(P, Q)$ entre la distribution réelle P et la distribution prédite Q. Arrondissez votre résultat final à quatre décimales. Expliquez ce que cette valeur signifie pour l'évaluation de notre modèle de langage.
(Les valeurs numériques utiles en plus de celles de la Partie 1 : $\ln(0.6) \approx -0.51083$, $\ln(0.3) \approx -1.20397$)

\vspace{0.5cm}

\textbf{Partie 3 : Divergence de Kullback-Leibler (D\textsubscript{KL}(P \textbar\textbar Q))}

3.1. Rappelez la formule de la divergence de Kullback-Leibler (KL) de P par rapport à Q, notée $D_{KL}(P || Q)$.

3.2. Calculez la divergence $D_{KL}(P || Q)$. Arrondissez votre résultat final à quatre décimales.
(Utilisez les mêmes valeurs numériques que précédemment. N'oubliez pas que $\ln(a/b) = \ln(a) - \ln(b)$ peut simplifier les calculs.)

3.3. Vérifiez la relation fondamentale $D_{KL}(P || Q) = H(P, Q) - H(P)$ en utilisant les résultats que vous avez calculés dans les parties précédentes. Commentez brièvement l'exactitude de cette relation dans le cadre de vos calculs numériques approximatifs.

\vspace{0.5cm}

\textbf{Partie 4 : Interprétation et Synthèse}

4.1. Sur la base des valeurs numériques que vous avez obtenues pour $H(P)$, $H(P, Q)$, et $D_{KL}(P || Q)$, décrivez la performance du modèle de langage. Comment l'entropie croisée et la divergence KL nous éclairent-elles sur la qualité de l'alignement entre les prédictions du modèle et la réalité linguistique ?

4.2. Imaginez un modèle de langage "parfait", notons-le $Q^*$, dont la distribution de probabilité prédite est *identique* à la distribution réelle P, c'est-à-dire $Q^* = P$. Sans effectuer de nouveaux calculs détaillés, déterminez quelles seraient les valeurs de $H(P, Q^*)$ et de $D_{KL}(P || Q^*)$. Justifiez votre réponse en vous appuyant sur la signification intrinsèque de ces mesures.

\vspace{2cm}
\noindent\rule{\textwidth}{1pt}
\vspace{0.5cm}

\textbf{Corrigé}

\vspace{0.5cm}

\textbf{Préliminaires et Rappels :}
Les distributions de probabilité données sont :
*   Distribution réelle P : $P(\text{"dort"}) = 0.7$, $P(\text{"le"}) = 0.2$, $P(\text{"chat"}) = 0.1$
*   Distribution prédite Q : $Q(\text{"dort"}) = 0.6$, $Q(\text{"le"}) = 0.3$, $Q(\text{"chat"}) = 0.1$

Les valeurs des logarithmes naturels (arrondies à cinq décimales pour les calculs intermédiaires) :
*   $\ln(0.7) \approx -0.35667$
*   $\ln(0.2) \approx -1.60944$
*   $\ln(0.1) \approx -2.30259$
*   $\ln(0.6) \approx -0.51083$
*   $\ln(0.3) \approx -1.20397$

\vspace{0.5cm}

\textbf{Partie 1 : Entropie de Shannon (H(P))}

\textbf{1.1. Formule de l'entropie de Shannon :}
L'entropie de Shannon $H(X)$ d'une variable aléatoire discrète $X$ qui prend des valeurs $x_i$ avec des probabilités $P(x_i)$ est définie par :
$H(X) = - \sum_{i=1}^{N} P(x_i) \ln(P(x_i))$
où $N$ est le nombre d'issues possibles dans l'espace des événements. Le signe négatif est introduit pour garantir que l'entropie, qui mesure l'information ou l'incertitude, est une valeur positive, car $\ln(P(x_i))$ est toujours négatif ou nul pour $0 < P(x_i) \le 1$.

\textbf{1.2. Calcul de l'entropie de Shannon de la distribution réelle P ($H(P)$) :}
La distribution réelle P pour le prochain mot est :
$P(\text{"dort"}) = 0.7$
$P(\text{"le"}) = 0.2$
$P(\text{"chat"}) = 0.1$

Nous appliquons la formule de l'entropie de Shannon :
$H(P) = - [P(\text{"dort"}) \ln(P(\text{"dort"})) + P(\text{"le"}) \ln(P(\text{"le"})) + P(\text{"chat"}) \ln(P(\text{"chat"}))]$

Substituons les valeurs de probabilité et les valeurs numériques approximatives de $\ln$ :
$H(P) = - [0.7 \times \ln(0.7) + 0.2 \times \ln(0.2) + 0.1 \times \ln(0.1)]$
$H(P) = - [0.7 \times (-0.35667) + 0.2 \times (-1.60944) + 0.1 \times (-2.30259)]$

Effectuons les multiplications :
$0.7 \times (-0.35667) = -0.249669$
$0.2 \times (-1.60944) = -0.321888$
$0.1 \times (-2.30259) = -0.230259$

Ajoutons ces termes :
$H(P) = - [-0.249669 - 0.321888 - 0.230259]$
$H(P) = - [-0.801816]$
$H(P) = 0.801816$

Arrondi à quatre décimales, $H(P) \approx 0.8018$.

\textbf{Interprétation :} L'entropie de Shannon $H(P)$ mesure la quantité moyenne d'information contenue dans la distribution réelle P, ou de manière équivalente, l'incertitude intrinsèque associée à la prédiction du prochain mot si l'on connaissait parfaitement la distribution réelle. Une valeur plus élevée signifierait plus d'incertitude (les probabilités des différents mots seraient plus proches les unes des autres), tandis qu'une valeur plus faible indiquerait moins d'incertitude (une ou plusieurs issues seraient beaucoup plus probables que les autres). Dans notre cas, 0.8018 unités d'information (exprimées en "nats" car nous utilisons le logarithme naturel) représente l'incertitude moyenne sur le mot suivant "Le chat" selon la réalité linguistique observée.

\vspace{0.5cm}

\textbf{Partie 2 : Entropie Croisée (H(P, Q))}

\textbf{2.1. Formule de l'entropie croisée :}
L'entropie croisée $H(P, Q)$ entre deux distributions de probabilité discrètes P (la distribution réelle ou "vraie") et Q (la distribution prédite ou "modèle") est définie par :
$H(P, Q) = - \sum_{i=1}^{N} P(x_i) \ln(Q(x_i))$
Elle mesure la quantité moyenne de bits (ou nats) nécessaire pour identifier un événement tiré de la distribution P si l'on utilise un schéma de codage optimisé pour la distribution Q. Elle quantifie le coût moyen en termes de surprise lorsque l'on observe un événement réel $x_i$ mais que l'on s'attendait à ce qu'il se produise avec la probabilité $Q(x_i)$.

\textbf{2.2. Calcul de l'entropie croisée $H(P, Q)$ :}
Nous utilisons la distribution réelle P :
$P(\text{"dort"}) = 0.7$
$P(\text{"le"}) = 0.2$
$P(\text{"chat"}) = 0.1$

Et la distribution prédite Q :
$Q(\text{"dort"}) = 0.6$
$Q(\text{"le"}) = 0.3$
$Q(\text{"chat"}) = 0.1$

Nous appliquons la formule de l'entropie croisée :
$H(P, Q) = - [P(\text{"dort"}) \ln(Q(\text{"dort"})) + P(\text{"le"}) \ln(Q(\text{"le"})) + P(\text{"chat"}) \ln(Q(\text{"chat"}))]$

Substituons les valeurs de probabilité et les valeurs numériques approximatives de $\ln$ :
$H(P, Q) = - [0.7 \times \ln(0.6) + 0.2 \times \ln(0.3) + 0.1 \times \ln(0.1)]$
$H(P, Q) = - [0.7 \times (-0.51083) + 0.2 \times (-1.20397) + 0.1 \times (-2.30259)]$

Effectuons les multiplications :
$0.7 \times (-0.51083) = -0.357581$
$0.2 \times (-1.20397) = -0.240794$
$0.1 \times (-2.30259) = -0.230259$

Ajoutons ces termes :
$H(P, Q) = - [-0.357581 - 0.240794 - 0.230259]$
$H(P, Q) = - [-0.828634]$
$H(P, Q) = 0.828634$

Arrondi à quatre décimales, $H(P, Q) \approx 0.8286$.

\textbf{Interprétation :} L'entropie croisée $H(P, Q)$ est une mesure clé de la performance du modèle de langage. Elle représente le coût moyen de la prédiction (en nats) lorsque l'on utilise les probabilités du modèle Q pour décrire des événements tirés de la distribution réelle P. Plus la valeur de $H(P, Q)$ est faible, meilleure est la correspondance entre les prédictions du modèle Q et la distribution réelle P, et donc meilleure est la qualité du modèle. Dans notre cas, la valeur de 0.8286 nats est le coût moyen pour "encoder" les mots réels en utilisant l'hypothèse des probabilités du modèle. Il est important de noter que $H(P, Q)$ est toujours supérieur ou égal à $H(P)$. Ici, $H(P, Q) \approx 0.8286$ est légèrement supérieur à $H(P) \approx 0.8018$, ce qui est attendu pour un modèle imparfait.

\vspace{0.5cm}

\textbf{Partie 3 : Divergence de Kullback-Leibler (D\textsubscript{KL}(P \textbar\textbar Q))}

\textbf{3.1. Formule de la divergence de Kullback-Leibler (KL) :}
La divergence de Kullback-Leibler (KL) de P par rapport à Q, notée $D_{KL}(P || Q)$, est définie par :
$D_{KL}(P || Q) = \sum_{i=1}^{N} P(x_i) \ln\left(\frac{P(x_i)}{Q(x_i)}\right)$
Elle quantifie la perte d'information (ou le "gain d'information" de P par rapport à Q) lorsque la distribution Q est utilisée pour approximer la distribution P. Elle mesure "à quel point" la distribution Q est différente de la distribution P. Une valeur de 0 indique que les deux distributions sont identiques.

\textbf{3.2. Calcul de la divergence $D_{KL}(P || Q)$ :}
Nous utilisons la formule directe :
$D_{KL}(P || Q) = P(\text{"dort"}) \ln\left(\frac{P(\text{"dort"})}{Q(\text{"dort"})}\right) + P(\text{"le"}) \ln\left(\frac{P(\text{"le"})}{Q(\text{"le"})}\right) + P(\text{"chat"}) \ln\left(\frac{P(\text{"chat"})}{Q(\text{"chat"})}\right)$

Substituons les valeurs des probabilités :
$D_{KL}(P || Q) = 0.7 \times \ln\left(\frac{0.7}{0.6}\right) + 0.2 \times \ln\left(\frac{0.2}{0.3}\right) + 0.1 \times \ln\left(\frac{0.1}{0.1}\right)$

Simplifions les termes logarithmiques en utilisant la propriété $\ln(a/b) = \ln(a) - \ln(b)$ :
$\ln\left(\frac{0.7}{0.6}\right) = \ln(0.7) - \ln(0.6) \approx (-0.35667) - (-0.51083) = 0.15416$
$\ln\left(\frac{0.2}{0.3}\right) = \ln(0.2) - \ln(0.3) \approx (-1.60944) - (-1.20397) = -0.40547$
$\ln\left(\frac{0.1}{0.1}\right) = \ln(1) = 0$

Maintenant, substituons ces valeurs calculées dans la formule de $D_{KL}(P || Q)$ :
$D_{KL}(P || Q) = 0.7 \times 0.15416 + 0.2 \times (-0.40547) + 0.1 \times 0$

Effectuons les multiplications :
$0.7 \times 0.15416 = 0.107912$
$0.2 \times (-0.40547) = -0.081094$
$0.1 \times 0 = 0$

Ajoutons ces termes :
$D_{KL}(P || Q) = 0.107912 - 0.081094 + 0$
$D_{KL}(P || Q) = 0.026818$

Arrondi à quatre décimales, $D_{KL}(P || Q) \approx 0.0268$.

\textbf{3.3. Vérification de la relation $D_{KL}(P || Q) = H(P, Q) - H(P)$ :}
Nous avons calculé précédemment :
$H(P, Q) \approx 0.828634$
$H(P) \approx 0.801816$

Calculons la différence entre ces deux valeurs :
$H(P, Q) - H(P) = 0.828634 - 0.801816 = 0.026818$

Ce résultat de 0.026818 est *exactement* le même que la valeur que nous avons calculée pour $D_{KL}(P || Q)$ (0.026818) en utilisant la formule directe de la divergence KL avec les valeurs non arrondies des logarithmes.

La relation $D_{KL}(P || Q) = H(P, Q) - H(P)$ est donc parfaitement vérifiée par nos calculs. Cette relation est une propriété fondamentale qui montre que la divergence KL représente l'excès d'information (ou le coût supplémentaire) de l'utilisation de la distribution Q au lieu de la distribution P, par rapport à l'incertitude intrinsèque de la distribution P. Toute variation minime si l'on utilisait les résultats finaux arrondis (0.8286 - 0.8018 = 0.0268) serait uniquement due aux approximations numériques et non à une invalidité de la relation théorique.

\vspace{0.5cm}

\textbf{Partie 4 : Interprétation et Synthèse}

\textbf{4.1. Interprétation de la performance du modèle :}
Nous avons obtenu les valeurs numériques suivantes :
*   Entropie de Shannon de la distribution réelle : $H(P) \approx 0.8018$ nats
*   Entropie croisée entre P et Q : $H(P, Q) \approx 0.8286$ nats
*   Divergence de Kullback-Leibler de P par rapport à Q : $D_{KL}(P || Q) \approx 0.0268$ nats

$H(P)$ représente l'incertitude minimale inhérente à la distribution réelle des mots. C'est la limite inférieure théorique de l'entropie croisée que n'importe quel modèle de langage, même parfait, pourrait atteindre pour cette tâche.
L'entropie croisée $H(P, Q)$ est la mesure la plus directe de la performance de notre modèle de langage. Le fait que $H(P, Q) \approx 0.8286$ soit légèrement supérieur à $H(P) \approx 0.8018$ indique que le modèle Q n'est pas parfait. Il y a un coût supplémentaire (une pénalité) en information lorsque nous utilisons les prédictions de Q au lieu de la distribution réelle P pour caractériser ou "coder" les événements observés.
La divergence KL $D_{KL}(P || Q)$ quantifie précisément cet "excès" d'information ou cette "pénalité". Une valeur de $D_{KL}(P || Q) \approx 0.0268$ nats est une petite valeur positive. Cela signifie que le modèle Q est relativement proche de la distribution réelle P, mais qu'il existe une divergence non nulle. Plus cette valeur serait élevée, plus la distribution du modèle Q s'écarterait de la distribution réelle P, et plus le modèle serait jugé de mauvaise qualité. Une divergence KL nulle serait le signe d'un modèle parfait (Q = P).
En synthèse, le modèle de langage Q n'est pas idéal, car ses prédictions ne sont pas parfaitement alignées avec la réalité linguistique P. Cependant, la faible valeur de la divergence KL indique que l'écart n'est pas drastique, suggérant que le modèle a appris une approximation raisonnable de la distribution réelle, mais qu'il reste de la marge pour son amélioration.

\textbf{4.2. Cas d'un modèle parfait $Q^* = P$ :}
Si un modèle de langage $Q^*$ était parfait et que sa distribution de probabilité prédite était *identique* à la distribution réelle P, c'est-à-dire $Q^*(x_i) = P(x_i)$ pour tous les mots $x_i$ :

*   \textbf{Valeur de $H(P, Q^*)$ :}
    La formule de l'entropie croisée est $H(P, Q^*) = - \sum_{i} P(x_i) \ln(Q^*(x_i))$.
    Puisque nous avons $Q^*(x_i) = P(x_i)$ pour chaque mot $x_i$, nous pouvons substituer $Q^*(x_i)$ par $P(x_i)$ dans la formule :
    $H(P, Q^*) = - \sum_{i} P(x_i) \ln(P(x_i))$.
    Cette dernière expression est, par définition, la formule de l'entropie de Shannon de la distribution P, soit $H(P)$.
    Par conséquent, pour un modèle parfait, l'entropie croisée serait égale à l'entropie de Shannon de la distribution réelle.
    Avec les valeurs calculées précédemment, $H(P, Q^*) = H(P) \approx 0.8018$ nats.
    Cela signifie que si le modèle était parfait, le coût moyen d'encodage des événements (l'entropie croisée) serait le minimum théorique possible, égal à l'incertitude intrinsèque de la distribution réelle elle-même.

*   \textbf{Valeur de $D_{KL}(P || Q^*)$ :}
    La formule de la divergence de Kullback-Leibler est $D_{KL}(P || Q^*) = \sum_{i} P(x_i) \ln\left(\frac{P(x_i)}{Q^*(x_i)}\right)$.
    Puisque nous avons $Q^*(x_i) = P(x_i)$ pour chaque mot $x_i$, le rapport $\frac{P(x_i)}{Q^*(x_i)}$ devient $\frac{P(x_i)}{P(x_i)} = 1$ pour toutes les issues.
    La formule de la divergence KL se simplifie alors en :
    $D_{KL}(P || Q^*) = \sum_{i} P(x_i) \ln(1)$.
    Nous savons que $\ln(1) = 0$.
    Donc, $D_{KL}(P || Q^*) = \sum_{i} P(x_i) \times 0 = 0$.
    Par conséquent, pour un modèle parfait, la divergence KL serait de 0 nats.
    Cela signifie qu'il n'y a aucune perte d'information en approximant la distribution réelle P par la distribution du modèle $Q^*$ car les deux distributions sont identiques. C'est l'objectif ultime de l'entraînement d'un modèle de langage : réduire la divergence KL à une valeur aussi proche de zéro que possible.