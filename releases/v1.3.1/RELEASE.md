# CharlyNé — Release v1.3.1

Date : 11 septembre 2026

## Objet

Cette release ajoute des packages Projet distincts par plateforme afin de simplifier l’installation pour les utilisateurs qui ne souhaitent pas ou ne peuvent pas installer une Skill.

La KB logique reste inchangée par rapport à v1.3.0 : même ontologie 0.3.0, mêmes 113 connaissances runtime, 126 relations, 16 sources et 16 compétences. Aucun contenu doctrinal n’est modifié dans cette release.

## Livrables

- `skill.zip` : Skill autonome inchangée par rapport à v1.3.0 ;
- `charly-chatgpt-project.zip` : package Projet ChatGPT ;
- `charly-claude-project.zip` : package Projet Claude ;
- `charly-gemini-project.zip` : package Gem Gemini ;
- `project-validation-report.json` : contrôles d’intégrité et empreintes SHA-256.

## Principe de distribution

Les trois packages Projet embarquent strictement la même KB. Seul `INSTRUCTIONS.md` diffère selon la plateforme, car il fusionne le socle commun avec l’adaptateur ChatGPT, Claude ou Gemini.

Chaque archive contient :

- `README.md` ;
- `INSTRUCTIONS.md` ;
- `kb/charly_knowledge.jsonl` ;
- `kb/charly_competences.jsonl` ;
- `kb/charly_relations.jsonl` ;
- `kb/charly_sources.jsonl` ;
- `kb/charly_schema.json` ;
- `kb/charly_kb_manifest.json`.

## Installation recommandée

Faire de préférence l’installation depuis un ordinateur : télécharger l’archive correspondant à la plateforme, la décompresser, créer un Projet ou un Gem, copier le contenu de `INSTRUCTIONS.md` dans les instructions et charger les six fichiers du dossier `kb/` comme base documentaire.

Une fois configuré, CharlyNé peut ensuite être utilisé normalement depuis mobile.

## Identité

- Nom visible : CharlyNé
- Handle principal : `@charly`
- Identifiant technique Skill : `charly-coach-militant-ne`
- Auteur : Maximatique - Bureau NÉ 13 -  Aix en Provence

## Validation

Le build vérifie que les trois packages Projet utilisent la même KB et génère les SHA-256 de chaque archive. La validation technique ne remplace pas la relecture juridique prévue par la spécification.
