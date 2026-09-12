# CharlyNé v1.4.0

Date : 12 septembre 2026

## Contenu

Cette release aligne la distribution sur la spécification **v1.3** et l'ontologie **0.4.0**.

Elle introduit l'architecture **KB Core + KB Live** : la Core reste la doctrine consolidée commune à toutes les plateformes ; la Live permet de consulter Presse et Agenda récents via le `manifest.json` distant lorsque la plateforme dispose de l'accès nécessaire.

La release intègre également la tribune JDD du 11 septembre 2026 sur l'école : enrichissement de `NE-EDU-001` et `NE-EDU-002`, création de `NE-EDU-004`, et ajout de la méthode `CHARLY-METH-018`.

## Runtime

- 115 connaissances actives embarquées
- 126 relations runtime
- 17 sources actives
- 16 compétences actives
- 3 connaissances `ARBITRATION_REQUIRED` exclues du runtime public

## Packages

- `skill.zip`
- `charly-chatgpt-project.zip`
- `charly-claude-project.zip`
- `charly-gemini-project.zip`
- `charly-universal-project.zip`

Les packages Projet embarquent exactement la même KB Core. La validation technique ne remplace pas la relecture juridique prévue par la spécification.
