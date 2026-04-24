# LE DARK WEB — COMPRENDRE, NAVIGUER, INVESTIGUER

*Architecture • Écosystèmes • OPSEC • Investigation • Renseignement*

**Cours complet — 44 chapitres, 8 parties, 7 annexes.**

---

## Avant-propos

Ce cours apprend à **comprendre et investiguer le dark web** dans une posture professionnelle. Il s'adresse aux analystes CTI, investigateurs, RSSI, chercheurs en sécurité, et professionnels de la conformité et de la lutte contre la cybercriminalité. Il est conçu pour être **auto-suffisant** — un lecteur qui part de zéro, travaille le cours dans l'ordre, et fait les exercices proposés, acquiert un niveau professionnel.

**Ce que ce cours fait** : il vous apprend à situer le dark web dans le paysage numérique, comprendre ses infrastructures techniques (Tor, I2P, cryptomonnaies), cartographier ses écosystèmes (forums, marchés, leak sites, messageries), naviguer avec une OPSEC rigoureuse, investiguer une fuite de données ou une compromission, produire du renseignement actionnable, et coopérer avec les autorités. Il couvre aussi les cadres juridiques, les pièges analytiques, et les évolutions 2024-2026.

**Ce que ce cours ne fait pas** : il n'est pas un mode d'emploi pour l'activité criminelle. Il ne fournit pas de liens actifs vers des plateformes illicites, ne donne pas de techniques de contournement du law enforcement pour un usage criminel, et ne vend pas de sensationnel. Les exemples techniques sont suffisamment précis pour comprendre, pas assez pour reproduire une infraction.

**Posture pédagogique** : factuelle, calibrée, vérifiable. Chaque affirmation forte renvoie à une source publique (rapport d'agence, publication journalistique reconnue, analyse vendor CTI sérieuse). Les ordres de grandeur sont donnés avec leurs limites. Les analyses sont honnêtes sur l'incertitude.

**Continuité avec la bibliothèque** : ce cours s'articule avec OSINT Mastery (techniques OSINT transposées au dark web), AU CŒUR DES APT (acteurs étatiques qui utilisent le dark web pour leurs opérations), Cartographie des écosystèmes cybercriminels (contexte structural), OSINT Crypto (traçage blockchain), et FININT (investigation financière). Les renvois explicites permettent d'approfondir sans dupliquer.

---

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
- Ch.16 — Services criminels et profils d'acteurs
- Ch.17 — Marché des 0-day et chaîne exploit → attaque

**PARTIE IV — ÉCONOMIE CLANDESTINE**
- Ch.18 — Pourquoi l'économie du dark web fonctionne
- Ch.19 — Réputation, escrow, vouching, arbitrage
- Ch.20 — Arnaques, exit scams et manipulation de la confiance
- Ch.21 — Modèles économiques criminels

**PARTIE V — INVESTIGATION, VEILLE ET COLLECTE**
- Ch.22 — Cadre juridique, éthique et sécurité de l'analyste
- Ch.23 — OPSEC opérationnelle de l'investigation
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
- Ch.35 — Menaces dark web par secteur d'activité

**PARTIE VII — CAS D'USAGE, TENDANCES ET PROSPECTIVE**
- Ch.36 — Ransomware, extorsion et leak sites
- Ch.37 — Dark web, influence et opérations informationnelles
- Ch.38 — Hacktivisme, zones grises et usages légitimes
- Ch.39 — IA et dark web : menaces émergentes et défensives
- Ch.40 — Forces de l'ordre, disruption et coopération internationale

**PARTIE VIII — ÉTUDES DE CAS ET SYNTHÈSE**
- Ch.41 — Cas DARKSTREAM complet — investigation d'une vente de données industrielles
- Ch.42 — Cas surveillance d'un leak site ransomware
- Ch.43 — Cas traque d'un Initial Access Broker
- Ch.44 — Maturité analyste et programme de veille durable

**ANNEXES**
- Annexe A — Glossaire
- Annexe B — Typologie des espaces dark web
- Annexe C — OPSEC analyste : checklists
- Annexe D — Outils d'investigation dark web
- Annexe E — Grille d'évaluation de crédibilité
- Annexe F — Templates de livrables
- Annexe G — Ressources et veille

---

## Fil rouge : Opération DARKSTREAM

Pour ancrer la théorie dans la pratique, ce cours suit un cas fictif inspiré d'investigations réelles. **Opération DARKSTREAM** déroule, chapitre après chapitre, l'investigation d'une exfiltration de données industrielles.

**Le contexte.** **Vectris Aerospace** est un équipementier aérospatial européen (4 500 collaborateurs, coté SBF 120), partenaire de plusieurs programmes de défense et spatiaux. En mars 2026, son SOC détecte une anomalie de trafic sortant vers une IP résidentielle. L'investigation interne remonte à un poste R&D compromis. Volume exfiltré estimé : **420 Go** — spécifications techniques, documents de conception, bases clients, notes de conception propulsion. Compromission entre 8 et 14 semaines avant détection. Vectris classifie l'incident *critique*, notifie l'ANSSI et la DGSI (OIV défense), et mandate **Athéna Group**, un cabinet CTI français.

**L'analyste.** **Lucas Ferreira**, analyste CTI senior chez Athéna Group. 8 ans d'expérience dont 3 au CERT d'une grande banque. PASSI-qualifié. Le mandat d'Athéna : **(1)** confirmer ou infirmer la circulation des données Vectris sur le dark web ; **(2)** authentifier les données offertes ; **(3)** cartographier l'écosystème impliqué (vendeur, acheteurs potentiels, courtiers) ; **(4)** produire un rapport actionnable pour Vectris et la DGSI ; **(5)** si possible, contribuer à l'identification du vendeur.

**Les signaux initiaux.** Un service de monitoring (Recorded Future) a détecté une mention de « Vectris » et « propulsion specs » sur un forum .onion russophone, **IndustrialLeaks** — forum spécialisé dans les données industrielles, ~3 000 membres, créé en 2022. Un vendeur au pseudonyme **aero_source** propose « aerospace dump 420GB, EU supplier, reconnaissance française, propulsion R&D inside ». Prix demandé : 65 000 USDT.

**La méthode.** Lucas applique une méthode rigoureuse : OPSEC stricte pour la collecte, authentification par échantillons, pivoting OSINT sur le pseudonyme, traçage crypto des transactions connues, analyse linguistique, corrélation cross-forum, calibration de l'attribution. L'opération durera **6 semaines** — Ch.41 en détaillera la synthèse complète.

Les épisodes DARKSTREAM jalonnent le cours aux moments où le concept enseigné éclaire la progression de Lucas.

---

## PARTIE I — FONDATIONS : COMPRENDRE LE DARK WEB

> **Ce que cette partie apprend.** Situer le dark web dans le paysage numérique, comprendre la différence entre surface, deep et dark web, connaître son histoire, saisir pourquoi il existe, et le considérer comme un écosystème plutôt qu'un lieu.
>
> **Ce qu'elle ne couvre pas.** Les détails techniques de Tor (Partie II), les méthodes d'investigation (Partie V), les acteurs et espaces précis (Partie III).
>
> **Ce que vous saurez faire après cette partie.** Répondre correctement à la question « qu'est-ce que le dark web ? », expliquer pourquoi il existe et à qui il sert, et présenter son écosystème à un non-spécialiste sans tomber dans les clichés médiatiques.

---

### Chapitre 1 — Internet, web visible, deep web, dark web : remettre les mots à l'endroit

#### 1.1 Internet n'est pas le web

La confusion commence ici. **Internet** est le réseau physique mondial — un ensemble de câbles sous-marins, de fibres optiques, de routeurs, de satellites, et de protocoles (principalement TCP/IP) qui relient des milliards de machines à travers la planète. Internet transporte beaucoup plus que le web : email (SMTP, IMAP), streaming vidéo (RTP, HLS), trafic VPN (IPsec, WireGuard), requêtes DNS, pair-à-pair (BitTorrent), voix sur IP, jeux en ligne, protocoles industriels, trafic de mise à jour automatique.

Le **web** (World Wide Web) est un **service** qui fonctionne sur Internet, basé sur le protocole HTTP/HTTPS et des standards de présentation (HTML, CSS, JavaScript). C'est ce qu'on consulte avec un navigateur. Le web est une couche applicative parmi d'autres — une partie importante d'Internet, certes, mais pas la totalité.

Confondre Internet et web, c'est confondre le réseau routier et les magasins qu'on peut atteindre en voiture. Cette précision est importante parce que **les darknets sont des réseaux overlay** — ils fonctionnent sur Internet, en utilisant son infrastructure physique, mais construisent au-dessus une couche logique séparée avec des propriétés différentes (anonymat, routage alternatif). Comprendre cette distinction empêche de confondre le transport (TCP/IP classique) et la couche logique d'anonymisation.

#### 1.2 Les trois couches du web

Dans le langage courant, on distingue trois couches — simplification utile même si les frontières sont poreuses.

**Surface web (clearnet)**. L'ensemble des pages indexées par les moteurs de recherche généralistes (Google, Bing, Yandex, DuckDuckGo, Baidu). En volume, le surface web représente environ 5 à 10% du contenu web total — estimation stable depuis une décennie malgré la croissance du web en valeur absolue. Tout site accessible par une URL classique (`https://example.com`) et dont les pages apparaissent dans les résultats Google fait partie du surface web.

**Deep web**. L'ensemble des contenus web **non indexés** par les moteurs de recherche généralistes. C'est la couche **la plus vaste et la plus banale** : intranets d'entreprise, bases de données académiques, contenu derrière authentification (compte bancaire, messagerie, réseaux sociaux privés, factures de services publics), archives techniques non indexées, pages dynamiques générées à la demande. Le deep web représente environ **90% du contenu web** en volume.

**La quasi-totalité du deep web est parfaitement légale et banale**. Quand on parle du deep web, on ne parle **pas** de cybercriminalité — on parle de tout ce que Google ne voit pas, pour des raisons techniques (robots.txt, authentification requise) ou de design (bases de données consultables uniquement via un formulaire). Votre boîte mail Gmail est du deep web. L'intranet de votre employeur est du deep web. La base de données d'un laboratoire universitaire est du deep web. Cette banalité est structurante — elle rappelle que l'absence d'indexation n'a rien de sinistre.

**Dark web**. Sous-ensemble du deep web accessible **uniquement via des réseaux d'anonymisation spécifiques** — principalement Tor (sites `.onion`), accessoirement I2P (eepsites), Freenet, Lokinet, ZeroNet, et quelques autres darknets plus confidentiels. Le dark web n'est pas simplement « non indexé » — il est **volontairement caché**, hébergé sur des infrastructures d'anonymisation qui masquent à la fois l'identité du serveur (son IP) et du visiteur (son IP). En volume, le dark web est une fraction **minuscule** d'Internet : quelques centaines de milliers de domaines .onion observés par le Tor Project, dont la majorité sont inactifs, abandonnés, dupliqués, ou artefacts de tests.

#### 1.3 Darknets vs dark web : une distinction technique utile

Un **darknet** est un réseau **overlay** (superposé à Internet) conçu pour l'anonymat. Tor est un darknet. I2P est un darknet. Freenet est un darknet. Chacun implémente un modèle d'anonymisation différent (onion routing, garlic routing, freenet caching) avec ses propres propriétés.

Le **dark web** est l'ensemble des **contenus accessibles via ces darknets**. La distinction est importante : on peut utiliser le darknet Tor **sans visiter de site .onion** — par exemple, en utilisant Tor uniquement comme proxy pour naviguer de manière anonyme sur le web classique. Et on ne peut visiter un site .onion **qu'en passant par le réseau Tor**.

En pratique, l'analyste manipule les deux termes. « Investiguer sur le dark web » signifie explorer les contenus hébergés sur les darknets. « Utiliser le darknet Tor » signifie exploiter l'infrastructure d'anonymisation, qu'on aille sur un .onion ou sur le clearnet via Tor.

#### 1.4 Pourquoi le terme « dark web » est souvent mal utilisé

Les médias utilisent « dark web » comme synonyme de « cybercriminalité » — raccourci compréhensible, mais analytiquement dommageable pour trois raisons.

**Il surestime le dark web comme espace criminel**. Beaucoup d'activité cybercriminelle se déroule sur le **clear web** (forums à accès restreint, marketplaces à ciel ouvert dans certaines juridictions, plateformes de communication grand public). Telegram, Discord, Signal, pastebins publics, forums publics, GitHub — tous hébergent des activités illicites sans être du dark web. Genesis Market et RaidForums, deux plateformes criminelles majeures, opéraient sur le web de surface. Inversement, beaucoup de sites .onion sont parfaitement légaux.

**Il sous-estime les usages légitimes du dark web**. Contournement de censure dans les régimes autoritaires, protection des sources journalistiques, communication sécurisée pour lanceurs d'alerte, recherche en cybersécurité, protection de la vie privée — ce sont des usages essentiels et pleinement légaux. Des institutions parfaitement légitimes (BBC, New York Times, Deutsche Welle, Facebook, ProPublica, Amnesty International) maintiennent des miroirs .onion officiels.

**Il crée une fascination sensationnaliste** qui obscurcit la réalité opérationnelle. Le dark web, en vrai, est souvent **lent** (latence de plusieurs secondes par clic), **fréquemment en panne** (les .onion disparaissent, les marchés tombent, les forums exit-scament), **rempli d'arnaques** (un post sur trois est une tentative de scam), et **plus petit qu'on ne le croit**. Ce n'est pas un bazar secret infini — c'est un espace opérationnel limité, où les vrais acteurs compétents se connaissent, où la confiance est rare et chère, et où le folklore médiatique sur les « services de tueurs à gages » est quasi entièrement fictif (les rares sites qui proposent cela sont des scams).

#### 1.5 Ordres de grandeur

Les mesures publiques du Tor Project (metrics.torproject.org) donnent les ordres de grandeur suivants pour 2025-2026. Le nombre d'adresses .onion v3 uniques observées par les relais directory oscille autour de **800 000**, avec une variation quotidienne importante. Parmi ces adresses, seule une fraction est **active** à un instant donné — les estimations convergent sur 10 à 30% de sites répondant aux requêtes. Parmi les sites actifs, environ 50 à 60% sont des **usages légitimes, miroirs, ou services abandonnés**, 20 à 30% sont des **arnaques** (fausses marketplaces, faux services), et 10 à 20% hébergent du **contenu illicite réel** (forums criminels, marchés actifs, leak sites ransomware, CSAM — qui fait l'objet d'une lutte prioritaire des forces de l'ordre).

Côté usage : le Tor Project rapporte environ **2 à 3 millions d'utilisateurs quotidiens** du réseau Tor. Le Congressional Research Service estimait en 2015 qu'environ **3,4% seulement** des utilisateurs Tor visitaient des hidden services — la **grande majorité** utilise Tor pour naviguer sur le web classique de manière anonyme (résistance à la surveillance, contournement de censure).

Ces chiffres importent : le dark web est un espace **modeste** comparé au web classique. Une investigation dark web n'est pas une exploration d'un océan infini — c'est un travail ciblé dans un écosystème connaissable, dont on peut cartographier les principaux acteurs en quelques semaines de travail méthodique.

#### 1.6 Fil rouge — DARKSTREAM : le point de départ

> **🌐 DARKSTREAM — Épisode 1 : le mandat**
>
> Lucas reçoit le brief de Vectris Aerospace le lundi matin. Réunion de cadrage en visio avec le RSSI de Vectris, la DGSI (deux interlocuteurs), et le directeur d'Athéna Group. Le RSSI présente les faits : exfiltration détectée il y a 11 jours, investigation IR en cours avec un prestataire PRIS (Mandiant), signal faible sur le dark web via Recorded Future.
>
> La DGSI précise le cadre : coopération ouverte avec Athéna, remontée bi-hebdomadaire des observations, **ne pas engager de contact direct avec le vendeur** sans concertation préalable, respect strict du périmètre légal de la collecte.
>
> Le mandat d'Athéna est clair : **confirmer ou infirmer** la circulation des données sur le dark web, **authentifier** les données si elles circulent, **cartographier** l'écosystème du vendeur et des acheteurs potentiels, **produire** un rapport actionnable pour la cellule de crise Vectris et la DGSI.
>
> Lucas commence par la première question : les alertes de monitoring dark web sont souvent des **faux positifs**. Avant de déclencher une investigation approfondie, il doit vérifier que la mention « Vectris » sur IndustrialLeaks est réelle, pertinente, et pas un artefact d'homonymie ou un scam opportuniste. Le Ch.2 contextualise le forum cible dans l'histoire des darknet markets ; le Ch.24 détaillera la méthode d'accès.

---

### Chapitre 2 — Histoire et évolution des darknets

Comprendre le dark web contemporain nécessite de connaître son histoire. Les darknets ont une trajectoire de 25 ans, marquée par des ruptures technologiques, des figures emblématiques, et des grandes opérations de police qui ont reconfiguré l'écosystème à plusieurs reprises.

#### 2.1 Les origines : anonymat et recherche militaire (1990s)

L'histoire du dark web commence dans les années 1990 au **Naval Research Laboratory** (NRL) américain, où des chercheurs (notamment **Paul Syverson**, **Michael Reed**, **David Goldschlag**) développent le concept d'**onion routing** : un protocole où les communications sont chiffrées en couches successives, chaque nœud intermédiaire ne pouvant déchiffrer que la couche qui lui est destinée, révélant le saut suivant sans connaître ni l'origine ni la destination finale. L'objectif initial est la **protection des communications de renseignement** — permettre à des agents de communiquer sans que leur trafic puisse être identifié par un adversaire observant le réseau.

Paradoxe fondamental vite identifié : un réseau d'anonymat **ne fonctionne que si beaucoup de gens l'utilisent**. Si seuls les agents de renseignement américains utilisent l'onion routing, tout le trafic observé devient attribuable (« cette communication vient d'un agent américain »). L'anonymat requiert une **foule** — et la foule requiert des usages multiples, y compris civils.

En 2002, **Roger Dingledine** et **Nick Mathewson**, rejoints par Paul Syverson, lancent le **Tor Project** comme implémentation **open source** de l'onion routing. Le projet devient indépendant en 2006 sous la forme d'une organisation à but non lucratif, avec un financement mixte — initialement beaucoup du gouvernement américain (Naval Research Laboratory, Broadcasting Board of Governors, State Department DRL), puis progressivement diversifié (donations individuelles, Mozilla, DARPA, fondations). Cette structure de financement mixte est emblématique du paradoxe : le gouvernement américain finance un outil qui protège aussi les criminels (cible d'investigation FBI), parce qu'il protège surtout les usages légitimes qui justifient stratégiquement l'existence du réseau.

#### 2.2 L'ère Silk Road (2011-2013)

**Silk Road**, créé par **Ross Ulbricht** (alias « Dread Pirate Roberts ») en février 2011, est le premier darknet market généraliste significatif. L'idée : un e-commerce clandestin inspiré d'eBay, utilisant Tor pour l'anonymat et Bitcoin pour les paiements. Ulbricht articule une vision libertarienne — vendre n'importe quel produit entre adultes consentants sans intervention étatique.

Silk Road grandit rapidement. Au moment de sa saisie par le FBI en octobre 2013, la plateforme totalise plus de **1,2 million de transactions** avec plus de **150 000 acheteurs** et **4 000 vendeurs**. Dominé par les drogues (~70% des ventes), le catalogue inclut aussi documents contrefaits, services de hacking, armes (controversé, règles internes restrictives sur ce point), mais exclut explicitement CSAM et contrats de tueurs à gages (règles internes interdisant l'« harm against others »).

Ulbricht est arrêté le 1er octobre 2013 dans une bibliothèque publique de San Francisco, ordinateur portable ouvert sur son interface administrateur. Identifié via plusieurs **erreurs OPSEC** cumulatives : un post sur StackOverflow avec son vrai email rthomeumm sous le pseudonyme « frosty », un post sur un forum Bitcoin en avril 2011 sous le pseudonyme « altoid » promouvant Silk Road (alors tout nouveau), un serveur CAPTCHA qui a leaké l'IP du serveur Silk Road lors d'une requête mal configurée (point débattu — les défenseurs d'Ulbricht ont soutenu que cette découverte était une reconstruction *a posteriori* par le FBI, possiblement couvrant une méthode de collecte classifiée).

Ulbricht est condamné en mai 2015 à **double perpétuité sans possibilité de libération conditionnelle plus 40 ans**, peine considérée comme disproportionnée par de nombreux observateurs (aucun meurtre n'ayant été commis — les accusations de tentative de contrat sur des témoins ont été utilisées pendant le sentencing sans inculpation formelle). Grâce présidentielle obtenue en janvier 2025 sous l'administration Trump.

L'héritage Silk Road est ambivalent : démonstration que l'e-commerce clandestin à grande échelle est possible (inspiration pour des dizaines de successeurs), mais aussi démonstration des limites de l'OPSEC individuelle face à une enquête FBI déterminée.

#### 2.3 La professionnalisation (2014-2019)

Après Silk Road, les successeurs se professionnalisent. **Silk Road 2.0** est lancé en novembre 2013, saisi un an plus tard (novembre 2014, operation Onymous — opération coordonnée qui saisit aussi plusieurs dizaines d'autres marchés). **Evolution Market** devient leader en 2014-2015 avant un exit scam retentissant (mars 2015, ~12 millions de dollars envolés). **Agora**, **Abraxas**, **Dream Market** se succèdent.

**AlphaBay**, lancé en décembre 2014 par **Alexandre Cazes** (canadien basé en Thaïlande, alias « alpha02 »), devient le **plus grand darknet market de l'histoire**. Au moment de sa saisie, le Département de la Justice américain documente **plus de 250 000 listings de drogues et produits chimiques**, auxquels s'ajoutent **plus de 100 000 listings** pour faux documents, accès frauduleux, malwares, armes et services divers. AlphaBay mature significativement le modèle : multiple cryptomonnaies acceptées (Bitcoin, Monero, Ethereum), 2FA obligatoire, PGP, système d'escrow robuste, ratings élaborés.

**Operation Bayonet** (juillet 2017) est une double frappe coordonnée entre le FBI américain et la police néerlandaise. AlphaBay est saisi suite à une erreur OPSEC de Cazes (inclusion de son email personnel `pimp_alex_91@hotmail.com` dans l'en-tête d'un email de bienvenue automatique généré en 2014). Cazes est arrêté en Thaïlande le 5 juillet 2017. Il est retrouvé mort en cellule le 12 juillet 2017 — officiellement suicide, version contestée par sa famille.

Le coup génial de l'opération : la police néerlandaise avait pris le contrôle de **Hansa Market** quelques semaines avant la saisie d'AlphaBay. Quand AlphaBay tombe, les utilisateurs et vendeurs migrent en masse vers Hansa — qui est maintenant opéré par la police. Pendant **30 jours**, les autorités néerlandaises collectent les données (vraies adresses de livraison, IPs, communications, patterns de transactions) avant de saisir Hansa à son tour. Cette opération devient la référence moderne de l'**infiltration active** par les forces de l'ordre.

#### 2.4 Hydra et la domination russophone (2015-2022)

**Hydra Market** (ru-center : hydraruzxpnew4af.onion et successeurs) est un cas à part. Lancé en 2015 et exclusivement opéré en russe, Hydra devient le **leader absolu** de l'écosystème russophone. Le DOJ américain et les autorités allemandes indiquent, lors de la saisie d'avril 2022, qu'Hydra a reçu environ **5,2 milliards de dollars en cryptomonnaies depuis 2015** et représentait environ **80% des transactions crypto liées aux darknet markets en 2021**.

Deux particularités structurantes. **Exclusivement russophone** : barrière d'entrée linguistique qui l'a partiellement protégé des actions law enforcement occidentales et de l'infiltration par analystes étrangers. **Système de dead drops physiques** unique : contrairement aux marchés occidentaux qui utilisent la poste (avec les risques que cela implique), Hydra fonctionnait avec des *kladmen* — courriers qui cachaient physiquement les produits dans des endroits spécifiques (sous une pierre dans un parc, dans un interstice de mur), dont les coordonnées GPS étaient ensuite communiquées à l'acheteur. Modèle qui supprime l'interception postale mais crée un écosystème de travailleurs à bas salaire (les kladmen) avec une rotation élevée.

La saisie d'Hydra en avril 2022 par les autorités allemandes (Zentrale Kriminalinspektion, Bundeskriminalamt, avec soutien du FBI) a créé une **fragmentation** massive de l'écosystème russophone : plusieurs marchés successeurs (OMG!OMG!, Mega, BlackSprut, Kraken) se sont partagé le marché sans qu'un leader clair ne s'impose comme Hydra l'était. La fragmentation complique le monitoring (plus de plateformes à suivre) et augmente la méfiance (exit scams plus fréquents sur les nouveaux marchés).

#### 2.5 L'ère post-Hydra et les tendances 2024-2026

L'écosystème 2024-2026 présente plusieurs caractéristiques structurantes.

**Fragmentation des marchés généralistes**. Les marchés « tout-en-un » type AlphaBay cèdent la place à des marchés **spécialisés** : marchés de logs (Russian Market), marchés de fraude (BriansClub, WWH Club, anciens 2easy.gg), marchés de ransomware-as-a-service, marchés de services (CaaS). Cette spécialisation reflète la professionnalisation de la cybercriminalité organisée.

**Montée de Telegram comme concurrent**. Telegram est devenu, dans la période 2020-2024, un canal majeur de communication cybercriminelle. Plus accessible que Tor (pas besoin d'outils spéciaux), plus réactif (chats en temps réel), avec des canaux publics et privés. Les canaux Telegram cybercriminels comptent des centaines de milliers de membres cumulés. **Arrestation de Pavel Durov en France le 24 août 2024** — inculpation incluant complicité dans la diffusion de contenus illicites. Impact : Telegram a considérablement durci sa modération (suppression massive de canaux criminels, coopération accrue avec les autorités), conduisant à une migration **partielle** des acteurs vers d'autres plateformes (Session, Matrix sur Tor, retour partiel vers les forums .onion).

**Glissement du vecteur d'accès initial**. L'évolution majeure 2025-2026 documentée par SOCRadar, Flare, Recorded Future : les attaquants **achètent** des credentials valides sur le dark web via des **stealer logs** à prix dérisoire (dès 15 USD) plutôt que de développer des exploits sophistiqués. Le dark web est devenu le **supermarché de l'accès initial**. L'attaquant moderne n'exploite plus la sophistication technique mais la **commoditisation** : pour 15 USD il achète un log d'infostealer, pour 500-50 000 USD il achète un accès VPN corporate préqualifié auprès d'un IAB, et il n'a plus qu'à monétiser.

**Intégration massive de l'IA**. Deepfakes, génération de phishing, chatbots criminels, analyse assistée — l'IA a basculé d'outil émergent à commodité dans la cybercriminalité. Parallèlement, les défenseurs adoptent l'IA pour le monitoring, l'analyse linguistique, et la détection d'anomalies (Ch.39).

**Pression croissante des forces de l'ordre**. Opérations de démantèlement plus fréquentes et plus sophistiquées (LockBit/Cronos février 2024, Kidflix mars 2025, BreachForums multiple, Qakbot, Hive, ALPHV/BlackCat, Genesis Market). Les grands opérateurs RaaS perdent en moyenne **18 mois** d'existence opérationnelle avant démantèlement. La pression a des effets : le niveau de paranoia opérationnelle augmente, les infrastructures se fragmentent pour résilience, et certains opérateurs se « retirent » après un gain significatif.

#### 2.6 Chronologie synthétique des grandes dates

| Période | Événement | Impact structurant |
|---------|-----------|--------------------|
| 1995-2002 | Développement onion routing (NRL) | Foundation technique |
| 2002 | Lancement Tor | Accessibilité publique |
| 2009 | Lancement Bitcoin | Couche financière du dark web |
| 2011 | Lancement Silk Road | Premier grand market généraliste |
| 2013 | Saisie Silk Road, arrestation Ulbricht | Premier shock LE majeur |
| 2014 | Lancement AlphaBay, saisie Silk Road 2.0 | Professionnalisation |
| 2015 | Lancement Hydra (ru) | Émergence bloc russophone |
| 2017 | Operation Bayonet (AlphaBay + Hansa) | Référence infiltration LE |
| 2018-2019 | Dream Market, Wall Street Market | Succession post-AlphaBay |
| 2020-2022 | Ascension Telegram / CaaS | Convergence dark web / clearnet |
| 2022 (avril) | Saisie Hydra | Fragmentation russophone |
| 2023 | Operation Cookie Monster (Genesis) | Saisie marché de logs |
| 2024 (février) | Operation Cronos (LockBit) | Disruption grand RaaS |
| 2024 (août) | Arrestation Pavel Durov | Durcissement Telegram |
| 2025-2026 | Commoditisation accès, montée IA | Paradigme contemporain |

#### 2.7 Fil rouge — DARKSTREAM : le forum ciblé

> **🌐 DARKSTREAM — Épisode 2 : IndustrialLeaks dans son contexte**
>
> Avant d'y accéder, Lucas documente le forum signalé. **IndustrialLeaks** est un forum .onion russophone créé fin 2022, dans le contexte post-Hydra. Il s'est positionné sur une niche : les **données industrielles** (pas le ransomware classique, pas les credentials bancaires) — documents techniques, spécifications, bases clients, données de supply chain industrielle.
>
> Environ 3 000 membres enregistrés selon les rares rapports publics disponibles. Accès sur **vouching** (parrainage par un membre établi) ou paiement d'un droit d'entrée (0,005 BTC, ~250 USD au cours actuel). Le forum a changé d'adresse .onion **trois fois** en 18 mois — comportement classique face à la pression (soit d'attaques DDoS concurrentes, soit de tentatives d'infiltration). Un miroir I2P est maintenu, indice de maturité technique des opérateurs. La langue principale est le russe ; l'anglais est toléré mais réservé aux ventes grand format.
>
> L'activité principale documentée : ventes de données d'entreprises industrielles (énergie, défense, aérospatial, chimie), occasionnellement services associés (accès persistant, exfiltration ciblée sur commande). Quelques posts de « dumps » publics pour établir la réputation de vendeurs cherchant à monter en crédibilité.
>
> Pour Lucas, ce contexte suggère qu'**IndustrialLeaks est un forum sérieux plus qu'un bazar à scams** — ce qui augmente la probabilité que la mention Vectris soit réelle. Mais il reste prudent : même dans un forum sérieux, l'opportunisme scam est fréquent. La vérification d'authenticité (Ch.14, Ch.25) reste incontournable.

---

### Chapitre 3 — Pourquoi le dark web existe

Le dark web n'est pas une accumulation fortuite d'infrastructures. Il existe parce qu'il répond à des besoins réels, et il persiste parce que ces besoins persistent. Ce chapitre articule les raisons légitimes, les usages détournés, et la tension fondamentale qui structure le débat public.

#### 3.1 L'anonymat comme besoin fondamental

**Résistance à la censure**. Dans les régimes autoritaires (République populaire de Chine, Iran, Russie depuis 2022, Biélorussie, Myanmar, Érythrée, Corée du Nord dans une certaine mesure, Turkménistan), l'accès à des contenus jugés subversifs par l'État est filtré, surveillé, parfois criminalisé. Tor permet, dans beaucoup de ces contextes, d'accéder à Wikipedia, à des médias indépendants (Voice of America, BBC Persian, Deutsche Welle), à des réseaux sociaux bloqués (Twitter/X bloqué en Chine, Facebook en Iran). **Reporters Sans Frontières** opère des miroirs .onion de médias dissidents. Le **Tor Project** développe des techniques dédiées (bridges, pluggable transports comme obfs4, meek, snowflake) pour contourner le Deep Packet Inspection des censeurs.

La mesure n'est pas théorique. Pendant les manifestations en Iran (2022-2023, mouvement Woman Life Freedom), l'usage de Tor a bondi. Après l'invasion russe de l'Ukraine (février 2022) et le durcissement du régime russe vis-à-vis des médias (blocage de Facebook, Twitter, de nombreux médias indépendants), les connexions russes à Tor ont augmenté. Ces périodes de pic confirment que Tor est un **outil opérationnel de résistance informationnelle**.

**Protection des sources journalistiques**. La protection des sources est un pilier de la liberté de la presse, reconnu dans les législations démocratiques (article 10 CEDH, jurisprudence Goodwin c. Royaume-Uni 1996, First Amendment américain, loi française sur la liberté de la presse). Le dark web offre des canaux techniques pour que les sources communiquent avec les journalistes sans risque d'identification.

**SecureDrop** (développée initialement par Aaron Swartz et James Dolan, maintenue par la Freedom of the Press Foundation) est la plateforme de référence. Déployée par : le New York Times, le Guardian, le Washington Post, Le Monde, Der Spiegel, ProPublica, The Intercept, la BBC, et des dizaines d'autres médias. L'affaire **Panama Papers** (2016) et l'affaire **LuxLeaks** (2014) n'auraient pas été techniquement possibles sans des canaux de transmission anonymes.

**AfriLeaks** pour les lanceurs d'alerte africains, **GlobaLeaks** comme plateforme open source généraliste, **Hermes Center** pour le soutien technique à ces déploiements — un écosystème s'est structuré autour de cet usage.

**Vie privée comme droit fondamental**. Article 8 de la CEDH (respect de la vie privée et familiale), article 12 de la Déclaration universelle des droits de l'homme, article 7 de la Charte des droits fondamentaux de l'UE. L'anonymat en ligne est un **instrument** de ces droits. Dans un contexte de surveillance massive (activités commerciales de profilage, surveillance étatique légale ou illégale, collecte par des États hostiles), l'anonymat permet des choix informationnels libres.

**Communications sensibles légitimes**. Défenseurs des droits humains en zones hostiles, avocats consultant des cas sensibles, médecins communiquant sur des patients en zones de conflit, chercheurs en sécurité testant des infrastructures, employés lanceurs d'alerte envers leur propre employeur. L'anonymat technique protège des usages légitimes qui, sans anonymat, seraient impossibles ou dangereux.

#### 3.2 L'anonymat comme facilitateur criminel

Le dark web offre aux acteurs malveillants un espace où :
- **L'identification est difficile** : l'IP source est masquée, les pseudonymes sont jetables, les artefacts de compilation et les conventions linguistiques peuvent être contrôlés.
- **Les transactions sont pseudonymes ou anonymes** : Bitcoin pseudonyme avec traçabilité croissante, Monero anonyme par construction.
- **L'infrastructure est résistante aux saisies** : un site .onion ne dépend d'aucun registre centralisé ; la saisie nécessite soit la compromission du serveur physique, soit l'identification de l'opérateur.

Les usages criminels documentés couvrent un spectre large : marchés de drogues (de loin le volume dominant historiquement, en baisse relative depuis 2020), données volées et credentials, armes (volume marginal, beaucoup de scams), documents contrefaits, services de hacking, CSAM (priorité 1 des forces de l'ordre), blanchiment, forums de fraude, infrastructures de communication pour cybercriminels sophistiqués.

La diversité de ces usages, du trafiquant solo au groupe ransomware étatique, montre que le dark web n'est **ni un repaire de super-criminels ni un simple outil de liberté** — l'anonymat est moralement neutre, c'est **l'usage** qui est qualifiable.

#### 3.3 La tension fondamentale et ses régulations

La tension n'a pas de résolution simple : **l'anonymat technique qui protège les dissidents protège aussi les criminels**. Supprimer Tor (si c'était techniquement faisable, ce qui est contesté) ne supprimerait pas le besoin d'anonymat des dissidents — il les priverait d'un outil essentiel. Surveiller massivement Tor (comme certaines juridictions autoritaires tentent de le faire) compromet structurellement les usages légitimes.

Les régulations contemporaines tentent de naviguer cette tension par plusieurs approches.

**Lutte ciblée contre les usages criminels spécifiques**. Approche occidentale dominante : ne pas interdire Tor, mais poursuivre les opérateurs de plateformes criminelles (Ulbricht, Cazes, Khoroshev/LockBitSupp), les utilisateurs de CSAM identifiables, les infrastructures de paiement du crime. Les investigations combinent OSINT, analyse blockchain, erreurs OPSEC, infiltration, coopération internationale.

**Régulation des cryptomonnaies**. Parce que l'anonymat financier est le **maillon faible** de la cybercriminalité (à un moment, l'argent doit être converti en fiat utilisable), les régulateurs durcissent les exchanges (KYC renforcé, déclaration de transactions, sanctions ciblées type Tornado Cash en août 2022). Voir Ch.8 et Ch.31.

**Coopération internationale**. Convention de Budapest sur la cybercriminalité (2001), élargie par un deuxième protocole additionnel en 2022 sur la coopération renforcée et la divulgation électronique de preuves. Europol, Interpol, J-CAT, FBI Legal Attaché en poste dans les ambassades. Un écosystème d'échanges de renseignement et de coordination d'opérations.

**Approches contestées dans les démocraties**. Certaines juridictions explorent des pistes qui posent des questions de libertés publiques : lois sur la « responsabilité des plateformes » (Royaume-Uni Online Safety Act, UE Digital Services Act), tentatives de contrer le chiffrement de bout en bout pour permettre l'accès des autorités (projets récurrents type EARN IT aux US, Chat Control en UE — encore débattu), extension des pouvoirs d'interception (projets de mise à jour des législations nationales). Ces approches divisent, parce qu'elles pèsent sur l'équilibre vie privée / sécurité publique.

**Approches criminelles dans les régimes autoritaires**. Blocage pur et simple de Tor (Chine, Iran périodiquement), criminalisation de son usage (Russie depuis 2021 sous certaines formes), surveillance agressive des utilisateurs identifiés. Ces approches s'alignent sur des objectifs de contrôle politique plus que de lutte contre la criminalité.

L'équilibre exact entre anonymat et responsabilité reste un débat politique et sociétal vivant, sans résolution consensuelle à l'horizon.

---

### Chapitre 4 — Le dark web comme écosystème

Le dark web n'est pas une seule chose — c'est un **écosystème** composé d'acteurs aux rôles distincts, d'espaces aux fonctions différentes, et de mécanismes de circulation qui le font fonctionner. Ce chapitre pose le cadre que les parties suivantes approfondiront.

#### 4.1 Les types d'espaces

Six grandes catégories d'espaces dark web, détaillées en Partie III.

**Forums** (Ch.10) : espaces de discussion structurés autour de thèmes (fraude, hacking, drogues, données, géographie). Modérés, avec hiérarchie de membres (newbie, member, trusted, VIP, moderator, admin), système de réputation. XSS Forum, Exploit.in, BreachForums successive, IndustrialLeaks (fictif, inspiré de cas réels).

**Marchés (marketplaces)** (Ch.11) : plateformes d'e-commerce clandestin, avec listings, panier, escrow, ratings. AlphaBay historique, Abacus Market, BlackSprut (ru), Mega (ru), TorZon.

**Leak sites** (Ch.12) : vitrines publiques des groupes ransomware, où ils revendiquent les victimes et menacent de publier les données volées. LockBit, ALPHV/BlackCat, Black Basta, RansomHub, Play, Qilin — chacun avec son esthétique propre.

**Messageries et canaux** (Ch.13) : Telegram, Matrix via Tor, Session, Jabber/XMPP, Tox. Les messageries servent à la fois comme canaux opérationnels (négociations, coordination) et comme canaux de diffusion (canaux publics avec abonnés).

**Marchés spécialisés** : marchés de logs (Russian Market), marchés de fraude (Genesis historique, successeurs), marchés 0-day (Ch.17).

**Services** : infrastructure hosting bulletproof, blanchiment-as-a-service, cryptage-as-a-service, bot-as-a-service, phishing kits.

#### 4.2 Les types d'acteurs

**Opérateurs de plateformes** : développeurs et administrateurs des forums, marchés, leak sites. Économiquement, ils prélèvent des commissions (1-10% sur les transactions), des frais d'inscription, des frais de vendeur. Politiquement, ils arbitrent les conflits. Opérationnellement, ils gèrent la résilience technique.

**Vendeurs** : acteurs qui monétisent des produits ou services sur les marchés. Spécialisations multiples : drug vendors, carders, credential brokers, fullz vendors, weapon vendors, 0-day brokers, service providers.

**Acheteurs** : clients finaux ou intermédiaires. Profils variés — particuliers cherchant drogues ou documents, cybercriminels achetant des outils, fraudeurs achetant des données, opérateurs ransomware achetant des accès IAB.

**Initial Access Brokers (IAB)** : acteurs spécialisés dans la compromission initiale d'organisations et la vente des accès à d'autres acteurs (typiquement des opérateurs ransomware). Chaîne de valeur centrale de la cybercriminalité contemporaine.

**Affiliés RaaS** : opérateurs qui déploient un ransomware-as-a-service moyennant partage des gains avec le propriétaire du malware.

**Blanchisseurs** : spécialistes de la conversion crypto → fiat utilisable, typiquement 10-30% de commission sur le montant blanchi.

**Services transversaux** : hébergeurs bulletproof, développeurs de malware, opérateurs botnets, crypters, spammers.

**Analystes CTI, forces de l'ordre, journalistes** : observateurs, dans des postures légales variées (voir Partie V sur le cadre légal et Ch.30 sur l'infiltration policière).

#### 4.3 Les flux qui font fonctionner l'écosystème

**Flux d'information** : montée en crédibilité des vendeurs, annonces de produits/services, négociations, litiges. Support : forums, canaux dédiés aux marchés, messageries privées.

**Flux financier** : paiements via cryptomonnaies (Bitcoin historique mais en repli, Monero en hausse, quelques stablecoins type USDT), escrow sur les marchés, blanchiment aval. Ch.8 détaille les mécanismes.

**Flux de confiance** : réputation construite par l'historique transactionnel, vouching par membres établis, arbitrage en cas de litige. Sans ces mécanismes, l'économie ne fonctionnerait pas. Ch.19 détaille.

**Flux de données** : données volées circulent des breachers initiaux vers les courtiers, puis vers les acheteurs finaux. Chaîne typique : breach → vente exclusive à prix élevé → revente en baisse → diffusion gratuite tardive (Ch.14).

**Flux d'accès** : les IAB compromettent → vendent l'accès → l'acheteur déploie ransomware ou autre monétisation. Chaîne souvent constatée dans les investigations post-incident.

#### 4.4 La géographie linguistique et culturelle

L'écosystème dark web est structuré par **plusieurs blocs linguistiques** largement cloisonnés.

**Bloc russophone** : le plus large historiquement. Forums majeurs (XSS, Exploit.in, RAMP historique), marchés (Hydra historique, successeurs), opérateurs ransomware (LockBit, Conti, ALPHV). La ligne russophone inclut ex-URSS (Russie, Bélarus, Ukraine pré-2022, Kazakhstan, etc.). Règle opérationnelle tacite des groupes russophones : **ne pas cibler la CEI** (Communauté des États indépendants) — règle respectée en grande partie, traduite dans le code de certains ransomware (vérification de la langue du clavier, exclusion des locales russophones).

**Bloc anglophone** : historiquement dominant pour les marchés généralistes (Silk Road, AlphaBay, Dream), devenu plus discret post-grandes saisies. Forums anglophones majeurs (BreachForums multiple, RaidForums historique).

**Bloc chinois** : opère largement sur des plateformes spécifiques, avec forums et canaux accessibles aux sinophones. Moins documenté dans les analyses vendor occidentales, nécessite une expertise linguistique spécialisée.

**Bloc persophone et arabophone** : croissance notable depuis 2020, avec des forums et canaux dédiés, activités orientées fraude, credentials, et parfois opérations liées à des tensions géopolitiques régionales.

**Autres** : francophone (présence modeste, parfois sur forums anglophones), hispanophone (Amérique latine, forums cartels), portugaise (Brésil), turc, coréen.

Pour l'analyste, la **barrière linguistique** est structurante : un analyste non russophone a une visibilité très partielle sur l'écosystème russophone. Les équipes CTI matures recrutent des locuteurs natifs ou utilisent des partenariats (SentinelOne, Recorded Future, Kaspersky, Sekoia, Group-IB ont tous des équipes multilingues).

#### 4.5 Les évolutions structurantes 2020-2026

Plusieurs tendances transforment l'écosystème.

**Professionnalisation continue**. Les opérateurs sont devenus plus matures techniquement, OPSEC plus rigoureuse, modèles économiques plus articulés (RaaS, CaaS). L'amateurisme des années 2010 est en recul.

**Commoditisation de l'accès**. Les stealer logs et les IAB ont abaissé les barrières d'entrée. Un acteur peu sophistiqué peut désormais, avec quelques centaines de dollars, acquérir un accès à une entreprise et lancer une attaque.

**Convergence clearnet/darkweb**. Beaucoup d'activité qui aurait été sur Tor en 2015 est maintenant sur Telegram, Discord, certains forums clearnet à accès restreint. L'analyste doit donc couvrir un spectre plus large que le seul .onion.

**Pression réglementaire et policière**. Multiplication des opérations de démantèlement, sanctions ciblées (Tornado Cash, adresses OFAC), coopération internationale renforcée, durcissement du KYC sur les exchanges crypto. Impact : augmentation des coûts opérationnels, accélération de la rotation des plateformes, montée de la paranoïa.

**Intégration de l'IA**. Deepfakes, chatbots criminels, automatisation du phishing, assistance au développement de malware. L'IA abaisse encore les barrières pour les acteurs peu qualifiés, même si elle ne transforme pas un script kiddie en APT.

**Retour de balancier vers les .onion**. Après le durcissement de Telegram post-Durov, certains acteurs retournent vers les forums .onion historiques — meilleure résilience juridique, même si accès plus friction.

#### 4.6 Ce que l'analyste doit retenir

Trois principes opérationnels pour aborder le dark web.

**C'est un écosystème, pas un lieu**. On n'« entre pas dans le dark web » comme on entre dans un bâtiment — on observe un ensemble d'espaces distincts, chacun avec ses règles, sa langue, ses acteurs. L'investigation se déplace entre forums, marchés, messageries, leak sites selon les pistes.

**Les acteurs jouent des rôles spécialisés**. L'IAB ne fait pas de ransomware ; l'opérateur RaaS n'exfiltre pas ; le blanchisseur ne vole pas. Cette spécialisation structure les chaînes d'attaque et fournit les angles d'investigation.

**L'écosystème évolue vite**. Un forum qui dominait il y a 18 mois a pu exit-scammer, être saisi, ou migrer. Les statistiques de prix bougent, les pseudonymes changent, les plateformes tombent. La connaissance acquise doit être rafraîchie en continu — ce qui fait de la veille (Ch.27) un pilier de la pratique.

---

## PARTIE II — INFRASTRUCTURES TECHNIQUES ET ANONYMAT

> **Ce que cette partie apprend.** Comprendre les infrastructures techniques qui rendent le dark web possible — architecture Tor, onion services v3, réseaux alternatifs (I2P, Freenet), cryptomonnaies et leur traçabilité, hébergement bulletproof. Comprendre aussi leurs limites — Tor n'est pas magique, Monero n'est pas absolu, un bulletproof host peut être saisi.
>
> **Ce qu'elle ne couvre pas.** Les méthodes d'investigation exploitant ces infrastructures (Partie V et VI), les méthodes concrètes de dé-anonymisation (Ch.29), les techniques de configuration offensive (hors périmètre).
>
> **Ce que vous saurez faire après cette partie.** Expliquer techniquement le fonctionnement de Tor à un collègue, évaluer la résistance d'un service .onion à une saisie, distinguer les propriétés d'anonymat de Bitcoin et Monero, identifier les points de faiblesse typiques d'une infrastructure criminelle.

---

### Chapitre 5 — Architecture de Tor

Tor (The Onion Router) est le darknet dominant. Comprendre son architecture permet de comprendre ses propriétés, ses limites, et les angles d'attaque — défensifs ou offensifs — qui s'appliquent.

#### 5.1 Principe de l'onion routing

L'idée centrale de l'onion routing est **séparer la connaissance de l'origine et de la destination** entre plusieurs nœuds intermédiaires, de telle sorte qu'**aucun nœud seul** ne connaisse les deux extrémités de la communication.

Mécanisme : le client Tor construit un **circuit** à trois nœuds (guard, middle, exit) en négociant des clés de chiffrement successives. Chaque paquet envoyé est **chiffré trois fois**, dans des couches successives. Chaque nœud intermédiaire déchiffre **une couche** pour révéler le saut suivant, sans pouvoir déchiffrer les autres couches.

Concrètement, pour une requête du client Alice vers le site `example.com` :

1. Le client Tor d'Alice choisit trois nœuds : un **guard** (premier relais, connu du client), un **middle** (relais intermédiaire), un **exit** (relais de sortie qui parle au site final).
2. Alice chiffre sa requête en trois couches, dans l'ordre inverse du chemin : couche exit, couche middle, couche guard — chaque couche chiffrée avec la clé du nœud correspondant.
3. Le paquet transite : Alice → guard. Le guard déchiffre sa couche, voit l'adresse du middle mais pas la destination finale.
4. Guard → middle. Le middle déchiffre sa couche, voit l'adresse de l'exit mais ne connaît ni Alice (qui a parlé au guard) ni la destination finale.
5. Middle → exit. L'exit déchiffre sa couche, voit la requête en clair (si HTTP) et l'envoie vers example.com. L'exit connaît la destination mais ne connaît pas Alice.

Réponse : même mécanisme en sens inverse. Chaque nœud ne chiffre qu'une couche avec sa clé sur le retour.

**Propriété clé** : dans ce modèle, aucun nœud seul ne connaît à la fois l'identité de l'origine (Alice) et la destination (example.com). Un adversaire doit contrôler **à la fois le guard et l'exit** pour corréler. C'est toute la sécurité du système — et son talon d'Achille.

#### 5.2 Les types de relais

Le réseau Tor comprend environ **7 000 à 8 000 relais** actifs en 2025-2026, répartis géographiquement (concentration en Europe, US, Canada, quelques en Asie). Ils se classent en catégories.

**Guard relays** : premier nœud d'un circuit, choisi parmi un ensemble de relais stables et bien connectés. Un client Tor utilise le **même petit ensemble de guards** pendant plusieurs mois (rotation lente), pour limiter l'exposition à un attaquant qui compromettrait des guards aléatoirement (l'attaquant a plus de chances de tomber sur un mauvais guard avec rotation rapide).

**Middle relays** : relais intermédiaires, les plus nombreux. Rôle de relais pur, sans visibilité ni sur l'origine ni sur la destination.

**Exit relays** : relais qui parlent au monde extérieur. Les moins nombreux (risque juridique élevé — un abus commis via Tor sort par l'exit, dont l'opérateur peut recevoir des plaintes ou des requêtes légales). Environ 1 000 exits actifs. Certains exits ont des politiques restrictives (bloquent certains ports, certains protocoles).

**Directory authorities** : serveurs qui maintiennent la liste des relais (le « consensus »). Il y a **9 directory authorities** actuellement, opérées par des entités de confiance (universités, Tor Project, individus de long terme). Tous les clients Tor téléchargent périodiquement ce consensus pour choisir leurs circuits.

**Bridges** : relais **non publics** (absents du consensus public), accessibles uniquement à ceux qui en obtiennent l'adresse par des canaux spécifiques (site web du Tor Project, email, Telegram, Messenger). Usage : contourner la censure là où les relais publics sont bloqués.

**Pluggable transports** : techniques d'obfuscation du trafic Tor pour contourner le Deep Packet Inspection. **obfs4** (fait ressembler Tor à du trafic aléatoire), **meek** (fait ressembler Tor à du trafic vers un grand service cloud type Azure, AWS, Fastly — « domain fronting »), **snowflake** (utilise des volontaires côté client comme relais WebRTC).

#### 5.3 Construction d'un circuit — détail

Plus précisément, voici comment un client Tor construit un circuit (simplifié).

1. **Téléchargement du consensus** : le client télécharge la liste des relais et leurs clés publiques auprès d'un directory authority ou d'un cache.

2. **Sélection des relais** : le client choisit un guard (parmi ses guards persistants), un middle, un exit — selon des critères de stabilité, bande passante, géographie (pour éviter par exemple de choisir trois relais dans le même pays), et politiques d'exit.

3. **Handshake avec le guard** : le client établit une connexion TLS avec le guard et négocie une clé symétrique via un protocole d'échange de clés (actuellement NTor — Noise-based Tor handshake).

4. **Extension vers le middle** : le client envoie au guard une commande « extend » chiffrée, qui demande au guard de contacter le middle et de négocier une clé symétrique avec lui. Le client obtient ainsi une clé partagée avec le middle via le guard comme relais.

5. **Extension vers l'exit** : pareil, le client étend le circuit vers l'exit.

Le client dispose maintenant de trois clés symétriques, une avec chaque relais. Toute donnée envoyée sera chiffrée en trois couches.

6. **Envoi de données** : le client construit son paquet en trois couches chiffrées et l'envoie au guard. Le guard déchiffre sa couche, fait suivre au middle, etc.

La durée de vie d'un circuit est typiquement de **10 minutes**, après quoi un nouveau circuit est construit pour les nouvelles connexions. Les streams existants peuvent continuer sur l'ancien circuit.

#### 5.4 Attaques et limites

Tor fournit un anonymat **fort mais pas absolu**. Plusieurs classes d'attaques existent.

**Attaque par corrélation de trafic**. Si un adversaire contrôle (ou observe) à la fois le guard et l'exit d'un circuit, il peut corréler les flux entrants et sortants par leur timing et leur volume, et identifier l'origine et la destination. Cette attaque nécessite une observation globale ou la compromission massive de relais. Les grands services de renseignement (NSA, GCHQ) sont crédités de cette capacité dans certaines conditions.

**Attaques sur les bridges**. Les censeurs ciblent les bridges en enregistrant leur trafic ou en les bloquant par DPI. La course entre obfuscations (nouveaux pluggable transports) et détection est continue.

**Attaques sur le navigateur**. Les utilisateurs de Tor Browser sont parfois attaqués via des exploits navigateur (historiques : **NIT du FBI en 2015 contre Playpen**, plusieurs opérations documentées contre Freedom Hosting). Ces attaques exploitent des vulnérabilités du navigateur sous-jacent (Firefox modifié) pour faire exécuter du code chez l'utilisateur et révéler son IP réelle hors de Tor. Voir Ch.30.

**Attaques par fingerprinting**. Même si l'IP est masquée, l'ensemble du comportement d'un utilisateur (timing, patterns de clics, taille de fenêtre, fingerprint navigateur) peut contribuer à son identification. Tor Browser est conçu pour uniformiser autant que possible les fingerprints (même résolution, même user-agent, anti-canvas), mais la recherche académique montre que l'anonymat parfait est illusoire.

**Attaques sur le DNS**. Si une application autre que Tor Browser fait des requêtes DNS non-tunnelées, elle leak l'IP réelle. C'est pourquoi Tor Browser isole le DNS dans le circuit.

**Erreurs utilisateur**. Loggin avec un compte identifié, réutilisation de pseudonymes, corrélation temporelle par les actions — beaucoup de dé-anonymisations historiques viennent d'erreurs d'OPSEC plus que d'attaques cryptographiques (Ulbricht, Cazes, beaucoup d'administrateurs de Hansa ou Silk Road 2.0).

#### 5.5 Tor Browser et les bonnes pratiques

**Tor Browser** (basé sur Firefox ESR avec modifications majeures) est le client de référence. Il intègre Tor, configure les proxies correctement, active NoScript, définit des paramètres de confidentialité par défaut (pas de cookies tiers persistants, pas de WebRTC, canvas bloqué). Disponible pour Windows, macOS, Linux, Android (Android via Orbot + Firefox-based browser). iOS n'a pas de Tor Browser officiel (limitations App Store) mais Onion Browser est une alternative acceptable.

**Mode Safer / Safest** : Tor Browser offre trois niveaux de sécurité (Standard, Safer, Safest). Safest désactive JavaScript sur tous les sites — recommandé pour l'investigation dark web (beaucoup de sites illicites exploitent des vulnérabilités JS pour identifier les visiteurs, voir Ch.30).

**Tails** : distribution Linux live qui force tout le trafic à passer par Tor, ne laisse aucune trace sur la machine. Usage recommandé pour les analystes travaillant sur des cas sensibles, et pour les journalistes/sources (Edward Snowden l'utilisait). Pas d'amnésie parfaite — une compromission exploitée en live peut leaker des données.

**Whonix** : architecture en deux VM (Whonix-Gateway qui fait le routage Tor, Whonix-Workstation où tournent les applications). L'isolation renforce la sécurité : si la workstation est compromise, elle ne peut pas obtenir l'IP réelle (qui n'est connue que de la gateway).

#### 5.6 Fil rouge — DARKSTREAM : préparation technique

> **🌐 DARKSTREAM — Épisode 3 : setup**
>
> Lucas prépare son environnement d'investigation. Protocole Athéna : **machine dédiée**, non reliée au réseau d'entreprise, allumée uniquement pour les sessions d'investigation. OS : Whonix, Gateway + Workstation dans VirtualBox, patchs à jour. Tor Browser en mode **Safest** (JavaScript désactivé par défaut). Outils : navigateur uniquement pour la première phase, pas de screenshot direct de la machine (passage par OCR d'une photo d'écran pour éviter les métadonnées).
>
> Pseudonymes dédiés à l'investigation : jamais de réutilisation d'un pseudo personnel, jamais de référence à Athéna. Lucas prépare trois pseudonymes distincts, un par type de forum à explorer, avec des styles linguistiques légèrement différents. Pas de paiement depuis un compte personnel — budget alloué par Athéna via un wallet crypto dédié à l'investigation, financé depuis un exchange professionnel avec KYC Athéna (pas de KYC Lucas personnel).
>
> Ch.22 détaillera le cadre légal qui encadre cette préparation, Ch.23 l'OPSEC complète.

---

### Chapitre 6 — Onion services (hidden services)

Les sites `.onion` sont l'une des fonctionnalités les plus emblématiques de Tor. Ils permettent à un serveur d'être **anonyme lui-même** — pas seulement ses visiteurs. Le serveur n'expose pas son IP, et les visiteurs qui s'y connectent ne connaissent pas non plus son IP.

#### 6.1 Principe des hidden services

Un hidden service (aussi appelé **onion service**) est un service accessible uniquement via Tor, identifié par une adresse se terminant en `.onion`. L'adresse elle-même est dérivée cryptographiquement de la **clé publique** du service — elle n'est **pas résolue par DNS**.

**Architecture** :
- Le serveur hidden service choisit plusieurs relais Tor comme **introduction points** et leur annonce qu'il est disponible via eux.
- Le serveur publie cette information dans la **hidden service directory** (une table de hachage distribuée sur les relais).
- Quand un client veut se connecter, il recherche dans la directory l'adresse `.onion` du service, trouve ses introduction points, et négocie avec eux.
- Un **rendezvous point** (relais tiers) est établi où client et serveur se rencontrent.
- Les deux parties communiquent via ce rendezvous, chacune masquée par son propre circuit Tor.

Cette architecture implique **six hops** (trois côté client + trois côté serveur) pour la communication — ce qui explique la lenteur relative des sites .onion.

#### 6.2 Onion v3 : les adresses modernes

Les adresses .onion historiques (« v2 ») étaient des hashs tronqués de 16 caractères, par exemple `3g2upl4pq6kufc4m.onion`. Cette génération a été **dépréciée** en octobre 2021 pour cause de vulnérabilités cryptographiques.

Les **onion v3** (actives depuis 2017, seules supportées depuis 2021) sont des adresses de **56 caractères**, dérivées d'une clé Ed25519 (256 bits) plus quelques éléments. Exemple : `duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion` (DuckDuckGo).

Les propriétés des v3 :
- Sécurité cryptographique forte (résistant aux attaques actuellement connues).
- Authentification mutuelle par défaut.
- Possibilité de **onion services authentifiés** — seuls les clients connaissant une clé préalable peuvent se connecter.
- Meilleure résistance au « directory scraping » — il est plus difficile d'énumérer les .onion actifs qu'avec v2.

#### 6.3 Propriétés de sécurité

Un hidden service bien configuré offre plusieurs propriétés.

**Anonymat du serveur** : l'IP réelle du serveur n'est pas exposée aux clients. Même un attaquant qui compromet un client ne peut pas remonter à l'IP du serveur via des moyens cryptographiques simples.

**Authentification du serveur** : l'adresse `.onion` **est** la clé publique du service. Un man-in-the-middle est quasi impossible — si vous vous connectez à `xxxxxxx.onion`, vous êtes cryptographiquement certain de parler à celui qui détient la clé privée correspondante.

**Pas de dépendance aux autorités de certification** : contrairement à HTTPS qui dépend d'une PKI centralisée (autorités de certification), les hidden services n'ont pas ce point de centralisation.

**Résistance aux saisies** : l'infrastructure est globalement distribuée. Pour saisir un service, les autorités doivent identifier et saisir le serveur physique — ce qui nécessite de dé-anonymiser l'opérateur.

**Cependant, ces propriétés ne garantissent pas que le service soit inviolable**. L'histoire des saisies montre que la chaîne faible est souvent :
- L'**OPSEC de l'opérateur** (Ulbricht, Cazes identifiés par leurs erreurs personnelles).
- Les **vulnérabilités applicatives** du service (SQL injection, RCE) qui exposent l'IP via des misconfigurations.
- Les **leaks d'infrastructure** (serveurs DNS publics mal configurés, headers HTTP, fuites via iframes).
- L'**infiltration** (opérations de police sur des années, compromission des clés).

#### 6.4 Les services légitimes en .onion

Beaucoup d'organisations légitimes maintiennent des miroirs .onion pour servir les utilisateurs dans des contextes sensibles (censure, surveillance) ou simplement comme service additionnel.

- **DuckDuckGo** : `duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion`
- **BBC News** : miroir Tor pour servir les pays où la BBC est censurée.
- **New York Times** : miroir pour la protection des sources.
- **ProPublica** : miroir, un des premiers grands médias à en avoir créé un.
- **Facebook** : miroir .onion depuis 2014, notamment pour les utilisateurs en Chine et en Iran.
- **Protonmail** : miroir .onion pour l'accès à la messagerie chiffrée.
- **SecureDrop** : chaque déploiement SecureDrop est un onion service (NYT, Guardian, etc.).
- **Tor Project** lui-même : tous les services (site web, documentation, téléchargements) ont des miroirs .onion.
- **Amnesty International, Reporters Sans Frontières** : miroirs pour les régions sensibles.
- **Ahmia, Torch, Haystak** : moteurs de recherche .onion (indexation limitée de ressources publiques).

Ces miroirs légitimes constituent une part significative des sites actifs — contre-exemple direct au cliché « tout ce qui est .onion est criminel ».

#### 6.5 Les limites pratiques pour les opérateurs

Exploiter un hidden service n'est pas trivial. Plusieurs difficultés.

**Latence élevée** : six hops + chiffrement multiple = latence typique de 500 ms à plusieurs secondes par requête. Un site .onion interactif (forum, marché) est intrinsèquement lent. Les utilisateurs habitués au web clearnet le ressentent.

**DDoS**. Les hidden services sont notoirement vulnérables aux DDoS. Un attaquant peut saturer le service en générant du trafic via Tor (qui le masque) — la cible ne peut pas bloquer l'origine puisqu'elle ne la connaît pas. De nombreux grands forums ont été indisponibles des jours ou semaines suite à des DDoS concurrents. Des techniques de protection existent (proof-of-work, rate-limiting intelligent, Vanguards/onion-balance) mais restent imparfaites.

**Maintenance**. Maintenir un service .onion stable dans la durée est techniquement exigeant. Patching, monitoring, gestion des attaques, renouvellement d'infrastructure — beaucoup de services échouent par épuisement opérationnel des admins plus que par saisie.

**Référencement**. Les .onion ne sont pas indexés par Google. La découverte se fait par liste communautaires (Hidden Wiki historique, The Onion Link List), word-of-mouth, posts sur forums clearnet, moteurs de recherche .onion eux-mêmes (Ahmia, Haystak — indexation partielle).

#### 6.6 Vanity addresses et reconnaissance

Les adresses .onion sont dérivées cryptographiquement, mais il est possible de générer des **vanity addresses** (adresses contenant un préfixe choisi) en brute-forçant des clés jusqu'à trouver une qui donne le préfixe voulu.

Exemples historiques :
- `facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion` commence par `facebook`.
- `propub3r6espa33w.onion` (ProPublica v2 historique) commençait par `propub`.

Pour un préfixe court (4-6 caractères), c'est trivial ; pour un préfixe de 10+ caractères, cela demande des ressources GPU significatives. Générer `facebookwkhpilnemxj7` a mobilisé des ressources Facebook pour en faire une démonstration.

Cette pratique permet aux services légitimes de signaler leur authenticité par un préfixe reconnaissable, mais aussi aux scammers de créer des adresses qui ressemblent aux vrais services (typosquatting .onion — un faux AlphaBay avec un préfixe similaire à l'original).

L'investigateur vérifie toujours l'adresse complète avant de conclure à l'authenticité d'un service.

---

### Chapitre 7 — I2P, Freenet et réseaux alternatifs

Tor n'est pas le seul darknet. Plusieurs réseaux alternatifs coexistent, avec des propriétés différentes. Pour un analyste CTI, leur connaissance est utile : certains acteurs migrent vers ces réseaux quand Tor devient trop surveillé ou quand ils cherchent des propriétés spécifiques.

#### 7.1 I2P (Invisible Internet Project)

**I2P** (invisibleinternet.net) est un darknet développé depuis 2003, conçu pour les communications peer-to-peer dans un réseau fermé (contrairement à Tor qui permet aussi de sortir vers l'Internet clearnet).

**Architecture — « garlic routing »** : variation de l'onion routing où plusieurs messages sont **regroupés en ail** (garlic) avant d'être chiffrés. Cette approche offre des propriétés d'obfuscation du trafic différentes.

**Tunnels unidirectionnels** : contrairement à Tor qui utilise des circuits bidirectionnels, I2P utilise des tunnels séparés pour l'entrée et la sortie. Un serveur a ses tunnels entrants, un client a ses tunnels sortants — cette séparation complique l'analyse de trafic.

**Distribution peer-to-peer** : I2P n'a pas de directory authorities centraux (contrairement aux 9 directory authorities Tor). Chaque nœud participe au routage. Cette décentralisation renforce la résilience mais complique le bootstrap.

**Terminologie propre** : les sites sur I2P s'appellent des **eepsites** et utilisent des adresses en `.i2p` (par exemple `stats.i2p`, `i2p-projekt.i2p`).

**Usages**. I2P est moins populaire que Tor — réseau plus petit (quelques dizaines de milliers de nœuds vs millions d'utilisateurs Tor), interface moins accessible, écosystème applicatif restreint. Les forums cybercriminels russophones maintiennent souvent un miroir I2P en plus de leur .onion, par résilience. Certains acteurs préfèrent I2P pour des communications ciblées où Tor est perçu comme trop surveillé (perception plutôt qu'évidence technique).

**Exemple concret** : IndustrialLeaks (le forum fictif de DARKSTREAM) mentionne un miroir I2P. C'est un pattern typique — un forum sérieux maintient deux points d'entrée indépendants pour résilience face aux saisies.

**Attaques et limites**. I2P a été moins étudié académiquement que Tor, et moins attaqué publiquement — mais les propriétés de sécurité sont similaires. La décentralisation peut être un faux confort : un adversaire qui participe en masse au réseau (sybil attack) peut potentiellement compromettre l'anonymat.

#### 7.2 Freenet / Hyphanet

**Freenet** (rebaptisé **Hyphanet** en 2023) est l'un des plus anciens darknets, lancé en 2000 par Ian Clarke. Modèle radicalement différent de Tor et I2P : **stockage distribué**.

**Principe** : les utilisateurs contribuent de l'espace disque local au réseau. Les contenus publiés sont **chiffrés et dispersés** sur les machines des utilisateurs, sans qu'aucune ne connaisse l'intégralité d'un contenu. Les contenus populaires sont automatiquement répliqués ; les contenus oubliés s'effacent.

**Propriétés** :
- **Résistance à la censure** : supprimer un contenu de Freenet est très difficile — il faudrait saisir toutes les machines qui en hébergent un fragment.
- **Déni plausible** : un utilisateur hébergeant des fragments chiffrés peut plausiblement ignorer ce qu'il héberge.
- **Usage principal** : publication de contenu (sites statiques, blogs, fichiers) plutôt que communication en temps réel.

**Opennet vs Darknet** : Freenet offre deux modes. **Opennet** : tout nœud peut rejoindre. **Darknet** (« friend-to-friend ») : vous n'êtes connecté qu'à des nœuds opérés par des personnes que vous connaissez — résilience maximale mais effet réseau limité.

**Usages criminels** : Freenet a historiquement été un canal de diffusion de CSAM, raison pour laquelle de nombreuses opérations de police l'ont visé. La capacité à poursuivre un utilisateur sur la seule présence de fragments chiffrés (sans preuve qu'il connaissait le contenu) a été discutée dans plusieurs juridictions.

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
- **Redondance** : les opérateurs sérieux maintiennent souvent deux ou trois points d'entrée (onion, i2p, éventuellement Tor v3 authenticated + i2p) pour survivre à une saisie.
- **Évolution défensive** : quand un darknet devient intensément surveillé (perception), une partie de la population migre.

Pour l'investigateur CTI, l'implication pratique : **toujours vérifier si un service cible a un miroir sur un autre darknet**. Un forum saisi sur Tor peut rester opérationnel sur I2P pendant des semaines avant que les autorités l'attrapent aussi. Un acteur privé peut continuer ses activités via I2P après que son .onion est compromis.

---

### Chapitre 8 — Cryptomonnaies et anonymat financier

Les cryptomonnaies sont la couche **financière** du dark web. Sans elles, l'économie clandestine à l'échelle observée serait impossible. Mais les propriétés d'anonymat des cryptomonnaies sont largement mal comprises, y compris par leurs utilisateurs criminels — ce qui explique une part importante des identifications réussies.

#### 8.1 Bitcoin : pseudonymat, pas anonymat

Bitcoin (2009, Satoshi Nakamoto) est la cryptomonnaie historique. Propriété fondamentale souvent mécomprise : Bitcoin est **pseudonyme**, pas **anonyme**.

**Principe** : chaque transaction Bitcoin est enregistrée publiquement dans la blockchain. Tout le monde peut voir : quelle adresse a envoyé combien à quelle adresse, à quel moment. Les adresses sont des chaînes de caractères (par exemple `bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh`) sans lien apparent avec une identité réelle.

**Mais** : à un moment, une adresse Bitcoin doit être liée à une identité pour être utile — que ce soit via un exchange (qui fait du KYC), une merchant (qui a votre livraison), ou toute interaction qui relie l'adresse à un nom. Une fois ce lien établi, l'historique entier de l'adresse devient attribuable.

Cette propriété a structuré toutes les investigations crypto du dark web : les grandes saisies (Silk Road, AlphaBay, Hydra, multiples ransomware) ont reposé sur le traçage blockchain des flux financiers. **Les cryptocurrency tracing firms** (Chainalysis, TRM Labs, Elliptic, CipherTrace/Mastercard) ont construit un écosystème de renseignement blockchain qui est devenu un outil central de lutte contre la cybercriminalité (Ch.31).

#### 8.2 Le traçage Bitcoin en pratique

Plusieurs techniques de traçage sont systématiquement appliquées.

**Clusterisation** : regrouper les adresses qui appartiennent probablement à la même entité, en observant les patterns (adresses qui co-dépensent dans une même transaction sont probablement contrôlées par la même entité).

**Heuristiques de change** : identifier les adresses de change (monnaie rendue) lors d'une transaction pour suivre le portefeuille source.

**Labellisation** : des milliers d'adresses connues sont labellisées (adresses Silk Road historiques, adresses ransomware connues, adresses de grands exchanges type Binance, Coinbase). Les transactions qui touchent ces adresses labellisées donnent des points d'attribution.

**Suivi cross-chain** : les flux passent souvent par plusieurs blockchains (Bitcoin → Ethereum → stablecoin). Les outils modernes suivent ces chaînes.

**Corrélation on-chain / off-chain** : croisement avec données exchanges (requêtes légales pour identifier un compte), surveillance de forums (vendeurs postent parfois leur adresse de paiement), et autres sources.

L'efficacité a été démontrée par une série de cas emblématiques : saisie des fonds Colonial Pipeline (FBI récupère ~2,3 M USD en juin 2021), saisie Bitfinex (DOJ saisit ~3,6 Mrd USD en février 2022), multiples saisies Lazarus, démantèlement Chipmixer (mars 2023), etc.

#### 8.3 Monero : anonymat par construction

**Monero (XMR)** (2014, projet open source) est conçu dès l'origine pour l'anonymat. Trois mécanismes cryptographiques :

**Ring signatures** : chaque transaction inclut plusieurs inputs possibles, dont un seul est le vrai. Un observateur ne peut pas distinguer le véritable input. Par défaut, 16 inputs de décoi ("ring size 16" depuis 2022, renforcé par hard fork).

**Stealth addresses** : chaque transaction génère une adresse unique pour le destinataire, dérivée de sa clé publique. Impossible de lier plusieurs transactions reçues par un même destinataire.

**RingCT** (Ring Confidential Transactions) : les montants des transactions sont chiffrés. Un observateur ne voit pas combien a été transféré — seulement qu'une transaction valide a eu lieu.

**Propriétés** : anonymat par défaut, fungibilité (chaque Monero est interchangeable avec tout autre Monero — impossible de « marquer » une pièce comme suspecte). Monero est devenu la cryptomonnaie de choix pour beaucoup d'acteurs cybercriminels depuis 2019-2020.

**Mais pas infaillible**. La recherche académique et les praticiens ont documenté des **faiblesses** :
- Les **decoys** ne sont pas parfaitement aléatoires — des patterns de sélection peuvent être exploités statistiquement.
- Les anciennes transactions (avant 2017 notamment) étaient bien moins protégées et ont pu être analysées rétrospectivement.
- Des **vulnérabilités d'implémentation** ont été corrigées au fil des ans (problèmes de génération d'aléatoire, fuites dans les logs).
- Les flux **on-ramp / off-ramp** (conversion fiat → Monero, Monero → fiat) passent par des exchanges soumis au KYC, donnant des points d'attribution.
- Les **atomic swaps BTC↔XMR** permettent de convertir sans exchange, mais posent des défis logistiques.
- Certaines agences de renseignement (US, multiples) ont annoncé des **contrats** pour développer des capacités de traçage Monero — le statut exact de ces capacités n'est pas public.

L'état consensuel : Monero offre un anonymat **très fort mais pas absolu**. Traçable avec des moyens importants et des conditions particulières ; intraçable dans la pratique courante face à un adversaire standard.

#### 8.4 Stablecoins : le nouveau facilitateur

Depuis 2020-2021, les **stablecoins** (USDT Tether principalement, USDC dans une moindre mesure) sont devenus **un vecteur massif de transactions dark web**. Raisons :
- **Stabilité** : pas de volatilité (contrairement à Bitcoin qui peut varier de 20% en une semaine).
- **Liquidité** : facilement convertibles partout.
- **Blockchain TRON** : USDT sur TRON est dominant — frais très faibles (~1 cent par transaction), confirmations rapides (~3 secondes). TRON est devenu la blockchain dominante des flux illicites crypto en volume transactionnel.

**Mais** : les stablecoins ne sont **pas anonymes**. Chaque transaction est on-chain et visible. Les émetteurs (Tether pour USDT, Circle pour USDC) peuvent **geler** les adresses sur requête des autorités — Tether a gelé des centaines de millions de dollars d'adresses suspectes sur les années 2022-2024. USDC est encore plus coopérant avec les autorités américaines.

L'attrait des stablecoins pour le dark web est donc structurellement ambigu : plus facile que Bitcoin pour les transactions, plus surveillé que Monero. Beaucoup d'acteurs utilisent USDT comme monnaie d'échange opérationnelle (prix affichés, paiements rapides) mais convertissent en Monero pour le stockage à long terme.

#### 8.5 Les mixers et tumblers

Les **mixers** (ou tumblers) sont des services qui mélangent les fonds de plusieurs utilisateurs pour casser la traçabilité. Vous envoyez 1 BTC, le mixer reçoit aussi les BTC d'autres utilisateurs, et vous renvoie 1 BTC (moins une commission de 1-3%) depuis un pool partagé — théoriquement impossible à relier à votre adresse source.

**Services historiques et statut** :
- **Helix** (saisi en 2020, Larry Harmon condamné à 3 ans de prison).
- **Bitcoin Fog** (saisi en 2021, Roman Sterlingov condamné en 2024).
- **Chipmixer** (saisi en mars 2023 — le DOJ et EPRS estiment ~152 000 BTC blanchis soit ~2,73 Mrd EUR).
- **Tornado Cash** : mixer Ethereum, **sanctionné par l'OFAC en août 2022** — première sanction d'un smart contract dans l'histoire. Des développeurs ont été inculpés, y compris Alexey Pertsev (condamné aux Pays-Bas en mai 2024) et Roman Storm (procès aux US en 2024-2025).
- **Wasabi Wallet, Samourai Wallet** : wallets Bitcoin avec CoinJoin intégré. **Samourai saisi en avril 2024, fondateurs inculpés**. Wasabi continue mais avec restrictions accrues.

**Limites actuelles** : les mixers sont une cible prioritaire des forces de l'ordre et des régulateurs. Leur utilisation est devenue un **signal** — les exchanges KYC refusent souvent de créditer des fonds qui ont transité par un mixer connu. Pour un criminel moderne, utiliser un mixer peut être plus coûteux (frais, délais, déclassement du fund) que de convertir directement en Monero.

#### 8.6 L'off-ramp comme talon d'Achille

Le problème fondamental pour le criminel : **à un moment, il faut convertir la crypto en monnaie utilisable** (fiat pour des achats du quotidien, biens physiques, immobilier). Cette étape **off-ramp** est le talon d'Achille.

Plusieurs canaux, tous partiellement compromis :
- **Exchanges KYC** (Binance, Coinbase, Kraken, OKX) : conversion facile mais laisse des traces sous un nom réel. Soumis à GAFI Travel Rule, TRF, etc.
- **Exchanges non-KYC** (historiquement BTC-e, plus récemment quelques plateformes peu réglementées) : de plus en plus rares sous pression internationale.
- **P2P platforms** (LocalBitcoins historique, Paxful, Binance P2P) : permettent des échanges directs avec moins de KYC, mais volumes limités, risque de scam.
- **OTC desks clandestins** : traders informels, souvent basés dans des juridictions peu régulées (Russie, quelques zones d'Asie), commissions élevées (5-20%).
- **Cartes de débit crypto** : convertissent en fiat au point de vente, mais émetteurs majoritaires KYC.
- **Achats directs en crypto** : immobilier, luxe, voitures — dans les juridictions qui l'acceptent.
- **Nested exchanges** : exchanges qui ont un compte sur un exchange majeur et ré-sertent en interne. Plusieurs ont été sanctionnés par OFAC (Suex, Garantex, Bitzlato).

Les investigations crypto identifient souvent le criminel à l'off-ramp — même après plusieurs mixers, une fois que le fund atteint un exchange KYC, l'identité est obtenue par requête légale. Ch.31 détaille le traçage crypto en profondeur.

#### 8.7 Fil rouge — DARKSTREAM : préparation financière

> **🌐 DARKSTREAM — Épisode 4 : le wallet d'investigation**
>
> Athéna alloue un budget opérationnel à Lucas pour son investigation DARKSTREAM. **3 000 USDT** sur un wallet dédié, financé depuis un exchange professionnel (KYC Athéna, pas Lucas). Usage prévu : paiement du droit d'entrée IndustrialLeaks (~0,005 BTC si requis), achats éventuels d'échantillons (sous coordination DGSI), pourboires occasionnels pour obtenir des informations de membres coopératifs.
>
> Lucas note que le vendeur aero_source demande **65 000 USDT** pour les 420 Go. Athéna **n'a aucune intention d'acheter** — le cadre mandaté est investigation, pas acquisition. Mais le prix demandé est un signal : 65 000 USDT correspond à un dump « premium », ce qui suggère soit de vraies données de valeur, soit un scammer ambitieux.
>
> Lucas prévoit d'utiliser les capacités de traçage blockchain de ses outils (Chainalysis, TRM Labs via l'abonnement Athéna) pour **surveiller** l'adresse BTC affichée par aero_source dans son post — capter les paiements éventuels et identifier les acheteurs. C'est un angle d'attribution précieux : même sans identifier aero_source, identifier **un** acheteur peut donner un point d'entrée investigatif.

---

### Chapitre 9 — Hébergement, infrastructure et résilience

Les services illicites du dark web ne sont pas hébergés par magie. Un serveur physique existe quelque part, avec un opérateur, une facture d'hébergement, et une exposition juridique — même masqués par Tor. Comprendre les mécanismes d'hébergement permet de comprendre où sont les points de défaillance.

#### 9.1 Les choix d'hébergement d'un service .onion

L'opérateur d'un service .onion a plusieurs options.

**Hébergement classique dans un pays « coopératif »** : un VPS chez OVH, Hetzner, Digital Ocean, AWS. Facile, bon marché, mais **totalement exposé à une saisie** si l'opérateur est identifié. La plupart des grandes saisies de marchés dark web ont concerné des infrastructures hébergées dans des clouds classiques — Silk Road chez des hébergeurs américains et islandais, AlphaBay chez des hébergeurs lituaniens, etc.

**Bulletproof hosting** : hébergeurs situés dans des juridictions où la coopération avec les forces de l'ordre est limitée (historiquement Russie, quelques pays d'Europe de l'Est, certaines zones asiatiques), ou hébergeurs qui se spécialisent explicitement dans l'hébergement de contenus « contestés ». Prix 5 à 10 fois plus élevés qu'un hébergement classique, mais résistance accrue. Bulletproof **ne signifie pas invulnérable** — plusieurs grands bulletproof hosts ont été saisis (Atrivo/Intercage 2008, McColo 2008, Russian Business Network, Hostinger/Cyberbunker 2019).

**Auto-hébergement physique** : machine chez soi ou dans un local loué, connexion Internet standard, Tor masquant l'IP. Solution la plus résiliente juridiquement (pas de tiers coopératif à contacter pour les autorités) mais la plus risquée pour l'opérateur (saisie physique de son domicile s'il est identifié, pas de redondance).

**Hébergement distribué** : plusieurs serveurs miroirs dans plusieurs pays, avec load balancing. Augmente la résilience, mais chaque miroir est un point de compromission potentiel.

**Hybrides** : opérateurs sophistiqués combinent plusieurs approches. Un frontend bulletproof pour la face publique, un backend chez un hébergeur différent moins exposé, des backups chiffrés distribués.

#### 9.2 Les mécanismes de résilience typiques

Les grands services clandestins mettent en place plusieurs mécanismes pour survivre aux tentatives de saisie.

**Multiple onion addresses**. Un même service peut publier plusieurs adresses .onion (v3 le permet), avec load balancing via onion-balance. Si une adresse est compromise, les autres restent fonctionnelles.

**Rotation d'adresse**. Certains services changent d'adresse .onion périodiquement (tous les X mois) et communiquent la nouvelle aux utilisateurs via des canaux out-of-band (Telegram, XMPP, mailing list chiffrée). Complique le monitoring long terme mais cohérent avec une posture défensive.

**Multiple darknets**. Maintenir simultanément un .onion et un .i2p (ou Lokinet, ou Freenet) — si un darknet devient intenable, l'autre reste. IndustrialLeaks (fictif) illustre ce pattern.

**Infrastructure distribuée**. Frontend, backend, base de données, stockage de fichiers sur des machines séparées, dans des juridictions différentes. Saisir le frontend ne suffit pas ; il faut aussi identifier les autres composants.

**Clés hors ligne**. Les clés privées les plus critiques (signature des annonces, wallet principal) sont conservées hors ligne, sur des machines air-gapped. Une saisie du serveur public ne donne pas accès aux fonds principaux.

**Backups chiffrés**. Les données opérationnelles sont régulièrement sauvegardées chiffrées sur des infrastructures tierces (cloud storage avec chiffrement client-side, stockage distribué type IPFS). Permet de relancer le service même après saisie complète du serveur principal.

**Kill switches**. Certains opérateurs implémentent des kill switches qui effacent automatiquement les données en cas de signes de compromission (pas d'accès admin depuis X heures, tentative de boot sans la bonne clé). Destiné à limiter les preuves collectables lors d'une saisie.

#### 9.3 Les points d'attaque des forces de l'ordre

Face à cette résilience, les investigateurs visent les points de faiblesse structurels.

**Identification de l'opérateur**. La méthode la plus efficace historiquement. Une fois l'opérateur identifié, son domicile/bureau peut être perquisitionné, ses infrastructures connues saisies simultanément, et ses clés capturées avant qu'il ne puisse les détruire. Ulbricht capturé ordinateur ouvert, Cazes de même en Thaïlande.

**Vulnérabilités applicatives du service**. Une SQL injection, une RCE, une mauvaise configuration CORS peuvent exposer l'IP réelle du serveur. Les services matures font tester régulièrement leur propre sécurité ; les services amateurs sont souvent identifiables ainsi.

**Fuites d'infrastructure**. Headers HTTP qui révèlent le vrai IP, certificats TLS utilisés à la fois sur clearnet et onion, iframes vers des ressources externes qui font un DNS lookup hors Tor, misconfigurations NTP. Le Tor Project publie régulièrement des recommandations pour éviter ces fuites, mais toutes ne sont pas suivies.

**Analyse de trafic**. Pour un adversaire qui peut observer le trafic entrant/sortant d'un hébergeur suspect, corréler avec les patterns d'activité du service .onion peut permettre d'identifier le serveur. Technique coûteuse, mais documentée dans plusieurs investigations.

**Infiltration**. Opérer le service depuis l'intérieur après saisie (Hansa model) ou infiltrer des comptes admin via social engineering, compromission de machines d'opérateurs, ou pivoting via des services tiers qu'ils utilisent.

**Coopération de l'hébergeur**. Pour les services hébergés chez des clouds mainstream, une simple requête légale suffit à obtenir l'identité du client. C'est pourquoi les opérateurs sérieux n'utilisent pas ces hébergeurs — mais beaucoup d'amateurs le font, et les petits services tombent souvent ainsi.

#### 9.4 Le cas emblématique des bulletproof hosts

**Cyberbunker** (originellement Pays-Bas, puis Allemagne) : ancien bunker OTAN reconverti en bulletproof host à partir de 2013. Hébergeait des marchés dark web, des CSAM, des infrastructures criminelles. Saisi en septembre 2019 par la police allemande après une opération de surveillance de trois ans. Le fondateur et plusieurs associés condamnés en 2021. Cas souvent cité comme démonstration que même les bulletproof hosts finissent par tomber.

**Russian Business Network (RBN)** : actif dans les années 2000, St Pétersbourg. Hébergeait malware, phishing, botnets. Jamais saisi stricto sensu, mais progressivement neutralisé par pression sur ses opérateurs de paiement et upstream providers. Dissolution de facto vers 2009.

**Atrivo/Intercage** : US, fermé en 2008 suite à une campagne de denaming par les autres hébergeurs (« de-peering ») qui ont refusé de lui faire du transit.

**McColo** : US, fermé en 2008 de la même manière.

Ces cas illustrent un pattern : les bulletproof hosts finissent par être neutralisés, soit par saisie directe, soit par pression sur leur écosystème (upstream providers, moyens de paiement, banquiers). Durée de vie typique : 5 à 15 ans. Rarement plus.

#### 9.5 L'émergence des « underground ISPs »

Ces dernières années, certains acteurs ont tenté de construire des **infrastructures d'ISP entièrement sous contrôle** — leurs propres connexions Internet, leurs propres IPs, leur propre transit. L'idée : ne plus dépendre d'un hébergeur tiers saisissable, mais opérer comme un FAI miniature.

Cas observés avec profils divers : hébergeurs ayant leur propre AS (Autonomous System) BGP dans des juridictions permissives, liaisons satellite pour bypass des FAI nationaux, infrastructure mesh dans des zones sans contrôle étatique effectif. Reste marginal — exige des investissements importants et des compétences techniques avancées.

#### 9.6 Fil rouge — DARKSTREAM : l'infrastructure d'IndustrialLeaks

> **🌐 DARKSTREAM — Épisode 5 : analyse d'infrastructure**
>
> Lucas documente ce qu'il peut apprendre de l'infrastructure d'IndustrialLeaks. Depuis le forum lui-même, peu d'indices techniques directs — les opérateurs ont suivi les bonnes pratiques OPSEC.
>
> Mais plusieurs signaux indirects :
> - **Trois changements d'adresse .onion** en 18 mois, toujours annoncés à l'avance sur un canal Telegram public associé au forum. Cohérent avec une posture défensive proactive (pas avec une saisie réussie — pas d'interruption longue observable).
> - **Miroir I2P fonctionnel**, avec la même base de données (posts synchronisés). Indique une architecture centralisée avec deux points d'accès plutôt que deux services indépendants.
> - **Disponibilité élevée** : le forum répond en ~800 ms la plupart du temps, quelques pannes de 2-4 heures observables dans les archives communautaires. Cohérent avec un hébergement sérieux, possiblement bulletproof.
> - **Règles internes publiées** : modération active, bannissements documentés, posts de warning aux scammers. Indique un opérateur impliqué, pas un dump-and-forget.
>
> Hypothèse de travail : IndustrialLeaks est probablement hébergé sur un bulletproof host d'Europe de l'Est, avec une équipe de 2-5 opérateurs (un admin principal, des modérateurs russophones), et une infrastructure miroir I2P active. Son modèle économique : droits d'entrée (250 USD × 3 000 membres = ~750 000 USD si on suppose tous payants — irréaliste, plus réaliste quelques centaines de payants), commissions sur ventes (1-3% probablement), peut-être services premium.
>
> Pour Lucas, les implications d'investigation : accès via vouching (privilégier pour la crédibilité de la persona d'investigation), attentes réalistes de durée de vie (1-3 ans avant rotation ou saisie), priorité à la capture d'indices d'authentification des données **avant** que le forum ne disparaisse.

---

## PARTIE II — INFRASTRUCTURES TECHNIQUES ET ANONYMAT

> **Ce que cette partie apprend.** Comprendre les infrastructures techniques qui rendent le dark web possible — architecture Tor, onion services v3, réseaux alternatifs (I2P, Freenet), cryptomonnaies et leur traçabilité, hébergement bulletproof. Comprendre aussi leurs limites — Tor n'est pas magique, Monero n'est pas absolu, un bulletproof host peut être saisi.
>
> **Ce qu'elle ne couvre pas.** Les méthodes d'investigation exploitant ces infrastructures (Partie V et VI), les méthodes concrètes de dé-anonymisation (Ch.29), les techniques de configuration offensive (hors périmètre).
>
> **Ce que vous saurez faire après cette partie.** Expliquer techniquement le fonctionnement de Tor à un collègue, évaluer la résistance d'un service .onion à une saisie, distinguer les propriétés d'anonymat de Bitcoin et Monero, identifier les points de faiblesse typiques d'une infrastructure criminelle.

---

### Chapitre 5 — Architecture de Tor

Tor (The Onion Router) est le darknet dominant. Comprendre son architecture permet de comprendre ses propriétés, ses limites, et les angles d'attaque — défensifs ou offensifs — qui s'appliquent.

#### 5.1 Principe de l'onion routing

L'idée centrale de l'onion routing est **séparer la connaissance de l'origine et de la destination** entre plusieurs nœuds intermédiaires, de telle sorte qu'**aucun nœud seul** ne connaisse les deux extrémités de la communication.

Mécanisme : le client Tor construit un **circuit** à trois nœuds (guard, middle, exit) en négociant des clés de chiffrement successives. Chaque paquet envoyé est **chiffré trois fois**, dans des couches successives. Chaque nœud intermédiaire déchiffre **une couche** pour révéler le saut suivant, sans pouvoir déchiffrer les autres couches.

Concrètement, pour une requête du client Alice vers le site `example.com` :

1. Le client Tor d'Alice choisit trois nœuds : un **guard** (premier relais, connu du client), un **middle** (relais intermédiaire), un **exit** (relais de sortie qui parle au site final).
2. Alice chiffre sa requête en trois couches, dans l'ordre inverse du chemin : couche exit, couche middle, couche guard — chaque couche chiffrée avec la clé du nœud correspondant.
3. Le paquet transite : Alice → guard. Le guard déchiffre sa couche, voit l'adresse du middle mais pas la destination finale.
4. Guard → middle. Le middle déchiffre sa couche, voit l'adresse de l'exit mais ne connaît ni Alice (qui a parlé au guard) ni la destination finale.
5. Middle → exit. L'exit déchiffre sa couche, voit la requête en clair (si HTTP) et l'envoie vers example.com. L'exit connaît la destination mais ne connaît pas Alice.

Réponse : même mécanisme en sens inverse. Chaque nœud ne chiffre qu'une couche avec sa clé sur le retour.

**Propriété clé** : dans ce modèle, aucun nœud seul ne connaît à la fois l'identité de l'origine (Alice) et la destination (example.com). Un adversaire doit contrôler **à la fois le guard et l'exit** pour corréler. C'est toute la sécurité du système — et son talon d'Achille.

#### 5.2 Les types de relais

Le réseau Tor comprend environ **7 000 à 8 000 relais** actifs en 2025-2026, répartis géographiquement (concentration en Europe, US, Canada, quelques en Asie). Ils se classent en catégories.

**Guard relays** : premier nœud d'un circuit, choisi parmi un ensemble de relais stables et bien connectés. Un client Tor utilise le **même petit ensemble de guards** pendant plusieurs mois (rotation lente), pour limiter l'exposition à un attaquant qui compromettrait des guards aléatoirement (l'attaquant a plus de chances de tomber sur un mauvais guard avec rotation rapide).

**Middle relays** : relais intermédiaires, les plus nombreux. Rôle de relais pur, sans visibilité ni sur l'origine ni sur la destination.

**Exit relays** : relais qui parlent au monde extérieur. Les moins nombreux (risque juridique élevé — un abus commis via Tor sort par l'exit, dont l'opérateur peut recevoir des plaintes ou des requêtes légales). Environ 1 000 exits actifs. Certains exits ont des politiques restrictives (bloquent certains ports, certains protocoles).

**Directory authorities** : serveurs qui maintiennent la liste des relais (le « consensus »). Il y a **9 directory authorities** actuellement, opérées par des entités de confiance (universités, Tor Project, individus de long terme). Tous les clients Tor téléchargent périodiquement ce consensus pour choisir leurs circuits.

**Bridges** : relais **non publics** (absents du consensus public), accessibles uniquement à ceux qui en obtiennent l'adresse par des canaux spécifiques (site web du Tor Project, email, Telegram, Messenger). Usage : contourner la censure là où les relais publics sont bloqués.

**Pluggable transports** : techniques d'obfuscation du trafic Tor pour contourner le Deep Packet Inspection. **obfs4** (fait ressembler Tor à du trafic aléatoire), **meek** (fait ressembler Tor à du trafic vers un grand service cloud type Azure, AWS, Fastly — « domain fronting »), **snowflake** (utilise des volontaires côté client comme relais WebRTC).

#### 5.3 Construction d'un circuit — détail

Plus précisément, voici comment un client Tor construit un circuit (simplifié).

1. **Téléchargement du consensus** : le client télécharge la liste des relais et leurs clés publiques auprès d'un directory authority ou d'un cache.

2. **Sélection des relais** : le client choisit un guard (parmi ses guards persistants), un middle, un exit — selon des critères de stabilité, bande passante, géographie (pour éviter par exemple de choisir trois relais dans le même pays), et politiques d'exit.

3. **Handshake avec le guard** : le client établit une connexion TLS avec le guard et négocie une clé symétrique via un protocole d'échange de clés (actuellement NTor — Noise-based Tor handshake).

4. **Extension vers le middle** : le client envoie au guard une commande « extend » chiffrée, qui demande au guard de contacter le middle et de négocier une clé symétrique avec lui. Le client obtient ainsi une clé partagée avec le middle via le guard comme relais.

5. **Extension vers l'exit** : pareil, le client étend le circuit vers l'exit.

Le client dispose maintenant de trois clés symétriques, une avec chaque relais. Toute donnée envoyée sera chiffrée en trois couches.

6. **Envoi de données** : le client construit son paquet en trois couches chiffrées et l'envoie au guard. Le guard déchiffre sa couche, fait suivre au middle, etc.

La durée de vie d'un circuit est typiquement de **10 minutes**, après quoi un nouveau circuit est construit pour les nouvelles connexions. Les streams existants peuvent continuer sur l'ancien circuit.

#### 5.4 Attaques et limites

Tor fournit un anonymat **fort mais pas absolu**. Plusieurs classes d'attaques existent.

**Attaque par corrélation de trafic**. Si un adversaire contrôle (ou observe) à la fois le guard et l'exit d'un circuit, il peut corréler les flux entrants et sortants par leur timing et leur volume, et identifier l'origine et la destination. Cette attaque nécessite une observation globale ou la compromission massive de relais. Les grands services de renseignement (NSA, GCHQ) sont crédités de cette capacité dans certaines conditions.

**Attaques sur les bridges**. Les censeurs ciblent les bridges en enregistrant leur trafic ou en les bloquant par DPI. La course entre obfuscations (nouveaux pluggable transports) et détection est continue.

**Attaques sur le navigateur**. Les utilisateurs de Tor Browser sont parfois attaqués via des exploits navigateur (historiques : **NIT du FBI en 2015 contre Playpen**, plusieurs opérations documentées contre Freedom Hosting). Ces attaques exploitent des vulnérabilités du navigateur sous-jacent (Firefox modifié) pour faire exécuter du code chez l'utilisateur et révéler son IP réelle hors de Tor. Voir Ch.30.

**Attaques par fingerprinting**. Même si l'IP est masquée, l'ensemble du comportement d'un utilisateur (timing, patterns de clics, taille de fenêtre, fingerprint navigateur) peut contribuer à son identification. Tor Browser est conçu pour uniformiser autant que possible les fingerprints (même résolution, même user-agent, anti-canvas), mais la recherche académique montre que l'anonymat parfait est illusoire.

**Attaques sur le DNS**. Si une application autre que Tor Browser fait des requêtes DNS non-tunnelées, elle leak l'IP réelle. C'est pourquoi Tor Browser isole le DNS dans le circuit.

**Erreurs utilisateur**. Loggin avec un compte identifié, réutilisation de pseudonymes, corrélation temporelle par les actions — beaucoup de dé-anonymisations historiques viennent d'erreurs d'OPSEC plus que d'attaques cryptographiques (Ulbricht, Cazes, beaucoup d'administrateurs de Hansa ou Silk Road 2.0).

#### 5.5 Tor Browser et les bonnes pratiques

**Tor Browser** (basé sur Firefox ESR avec modifications majeures) est le client de référence. Il intègre Tor, configure les proxies correctement, active NoScript, définit des paramètres de confidentialité par défaut (pas de cookies tiers persistants, pas de WebRTC, canvas bloqué). Disponible pour Windows, macOS, Linux, Android (Android via Orbot + Firefox-based browser). iOS n'a pas de Tor Browser officiel (limitations App Store) mais Onion Browser est une alternative acceptable.

**Mode Safer / Safest** : Tor Browser offre trois niveaux de sécurité (Standard, Safer, Safest). Safest désactive JavaScript sur tous les sites — recommandé pour l'investigation dark web (beaucoup de sites illicites exploitent des vulnérabilités JS pour identifier les visiteurs, voir Ch.30).

**Tails** : distribution Linux live qui force tout le trafic à passer par Tor, ne laisse aucune trace sur la machine. Usage recommandé pour les analystes travaillant sur des cas sensibles, et pour les journalistes/sources (Edward Snowden l'utilisait). Pas d'amnésie parfaite — une compromission exploitée en live peut leaker des données.

**Whonix** : architecture en deux VM (Whonix-Gateway qui fait le routage Tor, Whonix-Workstation où tournent les applications). L'isolation renforce la sécurité : si la workstation est compromise, elle ne peut pas obtenir l'IP réelle (qui n'est connue que de la gateway).

#### 5.6 Fil rouge — DARKSTREAM : préparation technique

> **🌐 DARKSTREAM — Épisode 3 : setup**
>
> Lucas prépare son environnement d'investigation. Protocole Athéna : **machine dédiée**, non reliée au réseau d'entreprise, allumée uniquement pour les sessions d'investigation. OS : Whonix, Gateway + Workstation dans VirtualBox, patchs à jour. Tor Browser en mode **Safest** (JavaScript désactivé par défaut). Outils : navigateur uniquement pour la première phase, pas de screenshot direct de la machine (passage par OCR d'une photo d'écran pour éviter les métadonnées).
>
> Pseudonymes dédiés à l'investigation : jamais de réutilisation d'un pseudo personnel, jamais de référence à Athéna. Lucas prépare trois pseudonymes distincts, un par type de forum à explorer, avec des styles linguistiques légèrement différents. Pas de paiement depuis un compte personnel — budget alloué par Athéna via un wallet crypto dédié à l'investigation, financé depuis un exchange professionnel avec KYC Athéna (pas de KYC Lucas personnel).
>
> Ch.22 détaillera le cadre légal qui encadre cette préparation, Ch.23 l'OPSEC complète.

---

### Chapitre 6 — Onion services (hidden services)

Les sites `.onion` sont l'une des fonctionnalités les plus emblématiques de Tor. Ils permettent à un serveur d'être **anonyme lui-même** — pas seulement ses visiteurs. Le serveur n'expose pas son IP, et les visiteurs qui s'y connectent ne connaissent pas non plus son IP.

#### 6.1 Principe des hidden services

Un hidden service (aussi appelé **onion service**) est un service accessible uniquement via Tor, identifié par une adresse se terminant en `.onion`. L'adresse elle-même est dérivée cryptographiquement de la **clé publique** du service — elle n'est **pas résolue par DNS**.

**Architecture** :
- Le serveur hidden service choisit plusieurs relais Tor comme **introduction points** et leur annonce qu'il est disponible via eux.
- Le serveur publie cette information dans la **hidden service directory** (une table de hachage distribuée sur les relais).
- Quand un client veut se connecter, il recherche dans la directory l'adresse `.onion` du service, trouve ses introduction points, et négocie avec eux.
- Un **rendezvous point** (relais tiers) est établi où client et serveur se rencontrent.
- Les deux parties communiquent via ce rendezvous, chacune masquée par son propre circuit Tor.

Cette architecture implique **six hops** (trois côté client + trois côté serveur) pour la communication — ce qui explique la lenteur relative des sites .onion.

#### 6.2 Onion v3 : les adresses modernes

Les adresses .onion historiques (« v2 ») étaient des hashs tronqués de 16 caractères, par exemple `3g2upl4pq6kufc4m.onion`. Cette génération a été **dépréciée** en octobre 2021 pour cause de vulnérabilités cryptographiques.

Les **onion v3** (actives depuis 2017, seules supportées depuis 2021) sont des adresses de **56 caractères**, dérivées d'une clé Ed25519 (256 bits) plus quelques éléments. Exemple : `duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion` (DuckDuckGo).

Les propriétés des v3 :
- Sécurité cryptographique forte (résistant aux attaques actuellement connues).
- Authentification mutuelle par défaut.
- Possibilité de **onion services authentifiés** — seuls les clients connaissant une clé préalable peuvent se connecter.
- Meilleure résistance au « directory scraping » — il est plus difficile d'énumérer les .onion actifs qu'avec v2.

#### 6.3 Propriétés de sécurité

Un hidden service bien configuré offre plusieurs propriétés.

**Anonymat du serveur** : l'IP réelle du serveur n'est pas exposée aux clients. Même un attaquant qui compromet un client ne peut pas remonter à l'IP du serveur via des moyens cryptographiques simples.

**Authentification du serveur** : l'adresse `.onion` **est** la clé publique du service. Un man-in-the-middle est quasi impossible — si vous vous connectez à `xxxxxxx.onion`, vous êtes cryptographiquement certain de parler à celui qui détient la clé privée correspondante.

**Pas de dépendance aux autorités de certification** : contrairement à HTTPS qui dépend d'une PKI centralisée (autorités de certification), les hidden services n'ont pas ce point de centralisation.

**Résistance aux saisies** : l'infrastructure est globalement distribuée. Pour saisir un service, les autorités doivent identifier et saisir le serveur physique — ce qui nécessite de dé-anonymiser l'opérateur.

**Cependant, ces propriétés ne garantissent pas que le service soit inviolable**. L'histoire des saisies montre que la chaîne faible est souvent :
- L'**OPSEC de l'opérateur** (Ulbricht, Cazes identifiés par leurs erreurs personnelles).
- Les **vulnérabilités applicatives** du service (SQL injection, RCE) qui exposent l'IP via des misconfigurations.
- Les **leaks d'infrastructure** (serveurs DNS publics mal configurés, headers HTTP, fuites via iframes).
- L'**infiltration** (opérations de police sur des années, compromission des clés).

#### 6.4 Les services légitimes en .onion

Beaucoup d'organisations légitimes maintiennent des miroirs .onion pour servir les utilisateurs dans des contextes sensibles (censure, surveillance) ou simplement comme service additionnel.

- **DuckDuckGo** : `duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion`
- **BBC News** : miroir Tor pour servir les pays où la BBC est censurée.
- **New York Times** : miroir pour la protection des sources.
- **ProPublica** : miroir, un des premiers grands médias à en avoir créé un.
- **Facebook** : miroir .onion depuis 2014, notamment pour les utilisateurs en Chine et en Iran.
- **Protonmail** : miroir .onion pour l'accès à la messagerie chiffrée.
- **SecureDrop** : chaque déploiement SecureDrop est un onion service (NYT, Guardian, etc.).
- **Tor Project** lui-même : tous les services (site web, documentation, téléchargements) ont des miroirs .onion.
- **Amnesty International, Reporters Sans Frontières** : miroirs pour les régions sensibles.
- **Ahmia, Torch, Haystak** : moteurs de recherche .onion (indexation limitée de ressources publiques).

Ces miroirs légitimes constituent une part significative des sites actifs — contre-exemple direct au cliché « tout ce qui est .onion est criminel ».

#### 6.5 Les limites pratiques pour les opérateurs

Exploiter un hidden service n'est pas trivial. Plusieurs difficultés.

**Latence élevée** : six hops + chiffrement multiple = latence typique de 500 ms à plusieurs secondes par requête. Un site .onion interactif (forum, marché) est intrinsèquement lent. Les utilisateurs habitués au web clearnet le ressentent.

**DDoS**. Les hidden services sont notoirement vulnérables aux DDoS. Un attaquant peut saturer le service en générant du trafic via Tor (qui le masque) — la cible ne peut pas bloquer l'origine puisqu'elle ne la connaît pas. De nombreux grands forums ont été indisponibles des jours ou semaines suite à des DDoS concurrents. Des techniques de protection existent (proof-of-work, rate-limiting intelligent, Vanguards/onion-balance) mais restent imparfaites.

**Maintenance**. Maintenir un service .onion stable dans la durée est techniquement exigeant. Patching, monitoring, gestion des attaques, renouvellement d'infrastructure — beaucoup de services échouent par épuisement opérationnel des admins plus que par saisie.

**Référencement**. Les .onion ne sont pas indexés par Google. La découverte se fait par liste communautaires (Hidden Wiki historique, The Onion Link List), word-of-mouth, posts sur forums clearnet, moteurs de recherche .onion eux-mêmes (Ahmia, Haystak — indexation partielle).

#### 6.6 Vanity addresses et reconnaissance

Les adresses .onion sont dérivées cryptographiquement, mais il est possible de générer des **vanity addresses** (adresses contenant un préfixe choisi) en brute-forçant des clés jusqu'à trouver une qui donne le préfixe voulu.

Exemples historiques :
- `facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion` commence par `facebook`.
- `propub3r6espa33w.onion` (ProPublica v2 historique) commençait par `propub`.

Pour un préfixe court (4-6 caractères), c'est trivial ; pour un préfixe de 10+ caractères, cela demande des ressources GPU significatives. Générer `facebookwkhpilnemxj7` a mobilisé des ressources Facebook pour en faire une démonstration.

Cette pratique permet aux services légitimes de signaler leur authenticité par un préfixe reconnaissable, mais aussi aux scammers de créer des adresses qui ressemblent aux vrais services (typosquatting .onion — un faux AlphaBay avec un préfixe similaire à l'original).

L'investigateur vérifie toujours l'adresse complète avant de conclure à l'authenticité d'un service.

---

### Chapitre 7 — I2P, Freenet et réseaux alternatifs

Tor n'est pas le seul darknet. Plusieurs réseaux alternatifs coexistent, avec des propriétés différentes. Pour un analyste CTI, leur connaissance est utile : certains acteurs migrent vers ces réseaux quand Tor devient trop surveillé ou quand ils cherchent des propriétés spécifiques.

#### 7.1 I2P (Invisible Internet Project)

**I2P** (invisibleinternet.net) est un darknet développé depuis 2003, conçu pour les communications peer-to-peer dans un réseau fermé (contrairement à Tor qui permet aussi de sortir vers l'Internet clearnet).

**Architecture — « garlic routing »** : variation de l'onion routing où plusieurs messages sont **regroupés en ail** (garlic) avant d'être chiffrés. Cette approche offre des propriétés d'obfuscation du trafic différentes.

**Tunnels unidirectionnels** : contrairement à Tor qui utilise des circuits bidirectionnels, I2P utilise des tunnels séparés pour l'entrée et la sortie. Un serveur a ses tunnels entrants, un client a ses tunnels sortants — cette séparation complique l'analyse de trafic.

**Distribution peer-to-peer** : I2P n'a pas de directory authorities centraux (contrairement aux 9 directory authorities Tor). Chaque nœud participe au routage. Cette décentralisation renforce la résilience mais complique le bootstrap.

**Terminologie propre** : les sites sur I2P s'appellent des **eepsites** et utilisent des adresses en `.i2p` (par exemple `stats.i2p`, `i2p-projekt.i2p`).

**Usages**. I2P est moins populaire que Tor — réseau plus petit (quelques dizaines de milliers de nœuds vs millions d'utilisateurs Tor), interface moins accessible, écosystème applicatif restreint. Les forums cybercriminels russophones maintiennent souvent un miroir I2P en plus de leur .onion, par résilience. Certains acteurs préfèrent I2P pour des communications ciblées où Tor est perçu comme trop surveillé (perception plutôt qu'évidence technique).

**Exemple concret** : IndustrialLeaks (le forum fictif de DARKSTREAM) mentionne un miroir I2P. C'est un pattern typique — un forum sérieux maintient deux points d'entrée indépendants pour résilience face aux saisies.

**Attaques et limites**. I2P a été moins étudié académiquement que Tor, et moins attaqué publiquement — mais les propriétés de sécurité sont similaires. La décentralisation peut être un faux confort : un adversaire qui participe en masse au réseau (sybil attack) peut potentiellement compromettre l'anonymat.

#### 7.2 Freenet / Hyphanet

**Freenet** (rebaptisé **Hyphanet** en 2023) est l'un des plus anciens darknets, lancé en 2000 par Ian Clarke. Modèle radicalement différent de Tor et I2P : **stockage distribué**.

**Principe** : les utilisateurs contribuent de l'espace disque local au réseau. Les contenus publiés sont **chiffrés et dispersés** sur les machines des utilisateurs, sans qu'aucune ne connaisse l'intégralité d'un contenu. Les contenus populaires sont automatiquement répliqués ; les contenus oubliés s'effacent.

**Propriétés** :
- **Résistance à la censure** : supprimer un contenu de Freenet est très difficile — il faudrait saisir toutes les machines qui en hébergent un fragment.
- **Déni plausible** : un utilisateur hébergeant des fragments chiffrés peut plausiblement ignorer ce qu'il héberge.
- **Usage principal** : publication de contenu (sites statiques, blogs, fichiers) plutôt que communication en temps réel.

**Opennet vs Darknet** : Freenet offre deux modes. **Opennet** : tout nœud peut rejoindre. **Darknet** (« friend-to-friend ») : vous n'êtes connecté qu'à des nœuds opérés par des personnes que vous connaissez — résilience maximale mais effet réseau limité.

**Usages criminels** : Freenet a historiquement été un canal de diffusion de CSAM, raison pour laquelle de nombreuses opérations de police l'ont visé. La capacité à poursuivre un utilisateur sur la seule présence de fragments chiffrés (sans preuve qu'il connaissait le contenu) a été discutée dans plusieurs juridictions.

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
- **Redondance** : les opérateurs sérieux maintiennent souvent deux ou trois points d'entrée (onion, i2p, éventuellement Tor v3 authenticated + i2p) pour survivre à une saisie.
- **Évolution défensive** : quand un darknet devient intensément surveillé (perception), une partie de la population migre.

Pour l'investigateur CTI, l'implication pratique : **toujours vérifier si un service cible a un miroir sur un autre darknet**. Un forum saisi sur Tor peut rester opérationnel sur I2P pendant des semaines avant que les autorités l'attrapent aussi. Un acteur privé peut continuer ses activités via I2P après que son .onion est compromis.

---

### Chapitre 8 — Cryptomonnaies et anonymat financier

Les cryptomonnaies sont la couche **financière** du dark web. Sans elles, l'économie clandestine à l'échelle observée serait impossible. Mais les propriétés d'anonymat des cryptomonnaies sont largement mal comprises, y compris par leurs utilisateurs criminels — ce qui explique une part importante des identifications réussies.

#### 8.1 Bitcoin : pseudonymat, pas anonymat

Bitcoin (2009, Satoshi Nakamoto) est la cryptomonnaie historique. Propriété fondamentale souvent mécomprise : Bitcoin est **pseudonyme**, pas **anonyme**.

**Principe** : chaque transaction Bitcoin est enregistrée publiquement dans la blockchain. Tout le monde peut voir : quelle adresse a envoyé combien à quelle adresse, à quel moment. Les adresses sont des chaînes de caractères (par exemple `bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh`) sans lien apparent avec une identité réelle.

**Mais** : à un moment, une adresse Bitcoin doit être liée à une identité pour être utile — que ce soit via un exchange (qui fait du KYC), une merchant (qui a votre livraison), ou toute interaction qui relie l'adresse à un nom. Une fois ce lien établi, l'historique entier de l'adresse devient attribuable.

Cette propriété a structuré toutes les investigations crypto du dark web : les grandes saisies (Silk Road, AlphaBay, Hydra, multiples ransomware) ont reposé sur le traçage blockchain des flux financiers. **Les cryptocurrency tracing firms** (Chainalysis, TRM Labs, Elliptic, CipherTrace/Mastercard) ont construit un écosystème de renseignement blockchain qui est devenu un outil central de lutte contre la cybercriminalité (Ch.31).

#### 8.2 Le traçage Bitcoin en pratique

Plusieurs techniques de traçage sont systématiquement appliquées.

**Clusterisation** : regrouper les adresses qui appartiennent probablement à la même entité, en observant les patterns (adresses qui co-dépensent dans une même transaction sont probablement contrôlées par la même entité).

**Heuristiques de change** : identifier les adresses de change (monnaie rendue) lors d'une transaction pour suivre le portefeuille source.

**Labellisation** : des milliers d'adresses connues sont labellisées (adresses Silk Road historiques, adresses ransomware connues, adresses de grands exchanges type Binance, Coinbase). Les transactions qui touchent ces adresses labellisées donnent des points d'attribution.

**Suivi cross-chain** : les flux passent souvent par plusieurs blockchains (Bitcoin → Ethereum → stablecoin). Les outils modernes suivent ces chaînes.

**Corrélation on-chain / off-chain** : croisement avec données exchanges (requêtes légales pour identifier un compte), surveillance de forums (vendeurs postent parfois leur adresse de paiement), et autres sources.

L'efficacité a été démontrée par une série de cas emblématiques : saisie des fonds Colonial Pipeline (FBI récupère ~2,3 M USD en juin 2021), saisie Bitfinex (DOJ saisit ~3,6 Mrd USD en février 2022), multiples saisies Lazarus, démantèlement Chipmixer (mars 2023), etc.

#### 8.3 Monero : anonymat par construction

**Monero (XMR)** (2014, projet open source) est conçu dès l'origine pour l'anonymat. Trois mécanismes cryptographiques :

**Ring signatures** : chaque transaction inclut plusieurs inputs possibles, dont un seul est le vrai. Un observateur ne peut pas distinguer le véritable input. Par défaut, 16 inputs de décoi ("ring size 16" depuis 2022, renforcé par hard fork).

**Stealth addresses** : chaque transaction génère une adresse unique pour le destinataire, dérivée de sa clé publique. Impossible de lier plusieurs transactions reçues par un même destinataire.

**RingCT** (Ring Confidential Transactions) : les montants des transactions sont chiffrés. Un observateur ne voit pas combien a été transféré — seulement qu'une transaction valide a eu lieu.

**Propriétés** : anonymat par défaut, fungibilité (chaque Monero est interchangeable avec tout autre Monero — impossible de « marquer » une pièce comme suspecte). Monero est devenu la cryptomonnaie de choix pour beaucoup d'acteurs cybercriminels depuis 2019-2020.

**Mais pas infaillible**. La recherche académique et les praticiens ont documenté des **faiblesses** :
- Les **decoys** ne sont pas parfaitement aléatoires — des patterns de sélection peuvent être exploités statistiquement.
- Les anciennes transactions (avant 2017 notamment) étaient bien moins protégées et ont pu être analysées rétrospectivement.
- Des **vulnérabilités d'implémentation** ont été corrigées au fil des ans (problèmes de génération d'aléatoire, fuites dans les logs).
- Les flux **on-ramp / off-ramp** (conversion fiat → Monero, Monero → fiat) passent par des exchanges soumis au KYC, donnant des points d'attribution.
- Les **atomic swaps BTC↔XMR** permettent de convertir sans exchange, mais posent des défis logistiques.
- Certaines agences de renseignement (US, multiples) ont annoncé des **contrats** pour développer des capacités de traçage Monero — le statut exact de ces capacités n'est pas public.

L'état consensuel : Monero offre un anonymat **très fort mais pas absolu**. Traçable avec des moyens importants et des conditions particulières ; intraçable dans la pratique courante face à un adversaire standard.

#### 8.4 Stablecoins : le nouveau facilitateur

Depuis 2020-2021, les **stablecoins** (USDT Tether principalement, USDC dans une moindre mesure) sont devenus **un vecteur massif de transactions dark web**. Raisons :
- **Stabilité** : pas de volatilité (contrairement à Bitcoin qui peut varier de 20% en une semaine).
- **Liquidité** : facilement convertibles partout.
- **Blockchain TRON** : USDT sur TRON est dominant — frais très faibles (~1 cent par transaction), confirmations rapides (~3 secondes). TRON est devenu la blockchain dominante des flux illicites crypto en volume transactionnel.

**Mais** : les stablecoins ne sont **pas anonymes**. Chaque transaction est on-chain et visible. Les émetteurs (Tether pour USDT, Circle pour USDC) peuvent **geler** les adresses sur requête des autorités — Tether a gelé des centaines de millions de dollars d'adresses suspectes sur les années 2022-2024. USDC est encore plus coopérant avec les autorités américaines.

L'attrait des stablecoins pour le dark web est donc structurellement ambigu : plus facile que Bitcoin pour les transactions, plus surveillé que Monero. Beaucoup d'acteurs utilisent USDT comme monnaie d'échange opérationnelle (prix affichés, paiements rapides) mais convertissent en Monero pour le stockage à long terme.

#### 8.5 Les mixers et tumblers

Les **mixers** (ou tumblers) sont des services qui mélangent les fonds de plusieurs utilisateurs pour casser la traçabilité. Vous envoyez 1 BTC, le mixer reçoit aussi les BTC d'autres utilisateurs, et vous renvoie 1 BTC (moins une commission de 1-3%) depuis un pool partagé — théoriquement impossible à relier à votre adresse source.

**Services historiques et statut** :
- **Helix** (saisi en 2020, Larry Harmon condamné à 3 ans de prison).
- **Bitcoin Fog** (saisi en 2021, Roman Sterlingov condamné en 2024).
- **Chipmixer** (saisi en mars 2023 — le DOJ et EPRS estiment ~152 000 BTC blanchis soit ~2,73 Mrd EUR).
- **Tornado Cash** : mixer Ethereum, **sanctionné par l'OFAC en août 2022** — première sanction d'un smart contract dans l'histoire. Des développeurs ont été inculpés, y compris Alexey Pertsev (condamné aux Pays-Bas en mai 2024) et Roman Storm (procès aux US en 2024-2025).
- **Wasabi Wallet, Samourai Wallet** : wallets Bitcoin avec CoinJoin intégré. **Samourai saisi en avril 2024, fondateurs inculpés**. Wasabi continue mais avec restrictions accrues.

**Limites actuelles** : les mixers sont une cible prioritaire des forces de l'ordre et des régulateurs. Leur utilisation est devenue un **signal** — les exchanges KYC refusent souvent de créditer des fonds qui ont transité par un mixer connu. Pour un criminel moderne, utiliser un mixer peut être plus coûteux (frais, délais, déclassement du fund) que de convertir directement en Monero.

#### 8.6 L'off-ramp comme talon d'Achille

Le problème fondamental pour le criminel : **à un moment, il faut convertir la crypto en monnaie utilisable** (fiat pour des achats du quotidien, biens physiques, immobilier). Cette étape **off-ramp** est le talon d'Achille.

Plusieurs canaux, tous partiellement compromis :
- **Exchanges KYC** (Binance, Coinbase, Kraken, OKX) : conversion facile mais laisse des traces sous un nom réel. Soumis à GAFI Travel Rule, TRF, etc.
- **Exchanges non-KYC** (historiquement BTC-e, plus récemment quelques plateformes peu réglementées) : de plus en plus rares sous pression internationale.
- **P2P platforms** (LocalBitcoins historique, Paxful, Binance P2P) : permettent des échanges directs avec moins de KYC, mais volumes limités, risque de scam.
- **OTC desks clandestins** : traders informels, souvent basés dans des juridictions peu régulées (Russie, quelques zones d'Asie), commissions élevées (5-20%).
- **Cartes de débit crypto** : convertissent en fiat au point de vente, mais émetteurs majoritaires KYC.
- **Achats directs en crypto** : immobilier, luxe, voitures — dans les juridictions qui l'acceptent.
- **Nested exchanges** : exchanges qui ont un compte sur un exchange majeur et ré-sertent en interne. Plusieurs ont été sanctionnés par OFAC (Suex, Garantex, Bitzlato).

Les investigations crypto identifient souvent le criminel à l'off-ramp — même après plusieurs mixers, une fois que le fund atteint un exchange KYC, l'identité est obtenue par requête légale. Ch.31 détaille le traçage crypto en profondeur.

#### 8.7 Fil rouge — DARKSTREAM : préparation financière

> **🌐 DARKSTREAM — Épisode 4 : le wallet d'investigation**
>
> Athéna alloue un budget opérationnel à Lucas pour son investigation DARKSTREAM. **3 000 USDT** sur un wallet dédié, financé depuis un exchange professionnel (KYC Athéna, pas Lucas). Usage prévu : paiement du droit d'entrée IndustrialLeaks (~0,005 BTC si requis), achats éventuels d'échantillons (sous coordination DGSI), pourboires occasionnels pour obtenir des informations de membres coopératifs.
>
> Lucas note que le vendeur aero_source demande **65 000 USDT** pour les 420 Go. Athéna **n'a aucune intention d'acheter** — le cadre mandaté est investigation, pas acquisition. Mais le prix demandé est un signal : 65 000 USDT correspond à un dump « premium », ce qui suggère soit de vraies données de valeur, soit un scammer ambitieux.
>
> Lucas prévoit d'utiliser les capacités de traçage blockchain de ses outils (Chainalysis, TRM Labs via l'abonnement Athéna) pour **surveiller** l'adresse BTC affichée par aero_source dans son post — capter les paiements éventuels et identifier les acheteurs. C'est un angle d'attribution précieux : même sans identifier aero_source, identifier **un** acheteur peut donner un point d'entrée investigatif.

---

### Chapitre 9 — Hébergement, infrastructure et résilience

Les services illicites du dark web ne sont pas hébergés par magie. Un serveur physique existe quelque part, avec un opérateur, une facture d'hébergement, et une exposition juridique — même masqués par Tor. Comprendre les mécanismes d'hébergement permet de comprendre où sont les points de défaillance.

#### 9.1 Les choix d'hébergement d'un service .onion

L'opérateur d'un service .onion a plusieurs options.

**Hébergement classique dans un pays « coopératif »** : un VPS chez OVH, Hetzner, Digital Ocean, AWS. Facile, bon marché, mais **totalement exposé à une saisie** si l'opérateur est identifié. La plupart des grandes saisies de marchés dark web ont concerné des infrastructures hébergées dans des clouds classiques — Silk Road chez des hébergeurs américains et islandais, AlphaBay chez des hébergeurs lituaniens, etc.

**Bulletproof hosting** : hébergeurs situés dans des juridictions où la coopération avec les forces de l'ordre est limitée (historiquement Russie, quelques pays d'Europe de l'Est, certaines zones asiatiques), ou hébergeurs qui se spécialisent explicitement dans l'hébergement de contenus « contestés ». Prix 5 à 10 fois plus élevés qu'un hébergement classique, mais résistance accrue. Bulletproof **ne signifie pas invulnérable** — plusieurs grands bulletproof hosts ont été saisis (Atrivo/Intercage 2008, McColo 2008, Russian Business Network, Hostinger/Cyberbunker 2019).

**Auto-hébergement physique** : machine chez soi ou dans un local loué, connexion Internet standard, Tor masquant l'IP. Solution la plus résiliente juridiquement (pas de tiers coopératif à contacter pour les autorités) mais la plus risquée pour l'opérateur (saisie physique de son domicile s'il est identifié, pas de redondance).

**Hébergement distribué** : plusieurs serveurs miroirs dans plusieurs pays, avec load balancing. Augmente la résilience, mais chaque miroir est un point de compromission potentiel.

**Hybrides** : opérateurs sophistiqués combinent plusieurs approches. Un frontend bulletproof pour la face publique, un backend chez un hébergeur différent moins exposé, des backups chiffrés distribués.

#### 9.2 Les mécanismes de résilience typiques

Les grands services clandestins mettent en place plusieurs mécanismes pour survivre aux tentatives de saisie.

**Multiple onion addresses**. Un même service peut publier plusieurs adresses .onion (v3 le permet), avec load balancing via onion-balance. Si une adresse est compromise, les autres restent fonctionnelles.

**Rotation d'adresse**. Certains services changent d'adresse .onion périodiquement (tous les X mois) et communiquent la nouvelle aux utilisateurs via des canaux out-of-band (Telegram, XMPP, mailing list chiffrée). Complique le monitoring long terme mais cohérent avec une posture défensive.

**Multiple darknets**. Maintenir simultanément un .onion et un .i2p (ou Lokinet, ou Freenet) — si un darknet devient intenable, l'autre reste. IndustrialLeaks (fictif) illustre ce pattern.

**Infrastructure distribuée**. Frontend, backend, base de données, stockage de fichiers sur des machines séparées, dans des juridictions différentes. Saisir le frontend ne suffit pas ; il faut aussi identifier les autres composants.

**Clés hors ligne**. Les clés privées les plus critiques (signature des annonces, wallet principal) sont conservées hors ligne, sur des machines air-gapped. Une saisie du serveur public ne donne pas accès aux fonds principaux.

**Backups chiffrés**. Les données opérationnelles sont régulièrement sauvegardées chiffrées sur des infrastructures tierces (cloud storage avec chiffrement client-side, stockage distribué type IPFS). Permet de relancer le service même après saisie complète du serveur principal.

**Kill switches**. Certains opérateurs implémentent des kill switches qui effacent automatiquement les données en cas de signes de compromission (pas d'accès admin depuis X heures, tentative de boot sans la bonne clé). Destiné à limiter les preuves collectables lors d'une saisie.

#### 9.3 Les points d'attaque des forces de l'ordre

Face à cette résilience, les investigateurs visent les points de faiblesse structurels.

**Identification de l'opérateur**. La méthode la plus efficace historiquement. Une fois l'opérateur identifié, son domicile/bureau peut être perquisitionné, ses infrastructures connues saisies simultanément, et ses clés capturées avant qu'il ne puisse les détruire. Ulbricht capturé ordinateur ouvert, Cazes de même en Thaïlande.

**Vulnérabilités applicatives du service**. Une SQL injection, une RCE, une mauvaise configuration CORS peuvent exposer l'IP réelle du serveur. Les services matures font tester régulièrement leur propre sécurité ; les services amateurs sont souvent identifiables ainsi.

**Fuites d'infrastructure**. Headers HTTP qui révèlent le vrai IP, certificats TLS utilisés à la fois sur clearnet et onion, iframes vers des ressources externes qui font un DNS lookup hors Tor, misconfigurations NTP. Le Tor Project publie régulièrement des recommandations pour éviter ces fuites, mais toutes ne sont pas suivies.

**Analyse de trafic**. Pour un adversaire qui peut observer le trafic entrant/sortant d'un hébergeur suspect, corréler avec les patterns d'activité du service .onion peut permettre d'identifier le serveur. Technique coûteuse, mais documentée dans plusieurs investigations.

**Infiltration**. Opérer le service depuis l'intérieur après saisie (Hansa model) ou infiltrer des comptes admin via social engineering, compromission de machines d'opérateurs, ou pivoting via des services tiers qu'ils utilisent.

**Coopération de l'hébergeur**. Pour les services hébergés chez des clouds mainstream, une simple requête légale suffit à obtenir l'identité du client. C'est pourquoi les opérateurs sérieux n'utilisent pas ces hébergeurs — mais beaucoup d'amateurs le font, et les petits services tombent souvent ainsi.

#### 9.4 Le cas emblématique des bulletproof hosts

**Cyberbunker** (originellement Pays-Bas, puis Allemagne) : ancien bunker OTAN reconverti en bulletproof host à partir de 2013. Hébergeait des marchés dark web, des CSAM, des infrastructures criminelles. Saisi en septembre 2019 par la police allemande après une opération de surveillance de trois ans. Le fondateur et plusieurs associés condamnés en 2021. Cas souvent cité comme démonstration que même les bulletproof hosts finissent par tomber.

**Russian Business Network (RBN)** : actif dans les années 2000, St Pétersbourg. Hébergeait malware, phishing, botnets. Jamais saisi stricto sensu, mais progressivement neutralisé par pression sur ses opérateurs de paiement et upstream providers. Dissolution de facto vers 2009.

**Atrivo/Intercage** : US, fermé en 2008 suite à une campagne de denaming par les autres hébergeurs (« de-peering ») qui ont refusé de lui faire du transit.

**McColo** : US, fermé en 2008 de la même manière.

Ces cas illustrent un pattern : les bulletproof hosts finissent par être neutralisés, soit par saisie directe, soit par pression sur leur écosystème (upstream providers, moyens de paiement, banquiers). Durée de vie typique : 5 à 15 ans. Rarement plus.

#### 9.5 L'émergence des « underground ISPs »

Ces dernières années, certains acteurs ont tenté de construire des **infrastructures d'ISP entièrement sous contrôle** — leurs propres connexions Internet, leurs propres IPs, leur propre transit. L'idée : ne plus dépendre d'un hébergeur tiers saisissable, mais opérer comme un FAI miniature.

Cas observés avec profils divers : hébergeurs ayant leur propre AS (Autonomous System) BGP dans des juridictions permissives, liaisons satellite pour bypass des FAI nationaux, infrastructure mesh dans des zones sans contrôle étatique effectif. Reste marginal — exige des investissements importants et des compétences techniques avancées.

#### 9.6 Fil rouge — DARKSTREAM : l'infrastructure d'IndustrialLeaks

> **🌐 DARKSTREAM — Épisode 5 : analyse d'infrastructure**
>
> Lucas documente ce qu'il peut apprendre de l'infrastructure d'IndustrialLeaks. Depuis le forum lui-même, peu d'indices techniques directs — les opérateurs ont suivi les bonnes pratiques OPSEC.
>
> Mais plusieurs signaux indirects :
> - **Trois changements d'adresse .onion** en 18 mois, toujours annoncés à l'avance sur un canal Telegram public associé au forum. Cohérent avec une posture défensive proactive (pas avec une saisie réussie — pas d'interruption longue observable).
> - **Miroir I2P fonctionnel**, avec la même base de données (posts synchronisés). Indique une architecture centralisée avec deux points d'accès plutôt que deux services indépendants.
> - **Disponibilité élevée** : le forum répond en ~800 ms la plupart du temps, quelques pannes de 2-4 heures observables dans les archives communautaires. Cohérent avec un hébergement sérieux, possiblement bulletproof.
> - **Règles internes publiées** : modération active, bannissements documentés, posts de warning aux scammers. Indique un opérateur impliqué, pas un dump-and-forget.
>
> Hypothèse de travail : IndustrialLeaks est probablement hébergé sur un bulletproof host d'Europe de l'Est, avec une équipe de 2-5 opérateurs (un admin principal, des modérateurs russophones), et une infrastructure miroir I2P active. Son modèle économique : droits d'entrée (250 USD × 3 000 membres = ~750 000 USD si on suppose tous payants — irréaliste, plus réaliste quelques centaines de payants), commissions sur ventes (1-3% probablement), peut-être services premium.
>
> Pour Lucas, les implications d'investigation : accès via vouching (privilégier pour la crédibilité de la persona d'investigation), attentes réalistes de durée de vie (1-3 ans avant rotation ou saisie), priorité à la capture d'indices d'authentification des données **avant** que le forum ne disparaisse.

---

## PARTIE III — ÉCOSYSTÈMES DU DARK WEB : ESPACES, ACTEURS ET CULTURE

> **Ce que cette partie apprend.** Connaître concrètement les types d'espaces (forums, marchés, leak sites, messageries, marchés spécialisés) et les acteurs qui les peuplent. Comprendre leurs codes, leurs dynamiques, leurs économies. Maîtriser les objets d'investigation que rencontrera l'analyste.
>
> **Ce qu'elle ne couvre pas.** L'économie clandestine dans son ensemble (Partie IV), les méthodes de collecte (Partie V), les mécanismes d'attribution (Partie VI).
>
> **Ce que vous saurez faire après cette partie.** Reconnaître un forum sérieux d'un forum scam, lire un post de leak site ransomware avec discernement, comprendre ce qu'achètent vraiment les acheteurs sur Russian Market, et situer un vendeur de 0-day dans la chaîne d'attaque.

---

### Chapitre 10 — Forums clandestins : culture, hiérarchie et codes

Les forums sont l'ossature sociale du dark web. Contrairement aux marchés qui sont des points de transaction et aux messageries qui sont des canaux éphémères, les forums sont des **espaces de communauté persistants** où se construisent les réputations, se partagent les connaissances, et se recrutent les collaborations.

#### 10.1 Typologie des forums

Les forums varient par leur **spécialité** et leur **langue**.

**Forums généralistes cybercriminels**. XSS Forum (ex-DamageLab, russophone, historique), Exploit.in (russophone), BreachForums (anglophone — succession de plusieurs instances après saisies, la plus récente opérée par ShinyHunters après l'arrestation de Pompompurin en 2023 puis de Baphomet en 2024). Ces forums couvrent un spectre large : vente de données, discussions sur le hacking, recherche de partenaires, ventes d'outils.

**Forums spécialisés par thématique**. Carding (BriansClub, WWH Club), fraude bancaire, ransomware, drogue (forums adjacents aux marchés), armes (très rares, majoritairement scams), CSAM (priorité 1 des forces de l'ordre).

**Forums géographiques**. Marchés régionaux — forums ukrainien, polonais, chinois, coréen, persophone, arabophone. Chaque bloc avec ses codes et ses acteurs.

**Forums de niche**. **IndustrialLeaks** (fictif, DARKSTREAM) est un exemple de ces forums nichés — spécialisation sur un segment (données industrielles) permet de concentrer une communauté de confiance plus étroite.

**Forums « respectables »** vs **forums low-end**. Les forums sérieux (XSS, Exploit) ont un KYC interne fort — vouching, tests techniques, réputation durable. Les forums low-end sont ouverts à tous, majoritairement peuplés de script kiddies et scammers.

#### 10.2 Hiérarchie de membres

Structure typique d'un forum sérieux.

**Newcomer / Noob** : membre nouvellement inscrit, peu ou pas de posts. Accès limité — consultation des zones publiques, pas d'accès aux zones premium, pas droit de poster dans certains canaux.

**Member** : membre établi, quelques mois d'ancienneté, posts réguliers. Accès élargi, peut répondre à des posts, commencer à construire une réputation.

**Trusted / Verified** : membre vérifié — soit par **vouching** (parrainage par un membre établi qui engage sa réputation), soit par des transactions réussies, soit par un test technique. Peut vendre, peut poster dans les zones premium.

**VIP / Senior** : membre de très long terme avec réputation solide. Souvent des acteurs impliqués dans les activités majeures (opérateurs ransomware, IAB de premier plan). Accès à toutes les zones, peut parrainer des newcomers.

**Moderator** : modérateurs nommés par les admins. Arbitrent les litiges, bannissent les comptes indésirables, surveillent l'activité. Leur identité réelle est souvent connue des admins uniquement.

**Admin** : opérateurs du forum. Peuvent voir tout, décider des règles, collecter les droits d'entrée et commissions.

**Lurkers** : lecteurs silencieux. Les forums sérieux les tolèrent avec réserve — un compte inactif pendant 6 mois peut être supprimé. Les acteurs défensifs (analystes CTI, forces de l'ordre) sont presque toujours des lurkers par défaut.

#### 10.3 Règles internes et modération

Les forums sérieux ont des règles publiées et appliquées. Variations selon les forums, mais constantes récurrentes.

**Interdictions typiques** :
- **Pédopornographie** : universellement interdite, même dans les forums criminels. Raison : attraction maximale des forces de l'ordre, destruction potentielle du forum.
- **Cibles sensibles** : dans les forums russophones, ciblage d'entités CEI souvent interdit par règle (protection politique implicite du Kremlin envers ces acteurs, en échange tacite d'un ciblage exclusif hors-CEI).
- **Dox personnels** : publication d'informations personnelles sur des membres, sauf dispute résolue par arbitrage.
- **Scam** : membre scammant un autre membre est bannissable — mais prouver le scam est toujours l'objet de débats.
- **Multi-accounts** : création de plusieurs comptes pour simuler la popularité (sock puppets).

**Sanctions** :
- **Warning** : avertissement, souvent assorti d'une perte de privilèges temporaire.
- **Bannissement** : temporaire (jours/semaines) ou définitif. Le compte ban est souvent conservé publiquement avec motif — signal pour la communauté.
- **Bannissement étendu** : dans certains forums sérieux, un bannissement sur un forum est communiqué à d'autres forums partenaires, créant un « blacklisting » cross-forum.

**Arbitrage** : en cas de litige commercial, un modérateur ou admin arbitre. Peut imposer un remboursement partiel, valider le scam, ou déclarer l'affaire non-résolue. Le pouvoir d'arbitrage est considérable — un admin corrompu ou compromis peut basculer le destin d'une dispute.

#### 10.4 Codes culturels et jargon

Chaque forum a ses codes. Certains se retrouvent largement dans l'écosystème.

**Salutations et conventions**. « Hi all », « Greetings », « Bro » selon le style. Les forums russophones utilisent **Привет** (privet), **Коллеги** (kollegi — « collègues »), **Уважаемые** (uvazhaemye — « estimés »). Les usages trahissent parfois l'origine : un anglophone qui écrit « Privet all » tente probablement de se faire passer pour russophone.

**Termes techniques**. **FUD** (Fully Undetected — se dit d'un malware indétectable par les AV), **stub**, **crypter**, **binder**, **loader**. **IAB** (Initial Access Broker), **RaaS**, **CaaS**. Les forums spécialisés ont un lexique dense ; maîtriser ce lexique est essentiel pour comprendre les posts et ne pas se trahir.

**Formats de post standardisés**. Vente de données : description du contenu, échantillon gratuit, méthode de paiement acceptée, méthode de contact (Jabber/XMPP, Telegram, TOX, messagerie du forum). Annonce IAB : pays, secteur, type d'accès (VPN, RDP, Citrix, Active Directory), niveau de privilèges (user, admin local, admin domaine), revenue annuel de la cible, prix demandé.

**Réactions et feedback**. Systèmes de ratings, reviews, reputation score. Forums avancés : positive/negative feedback comme eBay, avec commentaires.

**Signature et PGP**. Membres sérieux signent leurs posts en PGP — garantit que le compte n'a pas été usurpé. Un vendeur établi change rarement sa clé PGP sur la durée. Une rotation de clé PGP est un signal de changement d'opérateur (rachat de compte, compromis).

#### 10.5 Économie des forums

Sources de revenus pour les opérateurs.

**Droits d'entrée**. Forums à accès payant : 50-500 USD typiquement. IndustrialLeaks demanderait 0,005 BTC (~250 USD actuel). Barrière à l'entrée qui filtre les simples curieux et monétise la curiosité.

**Abonnements premium**. Accès aux zones VIP avec contenus plus sensibles (0-days, leaks privés, tutoriaux avancés). 100-1 000 USD/mois.

**Commissions sur ventes**. 1-5% sur chaque transaction, collectés via l'escrow du forum.

**Vente de services**. Hosting pour membres, advertising pour vendeurs, slots prioritaires.

**Droits de vouching**. Certains forums monétisent les droits de vouching — un membre établi peut vendre ses « slots » de parrainage.

Un forum sérieux actif peut générer 50 000 à 500 000 USD/an pour ses opérateurs, parfois davantage. Modèle économique durable tant que la base active reste fidèle.

#### 10.6 Cycle de vie typique

Les forums dark web ont des cycles de vie prévisibles.

**Phase 1 — Lancement**. Fondateur crée le forum, recrute quelques membres initiaux (souvent de forums existants ou de son réseau). Période de 6-12 mois où le forum se fait une réputation.

**Phase 2 — Croissance**. Le forum gagne en traction, plus de membres, activité soutenue. Les opérateurs investissent dans la modération, la résilience technique, le marketing discret (posts sur forums existants). Peut durer 2-5 ans.

**Phase 3 — Maturité**. Le forum est reconnu comme un acteur majeur dans son segment. Communauté stable, revenus soutenus. Peut durer plusieurs années avec peu de changement.

**Phase 4 — Décadence ou événement de rupture**. Plusieurs scénarios :
- **Saisie par les autorités** : Hydra avril 2022, Genesis avril 2023, BreachForums multiple.
- **Exit scam** : admins disparaissent avec les fonds en escrow (Evolution Market 2015, Empire Market 2020 — ~30 M USD partis).
- **Épuisement opérationnel** : les admins se retirent, souvent en transférant l'infrastructure à un successeur.
- **Guerre interne** : conflit entre opérateurs qui fracture la communauté.
- **Désertion** : la communauté migre vers un concurrent plus attractif.

**Phase 5 — Reconstitution**. Après la disparition d'un forum, la communauté se reconstitue ailleurs. Des successeurs émergent, parfois avec d'anciens admins. RaidForums → BreachForums → BreachForums v2 → ... illustre cette dynamique de reconstitution cyclique.

Pour l'investigateur, le cycle implique : **un forum étudié aujourd'hui n'existera peut-être plus dans 6 mois**. La documentation et la capture préservent la trace ; l'expertise historique (qui était sur quel forum) est un actif d'investigation durable même quand les forums disparaissent.

#### 10.7 Fil rouge — DARKSTREAM : lecture d'IndustrialLeaks

> **🌐 DARKSTREAM — Épisode 6 : exploration initiale**
>
> Après accès validé par vouching (Athéna a un membre partenaire dans un forum affilié qui a accepté de vouch une persona d'investigation, sous encadrement DGSI), Lucas explore IndustrialLeaks.
>
> **Structure du forum** : 8 zones publiques + 3 zones premium. Les zones publiques couvrent annonces, ventes générales de données, recherche de partenaires, discussions techniques. Les zones premium (accessibles après paiement additionnel) couvrent « industrial espionage », « government access », « supply chain intrusion ».
>
> **Activité récente** : ~30-40 nouveaux posts par semaine en zone publique, ~10 en zones premium. Rythme soutenu, pas un forum mort.
>
> **Le post aero_source** : posté il y a 11 jours dans la zone « Data sales ». Titre : « EU aerospace supplier, 420GB, propulsion R&D, defense programs inside ». Corps du post : brève description, liste d'échantillons disponibles (5 fichiers), prix 65 000 USDT. Méthode de contact : XMPP (aero_source@xmpp.jp — serveur non-custodial classique).
>
> **Profil aero_source** : compte créé il y a **8 mois**. 12 posts au total. 2 transactions confirmées précédemment (petits dumps, 5 000-15 000 USD). Pas de vouching publicly affiché. Pas de rating négatif.
>
> Lucas note : profil **intermédiaire** — pas un scammer opportuniste (historique transactionnel), pas un vétéran majeur. Possiblement un acteur qui a gradé de petites ventes à un dump plus gros. Possiblement aussi un proxy pour un acteur plus sophistiqué qui ne veut pas utiliser son propre pseudo.
>
> La première tâche est maintenant de **demander un échantillon** (via XMPP, avec une persona crédible). Avant cela, Lucas va continuer à cartographier : activités aero_source sur d'autres forums (Ch.26 pivoting), monitoring des posts d'aujourd'hui, observation du comportement conversationnel en zone commune.

---

### Chapitre 11 — Marchés du dark web : histoire, fonctionnement, évolution

Les **marchés** (marketplaces) sont les plateformes d'e-commerce clandestin — la couche la plus visible et la plus médiatisée du dark web. Après Silk Road, plusieurs dizaines ont existé et disparu.

#### 11.1 Anatomie d'un marché

Un marché dark web typique présente une interface familière. Comparable à Amazon ou eBay dans son ergonomie, avec des différences structurantes.

**Catégories de produits** :
- Drogues (cannabis, cocaïne, MDMA, amphétamines, opioïdes, psychédéliques) — catégorie historique dominante.
- Digital goods : comptes, credentials, accès, exploits, malware, guides.
- Documents : faux permis, faux passeports, modèles de factures, templates.
- Services : hacking sur commande, DDoS, escrow, physical services (rares).
- Armes : présent sur certains marchés mais marginalement, majoritairement scam.
- Fraude : carding tools, dumps, fullz.

**Fonctionnalités** :
- Listings avec photos, descriptions, stock, prix (souvent en multiple devises crypto).
- Système de panier et checkout.
- **Escrow** : les fonds sont retenus par le marché jusqu'à confirmation de la livraison.
- **Dispute resolution** : mécanisme d'arbitrage en cas de litige.
- **Ratings et reviews** : feedback post-transaction, souvent visible publiquement.
- **Messagerie interne** : communication chiffrée entre acheteur et vendeur, souvent avec option PGP.
- **2FA et PGP** : obligatoires sur les marchés sérieux pour les comptes vendeur.

**Accès** :
- Adresse .onion communiquée via listes communautaires, Reddit (historiquement DarkNetMarkets avant son shutdown en 2018, multiple successeurs), forums affiliés.
- Inscription : email jetable, choix de pseudonyme, création d'un compte. Certains exigent un mnemonic seed pour récupération de compte (pas de « mot de passe oublié » classique).
- Authentification : login + password + 2FA PIN + parfois PGP challenge.

#### 11.2 Les grands marchés historiques et actuels

Les marchés majeurs observés historiquement et 2024-2026.

**Silk Road (2011-2013)** — pionnier, traité Ch.2.

**Silk Road 2.0 (2013-2014)** — successeur immédiat, saisi lors d'operation Onymous.

**Evolution Market (2014-2015)** — grand marché de son époque, exit scam retentissant en mars 2015.

**Agora (2013-2015)** — longévité notable pour son époque, fermeture volontaire par ses opérateurs (rare).

**AlphaBay (2014-2017)** — plus grand marché de l'histoire au moment de sa saisie (Ch.2).

**Hansa (2013-2017)** — « capté » par la police néerlandaise pendant 30 jours après la saisie d'AlphaBay.

**Dream Market (2013-2019)** — très longue durée de vie, fermeture volontaire des opérateurs en avril 2019 (rumeurs de menaces law enforcement).

**Wall Street Market (2016-2019)** — exit scam en 2019 suivi d'arrestations allemandes.

**Empire Market (2018-2020)** — exit scam en août 2020, ~30 M USD partis.

**Hydra (2015-2022)** — dominant russophone, traité Ch.2.

**Monopoly Market, Versus, Tor2Door, Dark0de, ASAP Market** — générations 2020-2023, disparitions variées.

**Marchés actuels 2025-2026** (mentions publiques, listes susceptibles d'évolution rapide) :
- **Abacus Market** : marché généraliste anglophone, actif depuis ~2022.
- **TorZon** : anglophone, en croissance 2023-2024.
- **MGM Grand / MGM Gold Market** : anglophone.
- **BlackSprut, OMG!OMG!, Mega, Kraken Market** : marchés russophones post-Hydra.
- **DarkDock, Vice City, Incognito** : statuts variables.

#### 11.3 Le modèle économique d'un marché

**Revenue** :
- **Commissions** sur les transactions : typiquement 2-5%, parfois jusqu'à 10%. Prélevé automatiquement via l'escrow.
- **Fees vendor** : droit d'inscription vendeur (100-1 000 USD), fees mensuels pour les slots, promotion payante.
- **Fees acheteur** : certains marchés demandent un dépôt minimum pour ouvrir un compte.
- **Advertising** : bannières, placements en haut des catégories.

**Coûts** :
- **Hosting** : bulletproof coûteux (5 000-30 000 USD/mois selon scale).
- **Développement** : équipe interne ou sous-traitants.
- **Modération** : staff pour surveiller les scammers, gérer les disputes.
- **Sécurité** : audits, monitoring, réponse aux attaques (DDoS).
- **Marketing** : présence sur forums, canaux Telegram, Reddit.

Un grand marché génère plusieurs millions à plusieurs dizaines de millions USD par an. Le ratio commission × volume transactionnel × année définit l'envergure. Hydra à son apogée : estimations 5-10% du volume crypto transactionnel mondial lié aux darknet markets.

#### 11.4 La dynamique de l'exit scam

L'**exit scam** — les opérateurs disparaissent avec les fonds en escrow — est une fin récurrente pour les marchés. Mécanisme typique :

**Phase 1 — Build-up**. Les opérateurs construisent la confiance et font croître le volume d'escrow. Plus le volume est haut, plus la « prime de départ » est attrayante.

**Phase 2 — Signals**. Dégradation de la qualité — support moins réactif, disputes mal résolues, retards de déblocage. Certains vendeurs commencent à s'alarmer sur les forums.

**Phase 3 — Retention**. Les opérateurs ralentissent les withdrawals — imposent des délais accrus, des vérifications supplémentaires. Les fonds s'accumulent.

**Phase 4 — Disappearance**. Le marché devient inaccessible. L'adresse .onion ne répond plus. Les opérateurs ont transféré les fonds et disparu.

**Phase 5 — Succession**. Parfois, des « rescue » se proposent de racheter la base de données pour relancer le marché sous une nouvelle marque. Rarement efficace — la confiance est cassée.

Exit scams majeurs historiques : Evolution (~12 M USD, 2015), Empire (~30 M USD, 2020), multiples plus petits. La probabilité d'exit scam augmente quand : le marché grandit, les forces de l'ordre mettent la pression, les opérateurs vieillissent. Pour les acheteurs avertis, la règle est de **ne pas laisser plus que nécessaire sur le marché** — transactions rapides, pas de gros stock de crypto chez le marché.

#### 11.5 Les marchés spécialisés 2024-2026

L'époque des grands marchés généralistes AlphaBay décline au profit de marchés **spécialisés**.

**Marchés de logs** : Russian Market est le leader actuel. Spécialisation totale sur les stealer logs (Ch.15). Interface orientée recherche par domaine. Croissance massive depuis 2023.

**Marchés de fraude** : vente de cartes bancaires, comptes bancaires compromis, accès PayPal/Venmo, fullz. Brians Club, WWH Club, Joker's Stash historique (saisi en 2021).

**Marchés de SaaS criminel** : RaaS (Ransomware-as-a-Service), Phishing-as-a-Service, DDoS-as-a-Service. Interface orientée services avec abonnements.

**Marchés d'accès** : Initial Access Brokers opèrent sur leurs propres plateformes ou via forums. Structure différente d'un marché classique — annonces plutôt que catalogue, négociation plutôt que prix fixe.

**Marchés de malware** : vente de malware spécifique, crypters, loaders. Souvent intégrés dans les forums plutôt que comme marchés séparés.

Cette spécialisation reflète la **professionnalisation** de la cybercriminalité : chaque segment a ses acteurs, ses codes, ses mécanismes de confiance.

#### 11.6 Investigation sur un marché : ce qu'on peut observer

Pour un analyste CTI, un marché offre plusieurs types d'observations utiles.

**Pricing intelligence** : prix observés sur les marchés donnent une grille utile pour évaluer les signals (Ch.14 sur les prix des données, Ch.15 pour les stealer logs).

**Vendor profiling** : histoire d'un vendeur (ancienneté, nombre de transactions, ratings, spécialisations). Les profils anciens avec beaucoup de transactions sont des acteurs établis — leurs annonces sont plus susceptibles d'être authentiques.

**Victim signaling** : annonces qui mentionnent des cibles nommées (entreprises, secteurs, géographies) donnent des signaux pour le monitoring défensif.

**Trends** : évolution du volume de certains types de produits (par exemple, hausse des ventes de credentials cloud AWS depuis 2022 est un signal industry-wide).

**Indicators** : adresses crypto observées comme paiements, pseudonymes observés comme vendeurs ou acheteurs, infrastructures mentionnées.

Les **limites** : tout ce qui est sur un marché n'est pas authentique. Scams, recyclages, agit-prop — l'analyste doit rester critique (Ch.32 sur les pièges analytiques).

---

### Chapitre 12 — Leak sites ransomware et vitrines de revendication

Les **leak sites** sont les vitrines publiques des groupes ransomware. C'est là que les groupes revendiquent les victimes, publient des échantillons de données volées, et menacent de publier l'intégralité si la rançon n'est pas payée. Depuis l'avènement du modèle « double extorsion » (chiffrement + menace de publication), les leak sites sont devenus un des objets d'investigation CTI les plus riches.

#### 12.1 Le modèle de la double extorsion

Historiquement, un ransomware chiffrait les données et demandait une rançon pour la clé de déchiffrement. La victime avait deux options : payer, ou restaurer depuis des backups. Si les backups existaient et étaient intacts, la victime pouvait refuser de payer.

Le modèle **double extorsion** (popularisé par Maze en 2019-2020) ajoute une couche. L'attaquant **exfiltre les données avant de les chiffrer**, puis menace de les publier publiquement si la rançon n'est pas payée — même si la victime a des backups et peut restaurer. L'intérêt criminel : augmente la pression (risque réputationnel, légal, contractuel de la publication), élargit le levier (même les victimes avec backups sont touchées).

Le **leak site** est l'outil de cette menace. Plateforme publique où le groupe :
- **Revendique** la victime : nom, secteur, pays.
- **Publie des échantillons** de données volées (documents sensibles, financiers, RH).
- **Affiche un countdown** jusqu'à publication intégrale.
- **Publie intégralement** si non-paiement.

L'effet psychologique est considérable. Une victime qui voit son nom publié sur un leak site majeur est dans une position extrêmement inconfortable — ses clients, partenaires, journalistes, autorités voient le post. La pression au paiement est forte.

#### 12.2 Anatomie d'un post de leak site

Un post typique de leak site contient :

- **Nom de la victime** : raison sociale, parfois logo.
- **Secteur d'activité** : aerospace, healthcare, manufacturing, etc.
- **Pays / région** : juridiction.
- **Taille** : chiffre d'affaires approximatif, nombre d'employés.
- **Description** : quelques paragraphes sur ce que le groupe a exfiltré, type de données, volumétrie.
- **Countdown** : temps restant avant publication intégrale (typiquement 1-4 semaines).
- **Échantillons** : 10-100 fichiers publiés comme preuve de compromission. Choisis pour maximiser l'impact réputationnel (docs financiers, contrats, emails de dirigeants, données RH).
- **Contact** : méthode pour initier la négociation (souvent un onion avec un chat ou un formulaire).

Certains leak sites permettent des **interactions** : vote de la communauté pour pousser à la publication, mise en vente des données à la pièce, achats « first-come first-served » pour les autres criminels intéressés.

#### 12.3 Les principaux groupes et leurs leak sites en 2024-2026

*Liste non exhaustive et évolutive — plusieurs de ces groupes disparaissent ou rebrandent.*

**LockBit** — historiquement le plus prolifique. Leak site très actif, interface sombre, countdown flashy. **Operation Cronos (février 2024)** a saisi l'infrastructure, identifié Dmitry Khoroshev comme LockBitSupp, rendu publiques des clés de déchiffrement. LockBit a tenté un relaunch mais sa crédibilité est entamée.

**ALPHV / BlackCat** — malware sophistiqué écrit en Rust. Disparition en mars 2024 suite à ce qui semble être un exit scam post-paiement Change Healthcare (~22 M USD présumés).

**Cl0p** — spécialisé dans l'exploitation de vulnérabilités d'edge devices (MOVEit 2023, Fortra GoAnywhere, Oracle EBS 2025). Leak site moins visuel que LockBit mais attaques techniquement sophistiquées.

**Black Basta** — actif depuis 2022, ciblage enterprise. Leak data massives en 2024-2025.

**Play / PlayCrypt** — actif depuis 2022, ciblage varié.

**Akira** — émergent fin 2023, croissance rapide.

**RansomHub** — émergent mi-2024, semble absorber des affiliés d'ALPHV post-disparition.

**Qilin** — anglophone malgré son nom, actif.

**Medusa** — à ne pas confondre avec autres entités nommées Medusa.

**BianLian** — historiquement hybrid chiffrement + exfiltration, en 2023 s'est tourné vers extorsion seule (sans chiffrement).

**8Base, Hunters International, Inc Ransom, Dragonforce** — autres groupes actifs à surveiller.

La scène change **mensuellement** — des groupes disparaissent, rebrandent, émergent. Les outils de monitoring (Ransomfeed, Ransomwatch) suivent ces évolutions en temps réel.

#### 12.4 La lecture analytique d'un leak site

Pour un analyste CTI, chaque revendication de leak site est une source de renseignement.

**Vérification de la compromission réelle**. Tous les posts ne correspondent pas à de vraies victimes.
- **True positives** : la victime confirme (rarement publiquement, souvent via comms privées).
- **False claims** : groupe re-publie des données d'un breach antérieur sous son nom (pattern récurrent), ou revendique une compromission inexistante pour gonfler sa réputation.
- **Doubles claims** : la même victime revendiquée par deux groupes (conflit d'affiliés, rachat d'accès).

**Signaux sur l'activité du groupe**. Volume de revendications par mois, secteurs ciblés, géographies, évolution du rythme. Un groupe qui passe de 5 à 50 revendications/mois signale une croissance significative ou un recrutement d'affiliés.

**Patterns de targeting**. Les secteurs / pays ciblés donnent des indications sur les priorités et les compétences du groupe. Un groupe avec beaucoup de santé US est différent d'un groupe avec beaucoup de manufacturing EU.

**TTP implicites**. Les leak sites ne publient pas les TTPs (pour protéger leurs accès), mais des patterns peuvent se déduire — affinité pour certaines tailles de victimes, certains vecteurs d'entrée inférables par crosscheck avec cas connus.

**Indicateurs de disruption**. Un leak site qui disparaît brutalement, dont le countdown se fige, dont les affiliés migrent vers un concurrent — signaux d'une operation law enforcement en cours ou d'un conflit interne.

#### 12.5 Le monitoring automatisé

**Ransomfeed.it** (site public, gratuit) agrège les revendications de dizaines de leak sites en temps réel. Outils open source type **Ransomwatch** fournissent des archives.

**Vendors CTI** (Recorded Future, Mandiant, CrowdStrike, Flashpoint, SOCRadar, Flare) intègrent le monitoring dans leurs plateformes avec alerting sur marques, secteurs, géographies.

**Limites** :
- Les leak sites modernes implémentent des protections anti-scraping (CAPTCHA, rate limiting, proof-of-work).
- Certains groupes ont des leak sites « tiered » avec une partie publique et une partie accessible uniquement après interaction (contact du groupe).
- Les échantillons publiés ne sont pas toujours téléchargés / analysés — le contenu brut des leaks reste difficile d'accès.

#### 12.6 Le paiement de rançon : angle d'investigation

Les paiements de rançon, quand ils surviennent, laissent des traces **on-chain** exploitables.

**Mécanisme** : le groupe fournit une adresse Bitcoin / Monero / autre dans un portail de négociation. La victime paie. Les fonds transitent vers le groupe, puis sont blanchis (mixers, Monero swaps, OTC).

**Pour l'investigation** :
- Si l'adresse est connue, le paiement confirme une compromission.
- Les mouvements on-chain peuvent révéler des connexions à d'autres opérations du même groupe.
- Les tentatives d'off-ramp peuvent révéler des identités si passage par exchange KYC.

**Saisies de paiements** : le FBI a récupéré des portions de rançons dans plusieurs cas emblématiques — Colonial Pipeline (~2,3 M USD récupérés en juin 2021), autres cas plus récents. Nécessite coopération internationale et vitesse d'exécution (avant blanchiment complet).

**Sanctions OFAC** : payer un groupe sanctionné (certains groupes sont sur listes OFAC) peut exposer l'organisation payeuse à des sanctions américaines. Considération réglementaire importante, qui pèse dans les décisions de paiement.

#### 12.7 Le débat sur le paiement

Question récurrente : faut-il payer une rançon ? Débat complexe.

**Arguments contre le paiement** :
- Finance l'activité criminelle.
- Ne garantit pas la non-publication (plusieurs cas de groupes publiant après paiement).
- Ne garantit pas l'intégrité des données exfiltrées.
- Crée un précédent — une organisation qui paie devient cible récurrente.
- Expose à sanctions (groupes OFAC).

**Arguments pour le paiement** :
- Urgence opérationnelle (vie humaine en cause dans certains cas — hôpitaux).
- Coût moindre que la perte business prolongée.
- Clé de déchiffrement peut accélérer la reprise.

**Positions officielles** : la plupart des agences nationales (FBI, ANSSI, NCSC) recommandent de **ne pas payer** comme principe, tout en acceptant pragmatiquement que la décision incombe à la victime.

**Les faits statistiques** (rapports Coveware, Chainalysis) : la proportion de victimes qui paient a **baissé** sur la décennie (de ~70% en 2018-2019 à ~25-30% en 2024). Le paiement moyen a augmenté (quelques millions de dollars par cas en moyenne sur les grandes victimes). La dynamique a changé : moins de payeurs, payeurs plus gros.

---

### Chapitre 13 — Canaux, chats et messageries clandestines

Les **messageries et canaux** sont la couche temps réel du dark web. Là où forums et marchés sont persistants, les messageries sont éphémères — ce qui leur confère à la fois un intérêt opérationnel (communication rapide, pas de traces longues) et un défi investigatif (capturer les flux avant qu'ils disparaissent).

#### 13.1 Les plateformes dominantes

**Telegram**. Dominant dans la cybercriminalité 2020-2024. Facilité d'usage, canaux publics avec des milliers d'abonnés, canaux privés invitation-only, groupes de discussion, bots. Historiquement perçu comme plus tolérant que les alternatives — politique de modération limitée.

**Impact de l'arrestation de Pavel Durov (août 2024)**. Suite à l'interpellation en France, Telegram a durci significativement sa modération — suppression massive de canaux criminels, coopération accrue avec les autorités sur les requêtes légales. Résultat : **migration partielle** de certains acteurs vers d'autres plateformes (Session, Matrix sur Tor, XMPP, retour aux forums .onion), mais Telegram reste dominant en volume absolu.

**XMPP (Jabber)**. Historiquement central dans la cybercriminalité russophone. Chaque utilisateur un JID (jabber ID) type `username@domain.com`. Chiffrement de bout en bout via OMEMO ou OTR. Serveurs non-custodial (l'admin du serveur ne peut pas lire les messages chiffrés). Résilient — si un serveur tombe, l'utilisateur peut migrer en changeant de JID. Usage encore courant chez les acteurs sérieux.

**TOX**. Protocole peer-to-peer chiffré de bout en bout. Pas de serveur central, pas de registrations. Moins populaire que XMPP mais utilisé pour communications très sensibles.

**Matrix (+ Element)**. Protocole fédéré, chiffrement E2E, parfois opéré sur Tor via onion routing des homeservers. Adoption lente dans la cybercriminalité mais croissante post-Durov.

**Session**. Messagerie basée sur Oxen/Lokinet, conçue pour anonymat. Pas de numéro de téléphone requis (contrairement à Signal, WhatsApp), pas de metadata centrale. Usage croissant chez acteurs paranoïaques.

**Signal**. Messagerie chiffrée grand public. **Moins utilisée** par cybercriminalité sophistiquée car : requiert numéro de téléphone, metadata potentiellement saisissables via Twilio (fournisseur de Signal), cible fréquente de requêtes légales. Utilisée par activistes et journalistes plutôt que cybercrime organisé.

**IRC historique**. Usage résiduel pour certaines communautés de niche. Remplacé par les alternatives modernes.

**Discord**. Usage modeste en cybercrime sérieux (modération forte, liens avec identités réelles fréquents), mais présent pour les marchés jeunes/gaming.

#### 13.2 Les canaux Telegram cybercriminels

Les canaux Telegram publics cybercriminels peuvent être classés :

**Canaux de leak** : publient des leaks gratuits (combo lists, databases publiées), souvent comme teasers pour des services payants. Des centaines de canaux de ce type, cumul de millions d'abonnés.

**Canaux de CaaS** : services-as-a-service — phishing kits, DDoS, logs access. Interface commerciale, avec prix et méthodes de paiement.

**Canaux de coordination** : groupes privés pour coordination opérationnelle entre membres d'une campagne. Typiquement invite-only.

**Canaux d'hacktivisme** : canaux revendiquant des attaques, publiant des données volées dans un contexte idéologique (pro-russe, anti-israélien, etc.).

**Canaux d'influence** : désinformation, amplification de narratifs, coordination d'opérations informationnelles.

#### 13.3 L'investigation des messageries

Plusieurs angles d'investigation spécifiques aux messageries.

**Capture de canaux publics**. Telegram notamment permet d'archiver les messages de canaux publics avec des outils comme Telethon (bibliothèque Python). Les canaux privés nécessitent une invitation — soit obtenue légitimement via un contact, soit impossible à obtenir.

**Métadonnées**. Même les messageries chiffrées laissent des métadonnées (qui a parlé à qui, quand, volume). Sur Telegram, les numéros de téléphone des membres de groupes peuvent parfois être extraits selon les paramètres de confidentialité.

**Corrélation avec pseudonymes**. Un pseudonyme sur un forum .onion peut avoir un handle Telegram affiché dans les posts. Suivre ce handle sur Telegram permet d'élargir la collecte.

**Identification par patterns**. Analyse stylométrique (Ch.29), timing d'activité, patterns de langue — permettent parfois de corréler des comptes supposés distincts.

**Actions légales**. Les autorités peuvent, dans certaines juridictions, exiger la coopération des plateformes. Telegram post-Durov coopère plus activement avec les requêtes légales.

#### 13.4 Les limites investigatives

Les messageries sont plus difficiles à investiguer que les forums pour plusieurs raisons.

**Éphémérité**. Messages supprimés, canaux fermés, comptes bannis — la trace est vite perdue. Un analyste qui ne capture pas en temps réel perd l'information.

**Chiffrement**. Les messages chiffrés de bout en bout ne sont accessibles qu'aux participants — ni le serveur, ni les investigateurs ne peuvent les lire sans compromettre un endpoint.

**Volatilité des plateformes**. Un canal peut déménager ou disparaître du jour au lendemain. Maintenir le tracking nécessite de l'automatisation et de la réactivité.

**Faux comptes et sybil**. Les plateformes ouvertes permettent la création massive de faux comptes pour simuler l'activité, booster des narratifs, ou confondre les investigations.

#### 13.5 L'usage des messageries dans DARKSTREAM

> **🌐 DARKSTREAM — Épisode 7 : XMPP avec aero_source**
>
> Lucas contacte aero_source via son XMPP affiché : `aero_source@xmpp.jp`. Serveur classique, non-custodial, fréquent dans la cybercriminalité russophone. Session chiffrée OTR négociée.
>
> Premier message de Lucas (persona « mapletech », se présente comme acheteur potentiel d'une entreprise tech intéressée par des specs aéronautiques — légende crédible côté profil Athéna) : demande d'échantillons supplémentaires, vérification du volume réel, méthode de paiement préférée.
>
> aero_source répond en 6 heures (cohérent avec un opérateur à temps plein sur fuseau horaire moscovite). Fournit 3 fichiers sample additionnels (1 spec technique de propulsion, 1 liste de fournisseurs, 1 extrait de notes de design). Confirme 420 Go total, paiement XMR préféré mais BTC accepté.
>
> Lucas note : style de langue russophone anglicisé (« I have all the data, you see ? ») — cohérent avec profil russophone. Fuseau horaire des réponses (toutes entre 08:00 et 22:00 MSK) conforte. Pas de fautes de tournure inhabituelles — acteur probablement expérimenté, pas un débutant.
>
> L'échantillon reçu sera analysé (Ch.25 — authentification). En parallèle, Lucas documente les métadonnées de la session : timestamps exacts, clé OTR négociée, serveur. Ces éléments pourront servir au rapport et au cross-matching avec d'autres pseudonymes.

---

### Chapitre 14 — Données volées et marchés de la fuite

Les données volées sont l'un des produits les plus échangés sur le dark web. Credentials, identités, dossiers médicaux, données d'entreprise — chaque type a son marché, son prix, ses acheteurs.

#### 14.1 Types de données en circulation

**Credentials**. Couples email/mot de passe issus de breaches. Vendus en bulk (combo lists de millions d'entrées pour 5-50 USD) ou au détail (5-50 USD/pièce pour des credentials vérifiés sur services spécifiques).

**Logs d'infostealers**. Sessions complètes avec credentials, cookies, données machine — traités au Ch.15 en détail.

**Données bancaires**. Numéros de carte, CVV, accès aux comptes. Marché organisé (BriansClub, WWH Club, successeurs). Prix selon fraîcheur et pays.

**Données personnelles (fullz)**. Identité complète : nom, adresse, SSN/NIR, date de naissance, documents d'identité scannés. Utilisées pour fraude à l'identité, ouverture de comptes frauduleux.

**Données d'entreprise**. Documents internes, propriété intellectuelle, emails, bases clients. Les volumes exfiltrés par ransomware alimentent cette catégorie.

**Données de santé**. Dossiers médicaux, très prisés pour la fraude à l'assurance (US), le chantage, et la fraude à l'identité. Prix relativement élevés par unité (50-250 USD/dossier).

**Données gouvernementales**. Accès ou exfiltrations concernant administrations. Rareté élevée, prix variables selon sensibilité.

**Données industrielles / défense**. Spécifications techniques, plans, documents classifiés. Niche — DARKSTREAM s'inscrit dans cette catégorie. Acheteurs : concurrents industriels, services de renseignement étrangers, parfois groupes ransomware cherchant un levier de revente.

#### 14.2 Grille de prix indicative 2025-2026

Sources : rapports SOCRadar (Annual Dark Web Report 2025), Privacy Affairs (Dark Web Price Index), observations Recorded Future, Flare. **Fortement indicatif** — varie par fraîcheur, spécificité, vendeur, marché.

| Type de donnée | Prix indicatif |
|---|---|
| Combo list (millions d'entrées, dates variables) | 5-50 USD |
| Credentials vérifiés, service spécifique | 5-50 USD / pièce |
| Carte bancaire avec CVV (compte actif) | 5-30 USD |
| Carte bancaire avec PIN / full access | 30-150 USD |
| Compte PayPal vérifié | 20-200 USD selon balance |
| Compte bancaire vérifié avec online banking | 100-1 000 USD selon balance |
| Fullz (identité complète) | 10-70 USD |
| Passeport scanné | 20-150 USD |
| Permis de conduire scanné | 15-70 USD |
| Log d'infostealer basique | 1-15 USD |
| Log d'infostealer avec VPN corporate | 50-500 USD |
| Accès VPN/RDP corporate (IAB) | 500-50 000 USD |
| Base de données d'entreprise | 500-100 000 USD+ |
| Dossier médical US | 50-250 USD |
| 0-day exploit (selon plateforme) | 5 000 - 2 500 000 USD |
| RaaS affiliation (droit d'affiliation) | 1 000 - 100 000 USD |

> **⚠️ ALERTE ANALYSTE** : Ces prix sont des moyennes indicatives à date (2025-2026) et fluctuent selon la réputation du vendeur, la fraîcheur, la verification, et les dynamiques de marché. Les prix des données bancaires simples ont tendance à se stabiliser ou baisser (saturation) tandis que les credentials d'accès corporate et les stealer logs avec tokens de session augmentent (demande RaaS).

#### 14.3 Le lifecycle d'un breach

Les données volées suivent un cycle prévisible.

**Phase 1 — Exploitation privée**. Le groupe auteur du breach exploite d'abord les données pour son propre compte — ransomware, fraude, chantage de la victime. Durée : jours à mois.

**Phase 2 — Vente exclusive**. Les données sont mises en vente à prix élevé, avec clause d'exclusivité (pas de revente par le vendeur). Acheteurs : autres groupes cybercriminels cherchant un levier, concurrents industriels (rare et risqué), services de renseignement (cas politiques).

**Phase 3 — Revente large**. Si les données ne sont pas exclusivement vendues, ou si les termes d'exclusivité sont violés, revente à multiple acheteurs avec prix décroissant.

**Phase 4 — Publication publique / gratuite**. Après que la valeur commerciale a été extraite, les données sont souvent publiées gratuitement sur des canaux Telegram, pastebins, forums. Sert à construire la réputation d'un vendeur ou à publier sous couvert idéologique.

**Phase 5 — Intégration dans les bases publiques**. Have I Been Pwned, DeHashed, et autres services indexent les données pour vérification défensive. Les données deviennent **un asset défensif** — les DSI peuvent vérifier si leurs emails sont compromis.

La durée entre phase 1 et phase 5 varie considérablement — quelques semaines pour des petits breaches de moindre intérêt, plusieurs années pour des breaches majeurs gardés exclusifs longtemps.

#### 14.4 Vérification de l'authenticité

Les annonces de données volées sont **massivement polluées par des scams, des recyclages, et des fabrications**. La vérification d'authenticité est un skill central de l'analyste.

**Échantillons**. Un vendeur sérieux fournit des échantillons gratuits vérifiables — emails avec domaine cohérent, formats réalistes. Un vendeur refusant systématiquement tout échantillon est suspect.

**Fraîcheur**. Les données déjà vues dans des breaches publics (via HIBP, DeHashed) sont recyclées — pas un nouveau breach, valeur réduite.

**Spécificité**. Des données très spécifiques à une organisation (noms d'employés internes, codes produit internes, contrats signés) sont plus crédibles que des templates génériques.

**Corroboration externe**. La victime confirme-t-elle ? Un CERT ou prestataire IR est-il impliqué ? Des indices publics confirment-ils la compromission (notifications régulateurs, communiqué de presse) ?

**Cohérence interne**. Les formats, conventions, horodatages sont-ils cohérents ? Une base de données avec des inconsistances format (dates parfois US, parfois EU) signale potentiellement un assemblage factice.

**Échantillon ciblé**. Demander au vendeur un échantillon spécifique (par exemple, un fichier contenant un certain nom). S'il peut le produire, authenticité probable. S'il refuse ou produit quelque chose d'incohérent, probable scam.

Voir Annexe E pour une grille d'évaluation complète de crédibilité.

#### 14.5 La dimension sectorielle

Les données volées ne sont pas distribuées uniformément. Rapport Cyberint 2025 documente une concentration sur les secteurs à forte valeur : institutions financières (cartes, credentials bancaires, accès systèmes de trading), santé (dossiers médicaux, chantage, fraude assurance), télécommunications (SIM swapping, accès réseaux), gouvernement (données classifiées, identités fonctionnaires). Chaque secteur a son **modèle de monétisation** propre — détaillé au Ch.35.

#### 14.6 Fil rouge — DARKSTREAM : premiers échantillons

> **🌐 DARKSTREAM — Épisode 8 : analyse des échantillons**
>
> Lucas reçoit 5 fichiers d'échantillons initiaux + 3 additionnels via XMPP. Protocole Athéna strict : fichiers ouverts **uniquement** dans une VM isolée (Whonix + Windows 10 jetable), jamais sur la machine de production. Scan antivirus préalable. Extraction des métadonnées avec exiftool.
>
> **Fichier 1** — « Propulsion_specs_Rev7.pdf ». 14 pages, schémas techniques. Métadonnées internes : auteur « M. Dubois », entreprise « Vectris Aerospace », créé en Nov 2025, modifié en Dec 2025. Softare MS Word → PDF. Numéro de révision cohérent avec conventions Vectris.
>
> **Fichier 2** — « Supplier_list_2025.xlsx ». 340 lignes de fournisseurs. Formatage Excel, adresses cohérentes (pays UE, US, Asie). Contient un fournisseur de test interne reconnu par le RSSI de Vectris (confidentiel — nom de fantaisie utilisé comme marker).
>
> **Fichier 3** — extrait email. Export de boîte mail interne d'un ingénieur R&D. Discussions techniques, jamais publiées publiquement. Content cohérent avec un vol Office 365.
>
> Les 3 échantillons additionnels : d'autres spécifications techniques, notes de réunion, extrait budgétaire.
>
> **Verdict Lucas** : authenticité **confirmée** au niveau échantillon. Cohérence avec la compromission initiale identifiée par Mandiant chez Vectris. Le marker interne présent dans le fichier 2 est un signe fort que le dump provient bien de la compromission Vectris. Lucas escalade immédiatement à la cellule de crise Vectris et à la DGSI. Le post aero_source est authentique ; la compromission est confirmée ; l'exfiltration circule bien sur le dark web.
>
> Question suivante : qui est aero_source ? Est-ce l'attaquant initial, un proxy, un courtier ? Prochaine étape : élargir le profiling via les autres activités du pseudonyme et via l'analyse des flux crypto associés.

---

### Chapitre 15 — Stealer logs : anatomie, marchés, investigation défensive

*Ce chapitre traite en profondeur le vecteur de compromission initiale le plus courant en 2025-2026. Les stealer logs sont devenus la matière première de l'écosystème cybercriminel — l'équivalent du pétrole brut qui alimente toute la chaîne de valeur.*

#### 15.1 Qu'est-ce qu'un stealer log ?

Un **stealer log** est le produit de l'exécution d'un **infostealer** (malware spécialisé dans le vol de données de sessions) sur la machine d'une victime. Contrairement à un breach de base de données (qui produit des listes de credentials en masse), un stealer log capture **l'intégralité de l'environnement de la session utilisateur** sur un poste spécifique.

Un log typique contient :
- **Credentials du navigateur** : tous les logins/mots de passe enregistrés dans Chrome, Firefox, Edge, Brave, Opera — des dizaines voire des centaines de comptes par victime.
- **Cookies de session actifs** : permettent de se connecter à un service **sans mot de passe**, en contournant même le MFA. C'est **le vecteur le plus dangereux** de 2024-2026.
- **Données d'autofill** : noms, adresses, téléphones, données de cartes bancaires stockées.
- **Wallets crypto** : clés privées ou seed phrases stockées dans des extensions navigateur (MetaMask, Phantom, Exodus).
- **Données machine** : hostname, IP, OS, logiciels installés, capture d'écran au moment de l'exécution.
- **Sessions de messagerie** : tokens Discord, Telegram Desktop, WhatsApp Desktop.
- **Données Steam, Epic Games** : sessions gaming, de plus en plus ciblées.
- **Fichiers sélectifs** : certains stealers exfiltrent des fichiers selon patterns (documents avec mots-clés, certains types de fichiers).

La **puissance destructrice** d'un stealer log tient à sa granularité : ce n'est pas un seul couple login/mot de passe — c'est **l'intégralité de l'identité numérique** d'un utilisateur, capturée à un instant T, sur un poste spécifique.

#### 15.2 Les infostealers dominants en 2025-2026

**Lumma Stealer** (aussi « LummaC2 »). Modèle d'abonnement, ~250 USD/mois. Extrêmement répandu. Évolution constante pour éviter la détection (polymorphic, updates hebdomadaires). En 2024-2025, dominant en volume.

**RedLine**. Historiquement dominant, toujours actif malgré tentatives de disruption. Développé par un acteur russophone. Large écosystème d'affiliés.

**Vidar** (dérivé d'Arkei). Populaire pour le ciblage de wallets crypto — modules spécifiques pour MetaMask, Coinbase Wallet, etc.

**Raccoon Stealer v2**. Relancé après l'arrestation de son opérateur initial en 2022.

**StealC**. Émergent, léger et polyvalent.

**RisePro**. Ciblage spécifique des applications crypto et des gestionnaires de mots de passe (LastPass, 1Password, Bitwarden).

**Meta Stealer, Phemedrone, DarkCrystal RAT** : autres familles documentées.

**Point d'entrée économique**. SOCRadar 2025 : **dès 15 USD en version de base**, avec modèles d'abonnement qui rendent les stealers accessibles à pratiquement n'importe quel acteur. Cette accessibilité explique leur adoption massive.

**Vecteurs de distribution** :
- **Malvertising** : publicités Google/Bing malveillantes redirigeant vers des téléchargements piégés. Technique en forte croissance 2024-2025.
- **Faux sites de téléchargement logiciels crackés**. Vecteur historique dominant — particulièrement efficace sur utilisateurs cherchant cracks.
- **YouTube tutorials malveillants** : descriptions de tutoriels contenant des liens vers des malwares sous couvert d'outils légitimes.
- **Pièces jointes email** : documents Office avec macros, archives protégées par mot de passe.
- **Packages npm/PyPI malveillants** : supply chain logicielle.
- **Telegram groupes** : liens de téléchargement douteux.

#### 15.3 Les marchés de stealer logs

**Russian Market**. Successeur de facto de Genesis Market (saisi avril 2023, Operation Cookie Monster). Plus grand marché de logs actif en 2025-2026. Logs vendus individuellement avec système de **recherche par domaine** — l'acheteur cherche des logs contenant des credentials pour un domaine spécifique (par exemple, un VPN d'entreprise cible). Prix : 1-15 USD pour log basique, 50-500 USD pour log avec accès corporate (VPN, Citrix, RDP).

**Genesis Market (historique, saisi 2023)** — modèle innovant qui mérite mention. Genesis ne vendait pas seulement des credentials, mais des **bots** — navigateurs virtuels répliquant l'empreinte exacte de la victime (fingerprint navigateur, cookies, résolution d'écran, timezone, liste des plugins). Permettait d'usurper la session sans déclencher les contrôles anti-fraude basés sur fingerprint. Modèle repris par d'autres marchés.

**Canaux Telegram**. De nombreux logs distribués en bulk via canaux spécialisés, souvent **gratuitement** (« free logs ») pour attirer vers des services premium. Canaux gratuits contiennent logs anciens ou faibles valeur, mais constituent point d'entrée pour acteurs peu sophistiqués.

**2easy.gg historique**. Marché spécialisé fermé, opérations law enforcement en 2024.

**StealC Marketplace, LummaC2 Shop** : marchés adossés à des familles de stealers spécifiques.

#### 15.4 Investigation défensive : workflow

Pour un analyste défensif surveillant l'exposition de son organisation.

**Étape 1 — Monitoring des domaines**. Configurer des alertes sur marchés de logs (via plateformes commerciales type Flare, Hudson Rock, SOCRadar, Breach.ai, Flashpoint) pour les domaines de l'organisation. Chaque nouveau log contenant des credentials du domaine déclenche une alerte.

**Étape 2 — Évaluation du log**. Pour chaque log détecté, évaluer la criticité :
- **Log avec credentials webmail uniquement** : préoccupant mais gérable (reset mot de passe + vérif MFA).
- **Log avec credentials VPN/Citrix + cookies de session actifs** : **urgence** — l'attaquant peut accéder au SI sans connaître le mot de passe actuel si le cookie est encore valide.
- **Log avec credentials cloud (Azure, AWS, GCP)** : critique — impact potentiellement majeur sur l'infrastructure.

**Étape 3 — Identification du poste source**. Les métadonnées du log (hostname, IP, OS, softwares installés) permettent souvent d'identifier le poste compromis. Ce poste est **potentiellement toujours infecté** par le stealer — **changer le mot de passe sans éradiquer le stealer ne fait que fournir un nouveau mot de passe à l'attaquant**. C'est l'erreur la plus fréquente et la plus dangereuse.

**Étape 4 — Remédiation**. Le poste source doit être **isolé et réimaginé**. Tous les credentials contenus dans le log doivent être réinitialisés — pas seulement les credentials corporate, mais aussi les comptes personnels qui pourraient servir de pivot (compte GitHub personnel avec accès à des repos de l'entreprise). **Sessions actives révoquées** (tokens, cookies invalidés).

**Étape 5 — Hunting**. Le SOC vérifie si les credentials du log ont été utilisés pour des connexions suspectes depuis la date estimée de compromission. Recherche dans logs d'authentification (VPN, AD, applications cloud) pour connexions depuis IPs inhabituelles, user agents inconnus, horaires atypiques.

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

Géographie : Inde domine (2,7M logs), Brésil (1,9M), Indonésie (1,3M), États-Unis (1,2M). La position basse des US suggère meilleure détection ou remédiation plus rapide plutôt que taux d'infection inférieur.

**Implications** : plateformes gaming (Roblox, Twitch, Epic Games — utilisateurs jeunes avec hygiène credentials faible) et e-commerce/streaming (Amazon, Netflix — données de paiement stockées) sont cibles privilégiées. PayPal se distingue comme facilitateur direct de fraude.

#### 15.6 Limites et faux positifs

**Expiration**. Les cookies expirent (typiquement 30-90 jours), les mots de passe peuvent avoir été changés, le poste peut avoir été réimaginé. Log ancien (6+ mois) a une probabilité d'exploitation réussie **beaucoup plus faible** qu'un log frais.

**Faux positifs**. Domaine similaire (typosquatting), employé utilisant email pro sur site grand public, log recyclé déjà traité. Filtrage humain indispensable.

**Bruit**. Un grand compte monitoring génère des dizaines d'alertes par jour — priorisation nécessaire (criticité, fraîcheur).

#### 15.7 Fil rouge — DARKSTREAM : les stealer logs Vectris

> **🌐 DARKSTREAM — Épisode 9 : découverte collatérale**
>
> En parallèle de son investigation sur aero_source, Lucas vérifie l'exposition Vectris sur les marchés de logs. Recherche sur Russian Market via l'accès monitoring Athéna : **12 logs** contenant des credentials du domaine `vectris-aerospace.eu`.
>
> Analyse des 12 logs :
> - 3 logs contiennent **credentials VPN (Fortinet FortiClient) avec cookies de session** — **urgence maximale**.
> - 4 logs avec credentials webmail Outlook 365.
> - 2 logs avec accès à une application SaaS RH.
> - 3 logs avec credentials divers (Jira, GitLab enterprise).
>
> Les 3 logs VPN datent de **2 à 4 mois** — compatible avec la timeline de la compromission Vectris. **Hypothèse** : l'attaquant initial aurait utilisé un infostealer comme vecteur d'accès, les logs ont ensuite été revendus sur Russian Market par un courtier (possiblement distinct de l'auteur de l'exfiltration finale), et aero_source est soit le même acteur, soit un acheteur final qui revend les données.
>
> Hostnames des 3 logs VPN :
> - VECTRIS-SALES-047 : laptop commercial.
> - VECTRIS-RD-112 : poste R&D — **celui-ci est particulièrement préoccupant**, potentiellement le vecteur de l'exfiltration initiale des 420 Go.
> - VECTRIS-IT-008 : poste IT.
>
> Lucas escalade immédiatement au RSSI Vectris. Mandiant (IR prestataire) confirme : VECTRIS-RD-112 est bien le poste central de la compromission, déjà identifié comme point d'entrée. Les deux autres sont des compromissions collatérales non identifiées jusqu'ici — actions immédiates enclenchées (isolement, forensics, reset massif).
>
> Découverte collatérale précieuse : la surveillance dark web a révélé **deux postes compromis supplémentaires** que l'investigation interne n'avait pas identifiés. Illustration concrète de la valeur défensive de la veille dark web.

---

### Chapitre 16 — Services criminels et profils d'acteurs

Au-delà des produits (données, credentials), le dark web est un marché de **services** — crime-as-a-service sous toutes ses formes. Ce chapitre cartographie les services majeurs et les profils d'acteurs.

#### 16.1 Les services majeurs

**Ransomware-as-a-Service (RaaS)**. Modèle dominant de l'écosystème ransomware. L'opérateur développe et maintient le malware + l'infrastructure (leak site, portail de négociation). Les **affiliés** déploient le ransomware chez des victimes, moyennant partage des gains (typiquement 70/30 affilié/opérateur, parfois 80/20). Ce modèle a industrialisé le ransomware : LockBit, ALPHV, Conti historique, Black Basta, Play, RansomHub actuels.

**Initial Access-as-a-Service (IAaaS)**. Les IAB compromettent et **vendent l'accès** préqualifié. Modèle spécialisé : l'IAB ne ransomware pas lui-même, il vend à un opérateur ransomware (ou autre acheteur) un accès déjà installé. Prix : 500-50 000 USD selon la cible (CA, secteur, niveau de privilèges). Délai de monétisation : plus rapide que développer une intrusion soi-même.

**Phishing-as-a-Service (PhaaS)**. Kits de phishing prêts à l'emploi, avec interface de gestion, templates, hosting. LabHost (démantelé avril 2024), EvilProxy, Evilginx (open source mais utilisé massivement). PhaaS a popularisé l'**AiTM** (Adversary-in-the-Middle) qui contourne le MFA en capturant cookies de session.

**Malware-as-a-Service (MaaS)**. Location de malware — infostealers (Lumma, RedLine mensuel), loaders, RAT, cryptominers.

**DDoS-as-a-Service**. Booters et stressers. De quelques dollars par attaque à plusieurs centaines pour attaques soutenues.

**Hosting bulletproof**. Infrastructure pour héberger contenu illicite (Ch.9).

**Cryptage / Obfuscation-as-a-Service**. Crypters et obfuscateurs pour rendre malware FUD. Service essentiel pour les opérateurs malware.

**Money laundering-as-a-Service**. Services de blanchiment crypto. Commissions 10-30% (Ch.21).

**Account checker / cracking services**. Vérification en masse de combo lists contre des services cibles (valider quels credentials marchent réellement).

**Spam / SMS bombing services**. Services commerciaux d'envoi massif.

#### 16.2 Profils d'acteurs typiques

**L'opérateur RaaS**. Figure centrale. Développe le malware, opère l'infrastructure, gère les affiliés, négocie les rançons. Équipe typique : 5-20 personnes. Revenu : plusieurs millions à dizaines de millions USD/an pour les groupes dominants. Exemple public : Dmitry Khoroshev / LockBitSupp (LockBit), autres en grande partie anonymes.

**L'affilié RaaS**. Exécutant opérationnel. Achète l'accès (via IAB ou compromet lui-même), déploie le ransomware, reçoit sa part des gains. Peut être indépendant ou partie d'une équipe. Skills : persistance, lateral movement, AD domination, parfois exfiltration. Turnover élevé — les affiliés changent de groupe selon conditions et opportunités.

**L'Initial Access Broker (IAB)**. Spécialisé dans la compromission initiale. Sources d'accès : exploitation d'edge devices (VPN, RDP exposés, vulnérabilités publiques), phishing, achat de logs, social engineering. Vend l'accès après qualification (confirmation des privilèges, cartographie minimale). Actifs connus : marées de posts sur XSS, Exploit, parfois accès de premier plan sur BreachForums.

**Le developer malware**. Écrit le code. Profil technique pur. Peut travailler pour un groupe, en freelance, ou vendre son malware comme produit. Certains devs sont très réputés dans l'écosystème pour des familles de malware spécifiques.

**Le courtier (broker) de données**. Collecte des données (achat, récupération de breaches publiés) et revend en les repackageant. Spécialisation par type (fullz, credentials bancaires, dossiers médicaux).

**Le money mule et le launderer**. Deux profils distincts. Le **mule** prête son compte bancaire ou son wallet crypto pour faire transiter des fonds — souvent recruté sous prétexte d'un emploi légitime, parfois consentant. Le **launderer** est professionnel, structure des opérations de blanchiment sophistiquées (multi-hop crypto, mixers, conversions off-chain).

**Le carder**. Spécialisé fraude cartes bancaires. Achète des dumps, les teste, les monétise (achats de biens revendables, cash advance, autres).

**Le script kiddie**. Amateur avec skills limités, utilise outils achetés. Majoritaire en nombre, minoritaire en impact. Dans les forums sérieux, traités avec condescendance.

**Le hacktiviste**. Motivation idéologique plus que financière. Opère souvent via canaux Telegram publics, moins sur forums .onion fermés. Anonymous historique, KillNet, Cyber Av3ngers, IT Army of Ukraine, etc. (Ch.38).

**L'agent étatique**. Opérateur qui utilise le dark web comme cover ou comme canal d'acquisition. APT29 a historiquement acheté des accès sur forums. La DPRK utilise le dark web pour vendre des données volées (Lazarus). Ces acteurs n'ont pas de « profil » simple — ils adaptent à chaque opération.

**L'analyste défensif / force de l'ordre / journaliste**. Observateur légitime (avec mandat). Se présente généralement comme lurker, parfois sous couverture avec persona active (Ch.22, Ch.23, Ch.30).

#### 16.3 La chaîne de valeur d'une compromission moderne

Comprendre les acteurs permet de reconstituer la chaîne typique d'une attaque enterprise 2024-2026.

**Étape 1 — Vol initial de credentials**. Un utilisateur télécharge un logiciel crack piégé, son poste personnel est infecté par un infostealer (Lumma), ses credentials (y compris son compte pro utilisé sur le poste perso) sont exfiltrés.

**Étape 2 — Vente en bulk**. L'opérateur de stealer vend les logs en lot sur Russian Market. Log basique : 15 USD.

**Étape 3 — Achat par IAB**. Un IAB achète des logs en volume, les trie pour identifier ceux avec accès corporate intéressants (VPN, Citrix, tokens cloud).

**Étape 4 — Qualification par IAB**. L'IAB utilise les credentials pour entrer dans le SI cible, vérifier les privilèges, cartographier l'environnement, identifier les cibles de valeur (DC, fileservers, backups).

**Étape 5 — Vente à affilié RaaS**. L'IAB poste l'accès sur un forum : « Access RDP + AD domain admin, EU manufacturing company, CA 500M USD, 2 000 endpoints, backup Veeam visible ». Prix : 25 000 USD.

**Étape 6 — Déploiement ransomware**. L'affilié achète l'accès, déploie le ransomware du groupe (Black Basta, par exemple). Exfiltre d'abord 800 Go de données sensibles (double extorsion), puis chiffre.

**Étape 7 — Négociation et rançon**. La victime est contactée via portail de négociation. Rançon demandée : 3 M USD. Négociation éventuelle. Paiement en Bitcoin.

**Étape 8 — Partage des gains**. Affilié reçoit 70% (2,1 M USD), opérateur RaaS 30% (0,9 M USD). Transferts crypto vers wallets opérationnels.

**Étape 9 — Blanchiment**. Les fonds passent par mixers, swaps Monero, exchanges non-KYC, OTC desks. Après 3-6 mois de chaînes, partie des fonds est convertie en fiat utilisable.

**Étape 10 — Publication partielle ou totale si non-paiement**. Si la victime ne paie pas, le groupe RaaS publie tout ou partie des données sur son leak site. Certaines données valorisables peuvent être revendues en parallèle.

Toute cette chaîne — de l'infection initiale au blanchiment — peut prendre **3 à 6 mois**. Chaque étape est opérée par un acteur spécialisé, avec ses skills et ses marchés. La cybercriminalité est une **industrie structurée**, pas une activité individuelle.

Pour le défenseur, chaque étape de cette chaîne est une **opportunité d'interruption** : détecter le stealer avant l'exfiltration, le log avant l'achat par IAB, l'accès IAB avant la vente, l'affilié avant le déploiement, l'exfiltration avant le chiffrement, la rançon avant le paiement. Plus la détection est précoce, plus l'impact est limité.

#### 16.4 Fil rouge — DARKSTREAM : la chaîne reconstituée

> **🌐 DARKSTREAM — Épisode 10 : cartographie de la chaîne**
>
> Au terme de 2 semaines d'investigation, Lucas reconstitue la chaîne probable de compromission Vectris.
>
> **Étape 1** — Infection initiale : un ingénieur R&D (VECTRIS-RD-112) a téléchargé un outil CAD crackéé depuis un site de warez. Infostealer Lumma déployé. Log exfiltré fin 2025.
>
> **Étape 2** — Vente du log sur Russian Market fin 2025, ~120 USD (tier « corporate VPN + tokens actifs », premium).
>
> **Étape 3** — Achat par un IAB russophone (pseudonyme identifié partiellement : **magnit_ru**, actif sur XSS Forum). Qualification : vérification que les credentials VPN fonctionnent, exploration réseau, identification que Vectris est un groupe industriel aerospace.
>
> **Étape 4** — Revente. magnit_ru poste l'accès sur XSS début 2026 : « Access aerospace EU, R&D network, defense programs ». Prix demandé : ~35 000 USD.
>
> **Étape 5** — Achat par aero_source (ou un commanditaire derrière lui). Hypothèse Lucas : aero_source est soit (a) un opérateur individuel qui a acheté l'accès et a exfiltré les 420 Go lui-même, soit (b) le front d'une équipe plus grande, soit (c) un revendeur qui a acheté le dump à un acteur qui lui a fait l'exfiltration.
>
> **Étape 6** — Exfiltration : ~12 semaines d'activité sur le réseau Vectris (traces cohérentes avec les logs Mandiant), 420 Go extraits, focus sur R&D propulsion et dossiers fournisseurs défense.
>
> **Étape 7** — Vente sur IndustrialLeaks : post public il y a 11 jours à 65 000 USDT.
>
> La chaîne implique donc **au moins 3 acteurs distincts** : opérateur Lumma (infection initiale, revente bulk), magnit_ru (IAB), aero_source (exfiltration ou revente finale). Complexifie l'attribution mais multiplie les angles d'investigation. Identifier un seul de ces acteurs précisément pourrait suffire à remonter la chaîne.

---

### Chapitre 17 — Marché des 0-day et chaîne exploit → attaque

Les **0-day** — vulnérabilités non connues de l'éditeur et donc non patchées — sont l'apex de l'écosystème offensif. Leur marché est structurant pour le dark web, avec des particularités qui distinguent ce segment du reste de la cybercriminalité.

#### 17.1 Qu'est-ce qu'un 0-day

Terminologie précise.

**Vulnérabilité** : faille dans un logiciel, une configuration, un protocole permettant potentiellement une exploitation malveillante.

**0-day (zero-day)** : vulnérabilité non encore connue publiquement et non patchée par l'éditeur. Son exploitation est potentiellement **surprise** — aucune signature ne la détecte, aucune mitigation connue ne la bloque.

**N-day** : vulnérabilité récemment rendue publique et patchée, mais pas encore déployée largement. Les attaquants exploitent les N-day pendant la fenêtre entre publication du patch et déploiement généralisé.

**Exploit** : code qui exploite une vulnérabilité. Peut être théorique (proof-of-concept), fonctionnel (weaponisé), ou en production (stable, compatible multi-environnements).

**Exploit chain** : chaîne de plusieurs exploits combinés pour atteindre un objectif plus ambitieux (par exemple : escape sandbox navigateur + escalation privilèges kernel → RCE avec privilèges système).

#### 17.2 Le marché légal : bug bounty et brokers

L'écosystème des vulnérabilités n'est pas uniquement illégal. Un marché légal existe, structuré.

**Bug bounty programs**. Les grands éditeurs (Google, Microsoft, Apple, Mozilla, Meta, Samsung, etc.) offrent des récompenses pour la déclaration responsable de vulnérabilités. Montants : de quelques centaines de dollars pour des bugs mineurs à plusieurs millions pour des chaînes d'exploits complètes sur iOS ou Android. **Apple Security Bounty** : jusqu'à 2 M USD pour une chaîne avec persistance sur iOS. **Google Vulnerability Reward Program** : jusqu'à 1,5 M USD pour certains cas Android.

**Plateformes bug bounty** : HackerOne, Bugcrowd, Intigriti, YesWeHack (français), Synack. Hébergent les programmes de dizaines de milliers d'organisations.

**Pwn2Own** : compétition annuelle (ZDI / Trend Micro, plusieurs éditions par an dans différentes villes) où des chercheurs exploitent des logiciels cibles pour des récompenses publiques. Moyen médiatisé de révéler des vulnérabilités.

**ZDI (Zero Day Initiative)** : programme de rachat de vulnérabilités par Trend Micro. Paye les chercheurs, travaille avec les éditeurs pour patch, publie les advisories.

**Brokers commerciaux** : entreprises qui achètent des vulnérabilités à des chercheurs et revendent à des clients (souvent gouvernementaux). **Zerodium** est la référence historique — prix publics depuis des années, jusqu'à 2,5 M USD pour des chaînes Android. **Crowdfense** : concurrent. **Intrepidus / ERNW / Vupen historique** : prédécesseurs. Ces brokers opèrent **légalement**, vendant à des gouvernements de démocraties (ou présentés comme tels — débats existent sur certains clients effectifs).

#### 17.3 Le marché gris et noir

En parallèle du marché légal, un marché **gris** (légalité ambiguë) et **noir** (clairement illégal) existe.

**Marché gris** : vente à des gouvernements de régimes autoritaires, ou à des entreprises de surveillance. Le 0-day lui-même n'est pas illégal — la vulnérabilité est juste de l'information technique. Mais son usage ultérieur peut être problématique. NSO Group (Pegasus), Candiru, Intellexa / Predator achètent des 0-day et les intègrent dans leurs outils de surveillance. Leurs clients incluent parfois des États qui ciblent journalistes et dissidents.

**Marché noir** : vente à des acteurs cybercriminels ou à des services de renseignement hostiles qui exploitent pour opérations offensives. Moins médiatisé, moins structuré, mais actif. Les prix peuvent rivaliser avec le marché légal pour les vulnérabilités les plus précieuses.

**Disruption** : les 0-day disparaissent du marché après publication. Leur valeur chute de 90%+ dans les semaines suivant un patch public. Les acteurs du marché noir cherchent donc à acheter des 0-day avec **exclusivité** et à les utiliser **rapidement** avant découverte et patching.

#### 17.4 Prix indicatifs

Sources : Zerodium price list publique, Crowdfense, rapports Atlantic Council, observations marché noir.

| Cible | Marché légal bug bounty | Marché broker (Zerodium, Crowdfense) | Marché gris/noir |
|---|---|---|---|
| Chrome RCE | 250 k USD (Google VRP) | 500 k - 1,5 M USD | 500 k - 2 M USD |
| iOS complete chain avec persistance | 2 M USD (Apple) | 2 - 2,5 M USD | 5 - 10 M USD (rumeurs) |
| Android complete chain | 1,5 M USD (Google) | 1,5 - 2,5 M USD | 3 - 8 M USD |
| WhatsApp RCE 1-click | N/A | 1,5 M USD | Plus |
| Windows LPE | ~30 k USD | ~80 k - 200 k USD | Comparable |
| Exchange Server RCE | ~30 k USD | ~100 k USD | Plus |
| Safari RCE | 100 k USD | ~300 k USD | Plus |
| Tor Browser exploit | — | Jusqu'à 1 M USD | Demande forte renseignement |

Variation par :
- **Fiabilité** : exploit stable qui marche à 100% vaut plus qu'un exploit probabiliste.
- **Fraîcheur** : exploit qui vient d'être découvert vs exploit avec risque de découverte imminente.
- **Contexte d'exploitation** : nécessite interaction utilisateur vs fully remote, 1-click vs 0-click.
- **Persistance** : survit aux reboot ou non.
- **Compatibilité** : fonctionne sur multiple versions du logiciel cible.

#### 17.5 La chaîne 0-day → attaque

Comment un 0-day devient une attaque concrète.

**Étape 1 — Découverte**. Un chercheur identifie une vulnérabilité. Peut venir de fuzzing automatisé (AFL, libFuzzer), de reverse engineering de patches (« 1-day research » — étudier un patch pour identifier la vuln qu'il corrige), d'audit manuel de code source.

**Étape 2 — Weaponisation**. Développement d'un exploit fonctionnel. Fiabilisation, test sur multiples versions, contournement des mitigations (ASLR, DEP, CFI, PAC, etc.). Peut prendre des semaines à des mois.

**Étape 3 — Décision économique**. Le chercheur choisit un canal : responsible disclosure (bug bounty, gratuit jusqu'à 2 M USD chez Apple), broker légal (Zerodium), broker gris, vente privée à un acteur offensif.

**Étape 4 — Intégration dans un outil**. L'acheteur intègre l'exploit dans son framework. NSO l'intègre dans Pegasus ; un APT l'intègre dans sa toolchain ; un opérateur ransomware l'intègre dans son loader.

**Étape 5 — Déploiement**. L'outil est utilisé contre des cibles. La vulnérabilité commence à être exploitée dans la nature.

**Étape 6 — Détection**. Tôt ou tard, un défenseur détecte l'attaque. Peut prendre des jours (attaque bruyante, nombreuses victimes) ou des années (opération ciblée discrète, peu de victimes).

**Étape 7 — Publication / patching**. Après détection, l'éditeur est notifié (par le défenseur, par un chercheur ayant découvert indépendamment, par le vendor observant les attaques), patche, publie l'advisory. La vuln devient N-day.

**Étape 8 — Exploitation N-day**. Fenêtre de quelques jours à semaines où le patch existe mais pas partout. Acteurs moins sophistiqués exploitent massivement.

**Étape 9 — Oubli**. La vuln devient partie de l'histoire. Son usage continue longtemps contre les systèmes non patchés (certains systèmes hérités jamais patchés sont vulnérables à des bugs découverts il y a 10 ans).

#### 17.6 Les vagues récentes exploitant des 0-day

Illustrations récentes de la chaîne 0-day → attaque dans la nature.

**MOVEit Transfer (mai-juin 2023)** — Cl0p exploite CVE-2023-34362 (0-day SQL injection dans MOVEit) massivement, impacte des milliers d'organisations (santé, gouvernements, entreprises) via leurs prestataires utilisant MOVEit.

**Citrix Bleed (CVE-2023-4966, octobre 2023)** — vulnérabilité Citrix Netscaler exploitée par LockBit, autres acteurs. Permet bypass MFA via leak de sessions.

**Ivanti Connect Secure (CVE-2023-46805, CVE-2024-21887, janvier 2024)** — exploitation par Volt Typhoon (Chine, APT) et d'autres.

**Palo Alto GlobalProtect (CVE-2024-3400, avril 2024)** — exploité par UTA0218 (possible APT).

**Oracle EBS (2025)** — exploité par Cl0p comme continuation de leur stratégie d'exploitation edge devices.

Ces vagues illustrent une tendance : les APT et groupes ransomware sophistiqués ont progressivement adopté l'exploitation de 0-day sur edge devices comme vecteur privilégié — plus discret qu'un phishing (qui génère des alertes), plus scalable qu'une intrusion manuelle, et ciblant des dispositifs souvent dépourvus de visibilité défensive.

#### 17.7 Les ventes de 0-day sur forums

Sur les forums cybercriminels, les ventes de 0-day sont **rares publiquement** mais existent. Patterns observés :

**Posts discrets**. Annonce sur XSS ou Exploit avec minimum d'info publique, négociation en privé. L'annonce mentionne classe de vulnérabilité (RCE, LPE, sandbox escape), cible (Chrome, Firefox, iOS, Android, produit spécifique), prix plancher.

**Escrow par forum**. Les forums sérieux proposent un escrow qualifié pour ces transactions — admin prend la clé du buyer et du seller, valide l'exploit fonctionne, libère après validation.

**Réputation extrême**. Seuls les vendeurs les plus établis font des ventes visibles — un nouveau compte qui prétend vendre un iOS 0-day est presque certainement scammer.

**Screenshots de démonstration**. Certains vendeurs fournissent preuve de fonctionnement (vidéo, screenshot) sous NDA avant achat. D'autres refusent toute démo sans paiement préalable (difficile à contourner mais classique).

**Clients typiques forums** : affiliés RaaS, APT moins dotés, acteurs étatiques moyens — pas les grands (qui ont leurs propres canaux).

#### 17.8 Investigation et renseignement sur les 0-day

Pour un analyste CTI défensif.

**Veille des annonces**. Monitoring de XSS, Exploit, BreachForums pour posts liés à des 0-day cibles (produits utilisés par son organisation). Alerting sur mots-clés.

**Détection des exploitations dans la nature**. Anomalies comportementales sur les edge devices (VPN, firewalls, serveurs exposés) même sans signature existante. Threat hunting proactif sur les produits historiquement ciblés.

**Collaboration avec éditeurs**. Remontée rapide à l'éditeur en cas de détection d'exploitation suspecte, pour accélérer potentiel patching.

**Analyse de patches**. Étude des patches publiés pour identifier les vulns patchées (1-day research en usage défensif) et anticiper les exploitations massives dans la fenêtre N-day.

#### 17.9 Fil rouge — DARKSTREAM : pas de 0-day impliqué

> **🌐 DARKSTREAM — Épisode 11 : angle 0-day écarté**
>
> Lucas a initialement envisagé que la compromission Vectris aurait pu impliquer un 0-day (cible industrielle de valeur). Son investigation croisée (forensics Mandiant côté Vectris, observations dark web) confirme : **pas de 0-day**. Le vecteur était un **stealer log** classique, un accès VPN corporate acheté sur Russian Market, exploité sur plusieurs semaines pour cartographier et exfiltrer.
>
> Cette absence de 0-day est en soi un renseignement important. Elle place l'attaquant dans la catégorie **« cybercriminel sophistiqué avec moyens limités »** plutôt que **« APT étatique avec capacités offensives haut de gamme »**. Un APT étatique ciblant Vectris pour ses secrets aerospace/défense aurait probablement utilisé un vecteur plus discret (0-day sur edge device, spear-phishing sophistiqué), pas une chaîne commoditisée stealer log → IAB → exfiltrateur.
>
> Conséquence pour le rapport final : l'attribution pointe vers **criminalité organisée à motivation financière** plutôt que **espionnage étatique**. La DGSI confirme cette lecture. Les données exfiltrées pourraient finir entre les mains d'un acteur étatique in fine (si elles sont achetées sur IndustrialLeaks par un acheteur intermédiaire), mais le vol initial et sa commercialisation sont de profil cybercriminel.

---

## PARTIE IV — ÉCONOMIE CLANDESTINE

> **Ce que cette partie apprend.** Comprendre **pourquoi** l'économie du dark web fonctionne malgré l'absence d'État, de contrats juridiquement exécutables, et de confiance interpersonnelle. Connaître les mécanismes (réputation, escrow, vouching, arbitrage), les pathologies (arnaques, exit scams, manipulation de la confiance), et les modèles économiques criminels qui structurent l'écosystème.
>
> **Ce qu'elle ne couvre pas.** Les techniques d'investigation de ces économies (Partie V), les analyses de traçage financier (Ch.31), les éléments réglementaires qui tentent de les contrer (Ch.40).
>
> **Ce que vous saurez faire après cette partie.** Lire un escrow pour y repérer les signaux d'intégrité, détecter les prémices d'un exit scam, situer un acteur dans un modèle économique (IAB, courtier, opérateur), et comprendre les incitations qui gouvernent les comportements observés.

---

### Chapitre 18 — Pourquoi l'économie du dark web fonctionne

À première vue, l'économie du dark web devrait être impossible. Des inconnus anonymes transigent pour des montants significatifs sans tribunaux, sans contrats exécutables, sans banque centrale, sans identité vérifiée. La tentation d'arnaque devrait être permanente et dévastatrice. Pourtant, des dizaines de millions de transactions se déroulent chaque année, avec un taux de complétion relativement élevé. Comprendre pourquoi c'est un problème économique fondamental — et sa solution éclaire l'investigation.

#### 18.1 Le problème du trust sans tiers de confiance

Toute transaction économique pose un **problème de confiance**. Le vendeur craint le non-paiement, l'acheteur craint la non-livraison. Dans une économie classique, ce problème est résolu par plusieurs instruments :
- **Tribunaux** : en cas de litige, une juridiction neutre tranche selon un droit écrit.
- **Contrats** : engagements formalisés exécutables.
- **Intermédiaires** : banques, cartes de crédit avec mécanisme de chargeback, plateformes avec garanties.
- **Identité publique** : les parties sont identifiées, leur réputation est documentée, les arnaques laissent des traces traçables.

Dans le dark web, **aucun de ces instruments classiques n'est disponible**. Les parties sont pseudonymes, il n'y a pas de tribunal applicable aux transactions illégales, les paiements crypto sont irréversibles (pas de chargeback), aucune autorité ne peut légitimement contraindre une partie à exécuter.

Comment l'économie fonctionne-t-elle alors ? La réponse : par un **système de substitution institutionnelle** — les forums, marchés et communautés créent des institutions privées qui remplacent fonctionnellement les institutions publiques manquantes.

#### 18.2 Les institutions de substitution

**La réputation individuelle persistante**. Chaque pseudonyme a un historique transactionnel, des reviews, des feedbacks. Un pseudonyme avec 500 transactions réussies et 2 ratings négatifs est plus digne de confiance qu'un pseudonyme avec 3 transactions. La **réputation est le capital principal** d'un acteur sérieux — et la perdre est coûteux (repartir de zéro sous un nouveau pseudo, temps d'accumulation de 6-18 mois).

**L'escrow de forum ou marché**. Mécanisme de dépôt : l'acheteur envoie le paiement à un tiers (le forum ou le marché), qui le retient jusqu'à confirmation de livraison. Si l'acheteur confirme, le vendeur est payé. Si litige, arbitrage. Ce mécanisme, quoique imparfait, réduit drastiquement le risque d'arnaque unilatérale (Ch.19).

**Le vouching (parrainage)**. Un membre établi engage sa propre réputation en garantissant un nouveau. Si le nouveau scam, le parrain est pénalisé. Cette **chaîne de confiance transitive** permet d'accepter des nouveaux sans qu'ils partent de zéro total.

**L'arbitrage communautaire**. En cas de litige, les modérateurs ou admins tranchent selon des principes publiés (règles du forum, précédents). La **publication du jugement** fait fonctionner le système — un vendeur déclaré scammer voit son pseudonyme sali sur toute la plateforme, souvent cross-platform.

**La pression sociale et la communauté**. Les forums actifs ont une **mémoire collective**. Les scammers notoires sont connus, leurs pseudonymes listés publiquement, leurs IPs parfois publiées. Cette publicité sociale fonctionne comme un ban industriel — un scammer identifié est grillé dans tout l'écosystème pour des mois.

**Les blacklists cross-forum**. Certains forums partagent leurs listes de bannis. Un scammer banni sur XSS peut se retrouver banni préventivement sur Exploit. Cette coordination inter-forums est imparfaite mais réelle.

#### 18.3 La coûteuse construction de réputation

Pour un acteur sérieux, construire une réputation utilisable prend **6-18 mois au minimum**. Le processus typique :

**Mois 1-3 — entrée**. Création du compte sur un forum, posts de présentation, participation à des discussions. Lecture active, apprentissage des codes. Pas de vente immédiate (interdit par les règles de la plupart des forums sérieux pour les nouveaux).

**Mois 3-6 — premières transactions**. Petites ventes (50-500 USD), avec échantillons gratuits pour démontrer la qualité. Chaque transaction réussie ajoute une review positive. Les premiers 10-20 transactions sont les plus difficiles — pas encore de réputation établie, les acheteurs sont prudents.

**Mois 6-12 — consolidation**. Avec ~30-50 transactions réussies, le vendeur est **trusted**. Prix peuvent monter, qualité/spécificité de l'offre plus haute, accès aux zones premium du forum. Les gains commencent à être significatifs.

**Mois 12+ — établissement**. Après 100+ transactions, le vendeur est une figure reconnue. Clients récurrents, accès à des produits premium (0-day, accès corporate haut de gamme). Revenus potentiels de plusieurs centaines de milliers à plusieurs millions USD/an.

**Cette courbe explique plusieurs comportements** : les scammers ont tendance à opérer en rafales courtes (2-4 semaines de scam intensif, puis abandon du pseudo), parce que construire une réputation sérieuse prend trop de temps pour le petit gain à court terme. Les acteurs sérieux protègent leur réputation — ne scamment pas leurs clients, parce que la valeur actualisée de leur réputation est bien supérieure au gain d'un scam.

#### 18.4 Les ruptures de confiance

Malgré ces mécanismes, les ruptures se produisent.

**Exit scams par opérateur**. Traitement Ch.20. Un opérateur de marché ou forum s'enfuit avec les fonds en escrow.

**Vendeurs seniors qui scamment**. Rare mais arrive. Un vendeur avec 500 transactions et excellente réputation qui scam massivement en une seule opération finale. Motivation : gain ponctuel considérable avec perte de la réputation acceptée. Plus fréquent quand le vendeur sent que sa réputation va tomber de toute façon (arrestation imminente, conflit interne).

**Attaques externes**. Un forum compromis par les forces de l'ordre ou par des concurrents peut voir son historique de transactions falsifié, ses escrows volés, ses membres dox. Disruption temporaire ou définitive de l'économie locale.

**Cyclic collapse**. Parfois, une cascade de méfiance se déclenche : un vendeur majeur scam → les acheteurs méfiants retirent leurs fonds en masse → l'opérateur ne peut honorer les retraits → exit scam de l'opérateur → plateforme fermée. Panique bancaire, version dark web.

#### 18.5 Pourquoi ça marche malgré tout

Mathématiquement, l'économie fonctionne parce que :
- **Le nombre de transactions honnêtes dépasse les transactions frauduleuses**. Les acteurs sérieux, majoritaires en nombre et en volume, dominent l'activité globale.
- **La perte de réputation est coûteuse**. Pour un acteur établi, le gain d'un scam est typiquement inférieur à la valeur actualisée de sa réputation. L'incitation rationnelle est d'honorer les transactions.
- **Les mécanismes de substitution capturent la plupart des cas**. Escrow, arbitrage, blacklists gèrent la majorité des litiges.
- **Les pertes sont partagées**. Les acheteurs savent qu'un certain pourcentage de transactions échoueront. Ils calculent cette « taxe » dans leur modèle économique.

Pour un analyste, ces mécanismes sont autant de **points d'observation**. Un vendeur qui sort du schéma standard (pseudonyme neuf, pas de vouching, prix très bas, refus d'échantillon) est en probabilité très élevée un scammer — ce qui influe sur la priorisation des pistes d'investigation.

---

### Chapitre 19 — Réputation, escrow, vouching, arbitrage

Approfondissement des mécanismes fiduciaires du dark web. Ce chapitre détaille comment ils fonctionnent concrètement et comment l'investigateur peut les lire.

#### 19.1 Le système de réputation

**Composantes d'un profil de vendeur** :
- **Ancienneté** : date d'inscription sur le forum/marché, date du premier post, date de la première transaction.
- **Nombre de transactions** : total cumulatif.
- **Feedback positif / négatif / neutre** : généralement sur échelle eBay-like.
- **Commentaires** : remarques textuelles des acheteurs post-transaction.
- **Tags et ranks** : « Trusted », « VIP », « Verified Vendor », selon le forum.
- **Historique des posts** : contributions aux discussions, activité communautaire.
- **Vouches externes** : mentions positives par d'autres vendeurs établis.

**Lecture analytique** :
- **Feedback 98%+** : probable vendeur sérieux (rares disputes, bien résolues).
- **Feedback 80-95%** : zone ambiguë — soit vendeur correct avec quelques problèmes, soit vendeur médiocre mais non scammer.
- **Feedback < 80%** : **red flag** — fuir.
- **Volume soudain en hausse** : peut signaler build-up avant exit (si opérateur) ou simplement succès légitime (si vendeur). À contextualiser.
- **Disputes récentes non résolues** : signal négatif croissant.
- **Changement de PGP** : **très rouge** — rachat de compte possible, compromis d'opérateur, acteur différent derrière le pseudo.

#### 19.2 L'escrow

**Mécanisme standard** :

1. **Listing** : vendeur crée une annonce, précise prix, escrow délai attendu (typiquement 3-14 jours).
2. **Commande** : acheteur commande, **envoie le paiement au wallet de l'escrow du marché** (pas au vendeur).
3. **Vendeur expédie** : vendeur est notifié du paiement reçu, expédie le produit.
4. **Confirmation de réception** : acheteur reçoit le produit, marque la transaction comme « finalized ».
5. **Libération** : marché libère les fonds au wallet du vendeur (moins la commission).

**En cas de litige** :
- Acheteur ouvre un dispute : explique pourquoi (non-livraison, produit non conforme, produit de moindre qualité).
- Vendeur répond : fournit preuve d'expédition, tracking, explications.
- Modérateur/admin arbitre : décision (total à l'acheteur, total au vendeur, split 50/50 ou autre).
- Feedback mutuel : les deux parties peuvent laisser des commentaires, affectant les réputations futures.

**Finalize Early (FE)**. Option disponible sur certains marchés : l'acheteur libère les fonds **avant** réception. Utilisé par vendeurs extra-fiables comme avantage compétitif (évite la trésorerie bloquée). **Risque majeur pour acheteur** — si le produit n'arrive pas, aucun recours. FE est typiquement réservée aux vendeurs top-tier.

**Multi-sig escrow**. Variante avancée : les fonds sont verrouillés sur une adresse multi-signature (2-of-3 typiquement : acheteur, vendeur, arbitre). Libération nécessite 2 signatures sur 3. Pour le vendeur : paiement libéré si acheteur confirme (2-of-3). Pour l'acheteur : remboursement possible si arbitre valide le litige (2-of-3 avec vendeur ou, en dispute, arbitre + acheteur). Le marché ne détient jamais les fonds directement — réduction du risque d'exit scam de l'opérateur. Techniquement plus complexe, pas universellement adopté.

#### 19.3 Le vouching

**Mécanisme**. Un membre établi de la communauté (« voucher ») publie un endorsement d'un nouveau membre ou d'un vendeur. Cet endorsement engage la réputation du voucher. Si le vouché scam, le voucher subit une pénalité (baisse de rank, bannissement temporaire, perte de privilèges de vouching).

**Variantes** :
- **Vouching ouvert** : le post de vouch est public, visible de tous.
- **Vouching privé** : confirmation transmise à l'admin du forum, qui valide le nouveau sans exposer le voucher.
- **Vouching transactionnel** : un membre atteste avoir réalisé une transaction avec succès avec le vouché.
- **Vouching caractérologique** : un membre atteste que le vouché est « sérieux », « honorable », sans nécessairement avoir transigé.

**Limites** :
- **Chain of vouches vulnérable** : si un voucher senior est compromis, tout ce qu'il a vouché est suspect.
- **Vouching mercenaire** : certains membres vendent leurs endorsements à prix. Pratique mal vue mais existe.
- **Sybil vouching** : un acteur contrôle plusieurs comptes et vouche lui-même ses propres comptes secondaires. Difficile à détecter dans les petits forums.

#### 19.4 L'arbitrage

**Qui arbitre** :
- **Modérateurs** du forum/marché, habituellement pour les petites disputes.
- **Admins** pour les disputes importantes ou les affaires sensibles.
- **Tiers arbitre** : certains forums ont des arbitres indépendants (membres seniors mandatés) pour réduire le conflit d'intérêt des admins.

**Processus type** :
1. Une partie ouvre le dispute, expose les faits avec preuves (screenshots, hashes, tracking, communications).
2. L'autre partie répond sous 48-72h avec sa version.
3. L'arbitre demande preuves supplémentaires si besoin.
4. Décision rendue, souvent avec argumentaire publié (visibilité pour la communauté).
5. Exécution : les fonds sont libérés selon la décision.

**Types de décisions** :
- **Full refund acheteur** : vendeur reconnu scammer ou incapable de prouver l'expédition.
- **Full release vendeur** : acheteur reconnu de mauvaise foi (dispute frauduleux après réception).
- **Split 50/50 ou autre** : incertitude, pas de preuve décisive pour l'une ou l'autre partie.
- **Dispute closed sans décision** : rare, typiquement quand les deux parties disparaissent.

**Intégrité de l'arbitrage**. Un admin corrompu peut favoriser systématiquement une partie (vendeur cartel, vendeur qui paie des bakchichs, etc.). Les forums sérieux ont des **audit trails** et parfois des **appeals** à un niveau supérieur. Un pattern de décisions biaisées finit par être identifié par la communauté, érode la confiance, et peut faire chuter le forum.

#### 19.5 L'économie de la confiance

Ce système crée une **économie de la confiance**. La réputation est un actif :
- **Transférable partiellement** : un vendeur établi peut « migrer » vers un nouveau forum en apportant des vouches de ses pairs. Il ne repart pas de zéro, mais ne bénéficie pas immédiatement de son rang maximal ailleurs.
- **Monétisable directement** : certains pseudonymes établis sont **vendus** sur des forums (rare, interdit par la plupart des règles, mais existe). Prix : 1 000-50 000 USD selon la force du pseudo.
- **Coûteuse à perdre** : un scam détruit des années de construction.

Pour l'analyste, l'économie de la confiance est un point d'attaque :
- Un acteur établi a beaucoup à perdre — les approches de type « coopération avec les autorités » ou « retournement » peuvent fonctionner là où un nouveau scammer ne céderait rien.
- Un scammer jetable est plus facile à identifier par patterns (neuf, prix bas, refus d'échantillon) mais aussi plus difficile à poursuivre (disparaît rapidement, pseudo sans histoire, pas de levier).

---

### Chapitre 20 — Arnaques, exit scams et manipulation de la confiance

Malgré les mécanismes de confiance, l'arnaque est structurelle dans l'écosystème. Ce chapitre cartographie les grandes catégories, leurs mécanismes, et leurs signaux.

#### 20.1 Taxonomie des arnaques

**Petits scams de vendeur** :
- **Non-livraison** : acheteur paie, produit jamais envoyé. Typique pour vendeurs jetables.
- **Produit de moindre qualité** : drogues diluées, données périmées, accès non fonctionnel, malware à la place du logiciel promis.
- **Volume réduit** : vendeur promet 500 Go, livre 50 Go. Espère que l'acheteur n'audite pas.
- **Données recyclées** : vente comme « fresh breach » de données publiquement disponibles depuis des mois.

**Scams structurés** :
- **Double selling** : la même donnée vendue en exclusivité à plusieurs acheteurs. Viole les termes annoncés, destruction de la valeur.
- **Fake breach** : annonce d'un breach qui n'a pas eu lieu, avec données fabriquées pour passer quelques vérifications superficielles.
- **Impersonation** : pseudonyme qui mime un vendeur établi (slight variation orthographique). Exploite la crédibilité de la cible impersonnée.

**Exit scams** (Ch.11.4).

**Meta-scams** :
- **Fake escrow** : un « tiers de confiance » se propose pour un escrow, disparaît avec les fonds. Les forums sérieux ont leurs escrows officiels ; tout escrow tiers « découvert récemment » est suspect.
- **Fake arbitres** : usurpation d'identité d'admin. Un « admin » qui contacte en privé pour résoudre un litige est probablement faux — les vrais arbitres interviennent dans les threads officiels.

**Scams contre les analystes / forces de l'ordre** :
- **Honeypots criminels** : vendeurs qui distribuent intentionnellement des données piégées (fichiers contenant des beacons web, scripts malveillants) à des profils soupçonnés d'être des analystes.
- **Faux dissidents** : pseudonymes qui prétendent vouloir quitter le crime, vendent des « informations » aux investigateurs, souvent fausses ou trompeuses.

#### 20.2 Signaux de scam typiques

**Côté vendeur** :
- **Compte neuf** (< 3 mois) sans vouching.
- **Prix nettement inférieur** à la moyenne du marché pour le même type de produit.
- **Refus d'échantillon** systématique.
- **Pression temporelle** : « offre limitée 24h », pour empêcher la due diligence.
- **Communications incohérentes** : russe correct puis anglais bizarre puis retour russe — plusieurs opérateurs derrière un pseudo, parfois des scammers coopérant.
- **PGP non signé ou nouveau** : sérieux vendeur signe ses posts, avec clé stable.
- **Refus de multi-sig escrow** : préférence pour paiement direct ou FE. Légitime parfois, suspect souvent.

**Côté opérateur (forum/marché)** :
- **Dégradation des délais** : support qui ne répond plus, disputes qui traînent.
- **Retraits ralentis** : nouveaux délais imposés, vérifications additionnelles.
- **Buffer d'escrow visible anormalement élevé** : si le forum affiche (volontairement ou en leak) ses stocks en escrow qui grimpent alors que retraits diminuent, exit scam probable.
- **Communications des admins qui changent de ton** : plus promotionnelles, plus silencieuses, ou disparues.
- **Domaines .onion qui changent sans annonce cohérente**.
- **Partenariats communautaires qui se rompent** : anciens admins qui partent, voisins forums qui dé-vouchent publiquement.

#### 20.3 Comment se protéger (pour acheteur, pour investigateur)

**Pour l'acheteur avisé** :
- Transiger **uniquement avec des vendeurs établis** (500+ transactions, 98%+ feedback, ancienneté > 12 mois).
- Utiliser **escrow du marché** systématiquement. Jamais de paiement direct.
- **Ne pas utiliser FE** sauf vendeur trustissime.
- **Ne pas laisser de gros stock** chez un marché (retirer rapidement après transactions).
- **Vérifier les PGP** : les clés des vendeurs réputés sont stables et cross-signed.
- **Monitoring des signaux** : si le forum commence à montrer des signes d'exit scam, retirer tout immédiatement.

**Pour l'investigateur** :
- **Considérer tout nouveau post suspect par défaut** — probabilité de scam plus élevée que probabilité d'authenticité.
- **Vérifier via échantillons** avant d'allouer des ressources à une piste.
- **Cross-checker les pseudonymes** sur multiple forums pour détecter les impersonations.
- **Ne jamais payer pour « débloquer » information** — les demandes de paiement pour information sont fréquemment des scams.
- **Valider via autorités ou victime** quand possible — un breach revendiqué mais non confirmé par la victime est à traiter avec scepticisme élevé.

#### 20.4 Les grands exit scams

Historique sélectif.

**Evolution Market (mars 2015)**. Ex-second plus grand marché de l'époque. Admins « Verto » et « Kimble » disparaissent avec environ 12 M USD de BTC en escrow. Communauté anéantie, migration massive vers Abraxas puis AlphaBay.

**Nucleus (avril 2016)**. Exit scam plus modeste, ~5 M USD.

**Empire Market (août 2020)**. ~30 M USD, un des plus gros de l'histoire. Admins s'évaporent sans annonce. Les spéculations ont évoqué soit exit volontaire, soit compromission par un tiers, soit panic mid-course face à une menace judiciaire.

**Monopoly Market (2023)**. Saisi par les autorités mais au même moment, des signaux d'exit étaient présents — confusion post-hoc sur le réel séquencement.

**Incognito Market (2024)**. Modèle hybride — exit scam avec menace de dox des utilisateurs non-payeurs.

#### 20.5 La gestion d'un exit scam côté analyste

Quand un exit scam se produit sur un forum suivi, l'analyste peut :

**Capturer immédiatement** les dernières observations avant que le forum disparaisse (posts actifs, pseudonymes actifs, annonces récentes). Le forum peut re-disparaître définitivement.

**Monitorer la migration**. Les membres scammed se regrouperont sur d'autres forums, souvent avec posts « je viens de perdre 20k sur Empire, quelqu'un a des nouvelles ». Ces posts sont **riches en renseignement** — ils exposent des pseudonymes, des patterns de transaction, des sommes.

**Suivre les wallets**. Si l'admin exit scam, les fonds transitent. Les adresses reçoivent de gros montants en peu de temps, puis se dispersent. Tracking on-chain (Chainalysis, TRM) peut révéler des patterns (où vont les fonds, quelle méthode de blanchiment) et potentiellement identifier l'opérateur.

**Documenter**. Même si l'investigation ne peut pas pénaliser l'exit scammer, la documentation nourrit la connaissance de l'écosystème — profils d'admins, patterns d'opération, durées de vie typiques.

---

### Chapitre 21 — Modèles économiques criminels

Synthèse des modèles économiques observés sur le dark web. Ce chapitre articule les rôles de la Partie III en modèles financiers cohérents.

#### 21.1 Le modèle du vendeur individuel

**Acteur** : individu ou petite équipe (1-5 personnes).

**Produit** : spécialisé — drogues, fullz, credentials, documents contrefaits, petits services.

**Volumes** : dizaines à centaines de transactions par mois.

**Revenus annuels** : 50 k - 500 k USD typiquement, jusqu'à quelques millions pour les meilleurs.

**Risques** : identification via patterns (timing, OPSEC faible), erreurs opérationnelles (réutilisation pseudonyme, leaks personnels), dispute avec un gros acheteur qui dox.

**Exemples publics** : les vendeurs condamnés sont légion dans la presse judiciaire US, UK, DE. Exemples emblématiques : « Xanax King » condamné pour vente de faux Xanax sur AlphaBay (2017-2019) ; multiples dealers saisis lors d'operations police.

#### 21.2 Le modèle de l'opérateur de plateforme

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

**Risques** : saisies d'infrastructure, inculpations nominales (LockBitSupp), conflits d'affiliés, érosion post-disruption (LockBit qui peine à rebondir).

#### 21.4 Le modèle de l'IAB

**Acteur** : individu ou petite équipe.

**Produit** : accès préqualifiés.

**Volumes** : 10-50 accès vendus par an.

**Revenus** : 500-50 000 USD par accès, selon qualité. Revenus annuels typiques 200 k - 2 M USD.

**Risques** : identification via l'accès lui-même (si l'acheteur est infiltré, les comms peuvent remonter à l'IAB), erreurs d'OPSEC dans la compromission initiale.

#### 21.5 Le modèle du service provider (CaaS)

**Acteur** : opérateur d'un service — phishing kit, DDoS booter, malware-as-service, etc.

**Produit** : service récurrent avec abonnement.

**Revenus** : abonnements (50-1 000 USD/mois par utilisateur), jusqu'à dizaines de milliers d'utilisateurs pour les plus grands. Revenus annuels de 100 k à 10 M USD selon scale.

**Exemples** : Lumma Stealer (estimation sur plusieurs milliers d'abonnés × 250 USD/mois), LabHost avant démantèlement.

**Risques** : saisies (LabHost démantelé avril 2024), inculpations d'opérateurs.

#### 21.6 Le modèle de blanchiment

**Acteur** : spécialistes financiers, souvent liés à l'écosystème crypto.

**Produit** : conversion crypto → fiat utilisable.

**Revenus** : commissions 10-30% du montant blanchi. Volumes considérables possible — plusieurs entités (Suex, Bitzlato, Garantex historiquement, Chipmixer) ont traité des milliards USD avant saisie/sanction.

**Risques** : sanctions OFAC (Suex, Bitzlato, Garantex sanctionnés), saisies (Chipmixer mars 2023, Samourai avril 2024), inculpations (Larry Harmon condamné pour Helix, Alexey Pertsev pour Tornado Cash).

#### 21.7 Le modèle de l'hébergeur bulletproof

**Acteur** : opérateur d'infrastructure.

**Produit** : hosting résistant.

**Revenus** : abonnements de hosting premium. Centaines à milliers de clients, 500-10 000 USD/mois chacun.

**Risques** : saisies (Cyberbunker 2019, multiples avant), pression upstream (de-peering, blocages).

#### 21.8 La convergence des modèles

Les modèles se chevauchent et convergent. Un acteur peut opérer comme IAB **et** affilié RaaS, comme développeur malware **et** opérateur d'un service CaaS, comme plateforme **et** commanditaire de ransomware. Cette **polymorphie économique** rend l'attribution fine complexe.

Le dark web économique 2025-2026 est mieux décrit comme un **réseau de spécialistes interconnectés** que comme un écosystème de rôles purs. Un même individu ou groupe peut jouer plusieurs rôles selon les opportunités, les contraintes, les rythmes.

#### 21.9 Implications analytiques

Pour l'analyste, cette structure économique suggère plusieurs focus.

**Suivre les flux financiers** : chaque modèle produit des patterns crypto distinctifs. Les IAB reçoivent des paiements moyens, les RaaS reçoivent de très gros paiements épisodiques, les stealer operators reçoivent des flux constants de petits paiements. Chainalysis et équivalents peuvent identifier le modèle économique par profil transactionnel.

**Reconstruire les chaînes de valeur** : identifier le modèle économique d'un acteur aide à identifier ses partenaires amont/aval. Un IAB « accès manufacturing EU » est probablement lié à un groupe RaaS anglophone ; un opérateur de stealer logs alimente des IAB multiples.

**Anticiper les transformations** : les modèles évoluent. Un vendeur individuel peut devenir IAB en montant en gamme, un IAB peut fonder son propre groupe RaaS, un opérateur RaaS peut se retirer en blanchisseur. L'analyste suit ces trajectoires pour anticiper les tendances.

**Calibrer l'attribution** : chaque modèle a ses OPSEC typiques. Un vendeur individuel fait plus d'erreurs personnelles ; un opérateur RaaS opère avec plus de rigueur ; un service provider a des infrastructures plus visibles. L'attribution est plus facile sur certains profils que sur d'autres.

---

## PARTIE V — INVESTIGATION, VEILLE ET COLLECTE

> **Ce que cette partie apprend.** Conduire une investigation dark web de manière professionnelle — cadre juridique et éthique, OPSEC de l'analyste, méthodes de collecte, workflow d'investigation d'un data leak, pivoting OSINT, veille continue, préservation des preuves.
>
> **Ce qu'elle ne couvre pas.** Les méthodes avancées d'analyse et d'attribution (Partie VI), les cas d'usage spécifiques par secteur (Partie VII), les études de cas complètes (Partie VIII).
>
> **Ce que vous saurez faire après cette partie.** Conduire une enquête OSINT sur le dark web en respectant le cadre légal français/européen, bâtir et maintenir une persona, investiguer un leak de données de manière structurée, préserver les preuves de manière admissible, et construire un programme de veille dark web durable.

---

### Chapitre 22 — Cadre juridique, éthique et sécurité de l'analyste

Avant tout outil technique, l'analyste dark web doit maîtriser le cadre légal qui encadre son activité. Consulter un forum cybercriminel n'est pas illégal en soi — mais certains actes d'investigation le sont, et d'autres sont dans une **zone grise** qu'il faut savoir naviguer.

#### 22.1 Le cadre français

**Code pénal articles 323-1 à 323-8**. Atteinte aux STAD (systèmes de traitement automatisé de données). Incrimine :
- **323-1** : l'accès ou le maintien frauduleux dans un STAD (maximum 3 ans d'emprisonnement et 100 000 € d'amende ; circonstances aggravantes si suppression/modification de données : 5 ans, 150 000 €).
- **323-2** : l'entrave du fonctionnement d'un STAD (7 ans, 300 000 €).
- **323-3** : la modification frauduleuse de données (7 ans, 300 000 €).
- **323-3-1** : la détention et la diffusion d'outils conçus pour commettre ces infractions — **article clé pour l'analyste**, qui encadre la manipulation d'outils offensifs.

**Loi du 24 juillet 2015 sur le renseignement** et articles associés dans le Code de la sécurité intérieure : cadre des activités de renseignement encadrées par l'État. L'analyste privé n'opère pas sous ce régime, mais les agences partenaires (DGSI, DGSE) peuvent.

**Loi Informatique et Libertés + RGPD**. La collecte et le traitement de données personnelles exposées (même exposées par un attaquant) restent soumis aux régimes de protection. Un analyste qui capture un dump contenant des données personnelles doit gérer ce stock selon les règles applicables — base légale de traitement, minimisation, sécurisation, suppression post-exploitation.

**Code de procédure pénale article 40**. Tout fonctionnaire qui, dans l'exercice de ses fonctions, acquiert la connaissance d'un crime ou d'un délit, est tenu d'en aviser le procureur. Un analyste fonctionnaire (service public, OIV) peut être concerné — même en secteur privé, la logique de signalement est structurante.

**Cadre ANSSI / OIV**. Les OIV ont obligation de notification d'incidents significatifs à l'ANSSI. Les prestataires PASSI/PDIS/PRIS opèrent sous qualification.

#### 22.2 Le cadre européen

**Directive NIS 2 (UE 2022/2555)**. Transposée en France et dans tous les États membres. Obligations de cybersécurité et notification pour les entités essentielles et importantes dans 18 secteurs. Les analystes opérant pour ces entités ont un rôle dans la posture de notification.

**RGPD**. Régit les données personnelles. Les dumps contenant données personnelles doivent être traités avec base légale (intérêt légitime de l'investigation, mission de service public, etc.), minimisation, sécurité.

**Convention de Budapest sur la cybercriminalité (2001) et ses protocoles additionnels**. Cadre de coopération internationale en matière cybercriminalité. Protocole additionnel de mai 2022 facilite l'accès transfrontière à la preuve électronique.

**EU Cyber Solidarity Act (2024)**. Crée un réseau européen de SOC et un mécanisme de réponse d'urgence pour incidents cyber transfrontaliers.

**EU Cyber Sanctions Regime**. Sanctions ciblées contre cyberacteurs malveillants.

#### 22.3 Les zones grises

Plusieurs activités sont **dans la zone grise** — techniquement légales mais nécessitent prudence.

**Consulter des forums criminels**. Légal en tant que tel. La simple consultation d'un contenu publiquement accessible (même sur .onion) n'est pas une infraction.

**Créer un compte sur un forum criminel**. Nécessaire pour accéder aux zones fermées. Légal, avec précautions — le pseudonyme ne doit pas être utilisé pour commettre des infractions (solliciter des services criminels, acheter des données, participer à des discussions opérationnelles).

**Télécharger des échantillons**. Zone sensible. Télécharger un fichier contenant des données personnelles (même publiquement exposées par l'attaquant) peut contrevenir au RGPD. Télécharger du malware pour analyse est **généralement accepté** dans un cadre de recherche, mais la détention de malware est encadrée par l'article 323-3-1. Pratique recommandée : n'en télécharger que ce qui est strictement nécessaire à la mission, documenter la justification, sécuriser le stock, supprimer après exploitation.

**Télécharger des données volées**. Encore plus sensible. Principe : **nécessité et proportionnalité**. Télécharger un échantillon pour authentification est différent de télécharger l'intégralité d'un dump.

**Télécharger du CSAM**. **Interdit absolument**. Même dans un cadre d'investigation, la détention est criminelle. Les investigations CSAM relèvent des autorités judiciaires avec cadre spécifique (pornographie enfantine, articles 227-23 et suivants du Code pénal).

**Payer pour obtenir de l'information**. Dépend du contexte. Payer un droit d'entrée forum pour investigation : généralement accepté avec autorisation hiérarchique et traçabilité. Acheter des données volées : **risqué** — peut constituer recel. La DGSI accompagne ces cas.

**Contacter un vendeur en se faisant passer pour acheteur**. Zone grise classique. Généralement accepté pour investigation avec encadrement, mais peut constituer provocation dans certains cadres — la jurisprudence française est restrictive sur la **provocation à la commission d'infraction**. L'analyste doit se présenter comme acheteur potentiel pour obtenir des échantillons, mais ne pas pousser le vendeur à augmenter son activité criminelle.

**Infiltrer un groupe comme membre actif**. Réservé aux forces de l'ordre avec mandat judiciaire. Un analyste privé qui « infiltrerait » un groupe criminel dépasse largement le cadre légal.

#### 22.4 L'éthique professionnelle

Au-delà de la légalité stricte, plusieurs principes éthiques s'appliquent.

**Minimisation**. Collecter le minimum nécessaire à la mission. Ne pas stocker plus que ce qu'on exploite. Supprimer après exploitation.

**Non-prolifération**. Ne pas rediffuser les données collectées au-delà du cercle justifié. Un dump contenant des données personnelles ne se partage pas lightly, même entre analystes.

**Non-exploitation abusive**. Les données volées peuvent contenir des informations sensibles (vie privée, communications intimes, données médicales). L'analyste ne les exploite qu'au strict nécessaire à la mission, pas par curiosité.

**Transparence hiérarchique**. Les choix d'investigation sensibles (contact vendeur, paiement, téléchargement) sont documentés et autorisés par la hiérarchie.

**Respect des victimes**. Les victimes de breach sont des personnes. Contact avec elles doit respecter leur dignité — ni sensationnaliser, ni exploiter leur détresse.

**Coopération avec autorités**. Si l'investigation révèle des infractions graves (trafic humain, CSAM, terrorisme), signalement obligatoire aux autorités compétentes. Le secret professionnel n'est pas absolu.

#### 22.5 La sécurité personnelle de l'analyste

L'investigation dark web expose à plusieurs risques **personnels**.

**Risque technique**. Compromission du poste d'investigation via malware piégé. Les fichiers téléchargés, les liens cliqués, les sites visités peuvent contenir des exploits ciblant les analystes. Mesures : machine dédiée, VM jetables (Whonix + VM d'exécution), pas de comptes personnels sur la machine.

**Risque d'identification par les cibles**. Les acteurs malveillants font de la contre-surveillance. Un analyste qui utilise ses accès personnels, qui lit systématiquement les posts d'un vendeur spécifique, qui pose des questions révélatrices — peut être identifié comme investigateur. Conséquences : ciblage du compte d'investigation, tentative d'identification réelle (dox), voire menaces physiques dans les cas extrêmes.

**Risque juridique transfrontalier**. Un analyste français qui interagit avec un vendeur russe via un forum hébergé aux Pays-Bas peut techniquement tomber sous multiple juridictions. En pratique, si l'activité est légale en France et dans le cadre d'une mission professionnelle, le risque est faible, mais pas nul.

**Risque de manipulation psychologique**. L'immersion dans l'écosystème dark web expose à des contenus difficiles (violences, CSAM accidentellement croisé, narratifs extrêmes). L'analyste doit être soutenu par son organisation — debriefing psychologique, rotation des missions, limitation de l'exposition aux contenus traumatisants.

**Risque de compromission éthique**. Dérive possible — un analyste exposé longtemps à l'écosystème peut développer de l'empathie pour les cibles, se laisser tenter par des relations personnelles avec des sources, perdre la distance professionnelle. Supervision hiérarchique et rotation atténuent.

#### 22.6 Fil rouge — DARKSTREAM : encadrement légal

> **🌐 DARKSTREAM — Épisode 12 : cadrage DGSI**
>
> Lucas prépare son premier contact avec aero_source. Avant action, validation DGSI obligatoire.
>
> Réunion avec l'officier DGSI référent. Points validés :
> - **Contact OK** sous persona « mapletech » — acheteur technologique intéressé par specs aéronautiques. Légende crédible.
> - **Pas d'engagement ferme d'achat** — Lucas peut exprimer intérêt, demander échantillons, négocier indirectement, mais jamais confirmer la transaction. La DGSI précise : « ne provoquez pas la vente, cherchez à comprendre ».
> - **Pas de téléchargement de l'intégralité** — échantillons acceptés pour authentification, le dump complet non.
> - **Remontée bi-hebdomadaire** : Lucas briefe la DGSI tous les 3-4 jours sur l'évolution.
> - **Arrêt immédiat** si Lucas perçoit un risque d'exposition (persona identifiée comme analyste, menaces, contre-enquête).
> - **Pas d'achat** des données. Si aero_source impose paiement pour les échantillons (rare), arrêt de l'investigation de ce côté.
>
> Tous les échanges XMPP sont archivés (logs chiffrés chez Athéna, accessibles DGSI). Capture d'écran au fur et à mesure. Hash des fichiers téléchargés. Documentation exhaustive du cheminement d'investigation.
>
> Cette rigueur procédurale est **la condition de l'utilisabilité** de ce que Lucas produira. Un rapport sans chain of custody documentée n'a aucune valeur judiciaire. Un rapport trop fondé sur des actions juridiquement douteuses peut être écarté.

---

### Chapitre 23 — OPSEC opérationnelle de l'investigation

L'**OPSEC** (Operations Security) de l'analyste dark web est le pilier de la réussite d'une investigation. Une OPSEC défaillante expose l'analyste, compromet la mission, et peut mettre en danger les sources coopératives ou les collègues.

#### 23.1 La séparation des univers

Principe fondamental : **séparation totale** entre l'univers personnel de l'analyste, son univers professionnel hors investigation, et son univers d'investigation.

**Machines séparées**. Ordinateur dédié à l'investigation dark web. Jamais utilisé pour activités personnelles (réseaux sociaux, emails, banque), jamais pour activités professionnelles générales (mails corporate, documents, visioconférences). Configuration minimale : OS dédié (Whonix, Tails), navigateur Tor Browser uniquement, outils strictement nécessaires.

**Comptes séparés**. Emails jetables (protonmail, ctemplar, services .onion) pour les comptes d'investigation. Jamais de lien avec emails corporate ou personnels.

**Identités séparées**. Les personas d'investigation (pseudonymes, handles Telegram, JID XMPP) sont **strictement cloisonnées** de l'identité réelle de l'analyste. Aucune réutilisation d'un pseudo entre personas. Aucun lien traçable entre les personas et l'identité réelle.

**Financier séparé**. Wallets crypto dédiés à l'investigation, financés par un circuit professionnel (exchange corporate avec KYC de l'entreprise, pas de l'analyste personnellement). Transactions tracées par l'entreprise pour audit.

**Temporel séparé**. L'investigation se fait dans des créneaux dédiés. Le mélange entre activités dark web et tâches personnelles dans le même créneau temporel crée des risques de contamination (oubli de fermer Tor Browser avant d'ouvrir son email personnel, etc.).

#### 23.2 La persona

Une **persona** est un personnage fictif construit pour l'investigation. Elle doit être **crédible** et **cohérente**.

**Éléments de la persona** :
- **Pseudonyme** : unique, ne ressemble pas à d'autres pseudonymes utilisés par l'analyste (pas de pattern identifiable).
- **Histoire** : d'où vient-elle ? quel métier ? quelles compétences ? quels intérêts ?
- **Langue** : style d'écriture cohérent avec l'origine prétendue. Un analyste français qui joue un persona russophone doit maîtriser les codes linguistiques russophones — sinon se cantonne à l'anglais.
- **Niveau technique** : si persona « script kiddie » prétend avoir peu de skills, elle ne doit pas poser des questions trop sophistiquées. Si persona « pro » doit comprendre les concepts avancés.
- **Activité historique** : la persona a-t-elle des posts dans des forums parallèles ? Une présence sur Telegram ? Un historique crédible ?
- **Infrastructure cohérente** : serveur XMPP utilisé, méthodes de paiement préférées, heures d'activité.

**Construction préalable**. Une persona utilisable pour une investigation sérieuse prend **3-6 mois** à construire — inscription sur un forum, posts graduels, participation communautaire, construction d'une histoire minimale. Les personas « jetables » (créées le jour, utilisées le lendemain) sont facilement identifiables comme non-authentiques.

**Maintenance**. Une persona doit être **active** même quand pas utilisée sur une investigation active. Posts occasionnels, participation à des discussions générales. Une persona inactive pendant 6 mois puis réactivée pour une enquête ciblée déclenche la méfiance.

**Burnability**. Accepter qu'une persona peut être brûlée. En ce cas, ne pas chercher à la « sauver » — l'abandonner, en construire une nouvelle. Toute tentative de réactiver une persona suspecte aggrave l'exposition.

#### 23.3 La sécurité technique

**Tor Browser en mode Safest**. JavaScript désactivé. Beaucoup de fonctionnalités cassées, mais pas d'exécution de code exploitable. Certains sites nécessitent JS — évaluer le risque au cas par cas, activer temporairement si site considéré sûr.

**VM isolée**. Toute interaction au-delà de la simple navigation (téléchargements, fichiers exécutables) dans une VM jetable. Snapshot avant action, restauration après. Ne jamais exposer l'OS hôte à du contenu dark web non-simple-HTML.

**Pas de JavaScript actif sur sites suspects**. Les NIT (Network Investigative Techniques) et les exploits navigateur exploitent JS (Ch.30). Mode Safest le bloque ; si on l'active, on doit comprendre les risques.

**Pas de WebRTC**. Tor Browser désactive WebRTC ; ne pas l'activer manuellement. WebRTC peut leaker l'IP réelle.

**Pas de plugins**. Flash, Java, PDF readers intégrés — désactivés ou absents. Tor Browser configure ça par défaut.

**Vérification des .onion**. Les adresses .onion sont longues (56 caractères v3). Les scammers créent des adresses similaires via vanity generation. **Toujours vérifier l'adresse complète**, via source fiable (site officiel du service, post établi sur forum réputé, backup en dur pré-validé).

**Hashing des fichiers**. Tout fichier téléchargé est hashé (SHA-256 minimum) avant ouverture. Le hash sert de référence pour la chain of custody et pour vérifier que le fichier n'a pas été altéré entre collecte et analyse.

**Pas de métadonnées**. Les screenshots sont pris puis **strippés de métadonnées** (exiftool). Les documents créés pendant l'investigation (notes, rapports) ne doivent pas contenir de métadonnées personnelles (nom d'auteur dans Word, etc.).

#### 23.4 Les erreurs classiques

**Réutilisation de pseudonymes**. Un analyste qui utilise le même pseudo sur plusieurs enquêtes risque la corrélation. Les forums observent les patterns — un pseudo qui demande des échantillons de données industrielles aerospace sur un forum et des échantillons bancaires sur un autre est soit un acheteur éclectique, soit un investigateur.

**Corrélation temporelle**. Pseudo actif aux heures ouvrables françaises systématiquement. Indique fuseau horaire Europe occidentale, incompatible avec un persona prétendument russophone.

**Fuites linguistiques**. Expressions françaises dans un persona anglophone, conventions de dates françaises (DD/MM) dans un persona américain (MM/DD), traduction littérale d'idiomes français.

**Over-sharing**. Par nervosité ou tentative de crédibilité, l'analyste donne trop d'infos sur sa « persona » — détails sur son entreprise fictive, anecdotes personnelles vérifiables. Chaque détail est une surface d'attaque pour la contre-investigation.

**Accès depuis infrastructure corporate**. L'analyste qui accède à Tor depuis l'IP corporate de son bureau (même via VPN Tor) expose son organisation. Poste dédié dans un réseau isolé recommandé.

**Comptes personnels sur la machine d'investigation**. Un analyste qui check ses emails personnels sur la machine dark web compromet tout le cloisonnement.

**Documentation défaillante**. Une investigation sans logs précis de chaque action (heure, URL visitée, fichier téléchargé, hash, pseudonyme utilisé) ne produit pas de preuves utilisables.

**Abandon de prudence sur la durée**. Au début de l'enquête, OPSEC rigoureuse. Après 3 mois, fatigue, relâchement. L'erreur survient plus tard, pas au début.

#### 23.5 Le programme OPSEC d'équipe

Pour une équipe CTI, l'OPSEC doit être **institutionnelle**, pas individuelle.

**Procédures documentées**. Playbook formalisé : comment créer une persona, comment ouvrir un compte, comment gérer les paiements, comment capturer les preuves, comment documenter.

**Peer review**. Chaque action sensible (création de persona, premier contact vendeur, téléchargement d'échantillon) est validée par un pair ou la hiérarchie.

**Supervision**. Un responsable CTI a visibilité sur les investigations en cours, alloue les personas, valide les escalades.

**Formation continue**. L'OPSEC évolue (nouvelles techniques de dé-anonymisation, nouveaux pièges). Formation périodique, veille sur les techniques offensives utilisées contre les analystes.

**Incident response OPSEC**. Plan d'action en cas de compromission de persona — quoi abandonner, quoi sauvegarder, qui prévenir, comment communiquer.

**Débriefing psychologique**. Les missions longues dans l'écosystème dark web sont éprouvantes. Sessions régulières avec psychologue ou pair expérimenté.

---

### Chapitre 24 — Naviguer et collecter : méthodes, outils, limites

Aspect pratique : comment on navigue effectivement sur le dark web, quels outils on utilise, et quelles sont les limites techniques et méthodologiques.

#### 24.1 L'outillage de base

**Tor Browser** : navigateur de référence. Basé sur Firefox ESR, hardened, en mode Safest pour l'investigation. À télécharger **uniquement** depuis torproject.org (ou ses miroirs officiels).

**Tails** : distribution Linux live. Démarre sur clé USB, ne laisse aucune trace sur la machine. Recommandée pour les investigations les plus sensibles.

**Whonix** : architecture en deux VM (Gateway + Workstation). Isolation forte. Recommandée pour setup permanent d'investigation.

**Qubes OS** : système d'exploitation avec isolation par VM (AppVMs). Très sécurisé mais courbe d'apprentissage plus raide.

**VM dédiée dans VMware/VirtualBox** : alternative accessible si Whonix est trop lourd. Clone de l'OS avant chaque session, restauration post-session.

**Outils complémentaires** :
- **curl / wget via Tor** (torify) : récupération en ligne de commande.
- **OnionScan** : audit automatique de services .onion pour failles OPSEC.
- **tsocks / proxychains** : chaînage de proxies.
- **Aquatone, Eyewitness** : capture automatisée de screenshots en masse.
- **Hunchly** : outil commercial de capture structurée d'investigation (horodatage, archivage, notes).
- **Maltego** : graphing des relations entre entités (avec transformations spécifiques dark web).

#### 24.2 Les sources et points d'entrée

**Comment trouve-t-on des .onion** ?

**Listes communautaires**. The Hidden Wiki (multiple instances, pas toutes fiables), Dark.fail, Tor.taxi. Ces listes sont **partielles et partiellement scam-compromised** — ne jamais cliquer aveuglément.

**Moteurs de recherche .onion**. Ahmia, Torch, Haystak, Excavator. Indexation **très partielle** du contenu .onion. Utile pour des recherches spécifiques, mais rarement exhaustif.

**Cross-references depuis forums**. Les forums mentionnent d'autres forums, marchés, canaux. Documentation par ce biais — plus fiable que les listes car vouchées par la communauté.

**Canaux Telegram**. Beaucoup d'acteurs postent leurs adresses .onion sur Telegram, ce qui les rend plus facilement découvrables. Surveiller les canaux pertinents.

**Services de monitoring commerciaux**. Recorded Future, SOCRadar, Flashpoint, Flare, Intel471, DarkOwl, Cybersixgill — tous maintiennent des bases d'entités dark web crawlées. Accès via abonnement entreprise.

**OSINT public**. Articles de presse, papers académiques, rapports vendors — regorgent de mentions d'adresses .onion qui ont fait l'actualité.

#### 24.3 La collecte structurée

**Capture vs simple navigation**. La collecte doit être **structurée**, pas simple navigation. Capturer systématiquement :
- **URL complète** visitée.
- **Horodatage précis** (timestamp avec seconde, fuseau horaire).
- **Capture d'écran** du contenu.
- **HTML source** sauvegardé.
- **Hash** du contenu sauvegardé.
- **Pseudonyme utilisé** pour la session.

**Archivage**. Plusieurs options :
- **Hunchly** : outil commercial qui automatise capture + organisation + horodatage.
- **Archivage manuel** : dossiers structurés, nommage convention (YYYYMMDD-HHMMSS-source-description), fichiers immutables.
- **Container cryptographiquement signé** : après collecte, générer un hash global du dossier, horodater, signer (GPG), stocker en immutable.

**Organisation**. Par cas d'investigation, par source, par date. Éviter le « one big folder » — impossible à remonter après 6 mois.

#### 24.4 Les challenges techniques

**Lenteur du réseau Tor**. Navigation 5-10× plus lente que clearnet. Planifier des sessions d'investigation longues, éviter la multitâche excessive.

**Disponibilité intermittente des .onion**. Un site .onion peut être down pour heures ou jours. Tenter plusieurs fois, utiliser des mirrors (si connus), noter les patterns de disponibilité.

**DDoS permanents**. Les grands forums sont régulièrement DDoSés. Les pages chargent lentement, partiellement, ou pas du tout. Les meilleures heures d'investigation sont souvent les créneaux nocturnes (fuseau horaire attaquant).

**CAPTCHA pervasifs**. Pour limiter le scraping, beaucoup de sites .onion implémentent CAPTCHAs difficiles, parfois impossibles pour des outils automatisés.

**Protections anti-scraping**. Limites de requêtes, défis JS, tokens de session, fingerprinting — rendent la collecte automatisée complexe.

**Sites éphémères**. Un forum peut déménager d'adresse .onion sans préavis. Une capture d'il y a 6 mois peut pointer vers un site disparu. Les archives ont donc une valeur disproportionnée sur le dark web.

#### 24.5 Les limites méthodologiques

**Biais de survivance**. Ce qu'on observe est ce qui existe actuellement. Les acteurs qui disparaissent ne sont plus observables. Les forums saisis ne sont plus accessibles (sauf archives). L'image du dark web à un instant T est partielle et biaisée vers les survivants.

**Biais de visibilité**. Les acteurs les plus sophistiqués sont souvent les moins visibles. Un APT étatique n'a pas besoin d'un leak site flashy — il opère discrètement. Les acteurs observables sur forums publics sont majoritairement de profil intermédiaire.

**Biais de représentation**. L'analyste observe à travers les forums qu'il connaît. L'écosystème russophone, chinois, arabophone, persan ont chacun leurs dynamiques propres, partiellement accessibles selon les compétences linguistiques de l'équipe.

**Biais de fraîcheur**. Les données anciennes disparaissent. Un forum actif il y a 2 ans peut être invisible aujourd'hui. L'histoire du dark web est partiellement perdue.

**Biais d'accès**. Les zones premium des forums (souvent les plus intéressantes analytiquement) nécessitent paiement, vouching, tenure. Un analyste privé n'a pas toujours les moyens d'accéder à toutes les zones utiles.

#### 24.6 Automatisation et échelle

**Scraping automatisé** : possible mais difficile. Les protections anti-bot sont fortes. Nécessite infrastructure (plusieurs instances Tor, rotation d'identités), résilience (retry logic, gestion erreurs), légalité (certains ToS interdisent scraping même sur sites criminels).

**Plateformes commerciales** : outils SaaS qui font le crawling à grande échelle et exposent les résultats via API. Recorded Future, DarkOwl, Flare, Intel471, Cybersixgill. Coût : 50 k - 500 k USD/an selon scale.

**Open source** : quelques projets open source (OnionScan, TorBot, Dark-Scrape) mais moins robustes que solutions commerciales.

**Approche hybride** : scraping ciblé sur sources prioritaires + plateforme commerciale pour couverture large + veille humaine pour les signaux faibles.

#### 24.7 Fil rouge — DARKSTREAM : l'accès à IndustrialLeaks

> **🌐 DARKSTREAM — Épisode 13 : setup et navigation**
>
> Lucas utilise son environnement Whonix avec Tor Browser Safest. Accès initial à IndustrialLeaks via l'adresse .onion communiquée par le partenaire vouching. Vérification de l'adresse : 56 caractères, cross-check sur 2 sources indépendantes (mention dans un post Recorded Future + mention sur un forum russophone peer).
>
> Navigation lente — 2-3 secondes par clic. Le forum affiche un CAPTCHA proof-of-work (JS requis à minima pour le CAPTCHA). Lucas active JS **uniquement pour la page de login**, puis le désactive après. Session de navigation active, avec Hunchly en background pour capture systématique.
>
> Exploration structurée :
> 1. Captures de toutes les catégories publiques (arborescence du forum).
> 2. Lecture et capture du post aero_source + tous les posts du même user.
> 3. Navigation aux autres vendeurs du mois, pour profiling comparatif.
> 4. Règles du forum (capture).
> 5. Statistiques visibles (nombre de membres, posts, transactions).
>
> Cycle de 3 heures. 147 pages capturées, structurées par dossier. Hash du corpus calculé. Persona « mapletech » affiche activité cohérente (quelques réponses en threads, aucun message offensif, aucune tentative de solliciter info sensible au-delà de ce qui est publiquement affiché).
>
> Post-session, Lucas produit un **mémo d'observations** : architecture du forum, profils de vendeurs actifs, posts d'intérêt, observations sur aero_source. Ce mémo alimente le dossier DARKSTREAM et permet aux autres membres de l'équipe Athéna d'orienter leurs propres recherches sans re-naviguer manuellement.