# OSINT CRYPTO — ENQUÊTE SUR CRYPTO-ACTIFS ET BLOCKCHAIN INTELLIGENCE

*Adresse → Transaction → Entité → Flux → Cashout → Attribution prudente → Rapport*

**Cours complet — 50 chapitres, 9 parties, 10 annexes, parcours express d’ouverture.**

-----

## Avant-propos

Ce cours apprend à **investiguer les crypto-actifs** dans une posture professionnelle. Il s’adresse aux analystes CTI, investigateurs financiers, RSSI, équipes IR, professionnels de la conformité (AML/CFT), et services de renseignement. Il est conçu pour être **auto-suffisant** — un lecteur qui part de zéro, travaille le cours dans l’ordre, et fait les exercices proposés, acquiert un niveau professionnel d’enquête crypto-forensique.

**Ce que ce cours fait** : il vous apprend à lire les blockchains majeures (Bitcoin, Ethereum, TRON, Solana), à construire un raisonnement d’enquête depuis un indice (adresse, transaction hash, ransom note) jusqu’à un rapport actionnable, à utiliser les outils gratuits et professionnels (Chainalysis, TRM, Elliptic) avec discernement, à comprendre les techniques d’obfuscation (mixers, bridges, privacy coins) et leurs limites, à investiguer les grandes typologies d’abus (pig butchering, ransomware, hacks DeFi, NFT scams), et à coopérer avec VASP et autorités. Il intègre le cadre français/UE (TRACFIN, MiCA, Travel Rule, sanctions OFAC).

**Ce que ce cours ne fait pas** : il ne vous apprend pas à blanchir ou contourner la traçabilité. Il ne fournit pas de guide de cashout. Il ne promet pas l’attribution magique d’une adresse à une personne — il vous apprend à **calibrer** ce que les données publiques permettent de dire, ce qu’elles suggèrent, et ce qu’elles ne permettent pas de conclure.

**Posture pédagogique** : factuelle, calibrée, vérifiable. Chaque affirmation forte renvoie à une source publique (rapport vendor, document FATF, jurisprudence, advisory officiel). Les ordres de grandeur sont donnés avec leurs limites. Les analyses sont honnêtes sur l’incertitude.

**Continuité avec la bibliothèque** : ce cours s’articule avec **Dark Web — Comprendre, Naviguer, Investiguer** (le dark web est l’écosystème où les flux crypto illicites s’organisent), **AU CŒUR DES APT** (Lazarus et autres acteurs étatiques utilisant le crypto-laundering), **FININT — Investigation financière** (OSINT financier corporate, complémentaire à l’analyse on-chain), **Cartographie des écosystèmes cybercriminels** (contexte structurel), et **CTI** (production de renseignement actionnable). Les renvois explicites permettent d’approfondir sans dupliquer.

**Sur la séparation OSINT_Crypto / FININT** : ce cours traite l’**enquête crypto pure** (lecture blockchain, traçage on-chain, attribution probabiliste, cashout). FININT traite l’**OSINT financier classique** (registres, UBO, sanctions, structures corporate, SOCMINT financier). Beaucoup d’investigations réelles combinent les deux — les renvois inter-cours organisent cette complémentarité.

-----

## Table des matières

- [Parcours express — Lire une transaction crypto en 30 minutes](#parcours-express)
- [Fil rouge : Opération MIXSHADOW](#fil-rouge--opération-mixshadow)

**PARTIE I — COMPRENDRE L’ÉCOSYSTÈME CRYPTO SANS FANTASME**

- Ch.1 — Pourquoi l’OSINT crypto est devenu central
- Ch.2 — Ce que l’enquête crypto permet vraiment (et ne permet pas)
- Ch.3 — Lexique opérationnel des crypto-actifs
- Ch.4 — Les grandes familles de blockchains
- Ch.5 — Le métier d’analyste crypto-forensique : posture, OPSEC, éthique

**PARTIE II — LIRE LES BLOCKCHAINS**

- Ch.6 — Lire une transaction Bitcoin
- Ch.7 — Le modèle UTXO en profondeur
- Ch.8 — Lire une transaction Ethereum
- Ch.9 — Tokens et smart contracts
- Ch.10 — Stablecoins : USDT, USDC, et le rôle opérationnel
- Ch.11 — Explorateurs blockchain : méthodologie de lecture

**PARTIE III — MÉTHODOLOGIE D’ENQUÊTE**

- Ch.12 — Construire une fiche d’adresse
- Ch.13 — Point de départ d’une enquête : typologie d’indices
- Ch.14 — De l’indice au graphe : chaîne de raisonnement
- Ch.15 — Construire un graphe de flux lisible
- Ch.16 — Temporalité et chronologie d’enquête
- Ch.17 — Clustering : heuristiques, promesses et limites
- Ch.18 — Attribution : adresse → service → personne

**PARTIE IV — OUTILS ET WORKFLOW**

- Ch.19 — Outils gratuits et explorateurs avancés
- Ch.20 — Outils professionnels : Chainalysis, TRM Labs, Elliptic
- Ch.21 — Outils de visualisation
- Ch.22 — Labels publics et qualification des sources
- Ch.23 — Collecte, conservation et chaîne de preuve crypto
- Ch.24 — Workflow complet d’une enquête crypto

**PARTIE V — TYPOLOGIES D’ABUS CRYPTO**

- Ch.25 — Scams retail : romance scam et pig butchering
- Ch.26 — Ransomware et extorsion
- Ch.27 — Hacks DeFi et compromission de wallets
- Ch.28 — Fraudes NFT, tokens frauduleux, rug pulls
- Ch.29 — Acteurs étatiques : Lazarus et contournement de sanctions

**PARTIE VI — OBFUSCATION, LAUNDERING ET CASHOUT**

- Ch.30 — Le cashout : où l’on quitte l’on-chain
- Ch.31 — Mixers et tumblers
- Ch.32 — CoinJoin (Wasabi, Samourai) : analyse partielle
- Ch.33 — Bridges et cross-chain laundering
- Ch.34 — DEX, swaps et obfuscation DeFi
- Ch.35 — Privacy coins : Monero, Zcash, limites radicales

**PARTIE VII — CAS PRATIQUES DÉROULÉS**

- Ch.36 — Cas 1 : victime de pig butchering USDT Tron
- Ch.37 — Cas 2 : paiement ransomware BTC à un affilié RaaS
- Ch.38 — Cas 3 : wallet drain Ethereum par approval phishing
- Ch.39 — Cas 4 : flux multi-chaînes avec bridge et stablecoins
- Ch.40 — Cas 5 : enquête Monero — quand la blockchain ne suffit pas

**PARTIE VIII — CAS HISTORIQUES EMBLÉMATIQUES**

- Ch.41 — Bitfinex 2016 → saisie 3,6 Mrd USD 2022
- Ch.42 — Colonial Pipeline 2021 — récupération FBI
- Ch.43 — Ronin / Lazarus 2022 — 625 M USD à travers Tornado Cash
- Ch.44 — Tornado Cash — sanctions OFAC et procès
- Ch.45 — Synthèse MIXSHADOW

**PARTIE IX — PRODUCTION, CADRE ET PROFESSIONNALISATION**

- Ch.46 — Produire un rapport OSINT crypto
- Ch.47 — Échelle de confiance et formulation analytique
- Ch.48 — Coopération avec VASP, autorités et compliance
- Ch.49 — Éthique, légalité et sécurité de l’enquêteur
- Ch.50 — Maturité analyste et programme de surveillance crypto durable

**ANNEXES**

- A — Glossaire opérationnel crypto
- B — Modèle de fiche adresse
- C — Modèle de fiche transaction
- D — Modèle de timeline d’enquête
- E — Matrice des signaux d’alerte
- F — Matrice « ce que je peux conclure / ce que je ne peux pas conclure »
- G — Outils par usage (catalogue raisonné)
- H — Modèle de rapport OSINT crypto
- I — Erreurs fréquentes d’analyse
- J — 5 mini-cas synthétiques d’entraînement

-----

## Parcours express — Lire une transaction crypto en 30 minutes

> Avant les chapitres experts, ce parcours express donne les bases minimales pour ne pas être perdu. Si vous lisez régulièrement des transactions blockchain, vous pouvez le sauter. Sinon, 30 minutes ici font gagner des heures plus loin.

### Étape 1 — Qu’est-ce qu’une adresse crypto ?

Une **adresse crypto** est une chaîne de caractères qui identifie un point de réception sur une blockchain. Trois exemples concrets :

- **Bitcoin** : `bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh` (format SegWit, ~42 caractères) ou `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa` (format historique, ~34 caractères).
- **Ethereum** : `0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb1` (42 caractères, commence toujours par `0x`).
- **TRON** : `TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t` (34 caractères, commence par `T`).

**Ce qu’il faut comprendre** : une adresse est un **identifiant cryptographique** dérivé d’une clé privée. Qui contrôle la clé privée contrôle les fonds à l’adresse. **L’adresse n’est pas une personne** — c’est un endroit. Une même personne peut contrôler des milliers d’adresses ; une adresse peut être contrôlée par plusieurs personnes (multi-signature) ou par un service (exchange custodian).

### Étape 2 — Qu’est-ce qu’une transaction ?

Une **transaction** est un transfert d’actif (BTC, ETH, USDT…) d’une ou plusieurs adresses vers une ou plusieurs adresses, enregistré publiquement et **immutablement** dans la blockchain. Chaque transaction a un identifiant unique : le **TXID** (transaction hash).

Exemple Bitcoin TXID : `e3a5f9a8c1b2d4e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0` (64 caractères hexadécimaux).

Une transaction est **horodatée** (timestamp), incluse dans un **bloc** (groupé avec d’autres transactions), et propagée à tous les nœuds du réseau. Une fois confirmée (typiquement 6 confirmations pour Bitcoin, ~1h ; quelques secondes à minutes pour les blockchains plus rapides), elle est irréversible.

### Étape 3 — Comment lire un explorateur blockchain ?

Un **explorateur blockchain** (block explorer) est un site web qui affiche les transactions et adresses d’une blockchain de manière humainement lisible. Les principaux :

- **Bitcoin** : mempool.space, blockstream.info, blockchair.com.
- **Ethereum** : etherscan.io.
- **TRON** : tronscan.org.
- **Multi-chain** : blockchair.com.

Quand vous chargez l’adresse `bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh` sur mempool.space, vous voyez :

- Le **solde** actuel (combien de BTC à cette adresse).
- L’**historique des transactions** : entrées (reçues) et sorties (envoyées).
- La **première transaction** (date de création de l’adresse en activité).
- La **dernière transaction**.

C’est gratuit, public, et la base de toute enquête crypto.

### Étape 4 — Comment identifier l’actif transféré ?

Une transaction peut transférer :

- **Le coin natif** de la blockchain : BTC sur Bitcoin, ETH sur Ethereum, TRX sur TRON.
- **Un token** déployé sur cette blockchain : USDT, USDC, des milliers de tokens ERC-20 sur Ethereum, des tokens TRC-20 sur TRON.

**Sur Etherscan**, regardez :

- L’**onglet « Overview »** pour le solde ETH et l’activité native.
- L’**onglet « Token Holdings »** pour les tokens détenus.
- Les **« ERC-20 Token Txns »** pour l’historique des transferts de tokens.

Une erreur classique : voir « 0 ETH » sur une transaction et conclure qu’aucune valeur n’a été transférée. Souvent, la **valeur réelle** est dans un transfert de token (USDT par exemple), visible dans le détail mais pas dans le solde ETH.

### Étape 5 — Comment repérer un exchange, un smart contract, un bridge, un mixer ?

En cliquant sur une adresse dans Etherscan ou un autre explorateur, certaines sont **labellisées** :

- **Exchange** : `Binance Hot Wallet`, `Coinbase 1`, `Kraken Cold Storage`. Indique que l’adresse est contrôlée par un exchange.
- **Smart contract** : si l’adresse contient du code, l’explorateur l’indique avec onglet « Contract ».
- **Bridge** : `Wormhole Bridge`, `Multichain Bridge`. Permet le transfert cross-chain.
- **Mixer** : `Tornado Cash 1 ETH`, `Wasabi CoinJoin`. Service d’anonymisation.

Ces labels viennent de sources variées (annonces officielles, recherche communautaire, analyse vendor). Ils sont **utiles mais non infaillibles** — un label peut être obsolète, mal attribué, ou marketing.

### Étape 6 — Pourquoi adresse ≠ personne

C’est **le concept à intérioriser**.

Une adresse est un identifiant technique. Pour relier une adresse à une personne identifiable, il faut un **lien externe** : l’adresse a été utilisée pour s’inscrire sur un exchange KYC, l’adresse a été publiée par son propriétaire, l’adresse apparaît dans une plainte, etc.

Sans ce lien externe, l’enquête peut établir :

- Que l’adresse est **active** (transactions observables).
- Que l’adresse a **interagi** avec d’autres adresses (graphes de flux).
- Que l’adresse a **transité** par tel service (passages à des points labellisés).
- Que l’adresse fait **partie d’un cluster** (heuristiques de regroupement).

Mais elle ne peut pas, sur les seules données publiques, dire **qui contrôle** l’adresse. C’est la différence fondamentale entre **OSINT crypto** (analyse on-chain) et **investigation judiciaire** (qui peut, par réquisition, obtenir des données KYC d’un exchange).

### Étape 7 — Comment formuler une hypothèse d’enquête proprement

Au terme d’une analyse, on **n’écrit pas** : « Cette adresse appartient à X ».

On écrit (selon le niveau de preuve) :

- « Cette adresse a reçu un paiement de 0,5 BTC le [date] depuis [adresse source]. » → **fait observable**.
- « Cette adresse fait partie d’un cluster de 47 adresses présentant des heuristiques de co-spending. » → **observation analytique**.
- « Le cluster auquel appartient cette adresse a, à plusieurs reprises, déposé des fonds vers une adresse labellisée Binance Hot Wallet. » → **observation enrichie**.
- « Le pattern de flux suggère, avec un niveau de confiance modéré, une activité de collecte type pig butchering. » → **hypothèse calibrée**.
- « L’identification du titulaire effectif de l’adresse n’est pas possible sur les seules données publiques. Une réquisition auprès du VASP destinataire serait nécessaire. » → **limite explicite**.

Le **vocabulaire calibré** (Words of Estimative Probability — WEP) est la signature de l’analyste sérieux. Toute affirmation forte non démontrée détruit la crédibilité d’un rapport.

-----

Vous avez maintenant les bases pour aborder le cours. Le reste va vous apprendre à creuser chaque étape avec rigueur, méthode, et discernement.

-----

## Fil rouge : Opération MIXSHADOW

Pour ancrer la théorie dans la pratique, ce cours suit un cas fictif inspiré de cas réels. **Opération MIXSHADOW** déroule, chapitre après chapitre, l’investigation d’un paiement de rançon ransomware.

**Le contexte.** **Aurélien Médical** est un équipementier français de matériel hospitalier (700 collaborateurs, OIV santé, basé à Lyon). En mars 2026, son SI est compromis par le ransomware **Akira** (groupe RaaS actif depuis 2023). Production paralysée : machines de dialyse, scanners, pousse-seringues, dispositifs cardio-vasculaires — l’arrêt de la chaîne logicielle bloque les livraisons. Trois hôpitaux clients alertent sur des patients en attente de soins, dont des cas vitaux.

Sous pression vitale, et après concertation avec ANSSI, DGSI, ministère de la santé, et juridique, la direction d’Aurélien Médical décide de **payer la rançon**. 35 BTC (~2 M EUR au cours du moment) versés le 14 mars 2026 à l’adresse fournie par l’opérateur Akira via portail de négociation. La clé de déchiffrement est obtenue 6 heures plus tard. Reprise progressive de l’activité sur 3 semaines.

**Le mandat.** Aurélien Médical et la DGSI mandatent **Athéna Group** (cabinet CTI français, déjà acteur de DARKSTREAM) pour : **(1)** tracer les BTC payés depuis l’adresse de paiement initial ; **(2)** cartographier la chaîne de blanchiment ; **(3)** identifier les off-ramps potentiels et points de coopération ; **(4)** contribuer à l’attribution du groupe Akira (affilié individuel, équipe régionale, lien avec d’autres opérations) ; **(5)** coopérer avec TRACFIN, DGSI, et leurs homologues internationaux (FBI Cyber Division, BKA allemand, Europol EC3).

**L’analyste.** **Sarah Marin**, analyste crypto-forensique senior chez Athéna Group. 6 ans d’expérience dont 3 ans à TRACFIN comme analyste financière, transition vers le privé en 2023. Certifiée Chainalysis Reactor (CRC), TRM Labs Investigations, formation Elliptic. Background master Finance + master Cybersécurité. Collègue de **Lucas Ferreira** (DARKSTREAM) chez Athéna — ils collaborent occasionnellement sur des dossiers transverses.

**La méthode.** Sarah applique la doctrine Athéna : OPSEC stricte, outils combinés (Chainalysis Reactor pour l’investigation principale, TRM Labs en validation croisée, OXT et explorateurs publics pour la documentation reproductible), workflow méthodologique reproductible, calibration WEP systématique, livrables structurés.

**Le bilan attendu.** Sarah travaillera 8 semaines sur le dossier. Le bilan honnête, à la fin, sera : récupération **partielle** (quelques pourcents), attribution **probable** (pas certaine), apport **significatif** à un dossier multi-juridictionnel en cours, contribution à la **CTI** sectorielle santé. Pas de happy ending hollywoodien — la réalité du métier.

Les épisodes MIXSHADOW jalonnent le cours aux moments où le concept enseigné éclaire la progression de Sarah.

-----

## PARTIE I — COMPRENDRE L’ÉCOSYSTÈME CRYPTO SANS FANTASME

> **Ce que cette partie apprend.** Situer les crypto-actifs dans leur réalité économique et criminologique. Comprendre pourquoi ils sont devenus centraux dans les enquêtes financières contemporaines, ce que l’enquête crypto permet réellement (et ne permet pas), maîtriser le lexique opérationnel, distinguer les grandes familles de blockchains, et adopter la posture professionnelle d’analyste crypto-forensique.
> 
> **Ce qu’elle ne couvre pas.** Les techniques de lecture détaillée des blockchains (Partie II), les méthodes d’enquête (Partie III), les outils précis (Partie IV).
> 
> **Ce que vous saurez faire après cette partie.** Expliquer à un non-spécialiste pourquoi le crypto est traçable mais pas anonyme, présenter les limites honnêtes de l’OSINT crypto, manier le vocabulaire opérationnel, et différencier Bitcoin, Ethereum, TRON, Solana dans leur logique d’enquête.

-----

### Chapitre 1 — Pourquoi l’OSINT crypto est devenu central

Les crypto-actifs ne sont plus une curiosité technique réservée aux passionnés. En 2026, ils sont **infrastructure de transfert de valeur** pour des pans entiers de la cybercriminalité, de la fraude retail, du contournement de sanctions, et plus marginalement de l’économie légitime. L’analyste financier ou cyber qui ne sait pas lire une transaction blockchain est aujourd’hui handicapé sur une part croissante de ses dossiers.

#### 1.1 Le crypto comme infrastructure de transfert de valeur

Les blockchains publiques offrent une fonctionnalité que les systèmes bancaires traditionnels n’ont jamais su offrir aussi simplement : **transférer de la valeur de pair à pair, sans intermédiaire de confiance, à travers les frontières, en quelques minutes**. Cette propriété, neutre par construction, sert :

- L’**économie légitime** : remittances internationales (envois d’argent par les diasporas), paiements B2B cross-border, marchés DeFi régulés, achats institutionnels (entreprises listées détenant du Bitcoin en trésorerie).
- L’**économie grise** : contournement de contrôles des changes (Chine, Argentine, Liban, Nigeria), utilisation par des entrepreneurs dans des juridictions à banking dysfonctionnel.
- L’**économie criminelle** : ransomware, fraudes retail (pig butchering, Ponzi crypto), darknet markets, contournement de sanctions internationales (Russie post-2022, Corée du Nord), blanchiment d’argent.

Pour l’analyste, comprendre que le crypto est **infrastructure neutre** — pas intrinsèquement criminelle — est important. La même blockchain qui transporte une rançon ransomware transporte aussi le salaire d’un développeur ukrainien payé par une entreprise européenne. La distinction est dans **l’usage**, pas dans l’outil.

#### 1.2 Pourquoi les criminels utilisent le crypto

Plusieurs propriétés rendent les crypto-actifs attractifs pour la criminalité.

**Pseudonymat**. Les adresses ne sont pas directement reliées à l’identité civile. Pour un criminel ne maîtrisant pas l’OPSEC, c’est une protection apparente.

**Globalité**. Une transaction crypto traverse les frontières instantanément, sans contrôle bancaire intermédiaire. Pratique pour les transactions internationales criminelles.

**Irréversibilité**. Une transaction confirmée ne peut pas être annulée par chargeback (contrairement aux cartes bancaires). Pour le ransomware, c’est essentiel — la victime ne peut pas « rappeler » la rançon.

**Liquidité globale**. Les marchés crypto fonctionnent 24/7, dans toutes les juridictions, avec des centaines d’exchanges. La conversion en monnaie utilisable est, en principe, possible partout.

**Absence d’intermédiaire centralisé** (pour les blockchains publiques). Pas de banque à convaincre, pas de régulateur à contourner — du moins en théorie.

**Mais ces avantages criminels sont contrebalancés par une faiblesse structurelle** : la **traçabilité publique**. Sur une blockchain comme Bitcoin ou Ethereum, **toutes les transactions sont visibles à jamais**. C’est une différence fondamentale avec le cash (anonyme et sans trace) ou même le système bancaire (où les transactions sont privées sauf réquisition légale). Le criminel crypto laisse une trace **publique, permanente, analysable**. C’est l’opportunité que l’OSINT crypto exploite.

#### 1.3 La transparence partielle des blockchains

Les blockchains publiques sont **transparentes**. Toute transaction est visible :

- Quelle adresse a envoyé combien à quelle adresse.
- Quand (timestamp précis).
- Quel actif (BTC, ETH, USDT, etc.).
- Avec quels frais.

Cette transparence est **publique** : pas besoin d’être bank, pas besoin de réquisition, pas besoin de mandat. N’importe qui avec un explorateur peut lire les transactions de n’importe quelle adresse, à tout moment, depuis le bloc genesis.

**Mais transparence ≠ identité**. Voir qu’une adresse a reçu 10 BTC ne dit pas qui contrôle cette adresse. C’est ici qu’intervient le travail d’enquête : relier les adresses observées à des **entités** (services, individus, groupes) via des labels publics, des heuristiques de clustering, et des recoupements OSINT off-chain.

#### 1.4 Pseudonymat vs anonymat — la nuance fondamentale

**Pseudonymat** : les transactions sont publiques mais associées à des pseudonymes (adresses) qui ne révèlent pas directement l’identité. Bitcoin et Ethereum sont pseudonymes. Une fois le pseudonyme relié à une identité (KYC d’exchange, publication volontaire, erreur OPSEC), **l’historique entier devient attribuable**.

**Anonymat** : les transactions ne révèlent ni les parties ni les montants. Monero, Zcash (mode shielded). Casser cet anonymat nécessite des moyens cryptographiques avancés ou des erreurs spécifiques de l’utilisateur.

Cette distinction est **structurante** pour l’analyste :

- Sur **Bitcoin / Ethereum / TRON / Solana / la plupart des blockchains** : l’enquête est faisable, parfois fastidieuse mais méthodologiquement claire.
- Sur **Monero** : l’enquête on-chain est largement bloquée. Le travail se déplace vers les **points off-chain** (exchanges, OPSEC errors, infrastructure).

#### 1.5 « Tout est public » ne veut pas dire « tout est attribuable »

Erreur répandue, y compris chez certains journalistes : confondre la **lisibilité publique** des transactions avec la **possibilité d’attribuer** chaque adresse à une personne.

La réalité :

- **~10-20%** des adresses Bitcoin actives sont labellisées (services connus, exchanges, mixers, sanctioned entities). Source : observations Chainalysis et autres vendors.
- **~80-90%** restent **unlabelled** — appartenant à des entités non identifiées (utilisateurs particuliers, services obscurs, criminels n’ayant jamais interagi avec un service KYC).
- Les **clusters** regroupent des adresses appartenant probablement à une même entité, mais l’identification de cette entité reste ouverte sans données off-chain.

Pour le criminel sophistiqué qui n’utilise jamais un exchange KYC, dont les wallets sont créés avec OPSEC stricte, et dont les flux passent par mixers et privacy coins, **l’attribution complète peut être impossible** sur les seules données publiques.

#### 1.6 Place de l’OSINT crypto dans l’écosystème professionnel

L’OSINT crypto s’intègre dans plusieurs métiers :

**CTI (Cyber Threat Intelligence)**. Suivi de wallets de groupes ransomware, IAB, opérateurs malware. Identification de patterns de paiement. Alimentation de threat intel actionnable.

**SOC et IR**. Validation de paiements de rançon, traçage post-incident, identification de wallets compromis. Coordination avec les enquêteurs financiers.

**Forensique**. Capture et analyse de preuves crypto dans le cadre d’investigations. Documentation pour procédures judiciaires.

**Lutte anti-fraude**. Investigation de scams retail (pig butchering, faux investissements), détection de patterns de blanchiment.

**Conformité (AML/CFT)**. Screening de transactions, surveillance de clientèle, déclarations TRACFIN, application des sanctions OFAC/UE.

**Enquête judiciaire**. Soutien technique aux enquêteurs financiers et magistrats. Production de pièces à conviction. Coopération internationale via réquisitions.

**Enquête patrimoniale**. Identification d’avoirs crypto dans le cadre de successions, divorces, recouvrement de créances.

**Renseignement**. Suivi des flux financiers liés à des acteurs étatiques sanctionnés, organisations terroristes, prolifération.

Pour chacun de ces métiers, l’OSINT crypto est un **outil** parmi d’autres, à intégrer dans une démarche plus large. Rare est le dossier qui se résout uniquement par analyse on-chain — le crypto **complète** l’OSINT classique, le SIGINT, le HUMINT, la coopération institutionnelle.

#### 1.7 L’évolution 2020-2026

L’écosystème crypto et son investigation ont profondément évolué.

**Maturation des outils**. Chainalysis (fondé 2014), TRM Labs (2018), Elliptic (2013) ont structuré une industrie de la blockchain intelligence. Capacités de clustering, labellisation, scoring de risque, intégration AML — tout cela était embryonnaire en 2017, mature en 2026.

**Saisies massives**. La saisie Bitfinex (3,6 Mrd USD en 2022, Ch.41), Colonial Pipeline (2,3 M USD récupérés, Ch.42), opérations contre mixers (Helix, Bitcoin Fog, Chipmixer, Tornado Cash, Samourai) montrent que **le traçage fonctionne** — quand les ressources et la coopération internationale s’alignent.

**Diversification des typologies**. Le ransomware reste dominant en volume médiatique, mais le **pig butchering** est devenu un fléau retail en explosion (estimations Chainalysis 2024-2025 : plusieurs milliards USD/an), les **hacks DeFi** alimentent des vols récurrents, les **acteurs étatiques** (Lazarus en tête) mobilisent des techniques de plus en plus sophistiquées.

**Essor des stablecoins**. USDT et USDC sont devenus la **monnaie de transaction** de pans entiers de l’écosystème, légitime comme illicite. Le FATF souligne en 2024-2025 que les stablecoins représentent une part majeure des volumes on-chain et une fraction significative des flux illicites observables. TRON est devenu la blockchain dominante pour les flux USDT illicites en volume.

**Pression réglementaire**. MiCA en UE (entrée en vigueur 2024), Travel Rule étendue, sanctions OFAC ciblant des entités crypto (Tornado Cash août 2022, Garantex, Suex, Bitzlato), durcissement KYC sur les exchanges centralisés. L’écosystème devient progressivement **moins anonyme** par couche réglementaire.

**Intégration IA**. Les outils de blockchain intelligence intègrent du ML pour détection de patterns, automatisation d’attribution, scoring de risque. Côté criminel, l’IA assiste la création de faux profils (pig butchering automatisé), le contournement de KYC.

#### 1.8 Fil rouge — MIXSHADOW : la sollicitation

> **🔗 MIXSHADOW — Épisode 1 : le mandat**
> 
> Lundi 16 mars 2026. Sarah Marin reçoit le brief de mission. Réunion de cadrage en visio avec :
> 
> - Le **RSSI d’Aurélien Médical**, qui a piloté la cellule de crise depuis le 8 mars (date de chiffrement).
> - Deux **interlocuteurs DGSI** (officier traitant + spécialiste cyber).
> - Un **représentant TRACFIN** (cellule cyber).
> - Le **directeur d’Athéna Group**.
> 
> Le RSSI présente les faits. Compromission Akira datée du 8 mars vers 03h47 (chiffrement effectif). Vecteur d’entrée : compromission d’un compte VPN administrateur via stealer log acquis sur Russian Market (forensics Mandiant). Demande de rançon initiale : 80 BTC (~4,5 M EUR). Négociation via portail Tor descend à 35 BTC (~2 M EUR). Paiement effectué le 14 mars à 09h12. Décryption key reçue à 15h28 le même jour. Reprise opérationnelle progressive sur 3 semaines.
> 
> La DGSI précise le cadre : Athéna travaille sous mandat client (Aurélien Médical) avec **coopération étroite** mais non exclusive avec la DGSI. Remontée bi-hebdomadaire. Pas d’engagement public, TLP RED jusqu’à autorisation contraire. Coordination prévue avec Europol EC3 (le groupe Akira étant suivi par plusieurs services européens). FBI Cyber Division en partenaire potentiel via la DGSI (les US ont également des victimes Akira documentées).
> 
> Le mandat Athéna : tracer, cartographier, identifier les off-ramps, contribuer à l’attribution, coopérer.
> 
> Sarah note : objectif réaliste. Pas de promesse de récupération. La mission est de **maximiser la valeur de renseignement** extraite des 35 BTC payés, et d’alimenter des dossiers en cours qui dépassent largement le cas Aurélien Médical isolé.
> 
> Première action : préparer son environnement d’investigation et démarrer le traçage. Ch.5 détaillera l’OPSEC ; Ch.6 l’environnement ; Ch.13 le démarrage formel.

-----

### Chapitre 2 — Ce que l’enquête crypto permet vraiment (et ne permet pas)

Avant de plonger dans les techniques, il est essentiel de **calibrer les attentes**. Un mandat client mal cadré ou un management qui croit que « le crypto est traçable, donc tout se résout » conduit à des frustrations et des rapports inadaptés.

#### 2.1 Ce que l’enquête crypto permet

**Suivre des flux publics**. L’analyste peut, sur Bitcoin/Ethereum/etc., suivre les mouvements depuis une adresse de départ jusqu’à la dispersion finale ou la rupture de visibilité (mixer, privacy coin, off-ramp non coopératif). Cette traçabilité est gratuite, publique, vérifiable.

**Identifier des points de contact avec des services connus**. Quand les fonds passent par un exchange labellisé, un mixer connu, un bridge identifié — l’analyse capture ces points. Ils servent d’**ancrage** pour la suite (réquisition, coopération exchange, qualification de risque).

**Repérer des patterns**. Récurrence dans les flux, montants typiques, fenêtres temporelles, structures de wallets. Patterns qui aident à identifier la **typologie** d’activité (pig butchering, ransomware, fraude, etc.).

**Documenter un chemin de fonds**. Reconstituer, pas à pas, la trajectoire d’une somme entre l’adresse de départ et un point d’aboutissement (ou d’opacité). Cette documentation est un **livrable** essentiel — pour la victime, le procureur, l’autorité, ou la communauté CTI.

**Produire des hypothèses calibrées**. À partir des observations, formuler des hypothèses sur la nature de l’activité, les acteurs probables, les juridictions impliquées, les moyens de coopération.

**Appuyer un signalement ou une plainte**. Un rapport OSINT crypto solide permet à la victime de déposer plainte avec éléments tangibles, à TRACFIN de qualifier un signalement de soupçon, à un magistrat de fonder une commission rogatoire internationale, à une autorité de geler des fonds via émetteur stablecoin coopératif.

**Soutenir une saisie**. Quand la coopération internationale s’aligne, l’enquête OSINT prépare les éléments techniques permettant aux forces de l’ordre d’opérer une saisie effective (cf cas Bitfinex, Colonial Pipeline, Ch.41-42).

#### 2.2 Ce que l’enquête crypto ne permet pas

**Identifier directement une personne à partir d’une adresse**. Sauf cas particulier (publication volontaire, mismatch OPSEC évident, données KYC obtenues via réquisition), l’OSINT crypto pure ne donne pas l’identité civile. Le mandat « identifie qui possède cette adresse » est un mandat **mal posé**.

**Récupérer des fonds dispersés sans intervention extérieure**. L’analyste documente le chemin ; la récupération nécessite une action **off-chain** (gel par émetteur stablecoin, saisie par autorité, coopération exchange). Sans cette action, les fonds restent où ils sont.

**Casser le chiffrement Monero**. Sauf cas spécifiques (vulnérabilités d’implémentation, decoy patterns exploitables), Monero reste opaque. L’enquête se déplace vers d’autres angles.

**Démixer avec certitude un mixer custodial**. Un mixer comme Tornado Cash mélange les fonds de centaines d’utilisateurs. Reconstituer **avec certitude** les paires entrée/sortie est dans la plupart des cas impossible — sauf erreurs spécifiques (montants atypiques, timings exploitables, patterns d’usage).

**Garantir la traçabilité cross-chain sans outil professionnel**. Les bridges complexifient considérablement le suivi. Un fonds qui passe d’Ethereum à BNB Chain via plusieurs bridges, swaps DEX, et conversions stablecoin peut devenir difficile à suivre avec les seuls outils gratuits.

**Obtenir des données KYC d’exchanges**. Réservé aux autorités via réquisition légale. L’analyste OSINT prépare la cible (« cette adresse est probablement un exchange deposit address de [exchange X] »), l’autorité opère la requête.

**Produire une attribution judiciairement opposable sans corroboration**. Un rapport OSINT seul, même excellent, ne suffit généralement pas à condamner devant un tribunal. Il sert à **orienter** une enquête, pas à la conclure judiciairement.

#### 2.3 Les zones grises

Entre le « je peux » et le « je ne peux pas », plusieurs zones intermédiaires.

**Attribution probabiliste**. Avec recoupement de plusieurs signaux faibles (style d’usage, patterns temporels, infrastructure, mentions OSINT), on peut formuler une attribution **probable** (60-80% confiance). Utilisable opérationnellement, pas judiciairement.

**Identification d’une typologie d’activité**. Reconnaître qu’un cluster fait du pig butchering est généralement faisable (patterns de collection, tailles de transactions, flux vers exchanges). L’identification du **réseau précis** derrière est plus dure.

**Contribution à l’identification d’un VASP non coopératif**. Plusieurs investigations montrent qu’analyser les patterns d’un exchange permet d’identifier sa juridiction probable, ses banques partenaires, ses points faibles — utile pour pression réglementaire et coordination internationale.

**Détection de fraude en temps réel**. Avec des feeds adaptés, on peut alerter sur des transactions suspectes en cours (paiements vers des adresses sanctionnées, patterns de pump-and-dump). Capacité défensive valable, attribution post-hoc nécessaire.

#### 2.4 Calibration des attentes du mandant

Un mandat client crypto bien cadré contient :

**Périmètre clair**. Quelles adresses, quels flux, quelle période. « Tracez tout » est un mandat creux.

**Objectifs réalistes**. « Documenter le chemin des fonds, identifier les points de contact avec des services, produire un rapport actionnable » plutôt que « identifier le criminel ».

**Livrables explicites**. Rapport, captures, IoC structurés, recommandations.

**Cadre coopératif**. Avec quelles autorités, quelle TLP, quelle politique de communication.

**Budget et délai**. Une investigation crypto sérieuse prend 2-12 semaines selon complexité. Pas 48h.

**Sortie attendue**. Que doit-il se passer après le rapport ? Plainte, signalement, gel d’actifs, communication interne, threat intel partagée ?

Sarah Marin, dans MIXSHADOW, opère sous mandat **bien cadré** : le DGSI et le client sont alignés sur des attentes réalistes — pas de promesse de récupération, pas d’attribution magique, valeur ajoutée par renseignement et coopération.

#### 2.5 Le piège des promesses excessives

L’industrie de la blockchain intelligence est, à juste titre, en croissance. Mais elle peut aussi être tentée par le marketing excessif — promesses de « démixage parfait », « attribution garantie », « récupération assurée ». L’analyste sérieux résiste à ces promesses, autant pour préserver sa crédibilité que pour aligner les attentes du mandant sur la réalité opérationnelle.

Phrase à intérioriser : **« Je vais documenter tout ce que les données publiques permettent de dire. Je ne vais pas inventer ce qu’elles ne permettent pas de conclure. »** C’est la signature de l’analyste pro.

-----

### Chapitre 3 — Lexique opérationnel des crypto-actifs

Maîtriser le vocabulaire est la condition pour comprendre le reste du cours, mais aussi pour **communiquer crédiblement** avec ses interlocuteurs (autres analystes, autorités, exchanges, journalistes). Ce chapitre n’est pas un glossaire encyclopédique mais un panorama opérationnel des termes que l’analyste manipule quotidiennement.

#### 3.1 Termes fondamentaux

**Blockchain**. Registre distribué de transactions, validé cryptographiquement, partagé entre les nœuds d’un réseau. Bitcoin (depuis 2009), Ethereum (depuis 2015), TRON (depuis 2018), Solana (depuis 2020), des centaines d’autres. Chaque blockchain a ses règles propres (consensus, structure de transaction, capacités de smart contracts).

**Wallet**. Logiciel ou matériel qui stocke les clés privées et permet de signer des transactions. Distinction importante :

- **Wallet logiciel** : application sur ordinateur ou mobile (MetaMask, Phantom, Trust Wallet, Electrum).
- **Wallet matériel** : appareil dédié hors ligne (Ledger, Trezor) — plus sécurisé.
- **Wallet custodial** : géré par un tiers (exchange) qui détient les clés à votre place — Binance, Coinbase. **Vous ne contrôlez pas vraiment** les fonds.
- **Wallet non-custodial** : vous détenez les clés. « Not your keys, not your coins ».

**Adresse**. Identifiant public d’un point de réception sur une blockchain. Dérivée cryptographiquement d’une clé publique elle-même dérivée d’une clé privée. Voir Ch.3.4 pour les formats.

**Clé privée**. Secret cryptographique permettant de signer des transactions depuis une adresse. Connaissance de la clé privée = contrôle de l’adresse. Si une clé privée est compromise, les fonds peuvent être volés.

**Seed phrase / Mnemonic**. Suite de 12 ou 24 mots permettant de reconstituer une clé privée. Format standardisé (BIP-39). **Si quelqu’un obtient votre seed phrase, il prend le contrôle de tous les wallets qu’elle génère**. Utilisée pour récupération.

**Transaction (TX)**. Transfert d’actif entre adresses, signé cryptographiquement, propagé sur la blockchain.

**Transaction hash (TXID)**. Identifiant unique d’une transaction. Référence pour citer ou rechercher une transaction.

**Bloc**. Groupe de transactions agrégées et validées ensemble. Identifié par un numéro (block height) et un hash.

**Confirmations**. Nombre de blocs ajoutés depuis qu’une transaction a été incluse. Plus de confirmations = plus de finalité. Bitcoin : 6 confirmations standard (~1h). Ethereum post-Merge : finalité après ~12-15 minutes.

#### 3.2 Termes économiques

**Coin natif**. L’actif intrinsèque d’une blockchain. BTC sur Bitcoin, ETH sur Ethereum, TRX sur TRON, SOL sur Solana, BNB sur BNB Chain.

**Token**. Actif déployé sur une blockchain via un smart contract (sans avoir sa propre blockchain). USDT, USDC, des dizaines de milliers d’autres. Distinction des standards :

- **ERC-20** sur Ethereum (et chaînes EVM-compatibles).
- **TRC-20** sur TRON.
- **BEP-20** sur BNB Chain.
- **SPL** sur Solana.

**Stablecoin**. Token dont la valeur est arrimée à une référence stable (généralement USD). USDT (Tether), USDC (Circle), DAI (MakerDAO). Détaillé Ch.10.

**NFT (Non-Fungible Token)**. Token unique non-divisible (contrairement aux fungibles type USDT). ERC-721 standard sur Ethereum. Représente collectibles, art numérique, droits, etc.

**Gas**. Frais de transaction sur Ethereum (et chaînes EVM). Mesuré en gwei (10^-9 ETH). Plus le réseau est congestionné, plus le gas coûte cher.

**Mining / Staking**. Mécanismes de validation des blocs. Bitcoin utilise Proof-of-Work (mining). Ethereum a basculé en Proof-of-Stake en septembre 2022 (The Merge). Implications pour l’analyste : peu directes, mais impact sur certaines heuristiques.

#### 3.3 Termes d’enquête

**UTXO (Unspent Transaction Output)**. Modèle Bitcoin (et clones) où chaque transaction consomme des « pièces » (outputs précédents) et en génère de nouvelles. Détaillé Ch.7.

**Account model**. Modèle Ethereum (et chaînes EVM) où les adresses ont un solde directement (pas d’UTXO). Plus simple en surface, complexité différente en profondeur. Détaillé Ch.8.

**Clustering**. Regroupement d’adresses appartenant probablement à la même entité, basé sur des heuristiques (co-spending, change detection, etc.). Détaillé Ch.17.

**Attribution**. Association d’une adresse ou d’un cluster à une entité identifiable (exchange, mixer, individu, organisation). Niveaux de confiance variables. Détaillé Ch.18.

**Label**. Étiquette publique ou propriétaire associée à une adresse. Sources : annonces officielles, recherche communautaire, vendor commerciaux. Détaillé Ch.22.

**Heuristique**. Règle d’inférence non garantie, utilisée pour faire des hypothèses. Exemple : « si plusieurs inputs sont co-dépensés dans une même transaction, ils appartiennent probablement à la même entité ».

**Peeling chain**. Technique d’obfuscation Bitcoin où une grosse somme est progressivement « épluchée » en transferts successifs, chaque transaction laissant un petit montant à un destinataire et le reste à une nouvelle adresse de change. Détaillé Ch.7.

**Cluster**. Ensemble d’adresses regroupées comme appartenant probablement à la même entité.

**Cashout / Off-ramp**. Conversion de crypto en monnaie utilisable (fiat, biens, services). Le moment où l’on **quitte la blockchain**. Point critique d’enquête. Détaillé Ch.30.

#### 3.4 Termes liés aux services

**CEX (Centralized Exchange)**. Plateforme d’échange centralisée. Binance, Coinbase, Kraken, OKX, Bybit, Bitstamp, Bitfinex. Détient les fonds des utilisateurs (custodial). Soumis à KYC dans les juridictions régulées.

**DEX (Decentralized Exchange)**. Plateforme d’échange décentralisée, sur smart contracts. Uniswap, PancakeSwap, Curve, dYdX. Pas de KYC (en principe), pas de custodian. L’utilisateur conserve ses clés.

**VASP (Virtual Asset Service Provider)**. Terme FATF désignant tout service qui manipule des actifs virtuels (exchanges, custodians, wallet providers, parfois DEX selon interprétation). Soumis à la Travel Rule.

**Bridge**. Pont permettant le transfert d’actifs entre blockchains. Wormhole, Multichain (compromis 2023), Stargate, etc. Souvent ciblé par hacks (cf Ronin, Ch.43). Détaillé Ch.33.

**Mixer / Tumbler**. Service mélangeant les fonds de plusieurs utilisateurs pour casser la traçabilité. Tornado Cash (sanctionné 2022), Helix (saisi 2020), Bitcoin Fog (saisi 2021), Chipmixer (saisi 2023), Samourai (saisi 2024). Détaillé Ch.31.

**CoinJoin**. Technique de mélange Bitcoin coopérative (sans custodian central). Wasabi, Samourai. Détaillé Ch.32.

**Privacy coin**. Cryptomonnaie conçue pour anonymat. Monero, Zcash, Dash. Détaillé Ch.35.

**Smart contract**. Programme déployé sur une blockchain, exécuté quand des conditions sont remplies. Ethereum est la blockchain pionnière. Détaillé Ch.9.

**DeFi (Decentralized Finance)**. Écosystème d’applications financières sur blockchain (DEX, lending, yield farming, dérivés). Détaillé Ch.34.

#### 3.5 Termes liés à la conformité et la réglementation

**KYC (Know Your Customer)**. Procédure d’identification des clients par les VASP. Exigée par MiCA et la plupart des juridictions sérieuses.

**AML (Anti-Money Laundering) / CFT (Counter-Financing of Terrorism)**. Cadre réglementaire de lutte contre le blanchiment et le financement du terrorisme.

**Travel Rule**. Recommandation FATF étendue aux VASP : pour transferts au-delà d’un certain seuil (1 000 USD/EUR), l’expéditeur doit transmettre des informations sur l’expéditeur et le destinataire au VASP destinataire.

**MiCA (Markets in Crypto-Assets)**. Règlement UE 2023/1114, entré en vigueur progressivement à partir de 2024. Cadre réglementaire crypto unifié pour l’UE.

**Sanctions OFAC**. Sanctions américaines ciblant entités, individus, et désormais adresses crypto. Tornado Cash (août 2022), Garantex, Suex, Bitzlato, multiples wallets Lazarus.

**TRACFIN**. Cellule française de renseignement financier. Reçoit les déclarations de soupçon des assujettis (banques, VASP). Cadre français de lutte AML/CFT.

**SAR (Suspicious Activity Report)**. Déclaration de soupçon (équivalent international du signalement TRACFIN).

#### 3.6 Termes spécifiques d’enquête

**Drainer**. Smart contract ou script malveillant qui vide automatiquement un wallet une fois que la victime signe une transaction d’approval. Vecteur de phishing crypto majeur 2022-2026.

**Approval**. Permission accordée à un smart contract de dépenser certains tokens. Mécanisme légitime (DEX, lending) mais détourné par phishing.

**Rug pull**. Arnaque où les créateurs d’un projet crypto disparaissent avec les fonds des investisseurs. Variante : honeypot token (impossible à revendre).

**Pig butchering** (« 杀猪盘 », shā zhū pán). Type de fraude combinant manipulation sentimentale (romance scam) et faux investissement crypto. Volumes massifs depuis 2022. Ch.25 détaillé.

**Pump-and-dump**. Manipulation coordonnée du cours d’un token : achats coordonnés (pump) suivis d’une revente massive (dump) qui plante le cours.

**Wash trading**. Fausses transactions entre wallets contrôlés par la même entité, pour simuler du volume.

**Dust attack**. Envoi de petits montants vers de nombreuses adresses pour tenter de les corréler par heuristiques de co-spending si elles « consolident » la poussière.

-----

### Chapitre 4 — Les grandes familles de blockchains

Toutes les blockchains ne sont pas équivalentes. Pour l’analyste, comprendre les différences structurelles entre familles est essentiel — elles déterminent les méthodes d’enquête applicables, les outils utilisables, et les patterns à observer.

#### 4.1 Bitcoin et le modèle UTXO

**Bitcoin** (lancé 2009). Première blockchain. Modèle **UTXO** (Unspent Transaction Output). Pas de smart contracts (au sens Ethereum) — Bitcoin est volontairement minimaliste.

**Caractéristiques pour l’enquête** :

- **Très grande lisibilité** : chaque transaction est un graphe d’inputs et outputs.
- **Heuristiques de clustering matures** (co-spend, change detection, peeling).
- **Outils nombreux** : Mempool.space, Blockstream.info, OXT, Breadcrumbs, Chainalysis, etc.
- **Communauté de recherche active** depuis 15+ ans.

**Usages illicites observés** : ransomware (BTC reste dominant pour les rançons selon Chainalysis 2024-2025), darknet markets (BTC + Monero), saisies historiques (Silk Road, AlphaBay, Bitfinex, Colonial Pipeline). En **baisse relative** vs stablecoins pour les autres typologies.

**Forks et clones notables** : Bitcoin Cash (BCH), Bitcoin SV (BSV), Litecoin (LTC), Dogecoin (DOGE). Mêmes principes d’analyse. Volumes illicites significativement moindres.

#### 4.2 Ethereum et chaînes EVM

**Ethereum** (lancé 2015). Modèle **account-based** (pas UTXO). Introduction des **smart contracts** programmables. Dominance dans DeFi, NFT, DAO, et multiples couches d’application.

**Caractéristiques pour l’enquête** :

- **Lisibilité bonne mais différente** : transactions plus simples (un emetteur, un destinataire, un montant), mais complexité dans les **internal transactions** (appels entre smart contracts) et **logs d’événements**.
- **Outil dominant** : Etherscan.
- **Tokens omniprésents** : transferts ETH directs souvent moins importants que les transferts de tokens (USDT, USDC, autres).

**EVM (Ethereum Virtual Machine) compatibles** : BNB Chain, Polygon, Avalanche, Arbitrum, Optimism, Fantom, Base. **Mêmes principes d’enquête**, mêmes adresses (compatibles 0x…), mêmes outils dérivés (BscScan, PolygonScan, etc.). L’analyste qui maîtrise Ethereum peut travailler sur ces chaînes avec courbe d’apprentissage faible.

**Usages illicites** : DeFi exploits, rug pulls, NFT scams, drainers de wallets, certains flux ransomware (en hausse). Moins dominante que Bitcoin pour ransomware, mais centrale pour fraudes retail et acteurs étatiques (Lazarus utilise massivement Ethereum + Tornado Cash).

#### 4.3 TRON

**TRON** (lancé 2018, fondateur Justin Sun). Blockchain à modèle compte, transactions très bon marché (~quelques centimes USD), confirmation rapide (~3 secondes).

**Caractéristiques structurantes pour l’enquête** :

- **USDT-TRON est dominant** : la blockchain TRON est devenue **la plate-forme principale** pour les flux USDT, légitimes et illicites. Source : observations Chainalysis, TRM Labs, Elliptic 2024-2026.
- **Frais minimes** : un transfert USDT-TRON coûte ~1 centime, contre ~5-30 USD sur Ethereum (selon congestion). Cette économie attire les flux à haute fréquence, dont le pig butchering et certaines opérations de blanchiment.
- **Confirmation rapide** : en 3 secondes, une transaction est finalisée. Pratique pour les criminels qui veulent disperser rapidement.
- **Outil principal** : Tronscan.

**Usages illicites observés** : pig butchering massif (volumes en milliards USD selon estimations), certaines fraudes ransomware (en hausse), opérations Lazarus, blanchiment et placement.

**Critique** : l’écosystème TRON est moins coopératif sur la régulation que d’autres. La fondation TRON est controversée. Plusieurs procédures aux US visent Justin Sun et entités liées.

**Pour l’analyste** : TRON ne peut **pas être ignoré**. Une part majeure des flux illicites stablecoin y transite. Maîtriser Tronscan et les heuristiques TRON est aussi important que maîtriser Etherscan.

#### 4.4 Solana

**Solana** (lancé 2020). Architecture différente, très haute performance (théorique 65 000 TPS), confirmation quasi-instantanée, frais infimes.

**Caractéristiques pour l’enquête** :

- **Modèle compte** différent d’Ethereum (account model spécifique Solana).
- **Tokens SPL** (Solana Program Library) — équivalent ERC-20.
- **Outil** : Solscan, Solana Explorer.
- **Volumes croissants** : DeFi Solana, NFT Solana, memecoins (pump.fun et écosystème associé 2024-2025).

**Usages illicites observés** : memecoin scams massifs (rug pulls quasi-industriels via pump.fun), certaines fraudes retail. En forte croissance.

**Pour l’analyste** : Solana est **moins mature** dans l’outillage forensique que Bitcoin/Ethereum. Les outils commerciaux (Chainalysis, TRM, Elliptic) couvrent Solana mais avec moins de profondeur historique. Les heuristiques de clustering sont moins éprouvées.

#### 4.5 Autres chaînes pertinentes

**BNB Chain (ex-Binance Smart Chain)**. EVM-compatible. Volumes massifs, particulièrement DeFi et memecoins. Outil : BscScan.

**Polygon**. Layer-2 Ethereum. EVM-compatible. Croissance.

**Avalanche**. EVM-compatible. Subnets. Croissance modérée.

**Arbitrum, Optimism, Base**. Layer-2 Ethereum (rollups). EVM-compatibles. Forte croissance 2023-2026.

**Cosmos écosystème** (Cosmos Hub, Osmosis, etc.). Différent d’Ethereum, IBC pour cross-chain. Outils moins matures.

**XRP Ledger (Ripple)**. Modèle différent. Usage majoritaire institutionnel.

**Stellar**. Similaire dans la philosophie à XRP.

#### 4.6 Privacy coins

**Monero (XMR)** (lancé 2014). Anonymat par construction. Ring signatures, RingCT, stealth addresses. Détaillé Ch.35.

**Zcash (ZEC)** (lancé 2016). Optionnellement anonymisable (transparent par défaut, shielded en option). Une fraction des transactions est shielded.

**Dash** (lancé 2014). Anonymisation via PrivateSend (CoinJoin amélioré). Moins efficace que Monero, plus simple à analyser.

**Pour l’analyste** : Monero est **largement opaque**. Zcash transparent est lisible. Zcash shielded est opaque (mais peu utilisé en pratique). Dash est analysable avec effort.

#### 4.7 Implications opérationnelles

**Pour Bitcoin**, l’analyste a besoin :

- Maîtrise du modèle UTXO.
- Heuristiques de clustering (co-spend, change).
- Outils : Mempool.space, OXT, Chainalysis.

**Pour Ethereum et EVM-chains**, l’analyste a besoin :

- Compréhension du model account.
- Lecture de smart contracts et events.
- Outils : Etherscan + équivalents par chaîne.

**Pour TRON**, l’analyste a besoin :

- Maîtrise de Tronscan.
- Spécificités USDT-TRON.
- Patterns pig butchering et blanchiment.

**Pour Solana**, l’analyste a besoin :

- Solscan.
- Spécificités SPL tokens.
- Conscience des limites d’outillage forensique.

**Pour Monero**, l’analyste se prépare à :

- Utiliser les **points off-chain** (exchanges, KYC, OPSEC errors).
- Documenter la rupture de visibilité.

Une enquête moderne touche **fréquemment plusieurs chaînes**. L’analyste polyvalent est l’analyste utile.

-----

### Chapitre 5 — Le métier d’analyste crypto-forensique

Avant les techniques, la **posture professionnelle**. Ce chapitre couvre les compétences, l’OPSEC, l’éthique, et l’organisation du métier.

#### 5.1 Le profil d’analyste crypto-forensique

**Compétences techniques** :

- Lecture fluide des blockchains majeures (Bitcoin, Ethereum, TRON minimum).
- Maîtrise des explorateurs publics (Mempool, Etherscan, Tronscan).
- Maîtrise d’au moins un outil professionnel (Chainalysis, TRM, ou Elliptic) si budget disponible.
- Capacité à lire et interpréter du code de smart contract basique (Solidity).
- Compréhension des techniques d’obfuscation (mixers, bridges, swaps).
- Fluence avec un environnement Python pour scripts d’analyse personnalisés.

**Compétences analytiques** :

- Méthodologie d’enquête structurée.
- Vocabulaire calibré (WEP).
- Capacité de discernement (distinguer observation, inférence, attribution).
- Discipline anti-biais.
- Rédaction analytique claire.

**Compétences transverses** :

- Curiosité (l’écosystème évolue, il faut suivre).
- Rigueur (la documentation conditionne la valeur du travail).
- Patience (les enquêtes prennent semaines/mois).
- Communication (rapports adaptés à des audiences variées).
- Éthique (résistance aux dérives, alignement avec mandat).

**Background typique** :

- Parcours **finance/AML** reconverti vers crypto (ex-banquier, ex-analyste TRACFIN, ex-compliance officer).
- Parcours **technique/cyber** étendu vers crypto (ex-SOC, ex-pentester, ex-CTI).
- Parcours **académique** (master Finance, master Cybersécurité, parfois doctorat en cryptographie).
- Parcours **enquêteur** (gendarmerie/police, services de renseignement) reconverti.

Sarah Marin, dans MIXSHADOW, illustre le profil hybride : 3 ans TRACFIN (analyste financière) puis 3 ans Athéna (crypto-forensique pure). Combinaison appréciée.

#### 5.2 OPSEC de l’analyste crypto

L’analyste crypto manipule des données sensibles : adresses de criminels actifs, flux en cours, méthodologies. Plusieurs principes OPSEC.

**Séparation des univers**. Ne pas mélanger comptes personnels et infrastructure d’investigation. Une machine dédiée pour les analyses sensibles (comme pour Dark Web — voir cours associé).

**Wallet d’investigation séparé**. Si l’enquête nécessite des transactions de test (rare en OSINT pur, plus fréquent en undercover), wallet dédié, financé par circuit professionnel, jamais lié à l’identité personnelle de l’analyste.

**Pas d’interaction directe avec les wallets cibles**. L’analyste OSINT **observe**, il ne **transacte pas** avec les wallets criminels. Envoyer même 1 satoshi vers un wallet ransomware peut alerter l’opérateur et compromettre l’investigation. C’est aussi potentiellement illégal (financement de groupe sanctionné selon l’acteur).

**Pas de phishing aux acteurs**. Tentation parfois : « contacter le scammer en feignant être une victime ». Cela dépasse souvent le cadre OSINT et peut tomber dans l’enquête sous couverture, réservée aux autorités.

**Documentation immédiate**. Toute observation est captée, horodatée, hachée. Pas de mémoire orale. Voir Ch.23.

**Pas de rediffusion incontrôlée**. Les observations ne sont partagées qu’au cercle justifié (mandant, autorités, ISAC selon TLP). Pas de bavardage entre analystes ou avec journalistes.

**Confidentialité du mandat client**. Sauf accord explicite, l’identité du mandant et la nature exacte de l’enquête restent confidentielles, y compris vis-à-vis de l’écosystème pro.

#### 5.3 Cadre éthique

**Principes** :

**Légalité scrupuleuse**. L’OSINT crypto opère dans un cadre légal — RGPD, sanctions, AML, secret professionnel. L’analyste connaît le cadre applicable à son périmètre.

**Mandat respecté**. L’enquête se déroule selon le mandat. Pas d’extension non autorisée vers d’autres cibles, pas de curiosité incontrôlée.

**Minimisation**. Collecter ce qui est nécessaire. Ne pas extraire systématiquement toutes les données accessibles « au cas où ».

**Non-prolifération**. Les données collectées ne fuitent pas hors du cercle justifié.

**Calibration honnête**. Ne pas embellir les conclusions. Ne pas masquer les limites.

**Respect des victimes**. Beaucoup d’enquêtes impliquent des victimes (pig butchering, ransomware). Leurs données et leur dignité sont respectées.

**Coopération avec autorités**. Si l’enquête révèle des infractions graves, signalement obligatoire (article 40 CPP pour fonctionnaires, signalement TRACFIN pour assujettis).

**Refus des dérives**. L’analyste résiste aux pressions pour produire des rapports orientés (« attribuer cet acteur à tel groupe pour des raisons politiques »).

#### 5.4 Outils, certifications, formation

**Certifications utiles** :

- **Chainalysis Certified Reactor (CRC)** : référence industrie, formation officielle Chainalysis.
- **TRM Labs Certified Investigator (CTI)** : certification TRM Labs.
- **Certified Cryptocurrency Investigator (CCI)** : certification de la blockchain forensics community.
- **CAMS (Certified Anti-Money Laundering Specialist)** : certification AML transverse, utile pour le contexte.

**Formations courtes** :

- **Bellingcat OSINT trainings** (volet crypto inclus).
- **SANS FOR578 / FOR589** (CTI / cybercrime intelligence, modules crypto).
- **Webinars vendors** (Chainalysis, TRM, Elliptic — gratuits ou peu coûteux).

**Auto-formation** :

- Lecture des rapports annuels Chainalysis Crypto Crime, TRM Labs reports, Elliptic publications.
- Suivre Twitter/X de chercheurs publics : @zachxbt, @mishasolovyov (Solovyov), @pcaversaccio (smart contract security), @0x_lasagna, @samczsun (security DeFi), @tayvano_ (Tay).
- Outils de pratique : explorateurs publics gratuits, analyse de cas historiques publiés.
- Communautés : OnChain Investigators, OSINT Curious, SEAL ISAC.

**Veille à entretenir** :

- Rapports Chainalysis (annuels + mid-year updates).
- TRM Labs blog et threat reports.
- Elliptic publications.
- Rapports FATF (Virtual Assets, Targeted Financial Sanctions, etc.).
- Bulletins OFAC SDN.
- Travaux ZachXBT (chercheur indépendant prolifique).
- Blogs communautaires (Defillama, DeFiLlama Adapter, Rekt News pour les hacks).

#### 5.5 L’organisation du travail

**Outillage informatique** :

- Machine principale propre (Linux ou macOS, Windows acceptable).
- VM dédiée pour analyses sensibles (Whonix ou équivalent si interaction Tor).
- Espace de stockage dédié et sauvegardé pour les preuves.
- Outils de capture (Hunchly ou équivalent).
- Outils blockchain (cf Partie IV).

**Workflow type** :

- Réception du mandat / alerte.
- Cadrage et planification.
- Investigation structurée (Partie III).
- Documentation continue.
- Rédaction du rapport (Ch.46).
- Présentation et coopération.
- Clôture et archivage.

**Gestion des dossiers** :

- Un dossier = un répertoire structuré (notes, captures, exports, rapport final).
- Versioning (Git ou équivalent pour rapports).
- Archivage immutable post-clôture.

**Travail en équipe** :

- Pour les grandes investigations, plusieurs analystes (un lead, des contributeurs).
- Partage via plateforme sécurisée (Mattermost, Element/Matrix self-hosted, etc.).
- Peer review systématique des rapports.

#### 5.6 Carrière et évolution

**Trajectoires possibles** :

- **Cabinet de conseil / forensique** : Athéna (fictif), Wavestone, Mandiant, Kroll, etc.
- **Vendor blockchain intelligence** : Chainalysis, TRM Labs, Elliptic recrutent.
- **Forces de l’ordre** : SDLC, OFAC français, gendarmerie nationale (cellule cyber), magistrature spécialisée.
- **TRACFIN, ANSSI, DGSI**.
- **Compliance d’exchange ou banque** : équipes AML internes des VASP régulés.
- **Renseignement** : DGSE, services partenaires.
- **Indépendant** : ZachXBT comme modèle (mais rare).

**Évolution des compétences** :

- Junior (0-2 ans) : maîtrise technique, lecture, outils.
- Senior (3-7 ans) : pilotage d’enquêtes complètes, mentoring, livrables.
- Lead (7+ ans) : direction d’équipe, méthodologie, contribution doctrinale.

**Rémunération** (indicatif France 2025-2026) : junior 45-55 k€, senior 65-90 k€, lead 100-150 k€+. Plus élevé chez vendors (Chainalysis, TRM) et en finance (banques d’investissement, hedge funds).

#### 5.7 Fil rouge — MIXSHADOW : préparation de l’analyste

> **🔗 MIXSHADOW — Épisode 2 : setup**
> 
> Sarah prépare son environnement. Protocole Athéna pour MIXSHADOW :
> 
> - **Machine dédiée** : laptop sécurisé, OS Ubuntu LTS hardened, accès limité au sous-réseau d’investigation.
> - **Outils blockchain** : Chainalysis Reactor (licence Athéna), TRM Labs Investigations (validation croisée), Etherscan/Tronscan/Mempool en accès direct, scripts Python pour exports CSV.
> - **Espace de travail** : dossier MIXSHADOW chiffré, accès restreint à l’équipe (Sarah + 1 analyste junior + revue par directeur Athéna), backup quotidien sur stockage immutable.
> - **Documentation** : Hunchly pour captures de pages d’explorateur, journal d’enquête en Markdown, exports CSV horodatés et hashés.
> - **Pas de wallets de test** : MIXSHADOW est OSINT pur, pas d’interaction transactionnelle.
> - **Communication** : Element/Matrix interne Athéna pour discussions équipe, email chiffré avec DGSI, audio sécurisé pour les briefings.
> 
> Avant de démarrer le traçage proprement dit, Sarah complète le **dossier de cadrage** : périmètre, objectifs, livrables attendus, contacts, échéances. Validation directeur Athéna et DGSI. Le cadrage prend 4 heures — temps bien investi.
> 
> Action immédiate : récupérer l’**adresse Bitcoin** où les 35 BTC ont été versés. Le RSSI Aurélien Médical fournit la clé : adresse de paiement BTC fournie par Akira via portail Tor, montant exact 35,00000000 BTC, TXID de la transaction de paiement, timestamp 14 mars 09:12 UTC.
> 
> Sarah valide le TXID sur Mempool.space. Le paiement est bien enregistré, 6 confirmations atteintes. Adresse réceptrice : `bc1q...[adresse fictive de 42 caractères]`. Premier nœud du graphe MIXSHADOW.
> 
> Ch.6 va détailler comment lire cette transaction Bitcoin en profondeur. Ch.13 reprendra MIXSHADOW pour l’investigation proprement dite.

-----

## PARTIE II — LIRE LES BLOCKCHAINS

> **Ce que cette partie apprend.** Lire concrètement les blockchains majeures. Décortiquer une transaction Bitcoin, comprendre le modèle UTXO, lire une transaction Ethereum, manipuler tokens et smart contracts, maîtriser les stablecoins et leur logique opérationnelle, naviguer dans les explorateurs.
> 
> **Ce qu’elle ne couvre pas.** Les méthodes d’enquête (Partie III), les outils professionnels (Partie IV), les techniques d’obfuscation (Partie VI).
> 
> **Ce que vous saurez faire après cette partie.** Lire une transaction Bitcoin sans confondre change et destinataire, interpréter une transaction Ethereum incluant transferts de tokens et internal transactions, comprendre pourquoi un même actif (USDT) se comporte différemment selon la blockchain, et naviguer fluidement Mempool/Etherscan/Tronscan.

-----

### Chapitre 6 — Lire une transaction Bitcoin

Bitcoin est la blockchain la plus ancienne, la plus étudiée, et celle dont l’analyse a le corpus de connaissances le plus mature. Mais sa lecture demande un changement mental par rapport au modèle bancaire classique. Ce chapitre apprend à lire une transaction Bitcoin sans erreur d’interprétation — en particulier la confusion fréquente entre **destinataire** et **adresse de change**.

#### 6.1 Anatomie d’une transaction Bitcoin

Une transaction Bitcoin a la structure suivante :

```
Transaction TXID: e3a5f9a8c1b2d4e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0
Block height: 825 432
Timestamp: 2026-03-14 09:12:34 UTC
Confirmations: 6+

INPUTS:
  Input 0:
    From: bc1qsource1address...
    Amount: 0.4 BTC
  Input 1:
    From: bc1qsource2address...
    Amount: 0.6 BTC
  Total inputs: 1.0 BTC

OUTPUTS:
  Output 0:
    To: bc1qdestination...
    Amount: 0.7 BTC
  Output 1:
    To: bc1qchange...
    Amount: 0.299 BTC

Fee: 0.001 BTC (= total inputs - total outputs)
```

**Concepts clés** :

**Inputs** : références à des outputs **précédents** (UTXO non dépensés) que cette transaction va consommer. Chaque input pointe vers un TXID + index d’output dans une transaction antérieure. L’expéditeur prouve qu’il contrôle ces UTXO en signant.

**Outputs** : nouveaux UTXO créés par cette transaction. Chacun assigne un montant à une adresse destinataire.

**Frais (fees)** : différence entre total inputs et total outputs. Va aux mineurs qui valident le bloc.

**Pas de notion de « solde »** explicite dans Bitcoin. Une adresse a un solde **calculé** comme la somme de ses UTXO non dépensés.

#### 6.2 La confusion classique : destinataire vs change

Reprenons l’exemple ci-dessus. Une lecture **naïve** dirait :

- L’expéditeur a envoyé 1 BTC à 2 destinataires : 0,7 BTC à `bc1qdestination` et 0,299 BTC à `bc1qchange`.
- Donc deux destinataires.

**Cette lecture est très probablement fausse**. La réalité, dans la grande majorité des cas :

- **Le vrai destinataire** est `bc1qdestination` qui reçoit 0,7 BTC.
- **`bc1qchange` est une adresse de change** : c’est une adresse contrôlée par **l’expéditeur lui-même**, qui récupère le « rendu de monnaie ». L’expéditeur avait des UTXO totalisant 1 BTC mais voulait n’envoyer que 0,7 BTC, donc il s’envoie 0,299 BTC à lui-même (le reste 0,001 BTC va aux frais).

**Pourquoi ce mécanisme ?** Bitcoin est **UTXO**. On ne peut pas « dépenser une partie d’un UTXO » — on consomme l’UTXO entier et on en crée de nouveaux. Si vous avez un UTXO de 1 BTC et voulez envoyer 0,7 BTC, vous devez consommer le UTXO de 1 BTC entier, créer un output de 0,7 BTC pour le destinataire, et un output de 0,299 BTC qui revient à vous (moins les frais).

**Erreur classique de lecture** : conclure que `bc1qchange` est un destinataire distinct, l’ajouter au graphe d’enquête comme entité séparée, le suivre comme un acteur indépendant. C’est une erreur **fondamentale** qui pollue toute l’enquête.

#### 6.3 Reconnaître l’adresse de change

Plusieurs heuristiques permettent d’identifier l’adresse de change.

**Heuristique du nouveau wallet**. Le change va typiquement vers une **nouvelle adresse fraîchement générée** (jamais utilisée auparavant). Les adresses « destinataires » sont plus souvent réutilisées. Si dans une transaction vous avez deux outputs et que l’un pointe vers une adresse fraîche jamais vue, c’est probablement le change.

**Heuristique du round number**. Le destinataire reçoit souvent un **montant rond** (1 BTC, 0,5 BTC, 0,1 BTC). Le change reçoit un montant non-rond (0,299 BTC dans l’exemple). Si vous voyez `0,7000` et `0,2998` en outputs, le `0,7000` est très probablement le destinataire.

**Heuristique du script type**. Le change utilise **généralement le même type d’adresse** que les inputs (P2PKH, P2SH, SegWit, Taproot). Le destinataire peut être de type différent. Heuristique faible isolément, plus forte combinée.

**Heuristique du wallet client**. Certains wallets (Electrum, par exemple) ont des patterns comportementaux récurrents dans la sélection d’adresses de change. Un analyste expérimenté reconnaît parfois le wallet utilisé d’après la structure.

**Limitation** : aucune de ces heuristiques n’est **certaine**. Chacune a un taux d’erreur. Les outils professionnels (Chainalysis, TRM, Elliptic) combinent plusieurs heuristiques + ML pour scorer la probabilité.

#### 6.4 Les inputs multiples : co-spending

Dans l’exemple, la transaction consomme deux inputs (0,4 BTC + 0,6 BTC). C’est le **co-spending**.

**Heuristique du co-spend (« common-input ownership »)** : si plusieurs inputs sont dépensés ensemble dans une même transaction, ils sont **probablement contrôlés par la même entité**. Pourquoi ? Parce que dépenser plusieurs UTXO ensemble nécessite de signer chacun avec sa clé privée. Une entité qui ne contrôle pas les deux clés ne peut pas faire cette transaction.

**Forte mais pas absolue** : exceptions notables :

- **CoinJoin** : protocole coopératif où plusieurs parties signent ensemble une transaction sans partager les clés (Ch.32). Dans un CoinJoin, les inputs **ne sont PAS contrôlés par la même entité**. Heuristique caduque.
- **Multi-sig collaboratif** : plus rare mais existe.
- **Transactions exchange** : un exchange agrège les fonds de plusieurs utilisateurs dans des UTXO, puis les re-dispatche. Le co-spending au niveau exchange ne dit rien sur les utilisateurs finaux.

L’heuristique du co-spend est **la base du clustering Bitcoin**. Les outils modernes l’appliquent en masse pour regrouper des millions d’adresses en clusters d’entité probable.

#### 6.5 Lire une transaction sur Mempool.space

**Mempool.space** est un excellent explorateur Bitcoin gratuit, open source, populaire dans la communauté. Walkthrough de lecture.

**1. Ouvrir mempool.space**. Page d’accueil avec mempool actuel, transactions récentes, statistiques.

**2. Coller un TXID** dans la barre de recherche. La page transaction s’affiche.

**3. Ce qu’on voit** :

- **Header** : block height, timestamp, confirmations.
- **Inputs** : liste avec adresse source, montant, lien vers transaction d’origine.
- **Outputs** : liste avec adresse destinataire, montant.
- **Fee** : frais payés.
- **Size** : taille de la transaction en octets (impacte les fees).
- **Vsize** : virtual size (compte SegWit).

**4. Naviguer**. En cliquant sur une adresse, on accède à sa page :

- Solde actuel.
- Historique des transactions (entrantes et sortantes).
- Première transaction (date « d’apparition » de l’adresse).
- Dernière activité.

**5. Outils additionnels Mempool** :

- Visualisation graphique de la transaction.
- Mempool actuel et estimation des frais.
- Analyse de blocs.
- API gratuite pour scripts.

**Bonne pratique** : pour chaque transaction d’enquête, **capturer la page** (Hunchly ou équivalent), noter le TXID dans le journal, hasher la capture. Les blockchains sont immutables mais les explorateurs peuvent évoluer (UI, données enrichies).

#### 6.6 Erreurs classiques

**Confondre destinataire et change**. Déjà détaillé. Erreur la plus fréquente.

**Ignorer les frais**. Un input de 1 BTC qui produit des outputs totalisant 0,999 BTC : ce n’est pas un « 0,001 BTC perdu », c’est les frais.

**Confondre montant brut et montant net**. Si vous regardez `bc1qsource1` qui a un input de 0,4 BTC dans une transaction, ce 0,4 BTC est le **UTXO consommé**, pas nécessairement « le montant envoyé par cette adresse ». Le montant net envoyé dépend des outputs.

**Mal interpréter une consolidation**. Un wallet peut **consolider** : prendre 50 petits UTXO et les regrouper en un seul gros UTXO (output unique vers une adresse contrôlée par le même wallet). C’est une opération **interne** au wallet, pas un transfert. Sans heuristique, on peut croire à un envoi de 50 sources vers un destinataire.

**Confondre adresse et personne**. Rappel : une adresse peut être contrôlée par plusieurs personnes (multisig), une personne contrôle souvent des dizaines d’adresses, un service exchange agrège des milliers d’utilisateurs derrière quelques hot wallets.

**Ignorer les fuseaux horaires**. Les timestamps sont en UTC. Si vous documentez « la transaction de 9h12 », précisez « 09:12 UTC, soit 10:12 heure de Paris ». Sinon confusion garantie quand vous corroborez avec des logs internes (bancaires, applicatifs).

**Sur-attribuer trop tôt**. Voir un cluster de 50 adresses ne dit pas qui les contrôle. Documenter le cluster = OK. Conclure « ces adresses appartiennent à X » = pas OK sans preuve externe.

#### 6.7 Fil rouge — MIXSHADOW : la transaction de paiement

> **🔗 MIXSHADOW — Épisode 3 : lecture du paiement**
> 
> Sarah ouvre mempool.space et entre le TXID fourni par Aurélien Médical : `[TXID fictif 64 chars]`.
> 
> Page transaction :
> 
> - **Block height** : 873 245.
> - **Timestamp** : 2026-03-14 09:12:34 UTC.
> - **Confirmations** : 156 (bien finalisée).
> 
> **Inputs** : 4 inputs depuis 4 adresses contrôlées par Aurélien Médical (wallet d’urgence approvisionné en interne pour le paiement). Total inputs : 35,002 BTC.
> 
> **Outputs** : 1 seul output. 35,000 BTC vers `bc1q[adresse Akira fictive]`. Pas de change — Aurélien Médical avait approvisionné exactement 35,002 BTC, le 0,002 BTC va aux frais.
> 
> Sarah note l’adresse Akira comme **point de départ** de l’enquête. Elle clique sur cette adresse pour voir son historique :
> 
> - **Première transaction** : 2026-03-14 09:12 — exactement le paiement Aurélien Médical. Adresse **fraîche**.
> - **Solde actuel** : 35,000 BTC (inchangé pour l’instant).
> - **Aucune autre transaction** avant ou après. Adresse à usage unique pour ce paiement.
> 
> **Hypothèse initiale** (non confirmée) : Akira utilise probablement des **adresses uniques par victime** (pratique courante en RaaS pour cloisonner et faciliter la comptabilité interne). Cette adresse est dédiée Aurélien Médical.
> 
> Sarah capture la page Mempool.space (Hunchly), exporte le détail de la transaction en CSV, hashe le tout, et alimente le journal MIXSHADOW. Premier nœud du graphe documenté.
> 
> Question naturelle suivante : **où vont aller ces 35 BTC ?** L’adresse n’a encore rien envoyé au moment de la lecture initiale (14 mars). Sarah configure une **alerte de monitoring** sur Chainalysis et TRM Labs : elle sera notifiée dès que cette adresse fait une transaction sortante. En attendant, elle continue son cadrage et son setup.
> 
> Ch.7 va détailler le modèle UTXO en profondeur — utile car les 35 BTC vont, dans les jours qui suivent, transiter à travers de multiples transactions, et leur lecture exigera la maîtrise complète du modèle.

-----

### Chapitre 7 — Le modèle UTXO en profondeur

Comprendre le modèle UTXO sans erreur est la condition pour ne pas se perdre dans les flux Bitcoin. Ce chapitre dépasse les bases du Ch.6 pour aborder les patterns avancés : peeling chains, consolidation, splits, et les heuristiques fines.

#### 7.1 La logique UTXO

Reprenons. Dans le modèle UTXO :

- Une « adresse » n’a pas de solde stocké comme variable. Son solde est **calculé** à la volée comme la somme des UTXO non dépensés qui lui sont assignés.
- Une transaction **consomme** des UTXO existants (les inputs) et **crée** de nouveaux UTXO (les outputs).
- Un UTXO est soit **non-dépensé** (UTXO actif, partie du « set UTXO ») soit **dépensé** (consommé par une transaction ultérieure).

**Implications pour l’enquête** :

L’historique d’une adresse est un **graphe** : les transactions qui ont créé des UTXO vers cette adresse, les transactions qui ont consommé ces UTXO. Pour chaque UTXO assigné à l’adresse, on peut dire « il a été créé par TX1 et consommé par TX2 ».

L’analyste qui veut comprendre **« d’où viennent les BTC actuellement à l’adresse X »** suit, pour chaque UTXO non-dépensé, la transaction qui l’a créé, puis remonte à ses inputs, etc. C’est ce qu’on appelle **« remonter la chaîne UTXO »**.

#### 7.2 Le peeling chain — le pattern de blanchiment classique

Un **peeling chain** est un pattern où une grosse somme initiale est **progressivement épluchée** : chaque transaction laisse un petit montant à un destinataire et le reste continue vers une nouvelle adresse contrôlée par la même entité.

**Exemple** :

- **TX1** : 100 BTC en input. Outputs : 1 BTC vers exchange A, 99 BTC vers nouvelle adresse W1 (interne).
- **TX2** (depuis W1) : 99 BTC en input. Outputs : 1 BTC vers exchange B, 98 BTC vers nouvelle adresse W2 (interne).
- **TX3** (depuis W2) : 98 BTC en input. Outputs : 0,5 BTC vers exchange C, 97,5 BTC vers W3.
- … et ainsi de suite, sur des dizaines de transactions.

**Pourquoi faire ça ?** Plusieurs raisons :

- **Petits dépôts plus discrets** : un dépôt de 1 BTC sur un exchange déclenche moins d’alerte qu’un dépôt de 100 BTC.
- **Multiple exchanges** : diversifier les off-ramps pour ne pas être bloqué par une seule plateforme.
- **Brouiller l’analyse linéaire** : chaque pas est une nouvelle adresse, l’enquêteur doit suivre.
- **Time delay** : étaler dans le temps réduit la probabilité d’alerte coordonnée.

**Identification d’un peeling chain** :

- **Pattern** : à chaque transaction, un petit output « spent » (vers une adresse externe, souvent un exchange) et un gros output « change » (vers une nouvelle adresse interne).
- **Adresse change toujours fraîche**.
- **Continuité** : les adresses change forment une chaîne — chacune ne reçoit qu’une fois (de la transaction précédente) et envoie une fois (vers la suivante).
- **Montants décroissants** progressivement.

**Reconstitution de la chaîne** : avec les outils, suivre la chaîne de change adresses jusqu’à son extinction. Les outils professionnels visualisent automatiquement les peeling chains.

**Cas réels** : nombreux cas de blanchiment ransomware utilisent peeling chains. Cas Bitfinex (Ch.41) en est emblématique avec des chaînes étalées sur des années.

#### 7.3 La consolidation

Inverse du peeling : la **consolidation** regroupe plusieurs UTXO en un seul.

**Exemple** :

- 50 UTXO existent à 50 adresses différentes (toutes contrôlées par la même entité — souvent un wallet ou un exchange).
- Une transaction prend les 50 UTXO en inputs et les consolide en 1 ou 2 gros UTXO en output.

**Pourquoi consolider ?** :

- **Réduire les frais futurs** : consommer un seul gros UTXO coûte moins qu’en consommer 50 petits.
- **Préparer un gros transfert** : avant un envoi de 100 BTC, il faut avoir des UTXO totalisant au moins 100 BTC.
- **Maintenance de wallet** : exchange qui consolide les dépôts utilisateurs vers ses cold storage.

**Pour l’analyste** :

- La consolidation est un **signal fort de clustering** : les 50 inputs co-dépensés sont probablement contrôlés par la même entité (heuristique multi-input).
- Elle peut révéler le **wallet sous-jacent** : reconnaître les patterns de consolidation d’un exchange (ex : Coinbase consolide selon une cadence et des seuils particuliers).
- Différencier **consolidation interne** (exchange agrégeant les fonds utilisateurs) **vs consolidation utilisateur final** : implications différentes pour l’enquête.

#### 7.4 Les splits

Un **split** dispatche un UTXO vers de multiples destinataires en une seule transaction.

**Exemple** :

- Input : 100 BTC.
- Outputs : 5 BTC × 20 destinataires différents.

**Cas légitimes** :

- Paiements de salaires d’une entreprise crypto.
- Distribution de token holders.
- Airdrops.

**Cas illicites** :

- **Distribution post-hack** : après un vol, attaquant disperse vers plusieurs wallets pour brouiller.
- **Flow de blanchiment** : envoi vers plusieurs comptes d’exchanges pour off-ramp diversifié.
- **Mixer output** : sortie de mixer custodial vers plusieurs adresses.

**Lecture** : un split avec des montants similaires et destinataires sans pattern commun évident = signal à investiguer. Suivre **chaque destinataire** pour cartographier la dispersion.

#### 7.5 Heuristiques avancées de clustering

Au-delà du co-spend (Ch.6), plusieurs heuristiques affinent le clustering Bitcoin.

**Heuristique de l’adresse change moderne**. Avec SegWit et Taproot, les wallets utilisent généralement le **même type d’adresse** pour le change que pour les inputs. Si une transaction a inputs en P2WPKH (SegWit native, `bc1q...`) et un output en P2WPKH (probable change) + un output en P2PKH (`1...`, probable destinataire), l’output P2WPKH est très probablement le change.

**Heuristique du montant exact**. Si un montant en output correspond exactement à un montant communément requis pour un service (ex : 0,5 BTC pour un dépôt minimum exchange), c’est un signal pour le destinataire. Le change a un montant « calculé » non-rond.

**Heuristique des adresses jamais réutilisées**. Les wallets modernes (BIP-32 hierarchical deterministic) génèrent une nouvelle adresse pour chaque transaction. Si une adresse n’est utilisée qu’une fois (recevoir une transaction et envoyer immédiatement), c’est cohérent avec un usage HD wallet (potentiellement adresse change ou adresse temporaire).

**Heuristique du timing**. Une transaction qui consomme rapidement après création (en quelques blocs) est cohérente avec un comportement automatisé (script, exchange) ou un peeling. Une consommation après semaines/mois suggère plutôt un wallet personnel.

**Heuristique du comportement « hot wallet »**. Une adresse qui reçoit beaucoup et envoie beaucoup en flux constants, avec des soldes rarement à zéro mais variables, est probablement un **hot wallet** d’un service (exchange, marchand, processeur de paiement).

**Heuristique du « cold storage »**. Une adresse qui reçoit beaucoup, garde longtemps, et envoie rarement (ou jamais) est probablement un **cold storage** (réserve d’un service ou d’un investisseur).

#### 7.6 Limites des heuristiques

**Importance des limites**.

**CoinJoin casse le co-spending**. Wasabi, Samourai (Ch.32) — multi-input non lié à entité unique. Un cluster constitué via co-spending sur des transactions CoinJoin est **faux**. Les outils modernes détectent les CoinJoin et excluent ces transactions du clustering.

**Wallets modernes randomisent**. Certains wallets randomisent volontairement la position du change, le type d’adresse, et même le montant non-rond pour brouiller les heuristiques. Limite l’efficacité.

**Multi-sig**. Adresses multisig sont contrôlées par plusieurs parties. Heuristiques de clustering classique ne s’appliquent pas trivialement.

**Erreurs en cascade**. Une heuristique erronée à une étape pollue tout le cluster qui en découle. Les outils intègrent des **scores de confiance** pour limiter la propagation d’erreurs.

**Adversarial usage**. Un acteur qui connaît les heuristiques peut **délibérément** créer des transactions trompeuses pour brouiller l’analyse (faux co-spending, fausses peeling chains, etc.).

**Conclusion pour l’analyste** : les heuristiques sont **utiles mais probabilistes**. Toujours qualifier la confiance, croiser les sources, et documenter l’incertitude.

#### 7.7 Outils pour analyse UTXO avancée

**Mempool.space** : excellent pour lecture transaction par transaction.

**OXT.me** (OpenX Tools) : outil communautaire orienté Bitcoin avancé. Visualisations de peeling chains, analyses heuristiques. Gratuit.

**KYCP.org** : outil dédié à l’analyse CoinJoin (« Know Your CoinJoin Privacy »). Permet d’évaluer la qualité d’un mélange CoinJoin.

**Breadcrumbs.app** : interface graphique pour exploration de flux. Tier gratuit limité.

**Chainalysis Reactor** : référence professionnelle. Clustering automatique, visualisation, scoring. Voir Ch.20.

**TRM Labs Investigations** : alternative pro. Même type de capacités.

**Scripts custom Python** : pour analyses spécifiques (parsing, statistiques sur des milliers de transactions). Bibliothèques : `python-bitcoinlib`, `electrum-protocol`, ou directement via API d’explorateurs.

#### 7.8 Fil rouge — MIXSHADOW : premier mouvement Akira

> **🔗 MIXSHADOW — Épisode 4 : le premier hop**
> 
> 17 mars 2026, 03:42 UTC. L’alerte Chainalysis se déclenche : l’adresse Akira de réception (35 BTC) vient d’envoyer une transaction.
> 
> Sarah ouvre la transaction. Lecture :
> 
> - Input : 35,000 BTC (les fonds Aurélien Médical).
> - Output 1 : 35,000 BTC vers nouvelle adresse `bc1q[H1]...` (adresse fraîche, jamais utilisée).
> - Frais : 0,00012 BTC.
> 
> **Lecture initiale** : c’est un **simple transfer** vers une autre adresse contrôlée par Akira. Pas de split, pas de partage encore. L’adresse `bc1q[H1]` reçoit l’intégralité.
> 
> Sarah note : ce hop pourrait être :
> 
> - Une consolidation pré-blanchiment (déplacer les fonds vers wallet opérationnel).
> - Une rotation OPSEC (changer d’adresse tous les X jours).
> - Le début d’un peeling chain.
> 
> Elle continue la surveillance. À 04:18 UTC (36 minutes plus tard), `bc1q[H1]` envoie à son tour :
> 
> - Input : 35,000 BTC.
> - Output 1 : 0,500 BTC vers nouvelle adresse externe.
> - Output 2 : 34,500 BTC vers nouvelle adresse `bc1q[H2]` (probable change).
> 
> **C’est un peeling chain**. Sarah identifie le pattern : 0,5 BTC est éplutché vers ce qui sera probablement un dépôt d’exchange ou une étape de blanchiment, et le reste continue vers `bc1q[H2]`.
> 
> Sur les 6 heures suivantes, le pattern se répète :
> 
> - `bc1q[H2]` → 0,3 BTC à externe + 34,2 BTC à `bc1q[H3]`.
> - `bc1q[H3]` → 0,7 BTC à externe + 33,5 BTC à `bc1q[H4]`.
> - `bc1q[H4]` → 0,4 BTC à externe + 33,1 BTC à `bc1q[H5]`.
> - … etc.
> 
> Sarah documente chaque transaction en temps réel. Le journal MIXSHADOW capture chaque hop avec timestamp, montant, adresse externe destinatrice (qui sera analysée séparément).
> 
> Au bout de 24h, Sarah a identifié **18 hops** avec un total de **~7,5 BTC éplutchés** vers des adresses externes (à analyser une par une) et **~27,5 BTC** restant dans le wallet principal en mouvement.
> 
> Hypothèse : **peeling chain classique** post-rançon Akira. Sarah priorisera les premiers outputs externes pour identifier les destinations (exchanges, mixers, etc.) — Ch.13 développera cette priorisation. Pour l’instant, le travail est de **suivre méthodiquement chaque hop**.

-----

### Chapitre 8 — Lire une transaction Ethereum

Ethereum a un modèle radicalement différent de Bitcoin. La lecture demande des réflexes nouveaux. Ce chapitre couvre les transactions Ethereum natives, l’usage du gas, et les pièges classiques.

#### 8.1 Anatomie d’une transaction Ethereum

Une transaction Ethereum a la structure suivante :

```
Transaction Hash: 0xabc123...def
Block: 19 234 567
Timestamp: 2026-03-14 14:23:11 UTC
Status: Success ✓

From: 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb1
To: 0x8e9F23456...A1B2C3
Value: 1.5 ETH

Nonce: 142
Gas Limit: 21 000
Gas Price: 25 gwei
Gas Used: 21 000 (100%)
Transaction Fee: 0.000525 ETH ($1.25 at the time)
```

**Concepts clés** :

**From** : adresse émettrice (signataire). Une seule.

**To** : adresse destinataire. Une seule (peut être un wallet ou un smart contract).

**Value** : montant ETH transféré. Peut être 0 si la transaction appelle un smart contract sans transférer ETH directement.

**Nonce** : numéro séquentiel de la transaction pour cette adresse émettrice. Empêche le rejeu.

**Gas** : « carburant » consommé. `Gas Used` × `Gas Price` = `Transaction Fee`.

**Status** : Success ou Failed. Une transaction Failed paie quand même les frais (gas consommé) mais l’effet voulu n’a pas eu lieu.

**Pas d’UTXO**. Le modèle est **account-based** : chaque adresse a un solde direct stocké dans la blockchain. Une transaction modifie deux soldes (from -= value, to += value) plus les frais.

#### 8.2 Différences avec Bitcoin

**Source unique vs multiple inputs**. Une transaction Ethereum a **un seul émetteur**. Pas de co-spending Bitcoin-style. Heuristique de clustering différente.

**Pas de change**. Pas besoin d’adresse change — la blockchain met à jour directement les soldes.

**Smart contracts comme destinataires**. Le `To` peut être un smart contract qui exécute du code. Cela ouvre des possibilités énormes (DeFi, NFT) et complexifie la lecture.

**Gas variable**. Le coût d’une transaction dépend de sa complexité. Un simple transfer ETH = 21 000 gas. Une interaction smart contract complexe peut consommer 500 000+ gas.

**Tokens omniprésents**. Beaucoup de « valeur » sur Ethereum est dans des tokens (USDT, USDC, etc.) — pas dans ETH. Une transaction qui transfère 100 000 USDT a Value = 0 ETH (parce que la valeur est dans le token, pas dans ETH).

#### 8.3 Lire une transaction Ethereum sur Etherscan

**Etherscan.io** est l’explorateur de référence Ethereum. Walkthrough.

**1. Coller un transaction hash** dans la barre de recherche.

**2. Onglet « Overview »** :

- Status, Block, Timestamp.
- From, To.
- Value (ETH transféré natif).
- Transaction Fee.
- Gas Price.

**3. Onglet « Logs »** :

- **Events émis par les smart contracts** appelés. Crucial pour les transferts de tokens.
- Format : event name, paramètres, topics, data.

**4. Onglet « State »** :

- Modifications d’état (avancé).

**5. Onglet « Comments »** :

- Notes communautaires (rare).

**6. Section « ERC-20 Tokens Transferred »** :

- Si la transaction a déclenché des transferts de tokens, ils sont listés ici.
- Format : `From → To, Amount, Token (Symbol)`.

**7. Section « ERC-721 Tokens Transferred »** :

- Pour les NFT.

**8. Section « Internal Transactions »** :

- **Très important**. Les internal transactions sont les **appels entre smart contracts** déclenchés par la transaction principale. Elles ne sont **pas** des transactions séparées au sens propre, mais des effets internes.
- Format : Type (call, delegatecall, etc.), From, To, Value.

#### 8.4 La piège des internal transactions

**Erreur classique** : regarder l’onglet Overview, voir « Value: 0 ETH », et conclure « pas de transfert de valeur ».

**Réalité** : la transaction peut avoir déclenché :

- Des **transferts de tokens** (USDT, USDC) dans les logs ERC-20.
- Des **internal transactions** transférant ETH entre smart contracts.
- Des **ERC-721 transfers** (NFT).

Sans regarder ces sections, on **rate** la majeure partie de l’activité économique de la transaction.

**Exemple concret** : une transaction d’achat d’NFT typique :

- Value : 0 ETH (l’utilisateur n’envoie pas directement d’ETH au vendeur).
- Mais : ETH transféré via internal transactions du smart contract de marketplace vers le vendeur.
- Et : ERC-721 transféré du vendeur à l’acheteur.
- Et : éventuels frais transférés à la marketplace.

Tout ça sur **une seule transaction** principale. Lire correctement nécessite de regarder logs + internal transactions + token transfers.

#### 8.5 Le nonce et son intérêt

Le **nonce** est un compteur séquentiel par adresse. La première transaction d’une adresse a nonce 0, la deuxième nonce 1, etc.

**Implications enquête** :

**Confirmer l’auteur**. Le nonce séquentiel signifie qu’on peut savoir « combien de transactions cette adresse a déjà fait au moment de cette transaction ». Si une adresse fait sa transaction nonce 1, c’est sa **2ème transaction** de toute son histoire.

**Détecter des transactions fail**. Si une adresse a une transaction nonce N qui Fail, la prochaine transaction sera nonce N+1 (le nonce a été consommé même en cas d’échec). Voir des trous dans la séquence d’une adresse = drapeau d’investigation.

**Reconnaître l’activité d’un wallet**. Une adresse à nonce élevé (1000+) est une adresse **très active** (probable hot wallet de service). Une adresse à nonce 1 est presque vierge.

**Détection anomalie**. Une adresse avec activité importante (gros volumes) mais nonce faible (3-5 transactions) est suspicieuse — pourquoi un wallet récemment créé manipule-t-il déjà des montants significatifs ?

#### 8.6 Les transactions « Failed »

Une transaction Ethereum peut **Fail** (échouer) : par exemple, si le smart contract appelé revert (annule l’opération). Le gas est tout de même consommé.

**Pourquoi voir des transactions Failed est utile** :

**Détection de tentatives de phishing/drainer**. Un drainer mal configuré peut faire fail. La transaction est visible mais sans transfert de valeur.

**Reconnaissance de tests**. Un attaquant peut tester sa logique en envoyant des transactions tests qui fail. Les nonce qui suivent pas un gap sont les vraies tentatives.

**Diagnostic d’erreur logique**. Pour analyser un hack DeFi, voir la séquence des transactions Failed avant Success peut révéler la logique exploit utilisée.

#### 8.7 Erreurs classiques

**Ignorer les ERC-20 transferts**. Voir « Value: 0 ETH » et conclure qu’aucune valeur n’a bougé. Toujours regarder la section ERC-20 Tokens Transferred.

**Ignorer les internal transactions**. Pour les transactions impliquant des smart contracts, le mouvement réel d’ETH se fait souvent en internal.

**Confondre token contract et wallet**. L’adresse `0xdAC17F958D2ee523a2206206994597C13D831ec7` est le **contrat USDT** sur Ethereum. Ce n’est pas un wallet d’utilisateur — c’est l’infrastructure. Une transaction qui « envoie 100 USDT » a comme `To` cette adresse, mais le **destinataire réel** (qui reçoit les 100 USDT) est dans les logs ERC-20.

**Penser que `To = destinataire`**. Pour les interactions smart contract, `To` est le contrat appelé, pas le destinataire final de la valeur.

**Ignorer le contexte des chains**. Un transfer USDT sur Ethereum a une logique. Le même transfer sur BNB Chain a une logique similaire mais pas identique (frais différents, timings différents). L’analyste vérifie toujours **sur quelle chaîne** il regarde.

#### 8.8 Outils Ethereum

**Etherscan.io** : référence absolue.

**Tenderly.co** : pour debugging avancé de transactions complexes (DeFi, exploits).

**Phalcon (BlockSec)** : analyse forensique de transactions complexes, simulation.

**EigenPhi** : analytics MEV (Maximal Extractable Value), arbitrage.

**Dune Analytics** : dashboards SQL personnalisables sur la blockchain.

**Bloxy** : explorer alternatif avec analytics.

**DeBank** : portfolio explorer multi-chain.

**Chainalysis Reactor / TRM Labs** : pour Ethereum aussi (Ch.20).

#### 8.9 Fil rouge — MIXSHADOW : un détour par Ethereum

> **🔗 MIXSHADOW — Épisode 5 : un peeling vers Ethereum**
> 
> Sarah continue de suivre les flux Akira sur Bitcoin. Le 19 mars, elle observe quelque chose de différent : une des adresses externes éplutchées (vers laquelle 0,8 BTC ont été envoyés en sortie de peeling chain, hop 7) est une **adresse exchange** étiquetée par Chainalysis comme « FixedFloat hot wallet ».
> 
> **FixedFloat** est un service de swap crypto **non-KYC**, populaire dans les flux illicites. Il permet de convertir un actif en un autre (BTC → ETH par exemple) sans création de compte ni vérification d’identité, en quelques minutes.
> 
> Sarah pose l’hypothèse : Akira utilise FixedFloat pour convertir partiellement les BTC en ETH, probablement en route vers Tornado Cash ou un autre service Ethereum.
> 
> Sarah suit la suite. Sur la blockchain Ethereum, en croisant les timestamps, elle identifie une transaction Ethereum avec :
> 
> - **Hash** : `0xabc...123`.
> - **Timestamp** : 2026-03-19 11:43 UTC (cohérent avec un swap FixedFloat ~10 minutes après le dépôt BTC).
> - **From** : adresse FixedFloat.
> - **To** : `0xAk1...` (nouvelle adresse, fraîche).
> - **Value** : ~12,5 ETH (cohérent avec swap de 0,8 BTC à taux de marché du moment, moins frais).
> 
> Sarah ouvre cette transaction sur Etherscan :
> 
> - Status : Success.
> - Logs : pas d’événements ERC-20 (transfer ETH natif simple).
> - Internal transactions : aucune.
> 
> Lecture simple : 12,5 ETH transférés de FixedFloat hot wallet vers `0xAk1...`. Cette adresse est désormais dans le périmètre MIXSHADOW.
> 
> Sarah suit `0xAk1...`. Quelques heures plus tard, elle observe une transaction sortante :
> 
> - Value : 0 ETH (suspect au premier abord).
> - To : `0x47CE...` (adresse smart contract).
> - Section logs : ERC-20 Token Transferred — **12 ETH transférés vers Tornado Cash 10 ETH pool**.
> 
> Sarah identifie **deux dépôts Tornado Cash de 5 ETH** + **un dépôt de 2 ETH résiduel**. Akira a utilisé Tornado Cash pour anonymiser une partie des fonds.
> 
> **Implication enquête** : à partir du dépôt Tornado Cash, la **traçabilité directe est cassée** (Ch.31 expliquera Tornado Cash). L’analyse va se déplacer vers l’analyse statistique des sorties Tornado Cash pour tenter d’identifier les retraits correspondants — possible mais probabiliste.
> 
> Sarah documente cette branche du flux. Le graphe MIXSHADOW commence à montrer la complexité réelle : Bitcoin (peeling chain) → FixedFloat (swap) → Ethereum (transfert) → Tornado Cash (anonymisation). Quatre étapes, deux chaînes, plusieurs services. Et c’est juste **une** des branches éplutchées du peeling chain initial.
> 
> Le métier de crypto-forensique se révèle dans ces enchaînements multi-chaînes. Ch.9 va détailler les tokens et smart contracts, qui sont au cœur de l’écosystème Ethereum et des flux illicites.

-----

### Chapitre 9 — Tokens et smart contracts

L’écosystème crypto moderne ne se résume pas aux coins natifs. Une part majoritaire de l’activité économique on-chain passe par des **tokens** — actifs déployés via smart contracts. Comprendre tokens et smart contracts est indispensable pour ne pas rater l’essentiel d’une enquête.

#### 9.1 Les standards de tokens

**ERC-20** (Ethereum). Standard pour tokens **fongibles** (interchangeables, divisibles). USDT, USDC, DAI, des dizaines de milliers d’autres. Spécification simple : `transfer`, `approve`, `transferFrom`, `balanceOf`, `totalSupply`, `allowance`. Chaque token ERC-20 est un smart contract dédié déployé sur Ethereum.

**ERC-721** (Ethereum). Standard pour **NFT** (Non-Fungible Tokens) — tokens uniques non-divisibles. Chaque token a un `tokenId` unique. CryptoPunks, BAYC, des millions d’autres.

**ERC-1155** (Ethereum). Standard hybride permettant tokens fongibles et non-fongibles dans un même contrat. Usage en gaming notamment.

**TRC-20** (TRON). Équivalent ERC-20 sur TRON. USDT-TRON est le plus important économiquement.

**BEP-20** (BNB Chain). Équivalent ERC-20 sur BNB Chain.

**SPL** (Solana Program Library). Standard tokens Solana, structure différente.

**Implications enquête** : un token est un smart contract avec une **adresse propre** sur la blockchain. Cette adresse est l’« infrastructure » du token, pas un wallet utilisateur. Confondre les deux = erreur classique.

#### 9.2 Le contrat USDT sur Ethereum

Cas concret. Le contrat USDT sur Ethereum a comme adresse : `0xdAC17F958D2ee523a2206206994597C13D831ec7`.

Sur Etherscan, cette adresse :

- Est marquée « Contract ».
- A des onglets « Code », « Read Contract », « Write Contract ».
- Affiche son ABI (Application Binary Interface).

**Quand quelqu’un envoie 100 USDT à un destinataire** :

- La transaction a `From: l'expéditeur`.
- `To: 0xdAC17F958D2ee523a2206206994597C13D831ec7` (le contrat USDT).
- `Value: 0 ETH` (parce que le transfert n’est pas en ETH).
- Dans les **logs ERC-20**, on voit l’événement `Transfer(from=expéditeur, to=destinataire, value=100000000)` (USDT a 6 décimales, donc 100 USDT = 100 000 000 unités).

**Ne pas confondre** :

- L’adresse `0xdAC17...` est l’**infrastructure** USDT. Aucun utilisateur final n’a ses USDT « stockés là » au sens propre.
- Les balances utilisateurs sont stockées dans une **mapping interne** du smart contract.
- Le destinataire réel d’un transfert est dans les **logs**, pas dans le `To`.

#### 9.3 Approve et allowance — le mécanisme central

Pour qu’un smart contract (DEX, lending) puisse manipuler vos tokens, vous devez lui donner une **autorisation préalable** via `approve`.

**Mécanisme** :

1. Vous appelez `approve(spender, amount)` sur le contrat token. Cela autorise `spender` à dépenser jusqu’à `amount` de vos tokens.
1. Plus tard, `spender` (souvent un DEX) appelle `transferFrom(from=vous, to=destinataire, amount)` qui transfère vos tokens.

**Cas légitime** : utiliser Uniswap pour échanger USDT contre ETH. Vous approuvez Uniswap pour dépenser X USDT. Uniswap exécute le swap via `transferFrom`.

**Cas malveillant — drainer** : un site de phishing imitant une plateforme légitime vous demande de signer un `approve` pour un montant **illimité** (`type(uint256).max`). Une fois la signature obtenue, le drainer (smart contract du scammer) peut vider tous vos tokens à tout moment via `transferFrom`.

**Implications enquête** :

- Investigation d’un wallet drain : toujours regarder l’historique des **approvals** de la victime. Quel contrat a-t-elle approuvé ? Quand ? Pour quel montant ?
- Reconnaître une transaction de drain : le contrat malveillant appelle `transferFrom` quelques minutes/heures après l’`approve` de la victime, vide les tokens.
- Outils : `revoke.cash` permet à un utilisateur de **révoquer** des approvals existants. Pour l’analyste, l’historique des approvals d’une adresse est une mine d’information.

#### 9.4 Lire les logs ERC-20

Sur Etherscan, l’onglet **Logs** d’une transaction affiche tous les événements émis par les smart contracts appelés.

Format type d’un Transfer ERC-20 :

```
Address: 0xdAC17F958D2ee523a2206206994597C13D831ec7 (USDT)
Name: Transfer (index_topic_1 address from, index_topic_2 address to, uint256 value)
Topics:
  0: 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef (signature de l'event Transfer)
  1: 0x000...0xExpediteur
  2: 0x000...0xDestinataire
Data:
  0x0000...montant en hex
```

**Décodage** :

- `Address` : le contrat émetteur de l’event = le contrat token (ici USDT).
- `from` et `to` : les vraies parties du transfert.
- `value` : montant en plus petite unité du token. Pour USDT (6 décimales), 100000000 = 100 USDT.

Etherscan **décode automatiquement** ces events si l’ABI du contrat est publié, ce qui simplifie la lecture humainement. Mais comprendre le format brut est utile pour parser massivement (scripts) ou analyser des contrats sans ABI publique.

#### 9.5 Smart contracts : risques et opportunités d’enquête

**Smart contract** = code immutable déployé sur la blockchain. Une fois déployé, peut être appelé par n’importe qui (selon les permissions définies).

**Pour l’enquête** :

**Code souvent vérifié et public**. Les développeurs « vérifient » leur contrat sur Etherscan en publiant le code source Solidity. L’analyste peut **lire le code** pour comprendre la logique. Particulièrement utile pour analyser les drainers, exploits, fraudes.

**Code non-vérifié = drapeau rouge**. Un contrat sans code vérifié est plus suspect. L’analyste doit alors lire le **bytecode** (langage machine EVM) ou **désassembler**, beaucoup plus difficile.

**Honeypot tokens**. Token déployé avec code malveillant : la fonction `transfer` est altérée pour empêcher les acheteurs de revendre. L’analyse du code révèle le piège (souvent via condition cachée : seul le créateur peut transferer, blacklist abusive, taxe à 100%, etc.).

**Backdoors et privilèges**. Beaucoup de contrats ont des fonctions « owner-only » (mint, burn, pause, blacklist). L’analyste vérifie qui détient l’ownership et si le contrat est « renoncé » (ownership transférée à 0x0).

**Outils d’analyse smart contract** :

- **Etherscan Read/Write Contract** : interface basique d’inspection.
- **Tenderly** : simulation et debugging avancé.
- **Phalcon (BlockSec)** : forensique de transactions complexes.
- **GoPlus, Token Sniffer** : analyse automatique de tokens (détection de honeypots).
- **DeFiSafety, CertiK** : audits publics.

#### 9.6 Phishing par smart contract

Les attaques par smart contract phishing sont devenues un vecteur majeur 2022-2026.

**Schémas typiques** :

**Faux site DEX**. L’utilisateur croit interagir avec Uniswap, signe un `approve` pour un drainer.

**Faux mint NFT**. Site qui propose de minter un NFT « gratuit » mais demande l’approval de tokens existants.

**Faux airdrop**. Notification d’airdrop, l’utilisateur doit « claim » via signature qui en réalité approuve un drainer.

**Walletconnect malveillant**. Faux dApp connecté qui demande des signatures abusives.

**EIP-712 / signature de message**. Au lieu d’une transaction visible, l’attaquant fait signer un **message off-chain** (EIP-712). La signature est ensuite utilisée on-chain pour drainer. Plus subtil parce que l’utilisateur croit « juste signer un message ».

**Investigation post-drain** :

- Identifier l’adresse drainer (qui a appelé `transferFrom`).
- Tracer où vont les fonds drainés (souvent vers mixer ou bridge).
- Si le drainer est public, analyser le code pour comprendre la mécanique.
- Identifier le **draining service** sous-jacent (services-as-a-service comme Inferno Drainer, Pink Drainer, Angel Drainer en 2023-2024 — multiples variantes ensuite).

#### 9.7 Fil rouge — MIXSHADOW : analyse smart contract Tornado

> **🔗 MIXSHADOW — Épisode 6 : Tornado Cash inspection**
> 
> Sarah continue MIXSHADOW. Elle a identifié plusieurs dépôts Tornado Cash de la branche Ethereum. Avant d’analyser les sorties potentielles (Ch.31), elle veut comprendre **précisément** ce qui s’est passé.
> 
> Elle ouvre la transaction de dépôt Tornado Cash sur Etherscan :
> 
> - Hash : `0xdef...456`.
> - From : `0xAk1...` (adresse de Akira sur Ethereum).
> - To : `0x910Cbv...` (Tornado Cash 10 ETH pool, contrat connu).
> - Value : 10 ETH.
> - Status : Success.
> 
> **Logs** : un événement `Deposit` émis par le contrat Tornado, contenant un **commitment** (hash cryptographique).
> 
> Sarah note : Tornado Cash fonctionne par **pools de montants fixes** (0,1 ETH, 1 ETH, 10 ETH, 100 ETH). Akira a utilisé le pool 10 ETH × 2 + le pool 1 ETH × 2 pour anonymiser les 12 ETH (en pratique, légèrement moins parce que des frais de gaz s’appliquent).
> 
> Le **commitment** est un engagement cryptographique. Pour retirer, l’utilisateur fournira un **proof zero-knowledge** prouvant qu’il connaît le secret correspondant à un commitment dans la pool, sans révéler **lequel**. C’est la magie cryptographique de Tornado Cash.
> 
> Sarah documente :
> 
> - Le **dépôt** est observable on-chain (qui a déposé, quand, combien).
> - Le **retrait correspondant** (somewhere later) sera observable on-chain (qui retire, quand, combien) — mais **non-liable au dépôt** sans information additionnelle.
> - Il existe néanmoins des **techniques d’analyse statistique** pour réduire l’incertitude (timing analysis, montants atypiques, comportement post-retrait). Ch.31 détaillera.
> 
> Sarah ajoute aux indices MIXSHADOW : **timestamp précis du dépôt**, **gas price** payé (signe d’urgence ou non), **nonce** de l’adresse Akira au moment du dépôt (combien d’autres opérations elle a faites avant et après), **adresses adjacentes** dans le bloc (qui d’autre déposait à Tornado Cash dans le même bloc, créant des co-occurrences potentiellement exploitables).
> 
> Cette analyse fine n’est pas du « lire un explorateur ». C’est du **raisonnement crypto-forensique** : comprendre la mécanique du smart contract, identifier les signaux exploitables, documenter ce que les données permettent de faire et ne pas faire.
> 
> Au passage, Sarah note pour l’attribution Akira : **utilisation de Tornado Cash post-sanctions OFAC (août 2022)**. Akira accepte donc d’utiliser un service sanctionné, ce qui contraint les off-ramps possibles (la plupart des exchanges régulés bloquent les fonds tracés à Tornado). Signal sur le profil opérationnel d’Akira.

-----

### Chapitre 10 — Stablecoins : USDT, USDC et le rôle opérationnel

Les **stablecoins** sont devenus la **monnaie de transaction** de pans entiers de l’écosystème crypto. Légitime comme illicite. Ce chapitre approfondit leur fonctionnement, leur dominance dans certains flux illicites, et les opportunités défensives qu’ils offrent (gel d’actifs).

#### 10.1 Qu’est-ce qu’un stablecoin

Un **stablecoin** est un crypto-actif dont la valeur est arrimée à une référence stable, généralement le **dollar US** (1 stablecoin = 1 USD).

**Mécanismes d’arrimage** :

**Adossés à des réserves fiat (« centralized fiat-backed »)** : émis par une entreprise (Tether, Circle, Paxos) qui détient des réserves USD (cash + bons du Trésor + autres) en quantité équivalente aux tokens en circulation. C’est le modèle dominant.

- USDT (Tether) — émetteur Tether Limited.
- USDC (USD Coin) — émetteur Circle.
- BUSD (Binance USD) — émetteur Paxos, en déclin depuis 2023.
- TUSD (TrueUSD), USDP (Pax Dollar), GUSD (Gemini Dollar) — plus petits.

**Adossés à du crypto (« crypto-collateralized »)** : maintien du peg via collatéralisation crypto + mécanismes algorithmiques.

- DAI (MakerDAO) — adossé à un panier d’actifs crypto (ETH, USDC, autres) avec sur-collatéralisation.

**Algorithmiques** : sans collatéral réel, pegging par algorithme. Modèle qui a connu des effondrements catastrophiques.

- UST (TerraUSD) — effondré en mai 2022, perte ~40 Mrd USD pour les investisseurs. Modèle discrédité.

#### 10.2 Pourquoi les stablecoins dominent les flux

**Stabilité de valeur**. Pour un criminel comme pour un usager légitime, la **volatilité** de Bitcoin/Ethereum est un problème. Recevoir 35 BTC à 9h et les convertir 6h plus tard peut signifier une perte de 5-10% (ou un gain — symétrique). Les stablecoins éliminent ce risque pour les opérations de trésorerie.

**Liquidité globale**. USDT et USDC sont disponibles sur la quasi-totalité des exchanges, DEX, plateformes DeFi. Conversion en/depuis n’importe quel autre actif crypto en quelques secondes.

**Multi-chaînes**. USDT existe sur Ethereum, TRON, BNB Chain, Solana, Polygon, Avalanche, Arbitrum, Optimism, et des dizaines d’autres. Permet l’arbitrage entre chaînes selon coûts et disponibilités.

**Rapidité et coût**. Sur TRON, un transfer USDT coûte ~1 centime et confirme en 3 secondes. Sur Ethereum, plus cher (5-30 USD) mais flexible.

**Inclusion bancaire informelle**. Dans des pays à banking dysfonctionnel (Argentine, Liban, Nigeria, Venezuela, Zimbabwe), USDT sert de **dollar de remplacement** accessible.

**Pour l’écosystème criminel**, les stablecoins offrent :

- Pas de volatilité pendant le blanchiment.
- Rapidité de transfert.
- Multi-chaînes pour cross-chain laundering.
- Volume liquide pour fondre les flux dans le bruit légitime.

Selon les rapports Chainalysis 2024-2025, **les stablecoins représentent une part dominante des volumes de transactions on-chain** et une fraction significative et croissante des **flux illicites identifiables**. TRON est devenu particulièrement central pour USDT illicite.

#### 10.3 USDT vs USDC — différences pour l’enquête

**USDT (Tether)** :

- Émetteur : **Tether Limited**, opaque historiquement, basée hors juridictions strictes.
- **Dominant** en volume (~110 Mrd USD en circulation 2025).
- Coopération avec autorités : **variable**. Tether gèle des adresses sur réquisition mais pas systématiquement, et avec délais variables. Plus rapide depuis 2023.
- Disponible sur **toutes les chaînes principales**.

**USDC (Circle)** :

- Émetteur : **Circle**, US-based, régulé.
- ~30 Mrd USD en circulation 2025.
- Coopération avec autorités : **forte et rapide**. Circle gèle les adresses listées par OFAC quasi-immédiatement. Bien intégré aux processus US.
- Disponible sur multiples chaînes mais moins que USDT.

**Pour l’analyste** :

- Voir des fonds illicites passer par **USDC** est moins fréquent que par USDT (les criminels savent que Circle gèle vite).
- **USDT-TRON** est aujourd’hui le pipeline majeur des flux illicites stablecoin (frais bas + Tether moins réactif + multi-juridictionnel).
- **USDT-Ethereum** reste utilisé, surtout pour interactions DeFi.
- Identifier dès qu’un fonds passe en USDC = potentiel **angle de gel** rapide.

#### 10.4 Le gel d’actifs

Les stablecoins centralisés (USDT, USDC, autres) ont une **fonction blacklist** dans leur smart contract. L’émetteur peut **geler** une adresse — les tokens à cette adresse deviennent intransférables, même si l’utilisateur a la clé privée.

**Mécanisme technique** :

- Dans le contrat USDT, fonction `addBlackList(address)` (réservée à l’owner).
- Une fois une adresse blacklistée, ses tokens ne peuvent plus être transférés.
- L’émetteur peut aussi `destroyBlackFunds(address)` — détruire les tokens de l’adresse blacklistée (équivalent à les retirer de la circulation).

**Cas d’usage pour les autorités** :

- Réquisition adressée à Tether ou Circle pour geler une adresse identifiée comme criminelle.
- En coopération étroite, le délai entre demande et gel peut être de quelques heures (USDC, Circle bien préparé).
- Pour USDT, le délai est plus variable (heures à jours selon la procédure et la juridiction demandeuse).

**Cas réels** :

- Tether a gelé des centaines de millions USDT cumulés depuis 2017, en réponse à demandes OFAC, FBI, autorités étrangères.
- Circle a gelé Tornado Cash addresses immédiatement après la sanction OFAC d’août 2022.
- En cas de hack majeur (ex : Ronin, Wormhole), les fonds qui transitent par stablecoins sont parfois gelés à la requête des victimes.

**Pour l’enquêteur** : identifier dès qu’un flux transite par un stablecoin gel-able = **opportunité de coordination**. Remontée rapide à l’émetteur via les autorités peut figer des fonds avant cashout.

#### 10.5 USDT-TRON vs USDT-Ethereum

**Erreur classique** : penser que « USDT est USDT » indépendamment de la chaîne. **Faux**.

- **USDT-Ethereum** : un token ERC-20 sur Ethereum, contrat `0xdAC17...`.
- **USDT-TRON** : un token TRC-20 sur TRON, contrat `TR7N...`.
- **Ce sont DEUX tokens distincts**, juste émis par le même émetteur (Tether) avec le même peg USD.

**Conséquences** :

**Un USDT-Ethereum NE PEUT PAS être directement transféré à une adresse TRON**. Il faut un **bridge** ou un **swap cross-chain** (passage par exchange ou service de bridging).

**Les soldes sont distincts**. Une adresse Ethereum peut avoir 1000 USDT, et l’« même utilisateur » sur TRON peut avoir 500 USDT — c’est deux balances séparées.

**Les frais sont radicalement différents**. Transfer USDT-TRON ~1 centime. Transfer USDT-Ethereum 5-30 USD selon congestion. Cette différence explique pourquoi les flux à haute fréquence (pig butchering, certains blanchiments) privilégient TRON.

**L’enquêteur** vérifie toujours **sur quelle chaîne** il regarde. Mentions « USDT » sans préciser la chaîne sont ambiguës et doivent être clarifiées.

#### 10.6 Patterns de blanchiment via stablecoins

**Pattern 1 — Conversion BTC → USDT**. Après un paiement BTC (rançon, paiement darknet), conversion rapide en USDT pour stabiliser la valeur, soit via exchange centralisé, soit via swap (FixedFloat, ChangeNOW, etc.).

**Pattern 2 — Bridge cross-chain via USDT**. USDT-Ethereum → USDT-TRON via bridge ou exchange. Réduit la traçabilité et change le coût opérationnel.

**Pattern 3 — Layering USDT-TRON**. Multiple transferts entre adresses TRON contrôlées, peeling chain-style, avec frais minimes. Alimente la dispersion.

**Pattern 4 — Off-ramp via P2P**. Conversion USDT → fiat via plateformes P2P (Binance P2P, LocalCryptos, etc.) ou OTC desks. Permet de quitter la blockchain en monnaie locale.

**Pattern 5 — Obfuscation pré-cashout**. Avant cashout final, mélange via DEX ou usage de protocoles DeFi pour ajouter du bruit.

#### 10.7 Investigation TRON spécifique

**Tronscan.org** : explorateur principal TRON.

**Lecture de transaction USDT-TRON** :

- Page transaction TRON, similaire à Etherscan.
- Section « TRC-20 Tokens Transferred » montre les transferts USDT (et autres TRC-20).
- Adresse contrat USDT-TRON : `TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t`.

**Heuristiques TRON** :

- Beaucoup de wallets utilisateurs (vs services), donc moins d’agrégation que Bitcoin.
- Pattern pig butchering reconnaissable : adresses recevant de **multiples victimes**, consolidant rapidement, et déposant sur exchange.
- Vérifier les **labels Tronscan** (limités vs Etherscan), enrichir avec Chainalysis ou TRM.

**Limites** :

- Outils forensiques moins matures que pour Bitcoin/Ethereum.
- Documentation communautaire moins riche.
- Cooperation Tron Foundation variable.

#### 10.8 Fil rouge — MIXSHADOW : transit par stablecoins

> **🔗 MIXSHADOW — Épisode 7 : conversion partielle vers USDT**
> 
> Sarah continue le suivi des branches éplutchées du peeling chain Akira. L’une des branches (~3 BTC envoyés à un exchange non-KYC en hop 12) ressort, 4 heures plus tard, sous forme d’**USDT-TRON**.
> 
> Sequence :
> 
> - 3 BTC déposés sur exchange non-KYC X (identifié par Chainalysis comme « Exchange à risque, pas de KYC, juridiction grise »).
> - Conversion BTC → USDT-TRON sur l’exchange (interne, pas observable on-chain).
> - Retrait : ~290 000 USDT-TRON envoyés depuis l’adresse retrait de l’exchange vers `TR[Akira-TRON]...` (nouvelle adresse Akira sur TRON).
> 
> Sur Tronscan, Sarah observe :
> 
> - Adresse `TR[Akira-TRON]` reçoit 290 000 USDT.
> - Quelques heures plus tard, dispersion : 6 transferts vers 6 nouvelles adresses TRON, montants variables (40-60k USDT chacun).
> - Chaque sub-adresse refait à son tour des transferts (peeling-style adapté à TRON).
> 
> **Hypothèse Sarah** : Akira utilise USDT-TRON comme **monnaie d’opération** pour la phase de blanchiment finale. Les frais bas permettent un layering étendu. Les destinations finales seront probablement :
> 
> - Off-ramp via P2P / OTC dans des juridictions grises (Russie, Asie centrale).
> - Cashout via cartes prepaid crypto.
> - Certains flux peuvent revenir vers fiat via exchanges régionaux moins regardants.
> 
> Sarah note : **opportunité de coordination Tether**. Bien que Tether soit moins réactif que Circle, dans le cadre d’une coordination DGSI/TRACFIN avec FBI/OFAC, une demande de gel sur les principales adresses Akira identifiées peut être tentée. Elle prépare la liste des **6 adresses TRON principales** + **2 adresses Ethereum** pour transmission.
> 
> Le rapport intermédiaire MIXSHADOW (à 4 semaines de mission) inclura cette demande de coordination Tether.
> 
> Au passage, Sarah documente les **patterns Akira** observés : peeling Bitcoin → swap partiel via FixedFloat → Tornado Cash sur Ethereum → conversion vers USDT-TRON via exchange non-KYC → dispersion TRON. C’est un pattern qu’elle pourrait reconnaître chez d’autres victimes Akira pour corroboration. Elle alerte d’autres investigateurs Athéna et la DGSI : si d’autres victimes Akira nécessitent investigation, ce template de blanchiment est potentiellement réutilisé.

-----

### Chapitre 11 — Explorateurs blockchain : méthodologie de lecture

L’analyste qui passe ses journées dans des explorateurs doit en maîtriser la lecture. Ce chapitre couvre les principaux explorateurs, leurs spécificités, et la méthodologie pour les utiliser efficacement.

#### 11.1 Les explorateurs Bitcoin

**Mempool.space** :

- Open source, moderne, performant.
- Excellente UX pour navigation transaction/adresse/bloc.
- Visualisations mempool en temps réel.
- API gratuite généreuse.
- Communauté active.
- **Recommandé** pour usage quotidien et vérification.

**Blockstream.info (Esplora)** :

- Blockstream, open source aussi.
- Solide, classique.
- Bon pour intégration via API.

**Blockchain.com Explorer** :

- Historique, large utilisation.
- Interface vieillissante.
- Toujours fonctionnel.

**BTC.com Explorer** :

- Géré par Bitmain.
- Statistiques mining riches.

**OXT.me** :

- Spécialisé analyses Bitcoin avancées.
- Excellent pour peeling chains et clusters.

**Blockchair.com** :

- Multi-chain (BTC, ETH, autres).
- Recherche cross-chain pratique.

**Pour l’analyste** : Mempool.space en premier choix, OXT pour analyses avancées, autres en validation croisée.

#### 11.2 Les explorateurs Ethereum

**Etherscan.io** :

- **Référence absolue**.
- UX éprouvée.
- Décodage automatique des smart contracts vérifiés.
- Labels riches (exchanges, contracts, sanctions OFAC).
- API gratuite (avec limites) + tier payant.
- Indispensable.

**Beaconcha.in** :

- Couvre la beacon chain (consensus) Ethereum post-Merge.
- Utile pour analyser staking, validators.

**Phalcon.xyz (BlockSec)** :

- Analyse forensique avancée.
- Excellent pour transactions complexes (DeFi, exploits).
- Visualisation des appels internes.

**Tenderly.co** :

- Plateforme dev, mais utile pour analyse.
- Simulation de transactions, debugging.

**Bloxy.info** :

- Analytics et reporting.
- Recherche avancée.

#### 11.3 Les autres explorateurs

**Tronscan.org** : référence TRON. Couvre transactions, USDT-TRON, smart contracts TRON.

**Solscan.io** : référence Solana. Tokens SPL, NFT Solana.

**BscScan.com** : BNB Chain. Clone d’Etherscan (même équipe).

**PolygonScan.com** : Polygon. Clone Etherscan.

**Arbiscan.io, Optimistic.etherscan.io, Basescan.org** : Layer-2 Ethereum. Clones Etherscan.

**Snowtrace.io** : Avalanche.

**FtmScan.com** : Fantom.

**Multiversx Explorer (anciennement Elrond)** : MultiversX.

**Cosmos / Mintscan.io** : Cosmos écosystème.

**XRPSCAN, Bithomp** : XRP Ledger.

**Pour l’analyste polyvalent** : maîtriser au minimum Etherscan + Tronscan + Mempool. Étendre selon les chaînes rencontrées dans les enquêtes.

#### 11.4 Méthodologie de lecture

**Phase 1 — Validation initiale**.

- Vérifier que le TXID/adresse existe bien (mauvaise saisie, typo, mauvaise chaîne).
- Vérifier la chaîne — beaucoup d’erreurs viennent de chercher un transaction ETH sur Etherscan alors qu’elle est sur BNB Chain.
- Status : Success ou Failed.
- Confirmations suffisantes (transaction finalisée).

**Phase 2 — Lecture structurée**.

- Header (block, timestamp).
- From / To.
- Value (native).
- Logs / Events (token transfers, autres).
- Internal transactions.
- Fee.

**Phase 3 — Documentation**.

- Capture de la page (Hunchly).
- Notation dans le journal d’enquête.
- Hash de la capture.
- Lien vers l’explorateur (stable, vérifiable plus tard).

**Phase 4 — Enrichissement**.

- Vérifier les labels associés (exchange, mixer, sanction).
- Pour les contrats, vérifier le code source si vérifié.
- Pour les adresses, regarder l’historique complet.

**Phase 5 — Croisement multi-explorateurs** (selon enjeu) :

- Pour les cas critiques, vérifier la même transaction sur 2 explorateurs indépendants.
- Confirme l’absence de bug d’affichage.
- Capture les enrichissements différents (labels, etc.).

#### 11.5 Citer une page d’explorateur correctement

**Format de citation** :

- URL complète et stable.
- TXID ou adresse complète (pas tronquée).
- Date et heure de consultation (UTC).
- Hash de la capture (SHA-256).
- Pour pages dynamiques (qui peuvent évoluer), capture HTML + screenshot.

**Exemple journal** :

```
2026-03-19 14:23 UTC
Consulté Mempool.space pour TXID e3a5f9a8... 
URL: https://mempool.space/tx/e3a5f9a8c1b2d4e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0
Capture: tx_e3a5f9a8_20260319.html, hash SHA-256: abc123...
Observation: Transaction confirmée, 35 BTC transférés depuis 4 inputs Aurélien Médical vers bc1q[Akira]
Document de référence: MIXSHADOW_journal.md ligne 42
```

**Pourquoi ce niveau de rigueur ?** Les blockchains sont immutables, mais les explorateurs peuvent évoluer (UI change, labels updated, données enrichies). Une capture précise garantit reproductibilité d’analyse 6 mois ou 5 ans plus tard, voire devant juge.

#### 11.6 Limites des explorateurs publics

**Manque de clustering**. Les explorateurs publics affichent transactions et adresses individuellement. Pour voir le cluster d’une adresse, il faut un outil professionnel (Chainalysis Reactor, TRM Labs).

**Labels limités**. Etherscan a beaucoup de labels mais pas tous. Tronscan en a moins. Les outils pro ont des bases label propriétaires bien plus riches.

**Pas de visualisation graphe**. Les explorateurs sont transactionnels, pas graphiques. Pour visualiser des flux complexes (peeling chains, dispersions), outil dédié (Maltego, Gephi, Chainalysis Reactor).

**Pas de scoring de risque**. Les explorateurs n’évaluent pas le risque d’une adresse. Outils pro le font.

**Performance sur grosses adresses**. Une adresse avec 100 000 transactions sera lente à charger. Outils pro paginent et indexent mieux.

**Conclusion** : explorateurs publics = base nécessaire et gratuite pour vérification. Outils pro = amplification de capacité pour investigations sérieuses. Combiner les deux. Voir Ch.19 (gratuits) et Ch.20 (pro).

#### 11.7 Fil rouge — MIXSHADOW : navigation multi-explorateurs

> **🔗 MIXSHADOW — Épisode 8 : routine quotidienne**
> 
> Le travail de Sarah devient routine. Chaque jour, elle :
> 
> 1. Vérifie sur Mempool.space les nouveaux mouvements depuis les adresses Akira identifiées.
> 1. Cross-check sur Etherscan pour les flux Ethereum.
> 1. Tronscan pour les flux TRON.
> 1. Chainalysis Reactor pour la vue cluster et alertes.
> 1. TRM Labs en validation parallèle.
> 
> Au bout de 3 semaines :
> 
> - **62 adresses Bitcoin** identifiées dans les peeling chains et leurs branches.
> - **18 adresses Ethereum** identifiées dans la branche Tornado Cash et post-retraits.
> - **47 adresses TRON** identifiées dans les flux USDT.
> - **12 adresses dans 4 exchanges différents** (FixedFloat, ChangeNOW, exchange non-KYC X, autre exchange non-KYC Y).
> 
> Sarah maintient un **graphe maître** dans Chainalysis Reactor + un **journal Markdown détaillé** pour chaque mouvement. Pour chaque adresse, une **fiche d’adresse** (Ch.12) est constituée.
> 
> Elle remarque : **certaines adresses TRON** (3 d’entre elles) ont un comportement « hub » — elles reçoivent de multiples sources et redistribuent. Hypothèse : ces adresses pourraient appartenir à un **service de blanchiment** (mixer manuel, OTC desk) qu’Akira utilise comme intermédiaire, plutôt qu’à Akira directement.
> 
> Cette nuance est importante : si ces hubs sont des **services**, l’attribution ne peut pas remonter directement à Akira via ces hubs. Mais identifier le **service utilisé** par Akira est en soi une **valeur de renseignement** : d’autres groupes ransomware utilisent peut-être le même service, et le service lui-même peut être ciblé par les autorités.
> 
> Sarah documente cette hypothèse comme « probable » (confiance ~70%), avec actions de vérification : continuer à surveiller, vérifier si d’autres clusters ransomware connus ont historiquement utilisé ces hubs, croiser avec bases TRM/Chainalysis (dont les labels propriétaires sont plus riches que les labels Etherscan/Tronscan).
> 
> La méthodologie d’enquête (Partie III) va structurer cette analyse — comment passer de l’observation brute (« je vois des hops, des adresses, des flux ») à la production de renseignement (« voici la topologie du réseau de blanchiment Akira, avec niveaux de confiance et angles d’action »).

-----

## PARTIE III — MÉTHODOLOGIE D’ENQUÊTE

> **Ce que cette partie apprend.** Structurer l’enquête crypto comme une démarche méthodologique, pas comme une exploration intuitive. Construire des fiches d’adresses opérationnelles, démarrer une enquête depuis n’importe quel indice, raisonner de l’indice au graphe, visualiser les flux de manière lisible, gérer la temporalité, comprendre les promesses et limites du clustering, calibrer l’attribution.
> 
> **Ce qu’elle ne couvre pas.** Les outils précis (Partie IV), les typologies d’abus (Partie V), les techniques d’obfuscation (Partie VI).
> 
> **Ce que vous saurez faire après cette partie.** Conduire une enquête crypto structurée et reproductible, depuis un indice initial jusqu’à une analyse calibrée, avec graphes lisibles, hypothèses formulées proprement, et niveaux de confiance documentés.

-----

### Chapitre 12 — Construire une fiche d’adresse

La **fiche d’adresse** est l’unité documentaire de base de l’enquête crypto. Pour chaque adresse pertinente, l’analyste constitue une fiche structurée qui synthétise tout ce qu’il sait. Les fiches s’agrègent en graphe d’enquête. Sans fiche, l’enquête se dilue dans le flou.

#### 12.1 Pourquoi la fiche d’adresse

Trois fonctions :

**Mémoire**. L’enquête sur 50 adresses, sur 8 semaines, ne peut pas tenir « dans la tête ». La fiche externalise la mémoire et permet de retrouver instantanément ce qu’on sait sur une adresse spécifique.

**Communication**. Quand Sarah doit briefer la DGSI ou son directeur Athéna sur l’enquête, les fiches d’adresses sont son support. Synthèse précise, vérifiable.

**Calibration**. Tenir une fiche oblige à expliciter ce qu’on sait, ce qu’on suppose, et ce qu’on ne sait pas. Discipline anti-confusion entre observation et inférence.

#### 12.2 Le template fiche d’adresse

Modèle complet à adapter selon l’enquête. À retrouver en Annexe B.

```markdown
# Fiche adresse — [Identifiant abrégé]

## Identification
- **Adresse complète** : [adresse exacte 42-56 caractères]
- **Blockchain** : [Bitcoin / Ethereum / TRON / Solana / etc.]
- **Type d'adresse** : [P2PKH / P2SH / SegWit / Taproot / EOA / Contract / autre]
- **Identifiant interne enquête** : [Akira-BTC-007 par exemple]

## Activité observable
- **Première transaction** : [date UTC, TXID]
- **Dernière transaction** : [date UTC, TXID]
- **Nombre total de transactions** : [N]
- **Solde actuel** : [montant et actif]
- **Actifs reçus historiques** : [montants par actif]
- **Actifs envoyés historiques** : [montants par actif]

## Contreparties
- **Adresses contreparties principales** : [top 5-10 par volume]
- **Services labellisés impliqués** : [exchanges, mixers, bridges identifiés]
- **Cluster Chainalysis (ou TRM)** : [ID cluster + nb adresses + label si applicable]

## Labels publics
- **Labels Etherscan / Tronscan / Mempool** : [liste]
- **Labels propriétaires Chainalysis / TRM** : [si accès]
- **Sanctions OFAC** : [oui/non + détail si oui]
- **Mentions OSINT** : [forums, presse, twitter, etc.]

## Hypothèses
- **Hypothèse principale** : [ex : « adresse de réception ransomware Akira »]
- **Niveau de confiance** : [WEP : très probable / probable / possible / spéculatif]
- **Hypothèses alternatives** : [autres explications possibles, à noter]
- **Éléments de preuve** : [observations supportant l'hypothèse principale]
- **Éléments d'incertitude** : [observations qui pourraient contredire ou nuancer]

## Captures et sources
- **Captures de pages d'explorateur** : [liens vers fichiers archivés + hashes]
- **Sources externes** : [URL forums, presse, etc.]
- **Cross-check effectués** : [outils utilisés, dates]

## Statut enquête
- **Date de création de la fiche** : YYYY-MM-DD
- **Dernière mise à jour** : YYYY-MM-DD
- **Statut** : [Active / Surveillance / Clôturée]
- **Investigateur** : [nom]
- **Liens vers fiches connexes** : [autres adresses du graphe]
```

#### 12.3 Renseigner la fiche : ordre méthodologique

**Étape 1 — Identification**. Saisie immédiate dès qu’une adresse entre dans le périmètre d’enquête. Vérifier la blockchain (erreur classique : adresse Ethereum rentrée comme adresse Bitcoin).

**Étape 2 — Activité observable**. Lecture sur explorateur principal (Mempool, Etherscan, Tronscan). Captures systématiques. Hash de chaque capture.

**Étape 3 — Contreparties**. Lister les adresses qui ont reçu/envoyé. Pour les top contreparties (par volume), noter et identifier si elles sont dans le périmètre d’enquête ou nouvelles.

**Étape 4 — Labels**. Vérifier sur explorateurs publics. Si accès aux outils pro, croiser. Sanctions OFAC : vérifier sur SDN list.

**Étape 5 — OSINT externe**. Recherche sur l’adresse dans Google, Twitter, forums (parfois des adresses sont publiquement associées à des services ou acteurs). Recherche sur DeHashed/IntelX au cas où l’adresse apparaît dans des leaks. Cf. cours **Dark Web** et **OSINT Mastery** pour méthodes.

**Étape 6 — Hypothèses**. Formuler explicitement. Calibrer la confiance.

**Étape 7 — Documentation**. Toutes les sources, captures, dates.

#### 12.4 Le piège de la fiche prématurée

Une fiche peut **figer prématurément** une hypothèse. Tentation : nommer l’adresse « Akira-Hot-Wallet-3 » alors qu’on ne sait pas encore que c’est un hot wallet d’Akira.

**Bonne pratique** :

- Identifiant interne **neutre** au début (« BTC-Investigation-007 ») jusqu’à preuve d’attribution suffisante.
- Hypothèse principale **calibrée** : « possible adresse de blanchiment Akira (confiance 50%) » plutôt que « adresse Akira ».
- **Mises à jour** quand de nouvelles infos arrivent. La fiche évolue.

#### 12.5 Maintien de la fiche dans le temps

Une fiche n’est pas un document one-shot. Elle évolue.

**Mises à jour quotidiennes** pour adresses actives en surveillance.

**Vérification hebdomadaire** pour adresses moins actives.

**Reprise complète** lors de tournants d’enquête (nouvel angle, validation/invalidation d’hypothèse).

**Versioning** : noter les versions successives, dater chaque mise à jour. Outils Git ou systèmes de fichiers avec horodatage suffisent.

#### 12.6 Fiches et graphe

Les fiches s’articulent en **graphe** :

- Chaque fiche = un **nœud**.
- Les contreparties identifiées = **arêtes** vers d’autres fiches.
- Les patterns (peeling chain, consolidation) sont représentés par séquences d’arêtes.

Outils de visualisation (Ch.21) consomment ce graphe pour produire des vues exploitables.

-----

### Chapitre 13 — Point de départ d’une enquête : typologie d’indices

L’enquête crypto démarre toujours par un **indice initial**. Sa nature détermine les premières actions et oriente l’enquête. Ce chapitre cartographie les types d’indices et la méthode pour les exploiter.

#### 13.1 Adresse fournie par une victime

**Cas typique** : pig butchering. La victime communique l’adresse à laquelle elle a envoyé ses fonds.

**Étapes** :

1. **Vérifier la blockchain**. La victime peut se tromper — elle dit « Bitcoin » alors qu’elle a envoyé USDT-TRON. Demander captures de transaction.
1. **Récupérer le TXID** si possible. Avec le TXID, on a une preuve plus solide que juste l’adresse.
1. **Lire la transaction sur explorateur**. Montant, timestamp, adresse de destination.
1. **Constituer fiche** sur l’adresse de destination.
1. **Suivre les flux sortants**. La destination redistribue probablement vers d’autres adresses.

#### 13.2 Transaction hash (TXID)

**Cas typique** : alerte SOC sur transaction suspecte, victime de hack ayant capté la transaction de drain.

**Étapes** :

1. Identifier la blockchain (parfois implicite, parfois à vérifier).
1. Lire la transaction complète.
1. Identifier les parties (from, to, montants).
1. Étendre l’enquête depuis ces parties.

#### 13.3 Capture d’écran

**Cas typique** : victime envoie capture de la confirmation reçue d’un wallet, screenshot Telegram, photo de QR code.

**Étapes** :

1. **Extraire l’adresse ou TXID** lisiblement de la capture (parfois OCR utile).
1. **Vérifier l’authenticité** : la capture peut être falsifiée. Recouper avec on-chain (l’adresse a-t-elle bien reçu cette transaction à ce timestamp ?).
1. Procéder ensuite comme avec adresse/TXID.

**Piège** : QR code dans la capture. Le décoder (outils en ligne, smartphone). Vérifier qu’il pointe bien vers l’adresse mentionnée.

#### 13.4 Lien de paiement / payment URI

**Format BIP-21 Bitcoin** : `bitcoin:bc1q...?amount=0.5&label=Donation`.

**Format Ethereum** : `ethereum:0x...?value=1000000000000000000`.

**Étapes** :

1. Décoder l’URI.
1. Vérifier l’adresse extraite.
1. Procéder comme avec adresse classique.

#### 13.5 Email de rançon

**Cas typique** : ransomware, sextortion, fausses menaces.

**Contenu type** : adresse Bitcoin/Monero pour paiement, montant demandé, deadline, instructions.

**Étapes** :

1. **Extraire l’adresse**.
1. Vérifier sur blockchain : a-t-elle été utilisée pour d’autres demandes de rançon (fiche enrichie de l’écosystème ransomware) ? A-t-elle reçu des paiements ?
1. **Croiser** avec bases publiques (databases ransomware tracking, AnyRun, autres).
1. Si sextortion classique de masse, l’adresse peut apparaître dans des centaines/milliers d’emails — pattern de fraude reconnaissable.
1. Si ransomware ciblé, adresse souvent fraîche, dédiée à la victime.

#### 13.6 Message Telegram / canal

**Cas typique** : opérateurs ransomware via canaux Telegram, scammers via groupes Telegram, vendeurs de données.

**Étapes** :

1. **Documenter le contexte** : nom du canal, date du message, contenu.
1. Extraire les adresses crypto mentionnées.
1. Suivre méthodologie standard.
1. **Croiser** avec d’autres mentions du canal/acteur.

**Important** : pas de contact direct avec le canal sans cadre clair. Observation passive uniquement pour OSINT.

#### 13.7 Wallet trouvé dans un malware

**Cas typique** : analyse de malware ransomware / clipper / stealer qui contient une adresse hardcodée.

**Étapes** :

1. Reverse engineering du malware (compétence cyber, voir cours **Forensique** ou **APT**).
1. Extraction de l’adresse hardcodée ou des adresses générées dynamiquement.
1. Procéder comme avec adresse classique.
1. **Croiser** avec autres souches du malware : la même famille ransomware utilise-t-elle les mêmes patterns ?

#### 13.8 Adresse sur forum dark web

**Cas typique** : enquête sur un acteur dark web qui partage son adresse pour réception de paiements (vente de données, services).

**Étapes** :

1. **Documenter le contexte** : forum, post, date, vendeur, contenu vendu/proposé.
1. Extraire l’adresse.
1. Suivre méthodologie standard.
1. **Croiser** avec activités du vendeur (autres forums, autres pseudonymes).

Cf. cours **Dark Web** pour la méthodologie d’enquête sur les forums clandestins.

#### 13.9 Adresse dans note de ransomware

Voir Ch.13.5.

#### 13.10 Indice indirect : nom d’un acteur, alias, organisation

**Cas typique** : on demande à Sarah « investigue Lazarus » sans adresse de départ.

**Étapes** :

1. **Recherche dans bases publiques d’adresses associées**. OFAC SDN list (qui inclut désormais des adresses crypto). Reports Chainalysis, TRM, Elliptic publiquement disponibles.
1. **Recherche sur Twitter / X** : ZachXBT et autres chercheurs publient régulièrement des adresses associées à des hacks/acteurs.
1. **Recherche dans IndexedLeaks et bases CTI** : des wallets connus sont publiés.
1. **Avec point de départ obtenu**, suivre méthodologie standard.

Cas Lazarus : OFAC a sanctionné de multiples wallets liés. Plusieurs hacks majeurs (Ronin, Atomic Wallet, multiple exchanges) ont des adresses publiques documentées par Chainalysis et FBI.

#### 13.11 Priorisation des indices

Quand l’analyste a **plusieurs indices** au démarrage (ce qui est commun dans les gros incidents), il priorise.

**Critères** :

**Solidité**. Un TXID est plus solide qu’une capture d’écran (qui peut être falsifiée). Une adresse confirmée par on-chain analysis est plus solide qu’une mention forum.

**Fraîcheur**. Une adresse active dernière 24h offre plus d’angles (suivre les flux en temps réel) qu’une adresse inactive depuis 2 ans.

**Centralité**. L’adresse principale d’un acteur (hot wallet ransomware) est plus critique qu’une adresse périphérique.

**Coopérabilité**. Une adresse qui transite vers un exchange régulé permet potentiellement réquisition. Une adresse 100% interne au réseau criminel sans interaction externe est plus opaque.

**Effort vs valeur**. Investir 20h sur une adresse Monero qui ne donnera rien vs 5h sur une adresse Bitcoin avec angles multiples → choix évident.

#### 13.12 Fil rouge — MIXSHADOW : priorisation des branches

> **🔗 MIXSHADOW — Épisode 9 : choix d’angles**
> 
> Au bout de 3 semaines, Sarah a identifié 62 adresses Bitcoin, 18 Ethereum, 47 TRON. Trop pour tout suivre en profondeur. Elle priorise.
> 
> **Branche prioritaire 1** : peeling chain principale Bitcoin. 27,5 BTC restent en circulation, mouvement continu. Suivi quotidien justifié.
> 
> **Branche prioritaire 2** : flux USDT-TRON. 290 000 USDT en dispersion. Plusieurs hubs identifiés. Coordination Tether possible.
> 
> **Branche secondaire 3** : Tornado Cash Ethereum. Les 12 ETH sont déposés. Analyse statistique des sorties à mener mais probabiliste — moins de certitude sur attribution mais utile pour profiler Akira.
> 
> **Branche tertiaire 4** : adresses externes du peeling chain non encore caractérisées. Chacune représente un dépôt de quelques BTC dans un service ou wallet. Plusieurs sont déjà identifiées comme exchanges non-KYC. Quelques-unes sont des inconnues à investiguer.
> 
> Sarah alloue son temps : 60% sur prioritaires 1+2, 20% sur Tornado, 20% sur les autres branches.
> 
> Elle demande aussi à un junior d’Athéna de prendre en charge la **fiche d’écosystème** Akira (ce qui n’est pas dans le périmètre crypto strict mais alimente l’attribution) : profil du groupe, historique des victimes connues, TTP, leak site Akira, infrastructure.

-----

### Chapitre 14 — De l’indice au graphe : chaîne de raisonnement

Une fois l’indice initial exploité, l’enquête entre dans sa **phase exploratoire**. Construire le graphe de l’écosystème de l’acteur. Ce chapitre couvre la chaîne de raisonnement de l’analyste pour passer méthodiquement de l’indice au graphe documenté.

#### 14.1 La distinction critique : observation, inférence, attribution

Trois niveaux à ne jamais confondre.

**Observation** : ce qu’on **voit** directement sur la blockchain. « L’adresse A a envoyé 10 BTC à l’adresse B le [date] ». Vérifiable, factuel.

**Inférence** : ce qu’on **déduit** des observations via raisonnement et heuristiques. « L’adresse B est probablement contrôlée par la même entité que A (heuristique de change) ». Probabiliste, justifiable.

**Attribution** : ce qu’on **affirme** sur l’identité ou la nature de l’entité. « Le cluster A-B est un wallet du groupe ransomware Akira ». Nécessite des **éléments externes** (recoupements OSINT, labels propriétaires, données KYC obtenues légalement).

**L’analyste sérieux** :

- Distingue ces niveaux dans son journal et ses rapports.
- Ne **promeut** pas une inférence en attribution sans preuve additionnelle.
- Calibre la confiance à chaque niveau.

#### 14.2 La chaîne de raisonnement type

**Étape 1 — Identifier l’actif et la chaîne** (observation immédiate).

L’indice est sur quelle blockchain ? Quel actif ? Vérifications de base avant tout autre travail.

**Étape 2 — Vérifier l’existence de la transaction / activité de l’adresse** (observation).

L’indice n’est pas une fabrication. La transaction existe bien, l’adresse a bien l’historique attendu.

**Étape 3 — Lire la transaction / activité initiale en détail** (observation).

Toutes les composantes (inputs, outputs, value, logs, internal). Pas de raccourci.

**Étape 4 — Identifier les contreparties** (observation).

Qui sont les autres adresses dans la transaction. Lister sans interpréter encore.

**Étape 5 — Catégoriser les contreparties** (inférence).

Pour chaque contrepartie : est-ce un service connu (label) ? Une nouvelle adresse fraîche ? Une adresse à activité passée ? Catégorie initiale : exchange / mixer / bridge / wallet personnel inconnu / etc.

**Étape 6 — Suivre les flux pertinents** (observation + inférence).

Pour chaque contrepartie pertinente, lire ses transactions sortantes. Reconstituer le **chemin des fonds** post-réception.

**Étape 7 — Identifier les patterns** (inférence).

Peeling chain ? Consolidation ? Split ? Dépôt exchange ? Bridge ? Mixer ? Caractériser le type d’opération.

**Étape 8 — Formuler hypothèses** (inférence calibrée).

À partir des patterns, proposer des hypothèses sur la nature de l’activité (« blanchiment post-rançon », « collecte de victimes », « préparation cashout »).

**Étape 9 — Croiser avec sources externes** (recoupement).

Recherche OSINT sur les adresses, labels propriétaires, mentions publiques, base CTI Athéna interne.

**Étape 10 — Mettre à jour les fiches et le graphe** (documentation).

Synthétiser dans les fiches d’adresses + graphe global.

**Étape 11 — Itérer** (cycle).

Chaque nouvelle adresse identifiée comme pertinente devient indice de Étape 1. Le graphe s’étend.

#### 14.3 Le piège de l’expansion sans bornes

**Erreur classique** : suivre **toutes** les adresses, à toutes les profondeurs. Le graphe explose. Au bout de 5 hops, on a des dizaines de milliers d’adresses, dont 99% sans rapport avec l’enquête initiale.

**Stratégie de bornage** :

**Profondeur limitée**. Ne pas dépasser 5-7 hops typiquement, sauf cas spécifique. Au-delà, le signal se perd dans le bruit.

**Filtrage par pertinence**. Ne suivre les adresses dont les flux sont significatifs (gros montants, patterns suspects). Ignorer les flux poussiéreux (dust).

**Stop conditions**. Arrêter sur :

- Dépôt exchange identifié → angle de coopération autorité, suivi terminé pour cette branche.
- Mixer / privacy coin → rupture de visibilité, documenter et passer.
- Adresse dormante (pas de mouvement depuis longtemps) → pas de progrès attendu.
- Cluster déjà attribué → information acquise.

**Priorisation continue**. Réévaluer hebdomadairement quelles branches méritent encore l’effort.

#### 14.4 Distinguer un service d’un wallet utilisateur

Erreur fréquente : confondre une adresse de **service** (exchange, processeur de paiement, mixer) avec une adresse de **wallet utilisateur**.

**Signaux qu’une adresse est un service** :

**Volume très élevé**. Service principal d’exchange peut traiter des milliers de transactions par jour. Wallet utilisateur typique a quelques transactions par mois.

**Multi-counterparties**. Service interagit avec des centaines/milliers d’adresses différentes. Wallet utilisateur a un nombre limité de contreparties.

**Patterns automatisés**. Service consolide/dispatche selon patterns programmés (chaque 6h, chaque seuil atteint, etc.). Wallet utilisateur a des patterns plus erratiques.

**Solde stable ou cyclique**. Service maintient solde dans une fourchette opérationnelle. Wallet utilisateur peut avoir solde très variable.

**Labellisation**. Service souvent labellisé par les outils. Wallet rarement.

**Erreur si confusion** : analyser un service comme s’il était un acteur permet de l’attribuer à tort à l’acteur enquêté. Toutes les transactions d’un exchange ne sont pas des transactions de l’enquêteur — c’est l’**utilisateur final** dans le service qui compte.

#### 14.5 Le raisonnement face à l’incertitude

Beaucoup d’observations sont **ambiguës**. L’analyste doit calibrer.

**Exemple typique** : adresse A envoie à adresse B 0,5 BTC. Adresse B est nouvelle, jamais vue.

Hypothèses possibles :

- B est une adresse de change de A (continuation interne).
- B est un wallet personnel de la même entité, géré séparément.
- B est un destinataire externe (paiement à un autre acteur).
- B est un dépôt exchange (bientôt vidé vers hot wallet de l’exchange).

Sans information additionnelle, **on ne peut pas trancher**. On documente toutes les hypothèses, on attend l’évolution (B fait quoi ensuite ?), on enrichit avec labels.

**Discipline** : ne pas trancher prématurément. Garder les hypothèses ouvertes. Ne refermer que quand des éléments solides arrivent.

#### 14.6 Calibration WEP en pratique

L’analyste utilise un vocabulaire calibré (Words of Estimative Probability).

**Échelle type** (voir Annexe F pour matrice complète) :

|WEP              |Probabilité|Usage                                                               |
|-----------------|-----------|--------------------------------------------------------------------|
|Quasi-certain    |>95%       |Preuve directe, multiple corroboration. Rare dans l’OSINT pur.      |
|Très probable    |80-95%     |Multiple convergence, peu d’alternatives plausibles                 |
|Probable         |60-80%     |Convergence majoritaire, alternatives possibles mais moins probables|
|Possible         |40-60%     |Hypothèse parmi d’autres, pas dominante                             |
|Peu probable     |15-40%     |Possible mais des alternatives plus plausibles                      |
|Très peu probable|<15%       |Hypothèse marginale                                                 |
|Indéterminable   |N/A        |Données insuffisantes pour évaluer                                  |

**Bonne pratique** : utiliser **systématiquement** un WEP à chaque hypothèse formulée. Et expliciter ce qui pourrait faire évoluer le WEP (« si on apprend X, le WEP passerait à Y »).

#### 14.7 Le journal d’enquête

Le **journal d’enquête** est la trace écrite quotidienne de la chaîne de raisonnement.

**Format type (Markdown)** :

```markdown
# Journal MIXSHADOW

## 2026-03-19

### 14:23 UTC — Suivi adresse Akira-BTC-007
- Observation : adresse a fait nouvelle transaction sortante.
- TXID : [hash]
- Lecture : peeling pattern continue, 0,4 BTC à external + 32,7 BTC à change.
- External destination : adresse fraîche, jamais vue.
- Action : créer fiche Akira-BTC-008 (external) et Akira-BTC-Change-008 (change).

### 14:45 UTC — Hypothèse sur Akira-BTC-008
- Pas encore d'activité sortante.
- Hypothèse : possible dépôt exchange (probable, 60%).
- Alternative : wallet personnel intermédiaire (possible, 30%).
- Alternative : OTC desk (possible, 20%).
- Surveillance : alerte Chainalysis activée pour mouvements futurs.

### 16:12 UTC — Réflexion sur progression globale
- 5 branches actives en parallèle.
- Branche peeling principale : 18 hops, 7,5 BTC dispersés, 27,5 BTC en circulation.
- Branche Ethereum/Tornado : 12 ETH déposés, sorties non analysées encore.
- Branche TRON/USDT : 290k USDT en dispersion.
- Décision : prioriser TRON + Bitcoin pour cette semaine. Tornado attend.
```

Ce journal **n’est pas le rapport final**. C’est la matière brute qui alimentera le rapport, mais aussi la **trace** pour reproduire/contester l’analyse plus tard.

-----

### Chapitre 15 — Construire un graphe de flux lisible

Le **graphe de flux** est la représentation visuelle de l’enquête. Bien construit, il rend l’enquête lisible en une page. Mal construit, il devient un **plat de spaghetti** illisible. Ce chapitre couvre la méthodologie de visualisation.

#### 15.1 Pourquoi visualiser

**Comprendre soi-même**. La représentation visuelle révèle des patterns invisibles dans le tableau. Un peeling chain devient évident en graphe, opaque en liste.

**Communiquer**. Un rapport avec graphe est lu et compris ; un rapport texte-only est plus difficile à digérer pour décideurs.

**Coopérer**. Quand Sarah brieffe la DGSI, un graphe permet à l’auditoire d’absorber la topologie en quelques minutes.

**Soutenir la mémoire**. Une fois l’enquête archivée, le graphe permet de reconstituer rapidement l’analyse 6 mois plus tard.

#### 15.2 Anatomie d’un graphe de flux

**Nœuds** : adresses crypto.

**Arêtes** : transactions (montant, direction, timestamp, actif).

**Attributs des nœuds** :

- Type d’entité présumée (wallet utilisateur / service / contrat / mixer / etc.).
- Solde actuel.
- Volume cumulé (entrées + sorties).
- Niveau de confiance d’attribution.

**Attributs des arêtes** :

- Direction (qui envoie à qui).
- Montant.
- Actif (BTC, ETH, USDT, etc.).
- Timestamp.
- TXID référence.

**Annotations contextuelles** :

- Légende (couleurs, formes).
- Période couverte.
- Source des données.

#### 15.3 Codes visuels recommandés

**Couleur par type d’entité** :

- **Vert** : adresse cible / contrôlée par enquêté (acteur principal de l’enquête).
- **Rouge** : adresse à risque (sanctioned, mixer, etc.).
- **Bleu** : exchange / VASP régulé.
- **Orange** : exchange non-KYC ou à risque.
- **Gris** : adresse non encore caractérisée.
- **Jaune** : smart contract / DeFi.

**Forme par fonction** :

- **Cercle** : wallet (EOA Ethereum, adresse Bitcoin classique).
- **Carré** : smart contract.
- **Hexagone** : service (exchange, bridge).
- **Triangle** : adresse sanctionnée.

**Épaisseur d’arête** : proportionnelle au montant (logarithmique pour grosse plage de valeurs).

**Style d’arête** :

- Plein : transaction confirmée.
- Pointillé : flux inféré (pas observable directement, ex : sortie de mixer présumée).

#### 15.4 Niveaux d’abstraction

Un même graphe peut être visualisé à différents niveaux.

**Niveau 1 — Adresses brutes**. Chaque adresse = un nœud. Trop dense pour une enquête à 100+ adresses. Utile pour analyse fine d’une zone.

**Niveau 2 — Clusters**. Les adresses du même cluster (heuristiques) sont fusionnées en un seul nœud. Donne le « squelette » de l’écosystème. Vue plus lisible pour acteurs majeurs.

**Niveau 3 — Entités**. Les adresses identifiées comme un même service (exchange, mixer) sont fusionnées en une entité. Donne la vue **business** : « Akira → exchange non-KYC X → Tornado Cash → exchange régulé Y ».

**Niveau 4 — Phases**. Synthèse en phases d’opération : « Réception → Layering → Cashout ». Vue ultime pour rapport exécutif.

L’analyste produit **plusieurs vues** selon l’audience :

- SOC / IR : niveau 1 et 2 (détail technique).
- CISO / direction : niveau 3 et 4 (stratégique).
- Autorités : niveau 2 et 3 (opérationnel).

#### 15.5 Outils de visualisation

**Chainalysis Reactor** : visualisation native intégrée à l’outil de clustering. Excellente pour enquêtes utilisant Chainalysis. Limites : exports parfois rigides, dépendance plateforme.

**TRM Labs Investigations** : équivalent. Bon graphique intégré.

**Maltego** : référence transverse OSINT. Connecteurs blockchain via plugins (Maltego CTAS, Maltego Crypto). Très flexible, courbe d’apprentissage modérée. Excellent pour graphes multi-sources (crypto + OSINT classique + autres).

**Gephi** : open source, puissant pour grands graphes. Plus orienté analyse statistique réseau (centralité, communautés). Courbe d’apprentissage forte.

**Graphistry** : visualisation GPU pour très grands graphes (>100k nœuds). Cloud ou self-hosted. Cas avancés.

**Obsidian** : pour graphes simples avec annotations textuelles. Léger, rapide. Limité en taille.

**Mermaid (Markdown)** : pour graphes simples intégrables dans rapports Markdown. Limites visuelles fortes mais portable.

**Drawio / Excalidraw** : pour graphes manuels simples. Bons pour documents finaux. Peu adapté pour gros graphes.

**Cytoscape** : alternative à Gephi, JavaScript-based, customisable.

#### 15.6 Quand ne PAS visualiser

**Trop peu de données**. Si l’enquête a 5 adresses et 3 transactions, un tableau suffit. Visualisation overkill.

**Trop de données sans abstraction**. 10 000 adresses sans cluster = spaghetti. Soit on abstractit (clusters, entités), soit on segmente (zoom sur une partie).

**Pour le draft d’analyse**. La visualisation soigneusement formattée prend du temps. Ne la produire qu’aux livraisons importantes (rapport intermédiaire, rapport final, briefing). En cours d’enquête, journal Markdown + tableau excel suffit.

#### 15.7 Le graphe minimal pour rapport

Pour rapport exécutif (audience non-technique), un **graphe minimal** :

- 5-15 nœuds maximum.
- Niveau 3 (entités) ou Niveau 4 (phases).
- Couleurs claires, légende explicite.
- Annotations textuelles pour les éléments clés (« Étape 3 : conversion BTC → USDT-TRON via exchange non-KYC X »).
- Pas plus de 10-15 arêtes.

Si l’enquête a 100+ adresses, le rapport contient le **graphe minimal** dans le corps, et le **graphe détaillé** en annexe technique.

#### 15.8 Fil rouge — MIXSHADOW : graphe à 4 semaines

> **🔗 MIXSHADOW — Épisode 10 : visualisation d’étape**
> 
> Sarah prépare un graphe pour le briefing intermédiaire DGSI à 4 semaines de mission. Il doit synthétiser ce qu’elle a compris jusque-là.
> 
> **Niveau 3 (entités)**, 12 nœuds principaux :
> 
> - Aurélien Médical (vert).
> - Akira receive address (rouge, central).
> - Akira BTC operational wallet (rouge, peeling chain principale).
> - FixedFloat (orange, exchange non-KYC).
> - Akira ETH wallet (rouge).
> - Tornado Cash 10 ETH pool (gris, mixer).
> - Tornado Cash 1 ETH pool (gris, mixer).
> - Exchange non-KYC X (orange).
> - Akira TRON wallet 1 (rouge).
> - Hub TRON 1 (orange, suspect service de blanchiment).
> - Hub TRON 2 (orange, suspect service de blanchiment).
> - Multiple destinations TRON (gris, à investiguer).
> 
> Arêtes annotées avec montants et timing.
> 
> Légende explicite. Phase indiquées sur le graphe : (1) réception, (2) peeling Bitcoin, (3) conversion ETH/Tornado, (4) conversion TRON/dispersion.
> 
> Le graphe tient sur une page. Le briefing à la DGSI utilise ce graphe + 5 slides additionnelles (contexte, observations clés, hypothèses, limites, prochaines étapes). Durée totale : 30 minutes + 30 min Q&A.
> 
> Retour DGSI : le graphe permet une lecture immédiate. Validation pour pousser la coordination Tether sur les adresses TRON principales. Validation aussi pour transmettre les 4 adresses des principaux exchanges non-KYC à Europol/FBI pour évaluation de coopération internationale.
> 
> Sarah note : sans ce graphe, l’enquête « 4 semaines, 130 adresses » serait incommunicable.

-----

### Chapitre 16 — Temporalité et chronologie d’enquête

La dimension **temporelle** est centrale en enquête crypto. Les transactions sont horodatées avec précision, et leur **séquence** porte de l’information. Mal traiter la temporalité = manquer des patterns clés.

#### 16.1 Les timestamps blockchain

Toute transaction blockchain a un **timestamp précis**, en **UTC**. Précision :

- Bitcoin : timestamp du bloc, ~10 minutes de granularité.
- Ethereum : timestamp du bloc, ~12 secondes de granularité (post-Merge).
- TRON, Solana : seconde près.

**Important** : le timestamp est celui d’**inclusion dans un bloc**, pas de **broadcast**. Une transaction émise à 14:23:00 peut être incluse dans un bloc à 14:25:30. Pour les analyses fines, cette différence importe.

**Mempool** : sur Bitcoin notamment, les transactions « attendent » dans le mempool avant inclusion. Si congestion, elles peuvent attendre plusieurs heures. L’analyste sophistiqué regarde aussi les **logs mempool** (si disponibles) pour saisir le moment exact d’émission.

#### 16.2 Patterns temporels remarquables

**Activité par fuseau horaire**. Les acteurs actifs uniquement entre 9h et 18h dans une fenêtre cohérente avec un fuseau (Moscou, Pyongyang, etc.) trahissent leur localisation probable. Adresses gérées par humains ont des patterns horaires ; bots ont des patterns non-humains.

**Jours fériés / chômés**. Inactivité pendant jours fériés russes (1-8 janvier, 8 mars, 1-9 mai), chinois (Nouvel An lunaire), iraniens (Nowruz), nord-coréens (Chuseok, Day of the Foundation), etc. — signal sur la juridiction d’opération.

**Cohérence horaire avec autres événements**. Un paiement crypto à H+0 d’une demande de rançon, un transfert post-hack à H+5 minutes, un dépôt exchange juste après hop d’obfuscation = patterns cohérents avec acteur unique pilotant l’opération.

**Bursts d’activité**. Soudaine multiplication de transactions sur 1-2h = signal de **dispersion en urgence** (peur d’alerte) ou **automatisation** (bot consolidant).

**Inactivité longue avec activité subite**. Wallet dormant pendant des mois qui se réveille = signal fort. Soit l’attaquant change de tactique, soit un nouveau cycle d’opération démarre.

#### 16.3 Délais entre événements

**Délai paiement-rançon → premier mouvement**. Mesure le **temps de réaction** de l’opérateur. Quelques minutes = automatisation. Quelques heures = supervision humaine. Plusieurs jours = peut-être pas le vrai propriétaire (revente, intermédiaire).

**Délai dépôt exchange → retrait en autre actif**. Mesure le **temps de blanchiment**. Conversion BTC → USDT en 5 minutes = pattern automatisé. En 24h = manuel.

**Délai entre branches d’un peeling chain**. Trop régulier (toutes les heures pile) = bot. Variable et erratique = humain.

#### 16.4 Construire une timeline d’enquête

Pour rapports, une **timeline** synthétise les événements clés en ordre chronologique.

**Format type** (Annexe D pour template) :

```markdown
## Timeline MIXSHADOW

| Date UTC | Événement | Adresse | Montant | Source |
|---|---|---|---|---|
| 2026-03-08 03:47 | Compromission initiale Aurélien Médical | - | - | Forensics Mandiant |
| 2026-03-08 04:30 | Démarrage chiffrement Akira | - | - | Logs internes |
| 2026-03-12 11:00 | Demande rançon initiale 80 BTC | bc1q[Akira-receive] | 80 BTC | Note ransomware |
| 2026-03-13 16:30 | Négociation : 35 BTC accepté | - | - | Comm. cellule crise |
| 2026-03-14 09:12 | Paiement Aurélien Médical | bc1q[Akira-receive] | 35 BTC | Mempool TXID [...] |
| 2026-03-14 15:28 | Réception clé déchiffrement | - | - | Comm. portail Akira |
| 2026-03-17 03:42 | Premier mouvement sortant Akira | bc1q[H1] | 35 BTC | Mempool TXID [...] |
| 2026-03-17 04:18 | Début peeling chain | bc1q[H2] | 0,5 + 34,5 BTC | Mempool TXID [...] |
| ... | ... | ... | ... | ... |
| 2026-03-19 11:43 | Conversion BTC → ETH via FixedFloat | 0xFixedFloat → 0xAk1 | 12,5 ETH | Etherscan TXID [...] |
| 2026-03-19 12:55 | Dépôts Tornado Cash (3 dépôts) | 0xAk1 → Tornado | 12 ETH | Etherscan TXIDs [...] |
| 2026-03-22 08:30 | Conversion via exchange non-KYC X | bc1q[H12] → exchange | 3 BTC | Mempool + monitoring |
| 2026-03-22 12:30 | Retrait USDT-TRON | exchange → TR[Akira-TRON] | 290 000 USDT | Tronscan TXID [...] |
| ... | ... | ... | ... | ... |
```

La timeline est **synthétique** (pas exhaustive — elle synthétise le journal complet). Elle est **enrichie de sources** (TXID, références internes). Elle est **chronologique stricte**.

#### 16.5 Corrélation avec événements off-chain

L’enquête crypto **gagne** quand on corrèle avec des événements off-chain.

**Avec logs internes victime**. Le timestamp d’une transaction crypto peut être corrélé avec :

- Logs SIEM (compromission initiale, activité suspecte).
- Logs réseau (exfiltration de données précédant le ransomware).
- Logs téléphone/email du RSSI (notifications, négociations).

**Avec comms négociation**. Les portails de négociation Tor utilisés par les opérateurs ransomware ont leurs propres timelines (messages, deadlines, ultimatums). Croiser avec timeline crypto.

**Avec leak site**. La publication sur le leak site Akira d’Aurélien Médical (s’il y en a eu) a un timing à corréler. Avant paiement, après paiement, etc.

**Avec presse / médias**. Les annonces publiques de rançonnage / paiement / récupération forment une trame externe.

**Avec d’autres victimes**. Si Akira a frappé 5 victimes la même semaine, leurs timelines comparées peuvent révéler **patterns opérationnels** du groupe (séquencement d’attaques, ressource humaine consacrée, etc.).

#### 16.6 Fuseaux horaires : la rigueur

**Toujours en UTC dans les rapports techniques**. Évite ambiguïté. Les blockchains sont en UTC.

**Conversion explicite si nécessaire**. « 09:12 UTC, soit 10:12 heure de Paris (UTC+1, hiver) ». Évite confusion lecteur.

**Ne jamais faire de raisonnement sans timezone**. « La transaction a eu lieu à 9h12 » est insuffisant. **9h12 où ?**

**Cohérence dans tout le rapport**. Si le rapport mélange UTC pour blockchain et heure locale pour comms, expliciter au début et marquer chaque mention.

#### 16.7 Fil rouge — MIXSHADOW : insight temporel

> **🔗 MIXSHADOW — Épisode 11 : pattern horaire Akira**
> 
> Sarah analyse les **patterns temporels** des opérations Akira observées dans MIXSHADOW.
> 
> **Activité par heure UTC** (sur les 30+ transactions Akira analysées) :
> 
> - 0h-4h UTC : 35% de l’activité.
> - 4h-8h UTC : 8%.
> - 8h-12h UTC : 12%.
> - 12h-16h UTC : 5%.
> - 16h-20h UTC : 15%.
> - 20h-24h UTC : 25%.
> 
> **Décodage** : pic d’activité en deux fenêtres : 0h-4h UTC et 20h-24h UTC. Si on convertit :
> 
> - 0h-4h UTC = 3h-7h MSK (Moscou), ou 9h-13h KST (Séoul/Pyongyang).
> - 20h-24h UTC = 23h-3h MSK, ou 5h-9h KST.
> 
> Le pattern est **plus cohérent avec un fuseau Asie de l’Est** (KST, Pyongyang ou Séoul) qu’avec MSK. Heure de travail KST = pic d’activité crypto.
> 
> Mais Sarah reste prudente : c’est un **signal**, pas une preuve. Hypothèses alternatives :
> 
> - Acteur en Russie qui travaille de nuit (par choix ou contrainte).
> - Acteur dans une autre TZ qui imite délibérément patterns asiatiques.
> - Plusieurs membres dans des TZ différentes coordonnant.
> 
> WEP : « possible profil opérateur en fuseau Asie de l’Est (40%), profil russophone toujours plausible (30%), autre / mixte (30%) ».
> 
> Cette observation est **incertaine** mais alimente l’attribution. Elle est combinée avec d’autres signaux (langue dans portail négociation, infrastructure technique, patterns d’attaques précédentes) pour profiler Akira. Akira pourrait avoir des liens DPRK (cf Lazarus, Ch.29), ce qui collerait avec KST. Mais aussi des liens russophones documentés. Le profil pourrait être **hybride** (opérateurs DPRK + affiliés russophones, modèle observé chez d’autres groupes).
> 
> Sarah note dans le rapport : « les patterns horaires sont cohérents avec une activité d’opérateur en fuseau UTC+9 (KST), mais cette observation est insuffisamment robuste pour conclure sur localisation géographique ». Calibration honnête.

-----

### Chapitre 17 — Clustering : heuristiques, promesses et limites

Le **clustering** — regroupement d’adresses appartenant probablement à la même entité — est l’une des techniques fondamentales de l’enquête crypto. Mais c’est aussi un domaine où les illusions sont nombreuses. Ce chapitre détaille promesses et limites.

#### 17.1 Le concept

**Clustering** : à partir des observations on-chain, on regroupe les adresses qui semblent contrôlées par la **même entité** (un même utilisateur, un même service, une même organisation).

**Pourquoi clusters** :

- Une entité utilise typiquement **multiples adresses** (rotation, séparation par usage, hot/cold).
- Reconstituer le **portefeuille complet** d’une entité permet une vue économique réaliste.
- Identifier l’entité (si possible) sur **n’importe quelle adresse du cluster** étend l’attribution à tout le cluster.

**Comment** : par application d’**heuristiques** sur les transactions observées.

#### 17.2 Les heuristiques principales

**1. Heuristique du co-spend (multi-input)**. Sur Bitcoin, plusieurs inputs co-dépensés dans une transaction sont contrôlés par la même entité (qui possède les clés privées de tous). Forte mais cassée par CoinJoin.

**2. Heuristique du change**. Sur Bitcoin, l’output « change » d’une transaction est contrôlé par l’entité qui a émis. Diverses sous-heuristiques pour identifier le change (Ch.6).

**3. Heuristique du timing**. Adresses actives dans des fenêtres temporelles très proches sont possiblement liées.

**4. Heuristique du wallet**. Certains wallets (Electrum, Bitcoin Core, etc.) génèrent les adresses selon des patterns reconnaissables. Reconnaissance du wallet utilisé est un signal.

**5. Heuristique de l’address reuse**. Une adresse qui reçoit un dépôt unique puis envoie immédiatement vers une nouvelle adresse jamais vue suit un pattern HD wallet (transit).

**6. Heuristique des patterns de service**. Exchange consolide selon patterns reconnaissables (cadence, seuils). L’analyste expérimenté identifie les patterns d’exchange spécifiques.

**7. Heuristique des labels propriétaires**. Les outils Chainalysis/TRM/Elliptic ont des **bases label** internes (acquises par : recherche, KYC achetés, leaks, partenariats avec exchanges). Une adresse labellisée est un point d’attribution dans un cluster.

#### 17.3 Le clustering Ethereum : différent

Ethereum n’a **pas** d’heuristique du co-spend (transactions à un seul émetteur). Le clustering Ethereum repose sur :

**Patterns d’activité**. Adresses contrôlées par une même entité se comportent souvent de manière cohérente (interactions avec mêmes smart contracts, paiements gas par même source, etc.).

**Funding source**. Si une adresse est créée et immédiatement financée par une autre adresse, c’est un signal de contrôle commun.

**Smart contract ownership**. Une adresse qui a déployé un smart contract est probablement liée aux adresses qui interagissent avec ce contrat de manière privilégiée.

**Cross-chain activity**. Une adresse Ethereum qui bridge des fonds vers TRON, et l’adresse TRON destinataire qui a un pattern d’activité similaire, suggère même entité.

**Limites** : clustering Ethereum est **moins robuste** que Bitcoin co-spend. Les outils s’appuient massivement sur **labels propriétaires** et heuristiques mixtes.

#### 17.4 Promesses du clustering

**Quand le clustering fonctionne bien** :

**Wallets utilisateurs simples**. Un utilisateur basique avec wallet Bitcoin Core génère plusieurs adresses, fait des transactions classiques. Heuristique du co-spend reconstitue le wallet en cluster. Précision élevée.

**Services / exchanges**. Les services consolident des fonds utilisateurs vers hot wallets. Le co-spend massif et patterns reconnaissables identifient le service. Cluster Coinbase = des centaines de milliers d’adresses, identifié avec précision élevée.

**Acteurs criminels naïfs**. Les acteurs qui n’ont pas pris de précautions OPSEC (réutilisation d’adresses, co-spend entre wallets « privés » et wallets « publics ») sont rapidement identifiés.

**Ransomware classique**. Les opérateurs ransomware qui collectent des dizaines de paiements vers un même wallet opérationnel forment un cluster identifiable.

#### 17.5 Limites du clustering

**Quand le clustering échoue ou induit en erreur** :

**CoinJoin**. Wasabi et Samourai cassent l’heuristique du co-spend. Inputs co-dépensés ne sont **pas** d’une même entité. Un cluster constitué via co-spending sur des transactions CoinJoin est **faux**. Les outils modernes détectent les CoinJoin et excluent ces transactions du clustering — vérifier que c’est le cas.

**Wallets modernes anti-tracking**. Wallets qui randomisent volontairement la structure des transactions (montants non-ronds aléatoires, position du change, etc.) limitent l’efficacité des heuristiques.

**Multi-sig**. Adresses multisig sont contrôlées par plusieurs parties (M-of-N). Pas une seule entité. Heuristiques qui supposent contrôle unique se trompent.

**Smart contracts (Ethereum)**. Adresses contrôlées par smart contracts (exchanges décentralisés, pools de liquidité, comptes contrats) ont des patterns propres qui ne se prêtent pas au clustering classique.

**Adresses partagées implicites**. Certains wallets « shared » ou exchanges qui n’utilisent qu’un seul wallet pour multiples utilisateurs créent des « clusters » qui sont en fait des **agrégations**, pas des entités uniques.

**Erreurs en cascade**. Si une heuristique commet une erreur en début de chaîne, tout le cluster qui en découle est faux. Outils intègrent scores de confiance pour limiter, mais erreurs existent.

**Adversarial design**. Acteurs qui connaissent les heuristiques peuvent **délibérément** créer des transactions trompeuses pour brouiller (faux co-spending, fausses peeling chains).

#### 17.6 Vocabulaire et calibration

**Cluster** : ensemble d’adresses regroupées comme appartenant probablement à la même entité.

**Niveau de confiance d’un cluster** :

- **Très fiable** : multiple heuristiques convergentes, peu de risques d’erreur (cluster d’exchange majeur, par exemple).
- **Fiable** : heuristique principale solide, validation par patterns secondaires.
- **Probable** : heuristique principale plausible, mais alternatives existent.
- **Spéculatif** : pattern observé mais sans fort support, à vérifier.

**Affirmer « le cluster X »** sans calibration de confiance est une erreur. Toujours expliciter.

**Vocabulaire à utiliser** :

- « Le cluster comprend X adresses, attribué par Chainalysis avec confiance « high » à l’entité Y ».
- « Le cluster reconstruit par heuristiques de co-spend regroupe N adresses ; cette construction est probable (~80%) sauf erreur de heuristique non détectée ».
- « L’entité présumée derrière le cluster est probablement [exchange/individu/groupe] (confiance Y%) ».

#### 17.7 Validation croisée

**Multi-outils**. Si Chainalysis et TRM Labs concluent au même cluster, confiance plus élevée que si un seul outil. Validation indépendante.

**Cohérence comportementale**. Le cluster a-t-il un comportement **cohérent** dans le temps ? Patterns d’activité stables ? Si le cluster évolue brusquement (devient hyperactif, change de patterns), il peut s’agir d’un **changement de contrôle** (vente, hack, changement opérationnel).

**Recoupement OSINT**. Si le cluster correspond à une entité publiquement attribuée (annonce officielle, label vendor, mention OSINT), validation externe.

#### 17.8 Le clustering n’est pas une preuve d’identité

**Message clé à intérioriser** :

> Le clustering ne prouve pas une identité. Il propose un regroupement probable d’adresses contrôlées par une même entité ou un même service, selon des heuristiques discutables.

Une entité du cluster peut être :

- Un wallet utilisateur unique.
- Un service (exchange, mixer).
- Un agrégat artificiel (erreur de heuristique).

L’**identité civile** derrière n’est pas dans le cluster. Elle nécessite des éléments **off-chain** (KYC exchange, mention publique, recoupement OSINT).

Le cluster est un outil pour **structurer la vue**, pas pour conclure. L’analyste avisé manipule les clusters comme des hypothèses calibrées, pas comme des vérités.

-----

### Chapitre 18 — Attribution : adresse → service → personne

L’**attribution** est l’opération qui consiste à associer une adresse, un cluster, ou un flux à une **entité identifiée**. Plusieurs niveaux existent. Ce chapitre les distingue et calibre les niveaux de preuve.

#### 18.1 Les trois niveaux d’attribution

**Niveau 1 — Attribution à un service**. « Cette adresse est un dépôt Binance. » L’entité attribuée est un **service** (exchange, custodian, marchand). Le service connaît l’identité civile de l’utilisateur (via KYC), mais l’analyste OSINT ne la connaît pas — elle nécessite réquisition.

**Niveau 2 — Attribution à un acteur connu**. « Cette adresse est contrôlée par Lazarus / Akira / AlphaBay. » L’entité attribuée est un **acteur identifié** (groupe, individu connu, organisation). L’attribution s’appuie sur preuves publiques (annonces vendor, labels OFAC, recoupements OSINT).

**Niveau 3 — Attribution à une personne nommée**. « Cette adresse est contrôlée par [Nom de personne réelle]. » L’entité attribuée est un **individu civil identifié**. Très rare en OSINT pur, généralement issue de procédures judiciaires (saisies, inculpations).

L’analyste opère principalement aux niveaux 1 et 2. Niveau 3 relève des autorités.

#### 18.2 Distinguer adresse, wallet, service, personne

**Adresse** : identifiant cryptographique. Singulier.

**Wallet** : ensemble d’adresses contrôlées par une même clé privée racine (HD wallet) ou une même infrastructure (multi-sig, custody). Peut contenir des centaines ou milliers d’adresses.

**Service** : entité qui opère un wallet (ou des wallets) pour servir des clients. Exchange, custodian, processeur de paiement, mixer. Le service contrôle les clés ; les utilisateurs ont des **comptes** chez le service mais pas les clés.

**Personne** : individu civil. Peut être :

- Utilisateur direct d’un wallet (non-custodial).
- Utilisateur d’un service (custodial).
- Salarié / dirigeant d’un service.
- Membre d’un groupe criminel utilisant un wallet collectif.

Chaque niveau requiert un type d’attribution différent.

**Erreur classique** : « cette adresse appartient à [personne] » alors que l’enquête montre seulement « cette adresse a déposé chez Binance ». Personne ≠ adresse de dépôt.

#### 18.3 Sources d’attribution

**Preuve directe** :

- Publication volontaire par le propriétaire (« voici mon adresse de tip »).
- Données KYC obtenues via réquisition (autorités).
- Aveu / coopération (procédure judiciaire).

**Preuve forte** :

- Saisies officielles avec adresses publiquement attribuées (FBI press release, DOJ unsealed indictment).
- Sanctions OFAC (SDN list inclut adresses crypto).
- Documents judiciaires publics (acte d’accusation, jugement).

**Preuve modérée** :

- Labels d’outils professionnels (Chainalysis, TRM, Elliptic) — basés sur recherche propriétaire, parfois leaks, parfois partenariats.
- Annonces publiques de vendeurs, services (« notre adresse hot wallet est X »).
- Patterns d’usage cohérents avec attribution (très haut volume, pattern exchange).

**Preuve faible** :

- Recoupement par cluster avec une adresse labellisée.
- Mention sur forum non-vérifiée.
- Inférence par pattern.

**Les outils pro mélangent souvent ces niveaux** — un label dans Chainalysis peut être basé sur preuve forte (annonce officielle exchange) ou modérée (inférence pattern). La documentation interne précise généralement, mais l’analyste sérieux **vérifie la source**.

#### 18.4 L’échelle de confiance d’attribution

**Format type** (Annexe E pour matrice complète) :

|Niveau       |Probabilité|Critères                                            |
|-------------|-----------|----------------------------------------------------|
|Certain      |>95%       |Preuve directe (saisie officielle, OFAC, KYC obtenu)|
|Très probable|80-95%     |Multiple labels convergents + comportement cohérent |
|Probable     |60-80%     |Label outil pro + patterns soutenant                |
|Possible     |40-60%     |Inférence par cluster + label faible                |
|Spéculatif   |<40%       |Pattern observé sans support fort                   |

**Bonne pratique** : noter le niveau dans la fiche d’adresse et dans le rapport.

**Évolution dans le temps** : attribution peut **monter** (nouvelles preuves) ou **descendre** (preuves contradictoires émergentes). La fiche évolue.

#### 18.5 Cas typiques de mauvaise attribution

**Mauvaise attribution 1 — confondre dépôt exchange et exchange lui-même**.

Une adresse de **dépôt** chez un exchange (créée par l’exchange pour un utilisateur précis) est différente du **hot wallet** de l’exchange. L’adresse de dépôt est attribuée à **l’utilisateur** (via KYC exchange), pas à l’exchange en tant qu’entité criminelle.

Erreur : « cette adresse est Binance » alors que c’est en fait l’adresse de dépôt d’un utilisateur de Binance.

Bon : « cette adresse est une adresse de dépôt utilisateur chez Binance. L’identification de l’utilisateur nécessite réquisition ».

**Mauvaise attribution 2 — sur-attribution par cluster**.

Cluster reconstitué par heuristiques regroupe 50 adresses. Une des adresses est labellisée « possibly Lazarus ». Conclure « tout le cluster est Lazarus » est une **sur-attribution** : le label est faible, le cluster peut contenir d’autres entités, l’erreur peut se propager.

Bon : « cluster contient une adresse labellisée ‘possibly Lazarus’ avec confiance modérée. Le label peut être correct ou ne couvrir qu’une partie du cluster ».

**Mauvaise attribution 3 — attribution à un acteur étatique sans preuve**.

Un cluster qui utilise Tornado Cash et bridges → tentation de l’attribuer à Lazarus. Mais Lazarus n’est pas le seul à utiliser ces outils. Sans preuve spécifique (technique d’attaque, infrastructure, adresses précédemment attribuées), l’attribution étatique est spéculative.

Bon : « patterns cohérents avec acteurs étatiques type Lazarus, mais attribution requiert éléments additionnels pour confirmation ».

**Mauvaise attribution 4 — confondre opérateur et affilié**.

Dans le RaaS, l’opérateur (qui fournit le malware et l’infrastructure) est distinct des affiliés (qui exécutent les attaques). Une adresse de paiement ransomware peut être contrôlée par l’affilié, le service de blanchiment, l’opérateur, ou une combinaison.

Bon : « adresse contrôlée par un acteur du programme Akira, sans précision possible sur affilié ou opérateur sans preuves additionnelles ».

#### 18.6 L’attribution dans les rapports

**Bonnes formulations** :

- « L’adresse X est très probablement (confiance >90%) une adresse de hot wallet de Binance, sur la base du label Chainalysis et du pattern d’activité cohérent. »
- « Le cluster Y contient une adresse précédemment attribuée par OFAC à Lazarus. Le cluster lui-même est probablement (confiance ~75%) lié à des opérations Lazarus, sans pouvoir préciser si l’ensemble du cluster est dédié ou partagé. »
- « L’adresse Z a un comportement cohérent avec un opérateur de pig butchering, mais sans label vendor ni recoupement OSINT, l’attribution reste possible (~50%). »
- « L’identification de l’utilisateur final derrière l’adresse de dépôt nécessite une réquisition auprès de l’exchange concerné, qui dépend des autorités compétentes. »

**Mauvaises formulations** (à éviter) :

- « L’adresse X est Lazarus. » (Sans calibration ni preuve.)
- « Le propriétaire de cette adresse est [nom]. » (Sans preuve directe.)
- « Le cluster est entièrement contrôlé par [groupe]. » (Sur-attribution.)

#### 18.7 La responsabilité de l’analyste

L’attribution **engage**. Une attribution incorrecte peut :

**Nuire à un tiers innocent**. Si Sarah attribue à tort un wallet à un individu nommé, et que le rapport est utilisé contre cet individu, dommage réputationnel et juridique potentiel.

**Compromettre une enquête**. Mauvaise attribution oriente l’enquête dans la mauvaise direction, ressources gaspillées.

**Discréditer l’analyste et son organisation**. Une attribution démontrée fausse érode la crédibilité.

**Implications légales**. Diffamation crypto : possible si nom propre attribué sans base solide.

**Discipline** : l’analyste calibre **systématiquement**. Mieux vaut « probable » correct que « certain » incorrect. Mieux vaut « identité non déterminable sans réquisition » que « propriétaire X » erroné.

#### 18.8 Fil rouge — MIXSHADOW : attribution prudente

> **🔗 MIXSHADOW — Épisode 12 : calibration d’attribution**
> 
> Sarah finalise l’attribution dans son rapport intermédiaire (semaine 4).
> 
> **Adresse de réception ransomware** :
> 
> - Niveau d’attribution : **probable**, dédiée à l’opération Aurélien Médical, contrôlée par un opérateur Akira ou affilié.
> - Confiance : ~85%.
> - Base : pattern dédié (adresse fraîche utilisée une seule fois pour cette victime), montant correspondant exactement à la rançon négociée, contexte (le portail de négociation Akira a fourni cette adresse).
> - Pas plus précis que « opérateur Akira ou affilié » — distinction non déterminable.
> 
> **Cluster Bitcoin opérationnel post-paiement** :
> 
> - Niveau d’attribution : **probable** Akira (contrôle continu post-paiement).
> - Confiance : ~80%.
> - Base : continuité du peeling chain depuis l’adresse de réception, pattern cohérent, pas de discontinuité.
> - Reste : pourrait être un **service de blanchiment** sous-traitant pour Akira, plutôt qu’Akira directement.
> 
> **Hubs TRON suspects (services de blanchiment)** :
> 
> - Niveau d’attribution : **possible** services de blanchiment.
> - Confiance : ~65%.
> - Base : patterns hub (multi-sources / multi-destinations), pas attribué dans labels Chainalysis/TRM mais cohérent avec services à risque.
> - Action : alerter labels Chainalysis pour enrichir leur base, croiser avec d’autres incidents Akira.
> 
> **FixedFloat / exchange non-KYC X / Tornado Cash** :
> 
> - Niveau d’attribution : **certain** (services publiquement identifiés).
> - Pas de confusion possible — ce sont des services connus.
> 
> **Acteur Akira lui-même (groupe)** :
> 
> - Niveau d’attribution : **certain** que ces fonds sont liés à l’opération ransomware Aurélien Médical attribuée à Akira (le groupe Akira a revendiqué via leak site et négocié avec Aurélien Médical).
> - Mais attribution **personnelle** (qui est dans Akira ?) : **non déterminable** dans le périmètre OSINT MIXSHADOW. Réservé aux autorités via coopération internationale.
> 
> Sarah documente chaque niveau dans le rapport. Pas de précipitation. Pas d’attribution civile spéculative. Calibration honnête. Le rapport est crédible parce qu’il est calibré.
> 
> Cette discipline va payer : la DGSI valide le rapport intermédiaire et le transmet à Europol pour exploitation, parce que les attributions sont exploitables (claires, calibrées, sourcées) — pas politiquement compromises par des sur-attributions.

-----

## PARTIE IV — OUTILS ET WORKFLOW

> **Ce que cette partie apprend.** Choisir et utiliser les bons outils pour l’enquête crypto. Outils gratuits et leurs limites, outils professionnels (Chainalysis, TRM Labs, Elliptic) et leurs walkthroughs concrets, outils de visualisation, qualification des sources de labels, gestion de la chaîne de preuve, et construction d’un workflow d’enquête reproductible.
> 
> **Ce qu’elle ne couvre pas.** Catalogue exhaustif d’outils (référence : Annexe G). Détails de fonctionnalités secondaires. Outils trop spécialisés pour l’usage courant.
> 
> **Ce que vous saurez faire après cette partie.** Construire une investigation outillée avec les bons choix selon enjeu, budget et contexte. Utiliser Chainalysis Reactor ou TRM Labs avec efficacité. Visualiser un graphe d’enquête lisible. Maintenir une chaîne de preuve crypto solide.

-----

### Chapitre 19 — Outils gratuits et explorateurs avancés

Avant de souscrire à Chainalysis ou TRM Labs (50-500 k USD/an), beaucoup d’enquêtes peuvent être menées avec des **outils gratuits**. Ce chapitre cartographie l’arsenal gratuit du crypto-forensique.

#### 19.1 Les explorateurs blockchain (rappel et approfondissement)

Déjà couverts Ch.11. En usage avancé :

**Mempool.space** :

- API gratuite généreuse pour scripts.
- Fonctionnalités avancées : visualisation des UTXO, estimateur de frais, vue mempool en temps réel.
- Parfait pour Bitcoin.

**Etherscan.io** :

- API gratuite (5 calls/sec gratuit, plus en payant).
- Recherche avancée : filtrage transactions par range de blocs, par méthode appelée.
- Watch list pour monitoring d’adresses.

**Tronscan, Solscan, BscScan, etc.** : équivalents par chaîne.

**Blockchair.com** : multi-chain, recherche cross-chain pratique.

#### 19.2 OXT.me — l’outil Bitcoin avancé gratuit

**OXT** (OpenX Tools) est un outil communautaire dédié à l’analyse Bitcoin avancée. Maintenu par Samourai Wallet historiquement, accessible via oxt.me.

**Capacités** :

- Analyse de peeling chains.
- Reconstitution de clusters par heuristiques.
- Visualisation de graphes Bitcoin.
- Statistiques transactionnelles avancées.
- Détection de patterns (CoinJoin, consolidation, etc.).

**Cas d’usage** : analyse fine d’une chaîne de transactions, validation de clustering, exploration d’historique.

**Limites** : Bitcoin uniquement, interface technique, pas de support client.

#### 19.3 Breadcrumbs.app

**Breadcrumbs** propose une interface graphique pour exploration de flux. Tier gratuit limité (en transactions explorées par jour) ; tier payant pour usage intensif.

**Capacités** :

- Visualisation interactive de flux blockchain.
- Multi-chain (BTC, ETH, principales).
- Suivi simple de chemins (« où vont ces fonds ? »).
- Export pour rapports.

**Cas d’usage** : visualisation rapide d’un flux pour rapport ou démo.

**Limites** : moins puissant que Chainalysis Reactor mais plus accessible.

#### 19.4 Arkham Intelligence (accès public)

**Arkham Intelligence** est une plateforme de blockchain intelligence. Une partie est en accès **public gratuit** (recherche d’adresses, vue de wallets attribués) ; les fonctionnalités avancées sont en abonnement.

**Capacités gratuites** :

- Recherche d’adresses avec attributions publiques (« Vitalik Buterin », « Justin Sun », et milliers d’entités).
- Vue d’ensemble des holdings d’une adresse multi-chain.
- Information sur transactions notables.

**Pour l’enquêteur** : excellent pour vérifier rapidement si une adresse est connue publiquement. Complémentaire d’Etherscan.

#### 19.5 DeBank

**DeBank** : portfolio explorer multi-chain pour adresses Ethereum/EVM. Gratuit en consultation.

**Capacités** :

- Vue portfolio d’une adresse (tokens détenus, valeurs USD).
- Activité DeFi (positions sur protocoles).
- Historique de transactions DeFi décodé.

**Cas d’usage** : pour adresse Ethereum identifiée, comprendre rapidement « combien vaut ce wallet et où est l’argent ».

#### 19.6 Dune Analytics

**Dune Analytics** : plateforme de dashboards SQL sur données blockchain. Tier gratuit pour consultation, payant pour création/édition avancée.

**Capacités** :

- Dashboards créés par communauté pour des sujets spécifiques (volumes ransomware, flux Tornado Cash, exchanges activity, etc.).
- Recherche libre via SQL pour analystes techniques.
- Visualisations préconfigurées.

**Cas d’usage** : recherche de patterns macro (« qui sont les plus gros utilisateurs de tel mixer ? »), benchmarks sectoriels.

#### 19.7 Token Sniffer / GoPlus

Outils d’**analyse de tokens** pour détection de honeypots, rug pulls, tokens malveillants.

**Capacités** :

- Vérification automatique du code d’un token (présence de blacklist, fonctions cachées, taxes anormales).
- Score de risque.
- Détection de patterns connus de fraude.

**Cas d’usage** : pour enquête sur un token suspect (rug pull, scam), valider rapidement la malveillance.

#### 19.8 Revoke.cash

**Revoke.cash** : outil pour utilisateurs (révoquer approvals abusifs), mais aussi pour enquêteurs (consulter approvals d’une adresse).

**Capacités** :

- Liste des approvals actifs d’une adresse Ethereum (ou EVM).
- Identifie les approvals « illimités » (potentiellement dangereux).
- Permet la révocation pour les utilisateurs (transaction signée).

**Cas d’usage enquêteur** : pour adresse drainée, comprendre **quel contrat** la victime a approuvé. Identifier le drainer.

#### 19.9 Chainabuse

**Chainabuse** : plateforme communautaire de signalement d’arnaques crypto.

**Capacités** :

- Recherche d’adresses signalées comme frauduleuses.
- Détails des arnaques (catégorie, date, victimes).
- Contribution communautaire.

**Cas d’usage** : pour adresse potentiellement liée à fraude, vérifier si déjà signalée. Économise du travail (« cette adresse est déjà documentée comme scam, voici les détails »).

#### 19.10 Outils de sécurité et leak research

**Etherscan / Tronscan watch lists** : créer des alertes sur adresses (notifications par email).

**Whale Alert** : suivi public des grosses transactions on-chain (Twitter/X, alertes API). Utile pour macro-trends mais pas pour enquête fine.

**ZachXBT et chercheurs publics** : suivre Twitter/X pour annonces de nouvelles attributions, hacks, scams.

**OnChainScores** : scoring de risque communautaire pour adresses Ethereum.

#### 19.11 Scripts custom Python

Pour usages avancés, **scripts Python** sont incontournables.

**Bibliothèques** :

- **`web3.py`** : interactions Ethereum (lecture transactions, smart contracts).
- **`tronpy`** : équivalent TRON.
- **`python-bitcoinlib`** : Bitcoin.
- **`requests`** + APIs explorateurs : pour analyses sur mesure.
- **`pandas`** : manipulation de données.
- **`networkx`** : graphes d’analyse.

**Cas d’usage** :

- Pull massif de transactions pour une adresse / cluster.
- Analyse statistique sur des milliers de transactions.
- Automatisation de monitoring (scripts cron).
- Intégration de données blockchain dans pipelines analytiques internes.

**Pour l’analyste pro** : minimum un peu de Python est utile. Permet d’automatiser des tâches répétitives et de produire des analyses sur mesure.

#### 19.12 Limites des outils gratuits

Honnêtement :

**Pas de clustering automatique sophistiqué**. Reconstituer manuellement avec heuristiques fonctionne pour petits cas. Pour cas complexes, outils pro nettement supérieurs.

**Labels limités**. Etherscan et autres ont des labels mais bien moins riches que Chainalysis/TRM (qui ont bases propriétaires acquises sur années).

**Pas de scoring de risque automatisé**. Outils gratuits affichent les données ; ils n’évaluent pas le risque (« cette adresse est à 80% risque élevé »).

**Performance sur grosses adresses**. Pour wallet exchange à 100 000 transactions, outils gratuits sont lents.

**Pas de visualisation graphe automatique** (sauf Breadcrumbs limité).

**Pas d’API entreprise**. Pour intégration dans pipelines, outils gratuits sont limités.

**Pour cas complexes** : outils pro indispensables. Pour cas plus simples : outils gratuits suffisent souvent.

#### 19.13 Stratégie de mix gratuit / payant

Recommandation pour cabinet en démarrage ou analyste indépendant :

**100% gratuit** (budget zéro) :

- Mempool, Etherscan, Tronscan + autres explorateurs.
- OXT pour Bitcoin avancé.
- DeBank pour Ethereum portfolios.
- Arkham public.
- Chainabuse pour fraude.
- Maltego Community Edition (limité).
- Scripts Python.

**Premier investissement** (~5-30 k USD/an) :

- Breadcrumbs ou tier payant Arkham.
- Maltego Pro avec quelques connecteurs.
- API payantes Etherscan/équivalents.

**Investissement professionnel** (50-200 k USD/an) :

- Une licence Chainalysis Reactor ou TRM Labs.
- Maltego Pro complet.
- Outils d’automatisation (Splunk, Elastic).

**Investissement enterprise** (200-500 k+ USD/an) :

- Chainalysis Reactor + Chainalysis KYT.
- TRM Labs Investigations + Know Your VASP.
- Elliptic Investigator.
- Plateforme CTI complète intégrée.

L’analyste expérimenté **utilise les bons outils pour les bons cas**. Pas besoin de licence Chainalysis pour suivre une simple transaction Bitcoin. Pas judicieux d’utiliser Etherscan seul pour un dossier multi-chaînes complexe à enjeux M USD.

-----

### Chapitre 20 — Outils professionnels : Chainalysis, TRM Labs, Elliptic

Les **outils professionnels de blockchain intelligence** sont les standards de l’industrie. Ils ne sont pas des « explorateurs en mieux » — ce sont des plateformes intégrées avec capacités cluster, label, scoring, visualisation, et workflow. Ce chapitre couvre les trois leaders et leur usage concret.

#### 20.1 Le marché des outils pro

**Chainalysis** (US, fondé 2014). Leader historique. Solutions :

- **Reactor** : investigation forensique (l’outil détaillé ici).
- **KYT (Know Your Transaction)** : screening AML temps réel pour exchanges/banques.
- **Crypto Investigations Solution** : suite complète pour LEA (Law Enforcement Agencies).

**TRM Labs** (US, fondé 2018). Concurrent direct. Solutions :

- **Forensics / Investigations** : équivalent Reactor.
- **Know Your VASP** : risk rating sur exchanges et services.
- **Tactical Intelligence** : suite LEA.

**Elliptic** (UK, fondé 2013). Solutions :

- **Investigator** : plateforme forensique.
- **Discovery** : screening AML.
- **Lens** : monitoring DeFi.

**Autres acteurs** : CipherTrace (Mastercard), Crystal (Bitfury), Scorechain, Merkle Science, Coinpath / Bitquery, Glassnode (analytics), Nansen (Ethereum/Solana retail), Spot On Chain.

**Différenciateurs** :

- **Couverture** : nombre de chaînes supportées.
- **Profondeur de labels** : taille de la base label propriétaire.
- **Qualité de clustering** : précision des heuristiques.
- **UX et workflow** : ergonomie pour analystes quotidiens.
- **Prix** : varie de 30 k USD/an (petits tiers) à 500 k+ USD/an (full enterprise).

**Pour l’analyste polyvalent** : maîtriser **au moins un** des trois leaders (Chainalysis ou TRM ou Elliptic) est un standard de la profession. La maîtrise d’un permet apprentissage rapide des autres (logiques similaires).

#### 20.2 Chainalysis Reactor : walkthrough

**Reactor** est le produit d’investigation phare de Chainalysis. Référence industrie.

**Interface** :

- **Search bar** : entrée par adresse, TXID, nom d’entité.
- **Graph view** : visualisation interactive des flux.
- **Wallet view** : vue détaillée d’un cluster.
- **Tracking** : suivi de fonds depuis un point de départ.
- **Reports** : génération de rapports.

**Workflow type pour enquête** :

**1. Saisir l’adresse de départ**. Reactor charge le **cluster** auquel elle appartient (basé sur heuristiques + labels propriétaires).

**2. Examiner le cluster** :

- Combien d’adresses dans le cluster.
- Solde total.
- Volume cumulé entrant/sortant.
- **Label propriétaire** si attribué (« Binance », « Tornado Cash », etc.).
- Risk score.

**3. Visualiser les flux**. Reactor affiche un graphe interactif où :

- Les nœuds sont des **clusters** (pas adresses individuelles), simplifiant la vue.
- Les arêtes représentent les flux entre clusters, avec montants agrégés.
- Couleurs encodent les types d’entités (exchange, mixer, sanctioned, unknown).

**4. Drill down**. Cliquer sur un nœud pour voir les adresses du cluster, les transactions, les flux.

**5. Tracking automatisé**. Reactor permet de suivre les flux depuis un point de départ, automatiquement, à travers multiple hops, en identifiant les services traversés. Excellent pour peeling chains et dispersions.

**6. Cross-chain tracking**. Reactor suit les flux à travers les bridges (avec couverture variable selon les bridges supportés).

**7. Export et rapport**. Génère des rapports avec graphes, listes d’adresses, captures pour intégration dans rapport externe.

#### 20.3 TRM Labs Investigations : walkthrough

**TRM Labs Investigations** est l’équivalent. Logique similaire avec quelques différences.

**Forces TRM** :

- **Couverture multi-chaînes** souvent saluée.
- **Labels** sur exchanges régulés et VASPs (couplé à Know Your VASP, fort sur compliance).
- **UX** moderne, workflow fluide.
- **Risk rating** intégré, exploitable pour décisions AML.

**Différences avec Chainalysis** :

- Bases label distinctes (chaque vendor a fait sa recherche).
- Heuristiques de clustering avec calibrations différentes.
- UX différente, préférences personnelles.

**Bonne pratique** : **valider croisée** en utilisant TRM en complément de Chainalysis. Si les deux outils convergent sur une attribution / cluster, confiance plus élevée.

#### 20.4 Elliptic Investigator : walkthrough

**Elliptic Investigator** complète le trio.

**Forces Elliptic** :

- Solide intégration avec écosystème AML traditionnel.
- Capacités spécifiques DeFi via Elliptic Lens.
- Présence forte UK/Europe.

**Logique similaire** aux deux autres. Workflow : adresse → cluster → flux → labels → rapport.

#### 20.5 Limites des outils pro

Ne pas idéaliser. Limites communes :

**Boîtes noires partielles**. Les heuristiques de clustering et les bases label sont propriétaires. L’analyste ne peut pas toujours **vérifier** comment un label a été attribué. Risque : faire confiance aveugle à une « vérité » de l’outil. Discipline : qualifier la source d’un label, croiser quand important.

**Erreurs persistantes**. Tous les outils ont des erreurs (clusters faux, labels obsolètes ou erronés). Réduits dans le temps mais non éliminés. La validation croisée et l’OSINT externe sont sécurisations.

**Couverture incomplète**. Certaines chaînes sont moins bien couvertes (Solana, certaines Layer-2, Cosmos écosystème). Performance varie.

**Lag temporel**. Les outils mettent à jour leurs bases label avec délai. Une adresse récemment attribuée peut ne pas être dans la base au moment de l’enquête.

**Coût**. Peu accessibles aux petites structures, journalistes indépendants, chercheurs académiques.

**Risque de dépendance**. Une organisation 100% dépendante d’un outil unique est vulnérable (changement contractuel, faillite, conflit). Diversifier.

#### 20.6 Quand utiliser quoi

**Reactor / TRM / Elliptic** :

- Investigations à enjeu (paiements ransomware, gros vols, dossiers judiciaires).
- Clusters complexes nécessitant heuristiques avancées.
- Cross-chain tracking.
- Labels propriétaires nécessaires.
- Rapports formels.

**Outils gratuits** (Ch.19) :

- Vérifications ponctuelles.
- Analyses de routine.
- Cas simples bien circonscrits.
- Validation croisée.
- Recherche académique sans budget.

**Combinaison** :

- Étude pro pour analyse principale.
- Outils gratuits pour vérifications, captures publiques (les rapports peuvent référer à Mempool/Etherscan, plus accessible que captures Reactor pour le lecteur externe).

#### 20.7 Fil rouge — MIXSHADOW : workflow Chainalysis + TRM

> **🔗 MIXSHADOW — Épisode 13 : usage des outils pro**
> 
> Sarah utilise **Chainalysis Reactor** comme outil principal et **TRM Labs Investigations** en validation croisée pour MIXSHADOW.
> 
> **Avantages observés** :
> 
> - **Reactor** identifie le cluster Akira BTC operational comme regroupant ~120 adresses (incluant les hops du peeling chain). Sans Reactor, Sarah avait identifié manuellement 62 adresses ; le cluster en révèle 60+ supplémentaires (extensions du peeling chain ou activités annexes du même opérateur).
> - **TRM** confirme le cluster avec ~115 adresses (légère différence de heuristiques, normale). Convergence sur l’essentiel — confiance élevée que le cluster est bien réel et attribué à un acteur Akira.
> - **Reactor** permet de tracker automatiquement les flux à partir du wallet Akira, en suivant à travers les services (FixedFloat, exchanges non-KYC). Visualisation graphe en quelques clics.
> - **TRM Risk Rating** sur les exchanges traversés : exchange non-KYC X est rated « very high risk », confirmant l’angle d’investigation.
> - **Labels propriétaires** : TRM identifie les Hubs TRON suspects comme « probable laundering service, internal cluster » — confirme l’hypothèse Sarah formulée par patterns. Le service n’est pas publiquement connu mais TRM le suit en interne.
> 
> **Limites observées** :
> 
> - **Solana** : un sous-flux mineur transite par Solana en cours de mission. La couverture Reactor est moins profonde sur Solana, certaines transactions ne sont pas labellisées. Sarah complète manuellement.
> - **Tornado Cash sorties** : aucun outil ne « démixe » Tornado Cash directement. Les capacités d’analyse statistique des sorties sont disponibles mais probabilistes, pas certaines.
> - **Erreur ponctuelle** : sur une transaction, Reactor labelise un destinataire comme « Binance hot wallet » alors qu’investigation manuelle révèle que c’est en fait un autre exchange (Bitstamp). Sarah signale l’erreur à Chainalysis support pour mise à jour. Discipline de validation croisée a évité une erreur dans le rapport.
> 
> Sarah produit ses graphes finaux via Reactor (pour visualisations propres), exporte les listes d’adresses, et complète avec captures Mempool/Etherscan/Tronscan pour les éléments référés dans le rapport.
> 
> Le coût des outils est justifié par le résultat : sans Reactor + TRM, l’enquête serait probablement 3x plus longue, avec couverture 50% inférieure. C’est l’investissement qui rend Athéna compétitif.

-----

### Chapitre 21 — Outils de visualisation

Les visualisations sont la **forme finale** des analyses. Elles transforment des données complexes en compréhension humaine. Ce chapitre couvre les outils dédiés.

#### 21.1 Maltego

**Maltego** est l’outil de référence en OSINT investigative pour la visualisation de relations entre entités.

**Capacités pour crypto** :

- **Connecteurs blockchain** via plugins (Maltego CTAS, Maltego Crypto, autres).
- Visualisation de graphes multi-source : crypto + OSINT classique + autres.
- Transforms : enrichissement automatique d’une entité (« voici toutes les transactions de cette adresse »).
- Export pour rapports.

**Forces** :

- **Multi-sources** : combiner crypto avec données OSINT classiques (registres, social media, etc.).
- Communauté active, plugins variés.
- Format reconnu, échange entre analystes.

**Limites** :

- Pas de clustering crypto natif (utilise les données passées via connecteurs).
- Performance limitée pour grands graphes.
- Coût (Pro tier).

**Cas d’usage** : enquêtes mêlant crypto et OSINT classique. Très utilisé en LEA et CTI privé.

#### 21.2 Gephi

**Gephi** est un outil open source d’analyse de réseau.

**Capacités** :

- Import de graphes en multiples formats (CSV, GEXF, GraphML).
- Algorithmes d’analyse réseau : centralité, communautés, modularité.
- Visualisation customisable.
- Export images haute qualité.

**Forces** :

- Gratuit et open source.
- Excellent pour analyses **statistiques** de graphes.
- Permet de détecter automatiquement des communautés (clusters au sens statistique) dans les flux.

**Limites** :

- Courbe d’apprentissage forte.
- Pas conçu spécifiquement pour crypto (pas de connecteurs natifs).
- Workflow d’import / export à automatiser via scripts.

**Cas d’usage** : analyse macro de grands graphes (« quels sont les clusters de communauté dans cet écosystème de wallets ? »).

#### 21.3 Graphistry

**Graphistry** : visualisation GPU pour très grands graphes (>100 k nœuds). Cloud SaaS ou self-hosted.

**Forces** :

- Performance sur graphes massifs.
- Interface moderne.
- API pour intégration.

**Limites** :

- Coût.
- Apprentissage spécifique.

**Cas d’usage** : enquêtes massives, ecosystem-level analysis.

#### 21.4 Mermaid (Markdown)

**Mermaid** : syntaxe pour graphes simples intégrables dans Markdown.

**Exemple** :

```mermaid
graph LR
    A[Aurélien Médical] -->|35 BTC| B[Akira receive]
    B -->|peeling chain| C[Akira ops wallet]
    C -->|0.8 BTC| D[FixedFloat]
    D -->|12.5 ETH| E[Akira ETH]
    E -->|10 ETH| F[Tornado Cash]
```

**Forces** :

- Intégration native dans rapports Markdown / GitLab / GitHub.
- Lisibilité du code.
- Versionnable en texte.

**Limites** :

- Très basique visuellement.
- Pas pour graphes >20 nœuds.

**Cas d’usage** : graphes simples illustratifs dans rapports techniques.

#### 21.5 Excalidraw / drawio

**Excalidraw** et **drawio** sont des outils de dessin diagram interactifs.

**Forces** :

- Gratuits.
- Dessin manuel facile et propre.
- Export multiple formats.
- Excellents pour graphes finaux soignés (rapport exécutif).

**Limites** :

- Manuel — pas de génération automatique depuis données.
- Pas pour grands graphes.

**Cas d’usage** : graphes synthétiques niveau 3/4 pour rapports.

#### 21.6 Cytoscape

**Cytoscape** : alternative à Gephi, JavaScript-based. Customisable. Bon pour intégration dans dashboards web.

#### 21.7 Outils de visualisation intégrés (Reactor, TRM)

Les outils pro (Ch.20) ont leurs **propres visualisations** intégrées. Pour usage interne, suffisent souvent.

**Forces** : intégration native, données déjà clustérisées.

**Limites** : exports parfois rigides, dépendance plateforme.

**Bonne pratique** : utiliser visualisations Reactor/TRM pour analyse en cours, **exporter** vers Maltego/Excalidraw/drawio pour rapports finaux soignés.

#### 21.8 Quand visualiser, quand ne pas

**Visualiser** :

- Pour rapports formels.
- Pour briefings de décideurs.
- Pour comprendre soi-même un flux complexe.
- Pour partager avec des pairs (analystes, autorités).

**Ne pas visualiser** :

- Pour analyses en cours, où le journal Markdown + tableau suffit.
- Pour très petits cas (3 adresses, 2 transactions).
- Quand le graphe serait illisible (10 000 nœuds non abstrait).

#### 21.9 Le graphe pour rapport exécutif

Pour direction / haut management :

- Maximum 5-15 nœuds.
- Niveau 3 (entités) ou 4 (phases).
- Couleurs simples avec légende.
- Annotations textuelles claires.
- Période et source documentées.

Pour audience technique (analystes pairs, autorités) :

- Plus de détail acceptable.
- Niveau 2 (clusters) jusqu’à 20-50 nœuds.
- Détail technique conservé.

Pour annexe technique :

- Détail complet.
- Niveau 1 (adresses) si nécessaire.
- Tout le graphe d’investigation.

#### 21.10 Fil rouge — MIXSHADOW : visualisations finales

> **🔗 MIXSHADOW — Épisode 14 : graphes finaux du rapport**
> 
> Pour le rapport final MIXSHADOW (semaine 8), Sarah produit **trois graphes** :
> 
> **Graphe 1 — Vue exécutive (Excalidraw)** :
> 
> - 10 nœuds : Aurélien Médical → Akira receive → Akira BTC ops → FixedFloat → Tornado Cash → exchange non-KYC X → Hubs TRON → Multiple destinations.
> - 4 phases annotées : Réception / Layering Bitcoin / Conversion-Anonymisation / Dispersion Stablecoins.
> - Couleurs claires, légende.
> - Une page A4.
> 
> **Graphe 2 — Vue opérationnelle (Maltego)** :
> 
> - ~50 nœuds : adresses principales et clusters.
> - Niveau 2/3.
> - Annotations sur niveaux de confiance.
> - Pour briefing DGSI et coordination Europol.
> 
> **Graphe 3 — Vue technique complète (Reactor export)** :
> 
> - Toutes les adresses (~250).
> - Niveau 1.
> - Annexe technique du rapport.
> - Format détaillé pour analystes pairs vérification.
> 
> Les trois graphes sont produits avant la rédaction finale du rapport. Ils servent de **support de réflexion** (Sarah valide sa compréhension en visualisant) puis de **livrables**.
> 
> Au passage, Sarah découvre **deux insights** en construisant le graphe Maltego :
> 
> 1. Une connexion qu’elle n’avait pas vue auparavant : un des Hubs TRON connecte (via une transaction de 5000 USDT) à un cluster déjà documenté dans la base Athéna comme lié à un autre groupe ransomware (Black Basta). Hypothèse : possible **service de blanchiment partagé** entre Akira et Black Basta. Insight majeur — alimente un dossier transversal.
> 1. Un timing remarquable : Akira a fait **trois mouvements** post-paiement en l’espace de 4 heures (peeling, FixedFloat, Tornado), mais ensuite **aucun mouvement** pendant 11 jours. Hypothèse : possible **délai d’observation** par Akira pour vérifier qu’aucune autorité n’a tracé. Pattern OPSEC documenté.
> 
> Ces insights sont intégrés dans le rapport et alimentent les recommandations.

-----

### Chapitre 22 — Labels publics et qualification des sources

Les **labels** sont les étiquettes qui transforment des adresses anonymes en entités identifiables (« exchange Binance », « Tornado Cash », « Lazarus wallet »). Toute l’enquête en dépend. Mais la qualité varie énormément. Ce chapitre apprend à qualifier les sources et à manipuler les labels avec discernement.

#### 22.1 Sources de labels

**Labels Etherscan** (et explorateurs publics) :

- Sourcés par : Etherscan eux-mêmes, contributions communautaires, déclarations d’entités.
- Couverture : exchanges majeurs, smart contracts populaires, certaines adresses notables.
- Qualité : variable. Bonne pour exchanges connus, faible pour acteurs criminels (souvent à jour avec délai).

**Labels Tronscan, Solscan, etc.** :

- Moins riches qu’Etherscan.
- Couvrent les services majeurs sur la chaîne.

**Labels Chainalysis (Reactor, KYT)** :

- Sourcés par : recherche interne Chainalysis, partenariats avec exchanges (KYC information dans certains cas), saisies publiques, OSINT.
- Couverture : très étendue. Centaines de milliers d’entités labellisées.
- Qualité : élevée pour exchanges régulés, moyenne pour acteurs criminels (avec délai pour nouveaux acteurs).

**Labels TRM Labs** :

- Logique similaire à Chainalysis. Bases label distinctes.
- Particulièrement fort sur compliance (Know Your VASP) — exchanges et VASPs dans le monde entier.

**Labels Elliptic** :

- Idem.

**Labels OFAC SDN list** :

- **Source officielle US** : adresses sanctionnées.
- Mise à jour régulière.
- **Référence absolue** pour sanctions : si une adresse y est, elle est officiellement sanctionnée.
- URL : `treasury.gov/ofac/downloads/sdnlist.txt` ou format JSON/XML.

**Labels EU sanctions list** :

- Liste UE des sanctions financières.
- Inclut désormais des adresses crypto.

**Labels saisies / press releases** :

- DOJ, FBI, NCA, Europol, ANSSI, etc. publient parfois des adresses crypto liées à saisies / opérations.
- Officielles, vérifiables.
- Mais limitées dans la couverture (seulement les cas annoncés publiquement).

**Labels par chercheurs publics** :

- ZachXBT (twitter.com/zachxbt) : très actif, attributions souvent reconnues.
- Researchers indépendants.
- Qualité variable selon réputation.

**Labels par communautés** :

- Chainabuse (signalement scams).
- OnChainScores.
- Crypto Scam DB.
- Variable.

**Labels par leaks** :

- Parfois, des leaks (Twitter, Pastebin, dump publics) révèlent des adresses associées à des entités.
- À vérifier avec rigueur.

**Labels par recherche académique** :

- Papers académiques publient parfois listes d’adresses.
- Source crédible, mais peut être obsolète.

#### 22.2 Qualification des labels

Tous les labels ne se valent pas. Critères de qualité :

**Source** : qui a produit le label ? Vendor pro (Chainalysis), source officielle (OFAC), chercheur réputé (ZachXBT) ou source anonyme/communautaire.

**Méthode** : sur quelle base l’attribution a été faite ? Preuve directe (saisie), partenariat (KYC), inférence (heuristique), recoupement OSINT.

**Date** : quand le label a été créé ? Un label de 2020 peut être obsolète en 2026 (compromission, vente, transfert de wallet).

**Validation indépendante** : d’autres sources convergent-elles ? Validation croisée multiple.

**Spécificité** : le label est-il précis (« hot wallet 3 de Binance ») ou vague (« exchange ») ? Précision = utilisable pour décisions, vague = orientation seulement.

#### 22.3 Échelle de confiance des labels

**Référence absolue** :

- Sanctions OFAC SDN list.
- Sanctions UE / ONU.
- Annonce officielle d’une autorité (FBI press release avec adresses).
- Annonce officielle d’un exchange (« voici notre hot wallet »).

**Très fiable** :

- Labels Chainalysis / TRM / Elliptic « high confidence ».
- Multiple convergence multi-vendor.
- Attribution publique par chercheurs reconnus + validation.

**Fiable** :

- Labels Chainalysis / TRM / Elliptic « medium confidence ».
- Source unique mais réputée.
- Recoupements OSINT cohérents.

**À vérifier** :

- Labels Etherscan communautaires non vérifiés.
- Mentions sur Twitter de chercheurs moins connus.
- Attributions par seul outil sans validation.

**Faible confiance** :

- Mentions sur forums.
- Attributions par sources anonymes.
- Patterns sans label vendor.

#### 22.4 Limites communes

**Labels obsolètes**. Une adresse labellisée « Binance » peut avoir été abandonnée par Binance et reprise par d’autres. Les outils mettent à jour avec délai.

**Labels par contagion erronée**. Si un label est attribué à un cluster entier mais qu’une adresse du cluster est en fait différente, le label se propage par erreur.

**Labels marketing**. Certains vendors peuvent labelliser de manière promotionnelle (« voici nos labels exclusifs »). Critique nécessaire.

**Manque de transparence**. Souvent, l’analyste ne peut pas savoir **comment** un label a été attribué. Confiance par défaut + validation croisée.

**Conflits entre vendors**. Chainalysis et TRM peuvent occasionnellement diverger sur un cluster ou un label. Validation croisée et investigation manuelle requise.

#### 22.5 Bonnes pratiques

**Ne jamais reposer sur un seul label**. Pour décisions importantes, recoupement minimum.

**Documenter la source**. Dans la fiche, noter explicitement « Label Chainalysis ‘Binance Hot Wallet’ (confidence: high), confirmé TRM ‘Binance Hot 3’ ».

**Vérifier les sanctions OFAC**. Pour toute adresse importante, vérification SDN. C’est gratuit et rapide.

**Mettre à jour**. Les labels évoluent. Lors des phases de revue, re-vérifier.

**Croiser avec OSINT externe**. Pour adresses notables, recherche Twitter/Google peut révéler attributions complémentaires.

**Marquer le doute**. Si un label semble suspect (incohérence avec le pattern observé), noter et investiguer avant d’utiliser.

#### 22.6 Le cas spécial : sanctions OFAC

Les **sanctions OFAC** méritent traitement spécial.

**Liste SDN (Specially Designated Nationals)**. Tenue par OFAC (Office of Foreign Assets Control, US Treasury). Inclut :

- Personnes physiques sanctionnées.
- Entités sanctionnées (entreprises, organisations).
- **Adresses crypto sanctionnées**.

**Mise à jour** : régulière, avec annonces officielles.

**Implications légales** : interagir avec une adresse OFAC depuis un US person ou via un VASP US peut constituer **violation des sanctions**. Sanctions sévères. Pour entités EU, le cadre est aussi strict (sanctions UE).

**Cas notables** :

- **Tornado Cash** : sanctionné août 2022. Adresses des smart contracts incluses.
- **Garantex** (exchange) : sanctionné avril 2022.
- **Suex** (exchange) : sanctionné septembre 2021.
- **Bitzlato** : sanctionné janvier 2023.
- **Multiple wallets Lazarus** : sanctionnés depuis 2018-2024.

**Pour l’analyste** : toute adresse pertinente est cross-checked avec SDN list. Outils pro intègrent cette vérification automatiquement. Outils gratuits : vérification manuelle possible via le site OFAC.

#### 22.7 Construire sa propre base label

Pour cabinets ou organisations qui investiguent régulièrement, **base label interne** vaut investissement.

**Format type** :

```
| Adresse | Blockchain | Label | Source | Date | Confiance | Notes |
|---|---|---|---|---|---|---|
| bc1q[...] | BTC | Akira receive Aurélien Médical | MIXSHADOW investigation Athéna | 2026-03-14 | High | Adresse fraîche dédiée victime |
| 0xAk1[...] | ETH | Akira ETH wallet (probable) | MIXSHADOW investigation Athéna | 2026-03-19 | Medium | Reçoit fonds via FixedFloat |
| TR[Akira-TRON][...] | TRX | Akira TRON wallet (probable) | MIXSHADOW investigation Athéna | 2026-03-22 | Medium | Reçoit USDT depuis exchange non-KYC X |
```

**Maintenance** : revue trimestrielle, vérification labels obsolètes, ajout de nouvelles attributions.

**Partage** : avec partenaires sectoriels (ISAC, autorités) selon TLP. Contribution à l’écosystème.

-----

### Chapitre 23 — Collecte, conservation et chaîne de preuve crypto

L’enquête ne sert à rien si les preuves ne sont pas **conservées** correctement. Pour rapport, contestation, procédure judiciaire — la **chaîne de preuve** détermine la valeur du travail. Ce chapitre couvre la méthode.

#### 23.1 Pourquoi la chaîne de preuve

Trois objectifs :

**Reproductibilité**. Un autre analyste, 6 mois ou 5 ans plus tard, doit pouvoir refaire l’analyse à partir des mêmes données.

**Crédibilité**. En cas de contestation (par l’acteur enquêté, par un tribunal, par un journaliste), l’analyste peut prouver que les données utilisées sont authentiques.

**Valeur juridique**. Pour soutenir une plainte, une réquisition, ou une saisie, les preuves doivent répondre à des standards.

#### 23.2 Captures d’écran et documents

**Méthode** :

**Screenshots** :

- Capture **complète** de la page (pas seulement zone d’intérêt).
- URL visible.
- Horodatage de capture (date+heure UTC précis).
- Format PNG ou JPG haute qualité.

**HTML / Source** :

- Sauvegarde du **HTML brut** pour archives permanentes.
- Outils : Hunchly, Save Page WE, wget, scripts custom.
- Permet inspection sans dépendance à site externe (qui peut évoluer).

**PDF** :

- Capture en PDF pour annexes de rapport.
- Format portable.

**Hash** :

- SHA-256 de chaque fichier capturé.
- Permet de **prouver** que le fichier n’a pas été modifié.
- Stocker les hashes dans un journal séparé.

#### 23.3 Captures de transactions

Pour chaque transaction d’enquête :

**Capture de la page d’explorateur** :

- Mempool.space, Etherscan, Tronscan, etc.
- Fenêtre complète avec URL.
- Onglets pertinents (Logs ERC-20, Internal Transactions, etc.).

**TXID** :

- Noté dans le journal d’enquête.
- La blockchain est immutable — le TXID est une référence permanente.

**Cross-references** :

- Si même transaction visible sur plusieurs explorateurs, capturer plusieurs vues. Validation croisée.

**Outils pro export** :

- Reactor / TRM / Elliptic permettent exports CSV des transactions analysées.
- Capturer aussi la vue graph dans l’outil.

#### 23.4 Captures d’adresses

Pour chaque adresse pertinente :

**Page d’explorateur** :

- Solde actuel.
- Historique transactions (paginer si nécessaire).
- Labels visibles.
- Première et dernière transaction.

**Page outil pro** (si applicable) :

- Vue cluster.
- Labels propriétaires.
- Risk score.

**Captures successives** : pour adresse en surveillance active, captures régulières (quotidiennes) pour tracer l’évolution.

#### 23.5 Métadonnées du journal d’enquête

Le journal d’enquête (Markdown) inclut, pour chaque entrée :

- **Date et heure UTC**.
- **Action effectuée**.
- **Source consultée** (URL si applicable).
- **Référence à la capture** (nom de fichier + hash SHA-256).
- **Observation et hypothèse**.

Ce journal est lui-même versionné (Git ou équivalent), avec sauvegardes immutables.

#### 23.6 Stockage immutable

**Principe** : les preuves ne doivent pas pouvoir être **modifiées rétroactivement** (par négligence ou par malveillance interne).

**Méthodes** :

**WORM storage (Write Once Read Many)** :

- Solutions enterprise (NetApp, Dell, AWS S3 Object Lock).
- Garantie technique d’immutabilité.
- Standard pour environnements judiciaires sérieux.

**Hashing avec timestamping qualifié** :

- Hash SHA-256 des fichiers.
- Timestamping via service qualifié (e.g. eIDAS qualified timestamping en EU).
- Permet de prouver que le fichier existait à une date précise.

**Blockchain anchoring** :

- Hash des fichiers ancrés dans une blockchain (OpenTimestamps via Bitcoin, par exemple).
- Preuve d’existence à une date.
- Coût marginal.

**Bonne pratique combinée** :

- Hash SHA-256 de chaque preuve.
- Stockage en WORM (ou équivalent).
- Hashes archivés dans un journal cumulatif lui-même WORM.
- Pour cas judiciaires importants : timestamping qualifié.

#### 23.7 Chain of custody

Pour preuves potentiellement judiciaires, tenue d’une **chain of custody** explicite.

**Format type** :

```
Pièce de preuve : Capture transaction TXID e3a5...
Date de collecte : 2026-03-14 09:30 UTC
Collecté par : Sarah Marin, Athéna Group
Source : mempool.space
Hash SHA-256 : abc123...
Format : HTML + PNG screenshot
Stockage : Athéna secure storage, path /MIXSHADOW/evidence/tx_e3a5...
Accès : Sarah Marin, directeur Athéna, autorités sur réquisition
Modifications : Aucune (immutable)
Transmission : Transmise à DGSI le 2026-03-15 (capture intégrale + hash)
```

Chaque pièce a sa fiche. Ensemble forme la chain of custody.

#### 23.8 Limites des captures

**Captures pas suffisantes pour preuve judiciaire absolue**. Une capture peut être falsifiée. Pour preuves lourdes :

- Hashing + timestamping qualifié.
- Cross-references multiples.
- Données de la blockchain elle-même (TXID, qui est immutable).

**Données dynamiques**. Soldes peuvent évoluer entre capture et utilisation. Toujours noter le timestamp.

**Variations explorateurs**. Les explorateurs peuvent évoluer (UI changes, données enrichies). Capture à un moment T peut différer de capture à T+6 mois.

**Solution robuste** : référer aux **données blockchain elles-mêmes** (TXID, block height) — immutables — plutôt qu’aux représentations dans les explorateurs.

#### 23.9 Pour les rapports formels

**Citations de transactions** :

- Format normalisé : « TXID [hash], block [N], date [UTC] ».
- Capture en annexe avec hash.
- Lien stable vers explorateur (si possible).

**Citations d’adresses** :

- Adresse complète.
- Blockchain explicite.
- Capture de page d’explorateur en annexe.

**Citations d’analyses outils pro** :

- « Cluster Reactor ID […] avec [N] adresses, label ‘Akira’ attribué avec confiance high par Chainalysis le [date] ».
- Captures Reactor en annexe.

#### 23.10 Fil rouge — MIXSHADOW : chain of custody

> **🔗 MIXSHADOW — Épisode 15 : preuve solide**
> 
> Pour MIXSHADOW, Sarah maintient une chain of custody rigoureuse.
> 
> **Pour chaque transaction Akira** capturée :
> 
> - Capture HTML de la page Mempool.space (ou Etherscan / Tronscan selon chaîne).
> - Screenshot PNG.
> - Capture de la vue Reactor correspondante.
> - Hash SHA-256 de chaque fichier.
> - Entrée dans le journal Markdown daté.
> 
> **Pour chaque rapport hebdomadaire** envoyé à la DGSI :
> 
> - PDF du rapport.
> - Hash SHA-256 du PDF.
> - Annexes incluses (captures principales).
> - Email avec accusé de réception.
> 
> **Stockage** :
> 
> - Tous les fichiers MIXSHADOW dans un répertoire chiffré.
> - Sauvegarde quotidienne sur stockage WORM Athéna.
> - Hashes cumulés dans un fichier `MIXSHADOW_hashes.csv` lui-même hashé.
> - Tâche cron qui ancre le hash global hebdomadaire dans Bitcoin via OpenTimestamps (preuve d’existence à date).
> 
> **Pour le rapport final** (semaine 8) :
> 
> - Toutes les preuves référées sont accompagnées de leur hash dans l’annexe.
> - Méthodologie de collecte décrite (« captures via Hunchly, hashing SHA-256, stockage WORM, anchoring OpenTimestamps »).
> - Permet à la DGSI ou autorité ultérieure (procureur, juge) de vérifier l’intégrité.
> 
> Le coût en temps : ~10% du temps total d’enquête. Cher mais indispensable. Sans cette discipline, le rapport est lu mais non utilisable formellement. Avec, il est exploitable judiciairement.

-----

### Chapitre 24 — Workflow complet d’une enquête crypto

Synthèse de toute la Partie III. Ce chapitre articule le **workflow complet** depuis la réception du mandat jusqu’à la clôture, intégrant méthodes (Partie III), outils (Ch.19-23), et discipline.

#### 24.1 Phase 1 — Cadrage et réception du mandat

**Inputs** : demande client / autorité / alerte.

**Actions** :

- **Validation du mandat** : périmètre clair, objectifs réalistes, livrables explicites, délais et budget.
- **Cadre légal** : confirmation du cadre (RGPD, secret professionnel, sanctions, autorisation autorités).
- **Affectation analyste(s)** : compétences, charge de travail, conflits d’intérêt.
- **Setup technique** : environnement d’investigation, outils, accès.
- **Communication initiale** : briefing donneur d’ordre, contacts d’autorités si applicable.

**Livrable** : note de cadrage validée par toutes les parties.

#### 24.2 Phase 2 — Collecte initiale

**Inputs** : indices initiaux (adresse, TXID, capture, etc. — Ch.13).

**Actions** :

- **Vérification** des indices (blockchain correcte, transaction existe, etc.).
- **Lecture initiale** : transaction, adresse principale.
- **Constitution fiche d’adresse** initiale.
- **Captures** systématiques (chain of custody).
- **Documentation** dans journal d’enquête.

**Livrable** : journal initial + fiches d’adresses initiales.

#### 24.3 Phase 3 — Investigation iterative

**Inputs** : indices initiaux exploités.

**Actions** (cycle itératif, plusieurs semaines) :

- **Suivi des flux** : par étape, en suivant chaque output significatif.
- **Identification des contreparties** : nouvelles adresses, services traversés.
- **Enrichissement** : labels, OSINT externe, recoupement.
- **Hypothèses** : formulation et calibration WEP.
- **Construction du graphe** : extension progressive.
- **Documentation continue** : fiches mises à jour, journal à jour.
- **Priorisation** : quelles branches valent l’effort, lesquelles peuvent être abandonnées.

**Livrable** : graphe d’investigation en évolution, fiches multiples.

#### 24.4 Phase 4 — Analyse et synthèse

**Inputs** : graphe et fiches matures.

**Actions** :

- **Identification de patterns** : ransomware, pig butchering, blanchiment, etc.
- **Attribution** : niveau et calibration.
- **Caractérisation des acteurs** : profils, méthodes, infrastructure.
- **Identification des points de coopération** : exchanges KYC, services coopérants.
- **Validation hypothèses** : croisements multiples, validation par pairs.

**Livrable** : analyse synthétique structurée.

#### 24.5 Phase 5 — Production du rapport

**Inputs** : analyse complète.

**Actions** :

- **Rédaction** du rapport selon template (Annexe H).
- **Visualisations** : graphes pour rapport.
- **Captures** : annexe technique avec preuves.
- **Recommandations** : actionables et calibrées.
- **Limites** : explicites et calibrées.
- **Revue par pairs** : peer review interne.

**Livrable** : rapport final.

#### 24.6 Phase 6 — Restitution et coopération

**Inputs** : rapport final.

**Actions** :

- **Briefing** : présentation orale au mandant et autorités.
- **Q&A** : réponses aux questions et clarifications.
- **Coopération** : transmission aux autorités selon TLP, support à actions ultérieures.
- **Signalement** : si infractions graves découvertes (article 40 CPP).
- **Communication** : selon TLP, partage sectoriel (ISAC) si applicable.

**Livrable** : rapport diffusé + restitutions effectuées.

#### 24.7 Phase 7 — Clôture et archivage

**Inputs** : restitution effectuée.

**Actions** :

- **Archivage immutable** : tout le dossier, conformément à la chain of custody.
- **Réflexion post-mortem** : ce qui a fonctionné, ce qui pourrait être amélioré.
- **Capitalisation** : enrichissement de la base interne (labels, patterns, fiches d’acteurs).
- **Communication finale** : remerciements, retours mandant.

**Livrable** : dossier archivé + retours d’expérience.

#### 24.8 Surveillance post-clôture

Selon mandat, **surveillance** des adresses identifiées peut continuer après clôture :

- Alertes automatiques sur mouvements futurs.
- Notification du mandant si évolutions significatives.
- Maintien de la base label.

#### 24.9 Discipline transversale

À chaque phase, principes communs :

**Documentation continue** : journal à jour, fiches actualisées, captures faites.

**Calibration WEP systématique** : pas d’affirmation sans niveau de confiance.

**Validation croisée** : multiple sources, multiple outils.

**Communication claire** : points d’étape réguliers avec mandant.

**Discipline éthique** : pas d’interaction directe avec wallets cibles, respect du périmètre, pas de prolifération.

**Adaptation** : le workflow est un guide, pas un dogme. Chaque enquête a ses spécificités.

#### 24.10 Indicateurs de qualité

Pour évaluer la qualité d’une enquête crypto :

**Couverture** : pourcentage des flux pertinents tracés.

**Calibration** : niveaux de confiance bien justifiés et cohérents.

**Reproductibilité** : un autre analyste peut-il refaire l’analyse à partir des mêmes données ?

**Actionnabilité** : les recommandations sont-elles concrètes et exploitables ?

**Honnêteté** : les limites sont-elles documentées clairement ?

**Délai** : respect des échéances mandat.

**Coût** : budget respecté.

**Satisfaction mandant** : feedback du donneur d’ordre.

#### 24.11 Fil rouge — MIXSHADOW : workflow complet

> **🔗 MIXSHADOW — Épisode 16 : bilan workflow**
> 
> À 8 semaines de mission, Sarah a parcouru le workflow complet :
> 
> - **Cadrage** (semaine 1) : note validée par DGSI + Aurélien Médical + Athéna.
> - **Collecte initiale** (semaines 1-2) : indices initiaux exploités, fiche Akira receive établie.
> - **Investigation** (semaines 2-7) : 250 adresses identifiées, 4 chaînes (Bitcoin, Ethereum, TRON, Solana mineur), graphe complet construit.
> - **Analyse** (semaine 6-7) : patterns Akira caractérisés, attribution calibrée, points de coopération identifiés.
> - **Rapport** (semaine 7-8) : rédaction, visualisations, peer review interne, validation directeur Athéna.
> - **Restitution** (semaine 8) : briefing DGSI + Aurélien Médical, transmission Europol via DGSI.
> - **Clôture** (semaine 8) : archivage immutable, retours mandant.
> 
> **Bilan honnête** :
> 
> ✅ **Réussites** :
> 
> - Cartographie complète des flux Akira post-paiement.
> - Identification de **2 hubs de blanchiment** non précédemment documentés (alimentent la base TRM Labs et Chainalysis).
> - **6 adresses TRON** principales transmises à Tether via DGSI pour évaluation de gel.
> - Pattern de blanchiment Akira **documenté** (template réutilisable pour d’autres victimes).
> - Insight sur **service de blanchiment partagé** Akira / Black Basta — alimente dossier transversal.
> - **3 adresses identifiées comme déposées sur Binance** — coopération Binance via DGSI permet identification utilisateur du compte (mais résultat non communiqué à Athéna).
> 
> ⚠️ **Limites** :
> 
> - **Pas de récupération** des fonds.
> - **Attribution civile** non possible en OSINT — relevait des autorités.
> - **Tornado Cash** : analyse statistique des sorties n’a pas permis attribution claire des retraits correspondants.
> - **Plusieurs branches** n’ont pas été suivies en profondeur (priorisation imposée par budget).
> 
> 📊 **Métriques** :
> 
> - Durée : 8 semaines.
> - Charge : Sarah 80% temps + 1 junior 50% temps.
> - Budget : ~80 k EUR (incluant outils, peer review, livrables).
> - Couverture estimée : ~75% des flux Akira post-paiement Aurélien Médical.
> - Calibration : tous les éléments du rapport ont WEP explicite.
> 
> Sarah note pour le retour d’expérience interne Athéna :
> 
> - **Outils pro** (Chainalysis + TRM) ont apporté gain majeur de temps et couverture.
> - **Coordination DGSI** a permis ouvertures (Tether, Binance) impossibles en OSINT pur.
> - **Workflow structuré** a rendu l’enquête lisible et le rapport crédible.
> - **Limites honnêtes** ont préservé la crédibilité d’Athéna (vs un rapport sur-promesses qui se serait effondré à la première vérification).
> 
> Le dossier MIXSHADOW est archivé. Les insights alimentent les enquêtes futures Athéna.

-----

## PARTIE V — TYPOLOGIES D’ABUS CRYPTO

> **Ce que cette partie apprend.** Reconnaître les grandes typologies d’abus crypto contemporains : pig butchering et scams retail, ransomware et extorsion, hacks DeFi et compromission de wallets, fraudes NFT et tokens, acteurs étatiques (Lazarus). Pour chacune : patterns, modus operandi, signaux, méthodes d’enquête spécifiques.
> 
> **Ce qu’elle ne couvre pas.** Les techniques d’obfuscation détaillées (Partie VI), les cas pratiques déroulés (Partie VII), les cas historiques (Partie VIII).
> 
> **Ce que vous saurez faire après cette partie.** Identifier rapidement la typologie d’une affaire à partir des indices initiaux. Adapter la méthode d’enquête à la typologie. Reconnaître les signaux d’alerte spécifiques. Comprendre où chaque type d’abus s’inscrit dans l’écosystème crypto criminel global.

-----

### Chapitre 25 — Scams retail : romance scam et pig butchering

Le **pig butchering** (« 杀猪盘 », *shā zhū pán* — « élevage du cochon avant l’abattage ») est devenu en 2022-2026 l’un des plus gros postes de pertes financières liées au crypto, avec des estimations Chainalysis cumulées en milliards USD/an. Il combine manipulation sentimentale et faux investissement, ciblant des victimes individuelles sur des durées de plusieurs mois.

#### 25.1 Le modus operandi

**Phase 1 — Approche**. La victime est contactée :

- Via réseaux sociaux (Instagram, LinkedIn, Facebook).
- Via applications de rencontre (Tinder, Bumble, Hinge).
- Via WhatsApp ou Telegram (« mauvais numéro » prétendu).
- Via groupes d’investissement crypto Telegram / Discord.

L’approche est **généralement chaleureuse**, sans demande financière initiale. Construction d’une relation (amicale, sentimentale, professionnelle).

**Phase 2 — Construction de la confiance**. Sur plusieurs semaines/mois :

- Communications quotidiennes.
- Partage de détails « personnels » (vie, famille, succès).
- Création d’intimité.
- Mention progressive du « succès en investissement crypto ».
- Photos volées d’autres personnes (réelles ou IA-générées).

**Phase 3 — Introduction de l’investissement**. Le scammer mentionne :

- Une « plateforme exclusive » avec « gains garantis ».
- Un « mentor » ou « insider tip ».
- Des « gains incroyables » que le scammer prétend avoir réalisés (captures truquées montrant son « portefeuille »).

**Phase 4 — Premier dépôt et premier retrait**. La victime dépose une **petite somme** (500-5000 USD) sur la plateforme frauduleuse. Le scammer **autorise un petit retrait** initial pour crédibiliser. La victime voit ses fonds revenir, gagne confiance.

**Phase 5 — Escalade**. Encouragée par le « succès initial », la victime augmente progressivement :

- Investissements plus gros.
- Prises de prêts pour investir plus.
- Liquidation d’épargne.
- Demande aux proches.

**Phase 6 — Le « chômage » du retrait**. Quand la victime tente de retirer une somme significative :

- « Frais d’audit fiscal » à payer.
- « Caution de sécurité » exigée.
- « Vérification d’identité supplémentaire » qui débloque un retrait moyennant nouveau paiement.
- Cycle : chaque demande de retrait génère une nouvelle demande de paiement.

**Phase 7 — Disparition**. Quand la victime réalise (ou n’a plus rien à donner), le scammer disparaît. Compte coupé, profil supprimé, plateforme inaccessible.

**Bilans typiques** : pertes individuelles de 50 k à 1 M USD+. Cas documentés dépassant 5 M USD pour victimes uniques.

#### 25.2 Le réseau opérateur

**Pig butchering n’est PAS un scam individuel**. C’est une **industrie**.

**Structure typique** :

- **Scam compounds** localisés en Asie du Sud-Est (Cambodge, Laos, Myanmar, Philippines). Bâtiments où des centaines à milliers de **« scammeurs »** (parfois eux-mêmes victimes de trafic humain) opèrent sous coercion.
- **Opérateurs / patrons** : organisations criminelles (souvent liées à des syndicats chinois) qui gèrent les compounds.
- **Réseau de blanchiment** : flux USDT-TRON consolidant les paiements des victimes.
- **Infrastructure** : plateformes web crédibles, sites de phishing, canaux Telegram/WhatsApp.

**Cooperation avec le crime organisé**. ZachXBT, OFAC et plusieurs reports (Chainalysis, TRM, Elliptic) documentent depuis 2022-2024 le rôle de syndicats criminels asiatiques dans le pig butchering. Sanctions contre certains compounds documentées.

**Pour la victime** : dans la grande majorité des cas, le « scammeur » qui lui parle quotidiennement n’est **pas le décideur** — c’est un opérateur de bas niveau sous pression (parfois traffiqué). La structure derrière est ce qui prélève les fonds et organise le blanchiment.

#### 25.3 Les flux crypto typiques

**Pattern observable on-chain** :

**Étape 1 — Réception sur adresse de collecte**. La plateforme frauduleuse demande à la victime d’envoyer USDT-TRON (le plus fréquent, ou parfois USDT-Ethereum, plus rarement BTC) vers une adresse spécifique.

**Étape 2 — Adresses de collecte multi-victimes**. Sur Tronscan, on observe l’**adresse de collecte** recevant des USDT depuis plusieurs adresses de victimes différentes. Un cluster typique :

- Adresse de collecte centrale.
- 10-100 adresses de victimes envoyant.
- Montants variables (de 500 à 100 000+ USD chacun).
- Période étalée sur semaines/mois.

**Étape 3 — Consolidation rapide**. L’adresse de collecte transfère rapidement les fonds vers une adresse hub.

**Étape 4 — Layering**. Le hub fait du peeling chain TRON-style ou disperse vers multiples sub-adresses.

**Étape 5 — Off-ramp**. Les fonds finissent vers :

- Exchanges régionaux moins regardants (souvent Asie).
- P2P / OTC.
- Conversion en autres cryptos (BTC, monero, autres).
- Cartes prepaid crypto.

#### 25.4 Reconnaître un cluster pig butchering

**Signaux** :

**Adresse de collecte centrale** recevant de **multiples sources** (>5-10 victimes différentes).

**Montants variables** (pas tous identiques) — caractéristique de victimes individuelles vs scam d’identité de masse.

**Pattern temporel étalé** sur des semaines/mois (vs scam ponctuel).

**Consolidation rapide** vers hub après réception.

**Flux vers exchanges régionaux** ou P2P en finale.

**Activité concentrée** sur USDT-TRON.

**Fraîcheur** : les adresses de collecte sont souvent fraîches (créées peu avant l’opération), réutilisées sur quelques semaines, puis abandonnées au profit de nouvelles.

#### 25.5 Méthode d’enquête

**Étape 1 — Indice initial**. Souvent : adresse fournie par victime + screenshots conversation + détails plateforme frauduleuse.

**Étape 2 — Validation**. TXID confirmant le dépôt. Lecture sur Tronscan.

**Étape 3 — Expansion vers cluster**. Identifier l’**adresse de collecte** (premier destinataire). Lire son historique : combien d’autres dépôts a-t-elle reçu ? Volume cumulé ? Patterns ?

**Étape 4 — Identification d’autres victimes**. Les autres adresses ayant déposé sur la même collecte sont **probablement d’autres victimes**. Si la victime principale fait plainte, ces co-victimes peuvent être identifiées (et alerter les autorités si plaintes coordonnées).

**Étape 5 — Suivi des flux post-collecte**. Le hub redistribue vers où ? Identification des chemins de blanchiment.

**Étape 6 — Off-ramps**. Identification des exchanges utilisés en finale. Si exchange régulé : possibilité de réquisition KYC.

**Étape 7 — Rapport et action**.

#### 25.6 Limites de l’enquête pig butchering

**Récupération rare**. Les fonds sont souvent dispersés rapidement. Le délai entre dépôt victime et cashout est court (jours/semaines). Au moment où la victime réalise et porte plainte, fonds sont souvent déjà out.

**Identification du « scammeur » individuel** : très difficile. C’est rarement un acteur identifiable (compounds Asie du Sud-Est).

**Identification des opérateurs** : possible via patterns à grande échelle, mais judiciairement complexe (juridictions, coopération internationale variable).

**Effet psychologique sur victime**. La victime est souvent **doublement traumatisée** : perte financière + manipulation sentimentale révélée. Approche humaine importante.

**Réponse défensive sectorielle** : sensibilisation grand public, alertes plateformes, partenariats avec banques pour détecter virements suspects.

#### 25.7 Coordination

**Signalement aux autorités** :

- **Cybermalveillance.gouv.fr** (France) : pour victimes individuelles.
- **TRACFIN** : pour banque détectant flux suspect.
- **Plainte police / gendarmerie** locale.
- **FBI IC3** (US) si concerné.

**Coopération internationale** :

- **Operation Shamrock** (US, depuis 2024) : coordination LEA contre pig butchering.
- **GLACY+ Council of Europe** : capacity building anti-cybercrime.
- **Europol EC3** : coordination EU.

**Sanctions** : OFAC a sanctionné certains compounds et opérateurs depuis 2024. Suivre les listes pour adresses sanctionnées.

#### 25.8 Cas typiques

**Romance scam pure** : intimité construite, demande de fonds pour « urgence familiale » ou « problème médical ». Moins de prétention investissement, plus d’émotionnel.

**Faux investissement plateformes**. Plateforme prétendant être trading bot, AI investment, DeFi proprietary. Captures truquées de gains.

**Faux investissement « insider »**. Le scammer prétend avoir un « tip » d’initié sur une crypto qui va exploser. Transfert vers « sa » plateforme.

**Faux investissement pyramidal**. Combinaison schéma de Ponzi et scam — les premiers déposants peuvent retirer (avec fonds des suivants) jusqu’à effondrement.

**Job scam**. Variation : la victime est « recrutée » pour faire du « trading test », doit déposer pour qualifier, puis bloquée.

#### 25.9 Tendances 2024-2026

**Augmentation explosive** depuis 2022.

**IA dans le scam** :

- Génération d’images de profil par IA (StyleGAN, Stable Diffusion, etc.).
- Voice cloning pour appels téléphoniques crédibles.
- Chatbots IA pour gérer multiples victimes simultanément.
- Multi-langue automatique pour cibler globalement.

**Blanchiment via stablecoins** dominant.

**Sophistication accrue** des plateformes frauduleuses (UI proche d’exchanges légitimes).

**Pour l’enquêteur** : la **typologie évolue**. Les patterns 2026 incluent IA et stablecoins multi-chaînes. La méthodologie de base reste mais s’adapte.

-----

### Chapitre 26 — Ransomware et extorsion

Le ransomware est l’un des plus gros postes médiatisés de cybercriminalité. Pour l’enquêteur crypto, c’est aussi un **flux structuré et reconnaissable**, particulièrement adapté à l’analyse on-chain.

#### 26.1 Le modèle économique

**Acteurs** :

- **Opérateurs / développeurs** : fournissent malware + infrastructure (leak site, portail négociation).
- **Affiliés** : exécutent les attaques, prennent typiquement 70-80% des rançons.
- **Initial Access Brokers (IAB)** : vendent les accès initiaux aux affiliés.
- **Négociateurs** : négocient avec les victimes côté criminel.
- **Services de blanchiment** : prennent en charge les flux post-paiement.

**Flux financier typique** :

1. Victime paie en crypto (BTC dominant, parfois XMR pour Monero-only).
1. Adresse de réception dédiée à la victime.
1. Mouvement post-paiement : peeling chain ou consolidation rapide.
1. Conversion potentielle (vers stablecoins, autres chaînes).
1. Anonymisation : mixers, bridges, swaps.
1. Cashout : exchanges non-KYC, P2P, OTC.

#### 26.2 Le paiement

**Formats** :

- **Adresse fournie via portail Tor** : opérateurs maintiennent portails de négociation .onion, victime y accède pour négocier et obtenir l’adresse.
- **Adresse dans note de rançon** : moins courant pour gros opérateurs (préfèrent négociation), plus fréquent pour ransomware moins ciblé.
- **Email avec adresse** : sextortion et ransomware basique.

**Délai de paiement** : typiquement 7-14 jours négociés. Au-delà, leak site publication ou augmentation de la demande.

**Adresses fraîches dédiées**. La pratique standard est : **une adresse par victime**, fraîche, jamais utilisée. Évite que d’autres victimes (ou des observateurs) voient les paiements totaux.

#### 26.3 Reconnaître un cluster ransomware

**Signaux d’une adresse ransomware** :

**Réception unique de gros montant**. Adresse fraîche reçoit un montant rond ou semi-rond (35 BTC, 50 BTC, 100 BTC…) en une seule transaction.

**Mouvement rapide post-paiement**. Le délai entre réception et premier mouvement est souvent court (heures à 1-2 jours).

**Pattern de blanchiment standardisé**. Peeling chain, consolidation, conversions. Les opérateurs établis ont des patterns reconnaissables.

**Multiple paiements pour le même opérateur**. Sur les outils pro, les clusters ransomware sont identifiés (« cluster Akira », « cluster LockBit », « cluster Black Basta »). Les nouvelles adresses sont assignées au cluster sur la base d’heuristiques + labels propriétaires.

#### 26.4 Cluster opérateur vs cluster affilié

Distinction importante.

**Cluster opérateur** : infrastructure de l’opérateur (développeurs du ransomware). Reçoit la part de l’opérateur (~20-30% des rançons). Stable dans le temps.

**Cluster affilié** : infrastructure des affiliés. Reçoit la part de l’affilié (~70-80%). Multiple affiliés par opérateur, chacun avec ses patterns.

**Pour l’enquêteur** : identifier si l’enquête remonte vers opérateur ou affilié change la lecture. Affilié = un acteur parmi N. Opérateur = peut révéler infrastructure plus large.

#### 26.5 Méthode d’enquête

**Étape 1 — Indices initiaux**. Adresse de paiement (du portail négociation, de la note ransomware, ou de la victime).

**Étape 2 — Validation**. TXID confirmant le paiement. Lecture sur Mempool.

**Étape 3 — Identification du cluster**. Outils pro identifient le cluster. Parfois directement attribué à un groupe ransomware.

**Étape 4 — Suivi des flux**. Comme MIXSHADOW : peeling chain, conversions, etc.

**Étape 5 — Identification des points de coopération**. Exchanges traversés, mixers, bridges.

**Étape 6 — Caractérisation du groupe**. Patterns, infrastructure, leak site, victimologie.

**Étape 7 — Rapport et coopération**.

#### 26.6 Coopération avec les autorités

**FBI Cyber Division** (US) : référence pour ransomware. Multiple opérations (saisie Bitfinex, opération Cronos contre LockBit, etc.).

**NCA (UK)** : équivalent.

**Europol EC3** : coordination EU.

**ANSSI / DGSI / TRACFIN** (France) : pour victimes françaises.

**BKA (Allemagne)**.

**Coopération exchanges** : nombreux exchanges réguliers gèlent fonds tracés à ransomware sur réquisition.

**Coopération émetteurs stablecoins** : Tether et Circle ont gelé à plusieurs reprises des fonds de groupes ransomware.

#### 26.7 Le débat « payer ou pas »

**Position officielle (US, France, UK)** : **déconseiller le paiement**. Arguments :

- Finance la criminalité.
- Ne garantit pas le déchiffrement.
- Crée incitation pour autres attaques.
- Peut violer sanctions OFAC (si groupe sanctionné).

**Réalité** : la décision relève de la victime, sous pression vitale (cf MIXSHADOW). Pas de critère universel.

**Pour l’enquêteur** : pas de jugement moral. Si paiement, l’enquête maximize la valeur (récupération potentielle, attribution, contribution sectorielle).

#### 26.8 Tendances 2024-2026

**Multi-extorsion** : chiffrement + exfiltration + chantage clients + DDoS. Rançons plus élevées.

**Dual ransomware** : double chiffrement par deux groupes différents (rare mais documenté).

**Ciblage de la santé et OIV** : croissance.

**Sanctions et démantèlements** : LockBit (Operation Cronos février 2024), AlphaV/BlackCat, Hive (saisie 2023). Écosystème en mutation continue.

**Akira, Black Basta, Play, LockBit (relaunch), Medusa** : groupes actifs 2025-2026.

**Pour l’enquêteur** : la **typologie ransomware est pleine d’enjeux** mais aussi de **success stories** (Bitfinex saisie 3,6 Mrd, Colonial Pipeline récupération 2,3 M, opérations Cronos). L’enquête contribue.

-----

### Chapitre 27 — Hacks DeFi et compromission de wallets

Les hacks DeFi et compromissions de wallets représentent des **milliards USD/an** depuis 2021 selon Chainalysis. Différent du ransomware (où victime paie volontairement) — ici, fonds sont **volés** sans consentement.

#### 27.1 Hacks de protocoles DeFi

**Vecteurs typiques** :

**Vulnérabilités de smart contracts**. Bug dans le code (re-entrancy, overflow, logique faillible). Permet à attaquant de drainer le protocole.

**Compromission de clés admin**. Si un protocole DeFi a des fonctions admin (upgrade, pause, mint), compromission de la clé admin = takeover total.

**Oracles attaques**. Manipulation des oracles de prix utilisés par le protocole. Permet de profiter des conditions favorables artificielles.

**Flash loan attacks**. Combinaison de flash loans (prêts non-collatéralisés sur 1 transaction) avec exploitation de vulnérabilités. Permet à attaquant sans capital initial de drainer un protocole.

**Bridge exploits**. Bridges cross-chain sont particulièrement vulnérables (combinaison de smart contracts complexes et de validateurs externes). Cf Ronin (Ch.43), Wormhole (2022, 326 M USD), Nomad (2022, 190 M USD), Multichain (2023, 130 M USD).

**Cas marquants** :

- **Ronin Network** (mars 2022, 625 M USD) — Lazarus / DPRK.
- **Wormhole** (février 2022, 326 M USD) — restitution partielle suite à exploit reverse.
- **Nomad** (août 2022, 190 M USD) — exploitation chaotique multi-acteurs.
- **Mango Markets** (octobre 2022, 117 M USD) — Avraham Eisenberg, condamné aux US.
- **Curve Finance** (juillet 2023, 70 M USD).
- **Mixin Network** (septembre 2023, 200 M USD).
- **Multiple en 2024-2026** : pertes cumulées en milliards.

**Bilan annuel** : Chainalysis 2024 indique des fonds volés dans crypto en hausse, atteignant des chiffres records. Mid-year update 2025 confirme la tendance.

#### 27.2 Compromission de wallets utilisateurs

**Vecteurs** :

**Stealer logs**. Malware (Lumma, RedLine, Vidar, etc.) qui vole credentials, cookies, seed phrases stockées localement. Cf cours Dark Web.

**Phishing de seed phrase**. Sites imitant wallet officiel demandant seed phrase « pour vérification ».

**Compromission email + reset MFA**. Reset password exchange / SMS swap / SIM swap.

**Approval phishing / drainers** (Ch.9). Site faux qui fait signer approval, drainer vide le wallet.

**Compromission physique**. Vol de hardware wallet, contraintes physiques. Plus rare.

**Bilan** : Chainalysis 2024-2025 souligne **augmentation forte** des fonds volés via compromission de wallets personnels. Particulièrement pour adresses high-value (whale wallets).

#### 27.3 Reconnaître un hack vs vol vs scam

**Hack DeFi** :

- Exploit technique d’un protocole.
- Smart contract vidé.
- Souvent montant élevé (millions à centaines de millions USD).
- Communauté DeFi alertée immédiatement (twitter, dashboards).

**Compromission wallet individuel** :

- Wallet personnel vidé.
- Drainer ou transfert direct.
- Montants variables (quelques USD à millions USD).
- Souvent identifié par victime via alerte mouvement inattendu.

**Scam** (rug pull, fake token, etc.) :

- Investisseurs ont **volontairement** investi.
- Token déprécié à zéro après dump du créateur (rug pull).
- Différent du hack — pas de vulnérabilité exploitée techniquement, mais escroquerie sur l’intention.

L’enquête diffère selon catégorie.

#### 27.4 Méthode d’enquête : hack DeFi

**Étape 1 — Détection / annonce**. Souvent annoncé immédiatement par victime ou observers (Twitter/X, Rekt News, Defi Watch).

**Étape 2 — Identification de la transaction d’exploit**. Le hash de la transaction où l’exploit s’est produit est public (sinon on cherche dans les transactions du protocole).

**Étape 3 — Lecture de la transaction**. Sur Etherscan / Phalcon / Tenderly :

- Comprendre la **logique exploit**.
- Identifier les **smart contracts** appelés.
- Identifier les **adresses attaquant**.

**Étape 4 — Suivi des fonds volés**. Méthode standard. Souvent les attaquants utilisent immédiatement Tornado Cash, bridges, ou d’autres techniques d’obfuscation.

**Étape 5 — Identification de l’attaquant**. Si trace publique (white hat hack annoncé), identification facile. Si exploit anonyme, attribution probable via patterns.

**Étape 6 — Coopération avec protocole victime et exchanges**. Souvent demande de gel à exchanges si fonds y atterrissent. Bounty du protocole pour incitation à restitution.

**Étape 7 — Rapport et action**.

#### 27.5 Méthode d’enquête : compromission wallet

**Étape 1 — Indices initiaux**. La victime fournit son adresse, le timestamp du drainage, et idéalement des informations sur le vecteur (« j’ai cliqué sur ce lien… », « je crois que mon ordinateur a un virus… »).

**Étape 2 — Lecture des transactions de drainage**. Sur Etherscan, les **dernières transactions** du wallet de la victime montrent où sont allés les fonds.

**Étape 3 — Identification du drainer**. Si pattern approval phishing : voir les transactions d’`approve` précédentes. Identifier le smart contract du drainer.

**Étape 4 — Suivi des fonds drainés**. Le drainer consolide vers son propre wallet, qui ensuite blanchit.

**Étape 5 — Identification du drainer service**. Beaucoup de drainers sont **services-as-a-service** (Inferno Drainer, Pink Drainer historiquement, autres en 2024-2026). Identification du service permet attribution macro.

**Étape 6 — Coopération**. Si fonds vers exchange régulé : demande de gel.

#### 27.6 Limites

**Récupération**. Variable. Hacks DeFi : parfois récupération via négociation (white hat reward) ou pression. Compromissions individuelles : récupération rare.

**Attribution**. Hacks sophistiqués (Lazarus) : attribution publique parfois. Drainers individuels : souvent anonymes.

**Vitesse**. Les hackers sont rapides. Les premières heures sont critiques. Si l’enquête ne démarre pas dans la journée, fonds souvent déjà out.

#### 27.7 Tendances 2024-2026

**Hacks DeFi** : continuent à grand échelle. Bridges restent ciblés.

**Drainer-as-a-service** : démocratisation des drainers, baisse de la barrière technique.

**Lazarus** : continue à dominer les hacks majeurs. ~Mrd USD/an attribués.

**Compromission de wallets via stealer logs** : croissance massive.

**Retraits forcés via violence physique** : émergent (« 5 dollar wrench attacks », attaques contre des holders identifiés).

-----

### Chapitre 28 — Fraudes NFT, tokens frauduleux et rug pulls

L’écosystème NFT et tokens connaît une **forte sinistralité fraude**. Différentes typologies, chacune avec ses patterns.

#### 28.1 Rug pulls

**Schéma** :

1. Création d’un token (ERC-20, BEP-20, SPL, etc.).
1. Marketing intense (Twitter, Discord, Telegram, parfois influenceurs).
1. Liquidité ajoutée sur DEX (paire token/ETH ou token/USDT).
1. Investisseurs achètent.
1. Au pic, **les créateurs vident la liquidité** (« pull the rug »).
1. Token à zéro, investisseurs perdent tout.

**Variantes** :

- **Soft rug** : créateurs disparaissent silencieusement, abandon du projet.
- **Hard rug** : drain explicite de la liquidité.
- **Honeypot** : token codé pour empêcher acheteurs de revendre (techniquement plus subtil).

**Reconnaissance** :

- Tokens nouveaux sans audit.
- Concentration de l’offre dans quelques wallets (owner garde 50%+).
- Liquidité non « locked ».
- Communauté artificielle (bots).

#### 28.2 Honeypot tokens

**Mécanisme** : le smart contract du token contient une fonction cachée qui empêche les acheteurs (sauf le créateur) de revendre. Investisseurs achètent, **ne peuvent jamais sortir**.

**Détection** : analyse du code Solidity. Fonctions avec conditions cachées sur `transfer`. Outils comme Token Sniffer, GoPlus automatisent.

#### 28.3 Pump-and-dump

**Schéma** :

1. Création / sélection d’un token de faible capitalisation.
1. Coordination dans groupes Telegram / Discord (« pump signal »).
1. Achats coordonnés synchronisés.
1. Cours du token explose (multiplication 5-50x).
1. Insiders / leaders **dumpent** au pic.
1. Cours s’effondre, late-comers perdent.

Sur Solana 2024-2026, l’écosystème **memecoin** (pump.fun et associés) industrialise ce schéma à échelle massive.

#### 28.4 Fraude NFT

**Faux mint**. Site phishing imitant un drop NFT légitime. Demande approval qui draine wallet.

**Faux marketplace**. Plateforme imitant OpenSea/Blur, avec listings frauduleux ou drainer.

**Wash trading**. Achats / ventes d’NFT entre wallets contrôlés par même entité, pour gonfler artificiellement le « volume » et tromper acheteurs.

**Fake collections**. Collections imitant collections célèbres (CryptoPunks, BAYC) avec léger changement de nom ou logo.

**Fake floor**. Listings à très bas prix (faux) pour attirer attention sur une collection.

**Phishing Discord**. Hack de Discord officiel d’un projet NFT, annonce de mint frauduleux qui draine wallets.

#### 28.5 Méthode d’enquête : rug pull

**Étape 1 — Indices**. Token contracté, plainte d’investisseurs.

**Étape 2 — Analyse du contrat**. Lecture Solidity (si vérifié) ou bytecode. Identification de fonctions backdoor.

**Étape 3 — Identification des wallets créateurs**. Adresse de déploiement du contrat. Premiers holders. Adresses ayant ajouté la liquidité initiale.

**Étape 4 — Analyse des mouvements**. Quand les créateurs ont-ils dump ? Vers où ?

**Étape 5 — Suivi des fonds**. Standard.

**Étape 6 — Identification des créateurs**. Si OPSEC faible (réutilisation d’adresses, déposit sur exchange KYC), attribution possible.

#### 28.6 Méthode d’enquête : phishing NFT

**Étape 1 — Indices**. Victime fournit transaction de drain.

**Étape 2 — Identification du drainer**. Smart contract appelé. Souvent service connu (drainer-as-a-service).

**Étape 3 — Suivi des fonds**. Standard.

#### 28.7 Limites

**Volume massif**. Trop de rug pulls / scams pour tous les enquêter individuellement. Triage obligatoire (impact, victimes notables).

**Anonymat des créateurs**. Souvent OPSEC stricte (création depuis wallets fonds Tornado Cash, etc.).

**Aspects civils vs pénaux**. Beaucoup de rug pulls relèvent de **fraude civile** plus que pénale (selon juridiction, intentionnalité difficile à prouver).

#### 28.8 Tendances 2024-2026

**Memecoin scams** : explosion via pump.fun et écosystème Solana.

**AI-generated NFT scams** : NFT générés en masse pour rug pull.

**Cross-chain rug pulls** : exploitation de bridges et confusion multi-chaîne.

-----

### Chapitre 29 — Acteurs étatiques : Lazarus et contournement de sanctions

Les acteurs étatiques sophistiqués utilisent le crypto à grande échelle. **Lazarus** (DPRK / Corée du Nord) est l’archétype documenté. Les opérations de contournement de sanctions (Russie post-2022, Iran) sont également structurantes.

#### 29.1 Le profil Lazarus

**Lazarus Group** (alias APT38, alias Hidden Cobra). Cluster d’acteurs DPRK opérant sous direction du Bureau 121 / Reconnaissance General Bureau (RGB).

**Évolution** :

- 2014-2016 : ciblage banques traditionnelles (SWIFT). Heist Bangladesh Bank 2016 : 81 M USD.
- 2017+ : pivot massif vers crypto. Cible exchanges, particuliers, DeFi.
- 2022+ : domination des plus gros vols crypto annuels.

**Cas marquants attribués** :

- **Ronin Network** (mars 2022, 625 M USD).
- **Harmony Bridge** (juin 2022, 100 M USD).
- **Atomic Wallet** (juin 2023, 100 M USD).
- **CoinEx** (septembre 2023, 54 M USD).
- **Stake.com** (septembre 2023, 41 M USD).
- **Multiple incidents** 2024-2025.

Estimations cumulées : **plusieurs milliards USD** volés depuis 2017. Selon TRM Labs et Chainalysis, Lazarus est l’acteur étatique le plus prolifique en crypto.

**Usage des fonds** : finance les programmes étatiques DPRK, contourne les sanctions internationales.

#### 29.2 TTP Lazarus crypto

**Vecteurs d’accès** :

- Phishing sophistiqué (fake recruiters, fake job offers — « Operation Dream Job »).
- Compromission d’employés clés d’exchanges et protocoles.
- Vulnérabilités de smart contracts.
- Compromission d’infrastructure (nodes, relayers).

**Patterns de blanchiment** :

- **Tornado Cash** historiquement (avant sanctions août 2022, après aussi).
- **Bridges cross-chain** intensifs.
- **CoinJoin** Bitcoin.
- **Conversion en privacy coins** (Monero) parfois.
- **Off-ramp via OTC asiatiques** (Russie, Asie centrale).
- **Réseau de mules** pour cashout.

**Sophistication opérationnelle** : OPSEC souvent élevée. Wallets fraîs, infrastructure rotative, blanchiment méticuleusement structuré.

#### 29.3 Reconnaître un cluster Lazarus

**Indicators** (selon TRM, Chainalysis, FBI) :

- Adresses précédemment attribuées à Lazarus dans les bases vendor.
- Patterns de blanchiment cohérents avec doctrine Lazarus.
- TTP de compromise compatibles.
- Liens infrastructure (mêmes serveurs, même malware family).

**Important** : Lazarus n’est **pas** la seule explanation pour des patterns sophistiqués. Sur-attribution est piège. Validation requise.

#### 29.4 Sanctions et coopération

**OFAC** :

- A sanctionné de multiples wallets Lazarus.
- Sanction Tornado Cash (août 2022) cite Lazarus comme une des raisons.
- Mises à jour régulières.

**FBI** : très actif sur ransomware DPRK et Lazarus. Multiple advisory et identifications publiques.

**Coopération internationale** : tendue (DPRK n’est pas coopératif), mais pression des US/UE/Japon/Corée du Sud sur exchanges et points de cashout.

#### 29.5 Russie et contournement de sanctions

Depuis 2022, contournement de sanctions Russie via crypto est documenté.

**Acteurs** :

- Particuliers russes contournant restrictions financières.
- Exchanges russes / liés (Garantex, sanctionné OFAC).
- Acteurs étatiques utilisant crypto pour transactions internationales.

**Outils** :

- Stablecoins (USDT-TRON dominant).
- P2P trading (LocalBitcoins historiquement, Binance P2P, autres).
- OTC desks dans juridictions permissives.

**Pour l’enquêteur** : flux Russie-related identifiables par patterns. Coopération avec exchanges pour gel possible (USDT-Tether a gelé multiples adresses Russie sur réquisition).

#### 29.6 Iran et autres

**Iran** : usage crypto pour contourner sanctions, financer programmes étatiques. Cluster acteurs étatiques iraniens (« Pioneer Kitten », « APT34 », autres) avec activité crypto.

**Autres acteurs étatiques** : Chine (moins dans crypto direct, plus dans surveillance et minage), pays émergents avec capacité cyber moindre.

#### 29.7 Méthode d’enquête : acteurs étatiques

**Étape 1 — Hypothèse étatique**. Patterns sophistiqués + indicateurs ne signifient **pas automatiquement** acteur étatique. Validation requise.

**Étape 2 — Recoupement avec bases vendor**. Chainalysis, TRM, Elliptic ont des labels « Lazarus », « Iran-related », etc. avec des niveaux de confiance.

**Étape 3 — Recoupement avec sources publiques**. OFAC SDN, FBI advisory, Mandiant / CrowdStrike threat reports.

**Étape 4 — Analyse TTP**. Patterns techniques (vecteurs, infrastructure, malware) si applicables.

**Étape 5 — Coopération**. Impossible directement (les acteurs sont étatiques). Coopération via FBI / Europol / autorités équivalentes pour suivre les flux et identifier points d’action (exchanges traversés, cashout).

**Étape 6 — Rapport et calibration**. Attribution étatique nécessite calibration prudente (cf Ch.18). Rarement « certain » sans accès renseignement classifié.

#### 29.8 Limites

**Attribution civile impossible**. L’identification des opérateurs individuels au sein de Lazarus est réservée aux services de renseignement. OSINT identifie les **clusters** et **patterns**, pas les **individus**.

**Coopération minimale avec juridictions sanctuaires**. DPRK, Russie, Iran ne coopèrent pas. Action via points externes (exchanges, services, transit).

**Récupération limitée**. Quelques cas (Bitfinex saisie 3,6 Mrd, autres opérations FBI), mais dans l’ensemble, fonds Lazarus difficiles à récupérer.

#### 29.9 Tendances 2024-2026

**Lazarus en croissance**. Vols cumulés en milliards USD/an.

**Sophistication croissante**. Usage de tous les outils d’obfuscation (mixers post-Tornado, bridges, privacy coins, réseaux de mules complexes).

**Coopération internationale renforcée**. Mais lente et fragmentée.

**Sanctions ciblées** : OFAC continue d’ajouter wallets et entités. UE suit progressivement.

**Pour l’analyste** : les acteurs étatiques sont **angle stratégique** pour les services de renseignement et CTI privé senior. Pour l’analyste défensif d’organisation, les détecter dans son périmètre = **alerte rouge** justifiant escalade immédiate (ANSSI, DGSI selon contexte).

-----

## PARTIE VI — OBFUSCATION, LAUNDERING ET CASHOUT

> **Ce que cette partie apprend.** Comprendre les techniques d’obfuscation utilisées par les acteurs criminels pour casser la traçabilité on-chain. Mixers et tumblers, CoinJoin, bridges cross-chain, DEX et swaps, privacy coins. Pour chaque technique : fonctionnement, ce qui reste observable, ce qui devient opaque, et signaux exploitables.
> 
> **Ce qu’elle ne couvre pas.** Les cas pratiques déroulés (Partie VII), les cas historiques (Partie VIII), la production de rapport (Partie IX).
> 
> **Ce que vous saurez faire après cette partie.** Reconnaître chaque technique d’obfuscation à sa signature on-chain. Évaluer ce qui reste analysable malgré l’obfuscation. Calibrer la confiance dans les conclusions face à des techniques mixtes. Identifier les opportunités défensives (gel d’actifs, coopération exchanges).

-----

### Chapitre 30 — Le cashout : où l’on quitte l’on-chain

Le **cashout** est le moment où les fonds quittent la blockchain pour entrer dans le monde fiat (ou être consommés sous forme de biens/services). C’est **le maillon le plus important** pour l’enquêteur et le plus vulnérable pour le criminel.

#### 30.1 Pourquoi le cashout est central

**Pour le criminel** : le crypto en lui-même est rarement « utile ». Pour acheter une voiture, payer un loyer, financer une opération, il faut **convertir** en monnaie utilisable.

**Pour l’enquêteur** : le cashout est où le KYC entre en jeu. Les exchanges régulés exigent identification. Le moment du cashout est souvent **le seul** où on peut relier une adresse blockchain à une identité civile.

**Stratégique** : si l’enquête identifie le cashout, elle a identifié **l’angle d’attaque** des autorités — réquisition pour KYC, gel de fonds, identification.

#### 30.2 Les méthodes de cashout

**Exchange centralisé régulé (CEX KYC)**. La méthode standard mais risquée pour le criminel.

- Avantages criminels : volume élevé, facilité, multi-paires.
- Inconvénients : KYC obligatoire, monitoring AML, possibilité de gel.

**Exchange centralisé non-KYC ou faible KYC**. Plateformes dans juridictions permissives. KYC inexistant ou contournable.

- Cas connus : multiple petits exchanges (souvent peu durables, fermés / sanctionnés).
- Garantex (sanctionné OFAC 2022). Bitzlato (sanctionné 2023). Suex (sanctionné 2021). Successeurs émergent et sont sanctionnés à leur tour.

**OTC desks (Over-The-Counter)**. Brokers qui matchent acheteurs / vendeurs hors orderbook public.

- Régulés (intégrés à exchanges) : KYC requis.
- Non-régulés : permissif, populaire pour gros montants.
- Spread (différence d’achat/vente) plus élevé pour montants importants.

**P2P (peer-to-peer) trading**. Plateformes où particuliers échangent crypto/fiat directement.

- **Binance P2P** : marché P2P intégré à Binance, KYC requis pour comptes.
- **HodlHodl, AgoraDesk** : alternatives sans KYC.
- **LocalCoinSwap, autres** : variantes.
- Permet conversion en monnaie locale par virement bancaire entre individus.

**ATM crypto (BTM)**. Distributeurs Bitcoin permettant achat / vente cash. Présents dans plusieurs pays. KYC variable selon machine et juridiction. Limites de montant.

**Cartes prepaid crypto**. Crypto debit cards (Wirex, Crypto.com, autres). Permettent conversion progressive crypto vers achats en ligne / retraits ATM.

**Achats directs** :

- Immobilier (dans juridictions permissives — quelques pays acceptent crypto pour transactions immobilières).
- Voitures, luxe (cars, montres, art).
- Or et métaux précieux.

**Mules / muleware**. Réseaux de personnes (souvent recrutées en ligne) qui reçoivent fonds crypto et convertissent / transfèrent. Communs dans pig butchering et fraudes massives.

**Gambling**. Casinos crypto (Stake, Bitcasino, autres). Permettent conversion via dépôt crypto + retrait fiat ou autres crypto. Moins efficace mais pratiqué.

**Gift cards / vouchers**. Achats de gift cards Amazon, Apple, Walmart payés en crypto. Revente sur marchés secondaires.

**Conversion sur DEX puis off-ramp ailleurs**. DEX permet swap entre cryptos sans KYC. Mais final off-ramp en fiat nécessite quand même un point centralisé quelque part.

#### 30.3 Reconnaître les patterns de cashout

**Signaux d’un dépôt sur exchange régulé** :

- Adresse destinatrice labellisée par outils pro.
- Montant cohérent avec dépôt utilisateur (quelques centaines à milliers USD typiquement, parfois plus).
- Pattern de dépôt unique (l’adresse de dépôt utilisateur reçoit, le hot wallet exchange centralise).

**Signaux d’OTC ou P2P** :

- Transferts vers wallets « privés » (pas exchange).
- Patterns « hub » : adresse recevant multiples dépôts et redistributant en montants équivalents (broker P2P matchant trades).

**Signaux de cards crypto** :

- Conversion progressive en stablecoins (USDC notamment, intégré aux cartes).
- Petits transferts réguliers vers wallets de cards providers.

#### 30.4 Coopération avec les exchanges

**Exchanges régulés** :

- Procédures d’investigation établies.
- Coopèrent avec autorités sur réquisition (USA, EU, UK, autres juridictions).
- Capacité de **gel** des comptes utilisateurs et **fourniture de KYC**.
- Délais variables (heures à semaines).

**Exchanges non-KYC ou peu coopérants** :

- Souvent dans juridictions permissives.
- Coopération difficile.
- Action possible via sanctions (OFAC) ou pressions juridictionnelles.

**Pour l’enquêteur** : identifier l’exchange traversé est **étape critique**. Permet d’orienter l’action des autorités. Sarah Marin dans MIXSHADOW a identifié plusieurs exchanges à risque traversés par les fonds Akira ; cette information est transmise à la DGSI pour évaluation de coopération.

#### 30.5 Mules et réseaux de cashout

**Mules** : individus utilisés pour recevoir / convertir des fonds illicites.

**Mode de recrutement** :

- Annonces fausses « gagnez de l’argent en travaillant à domicile ».
- Romance scam (la mule est elle-même victime).
- Recrutement direct via Telegram / forums.
- Coercition / trafic humain (cas extrêmes, pig butchering compounds).

**Implications** :

- La mule peut être identifiée KYC sur exchange, mais l’**enquête remonte à la mule**, pas au cerveau.
- Coopération de la mule (si pas complice consciente) peut donner indications sur les commanditaires.

#### 30.6 Limites OSINT au cashout

**Le KYC est off-chain**. L’analyste OSINT identifie l’adresse de dépôt exchange, mais **ne peut pas** accéder aux données KYC sans réquisition légale.

**Identification finale = autorités**. OSINT prépare le terrain (« cette adresse a déposé chez exchange X »), autorités opèrent la requête.

**Délais**. Entre identification du cashout et obtention du KYC, plusieurs semaines/mois peuvent passer. Pendant ce temps, les fonds peuvent avoir été déjà retirés.

**Multi-juridiction**. Réquisitions internationales sont lentes. Coopération variable selon juridiction.

#### 30.7 Le cashout comme point d’attention défensif

Pour défense :

**Monitoring de cashout**. Pour fonds tracés à des activités illicites, alerter dès que mouvement vers exchange régulé connu = opportunité de gel.

**Coopération sectorielle**. Exchanges qui partagent informations (FATF Travel Rule, ISACs financiers) accroissent capacité collective.

**AML automation**. Outils intégrés (Chainalysis KYT, TRM, Elliptic Discovery) permettent screening en temps réel des dépôts.

#### 30.8 Le message à intérioriser

> Le cashout est souvent le moment le plus intéressant pour l’enquête, mais aussi celui où l’OSINT atteint ses limites sans coopération d’un VASP ou réquisition.

L’OSINT identifie. Les autorités agissent. La coopération entre les deux est le multiplicateur de capacité.

#### 30.9 Fil rouge — MIXSHADOW : les cashouts identifiés

> **🔗 MIXSHADOW — Épisode 17 : points de cashout**
> 
> À 6 semaines de mission, Sarah a identifié les **points de cashout** des fonds Akira issus du paiement Aurélien Médical :
> 
> **Exchange régulé via dépôts identifiables** :
> 
> - **3 dépôts sur Binance** : ~80 000 USDT cumulés. Adresses de dépôt identifiables, KYC potentiel via réquisition.
> - **2 dépôts sur Kraken** : ~25 000 USDT. Idem.
> - **1 dépôt sur Coinbase** : ~12 000 USDT. Idem.
> 
> **Exchange non-KYC** :
> 
> - **Exchange non-KYC X** : ~150 000 USDT cumulés transités. Pas d’angle KYC. Sanctions OFAC sur cet exchange demandées par l’enquête (alimente dossier).
> 
> **OTC / P2P (probable)** :
> 
> - **2 hubs TRON** identifiés (cf Ch.13). Probable services de blanchiment (broker P2P / OTC). Pas d’angle KYC direct, mais alimentation profil pour traque future.
> 
> **Cartes prepaid (suspecté)** :
> 
> - Quelques flux résiduels semblent transiter par des wallets compatibles avec providers de cartes prepaid crypto. Volume modéré (~30 000 USDT). Investigation continue.
> 
> **Non identifiés / dispersion** :
> 
> - **~50 000 USDT** dans un layering profond TRON, destination finale non encore caractérisée à 6 semaines.
> 
> **Bilan** :
> 
> - **~120 000 USDT** identifiés sur exchanges régulés (Binance / Kraken / Coinbase) — **angle KYC fort**, transmission DGSI pour coordination réquisition.
> - **~150 000 USDT** sur exchange non-KYC X — angle sanctions / coordination internationale.
> - **~80 000 USDT** dispersés / non identifiés pour le moment.
> 
> Sarah note dans le rapport intermédiaire : **120 000 USDT sur exchanges régulés** = potentiel **angle de récupération partielle** via gel et identification. Si les exchanges identifient les comptes (probable, dépôts récents) et coopèrent rapidement, une partie peut être gelée. La DGSI prend en charge la coordination.
> 
> 6 semaines plus tard (semaine finale), retour : **~45 000 USDT effectivement gelés** sur Binance et Kraken (3 comptes mules identifiés), KYC fournis aux autorités. Dossiers transmis à FBI Cyber Division pour enquête sur les mules. Récupération définitive des fonds dépend de la procédure judiciaire ultérieure.
> 
> 45 000 USDT sur 2 M EUR initial = **~2,3% récupération nominale**, mais **valeur de renseignement** beaucoup plus large : 3 mules identifiées, alimentent dossier multi-juridictionnel sur réseau Akira.

-----

### Chapitre 31 — Mixers et tumblers

Les **mixers** (ou tumblers) sont des services qui mélangent les fonds de multiples utilisateurs pour casser la traçabilité. Ils existent depuis les premiers jours du Bitcoin. Plusieurs ont été démantelés ; d’autres continuent. Ce chapitre couvre leur fonctionnement et limites de l’analyse.

#### 31.1 Qu’est-ce qu’un mixer

**Principe** : un mixer reçoit les fonds d’utilisateur A et lui restitue, après délai, des fonds **différents** (issus d’autres utilisateurs B, C, D, etc.) à une adresse de destination différente.

**Effet** : casser le lien direct entre origine des fonds et destination. Si A a déposé 1 BTC entaché et reçoit 1 BTC « propre » (anciennement détenu par B), le lien on-chain entre origine et destination est rompu.

**Types** :

- **Mixers custodial** : service centralisé qui détient les fonds pendant le mélange. Tornado Cash (originellement), Helix, Bitcoin Fog, Chipmixer, Samourai Whirlpool partiellement.
- **CoinJoin (peer-to-peer, non-custodial)** : protocole coopératif sans custodian central. Wasabi, Samourai. Cf Ch.32.

**Différence** :

- Custodial : confiance dans l’opérateur (qui peut voler les fonds).
- Non-custodial : pas de risque de vol, mais moins « profond » comme mélange.

#### 31.2 Fonctionnement d’un mixer custodial classique

Schéma type (mixer historique type Helix, Bitcoin Fog) :

**Étape 1 — Dépôt**. Utilisateur envoie ses BTC à une adresse fournie par le mixer.

**Étape 2 — Pool**. Les fonds sont agrégés dans un pool central.

**Étape 3 — Délai**. Le mixer attend un délai variable (heures à jours) pour que d’autres dépôts arrivent.

**Étape 4 — Restitution**. Le mixer envoie à l’utilisateur, depuis le pool, des BTC issus d’autres dépôts. Souvent via plusieurs petites transactions vers adresses fournies par l’utilisateur.

**Étape 5 — Fees**. Le mixer prélève une commission (1-5% typiquement).

**Failles** :

- **Confiance** : l’opérateur peut voler.
- **Logs internes** : si saisi, les logs peuvent dé-mixer (cf saisie Helix, Bitcoin Fog, Chipmixer).
- **Patterns observables** : timing, montants, adresses peuvent permettre des inférences statistiques.

#### 31.3 Tornado Cash : le mixer décentralisé

**Tornado Cash** (lancé août 2019) est un mixer **non-custodial** sur Ethereum, basé sur **zero-knowledge proofs**. Référence du genre.

**Fonctionnement** :

**Pool fixe** : Tornado opère par pools de montants fixes (0,1 ETH, 1 ETH, 10 ETH, 100 ETH).

**Dépôt** :

- Utilisateur génère un **secret** (note) localement.
- Calcule le **hash du secret** (commitment).
- Appelle `deposit(commitment)` sur le smart contract pool, en envoyant le montant fixe.
- Smart contract enregistre le commitment dans un Merkle tree.

**Délai** : utilisateur attend (recommandation : plusieurs jours à semaines pour maximiser anonymat).

**Retrait** :

- Utilisateur génère un **proof zero-knowledge** prouvant qu’il connaît le secret correspondant à un commitment dans le Merkle tree, **sans révéler lequel**.
- Appelle `withdraw(proof, recipient)` sur le smart contract.
- Smart contract vérifie le proof, marque le commitment comme « spent », et envoie le montant fixe au `recipient`.

**Effet** : depuis l’extérieur, on voit que A a déposé (transaction publique) et que X a retiré (transaction publique), mais le **lien entre A et X** est cryptographiquement caché.

**Anonymity set** : le degré d’anonymat dépend du **nombre de dépôts non-retirés** dans la pool au moment du retrait. Plus la pool est utilisée, plus l’anonymat est fort.

#### 31.4 Sanctions OFAC sur Tornado Cash

**Août 2022** : OFAC sanctionne Tornado Cash. Justifications : usage massif par Lazarus et autres acteurs criminels, blanchiment de centaines de millions USD.

**Implications** :

- Adresses smart contracts Tornado sur SDN list.
- Interactions avec ces adresses depuis US persons = violation.
- Multiple plateformes (DEX, frontend wallets) ont retiré l’accès.
- Volume utilisateurs a chuté.

**Procès des développeurs** :

- **Alexey Pertsev** : développeur Tornado, arrêté Pays-Bas août 2022. **Condamné mai 2024** à 5 ans 4 mois prison pour blanchiment.
- **Roman Storm** : co-développeur, inculpé US août 2023. **Procès US 2024-2025** en cours, verdict attendu / partiellement rendu selon évolution.
- **Roman Semenov** : autre co-développeur, sanctionné OFAC 2023, en fuite.

**Débat** : développeurs de logiciel open source vs responsabilité légale. Tornado est code immutable, fonctionne sans intervention. Les développeurs ont écrit le code mais ne le contrôlent plus. Question juridique structurante.

#### 31.5 Analyse statistique des sorties Tornado

Bien que Tornado casse le lien direct, **analyse statistique** peut réduire l’incertitude.

**Techniques** :

**Timing analysis** :

- Si dépôt à T0 et retrait à T0 + 5 minutes, et que peu d’autres dépôts ont eu lieu entre, lien probable.
- Si retrait correspond exactement au timing typique d’un opérateur connu, indication.

**Montant matching** :

- Si total dépôts = total retraits dans une fenêtre temporelle, possibilité de pairing.
- Plus complexe si l’utilisateur dépose / retire des montants non-uniformes.

**Address reuse** :

- Si l’adresse de retrait apparaît dans d’autres contextes liés à l’opérateur, indication.

**Funding source du gas** :

- Le gas pour le retrait Tornado est payé. Si la source de gas est traçable, indication sur l’utilisateur.

**Behavioral patterns** :

- Comportement post-retrait peut matcher patterns connus.

**Limites** : ces techniques produisent **probabilités**, pas certitudes. Pour cas avec petite anonymity set (dépôts/retraits peu nombreux dans la pool), efficacité plus forte. Pour pool très active, efficacité faible.

#### 31.6 Mixers démantelés

**Helix** (saisi 2020) : opérateur Larry Harmon condamné, 11 M USD saisis.

**Bitcoin Fog** (saisi 2021) : opérateur Roman Sterlingov condamné en 2024.

**Chipmixer** (saisi mars 2023) : opération Allemagne / Belgique, 46 000 BTC (~2,7 Mrd EUR) saisis ou identifiés.

**Sinbad.io** (sanctionné OFAC novembre 2023) : successeur d’autres mixers démantelés.

**Samourai Wallet** (saisi avril 2024) : opérateurs Keonne Rodriguez et William Hill inculpés US.

**Pour l’enquêteur** : démantèlements créent **opportunités d’analyse** post-saisie. Logs récupérés permettent dé-mixage rétroactif. Multiple cas où des fonds ransomware historiques ont été tracés grâce à logs Helix / Bitcoin Fog post-saisie.

#### 31.7 Méthode d’enquête face à un mixer

**Étape 1 — Reconnaître le mixer**. Dépôts vers adresses connues de mixers (labels outils pro, listes publiques).

**Étape 2 — Documenter le dépôt**. Timestamp, montant, adresse source, identifiant du pool / mixer.

**Étape 3 — Lister les retraits dans la pool autour du timing**. Pour pool active, peut être beaucoup. Pour pool peu active, peut être peu.

**Étape 4 — Analyse statistique**. Timing, montant, behavioral. Identifier candidats probables.

**Étape 5 — Croiser avec contexte externe**. Si l’opérateur est suspecté d’utiliser Tornado et a une adresse de retrait probable, vérifier cohérence.

**Étape 6 — Calibrer la confiance**. Pour analyse statistique pure, attribution rarement « probable » (souvent « possible » ou plus faible).

**Étape 7 — Rapport avec limites explicites**.

#### 31.8 L’impact des sanctions sur l’usage

**Pre-sanctions août 2022** : Tornado Cash utilisé massivement, par Lazarus et nombreux autres acteurs. Volume mensuel : centaines de M USD.

**Post-sanctions** : volume a chuté drastiquement. Mais Tornado **continue à fonctionner** (code immutable). Acteurs critiques (Lazarus) continuent à l’utiliser malgré sanctions, acceptant la pression sur off-ramps.

**Migrations** : certains acteurs ont migré vers :

- Sinbad.io (avant sanctions OFAC).
- Mixers Bitcoin résiduels (Wasabi, Samourai pre-saisie).
- Bridges + DEX comme alternatives partielles.
- Privacy coins (Monero).

#### 31.9 Stratégie défensive face aux mixers

**Côté exchange** : screening de dépôts pour détecter fonds tracés à mixers (KYT Chainalysis, équivalents). Refus d’acceptation ou alerting.

**Côté plateforme** : Many DEX et frontends ont implémenté blocages des adresses Tornado post-sanctions.

**Côté autorités** : poursuite des opérateurs (Pertsev, Storm), sanctions continues.

#### 31.10 Fil rouge — MIXSHADOW : analyse Tornado

> **🔗 MIXSHADOW — Épisode 18 : limite de l’analyse Tornado**
> 
> Sarah revient sur les **dépôts Tornado** d’Akira (12 ETH cumulés sur 3 dépôts).
> 
> Elle applique l’analyse statistique :
> 
> **Anonymity set au moment des dépôts** : ~50-200 dépôts non-retirés par pool selon la fenêtre. Anonymity set moyen.
> 
> **Recherche de retraits candidats** :
> 
> - Sarah liste tous les retraits sur les pools 10 ETH et 1 ETH dans la fenêtre 3-30 jours post-dépôts Akira.
> - Total : ~120 retraits candidats à examiner.
> 
> **Filtrage par pattern** :
> 
> - Retraits avec timing très court post-dépôt (<1 jour) éliminés (probable autres utilisateurs avec patterns d’urgence — pas Akira qui semble patient).
> - Retraits vers adresses sanctionnées éliminés (autres acteurs).
> - Retraits vers adresses à patterns clairement non-criminels éliminés.
> 
> **Reste** : ~30 retraits candidats.
> 
> **Recoupement avec autres données MIXSHADOW** :
> 
> - Sarah compare les adresses de retrait avec les adresses Akira identifiées sur les autres branches.
> - **Aucune correspondance directe**.
> - **2 adresses « similaires »** dans le sens où elles montrent ensuite des patterns cohérents avec opérations de blanchiment Akira ultérieures.
> 
> **Calibration** :
> 
> - Attribution des **2 adresses comme retraits Akira probables** : confiance ~50% (« possible » fort, mais pas « probable » solide).
> - Autres retraits candidats : indéterminable sans données additionnelles.
> 
> Sarah documente dans le rapport :
> > « Sur les 12 ETH déposés à Tornado Cash, l’analyse statistique des retraits dans la fenêtre temporelle compatible identifie 2 candidats de retrait avec des patterns d’usage post-retrait cohérents avec les opérations Akira observées sur les autres branches. La confiance d’attribution est cependant limitée à « possible » (~50%). Pour les 10 ETH restants, aucun candidat avec confiance suffisante n’a été identifié. La rupture de visibilité induite par Tornado Cash limite intrinsèquement l’enquête sur cette branche. »
> 
> Calibration honnête. Pas de sur-attribution. Pas non plus de capitulation totale (les 2 candidats identifiés alimentent la fiche acteurs).
> 
> Sarah ajoute pour le rapport : **possibilité de coordination internationale** sur les 30 retraits candidats. Si la DGSI / FBI peuvent confronter ces 30 adresses à leurs propres données (renseignement, autres enquêtes), des matches peuvent émerger qui passeront du statut « possible » à « probable ». Cf Ch.43 — Tornado Cash dans le cas Ronin / Lazarus a été partiellement « démêlé » par cette approche multi-source.

-----

### Chapitre 32 — CoinJoin : Wasabi, Samourai

Le **CoinJoin** est une technique d’anonymisation Bitcoin différente des mixers custodial. Coopérative, non-custodial. Wasabi et Samourai sont les implémentations principales.

#### 32.1 Principe du CoinJoin

**Idée** : multiple utilisateurs créent **collectivement une transaction** Bitcoin avec multiples inputs et outputs, sans révéler à un opérateur central qui possède quoi.

**Mécanisme simplifié** :

1. Plusieurs utilisateurs (5 à 100+ selon implémentation) coordonnent.
1. Chacun fournit des inputs (UTXO qu’il contrôle).
1. Tous signent une transaction agrégée.
1. Outputs sont mélangés : impossible de dire depuis l’extérieur quel input correspond à quel output.

**Exemple** :

- 10 utilisateurs, chacun 1 BTC en input (10 BTC total).
- Outputs : 10 × 1 BTC vers 10 nouvelles adresses.
- Heuristique du co-spend appliquée naïvement dirait : tous appartiennent à même entité. **C’est faux** dans le CoinJoin.

**Effet** : casser l’heuristique du co-spend. Chaque output, vu de l’extérieur, peut appartenir à n’importe quel input.

#### 32.2 Wasabi Wallet

**Wasabi Wallet** est un wallet Bitcoin avec CoinJoin intégré. Implémentation **ZeroLink** (variante CoinJoin avec Chaumian e-cash).

**Caractéristiques** :

- Coordinator central (mais ne détient pas les fonds).
- Anonymity set fixe (~100 utilisateurs par round historiquement).
- Frais (sur le coordinator).

**Évolution** :

- Wasabi 1.0 : protocole ZeroLink pur.
- Wasabi 2.0 : WabiSabi, anonymity set plus flexible, frais plus bas.

**Réputation** : utilisé par utilisateurs privacy-conscious légitimes ET par criminels. Coordinator peut blacklister certains UTXO (controverse).

#### 32.3 Samourai Wallet

**Samourai Wallet** : wallet Bitcoin alternatif, focus privacy.

**Whirlpool** : implémentation CoinJoin de Samourai. Différences :

- Anonymity set plus petit par round (5 utilisateurs).
- Mais cycles répétés pour augmenter anonymat cumulatif.
- Coordinator distinct.

**Saisie avril 2024** : opération US, fondateurs Keonne Rodriguez et William Lonergan Hill inculpés. Infrastructure saisie. Whirlpool stoppé.

**Implications** :

- Logs du coordinator récupérés permettent investigation rétroactive.
- Saisie envoie message sur acceptabilité légale des CoinJoin services, débat actif.

#### 32.4 Détection de CoinJoin

**Signaux** :

**Multiple inputs et multiple outputs avec montants identiques**. Une transaction CoinJoin Wasabi typique : 100 inputs, 100 outputs de même valeur. Très distinctif.

**Coordinator address**. Wasabi prélève une fee qui va à un coordinator. Adresse identifiable.

**Patterns de timing**. Les CoinJoin ont des cycles temporels. Wasabi v2 fait des CoinJoin réguliers.

**Outils d’analyse** : KYCP.org analyse spécifiquement les CoinJoin. Détecte les transactions, calcule l’anonymity set, score la qualité du mix.

#### 32.5 Limites du dé-mixage CoinJoin

**Heuristique cassée** : le co-spend dans CoinJoin n’est pas une indication d’entité commune. Outils pro **doivent détecter** les CoinJoin et **exclure** ces transactions du clustering. Reactor / TRM le font.

**Analyse possible mais limitée** :

- **Sub-mixing** : si l’anonymity set est petit (Whirlpool 5 inputs), inférence statistique partielle.
- **Toxic UTXO** : si un UTXO entré dans CoinJoin est entaché (par exemple, vient d’une adresse sanctionnée), le mélange CoinJoin ne « purifie » pas pour les autorités — les outputs gardent une « contamination » statistique.
- **Behavioral analysis** : patterns post-CoinJoin peuvent identifier l’utilisateur initial.

**Coordinator logs** : si coordinator coopère ou est saisi, logs permettent dé-mixage substantiel. Cas Samourai.

#### 32.6 Wasabi vs mixers custodial

|Critère      |CoinJoin (Wasabi)                        |Mixer custodial (Tornado)                                                                 |
|-------------|-----------------------------------------|------------------------------------------------------------------------------------------|
|Custody      |Non-custodial                            |Custodial (Tornado est non-custodial via smart contract, autres mixers BTC sont custodial)|
|Risque de vol|Faible                                   |Élevé (mixers traditionnels)                                                              |
|Anonymat     |Modéré                                   |Variable                                                                                  |
|Logs         |Coordinator a logs (Wasabi)              |Variable                                                                                  |
|Légalité     |Moins claire mais usage légitime fréquent|Plus contestée                                                                            |
|Démantèlement|Wasabi continue, Samourai saisi          |Multiple démantèlements (Helix, BitcoinFog, ChipMixer, Tornado sanctionné)                |

#### 32.7 Méthode d’enquête face à CoinJoin

**Étape 1 — Détecter le CoinJoin**. Outils pro indiquent. Manuellement : pattern de transaction (multiple in/out de même valeur).

**Étape 2 — Documenter**. Quelle implémentation (Wasabi v1, v2, Samourai), quel anonymity set, quel coordinator.

**Étape 3 — Continuer le tracking**. Outils pro continuent souvent à suivre la « probabilité » de chaque input vers chaque output (pas certain mais probabiliste).

**Étape 4 — Calibrer**. Confidence sur destinataires post-CoinJoin = limitée.

**Étape 5 — Coopération**. Pour cas critiques, demande au coordinator (si encore actif) ou récupération de logs post-saisie.

#### 32.8 Tendances 2024-2026

**Saisie Samourai (avril 2024)** : impact majeur. Samourai était populaire. Migration vers Wasabi ou autres alternatives.

**Wasabi** : continue, mais sous pression. Coordinator en juridiction permissive pour minimiser risque. Updates régulières.

**Joinmarket** : alternative décentralisée (pas de coordinator central), moins user-friendly mais plus résiliente.

**Lightning Network** : autre approche privacy (pas CoinJoin technique, mais effet similaire — paiements off-chain limitent traçabilité on-chain).

**Pour l’enquêteur** : CoinJoin reste une **rupture analytique** sur Bitcoin, mais pas absolue. Combinaison avec autres indices et analyse temporelle / behavioral peut donner des angles.

-----

### Chapitre 33 — Bridges et cross-chain laundering

Les **bridges** sont des protocoles permettant de transférer des actifs entre blockchains. Ils sont **infrastructure légitime** mais aussi vecteur majeur de blanchiment et de hacks. Comprendre leur fonctionnement et leurs limites pour l’enquête est central.

#### 33.1 Pourquoi les bridges existent

**Problème** : un Bitcoin natif ne peut pas exister directement sur Ethereum. Une USDT ERC-20 (Ethereum) ne peut pas être directement transférée à une adresse TRC-20 (TRON). Les blockchains sont **isolées** par construction.

**Solution** : bridges permettent de « migrer » un actif d’une chaîne à une autre, par mécanismes variés.

**Mécanismes** :

**Wrapped tokens** : sur la chaîne destinataire, un token « wrapped » est créé représentant l’actif natif de la chaîne source. Exemple : WBTC (Wrapped Bitcoin) sur Ethereum est un ERC-20 dont la valeur correspond à du BTC réel détenu en custody.

- Étapes : utilisateur dépose BTC sur custody → mint WBTC sur Ethereum → utilise WBTC dans DeFi → burn WBTC + retrait BTC depuis custody.

**Lock-and-mint** : actif locké sur chaîne source, équivalent miné sur chaîne destinataire.

**Burn-and-mint** : actif burned sur chaîne source, miné sur chaîne destinataire.

**Liquidity pools cross-chain** : pools de liquidité présents sur multiples chaînes, swap effectif entre chaînes.

**Intermediate exchanges** : non un « bridge » technique, mais effet équivalent — passer par exchange centralisé pour switch entre chaînes.

#### 33.2 Bridges majeurs

**Wormhole** : Ethereum, Solana, BNB, Avalanche, Polygon, etc. Hack majeur février 2022 (326 M USD).

**Multichain (anciennement Anyswap)** : multi-chain. Compromis 2023, ~130 M USD volés dans circumstances opaques.

**Stargate** : LayerZero-based, multi-chain.

**Synapse** : multi-chain.

**Hop Protocol** : Layer-2 Ethereum focus.

**Across** : multi-chain, optimistic.

**deBridge** : multi-chain.

**Rainbow Bridge** (Aurora / NEAR) : Ethereum-NEAR.

**WBTC** : centralisé, Bitcoin → Ethereum.

**RenBTC** : décentralisé, multi-chain BTC. RenVM stoppé en 2023, mais cf forks.

**THORChain** : decentralized cross-chain swaps. Multiple incidents et reprises.

**FixedFloat, ChangeNOW, SimpleSwap** : services de swap cross-chain non-KYC. Différents techniquement (intermediaires opérant des pools propres) mais effet bridge utilisateur.

**Pour l’enquêteur** : la liste évolue rapidement. Vérifier la couverture par les outils pro.

#### 33.3 Pourquoi les bridges sont attractifs pour le blanchiment

**Casser la chaîne**. Un fonds passe d’Ethereum à BNB Chain via bridge. Suivre cross-chain demande capacité spécifique.

**Multi-juridictionnel**. Différentes blockchains ont différents écosystèmes (régulés / non-régulés, KYC / non-KYC). Bridge permet de glisser du « monitoré » au « moins monitoré ».

**Faible KYC**. Bridges typiques sont smart contracts non-custodial — pas de KYC.

**Vitesse**. Bridge typique : minutes à heures. Plus rapide que conversion via exchange centralisé.

**Volume liquide**. Multi-billion USD passent par bridges quotidiennement. Fonds illicites se fondent dans le bruit.

#### 33.4 Hacks de bridges

Les bridges ont été ciblés massivement pour leurs vulnérabilités.

**Top hacks** :

- **Ronin** (mars 2022, 625 M USD) — Lazarus.
- **Wormhole** (février 2022, 326 M USD).
- **Nomad** (août 2022, 190 M USD).
- **Multichain** (juillet 2023, 130 M USD) — circumstances opaques.
- **Harmony Bridge** (juin 2022, 100 M USD) — Lazarus.
- **Orbit Chain** (janvier 2024, 80+ M USD).
- **Multiple autres** 2023-2026.

**Pourquoi cibles** :

- **Concentration de fonds** : bridges détiennent des centaines de millions USD en custody.
- **Code complexe** : surfaces d’attaque larges.
- **Validators externes** : si compromis, takeover possible.
- **Monitoring limité** : moins de regards techniques que sur protocoles DeFi mainstream.

**Pour l’enquêteur** : un hack de bridge nécessite **tracking cross-chain** intensif. Les attaquants utilisent les fonds pour disperser sur multiple chaînes immédiatement.

#### 33.5 Suivre un fonds à travers un bridge

**Méthode** :

**Étape 1 — Identifier la transaction de dépôt sur chaîne source**. Adresse utilisateur → smart contract bridge.

**Étape 2 — Consulter les logs / events du bridge**. Le bridge émet un event décrivant la transaction destinataire (chaîne, adresse, montant).

**Étape 3 — Identifier la transaction correspondante sur chaîne destinataire**. Souvent quelques minutes à heures plus tard. Rechercher par adresse destinataire et montant.

**Étape 4 — Continuer le suivi sur la nouvelle chaîne**.

**Outils pro** : Reactor / TRM / Elliptic suivent automatiquement les bridges majeurs. Mais couverture variable selon bridge et selon outil.

**Outils gratuits** : pour bridges populaires (Stargate, Across), sites comme `socket.tech` ou `debridge.finance` ont des explorateurs cross-chain. Utile pour traçage manuel.

#### 33.6 Limites du tracking cross-chain

**Pas tous les bridges sont supportés** par les outils pro. Bridges obscurs ou spécialisés peuvent passer sous le radar.

**Délai de résolution**. Sur certains bridges, le matching entre dépôt et retrait est différé. L’analyste peut perdre la trace si pas vigilant.

**Multiple hops cross-chain**. Fonds qui passent ETH → BSC → TRON → Polygon → ETH représentent une chaîne compliquée à suivre. Erreurs possibles à chaque saut.

**Liquidity pools** : les bridges via pools (Stargate, etc.) ne maintiennent pas un mapping 1-to-1 entre dépôts et retraits. Fonds entrent dans un pool, autres fonds sortent — l’utilisateur reçoit des fonds différents (en termes de UTXO).

**Wrapped tokens et redemption**. Un utilisateur peut wrap, déwrap, re-wrap — multiple cycles brouillent.

#### 33.7 Tracking spécifique par bridge

**Wormhole** : explorateur Wormhole Scan permet de matcher transactions cross-chain. Émet events détaillés.

**Stargate** : Stargate Finance interface, transactions traçables via LayerZero events.

**Multichain** : historiquement traçable, mais post-compromis 2023, situation chaotique.

**WBTC / wrapped centralisés** : custody centralisée, mints et burns visibles. Mais pour suivre quel BTC correspond à quel WBTC, custody internal logs nécessaires.

**FixedFloat / ChangeNOW** : pas de matching public direct (services internalisent). Suivi par timing et montant possible mais probabiliste.

#### 33.8 Coopération avec opérateurs de bridges

**Bridges decentralisés** : pas d’opérateur central à qui demander coopération. Smart contract immutable.

**Bridges semi-centralisés** (multisig validators, custodial) : peuvent coopérer sur réquisition. Cas variés.

**Wrapped tokens centralisés** (WBTC) : custody peut coopérer. WBTC custody (BitGo) coopère avec autorités sur cas légaux.

**FixedFloat / ChangeNOW / similaires** : politique de KYC / coopération variable. Souvent limitée.

#### 33.9 Tendances 2024-2026

**Bridges restent vulnerables** : continuent à se faire hacker régulièrement.

**Sophistication de tracking** : Reactor / TRM / Elliptic améliorent couverture cross-chain. Mais lag sur nouveaux bridges.

**Régulation** : MiCA en EU pourrait éventuellement imposer KYC sur bridges, mais débat actif. Les bridges décentralisés posent question juridique (qui régule un smart contract ?).

**Layer-2 et bridges natifs** : Arbitrum, Optimism, Base bridges ont architectures différentes (rollups), tracking spécifique.

#### 33.10 Fil rouge — MIXSHADOW : tracking cross-chain Akira

> **🔗 MIXSHADOW — Épisode 19 : la branche cross-chain**
> 
> Sarah a tracé une **branche secondaire** dans MIXSHADOW : ~5 BTC depuis le peeling chain ont été convertis via FixedFloat en USDT-Ethereum. Ces USDT ont ensuite été bridgés via **Stargate** vers BNB Chain.
> 
> **Tracking** :
> 
> - Transaction Ethereum : USDT-ETH → Stargate router contract.
> - Event Stargate : transfer to BNB Chain, destination address `0x[BNB-Akira]`.
> - Transaction BNB Chain : USDT-BNB reçus quelques minutes plus tard.
> 
> Reactor a suivi automatiquement. Validation manuelle via Stargate Finance interface confirme la correspondance.
> 
> Sur BNB Chain, suite : USDT-BNB swappés via DEX en BUSD (Binance USD), puis transférés vers adresses dépôt Binance. **3 dépôts Binance** identifiés sur cette branche.
> 
> **Coopération** : ces 3 adresses Binance (avec USDT cumulés ~30 000 USDT équivalent) sont transmises à la DGSI pour réquisition KYC. **2 mules identifiées** (cf Ch.30.9). Coopération Binance-DGSI productive.
> 
> Sarah note dans le rapport : la **branche cross-chain** Akira est plus modeste en volume (~5 BTC sur 35) que la branche TRON-USDT (~3 BTC qui sont devenus 290k USDT). Mais elle est **plus traçable** parce que Stargate est bien couvert par les outils et Binance KYC est solide. Paradoxe : le criminel qui choisit la « simplicité » (Stargate + Binance) est plus exposé que celui qui choisit le « non-KYC + dispersion » (FixedFloat + exchange non-KYC + hubs TRON). Akira a fait les deux choix sur des branches différentes — diversification des risques pour l’opérateur.
> 
> Cette observation (Akira diversifie les chemins de blanchiment) alimente la fiche acteur Akira pour la base Athéna et CTI sectoriel.

-----

### Chapitre 34 — DEX, swaps et obfuscation DeFi

Les **DEX** (decentralized exchanges) et plus largement les **protocoles DeFi** offrent des outils additionnels d’obfuscation. Plus subtils que mixers ou bridges, ils permettent transformations d’actifs et brouillage des origines.

#### 34.1 Les principaux DEX

**Uniswap** (Ethereum) : référence. Multi-version (V2, V3, V4). Pools de liquidité automated market maker (AMM).

**SushiSwap** : fork Uniswap, multi-chain.

**Curve Finance** : spécialisé stablecoins et actifs corrélés. Faible slippage sur paires similaires.

**PancakeSwap** : leader sur BNB Chain. Équivalent Uniswap.

**Balancer** : pools customisables, multi-actifs.

**1inch, Matcha, Paraswap** : aggregators (routent à travers multiple DEX pour meilleur prix).

**dYdX, GMX** : DEX dérivés (perpétuels, options).

**Trader Joe** : DEX Avalanche.

**Raydium, Orca, Jupiter** : DEX Solana.

**SunSwap, JustLend** : écosystème TRON.

#### 34.2 Pourquoi les DEX permettent obfuscation

**Pas de KYC**. Smart contracts non-custodial. Pas d’identité requise.

**Conversion d’actifs**. ETH → USDT en quelques secondes. Brouille l’origine.

**Liquidité massive**. Volumes énormes. Fonds illicites se fondent dans le bruit.

**Multi-pool / multi-route**. Aggregators routent via plusieurs pools. Trace plus complexe.

**Multi-chain**. Combinaison DEX + bridge donne transformations multi-chaînes.

#### 34.3 Patterns d’obfuscation via DEX

**Conversion simple**. Adresse reçoit ETH suspect, swap en USDT, USDT déposé sur exchange → KYC trace plus difficile.

**Multi-hop**. ETH → USDT → DAI → USDC → ETH. Multiple swaps redondants avant l’objectif. Brouille analyse simple.

**Yield farming intermédiaire**. Dépôt en pools de liquidité, claim de fees, retrait. Crée de l’historique « DeFi natural » qui peut tromper analyse superficielle.

**Flash loan layering**. Plus avancé : utilisation de flash loans pour manipulation de pools / arbitrage. Les fonds passent par multiple protocoles en une seule transaction.

#### 34.4 Tracker un swap DEX

**Étape 1 — Identifier la transaction de swap**. Sur Etherscan, transaction qui appelle un DEX router.

**Étape 2 — Lire les logs**. Events `Swap` indiquent montants et tokens d’entrée/sortie.

**Étape 3 — Comprendre la route**. Aggregators peuvent passer par 2-5 pools en une transaction. Analyser tous les hops.

**Étape 4 — Continuer le tracking sur les fonds reçus**. Adresse user reçoit le token de sortie.

**Outils pro** : Reactor / TRM / Elliptic suivent automatiquement à travers DEX. Excellente couverture pour DEX mainstream.

**Outils gratuits** : Etherscan affiche transactions DEX bien décodées si contrats vérifiés (presque toujours le cas pour DEX majeurs).

#### 34.5 Limites

**Multi-hop complexe**. Un aggregator routant via 5 pools est plus difficile à parser visuellement (mais bien décodé par les outils).

**MEV (Maximal Extractable Value)**. Les bots MEV peuvent intervenir dans les transactions, complexifiant l’analyse.

**Liquidity provider activity**. Si le criminel agit comme LP (provide liquidity), ses fonds sont mélangés avec la liquidité globale du pool. Tracking devient probabiliste.

**Pool extractables**. Certains LPs custodial peuvent retirer (par exemple, récupération fonds d’une pool LP), brouillant les traces.

#### 34.6 Cas typiques

**Hack DeFi → swap rapide**. Attaquant draine un protocole DeFi, swap rapidement les tokens volés en stablecoin ou ETH (plus liquide), puis suit chemin classique d’obfuscation. Vu dans nombreux hacks 2022-2026.

**Pig butchering → swap pré-cashout**. Fonds USDT-TRON consolidés peuvent être swappés en autres stablecoins ou BTC pour faciliter cashout sur certaines plateformes.

**Ransomware → swap pour anonymisation**. Cf MIXSHADOW : Akira a swappé partiellement BTC en ETH via FixedFloat avant Tornado Cash.

#### 34.7 Différence DEX vs CEX vs swap services

**DEX** (Uniswap, etc.) : smart contract pur. Pas de KYC. Pas d’opérateur central pour coopération.

**CEX** (Binance, etc.) : entreprise centralisée. KYC. Possible coopération.

**Swap services** (FixedFloat, ChangeNOW, SimpleSwap) : services qui permettent swap sans KYC mais avec opérateur central. Hybrides — pas vraiment décentralisés (l’opérateur peut blacklister, refuser), pas vraiment KYC. Souvent utilisés pour cross-chain rapide. Coopération variable selon service.

#### 34.8 Tendances 2024-2026

**Volume DEX en croissance**. DeFi mature, plus d’utilisateurs.

**Cross-chain DEX** : 1inch Cross-chain, autres aggregators cross-chain.

**Régulation** : MiCA cible exchange centralisés, mais DEX est zone grise. Débat actif.

**Réseaux MEV-dominants** : MEV-Boost et auctions deviennent partie intégrale de l’écosystème, complexifiant l’analyse.

**Pour l’enquêteur** : DEX est **moins une rupture de visibilité qu’un détour traçable**. Ne pas avoir peur, mais ajouter au temps d’analyse.

-----

### Chapitre 35 — Privacy coins : Monero, Zcash, limites radicales

Les **privacy coins** sont des cryptomonnaies conçues pour l’anonymat. Contrairement à Bitcoin (pseudonyme) ou aux mixers (obfuscation ajoutée), les privacy coins ont l’anonymat **par construction**. Ce chapitre couvre les principales et leurs implications pour l’enquête.

#### 35.1 Monero (XMR)

**Lancé** : avril 2014 (fork de Bytecoin).

**Principes** :

**Ring signatures**. Chaque transaction Monero contient des signatures multiples — la vraie + plusieurs « decoys » (faux signataires plausibles). Impossible de savoir quel signataire est le vrai. Effet : l’**émetteur** d’une transaction est ambigu parmi un ring de candidats.

**Ring Confidential Transactions (RingCT)**. Les **montants** sont cachés cryptographiquement. Visible : « cette transaction transfère un montant X ». Pas visible : la valeur de X.

**Stealth addresses**. Le **destinataire** d’une transaction est caché. Adresse de réception « one-time » dérivée pour chaque transaction. Lien entre adresse on-chain et destinataire réel non-trivial.

**Effet combiné** : émetteur masqué, montant masqué, destinataire masqué. Quasi-anonymat.

**Adoption** : populaire dans dark web markets, ransomware (certains exigent Monero), particuliers privacy-conscious.

#### 35.2 Limites de Monero

**Pas absolument anonyme** :

**Decoy quality**. Les decoys sont sélectionnés selon algorithme. Si l’algorithme a des biais ou si le ring inclut decoys peu plausibles (par exemple, decoys « trop vieux »), analyse statistique peut réduire l’incertitude. Recherche académique active.

**Vulnérabilités d’implémentation**. Certaines versions de Monero ont eu des vulnérabilités permettant dé-anonymisation partielle. Patches successifs.

**Usage off-chain**. Si l’utilisateur achète Monero sur exchange KYC, l’achat est traçable. La conversion en autres actifs après usage Monero est aussi un point.

**Erreurs OPSEC**. Réutilisation de wallets avec multiple couches d’obfuscation peut leak. Patterns d’usage peuvent identifier acteur.

**Decoy attacks** : des chercheurs ont publié plusieurs papers sur dé-anonymisation partielle Monero. Exemples : sélection de decoys old enough to be unrealistic, timing analysis sur outputs.

**Pour l’enquêteur** : Monero est **largement opaque** pour l’analyse on-chain pure. L’enquête se déplace vers les **points off-chain** (exchanges, achats fiat, OPSEC errors).

#### 35.3 Zcash (ZEC)

**Lancé** : octobre 2016.

**Principes** :

**zk-SNARKs** : zero-knowledge proofs avancés permettant transactions complètement privées (montants, parties cachés).

**Mode dual** :

- **Transparent** : transactions comme Bitcoin, lisibles publiquement.
- **Shielded** : transactions privées via zk-SNARKs.

**Adoption** : majoritairement transparent. La fraction shielded est faible. Des recherches indiquent que les transactions Zcash sont à >80% transparentes.

#### 35.4 Limites Zcash

**Mode transparent** : analysable comme Bitcoin.

**Mode shielded** : opaque, mais **anonymity set faible** (peu d’utilisateurs en mode shielded). Patterns d’entrée/sortie shielded peuvent réduire l’incertitude.

**Trusted setup** : Zcash early required a trusted setup ceremony. Si la randomness a été compromise, attaque théorique possible. Ceremonies multiples, peu probable d’être compromis pour les versions récentes.

**Pour l’enquêteur** : Zcash est **moins opaque que Monero en pratique** parce que l’usage shielded est minoritaire. Pour transactions transparentes, méthode standard. Pour shielded, limites similaires à Monero.

#### 35.5 Dash et autres

**Dash** (lancé 2014) : « PrivateSend » est CoinJoin amélioré. Moins efficace que Monero, plus simple à analyser.

**Beam, Grin** (lancés 2019) : implémentent Mimblewimble. Concept différent (no addresses, transactions agrégées). Adoption faible.

**Pirate Chain (ARRR)** : zk-SNARKs forced (pas de mode transparent). Faible volume.

**Pour l’enquêteur** : Monero domine clairement le segment privacy. Autres rares en pratique.

#### 35.6 Méthode d’enquête face à Monero

**Étape 1 — Reconnaître la rupture**. Si fonds passent en Monero, traçabilité on-chain quasi-impossible.

**Étape 2 — Documenter la rupture**. « À l’étape N, fonds convertis en Monero via [exchange/swap]. Au-delà, traçabilité on-chain non possible sans données off-chain. »

**Étape 3 — Identifier les points off-chain** :

- **Achat de Monero** : comment ont-ils été obtenus ? Si depuis exchange KYC, identité achat traçable.
- **Vente de Monero** : si reconvertis en autre actif via exchange, identité vente traçable.
- **OPSEC errors** : réutilisation, patterns, mentions publiques.

**Étape 4 — Inférer ce qui peut être inféré** :

- Si fonds entrent en Monero à T0 et un autre acteur reconvertit Monero en USDT à T0+5min via même exchange, **possible** lien.
- Pas certain — coïncidence possible.

**Étape 5 — Calibrer**. Confidence sur attribution post-Monero = très limitée sans autres données.

**Étape 6 — Coopération**. Si Monero a été obtenu/vendu via exchange KYC, réquisition possible. Si privé tout du long, impasse OSINT.

#### 35.7 Cas réels Monero

**Ransomware Monero-only** : Akira (cf MIXSHADOW), REvil (historique), DarkSide variantes. Demandent paiement en XMR pour rupture immédiate.

**Darknet markets** : multiple marchés russophones et anglophones acceptent ou exigent Monero.

**Acteurs étatiques Lazarus** : utilisation de Monero documentée pour certaines opérations.

**Limitation** : exchanges régulés ont **massivement délistsé Monero** depuis 2020. Coinbase, Kraken, Binance ont retiré Monero. Cela limite cashout pour criminels (plus difficile de revenir en fiat sans suspicion). Effet partiel — exchanges secondaires et P2P continuent.

#### 35.8 Tendances 2024-2026

**Pression réglementaire** : Monero ciblé par autorités. Multiples démarches pour limiter accessibilité.

**Améliorations techniques Monero** : protocole évolue (Bulletproofs, Triptych, autres). Augmente anonymat.

**Recherche académique active** : papers réguliers sur dé-anonymisation partielle.

**Migration** : certains acteurs criminels migrent vers Monero alternatives ou vers techniques mixtes (Bitcoin + privacy layers comme Lightning Network ou CoinJoin chained).

#### 35.9 Le message à intérioriser

> Monero est une rupture de visibilité quasi-totale pour l’analyse on-chain. L’enquêteur OSINT honnête le reconnaît, le documente, et déplace l’enquête vers les angles off-chain. Promettre un « démêlage » Monero = sur-promesse risquée.

#### 35.10 Fil rouge — MIXSHADOW : pas de Monero pour Akira… cette fois

> **🔗 MIXSHADOW — Épisode 20 : absence de Monero**
> 
> Akira accepte généralement les paiements en Bitcoin (selon docs récentes du groupe). Le paiement Aurélien Médical était en BTC, comme négocié.
> 
> Sarah note cependant que **certains autres acteurs ransomware** exigent Monero (REvil historique, certains affiliés ciblés). Dans le cadre d’Akira spécifiquement, Bitcoin domine.
> 
> Si Akira avait demandé du Monero, l’enquête MIXSHADOW serait **très différente** :
> 
> - Traçabilité on-chain quasi nulle au-delà de la conversion BTC → XMR.
> - Enquête se serait déplacée vers : analyse de l’exchange où conversion XMR/USD effectuée, points OPSEC d’Akira, ciblage de cashout fiat.
> - Couverture beaucoup plus faible (~10-20% des flux possibles à tracer vs ~75% atteints en BTC).
> - Rapport aurait conclu rapidement sur **rupture de visibilité** et pivot vers angles off-chain.
> 
> Sarah documente dans le rapport final :
> > « Le choix Bitcoin par Akira pour le paiement Aurélien Médical, plutôt que Monero, a permis une investigation crypto-forensique substantielle. Si Akira avait imposé Monero (comme certains autres opérateurs ransomware), la traçabilité on-chain aurait été drastiquement réduite. Cette observation suggère qu’Akira accepte un compromis traçabilité / facilité opérationnelle, peut-être par contrainte de liquidité (BTC plus liquide / acceptable pour victimes), peut-être par sous-estimation de la capacité forensique. »
> 
> Insight : pour victimes futures d’Akira, négocier paiement en BTC plutôt qu’en Monero peut être un angle (si négociation possible, ce qui n’est pas toujours le cas — l’opérateur impose).
> 
> La Partie VII va dérouler **5 cas pratiques** complets pour appliquer toutes les méthodes apprises.

-----

## PARTIE VII — CAS PRATIQUES DÉROULÉS

> **Ce que cette partie apprend.** Voir 5 enquêtes complètes déroulées bout en bout, depuis l’indice initial jusqu’au rapport. Chaque cas mobilise toutes les méthodes des Parties précédentes en contexte. Cas fictifs construits pédagogiquement pour montrer la méthode pure ; les cas historiques réels sont en Partie VIII.
> 
> **Ce qu’elle ne couvre pas.** Théorie (déjà vue). Cas historiques (Partie VIII).
> 
> **Ce que vous saurez faire après cette partie.** Conduire vous-même une investigation crypto en suivant les méthodes apprises. Adapter aux typologies (pig butchering, ransomware, drainer, multi-chain, Monero). Anticiper les difficultés et calibrer vos conclusions.

-----

### Chapitre 36 — Cas 1 : victime de pig butchering USDT Tron

**Profil de l’enquête** : enquête typique sur un cas individuel de pig butchering. Volume modeste (~200 000 USD), pattern reconnaissable, méthode standard.

#### 36.1 Le contexte

Marie (nom d’emprunt), 52 ans, cadre supérieure dans une PME française, contacte un cabinet d’investigation après réalisation d’une fraude. Elle a été victime d’une opération de pig butchering sur 4 mois (octobre 2025 - février 2026).

**Récit factuel** (synthétisé à partir du briefing client) :

- Octobre 2025 : Marie est contactée sur Instagram par un certain « Daniel Wang », se présentant comme entrepreneur à Singapour. Approche amicale, pas de demande financière initiale.
- Novembre 2025 : la relation devient amicale-puis-sentimentale (à distance). Daniel partage des « histoires » de succès en investissement crypto.
- Décembre 2025 : Daniel introduit Marie à une « plateforme exclusive » d’investissement DeFi, gérée par un « ami fonds ». Premier dépôt suggéré : 3 000 USDT.
- Janvier 2026 : la plateforme montre des « gains » de 30% en deux semaines. Marie augmente : 15 000 USDT, puis 50 000 USDT.
- Février 2026 : Marie liquide une partie de son épargne et investit 130 000 USDT supplémentaires.
- Mi-février : Marie tente un retrait de 50 000 USDT. La plateforme demande une « caution fiscale » de 20 000 USDT pour débloquer. Marie refuse et tente de contacter Daniel. Plus de réponse. Plateforme inaccessible.

**Total perdu** : ~198 000 USDT (~ 198 000 EUR au cours du moment).

Marie a porté plainte (gendarmerie locale + signalement Pharos + cybermalveillance.gouv.fr). Elle mandate un cabinet privé pour cartographier les flux et préparer un dossier solide pour la procédure.

#### 36.2 Le cadrage de la mission

**Objectifs** :

1. Confirmer les flux on-chain depuis Marie vers la plateforme frauduleuse.
1. Identifier l’écosystème : autres victimes probables, opérateurs derrière la plateforme, points de cashout.
1. Identifier les **angles d’action** des autorités (exchanges traversés, demandes de gel possibles).
1. Produire un **rapport actionnable** pour soutien à la procédure judiciaire.

**Limites** :

- Pas d’identification civile espérée (compounds Asie du Sud-Est probables).
- Récupération des fonds peu probable (déjà 2 mois après dernier paiement).
- Mission OSINT pure, pas d’engagement direct avec scammer.

**Budget** : 15 jours analyste senior, ~25 000 EUR.

**Cadre légal** : mission privée mandatée, RGPD respecté, livrables transmissibles à autorités.

#### 36.3 Phase 1 — Collecte initiale

**Inputs fournis par Marie** :

- 18 transactions USDT-TRON (sur 4 mois).
- TXIDs de chacune.
- Captures de l’app de la plateforme frauduleuse (avec adresses de dépôt).
- Captures des conversations Instagram avec Daniel.
- Photos partagées par Daniel (à analyser pour reverse image search).

**Étape 1 — Vérification on-chain**.

L’analyste ouvre Tronscan et vérifie les 18 transactions. Toutes confirmées. Total : 198 200 USDT. Cohérent avec le récit Marie.

**Étape 2 — Adresses de réception**.

Marie a déposé sur **3 adresses différentes** (la plateforme rotait les adresses) :

- T1 : 7 dépôts cumulés ~45 000 USDT (octobre-novembre).
- T2 : 6 dépôts cumulés ~75 000 USDT (décembre-janvier).
- T3 : 5 dépôts cumulés ~78 000 USDT (janvier-février).

**Étape 3 — Constitution fiches initiales**.

Pour chaque adresse :

- Première transaction : voit Marie comme dépositaire principal mais aussi **autres adresses sources**.
- Solde actuel : 0 (consolidé).
- Pattern de réception : multi-source, montants variables.

**Insight initial** : ces adresses ont **chacune reçu de multiples sources** (~30-50 sources par adresse). Marie n’est pas la seule victime.

#### 36.4 Phase 2 — Expansion vers le cluster

**Étape 1 — Identifier l’adresse hub**.

T1, T2, T3 ont consolidé leurs fonds vers une **adresse hub commune** : T-HUB. Cette adresse a reçu cumulativement ~3,2 M USDT (donc bien plus que Marie — l’opération a multiple branches).

**Étape 2 — Caractériser T-HUB**.

T-HUB :

- Active depuis ~6 mois.
- Reçoit de ~12 adresses de collecte (T1-T12 dans la fiche).
- Volume total entrée : ~3,2 M USDT.
- Volume sortie : ~3,1 M USDT (consolidation rapide).
- Pas de label public Tronscan.
- Label Chainalysis Reactor : **« High risk - probable scam »** (label propriétaire basé sur patterns).

**Étape 3 — Identifier les sources des autres adresses de collecte**.

Sur Tronscan, l’analyste liste les sources de T1-T12. Total : ~400 adresses sources distinctes. Probables **400 victimes** différentes de la même opération de pig butchering.

**Étape 4 — Suivi post-T-HUB**.

T-HUB envoie ses fonds vers :

- 30% : exchange non-KYC asiatique (label Chainalysis : « Asian exchange, KYC weak »).
- 25% : 4 adresses « hub-niveau-2 » (probable layering supplémentaire).
- 20% : DEX SunSwap (TRON DEX) pour swap USDT → TRX → puis re-swap.
- 15% : adresses inconnues sans label.
- 10% : Garantex (avant sanctions OFAC), sinon successeur identifié.

**Insight** : opération **structurée** avec consolidation, layering, et points de cashout multiples.

#### 36.5 Phase 3 — Investigation off-chain

**Étape 1 — Reverse image search sur photos Daniel**.

Les photos partagées par Daniel sont passées à l’analyse. Résultat : **3 photos sont issues d’un compte Instagram d’un homme réel (entrepreneur singapourien légitime)**. Identité volée. Daniel n’existe pas — c’est un alias utilisant les photos d’un tiers innocent.

**Note importante** : l’identité réelle volée n’est **pas mise en cause**. Le rapport mentionne la victime collatérale (l’entrepreneur singapourien), avec recommandation que Marie / autorités le contactent pour signaler abus de son identité.

**Étape 2 — Recherche OSINT sur la « plateforme »**.

Le nom de la plateforme (« CryptoYield Pro » — fictif) est recherché :

- Site web (capture Wayback Machine) : créé 8 mois avant arnaque, design crédible imitant exchange légitime.
- Domaine : enregistré chez registrar opaque, propriétaire masqué.
- Adresses mentionnées sur le site (« contacts ») : adresse à Singapour qui correspond à un coworking commercial — pas de bureau réel.
- Multiple signalements sur Chainabuse, Reddit r/CryptoScams, autres forums anti-scam.
- Plateforme listée comme **scam** sur multiple sites de recensement.

**Étape 3 — Recoupement avec autres victimes**.

L’analyste contacte le forum r/CryptoScams où des victimes ont signalé la même plateforme. **6 autres victimes identifiées** publiquement avec adresses crypto perdues. Les adresses correspondent à T-HUB ou T1-T12. **Confirmation** que c’est la même opération.

**Étape 4 — Tentative attribution opérateur**.

Patterns observables :

- Adresses fraîches utilisées par cycles (T1-T12 alternées sur 6 mois).
- Consolidation rapide post-réception (souvent dans les 24h).
- Cashout via exchanges asiatiques.

Patterns cohérents avec **compound asiatique** (Cambodge, Myanmar, Laos selon distribution typologique 2024-2026 documentée par TRM Labs et Elliptic). Pas d’attribution individuelle.

#### 36.6 Phase 4 — Analyse et synthèse

**Calibration** :

|Élément                                                 |Niveau       |Confiance|
|--------------------------------------------------------|-------------|---------|
|Marie a déposé 198 200 USDT vers T1, T2, T3             |Fait         |Certain  |
|T1, T2, T3 sont liés à l’opération « CryptoYield Pro »  |Très probable|90%      |
|T-HUB est la consolidation centrale de l’opération      |Probable     |80%      |
|Au moins 400 victimes affectées par l’opération         |Probable     |75%      |
|L’opération est gérée depuis un compound Asie du Sud-Est|Possible     |50%      |
|L’identité « Daniel Wang » est usurpée                  |Très probable|90%      |
|Récupération des fonds Marie possible                   |Peu probable |15%      |

**Volume de l’opération** :

- ~3,2 M USDT cumulé sur 6 mois identifiés (probablement plus avant et après).
- Marie représente ~6% du volume total observé.

**Points de cashout identifiés** :

- Exchange asiatique (KYC faible).
- Garantex (sanctionné).
- DEX TRON.
- Adresses inconnues (probables OTC/P2P).

#### 36.7 Phase 5 — Rapport et recommandations

**Rapport de 22 pages** structuré (Annexe H) :

- Executive summary.
- Méthodologie.
- Faits Marie (timeline, transactions).
- Cartographie de l’opération (graphes).
- Volume estimé et nombre de victimes.
- Points de cashout et angles d’action.
- Limites et incertitudes.
- Recommandations.

**Recommandations** :

1. **Pour Marie** :
- Transmettre le rapport au procureur en charge de la plainte.
- Signaler l’identité usurpée à l’entrepreneur singapourien (action de courtoisie).
- Documenter ses pertes pour fiscalité (déduction de pertes en investissement frauduleux selon législation).
- Soutien psychologique recommandé.
1. **Pour les autorités** (si transmettent) :
- Coordination internationale via Europol / Interpol.
- Contact avec autorités cambodgiennes / myanmarcaises / laotiennes (limite : coopération variable).
- Demande de gel à exchange asiatique identifié (faible probabilité de succès).
- Surveillance des adresses identifiées (futures activités).
1. **Pour la communauté** :
- Signalement à Chainabuse pour enrichissement base communautaire.
- Partage anonymisé avec ISAC financier.

#### 36.8 Restitution

Restitution à Marie : 1 heure. Marie est soulagée d’avoir une compréhension claire et un dossier solide, même si récupération improbable. Marie remercie pour la calibration honnête (pas de fausse promesse de récupération).

Le rapport est transmis par Marie au procureur en charge. Devenir ultérieur : fonction de la procédure judiciaire, hors mission cabinet.

#### 36.9 Bilan honnête

✅ **Réussites** :

- Cartographie complète de l’opération.
- Identification de 400+ co-victimes potentielles.
- Volume total documenté.
- Rapport actionnable pour autorités.

⚠️ **Limites** :

- Pas de récupération des fonds Marie (probabilité faible reconnue dès le départ).
- Pas d’identification civile des opérateurs (probable compound asiatique, hors d’atteinte OSINT).
- Cashout via exchange non-KYC = peu d’angles directs.

📊 **Métriques** :

- Durée : 12 jours analyste senior.
- Coût : 22 000 EUR.
- Couverture : 100% des flux Marie tracés. ~75% des flux opération globale identifiés.
- Calibration : tous les éléments avec WEP explicite.

**Apprentissage clé** : pour pig butchering, l’enquête **fonctionne** (cartographie, identification écosystème, alimente justice) mais ne **récupère** pas les fonds dans la grande majorité des cas. Honnêteté du mandat dès le départ = relation client saine.

-----

### Chapitre 37 — Cas 2 : paiement ransomware BTC à un affilié RaaS

**Profil de l’enquête** : enquête sur paiement ransomware par une PME française. Cas similaire à MIXSHADOW dans son schéma général mais d’un autre opérateur, pour montrer la diversité.

#### 37.1 Le contexte

**Société** : « TechIndustrie » (nom fictif), PME française de 180 employés, fournisseur de pièces industrielles pour automobile. Compromission ransomware début mars 2026.

**Récit** :

- Vecteur initial : email phishing ciblé sur compte VPN d’un commercial.
- Découverte : 2026-03-04 vers 06:00 UTC. Postes de production chiffrés.
- Note de rançon : groupe « Black Basta » (cluster bien documenté).
- Demande initiale : 60 BTC (~3,5 M EUR au cours).
- Négociation : descend à 22 BTC (~1,3 M EUR).
- Décision direction : payer (impossibilité de reprise rapide via backups, pression production).
- Paiement : 2026-03-10 14:32 UTC.
- Réception clé : 2026-03-10 18:45 UTC. Reprise progressive sur 2 semaines.

**Mandat** : la cyber-assurance de TechIndustrie mandate Athéna Group pour investigation post-paiement. Sarah Marin (déjà engagée sur MIXSHADOW) est trop chargée ; un collègue, **Thomas Lefèvre** (analyste senior Athéna, 4 ans expérience, certifié TRM Labs), prend en charge.

**Objectifs** :

1. Tracer les fonds.
1. Cartographier le blanchiment.
1. Contribuer à la threat intelligence Black Basta.
1. Coopérer avec autorités.

**Budget** : 6 semaines analyste, 65 000 EUR.

#### 37.2 Phase 1 — Collecte initiale

**Inputs** :

- TXID du paiement.
- Adresse Black Basta de réception : `bc1q[BB-receive]...` (fictif).
- Note de rançon en pièce jointe (avec adresse mentionnée).
- Logs forensics (Mandiant) du vecteur d’entrée.

**Étape 1 — Vérification on-chain**.

Mempool.space confirme : 22 BTC reçus sur l’adresse `bc1q[BB-receive]` le 2026-03-10 14:32 UTC. Cohérent.

**Étape 2 — Caractérisation initiale**.

Adresse fraîche, jamais vue avant le paiement. Solde 22 BTC. Pas encore de mouvement sortant au moment de l’analyse initiale (J+1 du paiement).

**Étape 3 — Cluster Reactor**.

Reactor : adresse intégrée à un cluster de **180 adresses** déjà labellisé **« Black Basta operational wallet »** par Chainalysis. Confiance high.

**Bonne nouvelle** : Black Basta est un cluster bien suivi. Patterns documentés. Threat intel disponible.

#### 37.3 Phase 2 — Suivi post-paiement

**Étape 1 — Premier mouvement (J+1)**.

2026-03-11 09:15 UTC : adresse de réception envoie ses 22 BTC vers une **autre adresse Black Basta** (cluster identifié) : `bc1q[BB-ops1]...`. Transaction simple (1 input, 1 output, plus frais).

Hypothèse : rotation OPSEC standard (déplacer fonds après réception pour limiter exposition).

**Étape 2 — Peeling chain (J+2 à J+7)**.

Sur 5 jours, peeling chain avec ~30 hops. Chaque hop : 0,3-1,5 BTC vers adresse externe + reste vers nouvelle adresse Black Basta.

Total éplutchés : ~14 BTC (sur 22).

Reste dans wallet principal : ~8 BTC en mouvement continu.

**Étape 3 — Analyse des branches**.

Chaque output externe est suivi. Catégorisation :

- **6 branches** vers exchanges non-KYC (4 exchanges différents).
- **8 branches** vers Tornado Cash (~5,5 BTC convertis ETH puis dépôts Tornado).
- **5 branches** vers wallets intermédiaires non-attribués (probable layering supplémentaire).
- **3 branches** vers des hubs USDT-TRON (similaire à MIXSHADOW — services de blanchiment partagés).
- **8 branches** vers adresses non encore caractérisées.

**Insight cross-incident** : **2 des 3 hubs TRON** identifiés sont les **MÊMES** que ceux observés dans MIXSHADOW (Akira). Service de blanchiment partagé entre Black Basta et Akira. Confirme l’insight de Sarah dans MIXSHADOW. Thomas alerte Sarah qui complète sa fiche.

#### 37.4 Phase 3 — Caractérisation du cluster Black Basta

**Étape 1 — Examen du cluster Reactor élargi**.

Les 180 adresses du cluster Black Basta (avant le nouveau paiement) montrent :

- ~95 paiements de victimes identifiés sur 8 mois.
- Volumes individuels : 5-150 BTC par paiement.
- Total cumulé reçu : ~1 200 BTC (~70 M EUR équivalent moyen).

**TechIndustrie** est la victime n°96 du cluster (visible).

**Étape 2 — Patterns Black Basta**.

Patterns reconnus :

- Adresses fraîches dédiées par victime.
- Délai paiement → premier mouvement : 12-72h (variable).
- Peeling chain systématique.
- Tornado Cash usage.
- Bridges occasionnels vers BNB Chain.

Patterns cohérents avec opérations Black Basta documentées par Mandiant, CrowdStrike, Sophos en 2024-2025.

**Étape 3 — Threat intel sectoriel**.

Thomas alimente la base CTI Athéna :

- Nouvelles adresses identifiées dans cluster Black Basta.
- Pattern temporel du paiement (cohérent avec autres incidents Black Basta).
- Confirmation usage des hubs TRON partagés (avec Akira).

#### 37.5 Phase 4 — Cashouts et coopération

**Étape 1 — Identification des cashouts**.

À 4 semaines :

- **5 dépôts identifiés sur exchanges régulés** : Binance (3), Kraken (1), Bitstamp (1). Total ~2,3 BTC équivalent USDT (~140 000 EUR au cours).
- **3 dépôts identifiés sur exchange non-KYC** spécifique : ~3,5 BTC. Pas d’angle KYC.
- **Tornado Cash** : ~5,5 BTC. Rupture analytique.
- **Hubs TRON** : ~6 BTC convertis. Layering en cours.
- **Non encore caractérisé** : ~5 BTC.

**Étape 2 — Coordination DGSI / Europol**.

Thomas transmet à la DGSI :

- Liste des 5 adresses sur exchanges régulés (KYC potentiel).
- Liste des adresses Black Basta nouvellement identifiées (alimente fichier Black Basta multi-victimes).
- Insight sur hubs partagés Akira / Black Basta.

DGSI valide. Réquisitions envoyées vers Binance, Kraken, Bitstamp.

**Étape 3 — Retours coopération (à 6 semaines)**.

- Binance : 2 comptes identifiés, ~85 000 EUR équivalent gelés. KYC fournis (deux mules différentes).
- Kraken : 1 compte identifié, ~45 000 EUR équivalent gelés. KYC fourni.
- Bitstamp : 1 compte identifié mais fonds déjà retirés avant gel. KYC fourni mais fonds dispersés.
- Total gelés : ~130 000 EUR équivalent.

**Étape 4 — Tentative gel Tether**.

Pour les flux USDT-TRON via hubs, Tether contacté via DGSI. **Réponse Tether** : étude en cours, gel partiel sur 2 adresses identifiées (~30 000 USDT). Plusieurs autres adresses pas gelées (volume opérationnel Tether limité).

#### 37.6 Phase 5 — Rapport et restitution

**Rapport de 38 pages** :

- Executive summary.
- Cadrage et méthodologie.
- Faits TechIndustrie (timeline, paiement).
- Cartographie des flux (graphes Reactor + Maltego).
- Caractérisation du cluster Black Basta.
- Insight cross-incident (hubs partagés Akira / Black Basta).
- Cashouts identifiés et résultats coopération.
- Recommandations défensives.
- Limites.

**Restitution** :

- Briefing TechIndustrie + cyber-assurance + DGSI : 90 minutes + Q&A.
- Rapport diffusé en TLP RED initialement, puis TLP AMBER pour partage ISAC sectoriel.

#### 37.7 Bilan

✅ **Réussites** :

- Tracking complet sur ~85% des flux.
- Coordination DGSI productive : ~130 000 EUR gelés (sur 1,3 M EUR initial = **~10% récupération nominale**).
- 3 mules identifiées pour enquête judiciaire.
- 30 000 USDT additionnels gelés via Tether.
- Insight cross-incident : confirmation hubs partagés, alimente base CTI.
- Threat intel Black Basta enrichie.

⚠️ **Limites** :

- Tornado Cash : rupture sur ~5,5 BTC.
- Exchange non-KYC : ~3,5 BTC sans angle direct.
- Attribution civile Black Basta : non possible (relevait du FBI / autorités US qui ont opérations en cours).

📊 **Métriques** :

- Durée : 6 semaines.
- Coût : 65 000 EUR.
- Récupération nominale : ~12% (130k EUR + 30k USDT sur 1,3 M EUR).
- ROI cyber-assurance : positif (rapport produit + récupération partielle dépasse coût mission).

**Apprentissage clé** : pour ransomware d’opérateur établi (Black Basta, Akira), la **threat intel cumulative** finit par produire des résultats. L’investissement Athéna sur la base de connaissance interne paie sur le long terme.

-----

### Chapitre 38 — Cas 3 : wallet drain Ethereum par approval phishing

**Profil de l’enquête** : compromission d’un wallet personnel via approval phishing. Mécanisme moderne typique 2023-2026.

#### 38.1 Le contexte

**Victime** : Karim (nom fictif), 38 ans, développeur crypto-enthusiaste. Wallet auto-géré (MetaMask), participe activement DeFi et NFT depuis 2021. Patrimoine crypto estimé à ~280 000 USD au moment des faits.

**L’incident** :

- 2026-04-15 vers 22:30 UTC : Karim navigue sur Discord, suit lien partagé dans une community NFT (« nouveau drop exclusif »).
- Site web crédible imitant marketplace NFT légitime. Karim connecte son MetaMask.
- Site demande signature pour « vérifier l’éligibilité ». Karim signe sans relire attentivement.
- 2026-04-15 22:34 UTC : son wallet est vidé. NFT, ETH, tokens — tout part.

**Pertes** :

- ~12 ETH (~36 000 USD).
- Plusieurs NFT (CryptoPunks #XXXX, Bored Ape #YYYY, autres collections) — valeur estimée ~200 000 USD.
- ~30 000 USDC.
- Plusieurs autres tokens DeFi.
- Total ~280 000 USD.

Karim signale immédiatement à plusieurs outils communautaires (chainabuse, OpenSea pour les NFT volés). Il mandate un cabinet privé pour enquête détaillée et soutien à plainte.

**Mandat** : 4 semaines, 20 000 EUR.

#### 38.2 Phase 1 — Lecture des transactions de drainage

**Étape 1 — Adresse Karim**.

Karim fournit son adresse Ethereum : `0xKarim...`. L’analyste consulte sur Etherscan.

**Étape 2 — Identification des transactions de drainage**.

Sur la dernière demi-heure du 2026-04-15, ~15 transactions sortantes. Toutes vers une **adresse inconnue** : `0xDrainer1...`.

Examen détaillé d’une transaction type :

- TX hash : `0x...drain001`.
- From : `0xKarim`.
- To : `0xDrainer1`.
- Method : `transferFrom` appelé sur le contrat USDC.
- Logs : `Transfer(from=0xKarim, to=0xDrainer1, value=30000 USDC)`.

C’est un **transfer via approval**. Le drainer a appelé `transferFrom` parce que Karim avait préalablement signé un `approve`.

**Étape 3 — Identification de la transaction d’approve**.

L’analyste cherche dans l’historique de Karim juste avant le drainage. Trouve :

- TX hash : `0x...approve001`.
- From : `0xKarim`.
- To : USDC contract.
- Method : `approve`.
- Spender : `0xDrainer1`.
- Amount : `type(uint256).max` (illimité).
- Timestamp : 22:33 UTC (1 minute avant les drainages).

**Confirmation** : Karim a approuvé un montant illimité au drainer 1 minute avant. Pattern classique d’approval phishing.

#### 38.3 Phase 2 — Analyse du drainer

**Étape 1 — Caractérisation `0xDrainer1`**.

`0xDrainer1` est analysé. Smart contract (l’analyste vérifie sur Etherscan onglet « Contract »).

**Code source vérifié** : oui, le drainer a publié son code Solidity. Analyse rapide :

- Fonctions `transferFromAll(token, victim)` qui appellent `transferFrom` avec les approvals existants.
- Fonctions de retrait pour l’opérateur.
- Pas d’audit, pas de réputation.

**Activité** :

- Smart contract déployé il y a 6 mois.
- A été utilisé par ~340 victimes différentes selon analyse Etherscan.
- Volume cumulé : ~14 M USD équivalent (estimations).

**Reconnaissance du drainer service**.

Le code et les patterns du drainer correspondent à un service connu : **« Inferno Drainer »** (drainer-as-a-service identifié par chercheurs comme @scamsniffer en 2023). Il a évolué : variantes successives, multiples déploiements.

L’analyste note : Karim n’est pas victime d’un attaquant individuel, mais d’un **service utilisé par un affilié** d’Inferno Drainer (le service prend une commission, les affiliés font la distribution / le phishing).

#### 38.4 Phase 3 — Suivi des fonds

**Étape 1 — Consolidation drainer**.

Sur les 30 minutes post-drainage, `0xDrainer1` consolide vers `0xDrainerOps1` (wallet opérationnel de l’affilié) :

- ETH : 12 ETH → `0xDrainerOps1`.
- USDC : 30 000 → `0xDrainerOps1`.
- Tokens autres : converti via DEX (1inch) en ETH d’abord.
- NFT : transférés à `0xDrainerOps1` en l’état.

**Étape 2 — Suivi des NFT**.

NFT sont **traçables** publiquement (chaque NFT a un ID unique, leur historique est visible).

À J+3, les NFT sont listés sur OpenSea (depuis `0xDrainerOps1`) à des prix bas. Karim et ses contacts dans la communauté ont alerté OpenSea : les **NFT sont gelés** sur OpenSea (delisted, non-transférables sur la marketplace).

Mais : sur d’autres marketplaces moins coopératives, NFT sont vendus. À J+10, ~60% des NFT ont été vendus à des acheteurs tiers (qui les ont peut-être achetés sans savoir qu’ils sont volés).

Récupération des NFT : **complexe juridiquement**. Acheteurs tiers de bonne foi peuvent revendiquer propriété. Procédure longue.

**Étape 3 — Suivi des fonds liquides**.

ETH + USDC : `0xDrainerOps1` consolide :

- Étape A : swap USDC → ETH via Uniswap (J+0).
- Étape B : split en 4 sub-adresses (J+1).
- Étape C : 2 sub-adresses → Tornado Cash (~12 ETH au total).
- Étape D : 2 sub-adresses → bridge Stargate vers BNB Chain.
- Étape E : sur BNB, dispersion vers exchanges non-KYC.

Pattern d’obfuscation classique. ~70% via Tornado Cash, 30% via bridge.

#### 38.5 Phase 4 — Identification de l’affilié

**Étape 1 — `0xDrainerOps1` historique**.

`0xDrainerOps1` n’est pas seulement utilisé pour Karim. Analyse révèle :

- Adresse active depuis 4 mois.
- A consolidé fonds de **~80 victimes** différentes.
- Volume cumulé : ~3,2 M USD équivalent.

**Étape 2 — Patterns affilié**.

Patterns observables :

- Quelques fois par semaine, drainages.
- Fonds disparaissent rapidement (Tornado Cash, bridges).
- Adresse de payment de **service Inferno Drainer** : ~10% des fonds reversés à une adresse spécifique du service (commission).
- Pas d’erreur OPSEC visible (pas de réutilisation, pas de mention publique).

**Étape 3 — Possibilité d’attribution**.

Affilié reste **anonyme** au sens civil. Patterns suggèrent acteur expérimenté.

Pas de fonds vers exchange régulé identifié — l’affilié maintient OPSEC stricte.

**Recoupement Inferno Drainer général** : selon @scamsniffer et reports vendor, certains affiliés Inferno Drainer ont été identifiés (Telegram handles, infrastructure leaks). Pour cet affilié spécifique, pas de match identifiable dans les sources publiques au moment de l’enquête.

#### 38.6 Phase 5 — Coopération et action

**Étape 1 — OpenSea**.

NFT volés signalés. OpenSea a délisté les NFT compromis. **Action partielle** : les acheteurs tiers ne peuvent plus les revendre sur OpenSea. Mais marketplaces alternatives (Blur, X2Y2 historique) moins coopératives.

**Étape 2 — Coordination autorités**.

Plainte de Karim auprès de la gendarmerie. L’analyste fournit son rapport. Coordination via gendarmerie cyber → Pharos → potentiel relais vers FBI Cyber Division (drainer service est multi-juridictionnel).

**Étape 3 — Communauté**.

Information partagée sur Chainabuse. ScamSniffer alerté avec nouvelles indications sur le drainer / affilié. Alimente la base communautaire.

#### 38.7 Phase 6 — Rapport et restitution

**Rapport de 25 pages** :

- Executive summary.
- Méthodologie.
- Faits Karim (timeline précise — minutes).
- Mécanisme du drainer (analyse Solidity).
- Suivi des fonds.
- Identification de l’affilié et du service.
- Limites.
- Recommandations.

**Recommandations à Karim** :

- Action prioritaire : révoquer **tous les approvals existants** sur tous ses wallets via revoke.cash.
- Migration vers nouveau wallet (assumer compromission seed phrase est peu probable mais prudent).
- Hardware wallet pour fonds significatifs.
- Vigilance sur signatures (lire toujours le détail).
- Suivre la procédure judiciaire ; espoir limité de récupération.

**Recommandations communauté** :

- Signaler le service de drainer aux outils anti-phishing.
- Alerter chercheurs (scamsniffer) avec données enrichies.

#### 38.8 Bilan

✅ **Réussites** :

- Reconstitution complète du mécanisme.
- Identification du drainer-as-a-service utilisé.
- Identification de l’affilié (en tant que cluster, pas personne).
- ~60% des NFT délistsés OpenSea (limites valorisation).
- Alimentation base communautaire anti-phishing.

⚠️ **Limites** :

- Récupération financière improbable sans coopération internationale exhaustive.
- 70% des fonds liquides perdus dans Tornado Cash.
- Affilié reste anonyme.
- Acheteurs NFT tiers de bonne foi posent problème juridique pour récupération.

📊 **Métriques** :

- Durée : 4 semaines.
- Coût : 20 000 EUR.
- Récupération : indirecte (NFT délistsés sur OpenSea, mais valeur incertaine).

**Apprentissage clé** : pour wallet drain individuel, l’enquête **caractérise** mais récupère rarement. Valeur principale = clarification pour la victime et alimentation communauté.

-----

### Chapitre 39 — Cas 4 : flux multi-chaînes avec bridge et stablecoins

**Profil de l’enquête** : enquête sur une fraude internationale (intermédiaire commercial frauduleux) impliquant flux multi-chaînes complexes. Cas qui montre la complexité de l’enquête moderne.

#### 39.1 Le contexte

**Société victime** : « ImportExport SAS » (nom fictif), ETI française d’import-export de matériels électroniques, ~50 employés, CA ~25 M EUR/an.

**L’incident** :

ImportExport est cliente d’un fournisseur asiatique (Vietnam). Pour un contrat de 800 000 USD, négociation avec interlocuteur habituel (M. Tran, directeur achat, ImportExport est en relation depuis 3 ans).

Mi-février 2026, M. Tran annonce changement de procédure de paiement : fournisseur a souffert de problèmes bancaires (sanctions banques vietnamiennes liées à un autre dossier), nouvelle procédure : paiement en **USDT-Tron** vers une adresse fournie. Justification crédible. Email de confirmation reçu sur l’adresse habituelle de M. Tran.

Mi-février 2026 : ImportExport convertit 800 000 USD en USDT (via partenaire crypto OTC français régulé) et transfère vers l’adresse fournie.

Une semaine plus tard, contact direct au téléphone avec M. Tran (pas à Tran officiel mais à son standard) : Tran n’a **jamais demandé de paiement crypto**. Compromission de son email professionnel découverte. ImportExport est **victime de BEC (Business Email Compromise)** sophistiquée — avec demande de paiement détournée vers crypto.

**Mandat** : ImportExport mandate un cabinet pour cartographier les flux et soutenir plainte. Coopération avec autorités françaises ET vietnamiennes (M. Tran réel coopère également pour son côté). 6 semaines, 50 000 EUR.

#### 39.2 Phase 1 — Lecture initiale

**Inputs** :

- TXID du transfert USDT-TRON.
- Adresse destinataire : `TR[fraud-receive]...`.
- Email frauduleux et son origine technique.

**Étape 1 — Vérification on-chain**.

Tronscan : 800 000 USDT transférés à 2026-02-18 09:43 UTC vers `TR[fraud-receive]...`.

Adresse fraîche, première activité = ce transfert. Suggère adresse dédiée à cette fraude.

**Étape 2 — Suite immédiate**.

À 2026-02-18 11:15 UTC (90 minutes après réception), `TR[fraud-receive]` envoie l’intégralité (800 000 USDT) vers `TR[fraud-ops1]`.

Délai bref : opérateur supervise le compte ou bot automatique.

#### 39.3 Phase 2 — Cascade multi-chaîne

**Étape 1 — Mouvement TR[fraud-ops1]**.

À 2026-02-18 12:30 UTC, `TR[fraud-ops1]` :

- Conserve 200 000 USDT-TRON.
- Convertit 600 000 USDT-TRON via SunSwap DEX en TRX puis re-swap en USDT-Ethereum via service de swap cross-chain (FixedFloat ou équivalent).

Le swap cross-chain est **traçable** mais demande matching manuel : USDT-TRON sortie sur TRON, USDT-Ethereum entrée sur Ethereum quelques minutes plus tard.

**Étape 2 — Sur Ethereum**.

À 2026-02-18 13:45 UTC, 600 000 USDT-Ethereum reçus sur `0x[fraud-eth1]...`.

Quelques minutes plus tard :

- 300 000 USDT-Ethereum → bridge **Stargate** vers BNB Chain.
- 300 000 USDT-Ethereum → swap via Uniswap en ETH (~85 ETH au cours du moment).

**Étape 3 — Sur BNB Chain**.

USDT-BNB reçus. Quelques minutes plus tard, swap en BUSD via PancakeSwap.

BUSD transférés en 5 sub-adresses (60 000 BUSD chaque). Patterns de dispersion.

**Étape 4 — Sur Ethereum (suite swap ETH)**.

85 ETH dans `0x[fraud-eth1]`. Sur les 24h suivantes :

- 50 ETH déposés en 5 dépôts vers Tornado Cash (10 ETH × 5).
- 25 ETH transférés vers `0x[fraud-eth2]`.
- 10 ETH consolidés vers wallet opérationnel.

#### 39.4 Phase 3 — Cartographie complète

**À 1 semaine** : l’analyste a reconstitué la cascade :

```
ImportExport (800k USDT-TRON)
    ↓
TR[fraud-receive] (90 min)
    ↓
TR[fraud-ops1]
    ↓ split:
    ├── 200k USDT-TRON (reste sur TRON, dispersion vers hubs)
    └── 600k → cross-chain
              ↓
         0x[fraud-eth1] sur Ethereum
              ↓ split:
              ├── 300k → Stargate → BNB Chain → BUSD → 5 sub-addresses
              └── 300k → Uniswap swap → 85 ETH
                        ↓ split:
                        ├── 50 ETH → Tornado Cash
                        ├── 25 ETH → 0x[fraud-eth2]
                        └── 10 ETH → consolidation
```

**Outils utilisés** : Reactor pour suivi automatique, validation manuelle sur Etherscan / Tronscan / BscScan, Stargate Finance pour matching cross-chain.

**Étape — Caractérisation des destinations finales** (à 4 semaines) :

**Sur TRON** (200k USDT) :

- Layering via 6 hops jusqu’à dépôts vers exchange asiatique non-KYC.
- ~150k USDT cumulés identifiés sur exchange Y.

**Sur BNB Chain** (300k USDT puis BUSD) :

- 5 sub-adresses → consolidation puis dépôts Binance (KYC).
- 5 dépôts Binance identifiés totalisant ~280k BUSD.

**Sur Ethereum** :

- Tornado Cash (~50 ETH = ~150k USD équivalent) : rupture de visibilité.
- `0x[fraud-eth2]` → bridge vers Polygon → swap → consolidation. ~75k USD équivalent suivi jusqu’à dépôts Coinbase Pro.
- Consolidation 10 ETH : reste dormant, pas de mouvement à 4 semaines.

#### 39.5 Phase 4 — Coopération et identification

**Étape 1 — Binance (BNB Chain dépôts)**.

DGSI envoie réquisition à Binance pour les 5 dépôts BNB Chain.

Retour Binance (3 semaines plus tard) :

- 5 comptes identifiés, KYC complets.
- 4 mules : individus en Asie du Sud-Est avec patterns de mules (comptes ouverts récemment, multiple flux de dépôts crypto, retraits rapides).
- 1 compte semble-t-il du « cerveau » : individu en Russie (KYC valide), ~80k BUSD récupérés (gel) avant retrait.
- Total gelé Binance : ~80k EUR équivalent.

**Étape 2 — Coinbase Pro (75k USD via Polygon)**.

Réquisition Coinbase. Retour : 1 compte, mule en Roumanie. Fonds déjà retirés. Pas de gel.

**Étape 3 — Exchange non-KYC asiatique**.

Pas de coopération directe. Sanctions évaluées par DGSI mais procédures internationales lentes.

**Étape 4 — Email frauduleux**.

Forensics email coordonnée avec FAI vietnamien : compromission révèle malware infostealer sur poste de M. Tran ayant volé credentials email il y a 3 mois. **Pas un acteur étatique** — fraude opportuniste par groupe BEC.

Patterns techniques cohérents avec **groupe BEC russophone** (même infrastructure / même style de messages que d’autres incidents BEC documentés). Attribution **probable** russophone, mais pas plus précis.

#### 39.6 Phase 5 — Bilan

**Total tracé** : ~625k USD sur 800k initial (78%).

**Total gelé / récupéré** : ~80k EUR (Binance, ~10% du total).

**Tornado Cash** : ~150k USD perdus dans rupture analytique.

**Exchange non-KYC asiatique** : ~150k USDT, possible récupération via coopération internationale ultérieure.

**Identification** :

- 4 mules identifiées (utiles pour enquête judiciaire).
- 1 acteur principal en Russie (KYC fourni).
- Profil acteur principal : russophone, BEC professionnel.

#### 39.7 Rapport et action

**Rapport de 42 pages** :

- Executive summary.
- Méthodologie.
- Reconstitution timeline complète.
- Cartographie multi-chaînes (graphes Reactor + Maltego).
- Identifications et coopérations.
- Recommandations.
- Limites.

**Recommandations à ImportExport** :

- Sécurisation des emails (MFA, monitoring).
- Procédure de validation pour changements de paiement (téléphone direct + canal indépendant).
- Formation des équipes finance.
- Cyber-insurance évaluation.

**Recommandations autorités** :

- Soutenir procédure judiciaire avec pièces fournies.
- Coopération DGSI / Vietnam / Russie selon accords bilatéraux.
- Sanctions OFAC évaluation pour exchange non-KYC asiatique.

#### 39.8 Bilan honnête

✅ **Réussites** :

- Cartographie multi-chaînes complète (BTC → ETH → BNB → Polygon).
- Identification de 5 KYC (4 mules + 1 acteur principal).
- 80k EUR gelés.
- Profil acteur établi.

⚠️ **Limites** :

- 22% des flux non tracés (Tornado Cash, exchange non-KYC).
- Récupération limitée à ~10%.
- Acteur principal en Russie : peu coopération attendue.

**Apprentissage clé** : pour fraude multi-chaîne sophistiquée, l’enquête est **fastidieuse mais payante**. Les outils pro permettent le tracking cross-chain. La coopération exchanges régulés finit par produire des KYC. Le bilan financier est modeste mais le bilan **renseignement** est solide.

-----

### Chapitre 40 — Cas 5 : enquête Monero — quand la blockchain ne suffit pas

**Profil de l’enquête** : enquête honnête sur un cas où Monero rompt la traçabilité on-chain. Cas pédagogique pour montrer comment **gérer la rupture** et déplacer l’enquête vers les angles off-chain.

#### 40.1 Le contexte

**Société victime** : « SantéTech » (nom fictif), startup française BioTech (~80 employés), produit logiciel de gestion hospitalière. Compromise en mars 2026 par un opérateur ransomware **Helldown** (variante émergente de la galaxie Akira / Babuk).

**L’incident** :

- Compromission via vulnérabilité VPN Fortinet non patchée.
- Chiffrement le 2026-03-22.
- Helldown demande **35 XMR** (~6 000 USD au cours, mais valeur de levier psychologique liée à la criticité).

**Décision** : SantéTech décide de payer (impossibilité de reprise rapide, données sensibles en jeu — patients).

**Mais** : Helldown exige **Monero** (XMR). Pas de Bitcoin accepté.

**Conséquences** :

- SantéTech doit acquérir 35 XMR.
- L’acquisition se fait via partenaire crypto OTC français : conversion EUR → XMR via service partenaire (LocalMonero était option mais fermé en 2024 ; alternatives autres).
- Paiement effectué le 2026-03-25.
- Réception clé déchiffrement.

**Mandat** : SantéTech mandate Athéna pour « tenter de tracer ces 35 XMR autant que possible et identifier des angles d’action ». Sarah Marin (qui a déjà MIXSHADOW en cours) est consultée pour le cadrage. **Constat dès le départ** : Monero = traçabilité on-chain quasi-nulle. Sarah déconseille un mandat « tracking complet » mais propose un mandat différent — caractérisation Helldown + analyses des points off-chain.

**Mandat révisé** : 3 semaines, 25 000 EUR, focus sur :

1. Documenter ce qui peut l’être on-chain (rare).
1. Caractériser le profil Helldown.
1. Identifier les points off-chain potentiellement exploitables.
1. Coordonner avec autorités sur l’écosystème Helldown plus large.

#### 40.2 Phase 1 — Documenter la transaction Monero

**Étape 1 — TXID Monero**.

SantéTech fournit le TXID Monero de la transaction de paiement.

Sur explorateurs Monero (xmrchain.net, etc.) :

- TXID confirmée.
- Date / heure.
- **Mais** : pas de visibilité sur expéditeur (ring signatures), pas de visibilité sur destinataire (stealth address), pas de visibilité sur montant exact (RingCT) — sauf information transmise hors-chain par les parties.

SantéTech a la « view key » de sa propre transaction (donnée par leur wallet) qui permet de **vérifier qu’ils ont bien envoyé X XMR**. Mais pas de visibilité sur ce qui se passe ensuite.

**Étape 2 — Limite explicite**.

L’analyste documente : « La transaction de 35 XMR est confirmée par les view keys de SantéTech. Au-delà de la réception par Helldown, la traçabilité on-chain Monero n’est pas possible. »

#### 40.3 Phase 2 — Tracer les XMR avant le paiement

**Insight** : si on ne peut pas tracer les XMR **après** le paiement, on peut tenter de tracer **comment** SantéTech a obtenu les 35 XMR.

**Pourquoi utile ?**

- Les XMR ont été **achetés** via un service OTC français.
- Le service OTC a obtenu ces XMR de quelque part.
- Si on remonte la chaîne d’origine, on pourrait identifier des patterns.

Mais pour ce cas spécifique : les XMR achetés par SantéTech proviennent d’un service OTC légitime — origine sans intérêt pour l’enquête Helldown (qui a reçu les XMR, pas envoyé).

#### 40.4 Phase 3 — Pivot vers caractérisation Helldown

**Étape 1 — Recherche threat intel publique**.

Helldown est un opérateur récent (apparition fin 2024 / début 2025). Caractérisation par vendor reports :

- TRM Labs publication 2025 mentionne Helldown comme variante de la « galaxie Akira ».
- Mandiant / CrowdStrike : Helldown analysé. Codebase partagé avec Babuk leak 2021. Probable acteur(s) ayant adapté.
- Patterns de victimes : santé, manufacturing, ETI.
- Demandes de paiement : Bitcoin et **Monero** (préférence Monero affichée).
- Leak site Helldown actif sur Tor.

**Étape 2 — Recherche du leak site Helldown**.

Sur Tor, le leak site Helldown affiche ~25 victimes publiées (sur 8 mois d’activité). SantéTech n’y figure pas (paiement effectué, donc pas publication).

Captures du leak site (méthode Dark Web cours associé) :

- Liste des victimes.
- Statistiques de paiement (revendiquées).
- Communications avec victims (portail de négociation séparé).

**Étape 3 — Patterns Helldown**.

Caractérisation :

- Volume modéré (vs LockBit historique ou Black Basta).
- Cible de niche (souvent santé / éducation).
- Demandes monétaires modérées (3-50k USD typique).
- Préférence Monero **forte**.
- Communications professionnelles via portail Tor.

**Étape 4 — Hypothèse profil opérateur**.

Patterns suggèrent :

- Opérateur moins sophistiqué que LockBit / Black Basta.
- Possible affilié individuel ou petit groupe.
- Préférence Monero suggère **conscience forensique** — l’opérateur sait que Bitcoin se trace, choisit Monero pour rupture analytique.

Pas d’attribution civile possible.

#### 40.5 Phase 4 — Angles off-chain

**Angle 1 — Communications Helldown / SantéTech**.

Le portail Tor de Helldown a été utilisé pour négociation (passage de demande initiale à l’accord 35 XMR). Le portail est **observable** (URL .onion documentée).

Communications archivées par SantéTech (captures du portail) :

- Style : anglais correct, idiomatique. Pas de patterns linguistiques évidents.
- Délais de réponse : 4-24h, suggère opérateur seul ou petite équipe.
- Concession sur prix : flexibilité. Suggère acteur opportuniste (préfère paiement modéré à pas de paiement).

Pas de leak OPSEC évident dans les communications.

**Angle 2 — Vecteur d’attaque**.

Forensics SantéTech (par Mandiant) : compromission via Fortinet vulnerability. Patterns techniques :

- Outils utilisés : Cobalt Strike, Mimikatz, AnyDesk (LotL), Rclone pour exfiltration.
- C2 infrastructure : 2 IP utilisées (l’une saisie depuis par autorités sur autre dossier).

**Insight** : croisement avec autre dossier (saisie C2 IP). Possible coordination DGSI sur dossier multi-victimes Helldown si autres victimes françaises identifiées.

**Angle 3 — Service OTC Monero**.

Question hypothétique : Helldown va probablement convertir les XMR en autre actif (USDT, BTC) à un moment via service OTC ou exchange. Si l’opérateur utilise un service identifiable pour cette conversion, angle de coopération.

L’analyste n’a pas accès aux flux post-paiement (Monero opaque), mais documente les **services Monero** populaires (LocalMonero historique, autres) et propose à DGSI de **monitorer ces services pour transactions cohérentes** avec timing post-paiement Helldown — analyse statistique probabiliste.

**Angle 4 — Profil Helldown plus large**.

Recoupements multi-source :

- Vendor reports (Mandiant, TRM, Elliptic).
- Communications victimologie (autres victimes Helldown identifiées via leak site).
- Discussions communauté CTI (FIRST, ISACs).

**Étape 5 — Coordination avec autres victimes**.

L’analyste note que **2 autres victimes Helldown** sont identifiées dans la communauté CTI française (sans nom, par discrétion). DGSI peut potentiellement consolider une vue **multi-victimes Helldown** pour orienter enquête plus large.

Athéna soumet à DGSI une **demande de coordination** : si plusieurs victimes Helldown coopèrent ensemble, des signaux convergents peuvent émerger qui dépassent ce qu’une enquête isolée peut voir.

#### 40.6 Phase 5 — Rapport et limites

**Rapport de 18 pages** (volontairement plus court — moins à dire qu’avec Bitcoin) :

- Executive summary.
- Cadrage et limitations Monero (section dédiée explicite).
- Documentation transaction de paiement (limitée).
- Caractérisation Helldown (section principale du rapport).
- Angles off-chain explorés.
- Recommandations.
- Limites assumées.

**Section limites prend une place importante** :

> « En raison de l’usage de Monero pour le paiement, la traçabilité on-chain est intrinsèquement limitée. Le rapport documente ce qui peut l’être (transaction de paiement par view key SantéTech, profil Helldown via threat intel publique, angles off-chain identifiés) et expose honnêtement ce qui ne peut pas l’être (chemin des fonds post-paiement, identification des comptes Helldown sur exchanges, attribution civile). Cette enquête contribue à la threat intel sectorielle et à la coordination autorités, mais ne produit pas de récupération financière ni d’attribution personnelle. »

**Recommandations à SantéTech** :

- Rapport transmis à plainte (procédure judiciaire enregistrée).
- Considérer cyber-insurance pour incidents futurs.
- Mesures défensives durcies (patch management Fortinet, MFA, segmentation, EDR avancé).
- Plan IR pour incidents futurs.

**Recommandations DGSI** :

- Coordination multi-victimes Helldown (Athéna identifie 2 autres victimes potentielles via communauté CTI).
- Surveillance des services Monero pour patterns cohérents.
- Coordination internationale (Helldown a victimes US, UE, Asie).

#### 40.7 Bilan

✅ **Réussites** :

- Caractérisation profil Helldown.
- Identification du contexte plus large (multi-victimes Helldown documentées).
- Mandat **réaliste** dès le départ — pas de fausse promesse de tracking.
- Coordination DGSI productive sur dossier multi-victimes.
- Threat intel sectorielle enrichie.

⚠️ **Limites assumées dès le mandat** :

- Pas de tracking on-chain au-delà de la transaction de paiement.
- Pas d’identification civile.
- Pas de récupération.

📊 **Métriques** :

- Durée : 3 semaines (volume modeste vs cas Bitcoin).
- Coût : 22 000 EUR (sur 25 000 budgétés).
- Couverture : limitée par nature Monero. Mais 100% de ce qui était possible.

#### 40.8 Apprentissage clé

**Pour Monero, l’enquête est différente** :

1. **Mandat doit être réaliste**. Cf cadrage révisé. Le client doit comprendre **dès le départ** que tracker Monero on-chain n’est pas possible.
1. **L’enquête se déplace off-chain**. Profil acteur, vecteurs, infrastructure, communications, services off-chain — tout sauf on-chain pure.
1. **Valeur = renseignement et coordination**. Pas récupération.
1. **Calibration honnête essentielle**. Le rapport ne « tente pas » de faire passer pour acquis ce qui ne l’est pas.
1. **Coordination multi-source amplifie**. Une victime isolée a peu d’angles ; multi-victimes consolidées peuvent révéler des patterns convergents.

**Pour l’analyste OSINT** : refuser un mandat « tracker mes XMR » est parfois la décision **professionnellement correcte**. Proposer un mandat alternatif réaliste préserve la crédibilité et apporte de la valeur.

#### 40.9 Synthèse Partie VII

Cinq cas, cinq typologies, cinq logiques d’enquête :

1. **Pig butchering USDT-TRON** : cartographie d’écosystème, identification de co-victimes, peu de récupération.
1. **Ransomware BTC** : tracking systématique, threat intel cumulative, récupération partielle via exchanges régulés.
1. **Wallet drain Ethereum** : reconstitution mécanisme, identification du service drainer, récupération limitée.
1. **Multi-chaînes BEC** : tracking cross-chain complexe, coopération internationale, récupération modeste.
1. **Monero ransomware** : reconnaissance des limites, pivot off-chain, valeur en renseignement.

**Patterns transverses** :

- **Récupération nominale** souvent **5-15%** dans les meilleurs cas, **0%** dans certains.
- **Identification civile** rare en OSINT pur.
- **Threat intel et coordination** sont la valeur principale.
- **Calibration honnête** maintient la crédibilité.

La Partie VIII va aborder des **cas historiques réels emblématiques** où des enquêtes complètes ont permis des saisies majeures. Ces cas montrent ce qui est possible **avec ressources, coopération internationale, et persévérance** sur des années.

-----

## PARTIE VIII — CAS HISTORIQUES EMBLÉMATIQUES

> **Ce que cette partie apprend.** Quatre cas historiques majeurs où l’enquête crypto a abouti à des résultats marquants : la saisie Bitfinex (3,6 Mrd USD), la récupération Colonial Pipeline, le hack Ronin par Lazarus, et la saga Tornado Cash. Pour chaque cas : faits, méthodes employées, résultats, leçons. Synthèse finale du fil rouge MIXSHADOW.
> 
> **Ce qu’elle ne couvre pas.** Cas pratiques didactiques (Partie VII), production de rapport (Partie IX).
> 
> **Ce que vous saurez faire après cette partie.** Mobiliser ces cas comme références pour benchmark, formation, et communication. Comprendre ce qui est possible avec ressources, coopération internationale et temps long.

> **Note importante** : ces cas sont basés sur des informations publiquement disponibles (DOJ press releases, indictments unsealed, rapports vendor publics). Les chiffres et faits sont sourcés à la date de rédaction (2026). Pour utilisation professionnelle, vérifier les évolutions ultérieures (procédures en cours, appels, jurisprudence).

-----

### Chapitre 41 — Bitfinex 2016 → saisie 3,6 Mrd USD 2022

Le hack Bitfinex de 2016 et la saisie de 2022 constituent le **plus gros cas de récupération crypto** documenté à ce jour. Six ans entre le vol et la saisie. Démonstration que la traçabilité on-chain, combinée à la persévérance et la coopération, peut aboutir.

#### 41.1 Le hack — août 2016

**Faits** :

- 2 août 2016 : Bitfinex (exchange majeur, basé à Hong Kong) annonce avoir été piraté.
- **119 756 BTC** volés (~72 M USD au cours de l’époque, ~7,2 Mrd USD au cours record post).
- Vecteur précis : compromis multi-signature wallet via failles d’implémentation BitGo (debate technique sur la responsabilité, jamais entièrement clarifié publiquement).
- Bitfinex socialise les pertes : haircut de 36% sur tous les comptes utilisateurs, émission de tokens BFX comme dette.

**Adresses** :

- 119 756 BTC sont **disséminés** entre 2 000+ adresses fraîches dans les heures suivant le hack.
- Ces adresses restent ensuite **largement dormantes** pendant des années.

**Suivi** :

- Communauté Bitcoin et chercheurs (notamment **Sergej Kotliar**, Alec Ziupsnys, et plus tard Chainalysis, Elliptic) **monitor les wallets**.
- Quelques mouvements occasionnels (petites sommes) entre 2016 et 2022, surveillés.
- Bitfinex offre des récompenses pour informations.

#### 41.2 La saisie — février 2022

**Annonce DOJ — 8 février 2022** :

- **Heather « Razzlekhan » Morgan** et **Ilya « Dutch » Lichtenstein**, couple à Manhattan, arrêtés.
- Chargés de **conspiracy to commit money laundering** et **conspiracy to defraud the United States**.
- DOJ saisit **94 636 BTC** (sur les 119 756 originaux), valorisés à **3,6 Mrd USD** au cours de l’époque.

**Méthode d’investigation reconstituée** (depuis l’indictment unsealed et investigations journalistiques) :

**Étape 1 — Long monitoring**. Les adresses du hack sont surveillées par autorités et chercheurs depuis 2016. Quelques mouvements occasionnels alimentent le dossier.

**Étape 2 — Patterns émergent**. À partir de 2020-2021, des **mouvements plus actifs** émergent. Lichtenstein utilise progressivement les fonds via :

- AlphaBay (darknet market, saisi en 2017 — son historique permet aux autorités d’extraire des liens).
- Multiple exchanges (avec KYC pour certains).
- Mixers (Bitcoin Fog notamment).

**Étape 3 — KYC sur exchanges**. Lichtenstein dépose une **partie** des fonds sur exchanges utilisant **identités réelles** (lui ou Morgan, ou liens identifiables). Erreur OPSEC critique.

**Étape 4 — Décrypter l’infrastructure**. Le DOJ exécute un mandat de perquisition sur le **cloud storage** de Lichtenstein (Cloud account). Le cloud contenait un fichier chiffré avec **les clés privées des wallets contenant ~94 636 BTC**.

Le fichier était sécurisé par mot de passe. Le DOJ accède au mot de passe (modalités précises peu détaillées publiquement — possible exploitation cloud, possible recovery via partner, possible cryptanalyse). Décryption permet **prise de contrôle** des wallets et saisie effective.

**Étape 5 — Saisie**. 94 636 BTC transférés depuis les wallets compromis vers wallet contrôlé par US gouvernement.

**Étape 6 — Inculpation**. Indictment publié, charges expliquées, fonds publiquement annoncés.

#### 41.3 Le procès — 2023-2024

**Lichtenstein** : plaide coupable en août 2023 pour conspiracy to commit money laundering et fraud against the United States.

**Morgan** : plaide coupable au même moment pour conspiracy.

**Sentencing** :

- **Lichtenstein** : condamné en novembre 2024 à 5 ans de prison.
- **Morgan** : condamnée en novembre 2024 à 18 mois de prison.

**Restitution** : les BTC saisis vont en partie à la restitution des victimes (utilisateurs Bitfinex de 2016 ayant subi le haircut). Procédure complexe étant donné l’évolution de la valeur (BTC valait ~600 USD en 2016, ~40-70k en 2024).

#### 41.4 Méthodes mobilisées

**Tracking on-chain de longue durée** :

- Surveillance des adresses pendant 6 ans.
- Identification des mouvements progressifs.
- Outils : Chainalysis Reactor, monitoring custom, communauté.

**Saisies antérieures comme inputs** :

- AlphaBay saisi en 2017 a fourni données utilisées pour le dossier Bitfinex.
- Bitcoin Fog saisi 2021, idem.

**KYC exchange** :

- Erreurs OPSEC de Lichtenstein/Morgan exposant identité.

**Cloud forensics** :

- Mandat de perquisition sur le cloud account.
- Décryption des fichiers stockés.

**Coopération internationale** :

- DOJ + FBI + IRS + autres agences US.
- Coopération avec exchanges concernés.

**Persévérance institutionnelle** :

- 6 ans de monitoring patient.

#### 41.5 Leçons

**Pour les criminels (perspective des autorités)** :

- **Long terme = vulnérabilité**. Les adresses « tranquilles » pendant des années deviennent **incentive croissant** à mauvaise OPSEC quand l’opérateur tente de monétiser.
- **Erreurs OPSEC se cumulent**. Une seule erreur sur 6 ans suffit (KYC exchange, cloud non-sécurisé, etc.).
- **Cryptographie protège les fonds, pas les humains**. Lichtenstein avait techniquement les clés privées — mais ses **comptes utilisateur** étaient compromis par perquisition.

**Pour les enquêteurs** :

- **Patience institutionnelle** : LEA peuvent maintenir surveillance pendant des années.
- **Recoupement multi-source** : crypto + cloud + exchange KYC + saisies antérieures.
- **Volume justifie l’investissement** : 3,6 Mrd USD justifie ressources LEA significatives.

**Pour les analystes** :

- **Documentation longitudinale** des wallets criminels alimente les cas futurs.
- **Le « cold storage » pendant des années** ne signifie pas « impossible à saisir ».

**Pour les victimes** :

- **Récupération possible mais lente**. Bitfinex est exemple. Beaucoup d’incidents ne aboutissent pas comme cela.

#### 41.6 Bitfinex aujourd’hui

À 2026 :

- Procédure de restitution toujours en cours pour utilisateurs originaux.
- Bitfinex a survécu à l’incident, reste exchange actif (et Tether y est lié).
- Cas étudié dans formations forensiques (Chainalysis utilise comme étude de cas).

-----

### Chapitre 42 — Colonial Pipeline 2021 — récupération FBI

Le cas **Colonial Pipeline** est emblématique pour deux raisons : impact géopolitique majeur (perturbation infrastructure US critique), et **récupération significative** des fonds par le FBI dans des délais courts.

#### 42.1 Les faits

**Colonial Pipeline** : opérateur de pipelines de carburant US, fournit ~45% du fuel de la côte Est des États-Unis.

**Mai 2021** :

- 7 mai 2021 : Colonial Pipeline découvre compromission par ransomware.
- Vecteur : compte VPN avec mot de passe fuité (sans MFA).
- Auteur : groupe **DarkSide** (RaaS d’origine russophone).
- Décision : Colonial paie **75 BTC** (~4,4 M USD au cours du moment).
- Paiement effectué le 8 mai 2021.
- Décryption key reçue, mais **lente** — Colonial restaure depuis backups en parallèle.

**Impact** :

- Pipeline arrêté plusieurs jours.
- Pénuries de carburant côte Est.
- Réaction politique : Joe Biden émet executive order sur cybersécurité (12 mai 2021).
- Pression sur DarkSide qui annonce sa dissolution officielle (probable rebranding).

#### 42.2 La récupération — juin 2021

**Annonce DOJ — 7 juin 2021** :

- **63,7 BTC saisis** (sur 75 payés).
- Valeur au moment de la saisie : ~2,3 M USD (Bitcoin avait baissé entre mai et juin).
- FBI a obtenu accès à la clé privée du wallet contenant ces fonds.

**Méthode** (selon DOJ press release et analyse publique) :

**Étape 1 — Tracking immédiat post-paiement**. FBI suit les BTC payés via Chainalysis dès la transaction.

**Étape 2 — Identification d’un wallet de réception**. Les fonds atterrissent finalement (via plusieurs hops) sur une adresse spécifique contrôlée par un membre de DarkSide.

**Étape 3 — Obtention de la clé privée**. C’est l’élément le plus opaque publiquement. DOJ indique avoir **obtenu la clé privée**. Modalités jamais entièrement explicitées :

- Hypothèse 1 : cloud storage compromis (similaire à Bitfinex).
- Hypothèse 2 : opération sur infrastructure DarkSide (qui était pressurée par autorités à ce moment).
- Hypothèse 3 : informations d’un insider DarkSide (members défectant).
- Hypothèse 4 : exploitation de vulnérabilités dans wallet ou infrastructure.

**Étape 4 — Saisie**. FBI signe transaction avec la clé obtenue, transférant 63,7 BTC vers wallet US gouvernement.

**Étape 5 — Annonce**. DOJ rend public ~30 jours après le paiement initial.

#### 42.3 Pourquoi 63,7 sur 75 ?

Différence de 11,3 BTC (~15%). Explications probables :

- Commission affilié : DarkSide opérait en RaaS (affilié garde ~70-80%, opérateur 20-30%). 11,3 BTC pourrait correspondre à la part affilié déjà extraite vers son propre wallet (qu’autorités n’ont pas pu saisir).
- Frais opérationnels (gas, mixing).
- Conversion partielle déjà effectuée.

#### 42.4 Méthodes mobilisées

**Tracking on-chain rapide** :

- Réaction en jours (vs Bitfinex en années).
- Outils : Chainalysis utilisé activement.

**Coopération sectorielle** :

- Colonial coopère pleinement avec FBI dès le départ.
- Information sur transaction de paiement immédiate.

**Coordination LEA** :

- FBI Cyber Division.
- Intelligence agencies multiples.

**Pression sur DarkSide** :

- L’attention politique post-Colonial déstabilise le groupe.
- Possible facilitation du tracking par opportunités opérationnelles.

#### 42.5 Leçons

**Pour les victimes** :

- **Coopérer immédiatement** avec FBI / autorités améliore probabilité de récupération partielle.
- Pas garanti, mais sans coopération = aucune chance.

**Pour les enquêteurs** :

- **Réaction rapide** = avantage. Les premiers jours / semaines sont critiques.
- **Pression médiatique / politique** peut faciliter coopération internationale.

**Pour les criminels (perspective des autorités)** :

- **Cibler infrastructure critique** = attention politique disproportionnée. DarkSide a été un moment, jamais retrouvé sa stature.

#### 42.6 Suite — DarkSide → BlackMatter → ALPHV

**DarkSide** se dissout officiellement après Colonial Pipeline. Mais **rebranding probable** :

- **BlackMatter** apparaît juillet 2021. Patterns techniques similaires à DarkSide. Saisi novembre 2021.
- **ALPHV / BlackCat** apparaît novembre 2021. Patterns continuant lignée. Démantelé 2024.

Cycle classique du RaaS : démantèlement → rebranding → re-démantèlement. L’écosystème est résilient mais pressurized.

-----

### Chapitre 43 — Ronin / Lazarus 2022 — 625 M USD

Le hack du **Ronin Network** est le plus gros vol crypto à ce jour. Attribué à **Lazarus** (DPRK) par FBI et Chainalysis. Cas emblématique de l’intersection entre vulnérabilité technique et acteur étatique sophistiqué.

#### 43.1 Le hack — mars 2022

**Ronin Network** : sidechain Ethereum développée par Sky Mavis pour le jeu Axie Infinity. Bridge Ronin permet transferts entre Ronin et Ethereum.

**Architecture du bridge** : 9 validators, 5 signatures requises pour autoriser un retrait. 4 contrôlés par Sky Mavis directement, 1 par Axie DAO (qui avait délégué ses signatures à Sky Mavis temporairement).

**Vecteur d’attaque** :

- Compromission de **5 des 9 clés validator** par phishing (« Operation Dream Job », fake job offer LinkedIn).
- Une fois 5 clés compromis (4 Sky Mavis + 1 Axie DAO délégué), attaquant atteint le seuil de signatures.

**L’attaque — 23 mars 2022** :

- Signature de transactions de retrait massives.
- **173 600 ETH** (~600 M USD) + **25,5 M USDC** (~25 M USD) drainés.
- **Total : ~625 M USD** au cours du moment.

**Découverte** : 6 jours après (29 mars 2022) — délai signaling failures de monitoring.

#### 43.2 L’attribution

**14 avril 2022** : OFAC sanctionne adresses Lazarus liées au hack.

**Attribution** :

- FBI confirme attribution Lazarus / DPRK.
- Chainalysis confirme dans ses rapports.
- Patterns d’attaque cohérents avec opérations Lazarus (vecteur LinkedIn, techniques utilisées, infrastructure).

**Pourquoi attribution forte** :

- Patterns infra (C2 servers liés à autres opérations Lazarus).
- Vecteurs sociaux (Operation Dream Job documenté pour multiple opérations Lazarus).
- Behavioral post-hack (utilisation Tornado Cash, bridges, patterns de blanchiment cohérents).

#### 43.3 Le blanchiment

**Méthode Lazarus post-hack** :

**Étape 1 — Conversion**. ETH et USDC convertis. USDC partiellement gelé par Circle (Circle a gelé ~250k USDC sur réquisition).

**Étape 2 — Tornado Cash**. Massive utilisation. ~25-30k ETH déposés à Tornado Cash dans les semaines post-hack. Volume tel que ils représentaient une fraction substantielle des dépôts Tornado.

**Étape 3 — Bridges**. Une partie passe via bridges vers Bitcoin (Ren BTC ou autre).

**Étape 4 — Mixing Bitcoin**. Sur Bitcoin, CoinJoin (Wasabi, Samourai), peeling chains.

**Étape 5 — Off-ramp**. Exchanges régionaux (Asie), OTC desks, P2P. Beaucoup en juridictions peu coopératives.

#### 43.4 Récupération

**Récupération partielle documentée** :

- **Circle gel** : ~250k USDC.
- **Saisies multiples** : autorités US et Sky Mavis ont récupéré plusieurs millions USD via différents incidents.
- Total récupéré : **estimé ~30-40 M USD** sur 625 (5-6%).

**Sky Mavis** : a remboursé les utilisateurs via levée de fonds (350 M USD, dirigée par Binance), pas par récupération hack.

#### 43.5 Méthodes mobilisées

**Attribution rapide** :

- OFAC dans les semaines suivant.
- Chainalysis / TRM / FBI publications.

**Sanctions** :

- Adresses Lazarus sanctionnées.
- Tornado Cash sanctionné en partie pour cette opération (août 2022).

**Coopération exchanges** :

- Multiple exchanges gelent des fonds Lazarus identifiés.
- Difficulté : Lazarus utilise exchanges non-coopératifs.

**Pression politique** :

- US, Corée du Sud, Japon, UE coordonnent sanctions DPRK élargies post-Ronin.

#### 43.6 Leçons

**Pour acteurs DeFi / bridges** :

- **Sécurité validators** = critique. 5/9 c’était insuffisant. Multi-sig schemes doivent assumer compromise.
- **Monitoring real-time** des bridges essentiel.
- **Audit de gouvernance** : la délégation de signatures Axie DAO à Sky Mavis (de fait centralisation) était une faille.

**Pour enquêteurs** :

- **Attribution étatique** rapide possible avec ressources adéquates.
- **Récupération massive impossible** quand acteur étatique : Lazarus utilise tout l’arsenal d’obfuscation, opère depuis juridiction non-coopérative.
- **Sanctions et pressions** sont les outils principaux.

**Pour CTI / OSINT** :

- **Documentation des wallets Lazarus** alimentation continue.
- **Tracking long terme** parfois fournit des opportunités (saisies opportunistes des années plus tard).

#### 43.7 Suite

Lazarus continue à opérer. Hacks majeurs subséquents attribués (Atomic Wallet, CoinEx, Stake.com, autres). **Plusieurs milliards USD/an** estimés volés par Lazarus selon Chainalysis. L’écosystème reste vulnérable à des acteurs ressourcés.

-----

### Chapitre 44 — Tornado Cash — sanctions OFAC et procès

**Tornado Cash** est le cas emblématique de **conflit entre code open source et responsabilité légale**. Sanctions OFAC, démantèlement partiel, procès des développeurs — débat juridique en cours.

#### 44.1 Le contexte

**Tornado Cash** : mixer décentralisé sur Ethereum, lancé août 2019 par Roman Semenov, Roman Storm, Alexey Pertsev. Cf Ch.31.

**Adoption** :

- 2019-2022 : usage massif. Multi-milliards USD passés à travers les pools.
- Légitime : utilisateurs privacy-conscious, payments anonymes, donations sensibles.
- Illicite : Lazarus, ransomware, hackers DeFi.

#### 44.2 Les sanctions OFAC — août 2022

**8 août 2022** : OFAC sanctionne Tornado Cash.

**Justifications** :

- Plus de **7 Mrd USD** estimés blanchis via Tornado depuis 2019.
- Usage massif par Lazarus (incluant Ronin, Ch.43).
- Usage par autres acteurs ransomware et fraude.

**Sanctions** :

- Adresses smart contracts Tornado Cash placées sur SDN list.
- Toute interaction par US persons interdite.
- Étendu à GitHub : Microsoft désactive le repo Tornado et comptes développeurs (controverse, partiellement réversé après).

**Réactions** :

- Communauté privacy : réaction forte. Paradigme de **« les développeurs ne sont pas responsables des usages »**.
- Civil liberties orgs (EFF, Coin Center) attaquent en justice.
- Multi-application : Coinbase finance partiellement le procès Coin Center vs OFAC.

**Coin Center vs OFAC** :

- Argument : OFAC outrepasse son mandat en sanctionnant un smart contract immutable (vs une personne / entité).
- Procès en cours 2023-2024-2025.
- Premiers verdicts : partiellement favorables aux plaintifs (un juge a noté que les smart contracts immutables ne peuvent pas être « personnes » sanctionnables au sens classique).
- Évolution complexe, à suivre.

#### 44.3 Inculpation et procès Pertsev

**Alexey Pertsev** : développeur de Tornado Cash, Russe, résidant Pays-Bas.

**Arrestation — août 2022** : arrêté Pays-Bas suite à enquête FIOD (autorité financière néerlandaise).

**Charges** : blanchiment d’argent (faciliter le blanchiment via le service développé).

**Procès — 2023-2024** :

- Argumentation accusation : Pertsev a sciemment continué à développer un service utilisé massivement pour blanchiment, malgré conscience.
- Argumentation défense : Tornado est code open source, immutable, Pertsev ne contrôlait pas les usages.

**Verdict — 14 mai 2024** : Pertsev **condamné** par tribunal néerlandais à **5 ans et 4 mois de prison** pour blanchiment d’argent.

**Implications** :

- Premier verdict significatif sur responsabilité de développeur de mixer.
- Précédent juridique majeur EU.
- Appel en cours.

#### 44.4 Inculpation Storm aux US

**Roman Storm** : co-développeur Tornado, US-resident.

**Inculpation — août 2023** : DOJ inculpe Storm pour conspiracy to commit money laundering, conspiracy to operate unlicensed money transmitter, conspiracy to violate sanctions.

**Arrestation** : Storm arrêté août 2023.

**Procès US — 2024-2025** :

- Procès initialement programmé septembre 2024.
- Reporté à plusieurs reprises.
- Procès tenu finalement 2025 selon évolution.
- **Verdict** : à confirmer selon évolution. Au moment de rédaction (2026), procédures en cours / partiellement résolues.

**Roman Semenov** : autre développeur, sanctionné OFAC août 2023, en fuite (juridiction non révélée publiquement).

#### 44.5 Évolutions post-sanctions

**Tornado Cash continue de fonctionner** : code immutable. Smart contracts sur Ethereum, accessibles techniquement. Volume très réduit post-sanctions (~95% drop) mais non-nul.

**Acteurs contournant** :

- Lazarus continue à utiliser Tornado malgré sanctions.
- Autres acteurs criminels conscients du risque.

**Migrations** :

- Vers d’autres mixers (Sinbad sanctionné après).
- Vers privacy coins (Monero).
- Vers techniques mixtes (CoinJoin Bitcoin + bridges).

**Sanctions Sinbad — novembre 2023** : OFAC sanctionne Sinbad.io, mixer ayant pris une partie du volume post-Tornado. Cycle continue.

#### 44.6 Leçons

**Pour l’industrie crypto** :

- **Développeurs peuvent être tenus responsables** dans certaines juridictions.
- **Code immutable n’est pas immunité légale**.
- Distinction floue entre « outils neutres » et « facilitations volontaires ».

**Pour les utilisateurs** :

- **Risque de sanctions** d’utiliser un service dont l’opérateur sera sanctionné rétroactivement.
- **Compliance** devient préoccupation majeure.

**Pour les enquêteurs** :

- **Tornado Cash post-sanctions** : moins de volume, mais acteurs criminels qui continuent sont **identifiables comme criminels** (interaction avec sanctions = signal fort).
- **Multiplications de mixers** rend tracking plus complexe mais aussi chaque service plus exposé.

#### 44.7 Pour l’analyste

Le cas Tornado Cash illustre l’**évolution réglementaire rapide** de l’écosystème crypto. L’analyste suit :

- Listes OFAC SDN (mises à jour régulières).
- Sanctions UE / autres juridictions.
- Procédures judiciaires marquantes.
- Évolutions du débat « code as speech » vs régulation.

Ces cadres déterminent **ce qui est légitimement enquêtable**, **ce qui peut faire l’objet d’action** (gel, saisie), et **ce qui expose l’utilisateur final** (interaction avec sanctioned).

-----

### Chapitre 45 — Synthèse MIXSHADOW

Bilan complet du fil rouge déployé tout au long du cours.

#### 45.1 Récapitulatif factuel

**Victime** : Aurélien Médical, équipementier français de matériel hospitalier (700 collaborateurs, OIV santé, Lyon).

**Incident** : ransomware Akira, mars 2026. Vecteur : compromission VPN admin via stealer log. 3 hôpitaux clients impactés (patients en attente, dont cas vitaux).

**Paiement** : 35 BTC (~2 M EUR) le 14 mars 2026. Clé déchiffrement reçue. Reprise progressive sur 3 semaines.

**Mandat** : Aurélien Médical + DGSI mandatent Athéna Group. Sarah Marin, analyste senior. 8 semaines, 80 k EUR.

**Objectifs** : tracer, cartographier, identifier off-ramps, contribuer à attribution, coopérer avec autorités.

#### 45.2 Méthodes appliquées

**Outils** :

- Chainalysis Reactor (principal).
- TRM Labs (validation croisée).
- Mempool.space, Etherscan, Tronscan, BscScan (publics).
- Maltego, Excalidraw (visualisation).
- Hunchly (capture).
- OpenTimestamps (anchoring preuves).

**Méthodes** :

- Cadrage initial structuré (Ch.24).
- Fiches d’adresses pour 250+ adresses (Ch.12).
- Suivi peeling chain (Ch.7).
- Tracking cross-chain (Ch.33).
- Analyse Tornado Cash statistique (Ch.31).
- Caractérisation hubs TRON (Ch.10).
- Calibration WEP systématique (Ch.18).
- Chain of custody rigoureuse (Ch.23).

**Coordination** :

- Briefings DGSI bi-hebdomadaires.
- Coordination Tether pour gel USDT-TRON.
- Coordination FBI / Europol via DGSI.
- Réquisitions via DGSI vers Binance, Kraken, Coinbase.

#### 45.3 Résultats

**Cartographie** :

- **250 adresses identifiées** au total (Bitcoin, Ethereum, TRON, Solana mineur).
- **4 chaînes principales** couvertes.
- **~75% des flux** Akira post-paiement Aurélien Médical tracés.

**Caractérisation Akira** :

- Patterns de blanchiment documentés (peeling Bitcoin → swap FixedFloat → Tornado Cash sur ETH → conversion USDT-TRON via exchange non-KYC → dispersion TRON via hubs).
- Pattern temporel suggérant fuseau horaire UTC+9 / Asie de l’Est (possible, non-conclusif).
- Choix Bitcoin (vs Monero) suggérant compromis traçabilité / facilité opérationnelle.
- **Insight transversal** : 2 hubs TRON identifiés comme **services de blanchiment partagés** entre Akira et Black Basta (insight cross-incident, alimente dossier multi-victimes).

**Coopération** :

- **3 mules identifiées** sur Binance / Kraken.
- **~45 000 USDT gelés** sur exchanges régulés.
- **~30 000 USDT gelés** via Tether (sur 6 adresses TRON).
- **6 adresses Akira principales** transmises pour évaluation sanctions OFAC.
- **2 adresses « possibles retraits Tornado »** alimentent suivi complémentaire.

**Threat Intel** :

- Fiche acteur Akira enrichie (base Athéna).
- Pattern blanchiment Akira documenté pour réutilisation.
- Insight hubs partagés pour coordination CTI plus large.

#### 45.4 Bilan financier

**Récupération nominale** :

- 45 000 USDT (Binance/Kraken) + 30 000 USDT (Tether) = **75 000 USDT gelés**.
- ~ **3,75 % du paiement initial** (75k / 2 M EUR).

**Bilan en valeur de renseignement** :

- 3 mules identifiées (utiles pour enquête judiciaire ultérieure).
- 2 hubs blanchiment identifiés (alimentent base Chainalysis / TRM).
- Pattern Akira documenté (réutilisable pour autres victimes).
- Coopération multi-juridictionnelle activée.

**Bilan en valeur stratégique** :

- Aurélien Médical bénéficie d’un dossier complet pour procédure judiciaire et déclaration assurance.
- DGSI bénéficie d’un dossier alimentant ses suivis Akira / RaaS.
- Athéna renforce sa base CTI et sa crédibilité opérationnelle.

#### 45.5 Limites assumées

**Pas de récupération massive**. Le bilan financier est **modeste**. C’est la réalité de l’enquête ransomware, sauf cas exceptionnels (Bitfinex, Colonial).

**Pas d’attribution civile**. Akira reste un cluster sans identités civiles attribuées par OSINT seul. Relevait des autorités via voies classifiées.

**Tornado Cash** : rupture analytique sur ~12 ETH (~36 000 USD à l’époque). Hypothèses calibrées, pas certitudes.

**Exchange non-KYC X** : ~150 000 USDT sans angle KYC direct.

**Solana** : couverture moindre des outils, sous-flux peu caractérisés.

#### 45.6 Apprentissages

**Pour Sarah** :

- L’enquête « modeste en récupération » peut être **substantielle en valeur de renseignement**.
- La calibration honnête préserve la crédibilité et permet la coopération.
- Le travail de cartographie complète prend des semaines mais paie sur le long terme.

**Pour Athéna** :

- Combiner outils pro (Chainalysis + TRM) augmente la couverture et la confiance.
- La coordination DGSI active les leviers que l’OSINT pure ne peut activer.
- Les insights cross-incident (hubs partagés) construisent une vue stratégique.

**Pour Aurélien Médical** :

- Le paiement en pression vitale, choix difficile, contextualisé.
- L’enquête post-paiement maximize la valeur extraite des fonds payés.
- Renforcement des défenses pour incidents futurs.

**Pour l’écosystème** :

- L’industrie ransomware est résiliente mais pressurée.
- La coopération internationale finit par produire des résultats.
- Chaque enquête contribue à la capacité collective.

#### 45.7 Devenir post-MIXSHADOW

**Aurélien Médical** :

- Reprise complète de l’activité.
- Investissement majeur dans cybersécurité (EDR, MFA universel, segmentation, surveillance 24/7).
- Plan IR durci.
- Communication transparente avec clients hospitaliers.

**Sarah Marin** :

- Continue chez Athéna, monte en seniorité.
- MIXSHADOW comme étude de cas en formations internes.
- Contribue à publication CTI sectorielle (TLP AMBER) sur Akira.

**DGSI** :

- Dossier Akira enrichi.
- Coordination Europol / FBI continue.
- Démantèlement éventuel d’Akira : à plus long terme, comme tous les groupes RaaS — cycle continue.

**Akira (groupe)** :

- Continue à opérer en 2026.
- Pression croissante des autorités.
- Possible rebranding ultérieur.
- Patterns documentés alimentent la défense collective.

#### 45.8 Le message final de MIXSHADOW

> **L’enquête crypto-forensique professionnelle ne promet pas miracles. Elle produit du renseignement actionnable, contribue à la justice, et alimente la défense sectorielle. Sa valeur tient à sa rigueur méthodologique, sa calibration honnête, et son intégration dans des écosystèmes coopératifs.**

C’est ce que le cours OSINT Crypto a tenté de transmettre, à travers méthodes, outils, cas, et fil rouge.

La Partie IX va aborder la **production professionnelle** : rapport, calibration formelle, coopération, éthique, et programme durable.

-----

## PARTIE IX — PRODUCTION, CADRE ET PROFESSIONNALISATION

> **Ce que cette partie apprend.** Transformer l’enquête en livrable de qualité professionnelle. Rédiger un rapport OSINT crypto solide, manier l’échelle de confiance avec discipline, coopérer efficacement avec VASP et autorités, naviguer les enjeux éthiques et légaux, construire un programme durable de surveillance crypto.
> 
> **Ce qu’elle ne couvre pas.** Méthodes d’enquête (déjà vues), outils (Partie IV).
> 
> **Ce que vous saurez faire après cette partie.** Produire un rapport actionnable et calibré. Coopérer avec autorités et VASP de manière productive. Maintenir une posture éthique sous pression. Bâtir un programme crypto-forensique durable.

-----

### Chapitre 46 — Produire un rapport OSINT crypto

Le **rapport** est le livrable principal. Sa qualité détermine l’impact de l’enquête. Mauvais rapport = bonne enquête perdue. Bon rapport = enquête médiocre amplifiée. Ce chapitre couvre la méthode pour rapports professionnels.

#### 46.1 Adapter à l’audience

**Différentes audiences** ont différents besoins.

**Direction / management non-technique** :

- Executive summary clair.
- Faits clés sans jargon.
- Implications business.
- Recommandations actionables.
- Graphes simples.

**Équipe technique (SOC, IR, CTI)** :

- Détails techniques.
- IoCs structurés.
- Méthodologie.
- Reproductibilité.
- Annexes complètes.

**Autorités (DGSI, TRACFIN, FBI, Europol)** :

- Faits sourcés.
- Timeline rigoureuse.
- Identifications précises avec calibration.
- Recommandations de coopération.
- Pièces à conviction structurées.

**Tribunal / procureur** :

- Faits incontestables.
- Méthodologie reproductible.
- Chain of custody documentée.
- Calibration explicite.
- Limites assumées.

**Communauté CTI / partage sectoriel** :

- Patterns anonymisés.
- IoCs.
- Threat intel utilisable.
- Préservation TLP.

Un même dossier peut produire **plusieurs rapports** adaptés (executive summary public + rapport complet TLP AMBER + annexe technique TLP RED).

#### 46.2 Structure type d’un rapport OSINT crypto

**Page de garde** :

- Titre.
- Référence dossier.
- Mandant.
- Date.
- Auteur(s).
- TLP (Traffic Light Protocol).
- Version.

**Executive summary (1-2 pages)** :

- Contexte.
- Faits principaux.
- Conclusions clés.
- Recommandations.
- Limites.

**Cadrage de la mission** :

- Mandat.
- Périmètre.
- Méthodologie générale.
- Cadre légal.

**Méthodologie** :

- Outils utilisés.
- Sources.
- Méthodes appliquées.
- Calibration WEP.

**Faits et observations** :

- Timeline.
- Transactions documentées.
- Adresses identifiées.
- Patterns observés.

**Analyse** :

- Hypothèses formulées.
- Calibration.
- Recoupements.
- Identifications.

**Conclusions** :

- Synthèse.
- Niveaux de confiance.
- Implications.

**Recommandations** :

- Actions immédiates.
- Actions à moyen terme.
- Coordination requise.

**Limites** :

- Ce qui n’a pas pu être fait.
- Incertitudes.
- Évolutions possibles.

**Annexes** :

- Captures de preuves.
- Listes complètes (adresses, TXIDs).
- Graphes détaillés.
- Détails méthodologiques.
- Glossaire si nécessaire.

#### 46.3 L’executive summary

Le **executive summary** est la partie la plus lue. Souvent **la seule** lue par certains décideurs. Doit donc être autonome et clair.

**Structure** :

- **Contexte** : 1-2 phrases (« Aurélien Médical, équipementier français, victime ransomware Akira mars 2026, paiement 35 BTC »).
- **Mandat** : 1 phrase (« Athéna mandaté pour tracer flux post-paiement et identifier angles d’action »).
- **Conclusions principales** : 3-5 points clés (« 75% des flux tracés », « 3 mules identifiées », « 75 000 USDT gelés », « 2 hubs blanchiment partagés Akira / Black Basta », etc.).
- **Recommandations majeures** : 3-5 points (« coordination autorités sur mules », « surveillance hubs identifiés », « renforcement défenses », etc.).
- **Limites** : 1-2 phrases honnêtes (« récupération nominale ~3,75% du paiement », « attribution civile non possible OSINT »).

**Longueur** : 1 à 2 pages **maximum**. Deux pages = strict maximum. Une page si possible.

**Style** : phrases courtes, factuelles, sans jargon. Si le destinataire (CEO, journaliste) ne comprend pas l’executive summary, le rapport est raté.

#### 46.4 Calibration WEP dans le rapport

Chaque hypothèse / conclusion doit avoir un **WEP explicite**.

**Formulations recommandées** :

- « **Quasi-certain** (>95%) que [observation] » — réservé aux faits directement observés.
- « **Très probable** (80-95%) que [hypothèse] basé sur [éléments de preuve] »
- « **Probable** (60-80%) que [hypothèse] »
- « **Possible** (40-60%) que [hypothèse], en concurrence avec [alternatives] »
- « **Peu probable** (15-40%) que [hypothèse alternative] »

**Erreur classique** : oublier WEP, ce qui fait passer hypothèses comme certitudes. Tous les énoncés non-évidents doivent être qualifiés.

#### 46.5 Visualisations dans le rapport

Cf Ch.21. En synthèse :

**Pour rapport exécutif** : 1-3 graphes simples, niveau 3-4.

**Pour rapport opérationnel** : 3-7 graphes intermédiaires.

**Pour annexes techniques** : graphes détaillés.

**Tableaux** : timeline, listes d’adresses, mules identifiées. Toujours préférer tableaux propres à listes en prose pour données structurées.

#### 46.6 Recommandations

Les recommandations doivent être **SMART** :

- **Spécifiques** : pas « renforcer la sécurité » mais « déployer EDR sur 100% des postes Windows utilisateurs ».
- **Mesurables** : objectifs quantifiables.
- **Atteignables** : réalistes pour le contexte du mandant.
- **Pertinentes** : adressent les enjeux identifiés.
- **Temporellement définies** : avec délai.

**Hiérarchisation** :

- **Actions immédiates** (jours / semaines).
- **Actions à moyen terme** (mois).
- **Actions à long terme** (programme durable).

**Adaptation à audience** :

- Recommandations à victime : pratiques, opérationnelles.
- Recommandations à autorités : coopération, coordination.
- Recommandations à communauté : threat sharing, defensive measures.

#### 46.7 Annexes structurées

**Annexes typiques** :

**A — Liste exhaustive d’adresses identifiées** : tableau avec adresse, blockchain, label, niveau de confiance, source.

**B — Liste des transactions documentées** : tableau avec TXID, date, montant, source, destinataire.

**C — Captures d’écran** : avec hashes SHA-256.

**D — Graphes détaillés** : niveau 1 / 2.

**E — Méthodologie détaillée** : protocoles, outils, validations.

**F — Glossaire** : termes techniques expliqués (utile si rapport lu par non-spécialistes).

**G — IoCs structurés** : pour partage CTI (format STIX/TAXII si possible).

#### 46.8 Revue qualité avant livraison

Avant transmission, **peer review** systématique :

- Un pair lit le rapport entier.
- Vérifie cohérence, calibration, faits.
- Suggère améliorations.
- Validation directeur si projet sensible.

**Checklist qualité** :

- [ ] Executive summary autonome et clair.
- [ ] Tous WEP explicites.
- [ ] Captures référencées en annexes avec hashes.
- [ ] Timeline cohérente UTC.
- [ ] Recommandations SMART.
- [ ] Limites assumées explicitement.
- [ ] Pas de jargon inexpliqué.
- [ ] Cohérence terminologique.
- [ ] Graphes lisibles avec légende.
- [ ] Cadre légal respecté.
- [ ] TLP correctement positionné.

#### 46.9 Le rapport vivant

Pour enquêtes longues, **rapport intermédiaire** + rapport final, avec versionning. Conserve traçabilité de l’évolution analytique.

Pour surveillance continue, **rapports périodiques** (mensuels, trimestriels) selon mandat.

-----

### Chapitre 47 — Échelle de confiance et formulation analytique

Approfondissement du chapitre 18. La **calibration de la confiance** est la signature de l’analyste sérieux. Ce chapitre formalise.

#### 47.1 Les Words of Estimative Probability

Les WEP sont une **échelle standardisée** de calibration. Origine : communauté du renseignement US (Sherman Kent, années 1960). Adoptés mondialement.

**Échelle CIA / NATO / DGSE** (variantes mineures) :

|WEP                                |Probabilité|Usage                  |
|-----------------------------------|-----------|-----------------------|
|Quasi-certain / Almost certain     |95-100%    |Preuve directe forte   |
|Très probable / Highly likely      |80-95%     |Multiple convergence   |
|Probable / Likely                  |60-80%     |Convergence majoritaire|
|Possible / Even chance             |40-60%     |Hypothèse plausible    |
|Peu probable / Unlikely            |15-40%     |Alternative dominante  |
|Très peu probable / Highly unlikely|<15%       |Possibilité résiduelle |

**Adaptation pour OSINT crypto** : même échelle, applicabilité à toute hypothèse.

#### 47.2 Pourquoi cette discipline

**Plusieurs raisons** :

**Communication précise** : « probable » et « possible » ont des sens distincts. Sans calibration, le lecteur interprète différemment.

**Auto-discipline** : forcer à choisir un WEP oblige à examiner les preuves. Décourage les sur-affirmations.

**Comparabilité** : même échelle entre rapports permet de comparer hypothèses.

**Crédibilité** : analyste calibré est plus crédible que analyste qui prétend tout savoir.

**Gestion d’incertitude** : reconnaît que l’enquête OSINT est intrinsèquement probabiliste.

#### 47.3 Application en pratique

**Pour chaque hypothèse non-évidente** :

1. Lister les preuves en faveur.
1. Lister les preuves contre / alternatives.
1. Évaluer le poids relatif.
1. Choisir un WEP.
1. Documenter justification.

**Exemples MIXSHADOW** :

- « L’adresse `bc1q[Akira-receive]` est l’adresse de réception du paiement Aurélien Médical » → **Quasi-certain** (preuve : transaction confirmée + correspondance avec récit victime + portail négociation Akira).
- « Le cluster Bitcoin opérationnel est contrôlé par opérateur(s) Akira » → **Très probable** (heuristique cluster + continuité peeling + label Chainalysis).
- « Les hubs TRON identifiés sont services de blanchiment partagés Akira / Black Basta » → **Probable** (patterns de service + corroboration cross-incident).
- « Le pattern temporel suggère acteur en fuseau Asie de l’Est » → **Possible** (signal cohérent mais alternatives plausibles).
- « Akira a des liens DPRK » → **Spéculatif / non déterminé** (pas de preuve OSINT directe, base sectorielle suggère possible).

#### 47.4 Pièges à éviter

**Le piège du « possible »**. « Possible » signifie 40-60%, pas « peut-être ». Un événement « possible » a près d’une chance sur deux. Utilisé proprement, c’est fort. Utilisé comme « peut-être faible », c’est trompeur.

**Le piège du « peu probable »**. « Peu probable » signifie 15-40%. C’est une fourchette **assez large**. Un événement à 35% peut quand même se produire. Pas « impossible ».

**L’inflation lexicale**. « Très probable » devient automatique pour tout ce qui n’est pas certain. Discipline requise pour conserver le sens.

**Mélanger preuves et confiance**. Confiance = niveau de croyance. Preuves = ce qui supporte. Confiance basée sur preuves, mais distincte.

**Confiance sur la précision vs confiance sur l’attribution**. « 75% confiance que cluster X » vs « 75% confiance que cluster X est attribué à acteur Y ». Distinguer.

#### 47.5 La calibration cumulative

Quand l’analyse aggregue plusieurs hypothèses, la **confiance se compose**.

**Exemple** :

- A : 80% confiance.
- B (dépend de A) : 70% confiance si A est vrai.
- A et B simultanément : 80% × 70% = **56% confiance**.

Beaucoup de raisonnements crypto sont **chaînés** : adresse → cluster → service → entité → individu. Chaque maillon a une incertitude. Cumulée, l’incertitude finale peut être substantielle même si chaque maillon paraît fort.

L’analyste honnête **reconnaît cette propagation**. Ne pas affirmer « certain que individu X est responsable » quand chaque maillon de la chaîne est à 70-80%, donc cumulé à 30-40%.

#### 47.6 Rédaction calibrée

**Bonnes formulations** :

- « Sur la base de [preuves], il est très probable (85%) que [hypothèse]. »
- « L’analyse suggère, avec une confiance modérée (~65%), que [hypothèse]. Une explication alternative est [autre], qui reste possible (~25%). »
- « L’identification de [propriété] est probable (~70%) ; cependant, sans accès à [preuve manquante], une certitude n’est pas atteignable. »

**Mauvaises formulations** :

- « Cette adresse est X. » (Sans calibration.)
- « Il est clair que Y. » (« Clair » est subjectif.)
- « Tous les éléments convergent vers Z. » (Hyperbole, perd nuance.)

#### 47.7 Quand exprimer son désaccord interne

Si plusieurs analystes désaccordent sur calibration :

- **Documenter** le désaccord.
- **Présenter** les deux positions dans le rapport.
- **Proposer** un WEP médian si possible, ou les deux explicitement.
- **Attribuer** chaque position aux analystes concernés.

Le désaccord sain renforce la qualité.

-----

### Chapitre 48 — Coopération avec VASP, autorités et compliance

L’enquête OSINT crypto produit son maximum de valeur **en coopération** avec autres acteurs. Ce chapitre couvre le cadre de coopération.

#### 48.1 Coopération avec exchanges / VASP

**Pour quoi** :

- Réquisitions KYC sur dépôts identifiés.
- Gel de fonds.
- Information sur patterns / tentatives suspectes.

**Comment** :

- **Via autorités** : exchange ne coopère pas directement avec entité privée pour réquisition KYC. Doit passer par autorité (DGSI, FBI, équivalent juridiction).
- **Via signalement direct** : exchange peut recevoir signalement « possible activité frauduleuse » d’enquêteur privé, qui alimente leur propre AML monitoring.
- **Via partenariats sectoriels** : ISACs financiers, partage de threat intel.

**Délais** :

- Signalement → traitement : variable.
- Réquisition autorité → exchange : jours à semaines selon urgence.
- Gel de fonds : peut être rapide (heures) si coordination fluide.

**Limites** :

- Exchanges non-régulés : peu / pas de coopération.
- Juridictions hostiles : impasse.
- Confidentialité KYC : exchange ne peut pas divulguer KYC à entité privée, seulement à autorités.

#### 48.2 Coopération avec émetteurs de stablecoins

**Tether (USDT)** :

- Coopère avec autorités sur réquisition.
- Gels documentés sur centaines de millions USDT cumulés.
- Délais variables.
- Plus réactif depuis 2023.

**Circle (USDC)** :

- Coopère activement.
- Gels rapides (heures-jours).
- Bien intégré aux processus US (OFAC).

**Pour l’enquêteur** : identifier dès qu’un fonds passe en stablecoin = opportunité de gel. Remontée via autorité.

#### 48.3 Coopération avec autorités françaises

**TRACFIN** :

- Cellule de renseignement financier.
- Reçoit déclarations de soupçon des assujettis.
- Pour enquêteur privé, contact via mandant assujetti (banque, VASP français).
- Pour enquêteur travaillant avec entreprise victime, le mandant peut faire signalement TRACFIN.

**ANSSI** :

- Sécurité des SI.
- Intervient sur OIV et opérateurs de services essentiels.
- Pour ransomware sur OIV, coordination ANSSI obligatoire.

**DGSI** :

- Sécurité intérieure.
- Cyberterrorisme, atteintes à la nation.
- Coordination pour cas sensibles.

**Cybermalveillance.gouv.fr** :

- Service public d’aide aux victimes.
- Signalement individuel.
- Orientation vers services compétents.

**Pharos** :

- Plateforme de signalement de contenus illicites.
- Pour scams crypto repérés.

**Police / Gendarmerie cyber** :

- SDLC (Sous-direction de la lutte contre la cybercriminalité, gendarmerie).
- BL2C / OFCS (police).
- Plaintes formelles.

**Magistrats spécialisés** :

- JIRS / J3 (juridictions interrégionales spécialisées).
- Procureurs cyber.

#### 48.4 Coopération internationale

**Europol EC3** :

- European Cybercrime Centre.
- Coordonne enquêtes EU.
- Operations Cronos (LockBit), autres.

**Interpol** :

- Coordination 195 pays.
- Notices rouges (mandats internationaux).
- Cyber Fusion Centre.

**FBI Cyber Division** (US) :

- Très actif sur ransomware et crypto crime.
- IC3 pour signalement individuel.

**NCA (UK)** :

- National Crime Agency.
- Cyber unit active.

**BKA (Allemagne)** :

- Bundeskriminalamt.
- Coopération étroite avec partenaires.

**FIOD (Pays-Bas)** :

- Service fiscal-pénal.
- Investigations Tornado Cash, autres.

**Autres** :

- Centres cyber au Japon, Corée du Sud, Singapour, Australie, Canada, Israël.
- Coopération variable selon dossiers et juridictions.

#### 48.5 OFAC et sanctions

**OFAC** : Office of Foreign Assets Control, US Treasury.

- Maintient SDN list.
- Sanctionne entités, individus, et **adresses crypto** (depuis ~2018, plus actif depuis 2022).
- Interaction avec sanctioned = violation pour US persons et entités sous juridiction US.

**Pour enquêteur** :

- Cross-check systématique des adresses sur SDN list.
- Identifier flux vers ou depuis adresses sanctionnées = drapeau majeur.
- Informer autorités si enquête révèle interaction sanctioned.

**Sanctions UE** :

- Liste des sanctions financières UE.
- Coordination avec OFAC mais avec divergences.
- Implications pour entités EU.

**Sanctions UK, autres juridictions** : régimes spécifiques.

#### 48.6 Cadre juridique français

**Article 40 CPP** : tout fonctionnaire ayant connaissance d’un crime ou délit doit le signaler au procureur. S’applique aux analystes en services publics.

**Pour enquêteurs privés** :

- **Pas d’obligation article 40**.
- Mais souvent : si découverte d’infraction grave dans le cadre de l’enquête, signalement opportun.
- Discussion avec mandant et juridique.

**RGPD** :

- Données personnelles (incluant celles de tiers identifiés dans l’enquête) doivent être traitées conformément.
- Bases légales : intérêt légitime, mission d’intérêt public (selon contexte), consentement.

**Secret professionnel** :

- L’enquêteur respecte la confidentialité du mandat.
- Sauf obligations légales contraires.

**Secret bancaire / secret des télécommunications** : limites externes au mandat OSINT.

#### 48.7 ISAC et partage sectoriel

**ISAC** (Information Sharing and Analysis Centers) :

- Communautés sectorielles de partage de threat intel.
- FS-ISAC (financial sectors), H-ISAC (health), autres.
- Partage anonymisé selon TLP.

**Pour crypto-forensique** :

- **SEAL ISAC** : Security and Enforcement Analytics Lab, focus crypto.
- **Crypto ISAC** : initiative dédiée.
- **CTI-League** : volontariat communauté CTI.

**Bénéfices** :

- Patterns émergents partagés.
- Wallets / adresses connues distribuées.
- Coordination réponse à campagnes.

**Pour analyste / cabinet** : participation à ISAC pertinent enrichit base de connaissance et contribue à l’écosystème.

#### 48.8 Limites de la coopération

**Lenteur** : procédures internationales prennent mois / années.

**Variability** : coopération fluide avec certaines juridictions, opaque avec d’autres.

**Scoping** : autorités ont priorités. Petits dossiers peuvent être négligés.

**Confidentialité** : informations transmises peuvent être moins suivies que désiré.

**Politique** : enjeux géopolitiques peuvent ralentir / dévier coopération.

#### 48.9 Construire des relations

**Pour cabinet ou analyste** :

- Présence à conférences (FIRST, Cybersec Forum Europe, FIC, etc.).
- Participation à ISACs.
- Contributions publiques (blog, talks).
- Coopération sur dossiers concrets renforce confiance.

**Avec le temps** :

- Réseau de pairs construit.
- Contacts directs aux autorités (avec confiance).
- Partage facilité.

C’est un investissement sur années, mais structurant pour efficacité.

-----

### Chapitre 49 — Éthique, légalité et sécurité de l’enquêteur

L’enquête crypto opère dans un **cadre éthique et juridique** qui doit être maîtrisé. Ce chapitre couvre les principaux enjeux.

#### 49.1 Légalité

**Cadre français** :

**OSINT** : généralement légal. Données publiques accessibles légalement. Mais :

- **Pas de hacking** : pas d’accès non-autorisé à systèmes.
- **Pas d’usurpation d’identité** : pas de faux comptes (sauf cadre HUMINT autorisé).
- **Pas de manipulation** : pas d’interaction trompeuse avec cibles.
- **Respect RGPD** : traitement de données personnelles encadré.
- **Pas d’enquête sous couverture privée** : réservé aux autorités.

**Enquêteur privé** : peut être encadré par CNAPS (Conseil national des activités privées de sécurité) selon nature de l’activité.

**Crypto spécifique** :

- Lecture de blockchain publique : libre.
- Achat de crypto pour transaction de test : possible mais peu pratiqué OSINT pur (plus IR/red team).
- Interaction avec sanctioned addresses : interdit (sanctions OFAC, UE).

#### 49.2 Cadre éthique

**Principes** :

**Honnêteté** : ne pas mentir au mandant ni aux interlocuteurs. Calibration honnête.

**Discrétion** : confidentialité du mandat. Pas de bavardage. Respect TLP.

**Minimisation** : collecter seulement ce qui est nécessaire.

**Non-prolifération** : ne pas diffuser hors cercle justifié.

**Respect des victimes** : dignité, sensibilité.

**Pas d’aide aux acteurs criminels** : refus de mandat suspect.

**Pas de production de rapports orientés** : résister à pressions pour conclusions politiques.

#### 49.3 Conflits d’intérêt

**Détection** : évaluation systématique avant acceptation de mandat.

- Le mandant a-t-il intérêt à orienter l’enquête ?
- L’analyste a-t-il un intérêt personnel dans le résultat ?
- Y a-t-il des liens préexistants avec les cibles de l’enquête ?

**Gestion** : refus de mandat, recusation, transparence avec autres acteurs.

#### 49.4 Pression et menaces

L’enquête crypto peut générer **pressions et menaces**.

**Sources** :

- **Acteurs criminels** : acteur enquêté découvre l’enquête (si OPSEC analyste fait défaut), tentative d’intimidation.
- **Mandants insatisfaits** : pression pour conclusions différentes.
- **Médias / journalistes** : pression pour révélations prématurées.

**Protection** :

- **OPSEC stricte** : pas d’identification publique d’analyste sur dossiers sensibles.
- **Confidentialité** : pas de divulgation hors cercle justifié.
- **Cadre légal** : respect strict pour ne pas s’exposer.
- **Soutien institutionnel** : cabinet / employeur protège ses analystes.
- **Coopération autorités** : si menaces graves, signalement et protection.

#### 49.5 Sécurité physique et numérique

**Numérique** :

- Machine d’investigation isolée.
- VPN / Tor pour navigation sensible (selon contexte).
- Comptes dédiés.
- Crypto-wallets séparés (pas d’argent personnel).
- Sauvegardes chiffrées.
- MFA universel.

**Physique** :

- Pour cas à très haut risque (acteurs étatiques, terrorisme), consignes opérationnelles spécifiques.
- Protection de l’identité (en particulier pour analystes individuels publiant publiquement).

**Bureaux** :

- Sécurité périmétrique.
- Contrôle d’accès.
- Caméras (selon contexte).
- Politique de visiteurs.

#### 49.6 Bien-être psychologique

**Risques** :

- Exposition à contenus difficiles (cas victimes, contenus sensibles si Dark Web).
- Stress et pression (deadlines, enjeux).
- Isolement (travail solitaire en deep work).
- Burnout sur enquêtes longues / complexes.

**Mesures** :

- **Rotations** sur dossiers difficiles.
- **Soutien psychologique** disponible.
- **Pauses** structurées.
- **Limites horaires**.
- **Communauté de pairs** pour partage.
- **Activités hors travail** préservées.

Pour cabinets : politique formalisée de bien-être.

#### 49.7 Fin de mission et clôture

**Archivage** : preuves conservées immutablement, accessibles si re-questions ultérieures.

**Suppression** : selon politique RGPD, certaines données supprimées après période de conservation.

**Communication finale** : mandant remercie, debriefe.

**Retour d’expérience** : interne au cabinet.

**Post-mortem** : ce qui a fonctionné, ce qui peut s’améliorer.

#### 49.8 Limites éthiques absolues

Quelques cas où **refus est obligatoire** :

**Faciliter une activité illicite**. Mandat qui demanderait, sous prétexte d’enquête, à fournir éléments à acteur criminel.

**Cibler un innocent**. Mandat qui demanderait à « salir » un tiers sans base.

**Violer secret professionnel**. Mandat qui demanderait à divulguer informations privilégiées.

**Espionnage économique illégitime**. Mandat qui demanderait à enquêter sur concurrent sans cadre légal.

**Travail pour acteur sanctionné**. Évident.

L’analyste a la responsabilité de **détecter et refuser** ces cas. Si pression interne du cabinet, escalade.

-----

### Chapitre 50 — Maturité analyste et programme de surveillance crypto durable

Comment construire une **capacité durable** de crypto-forensique — pour cabinet, équipe interne, ou analyste individuel.

#### 50.1 Évaluation de maturité

**Niveau 1 — Réactif** :

- Investigations ad-hoc sur incidents.
- Pas de capacité interne, dépendance prestataires.
- Pas de base de connaissance.

**Niveau 2 — Structuré** :

- Méthodologie documentée.
- Outils choisis et maîtrisés.
- Quelques analystes formés.
- Premiers playbooks.

**Niveau 3 — Optimisé** :

- Programme structuré.
- Analystes seniors et juniors.
- Base de connaissance interne (labels, fiches acteurs).
- Coopération institutionnelle établie.
- Contribution à communauté CTI.

**Niveau 4 — Excellence** :

- Recherche propre.
- Publications (TLP variables).
- Influence sectorielle.
- Outils internes développés.
- Capacité 24/7 si requis.

Pour la plupart des organisations : **niveau 2 ou 3** est l’objectif réaliste. Niveau 4 réservé aux acteurs majeurs (vendors, gros cabinets, services de renseignement).

#### 50.2 Construire l’équipe

**Composition cible** (cabinet typique) :

- **1 lead** : 7+ ans d’expérience, vue stratégique, peer review.
- **2-3 seniors** : 3-7 ans, mènent enquêtes.
- **2-4 juniors** : 0-3 ans, support et apprentissage.
- **1 manager** : pilotage non-technique.

**Recrutement** :

- Profils financiers reconvertis (ex-AML, TRACFIN, banque).
- Profils cyber étendus (CTI, SOC senior).
- Académiques (master Finance, master Cybersécurité).
- Anciens enquêteurs publics (gendarmerie cyber, services).

**Formation continue** :

- Certifications (CRC Chainalysis, TRM CTI, autres).
- Conférences (FIC, FIRST, etc.).
- Veille interne organisée.

#### 50.3 Outillage

**Outils essentiels** (niveau 3) :

- **1 outil pro principal** : Chainalysis Reactor ou TRM Labs ou Elliptic. Coût 50-200k USD/an selon scope.
- **Maltego Pro** : visualisation transverse.
- **Hunchly + outils captures** : preuves.
- **Stockage immutable WORM**.
- **Plateforme collaborative interne** : Mattermost / Element / Confluence.
- **Scripts Python custom**.

**Outils complémentaires** :

- Validations croisées (un autre vendor pro en abonnement secondaire).
- OSINT classique (Maltego connecteurs supplémentaires, abonnements presse, base publique).
- Forensique éventuelle (pour enquêtes intégrées avec IR).

**Budget annuel** (niveau 3) : ordre de grandeur 200-500 k EUR (outils + formations + abonnements).

#### 50.4 Base de connaissance interne

**Fiches acteurs** :

- Ransomware groups suivis.
- Patterns documentés.
- Adresses identifiées.
- Évolutions.

**Labels propriétaires** :

- Adresses identifiées dans enquêtes propres.
- Cross-references avec vendors.
- Maintenue à jour.

**Playbooks** :

- Pour chaque typologie (ransomware, pig butchering, etc.).
- Workflow structuré.
- Templates rapports.

**Bibliothèque cas** :

- Études de cas internes.
- Apprentissages.
- Réutilisable pour formation.

#### 50.5 Coopération externe

**Réseaux à entretenir** :

- Autorités françaises (DGSI, TRACFIN, Cybermalveillance, gendarmerie cyber).
- Autorités internationales selon dossiers.
- ISACs sectoriels.
- Vendors (Chainalysis, TRM, Elliptic — relations commerciales mais aussi partage).
- Communauté CTI.
- Académiques.

**Production publique** :

- Blogs, articles.
- Talks à conférences.
- Contributions communautaires (CT Magazine, etc.).
- Threat intel partagée (TLP AMBER / GREEN selon contexte).

#### 50.6 Surveillance proactive

Pour clients avec risque récurrent (banques, gros corps, fonds d’investissement) :

**Service de surveillance** :

- Monitoring continu de wallets cibles.
- Alertes sur mouvements significatifs.
- Rapports périodiques.

**Threat hunting** :

- Recherche proactive de patterns émergents.
- Alimente threat intel.

**Stress tests** :

- Simulations d’incidents.
- Évaluation de la capacité de réponse.

#### 50.7 Évolution professionnelle

**Junior (0-2 ans)** :

- Maîtrise technique.
- Lecture des blockchains.
- Premiers cas sous supervision.

**Senior (3-7 ans)** :

- Pilotage d’enquêtes.
- Mentoring junior.
- Calibration solide.
- Coopération externe.

**Lead (7+ ans)** :

- Direction d’équipe.
- Méthodologie.
- Contributions doctrinales.
- Représentation publique.

**Pour rémunération** : cf Ch.5.

#### 50.8 Risques et résilience

**Risques pour le programme** :

- **Dépendance vendor** : si Chainalysis / TRM augmente prix ou change modèle, impact.
- **Évolution réglementaire** : MiCA, sanctions, autres peuvent imposer adaptations.
- **Talent rétention** : marché crypto-forensique compétitif.
- **Fatigue / burnout** : exposition à contenus difficiles.
- **Réputation** : un rapport raté ou divulgué peut nuire durablement.

**Mesures** :

- Diversification outils (au moins 2 vendors).
- Veille réglementaire continue.
- Politique RH solide.
- Bien-être structuré.
- Qualité processus rigoureuse.

#### 50.9 Évolution sectorielle 2026-2030

**Tendances anticipées** :

**Renforcement réglementaire** : MiCA en pleine application, élargissement Travel Rule, nouvelles sanctions.

**Maturation outils** : IA/ML intégré aux outils pro. Détection de patterns automatique. Réduction du travail répétitif.

**Évolution criminelle** : nouvelles techniques d’obfuscation (ZK proofs avancés, privacy chains nouvelles), Lazarus continue, RaaS résilient.

**Démocratisation** : outils gratuits s’améliorent, formation se diffuse. Niveau 1-2 plus accessible.

**Spécialisation** : le métier se spécialise (DeFi forensics, NFT specialist, privacy coins specialist, etc.).

**Pour l’analyste** : le métier reste **en croissance**. Demande supérieure à offre. Spécialisation paie. Veille continue indispensable.

#### 50.10 Conclusion

> Le crypto-forensique est un métier jeune, en croissance, exigeant, et passionnant. Il combine technicité, méthodologie, éthique, et coopération. Il évolue rapidement.
> 
> Le bon analyste n’est pas celui qui « démêle tout ». C’est celui qui produit, méthodiquement et honnêtement, le maximum de valeur que les données permettent — en calibrant ce qu’il sait, ce qu’il suppose, et ce qu’il ne sait pas.
> 
> Les enquêtes crypto-forensiques contribuent à la justice, à la défense des victimes, à la sécurité collective. Pas à elles seules — mais comme une pièce d’un écosystème plus large incluant autorités, exchanges, communautés, et chercheurs.
> 
> Bonne enquête.

-----

## ANNEXES

> Les annexes apportent des **outils opérationnels** réutilisables : glossaire, templates de fiches, modèles de rapports, matrices de calibration, listes d’outils, mini-cas d’entraînement. Elles complètent le cours pour le passage à la pratique.

-----

### Annexe A — Glossaire opérationnel crypto

**Adresse**. Identifiant cryptographique (chaîne de caractères) d’un point de réception sur une blockchain. Bitcoin : 26-62 caractères selon format. Ethereum : 42 caractères commençant par `0x`. TRON : 34 caractères commençant par `T`.

**ABI (Application Binary Interface)**. Spécification d’interaction avec un smart contract (signatures de fonctions, types). Etherscan affiche l’ABI des contrats vérifiés.

**Affilié RaaS**. Acteur qui exécute des attaques utilisant le malware d’un opérateur RaaS. Garde typiquement 70-80% des rançons.

**AMM (Automated Market Maker)**. Mécanisme DEX basé sur pools de liquidité avec formule mathématique de prix. Uniswap, Curve, etc.

**AML (Anti-Money Laundering)**. Cadre réglementaire de lutte contre le blanchiment.

**Anonymity set**. Nombre d’utilisateurs « indistinguables » dans un mécanisme d’anonymisation. Plus l’anonymity set est grand, plus l’anonymat est fort.

**Approve / Allowance**. Permission accordée à un smart contract de dépenser des tokens de l’utilisateur. Mécanisme central des DEX et lending protocols. Détourné par drainers (cf Ch.9).

**Bitcoin Core**. Implémentation de référence du protocole Bitcoin.

**BIP (Bitcoin Improvement Proposal)**. Standard d’évolution Bitcoin. BIP-21 (URI), BIP-32 (HD wallets), BIP-39 (mnemonic seed phrases), BIP-141 (SegWit), etc.

**Block**. Groupe de transactions agrégées et validées ensemble. Identifié par numéro (block height) et hash.

**Block height**. Numéro séquentiel d’un bloc dans la blockchain.

**Bootstrap**. Démarrage d’un wallet par téléchargement et synchronisation de la blockchain.

**Bridge**. Protocole permettant transferts d’actifs entre blockchains. Wormhole, Stargate, etc.

**BSC / BNB Chain**. Chaîne de Binance, EVM-compatible.

**Burn**. Destruction de tokens en les envoyant à une adresse non-récupérable (souvent `0x0`).

**CEX (Centralized Exchange)**. Exchange centralisé. Binance, Coinbase, Kraken, etc.

**Chain of custody**. Documentation traçant la possession et l’intégrité de preuves.

**Chainalysis**. Vendor de blockchain intelligence (Reactor, KYT). Référence industrie.

**Cluster**. Ensemble d’adresses regroupées comme contrôlées probablement par une même entité.

**Cold storage**. Wallet hors ligne (matériel, paper). Plus sécurisé. Réserves.

**CoinJoin**. Technique de mélange Bitcoin coopérative non-custodial. Wasabi, Samourai.

**Confirmations**. Nombre de blocs ajoutés depuis qu’une transaction a été incluse.

**Custodial / Non-custodial**. Custodial = un tiers détient les clés privées (exchange). Non-custodial = utilisateur les contrôle.

**dApp (decentralized application)**. Application décentralisée sur blockchain.

**DEX (Decentralized Exchange)**. Exchange décentralisé. Uniswap, PancakeSwap, etc.

**DeFi (Decentralized Finance)**. Écosystème d’applications financières sur blockchain.

**Drainer**. Smart contract / script malveillant vidant un wallet via approval phishing.

**ECDSA (Elliptic Curve Digital Signature Algorithm)**. Algorithme cryptographique de Bitcoin et Ethereum.

**EOA (Externally Owned Account)**. Compte Ethereum contrôlé par clé privée (wallet utilisateur). Vs smart contract.

**ERC-20**. Standard tokens fongibles Ethereum.

**ERC-721**. Standard NFT Ethereum.

**ERC-1155**. Standard hybride fongible/non-fongible Ethereum.

**EVM (Ethereum Virtual Machine)**. Machine virtuelle Ethereum. Compatibles : BNB, Polygon, Avalanche, etc.

**Exchange**. Plateforme d’échange crypto. Centralized (CEX) ou Decentralized (DEX).

**Fee / Frais**. Coût de transaction. Bitcoin : satoshis/byte. Ethereum : gas × gas price.

**Fork**. Divergence d’une blockchain. Bitcoin Cash est fork de Bitcoin.

**Gas**. Unité de compute Ethereum. Coût d’une transaction = gas used × gas price.

**Gwei**. Unité de gas price. 1 gwei = 10^-9 ETH.

**Hash**. Empreinte cryptographique. SHA-256 pour Bitcoin, Keccak-256 pour Ethereum.

**HD Wallet (Hierarchical Deterministic)**. Wallet générant adresses depuis seed unique (BIP-32).

**Hot wallet**. Wallet en ligne. Pratique pour usage. Moins sécurisé que cold.

**Honeypot**. Token codé pour empêcher acheteurs de revendre. Scam.

**IBC (Inter-Blockchain Communication)**. Protocole cross-chain Cosmos.

**KYC (Know Your Customer)**. Procédure d’identification client par VASP.

**KYT (Know Your Transaction)**. Solution Chainalysis de monitoring AML temps réel.

**Layer-1**. Blockchain de base. Bitcoin, Ethereum.

**Layer-2**. Blockchain déployée sur Layer-1 pour scaling. Lightning Network, Arbitrum, Optimism, Base.

**Lightning Network**. Layer-2 Bitcoin pour micro-paiements.

**Liquidity pool**. Pool de tokens dans un DEX permettant swaps.

**Mempool**. File d’attente des transactions pending non encore incluses dans un bloc.

**Mining / Stacking**. Mécanismes de validation. Bitcoin = PoW (mining). Ethereum post-Merge = PoS (staking).

**Mixer / Tumbler**. Service mélangeant fonds de multiples utilisateurs pour casser traçabilité.

**Mnemonic**. Suite de mots permettant reconstitution d’un wallet. BIP-39.

**Multi-sig**. Adresse nécessitant signatures multiples (M-of-N).

**NFT**. Non-Fungible Token. Token unique non-divisible.

**Nonce**. Compteur séquentiel des transactions d’une adresse Ethereum.

**OFAC**. Office of Foreign Assets Control, US Treasury. Sanctions list.

**Off-chain**. Tout ce qui se passe hors blockchain (KYC, communications, etc.).

**On-chain**. Transactions et états enregistrés sur blockchain.

**Off-ramp**. Conversion crypto → fiat (sortie).

**On-ramp**. Conversion fiat → crypto (entrée).

**OP_RETURN**. Output Bitcoin permettant inclusion de données arbitraires (limités).

**OPSEC (Operational Security)**. Discipline de protection des opérations.

**Oracle**. Service fournissant données externes à un smart contract (prix, événements).

**OTC (Over-The-Counter)**. Trading hors orderbook public.

**P2P (Peer-to-Peer)**. Échange direct entre particuliers.

**P2PKH, P2SH, P2WPKH (SegWit), P2TR (Taproot)**. Types d’adresses Bitcoin.

**Peeling chain**. Pattern de blanchiment Bitcoin où une grosse somme est progressivement épluchée.

**Pig butchering**. Type de fraude combinant manipulation sentimentale et faux investissement crypto.

**PoS / PoW (Proof of Stake / Work)**. Mécanismes de consensus.

**Privacy coin**. Cryptomonnaie conçue pour anonymat. Monero, Zcash.

**Private key**. Clé privée. Permet de signer transactions. Connaissance = contrôle des fonds.

**Public key**. Clé publique. Dérivée de la privée. Adresse dérivée de la publique.

**RaaS (Ransomware-as-a-Service)**. Modèle où opérateurs vendent malware à affiliés.

**Ring signature**. Mécanisme cryptographique Monero pour anonymiser émetteurs.

**Rug pull**. Scam où créateurs de token vident la liquidité.

**Saisie**. Action légale de prise de contrôle d’actifs par autorité.

**Satoshi (sat)**. Plus petite unité Bitcoin. 1 BTC = 100 000 000 sats.

**SDN (Specially Designated Nationals)**. Liste OFAC de personnes/entités sanctionnées.

**Seed phrase**. Mnemonic. Suite de 12-24 mots reconstituant wallet.

**SegWit**. Segregated Witness. Évolution Bitcoin permettant plus de transactions par bloc.

**Smart contract**. Programme déployé sur blockchain, exécuté quand conditions remplies.

**SPL (Solana Program Library)**. Tokens standard Solana.

**Stablecoin**. Crypto stable adossée à valeur de référence. USDT, USDC.

**Stealth address**. Adresse one-time Monero pour masquer destinataire.

**SWIFT**. Système international de paiement bancaire (mention pour comparaison).

**Taint**. Concept de « contamination » d’un fonds par origine illicite. Variable selon juridiction.

**Token**. Actif déployé sur blockchain via smart contract.

**Tor**. Réseau d’anonymisation web (cf cours Dark Web).

**Tornado Cash**. Mixer décentralisé Ethereum sanctionné OFAC août 2022.

**TRACFIN**. Cellule française de renseignement financier.

**Travel Rule**. Recommandation FATF étendue aux VASP.

**TRM Labs**. Vendor blockchain intelligence (concurrent Chainalysis).

**TXID**. Transaction Hash. Identifiant unique d’une transaction.

**UTXO (Unspent Transaction Output)**. Modèle Bitcoin de comptabilité par « pièces » non dépensées.

**VASP (Virtual Asset Service Provider)**. Terme FATF pour services manipulant actifs virtuels.

**Wallet**. Logiciel/matériel stockant clés et signant transactions.

**Watchlist**. Liste d’adresses surveillées pour alertes.

**WEP (Words of Estimative Probability)**. Vocabulaire calibré de niveau de confiance.

**WORM (Write Once Read Many)**. Stockage immutable.

**Zero-knowledge proof / zk-SNARK**. Preuve cryptographique sans révélation. Tornado Cash, Zcash shielded.

-----

### Annexe B — Modèle de fiche adresse

```markdown
# Fiche adresse — [Identifiant abrégé interne]

## Identification
- **Adresse complète** : [adresse exacte 26-62 caractères selon blockchain]
- **Blockchain** : [Bitcoin / Ethereum / TRON / Solana / autre]
- **Type d'adresse** : [P2PKH / P2SH / SegWit (P2WPKH/P2WSH) / Taproot / EOA / Smart Contract / autre]
- **Identifiant interne enquête** : [INVESTIGATION-XXX-YYY]
- **Date de création de la fiche** : YYYY-MM-DD UTC

## Activité observable
- **Première transaction** : YYYY-MM-DD HH:MM UTC, TXID: [...]
- **Dernière transaction** : YYYY-MM-DD HH:MM UTC, TXID: [...]
- **Nombre total de transactions** : [N entrantes / N sortantes]
- **Solde actuel** : [montant] [actif] (au YYYY-MM-DD HH:MM UTC)
- **Volume cumulé entrant** : [montant par actif]
- **Volume cumulé sortant** : [montant par actif]
- **Périodes d'activité notables** : [bursts, dormances]

## Contreparties principales
| Adresse | Direction | Volume cumulé | Actif | Notes |
|---|---|---|---|---|
| [...] | reçu | [...] | [...] | [...] |
| [...] | envoyé | [...] | [...] | [...] |

## Cluster
- **Cluster Chainalysis ID** : [...]
- **Cluster TRM ID** : [...]
- **Adresses connues du cluster** : [N]
- **Label cluster** : [...]
- **Confiance cluster** : [high/medium/low/none]

## Labels
- **Etherscan / Tronscan / Mempool** : [labels visibles]
- **Chainalysis** : [label, confiance]
- **TRM Labs** : [label, confiance]
- **Elliptic** : [label, confiance]
- **OFAC SDN** : [oui/non, date sanction si oui]
- **Sanctions UE** : [oui/non]
- **Mentions OSINT** : [Twitter, presse, forums — sources et dates]

## Hypothèses
- **Hypothèse principale** : [description]
- **WEP** : [Quasi-certain / Très probable / Probable / Possible / Peu probable / Très peu probable]
- **Justification** : [synthèse des éléments soutenant]
- **Hypothèses alternatives** : [autres explications avec WEP]
- **Contre-éléments** : [observations qui pourraient nuancer]
- **Évolution attendue** : [si X est observé, alors évolution du WEP vers Y]

## Captures et sources
- **Captures d'explorateur** : 
  - Mempool/Etherscan/Tronscan : [chemin fichier], hash SHA-256: [...]
  - Outil pro (Reactor/TRM) : [chemin fichier], hash SHA-256: [...]
- **Sources externes** : [URL, date consultation, hash si applicable]
- **Cross-checks effectués** : [outils, dates]

## Statut enquête
- **Statut** : [Active / Surveillance / Clôturée]
- **Priorité** : [Haute / Moyenne / Basse]
- **Investigateur principal** : [nom]
- **Liens vers fiches connexes** : [autres adresses du graphe]
- **Mises à jour** : [historique versionné]

## Actions
- **Actions effectuées** : [liste avec dates]
- **Actions à mener** : [priorisées]
- **Coopération externe** : [autorités contactées, dates, retours]
```

-----

### Annexe C — Modèle de fiche transaction

```markdown
# Fiche transaction — [TXID abrégé]

## Identification
- **TXID complet** : [hash 64 caractères]
- **Blockchain** : [Bitcoin / Ethereum / etc.]
- **Block height** : [N]
- **Timestamp** : YYYY-MM-DD HH:MM:SS UTC
- **Confirmations** (au moment de la consultation) : [N]
- **Status** : [Success / Failed (Ethereum)]

## Détails
- **From / Inputs** :
  - [adresse 1] : [montant]
  - [adresse 2] : [montant]
  - **Total inputs** : [montant]
- **To / Outputs** :
  - [adresse 1] : [montant]  ← [destinataire / change ?]
  - [adresse 2] : [montant]  ← [destinataire / change ?]
  - **Total outputs** : [montant]
- **Frais** : [montant]
- **Actif transféré** : [BTC / ETH / USDT / autre]
- **Si Ethereum** :
  - **Value (ETH natif)** : [montant]
  - **ERC-20 transfers** (si applicable) : [from, to, amount, token]
  - **Internal transactions** (si applicable)
  - **Gas used / Gas price**

## Lecture
- **Pattern observé** : [transfer simple / peeling / consolidation / split / etc.]
- **Contexte enquête** : [pertinence pour le dossier]

## Hypothèses
- **Hypothèse sur la nature** : [description avec WEP]
- **Hypothèse sur les destinataires** : [destinataire vs change pour Bitcoin]

## Captures
- **Page d'explorateur** : [chemin, hash SHA-256]
- **Page outil pro** : [chemin, hash SHA-256]

## Connexions
- **Adresses impliquées** : [liens vers fiches d'adresses]
- **Transactions liées** : [TXID prédécesseurs / successeurs significatifs]

## Statut
- **Statut** : [Documentée / Pertinente / Clôturée]
- **Date d'analyse** : YYYY-MM-DD UTC
```

-----

### Annexe D — Modèle de timeline d’enquête

```markdown
# Timeline d'enquête — [Nom du dossier]

## Période couverte : [date début] au [date fin]

## Pré-incident
| Date UTC | Événement | Source | Notes |
|---|---|---|---|
| YYYY-MM-DD HH:MM | [événement, ex: compromission initiale] | [source forensics, log, autre] | [...] |
| ... | ... | ... | ... |

## Incident
| Date UTC | Événement | Adresse | Montant | TXID / Source |
|---|---|---|---|---|
| YYYY-MM-DD HH:MM | Demande de rançon | - | - | Note ransomware |
| YYYY-MM-DD HH:MM | Paiement effectué | [adresse] | [montant] [actif] | [TXID] |
| ... | ... | ... | ... | ... |

## Post-incident — flux observés
| Date UTC | Événement | Adresses | Montant | TXID |
|---|---|---|---|---|
| YYYY-MM-DD HH:MM | Premier mouvement post-paiement | [from] → [to] | [...] | [...] |
| YYYY-MM-DD HH:MM | Conversion via swap | [...] | [...] | [...] |
| YYYY-MM-DD HH:MM | Dépôt Tornado Cash | [...] | [...] | [...] |
| YYYY-MM-DD HH:MM | Dépôt sur exchange régulé | [...] | [...] | [...] |
| ... | ... | ... | ... | ... |

## Coopération et actions
| Date UTC | Action | Acteur | Résultat | Notes |
|---|---|---|---|---|
| YYYY-MM-DD | Signalement TRACFIN | [...] | Reçu | [ref] |
| YYYY-MM-DD | Coordination DGSI | [...] | Active | [ref] |
| YYYY-MM-DD | Réquisition Binance | DGSI | KYC fourni | 2 mules |
| YYYY-MM-DD | Demande gel Tether | DGSI | 30k USDT gelés | [adresses] |
| ... | ... | ... | ... | ... |

## Étapes du rapport
| Date UTC | Étape | Auteur | Notes |
|---|---|---|---|
| YYYY-MM-DD | Rapport intermédiaire 1 | [...] | TLP RED |
| YYYY-MM-DD | Briefing DGSI | [...] | [...] |
| YYYY-MM-DD | Rapport final | [...] | [...] |
| YYYY-MM-DD | Restitution mandant | [...] | [...] |
| YYYY-MM-DD | Archivage | [...] | [...] |
```

-----

### Annexe E — Matrice des signaux d’alerte

Outil opérationnel pour reconnaître rapidement les patterns d’usage suspect.

|Catégorie                 |Signal                                                      |Niveau d’alerte|Action                                                          |
|--------------------------|------------------------------------------------------------|---------------|----------------------------------------------------------------|
|**Adresse fraîche**       |Première transaction = réception gros montant               |Élevé          |Investigation, hypothèse réception ransomware ou collecte fraude|
|**Adresse fraîche**       |Création + activité immédiate (<1h)                         |Moyen          |Vérifier contexte                                               |
|**Pattern transactionnel**|Peeling chain identifié                                     |Élevé          |Tracking étape par étape                                        |
|**Pattern transactionnel**|Consolidation de multiples sources                          |Moyen          |Possible service (exchange) ou hub                              |
|**Pattern transactionnel**|Split en multiple destinataires                             |Moyen          |Distribution post-collecte ou post-hack                         |
|**Mixers**                |Dépôt vers Tornado Cash                                     |Élevé          |Documenter, analyse statistique limitée                         |
|**Mixers**                |Dépôt vers mixer custodial                                  |Élevé          |Vérifier OFAC, documenter rupture                               |
|**Mixers**                |CoinJoin Wasabi/Samourai                                    |Moyen          |Heuristique cluster invalidée pour cette TX                     |
|**Bridges**               |Transfert via bridge cross-chain                            |Moyen          |Tracking avec outil pro nécessaire                              |
|**Privacy coins**         |Conversion vers Monero                                      |Élevé          |Rupture analytique, pivot off-chain                             |
|**Exchanges**             |Dépôt vers exchange non-KYC connu                           |Moyen-Élevé    |Identification angle limité                                     |
|**Exchanges**             |Dépôt vers exchange régulé                                  |Moyen          |Angle KYC potentiel via réquisition                             |
|**Stablecoins**           |Conversion en USDT-TRON                                     |Moyen          |Patterns blanchiment fréquent                                   |
|**Stablecoins**           |Passage en USDC                                             |Faible         |Coopération Circle rapide possible                              |
|**Sanctions**             |Adresse sur SDN list                                        |**Critique**   |Signalement obligatoire                                         |
|**Sanctions**             |Adresse interagissant avec sanctioned                       |**Critique**   |Investigation, signalement                                      |
|**Volumes**               |Transaction >100 BTC sur adresse fraîche                    |Élevé          |Investigation, possible saisie ou hack                          |
|**Volumes**               |Volumes cumulés >1 M USD                                    |Élevé          |Acteur significatif                                             |
|**Comportement**          |Multiple wallets actifs sur fenêtre courte                  |Moyen          |Possible bot ou opérateur synchronisé                           |
|**Comportement**          |Pattern temporel cohérent fuseau spécifique                 |Faible-Moyen   |Indicateur géographique probabiliste                            |
|**Comportement**          |Wallet dormant qui se réveille brutalement                  |Élevé          |Surveillance accrue, possible monétisation                      |
|**Compromission wallet**  |Drainage complet d’une adresse en quelques transactions     |Élevé          |Investigation drainer, victim potential                         |
|**Smart contract**        |Contrat non-vérifié recevant des fonds                      |Moyen          |Possible scam token / drainer                                   |
|**Smart contract**        |Approve illimité (`uint256.max`) à contrat inconnu          |Élevé          |Drapeau approval phishing                                       |
|**Pig butchering**        |Adresse de collecte multi-source (10+ victimes potentielles)|Élevé          |Investigation typologie pig butchering                          |
|**Ransomware**            |Adresse mentionnée dans ransom note publique                |Élevé          |Coordination CTI sectoriel                                      |
|**Lazarus / DPRK**        |Patterns cohérents avec Lazarus + montant significatif      |Élevé          |Escalade DGSI / FBI                                             |

-----

### Annexe F — Matrice « ce que je peux conclure / ce que je ne peux pas conclure »

Outil de calibration. Pour chaque type d’observation, ce qui est raisonnablement concluable vs ce qui ne l’est pas en OSINT pure.

|Observation                                     |Ce que je peux conclure                                   |Ce que je ne peux PAS conclure                                       |
|------------------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------|
|Transaction X confirmée sur blockchain          |Le transfert a eu lieu, à ce timestamp, entre ces adresses|L’identité civile des parties                                        |
|Adresse a reçu N BTC depuis l’adresse Y         |Flux observable, contreparties identifiées                |Qui contrôle les adresses                                            |
|Cluster de N adresses constitué par heuristiques|Probable même contrôle (confiance variable)               |Contrôle absolu, identité                                            |
|Cluster labellisé « Binance » par Chainalysis   |Probable infrastructure Binance                           |Quel utilisateur final est derrière une adresse de dépôt             |
|Adresse Z est sur la SDN list OFAC              |Adresse sanctionnée — interaction = violation             |Détails non publics de la sanction                                   |
|Pattern de peeling chain observé                |Probable activité de blanchiment                          |Nature exacte de l’activité (ransomware, autre)                      |
|Adresse fraîche reçoit gros montant (35 BTC)    |Possible adresse dédiée (ransomware, achat, collecte)     |Sans contexte off-chain, type d’activité                             |
|Pattern temporel cohérent fuseau Asie           |Possible localisation opérateur en TZ X                   |Géographie certaine                                                  |
|Cluster identifié comme Akira par Chainalysis   |Probable lien avec opérations Akira                       |Quel(s) individu(s) au sein du groupe                                |
|Dépôt sur exchange régulé                       |Existence d’un compte utilisateur identifiable via KYC    |KYC sans réquisition légale                                          |
|Dépôt sur Tornado Cash                          |Anonymisation tentée, transaction observable              |Lien avec retraits ultérieurs (sauf analyse statistique probabiliste)|
|Conversion en Monero via exchange               |Existence de la conversion                                |Destination on-chain post-Monero                                     |
|Smart contract drainer identifié                |Mécanisme du vol, adresses techniques                     |Identité civile du déployeur                                         |
|Adresse créatrice d’un token rug pull           |Action du rug pull tracée                                 |Identité civile du créateur                                          |
|Hub TRON multi-source/multi-destination         |Probable service (exchange, OTC, blanchiment)             |Type exact, identité opérateur                                       |
|2 hubs identiques entre 2 enquêtes ransomware   |Probable service partagé                                  |Si même opérateur ou client commun                                   |
|Approval illimité à un contrat inconnu          |Indicateur de risque (potentiel drainer)                  |Si drainage déjà eu lieu sans regarder transferts ultérieurs         |
|Adresse Lazarus précédemment attribuée          |Cluster cohérent                                          |Tous les clusters Lazarus actuels                                    |
|Mention publique d’une adresse par chercheur    |Information à recouper                                    |Vérité absolue (vérifier la source)                                  |
|Patterns BEC + email phishing fournisseur       |Identifie schéma BEC, possible groupe russophone          |Identité des opérateurs                                              |

**Principe** : pour chaque conclusion, l’analyste s’interroge sur la **nature exacte** de ce qu’il peut affirmer. Glisser de « peut » à « ne peut pas » est trahison méthodologique.

-----

### Annexe G — Outils par usage (catalogue raisonné)

#### G.1 Explorateurs blockchain (gratuits)

**Bitcoin** :

- Mempool.space — référence moderne, API généreuse
- Blockstream.info (Esplora) — solide
- Blockchain.com — historique
- BTC.com — statistiques mining
- OXT.me — analyses Bitcoin avancées
- Blockchair.com — multi-chain

**Ethereum et EVM** :

- Etherscan.io — référence absolue
- BscScan, PolygonScan, Arbiscan, Optimistic Etherscan, Basescan, Snowtrace, FtmScan — clones par chaîne
- Beaconcha.in — beacon chain Ethereum
- Tenderly.co — debugging avancé
- Phalcon (BlockSec) — forensique

**TRON** : Tronscan.org

**Solana** : Solscan.io, Solana Explorer

**XRP** : XRPSCAN, Bithomp

**Cosmos écosystème** : Mintscan.io

**MultiversX** : MultiversX Explorer

#### G.2 Outils professionnels (payants)

**Investigation** :

- **Chainalysis Reactor** — référence industrie. Réservoir de labels propriétaires.
- **TRM Labs Investigations** — concurrent. Excellente couverture multi-chaînes.
- **Elliptic Investigator** — alternative. Strong DeFi.
- **CipherTrace** — Mastercard.
- **Crystal** — Bitfury.
- **Scorechain, Merkle Science** — challengers.

**AML / Compliance** :

- **Chainalysis KYT** — temps réel.
- **TRM Know Your VASP** — risk rating.
- **Elliptic Discovery** — screening.

**Spécialisés** :

- **Coinpath / Bitquery** — données blockchain via GraphQL.
- **Glassnode, Nansen** — analytics.
- **Spot On Chain** — alertes.

#### G.3 Visualisation

- **Maltego** (Pro) — référence OSINT investigation.
- **Gephi** — open source, analyse réseau.
- **Graphistry** — GPU, grands graphes.
- **Cytoscape** — JS-based.
- **Mermaid** (Markdown) — graphes simples.
- **Excalidraw / drawio** — manuel propre.

#### G.4 Capture et preuve

- **Hunchly** — captures HTML + screenshots.
- **Save Page WE** (extension navigateur) — captures simples.
- **wget / curl** — captures via CLI.
- **OpenTimestamps** — anchoring blockchain.
- **WORM storage** — solutions enterprise.

#### G.5 OSINT crypto enrichissement

- **Arkham Intelligence** — attribution publique.
- **DeBank** — portfolio explorer.
- **Dune Analytics** — dashboards SQL.
- **Token Sniffer / GoPlus** — analyse tokens.
- **Revoke.cash** — approvals.
- **Chainabuse** — scams.
- **Whale Alert** — grosses transactions.

#### G.6 Détection cross-chain

- **Wormhole Scan** — bridge Wormhole.
- **Stargate Finance** — bridge Stargate.
- **socket.tech, debridge.finance** — explorateurs cross-chain.
- **Reactor / TRM** — automatique pour bridges majeurs.

#### G.7 Sanctions

- **OFAC SDN list** — treasury.gov, format text/JSON/XML.
- **EU Sanctions Map** — sanctionsmap.eu.
- **UK FCDO sanctions list**.
- **Chainalysis / TRM** — intègrent sanctions automatiquement.

#### G.8 Scripts Python

Bibliothèques utiles :

- `web3.py` — Ethereum
- `tronpy` — TRON
- `python-bitcoinlib` — Bitcoin
- `requests` + APIs explorers
- `pandas` — manipulation données
- `networkx` — graphes
- `pycoingecko` — prix historiques

#### G.9 Veille

- Twitter/X : @zachxbt, @scamsniffer, @samczsun, @pcaversaccio, @tayvano_, @0xfoobar, @MetaSleuth, @MistTrack_io, @Chainalysis, @TRMLabs, @ellipticinc
- Newsletters : Rekt News (DeFi hacks), Defiant, Crypto Crime Cartel Cypher
- Rapports annuels : Chainalysis Crypto Crime Report, TRM Labs Annual Reports, Elliptic Reports
- FATF : reports VASP, sanctions, virtual assets
- Communautés : SEAL ISAC, Crypto ISAC, OnChain Investigators

-----

### Annexe H — Modèle de rapport OSINT crypto

```markdown
# RAPPORT D'INVESTIGATION OSINT CRYPTO

**Référence** : [DOSSIER-XXX]
**Mandant** : [...]
**Date** : YYYY-MM-DD
**Auteur(s)** : [...]
**Version** : [1.0]
**TLP** : [RED / AMBER / GREEN / WHITE]
**Classification** : [Confidentiel / Restreint / Public selon politique]

---

## EXECUTIVE SUMMARY

### Contexte
[1-2 phrases sur le contexte de l'enquête]

### Mandat
[1 phrase sur ce qui a été demandé]

### Conclusions principales
1. [Conclusion 1 avec WEP]
2. [Conclusion 2 avec WEP]
3. [Conclusion 3 avec WEP]
4. [Conclusion 4 avec WEP]
5. [Conclusion 5 avec WEP]

### Recommandations majeures
1. [Recommandation 1]
2. [Recommandation 2]
3. [Recommandation 3]

### Limites
- [Limite 1]
- [Limite 2]

---

## 1. CADRAGE DE LA MISSION

### 1.1 Mandat
[Description du mandat reçu]

### 1.2 Périmètre
[Périmètre couvert / non-couvert]

### 1.3 Objectifs
[Objectifs définis]

### 1.4 Cadre légal
[Bases légales, RGPD, sanctions, secret professionnel]

### 1.5 Calendrier
[Phases et délais]

---

## 2. MÉTHODOLOGIE

### 2.1 Approche générale
[Méthodologie d'investigation suivie]

### 2.2 Outils utilisés
[Liste outils principaux]

### 2.3 Sources
[Sources consultées]

### 2.4 Calibration WEP
[Échelle utilisée, brièvement]

### 2.5 Chain of custody
[Méthode de conservation des preuves]

---

## 3. FAITS ET OBSERVATIONS

### 3.1 Indices initiaux
[Description des indices reçus / découverts]

### 3.2 Timeline des faits
[Tableau timeline]

### 3.3 Adresses identifiées
[Liste avec catégorisation]

### 3.4 Transactions documentées
[Liste / tableau]

### 3.5 Patterns observés
[Patterns analytiques]

---

## 4. ANALYSE

### 4.1 Cartographie des flux
[Description + graphe]

### 4.2 Caractérisation des entités
[Acteurs, services, infrastructure]

### 4.3 Hypothèses formulées
[Avec WEP pour chacune]

### 4.4 Recoupements
[OSINT externe, validations croisées]

### 4.5 Identifications
[Avec niveaux de confiance]

---

## 5. CONCLUSIONS

### 5.1 Synthèse
[Conclusions principales]

### 5.2 Niveaux de confiance
[Récap WEP]

### 5.3 Implications
[Implications business / opérationnelles / juridiques]

---

## 6. RECOMMANDATIONS

### 6.1 Actions immédiates (jours-semaines)
[SMART recommendations]

### 6.2 Actions à moyen terme (mois)
[SMART recommendations]

### 6.3 Coordination requise
[Avec autorités, exchanges, autres acteurs]

### 6.4 Surveillance recommandée
[Adresses, patterns à surveiller]

---

## 7. LIMITES

### 7.1 Ce qui n'a pas pu être tracé
[Tornado, Monero, exchanges non-KYC, etc.]

### 7.2 Incertitudes
[Calibration honnête]

### 7.3 Évolutions possibles
[Si X est observé, alors évolution]

### 7.4 Questions ouvertes
[Pour suite éventuelle]

---

## ANNEXES

### A. Liste exhaustive des adresses
[Tableau]

### B. Liste exhaustive des transactions
[Tableau]

### C. Captures avec hashes
[Liste fichiers + SHA-256]

### D. Graphes détaillés
[Fichiers]

### E. Méthodologie détaillée
[Protocoles outils]

### F. Glossaire
[Si nécessaire]

### G. IoCs structurés
[Pour partage CTI, format STIX si applicable]

---

**Fin du rapport**

Auteur(s) : [...]
Validation : [Lead / Directeur]
Date : YYYY-MM-DD
Hash SHA-256 du PDF : [...]
```

-----

### Annexe I — Erreurs fréquentes d’analyse

Catalogue des erreurs courantes pour vigilance.

#### I.1 Erreurs de lecture Bitcoin

**Confondre destinataire et change**. Voir 2 outputs et conclure 2 destinataires distincts. Cf Ch.6.

**Ignorer les frais**. Penser que `inputs - outputs ≠ 0` est une perte. Ce sont les frais.

**Mal interpréter une consolidation comme un transfer**. Une transaction interne qui regroupe 50 UTXO d’une même entité n’est pas un transfer de 50 personnes vers 1.

**Confondre adresse et personne**. Une adresse n’est pas une identité.

#### I.2 Erreurs de lecture Ethereum

**Ignorer les transferts ERC-20**. Voir « Value: 0 ETH » et conclure « pas de valeur transférée ». Toujours regarder section ERC-20.

**Ignorer les internal transactions**. Pour DeFi, les flux ETH sont souvent internal.

**Confondre token contract et wallet**. L’adresse `0xdAC17...` (USDT contract) n’est pas un wallet d’utilisateur.

**Penser que `To = destinataire`**. Pour smart contract calls, `To` est le contrat, pas le destinataire final.

#### I.3 Erreurs d’analyse de cluster

**Sur-attribuer par heuristique de co-spend**. CoinJoin casse cette heuristique. Vérifier que les transactions du cluster ne sont pas CoinJoin.

**Étendre un label par cluster sans précaution**. Un label sur une adresse ne s’étend pas automatiquement à tout le cluster. Vérifier la qualité du label initial.

**Confondre cluster d’exchange et cluster d’utilisateur**. Un cluster contenant une adresse de dépôt d’un exchange ne fait pas de l’utilisateur de cet exchange l’opérateur du cluster.

#### I.4 Erreurs d’attribution

**Attribuer à un acteur étatique sans preuve**. Patterns sophistiqués ≠ Lazarus automatiquement.

**Identifier un individu par cluster**. Le cluster identifie un contrôle, pas une personne.

**Confondre opérateur et affilié**. Dans RaaS, l’opérateur est le développeur, l’affilié est l’attaquant. Distinct.

**Sur-attribuer un service de blanchiment à son client**. Si Akira utilise un hub TRON, ce hub n’est pas Akira. C’est un service.

#### I.5 Erreurs de calibration

**Sauter les WEP**. Tous les énoncés non-évidents doivent avoir une calibration explicite.

**Inflation lexicale**. Tout devient « très probable ». Discipline.

**Confiance non-cumulative**. Une chaîne d’hypothèses cumule l’incertitude.

**Ne pas distinguer confiance de précision**. Précis ≠ certain.

#### I.6 Erreurs méthodologiques

**Pas de chain of custody**. Captures non-hashées, non-archivées immutablement.

**Pas de validation croisée**. Un seul outil utilisé pour conclusions critiques.

**Pas de peer review**. Rapport produit sans relecture.

**Mauvaise gestion fuseaux horaires**. Mélange UTC et heure locale sans expliciter.

**Pas de documentation continue**. Journal d’enquête lacunaire ; reconstitution impossible.

#### I.7 Erreurs de communication

**Rapport non-adapté à audience**. Trop technique pour direction, trop vague pour analystes.

**Executive summary trop long**. Doit être 1-2 pages max.

**Pas de limites assumées**. Rapport surconfiant qui s’effondre à la première vérification.

**Recommandations vagues**. « Améliorer la sécurité » au lieu de mesures SMART.

**TLP mal positionné**. Diffusion à mauvais cercle.

#### I.8 Erreurs éthiques

**Conflit d’intérêt non-déclaré**. Mandat accepté sans évaluation.

**Sur-promesse au mandant**. Promesse de récupération qui ne se réalise pas.

**Manipulation par pression**. Ajustement des conclusions sous pression mandant.

**Engagement direct avec cible**. Interactions OPSEC compromises.

**Diffusion hors cercle**. Bavardage entre analystes ou avec journalistes.

#### I.9 Erreurs de coopération

**Coordination tardive**. Coopération autorités initiée trop tard, fonds déjà out.

**Pas d’utilisation des canaux institutionnels**. Direct contact exchange par enquêteur privé (sans autorité) ne donne rien.

**Sous-utilisation des labels**. Ignorer ce que les outils pro savent déjà.

**Pas de partage CTI**. Ne pas alimenter ni puiser dans la communauté.

#### I.10 Erreurs sur l’évolution

**Outil non mis à jour**. Utiliser une version d’outil dépassée.

**Veille déficiente**. Pas au courant des nouveaux acteurs / nouvelles techniques.

**Pas d’apprentissage post-mortem**. Mêmes erreurs répétées.

**Méthodologie figée**. Pas d’adaptation aux évolutions de l’écosystème.

-----

### Annexe J — 5 mini-cas synthétiques d’entraînement

Cinq cas réduits à pratiquer la méthode. Pas de solutions « officielles » — l’analyste reproduit le raisonnement.

#### J.1 Mini-cas 1 — Suspicion de pig butchering

**Énoncé** : un client privé contacte le cabinet. Sa cousine, 60 ans, a perdu ~80 000 USD sur une plateforme « MetaInvest Pro » sur 5 mois. Elle fournit 12 TXIDs USDT-TRON, captures de l’app, et conversation Instagram avec « Alex », son contact qui l’a introduite.

**Questions à se poser** :

1. Quels sont vos premiers indices à investiguer ?
1. Quelle est votre méthode pour confirmer le pattern de pig butchering ?
1. Quels outils utilisez-vous principalement ?
1. Comment caractérisez-vous le cluster opérateur ?
1. Quelles sont les actions recommandables pour la cousine ?
1. Quels sont les WEP que vous appliqueriez à vos conclusions ?

**Pistes** : Tronscan pour vérification, Chainalysis pour cluster, recherche reverse image sur photos « Alex », identification d’autres victimes via adresse de collecte, signalement Chainabuse, plainte avec rapport.

#### J.2 Mini-cas 2 — Hack DeFi modeste

**Énoncé** : un protocole DeFi sur Ethereum (« YieldFarm v2 ») a été exploité en mai 2026. ~3 M USD drainés. L’équipe vous mandate (4 semaines, 30 k EUR) pour investigation et soutien à coopération avec autorités.

**Questions** :

1. Quelle est votre méthodologie de Phase 1 ?
1. Comment identifiez-vous l’attaquant on-chain ?
1. Comment suivez-vous les fonds post-hack ?
1. Quels patterns d’obfuscation anticipez-vous ?
1. Quelle attribution est possible / pas possible ?
1. Quelles coopérations activez-vous ?

**Pistes** : analyse transaction d’exploit sur Phalcon / Etherscan, identification adresse attaquant, suivi vers Tornado Cash probable, identification de bridges, coordination avec Etherscan pour labels, signalement à OFAC si patterns DPRK.

#### J.3 Mini-cas 3 — Compromission wallet personnel

**Énoncé** : vous êtes mandaté par un trader crypto français individuel. Son wallet a été drainé le matin (12 ETH + tokens valant ~50 k EUR). Il a signé une transaction sur un site de mint NFT découvert via Twitter.

**Questions** :

1. Quelles sont vos premières actions techniques ?
1. Comment identifiez-vous la mécanique du drain ?
1. Quel est le drainer-as-a-service utilisé probablement ?
1. Suivez-vous les fonds drainés ?
1. Quelles recommandations d’urgence donnez-vous au trader ?
1. Quelles actions de récupération sont raisonnables ?

**Pistes** : lecture des transactions de drain, identification de l’approval, identification du drainer (via patterns), suivi via Tornado Cash probable, recommandation revoke.cash sur tous les wallets, plainte, alerte communauté.

#### J.4 Mini-cas 4 — Suspect business email compromise

**Énoncé** : une PME française a payé 200 000 EUR en USDT-Ethereum à une adresse sur instructions présumées de son fournisseur (qui a été compromis par BEC). Le fournisseur réel n’a jamais demandé ce paiement. La PME mandate (3 semaines, 25 k EUR).

**Questions** :

1. Quelles méthodes pour vérifier le BEC vs autre fraude ?
1. Comment tracez-vous les fonds USDT-Ethereum ?
1. Quels patterns post-réception attendez-vous ?
1. Quels sont les angles de coopération potentiels ?
1. Quelles probabilités de récupération calibrer ?

**Pistes** : analyse email frauduleux off-chain, lecture transaction USDT, suivi via swap / bridge probables, identification d’exchanges régulés en aval, coordination autorités françaises + nationales du fournisseur.

#### J.5 Mini-cas 5 — Tentative d’enquête sur paiement Monero

**Énoncé** : une organisation française a payé 28 XMR à un opérateur ransomware « XYZware ». Elle vous demande « de tracer ces XMR autant que possible ». Quel mandat acceptez-vous ?

**Questions** :

1. Quelle réponse réaliste donnez-vous au mandant initial ?
1. Si mandat alternatif, quel cadrage proposez-vous ?
1. Que pouvez-vous faire on-chain ?
1. Que pouvez-vous faire off-chain ?
1. Quelle calibration de promesses faites-vous ?
1. Quelles coopérations sont pertinentes ?

**Pistes** : refus du mandat « tracking XMR » ; proposition mandat caractérisation profil acteur + analyse off-chain + coordination CTI sectoriel ; reconnaissance honnête des limites Monero ; pivot vers angles indirects.

-----

> **Fin des annexes. Fin du cours.**
> 
> L’analyste qui a parcouru le cours OSINT Crypto en intégralité et fait les mini-cas dispose d’une formation **substantielle** au métier de crypto-forensique. La maîtrise opérationnelle vient ensuite avec l’expérience — premiers cas réels, mentoring, mises en situation, veille continue.
> 
> L’écosystème évolue rapidement. La méthodologie de fond (rigueur, calibration, coopération, éthique) reste stable. Les outils, typologies, et patterns spécifiques évoluent.
> 
> Bonne investigation.

-----

**Document complet — OSINT Crypto, Athéna Group, 2026.**