# Charly Né — Coach Nouvelle Énergie

Source de distribution de CharlyNé.

## Version courante

- Release package : v1.2.3
- Spécification : v1.2
- Ontologie logique : 0.2.0
- Date de validation : 2026-09-06
- Fiches runtime ACTIVE : 98
- Auteur : Maximatique - Bureau NÉ 13 -  Aix en Provence
- Nom visible : `CoachNé`
- Handle principal : `@charly`
- Alias : `@charlyné`, `CoachNé`, `Lisnardassistant`, `assitantné`, `Charlyne`, `coachmilitant`
- Identifiant technique immuable : `charly-coach-militant-ne`
- Skill ChatGPT/Codex : validée par le validateur Skill
- Package Projet : commun ChatGPT / Claude
- Tests de référence : 30/30
- KB Projet / fallback Skill : identité d’octets vérifiée dans le build validé

## Structure

- `src/skill/` : adaptateur Skill ChatGPT/Codex.
- `src/project/` : adaptateurs Projet ChatGPT et Claude.
- `src/kb/` : KB runtime canonique commune.
- `tests/` : tests de référence.
- `releases/v1.2/` : release historique.
- `releases/v1.2.1/` : release historique.
- `releases/v1.2.2/` : release précédente.
- `releases/v1.2.3/` : release courante.

## Invocation

Le handle principal est `@charly`. Les formes `@charlyné`, `CoachNé`, `Lisnardassistant`, `assitantné`, `Charlyne` et `coachmilitant` sont des alias d’invocation équivalents.

## Identité de mise à jour

Toute release conserve exactement le champ `name: charly-coach-militant-ne` et le dossier racine `charly-coach-militant-ne/`. Les handles et alias d’invocation n’altèrent jamais cette identité canonique et ne doivent jamais être utilisés comme nouveau `name` technique.

`src/kb/charly_knowledge.jsonl.gz` est la version compressée du JSONL runtime. Les packages de distribution réinjectent ce même contenu décompressé dans la Skill et dans le Projet ; deux versions de KB ne sont jamais fusionnées.

## Statut

Version techniquement validée. Les connaissances `ARBITRATION_REQUIRED` restent exclues du runtime. Le drapeau `legal_review_required=true` reste en vigueur conformément à la spécification v1.2 ; cette validation ne vaut pas relecture juridique.
