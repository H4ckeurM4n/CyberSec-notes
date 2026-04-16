# LE DARK WEB — COMPRENDRE, NAVIGUER, INVESTIGUER

*Architecture • Écosystèmes • OPSEC • Investigation • Renseignement*

**Cours complet — 44 chapitres • 8 parties • 7 annexes**

---

## Table des matières

- [Fil rouge : Opération DARKSTREAM](#fil-rouge--opération-darkstream)
- **PARTIE I — FONDATIONS (Ch.1-4)**
- **PARTIE II — INFRASTRUCTURES TECHNIQUES ET ANONYMAT (Ch.5-9)**
- **PARTIE III — ÉCOSYSTÈMES DU DARK WEB (Ch.10-17)**
- **PARTIE IV — ÉCONOMIE CLANDESTINE (Ch.18-21)**
- **PARTIE V — INVESTIGATION, VEILLE ET COLLECTE (Ch.22-28)**
- **PARTIE VI — ANALYSE, RENSEIGNEMENT ET PRODUCTION (Ch.29-35)**
- **PARTIE VII — CAS D'USAGE, TENDANCES ET PROSPECTIVE (Ch.36-40)**
- **PARTIE VIII — ÉTUDES DE CAS ET SYNTHÈSE (Ch.41-44)**
- **ANNEXES (A-G)**

---

## Fil rouge : Opération DARKSTREAM

> **Lucas Ferreira**, analyste CTI senior chez **Athéna Group**, reçoit un mandat de **Vectris Aerospace** (équipementier aérospatial, 4 500 collaborateurs, SBF 120). Vectris a subi une exfiltration de 420 Go de données techniques classifiées. Le mandat : identifier si les données circulent sur le dark web, évaluer l'authenticité, cartographier l'écosystème de la vente, et produire un rapport actionnable pour Vectris et la DGSI.

---

## PARTIE I — FONDATIONS : COMPRENDRE LE DARK WEB

---

### Chapitre 1 — Internet, web visible, deep web, dark web : remettre les mots à l'endroit

#### 1.1 Internet n'est pas le web

La confusion commence ici. **Internet** est le réseau physique mondial — un ensemble de câbles sous-marins, de fibres optiques, de routeurs, et de protocoles (TCP/IP) qui relient des milliards de machines. Internet transporte de l'email, du streaming vidéo, du trafic VPN, des requêtes DNS, du pair-à-pair, et bien d'autres choses. Le **web** (World Wide Web) est un service qui fonctionne sur Internet, basé sur le protocole HTTP/HTTPS et le langage HTML — c'est ce qu'on consulte avec un navigateur. Le web n'est qu'une partie d'Internet — une partie importante, certes, mais pas la totalité. Confondre Internet et web, c'est confondre le réseau routier et les magasins qu'on peut atteindre en voiture.

#### 1.2 Les trois couches du web

Le **surface web** (ou clearnet) est l'ensemble des pages web indexées par les moteurs de recherche (Google, Bing, Yandex). En termes de volume, le surface web représente entre 5 et 10 % du contenu web total.

Le **deep web** est l'ensemble des contenus web non indexés par les moteurs de recherche. C'est la couche la plus vaste et la plus banale : intranets d'entreprise, bases de données académiques, contenu derrière authentification (compte bancaire, email, factures), archives non indexées, pages dynamiques. Le deep web représente environ 90 % du contenu web. La quasi-totalité est parfaitement légale. Quand on parle du deep web, on ne parle PAS de cybercriminalité — on parle de tout ce que Google ne voit pas.

Le **dark web** est un sous-ensemble du deep web, accessible uniquement via des réseaux d'anonymisation spécifiques — principalement Tor (sites `.onion`), mais aussi I2P (eepsites), Freenet, et d'autres darknets. Le dark web n'est pas simplement « non indexé » — il est volontairement caché, hébergé sur des infrastructures d'anonymisation qui masquent l'identité du serveur et du visiteur. En volume, le dark web est une fraction minuscule d'Internet : quelques centaines de milliers de domaines .onion, dont la majorité sont inactifs, abandonnés, ou dupliqués.

#### 1.3 Darknets vs dark web

Un **darknet** est un réseau overlay (superposé à Internet) conçu pour l'anonymat : Tor est un darknet, I2P est un darknet, Freenet est un darknet. Le dark web est l'ensemble des contenus accessibles via ces darknets. La distinction est technique mais utile : on peut accéder au réseau Tor sans visiter de site .onion (simplement en utilisant Tor comme proxy pour naviguer sur le web classique de manière anonyme), et on peut visiter un site .onion uniquement si on utilise le réseau Tor.

#### 1.4 Pourquoi le terme « dark web » est souvent mal utilisé

Les médias utilisent « dark web » comme synonyme de « cybercriminalité ». Cette confusion est dommageable pour trois raisons. Elle surestime le dark web comme espace criminel — beaucoup d'activité cybercriminelle se déroule sur le clear web (forums à accès restreint, Telegram, Discord, pastebins). Elle sous-estime les usages légitimes — contournement de censure, protection des sources, communication sécurisée. Et elle crée une fascination sensationnaliste qui obscurcit la réalité : le dark web est un espace relativement petit, souvent lent, fréquemment en panne, et rempli d'arnaques.

La frontière entre dark web et clear web est de plus en plus poreuse. Des plateformes criminelles majeures comme Genesis Market ou RaidForums opéraient sur le web de surface. Et inversement, des organisations parfaitement légitimes (le New York Times, la BBC, Facebook) maintiennent des miroirs .onion.

#### 1.5 Ordres de grandeur

Les mesures du Tor Project comptent en 2025-2026 environ 800 000 adresses .onion v3 uniques observées, dont 10-30 % sont actives à un moment donné. Parmi les sites actifs, environ 50-60 % sont légitimes, miroirs ou abandonnés ; 20-30 % sont des arnaques ; 10-20 % hébergent du contenu illicite. Le CRS (Congrès US) estimait en 2015 qu'environ 3,4 % seulement des utilisateurs de Tor visitaient des hidden services — la majorité des 8 millions d'utilisateurs quotidiens utilisent Tor pour naviguer sur le web classique de manière anonyme. (Source : Tor Metrics https://metrics.torproject.org/hidserv-dir-v3-onions-seen.html?start=2025-01-15&end=2026-04-15)

#### 1.6 Fil rouge — DARKSTREAM : le point de départ

> **🌐 DARKSTREAM — Épisode 1**
>
> Lucas reçoit le brief de Vectris Aerospace. Les données techniques exfiltrées auraient été repérées sur un forum .onion russophone spécialisé dans les données industrielles. L'information vient d'un service de monitoring dark web (Recorded Future), qui a détecté une mention de « Vectris » et de « propulsion specs ». Première tâche : vérifier l'information. Les alertes de monitoring dark web sont fréquemment des faux positifs.

---

### Chapitre 2 — Histoire et évolution des darknets

#### 2.1 Les origines : anonymat et recherche militaire

Dans les années 1990, le **Naval Research Laboratory** (NRL) développe l'onion routing comme technique de protection des communications de renseignement. En 2002, Roger Dingledine, Nick Mathewson, et Paul Syverson lancent le **Tor Project** — implémentation open source de l'onion routing. Le paradoxe fondamental : un réseau d'anonymat ne fonctionne que si suffisamment de personnes l'utilisent. Si seuls les agents de renseignement utilisent Tor, tout le trafic est attribuable. Le gouvernement américain finance Tor tout en cherchant à le compromettre quand il est utilisé à des fins criminelles.

#### 2.2 L'ère Silk Road (2011-2013)

**Silk Road**, créé par Ross Ulbricht (alias « Dread Pirate Roberts »), est le premier darknet market généraliste significatif. Lancé en février 2011, il combine Tor et Bitcoin dans un modèle d'e-commerce clandestin inspiré d'eBay. Silk Road atteint environ 1,2 million de transactions avant sa saisie par le FBI en octobre 2013, avec plus de 150 000 personnes impliquées dans les transactions et plus de 4 000 vendeurs. Ulbricht est identifié via des erreurs OPSEC : un post sur StackOverflow avec son vrai email, un pseudonyme relié à son identité réelle, et un serveur CAPTCHA qui a leaké l'IP du serveur.

#### 2.3 La professionnalisation (2014-2019)

**AlphaBay** (2014-2017, opéré par Alexandre Cazes) devient le plus grand darknet market de l'histoire, Le DOJ parle de plus de 250 000 listings de drogues et produits chimiques toxiques, auxquels s’ajoutaient plus de 100 000 listings pour faux documents, accès frauduleux, malwares, armes, etc. Sa saisie en juillet 2017 (Operation Bayonet) est couplée avec l'infiltration de **Hansa Market** par la police néerlandaise — les utilisateurs fuyant AlphaBay vers Hansa tombent dans un piège policier opéré pendant 30 jours.

#### 2.4 Hydra et la domination russophone (2015-2022)

**Hydra Market** (2015-2022) — Le DOJ indique qu’Hydra a reçu environ 5,2 milliards de dollars en cryptomonnaies depuis 2015 et représentait environ 80 % des transactions crypto liées aux darknet markets en 2021. Opéré exclusivement en russe, avec un système de « dead drops » physiques unique. Sa saisie par les autorités allemandes en avril 2022 crée une fragmentation de l'écosystème russophone.

#### 2.5 L'ère post-Hydra et les tendances 2024-2026

L'écosystème se fragmente : marchés spécialisés remplacent les marchés généralistes. Telegram émerge comme concurrent direct (plus accessible mais moins anonyme, avec une modération plus agressive après l'arrestation de Pavel Durov en août 2024). L'évolution majeure de 2025-2026 : le glissement du vecteur d'accès initial. Les attaquants achètent des credentials valides sur le dark web via des stealer logs à prix dérisoire (dès 15 $) plutôt que de développer des exploits sophistiqués. Le dark web est devenu le supermarché de l'accès initial.

#### 2.6 Fil rouge — DARKSTREAM : le forum ciblé

> **🌐 DARKSTREAM — Épisode 2**
>
> Le forum identifié est **IndustrialLeaks**, un forum .onion russophone créé en 2022, spécialisé dans les données industrielles. Environ 3 000 membres enregistrés. Accès par vouching ou paiement de 0,005 BTC. 3 changements d'adresse .onion en 18 mois. Miroir I2P disponible.

---

### Chapitre 3 — Pourquoi le dark web existe

#### 3.1 L'anonymat comme besoin fondamental

La **résistance à la censure** : dans les régimes autoritaires (Chine, Iran, Russie, Biélorussie, Myanmar), Tor permet d'accéder à Wikipedia, à des médias indépendants, et à des réseaux sociaux bloqués. Reporters Sans Frontières opère des miroirs .onion. Le Tor Project développe des bridges et des pluggable transports pour contourner le DPI des censeurs.

La **protection des sources journalistiques** : **SecureDrop** (déployée par le NYT, le Guardian, Le Monde, ProPublica), **AfriLeaks** pour les lanceurs d'alerte africains. Les affaires WikiLeaks, Panama Papers, et LuxLeaks n'auraient pas été possibles sans des canaux anonymes.

La **vie privée comme droit fondamental** : article 8 de la CEDH, article 12 de la DUDH. L'anonymat en ligne est un instrument de ces droits.

#### 3.2 L'anonymat comme facilitateur criminel

Le dark web offre aux acteurs malveillants un espace où l'identification est difficile, les transactions sont pseudonymes (Bitcoin) ou anonymes (Monero), et l'infrastructure est résistante aux saisies. Le dark web n'est ni un repaire de super-criminels ni un simple outil de liberté — l'anonymat est moralement neutre, c'est l'usage qui est qualifiable.

#### 3.3 La tension fondamentale

Le rapport de l'EPRS (2026) souligne que la nature anonyme du dark web rend toute régulation extrêmement difficile. La création de l'European Cybercrime Centre (EC3) par Europol en 2013 et du J-CAT en 2014 sont des réponses institutionnelles. Les débats sur le chiffrement en Europe (proposition « Chat Control ») illustrent la tension entre sécurité publique et vie privée. L'analyste CTI se situe au milieu de cette tension.

---

### Chapitre 4 — Le dark web comme écosystème

#### 4.1 Au-delà du « site caché »

Le dark web est un écosystème interconnecté avec ses communautés, ses marchés, ses intermédiaires, ses règles sociales, et ses dynamiques de pouvoir. L'écosystème comprend des **espaces** (forums, marchés, leak sites, canaux de communication), des **acteurs** (vendeurs, acheteurs, opérateurs, modérateurs, escrocs), des **mécanismes de confiance** (réputation, escrow, vouching), des **flux financiers** (crypto, mixing, blanchiment), et des **dépendances techniques** (hébergement, réseau Tor). Chaque composante est interdépendante.

#### 4.2 Les interactions entre le dark web et les autres espaces

Le dark web interagit constamment avec le surface web (promotion sur Telegram et Discord), les réseaux sociaux (revendications de ransomware relayées sur X), les écosystèmes crypto (exchanges clear web), et le monde physique (dead drops Hydra, livraisons postales). Le phénomène d'« uberisation » des marchés illicites illustre cette porosité croissante entre espaces.

#### 4.3 Les limites du dark web comme source de renseignement

Le dark web est une source précieuse mais partielle et biaisée. Ce qui est visible n'est pas représentatif de l'ensemble de l'activité criminelle. Les forums les plus fermés ne sont pas indexés. Les données publiées ne sont pas nécessairement fiables. « L'absence de données Vectris sur les forums observés ne signifie pas l'absence de circulation — elle signifie l'absence de visibilité dans le périmètre de cette investigation. »

#### 4.4 Fil rouge — DARKSTREAM : cartographier l'écosystème

> **🌐 DARKSTREAM — Épisode 3**
>
> Lucas cartographie l'écosystème : « aero_source » est actif sur IndustrialLeaks (forum .onion), un canal Telegram privé, et XSS (forum russophone de référence). 3 espaces à surveiller en parallèle. C'est un écosystème, pas un site isolé.

---

## PARTIE II — INFRASTRUCTURES TECHNIQUES ET ANONYMAT

---

### Chapitre 5 — Architecture de Tor

#### 5.1 L'onion routing en détail

Le client Tor construit un **circuit** à travers 3 relais minimum. Le message est chiffré en 3 couches successives. Le guard node déchiffre la couche extérieure et découvre l'adresse du second relais, sans connaître la destination. Le middle relay déchiffre la couche suivante sans connaître ni l'émetteur ni la destination. L'exit node déchiffre la dernière couche et envoie le trafic vers la destination, sans connaître l'émetteur. Résultat : aucun relais isolé ne dispose de suffisamment d'information pour relier l'utilisateur à sa destination.

#### 5.2 Les types de nœuds

Les **guard nodes** (entry guards) voient l'IP réelle de l'utilisateur — position la plus critique. Le client Tor utilise un petit nombre de guards stables sur une longue période. Les **middle relays** sont les plus nombreux et les moins critiques — ils voient uniquement le relais précédent et le suivant. Les **exit nodes** voient le trafic en clair si la destination n'utilise pas HTTPS (en 2026, la quasi-totalité du web utilise HTTPS). Les **bridge nodes** sont des relais non listés publiquement, utilisés pour contourner la censure. Les **pluggable transports** (obfs4, Snowflake, meek) déguisent le trafic Tor en trafic ordinaire. Les **directory authorities** (9 serveurs) maintiennent le consensus sur l'état du réseau, mis à jour toutes les heures.

#### 5.3 Ce que Tor protège et ce qu'il ne protège pas

**Tor protège** contre la surveillance du réseau local, contre la surveillance par le site de destination, et contre l'analyse de trafic simple.

**Tor ne protège PAS** contre un adversaire global qui surveille à la fois le guard et l'exit (corrélation de trafic — considérée comme réalisable par les agences de renseignement, notamment via le programme XKeyscore de la NSA qui aurait « fingerprinted » automatiquement les utilisateurs tentant de télécharger Tor), contre les vulnérabilités du navigateur (le FBI a utilisé des exploits Firefox pour révéler des IP réelles), contre les erreurs utilisateur (connexion à un compte personnel via Tor, téléchargement hors Tor), et contre le trafic des applications non-Tor (seul le Tor Browser route son trafic via Tor, sauf configuration Whonix/Tails).

#### 5.4 Métriques du réseau Tor

En 2025-2026 : environ 10 000 relais actifs dont ~3 000 exit nodes, bande passante ~800 Gbit/s, 8 millions d'utilisateurs/jour. Principaux pays d'utilisateurs : États-Unis, Russie, Allemagne, Inde, Iran. La part accédant aux hidden services : environ 3-6 % du trafic total. (Source Tor Metrics https://metrics.torproject.org/ & https://metrics.torproject.org/relayflags.html & https://metrics.torproject.org/bandwidth.html)

---

### Chapitre 6 — Onion services et services cachés

#### 6.1 Le principe des onion services

Un **onion service** est un serveur accessible exclusivement via Tor, identifié par une adresse `.onion`. Le serveur est aussi anonyme que le client. Le mécanisme fonctionne via un système de rendez-vous : le serveur crée des **introduction points** et publie leur adresse dans la DHT. Le client propose un **rendezvous point** via l'introduction point. Les deux parties communiquent via le rendezvous point — 6 relais au total.

#### 6.2 Adresses v2 et v3

Les adresses v2 (16 caractères, RSA-1024) sont obsolètes depuis octobre 2021. Les adresses **v3** (56 caractères, ed25519) offrent un chiffrement plus robuste et une résistance aux attaques par énumération. Les **vanity addresses** (préfixe personnalisé) sont générées par force brute — coût exponentiel au-delà de 10 caractères.

#### 6.3 Fragilités des onion services

Les **fuites d'IP** par mauvaise configuration sont la cause la plus fréquente de compromission : IP réelle dans un header HTTP, certificat SSL contenant le domaine, service compagnon écoutant sur l'IP publique, script faisant des requêtes DNS hors Tor. L'outil **OnionScan** détecte automatiquement ces fuites. Les forces de l'ordre exploitent systématiquement ces erreurs de configuration — c'est le vecteur principal d'identification des opérateurs de hidden services.

---

### Chapitre 7 — I2P, Freenet et réseaux alternatifs

#### 7.1 I2P (Invisible Internet Project)

I2P utilise le **garlic routing** — les messages sont encapsulés en « gousses d'ail » contenant plusieurs messages chiffrés, rendant la corrélation plus difficile. Architecture unidirectionnelle : tunnels d'envoi et de réception séparés. Services : messagerie (I2P-Bote, SusiMail), torrents (I2PSnark), forums (Syndie). Communauté plus petite que Tor (~30 000 nœuds) mais considérée par certains acteurs comme « moins surveillée ».

#### 7.2 Freenet

Réseau de stockage distribué et chiffré. Le contenu est fragmenté et chiffré — aucun nœud ne sait quel contenu il héberge. Deux modes : **opennet** (plus facile, moins sûr) et **darknet** (pairs de confiance uniquement). Les freesites sont statiques, ce qui limite les usages mais maximise la résistance à la censure.

#### 7.3 Réseaux émergents et messageries anonymes

**Lokinet** (LLARP, blockchain pour le registre de nœuds), **ZeroNet** (Bitcoin + BitTorrent), **Yggdrasil** (mesh chiffré IPv6), **IPFS** (stockage décentralisé utilisé pour la résilience aux takedowns). Messageries anonymes : **Tox** (P2P chiffré, canal de contact principal sur les forums russophones), **Session** (réseau Lokinet), **Briar** (fonctionne via Tor, WiFi direct, ou Bluetooth), **Ricochet Refresh** (chaque utilisateur est un hidden service), et **IRC sur Tor**.

#### 7.4 Comparaison technique

| Critère | Tor                                      | I2P | Freenet |
| ------------------------ | ---------------------------------------- | -------------------------------------------- | ----------------------------------- |
| Modèle de routage | Onion routing (circuits)                 | Garlic routing (tunnels unidirectionnels) | Stockage distribué |
| Usage principal | Navigation web anonyme + hidden services | Communication interne (eepsites, messagerie) | Publication résistante à la censure |
| Accès au web classique | Oui (exit nodes)                         | Limité (outproxies rares) | Non |
| Taille du réseau | ~10 000 relais, 8M utilisateurs/jour     | ~30 000 nœuds | ~5 000-10 000 nœuds |
| Latence | Moyenne (1-5s)                           | Moyenne à élevée | Élevée (minutes) |
| Contournement de censure | Oui (bridges, pluggable transports)      | Limité | Limité |

---

### Chapitre 8 — Cryptomonnaies et anonymat financier

#### 8.1 Bitcoin : pseudo-anonyme, pas anonyme

La blockchain Bitcoin est un registre public. Le pseudo-anonymat vient du fait que les adresses ne sont pas liées à une identité nominative par défaut. Mais les techniques de **blockchain analysis** (clustering d'adresses, identification des services connus, exploitation des exchanges KYC) permettent de remonter à des identités. Bitcoin est le moyen de paiement historique du dark web, mais sa traçabilité pousse les acteurs sophistiqués vers Monero. Renvoi au Ch.31 pour le détail du traçage.

#### 8.2 Monero (XMR) : la privacy coin dominante

Trois mécanismes de confidentialité : **ring signatures** (émetteur ambigu parmi un groupe), **stealth addresses** (adresses à usage unique), **RingCT** (montants masqués). En 2025-2026, Monero est considéré comme résistant au traçage pour les adversaires non étatiques.

#### 8.3 Services de mixing et d'obfuscation

Les mixers centralisés massivement saisis (Chipmixer mars 2023, Sinbad novembre 2023, Tornado Cash sanctionné OFAC août 2022). Les protocoles décentralisés (**CoinJoin**, **JoinMarket** — toujours actif). Les **atomic swaps** (échange direct Bitcoin↔Monero sans intermédiaire) sont une technique émergente.

#### 8.4 OPSEC financière sur le dark web

Ne jamais réutiliser un wallet entre activités, utiliser Monero pour les transactions sensibles, utiliser des wallets non custodial, gérer les change addresses correctement sur Bitcoin, ne jamais convertir directement via un exchange KYC lié à son identité réelle.

#### 8.5 Fil rouge — DARKSTREAM : le paiement d'accès

> **🌐 DARKSTREAM — Épisode 4**
>
> Pour accéder à IndustrialLeaks, Lucas doit payer 0,005 BTC (~180 €). Question juridique : un analyste privé peut-il payer pour accéder à un forum cybercriminel ? Lucas consulte le directeur juridique d'Athéna Group (détaillé au Ch.22). Le paiement est autorisé dans le cadre du mandat client, documenté dans le journal de collecte.

---

### Chapitre 9 — Hébergement, infrastructure et résilience des services clandestins

#### 9.1 Hébergement bulletproof

Les services du dark web nécessitent un hébergement qui ne répond pas aux plaintes d'abus. Certains opérateurs auto-hébergent dans des juridictions non coopératives. D'autres utilisent des services cloud légitimes (AWS, OVH, Hetzner) en masquant l'usage réel par des couches de misdirection.

#### 9.2 Résilience et fragilité

Techniques de résilience : **mirroring** (plusieurs domaines .onion et eepsites I2P), load balancing distribué, **dead man's switches**, backup automatisé. Points de défaillance : l'opérateur humain (identifiable par erreur OPSEC), l'infrastructure physique (saisissable), la clé privée du hidden service (single point of failure).

Le **DDoS** est endémique sur le dark web — marchés et forums sont régulièrement victimes d'attaques lancées par des concurrents, des extorqueurs, ou des forces de l'ordre. L'instabilité chronique (pages qui ne chargent pas, erreurs de connexion) est en partie due aux DDoS et en partie à l'architecture de Tor (6 relais = latence élevée).

#### 9.3 Fil rouge — DARKSTREAM : l'infrastructure d'IndustrialLeaks

> **🌐 DARKSTREAM — Épisode 5**
>
> IndustrialLeaks : 3 changements d'adresse .onion en 18 mois (DDoS probables). Miroir I2P. Captcha proof-of-work. Moteur personnalisé (pas un CMS standard — signe de compétences de développement). Temps de réponse 3-8 secondes. Actif depuis 4 ans — longévité remarquable.

---

## PARTIE III — ÉCOSYSTÈMES DU DARK WEB : ESPACES, ACTEURS ET CULTURE

---

### Chapitre 10 — Forums clandestins : culture, hiérarchie et codes

#### 10.1 La sociologie des forums underground

Les forums du dark web ne sont pas de simples places de marché — ce sont des communautés structurées avec leur propre culture, leurs codes sociaux, et leur gouvernance informelle. La **hiérarchie** est informelle mais rigide : administrateurs (pouvoir quasi absolu), modérateurs (application des règles, arbitrage), vendeurs vérifiés (« verified vendors » — aristocratie marchande), membres ordinaires, et lurkers (observateurs silencieux, suspects sur les forums fermés car indicateur d'infiltration).

#### 10.2 Forums russophones vs anglophones

Deux écosystèmes distincts. Les **forums russophones** (XSS, Exploit, RAMP) : fermés (accès par vouching ou paiement élevé — 500 à 5 000 $ pour un compte sur Exploit), techniquement sophistiqués, disciplinés (interdiction de cibler les pays de la CEI, interdiction des scams entre membres). Les **forums anglophones** (BreachForums et successeurs, Cracked, Nulled) : plus ouverts, plus accessibles, qualité plus variable, plus de bruit et de scams.

#### 10.3 Les codes sociaux

Ne pas cibler les pays de la CEI (quasi universelle sur les forums russophones), ne pas arnaquer les membres du forum (la confiance intra-communautaire est sacrée), ne pas coopérer avec les forces de l'ordre (le « snitching » est le péché capital), et ne pas discuter de CSAM (interdit explicitement par pragmatisme — attire l'attention disproportionnée des autorités).

Un phénomène émergent documenté par Cyberint : certains membres de la Gen Z se tournent vers la cybercriminalité pour la validation sociale. Des plateformes comme Twitter et Discord sont utilisées pour afficher leurs exploits et gagner en reconnaissance dans la communauté hacking — brouillant la frontière entre culture internet et activité criminelle.

---

### Chapitre 11 — Marchés du dark web : histoire, fonctionnement et évolution

#### 11.1 De Silk Road à l'ère post-Hydra

L'histoire des darknet markets est une succession de cycles : création → croissance → saisie/exit scam → migration. La résilience de l'écosystème tient à la demande (acheteurs et vendeurs existent indépendamment des plateformes) et à la faible barrière technique.

#### 11.2 Fonctionnement d'un darknet market

Modèle marketplace : commission de 2-5 % par transaction, frais de listing, frais d'inscription. **Escrow** : le marché retient les fonds jusqu'à confirmation de réception. **Système de réputation** : ratings, reviews, volume, ancienneté. Un profil avec 200+ transactions réussies et 3 ans d'ancienneté peut valoir 5 000-20 000 $.

#### 11.3 Ce qui se vend — cartographie factuelle

Les **stupéfiants** restent la catégorie dominante en volume. Les **données volées** sont la catégorie la plus pertinente pour les analystes CTI (détaillées aux Ch.14-15). Les **services cybercriminels** (Ch.16-17). Les **documents contrefaits** (qualité variable, souvent des scams). Les **armes** (marché plus petit que ce que les médias suggèrent, taux de scam très élevé). Les **médicaments** (y compris contrefaits et substances contrôlées).

#### 11.4 L'évolution 2024-2026

Fragmentation post-Hydra, spécialisation croissante, montée de Telegram, pression réglementaire sur les exchanges crypto. Les marchés qui survivent investissent dans la sécurité, la modération, et la résistance au DDoS.

---

### Chapitre 12 — Leak sites, blogs d'extorsion et vitrines de revendication

#### 12.1 Les leak sites de ransomware

Sites .onion opérés par les groupes de ransomware pour publier les données des victimes qui refusent de payer. Fonction triple : **pression** (« payez ou vos données sont publiées »), **marketing** criminel (démontrer la crédibilité), **preuve de compromission**.

#### 12.2 Structure et fonctionnement

Chaque victime a sa propre page : nom de l'organisation, description de l'attaque, échantillon de données, compte à rebours (7-14 jours), lien vers le portail de négociation. Après expiration, publication intégrale en archives téléchargeables.

#### 12.3 Narration et communication criminelle

Certains groupes publient des « communiqués de presse », contactent directement les journalistes, développent des « programmes de bug bounty » (LockBit). Cette communication sert un objectif commercial : plus la menace est crédible, plus les futures victimes sont incitées à payer.

#### 12.4 Le monitoring des leak sites pour le CTI

La surveillance révèle les cibles (secteurs, pays, taille), les volumes (victimes par mois, par groupe), les patterns, et les TTP. Outils de monitoring : Ransomwatch, Ransomfeed, plateformes commerciales. Renvoi au Ch.36 pour le détail opérationnel.

---

### Chapitre 13 — Canaux, chats et messageries clandestines

#### 13.1 Telegram comme extension du dark web

Depuis 2020-2021, principal concurrent du dark web pour le commerce cybercriminel. Avantages : accessibilité, rapidité, audience, fonctionnalités (bots, channels). Inconvénients : dépendance envers Telegram (fermeture de canaux plus agressive post-Durov août 2024), moins d'anonymat (numéro de téléphone requis, métadonnées accessibles, réquisitions possibles), pas d'escrow intégré.

#### 13.2 Les autres canaux

**Jabber/XMPP** (avec OTR ou OMEMO) : le plus utilisé par les acteurs sophistiqués. **Tox** : P2P chiffré, canal de contact principal sur les forums russophones. **Matrix** : protocole décentralisé, certaines communautés techniques. **IRC sur Tor** : historique, en déclin.

#### 13.3 La fragmentation des communications

Tendance 2024-2026 : les acteurs utilisent simultanément plusieurs canaux (forum .onion pour l'annonce, Telegram pour la promotion, Tox/Jabber pour la négociation, marché .onion pour la transaction). L'analyste qui ne surveille qu'un seul canal rate la majorité de l'activité. La corrélation entre canaux est une technique d'investigation fondamentale (Ch.26).

---

### Chapitre 14 — Données volées et marchés de la fuite

#### 14.1 Types de données en circulation

Les **credentials** (couples email/mot de passe issus de breaches) : vendus en bulk (combo lists de millions d'entrées pour quelques dollars) ou au détail (5-50 $ pièce). Les **logs d'infostealers** : sessions complètes avec credentials, cookies, données machine (détaillés au Ch.15). Les **données bancaires** : numéros de carte, CVV, accès aux comptes. Les **données personnelles** (fullz : nom, adresse, SSN/NIR, date de naissance, documents d'identité). Les **données d'entreprise** : documents internes, propriété intellectuelle, emails, bases clients. Les **données de santé** : dossiers médicaux, très prisés pour la fraude à l'assurance (US).

**Grille de prix indicative 2025 (source SOCRadar) :**

| Type de donnée | Prix indicatif |
|---------------|---------------|
| Combo list (millions d'entrées) | 5-50 $ |
| Credentials vérifiés (service spécifique) | 5-50 $/pièce |
| Carte bancaire (avec CVV) | 5-30 $ |
| Carte bancaire (avec PIN/accès complet) | 30-150 $ |
| Compte PayPal/Venmo vérifié | 20-200 $ |
| Fullz (identité complète) | 10-70 $ |
| Documents contrefaits (passeport, permis) | 20-150 $ |
| Log d'infostealer (basique) | 1-15 $ |
| Log d'infostealer (avec VPN corporate) | 50-500 $ |
| Accès VPN/RDP corporate (IAB) | 500-50 000 $ |
| Base de données d'entreprise | 500-100 000 $+ |
| Données de santé (dossier médical US) | 50-250 $ |

> **⚠️ ALERTE ANALYSTE** : Ces prix sont des moyennes indicatives à date (2025) et fluctuent selon la réputation du vendeur, la fraîcheur des données, et les dynamiques de marché. Les prix des données bancaires ont tendance à se stabiliser tandis que les credentials d'accès corporate augmentent.

#### 14.2 Le lifecycle d'un breach

Phase 1 : exploitation privée par le groupe auteur. Phase 2 : vente exclusive à prix élevé (first-sale market). Phase 3 : revente à prix décroissant. Phase 4 : publication gratuite ou à prix très bas (combo lists, collections). Phase 5 : intégration dans les bases de breach check (HIBP, DeHashed). Le temps entre phases 1 et 5 : quelques jours à plusieurs années. La phase est un indicateur de la valeur résiduelle.

#### 14.3 Vérification de l'authenticité

Échantillons gratuits (vérifiables ? emails existants ? domaines cohérents ?), fraîcheur (données déjà vues dans des breaches précédentes = recyclage), spécificité (données très spécifiques à une organisation = plus crédibles), corroboration (breach confirmé par la victime ou un CERT ?), cohérence interne (formats, conventions, dates). Les scams sont fréquents — un vendeur refusant des échantillons vérifiables est suspect. Renvoi au Ch.25 pour le workflow complet d'investigation dans un data leak.

#### 14.4 La dimension sectorielle des fuites

Les données volées ne sont pas distribuées uniformément. Le rapport Cyberint (2025) documente une concentration sur les secteurs à forte valeur : les institutions financières (données de cartes, credentials bancaires, accès aux systèmes de trading), le secteur santé (dossiers médicaux exploitables pour la fraude à l'assurance et le chantage), les télécommunications (SIM swapping, accès aux réseaux), et le secteur gouvernemental (données classifiées, identités de fonctionnaires). Chaque secteur a son propre modèle de monétisation des données volées — détaillé au Ch.35.

#### 14.5 Fil rouge — DARKSTREAM : les données en circulation

> **🌐 DARKSTREAM — Épisode 6a**
>
> En parallèle de sa surveillance d'IndustrialLeaks, Lucas vérifie si des credentials de Vectris Aerospace circulent dans les marchés de logs. Une recherche sur Russian Market (via un accès monitoring) révèle 12 logs d'infostealers contenant des credentials du domaine vectris-aerospace.eu — des sessions complètes avec cookies, autofill, et données machine. 8 des 12 logs datent de moins de 3 mois. Lucas escalade immédiatement vers le SOC de Vectris pour un reset ciblé des comptes concernés, tout en documentant cette découverte collatérale dans son journal d'investigation.

---

### Chapitre 15 — Stealer logs : anatomie, marchés et investigation défensive

*Ce chapitre traite en profondeur le vecteur de compromission initiale le plus courant en 2025-2026. Les stealer logs sont devenus la matière première de l'écosystème cybercriminel — l'équivalent du pétrole brut qui alimente toute la chaîne de valeur.*

#### 15.1 Qu'est-ce qu'un stealer log ?

Un **stealer log** est le produit de l'exécution d'un **infostealer** (malware spécialisé dans le vol de données de sessions) sur la machine d'une victime. Contrairement à un breach de base de données (qui produit des listes de credentials en masse), un stealer log capture l'intégralité de l'environnement de la session utilisateur sur un poste spécifique.

Un log d'infostealer typique contient : les **credentials du navigateur** (tous les logins/mots de passe enregistrés dans Chrome, Firefox, Edge — souvent des dizaines voire des centaines de comptes), les **cookies de session actifs** (qui permettent de se connecter à un service sans mot de passe, en contournant même le MFA — c'est le vecteur le plus dangereux), les **données d'autofill** (noms, adresses, numéros de téléphone, données de cartes bancaires), les **wallets crypto** (clés privées ou seed phrases stockés dans des extensions navigateur), les **données de la machine** (hostname, IP, OS, logiciels installés, captures d'écran), et les **sessions de messagerie** (tokens Discord, Telegram Desktop, etc.).

La puissance destructrice d'un stealer log tient à sa granularité : ce n'est pas un seul couple login/mot de passe — c'est l'intégralité de l'identité numérique d'un utilisateur, capturée à un instant T.

#### 15.2 Les infostealers dominants en 2025-2026

Les principales familles d'infostealers en circulation : **Lumma Stealer** (modèle d'abonnement, ~250 $/mois, extrêmement répandu, évolution constante pour éviter la détection), **RedLine** (historiquement dominant, toujours actif malgré des tentatives de disruption), **Vidar** (dérivé d'Arkei, populaire pour le ciblage de wallets crypto), **Raccoon Stealer** (v2, relancé après l'arrestation de son opérateur), **StealC** (émergent, léger et polyvalent), et **RisePro** (ciblage spécifique des applications crypto et des gestionnaires de mots de passe).

Le rapport SOCRadar 2025 confirme que les stealers ont un point d'entrée extrêmement bas : **15 $ en version de base**, avec des modèles d'abonnement qui les rendent accessibles à pratiquement n'importe quel acteur. Cette accessibilité explique leur adoption massive.

Les vecteurs de distribution des infostealers : malvertising (publicités Google malveillantes redirigeant vers des téléchargements piégés — technique en forte croissance), faux sites de téléchargement de logiciels crackés (vecteur historique toujours dominant, particulièrement efficace sur les utilisateurs cherchant des cracks de jeux ou de logiciels professionnels), pièces jointes email (documents Office avec macros, archives protégées par mot de passe), et compromission de la chaîne d'approvisionnement logicielle (packages npm/PyPI malveillants).

#### 15.3 Les marchés de stealer logs

Les logs volés sont commercialisés sur des marchés spécialisés :

**Russian Market** : successeur de facto de Genesis Market (saisi en avril 2023 lors de l'Operation Cookie Monster). Russian Market est le plus grand marché de logs actif en 2025-2026. Les logs sont vendus individuellement, avec un système de recherche par domaine (l'acheteur peut chercher des logs contenant des credentials pour un domaine spécifique — par exemple, un VPN d'entreprise). Prix : 1-15 $ pour un log basique, 50-500 $ pour un log contenant des accès corporate (VPN, Citrix, RDP).

**Genesis Market** (saisi) méritait une mention car il avait innové avec son modèle de « bot » — l'acheteur acquérait non pas un simple fichier de credentials, mais un navigateur virtuel qui répliquait l'empreinte exacte de la victime (fingerprint navigateur, cookies, résolution d'écran, timezone), permettant d'usurper la session sans déclencher les contrôles anti-fraude. Ce modèle a été repris par d'autres marchés.

**Canaux Telegram** : de nombreux logs sont distribués en bulk via des canaux Telegram spécialisés, souvent gratuitement (« free logs ») pour attirer les acheteurs vers des services premium. Ces canaux gratuits contiennent des logs anciens ou de faible valeur, mais constituent un point d'entrée pour les acteurs peu sophistiqués.

#### 15.4 Investigation défensive : vérifier si son organisation est touchée

Le workflow de l'analyste défensif pour surveiller l'exposition aux stealer logs :

**Étape 1 — Monitoring des domaines.** Configurer des alertes sur les marchés de logs (via des plateformes commerciales comme Flare, Hudson Rock, SOCRadar) pour les domaines de l'organisation. Chaque nouveau log contenant des credentials du domaine doit déclencher une alerte.

**Étape 2 — Évaluation du log.** Pour chaque log détecté, évaluer la criticité. Un log contenant des credentials pour le webmail est préoccupant mais gérable (reset du mot de passe + vérification MFA). Un log contenant des credentials VPN ou Citrix avec des cookies de session actifs est une urgence — l'attaquant peut potentiellement accéder au SI sans même connaître le mot de passe actuel si le cookie est encore valide.

**Étape 3 — Identification du poste source.** Les métadonnées du log (hostname, IP, OS, logiciels installés) permettent souvent d'identifier le poste compromis. Ce poste est potentiellement toujours infecté par le stealer — **changer le mot de passe sans éradiquer le stealer ne fait que fournir un nouveau mot de passe à l'attaquant**. C'est l'erreur la plus fréquente et la plus dangereuse.

**Étape 4 — Remédiation.** Le poste source doit être isolé et réimaginé. Tous les credentials contenus dans le log doivent être réinitialisés — pas seulement les credentials corporate, mais aussi les comptes personnels qui pourraient servir de pivot (un compte GitHub personnel avec accès à des repos de l'entreprise, par exemple). Les sessions actives doivent être révoquées (tokens, cookies).

**Étape 5 — Hunting.** Le SOC vérifie si les credentials du log ont été utilisés pour des connexions suspectes depuis la date estimée de la compromission (date du log). Recherche dans les logs d'authentification (VPN, AD, applications cloud) pour des connexions depuis des IP inhabituelles, des user agents inconnus, ou des horaires atypiques.

#### 15.5 Statistiques et géographie des stealer logs

Les données SOCRadar 2025 montrent une concentration des logs sur les grandes plateformes consumer : Facebook (93M+), Google (67M+), Roblox (66M+), Instagram (34M+), Microsoft Live (31M+), Amazon (22M+), Netflix (22M+), PayPal (19M+). Géographiquement, l'Inde domine largement (2,7M logs), suivie du Brésil (1,9M), de l'Indonésie (1,3M), et des États-Unis (1,2M). La position relativement basse des US suggère une meilleure détection ou une remédiation plus rapide plutôt qu'un taux d'infection plus bas.

Pour l'analyste CTI, ces statistiques indiquent que les plateformes gaming (Roblox, Twitch, Epic Games — base d'utilisateurs jeune avec une hygiène de credentials faible) et les plateformes e-commerce/streaming (Amazon, Netflix — données de paiement stockées) sont les cibles privilégiées. PayPal se distingue comme facilitateur direct de fraude plutôt que comme actif secondaire.

#### 15.6 Limites et faux positifs

Les logs ne sont pas toujours exploitables : les cookies expirent (durée de vie typique de 30-90 jours), les mots de passe peuvent avoir été changés depuis la capture, le poste peut avoir été réimaginé. Un log ancien (6+ mois) a une probabilité d'exploitation réussie beaucoup plus faible qu'un log frais. L'analyste doit évaluer la fraîcheur avant de déclencher une remédiation d'urgence.

Les faux positifs sont fréquents dans le monitoring : un domaine similaire (typosquatting), un employee personnel utilisant un email professionnel sur un site grand public, ou un log recyclé déjà traité. Le filtrage humain reste indispensable.

#### 15.7 Fil rouge — DARKSTREAM : les stealer logs de Vectris

> **🌐 DARKSTREAM — Épisode 6b**
>
> Lucas analyse les 12 logs d'infostealers de Vectris trouvés sur Russian Market. 3 logs contiennent des credentials VPN (Fortinet FortiClient) avec des cookies de session — urgence maximale. Les métadonnées révèlent 3 postes distincts : un laptop commercial (hostname VECTRIS-SALES-047), un poste R&D (VECTRIS-RD-112), et un poste IT (VECTRIS-IT-008). Le poste R&D est particulièrement préoccupant — c'est potentiellement le vecteur de l'exfiltration initiale des 420 Go.
>
> Lucas note que les logs datent de 2-4 mois — compatible avec la timeline de la compromission. Hypothèse : l'attaquant initial a utilisé un infostealer comme vecteur d'accès, les logs ont ensuite été revendus sur Russian Market par un courtier (possiblement distinct de l'auteur de l'exfiltration), et « aero_source » sur IndustrialLeaks est l'acheteur final qui revend les données techniques exfiltrées.

---

### Chapitre 16 — Services criminels : du crime-as-a-service aux profils d'acteurs

#### 16.1 Taxonomie des services et grille de prix 2025

**Malware-as-a-Service (MaaS)** : infostealers (Lumma, RedLine, Vidar — 15-1 000 $/mois en abonnement), RAT (Remcos, AsyncRAT — 50-500 $), loaders (500-5 000 $ selon sophistication). Les exploits commandent les prix les plus élevés, atteignant 5 000 $ pour des exploits à impact direct.

**Ransomware-as-a-Service (RaaS)** : modèle franchisé (LockBit, BlackBasta, Play — l'affilié partage 70-80 % des revenus avec l'opérateur). L'abonnement Crime-as-a-Service a radicalement abaissé les barrières d'entrée : les kits de phishing démarrent à 6 $, les abonnements DDoS à 20 $/semaine.

**Phishing-as-a-Service (PhaaS)** : kits de phishing avec panels d'administration (50-500 $), pages de scam personnalisées (jusqu'à 2 000 $ pour du brand targeting avancé), kits AitM (Adversary-in-the-Middle) pour l'interception MFA.

**Services de disruption** : DDoS-for-hire (20-600 $/mois selon la puissance — prix en baisse constante), stressers (même gamme), services email de spam (dès 1 $), services SMS/smishing (dès 0,05 $ par SMS).

**Services de support aux attaques** : AV disabling (le plus cher : 1 000-3 000 $ — contournement des antivirus en entreprise), droppers/abonnement (100-500 $), chiffrement de malware (100-500 $), dropper par fichier (50-100 $).

**Services de blanchiment** : mixing, OTC, mules — commission de 10-30 % du montant blanchi. Le rapport SOCRadar note que les services de blanchiment sont le tissu conjonctif de l'ensemble de l'économie criminelle.

#### 16.2 Les profils d'acteurs

Les **IAB** (Initial Access Brokers) : accès réseau compromis (VPN, RDP, Citrix) — 500 à 50 000 $ selon la cible. Les **vendeurs de bases de données**. Les **développeurs de malware** (souvent des développeurs compétents choisissant le crime pour les revenus). Les **opérateurs de ransomware**. Les **fraudeurs et carders**. Les **scammers** (couche parasitaire arnaquant les autres criminels). Les **acteurs idéologiques** (hacktivistes, extrémistes).

#### 16.3 Fil rouge — DARKSTREAM : le profil du vendeur

> **🌐 DARKSTREAM — Épisode 7**
>
> Lucas analyse « aero_source » sur IndustrialLeaks. Compte créé il y a 2 ans. 15 transactions confirmées. Rating 4.7/5. Style linguistique : anglais correct avec calques syntaxiques slaves. Montants de ventes précédentes : 5-80 BTC. Lucas conclut : vendeur spécialisé données industrielles, probablement un courtier (broker) achetant des données à des groupes d'intrusion pour les revendre avec marge. Il n'est probablement pas l'auteur de l'intrusion chez Vectris — il en est le revendeur.

---

### Chapitre 17 — Marché des 0-day et chaîne exploit → attaque

*Ce chapitre couvre un segment critique de l'écosystème dark web : le commerce des vulnérabilités non corrigées et la chaîne qui transforme un 0-day acheté sur un forum en attaque réelle — parfois en quelques semaines.*

#### 17.1 Qu'est-ce que le marché des 0-day ?

Un **0-day** est une vulnérabilité logicielle pour laquelle aucun correctif n'existe au moment de sa découverte. Le marché des 0-day sur le dark web est un marché de niche à haute valeur ajoutée où des chercheurs (ou des groupes offensifs) vendent des vulnérabilités exploitables à des acheteurs qui peuvent être des cybercriminels, des États, ou des courtiers intermédiaires.

Ce marché se distingue du commerce de credentials ou de malware par plusieurs caractéristiques. Les **volumes sont faibles** (quelques dizaines de transactions significatives par mois sur les forums majeurs). Les **prix sont élevés** (de 1 000 $ à plusieurs centaines de milliers de dollars). La **vérification est complexe** (l'acheteur ne peut pas tester un 0-day sans risquer de le « brûler »). Et les **conséquences sont disproportionnées** (un seul 0-day peut compromettre des milliers d'organisations).

#### 17.2 Grille de prix et évolution 2024-2026

Les données SOCRadar 2025 documentent trois tiers de prix pour les 0-day sur le dark web :

**Entrée de gamme (1 000-5 000 $)** : vulnérabilités de portée limitée, fiabilité incertaine, ou ciblant des logiciels peu déployés. Le plancher a augmenté significativement — les 0-day à 100 $ du marché de 2023 ont pratiquement disparu. Les 0-day à ce prix sont souvent des PoC (Proof of Concept) qui nécessitent un travail supplémentaire pour être rendus exploitables en conditions réelles.

**Milieu de gamme (10 000-50 000 $)** : exploits fonctionnels pour des plateformes courantes (applications web d'entreprise, logiciels de collaboration, VPN d'entreprise). Le prix moyen a doublé par rapport à 2023, reflétant la difficulté croissante de trouver des vulnérabilités dans des logiciels de plus en plus audités.

**Haut de gamme (50 000-150 000 $+)** : vulnérabilités critiques dans des systèmes largement déployés avec des contrôles défensifs forts (systèmes d'exploitation, navigateurs, solutions de sécurité). Le plafond observé a légèrement diminué par rapport aux 200 000 $ de 2023 — possiblement en raison d'une compétition accrue entre vendeurs ou d'un déplacement des 0-day les plus critiques vers des canaux étatiques non visibles sur le dark web.

> **⚠️ ALERTE ANALYSTE** : Les prix affichés sur les forums ne reflètent pas le marché étatique des 0-day (où des entreprises comme les anciens NSO Group, Zerodium, ou Crowdfense proposent des récompenses de 500 000 $ à 2,5 M$ pour des 0-day mobiles). Le marché du dark web est le segment « bas » du marché global des 0-day.

#### 17.3 La chaîne 0-day → attaque de masse : le cas Oracle EBS / Cl0p

Un cas documenté par SOCRadar illustre parfaitement la chaîne qui relie le marché des 0-day aux attaques de masse. Vers juin 2025, un acteur a mis en vente sur un forum dark web un 0-day affectant Oracle E-Business Suite (Preauth RCE) pour 70 000 $. Quelques mois plus tard (octobre-novembre 2025), le groupe de ransomware Cl0p a lancé une campagne ciblée contre des entreprises utilisant Oracle EBS.

Ce cas illustre plusieurs mécanismes. Le **délai entre achat et exploitation** (4-5 mois — temps nécessaire pour développer l'infrastructure d'attaque, identifier les cibles, et déployer). Le **passage de l'exploit individuel à l'exploitation de masse** (un 0-day acheté pour 70 000 $ rapporte des millions quand il est utilisé pour du ransomware contre des dizaines de victimes). La **rentabilité asymétrique** qui fait du marché des 0-day un investissement très rentable pour les groupes de ransomware. Et la **valeur du renseignement précoce** : un analyste CTI qui aurait détecté la vente du 0-day en juin aurait pu alerter les clients utilisant Oracle EBS 4 mois avant l'attaque.

#### 17.4 Anatomie d'une annonce de 0-day

Une annonce typique sur un forum contient : le logiciel affecté (sans toujours nommer la version exacte — pour éviter qu'un lecteur ne la trouve lui-même), le type de vulnérabilité (RCE, privilege escalation, authentication bypass), une description fonctionnelle de l'impact, le prix demandé, les conditions de vente (escrow, exclusivité ou non, nombre d'acheteurs limité), et parfois une vidéo de démonstration (la preuve que l'exploit fonctionne, sans révéler les détails techniques).

Les acteurs sérieux précisent souvent les conditions de test : « testé sur un environnement de test, pas sur des cibles externes » (comme dans l'annonce Oracle EBS documentée par SOCRadar). Cette précision sert deux objectifs : limiter la responsabilité juridique perçue, et signaler aux acheteurs que l'exploit n'a pas encore été « brûlé » (utilisé en conditions réelles et donc potentiellement détecté).

#### 17.5 Implications pour l'analyste CTI

Le monitoring du marché des 0-day est l'un des rares cas où le dark web offre un **renseignement prédictif** plutôt que réactif. Quand un analyste détecte la vente d'un 0-day ciblant un logiciel utilisé par son organisation, il dispose d'une fenêtre d'action pour prendre des mesures préventives : durcissement de la configuration, segmentation réseau, surveillance accrue des logs, et préparation d'un plan IR.

Cependant, les limites sont réelles : les annonces de 0-day sur les forums publics sont souvent des scams ou des vulnérabilités déjà corrigées présentées comme inédites. L'évaluation de crédibilité est critique — et repose sur la réputation du vendeur, l'historique de ses ventes précédentes, et la cohérence technique de l'annonce.

#### 17.6 Fil rouge — DARKSTREAM : la veille proactive

> **🌐 DARKSTREAM — Épisode 7b**
>
> En surveillant XSS (le forum russophone où « aero_source » a aussi une présence), Lucas repère une annonce sans lien avec Vectris mais pertinente pour un autre client d'Athéna Group : un 0-day affectant une solution VPN d'entreprise utilisée par plusieurs clients CAC 40. L'annonce est en vente à 45 000 $ avec « 3 acheteurs maximum ». Lucas documente l'annonce et escalade vers les équipes concernées — c'est un exemple de valeur ajoutée collatérale de la veille dark web.

---

## PARTIE IV — ÉCONOMIE CLANDESTINE ET MÉCANISMES DE CONFIANCE

---

### Chapitre 18 — Pourquoi l'économie du dark web fonctionne

Malgré l'absence de cadre légal et de confiance a priori, l'économie du dark web fonctionne — imparfaitement, mais elle fonctionne. Les mécanismes : la **spécialisation** (chaque acteur fait ce qu'il sait faire — l'IAB vend l'accès, l'opérateur RaaS déploie le ransomware, le blanchisseur convertit les crypto), la **modularité** (les services sont interconnectés comme des briques Lego), les **barrières d'entrée basses** (grâce au modèle as-a-Service), et les **mécanismes de confiance substitutifs** (réputation, escrow, vouching — Ch.19).

Le rapport SOCRadar 2025 confirme cette analyse : le hacking s'est déplacé de la sophistication technique vers l'exploitation d'opportunités. Les acteurs préfèrent acheter des credentials valides plutôt que de développer des exploits complexes. Le dark web fonctionne comme un supermarché qui abaisse les barrières d'entrée pour la cybercriminalité.

### Chapitre 19 — Réputation, escrow, vouching et arbitrage

La **réputation** se construit par l'historique de transactions, les ratings, et la validation par des membres de confiance. Un profil avec 200+ transactions et 3 ans d'ancienneté est un capital valant 5 000-20 000 $. L'**escrow** retient les fonds de l'acheteur jusqu'à confirmation. Le **vouching** est le parrainage par un membre établi. L'**arbitrage** est la résolution des litiges par un modérateur avec pouvoir discrétionnaire considérable.

### Chapitre 20 — Arnaques, exit scams et manipulation de la confiance

Les **exit scams** : l'opérateur d'un marché accumule les fonds d'escrow puis disparaît (Evolution Market, 2015 — ~12 M$). Les **faux vendeurs** avec profils crédibles (comptes anciens achetés ou transactions simulées avec des complices). Les **escrows fictifs** contrôlés par le vendeur. La **simulation de légitimité** (faux reviews, faux vouching) est endémique.

Pour l'analyste CTI, ces arnaques sont un piège analytique majeur (Ch.32) : un « vendeur de données Vectris » peut être un scammer capitalisant sur le buzz de la compromission.

### Chapitre 21 — Modèles économiques criminels observés via le dark web

#### 21.1 Les modèles dominants

Le **RaaS** (opérateur + affiliés + IAB + blanchisseur — chaîne de valeur complète). Le **pipeline infostealer** (infostealer → log market → exploitation — la chaîne la plus courte entre compromission et monétisation). L'**Initial Access Brokerage** (compromission → vente d'accès → exploitation par l'acheteur). La **fraude documentaire** (production → vente → utilisation). Les **services d'obfuscation** (crypters, hosting, mixing — services transversaux).

#### 21.2 Le blanchiment-as-a-Service

Le blanchiment de cryptomonnaies est le lubrifiant de l'ensemble du système. Les services de blanchiment (mixing, conversion via des exchanges non KYC, utilisation de mules, OTC desks clandestins) prélèvent une commission de 10-30 % du montant. La saisie de Chipmixer (mars 2023 — 152 000 BTC estimés blanchis, environ 2,73 milliards d'euros selon le rapport EPRS) illustre l'échelle de ces opérations. L'utilisation croissante de Monero et des atomic swaps BTC↔XMR rend le traçage progressivement plus difficile.

#### 21.3 Le modèle 0-day → ransomware

Modèle émergent documenté par SOCRadar : l'acquisition d'un 0-day sur le dark web (investissement de 20 000-150 000 $), suivi du développement d'une capacité d'exploitation, puis du déploiement de ransomware contre les cibles identifiées (retour sur investissement de 10x-100x). Le cas Oracle EBS/Cl0p (Ch.17) est l'archétype de ce modèle. Pour l'analyste CTI, ce modèle crée une opportunité de détection précoce : la vente du 0-day précède l'attaque de plusieurs mois.

---

## PARTIE V — INVESTIGATION, VEILLE ET COLLECTE

---

### Chapitre 22 — Cadre juridique, éthique et sécurité de l'analyste

#### 22.1 Ce que l'analyste privé a le droit de faire

La consultation passive (naviguer, lire, observer sans interagir) est légale en France et dans la plupart des juridictions occidentales. La collecte de données publiquement accessibles est légale dans le cadre d'une mission légitime. L'analyse de données fuitées pour la sécurité est tolérée mais encadrée par le RGPD. Le signalement aux autorités est obligatoire pour certains contenus (CSAM, terrorisme — 22.4).

#### 22.2 Ce que l'analyste privé n'a PAS le droit de faire

L'interaction active avec des acteurs criminels (provocation réservée aux forces de l'ordre). L'achat de données criminels (recel). L'intrusion dans les systèmes d'un service dark web (accès frauduleux, article 323-1 CP). Le téléchargement de CSAM (tolérance zéro, article 227-23 CP).

#### 22.3 Les zones grises

Le paiement d'un droit d'accès à un forum. L'utilisation de personas. La conservation de données fuitées (encadrée RGPD). Chaque zone grise nécessite un cadrage juridique préalable, documenté, avec l'aval du directeur juridique.

#### 22.4 Les obligations impératives

Signalement CSAM (article 434-3 CP). Signalement activité terroriste (article 421-2-5 CP). Via **PHAROS** ou directement auprès des services compétents. Le signalement est obligatoire et immédiat.

#### 22.5 Cadre pour les forces de l'ordre

Achats sous couverture (article 706-81 CPP), infiltration en ligne (« cyber-patrouilles »), réquisitions, coopération internationale (Europol EC3, Interpol, MLAT). Ces pouvoirs ne s'appliquent PAS aux investigateurs privés.

#### 22.6 Fil rouge — DARKSTREAM : le cadrage

> **🌐 DARKSTREAM — Épisode 8**
>
> Cadrage juridique validé : consultation passive autorisée, captures d'écran autorisées, paiement d'accès autorisé (plafonné 500 €, documenté), pas de téléchargement des documents techniques Vectris, pas d'interaction directe avec « aero_source », signalement DGSI recommandé si données confirmées liées à la défense.

---

### Chapitre 23 — OPSEC opérationnelle pour l'investigation dark web

#### 23.1 Modèle de menace de l'investigateur

Protections nécessaires contre : les acteurs criminels (identification), les opérateurs de plateformes (détection de comportement suspect), les forces de l'ordre (confusion avec un acteur malveillant), et les fuites accidentelles.

#### 23.2 Configuration de l'environnement

**Poste dédié** : jamais le poste professionnel. **Whonix** : VM Gateway (route tout via Tor) + VM Workstation (isolation réseau stricte). **Tails** : OS bootable amnésique pour les déplacements. **Séparation réseau** : WiFi public, SIM prépayée (achetée en espèces), ou VPN commercial en amont de Tor.

#### 23.3 VPN + Tor : le débat

**Tor seul** : simple, recommandé par le Tor Project. **VPN → Tor** : masque l'utilisation de Tor au réseau local — compromis le plus courant pour l'investigateur. **Tor → VPN** : l'exit node voit du trafic VPN au lieu de la destination finale. Recommandation : VPN → Tor avec VPN commercial fiable.

#### 23.4 Gestion des personas (sock puppets)

Composantes d'une persona : pseudonyme cohérent avec la culture du forum, email jetable (ProtonMail via Tor, sans téléphone), wallet crypto dédié (un par persona), Tox ID dédié, backstopping minimal. **Discipline de séparation** critique : jamais la même persona pour deux investigations, jamais de croisement avec l'identité réelle.

---

### Chapitre 24 — Naviguer et collecter : méthodes, outils et limites

#### 24.1 Trouver des services

Moteurs de recherche dark web (Ahmia, DarkSearch, Torch, Haystak) : couverture partielle, résultats souvent obsolètes. « Hidden wikis » et listes de liens : généralement périmés et truffés de scams. Sources les plus fiables : les forums eux-mêmes, canaux Telegram spécialisés, rapports CTI.

#### 24.2 Limites de la visibilité

L'analyste ne voit qu'une fraction : forums les plus fermés invisibles, transactions sensibles en privé, monitoring automatisé incomplet, données non représentatives. « L'absence de données Vectris sur les forums observés ne signifie pas l'absence de circulation. »

#### 24.3 Techniques de collecte et de préservation

Capture d'écran horodatée (date/heure UTC, adresse .onion, chemin, persona). **Hunchly** (capture et horodatage automatique + hash d'intégrité). Sauvegarde de pages (wget via torsocks, HTTrack via Tor). Hashing SHA-256 de chaque capture.

#### 24.4 Crawling et scraping automatisé

**OnionScan** : détection d'erreurs de configuration. **TorBot** et **ACHE** : crawlers automatisés. Scripts Python via PySocks ou stem. Limites : captchas, authentification, anti-bot, risque de bannissement, considérations éthiques.

---

### Chapitre 25 — Investigation dans un data leak : workflow opérationnel

*Ce chapitre est le cœur méthodologique de l'investigation dark web pour le praticien défensif. Il couvre le workflow complet depuis la détection d'une alerte de fuite jusqu'à la remédiation et le rapport — en combinant outils, techniques, et arbitrages méthodologiques.*

#### 25.1 Typologie des situations d'investigation

L'analyste peut être confronté à plusieurs scénarios d'investigation dans un data leak, chacun avec ses propres contraintes.

**Scénario 1 — Alerte de monitoring.** Une plateforme de monitoring (Flare, Recorded Future, Cybersixgill) détecte une mention de l'organisation sur un forum ou un marché. L'analyste doit vérifier l'authenticité, évaluer l'étendue, et décider des actions.

**Scénario 2 — Notification externe.** Un tiers (CERT, partenaire, journaliste, client) signale que des données de l'organisation circulent. L'analyste doit localiser la source, vérifier l'information, et cadrer la réponse.

**Scénario 3 — Découverte proactive.** L'analyste détecte lui-même des données lors d'une veille de routine (credentials dans les logs d'infostealers, documents dans un paste public, mention sur un canal Telegram).

**Scénario 4 — Post-incident.** Après un incident de sécurité confirmé (ransomware, exfiltration), l'analyste doit déterminer si les données volées ont été publiées ou mises en vente.

#### 25.2 Phase 1 — Qualification initiale de l'alerte

Avant de mobiliser des ressources, l'analyste évalue rapidement si l'alerte mérite investigation.

**Vérification du contexte source.** D'où vient l'alerte ? Un forum de référence (XSS, Exploit) avec un vendeur réputé a une crédibilité élevée. Un canal Telegram public créé la semaine dernière avec un vendeur inconnu a une crédibilité faible. La source détermine le niveau de priorité.

**Vérification sémantique.** Le nom de l'organisation est-il utilisé dans le bon contexte ? « Vectris » peut apparaître dans une discussion sans rapport (un nom commun dans une autre langue, un produit homonyme, une référence à une compromission ancienne déjà traitée). L'analyste vérifie que la mention est bien liée à une fuite de données active.

**Évaluation de fraîcheur.** Les données mentionnées sont-elles nouvelles ou recyclées ? Le recoupement avec les bases de breaches connus (HIBP, DeHashed) permet de déterminer si les données sont déjà en circulation depuis longtemps. Des credentials apparaissant dans un breach de 2019 republié en 2025 ne sont pas une nouvelle menace — c'est du recyclage.

**Décision GO/NO-GO.** Si l'alerte est crédible, fraîche, et contextuelle → investigation complète. Si elle est douteuse → surveillance renforcée pendant 48-72h avant de décider.

#### 25.3 Phase 2 — Recherche et localisation des données

L'analyste lance une recherche systématique pour localiser les données fuitées et évaluer l'étendue de la fuite.

**Recherche dans les bases de breaches.** **Have I Been Pwned** (gratuit, email uniquement — vérifie si des emails du domaine apparaissent dans des breaches répertoriés). **DeHashed** (payant, recherche par email, pseudo, mot de passe, domaine, IP — plus granulaire, permet de voir les mots de passe hashés ou en clair). **IntelX** (freemium, archive de pastebins, breaches, et contenus dark web — permet de rechercher des fragments de données). **Snusbase** (payant, recherche par email, pseudo, mot de passe, hash, nom, IP). **LeakCheck** (payant, vérification de credentials).

**Procédure concrète pour une recherche de credentials :**

1. Lister les domaines email de l'organisation (domaine principal + sous-domaines + domaines historiques/fusionnés).
2. Rechercher chaque domaine dans HIBP API pour identifier les breaches connus.
3. Rechercher les domaines dans DeHashed/IntelX pour identifier les credentials en clair ou hashés.
4. Rechercher dans les marchés de logs (Russian Market via monitoring, Hudson Rock) pour les logs d'infostealers contenant des credentials du domaine.
5. Rechercher dans les pastebins indexés (Pastebin, GhostBin, 0bin — via IntelX ou SpiderFoot).
6. Rechercher sur Telegram (canaux de dump connus, bots de recherche de credentials).

**Recherche dans les forums et marchés dark web.** Recherche par mots-clés sur les forums accessibles (nom de l'organisation, noms de produits, noms de dirigeants). Consultation des sections de vente de données. Vérification des leak sites de ransomware (Ransomwatch, Ransomfeed) pour une revendication. Recherche sur les marchés de données spécialisés.

#### 25.4 Phase 3 — Analyse et vérification de l'authenticité

Une fois les données localisées, l'analyste doit évaluer leur authenticité avant de déclencher des actions.

**Vérification des échantillons.** Si le vendeur fournit des échantillons : les emails existent-ils réellement ? Les noms d'employés correspondent-ils au répertoire (LinkedIn, annuaire interne) ? Les formats de documents (noms de fichiers, conventions, en-têtes) sont-ils cohérents avec les pratiques de l'organisation ? Les métadonnées des documents (auteur, date de création, logiciel) sont-elles plausibles ?

**Évaluation de la fraîcheur.** Comparer avec les breaches connus. Des mots de passe correspondant à la politique de l'entreprise (longueur, complexité) sont un indicateur de fraîcheur. Des mots de passe obsolètes (ne respectant pas la politique actuelle) suggèrent un breach ancien. La date de changement de mot de passe des comptes concernés (si accessible via le SOC) permet de dater approximativement la compromission.

**Test de validité (avec précautions).** L'analyste peut tester si un credential est encore valide — mais uniquement sur les systèmes de son organisation et avec l'autorisation écrite du client. Jamais sur des systèmes tiers. Ce test confirme l'exploitabilité actuelle de la fuite.

**Évaluation du volume.** Quelques credentials = probable log d'infostealer (Ch.15). Des milliers de credentials = probable breach de base de données. Des documents internes = probable exfiltration ciblée. Le volume et le type de données orientent la réponse.

#### 25.5 Phase 4 — Évaluation de l'impact et priorisation

Chaque fuite n'a pas le même impact. L'analyste évalue selon plusieurs critères.

**Criticité des données.** Des credentials de messagerie d'un stagiaire vs des credentials VPN d'un administrateur système : la criticité est radicalement différente. Des documents marketing vs des plans techniques classifiés : idem. L'analyste priorise la remédiation en fonction de la criticité.

**Exploitabilité.** Des credentials dans un breach de 2020 avec des mots de passe depuis changés : exploitabilité quasi nulle. Des cookies de session actifs d'un stealer log datant d'une semaine : exploitabilité critique. Des documents déjà publiés sur un leak site : le dommage est fait, la priorité est la gestion de crise plutôt que la remédiation technique.

**Exposition.** Les données sont-elles accessibles publiquement (publiées sur un paste ou un leak site) ou en vente privée (réduisant le nombre d'acteurs potentiellement en possession) ? L'exposition détermine l'urgence de la communication et la probabilité d'exploitation par des acteurs tiers.

#### 25.6 Phase 5 — Actions de remédiation et escalade

**Actions techniques immédiates (en coordination avec le SOC/IT) :**
- Reset des credentials compromis (mots de passe ET sessions/tokens/cookies).
- Révocation des sessions actives pour les comptes touchés.
- Vérification MFA (le MFA était-il activé ? un cookie de session permet-il de le contourner ?).
- Hunting dans les logs d'authentification pour des connexions suspectes depuis la date estimée de compromission.
- Si un stealer log est identifié : isolation et réimagerie du poste source (le stealer peut être toujours actif).

**Escalades nécessaires :**
- SOC/CSIRT : pour le hunting et la remédiation technique.
- Juridique : pour l'évaluation de l'obligation de notification (CNIL si données personnelles — 72h pour la notification initiale sous RGPD).
- Communication : si la fuite est publique ou susceptible de l'être, préparation de la communication de crise.
- Direction : si l'impact business est significatif (données sensibles, risque réputationnel, implications réglementaires).
- Autorités : si les données sont classifiées (DGSI/ANSSI) ou si une plainte est envisagée.

#### 25.7 Phase 6 — Documentation et rapport

L'intégralité du processus est documenté dans le journal de collecte (Ch.28). Le rapport final suit la structure du Ch.34. Les éléments spécifiques à documenter pour un data leak :
- Source de l'alerte initiale et date de détection.
- Plateformes et outils consultés, avec les résultats de chaque recherche.
- Échantillons vérifiés et méthode de vérification.
- Volume estimé et types de données compromises.
- Évaluation de la fraîcheur et de l'exploitabilité.
- Actions de remédiation effectuées avec dates et responsables.
- Indicateurs de compromission (IoC) extraits.
- Recommandations pour prévenir une récurrence.

#### 25.8 Cas particulier : retrouver un mot de passe dans un breach

L'analyste défensif peut avoir besoin de vérifier si des mots de passe spécifiques de son organisation circulent. Les approches :

**Recherche par hash.** HIBP propose une API « Pwned Passwords » permettant de vérifier si un hash de mot de passe (SHA-1 ou NTLM) apparaît dans les breaches connus — sans envoyer le mot de passe en clair. L'approche k-anonymity envoie uniquement les 5 premiers caractères du hash et reçoit tous les hashs correspondants, permettant une vérification locale sans exposition.

**Recherche dans les bases de breaches.** Les plateformes comme DeHashed permettent de rechercher par hash de mot de passe ou par mot de passe partiel. Cette recherche est légitime quand elle porte sur les comptes de son propre domaine et dans le cadre d'une mission documentée.

**Analyse des logs d'infostealers.** Les logs contiennent les mots de passe en clair (les infostealers capturent les mots de passe depuis le credential store du navigateur, qui les stocke en clair ou en réversible). Cette donnée est immédiatement exploitable — et immédiatement invalidable par un reset.

> **⚠️ ALERTE ÉTHIQUE ET JURIDIQUE** : La recherche de mots de passe dans les bases de breaches est légitime uniquement pour les comptes relevant de la responsabilité de l'analyste (domaine de son organisation ou du client mandant). Rechercher les mots de passe d'un tiers (concurrent, individu ciblé) sans mandat judiciaire est illégal et constitue un accès frauduleux aux données personnelles.

#### 25.9 Outils recommandés pour l'investigation de data leaks

| Outil | Type | Usage | Limites |
|-------|------|-------|---------|
| Have I Been Pwned | Gratuit | Vérification emails et mots de passe dans les breaches | Emails uniquement, pas de données détaillées |
| DeHashed | Payant (abo) | Recherche multi-critères dans les breaches | Couverture variable, certaines données anciennes |
| IntelX | Freemium | Archives pastebins, breaches, dark web | Résultats limités en version gratuite |
| Snusbase | Payant | Recherche par email, pseudo, mot de passe, hash | Couverture variable |
| Hudson Rock | Payant | Monitoring stealer logs par domaine | Accès commercial |
| Flare | Payant | Monitoring dark web + clear web + logs | Couverture incomplète sur forums fermés |
| SpiderFoot | Gratuit (OSS) | Framework OSINT avec modules breach/dark web | Courbe d'apprentissage |

#### 25.10 Fil rouge — DARKSTREAM : l'investigation du leak

> **🌐 DARKSTREAM — Épisode 9**
>
> Lucas applique ce workflow à l'annonce d'« aero_source » sur IndustrialLeaks. Les échantillons fournis par le vendeur (3 fichiers PDF : un rapport de test de composant, un schéma CAD en basse résolution, et un email interne) sont transmis au RSSI de Vectris pour vérification (via un canal sécurisé, sans transiter par email). Le RSSI confirme : les documents sont authentiques, datés de 8 mois, et correspondent à des fichiers stockés sur le serveur de fichiers R&D compromis.
>
> Lucas documente dans son rapport : « Authenticité confirmée — niveau de confiance élevé. Les données correspondent à l'exfiltration de 420 Go documentée dans le rapport IR. Le vendeur dispose d'au moins un sous-ensemble des données exfiltrées. L'étendue exacte ne peut être déterminée sans acquérir l'intégralité du lot — ce qui est hors du périmètre du mandat. »

---

### Chapitre 26 — Pivoting, enrichissement et corrélation OSINT

#### 26.1 Le workflow de pivot

À partir d'un identifiant trouvé dans un espace, l'analyste enrichit et relie vers d'autres espaces. Un pseudo → bases de breaches → email → clear web → profil. Un wallet Bitcoin → explorateurs blockchain → transactions sur exchanges. Un Tox ID → recherche sur d'autres forums et Telegram. Une clé PGP → serveurs de clés publiques et clear web. Chaque pont entre dark web et surface web est une faille OPSEC exploitable.

#### 26.2 Outils d'enrichissement

**Sherlock** / **WhatsMyName** : recherche de pseudo cross-platform. **DeHashed** / **IntelX** / **Snusbase** : recherche dans les bases de breaches. **OXT.me** / **Chainalysis** : exploration blockchain Bitcoin. **Maltego** (transforms dark web) : graphe de relations. **SpiderFoot** : framework OSINT modulaire.

#### 26.3 Corrélation dark web ↔ surface web

Technique d'investigation la plus productive. Erreurs OPSEC exploitables : pseudo réutilisé, email apparaissant dans un WHOIS et un forum .onion, style d'écriture identifiable, métadonnées dans des documents publiés (nom d'auteur, dates, logiciel).

#### 26.4 Fil rouge — DARKSTREAM : le pivoting

> **🌐 DARKSTREAM — Épisode 10**
>
> Lucas pivote à partir des identifiants de « aero_source ». Le Tox ID apparaît sur un post de 2023 sur un forum anglophone (archive RaidForums) sous le pseudo « aero_sell ». Le wallet Bitcoin montre des transactions avec un cluster associé à un exchange KYC basé en Asie du Sud-Est. Piste exploitable si les autorités sont saisies.

---

### Chapitre 27 — Veille dark web : surveillance, alerting et réduction du bruit

#### 27.1 Que surveiller

Pour une organisation : mentions du nom, des domaines, des emails d'employés, des noms de projets/produits, des noms de dirigeants, des identifiants techniques. Sur les leak sites, les forums, les marchés de logs, Telegram, et dans les breaches publiques.

#### 27.2 Plateformes de monitoring

Solutions commerciales (Flare, Recorded Future, Digital Shadows/ReliaQuest, Cybersixgill, Searchlight Cyber, ZeroFox, SOCRadar). Avantages : couverture large, alertes automatisées, intégration API. Limites : couverture incomplète sur forums fermés, latence, faux positifs, coût élevé (10 000-100 000+ $/an). Le monitoring artisanal reste complémentaire.

#### 27.3 Réduction du bruit

Affinement des mots-clés (spécifiques plutôt que génériques), vérification systématique, priorisation (leak sites ransomware > mentions génériques), connaissance de l'écosystème.

---

### Chapitre 28 — Preuve, capture et documentation

#### 28.1 Documentation du processus

Le **journal de collecte** enregistre chronologiquement chaque action : date/heure UTC, adresse visitée, persona utilisée, action effectuée, résultat, décision. Hashé quotidiennement.

Chaque capture : date/heure UTC, adresse .onion + chemin, persona, outil de capture, hash SHA-256. Chaîne de custody garantissant l'intégrité.

#### 28.2 Reproductibilité et limites

Grande difficulté : la **non-reproductibilité**. Un site .onion peut disparaître le lendemain. L'analyste ne peut pas prouver qu'une page existait — seulement qu'il l'a capturée et que sa capture n'a pas été modifiée. Cette limitation doit être explicitée dans le rapport.

---

## PARTIE VI — ANALYSE, RENSEIGNEMENT ET PRODUCTION

---

### Chapitre 29 — Dé-anonymisation : méthodes et limites

#### 29.1 Exploitation des erreurs OPSEC

Méthode la plus productive en pratique. Erreurs classiques : réutilisation de pseudo (Sherlock, WhatsMyName), réutilisation d'email (DeHashed, IntelX, WHOIS), fuite d'IP par mauvaise configuration (OnionScan), horaires d'activité révélant un fuseau horaire, style d'écriture identifiable (stylométrie), erreurs de gestion financière (réutilisation d'adresses Bitcoin, conversion via exchange KYC).

#### 29.2 Cas de dé-anonymisation documentés

**Ross Ulbricht** (Silk Road) : post StackOverflow avec email personnel + pseudo « Frosty ». **Alexandre Cazes** (AlphaBay) : email Hotmail dans les headers de l'email de bienvenue du marché. **Hansa Market** : métadonnées des images et serveur de développement non anonymisé. **Dmitry Khoroshev** (LockBitSupp) : convergence registrars, comptes crypto, analyse linguistique, renseignement humain. **Pompompurin** (BreachForums) : email personnel associé à un service traçable.

#### 29.3 Analyse linguistique et stylométrie

Marqueurs exploitables : langue native (erreurs grammaticales, calques syntaxiques), registre, tics de langage, orthographe. La stylométrie computationnelle est un indice convergent mais pas une preuve autonome. Particulièrement utile pour la corrélation cross-forum.

#### 29.4 Limites de la dé-anonymisation

Un acteur avec une OPSEC disciplinée est extrêmement difficile à identifier. Tor n'a jamais été « cassé » cryptographiquement — les compromissions viennent d'erreurs humaines. Monero est résistant au traçage. L'attribution définitive nécessite généralement des moyens judiciaires dépassant le périmètre de l'analyste privé.

---

### Chapitre 30 — Techniques avancées : NIT, honeypots et infiltration policière

*Ce chapitre détaille les techniques utilisées par les forces de l'ordre pour compromettre l'anonymat des utilisateurs du dark web. L'analyste CTI doit les connaître pour comprendre l'environnement dans lequel il opère, évaluer la crédibilité des informations obtenues, et comprendre les risques de confusion entre investigateur et suspect.*

#### 30.1 Network Investigative Techniques (NIT)

Le terme **NIT** désigne les techniques d'investigation réseau utilisées par le FBI (et d'autres agences) pour identifier les utilisateurs du dark web. En pratique, un NIT est un exploit logiciel — typiquement une vulnérabilité du navigateur (Firefox/Tor Browser) — déployé sur un site dark web contrôlé par les forces de l'ordre. Quand un utilisateur visite le site avec un navigateur vulnérable, le NIT s'exécute et envoie l'adresse IP réelle de l'utilisateur (et d'autres identifiants machine) à un serveur contrôlé par les enquêteurs.

Le cas le plus documenté est l'**Operation Pacifier** (2015) contre Playpen, un site de CSAM avec près de 215 000 membres. Le FBI a pris le contrôle du site, l'a maintenu en ligne pendant 13 jours, et a déployé un NIT qui a identifié les adresses IP de milliers de visiteurs dans 120 pays. Cette opération a conduit à l'identification de plus de 8 700 IP uniques, 300 poursuites judiciaires, et le sauvetage de dizaines d'enfants.

Le NIT utilisé dans Operation Pacifier exploitait une vulnérabilité de Firefox (le navigateur sur lequel est basé le Tor Browser) pour contourner la protection Tor et révéler l'IP réelle. La légalité de cette technique a été contestée devant les tribunaux (un seul mandat couvrant des milliers de cibles dans différentes juridictions), mais la plupart des condamnations ont été confirmées.

Les implications pour l'analyste : le Tor Browser en mode « Safest » (JavaScript désactivé) protège contre la majorité des NIT connus, qui reposent sur l'exécution de code JavaScript ou d'exploits navigateur. L'utilisation de Whonix (isolation réseau au niveau VM) offre une protection supplémentaire — même si un exploit s'exécute dans le navigateur, il ne peut accéder qu'à la VM Workstation, pas à l'hôte.

#### 30.2 End-to-end confirmation attacks

L'attaque par corrélation de trafic : un adversaire qui contrôle à la fois le guard node (entrée) et l'exit node (sortie) d'un circuit Tor peut corréler le timing et le volume du trafic pour relier l'utilisateur à sa destination. En théorie, un adversaire contrôlant une fraction significative des relais Tor (ou surveillant les points d'échange Internet — IXP) pourrait réaliser cette attaque à grande échelle.

Les forces de l'ordre ont exploité cette technique en compromettant les **hidden service directories** du réseau Tor — les nœuds qui stockent les descripteurs des onion services. En contrôlant ces nœuds, elles peuvent surveiller quels clients accèdent à quel hidden service, et corréler avec d'autres sources d'information.

Le programme **XKeyscore** de la NSA (révélé par Edward Snowden) aurait « fingerprinted » automatiquement tout utilisateur tentant de télécharger le Tor Browser ou le système Tails, permettant à l'agence d'identifier les utilisateurs potentiels de Tor avant même qu'ils ne se connectent au réseau.

#### 30.3 Honeypots et sting operations

Les **honeypots** sont des sites ou services du dark web opérés secrètement par les forces de l'ordre pour attirer et identifier des acteurs criminels. L'exemple le plus spectaculaire est **Hansa Market** : après la saisie d'AlphaBay en juillet 2017, la police néerlandaise a continué à opérer Hansa Market pendant 30 jours, collectant les identifiants, les messages, et les transactions de milliers d'utilisateurs qui avaient migré depuis AlphaBay. Les enquêteurs ont modifié le code du marché pour capturer les mots de passe en clair (au lieu des hashs), enregistrer les messages privés déchiffrés, et identifier les adresses IP des vendeurs par des modifications subtiles du processus de téléchargement d'images.

Les **sting operations** impliquent que des agents se fassent passer pour des acheteurs ou des vendeurs pour identifier et arrêter des criminels. En France, les « cyber-patrouilles » sont autorisées pour les agents habilités sous contrôle judiciaire (article 706-87-1 CPP). Ces opérations requièrent un cadre juridique strict — la provocation à l'infraction (inciter quelqu'un à commettre un crime qu'il n'aurait pas commis autrement) est illégale et invalidera les poursuites.

#### 30.4 Implications pour l'analyste CTI

L'existence de ces techniques a plusieurs implications pour l'analyste privé :

**Risque de confusion.** Un analyste opérant sous persona sur un forum pourrait être identifié par un NIT ou un honeypot et confondu avec un acteur criminel par les forces de l'ordre. Le cadrage juridique préalable (Ch.22) et la documentation rigoureuse sont des protections essentielles — l'analyste doit pouvoir démontrer la légitimité de son accès.

**Fiabilité des sources.** Un forum ou un marché peut être un honeypot sans que les utilisateurs le sachent. Les informations collectées sur un site contrôlé par les forces de l'ordre peuvent être contaminées (données plantées, acteurs sous contrôle). L'analyste doit considérer cette possibilité dans son évaluation de crédibilité.

**Environnement hostile.** Les acteurs criminels sont conscients de ces techniques et adaptent leur comportement — certains forums exigent des « preuves de criminalité » pour l'accès (proof of criminal activity), précisément pour filtrer les agents infiltrés. L'analyste privé ne peut évidemment pas fournir de telles preuves, ce qui limite son accès aux espaces les plus fermés.

---

### Chapitre 31 — Traçage crypto et analyse financière

#### 31.1 Bitcoin investigation

Techniques d'analyse : clustering d'adresses (heuristiques d'input commun), identification des services (exchanges, mixers, marchés), exploitation des points de conversion fiat↔crypto (réquisition exchanges KYC). Outils : OXT.me (gratuit, Bitcoin), Chainalysis Reactor (commercial, law enforcement), TRM Labs, Crystal Intelligence.

#### 31.2 Monero investigation

Beaucoup plus difficile. Approches possibles : analyse comportementale (corrélation timing), exploitation des erreurs (même adresse Monero sur clear et dark web), heuristiques anciennes (ring signatures pré-2017 moins robustes), exploitation des conversions Monero↔Bitcoin. Pratiquement impossible pour un adversaire non étatique en 2025-2026.

#### 31.3 Fil rouge — DARKSTREAM : le traçage financier

> **🌐 DARKSTREAM — Épisode 11**
>
> Le wallet Bitcoin de « aero_source » a reçu ~85 BTC (~3 M€) sur 2 ans. Les fonds sortants passent par un mixer connu avant d'atteindre un cluster associé à un exchange KYC en Asie du Sud-Est. Piste exploitable via réquisition judiciaire.

---

### Chapitre 32 — Pièges analytiques, désinformation et faux signaux

*Ce chapitre est l'un des plus importants du cours. Sur le dark web, les erreurs analytiques sont la norme si l'analyste ne s'en prémunit pas activement.*

#### 32.1 Faux leaks et données recyclées

Un « vendeur de données Vectris » peut être un scammer capitalisant sur la couverture médiatique. Les données peuvent être recyclées d'un breach antérieur. Vérifier l'authenticité AVANT de conclure.

#### 32.2 Faux drapeaux et usurpation

Un acteur peut publier sous un faux pseudo pour incriminer un concurrent. Les pseudos sont fréquemment réutilisés par des acteurs différents. Un acteur peut se prétendre affilié à un groupe connu sans l'être. Ne jamais attribuer sur la base d'un seul pseudo.

#### 32.3 Intoxication et manipulation

Publication délibérée de fausses informations : faux échantillons pour créer la panique, fausses revendications, faux « leaks internes ». Traiter chaque information comme potentiellement fausse jusqu'à vérification indépendante.

#### 32.4 Biais de survivance et d'échantillonnage

Le **biais de survivance** : les espaces visibles sont ceux qui n'ont pas (encore) été saisis. Le **biais d'échantillonnage** : l'analyste ne voit que les espaces auxquels il a accès. La confusion entre visibilité et importance : un forum bruyant n'est pas nécessairement important, un forum discret peut être beaucoup plus dangereux.

#### 32.5 Grille de vérification systématique

Pour chaque observation : **Source** (forum, ancienneté, réputation), **Contenu** (vérifiable, cohérent), **Corroboration** (source indépendante), **Motivation** (pourquoi l'acteur publie), **Ancienneté** (fraîcheur vs recyclage), **Contexte** (pattern connu). Grille complète en Annexe E.

#### 32.6 Fil rouge — DARKSTREAM : le piège évité

> **🌐 DARKSTREAM — Épisode 12**
>
> Un second post mentionnant Vectris apparaît sur un canal Telegram public : « Vectris Aerospace full database — 500 GB — 30 BTC ». Volume incohérent (500 Go vs 420 Go), canal créé il y a 2 semaines, échantillons non vérifiables, prix bas. Conclusion : probable scam opportuniste. Lucas le documente mais ne le confond pas avec « aero_source ».

---

### Chapitre 33 — Transformer les observations en renseignement actionnable

#### 33.1 De la donnée brute au renseignement

Processus en quatre étapes : **Contextualisation** (qui publie, où, dans quel historique), **Évaluation de crédibilité** (source et information évaluées indépendamment), **Niveau de confiance** (Admiralty Ratings ou système simplifié élevé/modéré/faible), **Implications** (actions que le client doit entreprendre).

#### 33.2 Les différents publics et leurs besoins

SOC/CSIRT → IoC. Équipe IR → contexte TTP. RSSI → évaluation de risque. COMEX → executive brief. Juridique → faits documentés et preuves. Chaque public a son propre format de livrable.

#### 33.3 Quand escalader

Vers l'IR : menace active (accès vendu, credentials fraîches, attaque en cours). Vers le juridique : données personnelles ou classifiées en circulation. Vers le COMEX : impact réputationnel imminent. Vers les autorités : données de défense nationale, CSAM, menace physique.

---

### Chapitre 34 — Produire une note analytique

#### 34.1 Structure d'une note analytique dark web

**Résumé exécutif** (1 page max — souvent le seul élément lu). **Contexte** (mandat, périmètre, sources, limitations). **Faits observés** (avec source, date, confiance). **Analyse** (au moins 2 hypothèses, avec éléments pour/contre). **Évaluation de la menace** (impact, probabilité, urgence). **Recommandations** (actions priorisées — techniques, juridiques, communicationnelles, stratégiques). **Annexes** (captures hashées, fiches d'acteurs, IoC, journal de collecte). Templates détaillés en Annexe F.

---

### Chapitre 35 — Menaces dark web par secteur d'activité

*Ce chapitre offre une lecture sectorielle des menaces dark web — indispensable pour l'analyste CTI qui doit adapter sa veille et ses recommandations au contexte métier de son client.*

#### 35.1 Secteur financier (BFSI)

Le secteur financier est la cible la plus prisée sur le dark web, combinant volume de données exploitables et monétisation directe. Les menaces principales : **données bancaires et cartes** (card shops spécialisés, validation de cartes volées en masse), **credentials bancaires** (accès aux comptes via stealer logs — les logs contenant des sessions bancaires actives sont les plus valorisés), **account takeover** (prise de contrôle de comptes via des credentials achetées), **phishing kits ciblés** (reproduisant les interfaces bancaires avec interception MFA), **fraude documentaire** (faux documents d'identité pour ouvrir des comptes), et **mobile banking malware** (RAT Android avec accès complet au device — capture d'écran, caméra, GPS, SMS). Le rapport Cyberint souligne que les institutions financières manquant de ressources et de contrôles adéquats sont particulièrement vulnérables, malgré des obligations réglementaires fortes (PCI-DSS, DORA, NIS2).

#### 35.2 Secteur santé

Les données de santé sont parmi les plus précieuses sur le dark web en raison de leur exploitabilité multiple : fraude à l'assurance (particulièrement aux US), chantage (dossiers médicaux sensibles), usurpation d'identité médicale, et accès aux systèmes hospitaliers (ransomware). Les menaces spécifiques : **fuites de dossiers médicaux** (PII + données médicales = « medical fullz »), **ransomware hospitalier** (impact vital — les hôpitaux paient plus souvent que d'autres secteurs), **IoT médical** (dispositifs médicaux connectés hackables — pompes à insuline, pacemakers, systèmes d'imagerie), et **cryptojacking/medjacking** (compromission de dispositifs médicaux pour le minage de cryptomonnaies). La combinaison de systèmes legacy, de budgets IT limités, et de données à haute valeur fait du secteur santé une cible de choix.

#### 35.3 Secteur télécom

Les opérateurs télécoms sont ciblés pour l'accès à l'infrastructure qu'ils contrôlent. Les menaces : **SIM swapping** (prise de contrôle du numéro de téléphone — utilisé pour contourner le MFA SMS), **données clients** (PII en masse), **accès réseau** (les compromissions de télécoms offrent un accès latéral à des milliers de clients), **interception de communications**, et **DDoS** (les télécoms sont à la fois cibles et vecteurs). Les outils spécifiques en circulation : outils de clonage SIM, bases de données de numéros de téléphone avec informations personnelles, et services de social engineering ciblant les centres d'appel des opérateurs.

#### 35.4 Secteur gouvernemental et défense

Les données classifiées, les identités de fonctionnaires, et les accès aux réseaux gouvernementaux sont des cibles à haute valeur, tant pour les cybercriminels que pour les acteurs étatiques. Les menaces : **fuites de données classifiées** (espionnage industriel et étatique), **APT** (accès persistant aux réseaux gouvernementaux via des outils achetés sur le dark web), **insider threats** (employés ou contractants mécontents utilisant le dark web pour vendre des accès ou des données), et **DDoS contre les services publics**. Le croisement entre cybercriminalité et espionnage étatique est particulièrement marqué dans ce secteur — un même outil ou un même accès peut être utilisé à des fins criminelles ou géopolitiques.

#### 35.5 Secteur retail et e-commerce

Les données de paiement et les comptes clients sont les cibles principales. Les menaces : **RAM scrapers** (malware installé sur les terminaux de paiement — technique utilisée dans le breach Target de 2013, toujours pertinente), **credentials de comptes clients** (avec données de paiement stockées), **fraude aux retours** (utilisation de comptes volés pour des achats frauduleux), et **contrefaçon** (vente de produits contrefaits utilisant les marques du retailer). Le rapport du CRS note que les données volées lors du breach Target ont inondé les marchés du dark web en quelques semaines, se vendant entre 20 et 100 $ par carte — illustrant la vitesse à laquelle les données volées se propagent.

#### 35.6 Adapter sa veille au secteur

L'analyste CTI doit calibrer sa veille selon le secteur de son client. Pour le financier : monitoring des card shops, des logs contenant des sessions bancaires, des forums de carding. Pour la santé : monitoring des leak sites (les hôpitaux sont surreprésentés), des forums vendant des données médicales, des vulnérabilités IoT médicales. Pour la défense : monitoring des forums spécialisés (IndustrialLeaks et équivalents), des canaux de vente d'accès, et des acteurs IAB ciblant le secteur. La priorisation des sources et des mots-clés est spécifique à chaque secteur.

---

## PARTIE VII — CAS D'USAGE, TENDANCES ET PROSPECTIVE

---

### Chapitre 36 — Ransomware, extorsion et leak sites

Le ransomware est le point de convergence entre le dark web et la cybersécurité opérationnelle. L'écosystème complet (IAB → RaaS affilié → négociation → publication) est détaillé au cours IR et au cours Écosystèmes. Ce chapitre se concentre sur le volet dark web : comment surveiller les leak sites (Ransomwatch, Ransomfeed, monitoring commercial), comment interpréter une revendication (authentique ? échantillons crédibles ?), comment suivre l'évolution d'une négociation, et comment anticiper la publication (compte à rebours réel ou bluff ?). Le rapport SOCRadar 2025 fournit des données actualisées sur les groupes les plus actifs et la distribution géographique des attaques. Le cas pratique du Ch.42 applique cette méthode.

---

### Chapitre 37 — Dark web, influence et opérations informationnelles

Le dark web comme vecteur d'opérations d'influence : **fuites orchestrées** (hack-and-leak operations — données volées puis publiées stratégiquement), **relais** entre espaces clandestins et réseaux sociaux, **instrumentalisation médiatique** (groupes de ransomware contactant directement les journalistes), et **campagnes hybrides** (cyber-attaque + fuite + amplification médiatique — playbook des opérations russo-ukrainiennes post-2022). La porosité croissante entre cybercriminalité, hacktivisme, et opérations d'influence étatique rend la catégorisation des acteurs de plus en plus difficile.

---

### Chapitre 38 — Hacktivisme, zones grises et usages légitimes

SecureDrop et les plateformes de whistleblowing. Les mouvements hacktivistes (Anonymous, IT Army of Ukraine, groupes pro-russes). Les zones grises : contrebande informationnelle, activisme anti-censure, usage étatique du dark web. La difficulté de catégorisation morale et juridique est assumée : le même outil est utilisé par un dissident iranien et par un trafiquant. L'analyste documente les faits sans porter de jugement moral.

---

### Chapitre 39 — IA et dark web : menaces émergentes, outils et limites

*Ce chapitre couvre l'intersection entre intelligence artificielle et dark web — à la fois comme menace (outils IA utilisés par les attaquants) et comme défense (IA au service de l'investigation et de la détection). Le paysage a considérablement évolué entre 2024 et 2026.*

#### 39.1 L'IA comme outil offensif sur le dark web

Le rapport SOCRadar 2025 documente un changement de paradigme par rapport à 2024 : si les outils IA malveillants vendus sur le dark web (chatbots jailbreakés, modèles sans guardrails) existaient déjà l'année précédente et restaient relativement inefficaces comparés aux outils cybercriminels traditionnels, **la démocratisation des outils IA grand public a fondamentalement changé la donne**.

Les outils d'IA accessibles sans passer par le dark web offrent désormais des capacités qui étaient autrefois réservées aux acteurs sophistiqués : génération de texte pour des campagnes de phishing convaincantes (emails sans fautes d'orthographe, personnalisés, contextuellement pertinents), génération de code pour l'adaptation de malware, analyse automatisée de vulnérabilités, et création de deepfakes audio/vidéo. Le fait que ces outils soient disponibles gratuitement ou à faible coût, sans nécessité d'accéder à des marchés illicites, abaisse encore les barrières d'entrée de la cybercriminalité.

#### 39.2 Outils IA malveillants vendus sur le dark web

Malgré la disponibilité des outils grand public, le dark web continue de proposer des outils IA spécifiquement conçus pour des usages malveillants. Le rapport SOCRadar documente des outils comme **LiarAI**, vendu sur les forums avec des capacités revendiquées : réponse aux questions illégales, développement d'exploits et de malware, interaction avec Internet, et génération d'images. D'autres outils comprennent des modèles jailbreakés (versions sans restrictions de modèles commerciaux), des chatbots « uncensored » pour l'assistance au hacking, et des générateurs de phishing automatisés.

Cependant, l'**efficacité réelle** de ces outils reste contestée. Beaucoup sont des wrappers basiques autour de modèles existants avec des prompts de jailbreak, dont la fiabilité et la pertinence sont limitées. L'analyste CTI doit évaluer ces outils avec le même scepticisme qu'il applique à tout produit vendu sur le dark web — entre le marketing et la réalité, l'écart est souvent considérable.

#### 39.3 Deepfakes : la menace la plus concrète

La manipulation audio et vidéo est le domaine où l'IA a fait le bond le plus significatif en 2025. Les outils open source et commerciaux de deepfake (changement de visage, clonage vocal, synthèse vidéo) sont désormais utilisables avec un minimum de données d'entraînement et sans compétences techniques avancées.

Les implications pour la sécurité : **fraude au CEO** (deepfake audio d'un dirigeant ordonnant un virement — plusieurs cas documentés avec des pertes de millions de dollars), **usurpation d'identité** (vidéos de vérification KYC contrefaites pour ouvrir des comptes bancaires), **désinformation** (vidéos de personnalités publiques diffusant de faux messages), et **chantage** (création de contenu compromettant à partir de photos publiques). Le rapport SOCRadar illustre le phénomène avec des exemples concrets de manipulation d'images de figures publiques, soulignant l'absence de garde-fous efficaces pour détecter et attribuer ces manipulations.

#### 39.4 L'IA comme outil défensif et investigatif

L'IA n'est pas seulement une menace — elle offre aussi des capacités accrues pour la défense et l'investigation dark web.

**Monitoring automatisé.** Les plateformes de monitoring dark web utilisent de plus en plus le NLP (Natural Language Processing) pour analyser automatiquement les posts de forums, détecter les mentions d'organisations, évaluer le sentiment, et prioriser les alertes. Ces systèmes réduisent significativement le bruit et permettent de traiter des volumes de données impossibles à analyser manuellement.

**Analyse de code malveillant.** Les outils d'IA assistent les analystes malware dans le reverse engineering : décompilation assistée, identification de familles de malware par similarité de code, et détection de patterns comportementaux.

**Stylométrie avancée.** Les modèles de NLP modernes permettent une analyse linguistique plus fine pour la corrélation cross-forum : identification d'auteurs probables par leur style d'écriture, détection de traduction automatique, et identification de la langue native derrière un texte écrit dans une autre langue.

**Outils de pentesting assistés par IA.** Des outils de scanning et d'évaluation de vulnérabilités intégrant de l'IA sont désormais disponibles, ce qui est à double tranchant — ils aident les équipes de sécurité mais sont aussi accessibles aux attaquants.

#### 39.5 Limites et mise en perspective

Plusieurs nuances essentielles :

Les outils IA du dark web ne remplacent pas les compétences techniques — ils les augmentent. Un attaquant incompétent avec un outil IA produit des attaques plus convaincantes en surface (meilleur phishing) mais pas nécessairement plus efficaces techniquement (l'exploitation de vulnérabilités et le post-exploitation restent des compétences humaines).

La détection des contenus générés par IA est un domaine en constante évolution. Les détecteurs actuels ne sont pas fiables (taux de faux positifs élevé) et ne doivent jamais être utilisés comme preuve autonome. L'analyste ne peut pas conclure qu'un texte est « écrit par IA » sur la base d'un outil de détection.

Le cadre réglementaire est en retard. L'AI Act européen (entré en vigueur en 2025) pose des bases mais ne couvre pas spécifiquement les usages malveillants sur le dark web. La question de la gouvernance des modèles open source (impossible à restreindre une fois publiés) reste ouverte.

> **⚠️ ALERTE ANALYSTE** : La tentation de surestimer l'impact de l'IA sur le paysage des menaces est forte (et entretenue par le marketing des vendeurs de solutions). L'analyste CTI doit maintenir une évaluation sobre : l'IA abaisse les barrières d'entrée et améliore certaines capacités, mais elle ne transforme pas un script kiddie en APT. Les fondamentaux de la cybercriminalité (social engineering, exploitation de vulnérabilités connues, erreurs de configuration) restent les mêmes.

---

### Chapitre 40 — Forces de l'ordre, disruption et droit international

#### 40.1 Les grandes opérations de police

- **Operation Bayonet** (2017) : AlphaBay + Hansa. La police néerlandaise a opéré Hansa pendant 30 jours après la saisie d'AlphaBay, capturant les utilisateurs en migration. 
- **Operation Cookie Monster** (2023) : saisie de Genesis Market, Europol parle de **plus de 1,5 million de bot listings** et **plus de 2 millions d’identités numériques**, avec **17 pays** impliqués. (https://www.europol.europa.eu/media-press/newsroom/news/takedown-of-notorious-hacker-marketplace-selling-your-identity-to-criminals)
- **Operation SpecTor** (2023) : 288 arrestations coordonnées dans 6 pays. 
- **Operation Cronos** (2024) : disruption de l'infrastructure LockBit, identification de Dmitry Khoroshev comme LockBitSupp, saisie de l'infrastructure et des clés de déchiffrement. 
- **Operation Stream** (2025) : démantèlement de Kidflix, l'une des plus grandes plateformes CSAM sur le dark web — plus de 91 000 vidéos CSAM, presque 2 millions d’utilisateurs, 1 393 suspects identifiés, 79 arrestations, 39 enfants protégés. Cette opération, menée en coordination internationale, illustre l'efficacité de la coopération européenne via Europol et le J-CAT. (https://www.europol.europa.eu/media-press/newsroom/news/global-crackdown-kidflix-major-child-sexual-exploitation-platform-almost-two-million-users)

#### 40.2 Disruption et impact

Les takedowns perturbent mais ne détruisent pas les écosystèmes. L'impact le plus durable est sur la **confiance** : les saisies créent une méfiance chronique qui augmente le coût et le risque des transactions. La publication des « seizing pages » et des données saisies est un outil de disruption psychologique.

#### 40.3 L'impact post-Durov sur Telegram

L'arrestation de Pavel Durov en France en août 2024 a eu des conséquences significatives sur l'écosystème cybercriminel. Telegram a considérablement renforcé sa modération des canaux illicites, conduisant à une migration partielle des acteurs vers d'autres plateformes (retour vers les forums .onion, migration vers des messageries alternatives comme Session ou Matrix sur Tor). Cependant, Telegram reste un canal majeur de communication cybercriminelle en 2025-2026 — l'écosystème s'est adapté plutôt que déplacé en masse.

#### 40.4 Cadre juridique international

La **Convention de Budapest** (2001, ratifiée par 68+ pays en 2025) est le traité de référence. Les MLAT pour les réquisitions cross-border. Le **Cloud Act** américain. La question de la juridiction (serveur au Panama, opérateur en Russie, vendeur en Allemagne, acheteur en France). La coopération via **Europol** (EC3), **Interpol**, et le **J-CAT**. Le rapport EPRS 2026 souligne l'importance d'une approche collaborative complétée par le partage d'innovations et la création d'unités spécialisées dans le dark web.

---

## PARTIE VIII — ÉTUDES DE CAS ET SYNTHÈSE

---

### Chapitre 41 — Cas complet : investigation d'une vente de données industrielles (synthèse DARKSTREAM)

Synthèse du fil rouge sous forme de cas autonome. Du mandat initial à la note analytique finale :

**Configuration OPSEC** : Whonix sur laptop dédié, VPN → Tor, persona « tech_researcher » créée avec email ProtonMail via Tor, wallet Bitcoin dédié, Tox ID dédié. **Accès au forum** : paiement de 0,005 BTC documenté dans le journal de collecte, cadrage juridique validé. **Analyse du profil vendeur** : ancienneté 2 ans, 15 transactions, rating 4.7/5, style linguistique slave, montants de ventes antérieures 5-80 BTC — courtier spécialisé, pas l'auteur de l'intrusion. **Vérification des échantillons** : 3 documents transmis au RSSI Vectris, authenticité confirmée. **Pivot OSINT** : pseudo → Tox ID → forum archivé (RaidForums archive, pseudo « aero_sell ») → wallet Bitcoin → mixer → exchange KYC (Asie du Sud-Est). **Filtrage des scams** : le faux vendeur Telegram (« data_broker_EU ») identifié et écarté — volume incohérent, canal récent, échantillons non vérifiables. **Découverte collatérale** : 12 stealer logs de Vectris sur Russian Market, dont 3 avec credentials VPN — escalade immédiate vers le SOC. **Traçage financier** : wallet → mixer → exchange KYC — piste documentée pour les autorités.

**Conclusions du rapport :** Données Vectris authentiques et en circulation (confiance : élevée). Vendeur « aero_source » est un courtier basé probablement en Europe de l'Est (confiance : modérée). Au moins 2 acheteurs identifiés via le système d'escrow. Stealer logs actifs avec credentials VPN (escalade immédiate). Signalement DGSI recommandé (données liées à des programmes de défense). Notification CNIL requise (données personnelles d'employés dans les stealer logs).

---

### Chapitre 42 — Cas complet : surveillance d'un leak site ransomware

Un RSSI découvre que son entreprise (ETI logistique, 1 200 employés) est listée sur le leak site de BlackBasta, avec un compte à rebours de 10 jours et des échantillons de documents internes.

**Jour 1** : confirmation du groupe (BlackBasta — TTP connues, style du leak site), évaluation de l'authenticité (échantillons confirmés par le client), mise en place du monitoring quotidien (leak site + canaux Telegram associés). **Jours 2-5** : alimentation de la cellule de crise (situational awareness, options de réponse), coordination avec le conseil juridique (notification CNIL, assurance cyber), préparation de la communication (si publication). **Jours 6-9** : surveillance de la négociation (portail de négociation accessible publiquement — le client a choisi de ne pas payer), anticipation de la publication. **Jour 10** : publication partielle (200 Go sur 800 Go annoncés), analyse du contenu publié, évaluation de l'impact, déclenchement de la communication de crise. **Post-publication** : monitoring de la rediffusion (les données de BlackBasta sont souvent reprises par des acteurs secondaires), notification des tiers concernés, retex.

---

### Chapitre 43 — Cas complet : traque d'un IAB vendant des accès

Un analyste détecte une annonce de vente d'accès VPN au SI d'un client (banque régionale) sur Exploit.in : « French bank, 2500 employees, Citrix VPN, Domain Admin access, asking 15000$ ».

**Vérification** : nombre d'employés et type de VPN correspondent au client. **Source de compromission** : les credentials VPN apparaissent dans les logs Russian Market, datés de 3 semaines — probable infostealer. **Profil du vendeur** : IAB actif depuis 6 mois, 8 ventes confirmées, spécialisé secteur financier européen. **Remédiation immédiate** : reset des credentials VPN, déploiement MFA renforcé, investigation forensic sur le poste source de l'infostealer (identifié via les métadonnées du log — hostname, IP, OS). **Hunting SIEM** : recherche de connexions suspectes depuis l'IP du log jusqu'au présent. **Résultat** : connexion suspecte détectée 5 jours après la date du log, depuis une IP ukrainienne, avec le compte VPN compromis — l'accès a été utilisé avant que la vente ne soit publiée.

---

### Chapitre 44 — Maturité analyste et programme de veille durable

#### 44.1 Niveaux de maturité

**Débutant** : navigue avec les outils de base, trouve les forums principaux, capture d'écran horodatée. Ne distingue pas scam/vrai, pas de méthodologie de vérification.

**Intermédiaire** : OPSEC maîtrisée, personas gérées, forums clés et vendeurs habituels connus, sait vérifier l'authenticité, sait pivoter dark web ↔ surface web, produit des notes analytiques avec niveaux de confiance.

**Avancé** : comprend les dynamiques sociologiques des communautés underground, détecte scams et intoxications, corrèle entre multiples sources (forums, Telegram, blockchain, OSINT, stealer logs), produit des cartographies d'écosystèmes, forme les analystes juniors.

#### 44.2 Programme de veille durable

Objectifs clairs (quelles menaces, pour quels métiers), sources priorisées (forums, leak sites, marchés de logs, Telegram — couverture réaliste), fréquence adaptée (quotidienne pour leak sites ransomware, hebdomadaire pour forums, mensuelle pour tendances), documentation rigoureuse, articulation avec SOC/IR/CTI/juridique/communication, amélioration continue (retex, mise à jour des sources, formation).

#### 44.3 Les bonnes habitudes

Ne jamais considérer une seule source comme suffisante. Documenter ce qu'on observe ET ce qu'on ne peut pas observer. Séparation stricte identité professionnelle/personas. Ne jamais surestimer ce que le dark web peut nous apprendre. Résister à la fascination du clandestin — le dark web est un outil de travail, pas un terrain d'aventure.

---

## ANNEXES

---

### Annexe A — Glossaire

| Terme | Définition |
|-------|-----------|
| **.onion** | Domaine utilisé par les onion services Tor (56 caractères en v3) |
| **Atomic swap** | Échange direct entre deux cryptomonnaies sans intermédiaire |
| **Bridge** | Relais Tor non listé publiquement, utilisé pour contourner la censure |
| **Bulletproof hosting** | Hébergement ignorant les plaintes d'abus et requêtes judiciaires |
| **CoinJoin** | Protocole décentralisé de mixing Bitcoin par transaction collaborative |
| **Combo list** | Liste massive de couples email/mot de passe issus de multiples breaches |
| **C2** | Command and Control — infrastructure de commande d'un malware |
| **Darknet** | Réseau overlay conçu pour l'anonymat (Tor, I2P, Freenet) |
| **Dark web** | Ensemble des contenus accessibles via les darknets |
| **DDoS** | Distributed Denial of Service — attaque par saturation |
| **Dead drop** | Point de dépôt physique pour la livraison de biens illicites |
| **Dead man's switch** | Mécanisme automatique activé si l'opérateur ne se manifeste pas |
| **Deep web** | Contenus web non indexés par les moteurs de recherche (~90 % du web) |
| **Deepfake** | Contenu audio/vidéo généré ou manipulé par IA pour imiter une personne réelle |
| **DHT** | Distributed Hash Table — utilisée par Tor pour les descripteurs d'onion services |
| **Directory authority** | Serveur de confiance maintenant le consensus du réseau Tor (9 serveurs) |
| **Eepsite** | Site web hébergé sur le réseau I2P |
| **Escrow** | Séquestre de fonds par un tiers de confiance pendant une transaction |
| **Exit node** | Dernier relais d'un circuit Tor, point de sortie vers Internet |
| **Exit scam** | Disparition de l'opérateur d'un marché avec les fonds d'escrow |
| **Fullz** | Identité complète pour l'usurpation (nom, adresse, SSN, date de naissance) |
| **Garlic routing** | Variante de l'onion routing utilisée par I2P |
| **Guard node** | Premier relais d'un circuit Tor — voit l'IP réelle de l'utilisateur |
| **HIBP** | Have I Been Pwned — service de vérification d'exposition aux breaches |
| **IAB** | Initial Access Broker — acteur vendant des accès réseau compromis |
| **Infostealer** | Malware spécialisé dans le vol de credentials, cookies, et données de session |
| **Introduction point** | Relais Tor servant de point de contact initial pour un onion service |
| **K-anonymity** | Technique de protection de la vie privée dans les requêtes de vérification |
| **Leak site** | Site .onion où les groupes de ransomware publient les données des victimes |
| **Log (infostealer)** | Session complète volée par un infostealer (credentials, cookies, données machine) |
| **Lurker** | Membre d'un forum qui observe sans participer |
| **Medical fullz** | Identité complète incluant des données médicales (pour fraude à l'assurance) |
| **Middle relay** | Relais intermédiaire d'un circuit Tor |
| **Mixer / Tumbler** | Service mélangeant les fonds crypto de plusieurs utilisateurs |
| **Monero (XMR)** | Cryptomonnaie conçue pour la confidentialité des transactions |
| **NIT** | Network Investigative Technique — exploit FBI pour dé-anonymiser les utilisateurs Tor |
| **NLP** | Natural Language Processing — traitement automatique du langage naturel |
| **0-day** | Vulnérabilité logicielle pour laquelle aucun correctif n'existe |
| **Onion routing** | Technique de chiffrement en couches pour l'anonymat réseau |
| **Onion service** | Serveur accessible exclusivement via le réseau Tor (adresse .onion) |
| **OPSEC** | Operational Security — pratiques de sécurité opérationnelle |
| **PHAROS** | Plateforme française de signalement des contenus illicites en ligne |
| **Pluggable transport** | Protocole déguisant le trafic Tor pour contourner la censure |
| **Proof-of-work captcha** | Captcha basé sur un calcul intensif, protection anti-DDoS |
| **RaaS** | Ransomware-as-a-Service — modèle franchisé de ransomware |
| **RAM scraper** | Malware installé sur un terminal de paiement pour capturer les données de cartes |
| **Rendezvous point** | Relais Tor servant de point de rendez-vous client/onion service |
| **Ring signature** | Signature cryptographique par un groupe d'adresses (Monero) |
| **Russian Market** | Marché de logs d'infostealers dominant (successeur de Genesis Market) |
| **Scam** | Arnaque — offre frauduleuse sans intention de livrer |
| **SecureDrop** | Plateforme de whistleblowing anonyme basée sur Tor |
| **SIM swapping** | Prise de contrôle d'un numéro de téléphone par ingénierie sociale |
| **Sock puppet** | Fausse identité (persona) créée pour l'investigation |
| **Stealth address** | Adresse crypto à usage unique (Monero) |
| **Stealer log** | Fichier produit par un infostealer contenant l'environnement de session complet |
| **Sting operation** | Opération policière utilisant de fausses identités pour piéger des criminels |
| **Surface web** | Web indexé par les moteurs de recherche (~5-10 % du web) |
| **Tails** | Système d'exploitation amnésique et anonyme (bootable USB) |
| **Tor** | The Onion Router — réseau d'anonymat le plus utilisé |
| **Tox** | Messagerie peer-to-peer chiffrée, utilisée sur les forums underground |
| **Vanity address** | Adresse .onion avec un préfixe personnalisé généré par force brute |
| **Vouching** | Système de parrainage par un membre établi d'un forum |
| **Whonix** | VM dédiée au routage Tor avec isolation réseau stricte |
| **XKeyscore** | Programme NSA de surveillance et fingerprinting des utilisateurs Tor |
| **Zero-day market** | Marché de vulnérabilités inédites sur le dark web |

---

### Annexe B — Typologie des espaces dark web

| Type d'espace | Fonction | Exemples d'usage | Intérêt analytique | Limites |
|--------------|----------|-----------------|-------------------|---------|
| **Forums généralistes** | Discussion, vente, recrutement | XSS, Exploit, BreachForums successeurs | Large spectre, tendances | Bruit, scams, accès fermé |
| **Forums spécialisés** | Vente ciblée (données industrielles, carding) | IndustrialLeaks, forums de carding | Données haute valeur, acteurs spécialisés | Très fermés, difficile d'accès |
| **Marchés généralistes** | Commerce multi-catégories | Successeurs d'Hydra/AlphaBay | Volume, diversité, tendances économiques | Cycle de vie court, exit scams |
| **Marchés de logs** | Vente de sessions d'infostealers | Russian Market | Credentials d'entreprise, monitoring de fuite | Volume massif, filtrage nécessaire |
| **Leak sites ransomware** | Publication données victimes | LockBit, BlackBasta, Play | Monitoring des attaques, TTP, secteurs ciblés | Données potentiellement sensibles |
| **Canaux Telegram** | Promotion, vente rapide | Canaux de revente, IAB, ransomware | Accessibilité, rapidité | Moins d'anonymat, éphémérité |
| **IRC / XMPP / Tox** | Communication directe | Négociation, coordination | Transactions privées | Invisibles de l'extérieur |
| **Pastebins** | Publication éphémère | Dumps de credentials, IoC | Données techniques | Volatilité, liens morts |
| **Marchés de 0-day** | Commerce de vulnérabilités | Sections spécialisées d'Exploit, XSS | Renseignement prédictif | Très fermés, scams fréquents |

---

### Annexe C — OPSEC analyste : checklists

#### Checklist configuration poste d'investigation

- [ ] Laptop dédié (sans données pro/perso)
- [ ] Whonix installé (Gateway + Workstation) OU Tails sur USB
- [ ] VPN commercial configuré (en amont de Tor si choisi)
- [ ] Aucun compte personnel connecté
- [ ] Réseau séparé du réseau professionnel
- [ ] Hunchly installé dans le Tor Browser de la VM
- [ ] Outils de capture et de hashing disponibles
- [ ] Journal de collecte ouvert

#### Checklist création de persona

- [ ] Pseudonyme cohérent avec le forum ciblé
- [ ] Email jetable créé via Tor (ProtonMail/Tutanota sans téléphone)
- [ ] Wallet crypto dédié (un par persona)
- [ ] Tox ID dédié (si nécessaire)
- [ ] Backstopping minimal (2-3 plateformes secondaires)
- [ ] Aucun croisement avec l'identité réelle
- [ ] Documentation de la persona dans un fichier sécurisé

#### Checklist navigation sécurisée

- [ ] Tor Browser en mode « Safest » (JavaScript désactivé)
- [ ] Fenêtre du navigateur NON maximisée
- [ ] Aucune extension (au-delà de Hunchly)
- [ ] Aucun téléchargement sans analyse sandbox préalable
- [ ] Aucune connexion à un compte personnel
- [ ] Captures d'écran horodatées pour chaque page pertinente
- [ ] Hash SHA-256 sur chaque capture
- [ ] Journal de collecte mis à jour en temps réel

#### Checklist investigation data leak

- [ ] Domaines de l'organisation listés (principal + sous-domaines + historiques)
- [ ] HIBP vérifié pour chaque domaine
- [ ] DeHashed/IntelX/Snusbase recherchés
- [ ] Marchés de logs vérifiés (Russian Market via monitoring)
- [ ] Pastebins indexés vérifiés (IntelX, SpiderFoot)
- [ ] Canaux Telegram de dump vérifiés
- [ ] Leak sites ransomware vérifiés (Ransomwatch/Ransomfeed)
- [ ] Échantillons évalués selon la grille de crédibilité (Annexe E)
- [ ] Fraîcheur des données évaluée
- [ ] Exploitabilité évaluée
- [ ] Remédiation coordonnée avec le SOC/IT
- [ ] Notification juridique évaluée (CNIL si données personnelles)

#### Checklist fin de session

- [ ] Captures hashées et archivées
- [ ] Journal de collecte complété et hashé
- [ ] VM Workstation réinitialisée au snapshot propre
- [ ] Aucune donnée résiduelle sur le poste hôte
- [ ] VPN déconnecté

---

### Annexe D — Outils d'investigation dark web

| Catégorie | Outil | Gratuit/Payant | Usage | Limites |
|-----------|-------|---------------|-------|---------|
| **Navigation** | Tor Browser | Gratuit | Navigation .onion | Lent, certains sites exigent JS |
| **Navigation** | Whonix | Gratuit | VM avec isolation réseau Tor | Config initiale complexe |
| **Navigation** | Tails | Gratuit | OS amnésique, portable | Pas de persistance par défaut |
| **Documentation** | Hunchly | Payant (~130 $/an) | Capture auto + hash + timeline | Extension navigateur uniquement |
| **Scan** | OnionScan | Gratuit | Scan hidden services (IP leaks) | Non maintenu activement |
| **Crawling** | TorBot | Gratuit | Crawler .onion | Basique, pas d'anti-bot bypass |
| **Monitoring** | Flare | Payant | Monitoring dark + clear web + logs | Couverture incomplète forums fermés |
| **Monitoring** | Recorded Future | Payant | CTI plateforme avec sources dark web | Coût élevé, latence |
| **Monitoring** | Cybersixgill | Payant | Monitoring dark web spécialisé | Couverture variable |
| **Monitoring** | SOCRadar | Payant | XTI avec Dark Web Radar | Couverture large, coût |
| **Monitoring** | Hudson Rock | Payant | Monitoring stealer logs par domaine | Accès commercial |
| **OSINT** | Sherlock | Gratuit | Recherche pseudo cross-platform | Faux positifs fréquents |
| **OSINT** | WhatsMyName | Gratuit | Recherche pseudo (plus complet) | Web only |
| **OSINT** | SpiderFoot | Gratuit/Payant | Framework OSINT modulaire | Courbe d'apprentissage |
| **OSINT** | Maltego | Payant | Graphe de relations, transforms | Coût élevé |
| **Breach** | DeHashed | Payant (abo) | Recherche multi-critères breaches | Couverture variable |
| **Breach** | IntelX | Freemium | Archives pastebins + breaches + dark web | Résultats limités en gratuit |
| **Breach** | Have I Been Pwned | Gratuit | Vérification email + mot de passe (k-anonymity) | Emails uniquement |
| **Breach** | Snusbase | Payant | Recherche par email, pseudo, hash, IP | Couverture variable |
| **Breach** | LeakCheck | Payant | Vérification credentials | Couverture variable |
| **Crypto** | OXT.me | Gratuit | Exploration blockchain Bitcoin | Bitcoin uniquement |
| **Crypto** | Chainalysis Reactor | Payant (LE) | Traçage crypto avancé multi-chain | Accès restreint |
| **Crypto** | TRM Labs | Payant | Traçage et compliance crypto | Accès restreint |
| **Ransomware** | Ransomwatch | Gratuit | Monitoring leak sites ransomware | Couverture manuelle, délai |
| **Ransomware** | Ransomfeed | Gratuit | Agrégation revendications ransomware | Couverture variable |
| **Linguistique** | Writeprints | Gratuit (académique) | Analyse de style d'écriture | Résultats indicatifs |
| **IA/NLP** | Outils NLP (spaCy, etc.) | Gratuit | Analyse linguistique automatisée | Nécessite développement |

---

### Annexe E — Grille d'évaluation de crédibilité

#### Évaluation de la source

| Critère | Score | Description |
|---------|-------|-------------|
| Ancienneté | 1-5 | 1 = nouveau compte, 5 = actif depuis 3+ ans |
| Réputation | 1-5 | 1 = aucune transaction, 5 = 100+ transactions, rating > 4.5 |
| Spécialisation | 1-5 | 1 = généraliste, 5 = spécialiste reconnu |
| Forum de publication | 1-5 | 1 = canal Telegram public, 5 = forum fermé de référence |
| Cohérence historique | 1-5 | 1 = incohérences, 5 = historique parfaitement cohérent |

#### Évaluation de l'information

| Critère | Score | Description |
|---------|-------|-------------|
| Vérifiabilité des échantillons | 1-5 | 1 = pas d'échantillon, 5 = échantillons vérifiés authentiques |
| Fraîcheur | 1-5 | 1 = données recyclées connues, 5 = données fraîches inédites |
| Corroboration | 1-5 | 1 = aucune source indépendante, 5 = confirmé par 2+ sources |
| Cohérence interne | 1-5 | 1 = incohérences majeures, 5 = parfaitement cohérent |
| Absence d'indicateurs de scam | 1-5 | 1 = indicateurs présents, 5 = aucun indicateur |

#### Niveaux de confiance résultants

| Score combiné | Niveau | Interprétation |
|--------------|--------|----------------|
| 40-50 | **Élevé** | Information probablement fiable, source crédible, corroborée |
| 25-39 | **Modéré** | Information plausible mais non confirmée |
| 10-24 | **Faible** | Information non vérifiée, source inconnue ou peu crédible |
| < 10 | **Très faible** | Probable scam, intoxication, ou données recyclées |

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
  Spécialisation : [secteur, type de données, géographie]
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

#### Template fiche d'incident data leak

```
FICHE INCIDENT DATA LEAK — [ORGANISATION]
Date de détection : [date]    Analyste : [nom]    Référence : [code]

SOURCE DE L'ALERTE
  Plateforme : [forum, Telegram, monitoring automatisé, notification externe]
  Date de l'alerte : [date]
  Crédibilité initiale : [élevée / modérée / faible]

DONNÉES OBSERVÉES
  Type : [credentials / documents / base de données / stealer logs / autre]
  Volume estimé : [nb d'entrées, taille en Go]
  Fraîcheur estimée : [date probable de la compromission]
  Exploitabilité : [critique / élevée / modérée / faible]

VÉRIFICATION
  Échantillons disponibles : [oui/non]
  Authenticité : [confirmée / probable / indéterminée / scam probable]
  Méthode de vérification : [détail]
  Recoupement avec breaches connus : [résultat]

IMPACT
  Comptes/systèmes compromis : [liste]
  Criticité : [critique / élevée / modérée / faible]
  Données personnelles concernées : [oui/non — implications RGPD]

ACTIONS EFFECTUÉES
  1. [action — responsable — date — statut]
  2. [action — responsable — date — statut]

RECOMMANDATIONS
  [liste priorisée]
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
| Internet Organised Crime Threat Assessment (IOCTA) | Europol | Annuel | Panorama menaces cyber Europe |
| Crypto Crime Report | Chainalysis | Annuel | Flux financiers criminels crypto |
| M-Trends | Mandiant/Google | Annuel | Incidents et tendances IR/CTI |
| Data Breach Investigations Report (DBIR) | Verizon | Annuel | Statistiques breaches |
| Threat Landscape | ENISA | Annuel | Menaces cyber Europe |
| Annual Dark Web Report | SOCRadar | Annuel | Pricing, tendances, marchés dark web |
| The Big Book of Deep and Dark Web | Cyberint | Ponctuel | Écosystèmes, menaces par secteur |
| Briefing dark web | EPRS (Parlement européen) | Ponctuel | Cadre réglementaire, opérations policières |
| Dark Web Price Index | Privacy Affairs | Semestriel | Prix des données et services |

#### Outils de veille gratuits

| Outil | Type | Usage |
|-------|------|-------|
| Tor Metrics (metrics.torproject.org) | Dashboard | Statistiques du réseau Tor |
| Ransomwatch | GitHub | Monitoring des leak sites ransomware |
| Ransomfeed | Site web | Agrégation revendications ransomware |
| Have I Been Pwned | Service web | Vérification exposition emails et mots de passe |
| VirusTotal | Service web | Vérification de hash, domaines, IP |
| Shodan | Service web | Recherche d'infrastructure exposée |

#### Communautés et conférences

| Ressource | Type | Description |
|-----------|------|-------------|
| FIRST | Communauté | Forum international des CERT/CSIRT |
| InterCERT France | Communauté | Association des CERT français |
| DEF CON | Conférence | Plus grande conférence hacking (Las Vegas) |
| Black Hat | Conférence | Conférence sécurité recherche/industrie |
| Botconf | Conférence | Botnets et malware (France) |
| FIC (Forum InCyber) | Conférence | Forum européen cybersécurité (Lille) |
| SSTIC | Conférence | Symposium sur la sécurité des TIC (Rennes) |
| CoRIIN | Conférence | Conférence sur la réponse aux incidents et l'investigation numérique |
| DarkOwl Blog | Blog | Analyses et rapports dark web |
| Flashpoint Blog | Blog | Intelligence menaces underground |
| Krebs on Security | Blog | Investigation cybercriminalité |

---

> **Note de clôture**
>
> Ce cours a été conçu pour former des professionnels à l'investigation et à l'analyse du dark web — pas pour satisfaire une curiosité morbide ni pour fournir un mode d'emploi d'activités illicites.
>
> Le dark web est un espace opérationnel pour l'analyste CTI, l'investigateur, et le RSSI. C'est là que les données volées apparaissent, que les accès compromis sont vendus, que les groupes de ransomware revendiquent, et que les menaces se matérialisent. Ne pas le comprendre, c'est naviguer à l'aveugle dans le paysage de la menace.
>
> Les 6 chapitres ajoutés dans cette version (Stealer logs, Investigation data leak, Marché des 0-day, NIT et techniques policières, IA et dark web, Menaces par secteur) reflètent l'évolution rapide du paysage en 2025-2026 : la commoditisation de l'accès initial via les stealer logs, l'émergence de l'IA comme outil dual (offensif et défensif), la sophistication croissante des opérations policières, et la nécessité d'une approche sectorielle de la veille.
>
> *Comprendre • Explorer • Cartographier • Investiguer • Contextualiser • Produire — avec rigueur et discernement.*
