## System Vulnerabilities & Security Measures
### Zero-Day 
- Zero-Day vulnérabilité : Vuln inconnue de l'éditeur, donc aucun patch officiel dispo au moment de sa découverte/exploitation
- Risque élevé car les défenses classiques basées sur signatures/patchs peuvent être inefficaces.
#### Défense en profondeur :
- Patching régulier des autres composants ;
- application layer Firewall / WAF ;
- IPS pour détecter/bloquer des comportements suspects ;
- EDR / monitoring comportemental en complément.
- Le patching ne corrige pas directement un vrai zero-day tant que le vendor n'a pas publié de fix mais réduit l'exposition globale et les autres chemins d'attaque.

### Origines des vulnérabilités 
#### Weak configuration / Misconfiguration 
- Une mauvaise configuration peut rendre un système vulnérable même si aucun bug logiciel n'existe.

| Problème                         | Risque / exemple                                                             |
| -------------------------------- | ---------------------------------------------------------------------------- |
| **Open Permissions**             | Droits trop larges, comptes guest/anonymous capables de modifier des données |
| **Unsecure Admin/Root Accounts** | Comptes privilégiés mal protégés ou trop nombreux                            |
| **Configuration Errors**         | Ex : DNS Zone Transfer accessible sans restriction                           |
| **Weak Encryption**              | Chiffrement faible ou absent pour données au repos/en transit                |
| **Unsecure Protocols**           | HTTP/Telnet/FTP au lieu de HTTPS/SSH/protocoles sécurisés                    |
| **Default Settings**             | Services inutiles installés/activés par défaut                               |
| **Open Ports & Services**        | Services inutiles exposés → surface d’attaque plus grande                    |
#### Third-Party Risks
- Un fournisseur ou partenaire peut introduire des vulnérabilités dans l'environnement.

| Problème                    | Risque / exemple                                                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Vendor Management           | Vérifier comment le produit s'intégre au réseau, protocoles utilisés, comptes nécessaires, support/patch encore dispo.                      |
| Supply Chain                | Fournisseur compromis peut livrer un produit/composant déjà malveillant.                                                                    |
| Outsourced code development | Code développé sans secure coding -> vuln applicatives.                                                                                     |
| Data storage                | Données stockées chez un tiers doivent rester : chiffrées, correctement contrôlées, idéalement déchiffrables uniquement par l'organisation. |
#### Patch management
- L'absence de stratégie de patching laisse les vuln connues exploitables.
- A maintenir à jour : 
	- Firmware : serveurs, routeurs, switches, appliances...
	- Operating System : patchs Windows/Linux/Mac...
	- Applications : Une app vuln peut compromettre l'host.

#### Vendor support / Legacy systems
- Legacy system : ancien système encore utilisé souvent : 
	- Plus supporté, plus patché, utilisant des protocoles obsolètes.
- Risque élevé car les vulns restent ouvertes.
- Si remplacement impossible :
	- isoler sur un segment réseau dédié, limiter flux autorisés, monitorer fortement, restreindre les accès.

### Impacts possibles d'une vulnérabilité non traitées

|Impact|Description|
|---|---|
|**Data Loss**|Suppression/chiffrement de données, ex : ransomware|
|**Data Breach**|Accès non autorisé à des données confidentielles|
|**Data Exfiltration**|Transfert non autorisé de données hors de l’organisation|
|**Identity Theft**|Données personnelles utilisées pour fraude/usurpation|
|**Financial Loss**|Arrêt de production, récupération, pertes commerciales|
|**Reputation Damage**|Perte de confiance clients/partenaires|
|**Availability Loss**|Service/système indisponible|
#### Data breach vs data exfiltration
- Breach : accès non autorisé aux données
- Exfiltration : données effectivement transférées hors de l'environnement.
- Exemple de protection contre exfiltration : 
	- désactivation/restriction USB, DLP, contrôle des uploads/emails, monitoring réseau.

### Configuration faible ou mauvaise configuration 
#### Unencrypted credentials / Cleartext
- Certains protocoles historiques transmettent les credentials sans chiffrement.
#### Logs & Event Anomalies
- Activer les logs ;
- Connaître leur emplacement ;
- Rechercher : 
	- Anomalies ;
	- event inhabituels ;
	- connexions suspectes ;
	- changement de configuration.
#### Permission issues
- Mauvaises permissions = cause fréquente de compromission interne.
- Appliquer : moindre privilege, revoir régulièrement ACL et permissions.
#### Access Violations 
- Accès à une ressource par un user non autorisé.
- Prévention :
	- Authentification obligatoire ;
	- trafic de login chiffré ;
	- permissions correctes ;
	- contrôles d'accès.
#### Certificate issues
- Les certificats sécurisent : web, email, communications serveur <-> serveur
- A vérifier : certificat non expiré, non révoqué, chaîne de confiance valdie, CA de confiance, nom du certificat correspondant au service.

## Principales menaces et stratégies d'atténuation
### Exfiltration de données
- Transfert de données hors d'un système/réseau sans autorisation.
- Exemple : 
	- copie sur USB, envoi par email, upload vers stockage cloud personnel.
- Prévention :
	- désactiver/restreindre les ports USB ;
	- utiliser solution DLP pour détecter/bloquer les transferts de données sensibles.
### Appareils mal configurés
- Les misconfigurations constituent un point d'entrée fréquent pour les attaquants. 

| Élément               | Risque / mesure                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------ |
| **Firewall**          | Vérifier les règles, segmenter le réseau et empêcher les accès non autorisés entre segments      |
| **Content Filtering** | Bloquer les sites dangereux ou susceptibles d’exécuter du contenu malveillant                    |
| **Access Points**     | WPA2/WPA3, clés robustes, changer les credentials admin par défaut, éventuellement MAC filtering |
| **Security Settings** | Vérifier ACL, passwords, clés, algorithmes de chiffrement et règles de filtrage                  |

### Problèmes liés aux employés 

| Élément                | Risque / mesure                                                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Policy violations**  | Former les employés aux politiques internes et à leur raison d'être.                                                                  |
| **Insider threat**     | Utiliser authentification, permissions et ACL, limiter les accès aux ressources nécessaires, anti malware sur les endpoints.          |
| **Social engineering** | Sensibiliser au phishing, baiting et autres techniques de manipulation.                                                               |
| **Social media**       | Définir ce qui peut être partagé, éviter photos/info internes pouvant révéler des données sensibles en arrière-plan.                  |
| **Personal email**     | Risque d'envoi de données pro vers extérieur, DLP pour bloquer les transferts, limiter l'accès au cloud/storage perso via firewall... |

### Application security
#### Logiciel non autorisé 
- Limiter les logiciels pouvant être installés/exécutés.
- Application allowlisting : seuls les logiciels explicitement autorisés peuvent s'exécuter. Type AppLocker.
####  Réferentiel de sécurité / Ecart par rapport au référentiel
- Security Baseline : configuration de sécurité de référence que les systèmes doivent conserver.
- Baseline Deviation : changement qui fait sortir un système de cet état attendu.
	- PowerShell Desired State Configuration (DSC) pour empêcher les changements qui s'écartent du référentiel.
#### Violation de la conformité des licences 
- Le dépassement ou non-respect des licences logicielles peut entraîner : 
	- problèmes de conformité ;
	- coûts/amendes.
- Utiliser inventaire centralisé pour suivre installations et licences.
#### Asset management
- Maintenir un inventaire et une gestion centralisée des systèmes :
	- Config, patches, drivers, applications....
	- Ex : GPO, MECM
#### Authentification Issues 
- Sécuriser les mécanismes d’authentification des applications.
- Éviter que les credentials puissent être interceptés.
- Utiliser des **comptes dédiés** pour les applications/services.

## Analyse des résultats des outils de sécurité 

- Diverses technologies de sécurité fournissent des résultats qui peuvent vous aider à identifier et à répondre aux incidents de sécurité potentiels.
### HIDS / HIPS
- **Output** : alertes sur des activités suspectes détectées sur l’hôte.
- Examiner :
    - date/heure ;
    - source ;
    - compte impliqué ;
    - événement déclencheur.

```
HIDS → détecte
HIPS → détecte + peut bloquer
```
### Antivirus
- Fournit logs/notifications sur :
    - malware détecté ;
    - fichier concerné ;
    - résultat du scan ;
    - action effectuée : quarantaine, suppression
→ Surveiller les détections et vérifier que la menace a bien été traitée.
### Advanced Malware Removal Tools
- Donnent davantage de détails sur :
    - malware identifié ;
    - suppression/quarantaine ;
    - état du nettoyage.

→ Vérifier que le malware est réellement **contenu et supprimé**.
### Patch Management Tools
- Rapports sur :
    - patches nécessaires ;
    - état du déploiement ;
    - systèmes à jour/non à jour ;
    - échecs d’installation.
→ Prioriser les patches critiques et enquêter sur les systèmes où le déploiement échoue
### UTM — Unified Threat Management
Regroupe plusieurs fonctions de sécurité dans une même solution.
Output possible :
- trafic suspect ;
- virus/spam bloqués ;
- violations de content filtering.
→ Examiner les alertes et rapports réseau.
### DLP
- Génère une alerte lorsqu’un transfert sensible est détecté/bloqué.
Exemples :
```
Copie fichier confidentiel → USB
Email contenant données sensibles → externe
```
→ appliquer les politiques DLP et surveiller les violations.
### DEP — Data Execution Prevention
- Empêche l’exécution de code dans certaines zones mémoire normalement destinées aux **données**.
### WAF — Web Application Firewall
- Filtre le trafic destiné aux **applications Web**.
- Les logs indiquent notamment :
    - requêtes autorisées ;
    - trafic malveillant bloqué ;
    - tentatives d’attaque Web.
```
Client → WAF → Web Application
```
→ analyser les logs pour identifier et répondre aux attaques applicatives.

## Cloud vs On Prem
- Lors de la transition vers des environnements cloud, il est essentiel de traiter les vulnérabilités qui peuvent découler d'erreurs de configuration.
- Voici les principales considérations pour les vulnérabilités basées sur le cloud par rapport aux installations sur site (on-premises) :

### Ports ouverts
**On-Prem :**
- ne pas exposer de ports/services inutiles sur le LAN ou Internet.
**Cloud :**
- éviter les ports inutiles sur VM/services ;
- ne pas exposer directement RDP/SSH si une solution intermédiaire existe.

Exemple Azure :

```
Internet
   ↓
Azure Bastion
   ↓
VM

plutôt que

Internet → RDP 3389 → VM
```

### Authentication Methods
**On-Prem :**
- authentification souvent gérée localement ou via **Active Directory / Domain Controllers**.

**Cloud :**
- ressources potentiellement accessibles mondialement ;
- utiliser **MFA** pour réduire l’impact d’un password compromis.

```
Password
+
Second facteur
→ MFA
```

> Un facteur résistant au phishing est préférable quand disponible ; le SMS reste une forme de MFA mais est moins robuste.
### Conditional Access
**On-Prem :**
- contrôles souvent basés sur réseau, AD et GPO.
**Cloud :**
- **Conditional Access Policies** selon :
    - identité utilisateur ;
    - emplacement ;
    - état/conformité du device ;
    - niveau de risque.
Exemple :
```
Login admin
+
device non conforme
+
pays inhabituel
→ MFA renforcée / accès bloqué
```
### Privilege Management
**On-Prem :**
- permissions locales/AD ;
- contrôle via rôles et groupes.

**Cloud :**
- éviter les privilèges excessifs ;
- appliquer **RBAC + Least Privilege** ;
- limiter fortement les rôles à très hauts privilèges (`Global Administrator`, etc.).

## Menaces sur la sécurité physique
### Espionnage - Snooping
- **Snooping** : accès non autorisé à des informations confidentielles par observation ou fouille.
- Exemples :
    - **Dumpster Diving** : récupérer des documents jetés ;
    - fouiller bureaux, tiroirs ou armoires d’autres employés.
- Prévention
	- **Clean Desk Policy** : ne pas laisser de documents sensibles sans surveillance.
	- Stocker les documents dans des **armoires verrouillées** et zones sécurisées.
	- **Détruire/shredder** les documents avant de les jeter.
```
Document sensible
→ stockage sécurisé
→ destruction avant élimination
```
### Asset Lost / Stolen
Les laptops, smartphones et tablettes perdus ou volés peuvent exposer des données sensibles.
- Ne pas laisser les appareils visibles dans une voiture → risque de **smash-and-grab**.
- Les placer dans un endroit non visible/sécurisé, par exemple le coffre.
- Au bureau, utiliser des **lockdown/security cables** pour attacher :
    - laptops ;
    - écrans ;
    - projecteurs ;
    - desktops.

> Les câbles antivol sont surtout un **moyen de dissuasion** : ils ne résistent pas forcément à un attaquant déterminé.
### Remote Device Reset / Wipe
- Un appareil perdu ou volé doit être **signalé immédiatement**.
- **Remote Wipe** : le serveur envoie une commande demandant au device d’effacer :
    - données ;
    - configurations.

```
Device perdu
→ signalement
→ Remote Wipe
→ données supprimées
```

→ réduit le risque d’exposition des données présentes sur l’appareil.
### Device Security Measures

#### Smartphones / Mobile Devices
Mesures principales :
- password/PIN ;
- **auto-lock** après une période d’inactivité ;
- fonctions de **device tracking** ;
- remote wipe.
L’objectif est qu’un appareil volé ne puisse pas être utilisé directement par l’attaquant.
#### Laptops
Mesures possibles au niveau BIOS/UEFI :
- **Power-on password** ;
- password administrateur BIOS/UEFI ;
- limiter/modifier le **boot order** pour empêcher facilement le démarrage sur USB/CD externe.
```
Boot externe bloqué
→ plus difficile de démarrer un OS contrôlé par l'attaquant
```
#### Full-Disk Encryption
Si un attaquant possède physiquement le disque, le chiffrement complet protège les données au repos.
Exemple Windows :
- **BitLocker**.
```
Disque volé
+
BitLocker
→ données chiffrées
```
**Complément :** BitLocker n’est pas simplement un « boot password ». Il chiffre le disque ; avec une configuration **TPM + PIN**, il peut également imposer une authentification avant le démarrage de Windows.
### Employee Mistakes
Les erreurs humaines peuvent provoquer des dégâts physiques.
#### ESD — Electrostatic Discharge
- Une personne peut accumuler de l’électricité statique.
- En touchant un composant, cette charge peut être transférée et :
    - endommager ;
    - voire détruire le composant.
Exemple :
```
Technicien
→ électricité statique
→ touche motherboard/RAM
→ ESD
→ composant endommagé
```
Prévention :
- former les équipes support ;
- utiliser un **anti-static wrist strap** relié à la terre avant de manipuler les composants.
### Malicious Interference / Sabotage
- **Sabotage** : action volontaire visant à endommager ou perturber les systèmes.
- Peut notamment provenir d’un **disgruntled employee**, mais pas uniquement.
Exemple :
```
Employé malveillant
→ modification/suppression d'une base de données
→ interruption du service
```
Prévention / Résilience
- identifier les systèmes particulièrement exposés au sabotage ;
- limiter les privilèges ;
- disposer d’un **Recovery Plan** détaillé ;
- prévoir :
    - procédures de restauration ;
    - backups ;
    - pièces de rechange nécessaires.
Le but n’est pas seulement d’empêcher le sabotage, mais aussi de pouvoir **restaurer rapidement le service** après un incident.