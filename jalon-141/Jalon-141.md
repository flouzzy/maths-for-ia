---
uuid: "jalon-141"
title: "Théorèmes de Glivenko-Cantelli généralisés pour les classes de fonctions VC."
year: 3
trimester: 12
tags:
  - math/fondations
  - ia/theorie
prev: "[[Jalon-140.md]]"
next: "[[Jalon 142 (Processus de décision de Markov).md]]"
---

# Jalon 141 : Théorèmes de Glivenko-Cantelli généralisés pour les classes de fonctions VC.

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*
- **La Métaphore :** Imaginez que vous deviez sonder l'opinion de tout un pays sur une infinité de questions possibles. Le théorème de Glivenko-Cantelli classique vous dit que pour UNE question, un sondage bien mené reflète la réalité globale. Le théorème généralisé nous dit qu'il existe des "classes de questions" (les classes VC) tellement structurées qu'un seul sondage suffit pour connaître la réalité globale sur *toutes* ces questions à la fois !
- **Le "Pourquoi on a inventé ça" :** En apprentissage automatique, nous ne voulons pas juste qu'un modèle soit bon sur les données d'entraînement, nous voulons garantir qu'il sera bon sur *toutes* les données futures possibles (généralisation). Le théorème généralisé garantit que si la famille de modèles (la classe VC) n'est pas trop complexe, l'erreur empirique convergera uniformément vers la vraie erreur.
- **Visualisation :** Visualisez une surface qui fluctue au gré des tirages aléatoires. Le théorème de Glivenko-Cantelli garantit que, pour des classes de fonctions spécifiques, cette surface tout entière "s'aplatit" et se rapproche de la surface théorique véritable à mesure que le nombre d'échantillons augmente.

## 2. Formalisation & Rigueur Académique

### A. Définitions Formelles

Soit $(\mathcal{Z}, \mathcal{A}, P)$ un espace de probabilité. Soit $Z_1, \dots, Z_n$ des variables aléatoires i.i.d. de loi $P$.
Soit $\mathcal{F}$ une classe de fonctions mesurables de $\mathcal{Z}$ dans $[0, 1]$.

La mesure empirique $P_n$ est définie par $P_n = \frac{1}{n} \sum_{i=1}^n \delta_{Z_i}$.
Pour toute fonction $f \in \mathcal{F}$, on note :
$$P(f) = \mathbb{E}_{Z \sim P}[f(Z)] = \int_{\mathcal{Z}} f(z) dP(z)$$
$$P_n(f) = \frac{1}{n} \sum_{i=1}^n f(Z_i)$$

La classe $\mathcal{F}$ est dite **Glivenko-Cantelli** pour $P$ si :
$$\sup_{f \in \mathcal{F}} |P_n(f) - P(f)| \xrightarrow{n \to \infty} 0 \quad \text{presque sûrement.}$$

### B. Théorèmes, Propositions & Lemmes

> **Théorème de Vapnik-Chervonenkis (Glivenko-Cantelli Généralisé) :**
> Soit $\mathcal{F}$ une classe de fonctions indicatrices (à valeurs dans $\{0, 1\}$). Si la dimension de Vapnik-Chervonenkis (VC) de $\mathcal{F}$, notée $VC(\mathcal{F})$, est finie, alors $\mathcal{F}$ est une classe de Glivenko-Cantelli universelle (pour toute mesure de probabilité $P$).
> Plus précisément, pour tout $\epsilon > 0$ :
> $$ P\left( \sup_{f \in \mathcal{F}} |P_n(f) - P(f)| > \epsilon \right) \le 8 \cdot S_{\mathcal{F}}(n) e^{-n \epsilon^2 / 32} $$
> où $S_{\mathcal{F}}(n)$ est la fonction de croissance de la classe $\mathcal{F}$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration du Théorème Pivot : Inégalité de Vapnik-Chervonenkis
1. **Initialisation / Cadre :** La démonstration repose sur le lemme de symétrisation. Soit un échantillon "fantôme" $Z_1', \dots, Z_n'$ i.i.d. de même loi que $Z_1, \dots, Z_n$, indépendant du premier échantillon. Notons $P_n'$ la mesure empirique associée.
2. **Étape 1 : Symétrisation**
   D'après le lemme de symétrisation (pour $n \epsilon^2 \ge 2$) :
   $$ P\left( \sup_{f \in \mathcal{F}} |P_n(f) - P(f)| > \epsilon \right) \le 2 P\left( \sup_{f \in \mathcal{F}} |P_n(f) - P_n'(f)| > \frac{\epsilon}{2} \right) $$
3. **Étape 2 (Introduction des variables de Rademacher) :**
   Soit $\sigma_1, \dots, \sigma_n$ des variables de Rademacher indépendantes ($P(\sigma_i=1)=P(\sigma_i=-1)=1/2$). Par symétrie, la distribution de $f(Z_i) - f(Z_i')$ est la même que celle de $\sigma_i (f(Z_i) - f(Z_i'))$. Ainsi :
   $$ 2 P\left( \sup_{f \in \mathcal{F}} \frac{1}{n} \left| \sum_{i=1}^n (f(Z_i) - f(Z_i')) \right| > \frac{\epsilon}{2} \right) = 2 P\left( \sup_{f \in \mathcal{F}} \frac{1}{n} \left| \sum_{i=1}^n \sigma_i (f(Z_i) - f(Z_i')) \right| > \frac{\epsilon}{2} \right) $$
   Par l'inégalité triangulaire, ceci est borné par :
   $$ 4 P\left( \sup_{f \in \mathcal{F}} \frac{1}{n} \left| \sum_{i=1}^n \sigma_i f(Z_i) \right| > \frac{\epsilon}{4} \right) $$
4. **Étape 3 (Conditionnement et Inégalité de Hoeffding) :**
   Conditionnellement à l'échantillon $Z_1, \dots, Z_n$, la classe $\mathcal{F}$ se réduit à au plus $S_{\mathcal{F}}(n)$ vecteurs distincts $(f(Z_1), \dots, f(Z_n))$. Par l'inégalité de borne d'union et l'inégalité de Hoeffding :
   $$ P\left( \sup_{f \in \mathcal{F}} \frac{1}{n} \left| \sum_{i=1}^n \sigma_i f(Z_i) \right| > \frac{\epsilon}{4} \bigg| Z \right) \le 2 S_{\mathcal{F}}(n) \exp\left( - \frac{2 n^2 (\epsilon/4)^2}{\sum_{i=1}^n 1^2} \right) = 2 S_{\mathcal{F}}(n) e^{-n \epsilon^2 / 8} $$
5. **Conclusion :**
   En intégrant par rapport à $Z$, on obtient :
   $$ P\left( \sup_{f \in \mathcal{F}} |P_n(f) - P(f)| > \epsilon \right) \le 8 S_{\mathcal{F}}(n) e^{-n \epsilon^2 / 32} $$
   Par le lemme de Sauer-Shelah, si la dimension VC est finie (notons la $d$), $S_{\mathcal{F}}(n) \le (en/d)^d$. La décroissance exponentielle l'emporte sur la croissance polynomiale, prouvant que la limite est $0$ (convergence uniforme). $\blacksquare$

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Application Directe
**Énoncé :** Soit $\mathcal{F}$ la classe des indicatrices des intervalles de la forme $(-\infty, t]$ dans $\mathbb{R}$. Montrer en utilisant le théorème généralisé que $\mathcal{F}$ est Glivenko-Cantelli.
**Correction Détaillée :**
* *Analyse de l'énoncé :* La dimension VC de la classe des demi-droites est $d = 1$.
* *Résolution pas-à-pas :*
  $$ VC(\mathcal{F}) = 1 < \infty $$
  Donc la fonction de croissance est bornée polynomialement : $S_{\mathcal{F}}(n) \le n+1$.
  Le théorème de VC s'applique directement et assure que la convergence uniforme est acquise. C'est le théorème de Glivenko-Cantelli classique.

### Exercice 2 : Niveau Avancé (Inspiré Concours X / ENS / MIT)
**Énoncé :** Démontrer le lemme de symétrisation.
**Correction Détaillée :**
* *Analyse de l'énoncé :* Il faut manipuler adroitement l'indépendance de l'échantillon fantôme.
* *Résolution pas-à-pas :*
  Soit $A = \{ \sup_{f \in \mathcal{F}} |P_n(f) - P(f)| > \epsilon \}$. Si $A$ est réalisé, il existe $f^*$ tel que $|P_n(f^*) - P(f^*)| > \epsilon$.
  Conditionnellement à l'échantillon, par l'inégalité de Tchebychev, si $n \ge 2/\epsilon^2$, $P'( |P_n'(f^*) - P(f^*)| < \epsilon / 2) \ge 1/2$.
  Ainsi, si $A$ est vrai, la probabilité que $|P_n(f^*) - P_n'(f^*)| > \epsilon/2$ est au moins $1/2$. Intégrer donne le facteur $2$.

## 5. Ancrage & Application en Intelligence Artificielle
- **Le Pont Théorique :** Le théorème VC garantit fondamentalement que l'apprentissage PAC (Probably Approximately Correct) est possible. C'est la fondation qui permet d'assurer qu'un réseau de neurones minimisant l'erreur sur le jeu d'entraînement générera bien de bonnes prédictions sur des données jamais vues (à condition que sa capacité VC ne soit pas infinie ou trop grande par rapport à $n$).
- **Exemple Concret :** La régularisation (comme le weight decay) dans les réseaux profonds vise empiriquement à restreindre la classe $\mathcal{F}$ parcourue par l'optimiseur pour réduire sa dimension VC effective, garantissant ainsi la borne supérieure de l'erreur de généralisation selon ce théorème de Glivenko-Cantelli.

## 6. Liens Sémantiques & Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon 136 (Theorie de Vapnik-Chervonenkis)]], [[Jalon 140]]
- **Concepts Futurs dépendants :** [[Jalon 142 (Processus de décision de Markov)]]
