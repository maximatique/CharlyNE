# Charly — Spécification v1.4 — évolution KB Live

Statut : **préparée dans Charlie Studio** — 2026-09-12.

La spécification v1.4 industrialise la couche KB Live introduite en v1.3 sans imposer de nouvelle release à chaque changement d’actualité.

## Collecte officielle prioritaire

Ordre de découverte recommandé :

1. Agenda NÉ : https://www.unenouvelleenergie.fr/agenda/
2. Presse / médias : https://www.unenouvelleenergie.fr/actualites/dans-les-medias/
3. Actualités générales, en complément : https://www.unenouvelleenergie.fr/actualites/
4. Sources ajoutées manuellement par Charlie Studio.

## Principes d’exploitation

- La collecte est incrémentale : on ajoute les nouvelles entrées et on ne réécrit une entrée existante que si la source a réellement changé.
- La déduplication utilise en priorité l’URL canonique, puis l’empreinte de contenu et, en dernier recours, la combinaison date + titre.
- Le manifeste Live conserve les curseurs de collecte, dates de contrôle, URL canoniques, compteurs et métadonnées utiles.
- Un événement n’a pas besoin d’être marqué manuellement `PAST` : son caractère à venir, en cours ou passé est calculé à la lecture à partir de ses dates et de la date courante.
- Les ressources Live restent exploitables sans maintenance temporelle après publication.
- Les sources manuelles suivent le même schéma que les sources collectées automatiquement.

## Séparation Live / Core

La collecte quotidienne Live est indépendante de la consolidation doctrinale.

Une ressource Live ne modifie pas automatiquement la KB Core et ne déclenche pas à elle seule une release. La consolidation vers l’ontologie et la KB Core se fait périodiquement ou à la demande, uniquement lorsque l’information est pertinente pour la doctrine, le programme, les arguments ou une connaissance stable.

Une contradiction Live/Core ne doit jamais être résolue silencieusement ; elle doit être remontée lors de la consolidation et peut conduire à `ARBITRATION_REQUIRED`.

## État initial du backfill Live

Backfill réalisé le 12 septembre 2026 sur environ trois mois :

- Presse : 30 entrées, période 12 juin → 11 septembre 2026 ;
- Agenda : 20 événements, période 15 juin → 29 août 2026 ;
- manifeste distant : schéma 1.1, version Live `2026-09-12.1`.

Dossier Live : https://drive.google.com/drive/folders/1zg7b_EJLM1jpM88onu3paz0LuREu7rQ6

Le backfill Agenda initial est best-effort pour les archives anciennes ; les collectes incrémentales ultérieures doivent capturer les nouveaux événements au moment où ils apparaissent.

## Versioning

Le versioning Live est indépendant du versioning Core et des releases de distribution.

Exemple :

- Release distribuée : `v1.4.0`
- KB Core : `0.4.0`
- KB Live : `2026-09-12.1`, puis versions quotidiennes ultérieures.

Cette séparation est volontaire : l’actualité peut évoluer quotidiennement sans imposer de réinstallation aux militants.
