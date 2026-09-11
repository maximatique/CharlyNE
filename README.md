# CharlyNé — Coach Nouvelle Énergie

Dépôt de distribution et de versioning de **CharlyNé**.

## Version courante

- Release de distribution : **v1.3.1**
- KB logique : **v1.3.0**
- Nom visible : **CharlyNé**
- Handle principal : `@charly`
- Alias : `@charlyné`, `CoachNé`, `Lisnardassistant`, `assitantné`, `Charlyne`, `coachmilitant`
- Identifiant technique immuable de la Skill : `charly-coach-militant-ne`
- Spécification : v1.2
- Ontologie logique : **0.3.0**
- Auteur : Maximatique - Bureau NÉ 13 -  Aix en Provence

## Choisir son mode d’installation

### Option la plus simple — Projet par plateforme

Pour les utilisateurs qui ne maîtrisent pas les Skills, utiliser le package correspondant à la plateforme :

- **ChatGPT** : [`releases/v1.3.1/charly-chatgpt-project.zip`](./releases/v1.3.1/charly-chatgpt-project.zip)
- **Claude** : [`releases/v1.3.1/charly-claude-project.zip`](./releases/v1.3.1/charly-claude-project.zip)
- **Gemini** : [`releases/v1.3.1/charly-gemini-project.zip`](./releases/v1.3.1/charly-gemini-project.zip)

Procédure :

1. Télécharger l’archive depuis un ordinateur.
2. La décompresser.
3. Créer un Projet ChatGPT, un Projet Claude ou un Gem Gemini.
4. Copier le contenu de `INSTRUCTIONS.md` dans les instructions du Projet/Gem.
5. Ajouter les six fichiers du dossier `kb/` à la connaissance du Projet/Gem.
6. Commencer à utiliser CharlyNé.

Une fois le Projet configuré, il peut ensuite être utilisé normalement depuis mobile.

Les trois packages Projet embarquent exactement la même KB. Seules les instructions d’adaptation à la plateforme diffèrent.

### Option avancée — Skill autonome

La Skill autonome reste disponible pour les environnements qui permettent son import :

1. Télécharger [`skill.zip`](./skill.zip).
2. Importer l’archive dans la section Skills de la plateforme.
3. Utiliser CharlyNé avec `@charly`.

Le binaire de Skill de la release v1.3.1 est inchangé par rapport à v1.3.0 ; cette release ajoute principalement les packages Projet.

### Installation depuis l’URL du dépôt

Vous pouvez également essayer dans un chat :

`Installe la skill https://github.com/maximatique/CharlyNE`

Cette forme dépend des capacités disponibles dans le produit et de ses accès au dépôt ; elle ne doit pas être considérée comme une méthode garantie d’installation.

## Contenu de la KB

La KB runtime courante contient :

- 113 connaissances actives embarquées ;
- 126 relations runtime ;
- 16 sources actives ;
- 16 compétences actives ;
- 40 tests de référence pour la Skill.

Les éléments `ARBITRATION_REQUIRED` restent exclus du runtime public.

## Release v1.3.1

Cette version ajoute :

- un package Projet ChatGPT ;
- un package Projet Claude ;
- un package Gem Gemini ;
- un adaptateur Gemini ;
- un build déterministe des trois packages ;
- un rapport de validation vérifiant que la KB est identique entre les plateformes.

La doctrine et la KB logique ne changent pas par rapport à v1.3.0.

Voir [`releases/v1.3.1/RELEASE.md`](./releases/v1.3.1/RELEASE.md).

## Structure

- `src/skill/` : source de la Skill autonome.
- `src/kb/` : KB runtime canonique générée depuis l’ontologie maître.
- `src/project/` : socle et adaptateurs Projet ChatGPT / Claude / Gemini.
- `scripts/build_skill_release.py` : reconstruction déterministe de la Skill.
- `scripts/build_project_releases.py` : génération des trois packages Projet.
- `tests/reference_tests.jsonl` : tests de référence.
- `releases/v1.3.0/` : release Skill précédente.
- `releases/v1.3.1/` : release multi-plateforme Projet.

## Fiabilité

La doctrine et les connaissances politiques sont produites depuis la chaîne de vérité du Studio. Les packages de plateforme ne doivent jamais maintenir des KB divergentes. La validation technique ne remplace pas la relecture juridique prévue par la spécification.
