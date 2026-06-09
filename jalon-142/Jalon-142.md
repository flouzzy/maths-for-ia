# Jalon 142

**Année 3 : le niveau master (analyse fonctionnelle, géométrie et apprentissage)** > **Trimestre 12 : théorie de l'apprentissage statistique**

> *Le sommet du cursus : prouver mathématiquement qu'une machine est capable de généraliser.*

## Description
Processus de décision de Markov (MDP) sur des espaces d'états continus, opérateurs de contraction de Bellman.

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*
- **La Métaphore :** Imaginez un navigateur tentant de traverser un océan parsemé d'îles et de tempêtes. À chaque instant, il doit choisir une direction (action), mais le vent et les courants marins introduisent une incertitude sur sa destination exacte (état futur). Son but est de minimiser le temps de trajet tout en évitant les récifs (récompense/pénalité).
- **Le "Pourquoi on a inventé ça" :** Les MDP ont été inventés pour formaliser la prise de décision séquentielle sous incertitude. Comment planifier une séquence d'actions optimale lorsque les conséquences de nos actes ne sont que partiellement prévisibles ?
- **Visualisation :** On peut visualiser un MDP comme un graphe où les nœuds représentent des états, les arêtes des actions possibles, et où chaque action mène à une distribution de probabilité sur les nœuds suivants, avec une récompense associée à chaque transition.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Un Processus de Décision de Markov (MDP) est défini par un 5-uplet $(\mathcal{S}, \mathcal{A}, P, R, \gamma)$ où :
- $\mathcal{S}$ est l'espace des états, supposé ici être un espace polonais (métrique complet séparable), souvent un sous-ensemble compact de $\mathbb{R}^n$.
- $\mathcal{A}$ est l'espace des actions, généralement un espace mesurable.
- $P : \mathcal{S} \times \mathcal{A} \times \mathcal{B}(\mathcal{S}) \to [0, 1]$ est un noyau de transition de probabilité, c'est-à-dire que pour tout $(s,a)$, $P(\cdot | s,a)$ est une mesure de probabilité sur la tribu borélienne $\mathcal{B}(\mathcal{S})$.
- $R : \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ est la fonction de récompense immédiate, supposée mesurable et bornée.
- $\gamma \in [0, 1)$ est le facteur d'escompte (discount factor).

Une politique (ou stratégie) est une application $\pi : \mathcal{S} \to \Delta(\mathcal{A})$ (ou $\pi : \mathcal{S} \to \mathcal{A}$ dans le cas déterministe). La fonction de valeur d'une politique $\pi$, notée $V^\pi(s)$, est l'espérance de la somme des récompenses escomptées :
$$ V^\pi(s) = \mathbb{E}_\pi \left[ \sum_{t=0}^\infty \gamma^t R(s_t, a_t) \mid s_0 = s \right] $$

La fonction de valeur optimale $V^*(s)$ est définie par $V^*(s) = \sup_\pi V^\pi(s)$.

### B. Théorèmes, Propositions & Lemmes
> **Théorème de Contraction de Bellman :**
> Soit $\mathcal{B}(\mathcal{S})$ l'espace de Banach des fonctions mesurables bornées de $\mathcal{S}$ dans $\mathbb{R}$, muni de la norme du supremum $\|V\|_\infty = \sup_{s \in \mathcal{S}} |V(s)|$. L'opérateur de Bellman optimal $T^* : \mathcal{B}(\mathcal{S}) \to \mathcal{B}(\mathcal{S})$ défini par :
> $$ (T^*V)(s) = \sup_{a \in \mathcal{A}} \left\{ R(s, a) + \gamma \int_{\mathcal{S}} V(s') P(ds' | s, a) \right\} $$
> est une contraction stricte de rapport $\gamma$ pour la norme $\|\cdot\|_\infty$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
### Démonstration du Théorème Pivot : Contraction de Bellman
1. **Initialisation / Cadre :** Soient $U, V \in \mathcal{B}(\mathcal{S})$. Nous voulons majorer $\|T^*U - T^*V\|_\infty$. Fixons un état $s \in \mathcal{S}$.
2. **Étape 1 :** Par définition du supremum, pour tout $\epsilon > 0$, il existe une action $a_U \in \mathcal{A}$ telle que :
   $$ (T^*U)(s) \le R(s, a_U) + \gamma \int_{\mathcal{S}} U(s') P(ds' | s, a_U) + \epsilon $$
3. **Étape 2 (Transition micro-calculatoire) :** Parallèlement, nous avons $(T^*V)(s) \ge R(s, a_U) + \gamma \int_{\mathcal{S}} V(s') P(ds' | s, a_U)$.
   En soustrayant cette inégalité de la précédente, on obtient :
   $$ (T^*U)(s) - (T^*V)(s) \le \gamma \int_{\mathcal{S}} (U(s') - V(s')) P(ds' | s, a_U) + \epsilon $$
   Or, pour tout $s'$, $U(s') - V(s') \le \|U - V\|_\infty$. Puisque l'intégrale porte sur une mesure de probabilité (masse totale égale à 1) :
   $$ \int_{\mathcal{S}} (U(s') - V(s')) P(ds' | s, a_U) \le \int_{\mathcal{S}} \|U - V\|_\infty P(ds' | s, a_U) = \|U - V\|_\infty $$
   D'où $(T^*U)(s) - (T^*V)(s) \le \gamma \|U - V\|_\infty + \epsilon$.
   Par un argument symétrique, en choisissant un $a_V$ quasi-optimal pour $V$, on montre de même que $(T^*V)(s) - (T^*U)(s) \le \gamma \|U - V\|_\infty + \epsilon$.
4. **Conclusion :** Puisque $\epsilon > 0$ est arbitraire, on en déduit que pour tout $s \in \mathcal{S}$, $|(T^*U)(s) - (T^*V)(s)| \le \gamma \|U - V\|_\infty$.
   En prenant le supremum sur $s$, on obtient finalement :
   $$ \|T^*U - T^*V\|_\infty \le \gamma \|U - V\|_\infty $$
   Comme $\gamma < 1$, l'opérateur $T^*$ est une contraction stricte. Par le théorème de Banach, il possède un unique point fixe, qui se trouve être la fonction de valeur optimale $V^*$.

## 4. Exercices d'Application & Pratique de Concours
*Les exercices sont fournis dans le dossier `exos/`.*

## 5. Ancrage & Application en Intelligence Artificielle
- **Le Pont Théorique :** Le théorème de contraction de Bellman est le fondement mathématique qui garantit la convergence des algorithmes d'Apprentissage par Renforcement (Reinforcement Learning) tels que le Q-Learning ou Value Iteration.
- **Exemple Concret :** Dans AlphaGo ou les modèles de robotique, l'espace des états est continu ou gigantesque. Les réseaux de neurones profonds agissent comme des approximateurs de la fonction de valeur (Deep Q-Networks). Bien que l'approximation introduise de nouvelles difficultés, la contraction sous-jacente reste le moteur théorique permettant d'espérer trouver une politique optimale.

---
**Précédent** : [[Jalon-141]] | **Suivant** : [[Jalon 143 (Théorie spectrale des graphes)]]
