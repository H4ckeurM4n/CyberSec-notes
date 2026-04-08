# RÉPONSE À INCIDENT DE CYBERSÉCURITÉ

*Préparer • Détecter • Qualifier • Investiguer • Contenir • Éradiquer • Restaurer • Capitaliser*

**Cours complet — 40 chapitres • 8 parties • 7 annexes**

*Méthodologie, investigation, coordination, crise et amélioration continue*

---

## Table des matières

- [Fil rouge : Opération BLACKTIDE](#fil-rouge--opération-blacktide)
- **PARTIE I — FONDATIONS : COMPRENDRE LA RÉPONSE À INCIDENT (Ch.1-4)**
  - [Ch.1 — Qu'est-ce qu'un incident de sécurité](#chapitre-1--quest-ce-quun-incident-de-sécurité)
  - [Ch.2 — L'Incident Response comme discipline d'orchestration](#chapitre-2--lincident-response-comme-discipline-dorchestration)
  - [Ch.3 — Incident technique, incident majeur, crise cyber : les seuils de bascule](#chapitre-3--incident-technique-incident-majeur-crise-cyber--les-seuils-de-bascule)
  - [Ch.4 — Référentiels, modèles et cadres méthodologiques](#chapitre-4--référentiels-modèles-et-cadres-méthodologiques)
- **PARTIE II — PRÉPARATION : AVANT QUE L'INCIDENT N'ARRIVE (Ch.5-10)**
  - [Ch.5 — Pourquoi la préparation détermine tout](#chapitre-5--pourquoi-la-préparation-détermine-tout)
  - [Ch.6 — Gouvernance et organisation IR](#chapitre-6--gouvernance-et-organisation-ir)
  - [Ch.7 — Playbooks et procédures opérationnelles](#chapitre-7--playbooks-et-procédures-opérationnelles)
  - [Ch.8 — Préparation technique : outillage et télémétrie](#chapitre-8--préparation-technique--outillage-et-télémétrie)
  - [Ch.9 — Préparation juridique, réglementaire et contractuelle](#chapitre-9--préparation-juridique-réglementaire-et-contractuelle)
  - [Ch.10 — Exercices et entraînement](#chapitre-10--exercices-et-entraînement)
- **PARTIE III — DÉTECTION, QUALIFICATION ET TRIAGE (Ch.11-15)**
  - [Ch.11 — Du signal faible à l'incident confirmé](#chapitre-11--du-signal-faible-à-lincident-confirmé)
  - [Ch.12 — Triage initial et premières mesures conservatoires](#chapitre-12--triage-initial-et-premières-mesures-conservatoires)
  - [Ch.13 — Qualification, catégorisation et évaluation de gravité](#chapitre-13--qualification-catégorisation-et-évaluation-de-gravité)
  - [Ch.14 — Scoping initial : délimiter l'étendue de la compromission](#chapitre-14--scoping-initial--délimiter-létendue-de-la-compromission)
  - [Ch.15 — Déclenchement formel et premières notifications](#chapitre-15--déclenchement-formel-et-premières-notifications)
- **PARTIE IV — INVESTIGATION ET ANALYSE (Ch.16-22)**
  - [Ch.16 — Principes de l'investigation IR](#chapitre-16--principes-de-linvestigation-ir)
  - [Ch.17 — Construction de la timeline d'attaque](#chapitre-17--construction-de-la-timeline-dattaque)
  - [Ch.18 — Cartographie des sources de données](#chapitre-18--cartographie-des-sources-de-données)
  - [Ch.19 — Investigation endpoint : collecte et analyse concrète](#chapitre-19--investigation-endpoint--collecte-et-analyse-concrète)
  - [Ch.20 — Investigation identité et Active Directory](#chapitre-20--investigation-identité-et-active-directory)
  - [Ch.21 — Investigation réseau et exfiltration](#chapitre-21--investigation-réseau-et-exfiltration)
  - [Ch.22 — Investigation des environnements hybrides, OT et dépendances tierces](#chapitre-22--investigation-des-environnements-hybrides-ot-et-dépendances-tierces)
- **PARTIE V — CONFINEMENT, DÉCISION ET PRÉSERVATION DE PREUVE (Ch.23-26)**
  - [Ch.23 — Stratégies de confinement et arbitrages](#chapitre-23--stratégies-de-confinement-et-arbitrages)
  - [Ch.24 — Confinement par type d'incident](#chapitre-24--confinement-par-type-dincident)
  - [Ch.25 — Préserver les preuves sous pression](#chapitre-25--préserver-les-preuves-sous-pression)
  - [Ch.26 — Décider sous incertitude](#chapitre-26--décider-sous-incertitude)
- **PARTIE VI — ÉRADICATION, RECONSTRUCTION ET REPRISE (Ch.27-32)**
  - [Ch.27 — Plan d'éradication coordonné](#chapitre-27--plan-déradication-coordonné)
  - [Ch.28 — Reconstruction des systèmes](#chapitre-28--reconstruction-des-systèmes)
  - [Ch.29 — Validation d'éradication et surveillance post-nettoyage](#chapitre-29--validation-déradication-et-surveillance-post-nettoyage)
  - [Ch.30 — Reprise d'activité](#chapitre-30--reprise-dactivité)
  - [Ch.31 — Durcissement post-incident](#chapitre-31--durcissement-post-incident)
  - [Ch.32 — Extorsion, rançon et arbitrages stratégiques](#chapitre-32--extorsion-rançon-et-arbitrages-stratégiques)
- **PARTIE VII — GESTION DE CRISE, COMMUNICATION ET COORDINATION (Ch.33-37)**
  - [Ch.33 — Quand l'incident devient une crise](#chapitre-33--quand-lincident-devient-une-crise)
  - [Ch.34 — Cellule de crise cyber](#chapitre-34--cellule-de-crise-cyber)
  - [Ch.35 — Communication de crise](#chapitre-35--communication-de-crise)
  - [Ch.36 — Coordination avec les parties prenantes externes](#chapitre-36--coordination-avec-les-parties-prenantes-externes)
  - [Ch.37 — Volet juridique, réglementaire et financier](#chapitre-37--volet-juridique-réglementaire-et-financier)
- **PARTIE VIII — POST-INCIDENT, MATURITÉ ET CAPITALISATION (Ch.38-40)**
  - [Ch.38 — Clôture de l'incident et retour d'expérience (RETEX)](#chapitre-38--clôture-de-lincident-et-retour-dexpérience-retex)
  - [Ch.39 — Métriques, maturité et programme IR durable](#chapitre-39--métriques-maturité-et-programme-ir-durable)
  - [Ch.40 — Scénarios d'incident : atelier de synthèse](#chapitre-40--scénarios-dincident--atelier-de-synthèse)
- **ANNEXES**
  - [Annexe A — Glossaire](#annexe-a--glossaire)
  - [Annexe B — Checklists opérationnelles](#annexe-b--checklists-opérationnelles)
  - [Annexe C — Templates de documents IR](#annexe-c--templates-de-documents-ir)
  - [Annexe D — Cheat sheets techniques](#annexe-d--cheat-sheets-techniques)
  - [Annexe E — Playbooks types détaillés](#annexe-e--playbooks-types-détaillés)
  - [Annexe F — Tableau d'outils de référence IR](#annexe-f--tableau-doutils-de-référence-ir)
  - [Annexe G — Grilles d'évaluation et RACI](#annexe-g--grilles-dévaluation-et-raci)

---

## Fil rouge : Opération BLACKTIDE

> **Contexte narratif — ce fil rouge traverse les 38 premiers chapitres du cours.**
>
> **Vendredi 14 mars 2026, 22h17.** Le SOC d'**Arvantis**, groupe industriel français coté au SBF 120 (12 000 collaborateurs, 15 sites de production en Europe, activité chimie fine et matériaux spéciaux, classé OIV sur 2 sites dont le complexe pétrochimique de Fos-sur-Mer), détecte une alerte EDR sur le contrôleur de domaine DC01 : exécution suspecte de `PsExec` couplée à une tentative de désactivation de Windows Defender via modification de GPO.
>
> L'analyste SOC N2 de garde, **Karim Belkacem**, vérifie l'alerte, confirme qu'il ne s'agit pas d'une opération d'administration planifiée, et escalade immédiatement vers l'IR lead.
>
> L'investigation va progressivement révéler une compromission profonde : un infostealer (variant Lumma) déployé 5 semaines plus tôt via un phishing ciblé sur le sous-traitant RH GestPaie, une élévation de privilèges via Kerberoasting sur un compte de service avec droits Domain Admin, un mouvement latéral méthodique via PsExec et RDP, une exfiltration de 380 Go de données R&D vers une instance AWS EC2 louée avec une carte prépayée, et le déploiement en cours d'un ransomware PhantomCrypt (connexion directe avec le cours *Cartographie des Écosystèmes Cybercriminels*) via GPO malveillante. Le chiffrement est partiellement contenu mais 3 sites sur 15 sont impactés, dont le site OIV de Fos-sur-Mer.
>
> L'équipe IR d'Arvantis, menée par **Nadia Moreau** (IR lead), sera confrontée à chaque chapitre à des décisions concrètes sous pression : quand couper le réseau et quand ne PAS le couper, comment préserver les preuves quand un admin a déjà redémarré 2 serveurs, quoi dire au CEO qui veut « redémarrer les usines lundi », comment articuler avec l'ANSSI et le CERT-FR, comment traiter la demande de rançon de 4,2 M€, comment reconstruire un AD dont le compte krbtgt est compromis, et comment s'assurer que l'attaquant n'est plus là avant de relancer la production chimique.
>
> Le coût total de l'incident sera estimé à 8,5 M€. Le retex final (Ch.38) produira 15 recommandations structurées et un plan d'amélioration sur 18 mois.

---

## PARTIE I — FONDATIONS : COMPRENDRE LA RÉPONSE À INCIDENT

*Avant de répondre à un incident : comprendre ce qu'est un incident, ce qui distingue l'IR des disciplines voisines, quand un incident devient une crise, et quels cadres méthodologiques structurent la discipline.*

---

### Chapitre 1 — Qu'est-ce qu'un incident de sécurité

#### 1.1 Définition opérationnelle : événement, alerte, incident, crise

La chaîne conceptuelle qui va du bruit ambiant du système d'information jusqu'à la crise majeure comprend quatre niveaux distincts, et la confusion entre ces niveaux est une source récurrente de dysfonctionnement dans les organisations.

Un **événement** est un fait observable dans le système d'information : une connexion réseau, une authentification, une modification de fichier, un scan de port, un redémarrage de service. Les systèmes d'information modernes génèrent des milliards d'événements par jour. La quasi-totalité sont normaux et attendus.

Une **alerte** est un événement signalé par un système de détection (EDR, SIEM, IDS, antivirus, règle de corrélation) comme potentiellement anormal ou malveillant. Le taux de faux positifs des systèmes de détection varie considérablement (de 10 % dans les environnements bien calibrés à plus de 90 % dans les environnements mal configurés), ce qui signifie que la majorité des alertes ne correspondent pas à des incidents réels. Le travail du SOC est précisément de trier ces alertes pour identifier celles qui nécessitent une investigation.

Un **incident** est une alerte confirmée qui compromet effectivement la confidentialité, l'intégrité, ou la disponibilité d'un actif du système d'information. La confirmation transforme la suspicion en certitude : un comportement malveillant est effectivement en cours ou a eu lieu. L'incident déclenche des processus spécifiques (investigation, confinement, notification) et mobilise des acteurs qui ne sont pas impliqués dans le traitement des alertes courantes.

Une **crise cyber** est un incident dont l'impact dépasse la capacité de réponse normale de l'organisation et nécessite l'activation d'une gouvernance exécutive. La crise se caractérise par l'ampleur de l'impact (technique, business, réputationnel, réglementaire), l'incertitude sur l'évolution, la pression temporelle intense, et la nécessité de décisions stratégiques qui dépassent le périmètre de l'équipe technique. La distinction entre incident et crise est traitée en profondeur au Ch.3.

Ces distinctions ne sont pas sémantiques. Elles déterminent le niveau de mobilisation (qui est réveillé à 2h du matin), les processus activés (IRP, cellule de crise, communication), les obligations réglementaires (notification ANSSI, CNIL), et les interlocuteurs impliqués (la direction générale n'est pas mobilisée pour chaque alerte — elle l'est pour une crise).

> **Piège fréquent :** Confondre la gravité technique et la gravité business. Un malware sur un poste isolé sans données sensibles est un incident technique mineur même si le malware est sophistiqué. Un phishing qui compromet le compte email du directeur financier est un incident business potentiellement majeur même si la technique est triviale. La classification doit intégrer les deux dimensions.

#### 1.2 Taxonomie des incidents

Une taxonomie partagée est indispensable pour trois raisons : elle accélère le triage (chaque catégorie active un playbook spécifique — voir Ch.7), elle normalise la communication (tous les acteurs parlent le même langage), et elle structure le reporting (les métriques et les tendances ne sont comparables que si les incidents sont classés de manière cohérente).

La classification par **vecteur d'attaque** identifie comment l'attaquant a pénétré le système : phishing (email, SMS, voix), exploitation de vulnérabilité (0-day, N-day non patchée), compromission supply chain (mise à jour logicielle piégée, prestataire compromis), credential stuffing ou brute force, insider (employé ou ex-employé malveillant), accès physique, ou compromission de tiers de confiance (VPN prestataire, accès partenaire).

La classification par **objectif** identifie ce que l'attaquant cherche à accomplir : ransomware et extorsion (chiffrement + menace de publication), espionnage et exfiltration (vol de propriété intellectuelle, renseignement), sabotage et destruction (wiper, manipulation de systèmes OT), fraude financière (BEC, détournement de virements), hacktivisme (défacement, DDoS idéologique), ou cryptomining (utilisation des ressources de calcul).

La classification par **impact** identifie les conséquences : atteinte à la confidentialité (données exposées), atteinte à la disponibilité (systèmes hors service), atteinte à l'intégrité (données modifiées), impact réputationnel (perte de confiance des clients, médiatisation), impact réglementaire (notification obligatoire, sanctions), et impact financier (perte d'exploitation, rançon, frais de remédiation).

La classification par **gravité** va de P4 (incident mineur — malware isolé, phishing sans compromission) à P1 (incident critique — compromission de l'AD, ransomware à grande échelle, exfiltration massive) avec des critères objectifs pour chaque niveau. Le détail de la grille de gravité est en Annexe G.

#### 1.3 L'incident comme révélateur systémique

Un incident de sécurité n'est jamais un événement isolé. Il est le symptôme visible d'une ou plusieurs défaillances systémiques dans les couches de défense de l'organisation. L'investigation IR ne vise pas seulement à résoudre l'incident présent — elle vise à comprendre pourquoi les défenses ont échoué et à corriger les causes racines.

Pourquoi le phishing a-t-il fonctionné ? Parce que le sous-traitant n'avait pas de MFA, parce que l'utilisateur n'était pas formé, parce que le filtre anti-phishing n'a pas détecté la pièce jointe. Pourquoi l'attaquant a-t-il pu progresser pendant 5 semaines ? Parce que l'infostealer a échappé à l'antivirus, parce que les alertes de l'EDR ont été classées en faux positifs, parce que la surveillance des comptes de service était insuffisante. Pourquoi le ransomware a-t-il pu chiffrer les sauvegardes ? Parce qu'elles étaient sur le même réseau, accessibles avec les mêmes credentials.

Chaque « pourquoi » révèle une faille corrigeable. C'est cette logique de Root Cause Analysis qui transforme un incident douloureux en opportunité d'amélioration structurelle. L'IR n'est pas du « pompierisme » — c'est de l'investigation structurée avec un double objectif : résoudre l'incident actuel ET empêcher le suivant.

#### 1.4 Fil rouge — BLACKTIDE : l'alerte initiale

> **🔍 BLACKTIDE — Épisode 1**
>
> Vendredi 14 mars 2026, 22h17. L'EDR CrowdStrike Falcon déployé sur le contrôleur de domaine DC01 d'Arvantis déclenche une alerte de sévérité « haute » : détection de l'exécution de `PsExec.exe` depuis le répertoire `C:\Users\svc_deploy\AppData\Local\Temp\`, couplée à une modification de GPO visant à désactiver Windows Defender (commande PowerShell `Set-MpPreference -DisableRealtimeMonitoring $true` exécutée via GPO).
>
> Karim Belkacem, analyste SOC N2 en astreinte, reçoit l'alerte sur son téléphone. Il se connecte à la console EDR depuis son domicile et vérifie : aucune opération de maintenance planifiée ce soir, le compte `svc_deploy` est un compte de service rarement utilisé, et l'exécution de PsExec depuis un répertoire temporaire est anormale. Il contacte l'administrateur d'astreinte : « Tu as lancé quelque chose sur DC01 ce soir ? » Réponse : « Non, rien du tout. »
>
> Karim qualifie : **incident confirmé**. L'activité n'est pas légitime, elle cible un contrôleur de domaine, et elle implique un outil de mouvement latéral et une tentative de désactivation des défenses. Classification initiale : P2 (incident significatif — compromission de serveur critique), en attente de réévaluation.
>
> Il applique la procédure d'escalade : appel à l'IR lead, Nadia Moreau. Il est 22h45.
>
> Première question que personne ne pose encore : depuis combien de temps l'attaquant est-il dans le réseau ?

---

### Chapitre 2 — L'Incident Response comme discipline d'orchestration

#### 2.1 Ce qui distingue l'IR du SOC

Le SOC (Security Operations Center) est un dispositif permanent de détection et de triage. Les analystes SOC N1 traitent les alertes en masse, filtrent les faux positifs, et escaladent les vrais positifs. Les analystes N2 investiguent les alertes escaladées et confirment ou infirment les incidents. Le SOC est un capteur permanent — il fonctionne 24/7, traite des centaines ou des milliers d'alertes par jour, et son objectif est de détecter et qualifier.

L'IR (Incident Response) prend le relais quand l'alerte est confirmée comme incident. L'IR pilote l'investigation approfondie, coordonne les acteurs techniques et non techniques, prend les décisions de confinement et d'éradication, et conduit l'organisation jusqu'à la résolution complète et le retour d'expérience. L'IR est une capacité activée ponctuellement — elle se déclenche quand un incident est confirmé et se désactive quand l'incident est clos.

La frontière entre SOC et IR n'est pas toujours nette dans les petites organisations (les mêmes personnes peuvent porter les deux casquettes), mais les fonctions sont distinctes : le SOC détecte, l'IR orchestre la réponse.

#### 2.2 Ce qui distingue l'IR du forensic

Le forensic numérique (digital forensics) est une discipline d'analyse technique approfondie : acquisition d'images disque bit-à-bit, analyse de la mémoire vive, analyse d'artefacts système, reverse engineering de malware, reconstitution chronologique granulaire des actions sur un système. Le forensic produit des preuves — au sens technique et parfois judiciaire.

L'IR utilise le forensic comme un outil parmi d'autres. L'investigateur IR fait du forensic « good enough » — orienté décision, pas orienté preuve exhaustive. La question de l'IR n'est pas « quelle est l'empreinte exacte du malware dans le registre à la microseconde près ? » mais « ce serveur est-il compromis ? oui ou non — parce que je dois décider dans 30 minutes si je l'isole ». L'IR cherche la compréhension opérationnelle suffisante pour agir ; le forensic cherche la reconstitution exhaustive.

En pratique, les deux sont souvent menés en parallèle : l'IR guide les actions immédiates (confinement, éradication), pendant qu'un forensicien dédié ou un prestataire PRIS produit les analyses approfondies et les preuves pour la plainte pénale. Le cours SOC de la bibliothèque traite de la détection en détail ; le cours Forensic traite de l'analyse technique en profondeur. Ce cours traite de l'orchestration.

#### 2.3 Ce qui distingue l'IR de la gestion de crise

La gestion de crise est un processus de gouvernance qui mobilise la direction générale, la communication, le juridique, et les métiers. Elle traite les aspects stratégiques, réputationnels, réglementaires et financiers de l'incident. L'IR est la composante technique de la gestion de crise.

Les deux doivent fonctionner en parallèle et se nourrir mutuellement, mais ce ne sont pas les mêmes compétences, les mêmes temporalités, ni les mêmes interlocuteurs. L'analyste forensic qui explique la structure des Event IDs Windows au CEO perd son temps et celui du CEO. Le CEO qui intervient dans les décisions de confinement technique prend des risques qu'il ne mesure pas. L'articulation entre la cellule technique (IR) et la cellule de crise exécutive est un enjeu majeur traité au Ch.3 (seuils de bascule) et en Partie VII (gestion de crise).

#### 2.4 Le rôle d'orchestration de l'IR lead

L'IR lead n'est pas nécessairement le meilleur forensicien de l'équipe, ni le meilleur analyste réseau, ni le meilleur spécialiste AD. Il est celui qui maintient la vision d'ensemble de l'incident, coordonne les experts en leur assignant des questions précises, arbitre les priorités quand les ressources sont limitées (et elles le sont toujours), fait l'interface entre le monde technique et le monde décisionnel (traduire « le krbtgt est compromis » en « l'attaquant contrôle potentiellement l'ensemble de notre infrastructure — c'est un incident majeur »), et documente les décisions et leurs justifications.

C'est un chef d'orchestre, pas un soliste. Sa valeur ne réside pas dans sa capacité à analyser un dump mémoire (il a des analystes pour ça) mais dans sa capacité à poser les bonnes questions, à prioriser les efforts, et à maintenir la cohérence de la réponse quand 15 personnes travaillent en parallèle sur des aspects différents de l'incident.

#### 2.5 La logique fondamentale : temps court, forte incertitude, conséquences élevées

L'IR opère dans un régime de décision radicalement différent de la sécurité « temps de paix ». En temps de paix, une décision de sécurité (déployer un EDR, durcir l'AD, segmenter le réseau) peut être étudiée pendant des semaines, testée en environnement de pré-production, et déployée progressivement. En temps d'incident, les décisions doivent être prises en heures (parfois en minutes), avec des informations partielles et évolutives.

Les conséquences d'une mauvaise décision sont immédiates et parfois irréversibles. Isoler un serveur de production arrête la production. Redémarrer un serveur sans collecte forensic détruit la mémoire vive. Communiquer publiquement trop tôt peut être contredit par les faits. Ne pas contenir assez vite laisse l'attaquant progresser. Chaque décision est un arbitrage entre des risques concurrents, et cet arbitrage se fait sous pression, avec de la fatigue, et souvent au milieu de la nuit.

Cette pression n'est pas un accident — c'est la nature même de l'IR. La capacité à décider sous incertitude, à accepter le risque résiduel de chaque décision, et à documenter le raisonnement qui a conduit à cette décision (pour le retex et pour la protection juridique des décideurs) est la compétence fondamentale de l'IR lead. Le Ch.26 est entièrement dédié à cette dimension.

#### 2.6 Fil rouge — BLACKTIDE : l'organisation de la réponse

> **🔍 BLACKTIDE — Épisode 2**
>
> 22h45. Karim appelle Nadia Moreau, IR lead d'Arvantis. Elle décroche immédiatement — elle était d'astreinte ce week-end.
>
> Nadia pose les questions de cadrage en 5 minutes : « Qu'est-ce qu'on voit ? » (PsExec + GPO Defender sur DC01). « Depuis quand ? » (l'alerte EDR date de 22h17, mais on ne sait pas depuis quand l'attaquant est dans le réseau). « Combien de systèmes ? » (DC01 confirmé, à vérifier sur les autres DC). « L'attaquant est-il toujours actif ? » (probablement — l'exécution est récente). « Est-ce qu'on a touché à quelque chose ? » (non, Karim n'a fait qu'observer).
>
> Nadia active le protocole de réponse :
> - Ouverture du canal Signal « IR-BLACKTIDE » (canal pré-configuré, hors SI d'entreprise — le SI interne n'est plus de confiance).
> - Appel au RSSI, Marc Delaunay (réveillé, répond en 2 sonneries — il était en astreinte).
> - Appel au prestataire PRIS sous contrat, CyberForce (SLA : intervention dans les 12h le week-end — arrivée estimée samedi 8h).
> - Message aux analystes SOC N2 disponibles : « surveillance renforcée immédiate sur tous les DC, recherche de PsExec et de modifications GPO sur le parc. »
>
> Première tension : le responsable astreinte IT, David Lemaire, est réveillé par les alertes et propose de « patcher et redémarrer DC01 pour stopper l'attaque ». Nadia l'arrête fermement : « Pas de redémarrage. Pas de modification. On ne touche à rien tant qu'on n'a pas compris ce qui se passe et collecté les preuves. La mémoire de DC01 contient peut-être les clés de l'investigation. » David accepte, mais avec réticence — il sent que « quelque chose de grave est en train de se passer » et son réflexe d'admin est de « réparer ».

---

### Chapitre 3 — Incident technique, incident majeur, crise cyber : les seuils de bascule

#### 3.1 Pourquoi cette distinction est critique

En pratique, la confusion entre « incident gérable par l'équipe technique » et « crise nécessitant une gouvernance exécutive » est une source majeure de dysfonctionnement. Deux erreurs symétriques menacent.

La **sous-escalade** : traiter une crise comme un incident technique ordinaire. L'équipe IT essaie de « gérer en interne » un ransomware qui a chiffré 200 serveurs, sans informer la direction, sans mobiliser le juridique, sans notifier l'ANSSI. Les conséquences : perte de temps critique, non-respect des obligations légales, décisions techniques prises sans validation stratégique, et découverte tardive de l'ampleur réelle — souvent quand l'attaquant publie les données sur son leak site et que la presse appelle.

La **sur-escalade** : déclencher la cellule de crise pour un incident mineur. Un phishing bloqué par le filtre email, un malware isolé sur un poste sans données sensibles, une tentative de brute force bloquée par le WAF. La sur-escalade crée de la panique inutile, use la crédibilité de l'équipe sécurité auprès de la direction (« ils crient au loup tout le temps »), et gaspille des ressources qui seraient mieux employées ailleurs.

La capacité à calibrer correctement l'escalade — ni trop, ni trop peu — est une compétence clé de l'IR lead. Elle repose sur des critères objectifs, pas sur l'intuition.

#### 3.2 Critères de bascule en incident majeur

Un incident technique standard bascule en **incident majeur** quand au moins un des critères suivants est vérifié : compromission de l'Active Directory (contrôleur de domaine, compte krbtgt, Golden Ticket — la perte de contrôle de l'AD signifie la perte de contrôle de l'ensemble du SI Windows), chiffrement ou destruction de données à grande échelle (le ransomware a touché plus de quelques postes isolés), exfiltration de données sensibles confirmée (propriété intellectuelle, données personnelles, secrets industriels), impact sur un site OIV ou une infrastructure critique (obligations légales spécifiques), atteinte au réseau OT/ICS (risque physique potentiel), compromission du système de sauvegarde (la dernière ligne de défense est tombée), ou indisponibilité d'un service critique métier (production, facturation, logistique).

L'incident majeur déclenche une mobilisation renforcée : le prestataire PRIS est appelé si pas encore mobilisé, le RSSI prend le relais de la coordination, et un point de situation régulier est établi avec la direction technique.

#### 3.3 Critères de bascule en crise cyber

Un incident majeur bascule en **crise cyber** quand l'impact dépasse la sphère technique et touche le fonctionnement de l'organisation dans ses dimensions business, réputationnelle, réglementaire ou stratégique.

Les critères de bascule incluent un impact business significatif (production arrêtée, perte de chiffre d'affaires mesurable, clients impactés), une exposition médiatique (revendication sur un leak site, article de presse, tendance sur les réseaux sociaux), un impact réglementaire (notification CNIL obligatoire, notification ANSSI en tant qu'OIV/OSE, enquête réglementaire potentielle), une demande d'extorsion (la rançon est un élément de crise par nature — elle implique des décisions stratégiques, juridiques et éthiques), une atteinte à la sécurité physique (compromission de systèmes OT/SCADA dans un environnement industriel à risque), ou un dépassement de la capacité de réponse technique (l'équipe IR est submergée, l'incident évolue plus vite que la capacité d'analyse).

#### 3.4 Gouvernance technique vs gouvernance exécutive

L'activation de la crise crée deux niveaux de gouvernance qui doivent fonctionner en parallèle sans se mélanger.

La **cellule technique** est pilotée par l'IR lead. Elle comprend les analystes forensic, les analystes logs/réseau, l'analyste CTI, les administrateurs systèmes et réseaux, et le prestataire PRIS. Elle gère l'investigation technique, les actions de confinement et d'éradication, la collecte de preuves, et la production des IoC. Elle travaille en heures et en minutes.

La **cellule de crise exécutive** est pilotée par le DG ou son représentant mandaté. Elle comprend le RSSI (interface entre les deux cellules), le directeur juridique, le directeur de la communication, le DRH, le DPO, le directeur des opérations/métiers, et le DSI. Elle gère les décisions stratégiques (couper ou ne pas couper la production, payer ou ne pas payer la rançon), la communication (interne et externe), le juridique (notifications réglementaires, dépôt de plainte), et l'allocation de ressources.

Les deux cellules communiquent via des SitRep (Situation Reports) réguliers — toutes les 4 à 6 heures en phase aiguë, 1 à 2 fois par jour en phase de stabilisation. Le RSSI est la charnière entre les deux : il traduit la situation technique en termes compréhensibles par la direction, et il répercute les décisions stratégiques vers la cellule technique. Quand cette articulation fonctionne, la réponse est fluide. Quand elle dysfonctionne (le DG veut comprendre les Event IDs, l'analyste forensic conteste la décision de communication), la réponse patine.

#### 3.5 Temporalités divergentes et objectifs parfois contradictoires

La cellule technique et la cellule exécutive ne travaillent pas dans le même temps, et leurs objectifs peuvent temporairement diverger.

La technique veut **comprendre avant d'agir**. L'idéal technique serait de cartographier complètement la compromission, d'identifier tous les mécanismes de persistance, et de planifier une éradication chirurgicale — ce qui peut prendre des jours. Observer l'attaquant sans l'alerter (pour comprendre l'étendue complète) est parfois plus productif que le confiner immédiatement.

Le business veut **agir avant de comprendre**. La direction veut redémarrer la production, rassurer les clients, communiquer que « tout est sous contrôle ». Chaque jour d'arrêt coûte des centaines de milliers d'euros, les clients menacent de partir, et le conseil d'administration demande des comptes.

L'arbitrage entre ces temporalités n'est pas technique — il est stratégique. Il appartient à la direction, informée par l'équipe technique. Le rôle de l'IR lead est de formuler des options claires avec leurs risques respectifs (voir Ch.26 — Décider sous incertitude), pas de prendre seul la décision.

> **Bonne pratique :** Quand les objectifs divergent, la question arbitrale est : « Quelle décision serions-nous le plus en difficulté de défendre a posteriori si elle s'avérait mauvaise ? » Redémarrer trop vite et être réinfecté est plus difficile à défendre que mettre 2 jours de plus à reprendre la production. Cette asymétrie des regrets guide la prise de décision.

#### 3.6 Fil rouge — BLACKTIDE : la bascule en crise

> **🔍 BLACKTIDE — Épisode 3**
>
> Samedi 15 mars, 02h00. L'investigation initiale progresse. En 3 heures, l'équipe a établi :
> - DC01, DC02 et DC03 montrent des traces de PsExec et de modification GPO.
> - Le ransomware PhantomCrypt est en cours de déploiement via GPO — les serveurs de fichiers de 3 sites commencent à chiffrer.
> - Le trafic sortant vers le domaine C2 `update-srv-infra[.]xyz` est identifié (corrélation avec le cours Cartographie des Écosystèmes — c'est le même domaine).
> - Le volume d'exfiltration est inconnu mais des flux suspects vers AWS S3 sont repérés dans les logs proxy.
>
> Nadia évalue : ce n'est plus un incident P2. C'est un incident P1 avec probable bascule en crise. Elle appelle Marc (RSSI) à 02h15 :
>
> « Marc, on a une compromission des 3 DC, un ransomware en cours de déploiement sur les serveurs de fichiers de Fos, Lyon et Cologne, et une exfiltration probable vers un serveur externe. Le site OIV est touché. Je recommande la bascule en crise. »
>
> Marc active la cellule de crise exécutive pour 06h00 le samedi matin. Les deux gouvernances — technique et exécutive — sont désormais actives en parallèle.
>
> À 02h30, Nadia produit le premier SitRep :
>
> **SITREP #1 — BLACKTIDE — 15/03/2026 02h30**
> - **Ce qu'on sait :** 3 DC compromis, ransomware en cours de déploiement (3 sites touchés dont OIV Fos), trafic C2 identifié.
> - **Ce qu'on ne sait pas :** Étendue complète de la compromission. Volume de données exfiltrées. Identité de l'attaquant. Durée de présence dans le réseau.
> - **Ce qu'on fait :** Investigation en cours. Surveillance renforcée. Préparation des options de confinement.
> - **Ce qu'on envisage :** Confinement réseau des 3 sites impactés. Mobilisation PRIS. Notification ANSSI.
> - **Ce dont on a besoin :** Décision de confinement (impact production). Autorisation de notification ANSSI. Confirmation de la mobilisation du prestataire PRIS.

---

### Chapitre 4 — Référentiels, modèles et cadres méthodologiques

#### 4.1 NIST SP 800-61 — le cadre de référence international

Le NIST Special Publication 800-61 (Computer Security Incident Handling Guide), publié par le National Institute of Standards and Technology américain, est le cadre de référence le plus largement adopté pour structurer la réponse à incident. Sa dernière révision majeure (Rev. 2) organise l'IR en quatre phases.

La **phase 1 — Preparation** couvre tout ce qui doit être en place avant l'incident : équipe, outils, processus, formation, exercices. Le NIST insiste sur le fait que la qualité de la réponse est directement proportionnelle à la qualité de la préparation — un constat que la Partie II de ce cours développe en 6 chapitres.

La **phase 2 — Detection & Analysis** couvre la détection de l'incident, sa confirmation, sa classification, sa notification aux parties prenantes, et l'analyse initiale. Le NIST distingue les vecteurs d'attaque (email, web, media amovible, attrition, etc.) et fournit des indicateurs de classification.

La **phase 3 — Containment, Eradication & Recovery** regroupe trois activités que d'autres cadres séparent. Le confinement stoppe la progression de l'attaquant. L'éradication supprime les mécanismes de compromission. La récupération restaure les systèmes à un état sûr. Le NIST reconnaît que ces trois activités sont souvent itératives et parallèles.

La **phase 4 — Post-Incident Activity** couvre le retour d'expérience, la capitalisation, et l'amélioration continue.

**Forces du NIST 800-61 :** structurant, adopté mondialement, applicable à toutes tailles d'organisation, régulièrement mis à jour. **Limites :** très conceptuel (peu de détails techniques opérationnels), centré contexte américain (les obligations réglementaires européennes ne sont pas couvertes), et pas de traitement explicite de la dimension « crise » (la gouvernance exécutive, la communication de crise, et la pression médiatique ne sont pas dans le périmètre du document).

#### 4.2 SANS PICERL — les 6 phases

Le modèle SANS (Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned) est plus granulaire que le NIST sur la distinction entre Containment, Eradication et Recovery — trois phases que le NIST regroupe. Cette granularité est utile pédagogiquement et opérationnellement : les trois phases mobilisent des compétences, des outils, et des temporalités différentes.

Le modèle SANS est la base des formations SANS les plus reconnues en IR : FOR508 (Advanced Incident Response, Threat Hunting, and Digital Forensics), FOR500 (Windows Forensic Analysis), et FOR578 (Cyber Threat Intelligence). Il est profondément ancré dans la communauté des praticiens.

**Limite principale :** la linéarité implicite du modèle (P→I→C→E→R→L) ne reflète pas la réalité itérative de l'IR. En pratique, on revient constamment en arrière : on identifie de nouveaux systèmes compromis pendant l'éradication (retour à l'identification), on découvre de nouvelles persistances pendant la recovery (retour à l'éradication), et les lessons learned commencent dès les premières heures de l'incident (pas seulement après la clôture).

#### 4.3 ISO 27035 — le cadre normatif

La norme ISO 27035 (Information Security Incident Management), en trois parties, fournit un cadre formel pour la gestion des incidents dans un contexte de système de management de la sécurité de l'information (SMSI) conforme à ISO 27001. Elle est plus structurée sur la gouvernance et la documentation que les cadres NIST/SANS, mais moins technique.

ISO 27035 est pertinente pour les organisations certifiées ISO 27001 qui doivent intégrer la gestion des incidents dans leur SMSI, et pour les organisations qui ont besoin d'un cadre normatif reconnu pour justifier leur approche auprès d'auditeurs ou de régulateurs.

#### 4.4 Cadre ANSSI, CERT-FR et PRIS

Le cadre français de la réponse à incident s'articule autour de plusieurs composantes.

L'**ANSSI** (Agence Nationale de la Sécurité des Systèmes d'Information) est l'autorité nationale en matière de cybersécurité. Elle opère le **CERT-FR**, qui fournit un service de réponse aux incidents pour les administrations et les OIV, publie des avis de sécurité et des alertes, et coordonne la réponse aux incidents d'ampleur nationale. Le CERT-FR peut déployer des équipes spécialisées (notamment en environnement OT/SCADA) en appui des organisations victimes.

Le référentiel **PRIS** (Prestataires de Réponse aux Incidents de Sécurité) définit les exigences de qualification pour les prestataires d'IR. La version 3.2, publiée en octobre 2025, couvre désormais cinq activités qualifiables : recherche d'indicateurs de compromission, investigation numérique (forensic), analyse de codes malveillants, pilotage et coordination des investigations, et — nouveauté de la v3.2 — gestion de crise d'origine cyber. Cette dernière activité, ajoutée après un appel à commentaires terminé en mai 2025, permet à l'ANSSI de délivrer des qualifications attestant la capacité d'un prestataire à gérer la dimension crise (pas seulement la dimension technique) d'un incident cyber.

Les **obligations de notification** dans le cadre français sont multiples. Les OIV (Opérateurs d'Importance Vitale) doivent notifier l'ANSSI dans les délais prescrits par les arrêtés sectoriels. La directive NIS 2, en cours de transposition en France via la « Loi relative à la résilience des infrastructures critiques et au renforcement de la cybersécurité » (dite « Loi Résilience ») — adoptée en commission spéciale à l'Assemblée nationale en septembre 2025, promulgation attendue début 2026 —, imposera des obligations de notification aux entités essentielles (notification initiale sous 24h, notification complète sous 72h) et aux entités importantes. Le périmètre est considérablement élargi par rapport à NIS 1 : environ 15 000 entités seront concernées en France, contre quelques centaines sous le régime actuel.

L'articulation avec les **forces de l'ordre** passe par le dépôt de plainte auprès du procureur de la République, qui peut être traité par l'OCLCTIC (Office Central de Lutte contre la Criminalité liée aux Technologies de l'Information et de la Communication), le C3N (Centre de lutte Contre les Criminalités Numériques, Gendarmerie), la BL2C (Brigade de Lutte contre la Cybercriminalité, Préfecture de Police de Paris), ou la JUNALCO (Juridiction Nationale de Lutte contre la Criminalité Organisée, parquet de Paris — section J3 cybercriminalité).

#### 4.5 Kill Chain, Diamond Model et ATT&CK comme outils d'investigation

Ces cadres ne sont pas des « modèles IR » au sens de NIST ou SANS — ce sont des outils que l'investigateur utilise pendant la réponse pour structurer ses observations et ses hypothèses.

La **Cyber Kill Chain** (Lockheed Martin) structure le raisonnement sur la progression de l'attaque en 7 étapes (Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command & Control, Actions on Objectives). Elle est utile pour situer l'attaque dans son cycle de vie : si l'attaquant en est à « Actions on Objectives » (exfiltration, chiffrement), c'est qu'il a traversé toutes les étapes précédentes — et l'investigation doit les reconstituer.

Le **Diamond Model** (adversary, capability, infrastructure, victim) structure le raisonnement sur l'attribution et le contexte. Pour chaque événement de l'intrusion, l'analyste identifie l'adversaire (qui ?), la capacité utilisée (quel outil, quelle technique ?), l'infrastructure employée (quel C2, quel hébergement ?), et la victime ciblée (quel système, quelle donnée ?).

La **matrice MITRE ATT&CK** fournit un vocabulaire commun pour décrire les TTP (Tactics, Techniques, and Procedures) observées pendant l'investigation. Chaque étape du chemin d'attaque est mappée sur les tactiques ATT&CK (Initial Access, Execution, Persistence, etc.), ce qui normalise le rapport, facilite le partage avec la communauté, et oriente la remédiation (pour chaque technique utilisée : quelle détection ou quelle mesure préventive aurait pu la contrer ?).

#### 4.6 Intérêt et limites des modèles

Aucun modèle ne reflète fidèlement la réalité d'un incident majeur. Les phases ne sont pas séquentielles mais itératives et parallèles : on contient pendant qu'on investigue, on investigue pendant qu'on éradique, on découvre de nouveaux problèmes pendant la reconstruction. L'incident avance sur plusieurs fronts simultanément, et les « phases » des modèles sont des repères intellectuels pour structurer la pensée, pas des check-lists rigides à suivre dans l'ordre.

Le danger des modèles est de créer une illusion de contrôle linéaire. L'analyste qui pense « je suis en phase de Containment, donc je ne fais pas d'Eradication » se trompe — si une opportunité d'éradiquer se présente pendant le confinement (par exemple, un mécanisme de persistance trivial à supprimer), il serait absurde de ne pas la saisir sous prétexte que « ce n'est pas la bonne phase ».

Les modèles doivent être connus, intériorisés, puis adaptés au contexte. Ils sont des garde-fous contre l'oubli (« avons-nous pensé aux lessons learned ? ») et des outils de communication (« nous sommes en phase de Containment, voici ce que cela signifie »), pas des carcans.

#### 4.7 Fil rouge — BLACKTIDE : le cadre opérationnel

> **🔍 BLACKTIDE — Épisode 4**
>
> L'équipe IR d'Arvantis utilise le NIST 800-61 comme référence procédurale. L'IRP interne reprend les 4 phases NIST et les décline en actions concrètes. Le mapping ATT&CK est utilisé comme grille de lecture des TTP observées au fil de l'investigation — chaque technique identifiée est documentée avec son ID ATT&CK dans le journal d'incident.
>
> Le prestataire PRIS sous contrat, CyberForce, utilise son propre cadre méthodologique (basé sur SANS PICERL), compatible avec le cadre interne d'Arvantis. L'articulation a été définie contractuellement : CyberForce apporte l'expertise forensic et l'expérience d'incidents similaires, l'équipe interne apporte la connaissance du SI et du contexte métier. L'IR lead reste Nadia (interne) — le consultant senior de CyberForce est en support, pas en pilotage.
>
> L'ANSSI est notifiée à 08h00 (obligation OIV — site de Fos-sur-Mer). Le CERT-FR accuse réception et propose un appui : déploiement d'une équipe spécialisée OT pour auditer le réseau SCADA de Fos, prévu pour lundi.

---

## PARTIE II — PRÉPARATION : AVANT QUE L'INCIDENT N'ARRIVE

*La qualité de la réponse est déterminée à 80 % par la qualité de la préparation. Cette partie traite ce que la plupart des organisations négligent — et ce qui fait la différence le jour J.*

---

### Chapitre 5 — Pourquoi la préparation détermine tout

#### 5.1 Le constat récurrent des retex

Dans la quasi-totalité des post-mortems d'incidents majeurs, les problèmes les plus graves ne sont pas techniques mais organisationnels. L'IRP existait mais n'avait jamais été testé — le jour J, personne ne savait où le trouver ni comment l'appliquer. Les contacts d'escalade étaient obsolètes — le RSSI avait changé de numéro 6 mois plus tôt. Les logs critiques n'étaient pas collectés — le PowerShell script block logging n'était pas activé, rendant l'investigation sur le mouvement latéral quasi impossible. Les sauvegardes étaient sur le même réseau que les serveurs de production — le ransomware les a chiffrées en même temps. Le canal de communication de crise n'était pas prévu — quand le serveur de messagerie a été chiffré, l'équipe s'est retrouvée sans moyen de communiquer.

Ces défaillances ne sont pas des « malchances » — ce sont des défauts de préparation identifiables et corrigeables avant l'incident. Chaque euro investi dans la préparation en économise dix ou cent en réponse.

#### 5.2 Les trois dimensions de la préparation

La préparation technique couvre les outils, les logs, les sauvegardes, la capacité d'isolation réseau, et les accès d'urgence. La préparation organisationnelle couvre les processus (IRP, playbooks, escalade), les rôles (qui fait quoi), les contrats (prestataire PRIS, assurance, exercices), et les relations (ANSSI, forces de l'ordre, CERT sectoriel). La préparation humaine couvre la formation (les analystes savent-ils utiliser Volatility ?), les réflexes (le SOC sait-il qu'il ne faut pas redémarrer un serveur compromis ?), et la capacité à fonctionner sous stress (l'IR lead a-t-elle déjà géré un incident majeur, même en exercice ?).

Négliger une seule dimension rend les deux autres insuffisantes. Un SIEM parfaitement configuré ne sert à rien si personne ne sait lire les alertes. Un IRP impeccable ne sert à rien si les logs ne sont pas collectés. Une équipe brillante ne sert à rien si elle n'a pas les outils pour investiguer.

#### 5.3 Le plan de réponse à incident (IRP)

L'IRP est le document fondateur de la capacité IR d'une organisation. Il doit contenir le périmètre d'application (quels systèmes, quels sites, quels processus sont couverts), la taxonomie des incidents adoptée (cohérente avec la classification du Ch.1), les critères de classification et de gravité (P1 à P4, avec des critères objectifs et des exemples), les critères de bascule en crise (repris du Ch.3), les rôles et contacts (à jour — c'est le point le plus souvent défaillant), les playbooks par type d'incident (ou pointeurs vers les playbooks séparés — Ch.7), les procédures d'escalade (qui appelle qui, dans quel ordre, avec quels critères), les modèles de communication pré-rédigés (premier message aux employés, premier SitRep à la direction, notification ANSSI, notification CNIL), les listes de diffusion (qui doit être informé à chaque niveau de gravité), et les arbres de décision (couper le réseau ? notifier l'ANSSI ? activer l'assurance ?).

Un IRP opérationnel fait 10 à 20 pages, pas 85. Il est stocké hors du SI principal (version papier, clé USB, cloud personnel du RSSI) car le SI peut être indisponible pendant l'incident. Il est mis à jour au minimum semestriellement et après chaque incident. Et il est testé en exercice au moins une fois par an (Ch.10).

> **Piège fréquent :** L'IRP « vitrine » — un document de 100 pages, magnifiquement rédigé, validé par la direction, rangé dans un tiroir, et jamais lu par les opérationnels. Le jour de l'incident, personne ne l'ouvre. Un IRP efficace est court, concret, et connu de tous les acteurs.

#### 5.4 Fil rouge — BLACKTIDE : l'état de préparation d'Arvantis

> **🔍 BLACKTIDE — Épisode 5**
>
> L'IRP d'Arvantis existe — un document de 85 pages rédigé 2 ans plus tôt par un consultant externe, validé par la direction, stocké sur SharePoint. Il n'a jamais été testé en conditions réelles. Le numéro du prestataire PRIS est à jour. Celui de l'ANSSI aussi. Le numéro personnel du DPO a changé il y a 3 mois — l'IRP n'a pas été mis à jour. Nadia l'a dans son téléphone — elle le retrouve. Par chance.
>
> L'IRP couvre les grandes lignes (escalade, classification, notification) mais ne contient pas de playbook ransomware détaillé. Il ne mentionne pas la procédure de double reset du krbtgt. Il ne traite pas l'articulation IT/OT. Et surtout : il est stocké sur SharePoint, qui est hébergé sur l'infrastructure Microsoft 365 d'Arvantis — si l'attaquant avait compromis le tenant M365, l'IRP aurait été inaccessible.

---

### Chapitre 6 — Gouvernance et organisation IR

#### 6.1 L'équipe IR : composition et rôles

L'**IR lead** (ou incident commander) coordonne l'ensemble de la réponse. Il maintient la vision d'ensemble, assigne les questions aux analystes, arbitre les priorités, fait l'interface avec la direction et le RSSI, et documente les décisions. Dans une PME, c'est souvent le RSSI lui-même. Dans un grand groupe, c'est un rôle dédié au sein du CSIRT.

Les **analystes forensic** mènent l'investigation technique sur les endpoints : acquisition de preuves (RAM, disques, artefacts), analyse des artefacts système, analyse de malware first-pass, et production des IoC. Compétences requises : maîtrise des outils forensic (KAPE, Velociraptor, Volatility, FTK Imager), connaissance approfondie des artefacts Windows et Linux.

Les **analystes logs/réseau** analysent les logs centralisés (SIEM), les flux réseau (pare-feu, proxy, DNS, NDR), et construisent la timeline par corrélation des sources. Compétences requises : maîtrise du SIEM (requêtes SPL, KQL, ou ELK), compréhension des protocoles réseau, capacité de corrélation multi-sources.

L'**analyste CTI** contextualise la menace : identification de l'adversaire (groupe, plateforme RaaS, TTP connues), enrichissement des IoC (hash, domaines, IP — sont-ils connus ? associés à quelle campagne ?), et anticipation des comportements (si c'est un affilié PhantomCrypt, quels mécanismes de persistance sont typiques ?). Renvoi vers le cours CTI et le cours Cartographie des Écosystèmes.

Le **représentant IT/infra** apporte la connaissance du SI (architecture, systèmes critiques, dépendances), exécute les actions techniques décidées par l'IR lead (isolation réseau, reset de comptes, restauration), et identifie les impacts opérationnels des actions proposées.

Le **RSSI** fait l'interface entre la cellule technique et la direction. Il traduit la situation technique en termes business, valide les décisions à impact stratégique, et porte la responsabilité managériale de la réponse.

Ces rôles peuvent être portés par 3 personnes dans une PME ou 15 dans un grand groupe. Ce qui compte n'est pas le nombre de personnes mais le fait que chaque fonction soit assignée explicitement à quelqu'un qui sait ce qu'on attend de lui.

#### 6.2 CSIRT interne vs prestataire PRIS

La décision entre réponse interne et mobilisation d'un prestataire qualifié PRIS dépend de plusieurs critères. La nature de l'incident (un phishing simple peut être traité en interne ; un ransomware avec compromission de l'AD nécessite presque toujours un PRIS), les compétences disponibles (l'organisation a-t-elle un forensicien capable d'analyser un dump mémoire de DC à 3h du matin un samedi ?), la charge (même si les compétences existent, l'équipe peut être submergée), le besoin d'indépendance (pour la plainte pénale, un rapport d'un tiers qualifié est plus crédible), et les exigences d'assurance (certaines polices imposent le recours à un PRIS de leur liste).

Le prestataire PRIS ne connaît pas le SI de l'organisation. Le temps d'on-boarding (comprendre l'architecture, les accès, les noms des serveurs, les personnes à contacter) est incompressible et peut prendre plusieurs heures, voire une demi-journée. Ce temps doit être anticipé : un document de synthèse du SI (architecture réseau, liste des systèmes critiques, comptes d'administration, outils de sécurité déployés) doit être préparé à l'avance et remis au PRIS dès son arrivée.

Le référentiel PRIS v3.2 de l'ANSSI (octobre 2025) qualifie les prestataires sur cinq activités : recherche d'indicateurs de compromission, investigation numérique, analyse de codes malveillants, pilotage et coordination des investigations, et gestion de crise d'origine cyber.

#### 6.3 Chaîne d'escalade et RACI

La chaîne d'escalade définit qui appelle qui, dans quel ordre, avec quels critères de déclenchement. Elle doit être simple (pas plus de 3 niveaux pour atteindre le décideur), redondante (si le contact principal ne répond pas, qui est le suppléant ?), et testée régulièrement (voir Ch.10).

Le RACI de l'IR (Responsible, Accountable, Consulted, Informed) doit être défini avant l'incident. Qui est responsable de la décision de confinement réseau ? (typiquement : IR lead propose, RSSI valide). Qui est responsable de la notification ANSSI ? (typiquement : RSSI). Qui est responsable de la communication interne ? (typiquement : direction de la communication, validée par le RSSI et le juridique). L'ambiguïté des rôles pendant un incident est une source majeure de paralysie (personne ne décide) ou de décisions contradictoires (deux personnes décident des choses incompatibles). Un RACI type est proposé en Annexe G.

#### 6.4 Modèle de permanence et astreinte

La réalité opérationnelle de l'IR est que l'incident n'arrive jamais à un moment pratique. L'alerte tombe le vendredi soir, l'expert AD est en vacances à l'étranger, le RSSI est dans un avion. Le modèle de permanence doit anticiper ces situations : astreinte formalisée (qui est joignable 24/7, avec quel délai de réponse), suppléances (si l'astreinte primaire ne répond pas dans les 15 minutes, qui prend le relais), et procédure de rappel d'effectifs (comment mobiliser l'équipe complète un dimanche matin).

La fatigue est un enjeu sous-estimé. Un incident majeur dure des jours, parfois des semaines. Les premières 24-48 heures sont intenses (adrénaline, urgence), mais au-delà, la fatigue dégrade la qualité des décisions, augmente le risque d'erreur, et peut conduire à des conflits interpersonnels. La rotation des équipes (shifts de 8 à 12 heures maximum, avec passage de relais structuré) est un enjeu de santé ET de qualité de réponse.

#### 6.5 Fil rouge — BLACKTIDE : la mobilisation

> **🔍 BLACKTIDE — Épisode 6**
>
> Nadia (IR lead) est d'astreinte ce week-end — elle répond en 3 minutes. Marc (RSSI) est d'astreinte — il répond en 2 sonneries. Le prestataire PRIS CyberForce est mobilisé à 23h30 — le consultant senior forensic, Thomas Hartmann, et un consultant spécialiste AD, Léa Chen, seront sur site samedi à 08h15 (SLA contractuel : 12h le week-end).
>
> L'expert AD interne d'Arvantis, Youssef Benmoussa, est en congé en Tunisie. Il est injoignable par téléphone (pas de réseau dans la zone). Il sera briefé par visioconférence dimanche matin quand il retrouvera du réseau. En attendant, Léa Chen (PRIS) couvrira l'analyse AD.
>
> L'analyste SOC N2, Karim, est en poste depuis 14h (début de shift à 14h). À 02h, cela fait 12 heures qu'il travaille. Nadia lui demande de rester encore 2 heures pour le passage de relais au N2 suivant, puis de dormir. L'analyste suivant, Fatima Zeroual, prend le relais SOC à 04h.

---

### Chapitre 7 — Playbooks et procédures opérationnelles

#### 7.1 Qu'est-ce qu'un playbook IR

Un playbook IR est un document opérationnel, court (5 à 10 pages maximum), qui décrit les actions concrètes à mener pour un type d'incident spécifique. Ce n'est pas l'IRP (qui est le cadre général de la capacité IR) — c'est la procédure détaillée pour un cas précis, avec des actions numérotées, des responsables identifiés, des seuils de décision, et des pointeurs vers les outils et commandes à utiliser.

Le playbook est le document que l'analyste ouvre à 3h du matin quand il est fatigué et stressé. Il doit être immédiatement actionnable : pas de prose de 3 pages avant la première action, pas de jargon inutile, pas de renvois vers 10 autres documents. L'action 1 doit pouvoir être exécutée dans les 5 premières minutes.

#### 7.2 Playbooks essentiels

Chaque organisation doit disposer au minimum des playbooks suivants, adaptés à son contexte.

**Playbook phishing** : trigger (alerte utilisateur ou détection email malveillant), actions immédiates (extraction des IoC : URL, pièce jointe, expéditeur ; recherche dans les boîtes mail de tous les destinataires ; isolation du poste de l'utilisateur qui a cliqué), investigation (le lien a-t-il été cliqué ? les credentials ont-elles été saisies ? le malware a-t-il été exécuté ?), confinement (blocage du domaine/hash au niveau proxy/EDR, reset du mot de passe si credentials compromises), et communication (notification aux utilisateurs touchés).

**Playbook ransomware** : trigger (détection EDR ou découverte de fichiers chiffrés), actions immédiates (isolation réseau des systèmes touchés — NE PAS éteindre avant collecte), évaluation (quel variant ? quel périmètre ? les sauvegardes sont-elles intactes ? le DC est-il compromis ?), confinement réseau (voir Ch.23), collecte forensic (RAM + triage KAPE avant tout reset), notification (ANSSI si OIV, CNIL si données personnelles), et décision sur la rançon (voir Ch.32).

**Playbook compromission de compte** : trigger (alerte SIEM sur comportement anormal, notification de geo-impossible travel, signalement utilisateur), actions (désactivation immédiate du compte, reset mot de passe, révocation des sessions actives et tokens OAuth, recherche d'activité suspecte : règles de forwarding email, accès aux données, création de comptes, modifications de configuration).

**Playbook malware** : trigger (détection EDR/antivirus), actions (isolation du poste via EDR containment, collecte du sample pour analyse, soumission sandbox, recherche de propagation latérale — le même hash est-il détecté sur d'autres machines ?), classification (commodity malware vs ciblé, infostealer vs RAT vs ransomware).

**Playbook exfiltration de données** : trigger (alerte DLP, volume anormal de trafic sortant, notification externe), investigation (quelles données ? quel volume ? vers quelle destination ?), confinement (blocage du canal d'exfiltration), et notification (CNIL si données personnelles, sous 72h).

**Playbook compromission cloud** : trigger (alerte Entra ID / CloudTrail), investigation (Sign-in Logs pour les accès anormaux, Unified Audit Log pour les actions, app registrations suspectes, conditional access policies modifiées), confinement (révocation de tokens, reset MFA, désactivation des app registrations suspectes).

Les playbooks détaillés avec les commandes concrètes sont en Annexe E.

#### 7.3 Concevoir un bon playbook

Structure type d'un playbook opérationnel :

**En-tête :** nom du playbook, version, date de dernière mise à jour, auteur, conditions de déclenchement (trigger).

**Actions immédiates** (0-15 minutes) : ce que l'analyste de garde doit faire sans attendre de validation. Chaque action a un responsable et un livrable.

**Actions d'investigation** (15 min - 4 heures) : les vérifications et analyses nécessaires pour qualifier l'incident et décider du confinement. Inclut les commandes concrètes (requêtes SIEM, commandes EDR, scripts de collecte).

**Actions de confinement** : les mesures de limitation de la progression, avec les critères de décision (quand isoler, quand couper, quand observer).

**Critères d'escalade** : à quel moment et vers qui escalader si la gravité s'avère supérieure à la classification initiale.

**Actions de communication** : qui informer, quand, avec quel message type.

**Actions de clôture** : vérifications post-résolution, documentation, et lien vers le RETEX.

#### 7.4 Maintenir les playbooks vivants

Un playbook non testé est un playbook mort. Les playbooks doivent être testés en exercice (Ch.10), révisés après chaque incident où ils ont été utilisés (le RETEX identifie les actions manquantes ou inadaptées), et mis à jour quand l'environnement change (nouveau SIEM, nouvel EDR, changement d'architecture, nouveau type de menace).

Fréquence de révision recommandée : après chaque utilisation en incident réel, après chaque exercice, et au minimum une fois par an même sans utilisation.

#### 7.5 Fil rouge — BLACKTIDE : le playbook ransomware insuffisant

> **🔍 BLACKTIDE — Épisode 7**
>
> Arvantis a un playbook ransomware — incomplet. Il décrit les actions de confinement réseau (isolation VLAN, coupure Internet) mais ne couvre pas le cas d'un AD compromis en profondeur (pas de procédure de double reset krbtgt, pas de procédure de reconstruction DC). Il ne mentionne pas l'articulation avec l'ANSSI en cas d'OIV impacté. Il ne traite pas le cas spécifique de l'environnement OT (comment confiner le réseau sans arrêter les automates SCADA ?). Et il n'a jamais été testé en exercice.
>
> Nadia l'utilise comme base mais doit improviser sur environ 40 % des actions. Elle note dans le journal : « Playbook ransomware utilisé — lacunes identifiées : pas de procédure AD compromis, pas de volet OT, pas de volet notification OIV. À mettre à jour en RETEX. »

---

### Chapitre 8 — Préparation technique : outillage et télémétrie

#### 8.1 Les outils qui doivent être en place AVANT l'incident

**EDR (Endpoint Detection and Response)** : déployé sur TOUS les endpoints — pas 85 %, pas 92 %, tous. Chaque machine non couverte est un angle mort dans lequel l'attaquant peut se cacher sans être détecté. L'EDR est le premier capteur de l'investigation (il fournit la telemetry qui reconstitue les actions de l'attaquant) et le premier outil de confinement (network containment, kill process). Les leaders du marché en 2025-2026 incluent CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne, et Palo Alto Cortex XDR. Le choix dépend du contexte (environnement, budget, intégration avec le SIEM), mais la couverture à 100 % est non négociable.

**SIEM (Security Information and Event Management)** : collecte centralisée des logs critiques avec capacité de recherche et de corrélation. Les sources minimales à collecter : Windows Event Logs (Security, System, PowerShell, Sysmon si déployé), logs Active Directory (réplication, modifications d'objets), logs pare-feu (flux autorisés et refusés), logs proxy (URLs, user-agents, volumes), logs DNS (résolutions), logs VPN (connexions), et logs des solutions de sécurité (EDR, antivirus). Les plateformes courantes : Splunk, Microsoft Sentinel, Elastic Security (ELK), QRadar, Chronicle (Google). Le choix dépend du volume de logs, du budget, et des compétences disponibles.

**NDR (Network Detection and Response)** : pas obligatoire mais extrêmement précieux. Le NDR capture et analyse le trafic réseau en temps réel, détecte les anomalies (beaconing, exfiltration, mouvement latéral), et fournit une visibilité que les logs endpoint et SIEM ne donnent pas (notamment sur les systèmes sans EDR — serveurs legacy, équipements réseau, systèmes OT).

**Outils de collecte forensic pré-packagés** : clés USB bootables contenant KAPE (collecte automatisée d'artefacts Windows), Velociraptor (collecte et hunting à grande échelle), DumpIt ou WinPmem (acquisition mémoire), et des scripts de triage personnalisés. Ces kits doivent être prêts à l'emploi, testés, et accessibles physiquement (pas sur un partage réseau qui sera chiffré).

#### 8.2 Rétention des logs

La durée de rétention des logs détermine la profondeur de l'investigation. Le dwell time médian (temps entre la compromission et la détection) est de 10 à 15 jours pour les ransomwares, mais peut atteindre des mois pour l'espionnage. Si les logs ne sont conservés que 30 jours et que l'attaquant est dans le réseau depuis 5 semaines, les traces du patient zéro sont perdues.

Minimum recommandé : 6 mois de rétention sur le SIEM chaud (recherche immédiate), 12 mois en stockage froid (archivage consultable). Pour les environnements à risque élevé (OIV, secteur financier, défense) : 12 mois chaud, 24 mois froid.

Le cas critique de Microsoft 365 : la rétention des Unified Audit Logs dépend de la licence. En E3 (la licence la plus courante en entreprise), la rétention est de 180 jours (améliorée par Microsoft en 2023, contre 90 jours auparavant pour certains types de logs). En E5, la rétention peut aller jusqu'à 365 jours. Cette différence est critique pour l'investigation — et elle est souvent découverte trop tard, au moment de l'incident.

#### 8.3 Horodatage, sauvegardes, isolation et accès d'urgence

**Synchronisation NTP :** si les horloges des machines ne sont pas synchronisées, la corrélation des événements entre sources est impossible. La synchronisation NTP sur tous les systèmes est un prérequis trivial mais souvent négligé.

**Sauvegardes :** les sauvegardes doivent être segmentées du réseau principal (pas un NAS sur le même VLAN — le ransomware le chiffrera en même temps que les serveurs), testées régulièrement (une sauvegarde non testée est une promesse non vérifiée), et idéalement immuables (stockage WORM, cloud avec versioning et MFA delete protection) ou offline (bandes magnétiques, rotation hebdomadaire). Le ransomware cible systématiquement les sauvegardes — c'est même souvent sa première cible après la compromission de l'AD, car l'attaquant sait que la volonté de payer la rançon est directement proportionnelle à l'indisponibilité des sauvegardes.

**Capacité d'isolation réseau :** VLAN de quarantaine pré-configuré, ACL pare-feu prêtes à être activées (pas à écrire en urgence à 3h du matin), capacité d'isolation via EDR (network containment à distance), et éventuellement un kill switch réseau (coupure totale de l'accès Internet en un clic — procédure documentée et testée).

**Comptes et accès d'urgence :** comptes d'administration « break glass » (non synchronisés avec l'AD principal, stockés de manière sécurisée — coffre-fort physique, gestionnaire de mots de passe hors SI), accès console aux équipements réseau (si le réseau est compromis, les accès in-band via SSH ou HTTPS peuvent être inaccessibles), et accès physique aux datacenters (badges, clés).

#### 8.4 Fil rouge — BLACKTIDE : forces et faiblesses techniques

> **🔍 BLACKTIDE — Épisode 8**
>
> **Forces :** EDR CrowdStrike Falcon déployé sur 92 % du parc (les 3 DC compromis sont couverts — c'est ce qui a permis la détection). SIEM Splunk avec 9 mois de rétention (suffisant pour remonter au patient zéro à J-35). Horodatage NTP synchronisé sur tout le parc. Logs pare-feu conservés 12 mois.
>
> **Faiblesses :** 8 % du parc sans EDR (postes legacy, serveurs OT, équipements réseau — autant d'angles morts). Pas de NDR (la visibilité réseau est limitée aux logs proxy et pare-feu). Microsoft 365 en licence E3 (rétention UAL de 180 jours — suffisant pour cet incident, mais pas pour un espionnage long terme). Sauvegardes quotidiennes sur NAS réseau, sur le même VLAN que les serveurs de fichiers (elles seront partiellement chiffrées par le ransomware). Sauvegardes hebdomadaires sur bandes offline (intactes — seule sauvegarde exploitable, mais avec 6 jours de perte de données). Comptes break glass : inexistants. PowerShell script block logging : non activé sur tous les postes (activé uniquement sur les serveurs — lacune sur les postes de travail).

---

### Chapitre 9 — Préparation juridique, réglementaire et contractuelle

#### 9.1 Obligations de notification

Le paysage réglementaire français impose plusieurs obligations de notification en cas d'incident cyber, avec des délais et des destinataires différents.

**ANSSI — OIV :** les Opérateurs d'Importance Vitale doivent notifier l'ANSSI dans les délais prescrits par les arrêtés sectoriels (variable selon le secteur, mais typiquement « sans délai » pour les incidents majeurs). La notification est obligatoire, et le non-respect peut entraîner des sanctions. L'ANSSI peut déployer des équipes du CERT-FR en appui.

**NIS 2 — Entités essentielles et importantes :** la directive NIS 2, en cours de transposition en France via la « Loi Résilience » (adoptée en commission spéciale à l'Assemblée nationale en septembre 2025, adoption finale attendue début 2026), imposera une notification initiale sous 24 heures (alerte préliminaire indiquant qu'un incident significatif a été détecté) et une notification complète sous 72 heures (analyse de l'incident, impact, mesures prises). Les entités concernées sont considérablement plus nombreuses qu'avec NIS 1 : environ 15 000 entités en France, réparties en « entités essentielles » et « entités importantes » selon leur secteur et leur taille. Les sanctions prévues sont significatives (amendes administratives pouvant atteindre 10 M€ ou 2 % du CA mondial pour les entités essentielles).

**CNIL — Violations de données personnelles :** notification sous 72 heures après la « prise de connaissance » de la violation (article 33 du RGPD). La « prise de connaissance » n'est pas le moment de la détection de l'incident, mais le moment où l'organisation acquiert une certitude raisonnable que des données personnelles sont compromises. La notification doit décrire la nature de la violation, les catégories de données concernées, le nombre de personnes touchées, les conséquences probables, et les mesures prises. Si la violation présente un risque élevé pour les personnes (données de santé, données bancaires, données permettant l'usurpation d'identité), la notification aux personnes concernées est également obligatoire (article 34 du RGPD).

**Forces de l'ordre :** le dépôt de plainte n'est pas une obligation réglementaire mais une recommandation forte, et il est souvent nécessaire pour activer l'assurance cyber. La plainte se fait auprès du procureur de la République (parquet de Paris, section J3 cybercriminalité pour les affaires complexes). Le dépôt de plainte ne nécessite pas d'avoir terminé l'investigation — il peut être fait dès que l'incident est confirmé, avec les éléments disponibles à ce stade.

La préparation de ces notifications en amont (templates pré-rédigés en Annexe C, contacts identifiés, processus documenté) accélère considérablement la réponse le jour J.

#### 9.2 Cadre contractuel des prestataires et assurance cyber

Le contrat avec le prestataire PRIS doit prévoir les SLA d'intervention (délai maximum entre l'appel et l'arrivée sur site ou la connexion à distance), le périmètre (quelles activités PRIS sont couvertes — toutes les 5 activités du référentiel ANSSI ?), les conditions de remontée d'information (que communique le PRIS au commanditaire, quand, sous quelle forme), les clauses de confidentialité (le PRIS a accès aux données les plus sensibles de l'organisation), et la responsabilité en cas de perte de preuve.

L'assurance cyber est un élément de plus en plus important de la préparation IR. Les points clés à connaître avant l'incident : les conditions d'activation (notification dans les délais — souvent 24 à 48h, préservation des preuves, non-aggravation), la couverture (frais de réponse à incident, perte d'exploitation, frais juridiques, frais de notification, communication de crise — et éventuellement la rançon, sujet controversé et variable selon les polices), les exclusions (actes de guerre, faute intentionnelle, certaines exclusions spécifiques), les plafonds et franchises, et la liste de prestataires agréés par l'assureur (vérifier la compatibilité avec le PRIS sous contrat).

#### 9.3 Conservation de preuve et recevabilité judiciaire

Les preuves collectées pendant l'IR peuvent être utilisées dans une procédure pénale (plainte pour accès frauduleux aux systèmes — art. 323-1 du Code pénal, extorsion — art. 312-1, destruction de données — art. 323-2) ou civile (action contre un prestataire défaillant, contentieux assurance). Pour être recevables, elles doivent respecter la chaîne de custody : documentation de chaque acquisition, calcul et vérification des hash SHA256, stockage sécurisé et intégrité vérifiable. Le détail de la chaîne de custody est traité au Ch.25.

#### 9.4 Fil rouge — BLACKTIDE : les obligations d'Arvantis

> **🔍 BLACKTIDE — Épisode 9**
>
> Arvantis est OIV sur 2 sites (Fos-sur-Mer et Lyon) → notification ANSSI obligatoire, effectuée le samedi 15 mars à 08h00. Données RH de 8 000 employés potentiellement exfiltrées (noms, adresses, RIB, numéros de sécurité sociale) → notification CNIL sous 72h, préparée par le DPO dès le samedi, envoyée le lundi 17 mars. Contrat PRIS en place avec CyberForce (SLA : 12h le week-end, couverture des 5 activités PRIS). Assurance cyber souscrite auprès d'AXA XL (plafond 5 M€, franchise 200 K€, exclusion rançon dans cette police, liste de prestataires agréés incluant CyberForce).

---

### Chapitre 10 — Exercices et entraînement

#### 10.1 Types d'exercices

Les **exercices tabletop** sont des simulations sur papier : un scénario est présenté (« il est 22h, le SOC détecte une alerte EDR sur un DC, que faites-vous ? »), les participants discutent leurs décisions, les processus sont testés sans manipulation technique. Efficace pour tester l'IRP, la chaîne d'escalade, la communication, et la coordination entre équipes. Peu coûteux, rapide à organiser (2 à 4 heures), et adapté à la sensibilisation de la direction.

Les **exercices techniques** sont des simulations en environnement de lab ou en production contrôlée : un malware est déployé (avec l'accord de la direction), un mouvement latéral est simulé, les analystes doivent détecter, investiguer, et confiner. Efficace pour tester les compétences techniques, l'outillage, et les playbooks. Plus coûteux (nécessite un environnement de test et un red team ou purple team), mais irremplaçable pour valider la capacité opérationnelle réelle.

Les **exercices de crise complets** impliquent la direction, la communication, le juridique, et les métiers — en plus de l'équipe technique. Le scénario inclut des éléments de pression réalistes : appel d'un journaliste (simulé), publication sur un faux leak site, pression des « clients » (acteurs de l'exercice). Efficace pour tester la gouvernance, la communication de crise, et la prise de décision stratégique. Lourd à organiser (une journée complète, préparation de plusieurs semaines), mais le seul moyen de tester la chaîne complète de la détection au RETEX.

#### 10.2 Fréquence et progression

Fréquence minimale recommandée : exercice tabletop trimestriel, exercice technique semestriel, exercice de crise complet annuel. Chaque exercice est suivi d'un retex structuré avec plan d'amélioration. La progression va du simple au complexe : d'abord un seul type d'incident avec l'équipe technique seule, puis des scénarios multi-vecteurs avec des parties prenantes multiples.

#### 10.3 Le test le plus simple et le plus révélateur

Appeler les numéros de la chaîne d'escalade un dimanche matin à 7h pour vérifier que quelqu'un répond, que la personne connaît son rôle, et qu'elle sait qui mobiliser ensuite. Résultat habituel : 30 à 50 % d'échec au premier essai (numéro qui ne répond pas, personne qui ne sait pas qu'elle est d'astreinte, personne qui ne connaît pas la procédure). Ce test coûte 30 minutes et révèle plus de failles que n'importe quel audit de 3 semaines.

#### 10.4 Fil rouge — BLACKTIDE : les exercices manqués

> **🔍 BLACKTIDE — Épisode 10**
>
> Arvantis avait prévu un exercice de crise cyber depuis 2 ans. Il a été reporté 4 fois (« pas le bon moment », « trop de projets en cours », « le budget est serré cette année », « on fera ça au prochain trimestre »). Le seul exercice réalisé est un tabletop basique il y a 18 mois, limité à l'équipe IT. La direction n'a jamais participé à un exercice de crise cyber.
>
> Conséquences : le CEO d'Arvantis découvre le fonctionnement d'une cellule de crise le samedi matin à 06h00, en situation réelle. Il ne comprend pas pourquoi « on ne peut pas simplement restaurer les sauvegardes et redémarrer ». Il ne connaît pas les obligations de notification ANSSI. Il est surpris par le coût du prestataire PRIS (« 2 500 € par jour et par consultant ?! »). Toutes ces surprises auraient été évitées par un exercice de crise incluant la direction.

---

## PARTIE III — DÉTECTION, QUALIFICATION ET TRIAGE

*L'incident est suspecté ou confirmé. Il faut comprendre de quoi il s'agit, depuis quand, et quelle est l'étendue probable — le tout en prenant les premières mesures conservatoires sans détruire les preuves.*

---

### Chapitre 11 — Du signal faible à l'incident confirmé

#### 11.1 Sources de détection et leurs biais

Chaque source de détection a un périmètre de visibilité et des angles morts. L'**EDR/XDR** détecte les comportements suspects sur les endpoints (exécution de binaires, modifications système, connexions réseau des processus) mais ne voit pas le trafic réseau entre les machines ni les activités cloud. Le **SIEM** voit les logs qui y sont envoyés — ce qui signifie que tout ce qui n'est pas journalisé est invisible (si le PowerShell script block logging n'est pas activé, le SIEM ne verra jamais les commandes PowerShell de l'attaquant). Le **NDR** voit le trafic réseau en temps réel mais ne voit pas le contenu du trafic chiffré (et en 2025-2026, la quasi-totalité du trafic C2 est chiffrée en HTTPS). Les **alertes antivirus** sont souvent noyées dans le bruit des faux positifs et des détections de PUA (Potentially Unwanted Applications). Le **signalement utilisateur** est parfois le premier signal (« j'ai cliqué sur un lien bizarre ») mais il est souvent tardif (l'utilisateur n'ose pas signaler, ou ne se rend pas compte). La **notification externe** (CERT-FR, partenaire, threat intel feed, notification par l'attaquant via une note de rançon) indique que la compromission est déjà connue en dehors de l'organisation — et souvent que le temps de séjour est déjà long.

La conséquence pour l'investigateur est qu'aucune source seule ne donne la vision complète. La corrélation multi-sources (endpoint + réseau + AD + cloud) est la seule méthode fiable pour établir l'étendue réelle de la compromission.

#### 11.2 Le temps de séjour (dwell time)

Le dwell time — la durée entre la compromission initiale et la détection — est la métrique qui détermine la profondeur de l'investigation. Selon le M-Trends 2025 de Mandiant, la médiane mondiale est d'environ 10 à 13 jours, avec une amélioration progressive grâce à la généralisation des EDR. Mais cette médiane masque une distribution très dispersée : les ransomwares sont souvent détectés en quelques jours (l'attaquant accélère pour chiffrer), tandis que les opérations d'espionnage peuvent durer des mois, voire des années.

Le dwell time détermine la fenêtre temporelle de l'investigation : si l'attaquant est dans le réseau depuis 5 semaines, il faut investiguer 5 semaines de logs, d'artefacts, et de flux réseau. Si les logs ne couvrent que 30 jours, les premières actions de l'attaquant sont perdues.

#### 11.3 Les signaux faibles pré-incident

Avant l'alerte majeure qui déclenche l'IR, des signaux faibles ont souvent été générés — et ignorés ou sous-priorisés. Les connexions à des heures inhabituelles (un compte de service qui s'authentifie à 3h du matin un dimanche), les alertes Kerberos en masse (erreurs de pré-authentification répétées sur de nombreux comptes = possible password spraying ou Kerberoasting), les modifications de GPO non documentées, les exécutions de binaires depuis des répertoires temporaires, les requêtes DNS vers des domaines générés algorithmiquement (DGA), et les petits pics d'exfiltration (quelques Go par jour, en dessous du seuil d'alerte mais visibles en tendance).

La difficulté est que ces signaux sont noyés dans le bruit de fonctionnement normal d'un SI de 12 000 utilisateurs. L'amélioration de la détection des signaux faibles passe par le tuning des règles de détection (réduction des faux positifs pour rendre les vrais positifs visibles), la détection comportementale (baseline de normalité par utilisateur et par machine, alertes sur les écarts), et la corrélation multi-sources (un signal faible sur l'endpoint + un signal faible sur le réseau + un signal faible sur l'AD = un signal fort).

#### 11.4 Fil rouge — BLACKTIDE : les signaux manqués

> **🔍 BLACKTIDE — Épisode 11**
>
> L'investigation post-incident révélera que 3 alertes avaient été générées et classées faux positifs ou basse priorité. À J-30 : alerte antivirus sur un script PowerShell encodé détecté sur le poste du DRH du sous-traitant GestPaie, qui se connectait via VPN au réseau Arvantis. L'alerte a été classée « PUA — faux positif probable » par le SOC N1. En réalité, c'était l'infostealer Lumma en phase d'installation. À J-22 : pic anormal de requêtes Kerberos TGS (Event ID 4769) avec encryption type RC4 (0x17) sur DC01 — signature classique de Kerberoasting. L'alerte SIEM a été classée « activité suspecte — priorité basse » parce que le volume ne dépassait pas le seuil d'alerte automatique. À J-15 : seconde alerte antivirus, cette fois sur DC01, pour un script PowerShell obfusqué dans `C:\Windows\Temp\`. Classée faux positif parce que « les admins utilisent parfois PowerShell sur les DC ».
>
> Trois occasions manquées de détecter l'intrusion 2 à 4 semaines plus tôt — quand le confinement aurait été beaucoup plus simple.

---

### Chapitre 12 — Triage initial et premières mesures conservatoires

#### 12.1 Les 30 premières minutes

Le triage initial est l'évaluation rapide qui transforme une alerte en décision d'action. Les objectifs des 30 premières minutes sont de confirmer le vrai positif (exclure le faux positif, l'erreur de configuration, l'opération de maintenance planifiée), d'identifier les systèmes visiblement impactés (la machine source de l'alerte, les machines contactées, les comptes utilisés), d'évaluer la sévérité initiale (P4 à P1, avec possibilité de réévaluation), et de prendre les premières mesures conservatoires.

#### 12.2 Ce que l'on sait et ce que l'on ne sait pas

L'exercice fondamental du triage consiste à lister explicitement les faits confirmés et les inconnues. Cette discipline évite les conclusions prématurées et oriente l'investigation. Format recommandé :

**Ce qu'on sait :** « L'EDR a détecté l'exécution de PsExec sur DC01 à 22h17, depuis le profil du compte svc_deploy. Une modification de GPO visant à désactiver Defender a été tentée. Le compte svc_deploy n'est pas utilisé par les administrateurs ce soir. »

**Ce qu'on ne sait pas :** « Depuis quand l'attaquant est-il dans le réseau. Combien de systèmes sont compromis. Si des données ont été exfiltrées. Si d'autres DC sont touchés. Si l'attaquant est toujours actif en ce moment. »

Cette distinction structure le raisonnement et guide les questions d'investigation suivantes.

#### 12.3 Premières mesures conservatoires

À ce stade, l'objectif n'est pas de contenir (c'est trop tôt — on ne connaît pas l'étendue) mais de préserver la capacité d'investigation et de limiter les risques immédiats sans alerter l'attaquant. Les mesures conservatoires incluent l'augmentation du niveau de logging sur les systèmes suspects (activer la journalisation de la ligne de commande des processus si elle ne l'est pas, augmenter la verbosité du logging AD), la capture réseau sur les segments critiques (si un NDR ou une capacité de capture existe), la sauvegarde immédiate des logs disponibles (avant qu'ils ne soient écrasés par la rotation), et la mise en surveillance renforcée des systèmes identifiés (le SOC concentre son attention sur les machines suspectes).

L'isolation réseau n'est pas systématiquement la bonne décision à ce stade. Si l'attaquant ne sait pas qu'il est détecté, l'isoler maintenant l'alertera et il pourra activer des mécanismes de destruction (wiper, chiffrement accéléré) ou détruire des preuves. Le dilemme du confinement est traité en détail au Ch.23.

#### 12.4 Fil rouge — BLACKTIDE : le triage

> **🔍 BLACKTIDE — Épisode 12**
>
> 22h30-23h00. Karim confirme : PsExec sur DC01, DC02 et DC03. Modification GPO tentée sur les 3 DC. Exécution d'un binaire inconnu sur DC01 (hash non présent dans VirusTotal — soumission en cours). Le compte svc_deploy est un compte de service pour le déploiement de logiciel via SCCM — il a des droits élevés mais est rarement utilisé manuellement. L'authentification avec ce compte provient de l'IP 10.42.15.87 (un serveur de fichiers du site de Lyon).
>
> Mesures conservatoires immédiates : augmentation du logging sur les 3 DC (activation de la journalisation de la ligne de commande, Event ID 4688), capture réseau activée sur le segment DMZ et le segment serveurs via le port mirroring du switch core, sauvegarde des Event Logs actuels des 3 DC sur un partage hors domaine (clé USB branchée par l'admin d'astreinte, sous les instructions de Nadia).
>
> Pas d'isolation réseau à ce stade. Nadia veut d'abord comprendre l'étendue avant de décider du périmètre de confinement.

---

### Chapitre 13 — Qualification, catégorisation et évaluation de gravité

#### 13.1 Catégorisation de l'incident

La catégorisation identifie le type d'incident pour orienter vers le playbook approprié et conditionner les obligations réglementaires. La question n'est pas « qu'est-ce qui s'est passé techniquement ? » (ça, c'est l'investigation) mais « quel type de problème avons-nous ? » (ransomware, espionnage, compromission de compte, etc.).

Dans le cas de BLACKTIDE, la catégorisation initiale est « compromission de serveur critique avec mouvement latéral ». Elle évoluera vers « ransomware avec double extorsion et exfiltration massive » au fur et à mesure de l'investigation.

#### 13.2 Évaluation de la gravité

La gravité s'évalue sur une grille multicritères. La **gravité technique** mesure le nombre de systèmes touchés, le niveau de privilèges compromis, et la propagation (en cours vs achevée). La **gravité métier** mesure l'impact sur la production, la facturation, la logistique, et les clients. La **sensibilité des données** qualifie les données potentiellement exposées (données personnelles, propriété intellectuelle, secret industriel, secret défense). La **criticité des systèmes** identifie les systèmes touchés (Active Directory, systèmes de paiement, systèmes OT, serveurs de production). Le **potentiel de propagation** évalue si l'attaquant est toujours actif et si la compromission peut s'étendre. L'**impact réglementaire** identifie les notifications obligatoires et les sanctions potentielles.

La grille de gravité complète avec les critères détaillés pour chaque niveau (P1 à P4) est en Annexe G.

#### 13.3 Évaluation dynamique

La gravité n'est pas figée — elle doit être réévaluée à chaque nouvelle découverte. Un incident initialement classé P3 peut basculer P1 quand l'investigation révèle que le malware « isolé » était en fait un infostealer actif depuis des semaines, alimentant la compromission de l'AD. La réévaluation régulière est une discipline essentielle : à chaque SitRep (toutes les 4-6 heures en phase aiguë), la gravité est recalculée et les décisions ajustées.

#### 13.4 Fil rouge — BLACKTIDE : réévaluation en cascade

> **🔍 BLACKTIDE — Épisode 13**
>
> La gravité est réévaluée 4 fois en 8 heures.
> - 22h30 : **P2** — alerte EDR sur un DC, compromission de serveur probable.
> - 01h00 : **P1** — 3 DC touchés, ransomware en cours de déploiement, compromission majeure confirmée.
> - 06h00 : **P1 / Crise** — exfiltration de 380 Go confirmée, 3 sites impactés dont un OIV, données RH de 8 000 personnes exposées.
> - 10h00 : **Crise confirmée** — publication sur le canal Telegram de PhantomCrypt avec compte à rebours de 10 jours, presse spécialisée informée par la revendication.

---

### Chapitre 14 — Scoping initial : délimiter l'étendue de la compromission

#### 14.1 La question la plus critique et la plus difficile

L'attaquant a-t-il compromis un seul poste, un segment réseau, ou le domaine entier ? La réponse conditionne toutes les décisions suivantes : le périmètre du confinement (isoler 3 machines ou 3 sites ?), le dimensionnement de l'équipe IR (3 analystes ou 15 ?), les notifications réglementaires (incident technique interne ou violation de données à déclarer ?), et la durée prévisible de la réponse (2 jours ou 3 semaines ?).

Le scoping est un exercice d'approximation rapide — il sera affiné au fil de l'investigation, mais la première estimation doit être produite dans les premières heures pour guider les décisions de confinement. Sous-estimer le périmètre conduit à un confinement insuffisant. Surestimer conduit à un impact business disproportionné.

#### 14.2 Méthode de scoping rapide

Croiser les sources disponibles dans les premières heures pour délimiter le périmètre. Les IoC identifiés (hash du malware, domaine C2, IP C2) sont recherchés sur l'ensemble du parc via l'EDR — quelles machines ont communiqué avec le C2, exécuté le hash, ou présenté les mêmes artefacts ? Les logs d'authentification Active Directory sont analysés — quels comptes ont été utilisés, depuis quelles machines, à quelles heures ? Y a-t-il des authentifications anormales (geo-impossible, horaires inhabituels, comptes de service utilisés manuellement) ? Les logs réseau sont examinés — quels systèmes communiquent avec des destinations suspectes ?

L'intersection de ces sources donne le périmètre initial : les machines confirmées compromises, les machines probablement compromises, et les machines non touchées (à ce stade).

#### 14.3 Première timeline

La timeline provisoire est la reconstitution chronologique des événements identifiés à ce stade. Elle sera enrichie et corrigée tout au long de l'investigation (Ch.17), mais la première version oriente le scoping : si le premier signe de compromission remonte à 5 semaines, tout ce qui s'est passé pendant ces 5 semaines doit être investigué.

#### 14.4 Fil rouge — BLACKTIDE : le scoping

> **🔍 BLACKTIDE — Épisode 14**
>
> En 3 heures (22h30-01h30), l'équipe établit un périmètre provisoire.
>
> **Confirmé compromis :** DC01, DC02, DC03 (traces de PsExec, GPO malveillante, exécution du ransomware builder). Serveur de fichiers FS01-Lyon, FS01-Fos, FS01-Cologne (chiffrement en cours). Le poste du DRH de GestPaie (sous-traitant — point d'entrée de l'infostealer, confirmé par analyse de l'alerte antivirus de J-30).
>
> **Probablement compromis :** 40+ machines listées dans les logs PsExec. Le serveur SCCM (utilisé comme pivot via le compte svc_deploy). Au moins un serveur du réseau OT de Fos (le poste d'ingénierie a des traces de connexion depuis DC01).
>
> **Volume estimé de l'exfiltration :** 380 Go (identifié par corrélation des logs proxy — flux HTTPS vers des endpoints AWS S3 depuis 3 machines internes, sur 7 jours).
>
> **Timeline provisoire :** Patient zéro estimé à J-35 (phishing sur GestPaie). Compromission de l'AD estimée à J-14 (DCSync). Début d'exfiltration estimé à J-7. Déploiement du ransomware : J-0.

---

### Chapitre 15 — Déclenchement formel et premières notifications

#### 15.1 Ouverture formelle de l'incident

L'ouverture formelle marque le passage du mode « investigation exploratoire » au mode « réponse structurée ». Elle comprend la désignation du pilote (IR lead), la constitution de la cellule technique, l'ouverture du journal d'incident (chronologique, chaque action horodatée et signée — le document le plus important de l'incident, car il reconstitue la séquence des décisions et protège les décideurs), l'activation du canal de communication sécurisé (hors SI — Signal, WhatsApp groupe, téléphone — le SI interne est potentiellement compromis et ne peut plus être utilisé pour des communications sensibles), et l'attribution d'un nom de code (pour la communication interne et la traçabilité des documents).

#### 15.2 Première SitRep

Le premier SitRep est produit dans les 2 à 4 premières heures, à destination du RSSI et de la direction. Il suit une structure standardisée : ce qu'on sait (faits confirmés, cotés), ce qu'on ne sait pas (inconnues explicites), ce qu'on fait (actions en cours), ce qu'on envisage (prochaines étapes, options de confinement), et ce dont on a besoin (ressources, décisions, autorisations). Format : une page maximum, factuel, sans jargon technique excessif.

#### 15.3 Notifications urgentes

Les notifications qui ne peuvent pas attendre : ANSSI/CERT-FR si OIV ou OSE (dans les délais réglementaires), prestataire PRIS (si non encore mobilisé), assureur cyber (dans les conditions du contrat — souvent 24 à 48h), et direction générale (information de la bascule en crise si applicable). Les notifications complètes (CNIL 72h, dépôt de plainte) viendront dans les jours suivants mais doivent être préparées dès maintenant.

#### 15.4 Fil rouge — BLACKTIDE : le déclenchement

> **🔍 BLACKTIDE — Épisode 15**
>
> 01h00 — Opération BLACKTIDE est officiellement ouverte. Nadia est IR lead. Canal Signal « IR-BLACKTIDE » activé avec 8 participants (Nadia, Karim, Marc/RSSI, David/admin astreinte, Fatima/SOC N2 relève, et 3 autres analystes mobilisables). Journal d'incident ouvert sur un tableur Excel hébergé sur le laptop personnel de Nadia (non joint au domaine Arvantis — bonne pratique improvisée).
>
> ANSSI notifiée à 08h00 le samedi (obligation OIV — site de Fos-sur-Mer impacté). Le CERT-FR accuse réception et propose un appui spécialisé OT pour le lundi. Prestataire PRIS CyberForce arrivé à 08h15 (Thomas Hartmann, consultant senior forensic, et Léa Chen, spécialiste AD). Assureur cyber AXA XL notifié à 10h00 le samedi (dans le délai contractuel de 48h).

---

## PARTIE IV — INVESTIGATION ET ANALYSE

*Le confinement initial est en place ou en cours de décision. L'investigation approfondie commence pour reconstituer le chemin d'attaque complet, déterminer l'étendue exacte, et identifier les données compromises.*

---

### Chapitre 16 — Principes de l'investigation IR

#### 16.1 Agir vite sans détruire la preuve

La tension fondamentale de l'investigation IR : collecter des évidences (rigueur, temps) tout en fournissant des réponses rapides aux décideurs (vitesse, pragmatisme). La méthode de résolution est le triage : collecte rapide des artefacts critiques d'abord (30 minutes par machine avec KAPE ou Velociraptor), image complète ensuite (si le temps et les ressources le permettent). Le triage donne 80 % de l'information en 20 % du temps ; l'image complète donne les 20 % restants mais prend 5 fois plus longtemps.

#### 16.2 Investigation orientée décision

Chaque action d'investigation doit répondre à une question opérationnelle concrète. « Ce serveur est-il compromis ? » → pour décider de l'isoler. « L'attaquant a-t-il les privilèges domain admin ? » → pour décider de l'ampleur du confinement et du reset des comptes. « Des données personnelles ont-elles été exfiltrées ? » → pour décider de la notification CNIL. « Le krbtgt est-il compromis ? » → pour décider si un double reset est nécessaire. Si une action d'investigation ne répond à aucune question décisionnelle en cours, elle est dé-priorisée — ce n'est pas qu'elle est inutile, c'est qu'elle n'est pas urgente.

#### 16.3 Hypothèses et itérativité

L'investigateur formule des hypothèses (« le point d'entrée est probablement un phishing sur le sous-traitant RH, car le premier compte compromis est un compte VPN du sous-traitant ») et les teste contre les données. Chaque hypothèse confirmée ouvre de nouvelles pistes. L'investigation n'est pas linéaire — elle est itérative, avec des allers-retours constants entre collecte, analyse, et reformulation des hypothèses.

#### 16.4 Fil rouge — BLACKTIDE : les priorités d'investigation

> **🔍 BLACKTIDE — Épisode 16**
>
> Samedi 08h30. Nadia établit les 4 questions prioritaires pour les 12 prochaines heures, chacune assignée à un analyste :
>
> **Q1 (Thomas/PRIS) :** Quel est le patient zéro ? Remonter au point d'entrée initial. → Investigation forensic sur le poste du DRH GestPaie et les logs VPN.
>
> **Q2 (Léa/PRIS) :** Le compte krbtgt est-il compromis ? → Investigation AD, analyse des logs de réplication, vérification des tickets Kerberos.
>
> **Q3 (Karim/SOC) :** Quel est le volume exact de données exfiltrées ? Quelles données ? → Analyse des logs proxy, identification des fichiers accédés avant l'exfiltration.
>
> **Q4 (Fatima/SOC) :** L'attaquant est-il toujours actif dans le réseau ? → Surveillance temps réel des communications C2, monitoring des authentifications suspectes.

---

### Chapitre 17 — Construction de la timeline d'attaque

#### 17.1 Méthode de reconstruction

La timeline d'attaque est le livrable central de l'investigation IR. Elle reconstitue la séquence complète des actions de l'attaquant, de la compromission initiale au déploiement final, en passant par chaque étape intermédiaire. La méthode est rétrospective : partir de ce qu'on sait (l'alerte qui a déclenché l'IR) et remonter dans le temps, événement par événement, jusqu'au patient zéro.

Pour chaque événement identifié, rechercher l'événement précédent : « PsExec a été exécuté sur DC01 à 22h17 — d'où venait la session ? depuis quel poste ? avec quel compte ? ce compte était-il compromis avant ? comment ? » Remonter de machine en machine, de compte en compte, jusqu'au point d'entrée initial.

Puis reconstruire la séquence dans l'ordre chronologique, en identifiant les phases ATT&CK (voir 17.3).

#### 17.2 Corrélation multi-sources

Les logs d'une seule source ne racontent qu'une partie de l'histoire. L'Event Log Windows montre que PsExec a été exécuté, mais pas d'où venait la connexion. Le log VPN montre qu'un compte s'est connecté depuis l'extérieur, mais pas ce que l'utilisateur a fait ensuite. Le log proxy montre un flux vers AWS S3, mais pas quel processus l'a généré. La corrélation entre sources reconstitue la séquence complète.

Outils pour la construction de timeline : le SIEM (Splunk, ELK, Sentinel) pour la corrélation des logs centralisés, Plaso/log2timeline pour la construction d'une « Super Timeline » à partir des artefacts forensic d'un endpoint (fusion de la MFT, du Prefetch, des Event Logs, du registre en une seule timeline chronologique), et Timesketch pour la visualisation collaborative de la timeline résultante.

#### 17.3 Mapping ATT&CK

Chaque étape du chemin d'attaque est cartographiée sur la matrice MITRE ATT&CK. Ce mapping remplit trois fonctions : il structure le rapport final (les TTP sont décrites dans un vocabulaire normalisé que les autres équipes de sécurité comprennent), il oriente la remédiation (pour chaque technique utilisée par l'attaquant, quelle détection ou quelle mesure préventive aurait pu la contrer ?), et il facilite le partage avec la communauté (IoC + TTP ATT&CK = renseignement actionnable pour les pairs).

#### 17.4 Fil rouge — BLACKTIDE : la timeline complète

> **🔍 BLACKTIDE — Épisode 17**
>
> Après 36 heures d'investigation, la timeline est reconstituée :
>
> | Date | Action | Technique ATT&CK |
> |------|--------|-------------------|
> | J-35 (7 fév.) | Phishing ciblé sur le DRH de GestPaie — email avec pièce jointe Excel contenant macro VBA | T1566.001 — Spearphishing Attachment |
> | J-35 | Macro exécutée → téléchargement et exécution de Lumma infostealer | T1204.002 — User Execution: Malicious File |
> | J-35 | Lumma collecte credentials navigateur, cookies, credentials VPN Arvantis | T1555 — Credentials from Password Stores |
> | J-28 (12 fév.) | Première connexion VPN au réseau Arvantis avec le compte compromis (`admin_rh_ext`), 20h47 | T1078 — Valid Accounts |
> | J-25 (15 fév.) | Exécution de BloodHound pour reconnaissance AD (détecté rétrospectivement via DNS) | T1087 — Account Discovery |
> | J-21 (19 fév.) | Kerberoasting — demande de TGS pour 12 comptes de service avec SPN | T1558.003 — Kerberoasting |
> | J-21 | Crackage offline du hash du compte `svc_deploy` (mot de passe : `Deploy2024!`, 12 car.) — 4h | T1110.002 — Password Cracking |
> | J-14 (26 fév.) | DCSync sur DC01 — dump de tous les hashes NTLM, y compris krbtgt | T1003.006 — DCSync |
> | J-12 (28 fév.) | Création d'un Golden Ticket avec le hash krbtgt | T1558.001 — Golden Ticket |
> | J-12 | Création de 3 comptes admin cachés dans des OU peu surveillées | T1136.001 — Create Account: Local Account |
> | J-7 (7 mars) | Installation de rclone sur 3 serveurs internes, exfiltration vers AWS S3 | T1567.002 — Exfiltration to Cloud Storage |
> | J-7 à J-0 | Exfiltration progressive : 380 Go de données R&D et RH | T1041 — Exfiltration Over C2 Channel |
> | J-0 (14 mars) | Création d'une GPO malveillante « Windows Update Configuration » | T1484.001 — Group Policy Modification |
> | J-0, 22h10 | Déploiement de PhantomCrypt via GPO sur les serveurs de fichiers | T1486 — Data Encrypted for Impact |
> | J-0, 22h17 | Détection EDR — PsExec + désactivation Defender | T1562.001 — Disable or Modify Tools |

---

### Chapitre 18 — Cartographie des sources de données

*Ce chapitre est un référentiel : il recense et décrit les sources de données disponibles pour l'investigation IR, avec leurs forces, leurs limites, et leur localisation. Il ne traite pas de l'analyse concrète des artefacts (c'est l'objet des Ch.19-22) mais de la cartographie de ce qui existe et de ce qu'on peut en attendre.*

#### 18.1 Sources endpoint (Windows)

Les **Windows Event Logs** sont la source primaire pour l'investigation Windows. Les Event IDs critiques pour l'IR sont référencés en Annexe D avec leur interprétation détaillée. Les catégories les plus importantes : Security (authentification 4624/4625, privilèges 4672, création de processus 4688, création de compte 4720, modification de groupe 4728/4732), System (installation de service 7045), PowerShell (script block logging 4104, module logging 4103), Sysmon (si déployé — fournit une granularité très supérieure aux Event Logs natifs : création de processus avec hash et ligne de commande, connexions réseau par processus, chargement de DLL).

Les **artefacts forensic Windows** incluent le Prefetch (historique des exécutions de programmes), l'Amcache et le ShimCache (historique des programmes exécutés avec hash), la MFT et le USN Journal (journal du système de fichiers — création, modification, suppression), le registre (persistence, configuration, activité utilisateur), le SRUM (consommation réseau par processus), et les Jump Lists et Shellbags (activité de navigation dans l'explorateur). Ces artefacts sont détaillés au Ch.19.

Les **logs EDR** fournissent une telemetry riche et centralisée : exécution de processus avec arbre de parenté, connexions réseau par processus, modifications système, et détections comportementales. La rétention varie selon l'EDR (typiquement 7 à 90 jours selon la licence).

#### 18.2 Sources endpoint (Linux)

Les fichiers de log système (`/var/log/auth.log`, `/var/log/secure`, `/var/log/syslog`), les journaux d'authentification (`wtmp`, `btmp`, `lastlog`), les historiques de commandes (`bash_history`, `zsh_history`), les tâches planifiées (`crontab`, `systemd timers`), et les fichiers de configuration modifiés récemment.

#### 18.3 Sources réseau

Les logs pare-feu (flux autorisés et refusés, volumes, destinations), les logs proxy (URLs visitées, user-agents, volumes de données sortantes, codes de retour HTTP), les logs DNS (résolutions vers des domaines suspects, patterns DGA, tunneling DNS), les logs VPN (connexions, géolocalisation, durée), le NetFlow (profils de communication entre IP internes et externes, volumes), et les PCAP (captures complètes de paquets — si le NDR ou une capacité de capture existe).

#### 18.4 Sources Active Directory

Les Event Logs des contrôleurs de domaine (authentification, réplication, modifications d'objets), les logs d'Azure AD Connect (si synchronisation hybride), et les métadonnées AD (date de création et de modification des objets, membres des groupes, ACL, GPO).

#### 18.5 Sources cloud

Microsoft 365 : Unified Audit Log (rétention variable selon licence), Sign-in Logs (Entra ID), Azure Activity Log, Mailbox Audit Log. AWS : CloudTrail (API calls), VPC Flow Logs, S3 Access Logs. GCP : Cloud Audit Logs, VPC Flow Logs. Azure IaaS : Activity Log, NSG Flow Logs.

#### 18.6 Sources externes

Les feeds de threat intelligence (IoC partagés par la communauté), les bases de malware (VirusTotal, MalwareBazaar, ANY.RUN), les rapports d'éditeurs CTI (Mandiant, CrowdStrike, Recorded Future, Secureworks), et les notifications du CERT-FR.

#### 18.7 Fil rouge — BLACKTIDE : les sources mobilisées

> **🔍 BLACKTIDE — Épisode 18**
>
> Sources disponibles et exploitées : EDR CrowdStrike Falcon (telemetry 90 jours sur 92 % du parc), SIEM Splunk (9 mois de rétention — Event Logs Windows, proxy Squid, DNS Infoblox, pare-feu Palo Alto, VPN Fortinet), logs VPN Fortinet (180 jours), logs pare-feu Palo Alto (12 mois), Microsoft 365 UAL (180 jours — licence E3).
>
> Sources manquantes : pas de NDR (la visibilité réseau est limitée aux logs proxy et pare-feu — pas de capture de paquets, pas de détection de beaconing sur le trafic chiffré). Pas de Sysmon (les Event Logs natifs sont moins granulaires). PowerShell script block logging activé sur les serveurs mais pas sur les postes de travail (angle mort sur l'exécution de scripts sur les postes).

---

### Chapitre 19 — Investigation endpoint : collecte et analyse concrète

*Ce chapitre est le volet pratique de l'investigation sur les machines. Là où le Ch.18 cartographie les sources, ce chapitre montre concrètement comment collecter et interpréter les artefacts pour répondre aux questions de l'investigation.*

#### 19.1 Acquisition de preuves : triage vs image complète

Le **triage live** collecte les artefacts les plus informatifs d'une machine en 20 à 30 minutes, sans éteindre la machine. L'outil de référence est KAPE (Kroll Artifact Parser and Extractor) qui collecte automatiquement les Event Logs, le Prefetch, l'Amcache, le ShimCache, le registre, le SRUM, les Scheduled Tasks, les services, les fichiers récents, et d'autres artefacts configurables. Velociraptor offre une capacité similaire mais avec la possibilité de déployer la collecte à distance sur des centaines de machines simultanément — essentiel quand le périmètre de compromission est large. Le triage est la méthode par défaut en IR : il donne 80 % de l'information en 20 % du temps.

L'**image complète** (bit-à-bit) capture l'intégralité du disque. Outils : FTK Imager (interface graphique, Windows), dd/dcfldd (ligne de commande, Linux), ou acquisition via EDR pour les environnements cloud. L'image est nécessaire quand la chaîne de custody doit être préservée pour une procédure judiciaire, quand une analyse approfondie est requise (analyse de la MFT complète, carving de fichiers supprimés, analyse du slack space), ou quand le triage n'a pas donné de résultats concluants.

L'**acquisition mémoire** capture la RAM de la machine en cours d'exécution. Outils : DumpIt (Windows, simple et rapide), WinPmem (Windows, plus flexible), ou LiME (Linux). L'acquisition mémoire doit être faite AVANT tout redémarrage — la mémoire est la source la plus volatile. Elle est indispensable pour les malwares fileless (qui n'écrivent rien sur le disque), pour l'extraction de credentials en mémoire (hashes NTLM dans le processus lsass), et pour l'analyse des connexions réseau actives.

**Chaîne de custody :** chaque acquisition est documentée : qui (nom de l'analyste), quoi (machine, artefact), quand (horodatage précis), avec quel outil (nom, version), et hash de vérification (SHA256 calculé immédiatement). Le formulaire de chaîne de custody est en Annexe C.

#### 19.2 Analyse mémoire

L'analyse de la mémoire vive avec **Volatility 3** (l'outil de référence open source) permet d'extraire les processus en cours d'exécution (`windows.pslist`, `windows.pstree` — identifier les processus suspects par leur arbre de parenté, leur chemin d'exécution, ou leur nom), les DLL chargées (`windows.dlllist` — identifier les DLL injectées ou suspectes), les connexions réseau actives (`windows.netscan` — les connexions vers le C2 sont directement visibles), les credentials en mémoire (hashes NTLM extraits du processus lsass — si mimikatz ou un outil similaire a été exécuté, les credentials déchiffrées peuvent encore être en mémoire), les commandes exécutées (`windows.cmdline` — les arguments passés aux processus), et le code injecté (`windows.malfind` — détection de zones mémoire suspectes dans les processus, indicatrices d'injection de code).

L'analyse mémoire est indispensable quand le malware est fileless (il s'exécute uniquement en mémoire, sans écrire de fichier sur le disque), quand l'attaquant utilise le process hollowing ou le reflective DLL loading (techniques d'évasion qui injectent du code dans des processus légitimes), et pour capturer les credentials actives (les hashes NTLM dans lsass permettent de comprendre quels comptes l'attaquant a compromis).

#### 19.3 Artefacts système Windows — interprétation pour l'IR

Le **Prefetch** (situé dans `C:\Windows\Prefetch\`) enregistre les programmes exécutés, avec le nom du fichier, les 8 dernières dates/heures d'exécution, et le nombre total d'exécutions. En IR, le Prefetch révèle l'exécution d'outils de l'attaquant (PsExec, mimikatz, rclone, ransomware builder) même si les fichiers ont été supprimés depuis.

L'**Amcache** (`C:\Windows\AppCompat\Programs\Amcache.hve`) et le **ShimCache** enregistrent les programmes exécutés avec leur hash SHA1 et leur chemin — permettant de confirmer que le binaire malveillant a bien été exécuté et d'en identifier le hash pour enrichissement CTI.

La **MFT** (Master File Table) et le **USN Journal** sont le journal du système de fichiers NTFS. Ils enregistrent la création, la modification, le renommage, et la suppression de fichiers avec horodatage. En IR, ils révèlent les fichiers créés par l'attaquant (scripts, binaires, fichiers de staging), les fichiers supprimés (l'attaquant nettoie souvent ses traces), et les mouvements de données (fichiers copiés vers un répertoire de staging avant exfiltration).

Le **registre Windows** contient des informations critiques pour l'IR : les clés `Run`/`RunOnce` (persistence via exécution automatique au démarrage), les services (persistence via création de service), les clés `UserAssist` (historique des programmes exécutés via l'interface graphique), les clés `BAM`/`DAM` (programmes exécutés avec horodatage, disponibles sur Windows 10/11 et Server 2016+), et les informations réseau (profils WiFi, historique des connexions).

Le **SRUM** (System Resource Usage Monitor, `C:\Windows\System32\SRU\SRUDB.dat`) enregistre la consommation réseau par processus sur 30 à 60 jours. En IR, il révèle les processus ayant généré du trafic réseau significatif — excellent pour détecter l'exfiltration (un processus rclone ayant transféré 380 Go sera visible dans le SRUM même si le processus n'est plus en cours d'exécution).

#### 19.4 Analyse malware first-pass

L'IR n'est pas du reverse engineering approfondi, mais un first-pass rapide sur le malware est essentiel pour extraire les IoC et comprendre le comportement. L'analyse statique rapide (strings — extraire les chaînes de caractères pour identifier les URLs, les IP, les clés de registre, les noms de fichiers ; imports — identifier les API Windows utilisées ; sections PE — identifier les sections suspectes ou packé) et la soumission en sandbox (ANY.RUN, Joe Sandbox, CAPE — exécution contrôlée avec observation du comportement réseau, des modifications système, et des artefacts créés) suffisent généralement pour l'IR. Le reverse engineering approfondi (décompilation, analyse du code assembleur) est délégué aux analystes malware spécialisés ou au prestataire PRIS.

#### 19.5 Fil rouge — BLACKTIDE : le forensic sur le DC

> **🔍 BLACKTIDE — Épisode 19**
>
> Samedi 09h00-14h00. Thomas (PRIS) priorise DC01 — le contrôleur de domaine principal, le plus compromis.
>
> **Acquisition mémoire (DumpIt) :** 32 Go, 12 minutes. L'analyse Volatility révèle un processus `lsass.exe` avec des zones mémoire modifiées (malfind positif — injection de code), des credentials en clair de 12 comptes admin dans la mémoire de lsass, et un processus `svchost.exe` suspect avec une connexion active vers le C2 `update-srv-infra[.]xyz` sur le port 443.
>
> **Triage KAPE (DC01, DC02, DC03) :** 20 minutes par machine. Le Prefetch confirme l'exécution de `psexec.exe`, `rclone.exe`, `bc.exe` (le builder PhantomCrypt), et `mimikatz.exe`. L'Amcache fournit les hashes SHA1 de tous ces binaires. Le SRUM de DC01 montre que `rclone.exe` a transféré 147 Go de données réseau sur les 7 derniers jours (une partie des 380 Go totaux). Les Scheduled Tasks révèlent une tâche `WindowsUpdateCheck` créée à J-12, exécutant un script PowerShell obfusqué toutes les 4 heures — mécanisme de persistence.
>
> **Constat :** David, l'admin d'astreinte, a redémarré les serveurs de fichiers FS01-Lyon et FS01-Fos à 23h30 la veille (« pour stopper le chiffrement »). La mémoire de ces serveurs est perdue. Les artefacts Prefetch et Amcache sont préservés (ils sont sur disque), mais les connexions réseau actives et les credentials en mémoire sont irrémédiablement perdus. Nadia documente : « Perte de preuve — RAM de FS01-Lyon et FS01-Fos — cause : redémarrage sans collecte préalable. »

---

### Chapitre 20 — Investigation identité et Active Directory

#### 20.1 Pourquoi l'AD est la cible ultime

Dans la quasi-totalité des compromissions Windows, l'objectif stratégique de l'attaquant est le contrôle de l'Active Directory. L'AD gère l'authentification de tous les utilisateurs, les autorisations sur toutes les ressources, le déploiement de logiciels et de configurations via GPO, et les secrets (hashes NTLM, clés Kerberos, mots de passe en clair dans certains cas). Compromettre l'AD signifie contrôler l'ensemble du SI Windows — c'est pourquoi l'investigation AD est la composante la plus critique de l'IR dans un environnement Windows.

#### 20.2 Techniques d'attaque AD et leur détection

**Kerberoasting :** l'attaquant demande des TGS (Ticket Granting Service) pour des comptes de service ayant un SPN (Service Principal Name), puis cracke les tickets offline pour obtenir le mot de passe en clair. Détection : Event ID 4769 avec encryption type RC4 (0x17), en volume anormal. Implication IR : si un compte de service avec droits DA a un mot de passe faible, il a été compromis.

**DCSync :** l'attaquant simule un contrôleur de domaine pour demander la réplication des hashes NTLM de tous les comptes, y compris le krbtgt. Détection : Event ID 4662 avec les GUID de réplication (`1131f6ad-...` et `1131f6aa-...`), provenant d'une machine qui n'est pas un DC. Implication IR : si le DCSync a réussi, TOUS les hashes sont compromis — y compris le krbtgt (Golden Ticket possible).

**Golden Ticket :** l'attaquant forge un TGT (Ticket Granting Ticket) avec le hash du compte krbtgt, lui donnant un accès illimité au domaine, sans expiration normale. Détection : anomalies dans les tickets Kerberos (lifetime anormalement long, SID incohérent), Event ID 4769 avec des tickets dont les propriétés ne correspondent pas à la politique du domaine. Implication IR : si un Golden Ticket a été créé, l'attaquant peut s'authentifier comme n'importe quel utilisateur du domaine, même après un reset des mots de passe — seul un double reset du krbtgt invalide les Golden Tickets.

**Modifications d'ACL/DACL :** l'attaquant modifie les permissions sur des objets AD (OU, groupes, comptes) pour se donner des droits persistants (GenericAll, WriteDACL, AddMember). Ces modifications sont subtiles et difficiles à détecter sans un audit AD dédié. Outils de détection : BloodHound (visualisation des chemins d'attaque), PingCastle (score de sécurité AD et identification des faiblesses), Purple Knight (audit automatisé).

#### 20.3 Évaluation de la profondeur de compromission

Les questions critiques que l'investigateur doit trancher pour déterminer le plan d'éradication :

Le **krbtgt est-il compromis ?** Si oui → le double reset est obligatoire (Ch.27). Un seul reset ne suffit pas car Kerberos retient les 2 derniers mots de passe du krbtgt — il faut donc 2 resets espacés de 12h minimum pour invalider tous les tickets.

Des **comptes admin cachés** ont-ils été créés ? Vérification de tous les groupes privilégiés (Domain Admins, Enterprise Admins, Schema Admins, Administrators, mais aussi les groupes avec des délégations non standard) et de toutes les créations de comptes récentes.

Des **GPO malveillantes** existent-elles ? Revue de toutes les GPO créées ou modifiées récemment — une GPO malveillante peut déployer du malware, désactiver des défenses, ou modifier des configurations de sécurité sur tout le parc.

Les **ACL/DACL** ont-elles été modifiées ? Des permissions anormales sur des objets critiques (OU des DC, OU des serveurs, comptes de service) peuvent permettre une re-compromission même après éradication.

#### 20.4 Fil rouge — BLACKTIDE : la profondeur de la compromission AD

> **🔍 BLACKTIDE — Épisode 20**
>
> Samedi 14h00. Léa (PRIS, spécialiste AD) présente ses conclusions à la cellule technique.
>
> **DCSync confirmé** sur DC01 à J-14. L'attaquant a obtenu tous les hashes NTLM du domaine, y compris le hash du krbtgt. **→ Golden Ticket possible et probable.**
>
> **Golden Ticket utilisé.** L'analyse des logs Kerberos montre des TGT avec un lifetime de 10 ans (la politique du domaine est de 10 heures) — signature d'un Golden Ticket.
>
> **3 comptes admin cachés** créés à J-12 dans l'OU `OU=ServiceAccounts,OU=IT,DC=arvantis,DC=local` : `svc_monitor01`, `svc_backup_ext`, `svc_audit_temp`. Noms choisis pour se fondre dans les comptes de service légitimes. Tous membres du groupe Domain Admins.
>
> **1 GPO malveillante** : « Windows Update Configuration » créée à J-0, liée aux OU des serveurs de fichiers, exécutant le ransomware PhantomCrypt via un script de démarrage.
>
> **Modification des ACL** : GenericAll attribué au compte `svc_deploy` (le compte compromis) sur l'OU des serveurs critiques — permettant à ce compte de modifier n'importe quel objet dans cette OU.
>
> **DSRM password** : non modifié par l'attaquant (il n'en a pas eu besoin — le Golden Ticket lui suffisait).
>
> **Conclusion de Léa :** « L'AD est compromis en profondeur. Un simple reset de mots de passe ne suffit pas. Il faut un double reset du krbtgt, la suppression des 3 comptes cachés, le retrait de la GPO malveillante, et la correction des ACL. La reconstruction complète de l'AD n'est pas strictement nécessaire si ces actions sont menées proprement, mais le risque résiduel n'est pas nul. »

---

### Chapitre 21 — Investigation réseau et exfiltration

#### 21.1 Identification des communications C2

Les communications C2 (Command and Control) sont le lien entre le malware et l'attaquant. Leur identification est un objectif prioritaire de l'investigation réseau car elles révèlent les machines compromises et les destinations de l'attaquant.

Le **beaconing** est le pattern le plus courant : le malware contacte le C2 à intervalles réguliers (toutes les 30 secondes, toutes les 5 minutes) pour recevoir des instructions. Les attaquants sophistiqués ajoutent du jitter (variation aléatoire de l'intervalle) pour simuler du trafic humain, mais le pattern reste détectable par analyse statistique. Le **DNS tunneling** utilise les requêtes DNS pour encapsuler des données — un volume anormal de requêtes DNS vers un même domaine, ou des requêtes avec des sous-domaines longs et encodés, sont des indicateurs. Le **fingerprinting TLS** (JA3/JA4) permet d'identifier des clients TLS suspects même sur du trafic chiffré — le hash JA3 du client TLS d'un malware est souvent distinct de celui d'un navigateur légitime.

#### 21.2 Identification de l'exfiltration

L'exfiltration est souvent la composante la plus difficile à détecter et à quantifier. Les indicateurs incluent un volume anormal de trafic sortant par rapport à la baseline, des flux vers des services cloud non autorisés (Mega, file.io, transfer.sh, ou des instances AWS/Azure/GCP louées à la demande), des connexions longue durée vers des IP inconnues, et l'utilisation d'outils de transfert identifiables (rclone a un user-agent caractéristique dans les logs proxy, WinSCP et FTP ont des empreintes réseau spécifiques).

L'estimation du volume exfiltré est cruciale pour la CNIL (la notification doit indiquer le nombre de personnes et le type de données concernées), pour la communication de crise (« avons-nous perdu nos secrets industriels ? »), et pour la décision sur la rançon (si les données sont déjà exfiltrées, payer ne les « dé-exfiltrera » pas).

Le cas du **living off trusted services** : les attaquants utilisent de plus en plus des services légitimes pour l'exfiltration (AWS S3, Azure Blob, Google Drive, OneDrive). Ces flux passent les contrôles de sécurité (les domaines sont réputés légitimes) et sont invisibles aux filtres URL. La détection repose sur l'identification des outils (rclone, aws-cli) via les user-agents proxy, l'analyse volumétrique, et la corrélation avec les autres IoC.

#### 21.3 Fil rouge — BLACKTIDE : l'exfiltration

> **🔍 BLACKTIDE — Épisode 21**
>
> Karim analyse les logs proxy (Squid) pour reconstituer l'exfiltration. Il identifie des connexions HTTPS vers `s3.eu-west-1.amazonaws.com` depuis 3 machines internes (10.42.15.87, 10.42.15.92, 10.42.10.45), totalisant 380 Go sur 7 jours (J-7 à J-0). Le user-agent est `rclone/v1.65.0` — confirmant l'utilisation de rclone, un outil de synchronisation cloud légitime détourné par l'attaquant.
>
> Les données exfiltrées sont identifiées par corrélation avec les logs d'accès aux partages de fichiers (Event ID 5140/5145) : accès massif aux partages `\\FS01-Lyon\R&D`, `\\FS01-Fos\Projets`, et `\\FS01-Lyon\RH` dans les 7 jours précédant l'exfiltration. Le volume se répartit en environ 310 Go de données R&D (formules chimiques, procédés de fabrication, brevets en cours) et 70 Go de données RH (fiches de paie, contrats, données de sécurité sociale de 8 000 employés).
>
> Le serveur de staging est une instance EC2 AWS en région `eu-west-1` (Irlande). L'identification du locataire nécessitera une réquisition judiciaire auprès d'AWS.

---

### Chapitre 22 — Investigation des environnements hybrides, OT et dépendances tierces

*Ce chapitre est un panorama qui traite trois environnements d'investigation spécifiques, chacun avec ses propres contraintes. Il assume explicitement un traitement moins approfondi que les chapitres précédents sur chaque volet, en renvoyant vers les cours spécialisés de la bibliothèque.*

#### 22.1 Investigation cloud (Microsoft 365 / Entra ID)

Les compromissions cloud suivent des logiques différentes de l'on-premise. L'attaquant ne « compromet » pas un serveur — il vole un token, il abuse d'un consentement OAuth, il modifie une conditional access policy. L'investigation repose sur les **Sign-in Logs** d'Entra ID (connexions, y compris les échecs, avec géolocalisation et device info), les **Unified Audit Logs** (toutes les actions administratives et utilisateur dans M365 — création de règles de forwarding, accès aux mailboxes, modifications de configuration, ajout d'app registrations), et les **Azure Activity Logs** (si Azure IaaS/PaaS est utilisé).

Les pièges spécifiques au cloud : la rétention des logs dépend de la licence (180 jours en E3, jusqu'à 365 jours en E5 pour certains types de logs), les tokens volés permettent un accès persistant même après reset du mot de passe (il faut révoquer explicitement les refresh tokens), et les app registrations malveillantes peuvent fournir un accès API permanent sans interaction utilisateur.

#### 22.2 Investigation OT/ICS

L'investigation en environnement OT (Operational Technology) est contrainte par des réalités physiques que l'IT ne connaît pas. Les systèmes ne sont pas patchables (un automate en production ne peut pas être redémarré pour appliquer un correctif), les protocoles sont propriétaires (Modbus, S7, OPC-UA — les outils d'investigation réseau classiques ne les comprennent pas), les logs centralisés sont rares (les automates n'envoient pas de syslog au SIEM), les agents EDR ne peuvent pas être déployés sur les PLC (Programmable Logic Controllers), et les contraintes de disponibilité sont extrêmes (arrêter un automate dans une usine chimique peut causer un accident physique).

La plupart des incidents OT commencent par une compromission IT qui pivote vers le réseau OT via les passerelles de supervision (SCADA), les jump servers, ou les postes d'ingénierie à double connexion (un poste connecté à la fois au réseau IT et au réseau OT — c'est exactement le cas de BLACKTIDE). L'investigation OT est donc souvent une extension de l'investigation IT, menée conjointement avec les ingénieurs de production.

L'évaluation critique : l'attaquant a-t-il atteint les systèmes de contrôle ? A-t-il modifié des configurations d'automates ? A-t-il la capacité de causer un dommage physique ? Ces questions déterminent le niveau d'urgence et la mobilisation de compétences spécialisées (CERT-FR dispose d'équipes OT déployables sur les OIV).

#### 22.3 Investigation supply chain et dépendances tierces

Quand l'incident provient d'un tiers de confiance (mise à jour logicielle piégée, accès VPN prestataire compromis, dépendance SaaS compromise), l'investigation dépasse le périmètre de l'organisation. Le scoping doit considérer tous les systèmes ayant interagi avec le tiers compromis, la coordination avec le fournisseur est indispensable (mais souvent lente, juridiquement complexe, et politiquement sensible), et l'évaluation de l'impact doit considérer le cas où le tiers a été un vecteur vers d'autres clients.

Dans le cas de BLACKTIDE, le point d'entrée est la compromission du sous-traitant RH GestPaie — un cas classique de supply chain via prestataire. L'infostealer sur le poste du DRH de GestPaie a fourni les credentials VPN d'Arvantis. La question de la responsabilité contractuelle (GestPaie avait-elle une obligation de MFA sur ses postes ?) est un enjeu juridique post-incident.

#### 22.4 Fil rouge — BLACKTIDE : les volets spécifiques

> **🔍 BLACKTIDE — Épisode 22**
>
> **Cloud :** l'attaquant a utilisé un token volé d'un admin M365 (obtenu via le DCSync — le hash NTLM du compte a permis un pass-the-hash vers Entra ID via Azure AD Connect sync). Il a créé une règle de forwarding sur la boîte mail du CFO (toutes les PJ PDF redirigées vers une adresse ProtonMail externe). La règle est active depuis J-10. Les UAL E3 (180 jours) permettent de confirmer qu'aucune autre manipulation M365 n'a eu lieu.
>
> **OT :** le site OIV de Fos-sur-Mer utilise un SCADA Schneider Electric pour le contrôle des réacteurs. L'investigation révèle que l'attaquant a atteint le poste d'ingénierie OT (Windows 10, connecté au réseau IT via un second adaptateur réseau — la segmentation IT/OT reposait uniquement sur un VLAN, pas sur un pare-feu physique). Le ransomware a chiffré le poste d'ingénierie mais PAS les PLC Schneider (pas de système de fichiers Windows sur les automates). L'ANSSI déploie une équipe CERT-FR spécialisée OT le lundi pour vérifier l'intégrité des configurations SCADA.
>
> **Supply chain :** GestPaie est notifié de la compromission de son poste DRH le samedi matin. Réponse : « On va regarder. » Arvantis désactive immédiatement l'accès VPN de GestPaie et demande un audit de sécurité contractuel (la clause existe dans le contrat de prestation).

---

## PARTIE V — CONFINEMENT, DÉCISION ET PRÉSERVATION DE PREUVE

*L'étendue de la compromission est estimée. Il faut contenir l'attaquant, préserver les preuves, et prendre des décisions critiques — souvent avec des informations incomplètes.*

---

### Chapitre 23 — Stratégies de confinement et arbitrages

#### 23.1 Le dilemme fondamental

Contenir **trop tôt** alerte l'attaquant. S'il détecte que ses connexions C2 sont coupées ou que ses comptes sont désactivés, il peut réagir de manière destructrice : accélérer le chiffrement, activer un wiper, supprimer les logs, ou activer un mécanisme de persistance de secours. Contenir **trop tard** lui laisse le temps d'aggraver les dégâts : chiffrer davantage de systèmes, exfiltrer davantage de données, s'enraciner plus profondément.

Le timing optimal dépend du type d'attaque. **Ransomware en cours de déploiement** : confinement immédiat — chaque minute de retard signifie des dizaines de machines chiffrées en plus. La course contre le chiffrement est réelle. **Espionnage discret** : observation contrôlée possible — si l'attaquant ne sait pas qu'il est détecté, continuer à l'observer permet de comprendre l'étendue complète de la compromission avant de le couper. **Compromission de compte sans activité destructrice** : désactivation immédiate du compte — l'impact est limité et la mesure est réversible.

#### 23.2 Confinement réseau

Les options de confinement réseau, de la plus chirurgicale à la plus radicale : isolation de machines spécifiques via EDR (network containment — la machine reste allumée mais ne peut plus communiquer, sauf avec la console EDR), isolation de segments via ACL pare-feu ou VLAN (couper les flux entre segments compromis et segments sains), coupure de l'accès Internet ciblée (bloquer les communications C2 sans couper toute la production), coupure de l'accès Internet totale (couper toutes les communications externes — radical mais efficace contre les ransomwares qui utilisent un C2 pour le chiffrement), et isolation inter-sites (couper les liens WAN entre sites pour empêcher la propagation d'un site compromis vers les autres).

Chaque option a un impact business mesurable. L'isolation d'un segment serveur arrête les services hébergés. La coupure Internet arrête les emails, le VPN, les services cloud, et potentiellement les systèmes de paiement. L'isolation inter-sites empêche la collaboration entre sites. Ces impacts doivent être évalués AVANT la décision, en concertation avec les métiers.

#### 23.3 Confinement des comptes

Désactivation des comptes compromis (identifiés par l'investigation), reset des mots de passe des comptes à privilèges (la question du timing : quand fait-on le reset massif ?), révocation des sessions et tokens (M365, VPN, SSO, OAuth), rotation des secrets de service (mots de passe des comptes de service, clés API, certificates), et désactivation des accès tiers (VPN prestataires, interconnexions partenaires).

Le risque de lock-out massif : un reset de tous les mots de passe du domaine un samedi matin bloquera les 12 000 utilisateurs lundi matin s'il n'est pas coordonné avec une communication claire et un mécanisme de reset autonome (portail de self-service, assistance téléphonique renforcée).

#### 23.4 Fil rouge — BLACKTIDE : la décision de confinement

> **🔍 BLACKTIDE — Épisode 23**
>
> Samedi 15 mars, 01h30. Le ransomware est en cours de déploiement. Nadia présente 3 options à la cellule de crise technique (Marc/RSSI valide).
>
> | Option | Action | Impact business | Risque sécurité |
> |--------|--------|----------------|----------------|
> | A — Chirurgical | Isoler les 3 DC + 40 machines identifiées via EDR | Production maintenue sauf serveurs de fichiers | Élevé — des machines compromises non identifiées restent actives |
> | B — Sites touchés | Coupure Internet + isolation inter-sites pour Fos, Lyon, Cologne | Production arrêtée sur 3 sites (40 % de la capacité) | Modéré — le confinement couvre le périmètre connu |
> | C — Total | Coupure réseau complète d'Arvantis | Production arrêtée partout (800 K€/jour) | Faible — tout est coupé |
>
> **Décision : Option B.** Les 3 sites touchés sont isolés (coupure Internet, isolation WAN inter-sites). Les 12 autres sites maintiennent leur activité avec surveillance renforcée et blocage des flux venant des 3 sites isolés. Le site OIV de Fos est isolé en priorité. La production est arrêtée sur les 3 sites impactés.

---

### Chapitre 24 — Confinement par type d'incident

Ce chapitre détaille les stratégies de confinement spécifiques aux types d'incidents les plus courants.

**Ransomware :** confinement réseau immédiat des segments touchés (priorité absolue), isolation du C2 (blocage du domaine/IP au pare-feu), protection immédiate des sauvegardes (déconnexion physique du NAS si sur le même réseau), vérification de l'intégrité des sauvegardes offline. Ne PAS éteindre les machines avant collecte forensic (la RAM contient des preuves critiques).

**Compromission de compte / BEC :** désactivation du compte, reset du mot de passe, révocation de toutes les sessions actives, vérification des règles de forwarding email, notification aux contacts qui ont pu recevoir des emails frauduleux.

**Exfiltration / espionnage :** bloquer le canal d'exfiltration identifié (mais attention : l'attaquant peut avoir plusieurs canaux), évaluer si l'observation contrôlée est préférable au confinement immédiat (pour comprendre l'étendue avant de couper).

**OT :** confinement de l'interface IT/OT (coupure des passerelles de supervision, isolation du réseau OT via le pare-feu IT/OT), vérification de l'intégrité des configurations d'automates avec les ingénieurs de production. Ne JAMAIS redémarrer un automate sans validation des ingénieurs — un automate dans un état intermédiaire peut causer un accident physique.

**Supply chain :** isolation immédiate du lien avec le tiers compromis (désactivation VPN, blocage des flux réseau, révocation des API keys), notification du fournisseur.

---

### Chapitre 25 — Préserver les preuves sous pression

#### 25.1 L'ordre de volatilité

La collecte de preuves doit suivre l'ordre de volatilité — du plus éphémère au plus durable. La **mémoire vive** s'efface à l'extinction (collecte en 10-20 minutes avec DumpIt). L'**état des processus et connexions réseau** est dynamique (capture via EDR ou ligne de commande). Les **fichiers temporaires et artefacts système** persistent jusqu'à écrasement. Les **logs** persistent jusqu'à rotation (jours à mois). Les **disques** persistent indéfiniment (sauf chiffrement par le ransomware).

Le principe fondamental : collecter AVANT ou PENDANT le confinement, pas après. Le confinement peut impliquer l'extinction de machines (perte de RAM), la modification de configurations réseau (perte de l'état réseau), ou la restauration de systèmes (écrasement des artefacts).

#### 25.2 Chaîne de custody

Chaque acquisition est documentée avec un formulaire de chaîne de custody (template en Annexe C) : identifiant unique de la preuve, description (machine, type d'acquisition), analyste responsable, date et heure de l'acquisition, outil et version utilisés, hash SHA256 de l'image ou du fichier, lieu de stockage, et journal des accès ultérieurs.

#### 25.3 Les erreurs qui détruisent les preuves

Redémarrer un serveur compromis sans collecte mémoire préalable (RAM perdue — irréversible). Lancer un scan antivirus qui supprime ou met en quarantaine le malware (sample perdu — le hash est peut-être préservé dans les logs, mais le binaire est détruit). Restaurer un système depuis une sauvegarde avant acquisition forensic (tous les artefacts écrasés). Modifier des configurations réseau avant capture de l'état (connexions actives perdues). Ne pas documenter les actions prises (impossible de reconstituer la séquence pour le retex ou la procédure judiciaire).

Chacune de ces erreurs est commise régulièrement par des administrateurs IT qui agissent de bonne foi mais sans formation IR. La formation des IT à « ne pas toucher avant le forensic » est un investissement de préparation critique (Ch.5).

#### 25.4 Fil rouge — BLACKTIDE : la preuve perdue

> **🔍 BLACKTIDE — Épisode 25**
>
> Deux serveurs de fichiers (FS01-Lyon et FS01-Fos) ont été redémarrés par David (admin astreinte) à 23h30, avant l'arrivée du PRIS. Nadia documente factuellement : « Serveurs redémarrés sans collecte préalable — cause : absence de procédure. Conséquence : perte de la RAM et des artefacts de session. » Elle note dans ses recommandations RETEX : « Former les admins d'astreinte au premier réflexe IR : NE PAS redémarrer, APPELER l'IR lead. »

---

### Chapitre 26 — Décider sous incertitude

#### 26.1 La réalité de la prise de décision en IR

L'IR n'est pas seulement collecter, analyser, contenir. C'est **décider** — et décider avec des informations incomplètes, des contraintes métiers contradictoires, des coûts immédiats, des conséquences juridiques potentielles, et un stress intense.

À aucun moment de l'incident l'équipe IR ne dispose de « toutes les informations ». Le scoping est toujours approximatif. L'étendue de la compromission est toujours sous-estimée dans les premières heures. Le volume de données exfiltrées n'est jamais connu avec précision tant que l'investigation n'est pas terminée — et l'investigation prend des jours.

La discipline de décision consiste à expliciter ce qu'on sait, ce qu'on ne sait pas, et ce qu'on suppose, puis à décider en connaissance de cause de cette incertitude — pas à attendre la certitude qui ne viendra pas.

#### 26.2 Arbitrage sécurité vs production

La sécurité veut isoler le réseau (pour contenir). La production veut maintenir le réseau (pour ne pas arrêter les usines). Les deux ont raison dans leur logique. L'arbitrage est une décision de direction, pas une décision technique — mais la direction a besoin de données claires pour décider.

L'IR lead doit formuler des **options** (pas une recommandation unique), avec pour chaque option : l'impact sécurité (quel risque accepte-t-on ?), l'impact business (quel coût subit-on ?), les conséquences (que se passe-t-il si l'option se révèle insuffisante ?), et la réversibilité (peut-on revenir en arrière ?).

#### 26.3 Erreurs réversibles vs irréversibles

Un principe directeur en situation d'incertitude : **privilégier les actions réversibles**. Isoler un serveur via EDR est réversible (on peut lever l'isolation en un clic). Éteindre un serveur sans collecte mémoire est irréversible (la RAM est perdue pour toujours). Restaurer un système depuis une sauvegarde est irréversible (les artefacts forensic sont écrasés). Communiquer publiquement est irréversible (on ne peut pas « dé-communiquer »). Payer une rançon est irréversible (l'argent est parti).

Quand deux options offrent un niveau de sécurité comparable, choisir la plus réversible.

#### 26.4 Documentation des décisions

Chaque décision significative est documentée dans le journal d'incident : qui a décidé, quand, sur la base de quelles informations (y compris les incertitudes), quelles alternatives ont été considérées, et pourquoi cette option a été retenue. Cette documentation protège les décideurs (ils ont agi raisonnablement avec les informations disponibles), alimente le retex (quelles informations manquaient pour mieux décider ?), et sert de preuve de bonne foi en cas de contentieux.

#### 26.5 Comment formuler des options à la direction

La direction ne veut pas un briefing technique de 30 minutes. Elle veut 3 options, chacune sur une ligne, avec : ce qu'on fait, ce que ça coûte en arrêt de production, ce que ça risque en termes de sécurité, et le délai de reprise estimé. Un tableau situation/options/risques/recommandation sur une page, avec un niveau de confiance explicite, est le format le plus efficace.

#### 26.6 Fil rouge — BLACKTIDE : les arbitrages du COMEX

> **🔍 BLACKTIDE — Épisode 26**
>
> Samedi 10h00. Réunion de la cellule de crise exécutive. Le CEO, Pierre Gautier, pose la question directe : « On redémarre quand ? »
>
> Marc (RSSI) présente le tableau des options de reprise (voir Ch.3, épisode BLACKTIDE). Le CEO choisit l'option B (reprise contrôlée, J+5 à J+12). La décision est documentée dans le PV de la réunion de crise, avec les réserves du RSSI (« le risque résiduel de l'option B n'est pas nul — nous recommandons un threat hunting post-reprise de 4 semaines ») et la signature du CEO.
>
> Deuxième arbitrage : la demande de rançon de 4,2 M€ arrivée à 09h00 via le portail de négociation PhantomCrypt. Le RSSI recommande de ne pas payer (les sauvegardes offline sont intactes, la production peut reprendre sans les données chiffrées). Le directeur juridique confirme qu'il n'y a pas d'obligation de payer, et que le paiement pourrait exposer Arvantis à des risques si l'opérateur est sanctionné par l'OFAC. Le CEO valide : pas de paiement. Décision documentée.

---

## PARTIE VI — ÉRADICATION, RECONSTRUCTION ET REPRISE

*L'attaquant est identifié, le périmètre est connu, les mécanismes de persistance sont cartographiés. Il faut éradiquer, reconstruire, valider, et reprendre — sans réintroduire la compromission.*

---

### Chapitre 27 — Plan d'éradication coordonné

#### 27.1 Éradication simultanée, pas séquentielle

Si l'éradication est menée machine par machine, l'attaquant réinfecte les machines nettoyées depuis les machines non encore traitées. Le plan d'éradication doit être coordonné : un « jour J » est planifié (typiquement quelques jours après la fin de l'investigation, le temps de préparer toutes les actions), et toutes les mesures d'éradication sont exécutées simultanément dans une fenêtre courte (4 à 8 heures).

Le plan d'éradication liste exhaustivement toutes les actions à mener, l'ordre d'exécution (certaines actions dépendent d'autres — le double reset du krbtgt doit être fait avant le reset massif des comptes), les responsables de chaque action, et les validations post-exécution (comment vérifie-t-on que chaque action a réussi ?).

#### 27.2 Suppression des mécanismes de persistance

Pour chaque mécanisme identifié au Ch.20 : suppression des tâches planifiées malveillantes (vérification sur tout le parc via Velociraptor ou GPO de nettoyage), désinstallation des services Windows parasites (identification par nom, chemin, et hash), nettoyage des clés de registre Run/RunOnce, suppression des comptes créés par l'attaquant (après documentation — les comptes sont une preuve), retrait de la GPO malveillante (suppression complète, pas simple désactivation), suppression des règles de forwarding email (vérification de toutes les boîtes mail du domaine, pas seulement celles identifiées), révocation de tous les tokens cloud (M365, Azure, AWS — forcer une réauthentification complète), retrait des clés SSH non autorisées (vérification de tous les serveurs Linux), et correction des ACL/DACL modifiées sur l'AD (retour aux permissions d'origine, documentées).

#### 27.3 Le cas du krbtgt compromis

Quand le hash du krbtgt est compromis (DCSync confirmé), l'attaquant peut forger des Golden Tickets — des TGT qui ne seront pas invalidés par un simple reset des mots de passe utilisateurs. Le seul remède est le **double reset du krbtgt** : deux resets du mot de passe du compte krbtgt espacés de 12 heures minimum.

Pourquoi deux resets ? Kerberos retient les 2 derniers mots de passe du krbtgt (pour permettre la transition sans interruption de service). Un seul reset invalide le mot de passe N-1 mais les tickets forgés avec le mot de passe N (celui que l'attaquant connaît) restent valides tant que N est l'un des 2 derniers mots de passe. Le second reset pousse N en position N-2 (plus retenu par Kerberos), invalidant tous les Golden Tickets.

Procédure : premier reset du krbtgt à T0, vérification du fonctionnement de l'authentification Kerberos (les perturbations sont normalement limitées mais possibles — surveiller les tickets de service), second reset à T0+12h minimum (certaines recommandations préconisent T0+24h pour plus de sécurité), re-vérification du fonctionnement.

Le double reset du krbtgt impacte le fonctionnement de Kerberos pendant la transition — tous les TGT en circulation deviennent invalides et doivent être renouvelés. L'impact est généralement transparent (les systèmes renouvellent automatiquement) mais peut causer des dysfonctionnements sur les systèmes legacy ou mal configurés. Le reset doit être planifié dans la fenêtre d'éradication avec une surveillance active des dysfonctionnements.

#### 27.4 Fil rouge — BLACKTIDE : le jour J

> **🔍 BLACKTIDE — Épisode 27**
>
> Le « jour J » est planifié pour le mercredi 19 mars, de 22h à 04h (fenêtre de maintenance). L'équipe est constituée de 4 analystes internes + 2 consultants PRIS + 3 admins système.
>
> Séquence d'éradication :
> 1. 22h00 : Premier reset du krbtgt sur DC01.
> 2. 22h15 : Suppression des 3 comptes admin cachés (svc_monitor01, svc_backup_ext, svc_audit_temp).
> 3. 22h30 : Suppression de la GPO « Windows Update Configuration ».
> 4. 22h45 : Nettoyage des scheduled tasks malveillantes sur les 40+ machines (via Velociraptor — exécution centralisée).
> 5. 23h00 : Correction des ACL sur l'OU des serveurs critiques (retrait du GenericAll de svc_deploy).
> 6. 23h15 : Révocation de tous les tokens M365 (forçage de réauthentification).
> 7. 23h30 : Désactivation du compte VPN `admin_rh_ext` (sous-traitant GestPaie).
> 8. 00h00 : Rotation de tous les mots de passe des comptes de service (25 comptes).
> 9. 10h00 (J+1) : Second reset du krbtgt (T0+12h).
> 10. 12h00 : Forçage du changement de mot de passe pour TOUS les comptes utilisateurs du domaine (12 000 comptes — communication préparée, helpdesk renforcé pour le lundi).

---

### Chapitre 28 — Reconstruction des systèmes

#### 28.1 Reconstruire plutôt que nettoyer

Le principe fondamental de la reconstruction post-incident : un système compromis ne peut jamais être « nettoyé » avec certitude absolue. Le nettoyage (suppression du malware visible, patchs, reset des configurations) laisse un doute résiduel — l'attaquant a pu installer un mécanisme de persistance non détecté par l'investigation (rootkit, firmware implant, backdoor dans un fichier système légitime). Le seul moyen fiable de garantir l'éradication est la reconstruction à partir de sources propres : images gold (images système de référence, maintenues à jour), sauvegardes vérifiées antérieures à la compromission, ou installation fraîche depuis les médias d'origine.

En pratique, la reconstruction complète de tout le parc est rarement réalisable (trop long, trop coûteux). L'approche courante est un mix : reconstruction des systèmes critiques (DC, serveurs d'infrastructure, serveurs sensibles), nettoyage vérifié des systèmes moins critiques (postes de travail — réinstallation du poste si compromission confirmée, scan EDR approfondi sinon), et surveillance renforcée post-éradication (Ch.29) pour détecter une persistance non identifiée.

#### 28.2 Reconstruction par cercles de confiance

L'infrastructure est reconstruite en 3 cercles concentriques. Le **cercle 1 (noyau de confiance)** comprend les DC, le DNS interne, la PKI, l'infrastructure de sécurité (EDR console, SIEM, serveur de logs). Ces systèmes sont reconstruits en premier, à partir d'images gold, sur un réseau isolé. Ils forment le « noyau dur » à partir duquel le reste est déployé. Le **cercle 2 (services critiques)** comprend les serveurs de fichiers, la messagerie, les applications métier essentielles, le VPN, les portails clients. Ils sont reconstruits ou restaurés une fois le cercle 1 validé. Le **cercle 3 (reste du parc)** comprend les postes de travail, les services secondaires, les applications non critiques. Chaque cercle n'est reconnecté au réseau de production qu'après vérification complète du cercle précédent.

#### 28.3 Restauration des données

La restauration des données (à distinguer de la reconstruction des systèmes) pose des questions spécifiques. Les sauvegardes sont-elles intactes ? (si elles sont chiffrées par le ransomware, elles sont inutilisables). Sont-elles antérieures à la compromission ? (attention au dwell time — si la compromission a commencé il y a 5 semaines et que les sauvegardes ont 4 semaines, elles contiennent potentiellement le malware ou des backdoors). Contiennent-elles des données exploitables ? (une sauvegarde de données utilisateur est différente d'une sauvegarde d'image système — restaurer les données sur un système reconstruit proprement est la bonne approche, restaurer une image système potentiellement compromise est la mauvaise).

Stratégie recommandée : restaurer les DONNÉES sur des SYSTÈMES reconstruits proprement (pas les images système depuis des sauvegardes qui pourraient être compromises). Vérifier l'intégrité des données restaurées (scan EDR, recherche d'artefacts malveillants).

#### 28.4 Fil rouge — BLACKTIDE : la reconstruction

> **🔍 BLACKTIDE — Épisode 28**
>
> La reconstruction suit le modèle par cercles de confiance.
>
> **Cercle 1 (J+5 à J+7) :** 3 DC reconstruits à partir d'images gold Windows Server 2022, durcis selon les recommandations CIS Benchmark. L'AD est nettoyé en profondeur (option a du Ch.28 — pas de reconstruction complète, car la compromission est bien délimitée après le double reset krbtgt et la suppression des comptes/GPO/ACL). SIEM Splunk vérifié. Console EDR CrowdStrike vérifiée.
>
> **Cercle 2 (J+7 à J+10) :** Serveurs de fichiers reconstruits (installation fraîche Windows Server 2022). Données restaurées depuis les sauvegardes hebdomadaires sur bandes offline — intactes, mais avec 6 jours de perte de données (les sauvegardes quotidiennes sur NAS réseau sont partiellement chiffrées — inutilisables). Messagerie Microsoft 365 : tokens révoqués, conditional access policies renforcées, règles de forwarding malveillantes supprimées.
>
> **Cercle 3 (J+10 à J+12) :** Postes de travail des 3 sites impactés : les postes confirmés compromis (12 machines) sont réinstallés. Les autres subissent un scan EDR approfondi et un reset de l'utilisateur local admin (LAPS activé à cette occasion).

---

### Chapitre 29 — Validation d'éradication et surveillance post-nettoyage

#### 29.1 Comment savoir qu'on a vraiment éradiqué

L'éradication n'est pas un acte ponctuel (« on a supprimé le malware, c'est fini ») mais un processus qui se valide dans la durée. La question « l'attaquant est-il vraiment parti ? » ne peut jamais recevoir une réponse avec certitude absolue — mais la confiance se construit par accumulation de vérifications positives et absence de réapparition.

#### 29.2 Checklist de validation technique

Après l'éradication, une checklist de contrôle est exécutée sur l'ensemble du parc. Aucun processus malveillant actif (scan EDR complet — tous les endpoints, pas un échantillon). Aucune tâche planifiée non légitime (script de vérification exécuté via Velociraptor sur tout le parc). Aucun service Windows non répertorié. Aucun compte non autorisé dans les groupes privilégiés (audit AD complet). Aucune GPO non légitime (revue de toutes les GPO). Aucune règle de forwarding email non légitime (audit de toutes les boîtes mail M365). Aucun flux réseau vers les destinations C2 identifiées (monitoring continu proxy + pare-feu). Intégrité vérifiée des fichiers système critiques.

#### 29.3 Hunts post-nettoyage

Pendant 2 à 4 semaines après l'éradication, un threat hunting ciblé est mené en continu. Les hypothèses de hunting sont dérivées directement de l'attaque observée. « L'attaquant utilisait des scheduled tasks pour la persistence → chercher toute nouvelle scheduled task créée depuis le jour J. » « L'attaquant utilisait rclone pour l'exfiltration → chercher tout processus rclone ou tout flux vers S3/Blob/Cloud storage. » « L'attaquant avait un Golden Ticket → monitorer les anomalies Kerberos (TGT avec lifetime anormal, authentifications sans pré-authentification). »

Si le hunting révèle des traces, l'éradication est incomplète et le cycle recommence (investigation complémentaire → éradication complémentaire → validation).

#### 29.4 Seuil de confiance

Après 3 à 4 semaines de surveillance renforcée sans détection de réapparition, l'éradication est déclarée réussie avec un niveau de confiance « élevé — risque résiduel faible ». Ce seuil est documenté : il ne signifie pas « certitude absolue » mais « confiance suffisante pour un retour à la normale, avec un monitoring standard ». Le risque résiduel (un mécanisme de persistance non détecté, une porte d'entrée secondaire non identifiée) est accepté explicitement et géré par la surveillance continue.

#### 29.5 Fil rouge — BLACKTIDE : la validation

> **🔍 BLACKTIDE — Épisode 29**
>
> 3 semaines de surveillance renforcée post-éradication. Hunting quotidien sur les IoC PhantomCrypt (hash, domaines C2, patterns de beaconing). Monitoring continu des flux réseau vers les IP/domaines identifiés. Audit AD hebdomadaire via PingCastle (score passé de D à B après le durcissement). Scan EDR approfondi de tout le parc (100 % — y compris les 8 % auparavant non couverts, sur lesquels l'EDR a été déployé en urgence pendant l'incident).
>
> Résultat : aucun indicateur de réapparition après 3 semaines. Marc (RSSI) déclare l'éradication réussie avec un niveau de confiance « élevé ».

---

### Chapitre 30 — Reprise d'activité

#### 30.1 Priorisation des services

La reprise ne se fait pas en « big bang » — elle est progressive et priorisée en fonction de l'impact business. Les services critiques (messagerie, VPN pour le télétravail, systèmes de production industrielle, systèmes de paiement) reprennent en premier. Les services secondaires (applications RH, intranet, outils collaboratifs non essentiels) reprennent ensuite. Chaque service redémarré est validé fonctionnellement (le service fonctionne-t-il ?) et sécuritairement (aucun indicateur de compromission ?) avant le suivant.

#### 30.2 Critères de retour nominal

Le SI est considéré comme revenu à un état normal quand tous les systèmes sont opérationnels et les performances normales, les sauvegardes fonctionnent sur la nouvelle architecture immuable, la surveillance est revenue au niveau standard (plus de monitoring renforcé), aucune action résiduelle d'éradication n'est en cours, et les processus métiers fonctionnent sans workaround.

#### 30.3 Fil rouge — BLACKTIDE : la reprise progressive

> **🔍 BLACKTIDE — Épisode 30**
>
> La production reprend progressivement sur 12 jours (pas « lundi » comme le CEO le voulait).
> - J+5 : Messagerie M365 et VPN (12 000 utilisateurs retrouvent l'email et l'accès distant).
> - J+7 : Serveurs de fichiers restaurés (avec 6 jours de perte de données sur les bandes).
> - J+8 : Applications métier non critiques (ERP en lecture seule pour vérification).
> - J+10 : Production reprise sur les 12 sites non impactés (qui fonctionnaient en mode dégradé par précaution — interdiction des flux inter-sites levée).
> - J+12 : Production reprise sur les 3 sites impactés (Fos, Lyon, Cologne). Le site OIV de Fos est le dernier — la reprise est conditionnée à la validation conjointe ANSSI/Arvantis de l'intégrité du réseau SCADA.

---

### Chapitre 31 — Durcissement post-incident

#### 31.1 Quick wins (premières semaines)

Les quick wins sont les mesures de durcissement à impact élevé et à déploiement rapide, directement inspirées des failles exploitées pendant l'incident. Segmentation IT/OT renforcée avec pare-feu dédié (pas juste un VLAN taggé — un pare-feu physique entre le réseau IT et le réseau OT, avec filtrage applicatif). MFA obligatoire sur tous les accès externes (VPN, Microsoft 365, portails web) y compris les accès prestataires (la faille GestPaie ne se reproduira pas). LAPS (Local Administrator Password Solution) activé sur tout le parc Windows (mots de passe admin locaux uniques et rotatifs). PowerShell script block logging activé sur TOUS les postes (pas seulement les serveurs). Sauvegardes migrées vers un système immuable (stockage cloud avec MFA delete protection et versioning). Comptes break glass créés et stockés en coffre-fort physique. PingCastle exécuté mensuellement avec suivi du score.

#### 31.2 Plan structurel (mois suivants)

Les mesures structurelles nécessitent un investissement plus significatif. Tiering model AD (Tier 0 pour les DC et l'infrastructure de sécurité, Tier 1 pour les serveurs, Tier 2 pour les postes de travail — avec des comptes admin dédiés par tier, jamais réutilisés entre tiers). PAW (Privileged Access Workstations) pour les administrateurs Tier 0 (des postes dédiés, durcis, non utilisés pour la navigation ou la messagerie). Déploiement NDR pour la visibilité réseau. Upgrade licence M365 vers E5 (rétention UAL étendue). Sysmon déployé sur l'ensemble du parc Windows. Programme d'exercices de crise annuel avec la direction. Revue contractuelle des prestataires (clause MFA obligatoire pour les accès au SI).

---

### Chapitre 32 — Extorsion, rançon et arbitrages stratégiques

#### 32.1 Le paysage de l'extorsion en 2025-2026

L'extorsion cyber a considérablement évolué. La **simple extorsion** (chiffrement seul) est devenue rare — la plupart des victimes qui ont de bonnes sauvegardes refusent de payer. La **double extorsion** (chiffrement + menace de publication des données exfiltrées) est le standard depuis 2020 — même si la victime peut restaurer ses systèmes, la menace de publication de données sensibles crée une pression supplémentaire. La **triple extorsion** (chiffrement + publication + pression directe sur les clients, employés, ou partenaires de la victime) se développe — certains groupes contactent directement les clients de la victime pour les informer de la fuite, ou menacent les employés individuellement. Certains groupes abandonnent le chiffrement et ne pratiquent que l'exfiltration avec menace de publication (**pure data extortion**) — ce modèle nécessite moins de compétences techniques et génère des revenus significatifs.

#### 32.2 Payer ou ne pas payer : les arguments

**Arguments pour ne pas payer :** position de principe (ne pas financer le crime), pas de garantie que le déchiffreur fonctionnera, pas de garantie que les données ne seront pas publiées (les attaquants mentent), signal envoyé que l'organisation est une « bonne payeuse » (risque de reciblage), risque de sanctions OFAC/UE (si l'opérateur est sanctionné), et positionnement éthique (l'ANSSI et les autorités françaises recommandent de ne pas payer).

**Arguments pour payer :** quand les sauvegardes sont détruites et que l'activité ne peut pas reprendre autrement (survie de l'entreprise en jeu), quand des vies sont en danger (hôpital sans accès aux dossiers patients), quand le coût de la non-reprise dépasse significativement le montant de la rançon. Payer n'est pas illégal en France (ce n'est pas une interdiction légale mais une recommandation de l'ANSSI), mais c'est une décision stratégique avec des implications juridiques, éthiques et réputationnelles.

#### 32.3 Si la décision est de payer

Engagement d'un négociateur spécialisé (certains PRIS ou courtiers spécialisés offrent ce service — la négociation est un métier, pas une improvisation). Vérification de la liste des sanctions OFAC et de l'UE (payer une entité sanctionnée expose à des sanctions pénales). Négociation du montant (les rançons sont systématiquement négociables — des réductions de 40 à 60 % sont courantes). Test du déchiffreur sur un échantillon avant paiement complet. Documentation exhaustive pour l'assureur (si la police couvre la rançon — ce qui est de moins en moins fréquent en France depuis la loi LOPMI de 2023 qui conditionne le remboursement au dépôt de plainte dans les 72h).

#### 32.4 Gestion de la publication des données

Si la décision est de ne pas payer (ou si l'attaquant publie malgré le paiement), la publication des données sur le leak site est quasi certaine. L'organisation doit anticiper : monitoring du leak site pour détecter la publication dès qu'elle survient, communication proactive vers les personnes concernées (RGPD — notification aux personnes dont les données sont publiées), communication publique préparée (communiqué de presse factuel, validé juridiquement), et analyse des données publiées (quelles données exactement ? le volume correspond-il à l'exfiltration estimée ? y a-t-il des données de tiers ?).

#### 32.5 Fil rouge — BLACKTIDE : la rançon

> **🔍 BLACKTIDE — Épisode 32**
>
> PhantomCrypt demande 4,2 M€ en Bitcoin, avec un compte à rebours de 10 jours sur le portail de négociation. Le portail est professionnel : chat en direct, FAQ, démo de déchiffrement sur 3 fichiers gratuits.
>
> L'analyse de la direction : les sauvegardes offline (bandes) sont intactes — la production peut reprendre avec 6 jours de perte. Les données R&D exfiltrées (310 Go) seront publiées que la rançon soit payée ou non (pas de garantie de suppression). Les données RH (70 Go) seront publiées aussi. Le coût de la non-reprise est limité (les sauvegardes fonctionnent). Le coût réputationnel de la publication est réel mais gérable.
>
> **Décision : ne pas payer.** Documentée, signée par le CEO. Motifs : sauvegardes exploitables, pas de garantie sur les données, refus éthique de financer le crime. La rançon n'est pas couverte par l'assurance (exclusion contractuelle).
>
> J+10 : PhantomCrypt publie les données sur son leak site. Le DPO notifie les 8 000 employés dont les données RH sont concernées. L'image de marque est impactée — 3 articles dans la presse spécialisée, 1 article dans un quotidien national. Le cours de bourse d'Arvantis baisse de 2,3 % avant de se stabiliser.

---

## PARTIE VII — GESTION DE CRISE, COMMUNICATION ET COORDINATION

*Quand l'incident dépasse le cadre technique : piloter la crise, communiquer sous pression, coordonner les parties prenantes, et gérer les dimensions juridique et financière.*

---

### Chapitre 33 — Quand l'incident devient une crise

Ce chapitre approfondit les critères de bascule introduits au Ch.3 et détaille la dynamique de crise — ce qui change concrètement quand la gouvernance exécutive est activée. La crise se caractérise par la multiplicité des fronts (technique, communication, juridique, métier, RH, financier ouverts simultanément), l'incertitude amplifiée (la direction demande des réponses que personne ne peut encore donner), la pression temporelle démultipliée (le leak site a un compte à rebours, la CNIL attend la notification dans 72h, les clients appellent, le CA se réunit mardi), et les risques de décisions impulsives sous stress (couper tout le réseau par panique, communiquer prématurément, payer la rançon par peur).

Le passage en crise ne signifie pas que la cellule technique est dessaisie — elle continue de piloter la réponse technique. Cela signifie qu'une cellule exécutive se met en place en parallèle pour gérer les dimensions non techniques.

---

### Chapitre 34 — Cellule de crise cyber

#### 34.1 Composition

DG ou représentant mandaté (décisions stratégiques), RSSI (charnière technique/exécutif), IR lead (situation technique, en visioconférence depuis la salle technique), DRH (impact employés, communication interne), directeur juridique (obligations réglementaires, dépôt de plainte, exposition), directeur de la communication (communication externe et interne, relation presse), DPO (RGPD, CNIL), directeur des opérations/métiers (impact production, priorisation de la reprise), DSI (ressources IT, infrastructure, budgets d'urgence).

#### 34.2 Fonctionnement

Le rythme des points de situation est de toutes les 4 à 6 heures en phase aiguë (les premières 48h), puis 1 à 2 fois par jour en phase de stabilisation. Chaque point suit un format standardisé : situation technique (par l'IR lead ou le RSSI — 5 minutes, pas 30), situation communication (messages envoyés, retours reçus, demandes presse), situation juridique (notifications effectuées, plainte, assurance), décisions à prendre (options formulées, pas de discussions techniques), et prochaine échéance.

Le tableau de bord de crise résume en une page : périmètre technique (systèmes touchés / total), impact business (production arrêtée / en cours), notifications (ANSSI fait/à faire, CNIL fait/à faire, plainte fait/à faire), communication (interne fait/à faire, externe fait/à faire), et prochains jalons (prochaine décision, prochaine échéance réglementaire).

#### 34.3 Erreurs classiques de la cellule de crise

Vouloir tout décider en plénière (paralysie — les discussions techniques de 45 minutes sur les Event IDs Windows n'ont pas leur place en cellule exécutive). Mélanger la cellule technique et la cellule exécutive (l'analyste forensic et le CEO n'ont rien à se dire directement — c'est le RSSI qui fait l'interface). Changer de stratégie à chaque point de situation (inconstance — les décisions prises doivent être maintenues sauf fait nouveau majeur). Sous-estimer la durée (« ce sera réglé lundi » → ce sera réglé dans 2 semaines minimum). Et négliger la fatigue des équipes (au bout de 72h sans dormir, les décisions sont mauvaises — la rotation est un enjeu de santé ET de qualité).

---

### Chapitre 35 — Communication de crise

#### 35.1 Communication interne vers les employés

Le premier message aux employés doit être envoyé dès que les consignes de sécurité sont claires — pas avant (un message « on a un problème mais on ne sait pas quoi vous dire » est pire que le silence). Canal : si la messagerie est compromise, utiliser un canal alternatif (SMS masse, téléphone, réseau social d'entreprise s'il est hébergé hors SI, affichage physique dans les locaux).

Contenu type du premier message : « Un incident informatique majeur est en cours de traitement par nos équipes. Par précaution : ne connectez aucun appareil au réseau d'entreprise, ne cliquez sur aucun lien suspect, changez vos mots de passe dès que le service sera rétabli. Nous vous informerons régulièrement de l'évolution de la situation. »

Ce qu'il ne faut PAS dire dans le premier message : ne pas utiliser les mots « ransomware », « données volées », « piratage » tant que la communication n'est pas validée juridiquement. Ne pas minimiser (« un petit problème technique ») — les employés verront les serveurs éteints et les usines arrêtées, la minimisation détruit la crédibilité. Ne pas accuser (ni interne ni externe — les conclusions de l'investigation viendront plus tard).

#### 35.2 Communication vers la direction et le conseil d'administration

La direction a besoin d'une note de synthèse sur 2 pages maximum, en langage non technique : impact financier estimé (perte de production + frais IR + frais juridiques + impact réputationnel), état de la couverture assurantielle, calendrier de reprise (réaliste, pas optimiste), exposition juridique (notifications, plainte, sanctions potentielles), et décisions en attente (payer ou ne pas payer, communiquer ou ne pas communiquer).

#### 35.3 Communication externe : clients, partenaires, médias

La communication externe est déclenchée quand l'un des critères suivants est rempli : obligation contractuelle (certains contrats clients prévoient une notification en cas de compromission de leurs données), obligation réglementaire (RGPD si données personnelles de clients sont compromises), ou médiatisation (si l'attaquant a revendiqué publiquement, ou si un journaliste appelle, il est trop tard pour le silence — mieux vaut communiquer proactivement avec un message maîtrisé que de subir une couverture non contrôlée).

La communication médias suit des règles strictes : porte-parole unique, communiqué de presse validé juridiquement, message factuel (ce qu'on sait, ce qu'on fait, ce qu'on ne peut pas encore confirmer), et jamais de mensonge (si l'information s'avère fausse plus tard, la crédibilité est détruite et l'exposition juridique augmente).

#### 35.4 Fil rouge — BLACKTIDE : la communication

> **🔍 BLACKTIDE — Épisode 35**
>
> Samedi 14h : SMS envoyé aux 12 000 employés via la plateforme de mass SMS (hors SI). Dimanche : note au conseil d'administration (réunion téléphonique extraordinaire). Lundi : communication aux 15 principaux clients industriels (les contrats prévoient une notification). Mardi : article dans la presse spécialisée (un journaliste de LeMagIT a vu la revendication PhantomCrypt). Réaction : communiqué de presse factuel publié le mardi 14h, après validation par le directeur juridique. J+10 : publication des données. Notification individuelle aux 8 000 employés concernés (email + courrier papier pour les données les plus sensibles).

---

### Chapitre 36 — Coordination avec les parties prenantes externes

#### 36.1 ANSSI et CERT-FR

L'ANSSI est notifiée dès la confirmation de l'incident sur un OIV (obligation légale). Le CERT-FR peut fournir un appui technique (analyse de malware, partage d'IoC, déploiement d'équipes spécialisées — notamment en environnement OT). La relation est de coopération, pas de contrôle : l'ANSSI aide, elle n'inspecte pas (dans le cadre de la réponse à incident — les inspections sont un processus séparé).

#### 36.2 Forces de l'ordre

Le dépôt de plainte est recommandé même s'il n'est pas juridiquement obligatoire (sauf pour l'activation de certaines polices d'assurance — la loi LOPMI de 2023 conditionne le remboursement du sinistre cyber au dépôt de plainte dans les 72h suivant la connaissance de l'incident). Le dossier de plainte comprend un rapport technique (chronologie, IoC, dommages), une estimation des préjudices, et les preuves collectées (avec chaîne de custody). L'enquête judiciaire peut apporter des éléments utiles à l'IR (identification de l'attaquant, saisie d'infrastructure, restitution de données), mais elle est longue (mois à années) et son calendrier n'est pas synchronisé avec celui de la réponse technique.

#### 36.3 Prestataire PRIS et assureur

Le PRIS est intégré à la cellule technique, sous la coordination de l'IR lead interne. L'assureur est activé dans les conditions du contrat. L'assureur mandatera souvent ses propres experts (forensic, juridique, communication de crise) — il est important de clarifier l'articulation entre les experts de l'assureur et l'équipe IR de l'organisation pour éviter les redondances et les conflits d'intérêts.

---

### Chapitre 37 — Volet juridique, réglementaire et financier

#### 37.1 Le dépôt de plainte en détail

Plainte simple (le parquet décide de poursuivre ou non) vs plainte avec constitution de partie civile (l'organisation se constitue partie civile et peut accéder au dossier d'instruction). Le dossier de plainte technique comprend la chronologie des faits, les indicateurs de compromission, les dommages constatés (chiffrement, exfiltration, arrêt de production), et l'estimation des préjudices (directs et indirects).

#### 37.2 Le volet RGPD

La notification CNIL sous 72h comprend la nature de la violation (type de données, nombre de personnes, catégories de personnes concernées), les conséquences probables (risque d'usurpation d'identité, risque financier, risque de discrimination), et les mesures prises (confinement, éradication, notification aux personnes). La notification aux personnes concernées est obligatoire quand le risque est élevé (article 34 RGPD) — elle doit être claire, compréhensible, et inclure des recommandations concrètes (changer ses mots de passe, surveiller ses comptes bancaires, signaler toute activité suspecte).

#### 37.3 Coût total de l'incident

L'estimation du coût total est un exercice nécessaire pour le retex, pour l'assureur, et pour le conseil d'administration. Les catégories de coûts incluent les coûts directs (prestataire PRIS, reconstruction IT, outils d'urgence, heures supplémentaires), la perte d'exploitation (production arrêtée × jours × marge), les coûts juridiques (avocat, procédure, notification CNIL, notification personnes), les coûts de communication (agence de communication de crise, communiqués, notifications individuelles), les coûts de durcissement (mesures post-incident, plan structurel), et les coûts indirects (perte de clients, atteinte à la réputation, impact sur le cours de bourse, attrition des talents).

#### 37.4 Fil rouge — BLACKTIDE : le bilan financier

> **🔍 BLACKTIDE — Épisode 37**
>
> Coût total estimé : **8,5 M€**.
> - Prestataire PRIS CyberForce : 350 K€ (2 consultants × 15 jours + analyses complémentaires).
> - Reconstruction et remédiation IT : 1,2 M€ (reconstruction DC, serveurs de fichiers, sauvegardes immuables, déploiement EDR 100 %).
> - Perte de production (3 sites × 12 jours) : 3 M€.
> - Plan de durcissement structurel 18 mois : 1,5 M€ (NDR, PAW, tiering, M365 E5, Sysmon, exercices).
> - Frais juridiques et communication : 500 K€ (avocat, communication de crise, notifications CNIL + personnes).
> - Impact commercial et réputationnel estimé : 1,8 M€ (perte de contrats, dépréciation de marque).
> - Franchise assurance : 200 K€.
>
> Couverture assurance AXA XL : 3,2 M€ (frais IR + perte d'exploitation, dans la limite du plafond de 5 M€ après franchise).
> Reste à charge pour Arvantis : environ 5,3 M€.

---

## PARTIE VIII — POST-INCIDENT, MATURITÉ ET CAPITALISATION

*L'incident est clos techniquement. Le travail le plus important commence : capitaliser pour ne pas revivre la même chose. Cette partie conclut le cours avec le retex, les métriques de maturité, et un chapitre d'application synthétique.*

---

### Chapitre 38 — Clôture de l'incident et retour d'expérience (RETEX)

#### 38.1 Quand considérer l'incident clos

Critères techniques : éradication validée (Ch.29), surveillance post-nettoyage terminée sans alerte, tous les systèmes en production. Critères métiers : activité revenue à la normale, backlog rattrapé. Critères administratifs : notifications effectuées (ANSSI, CNIL), plainte déposée, assureur informé, rapport final livré, actions résiduelles attribuées et suivies.

La clôture formelle est documentée : date, décideur, synthèse des résultats, et liste des actions résiduelles avec responsables et échéances.

#### 38.2 Le RETEX structuré

Le RETEX est mené 2 à 4 semaines après la clôture (assez proche pour que les mémoires soient fraîches, assez éloigné pour avoir le recul). Il implique toutes les parties prenantes (cellule technique, cellule exécutive, IT, métiers, communication, juridique). Il suit une structure en 5 parties.

**Chronologie factuelle** : reconstitution des événements sans interprétation ni jugement. « Le serveur FS01-Lyon a été redémarré à 23h30 par l'admin d'astreinte sans collecte forensic préalable. » Pas : « L'admin d'astreinte a commis une erreur en redémarrant le serveur. »

**Ce qui a fonctionné** : détection EDR efficace (l'alerte a déclenché la réponse), escalade rapide du SOC N2, mobilisation du PRIS dans les délais contractuels, décision de ne pas payer (justifiée par les sauvegardes intactes), communication maîtrisée.

**Ce qui n'a pas fonctionné** : signaux faibles manqués (3 alertes classées faux positifs en 5 semaines), IRP jamais testé, sauvegardes quotidiennes non segmentées, absence de MFA sur le VPN prestataire, logs M365 limités (E3), comptes de service avec droits DA, redémarrage de serveurs sans collecte, absence de NDR.

**Causes racines** (Root Cause Analysis) : pourquoi le phishing a-t-il réussi ? (pas de MFA sur le VPN du sous-traitant + pas de sandbox email sur les pièces jointes). Pourquoi l'attaquant a-t-il pu progresser ? (compte de service `svc_deploy` avec droits Domain Admin et mot de passe faible). Pourquoi l'exfiltration n'a-t-elle pas été détectée ? (pas de NDR, exfiltration via services cloud légitimes, pas de DLP sur les partages).

**Recommandations priorisées** : chaque recommandation est classée par impact, faisabilité, urgence, et budget.

#### 38.3 Culture du RETEX sans blâme

Le RETEX ne fonctionne que dans un environnement de sécurité psychologique. Les participants doivent pouvoir décrire leurs erreurs sans crainte de sanction. L'admin qui a redémarré les serveurs doit pouvoir dire « j'ai redémarré les serveurs parce que je pensais que c'était la bonne chose à faire et personne ne m'avait dit de ne pas le faire » — sans être blâmé. La culture du blâme tue le RETEX : les gens cachent leurs erreurs au lieu de les documenter, et les mêmes erreurs se reproduisent.

Le RETEX vise à améliorer le système, pas à punir les individus. La question n'est pas « qui a fait une erreur ? » mais « quel processus a permis que cette erreur soit possible, et comment le corriger ? »

#### 38.4 Fil rouge — BLACKTIDE : le RETEX final

> **🔍 BLACKTIDE — Épisode 38 (conclusion du fil rouge)**
>
> Réunion RETEX le 11 avril 2026, 3 semaines après la clôture. Présents : Nadia (IR lead), Marc (RSSI), Thomas et Léa (PRIS CyberForce), Karim et Fatima (SOC), David (admin), le DPO, et un représentant de la direction générale.
>
> **15 recommandations validées :**
>
> | # | Recommandation | Priorité | Budget | Échéance |
> |---|---------------|----------|--------|----------|
> | 1 | Segmentation IT/OT physique (pare-feu dédié) | Critique | 150 K€ | J+30 |
> | 2 | Sauvegardes immuables (cloud WORM) | Critique | 80 K€/an | J+21 |
> | 3 | MFA sur tous les accès externes y compris prestataires | Critique | 30 K€ | J+14 |
> | 4 | Déploiement EDR 100 % du parc | Critique | 60 K€ | J+30 |
> | 5 | Exercice de crise annuel avec la direction | Haute | 25 K€/an | J+90 |
> | 6 | Upgrade M365 E5 (rétention logs étendue) | Haute | 200 K€/an | J+60 |
> | 7 | NDR déployé sur les segments critiques | Haute | 180 K€ | J+120 |
> | 8 | Tiering model AD (Tier 0/1/2 + PAW) | Haute | 250 K€ | J+180 |
> | 9 | Formation IR pour les admins d'astreinte | Haute | 15 K€ | J+45 |
> | 10 | Révision des comptes de service (suppression droits DA inutiles) | Haute | Interne | J+30 |
> | 11 | Sysmon déployé sur tout le parc | Moyenne | 40 K€ | J+90 |
> | 12 | Clause MFA obligatoire dans les contrats prestataires | Moyenne | Interne | J+60 |
> | 13 | DLP sur les partages de fichiers sensibles | Moyenne | 120 K€ | J+180 |
> | 14 | Playbooks IR mis à jour (AD compromis, OT, notification OIV) | Haute | Interne | J+30 |
> | 15 | Comptes break glass créés et sécurisés | Haute | 5 K€ | J+7 |
>
> Le conseil d'administration approuve un budget exceptionnel de 1,2 M€ pour le plan de durcissement, étalé sur 18 mois.

---

### Chapitre 39 — Métriques, maturité et programme IR durable

#### 39.1 Métriques de performance IR

Les métriques clés pour évaluer et améliorer la capacité IR. Le **MTTD** (Mean Time To Detect) : délai entre la compromission initiale et la détection. Pour BLACKTIDE : 35 jours (l'infostealer est resté non détecté pendant 5 semaines) — un chiffre élevé qui révèle les failles de détection. Le **MTTC** (Mean Time To Contain) : délai entre la détection et le confinement effectif. Pour BLACKTIDE : environ 3 heures (de l'alerte EDR à la décision de confinement des 3 sites) — un chiffre honorable. Le **MTTR** (Mean Time To Recover) : délai entre le confinement et la reprise complète. Pour BLACKTIDE : 12 jours — un chiffre dans la norme pour un incident de cette ampleur.

Les métriques complémentaires incluent le taux de couverture EDR (92 % → objectif 100 %), la couverture des logs critiques (PowerShell logging activé sur les serveurs seulement → objectif : tout le parc), le pourcentage du parc sans Sysmon (100 % → objectif : 0 %), et la fréquence des exercices (1 tabletop en 18 mois → objectif : 1 tabletop trimestriel, 1 technique semestriel, 1 crise annuel).

#### 39.2 Modèle de maturité IR

5 niveaux de maturité pour auto-évaluation :

**Niveau 1 — Réactif ad hoc :** Pas de processus formalisé. L'équipe IT improvise quand un incident survient. Pas d'IRP, pas de playbooks, pas de PRIS sous contrat.

**Niveau 2 — Processus défini :** Un IRP existe, les rôles sont attribués, un PRIS est sous contrat. Mais l'IRP n'est pas testé, les playbooks sont incomplets, les logs sont partiels. C'est le niveau d'Arvantis avant BLACKTIDE.

**Niveau 3 — Outillage intégré :** EDR à 100 %, SIEM avec logs complets, playbooks testés, exercices réguliers, PRIS avec SLA validé. La capacité IR fonctionne en cas d'incident mais n'est pas proactive.

**Niveau 4 — Capacité proactive :** Threat hunting régulier, purple team, exercices de crise avec la direction, métriques suivies, amélioration continue post-incidents et post-exercices. C'est l'objectif d'Arvantis à 18 mois.

**Niveau 5 — Résilience systémique :** L'IR est intégré dans la culture de l'organisation. La direction participe activement aux exercices. Les boucles de rétroaction SOC → IR → CTI → Prévention fonctionnent. Le programme IR est budgété, staffé, et évalué annuellement.

#### 39.3 Construire un programme IR durable

Un programme IR durable repose sur une équipe dimensionnée et formée (formation continue SANS/GIAC, participation aux communautés FIRST/InterCERT), un budget pérenne (investissement initial + fonctionnement annuel — le budget IR ne doit pas être une ligne « exceptionnelle » supprimée l'année suivante), un outillage maintenu (EDR, SIEM, NDR, SOAR, outils forensic — mis à jour, calibrés, testés), des contrats à jour (PRIS, assurance, exercices), une astreinte organisée (rotation, compensation, formation des astreinteurs), un entraînement régulier (exercices progressifs, participation à des CTF, sessions de retex avec d'autres organisations), et une amélioration continue (chaque incident, chaque exercice, chaque retex alimente un plan de progrès suivi trimestriellement).

L'intégration des boucles de rétroaction entre disciplines est l'indicateur de maturité le plus avancé : le SOC alimente l'IR (détection → escalade), l'IR alimente le forensic (questions → investigation), le forensic alimente la CTI (artefacts → attribution → renseignement), la CTI alimente le SOC (IoC → règles de détection), et l'IR alimente la gestion de crise (situation technique → décisions stratégiques). Le programme IR durable organise ces boucles explicitement.

---

### Chapitre 40 — Scénarios d'incident : atelier de synthèse

*Ce chapitre est conçu comme un atelier de synthèse — une mise en pratique transversale de toute la méthodologie IR enseignée dans le cours. Chaque scénario applique le processus complet : détection → qualification → investigation → confinement → éradication → reprise → RETEX. L'objectif n'est pas d'ajouter de la matière théorique nouvelle, mais de démontrer la polyvalence de la méthode sur des types d'incidents aux dynamiques distinctes.*

---

#### 40.1 Scénario 1 — Ransomware avec double extorsion (synthèse BLACKTIDE)

Synthèse intégrée du fil rouge, structurée comme un cas d'étude autonome avec les décisions clés à chaque étape. Focus sur les arbitrages spécifiques au ransomware : timing du confinement (course contre le chiffrement), gestion de la double extorsion (l'exfiltration est irréversible — payer ne la « dé-fait » pas), décision sur la rançon (tableau d'aide à la décision avec critères : sauvegardes disponibles ?, survie de l'entreprise en jeu ?, données irremplaçables ?, opérateur sanctionné ?), et reconstruction sans paiement (cercles de confiance, restauration depuis bandes).

#### 40.2 Scénario 2 — Compromission de messagerie (BEC)

Un directeur financier d'une ETI française reçoit un email de son CEO demandant un virement urgent de 2,3 M€ vers un compte à Hong Kong. L'email provient du vrai compte M365 du CEO — compromis par un phishing 3 jours plus tôt. L'investigation via les Unified Audit Logs révèle : connexion depuis une IP nigériane, création d'une règle de forwarding (tous les emails du CFO redirigés vers une boîte externe), et envoi de 12 emails frauduleux à des partenaires bancaires. Confinement : désactivation du compte CEO, révocation de tous les tokens, suppression de la règle de forwarding, alerte aux banques. L'investigation montre que le phishing initial a exploité une absence de MFA (le CEO avait refusé le MFA pour « raisons de praticité »). Le virement a été bloqué par la banque (procédure de confirmation téléphonique pour les virements internationaux > 500 K€). RETEX : MFA obligatoire pour tous, sans exception, y compris la direction.

#### 40.3 Scénario 3 — Exfiltration de données / espionnage

Une entreprise de biotechnologie française est alertée par un partenaire : des données de R&D confidentielles circulent sur un forum underground. L'investigation révèle un dwell time de 8 mois — un implant RAT installé via une clé USB trouvée dans le parking (social engineering physique). L'attaquant a exfiltré lentement (quelques centaines de Mo par semaine) via DNS tunneling, en dessous de tous les seuils d'alerte. L'AD n'est pas compromis (l'attaquant est resté avec des privilèges utilisateur standard sur un poste R&D). Confinement : isolation du poste, blocage du domaine de tunneling DNS. Le scénario illustre l'importance du NDR (le DNS tunneling aurait été détectable) et des règles DLP (l'accès massif aux fichiers R&D depuis un seul poste sur 8 mois aurait pu être alerté).

#### 40.4 Scénario 4 — Compromission supply chain

Un éditeur de logiciel de supervision industrielle publie une mise à jour contenant un implant malveillant (à la SolarWinds). L'implant est découvert 3 semaines après la mise à jour, quand un CERT sectoriel publie un advisory. 200 clients sont potentiellement touchés. L'investigation dans chaque organisation cliente doit déterminer : la mise à jour a-t-elle été installée ?, l'implant a-t-il été activé (communication C2 observée) ou est-il dormant ?, si activé, quelles actions l'attaquant a-t-il menées ? Le scénario illustre la complexité de l'IR supply chain : le périmètre est vaste (centaines de clients), la coordination avec l'éditeur est critique, et chaque client doit mener sa propre investigation.

#### 40.5 Scénario 5 — Insider threat

Un ingénieur R&D annonce sa démission pour rejoindre un concurrent. Après son départ, un audit DLP révèle : 50 Go de documentation technique copiée sur une clé USB dans les 2 semaines précédant le départ, et un upload de 15 Go vers un compte Google Drive personnel depuis le réseau d'entreprise. L'investigation forensic (analyse du poste, des logs DLP, des logs proxy) confirme les transferts. Le scénario illustre les spécificités de l'insider threat : les accès sont légitimes (pas de mouvement latéral classique), l'investigation est autant RH/juridique que technique, la gestion de la preuve doit être compatible avec une procédure disciplinaire ou pénale (vol de secrets de fabrication — article L.1227-1 du Code du travail et articles L.621-1 et suivants du Code de la propriété intellectuelle), et la communication interne est extrêmement sensible (pas de witch hunt, pas de rumeurs).

---

## ANNEXES

---

### Annexe A — Glossaire

| Terme | Définition |
|-------|-----------|
| **ACL/DACL** | Access Control List / Discretionary ACL — permissions d'accès sur les objets Active Directory ou le système de fichiers |
| **Amcache** | Artefact Windows enregistrant l'historique des programmes exécutés avec leur hash SHA1 |
| **ASN** | Autonomous System Number — identifiant d'un réseau autonome, utile pour identifier l'hébergeur |
| **ATT&CK** | Framework MITRE décrivant les tactiques, techniques et procédures des attaquants |
| **Beaconing** | Pattern de communication périodique entre un malware et son serveur C2 |
| **BEC** | Business Email Compromise — fraude par compromission de messagerie professionnelle |
| **Blast radius** | Périmètre d'impact potentiel d'un incident — nombre de systèmes, utilisateurs, données touchés |
| **BloodHound** | Outil de cartographie des chemins d'attaque dans Active Directory |
| **Break glass account** | Compte d'administration d'urgence, non lié à l'AD principal, utilisable quand le SI est compromis |
| **C2** | Command and Control — infrastructure de commande utilisée par l'attaquant pour piloter le malware |
| **Cellule de crise** | Instance de gouvernance exécutive activée lors d'un incident majeur ou d'une crise |
| **CERT-FR** | Computer Emergency Response Team de l'ANSSI — centre de réponse aux incidents pour l'État français |
| **Chain of custody** | Chaîne de traçabilité des preuves, documentant chaque manipulation d'une preuve numérique |
| **Confinement** | Ensemble des mesures visant à stopper la progression de l'attaquant et limiter l'impact |
| **CSIRT** | Computer Security Incident Response Team — équipe de réponse aux incidents de sécurité |
| **DCSync** | Technique d'attaque AD permettant de simuler un DC pour récupérer les hashes NTLM de tous les comptes |
| **DGA** | Domain Generation Algorithm — algorithme générant des noms de domaine pseudo-aléatoires pour le C2 |
| **Dwell time** | Temps de séjour — durée entre la compromission initiale et la détection de l'incident |
| **EDR** | Endpoint Detection and Response — solution de détection et réponse sur les postes et serveurs |
| **Éradication** | Phase de l'IR consistant à supprimer tous les mécanismes de compromission et de persistence |
| **Event ID** | Identifiant numérique des événements dans les Windows Event Logs |
| **Fileless malware** | Malware s'exécutant uniquement en mémoire, sans écrire de fichier sur le disque |
| **FTK Imager** | Outil d'acquisition forensic pour la création d'images disque bit-à-bit |
| **Golden Ticket** | TGT Kerberos forgé avec le hash du compte krbtgt, donnant un accès illimité au domaine AD |
| **GPO** | Group Policy Object — objet de stratégie de groupe dans Active Directory |
| **IAB** | Initial Access Broker — acteur spécialisé dans la vente d'accès initiaux compromis |
| **IRP** | Incident Response Plan — plan de réponse à incident, document cadre de la capacité IR |
| **IoC** | Indicator of Compromise — indicateur technique de compromission (hash, domaine, IP) |
| **IoA** | Indicator of Attack — indicateur comportemental d'attaque (pattern de mouvement latéral, etc.) |
| **JA3/JA4** | Fingerprinting TLS — empreinte du client TLS permettant d'identifier des connexions suspectes |
| **KAPE** | Kroll Artifact Parser and Extractor — outil de collecte automatisée d'artefacts forensic Windows |
| **Kerberoasting** | Technique d'attaque AD consistant à demander des TGS pour craquer les mots de passe des comptes de service |
| **Kill Chain** | Modèle Lockheed Martin décrivant les 7 phases d'une cyber-attaque |
| **krbtgt** | Compte Active Directory utilisé pour le chiffrement des tickets Kerberos — sa compromission permet les Golden Tickets |
| **LAPS** | Local Administrator Password Solution — solution Microsoft de gestion des mots de passe admin locaux |
| **Lateral movement** | Mouvement latéral — progression de l'attaquant d'un système à un autre au sein du réseau |
| **Loader** | Malware de première étape qui télécharge et exécute le payload principal |
| **MFT** | Master File Table — table maîtresse du système de fichiers NTFS, enregistrant tous les fichiers et métadonnées |
| **MTTC** | Mean Time To Contain — délai moyen entre la détection et le confinement effectif |
| **MTTD** | Mean Time To Detect — délai moyen entre la compromission et la détection |
| **MTTR** | Mean Time To Recover — délai moyen entre le confinement et la reprise complète |
| **NDR** | Network Detection and Response — solution de détection et réponse sur le réseau |
| **NIS 2** | Directive européenne sur la sécurité des réseaux et des systèmes d'information, version 2 |
| **OIV** | Opérateur d'Importance Vitale — organisation identifiée par l'État français comme essentielle |
| **OPSEC** | Operational Security — pratiques de sécurité opérationnelle |
| **PAW** | Privileged Access Workstation — poste dédié et durci pour l'administration privilégiée |
| **Patient zéro** | Premier système compromis dans un incident — le point d'entrée initial de l'attaquant |
| **Playbook** | Document opérationnel décrivant les actions à mener pour un type d'incident spécifique |
| **Plaso** | Outil de création de Super Timeline à partir d'artefacts forensic multiples |
| **Prefetch** | Artefact Windows enregistrant l'historique des programmes exécutés |
| **PRIS** | Prestataires de Réponse aux Incidents de Sécurité — qualification ANSSI pour les prestataires IR |
| **PsExec** | Outil Sysinternals d'exécution de processus à distance — fréquemment utilisé pour le mouvement latéral |
| **RACI** | Responsible, Accountable, Consulted, Informed — matrice de responsabilité |
| **RaaS** | Ransomware-as-a-Service — modèle franchisé de distribution de ransomware |
| **RETEX** | Retour d'expérience — analyse post-incident structurée |
| **Scoping** | Délimitation du périmètre de compromission d'un incident |
| **ShimCache** | Artefact Windows (AppCompatCache) enregistrant les programmes exécutés |
| **SIEM** | Security Information and Event Management — plateforme de collecte et corrélation des logs |
| **SitRep** | Situation Report — rapport de situation périodique pendant un incident |
| **SPN** | Service Principal Name — identifiant de service dans Active Directory, cible du Kerberoasting |
| **SRUM** | System Resource Usage Monitor — artefact Windows enregistrant la consommation réseau par processus |
| **Tiering** | Modèle de séparation des niveaux d'administration AD (Tier 0/1/2) |
| **Timeline** | Chronologie reconstituée des événements d'un incident |
| **Triage** | Évaluation rapide initiale d'un incident pour déterminer sa nature et sa gravité |
| **TTP** | Tactics, Techniques, and Procedures — méthodes opérationnelles d'un attaquant |
| **UAL** | Unified Audit Log — journal d'audit unifié de Microsoft 365 |
| **USN Journal** | Update Sequence Number Journal — journal des modifications du système de fichiers NTFS |
| **Velociraptor** | Outil de collecte forensic et de threat hunting à grande échelle |
| **Volatility** | Framework open source d'analyse de mémoire vive (RAM) |
| **WORM** | Write Once Read Many — stockage immuable, résistant au ransomware |

---

### Annexe B — Checklists opérationnelles

#### Checklist des 30 premières minutes

- [ ] Confirmer le vrai positif (exclure faux positif, maintenance planifiée)
- [ ] Identifier les systèmes visiblement impactés
- [ ] Évaluer la sévérité initiale (P1-P4)
- [ ] Augmenter le logging sur les systèmes suspects
- [ ] Sauvegarder les logs actuels (avant rotation)
- [ ] Activer la capture réseau si possible
- [ ] NE PAS redémarrer, NE PAS nettoyer, NE PAS modifier
- [ ] Escalader vers l'IR lead selon la chaîne d'escalade
- [ ] Ouvrir le canal de communication sécurisé (hors SI)
- [ ] Documenter les actions dans le journal d'incident

#### Checklist de confinement

- [ ] Décision de confinement validée par le RSSI ou l'IR lead
- [ ] Collecte forensic (RAM + triage) effectuée AVANT l'isolation
- [ ] Isolation réseau exécutée (EDR containment / VLAN / ACL pare-feu)
- [ ] Comptes compromis désactivés
- [ ] Tokens et sessions révoqués (M365, VPN, SSO)
- [ ] Sauvegardes protégées (déconnexion si sur le même réseau)
- [ ] Accès tiers compromis désactivés
- [ ] Communication au SOC : surveillance renforcée sur les IoC identifiés
- [ ] SitRep mis à jour avec le périmètre de confinement

#### Checklist de collecte forensic

- [ ] Acquisition mémoire (DumpIt/WinPmem) — AVANT tout redémarrage
- [ ] Hash SHA256 calculé immédiatement après acquisition
- [ ] Triage KAPE ou Velociraptor (artefacts Windows/Linux)
- [ ] Image disque si nécessaire (FTK Imager / dd)
- [ ] Chaîne de custody documentée (formulaire complété)
- [ ] Stockage sécurisé de la preuve (hors SI compromis)
- [ ] Sample malware isolé pour analyse (sandbox)

#### Checklist de validation post-éradication

- [ ] Scan EDR complet sur 100 % du parc
- [ ] Aucune tâche planifiée malveillante résiduelle
- [ ] Aucun service non répertorié
- [ ] Aucun compte non autorisé dans les groupes privilégiés
- [ ] Aucune GPO non légitime
- [ ] Aucune règle de forwarding email non légitime
- [ ] Aucun flux réseau vers les C2 identifiés
- [ ] Audit AD (PingCastle / Purple Knight) passé
- [ ] Threat hunting ciblé en cours (4 semaines minimum)

#### Checklist de clôture

- [ ] Éradication validée (surveillance post sans alerte)
- [ ] Tous les systèmes en production
- [ ] Notifications effectuées (ANSSI, CNIL, assureur)
- [ ] Plainte déposée
- [ ] Rapport d'incident final livré
- [ ] Actions résiduelles attribuées avec responsables et échéances
- [ ] RETEX planifié (J+14 à J+28 après clôture)
- [ ] Journal d'incident archivé

---

### Annexe C — Templates de documents IR

#### Template SitRep

```
SITREP #[N] — [NOM OPÉRATION] — [DATE HEURE]
Classification : [INTERNE / CONFIDENTIEL]

1. CE QU'ON SAIT (faits confirmés)
   - ...

2. CE QU'ON NE SAIT PAS (inconnues explicites)
   - ...

3. CE QU'ON FAIT (actions en cours)
   - ...

4. CE QU'ON ENVISAGE (prochaines étapes, options)
   - ...

5. CE DONT ON A BESOIN (ressources, décisions, autorisations)
   - ...

6. PROCHAINE ÉCHÉANCE : [date/heure]

Rédigé par : [nom]    Validé par : [nom]
```

#### Template journal d'incident

```
JOURNAL D'INCIDENT — [NOM OPÉRATION]
Ouvert le : [date heure]    IR Lead : [nom]

| Date/Heure | Auteur | Action / Observation / Décision | Source | Impact |
|-----------|--------|-------------------------------|--------|--------|
| JJ/MM HH:MM | [nom] | [description] | [source] | [impact] |
```

#### Template notification CNIL (72h)

```
NOTIFICATION DE VIOLATION DE DONNÉES PERSONNELLES
(Article 33 du RGPD)

1. NATURE DE LA VIOLATION
   Type : [confidentialité / intégrité / disponibilité]
   Description : [description factuelle]
   Date de prise de connaissance : [date]

2. CATÉGORIES DE DONNÉES CONCERNÉES
   [données d'identification, données financières, données de santé, etc.]

3. CATÉGORIES ET NOMBRE DE PERSONNES CONCERNÉES
   [nombre estimé]    [catégories : employés, clients, partenaires]

4. CONSÉQUENCES PROBABLES
   [risque d'usurpation d'identité, risque financier, etc.]

5. MESURES PRISES OU PROPOSÉES
   [mesures de confinement, d'éradication, de notification aux personnes]

6. COORDONNÉES DU DPO
   [nom, email, téléphone]
```

---

### Annexe D — Cheat sheets techniques

#### Event IDs Windows critiques pour l'IR

| Event ID | Source | Signification IR |
|----------|--------|-----------------|
| 4624 | Security | Authentification réussie — types de logon : 2 (interactif), 3 (réseau), 10 (RDP) |
| 4625 | Security | Authentification échouée — volume élevé = brute force ou password spraying |
| 4648 | Security | Logon avec credentials explicites — indicateur de mouvement latéral |
| 4672 | Security | Attribution de privilèges spéciaux — accès administrateur |
| 4688 | Security | Création de processus — nécessite l'activation de la ligne de commande |
| 4698 | Security | Création de tâche planifiée — mécanisme de persistence fréquent |
| 4720 | Security | Création de compte — activité de backdoor account |
| 4728/4732 | Security | Ajout de membre à un groupe de sécurité global/local |
| 4769 | Security | Demande de TGS Kerberos — encryption type 0x17 (RC4) = Kerberoasting |
| 4662 | Security | Opération sur objet AD — avec GUID de réplication = DCSync |
| 5136 | Security | Modification d'objet DS — modification de GPO ou d'attribut AD |
| 5140/5145 | Security | Accès à un partage réseau / vérification d'accès à un fichier partagé |
| 7045 | System | Installation de service — mécanisme de persistence |
| 4103 | PowerShell | Module logging — modules PowerShell chargés |
| 4104 | PowerShell | Script block logging — contenu des scripts PowerShell exécutés |

#### Commandes Volatility 3 essentielles

```bash
# Lister les processus
python3 vol.py -f dump.raw windows.pslist
python3 vol.py -f dump.raw windows.pstree

# Connexions réseau actives
python3 vol.py -f dump.raw windows.netscan

# DLL chargées par un processus
python3 vol.py -f dump.raw windows.dlllist --pid [PID]

# Détection d'injection de code
python3 vol.py -f dump.raw windows.malfind

# Ligne de commande des processus
python3 vol.py -f dump.raw windows.cmdline

# Extraction des hashes
python3 vol.py -f dump.raw windows.hashdump

# Handles de fichiers/registre
python3 vol.py -f dump.raw windows.handles --pid [PID]
```

#### Commandes KAPE essentielles

```bash
# Triage complet Windows (tous les artefacts principaux)
kape.exe --tsource C: --tdest E:\KAPE_Output --tflush
  --target KapeTriage

# Collecte ciblée Event Logs + Prefetch + Amcache
kape.exe --tsource C: --tdest E:\KAPE_Output
  --target EventLogs,Prefetch,Amcache

# Collecte + parsing automatique
kape.exe --tsource C: --tdest E:\KAPE_Output
  --target KapeTriage --mdest E:\KAPE_Parsed
  --module !EZParser
```

---

### Annexe E — Playbooks types détaillés

Les playbooks complets sont structurés selon le format du Ch.7 : trigger, actions immédiates (0-15 min), actions d'investigation (15 min-4h), actions de confinement, critères d'escalade, communication, et clôture. Pour des raisons de volume, seuls les éléments clés de chaque playbook sont listés ici. Les versions complètes, avec les commandes exactes par outil (Splunk, CrowdStrike, Sentinel, Velociraptor), doivent être adaptées à l'environnement spécifique de chaque organisation.

#### Playbook Ransomware — Éléments clés

**Trigger :** Détection EDR (chiffrement de fichiers, exécution de binaire suspect), ou découverte de fichiers chiffrés / note de rançon.

**Actions immédiates (0-15 min) :** Ne PAS éteindre les machines. Isoler via EDR (network containment). Protéger les sauvegardes (déconnexion physique immédiate du NAS réseau). Alerter l'IR lead.

**Actions critiques :** Identifier le variant (note de rançon, extension des fichiers, hash du binaire). Évaluer l'étendue du chiffrement (combien de machines, quel pourcentage du parc). Vérifier l'intégrité des sauvegardes (sont-elles chiffrées ? antérieures à la compromission ?). Vérifier la compromission de l'AD (DCSync ? krbtgt ?). Estimer l'exfiltration (double extorsion ?).

**Escalade :** P1 automatique si plus de 10 machines chiffrées OU si un DC est compromis OU si les sauvegardes sont touchées.

#### Playbook Compromission de compte — Éléments clés

**Trigger :** Alerte SIEM (geo-impossible travel, connexion depuis IP suspecte, activité anormale), ou signalement utilisateur.

**Actions immédiates :** Désactiver le compte. Révoquer toutes les sessions actives et refresh tokens. Reset du mot de passe.

**Investigation :** Revue de l'activité du compte sur les 30 derniers jours (Sign-in Logs, UAL). Recherche de règles de forwarding email. Recherche de consentements OAuth suspects. Vérification : le phishing initial a-t-il touché d'autres utilisateurs ?

#### Playbook Exfiltration — Éléments clés

**Trigger :** Alerte DLP, volume anormal de trafic sortant, notification externe (données trouvées sur un forum).

**Actions immédiates :** Identifier le canal d'exfiltration (destination, protocole, outil). Bloquer le canal si identifié.

**Investigation :** Identifier les données exfiltrées (quels partages accédés, quels fichiers, quel volume). Identifier la source (quelle machine, quel compte). Remonter au point d'entrée.

**Notification :** CNIL sous 72h si données personnelles.

---

### Annexe F — Tableau d'outils de référence IR

| Catégorie | Outil | Gratuit/Payant | Usage | Limites |
|-----------|-------|---------------|-------|---------|
| **EDR** | CrowdStrike Falcon | Payant | Détection, containment, telemetry | Coût élevé, nécessite agent |
| **EDR** | Microsoft Defender for Endpoint | Payant (inclus E5) | Détection, containment, intégration M365 | Nécessite licence E5 pour full feature |
| **EDR** | SentinelOne | Payant | Détection, containment, rollback ransomware | Coût élevé |
| **SIEM** | Splunk Enterprise | Payant | Corrélation logs, investigation, dashboards | Coût de licence basé sur le volume |
| **SIEM** | Microsoft Sentinel | Payant (cloud) | Corrélation, intégration Azure/M365 | Coût variable selon ingestion |
| **SIEM** | Elastic Security (ELK) | Gratuit (OSS) / Payant (cloud) | Corrélation, flexible, extensible | Expertise nécessaire pour déploiement |
| **NDR** | Vectra AI | Payant | Détection réseau, beaconing, mouvement latéral | Coût élevé |
| **NDR** | Zeek (ex-Bro) | Gratuit (OSS) | Analyse de trafic réseau, génération de logs | Nécessite expertise, pas de GUI |
| **Forensic** | KAPE | Gratuit | Collecte automatisée d'artefacts Windows | Windows uniquement |
| **Forensic** | Velociraptor | Gratuit (OSS) | Collecte à grande échelle, hunting | Courbe d'apprentissage |
| **Forensic** | FTK Imager | Gratuit | Image disque bit-à-bit | Interface vieillissante |
| **Forensic** | Autopsy | Gratuit (OSS) | Analyse forensic complète | Performances variables |
| **Mémoire** | Volatility 3 | Gratuit (OSS) | Analyse de dumps mémoire | Nécessite expertise, plugins limités |
| **Mémoire** | DumpIt (Comae) | Gratuit | Acquisition mémoire Windows rapide | Windows uniquement |
| **Timeline** | Plaso (log2timeline) | Gratuit (OSS) | Super Timeline à partir d'artefacts multiples | Lent sur gros volumes |
| **Timeline** | Timesketch | Gratuit (OSS) | Visualisation collaborative de timelines | Nécessite infrastructure |
| **Malware** | ANY.RUN | Freemium | Sandbox interactive en ligne | Échantillons publics en version gratuite |
| **Malware** | Joe Sandbox | Payant | Sandbox automatisée, analyse approfondie | Coût |
| **Malware** | VirusTotal | Freemium | Multi-scanner, intelligence, relations | Échantillons partagés avec la communauté |
| **AD Audit** | PingCastle | Gratuit (usage interne) | Score de sécurité AD, recommandations | Ne couvre pas tout ATT&CK |
| **AD Audit** | Purple Knight (Semperis) | Gratuit | Audit AD automatisé, détection faiblesses | Rapport parfois verbeux |
| **AD Audit** | BloodHound | Gratuit (OSS) | Cartographie des chemins d'attaque AD | Nécessite collecte SharpHound |
| **SOAR** | Cortex XSOAR (Palo Alto) | Payant | Orchestration, playbooks automatisés | Coût, complexité |
| **SOAR** | Shuffle | Gratuit (OSS) | Orchestration, playbooks | Moins mature que XSOAR |
| **Cloud** | Hawk (PowerShell) | Gratuit (OSS) | Investigation M365 / Entra ID | Limité à l'écosystème Microsoft |

---

### Annexe G — Grilles d'évaluation et RACI

#### Grille de gravité des incidents

| Niveau | Critères techniques | Critères métier | Exemples |
|--------|-------------------|----------------|----------|
| **P4 — Mineur** | 1-2 postes impactés, malware isolé, pas de mouvement latéral | Pas d'impact production, pas de données sensibles | Phishing bloqué, PUA détecté, malware contenu par AV |
| **P3 — Significatif** | Compromission confirmée sur quelques systèmes, mouvement latéral limité | Impact limité sur un service non critique | Compromission d'un compte utilisateur, malware avec C2 actif sur 2-3 postes |
| **P2 — Majeur** | Compromission de serveurs critiques, mouvement latéral étendu, exfiltration possible | Impact sur un service critique, données sensibles potentiellement exposées | Compromission de serveur de fichiers, accès admin non autorisé, exfiltration détectée |
| **P1 — Critique** | Compromission AD (DC, krbtgt), ransomware déployé, exfiltration massive | Production arrêtée, données sensibles confirmées exfiltrées, site OIV impacté | Ransomware à grande échelle, Golden Ticket, exfiltration R&D/RH |

#### Grille de décision de confinement

| Situation | Confinement immédiat ? | Observation contrôlée possible ? | Critère de décision |
|-----------|----------------------|-------------------------------|-------------------|
| Ransomware en cours de déploiement | **OUI — immédiat** | NON | Chaque minute = machines chiffrées |
| Espionnage discret (attaquant non alerté) | Différé possible | **OUI — si l'attaquant ne sait pas** | Comprendre l'étendue avant de couper |
| Compromission de compte sans activité destructrice | **OUI — désactivation du compte** | NON | L'impact est limité et réversible |
| Exfiltration en cours | **OUI — blocage du canal** | Éventuellement, si plusieurs canaux suspectés | Arrêter la fuite est prioritaire |
| Compromission OT avec risque physique | **OUI — isolation IT/OT** | NON | La sécurité physique prime |

#### Matrice RACI type — Réponse à incident

| Action | SOC | IR Lead | Forensic | RSSI | DSI | DG | Juridique | Communication | DPO |
|--------|-----|---------|----------|------|-----|-----|-----------|--------------|-----|
| Détection et escalade | **R** | I | | I | | | | | |
| Classification et triage | C | **R/A** | C | I | | | | | |
| Décision de confinement | | **R** | C | **A** | I | I | | | |
| Collecte forensic | | C | **R** | I | | | | | |
| Investigation technique | | **A** | **R** | I | C | | | | |
| Notification ANSSI | | C | | **R/A** | | I | C | | |
| Notification CNIL | | C | | C | | I | C | | **R/A** |
| Communication interne | | I | | C | C | **A** | C | **R** | |
| Communication externe | | I | | C | | **A** | C | **R** | |
| Décision rançon | | C | | C | C | **A** | **R** | C | |
| Dépôt de plainte | | C | C | C | | I | **R/A** | | |
| RETEX | C | **R** | C | **A** | C | I | I | I | I |

R = Responsible (exécute), A = Accountable (valide), C = Consulted, I = Informed.

---

---

# Annexe — Questions types d'entretien et réponses types

## Questions essentielles

- **Question :** Quelles sont les grandes phases de la réponse à incident ?
  - **Réponse type :** Le NIST 800-61 définit 4 phases : Préparation (avant l'incident — playbooks, outillage, exercices), Détection et Analyse (du signal faible à l'incident confirmé, triage, scoping), Confinement-Éradication-Restauration (isoler, nettoyer, reconstruire), et Post-Incident (retex, amélioration). En réalité, ces phases ne sont pas linéaires — on investigue pendant qu'on contient, on découvre de nouvelles compromissions pendant l'éradication. C'est itératif et parallèle.

- **Question :** Quelle est la différence entre un événement, une alerte, un incident et une crise ?
  - **Réponse type :** Un événement c'est tout fait observable dans le SI — il y en a des milliards par jour. Une alerte c'est un événement signalé comme potentiellement anormal par un système de détection. Un incident c'est une alerte confirmée qui compromet effectivement la confidentialité, l'intégrité ou la disponibilité. Une crise c'est un incident dont l'impact dépasse la capacité de réponse normale et nécessite une gouvernance exécutive. Ces distinctions déterminent le niveau de mobilisation, les processus activés, et les obligations de notification.

- **Question :** Un ransomware est en cours de déploiement — que faites-vous en priorité ?
  - **Réponse type :** Confinement immédiat. Chaque minute qui passe c'est des machines supplémentaires chiffrées. On isole les segments réseau touchés — on coupe la connectivité mais on n'éteint PAS les machines pour préserver la mémoire (qui contient les clés de chiffrement et les artefacts forensic). On désactive les comptes compromis. On protège les sauvegardes — si elles sont accessibles par les mêmes credentials, c'est la priorité absolue. En parallèle, on commence le scoping : l'attaquant est-il ailleurs dans le réseau ?

- **Question :** Pourquoi la préparation est-elle si importante en IR ?
  - **Réponse type :** Parce que le jour de l'incident, il est trop tard pour construire les processus. La préparation détermine tout : est-ce qu'on a un IRP avec des playbooks par type d'incident ? Est-ce qu'on a la télémétrie nécessaire pour investiguer ? Est-ce qu'on sait qui appeler à 2h du matin ? Est-ce qu'on a un contrat avec un prestataire PRIS ? Est-ce qu'on a testé la restauration des sauvegardes ? Une organisation préparée contient un ransomware en quelques heures. Une organisation non préparée met des semaines et paie souvent la rançon.

- **Question :** Comment construisez-vous une timeline d'attaque ?
  - **Réponse type :** La timeline reconstitue chronologiquement toutes les actions de l'attaquant. On croise plusieurs sources : les logs EDR/Sysmon (processus, connexions), les Event Logs Windows (4624 logons, 4698 scheduled tasks), les logs d'authentification AD, les logs proxy/DNS, et les artefacts forensic (prefetch, amcache, MFT). On cherche le point d'entrée initial, les pivots, les escalades de privilèges, les persistances, et les actions sur objectif. La timeline est le livrable central de l'investigation.

## Questions complémentaires

- **Question :** Quand décidez-vous de confiner immédiatement vs observer ?
  - **Réponse type :** Confinement immédiat si l'impact est destructif (ransomware en cours, exfiltration active, risque OT). Observation contrôlée si l'attaquant est discret et ne sait pas qu'il est détecté — ça permet de comprendre l'étendue avant de couper, et d'identifier tous les mécanismes de persistence. Mais cette décision est un arbitrage : observer c'est prendre le risque que l'attaquant accélère. En cas de doute, le confinement prime — surtout s'il y a un risque physique (OT) ou des données sensibles en jeu.

- **Question :** Quels sont les cadres méthodologiques IR que vous connaissez ?
  - **Réponse type :** Les deux principaux sont le NIST SP 800-61 (4 phases : Préparation, Détection-Analyse, Confinement-Éradication-Restauration, Post-Incident) et le SANS PICERL (6 phases : Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned). En France, on a aussi le cadre ANSSI/CERT-FR et le référentiel PRIS pour la qualification des prestataires d'IR. En parallèle, MITRE ATT&CK est utilisé comme grille de lecture pour mapper les TTP observées.

- **Question :** Qu'est-ce qu'un RETEX et pourquoi c'est essentiel ?
  - **Réponse type :** Le RETEX (retour d'expérience) est l'analyse post-incident : timeline complète, vecteur initial, chemins d'escalade, persistence, ce qui a fonctionné et ce qui a échoué, et les recommandations d'amélioration. C'est essentiel parce que sans RETEX, on ne corrige pas les causes racines et on revit le même incident. Un bon RETEX produit des actions concrètes priorisées — pas juste un rapport technique, mais un plan d'amélioration avec des responsables et des délais.

## Questions les plus probables en entretien

1. Phases de la réponse à incident ?
2. Événement vs alerte vs incident vs crise ?
3. Ransomware en cours : premières actions ?
4. Pourquoi la préparation est critique ?
5. Comment construire une timeline d'attaque ?
6. Confiner immédiatement ou observer ?

## Réponses flash

- **Phases NIST** → Préparation → Détection/Analyse → Confinement/Éradication/Restauration → Post-Incident. Itératif, pas linéaire.
- **Échelle** → Événement (fait brut) → Alerte (signalé anormal) → Incident (confirmé) → Crise (dépasse la capacité normale).
- **Ransomware** → Confiner immédiatement, ne PAS éteindre (préserver mémoire), protéger les sauvegardes, désactiver comptes compromis, scoper.
- **Préparation** → IRP, playbooks, télémétrie, contrat PRIS, exercices, test de restauration. Le jour J c'est trop tard.
- **Timeline** → Croiser EDR + Event Logs + proxy/DNS + artefacts forensic. Point d'entrée → pivots → persistence → actions sur objectif.
- **Confinement vs observation** → Destructif/exfiltration = confinement immédiat. Espionnage discret = observation possible si l'attaquant ne sait pas. Doute = confiner.
- **RETEX** → Timeline + causes racines + ce qui a marché/échoué + plan d'amélioration priorisé.

---

> **Note de clôture**
>
> Ce cours a été conçu pour former à l'orchestration de la réponse à incident — la capacité de piloter une investigation, coordonner des acteurs hétérogènes, prendre des décisions sous pression, et ramener une organisation à un état de fonctionnement sûr.
>
> L'incident BLACKTIDE qui traverse les 38 premiers chapitres n'est pas un cas exceptionnel. C'est un incident représentatif de ce que vivent des centaines d'organisations chaque année : un phishing sur un sous-traitant, un infostealer qui vole des credentials VPN, un mouvement latéral progressif, un ransomware déployé un vendredi soir. Les montants, les noms et les circonstances sont fictifs, mais chaque décision, chaque tension, chaque erreur décrite dans le fil rouge est tirée de la réalité opérationnelle d'incidents réels.
>
> La réponse à incident n'est pas un exercice théorique. C'est une discipline qui se prépare (Partie II), se pratique en exercice (Ch.10), et s'améliore par le retour d'expérience (Ch.38). Le jour où l'incident arrive — et il arrivera —, ce qui fait la différence n'est pas la chance, c'est la préparation.
>
> *Préparer • Détecter • Qualifier • Investiguer • Contenir • Éradiquer • Restaurer • Capitaliser — avec méthode, rigueur et sang-froid.*

