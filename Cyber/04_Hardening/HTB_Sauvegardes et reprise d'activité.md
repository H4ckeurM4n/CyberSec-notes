## Backup — Sauvegarde
- Un **backup** est une copie des données conservée afin de pouvoir les restaurer si les données originales deviennent indisponibles, corrompues ou détruites.
- Les sauvegardes protègent notamment contre :
    - erreur humaine ;
    - panne matérielle / système ;
    - corruption de données ;
    - cyberattaque ;
    - catastrophe naturelle.
```
Original Data
    ↓
  Backup
    ↓
Restore si perte / corruption
```

> Un backup ne supprime pas le risque d’incident : il fournit surtout une **capacité de récupération** lorsque l’incident a déjà eu un impact sur les données.
### Importance des sauvegardes
#### Protection contre la perte de données
- Une perte de données peut résulter de :
	- suppression accidentelle ;
	- panne système ;
	- attaque informatique ;
	- ransomware ;
	- corruption ;
	- destruction physique de l’infrastructure.
```
Data Loss
→ Backup disponible
→ Restore
→ réduction de l'impact
```
#### Continuité des activités - Business Continuity
- Les organisations dépendent fortement de la disponibilité de leurs données et services.
- Une perte importante peut interrompre :
    - applications métier ;
    - production ;
    - services clients ;
    - opérations internes.
- Les backups contribuent donc à la **Business Continuity** en permettant de reprendre les opérations après un incident.
#### Conformité réglementaire - Regulatory Compliance
- Certains secteurs imposent des exigences concernant :
    - sauvegarde des données ;
    - conservation ;
    - protection ;
    - capacité de restauration.
- Une stratégie correctement documentée facilite également les **audits**.
> Les exigences exactes de conservation et de sauvegarde dépendent de la réglementation et du contexte de l’organisation.
#### Customer Trust
- Une perte de données peut entraîner :
	- perte de confiance des clients ;
	- atteinte à la réputation ;
	- interruption de service ;
	- impacts financiers.
- Les sauvegardes permettent de réduire l’impact opérationnel d’un incident, même si elles ne peuvent pas empêcher à elles seules une fuite de données.
```
Backup → protège contre la perte
Backup ≠ empêche l'exfiltration
```
#### Reprise des données (Reprise après sinistre) - Disaster Recovery
- Les sauvegardes constituent un élément essentiel du **Disaster Recovery (DR)**.
- Exemples de scénarios :
```
Datacenter détruit
Cyberattaque majeure
Ransomware
Panne critique
    ↓
Backup
    ↓
Recovery
```

> **Backup ≠ Disaster Recovery** : le backup correspond principalement aux copies des données, alors que le DR englobe l’ensemble des procédures, infrastructures et priorités permettant de remettre les systèmes en fonctionnement.
### Stratégie de sauvegarde
- Une sauvegarde efficace doit être :
	- réalisée régulièrement ;
	- protégée contre les accès non autorisés ;
	- suffisamment indépendante de la production ;
	- conservée pendant une durée adaptée ;
	- **testée en restauration**.
```
Backup créé
≠ données réellement récupérables

Restore Test
→ vérifie que le backup fonctionne
```
- Une stratégie de récupération prend généralement en compte :
```
RPO → quantité maximale de données acceptable à perdre
RTO → durée maximale acceptable avant restauration
```
- Ces objectifs déterminent notamment la fréquence des backups et la rapidité attendue du processus de recovery.
## Types et Supports de Sauvegarde
### Types de sauvegarde
- Le type de sauvegarde détermine **quelles données sont copiées** et donc :
	- temps de sauvegarde ;
	- espace nécessaire ;
	- vitesse de restauration ;
	- dépendances entre backups.
<img src="../../assets/backup.png" alt="Backup" width="400">
#### Full Backup — Sauvegarde complète
- Copie **toutes les données sélectionnées**.
- Type le plus simple à restaurer.
- Inconvénients :
    - plus long à créer ;
    - consomme davantage d’espace.
```
Full Backup
→ A + B + C + D + E
```
- Avantages :
	- restauration simple ;
	- peu de dépendances.
#### Incremental Backup — Sauvegarde incrémentielle
- Copie uniquement les données modifiées **depuis la dernière sauvegarde**, qu’elle soit complète ou incrémentielle.
- Exemple :
```
Lundi    → Full
Mardi    → changements depuis lundi
Mercredi → changements depuis mardi
Jeudi    → changements depuis mercredi
```
- Avantages :
	- sauvegarde rapide ;
	- faible consommation de stockage.
- Inconvénient :
	- restauration plus complexe.
- Pour restaurer jeudi :
```
Full
+ Incremental mardi
+ Incremental mercredi
+ Incremental jeudi
```
→ si un élément de la chaîne est perdu/corrompu, la restauration peut être compromise.
#### Differential Backup — Sauvegarde différentielle
- Copie toutes les modifications effectuées **depuis la dernière Full Backup**.
- Exemple :
```
Lundi    → Full
Mardi    → changements depuis lundi
Mercredi → changements depuis lundi
Jeudi    → changements depuis lundi
```
- Pour restaurer jeudi :
```
Full lundi
+ Differential jeudi
```
- Avantage :
	- restauration plus rapide/simple qu’avec une longue chaîne incrémentielle.
- Inconvénient :
	- les sauvegardes différentielles grossissent au fil du temps jusqu’à la prochaine Full.
#### Full vs Incremental vs Differential

|Type|Données copiées|Stockage|Restore|
|---|---|---|---|
|**Full**|Toutes les données|Élevé|Simple|
|**Incremental**|Depuis le dernier backup|Faible|Plus complexe|
|**Differential**|Depuis la dernière Full|Moyen → élevé|Plus simple que l’incrémental|

```
Incremental
→ optimise surtout le backup

Differential
→ compromis entre backup et restore
```

#### Mirror Backup — Sauvegarde miroir
- Maintient une copie presque identique de la source.
- Les changements peuvent être répliqués rapidement, voire en temps réel.

```
Source   ↔   Mirror
```
- Avantage :
	- accès/reprise rapide.
- Problème :
```
Delete source
→ Delete mirror

Corruption source
→ Corruption mirror
```

> ⚠️ Une réplication/mirror **ne remplace pas une véritable sauvegarde historique**. Un ransomware, une suppression accidentelle ou une corruption peuvent être répliqués sur la copie.
#### Snapshot
- Un **snapshot** représente l’état d’un système, volume ou VM à un instant donné.
```
System
   ↓
Snapshot @ 14:00
```
- Utilisé notamment pour :
	- virtualisation ;
	- stockage ;
	- bases de données ;
	- rollback rapide.
- Avantages :
	- création rapide ;
	- restauration rapide selon la technologie.

> ⚠️ Un snapshot n’est pas nécessairement une sauvegarde indépendante. Il peut dépendre du même stockage que les données originales : si ce stockage est détruit, les snapshots peuvent disparaître avec lui.

```
Snapshot → point de restauration rapide
Backup   → copie indépendante à privilégier pour la résilience
```
### Supports de sauvegarde — Backup Media
- Le **support** correspond à l’endroit ou au média sur lequel les backups sont stockés.
- Le choix dépend notamment de :
	- capacité ;
	- coût ;
	- vitesse ;
	- disponibilité ;
	- sécurité ;
	- durée de conservation.
#### Bandes magnétiques — Tape / LTO
- Toujours utilisées dans de grandes infrastructures.
- Très adaptées aux gros volumes et à l’archivage.
- Avantages :
	- coût par To relativement faible ;
	- longue conservation ;
	- peut être physiquement **offline / air-gapped**.
- Inconvénients :
	- accès séquentiel ;
	- restauration plus lente qu’avec du stockage disque.
```
Tape
→ grande capacité
→ archivage
→ offline possible
```
#### Disques durs externes
- Solution simple pour petites structures ou utilisateurs individuels.
- Accès relativement rapide.
- Risques :
	- panne matérielle ;
	- vol ;
	- dommage physique ;
	- corruption ;
	- ransomware si le disque reste connecté.
```
External HDD
→ utile
→ mais à déconnecter/protéger lorsqu'il n'est pas utilisé
```
#### NAS — Network Attached Storage
- Stockage accessible via le réseau.
- Utilisé comme espace centralisé de fichiers ou comme cible de backup.
```
Servers / Clients
      ↓
     NAS
```
- Avantages :
	- centralisation ;
	- facilité d’administration ;
	- capacité évolutive.

> Un NAS accessible avec les mêmes credentials/réseaux que la production peut également être compromis par un attaquant.
#### SAN — Storage Area Network
- Infrastructure de stockage dédiée, généralement utilisée dans les datacenters.
- Fournit du stockage en mode **bloc** avec de hautes performances.
- Utilisé notamment pour :
	- serveurs ;
	- virtualisation ;
	- bases de données ;
	- grandes infrastructures.
```
Servers
   ↓
SAN Fabric
   ↓
Storage Arrays
```
- haute performance ;
- grande capacité ;
- infrastructure plus complexe et coûteuse.

> NAS et SAN sont des **technologies de stockage**, pas automatiquement des solutions de backup. Leur sécurité dépend de la manière dont les sauvegardes y sont organisées et protégées.
#### Cloud Storage
- Sauvegardes stockées chez un fournisseur cloud.
- Permet d’éviter de maintenir toute l’infrastructure de stockage localement.
- Avantages :
	- scalable ;
	- accessible hors site ;
	- facilité d’augmentation de capacité ;
	- services d’immutabilité disponibles selon le fournisseur.
- Points à surveiller :
	- IAM / permissions ;
	- MFA ;
	- chiffrement ;
	- coûts de stockage/restauration ;
	- localisation des données ;
	- confidentialité ;
	- politique de rétention.
```
Cloud Backup
→ Offsite
→ Scalable
→ nécessite IAM + chiffrement + contrôle des accès
```
### Stratégie hybride
- Combiner plusieurs supports réduit le risque de **Single Point of Failure**.
- Exemple :
```
Production
   ↓
Local Backup / NAS
   ↓
Cloud / Offsite
   ↓
Offline / Immutable Copy
```
- Cela permet d’obtenir :
	- restauration locale rapide ;
	- protection hors site ;
	- meilleure résistance au ransomware/destruction physique.
## Processus de Sauvegarde et de Restauration
- Les processus de **Backup** et **Restore** servent à limiter l’impact d’une perte de données et à assurer la continuité d’activité.
```
Backup  → créer une copie exploitable
Restore → récupérer les données à partir de cette copie
```
### Processus de sauvegarde — Backup Process
#### 1. Spécifier les données
- Identifier les données à protéger.
- Prioriser notamment :
    - données métier critiques ;
    - bases de données ;
    - configurations ;
    - fichiers utilisateurs importants ;
    - systèmes nécessaires au fonctionnement de l’entreprise.
```
Inventory / Criticality
→ What must be backed up?
```
#### 2. Choisir le type de sauvegarde
- Selon les besoins :
	- **Full** ;
	- **Incremental** ;
	- **Differential** ;
	- **Mirror**.
- Le choix dépend notamment de :
	- volume de données ;
	- fréquence des changements ;
	- capacité de stockage ;
	- temps disponible pour le backup ;
	- temps attendu pour la restauration.
```
Backup Type
→ impacte Storage + Backup Time + Restore Time
```
#### 3. Planifier les sauvegardes
- Les sauvegardes sont généralement automatisées selon un **schedule**.
- Elles peuvent être exécutées pendant des périodes de faible activité afin de limiter leur impact sur :
    - CPU ;
    - stockage ;
    - bande passante ;
    - applications métier.

> Pour les systèmes critiques, la fréquence doit surtout être définie selon le **RPO**, pas uniquement selon les périodes de faible activité.

```
RPO faible
→ sauvegardes plus fréquentes
```
#### 4. Effectuer la sauvegarde
- Le processus est généralement réalisé automatiquement par :
    - logiciel de backup ;
    - appliance ;
    - service cloud ;
    - plateforme centralisée.
- À contrôler après exécution :
	- statut du job ;
	- erreurs ;
	- quantité de données sauvegardées ;
	- durée ;
	- destination ;
	- intégrité du backup.
```
Backup Job
→ Success / Failed
→ Logs + Monitoring
```

> Un job marqué `Successful` ne garantit pas que les données pourront réellement être restaurées.
### Processus de restauration — Restore Process
- Lorsqu’une donnée est supprimée, corrompue ou indisponible, une sauvegarde peut être utilisée pour la récupérer.
```
Data Loss
→ Select Backup
→ Restore
→ Validate
```
#### 1. Choisir le point de restauration
- Déterminer **quel backup utiliser**.
- Le plus récent n’est pas automatiquement le meilleur.
- Exemple :
```
Ransomware détecté vendredi
Compromission commencée mercredi

Backup jeudi → potentiellement compromis
Backup mardi → peut être préférable
```
- Il faut donc choisir un **known-good restore point** : un point connu comme sain.
#### 2. Choisir l’emplacement de restauration
- Deux possibilités principales :
	- Original Location :Utilisé lorsque l’environnement original est toujours considéré comme fiable.
	- Alternate Location : backup → nouvelle machine / environnement isolé. Utile notamment :
		- après compromission ;
		- pour tester une restauration ;
		- pour analyser des données ;
		- lorsque le système original est détruit.
#### 3. Effectuer la restauration
- La solution de backup récupère les données depuis le support choisi puis les replace à l’emplacement défini.
- Selon le type de backup :
```
Full Restore
→ Full

Incremental Restore
→ Full + tous les Incrementals nécessaires

Differential Restore
→ Full + dernier Differential
```
#### Validation après restauration
- Une restauration ne doit pas s’arrêter au message `Restore completed`.
- Il faut vérifier :
	- intégrité des fichiers ;
	- fonctionnement des applications ;
	- cohérence des bases de données ;
	- permissions ;
	- services ;
	- données attendues ;
	- absence de corruption.
```
Restore
→ Validate
→ Functional Test
→ Return to Production
```
#### Tests de restauration
- Les processus doivent être **régulièrement testés**.
- Objectifs :
	- vérifier que les backups sont utilisables ;
	- entraîner les équipes ;
	- mesurer la durée réelle de restauration ;
	- identifier les dépendances oubliées ;
	- vérifier que le RTO peut être respecté.
```
Backup Test
→ Can we restore?

Recovery Test
→ Can we restore correctly and fast enough?
```
#### RPO / RTO
- Deux métriques directement liées au processus :

|Concept|Question|
|---|---|
|**RPO — Recovery Point Objective**|Jusqu’à combien de données peut-on perdre ?|
|**RTO — Recovery Time Objective**|Combien de temps peut-on rester indisponible ?|

- Exemple :
```
RPO = 1h
→ au maximum 1h de données perdues

RTO = 4h
→ service restauré en moins de 4h
```
## Sécurité des sauvegardes & Disaster Recovery

### Sécurité des sauvegardes — Backup Security
- Les sauvegardes doivent être protégées au même titre que les données de production.
- Un attaquant qui compromet les backups peut :
    - voler les données ;
    - supprimer les copies ;
    - les chiffrer ;
    - empêcher toute restauration.
```
Production compromise
→ Backup compromise
→ Recovery impossible
```
#### Access Control
- Limiter l’accès aux sauvegardes aux seuls utilisateurs/services autorisés.
- Utiliser :
    - comptes dédiés ;
    - Least Privilege ;
    - MFA / 2FA ;
    - séparation des rôles.
```
User/Admin standard
        X
Backup Administration

Backup Admin
→ accès dédié + MFA
```
→ idéalement, la compromission d’un compte administrateur de production ne doit pas automatiquement donner accès aux backups.
#### Encryption
- Les sauvegardes doivent être chiffrées :
```
In Transit
→ lors du transfert

At Rest
→ lorsqu'elles sont stockées
```
- Objectif :
	- protéger la confidentialité des données ;
	- empêcher leur lecture en cas de vol du support ou d’accès non autorisé.

> Il faut également protéger les **clés de chiffrement** : perdre la clé peut rendre une sauvegarde parfaitement intacte mais inutilisable.
#### Integrity Checks
- Vérifier régulièrement que les backups :
    - ne sont pas corrompus ;
    - n’ont pas été modifiés ;
    - peuvent être restaurés correctement.
```
Backup
→ Integrity Check
→ Restore Test
```
- Un hash/checksum peut aider à détecter certaines altérations, mais le **test de restauration** reste essentiel.
#### Physical Security
- Les supports physiques doivent être protégés contre :
	- vol ;
	- incendie ;
	- dégâts matériels ;
	- accès non autorisé.
- Exemples :
```
External HDD
Tape / LTO
Offline Media
```
→ stockage dans des zones contrôlées, coffres ou sites sécurisés selon la criticité.
#### Copies multiples — règle 3-2-1
- Principe classique :
```
3 → copies des données au total
2 → types de supports différents
1 → copie offsite
```

> ⚠️ Le cours mélange ici **offsite** et **offline**. La règle 3-2-1 classique demande une copie **hors site** ; une copie offline/immutable correspond à une protection supplémentaire, souvent exprimée avec la règle **3-2-1-1-0**.

Pour renforcer la résistance au ransomware :

```
Offline / Air-Gapped / Immutable Backup
→ difficile à modifier ou supprimer
```
#### Secure Erase
- Lorsqu’un support arrive en fin de vie :
	- supprimer les données de manière irréversible ;
	- éviter qu’elles puissent être récupérées par un tiers.
- Selon le support :
	- secure erase ;
	- cryptographic erase ;
	- destruction physique.
```
Backup Media EOL
→ Secure Erase / Destroy
→ Dispose
```
### Disaster Recovery — Reprise après sinistre
- Le **Disaster Recovery (DR)** désigne l’ensemble des moyens permettant de **restaurer les systèmes et reprendre les services** après un incident majeur.
- Scénarios :
	- cyberattaque ;
	- ransomware ;
	- panne matérielle majeure ;
	- destruction d’un datacenter ;
	- catastrophe naturelle ;
	- corruption massive.
```
Disaster
→ Recover Data
→ Restore Systems
→ Restore Services
→ Resume Business
```

> Le **Data Recovery** concerne principalement la récupération des données, tandis que le **Disaster Recovery** est plus large : données + systèmes + infrastructure + procédures + ordre de reprise.
#### 1. Planification d'urgence - Emergency Planning
- Préparer à l’avance un **Disaster Recovery Plan / DRP**.
- Définir :
    - responsabilités ;
    - procédures ;
    - ordre de restauration ;
    - contacts ;
    - ressources nécessaires.
```
Incident majeur
→ Who does what?
→ What gets restored first?
→ How?
```
- L’objectif est d’éviter d’improviser pendant la crise.
#### 2. Data Backup
- Effectuer des sauvegardes régulières.
- Les stocker de manière sécurisée et indépendante.
- Vérifier régulièrement leur fonctionnement.

```
Backup
→ Protect
→ Monitor
→ Test
```
- La fréquence des backups doit être cohérente avec le **RPO** attendu.
#### 3. Data Restoration
- En cas de perte :
	1. identifier le bon restore point ;
	2. vérifier que le backup est sain ;
	3. restaurer les données ;
	4. valider leur intégrité.
```
Known-Good Backup
→ Restore
→ Validate
```
- Après une cyberattaque, restaurer simplement le backup le plus récent peut être dangereux s’il contient déjà des éléments compromis.
#### 4. System Reinstallation / Recovery
- Un sinistre peut nécessiter plus qu’une restauration de fichiers :
	- réinstaller OS et applications ;
	- reconstruire des serveurs ;
	- reconfigurer le réseau ;
	- restaurer les services ;
	- appliquer patches/hardening ;
	- effectuer des tests avant remise en production.
```
Clean System
→ Restore Configuration
→ Restore Data
→ Test
→ Production
```
- Dans certains incidents, reconstruire un système sain est préférable à réutiliser directement un système compromis.
#### 5. Test et amélioration
- Le DR Plan doit être régulièrement testé.
- Objectifs :
	- vérifier que les procédures fonctionnent ;
	- mesurer les temps de récupération ;
	- identifier les dépendances oubliées ;
	- former les équipes ;
	- corriger les faiblesses.

## Sauvegardes — Backups
- Les sauvegardes **n'empêchent pas** une attaque ransomware, mais constituent une **dernière ligne de défense / mécanisme de recovery**.
- Une sauvegarde inutilisable ou elle-même compromise peut mettre en danger la continuité de l'entreprise.
```
Ransomware → prévention/détection : EDR, hardening, segmentation...
Backup     → récupération après compromission
```
### Règle 3-2-1
- 3 copies > 2 supports différents > 1 une sauvegarde hors site
#### 3 copies
- Conserver **3 copies des données au total** :
    - données de production ;
    - Backup 1 ;
    - Backup 2.
#### 2 supports différents
- La règle classique demande de conserver les copies sur **au moins 2 types de supports / systèmes de stockage différents**.
- Exemples :
```
Disk + Tape
NAS + Object Storage
Local Storage + Cloud Backup
```
#### 1 copie hors site — Offsite
- Au moins une sauvegarde doit être située **hors du site principal**.
- Protège contre :
    - incendie ;
    - inondation ;
    - vol ;
    - destruction du datacenter.
```
Site principal détruit
→ Offsite Backup toujours disponible
```
### Règle 3-2-1-1-0
Extension de la règle 3-2-1 pour les ressources critiques.
#### +1 copie Offline
- Une copie doit être **isolée de l'infrastructure de production** afin qu'un attaquant ayant compromis le réseau ne puisse pas la supprimer/chiffrer.
```
Production Network
      X
Offline Backup
```
- Aujourd'hui, on utilise aussi des sauvegardes **air-gapped ou immutable**.
```
Offline / Air-Gapped / Immutable
→ difficile à modifier ou supprimer par l'attaquant
```
#### +0 erreur
- Les sauvegardes doivent être **vérifiées et restaurables sans erreur**.
- Il ne suffit pas qu'un job affiche `Backup successful`.
→ effectuer régulièrement des **restore tests** et vérifier l'intégrité des données restaurées.
### Durée de conservation — Retention
- Pouvoir restaurer des données datant d'au moins **30 jours**, afin d'éviter que toutes les sauvegardes disponibles contiennent déjà les traces d'une compromission ancienne.
```
Attaquant présent depuis plusieurs semaines
→ backups récents potentiellement déjà compromis
→ besoin de points de restauration plus anciens
```
> Les `30 jours` ne sont pas une règle universelle : la rétention doit être définie selon le risque, les contraintes légales, la criticité et les besoins métier.
### Tests de restauration
- Suivre/documenter les tests de restauration.
- Le cours recommande que **chaque serveur soit restauré au moins une fois par an**.
- Pour les systèmes critiques, des tests plus fréquents sont préférables.
- À vérifier :
	- données lisibles ;
	- fichiers non corrompus ;
	- applications fonctionnelles ;
	- procédure de restauration maîtrisée ;
	- temps nécessaire à la restauration.
### RPO (PDMA) / RTO (DMIA)
- Complément important pour la stratégie de backup :

| Concept                                                                             | Signification                                           |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **RPO — Recovery Point Objective** / PDMA - Perte de données maximale admissible    | Quantité maximale de données que l'on accepte de perdre |
| **RTO — Recovery Time Objective** / DMIA - durée maximale d'interruption admissible | Temps maximal acceptable pour restaurer le service      |
- Exemple :
```
RPO = 4h
→ backups suffisamment fréquents pour perdre ≤ 4h de données

RTO = 2h
→ service doit être restauré en ≤ 2h
```
### Protection des backups
- Pour éviter qu'un ransomware compromette aussi les sauvegardes :
	- comptes de backup dédiés ;
	- MFA sur les consoles d'administration ;
	- droits minimums ;
	- sauvegardes immutables/offline ;
	- séparation entre infrastructure de production et backup ;
	- alertes sur suppression/modification anormale des sauvegardes.
```
Attaquant Domain Admin
≠ doit automatiquement devenir Backup Admin
```
