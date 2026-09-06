# CharlyNé — Coach Nouvelle Énergie

Dépôt de distribution et de versioning de **CharlyNé**.

## Version courante

- Release : **v1.3.0**
- Nom visible : **CharlyNé**
- Handle principal : `@charly`
- Alias : `@charlyné`, `CoachNé`, `Lisnardassistant`, `assitantné`, `Charlyne`, `coachmilitant`
- Identifiant technique immuable : `charly-coach-militant-ne`
- Spécification : v1.2
- Ontologie logique : **0.3.0**
- Package distribué : **Skill autonome** ChatGPT / Claude
- Auteur : Maximatique - Bureau NÉ 13 -  Aix en Provence

## Release v1.3.0

Cette version met de côté le packaging Projet et distribue une Skill autonome contenant sa KB runtime sous `references/kb/`.

- 118 objets dans l’ontologie maître
- 115 objets `ACTIVE`
- 3 objets `ARBITRATION_REQUIRED` exclus du runtime
- 2 méthodes techniques liées au mode Projet exclues du périmètre de cette release
- 113 connaissances actives embarquées
- 126 relations runtime
- 16 sources actives
- 16 compétences actives
- 40 tests de référence

Les principaux enrichissements concernent la décentralisation et les Provinces, l’écologie bas carbone, la politique sociale, la sécurité et la justice, l’immigration, la souveraineté technologique, la défense, la dissuasion et la doctrine internationale.

## Installation

Le package prêt à installer est : `releases/v1.3.0/skill.zip`.

L’archive conserve le dossier racine `charly-coach-militant-ne/` et le champ `name: charly-coach-militant-ne`. Une nouvelle installation de la version remplace donc la Skill précédente à identité technique constante, au lieu de créer une Skill parallèle.

## Structure

- `src/skill/` : source de la Skill autonome.
- `src/kb/` : KB runtime canonique générée depuis l’ontologie maître.
- `tests/reference_tests.jsonl` : tests de référence de la release courante.
- `releases/v1.3.0/` : package installable, notes et rapport de validation.
- `src/project/` : historique conservé ; hors périmètre de la release v1.3.0.

## Fiabilité

La doctrine et les connaissances politiques sont produites depuis la chaîne de vérité du Studio. Les éléments `ARBITRATION_REQUIRED` restent exclus du runtime. La validation technique du package ne remplace pas la relecture juridique prévue par la spécification.
