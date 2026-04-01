# LE DARK WEB — COMPRENDRE, NAVIGUER, INVESTIGUER

*Architecture • Écosystèmes • OPSEC • Investigation • Renseignement*

**Cours complet — 38 chapitres • 8 parties • 7 annexes**

*Infrastructures anonymes • Marchés clandestins • Communautés illicites • Investigation et renseignement*

---

## Table des matières

- [Fil rouge : Opération DARKSTREAM](#fil-rouge--opération-darkstream)
- **PARTIE I — FONDATIONS : COMPRENDRE LE DARK WEB (Ch.1-4)**
  - [Ch.1 — Internet, web visible, deep web, dark web : remettre les mots à l'endroit](#chapitre-1--internet-web-visible-deep-web-dark-web--remettre-les-mots-à-lendroit)
  - [Ch.2 — Histoire et évolution des darknets](#chapitre-2--histoire-et-évolution-des-darknets)
  - [Ch.3 — Pourquoi le dark web existe](#chapitre-3--pourquoi-le-dark-web-existe)
  - [Ch.4 — Le dark web comme écosystème](#chapitre-4--le-dark-web-comme-écosystème)
- **PARTIE II — INFRASTRUCTURES TECHNIQUES ET ANONYMAT (Ch.5-9)**
  - [Ch.5 — Architecture de Tor](#chapitre-5--architecture-de-tor)
  - [Ch.6 — Onion services et services cachés](#chapitre-6--onion-services-et-services-cachés)
  - [Ch.7 — I2P, Freenet et réseaux alternatifs](#chapitre-7--i2p-freenet-et-réseaux-alternatifs)
  - [Ch.8 — Cryptomonnaies et anonymat financier](#chapitre-8--cryptomonnaies-et-anonymat-financier)
  - [Ch.9 — Hébergement, infrastructure et résilience des services clandestins](#chapitre-9--hébergement-infrastructure-et-résilience-des-services-clandestins)
- **PARTIE III — ÉCOSYSTÈMES DU DARK WEB : ESPACES, ACTEURS ET CULTURE (Ch.10-15)**
  - [Ch.10 — Forums clandestins : culture, hiérarchie et codes](#chapitre-10--forums-clandestins--culture-hiérarchie-et-codes)
  - [Ch.11 — Marchés du dark web : histoire, fonctionnement et évolution](#chapitre-11--marchés-du-dark-web--histoire-fonctionnement-et-évolution)
  - [Ch.12 — Leak sites, blogs d'extorsion et vitrines de revendication](#chapitre-12--leak-sites-blogs-dextorsion-et-vitrines-de-revendication)
  - [Ch.13 — Canaux, chats et messageries clandestines](#chapitre-13--canaux-chats-et-messageries-clandestines)
  - [Ch.14 — Données volées et marchés de la fuite](#chapitre-14--données-volées-et-marchés-de-la-fuite)
  - [Ch.15 — Services criminels : du crime-as-a-service aux profils d'acteurs](#chapitre-15--services-criminels--du-crime-as-a-service-aux-profils-dacteurs)
- **PARTIE IV — ÉCONOMIE CLANDESTINE ET MÉCANISMES DE CONFIANCE (Ch.16-19)**
  - [Ch.16 — Pourquoi l'économie du dark web fonctionne](#chapitre-16--pourquoi-léconomie-du-dark-web-fonctionne)
  - [Ch.17 — Réputation, escrow, vouching et arbitrage](#chapitre-17--réputation-escrow-vouching-et-arbitrage)
  - [Ch.18 — Arnaques, exit scams et manipulation de la confiance](#chapitre-18--arnaques-exit-scams-et-manipulation-de-la-confiance)
  - [Ch.19 — Modèles économiques criminels observés via le dark web](#chapitre-19--modèles-économiques-criminels-observés-via-le-dark-web)
- **PARTIE V — INVESTIGATION, VEILLE ET COLLECTE (Ch.20-25)**
  - [Ch.20 — Cadre juridique, éthique et sécurité de l'analyste](#chapitre-20--cadre-juridique-éthique-et-sécurité-de-lanalyste)
  - [Ch.21 — OPSEC opérationnelle pour l'investigation dark web](#chapitre-21--opsec-opérationnelle-pour-linvestigation-dark-web)
  - [Ch.22 — Naviguer et collecter : méthodes, outils et limites](#chapitre-22--naviguer-et-collecter--méthodes-outils-et-limites)
  - [Ch.23 — Pivoting, enrichissement et corrélation OSINT](#chapitre-23--pivoting-enrichissement-et-corrélation-osint)
  - [Ch.24 — Veille dark web : surveillance, alerting et réduction du bruit](#chapitre-24--veille-dark-web--surveillance-alerting-et-réduction-du-bruit)
  - [Ch.25 — Preuve, capture et documentation](#chapitre-25--preuve-capture-et-documentation)
- **PARTIE VI — ANALYSE, RENSEIGNEMENT ET PRODUCTION (Ch.26-30)**
  - [Ch.26 — Dé-anonymisation : méthodes et limites](#chapitre-26--dé-anonymisation--méthodes-et-limites)
  - [Ch.27 — Traçage crypto et analyse financière](#chapitre-27--traçage-crypto-et-analyse-financière)
  - [Ch.28 — Pièges analytiques, désinformation et faux signaux](#chapitre-28--pièges-analytiques-désinformation-et-faux-signaux)
  - [Ch.29 — Transformer les observations en renseignement actionnable](#chapitre-29--transformer-les-observations-en-renseignement-actionnable)
  - [Ch.30 — Produire une note analytique](#chapitre-30--produire-une-note-analytique)
- **PARTIE VII — CAS D'USAGE, TENDANCES ET PROSPECTIVE (Ch.31-34)**
  - [Ch.31 — Ransomware, extorsion et leak sites](#chapitre-31--ransomware-extorsion-et-leak-sites)
  - [Ch.32 — Dark web, influence et opérations informationnelles](#chapitre-32--dark-web-influence-et-opérations-informationnelles)
  - [Ch.33 — Hacktivisme, zones grises et usages légitimes](#chapitre-33--hacktivisme-zones-grises-et-usages-légitimes)
  - [Ch.34 — Forces de l'ordre, disruption et droit international](#chapitre-34--forces-de-lordre-disruption-et-droit-international)
- **PARTIE VIII — ÉTUDES DE CAS ET SYNTHÈSE (Ch.35-38)**
  - [Ch.35 — Cas complet : investigation d'une vente de données industrielles](#chapitre-35--cas-complet--investigation-dune-vente-de-données-industrielles)
  - [Ch.36 — Cas complet : surveillance d'un leak site ransomware](#chapitre-36--cas-complet--surveillance-dun-leak-site-ransomware)
  - [Ch.37 — Cas complet : traque d'un IAB vendant des accès](#chapitre-37--cas-complet--traque-dun-iab-vendant-des-accès)
  - [Ch.38 — Maturité analyste et programme de veille durable](#chapitre-38--maturité-analyste-et-programme-de-veille-durable)
- **ANNEXES**
  - [Annexe A — Glossaire](#annexe-a--glossaire)
  - [Annexe B — Typologie des espaces dark web](#annexe-b--typologie-des-espaces-dark-web)
  - [Annexe C — OPSEC analyste : checklists](#annexe-c--opsec-analyste--checklists)
  - [Annexe D — Outils d'investigation dark web](#annexe-d--outils-dinvestigation-dark-web)
  - [Annexe E — Grille d'évaluation de crédibilité](#annexe-e--grille-dévaluation-de-crédibilité)
  - [Annexe F — Templates de livrables](#annexe-f--templates-de-livrables)
  - [Annexe G — Ressources et veille](#annexe-g--ressources-et-veille)

---

## Fil rouge : Opération DARKSTREAM

> **Contexte narratif — ce fil rouge traverse les 30 premiers chapitres du cours et se conclut au Ch.35.**
>
> **Lucas Ferreira**, analyste CTI senior chez **Athéna Group** (cabinet de conseil en intelligence économique et cybersécurité, 60 consultants, clients CAC 40 et institutions publiques), reçoit un mandat de **Vectris Aerospace**, équipementier aérospatial européen de 4 500 collaborateurs coté au SBF 120. Vectris a subi une compromission détectée 3 mois plus tôt (traitée par le cours IR de la bibliothèque). L'investigation interne a confirmé l'exfiltration de 420 Go de données techniques, dont des spécifications de composants de propulsion classifiées « Confidentiel Entreprise ». Malgré l'éradication de l'attaquant, une inquiétude persiste : les données sont-elles en circulation sur le dark web ?
>
> Le mandat de Lucas est précis : identifier si les données de Vectris circulent sur le dark web (forums, marchés, canaux Telegram), évaluer l'authenticité et l'étendue de la fuite, cartographier l'écosystème autour de la vente (qui vend, via quel canal, quel modèle économique, quels acheteurs potentiels), évaluer la menace résiduelle (les données sont-elles toujours en circulation ? d'autres acteurs les ont-ils acquises ?), et produire un rapport actionnable pour Vectris et potentiellement pour la DGSI (les données sont liées à des programmes de défense).
>
> L'investigation va le mener des forums russophones spécialisés dans les données industrielles aux canaux Telegram de revente, des services d'escrow crypto aux tentatives d'authentification des échantillons, en confrontant à chaque étape des questions d'OPSEC (comment naviguer sans alerter le vendeur), de méthodologie (comment distinguer un vrai leak d'un scam), de droit (un analyste privé peut-il payer pour accéder à un forum criminel ?), et de rigueur analytique (comment qualifier une information trouvée dans un espace où la manipulation est la norme).
>
> Le cours suit Lucas à chaque étape — de la configuration de son poste d'investigation à la rédaction de sa note analytique finale.

---

## PARTIE I — FONDATIONS : COMPRENDRE LE DARK WEB

*Avant de naviguer : comprendre ce qu'est réellement le dark web, d'où il vient, pourquoi il existe, et comment il fonctionne comme écosystème — pas comme simple collection de « sites cachés ».*

---

### Chapitre 1 — Internet, web visible, deep web, dark web : remettre les mots à l'endroit

#### 1.1 Internet n'est pas le web

La confusion commence ici. **Internet** est le réseau physique mondial — un ensemble de câbles sous-marins, de fibres optiques, de routeurs, et de protocoles (TCP/IP) qui relient des milliards de machines. Internet transporte de l'email, du streaming vidéo, du trafic VPN, des requêtes DNS, du pair-à-pair, et bien d'autres choses. Le **web** (World Wide Web) est un service qui fonctionne sur Internet, basé sur le protocole HTTP/HTTPS et le langage HTML — c'est ce qu'on consulte avec un navigateur. Le web n'est qu'une partie d'Internet — une partie importante, certes, mais pas la totalité. Confondre Internet et web, c'est confondre le réseau routier et les magasins qu'on peut atteindre en voiture.

#### 1.2 Les trois couches du web

Le **surface web** (ou web de surface, ou clearnet dans le jargon) est l'ensemble des pages web indexées par les moteurs de recherche (Google, Bing, Yandex). C'est ce que la plupart des gens considèrent comme « Internet ». En termes de volume, le surface web représente une fraction modeste du contenu web total — les estimations varient entre 5 et 10 %, selon les méthodologies de comptage.

Le **deep web** est l'ensemble des contenus web qui ne sont pas indexés par les moteurs de recherche. C'est la couche la plus vaste et la plus banale : les intranets d'entreprise, les bases de données académiques, le contenu derrière des formulaires d'authentification (votre compte bancaire en ligne, votre boîte email, vos factures EDF), les archives non indexées, les pages dynamiques générées à la demande. Le deep web représente environ 90 % du contenu web. La quasi-totalité est parfaitement légale et ennuyeuse. Quand on parle du deep web, on ne parle PAS de cybercriminalité — on parle de tout ce que Google ne voit pas.

Le **dark web** est un sous-ensemble du deep web, accessible uniquement via des réseaux d'anonymisation spécifiques — principalement Tor (sites `.onion`), mais aussi I2P (eepsites), Freenet, et d'autres darknets. Le dark web n'est pas simplement « non indexé » — il est volontairement caché, hébergé sur des infrastructures d'anonymisation qui masquent l'identité du serveur et du visiteur. En volume, le dark web est une fraction minuscule d'Internet : quelques centaines de milliers de domaines .onion, dont la majorité sont inactifs, abandonnés, ou dupliqués.

#### 1.3 Darknets vs dark web

Un **darknet** est un réseau overlay (superposé à Internet) conçu pour l'anonymat : Tor est un darknet, I2P est un darknet, Freenet est un darknet. Le dark web est l'ensemble des contenus accessibles via ces darknets. La distinction est technique mais utile : on peut accéder au réseau Tor sans visiter de site .onion (simplement en utilisant Tor comme proxy pour naviguer sur le web classique de manière anonyme), et on peut visiter un site .onion (dark web) uniquement si on utilise le réseau Tor (darknet).

#### 1.4 Pourquoi le terme « dark web » est souvent mal utilisé

Les médias et le grand public utilisent « dark web » comme synonyme de « cybercriminalité ». Cette confusion est dommageable pour trois raisons. Elle surestime le dark web comme espace criminel (beaucoup d'activité cybercrimminelle se déroule sur le clear web — forums à accès restreint, Telegram, Discord, pastebins). Elle sous-estime les usages légitimes du dark web (contournement de censure, protection des sources, communication sécurisée). Et elle crée une fascination sensationnaliste (« le dark web, lieu de tous les dangers ») qui obscurcit la réalité : le dark web est un espace relativement petit, souvent lent, fréquemment en panne, et rempli d'arnaques. L'analyste professionnel doit s'en départir.

#### 1.5 Ordres de grandeur

Combien de sites .onion existent ? Les mesures du Tor Project (metrics.torproject.org) comptent en 2025-2026 environ 100 000 à 150 000 adresses .onion v3 uniques observées par le réseau, dont une fraction (estimée à 10-30 %) est active à un moment donné. Parmi les sites actifs, les études académiques (DarkOwl, Recorded Future) estiment qu'environ 50-60 % sont des sites légitimes, des miroirs de sites de surface, ou des pages abandonnées ; 20-30 % sont des arnaques ou des sites frauduleux ; et 10-20 % hébergent du contenu manifestement illicite (marchés, forums criminels, contenu d'abus). Le dark web est beaucoup plus petit et beaucoup plus chaotique que ce que la plupart des gens imaginent.

#### 1.6 Fil rouge — DARKSTREAM : le point de départ

> **🌐 DARKSTREAM — Épisode 1**
>
> Lucas reçoit le brief de Vectris Aerospace. Les données techniques exfiltrées (spécifications de composants, plans CAD, rapports de tests) auraient été repérées sur un forum .onion russophone spécialisé dans les données industrielles. L'information vient d'un service de monitoring dark web (Recorded Future), qui a détecté une mention de « Vectris » et de « propulsion specs » dans un post daté de 10 jours.
>
> Première tâche de Lucas : vérifier l'information. Les alertes de monitoring dark web sont fréquemment des faux positifs — le mot « Vectris » peut apparaître dans un contexte différent, les « propulsion specs » peuvent être recyclées d'une fuite antérieure non liée. Avant de mobiliser des ressources, il faut vérifier.

---

### Chapitre 2 — Histoire et évolution des darknets

#### 2.1 Les origines : anonymat et recherche militaire

L'histoire des darknets ne commence pas avec la cybercriminalité — elle commence avec la recherche en confidentialité des communications. Dans les années 1990, le **Naval Research Laboratory** (NRL) américain développe l'onion routing comme technique de protection des communications de renseignement. Le principe est simple mais puissant : si le trafic est chiffré en couches et acheminé via des relais multiples, aucun observateur ne peut relier l'émetteur au destinataire. Le premier prototype de réseau onion routing est déployé en 1998.

En 2002, Roger Dingledine, Nick Mathewson, et Paul Syverson (ce dernier du NRL) lancent le **Tor Project** — une implémentation open source de l'onion routing accessible au public. Le paradoxe fondamental est posé dès l'origine : un réseau d'anonymat ne fonctionne que si suffisamment de personnes l'utilisent (l'anonymat repose sur le fait que le trafic de chaque utilisateur est indistinguable dans la masse). Si seuls les agents de renseignement américains utilisent Tor, tout le trafic sortant de Tor est attribuable à la CIA. Il faut donc que des citoyens ordinaires, des journalistes, des activistes — et inévitablement des criminels — l'utilisent aussi. Le gouvernement américain finance Tor tout en cherchant à le compromettre quand il est utilisé à des fins criminelles. Ce paradoxe n'a jamais été résolu.

#### 2.2 L'ère Silk Road (2011-2013)

**Silk Road**, créé par Ross Ulbricht (alias « Dread Pirate Roberts »), est le premier darknet market généraliste à atteindre une échelle significative. Lancé en février 2011, il combine Tor (pour l'anonymat) et Bitcoin (pour les paiements) dans un modèle d'e-commerce clandestin inspiré d'eBay : listings de produits, système de réputation par étoiles, et escrow géré par la plateforme. Le catalogue est dominé par les stupéfiants, avec une politique de refus des armes, du CSAM, et des services de violence. Silk Road atteint environ 1,2 million de transactions avant sa saisie par le FBI en octobre 2013. Ulbricht est identifié via une combinaison d'erreurs OPSEC : un post sur StackOverflow avec son vrai email mentionnant un projet similaire à Silk Road, un pseudonyme « Frosty » utilisé sur un forum de champignons hallucinogènes et relié à son identité réelle, et un serveur CAPTCHA mal configuré qui a leaké l'IP du serveur.

#### 2.3 La professionnalisation (2014-2019)

Après Silk Road, l'écosystème se professionnalise. **AlphaBay** (2014-2017, opéré par Alexandre Cazes) devient le plus grand darknet market de l'histoire, avec plus de 250 000 listings et des centaines de millions de dollars de transactions. Sa saisie en juillet 2017 (Operation Bayonet) est couplée avec l'infiltration de **Hansa Market** par la police néerlandaise — les utilisateurs fuyant AlphaBay vers Hansa tombent dans un piège policier opéré pendant 30 jours. Les saisies successives (Dream Market, Wall Street Market) illustrent un cycle récurrent : création → croissance → saisie ou exit scam → migration des utilisateurs vers le marché suivant.

#### 2.4 Hydra et la domination russophone (2015-2022)

**Hydra Market** (2015-2022) est le plus grand marché jamais opéré en termes de volume financier — environ 5,2 milliards de dollars de transactions cumulées selon les estimations de Chainalysis. Opéré exclusivement en russe, Hydra couvre les stupéfiants (avec un système de « dead drops » physiques unique en Russie), le blanchiment d'argent, les services de hacking, et les données volées. Sa saisie par les autorités allemandes en avril 2022 crée un vide immédiat dans l'écosystème russophone — aucun successeur unique n'émerge, et le marché se fragmente entre plusieurs plateformes de taille moyenne.

#### 2.5 L'ère post-Hydra et les tendances 2024-2026

Depuis 2022, l'écosystème est en fragmentation. Les marchés généralistes (qui vendent de tout) sont progressivement remplacés par des marchés spécialisés (marchés de données, marchés de stupéfiants, marchés de services techniques). Telegram émerge comme un concurrent direct du dark web pour le commerce cybercriminel — plus accessible, plus rapide, mais avec moins d'anonymat et une dépendance envers un tiers (Telegram peut fermer les canaux, et l'a fait de manière plus agressive après l'arrestation de Pavel Durov en France en août 2024). La tendance est à l'hybridation : les acteurs utilisent le dark web pour les activités nécessitant un anonymat fort, et Telegram pour les interactions rapides et la promotion.

#### 2.6 Fil rouge — DARKSTREAM : le forum ciblé

> **🌐 DARKSTREAM — Épisode 2**
>
> Le forum identifié par le monitoring est **IndustrialLeaks**, un forum .onion russophone créé en 2022, spécialisé dans la vente de données industrielles et de propriété intellectuelle. Il compte environ 3 000 membres enregistrés (estimation basée sur les numéros de comptes visibles). L'accès nécessite soit un vouching par un membre existant, soit un paiement de 0,005 BTC. Le forum a changé 3 fois d'adresse .onion en 18 mois — signe de DDoS fréquents ou de migrations préventives. Il dispose d'un miroir I2P. Lucas note ces éléments dans sa fiche de plateforme (template en Annexe F).

---

### Chapitre 3 — Pourquoi le dark web existe

#### 3.1 L'anonymat comme besoin fondamental

Le dark web n'existe pas « parce que des criminels veulent se cacher ». Il existe parce que l'anonymat en ligne répond à des besoins fondamentaux que le web de surface ne satisfait pas.

La **résistance à la censure** : dans les régimes autoritaires (Chine, Iran, Russie, Biélorussie, Myanmar), l'accès à des informations non censurées est un acte de résistance. Tor permet d'accéder à Wikipedia, à des médias indépendants, et à des réseaux sociaux bloqués par les pare-feu étatiques (le « Great Firewall » chinois, le système de filtrage iranien). L'ONG Reporters Sans Frontières opère des miroirs .onion de sites d'information censurés. Le Tor Project développe des bridges (relais non listés) spécifiquement pour contourner les systèmes de détection et de blocage de Tor déployés par ces régimes.

La **protection des sources journalistiques** : les plateformes comme **SecureDrop** (déployée par le New York Times, le Guardian, Le Monde, ProPublica, et des dizaines d'autres médias) permettent aux lanceurs d'alerte de transmettre des documents de manière anonyme à des journalistes. Chaque instance SecureDrop est un hidden service Tor. Les affaires WikiLeaks, Panama Papers, et LuxLeaks n'auraient pas été possibles sans des canaux de communication anonymes.

La **vie privée comme droit fondamental** : l'article 8 de la Convention européenne des droits de l'homme protège le droit au respect de la vie privée. L'article 12 de la Déclaration universelle des droits de l'homme protège contre les immixtions arbitraires dans la vie privée. L'anonymat en ligne est un instrument de ces droits — utilisé par des individus qui ne veulent pas que leur activité en ligne soit surveillée par leur gouvernement, leur employeur, ou des entreprises publicitaires.

#### 3.2 L'anonymat comme facilitateur criminel

L'anonymat qui protège les dissidents protège aussi les criminels. Le dark web offre aux acteurs malveillants un espace où l'identification est difficile, les transactions sont pseudonymes (Bitcoin) ou anonymes (Monero), et l'infrastructure est résistante aux saisies (les hidden services n'ont pas d'adresse IP publique). Les usages criminels incluent le commerce de stupéfiants, la vente de données volées, les services cybercriminels (malware, ransomware, DDoS), les documents contrefaits, et dans les cas les plus graves, le CSAM (Child Sexual Abuse Material) et le financement du terrorisme.

L'analyste professionnel doit comprendre les deux faces — les usages légitimes et les usages criminels — sans naïveté ni sensationnalisme. Le dark web n'est ni un repaire de super-criminels ni un simple outil de liberté. C'est un espace d'anonymat, et l'anonymat est moralement neutre — c'est l'usage qui est qualifiable.

#### 3.3 La tension fondamentale

La tension entre vie privée et sécurité publique est au cœur de tous les débats sur le dark web. Les positions vont de « l'anonymat total est un droit fondamental inaliénable » (position de l'EFF, du Tor Project, d'Access Now) à « les forces de l'ordre doivent pouvoir accéder à toutes les communications pour prévenir les crimes graves » (position de certains gouvernements, notamment dans le cadre des débats sur le chiffrement en Europe — proposition de règlement « Chat Control »). L'analyste CTI se situe au milieu de cette tension : il utilise les outils d'anonymat pour son investigation tout en contribuant à la lutte contre les activités criminelles qui abusent de ces mêmes outils.

---

### Chapitre 4 — Le dark web comme écosystème

#### 4.1 Au-delà du « site caché »

Le dark web n'est pas une collection de sites isolés — c'est un écosystème interconnecté avec ses propres communautés, ses marchés, ses intermédiaires, ses règles sociales, et ses dynamiques de pouvoir. Comprendre le dark web comme un écosystème (plutôt que comme une liste de sites) est la première étape pour l'analyser efficacement.

L'écosystème comprend des **espaces** (forums, marchés, leak sites, canaux de communication), des **acteurs** (vendeurs, acheteurs, opérateurs, modérateurs, arbitres, escrocs), des **mécanismes de confiance** (réputation, escrow, vouching), des **flux financiers** (crypto, mixing, blanchiment), et des **dépendances techniques** (hébergement, réseau Tor, infrastructure DNS). Chaque composante est interdépendante : un marché a besoin de vendeurs (qui viennent des forums), d'un système de paiement (crypto), d'un hébergement (bulletproof), et d'une réputation (construite sur la durée). La disruption d'une composante affecte l'ensemble.

#### 4.2 Les interactions entre le dark web et les autres espaces

Le dark web n'est pas un espace hermétique. Il interagit constamment avec le surface web (les vendeurs font leur promotion sur Telegram et Discord avant de rediriger vers leurs services .onion), avec les réseaux sociaux (les revendications de ransomware sur les leak sites .onion sont relayées par des comptes Twitter/X et des journalistes spécialisés), avec les écosystèmes crypto (les paiements transitent par des exchanges qui opèrent sur le clear web), et avec le monde physique (les stupéfiants vendus en ligne sont livrés par la poste ; les dead drops de Hydra étaient dissimulés dans des parcs publics en Russie).

Le dark web est un nœud dans un réseau plus large — pas un silo isolé. L'analyste qui ne surveille que le dark web rate la majorité de l'activité criminelle, qui se déroule aussi (et de plus en plus) sur Telegram, les forums du clear web à accès restreint, et les pastebins éphémères.

#### 4.3 Les limites du dark web comme source de renseignement

Le dark web est une source de renseignement précieuse mais partielle et biaisée. Ce qui est visible sur le dark web n'est pas représentatif de l'ensemble de l'activité criminelle — c'est ce que les acteurs ont choisi de rendre visible (pour vendre, pour recruter, pour revendiquer). Les transactions les plus sensibles et les plus lucratives se font souvent en privé (messages directs, canaux chiffrés). Les données publiées sur les forums ne sont pas nécessairement fiables (scams, recyclage, intoxication). Et la couverture des outils de monitoring automatisé est incomplète (les forums les plus fermés ne sont pas indexés). L'analyste doit garder à l'esprit ces limitations tout au long de son investigation — ce qui est développé au Ch.28 (pièges analytiques).

#### 4.4 Fil rouge — DARKSTREAM : cartographier l'écosystème

> **🌐 DARKSTREAM — Épisode 3**
>
> Avant de plonger dans IndustrialLeaks, Lucas cartographie l'écosystème autour de la menace. Le monitoring Recorded Future indique que « aero_source » (le pseudo du vendeur) est actif sur IndustrialLeaks (forum .onion) mais aussi sur un canal Telegram privé (identifié par une mention croisée sur un autre forum anglophone). Les données seraient aussi promues sur XSS (forum russophone de référence, accessible sur Tor et sur le clear web avec VPN). Lucas identifie 3 espaces à surveiller en parallèle : IndustrialLeaks (source primaire), le canal Telegram (promotion), et XSS (visibilité communautaire). C'est un écosystème, pas un site isolé.

---

## PARTIE II — INFRASTRUCTURES TECHNIQUES ET ANONYMAT

*Comprendre comment ça fonctionne réellement — pas la version vulgarisée. L'architecture de Tor, les services cachés, les réseaux alternatifs, les cryptomonnaies, et l'infrastructure qui soutient les services clandestins.*

---

### Chapitre 5 — Architecture de Tor

#### 5.1 L'onion routing en détail

Le concept fondamental de Tor est le chiffrement en couches (d'où la métaphore de l'oignon). Quand un utilisateur Tor veut se connecter à un serveur, le client Tor construit un **circuit** à travers 3 relais (minimum) du réseau. Le message est chiffré en 3 couches successives (une couche par relais). Le premier relais (guard node) déchiffre la couche extérieure et découvre l'adresse du second relais, sans connaître la destination finale. Le second relais (middle relay) déchiffre la couche suivante et découvre l'adresse du troisième relais, sans connaître ni l'émetteur ni la destination. Le troisième relais (exit node) déchiffre la dernière couche et envoie le trafic vers la destination finale, sans connaître l'émetteur.

Résultat : le guard node connaît l'IP de l'utilisateur mais pas sa destination. L'exit node connaît la destination mais pas l'utilisateur. Le middle relay ne connaît ni l'un ni l'autre. Aucun relais isolé ne dispose de suffisamment d'information pour relier l'utilisateur à sa destination.

#### 5.2 Les types de nœuds

Les **guard nodes** (ou entry guards) sont le premier relais du circuit — la position la plus critique car ils voient l'IP réelle de l'utilisateur. Pour limiter le risque, le client Tor utilise un petit nombre de guards stables sur une longue période (plutôt que de changer à chaque connexion) — si le guard est de confiance, l'utilisateur est protégé pour toutes ses sessions. Les guards sont sélectionnés parmi les relais les plus stables, les plus anciens, et les plus performants.

Les **middle relays** sont les relais intermédiaires — les plus nombreux et les moins critiques. Ils voient uniquement le relais précédent et le relais suivant, sans pouvoir déchiffrer le contenu.

Les **exit nodes** sont le dernier relais du circuit — ils voient le trafic en clair si la destination n'utilise pas HTTPS (en 2026, la quasi-totalité du web utilise HTTPS, mais les protocoles non chiffrés comme DNS, FTP, ou HTTP simple restent vulnérables). Les exit nodes sont les plus risqués à opérer : le trafic qui en sort est associable au nœud (si un utilisateur Tor visite un site illicite, l'IP visible pour le site est celle de l'exit node — d'où les plaintes et les alertes que reçoivent les opérateurs d'exit nodes).

Les **bridge nodes** sont des relais non listés publiquement dans le consensus Tor, utilisés pour contourner la censure dans les pays qui bloquent Tor (Chine, Iran, Russie, Turkménistan). Les bridges sont distribués via des mécanismes résistants à l'énumération (email, site web, Moat intégré dans le Tor Browser). Les protocoles de transport enfichables (**pluggable transports** — obfs4, Snowflake, meek) déguisent le trafic Tor en trafic ordinaire (HTTPS, WebRTC) pour éviter la détection par les systèmes DPI (Deep Packet Inspection) des censeurs.

Les **directory authorities** sont les 9 serveurs de confiance qui maintiennent le consensus sur l'état du réseau Tor (quels relais existent, quelles sont leurs caractéristiques, quels sont les flags — Guard, Exit, Stable, Fast). Le consensus est mis à jour toutes les heures. La compromission d'une majorité de directory authorities compromettrait le fonctionnement du réseau.

#### 5.3 Ce que Tor protège et ce qu'il ne protège pas

**Tor protège** contre la surveillance du réseau local (l'administrateur du réseau WiFi ne voit que du trafic chiffré vers un guard node Tor, pas la destination finale), contre la surveillance par le site de destination (le site voit l'IP de l'exit node, pas celle de l'utilisateur), et contre l'analyse de trafic simple (un observateur intermédiaire ne peut pas relier l'entrée et la sortie du circuit par simple inspection des paquets).

**Tor ne protège PAS** contre un adversaire global qui surveille à la fois le guard et l'exit (corrélation de trafic par timing et volume — attaque théorique mais considérée comme réalisable par les agences de renseignement), contre les vulnérabilités du navigateur (un exploit 0-day dans Firefox peut révéler l'IP réelle — le FBI a utilisé cette technique), contre les erreurs utilisateur (se connecter à un compte personnel via Tor, télécharger un document qui fait une connexion directe hors Tor, activer JavaScript sur un site malveillant), et contre le trafic des applications non-Tor (seul le Tor Browser route son trafic via Tor — les autres applications de la machine se connectent directement, sauf configuration spécifique comme Whonix ou Tails).

#### 5.4 Métriques du réseau Tor

En 2025-2026, le réseau Tor compte environ 6 000 à 7 000 relais actifs, dont environ 1 000 exit nodes, pour une bande passante totale d'environ 500-700 Gbit/s. Le nombre d'utilisateurs directs estimé est d'environ 2 à 3 millions par jour (Tor Metrics). Les pays avec le plus d'utilisateurs sont les États-Unis, la Russie (malgré les restrictions), l'Allemagne, l'Inde, et l'Iran. La part d'utilisateurs qui accèdent à des hidden services (.onion) est estimée à environ 3-6 % du trafic total — la majorité des utilisateurs de Tor l'utilisent pour accéder au web classique de manière anonyme, pas pour visiter le dark web.

---

### Chapitre 6 — Onion services et services cachés

#### 6.1 Le principe des onion services

Un **onion service** (anciennement « hidden service ») est un serveur accessible exclusivement via le réseau Tor, identifié par une adresse `.onion`. La particularité est que le serveur est aussi anonyme que le client : ni le client ne connaît l'IP du serveur, ni le serveur ne connaît l'IP du client.

Le mécanisme fonctionne via un système de rendez-vous. Le serveur crée des **introduction points** (des relais Tor qui servent de point de contact initial) et publie leur adresse dans la DHT (Distributed Hash Table) du réseau Tor, associée à son adresse .onion. Le client qui connaît l'adresse .onion la recherche dans la DHT, obtient l'adresse des introduction points, puis propose un **rendezvous point** (un autre relais Tor choisi par le client) via l'introduction point. Le serveur accepte et les deux parties communiquent via le rendezvous point — chacun maintenant un circuit Tor de 3 relais entre lui et le rendezvous point, soit 6 relais au total.

#### 6.2 Adresses v2 et v3

Les adresses v2 (16 caractères, basées sur RSA-1024) sont obsolètes depuis octobre 2021 — le réseau Tor ne les supporte plus. Les adresses **v3** (56 caractères, basées sur ed25519) offrent un chiffrement plus robuste, une meilleure résistance aux attaques par énumération (il est computationnellement impossible de deviner une adresse v3), et une protection contre les attaques par compromission de la DHT. Une adresse v3 typique ressemble à `vww6ybal4bd7szmgncyruucpgfkqahzddi37ktceo3ah7ngmcopnpyyd.onion`.

Les **vanity addresses** (adresses personnalisées avec un préfixe lisible, comme `darkmarket...onion`) sont générées par force brute — l'opérateur génère des millions de clés jusqu'à trouver une adresse commençant par le préfixe souhaité. Plus le préfixe est long, plus le temps de génération est exponentiel. Les vanity addresses de 6-8 caractères sont courantes ; au-delà de 10, le coût en calcul devient prohibitif.

#### 6.3 Fragilités des onion services

Malgré l'anonymat théorique, les onion services ont des vulnérabilités pratiques. Les **fuites d'IP** par mauvaise configuration sont la cause la plus fréquente de compromission : un serveur web qui inclut son IP réelle dans un header HTTP, un certificat SSL qui contient le domaine ou l'IP du serveur, un service compagnon (base de données, serveur SSH) qui écoute sur l'IP publique au lieu de localhost, ou un script serveur qui fait des requêtes DNS hors Tor. L'outil **OnionScan** (Ch.22) détecte automatiquement ces fuites.

---

### Chapitre 7 — I2P, Freenet et réseaux alternatifs

#### 7.1 I2P (Invisible Internet Project)

I2P utilise le **garlic routing** — une variante de l'onion routing où les messages sont encapsulés en « gousses d'ail » contenant plusieurs messages chiffrés, ce qui rend la corrélation de trafic plus difficile. I2P est conçu principalement pour la communication interne au réseau (les **eepsites** sont l'équivalent des .onion), pas pour accéder au web classique. L'architecture est unidirectionnelle : les tunnels d'envoi et de réception sont séparés, chacun passant par des pairs différents. Les services I2P incluent la messagerie (I2P-Bote, SusiMail), les torrents (I2PSnark), et les forums (Syndie). La communauté est plus petite que Tor (quelques dizaines de milliers d'utilisateurs) mais considérée par certains acteurs comme « moins surveillée ».

#### 7.2 Freenet

Freenet est un réseau de stockage distribué et chiffré. Contrairement à Tor (qui route le trafic) ou I2P (qui route les messages), Freenet distribue le contenu de manière redondante sur les nœuds du réseau. Le contenu est stocké de manière fragmentée et chiffrée — aucun nœud ne sait quel contenu il héberge. Les deux modes : **opennet** (connexion à des nœuds inconnus — plus facile mais moins sûr) et **darknet** (connexion uniquement à des pairs de confiance — plus sûr, plus lent). Le contenu populaire persiste (il est répliqué sur de nombreux nœuds) ; le contenu peu demandé finit par être évincé. Les freesites sont des pages statiques (pas de contenu dynamique), ce qui limite les usages mais rend le réseau très résistant à la censure.

#### 7.3 Réseaux émergents

**Lokinet** (basé sur le protocole LLARP, utilise une blockchain pour le registre de nœuds) offre un routage anonyme avec une latence plus faible que Tor. **ZeroNet** utilise Bitcoin pour l'identité et BitTorrent pour la distribution — sites web pair-à-pair résistants à la censure. **Yggdrasil** est un réseau mesh chiffré de bout en bout, orienté IPv6. **IPFS** (InterPlanetary File System) n'est pas anonyme en soi mais est utilisé comme infrastructure de stockage décentralisée par certains services du dark web pour la résilience aux takedowns.

#### 7.4 Messageries anonymes et chiffrées

Leur rôle dans l'écosystème dark web est central — les transactions se négocient souvent hors des forums, via des canaux de communication directe. **Tox** (peer-to-peer, chiffré, utilisé comme canal de contact principal sur les forums russophones), **Session** (basée sur le réseau Lokinet, métadonnées minimales), **Briar** (décentralisée, fonctionne via Tor, WiFi direct, ou Bluetooth — conçue pour les environnements à connectivité limitée), **Ricochet Refresh** (chaque utilisateur est un hidden service Tor — pas de serveur central), et les canaux **IRC sur Tor** (le protocole historique des communications underground, encore utilisé sur certains réseaux comme OFTC via Tor).

#### 7.5 Comparaison technique

| Critère | Tor | I2P | Freenet |
|---------|-----|-----|---------|
| Modèle de routage | Onion routing (circuits) | Garlic routing (tunnels unidirectionnels) | Stockage distribué |
| Usage principal | Navigation web anonyme + hidden services | Communication interne (eepsites, messagerie) | Publication résistante à la censure |
| Accès au web classique | Oui (via exit nodes) | Limité (outproxies rares et lents) | Non |
| Taille du réseau | ~6 000-7 000 relais, 2-3M utilisateurs/jour | ~30 000 nœuds, quelques dizaines de milliers d'utilisateurs | ~5 000-10 000 nœuds |
| Latence | Moyenne (1-5 secondes) | Moyenne à élevée | Élevée (minutes) |
| Maturité | Haute (2002) | Moyenne (2003) | Haute (2000) |
| Contournement de censure | Oui (bridges, pluggable transports) | Limité | Limité |

---

### Chapitre 8 — Cryptomonnaies et anonymat financier

#### 8.1 Bitcoin : pseudo-anonyme, pas anonyme

La blockchain Bitcoin est un registre public : chaque transaction est visible par tous, avec l'adresse de l'émetteur, l'adresse du destinataire, et le montant. Le pseudo-anonymat vient du fait que les adresses ne sont pas liées à une identité nominative par défaut. Mais les techniques de **blockchain analysis** (heuristiques de clustering d'adresses, identification des services connus — exchanges, mixers, marchés —, et exploitation des points de conversion fiat↔crypto via les exchanges KYC) permettent de relier des adresses entre elles et, via les réquisitions judiciaires auprès des exchanges, de remonter à des identités. Bitcoin est le moyen de paiement historique du dark web, mais sa traçabilité croissante pousse les acteurs sophistiqués vers des alternatives. Renvoi au Ch.27 pour le détail du traçage.

#### 8.2 Monero (XMR) : la privacy coin dominante

Monero est la cryptomonnaie de référence pour l'anonymat financier sur le dark web. Trois mécanismes de confidentialité agissent simultanément : les **ring signatures** (chaque transaction est signée par un groupe d'adresses, rendant l'émetteur ambigu parmi le groupe), les **stealth addresses** (chaque transaction génère une adresse unique à usage unique pour le destinataire — les fonds reçus ne sont pas reliables entre eux), et **RingCT** (Ring Confidential Transactions — les montants sont masqués). Résultat : contrairement à Bitcoin, les transactions Monero ne sont pas traçables par les outils standard de blockchain analysis. Les recherches académiques ont montré des faiblesses dans les anciennes implémentations (avant 2017, les ring signatures étaient petites et les choix de decoys non aléatoires), mais en 2025-2026, Monero est considéré comme résistant au traçage pour les adversaires non étatiques.

#### 8.3 Services de mixing et d'obfuscation

Les **mixers/tumblers** Bitcoin mélangent les fonds de plusieurs utilisateurs pour brouiller la traçabilité. Les mixers centralisés (un service qui reçoit les fonds, les mélange, et les redistribue) ont été massivement saisis par les autorités ces dernières années (Chipmixer mars 2023, Sinbad novembre 2023, Tornado Cash sanctionné par l'OFAC en août 2022). Les protocoles décentralisés (**CoinJoin** — les utilisateurs construisent collaborativement une transaction multi-input/multi-output qui mélange leurs fonds ; **Wasabi Wallet** — implémentation de CoinJoin avec un coordinateur, dont le service a fermé en 2024 ; **JoinMarket** — CoinJoin décentralisé sans coordinateur, toujours actif) restent fonctionnels mais plus complexes d'utilisation.

Les **atomic swaps** (échange direct Bitcoin↔Monero sans intermédiaire, via des contrats cryptographiques) sont une technique émergente qui combine la liquidité de Bitcoin avec l'anonymat de Monero — l'utilisateur envoie du Bitcoin et reçoit du Monero (ou inversement) sans passer par un exchange centralisé.

#### 8.4 OPSEC financière sur le dark web

Les bonnes pratiques : ne jamais réutiliser un wallet entre activités (chaque opération a son propre wallet), utiliser Monero pour les transactions sensibles (si le forum l'accepte — la plupart des forums importants acceptent Monero), utiliser des wallets non custodial (pas d'exchange centralisé qui peut être réquisitionné), gérer les change addresses correctement sur Bitcoin (un change address qui relie deux transactions différentes compromet l'anonymat), et ne jamais convertir directement du crypto en fiat via un exchange KYC lié à son identité réelle. Les erreurs de gestion financière sont l'une des causes les plus fréquentes de dé-anonymisation (détaillé au Ch.26).

#### 8.5 Fil rouge — DARKSTREAM : le paiement d'accès

> **🌐 DARKSTREAM — Épisode 4**
>
> Pour accéder à IndustrialLeaks, Lucas doit payer 0,005 BTC (~180 € au cours actuel). Question juridique immédiate : un analyste privé peut-il payer pour accéder à un forum cybercriminel ? Lucas consulte le directeur juridique d'Athéna Group avant toute action (détaillé au Ch.20). La réponse encadrée : le paiement est autorisé dans le cadre du mandat client, avec documentation écrite, justification de la finalité d'investigation, et plafond financier convenu avec le client. Lucas utilise un wallet Bitcoin dédié à cette investigation, alimenté via un exchange avec des fonds de la société, documenté dans le journal de collecte.

---

### Chapitre 9 — Hébergement, infrastructure et résilience des services clandestins

#### 9.1 Hébergement bulletproof

Les services du dark web nécessitent un hébergement qui ne répond pas aux plaintes d'abus et aux requêtes judiciaires. L'hébergement bulletproof (renvoi au Ch.9 du cours Écosystèmes) existe sur le dark web avec une dimension supplémentaire : le serveur lui-même est un hidden service, ce qui signifie que même l'hébergeur ne connaît pas nécessairement l'IP réelle du client. Certains opérateurs auto-hébergent sur leur propre infrastructure physique, dans des juridictions choisies pour leur faible coopération judiciaire (certains États post-soviétiques, certains pays d'Asie du Sud-Est). D'autres utilisent des services cloud légitimes (AWS, OVH, Hetzner) en masquant l'usage réel par des couches de misdirection.

#### 9.2 Résilience et fragilité

Les techniques de résilience : le **mirroring** (plusieurs domaines .onion et eepsites I2P pointant vers le même service — si un est saisi, les autres restent actifs), le load balancing distribué, les **dead man's switches** (si l'opérateur est arrêté et ne se manifeste pas dans un délai donné, un message automatique avertit les utilisateurs), et les systèmes de backup automatisé (le contenu est répliqué vers un serveur de secours prêt à prendre le relais).

Malgré ces mécanismes, tout service dark web a des **points de défaillance** : l'opérateur humain (identifiable par erreur OPSEC, social engineering, ou infiltration), l'infrastructure physique (les serveurs sont quelque part et peuvent être saisis), la clé privée du hidden service (single point of failure cryptographique), et les dépendances (un marché qui repose sur un seul service d'escrow est vulnérable à la compromission de ce service).

Le **DDoS** est un fléau endémique sur le dark web. Les marchés et forums sont régulièrement victimes d'attaques DDoS lancées par des concurrents, des extorqueurs, ou des forces de l'ordre. Les solutions de protection (proof-of-work captchas, onion balancing) sont partiellement efficaces. L'instabilité chronique des services dark web (pages qui ne chargent pas, erreurs de connexion, temps de réponse de plusieurs minutes) est en partie due aux DDoS et en partie à l'architecture même de Tor (6 relais entre le client et le serveur = latence élevée).

#### 9.3 Fil rouge — DARKSTREAM : l'infrastructure d'IndustrialLeaks

> **🌐 DARKSTREAM — Épisode 5**
>
> Lucas documente l'infrastructure d'IndustrialLeaks dans sa fiche de plateforme. Le forum a changé 3 fois d'adresse .onion en 18 mois (migrations probablement liées à des DDoS). Il dispose d'un miroir I2P. L'accès est protégé par un captcha proof-of-work (l'utilisateur doit résoudre un calcul qui prend ~5 secondes — protection anti-bot et anti-DDoS basique). Le forum utilise un moteur personnalisé (pas un CMS standard comme FluxBB ou phpBB — signe d'un opérateur avec des compétences de développement). Le temps de réponse moyen est de 3-8 secondes (typique pour un hidden service Tor). Le forum est actif depuis 4 ans — une longévité remarquable qui suggère un opérateur expérimenté et prudent.

---

## PARTIE III — ÉCOSYSTÈMES DU DARK WEB : ESPACES, ACTEURS ET CULTURE

*Cartographie détaillée de ce qui se trouve réellement sur le dark web : les forums et leurs hiérarchies sociales, les marchés et leurs mécanismes, les leak sites, les canaux de communication, les données en circulation, et les profils d'acteurs.*

---

### Chapitre 10 — Forums clandestins : culture, hiérarchie et codes

#### 10.1 La sociologie des forums underground

Les forums du dark web ne sont pas de simples places de marché — ce sont des communautés structurées avec leur propre culture, leurs propres codes sociaux, et leur propre système de gouvernance informelle. Comprendre cette sociologie est indispensable pour l'analyste qui veut naviguer dans ces espaces sans se faire repérer et interpréter correctement ce qu'il observe.

La **hiérarchie** est informelle mais rigide. Les administrateurs ont un pouvoir quasi absolu sur le forum (bannissement, suppression, modification des règles). Les modérateurs forment la classe intermédiaire (application des règles, arbitrage des litiges, vérification des vendeurs). Les vendeurs vérifiés (« verified vendors ») sont l'aristocratie marchande — ils ont prouvé leur légitimité par des transactions réussies et des dépôts de garantie. Les membres ordinaires participent aux discussions et aux achats. Les lurkers (observateurs silencieux) sont tolérés sur les forums ouverts mais suspects sur les forums fermés (un compte qui ne poste jamais et ne participe pas est un indicateur d'infiltration).

#### 10.2 Forums russophones vs anglophones

Deux écosystèmes distincts coexistent avec peu d'interaction directe. Les **forums russophones** majeurs (XSS, Exploit, RAMP) sont généralement plus fermés (accès par vouching ou paiement élevé — 500 à 5 000 $ pour un compte sur Exploit), plus sophistiqués techniquement (les vendeurs sont plus compétents, les discussions techniques sont plus approfondies), et plus disciplinés (les règles sont strictement appliquées — interdiction de cibler les pays de la CEI, interdiction des scams entre membres). Les **forums anglophones** (BreachForums et ses successeurs, Cracked, Nulled, RaidForums avant sa saisie) sont généralement plus ouverts, plus accessibles, mais avec un niveau de qualité plus variable, plus de bruit, et plus de scams. La barrière de la langue crée deux « mondes » qui interagissent ponctuellement (les breaches et les outils circulent entre les deux) mais restent largement séparés.

#### 10.3 Les codes sociaux

Les « règles » non écrites des forums underground : ne pas cibler les pays de la CEI (règle quasi universelle sur les forums russophones — enfreindre cette règle conduit au bannissement et à l'exposition publique), ne pas arnaquer les membres du forum (la confiance intra-communautaire est sacrée — un vendeur qui arnaque un membre est blacklisté sur tous les forums associés), ne pas coopérer avec les forces de l'ordre (le « snitching » est le péché capital — un membre soupçonné de coopération est exposé publiquement, menacé, et banni), et ne pas discuter de CSAM (la plupart des forums cybercriminels l'interdisent explicitement — ce n'est pas par moralité mais par pragmatisme : le CSAM attire une attention disproportionnée des forces de l'ordre).

---

### Chapitre 11 — Marchés du dark web : histoire, fonctionnement et évolution

#### 11.1 De Silk Road à l'ère post-Hydra

L'histoire des darknet markets est une succession de cycles création → croissance → saisie/exit scam → migration. Silk Road (2011-2013) a posé le modèle. AlphaBay (2014-2017) l'a industrialisé. Hydra (2015-2022) l'a dominé. Chaque saisie concentre l'attention des médias et des autorités, mais l'écosystème se reconstruit systématiquement — les utilisateurs migrent, les opérateurs lancent de nouveaux marchés, et le cycle recommence. La résilience de l'écosystème tient à la demande (les acheteurs et les vendeurs existent indépendamment des plateformes) et à la faible barrière technique (lancer un marché est techniquement accessible).

#### 11.2 Fonctionnement d'un darknet market

Le modèle économique est celui d'une marketplace : commission de 2-5 % sur chaque transaction, frais de listing pour les vendeurs, et frais d'inscription pour les acheteurs (sur certains marchés). Le **système d'escrow** est la pierre angulaire de la confiance : le marché retient les fonds de l'acheteur jusqu'à la confirmation de réception du produit. Si l'acheteur ne confirme pas, le vendeur peut contester et l'arbitre (un modérateur du marché) tranche. Le **système de réputation** (ratings, reviews, volume de transactions, ancienneté) est le capital le plus précieux : un vendeur avec un historique de 500+ transactions réussies et un rating de 4.9/5 peut charger des prix premium.

#### 11.3 Ce qui se vend — cartographie factuelle

Les **stupéfiants** restent la catégorie dominante en volume sur les marchés généralistes (cannabis, cocaïne, MDMA, amphétamines, opioïdes, psychédéliques). Les **données volées** constituent la catégorie la plus pertinente pour les analystes CTI (credentials, cartes bancaires, données personnelles, bases d'entreprises — détaillées au Ch.14). Les **services cybercriminels** (malware, RaaS, DDoS, hacking — détaillés au Ch.15). Les **documents contrefaits** (faux passeports, faux permis, faux diplômes — qualité variable, souvent des scams). Les **armes** (un marché beaucoup plus petit que ce que les médias suggèrent, avec un taux de scam très élevé et une surveillance policière intense). Les **médicaments** (y compris contrefaits et substances contrôlées).

#### 11.4 L'évolution 2024-2026

La fragmentation post-Hydra (pas de successeur unique dans l'écosystème russophone), la spécialisation croissante (marchés de données spécialisés plutôt que marchés généralistes), la montée de Telegram comme canal de vente parallèle (Ch.13), et la pression réglementaire croissante sur les exchanges crypto (qui complique le cash-out). Les marchés qui survivent le plus longtemps sont ceux qui investissent dans la sécurité (infrastructure distribuée, OPSEC de l'opérateur, résistance au DDoS) et dans la modération (suppression des scams, arbitrage rapide des litiges, maintien de la confiance).

---

### Chapitre 12 — Leak sites, blogs d'extorsion et vitrines de revendication

#### 12.1 Les leak sites de ransomware

Les leak sites sont des sites .onion opérés par les groupes de ransomware pour publier les données des victimes qui refusent de payer la rançon. Leur fonction est triple : **pression** sur la victime (« payez ou vos données sont publiées »), **marketing** criminel (démontrer aux futures victimes que le groupe est sérieux et met ses menaces à exécution), et **preuve de compromission** (les échantillons publiés prouvent que le groupe a effectivement accédé aux données).

#### 12.2 Structure et fonctionnement

Chaque victime a sa propre page sur le leak site, avec le nom de l'organisation, une description de l'attaque (souvent exagérée), un échantillon de données (quelques fichiers pour prouver l'authenticité), un compte à rebours (typiquement 7 à 14 jours avant la publication complète), et un lien vers le portail de négociation (un chat .onion dédié). Après expiration du compte à rebours, les données sont publiées intégralement — souvent sous forme d'archives téléchargeables sur des serveurs dédiés.

#### 12.3 Narration et communication criminelle

Les groupes de ransomware ont développé des stratégies de communication sophistiquées. Certains publient des « communiqués de presse » sur leur leak site, justifiant leurs attaques (« nous ciblons les entreprises qui ne protègent pas les données de leurs clients »). D'autres contactent directement les journalistes spécialisés pour amplifier la couverture médiatique. LockBit avait même un « programme de bug bounty » (récompense pour quiconque trouverait des vulnérabilités dans leur infrastructure). Cette communication sert un objectif commercial : plus la menace est crédible, plus les futures victimes sont incitées à payer.

#### 12.4 Le monitoring des leak sites pour le CTI

La surveillance des leak sites est une composante essentielle de la veille CTI. Les données publiées révèlent les cibles (quels secteurs, quels pays, quelle taille d'entreprise), les volumes (combien de victimes par mois, par groupe), les patterns (certains groupes ciblent préférentiellement certains secteurs), et les TTP (les descriptions des attaques révèlent parfois les vecteurs et les techniques utilisés). Les outils de monitoring (Ransomwatch, Ransomfeed, et les plateformes commerciales) agrègent les publications de dizaines de leak sites.

---

### Chapitre 13 — Canaux, chats et messageries clandestines

#### 13.1 Telegram comme extension du dark web

Telegram est devenu, depuis 2020-2021, le principal concurrent du dark web pour le commerce cybercriminel. Les avantages : accessibilité (pas besoin de Tor — une simple application mobile suffit), rapidité (création de canal en 30 secondes vs des jours pour un forum .onion), audience (des centaines de millions d'utilisateurs potentiels vs quelques milliers sur un forum .onion), et fonctionnalités (bots d'automatisation, channels de diffusion, groupes de discussion). Les inconvénients : dépendance envers Telegram (qui peut fermer les canaux — et l'a fait plus agressivement après l'arrestation de Pavel Durov en août 2024), moins d'anonymat que Tor (Telegram nécessite un numéro de téléphone, les métadonnées sont accessibles à Telegram, et les réquisitions judiciaires sont possibles), et moins de mécanismes de confiance (pas d'escrow intégré, pas de système de réputation formalisé).

#### 13.2 Les autres canaux de communication

**Jabber/XMPP** (avec chiffrement OTR ou OMEMO) : le protocole de messagerie instantanée le plus utilisé par les acteurs sophistiqués du dark web. Les serveurs XMPP opérés en .onion offrent un bon niveau d'anonymat. **Tox** : messagerie peer-to-peer chiffrée, utilisée comme canal de contact principal sur de nombreux forums russophones (chaque vendeur publie son Tox ID). **Matrix** (avec serveurs hébergés sur Tor) : protocole décentralisé de messagerie, utilisé par certaines communautés techniques. **IRC sur Tor** : le protocole historique, en déclin mais encore utilisé par certaines communautés.

#### 13.3 La fragmentation des communications

La tendance 2024-2026 est à la fragmentation : les acteurs utilisent simultanément plusieurs canaux (un forum .onion pour l'annonce publique, Telegram pour la promotion rapide, Tox ou Jabber pour la négociation privée, et un marché .onion pour la transaction). L'analyste qui ne surveille qu'un seul canal rate la majorité de l'activité. La corrélation entre canaux (relier un pseudo de forum à un Tox ID puis à un canal Telegram) est une technique d'investigation fondamentale (Ch.23).

---

### Chapitre 14 — Données volées et marchés de la fuite

#### 14.1 Types de données en circulation

Les **credentials** (couples email/mot de passe issus de breaches) sont vendus en bulk (combo lists de millions d'entrées pour quelques dollars) ou au détail (credentials vérifiés pour des services spécifiques à 5-50 $ pièce). Les **logs d'infostealers** (sessions complètes : credentials navigateur + cookies de session + données de formulaires + wallets crypto + données machine) sont vendus sur des marchés spécialisés (Russian Market, le successeur de Genesis Market) — un log riche avec des credentials VPN d'entreprise peut atteindre 50-500 $. Les **données bancaires** (numéros de carte, CVV, accès aux comptes — vendus sur des marchés spécialisés appelés « card shops »). Les **données personnelles** (identités complètes pour l'usurpation — « fullz » : nom, adresse, SSN/NIR, date de naissance, documents d'identité). Les **données d'entreprise** (documents internes, propriété intellectuelle, emails, bases clients — c'est le cas DARKSTREAM). Et les **données de santé** (dossiers médicaux — très prisés aux US pour la fraude à l'assurance).

#### 14.2 Le lifecycle d'un breach

Comment une fuite passe du vol initial à la publication gratuite. Phase 1 : exploitation privée par le groupe auteur (fraude, extorsion). Phase 2 : vente exclusive à prix élevé à un ou quelques acheteurs (first-sale market — les données fraîches ont le plus de valeur). Phase 3 : revente à prix décroissant par les acheteurs initiaux. Phase 4 : publication gratuite ou à prix très bas sur les forums (combo lists, collections). Phase 5 : intégration dans les bases de breach check (Have I Been Pwned, DeHashed). Le temps entre la phase 1 et la phase 5 peut être de quelques jours à plusieurs années. Pour l'analyste, la phase est un indicateur de la valeur résiduelle des données : des données en phase 5 sont publiques et sans valeur marchande ; des données en phase 2 sont récentes et potentiellement exploitées activement.

#### 14.3 Vérification de l'authenticité

Quand un vendeur prétend avoir des données volées, comment évaluer l'authenticité ? Les échantillons gratuits (sont-ils vérifiables ? les emails existent-ils ? les domaines correspondent-ils à l'organisation revendiquée ?), la fraîcheur (des données déjà vues dans des breaches précédentes sont du recyclage), la spécificité (des données très spécifiques à une organisation sont plus crédibles que des données génériques), la corroboration (le breach a-t-il été confirmé par l'organisation victime ou par un CERT ?), et la cohérence interne (les formats de données, les conventions de nommage, les dates sont-ils cohérents avec ce que l'on sait de l'organisation ?). Les scams (fausses fuites pour extorquer de l'argent) sont fréquents — un vendeur qui refuse de fournir des échantillons vérifiables est suspect.

---

### Chapitre 15 — Services criminels : du crime-as-a-service aux profils d'acteurs

#### 15.1 Taxonomie des services

Cartographie complète des services criminels disponibles sur le dark web. **Malware-as-a-Service** (MaaS) : infostealers (Lumma, RedLine, Vidar — abonnements de 250 à 1 000 $/mois), RAT (Remcos, AsyncRAT — 50-500 $), loaders (chargeurs qui téléchargent et exécutent d'autres malwares — 500-5 000 $ selon la sophistication). **Ransomware-as-a-Service** (RaaS) : le modèle franchisé dominant (LockBit, BlackBasta, Play — l'affilié déploie le ransomware et partage 70-80 % des revenus avec l'opérateur). **Phishing-as-a-Service** (PhaaS) : kits de phishing avec panels d'administration, pages de phishing pré-faites, interception MFA (kits AitM — Adversary-in-the-Middle). **DDoS-for-hire** (booters/stressers — 10-500 $/mois selon la puissance). **Services de carding** (vérification de validité des cartes, cash-out via mules). **Services de blanchiment** (mixing, OTC, mules — commission de 10-30 %). **Documents contrefaits**.

#### 15.2 Les profils d'acteurs

Les **IAB** (Initial Access Brokers) vendent des accès réseau compromis (VPN, RDP, Citrix) — prix de 500 à 50 000 $ selon la cible (taille, secteur, revenus). Les **vendeurs de bases de données** commercialisent les données issues de breaches. Les **développeurs de malware** créent et maintiennent les outils (souvent des développeurs compétents qui pourraient travailler dans le légal mais choisissent le crime pour les revenus). Les **opérateurs de ransomware** coordonnent les attaques. Les **fraudeurs et carders** exploitent les données financières volées. Les **scammers** arnaquent les autres criminels — une couche parasitaire de l'écosystème. Et les **acteurs idéologiques** (hacktivistes, extrémistes) qui utilisent le dark web pour des motivations non financières.

#### 15.3 Fil rouge — DARKSTREAM : le profil du vendeur

> **🌐 DARKSTREAM — Épisode 6**
>
> Lucas analyse le profil de « aero_source » sur IndustrialLeaks. Compte créé il y a 2 ans. 15 transactions confirmées (toutes des ventes de données industrielles — aérospatiale, défense, énergie). Rating 4.7/5. Style d'écriture : anglais correct avec des calques syntaxiques qui suggèrent un locuteur slave (« I have good base for sell » au lieu de « for sale »). Les montants des ventes précédentes varient de 5 à 80 BTC — ce n'est pas un petit joueur.
>
> Lucas compare avec les profils d'autres vendeurs du même forum : « aero_source » est un vendeur spécialisé dans les données industrielles, probablement un courtier (broker) qui achète des données à des groupes d'intrusion et les revend avec une marge. Il n'est probablement pas l'auteur de l'intrusion chez Vectris — il en est le revendeur.

---

## PARTIE IV — ÉCONOMIE CLANDESTINE ET MÉCANISMES DE CONFIANCE

*Comment le commerce fonctionne dans un environnement où personne ne se fait confiance, où il n'y a pas de justice formelle, et où l'arnaque est endémique.*

---

### Chapitre 16 — Pourquoi l'économie du dark web fonctionne

Malgré l'absence de cadre légal, de recours judiciaire, et de confiance a priori, l'économie du dark web fonctionne — imparfaitement, mais elle fonctionne. Les mécanismes qui la rendent possible : la **spécialisation** (chaque acteur fait ce qu'il sait faire — l'IAB vend l'accès, l'opérateur RaaS déploie le ransomware, le blanchisseur convertit les crypto), la **modularité** (les services sont interconnectés comme des briques Lego — un acteur peu compétent peut monter une attaque sophistiquée en assemblant des services achetés), les **barrières d'entrée basses** (grâce au modèle as-a-Service, il n'est pas nécessaire de coder un ransomware pour en déployer un), et les **mécanismes de confiance substitutifs** (réputation, escrow, vouching — détaillés au Ch.17).

### Chapitre 17 — Réputation, escrow, vouching et arbitrage

La confiance est la monnaie la plus précieuse du dark web — et la plus fragile. La **réputation** se construit par l'historique de transactions (nombre, volume, ancienneté), les ratings et reviews des contreparties, et la validation par des membres de confiance. Un profil avec 200+ transactions réussies et 3 ans d'ancienneté est un capital qui vaut des dizaines de milliers de dollars — c'est pourquoi les comptes de forum sont achetés et vendus (5 000-20 000 $ pour un compte ancien avec bonne réputation sur Exploit ou XSS).

L'**escrow** est le mécanisme central de confiance pour les transactions : le marché ou le forum retient les fonds de l'acheteur jusqu'à confirmation de réception. Le **vouching** est le système de parrainage : un nouveau membre est présenté par un membre établi qui engage sa propre réputation. L'**arbitrage** est le mécanisme de résolution des litiges : un modérateur ou administrateur examine les preuves des deux parties et tranche — avec un pouvoir discrétionnaire considérable.

### Chapitre 18 — Arnaques, exit scams et manipulation de la confiance

L'envers de la confiance : les mécanismes d'arnaque qui exploitent les systèmes de confiance du dark web. Les **exit scams** sont le risque le plus dévastateur : l'opérateur d'un marché accumule les fonds d'escrow puis disparaît avec la totalité — des millions de dollars. Les exemples sont nombreux (Evolution Market, 2015 — exit scam estimé à 12 M$). Les **faux vendeurs** créent des profils crédibles (en achetant des comptes anciens ou en simulant des transactions avec des complices) puis escroquent les acheteurs. Les **escrows fictifs** sont des services d'escrow contrôlés par le vendeur lui-même (l'acheteur croit que ses fonds sont sécurisés, mais le vendeur contrôle les deux côtés). La **simulation de légitimité** (faux reviews, faux vouching, faux historique) est endémique.

Pour l'analyste CTI, ces arnaques sont un piège analytique majeur (Ch.28) : un « vendeur de données Vectris » peut être un scammer qui a repéré le buzz autour de la compromission et tente de capitaliser sur la peur de l'entreprise.

### Chapitre 19 — Modèles économiques criminels observés via le dark web

Ce chapitre synthétise les modèles économiques criminels visibles via le dark web (complément du cours Écosystèmes). Le **RaaS** (opérateur + affiliés + IAB + blanchisseur — chaîne de valeur complète), le **pipeline infostealer** (infostealer → log market → exploitation — détaillé au Ch.14), le **Initial Access Brokerage** (compromission → vente d'accès → exploitation par l'acheteur), la **fraude documentaire** (production → vente → utilisation), et les **services d'obfuscation** (crypters, hosting, mixing — services transversaux utilisés par tous les autres modèles). Pour chaque modèle : les acteurs impliqués, les flux financiers, les points de visibilité sur le dark web, et les indicateurs exploitables pour le CTI.

---

## PARTIE V — INVESTIGATION, VEILLE ET COLLECTE

*Comment un professionnel navigue, collecte, et documente sur le dark web — en respectant le cadre légal, l'éthique, la sécurité opérationnelle, et les limites méthodologiques.*

---

### Chapitre 20 — Cadre juridique, éthique et sécurité de l'analyste

#### 20.1 Ce que l'analyste privé a le droit de faire

La consultation passive (naviguer, lire, observer sans interagir) est légale en France et dans la plupart des juridictions occidentales. Le caractère « dark » d'un site ne change pas le statut juridique de l'observation passive — accéder à un site .onion n'est pas en soi une infraction. La collecte de données publiquement accessibles sur les forums (même sur le dark web) est légale dans le cadre d'une mission d'investigation légitime. L'analyse de données fuitées pour des fins de sécurité (vérifier si les credentials de son client sont compromises) est généralement tolérée — mais la conservation et le traitement sont encadrés par le RGPD (finalité légitime, durée limitée, proportionnalité). Le signalement aux autorités est une obligation en cas de découverte de certains contenus (CSAM, terrorisme — voir 20.4).

#### 20.2 Ce que l'analyste privé n'a PAS le droit de faire

L'interaction active avec des acteurs criminels (même sous persona — la provocation est réservée aux forces de l'ordre sous contrôle judiciaire). L'achat de services ou de données criminels (acheter des credentials volées « pour vérifier » est une infraction — recel de bien obtenu par un délit). L'intrusion dans les systèmes d'un service dark web (même pour identifier l'opérateur — c'est un accès frauduleux, article 323-1 du Code pénal). Le téléchargement de contenus illicites (CSAM — tolérance zéro, article 227-23 CP, obligation de signalement immédiat).

#### 20.3 Les zones grises

Le paiement d'un droit d'accès à un forum (nécessaire pour l'investigation mais constituant potentiellement un financement d'activité criminelle). L'utilisation de personas (la création d'une fausse identité en soi n'est pas illégale, mais les interactions qui en découlent peuvent l'être). La conservation de données fuitées (légale pour la détection de menaces mais encadrée par le RGPD — durée de conservation limitée, finalité légitime, information du DPO). Chaque zone grise nécessite un cadrage juridique préalable au cas par cas, documenté par écrit, avec l'aval du directeur juridique du cabinet et du client.

#### 20.4 Les obligations impératives

Signalement des contenus CSAM (article 434-3 CP — délit de non-dénonciation de mauvais traitements sur mineur). Signalement d'activité terroriste (article 421-2-5 CP). Le signalement se fait via la plateforme **PHAROS** (Plateforme d'Harmonisation, d'Analyse, de Recoupement et d'Orientation des Signalements — opérée par l'OCLCTIC) ou directement auprès des services compétents. Le signalement est obligatoire et immédiat — l'analyste interrompt son investigation pour signaler, puis documente le signalement dans son journal de collecte.

#### 20.5 Cadre pour les forces de l'ordre

Les enquêteurs sous mandat judiciaire disposent de pouvoirs étendus : achats sous couverture (autorisés sous contrôle du procureur pour les infractions de criminalité organisée — article 706-81 CPP), infiltration en ligne (cadre des « cyber-patrouilles » — agents habilités pouvant se présenter sous une fausse identité sur Internet), réquisitions auprès des fournisseurs de services, et coopération internationale (Europol EC3, Interpol, MLAT). Ces pouvoirs ne s'appliquent PAS aux investigateurs privés — la frontière est nette et son franchissement expose à des poursuites pénales.

#### 20.6 Fil rouge — DARKSTREAM : le cadrage

> **🌐 DARKSTREAM — Épisode 7**
>
> Avant toute action sur IndustrialLeaks, Lucas fait valider le cadre juridique avec le directeur juridique d'Athéna Group. Le cadrage écrit précise : consultation passive autorisée, collecte de captures d'écran autorisée, paiement d'accès au forum autorisé (cadre du mandat client, montant plafonné à 500 €, documenté), pas de téléchargement des documents techniques de Vectris (risque de recel de secret d'entreprise), pas d'interaction directe avec « aero_source », signalement DGSI recommandé si les données sont confirmées liées à des programmes de défense. Le client Vectris est informé et consent par écrit.

---

### Chapitre 21 — OPSEC opérationnelle pour l'investigation dark web

#### 21.1 Modèle de menace de l'investigateur

L'investigateur doit se protéger contre les acteurs criminels (qui peuvent tenter de l'identifier), les opérateurs de plateformes (qui surveillent les comportements suspects — un nouveau compte qui ne fait que lire et capturer est un indicateur d'infiltration), les forces de l'ordre (qui peuvent le confondre avec un acteur malveillant s'il opère sans cadrage juridique), et les fuites accidentelles (qui peuvent compromettre son identité professionnelle ou son organisation).

#### 21.2 Configuration de l'environnement

Le **poste dédié** : jamais le poste professionnel habituel. Un laptop dédié, sans données professionnelles, sans connexion aux comptes personnels ou professionnels. **Whonix** est la solution recommandée pour l'investigation dark web : une VM Gateway (qui route tout le trafic via Tor) couplée à une VM Workstation (dont tout le trafic passe obligatoirement par la Gateway — même si une application tente de se connecter directement, la VM ne peut pas atteindre Internet sans passer par Tor). **Tails** (The Amnesic Incognito Live System) est l'alternative pour les déplacements : un système d'exploitation bootable depuis une clé USB qui ne laisse aucune trace sur la machine hôte et route tout le trafic via Tor. À l'extinction, toute la mémoire est effacée.

La **séparation réseau** : ne jamais se connecter au réseau de l'entreprise avec le poste d'investigation. Utiliser un réseau WiFi public (café, bibliothèque — changer régulièrement), une connexion 4G/5G avec une SIM prépayée (achetée en espèces, sans lien avec l'identité réelle), ou un VPN commercial (en amont de Tor — le débat VPN+Tor est traité au 21.3).

#### 21.3 VPN + Tor : le débat

Trois configurations possibles. **Tor seul** : simple, efficace, recommandé par le Tor Project. L'ISP voit une connexion Tor mais pas la destination. **VPN → Tor** (le trafic entre dans le VPN, puis dans Tor) : l'ISP voit une connexion VPN (pas Tor — utile si l'utilisation de Tor est surveillée ou suspecte), mais le fournisseur VPN voit que l'utilisateur se connecte à Tor. **Tor → VPN** (le trafic entre dans Tor, puis dans le VPN) : l'exit node voit une connexion VPN (pas la destination finale), mais le fournisseur VPN voit le trafic en clair. Recommandation pour l'investigateur : VPN → Tor est le compromis le plus courant (masque l'utilisation de Tor au réseau local), avec un VPN commercial fiable (pas de logs, paiement en crypto, juridiction non coopérative).

#### 21.4 Gestion des personas (sock puppets)

La création et la maintenance de personas crédibles sont essentielles pour l'accès aux forums fermés. Les composantes d'une persona : un pseudonyme cohérent avec la culture du forum ciblé (un pseudo anglophone sur un forum russophone est immédiatement suspect), un email jetable (ProtonMail ou Tutanota créé via Tor — sans numéro de téléphone), un wallet crypto dédié (un wallet par persona, alimenté via des sources non traçables), un Tox ID dédié, et un backstopping minimal (des comptes créés sur d'autres plateformes pour simuler un historique — pas trop élaboré, juste suffisant pour ne pas paraître « frais »).

La **discipline de séparation** est critique : ne JAMAIS utiliser la même persona pour deux investigations différentes (risque de corrélation), ne JAMAIS croiser persona et identité réelle (pas de connexion au même réseau, pas d'utilisation du même navigateur, pas de publication aux mêmes horaires), et ne JAMAIS réutiliser un mot de passe ou un pattern de mot de passe entre persona et identité réelle.

---

### Chapitre 22 — Naviguer et collecter : méthodes, outils et limites

#### 22.1 Trouver des services

Les moteurs de recherche dark web (Ahmia — le seul qui filtre le contenu illicite, DarkSearch, Torch, Haystak) offrent une couverture partielle et des résultats souvent obsolètes. Les « hidden wikis » et listes de liens sont généralement périmés et truffés de scams. Les sources les plus fiables sont les forums eux-mêmes (les communautés maintiennent des listes à jour des services actifs), les canaux Telegram spécialisés, et les rapports CTI des éditeurs (qui mentionnent les plateformes actives). Le bouche-à-oreille (recommandation par un membre de confiance) reste le canal principal d'accès aux services fermés.

#### 22.2 Limites de la visibilité

L'analyste qui navigue sur le dark web ne voit qu'une fraction de ce qui s'y passe. Les forums les plus fermés (accès par vouching uniquement, sans possibilité de paiement) restent invisibles aux non-membres. Les transactions les plus sensibles se font en privé (messages directs, canaux chiffrés). Les outils de monitoring automatisé ne couvrent pas les sources les plus fermées. Les données publiées ne sont pas nécessairement représentatives (biais de sélection — ce qui est visible est ce que les acteurs ont choisi de rendre visible). Et les liens morts sont omniprésents (un .onion qui fonctionnait hier peut être hors ligne aujourd'hui, sans explication).

L'analyste doit intégrer ces limites dans ses conclusions : « l'absence de données Vectris sur les forums observés ne signifie pas l'absence de circulation — elle signifie l'absence de visibilité dans le périmètre de cette investigation ».

#### 22.3 Techniques de collecte et de préservation

La **capture d'écran horodatée** est la méthode de base : capture de la page avec les métadonnées de connexion (date/heure UTC, adresse .onion, chemin, persona utilisée). L'outil **Hunchly** (extension navigateur) capture et horodate automatiquement chaque page visitée, avec hash d'intégrité — c'est la référence pour la documentation d'investigation dark web. La sauvegarde de pages (wget via torsocks, HTTrack via Tor pour les sites entiers) permet l'archivage offline. Le hashing de chaque capture (SHA-256) garantit l'intégrité.

#### 22.4 Crawling et scraping automatisé

**OnionScan** scanne les hidden services pour détecter les erreurs de configuration (IP leaks, directory listing, informations dans les headers). **TorBot** et **ACHE** sont des crawlers automatisés de sites .onion. Les scripts Python custom (requests via PySocks ou stem pour router le trafic via Tor) permettent le scraping ciblé. Les limites : captchas, authentification, anti-bot, risque de bannissement, et considérations éthiques (le crawling massif consomme de la bande passante Tor et peut dégrader le service pour les autres utilisateurs).

---

### Chapitre 23 — Pivoting, enrichissement et corrélation OSINT

#### 23.1 Le workflow de pivot

Le pivot est la technique fondamentale de l'investigation dark web : à partir d'un identifiant trouvé dans un espace, l'analyste enrichit et relie vers d'autres espaces. Un pseudo de forum → recherche dans les bases de breaches (DeHashed, IntelX) → révèle un email → recherche de l'email sur le clear web (Google, Bing, réseaux sociaux) → révèle un profil → enrichissement. Un wallet Bitcoin → recherche sur les explorateurs blockchain → corrélation avec des transactions sur des exchanges ou des marchés. Un Tox ID publié sur un forum → recherche du même Tox ID sur d'autres forums et sur Telegram. Une clé PGP publiée → recherche de la même clé sur les serveurs de clés publiques et sur le clear web. Chaque pont entre le dark web et le surface web est une faille OPSEC exploitable.

#### 23.2 Outils d'enrichissement

**Sherlock** / **WhatsMyName** : recherche de pseudo sur des centaines de plateformes. **DeHashed** / **IntelX** / **Snusbase** : recherche dans les bases de breaches par email, pseudo, mot de passe, ou domaine. **OXT.me** / **Chainalysis** : exploration et analyse de la blockchain Bitcoin. **Maltego** (avec transforms dark web) : graphe de relations entre entités. **SpiderFoot** : framework OSINT modulaire avec modules dark web.

#### 23.3 Corrélation dark web ↔ surface web

C'est la technique d'investigation la plus productive. Les erreurs OPSEC des acteurs du dark web créent des ponts exploitables : un pseudo réutilisé entre le dark web et un forum technique du clear web, un email apparaissant dans un enregistrement WHOIS et dans un message de forum .onion, un style d'écriture identifiable entre un blog personnel et des posts de forum, et des métadonnées dans des documents publiés (nom d'auteur, dates, logiciel utilisé) qui révèlent des informations sur la source.

#### 23.4 Fil rouge — DARKSTREAM : le pivoting

> **🌐 DARKSTREAM — Épisode 8**
>
> Lucas pivote à partir des identifiants de « aero_source ». Le pseudo est recherché sur Sherlock — pas de correspondance directe sur le clear web. Le Tox ID publié sur IndustrialLeaks est recherché sur les forums archivés — le même Tox ID apparaît sur un post de 2023 sur un forum anglophone (RaidForums archive) sous le pseudo « aero_sell ». Le wallet Bitcoin associé aux transactions de « aero_source » (visible dans le système de réputation du forum) est analysé sur OXT.me — il montre des transactions avec un cluster d'adresses associé à un exchange KYC. Lucas note cette piste : si les autorités sont saisies, une réquisition auprès de l'exchange pourrait identifier le titulaire du wallet.

---

### Chapitre 24 — Veille dark web : surveillance, alerting et réduction du bruit

#### 24.1 Que surveiller

Pour une organisation : les mentions de son nom, de ses domaines, des emails de ses employés, des noms de ses projets et produits, des noms de ses dirigeants, et des identifiants techniques (IP ranges, ASN). Sur les leak sites (revendications de ransomware), sur les forums (ventes de données, ventes d'accès), sur les marchés de logs (credentials d'employés dans les logs d'infostealers), sur Telegram (canaux de revente, canaux de revendication), et dans les breaches publiques (Have I Been Pwned, DeHashed).

#### 24.2 Plateformes de monitoring

Les solutions commerciales (Flare, Recorded Future, Digital Shadows/ReliaQuest, Cybersixgill, Searchlight Cyber, ZeroFox) crawlent automatiquement les forums et marchés du dark web, indexent les données, et alertent quand des mots-clés correspondent. Leurs avantages : couverture large, alertes automatisées, intégration API avec le SIEM/SOAR. Leurs limites : couverture incomplète (les forums fermés ne sont pas indexés), latence (les données peuvent mettre des jours à être indexées), faux positifs (les alertes nécessitent une vérification humaine), et coût élevé (10 000 à 100 000+ $/an selon la couverture). Le monitoring artisanal (consultation manuelle des sources clés) reste complémentaire et irremplaçable pour les forums à accès restreint.

#### 24.3 Réduction du bruit

Le défi principal de la veille dark web est le bruit : les alertes non pertinentes, les données recyclées, les fausses revendications, et les scams. La réduction du bruit passe par l'affinement des mots-clés (spécifiques plutôt que génériques — « Vectris Aerospace » plutôt que « aerospace »), la vérification systématique des alertes (chaque alerte est évaluée : vrai positif, faux positif, données recyclées, scam), la priorisation (les alertes sur les leak sites de ransomware sont prioritaires sur les mentions dans des discussions génériques), et la connaissance de l'écosystème (l'analyste qui connaît les forums, les vendeurs habituels, et les patterns de publication sait distinguer une vraie menace du bruit de fond).

---

### Chapitre 25 — Preuve, capture et documentation

#### 25.1 Documentation du processus

L'investigation dark web produit des preuves dans un environnement intrinsèquement instable (les pages changent, les sites disparaissent, les posts sont supprimés). La documentation rigoureuse est donc encore plus critique que dans l'investigation classique.

Le **journal de collecte** (case log) enregistre chronologiquement chaque action : date/heure UTC, adresse visitée (.onion complète), persona utilisée, action effectuée (consultation, capture, téléchargement), résultat, et décision. Le journal est horodaté et hashé quotidiennement.

Chaque capture est accompagnée de métadonnées : date/heure UTC, adresse .onion + chemin complet, identifiant de la persona utilisée, outil de capture (Hunchly, screenshot manuel, wget), et hash SHA-256 de la capture. La chaîne de custody (simplifée par rapport au forensic judiciaire, mais rigoureuse) garantit l'intégrité des données collectées.

#### 25.2 Reproductibilité et limites

La grande difficulté des preuves dark web est la **non-reproductibilité** : un site .onion peut disparaître le lendemain de la capture, un post peut être supprimé, une page peut être modifiée. L'analyste ne peut pas toujours prouver qu'une page existait à un moment donné — il ne peut que prouver qu'il l'a capturée à un moment donné et que sa capture n'a pas été modifiée (hash d'intégrité). Cette limitation doit être explicitée dans le rapport : « la capture a été réalisée le [date] à [heure] UTC. Le site source peut avoir changé ou disparu depuis. »

---

## PARTIE VI — ANALYSE, RENSEIGNEMENT ET PRODUCTION

*La partie la plus critique pour l'analyste opérationnel : comment passer de l'observation brute à l'intelligence exploitable — en évitant les pièges analytiques qui sont omniprésents sur le dark web.*

---

### Chapitre 26 — Dé-anonymisation : méthodes et limites

#### 26.1 Exploitation des erreurs OPSEC

C'est la méthode la plus productive en pratique. Les erreurs classiques des opérateurs et acteurs du dark web : réutilisation de pseudo entre dark web et clear web (corrélable via Sherlock, WhatsMyName), réutilisation d'email (corrélable via DeHashed, IntelX, WHOIS), fuite d'IP par mauvaise configuration du hidden service (détectable par OnionScan), publication d'horaires d'activité cohérents avec un fuseau horaire spécifique (analyse des timestamps des posts), utilisation d'un style d'écriture identifiable (stylométrie — Ch.26.3), connexion depuis un réseau dont les métadonnées sont traçables, et erreurs de gestion financière (réutilisation d'adresses Bitcoin traçables, conversion via un exchange KYC).

#### 26.2 Cas de dé-anonymisation documentés

Analyse détaillée des erreurs OPSEC dans les cas les plus connus. **Ross Ulbricht** (Silk Road) : post StackOverflow avec son email personnel et pseudo « Frosty » sur un forum de champignons. **Alexandre Cazes** (AlphaBay) : email Hotmail personnel dans les headers de l'email de bienvenue du marché. **Hansa Market** : métadonnées des images du site et serveur de développement non anonymisé. **Dmitry Khoroshev** (LockBitSupp) : convergence d'indices — registrars, comptes crypto, analyse linguistique, renseignement humain. **Pompompurin** (BreachForums) : email personnel associé à un service en ligne traçable. Chaque cas illustre une catégorie d'erreur OPSEC différente — et une méthode d'investigation différente.

#### 26.3 Analyse linguistique et stylométrie

Le style d'écriture comme identifiant. Les marqueurs exploitables : langue native (détectable via les erreurs grammaticales, les calques syntaxiques), le registre (formel vs argotique vs technique), les tics de langage (abréviations, ponctuation, emojis), et l'orthographe (les erreurs récurrentes sont quasi uniques). La stylométrie computationnelle (comparaison statistique de textes) est un indice convergent mais pas une preuve à elle seule. L'analyse linguistique est particulièrement utile pour la corrélation cross-forum : un style distinctif retrouvé sur deux forums différents suggère le même auteur.

#### 26.4 Les limites de la dé-anonymisation

Un acteur avec une OPSEC disciplinée est extrêmement difficile à identifier. Tor lui-même n'a jamais été « cassé » au niveau cryptographique — les compromissions viennent toujours d'erreurs humaines ou de vulnérabilités d'implémentation. Monero est résistant au traçage. Les acteurs sophistiqués compartimentent rigoureusement (un pseudo par activité, des machines dédiées, aucune réutilisation d'identifiant). L'attribution définitive (identité réelle confirmée) nécessite généralement des moyens judiciaires (réquisitions, infiltrations) qui dépassent le périmètre de l'analyste privé.

---

### Chapitre 27 — Traçage crypto et analyse financière

#### 27.1 Bitcoin investigation

Les techniques d'analyse de la blockchain Bitcoin : clustering d'adresses (heuristiques d'input commun — les adresses utilisées comme inputs d'une même transaction sont probablement contrôlées par la même entité), identification des services (les exchanges, mixers, et marchés ont des patterns de transaction caractéristiques), et exploitation des points de conversion fiat↔crypto (réquisition judiciaire auprès des exchanges KYC pour obtenir l'identité du titulaire). Outils : OXT.me (gratuit, Bitcoin), Chainalysis Reactor (commercial, law enforcement), TRM Labs, Crystal Intelligence.

#### 27.2 Monero investigation

Beaucoup plus difficile que Bitcoin. Les approches possibles : analyse comportementale (corrélation timing de transactions avec d'autres activités), exploitation des erreurs (utilisation de la même adresse Monero sur le clear web et le dark web), heuristiques sur les anciennes transactions (ring signatures pré-2017 moins robustes), et exploitation des conversions Monero↔Bitcoin via les exchanges. Pour un adversaire non étatique, le traçage Monero est pratiquement impossible en 2025-2026.

#### 27.3 Fil rouge — DARKSTREAM : le traçage financier

> **🌐 DARKSTREAM — Épisode 9**
>
> Lucas analyse le wallet Bitcoin de « aero_source » visible dans le système de réputation d'IndustrialLeaks. Le wallet a reçu des paiements totalisant environ 85 BTC (~ 3 M€ au cours actuel) sur 2 ans. L'analyse OXT.me montre que les fonds sortants passent par un mixer connu avant d'arriver à un cluster d'adresses associé à un exchange KYC basé en Asie du Sud-Est. Lucas documente cette piste dans son rapport — si les autorités sont saisies, une réquisition auprès de l'exchange pourrait identifier le titulaire.

---

### Chapitre 28 — Pièges analytiques, désinformation et faux signaux

*Ce chapitre est l'un des plus importants du cours. Sur le dark web, les erreurs analytiques ne sont pas des exceptions — elles sont la norme si l'analyste ne s'en prémunit pas activement. Chaque observation doit être filtrée par une grille de vérification rigoureuse.*

#### 28.1 Faux leaks et données recyclées

Un « vendeur de données Vectris » peut être un scammer qui a repéré la couverture médiatique de la compromission et capitalise sur la peur de l'entreprise en vendant des données qu'il n'a pas. Les données peuvent aussi être recyclées : des documents publiés dans un breach antérieur non lié, repackagés et présentés comme « frais ». L'analyste vérifie l'authenticité (Ch.14) AVANT de conclure à la présence de données réelles.

#### 28.2 Faux drapeaux et usurpation de pseudo

Un acteur peut publier sous un faux pseudo pour incriminer un concurrent ou brouiller l'attribution. Les pseudos sont fréquemment réutilisés par des acteurs différents (un pseudo abandonné est repris par un nouveau venu). Un acteur peut se présenter comme affilié à un groupe connu (LockBit, BlackBasta) sans l'être — pour profiter de la crédibilité du groupe. L'analyste ne doit jamais attribuer sur la base d'un seul pseudo ou d'une seule revendication.

#### 28.3 Intoxication et manipulation

Les acteurs du dark web sont conscients de la surveillance des analystes CTI et des forces de l'ordre. Certains publient délibérément de fausses informations pour intoxiquer les observateurs : faux échantillons de données pour créer une panique chez la victime (et la pousser à payer plus vite), fausses revendications pour gonfler l'image du groupe, et faux « leaks internes » pour discréditer un concurrent. L'analyste doit traiter chaque information du dark web comme potentiellement fausse jusqu'à vérification par des sources indépendantes.

#### 28.4 Biais de survivance et biais d'échantillonnage

Le **biais de survivance** : les forums et marchés visibles sont ceux qui n'ont pas (encore) été saisis ou fermés. L'analyste qui observe les marchés actifs construit une image biaisée de l'écosystème — les marchés qui ont été saisis (potentiellement les plus actifs ou les plus visibles) sont absents de son échantillon. Le **biais d'échantillonnage** : l'analyste ne voit que les espaces auxquels il a accès. Les forums les plus fermés (accès par vouching uniquement, paiement de dizaines de milliers de dollars) restent invisibles. L'analyste doit expliciter ces limites dans ses conclusions.

#### 28.5 Confusion entre visibilité et importance

Un forum bruyant (beaucoup de posts, beaucoup de membres) n'est pas nécessairement important (il peut être plein de scams, de recyclage, et de bruit). Un forum discret (peu de membres, accès fermé) peut être beaucoup plus dangereux (transactions de haute valeur, acteurs sophistiqués). L'analyste doit évaluer la qualité, pas seulement la quantité.

#### 28.6 Surestimation du dark web

Le dark web fait l'objet d'une fascination médiatique qui déforme la réalité. La plupart des « révélations » médiatiques sur le dark web sont sensationnalistes, inexactes, ou obsolètes. L'analyste professionnel résiste à cette fascination et maintient une évaluation sobre : le dark web est un espace utile pour la collecte de renseignement, mais c'est un espace chaotique, peu fiable, et incomplet. Il ne doit jamais être la seule source d'une conclusion.

#### 28.7 Grille de vérification

Pour chaque observation sur le dark web, l'analyste applique une grille de vérification systématique : **Source** (quel forum, quelle ancienneté, quelle réputation ?), **Contenu** (les données sont-elles vérifiables ? les échantillons sont-ils cohérents ?), **Corroboration** (l'information est-elle confirmée par une source indépendante ?), **Motivation** (pourquoi l'acteur publie-t-il cette information ? quel est son intérêt ?), **Ancienneté** (les données sont-elles fraîches ou recyclées ?), et **Contexte** (l'information s'inscrit-elle dans un pattern connu ?). La grille complète est en Annexe E.

#### 28.8 Fil rouge — DARKSTREAM : le piège évité

> **🌐 DARKSTREAM — Épisode 10**
>
> Trois jours après son accès au forum, Lucas identifie un second post mentionnant Vectris — cette fois sur un canal Telegram public, par un compte différent (« data_broker_EU »). Le post prétend vendre « Vectris Aerospace full database — 500 GB — 30 BTC ». Les échantillons fournis sont des captures d'écran basse résolution de ce qui ressemble à des schémas techniques.
>
> Lucas applique sa grille de vérification. Le volume annoncé (500 Go) est incohérent avec l'exfiltration connue (420 Go). Le canal Telegram a été créé il y a 2 semaines (pas d'historique, pas de réputation). Les échantillons ne sont pas vérifiables (résolution trop basse pour confirmer l'authenticité). Le prix de 30 BTC est bas pour des données industrielles classifiées.
>
> **Conclusion :** probable scam opportuniste capitalisant sur le buzz de la compromission Vectris. Lucas le documente dans son journal mais ne le confond pas avec l'annonce d'« aero_source » (dont la crédibilité est beaucoup plus élevée — vendeur établi, forum fermé, échantillons vérifiables).

---

### Chapitre 29 — Transformer les observations en renseignement actionnable

*Ce chapitre fait le pont entre la collecte (Partie V) et la production (Ch.30). C'est ici que la donnée brute devient du renseignement.*

#### 29.1 De la donnée brute au renseignement

Une capture d'écran d'un post de forum n'est pas du renseignement — c'est une donnée brute. Le renseignement est le résultat de l'analyse, de la contextualisation, et de l'évaluation de cette donnée. Le processus de transformation comprend quatre étapes.

**Contextualisation :** placer l'observation dans son contexte. Un post de vente de données Vectris sur un forum spécialisé par un vendeur réputé est une observation très différente du même post sur un canal Telegram par un compte inconnu. Le contexte (qui publie, où, dans quel historique) change radicalement l'interprétation.

**Évaluation de crédibilité :** chaque source et chaque information sont évaluées indépendamment. La fiabilité de la source (le forum est-il connu, le vendeur est-il vérifié, l'historique est-il cohérent ?) et la crédibilité de l'information (les données sont-elles vérifiables, corroborées, cohérentes avec ce qu'on sait de la compromission ?). La grille d'évaluation de l'Annexe E formalise ce processus.

**Niveau de confiance :** chaque conclusion est accompagnée d'un niveau de confiance explicite, calibré selon la méthode des Admiralty Ratings (source fiabilité A-F × information crédibilité 1-6) ou un système simplifié (élevé, modéré, faible). Un renseignement sans niveau de confiance est un renseignement inutilisable — le décideur ne sait pas quelle confiance lui accorder.

**Implications :** qu'est-ce que cette observation signifie pour le client ? Quelles actions doit-il entreprendre ? Quelles décisions doit-il prendre ? Un renseignement qui n'a pas d'implication actionnable n'est pas du renseignement — c'est de l'information intéressante.

#### 29.2 Les différents publics et leurs besoins

L'analyste CTI produit pour des publics différents qui ont des besoins différents. Le **SOC/CSIRT** a besoin d'IoC (hash, domaines, IP, artefacts de persistance) pour la détection et le hunting — livrable : fiche d'IoC ou import STIX/TAXII. L'**équipe IR** a besoin de contexte sur la menace (quel groupe, quelles TTP, quel objectif) pour orienter l'investigation et la remédiation — livrable : note technique avec TTP mapping ATT&CK. Le **RSSI** a besoin d'une évaluation de risque (quelle est la menace, quelle est l'exposition, quelles sont les mesures prioritaires) — livrable : note de risque avec recommandations. Le **COMEX/direction** a besoin d'un résumé exécutif (quel est l'impact business, que fait-on, combien ça coûte) — livrable : executive brief sur 1-2 pages. Le **juridique** a besoin de faits documentés et de preuves (pour le dépôt de plainte, la notification CNIL, ou le contentieux assurance) — livrable : rapport factuel avec annexes de preuves.

#### 29.3 Quand escalader

L'analyste dark web doit savoir quand escalader vers d'autres équipes ou vers les autorités. Escalade vers l'**IR** : quand l'observation indique une menace active (accès vendu sur le SI du client, credentials fraîches en circulation, attaque en cours revendiquée). Escalade vers le **juridique** : quand des données personnelles ou classifiées sont confirmées en circulation (notification CNIL, signalement DGSI). Escalade vers le **COMEX** : quand l'impact réputationnel est imminent (publication imminente sur un leak site, couverture médiatique probable). Escalade vers les **autorités** : quand les données sont liées à la défense nationale, quand du CSAM est découvert, ou quand une menace physique est identifiée.

---

### Chapitre 30 — Produire une note analytique

#### 30.1 Structure d'une note analytique dark web

**Résumé exécutif** (1 page maximum) : ce qui a été observé, quelle menace cela représente, quel niveau de confiance, quelles actions recommandées. Ce résumé est souvent le seul élément lu par le décideur — il doit être autonome.

**Contexte** : le mandat, le périmètre de l'investigation, les sources consultées, et les limitations (qu'est-ce que l'analyste n'a PAS pu vérifier).

**Faits observés** : chaque observation est présentée factuellement, avec sa source, sa date, et son niveau de confiance. La distinction fait/déduction/hypothèse (empruntée au forensic, Ch.11 du cours Forensic) est explicite.

**Analyse** : contextualisation, évaluation de crédibilité, hypothèses concurrentes testées. L'analyste formule au moins deux hypothèses (par exemple : H1 — la vente est authentique et les données de Vectris sont en circulation ; H2 — la vente est un scam opportuniste utilisant des données recyclées) et indique laquelle est soutenue par les données avec quel niveau de confiance.

**Évaluation de la menace** : impact potentiel pour le client (financier, réputationnel, réglementaire, compétitif), probabilité de matérialisation, et urgence.

**Recommandations** : actions priorisées — techniques (IoC à intégrer dans le SOC, credentials à reseter, monitoring à renforcer), juridiques (signalement, dépôt de plainte, notification), communicationnelles (préparation de la communication de crise si publication imminente), et stratégiques (engagement des autorités, négociation avec l'assureur).

**Annexes** : captures d'écran hashées, fiches d'acteurs, cartographie d'écosystème, IoC, et journal de collecte.

#### 30.2 Formats spécifiques

La **fiche d'acteur** (profil d'un vendeur ou d'un groupe) : pseudo(s) connus, plateformes d'activité, type d'activité, historique de transactions, indicateurs linguistiques, wallets associés, et évaluation de la crédibilité. La **fiche de plateforme** (profil d'un forum ou d'un marché) : adresse(s), date de création, nombre estimé de membres, catégories d'activité, mécanismes de confiance, et évaluation de la pertinence. La **fiche d'incident** (alerte fuite de données) : données observées, source, authenticité estimée, volume, personnes/systèmes concernés, et actions recommandées. Les templates sont en Annexe F.

---

## PARTIE VII — CAS D'USAGE, TENDANCES ET PROSPECTIVE

---

### Chapitre 31 — Ransomware, extorsion et leak sites

Le ransomware est le point de convergence entre le dark web et la cybersécurité opérationnelle. Les leak sites sont la vitrine de l'extorsion. L'écosystème complet (IAB → RaaS affilié → négociation → publication) est détaillé au cours IR (Ch.32) et au cours Écosystèmes (Ch.16). Ce chapitre se concentre sur le volet dark web : comment surveiller les leak sites (outils : Ransomwatch, ransomfeed, monitoring commercial), comment interpréter une revendication (est-elle authentique ? les échantillons sont-ils crédibles ?), comment suivre l'évolution d'une négociation depuis l'extérieur (les portails de négociation sont parfois accessibles publiquement), et comment anticiper la publication (le compte à rebours est-il réel ou bluff ?). Le cas pratique du Ch.36 applique cette méthode à un scénario concret.

### Chapitre 32 — Dark web, influence et opérations informationnelles

Le dark web comme vecteur d'opérations d'influence : fuites orchestrées (des données sont volées puis publiées stratégiquement pour nuire à une organisation, un parti politique, ou un État — les hack-and-leak operations), relais entre espaces clandestins et réseaux sociaux (les données fuitées sur un forum .onion sont reprises par des comptes Twitter/X qui les amplifient auprès du grand public), instrumentalisation médiatique (les groupes de ransomware contactent directement les journalistes pour maximiser la couverture), et campagnes hybrides (combinaison de cyber-attaque, fuite de données, et amplification médiatique — le playbook des opérations d'influence russo-ukrainiennes post-2022). La porosité croissante entre cybercriminalité, hacktivisme, et opérations d'influence étatique rend la catégorisation des acteurs de plus en plus difficile.

### Chapitre 33 — Hacktivisme, zones grises et usages légitimes

Le dark web comme espace de résistance et de dissidence. SecureDrop et les plateformes de whistleblowing (comment elles fonctionnent, pourquoi l'anonymat est vital). Les mouvements hacktivistes (Anonymous, IT Army of Ukraine, groupes pro-russes) et leur utilisation du dark web pour la coordination et la publication. Les zones grises : contrebande informationnelle (fuites de documents gouvernementaux qui servent l'intérêt public mais violent la loi), activisme anti-censure (opérer des miroirs de sites d'information censurés dans des régimes autoritaires), et usage étatique ou para-étatique du dark web (les services de renseignement utilisent les mêmes outils que les criminels — la distinction est politique, pas technique). La difficulté de catégorisation morale et juridique est assumée : le même outil (Tor) est utilisé par un dissident iranien pour lire des nouvelles et par un trafiquant pour vendre de la drogue. L'analyste documente les faits sans porter de jugement moral.

### Chapitre 34 — Forces de l'ordre, disruption et droit international

#### 34.1 Les grandes opérations de police

Analyse détaillée des opérations majeures : Operation Bayonet (2017 — AlphaBay + Hansa), Operation Cookie Monster (2023 — Genesis Market), Operation SpecTor (2023 — 288 arrestations), et Operation Cronos (2024 — LockBit). Pour chaque opération : méthodes, résultats, et enseignements. Les méthodes récurrentes : exploitation des erreurs OPSEC des opérateurs, infiltration (opérer le marché sous contrôle policier), retournement d'informateurs, et analyse de la blockchain Bitcoin.

#### 34.2 Disruption et impact

Les takedowns perturbent mais ne détruisent pas les écosystèmes. L'impact le plus durable est sur la confiance : les saisies policières, combinées avec les exit scams, créent une méfiance chronique qui augmente le coût et le risque des transactions pour les criminels. La publication des « seizing pages » (pages de saisie affichant les logos des forces de l'ordre) et des données saisies (identités de vendeurs, transactions) est un outil de disruption psychologique autant que judiciaire.

#### 34.3 Cadre juridique international

La Convention de Budapest (2001, Conseil de l'Europe, ratifiée par 68 pays en 2025) est le traité de référence. Les MLAT (traités d'entraide judiciaire) pour les réquisitions cross-border. Le Cloud Act américain (accès aux données des providers US indépendamment de la localisation). La question de la juridiction (serveur au Panama, opérateur en Russie, vendeur en Allemagne, acheteur en France — quel pays est compétent ?). Et la coopération effective via Europol (EC3), Interpol, et le Joint Cybercrime Action Taskforce (J-CAT).

---

## PARTIE VIII — ÉTUDES DE CAS ET SYNTHÈSE

---

### Chapitre 35 — Cas complet : investigation d'une vente de données industrielles (synthèse DARKSTREAM)

Synthèse du fil rouge sous forme de cas autonome. Du mandat initial à la note analytique finale, en passant par la configuration OPSEC (Whonix, persona, wallet dédié), l'accès au forum (paiement documenté), l'analyse du profil du vendeur (ancienneté, historique, style linguistique), la vérification des échantillons (cohérence avec les données de Vectris, métadonnées, classification), le pivot OSINT (pseudo → Tox ID → forum archivé → wallet Bitcoin → exchange), le filtrage des scams (le faux vendeur Telegram identifié et écarté), le traçage financier (wallet Bitcoin → mixer → exchange KYC), et la production du rapport pour Vectris et la DGSI.

Conclusions du rapport de Lucas : les données de Vectris sont authentiques et en circulation sur IndustrialLeaks (niveau de confiance : élevé). Le vendeur « aero_source » est un courtier spécialisé, probablement basé en Europe de l'Est (niveau de confiance : modéré). Au moins 2 acheteurs ont acquis les données sur les 10 derniers jours (visible via les transactions du système d'escrow du forum). Le signalement à la DGSI est recommandé (données liées à des programmes de défense). Les credentials de 12 employés de Vectris sont aussi en circulation sur Russian Market (découverte collatérale — escalade immédiate vers le SOC de Vectris pour reset).

### Chapitre 36 — Cas complet : surveillance d'un leak site ransomware

Un RSSI découvre que son entreprise (ETI du secteur logistique, 1 200 employés) est listée sur le leak site d'un opérateur RaaS (BlackBasta), avec un compte à rebours de 10 jours et des échantillons de documents internes. L'analyste CTI doit identifier le groupe (BlackBasta — confirmation via les TTP connues et le style du leak site), évaluer l'authenticité (les échantillons correspondent à des documents internes réels — confirmé par le client), surveiller la publication (monitoring quotidien du leak site et des canaux Telegram associés), et alimenter la cellule de crise (situational awareness, options de réponse, timing de la communication). Le cas illustre le workflow complet de monitoring d'un leak site en temps réel, avec les décisions clés à chaque étape.

### Chapitre 37 — Cas complet : traque d'un IAB vendant des accès

Un analyste détecte une annonce de vente d'accès VPN au SI d'un client (banque régionale) sur le forum Exploit.in. L'annonce mentionne « French bank, 2500 employees, Citrix VPN, Domain Admin access, asking 15000$ ». L'investigation vérifie l'authenticité (le nombre d'employés et le type de VPN correspondent), identifie la source de compromission probable (infostealer — les credentials VPN apparaissent dans les logs Russian Market, datés de 3 semaines), trace le vendeur (profil IAB actif depuis 6 mois, 8 ventes confirmées, spécialisé dans le secteur financier européen), et alimente l'IR pour la remédiation immédiate (reset des credentials VPN, déploiement MFA, investigation forensic sur le poste source de l'infostealer).

### Chapitre 38 — Maturité analyste et programme de veille durable

#### 38.1 Niveaux de maturité

**Débutant :** navigue sur le dark web avec les outils de base, sait trouver les forums principaux, peut faire une capture d'écran horodatée. Ne sait pas encore distinguer un scam d'une vraie offre, n'a pas de méthodologie de vérification, et risque de tirer des conclusions hâtives.

**Intermédiaire :** maîtrise l'OPSEC, gère des personas, connaît les forums clés et les vendeurs habituels, sait vérifier l'authenticité d'une fuite, sait pivoter entre dark web et surface web, et produit des notes analytiques structurées avec niveaux de confiance.

**Avancé :** comprend les dynamiques sociologiques des communautés underground, détecte les scams et les intoxications, corrèle entre multiples sources (forums, Telegram, blockchain, OSINT), produit des cartographies d'écosystèmes, et forme les analystes juniors.

#### 38.2 Programme de veille durable

Un programme de veille dark web durable repose sur des objectifs clairs (quelles menaces surveiller, pour quels clients/métiers), des sources priorisées (forums, leak sites, marchés de logs, Telegram — avec une couverture réaliste, pas exhaustive), une fréquence adaptée (quotidienne pour les leak sites ransomware, hebdomadaire pour les forums, mensuelle pour les rapports de tendance), une documentation rigoureuse (journal de collecte, fiches de plateforme, fiches d'acteurs), une articulation avec les autres équipes (SOC, IR, CTI, juridique, communication), et une amélioration continue (retex après chaque investigation, mise à jour des sources, formation continue).

#### 38.3 Les bonnes habitudes de l'analyste

Ne jamais considérer une seule source comme suffisante. Toujours documenter ce qu'on observe ET ce qu'on ne peut pas observer (les limitations). Maintenir une séparation stricte entre identité professionnelle et personas d'investigation. Ne jamais surestimer ce que le dark web peut nous apprendre. Et résister à la fascination du clandestin — le dark web est un outil de travail, pas un terrain d'aventure.

---

## ANNEXES

---

### Annexe A — Glossaire

| Terme | Définition |
|-------|-----------|
| **.onion** | Domaine de premier niveau utilisé par les onion services Tor (adresses de 56 caractères en v3) |
| **Atomic swap** | Échange direct entre deux cryptomonnaies sans intermédiaire centralisé |
| **Beaconing** | Pattern de communication périodique entre un malware et son serveur C2 |
| **Bridge** | Relais Tor non listé publiquement, utilisé pour contourner la censure |
| **Bulletproof hosting** | Hébergement qui ignore les plaintes d'abus et les requêtes judiciaires |
| **Carving** | Technique de récupération de données par reconnaissance de signatures |
| **CoinJoin** | Protocole décentralisé de mixing Bitcoin par transaction collaborative |
| **Combo list** | Liste massive de couples email/mot de passe issus de multiples breaches |
| **C2** | Command and Control — infrastructure de commande d'un malware |
| **Darknet** | Réseau overlay conçu pour l'anonymat (Tor, I2P, Freenet) |
| **Dark web** | Ensemble des contenus accessibles via les darknets |
| **DDoS** | Distributed Denial of Service — attaque par saturation de trafic |
| **Dead drop** | Point de dépôt physique utilisé pour la livraison de biens illicites |
| **Dead man's switch** | Mécanisme automatique activé si l'opérateur ne se manifeste pas |
| **Deep web** | Contenus web non indexés par les moteurs de recherche (90 % du web) |
| **DHT** | Distributed Hash Table — table de hachage distribuée utilisée par Tor pour les descripteurs |
| **Directory authority** | Serveur de confiance maintenant le consensus sur l'état du réseau Tor |
| **Eepsite** | Site web hébergé sur le réseau I2P |
| **Escrow** | Séquestre de fonds par un tiers de confiance pendant une transaction |
| **Exit node** | Dernier relais d'un circuit Tor, point de sortie vers Internet |
| **Exit scam** | Disparition de l'opérateur d'un marché avec les fonds d'escrow |
| **Fullz** | Identité complète pour l'usurpation (nom, adresse, SSN, date de naissance) |
| **Garlic routing** | Variante de l'onion routing utilisée par I2P (encapsulation multi-messages) |
| **Guard node** | Premier relais d'un circuit Tor — voit l'IP réelle de l'utilisateur |
| **Hidden service** | Ancien terme pour onion service — serveur accessible via Tor |
| **IAB** | Initial Access Broker — acteur vendant des accès réseau compromis |
| **Introduction point** | Relais Tor servant de point de contact initial pour un onion service |
| **JA3/JA4** | Fingerprint TLS pour identifier des clients réseau spécifiques |
| **Leak site** | Site .onion où les groupes de ransomware publient les données des victimes |
| **Log (infostealer)** | Session complète volée par un infostealer (credentials, cookies, données machine) |
| **Lurker** | Membre d'un forum qui observe sans participer |
| **Middle relay** | Relais intermédiaire d'un circuit Tor |
| **Mixer / Tumbler** | Service mélangeant les fonds crypto de plusieurs utilisateurs |
| **Monero (XMR)** | Cryptomonnaie conçue pour la confidentialité des transactions |
| **NIT** | Network Investigative Technique — exploit utilisé par le FBI pour dé-anonymiser |
| **Onion routing** | Technique de chiffrement en couches pour l'anonymat réseau |
| **Onion service** | Serveur accessible exclusivement via le réseau Tor (adresse .onion) |
| **OPSEC** | Operational Security — pratiques de sécurité opérationnelle |
| **PHAROS** | Plateforme française de signalement des contenus illicites en ligne |
| **Pluggable transport** | Protocole qui déguise le trafic Tor pour contourner la censure (obfs4, Snowflake, meek) |
| **Proof-of-work captcha** | Captcha basé sur un calcul intensif, protection anti-DDoS et anti-bot |
| **RaaS** | Ransomware-as-a-Service — modèle franchisé de distribution de ransomware |
| **Rendezvous point** | Relais Tor servant de point de rendez-vous entre client et onion service |
| **Ring signature** | Signature cryptographique par un groupe d'adresses (Monero) |
| **Russian Market** | Marché de logs d'infostealers dominant (successeur de Genesis Market) |
| **Scam** | Arnaque — offre frauduleuse sans intention de livrer |
| **SecureDrop** | Plateforme de whistleblowing anonyme basée sur Tor |
| **Sock puppet** | Fausse identité (persona) créée pour l'investigation |
| **Stealth address** | Adresse crypto à usage unique générée pour chaque transaction (Monero) |
| **Surface web** | Web indexé par les moteurs de recherche (~5-10 % du web) |
| **Tails** | Système d'exploitation amnésique et anonyme (bootable depuis USB) |
| **Tor** | The Onion Router — réseau d'anonymat le plus utilisé |
| **Tox** | Messagerie peer-to-peer chiffrée, utilisée sur les forums underground |
| **Vanity address** | Adresse .onion avec un préfixe personnalisé généré par force brute |
| **Vouching** | Système de parrainage par un membre établi d'un forum |
| **Whonix** | VM dédiée au routage Tor avec isolation réseau stricte |

---

### Annexe B — Typologie des espaces dark web

| Type d'espace | Fonction | Exemples d'usage | Intérêt analytique | Limites |
|--------------|----------|-----------------|-------------------|---------|
| **Forums généralistes** | Discussion, vente, recrutement, socialisation | XSS, Exploit, BreachForums successeurs | Large spectre de menaces, tendances | Bruit, scams, accès souvent fermé |
| **Forums spécialisés** | Vente ciblée (données industrielles, carding, etc.) | IndustrialLeaks, forums de carding | Données de haute valeur, acteurs spécialisés | Très fermés, peu de membres, difficile d'accès |
| **Marchés généralistes** | Commerce multi-catégories (stupéfiants, données, services) | Successeurs d'Hydra et AlphaBay | Volume, diversité, tendances économiques | Cycle de vie court, exit scams fréquents |
| **Marchés de logs** | Vente de sessions volées par infostealers | Russian Market | Credentials d'entreprise, monitoring de fuite | Volume massif, nécessite filtrage |
| **Leak sites ransomware** | Publication de données de victimes | LockBit, BlackBasta, Play | Monitoring des attaques, TTP, secteurs ciblés | Données potentiellement sensibles |
| **Canaux Telegram** | Promotion, vente rapide, communication | Canaux de revente, IAB, ransomware | Accessibilité, rapidité | Moins d'anonymat, éphémérité |
| **IRC / XMPP / Tox** | Communication directe | Négociation, coordination | Transactions privées | Invisibles de l'extérieur |
| **Pastebins** | Publication éphémère | Dumps de credentials, IoC | Données techniques | Volatilité, liens morts |

---

### Annexe C — OPSEC analyste : checklists

#### Checklist configuration poste d'investigation

- [ ] Laptop dédié (sans données pro/perso)
- [ ] Whonix installé (Gateway + Workstation) OU Tails sur USB
- [ ] VPN commercial configuré (en amont de Tor si choisi)
- [ ] Aucun compte personnel connecté sur le poste
- [ ] Réseau séparé du réseau professionnel (WiFi public ou SIM prépayée)
- [ ] Hunchly installé dans le Tor Browser de la VM
- [ ] Outils de capture et de hashing disponibles
- [ ] Journal de collecte ouvert

#### Checklist création de persona

- [ ] Pseudonyme cohérent avec le forum ciblé
- [ ] Email jetable créé via Tor (ProtonMail/Tutanota sans téléphone)
- [ ] Wallet crypto dédié (un par persona)
- [ ] Tox ID dédié (si nécessaire)
- [ ] Backstopping minimal (comptes sur 2-3 plateformes secondaires)
- [ ] Aucun croisement avec l'identité réelle (réseau, horaires, patterns)
- [ ] Documentation de la persona dans un fichier sécurisé

#### Checklist navigation sécurisée

- [ ] Tor Browser en mode « Safest » (JavaScript désactivé)
- [ ] Fenêtre du navigateur NON maximisée
- [ ] Aucune extension installée (au-delà de Hunchly)
- [ ] Aucun téléchargement de fichier sans analyse préalable (sandbox)
- [ ] Aucune connexion à un compte personnel
- [ ] Captures d'écran horodatées pour chaque page pertinente
- [ ] Hash SHA-256 calculé sur chaque capture
- [ ] Journal de collecte mis à jour en temps réel

#### Checklist fin de session

- [ ] Toutes les captures hashées et archivées
- [ ] Journal de collecte complété et hashé
- [ ] VM Workstation réinitialisée au snapshot propre
- [ ] Aucune donnée résiduelle sur le poste hôte (si Tails : extinction suffit)
- [ ] VPN déconnecté

---

### Annexe D — Outils d'investigation dark web

| Catégorie | Outil | Gratuit/Payant | Usage | Limites |
|-----------|-------|---------------|-------|---------|
| **Navigation** | Tor Browser | Gratuit | Navigation .onion | Lent, certains sites exigent JavaScript |
| **Navigation** | Whonix | Gratuit | VM avec isolation réseau Tor | Configuration initiale complexe |
| **Navigation** | Tails | Gratuit | OS amnésique, portable | Pas de persistance par défaut |
| **Documentation** | Hunchly | Payant (~130 $/an) | Capture auto + hash + timeline | Extension navigateur uniquement |
| **Scan** | OnionScan | Gratuit | Scan de hidden services (IP leaks, config) | Non maintenu activement (communauté) |
| **Crawling** | TorBot | Gratuit | Crawler .onion | Basique, pas d'anti-bot bypass |
| **Monitoring** | Flare | Payant | Monitoring dark web + clear web | Couverture incomplète sur forums fermés |
| **Monitoring** | Recorded Future | Payant | CTI plateforme avec sources dark web | Coût élevé, latence |
| **Monitoring** | Cybersixgill | Payant | Monitoring dark web spécialisé | Couverture variable |
| **OSINT** | Sherlock | Gratuit | Recherche de pseudo cross-platform | Faux positifs fréquents |
| **OSINT** | WhatsMyName | Gratuit | Recherche de pseudo (plus complet que Sherlock) | Web only (pas dark web natif) |
| **OSINT** | SpiderFoot | Gratuit (OSS) / Payant (HX) | Framework OSINT modulaire | Courbe d'apprentissage |
| **OSINT** | Maltego | Payant | Graphe de relations, transforms dark web | Coût élevé |
| **Breach** | DeHashed | Payant (abo) | Recherche dans les bases de breaches | Couverture variable |
| **Breach** | IntelX | Freemium | Recherche breaches + pastebins + dark web | Résultats limités en version gratuite |
| **Breach** | Have I Been Pwned | Gratuit | Vérification d'email dans les breaches | Emails uniquement, pas de données |
| **Crypto** | OXT.me | Gratuit | Exploration blockchain Bitcoin | Bitcoin uniquement |
| **Crypto** | Chainalysis Reactor | Payant (LE) | Traçage crypto avancé multi-chain | Accès restreint (forces de l'ordre) |
| **Crypto** | TRM Labs | Payant | Traçage et compliance crypto | Accès restreint |
| **Ransomware** | Ransomwatch | Gratuit | Monitoring leak sites ransomware | Couverture manuelle, délai |
| **Linguistique** | Writeprints / Stylometry | Gratuit (académique) | Analyse de style d'écriture | Résultats indicatifs, pas probants |

---

### Annexe E — Grille d'évaluation de crédibilité

#### Évaluation de la source

| Critère | Score | Description |
|---------|-------|-------------|
| Ancienneté | 1-5 | 1 = nouveau compte, 5 = actif depuis 3+ ans |
| Réputation | 1-5 | 1 = aucune transaction, 5 = 100+ transactions confirmées, rating > 4.5 |
| Spécialisation | 1-5 | 1 = généraliste, 5 = spécialiste reconnu du type de données vendues |
| Forum de publication | 1-5 | 1 = canal Telegram public, 5 = forum fermé de référence (Exploit, XSS) |
| Cohérence historique | 1-5 | 1 = incohérences dans le profil, 5 = historique parfaitement cohérent |

#### Évaluation de l'information

| Critère | Score | Description |
|---------|-------|-------------|
| Vérifiabilité des échantillons | 1-5 | 1 = pas d'échantillon, 5 = échantillons vérifiés authentiques |
| Fraîcheur | 1-5 | 1 = données recyclées connues, 5 = données jamais vues, fraîches |
| Corroboration | 1-5 | 1 = aucune source indépendante, 5 = confirmé par 2+ sources indépendantes |
| Cohérence interne | 1-5 | 1 = incohérences majeures, 5 = parfaitement cohérent |
| Absence d'indicateurs de scam | 1-5 | 1 = indicateurs de scam présents, 5 = aucun indicateur de scam |

#### Niveaux de confiance résultants

| Score combiné | Niveau de confiance | Interprétation |
|--------------|-------------------|----------------|
| 40-50 | **Élevé** | Information probablement fiable, source crédible, corroborée |
| 25-39 | **Modéré** | Information plausible mais non confirmée, source partiellement vérifiable |
| 10-24 | **Faible** | Information non vérifiée, source inconnue ou peu crédible |
| < 10 | **Très faible / suspect** | Probable scam, intoxication, ou données recyclées |

---

### Annexe F — Templates de livrables

#### Template fiche d'acteur

```
FICHE ACTEUR — [PSEUDO]
Date de création : [date]    Dernière MàJ : [date]    Analyste : [nom]

IDENTIFIANTS
  Pseudo(s) : [liste]
  Plateformes : [forums, Telegram, etc.]
  Email(s) connus : [liste]
  Tox / Jabber / Session ID : [liste]
  Wallet(s) crypto : [adresses]
  PGP key fingerprint : [si disponible]

PROFIL
  Type d'activité : [vendeur données, IAB, développeur malware, etc.]
  Spécialisation : [secteur, type de données, géographie des cibles]
  Ancienneté : [date du premier post connu]
  Volume d'activité : [nb transactions, volume estimé]
  Rating/Réputation : [score, nb de reviews]

ANALYSE LINGUISTIQUE
  Langue probable : [indices]
  Fuseau horaire probable : [basé sur horaires d'activité]
  Style d'écriture : [notes]

ÉVALUATION
  Crédibilité : [élevée / modérée / faible]
  Niveau de menace : [élevé / modéré / faible]
  Pistes d'identification : [pseudos corrélés, wallets traçables, etc.]

SOURCES
  [liste des captures, dates, hash]
```

#### Template note analytique (résumé)

```
NOTE ANALYTIQUE — [TITRE]
Classification : [CONFIDENTIEL / DIFFUSION RESTREINTE]
Date : [date]    Analyste : [nom]    Référence : [code]

RÉSUMÉ EXÉCUTIF (1 page max)
  - Observation principale
  - Niveau de confiance
  - Impact potentiel
  - Actions recommandées

CONTEXTE
  - Mandat, périmètre, sources consultées, limitations

FAITS OBSERVÉS
  - [fait 1 — source, date, confiance]
  - [fait 2 — source, date, confiance]

ANALYSE
  - Hypothèse 1 : [description, éléments pour/contre, confiance]
  - Hypothèse 2 : [description, éléments pour/contre, confiance]
  - Hypothèse retenue : [laquelle, pourquoi]

ÉVALUATION DE LA MENACE
  - Impact : [financier / réputationnel / réglementaire / compétitif]
  - Probabilité : [élevée / modérée / faible]
  - Urgence : [immédiate / court terme / moyen terme]

RECOMMANDATIONS
  1. [action — responsable — échéance]
  2. [action — responsable — échéance]

ANNEXES
  - Captures hashées
  - Fiches d'acteurs
  - IoC
  - Journal de collecte
```

---

### Annexe G — Ressources et veille

#### Rapports de référence

| Rapport | Éditeur | Fréquence | Focus |
|---------|---------|-----------|-------|
| Internet Organised Crime Threat Assessment (IOCTA) | Europol | Annuel | Panorama des menaces cyber en Europe |
| Crypto Crime Report | Chainalysis | Annuel | Flux financiers criminels en crypto |
| M-Trends | Mandiant/Google | Annuel | Incidents et tendances IR/CTI |
| Data Breach Investigations Report (DBIR) | Verizon | Annuel | Statistiques sur les breaches |
| Threat Landscape | ENISA | Annuel | Menaces cyber en Europe |
| Dark Web Price Index | Privacy Affairs | Semestriel | Prix des données et services sur le dark web |

#### Outils de veille gratuits

| Outil | Type | Usage |
|-------|------|-------|
| Tor Metrics (metrics.torproject.org) | Dashboard | Statistiques du réseau Tor |
| Ransomwatch | GitHub | Monitoring des leak sites ransomware |
| Ransomfeed | Site web | Agrégation des revendications ransomware |
| Have I Been Pwned | Service web | Vérification d'exposition des emails |
| VirusTotal | Service web | Vérification de hash, domaines, IP |
| Shodan | Service web | Recherche d'infrastructure exposée |

#### Communautés et conférences

| Ressource | Type | Description |
|-----------|------|-------------|
| FIRST | Communauté | Forum international des CERT/CSIRT |
| InterCERT France | Communauté | Association des CERT français |
| DEF CON | Conférence | Plus grande conférence hacking (Las Vegas) |
| Black Hat | Conférence | Conférence sécurité recherche/industrie |
| Botconf | Conférence | Conférence sur les botnets et le malware (France) |
| FIC (Forum InCyber) | Conférence | Forum européen de cybersécurité (Lille) |
| SSTIC | Conférence | Symposium sur la sécurité des TIC (Rennes) |
| r/darknet | Reddit | Communauté de discussion (prudence — biais) |
| DarkOwl Blog | Blog | Analyses et rapports sur le dark web |
| Flashpoint Blog | Blog | Intelligence sur les menaces underground |

---

> **Note de clôture**
>
> Ce cours a été conçu pour former des professionnels à l'investigation et à l'analyse du dark web — pas pour satisfaire une curiosité morbide ni pour fournir un mode d'emploi d'activités illicites.
>
> Le dark web est un espace opérationnel pour l'analyste CTI, l'investigateur, et le RSSI. C'est là que les données volées apparaissent, que les accès compromis sont vendus, que les groupes de ransomware revendiquent, et que les menaces se matérialisent. Ne pas le comprendre, c'est naviguer à l'aveugle dans le paysage de la menace.
>
> Mais le comprendre exige de la rigueur — une rigueur que ce cours a cherché à transmettre à travers chaque chapitre. Rigueur méthodologique (OPSEC, documentation, chaîne de preuve). Rigueur analytique (vérification, hypothèses concurrentes, niveaux de confiance, résistance aux biais). Rigueur éthique (cadre juridique, signalement, séparation des rôles). Et rigueur intellectuelle (le dark web est un outil d'observation parmi d'autres, pas une source infaillible ni un terrain de fascination).
>
> L'opération DARKSTREAM illustre cette rigueur : Lucas n'a pas seulement « trouvé des données sur le dark web » — il a vérifié leur authenticité, écarté les scams, contextualisé la menace, évalué la crédibilité de la source, documenté chaque étape, et produit un rapport exploitable par des décideurs qui n'ont jamais visité un site .onion.
>
> *Comprendre • Explorer • Cartographier • Investiguer • Contextualiser • Produire — avec rigueur et discernement.*

