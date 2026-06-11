# Référentiel complet de taxonomie cyber — principes, familles d'attaques, défenses et raisonnement SOC/IR (index)

**Référentiel de référence — Principes, attaques, défenses et réponse à incident**

Un référentiel-pivot de culture cyber large : non pas un catalogue d'attaques isolées, mais une **carte mentale** complète permettant de *comprendre, classer, relier, défendre et répondre*. 14 parties, 319 chapitres, 9 annexes (dont une partie de cas filés d'investigation et des tableaux de correspondance utilisables comme fiches réflexes).

> **Nature de ce document.** C'est un *référentiel structurant* (une taxonomie), exhaustif **en largeur**. Il donne la carte du territoire et le raisonnement ; les cours spécialisés de la bibliothèque approfondissent ensuite chaque domaine (CTI, forensic, AD, cloud, web, malware…). Sa force est de *ranger, relier et raisonner*, pas de tout détailler en profondeur opérationnelle.

> **Fil rouge du cours :** `actif → menace → vulnérabilité → risque → attaque → impact → détection → réponse → remédiation`

> **Posture :** légal, défensif, pédagogique. Mécanismes, impacts, signaux de détection et défenses — sans payload offensif ni procédure d'exploitation.

---

## Les 8 volumes

**Volume 1 — Fondations, principes défensifs, GRC** *(`cours_cyber_vol1_fondations.md`)*
Introduction · Partie 1 (fondations : actif, menace, vulnérabilité, risque, CIA, AAA, surfaces, contrôles) · Partie 2 (principes : défense en profondeur, moindre privilège, Zero Trust, assume breach, tiering, hardening, secure by design, threat modeling, sauvegarde) · Partie 3 (GRC : PSSI, analyse de risque, homologation, gestion des vulnérabilités/actifs, classification, audit, sensibilisation, supply chain, crise). Chapitres 1–39.

**Volume 2 — Surfaces d'attaque & vulnérabilités** *(`cours_cyber_vol2_surfaces_vulnerabilites.md`)*
Partie 4 (22 surfaces : poste, serveur, réseau, AD/IAM, web, API, cloud, conteneurs, CI/CD, messagerie, navigateur, mobile, IoT, OT/ICS, Wi-Fi, VPN, SaaS, identité, données, humain, physique, firmware) · Partie 5 (20 familles de vulnérabilités, vocabulaire CWE). Chapitres 40–81.

**Volume 3 — Attaques web et applicatives** *(`cours_cyber_vol3_attaques_web.md`)*
Partie 6 : Broken Access Control, IDOR/BOLA, élévation de privilèges, famille XSS complète, famille SQLi complète, command/LDAP/XPath injection, SSTI, XXE, SSRF (+blind/métadonnées), file inclusion (LFI/RFI/traversal), upload, Zip Slip, désérialisation, CSRF, clickjacking, CORS, open redirect, host header, request smuggling, cache poisoning, web cache deception, prototype pollution, rate limit bypass, business logic, GraphQL. Chapitres 82–126.

**Volume 4 — Réseau et infrastructure** *(`cours_cyber_vol4_reseau_infra.md`)*
Partie 7 : reconnaissance/scan, énumération, sniffing, spoofing (ARP/DNS/DHCP), DNS tunneling, MITM, replay, downgrade, exploitation de services, SMB/RDP/VPN, pivoting, tunneling, lateral movement, DoS/DDoS, reflection/amplification, botnet, VLAN hopping, Wi-Fi evil twin, rogue AP, deauth, BGP hijacking. Chapitres 127–154.

**Volume 5 — Identité, Active Directory et privilèges** *(`cours_cyber_vol5_identite_ad.md`)*
Partie 8 : identité-périmètre, structure AD, Kerberos/NTLM/LDAP, comptes, tiering, Kerberoasting, AS-REP roasting, spraying/brute force/stuffing, pass-the-hash/ticket, overpass-the-hash, golden/silver ticket, DCSync/DCShadow, abus de délégation/RBCD, GPO/ACL abuse, shadow credentials, AD CS abuse, credential dumping, lateral movement Windows, PAM/bastion. Chapitres 155–183.

**Volume 6 — Malware, phishing et client-side** *(`cours_cyber_vol6_malware_phishing.md`)*
Partie 9 : classification des malwares (virus, ver, trojan, ransomware, wiper, spyware, infostealer, RAT, backdoor, loader/dropper/downloader, rootkit/bootkit, fileless, macro, LotL/LOLBins) ; ingénierie sociale (phishing, spear/whaling, smishing, vishing, quishing, BEC, malspam, drive-by, malvertising, SEO poisoning, watering hole, MFA fatigue, consent phishing). Chapitres 184–217.

**Volume 7 — Cloud, API, conteneurs et supply chain** *(`cours_cyber_vol7_cloud_api_supplychain.md`)*
Partie 10 : principes cloud/responsabilité partagée, IAM cloud, buckets/secrets/clés, métadonnées, élévation/lateral movement cloud, API (BOLA/BFLA/exposition/consommation), Kubernetes RBAC, container escape, images/registres, CI/CD, pipeline poisoning, dependency confusion, typosquatting, paquets/build compromis, signature/intégrité, SBOM, secrets management. Chapitres 218–244.

**Volume 8 — SOC/réponse, défenses, synthèse + annexes** *(`cours_cyber_vol8_soc_defenses_synthese.md`)*
Partie 11 (détection/SOC/IR : événement→alerte→incident, IOC/IOA/TTP, SIEM/EDR/NDR/SOAR, triage→qualification→escalade→investigation→confinement→éradication→rétablissement→REX, forensic, timeline, crise, PRA/PCA) · Partie 12 (taxonomie des défenses, reliées aux attaques) · Partie 13 (synthèse : classer/relier/prioriser, carte mentale, erreurs de raisonnement) · **Partie 14 (V2 — cas filés d'investigation SOC/IR : phishing, Kerberoasting, malware poste, exfiltration cloud, ransomware, SSRF métadonnées)** · Annexes A–J (glossaire, tableau de correspondance central multi-colonnes, tableaux surface/cadres, fiches réflexes, mini-cas, métiers, apprentissage légal, bibliographie, schémas ASCII). Chapitres 245–319.

> **Note V2.** Cette édition ajoute, suite à relecture : une **Partie 14** de six cas filés d'investigation (du signal brut au REX) pour passer de « je connais les mots » à « je sais raisonner sur un incident » ; un **grand tableau de correspondance multi-colonnes** (Annexe B) attaque → famille → vulnérabilité-racine → surface → impact CIA → logs utiles → défenses, utilisable comme fiche réflexe ; et des **schémas mentaux ASCII** (Annexe J).

---

## Cadres de référence mobilisés

NIST CSF 2.0 · MITRE ATT&CK · MITRE D3FEND · MITRE CAPEC · CWE · OWASP Top 10 · OWASP API Security Top 10 · OWASP ASVS · SLSA/SBOM · ISO 27001/27005 · EBIOS RM · CIS · KEV (CISA).

## Comment utiliser ce cours

1. **Lecture linéaire** (volumes 1→8) pour construire la carte mentale.
2. **Lecture par besoin** : consulter une surface (vol. 2), une famille d'attaque (vol. 3–10), ou une défense (vol. 8) à la demande.
3. **Référence rapide** : annexes du volume 8 (glossaire, tableaux, fiches réflexes).
4. **Méthode de raisonnement** : appliquer les chapitres 306–310 face à toute situation nouvelle.


---

# Référentiel complet de taxonomie cyber — principes, familles d'attaques, défenses et raisonnement SOC/IR

> **Référentiel de référence — Volume 1/8**
> Parties 1 à 3 : Fondations · Grands principes défensifs · Gouvernance, risque et conformité
>
> Ce cours est conçu comme un **cours-pivot** : son objectif n'est pas de cataloguer des attaques isolées, mais de bâtir une **carte mentale** de toute la cybersécurité. On apprend à *classer*, à *relier*, et à passer de l'attaque à la défense.

---

## Comment lire ce cours

Encadrés récurrents utilisés tout au long du cours :

- 🎯 **À retenir** — l'essentiel d'un chapitre, mémorisable en une phrase.
- ⚠️ **Erreur fréquente** — la confusion ou la faute classique à éviter.
- 🔧 **Exemple concret** — illustration conceptuelle, jamais un payload offensif.
- 🛡️ **Défense** — les contre-mesures associées.
- 🧭 **Taxonomie** — où ranger la notion, à quoi elle se relie.

**Cadres de référence** mobilisés (utilisés comme ossature, pas recopiés) : NIST Cybersecurity Framework 2.0 (Govern, Identify, Protect, Detect, Respond, Recover), MITRE ATT&CK (tactiques/techniques/sous-techniques), MITRE D3FEND (contre-mesures), MITRE CAPEC (patterns d'attaque), CWE (faiblesses logicielles), OWASP Top 10 / API Security Top 10 / ASVS.

**Posture du cours :** légal, défensif, pédagogique. On explique les *mécanismes*, les *familles*, les *impacts*, les *signaux de détection* et les *défenses*. On ne fournit ni payload exploitable, ni procédure offensive opérationnelle.

---

# Introduction — Pourquoi une taxonomie ?

## Pourquoi la cybersécurité est illisible sans classification

La cybersécurité souffre d'un problème de **volume** et de **vocabulaire**. Un débutant rencontre en quelques jours des centaines de termes — XSS, SSRF, Kerberoasting, EDR, BOLA, golden ticket, MFA fatigue — sans grille de lecture pour les organiser. Le résultat est une connaissance en « liste de courses » : on connaît des noms, mais on ne sait pas les *ranger*, donc on ne sait pas *raisonner*.

Une taxonomie résout ce problème. Elle transforme une liste plate en **arbre** : familles, sous-familles, types, sous-types. Quand une attaque inconnue apparaît, on n'a plus besoin de la connaître par cœur : il suffit de la rattacher à une famille connue, et on hérite immédiatement de tout ce qu'on sait sur cette famille (mécanisme général, impacts probables, défenses applicables).

## Apprendre des attaques isolées vs comprendre des familles

Apprendre « le reflected XSS » isolément, c'est mémoriser un cas. Comprendre « l'injection » comme famille — *mélange de données et de code, exécuté par un interpréteur qui ne distingue pas les deux* — c'est obtenir une clé qui ouvre XSS, SQLi, command injection, LDAP injection, SSTI, etc. La famille donne le **principe** ; les sous-types ne sont que des variations de contexte (un navigateur, une base SQL, un shell, un annuaire LDAP, un moteur de templates).

C'est la différence entre retenir 300 faits et comprendre 12 principes qui génèrent ces 300 faits.

## Le fil rouge du cours

Tout le cours suit une chaîne de raisonnement unique, déclinée encore et encore :

> **comprendre → classer → relier → défendre → répondre**

Et au niveau d'un objet de sécurité, la chaîne canonique est :

> **actif → menace → vulnérabilité → risque → attaque → impact → détection → réponse → remédiation**

Retenez cette chaîne : elle est le squelette de toute la discipline. Chaque chapitre du cours occupe une position précise sur cette chaîne.

🎯 **À retenir** — La cybersécurité ne se mémorise pas, elle se *classe*. Une bonne taxonomie est un multiplicateur : elle vous fait comprendre des attaques que vous n'avez jamais vues.

---

# Partie 1 — Fondations de la cybersécurité

## Chapitre 1 — Cybersécurité, sécurité informatique, sécurité des SI

**Définition.** Trois termes voisins, souvent confondus, désignent des périmètres différents.

- **Sécurité informatique** : protection des composants techniques (postes, serveurs, réseaux, logiciels). Périmètre étroit, centré sur la machine.
- **Sécurité des systèmes d'information (SSI)** : protection de l'ensemble organisé qui traite l'information — incluant les processus, les procédures, les personnes, les données et la gouvernance, pas seulement la technique.
- **Cybersécurité** : terme le plus large, englobant la SSI mais ajoutant la dimension des **menaces externes actives** (cybercriminalité, espionnage, sabotage), le cyberespace, et souvent la défense des intérêts au-delà du seul SI (réputation, continuité d'activité, souveraineté).

**Pourquoi la distinction compte.** Un chiffrement parfait (sécurité informatique) ne protège pas contre un employé qui exfiltre des données par négligence (relève de la SSI : processus, sensibilisation) ni contre une campagne d'espionnage ciblée (relève de la cybersécurité : renseignement sur la menace).

🧭 **Taxonomie** — Pensez en cercles concentriques : sécurité informatique ⊂ SSI ⊂ cybersécurité.

⚠️ **Erreur fréquente** — Croire qu'« acheter un firewall » règle un problème de cybersécurité. Le firewall est de la sécurité informatique ; le risque, lui, est souvent organisationnel.

🎯 **À retenir** — La cybersécurité protège l'information *et* l'organisation, pas seulement les machines.

## Chapitre 2 — Actif, donnée, service, système, identité

**Définition.** Un **actif** (asset) est tout ce qui a de la valeur pour l'organisation et mérite donc d'être protégé. La sécurité commence toujours par *savoir ce qu'on protège*.

Cinq grandes catégories d'actifs structurants :

- **Donnée** : l'information elle-même (dossiers clients, secrets industriels, identifiants). Souvent l'actif de plus grande valeur.
- **Service** : une fonction rendue (messagerie, site marchand, paie). Sa valeur est sa *disponibilité* et son *intégrité*.
- **Système** : le support technique (serveur, application, base de données) qui héberge données et services.
- **Identité** : un compte et ses droits — l'actif devenu central, car compromettre une identité donne accès à tout ce que cette identité peut atteindre.
- **Actifs immatériels** : réputation, conformité, propriété intellectuelle.

🔧 **Exemple concret** — Dans une banque, la *donnée* « solde du compte » est l'actif ; le *service* « virement » la manipule ; le *système* « core banking » l'héberge ; l'*identité* « administrateur » peut tout modifier.

🧭 **Taxonomie** — Tout le reste du cours protège ces cinq familles d'actifs. Une attaque vise toujours, in fine, un actif.

🎯 **À retenir** — On ne peut pas protéger ce qu'on n'a pas inventorié. L'inventaire des actifs est le fondement de toute sécurité (NIST CSF : fonction *Identify*).

## Chapitre 3 — Menace, vulnérabilité, risque, impact, vraisemblance

**Définitions.** Ces cinq mots forment le cœur conceptuel de la gestion du risque. Les confondre rend tout raisonnement impossible.

- **Menace** (threat) : un *danger potentiel* — un acteur ou un événement capable de nuire (un attaquant, un malware, un incendie). La menace existe indépendamment de vous.
- **Vulnérabilité** : une *faiblesse* exploitable dans un actif (un mot de passe faible, un logiciel non patché, un employé non sensibilisé).
- **Risque** : la *combinaison* d'une menace exploitant une vulnérabilité, avec ses conséquences. C'est une grandeur, pas un objet.
- **Impact** : la *gravité des conséquences* si le risque se réalise (perte financière, arrêt d'activité, fuite de données).
- **Vraisemblance** (likelihood) : la *probabilité* que le risque se réalise.

**La formule mentale :**

> Risque ≈ Vraisemblance (menace × vulnérabilité × exposition) × Impact

🔧 **Exemple concret** — Menace : un cambrioleur. Vulnérabilité : une fenêtre sans verrou. Impact : vol des biens. Risque : élevé si le quartier est exposé (vraisemblance) et les biens précieux (impact). Poser un verrou réduit la *vulnérabilité*, donc le risque — sans supprimer la menace.

⚠️ **Erreur fréquente** — Dire « j'ai une vulnérabilité, donc j'ai un gros risque ». Faux : une vulnérabilité sans menace réaliste ni impact significatif est un risque faible. C'est la combinaison qui compte.

🧭 **Taxonomie** — Position sur le fil rouge : `menace` et `vulnérabilité` sont les *causes*, `risque` est l'*évaluation*, `impact` est la *conséquence*.

🎯 **À retenir** — Menace = qui/quoi peut nuire. Vulnérabilité = par où. Risque = combien ça compte. Ne jamais les confondre.

## Chapitre 4 — Attaque, incident, compromission, intrusion, fuite de données

**Définitions.** Termes proches qui décrivent des *étapes* ou des *états* différents d'un événement de sécurité.

- **Attaque** : une *action hostile délibérée* visant un actif. Une attaque peut échouer.
- **Intrusion** : un *accès non autorisé* obtenu dans un système. C'est une attaque qui a réussi à franchir le périmètre.
- **Compromission** : un système (ou une identité) est passé sous le contrôle, partiel ou total, d'un attaquant. État plus grave que la simple intrusion.
- **Incident (de sécurité)** : tout *événement* qui porte atteinte (ou menace de porter atteinte) à la confidentialité, l'intégrité ou la disponibilité. Terme générique du SOC. Une attaque réussie est un incident ; une panne accidentelle aussi.
- **Fuite de données** (data breach/leak) : une *catégorie d'impact* où des données confidentielles sortent du périmètre de contrôle, par attaque ou par erreur.

🔧 **Exemple concret** — Un attaquant envoie un mail piégé (**attaque**). Un employé clique et l'attaquant obtient un accès (**intrusion**). Il installe une porte dérobée et contrôle le poste (**compromission**). Le SOC ouvre un ticket (**incident**). L'attaquant exfiltre le fichier clients (**fuite de données**).

⚠️ **Erreur fréquente** — Utiliser « breach » pour toute attaque. Une attaque bloquée n'est pas une compromission ; une compromission sans sortie de données n'est pas une fuite.

🧭 **Taxonomie** — Ces termes décrivent une *progression* : attaque → (intrusion) → compromission → impact (dont fuite). L'incident est l'enveloppe qui englobe le tout côté défense.

🎯 **À retenir** — Distinguez l'*action* (attaque), l'*état* (intrusion, compromission) et la *conséquence* (fuite).

## Chapitre 5 — Confidentialité, intégrité, disponibilité (triptyque CIA)

**Définition.** Le triptyque **CIA** (Confidentiality, Integrity, Availability — en français DIC : Disponibilité, Intégrité, Confidentialité) est la boussole de la sécurité. Toute mesure de sécurité sert au moins l'une de ces trois propriétés.

- **Confidentialité** : l'information n'est accessible qu'aux personnes autorisées. Atteinte = fuite, espionnage.
- **Intégrité** : l'information n'est ni altérée ni falsifiée sans autorisation. Atteinte = sabotage, fraude, manipulation de données.
- **Disponibilité** : l'information et les services sont accessibles quand on en a besoin. Atteinte = déni de service, ransomware, panne.

**Extensions fréquentes** : on ajoute parfois la **traçabilité/imputabilité** (preuve de qui a fait quoi) et la **non-répudiation** (impossibilité de nier une action). Certains parlent du modèle étendu « Parkerian hexad ».

🔧 **Exemple concret** — Un ransomware chiffre les fichiers : il attaque surtout la **disponibilité** (et parfois la confidentialité par double extorsion). Une falsification de relevé bancaire attaque l'**intégrité**. Un vol de base de données attaque la **confidentialité**.

🧭 **Taxonomie** — Toute attaque peut être classée par la propriété CIA qu'elle vise. C'est une des grilles de classification les plus puissantes.

🎯 **À retenir** — Quand vous analysez une attaque, demandez : *quelle propriété CIA est visée ?* La réponse oriente immédiatement la défense.

## Chapitre 6 — Authentification, autorisation, traçabilité, imputabilité

**Définition.** Quatre piliers du contrôle d'accès, souvent regroupés sous **AAA** (Authentication, Authorization, Accounting) + imputabilité.

- **Authentification** : *prouver qui l'on est* (mot de passe, certificat, biométrie, MFA). Répond à « êtes-vous bien vous ? ».
- **Autorisation** : *déterminer ce que l'on a le droit de faire* une fois authentifié. Répond à « avez-vous le droit ? ».
- **Traçabilité** (accounting/auditing) : *enregistrer les actions* dans des journaux pour pouvoir les reconstituer.
- **Imputabilité** (accountability) : *pouvoir attribuer une action à un acteur précis* de manière fiable. Suppose authentification + traçabilité solides.

**Facteurs d'authentification** (à connaître) : ce que je *sais* (mot de passe), ce que je *possède* (téléphone, clé), ce que je *suis* (biométrie). Combiner au moins deux familles = MFA.

🔧 **Exemple concret** — Confondre les deux premiers est une faute classique : un système peut parfaitement *authentifier* un utilisateur (il est bien lui) tout en l'*autorisant* à trop de choses (droits excessifs). L'IDOR (chapitre 83) est précisément une faille d'**autorisation**, pas d'authentification.

⚠️ **Erreur fréquente** — « L'utilisateur est connecté donc il a le droit ». Authentification ≠ autorisation. Vérifier l'identité ne dit rien sur les permissions.

🧭 **Taxonomie** — Les attaques sur l'authentification (brute force, credential stuffing) et sur l'autorisation (IDOR, élévation de privilèges) forment deux familles distinctes — ne pas les mélanger.

🎯 **À retenir** — Authentification = *qui*. Autorisation = *quoi*. Traçabilité = *preuve*. Imputabilité = *attribution*.

## Chapitre 7 — Surface d'attaque, exposition, chemin d'attaque

**Définition.**

- **Surface d'attaque** : l'*ensemble des points* par lesquels un attaquant peut tenter d'entrer ou d'agir (ports ouverts, formulaires web, comptes, API, employés…). Plus elle est grande, plus il y a d'occasions d'attaque.
- **Exposition** : le *degré d'accessibilité* d'un actif depuis une zone dangereuse (Internet > réseau interne > réseau isolé). Un même actif est plus risqué s'il est exposé.
- **Chemin d'attaque** (attack path) : la *séquence d'étapes* reliant le point d'entrée de l'attaquant à son objectif final (souvent : Internet → phishing → poste → identité → serveur → données).

**Réduction de surface d'attaque** : principe défensif majeur (chapitre 22) — fermer les ports inutiles, désinstaller les logiciels superflus, limiter les comptes.

🔧 **Exemple concret** — Un serveur exposé sur Internet avec 30 ports ouverts a une grande surface d'attaque *et* une forte exposition. Le même serveur derrière un VPN, avec 2 ports, réduit les deux.

🧭 **Taxonomie** — La Partie 4 entière est une *taxonomie des surfaces d'attaque*. Le chemin d'attaque, lui, est l'objet d'étude de la modélisation de menace (chapitre 25) et du graphe d'attaque en Active Directory (Partie 8).

🎯 **À retenir** — On défend mieux en *réduisant la surface* qu'en empilant les contrôles sur une surface tentaculaire.

## Chapitre 8 — Contrôles préventifs, détectifs, correctifs et dissuasifs

**Définition.** Tout contrôle de sécurité se classe par sa *fonction temporelle* par rapport à l'incident.

- **Préventif** : empêche l'incident *avant* qu'il survienne (firewall, MFA, durcissement, chiffrement).
- **Détectif** : repère l'incident *pendant* ou *après* (SIEM, EDR, journaux, IDS, alarme).
- **Correctif** : *répare* après l'incident (restauration de sauvegarde, patch, reconstruction).
- **Dissuasif** : *décourage* l'attaquant (bannière légale, visibilité de la surveillance, réputation de robustesse).

On ajoute souvent **compensatoire** (mesure de substitution quand le contrôle idéal est impossible) et **récupératif/recovery**.

🔧 **Exemple concret** — Contre le vol : un verrou (préventif), une caméra (détectif), une assurance (correctif), un panneau « sous surveillance » (dissuasif). La sécurité combine les quatre car aucun n'est suffisant seul.

🧭 **Taxonomie** — Cette grille croise parfaitement le NIST CSF : *Protect* ≈ préventif, *Detect* ≈ détectif, *Respond/Recover* ≈ correctif. Toute défense de la Partie 12 peut être classée ici.

⚠️ **Erreur fréquente** — Tout miser sur le préventif (« assume breach » nous dira que la prévention échouera un jour). Sans détection ni correction, une seule faille devient catastrophique.

🎯 **À retenir** — Une bonne sécurité équilibre prévention, détection et correction. La prévention seule est une illusion.

## Chapitre 9 — Menace opportuniste vs menace ciblée

**Définition.** Classer la menace par son *intentionnalité envers vous*.

- **Menace opportuniste** : l'attaquant ne vous vise pas *vous*, il ratisse large et frappe qui est vulnérable (scans automatisés, ransomware de masse, phishing générique). Vous êtes une cible *parce que* vous étiez faible.
- **Menace ciblée** : l'attaquant vous a *choisi* et investit des efforts spécifiques (espionnage, APT — Advanced Persistent Threat, attaque de la supply chain visant un client précis). Vous êtes une cible *malgré* vos défenses.

**Conséquence défensive.** Contre l'opportuniste, l'hygiène de base suffit souvent (être « moins faible que le voisin »). Contre le ciblé, l'hygiène ne suffit pas : il faut détection avancée, threat hunting, renseignement (CTI).

🧭 **Taxonomie** — Cette distinction structure la *modélisation de menace* (qui m'attaque ?) et le niveau d'investissement défensif justifié.

🎯 **À retenir** — La question « suis-je une cible choisie ou de passage ? » change radicalement la stratégie de défense.

## Chapitre 10 — Risque technique vs risque métier

**Définition.** Un même fait technique a deux lectures.

- **Risque technique** : exprimé en termes de système (« cette vulnérabilité permet une exécution de code à distance », « ce port est exposé »).
- **Risque métier** : exprimé en termes d'*impact pour l'organisation* (« cette vulnérabilité peut interrompre la facturation pendant 3 jours et coûter X € »).

**Pourquoi la traduction est cruciale.** La direction ne décide pas sur des CVE, elle décide sur des conséquences métier. Le rôle de la GRC (Partie 3) est précisément de traduire le technique en métier pour permettre l'arbitrage et le financement.

🔧 **Exemple concret** — « Le serveur SAP n'est pas patché » (technique) devient « la paie de 2 000 salariés peut être bloquée » (métier). Seule la seconde formulation débloque un budget.

⚠️ **Erreur fréquente** — Présenter à la direction des risques uniquement techniques : ils ne seront ni compris ni priorisés.

🧭 **Taxonomie** — Le risque technique alimente le risque métier ; l'analyse de risque (chapitre 30) fait le pont.

🎯 **À retenir** — Un risque qu'on ne sait pas exprimer en langage métier ne sera jamais financé ni traité.

---

# Partie 2 — Grands principes défensifs

> Ces principes sont les **invariants** de la défense. Ils ne dépendent ni de la technologie ni de la mode. Maîtrisés, ils permettent d'évaluer n'importe quelle architecture.

## Chapitre 11 — Défense en profondeur

**Définition.** Empiler *plusieurs couches* de sécurité indépendantes, pour qu'aucune faille unique ne soit fatale. Métaphore du château : douves, remparts, herse, donjon, gardes.

**Principe.** Chaque couche peut échouer ; ce qui protège, c'est que l'attaquant doive *toutes* les franchir. Les couches doivent être **diverses** (pas dix firewalls identiques, mais firewall + segmentation + EDR + MFA + journalisation) pour qu'une même faille ne les traverse pas toutes.

🔧 **Exemple concret** — Un mail malveillant doit franchir : filtrage mail → sensibilisation de l'utilisateur → antivirus → EDR → segmentation → moindre privilège → détection SOC. Chaque couche réduit la probabilité de succès complet.

⚠️ **Erreur fréquente** — La « défense en largeur » : empiler des couches *redondantes* (même type) au lieu de *complémentaires*. Trois antivirus ne valent pas un antivirus + une segmentation.

🧭 **Taxonomie** — Méta-principe qui chapeaute presque tous les autres (segmentation, moindre privilège, MFA en sont des couches).

🎯 **À retenir** — Aucune couche n'est parfaite ; la profondeur transforme une faille unique en simple incident.

## Chapitre 12 — Moindre privilège

**Définition.** Accorder à chaque utilisateur, service ou processus *uniquement* les droits strictement nécessaires à sa fonction, et rien de plus (Principle of Least Privilege, PoLP).

**Principe.** Réduit l'impact d'une compromission : un compte limité, une fois volé, ne donne accès qu'à peu de choses. Inclut la *limitation dans le temps* (droits temporaires, just-in-time) et dans le *périmètre*.

🔧 **Exemple concret** — Une application web qui ne fait que *lire* une base ne doit pas avoir de droits d'*écriture* ni d'*administration*. Si elle est compromise par injection SQL, les dégâts restent limités à de la lecture.

⚠️ **Erreur fréquente** — Donner les droits administrateur « pour que ça marche tout de suite », puis ne jamais les retirer. L'accumulation de droits (privilege creep) est un fléau silencieux.

🧭 **Taxonomie** — Contre-mesure directe de l'*élévation de privilèges* (chapitre 84) et du *lateral movement* (chapitre 144). Pilier du Zero Trust.

🎯 **À retenir** — Le moindre privilège ne *prévient* pas l'intrusion, il en *limite l'impact*. C'est l'application de « assume breach ».

## Chapitre 13 — Besoin d'en connaître

**Définition.** Variante du moindre privilège appliquée à l'*information* : on n'accède à une donnée que si on en a besoin pour sa mission (need-to-know), même si on a l'habilitation théorique.

**Principe.** L'habilitation (niveau de confidentialité autorisé) et le besoin d'en connaître sont *cumulatifs* : avoir le niveau « secret » ne donne pas accès à *tous* les secrets, seulement à ceux nécessaires à sa tâche.

🔧 **Exemple concret** — Un analyste autorisé au niveau « confidentiel » n'a pas à consulter les dossiers RH d'un autre service, même classés au même niveau.

🧭 **Taxonomie** — Issu du monde militaire/renseignement, central dans la classification de l'information (chapitre 34).

🎯 **À retenir** — Habilitation ≠ accès. Le besoin d'en connaître ferme la porte même aux personnes « de confiance ».

## Chapitre 14 — Séparation des tâches

**Définition.** Répartir une action sensible entre *plusieurs personnes* pour qu'aucune seule ne puisse la mener de bout en bout (Separation of Duties, SoD). Le but : prévenir la fraude et l'erreur.

**Principe.** Celui qui *demande* n'est pas celui qui *approuve* ; celui qui *développe* n'est pas celui qui *met en production*. Implique aussi la *rotation* et le *double contrôle* (four-eyes principle).

🔧 **Exemple concret** — Un virement important nécessite un initiateur et un validateur distincts. Un seul compte compromis ne suffit alors pas à détourner les fonds.

🧭 **Taxonomie** — Contrôle organisationnel (GRC), contre-mesure de la fraude interne et de l'abus de privilèges. Complète le moindre privilège côté processus.

🎯 **À retenir** — Diviser une action critique entre plusieurs acteurs supprime le « point unique de malveillance ».

## Chapitre 15 — Cloisonnement et segmentation

**Définition.** *Découper* le système d'information en zones isolées pour qu'un incident dans l'une ne se propage pas aux autres.

- **Cloisonnement** : terme général de séparation logique ou physique entre environnements (prod/dev, métiers, niveaux de sensibilité).
- **Segmentation (réseau)** : découpage du réseau en sous-réseaux/VLAN avec filtrage entre eux, limitant la circulation latérale.

**Principe.** Sans segmentation, une fois un poste compromis, tout le réseau est atteignable (réseau « plat »). Avec segmentation, l'attaquant est contenu dans une zone.

🔧 **Exemple concret** — Isoler le réseau bureautique du réseau industriel (OT) empêche un ransomware bureautique d'arrêter l'usine.

🧭 **Taxonomie** — Contre-mesure majeure du *lateral movement* (chapitre 144). Précurseur de la microsegmentation (chapitre 16) et de la segmentation détaillée en Partie 12.

🎯 **À retenir** — Un réseau plat transforme une intrusion locale en compromission globale. Segmenter, c'est compartimenter le naufrage.

## Chapitre 16 — Microsegmentation

**Définition.** Forme fine de segmentation où l'on isole jusqu'à la *charge de travail individuelle* (machine, conteneur, application), avec des politiques de filtrage au plus près de chaque ressource, indépendantes de la topologie réseau physique.

**Principe.** Plutôt que de cloisonner par grands sous-réseaux, on définit *qui peut parler à qui* au niveau de chaque flux applicatif (par exemple : ce serveur web peut parler à cette base sur ce port, et à rien d'autre). C'est un fondement opérationnel du Zero Trust.

🔧 **Exemple concret** — Dans un datacenter, deux serveurs sur le même sous-réseau ne peuvent communiquer que si une règle explicite l'autorise — l'« est-ouest » est verrouillé.

🧭 **Taxonomie** — Évolution de la segmentation, fortement liée au Zero Trust (chapitre 17) et à la sécurité cloud/conteneurs (Partie 10).

🎯 **À retenir** — La microsegmentation passe du « cloisonner par zones » au « cloisonner par flux ». Le lateral movement devient très coûteux pour l'attaquant.

## Chapitre 17 — Zero Trust

**Définition.** Modèle de sécurité fondé sur « **ne jamais faire confiance, toujours vérifier** » : aucun utilisateur, appareil ou flux n'est implicitement de confiance du seul fait d'être « à l'intérieur » du réseau.

**Principes clés.** Vérification systématique de l'identité et de la posture à *chaque* accès ; accès au plus juste (moindre privilège) ; microsegmentation ; décision contextuelle (qui, quoi, d'où, quel appareil, quel risque) ; chiffrement généralisé. On abandonne le modèle « périmètre = château fort » au profit de « chaque ressource se défend elle-même ».

🔧 **Exemple concret** — Un employé connecté au VPN interne ne reçoit *pas* automatiquement l'accès à toutes les applications : chaque accès est réévalué selon son identité, son appareil et le contexte.

⚠️ **Erreur fréquente** — Croire que Zero Trust est un produit qu'on achète. C'est une *architecture* et une *philosophie*, mise en œuvre par de nombreux composants (IAM, MFA, ZTNA, microsegmentation, EDR).

🧭 **Taxonomie** — Cadre englobant qui combine moindre privilège, microsegmentation, IAM/MFA et assume breach. ZTNA (chapitre 280) en est la brique d'accès réseau.

🎯 **À retenir** — Zero Trust supprime la « confiance par localisation ». Être dans le réseau ne prouve plus rien.

## Chapitre 18 — Assume Breach

**Définition.** Posture mentale et stratégique : *partir du principe qu'on est déjà, ou qu'on sera, compromis*. On ne conçoit plus seulement pour empêcher l'intrusion, mais pour *limiter*, *détecter* et *répondre* quand elle survient.

**Principe.** Renverse l'optimisme défensif. Au lieu de « comment empêcher toute entrée ? », on demande « si l'attaquant est déjà dedans, jusqu'où peut-il aller, et le verrions-nous ? ». Justifie l'investissement dans la détection, la segmentation, le moindre privilège, la sauvegarde et l'exercice de crise.

🧭 **Taxonomie** — Fondement philosophique du Zero Trust et de toute la Partie 11 (détection et réponse). Contre-pied du tout-préventif.

🎯 **À retenir** — « Assume breach » ne signifie pas renoncer à la prévention, mais refuser d'en dépendre exclusivement.

## Chapitre 19 — Tiering d'administration

**Définition.** Organiser les comptes et systèmes d'administration en *niveaux (tiers)* étanches, pour qu'une compromission d'un niveau bas ne permette pas d'atteindre les joyaux.

- **Tier 0** : contrôle de l'identité et de l'infrastructure critique (contrôleurs de domaine, IAM, PKI). Le « cœur du royaume ».
- **Tier 1** : serveurs et applications métier.
- **Tier 2** : postes de travail des utilisateurs.

**Règle d'or.** Un compte d'un tier ne doit *jamais* s'authentifier sur un système d'un tier inférieur (sinon ses identifiants y deviennent volables), et un tier bas ne doit pas contrôler un tier haut.

🔧 **Exemple concret** — Un administrateur du domaine (Tier 0) ne se connecte jamais sur un poste utilisateur (Tier 2) : sinon, un poste compromis exposerait des identifiants Tier 0, permettant la prise totale du domaine.

🧭 **Taxonomie** — Contre-mesure structurante des attaques Active Directory (Partie 8), notamment pass-the-hash et lateral movement. Lié au modèle ESAE.

🎯 **À retenir** — Le tiering empêche qu'un poste banal compromis devienne une prise de contrôle du domaine entier.

## Chapitre 20 — Bastion, PAM et comptes privilégiés

**Définition.** Mesures dédiées à la protection des accès *à hauts privilèges*, qui sont les cibles de plus grande valeur.

- **Bastion** (jump server) : machine d'administration unique et durcie par laquelle *tous* les accès privilégiés transitent et sont journalisés/enregistrés.
- **PAM** (Privileged Access Management) : ensemble d'outils gérant le cycle de vie des comptes à privilèges — coffre-fort de secrets, mots de passe à usage unique, accès « just-in-time », enregistrement de session.
- **Comptes privilégiés** : administrateurs, comptes de service, comptes d'urgence (break-glass).

🔧 **Exemple concret** — Au lieu que chaque admin connaisse le mot de passe « root », le PAM le détient, le change après chaque usage, et n'accorde un accès que temporairement et tracé.

🧭 **Taxonomie** — Brique du tiering (chapitre 19) et du Zero Trust ; défense centrale en Partie 8 et Partie 12.

🎯 **À retenir** — Les comptes privilégiés sont la cible n°1. Sans bastion ni PAM, ils sont aussi le maillon faible.

## Chapitre 21 — Durcissement système

**Définition.** *Hardening* : configurer un système pour réduire sa vulnérabilité — désactiver les services inutiles, fermer les ports superflus, appliquer des configurations sécurisées, supprimer les comptes/défauts d'usine.

**Principe.** Un système installé par défaut est rarement sûr (services activés « au cas où », mots de passe par défaut, protocoles obsolètes). Le durcissement applique des référentiels (par ex. les benchmarks CIS) pour ramener le système à un état minimal et maîtrisé.

🔧 **Exemple concret** — Désactiver SMBv1, supprimer le compte invité, désinstaller les outils non utilisés, désactiver les macros par défaut.

🧭 **Taxonomie** — Réduit la surface d'attaque (chapitre 22) ; contre-mesure transversale (préventive). Détaillé en Partie 12.

🎯 **À retenir** — Un système non durci est une collection de portes ouvertes « par défaut ». Durcir = fermer ce qui ne sert pas.

## Chapitre 22 — Réduction de surface d'attaque

**Définition.** Diminuer activement le nombre de points exploitables : moins de services exposés, moins de comptes, moins de logiciels, moins de droits, moins de données conservées.

**Principe.** Chaque composant exposé est un risque potentiel. La sécurité la plus économique est souvent *l'absence* : ce qui n'existe pas ne peut être attaqué. Recoupe le durcissement, le moindre privilège et la minimisation des données.

🔧 **Exemple concret** — Supprimer une vieille application interne oubliée mais toujours en ligne élimine d'un coup toutes ses vulnérabilités potentielles.

🧭 **Taxonomie** — Principe transversal directement lié à la notion de surface d'attaque (chapitre 7) et à toute la Partie 4.

🎯 **À retenir** — La meilleure défense d'un composant inutile est sa suppression.

## Chapitre 23 — Sécurité par défaut

**Définition.** *Secure by default* : un système doit être sûr *dès l'installation*, sans que l'utilisateur ait à activer des protections. Les options sûres sont l'état par défaut ; l'insécurité doit être un choix explicite.

**Principe.** La plupart des utilisateurs ne modifient jamais les réglages par défaut. Si le défaut est non sécurisé (chiffrement désactivé, mot de passe « admin/admin », tout ouvert), la majorité du parc restera vulnérable.

🔧 **Exemple concret** — Une base de données qui, par défaut, n'écoute que sur localhost et exige un mot de passe — plutôt qu'ouverte au monde sans authentification.

🧭 **Taxonomie** — Couplé à « secure by design » (chapitre 24). Tendance lourde des cadres modernes (CISA « Secure by Design/Default »).

🎯 **À retenir** — Si la sécurité dépend d'une case à cocher que personne ne coche, elle n'existe pas.

## Chapitre 24 — Secure by design

**Définition.** Intégrer la sécurité *dès la conception* d'un système, et non comme une couche ajoutée à la fin. La sécurité est une exigence au même titre que la fonctionnalité.

**Principe.** Corriger une faille à la conception coûte une fraction de ce qu'elle coûte en production. « Secure by design » implique modélisation de menace en amont, choix d'architectures sûres, et exigences de sécurité dans les spécifications. Concept jumeau du *privacy by design* pour les données personnelles.

⚠️ **Erreur fréquente** — Le « bolt-on security » : tenter de sécuriser après coup un produit conçu sans sécurité. C'est cher, partiel et fragile.

🧭 **Taxonomie** — Englobe threat modeling (chapitre 25) et secure by default (chapitre 23). Pilier du développement sécurisé (SAST/DAST en Partie 12).

🎯 **À retenir** — La sécurité ajoutée à la fin est toujours plus chère et moins efficace que la sécurité conçue dès le départ.

## Chapitre 25 — Threat modeling

**Définition.** *Modélisation de menace* : démarche structurée pour identifier, en amont, ce qui peut mal tourner dans un système — quels actifs, quels attaquants, quelles menaces, quelles contre-mesures.

**Méthodes connues.** STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) pour catégoriser les menaces ; arbres d'attaque ; DREAD pour la cotation ; PASTA pour une approche centrée risque. Questions cardinales : *Que construit-on ? Qu'est-ce qui peut mal tourner ? Que fait-on ? A-t-on bien fait ?*

🔧 **Exemple concret** — Avant de développer une API, on liste : actifs (données clients), points d'entrée (endpoints), menaces STRIDE par endpoint, puis contre-mesures (authentification, contrôle d'accès, validation, journalisation).

🧭 **Taxonomie** — Outil central du secure by design ; relie systématiquement *menace → vulnérabilité potentielle → contre-mesure*, soit le fil rouge du cours appliqué à la conception.

🎯 **À retenir** — Le threat modeling déplace la découverte des failles du « après le piratage » vers « avant le code ».

## Chapitre 26 — Journalisation et traçabilité

**Définition.** Enregistrer de manière fiable les événements du système (connexions, actions, erreurs, accès) afin de pouvoir détecter, investiguer et prouver.

**Principe.** Sans journaux, une compromission est invisible et inexplicable. Les journaux doivent être *complets* (bonnes sources), *centralisés* (hors de portée de l'attaquant), *horodatés* (temps synchronisé), *intègres* (non modifiables) et *conservés* assez longtemps.

⚠️ **Erreur fréquente** — Journaliser localement uniquement : un attaquant qui compromet la machine efface ses traces. D'où la centralisation (SIEM) et l'immutabilité.

🧭 **Taxonomie** — Contrôle *détectif* fondamental ; matière première du SOC (Partie 11). Sert aussi l'imputabilité (chapitre 6) et le forensic (chapitre 263).

🎯 **À retenir** — Pas de journaux fiables = pas de détection, pas d'enquête, pas de preuve. La traçabilité est non négociable.

## Chapitre 27 — Supervision continue

**Définition.** *Continuous monitoring* : surveiller en permanence l'état de sécurité (journaux, alertes, vulnérabilités, conformité, posture) plutôt que par audits ponctuels.

**Principe.** Les menaces évoluent en continu ; une évaluation annuelle laisse 364 jours d'angle mort. La supervision continue (alimentée par journalisation, scanners, EDR, SIEM) donne une vue en temps quasi réel et raccourcit drastiquement le délai de détection (MTTD).

🧭 **Taxonomie** — Pilier de la fonction *Detect* (NIST CSF) ; relie journalisation (chapitre 26), SIEM/EDR (Partie 11) et gestion des vulnérabilités (chapitre 32).

🎯 **À retenir** — La sécurité n'est pas un état qu'on atteint, mais une surveillance qu'on maintient.

## Chapitre 28 — Sauvegarde, restauration et résilience

**Définition.**

- **Sauvegarde** : copie des données/systèmes permettant de revenir à un état antérieur sain.
- **Restauration** : capacité *éprouvée* à remettre en service à partir des sauvegardes.
- **Résilience** : aptitude globale de l'organisation à *continuer* et à *se rétablir* malgré l'incident.

**Règle 3-2-1 (et au-delà).** 3 copies, sur 2 supports différents, dont 1 hors site — étendue aujourd'hui à 3-2-1-1-0 : au moins 1 copie **immuable/hors-ligne** (résistante au ransomware) et 0 erreur de restauration vérifiée.

⚠️ **Erreur fréquente** — Sauvegarder sans jamais *tester la restauration*. Une sauvegarde qu'on n'a jamais restaurée n'est pas une sauvegarde, c'est un espoir. De plus, des sauvegardes accessibles en ligne sont chiffrées par le ransomware en même temps que la production.

🧭 **Taxonomie** — Contrôle *correctif/récupératif* clé ; cœur du PRA/PCA (chapitre 267) et seule vraie parade de fond au ransomware (chapitre 188).

🎯 **À retenir** — La sauvegarde immuable et testée est la dernière ligne de défense — souvent la seule qui sauve réellement face au ransomware.

---

# Partie 3 — Gouvernance, risque et conformité (GRC)

> La GRC répond à : *qui décide, sur quelles bases, et comment prouve-t-on qu'on maîtrise ?* C'est la fonction *Govern* placée au centre du NIST CSF 2.0. Sans gouvernance, la technique est aveugle.

## Chapitre 29 — PSSI, politiques, standards et procédures

**Définition.** La documentation de sécurité s'organise en *niveaux* allant du général au précis.

- **PSSI** (Politique de Sécurité des SI) : document fondateur exprimant les *objectifs* et la *volonté* de l'organisation. Le « pourquoi ».
- **Politiques** : règles de haut niveau par domaine (mots de passe, accès, sauvegarde).
- **Standards** : exigences concrètes et obligatoires (« longueur minimale 14 caractères », « TLS 1.2+ »). Le « quoi ».
- **Procédures** : étapes détaillées pour appliquer un standard. Le « comment ».
- **Guides/recommandations** : conseils non obligatoires.

🧭 **Taxonomie** — Pyramide documentaire : PSSI → politiques → standards → procédures. Plus on descend, plus c'est précis et opérationnel.

⚠️ **Erreur fréquente** — Écrire des politiques que personne n'applique ni ne contrôle (« sécurité-papier »). Un document non appliqué crée un faux sentiment de sécurité.

🎯 **À retenir** — La PSSI fixe le cap ; les standards et procédures le rendent applicable et vérifiable.

## Chapitre 30 — Analyse de risque

**Définition.** Démarche structurée pour *identifier, estimer et hiérarchiser* les risques, afin de décider lesquels traiter en priorité.

**Étapes type.** Identifier les actifs → identifier menaces et vulnérabilités → estimer vraisemblance et impact → évaluer le niveau de risque → décider du traitement. Méthodes connues : EBIOS Risk Manager (France/ANSSI), ISO 27005, FAIR (quantitatif, en valeur monétaire).

**Quatre traitements possibles du risque :**
- **Réduire** (mettre des contrôles),
- **Transférer** (assurance, sous-traitance),
- **Éviter** (renoncer à l'activité risquée),
- **Accepter** (assumer le risque résiduel, formellement).

🧭 **Taxonomie** — Cœur de la GRC ; fait le pont entre risque technique et risque métier (chapitre 10). Alimente l'homologation (chapitre 31).

🎯 **À retenir** — On ne traite jamais tous les risques ; on les *priorise* en fonction de vraisemblance × impact, puis on choisit consciemment réduire/transférer/éviter/accepter.

## Chapitre 31 — Homologation et acceptation du risque

**Définition.**

- **Homologation** (accreditation/authorization to operate) : décision *formelle*, prise par une autorité responsable, autorisant un système à fonctionner *en connaissance des risques résiduels*.
- **Acceptation du risque** : reconnaissance explicite et tracée qu'un risque résiduel est assumé par un responsable identifié.

**Principe.** La sécurité parfaite n'existe pas ; il reste toujours un risque résiduel. L'homologation force une *décision consciente et responsable* plutôt qu'un risque subi par défaut. Elle a un propriétaire et une date de revue.

⚠️ **Erreur fréquente** — Laisser le risque résiduel « non décidé » : personne ne l'assume, donc personne ne le surveille. L'acceptation doit être nominative et datée.

🧭 **Taxonomie** — Aboutissement de l'analyse de risque ; relève de la gouvernance (qui *signe*).

🎯 **À retenir** — Accepter un risque est une décision légitime — à condition qu'elle soit explicite, tracée et portée par une autorité.

## Chapitre 32 — Gestion des vulnérabilités

**Définition.** Processus *continu* d'identification, d'évaluation, de priorisation et de correction des vulnérabilités du parc.

**Cycle.** Découverte (scanners, veille CVE, pentest) → évaluation (gravité via CVSS, exploitabilité via EPSS, exposition réelle) → priorisation → remédiation (patch, contournement) → vérification → reporting. Notions clés : **CVE** (identifiant de vulnérabilité), **CVSS** (score de gravité 0–10), **EPSS** (probabilité d'exploitation), **KEV** (catalogue des vulnérabilités activement exploitées de la CISA).

⚠️ **Erreur fréquente** — Prioriser uniquement par CVSS. Une vulnérabilité « critique » non exposée et non exploitée est moins urgente qu'une « moyenne » exposée sur Internet et activement exploitée (présente dans le KEV). Croiser gravité, exploitabilité et exposition.

🧭 **Taxonomie** — Processus GRC opérationnel relié à la gestion des actifs (chapitre 33) et à la supervision continue (chapitre 27).

🎯 **À retenir** — Patcher tout est impossible ; patcher *intelligemment* (gravité × exploitabilité × exposition) est la compétence clé.

## Chapitre 33 — Gestion des actifs

**Définition.** Inventorier et maintenir à jour la connaissance de *tout* ce qu'on possède : matériels, logiciels, services cloud, données, comptes.

**Principe.** « On ne protège que ce qu'on connaît. » Un actif inconnu (shadow IT, serveur oublié) n'est ni patché, ni surveillé, ni sauvegardé — donc une porte d'entrée idéale. La gestion d'actifs alimente toutes les autres fonctions (vulnérabilités, surveillance, sauvegarde).

🔧 **Exemple concret** — Un vieux serveur de test, oublié de l'inventaire, exposé sur Internet et non patché : porte d'entrée classique des intrusions réelles.

🧭 **Taxonomie** — Fonction *Identify* du NIST CSF, prérequis de presque tout le reste. Inclut le **CMDB** et de plus en plus le **CAASM** (gestion de la surface d'attaque).

🎯 **À retenir** — L'inventaire d'actifs n'est pas un sujet « ennuyeux » : c'est la fondation de toute la sécurité. L'inconnu est l'ennemi.

## Chapitre 34 — Classification de l'information

**Définition.** Attribuer à chaque donnée un *niveau de sensibilité* (par ex. public / interne / confidentiel / secret) qui détermine les protections requises.

**Principe.** Toutes les données ne se valent pas. La classification permet d'appliquer des contrôles *proportionnés* : chiffrement, restrictions d'accès (besoin d'en connaître), règles de conservation et de destruction, marquage. Elle est le préalable à la DLP (chapitre 285).

🧭 **Taxonomie** — Relie le besoin d'en connaître (chapitre 13), la confidentialité (chapitre 5) et la protection des données. Base de la gouvernance de la donnée.

🎯 **À retenir** — Sans classification, on protège tout pareil — donc on sur-protège l'inutile et on sous-protège l'essentiel.

## Chapitre 35 — Gestion des exceptions

**Définition.** Processus formel pour *autoriser temporairement* un écart à une règle de sécurité, quand l'application stricte est impossible, avec validation, justification, mesures compensatoires et date d'expiration.

**Principe.** Les exceptions existent toujours (système legacy inpatchable, contrainte métier). Le danger n'est pas l'exception elle-même, mais l'exception *non tracée, non limitée dans le temps, non compensée*. Une bonne gestion les recense, les justifie et les revoit.

⚠️ **Erreur fréquente** — L'exception « provisoire » qui dure des années sans revue. Toute exception doit avoir une échéance et un propriétaire.

🧭 **Taxonomie** — Soupape de la GRC ; étroitement liée à l'acceptation du risque (chapitre 31) et aux mesures compensatoires (chapitre 8).

🎯 **À retenir** — Une exception acceptable est une exception *connue, justifiée, compensée et datée*.

## Chapitre 36 — Audit et contrôle

**Définition.**

- **Contrôle interne** : vérifications *continues* intégrées aux processus (le « premier niveau »).
- **Audit** : évaluation *indépendante et périodique* de la conformité et de l'efficacité des contrôles (interne ou externe).

**Principe.** « Faire confiance, mais vérifier. » L'audit fournit une assurance objective que les politiques sont réellement appliquées et efficaces. Il produit des constats, des écarts (gaps) et des plans d'action. Les **trois lignes de défense** : opérationnels (1), fonctions risque/conformité (2), audit interne (3).

🧭 **Taxonomie** — Contrôle *détectif* au niveau organisationnel ; pilier de la conformité (ISO 27001, SOC 2…).

🎯 **À retenir** — Sans audit, on ne sait pas si la sécurité documentée existe vraiment. L'audit transforme la croyance en preuve.

## Chapitre 37 — Sensibilisation

**Définition.** Programme visant à élever le niveau de vigilance et de compétence des utilisateurs face aux menaces (phishing, mots de passe, ingénierie sociale, manipulation de données).

**Principe.** L'humain est à la fois la cible privilégiée (phishing, social engineering — Partie 9) et un capteur précieux (un employé formé *signale* une attaque). La sensibilisation transforme le « maillon faible » en première ligne de détection. Formes : formations, simulations de phishing, communication régulière, culture du signalement *sans punition*.

⚠️ **Erreur fréquente** — Punir l'utilisateur qui « clique » : il cessera de signaler, ce qui aggrave le risque. On cultive le signalement, on ne le réprime pas.

🧭 **Taxonomie** — Contrôle transversal, à la fois préventif et détectif ; indispensable contre toute la Partie 9.

🎯 **À retenir** — Un utilisateur formé est un capteur de sécurité supplémentaire. La sensibilisation est un investissement à très fort rendement.

## Chapitre 38 — Sécurité des tiers et supply chain

**Définition.** Gérer les risques introduits par les *fournisseurs, prestataires et dépendances* externes — qui ont souvent un accès ou une influence sur votre SI.

**Principe.** Votre sécurité ne vaut que celle de votre maillon le plus faible, y compris externe. Un fournisseur compromis (logiciel, infogérant, composant) devient un vecteur d'attaque (supply chain attack). Mesures : évaluation des fournisseurs, clauses contractuelles de sécurité, droit d'audit, limitation des accès, surveillance.

🔧 **Exemple concret** — Une mise à jour logicielle d'un éditeur de confiance, compromise à la source, distribue une porte dérobée à tous ses clients (cf. dependency confusion, build system compromise — Partie 10).

🧭 **Taxonomie** — Risque transverse relié à la supply chain logicielle (chapitre 81, Partie 10) et à la gestion des tiers. Sujet en forte croissance.

🎯 **À retenir** — Vous héritez du risque de vos fournisseurs. La confiance contractuelle ne remplace pas la vérification.

## Chapitre 39 — Gestion de crise cyber

**Définition.** Dispositif *organisationnel* (et pas seulement technique) pour piloter une crise majeure : décision, coordination, communication, continuité, sous forte pression et incertitude.

**Composants.** Cellule de crise (rôles définis à l'avance), procédures d'escalade, moyens de communication *de secours* (hors du SI potentiellement compromis), plan de communication interne/externe/réglementaire, articulation avec le PRA/PCA. Préparée *à froid* par des exercices (tabletop, chapitre 304).

⚠️ **Erreur fréquente** — Improviser la crise le jour J, communiquer via les outils compromis, ou découvrir que personne ne sait qui décide. La crise se prépare *avant*.

🧭 **Taxonomie** — Niveau de pilotage au-dessus de la réponse à incident technique (Partie 11) ; relié au PRA/PCA (chapitre 267) et à la communication de crise (chapitre 268).

🎯 **À retenir** — La crise cyber se gère avec une cellule, des rôles et des canaux préparés à l'avance — jamais en improvisation.

---

> **Fin du Volume 1/8.**
>
> **Suite prévue :**
> - Volume 2 — Parties 4 & 5 : Taxonomie des surfaces d'attaque & des vulnérabilités
> - Volume 3 — Partie 6 : Attaques web et applicatives
> - Volume 4 — Partie 7 : Attaques réseau et infrastructure
> - Volume 5 — Partie 8 : Identité, Active Directory et privilèges
> - Volume 6 — Partie 9 : Malware, phishing et attaques client-side
> - Volume 7 — Partie 10 : Cloud, API, conteneurs et supply chain
> - Volume 8 — Parties 11 à 13 + Annexes : Détection/SOC/IR, défenses, synthèse, glossaire


---

# Taxonomie de la cybersécurité — Volume 2/8

> Parties 4 & 5 : Taxonomie des surfaces d'attaque · Taxonomie des vulnérabilités
>
> Rappel du fil rouge : **actif → menace → vulnérabilité → risque → attaque → impact → détection → réponse → remédiation**. La Partie 4 répond à *« par où peut-on m'attaquer ? »* (les surfaces). La Partie 5 répond à *« quelle faiblesse est exploitée ? »* (les vulnérabilités). Les attaques elles-mêmes viendront dans les volumes suivants.

---

# Partie 4 — Taxonomie des surfaces d'attaque

> Une **surface d'attaque** est l'ensemble des points exploitables d'un actif. Cette partie cartographie les grandes surfaces du SI moderne. Pour chacune : *ce qu'elle contient*, *pourquoi elle est exposée*, *les attaques typiques*, *les erreurs fréquentes*, *les défenses*. C'est la carte géographique du champ de bataille.

## Chapitre 40 — Poste utilisateur

**Ce qu'elle contient.** Postes de travail (Windows, macOS, Linux), leur système, leurs applications (navigateur, bureautique, lecteurs PDF), les sessions et identifiants de l'utilisateur, ses fichiers locaux.

**Pourquoi exposée.** C'est le point de contact direct entre l'humain et le SI : l'utilisateur ouvre des mails, navigue, branche des clés USB, installe des logiciels. C'est le *point d'entrée n°1* des attaques (phishing, pièce jointe piégée, drive-by).

**Attaques typiques.** Phishing et pièces jointes malveillantes, macro malware, drive-by download, infostealer, vol de jetons de session, exécution de LOLBins, escalade de privilèges locale.

⚠️ **Erreur fréquente** — Donner les droits administrateur local aux utilisateurs : une compromission devient immédiatement totale sur le poste, et facilite le vol d'identifiants.

🛡️ **Défense** — EDR, moindre privilège (pas d'admin local), durcissement, désactivation des macros, filtrage mail/web, application allowlisting, chiffrement disque, mises à jour.

🧭 **Taxonomie** — Souvent le **Tier 2** (chapitre 19) et la première étape d'un chemin d'attaque vers l'identité puis les serveurs.

🎯 **À retenir** — Le poste utilisateur est la porte d'entrée privilégiée : on le suppose tôt ou tard compromis (assume breach) et on limite ce qu'il permet d'atteindre.

## Chapitre 41 — Serveur

**Ce qu'elle contient.** Serveurs applicatifs, bases de données, serveurs de fichiers, contrôleurs de domaine, hyperviseurs — hébergeant services et données de valeur.

**Pourquoi exposée.** Concentration de valeur (données, services critiques) et souvent grande longévité (systèmes legacy, patchs retardés pour ne pas interrompre la production).

**Attaques typiques.** Exploitation de service exposé/non patché, exécution de code à distance (RCE), abus de comptes de service, mouvement latéral, déploiement de ransomware, exfiltration.

⚠️ **Erreur fréquente** — Exposer directement des services d'administration (RDP, SSH, bases) sur Internet ; retarder indéfiniment les patchs critiques.

🛡️ **Défense** — Durcissement, segmentation, gestion stricte des vulnérabilités, accès d'administration via bastion, journalisation, EDR serveur, sauvegardes immuables.

🧭 **Taxonomie** — Typiquement **Tier 1** (applications/données) ou **Tier 0** (contrôleurs de domaine, IAM, PKI — joyaux).

🎯 **À retenir** — Le serveur concentre la valeur : sa compromission a un impact direct sur les actifs essentiels.

## Chapitre 42 — Réseau

**Ce qu'elle contient.** Commutateurs, routeurs, pare-feu, VLAN, protocoles (ARP, DNS, DHCP, BGP), liaisons filaires et sans fil, flux de données en transit.

**Pourquoi exposée.** Le réseau relie *tout* : il transporte identifiants, données et commandes. Un réseau « plat » (non segmenté) permet à un attaquant d'atteindre tout depuis n'importe où.

**Attaques typiques.** Sniffing, spoofing (ARP/DNS/DHCP), MITM, scan/énumération, mouvement latéral, pivoting, DoS/DDoS, attaques sur les protocoles de routage (BGP).

🛡️ **Défense** — Segmentation et microsegmentation, chiffrement en transit (TLS), inspection (NDR/IDS), durcissement des équipements, contrôle d'accès réseau (NAC), supervision des flux.

🧭 **Taxonomie** — Surface centrale traitée en détail en Partie 7. Le réseau est aussi le *terrain* du chemin d'attaque.

🎯 **À retenir** — Un réseau non segmenté transforme toute intrusion locale en compromission globale.

## Chapitre 43 — Active Directory et IAM

**Ce qu'elle contient.** L'annuaire central (Active Directory, Entra ID, LDAP), la gestion des identités et des accès (IAM) : comptes, groupes, droits, authentification (Kerberos, NTLM), politiques (GPO).

**Pourquoi exposée.** C'est le *cerveau des accès* : qui contrôle l'AD/IAM contrôle tout le SI. Surface complexe, riche en relations de confiance et en chemins d'élévation souvent invisibles.

**Attaques typiques.** Kerberoasting, AS-REP roasting, pass-the-hash/ticket, DCSync, abus de délégation, abus d'ACL/GPO, AD CS abuse, password spraying, credential dumping.

🛡️ **Défense** — Tiering (Tier 0), PAM/bastion, durcissement AD, surveillance des objets et ACL, LAPS, désactivation des protocoles faibles, détection comportementale.

🧭 **Taxonomie** — **Tier 0** par excellence ; objet de toute la Partie 8. « L'identité est le nouveau périmètre. »

🎯 **À retenir** — Compromettre l'AD/IAM, c'est souvent compromettre l'entreprise entière. C'est la cible finale de la majorité des intrusions.

## Chapitre 44 — Application web

**Ce qu'elle contient.** Sites et applications accessibles par navigateur : code serveur, code client (JS), sessions, formulaires, logique métier, bases de données associées.

**Pourquoi exposée.** Souvent accessible depuis Internet, par nature ouverte au public, traitant des entrées non fiables. Surface immense et en évolution permanente.

**Attaques typiques.** Toute la Partie 6 : injection (XSS, SQLi), contrôle d'accès cassé (IDOR/BOLA), SSRF, désérialisation, CSRF, abus de logique métier, etc.

🛡️ **Défense** — Secure by design, validation/encodage des entrées-sorties, contrôle d'accès systématique côté serveur, WAF, tests (SAST/DAST/IAST), gestion des dépendances, en-têtes de sécurité (CSP).

🧭 **Taxonomie** — Surface la plus riche en sous-types d'attaques (OWASP Top 10). Détaillée en Partie 6.

🎯 **À retenir** — L'application web traite par définition des entrées hostiles : *ne jamais faire confiance à l'entrée utilisateur* est la règle d'or.

## Chapitre 45 — API

**Ce qu'elle contient.** Interfaces programmatiques (REST, GraphQL, gRPC, SOAP) exposant fonctions et données aux applications, partenaires et clients mobiles.

**Pourquoi exposée.** Les API exposent directement la logique et les données, souvent sans interface humaine pour « masquer » les failles. Multiplication rapide (microservices), documentation parfois publique, contrôle d'accès souvent insuffisant.

**Attaques typiques.** OWASP API Top 10 : BOLA (autorisation au niveau objet cassée), BFLA (au niveau fonction), exposition excessive de données, consommation de ressources non limitée, mauvaise gestion d'inventaire (shadow/zombie APIs).

⚠️ **Erreur fréquente** — Supposer qu'une API « non documentée publiquement » est invisible (sécurité par obscurité). Les endpoints sont découvrables.

🛡️ **Défense** — Authentification/autorisation robustes par objet *et* par fonction, validation de schéma, limitation de débit (rate limiting), inventaire d'API, passerelle API, journalisation.

🧭 **Taxonomie** — Surface en forte croissance ; traitée en Partie 10. L'autorisation par objet (BOLA) est l'équivalent API de l'IDOR web.

🎯 **À retenir** — Les API sont les nouvelles portes du SI ; leur faille la plus fréquente est l'**autorisation** (BOLA/BFLA), pas l'authentification.

## Chapitre 46 — Cloud

**Ce qu'elle contient.** Ressources IaaS/PaaS/SaaS : machines virtuelles, stockage objet (buckets), bases managées, IAM cloud, réseaux virtuels, fonctions serverless, services de secrets.

**Pourquoi exposée.** Surface gérée par configuration (et non plus par périmètre physique) : une simple erreur de configuration expose des données au monde entier. Modèle de **responsabilité partagée** souvent mal compris.

**Attaques typiques.** Buckets publics, secrets/clés exposés, abus du service de métadonnées, élévation de privilèges via IAM mal configuré, mouvement latéral cloud, prise de contrôle de comptes.

⚠️ **Erreur fréquente** — Croire que « le cloud est sécurisé par le fournisseur ». Le fournisseur sécurise *l'infrastructure* ; *vos* configurations et données restent *votre* responsabilité.

🛡️ **Défense** — Moindre privilège IAM, chiffrement, CSPM (détection de mauvaises configurations), gestion des secrets, journalisation cloud, durcissement par défaut, revue des accès.

🧭 **Taxonomie** — Surface détaillée en Partie 10. La mauvaise *configuration* y remplace souvent la *vulnérabilité* logicielle classique.

🎯 **À retenir** — Dans le cloud, l'erreur n°1 est la **mauvaise configuration**, pas la faille logicielle. La responsabilité partagée doit être comprise.

## Chapitre 47 — Conteneurs et Kubernetes

**Ce qu'elle contient.** Images de conteneurs, registres, moteurs d'exécution (Docker/containerd), orchestrateurs (Kubernetes : pods, RBAC, secrets, API server, etcd).

**Pourquoi exposée.** Densité (beaucoup de charges sur un même hôte), images héritées de dépendances vulnérables, complexité de configuration de Kubernetes (RBAC, réseau), API server parfois exposée.

**Attaques typiques.** Image vulnérable/malveillante, registre exposé, abus de RBAC Kubernetes, évasion de conteneur (container escape) vers l'hôte, secrets mal protégés, mouvement latéral entre pods.

🛡️ **Défense** — Images minimales et scannées, registres privés, RBAC au moindre privilège, isolation (politiques réseau, security contexts), gestion des secrets, durcissement de l'orchestrateur, admission control.

🧭 **Taxonomie** — Sous-surface du cloud moderne (Partie 10). L'évasion de conteneur est l'équivalent « escalade vers l'hôte ».

🎯 **À retenir** — Un conteneur n'est pas une frontière de sécurité parfaite : une mauvaise config peut permettre l'évasion vers l'hôte.

## Chapitre 48 — CI/CD

**Ce qu'elle contient.** La chaîne d'intégration et de déploiement continus : dépôts de code, pipelines de build, runners, artefacts, secrets de déploiement, accès aux environnements de production.

**Pourquoi exposée.** La CI/CD a, par conception, des *droits puissants* (déployer en production) et manipule du code et des secrets. La compromettre permet d'injecter du code malveillant *dans tout ce qui est déployé*.

**Attaques typiques.** Pipeline poisoning (injection dans le build), vol de secrets de pipeline, dependency confusion, compromission du système de build, altération d'artefacts, abus de tokens CI.

⚠️ **Erreur fréquente** — Stocker des secrets en clair dans les fichiers de pipeline ou les variables non protégées ; donner aux pipelines des droits de production illimités.

🛡️ **Défense** — Moindre privilège des pipelines, gestion des secrets dédiée, signature des artefacts, isolation des runners, revue de code obligatoire, provenance (SLSA), SBOM.

🧭 **Taxonomie** — Maillon critique de la **supply chain logicielle** (Partie 10). Cible à fort effet de levier.

🎯 **À retenir** — Compromettre la CI/CD, c'est empoisonner la source : le code malveillant est ensuite distribué « légitimement » partout.

## Chapitre 49 — Messagerie

**Ce qu'elle contient.** Serveurs et services de mail, boîtes des utilisateurs, passerelles, protocoles (SMTP, IMAP), mécanismes d'authentification d'expéditeur (SPF/DKIM/DMARC).

**Pourquoi exposée.** Canal d'entrée privilégié des attaques (phishing, malware, BEC), ouvert au monde par nature, reposant sur la confiance de l'utilisateur.

**Attaques typiques.** Phishing/spear phishing, BEC (fraude au président), malspam, usurpation d'expéditeur (spoofing), consent phishing, pièces jointes et liens piégés.

🛡️ **Défense** — Filtrage anti-spam/anti-malware, SPF/DKIM/DMARC, bac à sable des pièces jointes, réécriture/analyse des liens, sensibilisation, MFA pour contrer le vol de comptes.

🧭 **Taxonomie** — Vecteur d'entrée majeur ; relié à toute la Partie 9 (phishing, social engineering).

🎯 **À retenir** — La messagerie est le vecteur d'attaque le plus utilisé ; SPF/DKIM/DMARC + filtrage + sensibilisation forment la base.

## Chapitre 50 — Navigateur

**Ce qu'elle contient.** Le navigateur web et son écosystème : moteur de rendu, JavaScript, extensions, cookies/sessions, stockage local.

**Pourquoi exposée.** C'est l'application la plus exposée à du contenu hostile (chaque site visité est du code non fiable). Très ciblé par les exploits et le vol de session.

**Attaques typiques.** Drive-by download, exploitation de vulnérabilités du moteur, extensions malveillantes, vol de cookies/jetons de session, XSS côté client, malvertising.

🛡️ **Défense** — Mises à jour automatiques, contrôle des extensions, isolation/sandboxing, filtrage web/DNS, politiques (CSP côté sites), navigateur durci, isolation de la navigation à risque.

🧭 **Taxonomie** — Surface client-side ; pont entre le poste utilisateur (chapitre 40) et les attaques web (Partie 6).

🎯 **À retenir** — Le navigateur exécute en permanence du code étranger ; sa mise à jour et son isolation sont critiques.

## Chapitre 51 — Mobile

**Ce qu'elle contient.** Smartphones/tablettes (iOS, Android), applications mobiles, données locales, accès aux ressources d'entreprise (mail, MFA, VPN), capteurs.

**Pourquoi exposée.** Appareils nomades, souvent personnels (BYOD), hors du périmètre, cibles de smishing, d'applications malveillantes et de vol physique. Souvent dépositaires du second facteur MFA.

**Attaques typiques.** Smishing, applications malveillantes, MFA fatigue/SIM swapping, vol/perte d'appareil, exploitation d'OS non mis à jour, interception sur Wi-Fi public.

🛡️ **Défense** — MDM/MAM (gestion de flotte), chiffrement, conteneurisation pro/perso, magasins d'applications contrôlés, mises à jour, MFA résistant au phishing, effacement à distance.

🧭 **Taxonomie** — Extension nomade du poste utilisateur ; relié à l'identité (porteur du MFA) et au social engineering (smishing).

🎯 **À retenir** — Le mobile est souvent le coffre du second facteur : sa compromission peut faire tomber le MFA.

## Chapitre 52 — IoT

**Ce qu'elle contient.** Objets connectés (caméras, capteurs, imprimantes, domotique, dispositifs médicaux), souvent à faible puissance et faible sécurité.

**Pourquoi exposée.** Sécurité native faible (mots de passe par défaut, firmware rarement mis à jour, protocoles non chiffrés), nombre massif, durée de vie longue, souvent non inventoriés (shadow IoT).

**Attaques typiques.** Identifiants par défaut, enrôlement dans des botnets (DDoS), pivot vers le réseau interne, espionnage (caméras/micros), exploitation de firmware non patché.

🛡️ **Défense** — Segmentation dédiée (VLAN IoT isolé), changement des mots de passe par défaut, inventaire, mises à jour firmware, désactivation des services inutiles, supervision.

🧭 **Taxonomie** — Surface en explosion ; souvent un *point de pivot* faible vers des surfaces plus sensibles. Recoupe l'OT (chapitre 53).

🎯 **À retenir** — L'IoT élargit massivement la surface d'attaque avec des objets peu sécurisables : la segmentation est la parade clé.

## Chapitre 53 — OT / ICS

**Ce qu'elle contient.** Technologies opérationnelles : systèmes industriels (ICS), automates (PLC), SCADA, capteurs/actionneurs pilotant des processus physiques (usines, énergie, eau, transport).

**Pourquoi exposée.** Priorité historique à la *disponibilité et la sûreté physique* plutôt qu'à la cybersécurité ; systèmes très anciens, protocoles non chiffrés/non authentifiés, convergence IT/OT qui les expose désormais.

**Attaques typiques.** Sabotage de processus physique, ransomware débordant de l'IT vers l'OT, manipulation d'automates, déni de service industriel. Impact potentiel : *physique* (sécurité des personnes, environnement).

⚠️ **Erreur fréquente** — Appliquer tels quels les outils IT (patchs intempestifs, scans agressifs) sur de l'OT fragile, au risque d'interrompre un processus critique.

🛡️ **Défense** — Séparation stricte IT/OT (modèle de zones type Purdue), diodes/relais unidirectionnels, surveillance passive, durcissement prudent, plans de continuité spécifiques.

🧭 **Taxonomie** — Surface à part : ici l'impact peut être *physique et vital*, ce qui change la hiérarchie CIA (la disponibilité/sûreté prime).

🎯 **À retenir** — En OT, une cyberattaque peut avoir des conséquences physiques. L'isolation IT/OT est la priorité absolue.

## Chapitre 54 — Wi-Fi

**Ce qu'elle contient.** Réseaux sans fil, points d'accès, protocoles de chiffrement (WPA2/WPA3), portails captifs, clients connectés.

**Pourquoi exposée.** Le signal déborde des murs physiques : un attaquant à proximité peut écouter, usurper ou brouiller sans accès filaire.

**Attaques typiques.** Evil twin (faux point d'accès), rogue AP, deauthentication, capture de poignées de main, exploitation de protocoles faibles, interception sur Wi-Fi public.

🛡️ **Défense** — WPA3/WPA2-Enterprise (802.1X), réseaux invités isolés, détection de points d'accès indésirables, VPN sur réseaux non fiables, désactivation des protocoles faibles.

🧭 **Taxonomie** — Sous-surface réseau (Partie 7) ; point d'entrée physique de proximité.

🎯 **À retenir** — Le Wi-Fi étend le réseau au-delà des murs : il faut un chiffrement fort et la détection des faux points d'accès.

## Chapitre 55 — VPN

**Ce qu'elle contient.** Passerelles d'accès distant chiffré au réseau interne, clients VPN, concentrateurs.

**Pourquoi exposée.** Exposé sur Internet *par conception* (point d'entrée distant) et donnant accès au cœur du réseau. Cible récurrente d'exploits critiques et de vol d'identifiants.

**Attaques typiques.** Exploitation de vulnérabilités de la passerelle (RCE), credential stuffing/brute force, contournement de MFA, accès trop large une fois connecté.

⚠️ **Erreur fréquente** — VPN sans MFA, ou donnant un accès *plat* à tout le réseau interne une fois connecté (contraire au Zero Trust).

🛡️ **Défense** — Patch prioritaire des passerelles, MFA résistant au phishing, moindre privilège d'accès, journalisation, et migration progressive vers le **ZTNA** (accès par application plutôt que par réseau).

🧭 **Taxonomie** — Point d'entrée distant majeur ; le ZTNA (chapitre 280) en est le successeur Zero Trust.

🎯 **À retenir** — Le VPN est une porte exposée vers le cœur du réseau : patch + MFA + moindre privilège sont impératifs.

## Chapitre 56 — SaaS

**Ce qu'elle contient.** Applications en ligne tierces (messagerie cloud, CRM, stockage, collaboration), où *vos données* résident chez le fournisseur, gérées par configuration et identités.

**Pourquoi exposée.** Accessible de partout, dépendante de la configuration (partages, permissions) et de la sécurité des identités. Multiplication non maîtrisée (shadow SaaS) et intégrations OAuth à risque.

**Attaques typiques.** Prise de contrôle de comptes (sans MFA), partages publics involontaires, consent phishing (octroi d'autorisations OAuth à une app malveillante), mauvaises configurations, intégrations tierces compromises.

🛡️ **Défense** — SSO + MFA, revue des permissions et partages, contrôle des intégrations OAuth, CASB/SSPM, journalisation des accès, gouvernance des applications autorisées.

🧭 **Taxonomie** — Surface « données hors les murs » ; recoupe l'identité (chapitre 57) et le cloud (Partie 10).

🎯 **À retenir** — En SaaS, la sécurité repose surtout sur l'**identité** et la **configuration** : SSO/MFA et revue des partages sont essentiels.

## Chapitre 57 — Identité

**Ce qu'elle contient.** L'ensemble des comptes, identifiants, jetons, droits et mécanismes d'authentification — humains et machines — à travers tout le SI (on-prem et cloud).

**Pourquoi exposée.** « L'identité est le nouveau périmètre » : dans un monde cloud/SaaS/télétravail, l'identité est ce qui donne accès, indépendamment du réseau. Voler une identité = obtenir ses accès partout.

**Attaques typiques.** Phishing d'identifiants, credential stuffing, password spraying, vol de jetons de session, MFA fatigue, abus d'OAuth, attaques AD (Partie 8).

🛡️ **Défense** — MFA résistant au phishing, SSO, moindre privilège et revue d'accès, gestion des identités (gouvernance IGA), détection des connexions anormales, PAM pour les privilèges.

🧭 **Taxonomie** — Surface transverse et centrale, pont entre AD (chapitre 43), cloud, SaaS et Zero Trust.

🎯 **À retenir** — Protéger l'identité est devenu *la* priorité : c'est elle, plus que le réseau, qui garde les accès.

## Chapitre 58 — Données

**Ce qu'elle contient.** L'information elle-même, dans ses trois états : *au repos* (stockée), *en transit* (sur le réseau), *en cours d'utilisation* (en mémoire/traitement).

**Pourquoi exposée.** Les données sont l'objectif final de la plupart des attaques (vol, chiffrement, falsification). Elles se dispersent (copies, exports, cloud, SaaS, postes), rendant leur protection diffuse.

**Attaques typiques.** Exfiltration, chiffrement (ransomware), falsification (intégrité), fuite par mauvaise configuration, vol de sauvegardes, interception en transit.

🛡️ **Défense** — Classification (chapitre 34), chiffrement au repos et en transit, DLP, contrôle d'accès et besoin d'en connaître, minimisation et rétention maîtrisée, sauvegardes protégées.

🧭 **Taxonomie** — *L'actif* ultime du fil rouge ; toutes les autres surfaces ne sont que des chemins vers la donnée.

🎯 **À retenir** — Les données sont la cible finale ; les protéger dans leurs trois états (repos, transit, usage) est l'objectif de tout le reste.

## Chapitre 59 — Humain

**Ce qu'elle contient.** Les personnes : utilisateurs, administrateurs, dirigeants, prestataires — leurs décisions, leur vigilance, leurs droits.

**Pourquoi exposée.** L'humain prend des décisions sous influence (urgence, autorité, peur, appât du gain) et détient des accès. Il est la cible de l'ingénierie sociale, qui contourne *toutes* les défenses techniques.

**Attaques typiques.** Phishing, vishing, BEC, manipulation/ingénierie sociale, MFA fatigue, menace interne (négligence ou malveillance), corruption.

🛡️ **Défense** — Sensibilisation continue, culture du signalement sans punition, procédures de vérification (double validation des paiements), moindre privilège, séparation des tâches, surveillance des comportements à risque.

🧭 **Taxonomie** — Surface transverse ; cœur de la Partie 9 (social engineering). « On ne patche pas l'humain, on l'accompagne. »

🎯 **À retenir** — L'humain est à la fois la cible la plus exploitée et le meilleur capteur : la sensibilisation est un contrôle de sécurité à part entière.

## Chapitre 60 — Physique

**Ce qu'elle contient.** Les locaux, datacenters, postes, équipements réseau, supports (disques, sauvegardes, clés USB), badges, et l'accès physique en général.

**Pourquoi exposée.** Un accès physique contourne la plupart des protections logiques : « qui contrôle le matériel contrôle souvent les données ». Vol, branchement de périphériques, accès aux consoles.

**Attaques typiques.** Vol d'équipements/supports, intrusion dans les locaux (tailgating), branchement de périphériques malveillants, accès aux consoles/ports, photographie d'écrans, fouille (dumpster diving).

🛡️ **Défense** — Contrôle d'accès physique (badges, sas), vidéosurveillance, chiffrement disque (protège la donnée en cas de vol), verrouillage des sessions, gestion des supports, destruction sécurisée, sensibilisation au tailgating.

🧭 **Taxonomie** — Surface fondamentale souvent négligée ; le chiffrement disque est le pont entre sécurité physique et protection de la donnée.

🎯 **À retenir** — La sécurité logique s'effondre sans sécurité physique : un accès matériel est un quasi-game over, sauf chiffrement.

## Chapitre 61 — Firmware et matériel

**Ce qu'elle contient.** Le code de bas niveau (BIOS/UEFI, firmware des cartes, microcontrôleurs), les composants matériels, les chaînes d'approvisionnement matérielles.

**Pourquoi exposée.** Couche *sous* le système d'exploitation : une compromission y est très furtive, persistante (survit à la réinstallation) et difficile à détecter. Rarement mise à jour, peu surveillée.

**Attaques typiques.** Bootkits/implants firmware, altération de la chaîne d'approvisionnement matérielle, exploitation de vulnérabilités UEFI, attaques par canaux auxiliaires (side-channel), périphériques malveillants.

🛡️ **Défense** — Secure Boot, mesure d'intégrité (TPM, attestation), mises à jour de firmware signées, approvisionnement de confiance, surveillance de l'intégrité, désactivation des interfaces de debug.

🧭 **Taxonomie** — La surface la plus *basse* de la pile ; recoupe la supply chain (chapitre 38) côté matériel. Persistance maximale pour l'attaquant.

🎯 **À retenir** — Une compromission firmware/matériel est furtive et persistante : Secure Boot et intégrité matérielle (TPM) sont les garde-fous.

---

# Partie 5 — Taxonomie des vulnérabilités

> Une **vulnérabilité** est une faiblesse exploitable. Cette partie classe les vulnérabilités par *nature de la faiblesse* (et non par surface). C'est le vocabulaire structuré que **CWE** formalise. Comprendre ces familles permet de prédire les attaques et de choisir les contrôles. Référence utile : **OWASP ASVS** pour vérifier la sécurité applicative.

## Chapitre 62 — Défaut d'authentification

**Définition.** Faiblesse dans la *vérification de l'identité* : il est possible de se faire passer pour un autre, ou de contourner la preuve d'identité.

**Famille / catégorie.** Authentification cassée (OWASP « Identification and Authentication Failures » ; CWE-287 et apparentés).

**Mécanisme.** Mots de passe faibles ou par défaut, absence de MFA, gestion de session défaillante, énumération de comptes, récupération de mot de passe non sécurisée, jetons prévisibles.

**Impacts.** Usurpation d'identité, prise de contrôle de comptes, accès non autorisé.

**Signaux de détection.** Pics d'échecs de connexion (brute force, spraying), connexions depuis lieux/appareils anormaux, multiples comptes ciblés.

🛡️ **Défense** — MFA (idéalement résistant au phishing), politiques de mots de passe modernes, anti-brute-force/limitation, gestion sécurisée de session, messages d'erreur non révélateurs.

⚠️ **Erreur fréquente** — Confondre authentification (qui ?) et autorisation (quels droits ?). Ce chapitre concerne uniquement la *preuve d'identité*.

🎯 **À retenir** — Tout ce qui permet de *prouver faussement qui l'on est* relève du défaut d'authentification. MFA est la parade reine.

## Chapitre 63 — Défaut d'autorisation

**Définition.** Faiblesse dans la *vérification des droits* : un utilisateur authentifié accède à des ressources ou fonctions qui ne lui sont pas destinées.

**Famille / catégorie.** Contrôle d'accès cassé (OWASP « Broken Access Control » — n°1 du Top 10 ; CWE-285, CWE-639, CWE-862).

**Mécanisme.** Contrôles d'accès absents, incohérents, ou réalisés *côté client*, références d'objets non vérifiées (IDOR/BOLA), élévation de privilèges, fonctions d'administration accessibles sans contrôle.

**Impacts.** Accès et modification de données d'autrui, élévation de privilèges, contournement de la logique métier.

**Signaux de détection.** Accès à des identifiants d'objets hors périmètre de l'utilisateur, appels à des endpoints privilégiés par des comptes standard, énumération d'identifiants.

🛡️ **Défense** — Contrôle d'accès *systématique côté serveur*, « deny by default », vérification de propriété de chaque objet, RBAC/ABAC, tests d'autorisation.

🎯 **À retenir** — L'autorisation cassée est la vulnérabilité web n°1. Toujours vérifier *les droits*, à chaque accès, côté serveur — l'authentification ne suffit pas.

## Chapitre 64 — Injection

**Définition.** Faiblesse où une *entrée non fiable* est interprétée comme *du code ou une commande* par un interpréteur incapable de distinguer données et instructions.

**Famille / catégorie.** Injection (OWASP Top 10 ; CWE-74 et enfants : CWE-89 SQLi, CWE-79 XSS, CWE-78 command injection…).

**Mécanisme.** L'application mélange données utilisateur et structure de la requête/commande. L'interpréteur (SQL, shell, navigateur, LDAP, moteur de templates) exécute la partie injectée.

**Sous-types (détaillés en Partie 6).** SQLi, XSS, command injection, LDAP injection, XPath injection, SSTI, NoSQL injection, CRLF/header injection.

**Impacts.** Lecture/modification de données, exécution de code, contournement d'authentification, compromission du serveur.

🛡️ **Défense** — Séparer code et données : requêtes paramétrées/préparées, API sûres, encodage contextuel des sorties, validation par allowlist, moindre privilège de l'interpréteur.

🧭 **Taxonomie** — *La* méta-famille applicative : un seul principe (« données traitées comme du code ») génère de nombreux sous-types selon l'interpréteur.

🎯 **À retenir** — Toute injection a la même racine : un interpréteur confond données et instructions. La parade universelle est de *séparer* les deux (paramétrage + encodage).

## Chapitre 65 — Mauvaise validation d'entrée

**Définition.** L'application accepte des entrées sans vérifier qu'elles sont conformes à ce qui est attendu (type, format, longueur, plage, jeu de caractères).

**Famille / catégorie.** Validation d'entrée incorrecte (CWE-20).

**Mécanisme.** Faute amont qui *alimente* de nombreuses autres failles (injection, débordement, logique métier). Distinguer validation (l'entrée est-elle bien formée ?) et encodage de sortie (l'afficher sans danger).

**Impacts.** Variés : injection, corruption de données, plantage, contournement de règles.

🛡️ **Défense** — Validation stricte côté serveur par **allowlist** (ce qui est autorisé) plutôt que blocklist (ce qui est interdit), contrôles de type/format/longueur, rejet par défaut.

⚠️ **Erreur fréquente** — Valider uniquement côté client (contournable) ou se fier à une blocklist (toujours incomplète).

🎯 **À retenir** — La validation par allowlist côté serveur est une défense en profondeur qui coupe la racine de nombreuses attaques.

## Chapitre 66 — Mauvaise gestion de session

**Définition.** Faiblesse dans la création, la protection ou l'invalidation des sessions, permettant de voler ou détourner la session d'un utilisateur.

**Famille / catégorie.** Gestion de session défaillante (CWE-384 fixation, CWE-613 expiration).

**Mécanisme.** Identifiants de session prévisibles, non régénérés après connexion (fixation), transmis sans chiffrement, sans expiration, ou stockés de façon vulnérable au vol (XSS volant les cookies).

**Impacts.** Détournement de session (session hijacking), usurpation, accès persistant.

🛡️ **Défense** — Jetons aléatoires forts, régénération à l'authentification, cookies `HttpOnly`/`Secure`/`SameSite`, expiration et invalidation à la déconnexion, transport chiffré (TLS).

🧭 **Taxonomie** — À l'intersection de l'authentification (chapitre 62) et des attaques web (CSRF, XSS, fixation — Partie 6).

🎯 **À retenir** — Une session mal gérée annule une authentification forte : protéger le jeton est aussi important que vérifier l'identité.

## Chapitre 67 — Mauvaise configuration

**Définition.** Le système est *fonctionnel mais mal réglé* du point de vue sécurité : options par défaut dangereuses, services inutiles, permissions trop larges, comptes par défaut.

**Famille / catégorie.** Security Misconfiguration (OWASP Top 10 ; CWE-16, CWE-732).

**Mécanisme.** Pas une faille de code, mais un *réglage*. Très fréquent dans le cloud (buckets publics), les bases de données (sans mot de passe), les en-têtes web manquants, les pages d'administration exposées.

**Impacts.** Exposition de données, accès non autorisé, point d'entrée facile.

🛡️ **Défense** — Durcissement selon des référentiels (CIS), secure by default, suppression des comptes/services par défaut, gestion de configuration (IaC, baseline), CSPM dans le cloud, revues régulières.

🧭 **Taxonomie** — Famille dominante dans le cloud (Partie 10) ; cousine du défaut de durcissement (chapitre 21).

🎯 **À retenir** — La majorité des incidents cloud viennent d'une *configuration*, pas d'une *vulnérabilité logicielle*. Le durcissement par défaut est la parade.

## Chapitre 68 — Chiffrement faible ou absent

**Définition.** Données sensibles non chiffrées, ou protégées par une cryptographie obsolète/mal implémentée.

**Famille / catégorie.** Cryptographic Failures (OWASP Top 10 ; CWE-327 algorithme faible, CWE-311 absence de chiffrement).

**Mécanisme.** Pas de chiffrement en transit/au repos, algorithmes cassés (MD5, SHA1, DES), clés mal gérées, mauvais modes, hachage de mots de passe inadéquat, certificats mal validés.

**Impacts.** Interception et lecture de données, vol d'identifiants, atteinte à la confidentialité et à l'intégrité.

🛡️ **Défense** — TLS récent en transit, chiffrement au repos, algorithmes éprouvés, hachage de mots de passe adapté (Argon2/bcrypt/scrypt), gestion de clés rigoureuse (rotation, séparation), validation stricte des certificats.

⚠️ **Erreur fréquente** — « Chiffrer » avec un algorithme obsolète ou des clés mal gérées : faux sentiment de sécurité. Et ne jamais inventer sa propre crypto.

🎯 **À retenir** — Le chiffrement protège la donnée même en cas de vol — à condition d'algorithmes modernes et d'une *gestion de clés* sérieuse.

## Chapitre 69 — Fuite d'information

**Définition.** Le système révèle, involontairement, des informations utiles à un attaquant (détails techniques, données internes, secrets).

**Famille / catégorie.** Information Exposure (CWE-200 et apparentés).

**Mécanisme.** Messages d'erreur verbeux (traces de pile, versions, requêtes SQL), métadonnées, commentaires de code, endpoints de debug, en-têtes révélateurs, énumération de comptes.

**Impacts.** Facilite la reconnaissance et le ciblage ; parfois exposition directe de données ou de secrets.

🛡️ **Défense** — Messages d'erreur génériques, désactivation du mode debug en production, suppression des métadonnées/commentaires sensibles, en-têtes minimaux, réponses uniformes (anti-énumération).

🧭 **Taxonomie** — Souvent une faille *préparatoire* (aide la reconnaissance), parfois un impact en soi (exposition de secrets — chapitre 77).

🎯 **À retenir** — Chaque détail révélé est un cadeau à l'attaquant : la discrétion (erreurs génériques, pas de debug en prod) est une défense.

## Chapitre 70 — Vulnérabilités mémoire

**Définition.** Faiblesses dans la gestion de la mémoire des programmes (souvent en langages bas niveau comme C/C++) permettant de corrompre l'exécution.

**Famille / catégorie.** Memory safety (CWE-119 famille : CWE-787 écriture hors limites, CWE-416 use-after-free, CWE-476 déréférencement null).

**Mécanisme.** Débordement de tampon (buffer overflow), use-after-free, lecture/écriture hors limites, dépassement d'entier — pouvant mener à l'exécution de code arbitraire ou au plantage.

**Impacts.** Exécution de code (RCE), élévation de privilèges, déni de service, fuite mémoire de données.

🛡️ **Défense** — Langages à sûreté mémoire (Rust, Go, langages managés), protections compilateur/OS (ASLR, DEP, stack canaries), validation des tailles, fuzzing, revues de code, mises à jour.

🧭 **Taxonomie** — Famille reine des vulnérabilités *systèmes/binaires* (historiquement la base de l'exploitation). Concerne surtout logiciels natifs, OS, firmware.

🎯 **À retenir** — Les bugs mémoire restent une source majeure de RCE ; la tendance de fond est l'adoption de langages à *sûreté mémoire*.

## Chapitre 71 — Dépendances vulnérables

**Définition.** L'application intègre des composants tiers (bibliothèques, frameworks) qui contiennent des vulnérabilités connues.

**Famille / catégorie.** Vulnerable and Outdated Components (OWASP Top 10 ; CWE-1104, CWE-1395).

**Mécanisme.** Le code moderne est fait à 80–90 % de dépendances. Une faille dans l'une d'elles (souvent largement répandue) devient une faille de votre application, sans que vous ayez écrit le code fautif.

**Impacts.** Hérités de la dépendance : RCE, fuite, déni de service ; effet de masse (une CVE touche des millions d'applications).

🛡️ **Défense** — Inventaire des dépendances (**SBOM**), analyse de composition logicielle (**SCA**), mises à jour régulières, suivi des CVE, minimisation des dépendances, vérification d'intégrité.

🧭 **Taxonomie** — Pont vers la supply chain logicielle (chapitre 81, Partie 10). Distincte des dépendances *malveillantes* (typosquatting), qui relèvent de la supply chain offensive.

🎯 **À retenir** — Vous héritez des failles de tout ce que vous importez : connaître (SBOM) et surveiller (SCA) ses dépendances est indispensable.

## Chapitre 72 — Logique métier

**Définition.** Faiblesse non pas technique mais *fonctionnelle* : l'application fonctionne « comme codée » mais sa logique permet un abus que le concepteur n'avait pas prévu.

**Famille / catégorie.** Business Logic Flaws (CWE-840).

**Mécanisme.** Détournement des règles métier : enchaîner des étapes dans le désordre, manipuler des quantités/prix négatifs, abuser de remises cumulables, contourner des limites, exploiter des conditions de course métier.

**Impacts.** Fraude, perte financière, contournement de contrôles, abus de service — souvent invisibles aux scanners (rien n'est « techniquement » cassé).

🔧 **Exemple concret** — Appliquer un même bon de réduction des milliers de fois, ou commander une quantité négative pour se faire créditer.

🛡️ **Défense** — Modélisation de menace métier, validation des règles côté serveur, contrôles de cohérence, tests fonctionnels orientés abus, limites et plafonds, supervision des comportements anormaux.

⚠️ **Erreur fréquente** — Croire qu'un scanner automatique détecte ces failles : elles exigent une *compréhension du métier*, donc un test humain.

🎯 **À retenir** — La logique métier cassée n'est pas un bug technique mais un *abus de fonctionnement* : seuls la réflexion métier et le test humain la révèlent.

## Chapitre 73 — Race condition

**Définition.** Faiblesse où le résultat dépend de l'*ordre/temporalité* d'opérations concurrentes, exploitable en agissant dans une fenêtre temporelle critique.

**Famille / catégorie.** Concurrency / TOCTOU (CWE-362, CWE-367 « Time-of-check to time-of-use »).

**Mécanisme.** Entre le moment où une condition est *vérifiée* et celui où elle est *utilisée*, l'attaquant modifie l'état. Ou : des requêtes simultanées contournent une limite censée être unique.

**Impacts.** Double dépense, contournement de limites/quotas, élévation de privilèges, corruption de données.

🔧 **Exemple concret** — Lancer simultanément plusieurs retraits pour dépasser un solde censé être vérifié une seule fois (variante métier de la race condition).

🛡️ **Défense** — Opérations atomiques, verrous, transactions, contrôles d'idempotence, vérification *au moment de l'usage*, limitation de la concurrence.

🧭 **Taxonomie** — Recoupe la logique métier (chapitre 72) quand elle est exploitée fonctionnellement ; relève du système quand elle est bas niveau (TOCTOU).

🎯 **À retenir** — Une vérification suivie d'une action non atomique ouvre une fenêtre exploitable : l'atomicité est la parade.

## Chapitre 74 — Désérialisation

**Définition.** Faiblesse où des données sérialisées *non fiables* sont reconstruites en objets par l'application, permettant d'altérer l'exécution.

**Famille / catégorie.** Insecure Deserialization (CWE-502 ; OWASP « Software and Data Integrity Failures »).

**Mécanisme.** La désérialisation peut instancier des objets et déclencher du code (chaînes de gadgets), surtout dans les formats binaires riches. Une charge sérialisée malveillante peut alors mener à l'exécution de code.

**Impacts.** Exécution de code à distance (souvent), élévation de privilèges, manipulation d'objets, déni de service.

🛡️ **Défense** — Éviter de désérialiser des données non fiables, préférer des formats de données simples (JSON sans types), signer/chiffrer les données sérialisées, allowlist de classes, isolation.

🧭 **Taxonomie** — Famille « intégrité logicielle » ; détaillée côté attaque en Partie 6 (chapitre 114).

🎯 **À retenir** — Désérialiser une entrée non fiable revient souvent à exécuter du code étranger : ne jamais désérialiser sans contrôle d'intégrité et de type.

## Chapitre 75 — Erreurs de parsing

**Définition.** Faiblesses dans l'*analyse* de formats de données (XML, JSON, fichiers, URL, protocoles) : ambiguïtés, incohérences entre analyseurs, comportements inattendus.

**Famille / catégorie.** Improper Input Parsing (familles CWE liées à l'interprétation des entrées).

**Mécanisme.** Différences d'interprétation entre deux composants (parser differential), entités externes (XXE), expansion incontrôlée (« billion laughs »), confusion d'encodage, désynchronisation de protocole (request smuggling).

**Impacts.** Contournement de contrôles, déni de service, lecture de fichiers (XXE), désynchronisation HTTP, injection.

🛡️ **Défense** — Analyseurs robustes et à jour, désactivation des fonctionnalités dangereuses (entités externes XML), limites de taille/profondeur, normalisation des entrées, cohérence des composants en chaîne.

🧭 **Taxonomie** — Sous-tend XXE, request smuggling, certaines injections (Partie 6). Racine : *« deux composants ne lisent pas la même chose de la même façon »*.

🎯 **À retenir** — Quand deux analyseurs interprètent différemment la même donnée, l'écart devient exploitable. Normaliser et durcir les parsers ferme cette porte.

## Chapitre 76 — Permissions excessives

**Définition.** Comptes, fichiers, services ou rôles disposant de *plus de droits que nécessaire*, augmentant l'impact de toute compromission.

**Famille / catégorie.** Incorrect/Excessive Permissions (CWE-732, CWE-250 « exécution avec privilèges superflus »).

**Mécanisme.** Violation directe du moindre privilège : droits accordés « pour que ça marche » et jamais réduits, rôles cloud trop larges, fichiers world-writable, comptes de service surpuissants.

**Impacts.** Amplifie l'élévation de privilèges et le mouvement latéral ; transforme une petite faille en compromission étendue.

🛡️ **Défense** — Moindre privilège strict, revues d'accès régulières, just-in-time access, suppression du privilege creep, analyse des permissions (notamment IAM cloud), séparation des tâches.

🧭 **Taxonomie** — Manifestation concrète de la violation du moindre privilège (chapitre 12) ; aggrave presque toutes les autres familles.

🎯 **À retenir** — Les permissions excessives ne *créent* pas l'intrusion mais en *décuplent* l'impact. La revue d'accès est une hygiène continue.

## Chapitre 77 — Exposition de secrets

**Définition.** Des secrets (mots de passe, clés API, jetons, certificats, chaînes de connexion) se retrouvent accessibles là où ils ne devraient pas.

**Famille / catégorie.** Secrets Exposure (CWE-798 « identifiants codés en dur », CWE-312/522).

**Mécanisme.** Secrets dans le code source, les dépôts Git (et leur historique), les images de conteneurs, les fichiers de configuration, les logs, les variables d'environnement exposées, les buckets publics.

**Impacts.** Accès direct et immédiat aux systèmes/services protégés par ces secrets ; souvent un raccourci catastrophique pour l'attaquant.

🛡️ **Défense** — Gestionnaire de secrets dédié (coffre-fort), interdiction des secrets en dur, **secrets scanning** (pré-commit et CI), rotation, révocation rapide, principe « pas de secret dans le code/les logs ».

🧭 **Taxonomie** — Recoupe fuite d'information (chapitre 69) et mauvaise configuration (chapitre 67) ; vecteur récurrent dans le cloud et la CI/CD.

🎯 **À retenir** — Un secret exposé est une clé laissée sur la porte : scanner, externaliser dans un coffre, et faire tourner les secrets sont impératifs.

## Chapitre 78 — Logging insuffisant

**Définition.** Absence, insuffisance ou mauvaise protection des journaux, empêchant de détecter, comprendre et prouver une attaque.

**Famille / catégorie.** Security Logging and Monitoring Failures (OWASP Top 10 ; CWE-778).

**Mécanisme.** Événements de sécurité non journalisés, journaux locaux effaçables, absence de centralisation, pas d'alerte, horloges non synchronisées, rétention trop courte.

**Impacts.** Détection tardive ou nulle, investigation impossible, perte de preuves, temps de présence de l'attaquant (dwell time) prolongé.

🛡️ **Défense** — Journalisation des événements de sécurité, centralisation (SIEM) hors de portée de l'attaquant, intégrité et horodatage fiables, alerting, rétention adaptée, tests de détection.

🧭 **Taxonomie** — Symétrique défensif de la Partie 11 ; sans logs, pas de SOC ni de forensic. Relié à la traçabilité (chapitre 26).

🎯 **À retenir** — Ne pas journaliser, c'est être aveugle : une attaque non vue est une attaque non traitée, qui dure.

## Chapitre 79 — Absence de limitation de débit

**Définition.** Le système ne limite pas le *nombre de requêtes/actions* dans le temps, permettant l'abus par répétition massive.

**Famille / catégorie.** Improper Rate Limiting / Resource Consumption (CWE-770, CWE-799 ; OWASP API « Unrestricted Resource Consumption »).

**Mécanisme.** Sans plafond, l'attaquant peut brute-forcer des identifiants, énumérer des objets, scraper des données, ou épuiser les ressources (déni de service applicatif, surcoût cloud).

**Impacts.** Brute force/credential stuffing facilités, énumération de données, déni de service, explosion de coûts (cloud).

🛡️ **Défense** — Limitation de débit (par IP/compte/clé), quotas, throttling progressif, CAPTCHA ciblé, détection d'anomalies, contrôles de coût côté cloud.

🧭 **Taxonomie** — Facilitateur transverse : aggrave authentification (chapitre 62), autorisation (énumération), API (chapitre 45) et disponibilité.

🎯 **À retenir** — Sans limitation de débit, beaucoup d'attaques « lentes » deviennent triviales par la force brute. Plafonner est une défense simple et puissante.

## Chapitre 80 — Rupture de frontière de confiance

**Définition.** Faiblesse où une *frontière de confiance* (entre zones de niveaux de fiabilité différents) est franchie sans contrôle adéquat : on traite une donnée/un appelant non fiable comme fiable.

**Famille / catégorie.** Trust Boundary Violation (CWE-501).

**Mécanisme.** Données venant d'une zone non fiable (Internet, client, tiers) acceptées sans revalidation dans une zone de confiance ; confiance implicite accordée au réseau interne, au client, ou à un système amont.

**Impacts.** Sert de socle à l'injection, à la falsification de données, au contournement de contrôles ; cœur conceptuel de nombreux abus.

🔧 **Exemple concret** — Faire confiance à un prix calculé côté client, ou à un en-tête « interne » falsifiable, parce qu'il « vient de l'intérieur ».

🛡️ **Défense** — Identifier explicitement les frontières de confiance (threat modeling), revalider à chaque franchissement, ne jamais faire confiance au client ni à la localisation réseau (Zero Trust), contrôles côté serveur.

🧭 **Taxonomie** — Concept *transversal* qui sous-tend presque toutes les autres familles ; au cœur du Zero Trust (chapitre 17).

🎯 **À retenir** — Chaque fois qu'une donnée franchit une frontière de confiance, elle doit être revalidée. La confiance implicite est la racine de bien des failles.

## Chapitre 81 — Supply chain logicielle

**Définition.** Vulnérabilités introduites *par* ou *dans* la chaîne de production logicielle : dépendances, outils de build, distribution, mises à jour.

**Famille / catégorie.** Software Supply Chain (OWASP « Software and Data Integrity Failures » ; familles CWE liées à l'intégrité).

**Mécanisme.** Au-delà des dépendances simplement *vulnérables* (chapitre 71), la supply chain ajoute la dimension *malveillante et amont* : paquets piégés (typosquatting, dependency confusion), build compromis, mises à jour signées détournées, artefacts altérés.

**Impacts.** Compromission massive et « de confiance » (le code malveillant arrive par un canal légitime) ; très difficile à détecter.

🛡️ **Défense** — SBOM, provenance et intégrité (signatures, **SLSA**), dépôts internes filtrés, verrouillage des versions, vérification des paquets, isolation de la CI/CD, revue des mises à jour tierces.

🧭 **Taxonomie** — Pont entre la Partie 5 (faiblesse) et la Partie 10 (attaques supply chain) ; recoupe la gestion des tiers (chapitre 38).

🎯 **À retenir** — La supply chain transforme la confiance en vecteur d'attaque : ce qui arrive « par un canal de confiance » doit tout de même être vérifié (intégrité, provenance).

---

> **Fin du Volume 2/8.**
>
> **Acquis :** vous savez désormais cartographier *où* l'on peut être attaqué (Partie 4 — surfaces) et nommer *quelle faiblesse* est exploitée (Partie 5 — vulnérabilités, vocabulaire CWE).
>
> **Suite — Volume 3 : Partie 6, Attaques web et applicatives** (le plus dense : Broken Access Control, IDOR/BOLA, toute la famille XSS, toute la famille SQLi, command/LDAP/XPath injection, SSTI, XXE, SSRF, file inclusion, désérialisation, CSRF, clickjacking, CORS, request smuggling, cache poisoning, prototype pollution, GraphQL abuse…). Chaque grande attaque y suivra le format en 10 points : définition · famille · principe · sous-types · exemple conceptuel · impacts · détection · prévention · erreurs fréquentes · à retenir.


---

# Taxonomie de la cybersécurité — Volume 3/8

> Partie 6 : Attaques web et applicatives
>
> C'est la partie la plus dense du cours, car la surface web (chapitre 44) concentre le plus grand nombre de sous-types d'attaques. Les grandes attaques suivent le **format en 10 points** : 1) Définition · 2) Famille · 3) Principe · 4) Sous-types · 5) Exemple conceptuel (sans payload) · 6) Impacts · 7) Signaux de détection · 8) Prévention · 9) Erreurs fréquentes · 10) À retenir.
>
> **Rappel de posture** : on explique les *mécanismes* et les *défenses*, jamais de charge offensive exploitable. Les « exemples » restent conceptuels.

---

# Partie 6 — Attaques web et applicatives

## Vue d'ensemble taxonomique de la Partie 6

Les attaques web se rangent en quelques grandes familles, qu'il faut garder en tête :

- **Contrôle d'accès cassé** : on accède à ce qui ne nous appartient pas (IDOR/BOLA, élévation de privilèges).
- **Injection** : on fait exécuter du code/des commandes (XSS, SQLi, command, LDAP, XPath, SSTI, XXE).
- **Falsification de requêtes** : on fait agir le serveur ou le navigateur à notre place (SSRF, CSRF).
- **Accès aux fichiers** : on lit/écrit des fichiers non prévus (LFI/RFI, path traversal, upload, Zip Slip).
- **Confiance et intégrité** : on abuse de la confiance accordée (désérialisation, CORS, open redirect, host header, prototype pollution).
- **Protocole/infrastructure web** : on exploite la couche HTTP/cache (request smuggling, cache poisoning, web cache deception).
- **Logique et abus** : on détourne le fonctionnement prévu (business logic, rate limit bypass, GraphQL abuse).

🧭 **Taxonomie** — Quand vous rencontrez une attaque web inconnue, rattachez-la d'abord à l'une de ces sept familles : vous saurez immédiatement quel type de défense s'applique.

---

## Chapitre 82 — Broken Access Control

1. **Définition.** Faille permettant à un utilisateur d'agir au-delà de ses permissions : accéder, modifier ou supprimer des ressources/fonctions qui ne lui sont pas destinées.
2. **Famille.** Contrôle d'accès cassé (OWASP Top 10 n°1 ; CWE-285/862). Famille parente d'IDOR/BOLA et de l'élévation de privilèges.
3. **Principe.** Le contrôle d'autorisation est absent, incomplet, incohérent ou réalisé côté client. Le serveur exécute une action sans vérifier que l'appelant y a droit *pour cet objet précis*.
4. **Sous-types.** IDOR/BOLA (objets), BFLA (fonctions), élévation verticale/horizontale, forced browsing (accès direct à des URL non liées), contournement par paramètre, fonctions d'administration exposées.
5. **Exemple conceptuel.** Une page affiche « ma facture » via un identifiant dans l'URL ; en changeant l'identifiant, on accède à la facture d'autrui — parce que le serveur ne vérifie pas la propriété.
6. **Impacts.** Accès/modification de données d'autrui, élévation de privilèges, contournement de la logique métier, fuite massive de données.
7. **Détection.** Accès à des identifiants hors périmètre, appels d'endpoints privilégiés par des comptes standard, énumération séquentielle d'identifiants, schémas d'accès anormaux.
8. **Prévention.** Contrôle d'accès *systématique côté serveur*, « deny by default », vérification de propriété à chaque accès, RBAC/ABAC centralisé, refus d'exposer la logique d'autorisation au client, tests d'autorisation automatisés.
9. ⚠️ **Erreur fréquente.** Masquer un bouton dans l'interface et croire la fonction protégée : l'endpoint reste appelable directement (« sécurité par l'UI »).
10. 🎯 **À retenir.** N°1 du Top 10. L'authentification dit *qui* ; le contrôle d'accès doit dire *a-t-il le droit, pour cet objet précis* — à chaque requête, côté serveur.

## Chapitre 83 — IDOR / BOLA

1. **Définition.** *Insecure Direct Object Reference* (web) / *Broken Object Level Authorization* (API) : accéder à un objet en manipulant sa référence (identifiant), sans contrôle de propriété.
2. **Famille.** Sous-type majeur du Broken Access Control (chapitre 82).
3. **Principe.** L'application expose une référence directe à un objet (id numérique, nom de fichier, UUID) et se fie à cette référence sans vérifier que l'utilisateur courant en est bien le propriétaire/autorisé.
4. **Sous-types.** IDOR sur identifiants séquentiels (énumérables), sur UUID (devinables s'ils fuitent), en lecture vs écriture/suppression, sur fichiers, sur paramètres imbriqués.
5. **Exemple conceptuel.** Une API renvoie `/api/orders/{id}` ; en incrémentant `{id}`, on lit les commandes des autres clients faute de vérification d'appartenance.
6. **Impacts.** Fuite de données personnelles à grande échelle, modification/suppression de données d'autrui, violation de confidentialité réglementée.
7. **Détection.** Énumération d'identifiants, un même compte accédant à de nombreux objets distincts, accès à des id jamais « possédés » par l'utilisateur.
8. **Prévention.** Vérifier la *propriété/autorisation* de chaque objet côté serveur ; préférer des références indirectes ou liées à la session ; ne pas se reposer sur l'imprévisibilité d'un UUID ; tests d'autorisation par objet.
9. ⚠️ **Erreur fréquente.** Penser qu'un UUID « non devinable » protège : c'est de l'obscurité, pas du contrôle d'accès. Un UUID qui fuite (logs, référents) reste exploitable.
10. 🎯 **À retenir.** L'IDOR/BOLA est la faille d'autorisation la plus répandue (surtout en API) : *toujours* vérifier que l'utilisateur a le droit sur *cet objet*, jamais se fier à la seule référence.

## Chapitre 84 — Élévation de privilèges verticale et horizontale

1. **Définition.** Obtenir des droits supérieurs (verticale) ou accéder aux ressources d'un pair de même niveau (horizontale).
2. **Famille.** Broken Access Control (chapitre 82).
3. **Principe.** *Verticale* : un utilisateur standard accède à des fonctions d'administration. *Horizontale* : un utilisateur accède aux données d'un autre utilisateur de même rôle (l'IDOR en est une forme).
4. **Sous-types.** Verticale (user → admin), horizontale (user A → user B), via mass assignment (modifier son propre rôle), via fonctions cachées, via paramètres de rôle manipulables.
5. **Exemple conceptuel.** Un formulaire de profil accepte un champ `role` non prévu ; l'envoyer avec `role=admin` élève les privilèges si le serveur l'assigne aveuglément (mass assignment).
6. **Impacts.** Prise de contrôle de comptes, accès administrateur, compromission étendue de l'application.
7. **Détection.** Comptes standard exécutant des actions privilégiées, modifications de rôle inattendues, accès croisés entre utilisateurs.
8. **Prévention.** Contrôles d'accès par fonction *et* par objet, allowlist des champs modifiables (contre le mass assignment), séparation nette des rôles, refus par défaut, tests d'élévation.
9. ⚠️ **Erreur fréquente.** Lier des attributs de requête directement aux objets internes (mass assignment) sans filtrer les champs autorisés.
10. 🎯 **À retenir.** Verticale = monter en droits ; horizontale = aller chez le voisin. Les deux se préviennent par un contrôle d'accès strict, par fonction et par objet.

## Chapitre 85 — XSS — vue d'ensemble

1. **Définition.** *Cross-Site Scripting* : injection de scripts exécutés dans le navigateur d'autres utilisateurs, dans le contexte du site de confiance.
2. **Famille.** Injection (chapitre 64), côté client. CWE-79.
3. **Principe.** L'application renvoie une donnée contrôlée par l'attaquant *sans encodage adapté au contexte*, si bien que le navigateur l'interprète comme du code (HTML/JS) plutôt que comme du texte.
4. **Sous-types.** Reflected (86), Stored (87), DOM-based (88), Blind (89), Mutation/mXSS (90), Self-XSS, via fichiers/SVG/markdown (91) — et selon le *contexte* d'injection (HTML, attribut, JS, URL).
5. **Exemple conceptuel.** Un champ de recherche réaffiche le terme saisi sans encodage : un contenu actif soumis par un attaquant s'exécute dans le navigateur de la victime.
6. **Impacts.** Vol de session/cookies, actions au nom de la victime, keylogging, défiguration, hameçonnage dans la page, pivot vers le compte.
7. **Détection.** Présence de balises/contenu actif dans des champs de données, alertes WAF, anomalies dans les paramètres réfléchis, rapports CSP (violations).
8. **Prévention.** *Encodage de sortie contextuel* (la défense centrale), validation d'entrée, **CSP** (Content Security Policy), cookies `HttpOnly`, frameworks à échappement automatique, attention aux « sinks » dangereux côté JS.
9. ⚠️ **Erreur fréquente.** Filtrer « <script> » par blocklist : d'innombrables contextes et encodages contournent ce filtre. La bonne approche est l'encodage *selon le contexte de sortie*.
10. 🎯 **À retenir.** XSS = le serveur laisse une donnée devenir du code dans le navigateur. La parade reine est l'encodage contextuel des sorties, renforcé par CSP et HttpOnly.

## Chapitre 86 — Reflected XSS

1. **Définition.** XSS où le contenu injecté est *renvoyé immédiatement* dans la réponse à une requête (non stocké).
2. **Famille.** XSS (chapitre 85) / injection côté client.
3. **Principe.** Un paramètre de la requête (URL, formulaire) est réfléchi dans la page sans encodage. L'attaque exige que la victime suive un lien piégé.
4. **Sous-types.** Selon le contexte de réflexion (corps HTML, attribut, script, URL) ; via GET (lien) ou POST (formulaire piégé).
5. **Exemple conceptuel.** Une page d'erreur affiche « page introuvable : <valeur du paramètre> » sans encodage ; un lien spécialement formé fait exécuter du contenu actif chez qui le clique.
6. **Impacts.** Vol de session, actions au nom de la victime — limités à ceux qui suivent le lien.
7. **Détection.** Paramètres réfléchis sans encodage, clics sur des liens anormaux, alertes WAF/CSP.
8. **Prévention.** Encodage contextuel de toute donnée réfléchie, CSP, validation, méfiance envers les paramètres affichés.
9. ⚠️ **Erreur fréquente.** Considérer le reflected XSS « peu grave » car non persistant : couplé à du phishing, il suffit à compromettre des comptes ciblés.
10. 🎯 **À retenir.** Reflected = injection renvoyée à la volée, déclenchée par un lien piégé. Encoder la sortie réfléchie ferme la faille.

## Chapitre 87 — Stored XSS

1. **Définition.** XSS où le contenu injecté est *stocké* par l'application (base, fichier) puis *réaffiché* à d'autres utilisateurs.
2. **Famille.** XSS (chapitre 85).
3. **Principe.** L'attaquant dépose une fois le contenu actif (commentaire, profil, message) ; il s'exécute ensuite chez *tous* ceux qui consultent la page. Pas besoin de lien piégé : c'est persistant et « auto-propagé ».
4. **Sous-types.** Dans commentaires/messages, profils, noms de fichiers, métadonnées, champs admin (impact aggravé si vu par un administrateur).
5. **Exemple conceptuel.** Un champ « biographie » de profil accepte du contenu actif ; chaque visiteur du profil l'exécute dans son navigateur.
6. **Impacts.** Les plus graves des XSS : compromission de nombreux utilisateurs, propagation type « ver », prise de comptes admin si affiché dans une console.
7. **Détection.** Contenu actif persistant dans les données, pics d'événements XSS multi-utilisateurs, violations CSP en série.
8. **Prévention.** Encodage à l'affichage (sortie), validation/assainissement à l'entrée, CSP, assainisseur HTML pour le contenu riche, revue des champs affichés en zone privilégiée.
9. ⚠️ **Erreur fréquente.** Assainir uniquement à l'entrée et oublier l'encodage à la sortie (ou l'inverse) : les deux se complètent.
10. 🎯 **À retenir.** Stored XSS = injection persistante qui frappe tous les lecteurs. C'est la variante la plus dangereuse ; encodage de sortie + assainissement + CSP.

## Chapitre 88 — DOM-based XSS

1. **Définition.** XSS qui se produit *entièrement côté client*, lorsque du JavaScript de la page manipule des données contrôlables sans précaution.
2. **Famille.** XSS (chapitre 85), variante côté navigateur (le serveur peut ne jamais voir la charge).
3. **Principe.** Une « source » contrôlable (fragment d'URL, `location`, message) est passée à un « sink » dangereux (qui écrit du HTML/exécute du code) par le script de la page, sans encodage.
4. **Sous-types.** Selon source (hash d'URL, paramètres, `postMessage`, stockage) et sink (insertion HTML, évaluation dynamique, manipulation du DOM).
5. **Exemple conceptuel.** Un script lit la portion d'URL après `#` et l'insère telle quelle dans la page ; une valeur conçue par l'attaquant devient active sans aller au serveur.
6. **Impacts.** Identiques aux autres XSS ; particulièrement furtif (invisible côté serveur, donc des défenses serveur seules échouent).
7. **Détection.** Analyse du JS côté client (sources→sinks), tests DAST orientés DOM, rapports CSP, revue de code front.
8. **Prévention.** Éviter les sinks dangereux, API sûres de manipulation du DOM, encodage côté client, frameworks à liaison sûre, **Trusted Types**, CSP.
9. ⚠️ **Erreur fréquente.** Compter sur un WAF serveur : le DOM-XSS peut ne jamais transiter par le serveur (par ex. via le fragment d'URL).
10. 🎯 **À retenir.** DOM-XSS vit dans le navigateur : la défense est *côté client* (sinks sûrs, Trusted Types), pas seulement côté serveur.

## Chapitre 89 — Blind XSS

1. **Définition.** XSS stocké dont l'exécution survient dans un contexte *non visible* de l'attaquant (par ex. une interface d'administration interne).
2. **Famille.** Variante de Stored XSS (chapitre 87).
3. **Principe.** La charge est déposée dans un champ qui sera consulté plus tard par un tiers (support, admin) dans un panneau interne ; l'attaquant ne voit pas le rendu mais reçoit un signal lorsqu'elle s'exécute.
4. **Sous-types.** Via formulaires de contact, logs affichés en console admin, tickets de support, champs exportés vers des outils internes.
5. **Exemple conceptuel.** Un message envoyé au support s'affiche dans une console interne ; il s'y exécute quand un agent l'ouvre.
6. **Impacts.** Compromission de comptes *privilégiés* (admins/support), souvent à fort impact, malgré l'absence de retour visible immédiat.
7. **Détection.** Surveillance des consoles internes, CSP sur les back-offices, journalisation des rendus de champs utilisateur en zone admin.
8. **Prévention.** Traiter les données utilisateur *partout* où elles sont affichées (y compris back-offices internes), encodage de sortie, CSP sur les interfaces d'administration.
9. ⚠️ **Erreur fréquente.** Sécuriser le front public mais négliger les interfaces internes, considérées « de confiance ».
10. 🎯 **À retenir.** Le blind XSS frappe là où on ne regarde pas : les back-offices internes doivent être protégés comme le front public.

## Chapitre 90 — Mutation XSS (mXSS)

1. **Définition.** XSS où un contenu *réputé assaini* est ré-interprété (« muté ») par le navigateur lors de la normalisation du HTML, redevenant actif.
2. **Famille.** XSS (chapitre 85), catégorie avancée liée au parsing (chapitre 75).
3. **Principe.** L'assainisseur et le moteur de rendu du navigateur n'interprètent pas le HTML de la même façon ; après ré-écriture par le navigateur (innerHTML, normalisation), une chaîne inerte peut redevenir exécutable.
4. **Sous-types.** Via incohérences de parsing HTML/SVG/MathML, via re-sérialisation, via namespaces.
5. **Exemple conceptuel.** Un contenu validé par un assainisseur est ensuite ré-inséré et normalisé par le navigateur, produisant une structure active non anticipée.
6. **Impacts.** Contournement d'assainisseurs HTML, donc XSS malgré une protection apparente.
7. **Détection.** Tests avec des assainisseurs et navigateurs à jour, fuzzing de l'assainisseur, surveillance CSP.
8. **Prévention.** Assainisseurs HTML maintenus et éprouvés, éviter le re-traitement du HTML déjà assaini, Trusted Types, CSP, limiter le HTML riche.
9. ⚠️ **Erreur fréquente.** Faire confiance à un assainisseur maison ou obsolète : le mXSS exploite précisément ces écarts.
10. 🎯 **À retenir.** Le mXSS exploite le désaccord entre assainisseur et navigateur. Utiliser un assainisseur reconnu et à jour, et ne pas re-manipuler le HTML assaini.

## Chapitre 91 — XSS via fichiers, SVG, markdown ou éditeurs riches

1. **Définition.** XSS introduit par des *formats riches* : fichiers SVG/HTML uploadés, markdown converti en HTML, éditeurs WYSIWYG.
2. **Famille.** XSS (chapitre 85), à la frontière de l'upload (chapitre 112).
3. **Principe.** Ces formats peuvent contenir du contenu actif (un SVG est du XML pouvant porter du script ; le markdown peut produire du HTML ; un éditeur riche stocke du HTML). Servis ou rendus sans assainissement, ils exécutent du code.
4. **Sous-types.** SVG actif, upload HTML servi en ligne, markdown→HTML non assaini, contenu d'éditeur riche, métadonnées de fichiers affichées.
5. **Exemple conceptuel.** Un avatar au format SVG, contenant du contenu actif, s'exécute lorsqu'il est affiché en ligne dans le navigateur d'un visiteur.
6. **Impacts.** XSS stocké, souvent à large portée (avatars, documents partagés).
7. **Détection.** Inspection des fichiers riches uploadés, analyse du HTML généré par markdown/éditeurs, CSP, type MIME servi.
8. **Prévention.** Assainir le HTML issu du markdown/éditeurs, servir les fichiers uploadés depuis un domaine isolé avec `Content-Disposition` adapté et bon type MIME, désactiver le rendu en ligne du SVG non fiable, CSP.
9. ⚠️ **Erreur fréquente.** Traiter une image SVG comme une image inerte : c'est du code potentiellement actif.
10. 🎯 **À retenir.** Les formats riches (SVG, markdown, éditeurs) sont des vecteurs XSS : assainir le rendu et isoler le service des fichiers uploadés.

## Chapitre 92 — Injection SQL — vue d'ensemble

1. **Définition.** Injection où une entrée non fiable modifie une *requête SQL*, permettant de lire/écrire la base ou de contourner la logique.
2. **Famille.** Injection (chapitre 64). CWE-89.
3. **Principe.** L'application construit la requête en *concaténant* des données utilisateur ; l'attaquant injecte de la syntaxe SQL qui change le sens de la requête.
4. **Sous-types.** Union-based (93), error-based (94), boolean-blind (95), time-blind (96), out-of-band (97), second-order (98), plus NoSQL (99) et variantes (ORM injection).
5. **Exemple conceptuel.** Un champ de connexion concatène l'entrée dans la clause de filtrage ; une entrée structurée altère la condition et contourne le contrôle.
6. **Impacts.** Vol/altération massive de données, contournement d'authentification, parfois exécution de commandes ou compromission du serveur de base.
7. **Détection.** Erreurs SQL renvoyées, motifs d'injection dans les paramètres, requêtes anormales/lentes, alertes WAF, pics d'erreurs base.
8. **Prévention.** **Requêtes paramétrées/préparées** (défense reine), ORM utilisés correctement, validation par allowlist, moindre privilège du compte base, désactivation des messages d'erreur détaillés.
9. ⚠️ **Erreur fréquente.** « Échapper » manuellement les caractères au lieu de paramétrer : fragile et contournable. Le paramétrage sépare structurellement code et données.
10. 🎯 **À retenir.** SQLi = données traitées comme du SQL. Les requêtes paramétrées éliminent la racine du problème ; le moindre privilège limite l'impact résiduel.

## Chapitre 93 — Union-based SQL injection

1. **Définition.** SQLi exploitant l'opérateur d'union pour *ajouter* des résultats issus d'autres tables à la réponse légitime.
2. **Famille.** SQLi (chapitre 92), variante « in-band » (résultats directement visibles).
3. **Principe.** Quand la réponse affiche le résultat d'une requête, l'attaquant fusionne un second jeu de données (d'autres tables/colonnes) au résultat affiché.
4. **Sous-types.** Selon le nombre/type de colonnes à aligner, selon les données ciblées (identifiants, autres tables).
5. **Exemple conceptuel.** Une page listant des produits laisse l'attaquant adjoindre, à la liste affichée, des données provenant d'une autre table.
6. **Impacts.** Extraction directe et rapide de données arbitraires de la base.
7. **Détection.** Mots-clés d'union dans les paramètres, réponses contenant des données inattendues, erreurs de nombre de colonnes.
8. **Prévention.** Identiques à la SQLi (paramétrage, allowlist, moindre privilège) ; ne jamais refléter des résultats de requêtes construites par concaténation.
9. ⚠️ **Erreur fréquente.** Croire qu'afficher « peu de colonnes » protège : l'attaquant aligne ce qu'il faut.
10. 🎯 **À retenir.** L'union-based est la SQLi la plus directe quand les résultats sont affichés. Paramétrer la requête supprime le vecteur.

## Chapitre 94 — Error-based SQL injection

1. **Définition.** SQLi où les *messages d'erreur* de la base révèlent des données ou la structure.
2. **Famille.** SQLi in-band (chapitre 92).
3. **Principe.** L'attaquant provoque des erreurs dont le contenu (renvoyé à l'utilisateur) divulgue des informations (noms de tables, valeurs).
4. **Sous-types.** Selon le SGBD et les fonctions d'erreur exploitées.
5. **Exemple conceptuel.** Une requête mal formée renvoie un message technique détaillé contenant un fragment de donnée de la base.
6. **Impacts.** Extraction de données et cartographie de la base, reconnaissance facilitée.
7. **Détection.** Messages d'erreur SQL exposés, pics d'erreurs base, motifs d'injection.
8. **Prévention.** Paramétrage, **messages d'erreur génériques** en production (pas de détail technique), journalisation côté serveur uniquement, moindre privilège.
9. ⚠️ **Erreur fréquente.** Laisser les traces d'erreur détaillées en production : c'est à la fois une fuite d'information (chapitre 69) et un facilitateur de SQLi.
10. 🎯 **À retenir.** Les erreurs verbeuses transforment une SQLi en extraction facile. Génériciser les erreurs et paramétrer.

## Chapitre 95 — Boolean-based blind SQL injection

1. **Définition.** SQLi « à l'aveugle » où l'attaquant déduit l'information à partir de réponses *différentes selon une condition vraie/fausse*, sans voir les données.
2. **Famille.** SQLi inférentielle/blind (chapitre 92).
3. **Principe.** L'application ne renvoie pas les données ni les erreurs, mais son comportement (page différente, présence/absence d'un élément) change selon que la condition injectée est vraie ou fausse — permettant une extraction bit à bit.
4. **Sous-types.** Selon le signal observable (contenu, code de statut, longueur).
5. **Exemple conceptuel.** Selon qu'une condition injectée est vraie ou fausse, la page affiche « trouvé » ou « non trouvé » ; l'attaquant reconstitue l'information question après question.
6. **Impacts.** Extraction de données (plus lente mais fiable), même sans affichage direct.
7. **Détection.** Volume anormal de requêtes quasi identiques variant un paramètre, motifs d'inférence, sans limitation de débit.
8. **Prévention.** Paramétrage, réponses uniformes, **limitation de débit** (chapitre 79), détection d'anomalies, moindre privilège.
9. ⚠️ **Erreur fréquente.** Croire qu'« aucune donnée affichée » protège : l'inférence suffit à tout extraire.
10. 🎯 **À retenir.** L'absence d'affichage ne protège pas : le comportement de l'app suffit à fuiter. Paramétrer et limiter le débit.

## Chapitre 96 — Time-based blind SQL injection

1. **Définition.** SQLi à l'aveugle où l'information se déduit du *temps de réponse* (réponse retardée si la condition est vraie).
2. **Famille.** SQLi inférentielle/blind (chapitre 92).
3. **Principe.** Quand ni les données ni le comportement ne diffèrent, l'attaquant injecte une condition qui *retarde* la réponse selon vrai/faux, et mesure le délai.
4. **Sous-types.** Selon les fonctions de temporisation du SGBD.
5. **Exemple conceptuel.** Une réponse qui arrive « lentement » quand une condition est vraie, et « vite » sinon, révèle l'information par chronométrage.
6. **Impacts.** Extraction de données, plus lente encore, mais possible sans aucun retour visible.
7. **Détection.** Requêtes provoquant des délais anormaux et répétitifs, charge inhabituelle, absence de limitation.
8. **Prévention.** Paramétrage, limitation de débit, time-outs de requêtes, détection d'anomalies, moindre privilège.
9. ⚠️ **Erreur fréquente.** Ignorer les requêtes « lentes » répétées : ce sont des signaux d'inférence temporelle.
10. 🎯 **À retenir.** Même le *temps de réponse* fuit de l'information. Paramétrer, limiter le débit et surveiller les délais anormaux.

## Chapitre 97 — Out-of-band SQL injection

1. **Définition.** SQLi où les données sont exfiltrées par un *canal différent* (souvent une requête réseau sortante, ex. DNS/HTTP) plutôt que dans la réponse.
2. **Famille.** SQLi (chapitre 92), variante hors-bande.
3. **Principe.** Quand l'inférence est trop lente ou impossible, l'attaquant fait *émettre* à la base une requête réseau contenant la donnée, vers un serveur qu'il contrôle.
4. **Sous-types.** Via résolution DNS, via requêtes HTTP sortantes, selon les capacités du SGBD.
5. **Exemple conceptuel.** La base est amenée à effectuer une résolution de nom incluant une donnée, captée par l'attaquant côté serveur DNS.
6. **Impacts.** Exfiltration efficace, même sans retour applicatif.
7. **Détection.** Flux réseau sortants inattendus depuis le serveur de base (DNS/HTTP), corrélation avec des paramètres suspects.
8. **Prévention.** Paramétrage, **filtrage sortant** (la base ne doit pas initier de trafic Internet), durcissement du SGBD, moindre privilège, segmentation.
9. ⚠️ **Erreur fréquente.** Autoriser les serveurs de base à émettre du trafic sortant arbitraire.
10. 🎯 **À retenir.** Couper le trafic sortant des serveurs de base neutralise l'exfiltration hors-bande. Paramétrer reste la base.

## Chapitre 98 — Second-order SQL injection

1. **Définition.** SQLi où la donnée malveillante est *stockée* d'abord, puis exécutée *plus tard* lorsqu'elle est réutilisée dans une requête.
2. **Famille.** SQLi (chapitre 92), différée.
3. **Principe.** L'entrée passe les contrôles à la saisie (elle est juste stockée), mais une fonctionnalité ultérieure la réinjecte dans une requête sans paramétrage — l'injection se déclenche en différé.
4. **Sous-types.** Via champs de profil réutilisés, via traitements par lots, via fonctions d'export/reporting.
5. **Exemple conceptuel.** Une valeur enregistrée dans un profil est ensuite intégrée telle quelle à une requête lors d'un traitement administratif ultérieur.
6. **Impacts.** Identiques à la SQLi, mais plus furtifs (découplage saisie/exécution).
7. **Détection.** Difficile : nécessite de tracer le flux des données stockées vers les requêtes ; revue de code, tests ciblés.
8. **Prévention.** Paramétrer *toutes* les requêtes, y compris celles utilisant des données « déjà en base » ; ne jamais considérer une donnée stockée comme fiable (frontière de confiance — chapitre 80).
9. ⚠️ **Erreur fréquente.** Assainir à l'entrée puis traiter la donnée stockée comme sûre lors d'une réutilisation ultérieure.
10. 🎯 **À retenir.** Une donnée stockée n'est pas une donnée sûre : paramétrer partout, même en réutilisant des valeurs internes.

## Chapitre 99 — NoSQL injection

1. **Définition.** Injection ciblant les bases *NoSQL* (documents, clés-valeurs), manipulant la structure des requêtes/opérateurs.
2. **Famille.** Injection (chapitre 64), variante NoSQL. CWE-943.
3. **Principe.** Les requêtes NoSQL sont souvent des structures (objets/JSON) ; injecter des opérateurs ou altérer la structure modifie la logique (par ex. transformer une égalité en condition toujours vraie).
4. **Sous-types.** Injection d'opérateurs, injection par type (passer un objet là où une chaîne est attendue), injection dans des fonctions d'évaluation côté base.
5. **Exemple conceptuel.** Un filtre d'authentification attend une valeur simple ; recevoir une structure d'opérateur le rend toujours satisfait, contournant la vérification.
6. **Impacts.** Contournement d'authentification, accès/altération de données, parfois exécution côté base.
7. **Détection.** Types inattendus dans les paramètres (objets au lieu de chaînes), opérateurs dans les entrées, requêtes anormales.
8. **Prévention.** Validation stricte de type et de schéma, requêtes paramétrées propres au moteur, refus des structures non attendues, moindre privilège, éviter l'évaluation dynamique côté base.
9. ⚠️ **Erreur fréquente.** Croire que « NoSQL = pas d'injection ». Le principe d'injection demeure, sous une autre forme.
10. 🎯 **À retenir.** NoSQL n'immunise pas contre l'injection : valider type et schéma, et n'accepter que des structures attendues.

## Chapitre 100 — Command injection

1. **Définition.** Injection où une entrée non fiable est insérée dans une *commande système* exécutée par le serveur.
2. **Famille.** Injection (chapitre 64). CWE-78.
3. **Principe.** L'application appelle le système d'exploitation en concaténant des données utilisateur ; l'attaquant ajoute des commandes exécutées avec les droits du processus.
4. **Sous-types.** Injection directe, injection « aveugle » (sans retour), injection d'arguments (argument injection).
5. **Exemple conceptuel.** Une fonctionnalité « ping » qui passe une adresse fournie à une commande système permet, si concaténée sans contrôle, d'enchaîner une autre commande.
6. **Impacts.** Exécution de code sur le serveur (RCE), compromission complète, pivot vers le réseau.
7. **Détection.** Caractères de chaînage/échappement dans les paramètres, processus enfants inattendus, alertes EDR sur le serveur, trafic sortant anormal.
8. **Prévention.** Éviter d'appeler le shell ; utiliser des **API directes** sans interpréteur ; si nécessaire, passer des arguments via des API sûres (pas de concaténation), allowlist stricte, moindre privilège du processus.
9. ⚠️ **Erreur fréquente.** « Échapper » la chaîne de commande : approche fragile. Le mieux est de *ne pas* passer par un shell.
10. 🎯 **À retenir.** La command injection donne souvent un RCE direct : éviter le shell et n'utiliser que des API paramétrées avec moindre privilège.

## Chapitre 101 — LDAP injection

1. **Définition.** Injection ciblant les requêtes *LDAP* (annuaires), altérant les filtres de recherche/authentification.
2. **Famille.** Injection (chapitre 64). CWE-90.
3. **Principe.** Construction de filtres LDAP par concaténation ; l'attaquant injecte de la syntaxe de filtre pour modifier la logique (contourner une authentification, élargir une recherche).
4. **Sous-types.** Injection dans le filtre de recherche, injection dans le DN, contournement d'authentification.
5. **Exemple conceptuel.** Un filtre d'authentification construit avec l'entrée utilisateur peut être transformé en condition trop permissive.
6. **Impacts.** Contournement d'authentification, divulgation d'entrées d'annuaire, élévation.
7. **Détection.** Caractères spéciaux LDAP dans les entrées, recherches anormalement larges, motifs d'injection.
8. **Prévention.** Échappement LDAP via API dédiées, validation par allowlist, requêtes paramétrées, moindre privilège du compte de liaison.
9. ⚠️ **Erreur fréquente.** Réutiliser des entrées utilisateur directement dans des filtres LDAP de connexion.
10. 🎯 **À retenir.** L'annuaire LDAP est, lui aussi, un interpréteur : échapper via API dédiée et valider en allowlist.

## Chapitre 102 — XPath injection

1. **Définition.** Injection ciblant les requêtes *XPath* sur des documents XML.
2. **Famille.** Injection (chapitre 64). CWE-643.
3. **Principe.** Construction de requêtes XPath par concaténation ; l'attaquant modifie l'expression pour accéder à des nœuds non prévus ou contourner une condition.
4. **Sous-types.** XPath injection classique, « blind » (inférentielle, comme la SQLi aveugle).
5. **Exemple conceptuel.** Une authentification stockée en XML, interrogée par XPath construit avec l'entrée, peut voir sa condition contournée.
6. **Impacts.** Contournement d'authentification, lecture de données XML non autorisées.
7. **Détection.** Caractères de syntaxe XPath dans les entrées, accès anormaux, motifs d'injection.
8. **Prévention.** Requêtes XPath paramétrées, échappement via API, validation, éviter de stocker des données sensibles d'authentification en XML interrogé dynamiquement.
9. ⚠️ **Erreur fréquente.** Considérer le XML comme « inerte » : interrogé par XPath concaténé, il est injectable.
10. 🎯 **À retenir.** XPath est un interpréteur de plus : paramétrer et valider, comme pour toute injection.

## Chapitre 103 — SSTI (Server-Side Template Injection)

1. **Définition.** Injection dans un *moteur de templates* côté serveur, où l'entrée est évaluée comme expression de template.
2. **Famille.** Injection (chapitre 64). CWE-1336.
3. **Principe.** Quand une entrée utilisateur est insérée dans un template *interprété* (au lieu d'être passée en donnée), l'attaquant peut exécuter des expressions du moteur, menant souvent à l'exécution de code serveur.
4. **Sous-types.** Selon le moteur de template ; du simple accès d'objets à l'exécution de code (RCE) selon les capacités exposées.
5. **Exemple conceptuel.** Un message d'e-mail personnalisé qui insère directement une entrée dans le template fait évaluer une expression au lieu de l'afficher comme texte.
6. **Impacts.** De la fuite d'information jusqu'au RCE, selon le moteur et le bac à sable.
7. **Détection.** Expressions de template dans les entrées, comportements d'évaluation inattendus, alertes serveur/EDR.
8. **Prévention.** Ne jamais insérer d'entrée utilisateur *dans la structure* d'un template ; passer les données en *contexte* (variables), pas en template ; bacs à sable, moteurs logic-less, validation.
9. ⚠️ **Erreur fréquente.** Construire dynamiquement des templates à partir d'entrées « pour la personnalisation ».
10. 🎯 **À retenir.** Le SSTI mène souvent au RCE : les données doivent *alimenter* un template, jamais *le constituer*.

## Chapitre 104 — XXE (XML External Entity)

1. **Définition.** Attaque exploitant le traitement des *entités externes* XML par un analyseur mal configuré.
2. **Famille.** Erreurs de parsing (chapitre 75) / injection. CWE-611.
3. **Principe.** Un parser XML qui résout les entités externes peut être amené à lire des fichiers locaux, effectuer des requêtes réseau (SSRF), ou subir un déni de service (expansion d'entités).
4. **Sous-types.** XXE en lecture de fichier, XXE-vers-SSRF, XXE aveugle (out-of-band), « billion laughs » (DoS par expansion).
5. **Exemple conceptuel.** Un import de document XML déclenche, via une entité externe, la lecture d'un fichier du serveur renvoyé dans la réponse.
6. **Impacts.** Lecture de fichiers sensibles, SSRF, déni de service, exfiltration hors-bande.
7. **Détection.** Déclarations d'entités/DOCTYPE dans les entrées XML, accès fichiers/réseau anormaux depuis le parser.
8. **Prévention.** **Désactiver les entités externes et le DOCTYPE** dans les parsers XML, utiliser des configurations sûres par défaut, préférer des formats plus simples, limiter tailles/profondeur.
9. ⚠️ **Erreur fréquente.** Utiliser un parser XML aux réglages par défaut historiquement permissifs.
10. 🎯 **À retenir.** XXE = parser XML trop permissif. Désactiver entités externes et DOCTYPE règle l'essentiel.

## Chapitre 105 — SSRF (Server-Side Request Forgery)

1. **Définition.** Attaque où le serveur est *manipulé pour émettre des requêtes* vers des destinations choisies par l'attaquant.
2. **Famille.** Falsification de requêtes côté serveur (OWASP Top 10). CWE-918.
3. **Principe.** Une fonctionnalité qui récupère une ressource à partir d'une URL fournie peut être détournée pour atteindre des cibles internes (services privés, métadonnées cloud) non accessibles directement.
4. **Sous-types.** SSRF classique (réponse visible), blind (106), vers métadonnées cloud (107), via parser d'URL, via redirection ouverte (pivot), DNS rebinding.
5. **Exemple conceptuel.** Une fonction « prévisualiser une URL » est dirigée vers un service interne normalement inaccessible depuis l'extérieur.
6. **Impacts.** Accès à des services internes, vol de secrets cloud (via métadonnées), cartographie interne, pivot, parfois RCE indirect.
7. **Détection.** Requêtes sortantes du serveur vers des cibles internes/inhabituelles, accès au service de métadonnées, URL suspectes en paramètre.
8. **Prévention.** Allowlist stricte des destinations, interdiction des plages internes et du service de métadonnées, validation/normalisation d'URL, **filtrage sortant**, durcissement du service de métadonnées (cloud).
9. ⚠️ **Erreur fréquente.** Filtrer par blocklist d'IP : contournable (redirections, encodages, rebinding DNS, IPv6). Préférer l'allowlist.
10. 🎯 **À retenir.** SSRF = le serveur devient le proxy de l'attaquant vers l'interne. Allowlist des destinations + blocage des métadonnées + filtrage sortant.

## Chapitre 106 — Blind SSRF

1. **Définition.** SSRF où l'attaquant *ne voit pas* la réponse, mais confirme/agit via des canaux indirects.
2. **Famille.** SSRF (chapitre 105).
3. **Principe.** Même sans retour, le serveur peut être amené à atteindre des cibles internes ; l'attaquant détecte le succès par des signaux hors-bande (résolution DNS, requête reçue) et déclenche des effets.
4. **Sous-types.** Détection via DNS/HTTP hors-bande, exploitation d'effets de bord internes.
5. **Exemple conceptuel.** Une fonction de récupération d'URL, dont la réponse n'est pas affichée, provoque néanmoins une requête observable côté attaquant, prouvant l'accès interne.
6. **Impacts.** Cartographie interne, déclenchement d'actions, vol de secrets via cibles connues, même sans retour direct.
7. **Détection.** Trafic sortant inattendu, résolutions DNS anormales, corrélation avec des paramètres URL.
8. **Prévention.** Identiques à la SSRF : allowlist, blocage interne/métadonnées, filtrage sortant, normalisation d'URL.
9. ⚠️ **Erreur fréquente.** Penser qu'« absence de réponse affichée » signifie « pas exploitable ».
10. 🎯 **À retenir.** Le blind SSRF est exploitable sans retour : les mêmes défenses (allowlist + filtrage sortant) s'appliquent.

## Chapitre 107 — SSRF vers métadonnées cloud

1. **Définition.** SSRF visant le *service de métadonnées* des environnements cloud, qui peut exposer des identifiants temporaires.
2. **Famille.** SSRF (chapitre 105), cas cloud à fort impact.
3. **Principe.** Les instances cloud disposent d'un point interne fournissant configuration et *crédentiels temporaires* ; un SSRF qui l'atteint peut récupérer ces secrets et usurper le rôle de l'instance.
4. **Sous-types.** Selon le fournisseur et la version du service de métadonnées (les versions renforcées exigent une étape supplémentaire).
5. **Exemple conceptuel.** Une fonctionnalité serveur récupérant une URL est dirigée vers l'adresse interne de métadonnées, exposant des identifiants de rôle.
6. **Impacts.** Vol d'identifiants cloud, élévation et mouvement latéral dans le cloud, accès aux ressources (stockage, bases).
7. **Détection.** Accès au point de métadonnées depuis un composant qui ne devrait pas, usage anormal d'identifiants de rôle.
8. **Prévention.** Versions renforcées du service de métadonnées, blocage explicite de cette adresse depuis les applications, moindre privilège des rôles d'instance, allowlist SSRF.
9. ⚠️ **Erreur fréquente.** Laisser le service de métadonnées en version permissive et les rôles d'instance surprivilégiés.
10. 🎯 **À retenir.** Le SSRF vers métadonnées transforme une faille web en vol d'identifiants cloud : durcir le service de métadonnées et appliquer le moindre privilège aux rôles.

## Chapitre 108 — File inclusion (vue d'ensemble)

1. **Définition.** Attaques amenant l'application à *inclure/charger un fichier* contrôlé par l'attaquant.
2. **Famille.** Accès aux fichiers / injection de chemin. CWE-98, CWE-22.
3. **Principe.** Une application qui choisit dynamiquement un fichier à inclure à partir d'une entrée peut être détournée pour charger un fichier local sensible (LFI) ou distant (RFI).
4. **Sous-types.** LFI (109), RFI (110), path traversal (111) comme mécanisme sous-jacent.
5. **Exemple conceptuel.** Un paramètre « page » utilisé pour inclure un fichier permet, mal contrôlé, de désigner un autre fichier que ceux prévus.
6. **Impacts.** Lecture de fichiers sensibles, parfois exécution de code (selon le type de fichier inclus), divulgation de configuration/secrets.
7. **Détection.** Séquences de traversée et chemins inhabituels en paramètre, accès fichiers anormaux.
8. **Prévention.** Ne pas construire de chemins/inclusions à partir d'entrées ; allowlist d'identifiants mappés à des fichiers fixes ; désactiver l'inclusion distante ; moindre privilège.
9. ⚠️ **Erreur fréquente.** Filtrer naïvement les « ../ » : de multiples encodages contournent. Préférer l'allowlist mappée.
10. 🎯 **À retenir.** Ne jamais dériver un chemin de fichier d'une entrée libre : mapper des identifiants vers des fichiers prédéfinis.

## Chapitre 109 — LFI (Local File Inclusion)

1. **Définition.** Inclusion d'un *fichier local* du serveur choisi par l'attaquant.
2. **Famille.** File inclusion (chapitre 108).
3. **Principe.** L'application inclut un fichier dont le chemin dépend d'une entrée ; l'attaquant désigne des fichiers sensibles locaux (configuration, logs).
4. **Sous-types.** Lecture de fichiers sensibles ; dans certains contextes, chaînage vers exécution (par ex. via fichiers contrôlés ailleurs).
5. **Exemple conceptuel.** Un paramètre de langue utilisé pour inclure un fichier de traduction est détourné pour pointer vers un fichier de configuration.
6. **Impacts.** Divulgation de configuration/secrets, reconnaissance, parfois exécution indirecte.
7. **Détection.** Chemins de traversée, accès à des fichiers hors du répertoire prévu.
8. **Prévention.** Allowlist mappée, base path verrouillée, désactivation des wrappers dangereux, moindre privilège, normalisation des chemins.
9. ⚠️ **Erreur fréquente.** Concaténer une entrée à un chemin de base sans normalisation ni allowlist.
10. 🎯 **À retenir.** LFI = inclure un fichier local non prévu. Allowlist mappée et base path verrouillée.

## Chapitre 110 — RFI (Remote File Inclusion)

1. **Définition.** Inclusion d'un fichier *distant* (hébergé par l'attaquant), souvent menant à l'exécution de code.
2. **Famille.** File inclusion (chapitre 108).
3. **Principe.** Une configuration permettant l'inclusion d'une ressource distante laisse l'attaquant faire charger et exécuter un fichier qu'il contrôle.
4. **Sous-types.** Selon la techno et la configuration autorisant l'inclusion distante.
5. **Exemple conceptuel.** Un paramètre d'inclusion accepte une URL externe, faisant charger un contenu distant par le serveur.
6. **Impacts.** Exécution de code à distance (souvent), compromission du serveur.
7. **Détection.** URL externes en paramètre d'inclusion, trafic sortant inattendu, exécution anormale.
8. **Prévention.** **Désactiver l'inclusion distante**, allowlist locale stricte, moindre privilège, filtrage sortant.
9. ⚠️ **Erreur fréquente.** Laisser activées des options d'inclusion d'URL distantes.
10. 🎯 **À retenir.** RFI mène souvent au RCE : désactiver toute inclusion distante.

## Chapitre 111 — Path traversal / Directory traversal

1. **Définition.** Accès à des fichiers/répertoires *hors du dossier prévu* en manipulant le chemin.
2. **Famille.** Accès aux fichiers (CWE-22). Mécanisme sous-jacent du LFI et de nombreux abus de fichiers.
3. **Principe.** En insérant des séquences de remontée de répertoire (et leurs encodages), l'attaquant « sort » du dossier autorisé pour atteindre d'autres fichiers.
4. **Sous-types.** Traversée en lecture, en écriture, via encodages multiples, via chemins absolus.
5. **Exemple conceptuel.** Un paramètre de nom de fichier de téléchargement, mal contrôlé, désigne un fichier situé en dehors du répertoire public.
6. **Impacts.** Lecture/écriture arbitraire de fichiers, divulgation de secrets, parfois exécution.
7. **Détection.** Séquences de traversée et encodages suspects, accès hors périmètre.
8. **Prévention.** Normalisation puis vérification que le chemin résolu reste dans le répertoire autorisé, allowlist de noms, refus des chemins absolus/relatifs, moindre privilège.
9. ⚠️ **Erreur fréquente.** Filtrer « ../ » en surface sans normaliser : les variantes encodées passent.
10. 🎯 **À retenir.** Toujours *normaliser puis vérifier l'appartenance* du chemin résolu au dossier autorisé.

## Chapitre 112 — Unrestricted file upload

1. **Définition.** Upload de fichiers insuffisamment contrôlé, permettant de déposer un fichier dangereux (ex. webshell) ou abusif.
2. **Famille.** Accès aux fichiers / exécution. CWE-434.
3. **Principe.** L'application accepte un fichier sans vérifier type réel, contenu et emplacement de stockage/service ; un fichier exécutable ou actif peut alors être déposé puis déclenché.
4. **Sous-types.** Upload de webshell, contournement d'extension/type MIME (MIME confusion), upload de SVG/HTML actif (XSS — chapitre 91), écrasement de fichiers, archive abusive (Zip Slip — chapitre 113).
5. **Exemple conceptuel.** Un formulaire d'avatar acceptant tout fichier, servi ensuite depuis le domaine principal, permet de déposer un fichier actif déclenché par sa simple consultation.
6. **Impacts.** Exécution de code serveur (webshell), XSS stocké, déni de service (gros fichiers), écrasement de fichiers critiques.
7. **Détection.** Types/extensions inattendus, fichiers actifs uploadés, accès ultérieurs à ces fichiers, alertes EDR.
8. **Prévention.** Validation du *type réel* (pas seulement l'extension), renommage, stockage **hors webroot** ou sur domaine isolé sans exécution, `Content-Disposition`, taille limitée, analyse antivirus, moindre privilège.
9. ⚠️ **Erreur fréquente.** Se fier à l'extension ou au type MIME déclaré par le client (tous deux falsifiables).
10. 🎯 **À retenir.** Un upload mal maîtrisé peut donner un RCE. Valider le contenu réel, stocker hors zone exécutable, servir depuis un domaine isolé.

## Chapitre 113 — Zip Slip (archive extraction abuse)

1. **Définition.** Attaque où l'*extraction d'une archive* écrit des fichiers hors du répertoire cible via des chemins malveillants dans l'archive.
2. **Famille.** Path traversal (chapitre 111) appliqué aux archives. 
3. **Principe.** Les entrées d'une archive peuvent contenir des chemins de traversée ; une extraction qui ne valide pas les destinations écrit des fichiers ailleurs (écrasement de fichiers système/config).
4. **Sous-types.** Selon le format d'archive et le lien symbolique éventuel.
5. **Exemple conceptuel.** Une archive importée contient une entrée dont le chemin remonte hors du dossier d'extraction prévu, visant à écraser un fichier sensible.
6. **Impacts.** Écrasement de fichiers critiques, parfois exécution de code, compromission.
7. **Détection.** Chemins de traversée dans les entrées d'archive, écritures hors du dossier d'extraction.
8. **Prévention.** Valider chaque destination (chemin résolu dans le dossier cible), refuser les chemins absolus/traversants, ignorer les liens symboliques, bibliothèques d'extraction sûres, moindre privilège.
9. ⚠️ **Erreur fréquente.** Extraire une archive en faisant confiance aux chemins qu'elle contient.
10. 🎯 **À retenir.** Toute extraction d'archive doit valider la destination de chaque entrée, comme un path traversal.

## Chapitre 114 — Insecure deserialization

1. **Définition.** Reconstruction d'objets à partir de données sérialisées non fiables, menant à l'altération du comportement ou à l'exécution de code.
2. **Famille.** Désérialisation (chapitre 74) ; OWASP « Software and Data Integrity Failures ». CWE-502.
3. **Principe.** Désérialiser des données contrôlées par l'attaquant peut instancier des objets et déclencher des « chaînes de gadgets » aboutissant à l'exécution de code, surtout avec des formats binaires riches.
4. **Sous-types.** RCE par chaînes de gadgets, manipulation d'objets/état, déni de service.
5. **Exemple conceptuel.** Un jeton d'état sérialisé, modifié par l'attaquant, est désérialisé côté serveur et altère l'exécution.
6. **Impacts.** RCE (fréquent), élévation, contournement de logique, DoS.
7. **Détection.** Données sérialisées modifiées, comportements d'instanciation anormaux, alertes EDR.
8. **Prévention.** Ne pas désérialiser de données non fiables ; formats de données simples (sans types/objets) ; signer/chiffrer les données sérialisées ; allowlist de classes ; mises à jour.
9. ⚠️ **Erreur fréquente.** Transmettre au client des objets sérialisés « pour l'état » puis les désérialiser en confiance.
10. 🎯 **À retenir.** Désérialiser une entrée non fiable = exécuter potentiellement du code étranger. Éviter, ou signer/typer strictement.

## Chapitre 115 — CSRF (Cross-Site Request Forgery)

1. **Définition.** Attaque forçant le navigateur d'une victime *authentifiée* à émettre une requête non voulue vers une application de confiance.
2. **Famille.** Falsification de requêtes côté client / abus de confiance de session. CWE-352.
3. **Principe.** Le navigateur joint automatiquement les cookies de session ; un site malveillant déclenche une requête vers l'application cible, qui l'exécute en croyant qu'elle vient de l'utilisateur.
4. **Sous-types.** CSRF sur actions sensibles (changement d'e-mail, virement), login CSRF, CSRF sur API selon la gestion des jetons.
5. **Exemple conceptuel.** Une page piégée provoque, à l'insu de la victime connectée, une requête de modification de paramètre sur le site cible.
6. **Impacts.** Actions non autorisées au nom de la victime (modification de compte, transactions), parfois prise de contrôle.
7. **Détection.** Requêtes sensibles sans jeton anti-CSRF valide, référents/origines incohérents, schémas inhabituels.
8. **Prévention.** **Jetons anti-CSRF**, cookies `SameSite`, vérification d'origine, ré-authentification pour les actions sensibles, éviter les actions à effet de bord en GET.
9. ⚠️ **Erreur fréquente.** Croire que HTTPS ou l'authentification protègent du CSRF : ils ne le font pas (la requête « semble » légitime).
10. 🎯 **À retenir.** CSRF abuse de la session de la victime : jetons anti-CSRF + `SameSite` + vérification d'origine sont la parade.

## Chapitre 116 — Clickjacking

1. **Définition.** Tromper l'utilisateur pour qu'il clique sur un élément invisible/déguisé, déclenchant une action non voulue.
2. **Famille.** Abus de l'interface / UI redressing. CWE-1021.
3. **Principe.** L'attaquant superpose (souvent via une iframe) le site cible sous une page leurre transparente, de sorte que les clics de la victime atterrissent sur le site cible.
4. **Sous-types.** Clickjacking classique, likejacking, manipulation de glisser-déposer.
5. **Exemple conceptuel.** Un bouton « jouer » d'une page leurre est superposé à une action sensible du site cible chargé en transparence.
6. **Impacts.** Actions non voulues (validation, achat, changement de réglage), souvent couplées à d'autres attaques.
7. **Détection.** Site cible chargé en iframe par des tiers, absence d'en-têtes anti-cadrage.
8. **Prévention.** En-têtes **anti-cadrage** (`X-Frame-Options`/CSP `frame-ancestors`), confirmation explicite des actions sensibles, frame-busting moderne.
9. ⚠️ **Erreur fréquente.** Ne pas définir de politique de cadrage, laissant le site intégrable par n'importe qui.
10. 🎯 **À retenir.** Empêcher le cadrage du site (`frame-ancestors`) neutralise le clickjacking.

## Chapitre 117 — CORS misconfiguration

1. **Définition.** Mauvaise configuration du *partage de ressources entre origines* (CORS), exposant des données à des sites non autorisés.
2. **Famille.** Abus de confiance entre origines. CWE-942.
3. **Principe.** CORS assouplit la politique de même origine ; une configuration trop permissive (origines reflétées sans contrôle, autorisation des identifiants depuis n'importe quelle origine) laisse un site tiers lire des réponses authentifiées.
4. **Sous-types.** Reflet d'origine non validé, wildcard avec identifiants, confiance excessive en sous-domaines.
5. **Exemple conceptuel.** Une API renvoie une autorisation CORS reflétant toute origine *et* autorisant les identifiants, permettant à un site tiers de lire des données privées.
6. **Impacts.** Vol de données authentifiées par un site tiers, contournement de la politique de même origine.
7. **Détection.** En-têtes CORS reflétant des origines arbitraires, wildcard avec credentials, revue de configuration.
8. **Prévention.** Allowlist stricte d'origines, ne pas combiner wildcard et identifiants, valider l'origine côté serveur, limiter les méthodes/en-têtes exposés.
9. ⚠️ **Erreur fréquente.** Refléter dynamiquement l'origine reçue « pour que ça marche » avec les identifiants activés.
10. 🎯 **À retenir.** CORS doit reposer sur une allowlist d'origines ; jamais wildcard + identifiants.

## Chapitre 118 — Open redirect

1. **Définition.** Une fonctionnalité de redirection accepte une *destination contrôlable*, renvoyant l'utilisateur vers un site arbitraire.
2. **Famille.** Validation d'entrée / abus de confiance. CWE-601.
3. **Principe.** L'application redirige vers une URL fournie sans la restreindre ; un lien sur le domaine de confiance renvoie en réalité ailleurs.
4. **Sous-types.** Redirection directe, via paramètre encodé, pivot pour SSRF/OAuth, support de phishing.
5. **Exemple conceptuel.** Un lien de déconnexion qui redirige vers une URL fournie en paramètre est utilisé pour renvoyer la victime vers un site de phishing, tout en partant d'un domaine de confiance.
6. **Impacts.** Phishing crédibilisé, vol de jetons (flux OAuth), pivot SSRF, atteinte à la réputation du domaine.
7. **Détection.** Redirections vers des domaines externes via paramètre, schémas de phishing partant du domaine.
8. **Prévention.** Allowlist de destinations internes, redirections relatives uniquement, validation stricte, page d'avertissement pour les sorties.
9. ⚠️ **Erreur fréquente.** Considérer l'open redirect « mineur » : il crédibilise le phishing et casse des flux OAuth.
10. 🎯 **À retenir.** N'autoriser que des destinations en allowlist (ou relatives). Un open redirect est un multiplicateur d'autres attaques.

## Chapitre 119 — Host header injection

1. **Définition.** Abus de l'en-tête `Host` (ou apparentés) lorsque l'application lui fait confiance pour construire des URL ou prendre des décisions.
2. **Famille.** Rupture de frontière de confiance (chapitre 80) côté HTTP. CWE-644.
3. **Principe.** L'application réutilise un `Host` contrôlable (par ex. pour générer des liens de réinitialisation) ; l'attaquant le falsifie pour empoisonner ces liens ou contourner des contrôles.
4. **Sous-types.** Empoisonnement de liens (réinitialisation de mot de passe), routage/cache trompé, contournement d'autorisation basée sur l'hôte.
5. **Exemple conceptuel.** Un e-mail de réinitialisation construit son lien à partir du `Host` reçu ; falsifié, le lien pointe vers un domaine attaquant qui capte le jeton.
6. **Impacts.** Vol de jetons de réinitialisation, prise de comptes, empoisonnement de cache, contournement.
7. **Détection.** Valeurs de `Host` incohérentes avec le domaine attendu, liens générés anormaux.
8. **Prévention.** Ne pas faire confiance au `Host` ; utiliser une valeur canonique configurée côté serveur ; allowlist d'hôtes ; valider les en-têtes.
9. ⚠️ **Erreur fréquente.** Construire des liens absolus à partir de l'en-tête `Host` de la requête.
10. 🎯 **À retenir.** L'en-tête `Host` est contrôlable par le client : reposer dessus pour des décisions sensibles est une faille. Utiliser une valeur canonique fixe.

## Chapitre 120 — HTTP request smuggling

1. **Définition.** Attaque exploitant des *désaccords d'interprétation* des limites de requêtes HTTP entre deux serveurs en chaîne (frontal et back-end).
2. **Famille.** Erreurs de parsing (chapitre 75) au niveau protocole.
3. **Principe.** Quand le frontal et le back-end délimitent différemment les requêtes (longueur vs encodage par morceaux), l'attaquant « cache » une requête à l'un qui sera traitée par l'autre, désynchronisant le flux.
4. **Sous-types.** Selon l'incohérence exploitée entre composants ; variantes de désynchronisation.
5. **Exemple conceptuel.** Deux composants comptent différemment où finit une requête, si bien qu'un fragment est interprété comme une requête supplémentaire par le back-end.
6. **Impacts.** Contournement de contrôles, empoisonnement de cache, capture de requêtes d'autres utilisateurs, détournement de session.
7. **Détection.** Anomalies de framing HTTP, réponses désynchronisées, outils de détection spécialisés, journaux incohérents.
8. **Prévention.** Cohérence stricte du traitement HTTP entre composants, normalisation au frontal, rejet des requêtes ambiguës, configurations à jour, HTTP/2 de bout en bout bien configuré.
9. ⚠️ **Erreur fréquente.** Empiler des serveurs/proxys aux interprétations HTTP divergentes sans normalisation.
10. 🎯 **À retenir.** Le smuggling naît du désaccord entre serveurs sur « où finit une requête ». Normaliser et rejeter l'ambiguïté.

## Chapitre 121 — Cache poisoning

1. **Définition.** Empoisonnement d'un *cache* (web/CDN) pour servir un contenu malveillant à de nombreux utilisateurs.
2. **Famille.** Abus d'infrastructure web / parsing. CWE-444 apparenté.
3. **Principe.** Si le cache utilise comme clé une partie de la requête, mais que la réponse dépend d'éléments *non inclus dans la clé* (en-têtes non clés), l'attaquant peut faire stocker une réponse empoisonnée servie ensuite à tous.
4. **Sous-types.** Via en-têtes non clés, via paramètres ignorés par la clé, couplé à host header injection ou smuggling.
5. **Exemple conceptuel.** Un en-tête influençant la réponse mais ignoré par la clé de cache permet de faire mémoriser une version altérée de la page.
6. **Impacts.** Diffusion massive de contenu malveillant (XSS, redirection), déni de service, atteinte à l'intégrité.
7. **Détection.** Réponses en cache incohérentes, en-têtes inattendus influençant la réponse, surveillance du CDN.
8. **Prévention.** Inclure dans la clé de cache *tous* les éléments influençant la réponse, normaliser les entrées, durcir la configuration du cache, isoler les contenus dynamiques.
9. ⚠️ **Erreur fréquente.** Laisser des en-têtes influencer la réponse sans les inclure dans la clé de cache.
10. 🎯 **À retenir.** Tout ce qui modifie la réponse doit faire partie de la clé de cache, sinon le cache devient un amplificateur d'attaque.

## Chapitre 122 — Web cache deception

1. **Définition.** Tromper le cache pour qu'il stocke une page *contenant des données privées*, ensuite accessible à l'attaquant.
2. **Famille.** Abus d'infrastructure web (proche du cache poisoning, intention inverse).
3. **Principe.** En faisant croire au cache qu'une page dynamique privée est une ressource statique « cachable », l'attaquant l'amène à stocker la version personnalisée d'une victime, qu'il récupère ensuite.
4. **Sous-types.** Via extensions/chemins trompeurs, via règles de cache trop larges.
5. **Exemple conceptuel.** Une URL construite pour ressembler à une ressource statique amène le cache à mémoriser une page de profil personnalisée.
6. **Impacts.** Fuite de données privées d'autres utilisateurs, exposition d'informations de session.
7. **Détection.** Mise en cache de réponses authentifiées/personnalisées, règles de cache incohérentes.
8. **Prévention.** Ne jamais mettre en cache les réponses authentifiées/personnalisées, règles de cache strictes basées sur le type réel, en-têtes de cache explicites, normalisation des chemins.
9. ⚠️ **Erreur fréquente.** Règles « tout ce qui ressemble à du statique est cachable » sans vérifier le caractère privé de la réponse.
10. 🎯 **À retenir.** Le contenu privé ne doit jamais être mis en cache : des règles de cache précises évitent que des données personnelles soient partagées.

## Chapitre 123 — Prototype pollution

1. **Définition.** Attaque (écosystème JavaScript) altérant le *prototype partagé* des objets, modifiant le comportement global de l'application.
2. **Famille.** Rupture d'intégrité d'objets / injection de propriétés. CWE-1321.
3. **Principe.** En injectant des propriétés spéciales lors de fusions/copies d'objets non sécurisées, l'attaquant pollue le prototype hérité par tous les objets, ce qui peut altérer la logique, contourner des contrôles, voire mener à du XSS/RCE selon le contexte.
4. **Sous-types.** Côté client (vers XSS) et côté serveur (vers contournement/RCE), via fusion profonde, parsing, ou paramètres imbriqués.
5. **Exemple conceptuel.** Une fusion récursive d'un objet d'entrée injecte une propriété héritée qui modifie une valeur par défaut utilisée ailleurs dans l'application.
6. **Impacts.** Contournement de logique, déni de service, XSS, parfois RCE.
7. **Détection.** Propriétés spéciales dans les entrées, comportements globaux anormaux, audit des opérations de fusion/copie.
8. **Prévention.** Bloquer les clés dangereuses, objets sans prototype pour les données, fonctions de fusion sûres, validation de schéma, bibliothèques à jour, gel des prototypes le cas échéant.
9. ⚠️ **Erreur fréquente.** Fusionner récursivement des entrées non fiables dans des objets sans filtrer les clés spéciales.
10. 🎯 **À retenir.** La pollution de prototype contamine *tous* les objets : filtrer les clés dangereuses et n'utiliser que des fusions sûres.

## Chapitre 124 — Rate limit bypass

1. **Définition.** Contournement des mécanismes de *limitation de débit*, réactivant les attaques par répétition massive.
2. **Famille.** Abus / contournement de contrôle (lié au chapitre 79).
3. **Principe.** Si la limitation s'appuie sur un critère manipulable (en-tête d'IP falsifiable, casse d'URL, paramètres, comptes multiples), l'attaquant la contourne et reprend brute force, énumération ou scraping.
4. **Sous-types.** Via rotation d'IP/en-têtes, via variations d'URL/paramètres, via parallélisme, via comptes multiples.
5. **Exemple conceptuel.** Une limite appliquée selon un en-tête d'adresse falsifiable est contournée en variant cet en-tête à chaque requête.
6. **Impacts.** Réactivation du brute force/credential stuffing, énumération, déni de service, surcoûts.
7. **Détection.** Volume élevé malgré la limite, variations systématiques des critères de limitation, distribution d'IP anormale.
8. **Prévention.** Limiter sur des critères fiables (identité authentifiée, jetons), ne pas se fier aux en-têtes client, limitation côté serveur/passerelle, détection d'anomalies, défenses combinées.
9. ⚠️ **Erreur fréquente.** Limiter sur un en-tête d'IP fourni par le client (falsifiable) au lieu d'une source fiable.
10. 🎯 **À retenir.** Une limitation contournable n'en est pas une : s'appuyer sur des critères non manipulables.

## Chapitre 125 — Business logic abuse

1. **Définition.** Détournement du *fonctionnement légitime* de l'application pour obtenir un avantage non prévu, sans faille technique.
2. **Famille.** Logique métier (chapitre 72) côté attaque.
3. **Principe.** L'attaquant respecte la « technique » mais abuse des règles : ordre des étapes, cumuls, valeurs limites, conditions de course métier, automatisation d'actions prévues pour être manuelles.
4. **Sous-types.** Abus de remises/cumuls, contournement de workflow, manipulation de quantités/prix, exploitation de la concurrence (chapitre 73), automatisation abusive.
5. **Exemple conceptuel.** Enchaîner des étapes dans un ordre non prévu pour obtenir un bien sans franchir l'étape de paiement.
6. **Impacts.** Fraude, perte financière, contournement de contrôles, avantage indu — invisibles aux scanners.
7. **Détection.** Schémas d'usage anormaux, séquences d'actions atypiques, écarts métier, supervision fonctionnelle.
8. **Prévention.** Threat modeling métier, validation des règles et de l'ordre des étapes côté serveur, contrôles de cohérence, plafonds, idempotence, tests orientés abus, surveillance comportementale.
9. ⚠️ **Erreur fréquente.** Tester uniquement « est-ce que ça marche comme prévu », jamais « comment quelqu'un pourrait en abuser ».
10. 🎯 **À retenir.** L'abus de logique métier n'est pas un bug, c'est un usage détourné : seuls la réflexion métier et les tests d'abus le révèlent.

## Chapitre 126 — GraphQL abuse

1. **Définition.** Attaques propres aux API *GraphQL*, exploitant leur flexibilité de requêtage.
2. **Famille.** Abus d'API (Partie 10) appliqué à GraphQL.
3. **Principe.** GraphQL laisse le client composer ses requêtes (champs, profondeur, relations) ; sans garde-fous, cela ouvre la porte à la surcharge, à l'exposition excessive de données et au contournement d'autorisation par champ.
4. **Sous-types.** Requêtes profondes/imbriquées (DoS), introspection révélant le schéma, exposition excessive de champs, autorisation manquante au niveau champ/objet (BOLA/BFLA), batching abusif.
5. **Exemple conceptuel.** Une requête très imbriquée force le serveur à parcourir des relations en cascade, saturant les ressources.
6. **Impacts.** Déni de service, fuite de données (champs/objets non autorisés), reconnaissance via introspection.
7. **Détection.** Requêtes anormalement profondes/coûteuses, introspection en production, volumes inhabituels.
8. **Prévention.** Limites de profondeur/complexité/coût, autorisation *par champ et par objet*, désactivation/contrôle de l'introspection en production, limitation de débit, pagination obligatoire, validation de schéma.
9. ⚠️ **Erreur fréquente.** Exposer GraphQL avec introspection ouverte et sans limite de complexité ni contrôle d'autorisation fin.
10. 🎯 **À retenir.** La flexibilité de GraphQL est sa surface d'attaque : limiter la complexité et contrôler l'autorisation au niveau champ/objet.

---

> **Fin du Volume 3/8.**
>
> Vous disposez désormais d'une taxonomie complète des attaques web (chapitres 82–126), reliées à leurs familles, impacts, signaux de détection et défenses. Toutes se ramènent aux sept familles de la vue d'ensemble — et, plus en amont, aux familles de vulnérabilités de la Partie 5.
>
> **Suite — Volume 4 : Partie 7, Attaques réseau et infrastructure** (reconnaissance, sniffing, spoofing ARP/DNS/DHCP, MITM, replay, downgrade, exploitation de services, SMB/RDP/VPN, pivoting, mouvement latéral, DoS/DDoS, amplification/reflection, botnets, VLAN hopping, Wi-Fi evil twin, rogue AP, deauth, BGP hijacking).


---

# Taxonomie de la cybersécurité — Volume 4/8

> Partie 7 : Attaques réseau et infrastructure
>
> On quitte la couche applicative pour la couche réseau (chapitre 42). Ici, les attaques visent les *protocoles*, les *flux* et les *équipements*. Le fil conducteur : un attaquant qui a un pied dans le réseau (ou à proximité) cherche à *écouter*, *usurper*, *se déplacer* et *perturber*. Format en 10 points pour les attaques majeures.
>
> **Posture** : mécanismes et défenses, pas de procédure offensive opérationnelle.

---

# Partie 7 — Attaques réseau et infrastructure

## Vue d'ensemble taxonomique

Les attaques réseau se rangent en grandes intentions :

- **Reconnaissance** : découvrir la cible (scan, énumération).
- **Interception** : lire ce qui n'est pas pour soi (sniffing, MITM).
- **Usurpation** : se faire passer pour un autre élément du réseau (spoofing ARP/DNS/DHCP).
- **Rejeu et dégradation** : réutiliser ou affaiblir (replay, downgrade).
- **Exploitation et déplacement** : entrer puis circuler (services exposés, SMB/RDP/VPN, pivoting, lateral movement).
- **Disponibilité** : empêcher de fonctionner (DoS, DDoS, amplification, reflection, botnets).
- **Couche 2 / sans fil / routage** : abuser de l'infrastructure elle-même (VLAN hopping, evil twin, rogue AP, deauth, BGP hijacking).

🧭 **Taxonomie** — Beaucoup de ces attaques correspondent aux tactiques MITRE ATT&CK *Reconnaissance, Discovery, Lateral Movement, Collection, Impact*.

---

## Chapitre 127 — Reconnaissance et scan

1. **Définition.** Phase de collecte d'informations sur une cible : identifier hôtes, ports, services, versions, technologies.
2. **Famille.** Reconnaissance (ATT&CK *Reconnaissance/Discovery*).
3. **Principe.** Avant d'attaquer, l'adversaire cartographie la surface : reconnaissance *passive* (sources ouvertes, OSINT, sans toucher la cible) et *active* (scan de ports/services qui interroge directement la cible).
4. **Sous-types.** Reconnaissance passive (OSINT, DNS public, fuites), scan de ports, détection de services/versions, balayage réseau, découverte d'hôtes.
5. **Exemple conceptuel.** Recenser les sous-domaines et services exposés d'une organisation pour repérer une cible vulnérable, sans interaction intrusive.
6. **Impacts.** Préparation d'attaque ciblée ; en soi, peu de dommage, mais signal d'intention.
7. **Détection.** Pics de connexions vers de nombreux ports/hôtes, schémas de balayage, requêtes inhabituelles, signatures IDS.
8. **Prévention.** Réduction de surface (chapitre 22), minimisation de l'exposition, masquage des bannières/versions, surveillance, gestion de l'empreinte externe (ASM), pare-feu.
9. ⚠️ **Erreur fréquente.** Exposer des services et bannières détaillées qui facilitent le ciblage.
10. 🎯 **À retenir.** La reconnaissance précède tout : réduire ce qui est visible et exposé limite les options de l'attaquant dès le départ.

## Chapitre 128 — Énumération

1. **Définition.** Approfondissement de la reconnaissance : extraire des détails précis (comptes, partages, utilisateurs, configurations) d'un service identifié.
2. **Famille.** Reconnaissance/Discovery.
3. **Principe.** Une fois un service repéré, l'attaquant l'interroge pour lister ses objets : utilisateurs, groupes, partages réseau, informations d'annuaire, points d'API.
4. **Sous-types.** Énumération de comptes, de partages, d'annuaire (LDAP/AD), de services, d'API/endpoints.
5. **Exemple conceptuel.** Interroger un service pour distinguer les noms de comptes valides des invalides (énumération d'utilisateurs).
6. **Impacts.** Cartographie fine, préparation du brute force/spraying ciblé, découverte de chemins.
7. **Détection.** Requêtes répétitives systématiques, réponses différenciées exploitées, volume anormal.
8. **Prévention.** Réponses uniformes (anti-énumération), durcissement des services, limitation de débit, restriction d'accès, surveillance.
9. ⚠️ **Erreur fréquente.** Renvoyer des messages d'erreur qui distinguent « compte inexistant » de « mauvais mot de passe » (énumération offerte).
10. 🎯 **À retenir.** L'énumération transforme une liste vague en cibles précises : uniformiser les réponses et limiter les requêtes la freine.

## Chapitre 129 — Sniffing

1. **Définition.** Capture passive du trafic réseau pour en lire le contenu.
2. **Famille.** Interception (ATT&CK *Collection — Network Sniffing*) ; lié à l'absence de chiffrement (chapitre 68).
3. **Principe.** Sur un réseau partagé ou après un détournement de flux, l'attaquant écoute les paquets ; tout ce qui n'est pas chiffré (identifiants, données, jetons) est lisible.
4. **Sous-types.** Sniffing passif (sur média partagé), sniffing après spoofing/MITM, capture sur Wi-Fi.
5. **Exemple conceptuel.** Sur un réseau mal segmenté, des identifiants transmis en clair par un protocole non chiffré sont capturés.
6. **Impacts.** Vol d'identifiants et de données, atteinte à la confidentialité, préparation d'autres attaques.
7. **Détection.** Difficile (passif) ; indices via la détection de mode promiscuité, d'équipements suspects, d'attaques de redirection associées.
8. **Prévention.** **Chiffrement de bout en bout** (TLS), segmentation, commutation (vs hubs), 802.1X, désactivation des protocoles en clair, VPN sur réseaux non fiables.
9. ⚠️ **Erreur fréquente.** Supposer que le réseau interne est « sûr » et y laisser circuler des données en clair.
10. 🎯 **À retenir.** Le sniffing ne lit que ce qui n'est pas chiffré : chiffrer en transit neutralise l'essentiel de la menace.

## Chapitre 130 — Spoofing (vue d'ensemble)

1. **Définition.** Usurpation d'identité d'un élément du réseau (adresse, hôte, service) pour tromper d'autres systèmes.
2. **Famille.** Usurpation. Englobe ARP (131), DNS (132), DHCP (134) spoofing, et le spoofing d'adresses en général.
3. **Principe.** De nombreux protocoles historiques font *confiance par défaut* sans authentifier l'origine ; l'attaquant se fait passer pour une entité légitime (passerelle, serveur DNS, etc.).
4. **Sous-types.** Spoofing d'adresse IP/MAC, ARP, DNS, DHCP, d'e-mail (Partie 9), d'identité de service.
5. **Exemple conceptuel.** Se présenter comme la passerelle du réseau pour que les autres machines envoient leur trafic à l'attaquant.
6. **Impacts.** MITM, interception, redirection, déni de service, base de nombreuses autres attaques réseau.
7. **Détection.** Incohérences d'association (adresse/identité), changements anormaux de tables, surveillance réseau.
8. **Prévention.** Authentification des protocoles, fonctions de sécurité des commutateurs (inspection ARP dynamique, snooping DHCP), segmentation, chiffrement, supervision.
9. ⚠️ **Erreur fréquente.** S'appuyer sur des protocoles non authentifiés sans activer les protections des équipements.
10. 🎯 **À retenir.** Le spoofing exploite la confiance non vérifiée des protocoles : authentifier et activer les protections de commutateur sont les parades clés.

## Chapitre 131 — ARP spoofing

1. **Définition.** Usurpation au niveau de la résolution adresse IP↔MAC (protocole ARP) sur un réseau local.
2. **Famille.** Spoofing (chapitre 130), couche 2.
3. **Principe.** ARP n'authentifie pas les réponses ; l'attaquant annonce que sa propre adresse MAC correspond à l'IP de la passerelle (ou d'un hôte), détournant le trafic vers lui (MITM/sniffing).
4. **Sous-types.** Détournement vers l'attaquant (MITM), déni de service (associations erronées).
5. **Exemple conceptuel.** Les machines du réseau local sont amenées à envoyer leur trafic « vers la passerelle » à l'attaquant, qui relaie en écoutant.
6. **Impacts.** MITM, sniffing, vol d'identifiants, manipulation de trafic, DoS local.
7. **Détection.** Associations IP/MAC changeantes ou dupliquées, surveillance ARP, alertes des outils dédiés.
8. **Prévention.** **Inspection ARP dynamique (DAI)**, snooping DHCP, entrées statiques pour les actifs critiques, segmentation, chiffrement (limite l'impact), 802.1X.
9. ⚠️ **Erreur fréquente.** Réseau local plat sans protections de commutateur.
10. 🎯 **À retenir.** L'ARP spoofing rend le MITM local trivial ; l'inspection ARP dynamique et la segmentation sont les défenses de référence.

## Chapitre 132 — DNS spoofing

1. **Définition.** Falsification des réponses DNS pour rediriger une victime vers une adresse contrôlée par l'attaquant.
2. **Famille.** Spoofing (chapitre 130).
3. **Principe.** En répondant à une requête DNS avant le serveur légitime (ou en empoisonnant un cache), l'attaquant fait correspondre un nom de domaine à une mauvaise adresse.
4. **Sous-types.** Réponse falsifiée locale (souvent après MITM), empoisonnement de cache DNS, manipulation de résolveur.
5. **Exemple conceptuel.** Une victime saisit un nom de site légitime mais est dirigée vers un serveur malveillant à cause d'une réponse DNS falsifiée.
6. **Impacts.** Redirection vers phishing/malware, MITM, interception, contournement de confiance.
7. **Détection.** Réponses DNS incohérentes, résolutions anormales, surveillance DNS.
8. **Prévention.** **DNSSEC** (intégrité des réponses), DNS chiffré (DoH/DoT), résolveurs de confiance, protection contre l'ARP/MITM en amont, surveillance.
9. ⚠️ **Erreur fréquente.** Faire confiance aveuglément à la résolution DNS sur un réseau non maîtrisé.
10. 🎯 **À retenir.** Le DNS spoofing détourne la « carte » du réseau ; DNSSEC et DNS chiffré renforcent l'intégrité des résolutions.

## Chapitre 133 — DNS tunneling

1. **Définition.** Détournement du protocole DNS comme *canal caché* pour exfiltrer des données ou commander un implant (C2).
2. **Famille.** Exfiltration / commande et contrôle (ATT&CK *Exfiltration/C2*).
3. **Principe.** Le DNS est souvent autorisé à sortir même quand le reste est filtré ; l'attaquant encode des données dans les requêtes/réponses DNS pour traverser discrètement le pare-feu.
4. **Sous-types.** Exfiltration de données via DNS, canal C2 via DNS, selon l'encodage et la fréquence.
5. **Exemple conceptuel.** Des données sont encodées dans des noms de sous-domaines résolus vers un serveur DNS contrôlé par l'attaquant, qui les reconstitue.
6. **Impacts.** Exfiltration furtive, contrôle d'implants, contournement du filtrage.
7. **Détection.** Volumes/longueurs de requêtes DNS anormaux, domaines à forte entropie, fréquence inhabituelle, analyse DNS.
8. **Prévention.** Filtrage et inspection DNS, résolveurs internes contrôlés, détection d'anomalies, limitation des résolutions sortantes, filtrage de réputation.
9. ⚠️ **Erreur fréquente.** Laisser le DNS sortir sans inspection ni journalisation, le considérant « inoffensif ».
10. 🎯 **À retenir.** Le DNS peut servir de tunnel furtif : inspecter et journaliser le DNS sortant est essentiel.

## Chapitre 134 — DHCP spoofing

1. **Définition.** Usurpation d'un serveur DHCP pour distribuer aux clients une configuration réseau malveillante.
2. **Famille.** Spoofing (chapitre 130), couche 2/3.
3. **Principe.** Un faux serveur DHCP (rogue) répond aux demandes des clients en fournissant une passerelle/DNS contrôlés par l'attaquant, le plaçant en position de MITM.
4. **Sous-types.** Rogue DHCP, épuisement d'adresses (DHCP starvation) précédant l'installation du rogue.
5. **Exemple conceptuel.** Un client obtient une configuration réseau d'un serveur DHCP pirate, désignant l'attaquant comme passerelle.
6. **Impacts.** MITM, redirection DNS, interception, déni de service.
7. **Détection.** Présence de serveurs DHCP non autorisés, baux incohérents, surveillance.
8. **Prévention.** **DHCP snooping** (n'autoriser le DHCP que sur des ports de confiance), segmentation, surveillance, 802.1X.
9. ⚠️ **Erreur fréquente.** Ne pas activer le DHCP snooping, laissant n'importe quel hôte jouer au serveur DHCP.
10. 🎯 **À retenir.** Le DHCP snooping empêche les serveurs DHCP pirates et coupe ce vecteur de MITM.

## Chapitre 135 — Man-in-the-Middle (MITM)

1. **Définition.** Position d'attaque où l'adversaire s'intercale entre deux parties pour lire et/ou altérer leurs échanges.
2. **Famille.** Interception/usurpation (ATT&CK *Collection — Adversary-in-the-Middle*).
3. **Principe.** Après un détournement de flux (ARP/DNS/DHCP spoofing, rogue AP), l'attaquant relaie les communications en les écoutant, voire en les modifiant, idéalement sans que les parties s'en aperçoivent.
4. **Sous-types.** MITM passif (écoute) vs actif (modification), sur LAN, sur Wi-Fi, via proxy malveillant, downgrade TLS.
5. **Exemple conceptuel.** L'attaquant relaie le trafic entre une victime et un service, capturant ce qui transite et pouvant l'altérer.
6. **Impacts.** Vol d'identifiants/données, manipulation de contenu, contournement d'intégrité, injection.
7. **Détection.** Anomalies de certificats, alertes de spoofing en amont, latences/erreurs TLS, surveillance.
8. **Prévention.** **Chiffrement fort et authentifié** (TLS validé, HSTS), épinglage le cas échéant, protections couche 2 (DAI, DHCP snooping), VPN sur réseaux non fiables, vigilance aux avertissements de certificat.
9. ⚠️ **Erreur fréquente.** Ignorer/accepter les avertissements de certificat (qui signalent souvent un MITM).
10. 🎯 **À retenir.** Le MITM est l'aboutissement de l'interception : le chiffrement *authentifié* (et le respect des alertes de certificat) le rend inefficace.

## Chapitre 136 — Replay attack

1. **Définition.** Réémission de données légitimes capturées (jetons, requêtes authentifiées) pour reproduire une action sans connaître les secrets.
2. **Famille.** Rejeu (CWE-294).
3. **Principe.** Si un message d'authentification/transaction n'est pas lié à un usage unique (nonce, horodatage, séquence), l'attaquant qui l'a capturé peut le « rejouer » pour se faire passer pour l'émetteur.
4. **Sous-types.** Rejeu de jetons/sessions, de requêtes de paiement, de messages d'authentification.
5. **Exemple conceptuel.** Un message d'autorisation capturé est renvoyé tel quel plus tard pour répéter l'action autorisée.
6. **Impacts.** Usurpation, transactions répétées, contournement d'authentification.
7. **Détection.** Messages identiques répétés, horodatages incohérents, séquences anormales.
8. **Prévention.** **Nonces**, horodatages avec fenêtre courte, numéros de séquence, jetons à usage unique, canaux chiffrés authentifiés, idempotence.
9. ⚠️ **Erreur fréquente.** Authentifier sans garantir la *fraîcheur* du message (pas de nonce/horodatage).
10. 🎯 **À retenir.** Sans élément de fraîcheur (nonce/horodatage), un message valide peut être rejoué : lier chaque message à un usage unique.

## Chapitre 137 — Downgrade attack

1. **Définition.** Forcer deux parties à utiliser une version/un algorithme *plus faible* d'un protocole, exploitable ensuite.
2. **Famille.** Dégradation / cryptographie faible (chapitre 68).
3. **Principe.** Pendant la négociation, l'attaquant supprime/altère les options fortes pour imposer un mode vulnérable (chiffrement obsolète, protocole ancien), qu'il peut alors attaquer.
4. **Sous-types.** Downgrade de version TLS/protocole, de suite cryptographique, désactivation forcée du chiffrement (strip).
5. **Exemple conceptuel.** Une négociation est manipulée pour retomber sur une version ancienne et faible d'un protocole, ouvrant la voie à l'interception.
6. **Impacts.** Interception, MITM, cassage cryptographique, contournement de protections.
7. **Détection.** Usage de versions/suites obsolètes, négociations anormales, surveillance TLS.
8. **Prévention.** **Désactiver les versions/algorithmes faibles**, exiger des minimums (TLS récent), HSTS, options anti-downgrade des protocoles, surveillance de la configuration.
9. ⚠️ **Erreur fréquente.** Garder, « pour compatibilité », des protocoles/suites obsolètes activés.
10. 🎯 **À retenir.** On ne peut pas être rétrogradé vers ce qui est désactivé : supprimer les versions et algorithmes faibles ferme la porte au downgrade.

## Chapitre 138 — Exploitation de service exposé

1. **Définition.** Exploitation d'une vulnérabilité dans un service réseau accessible (souvent depuis Internet) pour obtenir un accès.
2. **Famille.** Exploitation (ATT&CK *Initial Access / Exploitation of Remote Services*).
3. **Principe.** Un service exposé et vulnérable (non patché, mal configuré) est attaqué pour exécuter du code ou s'authentifier indûment, fournissant un point d'entrée.
4. **Sous-types.** Exploitation de RCE, de contournement d'authentification, de mauvaise configuration ; sur services web, VPN, bases, partages.
5. **Exemple conceptuel.** Une passerelle exposée et non patchée est exploitée pour obtenir un premier accès au réseau interne.
6. **Impacts.** Accès initial, exécution de code, point de départ du mouvement latéral et de la compromission.
7. **Détection.** Tentatives d'exploitation (signatures IDS/IPS), comportements anormaux du service, alertes EDR, journaux.
8. **Prévention.** **Gestion des vulnérabilités** (patch prioritaire des services exposés), réduction de surface, segmentation, durcissement, accès via bastion/VPN+MFA, supervision.
9. ⚠️ **Erreur fréquente.** Exposer sur Internet des services d'administration ou non patchés (cf. KEV — chapitre 32).
10. 🎯 **À retenir.** Un service exposé non patché est la porte d'entrée n°1 des intrusions : patcher en priorité ce qui est exposé.

## Chapitre 139 — SMB abuse

1. **Définition.** Abus du protocole de partage de fichiers Windows (SMB) pour accès, propagation ou exécution.
2. **Famille.** Exploitation / lateral movement (environnement Windows).
3. **Principe.** SMB sert au partage de fichiers et à diverses opérations administratives ; mal configuré, exposé ou vulnérable, il permet l'accès aux partages, la capture/le relais d'authentification, ou l'exécution à distance.
4. **Sous-types.** Accès à des partages mal protégés, relais d'authentification (NTLM relay), exécution distante via SMB, propagation de malware/ransomware.
5. **Exemple conceptuel.** Un partage accessible et des authentifications relayées permettent de se déplacer vers d'autres machines.
6. **Impacts.** Accès aux données, mouvement latéral, propagation de ransomware, exécution de code.
7. **Détection.** Connexions SMB anormales, relais NTLM, accès massifs aux partages, alertes EDR.
8. **Prévention.** Désactiver SMBv1, signature SMB, segmentation, ne jamais exposer SMB sur Internet, durcissement de l'authentification, moindre privilège, surveillance.
9. ⚠️ **Erreur fréquente.** Laisser SMBv1 activé ou des partages largement accessibles ; exposer SMB hors du réseau interne.
10. 🎯 **À retenir.** SMB est un vecteur classique de propagation interne : le durcir (signature, pas de v1) et le segmenter est crucial. Détaillé côté identité en Partie 8.

## Chapitre 140 — RDP abuse

1. **Définition.** Abus du Bureau à distance (RDP) pour accès interactif non autorisé.
2. **Famille.** Exploitation / accès distant.
3. **Principe.** RDP donne un contrôle interactif d'une machine ; exposé sur Internet ou protégé par des identifiants faibles, il est ciblé par brute force, credential stuffing, ou exploitation de vulnérabilités.
4. **Sous-types.** Brute force/spraying RDP, exploitation de vulnérabilités RDP, détournement de session, pivot via RDP.
5. **Exemple conceptuel.** Un serveur RDP exposé avec un mot de passe faible est compromis, offrant un accès interactif au réseau.
6. **Impacts.** Accès initial, contrôle interactif, mouvement latéral, déploiement de ransomware (vecteur très courant).
7. **Détection.** Pics d'échecs/réussites RDP, connexions depuis l'extérieur ou à des heures anormales, alertes.
8. **Prévention.** **Ne pas exposer RDP sur Internet** (bastion/VPN+MFA), MFA, comptes forts, verrouillage anti-brute-force, restriction réseau, patch, surveillance.
9. ⚠️ **Erreur fréquente.** Exposer directement RDP sur Internet : l'un des vecteurs de rançongiciel les plus exploités.
10. 🎯 **À retenir.** RDP ne doit jamais être exposé nu sur Internet : passer par bastion/VPN + MFA et surveiller les accès.

## Chapitre 141 — VPN exploitation

1. **Définition.** Compromission des passerelles/accès VPN (chapitre 55) pour pénétrer le réseau interne.
2. **Famille.** Exploitation / accès initial.
3. **Principe.** Le VPN, exposé par conception et donnant accès au cœur du réseau, est ciblé via vulnérabilités critiques de la passerelle, vol/réutilisation d'identifiants, ou contournement de MFA.
4. **Sous-types.** Exploitation de CVE de passerelle (RCE), credential stuffing/spraying, contournement/absence de MFA.
5. **Exemple conceptuel.** Une vulnérabilité critique non patchée d'une passerelle VPN permet un accès au réseau interne sans identifiants valides.
6. **Impacts.** Accès initial direct au cœur du réseau, mouvement latéral, compromission étendue.
7. **Détection.** Connexions VPN anormales (lieux, horaires), tentatives d'exploitation, échecs MFA, surveillance.
8. **Prévention.** Patch prioritaire des passerelles, MFA résistant au phishing, moindre privilège d'accès, segmentation post-connexion, migration vers ZTNA, journalisation.
9. ⚠️ **Erreur fréquente.** Retarder les patchs de passerelle VPN ou ne pas y imposer le MFA.
10. 🎯 **À retenir.** Le VPN est une cible de choix : patch immédiat + MFA + moindre privilège, et envisager le ZTNA.

## Chapitre 142 — Pivoting

1. **Définition.** Utiliser une machine compromise comme *relais* pour atteindre des segments réseau autrement inaccessibles.
2. **Famille.** Mouvement latéral / post-exploitation (ATT&CK *Lateral Movement*).
3. **Principe.** Une fois un hôte compromis, l'attaquant l'emploie comme tremplin pour rebondir vers d'autres réseaux qu'il « voit » mais que l'attaquant ne pouvait pas joindre directement.
4. **Sous-types.** Pivot via proxy, redirection de ports, tunneling (chapitre 143).
5. **Exemple conceptuel.** Un poste compromis dans une zone bureautique sert de relais pour atteindre une zone serveur reliée à lui.
6. **Impacts.** Extension de l'accès, contournement de la segmentation imparfaite, progression vers les cibles de valeur.
7. **Détection.** Flux inhabituels entre segments via un hôte, relais/proxy anormaux, trafic est-ouest atypique, EDR/NDR.
8. **Prévention.** **Segmentation/microsegmentation** stricte, moindre privilège, surveillance est-ouest, restriction des flux entre zones, EDR.
9. ⚠️ **Erreur fréquente.** Compter sur une segmentation « partielle » qu'un hôte à cheval sur deux zones annule.
10. 🎯 **À retenir.** Le pivoting transforme un hôte compromis en pont entre zones : une segmentation rigoureuse et la surveillance est-ouest le contrent.

## Chapitre 143 — Tunneling

1. **Définition.** Encapsuler un trafic dans un autre protocole autorisé pour contourner filtrage et détection.
2. **Famille.** Évasion / exfiltration / C2 (ATT&CK *Command and Control — Protocol Tunneling*).
3. **Principe.** L'attaquant fait passer son trafic « interdit » à l'intérieur d'un protocole « autorisé » (DNS, HTTP/S, ICMP), traversant les contrôles qui n'inspectent pas le contenu.
4. **Sous-types.** Tunnel DNS (chapitre 133), HTTP/S, ICMP, via services cloud légitimes.
5. **Exemple conceptuel.** Un canal de commande est dissimulé dans du trafic web sortant chiffré, indistinct du trafic légitime.
6. **Impacts.** Contournement du filtrage, C2 furtif, exfiltration discrète.
7. **Détection.** Anomalies de volume/forme dans les protocoles autorisés, destinations inhabituelles, analyse comportementale, inspection.
8. **Prévention.** Filtrage et inspection en sortie, proxys avec inspection TLS maîtrisée, allowlist de destinations, détection d'anomalies, journalisation, restriction des protocoles sortants.
9. ⚠️ **Erreur fréquente.** N'inspecter que les ports/protocoles « à risque » et laisser HTTP/S/DNS sortir sans analyse.
10. 🎯 **À retenir.** Le tunneling cache l'interdit dans l'autorisé : seules l'inspection et l'analyse comportementale des flux sortants le révèlent.

## Chapitre 144 — Lateral movement

1. **Définition.** Déplacement d'un attaquant d'un système à un autre *au sein* du réseau, après l'accès initial, pour progresser vers ses objectifs.
2. **Famille.** ATT&CK *Lateral Movement* — pivot central de toute intrusion sérieuse.
3. **Principe.** Rarement l'accès initial atteint-il directement la cible. L'attaquant rebondit de machine en machine, en réutilisant des identifiants, en abusant de services d'administration (SMB/RDP/WinRM) et de relations de confiance, jusqu'aux actifs de valeur.
4. **Sous-types.** Via identifiants volés (pass-the-hash/ticket — Partie 8), via SMB/RDP/WinRM, via tâches planifiées, via outils d'administration légitimes (living-off-the-land).
5. **Exemple conceptuel.** Des identifiants récupérés sur un poste servent à se connecter à un serveur, puis à un contrôleur de domaine, de proche en proche.
6. **Impacts.** Extension de la compromission, accès aux joyaux, préalable au ransomware/exfiltration.
7. **Détection.** Connexions inter-machines anormales, usage atypique de comptes/outils d'administration, trafic est-ouest, EDR/NDR, corrélation SIEM.
8. **Prévention.** **Segmentation/microsegmentation**, **tiering** (chapitre 19), moindre privilège, MFA, LAPS (mots de passe locaux uniques), durcissement de l'administration (bastion/PAM), détection comportementale.
9. ⚠️ **Erreur fréquente.** Mots de passe d'administrateur local identiques partout : un seul vol permet de se déplacer sur tout le parc.
10. 🎯 **À retenir.** Le mouvement latéral est le cœur des intrusions réelles : segmentation, tiering, identifiants locaux uniques (LAPS) et moindre privilège le rendent coûteux. Approfondi en Partie 8.

## Chapitre 145 — DoS (Denial of Service)

1. **Définition.** Attaque visant à rendre un service indisponible, en l'épuisant ou en exploitant une faiblesse.
2. **Famille.** Disponibilité (CIA — chapitre 5 ; ATT&CK *Impact*). CWE-400.
3. **Principe.** Submerger les ressources (calcul, mémoire, bande passante, connexions) ou déclencher un plantage par une entrée pathologique, jusqu'à l'arrêt du service pour les utilisateurs légitimes.
4. **Sous-types.** DoS volumétrique (saturation), applicatif (requêtes coûteuses), par exploitation (crash), par épuisement d'état.
5. **Exemple conceptuel.** Une requête particulièrement coûteuse, répétée, sature les ressources et rend le service injoignable.
6. **Impacts.** Indisponibilité, perte de revenus/réputation, parfois diversion pour masquer une autre attaque.
7. **Détection.** Pics de trafic/charge, requêtes coûteuses répétées, dégradation des performances, surveillance.
8. **Prévention.** Limitation de débit (chapitre 79), dimensionnement/élasticité, optimisation des opérations coûteuses, filtrage, time-outs, protections en amont.
9. ⚠️ **Erreur fréquente.** Ignorer le DoS applicatif (peu de trafic mais requêtes très coûteuses) en se focalisant sur le volumétrique.
10. 🎯 **À retenir.** Le DoS attaque la disponibilité ; au-delà du volume, surveiller le coût unitaire des requêtes et plafonner.

## Chapitre 146 — DDoS (Distributed Denial of Service)

1. **Définition.** DoS mené depuis de *nombreuses sources* distribuées (souvent un botnet), démultipliant la puissance.
2. **Famille.** Disponibilité (ATT&CK *Impact — Network Denial of Service*).
3. **Principe.** Des milliers de machines compromises (ou des techniques d'amplification) génèrent simultanément du trafic vers la cible, rendant le filtrage par source difficile et saturant la capacité.
4. **Sous-types.** Volumétrique distribué, par épuisement de protocole, applicatif distribué, combiné à l'amplification/reflection (chapitres 147–148).
5. **Exemple conceptuel.** Un grand nombre d'hôtes répartis envoient simultanément du trafic vers un service, dépassant sa capacité.
6. **Impacts.** Indisponibilité massive, coûts, parfois extorsion (DDoS for ransom), diversion.
7. **Détection.** Pics massifs multi-sources, signatures de DDoS, alertes des protections amont.
8. **Prévention.** **Services anti-DDoS** (scrubbing, CDN), absorption à grande échelle, filtrage en amont (chez l'opérateur), surdimensionnement, plans de réponse, anycast.
9. ⚠️ **Erreur fréquente.** Tenter d'absorber un DDoS volumétrique uniquement sur sa propre infrastructure (capacité insuffisante).
10. 🎯 **À retenir.** Le DDoS exige une défense *en amont* (opérateur/CDN/scrubbing) : on ne le bloque pas seul à la porte de ses serveurs.

## Chapitre 147 — Reflection attack

1. **Définition.** DDoS où l'attaquant envoie des requêtes à des serveurs tiers en *usurpant l'adresse de la victime*, qui reçoit alors toutes les réponses.
2. **Famille.** DDoS (chapitre 146), technique de réflexion.
3. **Principe.** En falsifiant l'adresse source (spoofing), l'attaquant fait répondre des serveurs légitimes *vers la victime*, masquant l'origine réelle et concentrant le trafic sur la cible.
4. **Sous-types.** Réflexion via divers protocoles UDP sans état ; souvent combinée à l'amplification (chapitre 148).
5. **Exemple conceptuel.** De nombreux serveurs tiers, sollicités avec l'adresse usurpée de la victime, lui renvoient leurs réponses simultanément.
6. **Impacts.** Saturation de la victime, anonymisation de l'attaquant.
7. **Détection.** Afflux de réponses non sollicitées vers la victime, sources multiples « légitimes », surveillance.
8. **Prévention.** **Anti-spoofing** (filtrage des adresses source côté opérateurs — BCP38), durcissement des services réflecteurs, anti-DDoS amont, limitation.
9. ⚠️ **Erreur fréquente.** Laisser des services exploitables comme réflecteurs accessibles publiquement.
10. 🎯 **À retenir.** La réflexion détourne des serveurs tiers contre la victime ; l'anti-spoofing réseau et le durcissement des réflecteurs la limitent.

## Chapitre 148 — Amplification attack

1. **Définition.** Variante de réflexion où la *réponse* est bien plus grande que la requête, multipliant le volume envoyé à la victime.
2. **Famille.** DDoS (chapitre 146), couplée à la réflexion.
3. **Principe.** L'attaquant choisit des protocoles dont une petite requête déclenche une grosse réponse ; combiné au spoofing, un faible effort génère un trafic massif vers la victime (facteur d'amplification).
4. **Sous-types.** Selon les protocoles à fort facteur d'amplification.
5. **Exemple conceptuel.** Une petite requête usurpée déclenche une réponse volumineuse dirigée vers la victime, démultipliant le débit d'attaque.
6. **Impacts.** Saturation très efficace avec peu de ressources côté attaquant.
7. **Détection.** Trafic entrant volumineux d'un protocole donné, réponses massives non sollicitées, surveillance.
8. **Prévention.** Identiques à la réflexion (anti-spoofing, durcissement des services amplificateurs, anti-DDoS amont, désactivation/limitation des services exposés exploitables).
9. ⚠️ **Erreur fréquente.** Exposer publiquement des services connus pour leur fort facteur d'amplification, sans restriction.
10. 🎯 **À retenir.** L'amplification rend le DDoS « pas cher » pour l'attaquant : durcir les services amplificateurs et filtrer le spoofing en amont.

## Chapitre 149 — Botnet

1. **Définition.** Réseau de machines compromises (bots) contrôlées à distance par un attaquant pour des actions coordonnées.
2. **Famille.** Infrastructure offensive / C2 (ATT&CK *Command and Control*, *Impact*).
3. **Principe.** Des hôtes infectés (postes, serveurs, IoT) reçoivent des ordres d'un serveur de commande et contrôle (C2) et exécutent collectivement des tâches : DDoS, spam, minage, exfiltration, relais.
4. **Sous-types.** Botnets DDoS, de spam, de minage, IoT, à C2 centralisé vs pair-à-pair, à C2 furtif (DNS/HTTP).
5. **Exemple conceptuel.** Des milliers d'objets connectés mal sécurisés sont enrôlés pour lancer un DDoS sur commande.
6. **Impacts.** DDoS massif, spam/phishing à grande échelle, minage, relais d'attaques, exfiltration.
7. **Détection.** Trafic C2 (balises périodiques), connexions vers des domaines/IP malveillants, comportements coordonnés, EDR/NDR, renseignement (CTI).
8. **Prévention.** Hygiène anti-malware (EDR, patch), durcissement IoT (chapitre 52), filtrage sortant et de réputation, détection de C2, segmentation, sensibilisation.
9. ⚠️ **Erreur fréquente.** Négliger les objets connectés peu sécurisés, principal réservoir de bots.
10. 🎯 **À retenir.** Un botnet transforme des machines négligées en armée offensive : l'hygiène (patch, EDR, IoT durci) tarit la source, la détection de C2 repère l'enrôlement.

## Chapitre 150 — VLAN hopping

1. **Définition.** Attaque permettant à un hôte de communiquer avec un VLAN auquel il ne devrait pas avoir accès, brisant la segmentation de couche 2.
2. **Famille.** Couche 2 / contournement de segmentation.
3. **Principe.** En exploitant des configurations de commutateur permissives (négociation de trunk automatique, double étiquetage), un attaquant fait sortir son trafic du VLAN attribué vers un autre.
4. **Sous-types.** Via usurpation de commutateur (switch spoofing), via double tagging.
5. **Exemple conceptuel.** Un hôte se fait passer pour un commutateur et négocie un lien trunk, accédant à des VLAN normalement isolés.
6. **Impacts.** Contournement de la segmentation, accès à des zones sensibles, MITM inter-VLAN.
7. **Détection.** Négociations de trunk inattendues, trafic inter-VLAN anormal, surveillance des commutateurs.
8. **Prévention.** **Désactiver la négociation automatique de trunk**, fixer explicitement les ports en mode accès, VLAN natif dédié, durcissement des commutateurs, restriction des ports.
9. ⚠️ **Erreur fréquente.** Laisser les ports en négociation automatique (DTP) et un VLAN natif partagé.
10. 🎯 **À retenir.** La segmentation VLAN n'est sûre que si les commutateurs sont durcis : désactiver la négociation de trunk et fixer les modes de port.

## Chapitre 151 — Wi-Fi Evil Twin

1. **Définition.** Faux point d'accès Wi-Fi imitant un réseau légitime pour capter les connexions des victimes.
2. **Famille.** Sans fil / usurpation / MITM.
3. **Principe.** L'attaquant diffuse un point d'accès portant le même nom (SSID) qu'un réseau de confiance ; les appareils s'y connectent, plaçant l'attaquant en position de MITM.
4. **Sous-types.** Evil twin sur réseau ouvert, avec portail captif factice, couplé à la deauth (chapitre 153) pour forcer la reconnexion.
5. **Exemple conceptuel.** Dans un lieu public, un faux réseau au nom familier capte les appareils qui s'y connectent automatiquement.
6. **Impacts.** MITM, vol d'identifiants, interception, injection, redirection vers phishing.
7. **Détection.** Points d'accès dupliqués (même SSID, BSSID différent), détection de rogue AP (WIPS), surveillance.
8. **Prévention.** WPA2/WPA3-Enterprise (authentification mutuelle), VPN sur Wi-Fi non fiable, désactivation de la connexion automatique, sensibilisation, WIPS.
9. ⚠️ **Erreur fréquente.** Se connecter automatiquement à des réseaux ouverts au nom familier.
10. 🎯 **À retenir.** L'evil twin exploite la confiance dans un nom de réseau : l'authentification mutuelle (WPA-Enterprise) et le VPN le neutralisent.

## Chapitre 152 — Rogue access point

1. **Définition.** Point d'accès non autorisé branché sur le réseau (souvent par un employé bien intentionné ou un attaquant), créant une entrée incontrôlée.
2. **Famille.** Sans fil / extension non maîtrisée de surface.
3. **Principe.** Un AP non géré relié au réseau interne ouvre un accès sans fil échappant aux contrôles, contournant le périmètre filaire sécurisé.
4. **Sous-types.** Rogue AP interne (employé), AP malveillant (attaquant), distinct de l'evil twin (qui imite, sans forcément être branché au réseau).
5. **Exemple conceptuel.** Un petit point d'accès personnel branché sur une prise réseau interne crée une porte d'entrée sans fil non sécurisée.
6. **Impacts.** Accès non contrôlé au réseau interne, contournement des défenses, point d'entrée.
7. **Détection.** Détection de points d'accès non autorisés (WIPS), inventaire, surveillance des ports, balayage radio.
8. **Prévention.** Contrôle d'accès réseau (802.1X/NAC), détection WIPS, politique stricte, désactivation des ports inutilisés, sensibilisation.
9. ⚠️ **Erreur fréquente.** Ne pas surveiller l'apparition d'AP non autorisés ni verrouiller les ports réseau.
10. 🎯 **À retenir.** Un rogue AP perce un trou sans fil dans le périmètre : NAC et détection WIPS sont les parades.

## Chapitre 153 — Deauthentication

1. **Définition.** Attaque sans fil forçant la déconnexion d'appareils d'un réseau Wi-Fi.
2. **Famille.** Sans fil / disponibilité / préparation MITM.
3. **Principe.** En exploitant des trames de gestion non protégées, l'attaquant envoie des ordres de déconnexion qui éjectent les clients, provoquant un DoS ou les poussant à se reconnecter (vers un evil twin, ou pour capturer la reconnexion).
4. **Sous-types.** Deauth comme DoS, deauth comme déclencheur de reconnexion (vers evil twin/capture).
5. **Exemple conceptuel.** Des trames de déconnexion répétées empêchent les clients de rester connectés, ou les forcent à se reconnecter sur un faux point d'accès.
6. **Impacts.** Déni de service Wi-Fi, facilitation de l'evil twin et de la capture d'authentification.
7. **Détection.** Volume anormal de trames de déconnexion, WIPS, déconnexions répétées.
8. **Prévention.** **Protection des trames de gestion** (802.11w/PMF), WPA3, WIPS, surveillance, réseaux filaires pour le critique.
9. ⚠️ **Erreur fréquente.** Utiliser un Wi-Fi sans protection des trames de gestion (PMF).
10. 🎯 **À retenir.** La deauth abuse de trames non protégées : activer la protection des trames de gestion (802.11w/WPA3) la contre.

## Chapitre 154 — BGP hijacking et route leak

1. **Définition.** Manipulation du routage Internet : détourner (hijack) ou divulguer par erreur (leak) des routes pour rediriger ou intercepter du trafic à grande échelle.
2. **Famille.** Routage / infrastructure Internet / intégrité-disponibilité.
3. **Principe.** BGP, protocole de routage entre opérateurs, repose historiquement sur la confiance ; une annonce illégitime de routes peut détourner du trafic destiné à un réseau vers un autre (interception, blackhole, MITM).
4. **Sous-types.** Hijack (annonce malveillante d'un préfixe), route leak (propagation accidentelle de routes), détournement vers interception ou indisponibilité.
5. **Exemple conceptuel.** Un opérateur annonce à tort être le meilleur chemin vers un réseau, attirant et détournant son trafic.
6. **Impacts.** Interception/détournement de trafic à l'échelle d'Internet, indisponibilité, MITM, atteinte massive.
7. **Détection.** Surveillance des annonces BGP, anomalies de chemins, services de monitoring du routage, alertes.
8. **Prévention.** **RPKI** (validation de l'origine des routes), filtrage des préfixes, bonnes pratiques opérateurs (MANRS), surveillance BGP, relations de peering maîtrisées.
9. ⚠️ **Erreur fréquente.** Absence de validation d'origine (RPKI) et de filtrage de préfixes côté opérateur.
10. 🎯 **À retenir.** Le BGP hijacking détourne le trafic à l'échelle d'Internet ; la validation d'origine (RPKI) et le filtrage des préfixes sont les défenses structurantes.

---

> **Fin du Volume 4/8.**
>
> Vous savez désormais analyser les attaques réseau par intention (reconnaissance, interception, usurpation, rejeu/dégradation, exploitation/déplacement, disponibilité, abus d'infrastructure) et leurs défenses (chiffrement authentifié, protections de commutateur, segmentation, anti-DDoS amont, durcissement sans fil et routage).
>
> **Suite — Volume 5 : Partie 8, Identité, Active Directory et privilèges** (l'identité comme périmètre ; Kerberos/NTLM/LDAP ; tiering ; Kerberoasting, AS-REP roasting, password spraying, pass-the-hash/ticket, overpass-the-hash, golden/silver ticket, DCSync/DCShadow, abus de délégation/RBCD, GPO/ACL abuse, shadow credentials, AD CS abuse, credential dumping, lateral movement Windows, PAM/bastion).


---

# Taxonomie de la cybersécurité — Volume 5/8

> Partie 8 : Identité, Active Directory et privilèges
>
> « L'identité est le nouveau périmètre. » Cette partie est centrale : la majorité des intrusions sérieuses convergent vers la compromission de l'annuaire et des comptes privilégiés. On y décrit les *fondations* (Kerberos, NTLM, LDAP, tiering), puis les grandes familles d'attaques d'identité, toujours côté défensif et conceptuel.
>
> **Posture** : on explique *pourquoi* et *comment se défendre*, sans procédure offensive opérationnelle ni commande exploitable.

---

# Partie 8 — Identité, Active Directory et privilèges

## Vue d'ensemble taxonomique

Les attaques d'identité suivent une logique de progression :

- **Obtenir des identifiants** : deviner (spraying, brute force, stuffing), arracher (kerberoasting, AS-REP roasting), voler en mémoire (credential dumping).
- **Réutiliser sans casser** : pass-the-hash/ticket, overpass-the-hash — l'authentification par « preuve » sans connaître le mot de passe.
- **Forger des accès** : golden/silver ticket, shadow credentials, AD CS abuse — fabriquer ses propres preuves d'identité.
- **Abuser des relations de confiance** : délégation, RBCD, ACL/GPO abuse — exploiter la configuration de l'annuaire.
- **Atteindre le cœur** : DCSync/DCShadow — se faire passer pour un contrôleur de domaine.
- **Se déplacer** : lateral movement Windows vers le contrôle total.

🧭 **Taxonomie** — Ces techniques correspondent aux tactiques ATT&CK *Credential Access, Lateral Movement, Privilege Escalation, Persistence*. La défense de fond : tiering, PAM/bastion, durcissement, surveillance comportementale.

---

## Chapitre 155 — L'identité comme nouveau périmètre

**Définition.** Constat structurant : dans un SI moderne (cloud, SaaS, télétravail), ce n'est plus le réseau qui délimite la confiance, mais l'*identité*. Voler une identité, c'est obtenir ses accès où qu'ils soient.

**Principe.** Le « château fort » périmétrique s'efface : les ressources sont dispersées, accessibles de partout. L'authentification et l'autorisation deviennent le vrai point de contrôle. D'où la centralité de l'IAM, du MFA, du Zero Trust et de la protection de l'annuaire.

🔧 **Exemple concret** — Un identifiant volé par phishing donne accès à la messagerie cloud, au SaaS et au VPN — sans jamais « entrer » physiquement dans un réseau.

🧭 **Taxonomie** — Cadre directeur de toute la partie ; relie AD on-prem, identité cloud (Partie 10) et Zero Trust (chapitre 17).

🎯 **À retenir** — Protéger l'identité est devenu *la* priorité défensive : c'est elle, plus que le réseau, qui détient les clés.

## Chapitre 156 — Annuaire, domaine, forêt, OU, GPO

**Définition.** Les briques structurelles d'Active Directory.

- **Annuaire** : base centralisée des objets (utilisateurs, machines, groupes).
- **Domaine** : unité d'administration et de sécurité regroupant ces objets.
- **Forêt** : ensemble de domaines partageant un schéma et des relations de confiance ; *frontière de sécurité ultime* d'AD.
- **OU (unité d'organisation)** : conteneur pour organiser et déléguer l'administration.
- **GPO (stratégie de groupe)** : mécanisme de configuration/sécurité appliqué massivement aux objets.

**Principe.** Cette structure détermine *qui administre quoi* et *comment les politiques se propagent*. Sa complexité crée des chemins d'attaque souvent invisibles (relations de confiance, délégations, héritage de GPO).

🧭 **Taxonomie** — La **forêt** est la vraie frontière de sécurité : compromettre un domaine peut, via les relations de confiance, menacer toute la forêt.

🎯 **À retenir** — Comprendre la structure AD (forêt > domaine > OU, + GPO) est indispensable : c'est la carte du terrain que l'attaquant cherche à cartographier.

## Chapitre 157 — Kerberos

**Définition.** Protocole d'authentification d'AD fondé sur des *tickets* délivrés par un centre de distribution de clés (KDC, porté par le contrôleur de domaine).

**Principe.** Après authentification, l'utilisateur reçoit un ticket initial (TGT) lui permettant d'obtenir des tickets de service (TGS) pour accéder aux ressources, sans renvoyer son mot de passe. La sécurité repose sur des secrets cryptographiques (dont celui du compte *krbtgt*, clé de voûte du domaine).

🧭 **Taxonomie** — De nombreuses attaques d'identité ciblent Kerberos : kerberoasting (TGS), AS-REP roasting (pré-auth), pass-the-ticket, golden ticket (forge de TGT via krbtgt), silver ticket (forge de TGS).

⚠️ **Erreur fréquente** — Ignorer la sensibilité extrême du compte *krbtgt* : sa compromission permet de forger des accès quasi indétectables (golden ticket).

🎯 **À retenir** — Kerberos évite de transmettre les mots de passe mais introduit des tickets et des secrets (krbtgt) dont l'abus est au cœur des attaques AD.

## Chapitre 158 — NTLM

**Définition.** Protocole d'authentification Windows plus ancien, par défi-réponse, encore présent pour compatibilité.

**Principe.** NTLM authentifie via un condensat (hash) du mot de passe plutôt que le mot de passe en clair. Cette mécanique rend possible la *réutilisation du hash* (pass-the-hash) et le *relais* (NTLM relay), car « prouver qu'on a le hash » suffit.

🧭 **Taxonomie** — Racine du pass-the-hash (chapitre 168) et du NTLM relay (lié à SMB — chapitre 139).

⚠️ **Erreur fréquente** — Laisser NTLM (surtout ses versions anciennes) activé partout « pour compatibilité », au lieu de le restreindre et de privilégier Kerberos.

🎯 **À retenir** — NTLM, par sa mécanique de hash réutilisable, est un facilitateur majeur d'attaques d'identité : le restreindre et activer la signature/EPA est important.

## Chapitre 159 — LDAP

**Définition.** Protocole d'interrogation et de modification de l'annuaire (lecture/écriture des objets AD).

**Principe.** LDAP permet de *lire la structure* (énumération d'utilisateurs, groupes, ACL, délégations) et parfois de *modifier* des objets. C'est l'outil de reconnaissance interne d'AD par excellence, et un vecteur si les écritures sont mal contrôlées.

🧭 **Taxonomie** — Support de l'énumération AD (chapitre 128) et de l'analyse des chemins d'attaque (relations, ACL). Lié à l'injection LDAP côté applicatif (chapitre 101).

🎯 **À retenir** — LDAP est la « vue » de l'annuaire : un attaquant l'utilise pour cartographier les chemins vers les privilèges ; sa surveillance révèle la reconnaissance interne.

## Chapitre 160 — Comptes utilisateurs, machines et services

**Définition.** Les trois grands types de comptes dans AD.

- **Comptes utilisateurs** : personnes physiques.
- **Comptes machines** : ordinateurs joints au domaine (avec leur propre secret).
- **Comptes de service** : identités non humaines exécutant des applications/services, souvent à privilèges élevés et mots de passe rarement changés.

**Principe.** Les comptes de service sont une cible privilégiée : puissants, persistants, parfois avec un SPN exposé (cible du kerberoasting) et des mots de passe faibles/anciens.

🧭 **Taxonomie** — Les comptes de service relient kerberoasting (chapitre 163), permissions excessives (chapitre 76) et persistance.

🎯 **À retenir** — Les comptes de service, puissants et négligés, sont un maillon faible classique : mots de passe forts, gMSA, moindre privilège et rotation.

## Chapitre 161 — Groupes privilégiés

**Définition.** Groupes conférant des droits étendus (administrateurs du domaine, de l'entreprise, opérateurs divers).

**Principe.** L'appartenance à ces groupes est la « clé du royaume ». Les attaquants cherchent à y accéder directement ou *indirectement* (via une chaîne d'ACL/délégations menant à un membre). Leur surveillance et leur minimisation sont prioritaires.

🧭 **Taxonomie** — Cible finale des chemins d'attaque AD ; lié au tiering (chapitre 162) et à l'abus d'ACL (chapitre 178).

⚠️ **Erreur fréquente** — Comptes nominatifs accumulés dans les groupes d'administration, jamais revus (privilege creep).

🎯 **À retenir** — Minimiser et surveiller l'appartenance aux groupes privilégiés est l'un des contrôles AD les plus rentables.

## Chapitre 162 — Tier 0, Tier 1, Tier 2

**Définition.** Modèle de cloisonnement des privilèges d'administration (rappel du chapitre 19, appliqué à AD).

- **Tier 0** : ce qui contrôle l'identité (contrôleurs de domaine, comptes d'admin du domaine, krbtgt, AD CS).
- **Tier 1** : serveurs et applications.
- **Tier 2** : postes de travail.

**Principe.** Étanchéité entre tiers : un identifiant d'un tier ne doit jamais s'exposer sur un tier inférieur. Casser cette règle (un admin du domaine se connectant à un poste) offre à l'attaquant un chemin direct vers le Tier 0.

🧭 **Taxonomie** — Contre-mesure structurante du pass-the-hash, du lateral movement et de l'élévation vers le domaine.

🎯 **À retenir** — Le tiering empêche qu'un poste banal compromis ne mène au contrôle du domaine. C'est l'ossature défensive d'AD.

## Chapitre 163 — Kerberoasting

1. **Définition.** Technique visant à obtenir, puis à casser hors ligne, le secret de *comptes de service* via leurs tickets Kerberos.
2. **Famille.** Credential Access (ATT&CK T1558.003).
3. **Principe.** Tout utilisateur authentifié peut demander un ticket de service pour un compte doté d'un SPN ; ce ticket est chiffré avec une clé dérivée du mot de passe du compte de service. Si ce mot de passe est faible, il peut être retrouvé hors ligne, sans alerter le système.
4. **Sous-types.** Selon l'algorithme de chiffrement et la robustesse du mot de passe ciblé.
5. **Exemple conceptuel.** Un compte de service au mot de passe faible voit son ticket récupéré, puis son secret deviné hors ligne, donnant à l'attaquant ses privilèges.
6. **Impacts.** Compromission de comptes de service (souvent privilégiés), élévation, persistance.
7. **Détection.** Demandes anormales de tickets de service (volume, comptes ciblés), chiffrement faible demandé, surveillance Kerberos.
8. **Prévention.** Mots de passe **longs et aléatoires** pour les comptes de service (idéalement **gMSA** à rotation automatique), moindre privilège, suppression des SPN inutiles, chiffrement fort, surveillance.
9. ⚠️ **Erreur fréquente.** Comptes de service à mot de passe faible et privilèges élevés, jamais changés.
10. 🎯 **À retenir.** Le kerberoasting transforme un compte de service à mot de passe faible en porte d'entrée silencieuse : gMSA et mots de passe forts le neutralisent.

## Chapitre 164 — AS-REP roasting

1. **Définition.** Technique exploitant les comptes dont la *pré-authentification Kerberos est désactivée* pour récupérer un élément cassable hors ligne.
2. **Famille.** Credential Access (ATT&CK T1558.004).
3. **Principe.** Quand la pré-authentification est désactivée pour un compte, on peut obtenir une réponse chiffrée avec une clé dérivée de son mot de passe, puis tenter de retrouver ce dernier hors ligne.
4. **Sous-types.** Selon la robustesse du mot de passe et le compte ciblé.
5. **Exemple conceptuel.** Un compte sans pré-authentification permet de récupérer un matériel chiffré servant à deviner son mot de passe hors ligne.
6. **Impacts.** Compromission de comptes, élévation, persistance.
7. **Détection.** Comptes sans pré-authentification (audit), demandes anormales, surveillance Kerberos.
8. **Prévention.** **Activer la pré-authentification** pour tous les comptes, mots de passe forts, audit régulier de cette propriété, surveillance.
9. ⚠️ **Erreur fréquente.** Laisser des comptes hérités avec pré-authentification désactivée.
10. 🎯 **À retenir.** Désactiver la pré-authentification crée une faiblesse cassable hors ligne : auditer et réactiver la pré-auth partout.

## Chapitre 165 — Password spraying

1. **Définition.** Tester *quelques* mots de passe courants contre *de nombreux* comptes, pour éviter les verrouillages.
2. **Famille.** Credential Access (ATT&CK T1110.003).
3. **Principe.** Au lieu d'essayer beaucoup de mots de passe sur un compte (brute force, qui verrouille), on essaie un mot de passe probable sur tous les comptes, puis on recommence lentement — discret et efficace contre les politiques faibles.
4. **Sous-types.** Spraying lent/distribué, ciblé sur des services exposés (VPN, messagerie cloud, RDP).
5. **Exemple conceptuel.** Un mot de passe saisonnier courant est testé une fois sur l'ensemble des comptes de l'organisation.
6. **Impacts.** Compromission de comptes faibles, accès initial, point de départ d'une intrusion.
7. **Détection.** Nombreux comptes avec un échec quasi simultané, schémas distribués, pics d'authentification, surveillance.
8. **Prévention.** **MFA** (parade principale), mots de passe robustes/bannissement des mots de passe courants, détection de spraying, verrouillage intelligent, surveillance des services exposés.
9. ⚠️ **Erreur fréquente.** Se fier au seul verrouillage de compte (contourné par le spraying) sans MFA ni détection.
10. 🎯 **À retenir.** Le spraying contourne les verrouillages classiques ; le MFA et la détection des schémas distribués sont les vraies parades.

## Chapitre 166 — Brute force

1. **Définition.** Essayer systématiquement de nombreuses combinaisons pour deviner un secret (mot de passe, clé, PIN).
2. **Famille.** Credential Access (ATT&CK T1110).
3. **Principe.** Par essais répétés (en ligne ou hors ligne sur des condensats volés), on finit par trouver un secret faible. La robustesse du secret et la limitation des essais déterminent la faisabilité.
4. **Sous-types.** Brute force en ligne (contre un service), hors ligne (sur des hash volés), par dictionnaire, ciblé.
5. **Exemple conceptuel.** Un service sans limitation d'essais permet de tester un très grand nombre de mots de passe jusqu'à succès.
6. **Impacts.** Compromission de comptes, accès non autorisé.
7. **Détection.** Pics d'échecs d'authentification, essais répétés, surveillance, alertes de verrouillage.
8. **Prévention.** **Limitation/verrouillage**, MFA, mots de passe forts, hachage lent et salé (contre le hors ligne), CAPTCHA ciblé, surveillance.
9. ⚠️ **Erreur fréquente.** Hacher les mots de passe avec un algorithme rapide (facilite le brute force hors ligne) au lieu d'un algorithme lent dédié.
10. 🎯 **À retenir.** Le brute force réussit contre les secrets faibles et les services non limités : robustesse + limitation + MFA + hachage lent.

## Chapitre 167 — Credential stuffing

1. **Définition.** Réutiliser des identifiants volés ailleurs (fuites) pour se connecter, en pariant sur la *réutilisation de mots de passe*.
2. **Famille.** Credential Access (ATT&CK T1110.004).
3. **Principe.** D'immenses listes d'identifiants issus de fuites sont testées automatiquement ; les utilisateurs réutilisant leurs mots de passe sont compromis sans aucun « cassage ».
4. **Sous-types.** Stuffing distribué, ciblé sur des services grand public, combiné à la rotation d'IP (contre la limitation).
5. **Exemple conceptuel.** Des couples identifiant/mot de passe d'une fuite tierce sont essayés massivement contre un service.
6. **Impacts.** Prise de comptes en masse, fraude, accès initial.
7. **Détection.** Pics de connexions avec taux d'échec élevé, sources distribuées, identifiants connus comme compromis, surveillance.
8. **Prévention.** **MFA**, détection des identifiants compromis (bannissement), limitation, unicité des mots de passe (gestionnaires), surveillance comportementale.
9. ⚠️ **Erreur fréquente.** Compter sur la « complexité » des mots de passe alors que le problème est leur *réutilisation*.
10. 🎯 **À retenir.** Le stuffing exploite la réutilisation : MFA et détection des identifiants déjà fuités sont déterminants.

## Chapitre 168 — Pass-the-hash

1. **Définition.** S'authentifier en réutilisant le *condensat (hash)* du mot de passe, sans connaître le mot de passe en clair.
2. **Famille.** Lateral Movement / Credential Access (ATT&CK T1550.002).
3. **Principe.** Avec NTLM (chapitre 158), prouver qu'on détient le hash suffit. Un hash volé en mémoire sur une machine permet de s'authentifier ailleurs comme l'utilisateur, sans cassage.
4. **Sous-types.** Selon le compte et la portée (local vs domaine).
5. **Exemple conceptuel.** Un hash récupéré sur un poste est réutilisé pour s'authentifier sur d'autres machines acceptant NTLM.
6. **Impacts.** Mouvement latéral, élévation si le hash est privilégié, propagation.
7. **Détection.** Authentifications NTLM anormales, usage d'un même compte sur de nombreuses machines, EDR, surveillance.
8. **Prévention.** **Tiering** (ne pas exposer de hash privilégiés sur des machines basses), **LAPS** (mots de passe locaux uniques), restriction de NTLM, protection des secrets (Credential Guard), moindre privilège, détection.
9. ⚠️ **Erreur fréquente.** Mots de passe d'administrateur local identiques partout : un hash volé ouvre tout le parc.
10. 🎯 **À retenir.** Pass-the-hash réutilise une preuve sans casser le secret : tiering, LAPS et protection mémoire des secrets sont les parades clés.

## Chapitre 169 — Pass-the-ticket

1. **Définition.** Réutiliser un *ticket Kerberos* volé pour accéder à des ressources sans connaître le mot de passe.
2. **Famille.** Lateral Movement / Credential Access (ATT&CK T1550.003).
3. **Principe.** Un ticket Kerberos (TGT ou TGS) extrait de la mémoire d'une machine peut être réinjecté pour se faire passer pour l'utilisateur jusqu'à son expiration.
4. **Sous-types.** Réutilisation de TGT (accès large) ou de TGS (accès à un service précis).
5. **Exemple conceptuel.** Un ticket récupéré en mémoire est réutilisé pour accéder aux ressources du titulaire.
6. **Impacts.** Mouvement latéral, accès aux ressources, élévation selon le ticket.
7. **Détection.** Usage de tickets depuis des emplacements anormaux, anomalies Kerberos, EDR.
8. **Prévention.** Protection des secrets en mémoire (Credential Guard), tiering, durée de vie des tickets maîtrisée, moindre privilège, détection comportementale.
9. ⚠️ **Erreur fréquente.** Négliger la protection de la mémoire des contrôleurs/serveurs où des tickets précieux résident.
10. 🎯 **À retenir.** Pass-the-ticket réutilise des tickets volés : protéger la mémoire et appliquer le tiering limite le vol et la portée.

## Chapitre 170 — Overpass-the-hash

1. **Définition.** Utiliser un hash NTLM pour obtenir un *ticket Kerberos* légitime, combinant les deux mondes (aussi appelé « pass-the-key »).
2. **Famille.** Credential Access / Lateral Movement (ATT&CK T1550).
3. **Principe.** À partir d'un hash volé, l'attaquant demande un TGT Kerberos valide, obtenant ainsi une authentification Kerberos « propre » sans le mot de passe en clair — plus discret que le NTLM pur.
4. **Sous-types.** Selon la clé utilisée et la portée obtenue.
5. **Exemple conceptuel.** Un hash sert à obtenir un ticket Kerberos, utilisé ensuite comme une authentification normale.
6. **Impacts.** Mouvement latéral plus furtif, accès aux ressources Kerberos.
7. **Détection.** Incohérences entre type d'authentification et contexte, anomalies Kerberos, EDR.
8. **Prévention.** Identiques au pass-the-hash/ticket : tiering, protection mémoire (Credential Guard), LAPS, restriction NTLM, détection.
9. ⚠️ **Erreur fréquente.** Croire que « passer à Kerberos » suffit si les hash restent volables en mémoire.
10. 🎯 **À retenir.** Overpass-the-hash transforme un hash en ticket Kerberos : la protection des secrets en mémoire et le tiering restent les parades.

## Chapitre 171 — Golden ticket

1. **Définition.** Forge d'un *TGT arbitraire* à partir du secret du compte *krbtgt*, donnant un accès quasi total et persistant au domaine.
2. **Famille.** Persistence / Privilege Escalation (ATT&CK T1558.001).
3. **Principe.** Le compte krbtgt signe les TGT ; quiconque détient son secret peut forger des tickets pour n'importe quel utilisateur (y compris administrateur), valides et difficiles à révoquer sans réinitialiser krbtgt (deux fois).
4. **Sous-types.** Selon la portée et la durée forgées.
5. **Exemple conceptuel.** Avec le secret krbtgt, l'attaquant fabrique un ticket d'administrateur du domaine valide longtemps.
6. **Impacts.** Contrôle total et persistant du domaine, persistance majeure, très difficile à éradiquer.
7. **Détection.** Tickets aux propriétés anormales (durées, chiffrement), incohérences, surveillance avancée.
8. **Prévention.** **Protéger krbtgt absolument** (Tier 0), rotation (double) de krbtgt en cas de suspicion, durcissement et surveillance des contrôleurs, limiter l'accès au Tier 0.
9. ⚠️ **Erreur fréquente.** Sous-estimer la criticité de krbtgt et ne jamais prévoir sa rotation après incident.
10. 🎯 **À retenir.** Le golden ticket signifie un domaine entièrement compromis et persistant : la protection de krbtgt et sa rotation post-incident sont vitales.

## Chapitre 172 — Silver ticket

1. **Définition.** Forge d'un *ticket de service (TGS)* pour un service précis, à partir du secret de ce service, sans passer par le KDC.
2. **Famille.** Persistence / Lateral Movement (ATT&CK T1558.002).
3. **Principe.** Plus ciblé que le golden ticket : avec le secret d'un compte de service, l'attaquant forge des accès à *ce* service, plus furtivement (le contrôleur n'est pas sollicité).
4. **Sous-types.** Selon le service ciblé.
5. **Exemple conceptuel.** Le secret d'un service permet de forger un accès direct à ce service, sans interaction avec le contrôleur de domaine.
6. **Impacts.** Accès persistant et furtif à un service, mouvement latéral ciblé.
7. **Détection.** Plus difficile (pas de trace côté KDC) ; surveillance des accès de service incohérents, anomalies.
8. **Prévention.** Mots de passe forts/gMSA pour les comptes de service, rotation, moindre privilège, surveillance des services, durcissement.
9. ⚠️ **Erreur fréquente.** Comptes de service à secret faible/statique, permettant la forge silencieuse de tickets.
10. 🎯 **À retenir.** Le silver ticket forge des accès furtifs à un service : protéger et faire tourner les secrets de service (gMSA) est la parade.

## Chapitre 173 — DCSync

1. **Définition.** Abus consistant à se faire passer pour un contrôleur de domaine afin de *demander la réplication* des secrets de l'annuaire (dont les condensats des comptes).
2. **Famille.** Credential Access (ATT&CK T1003.006).
3. **Principe.** Un compte disposant de droits de réplication peut demander à un contrôleur de lui « répliquer » des secrets, comme le ferait un autre contrôleur — extrayant ainsi des hash sensibles (y compris krbtgt).
4. **Sous-types.** Selon les comptes/secrets ciblés.
5. **Exemple conceptuel.** Un compte aux droits de réplication récupère les condensats de comptes privilégiés via le mécanisme de réplication.
6. **Impacts.** Vol des secrets du domaine, préparation de golden ticket, compromission totale.
7. **Détection.** Demandes de réplication provenant d'hôtes non-contrôleurs, surveillance des droits de réplication et des événements associés.
8. **Prévention.** **Restreindre strictement les droits de réplication** (Tier 0), surveiller leur attribution, durcissement des contrôleurs, détection des réplications anormales.
9. ⚠️ **Erreur fréquente.** Droits de réplication accordés trop largement ou non surveillés.
10. 🎯 **À retenir.** DCSync extrait les secrets du domaine en imitant un contrôleur : verrouiller et surveiller les droits de réplication est essentiel.

## Chapitre 174 — DCShadow

1. **Définition.** Abus enregistrant un *faux contrôleur de domaine* pour injecter des modifications dans l'annuaire de façon furtive.
2. **Famille.** Persistence / Defense Evasion (ATT&CK T1207).
3. **Principe.** En se faisant passer pour un contrôleur légitime, l'attaquant pousse des modifications (ajout de droits, portes dérobées) via la réplication, contournant une partie de la journalisation classique.
4. **Sous-types.** Selon les modifications injectées (persistance, élévation).
5. **Exemple conceptuel.** Une modification malveillante de l'annuaire est introduite via un mécanisme de réplication, en imitant un contrôleur.
6. **Impacts.** Persistance furtive, élévation, altération de l'annuaire difficile à repérer.
7. **Détection.** Apparition d'objets contrôleurs inattendus, réplications anormales, surveillance avancée d'AD.
8. **Prévention.** Restreindre qui peut enregistrer/agir comme contrôleur (Tier 0), surveillance fine de la réplication et du schéma, durcissement, détection spécialisée.
9. ⚠️ **Erreur fréquente.** Ne surveiller que les journaux classiques, que DCShadow contourne partiellement.
10. 🎯 **À retenir.** DCShadow injecte des changements en imitant un contrôleur : seule une surveillance avancée de la réplication le détecte.

## Chapitre 175 — Delegation abuse (délégation Kerberos)

1. **Définition.** Abus des mécanismes de *délégation Kerberos*, qui permettent à un service d'agir au nom d'un utilisateur.
2. **Famille.** Privilege Escalation / Lateral Movement.
3. **Principe.** La délégation autorise un service à réutiliser l'identité d'un utilisateur pour accéder à d'autres ressources. Mal configurée (surtout la délégation *non contrainte*), elle permet à un attaquant contrôlant ce service d'usurper des utilisateurs privilégiés.
4. **Sous-types.** Délégation non contrainte (la plus dangereuse), contrainte, et RBCD (chapitre 176).
5. **Exemple conceptuel.** Un service avec délégation non contrainte capte des tickets d'utilisateurs privilégiés s'y connectant, permettant leur usurpation.
6. **Impacts.** Usurpation d'identités privilégiées, élévation, mouvement latéral.
7. **Détection.** Audit des configurations de délégation, comptes à délégation non contrainte, anomalies Kerberos.
8. **Prévention.** **Supprimer la délégation non contrainte**, préférer la délégation contrainte/RBCD maîtrisée, marquer les comptes sensibles comme non délégables, audit régulier, Tier 0.
9. ⚠️ **Erreur fréquente.** Laisser des serveurs en délégation non contrainte (configuration historique très risquée).
10. 🎯 **À retenir.** La délégation non contrainte est une bombe à retardement : l'éliminer et protéger les comptes sensibles de la délégation est prioritaire.

## Chapitre 176 — RBCD (Resource-Based Constrained Delegation abuse)

1. **Définition.** Abus de la *délégation contrainte basée sur les ressources*, où la configuration de délégation est portée par l'objet ressource.
2. **Famille.** Privilege Escalation / Lateral Movement.
3. **Principe.** Si un attaquant peut modifier l'attribut de délégation d'un objet (via un droit d'écriture mal maîtrisé), il peut se configurer pour usurper des utilisateurs sur cette ressource, élevant ses privilèges.
4. **Sous-types.** Selon l'objet et les droits d'écriture exploités.
5. **Exemple conceptuel.** Un droit d'écriture sur un objet machine est exploité pour configurer une délégation autorisant l'usurpation d'un compte privilégié sur cette machine.
6. **Impacts.** Élévation de privilèges, usurpation, prise de contrôle de ressources.
7. **Détection.** Modifications anormales des attributs de délégation, surveillance des ACL et des écritures sur objets, anomalies Kerberos.
8. **Prévention.** Contrôler strictement les **droits d'écriture** sur les objets (ACL), surveiller les attributs de délégation, durcissement, moindre privilège, Tier 0.
9. ⚠️ **Erreur fréquente.** Droits d'écriture sur des objets machine/compte accordés trop largement.
10. 🎯 **À retenir.** RBCD transforme un droit d'écriture mal placé en élévation : la maîtrise des ACL et la surveillance des attributs de délégation sont clés.

## Chapitre 177 — GPO abuse

1. **Définition.** Abus des *stratégies de groupe* (GPO) pour déployer des configurations/actions malveillantes à grande échelle.
2. **Famille.** Privilege Escalation / Lateral Movement / Persistence.
3. **Principe.** Les GPO s'appliquent massivement aux objets liés. Un attaquant pouvant *modifier* une GPO (ou la lier à une OU) peut pousser des actions malveillantes (tâches, scripts, paramètres) sur de nombreuses machines/utilisateurs.
4. **Sous-types.** Modification de GPO existante, liaison d'une GPO à une OU, abus de droits sur les GPO.
5. **Exemple conceptuel.** Une GPO modifiable est détournée pour déployer une configuration affaiblissant la sécurité sur tout un périmètre.
6. **Impacts.** Compromission massive, élévation, persistance, désactivation de défenses.
7. **Détection.** Modifications de GPO inattendues, changements de liaison, surveillance des droits sur les GPO et des journaux.
8. **Prévention.** Restreindre et **surveiller les droits de modification des GPO**, contrôle de version/validation des changements, moindre privilège, Tier 0, audit.
9. ⚠️ **Erreur fréquente.** Droits de modification de GPO accordés trop largement, sans surveillance.
10. 🎯 **À retenir.** Une GPO est un levier de déploiement de masse : qui peut la modifier peut compromettre largement. Restreindre et surveiller ces droits.

## Chapitre 178 — ACL abuse

1. **Définition.** Exploitation de *droits d'accès mal configurés* sur les objets de l'annuaire pour élever ses privilèges via des chaînes de permissions.
2. **Famille.** Privilege Escalation (cœur des « chemins d'attaque » AD).
3. **Principe.** AD est un graphe de permissions ; certains droits (réinitialiser un mot de passe, modifier l'appartenance d'un groupe, écrire un attribut) permettent de prendre le contrôle d'autres objets. En enchaînant ces droits, un attaquant trace un *chemin* d'un compte peu privilégié vers l'administration du domaine.
4. **Sous-types.** Droits de réinitialisation de mot de passe, d'écriture d'appartenance de groupe, de propriété d'objet, d'écriture d'attributs sensibles.
5. **Exemple conceptuel.** Un compte a le droit de modifier l'appartenance d'un groupe qui, lui-même, mène par étapes à un groupe privilégié — l'attaquant remonte la chaîne.
6. **Impacts.** Élévation jusqu'au contrôle du domaine, souvent par des chemins invisibles à l'œil nu.
7. **Détection.** Analyse des chemins d'attaque (graphes d'ACL), modifications anormales d'appartenance/d'attributs, surveillance.
8. **Prévention.** **Audit et nettoyage des ACL**, cartographie des chemins d'attaque (outils de graphe), moindre privilège, Tier 0, surveillance des modifications sensibles.
9. ⚠️ **Erreur fréquente.** Délégations d'administration historiques jamais revues, créant des chemins d'élévation cachés.
10. 🎯 **À retenir.** AD est un graphe de droits : l'abus d'ACL relie un compte banal à l'admin du domaine. Cartographier et nettoyer ces chemins est une défense majeure.

## Chapitre 179 — Shadow credentials

1. **Définition.** Technique ajoutant des *informations d'authentification alternatives* (par clé/certificat) à un compte pour s'authentifier comme lui.
2. **Famille.** Credential Access / Persistence.
3. **Principe.** En écrivant sur un attribut d'authentification d'un compte (via un droit mal maîtrisé), l'attaquant y associe une clé qu'il contrôle, lui permettant ensuite de s'authentifier comme ce compte sans son mot de passe.
4. **Sous-types.** Selon le droit d'écriture exploité et le compte ciblé.
5. **Exemple conceptuel.** Une information d'authentification alternative est ajoutée à un compte privilégié, donnant un accès durable à l'attaquant.
6. **Impacts.** Usurpation et persistance, élévation, contournement du changement de mot de passe.
7. **Détection.** Modifications de l'attribut d'authentification, surveillance des écritures sensibles, anomalies.
8. **Prévention.** Restreindre les **droits d'écriture** sur les attributs d'authentification, surveiller ces modifications, durcissement de l'infrastructure de certificats, Tier 0.
9. ⚠️ **Erreur fréquente.** Ne pas surveiller les écritures sur les attributs liés à l'authentification par clé.
10. 🎯 **À retenir.** Les shadow credentials ajoutent une clé d'accès cachée à un compte : surveiller les écritures sur les attributs d'authentification est la parade.

## Chapitre 180 — AD CS abuse

1. **Définition.** Abus des *services de certificats d'Active Directory* (PKI interne) pour obtenir des certificats permettant l'usurpation ou l'élévation.
2. **Famille.** Privilege Escalation / Persistence / Credential Access.
3. **Principe.** Une autorité de certification interne mal configurée (modèles de certificats trop permissifs, droits d'inscription larges) peut être amenée à délivrer des certificats permettant de s'authentifier comme un autre utilisateur, y compris privilégié.
4. **Sous-types.** Modèles de certificats vulnérables, droits d'inscription/gestion abusés, persistance via certificats à longue durée.
5. **Exemple conceptuel.** Un modèle de certificat permissif permet d'obtenir un certificat au nom d'un compte privilégié, utilisé ensuite pour s'authentifier comme lui.
6. **Impacts.** Élévation jusqu'au domaine, persistance durable (certificats peu révoqués), usurpation.
7. **Détection.** Inscriptions de certificats anormales, audit des modèles et des droits, surveillance de la CA.
8. **Prévention.** **Durcir les modèles de certificats** et les droits d'inscription, traiter l'AD CS comme du **Tier 0**, audit régulier, surveillance, révocation/rotation.
9. ⚠️ **Erreur fréquente.** Modèles de certificats permissifs et CA non considérée comme un actif Tier 0.
10. 🎯 **À retenir.** L'AD CS mal configuré offre des chemins d'élévation et de persistance puissants : durcir les modèles et protéger la CA comme un joyau (Tier 0).

## Chapitre 181 — Credential dumping

1. **Définition.** Extraction d'identifiants (hash, tickets, mots de passe en mémoire, secrets stockés) depuis un système compromis.
2. **Famille.** Credential Access (ATT&CK T1003) — alimente la plupart des techniques précédentes.
3. **Principe.** Sur une machine contrôlée, l'attaquant récupère les secrets présents en mémoire, dans les bases de comptes locales, ou dans des stockages applicatifs, pour alimenter pass-the-hash/ticket, lateral movement et élévation.
4. **Sous-types.** Extraction mémoire de secrets, extraction de la base de comptes locale, vol de tickets, secrets d'applications/navigateurs.
5. **Exemple conceptuel.** Sur un poste compromis, des secrets résidant en mémoire sont récupérés pour rebondir vers d'autres systèmes.
6. **Impacts.** Carburant du mouvement latéral et de l'élévation ; souvent l'étape pivot d'une intrusion.
7. **Détection.** Accès anormaux aux processus/mémoire sensibles, alertes EDR, comportements de collecte d'identifiants.
8. **Prévention.** **Protection des secrets en mémoire** (Credential Guard), EDR, moindre privilège (pas d'admin local), tiering (limiter les secrets exposés), LAPS, durcissement, surveillance.
9. ⚠️ **Erreur fréquente.** Laisser des secrets privilégiés résider sur des machines peu protégées (violation du tiering).
10. 🎯 **À retenir.** Le credential dumping alimente presque toutes les attaques AD : protéger la mémoire, appliquer le tiering et l'EDR coupe le carburant.

## Chapitre 182 — Lateral movement en environnement Windows

1. **Définition.** Application concrète du mouvement latéral (chapitre 144) dans un parc Windows/AD, combinant les techniques précédentes.
2. **Famille.** Lateral Movement (ATT&CK).
3. **Principe.** Après l'accès initial, l'attaquant enchaîne credential dumping → réutilisation (pass-the-hash/ticket) → abus de services d'administration (SMB/RDP/WinRM) → progression vers le Tier 0, jusqu'au contrôle du domaine.
4. **Sous-types.** Via partages/SMB, via RDP, via exécution distante (WinRM/tâches), via outils d'administration légitimes (living-off-the-land).
5. **Exemple conceptuel.** Des identifiants récupérés sur un poste permettent d'atteindre un serveur, d'y récupérer d'autres secrets, puis de viser un contrôleur de domaine.
6. **Impacts.** Compromission progressive jusqu'au domaine, préalable au ransomware et à l'exfiltration.
7. **Détection.** Connexions inter-machines anormales, usage atypique de comptes d'administration et d'outils légitimes, corrélation SIEM, EDR/NDR.
8. **Prévention.** **Tiering**, segmentation, LAPS, moindre privilège, MFA pour l'administration, bastion/PAM, durcissement, détection comportementale.
9. ⚠️ **Erreur fréquente.** Réutilisation de comptes d'administration sur tous les tiers, mots de passe locaux identiques, absence de segmentation.
10. 🎯 **À retenir.** Le lateral movement Windows est la « colonne vertébrale » des intrusions AD : tiering + LAPS + segmentation + détection le rendent lent et bruyant.

## Chapitre 183 — PAM, bastion et modèle tiering (synthèse défensive AD)

**Définition.** Récapitulatif des défenses structurantes de l'identité : gestion des accès privilégiés (PAM), bastion d'administration, et tiering.

**Principe.** Ces trois éléments, combinés, brisent les chemins d'attaque AD :
- le **tiering** empêche l'exposition de secrets privilégiés sur des machines peu fiables ;
- le **bastion** canalise et journalise tous les accès d'administration via un point durci ;
- le **PAM** supprime les secrets permanents (coffre-fort, accès just-in-time, rotation, enregistrement de session).

À cela s'ajoutent LAPS (mots de passe locaux uniques), MFA pour l'administration, Credential Guard (protection mémoire), audit des ACL/délégations/GPO, et surveillance comportementale.

🧭 **Taxonomie** — Ce chapitre relie toutes les attaques de la Partie 8 à leur antidote commun : casser la *réutilisation* et l'*exposition* des secrets privilégiés.

⚠️ **Erreur fréquente** — Déployer des outils PAM tout en laissant subsister des accès directs « de secours » non contrôlés qui contournent le dispositif.

🎯 **À retenir** — La défense de l'identité tient en une idée : *empêcher l'exposition et la réutilisation des secrets privilégiés*. Tiering + bastion + PAM + LAPS + MFA + surveillance forment le socle.

---

> **Fin du Volume 5/8.**
>
> Vous disposez d'une taxonomie des attaques d'identité (obtenir → réutiliser → forger → abuser des relations → atteindre le cœur → se déplacer) et de leur antidote commun (tiering, PAM/bastion, LAPS, protection mémoire, audit des ACL/délégations/GPO, surveillance).
>
> **Suite — Volume 6 : Partie 9, Malware, phishing et attaques client-side** (classification des malwares : virus, ver, trojan, ransomware, wiper, spyware, infostealer, RAT, backdoor, loader/dropper/downloader, rootkit/bootkit, fileless, macro, LOLBins ; et l'ingénierie sociale : phishing, spear phishing, whaling, smishing, vishing, quishing, BEC, malspam, drive-by, malvertising, SEO poisoning, watering hole, MFA fatigue, consent phishing).


---

# Taxonomie de la cybersécurité — Volume 6/8

> Partie 9 : Malware, phishing et attaques client-side
>
> Cette partie classe deux grandes familles : les **logiciels malveillants** (par fonction et par comportement) et l'**ingénierie sociale** (par canal et par cible). Le point commun : l'humain et le poste (chapitres 40, 59) sont les portes d'entrée. Format en 10 points pour les attaques majeures, format compact pour les variantes.
>
> **Posture** : on décrit la *fonction*, les *impacts*, la *détection* et la *défense* — jamais comment créer un malware ni conduire une campagne offensive.

---

# Partie 9 — Malware, phishing et attaques client-side

## Chapitre 184 — Malware : classification générale

**Définition.** Un *malware* (logiciel malveillant) est un programme conçu pour nuire : voler, chiffrer, espionner, détruire, ou donner le contrôle à un attaquant.

**Deux axes de classification complémentaires.**
- **Par propagation/forme** : virus (s'attache à un hôte), ver (se propage seul), trojan (se déguise).
- **Par fonction/charge utile (payload)** : ransomware (chiffre), spyware/infostealer (espionne/vole), RAT/backdoor (contrôle), wiper (détruit), etc.

Un même malware combine souvent plusieurs catégories (par ex. un ver portant un ransomware). Beaucoup s'organisent en *chaîne* : un loader installe un dropper qui télécharge la charge finale.

🧭 **Taxonomie** — Distinguer *comment il se répand* (forme) de *ce qu'il fait* (fonction) évite la confusion. Les chapitres suivants déclinent ces deux axes.

🎯 **À retenir** — Classer un malware = répondre à deux questions : *comment se propage-t-il ?* et *quelle est sa charge utile ?*

## Chapitre 185 — Virus

1. **Définition.** Code malveillant qui s'attache à un fichier/programme *hôte* et se réplique quand celui-ci est exécuté.
2. **Famille.** Malware par forme (réplication via hôte).
3. **Principe.** Le virus a besoin d'une action (exécuter le fichier infecté) pour se propager ; il insère son code dans d'autres fichiers.
4. **Sous-types.** Virus de fichier, de secteur d'amorçage, de macro (chapitre 200), polymorphes/métamorphes (mutent pour échapper à la détection).
5. **Exemple conceptuel.** Un exécutable infecté propage le virus à d'autres programmes à chaque lancement.
6. **Impacts.** Corruption/altération, propagation, support d'autres charges.
7. **Détection.** Antivirus/EDR (signatures + comportement), intégrité de fichiers, anomalies.
8. **Prévention.** Antivirus/EDR, application allowlisting, mises à jour, méfiance envers les fichiers non fiables, durcissement.
9. ⚠️ **Erreur fréquente.** Confondre virus (besoin d'un hôte et d'une action) et ver (autonome).
10. 🎯 **À retenir.** Le virus a besoin d'un hôte et d'une exécution pour se répliquer — c'est ce qui le distingue du ver.

## Chapitre 186 — Ver (worm)

1. **Définition.** Malware *autonome* qui se propage seul de machine en machine, sans hôte ni action humaine.
2. **Famille.** Malware par forme (auto-propagation).
3. **Principe.** Le ver exploite des vulnérabilités réseau ou des partages pour se répliquer automatiquement, parfois à très grande vitesse et à grande échelle.
4. **Sous-types.** Vers réseau (exploitation de service), vers de messagerie, vers portant un ransomware.
5. **Exemple conceptuel.** Un ver exploite une vulnérabilité d'un service réseau pour se copier sur les machines vulnérables, qui infectent à leur tour.
6. **Impacts.** Propagation explosive, saturation, support de charges destructrices (ransomware), indisponibilité.
7. **Détection.** Pics de trafic de propagation, connexions anormales en chaîne, EDR/NDR, signatures.
8. **Prévention.** **Patch** (les vers exploitent des vulnérabilités connues), segmentation, désactivation des protocoles vulnérables, EDR, surveillance.
9. ⚠️ **Erreur fréquente.** Retarder les patchs de services exploitables par des vers (propagation massive possible).
10. 🎯 **À retenir.** Le ver se propage seul en exploitant des failles : patcher et segmenter freine sa diffusion.

## Chapitre 187 — Trojan (cheval de Troie)

1. **Définition.** Malware *déguisé* en logiciel légitime pour tromper l'utilisateur qui l'installe.
2. **Famille.** Malware par forme (tromperie).
3. **Principe.** Le trojan ne se réplique pas forcément ; il mise sur l'apparence (faux utilitaire, fausse mise à jour) pour être exécuté volontairement, puis délivre sa charge.
4. **Sous-types.** Trojan d'accès distant (RAT — chapitre 192), bancaire, dropper/loader (chapitres 195–194), faux logiciels.
5. **Exemple conceptuel.** Un programme présenté comme un outil utile installe en réalité une charge malveillante à l'insu de l'utilisateur.
6. **Impacts.** Variés selon la charge : vol, contrôle, espionnage, porte dérobée.
7. **Détection.** Antivirus/EDR, réputation des fichiers/sources, comportements post-exécution anormaux.
8. **Prévention.** Sources logicielles de confiance, allowlisting, sensibilisation, EDR, vérification d'intégrité/signatures.
9. ⚠️ **Erreur fréquente.** Installer des logiciels depuis des sources non fiables (« crack », faux installeurs).
10. 🎯 **À retenir.** Le trojan se fait installer par ruse : la confiance dans la source et l'allowlisting sont les défenses clés.

## Chapitre 188 — Ransomware

1. **Définition.** Malware qui *chiffre* les données (et/ou les *exfiltre*) pour exiger une rançon.
2. **Famille.** Malware par fonction (atteinte à la disponibilité, parfois confidentialité). Impact ATT&CK.
3. **Principe.** Après accès initial et souvent mouvement latéral, le ransomware chiffre les fichiers/systèmes ; les variantes modernes pratiquent la *double extorsion* (exfiltration + menace de publication) voire triple (DDoS, pression sur les tiers).
4. **Sous-types.** Chiffrement simple, double/triple extorsion, ransomware-as-a-service (RaaS), ransomware porté par un ver.
5. **Exemple conceptuel.** Après s'être propagé, le ransomware chiffre les serveurs de fichiers et laisse une demande de rançon, tout en menaçant de publier les données volées.
6. **Impacts.** Indisponibilité majeure (arrêt d'activité), fuite de données, coûts, réputation — l'une des menaces les plus graves pour les organisations.
7. **Détection.** Chiffrement massif de fichiers, suppression de sauvegardes/clichés, comportements de propagation, exfiltration, EDR/SIEM.
8. **Prévention.** **Sauvegardes immuables et testées** (chapitre 28, parade de fond), segmentation, MFA, patch, EDR, moindre privilège, tiering, plan de réponse/PRA, sensibilisation.
9. ⚠️ **Erreur fréquente.** Sauvegardes accessibles en ligne (chiffrées avec la production) ou jamais testées ; absence de plan de crise.
10. 🎯 **À retenir.** Le ransomware vise la disponibilité et exfiltre : seules des sauvegardes immuables/testées et une défense en profondeur (segmentation, MFA, EDR) protègent réellement.

## Chapitre 189 — Wiper

1. **Définition.** Malware destructeur dont le but est d'*effacer/rendre inutilisables* les données, sans rançon.
2. **Famille.** Malware par fonction (destruction — Impact).
3. **Principe.** Contrairement au ransomware, le wiper ne cherche pas l'argent mais le *sabotage* ; il détruit données ou systèmes (parfois en se déguisant en ransomware).
4. **Sous-types.** Effacement de données, corruption du système d'amorçage, sabotage ciblé.
5. **Exemple conceptuel.** Un malware détruit irrémédiablement les données et l'amorçage des machines visées.
6. **Impacts.** Destruction irréversible, indisponibilité durable, sabotage (souvent géopolitique).
7. **Détection.** Effacements/corruptions massifs, comportements destructeurs, EDR.
8. **Prévention.** Sauvegardes hors-ligne/immuables, segmentation, EDR, durcissement, détection précoce, plan de continuité.
9. ⚠️ **Erreur fréquente.** Supposer qu'un incident de type « ransomware » est toujours récupérable contre rançon : un wiper déguisé ne l'est pas.
10. 🎯 **À retenir.** Le wiper détruit sans rançon : seules des sauvegardes hors-ligne et la continuité permettent de s'en relever.

## Chapitre 190 — Spyware

1. **Définition.** Malware d'*espionnage* qui collecte discrètement des informations sur l'utilisateur/le système.
2. **Famille.** Malware par fonction (atteinte à la confidentialité).
3. **Principe.** Le spyware surveille l'activité (frappe clavier, écran, navigation) et transmet les données à l'attaquant, souvent furtivement et durablement.
4. **Sous-types.** Keyloggers, capture d'écran, espionnage mobile (stalkerware), surveillance avancée.
5. **Exemple conceptuel.** Un programme caché enregistre l'activité de l'utilisateur et l'envoie à un tiers.
6. **Impacts.** Vol d'informations, surveillance, atteinte à la vie privée, préparation d'autres attaques.
7. **Détection.** Comportements de collecte/exfiltration, EDR, anomalies réseau.
8. **Prévention.** EDR/antivirus, durcissement, contrôle des applications, mises à jour, sensibilisation, MFA (limite l'impact des secrets volés).
9. ⚠️ **Erreur fréquente.** Négliger le spyware mobile (stalkerware), pourtant répandu.
10. 🎯 **À retenir.** Le spyware espionne en silence : détection comportementale, hygiène applicative et MFA réduisent son impact.

## Chapitre 191 — Infostealer

1. **Définition.** Malware spécialisé dans le *vol rapide d'identifiants et de secrets* (mots de passe enregistrés, cookies/jetons de session, portefeuilles).
2. **Famille.** Malware par fonction (credential access).
3. **Principe.** L'infostealer ratisse le poste pour récupérer un maximum de secrets en une fois, souvent revendus ensuite ; le vol de *jetons de session* permet de contourner le MFA.
4. **Sous-types.** Vol de mots de passe de navigateurs, de cookies/sessions, de portefeuilles crypto, de fichiers sensibles.
5. **Exemple conceptuel.** Un infostealer collecte les identifiants et cookies enregistrés sur un poste et les exfiltre rapidement.
6. **Impacts.** Prise de comptes (y compris malgré le MFA via les jetons), accès initial revendu, fraude.
7. **Détection.** Accès massifs aux stockages de secrets, exfiltration, EDR, connexions ultérieures anormales.
8. **Prévention.** EDR, moindre privilège, protection des secrets, expiration/réévaluation des sessions, MFA résistant au phishing, détection des connexions par jeton volé, sensibilisation.
9. ⚠️ **Erreur fréquente.** Croire le MFA infaillible : le vol de *jeton de session* le contourne. D'où l'importance de la gestion des sessions et de la détection.
10. 🎯 **À retenir.** L'infostealer vole vite et peut contourner le MFA via les jetons de session : protéger/expirer les sessions et détecter les réutilisations anormales est crucial.

## Chapitre 192 — RAT (Remote Access Trojan)

1. **Définition.** Malware donnant à l'attaquant un *contrôle à distance interactif* de la machine infectée.
2. **Famille.** Malware par fonction (contrôle / C2).
3. **Principe.** Une fois installé, le RAT établit un canal de commande et contrôle ; l'attaquant pilote la machine (fichiers, écran, micro/caméra, commandes) comme s'il était devant.
4. **Sous-types.** RAT généralistes, mobiles, furtifs (chiffrés/légitimes en apparence).
5. **Exemple conceptuel.** Un RAT installé via trojan permet à l'attaquant d'exécuter des actions arbitraires sur le poste.
6. **Impacts.** Contrôle total du poste, espionnage, pivot, vol, persistance.
7. **Détection.** Trafic C2 (balises), comportements de contrôle distant, EDR/NDR.
8. **Prévention.** EDR, filtrage/détection de C2, moindre privilège, durcissement, allowlisting, surveillance, sensibilisation.
9. ⚠️ **Erreur fréquente.** Ne pas surveiller le trafic sortant/C2, qui trahit le RAT.
10. 🎯 **À retenir.** Le RAT = contrôle distant complet : la détection de C2 et l'EDR sont les parades centrales.

## Chapitre 193 — Backdoor

1. **Définition.** Mécanisme d'accès *caché et persistant* contournant l'authentification normale.
2. **Famille.** Persistance / accès.
3. **Principe.** La backdoor (porte dérobée) assure à l'attaquant un retour discret même après remédiation partielle ; elle peut être un compte caché, un service, un implant, ou intégrée à du code (supply chain).
4. **Sous-types.** Comptes cachés, services/implants, backdoors logicielles (supply chain), web shells.
5. **Exemple conceptuel.** Un accès caché est laissé en place pour revenir discrètement après l'intrusion initiale.
6. **Impacts.** Persistance, retour après éviction incomplète, contrôle durable.
7. **Détection.** Comptes/services inattendus, implants, intégrité du code, EDR, surveillance.
8. **Prévention.** Durcissement, intégrité (supply chain, chapitre 81), revue des comptes/services, EDR, éradication complète post-incident, surveillance.
9. ⚠️ **Erreur fréquente.** Éradiquer la charge visible sans chercher les portes dérobées laissées par l'attaquant.
10. 🎯 **À retenir.** Une backdoor garantit le retour de l'attaquant : l'éradication doit être *complète* et l'intégrité (code, comptes) vérifiée.

## Chapitre 194 — Loader

1. **Définition.** Composant dont la fonction est de *charger et exécuter* une charge malveillante ultérieure, souvent en mémoire.
2. **Famille.** Chaîne d'infection (exécution/évasion).
3. **Principe.** Le loader est la première brique discrète ; il prépare le terrain et charge la charge finale (parfois sans toucher le disque, pour échapper à la détection).
4. **Sous-types.** Loaders en mémoire, modulaires, vendus « as-a-service ».
5. **Exemple conceptuel.** Un loader léger récupère et exécute une charge plus volumineuse une fois en place.
6. **Impacts.** Installation de la charge réelle (RAT, ransomware, stealer), évasion.
7. **Détection.** Comportements de chargement/injection, exécution en mémoire, EDR.
8. **Prévention.** EDR (détection comportementale/mémoire), allowlisting, durcissement, surveillance.
9. ⚠️ **Erreur fréquente.** Se focaliser sur la charge finale en ignorant le loader, point d'entrée de la chaîne.
10. 🎯 **À retenir.** Le loader ouvre la chaîne d'infection : la détection comportementale/mémoire (EDR) est essentielle.

## Chapitre 195 — Dropper

1. **Définition.** Composant qui *dépose* (extrait/installe) une charge malveillante embarquée sur le système.
2. **Famille.** Chaîne d'infection.
3. **Principe.** Proche du loader, le dropper *contient* la charge (plutôt que de la télécharger) et l'installe ; il sert souvent de première étape déguisée.
4. **Sous-types.** Droppers embarqués dans des documents, des installeurs, des trojans.
5. **Exemple conceptuel.** Un fichier d'apparence anodine extrait et installe une charge malveillante qu'il contient.
6. **Impacts.** Installation de la charge, point de départ de l'infection.
7. **Détection.** Extraction/dépôt de composants suspects, comportements d'installation, EDR.
8. **Prévention.** EDR, allowlisting, méfiance documents/installeurs, sandbox, durcissement.
9. ⚠️ **Erreur fréquente.** Confondre dropper (charge embarquée) et downloader (charge téléchargée).
10. 🎯 **À retenir.** Le dropper porte la charge en lui ; le downloader va la chercher. Tous deux ouvrent la chaîne d'infection.

## Chapitre 196 — Downloader

1. **Définition.** Composant qui *télécharge* une charge malveillante depuis un serveur distant.
2. **Famille.** Chaîne d'infection.
3. **Principe.** Le downloader, minimal et discret, récupère ensuite la charge réelle depuis Internet — ce qui permet de changer la charge à volonté et d'échapper à l'analyse initiale.
4. **Sous-types.** Downloaders via documents, scripts, liens.
5. **Exemple conceptuel.** Un petit composant initial télécharge la charge finale depuis un serveur contrôlé par l'attaquant.
6. **Impacts.** Installation flexible de la charge, évasion, mise à jour de la charge.
7. **Détection.** Téléchargements vers/depuis des sources malveillantes, comportements, filtrage de réputation, EDR.
8. **Prévention.** Filtrage web/DNS et de réputation, EDR, allowlisting, sandbox, restriction des téléchargements, surveillance.
9. ⚠️ **Erreur fréquente.** Ne pas filtrer/inspecter les téléchargements sortants déclenchés par des documents/scripts.
10. 🎯 **À retenir.** Le downloader va chercher la charge en ligne : le filtrage de réputation et l'inspection des flux sortants le contrent.

## Chapitre 197 — Rootkit

1. **Définition.** Malware conçu pour *se cacher* profondément dans le système et masquer la présence d'autres composants.
2. **Famille.** Évasion / persistance (furtivité).
3. **Principe.** Le rootkit opère à un niveau privilégié (noyau, voire au-dessous) pour intercepter et falsifier ce que voit le système/les outils, rendant l'infection quasi invisible.
4. **Sous-types.** Rootkits utilisateur, noyau, firmware (recoupe le bootkit — chapitre 198).
5. **Exemple conceptuel.** Un rootkit masque ses fichiers et processus aux outils d'inspection standards.
6. **Impacts.** Furtivité extrême, persistance, contrôle profond, détection/éradication très difficiles.
7. **Détection.** Difficile depuis le système infecté ; analyse hors-ligne, intégrité (mesure/attestation), EDR avancé, comportements.
8. **Prévention.** Secure Boot, intégrité (TPM/attestation), moindre privilège, durcissement, EDR, sources de confiance, mises à jour.
9. ⚠️ **Erreur fréquente.** Faire confiance aux outils du système infecté pour détecter un rootkit (qu'il falsifie justement).
10. 🎯 **À retenir.** Le rootkit ment au système lui-même : l'intégrité matérielle (Secure Boot/TPM) et l'analyse hors-ligne sont les seules garanties.

## Chapitre 198 — Bootkit

1. **Définition.** Rootkit ciblant le *processus d'amorçage* (firmware/secteur de démarrage), s'exécutant avant le système d'exploitation.
2. **Famille.** Évasion / persistance bas niveau (recoupe firmware — chapitre 61).
3. **Principe.** En s'installant dans la séquence de démarrage, le bootkit prend le contrôle très tôt, survit aux réinstallations du système et échappe aux défenses chargées plus tard.
4. **Sous-types.** Bootkits du secteur d'amorçage, UEFI/firmware.
5. **Exemple conceptuel.** Un implant dans la séquence de démarrage s'exécute avant les protections du système et persiste malgré une réinstallation.
6. **Impacts.** Persistance maximale, furtivité, contrôle pré-OS, éradication très difficile.
7. **Détection.** Mesure d'intégrité du démarrage (attestation), analyse firmware, comportements anormaux.
8. **Prévention.** **Secure Boot**, intégrité mesurée (TPM), mises à jour firmware signées, approvisionnement de confiance, surveillance.
9. ⚠️ **Erreur fréquente.** Croire qu'une réinstallation du système élimine toute infection (un bootkit firmware survit).
10. 🎯 **À retenir.** Le bootkit s'installe avant l'OS et survit aux réinstallations : Secure Boot et l'intégrité mesurée sont indispensables.

## Chapitre 199 — Fileless malware

1. **Définition.** Malware opérant *sans fichier sur disque*, en résidant en mémoire et en abusant d'outils légitimes.
2. **Famille.** Évasion (defense evasion).
3. **Principe.** En s'exécutant en mémoire et via des binaires/outils du système (living-off-the-land — chapitre 201), le fileless malware évite les détections basées sur les fichiers.
4. **Sous-types.** Exécution en mémoire, persistance via mécanismes système, abus d'interpréteurs/outils légitimes.
5. **Exemple conceptuel.** Une charge ne s'écrit jamais sur disque et opère uniquement en mémoire, via des outils déjà présents.
6. **Impacts.** Évasion des défenses classiques, furtivité, exécution de charges variées.
7. **Détection.** **Détection comportementale/mémoire** (EDR), surveillance de l'usage anormal d'outils système, journalisation des interpréteurs.
8. **Prévention.** EDR comportemental, journalisation/restriction des interpréteurs, moindre privilège, allowlisting, durcissement.
9. ⚠️ **Erreur fréquente.** S'appuyer sur la seule analyse de fichiers (signatures), inefficace contre le fileless.
10. 🎯 **À retenir.** Le fileless malware échappe à l'analyse de fichiers : seule la détection comportementale/mémoire le repère.

## Chapitre 200 — Macro malware

1. **Définition.** Malware véhiculé par les *macros* de documents bureautiques.
2. **Famille.** Vecteur d'exécution côté client (souvent via phishing).
3. **Principe.** Un document piégé incite l'utilisateur à activer les macros, qui exécutent alors un loader/downloader déclenchant la chaîne d'infection.
4. **Sous-types.** Macros dans documents texte/tableur/présentation, combinées à de l'ingénierie sociale.
5. **Exemple conceptuel.** Un document demande d'« activer le contenu » ; la macro lance alors le téléchargement d'une charge.
6. **Impacts.** Accès initial, installation de charges, point d'entrée fréquent.
7. **Détection.** Documents avec macros suspectes, comportements post-activation, EDR, filtrage mail.
8. **Prévention.** **Désactiver/bloquer les macros** (surtout depuis Internet), filtrage mail, sensibilisation, EDR, allowlisting, sandbox.
9. ⚠️ **Erreur fréquente.** Autoriser les macros par défaut, surtout sur les documents provenant d'Internet.
10. 🎯 **À retenir.** Les macros sont un vecteur d'entrée classique : les bloquer (notamment depuis Internet) coupe une voie majeure.

## Chapitre 201 — Living-off-the-land (LotL)

1. **Définition.** Technique consistant à mener l'attaque avec les *outils légitimes déjà présents* sur le système, pour se fondre dans l'activité normale.
2. **Famille.** Évasion / exécution.
3. **Principe.** Plutôt que d'apporter des outils détectables, l'attaquant abuse d'utilitaires d'administration et d'interpréteurs intégrés — difficile à distinguer d'une activité légitime.
4. **Sous-types.** Abus d'outils d'administration, d'interpréteurs de scripts, de binaires système (LOLBins — chapitre 202).
5. **Exemple conceptuel.** Des tâches malveillantes sont exécutées via des outils d'administration normaux, sans introduire de logiciel suspect.
6. **Impacts.** Évasion, mouvement latéral discret, exécution furtive.
7. **Détection.** **Analyse comportementale** (usage anormal d'outils légitimes), journalisation détaillée, corrélation, EDR.
8. **Prévention.** Journalisation et restriction des outils/interpréteurs, moindre privilège, allowlisting, durcissement, détection comportementale.
9. ⚠️ **Erreur fréquente.** Ne surveiller que les « logiciels malveillants » et ignorer l'usage détourné des outils légitimes.
10. 🎯 **À retenir.** Le LotL se cache dans le légitime : seule l'analyse comportementale du *contexte d'usage* le révèle.

## Chapitre 202 — LOLBins

1. **Définition.** *Living-off-the-Land Binaries* : binaires/outils système légitimes détournés à des fins malveillantes.
2. **Famille.** Sous-ensemble du LotL (chapitre 201).
3. **Principe.** Certains binaires intégrés ont des fonctionnalités (télécharger, exécuter, contourner) réutilisables par l'attaquant pour agir sans apporter d'outil suspect.
4. **Sous-types.** Selon les fonctions détournées (téléchargement, exécution, contournement de contrôle).
5. **Exemple conceptuel.** Un utilitaire système légitime est employé pour télécharger ou exécuter une charge, échappant aux contrôles centrés sur les « logiciels inconnus ».
6. **Impacts.** Exécution/évasion via des outils de confiance, détection difficile.
7. **Détection.** Usage anormal de binaires système (paramètres/contexte inhabituels), journalisation, EDR, corrélation.
8. **Prévention.** Restriction/journalisation des binaires sensibles, allowlisting fin, moindre privilège, détection comportementale.
9. ⚠️ **Erreur fréquente.** Allowlister un binaire « de confiance » sans surveiller *comment* il est utilisé.
10. 🎯 **À retenir.** Un binaire légitime peut être une arme : surveiller le contexte d'usage, pas seulement l'identité du binaire.

---

## Ingénierie sociale et phishing — vue d'ensemble

L'**ingénierie sociale** manipule l'humain (chapitre 59) plutôt que la technique. Elle se classe par *canal* (mail, SMS, voix, QR, web) et par *cible/objectif* (générique vs ciblé, vol d'identifiants vs fraude). Le levier psychologique est constant : *autorité, urgence, peur, curiosité, appât, confiance*.

🧭 **Taxonomie** — Le phishing est la famille mère ; les variantes se distinguent par le canal (smishing = SMS, vishing = voix, quishing = QR) et la cible (spear phishing = ciblé, whaling = dirigeants, BEC = fraude par usurpation).

## Chapitre 203 — Phishing

1. **Définition.** Tromperie de masse (souvent par e-mail) incitant la victime à divulguer des informations ou à exécuter une action (cliquer, ouvrir, payer).
2. **Famille.** Ingénierie sociale (canal e-mail), vecteur d'entrée n°1.
3. **Principe.** Un message usurpant une entité de confiance exploite un levier psychologique pour pousser à cliquer un lien (vers un faux site), ouvrir une pièce jointe, ou livrer des identifiants.
4. **Sous-types.** Vol d'identifiants (faux portail), pièce jointe piégée, lien malveillant ; décliné par canal/cible (chapitres 204–217).
5. **Exemple conceptuel.** Un faux message « sécurité » demande de « vérifier » son compte sur un site imitant le vrai, captant les identifiants saisis.
6. **Impacts.** Vol d'identifiants, accès initial, installation de malware, fraude.
7. **Détection.** Filtrage mail, signalements d'utilisateurs, anomalies de domaines/liens, authentification d'expéditeur, surveillance.
8. **Prévention.** **Sensibilisation + culture du signalement**, filtrage mail, SPF/DKIM/DMARC (chapitre 294), analyse des liens/pièces jointes, **MFA résistant au phishing**, moindre privilège.
9. ⚠️ **Erreur fréquente.** Punir les utilisateurs qui cliquent (ils cessent de signaler) ; se reposer sur la seule technique sans former.
10. 🎯 **À retenir.** Le phishing est la porte d'entrée la plus utilisée : sensibilisation, filtrage, authentification d'expéditeur et MFA résistant au phishing forment la défense.

## Chapitre 204 — Spear phishing

1. **Définition.** Phishing *ciblé* sur une personne/organisation précise, personnalisé pour être crédible.
2. **Famille.** Ingénierie sociale ciblée.
3. **Principe.** L'attaquant se renseigne (OSINT) pour adapter le message au contexte de la cible (collègues, projets, jargon), augmentant fortement le taux de succès.
4. **Sous-types.** Spear phishing d'identifiants, à charge, de fraude ; vers individus clés.
5. **Exemple conceptuel.** Un message faisant référence à un projet réel de la cible et à un collègue plausible demande une action urgente.
6. **Impacts.** Compromission ciblée, accès à des comptes/données de valeur.
7. **Détection.** Plus difficile (peu de volume) ; signalement, anomalies fines, authentification d'expéditeur, surveillance.
8. **Prévention.** Sensibilisation ciblée (notamment des profils à risque), procédures de vérification, MFA résistant au phishing, réduction de l'empreinte OSINT.
9. ⚠️ **Erreur fréquente.** Croire que seuls les messages « grossiers » sont du phishing : le spear phishing est soigné et personnalisé.
10. 🎯 **À retenir.** Le spear phishing est précis et crédible : sensibilisation ciblée, vérification hors canal et MFA fort sont essentiels.

## Chapitre 205 — Whaling

1. **Définition.** Spear phishing visant les *dirigeants* (« gros poissons »), à fort pouvoir et accès.
2. **Famille.** Ingénierie sociale ciblée (cible = direction).
3. **Principe.** Usurpation ou ciblage de cadres dirigeants, dont la compromission donne un accès et une autorité considérables (et facilite la fraude par usurpation — BEC).
4. **Sous-types.** Usurpation de dirigeant, ciblage de dirigeant.
5. **Exemple conceptuel.** Un message conçu pour un dirigeant exploite son autorité ou le cible pour obtenir un accès privilégié.
6. **Impacts.** Accès à haut niveau, fraude de grande ampleur, atteinte stratégique.
7. **Détection.** Surveillance des comptes dirigeants, authentification d'expéditeur, signalement, anomalies.
8. **Prévention.** Protection renforcée des dirigeants (MFA fort, sensibilisation dédiée), procédures de vérification des demandes sensibles, surveillance.
9. ⚠️ **Erreur fréquente.** Accorder aux dirigeants des exemptions de sécurité « par confort », les rendant plus vulnérables.
10. 🎯 **À retenir.** Les dirigeants sont des cibles de choix : leur protection doit être *renforcée*, jamais allégée.

## Chapitre 206 — Smishing

1. **Définition.** Phishing par *SMS/messagerie mobile*.
2. **Famille.** Ingénierie sociale (canal SMS).
3. **Principe.** Un SMS usurpant une entité de confiance (banque, livraison, administration) pousse à cliquer un lien ou à rappeler, exploitant la confiance et l'immédiateté du mobile.
4. **Sous-types.** Faux liens de suivi/paiement, faux supports, liens vers faux portails.
5. **Exemple conceptuel.** Un SMS « colis en attente » invite à régler des frais sur un faux site.
6. **Impacts.** Vol d'identifiants/paiement, installation d'app malveillante, fraude.
7. **Détection.** Signalement, filtrage SMS, réputation de liens/numéros, sensibilisation.
8. **Prévention.** Sensibilisation, prudence sur mobile, MFA, vérification hors canal, MDM/MAM (chapitre 51).
9. ⚠️ **Erreur fréquente.** Faire davantage confiance à un SMS qu'à un e-mail (le mobile inspire une confiance trompeuse).
10. 🎯 **À retenir.** Le smishing exploite la confiance mobile : appliquer la même vigilance que pour l'e-mail.

## Chapitre 207 — Vishing

1. **Définition.** Phishing par *appel vocal* (voice phishing).
2. **Famille.** Ingénierie sociale (canal voix).
3. **Principe.** L'attaquant appelle en se faisant passer pour un support, une banque ou un collègue, et manipule la victime en temps réel (urgence, autorité) pour obtenir secrets ou actions. La voix synthétique/clonée renforce la menace.
4. **Sous-types.** Faux support technique, fausse banque, usurpation de collègue/dirigeant, couplé au MFA fatigue.
5. **Exemple conceptuel.** Un appel « du service informatique » demande de confirmer un code ou d'effectuer une action « urgente ».
6. **Impacts.** Vol de secrets/codes, contournement de MFA, fraude, accès.
7. **Détection.** Difficile (canal voix) ; signalement, procédures de vérification, sensibilisation.
8. **Prévention.** **Procédures de vérification d'identité** (rappel par canal officiel), sensibilisation, ne jamais communiquer de code, MFA résistant au phishing.
9. ⚠️ **Erreur fréquente.** Communiquer un code MFA à un appelant « officiel » (jamais légitime).
10. 🎯 **À retenir.** Le vishing manipule en direct : ne jamais livrer de code/secret par téléphone, vérifier par canal officiel.

## Chapitre 208 — Quishing

1. **Définition.** Phishing via *QR codes* malveillants.
2. **Famille.** Ingénierie sociale (canal QR/visuel).
3. **Principe.** Un QR code (dans un e-mail, une affiche, un courrier) redirige vers un faux site ou déclenche une action ; il contourne certains filtres de liens et exploite la confiance dans les QR.
4. **Sous-types.** QR dans e-mails, affiches/autocollants détournés, faux paiements.
5. **Exemple conceptuel.** Un QR code « officiel » mène à un faux portail captant les identifiants.
6. **Impacts.** Vol d'identifiants/paiement, redirection vers malware.
7. **Détection.** Sensibilisation, analyse des QR/liens, signalement, filtrage.
8. **Prévention.** Sensibilisation, prévisualiser l'URL d'un QR, prudence, MFA, vérification de la source physique.
9. ⚠️ **Erreur fréquente.** Scanner un QR sans vérifier la destination (le QR masque l'URL).
10. 🎯 **À retenir.** Le quishing cache l'URL derrière une image : toujours vérifier la destination avant d'agir.

## Chapitre 209 — BEC (Business Email Compromise)

1. **Définition.** Fraude par usurpation/compromission d'e-mail professionnel, visant à détourner des fonds ou des données (« fraude au président »/au fournisseur).
2. **Famille.** Ingénierie sociale orientée fraude (souvent sans malware).
3. **Principe.** L'attaquant usurpe (ou compromet) une boîte de confiance (dirigeant, fournisseur) et demande un virement ou un changement de coordonnées bancaires, en jouant sur l'autorité et l'urgence. Souvent *sans pièce jointe ni lien*, donc difficile à filtrer.
4. **Sous-types.** Fraude au président, au fournisseur (changement d'IBAN), détournement de facture, compromission de compte réel.
5. **Exemple conceptuel.** Un message « du dirigeant » demande un virement urgent et confidentiel vers un nouveau compte.
6. **Impacts.** Pertes financières majeures, fuite de données, fraude difficile à récupérer.
7. **Détection.** Anomalies d'expéditeur/domaine, demandes inhabituelles, surveillance des règles de boîte (exfiltration), authentification d'expéditeur.
8. **Prévention.** **Procédures de double validation** des paiements/changements d'IBAN (hors canal e-mail), séparation des tâches (chapitre 14), MFA, SPF/DKIM/DMARC, sensibilisation des fonctions financières.
9. ⚠️ **Erreur fréquente.** Valider un virement ou un changement d'IBAN sur la seule foi d'un e-mail, sans vérification indépendante.
10. 🎯 **À retenir.** Le BEC est une fraude « sans malware » qui exploite la confiance : la double validation hors canal et la séparation des tâches sont les vraies parades.

## Chapitre 210 — Malspam

1. **Définition.** Diffusion *massive* d'e-mails malveillants (charges ou liens) pour infecter au volume.
2. **Famille.** Ingénierie sociale de masse / vecteur de malware.
3. **Principe.** Campagnes à grande échelle distribuant droppers/downloaders/macro malware via pièces jointes ou liens, comptant sur le nombre.
4. **Sous-types.** Pièces jointes piégées, liens vers charges, vagues thématiques (factures, livraisons).
5. **Exemple conceptuel.** Une vague d'e-mails « facture » diffuse un document piégé à grande échelle.
6. **Impacts.** Infections en masse, accès initiaux, point de départ de campagnes (ransomware).
7. **Détection.** Filtrage mail, réputation, signalement, sandbox, EDR.
8. **Prévention.** Filtrage mail robuste, blocage des macros/types dangereux, SPF/DKIM/DMARC, sensibilisation, EDR.
9. ⚠️ **Erreur fréquente.** Sous-estimer le malspam « générique » qui reste un vecteur d'entrée massif.
10. 🎯 **À retenir.** Le malspam mise sur le volume : filtrage mail + blocage des charges dangereuses + sensibilisation le contiennent.

## Chapitre 211 — Drive-by download

1. **Définition.** Infection déclenchée par la *simple visite* d'un site piégé, sans action volontaire de l'utilisateur.
2. **Famille.** Attaque client-side (navigateur — chapitre 50).
3. **Principe.** Un site malveillant (ou légitime compromis) exploite une vulnérabilité du navigateur/plugin pour installer une charge à l'insu du visiteur.
4. **Sous-types.** Via exploit de navigateur, via faux contenus, souvent couplé à malvertising/watering hole.
5. **Exemple conceptuel.** La visite d'une page compromise déclenche l'exploitation d'une faille du navigateur pour installer un malware.
6. **Impacts.** Infection silencieuse, accès initial.
7. **Détection.** Exploitation navigateur, comportements post-visite, EDR, filtrage web.
8. **Prévention.** **Mises à jour** du navigateur/plugins, isolation/sandboxing, filtrage web/DNS, allowlisting, EDR, durcissement.
9. ⚠️ **Erreur fréquente.** Retarder les mises à jour du navigateur, principal rempart contre les drive-by.
10. 🎯 **À retenir.** Le drive-by infecte sans clic : navigateur à jour, isolation et filtrage web sont les défenses centrales.

## Chapitre 212 — Malvertising

1. **Définition.** Diffusion de malware/redirections via des *publicités en ligne* piégées.
2. **Famille.** Attaque client-side / abus de l'écosystème publicitaire.
3. **Principe.** Des publicités malveillantes (injectées dans des réseaux publicitaires, parfois sur des sites légitimes) redirigent vers des kits d'exploitation, de fausses mises à jour, ou des sites de phishing.
4. **Sous-types.** Publicité piégée, redirection vers exploit kit, fausse mise à jour, typosquatting publicitaire, empoisonnement SEO (chapitre 213), campagne via réseau publicitaire compromis.
5. **Exemple conceptuel.** Une publicité affichée sur un site légitime redirige vers une fausse page de mise à jour proposant un malware.
6. **Impacts.** Infection, redirection vers phishing, drive-by, fraude.
7. **Détection.** Redirections publicitaires anormales, filtrage, EDR, signalement.
8. **Prévention.** Filtrage web/DNS, bloqueurs de publicités/scripts, navigateur à jour, isolation, sensibilisation (méfiance envers les « mises à jour » issues de pubs).
9. ⚠️ **Erreur fréquente.** Faire confiance à une publicité parce qu'elle apparaît sur un site légitime (le réseau pub peut être compromis).
10. 🎯 **À retenir.** Le malvertising piège même des sites légitimes via la pub : filtrage, blocage de scripts et navigateur à jour réduisent le risque.

## Chapitre 213 — SEO poisoning

1. **Définition.** Manipulation du référencement pour faire remonter des *sites malveillants* dans les résultats de recherche.
2. **Famille.** Attaque client-side / manipulation de la découverte.
3. **Principe.** L'attaquant optimise des pages malveillantes (souvent sur des sujets recherchés ou des « téléchargements de logiciels ») pour qu'elles apparaissent en tête, attirant des victimes qui les croient légitimes.
4. **Sous-types.** Faux sites de logiciels/cracks, sujets d'actualité, pages compromises optimisées.
5. **Exemple conceptuel.** Une recherche de logiciel populaire renvoie en tête un faux site distribuant un installeur piégé.
6. **Impacts.** Infection, vol d'identifiants, fraude.
7. **Détection.** Réputation des sites/domaines, filtrage web, EDR, signalement.
8. **Prévention.** Filtrage de réputation, allowlisting des sources logicielles, sensibilisation (ne pas télécharger « le premier résultat »), navigateur à jour.
9. ⚠️ **Erreur fréquente.** Télécharger un logiciel depuis le premier résultat de recherche sans vérifier la source officielle.
10. 🎯 **À retenir.** Le SEO poisoning exploite la confiance dans les résultats de recherche : privilégier les sources officielles et le filtrage de réputation.

## Chapitre 214 — Watering hole

1. **Définition.** Attaque compromettant un site *légitime fréquenté par la cible* pour l'infecter quand elle le visite.
2. **Famille.** Attaque ciblée client-side.
3. **Principe.** Plutôt que d'attaquer directement une cible bien défendue, l'attaquant piège un site que cette cible visite habituellement (« point d'eau »), puis attend qu'elle s'y rende (souvent via drive-by).
4. **Sous-types.** Compromission de sites sectoriels/communautaires fréquentés par la cible.
5. **Exemple conceptuel.** Un site spécialisé visité par les employés d'un secteur est compromis pour les infecter à leur passage.
6. **Impacts.** Infection ciblée, accès initial à des cibles difficiles d'accès.
7. **Détection.** Exploitation/drive-by à la visite, EDR, filtrage web, renseignement (CTI).
8. **Prévention.** Navigateur à jour, isolation, filtrage web, EDR, CTI sur les campagnes sectorielles, durcissement.
9. ⚠️ **Erreur fréquente.** Supposer qu'un site « habituel et de confiance » ne peut pas être compromis.
10. 🎯 **À retenir.** Le watering hole piège un site de confiance fréquenté par la cible : mises à jour, isolation et CTI sectorielle sont les parades.

## Chapitre 215 — Social engineering (synthèse)

**Définition.** Discipline d'ensemble : manipuler des personnes pour obtenir des informations, des accès ou des actions, en exploitant des leviers psychologiques.

**Principe.** Tous les chapitres précédents en sont des déclinaisons (par canal/cible). Les leviers récurrents : *autorité* (faire croire à un supérieur/une institution), *urgence* (empêcher la réflexion), *peur* (menace), *réciprocité/sympathie* (créer un lien), *preuve sociale*, *appât du gain*, *curiosité*. Techniques connexes : prétexting (scénario fabriqué), baiting (appât physique/numérique), tailgating (suivre quelqu'un dans un local).

🛡️ **Défense** — Sensibilisation continue et concrète, culture du signalement *sans punition*, procédures de vérification (double validation, rappel par canal officiel), séparation des tâches, moindre privilège, MFA résistant au phishing.

🧭 **Taxonomie** — Famille mère de la Partie 9 côté humain ; complète la famille « malware » côté technique. Cible la surface *humaine* (chapitre 59).

🎯 **À retenir** — L'ingénierie sociale contourne la technique en ciblant l'humain : la défense est *humaine et procédurale* autant que technique.

## Chapitre 216 — MFA fatigue

1. **Définition.** Attaque submergeant la victime de *demandes d'approbation MFA* jusqu'à ce qu'elle accepte par lassitude ou erreur.
2. **Famille.** Ingénierie sociale / contournement de MFA.
3. **Principe.** Disposant déjà du mot de passe (volé/fuité), l'attaquant déclenche des notifications push répétées ; la victime finit par approuver pour faire cesser le flot (parfois aidée par un appel de vishing « du support »).
4. **Sous-types.** Spam de push, couplé à du vishing, exploitation de la confusion.
5. **Exemple conceptuel.** Des demandes d'approbation répétées poussent la victime à valider l'une d'elles pour stopper les notifications.
6. **Impacts.** Contournement du MFA, prise de compte.
7. **Détection.** Volumes anormaux de demandes MFA, approbations après rafales, surveillance.
8. **Prévention.** **MFA résistant au phishing** (correspondance de nombre, clés FIDO2/passkeys), limitation des demandes, sensibilisation (ne jamais approuver une demande non initiée), surveillance.
9. ⚠️ **Erreur fréquente.** Utiliser un MFA par simple push « approuver/refuser », vulnérable à la fatigue.
10. 🎯 **À retenir.** La MFA fatigue exploite le push simple : passer à un MFA résistant au phishing (FIDO2/number matching) la neutralise.

## Chapitre 217 — Consent phishing

1. **Définition.** Tromperie poussant la victime à *accorder des autorisations OAuth* à une application malveillante (plutôt qu'à livrer un mot de passe).
2. **Famille.** Ingénierie sociale / abus d'OAuth (SaaS — chapitre 56).
3. **Principe.** L'attaquant présente une application demandant des permissions (lire les mails, accéder aux fichiers) ; en consentant, la victime donne un accès durable *sans* divulguer son mot de passe, et le MFA ne protège pas (l'accès passe par le jeton octroyé).
4. **Sous-types.** Fausses applications, permissions excessives, persistance via jetons.
5. **Exemple conceptuel.** Une application d'apparence légitime demande l'accès à la boîte mail ; le consentement accordé lui donne un accès persistant.
6. **Impacts.** Accès durable aux données (mail, fichiers), exfiltration, persistance contournant mot de passe et MFA.
7. **Détection.** Octrois de consentement à des applications inconnues/permissions larges, surveillance des intégrations OAuth.
8. **Prévention.** **Gouvernance des consentements OAuth** (restreindre, approuver les applications), revue des permissions, allowlist d'applications, sensibilisation, surveillance.
9. ⚠️ **Erreur fréquente.** Laisser les utilisateurs accorder librement des permissions OAuth à n'importe quelle application.
10. 🎯 **À retenir.** Le consent phishing vole un *accès délégué*, pas un mot de passe : la gouvernance des consentements OAuth est la défense spécifique (le MFA n'y suffit pas).

---

> **Fin du Volume 6/8.**
>
> Vous savez classer un malware sur deux axes (forme/propagation et fonction/charge) et situer chaque technique d'ingénierie sociale par canal et par cible, avec leurs défenses (EDR/comportemental, intégrité matérielle, filtrage, sensibilisation, MFA résistant au phishing, gouvernance OAuth, procédures de vérification).
>
> **Suite — Volume 7 : Partie 10, Cloud, API, conteneurs et supply chain** (principes cloud et responsabilité partagée ; IAM cloud, buckets/secrets/clés exposés, métadonnées, élévation et lateral movement cloud ; API : BOLA/BFLA, exposition de données, consommation non limitée, consommation non sûre d'API ; Kubernetes RBAC, container escape, images/registres ; CI/CD, pipeline poisoning, dependency confusion, typosquatting, paquets malveillants, compromission du build, signature/intégrité, SBOM, gestion des secrets).


---

# Taxonomie de la cybersécurité — Volume 7/8

> Partie 10 : Cloud, API, conteneurs et supply chain
>
> Cette partie couvre les surfaces « modernes » (chapitres 45–48) où la sécurité repose moins sur le périmètre que sur la **configuration**, l'**identité** et l'**intégrité de la chaîne logicielle**. Références utiles : OWASP API Security Top 10 (2023), SLSA, SBOM. Format en 10 points pour les attaques majeures.
>
> **Posture** : mécanismes, impacts et défenses, sans procédure offensive opérationnelle.

---

# Partie 10 — Cloud, API, conteneurs et supply chain

## Chapitre 218 — Cloud security : principes

**Définition.** Ensemble des pratiques sécurisant les ressources et données hébergées dans le cloud (IaaS/PaaS/SaaS).

**Principe central : la responsabilité partagée.** Le fournisseur sécurise *l'infrastructure* (« sécurité *du* cloud ») ; le client sécurise *ses configurations, identités et données* (« sécurité *dans* le cloud »). La frontière varie selon le modèle (IaaS → plus de responsabilité client ; SaaS → moins). La majorité des incidents cloud viennent d'erreurs *côté client* (mauvaise configuration, identités, secrets).

🧭 **Taxonomie** — Dans le cloud, la *mauvaise configuration* (chapitre 67) et l'*identité* (chapitre 57) remplacent souvent la vulnérabilité logicielle comme cause première.

⚠️ **Erreur fréquente** — Croire que « migrer dans le cloud » délègue toute la sécurité au fournisseur.

🎯 **À retenir** — Comprendre la responsabilité partagée est le préalable : le fournisseur sécurise le socle, vous restez responsable de vos configurations, identités et données.

## Chapitre 219 — IAM cloud

1. **Définition.** Gestion des identités et des droits dans le cloud — qui (utilisateur, service, rôle) peut faire quoi sur quelles ressources.
2. **Famille.** Identité / autorisation (cœur de la sécurité cloud).
3. **Principe.** L'IAM cloud est extrêmement granulaire et puissant ; mal maîtrisé, il crée des permissions excessives et des *chemins d'élévation* (un rôle pouvant en assumer un autre, plus privilégié).
4. **Sous-types.** Permissions excessives, rôles assumables en chaîne, politiques trop larges, clés/identités de service surpuissantes.
5. **Exemple conceptuel.** Un rôle peu privilégié peut en assumer un autre plus puissant, ouvrant un chemin d'élévation non prévu.
6. **Impacts.** Élévation de privilèges, accès étendu aux ressources/données, prise de contrôle du tenant.
7. **Détection.** Analyse des politiques (permissions effectives), usage anormal de rôles, journaux cloud, surveillance.
8. **Prévention.** **Moindre privilège** strict, analyse des permissions effectives, suppression des chemins d'élévation, séparation, revue d'accès, journalisation, MFA.
9. ⚠️ **Erreur fréquente.** Politiques permissives « pour que ça marche » (wildcards de permissions) jamais resserrées.
10. 🎯 **À retenir.** L'IAM est le vrai périmètre du cloud : moindre privilège, analyse des permissions effectives et suppression des chemins d'élévation sont prioritaires.

## Chapitre 220 — Bucket public

1. **Définition.** Espace de stockage objet (bucket) exposé publiquement par mauvaise configuration.
2. **Famille.** Mauvaise configuration (chapitre 67) / exposition de données.
3. **Principe.** Un stockage destiné à être privé est rendu accessible à tous (lecture, voire écriture) par une configuration trop ouverte — cause récurrente de fuites massives.
4. **Sous-types.** Lecture publique (fuite), écriture publique (altération/empoisonnement), permissions héritées trop larges.
5. **Exemple conceptuel.** Un espace de stockage contenant des données sensibles est accessible sans authentification à cause d'un réglage public.
6. **Impacts.** Fuite massive de données, altération de contenus, atteinte réglementaire.
7. **Détection.** Outils de posture cloud (CSPM), audit des configurations d'accès, surveillance des accès anonymes.
8. **Prévention.** **Blocage de l'accès public par défaut**, CSPM, chiffrement, moindre privilège, revue régulière, journalisation des accès.
9. ⚠️ **Erreur fréquente.** Rendre un bucket public « temporairement » et l'oublier ; permissions héritées non vérifiées.
10. 🎯 **À retenir.** Le bucket public est une cause classique de fuite : bloquer l'accès public par défaut et surveiller la posture (CSPM).

## Chapitre 221 — Secret exposé

1. **Définition.** Secret (mot de passe, jeton, certificat) rendu accessible dans un contexte cloud (configuration, stockage, variables, dépôt).
2. **Famille.** Exposition de secrets (chapitre 77) en contexte cloud.
3. **Principe.** Les secrets se retrouvent dans des fichiers de configuration, des images, des variables d'environnement, des dépôts — accessibles à qui ne devrait pas, offrant un accès direct.
4. **Sous-types.** Secrets dans le code/IaC, dans des images de conteneurs, dans des journaux, dans des buckets.
5. **Exemple conceptuel.** Un fichier de configuration exposé contient un secret donnant accès à un service cloud.
6. **Impacts.** Accès direct aux services/données, élévation, mouvement latéral cloud.
7. **Détection.** Secrets scanning, surveillance des dépôts/images/journaux, détection d'usage anormal de secrets.
8. **Prévention.** **Gestionnaire de secrets** dédié, interdiction des secrets en dur, scanning (pré-commit/CI), rotation/révocation rapide, moindre privilège.
9. ⚠️ **Erreur fréquente.** Stocker des secrets dans le code/l'IaC ou les variables, au lieu d'un coffre dédié.
10. 🎯 **À retenir.** Un secret exposé donne un accès immédiat : externaliser dans un coffre, scanner et faire tourner les secrets.

## Chapitre 222 — Clé API exposée

1. **Définition.** Cas particulier (et fréquent) de secret exposé : une clé d'API laissée accessible.
2. **Famille.** Exposition de secrets / accès aux services.
3. **Principe.** Les clés d'API authentifient des appels ; exposées (dépôt public, application cliente, journaux), elles permettent d'utiliser le service au nom du propriétaire, parfois avec des droits étendus et sans limite.
4. **Sous-types.** Clés dans dépôts publics, dans applications mobiles/front, dans journaux, surprivilégiées.
5. **Exemple conceptuel.** Une clé d'API trouvée dans un dépôt public permet d'appeler le service associé.
6. **Impacts.** Usage frauduleux (coûts), accès aux données, abus du service.
7. **Détection.** Secrets scanning, surveillance d'usage anormal des clés, alertes des fournisseurs.
8. **Prévention.** Coffre à secrets, **portée minimale** des clés, rotation, restriction (par IP/domaine/usage), ne pas exposer de clés sensibles côté client, scanning.
9. ⚠️ **Erreur fréquente.** Embarquer une clé puissante dans une application cliente (donc extractible).
10. 🎯 **À retenir.** Une clé d'API exposée est exploitable immédiatement : portée minimale, rotation, restriction et scanning sont indispensables.

## Chapitre 223 — Metadata service abuse

1. **Définition.** Abus du *service de métadonnées* d'instance cloud pour récupérer des identifiants temporaires.
2. **Famille.** Credential access cloud (souvent via SSRF — chapitre 107).
3. **Principe.** Les instances exposent en interne un service fournissant configuration et crédentiels de rôle ; un accès indu (via SSRF ou compromission de l'instance) permet de récupérer ces identifiants et d'usurper le rôle.
4. **Sous-types.** Via SSRF, via compromission d'instance, selon la version (renforcée ou non) du service.
5. **Exemple conceptuel.** Une faille permet d'interroger le point de métadonnées et d'obtenir les identifiants du rôle de l'instance.
6. **Impacts.** Vol d'identifiants cloud, élévation, mouvement latéral, accès aux ressources.
7. **Détection.** Accès anormaux au point de métadonnées, usage inattendu d'identifiants de rôle, journaux.
8. **Prévention.** **Version renforcée** du service de métadonnées, blocage de cet accès depuis les applications, moindre privilège des rôles d'instance, allowlist SSRF, surveillance.
9. ⚠️ **Erreur fréquente.** Service de métadonnées en version permissive + rôles d'instance surprivilégiés.
10. 🎯 **À retenir.** Le service de métadonnées peut livrer des identifiants : le durcir et appliquer le moindre privilège aux rôles d'instance.

## Chapitre 224 — Privilege escalation cloud

1. **Définition.** Élévation de privilèges au sein d'un environnement cloud, souvent via l'IAM.
2. **Famille.** Privilege Escalation cloud.
3. **Principe.** En exploitant des permissions mal configurées (créer/modifier des politiques, assumer des rôles, modifier des identités), un accès limité peut être transformé en accès étendu, voire administrateur du tenant.
4. **Sous-types.** Via chaînes de rôles, via droits de modification de politiques, via secrets/métadonnées, via services privilégiés.
5. **Exemple conceptuel.** Un droit de modification de politique permet de s'octroyer des permissions supplémentaires.
6. **Impacts.** Contrôle étendu du tenant, accès aux données, persistance.
7. **Détection.** Modifications de politiques/rôles anormales, analyse des chemins d'élévation, journaux cloud, surveillance.
8. **Prévention.** Moindre privilège, suppression des permissions « dangereuses » de modification, analyse des chemins d'élévation, séparation, surveillance, MFA.
9. ⚠️ **Erreur fréquente.** Accorder des droits de modification d'IAM sans en mesurer le potentiel d'auto-élévation.
10. 🎯 **À retenir.** L'élévation cloud passe surtout par l'IAM : traquer et supprimer les chemins d'auto-élévation est la défense clé.

## Chapitre 225 — Lateral movement cloud

1. **Définition.** Déplacement entre ressources/comptes/services cloud après un accès initial.
2. **Famille.** Lateral Movement cloud.
3. **Principe.** L'attaquant rebondit via identités (rôles assumables), relations de confiance entre comptes, services interconnectés, secrets et métadonnées, jusqu'aux ressources de valeur.
4. **Sous-types.** Via rôles/identités, via relations inter-comptes, via services partagés, via secrets récupérés.
5. **Exemple conceptuel.** Des identifiants récupérés sur une ressource permettent d'accéder à d'autres services puis à un autre compte lié.
6. **Impacts.** Extension de la compromission, accès aux données, contrôle multi-comptes.
7. **Détection.** Usage anormal d'identités/rôles, accès inter-services/comptes inhabituels, journaux cloud, surveillance.
8. **Prévention.** Moindre privilège, segmentation des comptes/ressources, maîtrise des relations de confiance, gestion des secrets, surveillance, détection comportementale.
9. ⚠️ **Erreur fréquente.** Relations de confiance trop larges entre comptes/services, facilitant le rebond.
10. 🎯 **À retenir.** Le lateral movement cloud suit les identités et relations de confiance : les minimiser et surveiller leur usage le freine.

## Chapitre 226 — API security : principes

**Définition.** Pratiques sécurisant les API (chapitre 45), socle des applications modernes et des microservices.

**Principe.** Les API exposent directement données et fonctions. Leurs failles dominantes ne sont pas l'injection classique mais l'**autorisation** (par objet et par fonction), l'**exposition excessive de données**, et l'**absence de limites**. L'OWASP API Security Top 10 (2023) structure ces risques.

🧭 **Taxonomie** — Les chapitres 227–231 déclinent les principaux risques API ; BOLA/BFLA sont les équivalents API du Broken Access Control (Partie 6).

🎯 **À retenir** — La sécurité des API se joue surtout sur l'autorisation fine, la minimisation des données exposées et les limites de consommation.

## Chapitre 227 — BOLA (Broken Object Level Authorization)

1. **Définition.** Faille d'autorisation *au niveau objet* : accéder aux objets d'autrui faute de vérification de propriété (équivalent API de l'IDOR — chapitre 83).
2. **Famille.** API Security Top 10 (risque n°1). Contrôle d'accès cassé.
3. **Principe.** L'API identifie un objet par sa référence sans vérifier que l'appelant y a droit ; en changeant la référence, on accède à d'autres objets.
4. **Sous-types.** En lecture/écriture/suppression, sur identifiants séquentiels ou non.
5. **Exemple conceptuel.** Un endpoint renvoyant un objet par identifiant laisse accéder aux objets d'autres utilisateurs en variant l'identifiant.
6. **Impacts.** Fuite/altération massive de données, violation de confidentialité.
7. **Détection.** Accès à des objets hors périmètre, énumération d'identifiants, schémas anormaux, journaux API.
8. **Prévention.** **Vérification de propriété/autorisation par objet** côté serveur, deny by default, références liées à la session, tests d'autorisation.
9. ⚠️ **Erreur fréquente.** Se fier à l'imprévisibilité de l'identifiant plutôt qu'à un contrôle d'accès.
10. 🎯 **À retenir.** BOLA est le risque API n°1 : toujours vérifier que l'appelant a le droit sur *cet objet*.

## Chapitre 228 — BFLA (Broken Function Level Authorization)

1. **Définition.** Faille d'autorisation *au niveau fonction* : accéder à des opérations (souvent privilégiées/administratives) sans en avoir le droit.
2. **Famille.** API Security Top 10. Contrôle d'accès cassé (équivalent de l'élévation verticale).
3. **Principe.** Certaines fonctions (administration, actions sensibles) ne vérifient pas le rôle de l'appelant ; un utilisateur standard les invoque directement.
4. **Sous-types.** Accès à des endpoints d'administration, à des méthodes non autorisées, à des actions privilégiées.
5. **Exemple conceptuel.** Un endpoint d'administration est appelable par un compte standard faute de contrôle de rôle.
6. **Impacts.** Élévation de privilèges, actions non autorisées, compromission.
7. **Détection.** Appels à des fonctions privilégiées par des comptes non autorisés, journaux API, surveillance.
8. **Prévention.** **Contrôle d'autorisation par fonction** côté serveur, deny by default, séparation des rôles, tests d'autorisation, refus d'exposer des fonctions sans contrôle.
9. ⚠️ **Erreur fréquente.** Protéger les fonctions d'administration uniquement en les « cachant » de l'interface, sans contrôle serveur.
10. 🎯 **À retenir.** BFLA = fonctions privilégiées accessibles sans droit : vérifier le rôle pour *chaque* fonction, côté serveur.

## Chapitre 229 — Excessive data exposure

1. **Définition.** Une API renvoie *plus de données que nécessaire*, laissant au client le soin de filtrer (ce qui expose les champs sensibles).
2. **Famille.** API Security Top 10 (exposition de données).
3. **Principe.** L'API renvoie des objets complets (incluant des champs sensibles) en comptant sur le client pour n'afficher que l'utile ; l'attaquant lit la réponse brute.
4. **Sous-types.** Champs sensibles non filtrés, objets entiers renvoyés, données internes exposées.
5. **Exemple conceptuel.** Une réponse destinée à afficher un nom renvoie aussi des champs sensibles non utilisés par l'interface.
6. **Impacts.** Fuite de données sensibles, atteinte à la confidentialité.
7. **Détection.** Analyse des réponses (champs superflus/sensibles), revue de schéma, tests.
8. **Prévention.** **Filtrer côté serveur** (ne renvoyer que les champs nécessaires), schémas de réponse explicites, minimisation, revue, classification.
9. ⚠️ **Erreur fréquente.** Compter sur le client (interface) pour masquer des données pourtant transmises.
10. 🎯 **À retenir.** Ne jamais déléguer le filtrage au client : l'API ne doit renvoyer que les données strictement nécessaires.

## Chapitre 230 — Unrestricted resource consumption

1. **Définition.** Absence de limites sur la consommation de ressources via l'API, permettant l'épuisement ou la surfacturation.
2. **Famille.** API Security Top 10 (lié au rate limiting — chapitre 79).
3. **Principe.** Sans quotas/limites, l'attaquant déclenche des opérations massives ou coûteuses (requêtes, calculs, stockage), provoquant déni de service ou explosion des coûts cloud.
4. **Sous-types.** Volume de requêtes, opérations coûteuses, requêtes profondes (GraphQL — chapitre 126), consommation de stockage/calcul.
5. **Exemple conceptuel.** Des requêtes coûteuses répétées épuisent les ressources ou génèrent des coûts cloud importants.
6. **Impacts.** Déni de service, surcoûts, dégradation.
7. **Détection.** Volumes/coûts anormaux, requêtes coûteuses répétées, surveillance, alertes de coût.
8. **Prévention.** **Limitation de débit et quotas**, plafonds de complexité/taille, pagination, time-outs, contrôles de coût cloud, détection d'anomalies.
9. ⚠️ **Erreur fréquente.** Exposer des opérations coûteuses sans aucun plafond ni quota.
10. 🎯 **À retenir.** Sans limites, une API devient un levier de DoS et de surcoût : quotas, plafonds et contrôles de coût sont indispensables.

## Chapitre 231 — Unsafe consumption of APIs

1. **Définition.** Faire *trop confiance* aux données reçues d'API tierces/en amont, sans les valider.
2. **Famille.** API Security Top 10 / rupture de frontière de confiance (chapitre 80).
3. **Principe.** En consommant une API tierce, on suppose ses données sûres ; si cette API est compromise ou renvoie des données malveillantes, l'application aval les traite en confiance (injection, corruption).
4. **Sous-types.** Confiance excessive en réponses tierces, suivi aveugle de redirections, absence de validation des données amont.
5. **Exemple conceptuel.** Une application traite sans validation les données d'une API partenaire, propageant un contenu malveillant si celle-ci est compromise.
6. **Impacts.** Injection, corruption de données, propagation de compromission via la chaîne d'API.
7. **Détection.** Anomalies dans les données amont, comportements inattendus, surveillance des intégrations.
8. **Prévention.** **Valider et assainir** les données reçues des API tierces, traiter l'amont comme non fiable, time-outs/contrôles, surveillance des intégrations, segmentation.
9. ⚠️ **Erreur fréquente.** Considérer une API « partenaire » comme intrinsèquement fiable et ne pas valider ses réponses.
10. 🎯 **À retenir.** Les données d'une API tierce franchissent une frontière de confiance : les valider comme toute entrée non fiable.

## Chapitre 232 — Kubernetes RBAC abuse

1. **Définition.** Abus des droits (RBAC) au sein d'un cluster Kubernetes pour élever ses privilèges ou accéder à des ressources.
2. **Famille.** Conteneurs/orchestration (chapitre 47) / autorisation.
3. **Principe.** Le RBAC Kubernetes accorde des droits sur les ressources du cluster ; des permissions trop larges (créer des pods, lire des secrets, exécuter dans des pods) permettent l'élévation ou la prise de contrôle du cluster.
4. **Sous-types.** Droits excessifs sur pods/secrets/nœuds, comptes de service surprivilégiés, accès à l'API server.
5. **Exemple conceptuel.** Un compte de service au RBAC trop large peut lire des secrets ou créer des charges privilégiées.
6. **Impacts.** Élévation, accès aux secrets, prise de contrôle du cluster, mouvement latéral.
7. **Détection.** Analyse du RBAC (permissions effectives), actions anormales sur l'API server, journaux d'audit Kubernetes.
8. **Prévention.** **Moindre privilège RBAC**, comptes de service minimaux, restriction de l'accès à l'API server, audit, séparation, surveillance.
9. ⚠️ **Erreur fréquente.** Comptes de service par défaut surprivilégiés, RBAC permissif jamais audité.
10. 🎯 **À retenir.** Le RBAC Kubernetes est le contrôle d'accès du cluster : moindre privilège et audit des permissions effectives sont essentiels.

## Chapitre 233 — Container escape

1. **Définition.** Évasion d'un conteneur vers l'hôte (ou vers d'autres conteneurs), brisant l'isolation.
2. **Famille.** Conteneurs (chapitre 47) / élévation.
3. **Principe.** Un conteneur mal isolé (privilégié, capacités excessives, montages sensibles, vulnérabilité du runtime/noyau) permet à l'attaquant de « sortir » vers l'hôte, compromettant potentiellement toutes les charges hébergées.
4. **Sous-types.** Via conteneur privilégié, capacités/montages dangereux, vulnérabilité du runtime ou du noyau.
5. **Exemple conceptuel.** Un conteneur disposant de privilèges/montages excessifs accède à l'hôte sous-jacent.
6. **Impacts.** Compromission de l'hôte et des autres conteneurs, élévation, mouvement latéral.
7. **Détection.** Comportements d'évasion, accès anormaux à l'hôte, EDR/runtime security, audit.
8. **Prévention.** **Conteneurs non privilégiés**, capacités minimales, pas de montages sensibles, security contexts/policies, isolation renforcée, runtime à jour, durcissement du noyau, admission control.
9. ⚠️ **Erreur fréquente.** Exécuter des conteneurs en mode privilégié ou avec des montages hôte sensibles.
10. 🎯 **À retenir.** Un conteneur n'est pas une frontière de sécurité parfaite : minimiser privilèges/capacités/montages évite l'évasion vers l'hôte.

## Chapitre 234 — Image vulnérable

1. **Définition.** Image de conteneur contenant des composants vulnérables ou des configurations dangereuses.
2. **Famille.** Conteneurs / dépendances vulnérables (chapitre 71).
3. **Principe.** Les images embarquent un système et des dépendances ; si ceux-ci sont obsolètes/vulnérables (ou contiennent des secrets), chaque conteneur lancé hérite de ces faiblesses.
4. **Sous-types.** Dépendances vulnérables, image obsolète, secrets embarqués, configuration non durcie.
5. **Exemple conceptuel.** Une image basée sur un système non patché déploie partout les mêmes vulnérabilités.
6. **Impacts.** Exploitation à l'échelle des déploiements, fuite de secrets, point d'entrée.
7. **Détection.** **Scan d'images** (vulnérabilités, secrets), inventaire, surveillance.
8. **Prévention.** Images **minimales** et à jour, scan en CI et au registre, SBOM, base d'images de confiance, durcissement, pas de secrets en image, mises à jour régulières.
9. ⚠️ **Erreur fréquente.** Déployer des images jamais re-scannées ni mises à jour (vulnérabilités héritées en masse).
10. 🎯 **À retenir.** Une image vulnérable se réplique à chaque conteneur : images minimales, scannées et à jour, sans secrets.

## Chapitre 235 — Registre exposé

1. **Définition.** Registre d'images de conteneurs accessible/modifiable indûment.
2. **Famille.** Conteneurs / supply chain.
3. **Principe.** Un registre exposé permet de *lire* des images (fuite de code/secrets) ou d'y *pousser* des images malveillantes ensuite déployées en confiance (empoisonnement de la chaîne).
4. **Sous-types.** Lecture publique (fuite), écriture non contrôlée (empoisonnement), absence de contrôle d'intégrité.
5. **Exemple conceptuel.** Un registre accessible en écriture permet de remplacer une image légitime par une version piégée.
6. **Impacts.** Fuite de code/secrets, déploiement d'images malveillantes, compromission de la supply chain.
7. **Détection.** Accès/poussées anormaux, modifications d'images, surveillance du registre, vérification d'intégrité.
8. **Prévention.** Registres **privés** et authentifiés, contrôle d'accès strict, **signature et vérification d'images**, scan, journalisation, moindre privilège.
9. ⚠️ **Erreur fréquente.** Registre accessible largement, sans signature ni vérification des images déployées.
10. 🎯 **À retenir.** Un registre exposé empoisonne la chaîne : accès strict + signature/vérification des images sont indispensables.

## Chapitre 236 — CI/CD compromise

1. **Définition.** Compromission de la chaîne d'intégration/déploiement continus (chapitre 48).
2. **Famille.** Supply chain logicielle (à fort effet de levier).
3. **Principe.** La CI/CD a des droits puissants (déployer en production) et manipule code et secrets ; la compromettre permet d'injecter du code malveillant dans *tout ce qui est déployé*, « légitimement ».
4. **Sous-types.** Vol de secrets de pipeline, pipeline poisoning (chapitre 237), abus de tokens CI, compromission du build (chapitre 241).
5. **Exemple conceptuel.** Un accès au système de CI/CD permet d'altérer le processus de build pour insérer une charge dans les artefacts produits.
6. **Impacts.** Distribution massive de code malveillant, accès production, compromission profonde et de confiance.
7. **Détection.** Modifications anormales des pipelines/configurations, usage anormal de secrets/tokens, intégrité des artefacts, surveillance.
8. **Prévention.** **Moindre privilège** des pipelines, gestion des secrets dédiée, isolation des runners, revue de code obligatoire, **signature/provenance** (SLSA), SBOM, journalisation.
9. ⚠️ **Erreur fréquente.** Pipelines aux droits de production illimités, secrets en clair, runners non isolés.
10. 🎯 **À retenir.** Compromettre la CI/CD = empoisonner la source : moindre privilège, isolation, secrets gérés et provenance/signature sont critiques.

## Chapitre 237 — Pipeline poisoning

1. **Définition.** Injection de code/étapes malveillants *dans le processus de build* lui-même.
2. **Famille.** Supply chain / CI/CD.
3. **Principe.** En modifiant la configuration de pipeline, des scripts de build, ou en injectant via une dépendance/entrée de build, l'attaquant fait produire des artefacts piégés tout en gardant l'apparence d'un build légitime.
4. **Sous-types.** Modification de la définition de pipeline, injection via dépendances de build, abus d'entrées contrôlables du pipeline (poisoned pipeline execution).
5. **Exemple conceptuel.** Une étape ajoutée au pipeline insère une charge dans l'artefact final, sans alerter.
6. **Impacts.** Artefacts compromis distribués, accès, persistance, compromission de confiance.
7. **Détection.** Modifications de pipeline/scripts inattendues, écarts d'intégrité des artefacts, surveillance, revue.
8. **Prévention.** Contrôle/validation des définitions de pipeline, isolation des étapes, **provenance/signature** (SLSA), revue obligatoire, moindre privilège, builds reproductibles.
9. ⚠️ **Erreur fréquente.** Laisser modifier les définitions de pipeline sans revue ni contrôle d'intégrité des artefacts.
10. 🎯 **À retenir.** Le pipeline poisoning insère le mal dans le build : revue, isolation et provenance/signature des artefacts sont les parades.

## Chapitre 238 — Dependency confusion

1. **Définition.** Attaque où un paquet *public* malveillant, portant le nom d'un paquet *interne*, est récupéré à la place de ce dernier par le gestionnaire de dépendances.
2. **Famille.** Supply chain logicielle (chapitre 81).
3. **Principe.** Si le gestionnaire de paquets privilégie (ou peut atteindre) un dépôt public, un attaquant publie un paquet public au même nom qu'un paquet interne, avec une version supérieure ; le build récupère le paquet malveillant.
4. **Sous-types.** Selon l'écosystème de paquets et la configuration des dépôts.
5. **Exemple conceptuel.** Un nom de paquet interne, publié publiquement par un attaquant avec une version élevée, est résolu à la place du paquet interne légitime.
6. **Impacts.** Exécution de code malveillant dans le build/les déploiements, compromission.
7. **Détection.** Résolution de paquets depuis des sources inattendues, écarts de version/source, surveillance des dépendances.
8. **Prévention.** **Dépôts internes prioritaires/exclusifs** (scoping, namespaces réservés), verrouillage des sources et versions (lockfiles), vérification d'intégrité, allowlist de paquets, SBOM.
9. ⚠️ **Erreur fréquente.** Configuration de paquets autorisant la résolution publique pour des noms internes.
10. 🎯 **À retenir.** La dependency confusion exploite la résolution de noms : prioriser/réserver les dépôts internes et verrouiller sources et versions.

## Chapitre 239 — Typosquatting package

1. **Définition.** Publication de paquets malveillants aux noms proches de paquets populaires (fautes de frappe), pour piéger les développeurs.
2. **Famille.** Supply chain logicielle.
3. **Principe.** L'attaquant mise sur l'erreur de saisie ou la confusion ; un développeur installe par mégarde le paquet piégé, dont le nom imite un paquet légitime.
4. **Sous-types.** Variantes de nom (fautes, tirets, ordre), imitation de paquets populaires.
5. **Exemple conceptuel.** Un paquet au nom presque identique à une bibliothèque connue contient une charge malveillante.
6. **Impacts.** Exécution de code malveillant à l'installation/au build, compromission.
7. **Détection.** Dépendances aux noms suspects, écarts par rapport aux paquets officiels, scan, surveillance.
8. **Prévention.** Allowlist de paquets, vérification des noms officiels, verrouillage (lockfiles), SBOM, dépôts internes filtrés, revue des dépendances.
9. ⚠️ **Erreur fréquente.** Installer un paquet sans vérifier son nom/source exacts.
10. 🎯 **À retenir.** Le typosquatting piège par la ressemblance des noms : vérifier les sources officielles et verrouiller les dépendances.

## Chapitre 240 — Malicious package

1. **Définition.** Paquet/dépendance intentionnellement malveillant (au-delà du typosquatting/dependency confusion), incluant les paquets légitimes *détournés*.
2. **Famille.** Supply chain logicielle.
3. **Principe.** Un paquet contient du code malveillant dès l'origine, ou un paquet légitime est compromis (compte mainteneur piraté, mise à jour piégée), distribuant le mal à tous ses utilisateurs.
4. **Sous-types.** Paquet malveillant dès l'origine, paquet légitime compromis (mainteneur/mise à jour), charge déclenchée à l'installation ou à l'exécution.
5. **Exemple conceptuel.** Une mise à jour d'une bibliothèque répandue, compromise à la source, distribue une charge à ses utilisateurs.
6. **Impacts.** Compromission massive et de confiance, exécution de code, exfiltration.
7. **Détection.** Comportements anormaux de dépendances, analyse de composition (SCA), surveillance des mises à jour, intégrité.
8. **Prévention.** SCA, **SBOM**, verrouillage et revue des mises à jour, vérification d'intégrité/signature, dépôts internes filtrés, minimisation des dépendances, surveillance des avis.
9. ⚠️ **Erreur fréquente.** Mettre à jour automatiquement des dépendances sans revue ni contrôle d'intégrité.
10. 🎯 **À retenir.** Un paquet de confiance peut devenir malveillant : SBOM, SCA, verrouillage et revue des mises à jour réduisent le risque.

## Chapitre 241 — Build system compromise

1. **Définition.** Compromission directe du *système de build* (serveurs, outils, environnement) qui produit les artefacts.
2. **Famille.** Supply chain logicielle (la plus profonde).
3. **Principe.** En contrôlant le système qui compile/assemble, l'attaquant peut altérer les artefacts produits *même si* le code source est sain — d'où la nécessité de garantir l'intégrité et la provenance du build.
4. **Sous-types.** Compromission des serveurs de build, des outils/dépendances de build, de l'environnement d'exécution.
5. **Exemple conceptuel.** Un système de build compromis insère une modification dans l'artefact final, indépendamment du code source.
6. **Impacts.** Artefacts piégés et signés « légitimement », compromission massive et difficile à détecter.
7. **Détection.** Écarts d'intégrité, builds non reproductibles, anomalies de l'environnement de build, surveillance.
8. **Prévention.** **Builds isolés/éphémères et reproductibles**, **provenance** (SLSA), intégrité de l'environnement, moindre privilège, durcissement, journalisation, vérification des artefacts.
9. ⚠️ **Erreur fréquente.** Faire confiance à l'artefact « parce que le code source est revu », sans garantir l'intégrité du build.
10. 🎯 **À retenir.** Un build compromis produit du mal à partir d'un code sain : builds reproductibles et provenance (SLSA) sont la garantie.

## Chapitre 242 — Signature et intégrité logicielle

**Définition.** Mécanismes garantissant qu'un artefact (paquet, image, binaire) provient bien de sa source légitime et n'a pas été altéré.

**Principe.** La **signature** (cryptographique) atteste l'origine ; la **vérification** côté consommateur garantit l'intégrité. La **provenance** (qui a produit quoi, comment, à partir de quelles entrées — formalisée par SLSA) étend cette garantie à toute la chaîne. C'est la défense de fond contre la supply chain : ne déployer/exécuter que ce qui est signé et vérifié.

🧭 **Taxonomie** — Antidote transversal des chapitres 235–241 ; relie intégrité (chapitre 81), CI/CD et déploiement.

⚠️ **Erreur fréquente** — Signer sans *vérifier* à la consommation (la signature seule ne protège pas si personne ne contrôle).

🎯 **À retenir** — Signer *et vérifier* les artefacts, et tracer leur provenance (SLSA), est la parade structurante contre la compromission de la supply chain.

## Chapitre 243 — SBOM (Software Bill of Materials)

**Définition.** Inventaire détaillé des composants logiciels (dépendances, versions, origines) d'une application — sa « liste d'ingrédients ».

**Principe.** On ne peut sécuriser que ce qu'on connaît (chapitre 33). Le SBOM permet, lorsqu'une vulnérabilité (ou un paquet malveillant) est révélé, de savoir *immédiatement* si on est concerné et où. Il est le socle de la gestion des dépendances (chapitre 71), de la SCA et de la réponse aux incidents supply chain.

🔧 **Exemple concret** — À l'annonce d'une vulnérabilité critique dans une bibliothèque répandue, le SBOM indique en minutes quels systèmes l'embarquent, au lieu de jours de recherche.

🧭 **Taxonomie** — Inventaire au niveau logiciel ; pendant de la gestion des actifs (chapitre 33) côté code.

🎯 **À retenir** — Le SBOM transforme « sommes-nous touchés ? » d'une enquête longue en une requête immédiate : c'est un prérequis de la sécurité de la supply chain.

## Chapitre 244 — Secrets management

**Définition.** Gestion centralisée et sécurisée des secrets (mots de passe, clés, jetons, certificats) tout au long de leur cycle de vie.

**Principe.** Antidote transversal à l'exposition de secrets (chapitres 77, 221, 222). Un gestionnaire de secrets (coffre-fort) : stocke les secrets chiffrés hors du code, contrôle/audite les accès, distribue les secrets de façon dynamique (idéalement à durée de vie courte), assure la **rotation** et la **révocation** rapides. Couplé au secrets scanning (détecter les fuites) et au moindre privilège.

🧭 **Taxonomie** — Défense centrale du cloud, de la CI/CD et des conteneurs ; relie identité, configuration et supply chain.

⚠️ **Erreur fréquente** — Déployer un coffre à secrets tout en laissant subsister des secrets en dur dans le code/l'IaC.

🎯 **À retenir** — Centraliser, chiffrer, faire tourner et auditer les secrets (et scanner les fuites) coupe l'un des chemins d'attaque les plus directs.

---

> **Fin du Volume 7/8.**
>
> Vous savez sécuriser les surfaces modernes : cloud (responsabilité partagée, IAM, configuration, secrets, métadonnées, élévation/lateral movement), API (autorisation par objet/fonction, minimisation des données, limites, consommation sûre), conteneurs/Kubernetes (RBAC, évasion, images, registres), et supply chain (CI/CD, pipeline poisoning, dependency confusion, typosquatting, paquets/build compromis, signature/provenance, SBOM, gestion des secrets).
>
> **Suite — Volume 8 (final) : Parties 11 à 13 + Annexes** — Détection/SOC/réponse à incident ; taxonomie des défenses ; synthèse transversale (classer une attaque inconnue, relier attaque↔vulnérabilité↔contrôle↔détection, prioriser, carte mentale, erreurs de raisonnement, glossaire) ; et les annexes (glossaire, tableaux de correspondance, fiches réflexes, métiers cyber, méthode d'apprentissage légal, bibliographie).


---

# Taxonomie de la cybersécurité — Volume 8/8 (final)

> Parties 11 à 13 + Annexes
>
> Ce volume ferme la boucle du fil rouge : après *comprendre, classer, relier, défendre*, on traite **répondre** (Partie 11), on consolide la **taxonomie des défenses** (Partie 12), puis on apprend à **raisonner** transversalement (Partie 13). Les annexes fournissent les outils de référence (glossaire, tableaux de correspondance, fiches réflexes, métiers, méthode d'apprentissage légal, bibliographie).

---

# Partie 11 — Détection, SOC et réponse à incident

> Le SOC (Security Operations Center) et la réponse à incident incarnent la posture *assume breach* : puisque la prévention échouera un jour, il faut *voir* (détection) et *agir* (réponse). On suit ici le cycle de vie d'un incident, du signal brut au retour d'expérience. Cadre de référence : NIST CSF *Detect / Respond / Recover*, et le cycle de réponse à incident (préparation, détection/analyse, confinement/éradication/rétablissement, post-incident).

## Chapitre 245 — Événement, alerte, incident

**Définition.** Trois niveaux d'objets du SOC, à ne pas confondre.

- **Événement** : tout fait journalisé (une connexion, une requête). Neutre, massif.
- **Alerte** : un événement (ou une corrélation) jugé *suspect* par une règle/un modèle, qui mérite examen.
- **Incident** : une alerte *confirmée* comme atteinte (ou menace) réelle à la sécurité, qui déclenche la réponse.

**Principe.** Le SOC filtre un déluge d'événements → quelques alertes → encore moins d'incidents réels. La qualité du filtrage (réduire le bruit sans rater le signal) est l'enjeu central.

🧭 **Taxonomie** — Pipeline : événements (logs) → alertes (détection) → incidents (qualification) → réponse.

🎯 **À retenir** — Tout incident est un événement, mais l'immense majorité des événements ne sont pas des incidents. Le travail du SOC est ce tri.

## Chapitre 246 — Faux positif, vrai positif, faux négatif

**Définition.** Vocabulaire de la qualité de détection.

- **Vrai positif** : une alerte correspondant à une vraie menace (bonne détection).
- **Faux positif** : une alerte déclenchée à tort (bruit) — coûte du temps d'analyse.
- **Faux négatif** : une menace réelle *non* détectée (le plus dangereux) — angle mort.
- **Vrai négatif** : absence d'alerte sur une activité légitime (normal).

**Principe.** Il y a un arbitrage : durcir la détection réduit les faux négatifs mais augmente les faux positifs (et la fatigue d'alerte), et inversement. L'objectif est de maximiser les vrais positifs tout en maîtrisant le bruit.

⚠️ **Erreur fréquente** — Trop d'alertes (faux positifs) noient les analystes et masquent les vraies menaces (fatigue d'alerte). Le réglage fin (tuning) est continu.

🎯 **À retenir** — Le faux négatif est le plus dangereux (menace ratée) ; le faux positif use les équipes. Le réglage des détections arbitre constamment entre les deux.

## Chapitre 247 — IOC, IOA, TTP

**Définition.** Trois niveaux d'indicateurs de menace, par ordre de valeur croissante.

- **IOC (Indicator of Compromise)** : trace technique d'une compromission (adresse, condensat de fichier, domaine malveillant). Concret mais *éphémère* (l'attaquant change facilement).
- **IOA (Indicator of Attack)** : signe d'un *comportement* d'attaque en cours (séquence d'actions), indépendant des artefacts précis.
- **TTP (Tactics, Techniques, Procedures)** : les *méthodes* de l'attaquant (le « comment » durable), formalisées par MITRE ATT&CK. Le plus stable et le plus précieux.

**Principe : la « pyramide de la douleur ».** Bloquer un IOC gêne peu l'attaquant (il le change) ; détecter ses TTP l'oblige à changer ses méthodes — bien plus coûteux pour lui.

🧭 **Taxonomie** — IOC (artefact) < IOA (comportement) < TTP (méthode). La détection mûre vise les TTP (ATT&CK).

🎯 **À retenir** — Détecter au niveau TTP (comportements/méthodes) fait bien plus mal à l'attaquant que bloquer des IOC volatils.

## Chapitre 248 — Log source

**Définition.** Toute origine de journaux alimentant la détection (postes, serveurs, réseau, applications, cloud, identité, EDR).

**Principe.** La détection ne vaut que par ses *sources* : sans les bons journaux (authentification, processus, réseau, cloud), des pans entiers d'attaque restent invisibles. Le choix et la couverture des sources déterminent ce que le SOC peut voir. Notions : complétude, fiabilité, horodatage synchronisé, centralisation.

🧭 **Taxonomie** — Matière première de la Partie 11 ; relie journalisation (chapitre 26) et logging insuffisant (chapitre 78).

🎯 **À retenir** — Pas de bonne source, pas de détection : la couverture des log sources est le socle du SOC.

## Chapitre 249 — SIEM

**Définition.** *Security Information and Event Management* : plateforme centralisant les journaux, les corrélant et générant des alertes.

**Principe.** Le SIEM agrège les sources, normalise, corrèle (relier des événements épars en un scénario), applique des règles de détection, et sert de base à l'investigation et au reporting. C'est le « cerveau » de corrélation du SOC.

🧭 **Taxonomie** — Cœur de la détection centralisée ; consomme les log sources, alimente le triage et l'investigation.

⚠️ **Erreur fréquente** — Déployer un SIEM sans sources pertinentes ni règles ajustées : un coûteux entrepôt de logs qui ne détecte rien.

🎯 **À retenir** — Le SIEM corrèle les sources pour transformer des événements épars en alertes exploitables — à condition d'être bien alimenté et réglé.

## Chapitre 250 — EDR

**Définition.** *Endpoint Detection and Response* : agent sur les postes/serveurs qui détecte les comportements malveillants et permet d'y répondre (isolation, investigation).

**Principe.** Au-delà de l'antivirus (signatures), l'EDR observe le *comportement* (processus, mémoire, actions) — clé contre le fileless, les LOLBins et les TTP. Il permet aussi des actions de réponse (isoler une machine, tuer un processus) et fournit la télémétrie pour l'investigation.

🧭 **Taxonomie** — Détection/réponse au niveau hôte ; complément du SIEM (vue centrale) et du NDR (vue réseau). Brique du XDR (corrélation multi-domaines).

🎯 **À retenir** — L'EDR voit le comportement sur l'hôte (pas seulement les fichiers) : indispensable contre les attaques furtives modernes.

## Chapitre 251 — NDR

**Définition.** *Network Detection and Response* : détection des menaces par l'analyse du *trafic réseau*.

**Principe.** Le NDR observe les flux (y compris est-ouest, internes) pour repérer scans, mouvement latéral, C2, exfiltration, tunneling — souvent invisibles côté hôte. Il complète l'EDR (qui peut être absent de certains équipements : IoT, OT).

🧭 **Taxonomie** — Détection au niveau réseau ; complément de l'EDR (hôte) et du SIEM (central). Particulièrement utile contre la Partie 7.

🎯 **À retenir** — Le NDR voit ce qui circule, y compris là où il n'y a pas d'agent (IoT/OT) : essentiel pour repérer mouvement latéral et exfiltration.

## Chapitre 252 — SOAR

**Définition.** *Security Orchestration, Automation and Response* : plateforme automatisant et orchestrant les tâches de réponse (playbooks).

**Principe.** Le SOAR enchaîne automatiquement des actions répétitives (enrichir une alerte, isoler une machine, bloquer un indicateur) selon des playbooks, réduisant le temps de réponse et la charge des analystes. Il orchestre les outils entre eux.

🧭 **Taxonomie** — Couche d'automatisation au-dessus du SIEM/EDR/NDR ; accélère le cycle détection→réponse.

⚠️ **Erreur fréquente** — Automatiser des réponses agressives sans garde-fous (risque d'auto-déni de service).

🎯 **À retenir** — Le SOAR automatise et orchestre la réponse : il démultiplie les analystes, à condition de playbooks sûrs et testés.

## Chapitre 253 — Cas d'usage SOC

**Définition.** Un *use case* est un scénario de menace concret que le SOC s'organise pour détecter (par ex. « tentative de password spraying », « exfiltration via DNS »).

**Principe.** On ne détecte pas « tout » : on définit des cas d'usage prioritaires (selon les menaces et les actifs), pour lesquels on identifie les sources, écrit les règles, et prépare la réponse. Les cas d'usage relient menace → détection → réaction. On les cartographie souvent sur ATT&CK pour mesurer la couverture.

🧭 **Taxonomie** — Unité de pilotage de la détection ; relie CTI (menaces), log sources, règles et playbooks.

🎯 **À retenir** — Le cas d'usage structure la détection autour de menaces concrètes : il évite le « tout détecter » illusoire et mesure la couverture.

## Chapitre 254 — Règle de détection

**Définition.** Logique (signature, corrélation, modèle) qui transforme des événements en alerte lorsqu'un schéma suspect apparaît.

**Principe.** Les règles vont de la signature simple (un indicateur connu) à la corrélation comportementale (séquence d'actions) et à l'analyse statistique/ML (anomalies). Elles doivent être *ajustées* (réduire faux positifs/négatifs) et *maintenues* (les menaces évoluent). Des formats partagés (par ex. règles ouvertes type Sigma/Yara) facilitent la mutualisation.

🧭 **Taxonomie** — Brique opérationnelle du cas d'usage ; vise idéalement le niveau TTP (chapitre 247).

🎯 **À retenir** — Une bonne règle détecte le comportement, pas seulement l'artefact, et se règle/maintient en continu.

## Chapitre 255 — Triage

**Définition.** Première étape de traitement d'une alerte : évaluer rapidement sa gravité et sa probabilité pour décider de la suite.

**Principe.** Face au volume d'alertes, le triage priorise : écarter le bruit évident, escalader le sérieux, enrichir (contexte, IOC, actif concerné). C'est le filtre d'entrée du processus de réponse.

🧭 **Taxonomie** — Première étape du cycle de réponse ; précède la qualification (chapitre 256).

🎯 **À retenir** — Le triage trie vite pour concentrer l'effort sur ce qui compte : il protège les analystes de la noyade.

## Chapitre 256 — Qualification

**Définition.** Analyse approfondie d'une alerte triée pour confirmer (ou infirmer) qu'il s'agit d'un incident, et en déterminer la nature/portée.

**Principe.** On rassemble le contexte (sources, télémétrie, IOC/IOA), on reconstitue ce qui se passe, et on décide : faux positif (clôture) ou incident (escalade et réponse). La qualification détermine la gravité et le périmètre initial.

🧭 **Taxonomie** — Transforme une alerte en incident qualifié ; précède l'escalade et le confinement.

🎯 **À retenir** — La qualification confirme la réalité et la portée de la menace : c'est la bascule alerte → incident.

## Chapitre 257 — Escalade

**Définition.** Transmission d'un incident qualifié au niveau/équipe approprié (analystes seniors, réponse à incident, gestion de crise) selon sa gravité.

**Principe.** Tout incident n'exige pas la même réponse ; l'escalade aiguille vers les bonnes compétences et déclenche, si besoin, la cellule de crise (chapitre 39). Des critères clairs (gravité, périmètre, impact) évitent les hésitations sous pression.

🧭 **Taxonomie** — Charnière entre détection (niveaux SOC) et réponse/gestion de crise.

🎯 **À retenir** — L'escalade met le bon niveau d'expertise sur le bon incident, au bon moment : des critères définis à froid l'objectivent.

## Chapitre 258 — Investigation

**Définition.** Analyse détaillée d'un incident pour comprendre *ce qui s'est passé* : vecteur d'entrée, actions, portée, persistance, données touchées.

**Principe.** L'investigation reconstitue le scénario d'attaque (souvent via ATT&CK), identifie tous les systèmes/compte touchés et les mécanismes de persistance — préalable indispensable à un confinement et une éradication *complets*. Elle s'appuie sur la télémétrie (EDR/NDR/SIEM) et le forensic (chapitre 263).

⚠️ **Erreur fréquente** — Réagir avant d'avoir compris la portée : on confine un symptôme en laissant des accès cachés.

🧭 **Taxonomie** — Sous-tend confinement, éradication et rétablissement ; alimente le post-mortem.

🎯 **À retenir** — Comprendre toute la portée *avant* d'agir évite une éradication incomplète et un retour de l'attaquant.

## Chapitre 259 — Containment (confinement)

**Définition.** Mesures pour *limiter la propagation* et l'impact d'un incident, sans nécessairement tout éradiquer immédiatement.

**Principe.** On isole les systèmes/comptes compromis (déconnexion réseau, désactivation de comptes, blocage de flux) pour stopper l'hémorragie. Confinement *court terme* (urgence) puis *long terme* (stabilisation). À équilibrer avec la préservation des preuves (forensic) et la continuité d'activité.

⚠️ **Erreur fréquente** — Confiner brutalement en détruisant les preuves, ou alerter l'attaquant trop tôt (qui accélère/détruit).

🧭 **Taxonomie** — Étape *Respond* ; précède l'éradication.

🎯 **À retenir** — Le confinement arrête la propagation ; il s'équilibre avec la préservation des preuves et la continuité.

## Chapitre 260 — Eradication

**Définition.** Suppression *complète* de la présence de l'attaquant : malwares, comptes/portes dérobées, mécanismes de persistance.

**Principe.** Sur la base d'une investigation complète, on élimine *tout* (pas seulement la charge visible) : backdoors, comptes créés, tâches, implants, secrets compromis (rotation, dont krbtgt si AD). Une éradication partielle = retour de l'attaquant.

⚠️ **Erreur fréquente** — Nettoyer le malware visible en laissant des accès de persistance (backdoor, shadow credentials, golden ticket).

🧭 **Taxonomie** — Étape *Respond* ; suit le confinement, précède le rétablissement.

🎯 **À retenir** — L'éradication doit être *exhaustive* (toute la persistance) sous peine de réinfection : d'où l'importance de l'investigation préalable.

## Chapitre 261 — Recovery (rétablissement)

**Définition.** Remise en service sécurisée des systèmes et données après éradication.

**Principe.** On restaure (sauvegardes saines), on durcit (corriger ce qui a permis l'intrusion), on surveille étroitement (l'attaquant peut tenter de revenir), et on rétablit progressivement l'activité. La restauration s'appuie sur des sauvegardes *vérifiées* (chapitre 28).

⚠️ **Erreur fréquente** — Restaurer à partir d'une sauvegarde elle-même compromise, ou rétablir sans corriger la faille initiale (réintrusion immédiate).

🧭 **Taxonomie** — Étape *Recover* ; relie sauvegarde/PRA (chapitres 28, 267).

🎯 **À retenir** — Le rétablissement remet en service *sainement* : sauvegardes vérifiées, correction de la cause, surveillance renforcée.

## Chapitre 262 — Lessons learned

**Définition.** Analyse rétrospective d'un incident pour en tirer des améliorations durables (techniques, processus, organisation).

**Principe.** Sans retour d'expérience, les mêmes incidents se répètent. On documente ce qui s'est passé, ce qui a bien/mal fonctionné, et on en tire des actions concrètes (nouvelles détections, correctifs, procédures, formation). C'est le moteur d'amélioration continue du SOC.

🧭 **Taxonomie** — Étape post-incident ; relie au post-mortem (chapitre 269) et boucle vers la préparation.

🎯 **À retenir** — Un incident non analysé est un incident à moitié subi : les lessons learned transforment la douleur en progrès.

## Chapitre 263 — Forensic

**Définition.** *Investigation numérique légale* : collecte, préservation et analyse rigoureuses de preuves numériques, exploitables y compris en justice.

**Principe.** Le forensic reconstitue les faits à partir d'artefacts (disques, mémoire, journaux) en garantissant l'*intégrité* et la *traçabilité* des preuves (chaîne de conservation — chapitre 265). Il sert l'investigation, l'attribution, et d'éventuelles suites légales/réglementaires.

🧭 **Taxonomie** — Appui de l'investigation (chapitre 258) ; exige rigueur de preuve (chapitres 264–265).

🎯 **À retenir** — Le forensic produit des preuves fiables et défendables : il impose rigueur et préservation de l'intégrité.

## Chapitre 264 — Timeline

**Définition.** Reconstitution chronologique des événements d'un incident (qui, quoi, quand, dans quel ordre).

**Principe.** La timeline relie les artefacts épars en un *récit* cohérent de l'attaque, du point d'entrée à l'impact. Elle exige des horodatages fiables et synchronisés (sinon les corrélations sont fausses). C'est l'épine dorsale de l'investigation et du forensic.

⚠️ **Erreur fréquente** — Horloges non synchronisées entre sources, rendant la chronologie incohérente.

🧭 **Taxonomie** — Outil central de l'investigation/forensic ; dépend de la qualité des log sources (horodatage).

🎯 **À retenir** — La timeline raconte l'attaque dans l'ordre : sans horodatage fiable et synchronisé, elle s'effondre.

## Chapitre 265 — Chaîne de conservation (chain of custody)

**Définition.** Traçabilité documentée de chaque preuve numérique : qui l'a collectée, manipulée, transférée, quand et comment.

**Principe.** Pour qu'une preuve soit recevable et crédible, on doit prouver qu'elle n'a pas été altérée depuis sa collecte. La chaîne de conservation documente chaque manipulation et garantit l'intégrité (empreintes, copies de travail, originaux préservés).

🧭 **Taxonomie** — Exigence du forensic (chapitre 263) ; condition de la valeur probante.

🎯 **À retenir** — Sans chaîne de conservation, une preuve perd sa valeur : documenter chaque manipulation est impératif.

## Chapitre 266 — Gestion de crise

**Définition.** Pilotage organisationnel d'un incident majeur (rappel du chapitre 39, côté opérationnel du SOC/IR).

**Principe.** Quand l'incident dépasse le SOC, la cellule de crise coordonne décisions, communication, continuité et aspects juridiques/réglementaires, sous pression. Elle s'appuie sur des rôles, des procédures et des canaux *préparés à froid* (et hors du SI potentiellement compromis).

🧭 **Taxonomie** — Niveau de pilotage au-dessus de la réponse technique ; relie PRA/PCA (chapitre 267) et communication (chapitre 268).

🎯 **À retenir** — La gestion de crise coordonne au-delà de la technique : préparée à l'avance, elle évite l'improvisation sous pression.

## Chapitre 267 — PRA / PCA

**Définition.**
- **PCA (Plan de Continuité d'Activité)** : maintenir les activités essentielles *pendant* la crise (avec des moyens dégradés/alternatifs).
- **PRA (Plan de Reprise d'Activité)** : *rétablir* les systèmes après le sinistre, dans des délais et avec des pertes de données maîtrisés.

**Notions clés.** **RTO** (durée de reprise visée) et **RPO** (perte de données acceptable) dimensionnent le dispositif. Le PRA repose sur des sauvegardes vérifiées (chapitre 28) et doit être *testé* régulièrement.

⚠️ **Erreur fréquente** — PRA jamais testé, RTO/RPO théoriques irréalistes le jour J.

🧭 **Taxonomie** — Résilience (chapitre 28) au niveau organisationnel ; pilier de la fonction *Recover*.

🎯 **À retenir** — PCA = tenir pendant ; PRA = se relever après. Tous deux doivent être chiffrés (RTO/RPO) et *testés*.

## Chapitre 268 — Communication de crise

**Définition.** Gestion des messages (internes, clients, partenaires, autorités, public) pendant et après un incident majeur.

**Principe.** Une mauvaise communication aggrave une crise (panique, perte de confiance, sanctions). Il faut des messages préparés, des porte-parole désignés, le respect des obligations de notification (réglementaires : violations de données, etc.), et une coordination avec le juridique. La transparence maîtrisée préserve la confiance.

⚠️ **Erreur fréquente** — Communiquer trop tôt/faux, ou via des canaux compromis ; ignorer les obligations légales de notification.

🧭 **Taxonomie** — Volet de la gestion de crise (chapitres 39, 266) ; à préparer à froid.

🎯 **À retenir** — La communication de crise se prépare à l'avance : messages, porte-parole, obligations de notification et canaux sûrs.

## Chapitre 269 — REX et amélioration continue

**Définition.** Le *retour d'expérience* (REX) et le post-mortem institutionnalisent l'apprentissage tiré des incidents (et des exercices).

**Principe.** Au-delà des « lessons learned » d'un incident, le REX nourrit un cycle d'amélioration continue : mise à jour des détections, des procédures, de l'architecture, de la formation. Idéalement *sans blâme* (blameless), pour favoriser l'honnêteté et l'apprentissage réel.

🧭 **Taxonomie** — Boucle de rétroaction reliant *Respond/Recover* à la préparation (*Govern/Identify/Protect/Detect*).

🎯 **À retenir** — La sécurité progresse par boucles d'apprentissage : un REX sans blâme transforme chaque incident en amélioration durable.

---

# Partie 12 — Taxonomie des défenses

> Cette partie classe les contrôles défensifs et les *relie aux attaques* qu'ils contrent. C'est le pendant « D3FEND » du cours : à chaque famille d'attaque, une famille de défenses. On peut classer chaque défense par fonction (préventive/détective/corrective — chapitre 8) et par couche (hôte, réseau, identité, données, application, organisation).

## Chapitre 270 — Hardening

**Définition.** Durcissement : réduire la vulnérabilité d'un système par configuration (rappel du chapitre 21).
**Contre quoi.** Exploitation de services, mauvaise configuration, réduction de surface.
**Principe.** Appliquer des référentiels (CIS), désactiver l'inutile, sécuriser les réglages par défaut.
🎯 **À retenir** — Le durcissement ferme les portes ouvertes « par défaut » ; base de toute défense préventive.

## Chapitre 271 — Patch management

**Définition.** Processus d'application maîtrisée des correctifs de sécurité.
**Contre quoi.** Exploitation de vulnérabilités connues (services exposés, vers).
**Principe.** Prioriser selon gravité × exploitabilité × exposition (CVSS/EPSS/KEV — chapitre 32), tester, déployer vite ce qui est exposé.
⚠️ **Erreur fréquente** — Retarder les patchs des actifs exposés (porte d'entrée n°1).
🎯 **À retenir** — Patcher *vite et bien* ce qui est exposé est l'un des contrôles les plus rentables.

## Chapitre 272 — Antivirus / EDR

**Définition.** Protection des hôtes par signatures (antivirus) et par comportement/réponse (EDR — chapitre 250).
**Contre quoi.** Malwares, fileless, LOLBins, TTP sur l'hôte.
**Principe.** L'EDR ajoute la détection comportementale et la réponse (isolation, télémétrie) que l'antivirus seul n'offre pas.
🎯 **À retenir** — L'EDR voit le comportement, pas seulement les fichiers : indispensable face aux menaces modernes.

## Chapitre 273 — Firewall

**Définition.** Filtrage du trafic réseau selon des règles (et, pour les NGFW, selon applications/identités/contenus).
**Contre quoi.** Accès non autorisés, réduction de surface réseau, contrôle des flux.
**Principe.** Filtrer entrant *et sortant* (le sortant limite C2/exfiltration), par défaut en deny.
🎯 **À retenir** — Le firewall contrôle les flux ; ne pas négliger le filtrage *sortant*.

## Chapitre 274 — WAF

**Définition.** *Web Application Firewall* : filtrage spécialisé du trafic web applicatif.
**Contre quoi.** Attaques web (injection, XSS, etc. — Partie 6), en *défense en profondeur*.
**Principe.** Détecte/bloque des motifs d'attaque web ; utile mais *ne remplace pas* un code sûr (contournable).
⚠️ **Erreur fréquente** — Compter sur le WAF au lieu de corriger le code (le WAF se contourne).
🎯 **À retenir** — Le WAF est une couche supplémentaire, pas un substitut au développement sécurisé.

## Chapitre 275 — Reverse proxy

**Définition.** Intermédiaire en façade des services, masquant et filtrant l'accès aux serveurs.
**Contre quoi.** Exposition directe, réduction de surface, point de contrôle (TLS, filtrage).
**Principe.** Centralise terminaison TLS, filtrage, journalisation, et cache la topologie interne.
🎯 **À retenir** — Le reverse proxy concentre contrôle et discrétion en façade des services.

## Chapitre 276 — Bastion

**Définition.** Point d'accès unique et durci pour l'administration (rappel du chapitre 20).
**Contre quoi.** Vol/réutilisation d'identifiants d'administration, lateral movement vers le Tier 0.
**Principe.** Tous les accès privilégiés transitent par le bastion, journalisés/enregistrés.
🎯 **À retenir** — Le bastion canalise et trace l'administration : pilier du tiering et du PAM.

## Chapitre 277 — Segmentation réseau

**Définition.** Découpage du réseau en zones filtrées (rappel du chapitre 15).
**Contre quoi.** Lateral movement, pivoting, propagation (vers/ransomware).
**Principe.** Contenir un incident dans une zone ; limiter les flux est-ouest.
🎯 **À retenir** — La segmentation compartimente le naufrage : un incident local ne devient pas global.

## Chapitre 278 — Microsegmentation

**Définition.** Segmentation fine au niveau de la charge de travail (rappel du chapitre 16).
**Contre quoi.** Lateral movement est-ouest, dans datacenter/cloud.
**Principe.** Autoriser uniquement les flux applicatifs explicitement nécessaires.
🎯 **À retenir** — La microsegmentation passe du « cloisonner par zones » au « cloisonner par flux » : socle du Zero Trust.

## Chapitre 279 — VPN

**Définition.** Tunnel chiffré d'accès distant (rappel du chapitre 55).
**Contre quoi.** Interception sur réseaux non fiables, accès distant non sécurisé.
**Principe.** Chiffrer l'accès distant ; mais exposé et donnant un accès large — d'où MFA, patch, moindre privilège.
⚠️ **Erreur fréquente** — VPN sans MFA donnant un accès réseau plat.
🎯 **À retenir** — Le VPN protège le transport mais reste une cible : MFA + patch + moindre privilège, et envisager le ZTNA.

## Chapitre 280 — ZTNA

**Définition.** *Zero Trust Network Access* : accès *par application* (et non par réseau), vérifié en continu selon l'identité et le contexte.
**Contre quoi.** Accès réseau trop large (défaut du VPN), lateral movement.
**Principe.** Pas de confiance par localisation ; chaque accès applicatif est réévalué (identité, posture, contexte).
🎯 **À retenir** — Le ZTNA remplace l'accès réseau large du VPN par un accès applicatif minimal et contextuel : mise en œuvre concrète du Zero Trust.

## Chapitre 281 — IAM

**Définition.** Gestion des identités et des accès (rappel des chapitres 57, 219).
**Contre quoi.** Accès non autorisés, élévation, comptes orphelins.
**Principe.** Cycle de vie des identités, moindre privilège, revue d'accès, SSO, gouvernance (IGA).
🎯 **À retenir** — L'IAM gouverne le « nouveau périmètre » : moindre privilège et revue d'accès en sont le cœur.

## Chapitre 282 — MFA

**Définition.** Authentification multi-facteur (rappel du chapitre 6).
**Contre quoi.** Vol/devinette d'identifiants (phishing, spraying, stuffing, brute force).
**Principe.** Exiger ≥2 familles de facteurs ; privilégier le **MFA résistant au phishing** (FIDO2/passkeys, number matching) contre le phishing et la MFA fatigue.
⚠️ **Erreur fréquente** — MFA par simple push (vulnérable à la fatigue) ; pas de protection contre le vol de jeton de session.
🎯 **À retenir** — Le MFA est la parade reine au vol d'identifiants ; la version résistante au phishing est désormais la cible.

## Chapitre 283 — PAM

**Définition.** Gestion des accès privilégiés (rappel du chapitre 20).
**Contre quoi.** Abus/vol de comptes privilégiés, lateral movement vers le Tier 0.
**Principe.** Coffre-fort de secrets, accès just-in-time, rotation, enregistrement de session.
🎯 **À retenir** — Le PAM supprime les secrets privilégiés permanents : antidote central des attaques d'identité.

## Chapitre 284 — Chiffrement

**Définition.** Protection cryptographique des données au repos, en transit, en usage (rappel du chapitre 68).
**Contre quoi.** Interception (sniffing/MITM), vol de données/supports.
**Principe.** Algorithmes éprouvés, gestion de clés rigoureuse ; protège la donnée même volée.
🎯 **À retenir** — Le chiffrement rend la donnée volée inexploitable — si la *gestion des clés* est sérieuse.

## Chapitre 285 — DLP

**Définition.** *Data Loss Prevention* : prévention de la fuite de données sensibles (détection/blocage des exfiltrations).
**Contre quoi.** Exfiltration, fuite involontaire ou malveillante de données.
**Principe.** Identifier les données sensibles (classification — chapitre 34) et contrôler leurs mouvements (mail, web, supports).
⚠️ **Erreur fréquente** — DLP sans classification fiable (faux positifs massifs, contournements).
🎯 **À retenir** — Le DLP surveille les mouvements de données sensibles : il dépend d'une bonne classification.

## Chapitre 286 — Sauvegardes

**Définition.** Copies de récupération des données (rappel du chapitre 28).
**Contre quoi.** Ransomware, wiper, panne, erreur, corruption.
**Principe.** Règle 3-2-1, tester la restauration.
🎯 **À retenir** — La sauvegarde testée est la dernière ligne de défense ; non testée, c'est un pari.

## Chapitre 287 — Sauvegardes immuables

**Définition.** Sauvegardes non modifiables/supprimables pendant une période définie (WORM, hors-ligne, air-gap).
**Contre quoi.** Ransomware/wiper qui ciblent justement les sauvegardes.
**Principe.** Garantir qu'au moins une copie résiste au chiffrement/à la suppression par l'attaquant.
🎯 **À retenir** — L'immutabilité (ou l'air-gap) est ce qui sauve réellement face au ransomware moderne.

## Chapitre 288 — Supervision

**Définition.** Surveillance continue de l'état de sécurité (rappel du chapitre 27).
**Contre quoi.** Détection tardive, angles morts.
**Principe.** Sources + SIEM/EDR/NDR + cas d'usage ; réduire le temps de détection (MTTD).
🎯 **À retenir** — On maintient la sécurité par la surveillance continue, pas par des contrôles ponctuels.

## Chapitre 289 — Threat hunting

**Définition.** Recherche *proactive* de menaces non détectées par les alertes automatiques.
**Contre quoi.** Attaquants furtifs (APT, fileless, LotL) passés sous les radars.
**Principe.** Formuler des hypothèses (souvent basées sur des TTP ATT&CK) et chercher activement leurs traces dans la télémétrie.
🎯 **À retenir** — Le threat hunting cherche ce que les alertes ratent : posture *assume breach* en action.

## Chapitre 290 — Deception et honeypot

**Définition.** Leurres (honeypots, comptes/données pièges) destinés à attirer et détecter les attaquants.
**Contre quoi.** Intrusions furtives, reconnaissance interne, lateral movement.
**Principe.** Un leurre n'a aucune raison légitime d'être touché : toute interaction est un signal *à très faible faux positif*.
🎯 **À retenir** — La déception transforme la curiosité de l'attaquant en alerte fiable : peu de bruit, fort signal.

## Chapitre 291 — Sandbox

**Définition.** Environnement isolé pour exécuter/analyser un contenu suspect sans risque pour le système réel.
**Contre quoi.** Malwares, pièces jointes/fichiers piégés.
**Principe.** Détoner le suspect en isolation pour observer son comportement (détection dynamique).
⚠️ **Erreur fréquente** — Oublier que certains malwares détectent la sandbox et restent inertes.
🎯 **À retenir** — La sandbox révèle le comportement d'un fichier en isolation, en complément des signatures.

## Chapitre 292 — Filtrage DNS

**Définition.** Contrôle des résolutions DNS pour bloquer domaines malveillants et détecter abus.
**Contre quoi.** C2, phishing, DNS tunneling, malvertising/SEO poisoning.
**Principe.** Bloquer/journaliser les résolutions vers des domaines malveillants ou anormaux.
🎯 **À retenir** — Le filtrage DNS coupe de nombreux canaux (C2, phishing) à peu de frais et révèle les abus.

## Chapitre 293 — Sécurité mail

**Définition.** Ensemble des protections de la messagerie (filtrage, sandbox, analyse de liens).
**Contre quoi.** Phishing, malspam, BEC, pièces jointes/liens piégés (Partie 9).
**Principe.** Filtrer, analyser, authentifier l'expéditeur, réécrire/inspecter les liens, bloquer les charges dangereuses.
🎯 **À retenir** — La messagerie étant le vecteur n°1, sa protection (filtrage + authentification + sensibilisation) est prioritaire.

## Chapitre 294 — SPF, DKIM, DMARC

**Définition.** Mécanismes d'*authentification de l'expéditeur* d'e-mail.
- **SPF** : déclare quels serveurs peuvent envoyer pour un domaine.
- **DKIM** : signe les messages (intégrité + origine).
- **DMARC** : politique combinant SPF/DKIM et reporting (que faire des messages non authentifiés).
**Contre quoi.** Usurpation de domaine (spoofing), phishing/BEC par usurpation directe.
⚠️ **Erreur fréquente** — DMARC en mode permissif (« none ») jamais durci, donc sans effet.
🎯 **À retenir** — SPF+DKIM+DMARC (en mode actif) empêchent l'usurpation directe du domaine : socle anti-phishing/BEC.

## Chapitre 295 — CSP

**Définition.** *Content Security Policy* : politique côté navigateur restreignant les sources de contenu/scripts d'une page web.
**Contre quoi.** XSS (défense en profondeur), injection de contenu (Partie 6).
**Principe.** Limiter ce que le navigateur exécute/charge ; couplée à Trusted Types contre le DOM-XSS.
⚠️ **Erreur fréquente** — CSP trop permissive (annule son intérêt).
🎯 **À retenir** — La CSP est une couche anti-XSS côté navigateur, en complément de l'encodage de sortie.

## Chapitre 296 — SAST

**Définition.** *Static Application Security Testing* : analyse du *code source* (sans l'exécuter) à la recherche de vulnérabilités.
**Contre quoi.** Vulnérabilités de code (injection, secrets en dur, etc.) — au plus tôt.
**Principe.** Intégré au développement/CI (« shift left ») ; détecte tôt mais génère des faux positifs.
🎯 **À retenir** — Le SAST trouve les failles dans le code, tôt : à intégrer en CI, avec tri des faux positifs.

## Chapitre 297 — DAST

**Définition.** *Dynamic Application Security Testing* : test de l'application *en exécution* (boîte noire), comme un attaquant.
**Contre quoi.** Vulnérabilités observables au runtime (injection, configuration, auth).
**Principe.** Complète le SAST en testant le comportement réel ; ne voit pas le code mais les effets.
🎯 **À retenir** — Le DAST teste l'application qui tourne : complémentaire du SAST (code) pour une couverture large.

## Chapitre 298 — IAST

**Définition.** *Interactive Application Security Testing* : analyse depuis *l'intérieur* de l'application en cours d'exécution (instrumentation).
**Contre quoi.** Vulnérabilités runtime, avec plus de précision (moins de faux positifs).
**Principe.** Combine vision interne (comme SAST) et exécution réelle (comme DAST), pendant les tests.
🎯 **À retenir** — L'IAST marie code et runtime pour une détection précise pendant les tests.

## Chapitre 299 — SCA

**Définition.** *Software Composition Analysis* : analyse des *dépendances tierces* (rappel des chapitres 71, 240).
**Contre quoi.** Dépendances vulnérables, paquets malveillants, problèmes de licence.
**Principe.** Inventorier (SBOM) et confronter les dépendances aux vulnérabilités connues ; surveiller les mises à jour.
🎯 **À retenir** — Le SCA surveille ce qu'on importe : indispensable, le code moderne étant surtout fait de dépendances.

## Chapitre 300 — Secrets scanning

**Définition.** Détection automatisée de secrets exposés (dans le code, l'historique, les images, les journaux).
**Contre quoi.** Exposition de secrets (chapitres 77, 221, 222).
**Principe.** Scanner en continu (pré-commit, CI, dépôts) pour détecter et révoquer/roter rapidement.
🎯 **À retenir** — Le secrets scanning attrape les fuites de secrets avant (ou dès) qu'elles surviennent : à coupler au coffre-fort.

## Chapitre 301 — Pentest

**Définition.** *Test d'intrusion* : évaluation offensive *autorisée et encadrée*, simulant un attaquant pour révéler des failles exploitables.
**Contre quoi.** Failles réelles, validation de l'efficacité défensive.
**Principe.** Périmètre et règles définis ; produit un rapport de vulnérabilités priorisées. Photographie à un instant T.
⚠️ **Erreur fréquente** — Confondre pentest (exploitation manuelle ciblée) et scan de vulnérabilités (automatisé, large).
🎯 **À retenir** — Le pentest révèle l'exploitable réel à un instant T, dans un cadre autorisé strict.

## Chapitre 302 — Bug bounty

**Définition.** Programme rémunérant des chercheurs externes qui signalent des vulnérabilités, dans un cadre défini.
**Contre quoi.** Failles non détectées en interne, en continu et à grande échelle.
**Principe.** Mobiliser une communauté de chercheurs (vs un test ponctuel) avec des règles (scope, divulgation responsable) et des récompenses.
🎯 **À retenir** — Le bug bounty étend la recherche de failles dans le temps et en diversité, en complément du pentest.

## Chapitre 303 — Purple teaming

**Définition.** Collaboration entre équipe offensive (red) et défensive (blue) pour *améliorer la détection/réponse*.
**Contre quoi.** Angles morts de détection, lacunes de réponse.
**Principe.** Le red rejoue des TTP (ATT&CK) pendant que le blue mesure ce qu'il détecte et améliore en boucle.
🎯 **À retenir** — Le purple teaming transforme l'attaque simulée en amélioration mesurable de la défense.

## Chapitre 304 — Tabletop exercise

**Définition.** Exercice de crise *sur table* (simulation discutée d'un scénario), sans impact réel sur les systèmes.
**Contre quoi.** Impréparation organisationnelle à la crise (chapitre 39).
**Principe.** Faire répéter décisions, rôles, communication et coordination à froid, pour révéler les lacunes avant le jour J.
🎯 **À retenir** — Le tabletop entraîne l'organisation à la crise sans risque : la crise se répète avant d'arriver.

## Chapitre 305 — Sensibilisation

**Définition.** Programme d'élévation de la vigilance humaine (rappel du chapitre 37).
**Contre quoi.** Ingénierie sociale, phishing, erreurs humaines (Partie 9).
**Principe.** Formations, simulations, culture du signalement *sans punition* ; transformer l'humain en capteur.
🎯 **À retenir** — La sensibilisation est un contrôle de sécurité à part entière, au rendement élevé : l'humain formé devient une ligne de détection.

---

> Suite et fin dans la **Partie 13 (synthèse transversale)** et les **Annexes**, fournies dans le document complémentaire de ce volume.


> Partie 13 : Synthèse transversale · Annexes A à I
>
> Après avoir *compris, classé, relié, défendu et répondu*, cette dernière partie apprend à **raisonner** : transformer la taxonomie en méthode de pensée. Les annexes sont des outils de référence à garder sous la main.

---

# Partie 13 — Synthèse transversale

## Chapitre 306 — Comment classer une attaque inconnue

**Méthode en 6 questions.** Face à une attaque jamais vue, ne pas chercher à la « connaître » mais à la *ranger* :

1. **Quelle surface ?** (Partie 4) — web, réseau, identité, cloud, humain… *Où* frappe-t-elle ?
2. **Quelle propriété CIA visée ?** (chapitre 5) — confidentialité, intégrité, disponibilité ?
3. **Quelle faiblesse exploitée ?** (Partie 5) — authentification, autorisation, injection, configuration, confiance… ?
4. **Quelle famille d'attaque ?** (Parties 6–10) — la faiblesse + la surface pointent vers une famille connue.
5. **Quelle tactique ATT&CK ?** — accès initial, exécution, élévation, mouvement latéral, exfiltration, impact ?
6. **Quel impact métier ?** (chapitre 10) — pour prioriser.

🔧 **Exemple concret** — « Une fonctionnalité d'import récupère une URL et atteint un service interne. » → surface : application/cloud ; faiblesse : confiance dans une entrée + accès non prévu ; famille : SSRF (chapitre 105). On hérite aussitôt des défenses SSRF.

🎯 **À retenir** — On ne mémorise pas les attaques, on les *classe*. Six questions suffisent à rattacher l'inconnu au connu.

## Chapitre 307 — Comment relier une attaque à une vulnérabilité

**Principe.** Toute attaque *exploite* une vulnérabilité (Partie 5). Remonter de l'attaque à sa faiblesse-racine, c'est comprendre *pourquoi* elle marche — et donc *quoi corriger*.

**Méthode.** Demander : « *Quelle faiblesse rend cette attaque possible ?* »
- XSS, SQLi → injection (interpréteur confond données et code).
- IDOR/BOLA → défaut d'autorisation.
- Bucket public → mauvaise configuration.
- Pass-the-hash → mécanique de réutilisation + permissions excessives.
- BEC → confiance humaine + absence de double validation.

🧭 **Taxonomie** — Une même vulnérabilité (ex. injection) génère plusieurs attaques (XSS, SQLi, command…). Corriger la *faiblesse* neutralise *toute la famille*.

🎯 **À retenir** — Remonter à la vulnérabilité-racine permet de corriger la cause, pas le symptôme — et souvent toute une famille d'attaques d'un coup.

## Chapitre 308 — Comment relier une vulnérabilité à un contrôle

**Principe.** À chaque vulnérabilité correspond un (ou des) contrôle(s) défensif(s) (Partie 12). C'est la logique D3FEND : faiblesse → contre-mesure.

**Méthode.** Demander : « *Quel contrôle supprime ou compense cette faiblesse ?* »
- Injection → requêtes paramétrées + encodage de sortie (+ WAF en profondeur).
- Défaut d'autorisation → contrôle d'accès serveur systématique, deny by default.
- Exposition de secrets → coffre-fort + secrets scanning + rotation.
- Vol d'identifiants → MFA résistant au phishing.
- Lateral movement → segmentation + tiering + LAPS.

🧭 **Taxonomie** — Un contrôle couvre souvent plusieurs vulnérabilités (le moindre privilège limite élévation *et* lateral movement *et* impact d'injection). On priorise les contrôles à *large couverture*.

🎯 **À retenir** — Relier faiblesse → contrôle transforme l'analyse en action. Privilégier les contrôles couvrant le plus de familles.

## Chapitre 309 — Comment relier une attaque à une détection

**Principe.** Toute attaque laisse (ou peut laisser) des *signaux* (Partie 11). Anticiper ces signaux, c'est concevoir la détection.

**Méthode.** Demander : « *Quelles traces cette attaque produit-elle, et dans quelle source ?* »
- Password spraying → pics d'échecs sur de nombreux comptes (journaux d'authentification).
- Exfiltration DNS → requêtes DNS anormales (logs DNS/NDR).
- Lateral movement → connexions inter-machines atypiques (EDR/NDR/SIEM).
- Ransomware → chiffrement massif + suppression de sauvegardes (EDR/SIEM).

🧭 **Taxonomie** — Viser le niveau **TTP** (chapitre 247) : détecter le *comportement* plutôt que l'artefact volatil. Cartographier les détections sur ATT&CK mesure la couverture.

🎯 **À retenir** — À chaque attaque, se demander *quelle trace, dans quelle source* : c'est ainsi qu'on construit des cas d'usage de détection.

## Chapitre 310 — Comment prioriser les risques

**Principe.** On ne traite jamais tout : on priorise (Partie 3). La priorité combine *vraisemblance* et *impact* (chapitre 3), pondérés par l'*exposition* réelle.

**Méthode.**
1. Identifier l'actif et son impact métier (chapitre 10).
2. Évaluer la vraisemblance : exposition (Internet ?), exploitabilité (EPSS/KEV ?), menace réaliste (ciblé vs opportuniste ?).
3. Croiser → niveau de risque.
4. Décider : réduire / transférer / éviter / accepter (chapitre 30).

⚠️ **Erreur fréquente** — Prioriser par le seul score technique (CVSS). Une « critique » non exposée pèse moins qu'une « moyenne » exposée et activement exploitée.

🎯 **À retenir** — Priorité = vraisemblance × impact × exposition. Le risque le plus « grave sur le papier » n'est pas toujours le plus urgent.

## Chapitre 311 — Carte mentale finale de la cybersécurité

**La structure complète, en un schéma mental :**

- **On protège des ACTIFS** (données, services, systèmes, identités, humains) — Partie 1.
- **Sur des SURFACES** (poste, réseau, AD, web, API, cloud, conteneurs, supply chain, humain…) — Partie 4.
- **Qui ont des VULNÉRABILITÉS** (authentification, autorisation, injection, configuration, confiance…) — Partie 5.
- **Exploitées par des ATTAQUES** classées par famille et par surface — Parties 6 à 10.
- **Menées selon des TACTIQUES** (ATT&CK : accès initial → … → impact).
- **Contrées par des PRINCIPES** (défense en profondeur, moindre privilège, Zero Trust, assume breach…) — Partie 2.
- **Mis en œuvre par des CONTRÔLES** (préventifs/détectifs/correctifs) — Partie 12.
- **Surveillés et traités** par la détection et la réponse — Partie 11.
- **Le tout GOUVERNÉ** par la GRC — Partie 3.

**Le fil rouge unique :** `actif → menace → vulnérabilité → risque → attaque → impact → détection → réponse → remédiation`.

🎯 **À retenir** — Toute notion cyber trouve sa place sur cette carte. Si vous savez où ranger une notion, vous savez la relier, la défendre et y répondre.

## Chapitre 312 — Les erreurs de raisonnement fréquentes

Pièges classiques qui faussent l'analyse :

1. **Confondre les niveaux** : vulnérabilité ≠ risque ; authentification ≠ autorisation ; alerte ≠ incident.
2. **Sécurité par l'obscurité** : croire que « caché » = « protégé » (UUID, endpoint non documenté).
3. **Tout-préventif** : négliger détection et réponse (oublier *assume breach*).
4. **Faire confiance au client / à la localisation réseau** : violer les frontières de confiance (chapitre 80).
5. **Prioriser par le score technique seul** : ignorer exposition et impact métier.
6. **Confondre le symptôme et la cause** : corriger une attaque sans traiter la vulnérabilité-racine.
7. **Croire un outil suffisant** : « j'ai un WAF/un SIEM/un MFA » sans configuration, sources ni réglage.
8. **Punir l'erreur humaine** : tuer la culture du signalement.
9. **Oublier la supply chain et l'identité** : se concentrer sur le périmètre.
10. **Sauvegardes non testées / non immuables** : faux sentiment de résilience.

🎯 **À retenir** — La plupart des échecs viennent moins d'une attaque sophistiquée que d'une *erreur de raisonnement* : confusion de niveaux, confiance implicite, ou dépendance à un seul contrôle.

## Chapitre 313 — Glossaire final (voir Annexe A)

Le glossaire complet est fourni en **Annexe A**. Il rassemble les termes clés du cours, à utiliser comme référence rapide. Conserver à l'esprit que *définir précisément* est déjà une compétence de sécurité : la plupart des confusions opérationnelles viennent d'un vocabulaire flou.

🎯 **À retenir** — Un vocabulaire précis est un outil de sécurité : il évite les malentendus coûteux en analyse, en réponse et en gouvernance.

---

---

# Partie 14 — Cas filés d'investigation SOC/IR (V2)

> Cette partie répond à la principale limite du référentiel : le passage du *vocabulaire* au *raisonnement opérationnel*. Six cas filés déroulent le cycle complet **événement → alerte → hypothèse → qualification → investigation → confinement → éradication → rétablissement → REX**, en nommant à chaque étape les **sources de logs**, les **signaux faibles** et les **décisions défensives**.
>
> **Posture inchangée** : défensive et pédagogique. Les cas sont conceptuels — aucune procédure offensive, aucune commande d'exploitation. Les noms de journaux et d'identifiants d'événements sont donnés à titre indicatif (les versions exactes évoluent ; se reporter aux sources de l'Annexe I).

## Schéma de référence du cycle d'incident

```text
ÉVÉNEMENT ──► ALERTE ──► TRIAGE ──► QUALIFICATION ──► [INCIDENT ?]
                                                          │ oui
                                                          ▼
   INVESTIGATION ──► CONFINEMENT ──► ÉRADICATION ──► RÉTABLISSEMENT ──► REX
   (portée totale)   (stopper)       (tout retirer)  (restaurer sain)   (apprendre)
        ▲                                                                   │
        └───────────────── boucle d'amélioration continue ◄────────────────┘
```

🧭 **Comment lire un cas.** Chaque cas suit la même trame : *contexte → signal initial → classement taxonomique (renvois aux chapitres) → hypothèse → sources de logs → investigation/pivots → confinement → éradication → rétablissement → REX → erreurs à éviter*.

---

## Chapitre 314 — Cas 1 : Phishing avec vol d'identifiants

**Contexte.** Une PME en environnement cloud + SaaS. Un employé reçoit un e-mail « sécurité » imitant le fournisseur d'identité.

**Signal initial (événement → alerte).** Le SIEM corrèle : une connexion réussie à la messagerie cloud depuis un pays inhabituel, quelques minutes après que l'utilisateur a soumis ses identifiants sur un domaine récemment enregistré (vu dans les logs proxy/DNS).

**Classement taxonomique.** Surface : identité + messagerie (ch. 49, 57). Vulnérabilité-racine : confiance humaine + absence de MFA résistant au phishing (ch. 62). Attaque : phishing → vol d'identifiants (ch. 203), suivi possible d'un consent phishing (ch. 217). Tactique ATT&CK : *Initial Access / Credential Access*.

**Hypothèse.** « Un compte a été hameçonné ; l'attaquant teste l'accès et va chercher à persister (règles de boîte, octroi OAuth) puis à pivoter. »

**Sources de logs utiles.**
- Journaux de connexion du fournisseur d'identité (sign-in logs) : localisation, appareil, ASN, statut MFA.
- Journaux de la messagerie cloud : création de **règles de transfert/suppression** (signal faible majeur de compromission), accès inhabituels.
- Logs proxy/DNS : domaine de phishing visité.
- Journaux d'**octrois OAuth** : application tierce nouvellement autorisée.

**Investigation / pivots.**
1. Confirmer la connexion suspecte (lieu, appareil, heure) et son écart avec la ligne de base de l'utilisateur.
2. Chercher les **mécanismes de persistance** propres au cloud : règles de boîte cachées, octroi OAuth, inscription d'un nouveau facteur MFA par l'attaquant.
3. Vérifier les accès aux fichiers/SharePoint et les envois sortants (exfiltration, fraude type BEC — ch. 209).
4. Identifier les autres destinataires de la campagne (même expéditeur/domaine) pour mesurer l'ampleur.

**Confinement.** Invalider les sessions actives (révoquer les jetons), réinitialiser le mot de passe, désactiver temporairement le compte si besoin, bloquer le domaine de phishing (proxy/DNS/mail), retirer les règles de boîte malveillantes.

**Éradication.** Supprimer les octrois OAuth illégitimes, retirer tout facteur MFA ajouté par l'attaquant, confirmer l'absence de backdoor cloud. Élargir aux autres comptes ciblés par la campagne.

**Rétablissement.** Réactiver le compte avec **MFA résistant au phishing** (FIDO2/passkeys — ch. 282), surveiller étroitement les connexions, informer l'utilisateur.

**REX.** Renforcer le filtrage mail et SPF/DKIM/DMARC (ch. 294), passer au MFA anti-phishing, ajouter une détection « création de règle de transfert externe » et « octroi OAuth à risque », simuler un phishing de sensibilisation.

⚠️ **Erreurs à éviter.** Réinitialiser le mot de passe *sans* révoquer les sessions (le jeton volé reste valide — ch. 191) ; oublier les persistances cloud (règles, OAuth, MFA ajouté) ; ne pas chercher les autres victimes de la campagne.

🎯 **À retenir.** Un phishing cloud ne s'arrête pas au mot de passe : il faut révoquer les sessions *et* traquer la persistance (règles de boîte, OAuth, MFA ajouté). Le MFA anti-phishing est la correction de fond.

---

## Chapitre 315 — Cas 2 : Suspicion de Kerberoasting

**Contexte.** Domaine Active Directory on-premise. Un poste utilisateur a déjà été compromis (accès initial obtenu).

**Signal initial.** Le SIEM remonte un **volume anormal de demandes de tickets de service** (TGS-REQ) émanant d'un seul poste, ciblant plusieurs comptes de service dotés d'un SPN, avec demande d'un chiffrement faible.

**Classement taxonomique.** Surface : Active Directory / identité (ch. 43). Vulnérabilité-racine : comptes de service à mot de passe faible + SPN exposés (ch. 160). Attaque : Kerberoasting (ch. 163). Tactique ATT&CK : *Credential Access (T1558.003)*.

**Hypothèse.** « Un attaquant déjà présent récolte des tickets de comptes de service pour casser leurs mots de passe hors ligne et élever ses privilèges. »

**Sources de logs utiles.**
- Journaux Kerberos des contrôleurs de domaine : **demandes de tickets de service** (Event ID 4769), en filtrant sur les chiffrements faibles et le volume par compte source.
- EDR du poste source : processus à l'origine des demandes, comportement de collecte.
- Inventaire AD : comptes de service avec SPN, leurs privilèges et l'ancienneté de leurs mots de passe.

**Investigation / pivots.**
1. Identifier le poste/compte à l'origine des demandes (le « qui »).
2. Lister les comptes de service ciblés et **évaluer leur danger** : sont-ils privilégiés ? mots de passe faibles/anciens ?
3. Vérifier si un cassage a déjà abouti : connexions réussies récentes de ces comptes de service depuis des emplacements anormaux (signal d'élévation réussie).
4. Rechercher la suite logique : mouvement latéral (ch. 182), tentative vers le Tier 0 (ch. 162).

**Confinement.** Isoler le poste source (EDR), désactiver/forcer le changement des comptes de service à risque, surveiller le Tier 0.

**Éradication.** Réinitialiser les mots de passe des comptes de service compromis (idéalement migrer vers **gMSA** à rotation automatique — ch. 163), retirer les SPN inutiles, vérifier l'absence de persistance (tickets forgés — ch. 171/172, shadow credentials — ch. 179).

**Rétablissement.** Remettre le poste en service après reconstruction, durcir les comptes de service, renforcer la surveillance Kerberos.

**REX.** Imposer gMSA / mots de passe longs aléatoires aux comptes de service, appliquer le tiering (ch. 162), créer/affiner la détection « TGS-REQ en volume + chiffrement faible », auditer régulièrement les SPN et privilèges.

⚠️ **Erreurs à éviter.** Traiter l'alerte comme un simple « bruit Kerberos » sans vérifier le cassage réussi ; réinitialiser les comptes de service sans corriger leur faiblesse de fond (gMSA) ; ignorer la progression possible vers le Tier 0.

🎯 **À retenir.** Le Kerberoasting est silencieux et hors-ligne : la détection se fait sur le *comportement de demande* (volume TGS-REQ, chiffrement faible), et la correction de fond est gMSA + tiering.

---

## Chapitre 316 — Cas 3 : Malware sur un poste de travail

**Contexte.** Poste utilisateur Windows. Une pièce jointe a été ouverte et a activé une macro.

**Signal initial.** L'EDR alerte sur un document bureautique lançant un processus enfant qui établit une connexion sortante vers un domaine de mauvaise réputation (comportement de loader/downloader — ch. 194/196).

**Classement taxonomique.** Surface : poste utilisateur (ch. 40). Vulnérabilité-racine : macro autorisée + confiance utilisateur (ch. 200). Attaque : macro malware → loader → charge (RAT/infostealer — ch. 192/191). Tactique ATT&CK : *Execution / Command and Control*.

**Hypothèse.** « Un loader a été exécuté via macro et tente de récupérer une charge ; il faut empêcher la suite (charge, persistance, C2) et vérifier le vol de secrets. »

**Sources de logs utiles.**
- EDR : arbre de processus (document → interpréteur → enfant), injections mémoire (fileless — ch. 199), persistance (tâches planifiées, clés de démarrage).
- Journaux DNS/proxy : domaine C2 contacté, autres résolutions suspectes.
- Journaux d'authentification : usage des identifiants depuis le poste (signe de vol/infostealer).

**Investigation / pivots.**
1. Reconstituer l'arbre de processus et déterminer si une charge a été récupérée/exécutée.
2. Chercher la **persistance** (tâches, démarrage, services).
3. Évaluer le **vol de secrets** (infostealer — ch. 191) : si des identifiants/jetons ont pu être volés, traiter aussi le volet identité (révoquer sessions, réinitialiser).
4. Vérifier un éventuel **mouvement latéral** initié depuis le poste.

**Confinement.** **Isoler le poste du réseau via l'EDR** (sans l'éteindre, pour préserver la mémoire/preuves — ch. 263), bloquer le domaine C2.

**Éradication.** Supprimer la charge et toute persistance ; en cas de doute sur la profondeur (fileless, rootkit — ch. 197), **reconstruire le poste** plutôt que nettoyer. Si vol de secrets confirmé : réinitialiser les identifiants concernés et révoquer les sessions.

**Rétablissement.** Réimager le poste, restaurer les données depuis une sauvegarde saine, surveiller le poste et le compte.

**REX.** Bloquer les macros (surtout depuis Internet — ch. 200), renforcer le filtrage mail, vérifier la couverture EDR, ajouter une détection « document → processus enfant → connexion sortante », sensibiliser.

⚠️ **Erreurs à éviter.** Éteindre le poste (perte des preuves mémoire) ; « nettoyer » un poste potentiellement infecté en profondeur au lieu de le reconstruire ; oublier le volet identité si un infostealer a opéré.

🎯 **À retenir.** Sur un malware de poste : isoler (sans éteindre), reconstruire en cas de doute, et toujours évaluer le vol d'identifiants — l'incident « poste » devient souvent un incident « identité ».

---

## Chapitre 317 — Cas 4 : Exfiltration depuis le cloud

**Contexte.** Environnement cloud IaaS. Une clé d'accès a fuité (dépôt public — ch. 222).

**Signal initial.** Les journaux d'audit cloud montrent un usage d'une clé d'accès depuis une adresse inhabituelle, avec une rafale d'opérations de **listing et de lecture sur des buckets** de stockage.

**Classement taxonomique.** Surface : cloud (ch. 46). Vulnérabilité-racine : secret exposé + permissions excessives (ch. 221/219). Attaque : usage de clé volée → accès aux données → exfiltration ; risque d'élévation (ch. 224) et de lateral movement cloud (ch. 225). Tactique ATT&CK : *Collection / Exfiltration*.

**Hypothèse.** « Une clé exposée est utilisée pour lire et exfiltrer des données ; l'attaquant peut tenter d'élever ses privilèges et de persister (nouvelle clé/utilisateur). »

**Sources de logs utiles.**
- Journaux d'audit cloud (type CloudTrail / journaux d'activité) : appels d'API, source, identité utilisée, opérations sur le stockage.
- Journaux d'accès au stockage : volumes lus/téléchargés (mesurer l'exfiltration).
- Journaux IAM : création de clés/utilisateurs/rôles, modifications de politiques (persistance/élévation).

**Investigation / pivots.**
1. Identifier la clé compromise et **toutes** ses actions (lecture, mais aussi création d'accès, modification de politiques).
2. Mesurer le périmètre de données exfiltrées (quels buckets, quel volume) — impact réglementaire potentiel.
3. Chercher la **persistance** : nouvelles clés/utilisateurs/rôles créés, politiques modifiées (auto-élévation — ch. 224).
4. Vérifier le rebond vers d'autres comptes/services (relations de confiance — ch. 225).

**Confinement.** **Révoquer/désactiver immédiatement la clé** compromise, restreindre les accès au stockage concerné, bloquer la source si possible.

**Éradication.** Supprimer toute persistance créée (clés/utilisateurs/rôles illégitimes), corriger les politiques modifiées, faire tourner les secrets potentiellement exposés.

**Rétablissement.** Émettre de nouveaux secrets à portée minimale, durcir les permissions (moindre privilège IAM — ch. 219), activer le blocage public par défaut (ch. 220), renforcer la surveillance.

**REX.** Déployer le **secrets scanning** (ch. 300) et un coffre-fort (ch. 244), appliquer le moindre privilège IAM et l'analyse des chemins d'élévation, activer/affiner les alertes « usage de clé depuis source inhabituelle » et « création d'accès IAM », gérer l'obligation de notification si fuite de données personnelles (ch. 268).

⚠️ **Erreurs à éviter.** Désactiver la clé sans chercher la persistance IAM créée entre-temps ; sous-estimer le périmètre de données (impact réglementaire) ; réémettre des secrets surprivilégiés.

🎯 **À retenir.** Une clé cloud volée mène vite à l'exfiltration *et* à la persistance IAM : révoquer la clé ne suffit pas, il faut traquer les accès créés et corriger le moindre privilège. La prévention de fond est le coffre-fort + le scanning.

---

## Chapitre 318 — Cas 5 : Ransomware

**Contexte.** Réseau d'entreprise mixte. Accès initial obtenu (ex. RDP exposé — ch. 140, ou phishing), suivi d'un mouvement latéral.

**Signal initial.** Vague d'alertes EDR/SIEM : **chiffrement massif de fichiers** sur plusieurs serveurs, **suppression des clichés/sauvegardes** accessibles, comptes d'administration utilisés à des heures inhabituelles. Souvent précédée (rétrospectivement) de signaux faibles : reconnaissance interne, désactivation de défenses.

**Classement taxonomique.** Surface : multiple (serveurs, identité, réseau). Vulnérabilité-racine : multiple (accès exposé, réutilisation d'identifiants, absence de segmentation/tiering). Attaque : ransomware (ch. 188), souvent avec double extorsion (exfiltration préalable). Tactique ATT&CK : *Impact (T1486)*, précédé de *Lateral Movement / Exfiltration*.

**Hypothèse.** « Un opérateur de ransomware est présent depuis un certain temps ; il a probablement exfiltré avant de chiffrer (double extorsion) et cherché à neutraliser les sauvegardes. »

**Sources de logs utiles.**
- EDR/SIEM : début du chiffrement, processus responsable, propagation, suppression de clichés/sauvegardes.
- Journaux d'authentification/AD : usage de comptes d'administration, mouvement latéral (ch. 182), accès au Tier 0.
- Journaux réseau/exfiltration : volumes sortants anormaux *avant* le chiffrement (double extorsion).
- Journaux des sauvegardes : tentatives de suppression/altération.

**Investigation / pivots.**
1. Déterminer l'**étendue** (machines chiffrées, données exfiltrées) et le **point d'entrée initial** (RDP, phishing, VPN — ch. 141).
2. Reconstituer le **mouvement latéral** et l'accès aux comptes privilégiés (krbtgt compromis ? ch. 171).
3. Évaluer l'**exfiltration** (impact réglementaire et négociation).
4. Identifier les sauvegardes **saines et hors-ligne/immuables** disponibles (ch. 287).

**Confinement.** **Segmenter/isoler** massivement (couper les liaisons entre zones) pour stopper la propagation, désactiver les comptes compromis, **déclencher la cellule de crise** (ch. 39/266) et activer le **PRA/PCA** (ch. 267). Communication de crise et obligations de notification (ch. 268).

**Éradication.** Identifier et supprimer *toute* la présence de l'attaquant (backdoors, comptes, persistance, krbtgt à roter deux fois si AD compromis — ch. 171) avant toute reconnexion. Une éradication partielle = rechiffrement.

**Rétablissement.** Restaurer depuis des **sauvegardes immuables et vérifiées** (ch. 287), reconstruire les systèmes critiques, corriger le vecteur initial, surveiller étroitement la réapparition de l'attaquant pendant la reprise.

**REX.** Supprimer les expositions (RDP/VPN — ch. 140/141), imposer MFA et tiering, déployer des sauvegardes immuables testées, segmenter, améliorer la détection précoce (reconnaissance interne, désactivation de défenses, suppression de clichés), réaliser des exercices de crise (tabletop — ch. 304).

⚠️ **Erreurs à éviter.** Restaurer avant d'avoir éradiqué (rechiffrement) ; restaurer depuis une sauvegarde elle-même compromise/en ligne ; négliger l'exfiltration (la double extorsion change la gestion de crise) ; payer en croyant que cela garantit la récupération (un wiper déguisé — ch. 189 — ne déchiffre rien).

🎯 **À retenir.** Le ransomware est l'aboutissement d'une intrusion complète : confiner (segmenter) + cellule de crise + éradication exhaustive *avant* restauration depuis l'immuable. La prévention de fond combine sauvegardes immuables testées, segmentation, tiering, MFA et détection précoce.

---

## Chapitre 319 — Cas 6 : SSRF vers les métadonnées cloud

**Contexte.** Application web hébergée sur une instance cloud, exposant une fonctionnalité qui récupère une ressource à partir d'une URL fournie.

**Signal initial.** Le NDR/journaux applicatifs montrent que le **serveur applicatif initie des requêtes vers l'adresse interne du service de métadonnées** de l'instance, puis un usage anormal des identifiants de rôle de l'instance apparaît dans les journaux cloud.

**Classement taxonomique.** Surface : web + cloud (ch. 44/46). Vulnérabilité-racine : validation/allowlist d'URL insuffisante + confiance (ch. 80). Attaque : SSRF → métadonnées cloud (ch. 105/107). Tactique ATT&CK : *Credential Access / Discovery*.

**Hypothèse.** « Une SSRF est exploitée pour atteindre le service de métadonnées et récupérer les identifiants temporaires du rôle de l'instance, ensuite utilisés pour accéder aux ressources cloud. »

**Sources de logs utiles.**
- Journaux applicatifs / reverse proxy : URL fournies en paramètre, requêtes sortantes du serveur.
- NDR / journaux réseau : **accès au point de métadonnées** depuis l'application (signal fort).
- Journaux d'audit cloud : usage des identifiants de rôle d'instance depuis des contextes anormaux, opérations sur les ressources.

**Investigation / pivots.**
1. Confirmer la SSRF (paramètre d'URL menant à l'adresse de métadonnées) et son exploitation.
2. Déterminer si des **identifiants de rôle** ont été récupérés et utilisés (journaux cloud).
3. Mesurer les actions effectuées avec ce rôle (lecture/exfiltration, élévation, persistance — comme le Cas 4).
4. Identifier le périmètre des ressources accessibles via ce rôle (impact lié au moindre privilège).

**Confinement.** Corriger/bloquer la fonctionnalité vulnérable (allowlist stricte, blocage de l'adresse de métadonnées), **révoquer/roter les identifiants de rôle** potentiellement exposés, restreindre les actions du rôle.

**Éradication.** Supprimer toute persistance créée avec le rôle (cf. Cas 4), corriger le code de l'application (allowlist de destinations, normalisation d'URL — ch. 105).

**Rétablissement.** Déployer la version corrigée, activer la **version renforcée du service de métadonnées** (étape supplémentaire requise pour y accéder), appliquer le **moindre privilège** au rôle d'instance, renforcer la surveillance.

**REX.** Généraliser la version renforcée des métadonnées et le filtrage sortant (egress filtering), revoir les rôles d'instance (moindre privilège), ajouter une détection « accès applicatif au point de métadonnées », intégrer un test SSRF aux campagnes DAST (ch. 297).

⚠️ **Erreurs à éviter.** Corriger la SSRF sans roter les identifiants déjà exposés ; laisser le service de métadonnées en version permissive ; conserver un rôle d'instance surprivilégié.

🎯 **À retenir.** Une SSRF côté web devient un vol d'identifiants côté cloud : la réponse couvre les *deux* surfaces (corriger le code + roter le rôle + durcir les métadonnées). Prévention de fond : allowlist SSRF, métadonnées renforcées, moindre privilège des rôles.

---

> **Synthèse de la Partie 14.** Ces six cas illustrent un invariant : un incident traverse presque toujours *plusieurs surfaces* (un phishing devient un incident identité ; une SSRF devient un incident cloud ; un malware de poste devient un vol d'identifiants). Le réflexe opérationnel est donc : **comprendre la portée complète avant d'agir**, **confiner sans détruire les preuves**, **éradiquer exhaustivement** (toute la persistance) *avant* de **rétablir depuis du sain**, puis **apprendre** (REX). C'est l'application vivante du fil rouge et de la posture *assume breach*.

---

# Annexes

## Annexe A — Glossaire cyber essentiel

- **Actif** : ce qui a de la valeur et qu'on protège (donnée, service, système, identité).
- **Menace** : danger potentiel (acteur/événement) pouvant nuire.
- **Vulnérabilité** : faiblesse exploitable.
- **Risque** : combinaison vraisemblance × impact d'une menace exploitant une vulnérabilité.
- **Impact** : gravité des conséquences.
- **CIA/DIC** : Confidentialité, Intégrité, Disponibilité.
- **Authentification** : prouver son identité. **Autorisation** : déterminer ses droits.
- **Surface d'attaque** : ensemble des points exploitables.
- **Défense en profondeur** : empilement de couches indépendantes.
- **Moindre privilège** : droits strictement nécessaires.
- **Zero Trust** : ne jamais faire confiance par défaut, toujours vérifier.
- **Assume breach** : supposer la compromission pour mieux limiter/détecter/répondre.
- **Tiering** : cloisonnement des niveaux d'administration (Tier 0/1/2).
- **MFA** : authentification multi-facteur ; *résistant au phishing* = FIDO2/passkeys, number matching.
- **EDR/NDR/SIEM/SOAR** : détection/réponse hôte / réseau / corrélation centrale / automatisation.
- **IOC/IOA/TTP** : indicateur de compromission / d'attaque / tactiques-techniques-procédures.
- **CVE/CVSS/EPSS/KEV** : identifiant de vulnérabilité / score de gravité / probabilité d'exploitation / catalogue d'exploitation active.
- **SBOM** : inventaire des composants logiciels.
- **PRA/PCA** : reprise / continuité d'activité ; **RTO/RPO** : délai de reprise / perte de données acceptables.
- **Lateral movement** : déplacement interne de l'attaquant.
- **RCE** : exécution de code à distance.
- **Pentest / bug bounty / purple teaming** : test offensif ponctuel / continu communautaire / collaboration red-blue.

## Annexe B — Tableau de correspondance central (fiche réflexe)

> **Tableau-pivot du référentiel** (enrichi en V2). Pour chaque attaque majeure : famille, vulnérabilité-racine, surface, propriété CIA visée, **logs utiles** (où chercher), **défenses principales**. C'est l'outil pratique à garder sous la main pour relier *attaque ↔ vulnérabilité ↔ surface ↔ impact ↔ détection ↔ défense* en une ligne.

| Attaque | Famille | Vulnérabilité-racine | Surface | Impact CIA | Logs utiles | Défenses principales |
|---|---|---|---|---|---|---|
| Stored XSS | Injection | Encodage de sortie absent | Web | Confidentialité / Intégrité | Logs applicatifs, rapports CSP, WAF | Encodage contextuel, CSP, cookies HttpOnly |
| Reflected/DOM XSS | Injection | Sortie/sink non sécurisés | Web / navigateur | Confidentialité | Logs app, CSP, analyse JS client | Encodage, CSP, Trusted Types |
| SQLi | Injection | Requête concaténée | Web / base | Confidentialité / Intégrité | Erreurs SQL, logs base/app, WAF | Requêtes paramétrées, moindre privilège base |
| Command injection | Injection | Concaténation vers shell | Web / serveur | C/I/Disponibilité | EDR serveur (processus enfants), logs app | API sans shell, allowlist, moindre privilège |
| SSTI | Injection | Entrée dans la structure du template | Web / serveur | C/I/D (RCE) | Logs app, EDR, comportement d'évaluation | Données en variables (jamais en template), sandbox |
| XXE | Parsing | Entités externes XML activées | Web / API | Confidentialité (+SSRF) | Logs app, accès fichiers/réseau du parser | Désactiver entités externes & DOCTYPE |
| IDOR / BOLA | Contrôle d'accès | Défaut d'autorisation par objet | Web / API | Confidentialité / Intégrité | Logs API (accès hors périmètre), énumération d'IDs | Contrôle d'accès par objet côté serveur, deny by default |
| BFLA | Contrôle d'accès | Défaut d'autorisation par fonction | API | Intégrité / privilège | Logs API (appels privilégiés) | Contrôle d'autorisation par fonction, séparation des rôles |
| SSRF → métadonnées | Falsification requête | Validation/allowlist d'URL insuffisante | Web / cloud | Confidentialité (secrets) | Proxy/app, NDR, accès au point de métadonnées, audit cloud | Allowlist, egress filtering, métadonnées renforcées, moindre privilège du rôle |
| CSRF | Falsification requête | Pas de jeton anti-CSRF / SameSite | Web | Intégrité | Logs app (requêtes sans jeton/origine incohérente) | Jetons anti-CSRF, SameSite, vérification d'origine |
| Path traversal / LFI / Zip Slip | Accès fichiers | Chemin dérivé d'une entrée | Web / serveur | Confidentialité (+RCE) | Logs app (séquences de traversée), accès fichiers | Allowlist mappée, normaliser puis vérifier l'appartenance |
| Unrestricted upload | Accès fichiers | Type/emplacement non contrôlés | Web | C/I/D (RCE) | Logs upload, EDR, accès aux fichiers servis | Valider le contenu réel, stockage hors webroot, domaine isolé |
| Insecure deserialization | Intégrité logicielle | Désérialisation d'entrée non fiable | Web / serveur | C/I/D (RCE) | EDR (instanciation/processus), logs app | Ne pas désérialiser le non fiable, signer/typer strictement |
| Request smuggling | Parsing protocole | Désaccord de framing entre serveurs | Web / infra | Intégrité / Confidentialité | Logs frontal/back incohérents, outils dédiés | Normaliser au frontal, rejeter l'ambiguïté, HTTP cohérent |
| Cache poisoning / deception | Infra web | Clé de cache incomplète / cache de privé | Web / CDN | Intégrité / Confidentialité | Logs cache/CDN, réponses incohérentes | Clé de cache complète, ne jamais cacher le privé |
| Bucket public | Mauvaise configuration | Accès public par défaut | Cloud | Confidentialité | CSPM, audit cloud, accès anonymes | Blocage public par défaut, CSPM, chiffrement |
| Clé/secret exposé | Exposition de secrets | Secret hors coffre | Cloud / CI-CD | Confidentialité | Secrets scanning, audit cloud (usage de clé) | Coffre-fort, portée minimale, rotation, scanning |
| Privilege escalation cloud | Autorisation cloud | Permissions IAM dangereuses | Cloud | C/I/privilège | Audit IAM (modif. politiques/rôles) | Moindre privilège, suppression des chemins d'auto-élévation |
| Kubernetes RBAC abuse | Autorisation conteneurs | RBAC trop large | Conteneurs | C/I/privilège | Audit Kubernetes, API server | Moindre privilège RBAC, comptes de service minimaux |
| Container escape | Élévation conteneurs | Conteneur privilégié / montages | Conteneurs | C/I/D | Runtime security, EDR, audit | Conteneurs non privilégiés, capacités/montages minimaux |
| Dependency confusion / typosquat | Supply chain | Résolution de paquets | CI-CD / dépendances | C/I/D (RCE) | Logs build, résolution de sources | Dépôts internes prioritaires, lockfiles, SBOM/SCA |
| CI/CD / pipeline poisoning | Supply chain | Build/pipeline non protégé | CI-CD | C/I/D | Logs CI, intégrité des artefacts | Moindre privilège, isolation, provenance/signature (SLSA) |
| Password spraying | Authentification | Mots de passe faibles, pas de MFA | Identité | C/privilège | Auth logs (échecs multi-comptes), sign-in logs | MFA, bannissement de mots de passe courants, détection de spraying |
| Credential stuffing | Authentification | Réutilisation de mots de passe | Identité / SaaS | Confidentialité | Sign-in logs (taux d'échec élevé, sources distribuées) | MFA, détection d'identifiants fuités, rate limiting |
| Kerberoasting | Identité (AD) | Compte de service/SPN + mot de passe faible | Active Directory | Confidentialité / privilège | Kerberos 4769 (TGS-REQ + chiffrement faible), EDR | gMSA, mots de passe longs, tiering, détection comportementale |
| Pass-the-hash / ticket | Identité (AD) | Réutilisation de secrets + privilèges excessifs | Active Directory | Privilège / latéral | Auth NTLM/Kerberos anormales, EDR | Tiering, LAPS, Credential Guard, restriction NTLM |
| DCSync | Identité (AD) | Droits de réplication excessifs | Active Directory | Confidentialité (secrets domaine) | Réplication depuis hôte non-DC, audit droits | Restreindre/surveiller les droits de réplication (Tier 0) |
| Golden ticket | Identité (AD) | Secret krbtgt compromis | Active Directory | Privilège / persistance | Tickets aux propriétés anormales (durée/chiffrement) | Protéger krbtgt, double rotation post-incident, surveillance DC |
| AD CS abuse | Identité (AD) | Modèles de certificats permissifs | Active Directory | Privilège / persistance | Inscriptions de certificats anormales, audit CA | Durcir modèles & droits, CA en Tier 0 |
| Lateral movement | Mouvement latéral | Réutilisation d'identifiants + réseau plat | Réseau / AD | Latéral / privilège | Connexions inter-machines, EDR/NDR, SIEM | Segmentation, tiering, LAPS, MFA admin |
| Ransomware | Impact (multi) | Accès + propagation + privilèges | Multi | Disponibilité (+Confidentialité) | EDR (chiffrement, suppression clichés), auth, exfiltration | Sauvegardes immuables/testées, segmentation, MFA, tiering, détection précoce |
| Wiper | Impact (destruction) | Accès + sabotage | Multi | Disponibilité / Intégrité | EDR (destruction), comportements | Sauvegardes hors-ligne, segmentation, continuité |
| Infostealer | Malware (vol) | Malware sur poste + secrets accessibles | Poste / identité | Confidentialité | EDR (accès aux stockages de secrets), connexions par jeton | EDR, expiration de session, MFA anti-phishing |
| Phishing | Ingénierie sociale | Confiance humaine, pas de MFA fort | Messagerie / humain | Confidentialité | Sign-in logs, logs mail/proxy, création de règles de boîte | Sensibilisation, filtrage mail, SPF/DKIM/DMARC, MFA anti-phishing |
| BEC | Ingénierie sociale | Confiance + pas de double validation | Messagerie / humain | Intégrité (fraude) | Logs mail (expéditeur/domaine), règles de boîte | Double validation hors canal, séparation des tâches, DMARC |
| Consent phishing | Ingénierie sociale / OAuth | Octroi OAuth non gouverné | SaaS / identité | Confidentialité / persistance | Journaux d'octrois OAuth | Gouvernance des consentements OAuth, allowlist d'applications |
| MFA fatigue | Contournement MFA | Push simple (approuver/refuser) | Identité | Privilège / accès | Volume anormal de demandes MFA, approbation après rafale | MFA résistant au phishing (FIDO2, number matching) |
| ARP/DNS/DHCP spoofing → MITM | Usurpation réseau | Protocoles non authentifiés | Réseau | Confidentialité / Intégrité | NDR, anomalies d'association, alertes WIPS | DAI, DHCP snooping, chiffrement authentifié, DNSSEC |
| DNS tunneling | Exfiltration / C2 | DNS sortant non inspecté | Réseau | Confidentialité | Logs DNS (volume/entropie/fréquence), NDR | Inspection/filtrage DNS, détection d'anomalies |
| DDoS | Disponibilité | Capacité finie / spoofing | Réseau | Disponibilité | NetFlow, signatures DDoS, alertes amont | Anti-DDoS amont (scrubbing/CDN), anti-spoofing (BCP38) |
| BGP hijacking | Routage | Confiance BGP non validée | Infra Internet | Intégrité / Disponibilité | Monitoring BGP, anomalies de chemins | RPKI, filtrage de préfixes, MANRS |

🧭 **Mode d'emploi.** Lire une ligne de gauche à droite, c'est dérouler le fil rouge sur une attaque : *où elle frappe* (surface), *pourquoi elle marche* (vulnérabilité-racine), *ce qu'elle vise* (CIA), *où la voir* (logs), *comment l'arrêter* (défenses). Pour une attaque inconnue, appliquer d'abord la méthode du chapitre 306, puis l'inscrire dans ce format.

## Annexe C — Tableau surface → attaques typiques → logs utiles

| Surface | Attaques typiques | Sources de logs utiles |
|---|---|---|
| Poste utilisateur | Phishing, malware, infostealer | EDR, logs système, proxy/DNS |
| Active Directory | Kerberoasting, DCSync, pass-the-hash | Journaux AD/Kerberos, EDR, SIEM |
| Application web | XSS, SQLi, IDOR, SSRF | Logs applicatifs, WAF, accès HTTP |
| API | BOLA, BFLA, exposition de données | Logs API/passerelle |
| Cloud | Buckets publics, IAM, métadonnées | Journaux cloud (audit), CSPM |
| Réseau | Scan, MITM, lateral movement | NDR/IDS, flux (NetFlow), DNS |
| Messagerie | Phishing, BEC, malspam | Logs mail, DMARC reports |
| Conteneurs/K8s | RBAC abuse, container escape | Audit Kubernetes, runtime security |

## Annexe D — Tableau de correspondance des cadres

| Besoin | Cadre de référence |
|---|---|
| Fonctions de sécurité de haut niveau | NIST CSF 2.0 (Govern, Identify, Protect, Detect, Respond, Recover) |
| Tactiques/techniques adverses | MITRE ATT&CK |
| Contre-mesures défensives | MITRE D3FEND |
| Patterns d'attaque | MITRE CAPEC |
| Faiblesses logicielles | CWE |
| Risques applicatifs web | OWASP Top 10 |
| Risques API | OWASP API Security Top 10 (2023) |
| Vérification applicative | OWASP ASVS |
| Intégrité de la supply chain | SLSA, SBOM |
| Analyse de risque | EBIOS RM, ISO 27005, FAIR |
| Gestion de la sécurité | ISO/IEC 27001 |

**Logique de lecture :** ATT&CK décrit *ce que fait l'attaquant* ; CWE/CAPEC, *par quelle faiblesse/pattern* ; D3FEND, *comment se défendre* ; NIST CSF, *comment organiser le tout* ; OWASP, *les risques applicatifs concrets*.

## Annexe E — Fiches réflexes

**XSS** — Encoder la sortie selon le contexte ; CSP ; cookies HttpOnly ; assainir le HTML riche. *Racine : injection côté navigateur.*

**SQLi** — Requêtes paramétrées partout (y compris données stockées) ; moindre privilège base ; erreurs génériques. *Racine : injection SQL.*

**SSRF** — Allowlist de destinations ; bloquer plages internes et service de métadonnées ; filtrage sortant ; durcir les rôles d'instance. *Racine : confiance dans une URL fournie.*

**Phishing** — Sensibilisation + culture du signalement ; filtrage mail ; SPF/DKIM/DMARC ; MFA résistant au phishing. *Racine : manipulation humaine.*

**Ransomware** — Sauvegardes immuables/testées ; segmentation ; MFA ; EDR ; patch ; tiering ; plan de crise/PRA. *Racine : multiple (accès + propagation).*

**Compromission AD** — Tiering (protéger le Tier 0/krbtgt) ; PAM/bastion ; LAPS ; Credential Guard ; audit ACL/délégations/GPO ; surveillance. *Racine : exposition/réutilisation de secrets privilégiés.*

## Annexe F — Mini-cas d'analyse défensive

**Cas 1 — Alerte « connexion réussie après 200 échecs sur 200 comptes ».**
Classer : authentification, password spraying (chapitre 165). Réponse : confiner le compte réussi, vérifier MFA, chercher le mouvement latéral. Fond : MFA + détection de spraying.

**Cas 2 — Un serveur web initie des requêtes vers l'adresse interne de métadonnées.**
Classer : SSRF vers métadonnées cloud (chapitre 107). Réponse : couper, vérifier l'usage des identifiants de rôle, roter. Fond : allowlist SSRF + métadonnées renforcées + moindre privilège.

**Cas 3 — Chiffrement massif de fichiers + suppression de clichés sur plusieurs serveurs.**
Classer : ransomware (chapitre 188), avec lateral movement. Réponse : confiner/segmenter, déclencher la cellule de crise et le PRA, restaurer depuis l'immuable. Fond : sauvegardes immuables + segmentation + MFA + tiering.

## Annexe G — Cartographie des métiers cyber

- **SOC analyst (N1/N2/N3)** : détection, triage, qualification, réponse de premier niveau.
- **Incident responder / DFIR** : investigation, forensic, éradication, rétablissement.
- **Threat intelligence (CTI)** : connaissance des menaces, acteurs, TTP, alimentation de la détection.
- **Pentester / Red team** : test offensif autorisé, simulation d'adversaire.
- **Blue team / Detection engineer** : construction et réglage des détections.
- **Purple team** : pont red/blue pour améliorer la détection.
- **GRC / Risk manager** : gouvernance, analyse de risque, conformité, homologation.
- **Security architect** : conception sécurisée (secure by design, Zero Trust).
- **AppSec / Product security** : sécurité du développement (SAST/DAST, threat modeling).
- **Cloud security engineer** : sécurité des environnements cloud (IAM, configuration, CSPM).
- **IAM/PAM engineer** : identités, accès, comptes privilégiés.
- **RSSI / CISO** : pilotage stratégique de la sécurité.

🧭 Ces métiers se répartissent sur le fil rouge : *prévenir* (architecture, AppSec, GRC), *détecter/répondre* (SOC, DFIR, CTI), *évaluer* (pentest, purple), *gouverner* (RSSI, GRC).

## Annexe H — Apprendre les attaques sans apprendre à attaquer illégalement

Principes pour progresser de façon **légale et éthique** :

1. **Comprendre les mécanismes, pas les payloads** : ce cours privilégie le *pourquoi ça marche* et *comment s'en défendre*.
2. **S'entraîner uniquement dans des environnements autorisés** : laboratoires personnels isolés, plateformes d'entraînement légales et dédiées, machines virtuelles vous appartenant, environnements de CTF/lab conçus pour cela.
3. **N'attaquer que ce qu'on est explicitement autorisé à tester** : un test sur un système sans autorisation écrite est illégal, même « pour apprendre ».
4. **Privilégier la posture défensive (blue/purple)** : détecter, comprendre les TTP (ATT&CK), construire des détections — une voie d'apprentissage riche et sans risque légal.
5. **Pratiquer la divulgation responsable** : si l'on découvre une faille, la signaler par les canaux prévus (bug bounty, contact sécurité), jamais l'exploiter.
6. **Se former via les cadres** : ATT&CK, OWASP, CWE/CAPEC, D3FEND offrent une montée en compétence structurée et légale.

⚠️ La frontière est simple : la *connaissance* est libre ; l'*action* sur un système exige une *autorisation*. Ce cours vise la première et la défense.

## Annexe I — Bibliographie indicative et standards à surveiller

- **NIST Cybersecurity Framework 2.0** — organisation des fonctions de sécurité.
- **MITRE ATT&CK** — base de connaissances des TTP adverses (à suivre, mise à jour régulière).
- **MITRE D3FEND** — contre-mesures défensives.
- **MITRE CAPEC** — patterns d'attaque.
- **CWE** — faiblesses logicielles (Top 25 mis à jour périodiquement).
- **OWASP Top 10** (web) et **OWASP API Security Top 10** (API) — révisés régulièrement.
- **OWASP ASVS** — exigences de vérification applicative.
- **ISO/IEC 27001 / 27005** — management et risque.
- **EBIOS Risk Manager (ANSSI)** — méthode d'analyse de risque.
- **CIS Benchmarks / CIS Controls** — durcissement et contrôles prioritaires.
- **SLSA** et travaux SBOM (formats type CycloneDX/SPDX) — intégrité de la supply chain.
- **Catalogue KEV (CISA)** — vulnérabilités activement exploitées, pour prioriser.

> **Note de mise à jour.** La cybersécurité évolue vite : versions de référentiels, nouvelles techniques, nouveaux outils. La *taxonomie* de ce référentiel (les familles et les principes) reste stable ; les *détails* (versions, CVE, produits) doivent être réactualisés via les sources ci-dessus.

## Annexe J — Schémas mentaux (ASCII)

> Quelques cartes mentales minimalistes à mémoriser. En cybersécurité, un bon schéma vaut souvent un paragraphe.

**Le fil rouge du référentiel**
```text
ACTIF → MENACE → VULNÉRABILITÉ → RISQUE → ATTAQUE → IMPACT → DÉTECTION → RÉPONSE → REMÉDIATION
```

**Chaîne d'un chemin d'attaque typique (du clic au domaine)**
```text
Phishing/Exploit → Poste compromis → Vol d'identifiants → Mouvement latéral → Tier 0 → Domaine compromis
   (Initial Access)   (Execution)      (Credential Access)   (Lateral Mvt)     (PrivEsc)   (Impact)
```

**SSRF → cloud (deux surfaces)**
```text
Attaquant → Application vulnérable (URL fournie) → Service de métadonnées → Identifiants de rôle → Ressources cloud
            [allowlist + egress filtering]          [métadonnées renforcées]  [moindre privilège du rôle]
```

**Injection (principe unique, plusieurs interpréteurs)**
```text
Entrée non fiable ─┬─► Navigateur  → XSS
                   ├─► SQL         → SQLi
                   ├─► Shell       → Command injection
                   ├─► LDAP/XPath  → LDAP/XPath injection
                   └─► Template    → SSTI
   Parade commune : SÉPARER données et code (paramétrage + encodage de sortie)
```

**Cycle de réponse à incident**
```text
Événement → Alerte → Triage → Qualification → [Incident] → Investigation →
Confinement → Éradication → Rétablissement → REX ──(boucle d'amélioration)──► Préparation
```

**Tiering Active Directory (étanchéité)**
```text
Tier 0  [Contrôleurs de domaine, krbtgt, IAM, AD CS]   ◄── ne jamais exposer ses identifiants plus bas
   ▲ (jamais de contrôle depuis le bas)
Tier 1  [Serveurs & applications]
   ▲
Tier 2  [Postes de travail]
```

**Défense en profondeur (un mail malveillant face aux couches)**
```text
Mail → [Filtrage mail] → [Sensibilisation] → [EDR] → [Moindre privilège] → [Segmentation] → [Détection SOC]
        chaque couche peut faillir ; l'attaquant doit TOUTES les franchir
```

**Pyramide de la douleur (valeur de la détection)**
```text
        TTP        ◄── le plus douloureux pour l'attaquant (change ses méthodes)
      Outils
   Artefacts réseau/hôte
      Noms de domaine
        IOC (hash, IP)  ◄── le moins douloureux (changé en un instant)
```

🎯 **À retenir** — Ces schémas condensent les invariants du référentiel : un même principe (injection, défense en profondeur, tiering, cycle d'incident) se décline partout. Les mémoriser, c'est tenir la carte mentale en tête.

---

> **Fin du référentiel.**
>
> Vous disposez désormais d'une cartographie complète et structurée de la cybersécurité : **14 parties, 319 chapitres** (dont 6 cas filés d'investigation), des fondations au raisonnement SOC/IR, reliées par un fil rouge unique et outillées de tableaux de correspondance et de schémas mentaux. L'objectif n'était pas de tout mémoriser, mais d'acquérir la **carte mentale** qui permet de *classer, relier, défendre et répondre* — y compris face à des menaces jamais rencontrées.
>
> Ce document est un **référentiel-pivot** : la colonne vertébrale d'une bibliothèque cyber. Les cours spécialisés (CTI, forensic, AD, cloud, web, malware…) approfondissent ensuite chaque territoire que cette carte permet de situer.
>
> *« Comprendre les familles, c'est comprendre les attaques qu'on n'a jamais vues. »*
