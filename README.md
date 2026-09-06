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

## Installation ChatGPT / Claude

### Méthode recommandée — `skill.zip`

1. Télécharger **[`skill.zip`](./skill.zip)** depuis la racine de ce dépôt. Le même binaire versionné est conservé dans [`releases/v1.3.0/skill.zip`](./releases/v1.3.0/skill.zip).
2. Dans ChatGPT : ouvrir **Plugins > Compétences > Créer > Importer depuis votre ordinateur**, puis sélectionner `skill.zip`.
3. Dans Claude.ai : ouvrir **Settings > Capabilities > Skills**, puis importer le même `skill.zip`.

Cette méthode est la méthode de distribution de référence pour cette release.

### Installation depuis l’URL du dépôt

Vous pouvez également essayer dans un chat :

`Installe la skill https://github.com/maximatique/CharlyNE`

Cette forme dépend des capacités disponibles dans le produit et de ses accès au dépôt ; elle ne doit pas être considérée comme la méthode garantie d’installation. Si l’installation directe depuis l’URL n’est pas proposée, utiliser `skill.zip`.

L’archive conserve le dossier racine `charly-coach-militant-ne/` et le champ `name: charly-coach-militant-ne`. Le nom visible reste **CharlyNé**. Les mises à jour doivent conserver cette identité technique afin d’éviter la création d’une Skill parallèle.

## Intégrité du package

- Taille : **29 024 octets**
- SHA-256 : `924383a2d4969004671e4849c0cacd82b5cafea94720a76e65026870ea854a32`
- 11 fichiers dans une racine unique `charly-coach-militant-ne/`
- package racine et package versionné strictement identiques

Le rapport détaillé est disponible dans [`releases/v1.3.0/validation-report.json`](./releases/v1.3.0/validation-report.json).

## Structure

- `src/skill/` : source de la Skill autonome.
- `src/kb/` : KB runtime canonique générée depuis l’ontologie maître.
- `scripts/build_skill_release.py` : reconstruction déterministe et contrôles de la release.
- `tests/reference_tests.jsonl` : tests de référence de la release courante.
- `releases/v1.3.0/` : package installable, notes et rapport de validation.
- `src/project/` : historique conservé ; hors périmètre de la release v1.3.0.

## Fiabilité

La doctrine et les connaissances politiques sont produites depuis la chaîne de vérité du Studio. Les éléments `ARBITRATION_REQUIRED` restent exclus du runtime. La validation technique du package ne remplace pas la relecture juridique prévue par la spécification.
