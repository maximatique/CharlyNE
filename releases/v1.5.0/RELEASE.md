# CharlyNé v1.5.0

Date : 22 octobre 2026

## Contenu

Cette release enrichit la KB Core sans modifier le fonctionnement de CharlyNé : même spécification **v1.3**, mêmes instructions, même socle, même schéma, mêmes compétences, même architecture **KB Core + KB Live**. L'ontologie logique passe en **0.5.0**.

Le contenu ajouté provient exclusivement des pages publiées sur le site officiel de Nouvelle Énergie : programme et pages thématiques, 112 fiches « Questions », *Livre noir de la bureaucratie*, livrets Agriculture et Santé.

- 74 connaissances créées : débureaucratisation (plan des cent jours, silence vaut accord, droit à l'erreur…), justice et exécution des peines, sécurité, immigration, économie et travail, retraites, finances publiques, Europe et international, écologie, santé, agriculture, éducation, positionnement politique et argumentaires de réponse aux objections.
- 42 connaissances existantes enrichies (mécanismes, chiffres, calendriers), avec incrément de version et date de mise à jour.
- Sources `SRC-FAQ-2026`, `SRC-PROG-2026`, `SRC-AGRI-2026` et `SRC-SANTE-2026` actualisées.
- 126 relations ajoutées avec les types existants.

Les écarts entre le site et des connaissances existantes n'ont pas été tranchés : ils sont signalés pour arbitrage et les connaissances concernées sont restées inchangées sur ces points.

## Runtime

- 189 connaissances actives embarquées
- 252 relations runtime
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
