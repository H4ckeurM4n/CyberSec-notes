# DIGITAL FORENSICS

*Acquisition • Analyse • Preuve • Rapport*

**Cours complet — 33 chapitres • 8 parties • 6 annexes**

*Forensic judiciaire • Triage DFIR • Investigation numérique*

---

## Table des matières

- [Fil rouge : Opération MUSIC BOX](#fil-rouge--opération-music-box)
- **PARTIE I — FONDATIONS (Ch.1-4)**
  - [Ch.1 — Qu'est-ce que le digital forensics](#chapitre-1--quest-ce-que-le-digital-forensics)
  - [Ch.2 — Cadre juridique et recevabilité de la preuve](#chapitre-2--cadre-juridique-et-recevabilité-de-la-preuve)
  - [Ch.3 — Méthodologie forensic et posture d'enquêteur](#chapitre-3--méthodologie-forensic-et-posture-denquêteur)
  - [Ch.4 — Environnement technique et outils fondamentaux](#chapitre-4--environnement-technique-et-outils-fondamentaux)
- **PARTIE II — ACQUISITION DE PREUVES (Ch.5-8)**
  - [Ch.5 — Acquisition disque et supports de stockage](#chapitre-5--acquisition-disque-et-supports-de-stockage)
  - [Ch.6 — Acquisition mémoire vive (RAM)](#chapitre-6--acquisition-mémoire-vive-ram)
  - [Ch.7 — Acquisition réseau et captures de trafic](#chapitre-7--acquisition-réseau-et-captures-de-trafic)
  - [Ch.8 — Acquisition des logs, des données d'identité et du cloud](#chapitre-8--acquisition-des-logs-des-données-didentité-et-du-cloud)
- **PARTIE III — ANALYSE FONDAMENTALE ET RAISONNEMENT FORENSIC (Ch.9-11)**
  - [Ch.9 — Systèmes de fichiers : comprendre ce qu'on analyse](#chapitre-9--systèmes-de-fichiers--comprendre-ce-quon-analyse)
  - [Ch.10 — Timeline analysis et corrélation temporelle](#chapitre-10--timeline-analysis-et-corrélation-temporelle)
  - [Ch.11 — Corrélation, raisonnement analytique et gestion des biais](#chapitre-11--corrélation-raisonnement-analytique-et-gestion-des-biais)
- **PARTIE IV — ANALYSE FORENSIC AVANCÉE (Ch.12-18)**
  - [Ch.12 — Windows forensics : registre et artefacts d'exécution](#chapitre-12--windows-forensics--registre-et-artefacts-dexécution)
  - [Ch.13 — Windows forensics : activité utilisateur, navigateur et mouvement latéral](#chapitre-13--windows-forensics--activité-utilisateur-navigateur-et-mouvement-latéral)
  - [Ch.14 — Windows forensics : Event Logs et journaux d'audit](#chapitre-14--windows-forensics--event-logs-et-journaux-daudit)
  - [Ch.15 — Linux forensics](#chapitre-15--linux-forensics)
  - [Ch.16 — macOS forensics](#chapitre-16--macos-forensics)
  - [Ch.17 — Memory forensics](#chapitre-17--memory-forensics)
  - [Ch.18 — Malware forensics](#chapitre-18--malware-forensics)
- **PARTIE V — INVESTIGATION RÉSEAU ET IDENTITÉ (Ch.19-21)**
  - [Ch.19 — Network forensics](#chapitre-19--network-forensics)
  - [Ch.20 — Active Directory forensics](#chapitre-20--active-directory-forensics)
  - [Ch.21 — Investigation des identités hybrides, du cloud et des accès distants](#chapitre-21--investigation-des-identités-hybrides-du-cloud-et-des-accès-distants)
- **PARTIE VI — FORENSIC SPÉCIALISÉ (Ch.22-25)**
  - [Ch.22 — Email forensics et messagerie](#chapitre-22--email-forensics-et-messagerie)
  - [Ch.23 — Mobile forensics](#chapitre-23--mobile-forensics)
  - [Ch.24 — Anti-forensics : comprendre et détecter](#chapitre-24--anti-forensics--comprendre-et-détecter)
  - [Ch.25 — Investigation des mécanismes de persistance](#chapitre-25--investigation-des-mécanismes-de-persistance)
- **PARTIE VII — FINALISATION ET PRODUCTION (Ch.26-29)**
  - [Ch.26 — Rapport forensic et expertise judiciaire](#chapitre-26--rapport-forensic-et-expertise-judiciaire)
  - [Ch.27 — Forensic readiness : préparer l'organisation](#chapitre-27--forensic-readiness--préparer-lorganisation)
  - [Ch.28 — Forensic et incident response : intégration opérationnelle](#chapitre-28--forensic-et-incident-response--intégration-opérationnelle)
  - [Ch.29 — Forensic automation et scripting](#chapitre-29--forensic-automation-et-scripting)
- **PARTIE VIII — APPLICATION ET SYNTHÈSE (Ch.30-33)**
  - [Ch.30 — Cas complet : compromission Windows avec mouvement latéral et exfiltration](#chapitre-30--cas-complet--compromission-windows)
  - [Ch.31 — Cas complet : investigation insider threat](#chapitre-31--cas-complet--investigation-insider-threat)
  - [Ch.32 — Cas complet : investigation serveur Linux compromis](#chapitre-32--cas-complet--investigation-serveur-linux-compromis)
  - [Ch.33 — Cas complet : compromission AD et identités hybrides cloud](#chapitre-33--cas-complet--compromission-ad-et-identités-hybrides-cloud)
- **ANNEXES**
  - [Annexe A — Glossaire forensic](#annexe-a--glossaire-forensic)
  - [Annexe B — Cheat sheets outils](#annexe-b--cheat-sheets-outils)
  - [Annexe C — Artefacts Windows : référence rapide](#annexe-c--artefacts-windows--référence-rapide)
  - [Annexe D — Artefacts Linux et macOS : référence rapide](#annexe-d--artefacts-linux-et-macos--référence-rapide)
  - [Annexe E — Templates](#annexe-e--templates)
  - [Annexe F — Ressources et certifications](#annexe-f--ressources-et-certifications)

---

## Fil rouge : Opération MUSIC BOX

> **Contexte narratif — ce fil rouge traverse les 29 premiers chapitres du cours.**
>
> **Vendredi 7 mars 2026, 17h12.** L'EDR CrowdStrike Falcon déployé chez **NovaPharma** — laboratoire pharmaceutique français de 800 collaborateurs, spécialisé dans la recherche sur les molécules anticancéreuses, coté sur Euronext Growth — déclenche une alerte de sévérité « critique » : un processus `svchost.exe` avec un arbre de parenté anormal (parent : `explorer.exe` au lieu de `services.exe`) tente d'accéder au processus LSASS (Local Security Authority Subsystem Service) sur le poste de travail d'un chercheur du département R&D.
>
> L'analyste SOC, **Romain Vasquez**, qualifie l'alerte comme un vrai positif de gravité élevée : l'accès à LSASS est un indicateur classique de credential dumping (technique T1003 ATT&CK). Le poste n'est pas isolé immédiatement — Romain contacte d'abord l'IR lead, **Claire Desjardins**, pour cadrer la réponse.
>
> L'investigation forensic va progressivement révéler une compromission qui remonte à J-60 : un spearphishing ciblé avec un document Word piégé (macro VBA → téléchargement d'un RAT custom via certutil), une élévation de privilèges via Kerberoasting sur un compte de service avec droits Domain Admin, un mouvement latéral via PsExec et RDP vers le serveur R&D Linux (Ubuntu 22.04, données de recherche sur la molécule NP-427), une exfiltration de 180 Go de données R&D vers un bucket S3 AWS via rclone, des tentatives d'anti-forensics (timestomping sur les fichiers accédés, effacement partiel des Security Event Logs), et un RAT custom avec capacités de keylogging, screenshot, et file listing.
>
> L'enquête posera des questions méthodologiques à chaque chapitre : comment préserver la RAM avant que l'admin ne redémarre le poste, comment distinguer un svchost légitime d'un svchost injecté dans le dump mémoire, comment reconstituer la timeline de 60 jours de compromission, comment tracer le mouvement latéral entre Windows et Linux, comment identifier le Kerberoasting dans les Event Logs AD, comment prouver l'exfiltration via les logs proxy et AWS CloudTrail, comment détecter le timestomping par comparaison $STANDARD_INFORMATION/$FILE_NAME, et comment produire un rapport exploitable à la fois par le juge d'instruction et par le COMEX de NovaPharma.
>
> L'équipe forensic : Claire Desjardins (IR lead et forensicienne senior), Romain Vasquez (analyste SOC/forensic junior), et **Maître Élise Fournier** (experte judiciaire inscrite à la cour d'appel de Paris, mandatée dès le samedi pour sécuriser la chaîne de custody en vue d'une judiciarisation probable).

---

## PARTIE I — FONDATIONS

*Cette première partie pose les bases indispensables avant toute investigation. Elle répond aux questions que tout analyste forensic doit maîtriser avant de toucher un clavier : qu'est-ce que le forensic numérique, dans quel cadre juridique il s'inscrit, quelle méthodologie il suit, avec quels outils il opère, et avec quelle posture intellectuelle il raisonne.*

---

### Chapitre 1 — Qu'est-ce que le digital forensics

#### 1.1 Définition : science de la preuve numérique

Le digital forensics — ou investigation numérique — est la discipline scientifique qui consiste à identifier, préserver, collecter, analyser et présenter des preuves numériques de manière à ce qu'elles soient recevables devant un tribunal ou exploitables pour une décision stratégique. Le mot clé est « scientifique » : le forensic n'est pas du bricolage technique, c'est un processus rigoureux, reproductible et documenté.

Le forensic numérique répond à des questions fondamentales : que s'est-il passé, quand, comment, par qui, et quelles données ont été impactées. Ces questions sont les mêmes qu'en criminalistique physique (qui a commis l'acte, avec quel outil, où, quand), transposées au monde numérique. Et comme en criminalistique physique, la qualité de la collecte de preuves détermine la qualité des conclusions. Un disque mal acquis, un log non préservé, un dump mémoire raté : autant de scènes de crime contaminées dont les conclusions seront contestables.

La particularité du numérique est la volatilité : contrairement à une empreinte digitale sur une poignée de porte, une connexion réseau disparaît quand le processus se termine, un fichier supprimé peut être écrasé par le système d'exploitation en quelques minutes sur un SSD, et un redémarrage de machine efface la mémoire vive avec tout ce qu'elle contenait — credentials en clair, processus malveillants, connexions C2 actives. L'urgence de la préservation est la contrainte fondamentale du forensic numérique.

#### 1.2 Forensic ≠ incident response ≠ pentest ≠ threat intel

Le forensic s'inscrit dans un écosystème plus large de cybersécurité, et les confusions de posture entre disciplines sont fréquentes et dommageables.

Le **digital forensics** cherche à comprendre ce qui s'est passé et à produire des preuves exploitables. Son tempo est long (jours à semaines), sa contrainte clé est l'intégrité des preuves et la rigueur méthodologique. L'**incident response** cherche à contenir l'attaque, éradiquer la menace, et restaurer le service. Son tempo est court (heures à jours), sa contrainte clé est la rapidité et la continuité d'activité. Le **pentest / red team** cherche à trouver les vulnérabilités avant les attaquants. Son tempo est planifié (semaines), sa contrainte est le périmètre autorisé. La **threat intelligence** cherche à comprendre les menaces, les acteurs, et les tendances. Son tempo est continu, sa contrainte est la qualité des sources et la prudence de l'attribution.

En pratique, ces disciplines interagissent constamment. Le SOC détecte une alerte, l'IR qualifie et contient, le forensic investigue en profondeur, et la CTI contextualise (quel groupe, quelles TTP, quel objectif). Le forensic peut aussi intervenir hors incident : investigation sur un employé suspect (insider threat), due diligence lors d'une acquisition d'entreprise, analyse d'un litige commercial (preuve de suppression de fichiers), ou expertise judiciaire ordonnée par un magistrat.

Le cours IR de la bibliothèque traite de l'orchestration de la réponse ; le cours CTI/Écosystèmes traite de la contextualisation de la menace. Ce cours traite de l'investigation technique et de la production de preuves.

#### 1.3 Les branches du forensic

Le forensic numérique se décline en plusieurs spécialités, chacune avec ses artefacts, ses outils et ses contraintes. Ces spécialités ne sont pas cloisonnées — une investigation complète les combine presque toujours.

Le **disk forensics** (analyse de supports de stockage) est la branche historique : acquisition bit-à-bit d'un disque, analyse du système de fichiers, récupération de fichiers supprimés, analyse des métadonnées et des artefacts système. C'est le socle du cours (Parties II-IV). Le **memory forensics** (analyse de mémoire vive) capture l'état instantané du système — processus, connexions, credentials, malware fileless. C'est devenu incontournable avec la montée des attaques sans fichier (Ch.17). Le **network forensics** (analyse réseau) examine les captures de trafic et les logs réseau pour reconstituer les communications de l'attaquant et caractériser l'exfiltration (Ch.19). Le **mobile forensics** analyse les smartphones et tablettes — terminaux qui contiennent souvent plus de données exploitables qu'un PC, mais avec des protections renforcées (Ch.23). Le **cloud forensics** investigue dans les environnements cloud (AWS, Azure, GCP, M365) avec des défis spécifiques : pas d'accès physique, données éphémères, multi-juridiction (Ch.21). Le **malware forensics** analyse le comportement d'un malware pour comprendre ses fonctionnalités et extraire les IoC, sans aller jusqu'au reverse engineering complet (Ch.18).

#### 1.4 La tension fondamentale : forensic judiciaire vs triage DFIR

C'est la distinction la plus structurante du cours, et elle conditionne chaque décision que l'analyste prendra sur le terrain.

Le **forensic judiciaire** vise à produire des preuves recevables devant un tribunal. L'exhaustivité prime sur la rapidité : chaque élément de preuve est acquis dans le respect de la chaîne de custody, hashé, documenté, et traçable. L'intégrité est absolue. Le tempo est long (jours à semaines). Le destinataire est un juge, un expert contradictoire, ou un procureur.

Le **triage DFIR** vise à comprendre rapidement ce qui se passe pour contenir la menace et éradiquer l'attaquant. La rapidité prime sur l'exhaustivité : on collecte les artefacts les plus parlants sur les machines les plus critiques, on analyse en parallèle, on produit des IoC pour le SOC. Le tempo est court (heures à jours). Le destinataire est l'IR lead, le SOC, et le RSSI.

En pratique, ces deux régimes ne s'excluent pas — ils s'articulent. La plupart des investigations commencent en mode triage (comprendre l'urgence) et basculent en mode judiciaire si les constatations le justifient (vol de données avéré, fraude, attaque étatique). Savoir quand et comment basculer est une compétence critique : le triage initial ne doit pas compromettre les preuves nécessaires à la judiciarisation. C'est pourquoi, même en triage, les bonnes pratiques de chaîne de custody et de hashing doivent être respectées dès le début — on ne sait jamais si l'affaire finira devant un juge.

Trois axes de tension traversent toute investigation : rapidité vs exhaustivité (collecter 80 % en 2 heures ou 100 % en 2 jours), continuité d'activité vs gel des preuves (laisser la machine en production ou la saisir), et investigation interne vs perspective judiciaire (souplesse méthodologique vs procédure stricte, scellés, expert judiciaire).

#### 1.5 Qui fait du forensic

Les acteurs du forensic sont variés. Les **CERT/CSIRT** (Computer Emergency Response Teams) combinent IR et forensic — en France, le CERT-FR (ANSSI) pour l'État et les OIV, les CSIRT sectoriels (santé, finance), et les CSIRT d'entreprise. Les **SOC** font du triage de premier niveau — qualification d'alertes, collecte initiale d'artefacts. Les **forces de l'ordre spécialisées** mènent les investigations judiciaires : le C3N (Centre de lutte contre les criminalités numériques, Gendarmerie), l'OCLCTIC (Office central de lutte contre la criminalité liée aux TIC), les ICC (Investigateurs en cybercriminalité) répartis dans les brigades territoriales, et la BL2C (Brigade de Lutte contre la Cybercriminalité, Préfecture de Police de Paris). Les **cabinets privés** et prestataires qualifiés PRIS interviennent pour des investigations internes, des due diligences, ou en appui des entreprises victimes. Les **experts judiciaires**, inscrits sur les listes des cours d'appel, sont mandatés par les magistrats pour les expertises contradictoires.

#### 1.6 Le forensic dans la chaîne cybersécurité

Le forensic s'insère dans une chaîne plus large : détection (le SOC identifie une alerte via le SIEM ou l'EDR) → qualification (l'analyste SOC confirme le vrai positif et évalue la gravité) → triage/investigation (l'équipe DFIR collecte les artefacts et analyse) → remédiation (éradication de la menace, restauration, durcissement) → judiciarisation éventuelle (dépôt de plainte, expertise judiciaire). Le forensic intervient principalement dans la phase triage/investigation, mais il prépare aussi la judiciarisation et alimente la remédiation. Le cours IR de la bibliothèque détaille l'ensemble de cette chaîne ; ce cours se concentre sur la phase forensic.

#### 1.7 Fil rouge — MUSIC BOX : l'alerte

> **🔬 MUSIC BOX — Épisode 1**
>
> Vendredi 7 mars 2026, 17h12. L'EDR déclenche sur le poste WKS-RD-047 (Windows 11, département R&D, utilisateur : Dr. Julien Mallet, chercheur principal sur la molécule NP-427). Alerte : « Process svchost.exe (PID 7284, parent: explorer.exe) attempting to access LSASS memory ».
>
> Romain (SOC) vérifie : svchost.exe avec explorer.exe comme parent est anormal — les svchost légitimes ont services.exe comme parent. L'accès à LSASS est un indicateur de credential dumping (T1003). C'est un vrai positif.
>
> Première décision : triage rapide ou investigation complète ? Claire (IR lead) tranche : triage immédiat pour évaluer la gravité (dump RAM du poste suspect, collecte des artefacts KAPE, vérification des connexions sortantes via le proxy). La machine n'est PAS éteinte, PAS isolée du réseau immédiatement — on veut d'abord comprendre avec qui elle communique. En parallèle, préservation de la chaîne de custody dès le début : l'experte judiciaire Maître Fournier est contactée et sera sur site samedi matin.
>
> La bascule vers une investigation complète sera décidée lundi, selon les premiers résultats. Mais la préservation des preuves commence maintenant — on ne sait pas encore si cette affaire finira devant un juge.

---

### Chapitre 2 — Cadre juridique et recevabilité de la preuve

#### 2.1 La preuve numérique en droit français

La preuve numérique est admissible en droit français, tant en matière pénale (Code de procédure pénale) qu'en matière civile et commerciale (Code civil, Code de commerce). Mais son admissibilité est conditionnée par trois principes fondamentaux qui guident toute la méthodologie forensic.

La **loyauté** signifie que la preuve doit avoir été obtenue par des moyens légaux et éthiques. Une preuve obtenue par piratage, par intrusion non autorisée dans un système tiers, ou en violation du droit du travail est irrecevable, quel que soit son contenu. En matière pénale, la jurisprudence est stricte : les preuves obtenues de manière déloyale par les forces de l'ordre sont annulées (principe posé par la chambre criminelle de la Cour de cassation). En matière civile, la jurisprudence a évolué : l'assemblée plénière de la Cour de cassation a admis en 2023 que des preuves obtenues de manière déloyale pouvaient être recevables si leur production était indispensable à l'exercice du droit à la preuve et proportionnée aux intérêts en jeu. Mais cette ouverture ne dispense pas de la rigueur.

L'**intégrité** garantit que la preuve n'a pas été altérée entre le moment de la collecte et le moment de la présentation. C'est le fondement de la chaîne de custody et du hashing : prouver qu'un fichier analysé est identique au fichier collecté, bit pour bit. Sans preuve d'intégrité, la partie adverse peut contester que la preuve a été modifiée — intentionnellement ou accidentellement.

Le **contradictoire** impose que la partie adverse puisse examiner, contester et faire contre-expertiser la preuve. C'est pourquoi la documentation méthodologique est aussi importante que l'analyse elle-même : il faut pouvoir expliquer exactement comment on a procédé, avec quels outils (nom, version, paramètres), et pourquoi, pour qu'un expert adverse puisse reproduire ou contester les résultats. Un rapport forensic techniquement brillant mais méthodologiquement opaque sera attaqué au contradictoire.

#### 2.2 Code de procédure pénale : perquisitions numériques

Les perquisitions numériques obéissent aux règles générales de la perquisition (autorisation judiciaire, présence de témoins, procès-verbal) adaptées au numérique. Les enquêteurs peuvent saisir les équipements informatiques ou, plus couramment dans la pratique actuelle, réaliser des copies forensic sur place (moins perturbant pour l'activité de l'entreprise). Les réquisitions (articles 60-1 et 77-1-1 du CPP) permettent d'obtenir des données auprès des fournisseurs de services (opérateurs télécom, hébergeurs, éditeurs SaaS, fournisseurs cloud) sans saisie physique. Les scellés numériques garantissent l'intégrité des supports saisis : le hash calculé au moment de la saisie est l'équivalent numérique du scellé physique apposé sur un sac de preuves.

L'accès aux données chiffrées est un enjeu croissant. L'article 434-15-2 du Code pénal punit le refus de remettre une convention de chiffrement (clé ou mot de passe) demandée par l'autorité judiciaire, mais en pratique, si le suspect ne coopère pas et que la clé n'est pas récupérable par ailleurs, les données restent inaccessibles. D'où l'importance du dump mémoire à chaud (la clé de chiffrement BitLocker ou FileVault est en mémoire tant que le volume est déverrouillé).

#### 2.3 L'expert judiciaire

L'expert judiciaire en informatique est un technicien inscrit sur la liste d'une cour d'appel, mandaté par un magistrat (juge d'instruction, juge civil, ou tribunal de commerce) pour réaliser une expertise technique. Son statut est régi par la loi du 29 juin 1971 et le décret du 23 décembre 2004.

L'expert reçoit une mission précise définie par le magistrat (par exemple : « déterminer si des données ont été exfiltrées du SI de la société X entre le 1er janvier et le 31 mars 2026, identifier les moyens utilisés, et chiffrer le préjudice »). Il est tenu par cette mission et ne peut pas la dépasser sans autorisation. Il doit respecter le contradictoire : les parties sont informées des opérations d'expertise, peuvent y assister (ou se faire représenter par un conseil technique, souvent appelé « sapiteur »), et peuvent soumettre des « dires » (observations écrites auxquelles l'expert doit répondre dans son rapport). Le rapport d'expertise est soumis au juge, qui reste libre de le suivre ou non (l'expertise est un avis technique, pas un jugement).

L'inscription sur la liste des experts exige une compétence technique reconnue et une formation à la procédure judiciaire. L'expert prête serment. Sa responsabilité professionnelle est engagée en cas de faute. Dans le contexte forensic, l'expert doit maîtriser à la fois la technique (acquisition, analyse, outils) et la procédure (chaîne de custody, documentation, rédaction pour le contradictoire).

#### 2.4 Chaîne de custody

La chaîne de custody (chain of custody) retrace le parcours complet d'une pièce à conviction numérique, de sa collecte à sa présentation. Elle répond à une question simple : qui a eu accès à cette preuve, quand, et qu'en a-t-il fait ?

Chaque manipulation est documentée : qui a acquis le support (nom, qualité, organisme), à quelle date et heure (horodatage précis, fuseau horaire explicite), avec quel outil (nom, version, paramètres), quel est le hash d'intégrité (MD5 + SHA-256 calculés immédiatement après l'acquisition), où le support est-il stocké (lieu physique, conditions de sécurité), qui l'a transporté (nom, date, moyen de transport), et qui l'a analysé (nom, dates, outils utilisés).

Une rupture dans la chaîne de custody — un moment où la preuve n'était pas sous contrôle documenté — permet à la partie adverse de contester son intégrité. C'est la différence entre une preuve et un simple fichier. Le formulaire de chaîne de custody est en Annexe E.

> **Bonne pratique :** Même en investigation interne (sans perspective judiciaire immédiate), respecter les principes de la chaîne de custody dès le départ. La raison est pragmatique : de nombreuses investigations internes basculent en judiciaire quand l'ampleur des faits est révélée. Si les preuves ont été collectées sans rigueur au début, elles sont inexploitables devant un tribunal — et l'entreprise a perdu sa chance de judiciariser.

#### 2.5 Recevabilité de la preuve numérique

Pour qu'une preuve numérique soit acceptée par un tribunal, plusieurs conditions cumulatives doivent être remplies : **authenticité** (la preuve est bien ce qu'elle prétend être — hash d'intégrité vérifié), **fiabilité** (la méthode de collecte et d'analyse est reconnue et reproductible — outils documentés, méthodologie explicite), **pertinence** (la preuve est en rapport avec les faits litigieux — hors sujet = irrecevable), **proportionnalité** (la collecte n'a pas été disproportionnée par rapport à l'enjeu — imager le disque du DG pour un conflit sur l'utilisation de la photocopieuse serait disproportionné), et **loyauté** (obtenue par des moyens légaux — ce critère a été assoupli en matière civile par la jurisprudence de 2023, mais reste strict en matière pénale).

Un rapport forensic parfaitement rédigé mais fondé sur une acquisition non documentée sera contesté. Un rapport fondé sur une acquisition impeccable mais dont les conclusions dépassent les constatations sera également contesté. La rigueur doit être de bout en bout.

#### 2.6 Forensic judiciaire vs investigation interne : deux régimes

L'investigation interne (menée par l'entreprise elle-même ou un prestataire mandaté) et l'investigation judiciaire (menée sous mandat d'un magistrat) obéissent à des règles différentes. L'investigation interne n'a pas de pouvoir de réquisition (elle ne peut pas forcer un hébergeur AWS à communiquer les logs CloudTrail), elle est contrainte par le RGPD et le droit du travail (voir 2.7 et 2.8), mais elle bénéficie d'une flexibilité méthodologique plus grande (pas de scellés formels, pas de contradictoire obligatoire). L'investigation judiciaire dispose de pouvoirs étendus (perquisition, réquisition, scellés, mandat international) mais est soumise à un cadre procédural strict dont la violation entraîne la nullité des actes.

Le moment de la bascule est critique : quand les premiers résultats de l'investigation interne révèlent une infraction pénale (accès frauduleux — art. 323-1 CP, vol de données, abus de confiance, extorsion), l'entreprise doit décider si elle judiciarise (dépôt de plainte). À ce moment, les preuves collectées en interne doivent être exploitables judiciairement — d'où l'importance de la rigueur dès le début.

#### 2.7 RGPD et forensic

Le RGPD s'applique dès que l'investigation traite des données à caractère personnel — ce qui est presque toujours le cas (un dump de disque contient les fichiers personnels de l'utilisateur, un log contient des identifiants, un dump mémoire peut contenir des mots de passe en clair). La base légale la plus courante pour l'investigation forensic est l'intérêt légitime de l'entreprise à assurer la sécurité de son SI (article 6.1.f du RGPD). La proportionnalité est essentielle : ne collecter que ce qui est nécessaire à l'investigation, ne conserver les données que le temps de l'investigation et de l'éventuelle procédure, et documenter la justification. Le DPO doit être impliqué dès le début de l'investigation.

#### 2.8 Droit du travail et forensic interne

L'investigation forensic sur le poste d'un salarié est encadrée par le droit du travail et la jurisprudence de la chambre sociale de la Cour de cassation. Les grands principes : l'employeur peut accéder aux fichiers professionnels du salarié (présomption de caractère professionnel des fichiers sur le poste de travail de l'entreprise), mais les fichiers explicitement marqués « personnel » ou « privé » ne peuvent être ouverts qu'en présence du salarié ou après information (sauf si un événement particulier le justifie — menace sur la sécurité du SI). La charte informatique de l'entreprise (si elle existe, a été communiquée, et est à jour) encadre l'utilisation des outils et les modalités de contrôle. En pratique, impliquer le juridique et le DPO avant toute investigation sur un poste de salarié est indispensable — une preuve obtenue en violation du droit du travail est irrecevable dans une procédure disciplinaire.

#### 2.9 Normes internationales

Trois normes ISO encadrent les pratiques forensic. **ISO 27037** (2012) couvre l'identification, la collecte, l'acquisition et la préservation des preuves numériques — c'est la norme de référence pour la phase d'acquisition (comment manipuler un support, quand utiliser un write blocker, comment documenter). **ISO 27042** (2015) couvre l'analyse et l'interprétation des preuves — elle formalise les principes d'analyse objective et de documentation des résultats. **ISO 27043** (2015) définit le processus global d'investigation — de l'identification au rapport. Ces normes ne sont pas obligatoires mais constituent un cadre de bonnes pratiques reconnu internationalement. S'y conformer renforce la crédibilité de l'investigation et la recevabilité des preuves, tant en France qu'à l'international.

#### 2.10 Fil rouge — MUSIC BOX : le cadrage juridique

> **🔬 MUSIC BOX — Épisode 2**
>
> Vendredi soir, 18h30. Claire appelle le directeur juridique de NovaPharma, Maître Antoine Renard, et le DPO, Sandrine Leclerc.
>
> Questions immédiates : peut-on investiguer le poste de Julien Mallet ? Réponse : oui, c'est une investigation de sécurité sur un poste professionnel, pas une surveillance du salarié. La charte informatique autorise les contrôles de sécurité. Le DPO valide la base légale (intérêt légitime). Faut-il déposer plainte maintenant ? Pas encore — il faut d'abord comprendre l'étendue. Mais on préserve les preuves comme si on allait judiciariser.
>
> Le directeur juridique recommande de mandater une experte judiciaire inscrite pour sécuriser la chaîne de custody dès le début. Maître Élise Fournier (experte judiciaire en informatique, cour d'appel de Paris) est contactée — elle sera sur site samedi 9h. Son rôle : superviser les acquisitions, garantir la chaîne de custody, et être en mesure de témoigner de la rigueur méthodologique si l'affaire est judiciarisée.

---

### Chapitre 3 — Méthodologie forensic et posture d'enquêteur

#### 3.1 Le modèle en 5 phases

Toute investigation forensic suit un processus structuré en cinq phases séquentielles. Ce n'est pas un formalisme bureaucratique — c'est un cadre qui évite les erreurs fatales et qui structure la documentation.

**Phase 1 — Identification :** définir le périmètre de l'investigation, les systèmes concernés, les données volatiles (à acquérir en priorité), et les questions investigatives auxquelles l'investigation doit répondre. Output : liste des cibles, ordre d'acquisition, questions investigatives formulées. Piège principal : périmètre trop large (on se noie dans les données) ou trop étroit (on rate l'essentiel).

**Phase 2 — Préservation :** protéger les preuves contre toute altération. Ne pas éteindre une machine allumée (on perdrait la RAM). Ne pas allumer une machine éteinte (le boot modifie le disque). Isoler la machine du réseau (pour éviter que l'attaquant efface ses traces ou que des processus légitimes écrasent des preuves). Documenter l'état initial (photos de l'écran, des connexions, des équipements). Piège principal : modifier involontairement la preuve par une action bien intentionnée mais mal exécutée.

**Phase 3 — Acquisition :** copier les données de manière forensiquement valide. Image bit-à-bit du disque avec write blocker, dump de la mémoire vive, export des logs, capture réseau. Hash d'intégrité (MD5 + SHA-256) calculé sur le support source et sur l'image acquise — si les hash correspondent, l'intégrité est prouvée. Piège principal : oublier le write blocker, rater le dump RAM, ne pas hasher immédiatement. Détaillé en Partie II.

**Phase 4 — Analyse :** extraire les artefacts pertinents, construire une timeline chronologique, formuler des hypothèses, et les tester contre les évidences. C'est le cœur intellectuel du forensic. Piège principal : biais de confirmation, tunnel vision. Détaillé en Parties III et IV.

**Phase 5 — Présentation :** produire le rapport forensic et, le cas échéant, témoigner devant un tribunal ou une direction générale. Le rapport doit être compréhensible par un non-technicien tout en étant techniquement inattaquable. La distinction fait/déduction/hypothèse doit être explicite à chaque étape. Piège principal : rapport trop technique ou conclusions dépassant les constatations. Détaillé au Ch.26.

#### 3.2 Scoping strategy : définir le périmètre d'enquête

Le scoping est l'une des compétences les plus sous-estimées en forensic. La difficulté n'est pas seulement d'analyser, c'est de délimiter : quelles machines investiguer, quelle période couvrir, quels utilisateurs examiner, quels logs collecter, quel niveau de profondeur, et quand s'arrêter.

Les **questions investigatives** structurent le périmètre. Avant de toucher un clavier, l'investigateur formule les questions auxquelles l'investigation doit répondre : comment l'attaquant a-t-il pénétré (vecteur d'accès initial) ? Quand l'intrusion a-t-elle commencé ? Quels systèmes ont été compromis (mouvement latéral) ? Quelles données ont été impactées (exfiltration, modification, destruction) ? L'attaquant est-il encore présent ? Qui est l'attaquant (attribution, si possible) ? Ces questions orientent chaque action d'investigation.

**Délimiter le périmètre** implique des choix concrets. Quelles machines : on commence par les machines directement concernées par l'alerte, puis on élargit en fonction des découvertes (mouvement latéral, même IoC trouvé sur d'autres machines). Quelle période : la fenêtre temporelle initiale est définie par l'alerte, mais l'investigation révèle souvent que l'intrusion remonte beaucoup plus loin (dans MUSIC BOX, l'alerte est à J, mais l'intrusion initiale est à J-60). Quels logs : dépend de la rétention réelle (pas la rétention théorique configurée, mais ce qui est effectivement disponible et exploitable).

Le **piège du scope creep** : chaque découverte ouvre de nouvelles pistes. Un bon investigateur distingue les pistes prioritaires (qui répondent aux questions investigatives) des pistes secondaires (intéressantes mais non essentielles). Il documente les pistes non suivies pour éventuelle investigation ultérieure (avec la mention « piste identifiée, non suivie dans le cadre du scoping actuel — recommandation : investiguer ultérieurement si nécessaire »).

**Quand s'arrêter :** l'investigation est terminée quand toutes les questions investigatives ont reçu une réponse (même si la réponse est « indéterminable avec les données disponibles »), que la couverture temporelle est suffisante, et que la timeline est cohérente. La tentation du perfectionnisme (« et si on regardait aussi ce serveur ? ») doit être résistée si elle ne répond à aucune question investigative ouverte.

**Triage vs investigation complète — arbre de décision :** le choix entre triage rapide (KAPE, Velociraptor — artefacts ciblés, résultats en heures) et investigation complète (image disque + dump RAM + capture réseau + timeline exhaustive — résultats en jours à semaines) dépend de la gravité confirmée, de la perspective judiciaire, de la sensibilité des données, et des moyens disponibles. La bascule du triage vers l'investigation complète se fait quand la gravité est confirmée (vol de données, compromission étendue, insider), quand des données réglementées sont concernées (RGPD, santé, défense), ou quand la direction souhaite judiciariser.

#### 3.3 Posture intellectuelle de l'enquêteur

Le forensic exige une posture intellectuelle rigoureuse qui va au-delà de la maîtrise technique des outils.

Le **doute méthodique** : l'analyste ne prend rien pour acquis. Un timestamp peut être falsifié (timestomping). Un log peut être incomplet (rotation, effacement). Un artefact peut être un planted evidence (fausse preuve déposée par l'attaquant pour incriminer un tiers ou brouiller les pistes). Chaque constatation est vérifiée contre au moins une source indépendante quand c'est possible.

Les **hypothèses alternatives** : l'analyste formule plusieurs hypothèses et les teste toutes, pas seulement celle qui semble la plus probable. Si l'hypothèse initiale est « le salarié Julien Mallet a exfiltré les données », l'analyste doit aussi tester « le compte de Julien Mallet a été compromis par un attaquant externe ». Le biais de confirmation — la tendance à chercher les données qui confirment l'hypothèse préférée et à ignorer celles qui la contredisent — est le piège le plus dangereux du forensic (développé au Ch.11).

La **distinction fait / déduction / hypothèse** : l'analyste distingue rigoureusement ce qu'il constate (« le fichier X a été supprimé le 3 mars à 14h32 » — fait, observable dans la MFT), ce qu'il en déduit (« la suppression a été effectuée par le compte svc-backup, car c'est le seul compte actif sur la machine à cette heure selon les Event Logs » — déduction logique), et ce qu'il suppose (« cette suppression est intentionnelle et liée à la compromission » — hypothèse, qui nécessite des évidences supplémentaires pour être confirmée). Le rapport forensic doit rendre cette distinction explicite à chaque étape.

#### 3.4 Documentation continue

La documentation est un livrable continu, pas un exercice de fin d'investigation. Le **journal d'investigation** (case log) enregistre chronologiquement chaque action de l'investigateur : heure, action, outil utilisé, résultat, décision. Le **formulaire de chaîne de custody** suit chaque pièce à conviction. Les **photos** documentent l'état physique des équipements (avant de débrancher un câble, on photographie). Les **captures d'écran horodatées** documentent les étapes de l'analyse. Sans documentation, l'investigation la plus brillante est irrecevable (en judiciaire) et irrépétable (en interne).

#### 3.5 Les 10 erreurs fatales

Ces erreurs invalident une preuve ou égarent une investigation : (1) éteindre une machine allumée avant le dump RAM, (2) allumer une machine éteinte sans write blocker, (3) oublier de hasher avant ET après l'acquisition, (4) travailler sur l'original au lieu de la copie, (5) ne pas documenter ses actions en temps réel, (6) ignorer les fuseaux horaires lors de la corrélation de timestamps, (7) se fixer sur la première hypothèse sans en tester d'autres, (8) ignorer les sources de preuves volatiles (connexions réseau, processus en mémoire), (9) sous-estimer l'anti-forensics (l'attaquant a pu falsifier des timestamps, supprimer des logs, ou déposer de fausses preuves), et (10) produire un rapport dont les conclusions dépassent les constatations.

#### 3.6 Fil rouge — MUSIC BOX : le scoping

> **🔬 MUSIC BOX — Épisode 3**
>
> Scoping initial chez NovaPharma. Claire formule 4 questions investigatives :
> 1. Comment l'attaquant a-t-il pénétré le SI ? (vecteur d'accès initial)
> 2. Quels systèmes sont compromis au-delà du poste WKS-RD-047 ? (mouvement latéral)
> 3. Des données ont-elles été exfiltrées, et si oui, lesquelles et quel volume ? (impact sur la propriété intellectuelle)
> 4. L'attaquant est-il encore présent dans le réseau ? (urgence de confinement)
>
> Machines prioritaires : WKS-RD-047 (poste compromis), SRV-RD-01 (serveur R&D Linux, données de recherche NP-427), DC01 (contrôleur de domaine — vérifier si l'AD est compromis).
>
> Fenêtre temporelle : J-90 à J (on prend large pour ne pas rater le début de l'intrusion — les logs du SIEM couvrent 12 mois, les logs proxy 6 mois).
>
> Décision : triage immédiat (dump RAM de WKS-RD-047 + collecte KAPE sur les 3 machines + export des logs AD) ce soir. Image disque complète de WKS-RD-047 et du serveur R&D samedi matin avec l'experte judiciaire. Perspective : probable judiciarisation si vol de données R&D confirmé.

---

### Chapitre 4 — Environnement technique et outils fondamentaux

#### 4.1 Le lab forensic

Un laboratoire forensic est un environnement contrôlé dédié à l'analyse des preuves numériques. Son objectif est double : protéger l'intégrité des preuves et fournir les outils nécessaires à l'analyse.

Le **matériel** comprend des write blockers matériels (Tableau/Guidance T356789iu, CRU WiebeTech — qui empêchent physiquement toute écriture sur le support source, indépendamment du logiciel), des duplicateurs forensic (Logicube Falcon Neo, Atola TaskForce — pour les acquisitions rapides avec hashing intégré), et des stations d'analyse puissantes (minimum 64 Go de RAM pour l'analyse mémoire avec Volatility, stockage rapide NVMe pour les images disque qui font souvent plusieurs centaines de Go, processeurs multi-cœurs pour le traitement de Super Timelines qui peuvent contenir des millions d'événements).

Le **réseau du lab** est isolé du réseau de production (on ne connecte jamais un support potentiellement compromis au réseau d'entreprise). Le stockage des preuves est sécurisé : coffre physique fermé à clé (ou salle avec contrôle d'accès et vidéosurveillance pour les investigations judiciaires), registre d'accès documentant chaque entrée/sortie de support.

#### 4.2 Distributions forensic

Plusieurs distributions Linux pré-configurées facilitent le travail forensic. **SIFT Workstation** (SANS Investigative Forensic Toolkit), maintenue par le SANS Institute, est la référence pédagogique et professionnelle — basée sur Ubuntu, elle contient Autopsy, Volatility, Plaso, RegRipper, les outils Eric Zimmerman (via Wine ou natifs), et des centaines d'outils spécialisés. **Tsurugi Linux** est une distribution très complète d'origine japonaise/italienne. **CSI Linux** est orientée investigation et OSINT. **Kali Linux**, connue pour le pentest, inclut un méta-paquet forensic (`kali-tools-forensics`). **REMnux** est spécialisée dans l'analyse de malware.

Le choix de la distribution est moins important que la maîtrise des outils qu'elle contient. Un analyste expert avec un Ubuntu nu et les bons outils installés sera plus efficace qu'un débutant avec la distribution la plus complète.

#### 4.3 Outils open source vs commerciaux

Les outils forensic se répartissent en deux catégories. Les **outils open source** (Autopsy/The Sleuth Kit pour le disk forensics, Volatility 3 pour le memory forensics, Wireshark/Zeek pour le network forensics, Plaso pour la Super Timeline, RegRipper pour le registre Windows) sont gratuits, auditables (leur code source est vérifiable — argument important pour le contradictoire), et largement utilisés tant par les forces de l'ordre que par les cabinets privés. Les **outils commerciaux** (EnCase d'OpenText, FTK d'Exterro, X-Ways Forensics, Magnet AXIOM, Cellebrite UFED pour le mobile) offrent des interfaces intégrées, un support commercial, et sont parfois requis ou préférés par certaines juridictions ou certains clients institutionnels.

En 2025-2026, la tendance est clairement à la convergence : Autopsy est devenu une plateforme mature capable de rivaliser avec les outils commerciaux pour le disk forensics, Volatility 3 est la référence incontestée pour le memory forensics (même les éditeurs commerciaux l'utilisent comme moteur), et les outils Eric Zimmerman ont transformé le Windows forensics en fournissant des parsers spécialisés de qualité professionnelle, gratuitement.

#### 4.4 La suite Eric Zimmerman — l'outillage Windows forensics de référence

Eric Zimmerman est un ancien agent du FBI devenu formateur SANS, qui a développé une suite d'outils de parsing forensic pour Windows, devenus la référence de facto en 2025-2026. Ces outils parsent les artefacts Windows bruts et produisent des résultats structurés (CSV) exploitables dans Timeline Explorer ou un tableur.

**MFTECmd** parse la $MFT (Master File Table) NTFS et produit une timeline de tous les fichiers avec leurs timestamps $SI et $FN — indispensable pour détecter le timestomping. **PECmd** parse le Prefetch — historique d'exécution des programmes avec dates, nombre d'exécutions, et fichiers chargés. **LECmd** parse les fichiers LNK (raccourcis) — révèlent les fichiers récemment ouverts, les chemins réseau accédés, les volumes USB connectés. **SBECmd** (ShellBags Explorer) parse les ShellBags du registre — historique complet de la navigation dans l'explorateur de fichiers. **JLECmd** parse les Jump Lists — fichiers récemment ouverts par application. **EvtxECmd** parse les Event Logs Windows (format evtx) en CSV structuré — beaucoup plus rapide et flexible que l'Event Viewer natif. **RECmd** parse le registre Windows en ligne de commande avec des batch files prédéfinies. **AmcacheParser** parse l'Amcache — historique des programmes exécutés avec hash SHA1. **AppCompatCacheParser** parse le ShimCache — historique des programmes avec timestamps. **SrumECmd** parse la base SRUM — consommation réseau et CPU par processus. **Timeline Explorer** est l'interface de visualisation qui permet de filtrer, trier, et analyser les CSV produits par tous les outils ci-dessus.

Ces outils sont distribués gratuitement via le site d'Eric Zimmerman (ericzimmerman.github.io) et sont pré-installés dans SIFT Workstation. Ils sont utilisés tout au long de la Partie IV.

#### 4.5 Hashing et vérification d'intégrité

Le hashing est le mécanisme fondamental de vérification d'intégrité en forensic. Un hash est une empreinte numérique de taille fixe calculée à partir de l'intégralité des données : si un seul bit change, le hash change complètement. **MD5** (128 bits) est rapide mais théoriquement vulnérable aux collisions (deux fichiers différents produisant le même hash — démontré en 2004). **SHA-256** (256 bits) est plus robuste et considéré comme sûr. La pratique recommandée est le **double hashing** (MD5 + SHA-256) : les deux doivent correspondre. La probabilité que deux fichiers différents produisent le même MD5 ET le même SHA-256 est négligeable.

Les outils standards sont `md5sum` et `sha256sum` (Linux), `Get-FileHash` (PowerShell), et `hashdeep` (multi-hash, récursif — utile pour hasher des répertoires entiers). Chaque acquisition doit être accompagnée de ses hash, notés dans le journal d'investigation et le formulaire de chaîne de custody.

#### 4.6 Outils d'acquisition et formats d'images

L'acquisition bit-à-bit d'un disque se fait avec des outils spécifiques. La commande **dd** (Linux) est l'outil historique : `dd if=/dev/sdX of=/path/image.raw bs=4M status=progress` — simple, universel, mais sans hashing intégré ni barre de progression utile. **dc3dd** (développé par le DoD américain) ajoute le hashing intégré, le logging, et la gestion des erreurs. **FTK Imager** (gratuit, Windows et Linux) est l'outil le plus utilisé en entreprise : interface graphique, hashing automatique, support des formats E01 et AFF4, preview du contenu avant acquisition. **Guymager** (Linux, open source) offre une acquisition multi-threadée rapide avec interface graphique.

Les formats d'images : le format **raw** (dd) est une copie exacte, secteur par secteur — simple mais volumineux (taille = taille du disque source) et sans métadonnées intégrées. Le format **E01** (EnCase/Expert Witness Format) compresse les données (réduction de 30-50 % typiquement), intègre les métadonnées (hash, notes, informations de case), et permet la segmentation en fichiers multiples — c'est le format le plus utilisé en forensic. Le format **AFF4** (Advanced Forensic Format 4) est un format ouvert moderne, conteneurisé, qui supporte le stockage de multiples types d'évidences dans un seul conteneur.

#### 4.7 Outils de triage rapide

Les outils de triage collectent rapidement les artefacts les plus pertinents sans image complète du disque. **KAPE** (Kroll Artifact Parser and Extractor) utilise des targets (définitions de quels fichiers/artefacts collecter) et des modules (parsers pour analyser les artefacts collectés). La commande `kape.exe --tsource C: --tdest E:\Output --target KapeTriage` collecte en quelques minutes les Event Logs, le registre, le Prefetch, l'Amcache, le ShimCache, la $MFT, le SRUM, les historiques navigateur, et d'autres artefacts clés. **Velociraptor** (open source, développé initialement par Google) est un agent déployable sur tout un parc : il permet de lancer des collectes et des hunts à distance sur des centaines de machines simultanément via des requêtes VQL (Velociraptor Query Language). **DFIR-ORC** (développé par l'ANSSI) est un outil de collecte français optimisé pour les grands déploiements dans les OIV.

#### 4.8 Environnement d'analyse

L'analyse se fait toujours sur une machine dédiée, jamais sur la machine source. L'environnement standard est une VM isolée du réseau, avec des snapshots pour pouvoir revenir en arrière si une manipulation corrompt l'état de l'analyse. Les images forensic sont montées en lecture seule dans la VM (sous Linux : `mount -o ro,loop,noexec image.raw /mnt/evidence`). Arsenal Image Mounter (Windows) permet de monter des images E01 comme des disques virtuels accessibles en lecture seule. La configuration de l'environnement (version des outils, options utilisées, paramètres de montage) est documentée pour la reproductibilité.

#### 4.9 Fil rouge — MUSIC BOX : le lab et l'acquisition initiale

> **🔬 MUSIC BOX — Épisode 4**
>
> Vendredi soir, 19h00. L'équipe met en place le dispositif d'investigation. Claire utilise sa station forensic portable (laptop avec 64 Go de RAM, 4 To NVMe, SIFT Workstation en VM, write blocker Tableau T35es).
>
> **Acquisition mémoire (priorité absolue) :** DumpIt est exécuté sur WKS-RD-047 (machine allumée, session utilisateur active). Dump RAM : 32 Go, 14 minutes. Hash SHA-256 calculé immédiatement : `a7f3e2...`. Documenté dans le journal d'investigation et le formulaire de chaîne de custody.
>
> **Triage KAPE :** lancé sur WKS-RD-047 en parallèle du dump. Target : KapeTriage. Résultat : tous les artefacts Windows critiques collectés en 8 minutes. Hash calculé sur l'archive.
>
> **Acquisition disque prévue samedi matin** avec l'experte judiciaire — image E01 via FTK Imager avec write blocker matériel.
>
> **Serveur R&D Linux (SRV-RD-01) :** la machine est en production et ne peut pas être éteinte (les expériences en cours seraient perdues). Décision : acquisition logique à chaud — copie des logs (`/var/log/`), de l'historique bash, du crontab, des authorized_keys SSH, et des fichiers récemment modifiés. Image disque reportée à un arrêt de maintenance planifié (dans 5 jours).
>
> Choix du format : E01 pour l'image disque (compression, métadonnées intégrées, compatibilité Autopsy). Raw pour le dump mémoire (compatibilité Volatility 3).

---

## PARTIE II — ACQUISITION DE PREUVES

*L'acquisition est l'étape la plus critique de toute investigation. Une analyse brillante ne compense jamais une acquisition bâclée : si l'image disque est incomplète, si le dump mémoire est corrompu, si les logs n'ont pas été préservés, les conclusions seront fragiles et potentiellement contestables.*

---

### Chapitre 5 — Acquisition disque et supports de stockage

#### 5.1 Principes fondamentaux

L'acquisition disque produit une copie bit-à-bit du support de stockage : chaque secteur est copié, y compris les espaces non alloués (où se trouvent les fichiers supprimés), le slack space (espace résiduel en fin de cluster), et les zones cachées (HPA, DCO). Ce n'est pas une simple copie de fichiers — c'est un clone exact du support au niveau des secteurs.

Le **write blocker** est le garant de l'intégrité. Un write blocker matériel (Tableau T35es, CRU WiebeTech) est un dispositif physique interposé entre le support source et la station d'acquisition qui empêche électriquement toute écriture sur le support. Un write blocker logiciel (sous Linux : montage avec `mount -o ro`, ou utilisation de udev rules) empêche les écritures au niveau du système d'exploitation. Le write blocker matériel est préféré en contexte judiciaire car il est physiquement vérifiable et indépendant du logiciel. Sans write blocker, le simple fait de connecter un disque à Windows modifie des métadonnées (timestamps d'accès, journaux du système de fichiers) — ce qui peut compromettre l'intégrité de la preuve.

La **vérification d'intégrité par double hash** (MD5 + SHA-256) est obligatoire. Le hash est calculé sur le support source avant l'acquisition, sur l'image produite immédiatement après l'acquisition, et éventuellement sur le support source après l'acquisition (pour vérifier que l'acquisition n'a rien modifié — ce qui serait le cas si le write blocker avait défailli). Si les hash correspondent, l'intégrité est prouvée mathématiquement.

#### 5.2 Acquisition physique vs logique

L'**acquisition physique** copie l'intégralité du support au niveau des secteurs — c'est la méthode privilégiée car elle capture tout, y compris les données supprimées et les zones cachées. Commande type sous Linux avec dc3dd :

```
dc3dd if=/dev/sdX hof=/path/image.dd hash=md5 hash=sha256 log=/path/acquisition.log
```

L'**acquisition logique** copie uniquement les fichiers visibles par le système de fichiers. Plus rapide et moins volumineuse, mais elle ne capture ni les fichiers supprimés, ni le slack space, ni les zones non allouées. L'acquisition logique est utilisée quand l'acquisition physique est impossible (VM en production accessible uniquement par réseau, volume chiffré qu'on ne peut pas déchiffrer hors ligne) ou quand le triage rapide suffit (combinée avec KAPE pour une collecte ciblée des artefacts).

#### 5.3 HDD : le support le plus favorable

Les disques durs magnétiques (HDD) sont les plus favorables au forensic. Les données supprimées restent physiquement présentes sur le plateau magnétique tant que les secteurs n'ont pas été réécrits par de nouvelles données — ce qui peut prendre des mois ou des années dans les zones peu utilisées du disque. La récupération de fichiers supprimés sur HDD est souvent possible et productive.

Les zones cachées du disque — **HPA** (Host Protected Area) et **DCO** (Device Configuration Overlay) — sont des zones que le BIOS et le système d'exploitation ne voient pas normalement, mais qui peuvent contenir des données dissimulées. L'outil `hdparm` (Linux) détecte leur présence (`hdparm -N /dev/sdX` affiche la taille réelle vs la taille visible) et permet de les rendre accessibles pour l'acquisition. Les outils forensic commerciaux (EnCase, X-Ways) gèrent cette détection automatiquement.

#### 5.4 SSD : les défis du forensic moderne

Les SSD ont fondamentalement changé le forensic. Trois mécanismes posent problème.

Le **TRIM** est une commande que le système d'exploitation envoie au SSD pour indiquer que des secteurs ne sont plus utilisés — le contrôleur du SSD peut alors effacer physiquement ces secteurs pour optimiser les performances d'écriture futures. Conséquence : les fichiers supprimés sur un SSD avec TRIM actif (c'est le cas par défaut sur tous les OS modernes depuis Windows 7, macOS 10.6, et Linux avec les filesystems récents) sont souvent irrécupérables, contrairement aux HDD. Le TRIM peut s'exécuter en quelques secondes après la suppression d'un fichier.

Le **garbage collection** est un processus interne au contrôleur SSD qui réorganise et nettoie les blocs de données de manière autonome — même sans commande du système d'exploitation. Le SSD peut effacer des données « supprimées » de sa propre initiative, à n'importe quel moment, y compris quand le disque est connecté via un write blocker (le write blocker empêche les écritures venant du système, mais pas les opérations internes du contrôleur).

Le **wear leveling** distribue les écritures sur toutes les cellules NAND pour équilibrer l'usure, ce qui signifie que les données ne sont pas nécessairement stockées à l'emplacement attendu au niveau des secteurs logiques.

Implication pratique : sur un SSD, l'acquisition doit être faite le plus rapidement possible après la détection de l'incident. Chaque minute qui passe est une minute pendant laquelle le garbage collection peut effacer des preuves. Et il ne faut jamais promettre de récupérer des fichiers supprimés sur un SSD — c'est souvent impossible.

#### 5.5 Stockage chiffré

Le chiffrement est un défi majeur. BitLocker (Windows), FileVault (macOS), LUKS (Linux) et VeraCrypt chiffrent le contenu du disque — sans la clé, l'image acquise est un bloc de données inexploitable. Stratégies de récupération :

Si la machine est **allumée et le volume déverrouillé**, la clé de chiffrement est en mémoire — d'où l'importance absolue du dump RAM avant toute extinction (Ch.6). Le dump mémoire, analysé avec Volatility, peut révéler la clé BitLocker, la passphrase FileVault, ou les clés LUKS.

La **recovery key** BitLocker est souvent stockée dans Active Directory (vérifiable par les administrateurs), dans le compte Microsoft de l'utilisateur, ou sur un support physique (papier, clé USB). La recovery key FileVault est stockable dans le compte Apple (iCloud) ou par un administrateur MDM. Les clés LUKS n'ont pas de recovery centralisé — si la passphrase est perdue et que la RAM n'a pas été dumpée, les données sont inaccessibles.

Le **TPM** (Trusted Platform Module) protège la clé BitLocker sur les machines modernes, mais il la libère automatiquement au boot normal — une acquisition à chaud (machine allumée avec le volume déverrouillé) contourne cette protection.

#### 5.6 RAID, NAS et serveurs virtualisés

Les serveurs utilisent généralement des configurations RAID. Deux approches : acquisition disque par disque (acquérir individuellement chaque disque du RAID, puis reconstruire le volume logique avec X-Ways, Autopsy, ou `mdadm` — méthode la plus sûre car elle préserve les données brutes de chaque disque) ou acquisition du volume logique via le contrôleur (capture directe du volume RAID reconstruit — plus rapide, mais perte des données résiduelles au niveau physique).

Les **NAS** et serveurs de fichiers en production posent la question de l'acquisition à chaud. Un NAS ne peut pas toujours être éteint et retiré du rack (impact sur la production). L'acquisition à chaud — via le réseau (FTK Imager en mode réseau, ou `dd` via SSH) ou via un snapshot — est souvent le seul choix, mais elle est moins « propre » qu'une acquisition physique avec write blocker car le système de fichiers peut évoluer pendant la copie.

Les **machines virtuelles** sont un cas favorable : l'image VMDK (VMware), VHDX (Hyper-V), ou QCOW2 (KVM/QEMU) EST le disque. Il suffit de copier le fichier d'image de la VM ou de prendre un snapshot (qui gèle l'état du disque à un instant T). Le snapshot de VM est l'équivalent fonctionnel d'une acquisition à chaud avec write blocker — et il capture simultanément la mémoire si la VM est en cours d'exécution.

#### 5.7 Fil rouge — MUSIC BOX : l'acquisition disque

> **🔬 MUSIC BOX — Épisode 5**
>
> Samedi 9h00. Maître Fournier (experte judiciaire) est sur site. L'acquisition formelle commence.
>
> **WKS-RD-047** (SSD NVMe 512 Go, Windows 11, BitLocker activé) : la machine est encore allumée (le dump RAM a été fait la veille — la clé BitLocker est en mémoire). Acquisition physique via FTK Imager avec write blocker Tableau T35es. Format E01, segmenté en fichiers de 4 Go. Durée : 45 minutes. Hash MD5 + SHA-256 calculés automatiquement : correspondance vérifiée. Documenté dans le formulaire de chaîne de custody, signé par Maître Fournier.
>
> **SRV-RD-01** (serveur Linux Ubuntu 22.04, RAID 5 × 4 disques de 2 To) : le serveur est en production, les expériences en cours ne peuvent pas être interrompues. Décision : acquisition logique via `dc3dd` sur le réseau (accès SSH), ciblée sur les répertoires `/home/`, `/var/log/`, `/tmp/`, et `/opt/research/`. Image physique reportée à l'arrêt de maintenance (J+5). Hash calculé sur chaque acquisition partielle.

---

### Chapitre 6 — Acquisition mémoire vive (RAM)

#### 6.1 Pourquoi le dump RAM est non négociable

La mémoire vive contient des données qui n'existent nulle part ailleurs et qui disparaissent irrémédiablement à l'extinction de la machine. Les processus en cours d'exécution (y compris les malwares fileless qui ne sont jamais écrits sur le disque), les connexions réseau actives (vers le C2, vers les machines latéralisées), les credentials en clair (les hashes NTLM dans le processus LSASS, les clés de session Kerberos, les mots de passe en clair si l'attaquant a utilisé mimikatz), les clés de chiffrement en mémoire (BitLocker, FileVault, VeraCrypt — récupérables depuis le dump), et les commandes récemment exécutées (historique de la console, arguments des processus).

La règle est simple : si la machine est allumée, on dumpe la RAM en premier. Avant de l'isoler du réseau, avant de la saisir, avant de la déplacer, et surtout avant de l'éteindre. La perte de la RAM est irréversible — c'est l'erreur forensic la plus courante et la plus grave.

#### 6.2 Outils d'acquisition mémoire

**DumpIt** (Comae/Magnet Forensics) : outil Windows le plus simple d'utilisation — un exécutable unique, double-clic, dump automatique de la RAM dans un fichier `.dmp` ou `.raw`. Rapide (environ 1-2 Go/minute selon le matériel), minimal en overhead. Recommandé pour les situations d'urgence où la simplicité prime.

**WinPmem** (Velocidex) : outil Windows open source plus flexible que DumpIt. Supporte les formats raw et AFF4. Permet l'acquisition de la mémoire physique ET du pagefile. Plus configurable mais légèrement plus complexe d'utilisation.

**Magnet RAM Capture** : outil gratuit de Magnet Forensics avec interface graphique. Simple, fiable, mais Windows uniquement.

**LiME** (Linux Memory Extractor) : module kernel Linux pour l'acquisition mémoire. Chargé dynamiquement (`insmod lime.ko "path=/path/dump.lime format=lime"`), il capture la mémoire physique avec un impact minimal. C'est la méthode standard pour les serveurs Linux.

**Acquisition mémoire de VM :** les snapshots VMware produisent un fichier `.vmem` qui est le dump mémoire de la VM. Les snapshots Hyper-V produisent un fichier `.bin`. Ces fichiers sont directement analysables avec Volatility sans avoir besoin d'exécuter un outil d'acquisition dans la VM — ce qui est un avantage considérable (pas de modification de la mémoire par l'outil d'acquisition).

**Acquisition à distance :** Velociraptor permet de déclencher un dump mémoire à distance sur n'importe quelle machine équipée de l'agent, sans intervention physique. F-Response offre une capacité similaire via un accès réseau au disque et à la mémoire de machines distantes.

#### 6.3 Pagefile et hiberfil : mémoire persistante

Le **pagefile.sys** (Windows) est le fichier d'échange — quand la RAM est pleine, Windows y déplace des pages mémoire. Ces pages peuvent contenir des fragments de processus, des credentials, des URLs, et d'autres données. Le pagefile persiste sur le disque même après un reboot — c'est une source de mémoire « fossile » quand le dump RAM n'a pas été fait à temps.

Le **hiberfil.sys** (Windows) est le fichier d'hibernation — quand la machine entre en hibernation, l'intégralité de la RAM est écrite dans ce fichier. Un hiberfil est littéralement un dump mémoire compressé, analysable avec Volatility (plugin `windows.hibernation`). Sur les laptops, l'hibernation est fréquente — c'est une source souvent négligée.

Sous Linux, le **swap** joue un rôle similaire au pagefile (fichier ou partition d'échange), et le suspend-to-disk écrit la RAM dans la partition swap.

#### 6.4 Workflow d'arrivée sur une machine allumée

L'ordre des opérations quand l'analyste arrive sur une machine allumée et potentiellement compromise :

1. **Documenter l'état initial** : photographier l'écran (ce qui est affiché), noter l'heure système (pour calibrer les timestamps), identifier les processus visibles.
2. **Dump RAM** : exécuter DumpIt ou WinPmem depuis une clé USB. Ne pas installer d'outil sur le disque de la machine (on contaminerait la preuve). Durée : 10-20 minutes selon la quantité de RAM.
3. **Triage KAPE** (optionnel si le temps le permet) : collecte des artefacts système depuis la clé USB. Durée : 5-10 minutes.
4. **Capturer l'état réseau** : `netstat -ano` (Windows) ou `ss -tunap` (Linux) pour capturer les connexions réseau actives — elles disparaîtront à l'isolation.
5. **Isoler du réseau** : déconnecter le câble réseau ou désactiver le WiFi — l'attaquant ne peut plus communiquer avec la machine, mais la mémoire est préservée.
6. **Acquisition disque** : si nécessaire, avec write blocker.

> **Alerte :** L'exécution de DumpIt ou de KAPE modifie la mémoire de la machine (l'outil lui-même charge du code en mémoire, crée des processus, alloue des pages). C'est inévitable et documenté — l'analyste note dans le journal que le dump a modifié l'état mémoire et que les artefacts de l'outil de collecte seront visibles dans l'analyse. Ce compromis est accepté car l'alternative (ne pas dumper la RAM) est pire.

#### 6.5 Fil rouge — MUSIC BOX : le dump RAM critique

> **🔬 MUSIC BOX — Épisode 6**
>
> Vendredi soir, 19h15. Claire arrive devant WKS-RD-047. L'écran affiche le bureau Windows avec plusieurs fenêtres ouvertes. Elle photographie l'écran (capture de l'état visuel), note l'heure système (19h15:23, UTC+1), et insère sa clé USB contenant DumpIt.
>
> Le dump prend 14 minutes (32 Go de RAM). Le hash SHA-256 est calculé immédiatement : `a7f3e2d8...`. Claire note dans le journal : « 19h15 — début dump RAM WKS-RD-047 avec DumpIt v2.1 depuis USB. 19h29 — fin du dump. SHA-256 : a7f3e2d8... Taille : 34 359 738 368 octets. La machine n'a pas été éteinte ni isolée du réseau avant le dump pour préserver les connexions actives. L'outil DumpIt a modifié l'état mémoire (attendu). »
>
> Ce dump sera la pièce maîtresse de l'investigation : c'est grâce à lui que l'équipe identifiera le processus svchost injecté, les connexions vers le C2 en Asie du Sud-Est, et les credentials en clair de 8 comptes dans la mémoire de LSASS.

---

### Chapitre 7 — Acquisition réseau et captures de trafic

#### 7.1 Quand et comment capturer du trafic

La capture de trafic réseau en temps réel n'est possible que si l'infrastructure le permet (port mirroring sur le switch, TAP réseau, ou NDR déployé). En forensic, la capture se fait rarement au moment de l'incident initial (on n'avait pas prévu de capturer) — on travaille plus souvent avec les logs réseau existants (proxy, pare-feu, DNS, VPN) et les captures historiques du NDR si disponible.

Si une capture live est possible, **tcpdump** est l'outil en ligne de commande de référence : `tcpdump -i eth0 -w capture.pcap -c 1000000` capture un million de paquets sur l'interface eth0. **Wireshark** offre une interface graphique pour la capture et l'analyse. **Zeek** (ex-Bro) ne capture pas les paquets bruts mais produit des logs structurés (connexions, requêtes DNS, requêtes HTTP, certificats TLS) beaucoup plus faciles à analyser à grande échelle.

Les captures doivent être filtrées par pertinence : capturer tout le trafic d'un réseau de 10 Gbit/s produit des téraoctets de données en quelques heures — inutilisable. Les filtres utiles : par IP suspecte (connue C2), par port (443 sortant vers des destinations inhabituelles), par machine source (la machine compromise), ou par protocole (DNS pour le tunneling, HTTP/HTTPS pour le C2).

#### 7.2 Logs réseau existants

En pratique, les logs existants sont la source réseau principale. Les **logs proxy** (Squid, Zscaler, Blue Coat) contiennent les URLs visitées, les user-agents, les volumes de données, et les codes de retour HTTP — essentiels pour identifier l'exfiltration et le C2 web. Les **logs pare-feu** (Palo Alto, Fortinet, Check Point) contiennent les flux autorisés et refusés avec IP source, IP destination, port, protocole, et volume — essentiels pour identifier les communications inhabituelles. Les **logs DNS** (Infoblox, BIND, Windows DNS) contiennent les résolutions de domaine — essentiels pour identifier les domaines DGA, le DNS tunneling, et les résolutions vers des C2. Les **logs VPN** contiennent les connexions avec géolocalisation, horodatage, et durée — essentiels pour identifier les accès compromis.

Les **NetFlow** (métadonnées de flux réseau sans le contenu des paquets : source, destination, port, volume, durée) sont une source intermédiaire entre les logs et le PCAP — moins détaillée que le PCAP mais disponible en rétention longue et à grande échelle.

#### 7.3 Fil rouge — MUSIC BOX : les logs réseau

> **🔬 MUSIC BOX — Épisode 7**
>
> NovaPharma n'a pas de NDR ni de capture PCAP historique. Les sources réseau disponibles sont le proxy Squid (6 mois de rétention), le pare-feu Palo Alto (12 mois), le DNS Infoblox (3 mois), et le VPN Fortinet (12 mois). Claire demande à l'IT d'exporter immédiatement ces logs vers le stockage forensic — avant que la rotation ne les efface.
>
> Premier résultat du proxy : le poste WKS-RD-047 a des connexions HTTPS régulières vers `103.xx.xx.xx:443` toutes les 30 minutes (pattern de beaconing) depuis 60 jours. Le user-agent est `Mozilla/5.0 NovaPharma` — l'attaquant a personnalisé le user-agent de son RAT.

---

### Chapitre 8 — Acquisition des logs, des données d'identité et du cloud

#### 8.1 Acquisition des Event Logs Windows

Les Event Logs Windows (format `.evtx`) sont stockés dans `C:\Windows\System32\winevt\Logs\`. Méthodes d'acquisition : copie directe des fichiers `.evtx` (possible sur une machine éteinte ou via un partage réseau), export via PowerShell (`wevtutil epl Security C:\export\Security.evtx`), collecte via KAPE (target `EventLogs` — collecte automatiquement tous les fichiers evtx), ou collecte centralisée depuis le SIEM (si les logs ont été envoyés à un SIEM, ils y sont préservés même si l'attaquant efface les logs locaux — c'est l'une des défenses les plus efficaces contre l'anti-forensics).

Les canaux critiques à collecter : Security (authentification, audit), System (services, pilotes), Application, PowerShell/Operational (script block logging — Event ID 4104), Microsoft-Windows-Sysmon/Operational (si Sysmon est déployé), Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational (RDP), et Microsoft-Windows-TaskScheduler/Operational (tâches planifiées).

#### 8.2 Acquisition des logs Linux

Les logs Linux sont stockés dans `/var/log/` et via systemd-journald. Les fichiers clés : `auth.log` ou `secure` (authentifications, sudo, SSH), `syslog` (événements système), `kern.log` (événements noyau), les logs applicatifs (`/var/log/apache2/`, `/var/log/nginx/`, `/var/log/mysql/`), et les fichiers de session (`wtmp`, `btmp`, `lastlog`).

Pour le journald : `journalctl --since "2026-01-01" --until "2026-03-08" -o json > journal_export.json` exporte les logs systemd au format JSON, exploitable par les outils de timeline.

La collecte des historiques de commandes (`.bash_history`, `.zsh_history`) doit inclure non seulement les fichiers dans les home directories mais aussi la recherche dans la mémoire et les fichiers supprimés — l'attaquant supprime souvent son historique, mais des traces peuvent persister en mémoire, dans le swap, ou dans les secteurs non alloués du disque.

#### 8.3 Acquisition des données Active Directory

L'AD est une source critique souvent sous-exploitée en forensic. Le fichier **ntds.dit** (la base de données AD, stockée sur les DC dans `C:\Windows\NTDS\`) contient tous les objets AD (utilisateurs, groupes, GPO, ACL) et les hashes NTLM de tous les comptes. Son acquisition se fait via volume shadow copy (`vssadmin create shadow /for=C:`) puis copie du ntds.dit depuis le shadow, ou via `ntdsutil` en mode snapshot. L'analyse avec `secretsdump.py` (Impacket) ou DSInternals (PowerShell) permet d'extraire les hashes et de comprendre la compromission AD (Ch.20).

Les **logs de réplication AD** sont essentiels pour détecter le DCSync (Event ID 4662 avec les GUID de réplication). Les **métadonnées AD** (date de création et de modification des objets, via `repadmin /showmeta` ou ADRecon) révèlent les modifications récentes — comptes créés, groupes modifiés, GPO ajoutées.

**ADTimeline** (outil de l'ANSSI) produit une timeline des modifications AD à partir des métadonnées de réplication — c'est l'outil de référence pour comprendre chronologiquement ce que l'attaquant a fait dans l'AD.

#### 8.4 Acquisition des données cloud

**Microsoft 365 :** l'Unified Audit Log (UAL) est exportable via PowerShell (`Search-UnifiedAuditLog`) ou via le portail Purview Compliance. La rétention dépend de la licence (180 jours en E3, jusqu'à 365 jours en E5). Le Sign-in Log est exportable via le portail Entra ID ou via l'API Microsoft Graph. L'eDiscovery permet de placer un **legal hold** sur des boîtes mail (préservation contre suppression) et d'exporter des données ciblées.

**AWS :** CloudTrail enregistre chaque appel API (exportable en JSON — `aws cloudtrail lookup-events`). Les VPC Flow Logs capturent les métadonnées réseau. Les S3 Access Logs tracent les accès aux buckets. Les EBS Snapshots permettent de capturer l'état d'un volume sans arrêter l'instance.

Les **limitations de rétention** sont un piège fréquent : si le dwell time dépasse la rétention des logs cloud, les premières actions de l'attaquant sont perdues. La vérification de la rétention effective (pas théorique) doit être faite dès le début de l'investigation.

#### 8.5 Fil rouge — MUSIC BOX : les logs AD et cloud

> **🔬 MUSIC BOX — Épisode 8**
>
> Samedi 10h00. Claire lance la collecte des données d'identité et cloud.
>
> **AD :** Export des Event Logs Security et System de DC01 via PowerShell (wevtutil). Snapshot volume shadow copy de DC01 pour acquisition du ntds.dit. Exécution d'ADTimeline pour reconstituer la chronologie des modifications AD.
>
> **Cloud :** NovaPharma utilise AWS pour le stockage des données R&D (S3) et Microsoft 365 (E3) pour la messagerie. Export du UAL M365 via PowerShell (180 jours disponibles — suffisant pour couvrir la fenêtre J-60 à J). Export de CloudTrail AWS (90 jours par défaut, mais NovaPharma avait configuré un trail vers S3 avec rétention longue — les 12 derniers mois sont disponibles).
>
> Premier résultat CloudTrail : 347 appels `GetObject` sur le bucket `projets-molecule-np427` en 5 jours (J-5 à J-1), depuis un rôle IAM légitime (`svc-backup-role`) mais utilisé depuis l'IP externe `103.xx.xx.xx` — le C2. Les access keys ont été exfiltrées du serveur R&D Linux par l'attaquant.

---

## PARTIE III — ANALYSE FONDAMENTALE ET RAISONNEMENT FORENSIC

*Cette partie couvre les fondamentaux transversaux de l'analyse : la compréhension des systèmes de fichiers (le substrat de toute analyse disque), la construction de la timeline (le livrable central), et le raisonnement analytique (la compétence intellectuelle qui distingue l'analyste du simple opérateur d'outils).*

---

### Chapitre 9 — Systèmes de fichiers : comprendre ce qu'on analyse

#### 9.1 Pourquoi comprendre le système de fichiers

Le système de fichiers est la couche d'organisation entre le stockage brut (secteurs du disque) et les fichiers tels que l'utilisateur les voit. Sans comprendre cette couche, l'analyste ne peut pas interpréter les métadonnées, récupérer les fichiers supprimés, ni détecter les manipulations de timestamps. Chaque système de fichiers a sa propre logique de stockage, ses propres métadonnées, et ses propres artefacts forensic.

#### 9.2 NTFS — le système de fichiers le plus riche en artefacts

NTFS (New Technology File System) est le système de fichiers standard de Windows et le plus riche en artefacts forensic.

La **MFT** (Master File Table) est le cœur de NTFS : chaque fichier et dossier du volume possède une entrée dans la MFT (enregistrement de 1 024 octets) qui contient ses attributs. Les attributs clés pour le forensic :

**$STANDARD_INFORMATION ($SI)** contient les timestamps MACB (Modified, Accessed, Changed, Born/Created) du fichier. Ces timestamps sont modifiés par le système d'exploitation lors des opérations normales, mais AUSSI par les outils de timestomping (l'attaquant modifie délibérément les dates pour brouiller la timeline). C'est pourquoi $SI seul ne suffit pas pour dater fiablement un fichier.

**$FILE_NAME ($FN)** contient un second jeu de timestamps MACB, mis à jour uniquement lors du renommage ou du déplacement du fichier — ils sont beaucoup plus difficiles à falsifier (les outils de timestomping standard ne les modifient pas). La comparaison $SI vs $FN est l'outil fondamental de détection du timestomping : si $SI indique « créé en 2022 » mais $FN indique « créé le 3 mars 2026 », il y a eu manipulation.

**$DATA** contient le contenu du fichier lui-même. Pour les petits fichiers (< environ 700 octets), le contenu est stocké directement dans l'entrée MFT (resident data). Pour les fichiers plus grands, $DATA pointe vers les clusters du disque qui contiennent les données.

Les **ADS** (Alternate Data Streams) sont des flux de données secondaires attachés à un fichier, invisibles dans l'explorateur Windows et dans la plupart des commandes (`dir`). Un fichier `rapport.docx` peut avoir un ADS `rapport.docx:hidden_data` contenant des données cachées. Les ADS sont utilisés par Windows lui-même (le flux `Zone.Identifier` indique d'où un fichier a été téléchargé) et par les attaquants pour cacher des données ou du code.

Le journal **$UsnJrnl** (Update Sequence Number Journal) enregistre toutes les modifications de fichiers sur le volume : création, modification, suppression, renommage. Même si un fichier a été supprimé, le $UsnJrnl conserve la trace (avec le nom, la date, et l'opération). C'est une source forensic de première importance, parseable avec MFTECmd.

Le journal **$LogFile** enregistre les transactions NTFS pour la récupération après crash — il contient des informations sur les opérations récentes du système de fichiers.

#### 9.3 ext4, FAT32/exFAT et APFS

**ext4** (Linux) utilise des inodes au lieu de la MFT. Les timestamps incluent crtime (creation time, introduit en ext4), mtime, atime, ctime. Le journal ext4 enregistre les transactions pour la cohérence. La récupération de fichiers supprimés est possible (extundelete, ext4magic) mais moins fiable qu'avec NTFS car ext4 réinitialise les pointeurs d'inode lors de la suppression.

**FAT32/exFAT** (USB, cartes SD) : structure simple, peu de métadonnées, pas de journalisation, pas d'ADS. Les fichiers supprimés sont souvent récupérables car FAT marque l'entrée de répertoire comme supprimée sans effacer les données.

**APFS** (macOS/iOS) : chiffrement natif (FileVault intégré), snapshots (instantanés récupérables contenant des états antérieurs du volume — source forensic précieuse), et clones. Le chiffrement natif rend l'acquisition physique sans clé inutile.

#### 9.4 Fichiers supprimés et carving

Comprendre ce qui se passe lors de la suppression est fondamental. Sur NTFS, supprimer un fichier marque l'entrée MFT comme inactive et libère les clusters — les données restent physiquement sur le disque tant que les clusters ne sont pas réécrits. Le **carving** est la technique de récupération par signature : l'outil (Scalpel, PhotoRec, foremost) parcourt l'espace non alloué en cherchant les en-têtes et pieds de page des formats de fichiers connus (JPEG commence par `FF D8 FF`, PDF par `%PDF-`, DOCX par `PK` car c'est un ZIP). Le carving fonctionne même quand l'entrée MFT est perdue — il retrouve les données brutes par leur structure interne. Mais sur SSD avec TRIM, les données supprimées sont souvent effacées physiquement par le contrôleur — le carving ne retrouve rien.

#### 9.5 Timestamps MACB et détection du timestomping

Les timestamps MACB sont les artefacts temporels fondamentaux de l'analyse forensic. En NTFS, chaque fichier possède deux jeux de timestamps (dans $SI et dans $FN). La comparaison entre les deux est l'outil principal de détection du timestomping.

Méthode concrète avec MFTECmd : parser la $MFT avec `MFTECmd.exe -f '$MFT' --csv output/ --csvf mft_results.csv`, puis ouvrir le CSV dans Timeline Explorer et comparer les colonnes `SI_Created` et `FN_Created`. Si `SI_Created` est antérieur à `FN_Created` (le fichier aurait été « créé » avant que son nom n'existe), c'est un indicateur de timestomping.

Les **fuseaux horaires** sont un piège récurrent. Les timestamps NTFS sont stockés en UTC, mais les outils d'affichage (Event Viewer, explorateur Windows) les convertissent en heure locale. Si deux machines dans des fuseaux horaires différents sont corrélées sans conversion en UTC, la timeline est incohérente. Règle : toujours travailler en UTC dans l'analyse forensic, convertir en heure locale uniquement pour la présentation au rapport.

#### 9.6 Slack space et unallocated space

Le **slack space** est l'espace résiduel entre la fin d'un fichier et la fin du cluster alloué (les systèmes de fichiers allouent par clusters de 4 Ko typiquement — un fichier de 2 Ko occupe un cluster entier, les 2 Ko restants contiennent des fragments du fichier précédemment stocké à cet emplacement). L'**unallocated space** est l'ensemble des clusters non affectés à un fichier actif — c'est là que se trouvent les données des fichiers supprimés. L'analyse de ces espaces par carving peut révéler des données que l'attaquant croyait avoir détruites.

---

### Chapitre 10 — Timeline analysis et corrélation temporelle

#### 10.1 Pourquoi la timeline est le livrable central

La timeline (chronologie d'investigation) est la reconstruction ordonnée dans le temps de tous les événements pertinents de l'incident. C'est le livrable qui répond à la question fondamentale du forensic : que s'est-il passé, dans quel ordre ? C'est aussi le support de raisonnement principal de l'analyste : en examinant la séquence des événements, il identifie les patterns, les corrélations, et les lacunes.

Une timeline forensic complète peut contenir des millions d'événements (sur une machine Windows, la MFT seule produit des centaines de milliers d'entrées, les Event Logs en ajoutent des dizaines de milliers, le Prefetch, l'Amcache, le registre, le navigateur en ajoutent encore). L'enjeu n'est pas de tout voir — c'est de filtrer, de prioriser, et de corréler.

#### 10.2 Construction d'une Super Timeline avec Plaso

**Plaso** (anciennement log2timeline) est l'outil de référence pour la construction de Super Timelines. Il prend en entrée une image disque (ou un ensemble d'artefacts collectés par KAPE) et produit en sortie un fichier contenant TOUS les événements temporels de toutes les sources, fusionnés et triés chronologiquement.

Workflow concret :

```bash
# Étape 1 : extraction des événements (long — heures sur une image de 500 Go)
log2timeline.py --storage-file timeline.plaso image.E01

# Étape 2 : filtrage et export en CSV
psort.py -o l2tcsv timeline.plaso -w timeline.csv "date > '2026-01-01' AND date < '2026-03-08'"
```

Le résultat est un CSV contenant potentiellement des millions de lignes, chaque ligne étant un événement avec sa date/heure, sa source (MFT, Event Log, Prefetch, navigateur...), sa description, et des métadonnées contextuelles.

Les **parsers Plaso** sont les modules qui extraient les événements de chaque type de source. Les parsers les plus importants pour le forensic Windows : `filestat` (timestamps du système de fichiers), `winevtx` (Event Logs), `prefetch` (Prefetch), `winreg` (registre), `chrome_history` / `firefox_history` (navigateurs), et `mft` (MFT NTFS). Pour Linux : `syslog`, `bash_history`, `wtmp`.

Les pièges de Plaso : le temps de traitement est long (plusieurs heures pour une image de 500 Go), le volume de données produit est massif (il faut filtrer agressivement), et les parsers peuvent produire des faux positifs (événements mal interprétés ou dupliqués entre parsers).

#### 10.3 Visualisation et analyse avec Timeline Explorer et Timesketch

**Timeline Explorer** (Eric Zimmerman) est l'outil de visualisation le plus utilisé pour analyser les CSV produits par Plaso ou par les autres outils de la suite Zimmerman. Il permet le filtrage par colonne (filtrer par source, par chemin de fichier, par mots-clés), le tri chronologique, le marquage d'événements (bookmarks), et l'export des résultats filtrés.

**Timesketch** (open source, développé par Google) est une plateforme web collaborative de visualisation de timelines. Il permet l'import de timelines Plaso, le partage entre analystes, l'annotation collaborative, et l'application de « sketches » (filtres prédéfinis pour identifier des patterns courants — beaconing, mouvement latéral, exfiltration).

#### 10.4 Corrélation multi-sources

Le défi de la corrélation est de fusionner des événements provenant de sources hétérogènes (endpoint + réseau + AD + cloud) dans une timeline cohérente. Un exemple concret : à 14h32:15 UTC, le Prefetch montre l'exécution de `psexec.exe` sur la machine A ; à 14h32:18 UTC, le Security Event Log de la machine B montre une authentification réussie (4624 type 3) depuis l'IP de la machine A avec le compte `svc_deploy` ; à 14h32:22 UTC, le log pare-feu montre un flux autorisé de A vers B sur le port 445 (SMB). Ces trois événements, provenant de trois sources différentes, racontent la même histoire : mouvement latéral de A vers B via PsExec.

La corrélation multi-sources exige une synchronisation horaire fiable (NTP — si les horloges ne sont pas synchronisées, les événements ne peuvent pas être alignés), une normalisation des fuseaux horaires (tout en UTC), et une normalisation des identifiants (le même compte peut apparaître sous différentes formes selon la source : `DOMAIN\user`, `user@domain.com`, SID).

#### 10.5 Pièges de la corrélation temporelle

**Fuseaux horaires incohérents :** les timestamps NTFS sont en UTC, les Event Logs Windows sont en UTC, les logs proxy peuvent être en heure locale, les logs applicatifs peuvent être dans le fuseau du serveur, et les captures réseau (PCAP) sont en UTC. Si un analyste mélange des sources sans normaliser en UTC, sa timeline est fausse.

**Précision des timestamps :** les timestamps NTFS ont une précision de 100 nanosecondes, les Event Logs ont une précision de 100 nanosecondes (format FILETIME), mais les logs proxy ou applicatifs peuvent n'avoir qu'une précision à la seconde. Ordonner des événements à la seconde près quand certaines sources n'ont qu'une précision à la seconde est un exercice de prudence.

**Timestamps falsifiés :** le timestomping modifie les timestamps $SI des fichiers (Ch.9, Ch.24). La corrélation avec d'autres sources (Event Logs, $UsnJrnl, $FN) permet de détecter les incohérences.

#### 10.6 Fil rouge — MUSIC BOX : la timeline de 60 jours

> **🔬 MUSIC BOX — Épisode 9**
>
> Dimanche. Claire construit la Super Timeline de WKS-RD-047 avec Plaso : 2,4 millions d'événements sur 60 jours. Elle filtre sur les événements les plus pertinents (exécution de programmes, accès réseau, modifications de fichiers dans les répertoires sensibles) et réduit à environ 15 000 événements exploitables. La corrélation avec les logs proxy (beaconing C2), les logs AD (authentifications), et les logs AWS (accès aux buckets S3) produit une timeline unifiée qui reconstitue les 60 jours de présence de l'attaquant.

---

### Chapitre 11 — Corrélation, raisonnement analytique et gestion des biais

#### 11.1 Le forensic n'est pas juste extraire des artefacts

La compétence technique — savoir parser une MFT, analyser un dump mémoire, interpréter un Event Log — est nécessaire mais pas suffisante. Ce qui distingue un analyste compétent d'un opérateur d'outils, c'est la capacité à raisonner sur les données : formuler des hypothèses, les tester, gérer l'incertitude, et distinguer ce que les données montrent de ce que l'analyste infère.

#### 11.2 Raisonnement par hypothèse

L'investigateur forensic ne cherche pas « la vérité » — il formule des hypothèses et les teste contre les données disponibles. Pour chaque question investigative, au moins deux hypothèses doivent être formulées.

Exemple dans MUSIC BOX : le compte `svc-backup` a été utilisé pour supprimer des fichiers de recherche. Hypothèse 1 : le compte a été compromis par un attaquant externe et utilisé pour l'exfiltration et la destruction de données. Hypothèse 2 : le titulaire légitime du compte (un administrateur système) a supprimé les fichiers pour une raison légitime ou malveillante (insider threat). L'investigation doit collecter des données qui permettent de discriminer entre ces hypothèses : l'IP source des connexions (interne vs externe), la présence d'un malware sur la machine, les logs de keylogging ou de credential dumping, et le profil comportemental de l'administrateur.

#### 11.3 Le biais de confirmation

Le biais de confirmation est le piège le plus dangereux de l'investigation forensic. Il consiste à chercher sélectivement les données qui confirment l'hypothèse initiale et à ignorer ou minimiser celles qui la contredisent. Ce biais est inconscient et universel — même les analystes expérimentés y sont vulnérables.

Exemple : l'analyste suspecte un insider (un employé sur le départ). Il trouve des fichiers copiés sur une clé USB. Il interprète immédiatement : « voilà la preuve du vol de données ». Mais il ne cherche pas si le malware présent sur la machine a pu copier les fichiers automatiquement vers la clé USB. Il ne vérifie pas si l'employé copiait régulièrement des fichiers sur USB dans le cadre de son travail normal. Le biais de confirmation l'a conduit à s'enfermer dans sa première hypothèse sans tester les alternatives.

Contremesure : pour chaque conclusion, l'analyste se pose la question « qu'est-ce qui pourrait contredire cette interprétation ? » et recherche activement ces données contradictoires. La discipline de l'hypothèse alternative (formuler au moins 2 hypothèses et les tester toutes) est le garde-fou principal.

#### 11.4 Niveaux de confiance dans les conclusions

Chaque conclusion forensic doit être accompagnée d'un niveau de confiance explicite.

**Fait vérifié :** observable directement dans les données, reproductible. « Le fichier `rclone.exe` a été exécuté sur WKS-RD-047 le 2 mars 2026 à 14h32 UTC » (constaté dans le Prefetch ET l'Amcache ET les Event Logs — triple confirmation).

**Déduction logique :** conclusion tirée par raisonnement à partir de faits vérifiés. « L'exfiltration a été réalisée via rclone, car le SRUM montre que `rclone.exe` a transféré 180 Go de données réseau entre le 2 et le 7 mars, et les logs proxy confirment des flux HTTPS vers des endpoints S3 AWS depuis cette machine pendant la même période. » (déduction forte, basée sur la convergence de 3 sources indépendantes).

**Hypothèse plausible :** interprétation cohérente mais non confirmée de manière certaine. « L'attaquant est probablement d'origine russophone, car les metadata du document Word piégé contiennent un auteur avec un nom cyrillique et le RAT utilise un C2 dans un ASN associé à un hébergeur d'Asie du Sud-Est couramment utilisé par des groupes russophones » (indices convergents mais non conclusifs — l'attaquant pourrait avoir falsifié ces éléments).

**Inconnue :** ce que l'investigation n'a pas pu déterminer. « L'identité réelle de l'attaquant n'a pas pu être établie dans le cadre de cette investigation. » Documenter les inconnues est aussi important que documenter les conclusions.

#### 11.5 Corrélation vs causalité

Deux événements proches dans le temps ne sont pas nécessairement liés. Un reboot de serveur à 03h00 et une connexion C2 à 03h02 ne sont pas forcément le même incident — le reboot peut être une maintenance planifiée, et la connexion C2 un beaconing régulier qui a coïncidé temporellement. La corrélation temporelle est un indice, pas une preuve de causalité. L'analyste doit chercher des liens causaux (le reboot a été déclenché par un script déposé par l'attaquant — vérifiable dans les Event Logs et le registre) et ne pas se contenter de la proximité temporelle.

#### 11.6 Fil rouge — MUSIC BOX : les hypothèses concurrentes

> **🔬 MUSIC BOX — Épisode 10**
>
> Lundi. Claire formule ses hypothèses concurrentes pour la question investigative #1 (vecteur d'accès initial).
>
> **H1 :** Spearphishing avec document piégé envoyé au Dr. Mallet. Indices : le RAT est actif sur son poste, les emails suspects sont à vérifier.
> **H2 :** Compromission d'un accès VPN/RDP exposé sur Internet. Indices : vérifier les logs VPN pour des connexions anormales.
> **H3 :** Insider — le Dr. Mallet ou un collègue a intentionnellement installé le RAT. Indices : vérifier le comportement de l'utilisateur, les accès physiques, et les motivations.
>
> L'investigation des emails (export PST de la boîte du Dr. Mallet) révèle un email de spearphishing reçu le 6 janvier 2026 (J-60), prétendant provenir d'un partenaire de recherche (`novapharma-partners.com` — domaine imitant le domaine légitime `novapharma-partner.com`). Le document Word joint contient une macro VBA obfusquée (confirmé par olevba). **H1 est confirmée. H2 et H3 ne sont pas soutenues par les données** (pas de connexion VPN anormale, pas d'accès physique suspect). Mais H3 n'est pas formellement exclue — elle est documentée comme « non soutenue en l'état ».

---

## PARTIE IV — ANALYSE FORENSIC AVANCÉE

*Le cœur technique du cours. Sept chapitres couvrant l'analyse détaillée des artefacts Windows (3 chapitres avec frontières nettes : registre/exécution, activité/mouvement latéral, Event Logs), Linux, macOS, mémoire vive, et malware.*

---

### Chapitre 12 — Windows forensics : registre et artefacts d'exécution

*Ce chapitre couvre ce que la machine « sait » sur les programmes qui ont été exécutés. Le Ch.13 couvrira l'activité utilisateur et le mouvement latéral. Le Ch.14 couvrira les Event Logs. Cette séparation évite les redites : le Prefetch apparaît ici (artefact d'exécution), les traces RDP apparaissent au Ch.13 (mouvement latéral), et les Event IDs apparaissent au Ch.14 (journaux d'audit).*

#### 12.1 Le registre Windows comme mine forensic

Le registre Windows est une base de données hiérarchique qui stocke la configuration du système et des applications. Pour le forensic, c'est la source la plus riche après les Event Logs.

Les **fichiers de ruche** (hive files) sont les fichiers physiques qui contiennent le registre. Leur localisation est fixe. **SAM** (`C:\Windows\System32\config\SAM`) contient les comptes locaux et leurs hashes NTLM — exploitable avec `secretsdump.py` ou RegRipper pour identifier les comptes créés par l'attaquant. **SYSTEM** (`C:\Windows\System32\config\SYSTEM`) contient la configuration matérielle, le nom de l'ordinateur, le fuseau horaire (critique pour la corrélation), les informations de boot, et la clé de déchiffrement (BootKey) nécessaire pour décrypter les hashes SAM. **SOFTWARE** (`C:\Windows\System32\config\SOFTWARE`) contient les logiciels installés (clé `Microsoft\Windows\CurrentVersion\Uninstall`), les profils réseau (clé `Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles` — historique des réseaux WiFi et Ethernet avec dates de connexion), et les services (clé `CurrentControlSet\Services`). **NTUSER.DAT** (`C:\Users\<username>\NTUSER.DAT`) est la ruche spécifique à chaque utilisateur : elle contient les MRU (Most Recently Used — derniers fichiers ouverts), les ShellBags (navigation dans l'explorateur), les clés Run/RunOnce (persistence au login), les UserAssist (programmes exécutés via le GUI avec nombre d'exécutions et timestamps), et les Typed Paths (chemins saisis manuellement dans l'explorateur — y compris les chemins réseau UNC). **UsrClass.dat** (`C:\Users\<username>\AppData\Local\Microsoft\Windows\UsrClass.dat`) contient les associations de fichiers et les ShellBags supplémentaires (notamment pour les dossiers réseau et les drives réseau mappés).

**Outils de parsing :** **RegRipper** (Harlan Carvey) est l'outil classique d'extraction automatisée — il exécute des plugins prédéfinis sur chaque ruche et produit un rapport texte structuré. **Registry Explorer** (Eric Zimmerman) offre une interface graphique d'exploration interactive avec recherche, favoris, et export. **RECmd** (Eric Zimmerman, ligne de commande) permet l'exécution de batch files prédéfinies (comme `RECmd_Batch_MC.reb` qui extrait automatiquement tous les artefacts forensic connus de toutes les ruches collectées).

#### 12.2 Artefacts d'exécution de programmes

Ces artefacts répondent à la question centrale : quels programmes ont été exécutés sur cette machine, quand, et combien de fois ?

**Prefetch** (`C:\Windows\Prefetch\`) : Windows crée un fichier `.pf` pour chaque programme exécuté, contenant le nom de l'exécutable, les 8 dernières dates/heures d'exécution (Windows 10/11), le nombre total d'exécutions, et la liste des fichiers et répertoires chargés par le programme lors des dernières exécutions. Le Prefetch est l'artefact le plus direct et le plus fiable pour prouver l'exécution d'un programme — même si l'exécutable a été supprimé du disque, le fichier .pf persiste. Outil de parsing : **PECmd** (Eric Zimmerman) — `PECmd.exe -f "PSEXEC.EXE-AD70946C.pf" --csv output/`. Le résultat inclut le nombre d'exécutions et les 8 dernières dates.

> **Limite :** Le Prefetch est désactivé par défaut sur Windows Server (le service SysMain n'est pas démarré). Sur les serveurs, l'Amcache et le ShimCache sont les alternatives.

**Amcache** (`C:\Windows\appcompat\Programs\Amcache.hve`) : registre qui enregistre les programmes installés et exécutés avec leurs hashes SHA1 et leur chemin complet. L'Amcache est particulièrement précieux pour deux raisons : le hash SHA1 permet d'identifier formellement le binaire exécuté (vérification sur VirusTotal), et il fonctionne sur Windows Server (contrairement au Prefetch). Outil : **AmcacheParser** — `AmcacheParser.exe -f Amcache.hve --csv output/`.

**ShimCache / AppCompatCache** (stocké dans la ruche SYSTEM, clé `CurrentControlSet\Control\Session Manager\AppCompatCache`) : enregistre le chemin et le timestamp de modification de chaque programme exécuté (ou simplement parcouru dans l'explorateur sur certaines versions). Le ShimCache est persisté au shutdown — il reflète l'état au dernier redémarrage. Outil : **AppCompatCacheParser** — `AppCompatCacheParser.exe -f SYSTEM --csv output/`.

**BAM/DAM** (Background Activity Moderator / Desktop Activity Monitor, stockés dans la ruche SYSTEM, clés `ControlSet001\Services\bam\State\UserSettings\<SID>`) : enregistrent les programmes exécutés avec des timestamps UTC précis. Disponible sur Windows 10 1709+ et Server 2016+. Parsed par RegRipper ou RECmd.

**SRUM** (System Resource Usage Monitor, base SQLite `C:\Windows\System32\SRU\SRUDB.dat`) : enregistre la consommation de ressources (réseau, CPU, énergie) par processus et par utilisateur, sur 30 à 60 jours. Pour le forensic, la colonne de consommation réseau par processus est l'information la plus précieuse : elle révèle quel processus a transféré quel volume de données — excellent pour quantifier l'exfiltration même si le processus n'est plus actif. Outil : **SrumECmd** — `SrumECmd.exe -f SRUDB.dat -r SOFTWARE --csv output/`.

#### 12.3 Artefacts de persistance dans le registre

La persistance est le mécanisme par lequel l'attaquant s'assure que son malware survit au redémarrage de la machine. Les mécanismes basés sur le registre sont détaillés ici ; les mécanismes basés sur les services, les tâches planifiées, et d'autres vecteurs sont traités au Ch.25.

Les clés **Run/RunOnce** (`HKCU\Software\Microsoft\Windows\CurrentVersion\Run` et `HKLM\...`) lancent automatiquement un programme au login de l'utilisateur ou au démarrage de la machine. C'est le mécanisme de persistance le plus basique et le plus facilement détectable. Les clés **Winlogon** (`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`, valeurs `Userinit` et `Shell`) sont détournées pour exécuter du code au login — plus subtil que Run. Les clés **Image File Execution Options** (IFEO, `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\<exe>`, valeur `Debugger`) permettent de rediriger l'exécution d'un programme légitime vers un programme malveillant — très subtil.

La vérification croisée avec **Autoruns** (Sysinternals) ou Velociraptor (query `Autoruns`) est la méthode la plus fiable pour inventorier tous les points de persistance actifs sur une machine.

#### 12.4 Fil rouge — MUSIC BOX : les artefacts d'exécution

> **🔬 MUSIC BOX — Épisode 11**
>
> L'analyse des artefacts d'exécution de WKS-RD-047 avec les outils Eric Zimmerman révèle :
>
> **PECmd (Prefetch) :** `PSEXEC.EXE` — 3 exécutions, dernière le 7 mars 14h47 UTC. `RCLONE.EXE` — 12 exécutions (une par jour de J-12 à J-1), dernière le 6 mars 22h15 UTC. `CERTUTIL.EXE` — 2 exécutions à J-60 (le jour de l'infection initiale — certutil utilisé par la macro VBA pour télécharger le RAT). `MIMIKATZ.EXE` — 1 exécution à J-45 (credential dumping). Le Prefetch de `SVCHOST_7284.EXE` (le processus injecté) n'existe pas — c'est cohérent avec un process hollowing (le processus légitime svchost a été démarré normalement puis son code a été remplacé en mémoire).
>
> **AmcacheParser :** confirme les hashes SHA1 de `psexec.exe`, `rclone.exe`, et `mimikatz.exe`. Soumission sur VirusTotal : `mimikatz.exe` est identifié positivement. `rclone.exe` est le binaire officiel (non malveillant en soi — c'est un outil de synchronisation cloud légitime détourné).
>
> **SrumECmd :** `rclone.exe` a transféré 183 Go de données réseau en 12 jours. C'est la quantification de l'exfiltration, confirmant les 180 Go estimés via les logs proxy.

---

### Chapitre 13 — Windows forensics : activité utilisateur, navigateur et mouvement latéral

*Ce chapitre couvre ce que l'utilisateur (ou l'attaquant se faisant passer pour l'utilisateur) a fait sur la machine : quels fichiers ont été accédés, quels dossiers ont été navigués, quels sites ont été visités, et comment l'attaquant s'est déplacé vers d'autres machines.*

#### 13.1 Artefacts d'activité utilisateur

**ShellBags** (stockés dans NTUSER.DAT et UsrClass.dat) : enregistrent chaque dossier navigué dans l'explorateur Windows, avec les dates d'accès et les préférences d'affichage — même si le dossier a été supprimé depuis, la trace persiste dans les ShellBags. Pour le forensic, ils révèlent les répertoires explorés par l'attaquant (partages réseau, dossiers sensibles, lecteurs USB). Outil : **SBECmd** — `SBECmd.exe -d "C:\Users\JMallet" --csv output/`.

**LNK files** (raccourcis, `.lnk`, dans `C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Recent\`) : créés automatiquement quand un fichier est ouvert. Chaque fichier .lnk contient le chemin complet du fichier cible (y compris les chemins réseau UNC — `\\SRV-RD-01\projets\`), le volume d'origine (nom du volume, numéro de série — identifie les clés USB), les timestamps MAC du fichier cible, et la taille du fichier. Outil : **LECmd** — `LECmd.exe -d "C:\Users\JMallet\AppData\Roaming\Microsoft\Windows\Recent" --csv output/`.

**Jump Lists** (dans `C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations\`) : listes de fichiers récemment ouverts par application. Chaque application a son propre fichier Jump List, identifié par un AppID. Les Jump Lists contiennent les mêmes informations que les LNK files mais organisées par application. Outil : **JLECmd** — `JLECmd.exe -d "AutomaticDestinations" --csv output/`.

**UserAssist** (dans NTUSER.DAT, clé `Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist`) : enregistre les programmes exécutés via l'interface graphique (GUI) avec un compteur d'exécutions et le dernier timestamp. Les données sont encodées en ROT13 (obfuscation triviale, pas du chiffrement).

#### 13.2 Browser forensics

Les navigateurs web sont une source d'évidence massive et souvent sous-exploitée. Chrome, Firefox, et Edge stockent leurs données dans des bases SQLite accessibles dans le profil utilisateur.

**Chrome** (`C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Default\`) : `History` (historique de navigation et de téléchargements), `Cookies` (cookies de session — peuvent révéler des accès à des services cloud avec credentials volées), `Login Data` (credentials enregistrés — chiffrés avec DPAPI), `Web Data` (formulaires auto-remplies), `Preferences` (extensions installées — certaines extensions peuvent être malveillantes), `Favicons` (icônes des sites visités — preuve de visite même si l'historique a été effacé). Outil de parsing : **Hindsight** (open source) — `hindsight.py -i "C:\Users\JMallet\AppData\Local\Google\Chrome\User Data\Default" -o output/`.

**Firefox** (`C:\Users\<user>\AppData\Roaming\Mozilla\Firefox\Profiles\<profile>\`) : `places.sqlite` (historique et favoris), `cookies.sqlite`, `formhistory.sqlite`, `logins.json` + `key4.db` (credentials). **Edge** (Chromium-based) utilise la même structure que Chrome mais dans un chemin différent.

L'historique de navigation peut révéler la préparation de l'attaque (l'attaquant a recherché des informations sur l'infrastructure de NovaPharma depuis le poste compromis), l'accès à des services de transfert de fichiers (mega.nz, transfer.sh), ou la consultation de forums underground.

#### 13.3 Artefacts de mouvement latéral

Le mouvement latéral est la progression de l'attaquant d'un système à un autre au sein du réseau. Chaque technique de mouvement latéral laisse des artefacts spécifiques — tant sur la machine source que sur la machine destination.

**PsExec** : sur la machine destination, PsExec crée un service temporaire `PSEXESVC` (visible dans les Event Logs : Event ID 7045 — installation de service). Le binaire `PSEXESVC.exe` est copié dans `C:\Windows\` (visible dans la MFT et potentiellement dans le Prefetch). L'Event Log Security montre une authentification réseau (4624 type 3) suivie d'un accès au partage ADMIN$ (Event ID 5140). Sur la machine source, le Prefetch de `PSEXEC.EXE` confirme l'exécution avec le timestamp.

**RDP** : les connexions RDP laissent des traces riches. Sur la machine destination : Event IDs 21/22/25 dans le canal `TerminalServices-RemoteConnectionManager` (connexion établie, réussie, reconnexion), Event ID 4624 type 10 (logon RDP) dans Security, et le **RDP Bitmap Cache** (`C:\Users\<user>\AppData\Local\Microsoft\Terminal Server Client\Cache\`) qui contient des fragments visuels de la session RDP — potentiellement des captures d'écran de ce que l'attaquant a vu. L'outil **bmc-tools** ou **rdpieces** peut reconstituer des images à partir du cache bitmap. Sur la machine source : la clé registre `HKCU\Software\Microsoft\Terminal Server Client\Default` et les fichiers `.rdp` dans le profil listent les connexions RDP récentes.

**WMI** (Windows Management Instrumentation) : l'exécution de commandes à distance via WMI est plus discrète que PsExec. Les traces : Event ID 4688 (création de processus) avec `wmiprvse.exe` comme parent sur la machine destination, et les logs WMI dans `Microsoft-Windows-WMI-Activity/Operational`.

**SMB / Accès aux partages réseau** : Event IDs 5140 (accès à un partage) et 5145 (vérification d'accès à un fichier/dossier partagé — plus granulaire, nécessite l'activation de l'audit des partages). Ces événements sont essentiels pour tracer quels fichiers l'attaquant a accédé sur les serveurs de fichiers.

**Artefacts USB** : les connexions USB sont tracées dans le registre (SYSTEM\CurrentControlSet\Enum\USBSTOR), dans les logs PnP (Event ID 20001, 20003), et dans `C:\Windows\inf\setupapi.dev.log`. Ces artefacts identifient le type de périphérique, son numéro de série, les dates de première et dernière connexion — essentiels dans les investigations d'insider threat.

#### 13.4 Fil rouge — MUSIC BOX : mouvement latéral détecté

> **🔬 MUSIC BOX — Épisode 12**
>
> L'analyse des artefacts de mouvement latéral de WKS-RD-047 révèle les connexions vers d'autres machines.
>
> **LNK files (LECmd) :** 15 fichiers .lnk pointent vers des chemins réseau `\\SRV-RD-01\projets\molecule-np427\` — l'attaquant a navigué dans les fichiers de recherche depuis le poste compromis.
>
> **RDP (registre + Event Logs) :** le registre montre une connexion RDP récente vers `SRV-RD-01` (le serveur Linux — l'accès SSH est possible via RDP Gateway ? Non — investigation complémentaire : l'attaquant a utilisé PuTTY, dont le Prefetch confirme l'exécution). Les fichiers `.rdp` du profil de l'attaquant montrent aussi une connexion vers `DC01` (le contrôleur de domaine).
>
> **PsExec :** le Prefetch confirme l'exécution de PsExec sur WKS-RD-047. Les Event Logs de DC01 (collectés au Ch.8) montrent la création du service PSEXESVC (Event ID 7045) à J-14 — c'est le moment où l'attaquant a utilisé PsExec pour exécuter le DCSync sur DC01.

---

### Chapitre 14 — Windows forensics : Event Logs et journaux d'audit

*Ce chapitre est le référentiel de l'interprétation des Event Logs Windows pour le forensic. Il ne répète pas les artefacts de registre (Ch.12) ni les artefacts d'activité utilisateur (Ch.13) — il se concentre sur ce que les journaux d'audit racontent, comment les lire, et comment les corréler.*

#### 14.1 Architecture des Event Logs Windows

Les Event Logs Windows sont stockés au format `.evtx` (XML binaire) dans `C:\Windows\System32\winevt\Logs\`. Chaque fichier correspond à un canal (channel) : `Security.evtx` (authentification, audit de sécurité — la source la plus importante pour le forensic), `System.evtx` (services, pilotes, erreurs système), `Application.evtx` (événements applicatifs), et de nombreux canaux spécialisés (`Microsoft-Windows-PowerShell/Operational`, `Microsoft-Windows-Sysmon/Operational`, `Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational`, etc.).

La **rotation** des Event Logs est configurée par taille maximale (par défaut : 20 Mo pour Security, ce qui est insuffisant pour une investigation — les événements les plus anciens sont écrasés quand le fichier est plein). Sur un DC actif avec la configuration par défaut, le Security log peut tourner en quelques heures. La recommandation forensic readiness (Ch.27) est d'augmenter la taille à 1 Go minimum et de centraliser les logs dans un SIEM.

La **collecte** et le **parsing** avec EvtxECmd (Eric Zimmerman) sont la méthode de référence : `EvtxECmd.exe -f Security.evtx --csv output/ --csvf security_parsed.csv`. Le résultat est un CSV structuré analysable dans Timeline Explorer, avec chaque Event ID parsé en colonnes exploitables.

Des outils complémentaires accélèrent l'analyse. **Chainsaw** (WithSecure, open source) applique des règles Sigma sur les Event Logs pour détecter automatiquement les patterns d'attaque. **Hayabusa** (open source, japonais) offre une détection similaire basée sur Sigma avec un focus sur la vitesse. **LogParser** (Microsoft, gratuit) permet des requêtes SQL sur les fichiers evtx.

#### 14.2 Event IDs critiques pour le forensic — interprétation détaillée

Plutôt qu'une simple liste, chaque Event ID est expliqué avec son contexte, son contenu, son interprétation forensic, et ses faux positifs.

**4624 (Successful Logon) :** enregistre chaque authentification réussie avec le type de logon. Les types pertinents pour le forensic : Type 2 (Interactive — login physique ou RDP via console), Type 3 (Network — accès à un partage réseau, authentification WMI ou PsExec), Type 7 (Unlock — déverrouillage de session), Type 10 (RemoteInteractive — RDP). L'Event 4624 contient le nom du compte, le domaine, l'adresse IP source (pour les logons réseau), et le processus d'authentification (NTLM vs Kerberos). Un 4624 Type 3 depuis une IP inconnue avec un compte de service à 3h du matin est un indicateur de mouvement latéral.

**4625 (Failed Logon) :** enregistre les échecs d'authentification. Un volume élevé de 4625 avec des comptes variés depuis une même source indique un password spraying ou un brute force. Le sous-status code précise la raison de l'échec (0xC0000064 = compte inexistant, 0xC000006A = mot de passe incorrect, 0xC0000234 = compte verrouillé).

**4648 (Logon with Explicit Credentials) :** enregistre quand un processus s'authentifie avec des credentials différentes de celles de la session en cours (runas, PsExec avec `-u`, ou pass-the-hash). C'est un indicateur fort de mouvement latéral — l'attaquant utilise des credentials volées pour accéder à d'autres machines.

**4672 (Special Privileges Assigned) :** enregistre l'attribution de privilèges administratifs lors d'un logon. Un 4672 pour un compte utilisateur standard est suspect (l'utilisateur a obtenu des droits qu'il ne devrait pas avoir).

**4688 (Process Creation) :** enregistre la création d'un processus avec le nom de l'exécutable et, si la journalisation de la ligne de commande est activée (GPO `Process Creation → Include command line`), la ligne de commande complète. C'est l'Event ID le plus riche pour le forensic d'exécution — la ligne de commande révèle exactement ce que l'attaquant a tapé. Sans l'activation de cette GPO, le 4688 est beaucoup moins informatif.

**7045 (Service Installed) :** enregistre l'installation d'un nouveau service. PsExec crée un service PSEXESVC. Les malwares installent souvent des services pour la persistence. Un 7045 avec un nom de service inhabituel, un chemin d'exécutable dans un répertoire temporaire, ou un service Type 0x10 (own process) mérite investigation.

**4698 (Scheduled Task Created) :** enregistre la création d'une tâche planifiée. Les tâches planifiées sont un mécanisme de persistence courant. Le contenu de l'événement inclut le XML de la tâche — action exécutée, déclencheur, compte utilisé.

**4769 (Kerberos Service Ticket Requested) :** avec encryption type 0x17 (RC4), c'est la signature du Kerberoasting. Un volume élevé de 4769 avec encryption RC4 depuis une seule machine indique que l'attaquant demande des TGS pour craquer les mots de passe des comptes de service. Détail au Ch.20 (AD forensics).

**1102 (Security Log Cleared) :** enregistre l'effacement du Security Event Log — ironiquement, l'acte de nettoyage produit lui-même un événement. Un 1102 est un indicateur d'anti-forensics. Si les logs sont centralisés dans un SIEM, les événements antérieurs au clearing sont préservés.

**Sysmon Event IDs** (si Sysmon est déployé) : Event 1 (Process Creation — plus détaillé que 4688, avec hash du binaire, ligne de commande complète, processus parent), Event 3 (Network Connection — quel processus se connecte à quelle IP), Event 7 (Image Loaded — DLL chargées par un processus), Event 10 (Process Access — accès à LSASS), Event 11 (File Create — fichiers créés), Event 22 (DNS Query — résolutions DNS par processus). Sysmon transforme la visibilité forensic d'une machine Windows — son déploiement est la recommandation de forensic readiness la plus impactante.

#### 14.3 Corrélation des Event Logs entre machines

Reconstituer le mouvement latéral exige de corréler les Event Logs de plusieurs machines. Sur la machine source : 4648 (logon avec credentials explicites), Prefetch de l'outil de latéralisation (PsExec, wmic). Sur la machine destination : 4624 (logon réussi, type 3 ou 10), 7045 (service installé par PsExec), 4688 (processus créé). La corrélation repose sur les timestamps (les événements doivent être proches dans le temps), les comptes (le même compte apparaît sur les deux machines), et les IP (l'IP source du 4624 sur la destination correspond à l'IP de la machine source).

#### 14.4 Fil rouge — MUSIC BOX : les Event Logs racontent l'histoire

> **🔬 MUSIC BOX — Épisode 13**
>
> L'analyse des Event Logs de DC01 (parsés avec EvtxECmd + Chainsaw) révèle la séquence de la compromission AD.
>
> J-45 : série de 4769 (Kerberos TGS) avec encryption type RC4 depuis WKS-RD-047 pour 12 comptes de service — **Kerberoasting confirmé**. Le compte `svc-backup` avait un SPN et un mot de passe faible (`NovaPharma2024!`, cracké en 2h).
>
> J-30 : 4624 type 3 depuis WKS-RD-047 avec le compte `svc-backup` (domain admin) — première utilisation du compte compromis pour le mouvement latéral.
>
> J-14 : 4662 avec les GUID de réplication (`1131f6ad-...`) depuis WKS-RD-047 — **DCSync confirmé**. Tous les hashes NTLM sont compromis.
>
> J-1, 03h42 : **1102 — Security Log cleared** sur DC01. L'attaquant a effacé le Security Log. Mais les événements antérieurs au clearing sont préservés dans le SIEM Splunk de NovaPharma — l'anti-forensics a échoué grâce à la centralisation des logs.

---

### Chapitre 15 — Linux forensics

#### 15.1 Les particularités du forensic Linux

Linux est omniprésent en serveur (web, base de données, stockage, cloud) mais ses artefacts forensic sont moins riches et moins standardisés que ceux de Windows. Il n'y a pas d'équivalent du Prefetch, de l'Amcache, ou des ShellBags. L'investigation Linux repose davantage sur les logs système, les historiques de commandes, les tâches planifiées, et l'analyse du système de fichiers ext4.

#### 15.2 Artefacts système Linux

**auth.log / secure** (`/var/log/auth.log` sur Debian/Ubuntu, `/var/log/secure` sur RHEL/CentOS) : chaque authentification (login, sudo, SSH, su) est enregistrée. Les connexions SSH montrent l'IP source, le compte utilisé, et le résultat (accepté/refusé). Les commandes sudo montrent quelle commande a été exécutée par quel utilisateur.

**wtmp / btmp / lastlog** : fichiers binaires enregistrant les sessions utilisateur. `wtmp` contient les connexions réussies (lisible avec la commande `last`). `btmp` contient les tentatives échouées (lisible avec `lastb`). `lastlog` contient la dernière connexion de chaque utilisateur.

**bash_history / zsh_history** (`~/.bash_history`, `~/.zsh_history`) : historique des commandes exécutées. C'est souvent la source la plus directement exploitable — l'attaquant peut y avoir laissé ses commandes de reconnaissance, de mouvement latéral, et d'exfiltration. Le piège : l'attaquant supprime souvent son historique (`history -c`, `rm ~/.bash_history`), mais des traces peuvent persister en mémoire (dans le dump RAM), dans le swap, ou dans les secteurs non alloués du disque (le fichier supprimé peut être récupéré si le disque est un HDD).

**journald** (systemd) : le journal système de systemd, exploitable avec `journalctl`. Plus structuré que syslog, il inclut des métadonnées riches (PID, UID, unité systemd). Exportable en JSON pour l'analyse : `journalctl --since "2026-01-01" -o json > journal.json`.

**crontab et systemd timers** : les tâches planifiées sont un mécanisme de persistance courant sous Linux. Les crontab utilisateur (`crontab -l -u <user>`) et système (`/etc/crontab`, `/etc/cron.d/`) doivent être vérifiés. Les systemd timers (`.timer` + `.service` dans `/etc/systemd/system/`) sont une alternative plus moderne.

#### 15.3 Investigation serveur web et conteneurs

Les **logs Apache/Nginx** (`/var/log/apache2/access.log`, `/var/log/nginx/access.log`) sont essentiels pour l'investigation de compromission de serveur web. La détection de webshells (fichiers PHP/ASP déposés par l'attaquant pour maintenir un accès distant) passe par l'analyse des requêtes POST vers des fichiers inhabituels, l'identification de user-agents suspects, et la recherche de fichiers récemment créés dans les répertoires web.

Les **conteneurs Docker** posent des défis spécifiques : l'éphémérité des conteneurs (un conteneur détruit emporte ses données), la superposition des layers (le filesystem du conteneur est une superposition de couches en lecture seule + une couche en lecture/écriture), et l'absence de logs centralisés par défaut. L'investigation de conteneurs passe par l'examen des layers (`docker history`, `docker inspect`), des logs (`docker logs`), et des volumes montés. Sans logs externalisés vers un SIEM ou un système de log centralisé, le forensic de conteneurs est souvent impossible.

#### 15.4 Outils Linux forensics

**The Sleuth Kit / Autopsy** supporte ext4. **extundelete** et **ext4magic** permettent la récupération de fichiers supprimés sur ext4 (avec des limitations — ext4 réinitialise les pointeurs d'inode). **Plaso** (log2timeline) supporte les artefacts Linux (syslog, wtmp, bash_history, etc.). Les outils de la suite Eric Zimmerman ne sont pas disponibles nativement sous Linux (ils sont conçus pour les artefacts Windows), mais ils fonctionnent via Wine ou sur une station Windows.

#### 15.5 Fil rouge — MUSIC BOX : le serveur R&D Linux

> **🔬 MUSIC BOX — Épisode 14**
>
> L'investigation de SRV-RD-01 (Ubuntu 22.04, serveur de données R&D) révèle :
>
> **auth.log :** connexion SSH réussie depuis WKS-RD-047 (IP interne 10.xx.xx.47) avec le compte `svc-backup` à J-28, J-21, J-14, J-7, et J-1. Le compte `svc-backup` avait un authorized_key SSH ajouté par l'attaquant à J-30 — c'est le mécanisme de persistance sur le serveur Linux.
>
> **bash_history :** l'attaquant a exécuté `find /opt/research/molecule-np427 -name "*.xlsx" -o -name "*.pdf" -o -name "*.docx"` (reconnaissance des fichiers de recherche), puis `tar czf /tmp/research_backup.tar.gz /opt/research/molecule-np427/` (staging des données pour exfiltration), puis `rm -f /tmp/research_backup.tar.gz` (nettoyage après exfiltration — mais le fichier tar apparaît dans les secteurs non alloués du disque, récupérable par carving).
>
> **authorized_keys :** une clé SSH non autorisée a été ajoutée dans `/home/svc-backup/.ssh/authorized_keys` à J-30 — la clé publique est différente de celles des administrateurs légitimes. C'est le mécanisme de persistance.

---

### Chapitre 16 — macOS forensics

#### 16.1 Artefacts spécifiques macOS

macOS possède des artefacts forensic riches et spécifiques qui n'existent pas sur Windows ni Linux.

Le **Unified Logging** (introduit en macOS 10.12) est le système de journalisation le plus riche des OS modernes — il capture des milliards d'événements par jour (processus, réseau, système, applications). L'outil `log show` permet d'interroger les logs avec des filtres : `log show --predicate 'processImagePath contains "ssh"' --start "2026-01-01" --end "2026-03-08"`. L'outil `log collect` exporte les logs pour analyse offline.

Les **FSEvents** (File System Events, stockés dans `.fseventsd/` à la racine de chaque volume) enregistrent toutes les modifications du système de fichiers avec un identifiant d'événement séquentiel. Ils persistent même après suppression des fichiers — c'est l'équivalent fonctionnel du $UsnJrnl de Windows.

**KnowledgeC.db** (`~/Library/Application Support/Knowledge/KnowledgeC.db`) est une base SQLite qui enregistre l'activité utilisateur : applications ouvertes avec durée d'utilisation, activité réseau, période d'éveil de la machine, et interactions utilisateur. C'est une source forensic extrêmement riche, spécifique à macOS.

Les **Spotlight metadata** (index `.Spotlight-V100/`) contiennent les métadonnées de tous les fichiers indexés par Spotlight — même si les fichiers sont supprimés, les métadonnées peuvent persister dans l'index.

**TCC.db** (`~/Library/Application Support/com.apple.TCC/TCC.db`) enregistre les permissions d'accès aux ressources sensibles (caméra, microphone, fichiers, accessibilité). Un malware qui a obtenu l'accès à l'accessibilité ou au Full Disk Access sera visible dans TCC.db.

**LaunchAgents / LaunchDaemons** (`~/Library/LaunchAgents/`, `/Library/LaunchAgents/`, `/Library/LaunchDaemons/`) sont les mécanismes de persistance macOS — des fichiers plist qui définissent des programmes à exécuter automatiquement.

Outils macOS forensics : **mac_apt** (macOS Artifact Parsing Tool — open source, parse les artefacts spécifiques macOS), **APOLLO** (Apple Pattern of Life Lazy Output — parse KnowledgeC.db et d'autres bases de données d'activité), et **Unified Log Parser**.

---

### Chapitre 17 — Memory forensics

#### 17.1 Workflows d'analyse concrète avec Volatility 3

Au-delà de la liste des plugins (présentée au Ch.6 pour le dump et dans le cours original), ce chapitre se concentre sur les workflows d'analyse concrets — comment l'analyste utilise les plugins en séquence pour répondre aux questions investigatives.

**Workflow 1 — Triage initial (5 minutes) :** identifier rapidement si la machine est compromise. (1) `windows.pslist` / `windows.pstree` → examiner l'arbre des processus : les processus avec des parents anormaux (svchost.exe avec explorer.exe comme parent, cmd.exe avec iexplore.exe comme parent) sont suspects. (2) `windows.netscan` → identifier les connexions réseau actives vers des destinations suspectes (IP externes non connues, ports inhabituels). (3) `windows.cmdline` → examiner les lignes de commande des processus suspects. En 5 minutes, l'analyste sait si la machine est compromise et a identifié les premiers IoC (IP C2, processus malveillant).

**Workflow 2 — Investigation de process injection (30 minutes) :** quand un processus suspect est identifié. (1) `windows.malfind` → détecter les régions mémoire avec des permissions suspectes (PAGE_EXECUTE_READWRITE — RWX — est rare pour du code légitime et typique d'injection). Attention aux faux positifs : certains programmes légitimes (JIT compilers comme .NET CLR, navigateurs web) utilisent RWX légitimement. L'analyse doit être contextuelle. (2) `windows.dlllist --pid <PID>` → lister les DLL chargées par le processus suspect — identifier les DLL inhabituelles ou non signées. (3) `windows.handles --pid <PID>` → examiner les handles ouverts (fichiers, clés de registre, mutex — un mutex nommé peut identifier une famille de malware connue). (4) `windows.procdump --pid <PID> --dump-dir output/` → extraire le binaire du processus pour analyse malware.

**Workflow 3 — Extraction de credentials (15 minutes) :** (1) `windows.hashdump` → extraire les hashes NTLM des comptes locaux depuis SAM en mémoire. (2) `windows.lsadump` → extraire les secrets LSA (mots de passe de services, clés DPAPI). (3) Recherche de strings caractéristiques de mimikatz (`sekurlsa::logonPasswords`, `sekurlsa::wdigest`) dans le dump pour déterminer si l'attaquant a utilisé mimikatz. (4) Recherche de credentials en clair dans le processus lsass avec `windows.memmap --pid <lsass_pid> --dump-dir output/` puis strings et grep.

**Workflow 4 — Analyse de rootkit (avancé) :** `windows.modules` → lister les modules kernel chargés. `windows.ssdt` → vérifier la System Service Dispatch Table pour détecter les hooks. `windows.callbacks` → lister les callbacks enregistrés (un rootkit enregistre des callbacks pour intercepter les opérations système).

#### 17.2 Pagefile et hiberfil comme mémoire fossile

Quand le dump RAM n'a pas été fait à temps (la machine a été redémarrée avant l'intervention forensic), le **pagefile.sys** et le **hiberfil.sys** sont des sources de mémoire « fossile ». Le pagefile contient des pages mémoire qui ont été déplacées vers le disque — elles peuvent contenir des fragments de processus, des credentials, des URLs, et d'autres données. Le hiberfil est un dump mémoire compressé créé lors de l'hibernation — analysable avec Volatility.

Extraction des strings du pagefile : `strings -el pagefile.sys > pagefile_strings_unicode.txt` puis recherche de patterns (URLs, IP, chemins de fichiers suspects, noms de domaine). La recherche dans le pagefile est moins structurée que l'analyse d'un dump RAM complet (pas de structure de processus), mais elle peut révéler des données critiques quand le dump RAM est indisponible.

#### 17.3 YARA rules sur les dumps mémoire

Les règles YARA permettent de scanner le dump mémoire pour détecter des patterns caractéristiques de familles de malware connues. Le plugin `windows.yarascan` de Volatility exécute des règles YARA sur l'espace mémoire de chaque processus. Les sources de règles YARA : le repository `awesome-yara` sur GitHub, les règles publiées par les éditeurs CTI (Mandiant, CrowdStrike, ESET), et les règles custom créées à partir des IoC spécifiques à l'investigation.

#### 17.4 Fil rouge — MUSIC BOX : la mémoire raconte tout

> **🔬 MUSIC BOX — Épisode 15**
>
> Analyse du dump RAM de WKS-RD-047 (32 Go) avec Volatility 3.
>
> **Workflow triage :** `pstree` révèle le processus suspect : `svchost.exe` (PID 7284, PPID 3412 = explorer.exe). Un svchost légitime a toujours `services.exe` comme parent — celui-ci est enfant d'explorer.exe. C'est un process hollowing : le processus svchost a été créé normalement puis son code a été remplacé en mémoire par le RAT.
>
> **Workflow injection :** `malfind` détecte une section RWX dans l'espace mémoire de PID 7284 contenant du code exécutable — confirmation de l'injection. `netscan` montre que PID 7284 maintient une connexion ESTABLISHED vers `103.xx.xx.xx:443` — le C2. `procdump` extrait le payload injecté pour analyse malware (Ch.18).
>
> **Workflow credentials :** `hashdump` extrait les hashes NTLM de 12 comptes locaux. La recherche de strings dans le processus `lsass.exe` révèle des credentials en clair pour 8 comptes AD (l'attaquant a utilisé mimikatz — les credentials wdigest sont en mémoire). Le compte `svc-backup` (Domain Admin) est parmi eux — confirmation que le credential dumping a réussi.

---

### Chapitre 18 — Malware forensics

#### 18.1 Positionnement

Le malware forensics dans le contexte de ce cours n'est pas du reverse engineering complet (désassemblage, décompilation, analyse du code assembleur instruction par instruction). C'est de l'analyse comportementale orientée compréhension de l'intrusion : que fait le malware (fonctionnalités), avec qui communique-t-il (C2), quelles données a-t-il volées (exfiltration), comment survit-il au reboot (persistance), et comment le détecter sur d'autres machines (IoC).

#### 18.2 Analyse statique de premier niveau

L'analyse statique examine le malware sans l'exécuter. Le **hashing** (MD5, SHA-256) permet la soumission à VirusTotal, MalwareBazaar, ou Hybrid Analysis pour vérifier si le malware est connu. L'extraction de **strings** (`strings -el malware.exe > strings_output.txt`) révèle les chaînes de caractères embarquées : URLs de C2, chemins de fichiers, clés de registre, messages d'erreur, et parfois des identifiants de campagne. L'analyse de la structure **PE** (Portable Executable, format Windows) montre les imports (quelles API Windows le malware utilise — `VirtualAlloc`, `WriteProcessMemory`, `CreateRemoteThread` sont des indicateurs d'injection de processus), les sections (une section `.text` avec une entropie élevée > 7.0 suggère du packing ou du chiffrement), et les métadonnées (timestamp de compilation, éditeur de liens — le timestamp peut être falsifié mais fournit un indice). Le matching **YARA** compare l'échantillon à des règles connues pour identifier la famille.

L'analyse de **documents piégés** est une sous-spécialité de l'analyse statique. Les macros VBA dans les documents Office (Word, Excel) sont extraites et analysées avec **olevba** (oletools) sans exécuter le document. Les PDF malveillants sont analysés avec **pdf-parser** et **peepdf** (recherche de JavaScript, d'objets Flash, de liens vers des payloads). Les objets OLE embarqués dans les documents (exécutables déguisés en icônes de document) sont extraits avec **oletools**.

#### 18.3 Analyse dynamique en sandbox

L'analyse dynamique exécute le malware dans un environnement contrôlé pour observer son comportement réel. Les sandboxes en ligne (**ANY.RUN** avec interface interactive, **Joe Sandbox**, **CAPE/Cuckoo**) capturent les modifications système (fichiers créés, clés de registre modifiées, processus lancés, services installés), le trafic réseau (connexions C2, requêtes DNS, téléchargements), et les captures d'écran.

Les résultats de la sandbox sont interprétés dans le contexte de l'investigation : le C2 identifié (IP, domaine, port, protocole) est corrélé avec les logs réseau de l'organisation ; les artefacts de persistance identifiés (clé de registre, service, scheduled task) sont recherchés sur les autres machines du parc ; les IoC extraits (hash, domaines, mutex, user-agent) sont injectés dans le SIEM et l'EDR pour détecter d'autres machines compromises.

#### 18.4 Types de malware et implications forensic

Chaque type de malware pose des questions forensic différentes. Un **RAT** (Remote Access Trojan) fournit un accès distant persistant — la question est : depuis combien de temps est-il installé et quels accès ont été obtenus (keylogging, screenshot, file listing, credential dumping). Un **infostealer** (Lumma, RedLine, Vidar) exfiltre automatiquement des données spécifiques — la question est : quelles données ont été volées (credentials navigateur, cookies de session, wallets crypto, données de formulaires). Un **ransomware** chiffre les fichiers — la question est : quel périmètre a été chiffré, quelle clé a été utilisée (récupérable ?), et y a-t-il eu exfiltration avant chiffrement (double extorsion). Un **fileless malware** n'existe qu'en mémoire — la question est : le dump RAM a-t-il été fait ? (si non, le malware est potentiellement invisible au disk forensics).

#### 18.5 Extraction d'IoC et partage

Les IoC (Indicators of Compromise) sont les traces observables laissées par le malware, utilisables pour la détection sur d'autres machines et pour le partage avec la communauté. Ils incluent les hashes (SHA-256 du binaire), les domaines et IP C2, les mutex (verrous nommés — un mutex spécifique identifie souvent une famille de malware), les clés de registre modifiées, les fichiers créés (chemins, noms), les patterns réseau (beaconing interval, user-agent spécifique, JA3 hash), et les certificats TLS utilisés par le C2.

Les IoC sont partagés au format STIX/TAXII ou OpenIOC et injectés dans le SIEM et l'EDR pour scanner l'ensemble du parc. Le mapping sur la matrice MITRE ATT&CK (T1566.001 Spearphishing Attachment, T1059.001 PowerShell, T1055.012 Process Hollowing, etc.) structure les résultats pour le rapport et oriente les mesures défensives.

#### 18.6 Fil rouge — MUSIC BOX : le RAT custom

> **🔬 MUSIC BOX — Épisode 16**
>
> Le payload extrait du dump mémoire (procdump de PID 7284) est analysé.
>
> **Statique :** SHA-256 inconnu de VirusTotal — malware custom. `strings` : URL `https://103.xx.xx.xx/api/beacon`, user-agent `Mozilla/5.0 NovaPharma` (personnalisé), chemin `C:\Users\JMallet\AppData\Local\Temp\svchost_update.dat`. Structure PE : section .text avec entropie 7.2 (packé). YARA : correspondance partielle avec les signatures du groupe APT connu pour cibler l'industrie pharmaceutique européenne (cluster d'activité « PharmaGhost » selon Mandiant).
>
> **Dynamique (ANY.RUN) :** RAT custom, beacon HTTPS toutes les 30 minutes (confirmé par les logs proxy), capacités identifiées : file listing (`dir` recursif), file download, screenshot (toutes les 5 minutes), keylogger (capture des frappes clavier), credential dump (appel à `sekurlsa::logonPasswords` de mimikatz).
>
> **IoC extraits :** IP C2 `103.xx.xx.xx`, user-agent `Mozilla/5.0 NovaPharma`, mutex `Global\NP_RAT_2024`, fichier `svchost_update.dat`, clé registre `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\WindowsUpdate`. IoC injectés dans le SIEM et l'EDR → scan des 800 postes du parc. Résultat : aucune autre machine infectée.

---

## PARTIE V — INVESTIGATION RÉSEAU ET IDENTITÉ

*Partie dédiée aux investigations qui dépassent le périmètre d'un seul endpoint : l'analyse du trafic réseau, l'investigation de l'Active Directory, et l'investigation des identités hybrides et du cloud.*

---

### Chapitre 19 — Network forensics

#### 19.1 Ce que le réseau raconte

Le réseau est le terrain de jeu de l'attaquant pour la communication C2 (commandes envoyées au malware), le mouvement latéral (progression entre machines), et l'exfiltration (envoi des données volées vers l'extérieur). L'analyse réseau répond à des questions que le forensic endpoint seul ne peut pas couvrir : avec qui la machine compromise communique-t-elle ? quel volume de données a été transféré ? quels autres systèmes ont été contactés ?

#### 19.2 Analyse PCAP avec Wireshark

Wireshark est l'outil de référence pour l'analyse de captures de paquets. Les filtres les plus utiles pour le forensic : `ip.addr == 103.xx.xx.xx` (isoler le trafic vers/depuis le C2), `http.request.method == POST` (identifier les données envoyées en HTTP — potentielle exfiltration), `dns.qry.name contains "suspect"` (résolutions DNS suspectes), `tcp.flags.syn == 1 && tcp.flags.ack == 0` (nouvelles connexions TCP — identifier les scans), et `tls.handshake.type == 1` (Client Hello — pour l'analyse JA3). La reconstruction de sessions TCP (`Follow TCP Stream`) permet de lire le contenu des communications non chiffrées. L'extraction de fichiers (`File > Export Objects > HTTP/SMB/...`) récupère les fichiers transférés via le réseau.

#### 19.3 Détection de C2 et beaconing

Le beaconing est le pattern de communication le plus courant des malwares C2 : le malware contacte le serveur de l'attaquant à intervalles réguliers pour recevoir des instructions. La détection repose sur l'analyse statistique des intervalles de connexion : un processus qui contacte la même IP toutes les 30 minutes (± un jitter de 10 %) pendant 60 jours n'est pas un comportement humain — c'est un automate. L'outil **RITA** (Real Intelligence Threat Analytics, open source) automatise la détection de beaconing dans les logs Zeek. Les **fingerprints JA3/JA4** (hash de la négociation TLS Client Hello) identifient des clients TLS spécifiques même sur du trafic chiffré — le JA3 d'un RAT custom est différent de celui d'un navigateur Chrome.

#### 19.4 Reconstruction de l'exfiltration

L'estimation du volume exfiltré est une question à laquelle le network forensics doit répondre. L'analyse des logs proxy (user-agent `rclone/v1.65.0`, volume cumulé vers des endpoints S3), des NetFlow (volume de données sortantes par destination), et des PCAP (si disponibles — extraction des fichiers transférés) permet de quantifier l'exfiltration. Le DNS tunneling est une technique d'exfiltration plus discrète — les données sont encodées dans les sous-domaines des requêtes DNS (`encoded-data.c2-domain.com`). La détection repose sur la longueur anormale des requêtes, l'entropie élevée des sous-domaines, et le volume de requêtes vers un même domaine.

#### 19.5 Outils complémentaires

**Zeek** (ex-Bro) produit des logs structurés à partir du trafic réseau — conn.log (connexions), dns.log (requêtes DNS), http.log (requêtes HTTP), ssl.log (certificats TLS), files.log (fichiers transférés). Ces logs sont beaucoup plus faciles à analyser à grande échelle que les PCAP bruts. **NetworkMiner** (open source) extrait automatiquement les fichiers, les images, et les metadata des captures réseau. **Arkime** (ex-Moloch) est une plateforme de capture et d'analyse réseau à grande échelle, avec indexation full-text et interface web.

---

### Chapitre 20 — Active Directory forensics

#### 20.1 Pourquoi un chapitre dédié à l'AD

Dans 95 % des compromissions Windows, l'objectif stratégique de l'attaquant est le contrôle de l'Active Directory. L'AD gère l'authentification de tous les utilisateurs, les autorisations sur toutes les ressources, le déploiement de logiciel via GPO, et les secrets (hashes NTLM, clés Kerberos). Le forensic AD est donc une composante centrale de presque toute investigation Windows — et pourtant, il est rarement traité comme une discipline à part entière.

Ce chapitre couvre l'investigation AD sous l'angle forensic : quels artefacts analyser, quelles attaques détecter, et comment reconstituer la chronologie de la compromission AD. Il complète le Ch.14 (Event Logs) en se focalisant sur les artefacts spécifiques à l'AD, et le Ch.20 du cours IR (investigation identité) en allant plus en profondeur sur la technique.

#### 20.2 Investigation des authentifications

Les Event Logs des DC sont la source primaire. Les patterns à rechercher : authentifications depuis des IP inhabituelles (le compte `svc-backup` se connecte habituellement depuis le serveur de sauvegarde — une connexion depuis un poste de travail est suspecte), authentifications à des heures inhabituelles (un admin qui se connecte à 3h du matin un dimanche), volume anormal d'échecs d'authentification depuis une même source (password spraying), et authentifications avec des comptes de service utilisés manuellement (les comptes de service ne devraient jamais être utilisés interactivement).

L'**ADTimeline** (outil de l'ANSSI) produit une timeline des modifications AD à partir des métadonnées de réplication — c'est l'outil de référence pour comprendre chronologiquement ce que l'attaquant a fait dans l'AD. Il parse les métadonnées de réplication (attributs `whenChanged`, `whenCreated`, `msDS-ReplAttributeMetaData`) pour reconstruire la séquence des modifications sans dépendre des Event Logs (qui peuvent avoir été effacés).

#### 20.3 Investigation Kerberos

**Kerberoasting :** l'attaquant demande des TGS (Ticket Granting Service) pour des comptes de service ayant un SPN (Service Principal Name), puis cracke les tickets offline pour obtenir le mot de passe en clair. Détection forensic : Event ID 4769 avec encryption type 0x17 (RC4) en volume anormal depuis une seule machine. Interprétation : si un seul poste demande des TGS RC4 pour 10+ comptes de service en quelques minutes, c'est du Kerberoasting. L'attaquant a obtenu les tickets et les cracke offline — il n'y aura pas d'autre trace visible tant que le mot de passe n'est pas cracké et utilisé.

**DCSync :** l'attaquant simule un DC pour demander la réplication des hashes NTLM de tous les comptes. Détection forensic : Event ID 4662 avec les GUID de réplication (`1131f6ad-9c07-11d1-f79f-00c04fc2dcd2` pour DS-Replication-Get-Changes, `1131f6aa-...` pour DS-Replication-Get-Changes-All) provenant d'une machine qui n'est PAS un DC. C'est la preuve formelle que l'attaquant a récupéré tous les hashes — y compris le krbtgt.

**Golden Ticket :** l'attaquant forge un TGT avec le hash du krbtgt. Détection forensic : anomalies dans les tickets Kerberos — lifetime anormalement long (le Golden Ticket a souvent un lifetime de 10 ans alors que la politique du domaine est de 10 heures), SID qui ne correspond pas à un utilisateur existant, ou TGT sans événement de pré-authentification (4768) correspondant. La détection est difficile — c'est pourquoi la prévention (mots de passe krbtgt complexes, rotation régulière) est critique.

#### 20.4 Investigation des modifications AD

Les modifications d'objets AD (comptes créés, groupes modifiés, GPO ajoutées, ACL modifiées) sont enregistrées dans les Event Logs (Event ID 5136 pour les modifications d'attribut via LDAP, Event IDs 4720/4728/4732 pour la gestion des comptes et groupes) et dans les métadonnées de réplication (parsables par ADTimeline).

L'analyse du fichier **ntds.dit** (la base de données AD, stockée sur les DC dans `C:\Windows\NTDS\`) avec **secretsdump.py** (Impacket) ou **DSInternals** (PowerShell) permet d'extraire les hashes NTLM de tous les comptes, de vérifier les mots de passe (comparaison avec des dictionnaires pour identifier les mots de passe faibles que l'attaquant a pu craquer), et d'auditer les comptes (date de création, date de dernière connexion, membership des groupes).

**BloodHound** (en mode défensif) peut être utilisé pour visualiser les chemins d'attaque que l'attaquant a pu emprunter : quels comptes avaient des droits sur quels systèmes, quels chemins menaient au Domain Admin, quelles ACL permettaient l'élévation de privilèges. C'est un outil offensif (utilisé par les pentesters et les attaquants pour la reconnaissance) qui est aussi un outil défensif puissant pour comprendre comment la compromission a été possible.

#### 20.5 Fil rouge — MUSIC BOX : la compromission AD

> **🔬 MUSIC BOX — Épisode 17**
>
> L'investigation AD révèle la séquence complète :
>
> **ADTimeline :** 3 modifications critiques identifiées. (1) J-30 : création du compte `svc-monitor-temp` (ajouté au groupe Domain Admins). (2) J-14 : modification de l'attribut `msDS-AllowedToDelegateTo` sur le compte `svc-backup` — délégation Kerberos contrainte ajoutée, permettant l'impersonation d'administrateurs. (3) J-7 : création d'une GPO « Application Update Policy » dans une OU peu surveillée — contenu : script PowerShell de staging de données.
>
> **ntds.dit (secretsdump.py) :** extraction des hashes de tous les comptes. Comparaison avec la base Have I Been Pwned et un dictionnaire de mots de passe : 23 comptes ont des mots de passe faibles (< 12 caractères, mots du dictionnaire). Le compte `svc-backup` avait le mot de passe `NovaPharma2024!` — cracable en 2 heures avec un GPU moderne.

---

### Chapitre 21 — Investigation des identités hybrides, du cloud et des accès distants

*Ce chapitre traite l'investigation au-delà du périmètre AD classique : les environnements hybrides (AD sync avec Entra ID), les services cloud (M365, AWS), et les accès distants (VPN). Il est conçu comme un chapitre de synthèse orienté identité — la question transversale étant : comment l'attaquant a-t-il pivoté entre l'on-premise et le cloud ?*

#### 21.1 Investigation des accès VPN

Les logs VPN sont une source critique pour identifier l'accès initial et le mouvement latéral inter-sites. Les indicateurs de compromission dans les logs VPN : connexions depuis des IP géographiquement incohérentes avec l'utilisateur (geo-impossible travel — le même utilisateur se connecte depuis Paris et depuis Hong Kong à 1 heure d'intervalle), connexions en dehors des horaires habituels, et utilisation de comptes rarement actifs (le compte `admin_rh_ext` du sous-traitant GestPaie dans le cours IR, le compte `svc-backup` dans MUSIC BOX).

#### 21.2 Investigation Microsoft 365 et Entra ID

Le **Unified Audit Log** (UAL) est la source centrale pour l'investigation M365. Les événements les plus pertinents : `UserLoggedIn` (connexions — corréler avec le Sign-in Log pour la géolocalisation et le device info), `New-InboxRule` et `Set-InboxRule` (règles de forwarding — technique BEC classique), `FileDownloaded` et `FileAccessed` (accès aux fichiers SharePoint/OneDrive), `Add application` et `Consent to application` (app registrations OAuth — technique de persistance cloud), et `Update StsRefreshTokenValidFrom` (révocation de token — une révocation non initiée par l'IT est suspecte).

Les **Sign-in Logs** d'Entra ID fournissent des détails sur chaque authentification : IP, géolocalisation, device info, résultat de la conditional access policy, et méthode MFA utilisée. L'absence de MFA (quand la politique devrait l'exiger) ou un MFA bypass (utilisation d'un token volé) sont des indicateurs critiques.

Quand l'AD on-premise est synchronisé avec Entra ID via **Azure AD Connect**, la compromission se propage : l'attaquant qui a le hash NTLM d'un compte on-premise peut l'utiliser pour accéder aux ressources cloud synchronisées. L'investigation doit couvrir les deux environnements.

#### 21.3 Investigation AWS

Les sources forensic AWS incluent **CloudTrail** (chaque appel API est enregistré : `GetObject` sur S3, `RunInstances` pour les EC2, `CreateUser` pour IAM — avec l'IP source, l'identité appelante, et le timestamp), les **VPC Flow Logs** (métadonnées réseau — source, destination, port, volume, accept/reject), les **S3 Access Logs** (accès aux buckets — qui a accédé à quel objet, quand), et les **EBS Snapshots** (pour la préservation de l'état d'un volume sans arrêter l'instance).

L'investigation AWS se concentre sur les questions d'identité : quel utilisateur IAM ou quel rôle a été utilisé ? depuis quelle IP ? les access keys sont-elles les mêmes que celles présentes sur un serveur compromis ? (corrélation on-premise → cloud). La rétention par défaut de CloudTrail est de 90 jours — au-delà, il faut un trail configuré vers S3 ou CloudWatch.

#### 21.4 Fil rouge — MUSIC BOX : le pivot vers le cloud

> **🔬 MUSIC BOX — Épisode 18**
>
> L'investigation cloud confirme l'exfiltration. CloudTrail montre 347 appels `GetObject` sur le bucket `projets-molecule-np427` en 5 jours, depuis le rôle IAM `svc-backup-role` mais avec des access keys (`AKIA...`) qui correspondent à celles trouvées dans le fichier `~/.aws/credentials` du serveur Linux SRV-RD-01. L'attaquant a exfiltré les données R&D via le serveur Linux compromis, en utilisant les credentials AWS stockées sur le serveur.
>
> M365 : le UAL montre une connexion au compte `j.mallet@novapharma.com` depuis l'IP C2 `103.xx.xx.xx` à J-20 (token volé via le credential dump de mimikatz). L'attaquant a accédé à 15 emails contenant des informations sur la stratégie de brevet de NovaPharma pour la molécule NP-427. Aucune règle de forwarding n'a été créée — l'accès était ponctuel et ciblé.

---

## PARTIE VI — FORENSIC SPÉCIALISÉ

---

### Chapitre 22 — Email forensics et messagerie

L'email est le vecteur d'intrusion initiale le plus courant (phishing, spearphishing). L'analyse des en-têtes complets (champs `Received` lus de bas en haut pour tracer le chemin de l'email), la vérification SPF/DKIM/DMARC (le domaine d'envoi est-il légitime ?), l'extraction de la pièce jointe pour analyse malware (Ch.18), et l'identification du domaine d'usurpation (typosquatting, homoglyphes) constituent le workflow standard.

Les formats de boîtes mail (PST pour Outlook, MBOX, EML), les outils d'extraction (pffexport, Kernel PST Viewer, Autopsy module email), et l'indexation full-text pour la recherche dans des boîtes de dizaines de milliers d'emails sont détaillés.

La messagerie instantanée (Teams, Slack, Signal, WhatsApp) devient une source forensic croissante. Teams stocke des bases SQLite locales et des logs Azure. Slack est exportable via l'API workspace. Signal et WhatsApp utilisent des bases SQLite chiffrées sur le terminal mobile — l'accès nécessite l'acquisition du terminal (Ch.23).

#### 22.1 Fil rouge — MUSIC BOX : l'email de spearphishing

> **🔬 MUSIC BOX — Épisode 19**
>
> L'email de spearphishing est retrouvé dans la boîte PST du Dr. Mallet. Headers : envoyé depuis un serveur compromis en Europe de l'Est (IP dans les Received). Domaine : `novapharma-partners.com` (typosquatting du domaine légitime `novapharma-partner.com`). SPF : pass (le domaine de typosquatting avait un SPF configuré — l'attaquant a préparé son infrastructure). Pièce jointe : `Rapport_collaboration_Q3.docx`. Analyse olevba : macro VBA obfusquée qui télécharge le RAT depuis un site WordPress compromis via certutil. Le vecteur initial est formellement identifié et documenté.

---

### Chapitre 23 — Mobile forensics

Le smartphone est un terminal d'une richesse informationnelle exceptionnelle : appels, SMS, emails, localisation GPS continue, photos géolocalisées, applications de messagerie, historique de navigation, credentials stockés. Mais les protections modernes (chiffrement intégral, Secure Enclave/TEE, verrouillage biométrique) rendent l'acquisition complexe.

**iOS forensics :** trois niveaux d'acquisition (logique via backup iTunes/libimobiledevice, filesystem via exploitation de vulnérabilités comme checkm8, physique — de plus en plus rare sur les modèles récents). La distinction AFU (After First Unlock — clés en mémoire, extraction possible) vs BFU (Before First Unlock — clés protégées, accès très limité) est fondamentale. Les données iCloud (backups, photos, messages) sont accessibles via les credentials ou par réquisition Apple.

**Android forensics :** plus de flexibilité d'accès. ADB (si activé), JTAG, chip-off (invasif), mode EDL (Qualcomm). Les bases SQLite contiennent l'essentiel des données applicatives.

**Outils :** Cellebrite UFED (référence forces de l'ordre), Magnet AXIOM, ALEAPP/iLEAPP (open source pour le parsing des artefacts). **Artefacts clés :** SMS/appels, bases de données messagerie (WhatsApp `msgstore.db`, Signal `signal.db`, Telegram `cache4.db`), photos EXIF (géolocalisation), historique de localisation, WiFi SSIDs connectés.

---

### Chapitre 24 — Anti-forensics : comprendre et détecter

L'anti-forensics regroupe les techniques de l'attaquant pour empêcher, ralentir ou tromper l'investigation. C'est un jeu du chat et de la souris : chaque technique anti-forensic a des contremesures, et les traces de l'anti-forensics elle-même sont souvent révélatrices.

**Destruction de données :** wiping sécurisé (SDelete, shred, DBAN), TRIM automatique sur SSD, destruction physique. Contremesure : le $UsnJrnl conserve la trace des fichiers supprimés, les traces de SDelete sont visibles dans la MFT (fichiers temporaires caractéristiques créés par l'outil).

**Dissimulation :** chiffrement (volumes VeraCrypt), stéganographie, ADS NTFS, rootkits. Contremesure : les ADS sont détectables avec `dir /r` ou les outils forensic, les rootkits sont détectables par l'analyse mémoire (Volatility malfind, modscan).

**Falsification :** timestomping (modification des timestamps $SI — détectable par comparaison avec $FN), falsification de logs (modification ou suppression sélective — détectable par les lacunes dans les séquences d'Event ID et par les logs centralisés dans le SIEM), planted evidence (fausses preuves — détectable par les incohérences dans la timeline).

**Évasion :** fileless malware (invisible au disk forensics — détectable uniquement par memory forensics), LOLBins (utilisation de binaires légitimes — certutil, PowerShell, bitsadmin — détectable par les Event Logs PowerShell et Sysmon), script-based attacks (détectables uniquement si le script block logging est activé).

**Détection de l'anti-forensics :** l'anti-forensics parfait est rare. L'Event ID 1102 (Security Log cleared) trahit le nettoyage de logs. Les incohérences de timestamps ($SI vs $FN) trahissent le timestomping. Le pagefile.sys et le hiberfil.sys conservent des fragments de mémoire anciens. Et les logs centralisés dans un SIEM préservent les événements même quand l'attaquant efface les logs locaux.

#### 24.1 Fil rouge — MUSIC BOX : l'anti-forensics détecté

> **🔬 MUSIC BOX — Épisode 20**
>
> L'attaquant a tenté de couvrir ses traces. **Timestomping détecté :** les timestamps $SI de 47 fichiers dans `/projets/molecule-np427/` montrent des dates de création en 2022, mais les timestamps $FN indiquent 2024 (détecté via MFTECmd). **Log clearing :** Event ID 1102 détecté sur DC01 à J-1, 03h42 — le Security Log a été effacé. Mais les événements antérieurs étaient centralisés dans le SIEM Splunk — l'anti-forensics a échoué. **Suppression de fichiers :** 47 fichiers supprimés dans le répertoire de recherche — mais le $UsnJrnl conserve les noms, dates, et comptes associés aux suppressions.

---

### Chapitre 25 — Investigation des mécanismes de persistance

Ce chapitre est une référence transversale : l'éradication post-incident (cours IR, Ch.27) nécessite d'avoir identifié TOUS les mécanismes de persistance de l'attaquant. Le forensicien doit savoir les trouver.

**Persistance Windows — registre :** Run/RunOnce, Winlogon (Userinit, Shell), Image File Execution Options (Debugger), AppInit_DLLs, et les clés de registre de services (voir Ch.12 pour le détail). **Persistance Windows — système :** Scheduled Tasks (Event ID 4698, fichiers XML dans `C:\Windows\System32\Tasks\`), services Windows (Event ID 7045, clé registre `HKLM\SYSTEM\CurrentControlSet\Services`), WMI Event Subscriptions (persistance via des événements WMI — très discrète, détectable via `Get-WMIObject -Namespace root\Subscription -Class __EventConsumer`), DLL hijacking (une DLL malveillante est placée dans un répertoire prioritaire du DLL search order), COM object hijacking (redirection d'un objet COM légitime vers un exécutable malveillant), et Startup folder (`C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\`).

**Persistance Linux :** crontab (utilisateur et système), systemd timers, scripts dans `/etc/init.d/`, modification de `.bashrc`/`.profile` (exécution de code au login), SSH authorized_keys (ajout de clé non autorisée — le mécanisme le plus courant), modules noyau malveillants (chargés via insmod), et LD_PRELOAD (injection de bibliothèque partagée).

**Persistance cloud :** app registrations avec secrets (OAuth tokens persistants qui survivent au reset du mot de passe), service principals avec des permissions excessives, et IAM users/roles avec des access keys — tous survivent aux resets de mots de passe des comptes utilisateur classiques.

Pour chaque mécanisme : comment l'attaquant l'installe, comment le forensicien le détecte, quels artefacts il laisse (Event Logs, registre, système de fichiers), et comment l'éradiquer. L'outil **Autoruns** (Sysinternals) et les hunts Velociraptor sont les méthodes les plus complètes pour inventorier les points de persistance sur une machine Windows.

---

## PARTIE VII — FINALISATION ET PRODUCTION

---

### Chapitre 26 — Rapport forensic et expertise judiciaire

#### 26.1 Le rapport comme produit final

Le rapport forensic transforme des centaines d'heures d'analyse technique en conclusions compréhensibles et défendables. C'est le document qui sera lu par le juge, le COMEX, l'assureur, ou le conseil d'administration. Le piège le plus fréquent : écrire un rapport technique brillant que seul un autre analyste forensic peut comprendre.

**Structure type du rapport forensic :**

**Résumé exécutif** (1-2 pages maximum) : résumé non technique des conclusions principales, de l'impact, et des recommandations. C'est souvent la seule section lue par les décideurs — elle doit être autonome et compréhensible.

**Cadre de l'investigation** : mandat (qui a demandé l'investigation, dans quel contexte), périmètre (quels systèmes, quelle période), questions investigatives, et méthodologie utilisée (outils, versions, paramètres — pour la reproductibilité et le contradictoire).

**Faits constatés** : chaque constatation est présentée factuellement, avec sa source (Event Log, artefact, capture réseau), sa date, et son niveau de confiance. La distinction fait/déduction/hypothèse (Ch.11) est explicite à chaque étape. Mauvais exemple : « L'attaquant a volé les données. » Bon exemple : « Le fichier `rclone.exe` a été exécuté sur WKS-RD-047 le 2 mars 2026 à 14h32 UTC (source : Prefetch, confirmé par Amcache — fait vérifié). Les logs proxy montrent des flux HTTPS vers des endpoints AWS S3 totalisant 183 Go depuis cette machine entre le 2 et le 7 mars (source : logs Squid — fait vérifié). Ces éléments indiquent une exfiltration de données de ce volume vers l'infrastructure AWS (déduction logique). »

**Analyse et interprétation** : reconstitution de la timeline complète, mapping ATT&CK, hypothèses concurrentes testées, et conclusions avec niveaux de confiance.

**Recommandations** : mesures correctives (éradication, durcissement, prévention), recommandations pour la procédure judiciaire (éléments de preuve exploitables, réquisitions complémentaires suggérées), et recommandations pour le forensic readiness.

**Annexes techniques** : IoC complets, timeline détaillée, captures d'écran, hash des preuves, et chaîne de custody.

#### 26.2 Écrire pour un juge

Le rapport judiciaire doit être compréhensible par un non-technicien. Les termes techniques sont définis quand ils sont utilisés pour la première fois. Les captures d'écran illustrent les constatations. Le raisonnement est explicite (« J'en déduis que... parce que... »). Les conclusions ne dépassent pas les constatations — l'expert donne un avis technique, pas un verdict.

Le témoignage d'expert (à la barre ou en audience) exige de vulgariser sans simplifier. L'expert doit être capable d'expliquer un timestamp NTFS à un procureur, une injection de processus à un avocat, et une chaîne de custody à un jury — en langage clair, sans condescendance, et en répondant aux questions du contre-interrogatoire avec rigueur.

#### 26.3 Le rapport de triage DFIR

Le rapport de triage est plus court (5-10 pages), orienté action et IoC, destiné au SOC et à l'équipe IR. Il contient les IoC (hash, domaines, IP, artefacts de persistance — immédiatement injectables dans le SIEM/EDR), les TTP observées (mapping ATT&CK — pour orienter le confinement et la remédiation), le périmètre de compromission connu (quelles machines, quels comptes), et les recommandations immédiates (quoi isoler, quoi reseter, quoi surveiller).

---

### Chapitre 27 — Forensic readiness : préparer l'organisation

Le forensic readiness est la capacité de l'organisation à mener une investigation forensic efficace quand un incident survient. C'est l'investissement préventif le plus rentable en forensic.

Les composantes : politique de rétention des logs (quelle durée, quelles sources, quel stockage — minimum 6 mois chaud, 12 mois froid), activation des sources critiques (PowerShell script block logging — Event ID 4104, Sysmon, audit AD étendu, processus creation avec ligne de commande — Event ID 4688 avec GPO), déploiement d'outils pré-positionnés (KAPE/Velociraptor/DumpIt sur clé USB sécurisée, accessible en urgence), protection de l'intégrité des logs (centralisation SIEM, stockage WORM — les logs locaux peuvent être effacés par l'attaquant), documentation de l'architecture SI (schéma réseau à jour, inventaire des serveurs et services, listes des comptes à privilèges, documentation des GPO), et formation des équipes (les IT doivent connaître les premiers réflexes : ne pas éteindre, ne pas nettoyer, appeler l'IR lead).

Sysmon est la recommandation de forensic readiness la plus impactante : son déploiement (gratuit, léger, configurable via XML) transforme la visibilité forensic d'une machine Windows en fournissant des Event IDs riches (processus avec hash et parenté, connexions réseau par processus, modifications de registre, chargement de DLL, accès à LSASS).

---

### Chapitre 28 — Forensic et incident response : intégration opérationnelle

Ce chapitre articule le forensic avec le processus IR détaillé dans le cours Incident Response de la bibliothèque. Le forensic s'intègre dans l'IR à trois niveaux : il alimente les décisions de confinement (quels systèmes isoler, quels comptes désactiver — basé sur l'étendue de la compromission révélée par l'investigation), il produit les IoC pour la détection à l'échelle du parc (les hash, domaines C2, et artefacts de persistance identifiés sont injectés dans le SIEM/EDR pour scanner toutes les machines), et il alimente le rapport final et le RETEX (la timeline complète, le mapping ATT&CK, et les causes racines identifiées par le forensic structurent le RETEX de l'incident).

---

### Chapitre 29 — Forensic automation et scripting

#### 29.1 Pourquoi l'automatisation est devenue indispensable

La réalité du forensic opérationnel en 2025-2026 : les volumes de données sont massifs (des téraoctets d'images disque, des millions d'événements dans les logs), les parcs à investiguer sont étendus (vérifier 800 postes pour la présence d'un IoC), et les délais sont serrés. L'analyste qui fait tout manuellement est submergé. L'automatisation ne remplace pas le raisonnement analytique (Ch.11) — elle libère du temps pour le raisonnement en automatisant les tâches répétitives.

#### 29.2 Python pour le forensic

Python est le langage de scripting dominant en forensic. Les librairies essentielles : **python-evtx** (parsing des Event Logs Windows), **python-registry** (parsing du registre Windows), **pefile** (analyse de binaires PE), **yara-python** (matching de règles YARA), **volatility3** comme librairie Python (analyse de dumps mémoire programmable), **pandas** (manipulation de données tabulaires — essentiel pour travailler avec les CSV produits par les outils Zimmerman), et **sqlite3** (accès aux bases de données SQLite des navigateurs, de Teams, de WhatsApp, etc.).

Exemple concret : un script Python qui parse le Prefetch de 800 postes collectés par Velociraptor, filtre les exécutions de `rclone.exe`, `psexec.exe`, et `mimikatz.exe`, et produit un CSV des machines sur lesquelles ces outils ont été exécutés — en 30 secondes au lieu de 30 heures d'analyse manuelle.

#### 29.3 PowerShell pour la collecte et l'analyse Windows

PowerShell est l'outil natif pour la collecte et l'analyse sur Windows. `Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624}` interroge les Event Logs. `Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'` lit les clés de registre. PowerShell Remoting (`Invoke-Command -ComputerName`) permet la collecte à distance sur un parc entier.

#### 29.4 Velociraptor VQL et KAPE custom

**Velociraptor** utilise le VQL (Velociraptor Query Language) pour définir des collectes et des hunts personnalisées. Un hunt Velociraptor peut scanner 1 000 machines en quelques minutes pour la présence d'un IoC spécifique (hash de fichier, nom de processus, clé de registre). **KAPE** permet la création de targets et modules custom — l'analyste peut définir exactement quels artefacts collecter et comment les parser, adapté à son environnement.

---

## PARTIE VIII — APPLICATION ET SYNTHÈSE

*Cette partie est un atelier de synthèse : 4 cas complets qui appliquent l'intégralité de la méthodologie forensic sur des types d'incidents distincts. Chaque cas suit le processus complet : identification → préservation → acquisition → analyse → rapport.*

---

### Chapitre 30 — Cas complet : compromission Windows avec mouvement latéral et exfiltration

Synthèse du fil rouge MUSIC BOX sous forme de cas autonome. Du spearphishing initial (J-60) au rapport final, en passant par le dump RAM, le triage KAPE, l'image disque, l'analyse mémoire (process hollowing, credentials en mémoire), l'analyse des artefacts d'exécution (Prefetch, Amcache, SRUM confirmant l'exfiltration), la détection du mouvement latéral (PsExec traces, RDP traces, SSH vers le serveur Linux), l'investigation AD (Kerberoasting, DCSync), la détection de l'anti-forensics (timestomping, log clearing), et la production du rapport pour le juge et le COMEX. La timeline unifiée de 60 jours est le livrable central.

### Chapitre 31 — Cas complet : investigation insider threat

Un chercheur senior de NovaPharma annonce son départ pour un concurrent. Trois semaines après son départ, un audit DLP révèle : 45 Go de documentation de recherche copiée sur une clé USB personnelle dans les 10 jours précédant le départ, et un upload de 12 Go vers un compte Google Drive personnel depuis le réseau d'entreprise.

L'investigation forensic du poste (Windows 11) utilise les artefacts USB (registre USBSTOR, SetupAPI logs — identification du modèle et du numéro de série de la clé USB, dates de connexion), les ShellBags (navigation dans les dossiers de recherche confidentielle), les LNK files (fichiers ouverts depuis la clé USB), le navigateur Chrome (historique de connexion à Google Drive, volumes uploadés — confirmés par les logs proxy), et le SRUM (confirmation du volume de données transférées par Chrome vers Google Drive).

Spécificités de l'investigation insider : droit du travail (la charte informatique autorise-t-elle l'usage personnel de clés USB ?), RGPD (les données copiées contiennent-elles des données personnelles de patients d'essais cliniques ?), et procédure disciplinaire/pénale (les preuves doivent être exploitables devant les prud'hommes ET potentiellement devant le tribunal correctionnel pour vol de secrets de fabrication — article L.1227-1 du Code du travail). Le rapport est rédigé en deux versions : une pour le DRH (procédure disciplinaire) et une pour l'avocat (procédure pénale).

### Chapitre 32 — Cas complet : investigation serveur Linux compromis

Un serveur web exposé sur Internet (Ubuntu 22.04, Apache, application PHP interne) est compromis via une vulnérabilité d'injection SQL dans l'application. L'attaquant a obtenu un shell via un webshell PHP, escaladé ses privilèges via un exploit kernel local, et déployé un cryptominer.

L'investigation Linux : logs Apache (identification de la requête d'injection SQL initiale, accès au webshell), auth.log (tentatives de su, sudo, escalade de privilèges), bash_history (commandes de l'attaquant — reconnaissance, téléchargement du cryptominer, installation du crontab de persistance), crontab (le cryptominer est relancé toutes les 5 minutes), analyse du webshell PHP (code obfusqué, capacités de commande), et analyse du binaire cryptominer (IoC, pool de mining, wallet — pour estimer les revenus de l'attaquant).

Spécificités : pas d'EDR sur le serveur (l'investigation repose entièrement sur les logs système et les artefacts du système de fichiers), logs limités (auth.log rotaîne à 4 fichiers, les logs les plus anciens sont perdus), et reconstruction à partir d'artefacts fragiles (l'attaquant a supprimé son bash_history, mais des fragments sont récupérés dans le swap par recherche de strings).

### Chapitre 33 — Cas complet : compromission AD et identités hybrides cloud

Un groupe hospitalier français (3 sites, 2 000 utilisateurs, AD synchronisé avec Microsoft 365 E3 via Azure AD Connect) est victime d'une compromission qui commence par un phishing sur M365 (token volé via un kit AitM — Adversary-in-the-Middle), pivot vers l'AD on-premise (l'attaquant utilise le token pour accéder à Azure AD Connect et obtenir les credentials de synchronisation), puis Golden Ticket sur l'AD on-premise (DCSync → forge de TGT), et enfin accès aux données de santé des patients via l'application métier hospitalière.

L'investigation combine forensic cloud (UAL M365 — identification du phishing initial et du token volé, Sign-in Logs — détection du MFA bypass par le kit AitM), forensic AD (Event Logs DC — DCSync détecté via 4662, Golden Ticket détecté via anomalies Kerberos, ADTimeline — modifications d'objets), et forensic endpoint (analyse du serveur Azure AD Connect — extraction de la configuration de synchronisation et des credentials stockées par le connecteur).

Ce cas illustre la complexité croissante des investigations dans les environnements hybrides : l'attaquant pivote entre le cloud et l'on-premise en exploitant les mécanismes de synchronisation qui, par design, font le pont entre les deux mondes. L'investigation doit couvrir les deux environnements de manière intégrée, pas séparée.

---

## ANNEXES

---

### Annexe A — Glossaire forensic

| Terme | Définition |
|-------|-----------|
| **ADS** | Alternate Data Stream — flux de données secondaire attaché à un fichier NTFS, invisible dans l'explorateur |
| **AFU / BFU** | After First Unlock / Before First Unlock — états d'un mobile chiffré déterminant l'accessibilité des données |
| **Amcache** | Ruche registre Windows enregistrant les programmes exécutés avec hash SHA1 |
| **Anti-forensics** | Techniques utilisées pour empêcher, ralentir ou tromper l'investigation forensic |
| **Artefact** | Trace numérique laissée par une action sur un système — exploitable pour l'investigation |
| **Autopsy** | Plateforme open source de disk forensics, interface graphique de The Sleuth Kit |
| **BAM/DAM** | Background Activity Moderator / Desktop Activity Monitor — artefacts Windows d'exécution |
| **BitLocker** | Solution de chiffrement de disque intégré à Windows |
| **Carving** | Technique de récupération de fichiers par reconnaissance de signatures dans l'espace non alloué |
| **Chain of custody** | Documentation traçant le parcours complet d'une preuve, de sa collecte à sa présentation |
| **Contradictoire** | Principe juridique garantissant que les parties puissent examiner et contester les preuves |
| **C2** | Command and Control — infrastructure de commande d'un malware |
| **DCSync** | Technique d'attaque AD simulant un DC pour récupérer les hashes de tous les comptes |
| **DFIR** | Digital Forensics and Incident Response — combinaison des deux disciplines |
| **DumpIt** | Outil d'acquisition de mémoire vive pour Windows |
| **E01** | Expert Witness Format — format d'image forensic compressé avec métadonnées intégrées |
| **Event Log** | Journal d'événements Windows (format .evtx), source primaire du forensic Windows |
| **ext4** | Système de fichiers standard de Linux |
| **Fileless malware** | Malware s'exécutant uniquement en mémoire, sans écrire de fichier sur le disque |
| **FSEvents** | Journal des modifications de système de fichiers macOS |
| **FTK Imager** | Outil gratuit d'acquisition forensic (image disque, mémoire, preview) |
| **Golden Ticket** | TGT Kerberos forgé avec le hash du krbtgt, donnant un accès illimité au domaine AD |
| **Hashing** | Calcul d'empreinte numérique (MD5, SHA-256) pour la vérification d'intégrité |
| **Hiberfil.sys** | Fichier d'hibernation Windows contenant un dump mémoire compressé |
| **HPA / DCO** | Host Protected Area / Device Configuration Overlay — zones cachées d'un disque dur |
| **Inode** | Structure de métadonnées d'un fichier dans les systèmes de fichiers Unix/Linux |
| **IoC** | Indicator of Compromise — trace observable laissée par un malware (hash, domaine, IP) |
| **JA3/JA4** | Fingerprint TLS — empreinte du client TLS pour identifier des connexions suspectes |
| **Jump Lists** | Listes de fichiers récemment ouverts par application sous Windows |
| **KAPE** | Kroll Artifact Parser and Extractor — outil de collecte automatisée d'artefacts forensic |
| **Kerberoasting** | Technique d'attaque AD consistant à craquer les mots de passe via les tickets Kerberos |
| **KnowledgeC.db** | Base SQLite macOS enregistrant l'activité utilisateur détaillée |
| **LiME** | Linux Memory Extractor — module kernel pour l'acquisition mémoire Linux |
| **LNK** | Fichier raccourci Windows contenant le chemin, le volume et les timestamps du fichier cible |
| **LOLBins** | Living Off the Land Binaries — binaires système légitimes détournés pour l'attaque |
| **MFT** | Master File Table — table maîtresse du système de fichiers NTFS |
| **NTFS** | New Technology File System — système de fichiers standard de Windows |
| **ntds.dit** | Base de données Active Directory contenant tous les objets et hashes |
| **Pagefile.sys** | Fichier d'échange Windows contenant des pages mémoire déplacées sur le disque |
| **Plaso** | Outil de création de Super Timeline à partir d'artefacts forensic multiples |
| **Prefetch** | Artefact Windows enregistrant l'historique des programmes exécutés |
| **Process hollowing** | Technique d'injection de code remplaçant le contenu d'un processus légitime |
| **RAID** | Redundant Array of Independent Disks — configuration de stockage serveur |
| **RAT** | Remote Access Trojan — malware fournissant un accès distant persistant |
| **RegRipper** | Outil d'extraction automatisée d'artefacts depuis le registre Windows |
| **Scoping** | Délimitation du périmètre d'une investigation forensic |
| **ShellBags** | Artefacts du registre Windows enregistrant la navigation dans l'explorateur |
| **ShimCache** | AppCompatCache — artefact Windows d'historique d'exécution de programmes |
| **Slack space** | Espace résiduel en fin de cluster, contenant potentiellement des fragments de fichiers |
| **SRUM** | System Resource Usage Monitor — base de données Windows de consommation de ressources par processus |
| **$STANDARD_INFORMATION** | Attribut MFT contenant les timestamps MACB du fichier (falsifiable par timestomping) |
| **$FILE_NAME** | Attribut MFT contenant un second jeu de timestamps (difficile à falsifier) |
| **Super Timeline** | Timeline unifiée intégrant tous les artefacts temporels de toutes les sources |
| **Sysmon** | System Monitor — outil Microsoft de journalisation avancée (processus, réseau, registre) |
| **Timestomping** | Modification délibérée des timestamps d'un fichier pour brouiller la timeline |
| **TRIM** | Commande SSD effaçant les secteurs marqués comme libérés — rend la récupération impossible |
| **Unified Logging** | Système de journalisation centralisé de macOS |
| **$UsnJrnl** | Update Sequence Number Journal — journal NTFS des modifications de fichiers |
| **Velociraptor** | Outil open source de collecte forensic et de threat hunting à grande échelle |
| **Volatility** | Framework open source d'analyse de mémoire vive |
| **VQL** | Velociraptor Query Language — langage de requête pour Velociraptor |
| **Write blocker** | Dispositif empêchant toute écriture sur un support de stockage pendant l'acquisition |
| **YARA** | Langage de règles pour l'identification de malware par pattern matching |

---

### Annexe B — Cheat sheets outils

#### Acquisition disque

```bash
# dd (basique)
dd if=/dev/sdX of=/path/image.raw bs=4M status=progress

# dc3dd (avec hashing et logging)
dc3dd if=/dev/sdX hof=/path/image.dd hash=md5 hash=sha256 log=/path/log.txt

# FTK Imager (ligne de commande Linux)
ftkimager /dev/sdX /path/image --e01 --compress 6 --frag 4G --verify
```

#### Acquisition mémoire

```bash
# DumpIt (Windows — double-clic ou CLI)
DumpIt.exe /OUTPUT /path/memory.dmp

# WinPmem (Windows)
winpmem_mini_x64.exe /path/memory.raw

# LiME (Linux)
insmod lime.ko "path=/path/memory.lime format=lime"
```

#### Volatility 3

```bash
# Triage rapide
vol -f memory.raw windows.pstree
vol -f memory.raw windows.netscan
vol -f memory.raw windows.cmdline

# Investigation injection
vol -f memory.raw windows.malfind
vol -f memory.raw windows.dlllist --pid 7284

# Credentials
vol -f memory.raw windows.hashdump
vol -f memory.raw windows.lsadump

# Extraction
vol -f memory.raw windows.procdump --pid 7284 --dump-dir output/
vol -f memory.raw windows.dumpfiles --pid 7284 --dump-dir output/
```

#### Eric Zimmerman tools

```bash
# MFT (timestamps, timestomping detection)
MFTECmd.exe -f '$MFT' --csv output/ --csvf mft.csv

# Prefetch (exécution de programmes)
PECmd.exe -d 'C:\Windows\Prefetch' --csv output/ --csvf prefetch.csv

# Amcache (programmes avec hash)
AmcacheParser.exe -f Amcache.hve --csv output/ --csvf amcache.csv

# ShimCache (historique d'exécution)
AppCompatCacheParser.exe -f SYSTEM --csv output/ --csvf shimcache.csv

# ShellBags (navigation explorateur)
SBECmd.exe -d 'C:\Users\JMallet' --csv output/ --csvf shellbags.csv

# LNK files (fichiers récents, chemins réseau)
LECmd.exe -d 'C:\Users\JMallet\AppData\Roaming\Microsoft\Windows\Recent' --csv output/

# Jump Lists
JLECmd.exe -d 'AutomaticDestinations' --csv output/

# Event Logs
EvtxECmd.exe -f Security.evtx --csv output/ --csvf security.csv

# Registre (batch)
RECmd.exe -d 'C:\evidence\registry' --bn RECmd_Batch_MC.reb --csv output/

# SRUM (consommation réseau)
SrumECmd.exe -f SRUDB.dat -r SOFTWARE --csv output/
```

#### Plaso (Super Timeline)

```bash
# Extraction
log2timeline.py --storage-file timeline.plaso image.E01

# Filtrage et export
psort.py -o l2tcsv timeline.plaso -w timeline.csv \
  "date > '2026-01-01' AND date < '2026-03-08'"
```

#### KAPE

```bash
# Triage complet
kape.exe --tsource C: --tdest E:\Output --target KapeTriage

# Collecte + parsing
kape.exe --tsource C: --tdest E:\Output --target KapeTriage \
  --mdest E:\Parsed --module !EZParser
```

#### Réseau

```bash
# Capture tcpdump
tcpdump -i eth0 -w capture.pcap -c 1000000

# Filtrage Wireshark (CLI avec tshark)
tshark -r capture.pcap -Y "ip.addr == 103.xx.xx.xx" -w filtered.pcap

# Zeek
zeek -r capture.pcap local
# Résultat : conn.log, dns.log, http.log, ssl.log, files.log
```

#### Hashing

```bash
# Double hash (Linux)
md5sum image.E01 && sha256sum image.E01

# Hash récursif (hashdeep)
hashdeep -r -c md5,sha256 /path/evidence/ > hashes.txt

# Vérification
hashdeep -r -k hashes.txt -a /path/evidence/
```

---

### Annexe C — Artefacts Windows : référence rapide

| Artefact | Localisation | Outil de parsing | Ce qu'il révèle | Limites |
|----------|-------------|-----------------|-----------------|---------|
| MFT | `$MFT` (racine NTFS) | MFTECmd | Tous les fichiers avec timestamps $SI et $FN, détection timestomping | Volume massif (millions d'entrées) |
| $UsnJrnl | `$Extend\$UsnJrnl:$J` | MFTECmd | Modifications de fichiers (création, suppression, renommage) avec compte utilisateur | Taille limitée, rotation |
| Prefetch | `C:\Windows\Prefetch\` | PECmd | Programmes exécutés (8 dernières dates, nb exécutions) | Désactivé sur Windows Server |
| Amcache | `C:\Windows\appcompat\Programs\Amcache.hve` | AmcacheParser | Programmes avec hash SHA1 | Pas de compteur d'exécutions |
| ShimCache | Registre SYSTEM (AppCompatCache) | AppCompatCacheParser | Programmes exécutés avec timestamp | Persisté au shutdown uniquement |
| BAM/DAM | Registre SYSTEM (bam\State) | RegRipper, RECmd | Programmes exécutés avec timestamp UTC précis | Win10 1709+ / Server 2016+ |
| SRUM | `C:\Windows\System32\SRU\SRUDB.dat` | SrumECmd | Consommation réseau/CPU par processus (30-60 jours) | Base SQLite, rotation |
| Registre Run | NTUSER.DAT / SOFTWARE | RegRipper, RECmd | Persistence (programmes au démarrage) | L'attaquant peut nettoyer |
| UserAssist | NTUSER.DAT | RegRipper | Programmes exécutés via GUI (compteur + timestamp) | Encodé ROT13, GUI uniquement |
| ShellBags | NTUSER.DAT + UsrClass.dat | SBECmd | Dossiers navigués dans l'explorateur | Pas le contenu des fichiers |
| LNK files | `\Recent\` | LECmd | Fichiers ouverts, chemins réseau, volumes USB | Limité aux fichiers ouverts via GUI |
| Jump Lists | `\Recent\AutomaticDestinations\` | JLECmd | Fichiers récents par application | Rotation selon le nb d'entrées |
| Event Logs | `C:\Windows\System32\winevt\Logs\` | EvtxECmd, Chainsaw | Authentification, processus, services, PowerShell | Rotation (taille par défaut : 20 Mo) |
| Browser (Chrome) | `\AppData\Local\Google\Chrome\User Data\Default\` | Hindsight | Historique, cookies, downloads, passwords | Base SQLite, effaçable |
| RDP Bitmap Cache | `\AppData\Local\Microsoft\Terminal Server Client\Cache\` | bmc-tools, rdpieces | Fragments visuels de sessions RDP | Images partielles |
| Sysmon | `Microsoft-Windows-Sysmon/Operational.evtx` | EvtxECmd | Processus avec hash, connexions réseau, DLL | Nécessite déploiement préalable |

---

### Annexe D — Artefacts Linux et macOS : référence rapide

#### Linux

| Artefact | Localisation | Outil | Ce qu'il révèle |
|----------|-------------|-------|----------------|
| auth.log / secure | `/var/log/auth.log` ou `/var/log/secure` | grep, Plaso | Authentifications SSH, sudo, su |
| wtmp / btmp | `/var/log/wtmp`, `/var/log/btmp` | `last`, `lastb` | Sessions utilisateur (réussies / échouées) |
| lastlog | `/var/log/lastlog` | `lastlog` | Dernière connexion de chaque utilisateur |
| bash_history | `~/.bash_history` | cat, Plaso | Commandes exécutées (si non supprimé) |
| journald | `/var/log/journal/` | `journalctl` | Journal système structuré (systemd) |
| crontab | `/var/spool/cron/`, `/etc/crontab`, `/etc/cron.d/` | cat | Tâches planifiées (persistance) |
| SSH authorized_keys | `~/.ssh/authorized_keys` | cat | Clés SSH autorisées (persistance) |
| Apache/Nginx logs | `/var/log/apache2/`, `/var/log/nginx/` | grep, GoAccess | Requêtes web (détection webshell, injection) |

#### macOS

| Artefact | Localisation | Outil | Ce qu'il révèle |
|----------|-------------|-------|----------------|
| Unified Logging | `/var/db/diagnostics/` | `log show`, Unified Log Parser | Tout : processus, réseau, système, apps |
| FSEvents | `.fseventsd/` (racine volume) | FSEventsParser, mac_apt | Modifications du système de fichiers |
| KnowledgeC.db | `~/Library/Application Support/Knowledge/` | APOLLO, mac_apt | Activité utilisateur (apps, durée, réseau) |
| Spotlight metadata | `.Spotlight-V100/` | mdls, mac_apt | Métadonnées de tous les fichiers indexés |
| TCC.db | `~/Library/Application Support/com.apple.TCC/` | sqlite3 | Permissions d'accès (caméra, micro, fichiers) |
| LaunchAgents/Daemons | `~/Library/LaunchAgents/`, `/Library/LaunchDaemons/` | plutil | Persistence (programmes au démarrage) |
| Keychain | `~/Library/Keychains/` | security (CLI) | Credentials stockés (avec autorisation) |
| Safari | `~/Library/Safari/` | mac_apt, Autopsy | Historique, downloads, tabs ouvertes |

---

### Annexe E — Templates

#### Formulaire de chaîne de custody

```
CHAÎNE DE CUSTODY — PIÈCE N° [XX]

Affaire : [Nom de l'affaire / Nom de code]
Description de la pièce : [Type de support, modèle, numéro de série]
État à la collecte : [Allumé/éteint, état physique, connexions]

COLLECTE
  Date/Heure : [JJ/MM/AAAA HH:MM:SS, fuseau horaire]
  Collecté par : [Nom, qualité, organisme]
  Méthode : [Outil utilisé, version, paramètres]
  Hash MD5 : [________________________]
  Hash SHA-256 : [________________________]
  Lieu de stockage : [Coffre, numéro de casier]

TRANSFERTS
  | Date | De | À | Motif | Signature |
  |------|-----|-----|-------|-----------|
  | | | | | |

ANALYSES
  | Date | Analyste | Action | Outil | Hash vérifié ? |
  |------|----------|--------|-------|----------------|
  | | | | | |

Signature du responsable : _____________ Date : _____________
```

#### Template rapport forensic (structure)

```
RAPPORT D'INVESTIGATION FORENSIC
[CONFIDENTIEL — DIFFUSION RESTREINTE]

1. RÉSUMÉ EXÉCUTIF (1-2 pages)
   - Contexte, mandat, conclusions principales, impact, recommandations

2. CADRE DE L'INVESTIGATION
   - Mandataire, périmètre, questions investigatives
   - Méthodologie, outils (noms, versions), environnement d'analyse

3. CHRONOLOGIE DES OPÉRATIONS
   - Acquisitions réalisées (avec hash et chaîne de custody)
   - Analyses menées (séquence chronologique)

4. FAITS CONSTATÉS
   - Chaque constatation : source, date, description, niveau de confiance
   - Distinction explicite : fait / déduction / hypothèse

5. ANALYSE ET INTERPRÉTATION
   - Timeline de l'intrusion
   - Mapping MITRE ATT&CK
   - Hypothèses concurrentes et test

6. CONCLUSIONS
   - Réponses aux questions investigatives
   - Niveaux de confiance explicites
   - Ce qui n'a pas pu être déterminé (angles morts)

7. RECOMMANDATIONS
   - Mesures correctives et préventives
   - Suggestions pour la procédure judiciaire (si applicable)

ANNEXES
  A. IoC complets (hash, domaines, IP, artefacts)
  B. Timeline détaillée
  C. Captures d'écran annotées
  D. Chaîne de custody de chaque pièce
  E. Configuration de l'environnement d'analyse
```

---

### Annexe F — Ressources et certifications

#### Certifications (à jour 2025-2026)

| Certification | Organisme | Focus | Cours associé |
|--------------|-----------|-------|---------------|
| GCFE (Forensic Examiner) | SANS/GIAC | Windows forensics fondamental | FOR500 |
| GCFA (Forensic Analyst) | SANS/GIAC | Forensics avancé, threat hunting | FOR508 |
| GNFA (Network Forensic Analyst) | SANS/GIAC | Network forensics | FOR572 |
| GASF (Advanced Smartphone Forensics) | SANS/GIAC | Mobile forensics | FOR585 |
| GREM (Reverse Engineering Malware) | SANS/GIAC | Malware analysis | FOR610 |
| EnCE (EnCase Certified Examiner) | OpenText | EnCase forensics | Formation éditeur |
| ACE (AccessData Certified Examiner) | Exterro | FTK forensics | Formation éditeur |
| CHFI (Computer Hacking Forensic Investigator) | EC-Council | Forensics général | Programme EC-Council |
| CCFP (Certified Cyber Forensics Professional) | ISC² | Forensics management | Auto-formation + examen |

#### Formations SANS de référence

| Code | Titre | Focus |
|------|-------|-------|
| FOR500 | Windows Forensic Analysis | Artefacts Windows, registre, timeline |
| FOR508 | Advanced Incident Response, Threat Hunting, and Digital Forensics | IR + forensics avancé, memory forensics |
| FOR518 | Mac and iOS Forensic Analysis and Incident Response | macOS et iOS |
| FOR572 | Advanced Network Forensics: Threat Hunting, Analysis, and Incident Response | Network forensics |
| FOR578 | Cyber Threat Intelligence | CTI appliqué au forensic |
| FOR585 | Smartphone Forensic Analysis In-Depth | Mobile forensics |
| FOR610 | Reverse-Engineering Malware | Malware analysis avancé |

#### Communautés et conférences

| Ressource | Type | Description |
|-----------|------|-------------|
| DFRWS (Digital Forensic Research Workshop) | Conférence | Recherche académique en forensic |
| OSDFCon (Open Source Digital Forensics) | Conférence | Forensic open source (Autopsy, Sleuth Kit) |
| Magnet User Summit | Conférence | Forensic commercial (Magnet AXIOM) |
| SANS DFIR Summit | Conférence/Webcasts | Présentations pratiques DFIR |
| The DFIR Report | Blog | Rapports d'intrusion détaillés, pas à pas |
| 13Cubed (YouTube) | Vidéos | Tutoriels forensic pratiques |
| SANS DFIR Blog | Blog | Articles techniques et cas d'étude |
| Forensic Focus | Communauté | Articles, forums, offres d'emploi |
| r/digitalforensics | Reddit | Communauté, questions, ressources |
| FIRST | Communauté | Forum international des CERT/CSIRT |
| InterCERT France | Communauté | Association des CERT français |

#### Ouvrages de référence

| Titre | Auteur(s) | Sujet |
|-------|-----------|-------|
| *The Art of Memory Forensics* | Hale Ligh, Case, Levy, Walters | Analyse mémoire avec Volatility |
| *File System Forensic Analysis* | Brian Carrier | Systèmes de fichiers (NTFS, ext, FAT) |
| *Incident Response & Computer Forensics* | Luttgens, Pepe, Mandia | IR + forensic intégré |
| *Digital Forensics with Kali Linux* | Parasram | Forensic pratique avec Kali |
| *Practical Malware Analysis* | Sikorski, Honig | Analyse de malware (statique + dynamique) |
| *Windows Forensic Analysis* (SANS courseware) | Rob Lee | Artefacts Windows en profondeur |
| *Network Forensics* | Davidoff, Ham | Analyse réseau forensic |

---

---

# Annexe — Questions types d'entretien et réponses types

## Questions essentielles

- **Question :** Quelle est la différence entre le forensic judiciaire et le triage DFIR ?
  - **Réponse type :** Le forensic judiciaire vise à produire des preuves recevables devant un tribunal — l'exhaustivité et la chaîne de custody priment. Le triage DFIR vise à comprendre rapidement ce qui se passe pour contenir la menace — la rapidité prime. En pratique, les deux s'articulent : on commence souvent en triage et on bascule en judiciaire si les constatations le justifient. C'est pour ça qu'il faut respecter les bonnes pratiques de préservation dès le début, même en triage — on ne sait jamais si l'affaire finira devant un juge.

- **Question :** Qu'est-ce que la chaîne de custody et pourquoi c'est critique ?
  - **Réponse type :** La chaîne de custody trace chaque manipulation d'une preuve : qui l'a collectée, quand, comment, où elle a été stockée, qui y a eu accès. C'est ce qui garantit l'intégrité et la recevabilité de la preuve en justice. Si la chaîne est rompue — par exemple une image disque non hashée ou un scellé mal documenté —, la partie adverse peut contester la preuve et le juge peut la rejeter.

- **Question :** Qu'est-ce que l'ordre de volatilité et comment l'appliquez-vous ?
  - **Réponse type :** L'ordre de volatilité dicte la priorité de collecte : on commence par ce qui disparaît le plus vite. La mémoire RAM est la plus volatile — elle contient les processus en cours, les clés de chiffrement, les connexions réseau, et elle disparaît au redémarrage. Ensuite les logs système, le cache, les fichiers temporaires, puis le disque dur. En pratique : d'abord le dump RAM (DumpIt), puis le triage KAPE pour les artefacts, puis l'image disque complète. Et surtout, ne jamais éteindre une machine avant d'avoir capturé la mémoire.

- **Question :** Quels sont les principaux artefacts Windows que vous analysez ?
  - **Réponse type :** Pour l'exécution : le Prefetch (programmes exécutés avec dates), l'Amcache et le ShimCache (historique d'exécution avec hash), les Event Logs (4688 création de processus, Sysmon). Pour l'activité utilisateur : les ShellBags (navigation explorateur), les Jump Lists (fichiers récents par application), les fichiers LNK (raccourcis avec chemins et dates). Pour la persistence : les clés Run/RunOnce du registre, les services, les tâches planifiées. La MFT pour la timeline de tous les fichiers. Les outils Eric Zimmerman (MFTECmd, PECmd, AmcacheParser) sont la référence pour parser tout ça.

- **Question :** Comment détectez-vous le timestomping ?
  - **Réponse type :** Le timestomping consiste à modifier les timestamps des fichiers pour masquer l'activité. Sous NTFS, il y a deux jeux de timestamps : $STANDARD_INFORMATION (modifiable par l'utilisateur) et $FILE_NAME (modifiable uniquement par le kernel). Si les deux divergent — par exemple si $SI montre une date ancienne mais $FN montre une date récente — c'est un signe de manipulation. MFTECmd extrait les deux et la comparaison est immédiate.

## Questions complémentaires

- **Question :** Quels outils utilisez-vous pour le triage rapide ?
  - **Réponse type :** KAPE (Kroll Artifact Parser and Extractor) pour la collecte et le parsing automatisé des artefacts Windows — en quelques minutes il collecte les Event Logs, le registre, le Prefetch, la MFT, l'Amcache, les historiques navigateur. Velociraptor pour la collecte à distance sur un parc entier via des requêtes VQL. FTK Imager pour l'acquisition disque en format E01 avec write blocker. Et DumpIt pour le dump mémoire.

- **Question :** C'est quoi l'analyse mémoire et pourquoi c'est indispensable ?
  - **Réponse type :** L'analyse mémoire capture l'état instantané du système : les processus en cours, les connexions réseau, les DLLs chargées, les credentials en clair, et le code des malwares fileless qui n'existent qu'en RAM. L'outil de référence c'est Volatility 3. On peut identifier un processus injecté (svchost.exe avec un parent anormal), extraire les clés de chiffrement d'un ransomware, ou trouver un RAT qui ne touche jamais le disque. Sans dump mémoire, on perd toute cette information au redémarrage.

## Questions les plus probables en entretien

1. Forensic judiciaire vs triage DFIR ?
2. Chaîne de custody : pourquoi c'est critique ?
3. Ordre de volatilité : RAM en premier ?
4. Artefacts Windows clés ?
5. Comment détecter le timestomping ?
6. Outils de triage et d'acquisition ?

## Réponses flash

- **Forensic vs triage** → Judiciaire = exhaustivité, preuve recevable, chaîne de custody. DFIR = rapidité, contenir la menace. Les deux s'articulent.
- **Chaîne de custody** → Qui, quand, comment, où. Hash (MD5 + SHA-256). Rupture = preuve contestable.
- **Volatilité** → RAM → cache → logs → fichiers temp → disque. D'abord DumpIt, puis KAPE, puis image disque.
- **Artefacts Windows** → Prefetch, Amcache, ShimCache (exécution). ShellBags, LNK, Jump Lists (activité). Run keys, services, tasks (persistence). MFT (timeline).
- **Timestomping** → Comparer $STANDARD_INFORMATION vs $FILE_NAME dans la MFT. Divergence = manipulation.
- **Outils** → KAPE (triage), Velociraptor (collecte à distance), FTK Imager (image E01), DumpIt (RAM), Volatility 3 (analyse mémoire), Eric Zimmerman tools (parsing).

---


> **Note de clôture**
>
> Ce cours a été conçu pour former à l'investigation numérique comme discipline scientifique complète — de l'acquisition rigoureuse des preuves à la production d'un rapport défendable devant un tribunal, en passant par l'analyse technique approfondie des artefacts sur tous les types de systèmes.
>
> L'investigation MUSIC BOX qui traverse les 29 premiers chapitres illustre la réalité du terrain : l'analyste forensic ne se contente pas d'extraire des artefacts d'une machine — il reconstitue une histoire de 60 jours de compromission, il corrèle des sources hétérogènes (endpoint, réseau, AD, cloud), il détecte les tentatives d'anti-forensics de l'attaquant, il raisonne par hypothèses en gérant ses propres biais, et il produit un rapport qui sera lu par un juge ET par un CEO.
>
> La compétence forensic ne se résume pas à la maîtrise des outils — c'est une posture intellectuelle : rigueur, doute méthodique, transparence des conclusions, et humilité face à la complexité du réel. Les outils évoluent (Volatility 4 remplacera peut-être Volatility 3, de nouveaux artefacts apparaîtront avec chaque version de Windows), mais la posture reste.
>
> *Acquisition • Analyse • Preuve • Rapport — avec rigueur et objectivité.*

