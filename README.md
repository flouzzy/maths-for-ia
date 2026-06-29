# 🎓 Mathématiques pour l'Intelligence Artificielle

> **Un cursus complet en 3 ans** (de la L1 au Master 2) conçu pour acquérir la **rigueur mathématique absolue** (niveau ENS / École Polytechnique / MIT) indispensable à la compréhension profonde et à la recherche en Intelligence Artificielle.

[![Obsidian Vault](https://img.shields.io/badge/Obsidian-Vault-purple?logo=obsidian&logoColor=white)](https://obsidian.md/)
[![Rigor Level](https://img.shields.io/badge/Rigueur-Polytechnique%20%2F%20ENS-red)](#)
[![Pedagogical Approach](https://img.shields.io/badge/P%C3%A9dagogie-Intuition%20%E2%9E%A1%EF%B8%8E%20Rigueur-blue)](#)

---

## 🎯 Objectif du Cursus

Ce dépôt est configuré comme un **coffre Obsidian (*Obsidian Vault*)** de fiches de notes interconnectées. L'objectif est de combler le fossé entre les explications superficielles ("avec les mains") et la rigueur universitaire de haut niveau. 

Chaque module guide l'apprenant à travers une progression sans rupture :
1. **L'intuition géométrique ou physique** (niveau Terminale S / L1) pour saisir le sens physique.
2. **La formalisation mathématique rigoureuse** (définitions $\epsilon-N$, axiomes, structures algébriques).
3. **La preuve complète à blanc** des théorèmes fondamentaux.
4. **L'application directe en IA** sous forme d'exercices théoriques avancés et de travaux pratiques de code.

---

## 💡 Philosophie et Structure d'un Jalon Enrichi

Pour chaque jalon traité, la structure Obsidian suivante est générée afin de séparer proprement la théorie de la pratique :

```text
📂 jalon-[N]/
  ├── 📄 Jalon-[N] (Nom).md    <-- Cours magistral de référence (LaTeX exhaustif)
  ├── 📄 README.md             <-- Historique d'apprentissage et statut d'avancement
  ├── 📂 exos/                 <-- 10 exercices progressifs (du niveau L1 jusqu'à l'ENS/X)
  └── 📂 tp/                   <-- 5 travaux pratiques codés "from scratch" en Python pur
```

---

## 🗺️ Organisation Globale du Programme

| Période | Thématique Majeure | Fondements Théoriques | Applications IA Clés |
| :--- | :--- | :--- | :--- |
| **Année 1** | **Bases & Analyse Réelle** | Logique, Algèbre Linéaire, Topologie de $\mathbb{R}^n$, Différentiabilité | Similarité cosinus, Décomposition SVD, Rétropropagation |
| **Année 2** | **Topologie & Mesures** | Topologie générale, Intégration de Lebesgue, Espaces $L^p$, Probabilités axiomatiques | Divergence KL, Théorème d'Approximation Universelle, Cross-Entropy |
| **Année 3** | **Analyse Fonctionnelle** | Espaces de Hilbert, Géométrie Différentielle, Optimisation Convexe, PAC Learning | Bornes de généralisation Rademacher/VC, GNNs, Robbins-Monro, Double Descente |

---

## ⚙️ Configuration avec Obsidian

Ce dépôt est conçu pour être ouvert directement comme un **Vault** dans [Obsidian](https://obsidian.md/).

### 🔌 Plugins Recommandés
Pour exploiter au mieux ce vault, nous vous suggérons d'installer et activer :
1. **MathJax** (intégré nativement) : pour le rendu optimal des équations en LaTeX.
2. **Excalidraw** : pour visualiser et éditer les schémas géométriques.
3. **Obsidian Git** : pour sauvegarder et versionner automatiquement votre progression.

---

## 📚 Sommaire Détaillé du Cursus

> [!NOTE]
> Les jalons marqués de l'icône 🔥 **Enrichi** contiennent le cours magistral de référence, **10 exercices corrigés** (jusqu'au niveau ENS) et **5 TP pratiques** codés en Python pur.


### 📅 Année 1 : le socle des fondations et l'analyse réelle

<details>
<summary><b>Trimestre 1 : logique, ensembles et algèbre linéaire de base</b></summary>
<br>

- **[Jalon 1](jalon-1/Jalon%201%20%28Logique%20formelle%29.md)** : Logique formelle, connecteurs, tables de vérité et calcul des propositions. 🔥 **Enrichi** *(10 Exos + 5 TP)*
- **[Jalon 2](jalon-2/Jalon%202%20%28M%C3%A9thodes%20de%20raisonnement%29.md)** : Méthodes de raisonnement (implication, contraposée, l'absurde, analyse-synthèse).
- **[Jalon 3](jalon-3/Jalon-3.md)** : Quantification ($\forall, \exists$), ordre des quantificateurs et négation de propositions complexes. 🔥 **Enrichi** *(10 Exos + 5 TP)*
- **[Jalon 4](jalon-4/Jalon-4.md)** : Théorie des ensembles (ZFC), opérations sur les ensembles, ensembles des parties $\mathcal{P}(E)$.
- **[Jalon 5](jalon-5/Jalon-5.md)** : Applications, injections, surjections, bijections et composition de fonctions.
- **[Jalon 6](jalon-6/Jalon%206%20%28Relations%20d%27%C3%A9quivalence%29.md)** : Relations d'équivalence, relations d'ordre, ensembles quotients et structures de base (groupes, anneaux, corps).
- **[Jalon 7](jalon-7/Jalon-7.md)** : Espaces vectoriels abstraits, familles libres, familles génératrices et bases en dimension finie.
- **[Jalon 8](jalon-8/Jalon-8.md)** : Applications linéaires, noyau ($\ker$), image ($\text{Im}$) et démonstration du théorème du rang.
- **[Jalon 9](jalon-9/Jalon%209%20%28Calcul%20matriciel%29.md)** : Calcul matriciel, opérations, inversibilité et représentations des applications linéaires.
- **[Jalon 10](jalon-10/Jalon-10.md)** : Changements de base, matrices de passage et matrices par blocs. 🔥 **Enrichi** *(10 Exos + 5 TP)*
- **[Jalon 11](jalon-11/Jalon%2011%20%28Formes%20lin%C3%A9aires%29.md)** : Formes linéaires, hyperplans, espace dual et orthogonalité en dimension finie.
- **[Jalon 12](jalon-12/Jalon%2012%20%28Livrable%20IA%29.md)** : Livrable IA T1 : Conception théorique d'un moteur de recherche sémantique par similarité cosinus (dualité et géométrie des espaces de plongement) et résolution d'un problème d'algèbre de l'X.

</details>

<details>
<summary><b>Trimestre 2 : analyse réelle, suites et séries de fonctions</b></summary>
<br>

- **[Jalon 13](jalon-13/Jalon%2013%20%28Structure%20de%20--mathbb%7BR%7D-%29.md)** : Structure de $\mathbb{R}$, axiome de la borne supérieure et propriété d'Archimède.
- **[Jalon 14](jalon-14/Jalon%2014%20%28Suites%20r%C3%A9elles%20et%20complexes%29.md)** : Suites réelles et complexes, définitions rigoureuses des limites ($\epsilon, N$) et critères de convergence.
- **[Jalon 15](jalon-15/Jalon%2015%20%28Sous-suites%29.md)** : Sous-suites, valeurs d'adhérence et preuve par séparation du théorème de Bolzano-Weierstrass.
- **[Jalon 16](jalon-16/Jalon-16.md)** : Séries numériques à termes positifs, critères de comparaison, de d'Alembert et de Cauchy. 🔥 **Enrichi** *(10 Exos + 5 TP)*
- **[Jalon 17](jalon-17/Jalon%2017%20%28S%C3%A9ries%20absolument%20convergentes%29.md)** : Séries absolument convergentes, semi-convergentes et produit de Cauchy de deux séries.
- **[Jalon 18](jalon-18/Jalon%2018%20%28Continuit%C3%A9%20des%20fonctions%20d%27une%20variable%20r%C3%A9elle%29.md)** : Continuité des fonctions d'une variable réelle, théorème des valeurs intermédiaires et compacité locale.
- **[Jalon 19](jalon-19/Jalon%2019%20%28D%C3%A9rivabilit%C3%A9%29.md)** : Dérivabilité, théorème de Rolle, théorème des accroissements finis et prolongement de la dérivée.
- **[Jalon 20](jalon-20/Jalon%2020%20%28D%C3%A9riv%C3%A9es%20successives%29.md)** : Dérivées successives, formules de Taylor-Lagrange, Taylor-Young et développements limités.
- **[Jalon 21](jalon-21/Jalon%2021%20%28Suites%20de%20fonctions%29.md)** : Suites de fonctions, étude de la convergence simple et de la convergence uniforme.
- **[Jalon 22](jalon-22/Jalon%2022%20%28S%C3%A9ries%20de%20fonctions%29.md)** : Séries de fonctions, convergence normale, théorèmes d'interversion limite-intégrale et limite-dérivée.
- **[Jalon 23](jalon-23/Jalon%2023%20%28S%C3%A9ries%20enti%C3%A8res%29.md)** : Séries entières, calcul du rayon de convergence (règle de d'Alembert-Cauchy) et propriétés de la somme.
- **[Jalon 24](jalon-24/Jalon%2024%20%28Livrable%20IA%29.md)** : Livrable IA T2 : Analyse mathématique des critères de convergence d'une régression polynomiale et résolution d'un problème d'analyse de l'ENS sur les interversions de limites.

</details>

<details>
<summary><b>Trimestre 3 : réduction des endomorphismes et espaces préhilbertiens</b></summary>
<br>

- **[Jalon 25](jalon-25/Jalon%2025%20%28Formes%20bilin%C3%A9aires%29.md)** : Formes bilinéaires, formes sesquilinieaires, produit scalaire et inégalité de Cauchy-Schwarz.
- **[Jalon 26](jalon-26/Jalon%2026%20%28Espaces%20euclidiens%29.md)** : Espaces euclidiens, orthogonalité, théorème de la projection orthogonale et algorithme de Gram-Schmidt.
- **[Jalon 27](jalon-27/Jalon%2027%20%28Endomorphismes%20sym%C3%A9triques%29.md)** : Endomorphismes symétriques, adjoint d'un opérateur et matrices orthogonales.
- **[Jalon 28](jalon-28/Jalon%2028%20%28Polyn%C3%B4mes%20d%27endomorphismes%29.md)** : Polynômes d'endomorphismes, idéaux annulateurs et démonstration du théorème de Cayley-Hamilton.
- **[Jalon 29](jalon-29/Jalon%2029%20%28%C3%89l%C3%A9ments%20propres%29.md)** : Éléments propres, polynôme caractéristique, sous-espaces propres et critères de diagonalisabilité.
- **[Jalon 30](jalon-30/Jalon%2030%20%28Trigonalisation%20d%27endomorphismes%20et%20d%C3%A9composition%20de%20Dunford.%29.md)** : Trigonalisation d'endomorphismes et décomposition de Dunford.
- **[Jalon 31](jalon-31/Jalon%2031%20%28Introduction%20%C3%A0%20la%20r%C3%A9duction%20de%20Jordan%20et%20structure%20des%20nilpotents.%29.md)** : Introduction à la réduction de Jordan et structure des nilpotents.
- **[Jalon 32](jalon-32/Jalon%2032%20%28Preuve%20compl%C3%A8te%20du%20th%C3%A9or%C3%A8me%20spectral%20pour%20les%20endomorphismes%20sym%C3%A9triques.%29.md)** : Preuve complète du théorème spectral pour les endomorphismes symétriques.
- **[Jalon 33](jalon-33/Jalon%2033%20%28Formes%20quadratiques%29.md)** : Formes quadratiques, réduction de Gauss, base orthogonale et loi d'inertie de Sylvester.
- **[Jalon 34](jalon-34/Jalon%2034%20%28Topologie%20%C3%A9l%C3%A9mentaire%20des%20espaces%20vectoriels%20norm%C3%A9s%29.md)** : Topologie élémentaire des espaces vectoriels normés (normes, équivalence des normes en dimension finie).
- **[Jalon 35](jalon-35/Jalon%2035%20%28Caract%C3%A9risation%20s%C3%A9quentielle%20des%20ouverts%29.md)** : Caractérisation séquentielle des ouverts, des fermés et des compacts (Heine-Borel).
- **[Jalon 36](jalon-36/Jalon%2036%20%28Livrable%20IA%29.md)** : Livrable IA T3 : Écriture des équations de la décomposition en valeurs singulières (SVD) et application mathématique à la compression d'une matrice de pixels d'image.

</details>

<details>
<summary><b>Trimestre 4 : calcul différentiel et intégration de Riemann</b></summary>
<br>

- **[Jalon 37](jalon-37/Jalon%2037%20%28Int%C3%A9grale%20de%20Riemann%20sur%20un%20segment%29.md)** : Intégrale de Riemann sur un segment, fonctions en escalier et propriétés de l'intégrale.
- **[Jalon 38](jalon-38/Jalon%2038%20%28Th%C3%A9or%C3%A8me%20fondamental%20de%20l%27analyse%29.md)** : Théorème fondamental de l'analyse, primitives et techniques d'intégration (IPP, changement de variable).
- **[Jalon 39](jalon-39/Jalon%2039%20%28Int%C3%A9grales%20g%C3%A9n%C3%A9ralis%C3%A9es%20sur%20un%20intervalle%20quelconque%20et%20crit%C3%A8res%20de%20convergence.%29.md)** : Intégrales généralisées sur un intervalle quelconque et critères de convergence.
- **[Jalon 40](jalon-40/Jalon%2040%20%28Int%C3%A9grales%20d%C3%A9pendant%20d%27un%20param%C3%A8tre%29.md)** : Intégrales dépendant d'un paramètre, théorèmes de continuité et de dérivation sous le signe $\int$.
- **[Jalon 41](jalon-41/Jalon%2041%20%28%C3%89quations%20diff%C3%A9rentielles%20lin%C3%A9aires%20du%20premier%20ordre%20et%20m%C3%A9thode%20de%20variation%20de%20la%20constante.%29.md)** : Équations différentielles linéaires du premier ordre et méthode de variation de la constante.
- **[Jalon 42](jalon-42/Jalon%2042%20%28%C3%89quations%20diff%C3%A9rentielles%20lin%C3%A9aires%20du%20second%20ordre%20%C3%A0%20coefficients%20constants.%29.md)** : Équations différentielles linéaires du second ordre à coefficients constants.
- **[Jalon 43](jalon-43/Jalon%2043%20%28Syst%C3%A8mes%20diff%C3%A9rentiels%20lin%C3%A9aires%20d%27ordre%201%20et%20calcul%20de%20l%27exponentielle%20de%20matrice.%29.md)** : Systèmes différentiels linéaires d'ordre 1 et calcul de l'exponentielle de matrice.
- **[Jalon 44](jalon-44/Jalon%2044%20%28Fonctions%20de%20plusieurs%20variables%29.md)** : Fonctions de plusieurs variables, limites, continuité et topologie de $\mathbb{R}^n$.
- **[Jalon 45](jalon-45/Jalon%2045%20%28Diff%C3%A9rentiabilit%C3%A9%29.md)** : Différentiabilité, différentielle totale, dérivées partielles et gradient.
- **[Jalon 46](jalon-46/Jalon%2046%20%28Matrice%20jacobienne%29.md)** : Matrice jacobienne, théorème de dérivation des fonctions composées (Chain Rule généralisée).
- **[Jalon 47](jalon-47/Jalon%2047%20%28D%C3%A9riv%C3%A9es%20partielles%20d%27ordre%20deux%29.md)** : Dérivées partielles d'ordre deux, matrice hessienne et lemme de Schwarz.
- **[Jalon 48](jalon-48/Jalon%2048%20%28Livrable%20IA%29.md)** : Livrable IA T4 : Formalisation mathématique complète de la rétropropagation (Backpropagation) d'un réseau de neurones profond sous forme de produits de matrices jacobiennes.

</details>


### 📅 Année 2 : l'abstraction topologique et la théorie de la mesure

<details>
<summary><b>Trimestre 5 : topologie générale et espaces métriques</b></summary>
<br>

- **[Jalon 49](jalon-49/Jalon%2049%20%28Espaces%20topologiques%20g%C3%A9n%C3%A9raux%29.md)** : Espaces topologiques généraux, définition par les ouverts, les fermés et les voisinages.
- **[Jalon 50](jalon-50/Jalon%2050%20%28Op%C3%A9rateurs%20topologiques%29.md)** : Opérateurs topologiques : intérieur, adhérence, frontière et ensembles denses.
- **[Jalon 51](jalon-51/Jalon%2051%20%28Espaces%20m%C3%A9triques%29.md)** : Espaces métriques, topologie induite par une distance et distances équivalentes.
- **[Jalon 52](jalon-52/Jalon%2052%20%28Applications%20continues%20entre%20espaces%20topologiques%20et%20d%C3%A9finition%20fine%20des%20hom%C3%A9omorphismes.%29.md)** : Applications continues entre espaces topologiques et définition fine des homéomorphismes.
- **[Jalon 53](jalon-53/Jalon%2053%20%28Axiomes%20de%20s%C3%A9paration%29.md)** : Axiomes de séparation (notamment les espaces de Hausdorff).
- **[Jalon 54](jalon-54/Jalon%2054%20%28Compacit%C3%A9%20g%C3%A9n%C3%A9rale%29.md)** : Compacité générale (propriété de Borel-Lebesgue) et démonstration du théorème de Tychonoff pour les produits finis.
- **[Jalon 55](jalon-55/Jalon%2055%20%28Connexit%C3%A9%29.md)** : Connexité, connexité par arcs et étude des composantes connexes.
- **[Jalon 56](jalon-56/Jalon%2056%20%28Espaces%20m%C3%A9triques%20complets%29.md)** : Espaces métriques complets, suites de Cauchy et théorème de prolongement des applications continues.
- **[Jalon 57](jalon-57/Jalon%2057%20%28Th%C3%A9or%C3%A8me%20du%20point%20fixe%20de%20Banach%29.md)** : Théorème du point fixe de Banach (contractions) et application à l'existence locale des solutions d'EDP.
- **[Jalon 58](jalon-58/Jalon%2058%20%28Th%C3%A9or%C3%A8me%20de%20Baire%29.md)** : Théorème de Baire (les espaces de l'impossible) et applications aux fonctions continues nulle part dérivables.
- **[Jalon 59](jalon-59/Jalon%2059%20%28Topologie%20des%20espaces%20de%20fonctions%29.md)** : Topologie des espaces de fonctions, convergence compacte et théorème d'Arzelà-Ascoli.
- **[Jalon 60](jalon-60/Jalon%2060%20%28Livrable%20IA%29.md)** : Livrable IA T5 : Preuve du théorème d'approximation universelle des réseaux de neurones (utilisation de la topologie de la convergence uniforme sur les compacts).

</details>

<details>
<summary><b>Trimestre 6 : théorie de la mesure et intégration de Lebesgue</b></summary>
<br>

- **[Jalon 61](jalon-61/Jalon%2061%20%28Insuffisances%20de%20l%27int%C3%A9grale%20de%20Riemann%29.md)** : Insuffisances de l'intégrale de Riemann, paradoxe de la fonction de Dirichlet.
- **[Jalon 62](jalon-62/Jalon%2062%20%28Alg%C3%A8bres%29.md)** : Algèbres, $\sigma$-algèbres (tribus), tribus engendrées et tribu de Borel sur $\mathbb{R}$.
- **[Jalon 63](jalon-63/Jalon%2063%20%28D%C3%A9finition%20axiomatique%20d%27une%20mesure%29.md)** : Définition axiomatique d'une mesure, mesures finies, $\sigma$-finies et propriétés de continuité monotone.
- **[Jalon 64](jalon-64/Jalon%2064%20%28Construction%20pas%20%C3%A0%20pas%20de%20la%20mesure%20de%20Lebesgue%20sur%20-mathbb%7BR%7D-%20via%20la%20mesure%20ext%C3%A9rieure.%29.md)** : Construction pas à pas de la mesure de Lebesgue sur $\mathbb{R}$ via la mesure extérieure.
- **[Jalon 65](jalon-65/Jalon%2065%20%28Fonctions%20mesurables%29.md)** : Fonctions mesurables, opérations élémentaires et approximation par des fonctions étagées.
- **[Jalon 66](jalon-66/Jalon%2066%20%28Construction%20de%20l%27int%C3%A9grale%20de%20Lebesgue%20pour%20les%20fonctions%20mesurables%20positives.%29.md)** : Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.
- **[Jalon 67](jalon-67/Jalon%2067%20%28D%C3%A9monstration%20du%20th%C3%A9or%C3%A8me%20de%20convergence%20monotone%29.md)** : Démonstration du théorème de convergence monotone (Beppo-Levi).
- **[Jalon 68](jalon-68/Jalon%2068%20%28Lemme%20de%20Fatou%20et%20d%C3%A9finition%20de%20l%27int%C3%A9grale%20pour%20les%20fonctions%20de%20signe%20quelconque%29.md)** : Lemme de Fatou et définition de l'intégrale pour les fonctions de signe quelconque (fonctions intégrables).
- **[Jalon 69](jalon-69/Jalon%2069%20%28D%C3%A9monstration%20compl%C3%A8te%20du%20th%C3%A9or%C3%A8me%20de%20convergence%20domin%C3%A9e%20de%20Lebesgue.%29.md)** : Démonstration complète du théorème de convergence dominée de Lebesgue.
- **[Jalon 70](jalon-70/Jalon%2070%20%28Espaces%20mesur%C3%A9s%20produits%29.md)** : Espaces mesurés produits, tribu produit et construction de la mesure produit.
- **[Jalon 71](jalon-71/Jalon%2071%20%28Th%C3%A9or%C3%A8mes%20de%20Fubini-Tonelli%29.md)** : Théorèmes de Fubini-Tonelli (fonctions positives) et de Fubini (fonctions intégrables).
- **[Jalon 72](jalon-72/Jalon%2072%20%28Livrable%20IA%29.md)** : Livrable IA T6 : Formalisation de la divergence de Kullback-Leibler entre deux distributions de probabilités continues complexes.

</details>

<details>
<summary><b>Trimestre 7 : espaces $L^p$ et analyse de Fourier</b></summary>
<br>

- **[Jalon 73](jalon-73/Jalon%2073%20%28D%C3%A9finition%20des%20espaces%20-mathcal%7BL%7D%5Ep-%20et%20passage%20%C3%A0%20l%27espace%20quotient%20-L%5Ep-%29.md)** : Définition des espaces $\mathcal{L}^p$ et passage à l'espace quotient $L^p$ (égalité presque partout).
- **[Jalon 74](jalon-74/Jalon%2074%20%28In%C3%A9galit%C3%A9s%20fondamentales%20de%20l%27analyse%20fonctionnelle%29.md)** : Inégalités fondamentales de l'analyse fonctionnelle : Hölder et Minkowski.
- **[Jalon 75](jalon-75/Jalon%2075%20%28Preuve%20de%20la%20compl%C3%A9tude%20des%20espaces%20-L%5Ep-%29.md)** : Preuve de la complétude des espaces $L^p$ (Théorème de Riesz-Fischer) : structure de Banach.
- **[Jalon 76](jalon-76/Jalon%2076%20%28Propri%C3%A9t%C3%A9s%20g%C3%A9om%C3%A9triques%20de%20l%27espace%20de%20Hilbert%20-L%5E2-%29.md)** : Propriétés géométriques de l'espace de Hilbert $L^2$, produit scalaire et identité du parallélogramme.
- **[Jalon 77](jalon-77/Jalon%2077%20%28Densit%C3%A9%20des%20fonctions%20simples%29.md)** : Densité des fonctions simples, des fonctions continues à support compact et des fonctions lisses dans $L^p$.
- **[Jalon 78](jalon-78/Jalon%2078%20%28S%C3%A9ries%20de%20Fourier%29.md)** : Séries de Fourier, calcul des coefficients, convergence ponctuelle (théorème de Dirichlet).
- **[Jalon 79](jalon-79/Jalon%2079%20%28Convergence%20en%20moyenne%20quadratique%20des%20s%C3%A9ries%20de%20Fourier%20et%20identit%C3%A9%20de%20Parseval.%29.md)** : Convergence en moyenne quadratique des séries de Fourier et identité de Parseval.
- **[Jalon 80](jalon-80/Jalon%2080%20%28Transform%C3%A9e%20de%20Fourier%20dans%20-L%5E1-%29.md)** : Transformée de Fourier dans $L^1$, propriétés algébriques, Riemann-Lebesgue et produit de convolution.
- **[Jalon 81](jalon-81/Jalon%2081%20%28Transform%C3%A9e%20de%20Fourier%20dans%20-L%5E2-%29.md)** : Transformée de Fourier dans $L^2$, prolongement par densité et théorème d'isométrie de Plancherel.
- **[Jalon 82](jalon-82/Jalon%2082%20%28Introduction%20%C3%A0%20la%20th%C3%A9orie%20des%20distributions%20de%20Schwartz%29.md)** : Introduction à la théorie des distributions de Schwartz, espace des fonctions tests $\mathcal{D}(\mathbb{R})$.
- **[Jalon 83](jalon-83/Jalon%2083%20%28D%C3%A9rivation%20au%20sens%20des%20distributions%29.md)** : Dérivation au sens des distributions, distribution de Dirac et introduction aux espaces de Sobolev $H^1(\mathbb{R})$.
- **[Jalon 84](jalon-84/Jalon%2084%20%28Livrable%20IA%29.md)** : Livrable IA T7 : Création d'un module d'analyse spectrale pour l'extraction de caractéristiques audio à partir de la transformée de Fourier dans $L^2$.

</details>

<details>
<summary><b>Trimestre 8 : probabilités axiomatiques et statistiques fondamentales</b></summary>
<br>

- **[Jalon 85](jalon-85/Jalon%2085%20%28Axiomes%20de%20Kolmogorov%29.md)** : Axiomes de Kolmogorov, espace de probabilité $(\Omega, \mathcal{F}, \mathbb{P})$ comme un espace mesuré de masse 1.
- **[Jalon 86](jalon-86/Jalon%2086%20%28Variables%20al%C3%A9atoires%20vues%20comme%20des%20applications%20mesurables%29.md)** : Variables aléatoires vues comme des applications mesurables, loi d'une variable et mesure de probabilité image.
- **[Jalon 87](jalon-87/Jalon%2087%20%28Int%C3%A9gration%20des%20variables%20al%C3%A9atoires%29.md)** : Intégration des variables aléatoires, espérance, variance et moments d'ordre supérieur.
- **[Jalon 88](jalon-88/Jalon%2088%20%28Ind%C3%A9pendance%20d%27%C3%A9v%C3%A9nements%29.md)** : Indépendance d'événements, de tribus et de variables aléatoires.
- **[Jalon 89](jalon-89/Jalon%2089%20%28Lemmes%20de%20Borel-Cantelli%29.md)** : Lemmes de Borel-Cantelli (lois du tout ou rien) et applications aux comportements asymptotiques.
- **[Jalon 90](jalon-90/Jalon%2090%20%28Les%20modes%20de%20convergence%29.md)** : Les modes de convergence : presque sûre, en probabilité, dans $L^p$ et en loi (convergence étroite des mesures).
- **[Jalon 91](jalon-91/Jalon%2091%20%28In%C3%A9galit%C3%A9s%20de%20concentration%29.md)** : Inégalités de concentration : Markov, Chebyshev, Bienaymé, Chernoff et lemme de Hoeffding.
- **[Jalon 92](jalon-92/Jalon%2092%20%28D%C3%A9monstration%20rigoureuse%20de%20la%20loi%20forte%20des%20grands%20nombres.%29.md)** : Démonstration rigoureuse de la loi forte des grands nombres.
- **[Jalon 93](jalon-93/Jalon%2093%20%28Fonctions%20caract%C3%A9ristiques%29.md)** : Fonctions caractéristiques (transformée de Fourier de la loi) et théorème de continuité de Lévy.
- **[Jalon 94](jalon-94/Jalon%2094%20%28D%C3%A9monstration%20du%20th%C3%A9or%C3%A8me%20central%20limite%29.md)** : Démonstration du théorème central limite (TCL) via les développements limités des fonctions caractéristiques.
- **[Jalon 95](jalon-95/Jalon%2095%20%28Vecteurs%20gaussiens%29.md)** : Vecteurs gaussiens, loi normale multidimensionnelle, matrice de covariance et conditionnement gaussien.
- **[Jalon 96](jalon-96/Jalon%2096%20%28Livrable%20IA%29.md)** : Livrable IA T8 : Démonstration rigoureuse de la convergence de la fonction de perte Cross-Entropy vers l'information théorique de Shannon lors de l'entraînement des modèles de langage.

</details>


### 📅 Année 3 : le niveau master (analyse fonctionnelle, géométrie et apprentissage)

<details>
<summary><b>Trimestre 9 : analyse fonctionnelle et théorie spectrale</b></summary>
<br>

- **[Jalon 97](jalon-97/Jalon%2097%20%28Espaces%20de%20Banach%29.md)** : Espaces de Banach, opérateurs linéaires continus entre Banach et topologie induite par la norme d'opérateur.
- **[Jalon 98](jalon-98/Jalon%2098%20%28Th%C3%A9or%C3%A8me%20de%20Hahn-Banach%29.md)** : Théorème de Hahn-Banach (forme analytique), prolongement des formes linéaires sous-linéaires.
- **[Jalon 99](jalon-99/Jalon%2099%20%28Th%C3%A9or%C3%A8me%20de%20Hahn-Banach%29.md)** : Théorème de Hahn-Banach (formes géométriques), séparation des ensembles convexes par des hyperplans.
- **[Jalon 100](jalon-100/Jalon%20100%20%28D%C3%A9monstration%20du%20th%C3%A9or%C3%A8me%20de%20Banach-Steinhaus%29.md)** : Démonstration du théorème de Banach-Steinhaus (principe de la borne uniforme).
- **[Jalon 101](jalon-101/Jalon%20101%20%28Th%C3%A9or%C3%A8me%20de%20l%27application%20ouverte%20et%20th%C3%A9or%C3%A8me%20du%20graphe%20ferm%C3%A9.%29.md)** : Théorème de l'application ouverte et théorème du graphe fermé.
- **[Jalon 102](jalon-102/Jalon%20102%20%28Topologies%20faibles%20et%20faibles-%29.md)** : Topologies faibles et faibles-*, compacité de la boule unité duale (Théorème de Banach-Alaoglu).
- **[Jalon 103](jalon-103/Jalon%20103%20%28Espaces%20de%20Hilbert%20g%C3%A9n%C3%A9raux%29.md)** : Espaces de Hilbert généraux, théorème de projection sur un convexe fermé et dualité de Riesz.
- **[Jalon 104](jalon-104/Jalon%20104%20%28Bases%20hilbertiennes%29.md)** : Bases hilbertiennes (systèmes orthonormés complets) et séparabilité des espaces de Hilbert.
- **[Jalon 105](jalon-105/Jalon%20105%20%28Op%C3%A9rateurs%20adjoints%29.md)** : Opérateurs adjoints, opérateurs compacts et propriétés de régularisation.
- **[Jalon 106](jalon-106/Jalon%20106%20%28Th%C3%A9or%C3%A8me%20spectral%20pour%20les%20op%C3%A9rateurs%20compacts%20autoadjoints%29.md)** : Théorème spectral pour les opérateurs compacts autoadjoints (décomposition en base hilbertienne d'éléments propres).
- **[Jalon 107](jalon-107/Jalon%20107%20%28Introduction%20%C3%A0%20la%20th%C3%A9orie%20des%20op%C3%A9rateurs%20non%20born%C3%A9s%20et%20r%C3%A9solvante.%29.md)** : Introduction à la théorie des opérateurs non bornés et résolvante.
- **[Jalon 108](jalon-108/Jalon%20108%20%28Livrable%20IA%29.md)** : Livrable IA T9 : Modélisation de l'opérateur d'Attention de la structure Transformer sous forme d'opérateur intégral borné sur un espace hilbertien.

</details>

<details>
<summary><b>Trimestre 10 : géométrie différentielle et calcul des variations</b></summary>
<br>

- **[Jalon 109](jalon-109/Jalon%20109%20%28Topologie%20des%20sous-vari%C3%A9t%C3%A9s%20de%20-mathbb%7BR%7D%5En-%29.md)** : Topologie des sous-variétés de $\mathbb{R}^n$, définition par des cartes locales, des paramétrages ou des équations.
- **[Jalon 110](jalon-110/Jalon%20110%20%28Vari%C3%A9t%C3%A9s%20diff%C3%A9rentielles%20abstraites%29.md)** : Variétés différentielles abstraites, atlas, fonctions de transition (structures lisses).
- **[Jalon 111](jalon-111/Jalon%20111%20%28Applications%20diff%C3%A9rentiables%20entre%20vari%C3%A9t%C3%A9s%29.md)** : Applications différentiables entre variétés, espace tangent en un point (dérivations) et fibré tangent $TM$.
- **[Jalon 112](jalon-112/Jalon%20112%20%28Champs%20de%20vecteurs%29.md)** : Champs de vecteurs, flots locaux, courbes intégrales et crochet de Lie.
- **[Jalon 113](jalon-113/Jalon%20113%20%28Tenseurs%29.md)** : Tenseurs, formes différentielles, produit extérieur $\wedge$ et calcul de la dérivée extérieure $d$.
- **[Jalon 114](jalon-114/Jalon%20114%20%28Orientation%20des%20vari%C3%A9t%C3%A9s%20et%20int%C3%A9gration%20des%20formes%20diff%C3%A9rentielles%20%C3%A0%20support%20compact.%29.md)** : Orientation des variétés et intégration des formes différentielles à support compact.
- **[Jalon 115](jalon-115/Jalon%20115%20%28D%C3%A9monstration%20du%20th%C3%A9or%C3%A8me%20de%20Stokes%20g%C3%A9n%C3%A9ralis%C3%A9%29.md)** : Démonstration du théorème de Stokes généralisé ($\int_{\partial M} \omega = \int_M d\omega$).
- **[Jalon 116](jalon-116/Jalon%20116%20%28Vari%C3%A9t%C3%A9s%20riemanniennes%29.md)** : Variétés riemanniennes, tenseur métrique, longueur des courbes et équations des géodésiques.
- **[Jalon 117](jalon-117/Jalon%20117%20%28Calcul%20des%20variations%29.md)** : Calcul des variations, fonctionnelles, dérivation au sens de Gâteaux et équations d'Euler-Lagrange.
- **[Jalon 118](jalon-118/Jalon%20118%20%28Conditions%20d%27optimalit%C3%A9%20du%20second%20ordre%20pour%20les%20fonctionnelles%20et%20introduction%20aux%20multiplicateurs%20de%20Lagrange%20de%20dimension%20infinie.%29.md)** : Conditions d'optimalité du second ordre pour les fonctionnelles et introduction aux multiplicateurs de Lagrange de dimension infinie.
- **[Jalon 119](jalon-119/Jalon%20119%20%28Connexions%20avec%20les%20groupes%20de%20Lie%29.md)** : Connexions avec les groupes de Lie, algèbres de Lie et symétries spatiales.
- **[Jalon 120](jalon-120/Jalon%20120%20%28Livrable%20IA%29.md)** : Livrable IA T10 : Formalisation mathématique des contraintes d'invariance par translation et rotation dans le cadre du Geometric Deep Learning (Graph Neural Networks).

</details>

<details>
<summary><b>Trimestre 11 : optimisation convexe avancée et méthodes à noyaux</b></summary>
<br>

- **[Jalon 121](jalon-121/Jalon%20121%20%28Ensembles%20convexes%29.md)** : Ensembles convexes, fonctions convexes, épigraphe et propriétés de continuité des fonctions convexes.
- **[Jalon 122](jalon-122/Jalon%20122%20%28Notion%20de%20sous-gradient%29.md)** : Notion de sous-gradient, sous-différentiel $\partial f(x)$ et optimisation de fonctions non lisses.
- **[Jalon 123](jalon-123/Jalon%20123%20%28Probl%C3%A8mes%20d%27optimisation%20sous%20contraintes%29.md)** : Problèmes d'optimisation sous contraintes, lagrangien et dualité de Lagrange (problème dual).
- **[Jalon 124](jalon-124/Jalon%20124%20%28Conditions%20de%20Karush-Kuhn-Tucker%29.md)** : Conditions de Karush-Kuhn-Tucker (KKT) pour l'optimalité globale sous contraintes de qualification (Slater).
- **[Jalon 125](jalon-125/Jalon%20125%20%28Op%C3%A9rateurs%20proximaux%29.md)** : Opérateurs proximaux, théorème de Moreau-Yosida et algorithmes de descente de gradient proximale (ISTA/FISTA).
- **[Jalon 126](jalon-126/Jalon%20126%20%28Noyaux%20d%C3%A9finis%20positifs%29.md)** : Noyaux définis positifs, théorème de Mercer et construction des espaces de Hilbert à noyau reproduisant (RKHS).
- **[Jalon 127](jalon-127/Jalon%20127%20%28D%C3%A9monstration%20du%20th%C3%A9or%C3%A8me%20du%20repr%C3%A9sentant%20dans%20les%20RKHS%29.md)** : Démonstration du théorème du représentant dans les RKHS (réduction d'un problème d'optimisation infini à la dimension finie).
- **[Jalon 128](jalon-128/Jalon%20128%20%28Flots%20de%20gradient%29.md)** : Flots de gradient (Gradient Flows) : interprétation continue de la descente de gradient comme courbe de plus grande pente dans l'espace des mesures.
- **[Jalon 129](jalon-129/Jalon%20129%20%28Optimisation%20stochastique%29.md)** : Optimisation stochastique, algorithme de Robbins-Monro et critères de convergence presque sûre de la descente de gradient stochastique (SGD).
- **[Jalon 130](jalon-130/Jalon%20130%20%28Regularisation%20implicite%20de%20la%20descente%20de%20gradient%20dans%20les%20modeles%20sur-parametres%29.md)** : Régularisation implicite de la descente de gradient dans les modèles sur-paramétrés.
- **[Jalon 131](jalon-131/Jalon%20131%20%28Algorithmes%20d%27optimisation%20de%20second%20ordre%20en%20grande%20dimension%29.md)** : Algorithmes d'optimisation de second ordre en grande dimension (quasi-Newton, L-BFGS).
- **[Jalon 132](jalon-132/Jalon%20132%20%28Livrable%20IA%29.md)** : Livrable IA T11 : Codage complet en Python pur d'un solveur de point proximal sous contraintes KKT strictes pour l'élagage théorique (pruning) de réseaux profonds.

</details>

<details>
<summary><b>Trimestre 12 : théorie de l'apprentissage statistique</b></summary>
<br>

- **[Jalon 133](jalon-133/Jalon%20133%20%28Modele%20PAC%29.md)** : Modèle PAC (Probably Approximately Correct), risque empirique vs risque réel.
- **[Jalon 134](jalon-134/Jalon%20134%20%28Complexite%20des%20classes%20de%20fonctions%29.md)** : Complexité des classes de fonctions, processus empiriques et inégalités de concentration maximales.
- **[Jalon 135](jalon-135/Jalon%20135%20%28Complexite%20de%20Rademacher%29.md)** : Complexite de Rademacher, symétrisation et bornes de généralisation basées sur Rademacher.
- **[Jalon 136](jalon-136/Jalon%20136%20%28Theorie%20de%20Vapnik-Chervonenkis%29.md)** : Théorie de Vapnik-Chervonenkis, fonction de croissance, dimension VC d'un espace d'hypothèses et lemme de Sauer.
- **[Jalon 137](jalon-137/Jalon%20137%20%28Preuve%20des%20bornes%20de%20generalisation%20universelles%20de%20Vapnik%20via%20la%20dimension%20VC%29.md)** : Preuve des bornes de generalisation universelles de Vapnik via la dimension VC
- **[Jalon 138](jalon-138/Jalon-138%20%28In%C3%A9galit%C3%A9s%20de%20concentration%20avanc%C3%A9es%29.md)** : Inégalités de concentration avancées, inégalité de McDiarmid (différences bornées) et entropie de concentration. 🔥 **Enrichi** *(10 Exos + 5 TP)*
- **[Jalon 139](jalon-139/Jalon-139_Notion_de_stabilite_algorithmique.md)** : Notion de stabilité algorithmique (Bousquet-Elisseeff) et son lien direct avec la capacité de généralisation. 🔥 **Enrichi** *(10 Exos + 5 TP)*
- **[Jalon 140](jalon-140/Jalon-140.md)** : Classifieur de Bayes optimal, fonctions de perte de substitution (Surrogate losses) et consistance de la minimisation du risque empirique. 🔥 **Enrichi** *(10 Exos + 5 TP)*
- **[Jalon 141](jalon-141/Jalon-141.md)** : Théorèmes de Glivenko-Cantelli généralisés pour les classes de fonctions VC. 🔥 **Enrichi** *(10 Exos + 5 TP)*
- **[Jalon 142](jalon-142/Jalon-142.md)** : Processus de décision de Markov (MDP) sur des espaces d'états continus, opérateurs de contraction de Bellman.
- **[Jalon 143](jalon-143/Jalon-143.md)** : Théorie spectrale des graphes, laplacien combinatoire, laplacien normalisé et étude des coupures optimales (Min-Cut). 🔥 **Enrichi** *(10 Exos + 5 TP)*
- **[Jalon 144](jalon-144/Jalon-144.md)** : Le phénomène de double descente : analyse de la rupture de la théorie statistique classique (compromis biais-variance) dans le régime sur-paramétré. 🔥 **Enrichi** *(10 Exos + 5 TP)*
- **[Jalons 145 à 152](jalon-145-152/Jalons%20145%20%C3%A0%20152%20%28R%C3%A9daction%20d%27un%20article%20de%20recherche%20th%C3%A9orique%20de%20synth%C3%A8se%20analysant%20les%20garanties%20de%20g%C3%A9n%C3%A9ralisation%20PAC%20d%27une%20couche%20d%27attention%20multi-t%C3%AAtes.%29.md)** : Rédaction d'un article de recherche théorique de synthèse analysant les garanties de généralisation PAC d'une couche d'attention multi-têtes.
- **[Jalons 153 à 156](jalon-153-156/Jalons%20153%20%C3%A0%20156%20%28Synth%C3%A8se%20finale%29.md)** : Synthèse finale, structuration de vos notes Obsidian en un graphe de connaissances unifié, et tournage de la série de vidéos YouTube clôturant le cycle d'études.

</details>

---

## 🛠️ Utilisation des Scripts d'Administration

### 1. Génération / Initialisation du Vault
Pour regénérer l'architecture par défaut du vault ou créer de nouveaux jalons squelettes :
```bash
python3 generate_jalons.py
```

### 2. Validation des Liens
Pour s'assurer que le graphe de concepts et les liens bidirectionnels ne contiennent aucune régression, lancez la suite de tests unitaires :
```bash
python3 -m unittest test_generate_jalons.py
```

---

## 📝 Historique & Avancement
- [2026-06-29] : Upsert du Jalon 12 - Livrable IA. Status: Terminé.
### 2026-06-25-audit
- [[#2026-06-25-audit|2026-06-25]] : [Audit & Weekly Compilation] - Jalon 5 - Applications, injections, surjections, bijections et composition de fonctions. Fichiers Obsidian .md mis à jour, intégration des figures TikZ et génération du polycopié PDF d'étude. Statut : Validé et Fixé.
- [2026-06-24] : Audit & Auto-correction du Jalon 4 - Théorie des ensembles. Statut : Validé et Fixé. Prêt pour le jalon suivant.
- [2026-06-24] : Upsert du Jalon 10 - Changements de base. Status: Terminé.
- [2026-06-18] : Audit & Auto-correction du Jalon 3 - Quantification. Statut : Validé et Fixé. Prêt pour le jalon suivant.

- [2026-06-20] : Audit & Auto-correction du Jalon 3 - Quantification. Statut : Validé et Fixé. Prêt pour le jalon suivant.
Le cursus est enrichi jalon par jalon de manière progressive :
- [2026-06-21] : Audit & Auto-correction du Jalon 3 - Quantification. Statut : Validé et Fixé. Prêt pour le jalon suivant.
- [2026-06-18] : Upsert du Jalon 7 - Espaces vectoriels abstraits. Status: Terminé.
- [2026-06-17] : Upsert du Jalon 6 - Relations d'équivalence. Status: Terminé.
- [2026-06-16] : Upsert du Jalon 5 - Applications. Status: Terminé.
- [2026-06-14] : Audit & Auto-correction du Jalon 1 - Logique formelle. Statut : Validé et Fixé. Prêt pour le jalon suivant.
- **Dernier Jalon Enrichi** : [Jalon 143](jalon-143/Jalon-143.md) (Cours complet, 10 exercices avancés, 5 TP d'implémentation pure Python).
- [2026-06-06] : Upsert du Jalon 140 - Classifieur de Bayes optimal. Status: Terminé.
- [2026-06-07] : Audit & Auto-correction du Jalon 141 - Théorèmes de Glivenko-Cantelli généralisés pour les classes de fonctions VC. Statut : Validé et Fixé. Prêt pour le jalon suivant.
- [2026-06-08] : Audit & Auto-correction du Jalon 142 - Processus de décision de Markov. Statut : Validé et Fixé. Prêt pour le jalon suivant.
- [2026-06-09] : Upsert du Jalon 143 - Théorie spectrale des graphes. Status: Terminé.
- [2026-06-09] : Audit & Auto-correction du Jalon 143 - Théorie spectrale des graphes. Statut : Validé et Fixé. Prêt pour le jalon suivant.
- [2026-06-09] : Upsert du Jalon 16 - Séries numériques à termes positifs. Status: Terminé.
- [2026-06-10] : Upsert du Jalon 144 - Le phénomène de double descente. Status: Terminé.
- [2026-06-10] : Audit & Auto-correction du Jalon 144 - Le phénomène de double descente. Statut : Validé et Fixé. Prêt pour le jalon suivant.
- [2026-06-13] : Audit & Auto-correction du Jalon 145-152 - Rédaction d'un article de recherche théorique de synthèse analysant les garanties de généralisation PAC d'une couche d'attention multi-têtes. Statut : Validé et Fixé. Prêt pour le jalon suivant.
- **Date de mise à jour** : 2026-06-13
- [2026-06-10] : Upsert du Jalon 2 - Méthodes de raisonnement. Status: Terminé.
- [2026-06-12] : Upsert du Jalon 3 - Quantification. Status: Terminé.
- [2026-06-12] : Audit & Auto-correction du Jalon 1 - Logique formelle. Statut : Validé et Fixé. Prêt pour le jalon suivant.
- [2026-06-17] : Audit & Auto-correction du Jalon 2 - Méthodes de raisonnement. Statut : Validé et Fixé. Prêt pour le jalon suivant.
- [2026-06-20] : Upsert du Jalon 8 - Applications linéaires. Status: Terminé.
- [2026-06-22] : Upsert du Jalon 9 - Calcul matriciel. Status: Terminé.

- [2026-06-25] : Upsert du Jalon 11 - Formes linéaires. Status: Terminé.
