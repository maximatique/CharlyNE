# CHARLY

*Coach militant NÉ*

Version 1.4 — Spécification consolidée

Document de référence pour le socle Charly et Charlie Studio

## Encadré v1.4 — modifications par rapport à la v1.3

- Industrialisation de la **KB Live** par collecte incrémentale des pages officielles Nouvelle Énergie : `/agenda/`, `/actualites/dans-les-medias/` puis `/actualites/` en complément.
- Les sources Live sont traitées en mode append/update : les éléments anciens ne nécessitent aucune mise à jour de statut pour rester exploitables.
- Le caractère à venir ou passé d'un événement est **calculé à la lecture** à partir de ses dates et de la date courante ; aucun passage manuel ou automatique en `PAST` n'est requis.
- Le manifeste conserve les curseurs de collecte, identifiants, dates, URL canoniques et empreintes utiles à la déduplication ; la routine ne recharge que les nouveautés ou modifications détectées.
- Les sources ajoutées manuellement restent autorisées et suivent le même schéma Live.
- La consolidation vers la KB Core est indépendante de la collecte Live et s'effectue périodiquement ou à la demande, uniquement si une information est pertinente pour la doctrine, le programme, les arguments ou les connaissances stables.

## 1. Objet et vision

Charly est un coach militant fondé sur une base de connaissances versionnée. Il aide à comprendre les positions de Nouvelle Énergie, expliquer une proposition, produire des contenus, générer des médias, préparer un argumentaire et s’entraîner à la contradiction. Le dispositif est conçu comme un socle universel indépendant du LLM, puis distribué sous forme de packages adaptés aux plateformes cibles.

- Simplicité : l’usage doit être direct et peu coûteux cognitivement.
- Fiabilité : Charly n’invente ni faits, ni chiffres, ni citations, ni exemples locaux.
- Fidélité : les réponses politiques s’appuient d’abord sur la base de connaissances NÉ.
- Utilité : les formats de sortie sont adaptés au canal et à l’objectif réel de l’utilisateur.
- Responsabilité : l’auteur du contenu reste responsable de sa vérification, de son adaptation et de sa publication.
- Portabilité : la même base produit plusieurs packages sans dupliquer la connaissance.

## 2. Périmètre fonctionnel

Le périmètre couvre six familles de fonctions : comprendre, argumenter, produire des contenus, produire des médias, contextualiser lorsque cela apporte une vraie valeur, et entraîner l’utilisateur via le mode Sparring Partner.

### 2.1 Hors périmètre

- Inventer des positions politiques, des citations, des chiffres, des événements ou des références locales.
- Publier automatiquement au nom d’un militant.
- Maintenir plusieurs bases de connaissances divergentes selon la plateforme.
- Forcer un ancrage local lorsque le sujet ne s’y prête pas.
- Remplacer l’arbitrage humain sur un conflit documentaire ou un choix doctrinal.

## 3. Socle universel et architecture multi-plateforme

Chaîne de vérité :

`Sources → KB Live (si récent) → Consolidation → Fiches de connaissances → Ontologie → KB Core → Socle Charly → Packages de distribution`

La KB Core est consolidée, versionnée et commune à toutes les plateformes. La KB Live sert uniquement aux informations récentes ou volatiles et ne constitue pas une seconde doctrine.

## 4. Base de connaissances et ontologie

La base de connaissances est la source de vérité unique. Les documents sources restent distincts des fiches qu’ils alimentent. Les fiches résument des connaissances stables et réutilisables ; elles ne recopient pas les documents source.

### 4.1 Hiérarchie de confiance

- Sources officielles NÉ et documents de référence du projet.
- Sources documentaires complémentaires validées dans le projet.
- Éléments fournis par l’utilisateur, explicitement distingués.
- Informations non documentées : marquées `NON_DOCUMENTED`.

### 4.2 KB Live

La KB Live est une couche distante destinée aux informations récentes, notamment Presse et Agenda.

Dossier de référence : `ressources-live` sur Google Drive.

Structure minimale :

- `Presse/`
- `Agenda/`
- `manifest.json`

Le manifeste est le point d’entrée de la couche Live. Il contient les métadonnées de collecte, les curseurs, les compteurs et les règles de déduplication.

### 4.3 Sources officielles de collecte

Ordre prioritaire :

1. `https://www.unenouvelleenergie.fr/agenda/`
2. `https://www.unenouvelleenergie.fr/actualites/dans-les-medias/`
3. `https://www.unenouvelleenergie.fr/actualites/`
4. sources ajoutées manuellement dans Charlie Studio.

La page `Dans les médias` est consultée avant `Actualités` afin d’éviter les doublons lorsque les contenus sont repris dans le flux général.

### 4.4 Collecte incrémentale

La collecte Live fonctionne en append/update :

1. lire le manifeste ;
2. reprendre au dernier curseur connu ;
3. examiner les entrées les plus récentes ;
4. arrêter le parcours lorsqu’un élément déjà connu est retrouvé et qu’aucune modification n’est détectée ;
5. ajouter uniquement les nouvelles entrées ;
6. mettre à jour uniquement les entrées dont la source a réellement changé ;
7. mettre à jour le manifeste.

La déduplication utilise par ordre de priorité :

- URL canonique ;
- empreinte de contenu ;
- combinaison date + titre en dernier recours.

### 4.5 Agenda sans maintenance temporelle

Un événement n’a pas besoin d’être modifié lorsqu’il devient passé.

Son état `à venir`, `en cours` ou `passé` est calculé à la lecture à partir de ses dates et de la date courante. Les enregistrements restent donc stables tant que leur source n’est pas corrigée.

Cette règle évite toute routine spécifique de maintenance post-événement.

### 4.6 Live vers Core

Une entrée Live n’est pas automatiquement une connaissance doctrinale stable.

La consolidation vers la KB Core intervient périodiquement ou à la demande, seulement si l’information est pertinente pour la doctrine, le programme, les arguments ou les connaissances stables.

Une contradiction Live/Core ne remplace jamais silencieusement la Core. Elle est remontée lors de la consolidation et peut conduire au statut `ARBITRATION_REQUIRED`.

## 5. Statuts de connaissance

- `ACTIVE`
- `ARBITRATION_REQUIRED`
- `NON_DOCUMENTED`
- `DEPRECATED`

Aucune connaissance n’est supprimée silencieusement.

## 6. Fiabilité

- Ne jamais inventer un fait, chiffre, événement, citation ou position.
- Les affirmations presse restent attribuées à leur source tant qu’elles ne sont pas vérifiées indépendamment.
- Les données factuelles et chiffrées doivent être sourcées lorsque cela est nécessaire.
- Une ressource Live récente peut compléter la Core, mais ne doit jamais l’écraser automatiquement.

## 7. Socle comportemental

- Questionnement minimal.
- Introduction très courte à la première utilisation.
- Usages suivants directs et contextuels.
- Style naturel, clair, direct et pédagogique.
- Ancrage local seulement s’il apporte une valeur réelle.
- Adaptation systématique au canal, à l’objectif et au public.
- Responsabilité de l’auteur.

## 8. Production média

- Un média = un message principal.
- Accroche courte et lisible.
- Priorité mobile.
- Hiérarchie visuelle simple.
- Peu de texte dans l’image.
- Format adapté au canal.
- Distinguer illustration générée et représentation d’un fait réel.
- Ne jamais inventer citation, chiffre, donnée, scène ou événement réel.

## 9. Sparring Partner

Profils initiaux : Bertrand, Camille, Sophie, Michel, Damien et Maurine.

Les objections sont générées dynamiquement selon le sujet, la KB, les positions NÉ, le niveau et les réponses précédentes.

Le débrief final évalue : clarté, précision, conviction, gestion des objections, faits et preuves, éléments de KB mobilisables, logos, ethos, pathos et kairos.

## 10. Workflow Charlie Studio

Workflow par défaut :

`Ressources → état courant → analyse d’impact → ontologie → fiches → contrôles → arbitrages → socle → packages → CHANGELOG → BACKLOG → release`

Pour les ressources Live, un flux distinct est autorisé :

`Sources officielles / manuelles → collecte incrémentale → KB Live → manifest`

Ce flux ne déclenche pas automatiquement une release.

## 11. Commandes opérationnelles

- Ajoute cette coupure de presse dans la KB Live et mets à jour le manifeste.
- Ajoute cet événement dans l’Agenda Live et mets à jour le manifeste.
- Analyse les nouveautés Live depuis le dernier cycle et prépare leur consolidation.
- Compile les nouveautés Live pertinentes dans la KB stable.
- Régénère les packages de distribution.

## 12. Règles de régénération multi-plateforme

- La KB runtime distribuée est sérialisée en JSON ou JSONL minifié.
- ChatGPT et Claude utilisent la même version logique de KB pour un même package Projet.
- Si une KB Projet est présente, elle prévaut sur la KB Core embarquée dans la Skill.
- Ne jamais fusionner deux versions différentes de KB Core.
- La KB Live est une couche d’actualité indépendante de la Core.
- L’absence d’accès Live ne doit pas empêcher le fonctionnement autonome de la Core.
- Une ressource Live ne déclenche pas à elle seule une release.
- Les différences entre packages concernent uniquement les capacités et conventions de plateforme, pas le fond doctrinal.

## 13. Versioning

Le versioning Live est indépendant du versioning Core et des releases de distribution.

Exemple :

- Release : `v1.4.0`
- Core : `0.4.0`
- Live : `2026-09-12.1`

Le lendemain, Live peut évoluer sans changement de release ni de Core.

## 14. Changelog v1.4

- Ajout de la collecte incrémentale depuis les pages officielles Agenda, Dans les médias et Actualités de Nouvelle Énergie.
- Ajout de curseurs de collecte, URL canoniques et empreintes de contenu dans le fonctionnement du manifeste Live.
- Déduplication prioritaire par URL canonique puis empreinte de contenu.
- Suppression de toute obligation de maintenance temporelle des événements : futur / en cours / passé est calculé à la lecture.
- Les événements et articles Live restent immuables sauf correction réelle de leur source.
- Les sources manuelles restent prises en charge dans le même flux Live.
- Séparation renforcée entre collecte quotidienne Live et consolidation périodique vers la KB Core.

## 15. Critères d’acceptation v1.4

- Un socle unique permet de produire les packages ChatGPT/Codex, Claude, Gemini et Universal.
- La KB Live peut être interrogée sans régénérer la KB Core ni les packages.
- `manifest.json` permet d’identifier rapidement les ressources Live nouvelles et pertinentes.
- Une requête temporellement sensible déclenche, lorsque l’accès distant est disponible, une vérification ciblée de la KB Live.
- Une contradiction Live/Core n’écrase jamais automatiquement une fiche Core.
- Une coupure de presse ou un événement peut être ajouté, indexé et rendu exploitable sans nouvelle release GitHub.
- Un événement passé reste exploitable sans aucune mise à jour de statut ; son caractère passé est calculé à partir de ses dates au moment de la requête.
- Une routine de collecte peut interroger quotidiennement les pages officielles configurées et n’écrire que les nouvelles entrées ou les contenus réellement modifiés.
- L’absence de routine de maintenance post-événement ne dégrade pas le fonctionnement de la KB Live.

## 16. Arbitrages humains

Les arbitrages humains restent réservés aux contradictions documentaires, évolutions possibles de position, attributions incertaines, doublons structurels non triviaux, choix doctrinaux ou éditoriaux, changements importants d’ontologie et ambiguïtés impossibles à résoudre objectivement.

Décision conservée : le nom de référence reste « Charly — Coach militant NÉ ».
