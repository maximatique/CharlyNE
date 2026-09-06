# Règles runtime et sélection de la KB

1. Chercher d'abord un fichier de Projet nommé `charly_kb_manifest.json` associé à `charly_knowledge.jsonl`.
2. Si un manifeste de Projet Charly est présent, utiliser exclusivement cette KB de Projet pour toute la conversation. Ignorer la KB fallback embarquée dans la Skill, même si sa version est différente.
3. Si aucun package Projet Charly n'est présent, utiliser la KB fallback `references/kb/` de la Skill.
4. Ne jamais fusionner, compléter ni dédupliquer deux versions de KB différentes.
5. Lire `charly_schema.json` avant d'interpréter les clés compactes JSON/JSONL.
6. Charger uniquement les entrées pertinentes par ID, branche, thème, sous-thème ou termes de la demande.
7. Les fichiers runtime ne contiennent que les connaissances `ACTIVE`; une absence documentaire doit conduire à `NON_DOCUMENTED`, pas à une invention.
8. Utiliser `charly_sources.jsonl` pour résoudre les identifiants de source et produire le format de sourcing obligatoire.
