# Release v1.2.1 — 2026-09-06

## Statut

Version techniquement validée.

## Identité de la Skill

- Nom visible : `CoachNé`.
- Alias conversationnel : `CharlyNé`.
- Appel explicite reconnu : `@CoachNé`.
- Identifiant canonique immuable : `charly-coach-militant-ne`.
- Dossier racine du ZIP : `charly-coach-militant-ne/`.

Le changement de nom visible ne modifie pas l'identité technique. Les releases futures doivent conserver exactement le même champ `name` dans `SKILL.md` et le même dossier racine. Aucun package `coach-ne`, `charly-ne` ou autre identifiant parallèle ne doit être distribué.

## Contrôles effectués

- Validateur Skill : OK.
- Structure ZIP : OK.
- Nom canonique stable : OK.
- Nom visible `CoachNé` : OK.
- Alias `CharlyNé` et `@CoachNé` présents dans la description de déclenchement : OK.
- KB Projet / fallback Skill : identité d’octets vérifiée.
- 30/30 tests de référence validés dans la release de base v1.2 ; aucun contenu doctrinal n'est modifié par v1.2.1.

## Empreintes des artefacts locaux validés

- `skill.zip` : `82494c82023630cc48b3d43b23f25b5dc846a1501c4b1b21e97c89f23078c3d1`
- `charly-project-gpt-claude-v1.2.1.zip` : `845a533e90d2193f66f367c20b90c7a42254aa63d03196a59f19ea49e7495819`

Le drapeau `legal_review_required=true` reste présent dans le manifeste runtime ; cette validation ne vaut pas relecture juridique.
