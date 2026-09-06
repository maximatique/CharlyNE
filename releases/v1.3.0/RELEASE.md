# CharlyNé v1.3.0 — Skill autonome

Date : 6 septembre 2026

## Portée

Release majeure centrée sur la distribution **Skill autonome**. L’aspect Projet ChatGPT/Claude est volontairement hors périmètre de cette version.

## Identité

- Nom visible : **CharlyNé**
- Handle principal : `@charly`
- Alias : `@charlyné`, `CoachNé`, `Lisnardassistant`, `assitantné`, `Charlyne`, `coachmilitant`
- Identifiant technique conservé : `charly-coach-militant-ne`
- Auteur : Maximatique - Bureau NÉ 13 -  Aix en Provence

## KB et ontologie

- Ontologie logique : **0.3.0**
- 118 objets dans l’ontologie
- 115 objets `ACTIVE`
- 3 objets `ARBITRATION_REQUIRED`, exclus du runtime
- 2 méthodes techniques Projet `ACTIVE` exclues de cette release Skill par périmètre (`CHARLY-METH-015`, `CHARLY-METH-016`)
- 113 connaissances actives embarquées dans la Skill
- 126 relations runtime
- 16 sources actives
- 16 compétences actives

## Enrichissements majeurs

Ajout ou consolidation de la décentralisation et des Provinces, de la doctrine écologique bas carbone, de l’allocation sociale unique, des aides aux entreprises, de la réduction des fonctions administratives, de l’islamisme radical, de la justice des mineurs, de la souveraineté technologique, de la défense, de la dissuasion et de la doctrine internationale.

Les fiches Éducation, Sécurité, Justice, Immigration, Nucléaire, Europe, Innovation et Réindustrialisation ont également été enrichies à partir des sources officielles et du site Nouvelle Énergie.

## Distribution

Le fichier `skill.zip` est le package d’installation. Il contient une seule Skill, avec `SKILL.md`, les métadonnées ChatGPT et la KB autonome sous `references/kb/`. Aucun XLS/XLSX, arbitrage interne, backlog ou package Projet n’est distribué.

Le même binaire est publié à deux emplacements :
- `/skill.zip`
- `/releases/v1.3.0/skill.zip`

## Validation finale

- Validateur Skill : PASS
- Contrôles structurels et référentiels : PASS
- Tests de référence : 40/40 identifiants attendus présents dans le runtime
- Nom visible `CharlyNé` vérifié
- Identité technique stable vérifiée
- 11 fichiers, racine unique `charly-coach-militant-ne/`
- Taille : 29 024 octets
- SHA-256 : `924383a2d4969004671e4849c0cacd82b5cafea94720a76e65026870ea854a32`
- Build reproductible via `scripts/build_skill_release.py`

La relecture juridique prévue par la spécification reste une étape de gouvernance distincte de la validation technique de la Skill.
