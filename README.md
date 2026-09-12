# CharlyNé — Coach Nouvelle Énergie

Dépôt de distribution et de versioning de **CharlyNé**.

## Version courante

- Release de distribution : **v1.4.0**
- KB logique : **v1.4.0**
- Spécification : **v1.3**
- Ontologie logique : **0.4.0**
- Nom visible : **CharlyNé**
- Handle principal : `@charly`
- Alias : `@charlyné`, `CoachNé`, `Lisnardassistant`, `assitantné`, `Charlyne`, `coachmilitant`
- Identifiant technique immuable de la Skill : `charly-coach-militant-ne`
- Auteur : Maximatique - Bureau NÉ 13 -  Aix en Provence

## Architecture de connaissance

CharlyNé utilise désormais deux couches complémentaires :

- **KB Core** : doctrine et connaissances consolidées, versionnées et identiques dans tous les packages ;
- **KB Live** : presse et agenda récents, stockés dans le dossier distant `ressources-live` et indexés par `manifest.json`.

La KB Live peut compléter la Core lorsqu'une information est récente, mais elle ne remplace jamais silencieusement une connaissance consolidée. Une contradiction ou une évolution potentielle doit être arbitrée lors de la consolidation.

Dossier Live : https://drive.google.com/drive/folders/1zg7b_EJLM1jpM88onu3paz0LuREu7rQ6

## Choisir son mode d’installation

### Projet par plateforme

- **ChatGPT** : [`releases/v1.4.0/charly-chatgpt-project.zip`](./releases/v1.4.0/charly-chatgpt-project.zip)
- **Claude** : [`releases/v1.4.0/charly-claude-project.zip`](./releases/v1.4.0/charly-claude-project.zip)
- **Gemini** : [`releases/v1.4.0/charly-gemini-project.zip`](./releases/v1.4.0/charly-gemini-project.zip)
- **Universal Markdown** : [`releases/v1.4.0/charly-universal-project.zip`](./releases/v1.4.0/charly-universal-project.zip)

Procédure :

1. Télécharger l’archive depuis un ordinateur.
2. La décompresser.
3. Créer le Projet/Gem correspondant.
4. Copier `INSTRUCTIONS.md` dans les instructions.
5. Ajouter les six fichiers du dossier `kb/` à la connaissance du Projet/Gem.
6. Commencer à utiliser CharlyNé.

Les quatre packages utilisent exactement la même **KB Core**. Seules les instructions d’adaptation à la plateforme diffèrent. La consultation de la KB Live dépend des capacités d’accès web/Drive disponibles dans la plateforme.

### Skill autonome

1. Télécharger [`skill.zip`](./skill.zip).
2. Importer l’archive dans la bibliothèque de Skills lorsque cette fonctionnalité est disponible.
3. Utiliser CharlyNé avec `@charly`.

L’identité technique reste `charly-coach-militant-ne`, afin qu’une mise à jour remplace la Skill existante au lieu de créer une variante parallèle.

## Contenu de la KB Core v1.4.0

- **115** connaissances actives embarquées ;
- **126** relations runtime ;
- **17** sources actives ;
- **16** compétences actives.

Les éléments `ARBITRATION_REQUIRED` restent exclus du runtime public.

Cette version intègre notamment :

- la tribune JDD du 11 septembre 2026 sur l’école ;
- l’enrichissement de `NE-EDU-001` et `NE-EDU-002` ;
- la nouvelle connaissance `NE-EDU-004` sur autorité, évaluation et différenciation des parcours ;
- la méthode `CHARLY-METH-018` pour la KB Live distante et sa consolidation périodique ;
- la spécification **v1.3** et l’ontologie **0.4.0**.

Voir [`releases/v1.4.0/RELEASE.md`](./releases/v1.4.0/RELEASE.md).

## Structure

- `src/skill/` : source de la Skill autonome ;
- `src/kb/` : KB Core runtime canonique ;
- `src/project/` : socle et adaptateurs de plateforme ;
- `scripts/` : builds déterministes ;
- `tests/` : tests de référence ;
- `releases/v1.4.0/` : packages distribuables et rapports de validation.

## Fiabilité

La chaîne de vérité reste pilotée par Charlie Studio. Les plateformes ne doivent jamais maintenir des KB doctrinales divergentes. Les faits issus de la presse restent attribués à leur source tant qu’ils ne sont pas vérifiés par une source indépendante adaptée. La validation technique ne remplace pas la relecture juridique prévue par la spécification.
