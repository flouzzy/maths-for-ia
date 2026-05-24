# Jalons de Mathématiques pour l'Intelligence Artificielle

Ce dépôt contient un script permettant de générer automatiquement un ensemble de fiches de notes (au format Markdown) destinées à être utilisées comme coffre (*vault*) dans [Obsidian](https://obsidian.md/). Ce projet modélise un programme de mathématiques sur 3 ans, spécifiquement orienté vers les fondements théoriques de l'intelligence artificielle.

## Objectif du Projet

Le projet génère des "Jalons" d'apprentissage répartis sur trois années de cursus :
- **Année 1 : Le socle des fondations et l'analyse réelle** (Logique, algèbre linéaire, analyse réelle, réduction d'endomorphismes, etc.)
- **Année 2 : L'abstraction topologique et la théorie de la mesure** (Topologie générale, théorie de la mesure, intégration de Lebesgue, espaces $L^p$, probabilités axiomatiques, etc.)
- **Année 3 : Le niveau master (analyse fonctionnelle, géométrie et apprentissage)** (Analyse fonctionnelle, géométrie différentielle, optimisation convexe avancée, théorie de l'apprentissage statistique, etc.)

Ces notes sont structurées et interconnectées. Elles incluent des liens de navigation vers les jalons précédents et suivants, ainsi que des liens sémantiques automatiques entre les concepts mathématiques transversaux.

- **`Tableau de bord.md`** : Un index global interactif (sous forme de checklist) permettant de suivre votre progression à travers tout le cursus. Chaque jalon y est lié pour une navigation rapide.

## Fichiers Principaux

- **`generate_jalons.py`** : C'est le script principal du projet, écrit en Python. Il contient le texte source du programme complet, le découpe par années et trimestres, et génère pour chaque jalon un dossier dédié contenant la fiche principale (par exemple : `Jalon 1 (Logique formelle)/Jalon 1 (Logique formelle).md`). Cette structure permet d'organiser proprement chaque jalon en y ajoutant des ressources complémentaires (exercices, schémas, notes personnelles) sans encombrer la racine du dépôt.
- **`test_generate_jalons.py`** : Contient la suite de tests unitaires du projet, permettant de vérifier la logique de création de liens inter-concepts (`generate_concept_links`) définie dans le script principal.
- **`generate_jalons.ps1`, `generate_index.ps1`, `git-sync.ps1`** : Scripts utilitaires PowerShell prévus pour une utilisation sous environnement Windows ou via `pwsh` pour générer des index ou automatiser certaines tâches Git.

## Historique d'enrichissement IA

- **Jalon 1** : Logique formelle, connecteurs, tables de vérité et calcul des propositions. (Enrichi le 2026-05-24)
- **Jalon 2** : Méthodes de raisonnement (implication, contraposée, l'absurde, analyse-synthèse). (Enrichi le 2026-05-24)
- **Jalon 3** : Quantification ($\forall, \exists$), ordre des quantificateurs et négation de propositions complexes. (Enrichi le 2026-05-24)
- **Jalon 4** : Théorie des ensembles (ZFC), opérations sur les ensembles, ensembles des parties $\mathcal{P}(E)$. (Enrichi le 2026-05-24)
- **Jalon 5** : Applications, injections, surjections, bijections et composition de fonctions. (Enrichi le 2026-05-24)
- **Jalon 6** : Relations d'équivalence, relations d'ordre, ensembles quotients et structures de base (groupes, anneaux, corps). (Enrichi le 2026-05-24)
- **Jalon 7** : Espaces vectoriels abstraits, familles libres, familles génératrices et bases en dimension finie. (Enrichi le 2026-05-24)
- **Jalon 8** : Applications linéaires, noyau (ker), image (Im) et démonstration du théorème du rang. (Enrichi le 2026-05-24)
- **Jalon 9** : Calcul matriciel, opérations, inversibilité et représentations des applications linéaires. (Enrichi le 2026-05-24)

## Comment Générer les Notes

Assurez-vous d'avoir Python 3 installé. Pour générer ou mettre à jour l'ensemble des notes Markdown, il vous suffit d'exécuter le script Python depuis la racine du dépôt :

```bash
python3 generate_jalons.py
```

Une fois la commande exécutée, le script créera de nombreux dossiers correspondant au cursus. Vous pouvez ensuite ouvrir le répertoire racine du projet directement dans Obsidian pour consulter et lier vos notes. Obsidian détectera automatiquement les fichiers Markdown à l'intérieur des dossiers.

## Comment Lancer les Tests

Le projet utilise le framework standard `unittest` de Python. Pour lancer les tests et s'assurer que le script de liens conceptuels fonctionne correctement sans introduire de régression, exécutez la commande suivante :

```bash
python3 -m unittest test_generate_jalons.py
```
