# Charly — Coach militant Nouvelle Énergie

Source de distribution de Charly.

## Version courante

- Spécification : v1.2
- Ontologie logique : 0.2.0
- Date de build : 2026-09-06
- Fiches runtime ACTIVE : 98
- Skill ChatGPT/Codex : validée par le validateur Skill
- Package Projet : commun ChatGPT / Claude
- Tests de référence : 30/30
- KB Projet / fallback Skill : identité d’octets vérifiée dans le build validé

## Structure

- `src/skill/` : adaptateur Skill ChatGPT/Codex.
- `src/project/` : adaptateurs Projet ChatGPT et Claude.
- `src/kb/` : KB runtime canonique commune.
- `tests/` : tests de référence.
- `releases/v1.2/validation-report.json` : rapport de validation déterministe.
- `releases/v1.2/RELEASE.md` : note de release.

`src/kb/charly_knowledge.jsonl.gz` est la version compressée du JSONL runtime. Les packages de distribution réinjectent ce même contenu décompressé dans la Skill et dans le Projet ; deux versions de KB ne sont jamais fusionnées.

## Statut

Version techniquement validée et approuvée pour dépôt GitHub. Les connaissances `ARBITRATION_REQUIRED` restent exclues du runtime. Le drapeau `legal_review_required=true` reste en vigueur conformément à la spécification v1.2 ; cette validation ne vaut pas relecture juridique.
