# CoachNé / CharlyNé — Nouvelle Énergie

Source de distribution de CharlyNé.

## Version courante

- Release package : v1.2.1
- Spécification : v1.2
- Ontologie logique : 0.2.0
- Date de validation : 2026-09-06
- Fiches runtime ACTIVE : 98
- Nom visible : `CoachNé`
- Alias conversationnel : `CharlyNé`
- Appel explicite : `@CoachNé`
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
- `releases/v1.2/` : release précédente.
- `releases/v1.2.1/` : release courante.

## Identité de mise à jour

Toute release conserve exactement le champ `name: charly-coach-militant-ne` et le dossier racine `charly-coach-militant-ne/`. Le nom visible `CoachNé` et l'alias `CharlyNé` n'altèrent jamais cette identité canonique. Ne jamais publier une variante sous `coach-ne`, `charly-ne` ou un autre `name`, car elle constituerait une Skill distincte.

`src/kb/charly_knowledge.jsonl.gz` est la version compressée du JSONL runtime. Les packages de distribution réinjectent ce même contenu décompressé dans la Skill et dans le Projet ; deux versions de KB ne sont jamais fusionnées.

## Statut

Version techniquement validée. Les connaissances `ARBITRATION_REQUIRED` restent exclues du runtime. Le drapeau `legal_review_required=true` reste en vigueur conformément à la spécification v1.2 ; cette validation ne vaut pas relecture juridique.
