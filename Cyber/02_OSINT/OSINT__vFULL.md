# OSINT MASTERY

*Investigation en sources ouvertes : doctrine, méthode, terrain*

**Cours complet — 28 chapitres • 8 parties • 7 annexes**

*Investiguer • Collecter • Vérifier • Analyser • Documenter*

-----

## Table des matières

- [Fil rouge : Opération MIRAGE](#fil-rouge--opération-mirage)
- **PARTIE I — POSTURE, CADRE ET MÉTHODE (Ch.1-4)**
  - Ch.1 — L’OSINT comme discipline de renseignement
  - Ch.2 — Cadre juridique et éthique de l’investigateur
  - Ch.3 — OPSEC de l’investigateur OSINT
  - Ch.4 — Méthodologie d’investigation et outillage
- **PARTIE II — RECHERCHE, PERSONNES ET RÉSEAUX SOCIAUX (Ch.5-9)**
  - Ch.5 — Moteurs de recherche, Google Dorking et archivage web
  - Ch.6 — Investigation sur les personnes physiques
  - Ch.7 — SOCMINT : méthodologie générale et plateformes occidentales
  - Ch.8 — Telegram : architecture, usages et méthodologie d’investigation
  - Ch.9 — Discord, forums et plateformes alternatives
- **PARTIE III — INVESTIGATION CORPORATE, INFRASTRUCTURE ET DONNÉES EXPOSÉES (Ch.10-13)**
  - Ch.10 — Investigation corporate : sociétés, UBO et structures juridiques
  - Ch.11 — Investigation domaines, DNS, certificats et infrastructure
  - Ch.12 — Breaches, leaks et exploitation de données fuitées
  - Ch.13 — Dark Web et DARKINT : navigation, investigation, monitoring
- **PARTIE IV — IMINT, GEOINT ET VÉRIFICATION VISUELLE (Ch.14-17)**
  - Ch.14 — IMINT : analyse d’images et recherche inversée
  - Ch.15 — GEOINT : géolocalisation, chronolocation et OSINT spatial
  - Ch.16 — OSINT maritime, aérien et de transport
  - Ch.17 — Contenus synthétiques, deepfakes et vérification
- **PARTIE V — FININT, CRYPTO ET INVESTIGATION FINANCIÈRE (Ch.18-20)**
  - Ch.18 — OSINT financier et patrimonial
  - Ch.19 — Crypto-actifs et blockchain : investigation OSINT
  - Ch.20 — Workflow d’investigation financière intégrée
- **PARTIE VI — ANALYSE, VÉRIFICATION ET PRODUCTION (Ch.21-24)**
  - Ch.21 — Analyse structurée : ACH, biais et raisonnement adversaire
  - Ch.22 — Cotation de fiabilité et niveaux de confiance
  - Ch.23 — Rédaction du rapport d’investigation OSINT
  - Ch.24 — Cadre judiciaire, transmission et veille post-rapport
- **PARTIE VII — CAS DE SYNTHÈSE COMPLETS (Ch.25-28)**
  - Ch.25 — Cas complet : synthèse Opération MIRAGE
  - Ch.26 — Cas complet : investigation GEOINT sur une vidéo virale
  - Ch.27 — Cas complet : dé-anonymisation d’un compte pseudonyme
  - Ch.28 — Cas complet : campagne de désinformation et faux comptes
- **ANNEXES**
  - Annexe A — Glossaire OSINT (60+ termes)
  - Annexe B — Catalogue de Google Dorks par objectif
  - Annexe C — Atlas des plateformes et registres par pays
  - Annexe D — Cheat sheets opérationnelles
  - Annexe E — Templates de livrables
  - Annexe F — Workflow d’enquête en 10 étapes (avec checklists)
  - Annexe G — Lab de l’investigateur, ressources et formations

-----

## Fil rouge : Opération MIRAGE

> **Contexte narratif — ce fil rouge traverse les 24 premiers chapitres et se conclut au Ch.25.**
> 
> Un cabinet d’avocats parisien, **Legrand & Associés**, mandate une investigation OSINT sur **Marc Delaunay**, 48 ans, directeur administratif et financier de **TechnoVert SAS** — ETI française spécialisée dans les technologies de recyclage industriel, 450 collaborateurs, CA 85 M€, deux sites de production (Lyon, Lille). Le cabinet représente un actionnaire minoritaire (12 % du capital) qui soupçonne Delaunay de trois choses : (1) détournement de fonds vers des structures offshore via des contrats de « consulting » fictifs ou surfacturés, (2) blanchiment partiel de ces fonds en crypto-actifs, et (3) orchestration d’une campagne de désinformation visant à discréditer un lanceur d’alerte interne — ancien contrôleur de gestion remercié 8 mois plus tôt après avoir alerté sur des écritures comptables suspectes.
> 
> **Sélecteurs initiaux fournis par le client** : nom complet (Marc Delaunay), date de naissance approximative (1976-1977), poste (DAF TechnoVert SAS), email professionnel (`m.delaunay@technovert.fr`).
> 
> **Mandat** : produire un rapport OSINT complet, exploitable judiciairement, identifiant les structures offshore, les flux financiers, les actifs détenus, et la campagne de désinformation. Le cabinet envisage un dépôt de plainte au Parquet National Financier et une saisine du C3N pour le volet désinformation.
> 
> **Délai** : 6 semaines. **Budget** : raisonnable (cabinet d’avocats), sans accès à des bases payantes lourdes (pas de Chainalysis, pas de WorldCheck Pro). L’investigation doit s’appuyer sur des sources ouvertes et des outils gratuits ou freemium.
> 
> **Contraintes** : aucune interaction avec la cible, aucun accès illégal, OPSEC stricte (Delaunay est techniquement compétent et pourrait détecter une approche). Le rapport doit pouvoir être versé à un dossier judiciaire.
> 
> Au fil des chapitres, l’investigateur va passer du nom de Delaunay à un schéma complet : un réseau de quatre sociétés écrans (Malte, Chypre, BVI, Luxembourg), des flux bancaires opaques convertis en Bitcoin via Binance, un patrimoine immobilier en SCI familiale incohérent avec les revenus déclarés, et une campagne de désinformation orchestrée via un blog, huit faux comptes coordonnés sur X, et une photo synthétique destinée à fabriquer un faux alibi. Chaque épisode du fil rouge illustre un chapitre — pas comme une démonstration parfaite, mais comme une suite de décisions méthodologiques sous contraintes.

-----

## PARTIE I — POSTURE, CADRE ET MÉTHODE

> **Ce que cette partie apprend.** Comprendre ce qu’est l’OSINT comme discipline (et ce qu’elle n’est pas), maîtriser le cadre juridique et éthique dans lequel opère l’investigateur, sécuriser son infrastructure d’enquête, et installer une méthodologie reproductible.
> 
> **Ce qu’elle ne couvre pas.** Les techniques de collecte par sélecteur (traitées en Partie II), les sources spécialisées (Parties III à V), la production du rapport (Partie VI).
> 
> **Ce que vous saurez faire après cette partie.** Cadrer une investigation, évaluer si une demande client est légalement et éthiquement acceptable, monter une infrastructure d’investigation OPSEC-compatible, structurer une enquête de la sollicitation au plan de collecte.

-----

### Chapitre 1 — L’OSINT comme discipline de renseignement

#### 1.1 Définition opérationnelle : information vs renseignement

L’OSINT (Open Source Intelligence) est la discipline du renseignement qui collecte, traite, analyse et exploite de l’information accessible publiquement pour produire du renseignement actionnable. Le mot clé est « discipline » — pas une collection d’outils, pas une recherche Google améliorée. C’est un processus structuré, reproductible, documenté, et orienté décision.

La distinction la plus importante du métier est celle entre **information** et **renseignement**. Une information est un fait brut : « Marc Delaunay est administrateur de Delta Consulting Ltd à Malte ». Un renseignement est une information traitée, contextualisée, corrélée à d’autres sources, évaluée en fiabilité, et présentée avec un niveau de confiance explicite : « Marc Delaunay est administrateur déclaré de Delta Consulting Ltd, société maltaise au capital symbolique, dont le siège est une adresse de domiciliation partagée par 47 autres entités, et dont les flux entrants depuis TechnoVert SAS représentent 89 % du chiffre d’affaires déclaré sur les trois derniers exercices — niveau de confiance élevé, sources A1 et B2 ». La différence n’est pas cosmétique : c’est ce qui distingue le travail d’un investigateur professionnel d’une recherche amateur.

L’OSINT se distingue de la simple recherche par trois traits structurants. Elle est **orientée par un objectif** : « Delaunay contrôle-t-il des sociétés offshore ? » est une question d’investigation, « que sais-je sur Delaunay ? » n’en est pas une. Elle suit une **méthodologie rigoureuse** : le cycle du renseignement (orientation, collecte, traitement, analyse, diffusion, feedback) appliqué de manière disciplinée. Elle produit un **livrable avec un niveau de confiance explicite** : chaque fait porte une cotation de fiabilité, chaque conclusion est qualifiée d’un niveau de confiance, chaque limite est documentée.

#### 1.2 Les disciplines du renseignement et la place de l’OSINT

L’OSINT s’inscrit dans un écosystème de disciplines de renseignement, chacune avec ses sources, ses méthodes, et ses contraintes légales. Il est utile de les distinguer pour comprendre ce que l’OSINT couvre — et ce qu’elle ne couvre pas.

Le **HUMINT** (Human Intelligence) est le renseignement issu de sources humaines : entretiens, informateurs, élicitation. Il est légal s’il est transparent (un journaliste qui interviewe une source, un investigateur qui pose une question dans un cadre normal de relation professionnelle). Il devient illégal si l’investigateur usurpe une identité ou exerce une pression pour obtenir l’information.

Le **SIGINT** (Signal Intelligence) est l’interception de communications. Il est strictement réservé aux services d’État autorisés. Aucun investigateur privé ne peut faire du SIGINT légalement.

L’**IMINT** (Image Intelligence) est le renseignement par l’imagerie. Une partie est en sources ouvertes (imagerie satellite Sentinel, Google Earth, photos publiées) — c’est cette partie que mobilise l’OSINT. L’IMINT classifié (imagerie satellite haute résolution militaire) est réservé aux services.

Le **GEOINT** (Geospatial Intelligence) combine l’imagerie, la cartographie, et les données géolocalisées pour produire du renseignement spatial. La méthodologie Bellingcat est entièrement bâtie sur le GEOINT en sources ouvertes. C’est l’un des sous-domaines les plus matures de l’OSINT moderne.

Le **SOCMINT** (Social Media Intelligence) est le renseignement issu des réseaux sociaux. C’est aujourd’hui l’un des plus gros volumes de l’OSINT, à la fois parce que les gens publient massivement leur vie en ligne et parce que les réseaux sociaux sont devenus des plateformes opérationnelles pour la criminalité, l’extrémisme, l’influence et la fraude.

Le **FININT** (Financial Intelligence) est le renseignement financier. Une partie est en sources ouvertes (registres d’entreprises, comptes publiés, listes de sanctions, Pandora Papers) — c’est cette partie que mobilise l’OSINT. Le FININT institutionnel (déclarations de soupçon, accès aux flux bancaires) est réservé aux Cellules de Renseignement Financier (TRACFIN, FinCEN).

Le **DARKINT** (Dark Web Intelligence) est le renseignement issu du dark web — forums clandestins, marketplaces, leak sites. La consultation est légale, l’interaction est réservée à un cadre professionnel strict ou aux LEA.

L’**OSINT** englobe ou recoupe l’IMINT, le GEOINT, le SOCMINT, la part ouverte du FININT, et le DARKINT en mode consultation. Une investigation OSINT typique combine plusieurs de ces sous-disciplines. Ce cours les enseigne de manière intégrée.

#### 1.3 Le cycle du renseignement appliqué à l’OSINT

Le cycle du renseignement structure toute investigation rigoureuse. Il comporte six phases qui ne sont pas strictement séquentielles — en pratique, elles se chevauchent et l’investigateur revient en arrière régulièrement.

L’**orientation** consiste à formuler les questions d’investigation et le plan de collecte. C’est l’étape la plus négligée par les débutants, qui plongent immédiatement dans la collecte. Un cadrage faible produit une investigation dispersée.

La **collecte** mobilise les sources identifiées dans le plan. Chaque donnée collectée est documentée : sélecteur utilisé, source, date, capture horodatée, hash. Sans cette discipline, la chaîne de custody est rompue dès le départ.

Le **traitement** nettoie, organise, déduplique. Les captures sont nommées de manière cohérente, les sélecteurs sont consolidés dans un graphe, les doublons sont fusionnés.

L’**analyse** corrèle les données, teste les hypothèses, cote la fiabilité, identifie les faux positifs. C’est ici que l’investigation devient du renseignement — sans analyse, on a un dossier de captures.

La **diffusion** produit le rapport avec ses conclusions, ses niveaux de confiance, et ses recommandations. Le format est calibré pour le destinataire (cabinet d’avocats, magistrat, RSSI, journaliste).

Le **feedback** ferme la boucle : le commanditaire réagit au rapport, demande des précisions, identifie de nouvelles pistes. L’investigation peut repartir pour un nouveau cycle.

#### 1.4 Les niveaux de confiance et la cotation : pourquoi c’est non négociable

Un rapport OSINT sans cotation de fiabilité n’est pas un rapport professionnel. C’est ce qui sépare le renseignement du bruit, et c’est ce que les utilisateurs sérieux d’OSINT (cabinets d’avocats, magistrats, services d’enquête, RSSI) attendent en premier.

La grille standard est le **code Admiralty (NATO system)**, à double entrée. La fiabilité de la source va de A (totalement fiable — registre officiel, publication d’État) à F (fiabilité inconnue — source nouvelle, non testée). La crédibilité de l’information va de 1 (confirmée par d’autres sources indépendantes) à 6 (véracité impossible à juger).

Un fait coté A1 (Pappers indique que Marc Delaunay est gérant de Delta Consulting France SARL — confirmé par Infogreffe) est solide. Un fait coté F6 (un post anonyme sur un forum prétend que Delaunay vit à Dubaï — aucune corroboration, source non testée) est une simple piste à investiguer, pas un élément de rapport.

Cette grille s’applique à **chaque fait** du rapport. C’est exigeant à mettre en œuvre — et c’est précisément ce qui distingue un rapport amateur (« voici tout ce que j’ai trouvé ») d’un rapport professionnel (« voici ce que j’ai établi, avec quelle solidité »). Le chapitre 22 développe la cotation en détail.

#### 1.5 Les acteurs de l’OSINT

L’OSINT n’est pas un métier monolithique. Plusieurs profils l’utilisent avec des cadres et des objectifs très différents.

Les **investigateurs privés** mènent des enquêtes pour des cabinets d’avocats, des compagnies d’assurance, des entreprises (due diligence, fraude interne, contentieux). Ils opèrent strictement en sources ouvertes — pas de réquisition, pas d’interception, pas d’accès aux registres réservés. Leurs livrables sont souvent versés à des dossiers judiciaires.

Les **forces de l’ordre** (en France : C3N, OCLCTIC, JUNALCO, BL2C ; à l’international : NCA, FBI, BKA) utilisent l’OSINT en complément de leurs pouvoirs propres (réquisition, interception, perquisition). L’OSINT permet souvent de cadrer l’enquête avant l’engagement des moyens lourds.

Les **journalistes d’investigation** (consortiums comme l’OCCRP, ICIJ — Pandora Papers, Bellingcat) ont fait de l’OSINT une méthodologie centrale. Leurs publications sont devenues des sources OSINT de référence pour les autres acteurs.

Les **organisations humanitaires** (Trace Labs pour les personnes disparues, Amnesty International, HRW) utilisent l’OSINT pour documenter des disparitions, des crimes de guerre, des violations des droits humains.

Les **équipes CTI et SOC** mobilisent l’OSINT pour le renseignement sur les menaces : profilage d’acteurs, monitoring d’infrastructure adverse, veille sur les fuites de données.

Les **équipes de défense et de renseignement** intègrent l’OSINT dans leurs cycles, souvent en complément de sources classifiées.

Chaque profil a ses contraintes spécifiques — éthiques, juridiques, opérationnelles. Ce cours adopte par défaut la posture de l’investigateur privé en mission pour un cabinet d’avocats, qui est la plus contraignante (pas d’accès aux pouvoirs des LEA) et donc la plus formatrice. Les adaptations à d’autres contextes sont signalées.

#### 1.6 Fil rouge — MIRAGE Épisode 1

> **🎯 MIRAGE — Épisode 1 : la sollicitation**
> 
> L’investigateur reçoit le brief du cabinet Legrand & Associés. La sollicitation est claire mais large : « identifier les structures offshore, les flux financiers, les actifs détenus, et la campagne de désinformation ». L’investigateur reformule en quatre **questions d’investigation** précises, qui structureront tout le travail.
> 
> **QI-1** — Marc Delaunay contrôle-t-il, directement ou indirectement, des sociétés non françaises non déclarées ? Si oui, lesquelles, dans quelles juridictions, et avec quelle structure ?
> 
> **QI-2** — Existe-t-il des flux financiers entre TechnoVert SAS et ces sociétés, et sont-ils cohérents avec une activité économique réelle ?
> 
> **QI-3** — Marc Delaunay détient-il des crypto-actifs non déclarés, et peut-on tracer un lien entre TechnoVert et ces actifs ?
> 
> **QI-4** — Existe-t-il une campagne de désinformation visant le lanceur d’alerte interne, et peut-on en identifier l’origine ?
> 
> Les **sélecteurs initiaux** sont consolidés : nom complet, date de naissance approximative, poste, email professionnel, employeur, et — ajouté par l’investigateur — l’adresse présumée du domicile (recherche annuaire inversée à partir du nom + ville). Le cadrage est documenté dans la fiche de cadrage (Annexe E). L’investigation peut commencer.

-----

### Chapitre 2 — Cadre juridique et éthique de l’investigateur

#### 2.1 Le cadre français : RGPD, Code pénal, jurisprudence

L’investigation OSINT en France s’inscrit dans plusieurs corpus juridiques qui se superposent. L’investigateur doit les connaître avant de toucher un clavier — pas après, quand le client demande pourquoi son rapport est inexploitable judiciairement.

Le **RGPD** (Règlement Général sur la Protection des Données, 2018) s’applique dès qu’on collecte des données personnelles. Trois principes structurent l’OSINT : la **proportionnalité** (collecter ce qui est nécessaire à la finalité, pas plus), la **minimisation** (conserver le minimum de données pendant le minimum de temps), et la **finalité explicite** (la collecte doit servir un objectif légitime documenté). Le RGPD ne *interdit* pas l’OSINT, contrairement à ce que certains pensent — mais il l’encadre. Une investigation OSINT mandatée par un cabinet d’avocats pour un contentieux est typiquement une finalité légitime (intérêt légitime au sens de l’article 6.1.f, voire mission d’intérêt public si les autorités sont saisies).

Le **Code pénal** réprime plusieurs comportements adjacents à l’OSINT :

- **Article 226-1** (atteinte à la vie privée) : enregistrer ou capter des paroles ou images dans un lieu privé sans consentement.
- **Article 226-4-1** (usurpation d’identité numérique) : usurper l’identité d’autrui pour troubler sa tranquillité.
- **Article 226-18** (collecte déloyale ou frauduleuse de données personnelles) : s’applique typiquement à l’OSINT qui contournerait des protections (faux profils, manipulations).
- **Article 323-1 et suivants** (accès et maintien frauduleux dans un système de traitement automatisé de données — STAD) : c’est ici que se joue la limite la plus fine.

La **jurisprudence Bluetouff** (2014) est devenue la référence en matière d’OSINT. Olivier Laurelli, journaliste, avait téléchargé des documents de l’ANSES via un bucket S3 mal configuré, accessible sans authentification. Il a été condamné en 2014 pour maintien frauduleux dans un STAD : la Cour a considéré que, bien que les fichiers soient techniquement accessibles, l’utilisateur ne pouvait ignorer qu’ils n’étaient pas destinés à être publics. La leçon pour l’investigateur : **accessible techniquement ≠ accessible légalement**. Un bucket S3 ouvert par erreur, un répertoire indexé par Google contenant des données qui ne devraient pas l’être, une configuration de permissions ratée — tout cela n’est pas de l’OSINT légitime.

#### 2.2 Le principe « accessible ≠ public » et la proportionnalité

Trois critères pratiques permettent de distinguer une donnée légitimement OSINT d’une donnée problématique.

Premier critère : la **publication explicite**. La donnée a été publiée par son détenteur sur un canal public, sans restriction d’accès. Un profil LinkedIn public, un article de presse, un registre légal officiel, un post Twitter accessible sans authentification : OSINT légitime. Un email envoyé à une mailing list privée, un document partagé sur un Google Drive « accessible avec le lien », une fuite récente non encore publiquement diffusée : zone à risque.

Deuxième critère : l’**absence de contournement**. La donnée a été obtenue sans contourner aucune protection. Si l’investigateur a dû créer un faux compte pour accéder, manipuler une URL, deviner un identifiant, ou utiliser un bucket mal configuré, il y a contournement.

Troisième critère : la **proportionnalité à la finalité**. La collecte est proportionnée à l’enquête. Collecter l’historique exhaustif Instagram d’un suspect sur dix ans pour une investigation patrimoniale n’est pas proportionné — collecter les publications mentionnant des actifs ou des voyages liés à la période d’enquête l’est.

Ces trois critères ne sont pas du droit, mais une grille opérationnelle. En cas de doute, la règle est simple : si l’investigateur n’est pas sûr qu’il pourrait expliquer publiquement comment il a obtenu une donnée sans embarras, c’est que la donnée n’est probablement pas OSINT.

#### 2.3 Variations internationales : USA, UK, Allemagne, Suisse

Le cadre juridique OSINT varie significativement entre juridictions, ce qui compte si l’investigation a une dimension internationale ou si l’investigateur intervient pour des clients étrangers.

Les **États-Unis** ont un cadre relativement permissif, fortement protégé par le Premier Amendement (liberté d’expression, qui couvre la publication d’informations véridiques). Pas de RGPD équivalent au niveau fédéral, mais des lois sectorielles (HIPAA pour la santé, FERPA pour l’éducation) et des lois d’État (CCPA en Californie). Le concept de « public records » est plus large : casiers judiciaires, registres immobiliers, dossiers de divorce, relevés de contributions politiques sont souvent publics.

Le **Royaume-Uni** applique le UK GDPR (équivalent post-Brexit du RGPD), modulé par le Data Protection Act 2018. La protection des données est forte mais l’investigation journalistique et la due diligence sont relativement bien protégées par les exceptions « legitimate interest ».

L’**Allemagne** a une protection de la vie privée parmi les plus fortes au monde, héritage historique. Le Bundesdatenschutzgesetz (BDSG) et la jurisprudence stricte rendent l’OSINT plus contraint qu’ailleurs en Europe. La reconnaissance faciale est particulièrement encadrée.

La **Suisse** a une protection structurellement forte (LPD révisée en 2023), mais une tradition de discrétion qui rend l’investigation sur des comptes ou des dirigeants suisses techniquement plus difficile que juridiquement.

L’investigateur qui opère sur plusieurs juridictions doit, à minima, **adopter le cadre le plus strict** des juridictions concernées. C’est la règle de prudence : si une investigation porte sur un suspect français résidant à Genève et impliquant une société à Londres, la conformité doit satisfaire le RGPD français, le LPD suisse, et le UK GDPR.

#### 2.4 OSINT pour les LEA vs secteur privé

Les **forces de l’ordre** disposent de pouvoirs que le secteur privé n’a pas : réquisitions judiciaires (obtenir des données auprès d’opérateurs télécom, de plateformes, de banques), interceptions, perquisitions, gel d’actifs, opérations sous couverture autorisées par un magistrat. L’OSINT, pour les LEA, est typiquement la phase amont : cadrer l’enquête, identifier les pistes, justifier l’engagement des moyens lourds.

Le **secteur privé** (cabinets d’avocats, entreprises, investigateurs privés) opère strictement en sources ouvertes, sans aucun de ces pouvoirs. La compensation est partielle : un investigateur privé OSINT bien outillé peut produire un rapport qui orientera ensuite l’enquête judiciaire. Le rapport identifie les pistes ; les autorités exercent les pouvoirs.

Cette distinction structure les chapitres du cours. Quand une technique nécessite des pouvoirs LEA (réquisitions à un exchange crypto, interception de communications), elle est signalée comme telle et l’alternative OSINT est précisée.

#### 2.5 Éthique au-delà du droit

Le droit fixe le minimum. L’éthique professionnelle va plus loin et conditionne la durée de carrière de l’investigateur autant que sa réputation.

**Ne pas doxxer.** Doxxer, c’est publier les données personnelles d’une personne pour permettre son harcèlement, sa traque, ou son agression. L’investigateur OSINT est techniquement capable de doxxer (c’est exactement la même méthodologie). Il ne le fait jamais. Le rapport est transmis au commanditaire, pas publié.

**Ne pas harceler.** L’OSINT ne doit pas devenir un instrument de pression ou de surveillance personnelle. Si une investigation semble servir à intimider une cible (ex-conjoint, ex-employé, journaliste), l’investigateur refuse le mandat.

**Signaler les contenus illicites.** Si l’investigation révèle des contenus pédopornographiques, des incitations au terrorisme, des menaces de mort crédibles, l’investigateur a une obligation morale (et parfois légale) de signaler aux autorités compétentes (Pharos en France, NCMEC aux US).

**Ne pas conserver indéfiniment.** Les données collectées sont conservées le temps nécessaire à la mission et à la conservation des preuves (typiquement 5 ans pour un dossier ayant un volet judiciaire), puis détruites. Le RGPD exige cette discipline ; l’éthique la confirme.

**Ne pas manipuler.** L’investigateur n’incite pas la cible à se découvrir (provocation), n’usurpe pas d’identité réelle, n’utilise pas de faux profils dans des interactions actives (à distinguer de l’observation passive avec un compte d’investigation, qui est légitime).

**Refuser certains mandats.** Un cabinet qui demande une investigation sur un témoin dans une affaire en cours, sur un journaliste qui enquête sur le client, sur un lanceur d’alerte légitime : l’investigateur a le droit (et parfois le devoir) de refuser.

#### 2.6 Données biométriques et reconnaissance faciale

Les données biométriques (visage, empreinte vocale) sont classées comme **données sensibles** par le RGPD (article 9). Leur traitement est par principe interdit, sauf exceptions strictes (consentement explicite, intérêt public majeur, etc.).

La **reconnaissance faciale** par OSINT (PimEyes, FaceCheck.id, Yandex Images) est techniquement accessible et juridiquement très exposée. Trois précautions structurent l’usage légitime :

D’abord, **utiliser uniquement pour confirmer une identité déjà identifiée par d’autres voies** — pas pour identifier une personne inconnue. Si l’investigateur connaît déjà l’identité de Delaunay et utilise PimEyes pour vérifier qu’une photo trouvée sur un site de rencontres correspond, c’est un usage défendable. Si un investigateur soumet la photo d’un individu inconnu à PimEyes pour découvrir son identité, c’est une zone juridique à très haut risque.

Ensuite, **ne jamais traiter le résultat comme une preuve**. La reconnaissance faciale OSINT a des taux de faux positifs et de faux négatifs significatifs. Un match PimEyes est une **piste**, à corroborer par d’autres sources. Un rapport qui présente un match de reconnaissance faciale comme preuve sera détruit par n’importe quel contradicteur.

Enfin, **documenter la cotation à la baisse**. Une correspondance par reconnaissance faciale est typiquement cotée C3 ou D3 — source de fiabilité moyenne, information non confirmée. Jamais A1.

#### 2.7 La question des mineurs et des victimes

Les investigations qui impliquent des mineurs (témoins, victimes, suspects) ou des victimes (de violence, d’abus, de fraude) imposent des précautions renforcées.

Pour les **mineurs**, le principe est de minimiser radicalement la collecte et la conservation. L’investigateur n’investigue pas un mineur sauf nécessité absolue de la mission, ne conserve aucune image d’identification, ne diffuse aucune donnée personnelle, et signale immédiatement toute découverte de contenu d’exploitation sexuelle de mineurs aux autorités (Pharos, CyberTipline).

Pour les **victimes**, l’investigation doit éviter la victimisation secondaire. Documenter une fraude dont X est la victime ne justifie pas d’exposer X au risque d’identification publique. Le rapport peut nommer la victime pour le cabinet client, mais sa diffusion ultérieure (presse, autorités) doit prévoir l’anonymisation.

Ces principes ne sont pas seulement éthiques. Ils protègent l’investigateur lui-même : un rapport mal calibré sur ces dimensions peut être inexploitable judiciairement, voire retourné contre son auteur (plainte de la cible, sanction professionnelle).

-----

### Chapitre 3 — OPSEC de l’investigateur OSINT

#### 3.1 Le threat model : calibrer l’OPSEC sur la menace

L’OPSEC (Operational Security) est l’ensemble des mesures qui empêchent la cible de l’investigation de détecter qu’elle est investiguée, et qui protègent l’investigateur contre les contre-mesures de la cible. L’OPSEC absolue n’existe pas — chaque interaction en ligne laisse des traces. L’objectif est la réduction du risque à un niveau acceptable pour la mission.

Le **threat model** (modèle de menace) est l’étape qui calibre l’OPSEC sur le contexte. Une investigation patrimoniale sur un dirigeant d’entreprise français lambda n’a pas le même profil de risque qu’une investigation sur un cadre du crime organisé ou sur un opérateur d’État. Trois questions structurent le threat model.

**Quelle est la sophistication technique de la cible ?** Un DAF d’ETI peut détecter une visite LinkedIn et regarder son profil. Un acteur étatique peut investiguer activement le profil de l’investigateur, exploiter des fuites, recouper des données. Un membre du crime organisé peut faire les deux et avoir des moyens de représailles physiques.

**Quelle est la motivation de la cible à découvrir l’investigation ?** Une investigation découverte précocement permet à la cible d’effacer les preuves (dissolution de sociétés, suppression de profils, mise en privé de comptes), d’orienter ses communications, voire de menacer l’investigateur. Plus la mission est sensible, plus l’OPSEC doit être stricte.

**Quelle est la durée de l’investigation ?** Une investigation courte (quelques jours) limite l’exposition. Une investigation longue (plusieurs mois) accumule les interactions et les risques de fuite. La discipline OPSEC se relâche naturellement avec le temps — il faut s’y préparer.

Le threat model produit une décision pratique : niveau d’OPSEC bas (compte d’investigation simple, navigateur séparé), moyen (VM dédiée, VPN, avatars), ou élevé (Tails ou Whonix, téléphones burner, cloisonnement physique).

#### 3.2 Infrastructure : VM dédiée, Tails, Whonix, navigateur

L’infrastructure de base pour une investigation OSINT comprend cinq couches de séparation par rapport à la machine personnelle ou professionnelle de l’investigateur.

Une **machine virtuelle dédiée à l’investigation** est le minimum. Elle isole l’environnement d’enquête du système hôte : si l’investigateur est compromis dans la VM (malware, fuite de données, traque par la cible), la machine principale reste intacte. Distributions courantes : **VM Linux générique** (Ubuntu, Debian) avec un profil dédié, **Tails** (système amnésique sur USB — aucune trace persistante après extinction), **Whonix** (système basé sur Tor avec architecture en deux VM : Gateway qui route tout via Tor, Workstation qui isole l’utilisateur).

Le choix dépend du threat model. Tails est excellent pour les missions sensibles ponctuelles (déplacement, terrain) mais peu pratique pour une enquête longue (rien n’est conservé). Whonix est excellent pour le travail sur le dark web (Ch.13) et les missions à haut risque. Une VM Linux dédiée est suffisante pour la majorité des missions OSINT classiques.

Le **VPN** masque l’adresse IP réelle de l’investigateur aux sites consultés. Il doit être un VPN commercial sérieux, sans logs vérifiables (audits indépendants), payé sans lien avec l’identité réelle. Il ne doit jamais être le VPN personnel ou professionnel de l’investigateur — la corrélation serait immédiate. Pour les missions à risque élevé, un VPN suivi de Tor (VPN → Tor) ajoute une couche.

Le **navigateur** est un profil vierge dédié à l’investigation. Firefox avec un profil séparé est un standard. Extensions : uBlock Origin, NoScript (selon le besoin), Cookie AutoDelete. Pas d’extensions liées à des comptes personnels (LastPass perso, Grammarly, etc.) qui pourraient leaker l’identité.

Le **DNS** doit être chiffré (DNS over HTTPS ou DNS over TLS) et indépendant du fournisseur d’accès personnel. Des résolveurs comme Quad9, Cloudflare 1.1.1.1, ou des résolveurs auto-hébergés sont préférables.

Le **stockage** des données d’investigation est chiffré au repos (LUKS sur Linux, FileVault sur macOS, BitLocker sur Windows). Les sauvegardes le sont également. Une investigation perdue dans un train ou volée dans un sac doit rester illisible.

#### 3.3 Avatars / sock puppets : construction, maturation, gestion

Un **avatar** (ou sock puppet) est une fausse identité créée pour permettre l’observation passive sur des plateformes qui exigent un compte. Il sert à consulter LinkedIn sans révéler l’identité réelle, à rejoindre un groupe Facebook public d’observation, à suivre un compte Telegram qui exige un compte. Il ne sert **jamais** à interagir avec la cible (poster, commenter, contacter) — l’interaction franchit la ligne de l’usurpation et de la manipulation.

La **construction** d’un avatar suit cinq étapes. D’abord le **pseudonyme** : crédible dans la culture de la plateforme (nom plausible, sans coïncidence avec une personne réelle), cohérent avec le profil construit. Ensuite la **photo** : générée par IA (ThisPersonDoesNotExist) en s’assurant que la version générée ne soit pas détectable en recherche inversée — sinon utiliser une photo générée avec d’autres outils (StyleGAN3, MidJourney) et tester en reverse search avant déploiement. Puis l’**email** : créé sur ProtonMail ou Tutanota via Tor, sans téléphone associé. Le **téléphone** si nécessaire : numéro burner SMS-online ou SIM prépayée dédiée (jamais le téléphone perso). Enfin la **maturation** : l’avatar publie quelques contenus banals, suit quelques comptes anodins, vit pendant plusieurs semaines avant d’être utilisé en enquête. Un compte créé hier qui consulte immédiatement le profil d’une cible déclenche les heuristiques anti-fraude des plateformes.

La **gestion** d’un avatar exige une discipline absolue. Un **registre interne** (chiffré, versionné) liste tous les avatars actifs, leurs identifiants, leurs plateformes, leurs missions. Un avatar n’est utilisé que pour **une seule investigation à la fois** — la réutilisation est l’erreur OPSEC la plus courante. Après usage, l’avatar est mis au repos, ou détruit selon la sensibilité.

Le **backstopping** (renforcement de la crédibilité) est rarement nécessaire pour de l’OSINT pure, mais peut être pertinent pour rejoindre un groupe semi-fermé : profil professionnel cohérent (entreprise fictive avec site web minimal), historique de publications crédible. Le backstopping élaboré est typiquement réservé aux contextes red team ou HUMINT.

#### 3.4 Téléphones d’investigation

Le téléphone est la pièce d’OPSEC la plus négligée. La majorité des plateformes (WhatsApp, Telegram, Signal, X) exigent un numéro de téléphone, et beaucoup associent ce numéro à des données identifiantes.

Un **téléphone d’investigation** physique est dédié à l’enquête. Il ne contient aucune application liée à l’identité personnelle (banque, email perso, réseaux sociaux perso). Son IMEI n’est pas associé au nom de l’investigateur. Les options : un smartphone dédié avec carte SIM prépayée achetée en espèces (en France, c’est devenu plus difficile depuis 2017 — l’identification est exigée à l’activation, mais une SIM activée par un tiers reste utilisable), un service de SMS en ligne (SMS-Activate, SMS-Online — utile pour la création de comptes mais traçable), ou un eSIM voyage anonyme (selon les juridictions).

Pour les missions sensibles, le téléphone d’investigation est physiquement séparé : jamais transporté avec le téléphone personnel allumé (corrélation par bornes télécom), jamais connecté au même réseau Wi-Fi domestique, jamais utilisé dans le même Wi-Fi que des comptes personnels actifs.

#### 3.5 Erreurs courantes documentées

Cinq erreurs OPSEC reviennent constamment dans les retours d’expérience des investigateurs.

**La fuite LinkedIn.** L’investigateur consulte le profil LinkedIn de la cible depuis son compte personnel. LinkedIn notifie. La cible voit le nom de l’investigateur, son employeur, son réseau. L’investigation est compromise. Parade : LinkedIn s’observe via Google dorks (`site:linkedin.com "Marc Delaunay"`), via un compte d’investigation en mode privé, ou via un compte premium qui permet la navigation privée.

**Les métadonnées dans les captures envoyées au client.** L’investigateur fait une capture d’écran avec son outil natif. La capture contient des métadonnées (nom de l’utilisateur, machine, parfois géolocalisation). Le client transmet la capture à un tiers, qui découvre l’identité de l’investigateur. Parade : ExifTool en post-traitement, ou outils de capture qui strippent les métadonnées (Hunchly).

**Le copier-coller entre VM et machine personnelle.** Le presse-papiers partagé entre la VM d’investigation et la machine hôte est le canal de fuite le plus discret. Une URL d’investigation collée par erreur dans un email personnel, un sélecteur sensible apparaissant dans l’historique du navigateur perso. Parade : désactiver le partage de presse-papiers dans la configuration de la VM.

**La réutilisation du VPN.** L’investigateur utilise le même VPN pour son usage personnel et pour ses investigations. Une fuite chez le fournisseur VPN (peu fiable malgré les promesses de no-logs) corrèle les deux usages. Parade : VPN strictement séparé pour l’investigation, payé sans lien avec l’identité réelle.

**Le téléchargement de fichiers piégés.** L’investigateur télécharge un PDF trouvé sur un forum, un dump partagé sur un canal Telegram, un sample de malware « pour analyse ». Le fichier contient un beacon ou un exploit. La VM est compromise — et si elle communique encore avec l’hôte, l’hôte aussi. Parade : ouvrir tout fichier suspect dans une VM jetable supplémentaire (VM dans la VM), désactiver les exécutions de scripts par défaut, ne jamais télécharger sur la machine hôte.

#### 3.6 Limites de l’OPSEC et risques de la sur-confiance

L’OPSEC parfaite n’existe pas. L’investigateur qui se croit invisible prend des risques en croyant être protégé. Quelques limites structurelles qu’il faut accepter.

Le **fingerprinting navigateur** est devenu très performant. Même en VM, même avec VPN, le navigateur expose des centaines de paramètres (résolution écran, polices installées, plugins, timezone, langue, fingerprint canvas). Une combinaison spécifique de ces paramètres est aussi identifiante qu’une adresse IP. Des outils comme Tor Browser et certains modes anti-tracking de Brave réduisent le fingerprinting, sans l’éliminer.

Les **plateformes elles-mêmes corrèlent** les comptes. Facebook, Google, Microsoft savent corréler plusieurs comptes utilisés depuis le même appareil, le même réseau, le même comportement de navigation. Un avatar utilisé depuis une VM qui partage des éléments d’environnement avec la machine perso peut être corrélé.

Les **fournisseurs VPN ne sont pas tous fiables**. Plusieurs scandales de logs ont émergé ces dernières années (PureVPN, IPVanish). Le « no-logs » est rarement audité, et les juridictions où sont basés les fournisseurs varient en obligation de coopération.

Les **fuites par erreur humaine** dominent les fuites techniques. La majorité des investigations compromises l’ont été par une erreur de l’investigateur (mauvais compte, presse-papiers, clic sur un lien personnel depuis la VM), pas par une attaque sophistiquée.

L’attitude juste : OPSEC sérieuse, calibrée sur le threat model, mais sans illusion d’invisibilité totale. Si une mission exige une OPSEC absolue qu’il est impossible de garantir, il faut le dire au client — pas le simuler.

#### 3.7 Fil rouge — MIRAGE Épisode 2

> **🎯 MIRAGE — Épisode 2 : préparation OPSEC**
> 
> L’investigateur évalue le threat model pour MIRAGE. Marc Delaunay est DAF d’une ETI, 48 ans, profil techniquement compétent (formation initiale ingénieur), mais sans indication de capacités cyber offensives ou de réseau de soutien sophistiqué. Le risque de découverte se situe à un niveau moyen : Delaunay peut détecter une visite LinkedIn ou des consultations agressives, mais n’a pas les moyens de mener une contre-investigation poussée.
> 
> **Décision OPSEC** : niveau moyen. VM dédiée Ubuntu sur l’ordinateur d’investigation (séparé du poste de travail principal), VPN ProtonVPN payé via crypto et dédié à cette enquête, profil Firefox vierge avec uBlock Origin. Trois avatars créés et maturés depuis trois semaines : un compte LinkedIn (profil de consultant freelance fictif), un compte Telegram (numéro burner SMS-Activate), un compte Twitter/X. Téléphone dédié avec SIM prépayée.
> 
> **Décision juridique** : la sollicitation est documentée par contrat avec Legrand & Associés, finalité explicite (collecte de renseignement en vue d’un éventuel contentieux et d’un dépôt de plainte), durée limitée à 6 semaines. Le RGPD est respecté : collecte proportionnée, conservation limitée, finalité légitime. La fiche de cadrage signée par le cabinet sert de justification de l’intérêt légitime.

-----

### Chapitre 4 — Méthodologie d’investigation et outillage

#### 4.1 Le processus structuré

Une investigation OSINT rigoureuse suit un processus en sept phases qui, bien que présentées séquentiellement, se chevauchent en pratique.

Le **cadrage** formule les questions d’investigation, identifie les sélecteurs initiaux, définit le périmètre (géographique, temporel, thématique), et précise les contraintes (délai, budget, OPSEC, livrables attendus). C’est l’étape la plus négligée et la plus déterminante. Une investigation mal cadrée produit du bruit, pas du renseignement.

Le **plan de collecte** liste les sources à mobiliser pour chaque question d’investigation, dans quel ordre, avec quels outils. Il anticipe les dépendances : l’identification d’un email peut conditionner l’accès à des breaches, l’identification d’une société peut conditionner l’accès à des registres. Le plan n’est pas figé — il évolue avec les découvertes — mais il existe.

La **collecte** exécute le plan. Chaque action est documentée dans le journal d’investigation : sélecteur utilisé, source consultée, date et heure, résultat, capture archivée. La discipline de documentation au moment de la collecte est ce qui permettra, des semaines plus tard, de reconstituer la chaîne de raisonnement.

Le **traitement** nettoie, organise, déduplique. Les captures sont nommées de manière cohérente (`YYYYMMDD_source_sélecteur_description.png`), les sélecteurs sont consolidés dans un graphe (Maltego ou équivalent), les doublons sont fusionnés. Le traitement est un travail de bibliothécaire, ingrat mais indispensable.

La **corrélation** établit les liens entre entités, identifie les pivots productifs, révèle les structures cachées. C’est ici que le graphe prend sens : « Delta Consulting Ltd partage son adresse de domiciliation avec 47 autres entités, dont 3 ont des dirigeants liés à Delaunay ».

L’**analyse** interprète : qu’est-ce qui est cohérent avec quelle hypothèse ? Quelle hypothèse alternative pourrait expliquer les mêmes faits ? Quel est le niveau de confiance global ? L’analyse mobilise l’ACH (Ch.21), la cotation de fiabilité (Ch.22), la documentation des biais.

La **production** rédige le rapport (Ch.23). C’est la phase la plus visible — et celle qui rend toutes les phases précédentes valorisables ou non. Un rapport mal rédigé peut détruire des semaines d’investigation rigoureuse.

#### 4.2 La logique du pivot et les six sélecteurs principaux

Le **pivot** est la mécanique centrale de l’OSINT. Un sélecteur (donnée d’identification) en révèle un autre, qui en révèle d’autres. La maîtrise des pivots distingue l’investigateur expérimenté du débutant.

Six sélecteurs principaux structurent la quasi-totalité des pivots OSINT.

Le **nom** est le sélecteur de départ le plus fréquent, et le plus piégeux : les homonymes sont la première cause d’attribution erronée. Un nom seul ne sert qu’à identifier des candidats potentiels — il doit être croisé avec d’autres sélecteurs (date de naissance approximative, ville, employeur, photo) pour confirmer l’identification.

L’**email** est le pivot le plus puissant pour l’OSINT moderne. Un email permet de découvrir les services en ligne où la personne est inscrite (Holehe, Epieos), les fuites de données qui contiennent ses credentials (HIBP, DeHashed), les comptes professionnels associés (Hunter.io, GHunt pour les comptes Google), les profils sociaux liés.

Le **username** (pseudonyme) révèle les comptes sur les centaines de plateformes où la personne s’est inscrite (Sherlock, Maigret, WhatsMyName). Les usernames cohérents entre plateformes sont une des sources les plus productives de corrélation.

Le **numéro de téléphone** ouvre les messageries (WhatsApp, Telegram, Signal — révèlent souvent un nom et une photo si l’utilisateur n’a pas verrouillé sa visibilité), les annuaires inversés (TrueCaller, Sync.me), et certaines fuites massives (le dump Facebook 2021 contient 533 millions de profils avec numéros).

La **photo** permet la recherche inversée (Google Images, Yandex, TinEye), la reconnaissance faciale (PimEyes, FaceCheck.id), l’analyse des métadonnées (EXIF — GPS, appareil, date), et la géolocalisation par indices visuels.

L’**adresse** (postale) révèle les registres immobiliers (cadastre, publicité foncière), les SCI, les voisins, les entreprises domiciliées au même endroit.

Chaque pivot doit être documenté : sélecteur de départ, source consultée, sélecteurs découverts, niveau de confiance de la corrélation. Un pivot non documenté est un pivot perdu — l’investigation deviendra incompréhensible dans quelques jours.

#### 4.3 Outils de gestion de l’investigation

Quatre outils structurent typiquement la gestion d’une enquête OSINT.

**Obsidian** (ou alternative comme Logseq, Joplin) est l’outil de notes structurées. Chaque enquête a son **vault** dédié, chiffré au repos. Une note par entité (personne, société, événement), liée aux notes connexes par des liens internes. Les requêtes Dataview permettent de filtrer (toutes les entités cotées B2 et au-dessus, toutes les sources non encore exploitées). Le formatage Markdown rend les notes portables et indépendantes du logiciel.

**Maltego** (Community Edition gratuite, ou Pro/Classic payantes) est l’outil de graphe relationnel. Les entités (personne, email, domaine, IP, société) sont représentées comme nœuds, les relations comme arêtes. Les **transforms** automatisent la collecte (un email Maltego transformé via Holehe révèle les services associés). La visualisation graphique révèle les structures invisibles dans les notes : grappes denses (concentration d’activité), nœuds centraux (acteurs pivots), liens transversaux (connexions inattendues entre entités).

**Hunchly** est l’outil de capture web. Il capture automatiquement chaque page consultée pendant la session d’investigation, avec horodatage et hash SHA-256. Il permet de constituer une **chaîne de custody** numérique : à n’importe quel moment, l’investigateur peut prouver qu’à telle date, telle page contenait telle information. Indispensable pour les investigations susceptibles de finir devant un juge.

**Timeline Explorer** (ou Aeon Timeline, ou même un simple tableur) gère la **chronologie**. Chaque événement daté est entré (création de société, paiement, post réseau social, voyage). La visualisation temporelle révèle les corrélations qui échappent à l’analyse texte : un transfert bancaire suivi à 48h d’un voyage à Dubaï, une création de société une semaine après un licenciement.

D’autres outils interviennent ponctuellement : **SpiderFoot** pour la collecte automatisée multi-sources, **OSINT Industries** pour les pivots email, **EclecticIQ** pour la CTI structurée, **Aleph** (OCCRP) pour les leaks de données structurées.

#### 4.4 Préservation : capturer avant disparition

La règle n°1 de l’OSINT opérationnelle est : **capturer avant disparition**. Une donnée vue aujourd’hui peut avoir disparu demain — la cible peut supprimer un post, fermer un compte, dissoudre une société, mettre un profil en privé. Si la donnée n’est pas capturée et préservée au moment de la consultation, elle est perdue.

La capture doit être **horodatée** (date et heure UTC), **sourcée** (URL exacte, chemin de navigation), et **hashée** (SHA-256 du fichier de capture). Ces trois éléments forment la base de la chaîne de custody.

Plusieurs niveaux de capture coexistent. La **capture d’écran** est le minimum — utile pour le contenu visuel, fragile pour le contenu textuel (un OCR peut être contesté). L’**enregistrement HTML complet** (via Hunchly, ou `wget --mirror`, ou « Enregistrer la page sous » du navigateur) préserve le contenu textuel et les métadonnées. L’**archivage public** (Wayback Machine via `web.archive.org/save`) crée une copie horodatée publique, vérifiable par un tiers — utile quand la preuve doit être opposable.

Le **hashing** se fait avec `sha256sum fichier.png` (Linux), `Get-FileHash fichier.png -Algorithm SHA256` (PowerShell), ou des outils intégrés (Hunchly hashe automatiquement). Le hash est consigné dans le journal d’investigation.

La **chaîne de custody** documente, pour chaque pièce de preuve, qui l’a capturée, quand, depuis quelle source, comment elle a été stockée, qui y a eu accès, et où elle est conservée. Cette discipline est inutile pour 90 % des investigations privées — mais quand elle devient nécessaire (procédure judiciaire, expertise contradictoire), son absence rend les preuves inexploitables.

#### 4.5 Documentation systématique : le journal d’investigation

Le **journal d’investigation** est le document vivant de l’enquête. Chaque action y est consignée, dans l’ordre chronologique, avec un format constant.

Format type d’une entrée :

```
2026-04-08 14:23 UTC
Sélecteur : Marc Delaunay
Source consultée : https://www.linkedin.com/in/marc-delaunay-XXXX/
Action : Consultation profil via avatar Inv-AV-001
Résultat : Profil identifié — DAF TechnoVert depuis 2019, MBA HEC 2003
Sélecteurs découverts : photo profil (capture jointe), formation HEC (à corroborer)
Capture : 20260408_LinkedIn_Delaunay_profil.png (hash : SHA256:a3f2...)
Cotation : B2 (LinkedIn = source habituellement fiable, info auto-déclarée)
Notes : pas de mention de Delta Consulting ni d'aucune activité externe
```

Le journal sert à trois choses : (1) **reconstituer la chaîne de raisonnement** plusieurs semaines après les faits, (2) **prouver la méthodologie** en cas de contestation (judiciaire, déontologique), (3) **transmettre l’investigation** à un collègue ou à un successeur sans perte d’information.

La discipline du journal est ingrate — c’est cinq minutes de saisie pour chaque action de collecte. C’est aussi ce qui distingue le travail professionnel du bricolage. Un investigateur qui prétend ne pas avoir besoin de journal parce qu’« il s’en souvient » se ment ou ment au client.

#### 4.6 Note sur la durée de vie des outils

Les outils OSINT évoluent rapidement. Des outils centraux il y a trois ans (Pipl en accès gratuit, Maltego avec ses transforms gratuites larges, Telegram bots libéraux) sont devenus payants, restreints, ou bloqués. Des outils nouveaux apparaissent chaque mois.

Cette évolution n’invalide pas le cours, parce que **la méthodologie est durable** alors que **l’outil spécifique est remplaçable**. Apprendre la logique du pivot email permet d’utiliser Holehe aujourd’hui, son successeur dans deux ans, et de comprendre pourquoi tel nouvel outil mérite l’attention quand il sort. Apprendre la nomenclature d’un outil sans la méthodologie produit une expertise périmée.

Les outils cités tout au long du cours sont des **exemples opérationnels à date** (2025-2026). Quand un outil disparaît ou évolue, l’investigateur en cherche un équivalent en gardant la méthodologie comme boussole.

-----

## PARTIE II — RECHERCHE, PERSONNES ET RÉSEAUX SOCIAUX

> **Ce que cette partie apprend.** Maîtriser la recherche structurée (moteurs et dorks), conduire une investigation sur une personne physique (six sélecteurs et leurs pivots), exploiter les réseaux sociaux occidentaux selon une méthodologie en cinq étapes, investiguer Telegram comme plateforme à part entière, et naviguer dans les espaces communautaires alternatifs (Discord, forums, plateformes émergentes).
> 
> **Ce qu’elle ne couvre pas.** Les sources techniques structurées (registres d’entreprises, infrastructure DNS — voir Partie III), les sources visuelles (Partie IV), les sources financières (Partie V).
> 
> **Ce que vous saurez faire après cette partie.** Identifier une personne à partir d’un sélecteur de départ, cartographier sa présence en ligne sur les principales plateformes, exploiter les caractéristiques spécifiques de chaque réseau social, et investiguer les espaces semi-fermés sans compromettre l’OPSEC.

-----

### Chapitre 5 — Moteurs de recherche, Google Dorking et archivage web

#### 5.1 Les moteurs : Google, Bing, Yandex, DuckDuckGo, Baidu

Aucun moteur n’indexe la totalité du web et chaque moteur a ses biais. Un investigateur sérieux n’utilise jamais un seul moteur — il les croise systématiquement.

**Google** reste le moteur avec l’index le plus large globalement, et celui dont les opérateurs avancés sont les plus aboutis. Son défaut est la personnalisation forte des résultats : un utilisateur connecté à son compte Google reçoit des résultats orientés par son historique. Pour l’OSINT, Google s’utilise toujours en navigation privée ou depuis un profil dédié, idéalement déconnecté de tout compte Google.

**Bing** indexe des résultats sensiblement différents de Google, particulièrement sur les contenus institutionnels et certains documents techniques. Il a une couverture supérieure de certains réseaux sociaux (LinkedIn notamment) et son moteur d’images est utile en recherche inversée.

**Yandex** est le moteur incontournable pour deux usages spécifiques : la **reconnaissance faciale** (de loin le plus performant des moteurs grand public sur les visages) et le **contenu non-anglophone**, particulièrement russophone. Pour toute investigation impliquant la sphère post-soviétique, Yandex est aussi indispensable que Google pour la sphère anglophone.

**DuckDuckGo** agrège principalement les résultats Bing, sans tracking. Il n’apporte pas de couverture supplémentaire mais permet de consulter Bing sans cookies persistants.

**Baidu** est le moteur dominant en Chine. Indispensable pour toute investigation sur la sphère sinophone — entreprises chinoises, dirigeants, contenus en mandarin. Son interface est entièrement en chinois ; les outils de traduction (Google Translate, DeepL) sont nécessaires pour exploiter les résultats.

**Naver** joue le même rôle pour la Corée du Sud, **Seznam** pour la République tchèque, **Daum** pour la Corée également. Les moteurs locaux indexent souvent des contenus que les moteurs globaux ratent.

#### 5.2 Google Dorks : opérateurs avancés

Les **Google Dorks** sont des opérateurs de recherche avancés qui transforment Google d’un moteur grand public en un outil d’investigation puissant. Apprendre les dorks est l’investissement le plus rentable du débutant en OSINT.

|Opérateur           |Effet                                         |Exemple                                |
|--------------------|----------------------------------------------|---------------------------------------|
|`site:`             |Restreint à un domaine                        |`site:linkedin.com "Marc Delaunay"`    |
|`filetype:`         |Restreint à un type de fichier                |`"TechnoVert" filetype:pdf`            |
|`intitle:`          |Mot dans le titre de la page                  |`intitle:"rapport annuel" "TechnoVert"`|
|`inurl:`            |Mot dans l’URL                                |`inurl:cv "Marc Delaunay"`             |
|`intext:`           |Mot dans le corps de la page                  |`intext:"Delta Consulting"`            |
|`"phrase exacte"`   |Recherche littérale                           |`"Delaunay" "Delta Consulting"`        |
|`-mot`              |Exclusion                                     |`Delaunay -prénom_homonyme`            |
|`OR`                |Disjonction                                   |`"Delta Consulting" OR "Delta Holding"`|
|`*`                 |Joker dans une expression                     |`"Marc * Delaunay"`                    |
|`AROUND(n)`         |Mots à proximité                              |`Delaunay AROUND(5) consultant`        |
|`before:` / `after:`|Filtre temporel                               |`"Delaunay" after:2020-01-01`          |
|`cache:`            |Version en cache                              |`cache:example.com`                    |
|`link:`             |Pages qui pointent vers (déprécié, peu fiable)|—                                      |
|`related:`          |Pages similaires                              |`related:technovert.fr`                |

La combinaison d’opérateurs démultiplie la puissance. `site:linkedin.com "Marc Delaunay" "Delta Consulting"` cherche des profils LinkedIn mentionnant les deux entités. `filetype:pdf "TechnoVert" intext:"chiffre d'affaires"` cherche des rapports PDF mentionnant TechnoVert avec ses chiffres.

#### 5.3 Dorks par objectif

Les dorks deviennent vraiment opérationnels quand ils sont organisés par objectif d’investigation. Le catalogue complet est en Annexe B ; voici les familles principales.

**Documents financiers exposés** : `filetype:pdf "rapport annuel" SOCIÉTÉ`, `filetype:xlsx "compte de résultat" SOCIÉTÉ`, `intitle:"index of" "factures" SOCIÉTÉ`. Beaucoup d’entreprises laissent traîner des documents internes sur des sous-domaines mal protégés.

**Organigrammes et trombinoscopes** : `filetype:pdf "organigramme" SOCIÉTÉ`, `site:SOCIÉTÉ.com inurl:team`, `site:SOCIÉTÉ.com inurl:about`. Utile pour identifier les dirigeants, les responsables, les structures.

**Emails exposés** : `site:SOCIÉTÉ.com filetype:pdf "@SOCIÉTÉ.com"`, `intext:"@SOCIÉTÉ.com" -site:SOCIÉTÉ.com` (mentions externes des emails de la société).

**Directory listings** (répertoires indexés par erreur) : `intitle:"index of" SOCIÉTÉ`, `intitle:"index of /backup"`, `intitle:"index of /admin"`. Ces résultats sont à manier avec précaution juridique (jurisprudence Bluetouff).

**Recherche temporelle** : `"événement" before:2024-12-31 after:2024-01-01` cible une fenêtre. Utile pour reconstituer une chronologie ou identifier la première mention d’un sujet.

**Plateformes spécifiques** : `site:linkedin.com/in/ "intitulé poste" "société"`, `site:t.me "username"`, `site:github.com "email@société.com"`, `site:pastebin.com "fragment de données"`.

#### 5.4 Yandex pour les visages et le contenu non-anglophone

Yandex Images mérite un traitement spécifique. Son algorithme de reconnaissance faciale et de matching d’images est sensiblement supérieur à celui de Google Images, particulièrement sur des personnes peu présentes dans l’index occidental.

Pour rechercher une personne par photo : sauvegarder l’image localement, aller sur `yandex.com/images`, cliquer sur l’icône appareil photo, uploader. Yandex retourne les images visuellement similaires, souvent avec des correspondances de visage dans des contextes différents (la même personne sur un autre site, dans un événement, dans un article).

La couverture **non-anglophone** de Yandex est également supérieure : sites russophones, ukrainiens, biélorusses, kazakhs, mais aussi turcs, arabes, persans dans certains cas. Pour toute investigation sur ces sphères, Yandex est un complément indispensable.

#### 5.5 Baidu et la recherche en chinois

Baidu indexe le web sinophone que Google n’indexe que partiellement (et que la Chine censure d’ailleurs côté Google). Pour une investigation sur une entreprise chinoise, un dirigeant chinois, ou des relations sino-européennes, Baidu est obligatoire.

Méthode pratique : traduire les sélecteurs de départ en chinois (idéogrammes simplifiés) avec un outil sérieux (DeepL, Pleco pour les noms propres), tester plusieurs translittérations possibles d’un nom occidental, croiser avec les bases d’entreprises chinoises (Qichacha, Tianyancha — équivalents de Pappers en Chine).

Les résultats sont entièrement en chinois. L’investigateur qui ne parle pas la langue doit s’appuyer sur Google Translate ou DeepL pour le contenu, et se faire valider les conclusions sensibles par un sinophone.

#### 5.6 Archivage web : Wayback Machine, archive.today, Google Cache

L’archivage web est l’arme contre la disparition. Les sites changent, les pages sont modifiées, les contenus sont supprimés. L’investigateur a besoin de retrouver l’état antérieur — pour reconstituer une chronologie, pour prouver qu’un contenu a existé, pour exploiter des informations effacées.

La **Wayback Machine** (`web.archive.org`) est l’archive web la plus large et la plus ancienne (depuis 1996). Elle archive automatiquement des centaines de milliards de pages. Couverture variable selon les sites : un grand journal est archivé plusieurs fois par jour, un site obscur peut n’avoir qu’une capture par an. La fonction « Save Page Now » permet d’archiver manuellement une page consultée — réflexe à acquérir pour toute page sensible.

**archive.today** (`archive.ph`) est un service alternatif qui capture des snapshots à la demande. Avantage : gère mieux les sites JavaScript-heavy et les paywalls. Indispensable en complément de Wayback.

**Google Cache** affichait la dernière version indexée par Google d’une page. Google a déprécié la fonction en 2024 — elle est désormais inaccessible directement. Bing Cache reste une alternative partielle.

**Mémoire des recherches** : si une page est citée dans des résultats Google avec un extrait pertinent, l’extrait constitue une preuve faible que le contenu a existé, même si la page a disparu.

Les **archives de spécialité** complètent : `archive-it.org` pour les institutions, `cachedview.com` qui agrège plusieurs caches, `pagefreezer.com` pour les besoins juridiques (preuves opposables certifiées).

#### 5.7 Captures et préservation des résultats

Une recherche productive ne sert à rien si les résultats ne sont pas préservés au moment de la consultation. La discipline de capture s’applique à chaque résultat significatif.

Pour une **page web entière** : capture HTML complète via Hunchly (idéal — automatique, hashée, horodatée), ou « Enregistrer la page sous → page web complète » du navigateur, ou `wget --mirror --convert-links URL`. La capture d’écran seule perd les métadonnées et le contenu structurel.

Pour un **résultat Google** : capture d’écran de la page de résultats (montre le contexte, les autres résultats), suivie de la capture de la page cible. Les deux captures sont liées dans le journal.

Pour un **profil de réseau social** : capture du profil au moment T, puis monitoring si l’investigation se prolonge (le profil peut être modifié, mis en privé, supprimé). Outils : Hunchly pour les captures successives, Visualping pour le monitoring de changement.

Pour les **vidéos** : téléchargement avec `yt-dlp` (succession de youtube-dl) qui supporte des centaines de plateformes, conservation du fichier original avec ses métadonnées.

#### 5.8 Limites et faux positifs des moteurs

Les moteurs de recherche ont des limites structurelles qu’il faut connaître pour ne pas tirer de conclusions erronées.

**Indexation partielle** : Google indexe entre 5 et 10 % du web — le reste est dans le « deep web » (contenus authentifiés, bases de données, intranets). Une absence de résultat Google ne signifie pas une absence d’information sur le sujet. C’est particulièrement vrai pour les contenus récents (délai d’indexation de quelques jours à quelques semaines), les contenus protégés par robots.txt, les contenus dans des langues peu indexées.

**Personnalisation et géolocalisation** : Google adapte les résultats à l’utilisateur (compte, historique) et à la localisation détectée (IP, paramètres de langue). Deux investigateurs au même moment, depuis des localisations différentes, voient des résultats différents pour la même requête. Parade : utiliser un VPN avec sortie dans un pays cohérent avec l’investigation, paramétrer la langue du navigateur, utiliser le mode privé.

**SafeSearch et filtres** : les filtres anti-contenu adulte (SafeSearch) éliminent des résultats légitimes en investigation (sites adultes utilisés par certaines arnaques, contenus violents documentant des crimes). À désactiver pour les investigations sensibles.

**Faux positifs sémantiques** : un résultat qui contient les mots-clés cherchés n’est pas nécessairement pertinent. Un article sur « Marc Delaunay » peut concerner un homonyme. Une mention de « TechnoVert » peut concerner une autre société. La vérification du contexte est obligatoire avant d’utiliser un résultat.

**Un résultat n’est pas une preuve** — c’est une piste à vérifier. Le fait qu’une page Google contienne une affirmation ne prouve pas que l’affirmation soit exacte. La cotation de fiabilité (Ch.22) s’applique à chaque source.

#### 5.9 Fil rouge — MIRAGE Épisode 3

> **🎯 MIRAGE — Épisode 3 : Google Dorking sur Marc Delaunay**
> 
> L’investigateur déploie une série de dorks ciblés.
> 
> `"Marc Delaunay" site:linkedin.com` → identifie un profil LinkedIn (DAF TechnoVert depuis 2019, MBA HEC, mentions de plusieurs sociétés antérieures). Capture via Hunchly.
> 
> `"m.delaunay" filetype:pdf` → un CV de 2018, hébergé sur un site de recrutement, mentionne un email personnel : `marcdelaunay75@gmail.com`. Sélecteur précieux — premier email perso identifié.
> 
> `"Marc Delaunay" "TechnoVert" -linkedin` → trois articles de presse économique, un communiqué TechnoVert pour une nomination, et un post sur un forum d’investisseurs (qui mentionne en passant « le DAF de TechnoVert qui passe ses week-ends à Malte »). Le post est anodin mais le détail Malte est noté.
> 
> `"TechnoVert" "Delta Consulting"` → un seul résultat : un PDF d’archive d’une conférence à Malte, qui liste « Delta Consulting Ltd » et « TechnoVert SAS » parmi les sponsors d’un même événement de 2022. Première trace publique d’un lien entre les deux entités.
> 
> `intitle:"index of" "TechnoVert"` → un répertoire indexé sur un sous-domaine (`old.technovert.fr`) contenant des anciens documents internes. L’investigateur **ne télécharge pas** : Bluetouff. Il documente l’existence du répertoire mais ne s’y maintient pas.
> 
> Première itération de pivot : nom → email perso, mention « Malte », lien public Delta Consulting / TechnoVert. Le graphe Maltego compte désormais 4 entités.

-----

### Chapitre 6 — Investigation sur les personnes physiques

#### 6.1 La logique du pivot appliquée aux personnes

L’investigation sur une personne physique mobilise systématiquement la logique des six sélecteurs (Ch.4.2). L’art consiste à savoir quel pivot utiliser à quel moment, et à reconnaître quand un pivot productif révèle un homonyme plutôt que la cible.

La séquence type d’une investigation personne commence par un **sélecteur de qualification** (le nom + un attribut secondaire qui élimine les homonymes : ville, employeur, date de naissance approximative). De là, l’investigateur cherche des **sélecteurs identifiants** (email, username, téléphone) qui permettent les pivots productifs vers les comptes en ligne, les fuites, et les services associés. Enfin, des **sélecteurs corroborants** (photos, mentions presse, registres officiels) confirment ou invalident les hypothèses.

Cette séquence n’est pas linéaire. Une enquête peut commencer par un username (compte pseudonyme à dé-anonymiser, voir Ch.27), une photo (identification d’une personne dans une image), ou un numéro de téléphone (numéro suspect dans une fraude). La méthodologie reste la même : pivoter, documenter, vérifier la cohérence.

#### 6.2 Recherche par nom et registres publics

Le nom seul est rarement suffisant — les homonymes sont la première cause d’attribution erronée en OSINT. Un Marc Delaunay en France, c’est plusieurs centaines de personnes. Le travail de qualification est donc l’étape obligatoire.

**Combiner le nom avec des qualificateurs** : ville, employeur, date de naissance approximative, formation, profession. Chaque qualificateur réduit l’espace des homonymes.

**Annuaires inversés et bases de personnes par pays** :

- **France** : 118712.fr, PagesJaunes (annuaire fixe), pas d’annuaire mobile public officiel — la portabilité des numéros a fragmenté les données.
- **États-Unis** : ThatsThem, FastPeopleSearch, BeenVerified (les trois nécessitent une IP US — VPN obligatoire pour un investigateur européen). Couverture américaine très large grâce aux « public records » plus libéraux.
- **Royaume-Uni** : 192.com (payant après quelques recherches), open electoral register.
- **Allemagne** : DasTelefonbuch, mais protection forte de la vie privée — moins de données publiques.
- **International** : Lampyre (payant, agrège plusieurs sources), Pipl (payant, anciennement gratuit, devenu professionnel).

**Registres publics français de haute fiabilité (cotation A1)** :

- **Pappers / Infogreffe** : sociétés, dirigeants, comptes, modifications statutaires.
- **BODACC** (Bulletin Officiel des Annonces Civiles et Commerciales) : créations, modifications, dissolutions.
- **JO Associations** : créations et modifications d’associations loi 1901.
- **Cadastre.gouv.fr** : parcelles, propriétaires (le nom du propriétaire n’est plus publiquement accessible depuis 2017, mais la consultation en mairie reste possible).
- **Publicité foncière** (notariale, payante) : transactions immobilières, hypothèques.
- **Légifrance** : jurisprudence — un nom dans une décision de justice publiée révèle un contentieux.
- **HAVTP (Haute Autorité pour la Transparence de la Vie Publique)** : déclarations d’intérêts et de patrimoine des élus et hauts fonctionnaires.

**Faux positifs fréquents** : les homonymes sont systématiques. Parade : toujours croiser avec **deux sélecteurs indépendants minimum**. Si le candidat « Marc Delaunay » trouvé dans Pappers est gérant d’une société à Lyon, mais que la cible vit à Paris et n’a aucun lien connu avec Lyon, c’est probablement un homonyme — à creuser, ou à écarter explicitement dans le rapport.

Si la confirmation est impossible, l’attribution est cotée « incertaine » et signalée comme telle. Mieux vaut un rapport avec des zones d’incertitude documentées qu’un rapport faussement précis.

#### 6.3 Recherche d’emails

L’email est le pivot le plus puissant de l’OSINT moderne, parce qu’il sert d’identifiant pour des centaines de services en ligne et qu’il apparaît dans de nombreuses fuites de données.

**Découvrir un email** :

- **Hunter.io** (freemium) : trouve les emails associés à un domaine et identifie le pattern de nommage (`prénom.nom@`, `pnom@`, `prénom_nom@`). Excellent pour les contextes corporate.
- **Phonebook.cz** : interroge les fuites de données pour trouver les emails associés à un domaine.
- **Email permutator** (plusieurs implémentations en ligne) : génère toutes les combinaisons probables (`marc.delaunay@`, `mdelaunay@`, `m.delaunay@`, etc.) à partir d’un nom et d’un domaine.
- **Vérification** : Hunter.io ou MailTester confirment qu’un email existe (sans alerter le destinataire — pas de mail envoyé).

**Pivoter à partir d’un email** — c’est ici que se joue l’essentiel :

- **Holehe** (open source, Python) : vérifie sur quels services en ligne l’email est enregistré, sans alerter le titulaire. Couvre une centaine de services (Spotify, Netflix, Adobe, eBay, Imgur, Dropbox, et critiquement les exchanges crypto : Coinbase, Binance, Kraken). Un email enregistré sur un exchange crypto est un signal majeur dans une investigation patrimoniale.
- **Epieos** (freemium, basé sur Holehe + extras) : interface web, ajoute des fonctions (reverse Google email pour récupérer le nom et la photo associés au compte Google).
- **GHunt** (open source) : spécifique à Google, récupère les informations publiques d’un compte Google à partir de l’email (photo, nom, organisation, calendrier public, avis Google Maps).
- **Have I Been Pwned, DeHashed, IntelX** : fuites contenant l’email (Ch.12).

**Limites** : ces outils open source se font régulièrement bloquer par les plateformes (rate limiting, changements d’API). Leur maintenance dépend de contributeurs bénévoles. Un résultat négatif (« email non trouvé ») ne signifie **pas** que le compte n’existe pas — la détection a pu échouer. Compléter par des vérifications manuelles (tentative de récupération de mot de passe sur le service ciblé, qui révèle souvent si l’email est connu, mais qui peut alerter le titulaire — précaution).

#### 6.4 Pivot email vers comptes : Holehe, Epieos, GHunt

L’utilisation typique de Holehe :

```bash
holehe marcdelaunay75@gmail.com
```

Sortie type : liste des services où l’email est enregistré, avec niveau de confiance. Un email enregistré sur Binance + Coinbase + Spotify + Adobe + Instagram donne immédiatement une cartographie des comptes à investiguer.

GHunt sur un email Google révèle :

- Le **nom** associé au compte Google (peut différer du nom déclaré ailleurs).
- La **photo de profil** Google (souvent réutilisée sur d’autres services).
- L’**organisation** si compte Google Workspace.
- Les **avis Google Maps** publics (révélateurs de localisation : restaurant local fréquenté = ville de résidence probable).
- Le **calendrier public** s’il existe.
- Les **photos partagées publiquement** dans Google Photos (rare mais pas impossible).

#### 6.5 Recherche de numéros de téléphone

Le numéro de téléphone est un sélecteur puissant parce qu’il est associé à des messageries (WhatsApp, Telegram, Signal) qui exposent souvent un nom et une photo si l’utilisateur n’a pas verrouillé sa visibilité.

**Annuaires inversés** :

- **TrueCaller** (mobile, freemium) : crowdsourcé — les utilisateurs partagent leurs carnets de contacts, ce qui permet à TrueCaller d’identifier un appelant même si le numéro n’est pas dans les annuaires officiels. Très efficace, juridiquement contesté (RGPD).
- **Sync.me** : équivalent de TrueCaller.
- **Annuaires nationaux** : 118712.fr (France, fixes), équivalents par pays.

**Pivot téléphone vers messageries** :

- **WhatsApp** : ajouter le numéro aux contacts du téléphone d’investigation, ouvrir WhatsApp — si le numéro a un compte WhatsApp, la photo de profil et le statut s’affichent (sauf si l’utilisateur a verrouillé la visibilité).
- **Telegram** : équivalent. Si l’utilisateur est sur Telegram, le username s’affiche (s’il en a un), et la photo si non verrouillée.
- **Signal** : indique uniquement si le numéro est sur Signal, sans photo (Signal est plus restrictif sur la confidentialité).

**Le dump Facebook 2021** est une ressource souvent utile. En avril 2021, un dump de 533 millions de profils Facebook a été publié, contenant pour chaque profil : numéro de téléphone, nom, email, date de naissance, lieu de résidence, employeur. Ce dump est consultable via DeHashed, IntelX, et certains autres services. Pivoter d’un numéro vers ce dump permet souvent d’obtenir nom + email + employeur d’un coup. Limite : les données datent de 2019 (date du scrape), peuvent être obsolètes.

#### 6.6 Recherche par username : Sherlock, Maigret, WhatsMyName

Le username est le pivot le plus productif pour identifier la présence en ligne d’une personne, parce que les utilisateurs réutilisent presque toujours le même pseudonyme (ou une variation proche) sur plusieurs plateformes.

**Sherlock** (open source, Python) cherche un username sur 300+ plateformes et liste celles où le compte existe. Usage :

```bash
sherlock marc_del75
```

**Maigret** (fork de Sherlock, plus complet) couvre 2500+ plateformes et tente d’extraire des données (photo, bio, localisation) en plus de l’existence du compte.

**WhatsMyName** est un outil web et CLI maintenu activement, avec un moindre taux de faux positifs que Sherlock (qui peut signaler des comptes existants alors qu’ils sont inactifs ou différents).

**Méthodologie** : tester le username exact, puis des variations (`marcdel75`, `m_delaunay`, `marcdelaunay75`, `delmarc`). Les outils ne sont pas exhaustifs — toujours compléter par une recherche Google `"username"` qui peut révéler des plateformes non couvertes par les outils.

**Faux positifs** : un username populaire peut avoir été utilisé par différentes personnes. `marc_del75` peut être notre Marc Delaunay sur GitHub (compte de développement professionnel) et un parfait inconnu sur un forum de moto (homonyme de pseudo). La **vérification de cohérence** est obligatoire :

- Cohérence temporelle (les comptes sont actifs aux mêmes périodes).
- Cohérence stylistique (style d’écriture, sujets traités).
- Cohérence visuelle (avatar, photo de profil).
- Cohérence du fuseau horaire (heures de publication).

Un username qui correspond sur 5 plateformes avec 3 dimensions de cohérence est une attribution forte. Un username sur une seule plateforme sans cohérence est une simple piste.

#### 6.7 Reconnaissance faciale : usages et garde-fous

La reconnaissance faciale OSINT a fait des progrès considérables depuis 2020. Les outils grand public permettent désormais ce qui, il y a cinq ans, était réservé aux services de police.

**PimEyes** (payant, ~30 €/mois) : recherche un visage dans une base agrégée d’images du web public. Performant, retourne des correspondances avec liens vers les pages source. Ne couvre **pas** les réseaux sociaux fermés (Facebook, Instagram fermés) mais couvre largement les forums, sites de rencontres, articles de presse, sites perso.

**FaceCheck.id** : équivalent freemium, performant sur les visages publics.

**Search4Faces** : spécialisé sur VK et Odnoklassniki (réseaux sociaux russophones). Indispensable pour les investigations sur la sphère post-soviétique.

**Yandex Images** : meilleur moteur de recherche d’images grand public sur les visages, largement supérieur à Google Images. Gratuit.

**Garde-fous obligatoires** :

- La reconnaissance faciale **suggère, ne prouve jamais**. Un match est une piste à corroborer, pas une identification.
- Cotation à la baisse systématique (C3 ou D3).
- Vérification que la correspondance est cohérente avec d’autres sélecteurs (timeline, géographie, cercle social).
- Précaution juridique RGPD (Ch.2.6) : utiliser pour confirmer une identité déjà identifiée, pas pour identifier un inconnu.

**Faux positifs** : significatifs. Les jumeaux (rare), les sosies (fréquent dans les profils types — homme blanc cadre 45 ans), les variations d’âge (la même personne à 30 ans et à 50 ans est mal reconnue), les angles différents, les lunettes, les barbes. Un seul match n’est rien — plusieurs matches cohérents commencent à compter.

#### 6.8 Le piège des homonymes et la discipline de cohérence

L’attribution erronée par homonymie est l’erreur la plus coûteuse de l’OSINT. Elle peut détruire la crédibilité d’une investigation entière, exposer l’investigateur à des poursuites pour diffamation, et nuire injustement à un tiers.

La discipline de cohérence est la parade. Avant d’attribuer un fait à la cible, l’investigateur vérifie systématiquement :

**Cohérence temporelle** : les éléments collectés sont-ils dans une période compatible avec la vie de la cible ? Un compte créé en 1998 sur un forum est-il compatible avec l’âge supposé de la cible ?

**Cohérence géographique** : les indices de localisation convergent-ils ? Si la cible vit à Paris, des activités systématiquement localisées à Lyon sont suspectes (ou révèlent une activité secondaire à Lyon — à investiguer, pas à conclure d’office).

**Cohérence sociale** : le réseau de relations est-il cohérent ? Si les amis Facebook supposés ne mentionnent jamais la cible, ou si aucun collègue connu n’apparaît dans les connexions LinkedIn, c’est un signal.

**Cohérence visuelle** : les photos identifiées sont-elles compatibles entre elles (même personne) ?

**Cohérence stylistique** : le style d’écriture entre comptes attribués à la même personne est-il cohérent ?

**Discipline** : si moins de trois dimensions de cohérence convergent, l’attribution est marquée comme « incertaine » dans le rapport. C’est éthique, c’est juridiquement protecteur, et c’est ce qui distingue le renseignement de la spéculation.

#### 6.9 Fil rouge — MIRAGE Épisode 4

> **🎯 MIRAGE — Épisode 4 : Holehe → Maigret → PimEyes**
> 
> L’investigateur exploite l’email perso identifié au Ch.5 : `marcdelaunay75@gmail.com`.
> 
> **Holehe** sur l’email : présence confirmée sur **Binance**, **Coinbase**, **Instagram**, **Booking**, **Airbnb**, **Adobe**, **Spotify**. Présence sur Binance et Coinbase = signal majeur pour la QI-3 (crypto-actifs).
> 
> **GHunt** sur l’email : récupère le nom Google associé (« Marc Delaunay »), la photo de profil Google (un homme la cinquantaine, costume, fond bureau), et trois avis Google Maps publics (un restaurant à Levallois-Perret — domicile probable, deux hôtels à La Valette — confirmation Malte).
> 
> **Username Instagram** identifié via consultation du profil public : `marc_del75`.
> 
> **Maigret** sur `marc_del75` : présence sur GitHub (un fork ancien d’un projet finance personnelle), sur un forum « Voitures de Luxe France » (pseudo actif depuis 2017, mentions de Porsche et Bentley — train de vie incohérent avec un salaire de DAF d’ETI), sur un forum poker en ligne (activité nocturne).
> 
> **PimEyes** sur la photo de profil Google : trois correspondances. Une sur le site TechnoVert (page « Direction » — confirmation identité). Une sur un site événementiel (conférence à Lisbonne 2023). Une sur un site de rencontres (`Marco D., 48 ans, Paris — chef d’entreprise »). Cotation D3 pour la dernière (PimEyes = peu fiable, à corroborer).
> 
> **Vérification de cohérence** : email perso → Binance/Coinbase + Instagram + Booking. Username `marc_del75` → cohérent avec `marcdelaunay75@gmail.com` (réutilisation du nombre 75 — code postal de Paris ? année de naissance ? les deux). Forum voitures de luxe → cohérent avec restaurants chers + voyages Malte. Site de rencontres → à corroborer (la photo correspond mais le pseudo « Marco D. » est ambigu).
> 
> **Sélecteurs ajoutés au graphe** : email perso, 7 services en ligne (dont 2 exchanges crypto), username `marc_del75`, 3 contextes de présence (TechnoVert, conférence Lisbonne, site de rencontres).

-----

### Chapitre 7 — SOCMINT : méthodologie générale et plateformes occidentales

#### 7.1 Méthodologie SOCMINT en cinq étapes

Toute investigation SOCMINT, quelle que soit la plateforme, suit cinq étapes structurées. La standardisation de la méthode permet de garantir la complétude et la traçabilité.

**Étape 1 — Identification.** Trouver le compte de la cible sur la plateforme. Cela peut se faire par recherche directe (Google dorks `site:plateforme.com`), par pivot (un username trouvé ailleurs, un email associé), ou par identification visuelle (PimEyes, recherche inversée de la photo de profil).

**Étape 2 — Extraction.** Capturer le contenu pertinent : profil (photo, bio, métadonnées), publications (texte, images, vidéos), relations (followers, following, amis, mentions), interactions (likes, partages, commentaires). La capture doit être horodatée et systématique — un post peut être supprimé à tout moment.

**Étape 3 — Analyse de contenu.** Que dit la cible ? De quoi parle-t-elle ? Avec quel ton, quels sujets, quels intérêts ? Les publications révèlent des localisations (check-ins, hashtags géographiques), des relations (mentions, tags), des opinions, des activités, un mode de vie.

**Étape 4 — Analyse de réseau.** Avec qui interagit-elle ? Qui sont les contacts récurrents ? Y a-t-il des grappes de relations identifiables (collègues, famille, cercle d’investissement) ? Le graphe relationnel révèle souvent plus que le contenu lui-même.

**Étape 5 — Préservation.** Tout est consigné dans le journal d’investigation, capturé via Hunchly, hashé, et organisé dans le vault Obsidian. La règle « capturer avant disparition » est absolue sur les réseaux sociaux : un compte mis en privé ou supprimé est perdu.

#### 7.2 Facebook

Facebook reste, malgré la baisse d’usage, l’un des réseaux sociaux les plus riches en données pour l’OSINT — particulièrement pour les profils créés avant 2018, époque où la confidentialité par défaut était plus laxiste.

**Recherche** : `site:facebook.com "Marc Delaunay"` via Google reste le moyen le plus fiable. La recherche interne Facebook est devenue très restreinte depuis la suppression de Graph Search (2019). Les **dorks Facebook** (URLs de recherche structurées) permettent encore certaines recherches avancées, mais avec un taux de fonctionnement variable.

**Extraction d’ID utilisateur** : chaque profil Facebook a un ID numérique stable (visible via `view-source:` sur le profil, ou via outils comme findmyfbid.in). L’ID stable permet de retrouver un profil même si l’utilisateur change son URL personnalisée ou son nom.

**Sources de données utilisables** :

- **Profil public** : photo, bio, ville, employeur, formation, situation amoureuse (champs auto-déclarés).
- **Photos publiques** : capturer toutes les photos du profil, vérifier les commentaires (qui apparaît, qui réagit) et les tags.
- **Amis publics** : visible si le paramètre n’est pas verrouillé. Le réseau d’amis révèle souvent l’identité réelle (nom et prénom des frères et sœurs, nom de jeune fille de la mère, etc.).
- **Likes et abonnements publics** : pages aimées, groupes rejoints (les groupes peuvent être publics ou privés).
- **Événements publics** : participation déclarée à des événements (concerts, conférences, fêtes).
- **Check-ins** : localisations déclarées sur des photos ou des publications.
- **Vie » et photos de profil archivées** : Facebook conserve l’historique des photos de profil et de couverture, souvent visible publiquement.

**Limites** : la majorité des profils ont aujourd’hui une confidentialité serrée. Un profil avec uniquement la photo de profil visible n’apporte pas grand-chose. Mais les **archives** des profils plus anciens, capturées par Wayback Machine, sont parfois exploitables.

#### 7.3 Instagram

Instagram est devenu central pour l’OSINT patrimoniale (train de vie visible) et pour l’OSINT sur les jeunes adultes (40 % des utilisateurs ont entre 18 et 34 ans).

**Recherche** : recherche directe par username, ou via Google `site:instagram.com "username"`. La recherche interne nécessite un compte. Pour observer sans laisser de trace, utiliser un avatar dédié (Ch.3.3).

**Sources** :

- **Profil public** : bio, lien externe (souvent un Linktree qui multiplie les liens), métriques (followers, following, posts).
- **Stories** : durée 24h — capturer immédiatement. Les stories révèlent souvent la vie quotidienne, les voyages en cours, les relations.
- **Posts** : photos avec leurs commentaires, hashtags, géolocalisations explicites.
- **Tagged posts** : photos où la cible a été taguée par d’autres — souvent plus révélatrices que ses propres posts.
- **Highlights** (stories à la une) : stories préservées par la cible — un signal de ce qu’elle juge important.
- **Reels** : vidéos courtes, parfois avec géolocalisation et avec des commentaires.
- **Followers / Following** : liste des comptes suivis et qui suivent. La consultation peut nécessiter de scroller indéfiniment ; outils comme Picuki (statut variable) ou des extractions semi-manuelles.

**Limites** : les profils privés ne révèlent rien d’autre que la photo et la bio. Les outils de scraping Instagram changent constamment — les fonctionnalités gratuites apparaissent et disparaissent.

#### 7.4 LinkedIn

LinkedIn est la première source OSINT corporate. Mais c’est aussi la plateforme avec les plus fortes contre-mesures contre l’observation passive.

**Le problème central** : LinkedIn **notifie** la cible quand on consulte son profil (en mode normal). Une consultation depuis le compte personnel de l’investigateur compromet immédiatement la mission.

**Solutions** :

- **Google dorks** : `site:linkedin.com/in/ "Marc Delaunay"` permet de voir le profil sans consulter directement (les snippets Google contiennent souvent les informations clés). Aucune notification.
- **Compte LinkedIn premium** avec mode privé activé : consultation possible sans révéler son identité (la cible voit « Quelqu’un de [secteur] a consulté votre profil »).
- **Avatar dédié** en mode privé : consultation depuis un compte d’investigation, mode confidentialité activé.

**Sources** :

- **Profil public** : poste actuel, historique professionnel, formation, certifications, compétences.
- **Recommandations** : qui a recommandé la cible — souvent révélateur du cercle professionnel réel (et plus fiable que les simples connexions).
- **Connexions partagées** (visible si compte premium ou via parcours de connexion) : intersection avec d’autres profils investigués.
- **Posts et activité** : ce que la cible publie, like, commente — révèle ses centres d’intérêt et ses positionnements.
- **Mentions externes** : LinkedIn est largement référencé hors plateforme — articles de presse qui citent le profil, conférences listant les intervenants.

**Limites** : la majorité des profils ont des paramètres de confidentialité qui masquent l’historique récent. Sales Navigator (payant) donne plus d’accès mais avec un risque détectable.

#### 7.5 X / Twitter

X (anciennement Twitter) est devenu sensiblement plus difficile à investiguer depuis 2023, avec la fermeture de l’API publique gratuite et les restrictions d’accès aux non-connectés.

**Recherche avancée** : Twitter Advanced Search (`twitter.com/search-advanced`) supporte de nombreux opérateurs :

- `from:username` — posts d’un utilisateur.
- `to:username` — posts adressés à un utilisateur.
- `since:YYYY-MM-DD until:YYYY-MM-DD` — fenêtre temporelle.
- `filter:replies` / `filter:media` / `filter:links` — types de posts.
- `geocode:lat,lng,rayon` — géolocalisation (en déclin de fonctionnalité).
- `lang:fr` — langue.

**Restrictions 2025** : depuis le rachat par Elon Musk, plusieurs restrictions ont été imposées. La **consultation sans compte** est limitée à quelques posts. L’**API** est devenue payante (à partir de plusieurs centaines d’euros par mois pour un usage sérieux). Les **instances Nitter** (front-ends alternatifs gratuits) sont en déclin — la plupart ont été bloquées par X courant 2024-2025.

**Stratégie 2025-2026** :

- **Compte d’investigation** sur X (avatar) pour la consultation passive.
- **Archivage anticipé systématique** des posts pertinents via Wayback Machine ou archive.today.
- **Outils tiers payants** : Brand24, Mention, Hootsuite Insights pour le monitoring (coûteux mais maintenus).
- **Ressources spécialisées** : SocialBearing, FollerMe (statuts variables).

**Sources** :

- **Profil** : bio, lien, date de création, métriques.
- **Timeline** : posts originaux, retweets, réponses, likes (les likes sont parfois révélateurs).
- **Following / Followers** : l’analyse du réseau peut révéler une coordination (Ch.28).
- **Spaces** (audio) : participation à des Spaces — moins archivés, à capturer en direct si possible.

#### 7.6 TikTok

TikTok est sous-investigué relativement à son volume d’usage. Ressource croissante, particulièrement pour les profils jeunes et pour l’observation de tendances.

**Recherche** : recherche par username ou hashtag dans l’app/web. Pas d’API publique gratuite sérieuse.

**Sources** :

- **Profil** : bio, lien, métriques.
- **Vidéos** : contenu, son utilisé, hashtags, géolocalisation parfois explicite.
- **Lives** : à capturer en direct (yt-dlp supporte les lives TikTok).
- **Sounds utilisés** : le son d’une vidéo peut révéler sa source originale et ses utilisations sur d’autres comptes.

**Géolocalisation dans les vidéos** : TikTok ne géolocalise pas explicitement les vidéos par défaut, mais les utilisateurs ajoutent souvent des localisations dans la légende ou dans le contenu visuel (lieux identifiables — méthodologie Bellingcat applicable, voir Ch.15).

#### 7.7 Reddit

Reddit reste une source précieuse pour le contenu thématique, les communautés spécialisées, et certains témoignages (subreddits comme r/legaladvice, r/personalfinance révèlent des situations personnelles concrètes).

**Recherche** :

- Reddit search interne (limité).
- Google dorks `site:reddit.com "username"` ou `site:reddit.com "sujet"`.
- **Reveddit** (`reveddit.com`) : permet de voir les posts et commentaires supprimés ou modifiés par l’utilisateur — précieux pour les investigations.
- **Pushshift** était l’API historique, devenue restreinte en 2023. Des alternatives existent (Arctic Shift, GDELT-like) avec couverture variable.

**Sources** :

- **Historique utilisateur** : tous les posts et commentaires d’un compte, organisables par subreddit, par date, par karma.
- **Subreddits fréquentés** : révèle les centres d’intérêt, parfois la profession (un actif sur r/sysadmin est probablement administrateur système), parfois la géographie (r/paris, r/france).

#### 7.8 Faux positifs SOCMINT et limites des informations auto-déclarées

Trois pièges majeurs caractérisent l’OSINT sur réseaux sociaux.

**Comptes inactifs ou abandonnés** : un profil Facebook créé en 2012, avec dernière activité en 2014, peut être un ancien compte abandonné — ce n’est pas le « profil actif » de la cible. La conclusion « la cible n’a pas de présence Facebook » peut être fausse si on a oublié de chercher d’autres comptes plus récents.

**Comptes parodiques, fan accounts, sosies** : un compte Instagram « marc_delaunay_real » avec la même photo n’est pas nécessairement la cible — c’est peut-être un fan, un parodiste, un usurpateur. La vérification croisée est obligatoire.

**Informations auto-déclarées** : un profil LinkedIn qui déclare un poste de DAF chez TechnoVert n’est pas une preuve que la personne occupe réellement ce poste. La vérification par d’autres sources (mention dans un communiqué officiel TechnoVert, Pappers si la personne est dirigeant déclaré, presse) est nécessaire pour confirmer.

**Limite fondamentale** : les réseaux sociaux montrent **ce que les gens veulent montrer**. L’absence d’information sur un réseau social ne signifie pas l’absence de l’activité. Une personne peut mener une activité importante hors ligne ou sur des canaux privés sans que rien n’apparaisse en SOCMINT. Le rapport doit distinguer « pas de signal observable » (constat) de « pas d’activité » (conclusion non justifiée).

-----

### Chapitre 8 — Telegram : architecture, usages et méthodologie d’investigation

#### 8.1 Pourquoi Telegram concentre tant d’activité

Telegram a connu une croissance spectaculaire en quelques années (plus de 900 millions d’utilisateurs actifs en 2024) et est devenu une plateforme d’investigation incontournable. La plateforme combine plusieurs caractéristiques qui en font un terrain à la fois riche et complexe.

D’un côté, Telegram offre des canaux de **diffusion de masse** (jusqu’à plusieurs millions d’abonnés sur certains canaux) et des **groupes** très volumineux (jusqu’à 200 000 membres). Cette capacité a attiré les médias, les communautés professionnelles, les communautés militantes, mais aussi les acteurs de la criminalité organisée, du terrorisme, de la fraude, et du commerce illicite. Beaucoup d’activités qui se déroulaient sur le dark web il y a cinq ans ont migré vers Telegram, plus accessible et avec une audience plus large.

De l’autre, Telegram a longtemps cultivé une réputation de **résistance aux demandes des autorités**. Cette réputation a été partiellement remise en cause par l’arrestation de Pavel Durov en France en août 2024, qui a conduit la plateforme à modifier sa politique de coopération. Les modérations se sont intensifiées en 2024-2025, mais l’écosystème reste largement opérationnel pour les usages clandestins.

Pour l’investigateur, Telegram est à la fois une mine d’or (volume d’activité, granularité des canaux thématiques) et un terrain piégé (présence d’acteurs malveillants, contenus parfois illégaux qui peuvent compromettre l’investigateur s’ils sont téléchargés).

#### 8.2 Architecture : canaux, groupes, supergroupes, bots, secret chats

Comprendre l’architecture de Telegram est indispensable pour savoir ce qu’on peut et ce qu’on ne peut pas observer.

Les **canaux** (channels) sont des outils de diffusion unidirectionnelle. Un administrateur publie, des abonnés lisent. Les commentaires sont possibles si l’admin les active (via un groupe lié). Les canaux peuvent être **publics** (recherchables, accessibles sans invitation, avec un username `@nom_canal`) ou **privés** (accessibles uniquement par lien d’invitation).

Les **groupes** sont des conversations multi-utilisateurs jusqu’à 200 000 membres. Ils peuvent également être publics ou privés. Les **supergroupes** sont des groupes qui ont basculé en mode étendu (au-delà de 200 membres) avec des fonctionnalités d’administration avancées.

Les **bots** sont des comptes automatisés contrôlés par des scripts. Ils sont omniprésents sur Telegram : bots de modération, bots utilitaires, bots de jeux, bots OSINT (qui peuvent renseigner sur un username, un numéro). Les bots sont aussi utilisés par les groupes criminels pour automatiser des ventes, des arnaques, et de la diffusion.

Les **secret chats** sont des conversations chiffrées de bout en bout entre deux utilisateurs, sans backup serveur. Inaccessibles à l’investigation OSINT (et à Telegram lui-même).

Les **messages classiques** (chats normaux, groupes, canaux) ne sont **pas** chiffrés de bout en bout — ils sont stockés sur les serveurs Telegram, accessibles à Telegram et théoriquement accessibles aux autorités sur réquisition. Cette nuance est centrale : Telegram n’est pas Signal.

#### 8.3 Recherche : interne, dorks, outils

**Recherche interne Telegram** : depuis le client, la barre de recherche permet de chercher des canaux et des groupes publics. Couverture incomplète et résultats parfois biaisés.

**Google dorks** : `site:t.me "mot-clé"` est efficace. Telegram expose les canaux publics via des pages web `t.me/nom_canal` qui sont indexées par Google. Ces pages contiennent souvent les derniers messages publics, ce qui permet une consultation initiale sans même rejoindre le canal.

**Outils tiers** :

- **TGStat** (`tgstat.com`) : annuaire et statistiques de canaux Telegram. Recherche par mot-clé, par catégorie, par langue. Donne le nombre d’abonnés, l’activité, le profil de l’audience. Indispensable pour le ciblage de canaux.
- **Telemetrio** : équivalent, avec parfois une couverture différente.
- **Telepathy** (open source) : outil OSINT qui collecte les messages, les membres (quand visibles), les métadonnées d’un canal ou groupe public. Nécessite une session Telegram authentifiée — utiliser le compte d’investigation.
- **Tdscan**, **TGDev** : outils complémentaires pour l’analyse de canaux.

**Méthode** : commencer par TGStat pour identifier les canaux pertinents sur un sujet ou une géographie, consulter via les pages `t.me/` pour les snippets publics, rejoindre avec l’avatar Telegram dédié pour l’observation continue.

#### 8.4 Investigation des administrateurs et des membres

Les administrateurs et les membres d’un canal/groupe sont des cibles d’investigation classiques. Plusieurs sources d’information.

**Visibilité directe** : dans un canal public, les administrateurs sont parfois visibles avec leur username. Dans un groupe public, la liste des membres peut être visible (selon les paramètres de confidentialité du groupe). Le compte d’investigation rejoint le groupe et peut consulter la liste.

**Bots OSINT** :

- **@SangMata_bot** : historique des changements de nom et de username d’un utilisateur (très révélateur — un utilisateur qui a changé 5 fois de pseudo en 2 ans signale soit une OPSEC active, soit une volonté de masquer un passé).
- **@getcontact_bot** (variantes) : tente de récupérer le nom associé à un numéro de téléphone via des bases crowdsourcées.
- **@username_to_id_bot** : convertit un username en ID Telegram numérique stable (utile car l’username peut changer mais l’ID reste).

**Limites des bots** : ils sont **instables**. Telegram bloque régulièrement les bots OSINT, qui réapparaissent sous d’autres noms. La maintenance dépend de communautés bénévoles. Un bot fonctionnel aujourd’hui peut être hors ligne demain.

**Numéros de téléphone des admins** : visibles uniquement si la confidentialité n’est pas configurée correctement par l’utilisateur. De plus en plus d’admins masquent leur numéro. Quand le numéro est visible, c’est un pivot massif (Ch.6.5).

#### 8.5 Le forwarding comme révélateur de réseau de canaux

Le **forwarding** (transfert) d’un message d’un canal à un autre laisse une trace : le message forwardé porte la mention « Forwarded from [canal d’origine] ». Cette trace permet de cartographier les **réseaux de canaux** liés.

Quand un canal X forwarde régulièrement des messages d’un canal Y, deux hypothèses :

- Les deux canaux sont gérés par le même opérateur (réseau coordonné de diffusion).
- Le canal X amplifie le canal Y (relation de promotion mutuelle ou unidirectionnelle).

Le mapping des forwardings dans un écosystème de canaux (par exemple : canaux d’extrême droite, canaux de désinformation pro-russe, canaux de carding) révèle la structure du réseau, identifie les canaux pivots (qui forwardent et sont forwardés massivement), et permet d’attribuer des opérateurs aux canaux satellites.

Outils : Telepathy peut extraire les statistiques de forwarding d’un canal. Une analyse manuelle reste souvent nécessaire pour les graphes complexes.

#### 8.6 Canaux clandestins : observation vs interaction

Les canaux clandestins couvrent un spectre large : vente de données volées, carding, vente de drogues, trafic d’armes, contrefaçon, distribution de malware, contenus extrémistes, contenus pédopornographiques.

**L’observation est légale** dans la plupart des juridictions, à condition de respecter quelques précautions : ne pas télécharger les contenus illégaux (les samples de données volées, les photos sensibles, les contenus pédopornographiques — la simple détention peut être pénalement réprimée), ne pas interagir activement (acheter, négocier, publier), documenter scrupuleusement la consultation.

**L’interaction est très risquée** pour un investigateur privé. Acheter un sample de données « pour vérifier » peut constituer un recel de données obtenues frauduleusement. Négocier avec un vendeur peut être qualifié de complicité. Les LEA peuvent légalement faire des achats contrôlés ; un investigateur privé ne peut pas.

**Précautions opérationnelles** :

- VM dédiée, idéalement Whonix ou Tails.
- Compte Telegram dédié à l’observation clandestine, jamais utilisé pour autre chose.
- Pas de téléchargement de fichiers, sauf preuves clairement légales (captures d’écran d’annonces, exports textuels de discussions).
- En cas de découverte de contenus pédopornographiques : signalement immédiat à Pharos (France) ou NCMEC (international), et arrêt immédiat de la consultation de la source concernée.

#### 8.7 OPSEC spécifique à Telegram

Telegram exige des précautions OPSEC particulières.

**Compte dédié** : l’investigation Telegram se fait depuis un compte créé spécifiquement pour cette mission, avec un numéro burner (SIM prépayée, SMS-Activate, ou eSIM voyage). Jamais le compte personnel de l’investigateur.

**Confidentialité maximale** : dans les paramètres du compte d’investigation : numéro de téléphone visible uniquement par les contacts (ou personne), photo de profil visible par tous mais photo générique, statut « Last seen » désactivé, qui peut me trouver par numéro = personne, qui peut m’ajouter à des groupes = mes contacts uniquement.

**Pas de listes de contacts importées** : si l’investigateur importe son carnet de contacts personnel sur le téléphone d’investigation, Telegram va corréler son numéro avec des contacts personnels qui ont son numéro dans leur carnet. Catastrophe d’OPSEC. Carnet d’adresses vide impératif sur le téléphone d’investigation.

**Comportement passif** : observer, lire, capturer. Ne pas réagir, ne pas commenter, ne pas envoyer de messages directs. Chaque interaction laisse une trace et peut révéler la présence de l’investigateur.

#### 8.8 Garde-fous juridiques

Trois zones juridiques distinctes structurent l’investigation Telegram.

**Zone verte (légale)** : consultation de canaux et groupes publics, capture de contenu visible sans authentification supplémentaire, observation des messages et de leurs métadonnées (forwarding, dates, comptes émetteurs).

**Zone grise** : rejoindre un groupe privé via un lien d’invitation publié publiquement (techniquement légal, mais peut être contesté si le groupe a des contenus illicites), utiliser un avatar pour observer un groupe (légal en observation, devient problématique si l’avatar est utilisé pour des interactions trompeuses).

**Zone rouge (illégale ou à très haut risque)** : télécharger des contenus illicites (données personnelles volées, contenus pédopornographiques, copies d’œuvres protégées), interagir activement avec un vendeur clandestin (achat, négociation), s’introduire dans un groupe par usurpation d’identité réelle.

L’investigateur professionnel reste en zone verte, occasionnellement en zone grise avec justification documentée, jamais en zone rouge.

#### 8.9 Fil rouge — MIRAGE Épisode 5

> **🎯 MIRAGE — Épisode 5 : le canal Telegram « Offshore Trading Club »**
> 
> L’investigateur cherche la présence Telegram de Marc Delaunay. Le username `marc_del75` testé sur Telegram via le compte d’investigation : pas de compte direct trouvé.
> 
> Recherche de canaux liés à l’offshore et à l’optimisation fiscale via TGStat : `offshore`, `Malta company`, `crypto tax`. Plusieurs résultats. L’un attire l’attention : un canal privé « Offshore Trading Club » (560 membres), invitation visible sur un site spécialisé (publication publique → rejoindre est en zone grise acceptable).
> 
> Le compte d’investigation rejoint le canal. Les messages sont visibles. L’administrateur principal a pour username `marc_offshore` — variation potentielle de `marc_del75`. Sa photo de profil ressemble à celle de Delaunay (cotation D3 — vérification via PimEyes : correspondance probable mais pas certitude).
> 
> **@SangMata_bot** sur le username `marc_offshore` : historique de noms et usernames. Le compte a porté successivement les usernames `mdelMT`, `marc_del`, `marc_offshore` — cohérence avec l’identité Delaunay.
> 
> Le numéro de l’admin n’est pas visible (confidentialité activée). Cependant, en croisant avec le **dump Facebook 2021** (Ch.6.5), un numéro associé à `marcdelaunay75@gmail.com` est trouvé. Test : ajouter ce numéro aux contacts du téléphone d’investigation. WhatsApp affiche un compte avec une photo de profil — la même que sur Telegram `marc_offshore`. **Cohérence multi-plateformes établie**.
> 
> Les messages du canal portent sur des **techniques d’optimisation fiscale internationale** : sociétés écrans, structures Malte/Chypre, conversion en crypto. Plusieurs messages de Delaunay (en tant qu’admin) répondent à des questions techniques avec une compétence professionnelle évidente. Cohérent avec un DAF qui pratique ces techniques pour son propre compte ou pour conseiller.
> 
> **Forwarding** : le canal forwarde régulièrement des messages d’un autre canal, « Crypto Tax Free » (1 200 membres). Le réseau s’étend.
> 
> **Sélecteurs ajoutés au graphe** : 1 canal Telegram (560 membres), 1 canal lié par forwarding (1 200 membres), 3 anciens usernames Telegram (cohérence longitudinale), 1 numéro confirmé multi-plateformes.

-----

### Chapitre 9 — Discord, forums et plateformes alternatives

#### 9.1 Distinction des espaces

Ce chapitre couvre les **espaces communautaires alternatifs** — par opposition aux grandes plateformes occidentales (Ch.7) et à Telegram (Ch.8). Trois familles structurent ce paysage :

- Les **espaces communautaires temps réel** (Discord, Matrix) : structurés en serveurs/salons, équivalents fonctionnels de Telegram avec une culture différente (gaming, crypto, communautés tech).
- Les **forums classiques** (vBulletin, phpBB, Discourse, Reddit-like) : structurés en threads et catégories, archivage long, indexation Google généralement bonne.
- Les **plateformes émergentes** (Bluesky, Mastodon, Threads, Truth Social) : alternatives ou compléments aux grands réseaux sociaux occidentaux, avec des dynamiques propres.

La méthodologie SOCMINT (Ch.7.1) reste applicable, mais chaque famille a ses spécificités d’accès, d’OPSEC et d’extraction.

#### 9.2 Discord

Discord est devenu une plateforme centrale pour les communautés tech, gaming, crypto, mais aussi pour certaines communautés extrémistes et pour le commerce de contenus illicites. C’est l’un des espaces les plus négligés par l’OSINT mainstream alors qu’il concentre des conversations très révélatrices.

**Architecture** : un serveur Discord est une organisation structurée en salons (channels — texte, voix, vidéo). Chaque salon peut être public ou réservé à des rôles spécifiques. Un serveur peut être public (recherchable, ouvert) ou privé (accessible uniquement par invitation).

**Recherche de serveurs** :

- **Disboard** (`disboard.org`) : annuaire public de serveurs Discord, recherche par tag.
- **Discadia** (`discadia.com`) : équivalent.
- **DiscordServers** : autres annuaires.
- Recherche Google `site:discord.com OR site:disboard.org "mot-clé"`.

**Recherche dans un serveur** : la recherche interne Discord est efficace, mais nécessite d’être membre du serveur. Une fois membre, on peut chercher par auteur, par mot-clé, par date, par salon.

**Outils de scrap** : le scraping Discord est complexe (anti-bot, terms of service stricts). Des outils comme **DiscordChatExporter** (open source) permettent d’exporter l’historique d’un salon où on est membre, en JSON ou HTML. À utiliser avec précaution OPSEC (l’export est lourd et peut être détecté).

**Sources** :

- **Profil utilisateur** : nom, discriminator (#1234, en cours de remplacement par le username unique), photo, bio, statut.
- **Messages** : contenu textuel, fichiers partagés, liens, réactions.
- **Voice channels** : difficiles à investiguer (audio temps réel, pas d’archivage natif).
- **Roles** : les rôles attribués révèlent la position dans la communauté (admin, modérateur, contributeur ancien).

**OPSEC** : compte d’investigation Discord dédié (création avec email burner). Pas de profil personnel. Comportement passif strict.

#### 9.3 Forums classiques

Malgré la domination des réseaux sociaux, les **forums** restent vivaces dans certains domaines : communautés techniques (Stack Overflow et équivalents), communautés thématiques (auto, voile, montres, photo), communautés professionnelles (avocats, médecins, ingénieurs), communautés clandestines (carding, hacking, certains forums dark web ont leur équivalent clearnet).

**Recherche** : Google dorks `site:forum.com "username"` ou `site:forum.com "sujet"`. La majorité des forums sont bien indexés. Les forums fermés (registration required) sont semi-accessibles : les pages publiques (extraits, métadonnées de threads) sont indexées, le contenu complet nécessite un compte.

**Sources** :

- **Profil utilisateur** : pseudonyme, date d’inscription, nombre de messages, signature (souvent révélatrice — site personnel, profession, localisation).
- **Historique de posts** : tous les messages publiés, organisables par date, par catégorie. Une mine d’or pour comprendre les centres d’intérêt et l’expertise d’une personne.
- **Threads créés** : les sujets initiés révèlent les préoccupations propres.
- **Profil des modérateurs et anciens** : la hiérarchie d’un forum révèle qui structure la communauté.

**Forums spécialisés à connaître** :

- **France** : Hardware.fr, Doctissimo (santé), Au Féminin, JeuxVidéo.com, forums automobiles spécifiques (BMW, Porsche, etc.).
- **International** : XDA Developers (mobile/Android), Reddit (transversal), Hacker News (tech/startup), Stack Exchange (Q&R techniques).
- **Communautés crypto** : BitcoinTalk (forum historique du Bitcoin), CryptoCompare forums.
- **Forums sensibles** : forums de carding, hacking, leak — typiquement sur le dark web (Ch.13) mais avec des doublons clearnet.

#### 9.4 Plateformes russophones : VK, OK.ru

Pour toute investigation impliquant la sphère post-soviétique, les plateformes russophones sont indispensables.

**VK (VKontakte)** est l’équivalent russe de Facebook, dominant en Russie, Ukraine, Biélorussie, Kazakhstan. Plus de 100 millions d’utilisateurs actifs. La culture VK est plus permissive que Facebook : profils souvent moins verrouillés, photos massives, listes d’amis fréquemment publiques.

**Recherche VK** : recherche interne (nécessite un compte d’investigation VK), Google dorks `site:vk.com "name"`, **Search4Faces** pour la reconnaissance faciale spécialisée VK/OK.

**OK.ru (Odnoklassniki)** est l’autre grand réseau russophone, plus vieillissant démographiquement. Contenu similaire, méthodologie analogue.

**Méthodologie spécifique** : translittération obligatoire des noms (de l’alphabet latin au cyrillique — Yandex Translate, ou expert humain pour les noms ambigus), traduction du contenu (DeepL est meilleur que Google sur le russe), consultation via VPN ne sortant pas en Russie (en raison des sanctions et restrictions actuelles, les services russes sont parfois inaccessibles depuis l’UE).

#### 9.5 Plateformes asiatiques

L’investigation sur la sphère asiatique exige de connaître les plateformes locales, qui sont souvent plus utilisées que leurs équivalents occidentaux.

**Chine** : **Weibo** (équivalent Twitter/Facebook hybride), **WeChat** (messagerie+réseau social, ultra-dominante mais très fermée à l’investigation), **Douyin** (TikTok chinois — différent de TikTok international), **Xiaohongshu / RedNote** (lifestyle), **Zhihu** (Q&R type Quora).

**Corée du Sud** : **KakaoTalk** (messagerie dominante), **Naver Cafés** (forums communautaires), **Daum** (portail).

**Japon** : **LINE** (messagerie), **Mixi** (réseau social en déclin), **2chan/5chan** (forums anonymes — équivalents historiques de 4chan occidental, source d’investigation extrémisme).

**Asie du Sud-Est** : **LINE** (Thaïlande, Taiwan), **Zalo** (Vietnam), **WhatsApp** (Inde, Indonésie — usage massif).

**Méthodologie** : ces plateformes nécessitent souvent un numéro de téléphone du pays (limitant l’inscription), des compétences linguistiques ou un partenariat local, et un VPN configuré en sortie dans le pays cible. Pour les investigations professionnelles sérieuses sur ces sphères, faire appel à un investigateur local est souvent plus efficace que de tenter une investigation à distance.

#### 9.6 Plateformes émergentes : Bluesky, Mastodon, Threads, Truth Social

L’écosystème post-Twitter a vu émerger plusieurs alternatives qui captent désormais une fraction non négligeable des conversations publiques.

**Bluesky** : créé par les fondateurs originaux de Twitter, basé sur un protocole décentralisé (AT Protocol). Croissance rapide depuis fin 2024. API ouverte, recherche relativement facile, communauté tech/journalistique surreprésentée.

**Mastodon** : fédération d’instances indépendantes (federverse, ActivityPub). Pas de moteur de recherche centralisé efficace, recherche par instance (`mastodon.social`, `mas.to`, etc.). Communauté hétérogène, présence forte de communautés tech et de migrants ex-Twitter.

**Threads** (Meta) : connecté à Instagram, croissance soutenue. Recherche limitée, API restreinte. Investigation similaire à Instagram (Ch.7.3) avec pivot Threads ↔ Instagram souvent productif.

**Truth Social** : plateforme conservatrice américaine. Monitorée intensivement par certains acteurs OSINT pour le suivi de l’écosystème politique américain.

**Méthodologie** : ces plateformes restent marginales dans la plupart des investigations grand public, mais elles peuvent être centrales dans les investigations sur des communautés spécifiques (tech transitionnée vers Bluesky, communautés conservatrices vers Truth Social). La méthodologie SOCMINT générale s’applique, avec des outils dédiés en développement (le paysage évolue chaque mois).

#### 9.7 Pastebins et leak sites

Les **pastebins** sont des services de partage de texte en ligne, souvent utilisés pour partager du code, des notes, mais aussi des données sensibles (credentials, doxing, données volées).

**Plateformes principales** :

- **Pastebin.com** : le plus connu, modération active mais pas immédiate.
- **GhostBin** : pastebin alternatif.
- **Paste.ee, dpaste.com, hastebin** : alternatives techniques.
- **Doxbin** : spécialisé dans le doxing (publication de données personnelles à des fins malveillantes).

**Recherche** : la majorité des pastebins ne sont pas indexés par Google (par paramétrage des opérateurs). La recherche se fait via :

- **IntelX** (`intelx.io`) : indexe massivement les pastebins, fournit une interface de recherche par mot-clé, email, domaine.
- **Pastesearch** : équivalent.
- **Monitoring** par alertes (mots-clés sensibles surveillés en temps réel).

Les données des pastebins peuvent être volatiles (suppression rapide après détection) — l’archivage immédiat est crucial.

#### 9.8 Plateformes de partage de contenu

Plusieurs plateformes hébergent des contenus qui peuvent être pertinents en investigation : documents, articles, images, vidéos.

**Telegraph** (lié à Telegram) : permet de publier des articles longs anonymement. Souvent utilisé pour des publications anonymes, des manifestes, des doxs détaillés. Indexé partiellement par Google (`site:telegra.ph`).

**Notion publié** : pages Notion rendues publiques par leur auteur. Souvent utilisées pour des wikis communautaires, des pages perso, parfois des documents internes oubliés. Recherche via `site:notion.site` ou `site:notion.so`.

**Google Docs publics** : documents Google rendus accessibles publiquement (souvent par erreur). `site:docs.google.com` ou recherche d’extension via dorks.

**SlideShare, Scribd, ISSUU** : plateformes de partage de documents. Beaucoup de présentations professionnelles et de rapports y sont hébergés.

Ces plateformes sont des compléments réguliers de l’investigation OSINT, à ne pas négliger lors des recherches initiales.

-----

## PARTIE III — INVESTIGATION CORPORATE, INFRASTRUCTURE ET DONNÉES EXPOSÉES

> **Ce que cette partie apprend.** Investiguer une société (registres légaux, UBO, structures juridiques opaques), exploiter l’infrastructure technique exposée (DNS, certificats, IP, ports), exploiter les données fuitées (breaches), et naviguer sur le dark web pour l’investigation.
> 
> **Ce qu’elle ne couvre pas.** L’analyse comptable détaillée (plutôt en Partie V), la conduite d’opérations sous couverture sur le dark web (réservé aux LEA, hors périmètre).
> 
> **Ce que vous saurez faire après cette partie.** Identifier le bénéficiaire effectif d’une société et cartographier ses structures, pivoter d’un domaine vers son infrastructure et inversement, exploiter une fuite de données dans une investigation, et investiguer le dark web sans compromettre l’OPSEC ni franchir de ligne juridique.

-----

### Chapitre 10 — Investigation corporate : sociétés, UBO et structures juridiques

#### 10.1 Pourquoi commencer par la société

Dans une investigation à dimension financière ou patrimoniale, commencer par l’individu et essayer de remonter aux structures qu’il contrôle est généralement moins efficace que l’inverse : commencer par les structures suspectées et remonter aux personnes qui les contrôlent.

La raison est structurelle. Les **registres d’entreprises sont publics et bien tenus** dans la majorité des juridictions occidentales. Ils contiennent des données fiables (cotation A1) sur les dirigeants, les associés, le capital, les comptes annuels, les modifications. Une investigation qui part d’une société identifie rapidement les personnes en position de contrôle, leurs autres mandats, et les liens entre structures.

À l’inverse, **partir d’un individu** pour découvrir ses structures suppose de connaître son nom et de chercher dans des bases qui ne sont pas toujours indexées par personne. Un dirigeant peut être listé dans des registres étrangers que son nom ne suffira pas à identifier sans connaître la juridiction.

En pratique, les investigations combinent les deux approches en parallèle. La recherche par société alimente la recherche par personne et inversement. Le fil rouge MIRAGE illustre cette dynamique : nom de Delaunay → identification d’une société (Delta Consulting) → identification de dirigeants apparents → identification d’autres sociétés liées → retour à Delaunay comme bénéficiaire effectif probable.

#### 10.2 Registres par juridiction

Chaque juridiction a son régime de publicité légale des sociétés. La connaissance des registres principaux est indispensable à l’investigateur OSINT financier.

**France** :

- **Pappers** (`pappers.fr`) : interface moderne agrégeant les données de l’Infogreffe, du BODACC, des comptes annuels. Gratuit pour la consultation de base, payant pour les exports massifs et les API. C’est l’outil de premier recours pour la France.
- **Infogreffe** (`infogreffe.fr`) : registre officiel, plus complet sur les actes et statuts mais interface vieillissante.
- **BODACC** (`bodacc.fr`) : Bulletin Officiel des Annonces Civiles et Commerciales — créations, modifications, dissolutions de sociétés, liquidations judiciaires.
- **Data.gouv.fr** : exports massifs des données SIRENE, registre national des entreprises.

**Royaume-Uni** :

- **Companies House** (`gov.uk/government/organisations/companies-house`) : registre national, intégralement gratuit et exhaustif. Interface excellente, données structurées, exports possibles. Référence mondiale en matière de transparence corporate.
- Accès public aux **People with Significant Control** (PSC) : registre des UBO obligatoire depuis 2016, libre d’accès.

**États-Unis** :

- Pas de registre fédéral unique. Chaque **État** gère son propre registre (Secretary of State du Delaware, du Nevada, du Wyoming, etc.). Le Delaware est le plus utilisé pour les sociétés (incluant des LLC opaques). OpenCorporates agrège.
- **SEC EDGAR** (`sec.gov/edgar`) : pour les sociétés cotées — déclarations 10-K (rapport annuel), 10-Q (trimestriel), 8-K (événements majeurs), proxy statements (rémunération des dirigeants, structure du capital).

**Allemagne** : **Handelsregister** (registre du commerce), **Bundesanzeiger** (publications légales). Accès partiellement payant mais essentiel pour les sociétés allemandes.

**Suisse** : **Zefix** (`zefix.ch`) — registre fédéral, gratuit. **Moneyhouse** (`moneyhouse.ch`) — agrégateur enrichi, payant après quelques recherches.

**Autres juridictions courantes** :

- **Belgique** : Banque-Carrefour des Entreprises (BCE).
- **Pays-Bas** : Kamer van Koophandel (KvK).
- **Espagne** : Registro Mercantil Central.
- **Italie** : Registro Imprese.
- **Luxembourg** : RCS et RCB.

**Agrégateurs internationaux** :

- **OpenCorporates** (`opencorporates.com`) : agrège plus de 200 millions de sociétés dans 140 juridictions. Gratuit pour la consultation, API payante. C’est l’outil de référence pour l’investigation internationale.
- **Orbis (Bureau van Dijk)** : payant, exhaustif, interface professionnelle. Utilisé par les services de compliance et les services d’enquête.

#### 10.3 Lecture d’un registre : K-bis, BODACC, rapport annuel

L’investigateur doit savoir lire les documents légaux qu’il consulte. Trois documents clés en France.

**Le K-bis** (extrait Kbis) est la « carte d’identité » d’une société française. Il contient : raison sociale, forme juridique, capital social, adresse du siège, numéro RCS, code APE/NAF, date d’immatriculation, dirigeant(s) actuel(s), nom du commissaire aux comptes le cas échéant, mentions des procédures collectives en cours. Un K-bis daté de moins de trois mois est la pièce de référence pour vérifier l’existence légale d’une société.

**Le BODACC** publie chaque mouvement légal : création, modification statutaire (changement de dirigeant, d’objet, de capital, de siège), cession de fonds de commerce, dépôt des comptes, procédures collectives. La consultation chronologique du BODACC pour une société révèle son histoire.

**Les comptes annuels** (déposés au greffe et publiés sur Infogreffe ou Pappers) contiennent : bilan, compte de résultat, annexe. Pour l’investigateur, les éléments à scruter sont : l’évolution du chiffre d’affaires (incohérences ?), les charges externes (postes anormaux ?), les comptes courants d’associés (entrées/sorties révélant des flux), le résultat (négatif sur plusieurs exercices = signal), la trésorerie. Une PME qui réalise un chiffre d’affaires spectaculaire avec un résultat constamment proche de zéro et des charges de « consulting » significatives à des sociétés liées présente un profil suspect.

**Le rapport annuel** (pour les sociétés cotées ou les grandes sociétés) ajoute le rapport de gestion, les notes sur les risques, les conventions réglementées (transactions avec des parties liées — souvent révélatrices de conflits d’intérêts).

#### 10.4 Identification du UBO

L’**UBO** (Ultimate Beneficial Owner) est la personne physique qui contrôle effectivement une société, indépendamment de la chaîne de structures intermédiaires. C’est le **vrai propriétaire**, par opposition au propriétaire apparent (qui peut être un nominee, une autre société, une fiducie).

L’identification du UBO est l’enjeu central de la lutte contre le blanchiment et de la due diligence. C’est aussi l’objectif principal de beaucoup d’investigations OSINT financières.

**Sources d’identification du UBO** :

**Déclarations légales** : depuis la 4e directive anti-blanchiment de l’UE (2015), les sociétés européennes doivent déclarer leur UBO dans des registres dédiés. En France, le **Registre des Bénéficiaires Effectifs** (RBE) est tenu par le greffe et accessible via Infogreffe (l’accès public a été restreint en novembre 2022 suite à un arrêt de la CJUE — il est désormais réservé aux personnes ayant un intérêt légitime, dont les services compétents et les acteurs financiers assujettis). Au Royaume-Uni, le PSC register est resté entièrement public.

**Cascade de participations** : remonter manuellement la chaîne de holdings. Société A est détenue à 100 % par Société B, qui est détenue à 80 % par Société C, qui est détenue à 60 % par Personne X. Personne X est l’UBO.

**Nominees** : un dirigeant ou actionnaire « nominee » apparaît dans les registres mais détient pour le compte d’un tiers. Les nominees sont fréquents dans les juridictions opaques (BVI, Caïmans, Panama). Les indices d’un nominee : individu qui apparaît dans des dizaines de sociétés sans logique apparente, professions de services (avocat local, comptable local), résidence dans la juridiction du registre.

**Structures écrans** : sociétés sans activité économique réelle, créées pour interposer une couche entre le bénéficiaire réel et l’activité. Indices : capital symbolique, adresse de domiciliation partagée par des dizaines d’entités, absence d’employés, absence de présence physique.

#### 10.5 Juridictions opaques et leaks ICIJ

Certaines juridictions sont historiquement utilisées pour l’opacité des structures de propriété. La connaissance de ces juridictions est indispensable pour l’investigateur.

**Juridictions opaques classiques** : British Virgin Islands (BVI), Cayman Islands, Bahamas, Panama, Seychelles, Belize. Ces juridictions ont historiquement permis l’enregistrement de sociétés sans publicité du UBO, avec nominees, et avec une coopération limitée avec les enquêtes étrangères.

**Juridictions « grises »** : Malte, Chypre, Luxembourg, Île Maurice, Hong Kong, Dubaï (UAE), Singapour. Ces juridictions ont une transparence intermédiaire — registres souvent publics mais avec des structures (trusts, foundations) qui restent opaques.

**Évolution récente** : sous la pression internationale (FATF, OCDE, sanctions UE), la majorité de ces juridictions ont amélioré leur transparence formelle. Les BVI ont mis en place un registre de UBO accessible aux autorités. Le Luxembourg a un registre RBE public. Mais la coopération réelle reste très variable, et beaucoup de structures historiques ne sont pas rétroactivement transparentes.

**Les leaks ICIJ** ont massivement enrichi l’investigation sur ces juridictions :

- **Panama Papers** (2016) : 11,5 millions de documents du cabinet Mossack Fonseca (Panama).
- **Paradise Papers** (2017) : Appleby (Bermudes) et Asiaciti Trust (Singapour).
- **Pandora Papers** (2021) : 14 cabinets de plusieurs juridictions, 11,9 millions de documents.
- **Suisse Secrets** (2022) : Credit Suisse.
- **FinCEN Files** (2020) : SARs (déclarations de soupçon) américaines fuitées.

L’**ICIJ Offshore Leaks Database** (`offshoreleaks.icij.org`) est une base consultable gratuitement qui agrège les principales données de tous ces leaks. Recherche par nom de personne, de société, ou d’adresse. Pour l’investigation OSINT financière internationale, c’est une ressource essentielle.

#### 10.6 Red flags structurels

Plusieurs caractéristiques structurelles d’une société alertent l’investigateur sur un risque accru de structure écran ou de fraude.

**Capital symbolique** : société à 1 € de capital réalisant un chiffre d’affaires important — incohérence financière, signal de structure de façade.

**Adresse de domiciliation partagée massivement** : si 50 ou 500 sociétés sont domiciliées à la même adresse, c’est probablement une **company formation agent** (cabinet qui crée et héberge des sociétés). Ce n’est pas illégal en soi mais c’est un indicateur de structure d’opacité. Outils : recherche de l’adresse dans OpenCorporates ou Pappers.

**Dirigeant nominee** : un individu listé comme dirigeant de dizaines de sociétés sans lien apparent entre elles est probablement un nominee professionnel.

**Absence de présence physique** : pas de site web, pas de téléphone, pas d’employés identifiables sur LinkedIn. Société qui n’existe que dans les registres.

**Activité incohérente avec le capital ou l’effectif** : société à 2 employés réalisant 50 millions de chiffre d’affaires en « consulting » est suspecte (sauf cas légitimes — un consultant senior peut facturer des honoraires importants).

**Modifications statutaires fréquentes** : changements de dirigeant, de siège, d’objet social tous les 6 mois. Signal d’agitation suspecte ou de tentative de brouillage.

**Mentions au BODACC anormales** : multiples cessions de fonds, multiples procédures collectives, transferts précipités — signaux d’historique trouble.

#### 10.7 Investigation des dirigeants

Une fois une société identifiée, l’investigation pivote vers ses dirigeants. Cette étape multiplie les pivots vers d’autres entités.

**Mandats croisés** : un dirigeant qui apparaît dans plusieurs sociétés trace un réseau de relations. Pappers permet de chercher par nom de dirigeant et liste tous ses mandats actifs et passés en France. OpenCorporates étend à l’international.

**Conflits d’intérêts** : un DAF qui dirige par ailleurs une société de « consulting » qui facture sa propre entreprise est en conflit d’intérêts manifeste. La détection passe par le croisement systématique des mandats avec les noms des fournisseurs.

**Sanctions et listes** : screening contre les listes de personnes sanctionnées (OFAC SDN, listes UE, ONU). Outils gratuits : OpenSanctions (`opensanctions.org`), Sanctions Search de l’OFAC.

**PEP** (Politically Exposed Persons) : dirigeants politiques, hauts fonctionnaires, leurs familles et leurs proches. Bases payantes (WorldCheck, LexisNexis Bridger) ou ressources gratuites limitées (OpenSanctions inclut un certain nombre de PEP).

**Profil professionnel** : LinkedIn, mentions presse, historique des entreprises antérieures, formations. Permet de comprendre la trajectoire et d’identifier d’éventuelles incohérences (un « consultant senior » qui n’a aucune trace publique avant l’an dernier).

#### 10.8 Limites et faux positifs

Plusieurs pièges classiques en investigation corporate.

**Optimisation fiscale légale ≠ blanchiment** : un dirigeant qui a une société au Luxembourg pour la propriété intellectuelle, une société aux Pays-Bas pour le financement, et une société en France pour l’opérationnel, peut faire de l’optimisation fiscale agressive parfaitement légale. Les structures multi-juridictions sont un signal à investiguer, pas une preuve d’illégalité.

**Nominees légitimes** : certains nominees opèrent légalement (avocat qui détient des actions au nom d’un client pour un tiers de bonne foi). La présence d’un nominee est un signal, pas une condamnation.

**Domiciliation partagée légitime** : beaucoup de PME sont domiciliées chez leur expert-comptable ou dans un centre d’affaires — c’est légal et neutre.

**Faux positifs de noms** : « John Smith » apparaît comme dirigeant dans 2 000 sociétés à travers le monde. La majorité ne sont pas la même personne. La désambiguïsation par autres sélecteurs (nationalité, date de naissance, adresse) est obligatoire.

La règle constante : un signal isolé est une piste, pas une conclusion. La convergence de plusieurs signaux (capital symbolique + nominee + domiciliation partagée + leak ICIJ + flux suspects) construit la solidité.

-----

### Chapitre 11 — Investigation domaines, DNS, certificats et infrastructure

#### 11.1 Whois et Whois historique

Le **Whois** est l’enregistrement public d’un nom de domaine : qui l’a enregistré, quand, chez quel registrar, avec quelles coordonnées. Historiquement très transparent, le Whois s’est progressivement opacifié sous l’effet du RGPD (les coordonnées des particuliers sont désormais souvent masquées par défaut depuis 2018).

**Whois actuel** :

- **whois** (commande Linux/Mac) : `whois example.com` retourne les informations publiques du registrar.
- **DomainTools** (`whois.domaintools.com`) : interface web, données enrichies, payant pour les fonctions avancées.
- **ICANN Lookup** (`lookup.icann.org`) : interface officielle, basique mais fiable.

**Données typiquement disponibles** : nom du domaine, dates de création, expiration, dernière modification, registrar, serveurs DNS associés. Les coordonnées du titulaire (registrant) sont souvent masquées (« redacted for privacy » ou « WHOIS Privacy »).

**Whois historique** (la mine d’or) :

- **DomainTools Historical Whois** (payant) : restitue les enregistrements Whois passés. Un domaine qui est masqué aujourd’hui peut avoir été enregistré au nom réel de son propriétaire en 2015 — l’historique le révèle.
- **WhoisXML API** : équivalent.
- **Whoxy** (`whoxy.com`) : alternative, freemium.

L’investigateur consulte systématiquement le Whois historique d’un domaine suspect. Un email apparaissant dans le Whois historique est un pivot massif vers l’identité du propriétaire.

#### 11.2 DNS et enregistrements

Les **enregistrements DNS** d’un domaine révèlent comment il est techniquement opéré.

**Types d’enregistrements à connaître** :

- **A** : adresse IPv4 du domaine — où il est hébergé.
- **AAAA** : adresse IPv6.
- **MX** : serveurs email (révèle le fournisseur email — Google Workspace, Microsoft 365, fournisseur custom).
- **NS** : serveurs de noms (révèle l’opérateur DNS — Cloudflare, AWS Route 53, etc.).
- **TXT** : enregistrements texte arbitraires, utilisés pour SPF (anti-spam), DKIM, DMARC, vérifications de propriété (Google, Microsoft, etc.).
- **CNAME** : alias d’un autre domaine.

**Outils** :

- **dig** ou **nslookup** (Linux/Mac) : commandes natives.
- **dnsdumpster** (`dnsdumpster.com`) : interface web qui visualise les enregistrements DNS et tente d’énumérer les sous-domaines.
- **SecurityTrails** (`securitytrails.com`) : freemium, historique DNS étendu, sous-domaines, données croisées.
- **MXToolbox** : outil web pratique pour vérifier les enregistrements MX et les listes noires.

**Pivots productifs** : les enregistrements TXT contiennent souvent des vérifications qui pointent vers des comptes Google Workspace ou Microsoft 365 — révélateur de l’organisation. Les enregistrements MX révèlent le fournisseur email. Les SPF (`v=spf1 include:_spf.example.com`) listent les domaines autorisés à envoyer du mail au nom du domaine — peut révéler des sous-traitants ou des relations d’affaires.

#### 11.3 Sous-domaines et certificate transparency

L’énumération des sous-domaines d’une cible est une étape cruciale pour cartographier son infrastructure.

**Outils d’énumération** :

- **Sublist3r** (open source) : agrège plusieurs sources publiques.
- **Amass** (OWASP, open source) : énumération avancée multi-techniques.
- **subfinder** (ProjectDiscovery, open source) : performant, maintenu activement.
- **DNSdumpster** : interface web pour les énumérations rapides.

**Certificate Transparency** : depuis 2018, toutes les autorités de certification (CA) publient les certificats SSL/TLS qu’elles émettent dans des **logs de transparence** publics et auditables. Cela permet de découvrir tous les sous-domaines d’une organisation pour lesquels un certificat a été émis.

- **crt.sh** (`crt.sh`) : moteur de recherche dans les logs CT. Recherche `%example.com` retourne tous les sous-domaines avec certificat. Outil indispensable.
- **Censys Certificates** : équivalent commercial avec plus de fonctionnalités.
- **Google Transparency Report** : pour des recherches ponctuelles.

L’énumération via crt.sh révèle souvent des sous-domaines internes ou de test que l’organisation pensait privés (`dev.example.com`, `staging.example.com`, `internal-vpn.example.com`). Ces sous-domaines pointent vers des services qui peuvent être exposés à investigation.

#### 11.4 Reverse IP et hébergement partagé

Le **reverse IP** identifie tous les domaines hébergés sur une même adresse IP. Si plusieurs cibles partagent un hébergement, elles peuvent être liées.

**Outils** :

- **YouGetSignal Reverse IP** : interface basique, gratuite.
- **DomainTools Reverse IP** (payant, plus complet).
- **SecurityTrails** : reverse IP intégré aux fonctions premium.
- **ViewDNS.info** : agrégateur de fonctions (reverse IP, reverse Whois, reverse MX, reverse NS).

**Limites** : la majorité des sites sont hébergés sur des hébergements mutualisés ou des CDN (Cloudflare, Fastly). Une IP Cloudflare peut héberger des centaines de milliers de sites — le reverse IP n’est pas discriminant. Les liens significatifs sont quand des sites sont hébergés sur des IP **dédiées** ou sur des **VPS petits hébergeurs** : la coïncidence est alors significative.

#### 11.5 Certificats TLS et SAN

Les **certificats TLS** d’un site contiennent plus d’information qu’on pense, exposable via une simple consultation.

**Information dans un certificat** :

- **Common Name (CN)** et **Subject Alternative Name (SAN)** : tous les domaines et sous-domaines couverts par le certificat.
- **Issuer** : autorité émettrice (Let’s Encrypt, DigiCert, Sectigo, etc.).
- **Validité** : dates de début et de fin.
- **Empreinte (fingerprint)** : identifiant unique du certificat.

**Le SAN est un pivot crucial** : un certificat unique peut couvrir plusieurs domaines apparemment sans lien. Si `companyA.com` et `unknown-related.net` sont dans le même certificat, ils sont opérés par la même entité.

**Consultation** :

- Dans le navigateur : cliquer sur l’icône cadenas, voir le certificat, lister les SAN.
- En ligne : `crt.sh`, `censys.io`, `ssllabs.com`.

#### 11.6 Shodan, Censys, ZoomEye

**Shodan** (`shodan.io`) est un moteur de recherche pour les **services exposés sur Internet**. Là où Google indexe les pages web, Shodan indexe les bannières de tous les services qui répondent sur les ports TCP/UDP : serveurs web, serveurs SSH, bases de données, caméras IP, systèmes industriels (SCADA), routeurs.

**Cas d’usage en OSINT** :

- Identifier l’infrastructure exposée d’une organisation : `org:"NomOrganisation"` ou `ssl:"NomOrganisation"`.
- Trouver des serveurs vulnérables (vieille version d’un service connu pour avoir des CVE).
- Identifier des dispositifs IoT exposés (caméras, routeurs SOHO).
- Tracker une infrastructure adverse (serveurs C2 utilisés par des attaquants — usage CTI).

**Censys** (`censys.io`) est un concurrent direct, avec une approche plus rigoureuse de scan et des données enrichies.

**ZoomEye** (chinois) est l’équivalent dont la couverture est meilleure sur l’Asie.

**Précaution** : la recherche est légale (les bannières sont publiques), l’**exploitation** des vulnérabilités identifiées est une attaque (illégale). L’investigateur OSINT documente ce qu’il observe — il ne touche pas.

#### 11.7 Géolocalisation IP

L’IP révèle généralement le pays, souvent la région ou la ville (avec une précision variable), le fournisseur d’accès, et parfois l’opérateur d’hébergement.

**Outils** :

- **MaxMind GeoIP2** : référence du marché, freemium pour la consultation, payant pour l’API.
- **IPinfo.io** : alternative, freemium.
- **IPLocation** : agrégateur web.

**Limites** :

- Les IP de **VPN** géolocalisent vers le pays de sortie du VPN, pas l’utilisateur réel.
- Les IP **mobiles** (4G/5G) ont une géolocalisation peu précise (pool d’IP de l’opérateur).
- Les IP **professionnelles** géolocalisent vers le siège du fournisseur, pas l’utilisateur.

La géolocalisation IP est un indice, pas une preuve de localisation. Particulièrement piégeuse en investigation criminelle où la cible utilise probablement un VPN ou Tor.

#### 11.8 Pivots croisés

L’investigation infrastructure devient productive par les **pivots croisés** entre les différentes dimensions techniques.

**Exemples de chaînes de pivot** :

- Domaine → Whois historique → email du registrant → Holehe → autres comptes
- Domaine → enregistrements MX → identification du fournisseur email → mise en cohérence avec l’organisation supposée
- Domaine → certificat → SAN → autres domaines opérés par la même entité
- Domaine → IP → reverse IP → autres domaines partageant l’hébergement
- IP → Shodan → bannières des services → version logicielle → CVE éventuelles → fingerprint de l’organisation
- Email → Holehe → service hébergé (ex : compte Google Workspace) → pivot vers le domaine du compte → tout le pivot domaine

#### 11.9 Fil rouge — MIRAGE Épisode 6

> **🎯 MIRAGE — Épisode 6 : le certificat SAN qui relie Delta Consulting à d’autres domaines**
> 
> L’investigateur s’attaque au domaine `deltaconsulting.mt` (Malte, identifié dans les résultats du Ch.5).
> 
> **Whois** : registrant masqué (« GDPR Masked »). Création en mars 2018. Registrar maltais.
> 
> **Whois historique via DomainTools** : avant 2019, le registrant était visible. Email : `m.consulting@protonmail.com`. Première trace nominative.
> 
> **Holehe sur `m.consulting@protonmail.com`** : présence sur Binance, Coinbase. Pas de pivot direct vers Delaunay nominativement — mais cohérence forte (DAF expert en finance + comptes crypto, déjà connus pour Delaunay).
> 
> **Enregistrements DNS** :
> 
> - MX : Google Workspace
> - TXT : vérifications Google Workspace (`google-site-verification=...`)
> - NS : Cloudflare
> 
> **crt.sh sur `deltaconsulting.mt`** : 4 certificats émis depuis 2019. Le dernier certificat couvre **trois SAN distincts** : `deltaconsulting.mt`, `delta-trading.mt`, et — surprise — `dt-investments.lu` (Luxembourg). Les trois domaines partagent le même certificat = **opérés par la même entité**.
> 
> **Investigation des deux domaines additionnels** :
> 
> - `delta-trading.mt` : société Delta Trading Ltd, Malte. Registre maltais : créée en 2020. Dirigeant : Joseph Borg (avocat maltais — probable nominee).
> - `dt-investments.lu` : société DT Investments S.à r.l., Luxembourg. Registre RCS Luxembourg : créée en 2021. Capital 12 000 €. Dirigeant : Jean Petit (consultant luxembourgeois, listé dans 80+ sociétés sur LinkedIn — nominee professionnel évident).
> 
> **Reverse IP sur l’IP du serveur de `deltaconsulting.mt`** : VPS chez OVH, mutualisé, plusieurs centaines de domaines — pas discriminant.
> 
> **Sélecteurs ajoutés au graphe** : 2 nouvelles sociétés (Delta Trading Ltd Malte, DT Investments S.à r.l. Luxembourg), 2 nominees (Joseph Borg, Jean Petit), 1 email pivot (`m.consulting@protonmail.com`). Le réseau s’étend de 1 société à 3, dans 2 juridictions opaques.

-----

### Chapitre 12 — Breaches, leaks et exploitation de données fuitées

#### 12.1 Cadre éthique et juridique

L’exploitation de données fuitées est l’un des sujets les plus délicats de l’OSINT. La consultation de données fuitées par des tiers, dans le cadre d’une investigation légitime, est généralement légale dans les juridictions occidentales — à plusieurs conditions.

**Première condition** : la fuite est **publique**. Les données ont été diffusées (pas obtenues directement par l’investigateur via une intrusion). Les bases comme Have I Been Pwned ou DeHashed agrègent des fuites publiques.

**Deuxième condition** : la consultation est **proportionnée à la finalité**. Vérifier si l’email d’une cible apparaît dans des breaches est légitime ; télécharger une base entière de millions d’enregistrements pour des recherches futures non spécifiées ne l’est pas.

**Troisième condition** : la **citation dans le rapport** doit être prudente. On peut écrire « le mot de passe de marc@example.com apparaît dans la fuite Adobe 2013 » — fait observable. On ne publie **jamais** le mot de passe lui-même (qui pourrait être réutilisé par d’autres comptes), ni des informations sensibles d’autres personnes incluses dans la même fuite.

**Quatrième condition** : la **conservation est limitée**. Les données issues de breaches ne sont conservées que le temps de la mission, dans un coffre chiffré, et détruites à la fin.

Le RGPD s’applique : les données personnelles issues de breaches restent des données personnelles. Leur traitement nécessite une finalité légitime et le respect des principes de minimisation.

#### 12.2 Have I Been Pwned

**Have I Been Pwned (HIBP)** (`haveibeenpwned.com`) est le service de référence, créé et maintenu par Troy Hunt. Gratuit pour la consultation, payant pour l’API et pour les recherches volumétriques.

**Usage basique** : entrer un email, voir dans quelles breaches il apparaît. HIBP ne révèle pas les mots de passe ni les données détaillées — seulement la présence et la nature des données compromises.

**API Pwned Passwords** : permet de vérifier si un mot de passe (ou plutôt son hash) apparaît dans des breaches, sans envoyer le mot de passe en clair (k-anonymity : on envoie les 5 premiers caractères du SHA-1, on reçoit tous les hashs commençant par ces 5 caractères, on compare localement).

**API HIBP** : pour les requêtes massives ou intégrées (typiquement utilisé en compliance pour vérifier les credentials des utilisateurs internes contre les breaches publiques).

**Limites** : HIBP n’inclut **pas** toutes les breaches existantes. Certaines breaches privées ou non publiées y manquent. C’est un point de départ, pas une source exhaustive.

#### 12.3 DeHashed, Snusbase, IntelX

Pour aller plus loin que HIBP, plusieurs services payants donnent accès aux **données détaillées** des breaches.

**DeHashed** (`dehashed.com`) : abonnement mensuel, recherche par email, pseudo, mot de passe (en clair ou hash), nom, adresse IP, téléphone, adresse postale. Couverture large (plusieurs milliards d’enregistrements). Standard professionnel.

**Snusbase** : équivalent, parfois avec des breaches que DeHashed n’a pas, et inversement.

**IntelX** (`intelx.io`) : couverture étendue qui dépasse les breaches classiques — inclut les pastebins, les fuites dark web, les leaks Telegram. Indispensable pour l’investigation moderne.

**LeakCheck** (`leakcheck.io`) : alternative, interface différente.

**Méthodologie** :

- Recherche par **email** : breaches contenant cet email + données associées (mots de passe en clair ou hashés, autres champs présents dans la base d’origine).
- Recherche par **username** : breaches contenant ce username (pivot croisé avec Sherlock/Maigret).
- Recherche par **mot de passe** : permet de trouver d’autres comptes utilisant le même mot de passe (hypothèse de la même personne).
- Recherche par **téléphone** : inclut les fuites téléphone notables (Facebook 2021, OpinionLab).
- Recherche par **domaine** : tous les emails d’un domaine présents dans des breaches — utile pour la due diligence d’entreprise.

#### 12.4 Logs d’infostealers

Une catégorie particulière de fuites s’est massivement développée depuis 2022 : les **logs d’infostealers**. Les infostealers (Lumma, RedLine, Vidar, Raccoon) sont des malwares qui volent les credentials stockés dans les navigateurs des machines infectées. Les logs contiennent : URL du site, identifiant, mot de passe en clair, cookies de session, et parfois données d’autocomplete (noms, adresses, numéros de carte).

Ces logs sont vendus sur des marchés dark web et sur Telegram, parfois publiés gratuitement. Plusieurs services indexent ces logs.

**Hudson Rock** (`hudsonrock.com`) : plateforme commerciale spécialisée dans le monitoring d’infostealer logs. Recherche par domaine — révèle si des employés d’une organisation ont été infectés et quels accès sont compromis.

**Flare** (`flare.io`) : monitoring multi-sources incluant les logs d’infostealers.

**Usage en investigation** : si un employé de la cible est infecté par un infostealer, ses cookies de session vendus permettent à un acquéreur de se connecter à ses comptes professionnels sans MFA. Pour l’investigateur OSINT défensif, c’est une source de monitoring précieuse.

#### 12.5 Pivots à partir d’une donnée trouvée

Un email, un username ou un mot de passe trouvé dans un breach ouvre plusieurs pivots productifs.

**Pivot par email** : le breach révèle d’autres données (nom, adresse, téléphone, employeur historique) qui enrichissent le profil de la cible.

**Pivot par mot de passe** : les utilisateurs réutilisent massivement leurs mots de passe. Trouver un mot de passe dans un breach permet de chercher où d’autres comptes utilisent le même mot de passe (à des fins de mapping de comptes, jamais à des fins d’accès non autorisé).

**Pivot par pattern** : un utilisateur peut avoir un pattern de mot de passe (`Marco75!`, `Marco2020`, `Marco75Paris!`). L’identification du pattern dans un breach révèle des comptes potentiellement utilisant des variations du même pattern.

**Pivot temporel** : la date du breach permet de situer la cible dans le temps. Un compte présent dans le breach LinkedIn 2012 confirme l’ancienneté de la présence en ligne.

#### 12.6 Le breach Ledger 2020

Un cas pratique mérite mention. En juin 2020, Ledger (fabricant de hardware wallets crypto) a été victime d’une breach exposant les données de 1 million de clients : email, nom, adresse postale, téléphone. Les acheteurs de Ledger sont par définition des détenteurs de crypto-actifs.

Pour l’investigateur patrimonial, le breach Ledger est un signal d’or : un email présent dans le breach Ledger confirme que la personne a acheté un Ledger entre 2017 et 2020, et donc détient (ou a détenu) des crypto-actifs. Combiné avec une absence de déclaration crypto dans les déclarations fiscales, c’est un signal d’enquête.

#### 12.7 Le dump Facebook 2021

En avril 2021, un dump de 533 millions de profils Facebook a été publié, scrapé en 2019 via une vulnérabilité de l’API Friends. Pour chaque profil : numéro de téléphone, nom, email, date de naissance, lieu de résidence, employeur, statut amoureux.

Pour l’investigateur, le dump Facebook 2021 est une **base de réconciliation téléphone ↔ identité** d’une ampleur inégalée. Un numéro identifié dans Telegram peut être vérifié contre le dump Facebook pour obtenir nom, email, et employeur d’un coup.

Limitation : les données datent de 2019. Un employeur déclaré sur Facebook en 2019 peut avoir changé. Mais comme indicateur, c’est extrêmement productif.

#### 12.8 Distinguer piste et fait corroboré

Toute donnée issue d’un breach doit être qualifiée. La présence d’un email dans un breach n’est pas équivalente à une preuve d’identité ou de fait.

**Une piste** : un email cible apparaît dans un breach Ledger. Indique probablement la détention de crypto-actifs au moment du breach.

**Un fait corroboré** : l’email cible apparaît dans le breach Ledger + un compte Coinbase est associé à cet email (Holehe) + une adresse Bitcoin est publiée par la cible sur Telegram + cette adresse a interagi avec Coinbase + le compte Coinbase est au nom de la cible (vérification via Holehe + corroboration). Faisceau convergent.

La cotation : un fait isolé issu d’un breach est typiquement coté C3 (source de fiabilité moyenne — la breach est authentique mais la donnée elle-même peut être obsolète, l’email peut avoir été partagé ou usurpé). Un faisceau convergent peut atteindre B2 voire A2.

#### 12.9 Limites et précautions

**Couverture variable** : aucune base ne contient toutes les breaches. Combiner HIBP + DeHashed + IntelX + Snusbase couvre bien, mais reste incomplet. Une absence de résultat ne signifie pas une absence de breach.

**Données obsolètes** : les breaches sont datées. Un email présent dans un breach de 2013 n’est pas nécessairement encore utilisé, et l’information associée peut être périmée.

**Faux dumps** : certains vendeurs dark web commercialisent de faux dumps recyclés ou fabriqués. Vérifier la crédibilité de la source et croiser avec plusieurs bases.

**Protection de l’investigateur** : certains breaches circulent via des canaux où la simple détention peut être problématique (dumps de données médicales, dumps contenant des données de mineurs). L’investigateur se limite aux services agrégateurs légitimes (HIBP, DeHashed) et évite le téléchargement direct de dumps bruts.

#### 12.10 Fil rouge — MIRAGE Épisode 7

> **🎯 MIRAGE — Épisode 7 : DeHashed et le pattern de mot de passe**
> 
> L’investigateur interroge DeHashed sur les emails connus de Delaunay.
> 
> Sur `marcdelaunay75@gmail.com` : présence dans 6 breaches.
> 
> - **LinkedIn 2012** : mot de passe hashé (SHA-1), craqué publiquement → `Marco75`
> - **Adobe 2013** : mot de passe en clair → `Marco75Paris!`
> - **MyFitnessPal 2018** : hash non craqué
> - **Ledger 2020** : email + nom + adresse (Levallois-Perret, confirmation domicile) + téléphone (le même que celui du dump Facebook 2021)
> - **LinkedIn 2021** (re-scrape) : profil confirmé
> - **Neopets 2020** : compte créé en 2004 (présence ancienne en ligne)
> 
> Sur `m.consulting@protonmail.com` : présence dans 1 breach.
> 
> - **Dream Market 2020** (leak d’un marché dark web) : email utilisé pour créer un compte → **lien direct entre l’email pivot de Delta Consulting et une activité sur un marché dark web**.
> 
> **Pattern de mot de passe identifié** : `Marco75`, `Marco75Paris!` — utilisation du nom italianisé + 75 (code postal Paris) + variations. L’investigateur note ce pattern pour les futures corroborations, sans jamais tenter de l’utiliser pour accéder à un compte (ligne rouge pénale).
> 
> **Confirmation patrimoine crypto** : le breach Ledger confirme la détention d’un hardware wallet. Combiné avec les comptes Binance et Coinbase identifiés au Ch.6 (via Holehe), la dimension crypto de l’enquête est solidement établie.
> 
> **Nouveau signal** : l’email `m.consulting@protonmail.com` (lié à Delta Consulting) a interagi avec un marché dark web en 2020. Ouvre la QI-3 (crypto-actifs) vers une investigation dark web dédiée au Ch.13.
> 
> **Sélecteurs ajoutés au graphe** : 6 présences de l’email perso dans des breaches datées, pattern de mot de passe identifié, téléphone confirmé multi-sources (Ledger + Facebook), adresse domicile confirmée (Levallois-Perret), 1 présence dark web pour l’email Delta Consulting.

-----

### Chapitre 13 — Dark Web et DARKINT : navigation, investigation, monitoring

#### 13.1 Internet ≠ web ≠ deep web ≠ dark web

La confusion entre ces termes est systématique dans les médias et nuit à la clarté de l’investigation. Remettre les mots à l’endroit est le préalable.

**Internet** est le réseau physique mondial — câbles, fibres, routeurs, protocoles TCP/IP. Il transporte du web, de l’email, du streaming, du pair-à-pair, du VPN, et bien d’autres choses. Le web n’est qu’une partie d’Internet.

Le **web** (World Wide Web) est un service sur Internet, basé sur HTTP/HTTPS et HTML. Il se décompose en trois couches.

Le **surface web** (ou clearnet) est l’ensemble des pages indexées par les moteurs de recherche classiques (Google, Bing). Estimation : 5 à 10 % du contenu web total.

Le **deep web** est l’ensemble des contenus web non indexés par les moteurs, qu’il soit légitime (intranets d’entreprise, bases de données académiques, contenus derrière authentification : compte bancaire, email, factures) ou non. Environ 90 % du web. La quasi-totalité est parfaitement légale. Confondre deep web et activité criminelle est une erreur de débutant.

Le **dark web** est un sous-ensemble du deep web, accessible uniquement via des réseaux d’anonymisation spécifiques (Tor, I2P, Freenet). En volume, le dark web est une fraction minuscule d’Internet : quelques centaines de milliers de domaines .onion, dont une majorité sont inactifs, dupliqués, ou abandonnés.

#### 13.2 Tor, I2P, Freenet : architectures

**Tor** (The Onion Router) est le darknet dominant. Architecture en trois couches de relais chiffrés (entry, middle, exit) qui anonymisent le trafic. Les services cachés ont des adresses en `.onion` (v3 aujourd’hui, 56 caractères). Tor sert aussi à naviguer anonymement sur le clearnet via l’exit relay.

**I2P** (Invisible Internet Project) est un darknet alternatif, moins utilisé que Tor. Architecture différente (packet-switched, chaque utilisateur relaye aussi du trafic). Services internes (eepsites, .i2p). Communauté plus réduite, usage concentré sur des publics techniques.

**Freenet / Hyphanet** est un réseau de stockage distribué anonyme. Architecture radicalement différente : les contenus sont répliqués à travers le réseau, pas hébergés sur des serveurs identifiables. Usage marginal aujourd’hui.

Pour l’investigateur, 95 % du travail se fait sur Tor. I2P et Freenet sont à connaître mais rarement pertinents sauf investigation très spécifique.

#### 13.3 Accès sécurisé : Tails ou Whonix

L’accès au dark web depuis le poste personnel est une faute d’OPSEC grossière. La distinction d’environnement est obligatoire.

**Tails** est un système d’exploitation live amnésique, démarré depuis une clé USB. Tout le trafic passe par Tor. Aucune trace n’est conservée après extinction. Usage : missions ponctuelles, terrain sensible, investigations qui ne nécessitent pas de continuité.

**Whonix** est une architecture en deux machines virtuelles : **Whonix-Gateway** route tout le trafic de la VM utilisateur par Tor, **Whonix-Workstation** est l’environnement de travail. Même si la workstation est compromise par un malware, elle ne peut pas leaker l’IP réelle (elle n’en a pas — elle ne voit que la gateway). Usage : investigations longues qui nécessitent de conserver des données entre sessions.

**Tor Browser sur une VM dédiée** est un compromis acceptable pour les missions peu sensibles, mais moins protecteur que Whonix ou Tails.

**Jamais** Tor Browser sur le poste personnel avec son navigateur habituel — la fuite d’identité est quasi-garantie (cookies, extensions, fingerprinting).

#### 13.4 OPSEC dark web

Quelques principes renforcés pour le dark web.

**VPN → Tor** : utiliser un VPN en amont de Tor masque l’utilisation de Tor à l’opérateur d’accès Internet (utile si l’usage de Tor est rare chez l’investigateur et pourrait se remarquer). Choix de compromis — Tor seul est recommandé par le Tor Project, mais VPN → Tor est une option défendable pour l’investigateur privé.

**Jamais Tor → VPN** : si le VPN est placé après l’exit node Tor, le trafic sort avec l’IP du VPN — ce qui identifie l’utilisateur et annule l’anonymat.

**Personas strictement dédiées** : un compte sur un forum .onion n’est utilisé que pour cette mission, avec un username qui n’est jamais utilisé ailleurs (ni sur le clearnet, ni sur d’autres missions). La réutilisation est l’erreur la plus productive pour la dé-anonymisation par les adversaires.

**Séparation stricte** : pas de copier-coller entre la VM dark web et la machine hôte. Pas de téléchargement de fichiers sur la machine hôte. Pas de sessions parallèles clearnet et dark web sur la même machine.

**JavaScript désactivé** : beaucoup d’attaques de dé-anonymisation exploitent JavaScript. Tor Browser désactive JavaScript par défaut en niveau de sécurité « Safest » — à conserver sauf nécessité absolue.

#### 13.5 Trouver des services .onion

L’absence de moteur de recherche centralisé est une caractéristique du dark web. Plusieurs outils partiels.

**Ahmia** (`ahmia.fi`) : moteur de recherche .onion le plus sérieux, interface clearnet qui liste les hidden services (également accessible en .onion). Couverture partielle mais curated — les contenus illégaux sont filtrés.

**Torch** (`xmh57jrzrnw6insl.onion`) : moteur historique du dark web, couverture plus large mais résultats noyés dans le bruit et le spam.

**Haystak** (`haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion`) : moteur avec une interface améliorée.

**DuckDuckGo .onion** (`duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion`) : le DuckDuckGo classique accessible via Tor, pour la recherche clearnet anonymisée (pas pour trouver des .onion).

**Hidden wikis** : listes de liens .onion maintenues par la communauté. Taux d’obsolescence très élevé (beaucoup de liens morts), souvent infestés de scams. À utiliser avec scepticisme.

**Sources les plus fiables pour trouver un service précis** : les références dans les rapports CTI (Recorded Future, Flare, SOCRadar publient régulièrement les .onion actifs), les forums eux-mêmes (un forum légitime cite ses pairs), les canaux Telegram spécialisés (paradoxalement, une partie de l’écosystème dark web se coordonne sur Telegram).

#### 13.6 Forums cybercriminels

Les forums cybercriminels sont une catégorie centrale du dark web pour l’investigation. Ils combinent marchés (vente de données, d’accès, d’outils) et communauté (discussions techniques, réputation, vouching).

**Grands forums actifs (état 2025-2026)** :

- **Exploit.in** : forum russophone historique, haut niveau technique, vouching strict, sujets dominants : exploits 0-day, accès corporate, ransomware.
- **XSS.is** : similaire à Exploit.in, russophone, plus ouvert.
- **BreachForums** : forum anglophone de données volées, fermé et rouvert plusieurs fois, successeur des RaidForums.
- **Dread** : équivalent Reddit du dark web, forum communautaire couvrant les marketplaces.
- **Nulled, Cracked** : forums grand public de carding, comptes volés, scripts.

**Structure typique** : sections par thématique (exploits, access, data, services, discussion), vouching pour les sections avancées (un nouveau membre doit être parrainé par plusieurs existants), réputation (système de karma basé sur les transactions réussies), règles strictes (trahison = bannissement définitif + exposition publique).

**Économie de la confiance** : dans un environnement où tout le monde est anonyme et criminel, la **réputation** est la seule monnaie. Les forums investissent beaucoup dans les mécanismes de vouching, arbitrage, et réputation. L’investigateur qui comprend ces dynamiques peut exploiter les erreurs (un vendeur qui change de pseudo perd sa réputation — identifier le lien est précieux).

#### 13.7 Marketplaces

Les marketplaces dark web ont connu une évolution significative depuis Silk Road (2011-2013). L’écosystème a fragmenté après les saisies majeures (AlphaBay 2017, Hansa 2017, Hydra 2022).

**Catégories de marketplaces (état 2025-2026)** :

- **Drogues** : toujours le volume dominant, marchés spécialisés par région (Archetyp, MGM Grand, Kingdom Market — statuts très variables, nouveaux marchés émergent et disparaissent régulièrement).
- **Données** : Genesis Market (saisi 2023), Russian Market (actif), 2easy — vente de logs d’infostealers et d’accès.
- **Armes, faux documents, services** : marchés plus marginaux, majoritairement scams.
- **Services spécialisés** : ransomware-as-a-service (RaaS), bulletproof hosting, blanchiment crypto, vouching services.

**Tendance 2024-2026** : migration d’une partie de l’activité des marketplaces centralisées vers Telegram et des canaux dédiés. L’arrestation de Pavel Durov en août 2024 a marginalement ralenti cette tendance sans l’inverser — Telegram reste plus accessible que Tor.

**Vue d’investigateur** : l’investigation sur les marketplaces documente les tendances (prix des accès, populations de vendeurs, réputations), identifie les liens entre un vendeur et une identité possible (pivot par PGP key, par username réutilisé, par style d’écriture), et alerte sur les données volées concernant la cible.

#### 13.8 Investigation des erreurs OPSEC criminelles

Les criminels font des erreurs d’OPSEC. Ces erreurs sont la principale source d’investigation productive sur le dark web.

**Username réutilisé** : un vendeur dark web qui utilise le même pseudo sur un forum clearnet (gaming, jeux d’argent, forum tech de jeunesse) est identifiable. Les outils classiques (Sherlock, Maigret) s’appliquent. Nombreuses arrestations historiques via ce vecteur.

**Clé PGP avec email identifiable** : les vendeurs utilisent des clés PGP pour les transactions sensibles. Une clé PGP expose un fingerprint et parfois un email associé. Les **serveurs de clés PGP publics** (`keys.openpgp.org`, `pgp.mit.edu`) sont indexables. Un fingerprint PGP trouvé sur le dark web peut matcher un email publié sur un profil clearnet.

**Adresse Bitcoin réutilisée** : une adresse Bitcoin qui reçoit des paiements d’un marché dark web et qui est également publiée sur un profil clearnet (pour des pourboires, des dons, des paiements) établit un lien direct. Le clustering Bitcoin (Ch.19) aggrave ce risque pour les criminels.

**Métadonnées dans les fichiers partagés** : PDF avec nom d’auteur, images avec EXIF, documents Office avec historique d’édition. Les criminels qui partagent des preuves de leurs stocks ou de leurs services laissent souvent fuiter des métadonnées.

**Style d’écriture (stylométrie)** : un analyste peut identifier un même auteur entre deux textes (sur un forum criminel et sur un blog personnel par exemple) par l’analyse stylométrique (vocabulaire, structure de phrase, erreurs typiques, tics). Technique d’attribution avancée (voir Ch.27).

**Fuseau horaire** : les heures de publication révèlent le fuseau horaire. Un vendeur « anonyme » qui publie systématiquement entre 9h et 18h UTC+3 est probablement basé en Russie, en Turquie, ou en Arabie.

#### 13.9 Monitoring dark web

Le monitoring continu du dark web est une prestation d’OSINT pour les organisations qui veulent surveiller leurs mentions, leurs données fuitées, les menaces ciblant leurs systèmes.

**Solutions commerciales** :

- **Flare** (`flare.io`) : monitoring multi-sources (dark web, clearnet, Telegram), interface moderne, API.
- **Recorded Future** : leader historique, très coûteux, couverture étendue.
- **DarkOwl** : spécialiste dark web avec indexation massive.
- **Cybersixgill** : monitoring ciblé entreprise.
- **SOCRadar** : alternative plus accessible.
- **Digital Shadows (ReliaQuest)** : intégré à une suite de threat intelligence.

**Ce que les solutions commerciales surveillent** : mentions du nom de l’organisation, domaines, emails d’employés, produits, noms de dirigeants. Les alertes remontent quand une mention est détectée.

**Limites** : aucun service ne couvre 100 % du dark web. Les forums les plus fermés (vouching requis, communauté restreinte) restent inaccessibles à l’indexation automatisée. Le coût est élevé (10 000 à 100 000+ €/an). Les faux positifs sont fréquents (mentions génériques, homonymes).

**Monitoring artisanal** : pour un investigateur indépendant ou un petit CERT, le monitoring artisanal via Ahmia, Telegram channels, et consultation manuelle de forums pertinents reste utile. Moins exhaustif, mais ciblé et économique.

#### 13.10 Limites pour l’investigateur privé

La ligne rouge est nette : **observer oui, interagir non**.

La **consultation** d’un forum ou d’un marché est généralement légale (les contenus sont publics pour qui se donne la peine d’accéder). L’investigateur peut parcourir les annonces, capturer les pages pertinentes, documenter les vendeurs.

L’**interaction** est très risquée :

- **Acheter un échantillon** pour vérifier si les données volées concernent la cible = recel de données obtenues frauduleusement (sanction pénale).
- **Négocier avec un vendeur** sans conclure d’achat = complicité potentielle, surtout si des paiements sont faits.
- **Commander un service** (doxing, hacking à façon) = commande d’infraction.
- **Rejoindre un groupe nécessitant un vouching** en se faisant parrainer par un membre existant = risque de participation active à la communauté criminelle.

Les LEA ont un cadre différent : opérations sous couverture autorisées par un magistrat, achats contrôlés de preuves, infiltration de groupes. L’investigateur privé ne dispose pas de ces pouvoirs et ne peut pas les simuler.

**En cas de découverte de contenus pédopornographiques** : arrêt immédiat de la consultation de la source, signalement à Pharos (France) ou NCMEC (international). Pas de capture de la preuve (la détention est pénalement sanctionnée) — mention de l’observation dans le rapport sans conservation du contenu.

#### 13.11 Faux positifs sur le dark web

Le dark web est un environnement de tromperie permanente. Les faux positifs sont la norme, pas l’exception.

**Marques trompeuses** : un forum « FrenchHackers » n’est pas nécessairement français. Les marques et les drapeaux sont utilisés pour attirer — la géographie réelle des opérateurs doit être investiguée séparément.

**Données recyclées ou fausses** : un vendeur qui prétend vendre 10 millions de comptes peut vendre un vieux dump déjà public, un échantillon repackagé, ou des données fabriquées. La vérification est obligatoire avant de traiter une information dark web comme fiable.

**Faux vendeurs (scammers)** : une large proportion des vendeurs dark web sont des scammers qui prennent les paiements sans livrer. Les mécanismes d’escrow des marketplaces réduisent le risque mais ne l’éliminent pas.

**Opérations de provocation** : certains forums, comptes ou annonces sont en réalité des honeypots opérés par des LEA ou des services de renseignement. Interagir activement sur un honeypot peut exposer l’investigateur privé.

**Traduction piégée** : beaucoup de contenus dark web sont en russe, chinois, ou autres langues. Les traductions automatiques peuvent modifier significativement le sens — faire valider par un locuteur natif pour les informations critiques.

#### 13.12 Fil rouge — MIRAGE Épisode 8

> **🎯 MIRAGE — Épisode 8 : monitoring dark web sur les sociétés Delaunay**
> 
> Le signal remonté au Ch.12 (`m.consulting@protonmail.com` présent dans le leak Dream Market 2020) motive une investigation dark web ciblée.
> 
> **Environnement** : VM Whonix-Workstation (avec Whonix-Gateway pour le routage Tor), compte d’investigation dédié créé pour cette mission.
> 
> **Recherche sur Ahmia** : mots-clés `technovert`, `delta consulting`, `malta company formation`. Pas de résultat direct pour les noms cibles.
> 
> **Consultation de BreachForums** (snapshot récent, via un mirror clearnet + vérification sur le forum actif en .onion) : recherche de mentions des domaines cibles. Pas de résultat.
> 
> **IntelX** (qui indexe partiellement le dark web) sur `m.consulting@protonmail.com` : l’email apparaît dans la fuite Dream Market 2020 (confirmation du Ch.12) et dans un dump de 2022 d’un forum francophone mineur de fiscalité agressive (capture partielle, discussions sur les montages offshore).
> 
> **Consultation du forum mineur** : après identification du .onion via TGStat (canaux Telegram spécialisés), l’investigateur accède au forum en observation passive. Recherche dans les archives : deux posts en 2021 et 2022 d’un utilisateur `delta_mt` posent des questions techniques sur les structures Malte-Luxembourg et les flux crypto. Style d’écriture proche de celui observé sur le canal Telegram « Offshore Trading Club » (Ch.8).
> 
> **Stylométrie légère** (comparaison manuelle) : vocabulaire technique, tournures, erreurs de ponctuation convergent. Cotation C3 (source moyenne, corroboration partielle).
> 
> **Pas de tentative d’achat** de données, pas d’interaction avec quiconque sur le forum. Observation pure.
> 
> **Résultat de l’épisode** : confirmation indirecte d’une activité de Delaunay (via persona `delta_mt`) sur un forum francophone de fiscalité agressive. Ajout au rapport avec cotation C3, à corroborer avec d’autres sources si possible.
> 
> **Sélecteurs ajoutés au graphe** : 1 forum .onion, 1 username dark web (`delta_mt`), 2 posts datés avec contenu technique cohérent avec le profil professionnel de Delaunay. Risque documenté : la cotation est prudente (C3) pour ne pas sur-interpréter.

-----

## PARTIE IV — IMINT, GEOINT ET VÉRIFICATION VISUELLE

> **Ce que cette partie apprend.** Analyser des images (recherche inversée, métadonnées, authenticité), géolocaliser et chronolocaliser des scènes (méthodologie Bellingcat), investiguer les transports (maritime, aérien, véhicules), et vérifier les contenus synthétiques (deepfakes, images IA).
> 
> **Ce qu’elle ne couvre pas.** L’analyse technique avancée en vision par ordinateur (champ spécialisé hors OSINT), le reverse engineering de générateurs IA.
> 
> **Ce que vous saurez faire après cette partie.** Vérifier l’authenticité d’une image ou vidéo, localiser une scène à partir d’indices visuels, suivre un navire ou un avion d’intérêt, et reconnaître les signaux de contenu synthétique.

-----

### Chapitre 14 — IMINT : analyse d’images et recherche inversée

#### 14.1 La recherche inversée : une discipline, pas un moteur

La recherche inversée d’image est la première étape de toute investigation visuelle. Elle répond à trois questions : cette image existe-t-elle ailleurs, depuis quand, et dans quels contextes ?

Aucun moteur n’est exhaustif — la règle est la **multiplication des sources**.

**Google Images** : index le plus large en volume, mais algorithme orienté similarité visuelle globale plutôt que matching précis. Bon pour les images très diffusées, moins pour les images obscures.

**Yandex Images** : largement supérieur à Google sur les visages et les correspondances partielles. La référence pour l’identification visuelle.

**TinEye** (`tineye.com`) : spécialisé dans la **recherche exacte** de correspondances et la **datation de première apparition**. C’est l’outil pour savoir si une image est récente ou recyclée — trier les résultats par date la plus ancienne révèle quand l’image est apparue sur le web indexé.

**Bing Visual Search** : alternative parfois productive, index différent de Google.

**Google Lens** (mobile, disponible en web via images.google.com) : reconnaissance visuelle avec extraction de texte, identification d’objets. Complémentaire de la recherche par similarité.

**Méthode** : tester **tous** les moteurs systématiquement sur chaque image pertinente. Ne jamais conclure « l’image n’existe pas ailleurs » sur la base d’un seul moteur.

#### 14.2 Métadonnées EXIF

Les **métadonnées EXIF** (Exchangeable Image File Format) sont intégrées dans la majorité des fichiers images et contiennent des informations précieuses.

**Données typiques** :

- **GPS** : coordonnées de prise de vue (si le GPS était activé).
- **Date et heure** : de prise de vue et de modification.
- **Appareil** : modèle d’appareil photo ou de smartphone.
- **Paramètres** : ouverture, vitesse, ISO, focale.
- **Logiciel de retouche** : Photoshop, GIMP, etc.
- **Auteur** : champ parfois renseigné.

**Outils** :

- **ExifTool** (Phil Harvey, ligne de commande) : référence absolue, lit tous les formats d’image, vidéo, audio.
- **Jimpl** (`jimpl.com`) : interface web simple pour l’analyse rapide.
- **Metadata2Go** : alternative web.
- **ExifPurge** (inverse) : pour stripper les métadonnées avant de partager.

**Piège majeur** : la plupart des réseaux sociaux **suppriment les EXIF** automatiquement à l’upload (Facebook, Instagram, Twitter, LinkedIn). Une image téléchargée depuis un réseau social n’a généralement plus ses EXIF d’origine.

**Exceptions utiles** :

- **WhatsApp en mode “document”** (pas en mode image) : conserve les EXIF.
- **Email en pièce jointe** : conserve généralement les EXIF.
- **Sites hébergeant l’image brute** : certains forums, sites personnels, services de stockage ne strippent pas.
- **Archives** (Wayback Machine) : parfois les versions archivées conservent les EXIF.

La règle : toujours essayer d’obtenir l’image dans sa version originale (avant passage par un réseau social) pour maximiser les chances de récupérer des EXIF.

#### 14.3 Analyse sans EXIF : les indices visuels

Dans 80 % des cas, les EXIF sont absents. L’analyse repose alors entièrement sur les **indices visuels** contenus dans l’image.

**Catégories d’indices** :

**Enseignes et texte** : langue, alphabet, marques commerciales visibles. Une enseigne en cyrillique élimine tout pays non slave. Une marque McDonald’s indique soit l’Occident, soit les pays où McDonald’s est présent (ce qui exclut des zones précises — Iran, Corée du Nord, certains pays africains).

**Plaques d’immatriculation** : format très révélateur. Les plaques européennes, américaines, asiatiques ont chacune des caractéristiques visuelles (ratio, couleur, position des lettres et chiffres, drapeau UE). Un outil comme **plateshack.com** liste les formats par pays.

**Signalétique routière** : couleur des panneaux (jaune aux US, bleu en Europe pour les autoroutes), forme, police, types de marquage au sol. Les **normes routières** varient subtilement entre pays voisins et sont diagnostiques.

**Végétation** : une végétation méditerranéenne (oliviers, cyprès, palmiers) élimine l’Europe du Nord. Des bouleaux ou sapins éliminent les régions tropicales. Des outils spécialisés (iNaturalist) peuvent identifier des espèces.

**Architecture** : style des bâtiments, matériaux, fenêtres, toitures — révélateurs de région et d’époque. Maisons à toits rouges et murs blancs = Méditerranée. Maisons victoriennes = Royaume-Uni ou anciennes colonies.

**Uniformes** : militaires, policiers, sécurité — les uniformes sont standardisés par pays et parfois par unité.

**Météo** : la combinaison de végétation et de météo apparente renseigne sur la saison et la latitude.

**Cohérence globale** : un seul indice peut être trompeur. Un panneau en arabe ne dit pas « Syrie » — il peut être au Maroc, en Tunisie, en Jordanie, en Irak. La **convergence** de plusieurs indices indépendants est la seule approche fiable.

#### 14.4 Recherche par crop et zoom

Une technique souvent négligée : **isoler une portion pertinente** de l’image et la rechercher séparément. Google Images permet (via clic droit « Rechercher cette image avec Google Lens ») de sélectionner un rectangle dans l’image et de chercher uniquement cette portion.

Exemple : dans une photo de ville, crop sur une enseigne visible au fond → recherche de cette enseigne → identification du magasin → localisation précise. Beaucoup d’identifications GEOINT impossibles sur l’image entière réussissent sur un crop.

De même, une **amélioration ciblée** (contraste, luminosité, netteté) d’une zone spécifique peut rendre lisible un texte flou ou identifier un détail important.

#### 14.5 Vérification d’authenticité : ELA et cohérence visuelle

Vérifier si une image a été manipulée est une compétence cruciale en 2026.

**Error Level Analysis (ELA)** : technique qui visualise les zones d’une image compressées différemment. Une image JPEG non modifiée a un niveau d’erreur relativement homogène sur toute sa surface. Une zone modifiée (ajoutée, retouchée) a généralement un niveau d’erreur différent, révélé par ELA.

**Outils** :

- **FotoForensics** (`fotoforensics.com`) : outil web gratuit de référence, analyse ELA + autres techniques.
- **Forensically** (`29a.ch/photo-forensics`) : alternative gratuite avec plusieurs algorithmes.
- **Ghiro** : solution open source auto-hébergeable.

**Limites de l’ELA** : les compressions JPEG multiples (image sauvegardée plusieurs fois, passée par les réseaux sociaux) créent des artefacts qui ressemblent à des modifications. Une image avec un ELA suspect n’est pas nécessairement modifiée — et une image au ELA « propre » peut l’être.

**Cohérence des ombres** : dans une image authentique, toutes les ombres devraient être cohérentes avec une source lumineuse unique. Des ombres contradictoires signalent une composition. Outils de visualisation : règle graphique, tracés d’angles.

**Cohérence des reflets** : dans les yeux, sur les surfaces brillantes, sur l’eau — les reflets contiennent des informations sur l’environnement. Incohérences = signe de manipulation.

**Recherche de première occurrence** : via TinEye, identifier la plus ancienne apparition publique de l’image. Si une image « récente » apparaît déjà sur un site de 2015, c’est du recyclage.

#### 14.6 Limites et règle de la convergence

**Originalité non indexée** : une image originale non publiée ne donnera aucun résultat en recherche inversée. L’absence de résultat ne signifie pas que l’image est authentique — seulement qu’elle n’a pas été indexée auparavant.

**Compressions multiples** : les passages par les réseaux sociaux dégradent progressivement les images, ce qui brouille les analyses techniques (ELA, métadonnées).

**Ombres et sol plat** : l’analyse géométrique des ombres nécessite un sol plat et des ombres nettes. Impossible sur une photo en intérieur ou par temps couvert.

**Sur-interprétation** : l’erreur classique est de traiter un indice comme une conclusion. Un panneau en arabe, un drapeau, un uniforme — chaque élément pris isolément est un indice faible. **La convergence de plusieurs indices indépendants** est la seule approche fiable pour une conclusion.

-----

### Chapitre 15 — GEOINT : géolocalisation, chronolocation et OSINT spatial

#### 15.1 La méthodologie Bellingcat

La **méthodologie Bellingcat** s’est imposée comme la référence en géolocalisation OSINT. Elle structure l’analyse d’une image ou vidéo en étapes systématiques.

**Étape 1 — Extraction des indices** : lister tous les éléments visibles qui portent une information géographique (enseignes, plaques, signalétique, architecture, végétation, reliefs, ombres).

**Étape 2 — Formulation d’hypothèses** : à partir des indices, formuler 2 à 5 hypothèses de localisation. Ne pas se fixer prématurément sur une.

**Étape 3 — Vérification** : pour chaque hypothèse, confronter les indices supplémentaires (Street View, imagerie satellite, photos panoramiques) aux éléments visibles. Une hypothèse qui résiste à plusieurs vérifications indépendantes devient la conclusion.

**Étape 4 — Cohérence temporelle** : utiliser les ombres (SunCalc) et la météo (archives) pour valider la date et l’heure supposées.

**Étape 5 — Documentation** : capturer chaque étape, chaque comparaison, chaque vérification. Un rapport GEOINT démontre la méthode.

Cette méthodologie est enseignée gratuitement par Bellingcat (articles, vidéos, exercices). Une investigation GEOINT professionnelle la suit systématiquement.

#### 15.2 Outils de cartographie

**Google Maps** et **Google Street View** : couverture massive dans les zones développées. Fonction « historique » de Street View : voir les différentes captures dans le temps (jusqu’à 10-15 ans d’historique dans certaines rues).

**Mapillary** (`mapillary.com`, Meta) : plateforme communautaire de photos à 360°, couverture variable mais parfois meilleure que Street View dans certaines zones (pays en développement, zones rurales).

**KartaView** (`kartaview.org`) : alternative open source.

**OpenStreetMap** : cartographie collaborative, très complète, avec parfois des détails manquants sur Google Maps (petits chemins, points d’intérêt communautaires).

**Bing Maps** : occasionnellement utile pour sa vue « Bird’s Eye » (oblique) qui révèle des angles non visibles sur Google.

**Apple Maps** : différent de Google Maps dans certaines zones, à tester pour des vérifications croisées.

#### 15.3 Imagerie satellite

L’imagerie satellite ouvre des possibilités impossibles avec la cartographie.

**Sentinel Hub** (`sentinel-hub.com`) : accès aux images Sentinel-2 (Copernicus, UE) gratuitement. Résolution ~10 mètres, acquisition tous les 5 jours sur chaque point du globe. Suffisant pour détecter des évolutions à grande échelle (construction, destruction, mouvements de flotte).

**Google Earth** : couverture historique précieuse (archives remontant parfois à 20 ans). Résolution variable selon les zones. Fonction « Timeline » pour comparer les évolutions.

**Planet Labs** et **Maxar** (payants) : imagerie commerciale haute résolution (sub-mètre), acquisition quotidienne. Utilisé par les journalistes d’investigation et les services de renseignement. Tarifs élevés mais ponctuellement accessible pour des projets.

**NASA Worldview** : imagerie scientifique gratuite, utile pour les phénomènes environnementaux.

**Cas d’usage** : détection de nouvelles constructions, évolution d’un site industriel ou militaire, mouvements de flotte dans un port, présence/absence d’aéronefs sur une base.

#### 15.4 Chronolocation par les ombres

Les **ombres** révèlent l’heure et la date d’une prise de vue, sous réserve d’avoir un sol plat et des ombres nettes.

**Principe** : la direction et la longueur d’une ombre dépendent de la position du soleil, elle-même fonction de la latitude, de la longitude, de la date, et de l’heure (UTC). Inversement, connaissant la position géographique et l’ombre, on peut calculer la date et l’heure.

**Outil de référence** : **SunCalc** (`suncalc.org`). Entrer la position supposée sur la carte + la date supposée → SunCalc affiche la trajectoire du soleil et la position des ombres à chaque heure. Comparer avec l’ombre observée sur l’image.

**Méthodologie pratique** :

1. Identifier un élément vertical connu sur l’image (poteau, arbre, personne debout) et son ombre.
1. Mesurer l’angle de l’ombre par rapport au Nord (en utilisant la géométrie de l’environnement).
1. Utiliser SunCalc pour trouver à quelle heure et quelle date l’ombre a cet angle à cette position.
1. Recouper avec d’autres indices (température apparente, végétation — saison).

**Précision** : avec un bon élément vertical et des ombres nettes, on peut typiquement déterminer l’heure à 30 minutes près et la date à quelques jours près (au moins la saison).

#### 15.5 Chronolocation par la météo

La **météo apparente** dans une image peut être corroborée avec les **archives météo** du lieu supposé à la date supposée.

**Archives météo** :

- **Weather Underground** (`wunderground.com`) : historique détaillé par station, beaucoup de stations de particuliers en plus des stations officielles.
- **Ogimet** (`ogimet.com`) : archives synoptiques mondiales, format brut mais exhaustif.
- **Météo-France** (archives, partiellement payantes) : pour la France.

**Cas d’usage** : une vidéo filmée en extérieur par temps pluvieux à Paris le 15 mars 2024 — vérification dans les archives météo qu’il pleuvait effectivement à Paris ce jour-là. Si les archives indiquent un temps ensoleillé, la date prétendue est fausse.

Cette méthode fonctionne bien pour exclure des dates (prétendue date incohérente avec la météo réelle) et moins bien pour confirmer (beaucoup de jours ont la même météo).

#### 15.6 Croiser géolocalisation et chronolocation

La puissance de la GEOINT moderne vient du **croisement** des deux axes.

**Exemple type** : une vidéo prétend montrer un événement à Alep en octobre 2015. L’analyste géolocalise via les indices visuels (bâtiments, enseignes, reliefs) → confirmation Alep. Il chronolocalise via les ombres → 14h30 locale. Il vérifie la météo via archives → temps ensoleillé, cohérent. Conclusion : lieu et temporalité plausibles.

Inversement, une vidéo prétendue de 2025 dont les ombres et la végétation suggèrent une autre saison, ou dont la météo archivée ne correspond pas, est suspecte.

#### 15.7 Cas pratiques type Bellingcat

Bellingcat publie régulièrement des méthodologies détaillées de géolocalisation. Quelques cas types à connaître.

**Géolocalisation d’une vidéo de combat** (conflit ukrainien, syrien) : extraction d’indices (type de route, végétation, infrastructures), hypothèses régionales, vérification Street View ou imagerie satellite.

**Géolocalisation d’une photo de propagande** : un dirigeant dans un lieu supposé → vérification de l’architecture, des détails de décoration, des personnes présentes.

**Identification d’un site industriel militaire** : comparaison imagerie satellite, évolution dans le temps, présence de véhicules typiques.

Le site Bellingcat (`bellingcat.com`) propose des **exercices pratiques** (« Bellingcat challenges ») qui sont la meilleure école de la discipline.

#### 15.8 Limites

**Couverture Street View partielle** : l’Afrique subsaharienne, l’Asie centrale, certaines régions sont peu couvertes. Mapillary complète partiellement.

**Intérieurs** : impossibles à localiser avec les méthodes Bellingcat classiques. Indices possibles : type de prise électrique, interrupteurs, marques d’appareils électroménagers visibles, extincteurs (normes locales).

**Ombres absentes** : par temps couvert ou en intérieur, la chronolocation par les ombres est impossible.

**Sur-interprétation** : l’erreur classique est de conclure trop rapidement. Un panneau en langue donnée, un style architectural, un type de véhicule — chaque indice isolé autorise plusieurs hypothèses. La conclusion nécessite la convergence.

-----

### Chapitre 16 — OSINT maritime, aérien et de transport

#### 16.1 OSINT maritime

La majorité des navires de commerce émettent un signal **AIS** (Automatic Identification System) qui contient leur position, leur cap, leur vitesse, et leur identifiant. Ces signaux sont captés par des récepteurs côtiers et satellites, et agrégés par plusieurs services publics.

**MarineTraffic** (`marinetraffic.com`) : la référence grand public, freemium. Interface carte, recherche par nom de navire, IMO, MMSI. Historique accessible avec abonnement.

**VesselFinder** (`vesselfinder.com`) : concurrent direct, interface différente, couverture légèrement différente. Utile pour des vérifications croisées.

**Données disponibles par navire** :

- **Identité** : nom, IMO (numéro unique OMI, permanent), MMSI (identifiant radio), pavillon, type de navire.
- **Position actuelle** et **historique de route** (selon abonnement).
- **Propriétaire et opérateur** (souvent partiels ou obsolètes dans les bases gratuites).
- **Dimensions** : longueur, largeur, tirant d’eau.

#### 16.2 Comportements suspects en OSINT maritime

Plusieurs comportements signalent une activité à investiguer.

**Extinction AIS** : un navire qui cesse d’émettre son AIS « disparaît » des cartes. L’AIS peut être éteint légitimement (zones de conflit, pirates) ou illégitimement (trafic de pétrole sous sanctions, pêche illégale). Les analystes OSINT maritime détectent les extinctions en identifiant qu’un navire est arrivé à un port sans avoir été suivi — preuve qu’il a éteint son AIS.

**Transbordement en mer** (ship-to-ship transfer) : deux navires se rejoignent en haute mer pour transférer leur cargaison, souvent pour contourner des sanctions. Détectable par la convergence inhabituelle de deux navires suivie d’une séparation.

**Dark fleet** : flottes de navires (souvent pétroliers) qui opèrent en contournant les sanctions (Iran, Russie, Venezuela). Caractéristiques : navires anciens, pavillons de complaisance, changements fréquents de nom et de pavillon, propriétaires opaques.

**Cas documentés** : le suivi de la flotte fantôme russe post-2022 par plusieurs ONG (Windward, Kpler) a documenté des milliers de transferts de pétrole en violation du plafonnement des prix.

#### 16.3 OSINT aéronautique

Les avions civils émettent un signal **ADS-B** (Automatic Dependent Surveillance-Broadcast) qui est capté par des récepteurs amateurs et professionnels, agrégés par plusieurs plateformes.

**FlightRadar24** (`flightradar24.com`) : la référence grand public. Position en temps réel, historique (accessible avec abonnement), informations sur l’aéronef.

**ADS-B Exchange** (`adsbexchange.com`) : alternative gratuite, couverture souvent supérieure à FlightRadar24 sur les vols militaires ou sensibles (moins de filtrage).

**Flightaware** (`flightaware.com`) : équivalent, intégration avec les plans de vol déposés.

**Données par vol** :

- **Identité** : immatriculation (ex : F-HAAA pour Air France, N12345 pour les US), ICAO hex code.
- **Plan de vol** : origine, destination, heure départ/arrivée, route.
- **Position temps réel et historique**.
- **Type d’appareil** : modèle, compagnie (parfois).

#### 16.4 Identification d’un aéronef

**Registres par pays** :

- **FAA** (US) : `registry.faa.gov` — recherche par immatriculation N-number, propriétaire.
- **EASA** et registres européens : dispersés par pays, moins centralisés.
- **OACI** : registre international.

**Jets privés** : les registres publient propriétaires et opérateurs (parfois anonymisés via trusts ou sociétés). Les outils spécialisés (**JetSpotter**, **Dictator Alert**) suivent les vols de PEP et de figures d’intérêt. Un jet privé qui fait régulièrement Paris → Dubaï → Chypre est un signal digne d’investigation patrimoniale.

**Cas notable** : la coupure en 2022-2023 par Elon Musk du tracking de son jet privé (compte @ElonJet sur Twitter) a mis en lumière la capacité publique de suivre les jets privés via ADS-B.

**Limites** : certains vols militaires ou gouvernementaux n’émettent pas d’ADS-B, ou sont filtrés des bases publiques (accord entre FlightRadar24 et certaines agences). ADS-B Exchange est moins restrictif sur ce filtrage.

#### 16.5 OSINT véhicules terrestres

Les véhicules civils laissent moins de traces que navires et avions, mais plusieurs sources existent.

**Plaques d’immatriculation** : identifiables visuellement (format pays, année de mise en circulation selon les systèmes), mais la correspondance plaque → propriétaire nécessite généralement un accès LEA (en France, le fichier SIV n’est pas public).

**Péages et caméras publiques** : non accessibles à l’investigateur privé sauf réquisition judiciaire.

**Données publiques marginales** : certains États américains publient partiellement les registres de véhicules. Certains forums (tuning, collection) révèlent des véhicules rares et leurs propriétaires.

**Photos sur réseaux sociaux** : le véhicule visible sur une photo Instagram ou LinkedIn corrobore un train de vie, un déplacement (par la plaque visible), une localisation.

#### 16.6 OSINT logistique et fret

Pour les investigations commerciales ou géopolitiques, le suivi des flux de fret est parfois crucial.

**Containers** : le numéro de container peut être tracé via certains sites de compagnies maritimes (Maersk, MSC tracking public).

**Déclarations douanières** (US) : **Import Genius**, **Panjiva** — bases commerciales qui agrègent les déclarations douanières américaines (publiques par loi) et permettent de tracer les imports d’une entreprise. Très utile pour cartographier les chaînes d’approvisionnement.

**Suivi ferroviaire** : couverture très limitée, principalement via observation terrain et communautés d’enthousiastes (railway spotters).

-----

### Chapitre 17 — Contenus synthétiques, deepfakes et vérification

#### 17.1 Le principe fondamental

Un principe structure tout ce chapitre : **absence de preuve de manipulation ≠ authenticité**. Un outil de détection qui dit « probablement authentique » ne prouve pas l’authenticité. Un outil qui dit « probablement IA » donne un indice, pas une certitude.

**Un seul indice technique ne suffit jamais.** La vérification repose sur la **convergence de plusieurs indicateurs indépendants** — technique, contextuel, corroboratif. C’est la même logique que toute la méthodologie OSINT : pas de conclusion sur un indice unique.

Cette rigueur est d’autant plus importante que les détecteurs automatiques sont dans une course perdue contre les générateurs. Un détecteur qui fonctionne bien aujourd’hui sera contourné dans 6 à 12 mois par les nouveaux modèles. Les méthodes durables sont celles qui combinent analyse technique, analyse contextuelle, et corroboration.

#### 17.2 Images synthétiques : signaux visuels et leur obsolescence

Les générateurs d’images IA (Midjourney, DALL-E, Stable Diffusion, Flux, Ideogram) produisent des images de qualité croissante. Les signaux visuels classiques vieillissent vite.

**Signaux historiques (en déclin de fiabilité)** :

- **Mains et doigts incohérents** : six doigts, doigts fusionnés. De moins en moins fréquent dans les modèles 2024-2026.
- **Texte illisible** : les générateurs avaient du mal avec le texte — les modèles récents (Ideogram, Flux) s’en sortent mieux.
- **Arrière-plans avec structures impossibles** : architecture incohérente, perspectives impossibles. De moins en moins fréquent.
- **Symétrie excessive des visages** : visage trop parfaitement symétrique, quasi sans défaut humain.
- **Yeux** : reflets incohérents entre deux yeux, iris aux motifs étranges.
- **Bijoux et textures complexes** : détails qui ne tiennent pas à l’examen rapproché.

**Signaux émergents (2025-2026)** :

- **Absence de micro-imperfections** : grain de peau trop régulier, absence de cicatrices/taches, cohérence trop parfaite.
- **Arrière-plan sur-détaillé ou sous-détaillé** de manière incohérente avec la mise au point.
- **Comportement du flou de mouvement** : inexistant ou mal calibré.

Ces signaux deviendront obsolètes à leur tour. Le principe qui reste : examen minutieux + convergence de plusieurs signaux, jamais un seul.

#### 17.3 Métadonnées et watermarks

**Métadonnées absentes** : les images générées par IA n’ont généralement pas d’EXIF caméra. Mais l’absence d’EXIF n’est pas une preuve de synthèse — les réseaux sociaux les suppriment aussi.

**C2PA (Coalition for Content Provenance and Authenticity)** : norme émergente qui intègre des métadonnées signées cryptographiquement dans les fichiers (origine, historique de modification). Adopté par Adobe, Microsoft, Google, OpenAI, Meta (progressivement). Un fichier avec manifest C2PA peut être vérifié — absence de manifest n’est pas concluante dans un sens ou l’autre.

**SynthID** (Google DeepMind) : watermarking invisible intégré aux images générées par les modèles Google. Détectable par les outils Google.

**Watermarks visibles** : certains modèles (DALL-E) intégraient un watermark visible au moment de la génération. Systématiquement retiré par les utilisateurs — absence de watermark n’est pas une preuve.

L’écosystème des watermarks est en construction. Dans 2-3 ans, leur présence sera probablement plus généralisée. Aujourd’hui, c’est un outil complémentaire, pas central.

#### 17.4 Outils de détection : aides, pas verdicts

Plusieurs outils de détection publics existent, avec une fiabilité variable et des taux d’erreur significatifs.

**Hive Moderation** (`thehive.ai`) : API commerciale de détection de contenus IA (images, vidéos, texte). Relativement sérieuse.

**Illuminarty** (`illuminarty.ai`) : détection gratuite avec interface web, utile pour une première évaluation.

**Sensity AI** : professionnel, orienté entreprises (deepfake detection).

**SynthID Detector** : outil Google pour les contenus marqués par SynthID.

**Règle d’usage** : ces outils fournissent un **score de probabilité**, pas un verdict binaire. Un score de 70 % « probablement IA » est une orientation, pas une conclusion. Il doit être combiné avec l’analyse visuelle (17.2), le contexte, et la corroboration.

#### 17.5 Deepfakes vidéo

Les deepfakes vidéo (face swap, reenactment) sont techniquement plus complexes à produire que les images, et laissent généralement plus d’indices.

**Signaux visuels** :

- **Clignement anormal** : trop rapide, trop lent, asymétrique, ou absent.
- **Contour du visage flou** : les limites entre visage swappé et corps peuvent être floues, surtout avec des mouvements rapides.
- **Incohérence d’éclairage** : visage avec un éclairage différent du reste de la scène.
- **Dents et bouche** : mouvements labiaux parfois désynchronisés du son.
- **Oreilles et cheveux** : fréquemment mal rendus lors des mouvements.

**Méthodologie** : ralentir la vidéo image par image, examiner les transitions rapides, chercher les artefacts sur les mouvements de tête.

**Outils** :

- **Deepware Scanner** : détection publique gratuite.
- **Sensity AI** : professionnel.
- **Intel FakeCatcher** : orienté temps réel.

#### 17.6 Deepfakes audio

Le clonage vocal (voice cloning) a fait des progrès massifs (ElevenLabs, Play.ht, outils open source). Une vidéo audio de 30 secondes permet de cloner raisonnablement une voix.

**Signaux** :

- **Microprosodie anormale** : les variations fines de ton et de rythme qui caractérisent une voix humaine peuvent être plates ou incohérentes.
- **Transitions abruptes** : passages entre phrases qui sonnent concaténés.
- **Bruit de fond absent ou constant** : une voix clonée sur fond silencieux, là où la personne parle habituellement dans des environnements variés.
- **Respiration** : absente ou mal placée.

**Contextuel** : vérifier le **canal** de diffusion (un message audio WhatsApp d’un CEO qui demande un virement urgent → appeler le CEO par un autre canal pour confirmer). Le vishing assisté par IA (Ch.3 du cours Cybersécurité du quotidien) est une menace croissante.

**Outils** : moins matures que pour la vidéo. La méthode la plus fiable reste la **corroboration hors bande** : si la voix cible prétend demander une action sensible, vérifier par un autre canal avant d’agir.

#### 17.7 Texte généré : vérifier, pas détecter

La détection technique de texte généré par IA est la **moins fiable** de toutes les catégories. Les détecteurs (GPTZero, Originality.ai, Turnitin AI) ont des taux de faux positifs élevés et sont systématiquement contournés.

**La stratégie qui marche** : **vérifier les faits**, pas la génération.

- **Les faits cités sont-ils exacts ?** Les LLMs hallucinent. Un article qui cite une décision de justice, une publication académique, ou un fait historique peut l’avoir inventé. Vérifier chaque citation.
- **Les personnes mentionnées existent-elles ?** Les experts cités, les sources nommées — vérifier leur existence.
- **Les liens sont-ils valides et pointent-ils vers ce qui est prétendu ?** Les LLMs génèrent parfois des URLs plausibles mais inexistantes.
- **Première occurrence** : un texte apparaissant sur plusieurs sites quasi simultanément est suspect de génération ou de diffusion coordonnée.
- **Stylométrie** : comparer avec le style antérieur attesté de l’auteur prétendu. Changement radical de style = signal.

#### 17.8 Méthodologie de vérification en cinq étapes

Toute image, vidéo ou contenu suspect passe par cinq étapes de vérification.

**Étape 1 — Recherche inversée** : l’image ou la vidéo existe-t-elle ailleurs, depuis quand ?

**Étape 2 — Métadonnées** : que révèlent les EXIF (si présentes), les manifests C2PA, la structure du fichier ?

**Étape 3 — Analyse technique** : ELA, cohérence des ombres, signaux visuels de synthèse, détection IA.

**Étape 4 — Contexte** : l’élément est-il cohérent avec d’autres sources indépendantes ? Les personnes présentes, les lieux, les événements évoqués sont-ils vérifiables autrement ?

**Étape 5 — Corroboration** : existe-t-il d’autres sources qui confirment ou infirment le contenu ? Témoignages, autres photos/vidéos du même événement, mentions officielles ?

La **convergence** des cinq étapes produit un niveau de confiance. Une image qui passe toutes les étapes a une probabilité élevée d’authenticité. Une image qui échoue à plusieurs étapes est suspecte — sans qu’aucune étape seule ne soit concluante.

#### 17.9 Implications pour l’investigateur

La généralisation des contenus synthétiques transforme la posture de l’investigateur.

**Vérifier systématiquement avant d’utiliser** : un contenu visuel ou audio qui appartient à l’investigation doit être vérifié avant d’être traité comme élément factuel. La vérification est documentée au journal.

**Coter à la baisse par défaut** : en 2026, toute image ou vidéo trouvée en ligne sans corroboration doit être cotée avec prudence (C3 ou D3 par défaut, remontant avec la corroboration).

**Distinguer canal et message** : un message authentique peut être modifié. Un contenu authentique dans son existence peut être contextualisé de manière trompeuse (recyclage d’image ancienne, détournement de contexte).

**Former les clients** : le client d’une investigation (cabinet d’avocats, entreprise) peut ne pas être familier avec les limites de vérification. L’investigateur explique ce qu’il a vérifié et avec quelle confiance — il ne produit jamais un rapport qui donne une image pour authentique sans documenter la vérification.

#### 17.10 Fil rouge — MIRAGE Épisode 9

> **🎯 MIRAGE — Épisode 9 : la photo « alibi » de Delaunay**
> 
> En parallèle de l’investigation patrimoniale, le cabinet Legrand & Associés transmet à l’investigateur une photo postée publiquement sur l’Instagram de Delaunay (`marc_del75`). La photo montre Delaunay à Genève, dans un café, avec la date visible en légende : « 15 février 2026, pause café à Genève » — elle correspond au jour d’une transaction Bitcoin suspecte détectée par la banque. Le cabinet veut savoir si cette photo est authentique et peut constituer un alibi.
> 
> **Étape 1 — Recherche inversée (TinEye, Google, Yandex)** : aucune occurrence antérieure à la publication Instagram. Pas de recyclage détecté.
> 
> **Étape 2 — Métadonnées** : l’image téléchargée depuis Instagram n’a plus d’EXIF (Instagram les strippe). Demande au cabinet : existe-t-il une version originale (email, WhatsApp) ? Pas disponible.
> 
> **Étape 3 — Analyse technique** : ELA sur FotoForensics révèle des incohérences dans la zone du visage de Delaunay — niveau d’erreur différent du fond. Cotation prudente : suspect mais pas concluant.
> 
> **Étape 4 — Contexte** :
> 
> - Le café visible au fond : identifiable via les enseignes — un café réel à Genève (vérification via Google Street View, correspondance exacte avec une vue de la rue). Le lieu existe et est bien à Genève.
> - Mais : les **ombres** sur la photo ne sont pas cohérentes avec l’heure prétendue. SunCalc pour Genève le 15 février 2026 à midi → soleil au sud, ombres vers le nord. Sur la photo, les ombres pointent dans une direction incompatible.
> - La **météo** archivée à Genève le 15 février 2026 : ciel couvert et neige faible. Or la photo montre un ensoleillement franc.
> 
> **Étape 5 — Corroboration** :
> 
> - Aucune autre publication de Delaunay ou de son entourage ne mentionne un déplacement à Genève ce jour-là.
> - Son jet privé professionnel (si tracé via FlightRadar24 — pas de jet privé personnel identifié) : pas applicable ici.
> - Son téléphone (pas d’accès légal sans réquisition) : ligne rouge, l’investigateur ne tente rien.
> 
> **Conclusion analytique** : la photo est **techniquement incohérente** avec la date et le lieu prétendus. Trois indépendances signalent une manipulation : ELA suspect + ombres incohérentes + météo archivée contradictoire. Cotation E5 (source peu fiable, information probablement fausse). Cohérent avec une photo synthétique ou manipulée, destinée à fabriquer un faux alibi.
> 
> **Le rapport** : « La photo publiée ne peut être utilisée comme preuve d’une présence de Delaunay à Genève le 15 février 2026. Trois éléments techniques indépendants (analyse ELA, cohérence des ombres calculée via SunCalc, archives météo de Genève) contredisent la date et le lieu prétendus. Niveau de confiance : élevé sur la conclusion d’incohérence ; conclusion sur l’intention (fabrication d’alibi vs erreur de publication) : modérée. »
> 
> **Sélecteurs ajoutés au graphe** : 1 tentative d’alibi documentée, 1 vérification vidéo/image complète, faisceau d’éléments documentant la mauvaise foi (renforce les éléments sur la campagne de désinformation).

-----

## PARTIE V — FININT, CRYPTO ET INVESTIGATION FINANCIÈRE

> **Ce que cette partie apprend.** Mobiliser les sources financières ouvertes (comptes publiés, patrimoine, PEP, sanctions), investiguer les crypto-actifs (Bitcoin, Ethereum, stablecoins, DeFi, mixers, privacy coins), et articuler ces investigations dans un workflow OSINT cohérent.
> 
> **Ce qu’elle ne couvre pas.** L’investigation financière institutionnelle avec accès aux flux bancaires (domaine des CRF et services d’enquête), le traçage crypto professionnel avec outils dédiés comme Chainalysis Reactor ou TRM Labs (hors périmètre OSINT). La Partie V reste délibérément plus sobre que les parties voisines : son centre de gravité est l’articulation OSINT, pas une encyclopédie financière.
> 
> **Ce que vous saurez faire après cette partie.** Évaluer la cohérence patrimoniale d’une cible, tracer une chaîne de flux Bitcoin ou stablecoin jusqu’à un point de dé-anonymisation, intégrer la dimension financière dans une investigation OSINT complète.

-----

### Chapitre 18 — OSINT financier et patrimonial

#### 18.1 Lecture des comptes publiés

Les comptes publiés d’une entreprise (bilan, compte de résultat, annexe) sont une source OSINT de premier ordre — à condition de savoir les lire.

**Indicateurs à surveiller** :

- **Évolution du chiffre d’affaires** : une croissance brutale inexpliquée peut signaler une activité de blanchiment ou de surfacturation. Une stagnation avec augmentation des charges de consulting vers des sociétés liées = signal.
- **Charges externes** : postes de « consulting », « prestations », « honoraires » disproportionnés par rapport à l’activité réelle = red flag.
- **Résultat proche de zéro récurrent** : une entreprise qui génère un CA important sans jamais de résultat significatif, par des charges « exactement calibrées », signale une optimisation agressive ou une construction.
- **Comptes courants d’associés** : entrées et sorties de fonds des dirigeants — révèle des flux non documentés autrement.
- **Trésorerie** : incohérence entre CA annoncé et trésorerie disponible.
- **Commissaire aux comptes** : absence de CAC au-delà des seuils légaux = anomalie réglementaire.

**Sources principales** :

- **Pappers** (France) : comptes annuels publiés, ratios calculés.
- **Companies House** (UK) : rapports annuels complets, exhaustifs.
- **SEC EDGAR** (US) : 10-K, 10-Q, 8-K, proxy statements pour les sociétés cotées.
- **Orbis / Diane** (Bureau van Dijk, payant) : bases professionnelles exhaustives.

**Limite fondamentale** : les comptes publiés sont une **déclaration** — ils montrent ce que la société veut montrer. L’investigateur cherche les **incohérences** entre les comptes, les flux visibles, et la réalité opérationnelle (taille réelle, visibilité, effectif, présence physique).

#### 18.2 Investigation patrimoniale

Le patrimoine d’un individu laisse des traces publiques dans plusieurs registres.

**Immobilier** :

- **France** : cadastre (parcelles, pas de nom propriétaire depuis 2017 en public), **publicité foncière** (via notaires, payant) — révèle les transactions et les hypothèques. **SCI familiales** : détectables via Pappers (recherche par gérant/associé).
- **UK** : HM Land Registry (accès partiellement payant).
- **US** : public records des États — très ouverts, plusieurs agrégateurs (PropertyShark, Zillow pour les prix).

**Véhicules** : généralement non publics sauf dans certains États US. Investigation via photos (Instagram, LinkedIn) pour identifier les véhicules possédés.

**Biens de luxe** :

- **Bateaux** : **MarineTraffic** + **registres nationaux** (les bateaux > 7 m sont immatriculés en France et cherchables).
- **Avions privés** : registres FAA, EASA, OACI — propriétaire public ou trust.
- **Montres, œuvres d’art, bijoux** : pas de registres publics généralisés, investigation via assurance (pas accessible au privé) ou publications/photos.

**Train de vie visible** : Instagram, Facebook, Strava (trajets sportifs révélateurs de localisation). Les photos de voyages, les mentions de restaurants et hôtels, les marques portées sont des indicateurs de train de vie.

#### 18.3 PEP, sanctions et screening

Le screening contre les listes PEP et sanctions est une étape automatique de toute due diligence.

**Listes de sanctions** :

- **OFAC SDN (US)** : Specially Designated Nationals, sanctions américaines. Consultable gratuitement sur `sanctionssearch.ofac.treas.gov`.
- **UE** : liste consolidée, consultable via `webgate.ec.europa.eu/fsd`.
- **ONU** : liste consolidée des sanctions du Conseil de sécurité.
- **UK** : HM Treasury sanctions list.

**OpenSanctions** (`opensanctions.org`) : agrégateur open source de dizaines de listes (sanctions, PEP, criminalité) avec API gratuite. Standard pour le screening open source.

**PEP (Politically Exposed Persons)** : personnalités politiques, hauts fonctionnaires, dirigeants d’organisations internationales, leurs familles et proches. Bases payantes (WorldCheck, LexisNexis Bridger) couvrent exhaustivement. OpenSanctions inclut une liste PEP croissante en accès libre.

**Usage en investigation** : screening systématique des cibles d’une due diligence. Un PEP qui reçoit des flux importants sans justification économique = signal de corruption potentielle.

#### 18.4 Due diligence KYC/AML

La due diligence combine les sources précédentes dans un workflow structuré.

**Étapes d’une due diligence sur un individu ou une société** :

1. **Identification** : vérifier l’identité réelle (profil LinkedIn, présence en ligne cohérente, absence de red flags d’identité fictive).
1. **Registres légaux** : Pappers, Companies House, registres pays pertinents. Vérifier la société existe, est en activité, a des dirigeants cohérents.
1. **Screening sanctions** : OpenSanctions + listes officielles.
1. **Screening PEP** : bases dédiées.
1. **Presse et médias** : recherche Google, archives Factiva/Nexis si accès, vérification contentieux (Légifrance).
1. **Analyse structurelle** : si société, chaîne de participations, UBO, cohérence activité/capital/effectif.
1. **Patrimoine** : immobilier, véhicules, biens visibles cohérents avec revenus déclarés.
1. **Crypto** : présence sur exchanges (Holehe), breaches Ledger, mentions publiques d’actifs.
1. **Réputation en ligne** : réseaux sociaux, forums, mentions.
1. **Livrable** : rapport avec cotation par dimension, conclusion go/no-go ou go with conditions.

#### 18.5 Distinguer signal et corroboration

Règle constante de l’OSINT financière : un signal isolé n’est jamais une conclusion.

**Un patrimoine élevé ≠ preuve de fraude** : peut être hérité, issu d’une activité légitime antérieure, financé par un conjoint, etc.

**Une société offshore ≠ blanchiment** : optimisation fiscale légale, activité internationale justifiée, succession internationale — beaucoup de raisons légitimes à une société hors juridiction.

**Un train de vie incohérent avec le salaire déclaré ≠ fraude prouvée** : dividendes, plus-values, cadeaux familiaux, emprunts, choix de consommation spécifiques.

**La convergence fait la solidité** : patrimoine incohérent avec les revenus déclarés + sociétés offshore dans juridictions opaques + flux crypto non déclarés + mentions dans des leaks + historique de contentieux → faisceau convergent avec niveau de confiance élevé.

Le rapport distingue toujours les **signaux** (à investiguer) des **éléments corroborés** (qui peuvent fonder une conclusion). Cette discipline est éthique et juridiquement protectrice — pour l’investigateur et pour la cible.

-----

### Chapitre 19 — Crypto-actifs et blockchain : investigation OSINT

#### 19.1 Pourquoi le crypto est central en 2025-2026

Les crypto-actifs sont devenus incontournables en investigation. Plusieurs dynamiques convergent.

Les **flux illicites** passent massivement par le crypto. Ransomware, dark web, sanctions evasion, blanchiment — les estimations de Chainalysis situent entre 20 et 40 milliards de dollars de volumes illicites par an, dont la majorité en stablecoins (principalement USDT sur TRON).

La **pseudo-anonymité** du Bitcoin et de l’Ethereum les rend investigables (les transactions sont publiques) tout en créant un défi d’attribution (associer une adresse à une identité).

Les **points de dé-anonymisation** existent : les exchanges centralisés (Binance, Coinbase, Kraken) appliquent le KYC. Une adresse qui interagit avec un exchange KYC peut, sur réquisition judiciaire, être rattachée à un compte identifié. Pour l’investigateur privé, identifier ces points est souvent l’objectif central.

L’investigation OSINT crypto ne remplace pas les outils professionnels (Chainalysis Reactor, TRM Labs, Elliptic) qui offrent clustering avancé, base d’attributions, et analyses automatisées. Mais elle permet une couverture significative avec des moyens limités.

#### 19.2 Bitcoin : UTXO et explorateurs

Bitcoin fonctionne sur le modèle **UTXO** (Unspent Transaction Outputs). Chaque transaction consomme des UTXO en entrée et crée des UTXO en sortie. Les adresses contiennent des UTXO, pas des soldes au sens compte bancaire.

**Conséquence pour l’investigation** : les adresses Bitcoin sont typiquement **à usage unique** dans les bonnes pratiques. Un wallet (portefeuille) génère une nouvelle adresse à chaque réception. Plusieurs adresses appartiennent au même wallet, même s’il n’y a pas de lien direct visible.

**Explorateurs publics** :

- **Blockchain.com** (`blockchain.com`) : explorateur grand public, gratuit.
- **Blockchair** (`blockchair.com`) : interface avancée, agrège plusieurs blockchains, fonctions de recherche étendues.
- **OXT** (`oxt.me`) : explorateur avancé avec visualisation graphique, clustering heuristique — puissant pour l’investigation.
- **Mempool.space** : focalisé sur le mempool (transactions en attente).

**Consultation d’une adresse** : l’investigateur voit le solde, le nombre de transactions, la chronologie, les contreparties. Pas d’identité, mais des **patterns** (régularité, montants, interactions avec des services identifiés).

#### 19.3 Ethereum et chaînes EVM

Ethereum et les chaînes compatibles EVM (Polygon, BSC, Avalanche, Arbitrum, Optimism) fonctionnent sur un modèle **compte** (pas UTXO). Chaque adresse a un solde, et les transactions sont similaires à des virements bancaires.

**Explorateurs** :

- **Etherscan** (`etherscan.io`) : référence absolue pour Ethereum. Interface exhaustive, historique complet, détection de contrats intelligents.
- **Polygonscan, BscScan, Arbiscan, Optimistic Etherscan** : équivalents pour les autres chaînes EVM.
- **DeBank** (`debank.com`) : vue multi-chaîne par wallet, positions DeFi agrégées.

**ENS (Ethereum Name Service)** : service de nommage Ethereum — `alice.eth` pointe vers une adresse. Les ENS sont publics et recherchables. Un ENS qui correspond au nom ou au pseudo d’une cible est un pivot productif.

**Smart contracts** : interactions visibles sur Etherscan. Si la cible interagit avec un contrat DeFi (Uniswap, Aave, Compound), les flux sont traçables.

#### 19.4 Stablecoins : USDT, USDC et TRON

Les **stablecoins** (principalement USDT et USDC) représentent aujourd’hui la majorité des flux illicites crypto. USDT sur **TRON** est dominant en volume — frais très bas (quelques centimes), confirmations rapides, fonge bien dans le volume légitime important.

**Tronscan** (`tronscan.org`) : explorateur TRON, équivalent d’Etherscan pour TRON.

**Investigation typique** : un flux de USDT sur TRON part d’un wallet → passe par plusieurs adresses intermédiaires → atterrit sur un exchange KYC. Le traçage technique est identique à Ethereum (chaîne publique).

Les **émetteurs de stablecoins** (Tether pour USDT, Circle pour USDC) peuvent **geler** des fonds sur demande autorité. Un USDC gelé par Circle est une piste d’enquête — la liste des adresses gelées est partiellement publique.

#### 19.5 Pivots OSINT vers crypto

Plusieurs façons de relier une identité à une adresse crypto.

**Email lié à un exchange** : Holehe sur l’email cible révèle souvent la présence sur Binance, Coinbase, Kraken. Signal que la cible a un compte KYC sur cet exchange — point de dé-anonymisation potentiel (accessible uniquement sur réquisition, l’OSINT documente le lien, les autorités obtiennent l’identité).

**ENS associé à un nom** : si la cible a un ENS public (`marcdelaunay.eth`), toute son activité sur ce wallet est visible.

**Adresse publiée** : l’erreur OPSEC courante — la cible publie une adresse Bitcoin ou Ethereum sur son profil Telegram, Twitter, site perso, email signature, QR code. L’investigateur collecte, et toute l’activité du wallet devient traçable.

**Wallet hardware identifié par breach** : le breach Ledger 2020 confirme la détention d’un hardware wallet (donc de crypto-actifs), sans révéler les adresses directement.

**Paiements visibles** : un paiement crypto visible sur la blockchain (à un service, à une œuvre caritative, à un don public) dont la cible se vante publiquement établit le lien adresse ↔ identité.

#### 19.6 Investigation d’une adresse

Une fois une adresse identifiée comme liée à la cible, l’investigation produit :

**Analyse de volume et temporalité** : sur combien d’années l’adresse est active, quel volume total, quelle régularité des transactions.

**Contreparties identifiables** : les adresses avec lesquelles la cible interagit. Certaines sont identifiées publiquement (adresses d’exchanges, de services connus, d’ONG, de mixers).

**Patterns** : montants réguliers (revenus ?), pics épisodiques (gains d’investissement ?), sortie vers un exchange identifié (cashout ?).

**Outils d’annotation** : **Arkham Intelligence** (freemium) annote des adresses connues (exchanges, DeFi, entités publiques). **Etherscan labels** annote les adresses identifiées publiquement.

#### 19.7 Clustering basique

Les heuristiques de **clustering** permettent de regrouper des adresses appartenant au même wallet.

**Heuristique de co-spending** : si deux adresses sont inputs dans une même transaction, elles sont contrôlées par la même personne (qui possède les clés privées des deux).

**Heuristique de change** : une transaction Bitcoin typique a un input, un output vers le destinataire, et un output de « change » qui retourne à l’expéditeur (sur une nouvelle adresse générée). Identifier laquelle est le change permet d’étendre le cluster de l’expéditeur.

Ces heuristiques sont intégrées dans les outils (OXT pour Bitcoin, certains outils EVM). Elles sont **probabilistes** — elles peuvent se tromper, et les utilisateurs avertis les contournent (CoinJoin, PayJoin pour Bitcoin).

#### 19.8 Le point de dé-anonymisation : exchanges KYC

Les **exchanges centralisés KYC** sont le point où l’anonymat crypto rencontre l’identité réelle. Binance, Coinbase, Kraken, Bitstamp, et la plupart des exchanges majeurs collectent aujourd’hui une identification vérifiée (pièce d’identité, preuve de domicile, parfois preuve de fonds).

**Pour l’investigateur OSINT** : identifier qu’une chaîne de flux aboutit à un exchange KYC est souvent la conclusion actionnable — c’est là que les autorités, sur réquisition, peuvent identifier le titulaire du compte.

**Identifier les adresses d’exchanges** : bases publiques (Arkham, Etherscan labels), rapports CTI, reconnaissance de patterns (adresses stables recevant des volumes énormes, distributions régulières).

**Cashout via exchanges non-KYC** : certains exchanges restent peu ou pas KYC (petits échanges dans des juridictions opaques). Tracer vers ces exchanges diminue l’actionnabilité.

#### 19.9 Limites et opacification

Plusieurs techniques rendent le traçage plus difficile.

**Mixers / tumblers** : services qui mélangent les fonds de multiples utilisateurs pour casser la traçabilité. **Tornado Cash** (Ethereum, sanctionné en 2022), **Wasabi Wallet** (Bitcoin, CoinJoin), **Samourai Wallet** (Bitcoin, fermé en 2024 par les autorités). Le traçage au-delà d’un mixer nécessite des heuristiques probabilistes et des outils professionnels — souvent impossible en OSINT pure.

**Bridges cross-chain** : services qui transfèrent des fonds entre blockchains (Bitcoin → Ethereum → BSC → TRON). Chaque bridge complique le suivi et introduit des zones d’opacité.

**DeFi sans KYC** : Uniswap, Curve, Aave permettent de swap et lend sans identification. Traçable mais opaque d’attribution.

**Privacy coins** : Monero (XMR) est conçu pour être intraçable (transactions confidentielles, signatures de cercle, adresses furtives). Le traçage Monero est **extrêmement difficile** même pour les outils professionnels — généralement, on trace jusqu’à une conversion vers Monero, puis on perd la trace. Zcash (ZEC) a des options privacy mais est moins utilisé.

#### 19.10 Outils gratuits vs professionnels

Les outils professionnels (**Chainalysis Reactor**, **TRM Labs**, **Elliptic**, **CipherTrace**) offrent :

- Clustering avancé propriétaire.
- Base d’attributions massive (dizaines de millions d’adresses catégorisées).
- Interfaces d’investigation visuelle.
- Alertes et monitoring.

Coûts : dizaines à centaines de milliers d’euros par an. Accessibles aux LEA, grandes banques, services de conformité.

**Pour l’investigateur OSINT** : combiner les outils gratuits et freemium (explorateurs publics, OXT, Arkham, DeBank) permet une couverture significative. Les limites commencent quand on doit démêler un cluster complexe, suivre à travers un mixer, ou attribuer une adresse non identifiée publiquement.

**Règle pratique** : l’investigation OSINT trace jusqu’au point de dé-anonymisation identifiable (exchange KYC, service avec identification) et documente les limites (mixer, cross-chain, privacy coin) comme zones d’opacité à transmettre aux autorités si la mission est judiciaire.

#### 19.11 Asset recovery : workflow

Dans les missions de recouvrement d’actifs (fraude, ransomware, divorce contentieux), le workflow OSINT crypto vise à documenter les actifs et préparer les saisies.

**Étapes** :

1. Identification des adresses contrôlées par la cible (pivots OSINT → crypto).
1. Cartographie complète des flux (entrées, sorties, soldes actuels).
1. Identification des exchanges et services où des fonds sont détenus.
1. Documentation pour réquisitions (adresses, dates, volumes, exchanges cibles).
1. Transmission aux autorités (OCLCTIC pour la France, ARCOS pour le gel des avoirs numériques).

**Limites** : la saisie crypto nécessite soit l’obtention des clés privées (par perquisition ou coopération de la cible), soit le gel sur l’exchange. L’investigateur OSINT documente ; la saisie relève des autorités.

#### 19.12 Fil rouge — MIRAGE Épisode 10

> **🎯 MIRAGE — Épisode 10 : du Telegram à Binance, traçage Bitcoin**
> 
> L’investigateur mobilise toutes les sources pour la QI-3 (crypto-actifs).
> 
> **Sources de départ** :
> 
> - Holehe (Ch.6) : Delaunay présent sur Binance et Coinbase avec son email perso.
> - Breach Ledger 2020 (Ch.12) : détention confirmée d’un hardware wallet.
> - Canal Telegram « Offshore Trading Club » (Ch.8) : Delaunay/marc_offshore admin d’un canal dédié à l’optimisation fiscale crypto.
> 
> **Publication d’une adresse Bitcoin** : en remontant les messages du canal Telegram (2023), un post de `marc_offshore` mentionne « pour les tips, voici mon wallet » avec une adresse Bitcoin `bc1q...xyz` (64 caractères, format bech32). Publication publique sur le canal → utilisation légitime en investigation.
> 
> **Investigation de l’adresse sur Blockchain.com** :
> 
> - 12,4 BTC de volume total sur 18 mois.
> - 47 transactions d’entrée, 12 transactions de sortie.
> - Entrées : majoritairement petits montants (0,01 à 0,1 BTC) depuis des adresses variées — cohérent avec des tips / réception de paiements multiples.
> - Sorties : consolidation en quelques transactions vers une même adresse destination, qui après traçage mène à **Binance** (identifié via Arkham Labels).
> 
> **OXT pour le clustering** : l’heuristique de co-spending regroupe l’adresse `bc1q...xyz` avec 3 autres adresses dans le même cluster. Le cluster total : 18,7 BTC mouvementés.
> 
> **Lien adresse → Binance → identité (OSINT)** : le compte Binance associé à `marcdelaunay75@gmail.com` (Holehe) est identifié comme destinataire probable des flux. L’investigateur établit le **faisceau** :
> 
> - Email `marcdelaunay75@gmail.com` → Binance (Holehe, cotation B2)
> - Cluster Bitcoin → sortie vers Binance (OXT + Arkham, cotation B1)
> - Publication de l’adresse sur canal Telegram Delaunay (cotation A1 — capture publique)
> 
> **Conclusion OSINT** : faisceau convergent pour attribuer le cluster Bitcoin à Delaunay. La confirmation définitive (et l’accès aux détails du compte Binance) nécessite une réquisition judiciaire.
> 
> **Investigation du cluster Delta Consulting** : l’email `m.consulting@protonmail.com` (lié aux sociétés offshore, Ch.11) est aussi présent sur Binance et Coinbase. L’investigateur cherche des adresses crypto publiées pour Delta Consulting ou Delta Trading — trouvées via un post de 2022 sur le forum francophone dark web (Ch.13). Une adresse Ethereum `0xAB...` est trouvée.
> 
> **Etherscan + DeBank sur `0xAB...`** :
> 
> - Flux en USDT sur Ethereum (puis pont vers USDT TRON via un bridge — traçage partiel).
> - Environ 1,2 M USD équivalent mouvementé sur 18 mois.
> - Sortie vers un exchange non-KYC (OKX à l’époque — depuis renforcement KYC, zone grise).
> 
> **Sélecteurs ajoutés au graphe** : 1 cluster Bitcoin (4 adresses, 18,7 BTC), 1 adresse Ethereum USDT (1,2 M USD mouvementés), 2 points de dé-anonymisation identifiés (Binance France, OKX), 1 bridge cross-chain (zone d’opacité documentée).
> 
> **Faisceau pour le rapport** : QI-3 fortement corroborée — Delaunay détient et opère des crypto-actifs non déclarés, articulés avec les structures offshore identifiées.

-----

### Chapitre 20 — Workflow d’investigation financière intégrée

> **Note sur le positionnement de ce chapitre.** Ce chapitre ne re-traite pas les Ch.18 et 19. Il montre comment les **articuler** dans un workflow OSINT intégré et ramène le centre de gravité de la Partie V vers l’investigation OSINT (pas une encyclopédie financière). Volontairement court.

#### 20.1 L’articulation OSINT patrimoine + crypto + corporate

L’investigation financière par OSINT se structure en un workflow intégré qui combine les dimensions traitées séparément dans les chapitres précédents. Trois grappes d’analyse à mener en parallèle, puis à faire converger.

**Grappe 1 — Structures** (Ch.10) : cartographier les sociétés détenues, gérées, ou liées à la cible. Identifier les juridictions, les nominees, les UBO déclarés vs UBO réels probables.

**Grappe 2 — Patrimoine visible** (Ch.18) : immobilier, véhicules, biens de luxe, train de vie visible sur réseaux sociaux. Comparer avec les revenus déclarés (quand accessibles — comptes publiés, déclarations TVA, cotations boursières).

**Grappe 3 — Crypto** (Ch.19) : adresses identifiées, flux, points de dé-anonymisation, volumes estimés.

L’investigateur construit ces trois grappes **simultanément**, car chacune enrichit les autres : une société identifiée révèle des dirigeants qui peuvent avoir des wallets crypto ; un wallet crypto interagit avec un service qui est relié à une société ; une propriété immobilière est détenue via une SCI qui révèle un réseau familial.

#### 20.2 Le graphe patrimonial intégré

Le **graphe patrimonial** visualise dans Maltego (ou équivalent) l’ensemble des entités identifiées et leurs relations. Entités typiques : personnes, sociétés, adresses crypto, propriétés immobilières, comptes bancaires (identifiés partiellement), véhicules, domaines, emails.

Relations : contrôle (UBO), détention (actionnariat), flux (paiement tracé), cohabitation (adresse commune), lien familial, lien professionnel.

La lecture du graphe révèle les **grappes denses** (concentrations d’activité suggérant une structure), les **nœuds centraux** (entités pivots dans le montage), et les **chemins de flux** (de TechnoVert à Binance via Delta Consulting et un cluster Bitcoin).

#### 20.3 Cohérence patrimoine / revenus / flux

Le test analytique central de l’investigation patrimoniale est le test de cohérence.

**Revenus déclarés** (salaire TechnoVert + éventuels dividendes de sociétés : via Pappers, recherche du rôle de Delaunay dans les sociétés déclarées) → ordre de grandeur des revenus annuels légitimes.

**Patrimoine visible** (immobilier via SCI, train de vie Instagram, voyages) → ordre de grandeur du patrimoine et du niveau de dépense.

**Flux crypto identifiés** (cluster Bitcoin 18,7 BTC + 1,2 M USD équivalent stablecoins) → volumes additionnels non déclarés fiscalement.

**L’écart entre les trois** construit le signal. Un DAF déclarant 150 k€/an de revenus bruts, avec un patrimoine immobilier apparent de 2 M€ + des actifs crypto traçables de 1,5 M€ + un train de vie (voitures de luxe, voyages, restaurants), présente une incohérence que seule une justification claire (héritage documenté, activité annexe déclarée) peut résoudre.

#### 20.4 Les schémas typiques

Plusieurs schémas récurrents sont utiles à connaître.

**Schéma 1 — Surfacturation via société offshore** : la cible orchestre, via sa position dans une société française, des contrats de « consulting » ou de « prestations » vers une société offshore qu’elle contrôle indirectement. Les fonds sortent légalement (facture acceptée, paiement tracé) et atterrissent sur une structure qui n’est pas connectable à la cible dans les registres ouverts. Schéma MIRAGE probable.

**Schéma 2 — Cashout crypto** : les fonds étrangers sont convertis en crypto via un exchange (centralisé KYC, mais sur une identité différente — parfois un nominee, parfois une société), puis mixés ou transférés vers un autre exchange où ils sont convertis et retirés.

**Schéma 3 — Trust multi-juridictions** : la cible établit un trust dans une juridiction opaque (BVI, Jersey, Cayman), trust qui détient des sociétés dans d’autres juridictions, qui possèdent les actifs réels. Opaque même pour les autorités sans coopération internationale.

**Schéma 4 — Holding familial + SCI** : usage combiné d’une holding et de SCI familiales pour détenir les actifs patrimoniaux, avec des flux entre les structures qui permettent de sortir les revenus du patrimoine imposable.

Chaque schéma a ses signaux et ses parades. L’investigateur expérimenté reconnaît rapidement le schéma auquel il a affaire, ce qui oriente la collecte.

#### 20.5 Production du rapport patrimonial

Le livrable d’une investigation patrimoniale OSINT contient typiquement :

- **Sommaire exécutif** : conclusion en une page — schéma identifié, cotation du patrimoine non déclaré estimé, recommandations (dépôt de plainte, réquisitions prioritaires).
- **Cartographie structurelle** : graphe des entités, légendes, cotations de fiabilité par branche.
- **Analyse des flux** : chronologie des flux principaux, points de sortie, zones d’opacité identifiées.
- **Analyse de cohérence** : comparaison patrimoine / revenus / train de vie avec conclusion quantitative.
- **Pistes de réquisitions** : exchanges à réquisitionner, registres étrangers à solliciter, parties à entendre.
- **Annexes** : toutes les sources cotées, les captures hashées, les listes d’adresses crypto, les références de leaks ICIJ.

#### 20.6 Fil rouge — MIRAGE Épisode 11

> **🎯 MIRAGE — Épisode 11 : reconstitution du schéma complet**
> 
> L’investigateur consolide les trois grappes à mi-parcours de l’enquête.
> 
> **Structures identifiées** : Delta Consulting Ltd (Malte), Delta Trading Ltd (Malte), DT Investments S.à r.l. (Luxembourg), deux nominees (Joseph Borg, Jean Petit), une SCI familiale (SCI Delaunay Patrimoine, France, 1,2 M€ d’actifs immobiliers).
> 
> **Patrimoine visible** : résidence principale Levallois-Perret (via SCI Delaunay Patrimoine, Pappers), train de vie élevé (forum voitures de luxe, Instagram voyages récurrents à Malte et Dubaï), voyages réguliers détectés via posts Instagram et GHunt (avis Google Maps La Valette).
> 
> **Crypto** : cluster Bitcoin 18,7 BTC (~800 k€ au cours 2024), adresse Ethereum 1,2 M USD USDT mouvementés, 2 comptes exchanges KYC (Binance, Coinbase) + 1 compte exchange moins KYC (OKX).
> 
> **Cohérence** :
> 
> - Revenus déclarés (estimation DAF ETI : ~180 k€/an brut + dividendes éventuels TechnoVert) → ~1,5 M€ sur 8 ans.
> - Patrimoine visible : 1,2 M€ immobilier + estimation train de vie 50 à 80 k€/an = ~1,6-1,8 M€ cumulé.
> - Crypto tracé : ~2 M€ équivalents mouvementés (non nécessairement conservés, mais passés entre les mains).
> - Sociétés offshore : flux estimables à plusieurs centaines de milliers d’euros par an via les chevauchements TechnoVert/Delta Consulting.
> 
> **Conclusion de cohérence** : les revenus déclarés ne suffisent pas à expliquer le patrimoine + le train de vie + les flux crypto. Hypothèse dominante : Delaunay détourne des fonds via les structures offshore (surfacturation de « consulting » de TechnoVert vers Delta Consulting, flux crypto pour le cashout, patrimoine partiellement immobilisé dans la SCI française pour donner l’apparence de moyens limités).
> 
> **Pistes de réquisitions pour le cabinet Legrand & Associés** :
> 
> 1. Réquisition Binance (identité du titulaire du compte lié à `marcdelaunay75@gmail.com`, historique des transactions).
> 1. Réquisition Coinbase (même).
> 1. Réquisition OKX (coopération à tester, juridiction Seychelles).
> 1. Coopération internationale avec autorités maltaises pour Delta Consulting et Delta Trading (via JUNALCO ou PNF).
> 1. Coopération luxembourgeoise pour DT Investments.
> 1. Expertise comptable de TechnoVert pour identifier les factures de « consulting » vers Delta Consulting.
> 1. Vérification fiscale (déclarations crypto dans l’IR de Delaunay).
> 
> **Le rapport préliminaire est produit** pour le cabinet, qui le transmet au PNF et saisit le C3N pour le volet désinformation.

-----

## PARTIE VI — ANALYSE, VÉRIFICATION ET PRODUCTION

> **Ce que cette partie apprend.** Raisonner de manière structurée (ACH, gestion des biais, pensée adversaire), coter rigoureusement la fiabilité des sources et la crédibilité des informations, rédiger un rapport d’investigation exploitable, et articuler le cadre judiciaire avec la transmission et la veille post-rapport.
> 
> **Ce qu’elle ne couvre pas.** Le reporting exécutif en gestion de crise (champ voisin mais distinct), la contradiction juridique formelle (expertise judiciaire approfondie — le cours pose les jalons, pas la profession entière).
> 
> **Ce que vous saurez faire après cette partie.** Construire une matrice ACH sur un cas complexe, éviter les biais cognitifs dominants, coter chaque fait avec Admiralty, rédiger un rapport OSINT calibré pour un cabinet d’avocats ou des autorités, et gérer la transmission et la veille post-rapport.

-----

### Chapitre 21 — Analyse structurée : ACH, biais et raisonnement adversaire

#### 21.1 De la donnée au renseignement : la valeur ajoutée de l’analyse

Toutes les phases précédentes (collecte, traitement, corrélation) produisent un **dossier de données**. La transformation en **renseignement** se joue dans l’analyse. Sans analyse, un dossier même riche reste inutilisable pour la décision.

L’analyse répond à trois questions successives :

- Que signifient ces données, prises ensemble ?
- Quel est le niveau de confiance de cette interprétation ?
- Quelles actions ou décisions peuvent s’appuyer sur cette conclusion ?

Une investigation MIRAGE qui produit 200 captures et 50 entités dans un graphe, sans analyse structurée, ne permet pas au cabinet Legrand & Associés de décider. Une investigation qui conclut « faisceau convergent pour un schéma de détournement par surfacturation offshore, confiance modérée à élevée, justifiant un dépôt de plainte + réquisitions prioritaires » permet la décision.

#### 21.2 ACH (Analysis of Competing Hypotheses) appliqué à l’OSINT

L’**ACH** (Richards Heuer, CIA, 1999) est la technique analytique la plus utile pour l’investigateur OSINT. Elle force à tester plusieurs hypothèses contre les mêmes évidences, plutôt que de construire un raisonnement qui conforte l’hypothèse initiale.

**Méthodologie ACH** :

**Étape 1 — Lister les hypothèses concurrentes** : au minimum 3 hypothèses, incluant les alternatives « non suspectes ». Pour MIRAGE :

- H1 — Delaunay détourne des fonds de TechnoVert via le réseau de sociétés offshore (schéma frauduleux).
- H2 — Delaunay fait de l’optimisation fiscale agressive mais légale (structures internationales légitimes).
- H3 — Delaunay opère une activité de conseil indépendante en parallèle, légalement déclarée ailleurs (cumul d’emplois autorisé par son contrat).
- H4 — Les flux observés concernent des activités légitimes dont Delaunay est l’intermédiaire sans être le bénéficiaire final (nominee lui-même pour un tiers).

**Étape 2 — Lister les évidences** : tous les faits collectés pendant l’investigation, cotés selon Admiralty (Ch.22).

**Étape 3 — Construire la matrice ACH** : un tableau avec les évidences en lignes, les hypothèses en colonnes. Pour chaque évidence et chaque hypothèse, noter : **Cohérent (C)**, **Incohérent (I)**, **Non applicable (N)**.

**Étape 4 — Éliminer les hypothèses avec le plus d’incohérences** : contrairement à l’intuition, l’ACH cherche l’hypothèse **la moins incohérente**, pas la plus cohérente. Une hypothèse cohérente avec toutes les preuves est potentiellement triviale (explique trop). Une hypothèse qui a peu d’incohérences est la plus solide.

**Étape 5 — Évaluer la confiance** : confiance élevée si l’hypothèse retenue a peu d’incohérences et les alternatives en ont beaucoup. Confiance modérée si plusieurs hypothèses restent plausibles. Confiance faible si aucune hypothèse ne domine clairement.

#### 21.3 Construction de la matrice ACH pour MIRAGE

Exemple partiel de matrice ACH appliquée au cas Delaunay :

|Évidence                                          |Cote|H1 Détournement|H2 Optimisation légale|H3 Activité annexe|H4 Nominee lui-même|
|--------------------------------------------------|----|:-------------:|:--------------------:|:----------------:|:-----------------:|
|Chaîne Malte-Lux-Chypre via nominees              |A1  |C              |C                     |C                 |C                  |
|Flux TechnoVert → Delta Consulting non justifiés  |B2  |C              |I                     |I                 |C                  |
|Pas de déclaration annexe d’activité indépendante |A1  |C              |I                     |**I**             |C                  |
|Crypto non déclaré fiscalement                    |B2  |C              |I                     |C                 |C                  |
|Patrimoine > revenus déclarés                     |A2  |C              |I                     |I                 |C                  |
|Tentative de faux alibi (photo synthétique)       |B2  |**C**          |**I**                 |**I**             |I                  |
|Canal Telegram « Offshore Trading Club »          |A1  |C              |C                     |C                 |C                  |
|Campagne de désinformation contre lanceur d’alerte|B2  |C              |I                     |I                 |I                  |

**Lecture** : H2 a de multiples incohérences (les flux non justifiés + pas de déclaration annexe + patrimoine > revenus + faux alibi + désinformation ne s’expliquent pas par une optimisation fiscale légale). H3 est éliminée par l’absence de déclaration d’activité annexe. H4 est éliminée par le faux alibi (un simple nominee n’aurait pas à fabriquer d’alibi).

**H1 domine** : cohérente avec toutes les évidences disponibles. Confiance **élevée** sur la conclusion « schéma de détournement », confiance **modérée** sur les modalités précises (la surfacturation est plausible mais d’autres mécanismes pourraient coexister).

#### 21.4 Les biais cognitifs à neutraliser

L’investigateur, comme tout humain, est soumis à des biais cognitifs qui déforment son analyse. Les connaître permet de les neutraliser.

**Biais de confirmation** : tendance à chercher et retenir les informations qui confirment l’hypothèse initiale, et à ignorer celles qui la contredisent. **Parade** : formuler l’hypothèse initiale, puis **chercher activement** les faits qui la contrediraient.

**Biais d’ancrage** : la première information reçue pèse trop dans l’évaluation ultérieure. **Parade** : reformuler régulièrement la synthèse à partir de toutes les évidences, pas à partir de l’évidence initiale.

**Biais de disponibilité** : on surestime l’importance des éléments facilement accessibles en mémoire (dernière information lue, cas médiatisé). **Parade** : travailler avec le journal d’investigation et le graphe, pas avec la mémoire.

**Effet de halo** : un suspect perçu comme coupable sur un point est suspecté de tout. Un suspect qui ment sur un fait ne ment pas nécessairement sur tous. **Parade** : chaque fait est analysé pour lui-même.

**Sunk cost fallacy** : plus l’investigateur a investi de temps, plus il a tendance à conclure dans le sens qui justifie cet investissement. **Parade** : accepter qu’une investigation puisse conclure « pas assez d’éléments pour conclure » — ce n’est pas un échec, c’est une conclusion honnête.

**Groupthink** : en équipe, tendance à converger vers l’opinion dominante sans débat critique. **Parade** : désigner un « devil’s advocate » qui doit défendre une hypothèse alternative.

**Biais culturel** : projeter ses propres références culturelles sur des contextes étrangers. Un investigateur français enquêtant sur un dirigeant chinois ne doit pas projeter les codes français sur des pratiques locales différentes.

#### 21.5 La discipline de l’hypothèse alternative

L’**hypothèse alternative** est la pratique quotidienne qui neutralise le biais de confirmation. À chaque conclusion partielle, l’investigateur se pose la question : **« qu’est-ce qui invaliderait cette conclusion ? »**

Pour MIRAGE : la conclusion « Delaunay contrôle Delta Consulting » pourrait être invalidée par :

- Un document prouvant que Delta Consulting a été créée avant que Delaunay ne rejoigne TechnoVert, et qu’elle est détenue par un tiers sans lien avec lui.
- Une déclaration fiscale où Delaunay déclare son rôle dans Delta Consulting (optimisation légale).
- Une identification du véritable UBO qui serait un autre individu, avec Delaunay comme simple opérateur local.

L’investigateur cherche ces faits invalidants. S’il ne les trouve pas, la conclusion se consolide. S’il en trouve, la conclusion doit être nuancée ou révisée.

Cette discipline est épuisante — elle force à contredire son propre travail. Elle est ce qui distingue l’analyste du simple collecteur.

#### 21.6 Raisonnement adversaire

Le **raisonnement adversaire** consiste à se mettre à la place de la cible : « qu’est-ce qu’elle voudrait que je croie ? », « comment aurait-elle orchestré les traces que je vois si elle cherchait à me tromper ? ».

Pour MIRAGE : la photo « alibi » à Genève (Ch.17 Épisode 9) est précisément ce qu’un adversaire aurait produit s’il voulait créer un alibi pour le jour d’une transaction suspecte. La détection de la fabrication est un indice **renforçant** plutôt qu’affaiblissant le schéma frauduleux : la cible se donne la peine de fabriquer un alibi, donc elle a quelque chose à cacher.

Le raisonnement adversaire est aussi utile pour **anticiper** : si la cible découvre l’investigation, qu’est-ce qu’elle va faire ? (Supprimer des comptes, dissoudre des sociétés, transférer les crypto, menacer l’investigateur, déposer une plainte pour diffamation préventive.) Cette anticipation permet de préserver les preuves (archivage anticipé) et de se protéger (documentation stricte, OPSEC renforcée).

#### 21.7 Timeline et chronologie

La **chronologie** est un outil analytique sous-estimé. Organiser les événements datés dans l’ordre temporel révèle des corrélations invisibles dans l’analyse par entité.

Pour MIRAGE : la création de Delta Consulting Ltd en mars 2018, la prise de poste de Delaunay chez TechnoVert en octobre 2019, les premiers flux entre les deux en janvier 2020, le renforcement du patrimoine crypto en 2022-2023, le licenciement du lanceur d’alerte en juillet 2025, la photo « alibi » en février 2026 — alignés sur une timeline, ils dessinent l’histoire d’un schéma évolutif.

Outils : **Aeon Timeline**, **Timeline Explorer**, **Excel avec graphique temporel**. L’objectif n’est pas l’esthétique mais la révélation de patterns temporels (concentrations d’événements, séquences causales, corrélations avec des événements externes).

#### 21.8 Les pièges classiques

**Confondre corrélation et causalité** : la présence simultanée de deux faits ne signifie pas que l’un cause l’autre. Les flux vers Delta Consulting et l’enrichissement crypto de Delaunay sont corrélés ; l’investigation doit établir le mécanisme causal (ou s’abstenir de conclure).

**Confondre absence de preuve et preuve d’absence** : « aucune déclaration fiscale d’activité annexe trouvée » ne signifie pas « aucune activité annexe » — la déclaration pourrait exister dans un régime que l’OSINT ne couvre pas. La formulation correcte : « aucune activité annexe déclarée publiquement identifiée ».

**Sur-interprétation** : conclure sur un signal isolé ce qui nécessiterait un faisceau. Un forum Voitures de Luxe ne prouve pas un train de vie incohérent — il faut le combiner avec d’autres indices (photos, transactions, posts explicites).

**Sous-interprétation** : ignorer un signal faible qui, combiné avec d’autres, serait significatif. Les signaux faibles (comptes sur un exchange, mention Malte sur un forum, photo avec un détail) deviennent productifs quand ils sont corrélés.

-----

### Chapitre 22 — Cotation de fiabilité et niveaux de confiance

#### 22.1 Pourquoi coter chaque fait

Un rapport OSINT sans cotation est un rapport sans rigueur. La cotation structure la communication analytique de plusieurs façons.

**Discriminer les niveaux de certitude** : tous les faits ne se valent pas. Un extrait Pappers est infiniment plus fiable qu’un post anonyme sur un forum. Présenter les deux au même niveau dans un rapport désoriente le lecteur.

**Permettre la pondération** : le décideur (cabinet, magistrat, RSSI) peut prendre une décision appropriée selon la solidité de chaque élément. Une décision lourde (dépôt de plainte, action en justice) exige une solidité élevée. Une décision exploratoire (réquisition complémentaire, surveillance) peut s’appuyer sur des éléments de cotation moyenne.

**Protéger l’investigateur** : un rapport qui présente comme certaines des informations en réalité douteuses expose l’investigateur à des reproches si les faits se révèlent faux. Un rapport qui cote prudemment protège.

**Discipliner l’analyse** : l’obligation de coter force à réfléchir à la source et à l’information plutôt qu’à les accepter comme naturellement fiables.

#### 22.2 La grille Admiralty A-F / 1-6

Le **code Admiralty** (ou NATO system) est la grille standard utilisée par les services d’intelligence et les CERT. Elle combine deux dimensions indépendantes.

**Fiabilité de la source** :

- **A — Totalement fiable** : source avec un historique de fiabilité démontré dans le temps, généralement une autorité officielle (registre légal, publication d’État). Exemple : Infogreffe, Companies House, gouvernement français officiel.
- **B — Habituellement fiable** : source éprouvée mais pouvant occasionnellement être en erreur. Exemple : grands médias (Le Monde, Reuters), services CTI professionnels (Mandiant, CrowdStrike reports publics), LinkedIn pour les données corporate.
- **C — Assez fiable** : source dont la fiabilité est moyenne, documentée partiellement. Exemple : bases commerciales non-officielles (Hunter.io, OpenCorporates pour certaines juridictions), Pappers pour les données enrichies non-officielles.
- **D — Pas toujours fiable** : source dont les erreurs sont fréquentes mais qui reste occasionnellement utile. Exemple : forums spécialisés, reconnaissance faciale automatique.
- **E — Peu fiable** : source généralement inexacte ou fortement biaisée. Exemple : certains agrégateurs de données personnelles, sites de rumeurs.
- **F — Fiabilité inconnue** : source nouvelle ou pas encore évaluée. Par défaut pour toute source rencontrée pour la première fois.

**Crédibilité de l’information** :

- **1 — Confirmée par d’autres sources** : l’information est indépendamment confirmée par au moins une autre source.
- **2 — Probablement vraie** : cohérente avec les autres informations disponibles, plausible.
- **3 — Possiblement vraie** : ni clairement cohérente ni clairement incohérente avec le reste.
- **4 — Douteuse** : incohérente avec d’autres informations, ou peu plausible.
- **5 — Improbable** : fortement incohérente ou peu crédible.
- **6 — Crédibilité impossible à juger** : pas assez de contexte pour évaluer.

Un fait est coté par une combinaison lettre + chiffre : A1 (top), A2, B1, B2, C3, D4, F6 (bottom).

#### 22.3 Comment coter en pratique

L’exercice semble abstrait mais devient rapide avec la pratique. Quelques repères.

**Exemples de cotation B2** : « Marc Delaunay est DAF de TechnoVert depuis 2019 » — source LinkedIn (B), information probablement vraie et cohérente avec le communiqué de nomination trouvé dans la presse (2). Coté B2.

**Exemples de cotation A1** : « Delta Consulting Ltd est enregistrée à Malte depuis mars 2018 avec Joseph Borg comme dirigeant » — source registre maltais (A), information confirmée par l’enregistrement officiel (1). Coté A1.

**Exemples de cotation C3** : « L’utilisateur `delta_mt` sur un forum francophone dark web semble avoir un style d’écriture cohérent avec celui de `marc_offshore` sur Telegram » — source forum + analyse stylométrique légère (C), information possiblement vraie mais non confirmée (3). Coté C3.

**Exemples de cotation D4** : « Un match PimEyes entre la photo de profil Google de Delaunay et un profil de site de rencontres ‘Marco D., 48 ans, Paris’ » — reconnaissance faciale (D, peu fiable), non corroboré indépendamment (4). Coté D4 jusqu’à corroboration.

**Piège de la cotation** : la tentation de coter à la hausse parce qu’une information « semble évidente ». La photo synthétique de Delaunay, analysée via ELA + cohérence des ombres + météo archivée, est-elle cotée A1 ? Non — l’analyse technique reste probabiliste, l’investigateur ne dispose pas du négatif original. Cotation prudente B2 voire C2.

**Piège inverse** : coter systématiquement à la baisse par sur-prudence. Une donnée issue d’un registre officiel ET corroborée par une autre source officielle ne mérite pas une cotation prudente — elle est A1 et c’est l’honnêteté qui l’exige.

#### 22.4 Words of Estimative Probability (WEP)

La cotation par fait est complétée par un **niveau de confiance global** sur la conclusion, exprimé en langage calibré (WEP, Words of Estimative Probability).

La grille standard (Kent / CIA, utilisée également par l’ENISA et les services occidentaux) :

|Expression                                    |Probabilité|
|----------------------------------------------|-----------|
|Almost certain / Quasi-certain                |>95 %      |
|Very likely / Très probable                   |80-95 %    |
|Likely / Probable                             |55-80 %    |
|Roughly even chance / Probabilité indéterminée|45-55 %    |
|Unlikely / Improbable                         |20-45 %    |
|Very unlikely / Très improbable               |5-20 %     |
|Almost certainly not / Quasi-certainement non |<5 %       |

**Usage** : la conclusion principale d’un rapport est formulée dans ce vocabulaire calibré. « L’analyse rend très probable le schéma de détournement par surfacturation offshore » est plus précis et plus honnête que « Delaunay détourne des fonds ».

L’investigateur évite les formulations de verdict (« il est coupable », « il est prouvé que ») qui excèdent le cadre du renseignement et peuvent exposer juridiquement.

#### 22.5 Distinguer piste, indice, élément corroboré, fait établi

Terminologie progressive à maîtriser.

**Piste** : un signal unique, non vérifié, digne d’investigation. Exemple : un username qui correspond à la cible sur une plateforme obscure. Cotation typique D3 à F6.

**Indice** : un signal vérifié dans sa réalité matérielle (la capture existe, la source est documentée), mais pas corroboré par une source indépendante. Cotation typique C3 à D3.

**Élément corroboré** : un signal confirmé par au moins une source indépendante. Cotation typique B2 à C2.

**Fait établi** : un signal confirmé par deux sources indépendantes ou plus, typiquement officielles. Cotation typique A1 à B1.

Cette progression doit apparaître dans le rapport. Un bon rapport distingue systématiquement « les faits établis sont… », « les éléments corroborés sont… », « les pistes qui nécessitent investigation complémentaire sont… ». Cette structuration protège l’investigateur et aide le décideur.

#### 22.6 La règle des 2+ sources indépendantes

La **corroboration indépendante** est le test de solidité. Un fait n’est véritablement établi que si au moins deux sources indépendantes le confirment.

**Indépendance** : deux articles de presse qui citent la même source ne sont pas indépendants. Deux enregistrements Companies House et Pappers sur la même société, dérivés des mêmes registres, ne sont qu’une source. L’indépendance suppose des origines distinctes.

**Convergence** : un fait confirmé par LinkedIn + un article de presse + le registre officiel = trois sources indépendantes, haute solidité.

**Règle pragmatique** : pour les faits critiques du rapport (ceux sur lesquels une décision lourde va s’appuyer), exiger au moins deux corroborations indépendantes. Pour les faits d’appoint (contexte, arrière-plan), une source bien cotée peut suffire avec mention de la corroboration manquante.

#### 22.7 Communiquer l’incertitude au client

Le rapport doit transmettre les niveaux de confiance au client sans jargon excessif.

**Vocabulaire calibré** : « il est quasi-certain que… », « il est très probable que… », « les éléments disponibles suggèrent que… », « l’hypothèse la plus plausible est… ». Éviter absolument : « il est démontré que… », « il est certain que… », « il est prouvé que… » sauf pour les faits de cotation A1 à plusieurs sources convergentes.

**Encadrés d’incertitude** : pour les zones d’investigation où l’incertitude est forte, un encadré explicite. « Zone d’incertitude : l’identification de Joseph Borg comme nominee de Delta Consulting repose sur un pattern (présence dans 80+ sociétés maltaises) plutôt que sur une preuve directe. La confiance sur son statut de nominee est forte ; l’identification du bénéficiaire réel derrière Borg nécessiterait une coopération maltaise. »

**Recommandations proportionnées** : les recommandations d’action (réquisitions, plaintes, mesures) sont calibrées sur le niveau de confiance. On ne recommande pas une plainte au pénal sur des éléments de cotation C3. On recommande une investigation complémentaire ciblée.

-----

### Chapitre 23 — Rédaction du rapport d’investigation OSINT

#### 23.1 Structure du rapport professionnel

Le rapport OSINT professionnel suit une structure type qui facilite la lecture et l’exploitation. L’ordre des sections est standardisé.

**1. Sommaire exécutif** (1-2 pages) : la conclusion en haut, pour le décideur pressé.

**2. Mandat et périmètre** : pourquoi cette investigation, qui l’a commandée, quelles questions, quelles contraintes.

**3. Méthodologie et sources** : comment l’investigation a été menée, quelles catégories de sources mobilisées, quelle OPSEC.

**4. Constatations** : tous les faits établis, indices et pistes, avec leur cotation.

**5. Analyse** : ACH, timeline, raisonnement, biais identifiés et neutralisés.

**6. Conclusions** : réponse structurée aux questions d’investigation, avec niveaux de confiance.

**7. Recommandations** : actions à envisager, pistes de réquisitions, suites possibles.

**8. Annexes** : captures hashées, graphe complet, chronologie détaillée, liste des sources.

Cette structure sert autant le cabinet d’avocats qui exploite le rapport qu’un juge qui le versera au dossier. Elle est l’attendu professionnel standard.

#### 23.2 Le sommaire exécutif (la page qui compte)

Le **sommaire exécutif** est la page que tout le monde lit. Si elle n’est pas claire, le reste du rapport est mal exploité, quelle que soit sa qualité.

**Structure type** (1 page) :

- **Contexte** (3 lignes) : mandat, cible, questions principales.
- **Résultats clés** (5-7 points) : les conclusions majeures, chacune avec son niveau de confiance (WEP).
- **Schéma identifié** (2-3 lignes) : la structure d’ensemble révélée par l’investigation.
- **Évaluation quantitative** si applicable : patrimoine non déclaré estimé, volume de flux identifié, etc.
- **Recommandations principales** (3-5 points) : les actions à entreprendre en priorité.

**Ton** : factuel, calibré, sans effet de style. Le décideur veut de la clarté, pas de la littérature.

**Auto-contenu** : le sommaire exécutif doit être compréhensible sans lire le reste du rapport. Un associé de cabinet le lit le matin, fait l’orientation stratégique, et délègue la lecture approfondie.

#### 23.3 Les constatations cotées

Chaque fait présenté dans le rapport porte une cotation et une source. Format type :

```
FAIT 27 — Delta Consulting Ltd est détenue à 100 % par DT Investments S.à r.l.
(Luxembourg), elle-même détenue à 99 % par Delta Holding Ltd (BVI, bénéficiaire
non identifié dans les registres publics BVI).
Source : Registre maltais (A) + Registre luxembourgeois RCS (A) + ICIJ Offshore
Leaks Database (A, Pandora Papers).
Cotation : A1 (triple source officielle, convergentes).
Capture : 20260412_Pappers_DeltaConsulting_Ownership.pdf (SHA-256: 4d8f2a...)
Commentaire : la chaîne aboutit dans une juridiction opaque (BVI) où l'UBO n'est
pas identifiable sans coopération des autorités locales.
```

Cette forme structurée permet au lecteur de vérifier chaque élément et de pondérer.

#### 23.4 Le graphe relationnel

Le **graphe relationnel** est la représentation visuelle de l’investigation. Maltego est l’outil de référence mais d’autres alternatives existent (yEd, Gephi, Neo4j, ou simplement un schéma construit dans un outil de visualisation).

**Bonnes pratiques** :

- **Légende claire** : code couleur par type d’entité (personnes en vert, sociétés en bleu, adresses crypto en orange, etc.).
- **Hiérarchie visuelle** : les entités centrales sont plus grosses ou placées centralement.
- **Annotations** : les relations sont annotées (« dirigeant », « actionnaire », « flux 2022-2024 », « nominee »).
- **Simplification** : un graphe avec 500 entités est illisible. Pour le rapport, produire une version simplifiée (20-40 entités principales) et mettre le graphe complet en annexe.
- **Hashé et horodaté** : comme les autres pièces, pour la chaîne de custody.

Un bon graphe **communique** plus efficacement que 10 pages de texte. Il est souvent le premier élément que le décideur examine après le sommaire exécutif.

#### 23.5 La timeline annotée

La **timeline** (chronologie) est le second outil de visualisation majeur. Elle révèle les patterns temporels invisibles dans l’analyse par entité.

**Niveaux de timeline** : une timeline principale qui couvre toute l’investigation (éventuellement plusieurs années), et des timelines zoomées sur des périodes clés (le mois du dépôt d’une plainte, la semaine d’une transaction suspecte).

**Types d’événements à inclure** : créations et dissolutions de sociétés, changements de dirigeants, flux financiers identifiés, événements de vie de la cible (voyages, publications), événements externes significatifs (changement de réglementation, actualité de secteur).

Outils : Aeon Timeline (spécialisé, payant), Timeline Explorer (gratuit), ou une simple feuille Excel avec graphique temporel.

#### 23.6 Vocabulaire calibré et formulations à éviter

Le **vocabulaire** du rapport reflète la rigueur analytique.

**Formulations recommandées** :

- « Les éléments sont compatibles avec… »
- « L’hypothèse la plus probable est… »
- « Les flux observés suggèrent… »
- « Aucun élément disponible ne permet de conclure… »
- « Les corroborations indépendantes établissent… »

**Formulations à éviter** :

- « Il est prouvé que… » (réservé aux faits A1 multi-sources).
- « La cible est coupable de… » (langage de verdict — outrepasse le cadre du renseignement).
- « La cible a menti sur… » (affirmation intentionnelle invérifiable — préférer « les déclarations publiques de la cible sont incohérentes avec les éléments suivants »).
- « Manifestement… », « à l’évidence… », « sans aucun doute… » (effets rhétoriques qui trahissent un manque de rigueur).

Le ton calibré **protège** l’investigateur juridiquement et renforce sa crédibilité professionnelle.

#### 23.7 Les annexes

Les **annexes** sont le réceptacle des preuves brutes. Elles doivent être organisées pour permettre la vérification par un tiers (contradicteur, magistrat, expert).

**Annexes typiques** :

- **Liste complète des sources** avec URLs, dates de consultation, hashes.
- **Captures hashées** organisées par thème et horodatées.
- **Graphe complet** (pas la version simplifiée du corps du rapport).
- **Timeline détaillée**.
- **Extraits de registres** en version complète (pas seulement la partie citée).
- **Méthodologie détaillée** (outils, versions, paramètres utilisés).
- **Journal d’investigation** ou ses extraits pertinents.

Volume typique des annexes : souvent plus volumineux que le corps du rapport. Elles ne sont pas lues linéairement mais consultées ponctuellement.

#### 23.8 Documenter les limites et incertitudes

Un rapport professionnel **documente explicitement** ses limites. Cette pratique est ce qui distingue un rapport sérieux d’un rapport commercial.

**Zones d’incertitude à documenter** :

- **Juridictions non couvertes** : « L’investigation n’a pas pu identifier le bénéficiaire effectif derrière Delta Holding Ltd (BVI) sans coopération des autorités des Îles Vierges britanniques. »
- **Sources non accessibles** : « Les comptes bancaires des sociétés offshore ne sont pas accessibles sans réquisition judiciaire. L’investigation OSINT permet d’identifier les flux extérieurs (entrées et sorties), pas les flux intra-offshore. »
- **Limites temporelles** : « L’investigation a été menée du [date] au [date]. Les évolutions postérieures ne sont pas couvertes. »
- **Limites de la cotation** : « Les éléments cotés D3 ou inférieurs sont présentés à titre d’orientation et n’ont pas le niveau de solidité requis pour fonder une décision judiciaire isolée. »
- **Alternatives non invalidées** : les hypothèses alternatives qui n’ont pas pu être formellement écartées.

Cette transparence sur les limites **renforce** la crédibilité du rapport plutôt que de l’affaiblir.

#### 23.9 Faire valider le rapport

Idéalement, un rapport important passe par une **revue par pair** avant transmission. Un collègue ou un contradicteur interne relit le rapport et teste ses conclusions.

**Questions à poser en revue** :

- Les conclusions sont-elles cohérentes avec les évidences citées ?
- Les hypothèses alternatives sont-elles documentées et évaluées ?
- Les cotations sont-elles justes ou sur/sous-évaluées ?
- Y a-t-il des biais visibles dans l’analyse ?
- Les formulations respectent-elles le vocabulaire calibré ?
- Les limites sont-elles suffisamment documentées ?
- Un contradicteur pourrait-il démonter facilement le rapport ?

La revue par pair est la dernière ligne de défense avant que le rapport ne quitte le bureau de l’investigateur. Pour les missions isolées où la revue est impossible, l’investigateur peut au moins se relire à 48 heures d’intervalle avec un œil de contradicteur.

-----

### Chapitre 24 — Cadre judiciaire, transmission et veille post-rapport

> **Note sur ce chapitre.** Volontairement recentré sur quatre volets : cadre judiciaire, transmission, expertise, veille post-rapport. Le volet « coordination d’équipe sur investigation longue » est sorti — c’est de la gestion de projet, pas de la méthodologie OSINT.

#### 24.1 Investigateur privé vs LEA : qui peut faire quoi

La distinction fondamentale structure la transmission de l’investigation.

L’**investigateur privé** mène l’investigation en sources ouvertes, produit un rapport, mais n’a **aucun pouvoir d’enquête formel** : pas de réquisition, pas d’interception, pas de perquisition, pas d’audition sous serment, pas de gel d’actifs.

Les **LEA** (C3N, OCLCTIC, JUNALCO, BL2C, PNF, TRACFIN, etc.) disposent de ces pouvoirs, sous le contrôle d’un magistrat. Leur engagement nécessite soit une plainte, soit une saisine d’autorité administrative, soit une initiative propre du parquet.

Le rapport OSINT sert à **orienter l’engagement des LEA** : il identifie les pistes, justifie la proportionnalité des moyens à engager, et prépare le travail des enquêteurs. Un rapport bien fait divise par deux le temps des premières semaines d’enquête judiciaire.

#### 24.2 La transmission au client

Le **format et le canal** de transmission sont cruciaux.

**Format** : PDF signé numériquement (authentification de l’émetteur), archive ZIP chiffrée contenant les annexes, volumétrie clairement indiquée. Pas de document Word modifiable — le rapport doit être figé.

**Canal** : transmission sécurisée (ProtonMail, SecureDrop, ou remise physique en main propre pour les rapports hautement sensibles). Pas de pièce jointe par email standard non chiffré.

**Classification (TLP)** : Traffic Light Protocol pour indiquer le niveau de diffusion autorisé. TLP:RED (strictement limité aux destinataires nommés), TLP:AMBER (limité à l’organisation destinataire et partenaires nommés), TLP:GREEN (diffusion limitée à la communauté), TLP:CLEAR (public). Un rapport d’investigation privé est typiquement TLP:RED ou TLP:AMBER.

**Confirmation de réception** : le destinataire accuse réception. L’investigateur conserve la trace de la transmission.

**Conservation** : l’investigateur conserve une copie du rapport et les sources brutes pendant la durée nécessaire (durée de la procédure judiciaire plus prescription applicable), puis destruction sécurisée.

#### 24.3 Transmission aux autorités

Quand le rapport doit être transmis aux autorités, plusieurs canaux selon la nature.

**Via le cabinet d’avocats** : la voie la plus courante. Le cabinet intègre le rapport OSINT à un dossier de plainte, le dépose au parquet compétent. L’investigateur peut être auditionné par les enquêteurs comme témoin de la méthodologie.

**Saisie directe des LEA spécialisées** (avec l’autorisation du client) :

- **C3N** (Centre de lutte contre les criminalités numériques, Gendarmerie) : cybercriminalité, escroquerie en ligne, désinformation.
- **OCLCTIC** (Office central de lutte contre la criminalité liée aux TIC, Police) : cybercriminalité.
- **JUNALCO** (Juridiction nationale chargée de la lutte contre la criminalité organisée) : dossiers complexes, crime organisé, blanchiment de grande ampleur.
- **PNF** (Parquet National Financier) : corruption, fraude fiscale, blanchiment.
- **TRACFIN** (Cellule de Renseignement Financier) : en cas de signalement financier.
- **Pharos** : signalement de contenus illicites en ligne.

**Saisine des autorités administratives** :

- **CNIL** : en cas d’atteinte aux données personnelles.
- **AMF** : en cas d’opérations de marché suspectes.
- **ACPR** : pour les établissements bancaires et d’assurance.

**Le choix du canal** est souvent discuté entre l’investigateur, le cabinet d’avocats et parfois des conseils judiciaires. Un mauvais choix (saisir l’autorité inadéquate) peut retarder le traitement de plusieurs mois.

#### 24.4 L’expertise judiciaire OSINT

Certains rapports OSINT peuvent être demandés sous forme d’**expertise judiciaire**, ordonnée par un magistrat dans le cadre d’une procédure.

**Cadre** : l’expert est inscrit sur la liste des experts près une cour d’appel, a prêté serment, et intervient sur mandat du juge. Son rapport est versé au dossier et soumis au contradictoire des parties.

**Spécificités de l’expertise par rapport à l’investigation privée** :

- **Neutralité** : l’expert n’est plus à la solde d’une partie — il travaille pour le juge. Le rapport doit être impartial et répondre strictement aux questions posées dans la mission.
- **Contradictoire** : les parties peuvent contester les constatations, demander des opérations complémentaires, opposer leurs propres experts. Le rapport doit résister à la contradiction d’experts adverses.
- **Méthodologie opposable** : chaque opération doit être reproductible. Un contradicteur doit pouvoir, en suivant la méthodologie décrite, retrouver les mêmes résultats.
- **Forme du rapport** : suit des règles codifiées (NCPC en France — article 276 et suivants), avec une structure précise, un résumé des dires des parties, des conclusions motivées.

**Valeur probante** : supérieure à celle d’un rapport privé. Le magistrat peut s’appuyer sur un rapport d’expertise judiciaire pour fonder sa décision, sous réserve de la critique apportée par les parties au contradictoire.

**Veille en post-expertise** : l’expert peut être rappelé pour un complément d’expertise, une réponse aux dires des parties, ou pour une audition. Le dossier d’expertise se conserve pendant toute la durée de la procédure plus prescription.

Pour l’investigateur OSINT qui ambitionne l’inscription sur liste d’experts : cursus de formation, démonstration d’une pratique professionnelle établie, et dépôt de candidature auprès de la cour d’appel. C’est un parcours à moyen terme, pas une qualification immédiate.

#### 24.5 Veille post-rapport

La **veille post-rapport** est une phase souvent négligée mais critique. Une fois le rapport transmis, l’investigation n’est pas terminée — la cible va réagir.

**Risques post-rapport** :

- **Disparition de preuves** : la cible découvre (directement ou par fuite) qu’elle est investiguée, et cherche à effacer ce qui peut l’être. Suppression de comptes, dissolution de sociétés, mise en privé de profils, transfert de fonds.
- **Modification de comportement** : les sociétés offshore changent d’adresse, de nominee, de nom ; les wallets crypto sont vidés ; les canaux Telegram sont supprimés.
- **Réaction juridique** : la cible peut déposer une plainte en diffamation, assigner l’investigateur, menacer le client.

**Veille méthodologique** :

**Archivage anticipé** : dès la phase de collecte, archivage systématique via Wayback Machine et archive.today. Les captures Hunchly conservent les versions locales hashées. Le rapport cite des URL archivées (Wayback Machine) plutôt que les URL vivantes susceptibles de disparaître.

**Alertes** : configuration d’alertes Google (pour les mentions publiques de la cible et des entités), monitoring des canaux Telegram surveillés, alertes sur les modifications de Pappers ou des registres étrangers (services de monitoring comme Sayari, Tenders.pro, alertes Pappers).

**Monitoring des modifications** : outils comme Visualping ou Distill pour détecter les changements sur des pages précises (profil LinkedIn, site d’une société cible, page Pappers).

**Monitoring dark web** : si l’investigation a révélé une présence dark web, continuer le monitoring (Flare, monitoring artisanal) pour détecter de nouvelles activités ou la disparition des anciennes.

**Re-captures périodiques** : les pages importantes sont re-capturées périodiquement (chaque trimestre par exemple) pour documenter l’évolution.

**Documentation des modifications** : chaque changement détecté post-rapport est documenté (date de détection, nature du changement, capture avant/après). Ces modifications deviennent elles-mêmes des éléments d’investigation — une dissolution soudaine de société peut être une preuve indirecte.

**Durée de veille** : typiquement corrélée à la durée de la procédure judiciaire. Une veille active pendant les 6 à 18 mois qui suivent le dépôt de plainte, puis réduite mais maintenue jusqu’à la clôture définitive de la procédure.

#### 24.6 Fil rouge — MIRAGE Épisode 12

> **🎯 MIRAGE — Épisode 12 : transmission au C3N et veille post-rapport**
> 
> Le rapport final (78 pages + 142 pages d’annexes, TLP:RED) est remis au cabinet Legrand & Associés par remise physique en main propre, avec signature d’un reçu.
> 
> Le cabinet intègre le rapport au dossier de plainte. Deux saisines séparées :
> 
> - **Dépôt de plainte au PNF** pour abus de biens sociaux, blanchiment, et fraude fiscale — dossier adossé au rapport OSINT, avec pistes de réquisitions priorisées.
> - **Signalement au C3N** pour le volet désinformation (faux comptes coordonnés, campagne visant le lanceur d’alerte).
> 
> **Audition de l’investigateur** par les enquêteurs du C3N trois semaines plus tard : description de la méthodologie, justification des cotations, documentation des limites. Le contradictoire d’un éventuel procès reste à venir.
> 
> **Mise en place de la veille post-rapport** par l’investigateur, sur mandat du cabinet pour 12 mois :
> 
> - Alertes Google sur les noms des entités (TechnoVert, Delta Consulting, Delta Trading, DT Investments).
> - Monitoring Pappers sur les sociétés françaises (modifications, dissolutions).
> - Monitoring Visualping sur les pages LinkedIn de Delaunay et des dirigeants des structures offshore.
> - Monitoring du canal Telegram « Offshore Trading Club » pour détecter sa suppression ou son déplacement.
> - Archivage trimestriel systématique des pages importantes via Wayback Machine.
> 
> **Événements détectés dans les 3 premiers mois post-rapport** :
> 
> - M+1 : le canal Telegram « Offshore Trading Club » passe en mode privé (coïncidant avec la perquisition au domicile de Delaunay dans le cadre de l’enquête PNF). Capture avant/après archivée.
> - M+2 : dissolution de DT Investments S.à r.l. au Luxembourg (BODACC luxembourgeois). Mouvement documenté, potentiellement un élément à charge supplémentaire (dissolution post-enquête).
> - M+3 : Delaunay démissionne de TechnoVert. Communiqué LinkedIn. Capture archivée.
> 
> Ces éléments sont transmis en complément d’information aux autorités saisies. Ils ne changent pas les conclusions du rapport initial, mais les renforcent : **les modifications constatées sont cohérentes avec H1 (détournement), incohérentes avec H2 (optimisation légale, qui n’aurait pas déclenché ces réactions précipitées)**.

-----

## PARTIE VII — CAS DE SYNTHÈSE COMPLETS

> **Ce que cette partie apprend.** Articuler l’ensemble des méthodes du cours sur des cas complets. Chaque chapitre reconstitue une investigation de bout en bout — cadrage, OPSEC, collecte, corrélation, analyse, production — sur un type de scénario différent.
> 
> **Ce qu’elle ne couvre pas.** De nouvelles méthodes — tout ce qui est mobilisé ici a été enseigné dans les Parties I à VI. Les cas présentés sont inspirés de configurations réelles mais anonymisés et reconstitués pour les besoins pédagogiques.
> 
> **Ce que vous saurez faire après cette partie.** Prendre une mission OSINT de bout en bout, quelle qu’en soit la nature (patrimoniale, GEOINT, dé-anonymisation, désinformation), et produire un livrable exploitable.

-----

### Chapitre 25 — Cas complet : synthèse Opération MIRAGE

Ce chapitre rassemble les douze épisodes du fil rouge dans une vue d’ensemble cohérente, qui correspond à ce qu’aurait été le rapport final tel que transmis au cabinet Legrand & Associés.

#### 25.1 Récapitulatif du mandat et des questions d’investigation

Le cabinet d’avocats Legrand & Associés, représentant un actionnaire minoritaire détenant 12 % du capital de **TechnoVert SAS** (ETI française du recyclage industriel, 450 collaborateurs, CA 85 M€), a mandaté une investigation OSINT sur **Marc Delaunay**, 48 ans, Directeur Administratif et Financier de la société depuis octobre 2019.

Quatre questions d’investigation ont structuré la mission sur 6 semaines.

**QI-1** — Marc Delaunay contrôle-t-il, directement ou indirectement, des sociétés non françaises non déclarées ? Si oui, lesquelles, dans quelles juridictions, et avec quelle structure ?

**QI-2** — Existe-t-il des flux financiers entre TechnoVert SAS et ces sociétés, et sont-ils cohérents avec une activité économique réelle ?

**QI-3** — Marc Delaunay détient-il des crypto-actifs non déclarés, et peut-on tracer un lien entre TechnoVert et ces actifs ?

**QI-4** — Existe-t-il une campagne de désinformation visant le lanceur d’alerte interne licencié en juillet 2025, et peut-on en identifier l’origine ?

Le périmètre excluait strictement toute interaction avec la cible, tout accès non autorisé, et toute technique hors OSINT. Le livrable devait être exploitable judiciairement.

#### 25.2 La méthodologie déployée

L’investigation a mobilisé la méthodologie standard structurée en sept phases : cadrage, plan de collecte, collecte disciplinée, traitement, corrélation, analyse, production.

**OPSEC** : niveau moyen calibré sur le threat model (DAF d’ETI, techniquement compétent, sans capacités offensives avérées). VM Ubuntu dédiée, VPN ProtonVPN isolé, profil Firefox vierge, trois avatars (LinkedIn, Telegram, X) créés et maturés pendant trois semaines avant utilisation. Téléphone dédié avec SIM prépayée. Hunchly pour la capture hashée, Obsidian pour le journal, Maltego pour le graphe.

**Plan de collecte** structuré par question d’investigation, avec dépendances explicites : QI-1 (corporate) et QI-3 (crypto) se nourrissent mutuellement ; QI-2 nécessite des deux précédentes pour identifier les flux ; QI-4 (désinformation) est relativement indépendante mais recoupe QI-1 par l’infrastructure.

**Sources mobilisées** : moteurs de recherche et Google Dorks, registres d’entreprises (Pappers, Registre maltais, RCS Luxembourg, ICIJ Offshore Leaks, Companies House), réseaux sociaux (LinkedIn, Instagram, Telegram, forum voitures de luxe, forum dark web), outils de pivot (Holehe, Epieos, GHunt, Maigret, PimEyes), breaches (HIBP, DeHashed, IntelX), infrastructure (Whois historique DomainTools, crt.sh, SecurityTrails), crypto (Blockchain.com, OXT, Etherscan, DeBank, Arkham).

#### 25.3 Le schéma reconstitué étape par étape

L’investigation a permis de reconstituer un schéma en cinq couches.

**Couche 1 — TechnoVert SAS** (France) : le centre opérationnel. Delaunay, en position de DAF, contrôle les flux comptables et engage des contrats de « consulting » avec Delta Consulting Ltd pour un volume annuel estimé entre 800 k€ et 1,5 M€ (estimation indirecte via analyse des comptes publiés et postes de charges externes).

**Couche 2 — Delta Consulting Ltd** (Malte) : receveur des flux TechnoVert. Dirigeant déclaré Joseph Borg (nominee maltais, présent dans 80+ sociétés). UBO non déclaré publiquement (RBE maltais restreint). Détenue à 100 % par DT Investments S.à r.l.

**Couche 3 — DT Investments S.à r.l.** (Luxembourg) : couche intermédiaire. Dirigeant Jean Petit (nominee luxembourgeois, présent dans 80+ sociétés). Détenue à 99 % par Delta Holding Ltd.

**Couche 4 — Delta Holding Ltd** (BVI) : couche opaque. UBO non identifiable dans les registres publics BVI sans coopération des autorités locales. Identifiable indirectement via : l’email `m.consulting@protonmail.com` dans le Whois historique de `deltaconsulting.mt`, croisement du cluster Bitcoin (publié sur Telegram par `marc_offshore` alias Delaunay) aboutissant au même dispositif crypto, présence de cet email dans le leak Dream Market 2020 lié à l’activité dark web.

**Couche 5 — Delaunay, bénéficiaire effectif probable** : le faisceau convergent (Telegram, stylométrie, leaks, pattern de mot de passe, comptes exchanges, train de vie incohérent avec revenus déclarés) pointe Delaunay comme UBO final avec un niveau de confiance très élevé sur les couches 1-3 (France, Malte, Luxembourg) et **probable** sur la couche 4 (BVI), compte tenu de l’opacité légale de cette juridiction.

En parallèle, un **patrimoine immobilier en SCI familiale** (SCI Delaunay Patrimoine, 1,2 M€ d’actifs immobiliers à Levallois-Perret) donne apparemment l’image d’un cadre bien rémunéré mais sans train de vie extraordinaire. La comparaison avec le cluster crypto identifié (~800 k€ au cours 2024) et les flux USDT tracés (1,2 M USD mouvementés) montre l’incohérence.

#### 25.4 La matrice ACH finale

La matrice ACH détaillée dans le Ch.21 a été testée sur 47 évidences cotées. Synthèse finale :

- **H1 (détournement)** : cohérente avec 41 des 47 évidences, incohérente avec 2, non applicable sur 4. **Hypothèse retenue comme principale**.
- **H2 (optimisation légale)** : cohérente avec 12, incohérente avec 24, non applicable sur 11. **Éliminée**.
- **H3 (activité annexe déclarée ailleurs)** : cohérente avec 18, incohérente avec 22, non applicable sur 7. **Éliminée**.
- **H4 (Delaunay nominee pour un tiers)** : cohérente avec 28, incohérente avec 14, non applicable sur 5. **Affaiblie** mais non totalement éliminée — l’hypothèse que Delaunay soit lui-même un intermédiaire pour un bénéficiaire encore en amont ne peut être écartée sans coopération BVI.

**Conclusion analytique** : le schéma de détournement (H1) est **très probable** (85 % au sens WEP). Une composante possible (H1 + H4 partiellement : Delaunay détourne, et reverse une partie à un tiers qu’il sert) ne peut être écartée et est documentée comme zone d’incertitude.

#### 25.5 Le rapport final : structure et principales constatations cotées

Le rapport remis au cabinet comporte 78 pages + 142 pages d’annexes.

**Structure** :

- Sommaire exécutif (1 page).
- Mandat et périmètre (3 pages).
- Méthodologie et sources (5 pages).
- Constatations (42 pages — 47 faits cotés, chacun avec source, cotation, capture).
- Analyse (12 pages — ACH, timeline, biais documentés, raisonnement adversaire).
- Conclusions (6 pages — réponse aux 4 QI avec niveaux de confiance).
- Recommandations (4 pages — pistes de réquisitions prioritaires).
- Limites et zones d’incertitude (5 pages).
- Annexes (142 pages — graphe complet, timeline détaillée, captures hashées, journal extraits).

**Constatations majeures** (extrait du sommaire exécutif) :

- **C-1** (A1) — Delaunay est administrateur du canal Telegram « Offshore Trading Club » (560 membres) via l’alias `marc_offshore`. Correspondance établie par triangulation : bot @SangMata_bot (historique de usernames convergent), WhatsApp (photo identique), dump Facebook 2021 (numéro confirmé).
- **C-12** (A1) — Delta Consulting Ltd, Delta Trading Ltd et DT Investments S.à r.l. sont opérées par une même entité : certificat TLS unique couvrant les trois domaines en SAN.
- **C-18** (B2) — Les flux TechnoVert → Delta Consulting représentent, selon l’estimation indirecte des postes de charges externes de TechnoVert publiés via Pappers, 89 % du chiffre d’affaires déclaré de Delta Consulting sur les trois derniers exercices.
- **C-23** (A1) — Le breach Ledger 2020 confirme la détention par Delaunay d’un hardware wallet crypto au moment du breach.
- **C-31** (B1) — Un cluster Bitcoin de 4 adresses (18,7 BTC mouvementés) est attribué à Delaunay avec un niveau de confiance élevé (publication de l’adresse principale sur le canal Telegram qu’il administre, sortie vers Binance où son email est enregistré).
- **C-37** (B2) — Une photo postée sur l’Instagram de Delaunay le 15 février 2026, prétendant documenter sa présence à Genève, présente trois incohérences techniques indépendantes (ELA suspect, ombres incompatibles avec SunCalc, météo archivée contradictoire). Tentative de fabrication d’alibi probable.
- **C-42** (B2) — La campagne de désinformation visant le lanceur d’alerte utilise huit comptes X coordonnés (créés dans la même fenêtre de 48h, photos de profil AI-generated, retweets mutuels avec timing synchronisé), un blog lié au réseau d’infrastructure Delta par Whois historique, et plusieurs contenus synthétiques.

#### 25.6 Le graphe complet

Le graphe final comporte **47 entités** et **83 relations**, structurées en 5 juridictions (France, Malte, Luxembourg, BVI, écosystème crypto décentralisé).

Entités par type : 4 personnes physiques (Delaunay + 3 nominees identifiés), 7 sociétés (TechnoVert + 6 structures offshore), 12 entités crypto (adresses et clusters), 9 entités infrastructure (domaines, emails), 8 entités SOCMINT (canaux Telegram, forums, profils réseaux sociaux), 7 entités judiciaires (breaches, décisions de justice associées à des entités périphériques).

Relations annotées : contrôle, actionnariat, mandat, flux financier daté, nominee, cohabitation d’infrastructure, publication publique, breach.

Le graphe a révélé deux structures non anticipées en début d’investigation :

- Un **troisième nominee** (Joseph Borg) apparaît également dans une société liée au lanceur d’alerte — lien circonstanciel qui pourrait suggérer un système de surveillance par Delaunay de son ex-employé.
- Les **8 comptes X** de la campagne de désinformation partagent un point d’infrastructure (même domaine d’enregistrement via Whois historique) avec un ancien site abandonné de Delta Trading.

#### 25.7 Les pistes de réquisitions identifiées

Le rapport propose 11 pistes de réquisitions, priorisées par rapport coût/information.

**Priorité 1** :

- Réquisition **Binance** (identification du titulaire du compte lié à `marcdelaunay75@gmail.com`, historique complet des transactions).
- Réquisition **Coinbase** (même).
- **Coopération internationale maltaise** (via JUNALCO ou PNF) pour obtenir l’identité complète de l’UBO de Delta Consulting et Delta Trading.
- **Coopération luxembourgeoise** pour DT Investments.

**Priorité 2** :

- Expertise comptable **TechnoVert** pour identifier précisément les factures vers Delta Consulting et évaluer la réalité des prestations.
- **Vérification fiscale** (DGFiP) pour les déclarations IR/IFI de Delaunay sur la période, notamment sur le volet crypto.
- Réquisition **OKX** (juridiction moins coopérative — à tenter).

**Priorité 3** :

- Réquisition opérateur télécom pour identifier les connexions associées au numéro `marc_offshore`.
- Coopération **BVI** pour Delta Holding Ltd — longue et incertaine, mais nécessaire pour clore la boucle.
- Réquisition **X** (Twitter) pour l’identification des 8 comptes de la campagne de désinformation.
- Réquisition **Telegram** pour les métadonnées du canal « Offshore Trading Club ».

#### 25.8 La transmission au C3N et la suite judiciaire

Le cabinet Legrand & Associés a décidé de deux saisines parallèles.

**Saisine du PNF** (Parquet National Financier) pour abus de biens sociaux, blanchiment et fraude fiscale — dossier principal, adossé au rapport OSINT, avec les 11 pistes de réquisitions documentées.

**Signalement au C3N** (Centre de lutte contre les criminalités numériques) pour le volet désinformation — dossier complémentaire centré sur les 8 comptes X, le blog lié, et les contenus synthétiques.

L’investigateur a été entendu comme témoin par les enquêteurs du C3N trois semaines après la transmission. L’audition a porté sur la méthodologie, la justification des cotations, et la documentation des limites.

La procédure judiciaire suit son cours. Les événements détectés en veille post-rapport (dissolution de DT Investments, passage en privé du canal Telegram, démission de Delaunay de TechnoVert) ont été transmis en complément d’information.

#### 25.9 Les leçons de MIRAGE

**Ce qui a marché** :

- La logique du pivot email → exchange (Holehe) a été le pivot le plus productif de l’enquête. Sans le signal « Binance et Coinbase » dès la phase 1, la dimension crypto aurait été beaucoup plus longue à détecter.
- Le réflexe de Whois historique a été déterminant pour identifier l’email pivot `m.consulting@protonmail.com`.
- L’analyse du certificat TLS et des SAN a permis de découvrir DT Investments, qui n’était rattachable à Delta Consulting par aucun registre public.
- La vérification d’authenticité de la photo « alibi » (ELA + SunCalc + météo) a transformé une tentative de manipulation en élément à charge.

**Ce qui aurait pu rater** :

- Si Delaunay avait utilisé une OPSEC stricte (pas de réutilisation d’username entre Telegram et le forum Voitures de Luxe, pas de publication d’adresse Bitcoin publique, pas de tentative d’alibi photographique), l’investigation aurait été beaucoup plus difficile et probablement incomplète sur plusieurs dimensions.
- Les breaches ont été déterminantes — sans les breaches LinkedIn, Adobe, et surtout Ledger et le dump Facebook 2021, plusieurs pivots auraient été impossibles. Cette dépendance aux breaches pose question méthodologiquement (que faire quand les breaches ne couvrent pas la cible ?).
- La coopération BVI reste une zone d’incertitude qui ne sera levée que par l’action judiciaire.

**Ce qu’on aurait pu mieux faire** :

- Une revue par pair externe du rapport aurait probablement identifié deux formulations qui, à la relecture à froid, excèdent légèrement le vocabulaire calibré.
- Le monitoring post-rapport aurait pu être mis en place plus tôt (idéalement dès la semaine où l’investigation a été identifiée par la cible comme probable, vers la fin de la 4ème semaine).
- La documentation de l’hypothèse H4 (Delaunay lui-même nominee) aurait mérité plus de développement — elle reste la zone d’incertitude principale et conditionne la qualification juridique finale.

-----

### Chapitre 26 — Cas complet : investigation GEOINT sur une vidéo virale

#### 26.1 Le contexte

Un collectif de journalistes indépendants mandate une investigation OSINT pour vérifier une vidéo devenue virale sur les réseaux sociaux. La vidéo (47 secondes, filmée verticalement, sans audio identifiable) prétend documenter une **frappe militaire dans une ville du nord de la Syrie** le 8 novembre 2025 à 15h30 locale. La vidéo a été partagée 340 000 fois en 72 heures, principalement sur X et Telegram. Plusieurs médias l’ont reprise comme authentique. Le collectif veut savoir si le lieu, la date et la nature des événements sont conformes aux prétentions.

**Contraintes** : délai 5 jours, équipe réduite (un investigateur + revue par pair), sans accès à l’imagerie satellite commerciale HD.

#### 26.2 Phase 1 — Extraction des indices visuels

Méthodologie Bellingcat systématique. La vidéo est téléchargée via `yt-dlp` depuis le compte X initial. Métadonnées vérifiées avec ExifTool : aucune EXIF (attendu après passage par X).

Extraction frame par frame avec `ffmpeg` : 47 frames clés retenues pour analyse.

Indices visuels catalogués :

- **Enseignes en langue arabe** : dialecte identifié comme levantin (pas du Golfe, pas du Maghreb). Compatible avec Syrie, Liban, Jordanie, Palestine, Israël-Arabes.
- **Plaque d’immatriculation** sur un véhicule passant dans le cadre : format jordanien (plaque à fond blanc avec chiffres noirs, format spécifique). **Incohérent avec Syrie.**
- **Signalétique routière** : couleurs et typographie non standard syrienne. Correspond au code routier jordanien.
- **Architecture** : maisons à toits plats, constructions en pierre calcaire locale, topographie vallonnée. Compatible avec nord de la Jordanie ou sud de la Syrie.
- **Végétation** : pins parasols, oliviers, quelques figuiers — climat méditerranéen d’altitude. Compatible avec la région Irbid/Ajloun (Jordanie) ou le Jabal al-Druze (Syrie).
- **Pas de militaire visible, pas d’uniforme identifiable** dans le champ.
- **Panache de fumée** au loin (prétendue frappe) : forme et couleur compatibles avec une explosion d’origine multiple — pas discriminant entre frappe militaire et accident industriel.
- **Ombres** : courtes, angle d’environ 60° par rapport à la verticale, projetées vers l’Est-Nord-Est.

**Signal fort** : l’incompatibilité entre la plaque jordanienne et la localisation prétendue syrienne.

#### 26.3 Phase 2 — Formulation des hypothèses de localisation

Hypothèses retenues :

- **H-A** : nord de la Jordanie (Irbid, Ajloun, Jerash) — région urbaine/périurbaine, architecture cohérente, présence de plaques jordaniennes normale.
- **H-B** : zone frontalière sud de la Syrie (Deraa) — architecture cohérente, présence occasionnelle de véhicules jordaniens.
- **H-C** : plateau du Golan (Israël/Syrie contestée) — architecture similaire, mais absence de signalétique arabe compatible avec la partie israélienne.

H-C rapidement éliminée par la signalétique arabe non hébraïsée. Focus sur H-A et H-B.

#### 26.4 Phase 3 — Vérification via Street View et imagerie satellite

**Google Street View** sur les principales villes jordaniennes et zones frontalières syriennes. Plusieurs heures de parcours manuel des rues correspondant à la topographie de la vidéo (rues à flanc de colline, présence de petits commerces, type d’enseignes).

**Correspondance partielle** : un carrefour spécifique à **Irbid, Jordanie**, dans le quartier nord-est, présente une configuration architecturale très similaire à celle de la vidéo. Enseigne d’une pharmacie visible au fond de la vidéo : en croisant avec Street View, on trouve une pharmacie au nom compatible (capture Street View datant de juillet 2024). Le trottoir, les poteaux électriques, la disposition des fenêtres correspondent.

**Confirmation via Mapillary** : une photo déposée par un contributeur en septembre 2025 sur Mapillary montre le même carrefour sous un autre angle. Correspondance exacte avec plusieurs éléments de la vidéo.

**Imagerie satellite Sentinel-2** consultée pour la date prétendue (8 novembre 2025) sur Irbid : rien d’anormal visible à la résolution 10 m. **Même consultation pour la zone frontalière syrienne (Deraa)** : pas d’événement détectable sur la date.

**Google Earth historique** : consultation des images de 2023-2025 sur le carrefour identifié à Irbid — pas de changement suggérant une reconstruction post-frappe récente.

**Conclusion géographique** : la vidéo a été filmée à **Irbid, Jordanie**, pas en Syrie comme prétendu.

#### 26.5 Phase 4 — Chronolocation (SunCalc + archives météo)

**Calcul solaire** via SunCalc pour Irbid (32.55°N, 35.85°E) :

- La vidéo montre des ombres avec angle d’environ 60° de la verticale, projetées vers l’Est-Nord-Est.
- Cette configuration correspond à une heure d’environ **9h30 locale** en novembre, **pas 15h30** comme prétendu.
- À 15h30 en novembre à Irbid, les ombres devraient être projetées vers l’Est (soleil déclinant à l’Ouest), avec un angle plus proche de 70° de la verticale.

**Incohérence temporelle majeure** : la vidéo ne peut pas avoir été filmée à 15h30 le 8 novembre 2025.

**Archives météo** (via Weather Underground / station d’Irbid) pour le 8 novembre 2025 : ciel partiellement nuageux, visibilité réduite. La vidéo montre un ciel très clair. **Incohérence secondaire.**

**Vérification complémentaire** : consultation des archives météo pour Irbid sur une fenêtre de plusieurs semaines autour de la date prétendue. Le seul jour compatible avec la météo visible dans la vidéo (ciel clair, ombres nettes) sur la période septembre-novembre 2025 est le **3 octobre 2025**.

**Conclusion chronologique** : la vidéo date très probablement d’une date antérieure à la prétention (candidat : 3 octobre 2025), et l’heure est le matin (environ 9h30 locale), pas l’après-midi.

#### 26.6 Phase 5 — Vérification d’authenticité

**TinEye** sur plusieurs frames extraites de la vidéo : aucun match antérieur au 10 novembre 2025 (date de publication initiale sur X). La vidéo elle-même semble récente en tant que publication, bien que son contenu puisse être plus ancien.

**Recherche par crop** : le panache de fumée au loin est cropé et recherché séparément. **Résultat critique** : Yandex Images identifie une correspondance avec une photo d’un **incendie industriel dans une usine textile d’Irbid le 3 octobre 2025**, largement couvert par la presse locale jordanienne. Le panache de fumée provient de cet incendie, pas d’une frappe militaire.

**ELA sur FotoForensics** (frames extraites) : légers artefacts compatibles avec la compression vidéo normale, aucune zone suggérant une modification additionnelle. La vidéo elle-même semble authentique, c’est sa **contextualisation** qui est fausse.

**Vérification du compte de publication** : le compte X qui a diffusé la vidéo initialement (@SyriaAlertXXX, 42 000 followers) a été créé en mai 2025, publie exclusivement du contenu orienté, et a déjà été pointé par plusieurs fact-checkers pour des publications de vidéos mal contextualisées.

#### 26.7 La conclusion analytique

**Conclusion à confiance élevée** :

- La vidéo a été filmée à **Irbid, Jordanie** (pas en Syrie).
- La date de filming est **très probablement le 3 octobre 2025** (pas le 8 novembre 2025).
- L’heure est **matin** (environ 9h30 locale), pas après-midi.
- Le panache de fumée correspond à un **incendie industriel dans une usine textile**, documenté par la presse locale, **pas à une frappe militaire**.

La vidéo est **authentique** dans son existence (pas de deepfake ni de manipulation numérique détectable), mais son **contexte prétendu est faux** sur les quatre dimensions : lieu, date, heure, nature des événements. Il s’agit d’un cas classique de **recontextualisation trompeuse** (misleading context), pas de contenu synthétique.

#### 26.8 Le rapport remis

Le rapport, remis au collectif journalistique dans les 5 jours, comporte 14 pages + 42 pages d’annexes (captures Street View, Mapillary, calculs SunCalc, archives météo, photos de l’incendie industriel jordanien).

**Conclusions cotées** :

- Localisation à Irbid : **quasi-certain** (A1 — correspondances Street View et Mapillary convergentes, architecture, plaque, dialecte).
- Date réelle du 3 octobre 2025 : **très probable** (B1 — SunCalc + météo + incendie documenté convergents).
- Nature de l’événement (incendie, pas frappe) : **quasi-certain** (A1 — panache identifié via recherche inversée, presse locale documentée).
- Intention trompeuse du compte diffuseur : **probable** (B2 — antécédents documentés, mais pas de preuve directe de mauvaise foi).

Le collectif publie un article de fact-check dans les 48 heures suivantes. Les médias qui avaient repris la vidéo sans vérification la corrigent progressivement.

-----

### Chapitre 27 — Cas complet : dé-anonymisation d’un compte pseudonyme

#### 27.1 Le contexte

Un éditeur de logiciels B2B (1 200 employés, chiffre d’affaires 180 M€) est victime d’une fuite interne : un compte X pseudonyme, `@insider_leak42`, publie depuis trois semaines des informations confidentielles sur la société (roadmap produit non annoncée, conflits internes, email du DG fuité partiellement). L’audience du compte (8 700 followers) inclut des clients, des concurrents, et quelques journalistes tech.

La direction sécurité mandate une investigation OSINT pour identifier l’auteur, de manière à prendre les mesures internes appropriées (entretien disciplinaire, dépôt de plainte, gestion de crise RH).

**Contraintes** : identification avec un niveau de confiance suffisant pour fonder une décision disciplinaire, sans nécessairement atteindre le seuil pénal (qui relèverait d’une réquisition à X). Discrétion absolue vis-à-vis de la cible pour ne pas alerter avant décision.

#### 27.2 Phase 1 — Pivot username

**Username `insider_leak42`** testé sur Sherlock et Maigret.

**Correspondances détectées** :

- **GitHub** : compte `insider_leak42` créé il y a 4 ans, 12 repositories publics (tous privés désormais, mais quelques forks anciens restés visibles).
- **Forum de jeux vidéo** (subreddit-like non indexé par Google, identifié via WhatsMyName) : compte `insider_leak42` actif depuis 6 ans, 340 posts.
- **Stack Overflow** : compte `insider_leak42`, quelques questions techniques anciennes (2020-2022).

**Cohérence initiale** : le username existe antérieurement à la fuite actuelle (6 ans d’historique sur le forum jeux), ce qui écarte l’hypothèse d’un compte créé spécifiquement pour la fuite.

#### 27.3 Phase 2 — Pivot email via GitHub

**Investigation GitHub** : les forks publics anciens contiennent, dans l’historique git, des **commits signés** avec un email associé. Un fork datant de 2022 révèle deux commits avec email visible : `j.martin.dev@outlook.com`.

**Holehe sur `j.martin.dev@outlook.com`** :

- Présent sur LinkedIn.
- Présent sur Instagram.
- Présent sur Dropbox.
- Présent sur Spotify.
- Présent sur Skype.

**GHunt sur l’équivalent Google** (`j.martin.dev@gmail.com`, essayé en permutation) : aucun compte Google actif trouvé.

#### 27.4 Phase 3 — Pivot profil et photo

**LinkedIn** (consulté via avatar d’investigation en mode privé, pas avec le compte de la direction sécurité) : profil de **Julien Martin**, Développeur Senior chez l’éditeur de logiciels cible, embauché il y a 3 ans. Formation informatique, mentions de projets cohérents avec les repositories GitHub identifiés.

**Instagram** (profil public, `julien.martin.92`) : 147 posts, photos personnelles, voyages, vie quotidienne. Photo de profil claire visible.

**PimEyes sur la photo de profil Instagram** : deux correspondances.

- Une correspondance sur le site officiel de l’éditeur, page « nos talents » (photo d’équipe, Julien Martin identifiable au 2ème rang). **Confirmation forte** de l’identité.
- Une correspondance sur une photo ancienne d’un meetup tech parisien en 2022.

**Vérification sociale** : les posts Instagram mentionnent des collègues identifiables sur LinkedIn comme employés de l’éditeur. Le cercle social est cohérent.

#### 27.5 Phase 4 — Corroboration multi-dimensionnelle

**Cohérence temporelle** : les heures de publication de `@insider_leak42` sur X (mesurées sur les 3 semaines de l’activité) sont concentrées entre 19h et 23h UTC, avec quelques publications à 12h-14h UTC. Compatible avec une personne qui travaille en journée (pause déjeuner + soirées), fuseau Europe de l’Ouest.

Les commits GitHub publics anciens (2020-2022) sont également majoritairement concentrés en soirée — même pattern.

**Cohérence stylistique** : analyse stylométrique manuelle (vocabulaire technique, tournures, usage de la ponctuation, anglicismes) entre les posts X et les messages du forum de jeux. Convergence forte — même locuteur très probable.

**Cohérence des intérêts** : les centres d’intérêt évoqués sur X (tech, indie games, hardware custom) correspondent à ceux du forum jeux et aux repositories GitHub.

**Cohérence des griefs** : les posts X mentionnent des conflits internes spécifiques (réorganisation d’équipe, changement de stack technique) qui correspondent à des événements réels survenus dans l’équipe de Julien Martin — information validée par la direction sécurité.

#### 27.6 La matrice ACH

Trois hypothèses testées.

**H1** : Julien Martin est `@insider_leak42`. Cohérent avec : username partagé sur 4 plateformes, email via GitHub, photo via PimEyes, cercle social LinkedIn, pattern temporel, style d’écriture, griefs internes spécifiques.

**H2** : Le username `insider_leak42` a été usurpé par un tiers qui l’a repris pour créer le compte X récent. Testable : vérifier si le compte X a été créé récemment ou est ancien. **Vérification X** : le compte `@insider_leak42` a été créé il y a 4 ans, dormant jusqu’à il y a 3 semaines. Usurpation improbable (le tiers aurait dû prendre le contrôle du compte existant — suppose un piratage, pas documenté).

**H3** : L’email `j.martin.dev@outlook.com` trouvé dans les commits GitHub est un piège (honeytoken délibéré, faux email placé pour égarer). Testable : vérifier la cohérence avec d’autres sélecteurs. **Vérification** : l’email correspond au profil LinkedIn (qui n’est pas sous contrôle de l’investigation), à la photo PimEyes, et au cercle social. Piège improbable — demanderait une sophistication considérable sans motif clair.

**Conclusion ACH** : **H1 retenue avec niveau de confiance élevé** (85-90% WEP). H2 et H3 ne peuvent être formellement éliminées mais sont fortement improbables.

#### 27.7 La conclusion et ses limites

**Attribution** : Julien Martin est, avec une **haute probabilité** (85-90%), l’auteur du compte `@insider_leak42`.

**Ce que l’OSINT ne peut pas prouver seule** :

- **Preuve directe** : l’attribution définitive nécessiterait une réquisition judiciaire à X (identification de l’IP source, vérification du numéro de téléphone associé, corrélation avec d’autres accès).
- **Preuve d’intentionnalité** : l’OSINT établit le lien entre identité et compte, pas l’intention de nuire (question juridique distincte).

**Limites documentées explicitement** :

- Le username pourrait avoir été recyclé — mais l’historique X (compte dormant 4 ans) rend cette hypothèse peu crédible.
- L’email GitHub pourrait avoir été faux — mais la convergence avec tous les autres sélecteurs rend cette hypothèse peu crédible.
- La reconnaissance faciale PimEyes est une correspondance forte mais pas absolue — elle est corroborée par le site de l’éditeur, ce qui la renforce considérablement.

#### 27.8 Gestion éthique : que faire de la dé-anonymisation

**Recommandation au client** : le rapport est remis à la direction sécurité pour **usage strictement interne**. Il n’est **pas** destiné à fonder une dé-anonymisation publique.

**Utilisation appropriée** :

- Entretien préalable confidentiel avec Julien Martin, dans un cadre disciplinaire, avec présentation des éléments permettant une confrontation.
- Si la personne confirme ou si les éléments supplémentaires (preuves internes — usage de matériel professionnel pour poster, logs d’accès aux informations fuitées) corroborent, procédure disciplinaire ou judiciaire selon la gravité.
- **Pas** de divulgation publique de l’identité, **pas** de diffusion dans l’entreprise au-delà des personnes strictement autorisées.

**Utilisation inappropriée** (à refuser) :

- Publication de l’identité sur les réseaux sociaux en réponse aux posts.
- Diffusion interne large (risque de doxxing par collègues).
- Utilisation du rapport pour une action extrajudiciaire (pression, menace, représailles informelles).

Cette éthique protège à la fois la cible (qui garde son droit à la présomption d’innocence et au contradictoire), le client (qui ne s’expose pas à des poursuites en cas d’erreur), et l’investigateur (dont la crédibilité repose sur l’usage responsable des rapports).

-----

### Chapitre 28 — Cas complet : campagne de désinformation et faux comptes

#### 28.1 Le contexte

Une société cotée de biotechnologie voit son cours de bourse chuter de 14 % en 48 heures après la diffusion d’une rumeur sur X et Telegram : des comptes prétendent qu’un essai clinique de phase 3 aurait été interrompu par l’ANSM pour effets indésirables graves. L’information est fausse — la société est en mesure de démentir documents à l’appui — mais le dommage financier est réel.

La société mandate une investigation OSINT pour identifier l’origine de la campagne, évaluer sa coordination, et préparer un dossier pour l’AMF (Autorité des Marchés Financiers) en raison du soupçon de manipulation de marché.

#### 28.2 Phase 1 — Détection de la coordination

**Inventaire des comptes** diffuseurs : l’investigation identifie 12 comptes actifs dans la campagne, principalement sur X, avec quelques relais sur Telegram.

**Patterns de création** :

- 9 des 12 comptes X ont été **créés la même semaine**, il y a 4 mois.
- Tous ont une photo de profil générée par IA (vérifiées par signaux visuels — symétrie excessive, arrière-plans incohérents — et par outils de détection Illuminarty : scores 75-90% probablement AI-generated).
- Les bios sont similaires, avec variations mineures autour du thème « investisseur indépendant », « passionné biotech », « santé publique ».

**Premier faisceau** : création coordonnée + photos AI-generated = très forte suspicion d’opération coordonnée plutôt que d’individus authentiques.

#### 28.3 Phase 2 — Analyse de réseau

**Graphe des interactions** (retweets mutuels, mentions, réponses) entre les 12 comptes sur les 48 heures critiques :

- Chaque post de l’un des comptes est retweeté par au moins 8 des 11 autres, avec un timing très resserré (médiane 3 minutes).
- Les réponses s’enchaînent selon des patterns atypiques pour un écosystème authentique : ratio réponses/auteurs très faible, contenu des réponses souvent en renforcement du message initial sans variation argumentative.
- Un outil comme **Hoaxy** ou simplement un graphe Maltego construit sur les URL de retweets révèle une **structure quasi-étoile** avec un compte central qui est systématiquement à l’origine des chaînes.

**Compte central identifié** : `@bio_insider_paris`, 24 000 followers, le plus ancien des 12 (créé il y a 2 ans), le plus suivi. Il est le **source** de 7 des 9 fils viraux majeurs de la campagne.

#### 28.4 Phase 3 — Analyse d’infrastructure

La campagne s’appuie sur **trois domaines web** référencés dans les posts des 12 comptes :

- `bio-insider-pharma.com` : blog « analyse indépendante biotech ».
- `pharma-watchdog-fr.net` : prétendu lanceur d’alerte pharma.
- `clinical-trials-leak.info` : prétendu agrégateur de fuites cliniques.

**Whois actuel** : les trois domaines ont un Whois privacy-protected.

**Whois historique via DomainTools** : **découverte majeure**. Les trois domaines ont été enregistrés au même mois (juin 2025), chez le même registrar (Namecheap), avec des coordonnées de registrant masquées maintenant mais **visibles dans les premières 48 heures avant mise en privacy**. Les trois domaines ont été enregistrés avec le même email : `m.roux@protonmail.com`.

**Reverse IP et hébergement** : les trois sites sont hébergés sur une même IP (VPS chez OVH, dédié — pas un hébergement mutualisé). **Cohabitation forte**.

**Certificats TLS** : les trois domaines utilisent Let’s Encrypt mais avec des certificats séparés — pas de SAN partagé. Cependant, les timestamps d’émission sont groupés à la minute près.

**Enregistrements DNS** : MX tous sur Google Workspace, TXT SPF identique pour les trois — paramétrage administrativement commun.

**Conclusion infrastructure** : les trois domaines sont opérés par la même entité, identifiable par l’email `m.roux@protonmail.com` et l’hébergement unique.

#### 28.5 Phase 4 — Attribution

**Investigation sur `m.roux@protonmail.com`** :

**Holehe** : présent sur LinkedIn, Twitter (X), Spotify.

**Recherche du profil LinkedIn** : profil de **Marc Roux**, consultant indépendant en communication stratégique, 52 ans, Paris. Expérience précédente dans des agences de communication.

**Recherche approfondie** : Marc Roux est listé publiquement comme ayant conseillé, il y a 5 ans, un **concurrent direct** de la biotechnologie cible (autre société cotée française, même aire thérapeutique). Source : archives de presse économique (`site:latribune.fr "Marc Roux"` révèle une mention dans un article de 2020).

**Le concurrent** : cette société concurrente a plusieurs raisons stratégiques de voir chuter le cours de la cible (partage de catégorie de marché, concurrence sur un lancement prévu dans le même trimestre).

**Prudence** : le lien « Marc Roux — concurrent » est **circonstanciel**. L’investigation OSINT ne peut **pas** prouver que le concurrent a commandité Marc Roux pour la campagne. Elle établit :

- Marc Roux a très probablement opéré la campagne (cotation B1 sur la base de l’email Whois, de l’hébergement, et du profil).
- Marc Roux a, dans le passé, travaillé pour un concurrent direct (cotation A1 via archive de presse).

La conclusion « le concurrent a commandité la campagne » nécessiterait des preuves additionnelles (contrats, paiements, correspondance) **non accessibles en OSINT**. Elle relève de l’enquête judiciaire.

#### 28.6 Documentation : timeline, graphe, cotations

**Timeline** reconstituée :

- Juin 2025 : enregistrement des 3 domaines par Marc Roux.
- Juillet 2025 : création de 9 comptes X avec photos AI-generated.
- Août-octobre 2025 : montée en audience des comptes, publication de contenus généralistes biotech pour construire une crédibilité.
- Début novembre 2025 : premiers signaux ciblant la société (rumeurs d’essai clinique).
- 8-9 novembre 2025 : campagne coordonnée sur les 12 comptes et les 3 blogs — chute du cours.

**Graphe final** : 12 comptes X, 3 domaines, 1 compte Telegram relais, 1 personne identifiée (Marc Roux), 1 lien circonstanciel vers un concurrent. 18 entités, 27 relations.

**Cotations** :

- Coordination des 12 comptes : **A1** (patterns de création, AI-generated, graphe d’interactions).
- Lien infrastructure → Marc Roux : **B1** (Whois historique + hébergement unique).
- Lien Marc Roux → concurrent passé : **A1** (archive presse publique).
- Commandite par le concurrent actuel : **non prouvée en OSINT** (à investiguer judiciairement).

#### 28.7 Le rapport

Le rapport (22 pages + 58 pages d’annexes) est remis à la société, qui l’utilise pour deux actions :

**Signalement à l’AMF** : dossier de soupçon de manipulation de marché, avec l’ensemble des éléments OSINT. L’AMF dispose de pouvoirs d’enquête étendus (réquisitions bancaires, accès aux communications électroniques dans le cadre légal de ses missions) qui lui permettront d’aller au-delà de ce que l’OSINT a pu établir.

**Dépôt de plainte** : diffamation et possiblement manipulation des cours (articles L.465-1 et suivants du Code monétaire et financier). Le C3N est saisi pour le volet technique (infrastructure, attribution).

**Communication corrective** : la société publie un communiqué démentant documents à l’appui, en s’appuyant sur l’identification de la campagne comme coordonnée (ce qui renforce la crédibilité du démenti : « il ne s’agit pas d’une information mais d’une attaque »). Le cours se redresse partiellement dans les semaines suivantes.

#### 28.8 Risques juridiques et éthiques

**Diffamation potentielle** : nommer publiquement Marc Roux comme auteur de la campagne, même avec un rapport OSINT solide, exposerait la société à une plainte en diffamation de l’intéressé. L’identité reste **interne au dossier** et n’est transmise qu’aux autorités (AMF, C3N, parquet) avec présomption d’innocence.

**Attribution au concurrent** : encore plus risquée à communiquer publiquement. Le rapport se limite à documenter le lien circonstanciel et à recommander une investigation judiciaire pour établir ou écarter un rôle du concurrent. La société cible **ne publie pas** cette partie.

**Respect du contradictoire** : si Marc Roux est auditionné par les autorités, il aura droit à un conseil, à la présentation du dossier, et à la contradiction des éléments OSINT. Le rapport doit donc **résister au contradictoire** — d’où l’importance de la rigueur méthodologique et de la cotation prudente.

#### 28.9 Convergence des techniques

Ce cas illustre la convergence de **toutes** les grandes techniques du cours :

- **SOCMINT** (Partie II) : analyse des comptes X et Telegram.
- **OSINT technique** (Partie III) : Whois historique, DNS, reverse IP, certificats.
- **IMINT** (Partie IV) : détection des photos AI-generated.
- **Breaches et pivots email** (Partie III) : Holehe sur l’email pivot.
- **Analyse de réseau** (Partie VI) : graphe d’interactions, identification du compte central.
- **Cotation et ACH** (Partie VI) : distinction rigoureuse entre ce qui est établi, circonstanciel, et à investiguer.
- **Cadre judiciaire** (Partie VI) : saisine AMF, plainte C3N, respect du contradictoire.

Une investigation OSINT mature combine systématiquement plusieurs de ces techniques. La maîtrise de chacune prise isolément n’est qu’un préalable — la compétence professionnelle réside dans leur **articulation** au service d’une question d’investigation concrète.

-----

## ANNEXES

-----

### Annexe A — Glossaire OSINT

|Terme                       |Définition                                                                                                            |
|----------------------------|----------------------------------------------------------------------------------------------------------------------|
|**ACH**                     |Analysis of Competing Hypotheses — technique analytique de test de plusieurs hypothèses contre les mêmes évidences    |
|**Admiralty (code)**        |Grille standard de cotation fiabilité source / crédibilité information (A-F / 1-6)                                    |
|**ADS-B**                   |Automatic Dependent Surveillance-Broadcast — signal de position émis par les aéronefs civils                          |
|**AIS**                     |Automatic Identification System — signal de position et identification des navires                                    |
|**Avatar / Sock puppet**    |Fausse identité créée pour l’observation passive OSINT                                                                |
|**Backstopping**            |Construction d’éléments de crédibilité pour un avatar (profil professionnel, historique)                              |
|**BODACC**                  |Bulletin Officiel des Annonces Civiles et Commerciales — publications légales des entreprises en France               |
|**Breach**                  |Fuite de données issue d’une compromission (HIBP, DeHashed)                                                           |
|**C2PA**                    |Coalition for Content Provenance and Authenticity — norme de métadonnées signées pour l’authenticité des contenus     |
|**Carding**                 |Trafic de données de cartes bancaires volées                                                                          |
|**CERT**                    |Computer Emergency Response Team — équipe de réponse à incident                                                       |
|**Certificate Transparency**|Logs publics des certificats TLS émis — permet l’énumération de sous-domaines (crt.sh)                                |
|**Chronolocation**          |Détermination de la date et de l’heure d’une image par l’analyse des ombres, de la météo, etc.                        |
|**Clustering (crypto)**     |Regroupement d’adresses crypto appartenant au même wallet par heuristiques                                            |
|**Corroboration**           |Confirmation d’un fait par au moins deux sources indépendantes                                                        |
|**CTI**                     |Cyber Threat Intelligence — renseignement sur les cybermenaces                                                        |
|**DARKINT**                 |Dark Web Intelligence — renseignement issu du dark web                                                                |
|**Deep web**                |Partie du web non indexée par les moteurs de recherche (≠ dark web)                                                   |
|**Dorking**                 |Utilisation d’opérateurs avancés dans les moteurs de recherche (Google Dorks)                                         |
|**Due diligence**           |Vérification approfondie d’un tiers (personne, société) avant engagement                                              |
|**ELA**                     |Error Level Analysis — technique de détection de manipulation d’images                                                |
|**ENS**                     |Ethereum Name Service — service de nommage lisible pour les adresses Ethereum                                         |
|**Epieos**                  |Outil OSINT de pivot email → services en ligne                                                                        |
|**EXIF**                    |Exchangeable Image File Format — métadonnées intégrées aux images                                                     |
|**Exchange (crypto)**       |Plateforme d’échange de crypto-actifs (Binance, Coinbase, Kraken)                                                     |
|**FININT**                  |Financial Intelligence — renseignement financier                                                                      |
|**Forwarding (Telegram)**   |Transfert d’un message d’un canal à un autre, trace visible du canal source                                           |
|**GEOINT**                  |Geospatial Intelligence — renseignement géospatial                                                                    |
|**Graphe relationnel**      |Représentation visuelle des entités et de leurs relations (Maltego)                                                   |
|**GHunt**                   |Outil OSINT de pivot email Google → données publiques du compte                                                       |
|**Holehe**                  |Outil open source de vérification de présence d’un email sur des services en ligne                                    |
|**HUMINT**                  |Human Intelligence — renseignement par sources humaines                                                               |
|**ICIJ**                    |International Consortium of Investigative Journalists — éditeur de l’Offshore Leaks Database                          |
|**IMINT**                   |Image Intelligence — renseignement par l’imagerie                                                                     |
|**Infostealer**             |Malware qui vole les credentials stockés dans les navigateurs (Lumma, RedLine, Vidar)                                 |
|**KYC**                     |Know Your Customer — obligation de vérification d’identité des clients                                                |
|**LEA**                     |Law Enforcement Agency — forces de l’ordre                                                                            |
|**Maigret**                 |Outil OSINT de recherche de username sur 2500+ plateformes                                                            |
|**Maltego**                 |Plateforme de graphe relationnel pour l’OSINT et l’investigation                                                      |
|**Mixer / Tumbler**         |Service qui mélange les fonds crypto de multiples utilisateurs pour casser la traçabilité                             |
|**Nominee**                 |Dirigeant ou actionnaire apparent d’une société, détenant en réalité pour le compte d’un tiers                        |
|**OPSEC**                   |Operational Security — sécurité opérationnelle de l’investigateur                                                     |
|**OSINT**                   |Open Source Intelligence — renseignement en sources ouvertes                                                          |
|**Pandora Papers**          |Leak ICIJ de 2021 révélant 11,9 millions de documents sur les structures offshore                                     |
|**Panama Papers**           |Leak ICIJ de 2016 du cabinet Mossack Fonseca (Panama)                                                                 |
|**Pappers**                 |Base française agrégée des données d’entreprises (registres, comptes, BODACC)                                         |
|**PEP**                     |Politically Exposed Person — personne politiquement exposée (dirigeant, haut fonctionnaire)                           |
|**PimEyes**                 |Service de reconnaissance faciale OSINT (images du web public)                                                        |
|**Pivot**                   |Passage d’un sélecteur à un autre (email → comptes, username → plateformes)                                           |
|**RBE**                     |Registre des Bénéficiaires Effectifs — déclaration des UBO en France                                                  |
|**RGPD**                    |Règlement Général sur la Protection des Données (UE, 2018)                                                            |
|**Sélecteur**               |Identifiant de recherche utilisé comme point de départ ou de pivot (nom, email, username, téléphone, photo, adresse)  |
|**SIGINT**                  |Signal Intelligence — interception de communications (réservé aux États)                                              |
|**Sherlock**                |Outil OSINT de recherche de username sur 300+ plateformes                                                             |
|**Shodan**                  |Moteur de recherche des services exposés sur Internet                                                                 |
|**SOCMINT**                 |Social Media Intelligence — renseignement issu des réseaux sociaux                                                    |
|**Stablecoin**              |Crypto-actif à valeur stabilisée (USDT, USDC)                                                                         |
|**Stylométrie**             |Analyse du style d’écriture pour l’attribution d’un texte à un auteur                                                 |
|**SunCalc**                 |Outil de calcul de position solaire utilisé pour la chronolocation                                                    |
|**Tails**                   |Distribution Linux live amnésique routant tout le trafic via Tor                                                      |
|**TGStat**                  |Annuaire et statistiques des canaux Telegram                                                                          |
|**TinEye**                  |Moteur de recherche inversée d’images spécialisé dans la datation de première apparition                              |
|**TLP**                     |Traffic Light Protocol — système de classification du niveau de diffusion d’une information (RED, AMBER, GREEN, CLEAR)|
|**Tor**                     |The Onion Router — réseau d’anonymisation, porte d’accès principale du dark web                                       |
|**UBO**                     |Ultimate Beneficial Owner — bénéficiaire effectif réel d’une société                                                  |
|**UTXO**                    |Unspent Transaction Output — modèle de transaction Bitcoin                                                            |
|**Vouching**                |Mécanisme de parrainage dans les forums criminels pour accéder aux sections avancées                                  |
|**Wayback Machine**         |Archive web historique (Internet Archive, `web.archive.org`)                                                          |
|**WEP**                     |Words of Estimative Probability — vocabulaire calibré d’expression de la probabilité                                  |
|**Whois**                   |Enregistrement public d’un nom de domaine (titulaire, dates, registrar)                                               |
|**Whois historique**        |Historique des enregistrements Whois passés — souvent révélateur d’identités masquées aujourd’hui                     |
|**Whonix**                  |Architecture en deux VM pour l’isolation forte d’une session Tor                                                      |
|**WhatsMyName**             |Outil OSINT de recherche de username, alternative à Sherlock avec moins de faux positifs                              |

-----

### Annexe B — Catalogue de Google Dorks par objectif

#### B.1 Documents financiers et corporate

```
"SOCIÉTÉ" filetype:pdf (rapport OR "compte de résultat" OR bilan)
filetype:pdf "rapport annuel" "SOCIÉTÉ"
filetype:xlsx "chiffre d'affaires" "SOCIÉTÉ"
site:SOCIÉTÉ.com filetype:pdf (confidential OR internal OR "à usage interne")
inurl:reports "SOCIÉTÉ" filetype:pdf
```

#### B.2 Organigrammes et trombinoscopes

```
"SOCIÉTÉ" filetype:pdf (organigramme OR trombinoscope OR "our team")
site:SOCIÉTÉ.com inurl:team
site:SOCIÉTÉ.com inurl:about
site:SOCIÉTÉ.com inurl:management
site:SOCIÉTÉ.com filetype:pdf "organization chart"
```

#### B.3 Emails exposés

```
site:SOCIÉTÉ.com "@SOCIÉTÉ.com"
filetype:pdf "@SOCIÉTÉ.com"
intext:"@SOCIÉTÉ.com" -site:SOCIÉTÉ.com
site:github.com "@SOCIÉTÉ.com"
site:pastebin.com "@SOCIÉTÉ.com"
"contact" "@SOCIÉTÉ.com" filetype:pdf
```

#### B.4 Directory listings et fichiers oubliés

```
intitle:"index of" "SOCIÉTÉ"
intitle:"index of /backup"
intitle:"index of /admin"
intitle:"index of /config"
intitle:"index of /.git"
site:SOCIÉTÉ.com intitle:"index of"
```

*Précaution juridique* (jurisprudence Bluetouff) : ne **pas télécharger** les contenus trouvés dans des directory listings qui exposent des données non destinées à être publiques. Documenter l’existence, pas exploiter.

#### B.5 Recherche temporelle

```
"SUJET" before:2024-12-31 after:2024-01-01
"événement" before:DATE
"entité" before:DATE -site:siteactuel.com
```

#### B.6 Plateformes spécifiques

**LinkedIn** :

```
site:linkedin.com/in/ "NOM"
site:linkedin.com/in/ "POSTE" "SOCIÉTÉ"
site:linkedin.com/company/ "SOCIÉTÉ"
```

**Facebook** :

```
site:facebook.com "NOM"
site:facebook.com/events "MOT-CLÉ"
site:facebook.com/groups "SUJET"
```

**Telegram** :

```
site:t.me "MOT-CLÉ"
site:t.me "username"
site:tgstat.com "canal"
```

**GitHub** :

```
site:github.com "email@société.com"
site:github.com "SOCIÉTÉ" filename:.env
site:github.com "SOCIÉTÉ" password
site:gist.github.com "MOT-CLÉ"
```

**Pastebin et équivalents** :

```
site:pastebin.com "MOT-CLÉ"
site:ghostbin.com "MOT-CLÉ"
site:paste.ee "MOT-CLÉ"
```

**Telegraph** :

```
site:telegra.ph "MOT-CLÉ"
site:telegra.ph "NOM"
```

#### B.7 Fichiers techniques

```
filetype:conf "SOCIÉTÉ"
filetype:log "SOCIÉTÉ"
filetype:sql "SOCIÉTÉ"
filetype:env "SOCIÉTÉ"
filetype:bak "SOCIÉTÉ"
site:SOCIÉTÉ.com filetype:xml
```

#### B.8 Contenus sur sites étatiques (France)

```
site:gouv.fr "SOCIÉTÉ"
site:legifrance.gouv.fr "NOM"
site:journal-officiel.gouv.fr "SOCIÉTÉ"
site:data.gouv.fr "MOT-CLÉ"
```

-----

### Annexe C — Atlas des plateformes et registres par pays

#### C.1 France

|Ressource       |URL                                  |Usage                                               |
|----------------|-------------------------------------|----------------------------------------------------|
|Pappers         |pappers.fr                           |Sociétés, dirigeants, comptes annuels, BODACC agrégé|
|Infogreffe      |infogreffe.fr                        |Registre officiel, actes, statuts                   |
|BODACC          |bodacc.fr                            |Publications légales                                |
|JO Associations |journal-officiel.gouv.fr/associations|Associations loi 1901                               |
|Légifrance      |legifrance.gouv.fr                   |Jurisprudence, textes de loi                        |
|Cadastre.gouv.fr|cadastre.gouv.fr                     |Parcelles (noms propriétaires non publics)          |
|Data.gouv.fr    |data.gouv.fr                         |Exports SIRENE, données ouvertes                    |
|HAVTP           |hatvp.fr                             |Déclarations intérêts et patrimoine élus            |
|Annuaire 118712 |118712.fr                            |Annuaire téléphonique fixe                          |
|PagesJaunes     |pagesjaunes.fr                       |Entreprises par activité                            |

#### C.2 Royaume-Uni

|Ressource        |URL                                                 |Usage                                       |
|-----------------|----------------------------------------------------|--------------------------------------------|
|Companies House  |gov.uk/government/organisations/companies-house     |Registre complet, PSC (UBO)                 |
|HM Land Registry |gov.uk/government/organisations/land-registry       |Propriété immobilière (partiellement payant)|
|OpenCharities    |opencharities.org                                   |Organismes à but non lucratif               |
|192.com          |192.com                                             |Annuaire (payant)                           |
|UK Sanctions List|gov.uk/government/publications/the-uk-sanctions-list|Sanctions                                   |

#### C.3 États-Unis

|Ressource                        |URL                           |Usage                                   |
|---------------------------------|------------------------------|----------------------------------------|
|SEC EDGAR                        |sec.gov/edgar                 |Sociétés cotées (10-K, 10-Q, 8-K, proxy)|
|Delaware Division of Corporations|corp.delaware.gov             |Registre Delaware (LLC et corps)        |
|Secretary of State (par État)    |varie par État                |Registres par État                      |
|FAA Registry                     |registry.faa.gov              |Aéronefs immatriculés US                |
|OFAC SDN                         |sanctionssearch.ofac.treas.gov|Sanctions US                            |
|PACER                            |pacer.uscourts.gov            |Dossiers judiciaires fédéraux (payant)  |
|PropertyShark                    |propertyshark.com             |Propriété immobilière                   |
|ThatsThem, FastPeopleSearch      |—                             |Annuaires US (VPN US requis)            |

#### C.4 Allemagne

|Ressource      |URL               |Usage                                      |
|---------------|------------------|-------------------------------------------|
|Handelsregister|handelsregister.de|Registre du commerce (partiellement payant)|
|Bundesanzeiger |bundesanzeiger.de |Publications légales                       |
|DasTelefonbuch |dastelefonbuch.de |Annuaire                                   |

#### C.5 Suisse

|Ressource |URL          |Usage                                 |
|----------|-------------|--------------------------------------|
|Zefix     |zefix.ch     |Registre fédéral du commerce (gratuit)|
|Moneyhouse|moneyhouse.ch|Agrégateur enrichi (payant)           |
|Monetas   |monetas.ch   |Publications légales                  |

#### C.6 Pays opaques (via ICIJ)

|Juridiction                    |Source principale                           |Note                                               |
|-------------------------------|--------------------------------------------|---------------------------------------------------|
|BVI (Îles Vierges britanniques)|ICIJ Offshore Leaks + registre BVI post-2017|Registre UBO partiellement accessible aux autorités|
|Cayman Islands                 |ICIJ + Cayman Registry (limité)             |Registre non public                                |
|Panama                         |ICIJ (Panama Papers)                        |Registre limité                                    |
|Chypre                         |Cyprus Department of Registrar of Companies |Partiellement public                               |
|Malte                          |Registry of Companies (MBR)                 |Public, interface en ligne                         |
|Luxembourg                     |RCS et RCB                                  |Public                                             |
|Île Maurice                    |Registrar of Companies                      |Partiellement public                               |
|Dubaï (UAE)                    |DIFC, ADGM, DED                             |Accès par juridiction interne                      |

#### C.7 Russie et post-soviétique

|Ressource             |URL              |Usage                                 |
|----------------------|-----------------|--------------------------------------|
|SPARK-Interfax        |spark-interfax.ru|Sociétés russes (payant)              |
|Kontur.Focus          |focus.kontur.ru  |Sociétés russes (payant)              |
|Federal Tax Service RU|egrul.nalog.ru   |Registre officiel (accès russe requis)|
|VK                    |vk.com           |Réseau social                         |
|OK.ru                 |ok.ru            |Réseau social                         |

*Note* : sanctions UE post-2022 rendent certains accès problématiques depuis l’UE.

#### C.8 Asie

|Pays        |Sources principales                                          |
|------------|-------------------------------------------------------------|
|Chine       |Qichacha (qcc.com), Tianyancha (tianyancha.com), Baidu, Weibo|
|Hong Kong   |HK Companies Registry, ICRIS                                 |
|Singapour   |ACRA BizFile                                                 |
|Japon       |National Tax Agency, Mixi, LINE                              |
|Corée du Sud|DART (dart.fss.or.kr), Naver, Daum                           |
|Inde        |Ministry of Corporate Affairs (mca.gov.in), LinkedIn         |

#### C.9 Agrégateurs internationaux

|Ressource              |URL                   |Usage                                          |
|-----------------------|----------------------|-----------------------------------------------|
|OpenCorporates         |opencorporates.com    |200M+ sociétés, 140 juridictions               |
|OpenSanctions          |opensanctions.org     |Sanctions + PEP agrégés                        |
|ICIJ Offshore Leaks    |offshoreleaks.icij.org|Données leaks (Panama, Paradise, Pandora, etc.)|
|Orbis (Bureau van Dijk)|—                     |Payant, exhaustif                              |
|Aleph (OCCRP)          |aleph.occrp.org       |Leaks structurés                               |

-----

### Annexe D — Cheat sheets opérationnelles

#### D.1 Par sélecteur — checklist du pivot

|Sélecteur de départ|Étapes clés                                                                                                                                      |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
|**Nom**            |Qualifier avec un 2e attribut (ville, employeur, DoB) → Pappers / Companies House / OpenCorporates → registres par pays → LinkedIn → Google dorks|
|**Email**          |HIBP → DeHashed → Holehe → Epieos → GHunt (si Google) → recherche directe du domaine                                                             |
|**Username**       |Sherlock → Maigret → WhatsMyName → Google dorks `"username"` → recherche manuelle plateformes majeures                                           |
|**Téléphone**      |TrueCaller / Sync.me → dump Facebook 2021 (via DeHashed/IntelX) → WhatsApp / Telegram / Signal (photo de profil) → annuaires nationaux           |
|**Photo**          |Google Images → Yandex Images → TinEye (datation) → Google Lens → PimEyes (pour identification) → FaceCheck.id                                   |
|**Adresse**        |Pappers (sociétés domiciliées) → OpenCorporates → cadastre → recherche immobilière locale → street view contextuel                               |
|**Domaine**        |Whois → Whois historique (DomainTools) → DNS (MX, TXT, NS) → crt.sh → Shodan → reverse IP                                                        |
|**Adresse crypto** |Explorateur (Blockchain.com, Etherscan, Tronscan) → Arkham → DeBank → OXT (Bitcoin clustering)                                                   |

#### D.2 Par plateforme — points d’attention

|Plateforme     |Techniques clés                                                                              |
|---------------|---------------------------------------------------------------------------------------------|
|**Google**     |site: filetype: intitle: inurl: AROUND(n) before:/after: “exact” -exclusion                  |
|**Yandex**     |Reconnaissance faciale + contenu non-anglophone                                              |
|**Facebook**   |site:facebook.com + dorks, extraction d’ID, groupes publics, check-ins, vie photos archivées |
|**Instagram**  |Profils publics, stories (capturer immédiatement), hashtags, localisations, tagged           |
|**LinkedIn**   |Google dorks OU avatar en mode privé OU compte premium privé — JAMAIS le compte perso        |
|**X / Twitter**|Recherche avancée (from/since/until/filter), archivage anticipé, instances Nitter (en déclin)|
|**Telegram**   |site:t.me, TGStat, Telepathy, bots @SangMata_bot, forwarding, compte dédié                   |
|**Discord**    |Disboard / Discadia pour trouver, compte dédié pour observer, DiscordChatExporter            |
|**Reddit**     |Reveddit pour posts supprimés, historique utilisateur                                        |
|**Dark web**   |Tails ou Whonix, Ahmia, observation passive uniquement                                       |

#### D.3 Par pays — premiers réflexes

|Cible basée en                  |Sources prioritaires                                                                    |
|--------------------------------|----------------------------------------------------------------------------------------|
|**France**                      |Pappers, BODACC, LinkedIn, Légifrance, HAVTP si PEP                                     |
|**UK**                          |Companies House + PSC, LinkedIn, HMLand Registry                                        |
|**US**                          |OpenCorporates, Secretary of State de l’État concerné, SEC EDGAR si coté, public records|
|**Allemagne**                   |Handelsregister, Bundesanzeiger, LinkedIn, Xing                                         |
|**Russie / CEI**                |SPARK, Yandex, VK, Search4Faces, OpenSanctions                                          |
|**Chine**                       |Qichacha, Tianyancha, Baidu, Weibo (traduction requise)                                 |
|**Offshore (BVI/Cayman/Panama)**|ICIJ Offshore Leaks d’abord, puis registre local si accessible                          |

-----

### Annexe E — Templates de livrables

#### E.1 Template : Rapport OSINT complet

```
[Page de garde]
- Titre : Rapport d'investigation OSINT — [Cible] — [Date]
- Classification : TLP:RED / TLP:AMBER / TLP:GREEN
- Émetteur : [Investigateur]
- Destinataire : [Client]
- Référence : [Numéro de mission]
- Version : [Numéro + date]

1. SOMMAIRE EXÉCUTIF (1 page)
   1.1 Contexte (3 lignes)
   1.2 Résultats clés (5-7 points avec niveau de confiance WEP)
   1.3 Schéma identifié
   1.4 Évaluation quantitative (si applicable)
   1.5 Recommandations principales

2. MANDAT ET PÉRIMÈTRE
   2.1 Commanditaire
   2.2 Questions d'investigation
   2.3 Contraintes (délai, budget, OPSEC, éthique)
   2.4 Livrables attendus

3. MÉTHODOLOGIE ET SOURCES
   3.1 Approche générale
   3.2 OPSEC déployée
   3.3 Catégories de sources mobilisées
   3.4 Outils utilisés

4. CONSTATATIONS COTÉES
   [Une entrée par fait : fait, source, cotation Admiralty, capture hashée, commentaire]

5. ANALYSE
   5.1 Matrice ACH
   5.2 Timeline
   5.3 Graphe relationnel (version simplifiée)
   5.4 Biais identifiés et neutralisés
   5.5 Raisonnement adversaire

6. CONCLUSIONS
   6.1 Réponse à QI-1 (niveau de confiance WEP)
   6.2 Réponse à QI-2 (niveau de confiance WEP)
   [...]

7. RECOMMANDATIONS
   7.1 Pistes de réquisitions (priorisées)
   7.2 Actions immédiates
   7.3 Investigations complémentaires suggérées
   7.4 Veille post-rapport

8. LIMITES ET ZONES D'INCERTITUDE
   8.1 Juridictions non couvertes
   8.2 Sources non accessibles
   8.3 Alternatives non invalidées

9. ANNEXES
   A. Liste complète des sources (URL, date, hash)
   B. Captures hashées (organisées par thème)
   C. Graphe complet
   D. Timeline détaillée
   E. Extraits de registres (version intégrale)
   F. Méthodologie détaillée (outils, versions, paramètres)
   G. Extraits pertinents du journal d'investigation
```

#### E.2 Template : Sommaire exécutif (1 page)

```
INVESTIGATION OSINT — [NOM] — [DATE]
TLP:[RED/AMBER/GREEN]

CONTEXTE
[3 lignes : mandat, cible, questions principales]

RÉSULTATS CLÉS
• [Conclusion 1] — [Confiance WEP]
• [Conclusion 2] — [Confiance WEP]
• [Conclusion 3] — [Confiance WEP]
• [Conclusion 4] — [Confiance WEP]
• [Conclusion 5] — [Confiance WEP]

SCHÉMA IDENTIFIÉ
[2-3 lignes de synthèse]

ÉVALUATION QUANTITATIVE
• Patrimoine non déclaré estimé : [montant]
• Flux identifiés : [montant]
• Période couverte : [dates]

RECOMMANDATIONS PRINCIPALES
1. [Action prioritaire]
2. [Action prioritaire]
3. [Action prioritaire]

CONTACT
[Investigateur — coordonnées]
```

#### E.3 Template : Fiche de cadrage

```
FICHE DE CADRAGE — MISSION [NUMÉRO]

CLIENT
- Cabinet / Entreprise :
- Contact principal :
- Référence de commande :

OBJET DE LA MISSION
- Description synthétique (5-10 lignes) :
- Contexte business ou judiciaire :

CIBLE(S)
- Personne(s) physique(s) :
- Société(s) :
- Autres entités :

SÉLECTEURS INITIAUX FOURNIS
- Noms :
- Emails :
- Téléphones :
- Adresses :
- Photos :
- Autres :

QUESTIONS D'INVESTIGATION (QI)
QI-1 : [formulation précise]
QI-2 : [formulation précise]
[...]

PÉRIMÈTRE
- Géographique :
- Temporel :
- Thématique :
- Ce qui est exclu :

CONTRAINTES
- Délai :
- Budget :
- OPSEC (niveau requis) :
- Règles éthiques particulières :

LIVRABLES ATTENDUS
- Format :
- Volumétrie estimée :
- Date de remise :
- Canal de transmission :
- Classification TLP :

CADRE JURIDIQUE
- Finalité légitime documentée : [oui / non — si non, refuser]
- Base légale RGPD : [intérêt légitime / mission d'intérêt public / autre]
- Durée de conservation prévue :

SIGNATURE CLIENT / INVESTIGATEUR
[Dates et signatures]
```

#### E.4 Template : Journal d’investigation (format type)

```
[YYYY-MM-DD HH:MM UTC]
Mission : [référence]
Sélecteur utilisé : [description]
Source consultée : [URL ou description]
Action : [ce qui a été fait]
Résultat : [ce qui a été trouvé]
Sélecteurs découverts : [liste]
Capture : [nom de fichier] (SHA-256: [hash])
Cotation : [Admiralty]
Notes : [observations, pistes, limites]
```

#### E.5 Template : Fiche d’entité

```
ENTITÉ : [Nom]
TYPE : [Personne / Société / Adresse crypto / Domaine / etc.]

IDENTIFIANTS
- [Sélecteur 1] : [valeur] — source : [X], cotation : [Y]
- [Sélecteur 2] : [valeur] — source : [X], cotation : [Y]

RELATIONS
- → [Entité] (type de relation) — source, cotation

HISTORIQUE
- [Date] : [événement] — source

COTATION GLOBALE DE L'ENTITÉ
- Identité confirmée : [Admiralty]
- Rôle attribué : [Admiralty]

NOTES D'INVESTIGATION
[...]
```

#### E.6 Template : Note de transmission aux autorités

```
OBJET : Transmission d'éléments OSINT — [Affaire] — [Référence]

À : [Service destinataire : C3N / PNF / OCLCTIC / TRACFIN / etc.]

ÉMETTEUR : [Cabinet d'avocats ou client, via investigateur]

CONTEXTE
[Description du contexte et de la qualification envisagée]

ÉLÉMENTS TRANSMIS
- Rapport OSINT complet ([X] pages, [X] annexes)
- Captures hashées ([nombre])
- Graphe relationnel
- Pistes de réquisitions identifiées ([nombre])

QUALIFICATION PÉNALE OU ADMINISTRATIVE ENVISAGÉE
[Articles du Code pénal / Code de commerce / réglementaires visés]

DEMANDES
- [Saisine / signalement / audition]
- [Actions attendues]

INVESTIGATEUR
- Disponibilité pour audition : [oui / dates]
- Coordonnées :

CLASSIFICATION : TLP:RED
```

-----

### Annexe F — Workflow d’enquête en 10 étapes (avec checklists)

#### Étape 1 — Cadrage

**Objectifs** : formuler les questions d’investigation, identifier les sélecteurs initiaux, définir le périmètre et les contraintes.

**Livrables** : fiche de cadrage signée (Annexe E.3).

**Checklist** :

- [ ] Les questions d’investigation sont formulées précisément (pas « enquêter sur X », mais « X contrôle-t-il Y, avec quelle structure ? »).
- [ ] Les sélecteurs initiaux sont listés exhaustivement.
- [ ] Le périmètre géographique, temporel et thématique est explicite.
- [ ] Les contraintes (délai, budget, OPSEC, règles éthiques) sont documentées.
- [ ] La finalité légitime RGPD est justifiable.
- [ ] Le mandat est formalisé par un contrat ou une lettre de mission.

**Pièges à éviter** : accepter une mission floue, ne pas documenter les limites acceptables, sous-estimer la durée.

#### Étape 2 — OPSEC

**Objectifs** : calibrer l’OPSEC sur le threat model, déployer l’infrastructure d’investigation.

**Livrables** : checklist OPSEC signée.

**Checklist** :

- [ ] Threat model évalué (sophistication cible, motivation, durée).
- [ ] VM dédiée créée (Ubuntu / Tails / Whonix selon le niveau).
- [ ] VPN dédié activé (pas le VPN perso).
- [ ] Profil navigateur vierge.
- [ ] Avatar(s) créé(s) et maturé(s) (3+ semaines avant usage).
- [ ] Téléphone d’investigation dédié (si nécessaire).
- [ ] Séparation stricte avec la machine perso (presse-papiers, fichiers).

**Pièges à éviter** : sur-confiance en une OPSEC rapide, réutilisation d’avatars, mélange perso/pro.

#### Étape 3 — Plan de collecte

**Objectifs** : lister les sources à mobiliser par question d’investigation, dans quel ordre, avec quels outils.

**Livrables** : plan de collecte documenté.

**Checklist** :

- [ ] Chaque QI a un plan associé.
- [ ] Les dépendances sont identifiées (QI-X nécessite QI-Y d’abord).
- [ ] Les outils sont listés avec leur statut (gratuit/payant, accessible/à acquérir).
- [ ] Une estimation de temps par phase est faite.
- [ ] Les sources secondaires sont prévues si les primaires échouent.

**Pièges à éviter** : plonger dans la collecte sans plan, sous-estimer l’effort sur certaines sources (par exemple coopération internationale).

#### Étape 4 — Collecte

**Objectifs** : exécuter le plan, documenter chaque action.

**Livrables** : journal d’investigation à jour, captures hashées.

**Checklist** (par action de collecte) :

- [ ] Entrée au journal créée avant l’action.
- [ ] Source consultée documentée (URL, date, heure UTC).
- [ ] Résultat consigné.
- [ ] Capture produite (Hunchly ou équivalent) et hashée.
- [ ] Sélecteurs découverts ajoutés au graphe.
- [ ] Cotation préliminaire.

**Pièges à éviter** : reporter la documentation à plus tard (perte garantie), ne pas capturer les données volatiles.

#### Étape 5 — Préservation

**Objectifs** : garantir la chaîne de custody des preuves.

**Livrables** : archive chiffrée des captures, Wayback Machine submissions.

**Checklist** :

- [ ] Chaque capture a un hash SHA-256 consigné.
- [ ] Les pages publiques importantes sont soumises à Wayback Machine.
- [ ] L’archive des captures est stockée de manière chiffrée (LUKS / VeraCrypt).
- [ ] Une copie backup chiffrée est tenue à jour.

**Pièges à éviter** : stockage non chiffré, pas de backup, pas de Wayback pour les pages sensibles.

#### Étape 6 — Traitement

**Objectifs** : nettoyer, organiser, dédupliquer les données collectées.

**Livrables** : vault Obsidian structuré, graphe Maltego initial.

**Checklist** :

- [ ] Une note par entité majeure dans Obsidian.
- [ ] Les entités sont liées dans le graphe Maltego.
- [ ] Les doublons sont fusionnés.
- [ ] Nomenclature de fichiers cohérente (`YYYYMMDD_source_selecteur_description.ext`).

**Pièges à éviter** : accumuler sans structurer, perdre du temps à retrouver des informations déjà collectées.

#### Étape 7 — Corrélation

**Objectifs** : identifier les liens entre entités, révéler les structures cachées.

**Livrables** : graphe Maltego enrichi, liste de pivots productifs.

**Checklist** :

- [ ] Chaque entité a été testée contre les autres via les pivots standards.
- [ ] Les grappes denses sont identifiées.
- [ ] Les nœuds centraux sont identifiés.
- [ ] Les liens transversaux inattendus sont documentés.

**Pièges à éviter** : se concentrer sur les pivots évidents et rater les liens latéraux.

#### Étape 8 — Analyse

**Objectifs** : ACH, cotation finale, timeline, identification des biais.

**Livrables** : matrice ACH complète, timeline, conclusions cotées en WEP.

**Checklist** :

- [ ] Au moins 3 hypothèses concurrentes formulées.
- [ ] Matrice ACH construite sur toutes les évidences majeures.
- [ ] Hypothèses éliminées documentées.
- [ ] Conclusions formulées en vocabulaire calibré (WEP).
- [ ] Biais potentiels identifiés et neutralisés.
- [ ] Raisonnement adversaire appliqué.

**Pièges à éviter** : sauter l’ACH par gain de temps apparent, rester sur l’hypothèse initiale.

#### Étape 9 — Production

**Objectifs** : rédiger le rapport exploitable.

**Livrables** : rapport complet + annexes (selon template E.1).

**Checklist** :

- [ ] Sommaire exécutif rédigé en dernier, une fois les conclusions stabilisées.
- [ ] Chaque fait cité porte une cotation et une source.
- [ ] Vocabulaire calibré respecté (pas de verdict, pas d’affirmation excessive).
- [ ] Limites et zones d’incertitude explicitement documentées.
- [ ] Graphe simplifié dans le corps + graphe complet en annexe.
- [ ] Revue par pair effectuée (ou relecture à 48h d’intervalle).

**Pièges à éviter** : rédiger à chaud dans l’enthousiasme de la découverte, excéder le vocabulaire calibré, négliger les annexes.

#### Étape 10 — Transmission et veille

**Objectifs** : remettre le rapport au client, mettre en place la veille post-rapport.

**Livrables** : rapport transmis de manière sécurisée + plan de veille activé.

**Checklist** :

- [ ] Format figé (PDF signé), annexes chiffrées.
- [ ] Canal sécurisé (ProtonMail, remise physique).
- [ ] Classification TLP explicite.
- [ ] Accusé de réception conservé.
- [ ] Alertes et monitoring activés pour la veille.
- [ ] Conservation des sources brutes planifiée (durée + destruction).

**Pièges à éviter** : transmission par email standard, oubli de la veille post-rapport, conservation indéfinie des sources.

-----

### Annexe G — Lab de l’investigateur, ressources et formations

#### G.1 Composition du lab

**Matériel recommandé** :

- Ordinateur dédié à l’investigation (séparé du poste personnel).
- Disque externe chiffré pour les archives (LUKS / VeraCrypt).
- Téléphone d’investigation avec SIM prépayée dédiée.
- Clé USB Tails (pour les missions ponctuelles à haut risque).

**Logiciels essentiels (gratuits / open source)** :

- **VM** : VirtualBox ou VMware Workstation.
- **Systèmes** : Ubuntu 24.04 LTS (VM principale), Tails (USB), Whonix (VM haut risque).
- **Navigateur** : Firefox avec profil dédié + uBlock Origin + Cookie AutoDelete.
- **Notes** : Obsidian (vault chiffré par enquête).
- **Graphe** : Maltego Community Edition.
- **Capture** : Hunchly (payant, 129 $/an) — ou alternative artisanale (extension SingleFile + ExifTool).
- **Python + bibliothèques OSINT** : Sherlock, Maigret, Holehe, Photon, Recon-ng.
- **Outils image** : ExifTool, GIMP (manipulation basique), outils FotoForensics en ligne.

**Abonnements recommandés** (niveau professionnel) :

- DeHashed (~15 $/mois) : breaches.
- DomainTools Historical Whois (~200 $/mois) : crucial pour les investigations domain-heavy.
- PimEyes (~30 €/mois) : reconnaissance faciale.
- Pappers (accès étendu, ~50 €/mois) : données françaises enrichies.
- SecurityTrails (freemium à pro) : DNS et infrastructure.

**Abonnements avancés** (niveau agence) :

- Maltego Pro (~1 800 $/an) : transforms étendues.
- OpenCorporates API (selon volume).
- Flare / Recorded Future / Cybersixgill : monitoring dark web (coûteux).
- WorldCheck / LexisNexis Bridger : PEP et sanctions.

#### G.2 Formations

|Formation                                       |Organisme                        |Focus                                   |Durée / Tarif                       |
|------------------------------------------------|---------------------------------|----------------------------------------|------------------------------------|
|**SEC497 / GOSI**                               |SANS / GIAC                      |OSINT générale, référence mondiale      |6 jours / ~8 000 $                  |
|**PORP** (Practical OSINT Research Professional)|TCM Security                     |OSINT pratique, orientation terrain     |Self-paced / ~200 $                 |
|**OSIP** (Open Source Intelligence Professional)|IntelTechniques (Michael Bazzell)|Méthodologie complète, livre + formation|Livre + formation optionnelle       |
|**Bellingcat workshops**                        |Bellingcat                       |GEOINT, vérification                    |Ateliers réguliers, tarifs variables|
|**OSINT Curious**                               |Communauté OSINT Curious         |Webinaires, CTF                         |Gratuit                             |
|**MISP Training**                               |CIRCL                            |CTI et partage de renseignement         |Gratuit en ligne                    |

#### G.3 Communautés et veille

|Ressource                    |Type                   |Contenu                                    |
|-----------------------------|-----------------------|-------------------------------------------|
|**Sector035 — Week in OSINT**|Newsletter hebdomadaire|Agrégateur d’actualités et outils OSINT    |
|**OSINT Curious**            |Podcast + blog + CTF   |Communauté francophone/anglophone          |
|**Bellingcat**               |Site d’investigation   |Méthodologies, cas documentés, exercices   |
|**Trace Labs**               |CTF humanitaire        |Recherche de personnes disparues (éthique) |
|**SANS OSINT Blog**          |Blog                   |Articles techniques de niveau professionnel|
|**OSINT Framework**          |Annuaire               |Cartographie des outils (à date variable)  |
|**r/OSINT**                  |Subreddit              |Communauté large, niveaux variés           |

#### G.4 CTF d’entraînement

Les CTF (Capture The Flag) OSINT sont la meilleure école pratique.

- **Trace Labs Global Search Parties** : CTF humanitaires pour retrouver des personnes disparues. Ouverts au grand public, format compétition, encadrement éthique strict.
- **Bellingcat challenges** : exercices publics de géolocalisation et vérification, sur twitter.com/Quiztime ou dans les articles Bellingcat.
- **OSINT Dojo** : plateforme gratuite d’exercices progressifs.
- **Sans OSINT CTF** : événements ponctuels de niveau professionnel.

#### G.5 Lectures recommandées

**Fondamentaux** :

- Michael Bazzell, *Open Source Intelligence Techniques* (mise à jour régulière) — référence opérationnelle.
- Nihad Hassan, Rami Hijazi, *Open Source Intelligence Methods and Tools* — complément méthodologique.
- Richards Heuer, *Psychology of Intelligence Analysis* (gratuit en ligne, CIA) — sur l’ACH et les biais.

**Approfondissement** :

- Benjamin Strick, Eliot Higgins (Bellingcat), méthodologies en ligne.
- Publications ICIJ (Pandora, Panama, Paradise Papers) — cas d’études concrets.
- Rapports Chainalysis, TRM Labs (annuels) — pour la crypto.

**Veille continue** :

- Blog Sector035, newsletter OSINT Curious, rapports ENISA et ANSSI pour le contexte européen.

-----

> **Note de clôture**
> 
> Ce cours a été conçu comme un cours OSINT **autonome et complet** — la ressource de référence pour mener une investigation en sources ouvertes de bout en bout, sans dépendre d’autres ressources pour les sous-domaines spécialisés (SOCMINT, GEOINT, crypto, DARKINT, FININT en accès ouvert, CTI-OSINT).
> 
> L’opération **MIRAGE** a illustré, sur douze épisodes, la réalité d’une investigation OSINT professionnelle : les pivots s’enchaînent (un email vers un username, vers des comptes, vers des sociétés, vers des transactions crypto, vers une campagne de désinformation), chaque fait est coté (Admiralty A-F / 1-6, pas un exercice académique mais ce qui distingue le renseignement du bruit), et les limites sont explicites (une corrélation n’est pas une preuve, un outil de détection n’est pas un verdict, l’absence de preuve de manipulation n’est pas une preuve d’authenticité).
> 
> Le cours assume trois convictions. Première : l’OSINT est une **discipline de renseignement**, pas une collection d’outils — les outils changent tous les six mois, la méthodologie reste. Deuxième : chaque sous-domaine est enseigné **de manière suffisamment complète pour être opérationnel seul**. Troisième : la **vérification** est la compétence OSINT la plus critique en 2025-2026 — face à la prolifération des contenus synthétiques et aux restrictions croissantes des plateformes, un analyste qui ne vérifie pas systématiquement et qui ne documente pas ses limites produit du bruit, pas du renseignement.
> 
> *Investiguer avec méthode • Collecter avec rigueur • Vérifier avec discipline • Analyser avec probité • Documenter avec précision — et toujours distinguer ce qu’on sait de ce qu’on suppose.*