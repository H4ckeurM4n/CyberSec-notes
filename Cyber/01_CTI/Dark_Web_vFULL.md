# LE DARK WEB — COMPRENDRE, NAVIGUER, INVESTIGUER

*Architecture • Écosystèmes • OPSEC • Investigation • Renseignement*

**Cours complet — 44 chapitres, 8 parties, 7 annexes.**

-----

## Avant-propos

Ce cours apprend à **comprendre et investiguer le dark web** dans une posture professionnelle. Il s’adresse aux analystes CTI, investigateurs, RSSI, chercheurs en sécurité, et professionnels de la conformité et de la lutte contre la cybercriminalité. Il est conçu pour être **auto-suffisant** — un lecteur qui part de zéro, travaille le cours dans l’ordre, et fait les exercices proposés, acquiert un niveau professionnel.

**Ce que ce cours fait** : il vous apprend à situer le dark web dans le paysage numérique, comprendre ses infrastructures techniques (Tor, I2P, cryptomonnaies), cartographier ses écosystèmes (forums, marchés, leak sites, messageries), naviguer avec une OPSEC rigoureuse, investiguer une fuite de données ou une compromission, produire du renseignement actionnable, et coopérer avec les autorités. Il couvre aussi les cadres juridiques, les pièges analytiques, et les évolutions 2024-2026.

**Ce que ce cours ne fait pas** : il n’est pas un mode d’emploi pour l’activité criminelle. Il ne fournit pas de liens actifs vers des plateformes illicites, ne donne pas de techniques de contournement du law enforcement pour un usage criminel, et ne vend pas de sensationnel. Les exemples techniques sont suffisamment précis pour comprendre, pas assez pour reproduire une infraction.

**Posture pédagogique** : factuelle, calibrée, vérifiable. Chaque affirmation forte renvoie à une source publique (rapport d’agence, publication journalistique reconnue, analyse vendor CTI sérieuse). Les ordres de grandeur sont donnés avec leurs limites. Les analyses sont honnêtes sur l’incertitude.

**Continuité avec la bibliothèque** : ce cours s’articule avec OSINT Mastery (techniques OSINT transposées au dark web), AU CŒUR DES APT (acteurs étatiques qui utilisent le dark web pour leurs opérations), Cartographie des écosystèmes cybercriminels (contexte structural), OSINT Crypto (traçage blockchain), et FININT (investigation financière). Les renvois explicites permettent d’approfondir sans dupliquer.

-----

## Table des matières

- [Fil rouge : Opération DARKSTREAM](#fil-rouge--opération-darkstream)

**PARTIE I — FONDATIONS**

- Ch.1 — Internet, web visible, deep web, dark web
- Ch.2 — Histoire et évolution des darknets
- Ch.3 — Pourquoi le dark web existe
- Ch.4 — Le dark web comme écosystème

**PARTIE II — INFRASTRUCTURES TECHNIQUES ET ANONYMAT**

- Ch.5 — Architecture de Tor
- Ch.6 — Onion services (hidden services)
- Ch.7 — I2P, Freenet et réseaux alternatifs
- Ch.8 — Cryptomonnaies et anonymat financier
- Ch.9 — Hébergement, infrastructure et résilience

**PARTIE III — ÉCOSYSTÈMES DU DARK WEB**

- Ch.10 — Forums clandestins : culture, hiérarchie et codes
- Ch.11 — Marchés du dark web : histoire, fonctionnement, évolution
- Ch.12 — Leak sites ransomware et vitrines de revendication
- Ch.13 — Canaux, chats et messageries clandestines
- Ch.14 — Données volées et marchés de la fuite
- Ch.15 — Stealer logs : anatomie, marchés, investigation
- Ch.16 — Services criminels et profils d’acteurs
- Ch.17 — Marché des 0-day et chaîne exploit → attaque

**PARTIE IV — ÉCONOMIE CLANDESTINE**

- Ch.18 — Pourquoi l’économie du dark web fonctionne
- Ch.19 — Réputation, escrow, vouching, arbitrage
- Ch.20 — Arnaques, exit scams et manipulation de la confiance
- Ch.21 — Modèles économiques criminels

**PARTIE V — INVESTIGATION, VEILLE ET COLLECTE**

- Ch.22 — Cadre juridique, éthique et sécurité de l’analyste
- Ch.23 — OPSEC opérationnelle de l’investigation
- Ch.24 — Naviguer et collecter : méthodes, outils, limites
- Ch.25 — Investigation dans un data leak : workflow
- Ch.26 — Pivoting, enrichissement et corrélation OSINT
- Ch.27 — Veille dark web : surveillance, alerting, réduction du bruit
- Ch.28 — Preuve, capture et documentation

**PARTIE VI — ANALYSE, RENSEIGNEMENT ET PRODUCTION**

- Ch.29 — Dé-anonymisation : méthodes et limites
- Ch.30 — NIT, honeypots et infiltration policière
- Ch.31 — Traçage crypto et analyse financière
- Ch.32 — Pièges analytiques, désinformation, faux signaux
- Ch.33 — Transformer les observations en renseignement actionnable
- Ch.34 — Produire une note analytique
- Ch.35 — Menaces dark web par secteur d’activité

**PARTIE VII — CAS D’USAGE, TENDANCES ET PROSPECTIVE**

- Ch.36 — Ransomware, extorsion et leak sites
- Ch.37 — Dark web, influence et opérations informationnelles
- Ch.38 — Hacktivisme, zones grises et usages légitimes
- Ch.39 — IA et dark web : menaces émergentes et défensives
- Ch.40 — Forces de l’ordre, disruption et coopération internationale

**PARTIE VIII — ÉTUDES DE CAS ET SYNTHÈSE**

- Ch.41 — Cas DARKSTREAM complet — investigation d’une vente de données industrielles
- Ch.42 — Cas surveillance d’un leak site ransomware
- Ch.43 — Cas traque d’un Initial Access Broker
- Ch.44 — Maturité analyste et programme de veille durable

**ANNEXES**

- Annexe A — Glossaire
- Annexe B — Typologie des espaces dark web
- Annexe C — OPSEC analyste : checklists
- Annexe D — Outils d’investigation dark web
- Annexe E — Grille d’évaluation de crédibilité
- Annexe F — Templates de livrables
- Annexe G — Ressources et veille

-----

## Fil rouge : Opération DARKSTREAM

Pour ancrer la théorie dans la pratique, ce cours suit un cas fictif inspiré d’investigations réelles. **Opération DARKSTREAM** déroule, chapitre après chapitre, l’investigation d’une exfiltration de données industrielles.

**Le contexte.** **Vectris Aerospace** est un équipementier aérospatial européen (4 500 collaborateurs, coté SBF 120), partenaire de plusieurs programmes de défense et spatiaux. En mars 2026, son SOC détecte une anomalie de trafic sortant vers une IP résidentielle. L’investigation interne remonte à un poste R&D compromis. Volume exfiltré estimé : **420 Go** — spécifications techniques, documents de conception, bases clients, notes de conception propulsion. Compromission entre 8 et 14 semaines avant détection. Vectris classifie l’incident *critique*, notifie l’ANSSI et la DGSI (OIV défense), et mandate **Athéna Group**, un cabinet CTI français.

**L’analyste.** **Lucas Ferreira**, analyste CTI senior chez Athéna Group. 8 ans d’expérience dont 3 au CERT d’une grande banque. PASSI-qualifié. Le mandat d’Athéna : **(1)** confirmer ou infirmer la circulation des données Vectris sur le dark web ; **(2)** authentifier les données offertes ; **(3)** cartographier l’écosystème impliqué (vendeur, acheteurs potentiels, courtiers) ; **(4)** produire un rapport actionnable pour Vectris et la DGSI ; **(5)** si possible, contribuer à l’identification du vendeur.

**Les signaux initiaux.** Un service de monitoring (Recorded Future) a détecté une mention de « Vectris » et « propulsion specs » sur un forum .onion russophone, **IndustrialLeaks** — forum spécialisé dans les données industrielles, ~3 000 membres, créé en 2022. Un vendeur au pseudonyme **aero_source** propose « aerospace dump 420GB, EU supplier, reconnaissance française, propulsion R&D inside ». Prix demandé : 65 000 USDT.

**La méthode.** Lucas applique une méthode rigoureuse : OPSEC stricte pour la collecte, authentification par échantillons, pivoting OSINT sur le pseudonyme, traçage crypto des transactions connues, analyse linguistique, corrélation cross-forum, calibration de l’attribution. L’opération durera **6 semaines** — Ch.41 en détaillera la synthèse complète.

Les épisodes DARKSTREAM jalonnent le cours aux moments où le concept enseigné éclaire la progression de Lucas.

-----

## PARTIE I — FONDATIONS : COMPRENDRE LE DARK WEB

> **Ce que cette partie apprend.** Situer le dark web dans le paysage numérique, comprendre la différence entre surface, deep et dark web, connaître son histoire, saisir pourquoi il existe, et le considérer comme un écosystème plutôt qu’un lieu.
> 
> **Ce qu’elle ne couvre pas.** Les détails techniques de Tor (Partie II), les méthodes d’investigation (Partie V), les acteurs et espaces précis (Partie III).
> 
> **Ce que vous saurez faire après cette partie.** Répondre correctement à la question « qu’est-ce que le dark web ? », expliquer pourquoi il existe et à qui il sert, et présenter son écosystème à un non-spécialiste sans tomber dans les clichés médiatiques.

-----

### Chapitre 1 — Internet, web visible, deep web, dark web : remettre les mots à l’endroit

#### 1.1 Internet n’est pas le web

La confusion commence ici. **Internet** est le réseau physique mondial — un ensemble de câbles sous-marins, de fibres optiques, de routeurs, de satellites, et de protocoles (principalement TCP/IP) qui relient des milliards de machines à travers la planète. Internet transporte beaucoup plus que le web : email (SMTP, IMAP), streaming vidéo (RTP, HLS), trafic VPN (IPsec, WireGuard), requêtes DNS, pair-à-pair (BitTorrent), voix sur IP, jeux en ligne, protocoles industriels, trafic de mise à jour automatique.

Le **web** (World Wide Web) est un **service** qui fonctionne sur Internet, basé sur le protocole HTTP/HTTPS et des standards de présentation (HTML, CSS, JavaScript). C’est ce qu’on consulte avec un navigateur. Le web est une couche applicative parmi d’autres — une partie importante d’Internet, certes, mais pas la totalité.

Confondre Internet et web, c’est confondre le réseau routier et les magasins qu’on peut atteindre en voiture. Cette précision est importante parce que **les darknets sont des réseaux overlay** — ils fonctionnent sur Internet, en utilisant son infrastructure physique, mais construisent au-dessus une couche logique séparée avec des propriétés différentes (anonymat, routage alternatif). Comprendre cette distinction empêche de confondre le transport (TCP/IP classique) et la couche logique d’anonymisation.

#### 1.2 Les trois couches du web

Dans le langage courant, on distingue trois couches — simplification utile même si les frontières sont poreuses.

**Surface web (clearnet)**. L’ensemble des pages indexées par les moteurs de recherche généralistes (Google, Bing, Yandex, DuckDuckGo, Baidu). En volume, le surface web représente environ 5 à 10% du contenu web total — estimation stable depuis une décennie malgré la croissance du web en valeur absolue. Tout site accessible par une URL classique (`https://example.com`) et dont les pages apparaissent dans les résultats Google fait partie du surface web.

**Deep web**. L’ensemble des contenus web **non indexés** par les moteurs de recherche généralistes. C’est la couche **la plus vaste et la plus banale** : intranets d’entreprise, bases de données académiques, contenu derrière authentification (compte bancaire, messagerie, réseaux sociaux privés, factures de services publics), archives techniques non indexées, pages dynamiques générées à la demande. Le deep web représente environ **90% du contenu web** en volume.

**La quasi-totalité du deep web est parfaitement légale et banale**. Quand on parle du deep web, on ne parle **pas** de cybercriminalité — on parle de tout ce que Google ne voit pas, pour des raisons techniques (robots.txt, authentification requise) ou de design (bases de données consultables uniquement via un formulaire). Votre boîte mail Gmail est du deep web. L’intranet de votre employeur est du deep web. La base de données d’un laboratoire universitaire est du deep web. Cette banalité est structurante — elle rappelle que l’absence d’indexation n’a rien de sinistre.

**Dark web**. Sous-ensemble du deep web accessible **uniquement via des réseaux d’anonymisation spécifiques** — principalement Tor (sites `.onion`), accessoirement I2P (eepsites), Freenet, Lokinet, ZeroNet, et quelques autres darknets plus confidentiels. Le dark web n’est pas simplement « non indexé » — il est **volontairement caché**, hébergé sur des infrastructures d’anonymisation qui masquent à la fois l’identité du serveur (son IP) et du visiteur (son IP). En volume, le dark web est une fraction **minuscule** d’Internet : quelques centaines de milliers de domaines .onion observés par le Tor Project, dont la majorité sont inactifs, abandonnés, dupliqués, ou artefacts de tests.

#### 1.3 Darknets vs dark web : une distinction technique utile

Un **darknet** est un réseau **overlay** (superposé à Internet) conçu pour l’anonymat. Tor est un darknet. I2P est un darknet. Freenet est un darknet. Chacun implémente un modèle d’anonymisation différent (onion routing, garlic routing, freenet caching) avec ses propres propriétés.

Le **dark web** est l’ensemble des **contenus accessibles via ces darknets**. La distinction est importante : on peut utiliser le darknet Tor **sans visiter de site .onion** — par exemple, en utilisant Tor uniquement comme proxy pour naviguer de manière anonyme sur le web classique. Et on ne peut visiter un site .onion **qu’en passant par le réseau Tor**.

En pratique, l’analyste manipule les deux termes. « Investiguer sur le dark web » signifie explorer les contenus hébergés sur les darknets. « Utiliser le darknet Tor » signifie exploiter l’infrastructure d’anonymisation, qu’on aille sur un .onion ou sur le clearnet via Tor.

#### 1.4 Pourquoi le terme « dark web » est souvent mal utilisé

Les médias utilisent « dark web » comme synonyme de « cybercriminalité » — raccourci compréhensible, mais analytiquement dommageable pour trois raisons.

**Il surestime le dark web comme espace criminel**. Beaucoup d’activité cybercriminelle se déroule sur le **clear web** (forums à accès restreint, marketplaces à ciel ouvert dans certaines juridictions, plateformes de communication grand public). Telegram, Discord, Signal, pastebins publics, forums publics, GitHub — tous hébergent des activités illicites sans être du dark web. Genesis Market et RaidForums, deux plateformes criminelles majeures, opéraient sur le web de surface. Inversement, beaucoup de sites .onion sont parfaitement légaux.

**Il sous-estime les usages légitimes du dark web**. Contournement de censure dans les régimes autoritaires, protection des sources journalistiques, communication sécurisée pour lanceurs d’alerte, recherche en cybersécurité, protection de la vie privée — ce sont des usages essentiels et pleinement légaux. Des institutions parfaitement légitimes (BBC, New York Times, Deutsche Welle, Facebook, ProPublica, Amnesty International) maintiennent des miroirs .onion officiels.

**Il crée une fascination sensationnaliste** qui obscurcit la réalité opérationnelle. Le dark web, en vrai, est souvent **lent** (latence de plusieurs secondes par clic), **fréquemment en panne** (les .onion disparaissent, les marchés tombent, les forums exit-scament), **rempli d’arnaques** (un post sur trois est une tentative de scam), et **plus petit qu’on ne le croit**. Ce n’est pas un bazar secret infini — c’est un espace opérationnel limité, où les vrais acteurs compétents se connaissent, où la confiance est rare et chère, et où le folklore médiatique sur les « services de tueurs à gages » est quasi entièrement fictif (les rares sites qui proposent cela sont des scams).

#### 1.5 Ordres de grandeur

Les mesures publiques du Tor Project (metrics.torproject.org) donnent les ordres de grandeur suivants pour 2025-2026. Le nombre d’adresses .onion v3 uniques observées par les relais directory oscille autour de **800 000**, avec une variation quotidienne importante. Parmi ces adresses, seule une fraction est **active** à un instant donné — les estimations convergent sur 10 à 30% de sites répondant aux requêtes. Parmi les sites actifs, environ 50 à 60% sont des **usages légitimes, miroirs, ou services abandonnés**, 20 à 30% sont des **arnaques** (fausses marketplaces, faux services), et 10 à 20% hébergent du **contenu illicite réel** (forums criminels, marchés actifs, leak sites ransomware, CSAM — qui fait l’objet d’une lutte prioritaire des forces de l’ordre).

Côté usage : le Tor Project rapporte environ **2 à 3 millions d’utilisateurs quotidiens** du réseau Tor. Le Congressional Research Service estimait en 2015 qu’environ **3,4% seulement** des utilisateurs Tor visitaient des hidden services — la **grande majorité** utilise Tor pour naviguer sur le web classique de manière anonyme (résistance à la surveillance, contournement de censure).

Ces chiffres importent : le dark web est un espace **modeste** comparé au web classique. Une investigation dark web n’est pas une exploration d’un océan infini — c’est un travail ciblé dans un écosystème connaissable, dont on peut cartographier les principaux acteurs en quelques semaines de travail méthodique.

#### 1.6 Fil rouge — DARKSTREAM : le point de départ

> **🌐 DARKSTREAM — Épisode 1 : le mandat**
> 
> Lucas reçoit le brief de Vectris Aerospace le lundi matin. Réunion de cadrage en visio avec le RSSI de Vectris, la DGSI (deux interlocuteurs), et le directeur d’Athéna Group. Le RSSI présente les faits : exfiltration détectée il y a 11 jours, investigation IR en cours avec un prestataire PRIS (Mandiant), signal faible sur le dark web via Recorded Future.
> 
> La DGSI précise le cadre : coopération ouverte avec Athéna, remontée bi-hebdomadaire des observations, **ne pas engager de contact direct avec le vendeur** sans concertation préalable, respect strict du périmètre légal de la collecte.
> 
> Le mandat d’Athéna est clair : **confirmer ou infirmer** la circulation des données sur le dark web, **authentifier** les données si elles circulent, **cartographier** l’écosystème du vendeur et des acheteurs potentiels, **produire** un rapport actionnable pour la cellule de crise Vectris et la DGSI.
> 
> Lucas commence par la première question : les alertes de monitoring dark web sont souvent des **faux positifs**. Avant de déclencher une investigation approfondie, il doit vérifier que la mention « Vectris » sur IndustrialLeaks est réelle, pertinente, et pas un artefact d’homonymie ou un scam opportuniste. Le Ch.2 contextualise le forum cible dans l’histoire des darknet markets ; le Ch.24 détaillera la méthode d’accès.

-----

### Chapitre 2 — Histoire et évolution des darknets

Comprendre le dark web contemporain nécessite de connaître son histoire. Les darknets ont une trajectoire de 25 ans, marquée par des ruptures technologiques, des figures emblématiques, et des grandes opérations de police qui ont reconfiguré l’écosystème à plusieurs reprises.

#### 2.1 Les origines : anonymat et recherche militaire (1990s)

L’histoire du dark web commence dans les années 1990 au **Naval Research Laboratory** (NRL) américain, où des chercheurs (notamment **Paul Syverson**, **Michael Reed**, **David Goldschlag**) développent le concept d’**onion routing** : un protocole où les communications sont chiffrées en couches successives, chaque nœud intermédiaire ne pouvant déchiffrer que la couche qui lui est destinée, révélant le saut suivant sans connaître ni l’origine ni la destination finale. L’objectif initial est la **protection des communications de renseignement** — permettre à des agents de communiquer sans que leur trafic puisse être identifié par un adversaire observant le réseau.

Paradoxe fondamental vite identifié : un réseau d’anonymat **ne fonctionne que si beaucoup de gens l’utilisent**. Si seuls les agents de renseignement américains utilisent l’onion routing, tout le trafic observé devient attribuable (« cette communication vient d’un agent américain »). L’anonymat requiert une **foule** — et la foule requiert des usages multiples, y compris civils.

En 2002, **Roger Dingledine** et **Nick Mathewson**, rejoints par Paul Syverson, lancent le **Tor Project** comme implémentation **open source** de l’onion routing. Le projet devient indépendant en 2006 sous la forme d’une organisation à but non lucratif, avec un financement mixte — initialement beaucoup du gouvernement américain (Naval Research Laboratory, Broadcasting Board of Governors, State Department DRL), puis progressivement diversifié (donations individuelles, Mozilla, DARPA, fondations). Cette structure de financement mixte est emblématique du paradoxe : le gouvernement américain finance un outil qui protège aussi les criminels (cible d’investigation FBI), parce qu’il protège surtout les usages légitimes qui justifient stratégiquement l’existence du réseau.

#### 2.2 L’ère Silk Road (2011-2013)

**Silk Road**, créé par **Ross Ulbricht** (alias « Dread Pirate Roberts ») en février 2011, est le premier darknet market généraliste significatif. L’idée : un e-commerce clandestin inspiré d’eBay, utilisant Tor pour l’anonymat et Bitcoin pour les paiements. Ulbricht articule une vision libertarienne — vendre n’importe quel produit entre adultes consentants sans intervention étatique.

Silk Road grandit rapidement. Au moment de sa saisie par le FBI en octobre 2013, la plateforme totalise plus de **1,2 million de transactions** avec plus de **150 000 acheteurs** et **4 000 vendeurs**. Dominé par les drogues (~70% des ventes), le catalogue inclut aussi documents contrefaits, services de hacking, armes (controversé, règles internes restrictives sur ce point), mais exclut explicitement CSAM et contrats de tueurs à gages (règles internes interdisant l’« harm against others »).

Ulbricht est arrêté le 1er octobre 2013 dans une bibliothèque publique de San Francisco, ordinateur portable ouvert sur son interface administrateur. Identifié via plusieurs **erreurs OPSEC** cumulatives : un post sur StackOverflow avec son vrai email rthomeumm sous le pseudonyme « frosty », un post sur un forum Bitcoin en avril 2011 sous le pseudonyme « altoid » promouvant Silk Road (alors tout nouveau), un serveur CAPTCHA qui a leaké l’IP du serveur Silk Road lors d’une requête mal configurée (point débattu — les défenseurs d’Ulbricht ont soutenu que cette découverte était une reconstruction *a posteriori* par le FBI, possiblement couvrant une méthode de collecte classifiée).

Ulbricht est condamné en mai 2015 à **double perpétuité sans possibilité de libération conditionnelle plus 40 ans**, peine considérée comme disproportionnée par de nombreux observateurs (aucun meurtre n’ayant été commis — les accusations de tentative de contrat sur des témoins ont été utilisées pendant le sentencing sans inculpation formelle). Grâce présidentielle obtenue en janvier 2025 sous l’administration Trump.

L’héritage Silk Road est ambivalent : démonstration que l’e-commerce clandestin à grande échelle est possible (inspiration pour des dizaines de successeurs), mais aussi démonstration des limites de l’OPSEC individuelle face à une enquête FBI déterminée.

#### 2.3 La professionnalisation (2014-2019)

Après Silk Road, les successeurs se professionnalisent. **Silk Road 2.0** est lancé en novembre 2013, saisi un an plus tard (novembre 2014, operation Onymous — opération coordonnée qui saisit aussi plusieurs dizaines d’autres marchés). **Evolution Market** devient leader en 2014-2015 avant un exit scam retentissant (mars 2015, ~12 millions de dollars envolés). **Agora**, **Abraxas**, **Dream Market** se succèdent.

**AlphaBay**, lancé en décembre 2014 par **Alexandre Cazes** (canadien basé en Thaïlande, alias « alpha02 »), devient le **plus grand darknet market de l’histoire**. Au moment de sa saisie, le Département de la Justice américain documente **plus de 250 000 listings de drogues et produits chimiques**, auxquels s’ajoutent **plus de 100 000 listings** pour faux documents, accès frauduleux, malwares, armes et services divers. AlphaBay mature significativement le modèle : multiple cryptomonnaies acceptées (Bitcoin, Monero, Ethereum), 2FA obligatoire, PGP, système d’escrow robuste, ratings élaborés.

**Operation Bayonet** (juillet 2017) est une double frappe coordonnée entre le FBI américain et la police néerlandaise. AlphaBay est saisi suite à une erreur OPSEC de Cazes (inclusion de son email personnel `pimp_alex_91@hotmail.com` dans l’en-tête d’un email de bienvenue automatique généré en 2014). Cazes est arrêté en Thaïlande le 5 juillet 2017. Il est retrouvé mort en cellule le 12 juillet 2017 — officiellement suicide, version contestée par sa famille.

Le coup génial de l’opération : la police néerlandaise avait pris le contrôle de **Hansa Market** quelques semaines avant la saisie d’AlphaBay. Quand AlphaBay tombe, les utilisateurs et vendeurs migrent en masse vers Hansa — qui est maintenant opéré par la police. Pendant **30 jours**, les autorités néerlandaises collectent les données (vraies adresses de livraison, IPs, communications, patterns de transactions) avant de saisir Hansa à son tour. Cette opération devient la référence moderne de l’**infiltration active** par les forces de l’ordre.

#### 2.4 Hydra et la domination russophone (2015-2022)

**Hydra Market** (ru-center : hydraruzxpnew4af.onion et successeurs) est un cas à part. Lancé en 2015 et exclusivement opéré en russe, Hydra devient le **leader absolu** de l’écosystème russophone. Le DOJ américain et les autorités allemandes indiquent, lors de la saisie d’avril 2022, qu’Hydra a reçu environ **5,2 milliards de dollars en cryptomonnaies depuis 2015** et représentait environ **80% des transactions crypto liées aux darknet markets en 2021**.

Deux particularités structurantes. **Exclusivement russophone** : barrière d’entrée linguistique qui l’a partiellement protégé des actions law enforcement occidentales et de l’infiltration par analystes étrangers. **Système de dead drops physiques** unique : contrairement aux marchés occidentaux qui utilisent la poste (avec les risques que cela implique), Hydra fonctionnait avec des *kladmen* — courriers qui cachaient physiquement les produits dans des endroits spécifiques (sous une pierre dans un parc, dans un interstice de mur), dont les coordonnées GPS étaient ensuite communiquées à l’acheteur. Modèle qui supprime l’interception postale mais crée un écosystème de travailleurs à bas salaire (les kladmen) avec une rotation élevée.

La saisie d’Hydra en avril 2022 par les autorités allemandes (Zentrale Kriminalinspektion, Bundeskriminalamt, avec soutien du FBI) a créé une **fragmentation** massive de l’écosystème russophone : plusieurs marchés successeurs (OMG!OMG!, Mega, BlackSprut, Kraken) se sont partagé le marché sans qu’un leader clair ne s’impose comme Hydra l’était. La fragmentation complique le monitoring (plus de plateformes à suivre) et augmente la méfiance (exit scams plus fréquents sur les nouveaux marchés).

#### 2.5 L’ère post-Hydra et les tendances 2024-2026

L’écosystème 2024-2026 présente plusieurs caractéristiques structurantes.

**Fragmentation des marchés généralistes**. Les marchés « tout-en-un » type AlphaBay cèdent la place à des marchés **spécialisés** : marchés de logs (Russian Market), marchés de fraude (BriansClub, WWH Club, anciens 2easy.gg), marchés de ransomware-as-a-service, marchés de services (CaaS). Cette spécialisation reflète la professionnalisation de la cybercriminalité organisée.

**Montée de Telegram comme concurrent**. Telegram est devenu, dans la période 2020-2024, un canal majeur de communication cybercriminelle. Plus accessible que Tor (pas besoin d’outils spéciaux), plus réactif (chats en temps réel), avec des canaux publics et privés. Les canaux Telegram cybercriminels comptent des centaines de milliers de membres cumulés. **Arrestation de Pavel Durov en France le 24 août 2024** — inculpation incluant complicité dans la diffusion de contenus illicites. Impact : Telegram a considérablement durci sa modération (suppression massive de canaux criminels, coopération accrue avec les autorités), conduisant à une migration **partielle** des acteurs vers d’autres plateformes (Session, Matrix sur Tor, retour partiel vers les forums .onion).

**Glissement du vecteur d’accès initial**. L’évolution majeure 2025-2026 documentée par SOCRadar, Flare, Recorded Future : les attaquants **achètent** des credentials valides sur le dark web via des **stealer logs** à prix dérisoire (dès 15 USD) plutôt que de développer des exploits sophistiqués. Le dark web est devenu le **supermarché de l’accès initial**. L’attaquant moderne n’exploite plus la sophistication technique mais la **commoditisation** : pour 15 USD il achète un log d’infostealer, pour 500-50 000 USD il achète un accès VPN corporate préqualifié auprès d’un IAB, et il n’a plus qu’à monétiser.

**Intégration massive de l’IA**. Deepfakes, génération de phishing, chatbots criminels, analyse assistée — l’IA a basculé d’outil émergent à commodité dans la cybercriminalité. Parallèlement, les défenseurs adoptent l’IA pour le monitoring, l’analyse linguistique, et la détection d’anomalies (Ch.39).

**Pression croissante des forces de l’ordre**. Opérations de démantèlement plus fréquentes et plus sophistiquées (LockBit/Cronos février 2024, Kidflix mars 2025, BreachForums multiple, Qakbot, Hive, ALPHV/BlackCat, Genesis Market). Les grands opérateurs RaaS perdent en moyenne **18 mois** d’existence opérationnelle avant démantèlement. La pression a des effets : le niveau de paranoia opérationnelle augmente, les infrastructures se fragmentent pour résilience, et certains opérateurs se « retirent » après un gain significatif.

#### 2.6 Chronologie synthétique des grandes dates

|Période       |Événement                               |Impact structurant              |
|--------------|----------------------------------------|--------------------------------|
|1995-2002     |Développement onion routing (NRL)       |Foundation technique            |
|2002          |Lancement Tor                           |Accessibilité publique          |
|2009          |Lancement Bitcoin                       |Couche financière du dark web   |
|2011          |Lancement Silk Road                     |Premier grand market généraliste|
|2013          |Saisie Silk Road, arrestation Ulbricht  |Premier shock LE majeur         |
|2014          |Lancement AlphaBay, saisie Silk Road 2.0|Professionnalisation            |
|2015          |Lancement Hydra (ru)                    |Émergence bloc russophone       |
|2017          |Operation Bayonet (AlphaBay + Hansa)    |Référence infiltration LE       |
|2018-2019     |Dream Market, Wall Street Market        |Succession post-AlphaBay        |
|2020-2022     |Ascension Telegram / CaaS               |Convergence dark web / clearnet |
|2022 (avril)  |Saisie Hydra                            |Fragmentation russophone        |
|2023          |Operation Cookie Monster (Genesis)      |Saisie marché de logs           |
|2024 (février)|Operation Cronos (LockBit)              |Disruption grand RaaS           |
|2024 (août)   |Arrestation Pavel Durov                 |Durcissement Telegram           |
|2025-2026     |Commoditisation accès, montée IA        |Paradigme contemporain          |

#### 2.7 Fil rouge — DARKSTREAM : le forum ciblé

> **🌐 DARKSTREAM — Épisode 2 : IndustrialLeaks dans son contexte**
> 
> Avant d’y accéder, Lucas documente le forum signalé. **IndustrialLeaks** est un forum .onion russophone créé fin 2022, dans le contexte post-Hydra. Il s’est positionné sur une niche : les **données industrielles** (pas le ransomware classique, pas les credentials bancaires) — documents techniques, spécifications, bases clients, données de supply chain industrielle.
> 
> Environ 3 000 membres enregistrés selon les rares rapports publics disponibles. Accès sur **vouching** (parrainage par un membre établi) ou paiement d’un droit d’entrée (0,005 BTC, ~250 USD au cours actuel). Le forum a changé d’adresse .onion **trois fois** en 18 mois — comportement classique face à la pression (soit d’attaques DDoS concurrentes, soit de tentatives d’infiltration). Un miroir I2P est maintenu, indice de maturité technique des opérateurs. La langue principale est le russe ; l’anglais est toléré mais réservé aux ventes grand format.
> 
> L’activité principale documentée : ventes de données d’entreprises industrielles (énergie, défense, aérospatial, chimie), occasionnellement services associés (accès persistant, exfiltration ciblée sur commande). Quelques posts de « dumps » publics pour établir la réputation de vendeurs cherchant à monter en crédibilité.
> 
> Pour Lucas, ce contexte suggère qu’**IndustrialLeaks est un forum sérieux plus qu’un bazar à scams** — ce qui augmente la probabilité que la mention Vectris soit réelle. Mais il reste prudent : même dans un forum sérieux, l’opportunisme scam est fréquent. La vérification d’authenticité (Ch.14, Ch.25) reste incontournable.

-----

### Chapitre 3 — Pourquoi le dark web existe

Le dark web n’est pas une accumulation fortuite d’infrastructures. Il existe parce qu’il répond à des besoins réels, et il persiste parce que ces besoins persistent. Ce chapitre articule les raisons légitimes, les usages détournés, et la tension fondamentale qui structure le débat public.

#### 3.1 L’anonymat comme besoin fondamental

**Résistance à la censure**. Dans les régimes autoritaires (République populaire de Chine, Iran, Russie depuis 2022, Biélorussie, Myanmar, Érythrée, Corée du Nord dans une certaine mesure, Turkménistan), l’accès à des contenus jugés subversifs par l’État est filtré, surveillé, parfois criminalisé. Tor permet, dans beaucoup de ces contextes, d’accéder à Wikipedia, à des médias indépendants (Voice of America, BBC Persian, Deutsche Welle), à des réseaux sociaux bloqués (Twitter/X bloqué en Chine, Facebook en Iran). **Reporters Sans Frontières** opère des miroirs .onion de médias dissidents. Le **Tor Project** développe des techniques dédiées (bridges, pluggable transports comme obfs4, meek, snowflake) pour contourner le Deep Packet Inspection des censeurs.

La mesure n’est pas théorique. Pendant les manifestations en Iran (2022-2023, mouvement Woman Life Freedom), l’usage de Tor a bondi. Après l’invasion russe de l’Ukraine (février 2022) et le durcissement du régime russe vis-à-vis des médias (blocage de Facebook, Twitter, de nombreux médias indépendants), les connexions russes à Tor ont augmenté. Ces périodes de pic confirment que Tor est un **outil opérationnel de résistance informationnelle**.

**Protection des sources journalistiques**. La protection des sources est un pilier de la liberté de la presse, reconnu dans les législations démocratiques (article 10 CEDH, jurisprudence Goodwin c. Royaume-Uni 1996, First Amendment américain, loi française sur la liberté de la presse). Le dark web offre des canaux techniques pour que les sources communiquent avec les journalistes sans risque d’identification.

**SecureDrop** (développée initialement par Aaron Swartz et James Dolan, maintenue par la Freedom of the Press Foundation) est la plateforme de référence. Déployée par : le New York Times, le Guardian, le Washington Post, Le Monde, Der Spiegel, ProPublica, The Intercept, la BBC, et des dizaines d’autres médias. L’affaire **Panama Papers** (2016) et l’affaire **LuxLeaks** (2014) n’auraient pas été techniquement possibles sans des canaux de transmission anonymes.

**AfriLeaks** pour les lanceurs d’alerte africains, **GlobaLeaks** comme plateforme open source généraliste, **Hermes Center** pour le soutien technique à ces déploiements — un écosystème s’est structuré autour de cet usage.

**Vie privée comme droit fondamental**. Article 8 de la CEDH (respect de la vie privée et familiale), article 12 de la Déclaration universelle des droits de l’homme, article 7 de la Charte des droits fondamentaux de l’UE. L’anonymat en ligne est un **instrument** de ces droits. Dans un contexte de surveillance massive (activités commerciales de profilage, surveillance étatique légale ou illégale, collecte par des États hostiles), l’anonymat permet des choix informationnels libres.

**Communications sensibles légitimes**. Défenseurs des droits humains en zones hostiles, avocats consultant des cas sensibles, médecins communiquant sur des patients en zones de conflit, chercheurs en sécurité testant des infrastructures, employés lanceurs d’alerte envers leur propre employeur. L’anonymat technique protège des usages légitimes qui, sans anonymat, seraient impossibles ou dangereux.

#### 3.2 L’anonymat comme facilitateur criminel

Le dark web offre aux acteurs malveillants un espace où :

- **L’identification est difficile** : l’IP source est masquée, les pseudonymes sont jetables, les artefacts de compilation et les conventions linguistiques peuvent être contrôlés.
- **Les transactions sont pseudonymes ou anonymes** : Bitcoin pseudonyme avec traçabilité croissante, Monero anonyme par construction.
- **L’infrastructure est résistante aux saisies** : un site .onion ne dépend d’aucun registre centralisé ; la saisie nécessite soit la compromission du serveur physique, soit l’identification de l’opérateur.

Les usages criminels documentés couvrent un spectre large : marchés de drogues (de loin le volume dominant historiquement, en baisse relative depuis 2020), données volées et credentials, armes (volume marginal, beaucoup de scams), documents contrefaits, services de hacking, CSAM (priorité 1 des forces de l’ordre), blanchiment, forums de fraude, infrastructures de communication pour cybercriminels sophistiqués.

La diversité de ces usages, du trafiquant solo au groupe ransomware étatique, montre que le dark web n’est **ni un repaire de super-criminels ni un simple outil de liberté** — l’anonymat est moralement neutre, c’est **l’usage** qui est qualifiable.

#### 3.3 La tension fondamentale et ses régulations

La tension n’a pas de résolution simple : **l’anonymat technique qui protège les dissidents protège aussi les criminels**. Supprimer Tor (si c’était techniquement faisable, ce qui est contesté) ne supprimerait pas le besoin d’anonymat des dissidents — il les priverait d’un outil essentiel. Surveiller massivement Tor (comme certaines juridictions autoritaires tentent de le faire) compromet structurellement les usages légitimes.

Les régulations contemporaines tentent de naviguer cette tension par plusieurs approches.

**Lutte ciblée contre les usages criminels spécifiques**. Approche occidentale dominante : ne pas interdire Tor, mais poursuivre les opérateurs de plateformes criminelles (Ulbricht, Cazes, Khoroshev/LockBitSupp), les utilisateurs de CSAM identifiables, les infrastructures de paiement du crime. Les investigations combinent OSINT, analyse blockchain, erreurs OPSEC, infiltration, coopération internationale.

**Régulation des cryptomonnaies**. Parce que l’anonymat financier est le **maillon faible** de la cybercriminalité (à un moment, l’argent doit être converti en fiat utilisable), les régulateurs durcissent les exchanges (KYC renforcé, déclaration de transactions, sanctions ciblées type Tornado Cash en août 2022). Voir Ch.8 et Ch.31.

**Coopération internationale**. Convention de Budapest sur la cybercriminalité (2001), élargie par un deuxième protocole additionnel en 2022 sur la coopération renforcée et la divulgation électronique de preuves. Europol, Interpol, J-CAT, FBI Legal Attaché en poste dans les ambassades. Un écosystème d’échanges de renseignement et de coordination d’opérations.

**Approches contestées dans les démocraties**. Certaines juridictions explorent des pistes qui posent des questions de libertés publiques : lois sur la « responsabilité des plateformes » (Royaume-Uni Online Safety Act, UE Digital Services Act), tentatives de contrer le chiffrement de bout en bout pour permettre l’accès des autorités (projets récurrents type EARN IT aux US, Chat Control en UE — encore débattu), extension des pouvoirs d’interception (projets de mise à jour des législations nationales). Ces approches divisent, parce qu’elles pèsent sur l’équilibre vie privée / sécurité publique.

**Approches criminelles dans les régimes autoritaires**. Blocage pur et simple de Tor (Chine, Iran périodiquement), criminalisation de son usage (Russie depuis 2021 sous certaines formes), surveillance agressive des utilisateurs identifiés. Ces approches s’alignent sur des objectifs de contrôle politique plus que de lutte contre la criminalité.

L’équilibre exact entre anonymat et responsabilité reste un débat politique et sociétal vivant, sans résolution consensuelle à l’horizon.

-----

### Chapitre 4 — Le dark web comme écosystème

Le dark web n’est pas une seule chose — c’est un **écosystème** composé d’acteurs aux rôles distincts, d’espaces aux fonctions différentes, et de mécanismes de circulation qui le font fonctionner. Ce chapitre pose le cadre que les parties suivantes approfondiront.

#### 4.1 Les types d’espaces

Six grandes catégories d’espaces dark web, détaillées en Partie III.

**Forums** (Ch.10) : espaces de discussion structurés autour de thèmes (fraude, hacking, drogues, données, géographie). Modérés, avec hiérarchie de membres (newbie, member, trusted, VIP, moderator, admin), système de réputation. XSS Forum, Exploit.in, BreachForums successive, IndustrialLeaks (fictif, inspiré de cas réels).

**Marchés (marketplaces)** (Ch.11) : plateformes d’e-commerce clandestin, avec listings, panier, escrow, ratings. AlphaBay historique, Abacus Market, BlackSprut (ru), Mega (ru), TorZon.

**Leak sites** (Ch.12) : vitrines publiques des groupes ransomware, où ils revendiquent les victimes et menacent de publier les données volées. LockBit, ALPHV/BlackCat, Black Basta, RansomHub, Play, Qilin — chacun avec son esthétique propre.

**Messageries et canaux** (Ch.13) : Telegram, Matrix via Tor, Session, Jabber/XMPP, Tox. Les messageries servent à la fois comme canaux opérationnels (négociations, coordination) et comme canaux de diffusion (canaux publics avec abonnés).

**Marchés spécialisés** : marchés de logs (Russian Market), marchés de fraude (Genesis historique, successeurs), marchés 0-day (Ch.17).

**Services** : infrastructure hosting bulletproof, blanchiment-as-a-service, cryptage-as-a-service, bot-as-a-service, phishing kits.

#### 4.2 Les types d’acteurs

**Opérateurs de plateformes** : développeurs et administrateurs des forums, marchés, leak sites. Économiquement, ils prélèvent des commissions (1-10% sur les transactions), des frais d’inscription, des frais de vendeur. Politiquement, ils arbitrent les conflits. Opérationnellement, ils gèrent la résilience technique.

**Vendeurs** : acteurs qui monétisent des produits ou services sur les marchés. Spécialisations multiples : drug vendors, carders, credential brokers, fullz vendors, weapon vendors, 0-day brokers, service providers.

**Acheteurs** : clients finaux ou intermédiaires. Profils variés — particuliers cherchant drogues ou documents, cybercriminels achetant des outils, fraudeurs achetant des données, opérateurs ransomware achetant des accès IAB.

**Initial Access Brokers (IAB)** : acteurs spécialisés dans la compromission initiale d’organisations et la vente des accès à d’autres acteurs (typiquement des opérateurs ransomware). Chaîne de valeur centrale de la cybercriminalité contemporaine.

**Affiliés RaaS** : opérateurs qui déploient un ransomware-as-a-service moyennant partage des gains avec le propriétaire du malware.

**Blanchisseurs** : spécialistes de la conversion crypto → fiat utilisable, typiquement 10-30% de commission sur le montant blanchi.

**Services transversaux** : hébergeurs bulletproof, développeurs de malware, opérateurs botnets, crypters, spammers.

**Analystes CTI, forces de l’ordre, journalistes** : observateurs, dans des postures légales variées (voir Partie V sur le cadre légal et Ch.30 sur l’infiltration policière).

#### 4.3 Les flux qui font fonctionner l’écosystème

**Flux d’information** : montée en crédibilité des vendeurs, annonces de produits/services, négociations, litiges. Support : forums, canaux dédiés aux marchés, messageries privées.

**Flux financier** : paiements via cryptomonnaies (Bitcoin historique mais en repli, Monero en hausse, quelques stablecoins type USDT), escrow sur les marchés, blanchiment aval. Ch.8 détaille les mécanismes.

**Flux de confiance** : réputation construite par l’historique transactionnel, vouching par membres établis, arbitrage en cas de litige. Sans ces mécanismes, l’économie ne fonctionnerait pas. Ch.19 détaille.

**Flux de données** : données volées circulent des breachers initiaux vers les courtiers, puis vers les acheteurs finaux. Chaîne typique : breach → vente exclusive à prix élevé → revente en baisse → diffusion gratuite tardive (Ch.14).

**Flux d’accès** : les IAB compromettent → vendent l’accès → l’acheteur déploie ransomware ou autre monétisation. Chaîne souvent constatée dans les investigations post-incident.

#### 4.4 La géographie linguistique et culturelle

L’écosystème dark web est structuré par **plusieurs blocs linguistiques** largement cloisonnés.

**Bloc russophone** : le plus large historiquement. Forums majeurs (XSS, Exploit.in, RAMP historique), marchés (Hydra historique, successeurs), opérateurs ransomware (LockBit, Conti, ALPHV). La ligne russophone inclut ex-URSS (Russie, Bélarus, Ukraine pré-2022, Kazakhstan, etc.). Règle opérationnelle tacite des groupes russophones : **ne pas cibler la CEI** (Communauté des États indépendants) — règle respectée en grande partie, traduite dans le code de certains ransomware (vérification de la langue du clavier, exclusion des locales russophones).

**Bloc anglophone** : historiquement dominant pour les marchés généralistes (Silk Road, AlphaBay, Dream), devenu plus discret post-grandes saisies. Forums anglophones majeurs (BreachForums multiple, RaidForums historique).

**Bloc chinois** : opère largement sur des plateformes spécifiques, avec forums et canaux accessibles aux sinophones. Moins documenté dans les analyses vendor occidentales, nécessite une expertise linguistique spécialisée.

**Bloc persophone et arabophone** : croissance notable depuis 2020, avec des forums et canaux dédiés, activités orientées fraude, credentials, et parfois opérations liées à des tensions géopolitiques régionales.

**Autres** : francophone (présence modeste, parfois sur forums anglophones), hispanophone (Amérique latine, forums cartels), portugaise (Brésil), turc, coréen.

Pour l’analyste, la **barrière linguistique** est structurante : un analyste non russophone a une visibilité très partielle sur l’écosystème russophone. Les équipes CTI matures recrutent des locuteurs natifs ou utilisent des partenariats (SentinelOne, Recorded Future, Kaspersky, Sekoia, Group-IB ont tous des équipes multilingues).

#### 4.5 Les évolutions structurantes 2020-2026

Plusieurs tendances transforment l’écosystème.

**Professionnalisation continue**. Les opérateurs sont devenus plus matures techniquement, OPSEC plus rigoureuse, modèles économiques plus articulés (RaaS, CaaS). L’amateurisme des années 2010 est en recul.

**Commoditisation de l’accès**. Les stealer logs et les IAB ont abaissé les barrières d’entrée. Un acteur peu sophistiqué peut désormais, avec quelques centaines de dollars, acquérir un accès à une entreprise et lancer une attaque.

**Convergence clearnet/darkweb**. Beaucoup d’activité qui aurait été sur Tor en 2015 est maintenant sur Telegram, Discord, certains forums clearnet à accès restreint. L’analyste doit donc couvrir un spectre plus large que le seul .onion.

**Pression réglementaire et policière**. Multiplication des opérations de démantèlement, sanctions ciblées (Tornado Cash, adresses OFAC), coopération internationale renforcée, durcissement du KYC sur les exchanges crypto. Impact : augmentation des coûts opérationnels, accélération de la rotation des plateformes, montée de la paranoïa.

**Intégration de l’IA**. Deepfakes, chatbots criminels, automatisation du phishing, assistance au développement de malware. L’IA abaisse encore les barrières pour les acteurs peu qualifiés, même si elle ne transforme pas un script kiddie en APT.

**Retour de balancier vers les .onion**. Après le durcissement de Telegram post-Durov, certains acteurs retournent vers les forums .onion historiques — meilleure résilience juridique, même si accès plus friction.

#### 4.6 Ce que l’analyste doit retenir

Trois principes opérationnels pour aborder le dark web.

**C’est un écosystème, pas un lieu**. On n’« entre pas dans le dark web » comme on entre dans un bâtiment — on observe un ensemble d’espaces distincts, chacun avec ses règles, sa langue, ses acteurs. L’investigation se déplace entre forums, marchés, messageries, leak sites selon les pistes.

**Les acteurs jouent des rôles spécialisés**. L’IAB ne fait pas de ransomware ; l’opérateur RaaS n’exfiltre pas ; le blanchisseur ne vole pas. Cette spécialisation structure les chaînes d’attaque et fournit les angles d’investigation.

**L’écosystème évolue vite**. Un forum qui dominait il y a 18 mois a pu exit-scammer, être saisi, ou migrer. Les statistiques de prix bougent, les pseudonymes changent, les plateformes tombent. La connaissance acquise doit être rafraîchie en continu — ce qui fait de la veille (Ch.27) un pilier de la pratique.

-----

## PARTIE II — INFRASTRUCTURES TECHNIQUES ET ANONYMAT

> **Ce que cette partie apprend.** Comprendre les infrastructures techniques qui rendent le dark web possible — architecture Tor, onion services v3, réseaux alternatifs (I2P, Freenet), cryptomonnaies et leur traçabilité, hébergement bulletproof. Comprendre aussi leurs limites — Tor n’est pas magique, Monero n’est pas absolu, un bulletproof host peut être saisi.
> 
> **Ce qu’elle ne couvre pas.** Les méthodes d’investigation exploitant ces infrastructures (Partie V et VI), les méthodes concrètes de dé-anonymisation (Ch.29), les techniques de configuration offensive (hors périmètre).
> 
> **Ce que vous saurez faire après cette partie.** Expliquer techniquement le fonctionnement de Tor à un collègue, évaluer la résistance d’un service .onion à une saisie, distinguer les propriétés d’anonymat de Bitcoin et Monero, identifier les points de faiblesse typiques d’une infrastructure criminelle.

-----

### Chapitre 5 — Architecture de Tor

Tor (The Onion Router) est le darknet dominant. Comprendre son architecture permet de comprendre ses propriétés, ses limites, et les angles d’attaque — défensifs ou offensifs — qui s’appliquent.

#### 5.1 Principe de l’onion routing

L’idée centrale de l’onion routing est **séparer la connaissance de l’origine et de la destination** entre plusieurs nœuds intermédiaires, de telle sorte qu’**aucun nœud seul** ne connaisse les deux extrémités de la communication.

Mécanisme : le client Tor construit un **circuit** à trois nœuds (guard, middle, exit) en négociant des clés de chiffrement successives. Chaque paquet envoyé est **chiffré trois fois**, dans des couches successives. Chaque nœud intermédiaire déchiffre **une couche** pour révéler le saut suivant, sans pouvoir déchiffrer les autres couches.

Concrètement, pour une requête du client Alice vers le site `example.com` :

1. Le client Tor d’Alice choisit trois nœuds : un **guard** (premier relais, connu du client), un **middle** (relais intermédiaire), un **exit** (relais de sortie qui parle au site final).
1. Alice chiffre sa requête en trois couches, dans l’ordre inverse du chemin : couche exit, couche middle, couche guard — chaque couche chiffrée avec la clé du nœud correspondant.
1. Le paquet transite : Alice → guard. Le guard déchiffre sa couche, voit l’adresse du middle mais pas la destination finale.
1. Guard → middle. Le middle déchiffre sa couche, voit l’adresse de l’exit mais ne connaît ni Alice (qui a parlé au guard) ni la destination finale.
1. Middle → exit. L’exit déchiffre sa couche, voit la requête en clair (si HTTP) et l’envoie vers example.com. L’exit connaît la destination mais ne connaît pas Alice.

Réponse : même mécanisme en sens inverse. Chaque nœud ne chiffre qu’une couche avec sa clé sur le retour.

**Propriété clé** : dans ce modèle, aucun nœud seul ne connaît à la fois l’identité de l’origine (Alice) et la destination (example.com). Un adversaire doit contrôler **à la fois le guard et l’exit** pour corréler. C’est toute la sécurité du système — et son talon d’Achille.

#### 5.2 Les types de relais

Le réseau Tor comprend environ **7 000 à 8 000 relais** actifs en 2025-2026, répartis géographiquement (concentration en Europe, US, Canada, quelques en Asie). Ils se classent en catégories.

**Guard relays** : premier nœud d’un circuit, choisi parmi un ensemble de relais stables et bien connectés. Un client Tor utilise le **même petit ensemble de guards** pendant plusieurs mois (rotation lente), pour limiter l’exposition à un attaquant qui compromettrait des guards aléatoirement (l’attaquant a plus de chances de tomber sur un mauvais guard avec rotation rapide).

**Middle relays** : relais intermédiaires, les plus nombreux. Rôle de relais pur, sans visibilité ni sur l’origine ni sur la destination.

**Exit relays** : relais qui parlent au monde extérieur. Les moins nombreux (risque juridique élevé — un abus commis via Tor sort par l’exit, dont l’opérateur peut recevoir des plaintes ou des requêtes légales). Environ 1 000 exits actifs. Certains exits ont des politiques restrictives (bloquent certains ports, certains protocoles).

**Directory authorities** : serveurs qui maintiennent la liste des relais (le « consensus »). Il y a **9 directory authorities** actuellement, opérées par des entités de confiance (universités, Tor Project, individus de long terme). Tous les clients Tor téléchargent périodiquement ce consensus pour choisir leurs circuits.

**Bridges** : relais **non publics** (absents du consensus public), accessibles uniquement à ceux qui en obtiennent l’adresse par des canaux spécifiques (site web du Tor Project, email, Telegram, Messenger). Usage : contourner la censure là où les relais publics sont bloqués.

**Pluggable transports** : techniques d’obfuscation du trafic Tor pour contourner le Deep Packet Inspection. **obfs4** (fait ressembler Tor à du trafic aléatoire), **meek** (fait ressembler Tor à du trafic vers un grand service cloud type Azure, AWS, Fastly — « domain fronting »), **snowflake** (utilise des volontaires côté client comme relais WebRTC).

#### 5.3 Construction d’un circuit — détail

Plus précisément, voici comment un client Tor construit un circuit (simplifié).

1. **Téléchargement du consensus** : le client télécharge la liste des relais et leurs clés publiques auprès d’un directory authority ou d’un cache.
1. **Sélection des relais** : le client choisit un guard (parmi ses guards persistants), un middle, un exit — selon des critères de stabilité, bande passante, géographie (pour éviter par exemple de choisir trois relais dans le même pays), et politiques d’exit.
1. **Handshake avec le guard** : le client établit une connexion TLS avec le guard et négocie une clé symétrique via un protocole d’échange de clés (actuellement NTor — Noise-based Tor handshake).
1. **Extension vers le middle** : le client envoie au guard une commande « extend » chiffrée, qui demande au guard de contacter le middle et de négocier une clé symétrique avec lui. Le client obtient ainsi une clé partagée avec le middle via le guard comme relais.
1. **Extension vers l’exit** : pareil, le client étend le circuit vers l’exit.

Le client dispose maintenant de trois clés symétriques, une avec chaque relais. Toute donnée envoyée sera chiffrée en trois couches.

1. **Envoi de données** : le client construit son paquet en trois couches chiffrées et l’envoie au guard. Le guard déchiffre sa couche, fait suivre au middle, etc.

La durée de vie d’un circuit est typiquement de **10 minutes**, après quoi un nouveau circuit est construit pour les nouvelles connexions. Les streams existants peuvent continuer sur l’ancien circuit.

#### 5.4 Attaques et limites

Tor fournit un anonymat **fort mais pas absolu**. Plusieurs classes d’attaques existent.

**Attaque par corrélation de trafic**. Si un adversaire contrôle (ou observe) à la fois le guard et l’exit d’un circuit, il peut corréler les flux entrants et sortants par leur timing et leur volume, et identifier l’origine et la destination. Cette attaque nécessite une observation globale ou la compromission massive de relais. Les grands services de renseignement (NSA, GCHQ) sont crédités de cette capacité dans certaines conditions.

**Attaques sur les bridges**. Les censeurs ciblent les bridges en enregistrant leur trafic ou en les bloquant par DPI. La course entre obfuscations (nouveaux pluggable transports) et détection est continue.

**Attaques sur le navigateur**. Les utilisateurs de Tor Browser sont parfois attaqués via des exploits navigateur (historiques : **NIT du FBI en 2015 contre Playpen**, plusieurs opérations documentées contre Freedom Hosting). Ces attaques exploitent des vulnérabilités du navigateur sous-jacent (Firefox modifié) pour faire exécuter du code chez l’utilisateur et révéler son IP réelle hors de Tor. Voir Ch.30.

**Attaques par fingerprinting**. Même si l’IP est masquée, l’ensemble du comportement d’un utilisateur (timing, patterns de clics, taille de fenêtre, fingerprint navigateur) peut contribuer à son identification. Tor Browser est conçu pour uniformiser autant que possible les fingerprints (même résolution, même user-agent, anti-canvas), mais la recherche académique montre que l’anonymat parfait est illusoire.

**Attaques sur le DNS**. Si une application autre que Tor Browser fait des requêtes DNS non-tunnelées, elle leak l’IP réelle. C’est pourquoi Tor Browser isole le DNS dans le circuit.

**Erreurs utilisateur**. Loggin avec un compte identifié, réutilisation de pseudonymes, corrélation temporelle par les actions — beaucoup de dé-anonymisations historiques viennent d’erreurs d’OPSEC plus que d’attaques cryptographiques (Ulbricht, Cazes, beaucoup d’administrateurs de Hansa ou Silk Road 2.0).

#### 5.5 Tor Browser et les bonnes pratiques

**Tor Browser** (basé sur Firefox ESR avec modifications majeures) est le client de référence. Il intègre Tor, configure les proxies correctement, active NoScript, définit des paramètres de confidentialité par défaut (pas de cookies tiers persistants, pas de WebRTC, canvas bloqué). Disponible pour Windows, macOS, Linux, Android (Android via Orbot + Firefox-based browser). iOS n’a pas de Tor Browser officiel (limitations App Store) mais Onion Browser est une alternative acceptable.

**Mode Safer / Safest** : Tor Browser offre trois niveaux de sécurité (Standard, Safer, Safest). Safest désactive JavaScript sur tous les sites — recommandé pour l’investigation dark web (beaucoup de sites illicites exploitent des vulnérabilités JS pour identifier les visiteurs, voir Ch.30).

**Tails** : distribution Linux live qui force tout le trafic à passer par Tor, ne laisse aucune trace sur la machine. Usage recommandé pour les analystes travaillant sur des cas sensibles, et pour les journalistes/sources (Edward Snowden l’utilisait). Pas d’amnésie parfaite — une compromission exploitée en live peut leaker des données.

**Whonix** : architecture en deux VM (Whonix-Gateway qui fait le routage Tor, Whonix-Workstation où tournent les applications). L’isolation renforce la sécurité : si la workstation est compromise, elle ne peut pas obtenir l’IP réelle (qui n’est connue que de la gateway).

#### 5.6 Fil rouge — DARKSTREAM : préparation technique

> **🌐 DARKSTREAM — Épisode 3 : setup**
> 
> Lucas prépare son environnement d’investigation. Protocole Athéna : **machine dédiée**, non reliée au réseau d’entreprise, allumée uniquement pour les sessions d’investigation. OS : Whonix, Gateway + Workstation dans VirtualBox, patchs à jour. Tor Browser en mode **Safest** (JavaScript désactivé par défaut). Outils : navigateur uniquement pour la première phase, pas de screenshot direct de la machine (passage par OCR d’une photo d’écran pour éviter les métadonnées).
> 
> Pseudonymes dédiés à l’investigation : jamais de réutilisation d’un pseudo personnel, jamais de référence à Athéna. Lucas prépare trois pseudonymes distincts, un par type de forum à explorer, avec des styles linguistiques légèrement différents. Pas de paiement depuis un compte personnel — budget alloué par Athéna via un wallet crypto dédié à l’investigation, financé depuis un exchange professionnel avec KYC Athéna (pas de KYC Lucas personnel).
> 
> Ch.22 détaillera le cadre légal qui encadre cette préparation, Ch.23 l’OPSEC complète.

-----

### Chapitre 6 — Onion services (hidden services)

Les sites `.onion` sont l’une des fonctionnalités les plus emblématiques de Tor. Ils permettent à un serveur d’être **anonyme lui-même** — pas seulement ses visiteurs. Le serveur n’expose pas son IP, et les visiteurs qui s’y connectent ne connaissent pas non plus son IP.

#### 6.1 Principe des hidden services

Un hidden service (aussi appelé **onion service**) est un service accessible uniquement via Tor, identifié par une adresse se terminant en `.onion`. L’adresse elle-même est dérivée cryptographiquement de la **clé publique** du service — elle n’est **pas résolue par DNS**.

**Architecture** :

- Le serveur hidden service choisit plusieurs relais Tor comme **introduction points** et leur annonce qu’il est disponible via eux.
- Le serveur publie cette information dans la **hidden service directory** (une table de hachage distribuée sur les relais).
- Quand un client veut se connecter, il recherche dans la directory l’adresse `.onion` du service, trouve ses introduction points, et négocie avec eux.
- Un **rendezvous point** (relais tiers) est établi où client et serveur se rencontrent.
- Les deux parties communiquent via ce rendezvous, chacune masquée par son propre circuit Tor.

Cette architecture implique **six hops** (trois côté client + trois côté serveur) pour la communication — ce qui explique la lenteur relative des sites .onion.

#### 6.2 Onion v3 : les adresses modernes

Les adresses .onion historiques (« v2 ») étaient des hashs tronqués de 16 caractères, par exemple `3g2upl4pq6kufc4m.onion`. Cette génération a été **dépréciée** en octobre 2021 pour cause de vulnérabilités cryptographiques.

Les **onion v3** (actives depuis 2017, seules supportées depuis 2021) sont des adresses de **56 caractères**, dérivées d’une clé Ed25519 (256 bits) plus quelques éléments. Exemple : `duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion` (DuckDuckGo).

Les propriétés des v3 :

- Sécurité cryptographique forte (résistant aux attaques actuellement connues).
- Authentification mutuelle par défaut.
- Possibilité de **onion services authentifiés** — seuls les clients connaissant une clé préalable peuvent se connecter.
- Meilleure résistance au « directory scraping » — il est plus difficile d’énumérer les .onion actifs qu’avec v2.

#### 6.3 Propriétés de sécurité

Un hidden service bien configuré offre plusieurs propriétés.

**Anonymat du serveur** : l’IP réelle du serveur n’est pas exposée aux clients. Même un attaquant qui compromet un client ne peut pas remonter à l’IP du serveur via des moyens cryptographiques simples.

**Authentification du serveur** : l’adresse `.onion` **est** la clé publique du service. Un man-in-the-middle est quasi impossible — si vous vous connectez à `xxxxxxx.onion`, vous êtes cryptographiquement certain de parler à celui qui détient la clé privée correspondante.

**Pas de dépendance aux autorités de certification** : contrairement à HTTPS qui dépend d’une PKI centralisée (autorités de certification), les hidden services n’ont pas ce point de centralisation.

**Résistance aux saisies** : l’infrastructure est globalement distribuée. Pour saisir un service, les autorités doivent identifier et saisir le serveur physique — ce qui nécessite de dé-anonymiser l’opérateur.

**Cependant, ces propriétés ne garantissent pas que le service soit inviolable**. L’histoire des saisies montre que la chaîne faible est souvent :

- L’**OPSEC de l’opérateur** (Ulbricht, Cazes identifiés par leurs erreurs personnelles).
- Les **vulnérabilités applicatives** du service (SQL injection, RCE) qui exposent l’IP via des misconfigurations.
- Les **leaks d’infrastructure** (serveurs DNS publics mal configurés, headers HTTP, fuites via iframes).
- L’**infiltration** (opérations de police sur des années, compromission des clés).

#### 6.4 Les services légitimes en .onion

Beaucoup d’organisations légitimes maintiennent des miroirs .onion pour servir les utilisateurs dans des contextes sensibles (censure, surveillance) ou simplement comme service additionnel.

- **DuckDuckGo** : `duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion`
- **BBC News** : miroir Tor pour servir les pays où la BBC est censurée.
- **New York Times** : miroir pour la protection des sources.
- **ProPublica** : miroir, un des premiers grands médias à en avoir créé un.
- **Facebook** : miroir .onion depuis 2014, notamment pour les utilisateurs en Chine et en Iran.
- **Protonmail** : miroir .onion pour l’accès à la messagerie chiffrée.
- **SecureDrop** : chaque déploiement SecureDrop est un onion service (NYT, Guardian, etc.).
- **Tor Project** lui-même : tous les services (site web, documentation, téléchargements) ont des miroirs .onion.
- **Amnesty International, Reporters Sans Frontières** : miroirs pour les régions sensibles.
- **Ahmia, Torch, Haystak** : moteurs de recherche .onion (indexation limitée de ressources publiques).

Ces miroirs légitimes constituent une part significative des sites actifs — contre-exemple direct au cliché « tout ce qui est .onion est criminel ».

#### 6.5 Les limites pratiques pour les opérateurs

Exploiter un hidden service n’est pas trivial. Plusieurs difficultés.

**Latence élevée** : six hops + chiffrement multiple = latence typique de 500 ms à plusieurs secondes par requête. Un site .onion interactif (forum, marché) est intrinsèquement lent. Les utilisateurs habitués au web clearnet le ressentent.

**DDoS**. Les hidden services sont notoirement vulnérables aux DDoS. Un attaquant peut saturer le service en générant du trafic via Tor (qui le masque) — la cible ne peut pas bloquer l’origine puisqu’elle ne la connaît pas. De nombreux grands forums ont été indisponibles des jours ou semaines suite à des DDoS concurrents. Des techniques de protection existent (proof-of-work, rate-limiting intelligent, Vanguards/onion-balance) mais restent imparfaites.

**Maintenance**. Maintenir un service .onion stable dans la durée est techniquement exigeant. Patching, monitoring, gestion des attaques, renouvellement d’infrastructure — beaucoup de services échouent par épuisement opérationnel des admins plus que par saisie.

**Référencement**. Les .onion ne sont pas indexés par Google. La découverte se fait par liste communautaires (Hidden Wiki historique, The Onion Link List), word-of-mouth, posts sur forums clearnet, moteurs de recherche .onion eux-mêmes (Ahmia, Haystak — indexation partielle).

#### 6.6 Vanity addresses et reconnaissance

Les adresses .onion sont dérivées cryptographiquement, mais il est possible de générer des **vanity addresses** (adresses contenant un préfixe choisi) en brute-forçant des clés jusqu’à trouver une qui donne le préfixe voulu.

Exemples historiques :

- `facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion` commence par `facebook`.
- `propub3r6espa33w.onion` (ProPublica v2 historique) commençait par `propub`.

Pour un préfixe court (4-6 caractères), c’est trivial ; pour un préfixe de 10+ caractères, cela demande des ressources GPU significatives. Générer `facebookwkhpilnemxj7` a mobilisé des ressources Facebook pour en faire une démonstration.

Cette pratique permet aux services légitimes de signaler leur authenticité par un préfixe reconnaissable, mais aussi aux scammers de créer des adresses qui ressemblent aux vrais services (typosquatting .onion — un faux AlphaBay avec un préfixe similaire à l’original).

L’investigateur vérifie toujours l’adresse complète avant de conclure à l’authenticité d’un service.

-----

### Chapitre 7 — I2P, Freenet et réseaux alternatifs

Tor n’est pas le seul darknet. Plusieurs réseaux alternatifs coexistent, avec des propriétés différentes. Pour un analyste CTI, leur connaissance est utile : certains acteurs migrent vers ces réseaux quand Tor devient trop surveillé ou quand ils cherchent des propriétés spécifiques.

#### 7.1 I2P (Invisible Internet Project)

**I2P** (invisibleinternet.net) est un darknet développé depuis 2003, conçu pour les communications peer-to-peer dans un réseau fermé (contrairement à Tor qui permet aussi de sortir vers l’Internet clearnet).

**Architecture — « garlic routing »** : variation de l’onion routing où plusieurs messages sont **regroupés en ail** (garlic) avant d’être chiffrés. Cette approche offre des propriétés d’obfuscation du trafic différentes.

**Tunnels unidirectionnels** : contrairement à Tor qui utilise des circuits bidirectionnels, I2P utilise des tunnels séparés pour l’entrée et la sortie. Un serveur a ses tunnels entrants, un client a ses tunnels sortants — cette séparation complique l’analyse de trafic.

**Distribution peer-to-peer** : I2P n’a pas de directory authorities centraux (contrairement aux 9 directory authorities Tor). Chaque nœud participe au routage. Cette décentralisation renforce la résilience mais complique le bootstrap.

**Terminologie propre** : les sites sur I2P s’appellent des **eepsites** et utilisent des adresses en `.i2p` (par exemple `stats.i2p`, `i2p-projekt.i2p`).

**Usages**. I2P est moins populaire que Tor — réseau plus petit (quelques dizaines de milliers de nœuds vs millions d’utilisateurs Tor), interface moins accessible, écosystème applicatif restreint. Les forums cybercriminels russophones maintiennent souvent un miroir I2P en plus de leur .onion, par résilience. Certains acteurs préfèrent I2P pour des communications ciblées où Tor est perçu comme trop surveillé (perception plutôt qu’évidence technique).

**Exemple concret** : IndustrialLeaks (le forum fictif de DARKSTREAM) mentionne un miroir I2P. C’est un pattern typique — un forum sérieux maintient deux points d’entrée indépendants pour résilience face aux saisies.

**Attaques et limites**. I2P a été moins étudié académiquement que Tor, et moins attaqué publiquement — mais les propriétés de sécurité sont similaires. La décentralisation peut être un faux confort : un adversaire qui participe en masse au réseau (sybil attack) peut potentiellement compromettre l’anonymat.

#### 7.2 Freenet / Hyphanet

**Freenet** (rebaptisé **Hyphanet** en 2023) est l’un des plus anciens darknets, lancé en 2000 par Ian Clarke. Modèle radicalement différent de Tor et I2P : **stockage distribué**.

**Principe** : les utilisateurs contribuent de l’espace disque local au réseau. Les contenus publiés sont **chiffrés et dispersés** sur les machines des utilisateurs, sans qu’aucune ne connaisse l’intégralité d’un contenu. Les contenus populaires sont automatiquement répliqués ; les contenus oubliés s’effacent.

**Propriétés** :

- **Résistance à la censure** : supprimer un contenu de Freenet est très difficile — il faudrait saisir toutes les machines qui en hébergent un fragment.
- **Déni plausible** : un utilisateur hébergeant des fragments chiffrés peut plausiblement ignorer ce qu’il héberge.
- **Usage principal** : publication de contenu (sites statiques, blogs, fichiers) plutôt que communication en temps réel.

**Opennet vs Darknet** : Freenet offre deux modes. **Opennet** : tout nœud peut rejoindre. **Darknet** (« friend-to-friend ») : vous n’êtes connecté qu’à des nœuds opérés par des personnes que vous connaissez — résilience maximale mais effet réseau limité.

**Usages criminels** : Freenet a historiquement été un canal de diffusion de CSAM, raison pour laquelle de nombreuses opérations de police l’ont visé. La capacité à poursuivre un utilisateur sur la seule présence de fragments chiffrés (sans preuve qu’il connaissait le contenu) a été discutée dans plusieurs juridictions.

**Population** : très modeste par rapport à Tor. Usage résiduel, plutôt activiste/libertaire que cybercriminel organisé.

#### 7.3 ZeroNet, Lokinet et autres

**ZeroNet** : réseau décentralisé basé sur Bitcoin (identité et signature via clés Bitcoin) et BitTorrent (hosting distribué). Usage modeste, quelques sites politiques, quelques activistes.

**Lokinet** : darknet associé à la cryptomonnaie Loki/Oxen, basé sur une architecture type onion routing mais incentivée par la crypto. Usage limité, écosystème jeune.

**Yggdrasil, cjdns** : réseaux expérimentaux de mesh networking, pas spécifiquement orientés anonymat mais parfois utilisés comme alternatives.

**GNUnet** : projet académique de longue date, très peu déployé en pratique.

**Matrix fédéré** : pas un darknet à proprement parler, mais Matrix (protocole de messagerie fédéré) est parfois utilisé sur Tor pour des communications chiffrées de groupe. Session (basé sur Oxen/Lokinet) est une messagerie qui a émergé.

#### 7.4 Pourquoi la multiplicité des darknets ?

Aucun darknet ne domine totalement. Les raisons de la coexistence :

- **Préférences techniques** : Tor pour latence modérée + grande communauté ; I2P pour architectures peer-to-peer ; Freenet pour publication résistante.
- **Segmentation communautaire** : certains acteurs préfèrent se concentrer là où ils sont connus.
- **Redondance** : les opérateurs sérieux maintiennent souvent deux ou trois points d’entrée (onion, i2p, éventuellement Tor v3 authenticated + i2p) pour survivre à une saisie.
- **Évolution défensive** : quand un darknet devient intensément surveillé (perception), une partie de la population migre.

Pour l’investigateur CTI, l’implication pratique : **toujours vérifier si un service cible a un miroir sur un autre darknet**. Un forum saisi sur Tor peut rester opérationnel sur I2P pendant des semaines avant que les autorités l’attrapent aussi. Un acteur privé peut continuer ses activités via I2P après que son .onion est compromis.

-----

### Chapitre 8 — Cryptomonnaies et anonymat financier

Les cryptomonnaies sont la couche **financière** du dark web. Sans elles, l’économie clandestine à l’échelle observée serait impossible. Mais les propriétés d’anonymat des cryptomonnaies sont largement mal comprises, y compris par leurs utilisateurs criminels — ce qui explique une part importante des identifications réussies.

#### 8.1 Bitcoin : pseudonymat, pas anonymat

Bitcoin (2009, Satoshi Nakamoto) est la cryptomonnaie historique. Propriété fondamentale souvent mécomprise : Bitcoin est **pseudonyme**, pas **anonyme**.

**Principe** : chaque transaction Bitcoin est enregistrée publiquement dans la blockchain. Tout le monde peut voir : quelle adresse a envoyé combien à quelle adresse, à quel moment. Les adresses sont des chaînes de caractères (par exemple `bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh`) sans lien apparent avec une identité réelle.

**Mais** : à un moment, une adresse Bitcoin doit être liée à une identité pour être utile — que ce soit via un exchange (qui fait du KYC), une merchant (qui a votre livraison), ou toute interaction qui relie l’adresse à un nom. Une fois ce lien établi, l’historique entier de l’adresse devient attribuable.

Cette propriété a structuré toutes les investigations crypto du dark web : les grandes saisies (Silk Road, AlphaBay, Hydra, multiples ransomware) ont reposé sur le traçage blockchain des flux financiers. **Les cryptocurrency tracing firms** (Chainalysis, TRM Labs, Elliptic, CipherTrace/Mastercard) ont construit un écosystème de renseignement blockchain qui est devenu un outil central de lutte contre la cybercriminalité (Ch.31).

#### 8.2 Le traçage Bitcoin en pratique

Plusieurs techniques de traçage sont systématiquement appliquées.

**Clusterisation** : regrouper les adresses qui appartiennent probablement à la même entité, en observant les patterns (adresses qui co-dépensent dans une même transaction sont probablement contrôlées par la même entité).

**Heuristiques de change** : identifier les adresses de change (monnaie rendue) lors d’une transaction pour suivre le portefeuille source.

**Labellisation** : des milliers d’adresses connues sont labellisées (adresses Silk Road historiques, adresses ransomware connues, adresses de grands exchanges type Binance, Coinbase). Les transactions qui touchent ces adresses labellisées donnent des points d’attribution.

**Suivi cross-chain** : les flux passent souvent par plusieurs blockchains (Bitcoin → Ethereum → stablecoin). Les outils modernes suivent ces chaînes.

**Corrélation on-chain / off-chain** : croisement avec données exchanges (requêtes légales pour identifier un compte), surveillance de forums (vendeurs postent parfois leur adresse de paiement), et autres sources.

L’efficacité a été démontrée par une série de cas emblématiques : saisie des fonds Colonial Pipeline (FBI récupère ~2,3 M USD en juin 2021), saisie Bitfinex (DOJ saisit ~3,6 Mrd USD en février 2022), multiples saisies Lazarus, démantèlement Chipmixer (mars 2023), etc.

#### 8.3 Monero : anonymat par construction

**Monero (XMR)** (2014, projet open source) est conçu dès l’origine pour l’anonymat. Trois mécanismes cryptographiques :

**Ring signatures** : chaque transaction inclut plusieurs inputs possibles, dont un seul est le vrai. Un observateur ne peut pas distinguer le véritable input. Par défaut, 16 inputs de décoi (“ring size 16” depuis 2022, renforcé par hard fork).

**Stealth addresses** : chaque transaction génère une adresse unique pour le destinataire, dérivée de sa clé publique. Impossible de lier plusieurs transactions reçues par un même destinataire.

**RingCT** (Ring Confidential Transactions) : les montants des transactions sont chiffrés. Un observateur ne voit pas combien a été transféré — seulement qu’une transaction valide a eu lieu.

**Propriétés** : anonymat par défaut, fungibilité (chaque Monero est interchangeable avec tout autre Monero — impossible de « marquer » une pièce comme suspecte). Monero est devenu la cryptomonnaie de choix pour beaucoup d’acteurs cybercriminels depuis 2019-2020.

**Mais pas infaillible**. La recherche académique et les praticiens ont documenté des **faiblesses** :

- Les **decoys** ne sont pas parfaitement aléatoires — des patterns de sélection peuvent être exploités statistiquement.
- Les anciennes transactions (avant 2017 notamment) étaient bien moins protégées et ont pu être analysées rétrospectivement.
- Des **vulnérabilités d’implémentation** ont été corrigées au fil des ans (problèmes de génération d’aléatoire, fuites dans les logs).
- Les flux **on-ramp / off-ramp** (conversion fiat → Monero, Monero → fiat) passent par des exchanges soumis au KYC, donnant des points d’attribution.
- Les **atomic swaps BTC↔XMR** permettent de convertir sans exchange, mais posent des défis logistiques.
- Certaines agences de renseignement (US, multiples) ont annoncé des **contrats** pour développer des capacités de traçage Monero — le statut exact de ces capacités n’est pas public.

L’état consensuel : Monero offre un anonymat **très fort mais pas absolu**. Traçable avec des moyens importants et des conditions particulières ; intraçable dans la pratique courante face à un adversaire standard.

#### 8.4 Stablecoins : le nouveau facilitateur

Depuis 2020-2021, les **stablecoins** (USDT Tether principalement, USDC dans une moindre mesure) sont devenus **un vecteur massif de transactions dark web**. Raisons :

- **Stabilité** : pas de volatilité (contrairement à Bitcoin qui peut varier de 20% en une semaine).
- **Liquidité** : facilement convertibles partout.
- **Blockchain TRON** : USDT sur TRON est dominant — frais très faibles (~1 cent par transaction), confirmations rapides (~3 secondes). TRON est devenu la blockchain dominante des flux illicites crypto en volume transactionnel.

**Mais** : les stablecoins ne sont **pas anonymes**. Chaque transaction est on-chain et visible. Les émetteurs (Tether pour USDT, Circle pour USDC) peuvent **geler** les adresses sur requête des autorités — Tether a gelé des centaines de millions de dollars d’adresses suspectes sur les années 2022-2024. USDC est encore plus coopérant avec les autorités américaines.

L’attrait des stablecoins pour le dark web est donc structurellement ambigu : plus facile que Bitcoin pour les transactions, plus surveillé que Monero. Beaucoup d’acteurs utilisent USDT comme monnaie d’échange opérationnelle (prix affichés, paiements rapides) mais convertissent en Monero pour le stockage à long terme.

#### 8.5 Les mixers et tumblers

Les **mixers** (ou tumblers) sont des services qui mélangent les fonds de plusieurs utilisateurs pour casser la traçabilité. Vous envoyez 1 BTC, le mixer reçoit aussi les BTC d’autres utilisateurs, et vous renvoie 1 BTC (moins une commission de 1-3%) depuis un pool partagé — théoriquement impossible à relier à votre adresse source.

**Services historiques et statut** :

- **Helix** (saisi en 2020, Larry Harmon condamné à 3 ans de prison).
- **Bitcoin Fog** (saisi en 2021, Roman Sterlingov condamné en 2024).
- **Chipmixer** (saisi en mars 2023 — le DOJ et EPRS estiment ~152 000 BTC blanchis soit ~2,73 Mrd EUR).
- **Tornado Cash** : mixer Ethereum, **sanctionné par l’OFAC en août 2022** — première sanction d’un smart contract dans l’histoire. Des développeurs ont été inculpés, y compris Alexey Pertsev (condamné aux Pays-Bas en mai 2024) et Roman Storm (procès aux US en 2024-2025).
- **Wasabi Wallet, Samourai Wallet** : wallets Bitcoin avec CoinJoin intégré. **Samourai saisi en avril 2024, fondateurs inculpés**. Wasabi continue mais avec restrictions accrues.

**Limites actuelles** : les mixers sont une cible prioritaire des forces de l’ordre et des régulateurs. Leur utilisation est devenue un **signal** — les exchanges KYC refusent souvent de créditer des fonds qui ont transité par un mixer connu. Pour un criminel moderne, utiliser un mixer peut être plus coûteux (frais, délais, déclassement du fund) que de convertir directement en Monero.

#### 8.6 L’off-ramp comme talon d’Achille

Le problème fondamental pour le criminel : **à un moment, il faut convertir la crypto en monnaie utilisable** (fiat pour des achats du quotidien, biens physiques, immobilier). Cette étape **off-ramp** est le talon d’Achille.

Plusieurs canaux, tous partiellement compromis :

- **Exchanges KYC** (Binance, Coinbase, Kraken, OKX) : conversion facile mais laisse des traces sous un nom réel. Soumis à GAFI Travel Rule, TRF, etc.
- **Exchanges non-KYC** (historiquement BTC-e, plus récemment quelques plateformes peu réglementées) : de plus en plus rares sous pression internationale.
- **P2P platforms** (LocalBitcoins historique, Paxful, Binance P2P) : permettent des échanges directs avec moins de KYC, mais volumes limités, risque de scam.
- **OTC desks clandestins** : traders informels, souvent basés dans des juridictions peu régulées (Russie, quelques zones d’Asie), commissions élevées (5-20%).
- **Cartes de débit crypto** : convertissent en fiat au point de vente, mais émetteurs majoritaires KYC.
- **Achats directs en crypto** : immobilier, luxe, voitures — dans les juridictions qui l’acceptent.
- **Nested exchanges** : exchanges qui ont un compte sur un exchange majeur et ré-sertent en interne. Plusieurs ont été sanctionnés par OFAC (Suex, Garantex, Bitzlato).

Les investigations crypto identifient souvent le criminel à l’off-ramp — même après plusieurs mixers, une fois que le fund atteint un exchange KYC, l’identité est obtenue par requête légale. Ch.31 détaille le traçage crypto en profondeur.

#### 8.7 Fil rouge — DARKSTREAM : préparation financière

> **🌐 DARKSTREAM — Épisode 4 : le wallet d’investigation**
> 
> Athéna alloue un budget opérationnel à Lucas pour son investigation DARKSTREAM. **3 000 USDT** sur un wallet dédié, financé depuis un exchange professionnel (KYC Athéna, pas Lucas). Usage prévu : paiement du droit d’entrée IndustrialLeaks (~0,005 BTC si requis), achats éventuels d’échantillons (sous coordination DGSI), pourboires occasionnels pour obtenir des informations de membres coopératifs.
> 
> Lucas note que le vendeur aero_source demande **65 000 USDT** pour les 420 Go. Athéna **n’a aucune intention d’acheter** — le cadre mandaté est investigation, pas acquisition. Mais le prix demandé est un signal : 65 000 USDT correspond à un dump « premium », ce qui suggère soit de vraies données de valeur, soit un scammer ambitieux.
> 
> Lucas prévoit d’utiliser les capacités de traçage blockchain de ses outils (Chainalysis, TRM Labs via l’abonnement Athéna) pour **surveiller** l’adresse BTC affichée par aero_source dans son post — capter les paiements éventuels et identifier les acheteurs. C’est un angle d’attribution précieux : même sans identifier aero_source, identifier **un** acheteur peut donner un point d’entrée investigatif.

-----

### Chapitre 9 — Hébergement, infrastructure et résilience

Les services illicites du dark web ne sont pas hébergés par magie. Un serveur physique existe quelque part, avec un opérateur, une facture d’hébergement, et une exposition juridique — même masqués par Tor. Comprendre les mécanismes d’hébergement permet de comprendre où sont les points de défaillance.

#### 9.1 Les choix d’hébergement d’un service .onion

L’opérateur d’un service .onion a plusieurs options.

**Hébergement classique dans un pays « coopératif »** : un VPS chez OVH, Hetzner, Digital Ocean, AWS. Facile, bon marché, mais **totalement exposé à une saisie** si l’opérateur est identifié. La plupart des grandes saisies de marchés dark web ont concerné des infrastructures hébergées dans des clouds classiques — Silk Road chez des hébergeurs américains et islandais, AlphaBay chez des hébergeurs lituaniens, etc.

**Bulletproof hosting** : hébergeurs situés dans des juridictions où la coopération avec les forces de l’ordre est limitée (historiquement Russie, quelques pays d’Europe de l’Est, certaines zones asiatiques), ou hébergeurs qui se spécialisent explicitement dans l’hébergement de contenus « contestés ». Prix 5 à 10 fois plus élevés qu’un hébergement classique, mais résistance accrue. Bulletproof **ne signifie pas invulnérable** — plusieurs grands bulletproof hosts ont été saisis (Atrivo/Intercage 2008, McColo 2008, Russian Business Network, Hostinger/Cyberbunker 2019).

**Auto-hébergement physique** : machine chez soi ou dans un local loué, connexion Internet standard, Tor masquant l’IP. Solution la plus résiliente juridiquement (pas de tiers coopératif à contacter pour les autorités) mais la plus risquée pour l’opérateur (saisie physique de son domicile s’il est identifié, pas de redondance).

**Hébergement distribué** : plusieurs serveurs miroirs dans plusieurs pays, avec load balancing. Augmente la résilience, mais chaque miroir est un point de compromission potentiel.

**Hybrides** : opérateurs sophistiqués combinent plusieurs approches. Un frontend bulletproof pour la face publique, un backend chez un hébergeur différent moins exposé, des backups chiffrés distribués.

#### 9.2 Les mécanismes de résilience typiques

Les grands services clandestins mettent en place plusieurs mécanismes pour survivre aux tentatives de saisie.

**Multiple onion addresses**. Un même service peut publier plusieurs adresses .onion (v3 le permet), avec load balancing via onion-balance. Si une adresse est compromise, les autres restent fonctionnelles.

**Rotation d’adresse**. Certains services changent d’adresse .onion périodiquement (tous les X mois) et communiquent la nouvelle aux utilisateurs via des canaux out-of-band (Telegram, XMPP, mailing list chiffrée). Complique le monitoring long terme mais cohérent avec une posture défensive.

**Multiple darknets**. Maintenir simultanément un .onion et un .i2p (ou Lokinet, ou Freenet) — si un darknet devient intenable, l’autre reste. IndustrialLeaks (fictif) illustre ce pattern.

**Infrastructure distribuée**. Frontend, backend, base de données, stockage de fichiers sur des machines séparées, dans des juridictions différentes. Saisir le frontend ne suffit pas ; il faut aussi identifier les autres composants.

**Clés hors ligne**. Les clés privées les plus critiques (signature des annonces, wallet principal) sont conservées hors ligne, sur des machines air-gapped. Une saisie du serveur public ne donne pas accès aux fonds principaux.

**Backups chiffrés**. Les données opérationnelles sont régulièrement sauvegardées chiffrées sur des infrastructures tierces (cloud storage avec chiffrement client-side, stockage distribué type IPFS). Permet de relancer le service même après saisie complète du serveur principal.

**Kill switches**. Certains opérateurs implémentent des kill switches qui effacent automatiquement les données en cas de signes de compromission (pas d’accès admin depuis X heures, tentative de boot sans la bonne clé). Destiné à limiter les preuves collectables lors d’une saisie.

#### 9.3 Les points d’attaque des forces de l’ordre

Face à cette résilience, les investigateurs visent les points de faiblesse structurels.

**Identification de l’opérateur**. La méthode la plus efficace historiquement. Une fois l’opérateur identifié, son domicile/bureau peut être perquisitionné, ses infrastructures connues saisies simultanément, et ses clés capturées avant qu’il ne puisse les détruire. Ulbricht capturé ordinateur ouvert, Cazes de même en Thaïlande.

**Vulnérabilités applicatives du service**. Une SQL injection, une RCE, une mauvaise configuration CORS peuvent exposer l’IP réelle du serveur. Les services matures font tester régulièrement leur propre sécurité ; les services amateurs sont souvent identifiables ainsi.

**Fuites d’infrastructure**. Headers HTTP qui révèlent le vrai IP, certificats TLS utilisés à la fois sur clearnet et onion, iframes vers des ressources externes qui font un DNS lookup hors Tor, misconfigurations NTP. Le Tor Project publie régulièrement des recommandations pour éviter ces fuites, mais toutes ne sont pas suivies.

**Analyse de trafic**. Pour un adversaire qui peut observer le trafic entrant/sortant d’un hébergeur suspect, corréler avec les patterns d’activité du service .onion peut permettre d’identifier le serveur. Technique coûteuse, mais documentée dans plusieurs investigations.

**Infiltration**. Opérer le service depuis l’intérieur après saisie (Hansa model) ou infiltrer des comptes admin via social engineering, compromission de machines d’opérateurs, ou pivoting via des services tiers qu’ils utilisent.

**Coopération de l’hébergeur**. Pour les services hébergés chez des clouds mainstream, une simple requête légale suffit à obtenir l’identité du client. C’est pourquoi les opérateurs sérieux n’utilisent pas ces hébergeurs — mais beaucoup d’amateurs le font, et les petits services tombent souvent ainsi.

#### 9.4 Le cas emblématique des bulletproof hosts

**Cyberbunker** (originellement Pays-Bas, puis Allemagne) : ancien bunker OTAN reconverti en bulletproof host à partir de 2013. Hébergeait des marchés dark web, des CSAM, des infrastructures criminelles. Saisi en septembre 2019 par la police allemande après une opération de surveillance de trois ans. Le fondateur et plusieurs associés condamnés en 2021. Cas souvent cité comme démonstration que même les bulletproof hosts finissent par tomber.

**Russian Business Network (RBN)** : actif dans les années 2000, St Pétersbourg. Hébergeait malware, phishing, botnets. Jamais saisi stricto sensu, mais progressivement neutralisé par pression sur ses opérateurs de paiement et upstream providers. Dissolution de facto vers 2009.

**Atrivo/Intercage** : US, fermé en 2008 suite à une campagne de denaming par les autres hébergeurs (« de-peering ») qui ont refusé de lui faire du transit.

**McColo** : US, fermé en 2008 de la même manière.

Ces cas illustrent un pattern : les bulletproof hosts finissent par être neutralisés, soit par saisie directe, soit par pression sur leur écosystème (upstream providers, moyens de paiement, banquiers). Durée de vie typique : 5 à 15 ans. Rarement plus.

#### 9.5 L’émergence des « underground ISPs »

Ces dernières années, certains acteurs ont tenté de construire des **infrastructures d’ISP entièrement sous contrôle** — leurs propres connexions Internet, leurs propres IPs, leur propre transit. L’idée : ne plus dépendre d’un hébergeur tiers saisissable, mais opérer comme un FAI miniature.

Cas observés avec profils divers : hébergeurs ayant leur propre AS (Autonomous System) BGP dans des juridictions permissives, liaisons satellite pour bypass des FAI nationaux, infrastructure mesh dans des zones sans contrôle étatique effectif. Reste marginal — exige des investissements importants et des compétences techniques avancées.

#### 9.6 Fil rouge — DARKSTREAM : l’infrastructure d’IndustrialLeaks

> **🌐 DARKSTREAM — Épisode 5 : analyse d’infrastructure**
> 
> Lucas documente ce qu’il peut apprendre de l’infrastructure d’IndustrialLeaks. Depuis le forum lui-même, peu d’indices techniques directs — les opérateurs ont suivi les bonnes pratiques OPSEC.
> 
> Mais plusieurs signaux indirects :
> 
> - **Trois changements d’adresse .onion** en 18 mois, toujours annoncés à l’avance sur un canal Telegram public associé au forum. Cohérent avec une posture défensive proactive (pas avec une saisie réussie — pas d’interruption longue observable).
> - **Miroir I2P fonctionnel**, avec la même base de données (posts synchronisés). Indique une architecture centralisée avec deux points d’accès plutôt que deux services indépendants.
> - **Disponibilité élevée** : le forum répond en ~800 ms la plupart du temps, quelques pannes de 2-4 heures observables dans les archives communautaires. Cohérent avec un hébergement sérieux, possiblement bulletproof.
> - **Règles internes publiées** : modération active, bannissements documentés, posts de warning aux scammers. Indique un opérateur impliqué, pas un dump-and-forget.
> 
> Hypothèse de travail : IndustrialLeaks est probablement hébergé sur un bulletproof host d’Europe de l’Est, avec une équipe de 2-5 opérateurs (un admin principal, des modérateurs russophones), et une infrastructure miroir I2P active. Son modèle économique : droits d’entrée (250 USD × 3 000 membres = ~750 000 USD si on suppose tous payants — irréaliste, plus réaliste quelques centaines de payants), commissions sur ventes (1-3% probablement), peut-être services premium.
> 
> Pour Lucas, les implications d’investigation : accès via vouching (privilégier pour la crédibilité de la persona d’investigation), attentes réalistes de durée de vie (1-3 ans avant rotation ou saisie), priorité à la capture d’indices d’authentification des données **avant** que le forum ne disparaisse.

-----

## PARTIE III — ÉCOSYSTÈMES DU DARK WEB : ESPACES, ACTEURS ET CULTURE

> **Ce que cette partie apprend.** Connaître concrètement les types d’espaces (forums, marchés, leak sites, messageries, marchés spécialisés) et les acteurs qui les peuplent. Comprendre leurs codes, leurs dynamiques, leurs économies. Maîtriser les objets d’investigation que rencontrera l’analyste.
> 
> **Ce qu’elle ne couvre pas.** L’économie clandestine dans son ensemble (Partie IV), les méthodes de collecte (Partie V), les mécanismes d’attribution (Partie VI).
> 
> **Ce que vous saurez faire après cette partie.** Reconnaître un forum sérieux d’un forum scam, lire un post de leak site ransomware avec discernement, comprendre ce qu’achètent vraiment les acheteurs sur Russian Market, et situer un vendeur de 0-day dans la chaîne d’attaque.

-----

### Chapitre 10 — Forums clandestins : culture, hiérarchie et codes

Les forums sont l’ossature sociale du dark web. Contrairement aux marchés qui sont des points de transaction et aux messageries qui sont des canaux éphémères, les forums sont des **espaces de communauté persistants** où se construisent les réputations, se partagent les connaissances, et se recrutent les collaborations.

#### 10.1 Typologie des forums

Les forums varient par leur **spécialité** et leur **langue**.

**Forums généralistes cybercriminels**. XSS Forum (ex-DamageLab, russophone, historique), Exploit.in (russophone), BreachForums (anglophone — succession de plusieurs instances après saisies, la plus récente opérée par ShinyHunters après l’arrestation de Pompompurin en 2023 puis de Baphomet en 2024). Ces forums couvrent un spectre large : vente de données, discussions sur le hacking, recherche de partenaires, ventes d’outils.

**Forums spécialisés par thématique**. Carding (BriansClub, WWH Club), fraude bancaire, ransomware, drogue (forums adjacents aux marchés), armes (très rares, majoritairement scams), CSAM (priorité 1 des forces de l’ordre).

**Forums géographiques**. Marchés régionaux — forums ukrainien, polonais, chinois, coréen, persophone, arabophone. Chaque bloc avec ses codes et ses acteurs.

**Forums de niche**. **IndustrialLeaks** (fictif, DARKSTREAM) est un exemple de ces forums nichés — spécialisation sur un segment (données industrielles) permet de concentrer une communauté de confiance plus étroite.

**Forums « respectables »** vs **forums low-end**. Les forums sérieux (XSS, Exploit) ont un KYC interne fort — vouching, tests techniques, réputation durable. Les forums low-end sont ouverts à tous, majoritairement peuplés de script kiddies et scammers.

#### 10.2 Hiérarchie de membres

Structure typique d’un forum sérieux.

**Newcomer / Noob** : membre nouvellement inscrit, peu ou pas de posts. Accès limité — consultation des zones publiques, pas d’accès aux zones premium, pas droit de poster dans certains canaux.

**Member** : membre établi, quelques mois d’ancienneté, posts réguliers. Accès élargi, peut répondre à des posts, commencer à construire une réputation.

**Trusted / Verified** : membre vérifié — soit par **vouching** (parrainage par un membre établi qui engage sa réputation), soit par des transactions réussies, soit par un test technique. Peut vendre, peut poster dans les zones premium.

**VIP / Senior** : membre de très long terme avec réputation solide. Souvent des acteurs impliqués dans les activités majeures (opérateurs ransomware, IAB de premier plan). Accès à toutes les zones, peut parrainer des newcomers.

**Moderator** : modérateurs nommés par les admins. Arbitrent les litiges, bannissent les comptes indésirables, surveillent l’activité. Leur identité réelle est souvent connue des admins uniquement.

**Admin** : opérateurs du forum. Peuvent voir tout, décider des règles, collecter les droits d’entrée et commissions.

**Lurkers** : lecteurs silencieux. Les forums sérieux les tolèrent avec réserve — un compte inactif pendant 6 mois peut être supprimé. Les acteurs défensifs (analystes CTI, forces de l’ordre) sont presque toujours des lurkers par défaut.

#### 10.3 Règles internes et modération

Les forums sérieux ont des règles publiées et appliquées. Variations selon les forums, mais constantes récurrentes.

**Interdictions typiques** :

- **Pédopornographie** : universellement interdite, même dans les forums criminels. Raison : attraction maximale des forces de l’ordre, destruction potentielle du forum.
- **Cibles sensibles** : dans les forums russophones, ciblage d’entités CEI souvent interdit par règle (protection politique implicite du Kremlin envers ces acteurs, en échange tacite d’un ciblage exclusif hors-CEI).
- **Dox personnels** : publication d’informations personnelles sur des membres, sauf dispute résolue par arbitrage.
- **Scam** : membre scammant un autre membre est bannissable — mais prouver le scam est toujours l’objet de débats.
- **Multi-accounts** : création de plusieurs comptes pour simuler la popularité (sock puppets).

**Sanctions** : warning avec perte temporaire de privilèges, bannissement temporaire (jours/semaines) ou définitif, bannissement étendu cross-forum parmi forums partenaires.

**Arbitrage** : en cas de litige commercial, un modérateur ou admin arbitre. Peut imposer un remboursement partiel, valider le scam, ou déclarer l’affaire non-résolue. Le pouvoir d’arbitrage est considérable — un admin corrompu ou compromis peut basculer le destin d’une dispute.

#### 10.4 Codes culturels et jargon

Chaque forum a ses codes. Certains se retrouvent largement dans l’écosystème.

**Salutations et conventions**. « Hi all », « Greetings », « Bro » selon le style. Les forums russophones utilisent **Привет** (privet), **Коллеги** (kollegi — « collègues »), **Уважаемые** (uvazhaemye — « estimés »). Les usages trahissent parfois l’origine : un anglophone qui écrit « Privet all » tente probablement de se faire passer pour russophone.

**Termes techniques**. **FUD** (Fully Undetected — se dit d’un malware indétectable par les AV), **stub**, **crypter**, **binder**, **loader**. **IAB** (Initial Access Broker), **RaaS**, **CaaS**. Les forums spécialisés ont un lexique dense ; maîtriser ce lexique est essentiel pour comprendre les posts et ne pas se trahir.

**Formats de post standardisés**. Vente de données : description du contenu, échantillon gratuit, méthode de paiement acceptée, méthode de contact (Jabber/XMPP, Telegram, TOX, messagerie du forum). Annonce IAB : pays, secteur, type d’accès (VPN, RDP, Citrix, Active Directory), niveau de privilèges (user, admin local, admin domaine), revenue annuel de la cible, prix demandé.

**Signature et PGP**. Membres sérieux signent leurs posts en PGP — garantit que le compte n’a pas été usurpé. Un vendeur établi change rarement sa clé PGP sur la durée. Une rotation de clé PGP est un signal de changement d’opérateur (rachat de compte, compromis).

#### 10.5 Économie des forums

Sources de revenus pour les opérateurs :

- **Droits d’entrée** : 50-500 USD typiquement. IndustrialLeaks demanderait 0,005 BTC (~250 USD). Barrière à l’entrée qui filtre les simples curieux.
- **Abonnements premium** : accès VIP, 100-1 000 USD/mois.
- **Commissions sur ventes** : 1-5% via l’escrow du forum.
- **Vente de services** : hosting pour membres, advertising, slots prioritaires.
- **Droits de vouching** : certains forums monétisent les droits de parrainage.

Un forum sérieux actif peut générer 50 000 à 500 000 USD/an pour ses opérateurs, parfois davantage.

#### 10.6 Cycle de vie typique

**Phase 1 — Lancement** : recrutement initial, 6-12 mois de réputation à construire.

**Phase 2 — Croissance** : traction, modération, résilience. Peut durer 2-5 ans.

**Phase 3 — Maturité** : forum reconnu dans son segment, communauté stable.

**Phase 4 — Rupture** : saisie (Hydra 2022, Genesis 2023, BreachForums multiple), exit scam, épuisement opérationnel, guerre interne, ou désertion vers concurrent.

**Phase 5 — Reconstitution** : successeurs émergent. RaidForums → BreachForums → BreachForums v2 illustre cette cyclicité.

Pour l’investigateur, le cycle implique : **un forum étudié aujourd’hui n’existera peut-être plus dans 6 mois**. La documentation et la capture préservent la trace ; l’expertise historique est un actif d’investigation durable.

#### 10.7 Fil rouge — DARKSTREAM : lecture d’IndustrialLeaks

> **🌐 DARKSTREAM — Épisode 6 : exploration initiale**
> 
> Après accès validé par vouching (Athéna a un membre partenaire dans un forum affilié qui a accepté de vouch une persona d’investigation, sous encadrement DGSI), Lucas explore IndustrialLeaks.
> 
> **Structure du forum** : 8 zones publiques + 3 zones premium. Les zones publiques couvrent annonces, ventes générales de données, recherche de partenaires, discussions techniques. Les zones premium (accessibles après paiement additionnel) couvrent « industrial espionage », « government access », « supply chain intrusion ».
> 
> **Activité récente** : ~30-40 nouveaux posts par semaine en zone publique, ~10 en zones premium. Rythme soutenu, pas un forum mort.
> 
> **Le post aero_source** : posté il y a 11 jours dans la zone « Data sales ». Titre : « EU aerospace supplier, 420GB, propulsion R&D, defense programs inside ». Corps du post : brève description, liste d’échantillons disponibles (5 fichiers), prix 65 000 USDT. Méthode de contact : XMPP (aero_source@xmpp.jp — serveur non-custodial classique).
> 
> **Profil aero_source** : compte créé il y a **8 mois**. 12 posts au total. 2 transactions confirmées précédemment (petits dumps, 5 000-15 000 USD). Pas de vouching publicly affiché. Pas de rating négatif.
> 
> Lucas note : profil **intermédiaire** — pas un scammer opportuniste (historique transactionnel), pas un vétéran majeur. Possiblement un acteur qui a gradé de petites ventes à un dump plus gros. Possiblement aussi un proxy pour un acteur plus sophistiqué qui ne veut pas utiliser son propre pseudo.
> 
> La première tâche est maintenant de **demander un échantillon** (via XMPP, avec une persona crédible). Avant cela, Lucas va continuer à cartographier : activités aero_source sur d’autres forums (Ch.26 pivoting), monitoring des posts d’aujourd’hui, observation du comportement conversationnel en zone commune.

-----

### Chapitre 11 — Marchés du dark web : histoire, fonctionnement, évolution

Les **marchés** (marketplaces) sont les plateformes d’e-commerce clandestin — la couche la plus visible et la plus médiatisée du dark web. Après Silk Road, plusieurs dizaines ont existé et disparu.

#### 11.1 Anatomie d’un marché

Un marché dark web typique présente une interface familière. Comparable à Amazon ou eBay dans son ergonomie, avec des différences structurantes.

**Catégories de produits** :

- Drogues (cannabis, cocaïne, MDMA, amphétamines, opioïdes, psychédéliques) — catégorie historique dominante.
- Digital goods : comptes, credentials, accès, exploits, malware, guides.
- Documents : faux permis, faux passeports, modèles de factures, templates.
- Services : hacking sur commande, DDoS, escrow, physical services (rares).
- Armes : présent sur certains marchés mais marginalement, majoritairement scam.
- Fraude : carding tools, dumps, fullz.

**Fonctionnalités** : listings avec photos, descriptions, stock, prix (multiple devises crypto) ; panier et checkout ; **escrow** ; dispute resolution ; ratings et reviews ; messagerie interne ; 2FA et PGP obligatoires sur les marchés sérieux.

**Accès** : adresse .onion communiquée via listes communautaires, forums affiliés. Inscription : email jetable, pseudonyme, création de compte. Authentification : login + password + 2FA PIN + parfois PGP challenge.

#### 11.2 Les grands marchés historiques et actuels

**Silk Road (2011-2013)** — pionnier, traité Ch.2.

**Silk Road 2.0 (2013-2014)** — successeur immédiat, saisi lors d’operation Onymous.

**Evolution Market (2014-2015)** — grand marché de son époque, exit scam retentissant en mars 2015 (~12 M USD).

**Agora (2013-2015)** — longévité notable, fermeture volontaire par ses opérateurs.

**AlphaBay (2014-2017)** — plus grand marché de l’histoire au moment de sa saisie (Ch.2).

**Hansa (2013-2017)** — « capté » par la police néerlandaise pendant 30 jours après la saisie d’AlphaBay.

**Dream Market (2013-2019)** — longue durée de vie, fermeture volontaire des opérateurs avril 2019.

**Wall Street Market (2016-2019)** — exit scam suivi d’arrestations allemandes.

**Empire Market (2018-2020)** — exit scam août 2020, ~30 M USD.

**Hydra (2015-2022)** — dominant russophone, traité Ch.2.

**Marchés actuels 2025-2026** (listes susceptibles d’évolution rapide) :

- **Abacus Market** : généraliste anglophone, actif depuis ~2022.
- **TorZon** : anglophone, en croissance 2023-2024.
- **MGM Grand / MGM Gold Market** : anglophone.
- **BlackSprut, OMG!OMG!, Mega, Kraken Market** : marchés russophones post-Hydra.
- **DarkDock, Vice City, Incognito** : statuts variables.

#### 11.3 Le modèle économique d’un marché

**Revenue** : commissions 2-5% sur transactions (parfois jusqu’à 10%) prélevées via l’escrow ; fees vendor (inscription 100-1 000 USD, fees mensuels, promotion payante) ; fees acheteur (dépôt minimum) ; advertising.

**Coûts** : hosting bulletproof (5 000-30 000 USD/mois selon scale), développement, modération, sécurité (audits, DDoS), marketing.

Un grand marché génère plusieurs millions à plusieurs dizaines de millions USD par an. Hydra à son apogée : estimations 5-10% du volume crypto transactionnel mondial lié aux darknet markets.

#### 11.4 La dynamique de l’exit scam

**Phase 1 — Build-up**. Les opérateurs construisent la confiance et font croître le volume d’escrow. Plus le volume est haut, plus la « prime de départ » est attrayante.

**Phase 2 — Signals**. Dégradation qualité — support moins réactif, disputes mal résolues, retards de déblocage. Certains vendeurs s’alarment sur les forums.

**Phase 3 — Retention**. Ralentissement des withdrawals — délais accrus, vérifications supplémentaires. Les fonds s’accumulent.

**Phase 4 — Disappearance**. Le marché devient inaccessible. Les opérateurs ont transféré les fonds et disparu.

**Phase 5 — Succession**. Parfois, des « rescue » se proposent de racheter la base. Rarement efficace — la confiance est cassée.

Exit scams majeurs : Evolution (~12 M USD, 2015), Empire (~30 M USD, 2020). La probabilité d’exit scam augmente quand le marché grandit, que les FdO pressent, que les opérateurs vieillissent. Règle pour acheteurs avertis : **ne pas laisser plus que nécessaire sur le marché**.

#### 11.5 Les marchés spécialisés 2024-2026

L’époque des grands marchés généralistes AlphaBay décline au profit de marchés **spécialisés**.

- **Marchés de logs** : Russian Market leader. Spécialisation totale sur les stealer logs (Ch.15). Croissance massive depuis 2023.
- **Marchés de fraude** : cartes bancaires, comptes bancaires, accès PayPal/Venmo, fullz. BriansClub, WWH Club, Joker’s Stash historique (saisi 2021).
- **Marchés de SaaS criminel** : RaaS, PhaaS, DDoS-aaS. Interface orientée services avec abonnements.
- **Marchés d’accès** : IAB sur leurs propres plateformes ou via forums. Annonces et négociations plutôt que catalogue.
- **Marchés de malware** : vente de malware spécifique, crypters, loaders. Souvent intégrés aux forums.

Cette spécialisation reflète la **professionnalisation** de la cybercriminalité : chaque segment a ses acteurs, ses codes, ses mécanismes de confiance.

#### 11.6 Investigation sur un marché : ce qu’on peut observer

Pour un analyste CTI, un marché offre plusieurs types d’observations utiles.

**Pricing intelligence** : prix observés donnent une grille pour évaluer les signals (Ch.14 sur les données, Ch.15 pour les stealer logs).

**Vendor profiling** : histoire d’un vendeur (ancienneté, transactions, ratings, spécialisations). Profils anciens avec beaucoup de transactions = acteurs établis, annonces plus susceptibles d’être authentiques.

**Victim signaling** : annonces mentionnant des cibles nommées (entreprises, secteurs, géographies) donnent des signaux pour le monitoring défensif.

**Trends** : évolution du volume de certains types de produits (hausse des ventes credentials cloud AWS depuis 2022 = signal industry-wide).

**Indicators** : adresses crypto observées comme paiements, pseudonymes vendeurs/acheteurs, infrastructures mentionnées.

**Limites** : tout ce qui est sur un marché n’est pas authentique. Scams, recyclages, agit-prop — l’analyste doit rester critique (Ch.32).

-----

### Chapitre 12 — Leak sites ransomware et vitrines de revendication

Les **leak sites** sont les vitrines publiques des groupes ransomware. C’est là que les groupes revendiquent les victimes, publient des échantillons de données volées, et menacent de publier l’intégralité si la rançon n’est pas payée. Depuis l’avènement du modèle « double extorsion » (chiffrement + menace de publication), les leak sites sont devenus un des objets d’investigation CTI les plus riches.

#### 12.1 Le modèle de la double extorsion

Historiquement, un ransomware chiffrait les données et demandait une rançon pour la clé de déchiffrement. La victime avait deux options : payer, ou restaurer depuis des backups. Si les backups existaient et étaient intacts, la victime pouvait refuser de payer.

Le modèle **double extorsion** (popularisé par Maze en 2019-2020) ajoute une couche. L’attaquant **exfiltre les données avant de les chiffrer**, puis menace de les publier publiquement si la rançon n’est pas payée — même si la victime a des backups et peut restaurer. L’intérêt criminel : augmente la pression (risque réputationnel, légal, contractuel de la publication), élargit le levier (même les victimes avec backups sont touchées).

Le **leak site** est l’outil de cette menace. Plateforme publique où le groupe **revendique** la victime (nom, secteur, pays), **publie des échantillons** de données volées (documents sensibles, financiers, RH), **affiche un countdown** jusqu’à publication intégrale, et **publie intégralement** si non-paiement.

L’effet psychologique est considérable. Une victime qui voit son nom publié sur un leak site majeur est dans une position extrêmement inconfortable — ses clients, partenaires, journalistes, autorités voient le post. La pression au paiement est forte.

#### 12.2 Anatomie d’un post de leak site

Un post typique contient :

- **Nom de la victime** : raison sociale, parfois logo.
- **Secteur d’activité** : aerospace, healthcare, manufacturing, etc.
- **Pays / région** : juridiction.
- **Taille** : chiffre d’affaires approximatif, nombre d’employés.
- **Description** : quelques paragraphes sur ce que le groupe a exfiltré, type de données, volumétrie.
- **Countdown** : temps restant avant publication intégrale (typiquement 1-4 semaines).
- **Échantillons** : 10-100 fichiers publiés comme preuve de compromission. Choisis pour maximiser l’impact réputationnel (docs financiers, contrats, emails de dirigeants, données RH).
- **Contact** : méthode pour initier la négociation (souvent un onion avec un chat ou un formulaire).

Certains leak sites permettent des **interactions** : vote de la communauté pour pousser à la publication, mise en vente des données à la pièce, achats « first-come first-served » pour les autres criminels intéressés.

#### 12.3 Les principaux groupes et leurs leak sites en 2024-2026

*Liste non exhaustive et évolutive — plusieurs groupes disparaissent ou rebrandent.*

**LockBit** — historiquement le plus prolifique. Leak site très actif, interface sombre, countdown flashy. **Operation Cronos (février 2024)** a saisi l’infrastructure, identifié Dmitry Khoroshev comme LockBitSupp, rendu publiques des clés de déchiffrement. LockBit a tenté un relaunch mais sa crédibilité est entamée.

**ALPHV / BlackCat** — malware sophistiqué écrit en Rust. Disparition en mars 2024 suite à ce qui semble être un exit scam post-paiement Change Healthcare (~22 M USD présumés).

**Cl0p** — spécialisé dans l’exploitation de vulnérabilités d’edge devices (MOVEit 2023, Fortra GoAnywhere, Oracle EBS 2025). Leak site moins visuel que LockBit mais attaques techniquement sophistiquées.

**Black Basta** — actif depuis 2022, ciblage enterprise. Leak data massives en 2024-2025.

**Play / PlayCrypt** — actif depuis 2022, ciblage varié.

**Akira** — émergent fin 2023, croissance rapide.

**RansomHub** — émergent mi-2024, semble absorber des affiliés d’ALPHV post-disparition.

**Qilin** — anglophone malgré son nom, actif.

**BianLian** — historiquement hybrid chiffrement + exfiltration, en 2023 s’est tourné vers extorsion seule (sans chiffrement).

**8Base, Hunters International, Inc Ransom, Dragonforce, Medusa** — autres groupes actifs à surveiller.

La scène change **mensuellement** — des groupes disparaissent, rebrandent, émergent. Les outils de monitoring (Ransomfeed, Ransomwatch) suivent ces évolutions en temps réel.

#### 12.4 La lecture analytique d’un leak site

Pour un analyste CTI, chaque revendication de leak site est une source de renseignement.

**Vérification de la compromission réelle**. Tous les posts ne correspondent pas à de vraies victimes.

- **True positives** : la victime confirme (rarement publiquement, souvent via comms privées).
- **False claims** : groupe re-publie des données d’un breach antérieur sous son nom (pattern récurrent), ou revendique une compromission inexistante pour gonfler sa réputation.
- **Doubles claims** : la même victime revendiquée par deux groupes (conflit d’affiliés, rachat d’accès).

**Signaux sur l’activité du groupe**. Volume de revendications par mois, secteurs ciblés, géographies, évolution du rythme. Un groupe qui passe de 5 à 50 revendications/mois signale une croissance significative ou un recrutement d’affiliés.

**Patterns de targeting**. Les secteurs / pays ciblés donnent des indications sur les priorités et les compétences du groupe. Un groupe avec beaucoup de santé US est différent d’un groupe avec beaucoup de manufacturing EU.

**TTP implicites**. Les leak sites ne publient pas les TTPs (pour protéger leurs accès), mais des patterns peuvent se déduire — affinité pour certaines tailles de victimes, certains vecteurs d’entrée inférables par crosscheck avec cas connus.

**Indicateurs de disruption**. Un leak site qui disparaît brutalement, dont le countdown se fige, dont les affiliés migrent vers un concurrent — signaux d’une operation law enforcement en cours ou d’un conflit interne.

#### 12.5 Le monitoring automatisé

**Ransomfeed.it** (site public, gratuit) agrège les revendications de dizaines de leak sites en temps réel. Outils open source type **Ransomwatch** fournissent des archives.

**Vendors CTI** (Recorded Future, Mandiant, CrowdStrike, Flashpoint, SOCRadar, Flare) intègrent le monitoring dans leurs plateformes avec alerting sur marques, secteurs, géographies.

**Limites** : leak sites modernes implémentent protections anti-scraping (CAPTCHA, rate limiting, proof-of-work) ; leak sites « tiered » avec partie publique + partie accessible uniquement après interaction ; échantillons publiés pas toujours téléchargés / analysés.

#### 12.6 Le paiement de rançon : angle d’investigation

Les paiements de rançon, quand ils surviennent, laissent des traces **on-chain** exploitables.

**Mécanisme** : le groupe fournit une adresse Bitcoin / Monero / autre dans un portail de négociation. La victime paie. Les fonds transitent vers le groupe, puis sont blanchis (mixers, Monero swaps, OTC).

**Pour l’investigation** : si l’adresse est connue, le paiement confirme une compromission ; les mouvements on-chain peuvent révéler des connexions à d’autres opérations du même groupe ; les tentatives d’off-ramp peuvent révéler des identités si passage par exchange KYC.

**Saisies de paiements** : le FBI a récupéré des portions de rançons dans plusieurs cas emblématiques — Colonial Pipeline (~2,3 M USD récupérés en juin 2021), autres cas plus récents. Nécessite coopération internationale et vitesse d’exécution (avant blanchiment complet).

**Sanctions OFAC** : payer un groupe sanctionné (certains groupes sont sur listes OFAC) peut exposer l’organisation payeuse à des sanctions américaines. Considération réglementaire importante, qui pèse dans les décisions de paiement.

#### 12.7 Le débat sur le paiement

Question récurrente : faut-il payer une rançon ?

**Arguments contre le paiement** : finance l’activité criminelle ; ne garantit pas la non-publication (plusieurs cas de groupes publiant après paiement) ; ne garantit pas l’intégrité des données exfiltrées ; crée un précédent — organisation qui paie devient cible récurrente ; expose à sanctions (groupes OFAC).

**Arguments pour le paiement** : urgence opérationnelle (vie humaine en cause dans certains cas — hôpitaux) ; coût moindre que la perte business prolongée ; clé de déchiffrement peut accélérer la reprise.

**Positions officielles** : la plupart des agences nationales (FBI, ANSSI, NCSC) recommandent de **ne pas payer** comme principe, tout en acceptant pragmatiquement que la décision incombe à la victime.

**Les faits statistiques** (rapports Coveware, Chainalysis) : la proportion de victimes qui paient a **baissé** sur la décennie (de ~70% en 2018-2019 à ~25-30% en 2024). Le paiement moyen a augmenté (quelques millions de dollars par cas en moyenne sur les grandes victimes). La dynamique a changé : moins de payeurs, payeurs plus gros.

-----

### Chapitre 13 — Canaux, chats et messageries clandestines

Les **messageries et canaux** sont la couche temps réel du dark web. Là où forums et marchés sont persistants, les messageries sont éphémères — ce qui leur confère à la fois un intérêt opérationnel (communication rapide, pas de traces longues) et un défi investigatif (capturer les flux avant qu’ils disparaissent).

#### 13.1 Les plateformes dominantes

**Telegram**. Dominant dans la cybercriminalité 2020-2024. Facilité d’usage, canaux publics avec des milliers d’abonnés, canaux privés invitation-only, groupes de discussion, bots. Historiquement perçu comme plus tolérant que les alternatives — politique de modération limitée.

**Impact de l’arrestation de Pavel Durov (août 2024)**. Suite à l’interpellation en France, Telegram a durci significativement sa modération — suppression massive de canaux criminels, coopération accrue avec les autorités sur les requêtes légales. Résultat : **migration partielle** de certains acteurs vers d’autres plateformes (Session, Matrix sur Tor, XMPP, retour aux forums .onion), mais Telegram reste dominant en volume absolu.

**XMPP (Jabber)**. Historiquement central dans la cybercriminalité russophone. Chaque utilisateur un JID (jabber ID) type `username@domain.com`. Chiffrement de bout en bout via OMEMO ou OTR. Serveurs non-custodial (l’admin du serveur ne peut pas lire les messages chiffrés). Résilient — si un serveur tombe, l’utilisateur peut migrer en changeant de JID. Usage encore courant chez les acteurs sérieux.

**TOX**. Protocole peer-to-peer chiffré de bout en bout. Pas de serveur central, pas de registrations. Moins populaire que XMPP mais utilisé pour communications très sensibles.

**Matrix (+ Element)**. Protocole fédéré, chiffrement E2E, parfois opéré sur Tor via onion routing des homeservers. Adoption lente dans la cybercriminalité mais croissante post-Durov.

**Session**. Messagerie basée sur Oxen/Lokinet, conçue pour anonymat. Pas de numéro de téléphone requis (contrairement à Signal, WhatsApp), pas de metadata centrale. Usage croissant chez acteurs paranoïaques.

**Signal**. Messagerie chiffrée grand public. **Moins utilisée** par cybercriminalité sophistiquée car requiert numéro de téléphone, metadata potentiellement saisissables via Twilio, cible fréquente de requêtes légales. Utilisée par activistes et journalistes plutôt que cybercrime organisé.

**IRC historique**. Usage résiduel pour certaines communautés de niche.

**Discord**. Usage modeste en cybercrime sérieux (modération forte, liens avec identités réelles fréquents), mais présent pour les marchés jeunes/gaming.

#### 13.2 Les canaux Telegram cybercriminels

Les canaux Telegram publics cybercriminels peuvent être classés :

- **Canaux de leak** : publient des leaks gratuits (combo lists, databases publiées), souvent comme teasers pour des services payants. Des centaines de canaux, cumul de millions d’abonnés.
- **Canaux de CaaS** : phishing kits, DDoS, logs access. Interface commerciale, avec prix et méthodes de paiement.
- **Canaux de coordination** : groupes privés pour coordination opérationnelle entre membres d’une campagne. Typiquement invite-only.
- **Canaux d’hacktivisme** : revendiquent des attaques, publient des données volées dans un contexte idéologique (pro-russe, anti-israélien, etc.).
- **Canaux d’influence** : désinformation, amplification de narratifs, coordination d’opérations informationnelles.

#### 13.3 L’investigation des messageries

**Capture de canaux publics**. Telegram notamment permet d’archiver les messages de canaux publics avec des outils comme Telethon (bibliothèque Python). Les canaux privés nécessitent une invitation — soit obtenue légitimement via un contact, soit impossible à obtenir.

**Métadonnées**. Même les messageries chiffrées laissent des métadonnées (qui a parlé à qui, quand, volume). Sur Telegram, les numéros de téléphone des membres de groupes peuvent parfois être extraits selon les paramètres de confidentialité.

**Corrélation avec pseudonymes**. Un pseudonyme sur un forum .onion peut avoir un handle Telegram affiché dans les posts. Suivre ce handle sur Telegram permet d’élargir la collecte.

**Identification par patterns**. Analyse stylométrique (Ch.29), timing d’activité, patterns de langue — permettent parfois de corréler des comptes supposés distincts.

**Actions légales**. Les autorités peuvent, dans certaines juridictions, exiger la coopération des plateformes. Telegram post-Durov coopère plus activement avec les requêtes légales.

#### 13.4 Les limites investigatives

Les messageries sont plus difficiles à investiguer que les forums pour plusieurs raisons.

**Éphémérité**. Messages supprimés, canaux fermés, comptes bannis — la trace est vite perdue. Un analyste qui ne capture pas en temps réel perd l’information.

**Chiffrement**. Les messages chiffrés de bout en bout ne sont accessibles qu’aux participants — ni le serveur, ni les investigateurs ne peuvent les lire sans compromettre un endpoint.

**Volatilité des plateformes**. Un canal peut déménager ou disparaître du jour au lendemain. Maintenir le tracking nécessite de l’automatisation et de la réactivité.

**Faux comptes et sybil**. Les plateformes ouvertes permettent la création massive de faux comptes pour simuler l’activité, booster des narratifs, ou confondre les investigations.

#### 13.5 L’usage des messageries dans DARKSTREAM

> **🌐 DARKSTREAM — Épisode 7 : XMPP avec aero_source**
> 
> Lucas contacte aero_source via son XMPP affiché : `aero_source@xmpp.jp`. Serveur classique, non-custodial, fréquent dans la cybercriminalité russophone. Session chiffrée OTR négociée.
> 
> Premier message de Lucas (persona « mapletech », se présente comme acheteur potentiel d’une entreprise tech intéressée par des specs aéronautiques — légende crédible côté profil Athéna) : demande d’échantillons supplémentaires, vérification du volume réel, méthode de paiement préférée.
> 
> aero_source répond en 6 heures (cohérent avec un opérateur à temps plein sur fuseau horaire moscovite). Fournit 3 fichiers sample additionnels (1 spec technique de propulsion, 1 liste de fournisseurs, 1 extrait de notes de design). Confirme 420 Go total, paiement XMR préféré mais BTC accepté.
> 
> Lucas note : style de langue russophone anglicisé (« I have all the data, you see ? ») — cohérent avec profil russophone. Fuseau horaire des réponses (toutes entre 08:00 et 22:00 MSK) conforte. Pas de fautes de tournure inhabituelles — acteur probablement expérimenté, pas un débutant.
> 
> L’échantillon reçu sera analysé (Ch.25 — authentification). En parallèle, Lucas documente les métadonnées de la session : timestamps exacts, clé OTR négociée, serveur. Ces éléments pourront servir au rapport et au cross-matching avec d’autres pseudonymes.

-----

### Chapitre 14 — Données volées et marchés de la fuite

Les données volées sont l’un des produits les plus échangés sur le dark web. Credentials, identités, dossiers médicaux, données d’entreprise — chaque type a son marché, son prix, ses acheteurs.

#### 14.1 Types de données en circulation

**Credentials**. Couples email/mot de passe issus de breaches. Vendus en bulk (combo lists de millions d’entrées pour 5-50 USD) ou au détail (5-50 USD/pièce pour des credentials vérifiés sur services spécifiques).

**Logs d’infostealers**. Sessions complètes avec credentials, cookies, données machine — traités au Ch.15 en détail.

**Données bancaires**. Numéros de carte, CVV, accès aux comptes. Marché organisé (BriansClub, WWH Club, successeurs). Prix selon fraîcheur et pays.

**Données personnelles (fullz)**. Identité complète : nom, adresse, SSN/NIR, date de naissance, documents d’identité scannés. Utilisées pour fraude à l’identité, ouverture de comptes frauduleux.

**Données d’entreprise**. Documents internes, propriété intellectuelle, emails, bases clients. Les volumes exfiltrés par ransomware alimentent cette catégorie.

**Données de santé**. Dossiers médicaux, très prisés pour la fraude à l’assurance (US), le chantage, et la fraude à l’identité. Prix relativement élevés par unité (50-250 USD/dossier).

**Données gouvernementales**. Accès ou exfiltrations concernant administrations. Rareté élevée, prix variables selon sensibilité.

**Données industrielles / défense**. Spécifications techniques, plans, documents classifiés. Niche — DARKSTREAM s’inscrit dans cette catégorie. Acheteurs : concurrents industriels, services de renseignement étrangers, parfois groupes ransomware cherchant un levier de revente.

#### 14.2 Grille de prix indicative 2025-2026

Sources : rapports SOCRadar (Annual Dark Web Report 2025), Privacy Affairs (Dark Web Price Index), observations Recorded Future, Flare. **Fortement indicatif** — varie par fraîcheur, spécificité, vendeur, marché.

|Type de donnée                                  |Prix indicatif             |
|------------------------------------------------|---------------------------|
|Combo list (millions d’entrées, dates variables)|5-50 USD                   |
|Credentials vérifiés, service spécifique        |5-50 USD / pièce           |
|Carte bancaire avec CVV (compte actif)          |5-30 USD                   |
|Carte bancaire avec PIN / full access           |30-150 USD                 |
|Compte PayPal vérifié                           |20-200 USD selon balance   |
|Compte bancaire vérifié avec online banking     |100-1 000 USD selon balance|
|Fullz (identité complète)                       |10-70 USD                  |
|Passeport scanné                                |20-150 USD                 |
|Permis de conduire scanné                       |15-70 USD                  |
|Log d’infostealer basique                       |1-15 USD                   |
|Log d’infostealer avec VPN corporate            |50-500 USD                 |
|Accès VPN/RDP corporate (IAB)                   |500-50 000 USD             |
|Base de données d’entreprise                    |500-100 000 USD+           |
|Dossier médical US                              |50-250 USD                 |
|0-day exploit (selon plateforme)                |5 000 - 2 500 000 USD      |
|RaaS affiliation (droit d’affiliation)          |1 000 - 100 000 USD        |


> **⚠️ ALERTE ANALYSTE** : Ces prix sont des moyennes indicatives à date (2025-2026) et fluctuent selon la réputation du vendeur, la fraîcheur, la verification, et les dynamiques de marché. Les prix des données bancaires simples ont tendance à se stabiliser ou baisser (saturation) tandis que les credentials d’accès corporate et les stealer logs avec tokens de session augmentent (demande RaaS).

#### 14.3 Le lifecycle d’un breach

Les données volées suivent un cycle prévisible.

**Phase 1 — Exploitation privée**. Le groupe auteur du breach exploite d’abord les données pour son propre compte — ransomware, fraude, chantage de la victime. Durée : jours à mois.

**Phase 2 — Vente exclusive**. Les données sont mises en vente à prix élevé, avec clause d’exclusivité (pas de revente par le vendeur). Acheteurs : autres groupes cybercriminels cherchant un levier, concurrents industriels (rare et risqué), services de renseignement (cas politiques).

**Phase 3 — Revente large**. Si les données ne sont pas exclusivement vendues, ou si les termes d’exclusivité sont violés, revente à multiple acheteurs avec prix décroissant.

**Phase 4 — Publication publique / gratuite**. Après que la valeur commerciale a été extraite, les données sont souvent publiées gratuitement sur des canaux Telegram, pastebins, forums. Sert à construire la réputation d’un vendeur ou à publier sous couvert idéologique.

**Phase 5 — Intégration dans les bases publiques**. Have I Been Pwned, DeHashed, et autres services indexent les données pour vérification défensive. Les données deviennent **un asset défensif** — les DSI peuvent vérifier si leurs emails sont compromis.

La durée entre phase 1 et phase 5 varie considérablement — quelques semaines pour des petits breaches de moindre intérêt, plusieurs années pour des breaches majeurs gardés exclusifs longtemps.

#### 14.4 Vérification de l’authenticité

Les annonces de données volées sont **massivement polluées par des scams, des recyclages, et des fabrications**. La vérification d’authenticité est un skill central de l’analyste.

**Échantillons**. Un vendeur sérieux fournit des échantillons gratuits vérifiables — emails avec domaine cohérent, formats réalistes. Un vendeur refusant systématiquement tout échantillon est suspect.

**Fraîcheur**. Les données déjà vues dans des breaches publics (via HIBP, DeHashed) sont recyclées — pas un nouveau breach, valeur réduite.

**Spécificité**. Des données très spécifiques à une organisation (noms d’employés internes, codes produit internes, contrats signés) sont plus crédibles que des templates génériques.

**Corroboration externe**. La victime confirme-t-elle ? Un CERT ou prestataire IR est-il impliqué ? Des indices publics confirment-ils la compromission (notifications régulateurs, communiqué de presse) ?

**Cohérence interne**. Les formats, conventions, horodatages sont-ils cohérents ? Une base de données avec des inconsistances format (dates parfois US, parfois EU) signale potentiellement un assemblage factice.

**Échantillon ciblé**. Demander au vendeur un échantillon spécifique (par exemple, un fichier contenant un certain nom). S’il peut le produire, authenticité probable. S’il refuse ou produit quelque chose d’incohérent, probable scam.

Voir Annexe E pour une grille d’évaluation complète de crédibilité.

#### 14.5 La dimension sectorielle

Les données volées ne sont pas distribuées uniformément. Rapport Cyberint 2025 documente une concentration sur les secteurs à forte valeur : institutions financières (cartes, credentials bancaires, accès systèmes de trading), santé (dossiers médicaux, chantage, fraude assurance), télécommunications (SIM swapping, accès réseaux), gouvernement (données classifiées, identités fonctionnaires). Chaque secteur a son **modèle de monétisation** propre — détaillé au Ch.35.

#### 14.6 Fil rouge — DARKSTREAM : premiers échantillons

> **🌐 DARKSTREAM — Épisode 8 : analyse des échantillons**
> 
> Lucas reçoit 5 fichiers d’échantillons initiaux + 3 additionnels via XMPP. Protocole Athéna strict : fichiers ouverts **uniquement** dans une VM isolée (Whonix + Windows 10 jetable), jamais sur la machine de production. Scan antivirus préalable. Extraction des métadonnées avec exiftool.
> 
> **Fichier 1** — « Propulsion_specs_Rev7.pdf ». 14 pages, schémas techniques. Métadonnées internes : auteur « M. Dubois », entreprise « Vectris Aerospace », créé en Nov 2025, modifié en Dec 2025. Softare MS Word → PDF. Numéro de révision cohérent avec conventions Vectris.
> 
> **Fichier 2** — « Supplier_list_2025.xlsx ». 340 lignes de fournisseurs. Formatage Excel, adresses cohérentes (pays UE, US, Asie). Contient un fournisseur de test interne reconnu par le RSSI de Vectris (confidentiel — nom de fantaisie utilisé comme marker).
> 
> **Fichier 3** — extrait email. Export de boîte mail interne d’un ingénieur R&D. Discussions techniques, jamais publiées publiquement. Content cohérent avec un vol Office 365.
> 
> Les 3 échantillons additionnels : d’autres spécifications techniques, notes de réunion, extrait budgétaire.
> 
> **Verdict Lucas** : authenticité **confirmée** au niveau échantillon. Cohérence avec la compromission initiale identifiée par Mandiant chez Vectris. Le marker interne présent dans le fichier 2 est un signe fort que le dump provient bien de la compromission Vectris. Lucas escalade immédiatement à la cellule de crise Vectris et à la DGSI. Le post aero_source est authentique ; la compromission est confirmée ; l’exfiltration circule bien sur le dark web.
> 
> Question suivante : qui est aero_source ? Est-ce l’attaquant initial, un proxy, un courtier ? Prochaine étape : élargir le profiling via les autres activités du pseudonyme et via l’analyse des flux crypto associés.

-----

### Chapitre 15 — Stealer logs : anatomie, marchés, investigation défensive

*Ce chapitre traite en profondeur le vecteur de compromission initiale le plus courant en 2025-2026. Les stealer logs sont devenus la matière première de l’écosystème cybercriminel — l’équivalent du pétrole brut qui alimente toute la chaîne de valeur.*

#### 15.1 Qu’est-ce qu’un stealer log ?

Un **stealer log** est le produit de l’exécution d’un **infostealer** (malware spécialisé dans le vol de données de sessions) sur la machine d’une victime. Contrairement à un breach de base de données (qui produit des listes de credentials en masse), un stealer log capture **l’intégralité de l’environnement de la session utilisateur** sur un poste spécifique.

Un log typique contient :

- **Credentials du navigateur** : tous les logins/mots de passe enregistrés dans Chrome, Firefox, Edge, Brave, Opera — des dizaines voire des centaines de comptes par victime.
- **Cookies de session actifs** : permettent de se connecter à un service **sans mot de passe**, en contournant même le MFA. C’est **le vecteur le plus dangereux** de 2024-2026.
- **Données d’autofill** : noms, adresses, téléphones, données de cartes bancaires stockées.
- **Wallets crypto** : clés privées ou seed phrases stockées dans des extensions navigateur (MetaMask, Phantom, Exodus).
- **Données machine** : hostname, IP, OS, logiciels installés, capture d’écran au moment de l’exécution.
- **Sessions de messagerie** : tokens Discord, Telegram Desktop, WhatsApp Desktop.
- **Données Steam, Epic Games** : sessions gaming, de plus en plus ciblées.
- **Fichiers sélectifs** : certains stealers exfiltrent des fichiers selon patterns (documents avec mots-clés, certains types de fichiers).

La **puissance destructrice** d’un stealer log tient à sa granularité : ce n’est pas un seul couple login/mot de passe — c’est **l’intégralité de l’identité numérique** d’un utilisateur, capturée à un instant T, sur un poste spécifique.

#### 15.2 Les infostealers dominants en 2025-2026

**Lumma Stealer** (aussi « LummaC2 »). Modèle d’abonnement, ~250 USD/mois. Extrêmement répandu. Évolution constante pour éviter la détection (polymorphic, updates hebdomadaires). En 2024-2025, dominant en volume.

**RedLine**. Historiquement dominant, toujours actif malgré tentatives de disruption. Développé par un acteur russophone. Large écosystème d’affiliés.

**Vidar** (dérivé d’Arkei). Populaire pour le ciblage de wallets crypto — modules spécifiques pour MetaMask, Coinbase Wallet, etc.

**Raccoon Stealer v2**. Relancé après l’arrestation de son opérateur initial en 2022.

**StealC**. Émergent, léger et polyvalent.

**RisePro**. Ciblage spécifique des applications crypto et des gestionnaires de mots de passe (LastPass, 1Password, Bitwarden).

**Meta Stealer, Phemedrone, DarkCrystal RAT** : autres familles documentées.

**Point d’entrée économique**. SOCRadar 2025 : **dès 15 USD en version de base**, avec modèles d’abonnement qui rendent les stealers accessibles à pratiquement n’importe quel acteur. Cette accessibilité explique leur adoption massive.

**Vecteurs de distribution** :

- **Malvertising** : publicités Google/Bing malveillantes redirigeant vers des téléchargements piégés. Technique en forte croissance 2024-2025.
- **Faux sites de téléchargement logiciels crackés**. Vecteur historique dominant — particulièrement efficace sur utilisateurs cherchant cracks.
- **YouTube tutorials malveillants** : descriptions de tutoriels contenant des liens vers des malwares sous couvert d’outils légitimes.
- **Pièces jointes email** : documents Office avec macros, archives protégées par mot de passe.
- **Packages npm/PyPI malveillants** : supply chain logicielle.
- **Telegram groupes** : liens de téléchargement douteux.

#### 15.3 Les marchés de stealer logs

**Russian Market**. Successeur de facto de Genesis Market (saisi avril 2023, Operation Cookie Monster). Plus grand marché de logs actif en 2025-2026. Logs vendus individuellement avec système de **recherche par domaine** — l’acheteur cherche des logs contenant des credentials pour un domaine spécifique (par exemple, un VPN d’entreprise cible). Prix : 1-15 USD pour log basique, 50-500 USD pour log avec accès corporate (VPN, Citrix, RDP).

**Genesis Market (historique, saisi 2023)** — modèle innovant qui mérite mention. Genesis ne vendait pas seulement des credentials, mais des **bots** — navigateurs virtuels répliquant l’empreinte exacte de la victime (fingerprint navigateur, cookies, résolution d’écran, timezone, liste des plugins). Permettait d’usurper la session sans déclencher les contrôles anti-fraude basés sur fingerprint. Modèle repris par d’autres marchés.

**Canaux Telegram**. De nombreux logs distribués en bulk via canaux spécialisés, souvent **gratuitement** (« free logs ») pour attirer vers des services premium. Canaux gratuits contiennent logs anciens ou faibles valeur, mais constituent point d’entrée pour acteurs peu sophistiqués.

**2easy.gg historique**. Marché spécialisé fermé, opérations law enforcement en 2024.

**StealC Marketplace, LummaC2 Shop** : marchés adossés à des familles de stealers spécifiques.

#### 15.4 Investigation défensive : workflow

Pour un analyste défensif surveillant l’exposition de son organisation.

**Étape 1 — Monitoring des domaines**. Configurer des alertes sur marchés de logs (via plateformes commerciales type Flare, Hudson Rock, SOCRadar, Breach.ai, Flashpoint) pour les domaines de l’organisation. Chaque nouveau log contenant des credentials du domaine déclenche une alerte.

**Étape 2 — Évaluation du log**. Pour chaque log détecté, évaluer la criticité :

- **Log avec credentials webmail uniquement** : préoccupant mais gérable (reset mot de passe + vérif MFA).
- **Log avec credentials VPN/Citrix + cookies de session actifs** : **urgence** — l’attaquant peut accéder au SI sans connaître le mot de passe actuel si le cookie est encore valide.
- **Log avec credentials cloud (Azure, AWS, GCP)** : critique — impact potentiellement majeur sur l’infrastructure.

**Étape 3 — Identification du poste source**. Les métadonnées du log (hostname, IP, OS, softwares installés) permettent souvent d’identifier le poste compromis. Ce poste est **potentiellement toujours infecté** par le stealer — **changer le mot de passe sans éradiquer le stealer ne fait que fournir un nouveau mot de passe à l’attaquant**. C’est l’erreur la plus fréquente et la plus dangereuse.

**Étape 4 — Remédiation**. Le poste source doit être **isolé et réimaginé**. Tous les credentials contenus dans le log doivent être réinitialisés — pas seulement les credentials corporate, mais aussi les comptes personnels qui pourraient servir de pivot (compte GitHub personnel avec accès à des repos de l’entreprise). **Sessions actives révoquées** (tokens, cookies invalidés).

**Étape 5 — Hunting**. Le SOC vérifie si les credentials du log ont été utilisés pour des connexions suspectes depuis la date estimée de compromission. Recherche dans logs d’authentification (VPN, AD, applications cloud) pour connexions depuis IPs inhabituelles, user agents inconnus, horaires atypiques.

#### 15.5 Statistiques et géographie

Données SOCRadar 2025 : concentration des logs sur grandes plateformes consumer :

- Facebook : 93M+ logs
- Google : 67M+
- Roblox : 66M+
- Instagram : 34M+
- Microsoft Live : 31M+
- Amazon : 22M+
- Netflix : 22M+
- PayPal : 19M+

Géographie : Inde domine (2,7M logs), Brésil (1,9M), Indonésie (1,3M), États-Unis (1,2M). La position basse des US suggère meilleure détection ou remédiation plus rapide plutôt que taux d’infection inférieur.

**Implications** : plateformes gaming (Roblox, Twitch, Epic Games — utilisateurs jeunes avec hygiène credentials faible) et e-commerce/streaming (Amazon, Netflix — données de paiement stockées) sont cibles privilégiées. PayPal se distingue comme facilitateur direct de fraude.

#### 15.6 Limites et faux positifs

**Expiration**. Les cookies expirent (typiquement 30-90 jours), les mots de passe peuvent avoir été changés, le poste peut avoir été réimaginé. Log ancien (6+ mois) a une probabilité d’exploitation réussie **beaucoup plus faible** qu’un log frais.

**Faux positifs**. Domaine similaire (typosquatting), employé utilisant email pro sur site grand public, log recyclé déjà traité. Filtrage humain indispensable.

**Bruit**. Un grand compte monitoring génère des dizaines d’alertes par jour — priorisation nécessaire (criticité, fraîcheur).

#### 15.7 Fil rouge — DARKSTREAM : les stealer logs Vectris

> **🌐 DARKSTREAM — Épisode 9 : découverte collatérale**
> 
> En parallèle de son investigation sur aero_source, Lucas vérifie l’exposition Vectris sur les marchés de logs. Recherche sur Russian Market via l’accès monitoring Athéna : **12 logs** contenant des credentials du domaine `vectris-aerospace.eu`.
> 
> Analyse des 12 logs :
> 
> - 3 logs contiennent **credentials VPN (Fortinet FortiClient) avec cookies de session** — **urgence maximale**.
> - 4 logs avec credentials webmail Outlook 365.
> - 2 logs avec accès à une application SaaS RH.
> - 3 logs avec credentials divers (Jira, GitLab enterprise).
> 
> Les 3 logs VPN datent de **2 à 4 mois** — compatible avec la timeline de la compromission Vectris. **Hypothèse** : l’attaquant initial aurait utilisé un infostealer comme vecteur d’accès, les logs ont ensuite été revendus sur Russian Market par un courtier (possiblement distinct de l’auteur de l’exfiltration finale), et aero_source est soit le même acteur, soit un acheteur final qui revend les données.
> 
> Hostnames des 3 logs VPN :
> 
> - VECTRIS-SALES-047 : laptop commercial.
> - VECTRIS-RD-112 : poste R&D — **celui-ci est particulièrement préoccupant**, potentiellement le vecteur de l’exfiltration initiale des 420 Go.
> - VECTRIS-IT-008 : poste IT.
> 
> Lucas escalade immédiatement au RSSI Vectris. Mandiant (IR prestataire) confirme : VECTRIS-RD-112 est bien le poste central de la compromission, déjà identifié comme point d’entrée. Les deux autres sont des compromissions collatérales non identifiées jusqu’ici — actions immédiates enclenchées (isolement, forensics, reset massif).
> 
> Découverte collatérale précieuse : la surveillance dark web a révélé **deux postes compromis supplémentaires** que l’investigation interne n’avait pas identifiés. Illustration concrète de la valeur défensive de la veille dark web.

-----

### Chapitre 16 — Services criminels et profils d’acteurs

Au-delà des produits (données, credentials), le dark web est un marché de **services** — crime-as-a-service sous toutes ses formes. Ce chapitre cartographie les services majeurs et les profils d’acteurs.

#### 16.1 Les services majeurs

**Ransomware-as-a-Service (RaaS)**. Modèle dominant de l’écosystème ransomware. L’opérateur développe et maintient le malware + l’infrastructure (leak site, portail de négociation). Les **affiliés** déploient le ransomware chez des victimes, moyennant partage des gains (typiquement 70/30 affilié/opérateur, parfois 80/20). Ce modèle a industrialisé le ransomware : LockBit, ALPHV, Conti historique, Black Basta, Play, RansomHub actuels.

**Initial Access-as-a-Service (IAaaS)**. Les IAB compromettent et **vendent l’accès** préqualifié. Modèle spécialisé : l’IAB ne ransomware pas lui-même, il vend à un opérateur ransomware (ou autre acheteur) un accès déjà installé. Prix : 500-50 000 USD selon la cible (CA, secteur, niveau de privilèges). Délai de monétisation : plus rapide que développer une intrusion soi-même.

**Phishing-as-a-Service (PhaaS)**. Kits de phishing prêts à l’emploi, avec interface de gestion, templates, hosting. LabHost (démantelé avril 2024), EvilProxy, Evilginx (open source mais utilisé massivement). PhaaS a popularisé l’**AiTM** (Adversary-in-the-Middle) qui contourne le MFA en capturant cookies de session.

**Malware-as-a-Service (MaaS)**. Location de malware — infostealers (Lumma, RedLine mensuel), loaders, RAT, cryptominers.

**DDoS-as-a-Service**. Booters et stressers. De quelques dollars par attaque à plusieurs centaines pour attaques soutenues.

**Hosting bulletproof**. Infrastructure pour héberger contenu illicite (Ch.9).

**Cryptage / Obfuscation-as-a-Service**. Crypters et obfuscateurs pour rendre malware FUD. Service essentiel pour les opérateurs malware.

**Money laundering-as-a-Service**. Services de blanchiment crypto. Commissions 10-30% (Ch.21).

**Account checker / cracking services**. Vérification en masse de combo lists contre des services cibles (valider quels credentials marchent réellement).

**Spam / SMS bombing services**. Services commerciaux d’envoi massif.

#### 16.2 Profils d’acteurs typiques

**L’opérateur RaaS**. Figure centrale. Développe le malware, opère l’infrastructure, gère les affiliés, négocie les rançons. Équipe typique : 5-20 personnes. Revenu : plusieurs millions à dizaines de millions USD/an pour les groupes dominants. Exemple public : Dmitry Khoroshev / LockBitSupp (LockBit), autres en grande partie anonymes.

**L’affilié RaaS**. Exécutant opérationnel. Achète l’accès (via IAB ou compromet lui-même), déploie le ransomware, reçoit sa part des gains. Peut être indépendant ou partie d’une équipe. Skills : persistance, lateral movement, AD domination, parfois exfiltration. Turnover élevé — les affiliés changent de groupe selon conditions et opportunités.

**L’Initial Access Broker (IAB)**. Spécialisé dans la compromission initiale. Sources d’accès : exploitation d’edge devices (VPN, RDP exposés, vulnérabilités publiques), phishing, achat de logs, social engineering. Vend l’accès après qualification (confirmation des privilèges, cartographie minimale). Actifs connus : marées de posts sur XSS, Exploit, parfois accès de premier plan sur BreachForums.

**Le developer malware**. Écrit le code. Profil technique pur. Peut travailler pour un groupe, en freelance, ou vendre son malware comme produit. Certains devs sont très réputés dans l’écosystème pour des familles de malware spécifiques.

**Le courtier (broker) de données**. Collecte des données (achat, récupération de breaches publiés) et revend en les repackageant. Spécialisation par type (fullz, credentials bancaires, dossiers médicaux).

**Le money mule et le launderer**. Deux profils distincts. Le **mule** prête son compte bancaire ou son wallet crypto pour faire transiter des fonds — souvent recruté sous prétexte d’un emploi légitime, parfois consentant. Le **launderer** est professionnel, structure des opérations de blanchiment sophistiquées (multi-hop crypto, mixers, conversions off-chain).

**Le carder**. Spécialisé fraude cartes bancaires. Achète des dumps, les teste, les monétise (achats de biens revendables, cash advance, autres).

**Le script kiddie**. Amateur avec skills limités, utilise outils achetés. Majoritaire en nombre, minoritaire en impact. Dans les forums sérieux, traités avec condescendance.

**Le hacktiviste**. Motivation idéologique plus que financière. Opère souvent via canaux Telegram publics, moins sur forums .onion fermés. Anonymous historique, KillNet, Cyber Av3ngers, IT Army of Ukraine, etc. (Ch.38).

**L’agent étatique**. Opérateur qui utilise le dark web comme cover ou comme canal d’acquisition. APT29 a historiquement acheté des accès sur forums. La DPRK utilise le dark web pour vendre des données volées (Lazarus). Ces acteurs n’ont pas de « profil » simple — ils adaptent à chaque opération.

**L’analyste défensif / force de l’ordre / journaliste**. Observateur légitime (avec mandat). Se présente généralement comme lurker, parfois sous couverture avec persona active (Ch.22, Ch.23, Ch.30).

#### 16.3 La chaîne de valeur d’une compromission moderne

Comprendre les acteurs permet de reconstituer la chaîne typique d’une attaque enterprise 2024-2026.

**Étape 1 — Vol initial de credentials**. Un utilisateur télécharge un logiciel crack piégé, son poste personnel est infecté par un infostealer (Lumma), ses credentials (y compris son compte pro utilisé sur le poste perso) sont exfiltrés.

**Étape 2 — Vente en bulk**. L’opérateur de stealer vend les logs en lot sur Russian Market. Log basique : 15 USD.

**Étape 3 — Achat par IAB**. Un IAB achète des logs en volume, les trie pour identifier ceux avec accès corporate intéressants (VPN, Citrix, tokens cloud).

**Étape 4 — Qualification par IAB**. L’IAB utilise les credentials pour entrer dans le SI cible, vérifier les privilèges, cartographier l’environnement, identifier les cibles de valeur (DC, fileservers, backups).

**Étape 5 — Vente à affilié RaaS**. L’IAB poste l’accès sur un forum : « Access RDP + AD domain admin, EU manufacturing company, CA 500M USD, 2 000 endpoints, backup Veeam visible ». Prix : 25 000 USD.

**Étape 6 — Déploiement ransomware**. L’affilié achète l’accès, déploie le ransomware du groupe (Black Basta, par exemple). Exfiltre d’abord 800 Go de données sensibles (double extorsion), puis chiffre.

**Étape 7 — Négociation et rançon**. La victime est contactée via portail de négociation. Rançon demandée : 3 M USD. Négociation éventuelle. Paiement en Bitcoin.

**Étape 8 — Partage des gains**. Affilié reçoit 70% (2,1 M USD), opérateur RaaS 30% (0,9 M USD). Transferts crypto vers wallets opérationnels.

**Étape 9 — Blanchiment**. Les fonds passent par mixers, swaps Monero, exchanges non-KYC, OTC desks. Après 3-6 mois de chaînes, partie des fonds est convertie en fiat utilisable.

**Étape 10 — Publication partielle ou totale si non-paiement**. Si la victime ne paie pas, le groupe RaaS publie tout ou partie des données sur son leak site. Certaines données valorisables peuvent être revendues en parallèle.

Toute cette chaîne — de l’infection initiale au blanchiment — peut prendre **3 à 6 mois**. Chaque étape est opérée par un acteur spécialisé, avec ses skills et ses marchés. La cybercriminalité est une **industrie structurée**, pas une activité individuelle.

Pour le défenseur, chaque étape de cette chaîne est une **opportunité d’interruption** : détecter le stealer avant l’exfiltration, le log avant l’achat par IAB, l’accès IAB avant la vente, l’affilié avant le déploiement, l’exfiltration avant le chiffrement, la rançon avant le paiement. Plus la détection est précoce, plus l’impact est limité.

#### 16.4 Fil rouge — DARKSTREAM : la chaîne reconstituée

> **🌐 DARKSTREAM — Épisode 10 : cartographie de la chaîne**
> 
> Au terme de 2 semaines d’investigation, Lucas reconstitue la chaîne probable de compromission Vectris.
> 
> **Étape 1** — Infection initiale : un ingénieur R&D (VECTRIS-RD-112) a téléchargé un outil CAD crackéé depuis un site de warez. Infostealer Lumma déployé. Log exfiltré fin 2025.
> 
> **Étape 2** — Vente du log sur Russian Market fin 2025, ~120 USD (tier « corporate VPN + tokens actifs », premium).
> 
> **Étape 3** — Achat par un IAB russophone (pseudonyme identifié partiellement : **magnit_ru**, actif sur XSS Forum). Qualification : vérification que les credentials VPN fonctionnent, exploration réseau, identification que Vectris est un groupe industriel aerospace.
> 
> **Étape 4** — Revente. magnit_ru poste l’accès sur XSS début 2026 : « Access aerospace EU, R&D network, defense programs ». Prix demandé : ~35 000 USD.
> 
> **Étape 5** — Achat par aero_source (ou un commanditaire derrière lui). Hypothèse Lucas : aero_source est soit (a) un opérateur individuel qui a acheté l’accès et a exfiltré les 420 Go lui-même, soit (b) le front d’une équipe plus grande, soit (c) un revendeur qui a acheté le dump à un acteur qui lui a fait l’exfiltration.
> 
> **Étape 6** — Exfiltration : ~12 semaines d’activité sur le réseau Vectris (traces cohérentes avec les logs Mandiant), 420 Go extraits, focus sur R&D propulsion et dossiers fournisseurs défense.
> 
> **Étape 7** — Vente sur IndustrialLeaks : post public il y a 11 jours à 65 000 USDT.
> 
> La chaîne implique donc **au moins 3 acteurs distincts** : opérateur Lumma (infection initiale, revente bulk), magnit_ru (IAB), aero_source (exfiltration ou revente finale). Complexifie l’attribution mais multiplie les angles d’investigation. Identifier un seul de ces acteurs précisément pourrait suffire à remonter la chaîne.

-----

### Chapitre 17 — Marché des 0-day et chaîne exploit → attaque

Les **0-day** — vulnérabilités non connues de l’éditeur et donc non patchées — sont l’apex de l’écosystème offensif. Leur marché est structurant pour le dark web, avec des particularités qui distinguent ce segment du reste de la cybercriminalité.

#### 17.1 Qu’est-ce qu’un 0-day

Terminologie précise.

**Vulnérabilité** : faille dans un logiciel, une configuration, un protocole permettant potentiellement une exploitation malveillante.

**0-day (zero-day)** : vulnérabilité non encore connue publiquement et non patchée par l’éditeur. Son exploitation est potentiellement **surprise** — aucune signature ne la détecte, aucune mitigation connue ne la bloque.

**N-day** : vulnérabilité récemment rendue publique et patchée, mais pas encore déployée largement. Les attaquants exploitent les N-day pendant la fenêtre entre publication du patch et déploiement généralisé.

**Exploit** : code qui exploite une vulnérabilité. Peut être théorique (proof-of-concept), fonctionnel (weaponisé), ou en production (stable, compatible multi-environnements).

**Exploit chain** : chaîne de plusieurs exploits combinés pour atteindre un objectif plus ambitieux (par exemple : escape sandbox navigateur + escalation privilèges kernel → RCE avec privilèges système).

#### 17.2 Le marché légal : bug bounty et brokers

L’écosystème des vulnérabilités n’est pas uniquement illégal. Un marché légal existe, structuré.

**Bug bounty programs**. Les grands éditeurs (Google, Microsoft, Apple, Mozilla, Meta, Samsung, etc.) offrent des récompenses pour la déclaration responsable de vulnérabilités. Montants : de quelques centaines de dollars pour des bugs mineurs à plusieurs millions pour des chaînes d’exploits complètes sur iOS ou Android. **Apple Security Bounty** : jusqu’à 2 M USD pour une chaîne avec persistance sur iOS. **Google Vulnerability Reward Program** : jusqu’à 1,5 M USD pour certains cas Android.

**Plateformes bug bounty** : HackerOne, Bugcrowd, Intigriti, YesWeHack (français), Synack. Hébergent les programmes de dizaines de milliers d’organisations.

**Pwn2Own** : compétition annuelle (ZDI / Trend Micro, plusieurs éditions par an dans différentes villes) où des chercheurs exploitent des logiciels cibles pour des récompenses publiques. Moyen médiatisé de révéler des vulnérabilités.

**ZDI (Zero Day Initiative)** : programme de rachat de vulnérabilités par Trend Micro. Paye les chercheurs, travaille avec les éditeurs pour patch, publie les advisories.

**Brokers commerciaux** : entreprises qui achètent des vulnérabilités à des chercheurs et revendent à des clients (souvent gouvernementaux). **Zerodium** est la référence historique — prix publics depuis des années, jusqu’à 2,5 M USD pour des chaînes Android. **Crowdfense** : concurrent. **Intrepidus / ERNW / Vupen historique** : prédécesseurs. Ces brokers opèrent **légalement**, vendant à des gouvernements de démocraties (ou présentés comme tels — débats existent sur certains clients effectifs).

#### 17.3 Le marché gris et noir

En parallèle du marché légal, un marché **gris** (légalité ambiguë) et **noir** (clairement illégal) existe.

**Marché gris** : vente à des gouvernements de régimes autoritaires, ou à des entreprises de surveillance. Le 0-day lui-même n’est pas illégal — la vulnérabilité est juste de l’information technique. Mais son usage ultérieur peut être problématique. NSO Group (Pegasus), Candiru, Intellexa / Predator achètent des 0-day et les intègrent dans leurs outils de surveillance. Leurs clients incluent parfois des États qui ciblent journalistes et dissidents.

**Marché noir** : vente à des acteurs cybercriminels ou à des services de renseignement hostiles qui exploitent pour opérations offensives. Moins médiatisé, moins structuré, mais actif. Les prix peuvent rivaliser avec le marché légal pour les vulnérabilités les plus précieuses.

**Disruption** : les 0-day disparaissent du marché après publication. Leur valeur chute de 90%+ dans les semaines suivant un patch public. Les acteurs du marché noir cherchent donc à acheter des 0-day avec **exclusivité** et à les utiliser **rapidement** avant découverte et patching.

#### 17.4 Prix indicatifs

Sources : Zerodium price list publique, Crowdfense, rapports Atlantic Council, observations marché noir.

|Cible                              |Marché légal bug bounty|Marché broker (Zerodium, Crowdfense)|Marché gris/noir           |
|-----------------------------------|-----------------------|------------------------------------|---------------------------|
|Chrome RCE                         |250 k USD (Google VRP) |500 k - 1,5 M USD                   |500 k - 2 M USD            |
|iOS complete chain avec persistance|2 M USD (Apple)        |2 - 2,5 M USD                       |5 - 10 M USD (rumeurs)     |
|Android complete chain             |1,5 M USD (Google)     |1,5 - 2,5 M USD                     |3 - 8 M USD                |
|WhatsApp RCE 1-click               |N/A                    |1,5 M USD                           |Plus                       |
|Windows LPE                        |~30 k USD              |~80 k - 200 k USD                   |Comparable                 |
|Exchange Server RCE                |~30 k USD              |~100 k USD                          |Plus                       |
|Safari RCE                         |100 k USD              |~300 k USD                          |Plus                       |
|Tor Browser exploit                |—                      |Jusqu’à 1 M USD                     |Demande forte renseignement|

Variation par :

- **Fiabilité** : exploit stable qui marche à 100% vaut plus qu’un exploit probabiliste.
- **Fraîcheur** : exploit qui vient d’être découvert vs exploit avec risque de découverte imminente.
- **Contexte d’exploitation** : nécessite interaction utilisateur vs fully remote, 1-click vs 0-click.
- **Persistance** : survit aux reboot ou non.
- **Compatibilité** : fonctionne sur multiple versions du logiciel cible.

#### 17.5 La chaîne 0-day → attaque

Comment un 0-day devient une attaque concrète.

**Étape 1 — Découverte**. Un chercheur identifie une vulnérabilité. Peut venir de fuzzing automatisé (AFL, libFuzzer), de reverse engineering de patches (« 1-day research » — étudier un patch pour identifier la vuln qu’il corrige), d’audit manuel de code source.

**Étape 2 — Weaponisation**. Développement d’un exploit fonctionnel. Fiabilisation, test sur multiples versions, contournement des mitigations (ASLR, DEP, CFI, PAC, etc.). Peut prendre des semaines à des mois.

**Étape 3 — Décision économique**. Le chercheur choisit un canal : responsible disclosure (bug bounty, gratuit jusqu’à 2 M USD chez Apple), broker légal (Zerodium), broker gris, vente privée à un acteur offensif.

**Étape 4 — Intégration dans un outil**. L’acheteur intègre l’exploit dans son framework. NSO l’intègre dans Pegasus ; un APT l’intègre dans sa toolchain ; un opérateur ransomware l’intègre dans son loader.

**Étape 5 — Déploiement**. L’outil est utilisé contre des cibles. La vulnérabilité commence à être exploitée dans la nature.

**Étape 6 — Détection**. Tôt ou tard, un défenseur détecte l’attaque. Peut prendre des jours (attaque bruyante, nombreuses victimes) ou des années (opération ciblée discrète, peu de victimes).

**Étape 7 — Publication / patching**. Après détection, l’éditeur est notifié (par le défenseur, par un chercheur ayant découvert indépendamment, par le vendor observant les attaques), patche, publie l’advisory. La vuln devient N-day.

**Étape 8 — Exploitation N-day**. Fenêtre de quelques jours à semaines où le patch existe mais pas partout. Acteurs moins sophistiqués exploitent massivement.

**Étape 9 — Oubli**. La vuln devient partie de l’histoire. Son usage continue longtemps contre les systèmes non patchés (certains systèmes hérités jamais patchés sont vulnérables à des bugs découverts il y a 10 ans).

#### 17.6 Les vagues récentes exploitant des 0-day

Illustrations récentes de la chaîne 0-day → attaque dans la nature.

**MOVEit Transfer (mai-juin 2023)** — Cl0p exploite CVE-2023-34362 (0-day SQL injection dans MOVEit) massivement, impacte des milliers d’organisations (santé, gouvernements, entreprises) via leurs prestataires utilisant MOVEit.

**Citrix Bleed (CVE-2023-4966, octobre 2023)** — vulnérabilité Citrix Netscaler exploitée par LockBit, autres acteurs. Permet bypass MFA via leak de sessions.

**Ivanti Connect Secure (CVE-2023-46805, CVE-2024-21887, janvier 2024)** — exploitation par Volt Typhoon (Chine, APT) et d’autres.

**Palo Alto GlobalProtect (CVE-2024-3400, avril 2024)** — exploité par UTA0218 (possible APT).

**Oracle EBS (2025)** — exploité par Cl0p comme continuation de leur stratégie d’exploitation edge devices.

Ces vagues illustrent une tendance : les APT et groupes ransomware sophistiqués ont progressivement adopté l’exploitation de 0-day sur edge devices comme vecteur privilégié — plus discret qu’un phishing (qui génère des alertes), plus scalable qu’une intrusion manuelle, et ciblant des dispositifs souvent dépourvus de visibilité défensive.

#### 17.7 Les ventes de 0-day sur forums

Sur les forums cybercriminels, les ventes de 0-day sont **rares publiquement** mais existent. Patterns observés :

**Posts discrets**. Annonce sur XSS ou Exploit avec minimum d’info publique, négociation en privé. L’annonce mentionne classe de vulnérabilité (RCE, LPE, sandbox escape), cible (Chrome, Firefox, iOS, Android, produit spécifique), prix plancher.

**Escrow par forum**. Les forums sérieux proposent un escrow qualifié pour ces transactions — admin prend la clé du buyer et du seller, valide l’exploit fonctionne, libère après validation.

**Réputation extrême**. Seuls les vendeurs les plus établis font des ventes visibles — un nouveau compte qui prétend vendre un iOS 0-day est presque certainement scammer.

**Screenshots de démonstration**. Certains vendeurs fournissent preuve de fonctionnement (vidéo, screenshot) sous NDA avant achat. D’autres refusent toute démo sans paiement préalable (difficile à contourner mais classique).

**Clients typiques forums** : affiliés RaaS, APT moins dotés, acteurs étatiques moyens — pas les grands (qui ont leurs propres canaux).

#### 17.8 Investigation et renseignement sur les 0-day

Pour un analyste CTI défensif.

**Veille des annonces**. Monitoring de XSS, Exploit, BreachForums pour posts liés à des 0-day cibles (produits utilisés par son organisation). Alerting sur mots-clés.

**Détection des exploitations dans la nature**. Anomalies comportementales sur les edge devices (VPN, firewalls, serveurs exposés) même sans signature existante. Threat hunting proactif sur les produits historiquement ciblés.

**Collaboration avec éditeurs**. Remontée rapide à l’éditeur en cas de détection d’exploitation suspecte, pour accélérer potentiel patching.

**Analyse de patches**. Étude des patches publiés pour identifier les vulns patchées (1-day research en usage défensif) et anticiper les exploitations massives dans la fenêtre N-day.

#### 17.9 Fil rouge — DARKSTREAM : pas de 0-day impliqué

> **🌐 DARKSTREAM — Épisode 11 : angle 0-day écarté**
> 
> Lucas a initialement envisagé que la compromission Vectris aurait pu impliquer un 0-day (cible industrielle de valeur). Son investigation croisée (forensics Mandiant côté Vectris, observations dark web) confirme : **pas de 0-day**. Le vecteur était un **stealer log** classique, un accès VPN corporate acheté sur Russian Market, exploité sur plusieurs semaines pour cartographier et exfiltrer.
> 
> Cette absence de 0-day est en soi un renseignement important. Elle place l’attaquant dans la catégorie **« cybercriminel sophistiqué avec moyens limités »** plutôt que **« APT étatique avec capacités offensives haut de gamme »**. Un APT étatique ciblant Vectris pour ses secrets aerospace/défense aurait probablement utilisé un vecteur plus discret (0-day sur edge device, spear-phishing sophistiqué), pas une chaîne commoditisée stealer log → IAB → exfiltrateur.
> 
> Conséquence pour le rapport final : l’attribution pointe vers **criminalité organisée à motivation financière** plutôt que **espionnage étatique**. La DGSI confirme cette lecture. Les données exfiltrées pourraient finir entre les mains d’un acteur étatique in fine (si elles sont achetées sur IndustrialLeaks par un acheteur intermédiaire), mais le vol initial et sa commercialisation sont de profil cybercriminel.

-----

## PARTIE IV — ÉCONOMIE CLANDESTINE

> **Ce que cette partie apprend.** Comprendre **pourquoi** l’économie du dark web fonctionne malgré l’absence d’État, de contrats juridiquement exécutables, et de confiance interpersonnelle. Connaître les mécanismes (réputation, escrow, vouching, arbitrage), les pathologies (arnaques, exit scams, manipulation de la confiance), et les modèles économiques criminels qui structurent l’écosystème.
> 
> **Ce qu’elle ne couvre pas.** Les techniques d’investigation de ces économies (Partie V), les analyses de traçage financier (Ch.31), les éléments réglementaires qui tentent de les contrer (Ch.40).
> 
> **Ce que vous saurez faire après cette partie.** Lire un escrow pour y repérer les signaux d’intégrité, détecter les prémices d’un exit scam, situer un acteur dans un modèle économique (IAB, courtier, opérateur), et comprendre les incitations qui gouvernent les comportements observés.

-----

### Chapitre 18 — Pourquoi l’économie du dark web fonctionne

À première vue, l’économie du dark web devrait être impossible. Des inconnus anonymes transigent pour des montants significatifs sans tribunaux, sans contrats exécutables, sans banque centrale, sans identité vérifiée. La tentation d’arnaque devrait être permanente et dévastatrice. Pourtant, des dizaines de millions de transactions se déroulent chaque année, avec un taux de complétion relativement élevé. Comprendre pourquoi c’est un problème économique fondamental — et sa solution éclaire l’investigation.

#### 18.1 Le problème du trust sans tiers de confiance

Toute transaction économique pose un **problème de confiance**. Le vendeur craint le non-paiement, l’acheteur craint la non-livraison. Dans une économie classique, ce problème est résolu par plusieurs instruments :

- **Tribunaux** : en cas de litige, une juridiction neutre tranche selon un droit écrit.
- **Contrats** : engagements formalisés exécutables.
- **Intermédiaires** : banques, cartes de crédit avec mécanisme de chargeback, plateformes avec garanties.
- **Identité publique** : les parties sont identifiées, leur réputation est documentée, les arnaques laissent des traces traçables.

Dans le dark web, **aucun de ces instruments classiques n’est disponible**. Les parties sont pseudonymes, il n’y a pas de tribunal applicable aux transactions illégales, les paiements crypto sont irréversibles (pas de chargeback), aucune autorité ne peut légitimement contraindre une partie à exécuter.

Comment l’économie fonctionne-t-elle alors ? La réponse : par un **système de substitution institutionnelle** — les forums, marchés et communautés créent des institutions privées qui remplacent fonctionnellement les institutions publiques manquantes.

#### 18.2 Les institutions de substitution

**La réputation individuelle persistante**. Chaque pseudonyme a un historique transactionnel, des reviews, des feedbacks. Un pseudonyme avec 500 transactions réussies et 2 ratings négatifs est plus digne de confiance qu’un pseudonyme avec 3 transactions. La **réputation est le capital principal** d’un acteur sérieux — et la perdre est coûteux (repartir de zéro sous un nouveau pseudo, temps d’accumulation de 6-18 mois).

**L’escrow de forum ou marché**. Mécanisme de dépôt : l’acheteur envoie le paiement à un tiers (le forum ou le marché), qui le retient jusqu’à confirmation de livraison. Si l’acheteur confirme, le vendeur est payé. Si litige, arbitrage. Ce mécanisme, quoique imparfait, réduit drastiquement le risque d’arnaque unilatérale (Ch.19).

**Le vouching (parrainage)**. Un membre établi engage sa propre réputation en garantissant un nouveau. Si le nouveau scam, le parrain est pénalisé. Cette **chaîne de confiance transitive** permet d’accepter des nouveaux sans qu’ils partent de zéro total.

**L’arbitrage communautaire**. En cas de litige, les modérateurs ou admins tranchent selon des principes publiés (règles du forum, précédents). La **publication du jugement** fait fonctionner le système — un vendeur déclaré scammer voit son pseudonyme sali sur toute la plateforme, souvent cross-platform.

**La pression sociale et la communauté**. Les forums actifs ont une **mémoire collective**. Les scammers notoires sont connus, leurs pseudonymes listés publiquement, leurs IPs parfois publiées. Cette publicité sociale fonctionne comme un ban industriel — un scammer identifié est grillé dans tout l’écosystème pour des mois.

**Les blacklists cross-forum**. Certains forums partagent leurs listes de bannis. Un scammer banni sur XSS peut se retrouver banni préventivement sur Exploit. Cette coordination inter-forums est imparfaite mais réelle.

#### 18.3 La coûteuse construction de réputation

Pour un acteur sérieux, construire une réputation utilisable prend **6-18 mois au minimum**. Le processus typique :

**Mois 1-3 — entrée**. Création du compte sur un forum, posts de présentation, participation à des discussions. Lecture active, apprentissage des codes. Pas de vente immédiate (interdit par les règles de la plupart des forums sérieux pour les nouveaux).

**Mois 3-6 — premières transactions**. Petites ventes (50-500 USD), avec échantillons gratuits pour démontrer la qualité. Chaque transaction réussie ajoute une review positive. Les premiers 10-20 transactions sont les plus difficiles — pas encore de réputation établie, les acheteurs sont prudents.

**Mois 6-12 — consolidation**. Avec ~30-50 transactions réussies, le vendeur est **trusted**. Prix peuvent monter, qualité/spécificité de l’offre plus haute, accès aux zones premium du forum. Les gains commencent à être significatifs.

**Mois 12+ — établissement**. Après 100+ transactions, le vendeur est une figure reconnue. Clients récurrents, accès à des produits premium (0-day, accès corporate haut de gamme). Revenus potentiels de plusieurs centaines de milliers à plusieurs millions USD/an.

**Cette courbe explique plusieurs comportements** : les scammers ont tendance à opérer en rafales courtes (2-4 semaines de scam intensif, puis abandon du pseudo), parce que construire une réputation sérieuse prend trop de temps pour le petit gain à court terme. Les acteurs sérieux protègent leur réputation — ne scamment pas leurs clients, parce que la valeur actualisée de leur réputation est bien supérieure au gain d’un scam.

#### 18.4 Les ruptures de confiance

Malgré ces mécanismes, les ruptures se produisent.

**Exit scams par opérateur**. Traitement Ch.20. Un opérateur de marché ou forum s’enfuit avec les fonds en escrow.

**Vendeurs seniors qui scamment**. Rare mais arrive. Un vendeur avec 500 transactions et excellente réputation qui scam massivement en une seule opération finale. Motivation : gain ponctuel considérable avec perte de la réputation acceptée. Plus fréquent quand le vendeur sent que sa réputation va tomber de toute façon (arrestation imminente, conflit interne).

**Attaques externes**. Un forum compromis par les forces de l’ordre ou par des concurrents peut voir son historique de transactions falsifié, ses escrows volés, ses membres dox. Disruption temporaire ou définitive de l’économie locale.

**Cyclic collapse**. Parfois, une cascade de méfiance se déclenche : un vendeur majeur scam → les acheteurs méfiants retirent leurs fonds en masse → l’opérateur ne peut honorer les retraits → exit scam de l’opérateur → plateforme fermée. Panique bancaire, version dark web.

#### 18.5 Pourquoi ça marche malgré tout

Mathématiquement, l’économie fonctionne parce que :

- **Le nombre de transactions honnêtes dépasse les transactions frauduleuses**. Les acteurs sérieux, majoritaires en nombre et en volume, dominent l’activité globale.
- **La perte de réputation est coûteuse**. Pour un acteur établi, le gain d’un scam est typiquement inférieur à la valeur actualisée de sa réputation. L’incitation rationnelle est d’honorer les transactions.
- **Les mécanismes de substitution capturent la plupart des cas**. Escrow, arbitrage, blacklists gèrent la majorité des litiges.
- **Les pertes sont partagées**. Les acheteurs savent qu’un certain pourcentage de transactions échoueront. Ils calculent cette « taxe » dans leur modèle économique.

Pour un analyste, ces mécanismes sont autant de **points d’observation**. Un vendeur qui sort du schéma standard (pseudonyme neuf, pas de vouching, prix très bas, refus d’échantillon) est en probabilité très élevée un scammer — ce qui influe sur la priorisation des pistes d’investigation.

-----

### Chapitre 19 — Réputation, escrow, vouching, arbitrage

Approfondissement des mécanismes fiduciaires du dark web. Ce chapitre détaille comment ils fonctionnent concrètement et comment l’investigateur peut les lire.

#### 19.1 Le système de réputation

**Composantes d’un profil de vendeur** :

- **Ancienneté** : date d’inscription sur le forum/marché, date du premier post, date de la première transaction.
- **Nombre de transactions** : total cumulatif.
- **Feedback positif / négatif / neutre** : généralement sur échelle eBay-like.
- **Commentaires** : remarques textuelles des acheteurs post-transaction.
- **Tags et ranks** : « Trusted », « VIP », « Verified Vendor », selon le forum.
- **Historique des posts** : contributions aux discussions, activité communautaire.
- **Vouches externes** : mentions positives par d’autres vendeurs établis.

**Lecture analytique** :

- **Feedback 98%+** : probable vendeur sérieux (rares disputes, bien résolues).
- **Feedback 80-95%** : zone ambiguë — soit vendeur correct avec quelques problèmes, soit vendeur médiocre mais non scammer.
- **Feedback < 80%** : **red flag** — fuir.
- **Volume soudain en hausse** : peut signaler build-up avant exit (si opérateur) ou simplement succès légitime (si vendeur). À contextualiser.
- **Disputes récentes non résolues** : signal négatif croissant.
- **Changement de PGP** : **très rouge** — rachat de compte possible, compromis d’opérateur, acteur différent derrière le pseudo.

#### 19.2 L’escrow

**Mécanisme standard** :

1. **Listing** : vendeur crée une annonce, précise prix, escrow délai attendu (typiquement 3-14 jours).
1. **Commande** : acheteur commande, **envoie le paiement au wallet de l’escrow du marché** (pas au vendeur).
1. **Vendeur expédie** : vendeur est notifié du paiement reçu, expédie le produit.
1. **Confirmation de réception** : acheteur reçoit le produit, marque la transaction comme « finalized ».
1. **Libération** : marché libère les fonds au wallet du vendeur (moins la commission).

**En cas de litige** :

- Acheteur ouvre un dispute : explique pourquoi (non-livraison, produit non conforme, produit de moindre qualité).
- Vendeur répond : fournit preuve d’expédition, tracking, explications.
- Modérateur/admin arbitre : décision (total à l’acheteur, total au vendeur, split 50/50 ou autre).
- Feedback mutuel : les deux parties peuvent laisser des commentaires, affectant les réputations futures.

**Finalize Early (FE)**. Option disponible sur certains marchés : l’acheteur libère les fonds **avant** réception. Utilisé par vendeurs extra-fiables comme avantage compétitif (évite la trésorerie bloquée). **Risque majeur pour acheteur** — si le produit n’arrive pas, aucun recours. FE est typiquement réservée aux vendeurs top-tier.

**Multi-sig escrow**. Variante avancée : les fonds sont verrouillés sur une adresse multi-signature (2-of-3 typiquement : acheteur, vendeur, arbitre). Libération nécessite 2 signatures sur 3. Pour le vendeur : paiement libéré si acheteur confirme (2-of-3). Pour l’acheteur : remboursement possible si arbitre valide le litige (2-of-3 avec vendeur ou, en dispute, arbitre + acheteur). Le marché ne détient jamais les fonds directement — réduction du risque d’exit scam de l’opérateur. Techniquement plus complexe, pas universellement adopté.

#### 19.3 Le vouching

**Mécanisme**. Un membre établi de la communauté (« voucher ») publie un endorsement d’un nouveau membre ou d’un vendeur. Cet endorsement engage la réputation du voucher. Si le vouché scam, le voucher subit une pénalité (baisse de rank, bannissement temporaire, perte de privilèges de vouching).

**Variantes** :

- **Vouching ouvert** : le post de vouch est public, visible de tous.
- **Vouching privé** : confirmation transmise à l’admin du forum, qui valide le nouveau sans exposer le voucher.
- **Vouching transactionnel** : un membre atteste avoir réalisé une transaction avec succès avec le vouché.
- **Vouching caractérologique** : un membre atteste que le vouché est « sérieux », « honorable », sans nécessairement avoir transigé.

**Limites** :

- **Chain of vouches vulnérable** : si un voucher senior est compromis, tout ce qu’il a vouché est suspect.
- **Vouching mercenaire** : certains membres vendent leurs endorsements à prix. Pratique mal vue mais existe.
- **Sybil vouching** : un acteur contrôle plusieurs comptes et vouche lui-même ses propres comptes secondaires. Difficile à détecter dans les petits forums.

#### 19.4 L’arbitrage

**Qui arbitre** :

- **Modérateurs** du forum/marché, habituellement pour les petites disputes.
- **Admins** pour les disputes importantes ou les affaires sensibles.
- **Tiers arbitre** : certains forums ont des arbitres indépendants (membres seniors mandatés) pour réduire le conflit d’intérêt des admins.

**Processus type** :

1. Une partie ouvre le dispute, expose les faits avec preuves (screenshots, hashes, tracking, communications).
1. L’autre partie répond sous 48-72h avec sa version.
1. L’arbitre demande preuves supplémentaires si besoin.
1. Décision rendue, souvent avec argumentaire publié (visibilité pour la communauté).
1. Exécution : les fonds sont libérés selon la décision.

**Types de décisions** :

- **Full refund acheteur** : vendeur reconnu scammer ou incapable de prouver l’expédition.
- **Full release vendeur** : acheteur reconnu de mauvaise foi (dispute frauduleux après réception).
- **Split 50/50 ou autre** : incertitude, pas de preuve décisive pour l’une ou l’autre partie.
- **Dispute closed sans décision** : rare, typiquement quand les deux parties disparaissent.

**Intégrité de l’arbitrage**. Un admin corrompu peut favoriser systématiquement une partie (vendeur cartel, vendeur qui paie des bakchichs, etc.). Les forums sérieux ont des **audit trails** et parfois des **appeals** à un niveau supérieur. Un pattern de décisions biaisées finit par être identifié par la communauté, érode la confiance, et peut faire chuter le forum.

#### 19.5 L’économie de la confiance

Ce système crée une **économie de la confiance**. La réputation est un actif :

- **Transférable partiellement** : un vendeur établi peut « migrer » vers un nouveau forum en apportant des vouches de ses pairs. Il ne repart pas de zéro, mais ne bénéficie pas immédiatement de son rang maximal ailleurs.
- **Monétisable directement** : certains pseudonymes établis sont **vendus** sur des forums (rare, interdit par la plupart des règles, mais existe). Prix : 1 000-50 000 USD selon la force du pseudo.
- **Coûteuse à perdre** : un scam détruit des années de construction.

Pour l’analyste, l’économie de la confiance est un point d’attaque :

- Un acteur établi a beaucoup à perdre — les approches de type « coopération avec les autorités » ou « retournement » peuvent fonctionner là où un nouveau scammer ne céderait rien.
- Un scammer jetable est plus facile à identifier par patterns (neuf, prix bas, refus d’échantillon) mais aussi plus difficile à poursuivre (disparaît rapidement, pseudo sans histoire, pas de levier).

-----

### Chapitre 20 — Arnaques, exit scams et manipulation de la confiance

Malgré les mécanismes de confiance, l’arnaque est structurelle dans l’écosystème. Ce chapitre cartographie les grandes catégories, leurs mécanismes, et leurs signaux.

#### 20.1 Taxonomie des arnaques

**Petits scams de vendeur** :

- **Non-livraison** : acheteur paie, produit jamais envoyé. Typique pour vendeurs jetables.
- **Produit de moindre qualité** : drogues diluées, données périmées, accès non fonctionnel, malware à la place du logiciel promis.
- **Volume réduit** : vendeur promet 500 Go, livre 50 Go. Espère que l’acheteur n’audite pas.
- **Données recyclées** : vente comme « fresh breach » de données publiquement disponibles depuis des mois.

**Scams structurés** :

- **Double selling** : la même donnée vendue en exclusivité à plusieurs acheteurs. Viole les termes annoncés, destruction de la valeur.
- **Fake breach** : annonce d’un breach qui n’a pas eu lieu, avec données fabriquées pour passer quelques vérifications superficielles.
- **Impersonation** : pseudonyme qui mime un vendeur établi (slight variation orthographique). Exploite la crédibilité de la cible impersonnée.

**Exit scams** (Ch.11.4).

**Meta-scams** :

- **Fake escrow** : un « tiers de confiance » se propose pour un escrow, disparaît avec les fonds. Les forums sérieux ont leurs escrows officiels ; tout escrow tiers « découvert récemment » est suspect.
- **Fake arbitres** : usurpation d’identité d’admin. Un « admin » qui contacte en privé pour résoudre un litige est probablement faux — les vrais arbitres interviennent dans les threads officiels.

**Scams contre les analystes / forces de l’ordre** :

- **Honeypots criminels** : vendeurs qui distribuent intentionnellement des données piégées (fichiers contenant des beacons web, scripts malveillants) à des profils soupçonnés d’être des analystes.
- **Faux dissidents** : pseudonymes qui prétendent vouloir quitter le crime, vendent des « informations » aux investigateurs, souvent fausses ou trompeuses.

#### 20.2 Signaux de scam typiques

**Côté vendeur** :

- **Compte neuf** (< 3 mois) sans vouching.
- **Prix nettement inférieur** à la moyenne du marché pour le même type de produit.
- **Refus d’échantillon** systématique.
- **Pression temporelle** : « offre limitée 24h », pour empêcher la due diligence.
- **Communications incohérentes** : russe correct puis anglais bizarre puis retour russe — plusieurs opérateurs derrière un pseudo, parfois des scammers coopérant.
- **PGP non signé ou nouveau** : sérieux vendeur signe ses posts, avec clé stable.
- **Refus de multi-sig escrow** : préférence pour paiement direct ou FE. Légitime parfois, suspect souvent.

**Côté opérateur (forum/marché)** :

- **Dégradation des délais** : support qui ne répond plus, disputes qui traînent.
- **Retraits ralentis** : nouveaux délais imposés, vérifications additionnelles.
- **Buffer d’escrow visible anormalement élevé** : si le forum affiche (volontairement ou en leak) ses stocks en escrow qui grimpent alors que retraits diminuent, exit scam probable.
- **Communications des admins qui changent de ton** : plus promotionnelles, plus silencieuses, ou disparues.
- **Domaines .onion qui changent sans annonce cohérente**.
- **Partenariats communautaires qui se rompent** : anciens admins qui partent, voisins forums qui dé-vouchent publiquement.

#### 20.3 Comment se protéger (pour acheteur, pour investigateur)

**Pour l’acheteur avisé** :

- Transiger **uniquement avec des vendeurs établis** (500+ transactions, 98%+ feedback, ancienneté > 12 mois).
- Utiliser **escrow du marché** systématiquement. Jamais de paiement direct.
- **Ne pas utiliser FE** sauf vendeur trustissime.
- **Ne pas laisser de gros stock** chez un marché (retirer rapidement après transactions).
- **Vérifier les PGP** : les clés des vendeurs réputés sont stables et cross-signed.
- **Monitoring des signaux** : si le forum commence à montrer des signes d’exit scam, retirer tout immédiatement.

**Pour l’investigateur** :

- **Considérer tout nouveau post suspect par défaut** — probabilité de scam plus élevée que probabilité d’authenticité.
- **Vérifier via échantillons** avant d’allouer des ressources à une piste.
- **Cross-checker les pseudonymes** sur multiple forums pour détecter les impersonations.
- **Ne jamais payer pour « débloquer » information** — les demandes de paiement pour information sont fréquemment des scams.
- **Valider via autorités ou victime** quand possible — un breach revendiqué mais non confirmé par la victime est à traiter avec scepticisme élevé.

#### 20.4 Les grands exit scams

Historique sélectif.

**Evolution Market (mars 2015)**. Ex-second plus grand marché de l’époque. Admins « Verto » et « Kimble » disparaissent avec environ 12 M USD de BTC en escrow. Communauté anéantie, migration massive vers Abraxas puis AlphaBay.

**Nucleus (avril 2016)**. Exit scam plus modeste, ~5 M USD.

**Empire Market (août 2020)**. ~30 M USD, un des plus gros de l’histoire. Admins s’évaporent sans annonce. Les spéculations ont évoqué soit exit volontaire, soit compromission par un tiers, soit panic mid-course face à une menace judiciaire.

**Monopoly Market (2023)**. Saisi par les autorités mais au même moment, des signaux d’exit étaient présents — confusion post-hoc sur le réel séquencement.

**Incognito Market (2024)**. Modèle hybride — exit scam avec menace de dox des utilisateurs non-payeurs.

#### 20.5 La gestion d’un exit scam côté analyste

Quand un exit scam se produit sur un forum suivi, l’analyste peut :

**Capturer immédiatement** les dernières observations avant que le forum disparaisse (posts actifs, pseudonymes actifs, annonces récentes). Le forum peut re-disparaître définitivement.

**Monitorer la migration**. Les membres scammed se regrouperont sur d’autres forums, souvent avec posts « je viens de perdre 20k sur Empire, quelqu’un a des nouvelles ». Ces posts sont **riches en renseignement** — ils exposent des pseudonymes, des patterns de transaction, des sommes.

**Suivre les wallets**. Si l’admin exit scam, les fonds transitent. Les adresses reçoivent de gros montants en peu de temps, puis se dispersent. Tracking on-chain (Chainalysis, TRM) peut révéler des patterns (où vont les fonds, quelle méthode de blanchiment) et potentiellement identifier l’opérateur.

**Documenter**. Même si l’investigation ne peut pas pénaliser l’exit scammer, la documentation nourrit la connaissance de l’écosystème — profils d’admins, patterns d’opération, durées de vie typiques.

-----

### Chapitre 21 — Modèles économiques criminels

Synthèse des modèles économiques observés sur le dark web. Ce chapitre articule les rôles de la Partie III en modèles financiers cohérents.

#### 21.1 Le modèle du vendeur individuel

**Acteur** : individu ou petite équipe (1-5 personnes).

**Produit** : spécialisé — drogues, fullz, credentials, documents contrefaits, petits services.

**Volumes** : dizaines à centaines de transactions par mois.

**Revenus annuels** : 50 k - 500 k USD typiquement, jusqu’à quelques millions pour les meilleurs.

**Risques** : identification via patterns (timing, OPSEC faible), erreurs opérationnelles (réutilisation pseudonyme, leaks personnels), dispute avec un gros acheteur qui dox.

**Exemples publics** : les vendeurs condamnés sont légion dans la presse judiciaire US, UK, DE. Exemples emblématiques : « Xanax King » condamné pour vente de faux Xanax sur AlphaBay (2017-2019) ; multiples dealers saisis lors d’operations police.

#### 21.2 Le modèle de l’opérateur de plateforme

**Acteur** : équipe structurée (5-20 personnes).

**Produit** : infrastructure + arbitrage pour la communauté.

**Revenus** : commissions sur transactions + fees + services premium. Quelques millions à dizaines de millions USD/an pour les grandes plateformes.

**Risques** : saisie (multiple précédents), exit scam devenant la sortie rationnelle, conflits internes, DDoS concurrents.

**Exemples** : Ulbricht (Silk Road), Cazes (AlphaBay), Khoroshev (LockBit). Plus récemment : Baphomet (BreachForums multiple).

#### 21.3 Le modèle RaaS

**Acteur** : équipe opérationnelle (10-50 personnes au core).

**Produit** : ransomware + infrastructure + service aux affiliés.

**Revenus** : 20-30% des paiements de rançon perçus par les affiliés. Dizaines de millions USD/an pour les groupes dominants.

**Exemples** : LockBit (estimations 500 M+ USD cumulés 2020-2024 avant Cronos), Conti (estimé ~180 M USD dans la leak 2022), ALPHV (~22 M USD Change Healthcare avant disparition), Black Basta (estimations 100 M+ USD).

**Risques** : saisies d’infrastructure, inculpations nominales (LockBitSupp), conflits d’affiliés, érosion post-disruption (LockBit qui peine à rebondir).

#### 21.4 Le modèle de l’IAB

**Acteur** : individu ou petite équipe.

**Produit** : accès préqualifiés.

**Volumes** : 10-50 accès vendus par an.

**Revenus** : 500-50 000 USD par accès, selon qualité. Revenus annuels typiques 200 k - 2 M USD.

**Risques** : identification via l’accès lui-même (si l’acheteur est infiltré, les comms peuvent remonter à l’IAB), erreurs d’OPSEC dans la compromission initiale.

#### 21.5 Le modèle du service provider (CaaS)

**Acteur** : opérateur d’un service — phishing kit, DDoS booter, malware-as-service, etc.

**Produit** : service récurrent avec abonnement.

**Revenus** : abonnements (50-1 000 USD/mois par utilisateur), jusqu’à dizaines de milliers d’utilisateurs pour les plus grands. Revenus annuels de 100 k à 10 M USD selon scale.

**Exemples** : Lumma Stealer (estimation sur plusieurs milliers d’abonnés × 250 USD/mois), LabHost avant démantèlement.

**Risques** : saisies (LabHost démantelé avril 2024), inculpations d’opérateurs.

#### 21.6 Le modèle de blanchiment

**Acteur** : spécialistes financiers, souvent liés à l’écosystème crypto.

**Produit** : conversion crypto → fiat utilisable.

**Revenus** : commissions 10-30% du montant blanchi. Volumes considérables possible — plusieurs entités (Suex, Bitzlato, Garantex historiquement, Chipmixer) ont traité des milliards USD avant saisie/sanction.

**Risques** : sanctions OFAC (Suex, Bitzlato, Garantex sanctionnés), saisies (Chipmixer mars 2023, Samourai avril 2024), inculpations (Larry Harmon condamné pour Helix, Alexey Pertsev pour Tornado Cash).

#### 21.7 Le modèle de l’hébergeur bulletproof

**Acteur** : opérateur d’infrastructure.

**Produit** : hosting résistant.

**Revenus** : abonnements de hosting premium. Centaines à milliers de clients, 500-10 000 USD/mois chacun.

**Risques** : saisies (Cyberbunker 2019, multiples avant), pression upstream (de-peering, blocages).

#### 21.8 La convergence des modèles

Les modèles se chevauchent et convergent. Un acteur peut opérer comme IAB **et** affilié RaaS, comme développeur malware **et** opérateur d’un service CaaS, comme plateforme **et** commanditaire de ransomware. Cette **polymorphie économique** rend l’attribution fine complexe.

Le dark web économique 2025-2026 est mieux décrit comme un **réseau de spécialistes interconnectés** que comme un écosystème de rôles purs. Un même individu ou groupe peut jouer plusieurs rôles selon les opportunités, les contraintes, les rythmes.

#### 21.9 Implications analytiques

Pour l’analyste, cette structure économique suggère plusieurs focus.

**Suivre les flux financiers** : chaque modèle produit des patterns crypto distinctifs. Les IAB reçoivent des paiements moyens, les RaaS reçoivent de très gros paiements épisodiques, les stealer operators reçoivent des flux constants de petits paiements. Chainalysis et équivalents peuvent identifier le modèle économique par profil transactionnel.

**Reconstruire les chaînes de valeur** : identifier le modèle économique d’un acteur aide à identifier ses partenaires amont/aval. Un IAB « accès manufacturing EU » est probablement lié à un groupe RaaS anglophone ; un opérateur de stealer logs alimente des IAB multiples.

**Anticiper les transformations** : les modèles évoluent. Un vendeur individuel peut devenir IAB en montant en gamme, un IAB peut fonder son propre groupe RaaS, un opérateur RaaS peut se retirer en blanchisseur. L’analyste suit ces trajectoires pour anticiper les tendances.

**Calibrer l’attribution** : chaque modèle a ses OPSEC typiques. Un vendeur individuel fait plus d’erreurs personnelles ; un opérateur RaaS opère avec plus de rigueur ; un service provider a des infrastructures plus visibles. L’attribution est plus facile sur certains profils que sur d’autres.

-----

## PARTIE V — INVESTIGATION, VEILLE ET COLLECTE

> **Ce que cette partie apprend.** Conduire une investigation dark web de manière professionnelle — cadre juridique et éthique, OPSEC de l’analyste, méthodes de collecte, workflow d’investigation d’un data leak, pivoting OSINT, veille continue, préservation des preuves.
> 
> **Ce qu’elle ne couvre pas.** Les méthodes avancées d’analyse et d’attribution (Partie VI), les cas d’usage spécifiques par secteur (Partie VII), les études de cas complètes (Partie VIII).
> 
> **Ce que vous saurez faire après cette partie.** Conduire une enquête OSINT sur le dark web en respectant le cadre légal français/européen, bâtir et maintenir une persona, investiguer un leak de données de manière structurée, préserver les preuves de manière admissible, et construire un programme de veille dark web durable.

-----

### Chapitre 22 — Cadre juridique, éthique et sécurité de l’analyste

Avant tout outil technique, l’analyste dark web doit maîtriser le cadre légal qui encadre son activité. Consulter un forum cybercriminel n’est pas illégal en soi — mais certains actes d’investigation le sont, et d’autres sont dans une **zone grise** qu’il faut savoir naviguer.

#### 22.1 Le cadre français

**Code pénal articles 323-1 à 323-8**. Atteinte aux STAD (systèmes de traitement automatisé de données). Incrimine :

- **323-1** : l’accès ou le maintien frauduleux dans un STAD (maximum 3 ans d’emprisonnement et 100 000 € d’amende ; circonstances aggravantes si suppression/modification de données : 5 ans, 150 000 €).
- **323-2** : l’entrave du fonctionnement d’un STAD (7 ans, 300 000 €).
- **323-3** : la modification frauduleuse de données (7 ans, 300 000 €).
- **323-3-1** : la détention et la diffusion d’outils conçus pour commettre ces infractions — **article clé pour l’analyste**, qui encadre la manipulation d’outils offensifs.

**Loi du 24 juillet 2015 sur le renseignement** et articles associés dans le Code de la sécurité intérieure : cadre des activités de renseignement encadrées par l’État. L’analyste privé n’opère pas sous ce régime, mais les agences partenaires (DGSI, DGSE) peuvent.

**Loi Informatique et Libertés + RGPD**. La collecte et le traitement de données personnelles exposées (même exposées par un attaquant) restent soumis aux régimes de protection. Un analyste qui capture un dump contenant des données personnelles doit gérer ce stock selon les règles applicables — base légale de traitement, minimisation, sécurisation, suppression post-exploitation.

**Code de procédure pénale article 40**. Tout fonctionnaire qui, dans l’exercice de ses fonctions, acquiert la connaissance d’un crime ou d’un délit, est tenu d’en aviser le procureur. Un analyste fonctionnaire (service public, OIV) peut être concerné — même en secteur privé, la logique de signalement est structurante.

**Cadre ANSSI / OIV**. Les OIV ont obligation de notification d’incidents significatifs à l’ANSSI. Les prestataires PASSI/PDIS/PRIS opèrent sous qualification.

#### 22.2 Le cadre européen

**Directive NIS 2 (UE 2022/2555)**. Transposée en France et dans tous les États membres. Obligations de cybersécurité et notification pour les entités essentielles et importantes dans 18 secteurs. Les analystes opérant pour ces entités ont un rôle dans la posture de notification.

**RGPD**. Régit les données personnelles. Les dumps contenant données personnelles doivent être traités avec base légale (intérêt légitime de l’investigation, mission de service public, etc.), minimisation, sécurité.

**Convention de Budapest sur la cybercriminalité (2001) et ses protocoles additionnels**. Cadre de coopération internationale en matière cybercriminalité. Protocole additionnel de mai 2022 facilite l’accès transfrontière à la preuve électronique.

**EU Cyber Solidarity Act (2024)**. Crée un réseau européen de SOC et un mécanisme de réponse d’urgence pour incidents cyber transfrontaliers.

**EU Cyber Sanctions Regime**. Sanctions ciblées contre cyberacteurs malveillants.

#### 22.3 Les zones grises

Plusieurs activités sont **dans la zone grise** — techniquement légales mais nécessitent prudence.

**Consulter des forums criminels**. Légal en tant que tel. La simple consultation d’un contenu publiquement accessible (même sur .onion) n’est pas une infraction.

**Créer un compte sur un forum criminel**. Nécessaire pour accéder aux zones fermées. Légal, avec précautions — le pseudonyme ne doit pas être utilisé pour commettre des infractions (solliciter des services criminels, acheter des données, participer à des discussions opérationnelles).

**Télécharger des échantillons**. Zone sensible. Télécharger un fichier contenant des données personnelles (même publiquement exposées par l’attaquant) peut contrevenir au RGPD. Télécharger du malware pour analyse est **généralement accepté** dans un cadre de recherche, mais la détention de malware est encadrée par l’article 323-3-1. Pratique recommandée : n’en télécharger que ce qui est strictement nécessaire à la mission, documenter la justification, sécuriser le stock, supprimer après exploitation.

**Télécharger des données volées**. Encore plus sensible. Principe : **nécessité et proportionnalité**. Télécharger un échantillon pour authentification est différent de télécharger l’intégralité d’un dump.

**Télécharger du CSAM**. **Interdit absolument**. Même dans un cadre d’investigation, la détention est criminelle. Les investigations CSAM relèvent des autorités judiciaires avec cadre spécifique (pornographie enfantine, articles 227-23 et suivants du Code pénal).

**Payer pour obtenir de l’information**. Dépend du contexte. Payer un droit d’entrée forum pour investigation : généralement accepté avec autorisation hiérarchique et traçabilité. Acheter des données volées : **risqué** — peut constituer recel. La DGSI accompagne ces cas.

**Contacter un vendeur en se faisant passer pour acheteur**. Zone grise classique. Généralement accepté pour investigation avec encadrement, mais peut constituer provocation dans certains cadres — la jurisprudence française est restrictive sur la **provocation à la commission d’infraction**. L’analyste doit se présenter comme acheteur potentiel pour obtenir des échantillons, mais ne pas pousser le vendeur à augmenter son activité criminelle.

**Infiltrer un groupe comme membre actif**. Réservé aux forces de l’ordre avec mandat judiciaire. Un analyste privé qui « infiltrerait » un groupe criminel dépasse largement le cadre légal.

#### 22.4 L’éthique professionnelle

Au-delà de la légalité stricte, plusieurs principes éthiques s’appliquent.

**Minimisation**. Collecter le minimum nécessaire à la mission. Ne pas stocker plus que ce qu’on exploite. Supprimer après exploitation.

**Non-prolifération**. Ne pas rediffuser les données collectées au-delà du cercle justifié. Un dump contenant des données personnelles ne se partage pas lightly, même entre analystes.

**Non-exploitation abusive**. Les données volées peuvent contenir des informations sensibles (vie privée, communications intimes, données médicales). L’analyste ne les exploite qu’au strict nécessaire à la mission, pas par curiosité.

**Transparence hiérarchique**. Les choix d’investigation sensibles (contact vendeur, paiement, téléchargement) sont documentés et autorisés par la hiérarchie.

**Respect des victimes**. Les victimes de breach sont des personnes. Contact avec elles doit respecter leur dignité — ni sensationnaliser, ni exploiter leur détresse.

**Coopération avec autorités**. Si l’investigation révèle des infractions graves (trafic humain, CSAM, terrorisme), signalement obligatoire aux autorités compétentes. Le secret professionnel n’est pas absolu.

#### 22.5 La sécurité personnelle de l’analyste

L’investigation dark web expose à plusieurs risques **personnels**.

**Risque technique**. Compromission du poste d’investigation via malware piégé. Les fichiers téléchargés, les liens cliqués, les sites visités peuvent contenir des exploits ciblant les analystes. Mesures : machine dédiée, VM jetables (Whonix + VM d’exécution), pas de comptes personnels sur la machine.

**Risque d’identification par les cibles**. Les acteurs malveillants font de la contre-surveillance. Un analyste qui utilise ses accès personnels, qui lit systématiquement les posts d’un vendeur spécifique, qui pose des questions révélatrices — peut être identifié comme investigateur. Conséquences : ciblage du compte d’investigation, tentative d’identification réelle (dox), voire menaces physiques dans les cas extrêmes.

**Risque juridique transfrontalier**. Un analyste français qui interagit avec un vendeur russe via un forum hébergé aux Pays-Bas peut techniquement tomber sous multiple juridictions. En pratique, si l’activité est légale en France et dans le cadre d’une mission professionnelle, le risque est faible, mais pas nul.

**Risque de manipulation psychologique**. L’immersion dans l’écosystème dark web expose à des contenus difficiles (violences, CSAM accidentellement croisé, narratifs extrêmes). L’analyste doit être soutenu par son organisation — debriefing psychologique, rotation des missions, limitation de l’exposition aux contenus traumatisants.

**Risque de compromission éthique**. Dérive possible — un analyste exposé longtemps à l’écosystème peut développer de l’empathie pour les cibles, se laisser tenter par des relations personnelles avec des sources, perdre la distance professionnelle. Supervision hiérarchique et rotation atténuent.

#### 22.6 Fil rouge — DARKSTREAM : encadrement légal

> **🌐 DARKSTREAM — Épisode 12 : cadrage DGSI**
> 
> Lucas prépare son premier contact avec aero_source. Avant action, validation DGSI obligatoire.
> 
> Réunion avec l’officier DGSI référent. Points validés :
> 
> - **Contact OK** sous persona « mapletech » — acheteur technologique intéressé par specs aéronautiques. Légende crédible.
> - **Pas d’engagement ferme d’achat** — Lucas peut exprimer intérêt, demander échantillons, négocier indirectement, mais jamais confirmer la transaction. La DGSI précise : « ne provoquez pas la vente, cherchez à comprendre ».
> - **Pas de téléchargement de l’intégralité** — échantillons acceptés pour authentification, le dump complet non.
> - **Remontée bi-hebdomadaire** : Lucas briefe la DGSI tous les 3-4 jours sur l’évolution.
> - **Arrêt immédiat** si Lucas perçoit un risque d’exposition (persona identifiée comme analyste, menaces, contre-enquête).
> - **Pas d’achat** des données. Si aero_source impose paiement pour les échantillons (rare), arrêt de l’investigation de ce côté.
> 
> Tous les échanges XMPP sont archivés (logs chiffrés chez Athéna, accessibles DGSI). Capture d’écran au fur et à mesure. Hash des fichiers téléchargés. Documentation exhaustive du cheminement d’investigation.
> 
> Cette rigueur procédurale est **la condition de l’utilisabilité** de ce que Lucas produira. Un rapport sans chain of custody documentée n’a aucune valeur judiciaire. Un rapport trop fondé sur des actions juridiquement douteuses peut être écarté.

-----

### Chapitre 23 — OPSEC opérationnelle de l’investigation

L’**OPSEC** (Operations Security) de l’analyste dark web est le pilier de la réussite d’une investigation. Une OPSEC défaillante expose l’analyste, compromet la mission, et peut mettre en danger les sources coopératives ou les collègues.

#### 23.1 La séparation des univers

Principe fondamental : **séparation totale** entre l’univers personnel de l’analyste, son univers professionnel hors investigation, et son univers d’investigation.

**Machines séparées**. Ordinateur dédié à l’investigation dark web. Jamais utilisé pour activités personnelles (réseaux sociaux, emails, banque), jamais pour activités professionnelles générales (mails corporate, documents, visioconférences). Configuration minimale : OS dédié (Whonix, Tails), navigateur Tor Browser uniquement, outils strictement nécessaires.

**Comptes séparés**. Emails jetables (protonmail, ctemplar, services .onion) pour les comptes d’investigation. Jamais de lien avec emails corporate ou personnels.

**Identités séparées**. Les personas d’investigation (pseudonymes, handles Telegram, JID XMPP) sont **strictement cloisonnées** de l’identité réelle de l’analyste. Aucune réutilisation d’un pseudo entre personas. Aucun lien traçable entre les personas et l’identité réelle.

**Financier séparé**. Wallets crypto dédiés à l’investigation, financés par un circuit professionnel (exchange corporate avec KYC de l’entreprise, pas de l’analyste personnellement). Transactions tracées par l’entreprise pour audit.

**Temporel séparé**. L’investigation se fait dans des créneaux dédiés. Le mélange entre activités dark web et tâches personnelles dans le même créneau temporel crée des risques de contamination (oubli de fermer Tor Browser avant d’ouvrir son email personnel, etc.).

#### 23.2 La persona

Une **persona** est un personnage fictif construit pour l’investigation. Elle doit être **crédible** et **cohérente**.

**Éléments de la persona** :

- **Pseudonyme** : unique, ne ressemble pas à d’autres pseudonymes utilisés par l’analyste (pas de pattern identifiable).
- **Histoire** : d’où vient-elle ? quel métier ? quelles compétences ? quels intérêts ?
- **Langue** : style d’écriture cohérent avec l’origine prétendue. Un analyste français qui joue un persona russophone doit maîtriser les codes linguistiques russophones — sinon se cantonne à l’anglais.
- **Niveau technique** : si persona « script kiddie » prétend avoir peu de skills, elle ne doit pas poser des questions trop sophistiquées. Si persona « pro » doit comprendre les concepts avancés.
- **Activité historique** : la persona a-t-elle des posts dans des forums parallèles ? Une présence sur Telegram ? Un historique crédible ?
- **Infrastructure cohérente** : serveur XMPP utilisé, méthodes de paiement préférées, heures d’activité.

**Construction préalable**. Une persona utilisable pour une investigation sérieuse prend **3-6 mois** à construire — inscription sur un forum, posts graduels, participation communautaire, construction d’une histoire minimale. Les personas « jetables » (créées le jour, utilisées le lendemain) sont facilement identifiables comme non-authentiques.

**Maintenance**. Une persona doit être **active** même quand pas utilisée sur une investigation active. Posts occasionnels, participation à des discussions générales. Une persona inactive pendant 6 mois puis réactivée pour une enquête ciblée déclenche la méfiance.

**Burnability**. Accepter qu’une persona peut être brûlée. En ce cas, ne pas chercher à la « sauver » — l’abandonner, en construire une nouvelle. Toute tentative de réactiver une persona suspecte aggrave l’exposition.

#### 23.3 La sécurité technique

**Tor Browser en mode Safest**. JavaScript désactivé. Beaucoup de fonctionnalités cassées, mais pas d’exécution de code exploitable. Certains sites nécessitent JS — évaluer le risque au cas par cas, activer temporairement si site considéré sûr.

**VM isolée**. Toute interaction au-delà de la simple navigation (téléchargements, fichiers exécutables) dans une VM jetable. Snapshot avant action, restauration après. Ne jamais exposer l’OS hôte à du contenu dark web non-simple-HTML.

**Pas de JavaScript actif sur sites suspects**. Les NIT (Network Investigative Techniques) et les exploits navigateur exploitent JS (Ch.30). Mode Safest le bloque ; si on l’active, on doit comprendre les risques.

**Pas de WebRTC**. Tor Browser désactive WebRTC ; ne pas l’activer manuellement. WebRTC peut leaker l’IP réelle.

**Pas de plugins**. Flash, Java, PDF readers intégrés — désactivés ou absents. Tor Browser configure ça par défaut.

**Vérification des .onion**. Les adresses .onion sont longues (56 caractères v3). Les scammers créent des adresses similaires via vanity generation. **Toujours vérifier l’adresse complète**, via source fiable (site officiel du service, post établi sur forum réputé, backup en dur pré-validé).

**Hashing des fichiers**. Tout fichier téléchargé est hashé (SHA-256 minimum) avant ouverture. Le hash sert de référence pour la chain of custody et pour vérifier que le fichier n’a pas été altéré entre collecte et analyse.

**Pas de métadonnées**. Les screenshots sont pris puis **strippés de métadonnées** (exiftool). Les documents créés pendant l’investigation (notes, rapports) ne doivent pas contenir de métadonnées personnelles (nom d’auteur dans Word, etc.).

#### 23.4 Les erreurs classiques

**Réutilisation de pseudonymes**. Un analyste qui utilise le même pseudo sur plusieurs enquêtes risque la corrélation. Les forums observent les patterns — un pseudo qui demande des échantillons de données industrielles aerospace sur un forum et des échantillons bancaires sur un autre est soit un acheteur éclectique, soit un investigateur.

**Corrélation temporelle**. Pseudo actif aux heures ouvrables françaises systématiquement. Indique fuseau horaire Europe occidentale, incompatible avec un persona prétendument russophone.

**Fuites linguistiques**. Expressions françaises dans un persona anglophone, conventions de dates françaises (DD/MM) dans un persona américain (MM/DD), traduction littérale d’idiomes français.

**Over-sharing**. Par nervosité ou tentative de crédibilité, l’analyste donne trop d’infos sur sa « persona » — détails sur son entreprise fictive, anecdotes personnelles vérifiables. Chaque détail est une surface d’attaque pour la contre-investigation.

**Accès depuis infrastructure corporate**. L’analyste qui accède à Tor depuis l’IP corporate de son bureau (même via VPN Tor) expose son organisation. Poste dédié dans un réseau isolé recommandé.

**Comptes personnels sur la machine d’investigation**. Un analyste qui check ses emails personnels sur la machine dark web compromet tout le cloisonnement.

**Documentation défaillante**. Une investigation sans logs précis de chaque action (heure, URL visitée, fichier téléchargé, hash, pseudonyme utilisé) ne produit pas de preuves utilisables.

**Abandon de prudence sur la durée**. Au début de l’enquête, OPSEC rigoureuse. Après 3 mois, fatigue, relâchement. L’erreur survient plus tard, pas au début.

#### 23.5 Le programme OPSEC d’équipe

Pour une équipe CTI, l’OPSEC doit être **institutionnelle**, pas individuelle.

**Procédures documentées**. Playbook formalisé : comment créer une persona, comment ouvrir un compte, comment gérer les paiements, comment capturer les preuves, comment documenter.

**Peer review**. Chaque action sensible (création de persona, premier contact vendeur, téléchargement d’échantillon) est validée par un pair ou la hiérarchie.

**Supervision**. Un responsable CTI a visibilité sur les investigations en cours, alloue les personas, valide les escalades.

**Formation continue**. L’OPSEC évolue (nouvelles techniques de dé-anonymisation, nouveaux pièges). Formation périodique, veille sur les techniques offensives utilisées contre les analystes.

**Incident response OPSEC**. Plan d’action en cas de compromission de persona — quoi abandonner, quoi sauvegarder, qui prévenir, comment communiquer.

**Débriefing psychologique**. Les missions longues dans l’écosystème dark web sont éprouvantes. Sessions régulières avec psychologue ou pair expérimenté.

-----

### Chapitre 24 — Naviguer et collecter : méthodes, outils, limites

Aspect pratique : comment on navigue effectivement sur le dark web, quels outils on utilise, et quelles sont les limites techniques et méthodologiques.

#### 24.1 L’outillage de base

**Tor Browser** : navigateur de référence. Basé sur Firefox ESR, hardened, en mode Safest pour l’investigation. À télécharger **uniquement** depuis torproject.org (ou ses miroirs officiels).

**Tails** : distribution Linux live. Démarre sur clé USB, ne laisse aucune trace sur la machine. Recommandée pour les investigations les plus sensibles.

**Whonix** : architecture en deux VM (Gateway + Workstation). Isolation forte. Recommandée pour setup permanent d’investigation.

**Qubes OS** : système d’exploitation avec isolation par VM (AppVMs). Très sécurisé mais courbe d’apprentissage plus raide.

**VM dédiée dans VMware/VirtualBox** : alternative accessible si Whonix est trop lourd. Clone de l’OS avant chaque session, restauration post-session.

**Outils complémentaires** :

- **curl / wget via Tor** (torify) : récupération en ligne de commande.
- **OnionScan** : audit automatique de services .onion pour failles OPSEC.
- **tsocks / proxychains** : chaînage de proxies.
- **Aquatone, Eyewitness** : capture automatisée de screenshots en masse.
- **Hunchly** : outil commercial de capture structurée d’investigation (horodatage, archivage, notes).
- **Maltego** : graphing des relations entre entités (avec transformations spécifiques dark web).

#### 24.2 Les sources et points d’entrée

**Comment trouve-t-on des .onion** ?

**Listes communautaires**. The Hidden Wiki (multiple instances, pas toutes fiables), Dark.fail, Tor.taxi. Ces listes sont **partielles et partiellement scam-compromised** — ne jamais cliquer aveuglément.

**Moteurs de recherche .onion**. Ahmia, Torch, Haystak, Excavator. Indexation **très partielle** du contenu .onion. Utile pour des recherches spécifiques, mais rarement exhaustif.

**Cross-references depuis forums**. Les forums mentionnent d’autres forums, marchés, canaux. Documentation par ce biais — plus fiable que les listes car vouchées par la communauté.

**Canaux Telegram**. Beaucoup d’acteurs postent leurs adresses .onion sur Telegram, ce qui les rend plus facilement découvrables. Surveiller les canaux pertinents.

**Services de monitoring commerciaux**. Recorded Future, SOCRadar, Flashpoint, Flare, Intel471, DarkOwl, Cybersixgill — tous maintiennent des bases d’entités dark web crawlées. Accès via abonnement entreprise.

**OSINT public**. Articles de presse, papers académiques, rapports vendors — regorgent de mentions d’adresses .onion qui ont fait l’actualité.

#### 24.3 La collecte structurée

**Capture vs simple navigation**. La collecte doit être **structurée**, pas simple navigation. Capturer systématiquement :

- **URL complète** visitée.
- **Horodatage précis** (timestamp avec seconde, fuseau horaire).
- **Capture d’écran** du contenu.
- **HTML source** sauvegardé.
- **Hash** du contenu sauvegardé.
- **Pseudonyme utilisé** pour la session.

**Archivage**. Plusieurs options :

- **Hunchly** : outil commercial qui automatise capture + organisation + horodatage.
- **Archivage manuel** : dossiers structurés, nommage convention (YYYYMMDD-HHMMSS-source-description), fichiers immutables.
- **Container cryptographiquement signé** : après collecte, générer un hash global du dossier, horodater, signer (GPG), stocker en immutable.

**Organisation**. Par cas d’investigation, par source, par date. Éviter le « one big folder » — impossible à remonter après 6 mois.

#### 24.4 Les challenges techniques

**Lenteur du réseau Tor**. Navigation 5-10× plus lente que clearnet. Planifier des sessions d’investigation longues, éviter la multitâche excessive.

**Disponibilité intermittente des .onion**. Un site .onion peut être down pour heures ou jours. Tenter plusieurs fois, utiliser des mirrors (si connus), noter les patterns de disponibilité.

**DDoS permanents**. Les grands forums sont régulièrement DDoSés. Les pages chargent lentement, partiellement, ou pas du tout. Les meilleures heures d’investigation sont souvent les créneaux nocturnes (fuseau horaire attaquant).

**CAPTCHA pervasifs**. Pour limiter le scraping, beaucoup de sites .onion implémentent CAPTCHAs difficiles, parfois impossibles pour des outils automatisés.

**Protections anti-scraping**. Limites de requêtes, défis JS, tokens de session, fingerprinting — rendent la collecte automatisée complexe.

**Sites éphémères**. Un forum peut déménager d’adresse .onion sans préavis. Une capture d’il y a 6 mois peut pointer vers un site disparu. Les archives ont donc une valeur disproportionnée sur le dark web.

#### 24.5 Les limites méthodologiques

**Biais de survivance**. Ce qu’on observe est ce qui existe actuellement. Les acteurs qui disparaissent ne sont plus observables. Les forums saisis ne sont plus accessibles (sauf archives). L’image du dark web à un instant T est partielle et biaisée vers les survivants.

**Biais de visibilité**. Les acteurs les plus sophistiqués sont souvent les moins visibles. Un APT étatique n’a pas besoin d’un leak site flashy — il opère discrètement. Les acteurs observables sur forums publics sont majoritairement de profil intermédiaire.

**Biais de représentation**. L’analyste observe à travers les forums qu’il connaît. L’écosystème russophone, chinois, arabophone, persan ont chacun leurs dynamiques propres, partiellement accessibles selon les compétences linguistiques de l’équipe.

**Biais de fraîcheur**. Les données anciennes disparaissent. Un forum actif il y a 2 ans peut être invisible aujourd’hui. L’histoire du dark web est partiellement perdue.

**Biais d’accès**. Les zones premium des forums (souvent les plus intéressantes analytiquement) nécessitent paiement, vouching, tenure. Un analyste privé n’a pas toujours les moyens d’accéder à toutes les zones utiles.

#### 24.6 Automatisation et échelle

**Scraping automatisé** : possible mais difficile. Les protections anti-bot sont fortes. Nécessite infrastructure (plusieurs instances Tor, rotation d’identités), résilience (retry logic, gestion erreurs), légalité (certains ToS interdisent scraping même sur sites criminels).

**Plateformes commerciales** : outils SaaS qui font le crawling à grande échelle et exposent les résultats via API. Recorded Future, DarkOwl, Flare, Intel471, Cybersixgill. Coût : 50 k - 500 k USD/an selon scale.

**Open source** : quelques projets open source (OnionScan, TorBot, Dark-Scrape) mais moins robustes que solutions commerciales.

**Approche hybride** : scraping ciblé sur sources prioritaires + plateforme commerciale pour couverture large + veille humaine pour les signaux faibles.

#### 24.7 Fil rouge — DARKSTREAM : l’accès à IndustrialLeaks

> **🌐 DARKSTREAM — Épisode 13 : setup et navigation**
> 
> Lucas utilise son environnement Whonix avec Tor Browser Safest. Accès initial à IndustrialLeaks via l’adresse .onion communiquée par le partenaire vouching. Vérification de l’adresse : 56 caractères, cross-check sur 2 sources indépendantes (mention dans un post Recorded Future + mention sur un forum russophone peer).
> 
> Navigation lente — 2-3 secondes par clic. Le forum affiche un CAPTCHA proof-of-work (JS requis à minima pour le CAPTCHA). Lucas active JS **uniquement pour la page de login**, puis le désactive après. Session de navigation active, avec Hunchly en background pour capture systématique.
> 
> Exploration structurée :
> 
> 1. Captures de toutes les catégories publiques (arborescence du forum).
> 1. Lecture et capture du post aero_source + tous les posts du même user.
> 1. Navigation aux autres vendeurs du mois, pour profiling comparatif.
> 1. Règles du forum (capture).
> 1. Statistiques visibles (nombre de membres, posts, transactions).
> 
> Cycle de 3 heures. 147 pages capturées, structurées par dossier. Hash du corpus calculé. Persona « mapletech » affiche activité cohérente (quelques réponses en threads, aucun message offensif, aucune tentative de solliciter info sensible au-delà de ce qui est publiquement affiché).
> 
> Post-session, Lucas produit un **mémo d’observations** : architecture du forum, profils de vendeurs actifs, posts d’intérêt, observations sur aero_source. Ce mémo alimente le dossier DARKSTREAM et permet aux autres membres de l’équipe Athéna d’orienter leurs propres recherches sans re-naviguer manuellement.

-----

### Chapitre 25 — Investigation dans un data leak : workflow

Ce chapitre présente un workflow structuré pour investiguer une annonce de fuite de données. C’est l’une des situations les plus fréquentes pour un analyste CTI défensif — alerte de monitoring, il faut déterminer si la fuite est réelle, pertinente, et actionnable.

#### 25.1 Le cadre de l’investigation

**Déclencheur typique** :

- Alerte automatique de plateforme de monitoring (Recorded Future, Flare, Hudson Rock) : « mention de votre marque détectée sur forum X ».
- Signalement journalistique : « un journaliste cite une rumeur de breach sur votre entreprise ».
- Signalement partenaire : « un CERT sectoriel partage une alerte ».
- Auto-découverte : analyste qui observe un post suspect lors de sa veille courante.

**Objectifs de l’investigation** (dans l’ordre de priorité) :

1. **Confirmer ou infirmer l’existence** du breach.
1. **Authentifier les données** offertes.
1. **Évaluer le volume et la sensibilité** de ce qui circule.
1. **Cartographier l’écosystème** (vendeur, acheteurs, éventuels courtiers intermédiaires).
1. **Dater** la compromission.
1. **Identifier le vecteur** si possible.
1. **Produire un rapport actionnable** pour la cellule de crise.

**Contraintes** :

- **Temps** : la cellule de crise attend des réponses rapides. 24-72h pour premier verdict.
- **Légal** : cadre défini Ch.22. Pas de téléchargement massif, pas de provocation.
- **OPSEC** : ne pas alerter le vendeur que la victime est notifiée (sinon disparition des traces).
- **Coordination** : si OIV, DGSI/ANSSI impliqués ; si multi-victimes, partage sectoriel.

#### 25.2 Étape 1 — Triage initial

**Objectif** : en 2-4 heures, déterminer si l’alerte mérite investigation approfondie ou peut être classée.

**Questions clés** :

- Le **post** est-il récent ou recyclé (reposé d’un breach antérieur) ?
- Le **vendeur** a-t-il un profil crédible (ancienneté, transactions, vouching) ou est-ce un nouveau compte ?
- Le **forum** est-il sérieux (XSS, Exploit, BreachForums) ou low-end ?
- Les **détails du post** sont-ils spécifiques (volumétrie, types de données, contexte) ou génériques ?
- Les **échantillons** sont-ils fournis ou non ?

**Décision** :

- **Scam probable** : fermer le dossier avec note. Monitoring light pour détecter escalade.
- **Recyclage** : identifier le breach original, mettre à jour le dossier historique, pas d’investigation approfondie.
- **Cas authentique probable** : escalader en investigation structurée (suite du workflow).
- **Ambigu** : investigation légère pour clarifier avant décision.

#### 25.3 Étape 2 — Profiling du vendeur

**Objectif** : comprendre qui pose l’annonce.

**Collecte** :

- Historique **sur le forum principal** : tous les posts du pseudo, dates, catégories, réponses reçues.
- **Cross-platform** : présence du pseudo sur d’autres forums, canaux Telegram, Jabber, etc. Ch.26 pour pivoting détaillé.
- **Style linguistique** : langue maternelle apparente, niveau technique, style de négociation.
- **Activité financière connue** : adresses crypto affichées, patterns de transactions visibles on-chain.
- **Relations** : qui vouche le vendeur ? qui achète ? avec qui interagit-il dans les threads ?

**Output** : fiche de profil du vendeur, 2-4 pages, avec observations et hypothèses initiales sur son positionnement dans l’écosystème.

#### 25.4 Étape 3 — Acquisition d’échantillons

**Objectif** : obtenir des données permettant l’authentification.

**Modalités** :

- **Échantillons publics** : si le vendeur en a posté en thread public, capture simple.
- **Échantillons sur demande** : contact via canal indiqué (XMPP, Telegram), avec persona d’investigation.
- **Pas d’engagement ferme** : demande d’échantillons supplémentaires positionnée comme due diligence pré-achat, pas comme achat effectif.
- **Refus d’achat complet** : le cadre n’autorise pas l’achat du dump complet. Les échantillons servent à confirmer, pas à exfiltrer.

**Précautions** :

- Fichiers manipulés **uniquement en VM isolée**.
- Scan antivirus/sandbox avant ouverture.
- Extraction de métadonnées avant exécution.
- **Ne jamais ouvrir dans l’OS hôte**.

#### 25.5 Étape 4 — Authentification

**Objectif** : déterminer si les données sont authentiques et proviennent de la victime annoncée.

**Techniques** :

**Métadonnées de fichiers**. PDF, DOCX, XLSX — extraction des métadonnées avec exiftool. Cherche : auteur, entreprise, chemin de création, horodatages, révisions. Un document avec métadonnées « Created: Vectris Aerospace, Author: M. Dubois, 2025-11 » cohérentes avec l’entreprise cible est fort.

**Cohérence de contenu**. Les noms d’employés dans le fichier correspondent-ils à des employés réels (vérifiables sur LinkedIn, site corporate) ? Les références projets correspondent-elles à des projets connus ? Les références fournisseurs sont-elles plausibles ? Les numéros de révision, codes internes, formats de référence correspondent-ils aux conventions documentées de l’entreprise ?

**Markers internes**. Certaines entreprises matures incluent des **markers intentionnels** dans leurs documents sensibles — fausses entrées dans les bases fournisseurs, employés fictifs dans les annuaires internes, entreprises fictives dans les listes de partenaires. La présence de ces markers dans un dump confirme qu’il provient bien de l’entreprise. **Vectris avait un tel marker** (fictif) dans sa liste fournisseurs — retrouvé dans l’échantillon DARKSTREAM.

**Corrélation avec données publiques**. Si le dump contient des éléments disponibles publiquement (communiqués, rapports annuels, documents marketing), les comparer. Un dump qui contient un document public identique à la version publique n’ajoute rien ; un dump qui contient un brouillon du communiqué postérieur à une version précédente — et ce brouillon est antérieur à la publication officielle — atteste d’un accès interne.

**Demande d’échantillon ciblé**. Demander au vendeur un fichier spécifique contenant un nom connu. S’il peut le fournir, l’authenticité est très probable. S’il refuse ou fournit quelque chose d’incohérent, suspicion.

**Cross-check forensics interne**. Transmettre les échantillons à l’équipe IR de la victime. Ils peuvent confirmer l’authenticité par comparaison avec leurs bases internes.

**Output** : niveau de confiance dans l’authenticité (scale : non-authentique / probable / très probable / confirmé), argumentaire détaillé.

#### 25.6 Étape 5 — Cartographie de l’écosystème

Une fois l’authenticité évaluée, cartographier le contexte.

**Qui est l’auteur initial du vol** ? Le vendeur sur le forum est-il l’attaquant, un courtier, un acheteur final revendeur ?

**Y a-t-il d’autres traces** ? Le même dump est-il proposé sur d’autres forums ? Circulation privée ? Tentatives de chantage direct de la victime ?

**Qui sont les acheteurs potentiels** ? Concurrents ? Acteurs étatiques ? Groupes cybercriminels cherchant un levier de ransomware ? IndustrialLeaks ciblant une clientèle spécifique ?

**Quel est le vecteur d’entrée** ? Corrélation avec logs internes, stealer logs sur la victime, exploits publics de la période, TTP d’un groupe APT connu.

**Quelle est la chronologie** ? Dates de compromission, d’exfiltration, de mise en vente — compatibles avec les traces forensiques internes ?

#### 25.7 Étape 6 — Analyse des flux financiers

Si le vendeur affiche une adresse crypto (pour recevoir paiement), cette adresse est une mine de renseignement.

**Capture de l’adresse**. Copier exactement depuis la source.

**Traçage on-chain**. Analyse via Chainalysis Reactor, TRM Labs Forensics, Elliptic Investigator, ou équivalent open source (Breadcrumbs, OXT).

**Questions analytiques** :

- L’adresse a-t-elle reçu des paiements ? De qui (quels autres wallets) ?
- L’adresse est-elle connue comme liée à d’autres opérations (blacklistée par Chainalysis) ?
- Les fonds ont-ils été déplacés ? Vers où (mixer, exchange, autre wallet) ?
- Cluster d’adresses connecté : des dizaines d’autres adresses peuvent être contrôlées par le même acteur.

Voir Ch.31 pour détails du traçage crypto.

#### 25.8 Étape 7 — Production du rapport

**Structure standard** :

1. **Executive summary** (1 page) : qu’est-ce qui a fuité, degré de confiance, recommandations urgentes.
1. **Contexte** : comment l’alerte a été détectée, sources initiales.
1. **Observations factuelles** : ce qui a été observé sur le dark web, avec captures et horodatages.
1. **Analyse d’authenticité** : arguments pour/contre, conclusion.
1. **Cartographie** : acteurs impliqués, chaîne potentielle, chronologie.
1. **Impact évalué** : quelles données exposées, conséquences potentielles business/légale/réputationnelle.
1. **Recommandations** : actions immédiates (isolation postes, reset credentials, notifications), actions moyen terme (monitoring, communication, enquêtes).
1. **Annexes** : captures d’écran, hashes, extraits de communications, adresses crypto observées.

**Ton** :

- **Factuel**, pas sensationnaliste.
- **Calibré** : utiliser le vocabulaire des Words of Estimative Probability — « très probable », « probable », « possible », « incertain ».
- **Actionnable** : les recommandations sont concrètes, chiffrées quand possible, hiérarchisées.
- **Révisable** : le rapport est une photo d’un instant T, à compléter avec nouvelles observations.

**Diffusion** :

- Cellule de crise interne : diffusion restreinte, TLP RED ou AMBER selon sensibilité.
- Autorités (DGSI, ANSSI, CNIL si données personnelles) : remontée obligatoire pour OIV.
- Partenaires sectoriels (ISAC) : éventuellement TLP AMBER anonymisé.
- Public (rare, cas exceptionnels) : communiqué officiel coordonné.

#### 25.9 Fil rouge — DARKSTREAM : rapport intermédiaire

> **🌐 DARKSTREAM — Épisode 14 : rapport à mi-parcours**
> 
> Après 3 semaines d’investigation, Lucas produit un rapport intermédiaire pour la cellule de crise Vectris et la DGSI.
> 
> **Executive summary** :
> 
> - Authenticité des données Vectris sur IndustrialLeaks : **confirmée** (marker interne + cohérence forensics Mandiant).
> - Volume exfiltré : **420 Go confirmés**, incluant specs propulsion, documents de conception, bases clients/fournisseurs, emails internes, budgets.
> - Vendeur aero_source : acteur russophone intermédiaire, probablement **revendeur** (pas auteur direct de l’exfiltration).
> - Chaîne reconstituée : infostealer Lumma → vente log Russian Market → achat par IAB magnit_ru → revente accès → exfiltration par aero_source ou commanditaire.
> - Aucun acheteur final identifié pour les données Vectris (ni traces de paiement sur l’adresse BTC affichée par aero_source).
> - Niveau de menace : **élevé** mais pas **critique** en termes de diffusion élargie.
> 
> **Recommandations immédiates** :
> 
> - Poursuite isolation/reset des postes compromis identifiés (VECTRIS-RD-112, VECTRIS-SALES-047, VECTRIS-IT-008).
> - Notification aux partenaires défense concernés par les spécifications exposées.
> - Poursuite monitoring IndustrialLeaks + forums liés pour détection publication totale ou vente confirmée.
> - Préparation communication client/partenaires en cas d’escalade.
> 
> **Recommandations moyen terme** :
> 
> - Durcissement politique de téléchargement de logiciels sur postes R&D.
> - Déploiement EDR renforcé sur segment R&D.
> - Campagne sensibilisation antivol de credentials (stealer) pour collaborateurs.
> - Revue des règles firewall pour détecter exfiltrations volumineuses sortantes.
> 
> Le rapport est transmis TLP:RED à la cellule de crise, TLP:AMBER à la DGSI. La cellule active les recommandations ; la DGSI oriente Lucas vers la suite de l’investigation — identification d’aero_source.

-----

### Chapitre 26 — Pivoting, enrichissement et corrélation OSINT

Le **pivoting** est l’art de passer d’un indicateur à un autre pour enrichir l’investigation. Sur le dark web, c’est la différence entre une observation isolée et un renseignement exploitable.

#### 26.1 Les types de pivots

**Pseudonyme → autres forums**. Un pseudonyme observé sur un forum peut exister sur d’autres. Recherche directe du pseudo sur XSS, Exploit, BreachForums, forums concurrents.

**Pseudonyme → Telegram / Jabber / TOX**. Les posts mentionnent souvent des handles de contact. Suivre ces handles sur les plateformes correspondantes.

**PGP key → autres utilisations**. Une clé PGP est un identifiant quasi-unique. Rechercher la clé (fingerprint) sur d’autres forums, dans des archives, sur des keyservers publics — peut révéler d’autres pseudos ou usages antérieurs.

**Adresse crypto → transactions, clustering**. Une adresse BTC observée permet de découvrir : historique on-chain, adresses liées (cluster), exchanges interagis, autres wallets probablement contrôlés par le même acteur (via heuristiques de change, co-dépense, etc.).

**Infrastructure (domaines, IPs) → autres services**. Un domaine enregistré pour un service criminel peut partager des infos avec d’autres (registrant email, serveurs de noms, mêmes IPs d’hébergement). Outils : DomainTools, SecurityTrails, ViewDNS, passivedns commerciaux.

**Email / fingerprint → OSINT classique**. Un email leaked sur un forum, un pseudonyme utilisé ailleurs (Discord, GitHub, Reddit, StackOverflow, jabber distinct) — permettent de construire un graphe d’identité.

**Style linguistique → attribution**. Tournures, fautes, patterns — peuvent corréler plusieurs pseudos.

**Timing → fuseau horaire**. Patterns d’activité horaire révèlent fuseau. Crosscheck avec autres pseudonymes actifs aux mêmes heures.

#### 26.2 Méthodologie de pivoting

**Graph d’investigation**. Maintenir un graphe (Maltego, graphes maison) où chaque nœud est une entité (pseudo, email, wallet, IP, domaine) et chaque arête est une relation (« utilise », « contrôle », « a interagi avec », « mentionne »). Chaque nouveau pivot ajoute des nœuds et arêtes.

**Hypothèses explicites**. À chaque pivot, formuler une hypothèse (« Je pense que pseudo A et pseudo B sont la même personne parce que… »). Tester l’hypothèse avec nouveaux pivots. Renforcer ou rejeter.

**Niveaux de confiance**. Comme pour l’attribution APT (voir cours APT), utiliser vocabulaire calibré : certain / très probable / probable / possible / spéculatif.

**Limites documentées**. Certaines corrélations sont faibles (mêmes initiales pseudo, timing vague) ; d’autres fortes (même PGP key, même wallet). Le rapport final doit distinguer les deux.

#### 26.3 Les ressources OSINT utiles

**Bases de données de breach**. Have I Been Pwned, DeHashed, LeakCheck, Snusbase — vérifier si un email ou identifiant a été exposé dans des breaches publics, reconnaître un pseudo qui apparaît dans d’autres contextes.

**Archives forums**. Certains forums disparus ont des archives partielles disponibles — BreachForums archives, Tor’s Everything mirror, Internet Archive pour le clearnet.

**GitHub / GitLab**. Parfois, un acteur utilise le même pseudo professionnellement (développement, open source) et dans les forums cybercriminels. Historique public GitHub peut révéler nom réel, email, localisation, compétences.

**LinkedIn / Xing**. Pour les pivots partiels vers identité civile. Un email pro leaked peut correspondre à un profil LinkedIn.

**Keyservers PGP**. Ubuntu keyserver, SKS pools (legacy), Keys.openpgp.org. Recherche par fingerprint peut révéler identités alternatives.

**Blockchain explorers**. Blockstream.info, Mempool.space (Bitcoin), Etherscan (Ethereum), Tronscan (TRON), BlockChair (multi-chain). Traçage des transactions à partir d’adresses observées.

**WHOIS et passive DNS**. Pour le pivoting d’infrastructure.

**Reverse image search**. Google Images, TinEye, Yandex. Un profile picture d’un forum peut correspondre à un profil ailleurs.

**Services spécialisés dark web**. IntelX (archives .onion et leaks), Flare, Recorded Future, DarkOwl, Cybersixgill — agrègent et indexent.

#### 26.4 Les erreurs courantes

**Sur-corrélation**. Conclure qu’un pattern faible (initiales communes, style superficiel) prouve que deux pseudos sont la même personne. Le dark web compte des millions d’utilisateurs, beaucoup de coïncidences.

**Biais de confirmation**. Une fois qu’on a un chouchou (« c’est forcément X »), on trouve partout des « preuves ». Discipline : chercher activement ce qui **infirmerait** l’hypothèse.

**Timing trompeur**. Les fuseaux horaires se simulent facilement — un acteur peut activer son compte à des heures calibrées.

**Pseudos communs**. « admin », « king », « boss », « ghost » sont utilisés par des milliers d’acteurs indépendants. Pas un pivot fiable seul.

**Infrastructure partagée**. Plusieurs acteurs utilisent le même hébergeur, registrar, service de certificat. Pas un pivot fiable à lui seul.

**PGP reprise**. Rare, mais une clé PGP peut être volée ou rachetée. Changement soudain du style après une longue présence d’un pseudo avec la même clé = alerte sur une possible rachat.

#### 26.5 Fil rouge — DARKSTREAM : pivoting sur aero_source

> **🌐 DARKSTREAM — Épisode 15 : élargissement**
> 
> Lucas pivote sur aero_source au-delà d’IndustrialLeaks.
> 
> **Pivot 1 — XSS Forum** : recherche du pseudo « aero_source » sur XSS (accès Athéna via partenariat vouching). **Pas de compte direct**, mais un compte « aerosrc » créé il y a 13 mois, style similaire, utilise le même serveur XMPP. Probable sock puppet ou compte antérieur. Activité modeste (4 posts).
> 
> **Pivot 2 — Exploit.in** : recherche. Pseudo « aero_src » existe, compte créé il y a 7 mois, style compatible. 3 posts, un sur une vente de specs turbines (non-Vectris, différente cible). **Cohérent avec pattern** d’un même acteur opérant sur 3 forums russophones.
> 
> **Pivot 3 — PGP** : la clé PGP affichée par aero_source sur IndustrialLeaks est **identique** à celle sur aerosrc (XSS) et aero_src (Exploit.in). **Très forte corrélation** — probabilité qu’il s’agisse du même acteur : 95%+.
> 
> **Pivot 4 — Wallet BTC** : l’adresse BTC mentionnée dans le post aero_source sur IndustrialLeaks. Chainalysis révèle un cluster de ~40 adresses liées. Transactions totales : ~180 000 USDT sur 14 mois. Quelques flux vers exchange non-KYC (Garantex historique, avant sanctions 2022). Interactions avec adresses labellisées « BlackSprut » (marché russophone) — indique acheteur de drogues ou fournisseur dans cet écosystème.
> 
> **Pivot 5 — Analyse linguistique** : les posts des 3 comptes (aero_source, aerosrc, aero_src) présentent les mêmes tics — « dear colleagues » comme ouverture, « best regards » comme signature, fautes consistantes (confusion article « the », prépositions). Russophone, niveau anglais intermédiaire. **Corrélation linguistique cohérente avec PGP**.
> 
> **Pivot 6 — Telegram** : le handle mentionné par aero_source (non utilisé ici pour OPSEC) pointe vers un compte Telegram. Observation light, pas de contact. Ancienneté compte : 2 ans. Membre de plusieurs canaux cybercriminels russophones.
> 
> **Synthèse** : aero_source est (très probablement) un acteur russophone individuel, présent sur l’écosystème depuis 2+ ans, profil IAB/courtier de données intermédiaire, pas un acteur majeur. Son réel intérêt pour les données Vectris n’est pas idéologique ni étatique — motivation financière classique.
> 
> Ce profiling oriente l’attribution et le conseil : la menace est réelle mais contenue dans un profil cybercriminel, pas le signe d’une opération étatique majeure. Conséquences pour Vectris : le dump ne servira probablement pas un concurrent direct ou un service de renseignement étranger à court terme — il sera vendu au plus offrant, potentiellement n’importe qui.

-----

### Chapitre 27 — Veille dark web : surveillance, alerting, réduction du bruit

La **veille dark web** n’est pas une investigation ponctuelle — c’est un programme durable. Ce chapitre couvre la structuration d’une veille efficace, les outils, et la gestion du bruit.

#### 27.1 Les objectifs de la veille

Pour une organisation, plusieurs objectifs distincts peuvent justifier une veille dark web.

**Détection de compromission**. Mentions de la marque sur forums/marchés/leak sites → possible breach à investiguer. Détection de credentials de l’organisation sur marchés de logs → possible vecteur de compromission. Détection d’IAB proposant des accès compatibles → menace imminente.

**Monitoring de dirigeants et VIP**. Mentions de personnalités (CEO, CFO, membres du conseil) — risques de fraude, chantage, usurpation.

**Veille concurrentielle / réputationnelle**. Activité malveillante autour de la marque — deepfakes, impersonations, phishing ciblant clients.

**Renseignement sectoriel**. Tendances dans le secteur : quelles campagnes ransomware ciblent l’aerospace ? quels vecteurs utilisés pour compromettre manufacturers ? Alimentation de la threat intel.

**Renseignement géographique**. Tendances par pays : quelles entités françaises sont ciblées ? quels groupes actifs en Europe ?

**Renseignement sur adversaires spécifiques**. Suivi d’APT ou groupes ransomware identifiés comme menaces prioritaires pour l’organisation.

#### 27.2 Les sources à surveiller

**Leak sites ransomware**. Monitoring via Ransomwatch, Ransomfeed, plateformes commerciales. Alerting sur mentions de la marque ou du secteur.

**Forums majeurs**. XSS, Exploit, BreachForums — via crawling (si capacités) ou via plateformes qui le font.

**Marchés de logs**. Russian Market principalement. Monitoring par domaine.

**Marchés de fraude**. BriansClub, successeurs. Moins critique pour la plupart des organisations non-financières.

**Canaux Telegram**. Canaux identifiés comme pertinents — cybercrime russophone, leaks, hacktivisme pro/anti-pays X.

**Pastebins et assimilés**. Pastebin (partiellement désactivé pour usage criminel), Ghostbin, Rentry, Doxbin, etc.

**Feeds CTI**. VirusTotal, URLhaus, ThreatFox, etc. — indicateurs partagés communautairement.

**GitHub**. Fuites de credentials dans repos publics (GitHub dorking). Secrets committed par erreur, puis effacés mais toujours dans l’historique.

**Réseaux sociaux**. Twitter/X, Mastodon pour signaux de mentions, revendications hacktivistes, réactions de la communauté.

**Deep web non-tor**. Forums clearnet à accès restreint (payment, invite), souvent plus faciles d’accès que les .onion et riches en contenu.

#### 27.3 Les outils de monitoring

**Plateformes commerciales CTI** (budget 50 k - 500 k USD/an) :

- **Recorded Future** : leader du marché, intelligence mondiale, intégration étendue.
- **Flashpoint** : forte expertise russophone et Telegram.
- **Intel471** : focus acteurs et écosystème cybercriminel.
- **SOCRadar** : plus abordable, bon rapport qualité/prix pour PME.
- **Flare** : niche dark web et data leaks, prix compétitif.
- **DarkOwl** : crawling .onion étendu.
- **Cybersixgill** (Zenity) : profilage et attribution.
- **Hudson Rock** : spécialisé stealer logs.
- **KELA** : forte couverture russophone.
- **Group-IB** : vision Europe/Asie.

**Outils open source** :

- **Ahmia** : moteur de recherche .onion, partiellement open source.
- **TorBot, Dark-Scrape** : crawlers open source (maintenance variable).
- **OnionScan** : audit de services .onion.
- **GitHub dorking** : outils pour détecter secrets dans repos.
- **Ransomwatch** : agrégateur public de leak sites ransomware.

**Services sectoriels**. Certains ISAC (par secteur) partagent de la threat intel par abonnement ou gratuitement pour leurs membres.

**Services gouvernementaux**. En France, partage d’information via l’ANSSI (CERT-FR, signalement d’incidents). Bulletins d’alerte publics.

#### 27.4 Le défi du bruit

La veille dark web produit **énormément de faux positifs**. Un programme mal configuré génère des centaines d’alertes par semaine, dont la majorité ne nécessitent aucune action. Gérer le bruit est la compétence centrale du programme de veille.

**Sources de bruit** :

- **Homonymies** : « Vectris » est une marque, mais aussi possiblement un prénom, un nom commun dans d’autres langues, une entité sans lien.
- **Mentions éditoriales** : articles de presse, rapports CTI mentionnent l’entreprise sans être des signaux de compromission.
- **Credentials anciens** : comptes employés exposés dans breaches antérieurs (Adobe 2013, LinkedIn 2012, Collection #1 en 2019), re-mis en vente ou re-publiés.
- **Scams et fakes** : annonces de breach inexistants.
- **Typos et variantes** : « Vectriss », « Vectris_corp », « Victreis » — à filtrer ou à surveiller.

**Stratégies de réduction du bruit** :

**Keywords précis**. Utiliser des termes spécifiques (noms de produits internes, codes clients, adresses email pro, identifiants propriétaires) plutôt que seulement la marque générique.

**Whitelist éditoriale**. Filtrer les sources éditoriales (presse, rapports publics) qui mentionnent légitimement la marque sans menace.

**Filtrage temporel**. Dépriorer les mentions anciennes, prioritiser les nouvelles.

**Priorisation par criticité**. Mention sur forum XSS russophone > mention sur pastebin anonyme > mention éditoriale. Logs VPN corporate > logs consumer perso d’un employé.

**Machine learning**. Les plateformes commerciales appliquent du ML pour scorer la pertinence. Efficacité variable — complément de l’humain, pas remplaçant.

**Triage humain**. En fin de chaîne, un analyste trie les alertes résiduelles. 80-90% classées en quelques secondes chacune, 10-20% méritent investigation plus poussée.

#### 27.5 Workflow de veille type

**Quotidien** (1-2h/jour pour un analyste dédié) :

- Revue des alertes automatiques (plateforme commerciale).
- Triage initial — classement en « ignorer », « surveiller », « investiguer ».
- Investigations légères sur les alertes ambigües.
- Mise à jour des indicateurs suivis.

**Hebdomadaire** (demi-journée) :

- Revue des leak sites ransomware ciblage sectoriel.
- Veille sur forums prioritaires (top 5-10 identifiés).
- Synthèse hebdomadaire pour le CISO et la direction.
- Mise à jour de la liste de surveillance.

**Mensuel** :

- Rapport mensuel structuré : tendances, incidents majeurs, évolutions observées.
- Revue du scope de monitoring — ajouts, retraits.
- Évaluation de la qualité des sources et outils.

**Trimestriel** :

- Audit du programme de veille.
- Évolution du budget et des ressources.
- Formation continue des analystes.
- Partage avec pairs sectoriels (ISAC, RSSIs par secteur).

#### 27.6 Le programme de veille comme outil défensif

Au-delà de la détection d’incidents, un programme de veille bien structuré sert plusieurs fonctions défensives.

**Threat intelligence pour le SOC**. Les observations alimentent les règles de détection (IoC à surveiller, TTP à anticiper, vulnérabilités exploitées activement par acteurs connus).

**Aide à la priorisation défensive**. Si les stealers ciblent massivement un secteur, durcir les politiques correspondantes. Si un vecteur spécifique (phishing kit, vulnérabilité edge device) est en croissance, mitiger en priorité.

**Sensibilisation**. Les exemples observés nourrissent les campagnes de sensibilisation employés. « Regardez, voici un log d’infostealer vendu pour 15 USD qui contenait les credentials d’un collègue » fait plus d’impact qu’une théorie abstraite.

**Préparation stratégique**. Les tendances observées (convergence crime-étatique, montée de tel groupe, décl in de tel autre) alimentent la planification pluriannuelle de sécurité.

**Posture de négociation**. En cas de crise (ransomware subi, données exposées), une bonne veille préalable permet de connaître l’adversaire et de négocier en position informée.

-----

### Chapitre 28 — Preuve, capture et documentation

La différence entre une observation intéressante et une preuve utilisable tient à la **documentation**. Ce chapitre couvre la préservation des preuves de manière admissible — pour rapport interne, pour coordination avec autorités, et le cas échéant pour usage judiciaire.

#### 28.1 Les niveaux de documentation

**Niveau 1 — Documentation interne** : pour rapport à la cellule de crise, à la direction. Exigence : lisible, structuré, horodaté. Pas de formalisme judiciaire strict.

**Niveau 2 — Documentation pour autorités** : pour transmission à DGSI, ANSSI, CNIL. Exigence : chain of custody, horodatages fiables, hashes, traçabilité. Format standard (IOCs, STIX/TAXII si pertinent).

**Niveau 3 — Documentation admissible judiciairement** : pour usage dans procédure pénale. Exigence : chain of custody rigoureuse, capture forensically sound, témoin pour certaines captures, signature notariale ou équivalent pour éléments critiques. Un analyste privé produit rarement directement ce niveau ; il prépare les éléments pour que les forces de l’ordre puissent les reconstituer avec leur propre cadre.

**Niveau 4 — Documentation coopérative** : pour partage sectoriel (ISAC, pairs RSSI). TLP AMBER typiquement. Format structuré pour réutilisation par les pairs (indicators actionnables, sans données sensibles exposées).

#### 28.2 La chain of custody

Principe : pour chaque élément de preuve, tracer **qui l’a collecté, quand, comment, et par qui il a été manipulé depuis**. Toute rupture dans la chaîne invalide potentiellement la preuve.

**Éléments à tracer pour chaque capture** :

- **Date et heure précise** (UTC recommandé, avec fuseau indiqué).
- **Analyste** qui a effectué la capture.
- **Source** : URL .onion, forum, thread ID, post ID.
- **Méthode** : capture d’écran, HTML source save, wget, screenshot d’une VM.
- **Hash cryptographique** du fichier capturé (SHA-256 minimum).
- **Emplacement de stockage** : chemin dans l’archive Athéna, sauvegarde sur stockage immutable.
- **Modifications** : aucune idéalement, ou documentées si nécessaires.

**Outils d’aide** :

- **Hunchly** : outil commercial qui automatise une grande partie de la chain of custody.
- **OSINT Cloner** : alternative open source, moins complète.
- **Custom scripts** : beaucoup d’équipes développent leurs propres scripts de capture structurée.

#### 28.3 Types de preuves et méthodes de capture

**Pages web (HTML)**. Capture en deux formats :

- **Screenshot** : rendu visuel, incluant CSS et images. Utile pour le lecteur humain.
- **HTML source** : code source brut. Utile pour l’analyse technique et la reconstitution.

Outils : wget/curl (via torify), outils navigateur (save page as, print to PDF), Hunchly, Aquatone pour volumes.

**Threads de forums**. Capturer tous les posts d’un thread, même si longs et paginés. Hunchly ou scripts qui parcourent la pagination.

**Messages privés**. Dans une messagerie (XMPP, Telegram), exporter le log chiffré complet. Conserver les métadonnées (horodatages, clés de session, participants).

**Fichiers téléchargés**. Hash immédiat post-téléchargement. Pas de modification avant analyse en VM. Stockage du fichier original intact + copie de travail pour analyse.

**Adresses crypto et transactions**. Capture de l’adresse exacte (copier-coller, pas retranscrire). Capture de transactions via blockchain explorer avec screenshots. Exports via Chainalysis, TRM, etc. horodatés.

**Captures temporelles**. Un site peut changer entre 2 visites. Capture datée à chaque fois. Archive via service tiers (Internet Archive pour clearnet, mais difficile pour .onion — archives manuelles alors).

#### 28.4 Le stockage des preuves

**Immutabilité**. Une fois capturées, les preuves ne doivent pas pouvoir être modifiées. Options :

- **Stockage WORM** (Write Once Read Many) : solutions enterprise (AWS S3 Object Lock, Azure immutable blobs, NAS avec WORM).
- **Blockchain timestamping** : horodatage sur blockchain publique (OpenTimestamps, Bitcoin via OP_RETURN) — prouve qu’un document existait à une date donnée.
- **Signature cryptographique** : GPG signature par l’analyste, horodatée.
- **Archive sur CD/DVD non réinscriptibles** (pratique moins moderne mais acceptée judiciairement).

**Confidentialité**. Les preuves stockées restent sensibles. Chiffrement au repos, contrôle d’accès granulaire, logs d’accès. Idéalement : accès nécessitant plusieurs personnes pour ouvrir (modèle multi-party).

**Rétention**. Politique documentée : combien de temps conserver ? La plupart des organisations retiennent 3-7 ans selon cadre réglementaire et risques. Destruction formalisée après fin de rétention.

**Localisation**. Stockage dans pays cohérent avec le cadre juridique (France pour les preuves servant enquêtes françaises, idéalement), éviter stockage dans juridictions où les preuves pourraient être saisies ou exposées.

#### 28.5 La notarisation et l’horodatage qualifié

Pour les preuves à haute valeur, le **simple hash** ne suffit pas toujours. Techniques additionnelles :

**Horodatage qualifié**. En France et en UE, services d’horodatage qualifiés eIDAS. Un horodatage qualifié prouve juridiquement qu’un document existait à une date donnée. Plusieurs fournisseurs (Universign, Docapost, prestataires qualifiés).

**Constat d’huissier**. Un huissier de justice peut constater le contenu d’un site web à un instant T. Coûteux (plusieurs centaines à milliers d’euros par constat) mais haute valeur probante en procédure judiciaire française.

**APCTA** (Authentification de Preuve Constatée par un Tiers Attentif) — services privés qui fournissent une forme d’attestation horodatée, moins formelle qu’un huissier mais plus accessible.

Pour une investigation CTI courante, horodatage + hash + chain of custody documentée suffit. Les procédures judiciaires plus lourdes (constat d’huissier) sont réservées aux cas où la preuve sera utilisée en contentieux.

#### 28.6 Les indicators of compromise (IoC)

Au-delà de la documentation narrative, l’investigation produit des **indicators of compromise** — artefacts techniques réutilisables.

**Types d’IoC** :

- **Hashes de fichiers** (MD5, SHA-1, SHA-256 — le dernier préféré).
- **URLs / domaines** malveillants.
- **Adresses IP** C2, infrastructure.
- **Adresses crypto** utilisées par acteurs criminels.
- **Emails** utilisés dans phishing / scams.
- **Pseudonymes** de forum.
- **PGP fingerprints**.
- **YARA rules** : règles de pattern-matching pour détecter malwares.
- **Sigma rules** : règles de détection pour SIEM.
- **STIX objects** : format structuré pour interchange de TI.

**Format de partage** :

- **STIX/TAXII** : standard OASIS pour cyber threat intelligence, format structuré pour interchange machine-to-machine.
- **MISP** : plateforme communautaire de partage, format riche, TLP natif.
- **Feeds CSV / JSON** : formats simples pour intégration SIEM.
- **Emails structurés** pour partage ad hoc entre équipes.

**Coordination**. Les IoC sont partagés selon TLP :

- **TLP RED** : strictement entre équipes désignées.
- **TLP AMBER** : partage avec partenaires de confiance (ISAC, RSSI sectoriel).
- **TLP GREEN** : partage avec communauté élargie (CERT communautaire).
- **TLP CLEAR** : public.

#### 28.7 La communication des résultats

Au-delà de la production des preuves, **communiquer les résultats** est une compétence à part entière.

**À la cellule de crise interne** :

- **Sommaire exécutif** : 1 page max, conclusions et recommandations.
- **Dossier technique** : détails pour l’équipe IR.
- **Capture préservée** : preuves accessibles en cas de besoin ultérieur.

**Aux autorités** :

- **Format standard** requis par l’autorité (DGSI a ses canaux, ANSSI a ses templates).
- **Anonymisation éventuelle** : parfois, certaines informations ne peuvent être transmises (sources, méthodes d’obtention).
- **Chain of custody maintenue**.

**Aux pairs sectoriels (ISAC)** :

- **Indicators anonymisés** : victim stripped, IoC techniques conservés.
- **Tactics observées** : utile pour détection chez les pairs.
- **TLP AMBER** typiquement.

**Publiquement (rare)** :

- **Rapports éditoriaux** : pour sensibilisation. Un cabinet CTI peut publier son investigation après anonymisation de la victime (si elle consent) ou généralisation.
- **Advisories** publiques : pour alerter la communauté sur des menaces spécifiques.

**Erreurs de communication à éviter** :

- **Sur-confidence** : présenter une hypothèse comme certitude. Calibrer.
- **Jargon excessif** : audience non-technique se perd. Ajuster le niveau.
- **Conclusions trop techniques** : ne pas traduire en action business.
- **Rigidité** : le rapport est un instantané, pas une vérité éternelle. Indiquer révisabilité.

#### 28.8 Fil rouge — DARKSTREAM : la documentation finale

> **🌐 DARKSTREAM — Épisode 16 : la pochette de preuves**
> 
> Après 6 semaines d’investigation, Lucas finalise la **pochette de preuves** de DARKSTREAM pour remise à Vectris et DGSI.
> 
> **Contenu de la pochette** :
> 
> 1. **Rapport principal** (42 pages, signature PGP de Lucas) — narration complète, analyse, recommandations.
> 1. **Annexe A : captures IndustrialLeaks** — 147 screenshots + HTML sources de tous les posts pertinents, chaque fichier horodaté et haché SHA-256. Index XLSX avec correspondance screenshots/horodatages.
> 1. **Annexe B : conversations XMPP avec aero_source** — export complet chiffré, hashé, horodaté. 18 échanges sur 4 semaines.
> 1. **Annexe C : échantillons reçus** — les 8 fichiers reçus, en archives chiffrées, avec hashes et analyses.
> 1. **Annexe D : analyse blockchain** — exports Chainalysis du cluster aero_source, graphes de relations, IoC (adresses crypto).
> 1. **Annexe E : logs Russian Market** — les 12 stealer logs Vectris identifiés, métadonnées et extraits pertinents.
> 1. **Annexe F : IoC structurés** — format MISP, prêt pour partage sectoriel après anonymisation.
> 1. **Annexe G : chain of custody** — liste chronologique de toutes les actions d’investigation, signées par Lucas avec horodatage qualifié.
> 1. **Annexe H : note méthodologique** — sources, outils, limites, biais.
> 
> La pochette totale représente ~1,2 Go de données. Stockée sur share chiffré Athéna, accès contrôlé. Versions papier signées du rapport principal.
> 
> Transmission : TLP:RED à Vectris (cellule de crise + RSSI), TLP:AMBER à la DGSI. La DGSI a indiqué qu’elle transmettra les éléments pertinents à ses partenaires internationaux (notamment si identifications complémentaires d’aero_source émergent via d’autres services).
> 
> La solidité de cette pochette conditionne la solidité des actions défensives et coercitives qui en découleront. Si un jour aero_source est identifié physiquement et interpellé, les preuves collectées par Lucas pourront être remontées dans le dossier d’accusation. Si les données Vectris apparaissent ailleurs ultérieurement, la pochette fournira le baseline pour distinguer leak originel et recirculation.

-----

## PARTIE VI — ANALYSE, RENSEIGNEMENT ET PRODUCTION

> **Ce que cette partie apprend.** Transformer la collecte en renseignement. Méthodes de dé-anonymisation et leurs limites, techniques policières (NIT, honeypots), traçage crypto, pièges analytiques (désinformation, faux drapeaux, biais), production de renseignement actionnable, rédaction de notes analytiques, et panorama des menaces par secteur.
> 
> **Ce qu’elle ne couvre pas.** Les cas d’usage narratifs (Partie VII), les études de cas complètes (Partie VIII), les contre-mesures offensives (hors périmètre).
> 
> **Ce que vous saurez faire après cette partie.** Évaluer la solidité d’une attribution dark web, reconnaître les tentatives de désinformation et les pièges analytiques, transformer des observations brutes en note analytique utile à une direction, et calibrer une réponse défensive par secteur.

-----

### Chapitre 29 — Dé-anonymisation : méthodes et limites

La **dé-anonymisation** — associer un pseudonyme dark web à une identité réelle — est l’un des Graal de l’investigation. Elle est possible, mais rarement facile. Ce chapitre cartographie les méthodes, leurs limites, et les principes de calibration.

#### 29.1 Les grandes catégories d’attaque

**Attaques cryptographiques contre Tor**. En pratique, très rares en investigation. Les attaques théoriques contre le réseau Tor (analyse de trafic globale, compromission massive de relais) nécessitent des capacités d’État et restent pour l’essentiel classifiées. Pour l’analyste CTI privé, cette voie est fermée.

**Erreurs d’OPSEC**. Voie principale d’attribution historique. Un acteur qui réutilise un pseudo entre monde réel et dark web, qui révèle des détails personnels, qui laisse des métadonnées dans ses fichiers — s’auto-dé-anonymise. C’est ainsi qu’Ulbricht et Cazes ont été identifiés. Majoritaire parmi les cas de dé-anonymisation documentés publiquement.

**Corrélation OSINT**. Reconstruction progressive d’une identité par agrégation. Un pseudo sur forum → un email jetable → un profil réutilisé → un repo GitHub → un profil LinkedIn. Chaque étape réduit l’espace des candidats jusqu’à identification.

**Attaques applicatives**. Exploitation de failles d’un service .onion ou de comportements du navigateur de la cible pour faire leaker l’IP réelle. Les **NIT** (Network Investigative Techniques) policières — Ch.30 — en sont l’incarnation.

**Attaques financières**. Traçage blockchain qui remonte jusqu’à un off-ramp KYC. Ch.31.

**Attaques humaines**. Infiltration, informateurs, coopération sous pression de pairs arrêtés. Réservé aux forces de l’ordre mais structurant dans les grandes opérations (Operation Bayonet, Cronos).

#### 29.2 Les signaux d’auto-dé-anonymisation

Les acteurs se trahissent souvent par patterns observables. Les plus fréquents :

**Réutilisation de pseudonymes**. Un acteur utilise le même pseudo ou une variation proche entre dark web et clearnet. Le pseudo apparaît sur GitHub, forums publics, réseaux sociaux, jeux en ligne. Chaque occurrence ajoute des données.

**Métadonnées dans fichiers publiés**. Documents PDF/DOCX avec champ « auteur » renseigné du nom réel. Photos avec données EXIF (GPS, appareil photo, horodatage). Captures d’écran contenant éléments identifiants (notifications, onglets, thème OS personnel).

**Fuseau horaire révélé**. Patterns d’activité cohérents avec un fuseau unique. Un acteur prétendument « américain » actif exclusivement entre 10h et 22h MSK est probablement russophone.

**Langue maternelle révélée**. Tournures, fautes, idiomes trahissent la langue native. Analyse stylométrique automatisée peut corréler multiples pseudos.

**Détails personnels involontaires**. Mentions de villes, d’événements locaux, de traditions culturelles, de sports préférés — chaque détail contraint l’espace d’identification.

**Infrastructure partagée**. Même adresse email jetable pour multiple comptes. Même serveur XMPP. Même registrar/hébergeur pour projets publics et projets clandestins.

**PGP keys stables**. Une clé PGP peut persister sur des années et traverser plusieurs pseudos. Elle est un identifiant cryptographique fort.

**Photos personnelles leaked**. Par vanité, opportunisme, ou sexting, certains acteurs partagent des photos d’eux-mêmes. Reverse image search peut identifier.

**Comptes bancaires / crypto liés au vrai nom**. Les échanges KYC ou les cartes bancaires utilisées pour payer infrastructure exposent l’identité.

#### 29.3 La stylométrie

L’**analyse stylométrique** est l’étude des patterns stylistiques d’un auteur. Appliquée au dark web, elle permet :

- De corréler plusieurs pseudos comme appartenant au même auteur.
- Parfois d’orienter vers une région linguistique (locuteur natif russe ? arabophone ?).
- Exceptionnellement d’associer un texte dark web à un auteur connu (publications académiques, articles, posts publics).

**Techniques** :

- **Analyse de fréquence lexicale** : mots caractéristiques, vocabulaire.
- **Patterns syntaxiques** : structures de phrase, ponctuation, usage majuscules.
- **Fautes récurrentes** : erreurs grammaticales systématiques révélant langue maternelle.
- **Idiomes et expressions** : tournures idiomatiques spécifiques.
- **Métriques informatiques** : n-grams de caractères, distribution de longueur de phrase, type-token ratio.

**Outils** :

- **Signature** (logiciel académique).
- **JGAAP** (Java Graphical Authorship Attribution Program).
- **Stylo** (R package).
- Solutions commerciales dédiées pour grandes entreprises.

**Limites** :

- **Besoin d’un corpus suffisant** : quelques centaines de mots minimum par pseudo, idéalement plusieurs milliers.
- **Fragilité face à modification intentionnelle** : un acteur conscient peut altérer son style.
- **Biais des outils** : beaucoup entraînés sur littérature anglophone, moins fiables sur langues peu documentées.
- **Conclusions probabilistes** : stylométrie fournit un scoring de similarité, jamais une identification certaine.

#### 29.4 L’attribution technique versus attribution personnelle

Distinction fondamentale :

**Attribution technique** : associer un ensemble d’activités à un même acteur (ou cluster d’acteurs coordonnés), sans identifier son identité civile. On sait que « aero_source », « aerosrc », « aero_src » sont probablement un même individu, sans savoir qui il est dans la vie réelle. Utile pour le suivi, la priorisation, la threat intelligence.

**Attribution personnelle** : identifier l’identité civile de l’acteur (nom, localisation, état civil). Beaucoup plus difficile, réservé aux cas aboutis. Nécessaire pour action coercitive (arrestation, poursuite).

Pour l’analyste CTI privé, **l’attribution technique est presque toujours l’objectif réaliste**. L’attribution personnelle relève des forces de l’ordre et des services de renseignement. Le rôle du privé est de fournir la matière à l’attribution personnelle, pas de la produire directement.

#### 29.5 Niveaux de confiance en dé-anonymisation

Comme pour l’attribution APT, utiliser vocabulaire calibré.

**Certain** : preuve directe. Acte ou fichier signé du nom réel de l’acteur, photo claire identifiable, données KYC extraites d’exchange. Rare en investigation privée.

**Très probable** (80-95%) : convergence forte de multiples indicateurs indépendants. Exemple : PGP key + wallet crypto + analyse linguistique + localisation d’activité + photo partielle + pattern temporel — tous cohérents avec un individu spécifique.

**Probable** (55-80%) : convergence d’indicateurs, mais incomplète ou faiblement contraignante. Ex : stylométrie + fuseau horaire + pseudonyme similaire. Plusieurs candidats plausibles.

**Possible** (20-55%) : indicateurs suggestifs mais pas probants. Poursuite d’investigation nécessaire.

**Spéculatif** : hypothèse sans support fort. Utile pour orienter la recherche mais pas pour conclure.

**Indéterminable** : données insuffisantes pour même formuler une hypothèse crédible.

#### 29.6 Fil rouge — DARKSTREAM : attribution technique confirmée, personnelle partielle

> **🌐 DARKSTREAM — Épisode 17 : état de l’attribution**
> 
> Synthèse attribution DARKSTREAM au moment du rapport final :
> 
> **Attribution technique** — Très probable (confidence ~90%) :
> 
> - aero_source (IndustrialLeaks), aerosrc (XSS), aero_src (Exploit.in) = même individu, fondé sur identité PGP, analyse linguistique, chevauchement crypto.
> - Cet acteur est actif depuis ~2 ans sur l’écosystème russophone, profil courtier/IAB intermédiaire.
> - Pas de lien structurel avec APT étatique identifié. Profil purement cybercriminel à motivation financière.
> 
> **Attribution personnelle** — Possible (~30%), partielle :
> 
> - Russophone quasi-certain (linguistique + fuseau horaire + infrastructure + wallet).
> - Localisation probable : Russie européenne ou Bélarus (fuseau + inactivité lors de jours fériés russes).
> - Âge estimé : 25-40 ans (maturité de discours + durée sur l’écosystème).
> - Genre non déterminé (pas de signaux sûrs).
> - **Pas de nom civil identifiable** par l’investigation privée. Les indicateurs convergents pointent vers un profil, pas un individu.
> 
> **Communication à la DGSI** : la DGSI reçoit le dossier technique complet. Elle dispose de capacités additionnelles (coopération SIGINT, échanges avec services partenaires russes dans le cadre Europol/Interpol, requêtes légales sur exchanges crypto concernant les wallets identifiés). Ces capacités peuvent permettre de pousser plus loin l’attribution personnelle, mais Athéna n’en sera pas informée.
> 
> **Pour Vectris** : l’attribution technique suffit pour l’action défensive (monitoring, durcissement, communication). L’attribution personnelle, même si elle advenait, ne changerait pas immédiatement les actions. Elle pourrait servir ultérieurement pour d’éventuelles poursuites civiles internationales (procédure longue et coûteuse, rarement aboutissable contre un acteur russe dans le contexte géopolitique 2025-2026).

-----

### Chapitre 30 — NIT, honeypots et infiltration policière

Ce chapitre couvre les techniques **policières** de dé-anonymisation et d’infiltration. Même si elles ne sont pas accessibles aux analystes privés, les comprendre est essentiel pour deux raisons : elles expliquent comment les grandes saisies ont été possibles, et elles informent la vigilance OPSEC des analystes (qui peuvent eux-mêmes être ciblés par erreur ou par ciblage adversaire).

#### 30.1 NIT — Network Investigative Techniques

Les **NIT** sont des techniques techniques utilisées par les forces de l’ordre (principalement FBI historiquement) pour identifier les IPs réelles d’utilisateurs Tor, par exploitation de vulnérabilités.

**Principe général** : le FBI (ou équivalent) prend le contrôle d’un service .onion (via saisie précédente du serveur, ou infiltration de l’opérateur), puis injecte dans les pages servies un **exploit** qui cible le navigateur de la victime. L’exploit fait exécuter du code sur la machine de la victime et provoque une communication hors-Tor vers un serveur FBI, révélant l’IP réelle.

**Opération Playpen (2015)** — référence historique. Le FBI saisit Playpen (site CSAM .onion), continue son opération pendant **deux semaines** depuis ses propres serveurs, et déploie une NIT contre les visiteurs. Résultat : plus de 1 000 IPs identifiées aux US, des centaines d’autres à l’international. **Des centaines d’arrestations** découlent de cette opération.

Controverses Playpen :

- Légalité contestée — le FBI a opéré un site criminel actif pendant deux semaines pour tendre le piège.
- Jurisprudence complexe — plusieurs condamnations ont été annulées en appel sur des motifs procéduraux (warrant unique couvrant multiple juridictions).
- Révélation des techniques — le FBI a fait appel jusqu’à la Cour Suprême pour éviter de divulguer le code exploit utilisé, que les avocats de défense exigeaient pour vérifier son fonctionnement.

**Opération Pacifier (lié à Playpen)**. Suite d’opérations mondiales coordonnées.

**Freedom Hosting saisie (2013)**. Le FBI avait saisi Freedom Hosting (hébergeur de nombreux .onion CSAM) et injecté une NIT dans les pages servies. Exploit ciblait Tor Browser / Firefox ESR de l’époque. Efficace sur les utilisateurs en mode non-Safest.

**Leçon OPSEC**. Tor Browser en **mode Safest** (JavaScript désactivé) neutralise la quasi-totalité des NIT documentées, qui reposent sur exécution de JavaScript pour déployer l’exploit. C’est pourquoi tout analyste investigant le dark web opère en Safest par défaut.

#### 30.2 Les honeypots

Un **honeypot** est un service déployé intentionnellement pour attirer et observer les attaquants / visiteurs suspects.

**Honeypot CSAM** (plusieurs cas documentés). Les autorités créent ou prennent le contrôle de services qui attirent les criminels de cette catégorie. Collecte d’IPs, identification, arrestations.

**Honeypot marketplace / forum**. Un marché « trop beau pour être vrai » (prix cassés, vendeurs toujours disponibles, fonctionnalités inhabituelles) peut être un honeypot. Difficile à confirmer pour les participants.

**Honeypot accès corporate**. Défenseurs déploient des systèmes qui ressemblent à des cibles attractives (RDP, VPN, Citrix) pour capturer les tentatives et étudier les TTPs. Côté défensif, moins investigatif offensif.

**Sentinels et watermarks**. Versions des outils ou données avec markers individuels. Un acheteur d’un dump peut recevoir une copie avec un identifiant spécifique — si ce dump apparaît ailleurs, l’identifiant révèle qui l’a revendu.

#### 30.3 Les infiltrations coordonnées

Les grandes opérations policières combinent plusieurs techniques sur la durée.

**Operation Bayonet (AlphaBay + Hansa, 2017)** — cas d’école. Ch.2 a décrit la séquence : saisie AlphaBay + prise de contrôle de Hansa + opération silencieuse de 30 jours pour capter les migrants, puis annonce simultanée. L’infiltration a nécessité :

- Identification préalable de Cazes (opérateur AlphaBay) via ses erreurs OPSEC.
- Identification de l’infrastructure Hansa via investigation technique.
- Coordination internationale (FBI US, DEA, Police Nationale néerlandaise, Europol, agences de 7 pays).
- Secrecy opérationnelle pendant des mois.

**Operation Cronos (LockBit, 2024)**. Coordination NCA UK, FBI, Europol, forces de 10+ pays. Saisie d’infrastructure LockBit, identification de Dmitry Khoroshev comme LockBitSupp, publication de clés de déchiffrement. Amorcé par années d’investigation technique et humaine.

**Operation Endgame (2024)**. Opération Europol ciblant multiple botnets et infostealers. Démantèlement simultané de plusieurs infrastructures.

**Operation Cookie Monster (Genesis Market, 2023)**. Coordination FBI, Europol, forces de 17 pays. Saisie du marché de logs, arrestations de 120+ utilisateurs, identification de dizaines de milliers d’acheteurs.

**Kidflix (mars 2025)**. Opération contre plateforme CSAM. Démantèlement et arrestations internationales coordonnées.

**BreachForums (multiple saisies)**. Plusieurs saisies successives (mars 2023 avec Pompompurin arrêté, juillet 2024 avec Baphomet arrêté, reprise par ShinyHunters puis nouvelles actions).

Ces opérations illustrent la **capacité croissante** des autorités à coordonner des actions à échelle mondiale. Pour un acteur du dark web, la marge d’opération se réduit.

#### 30.4 L’infiltration humaine

Au-delà des moyens techniques, l’infiltration humaine reste un pilier.

**Agents infiltrés**. Un officier se crée une persona dans l’écosystème et monte progressivement. Rare en pratique (coût et risques élevés), mais pratiqué. Limité aux forces de l’ordre.

**Coopération de sources arrêtées**. Un acteur arrêté peut coopérer en échange de réduction de peine. Fournit informations sur ses contacts, ses méthodes, ses partenaires. Multiplie les arrestations en cascade.

**Informateurs**. Acteurs qui coopèrent préventivement, parfois pour éliminer des concurrents, parfois par repentir, parfois par pression discrète.

**Trolling stratégique**. Semer le doute dans une communauté — faire croire à une infiltration, créer conflits internes, déstabiliser la confiance. Peut provoquer exit scams ou fractures communautaires.

#### 30.5 Les hacks et deep leaks

Certaines enquêtes bénéficient de **leaks externes** non-autorisés.

**ContiLeaks (2022)**. Un dissident interne de Conti (possiblement ukrainien, en réaction à l’alignement de Conti avec la position russe sur la guerre en Ukraine) a publié massivement les communications internes du groupe. Des dizaines de milliers de messages, les outils, les discussions opérationnelles. **Révélations** : structure hiérarchique, montants traités, liens présumés avec FSB. Impact investigatif immense — Conti a dû se restructurer (via reformulation en multiple groupes affiliés).

**Leak de chats LockBit post-Cronos**. Communications internes révélées par les autorités dans le cadre d’Operation Cronos.

**Autres leaks**. Babuk (2021), Lapsus$ (2022 via membres arrêtés), et d’autres — chaque leak apporte une richesse investigative considérable.

**Ironie du dark web** : les groupes qui vivent de la fuite des données d’autrui sont eux-mêmes victimes de leaks qui les exposent. L’écosystème est fondamentalement hostile — alliances précaires, dissidents fréquents.

#### 30.6 Implications pour l’analyste privé

L’analyste ne mène pas d’opérations offensives ni d’infiltration active. Mais il doit :

**Comprendre ces capacités**. Pour ne pas sur-attribuer à l’analyse privée ce qui relève des services publics. Une investigation privée ne démantèle pas un groupe ransomware — elle documente.

**Collaborer avec les autorités**. Les capacités privées et publiques sont complémentaires. Le privé observe en grand, remonte les signaux, contextualise. Le public peut agir coercitivement.

**Maintenir OPSEC défensive**. Les mêmes techniques (NIT, honeypots, infiltration) peuvent être utilisées par adversaires (APT étatiques, criminels sophistiqués) contre les analystes. Mode Safest, machines isolées, identités cloisonnées — les règles s’appliquent.

**Suivre l’actualité des grandes opérations**. Chaque Operation Cronos, Bayonet, Cookie Monster change la configuration de l’écosystème. Un analyste qui les suit anticipe les migrations d’acteurs.

-----

### Chapitre 31 — Traçage crypto et analyse financière

Le **traçage crypto** est l’un des outils les plus puissants d’investigation dark web. Couvert en profondeur dans le cours **OSINT Crypto** de la bibliothèque ; ce chapitre donne l’essentiel applicable au dark web.

#### 31.1 Le paradoxe de Bitcoin

Bitcoin est **pseudonyme**, pas anonyme (Ch.8). Les transactions sont publiques et permanentes. Cette transparence est un **cadeau** pour les investigateurs — tout ce qui circule sur Bitcoin est archivé à jamais.

**Conséquences** :

- Une adresse BTC affichée publiquement sur un forum dark web est un **identifiant à vie**. Son historique est entièrement traçable.
- Une transaction d’il y a 5 ans est analysable aujourd’hui.
- Les techniques de clustering identifient les **autres adresses** probablement contrôlées par le même acteur.
- Les flux vers des exchanges KYC donnent des points d’**attribution personnelle**.

C’est pourquoi les acteurs sérieux migrent vers Monero ou mixers. Mais beaucoup continuent d’utiliser BTC par commodité, créant des opportunités pour les investigateurs.

#### 31.2 Outils de traçage crypto

**Plateformes commerciales** (leaders du marché) :

- **Chainalysis** (Reactor, KYT) : standard de l’industrie. Labellisation massive d’adresses, UI puissante. Utilisé par FBI, DOJ, multiple exchanges majeurs.
- **TRM Labs** (Forensics, Know Your VASP) : concurrent solide, focus compliance et investigation.
- **Elliptic** (Navigator, Discovery) : autre leader, labellisation et graphing.
- **CipherTrace** (maintenant Mastercard).
- **Crystal** (Bitfury).
- **Merkle Science**.

**Outils open source et gratuits** :

- **Blockchain explorers** : Blockstream.info, Mempool.space (Bitcoin), Etherscan (Ethereum), Tronscan (TRON), BlockChair (multi-chain). Gratuits, informations brutes.
- **Breadcrumbs.app** : interface graphique pour exploration, version gratuite limitée.
- **OXT (OpenX Tools)** : outil communautaire pour Bitcoin, analyses heuristiques.
- **WalletExplorer** : clustering basique Bitcoin.

**Les plateformes commerciales coûtent 50 k - 500 k USD/an** et sont nécessaires pour investigation professionnelle. Les outils open source suffisent pour cas ponctuels.

#### 31.3 Heuristiques de clustering

Les outils ne se contentent pas de montrer les transactions — ils **regroupent** les adresses contrôlées probablement par le même acteur.

**Heuristique de co-dépense (multi-input)**. Si une transaction inclut plusieurs inputs d’adresses différentes, elles sont probablement contrôlées par la même entité (le détenteur des clés privées). Heuristique forte historiquement, moins absolue avec les CoinJoin.

**Heuristique de change**. Une transaction typique a un output vers le destinataire + un output de change (retour) vers le payeur. Identifier l’adresse de change permet de poursuivre la chaîne.

**Heuristique temporelle**. Adresses actives dans les mêmes fenêtres temporelles, avec patterns cohérents.

**Heuristique de montants ronds**. Si une transaction envoie un montant rond, l’autre output est probablement le change.

**Heuristique de réutilisation**. Certains wallets réutilisent les adresses (mauvaise pratique), créant des clusters évidents.

**Limites** : ces heuristiques produisent des clusters **probabilistes**, pas certains. Un CoinJoin peut casser l’heuristique multi-input. Les wallets modernes (Electrum, Wasabi) emploient des techniques qui complique le clustering.

#### 31.4 Labellisation

Les plateformes maintiennent des bases de données d’adresses **labellisées** — associées à un acteur ou service connu.

**Labels typiques** :

- **Exchanges** : Binance, Coinbase, Kraken, OKX, etc. — avec adresses hot wallet et cold wallet identifiées.
- **Mixers** : Tornado Cash (Ethereum), Wasabi, Samourai (Bitcoin).
- **Darknet markets** : adresses actuelles et historiques de Hydra, AlphaBay, Silk Road, etc.
- **Ransomware groups** : adresses de collecte de LockBit, Conti, ALPHV, Black Basta, etc.
- **Scammers** : adresses documentées comme impliquées dans fraudes.
- **Sanctionnés OFAC** : Tornado Cash, Garantex, Suex, multiple adresses individuelles.
- **Criminels identifiés** : adresses liées à individus inculpés publiquement.

Ces labels alimentent l’analyse. Si une adresse suspecte envoie des fonds à une adresse labellisée « Binance hot wallet », on sait que les fonds sont transités par Binance — potentiel point de requête légale pour KYC.

#### 31.5 Le blanchiment et ses patterns

Comprendre comment les criminels tentent d’échapper au traçage aide à le contrer.

**Mixers et tumblers**. Envoi à un mixer, réception depuis le pool. Casse le lien direct. Mais : les mixers sont surveillés, sanctionnés, parfois saisis. Les entrées/sorties d’un mixer sont visibles — un cluster qui utilise massivement Tornado Cash est labellisé « mixer user ».

**Chain hopping**. Conversion BTC → ETH → autre chain → retour BTC, via exchanges ou DEX. Complique le traçage car change de blockchain, mais les outils modernes suivent cross-chain.

**Monero swaps**. Conversion BTC → XMR via exchange ou atomic swap. Une fois en XMR, quasi-intraçable. Revient en BTC après, chemin interrompu.

**Layering** : multiples transferts entre wallets contrôlés avant de sortir. Augmente la complexité d’analyse mais pas insurmontable.

**Off-ramp via exchange KYC**. La sortie en fiat reste le point faible. Passage par un exchange avec KYC — l’identité est accessible via requête légale.

**Off-ramp via P2P / OTC non-KYC**. Dans des juridictions peu régulées. Plus discret mais volumes limités, ou commissions élevées.

**Achats directs**. Immobilier en crypto, voitures, luxe. Dans juridictions qui l’acceptent, peut éviter la conversion fiat.

#### 31.6 Les saisies réussies

Quelques cas emblématiques montrent l’efficacité du traçage.

**Bitcoin Colonial Pipeline (juin 2021)**. Le FBI récupère ~2,3 M USD des 4,4 M USD de rançon payés à DarkSide, via identification et saisie des clés privées d’une adresse de réception. Spectaculaire.

**Bitfinex (février 2022)**. DOJ saisit **3,6 milliards USD** en crypto (prix du moment), liés au hack Bitfinex de 2016. Identification via analyse blockchain après que Ilya Lichtenstein et Heather Morgan ont tenté de blanchir les fonds.

**Chipmixer (mars 2023)**. Saisie du mixer, avec 46 000 BTC (~2,73 Mrd EUR à l’époque) saisis ou traçables.

**Samourai Wallet (avril 2024)**. Fondateurs (Keonne Rodriguez et William Hill) inculpés, infrastructure saisie.

**Tornado Cash**. Sanctionné par OFAC (août 2022). Multiple inculpations des développeurs : Alexey Pertsev (Pays-Bas, condamné mai 2024), Roman Storm (US, procès en cours).

**Suex, Garantex, Bitzlato** : exchanges non-KYC ou à KYC faible sanctionnés par OFAC pour facilitation de blanchiment criminel.

Ces cas montrent que le **traçage fonctionne** — avec ressources, patience, et coopération internationale. Le criminel sophistiqué n’est pas invulnérable, juste plus difficile à attraper.

#### 31.7 L’intégration dans l’investigation dark web

Pour l’analyste CTI investigant sur le dark web, le traçage crypto est un **pivot** puissant.

**Workflow type** :

1. **Observer une adresse** sur post forum, profil vendeur, paiement ransomware.
1. **Rechercher dans plateforme** (Chainalysis/TRM/Elliptic) — labels existants, cluster.
1. **Analyser historique** — transactions reçues, envoyées, comportement typique.
1. **Suivre les flux** — vers où vont les fonds ? Exchange ? Mixer ? Autre wallet ?
1. **Identifier points d’attribution** — passages par exchange KYC comme angles pour futures requêtes légales (via autorités).
1. **Cartographier cluster** — autres adresses probablement contrôlées, mises en relation avec autres acteurs.

**Intégration dans rapport** : adresses observées listées comme IoC, graphes de flux, identification des exchanges traversés, évaluation du profil financier (volumes, fréquence, patterns).

Le cours **OSINT Crypto** couvre cette discipline en profondeur.

-----

### Chapitre 32 — Pièges analytiques, désinformation et faux signaux

L’investigation dark web opère dans un environnement **hostile** où les acteurs cherchent activement à tromper, désinformer, piéger. Ce chapitre cartographie les pièges et les contre-mesures.

#### 32.1 Les biais analytiques

**Biais de confirmation**. Une fois une hypothèse formée, on cherche les preuves qui la confirment et on minimise les preuves qui la contredisent. Classique et puissant.

**Mitigation** : formuler explicitement l’hypothèse, puis lister activement ce qui l’infirmerait. ACH (Analysis of Competing Hypotheses) formalise cette discipline.

**Biais d’ancrage**. La première information reçue colore l’interprétation de toute la suite. Si le premier poster du cas a dit « c’est Lazarus », on cherche inconsciemment ce qui va dans ce sens.

**Mitigation** : réévaluer périodiquement depuis zéro. Faire re-présenter le cas par un collègue qui n’a pas été exposé à l’hypothèse initiale.

**Biais de disponibilité**. Ce qui est visible et récent semble plus important. Un groupe ransomware médiatisé la semaine dernière paraît plus menaçant qu’un groupe discret mais plus dangereux.

**Mitigation** : données quantitatives plutôt qu’impressions. Statistiques de ransomfeed, rapports sectoriels.

**Biais d’autorité**. On fait plus confiance à ce que dit un vendor CTI réputé qu’à ce que dit un chercheur indépendant. Parfois justifié, parfois pas.

**Mitigation** : évaluer les sources sur leur mérite, pas leur réputation. Un vendor réputé peut se tromper ; un chercheur indépendant peut voir juste.

**Biais de cohérence narrative**. On préfère les histoires qui font sens (« cet acteur est un agent russe qui cible la défense européenne ») aux histoires messy (« cet acteur est un opportuniste qui a acheté un accès revendu, peut-être revendra lui-même, motivation incertaine »). La réalité est souvent messy.

**Mitigation** : accepter l’ambiguïté. Ne pas sur-narrativiser.

**Biais géopolitique**. Face à un acteur russe, on tend à sur-attribuer à un État. Face à un acteur chinois, idem. Ces biais ne sont pas infondés (beaucoup d’acteurs sont liés à des États), mais ne doivent pas devenir automatiques.

**Mitigation** : évaluer chaque cas sur ses mérites, avec multiples hypothèses explicites.

#### 32.2 La désinformation active

Les acteurs malveillants produisent intentionnellement de la désinformation pour tromper analystes et autorités.

**Faux drapeaux (false flags)**. Un acteur se fait passer pour un autre — imite un TTP, utilise un pseudonyme inspiré d’un acteur connu, plante des indices pointant vers un tiers innocent.

Cas emblématique : **Olympic Destroyer (2018)**. Sandworm (GRU russe) inclut des fragments de code Lazarus + artefacts chinois dans son malware déployé pendant les JO de PyeongChang. Analyse minutieuse (Kaspersky) a identifié les faux indices et consolidé l’attribution russe — mais des vendeurs moins attentifs ont initialement pointé vers DPRK.

**Recyclage et fabrication**. Publication de données « fraîchement volées » qui sont en fait anciennes (recyclage) ou fabriquées (composition de différents breaches anciens + données inventées). Donne l’impression d’un breach récent sans réalité sous-jacente.

**Scam ciblé**. Un vendeur qui prétend offrir un accès à une organisation cible — en réalité, il n’a rien, mais veut vendre du vent à un acheteur crédule (qui pourrait être un investigateur lui-même).

**Amplification artificielle**. Un scam mineur présenté comme breach majeur pour attirer l’attention médiatique. Certains « leak massifs » sont en fait de petites compromissions + inflation.

**Honey traps contre analystes**. Un vendeur qui répond rapidement à l’investigateur, fournit des échantillons crédibles, tente de le conduire dans une direction qui bénéficie à l’acteur (faire porter le chapeau à un concurrent, mettre en avant une cible qui n’est pas réellement ciblée).

#### 32.3 Les pièges techniques

**Fichiers piégés**. Échantillons fournis par un vendeur qui contiennent malware ciblant l’environnement d’analyse. Exploits navigateur pour identifier l’IP. Macros Office malveillantes. PDF avec JS.

**Mitigation** : ouverture uniquement en VM isolée, mode Safest, sandbox, extraction de métadonnées avant exécution.

**Web beacons dans documents**. Documents PDF ou DOCX contenant des ressources externes (images chargées à l’ouverture, iframes). Signal l’ouverture du document à l’acteur, révèle fuseau horaire, potentiellement IP (si ressource chargée hors VPN/Tor).

**Mitigation** : ouverture offline, airplane mode avant ouverture, analyse des ressources liées avant d’ouvrir.

**URLs piégées**. Liens pointant vers pages avec exploits navigateur. Toujours investiguer en mode Safest.

**Telegram / XMPP avec read receipts**. Certaines messageries confirment lecture/livraison. L’adversaire sait quand son message a été lu — informe sur fuseau horaire, disponibilité. **Mitigation** : désactiver read receipts si possible, lire en offline puis se connecter (pour certains protocoles).

**Watermarks individualisés**. Un échantillon fourni à un « acheteur » peut contenir un marker unique qui l’identifie. Si l’analyste le rediffuse (à la victime, à la DGSI), l’acteur peut tracer via qui a diffusé. **Mitigation** : re-création des documents analysés, suppression d’éléments potentiellement markers.

#### 32.4 Les patterns de désinformation

**Narratifs coordonnés**. Plusieurs comptes (sock puppets) diffusent le même narratif sur différentes plateformes pour créer une impression de consensus communautaire. Classique dans hacktivisme et influence.

**Pseudo-leaks**. Fausses fuites conçues pour influencer. Données fabriquées qui contiennent des éléments plausibles + éléments orientés (accusant un tiers, poussant un agenda).

**Attribution fausse**. Certains acteurs s’attribuent délibérément des opérations qu’ils n’ont pas conduites (pour se faire de la pub) ou attribuent à d’autres leurs propres opérations (pour se protéger).

**Timing manipulé**. Publication d’un leak juste avant un événement politique, financier, médiatique — pour maximiser l’impact et suggérer un lien narratif.

#### 32.5 Contre-mesures analytiques

**Multi-source**. Ne jamais conclure sur une source unique. Crosscheck avec 2-3 sources indépendantes avant de considérer un fait établi.

**Validation indépendante**. Si un vendeur dit « j’ai X », demander échantillon. Si un vendor dit « APT tel a fait ci », voir si d’autres vendors concordent.

**ACH systématique**. Pour chaque attribution non-triviale, poser les hypothèses alternatives et les tester.

**Vocabulaire calibré**. WEP (Words of Estimative Probability) utilisé systématiquement.

**Documentation du doute**. Rapport analytique inclut section « limites et incertitudes » — honnête sur ce qui n’est pas certain.

**Review par pairs**. Un collègue qui lit un rapport avec œil neuf détecte souvent biais et sauts logiques.

**Red teaming analytique**. Demander à un collègue de jouer l’avocat du diable, tester les conclusions.

**Revisite temporelle**. Relire le rapport 48h après rédaction. Beaucoup de biais apparaissent avec recul.

#### 32.6 Les alertes classiques

Signaux qu’une observation est peut-être manipulée.

**« Trop beau pour être vrai »**. Un vendeur trop coopérant, un échantillon trop complet, une identification trop facile. Si l’investigation avance vite et loin, suspicion.

**Convergence trop parfaite**. Tous les indicateurs pointent dans la même direction, sans bruit. Le monde réel est messy ; une convergence parfaite est suspecte.

**Narratif qui « sert » quelqu’un**. Si l’attribution pointe commodément vers un acteur déjà stigmatisé, suspicion d’un false flag.

**Timing opportun**. Un leak qui arrive juste avant une échéance sensible, dans un contexte politiquement chargé.

**Source unique**. Un fait entier repose sur une seule source, même si réputée.

**Pression temporelle artificielle**. « Il faut conclure vite, avant la reunion board demain ». Les conclusions sous pression temporelle sont plus susceptibles à des biais — ralentir autant que possible.

#### 32.7 Fil rouge — DARKSTREAM : écarter les faux drapeaux

> **🌐 DARKSTREAM — Épisode 18 : vérification de l’absence de false flag**
> 
> Avant de finaliser, Lucas vérifie que DARKSTREAM n’est pas un false flag.
> 
> **Hypothèse alternative 1 — aero_source est un APT étatique déguisé**. Vérification : le style linguistique, les patterns d’activité, le profil financier (cluster modeste, flux vers BlackSprut marché de drogues), l’absence de TTP sophistiquée, l’infrastructure grand public (XMPP standard), le prix de vente (65k, dans la norme cybercriminelle) — tous pointent vers profil cybercriminel. **Hypothèse rejetée** (probabilité < 10%).
> 
> **Hypothèse alternative 2 — aero_source essaie de piéger Athéna**. Vérification : les échantillons fournis ne contiennent pas de watermarks détectés. Pas d’exploits identifiés. Communications cohérentes (pas d’over-cooperation suspecte). **Possible mais improbable** (les markers intentionnels sont rares chez acteurs de ce niveau).
> 
> **Hypothèse alternative 3 — le dump n’est pas réellement Vectris**. Vérification : marker interne Vectris confirmé. Cohérence avec forensics Mandiant côté victime. **Rejetée** avec très haute confiance.
> 
> **Hypothèse alternative 4 — aero_source est un proxy d’un acteur plus grand**. Vérification : style cohérent d’un acteur individuel (vs patterns de grande équipe), historique transactionnel personnel, comportement opportuniste (pas stratégique). **Possible (~25%)** mais sans support fort.
> 
> Lucas documente ces vérifications dans le rapport, section « limites et incertitudes ». Le rapport final conclut avec un profil cybercriminel individuel à haute confiance, mais note explicitement que la revente ultérieure à un acteur étatique est une hypothèse qui reste ouverte. La DGSI appréciera cette calibration.

-----

### Chapitre 33 — Transformer les observations en renseignement actionnable

La différence entre un analyste qui **observe** et un analyste qui **produit du renseignement** tient dans la capacité à transformer les observations brutes en **informations actionnables** — actions défensives concrètes, décisions de direction, priorisations.

#### 33.1 Qu’est-ce que l’« actionnabilité »

Une observation est **actionnable** si elle peut déclencher une action concrète par un destinataire identifié. Sans destinataire et sans action, une observation est juste du bruit, même si intéressante.

**Tests d’actionnabilité** :

- **Qui** est le destinataire ? (SOC, RSSI, direction, juridique, métier)
- **Quelle action** attendue ? (ajouter une règle de détection, isoler un poste, notifier une autorité, communiquer à un client, décider d’une investigation)
- **Dans quelle temporalité** ? (immédiat, dans la journée, dans la semaine)
- **Avec quels ressources** ? (techniques, humaines, budgétaires)

Une observation qui ne passe aucun de ces tests n’est pas actionnable — elle peut nourrir la veille générale, mais ne mérite pas de rapport dédié ou d’escalade.

#### 33.2 Les types de renseignement et leurs destinataires

Classification héritée de la doctrine militaire, adaptée au CTI.

**Renseignement tactique**. Court terme, opérationnel. Destinataire : SOC, équipe IR.

- Nouveaux IoC à ajouter dans les outils.
- TTP observés à monitorer.
- Signatures malware fraîchement publiées.
- Alerting sur menace immédiate.

**Renseignement opérationnel**. Moyen terme, gestion. Destinataire : RSSI, direction sécurité.

- Tendances dans les campagnes ciblant l’organisation ou son secteur.
- Évolution des groupes menaçants.
- Qualité de la posture défensive vs menaces observées.
- Priorisation des investissements sécurité.

**Renseignement stratégique**. Long terme, direction. Destinataire : DG, conseil d’administration.

- Paysage macro des menaces cyber pour l’organisation.
- Implications business des tendances (nouvelles géographies de risque, nouveaux secteurs ciblés).
- Ajustements de stratégie, M&A avec dimension cyber, décisions d’investissement.

**Renseignement réputationnel**. Destinataire : direction communication, juridique.

- Surveillance de mentions de la marque dans contexte criminel.
- Détection d’impersonations, deepfakes, phishing abusant la marque.
- Alerte sur possibles exfiltrations qui pourraient devenir publiques.

#### 33.3 Le cycle du renseignement

Cycle classique adapté au CTI dark web.

**Étape 1 — Direction (Direction)**. Le donneur d’ordre (CISO, DG) définit les priorités : quels acteurs surveiller, quels secteurs, quels scénarios. Sans direction claire, la veille devient généraliste et peu utile.

**Étape 2 — Collecte (Collection)**. Acquisition des observations (Partie V). Selon les priorités définies, focus sur sources pertinentes.

**Étape 3 — Traitement (Processing)**. Nettoyage, dé-duplication, normalisation des observations. Triage, qualification (scam/recyclage/authentique), enrichissement initial.

**Étape 4 — Analyse (Analysis)**. Le cœur du métier. Transformation des observations en insights. Corrélation, pivoting, attribution, tendances.

**Étape 5 — Diffusion (Dissemination)**. Production de livrables adaptés aux destinataires, avec format et niveau approprié. Actionnabilité explicite.

**Étape 6 — Feedback (Evaluation)**. Les destinataires retournent leurs observations — l’action a-t-elle été déclenchée ? Utile ou pas ? Manque quelque chose ? Feedback alimente la direction du cycle suivant.

Ce cycle est **continu et récursif**, pas linéaire. Une observation peut provoquer un nouveau besoin de direction.

#### 33.4 Les exigences de qualité du renseignement

**Pertinence**. Le renseignement doit répondre à un besoin du destinataire. Un rapport brillant sur un groupe ransomware ciblant exclusivement la santé américaine est peu pertinent pour un équipementier aerospace français.

**Actualité**. Un renseignement daté est moins précieux. Un leak site qui affichait Vectris hier intéresse énormément ; un leak site qui l’affichait il y a 18 mois intéresse moins (contexte historique uniquement).

**Précision**. Factuel et vérifiable. Éviter les généralités non-sourcées.

**Complétude**. Le renseignement couvre les aspects nécessaires pour l’action. Un rapport qui dit « vous êtes ciblés » sans préciser **qui, comment, avec quelle urgence** laisse le destinataire sans capacité d’action.

**Calibration**. Incertitudes explicitées. WEP utilisés. Sources identifiées (au niveau de confidentialité approprié).

**Lisibilité**. Format adapté au destinataire. SOC veut des IoC techniques ; direction veut impact business.

**Neutralité**. Factuel, sans biais idéologique ou commercial. Le renseignement interne ne sert pas à « vendre » plus de sécurité — il informe objectivement.

#### 33.5 La transformation pratique

**Exemple 1 — Observation brute** : « Post sur IndustrialLeaks : un vendeur aero_source propose 420 Go de données d’un équipementier aerospace EU à 65 000 USDT ».

**Transformation en renseignement** :

- Tactique (SOC) : surveillance renforcée sur les comptes Vectris, monitoring exfiltrations, IoC ajouts si adresses crypto ou pseudonymes identifiés.
- Opérationnel (RSSI) : confirmation de la compromission, priorités de remédiation, coordination avec prestataires IR, notification autorités.
- Stratégique (DG) : évaluation impact business, communication clients/partenaires, décision de payer ou non (le cas échéant), stratégie de crise.

Chaque destinataire reçoit une version adaptée du même constat, avec vocabulaire et actionnabilité pertinents.

**Exemple 2 — Observation brute** : « Tendance observée sur les marchés de logs : augmentation de 40% des logs contenant tokens cloud AWS/Azure au T3 2025 ».

**Transformation en renseignement** :

- Tactique : règles SOC de détection d’abus de tokens cloud.
- Opérationnel : audit des politiques IAM cloud, priorisation sur la rotation de tokens, durcissement conditional access.
- Stratégique : investissement dans CSPM et CNAPP, formation cloud security pour équipes dev.

#### 33.6 Les erreurs typiques

**Rapport encyclopédique**. Rapport de 80 pages qui couvre tout, tout est intéressant, rien n’est actionnable. Le destinataire le range et l’oublie. Préférer des rapports courts ciblés.

**Jargon impénétrable**. Surdosage d’acronymes, de références techniques incompréhensibles pour non-spécialistes. Particulièrement pour direction qui veut comprendre l’enjeu business.

**Ton alarmiste**. Sur-dramatisation pour obtenir des ressources. Fonctionne une fois, érode la crédibilité sur le long terme. Calibration honnête gagne toujours.

**Manque de contexte**. Observation présentée sans quoi c’est important, ni pourquoi maintenant. « LockBit affiche 12 nouvelles victimes ce mois » — et alors ? Traduction : cette intensification pourrait indiquer recrutement d’affiliés post-Cronos, ce qui affecte la probabilité de ciblage.

**Absence de recommandations**. Observations précises, analyse solide, mais pas de « et donc, il faut faire X ». Laisse le destinataire sans guide. Chaque rapport doit se terminer par actions proposées.

**Over-recommendations**. Au contraire, liste de 50 recommandations sans priorisation. Destinataire submergé, rien ne bouge. Limiter à 3-5 actions prioritaires, avec séquence claire.

**Non-suivi**. Le rapport est produit, puis le lien se perd. Pas de check post-livraison sur actions engagées. Le cycle feedback doit être explicite.

-----

### Chapitre 34 — Produire une note analytique

Forme pratique de livraison du renseignement. La **note analytique** (ou « intel note ») est le livrable type de l’analyste CTI. Ce chapitre couvre les conventions, la structure, et les pièges de rédaction.

#### 34.1 Les types de notes

**Flash alert**. Note très courte (1-2 pages), livraison immédiate sur événement important. Exemple : un leak site affiche une victime critique, un 0-day exploité massivement. Ton : urgent. Action : immédiate.

**Intel note**. Note standard (3-8 pages), livraison régulière sur observations significatives. Exemple : investigation DARKSTREAM. Ton : structuré. Action : planifiée.

**Bulletin sectoriel**. Note périodique (10-30 pages), synthèse des tendances dans un secteur. Souvent mensuelle ou trimestrielle. Exemple : « Menaces dark web contre secteur aerospace T3 2025 ». Ton : analytique. Action : stratégique.

**Note stratégique**. Note de fond (15-50 pages), vision long terme. Rare (1-4 par an). Destinée à direction. Exemple : « Évolution de l’écosystème cybercriminel 2020-2026 et implications pour Vectris ».

**Advisory**. Communication publique ou semi-publique sur menace spécifique. Format court, diffusion large (ISAC, communauté CTI). Exemple : « Campagne de phishing ciblée aerospace — IoC et mesures recommandées ».

#### 34.2 Structure standard d’une intel note

**En-tête**. Titre clair et précis, date de rédaction, auteur, destinataires, **classification TLP**, version/révision.

**Executive summary** (⅓-½ page). Réponse aux questions « so what ? » et « now what ? ». Le lecteur pressé ne lit que cette section — elle doit être suffisante.

- Qu’est-ce qui a été observé ?
- Pourquoi c’est important ?
- Qu’est-ce qu’il faut faire ?
- Quel niveau de confiance ?

**Contexte**. Pourquoi cette note est-elle produite ? Quel événement déclencheur ? Quelles observations antérieures pertinentes ?

**Observations**. Faits observés, avec sources et horodatages. Ton factuel, pas interprétatif ici.

**Analyse**. Interprétation des observations. Attribution, motivations, chaîne d’événements, liens avec autres renseignements. Ton analytique, WEP utilisés.

**Implications**. Pourquoi c’est important pour le destinataire. Risques concrets, impacts potentiels.

**Recommandations**. Actions concrètes, priorisées, avec destinataires et délais. Section la plus actionnable.

**Limites et incertitudes**. Ce qui n’est pas connu, ce qui pourrait changer l’analyse. Honnêteté méthodologique.

**Annexes**. IoC, détails techniques, captures, timelines détaillées, références.

#### 34.3 Les règles de rédaction

**Clarté avant tout**. Phrases courtes, vocabulaire précis. Acronymes introduits avant usage. Pas de jargon non-nécessaire.

**Structure logique**. Chaque section répond à une question précise. Le lecteur doit pouvoir naviguer par table des matières.

**Factualité**. Distinction nette entre observation et interprétation. « Le vendeur a publié un échantillon » (observation) vs « le vendeur est un russophone professionnel » (interprétation fondée sur observations listées).

**Calibration**. WEP systématiques. Pas de « certain » sans preuve directe, pas de « impossible » sans démonstration.

**Sources**. Chaque observation est sourcée (URL .onion, forum/post ID, outil utilisé, plateforme). Niveau de détail adapté au TLP — à TLP RED, on peut détailler ; à TLP CLEAR, généralisation.

**Actionnabilité**. Chaque section « observations » et « implications » est suivie d’une conclusion exploitable, pas juste descriptive.

**Neutralité**. Pas de jugements moraux (« ces criminels répugnants… »). Pas de bias idéologique. Pas de « vendre » plus de sécurité à sa direction.

**Révisabilité**. Le rapport est une photo d’un instant T. Mentionner date, noter que nouvelles observations peuvent changer l’analyse.

#### 34.4 Les pièges de rédaction

**Trop de détails techniques en exécutif**. L’executive summary pour la direction ne doit pas contenir « SHA-256 hashes a1b2c3… ». Les détails vont en annexes.

**Pas assez de détails pour les techniques**. Inverse — le SOC veut les IoC précis, pas des généralités. Adapter par destinataire.

**Redondance interne**. La même info répétée en executive summary, en analyse, en implications. Chaque section doit apporter quelque chose de différent.

**Over-narrativization**. Raconter une « histoire » trop fluide peut gommer les incertitudes. Le lecteur croit à une certitude que l’auteur n’a pas.

**Omissions politiques**. Éviter de parler d’un risque qui embarrasse la direction (« on a raté la détection depuis 3 mois »). Un rapport honnête peut déplaire mais maintient crédibilité long terme.

**Sur-confidence post-hoc**. Écrit après les faits, l’analyse peut paraître trop facile. Mentionner ce qui était incertain avant action.

**Manque de graphiques / visuels**. Un graphe de chaîne d’attaque, une timeline, un cluster crypto valent 1 000 mots de prose. Utiliser les visuels.

#### 34.5 Le template DARKSTREAM

Exemple concret de structure pour l’investigation DARKSTREAM.

**TITRE** : Opération DARKSTREAM — Investigation sur la circulation dark web des données exfiltrées de Vectris Aerospace — Rapport final

**MÉTADONNÉES** : Auteur Lucas Ferreira, Athéna Group ; Date 15/05/2026 ; Version 1.0 ; Classification TLP:RED ; Destinataires : Cellule crise Vectris + DGSI.

**EXECUTIVE SUMMARY** :

- 420 Go de données Vectris (R&D propulsion, specs défense, bases clients, emails) circulent sur forum russophone IndustrialLeaks.
- Vendeur aero_source, profil cybercriminel russophone individuel, pas d’acteur étatique identifié.
- Chaîne reconstituée : stealer Lumma → log Russian Market → IAB magnit_ru → exfiltration aero_source ou commanditaire.
- Confiance authentification : **très élevée** (marker interne + cohérence forensics).
- Confiance attribution technique : **élevée** (90%+).
- Confiance attribution personnelle : **faible** (identification civile hors d’atteinte de l’investigation privée).
- Menace élevée pour Vectris mais contenue — pas de preuve d’accès étatique actuel.

**CONTEXTE** : déclenchement investigation suite alerte Recorded Future, mandat Athéna + DGSI, 6 semaines d’investigation.

**OBSERVATIONS** :

- Post IndustrialLeaks (date, URL, capture).
- Profil aero_source (8 mois, 12 posts, 2 transactions antérieures).
- Échantillons authentifiés (fichiers, hashes, markers).
- 12 stealer logs Vectris identifiés sur Russian Market.
- Cluster crypto de 40 adresses, ~180 k USDT transactions, flux vers BlackSprut et Garantex (avant sanctions).
- Pseudonymes pivots : aerosrc (XSS), aero_src (Exploit.in).
- PGP commune, linguistique cohérente, fuseau MSK.

**ANALYSE** : [narration structurée de la chaîne, attribution technique, hypothèses alternatives testées et rejetées].

**IMPLICATIONS** :

- Risque de publication totale si non-acheteur trouvé (2-3 mois typiquement).
- Risque de revente à acteur étatique (possible, non déterminable).
- Exposure compliance (notification CNIL pour données personnelles, notification partenaires défense).
- Reputational — prédiction de question médiatique possible.

**RECOMMANDATIONS** :

1. **Immédiat** : poursuite isolation/reset des 3 postes compromis identifiés.
1. **Immédiat** : notification aux 4 partenaires défense concernés.
1. **7 jours** : préparation communication client top-20 (si escalade).
1. **30 jours** : durcissement politique téléchargement logiciels + EDR renforcé R&D.
1. **30 jours** : monitoring IndustrialLeaks continu, alerting sur évolution.
1. **90 jours** : revue complète politique credentials + formation sensibilisation.

**LIMITES** :

- Attribution personnelle impossible via moyens privés.
- Évolution possible (revente à étatique, publication totale) non prédictible.
- Biais possibles : sur-attribution à profil russophone (à confirmer par enrichissement).

**ANNEXES** :
A. Captures IndustrialLeaks (147 screenshots).
B. Conversations XMPP aero_source (18 échanges).
C. Échantillons authentifiés (8 fichiers).
D. Analyse blockchain cluster (graphe).
E. Logs Russian Market (12 logs).
F. IoC structurés MISP.
G. Chain of custody.
H. Note méthodologique.

#### 34.6 La présentation orale

Une note écrite s’accompagne souvent d’une **présentation orale** à la cellule de crise, direction, autorités.

**Format type** : 20-30 minutes présentation + 30-60 min Q&A.

**Structure** :

1. Contexte et déclenchement (2 min).
1. Ce qui a été observé (5 min).
1. Ce que ça veut dire (5 min).
1. Ce qu’il faut faire (5 min).
1. Ce qui reste incertain (3 min).
1. Q&A (le plus long).

**Support** : slides simples, pas de murs de texte. Graphes, timelines, captures emblématiques. Backup slides détaillées pour Q&A.

**Ton** : calme, structuré, calibré. Pas d’alarmisme, pas de minimisation. Accepter de ne pas savoir.

**Audience mixte** : adapter au dénominateur commun. Exécutifs demanderont impact business ; techniques demanderont détails IoC. Satisfaire chaque typologie sans perdre l’autre.

-----

### Chapitre 35 — Menaces dark web par secteur d’activité

Les menaces dark web ne sont pas homogènes — chaque secteur a ses profils de risque. Ce chapitre cartographie les patterns sectoriels observés 2024-2026 pour orienter les postures défensives.

#### 35.1 Services financiers

**Profil** : cible historique de premier rang. Concentre valeur monétaire directe et données sensibles.

**Menaces dominantes** :

- **Carding** et fraude à la carte bancaire. Marchés spécialisés (BriansClub, successeurs), prix 5-150 USD/carte selon qualité.
- **Comptes bancaires compromis** (access credentials + cookies session). Prix 100-1 000 USD selon balance.
- **Fraude à l’identité** : fullz pour ouverture de comptes frauduleux, crédit fraud.
- **Ransomware ciblé banks, assets management, fintech** : rançons élevées, sensibilité régulatoire.
- **Targeted phishing** sur employés clés (trading, IT, SWIFT). Industrialisation via PhaaS.
- **SIM swapping** pour contourner SMS 2FA sur comptes crypto et bancaires.
- **Insiders recrutés sur forums** : le recrutement d’employés de banques pour faciliter fraudes est documenté.

**Acteurs typiques** : groupes RaaS (LockBit, ALPHV, Black Basta ciblent finance régulièrement), carders spécialisés, IAB banking-focused, fraudeurs opportunistes.

**Impacts** : pertes financières directes, impact régulatoire (amendes CNIL/ACPR, sanctions réglementaires), réputationnel, opérationnel (ransomware).

**Priorités défensives** :

- MFA FIDO2 obligatoire (pas SMS).
- Monitoring approfondi des marchés de cartes et logs bancaires.
- Détection de SIM swapping par monitoring téléphonique.
- Veille insiders (anormalités comportement, patterns communications).
- Segmentation forte des systèmes critiques (trading, SWIFT).

#### 35.2 Santé

**Profil** : cible en forte croissance. Combinaison de données sensibles + systèmes critiques + budgets souvent plus faibles en cyber = cible privilégiée.

**Menaces dominantes** :

- **Ransomware** : impact vital (hôpitaux, urgences, PACS), urgence → taux de paiement historiquement élevé (bien que déclinant).
- **Vol de dossiers médicaux** : prix 50-250 USD/dossier US (marché développé), moins en Europe. Usages : fraude assurance, chantage, fraude à l’identité enrichie.
- **PHI (Protected Health Information)** et HIPAA breaches US — obligations de notification publique qui génèrent publicité négative.
- **Ciblage des labos et R&D pharma** : propriété intellectuelle (formules, essais cliniques, brevets).
- **Access to provider networks** : vente d’accès à hôpitaux, cabinets médicaux, cliniques sur forums.

**Cas emblématiques** :

- **Change Healthcare (2024)** : ransomware ALPHV, paiement ~22 M USD, impact massif sur chaîne de remboursements US.
- **Hôpitaux français** : multiples cas 2023-2025 (Corbeil-Essonnes, Versailles, André-Mignot).
- **Synnovis (UK, 2024)** : Qilin, impact sur analyses sanguines NHS Londres.

**Priorités défensives** :

- Backup offline testé et fiable.
- Segmentation IT/OT médicale (PACS, imaging, bloc opératoire).
- Plan de continuité avec procédures dégradées.
- MFA renforcé malgré les contraintes UX des soignants.
- Coopération sectorielle (H-ISAC).

#### 35.3 Industrie / manufacturing

**Profil** : montée en ciblage 2020-2026. Combine OT vulnérable + propriété intellectuelle + supply chain critique.

**Menaces dominantes** :

- **Ransomware** : impact opérationnel direct (arrêt production), pression au paiement.
- **Vol de propriété intellectuelle** : specs, plans, formules. Acheteurs : concurrents, États.
- **Targeted IAB sur OT** : accès aux systèmes SCADA revendus, usage potentiel sabotage ou espionnage.
- **Supply chain attacks** : compromission fournisseur pour atteindre cible en aval.

**Cas emblématiques** :

- **Colonial Pipeline (2021)** : DarkSide, impact infrastructurel US.
- **JBS (2021)** : REvil, impact chaîne alimentaire mondiale.
- **Saint-Gobain, Norsk Hydro, Picoty** : exemples européens de ransomware manufacturing.

**Ciblage aerospace/defense** : particulièrement sensible. DARKSTREAM s’inscrit dans ce segment. Intérêt étatique parfois, intérêt cybercriminel toujours.

**Priorités défensives** :

- Segmentation IT/OT stricte (modèle Purdue).
- Inventaire et patching des OT assets.
- Air-gap ou DMZ pour systèmes critiques.
- Backups offline pour automates et configurations industrielles.
- Partenariats avec CERT sectoriel (ex : France : CERT-IST).

#### 35.4 Énergie et utilities

**Profil** : cible stratégique, souvent OIV. Intérêt étatique potentiel (prépositionnement), cybercriminel (ransomware), hacktiviste (ciblage géopolitique).

**Menaces dominantes** :

- **Pré-positionnement étatique** (Volt Typhoon contre US, patterns similaires contre UE).
- **Ransomware ciblant opérateurs électriques, gaziers, eau** : impact potentiel sur population.
- **Sabotage par hacktivistes** : tentatives contre infrastructure eau (Cyber Av3ngers iraniens contre opérateurs US).
- **Exfiltration de données techniques** : topologie réseau, procédures, fournisseurs.

**Cas emblématiques** :

- **Colonial Pipeline** (cité).
- **Cyber Av3ngers contre Unitronics (2023-2024)** : compromissions opérateurs eau US par défaut-password sur PLC.
- **Multiples incidents ukrainien** (cours APT détaille).

**Priorités défensives** :

- Défense en profondeur IT/OT.
- Monitoring OT spécialisé (Dragos, Claroty, Nozomi).
- Plan de continuité incluant dégradés analogiques.
- Coopération ANSSI / FranceNum / ENTSO-E / E-ISAC.

#### 35.5 Retail et e-commerce

**Profil** : cible de masse pour fraude et credentials volumineux.

**Menaces dominantes** :

- **Credential stuffing** : comptes clients volés revendus.
- **Skimming / Magecart** : injection de JS malveillant dans sites e-commerce pour voler données de paiement.
- **Ransomware** : grandes chaînes ciblées (Marks & Spencer 2025, Co-op 2025, autres).
- **Fraude à l’identité** sur comptes clients.

**Priorités défensives** :

- Monitoring crédentiels sur stealer markets.
- Sécurité applicative web (OWASP, CSP, SRI pour scripts tiers).
- Détection fraude (ML sur comportements).
- Plan de continuité e-commerce.

#### 35.6 Télécoms

**Profil** : infrastructure critique + accès aux communications clients. Cible d’acteurs étatiques (Salt Typhoon contre télécoms US) et cybercriminels.

**Menaces dominantes** :

- **Accès au cœur réseau pour interception** : Salt Typhoon contre opérateurs US (2024).
- **SIM swapping** par insiders corrompus.
- **Ransomware** contre opérateurs.
- **Vol de données d’abonnés** (milliards de lignes potentielles).

**Priorités défensives** :

- Durcissement accès privilégiés réseau.
- Monitoring insiders (insider threat programs).
- Chiffrement des métadonnées et communications où possible.
- Coopération ANSSI et homologues internationaux.

#### 35.7 Secteur public et gouvernement

**Profil** : cible prioritaire d’APT étatiques. Données sensibles, fonctionnaires à haute valeur, services critiques.

**Menaces dominantes** :

- **Espionnage étatique** : APT29, APT40, APT31 ciblent régulièrement administrations.
- **Ransomware** : multiples collectivités locales victimes (mairies, départements).
- **Vol de données citoyens** : identités, fiscales, sociales.
- **Influence et désinformation** via compromission de comptes officiels.

**Cas emblématiques** :

- **France Travail (2024)** : breach massif de données chercheurs d’emploi.
- **Multiples collectivités françaises** victimes ransomware.
- **APT31 contre parlementaires britanniques et américains** (documenté 2024).

**Priorités défensives** :

- Alignement ANSSI (OIV, NIS 2).
- Segmentation et zero trust.
- Protection dirigeants et élus (monitoring VIP sur dark web).
- Sensibilisation face aux opérations d’influence.

#### 35.8 Éducation et recherche

**Profil** : cible régulière, budgets cyber limités, posture défensive souvent faible.

**Menaces dominantes** :

- **Ransomware** contre universités (multiples cas France 2024-2025).
- **Vol de propriété intellectuelle** : recherche, brevets, données d’essais cliniques.
- **Targeted espionnage** sur chercheurs dans domaines sensibles (quantique, IA, biotech).
- **Compromission d’infrastructures partagées** : sites universitaires hébergeant de multiples services.

**Priorités défensives** :

- Renforcement posture malgré contraintes budgétaires.
- Coopération Renater / CSIRT académique.
- Segmentation entre recherche sensible et usage général.

#### 35.9 Cryptomonnaies et fintech crypto

**Profil** : cible de très forte valeur (vols de millions USD possibles en une opération).

**Menaces dominantes** :

- **Vol de wallets** (exchanges, cold wallets). Cas Ronin Network, Bybit, FTX (mais pour FTX : hack post-faillite).
- **Phishing ciblé** des utilisateurs particuliers.
- **Compromission de smart contracts** (bridges DeFi notamment).
- **Stealers ciblant extensions crypto** (MetaMask, Phantom).

**Priorités défensives** :

- Cold storage pour majorité des fonds.
- Multi-sig hardware wallets.
- Sécurité opérationnelle des validateurs (Ronin a été compromis par vol de clés validateurs).
- Veille active sur marchés de phishing kits crypto.

#### 35.10 Fil rouge — DARKSTREAM : le secteur aerospace/defense

> **🌐 DARKSTREAM — Épisode 19 : contextualisation sectorielle**
> 
> Lucas inclut dans son rapport final une section sur le **contexte sectoriel aerospace/defense 2024-2026**.
> 
> **Observations générales sur le secteur** :
> 
> - Menace étatique croissante (Chine, Russie particulièrement intéressées par technologies sensibles).
> - Menace cybercriminelle opportuniste en hausse : le secteur est perçu comme « cible de valeur » avec revenus potentiels élevés via ransomware ou revente de données techniques.
> - Multiple cas 2024-2025 : plusieurs équipementiers aerospace européens et US victimes de ransomware ou exfiltrations.
> - IndustrialLeaks et forums similaires listent régulièrement des « aerospace sellers » — marché structuré pour ces données.
> - Acheteurs potentiels : services de renseignement (étatiques), concurrents industriels (via proxies), groupes cybercriminels cherchant à revendre ou exploiter levier chantage.
> 
> **Spécificités défense** :
> 
> - Données contrôlées export (ITAR aux US, équivalents européens) — exposition juridique accrue si fuite.
> - Partenariats multi-pays (programmes OTAN, européens) — ripple effects si un partenaire est compromis.
> - Sensibilité gouvernementale : remontée obligatoire aux autorités (en France : ANSSI, DGSI, autorités militaires selon classification des données).
> 
> **Recommandations spécifiques** pour Vectris au-delà des actions DARKSTREAM :
> 
> - Coopération accrue avec CERT-DEF (CERT défense).
> - Participation ISAC sectoriel aerospace (ASD-EUROSPACE, AIAC).
> - Revue des contrôles ITAR/export.
> - Sensibilisation collaborateurs R&D sur menace stealer et hygiène poste de travail.
> - Prépar communication gouvernementale (client défense) en cas d’escalade.
> 
> Cette contextualisation donne à la direction Vectris la dimension **stratégique** — l’incident DARKSTREAM n’est pas isolé, il s’inscrit dans un pattern sectoriel qui appelle réponse durable, pas seulement réaction ponctuelle.

-----

## PARTIE VII — CAS D’USAGE, TENDANCES ET PROSPECTIVE

> **Ce que cette partie apprend.** Comprendre les grandes catégories d’usage du dark web contemporain (ransomware/extorsion, influence, hacktivisme), les tendances 2024-2026 (IA offensive et défensive), et l’évolution des relations forces de l’ordre / écosystème.
> 
> **Ce qu’elle ne couvre pas.** Les études de cas détaillées (Partie VIII), les aspects techniques (couverts en Partie II), les méthodes d’investigation (Partie V).
> 
> **Ce que vous saurez faire après cette partie.** Lire l’écosystème contemporain avec perspective, anticiper les évolutions à 12-24 mois, et positionner votre programme de défense face à des tendances qui s’accélèrent.

-----

### Chapitre 36 — Ransomware, extorsion et leak sites

Le ransomware est le phénomène cyber le plus structurant des années 2020. Ce chapitre complète les Ch.11-12 (leak sites) avec une vision d’ensemble du phénomène, ses évolutions, ses impacts.

#### 36.1 L’évolution du modèle ransomware

**Génération 1 (2013-2018) — Ransomware de masse**. CryptoLocker (2013), Locky (2016), WannaCry (2017 — DPRK). Distribution massive non-ciblée, rançons faibles (300-5 000 USD typiquement), chiffrement local. Modèle : volume × petit paiement.

**Génération 2 (2019-2021) — Big game hunting**. Ryuk, Sodinokibi/REvil, Conti. Ciblage d’organisations spécifiques, reconnaissance approfondie avant déploiement, rançons 100 k - 10 M USD. Modèle : ciblage × gros paiements.

**Génération 3 (2020-présent) — Double extorsion**. Maze a popularisé le modèle : exfiltration **avant** chiffrement, leak site pour pressure, publication si non-paiement. Aujourd’hui standard pour tout ransomware sérieux.

**Génération 4 (2023-présent) — Multi-extorsion**. Au-delà du chiffrement + publication, pressions additionnelles :

- **Chantage direct des clients** de la victime (DarkSide historique, d’autres).
- **Chantage des partenaires et fournisseurs**.
- **DDoS** contre les services de la victime pendant la négociation.
- **Harcèlement téléphonique** des dirigeants.
- **Notification aux régulateurs** (mention explicite de SEC, CNIL, etc.) comme menace.
- **Publication auprès journalistes** pour maximiser impact médiatique.

**Génération 5 (émergente) — Extorsion pure, sans chiffrement**. BianLian depuis 2023 a abandonné le chiffrement et se concentre sur exfiltration + extorsion. Raisons : restauration depuis backups annule le levier de chiffrement, le chiffrement déclenche alertes défensives. L’exfiltration + chantage peut être plus subtile et plus efficace.

#### 36.2 Les modèles économiques ransomware contemporains

**RaaS (Ransomware-as-a-Service)**. Dominant. Opérateur fournit malware + infrastructure (leak site, portail négociation), affiliés déploient. Partage typique 70-80% affilié, 20-30% opérateur.

**Affiliés indépendants**. Un opérateur ransomware avec équipe interne (pas d’affiliés externes). Moins scalable mais contrôle qualité supérieur. Certains groupes matures opèrent ainsi (Cl0p partiellement).

**Opérateurs franchisés**. Variant RaaS avec contractual obligations plus strictes (territoires, cibles, comportements).

**Cartels** : coordination entre plusieurs groupes, partage d’infrastructure, coordination d’affiliés. Émergent 2023-2025.

#### 36.3 Les grands groupes 2024-2026

**LockBit** — leader historique, affecté par Operation Cronos (février 2024). Infrastructure saisie, Dmitry Khoroshev (LockBitSupp) identifié et sanctionné. Relaunch tenté, crédibilité entamée. Estimation historique : 500 M+ USD cumulé avant disruption.

**ALPHV / BlackCat** — second historique, disparition mars 2024 après suspicion d’exit scam post-paiement Change Healthcare (~22 M USD disparu avec opérateur).

**Cl0p** — modus operandi spécifique : exploitation de vulnérabilités d’edge devices (MOVEit 2023, Fortra GoAnywhere, Oracle EBS 2025). Campagnes massives par vagues, moins continu que LockBit historique.

**Black Basta** — actif 2022-2025, ciblage enterprise large, rançons élevées. Source probable de plusieurs incidents majeurs.

**Play / PlayCrypt** — actif depuis 2022, ciblage varié, rythme soutenu.

**Akira** — émergent fin 2023, croissance rapide. Ciblage diversifié.

**RansomHub** — émergent mi-2024, semble absorber affiliés ALPHV post-disparition. En forte croissance 2024-2025.

**Qilin** — actif, ciblage notable (Synnovis/NHS juin 2024).

**Groupes émergents** : 8Base, Hunters International, Dragonforce, Medusa, Inc Ransom — à surveiller.

#### 36.4 Ampleur et tendances macro

**Rapports Coveware** (trimestriels) donnent les tendances transversales :

- **Paiement moyen** en hausse tendancielle : de ~500 k USD en 2021 à ~2-3 M USD en 2024-2025 sur grandes victimes.
- **Taux de paiement** en baisse : de ~70% en 2018-2019 à ~25-30% en 2024. Moins de victimes paient, mais celles qui paient paient plus.
- **Time to recovery** : moyennes de 20-25 jours pour reprise opérationnelle partielle, plusieurs mois pour reprise complète.
- **Victimes par secteur** : healthcare, manufacturing, finance en tête. Secteur public croissant.
- **Géographie** : US majoritaire, mais EU en forte croissance.

**Rapports Chainalysis** sur crypto flux ransomware :

- **2024** : record ~1,1 Mrd USD (en paiements identifiés), malgré ou à cause de Cronos/ALPHV disappearance.
- Flux vers exchanges dans juridictions permissives, mixers, Monero swaps.

#### 36.5 Les leak sites comme théâtre médiatique

Les leak sites ne sont pas que des outils de coercition — ils sont aussi **des théâtres médiatiques** pour les groupes.

**Construction de réputation**. Un groupe avec leak site flashy, design soigné, countdown dramatique construit sa réputation. Attire affiliés, impressionne futurs victimes, domine la presse.

**Concurrence entre groupes**. Leak sites montrent les trophées — cibles prestigieuses compromises. Les groupes se comparent, se défient, se vantent.

**Communication aux victimes**. Message implicite : « regardez ce qu’on peut faire, payez ou voyez votre nom ici ».

**Communication à la communauté cybercriminelle**. Recruter affiliés (top des ransom payout), attirer autres acteurs.

**Communication aux médias**. Certains groupes soignent leur relation presse — portails avec section « media contact », press kits, mises à jour régulières. Stratégies de RP criminelles.

**Narratifs politiques**. Certains groupes se drapent dans des narratifs (« on cible les corrompus », « on cible les gouvernements oppresseurs »), soit sincèrement, soit comme cover. REvil historique jouait sur cette corde ; certains groupes actuels aussi.

Pour l’analyste, le **ton** du leak site informe sur l’acteur. Ton brutal + minimaliste = groupe pragmatique. Ton élaboré + narratif = groupe attentif à l’image. Ton politique = potentiel de hybridation avec hacktivisme.

#### 36.6 Les négociations

Une fois une victime compromise et revendiquée, les **négociations** commencent. Écosystème professionnalisé.

**Portails dédiés**. Chaque groupe maintient un portail de négociation (généralement sur .onion), avec chat, possibilité d’envoyer preuves d’exfiltration, compteur de rançon.

**Négociateurs**. Côté criminel, personnel dédié à la négociation. Souvent anglophones (ou utilisant traduction), patients, adoptant un ton « business ». Certains sont formés.

**Négociateurs côté victime**. Profession émergente. Cabinets spécialisés (Coveware, Kroll, GroupSense) maîtrisent les négociations avec groupes connus, connaissent patterns de discount, processus de paiement.

**Patterns de négociation** :

- **Demande initiale** souvent exagérée (facteur 3-5× de ce qui sera accepté).
- **Réduction par négociation** : 40-70% de discount réaliste avec négociateur professionnel.
- **Preuve de déchiffrement** (decryption test) avant paiement.
- **Preuve de destruction des données** exfiltrées (rarement vérifiable).
- **Délais** : 7-14 jours typiquement, extensible.

**Payer ou pas** : débat structurant, Ch.12. Tendance baisse du paiement.

**Sanctions OFAC** : certains groupes sanctionnés. Payer un groupe sanctionné expose à sanctions pour le payeur. Négociateurs doivent vérifier avant de faciliter paiement.

#### 36.7 L’impact des disruptions policières

**Operation Cronos contre LockBit (février 2024)**. Coordination NCA, FBI, Europol, 10+ pays. Saisie infrastructure, publication de clés de déchiffrement (permettant restauration gratuite pour certaines victimes), identification et sanction Khoroshev, leak de communications internes.

**Impact** : LockBit a tenté un relaunch mais avec crédibilité sérieusement entamée. Affiliés ont migré vers concurrents (Black Basta, Akira, RansomHub notamment).

**Ransom payments** ont connu une baisse mi-2024 liée à Cronos et disparition ALPHV, mais sont remontés rapidement — l’écosystème a absorbé les chocs.

**Enseignements** :

- Les disruptions ont un impact **temporaire** sur l’écosystème, pas définitif.
- Les affiliés sont **agnostiques** — ils migrent là où les conditions sont les meilleures.
- La **résilience structurelle** du ransomware est élevée — business model rentable, acteurs nombreux, juridictions permissives disponibles.
- Les **disruptions répétées** peuvent cependant augmenter les coûts opérationnels et réduire la confiance des affiliés — stratégie de long terme vs coup unique.

#### 36.8 Les contre-mesures défensives émergentes

**Cyber-insurance**. A évolué — certaines polices excluent désormais les paiements à groupes sanctionnés, imposent due diligence pré-paiement, requirement de contrôles défensifs (MFA, EDR, backups testés) pour couverture.

**Plans de continuité** éprouvés par exercices (tabletop, simulations). Objectif : récupérer **sans paiement**.

**Backups offline testés**. Le backup qui n’a jamais été testé ne marche pas. Test régulier de restauration partielle et complète.

**Zero Trust**. Limite la propagation latérale. Segmentation, least privilege, MFA partout.

**EDR/XDR et détection comportementale**. Détecter le ransomware **avant le chiffrement** — indicateurs d’exfiltration, modifications massives de fichiers, connexions C2.

**Threat hunting proactif** sur TTP ransomware connus.

**Coopération sectorielle** via ISAC pour partage rapide d’IoC.

**No-ransom coalitions** : initiatives (Counter Ransomware Initiative CRI, dirigée par US depuis 2021, 50+ pays membres) qui coordonnent la lutte, facilitent partage d’intel, découragent paiements.

-----

### Chapitre 37 — Dark web, influence et opérations informationnelles

Le dark web sert aussi de plateforme pour des **opérations d’influence** — désinformation, campagnes coordonnées, manipulation de l’opinion. Ce chapitre cartographie ce volet moins visible mais d’importance croissante.

#### 37.1 Les types d’opérations d’influence

**Hack-and-leak**. Technique classique : compromission de cibles politiques ou commerciales, puis publication sélective de données pour influencer narratif. Exemples emblématiques :

- **DNC hack (2016)** : GRU compromet le Democratic National Committee, publie via DCLeaks / Guccifer 2.0 / WikiLeaks. Impact élection présidentielle US.
- **Macron Leaks (2017)** : compromission campagne Macron, publication massive à 48h du second tour.
- **Multiple cas** ciblant partis politiques, campagnes, ONG, journalistes.

**Amplification coordonnée**. Réseaux de comptes (sock puppets, bots) qui amplifient certains messages sur réseaux sociaux. Le dark web sert de canal de coordination, de marché d’achat de comptes, d’outils.

**Fabrication de contenus**. Articles fabriqués, deepfakes, fake leaks. Le dark web héberge parfois la production et la distribution initiale.

**Doxing coordonné**. Publication d’informations personnelles de cibles (journalistes, politiques, activistes) pour les harceler, intimider, faire taire. Forums dédiés au doxing existent.

**Opérations « false flag ».** Attribution trompeuse d’une opération à un tiers pour le discréditer ou créer tensions.

#### 37.2 Les acteurs

**Services de renseignement étatiques**. Les opérations d’influence étatiques ont une dimension cyber importante. Russie (GRU, IRA/St. Petersburg troll farm — Prigojine historique), Chine (réseaux amplifiés), Iran, autres.

**Groupes hacktivistes**. Idéologiques, opérations revendiquées. Ch.38.

**Prestataires commerciaux d’influence**. Entreprises vendant des services d’influence (parfois légitimes, souvent gris). Plusieurs entreprises ont été exposées par journalistes (Team Jorge en 2023, Cambridge Analytica avant 2018).

**Opérateurs individuels**. Anonymous, Ghost Security, individus opérant selon leurs convictions.

**Opérations hybrides** : coordination multi-acteurs. Un État finance, un prestataire opérationnalise, des proxies exécutent, des sous-traitants amplifient.

#### 37.3 Les canaux

**Telegram**. Plateforme centrale pour les opérations d’influence russophones depuis 2022. Canaux pro-russes avec millions d’abonnés cumulés, coordination de narratifs, diffusion de contenus fabriqués. Arrestation Durov août 2024 a modifié la donne — modération durcie, partiellement contournée par migration.

**Forums dark web**. Coordination et mise en relation entre acteurs. Moins de diffusion publique (pas accessible à grand public) mais plus de discussion opérationnelle.

**Canaux dédiés**. KillNet (Telegram + sites annexes), NoName057(16) (canal DDoS revendiqué pro-russe), groupes Anonymous, IT Army of Ukraine.

**Réseaux sociaux mainstream**. La diffusion finale passe par X, Facebook, Instagram, TikTok, YouTube. Les plateformes font des efforts de modération mais restent débordées.

**Médias alternatifs et faux médias**. Sites qui imitent apparence de vrais médias (« Info-France »), sans journalisme réel, diffusant contenus alignés avec narratifs spécifiques. Parfois reliés à opérations étatiques (plusieurs démasquages documentés par EU DisinfoLab).

#### 37.4 La désinformation russe et l’opération Doppelganger

**Opération Doppelganger** (documentée par EU DisinfoLab, Meta, Microsoft depuis 2022) : réseau russe qui crée de fausses versions de médias occidentaux (faux Le Monde, Der Spiegel, Bild, The Guardian, Washington Post, NYT) pour diffuser narratifs pro-russes avec apparence crédible.

**Modus operandi** :

- Création de **clones** de sites de grands médias, avec URL similaires (un caractère différent).
- Publication d’articles fabriqués sur ces clones, avec design identique aux vrais.
- Amplification sur réseaux sociaux (bots, sock puppets, acteurs coordonnés).
- Liens partagés depuis comptes Telegram, Facebook, X — le lecteur voit « Der Spiegel » et ne vérifie pas l’URL exacte.

**Impact** : plusieurs vagues documentées. Ciblage : opinion publique allemande, française, américaine, sur narratifs liés à la guerre en Ukraine, aux sanctions, aux dirigeants démocratiques.

**Attribution** : liens avec entités russes identifiés (Structura et Social Design Agency — deux entreprises russes sanctionnées par UE en 2023, et par US Treasury en 2024).

**Défense** : sensibilisation du public, détection automatique par plateformes, sanctions ciblées sur acteurs identifiés.

#### 37.5 L’IRA et les opérations de troll

**Internet Research Agency (IRA)**, basée à St. Petersburg, historiquement financée par Yevgeny Prigojine (mort accidentellement en août 2023). Opérations de troll farm documentées sur plusieurs continents.

**Opérations documentées** :

- **Élections US 2016** (inculpations DOJ Mueller février 2018).
- **Influence en Afrique francophone** (Mali, RCA, autres — stratégie russe d’influence post-retraits français).
- **Divers conflits internes dans pays occidentaux** (race, immigration, divisions sociales).

**Modus operandi** :

- **Personas soigneusement construits** — pas simples bots, mais comptes faux avec identité fabriquée, activité cohérente sur années.
- **Coordination sur plateformes multiples** — X, Facebook, Instagram, Reddit.
- **Amplification de vrais contenus divisifs** autant que création de faux.
- **Mixage avec influenceurs locaux** parfois conscients, parfois manipulés.

**Post-Prigojine** : réorganisations internes russes, continuation avec autres structures. Les opérations persistent.

#### 37.6 Les opérations d’influence côté cybercrime

Les opérations d’influence ne sont pas que étatiques — le dark web cybercriminel produit aussi :

**Manipulation de réputation**. Groupes qui dénigrent concurrents, promeuvent leurs services, manipulent ratings sur forums.

**Doxing de rivaux**. Publication d’identité civile d’un opérateur concurrent par un autre. Classique dans guerres inter-groupes.

**Leaks stratégiques**. Fuite sélective de données pour embarasser un acteur (victime, concurrent, ex-partenaire).

**Faux témoignages**. Comptes qui prétendent être victimes satisfaites ou insatisfaites pour influencer marchés.

#### 37.7 Les deepfakes

**Deepfakes vidéo** et **deepfakes audio** émergent comme vecteurs :

- **Deepfakes de dirigeants** pour simuler déclarations, provoquer crises.
- **Voix truquées** pour fraude (cas documentés de CFO qui reçoivent appels « du CEO » avec voix clonée demandant transfert urgent).
- **Vidéos de « preuve » de scandales** inventés.

**Marchés** : les kits de deepfake et services de création sont disponibles sur dark web, prix variables. Certains services vendent « 1 minute de deepfake video » pour quelques centaines de dollars.

**Défense** : outils de détection (Microsoft Video Authenticator, Intel FakeCatcher, autres), watermarking des contenus légitimes, sensibilisation.

#### 37.8 Implications défensives pour organisations

**Monitoring réputation**. Veille sur mentions de la marque dans contextes d’influence — sites clones, fake accounts amplifiant narratifs contre l’organisation, deepfakes de dirigeants.

**Protection des dirigeants**. Monitoring de l’exposition publique des dirigeants, alerte sur deepfakes, procédures de vérification en cas de demande urgente « venant du CEO ».

**Procédures anti-fraude**. Pour éviter les CEO fraud via deepfake, procédures de double vérification sur transactions importantes (canal indépendant, code secret, confirmation multi-personnes).

**Sensibilisation**. Formations sur reconnaissance des opérations d’influence, vérification des sources, identification des narratifs coordonnés.

**Coopération sectorielle et autorités**. Signalement aux autorités (VIGINUM en France pour la contre-ingérence informationnelle), partage via ISAC.

-----

### Chapitre 38 — Hacktivisme, zones grises et usages légitimes

Le **hacktivisme** — action cyber à motivation idéologique ou politique — occupe une zone grise importante du dark web. Ce chapitre distingue ses formes, ses acteurs, et aborde les usages légitimes qui partagent l’infrastructure.

#### 38.1 Les grandes traditions hacktivistes

**Anonymous (depuis 2003)**. Mouvement décentralisé, symbole Guy Fawkes. Opérations cibles variées — Église de Scientologie (Project Chanology 2008), PayPal/Visa (Operation Payback 2010), PRISM révélations supporting (2013), ISIS (post-attentats Paris 2015), KKK, polices accusées d’abus, régimes autoritaires. Actions : DDoS, defacement, leaks, doxing. Pas de hiérarchie formelle — opérations revendiquées par qui veut.

**WikiLeaks (depuis 2006)**. Julian Assange, plateforme de publication de documents classifiés ou secrets. Cablegate (2010), Vault 7 (2017 — outils CIA), multiples leaks politiques. Plus plateforme que acteur, mais impact hacktiviste majeur.

**LulzSec (2011)**. Spin-off Anonymous, opérations médiatiquement marquantes (PBS, Sony, Nintendo, InfraGard FBI). Courte durée de vie, arrestations rapides (Sabu retourné informateur FBI).

**Chaos Computer Club (depuis 1981)**. Plus ancien, allemand, plus institutionnel. Activisme éthique, recherche sécurité, positions sur politique numérique.

**Telecomix**. Support technique aux révolutionnaires du printemps arabe (2011-2012), contournement de censure.

**Cult of the Dead Cow (depuis 1984)**. Très ancien collectif, influence sur éthique hacker, outils historiques (Back Orifice).

#### 38.2 Les hacktivismes contemporains (2022-2026)

**Contexte de la guerre en Ukraine** a relancé massivement l’hacktivisme, des deux côtés.

**IT Army of Ukraine**. Créé par le gouvernement ukrainien (Mykhailo Fedorov, ministre) fin février 2022 après l’invasion russe. Plus de 200 000 volontaires déclarés. Operations : DDoS contre cibles russes (gouvernement, banques, médias), défacement, leaks de données russes.

**Caractéristique unique** : mouvement hacktiviste **officiellement soutenu par un État** — ligne parfois floue entre volontaires citoyens et coordination étatique.

**KillNet**. Côté russe, pro-Kremlin. Créé 2022, opérations DDoS contre cibles occidentales (gouvernements EU, infrastructures, hôpitaux US). Positionnement « cyber armée » mais compétences limitées (surtout DDoS). Sanctionné par UE en 2023.

**NoName057(16)**. Autre groupe pro-russe, DDoS contre cibles occidentales. Sanctionné UE 2024. Plus technique que KillNet.

**Cyber Av3ngers**. Iranien, pro-gouvernement. Cibles : infrastructures eau US (compromission PLC Unitronics 2023-2024 — exploitation default passwords, impact symbolique).

**Groupes pro-palestiniens et anti-israéliens** (post-7 octobre 2023). Intensification des opérations, DDoS contre cibles israéliennes, leaks de données, défacement. Composition diverse — certains soutenus par Iran (via IRGC), d’autres hacktivistes indépendants.

**Anonymous actuels**. Fragmentés, opérations sporadiques. « Anonymous Russia » (pro-Ukraine), différents chapters nationaux. Moins structuré qu’historiquement.

**Ghost Security**. Anti-ISIS, anti-extrémisme.

#### 38.3 La zone grise : hacktivisme ou cybercrime ?

La frontière entre hacktivisme sincère et cybercrime déguisé est **floue**.

**Cas mixtes** :

- **Lapsus$ (2021-2022)**. Groupe d’adolescents, motivation mixte (argent + gloire + idéologie floue). Compromissions majeures (Okta, Microsoft, Nvidia, Samsung). Arrestations 2022-2023.
- **BianLian narratif**. Revendications parfois politiques malgré motivation financière claire.
- **Some Anonymous operations qui tournent à l’extorsion**.

**Instrumentalisation**. Des États utilisent l’apparence hacktiviste pour opérations étatiques (plausible deniability). KillNet/NoName : hacktivistes réels ? Proxies étatiques ? La frontière est difficile.

**Recrutement**. Des groupes cybercriminels recrutent des hacktivistes motivés idéologiquement comme collaborateurs — travail pour une cause, mais avec bénéfices financiers.

**Hacktivisme mercenaire**. Entreprises qui proposent des services « hacktivistes » à la commande, pour dénigrer concurrents, activistes, journalistes. Team Jorge documenté 2023.

#### 38.4 Les usages légitimes du dark web

Au-delà du crime et de l’hacktivisme (qui peut être contesté), le dark web sert **d’autres usages, parfaitement légitimes et essentiels**.

**Journalisme et protection des sources**. SecureDrop déployé par NYT, Guardian, Le Monde, Der Spiegel, WaPo, ProPublica, BBC, The Intercept. Plateforme permettant à des sources de transmettre documents aux journalistes de manière anonyme. Sans ces canaux, beaucoup de journalisme d’investigation serait impossible.

**Contournement de censure**. Dans régimes autoritaires (Chine, Iran, Russie post-2022, Biélorussie, Myanmar, Érythrée) :

- Accès à médias bloqués (BBC Persian, Voice of America, Deutsche Welle).
- Wikipedia accessible via .onion.
- Plateformes sociales bloquées (X, Facebook, Instagram) accessibles.
- Outils de communication chiffrée.

**Lanceurs d’alerte**. Plateformes type GlobaLeaks, hébergement de PublicLeaks. Protection de l’anonymat pour signaler actes illégaux depuis une organisation.

**Défense des droits humains**. ONG opérant dans régions hostiles (Reporters Sans Frontières, Amnesty International, Human Rights Watch) utilisent Tor et .onion pour coordination sécurisée, transmission de rapports, accès aux victimes.

**Communications d’activistes**. Dissidents politiques, opposants dans régimes autoritaires, manifestants. Tor permet communication sans traçage étatique.

**Recherche en cybersécurité**. Chercheurs accédant à marchés/forums pour investigation, threat intelligence, collecte d’indicators.

**Protection de la vie privée**. Utilisateurs simples qui veulent naviguer sans traçage commercial, sans profiling publicitaire. Argument philosophique valide indépendamment de toute activité « sensible ».

**Services légitimes hébergés en .onion**. Wikipedia, ProPublica, DuckDuckGo, Facebook, Twitter historique, Protonmail — tous maintiennent miroirs .onion pour servir utilisateurs sensibles.

#### 38.5 Les défenses et réponses

**Côté acteurs** (journalistes, dissidents, activistes) : formations à l’OPSEC, usage de Tails, Whonix, Signal, PGP. Écosystème d’outils et de guides (Freedom of the Press Foundation, Tactical Tech, EFF).

**Côté plateformes** : SecureDrop (Freedom of the Press Foundation), GlobaLeaks, OnionShare — infrastructures dédiées.

**Côté sensibilisation** : éducation à la protection de la vie privée, à la reconnaissance de la surveillance.

**Côté régulation** : équilibre délicat entre sécurité (contre-terrorisme, lutte contre cybercrime) et libertés publiques (vie privée, liberté d’expression, protection sources). Débat vivant et loin d’être résolu.

#### 38.6 La nuance éthique pour l’analyste

Un analyste CTI qui travaille sur le dark web doit maintenir une **nuance éthique**.

**Ne pas assimiler** tout ce qui est sur .onion à du cybercrime. Beaucoup d’activité légitime.

**Respecter les acteurs légitimes**. Un journaliste qui utilise Tor pour protéger sa source n’est pas une cible d’investigation. Un dissident en exil qui communique via .onion n’est pas un criminel.

**Différencier les cibles d’investigation**. Vrais cybercriminels (forums de vente de données, leak sites ransomware, marchés illicites) = cibles légitimes. Journalistes, activistes, dissidents = **non-cibles**.

**Protéger l’anonymat des sources légitimes**. Si l’investigation révèle incidemment l’identité de sources légitimes (d’un journaliste, d’un dissident), ces informations ne sont pas exploitées ni partagées.

**Considérer les motivations**. Un hacktiviste qui cible un régime autoritaire n’a pas les mêmes motivations qu’un ransomware qui chiffre un hôpital. L’analyste peut observer les deux, mais les qualifie différemment.

**Éviter le prisme idéologique**. Un analyste ne favorise pas un camp parce qu’il y adhère idéologiquement. Factualité et neutralité.

#### 38.7 Implications pratiques

Pour une entreprise, l’hacktivisme représente un risque selon les contextes.

**Profil à risque hacktiviste** :

- Entreprise avec position politique visible.
- Secteur controversé (défense, fossiles, pharma sur sujets sensibles).
- Présence dans pays / contextes sensibles.
- Dirigeants exposés médiatiquement.

**Mitigations** :

- Monitoring mentions de l’organisation dans canaux hacktivistes.
- Protection DDoS robuste (CDN, services anti-DDoS professionnels).
- Protection des dirigeants (monitoring VIP sur dark web).
- Plans de communication de crise adaptés aux revendications idéologiques.
- Segmentation des ressources critiques pour résister à leaks possibles.

Pour la plupart des organisations, l’hacktivisme est un risque **modéré** comparé aux cybercriminels et APT. Mais il peut exploser en volume lors de contextes politiques tendus.

-----

### Chapitre 39 — IA et dark web : menaces émergentes et défensives

L’**intelligence artificielle générative** transforme l’écosystème dark web depuis 2022-2023. Ce chapitre cartographie les usages observés, en menaces et en défenses, et anticipe les évolutions.

#### 39.1 L’arrivée des LLM dans le dark web

L’arrivée publique des LLM (ChatGPT novembre 2022, puis cascade — Claude, Gemini, Llama open source, etc.) a immédiatement été détournée. Plusieurs angles.

**Bypass des garde-fous des LLM commerciaux**. Les LLM mainstream (OpenAI, Anthropic, Google) ont des restrictions contre usages malveillants. Techniques de jailbreaking, prompt injection, role-playing — apparaissent rapidement dans la communauté cybercriminelle. Effectivité variable selon les versions, fenêtres exploitées puis fermées.

**Modèles alternatifs sur dark web**. Émergence de LLM spécifiquement marketés pour usage criminel.

- **WormGPT** (apparu 2023) : version sans garde-fous basée sur GPT-J open source, marketée pour BEC fraud, phishing, malware writing. Vendu en abonnement (~100 USD/mois). Modèle initial fermé après publicité, plusieurs successeurs.
- **FraudGPT** (2023) : focus fraude, carding, social engineering.
- **DarkBERT** (académique, pas malveillant) : modèle entraîné sur dark web pour recherche.
- **Multiples successeurs** : WolfGPT, EscapeGPT, EvilGPT, etc. Marketing principalement, sous le capot souvent simples LLM open source avec prompts adaptés.

**Usage des LLM open source**. Les LLM open source (Llama, Mistral, autres) ne posent pas de restriction d’usage par défaut. Les acteurs sophistiqués les déploient localement et les fine-tunent pour cas criminels.

#### 39.2 Les usages offensifs

**Génération de phishing**. LLM produisent emails de phishing en multiples langues, avec qualité linguistique excellente — fin du « phishing avec fautes d’orthographe identifiable ». Personnalisation à grande échelle (mention de détails du destinataire scrapés sur LinkedIn).

**Génération de code malveillant**. LLM aident à écrire malware. Compétence variable — pour code simple, efficace ; pour malware sophistiqué (évasion EDR, anti-analyse avancée), encore limité. Mais les progrès sont rapides.

**Génération de contenu pour social engineering**. Pretexts crédibles, scénarios élaborés, faux profils LinkedIn cohérents.

**Deepfakes vocaux**. Voice cloning à partir de quelques secondes d’audio. Usage : fraude au CEO (faux appel téléphonique du CEO demandant transfert urgent). Cas documentés multiples 2023-2025.

**Deepfakes vidéo**. Plus complexes mais accessibles. Usage : usurpation d’identité en visio-conférence (un employé voit son CEO en visio demandant transfert — c’est un deepfake animé). Incident à grande échelle documenté à Hong Kong début 2024 (Arup, ~25 M USD perdus à un deepfake en visio-conférence).

**Vishing automatisé**. Appels téléphoniques automatisés avec voix IA, conversation interactive. Plus convaincant que les robocalls classiques. En émergence.

**Génération de leak sites et phishing kits**. Création accélérée d’infrastructures cosmétiques.

**Reconnaissance et profilage**. LLM aident à analyser des grandes quantités de données OSINT pour profiler des cibles.

**Translation et adaptation linguistique**. Acteurs russophones produisent emails phishing impeccables en français, anglais, allemand.

#### 39.3 Les marchés IA criminels

**Marketplaces**. Plusieurs marketplaces dark web et Telegram listent des **services IA criminels** :

- Génération de phishing emails personnalisés.
- Génération de malware sur commande.
- Voice cloning à la demande.
- Deepfake vidéo à la commande (~50-500 USD selon complexité).
- Faux profils LinkedIn générés (avec photo, historique).
- LLMs sans restrictions par abonnement.

**Prix**. Très accessibles. Phishing kit IA-augmenté : 50-500 USD. Voice cloning : 100-1 000 USD selon qualité voulue. Deepfake vidéo simple : 200-2 000 USD.

**Évolution rapide**. La qualité progresse mensuellement. Le marché, encore embryonnaire en 2023, est mature en 2025.

#### 39.4 Les usages défensifs

L’IA n’est pas qu’offensive. Côté défensif, applications croissantes.

**Détection d’anomalies**. ML pour détecter comportements anormaux (fraude, intrusion, exfiltration). Plus performants que règles statiques.

**Analyse de logs à grande échelle**. SIEM augmentés par ML, threat hunting assisté par LLM.

**Classification de threat intelligence**. Tri automatique des alertes, scoring de pertinence, regroupement des indicateurs liés.

**Analyse stylométrique automatisée**. Pour pivoting et corrélation pseudonymes (Ch.29).

**Synthèse de rapports**. LLM aident l’analyste à rédiger rapports plus vite, à synthétiser corpus volumineux.

**Détection de deepfakes**. Outils dédiés (Microsoft Video Authenticator, Intel FakeCatcher, Reality Defender, Hive AI). Course offense/défense permanente.

**Détection de phishing IA-généré**. Outils émergents qui identifient signatures linguistiques de génération automatique. Effectivité variable.

**Veille dark web automatisée**. LLM analysent posts forums, traduisent, classifient. Réduit charge humaine.

**Sandboxing intelligent**. ML pour analyser comportements de fichiers suspects, détecter malware obfusqué.

#### 39.5 Les marchés défensifs IA

Côté défense, écosystème commercial structuré.

**Vendors mainstream** intégrant IA : Microsoft Security Copilot, CrowdStrike Charlotte AI, SentinelOne Purple AI, Google Security AI, Palo Alto Cortex avec IA, Recorded Future avec LLM intégré.

**Vendors spécialisés** : entreprises focused sur détection deepfake, sur détection phishing IA, sur threat intelligence avec LLM.

**Open source** : projets variés, performance variable.

**Standards émergents** : initiatives de watermarking (C2PA pour authentification de contenus), provenance des contenus.

#### 39.6 Le problème de la prolifération

L’IA criminelle pose un problème structurel : **prolifération vers acteurs moins sophistiqués**.

Avant IA : compromettre une entreprise nécessitait compétences techniques. Phishing efficace requérait talent linguistique. Deepfake nécessitait expertise.

Avec IA : un acteur sans compétences profondes peut produire phishing crédible, malware basique, deepfake convaincant. Le **plancher technique** descend.

**Impact** : explosion potentielle du volume d’attaques. Plus d’attaquants, attaques plus crédibles.

**Mais** : l’IA défensive aussi proliférise. Les organisations sans compétences cyber peuvent maintenant déployer des outils défensifs IA pré-emballés. Course technologique.

**Résultat net** : incertain. Hypothèses possibles : (a) avantage offensif court terme (les défenseurs sont réactifs), puis stabilisation ; (b) avantage défensif long terme (l’IA permet meilleure détection que prévention humaine) ; (c) escalade continue sans déséquilibre net. Les 5 prochaines années répondront.

#### 39.7 La menace deepfake spécifique

Les deepfakes méritent un traitement à part car leur impact peut être disproportionné.

**Types** :

- **Fraude financière** : faux CEO en visio demandant transfert. Cas Arup (2024) : ~25 M USD perdus.
- **Désinformation politique** : fausses déclarations de dirigeants pour influencer.
- **Sextorsion** : fausses images/vidéos compromettantes pour chantage. Pratique en croissance contre individus.
- **Diffamation** : faux contenus pour discréditer cibles.
- **Manipulation boursière** : faux contenus déstabilisant titres cotés.

**Défenses** :

- Procédures double-vérification pour transactions critiques (canal indépendant, code secret).
- Sensibilisation employés (recognize that deepfakes happen).
- Outils de détection technique.
- Watermarking des contenus officiels (provenance vérifiable).
- Cadre réglementaire émergent (UE AI Act 2024, obligations de transparence).

**Limites** : la course détection/génération est asymétrique. Les générateurs s’améliorent plus vite que les détecteurs. Approche structurée : ne pas se reposer uniquement sur détection technique, ajouter procédures organisationnelles.

#### 39.8 Les hallucinations et leurs implications criminelles

Les LLM **hallucinent** — produisent affirmations confiantes mais incorrectes. Pour un criminel utilisateur, conséquence ambivalente.

**Pour le criminel** : LLM peut produire malware qui ne fonctionne pas, conseils techniques erronés, identifiants fictifs. Réduit la fiabilité de l’IA criminelle pour acteurs peu sophistiqués qui ne peuvent pas vérifier.

**Pour la défense** : signaux d’IA dans phishing détectables si hallucinations. Email de phishing qui mentionne « votre commande N° 47823-XYZ chez Lufthansa » alors que la victime n’a jamais commandé chez Lufthansa = signal IA générique pas finement personnalisé.

**Évolution** : les hallucinations diminuent avec versions. RAG (Retrieval Augmented Generation) atténue. Mais ne disparaîtront pas totalement.

#### 39.9 Le cadre réglementaire

**UE AI Act (2024)**. Cadre majeur. Obligations de transparence, classification de risques, interdictions de certains usages (manipulation, social scoring), exigences pour systèmes high-risk. Impact sur produits commerciaux IA, peu d’impact direct sur usage criminel (qui est déjà illégal).

**US Executive Order on AI (octobre 2023)**. Cadre fédéral, focus sur sécurité IA, divulgation des modèles puissants.

**Initiatives sectorielles**. Standards C2PA, watermarking, partenariats public-privé.

**Pour l’analyste** : connaître ces cadres, anticiper les obligations qu’ils créent pour les organisations clients (déploiement IA légal, gestion des risques).

#### 39.10 Anticipation 2026-2030

Tendances probables.

**Multi-modalité IA**. Combinaison voix + vidéo + texte cohérent dans deepfakes. Contenus indistinguables du réel pour œil humain non-formé.

**Agents IA autonomes**. L’IA capable d’exécuter chaînes d’actions complexes (recon, exploitation, exfiltration). Émergent en 2024-2025, mature potentiel 2026-2028. Implications offensives : attaques largement automatisées. Implications défensives : agents défensifs équivalents.

**LLMs domain-specific criminels**. Modèles fine-tunés sur larges corpus criminels (malware code, phishing samples, fraud schemes). Performance technique en hausse.

**IA dans investigations défensives**. Analystes augmentés par agents qui automatisent collecte, corrélation, première analyse — humain valide et oriente.

**Régulation accrue**. Watermarking obligatoire pour contenus IA (US, UE en discussion). Obligations de provenance.

**Course armements**. Pas d’équilibre attendu — chaque progrès offensif appelle progrès défensif et vice versa.

Pour l’analyste actuel, **rester à jour** sur l’évolution IA est devenu une compétence centrale. Les outils et menaces de 2025 ne seront pas ceux de 2027.

-----

### Chapitre 40 — Forces de l’ordre, disruption et coopération internationale

Ce chapitre couvre l’autre face — comment les autorités luttent contre l’écosystème dark web. Comprendre leurs capacités et leur coordination informe à la fois la défense organisationnelle et la prospective.

#### 40.1 Les capacités étatiques

**FBI (US)**. Forces de l’ordre fédérales US, capacités cyber considérables. Opérations Bayonet, Cookie Monster, Cronos (lead côté US). Compétences techniques internes + coopération avec NSA pour SIGINT. Mandat large.

**Europol et EC3 (European Cybercrime Centre)**. Coordination des polices européennes, opérations multi-pays. Pas pouvoir de police directe mais coordination, intelligence sharing, soutien technique. Operations notables : Endgame (2024), Pacifier, Cookie Monster (côté EU), multiple ransomware.

**NCA (UK)**. National Crime Agency, lead Operation Cronos. Forte expertise cyber.

**BKA (Allemagne)**. Lead saisie Hydra (avril 2022), nombreuses opérations.

**ANSSI / SDLC / OFAC (France)**. ANSSI : agence cybersécurité, défensif principalement. **Sous-Direction de la Lutte contre la Cybercriminalité** (SDLC, gendarmerie). **OFAC français** (Office Anti-Cybercriminalité créé 2023). DGSI pour contre-espionnage cyber. DGSE pour renseignement extérieur. Coordination multi-agences en France.

**Interpol**. Coordination internationale globale, focal point pour pays moins équipés. Notable Operation Synergia (2024) contre infrastructure phishing.

**National CSIRTs**. CERT-FR (ANSSI), BSI (Allemagne), NCSC (UK), CISA (US), JPCERT (Japon), etc.

**Services de renseignement**. NSA (US), GCHQ (UK), DGSE (France), BND (Allemagne) — capacités SIGINT massives. Application sur dark web : surveillance d’infrastructures, déanonymisation par corrélation de trafic, infiltration par moyens classifiés.

#### 40.2 La coopération internationale

**Interpol-Europol Cybercrime Conferences** annuelles. Coordination, partage d’intelligence.

**J-CAT (Joint Cybercrime Action Taskforce)**. Hébergé par Europol, regroupe spécialistes des principaux pays européens + US, UK, Australie, Canada. Coordination opérationnelle.

**Counter Ransomware Initiative (CRI)**. Lancée par US 2021, 60+ pays membres en 2025. Coordination contre ransomware, partage intel, déclarations conjointes anti-paiement.

**Pall Mall Process (2024)**. Régulation des PSO (Private Sector Offensive — NSO, Intellexa, etc.). 40+ États signataires. Cadre non-contraignant mais structurant.

**Convention de Budapest (2001)** + protocole additionnel (2022) sur cybercriminalité. Cadre juridique de coopération.

**Mutual Legal Assistance Treaties (MLATs)**. Bilatéraux. Permettent demandes de preuves entre pays.

**Limites** : la coopération marche avec **pays alignés** (démocraties occidentales, Five Eyes, UE+). Avec Russie, Chine, certaines autres juridictions, coopération minimale ou nulle. C’est la raison structurelle de la persistance de l’écosystème criminel — sanctuaires juridictionnels existent.

#### 40.3 Les grandes opérations 2022-2026

**Operation Hydra (avril 2022)**. BKA + FBI. Saisie de Hydra Market (russophone, dominant). 25 M USD saisis en crypto. Fragmentation de l’écosystème russophone qui se poursuit.

**Operation Pacifier (2017+, multi-vagues)**. Suite de Playpen, contre CSAM globalement.

**Operation Lyrebird (2022)**. France+UK contre Glupteba botnet.

**Operation Cookie Monster (avril 2023)**. FBI + Europol + 17 pays. Saisie Genesis Market (marché de logs leader). 120+ arrestations.

**Operation Endgame (mai 2024)**. Europol-led. Démantèlement infrastructures multiples (IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee). 4 M USD saisis. Coordination avec FBI, BSI, Eurojust.

**Operation Cronos (février 2024)**. NCA, FBI, Europol, 10+ pays. LockBit. Infrastructure saisie, identification Khoroshev (LockBitSupp), publication clés de déchiffrement, sanctions.

**Operation Magnus (octobre 2024)**. Saisie d’infrastructure RedLine et MetaStealer (deux infostealers majeurs). Coordination globale.

**Operation Kaerb (septembre 2024)**. Démantèlement plateforme phishing iServer. Argentine + 10 pays.

**Kidflix (mars 2025)**. Plateforme CSAM, coordination internationale, arrestations.

**Saisies BreachForums multiples** (mars 2023, juillet 2024, autres). Pompompurin arrêté, Baphomet arrêté ensuite, ShinyHunters reprend opération, nouvelles actions.

**Pavel Durov (août 2024)**. Arrestation en France. Inculpation pour complicité dans diffusion de contenus illicites via Telegram. Impact massif sur Telegram (durcissement modération, coopération accrue avec autorités). Procédure ouverte, en cours.

#### 40.4 Les techniques d’opération law enforcement

**Investigation prolongée**. Les grandes opérations sont préparées sur **mois ou années**. Operation Cronos a été préparée depuis 2022. Bayonet mois de préparation.

**Coopération multi-agences**. FBI + Europol + NCA + 10+ pays. Coordination juridique complexe, harmonisation des actions.

**Coordination temporelle**. Saisies simultanées dans multiples pays pour empêcher fuite. Précis à la minute parfois.

**Opérations de takeover** (modèle Hansa). Prise de contrôle de l’infrastructure criminelle, opération sous contrôle pendant période, puis annonce. Objectif : maximiser collecte de données utilisateurs, pas seulement saisir.

**Saisies de cryptoactifs**. Coordination avec exchanges, gel de fonds, identification d’opérateurs via flux. FBI a récupéré centaines de millions USD cumulés.

**Communication post-opération**. Stratégique. Les autorités publient parfois avec mise en scène (LockBit a vu son leak site « hijacké » avec messages NCA/FBI), parfois avec discrétion. Objectif : maximiser effet dissuasif tout en protégeant méthodes.

**Coopération avec secteur privé**. Vendors CTI (Mandiant, CrowdStrike, Microsoft, Recorded Future) fournissent intelligence. Exchanges crypto coopèrent. Hébergeurs cooperent (parfois sous contrainte légale).

#### 40.5 Les limites et critiques

Malgré succès, limites structurelles.

**Sanctuaires juridictionnels**. Russie, Chine, certains pays — coopération minimale. Acteurs basés là-bas largement intouchables. Tant que le sanctuaire existe, l’écosystème persiste.

**Asymétrie coût-bénéfice**. Une opération comme Cronos mobilise des ressources énormes, pour un impact temporaire. LockBit reconstitue partiellement, affiliés migrent. Le ROI policier est questionné.

**Ressources limitées**. Le volume du cybercrime explose, les moyens policiers grandissent moins vite. Triage extreme — seules les opérations les plus impactantes sont menées.

**Frontières juridictionnelles**. Un acteur russe attaque une victime française via un serveur néerlandais avec paiement crypto à un wallet panaméen — qui poursuit ?

**Critiques sur méthodes**. Operation Playpen (FBI a opéré CSAM site pendant 2 semaines pour piéger). Multiple cas de NIT contestées. Question : où placer les limites éthiques ?

**Effet temporaire** : disrupter LockBit n’élimine pas le phénomène ransomware. Successeurs émergent.

**Underground innovation** : les acteurs s’adaptent. Plus de OPSEC, plus de fragmentation, plus de chiffrement, plus de cantonnement aux sanctuaires.

#### 40.6 La stratégie « pressure permanente »

Plutôt que viser élimination (impossible), la doctrine occidentale émergente est **pressure permanente**.

**Augmentation des coûts opérationnels** : forces les acteurs à investir plus en OPSEC, infrastructure résiliente, fragmentation. Réduit ROI criminel.

**Réduction des espaces sûrs** : sanctions ciblées (Tornado Cash, Garantex, Bitzlato, Suex), coopération sur juridictions précédemment permissives.

**Dissuasion par publicité** : grandes opérations communiquées créent doute chez acteurs, démontrent capacités.

**Fragilisation des chaînes** : taper IAB, RaaS opérateurs, blanchisseurs simultanément. Casse confiance écosystémique.

**Coopération public-privé**. Vendors CTI, exchanges, hébergeurs comme partenaires actifs.

**Efficacité** : pas d’élimination du cybercrime, mais réduction de son taux de croissance, augmentation de sa difficulté opérationnelle, réduction d’impact macro. Mesure ambivalente.

#### 40.7 Le rôle du privé

Pour les analystes CTI privés, plusieurs rôles dans l’écosystème law enforcement.

**Partenaires d’intelligence**. Vendors CTI fournissent indicateurs, attribution, contexte. Mandiant, CrowdStrike, Microsoft, Recorded Future, etc. — tous ont des liens fonctionnels avec FBI / NCA / Europol.

**Première ligne de détection**. Beaucoup d’incidents sont d’abord détectés par secteur privé (SOC), puis remontés aux autorités. La rapidité de détection privée conditionne l’impact des opérations publiques.

**Forensics et reconstitution**. Cabinets IR (Mandiant, Kroll, Stroz Friedberg, Wavestone, etc.) reconstituent attaques, alimentent enquêtes, témoignent en justice si besoin.

**Sensibilisation et formation**. Les analystes privés produisent rapports publics qui informent décideurs, journalistes, public. Sensibilisation de masse.

**Coopération sectorielle**. ISAC (FS-ISAC, H-ISAC, E-ISAC, etc.) facilitent partage rapide d’IoC entre pairs sectoriels.

**Limites du rôle privé** : pas de pouvoir coercitif, pas d’accès aux capacités SIGINT, contraintes commerciales (clients, conflits d’intérêt potentiels).

#### 40.8 Fil rouge — DARKSTREAM : conclusion law enforcement

> **🌐 DARKSTREAM — Épisode 20 : transmission DGSI**
> 
> Le rapport DARKSTREAM final est transmis à la DGSI le 15 mai 2026. La DGSI accuse réception, indique qu’elle exploitera les éléments selon ses canaux propres.
> 
> Lucas n’aura pas de retour direct sur les suites — la DGSI ne communique pas sur ses opérations en cours. Cela peut signifier :
> 
> - Investigation interne approfondie sur les acteurs identifiés (aero_source, magnit_ru).
> - Coopération avec partenaires internationaux (FBI, BKA, autres) pour traçage personnel, peut-être identification physique.
> - Inclusion dans intelligence stratégique sur menaces ciblant aerospace européen.
> - Rien — capacité non priorisée face à autres dossiers.
> 
> Pour Vectris, l’investigation DARKSTREAM se conclut sur :
> 
> - Confirmation et caractérisation de l’incident.
> - Recommandations défensives détaillées et applicables.
> - Cadre coopératif avec autorités établi.
> - Préparation à possible escalade (publication totale, revente à étatique).
> 
> Pour Athéna et Lucas, l’investigation produit :
> 
> - Cas documenté qui enrichit la doctrine interne.
> - Contacts opérationnels avec DGSI renforcés.
> - Compétences éprouvées par cas réel.
> - Référence anonymisée pour publications futures et formation.
> 
> **6 mois plus tard** (extrapolation) : pas de publication totale du dump observée. aero_source toujours actif sur l’écosystème (sous ses 3 pseudonymes). Possible : un acheteur final a payé, le dump est passé en circulation privée. Possible : aero_source attend opportunité commerciale meilleure. Possible : la DGSI et partenaires suivent en temps réel sans communiquer.
> 
> L’investigation DARKSTREAM aura été **un succès partiel** — pas d’identification personnelle, pas de récupération des données, pas d’arrestation. Mais : confirmation et caractérisation rapides, défense Vectris solide, cadre durable construit. C’est ce que l’investigation privée produit réalistement.

-----

## PARTIE VIII — ÉTUDES DE CAS ET SYNTHÈSE

> **Ce que cette partie apprend.** Articuler l’ensemble du cours sur des cas complets. Synthèse de DARKSTREAM, plus deux cas types complémentaires (surveillance d’un leak site, traque d’un IAB), puis la construction d’un programme de veille durable.
> 
> **Ce qu’elle ne couvre pas.** De nouveaux concepts — tout ce qui est ici a été vu en Parties I-VII. Les cas mobilisent les méthodes, les acteurs, les outils déjà introduits.
> 
> **Ce que vous saurez faire après cette partie.** Conduire une investigation dark web complète de bout en bout, structurer un programme de veille durable, et faire évoluer votre maturité analytique sur la durée.

-----

### Chapitre 41 — Cas DARKSTREAM complet — investigation d’une vente de données industrielles

Synthèse de l’investigation DARKSTREAM dans une vue intégrée. Ce chapitre rassemble les épisodes du fil rouge en un récit cohérent et pédagogique.

#### 41.1 Le mandat

**Contexte**. Mars 2026. Vectris Aerospace, équipementier européen 4 500 collaborateurs, OIV France, partenaire programmes défense et spatial. Détection interne d’une exfiltration : 420 Go extraits sur 8-14 semaines depuis poste R&D. Mandiant en IR. Recorded Future détecte mention « Vectris » sur forum russophone IndustrialLeaks.

**Mandat Athéna Group** : confirmer/infirmer la circulation des données, authentifier, cartographier l’écosystème, produire rapport actionnable. Coordination DGSI obligatoire (OIV défense). Lucas Ferreira, analyste senior, désigné lead.

**Cadre légal** : DGSI valide chaque action sensible. Pas d’achat, pas de provocation, pas d’engagement ferme. Échantillons OK pour authentification. Documentation rigoureuse, chain of custody.

#### 41.2 Phase 1 — Reconnaissance (semaines 1-2)

**Setup technique**. Whonix avec Tor Browser Safest, machine dédiée, réseau isolé. Personas dédiées avec histoire crédible (« mapletech » — acheteur tech intéressé par specs aéronautiques).

**Documentation IndustrialLeaks**. Forum russophone créé fin 2022, ~3 000 membres, niche données industrielles. 3 changements .onion en 18 mois. Miroir I2P. Accès vouching obligatoire — Athéna mobilise un partenariat pour vouching en coordination DGSI.

**Profil aero_source**. Compte 8 mois, 12 posts, 2 transactions antérieures (5-15k USD). PGP signature stable. Style russophone anglicisé. Profil intermédiaire — pas scammer débutant, pas vétéran majeur.

**Le post**. Titre « EU aerospace supplier, 420GB, propulsion R&D, defense programs inside ». 65 000 USDT demandés. Contact XMPP `aero_source@xmpp.jp`. 5 fichiers échantillons listés en thread.

**Stealer logs Russian Market**. 12 logs Vectris identifiés, dont 3 avec accès VPN corporate + cookies actifs. Hostnames : VECTRIS-RD-112 (poste R&D, central dans la compromission), VECTRIS-SALES-047 (laptop commercial), VECTRIS-IT-008 (poste IT). Datés 2-4 mois — compatibles avec timeline compromission.

#### 41.3 Phase 2 — Authentification (semaines 2-3)

**Contact XMPP avec aero_source** (validation DGSI préalable). Persona « mapletech » présentée crédiblement. Demande échantillons supplémentaires sous prétexte due diligence.

**aero_source répond en 6h**. Cohérent avec opérateur fuseau MSK. Fournit 3 fichiers additionnels via XMPP. Confirme 420 Go. Préfère paiement XMR mais BTC accepté.

**Analyse échantillons en VM isolée**. 8 fichiers totaux :

- Spécifications techniques propulsion (PDF) — métadonnées « Vectris Aerospace », auteur « M. Dubois ».
- Liste fournisseurs 2025 (XLSX) — 340 lignes, contient le **marker interne fictif** Vectris.
- Extrait email interne — boîte ingénieur R&D, discussions techniques inédites.
- Notes de conception, budgets, contrats partenaires.

**Verdict authentification** : **confirmée** avec très haute confiance. Marker interne + cohérence forensics Mandiant + spécificité du contenu.

**Découverte collatérale**. Les 3 logs VPN Russian Market révèlent **2 postes compromis non identifiés** par investigation Vectris interne. Mandiant escalade : isolement, forensics, reset des 2 postes.

#### 41.4 Phase 3 — Pivoting (semaines 3-4)

**Pivots multiples** sur aero_source.

**XSS Forum** : compte « aerosrc » créé il y a 13 mois. Style similaire, même PGP. Activité modeste (4 posts).

**Exploit.in** : compte « aero_src » créé il y a 7 mois. Même PGP. 3 posts dont un sur turbines (cible différente).

**Conclusion pivots PGP** : 95%+ même individu sur 3 forums.

**Wallet BTC**. Cluster Chainalysis de ~40 adresses liées. ~180 000 USDT cumulés sur 14 mois. Flux vers Garantex (avant sanctions 2022), interactions avec adresses BlackSprut (marché drogues russophone).

**Analyse linguistique**. Tics consistants entre les 3 comptes — « dear colleagues », « best regards », fautes prépositions. Russophone, niveau anglais intermédiaire.

**Telegram observation light**. Handle compatible identifié, ancienneté 2 ans, membre canaux cybercriminels russophones. Pas de contact direct (OPSEC, prudence).

#### 41.5 Phase 4 — Reconstitution de la chaîne (semaine 4)

Lucas reconstitue la chaîne probable de compromission Vectris.

**Étape 1** : ingénieur R&D Vectris télécharge un outil CAD crackéé fin 2025. Infostealer Lumma déployé. Log exfiltré.

**Étape 2** : log vendu sur Russian Market fin 2025, ~120 USD (tier corporate VPN + cookies actifs).

**Étape 3** : achat par IAB russophone identifié partiellement comme **magnit_ru** (XSS Forum). Qualification accès VPN, exploration réseau, identification Vectris comme cible aerospace.

**Étape 4** : magnit_ru poste accès sur XSS début 2026 : « Access aerospace EU, R&D network, defense programs ». ~35 000 USD.

**Étape 5** : achat par aero_source ou commanditaire derrière. Hypothèses : (a) aero_source = exfiltrateur direct, (b) front d’une équipe, (c) revendeur acheteur intermédiaire.

**Étape 6** : ~12 semaines d’activité réseau Vectris, 420 Go exfiltrés (cohérent forensics Mandiant).

**Étape 7** : vente sur IndustrialLeaks à 65 000 USDT.

**Au moins 3 acteurs distincts** : opérateur Lumma (infection initiale), magnit_ru (IAB), aero_source (exfiltration finale ou revente).

#### 41.6 Phase 5 — Vérifications anti-faux drapeau (semaine 5)

Hypothèses alternatives testées et écartées.

**H1 — APT étatique déguisé**. Rejetée (probabilité <10%). Profil cybercriminel — style, infrastructure standard, prix dans la norme, pas de TTP sophistiquée, flux vers marché drogues, absence de patterns étatiques.

**H2 — Piège pour Athéna**. Possible mais improbable. Pas de watermarks détectés sur échantillons, pas de exploits identifiés, communications naturelles.

**H3 — Dump n’est pas réellement Vectris**. Rejetée avec très haute confiance. Marker interne + cohérence forensics.

**H4 — aero_source = proxy d’acteur plus grand**. Possible (~25%) mais sans support fort. Style cohérent acteur individuel.

**Conclusion attribution** : **profil cybercriminel russophone individuel** confiance élevée. Motivation financière, pas étatique. Revente future à acteur étatique reste hypothèse ouverte.

#### 41.7 Phase 6 — Production du rapport (semaine 6)

**Pochette de preuves** finale, ~1,2 Go :

- Rapport principal 42 pages signé PGP.
- Annexe A : 147 captures IndustrialLeaks horodatées et hachées.
- Annexe B : conversations XMPP complètes (18 échanges, 4 semaines).
- Annexe C : 8 échantillons authentifiés.
- Annexe D : analyse blockchain cluster aero_source.
- Annexe E : 12 logs Russian Market.
- Annexe F : IoC structurés MISP.
- Annexe G : chain of custody.
- Annexe H : note méthodologique.

**Diffusion** : TLP RED Vectris cellule de crise + RSSI ; TLP AMBER DGSI.

**Recommandations principales** :

- Immédiat : poursuite isolation/reset 3 postes, notification 4 partenaires défense.
- 7 jours : préparation comm client top-20 si escalade.
- 30 jours : durcissement politique téléchargement, EDR renforcé R&D, monitoring continu IndustrialLeaks.
- 90 jours : revue politique credentials, formation sensibilisation, coopération CERT-DEF.

**Limites documentées** :

- Attribution personnelle hors d’atteinte de l’investigation privée.
- Évolution future (revente, publication totale) non prédictible.
- Possibles biais sur-attribution profil russophone à confirmer enrichissement.

#### 41.8 Bilan et apprentissages

**Ce que DARKSTREAM a permis** :

- Confirmation et caractérisation rapides de la circulation dark web (vs incertitude initiale).
- Authentification solide (vs scam/recyclage possible).
- Cartographie des acteurs et de la chaîne probable.
- Découverte collatérale de 2 postes compromis non identifiés.
- Cadre coopératif solide avec DGSI.
- Recommandations défensives applicables.

**Ce que DARKSTREAM n’a pas permis** :

- Identification personnelle d’aero_source (hors d’atteinte privée).
- Récupération des données exfiltrées (impossible).
- Empêchement d’une éventuelle revente future.
- Arrestation des acteurs.

**Apprentissages méthodologiques** :

- L’investigation dark web privée est **caractérisation** + **monitoring** + **conseils défensifs**, pas action coercitive.
- La rigueur OPSEC et procédurale conditionne la valeur du livrable.
- La coordination autorité (DGSI) est multiplier de capacité, pas contrainte.
- Les pivots techniques (PGP, wallet) donnent attribution technique solide ; l’attribution personnelle reste réservée aux États.
- La discipline anti-biais (vérifications faux drapeaux, hypothèses alternatives) protège contre erreurs.

**Apprentissages organisationnels pour Vectris** :

- Le vecteur **stealer log** sur poste personnel ayant credentials professionnels est insuffisamment protégé.
- La détection initiale (8-14 semaines de dwell time) reste trop longue.
- La coordination IR + CTI + LE peut être mieux structurée.
- La protection R&D mérite investissements dédiés (segmentation, durcissement, sensibilisation).

#### 41.9 Le devenir post-DARKSTREAM

**6 mois après livraison** (extrapolation cohérente avec patterns observés) :

- Pas de publication totale du dump observée publiquement.
- aero_source toujours actif sur ses 3 pseudonymes, posts modestes, autres ventes plus petites observées.
- Vectris a déployé toutes les recommandations 30 jours, partiellement les 90 jours.
- Pas de scandale médiatique — l’incident est resté contenu.
- Aucune communication DGSI sur suite éventuelle.

**Hypothèses sur le dump** (sans réponse définitive) :

- Soit un acheteur a payé en privé, dump en circulation restreinte.
- Soit aero_source attend opportunité (autre acheteur, prix maintenu).
- Soit DGSI/partenaires monitorent silencieusement, intervention possible non communiquée.

**Pour Vectris** : l’incident est **caractérisé, contenu, et utilisé pour renforcement durable**. Pas de récupération des données mais pas de catastrophe non plus. Posture défensive significativement améliorée. Coopération DGSI durable établie.

C’est ce que l’investigation dark web privée produit réalistement — pas la récupération magique des données volées, pas l’arrestation héroïque, mais la **caractérisation rigoureuse**, la **réduction d’impact**, et le **renforcement durable**. Souvent suffisant pour faire la différence.

-----

### Chapitre 42 — Cas surveillance d’un leak site ransomware

Cas type complémentaire : surveiller un leak site ransomware ciblant son secteur. Workflow différent de DARKSTREAM (qui répondait à un incident spécifique) — ici, c’est de la **veille proactive** sectorielle.

#### 42.1 Le contexte

**Organisation cible** : grande mutuelle de santé française, 8 M assurés, 12 000 collaborateurs, OIV santé. Données sensibles : dossiers santé, informations financières, identités complètes.

**Mandat veille** : programme CTI dédié, 2 analystes à temps plein. Mission : surveillance continue de l’écosystème ransomware ciblant la santé en Europe, alerte précoce sur menaces sectorielles, threat intel actionable pour SOC + direction.

**Outils** : abonnement Recorded Future (premium), Flare (focus dark web), accès Ransomwatch, monitoring manuel forums et leak sites majeurs. Plateforme MISP interne.

#### 42.2 Le programme de surveillance

**Sources surveillées en continu** :

**Leak sites prioritaires** (15 groupes) : LockBit (relaunch post-Cronos), Black Basta, Play, Akira, RansomHub, Qilin, BianLian, Inc Ransom, Hunters International, Medusa, 8Base, Cl0p, Dragonforce, Rhysida, Brain Cipher.

**Signaux trackés sur chaque leak site** :

- Nouvelles victimes affichées (en particulier secteur santé EU).
- Évolution du rythme (nb par mois) — peut signaler recrutement affiliés ou disruption.
- Changements de design / messaging — indicateur de restructuration.
- Disparition / fragilité — signaux disruption LE.
- Pages témoignages / preuves de paiement — marketing groupe.

**Forums prioritaires** : XSS, Exploit, BreachForums, RAMP. Recherches sur :

- Mots-clés santé, healthcare, médical, hospital, pharma, mutuelle, assurance santé.
- Géographie France, Europe.
- Spécifications techniques de cibles santé.

**Marchés de logs** (Russian Market notamment) : monitoring credentials du domaine de la mutuelle et de ses prestataires identifiés (TPA, hébergeur santé, sous-traitants).

**Canaux Telegram** : canaux spécialisés ransomware, leak channels santé, hacktivisme anti-corporate.

#### 42.3 Workflow type

**Quotidien** (1-2h par analyste) :

- Revue automatisée des alertes Recorded Future.
- Visite manuelle des 5 leak sites les plus actifs.
- Triage : ignorer / surveiller / investiguer.
- Mise à jour du tableau de bord interne.

**Hebdomadaire** :

- Synthèse trends de la semaine pour CISO.
- Revue manuelle approfondie des 15 leak sites.
- Veille forums sur posts pertinents santé.
- Update IoC et règles SIEM si nouvelles observations.

**Mensuel** :

- Rapport mensuel structuré (10-20 pages) pour direction sécurité.
- Statistiques sectorielles santé.
- Revue programme : sources, outils, processus.
- Échange ISAC santé européen.

**Trimestriel** :

- Rapport stratégique direction (60 min présentation).
- Audit du programme.
- Évolution du périmètre.

#### 42.4 Le cas concret : alerte sur Hunters International

**Jour 1 — détection**. Veille matinale, leak site de Hunters International publie nouvelle victime : « MutuelleSanté Régionale » (nom anonymisé), française, 1,2 M assurés. Pas la mutuelle cliente, mais un concurrent direct. Échantillons publiés : extraits de fichiers RH, factures, données médicales.

**Triage initial**. Concurrent direct du client → pertinence haute. Secteur identique → tendance à étudier. Possible spillover si compromission via prestataire commun.

**Investigation jour 1** :

- Vérification de la compromission : recherche de communiqué officiel de la mutuelle concurrente. Pas encore de communication publique.
- Capture du leak site (Hunchly).
- Analyse échantillons publiés (téléchargement en VM isolée).
- Identification potentiels prestataires communs avec mutuelle cliente — vérification que la compromission n’a pas affecté un fournisseur partagé.

**Jour 2 — escalade interne**. Note flash au CISO : compromission concurrent, possible signal de campagne sectorielle. Recommandations : durcissement temporaire, vigilance renforcée SOC.

**Jour 3-7 — investigation approfondie** :

- Recherche TTP Hunters International publiquement documentés.
- Cross-check avec MITRE ATT&CK.
- Identification de l’IAB possible derrière cette compromission (pas trouvé directement, mais profil typique).
- Veille leak site pour évolution (countdown, négociation visible, paiement).

**Jour 14 — escalade**. Hunters publie 30% des données. Nouveau signal — la mutuelle concurrente n’a pas payé. Escalade publication probable.

**Jour 21 — publication totale**. Données complètes publiées (~80 Go). Sur dark web.

**Jour 21+1 — analyse**. Échantillonage du dump (sans téléchargement total, légal/RGPD). Identification :

- Aucune preuve de compromission via prestataire commun.
- TTP cohérents avec un accès initial via VPN compromis.
- Aucune mention de la mutuelle cliente dans le dump.

**Jour 25 — note finale**. Synthèse au CISO :

- Pas d’impact direct sur la mutuelle cliente.
- Tendance Hunters International confirmée — santé EU dans cible.
- Recommandations renforcées : audit VPN, MFA résistant phishing partout, monitoring stealer logs prioritaire.
- Suivi continu du groupe.

#### 42.5 Apprentissages du cas

**Valeur de la veille sectorielle**. La compromission d’un concurrent informe la défense de la cible — mêmes profils, mêmes vecteurs probables. Sans cette veille, la mutuelle cliente n’aurait pas eu le signal.

**Réactivité**. Détection jour 1, escalade jour 2, recommandations jour 3-7. Vitesse compatible avec posture défensive — durcissement possible avant que l’acteur ne pivote vers d’autres cibles.

**Utilisation responsable**. L’investigation portait sur un concurrent — pas d’exploitation commerciale de l’information. Note interne au CISO + ISAC santé partagé (TLP AMBER), pas utilisé en marketing.

**Limites**. La veille ne **prévient** pas les compromissions — elle alerte sur tendances. Sans posture défensive solide en amont, la veille seule ne protège pas.

**Coopération sectorielle**. Le partage avec ISAC santé a permis à plusieurs autres mutuelles d’être informées rapidement. Effet bénéfice collectif de la veille.

-----

### Chapitre 43 — Cas traque d’un Initial Access Broker

Troisième cas type : la **traque d’un IAB** spécifique qui a posté une annonce concernant un type d’organisation que le client surveille.

#### 43.1 Le contexte

**Organisation cible** : grand groupe industriel énergétique français, OIV. RSSI cherche à comprendre les acteurs IAB qui pourraient cibler son secteur.

**Mandat** : investigation sur un IAB spécifique, **acidproxy**, qui a posté il y a 3 jours sur XSS Forum une annonce d’« Access French energy operator, AD admin, 4500 endpoints ». Description compatible avec plusieurs opérateurs énergétiques français. Pas nécessairement le client lui-même, mais investigation requise.

**Objectifs** :

- Identifier (au mieux possible) l’opérateur ciblé.
- Caractériser le profil acidproxy.
- Évaluer si client est concerné directement ou via prestataire.
- Produire intelligence sur ce type d’IAB pour défense préventive.

#### 43.2 Étape 1 — Profilage acidproxy

**Recherche XSS** : compte créé il y a 14 mois. 47 posts. Réputation : 2 reviews positives, 0 négative. Trois transactions confirmées par le forum (escrow). Profil intermédiaire.

**Posts antérieurs** : ventes d’accès dans manufacturing UK, retail DE, healthcare US. **Pas seulement énergie** — opportuniste large.

**Style linguistique** : anglais correct, quelques fautes typiques russophone (articles, prépositions). Tournures cohérentes.

**Pivots** :

- Exploit.in : pas de compte direct identifié.
- BreachForums : compte « acid_proxy » créé 8 mois, 12 posts. Style compatible. PGP **différente** — possible compte secondaire ou chemin distinct.
- Telegram : handle pas identifié dans posts publics.
- XMPP : `acidproxy@xmpp.is` mentionné — serveur classique.

**Wallet BTC** : adresse mentionnée pour 2 transactions antérieures. Cluster Chainalysis : ~25 adresses, ~85 000 USDT cumulés. Flux vers exchange non-KYC + quelques sorties identifiées vers wallet labellisé « Garantex » (avant sanctions 2022).

#### 43.3 Étape 2 — Identification de la cible

**Le post acidproxy** détaille : « French energy operator, ~4500 endpoints, AD admin (DA), Citrix admin, ICS network bridged, sells with proof, PoC available ». Prix demandé : 75 000 USD.

**4 500 endpoints** dans énergie française = environ une dizaine d’opérateurs candidats : majors (EDF, Engie, TotalEnergies subsidiaries), opérateurs régionaux, grandes entreprises de services énergétiques.

**Démarche** : pas de contact direct (risque que acidproxy alerte la cible). Recherche indirect.

**Cross-référencement** :

- Stealer logs Russian Market sur les 10 candidats. Patterns observés : multiples logs sur 3 candidats, mais aucun avec accès AD admin clairement identifié dans les logs.
- Posts adjacents acidproxy mentionnent « access via Fortinet vulnerability » — date de la vulnérabilité Fortinet exploitée massivement courant 2025-2026.
- Recherche de communiqués publics récents — un opérateur régional (« Énergie X » anonymisé) a publié il y a 2 semaines un communiqué mentionnant « incident de sécurité maîtrisé ». Communiqué vague — possible cover up partiel.

**Hypothèse forte** : Énergie X est la cible probable. Pas certitude, mais forte probabilité (75%+).

#### 43.4 Étape 3 — Décision et action

**Le client n’est pas Énergie X**. Mais Énergie X est un partenaire technique (interconnexions réseau électrique).

**Coordination** : le RSSI client contacte le RSSI Énergie X via canal sectoriel (ISAC énergie européen). Information partagée TLP RED.

**Réaction Énergie X** : confirme l’incident. Compromission identifiée 2 semaines plus tôt, en cours de remédiation. acidproxy peut effectivement avoir l’accès. Énergie X mobilise IR pour vérifier si l’accès est encore actif, déconnexion totale en cours. Communication avec ANSSI (déjà notifiée).

**Pour le client** : pas de compromission directe identifiée. Mais l’interconnexion réseau avec Énergie X est mise en revue. Pare-feux durcis, monitoring renforcé sur les flux concernés.

#### 43.5 Étape 4 — Suivi de acidproxy

Au-delà du cas immédiat, la veille acidproxy continue.

**Monitoring posts** : nouvelles annonces sur XSS, Exploit, BreachForums.

**Monitoring wallet** : transactions reçues, flux. Si un acheteur paie acidproxy, la transaction sera traçable.

**Monitoring secondaires** : si Énergie X confirme déconnexion, acidproxy ne peut plus livrer son « produit » → comportement après ?

**Apprentissage durable** : acidproxy est désormais documenté dans la base CTI interne du client. Si acidproxy poste une nouvelle annonce contre un acteur énergie EU, alerte automatique.

#### 43.6 Apprentissages

**Valeur de la veille IAB**. Détecter une annonce IAB **avant** qu’elle aboutisse à une attaque permet alerte précoce — soit pour la cible directe, soit pour l’écosystème adjacent.

**Identification probabiliste**. Sans contact direct (qui alerterait l’IAB), l’identification reste probabiliste. Mais 75%+ probabilité, croisé avec autres signaux (communiqué Énergie X), suffit pour action.

**Coopération sectorielle critique**. Sans ISAC, le client n’aurait pas pu transmettre l’alerte à Énergie X. Le canal ISAC fait la différence.

**Limites**. L’IAB peut continuer ses opérations contre d’autres cibles. La veille permet alertes ponctuelles, pas neutralisation de l’acteur.

**Doctrine**. Pour un OIV, la veille des IAB sectoriels devient stratégique. Investissement justifié par le ROI (une compromission majeure évitée vaut largement le coût annuel d’un programme de veille).

-----

### Chapitre 44 — Maturité analyste et programme de veille durable

Pour conclure, ce chapitre articule la **construction et l’évolution** d’un programme de veille dark web durable. Pas seulement une investigation ponctuelle, mais une capacité organisationnelle continue.

#### 44.1 Les niveaux de maturité

**Niveau 0 — Aucune veille**. L’organisation n’a pas de visibilité sur les menaces dark web la concernant. Découvre les compromissions par signaux externes (presse, autorités, victimes). Posture purement réactive.

**Niveau 1 — Veille ponctuelle**. Quelques alertes par services tiers (Have I Been Pwned, alertes vendor lors de breaches). Pas de programme structuré. Réaction au cas par cas.

**Niveau 2 — Veille basique**. Abonnement plateforme commerciale (SOCRadar, Flare). Triage hebdomadaire. Pas de personnel dédié — fonction adjointe d’un autre rôle.

**Niveau 3 — Programme structuré**. Au moins 1 analyste dédié, abonnement plateforme(s), procédures formalisées, rapports réguliers à direction. Coopération sectorielle (ISAC).

**Niveau 4 — Programme avancé**. Équipe dédiée 2-5 analystes, multiple plateformes, capacité d’investigation directe en .onion (Whonix, OPSEC), MISP interne, threat hunting proactif. Coopération autorités structurée.

**Niveau 5 — Programme leader**. Équipe 5+ analystes spécialisés (CTI, OSINT, blockchain, malware). Recherche propre publiée. Contributions à standards (STIX, MITRE). Liens organiques avec FdO et services. Influence sur secteur.

La plupart des grandes entreprises se situent entre niveaux 2 et 4. Niveau 5 réservé à acteurs majeurs (banques systémiques, GAFAM, certains États).

#### 44.2 La construction d’un programme

**Phase 1 — Cadrage** (1-3 mois) :

- Identification des objectifs (détection compromission, monitoring dirigeants, veille sectorielle, etc.).
- Évaluation des ressources allouables (budget, personnel, outils).
- Identification des sources prioritaires.
- Choix d’un sponsor exécutif.
- Procédures juridiques (cadre légal, validation DSI/juridique).

**Phase 2 — Mise en place** (3-6 mois) :

- Recrutement / désignation analyste(s).
- Souscription abonnements plateformes.
- Setup environnement technique (Whonix, machines dédiées si investigation directe).
- Formation initiale (méthodes, outils, OPSEC).
- Définition des KPIs.
- Procédures d’escalade.

**Phase 3 — Premiers résultats** (6-12 mois) :

- Premiers rapports réguliers.
- Premières alertes traitées.
- Premières corrélations sectorielles.
- Ajustements basés sur feedback.

**Phase 4 — Maturation** (12-24 mois) :

- Programme rodé, processus stabilisés.
- Coopération ISAC active.
- Possibles investigations directes en .onion (selon maturité).
- Threat hunting proactif lié.
- Contribution interne valorisée.

**Phase 5 — Évolution continue** :

- Veille sur l’évolution de l’écosystème (nouveaux groupes, nouveaux marchés, IA).
- Évolution des outils et méthodes.
- Formation continue de l’équipe.
- Possible élargissement (vers SOC augmenté, threat hunting avancé).

#### 44.3 Le profil d’analyste dark web

**Compétences de base** :

- Compréhension de la cybersécurité (vecteurs d’attaque, défense, écosystème criminel).
- Maîtrise des outils techniques (Tor Browser, VM, Hunchly, plateformes CTI).
- Compétences OSINT générales.
- Méthodes analytiques rigoureuses (ACH, vocabulaire calibré, biais).
- Rédaction analytique (notes structurées, executive summary).

**Compétences spécialisées appréciées** :

- **Linguistiques** : russe (incontournable pour l’écosystème dominant), chinois (croissant), arabe, persan.
- **Blockchain** : analyse on-chain, outils Chainalysis/TRM.
- **Malware analysis** basique : reconnaissance familles, IoC.
- **Forensique** basique : métadonnées, timelines.
- **Programmation** : Python notamment pour scripts d’automatisation.

**Compétences transverses** :

- **Curiosité** : essentielle. Le dark web évolue, l’analyste qui ne lit pas les vendor reports et les forums spécialisés se laisse dépasser.
- **Rigueur** : OPSEC, documentation, neutralité analytique.
- **Communication** : adapter le rapport à l’audience (technique, exécutive, juridique, autorités).
- **Patience** : les investigations prennent semaines/mois.
- **Résilience** : exposition à contenus difficiles (CSAM accidentel, violences, manipulation psychologique). Soutien psychologique nécessaire.
- **Éthique** : maintenir distance professionnelle, refuser dérives.

**Profils typiques** :

- Background sécurité technique (red team, IR, SOC) reconverti vers CTI.
- Background renseignement (militaire, services) vers privé.
- Background OSINT / journalisme d’investigation.
- Profils diplômés (master cyber, master renseignement, master géopolitique).

**Rétention** : profil rare et recherché. Marché tendu. Rétention via : formation continue, intérêt missions, salaires compétitifs, qualité management.

#### 44.4 Les KPIs d’un programme

**KPIs quantitatifs** :

- Nombre d’alertes traitées / mois.
- Nombre d’investigations approfondies / mois.
- Temps moyen de détection à action.
- Nombre d’IoC ajoutés au SOC.
- Nombre de notes produites par catégorie.
- Couverture des sources surveillées.

**KPIs qualitatifs** :

- Pertinence des alertes (taux de faux positifs).
- Actionnabilité des recommandations (suivi par destinataires).
- Satisfaction des destinataires (CISO, direction).
- Reconnaissance externe (publications, contributions).
- Contribution sectorielle (ISAC).

**Difficultés** :

- ROI cyber généralement difficile à mesurer (incidents évités sont invisibles).
- Mesurer la valeur ajoutée d’une veille proactive vs scénario sans veille.
- Distinguer succès (détection précoce) de succès apparent (alerte juste générique).

**Approche pragmatique** : combiner KPIs quantitatifs (volumes traités) et qualitatifs (cas marquants, témoignages clients internes). Réviser périodiquement.

#### 44.5 Les pièges du programme à éviter

**Le « rapport pour le rapport »**. Production de rapports non lus. Mesurer la lecture, l’actionnabilité, le feedback. Réduire si nécessaire.

**Le « tout sur dark web »**. Beaucoup de menaces sont sur clear web ou Telegram. Programme dark web pur est trop étroit.

**L’isolation**. Programme veille déconnecté du SOC, IR, communication. Doit être intégré dans gouvernance sécurité.

**La saturation par bruit**. Si triage non rigoureux, l’équipe se noie dans alertes faux positifs et perd de vue les vraies menaces.

**L’obsolescence**. Outils et sources évoluent. Un programme figé sur les pratiques de 2020 ne capte plus les menaces 2025-2026.

**Le burnout**. Exposition continue aux contenus difficiles épuise. Rotation, soutien psychologique, limites horaires.

**La sur-confidence**. Programme avancé = tentation de surévaluer ses capacités. La majorité des compromissions se produisent malgré la veille — humilité.

**La sur-spécialisation**. Analyste ultra-spécialisé risque déconnexion du business. Maintenir compréhension des enjeux organisationnels.

#### 44.6 L’évolution continue

L’écosystème dark web change vite — un programme statique se déclassait. Évolutions à suivre.

**Émergence de nouveaux acteurs**. Groupes ransomware, IAB, opérateurs de plateformes — à intégrer dans monitoring.

**Disparition / migration**. Forums saisis, plateformes déménagées. Mise à jour des sources.

**Nouvelles techniques d’OPSEC**. Acteurs adoptent nouvelles protections (Monero, Lokinet, deep encryption). Adaptation des méthodes investigation.

**IA offensive et défensive**. Évolution rapide. Veille sur outils, formations équipe.

**Réglementaire**. NIS 2 transposée 2024-2025, AI Act, Cyber Resilience Act, DORA. Implications pour le programme.

**Géopolitique**. Tensions Russie-Occident, Chine-Taiwan, Moyen-Orient — affectent l’activité dark web. Veille géopolitique parallèle.

**Coopérations**. ISAC évoluent, nouveaux partenariats, nouveaux standards. Rester partie prenante.

#### 44.7 La place dans l’écosystème de défense

Un programme de veille dark web n’est **qu’une pièce** de la défense globale. Sa place dans l’écosystème.

**Amont** : informe le SOC (IoC), threat hunting (TTP à chercher), gestion des risques (priorisation), direction (décisions stratégiques).

**Aval** : alimenté par signaux internes (alertes SOC, IR, leaks détectés), par sources externes (vendor CTI, ISAC, autorités).

**Latéral** : coopère avec compliance (notification breaches, RGPD), juridique (preuves, procédures), communication (gestion crise), métiers (sensibilisation).

**Externe** : ISAC sectoriels, autorités (ANSSI, DGSI, FdO), pairs RSSI.

Le programme est un **multiplicateur** des autres composantes de la sécurité — il les informe, les alerte, les guide. Sans les autres composantes (SOC, IR, formation, segmentation, etc.), la veille seule ne protège pas.

#### 44.8 Conclusion

Le dark web n’est ni un mythe sensationnaliste, ni une zone hors d’atteinte. C’est un **écosystème connaissable**, avec ses acteurs, ses dynamiques, ses codes — et qu’on peut investiguer méthodiquement, dans le cadre légal et éthique, avec des outils et méthodes maîtrisables.

Un analyste qui maîtrise les fondations (Partie I), les infrastructures (Partie II), les écosystèmes (Partie III), l’économie (Partie IV), les méthodes d’investigation (Partie V), l’analyse (Partie VI), et les usages contemporains (Partie VII) — peut conduire des investigations comme DARKSTREAM (Partie VIII), construire un programme de veille durable, et apporter une valeur défensive réelle à son organisation.

Le métier exige rigueur, curiosité, patience, éthique. Il évolue rapidement. Il expose à des contenus difficiles. Mais il contribue concrètement à la sécurité collective — détection précoce de menaces, alerte sectorielle, soutien aux victimes, coopération avec autorités. Dans un paysage cyber où l’attaquant a souvent l’avantage, chaque détection précoce, chaque investigation rigoureuse, chaque renseignement actionnable réduit l’écart.

Bonne route à l’analyste qui s’engage dans cette pratique.

-----

## ANNEXES

-----

### Annexe A — Glossaire

|Terme                    |Définition                                                                               |
|-------------------------|-----------------------------------------------------------------------------------------|
|**0-day (zero-day)**     |Vulnérabilité non publiquement connue et non patchée par l’éditeur                       |
|**AiTM**                 |Adversary-in-the-Middle — phishing interceptant credentials et cookies de session        |
|**APT**                  |Advanced Persistent Threat — acteur étatique sophistiqué et persistant                   |
|**BEC**                  |Business Email Compromise — fraude par compromission d’email professionnel               |
|**Bulletproof hosting**  |Hébergement résilient aux saisies, dans juridictions peu coopératives                    |
|**CaaS**                 |Crime-as-a-Service — services criminels en abonnement                                    |
|**CSAM**                 |Child Sexual Abuse Material — contenu d’abus sexuel d’enfants                            |
|**Carding**              |Fraude à la carte bancaire                                                               |
|**Chain of custody**     |Traçabilité d’une preuve depuis collecte jusqu’à exploitation                            |
|**Clearnet**             |Internet de surface accessible via navigateurs classiques                                |
|**CTI**                  |Cyber Threat Intelligence — renseignement sur les cybermenaces                           |
|**DDoS**                 |Distributed Denial of Service — attaque par déni de service distribué                    |
|**Deep web**             |Contenu web non indexé par moteurs de recherche généralistes                             |
|**Dark web**             |Sous-ensemble du deep web accessible via darknets (Tor, I2P, etc.)                       |
|**Darknet**              |Réseau overlay conçu pour l’anonymat (Tor, I2P, Freenet)                                 |
|**DLT**                  |Distributed Ledger Technology — technologies de registre distribué (incluant blockchains)|
|**Doxing**               |Publication d’informations personnelles d’une cible                                      |
|**DPI**                  |Deep Packet Inspection — inspection en profondeur du trafic réseau                       |
|**Dwell time**           |Temps entre compromission initiale et détection                                          |
|**EDR**                  |Endpoint Detection and Response — outil de détection sur poste de travail                |
|**Eepsite**              |Site hébergé sur le réseau I2P (.i2p)                                                    |
|**Escrow**               |Tiers de confiance détenant fonds entre acheteur et vendeur                              |
|**Exit node**            |Dernier nœud d’un circuit Tor, qui parle au site de destination                          |
|**Exit scam**            |Disparition des opérateurs avec les fonds en escrow                                      |
|**Fullz**                |Identité complète volée (nom, SSN, adresse, etc.)                                        |
|**FUD**                  |Fully Undetected — malware indétectable par antivirus                                    |
|**Garlic routing**       |Routage anonyme utilisé par I2P (variante de l’onion routing)                            |
|**Guard relay**          |Premier nœud d’un circuit Tor (côté client)                                              |
|**Hidden service**       |Service .onion, accessible uniquement via Tor                                            |
|**Hacktivisme**          |Activisme cyber motivé idéologiquement                                                   |
|**IAB**                  |Initial Access Broker — courtier vendant des accès compromis                             |
|**IoC**                  |Indicator of Compromise — artefact technique d’une compromission                         |
|**ISAC**                 |Information Sharing and Analysis Center — centre de partage sectoriel                    |
|**JID**                  |Jabber ID — identifiant utilisateur sur réseau XMPP                                      |
|**KYC**                  |Know Your Customer — vérification d’identité client                                      |
|**Leak site**            |Vitrine publique d’un groupe ransomware (revendications, échantillons)                   |
|**LotL**                 |Living off the Land — usage d’outils légitimes pour furtivité                            |
|**MaaS**                 |Malware-as-a-Service — location de malware                                               |
|**MFA**                  |Multi-Factor Authentication                                                              |
|**NIT**                  |Network Investigative Technique — technique policière d’identification                   |
|**NIS 2**                |Directive UE 2022/2555 sur la cybersécurité                                              |
|**OIV**                  |Opérateur d’Importance Vitale (France)                                                   |
|**OFAC**                 |Office of Foreign Assets Control (US) — sanctions économiques                            |
|**Onion routing**        |Protocole de routage anonyme par chiffrement en couches (utilisé par Tor)                |
|**OPSEC**                |Operations Security — sécurité opérationnelle                                            |
|**OSINT**                |Open Source Intelligence — renseignement de source ouverte                               |
|**PASSI**                |Prestataire d’Audit SSI qualifié ANSSI                                                   |
|**PDIS**                 |Prestataire de Détection d’Incidents de Sécurité ANSSI                                   |
|**PRIS**                 |Prestataire de Réponse aux Incidents de Sécurité ANSSI                                   |
|**PGP**                  |Pretty Good Privacy — standard de chiffrement et signature                               |
|**PhaaS**                |Phishing-as-a-Service                                                                    |
|**PSO**                  |Private Sector Offensive — fournisseur commercial d’outils offensifs (NSO, etc.)         |
|**RaaS**                 |Ransomware-as-a-Service                                                                  |
|**RAT**                  |Remote Access Trojan — cheval de Troie d’accès à distance                                |
|**RGPD**                 |Règlement Général sur la Protection des Données (UE)                                     |
|**SCAM**                 |Arnaque                                                                                  |
|**Stealer (infostealer)**|Malware spécialisé dans le vol de données de session                                     |
|**Stealer log**          |Output d’un infostealer — données extraites d’une victime                                |
|**STIX/TAXII**           |Standards d’échange de threat intelligence                                               |
|**Sock puppet**          |Faux compte créé pour simuler activité ou influence                                      |
|**SSO**                  |Single Sign-On — authentification unifiée                                                |
|**TLP**                  |Traffic Light Protocol — classification de partage (RED/AMBER/GREEN/CLEAR)               |
|**TOX**                  |Protocole de messagerie peer-to-peer chiffré                                             |
|**TTP**                  |Tactics, Techniques, and Procedures                                                      |
|**VM**                   |Virtual Machine — machine virtuelle                                                      |
|**Vouching**             |Parrainage d’un nouveau membre par un membre établi                                      |
|**WEP**                  |Words of Estimative Probability — vocabulaire calibré de probabilité                     |
|**XMPP / Jabber**        |Protocole de messagerie ouvert et chiffrable                                             |

-----

### Annexe B — Typologie des espaces dark web

#### B.1 Forums

|Type                              |Exemples                                                   |Caractéristiques principales                   |
|----------------------------------|-----------------------------------------------------------|-----------------------------------------------|
|Généralistes cybercrime russophone|XSS Forum, Exploit.in                                      |Vouching strict, vétérans, tout type d’activité|
|Généralistes cybercrime anglophone|BreachForums (multiple instances)                          |Plus accessible, vente de données dominante    |
|Spécialisés carding               |BriansClub, WWH Club                                       |Fraude bancaire, dumps                         |
|Spécialisés données               |IndustrialLeaks (fictif), BreachForums (data leaks section)|Vente de breaches, accès                       |
|Hacktivisme                       |Variés selon causes                                        |Coordination idéologique, revendications       |
|Géographiques                     |Forums chinois, persophones, arabophones                   |Barrière linguistique, communautés régionales  |

#### B.2 Marchés

|Type                  |Exemples actuels (2025-2026)      |Spécialités                            |
|----------------------|----------------------------------|---------------------------------------|
|Généralistes          |Abacus, TorZon, MGM Grand         |Drogues + digital goods                |
|Russophones post-Hydra|BlackSprut, OMG!OMG!, Mega, Kraken|Drogues, dead drops, bloc russophone   |
|Logs                  |Russian Market                    |Stealer logs avec recherche par domaine|
|Fraude                |BriansClub, WWH Club              |Cartes, comptes bancaires              |
|Spécialisés malware   |Variés sur forums                 |Crypters, loaders, RAT                 |

#### B.3 Leak sites ransomware

|Famille                                                                    |Statut 2025-2026                                             |
|---------------------------------------------------------------------------|-------------------------------------------------------------|
|LockBit                                                                    |Affecté Cronos février 2024, relaunch fragile                |
|ALPHV / BlackCat                                                           |Disparu mars 2024 (exit scam suspecté post-Change Healthcare)|
|Black Basta                                                                |Actif, ciblage enterprise large                              |
|Cl0p                                                                       |Actif, exploitation edge devices (MOVEit, Oracle EBS)        |
|Play / PlayCrypt                                                           |Actif depuis 2022                                            |
|Akira                                                                      |Émergent fin 2023, croissance rapide                         |
|RansomHub                                                                  |Émergent mi-2024, croissance forte                           |
|Qilin                                                                      |Actif, Synnovis/NHS notamment                                |
|BianLian                                                                   |Extorsion sans chiffrement depuis 2023                       |
|Medusa, 8Base, Hunters Intl, Inc Ransom, Dragonforce, Rhysida, Brain Cipher|Actifs, à surveiller                                         |

#### B.4 Messageries

|Plateforme      |Usage typique                                             |
|----------------|----------------------------------------------------------|
|Telegram        |Coordination, canaux publics, leaks. Durci post-Durov 2024|
|XMPP / Jabber   |Russophone classique, OTR/OMEMO, persistance              |
|TOX             |Peer-to-peer, communications très sensibles               |
|Matrix / Element|Fédéré, en croissance post-Durov                          |
|Session         |Sur Lokinet, anonymat strong, croissance                  |
|Signal          |Activistes, journalistes ; moins cybercrime sophistiqué   |

#### B.5 Sites légitimes en .onion

|Catégorie        |Exemples                                              |
|-----------------|------------------------------------------------------|
|Médias           |BBC, NYT, ProPublica, Le Monde, WaPo, Der Spiegel     |
|Recherche        |DuckDuckGo, Wikipedia (miroir)                        |
|ONG              |Amnesty International, Reporters Sans Frontières      |
|Plateformes      |Facebook, Twitter (historique), Protonmail            |
|Lanceurs d’alerte|SecureDrop instances (NYT, Guardian, etc.), GlobaLeaks|
|Communauté       |Tor Project miroirs, Ahmia, archives forum            |

-----

### Annexe C — OPSEC analyste : checklists

#### C.1 Préparation environnement (avant première session)

- [ ] **Machine dédiée** : ordinateur séparé de l’usage personnel et professionnel courant.
- [ ] **OS dédié** : Whonix (Gateway + Workstation), Tails, ou Qubes OS. Pas Windows / macOS personnel.
- [ ] **Réseau isolé** : connexion Internet séparée si possible (clé 4G dédiée, ou réseau invité, pas réseau corporate principal).
- [ ] **Tor Browser configuré** : mode Safest activé par défaut, vérification version à jour.
- [ ] **VM de manipulation** : VM jetable pour ouvrir échantillons (Windows 10 sandbox, ou Linux jetable).
- [ ] **Outils installés** : Hunchly ou équivalent capture, exiftool, hash utilities, scripts custom.
- [ ] **Pas de comptes personnels** sur la machine (mail perso, RS, banque — interdit).

#### C.2 Préparation persona

- [ ] **Pseudonyme unique** non lié à l’analyste ou ses identités antérieures.
- [ ] **Histoire crédible** : background fictif documenté (origine, métier, intérêts).
- [ ] **Style linguistique cohérent** avec l’origine prétendue.
- [ ] **Email jetable** sur service approprié (protonmail, autre).
- [ ] **Compte sur forum cible** : créé avec délai progressif d’activité, pas immédiat.
- [ ] **PGP key dédiée** à la persona, pas réutilisée d’ailleurs.
- [ ] **JID XMPP** dédié sur serveur approprié.
- [ ] **Maintenance** : posts occasionnels même hors investigation pour crédibilité.

#### C.3 Pendant chaque session

- [ ] **Vérification Tor Browser à jour** avant lancement.
- [ ] **Mode Safest confirmé** (icône bouclier).
- [ ] **Capture systématique** activée (Hunchly).
- [ ] **Notes en temps réel** : URL visitées, observations, hypothèses.
- [ ] **Pas de comptes personnels** ouverts en parallèle.
- [ ] **Aucun téléchargement direct** sur OS hôte — toujours en VM isolée.
- [ ] **Vérification adresse .onion** sur 2 sources avant accès à un service inconnu.
- [ ] **Pas de JS activé sauf nécessité absolue** identifiée.
- [ ] **Logs OTR/OMEMO** des sessions XMPP archivés.

#### C.4 Post-session

- [ ] **Capture finale** complète (Hunchly export, ou archives manuelles).
- [ ] **Hashing** des fichiers téléchargés (SHA-256 minimum).
- [ ] **Documentation chronologique** dans le journal d’investigation.
- [ ] **Pas de copie hors environnement sécurisé** des données collectées.
- [ ] **Snapshot VM** restauré si modifications.
- [ ] **Mise à jour du graphe d’investigation** (entités, relations).

#### C.5 Communication équipe

- [ ] **Validation hiérarchie** pour actions sensibles (contact vendeur, paiement, téléchargement).
- [ ] **Briefing pair** sur évolutions importantes.
- [ ] **Coordination autorités** maintenue selon mandat.
- [ ] **Confidentialité** stricte — pas de partage avec tiers non habilités.
- [ ] **Debriefing psychologique** disponible si exposition à contenus difficiles.

#### C.6 Signaux d’alerte (compromission persona)

- [ ] **Pseudo identifié** par cibles (contre-investigation, mention « cet acteur est suspect »).
- [ ] **Comportements de contact étranges** (over-cooperation soudaine, demandes inhabituelles).
- [ ] **Tentatives techniques** (envoi de fichiers piégés évidents, liens suspects).
- [ ] **Mentions du nom réel** ou organisation dans communications.
- [ ] **Patterns de surveillance** observés.

→ En cas de signal, **abandonner la persona immédiatement**, ne pas chercher à la « sauver », escalade hiérarchique, debriefing.

-----

### Annexe D — Outils d’investigation dark web

#### D.1 Environnements et navigateurs

|Outil                  |Usage                              |Coût                |
|-----------------------|-----------------------------------|--------------------|
|**Tor Browser**        |Navigation .onion (référence)      |Gratuit, open source|
|**Tails**              |Distribution Linux live (USB)      |Gratuit, open source|
|**Whonix**             |Architecture VM Gateway+Workstation|Gratuit, open source|
|**Qubes OS**           |OS isolation par VM                |Gratuit, open source|
|**VirtualBox / VMware**|Hyperviseur pour VM jetables       |Gratuit / payant    |

#### D.2 Capture et documentation

|Outil                   |Usage                                         |Coût                    |
|------------------------|----------------------------------------------|------------------------|
|**Hunchly**             |Capture structurée d’investigation, horodatage|Commercial (~130 USD/an)|
|**OSINT Cloner**        |Alternative open source                       |Gratuit                 |
|**wget / curl + torify**|Récupération CLI via Tor                      |Gratuit                 |
|**Aquatone**            |Capture screenshot en masse                   |Gratuit, open source    |
|**Eyewitness**          |Reconnaissance web automatique                |Gratuit, open source    |
|**OnionScan**           |Audit OPSEC de services .onion                |Gratuit, open source    |

#### D.3 Plateformes commerciales CTI

|Plateforme               |Force principale                     |Ordre de prix      |
|-------------------------|-------------------------------------|-------------------|
|**Recorded Future**      |Vision globale, intégration extensive|100k - 500k+ USD/an|
|**Flashpoint**           |Russophone, Telegram                 |100k - 300k USD/an |
|**Intel471**             |Acteurs, cybercrime profondeur       |100k - 300k USD/an |
|**SOCRadar**             |Rapport qualité/prix, PME-friendly   |30k - 100k USD/an  |
|**Flare**                |Niche dark web et data leaks         |30k - 100k USD/an  |
|**DarkOwl**              |Crawling .onion étendu               |50k - 200k USD/an  |
|**Cybersixgill** (Zenity)|Profilage, attribution               |100k - 300k USD/an |
|**Hudson Rock**          |Stealer logs spécialisé              |30k - 100k USD/an  |
|**KELA**                 |Russophone fort                      |100k - 300k USD/an |
|**Group-IB**             |Vision Europe/Asie                   |100k - 300k USD/an |

#### D.4 OSINT et pivoting

|Outil                                   |Usage                           |
|----------------------------------------|--------------------------------|
|**Maltego**                             |Graphing relations entités      |
|**SpiderFoot**                          |Reconnaissance automatisée      |
|**Have I Been Pwned**                   |Vérification breaches publics   |
|**DeHashed**                            |Recherche dans dumps publics    |
|**LeakCheck, Snusbase**                 |Bases de breach                 |
|**IntelX**                              |Archives leaks et .onion        |
|**GitHub dorking**                      |Secrets dans repos publics      |
|**Reverse image search**                |Google Images, TinEye, Yandex   |
|**DomainTools, SecurityTrails, ViewDNS**|WHOIS, DNS history              |
|**Shodan, Censys**                      |Recherche infrastructure exposée|

#### D.5 Analyse blockchain

|Outil                              |Force                                    |
|-----------------------------------|-----------------------------------------|
|**Chainalysis** (Reactor, KYT)     |Standard industrie, labellisation massive|
|**TRM Labs** (Forensics)           |Compliance et investigation              |
|**Elliptic** (Navigator)           |Graphing et labellisation                |
|**CipherTrace**                    |Mastercard subsidiary                    |
|**Crystal**                        |Bitfury subsidiary                       |
|**Breadcrumbs.app**                |Open access partiel                      |
|**OXT.me**                         |Open Bitcoin analysis                    |
|**WalletExplorer**                 |Clustering basique                       |
|**Blockstream.info, Mempool.space**|Bitcoin explorers                        |
|**Etherscan, Tronscan**            |Ethereum, TRON explorers                 |

#### D.6 Threat intelligence platforms

|Plateforme                                         |Usage                                  |
|---------------------------------------------------|---------------------------------------|
|**MISP**                                           |Plateforme open source de partage d’IoC|
|**OpenCTI**                                        |Plateforme open source TI              |
|**Anomali ThreatStream, ThreatConnect, EclecticIQ**|Commerciales                           |
|**Recorded Future, Flashpoint, etc.**              |Plateformes commerciales (incluent TIP)|

#### D.7 Surveillance leak sites

|Outil                        |Usage                             |
|-----------------------------|----------------------------------|
|**Ransomwatch**              |Archive open source des leak sites|
|**Ransomfeed.it**            |Agrégateur public                 |
|**SOCRadar Threat Hunting**  |Commercial                        |
|**DarkOwl Vision**           |Commercial                        |
|**Plateformes générales CTI**|Recorded Future, Flare, etc.      |

#### D.8 Outils analyse fichiers

|Outil                           |Usage                 |
|--------------------------------|----------------------|
|**exiftool**                    |Extraction métadonnées|
|**VirusTotal**                  |Scan multi-AV         |
|**Hybrid Analysis, Joe Sandbox**|Sandboxing            |
|**ANY.RUN**                     |Sandboxing interactif |
|**CyberChef**                   |Conversions, decoding |
|**Wireshark**                   |Analyse réseau        |
|**Volatility**                  |Analyse mémoire       |

#### D.9 Communication chiffrée

|Outil               |Usage                          |
|--------------------|-------------------------------|
|**GPG / GnuPG**     |Signature et chiffrement PGP   |
|**Pidgin + OTR**    |XMPP avec chiffrement          |
|**Signal, Wire**    |Messagerie chiffrée pour équipe|
|**Element / Matrix**|Communication chiffrée fédérée |
|**OnionShare**      |Partage de fichiers via Tor    |

-----

### Annexe E — Grille d’évaluation de crédibilité

Outil pour évaluer rapidement la crédibilité d’une annonce de breach, vente de données, ou autre contenu dark web.

#### E.1 Grille produit / annonce

|Critère                     |Indicateurs positifs (crédibilité ↑)       |Indicateurs négatifs (crédibilité ↓)           |
|----------------------------|-------------------------------------------|-----------------------------------------------|
|**Vendeur — ancienneté**    |Compte 12+ mois, posts réguliers           |Compte récent (<3 mois), peu d’activité        |
|**Vendeur — réputation**    |100+ transactions, feedback 95%+           |Pas de transactions visibles, pas de vouching  |
|**Vendeur — signature**     |PGP stable, signée systématiquement        |Pas de PGP, ou clé récente/changée             |
|**Forum**                   |Forum sérieux à vouching (XSS, Exploit)    |Forum public ou low-end                        |
|**Description**             |Spécifique, technique, cohérente           |Générique, vague, exagérée                     |
|**Volumétrie**              |Cohérente avec ce qui est plausible        |Disproportionnée (« 100 To en exclusivité »)   |
|**Échantillons**            |Disponibles, vérifiables                   |Refusés, vagues, ou demandant paiement         |
|**Prix**                    |Cohérent avec marché (voir Ch.14)          |Anormalement bas (scam) ou absurde             |
|**Méthode contact**         |Standard (XMPP, forum)                     |Telegram nouveau, email gratuit douteux        |
|**Métadonnées échantillons**|Cohérentes avec organisation présumée      |Vagues, génériques, ou contradictoires         |
|**Timing**                  |Cohérent avec compromission documentable   |Timing improbable (avant événement déclencheur)|
|**Markers internes**        |Présents (noms internes, codes spécifiques)|Absents ou contredits                          |
|**Cohérence cross-source**  |Corroboration sur autres canaux            |Source unique, non-corroboré                   |

#### E.2 Scoring rapide

Scoring informel : pour chaque critère, +1 (positif), 0 (neutre/incertain), -1 (négatif). Sommer.

- **+8 et plus** : très probablement authentique. Investigation approfondie justifiée.
- **+3 à +7** : probablement authentique avec réserves. Investigation prudente.
- **0 à +2** : ambigu. Recherche supplémentaire avant conclusion.
- **-3 à -1** : probablement scam ou recyclage. Faible priorité.
- **-4 et moins** : très probablement fake/scam. Classer.

Le scoring est un **outil d’orientation**, pas une vérité. Une investigation peut justifier d’un cas avec score modeste si certains critères sont déterminants (par exemple : marker interne unique = suffit à confirmer authenticité même si autres critères neutres).

#### E.3 Grille acteur (pseudonyme)

Pour évaluer la crédibilité d’un acteur observé (vendeur, IAB, opérateur).

|Critère                |Évaluation                            |
|-----------------------|--------------------------------------|
|Ancienneté du compte   |Mois / années                         |
|Volume de posts        |Nombre, fréquence                     |
|Activité par catégorie |Quels types de produits/services      |
|Transactions confirmées|Nombre, montants, types               |
|Feedback / ratings     |Distribution positive/négative        |
|Vouching               |Qui vouche, quels niveaux             |
|Présence multi-forum   |Quels forums, cohérence               |
|PGP                    |Stable ? Reconnue cross-platform ?    |
|Style linguistique     |Cohérence, langue maternelle apparente|
|Wallet crypto          |Activité, cluster, exchanges          |
|Disputes               |Litiges historiques, résolutions      |

Sortie : profil structuré du vendeur en 1-2 pages, base de tout dossier d’investigation sur cet acteur.

#### E.4 Pièges classiques à vérifier

- **Recyclage** : la donnée vient-elle d’un breach antérieur connu ? Vérifier HIBP, DeHashed.
- **Composition factice** : assemblage de plusieurs breaches anciens présenté comme nouveau ?
- **Watermark / honeypot** : la donnée contient-elle des markers qui pourraient identifier les acheteurs ou les diffuseurs ?
- **False flag** : le profil de l’acteur est-il cohérent ou semble-t-il « designed » pour pointer vers une autre attribution ?
- **Pression temporelle artificielle** : le vendeur impose-t-il « offre 24h » pour empêcher due diligence ?
- **Prix incohérent** : trop bas (scam) ou trop élevé sans justification ?

-----

### Annexe F — Templates de livrables

#### F.1 Template flash alert (1-2 pages)

```markdown
# FLASH ALERT — [Titre court]

**Référence** : FA-YYYYMMDD-NNN
**Date** : YYYY-MM-DD HH:MM (UTC+2)
**Auteur** : [Nom]
**Classification** : TLP:[RED/AMBER/GREEN/CLEAR]
**Destinataires** : [Liste]

## Synthèse (3-5 lignes)
[Que se passe-t-il ? Pourquoi maintenant ? Quel niveau de confiance ?]

## Observation
[Faits factuels, sources, timestamps]

## Implication immédiate
[Pourquoi ça concerne le destinataire]

## Action recommandée
- [Action 1, immédiat]
- [Action 2, dans la journée]
- [Action 3, dans la semaine]

## Limites
[Incertitudes, ce qu'on ne sait pas]

## Source(s)
[URL, plateforme, capture en annexe]

## Annexes
- A : Capture(s) horodatée(s) et hachée(s)
- B : Hashes (SHA-256)
```

#### F.2 Template intel note (3-8 pages)

```markdown
# INTEL NOTE — [Titre]

**Référence** : IN-YYYYMMDD-NNN
**Date de rédaction** : YYYY-MM-DD
**Version** : 1.0
**Auteur** : [Nom]
**Classification** : TLP:[RED/AMBER/GREEN/CLEAR]
**Destinataires** : [Liste]

## Executive Summary (½ page max)
[Réponses aux questions : que s'est-il passé ? Pourquoi est-ce important ? Que faut-il faire ? Quel niveau de confiance ?]

## Contexte
[Pourquoi cette note ? Quel événement déclencheur ? Quelles observations antérieures pertinentes ?]

## Observations
### Observation 1 : [Titre]
- Source, date, capture
- Description factuelle

### Observation 2 : [Titre]
[...]

## Analyse
[Interprétation, attribution, hypothèses testées, conclusions calibrées]

## Implications
[Risques pour le destinataire, impacts potentiels]

## Recommandations
1. **Immédiat (24-48h)** : [Action]
2. **Court terme (7 jours)** : [Action]
3. **Moyen terme (30 jours)** : [Action]
4. **Long terme (90 jours)** : [Action]

## Limites et incertitudes
[Ce qui n'est pas connu, ce qui pourrait changer l'analyse]

## Indicators (IoC)
[Adresses, domaines, hashes, pseudonymes — selon TLP]

## Annexes
A. Captures horodatées
B. Communications archivées
C. Analyses techniques
D. Chain of custody
```

#### F.3 Template bulletin sectoriel mensuel

```markdown
# BULLETIN MENSUEL — Menaces dark web — [Secteur] — [Mois Année]

**Auteur** : [Nom]
**Période** : [Mois] YYYY
**Classification** : TLP:[]
**Destinataires** : []

## Synthèse exécutive (1 page)
[Tendances majeures du mois, événements significatifs, recommandations stratégiques]

## Statistiques du mois
[Nombre revendications ransomware, top 5 acteurs, volumes leak detected, etc.]

## Événements significatifs
[Top 5-10 événements affectant le secteur ce mois]

## Acteurs en évolution
[Nouveaux groupes, disparitions, restructurations]

## Tendances observées
[Patterns émergents, vecteurs montants, géographies]

## Cas remarquables
[1-3 cas illustratifs avec leçons]

## Recommandations actionnables
[Priorisées par horizon temporel]

## Veille à venir
[Quoi surveiller le mois prochain]

## Annexes
[Détails par catégorie, IoC consolidés, statistiques détaillées]
```

#### F.4 Template rapport d’investigation (cas type DARKSTREAM)

```markdown
# RAPPORT D'INVESTIGATION — [Nom de l'opération]

**Référence** : INV-YYYYMMDD-NNN
**Date** : YYYY-MM-DD
**Version** : [N.N]
**Auteur principal** : [Nom]
**Investigateurs associés** : [Noms]
**Classification** : TLP:[]
**Destinataires** : [Liste]

## Executive Summary
[½ - 1 page max — tout ce qui compte si rien d'autre n'est lu]

## Mandat et cadre
- Donneur d'ordre, objectifs, contraintes
- Cadre légal, autorités impliquées
- Périmètre d'investigation

## Méthodologie
- Outils, sources, période d'investigation
- Personas utilisées
- Limites méthodologiques connues

## Phase 1 — Reconnaissance
[Description détaillée, captures pertinentes]

## Phase 2 — Authentification
[Méthodes, résultats, niveau de confiance]

## Phase 3 — Pivoting et corrélation
[Pivots effectués, résultats, graphes]

## Phase 4 — Analyse et attribution
[Hypothèses testées, conclusion calibrée]

## Phase 5 — Vérifications anti-désinformation
[False flags écartés, biais identifiés]

## Conclusions
[Synthèse des constatations]

## Implications pour le client
[Risques, impacts, échéances]

## Recommandations
[Priorisées, avec délais et destinataires]

## Limites et incertitudes
[Ce qui ne peut être conclu avec les moyens employés]

## Annexes
A. Captures forum (avec hashes)
B. Communications archivées
C. Échantillons et analyses
D. Analyse blockchain
E. IoC structurés (MISP/STIX)
F. Chain of custody
G. Note méthodologique
H. Bibliographie / sources externes
```

#### F.5 Template fiche IoC

```markdown
# FICHE IoC — [Identifiant ou pseudonyme]

**Type** : [Pseudonyme / Adresse crypto / Domaine / IP / Hash / etc.]
**Valeur** : [Indicator]
**Classification** : TLP:[]
**Date première observation** : YYYY-MM-DD
**Date dernière observation** : YYYY-MM-DD
**Confiance** : [WEP : très probable / probable / possible]

## Description
[Contexte, lien avec quel acteur/groupe/campagne]

## Sources de l'observation
[Forum/marché, URL, post ID, captures]

## Liens connus
[Autres IoC liés : autres pseudonymes, wallets, domaines]

## Recommandation
[Bloquer / Surveiller / Enquêter]

## Source originale
[Référence du rapport / investigation]
```

#### F.6 Template note IAB (pour suivi)

```markdown
# FICHE IAB — [Pseudonyme]

**Pseudonymes connus** : [Liste cross-forum]
**Forums présents** : [XSS, Exploit, BreachForums, etc.]
**Première observation** : YYYY-MM-DD
**Dernière observation** : YYYY-MM-DD

## Profil
- Ancienneté
- Style et qualité des posts
- Réputation observée
- Langues utilisées
- Fuseau horaire estimé

## Spécialisation
- Types d'accès vendus (VPN/RDP/Citrix/AD)
- Secteurs ciblés
- Géographies
- Niveau de privilèges typique

## Tarification observée
- Prix moyens demandés
- Évolutions

## Wallet crypto
- Adresses observées
- Cluster (lien Chainalysis/TRM si applicable)
- Exchanges traversés

## Réseau
- Voucheurs
- Acheteurs identifiés
- Partenaires fréquents

## Risque pour client
[Évaluation actualisée]

## Recommandations
[Surveillance, détection préventive, etc.]
```

-----

### Annexe G — Ressources et veille

#### G.1 Rapports annuels et périodiques de référence

**Sur les ransomware et leak sites** :

- Coveware (rapports trimestriels) — taux de paiement, montants, secteurs.
- Chainalysis Crypto Crime Report (annuel) — flux financiers ransomware, mixers, sanctions.
- Mandiant M-Trends (annuel) — incidents IR, tendances.
- Sophos State of Ransomware (annuel) — impacts, paiements, défense.
- Recorded Future Annual Threat Report.
- ENISA Threat Landscape (annuel).

**Sur le dark web et cybercrime généraliste** :

- SOCRadar Annual Dark Web Report.
- Flashpoint Cyber Threat Intelligence Report.
- Group-IB Hi-Tech Crime Trends.
- Kela State of Initial Access Brokers.
- Hudson Rock Stealer Report.
- Cyberint Annual Cybercrime Report.

**Sectoriels** :

- FS-ISAC reports (finance).
- H-ISAC reports (santé).
- Verizon DBIR (Data Breach Investigations Report).
- IBM Cost of a Data Breach Report.

**Académiques et recherche** :

- Journal of Cybersecurity, ACM digital library.
- Citizen Lab (University of Toronto) — surveillance, dissidents.
- VirusBulletin Conference papers.
- Black Hat / DEF CON briefings.

#### G.2 Vendors et plateformes commerciales — sites de référence

|Vendor                       |Site                  |Spécificité          |
|-----------------------------|----------------------|---------------------|
|Recorded Future              |recordedfuture.com    |Vision globale CTI   |
|Flashpoint                   |flashpoint.io         |Russophone, Telegram |
|Intel471                     |intel471.com          |Cybercrime profondeur|
|SOCRadar                     |socradar.io           |Rapport qualité-prix |
|Flare                        |flare.io              |Dark web specialist  |
|Mandiant (Google)            |mandiant.com          |IR + threat intel    |
|CrowdStrike                  |crowdstrike.com       |EDR + intel          |
|Microsoft Threat Intelligence|microsoft.com/security|Vision Microsoft     |
|Sekoia                       |sekoia.io             |CTI européen         |
|Group-IB                     |group-ib.com          |Vision Asie/Russie   |
|KELA                         |kela.com              |Russophone fort      |
|Cybersixgill (Zenity)        |cybersixgill.com      |Profilage            |
|Hudson Rock                  |hudsonrock.com        |Stealer logs         |
|DarkOwl                      |darkowl.com           |Crawling .onion      |

#### G.3 Sources gouvernementales et institutionnelles

**France** :

- ANSSI : ssi.gouv.fr — Bulletins, alertes, rapports.
- CERT-FR : cert.ssi.gouv.fr — Avis, alertes opérationnelles.
- DGSI : dgsi.interieur.gouv.fr — Cadre contre-ingérence.
- Cybermalveillance : cybermalveillance.gouv.fr — Grand public et PME.

**Europe** :

- ENISA : enisa.europa.eu — Reports, threat landscape.
- CERT-EU : cert.europa.eu.
- Europol EC3 : europol.europa.eu.
- Pall Mall Process : initiative régulation PSO.

**International** :

- CISA : cisa.gov (US) — Alerts, advisories, campaigns.
- NCSC : ncsc.gov.uk (UK) — Alerts, guidance.
- BSI : bsi.bund.de (Allemagne).
- ACSC : cyber.gov.au (Australie).
- CCCS : cyber.gc.ca (Canada).
- Interpol : interpol.int.

#### G.4 Communautés et forums professionnels

- **FIRST** (Forum of Incident Response and Security Teams) : first.org — communauté CSIRT internationale.
- **CSIRT national** (France) : Renater pour académique, par secteur ailleurs.
- **ISAC sectoriels** : FS-ISAC (finance), H-ISAC (santé), E-ISAC (énergie), R-CISC (retail), Aviation-ISAC, ASD-EUROSPACE/AIAC (aerospace).
- **MISP communauté** : misp-project.org — partage IoC.
- **CIRCL Luxembourg** : circl.lu — CSIRT et MISP.
- **OSINT communities** : Bellingcat, Citizen Lab, OSINT Curious.

#### G.5 Conférences et événements

**Internationaux** :

- Black Hat USA, DEF CON, Black Hat Europe — Las Vegas, Londres.
- RSA Conference — San Francisco.
- FIRST Annual Conference.
- Virus Bulletin (VB).
- Botconf — recherche botnets.

**Européens / francophones** :

- SSTIC (Rennes, juin) — francophone référence.
- FIC (Lille puis Marseille, janvier) — institutionnel français.
- Hack.lu (Luxembourg).
- Troopers (Heidelberg).
- NDSS, USENIX Security — académiques.

**OSINT spécifiques** :

- OSINT Symposium.
- OSMOSIS Conference.
- Trace Labs CTF events.

#### G.6 Newsletters et veille

- **Risky.Biz** (Patrick Gray) — podcast et newsletter, référence.
- **The CyberWire** — newsletter quotidienne.
- **Krebs on Security** — Brian Krebs blog.
- **The Record** (Recorded Future) — actualité CTI.
- **Bleeping Computer** — actualité accessible.
- **CyberScoop, ArsTechnica Security**.

**Comptes Twitter/X / Mastodon à suivre** (sélection, non exhaustive) :

- @briankrebs, @lorenzofb, @vxunderground, @malwrhunterteam, @MalwareTechBlog, @cyb3rops (Florian Roth), @JohnHultquist, @riskybusiness, @CrowdStrike, @Mandiant, @Flashpoint, @ESETresearch, @Kaspersky, @ANSSI_FR, @CERT_FR, @CISAgov, @NCSC, @citizenlab, @recorded_future.

#### G.7 Livres de référence

**Sur le dark web et cybercrime** :

- *DarkMarket* — Misha Glenny (cybercrime au tournant 2010).
- *American Kingpin* — Nick Bilton (Silk Road, Ross Ulbricht).
- *Sandworm* — Andy Greenberg (APT russe — focus APT mais contexte).
- *Tracers in the Dark* — Andy Greenberg (traçage crypto).
- *The Lazarus Heist* — Geoff White (DPRK cybercrime).
- *Cult of the Dead Cow* — Joseph Menn (histoire hacktivisme).

**Sur l’investigation** :

- *Open Source Intelligence Techniques* — Michael Bazzell (référence OSINT).
- *Hiding in Plain Sight* — Eric Cole (OSINT défensif).
- *Practical Threat Intelligence* — Valentina Costa-Gazcón.
- *The Threat Intelligence Handbook* — Recorded Future (gratuit).

**Sur la méthode analytique** :

- *Psychology of Intelligence Analysis* — Richards Heuer (CIA, classique).
- *Structured Analytic Techniques for Intelligence Analysis* — Heuer & Pherson.

**Sur la crypto** :

- *Mastering Bitcoin* — Andreas Antonopoulos.
- *Tracers in the Dark* (déjà cité).

**Ouvrages français** :

- *Cyberattaque et cyberdéfense* — Daniel Ventre.
- *La cyberdéfense* — Stéphane Taillat et al.
- Publications IRSEM, INHESJ.

#### G.8 Formations

**Certifications** :

- **SANS FOR578 — Cyber Threat Intelligence** (certification GCTI) — référence.
- **SANS FOR589 — Cybercrime Intelligence**.
- **SANS SEC487 — OSINT Foundations**.
- **SEC587 — Advanced OSINT**.
- **CompTIA CySA+** (analyse).
- **EC-Council CTIA** (Certified Threat Intelligence Analyst).

**Formations académiques** :

- Master cyber, master renseignement, master géopolitique en France.
- Programs spécialisés à l’EPITA, EPITECH, INSA, Télécom Paris, etc.

**Formations courtes** :

- Bellingcat (en ligne, OSINT).
- IntelTechniques (Bazzell, OSINT).
- Webinars vendors (Recorded Future, Flare, etc.).

**Communautés d’apprentissage** :

- Trace Labs (CTF OSINT for missing persons).
- Open Source Intelligence Curious (groupe communautaire).

-----

## CLÔTURE DU COURS

### Ce que ce cours a cherché à apprendre

Ce cours **LE DARK WEB — COMPRENDRE, NAVIGUER, INVESTIGUER** s’est donné pour mission de transmettre une vision **professionnelle, calibrée, opérationnelle** du dark web. Au-delà des clichés médiatiques, le dark web est un écosystème connaissable, traçable dans ses dynamiques, et investiguable par méthodes rigoureuses dans le cadre légal et éthique.

Le cours a posé les fondations (Partie I), expliqué les infrastructures (Partie II), cartographié les écosystèmes (Partie III), articulé l’économie clandestine (Partie IV), formalisé l’investigation (Partie V), structuré l’analyse et le renseignement (Partie VI), exploré les usages contemporains et tendances (Partie VII), et synthétisé sur des cas complets (Partie VIII).

Les annexes (A à G) fournissent les outils opérationnels — glossaire, typologie, checklists OPSEC, outils, grilles de crédibilité, templates, ressources de veille. L’analyste qui les utilise quotidiennement gagne en rigueur et en réactivité.

### Les quatre idées centrales

Quatre idées traversent le cours et méritent d’être retenues.

**Première idée — le dark web est un écosystème, pas un mythe**. Connaissable, mesurable, investiguable. Pas un océan infini hors d’atteinte, mais un ensemble structuré d’espaces, d’acteurs, et de dynamiques. Quelques semaines de travail méthodique permettent de cartographier les acteurs majeurs d’un secteur. La connaissance est accessible — il faut juste la rigueur de la construire.

**Deuxième idée — l’investigation est une discipline, pas une intuition**. OPSEC stricte, méthode formalisée, vocabulaire calibré, anti-biais systématique, documentation rigoureuse. L’investigation amateur produit du bruit ; l’investigation disciplinée produit du renseignement. La différence est dans la méthode, pas dans le talent intuitif.

**Troisième idée — la coopération est multiplicateur de capacité**. Avec les autorités (DGSI, ANSSI, FdO), avec les pairs sectoriels (ISAC), avec les vendors CTI, avec la communauté internationale. L’analyste isolé voit peu ; l’analyste connecté voit beaucoup. Les opérations efficaces (Cronos, Endgame, Cookie Monster) sont coopératives, pas solitaires.

**Quatrième idée — l’éthique encadre la pratique**. Légalité scrupuleuse, minimisation, non-prolifération, respect des victimes, neutralité analytique. Ces principes ne sont pas des contraintes — ils sont la condition de la durabilité. Un analyste qui dérive perd sa crédibilité, son organisation, et parfois sa liberté. Un analyste qui maintient l’éthique construit une carrière durable et une contribution réelle.

### Pour aller plus loin

La bibliothèque dont ce cours fait partie articule plusieurs dimensions complémentaires :

- **OSINT Mastery** : techniques OSINT générales, transposables au dark web pour pivoting.
- **AU CŒUR DES APT** : acteurs étatiques qui utilisent le dark web pour opérations. Compréhension géopolitique cyber.
- **Cartographie des écosystèmes cybercriminels** : contexte structurel large.
- **OSINT Crypto** : traçage blockchain en profondeur.
- **FININT — Investigation financière** : analyse financière au-delà du crypto.
- **Cours SOC, IR, Forensics** : aspects techniques défensifs complémentaires.
- **CTI** : structuration de programme de threat intelligence.
- **GRC** : intégration dans gouvernance d’entreprise.

Au-delà de la bibliothèque, l’apprentissage du dark web est **un métier de veille permanente**. Les acteurs évoluent, les marchés changent, les outils se renouvellent. Maintenir la compétence exige lecture continue, exercice régulier, échanges avec la communauté.

### Le mot de la fin

Le dark web restera un espace utilisé pour le crime, le journalisme, le militantisme, la dissidence. Sa neutralité technique en fait un instrument moralement ambigu — protecteur des dissidents, refuge des criminels, canal de la presse libre. Cette ambiguïté n’est pas un défaut à corriger ; c’est une caractéristique structurelle de l’anonymat.

Pour l’analyste, le dark web est un **terrain de travail**. Pas un mythe à démythifier, pas une zone à fuir, pas un sujet à éviter — mais un espace à comprendre méthodiquement, à investiguer rigoureusement, à exploiter défensivement.

Au fil des années, l’analyste mûri par cette pratique développe une **intuition formée** — il reconnaît rapidement un vendeur sérieux d’un scammer, un groupe en croissance d’un groupe en décadence, un signal authentique d’un faux drapeau. Cette intuition n’est pas magique — elle est le fruit accumulé des heures, des semaines, des années passées à observer, analyser, tirer des leçons.

Ce cours a tenté d’accélérer ce mûrissement — en proposant cadre, méthodes, exemples, références. Mais le métier s’apprend in fine **sur le terrain**, avec la patience, la curiosité, l’éthique, et la rigueur que l’analyste apporte chaque jour à son travail.

Bonne route à l’analyste qui s’y engage.