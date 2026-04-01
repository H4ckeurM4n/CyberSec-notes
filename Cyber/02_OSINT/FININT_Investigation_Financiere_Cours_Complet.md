# INVESTIGATION FINANCIÈRE NUMÉRIQUE — FININT AVANCÉ

*Suivre l'argent dans l'économie réelle — Flux bancaires, criminalité financière, blanchiment et recouvrement*

**Cours complet — 32 chapitres • 8 parties • 7 annexes**

*Renseignement financier • Analyse de flux • Blanchiment • Comptabilité forensique • Coopération internationale • Asset recovery*

---

## Table des matières

- [Fil rouge : Opération CLEARSTREAM](#fil-rouge--opération-clearstream)
- **PARTIE I — FONDATIONS DU RENSEIGNEMENT FINANCIER (Ch.1-4)**
  - [Ch.1 — Qu'est-ce que le renseignement financier](#chapitre-1--renseignement-financier)
  - [Ch.2 — Le cadre LCB-FT et la détection bancaire](#chapitre-2--lcb-ft-et-détection)
  - [Ch.3 — Le système bancaire et financier pour l'investigateur](#chapitre-3--système-bancaire)
  - [Ch.4 — La chaîne de valeur du renseignement financier](#chapitre-4--chaîne-de-valeur)
- **PARTIE II — CRIMINALITÉ FINANCIÈRE : TYPOLOGIES ET SCHÉMAS (Ch.5-9)**
  - [Ch.5 — Le blanchiment d'argent : les 3 phases et les secteurs vulnérables](#chapitre-5--blanchiment)
  - [Ch.6 — Trade-Based Money Laundering (TBML)](#chapitre-6--tbml)
  - [Ch.7 — Fraude fiscale, carrousels TVA et abus de biens sociaux](#chapitre-7--fraude-fiscale)
  - [Ch.8 — Corruption, financement du terrorisme et criminalité organisée](#chapitre-8--corruption-et-ft)
  - [Ch.9 — Systèmes de transfert informels : hawala et compensation](#chapitre-9--hawala)
- **PARTIE III — ANALYSE DE FLUX ET COMPTABILITÉ FORENSIQUE (Ch.10-13)**
  - [Ch.10 — Analyse de flux bancaires](#chapitre-10--analyse-de-flux)
  - [Ch.11 — Comptabilité forensique](#chapitre-11--comptabilité-forensique)
  - [Ch.12 — Investigation immobilière, patrimoniale et de train de vie](#chapitre-12--patrimoine)
  - [Ch.13 — Structures juridiques opaques et montages internationaux](#chapitre-13--structures-opaques)
- **PARTIE IV — OUTILS ET MÉTHODES D'INVESTIGATION (Ch.14-17)**
  - [Ch.14 — Sources de données et droits d'accès](#chapitre-14--sources)
  - [Ch.15 — Outils d'analyse et de visualisation](#chapitre-15--outils)
  - [Ch.16 — Méthodologie d'investigation financière](#chapitre-16--méthodologie)
  - [Ch.17 — Techniques d'analyse avancées](#chapitre-17--techniques-avancées)
- **PARTIE V — COOPÉRATION INTERNATIONALE ET CADRE JURIDIQUE (Ch.18-21)**
  - [Ch.18 — Coopération internationale](#chapitre-18--coopération)
  - [Ch.19 — Gel, saisie et confiscation](#chapitre-19--asset-recovery)
  - [Ch.20 — Régulations émergentes et évolutions](#chapitre-20--régulations)
  - [Ch.21 — Cadre juridique de l'investigation financière](#chapitre-21--cadre-juridique)
- **PARTIE VI — CONVERGENCE FININT-CYBER (Ch.22-24)**
  - [Ch.22 — Quand la criminalité financière rencontre le cyber](#chapitre-22--convergence)
  - [Ch.23 — Investigation intégrée : FININT + OSINT + crypto](#chapitre-23--investigation-intégrée)
  - [Ch.24 — Production de renseignement FININT](#chapitre-24--production)
- **PARTIE VII — ÉTUDES DE CAS (Ch.25-28)**
  - [Ch.25 — Cas complet : synthèse CLEARSTREAM](#chapitre-25--clearstream)
  - [Ch.26 — Cas complet : carrousel TVA intracommunautaire](#chapitre-26--carrousel)
  - [Ch.27 — Cas complet : corruption internationale et PEP](#chapitre-27--corruption)
  - [Ch.28 — Cas complet : BEC et réseau de mules](#chapitre-28--bec)
- **PARTIE VIII — MATURITÉ, VEILLE ET EXERCICES (Ch.29-32)**
  - [Ch.29 — Construire et piloter un pôle FININT](#chapitre-29--pôle-finint)
  - [Ch.30 — Veille et évolution des typologies](#chapitre-30--veille)
  - [Ch.31 — Exercice : analyse d'un dossier de DS](#chapitre-31--exercice-ds)
  - [Ch.32 — Exercice : investigation intégrée FININT + OSINT + crypto](#chapitre-32--exercice-intégré)
- **ANNEXES**

---

## Fil rouge : Opération CLEARSTREAM

> **Contexte narratif — ce fil rouge traverse les 24 premiers chapitres et se conclut au Ch.25.**
>
> **Nassim Belhaj**, analyste FININT au sein du département « Analyse et renseignement » d'une **CRF européenne**, reçoit un dossier complexe transmis par le pôle réception/traitement.
>
> **Le dossier :** 14 Déclarations de Soupçon (DS) convergentes déposées en 18 mois par 6 banques et 2 établissements de paiement, concernant un réseau de sociétés gravitant autour d'un homme d'affaires franco-libanais, **Karim Haddad**. Les DS signalent : des virements entrants depuis des sociétés de négoce basées à Dubaï et Istanbul vers des comptes français, des paiements sortants vers des fournisseurs au Bénin et en Côte d'Ivoire pour des marchandises dont la réalité est douteuse (surfacturation suspectée), des transferts vers des comptes personnels en Suisse et au Luxembourg, des retraits en espèces réguliers juste en dessous du seuil de déclaration (structuration), et des conversions partielles en crypto via un exchange européen.
>
> Montants cumulés : **18 M€** de flux sur 18 mois. Le schéma semble combiner trade-based money laundering (négoce fictif ou surfacturé), blanchiment classique (sociétés écrans, cascade, cash), et une dimension crypto.
>
> Nassim doit reconstituer le schéma complet : les flux réels (d'où vient l'argent), le mécanisme d'opacification (comment l'argent est blanchi), la destination finale (où va l'argent), et le réseau d'acteurs (qui participe).
>
> **Distinction fondamentale — ce fil transversal traverse tout le cours :** le renseignement FININT n'est PAS une preuve judiciaire. La note d'analyse de Nassim est du renseignement — elle oriente l'enquête, identifie les pistes, et recommande les actions. Elle ne constitue pas une preuve au sens du Code de procédure pénale. La transformation du renseignement en preuve nécessite des actes d'enquête (réquisitions judiciaires, auditions, expertises) conduits sous l'autorité d'un magistrat. L'analyste FININT doit en permanence savoir ce qu'il peut écrire, ce qui peut être disséminé, ce qui est exploitable judiciairement, et ce qui n'est qu'un faisceau d'indices.

---

## PARTIE I — FONDATIONS DU RENSEIGNEMENT FINANCIER

*Comprendre l'écosystème avant d'investiguer — les institutions, le cadre, le système financier, et la chaîne de valeur du renseignement.*

---

### Chapitre 1 — Qu'est-ce que le renseignement financier

#### 1.1 Définition

Le FININT (Financial Intelligence) est la discipline qui collecte, analyse et exploite l'information financière pour détecter, comprendre et entraver la criminalité économique et le financement d'activités illicites. L'analyste FININT ne produit pas de la donnée — il produit du **renseignement** qui oriente les enquêtes, les signalements et les saisies.

Le FININT se distingue des disciplines voisines tout en les croisant. L'**OSINT** collecte en sources ouvertes — le FININT utilise l'OSINT mais a aussi accès à des sources fermées (bases fiscales, bancaires, judiciaires). La **CTI** analyse la menace cyber — le FININT analyse la menace financière (mais les deux convergent quand le cybecrime se blanchit). L'**IE** protège le patrimoine économique — le FININT traque les flux illicites. Le FININT est la discipline du **« follow the money »** — suivre l'argent pour comprendre les réseaux et les schémas criminels.

#### 1.2 L'écosystème institutionnel

Les **CRF** (Cellules de Renseignement Financier) sont le cœur du dispositif : TRACFIN en France (~180 000 DS reçues/an), FinCEN aux US (~4 millions SAR/an), FIU-NL aux Pays-Bas, NCA UK, CTIF en Belgique, BaFin/FIU en Allemagne. Les **autorités de supervision** (ACPR en France, FCA au UK, BaFin — supervision AML des banques et institutions financières). Les **services d'enquête** (PNF — Parquet National Financier en France, SFO au UK, DOJ/FBI aux US). Les **offices de recouvrement** (AGRASC en France — Agence de Gestion et de Recouvrement des Avoirs Saisis et Confisqués, NCA Asset Recovery, US Marshals). Les **organisations internationales** (GAFI/FATF — normes, Egmont — réseau de CRF, Europol EFECC, INTERPOL).

#### 1.3 Les produits de l'analyste FININT

La **note d'analyse** (réponse structurée à une sollicitation ou à un dossier de DS — reconstitution des flux, identification du schéma, profil des acteurs, recommandations), le **rapport de flux** (graphe annoté avec montants, directions, contreparties, dates), le **rapport de renseignement spontané** (quand l'analyste détecte un schéma sans sollicitation — initiative), la **dissémination internationale** (transmission via Egmont à une CRF étrangère), et la **fiche de signalement** (transmission au parquet pour ouverture d'enquête judiciaire).

#### 1.4 Fil rouge — CLEARSTREAM : le dossier

> **💰 CLEARSTREAM — Épisode 1**
>
> Nassim reçoit le dossier : 14 DS, 6 banques, 2 établissements de paiement, 1 individu principal (Haddad), 7 sociétés identifiées, 5 juridictions (France, Liban, Chypre, Dubaï, Bénin). Les DS contiennent des anomalies convergentes : structuration, flux incohérents, négoce douteux. Nassim formule ses questions de renseignement : QR1 — d'où vient l'argent (quel est le prédécesseur criminel) ? QR2 — comment est-il blanchi (quel schéma) ? QR3 — où va-t-il (quel est le patrimoine réel de Haddad) ? QR4 — qui participe (réseau d'acteurs et facilitateurs) ?

---

### Chapitre 2 — Le cadre LCB-FT et la détection bancaire

#### 2.1 Les obligations des assujettis

Le cadre LCB-FT (Lutte contre le Blanchiment de Capitaux et le Financement du Terrorisme) impose des obligations à tous les **assujettis** : banques, assurances, établissements de paiement, notaires, avocats, agents immobiliers, experts-comptables, marchands d'art, casinos, et désormais les VASP (prestataires crypto — MiCA). Les obligations : **connaissance du client** (KYC — vérification d'identité, compréhension de l'activité, évaluation du profil de risque), **vigilance continue** (surveillance des opérations — les transactions sont-elles cohérentes avec le profil du client ?), **vigilance renforcée** (pour les clients à risque élevé — PEP, pays à risque, secteurs sensibles), **déclaration de soupçon** (DS/SAR — quand une opération suspecte est détectée, l'assujetti la déclare à la CRF), **gel des avoirs** (sur demande de la CRF ou dans le cadre des sanctions), et **conservation des documents** (5 ans après la fin de la relation — les pièces KYC et les traces des opérations).

#### 2.2 La détection bancaire : comment les établissements repèrent les anomalies

*Comprendre comment les DS arrivent à la CRF — et pourquoi certaines anomalies passent entre les mailles.*

Les établissements financiers déploient des systèmes de **transaction monitoring** (AML monitoring) qui analysent les flux en temps réel ou en batch. Le processus : les transactions passent par des **scénarios de détection** (règles paramétrées) qui génèrent des **alertes** quand un comportement anormal est détecté. Les alertes sont triées par des analystes compliance qui qualifient : **vrai positif** (l'anomalie est confirmée → investigation interne → DS si le soupçon persiste) ou **faux positif** (l'anomalie a une explication légitime → classement).

Les **scénarios AML typiques** : structuration (dépôts en espèces juste en dessous du seuil — 10 000 € en France), flux incohérents avec le profil client (un compte de particulier qui reçoit des virements internationaux de 200 K€), flux vers/depuis des pays à risque (juridictions GAFI liste grise/noire), mouvements rapides (les fonds arrivent et repartent en quelques heures — transit sans raison économique), virements circulaires (A → B → C → A), et utilisation excessive d'espèces pour le profil.

La **segmentation client** (le profil de risque du client détermine le niveau de surveillance — un commerçant cash-intensive a un profil différent d'un cadre salarié, et les seuils d'alerte sont calibrés en conséquence). Les **limites du screening automatisé** : les systèmes génèrent énormément de faux positifs (>95 % dans certains établissements — l'analyste compliance passe son temps à classer des alertes non pertinentes), les scénarios sont connus des criminels (ils adaptent leur comportement — la structuration est le contournement le plus basique), et les systèmes ne détectent que ce qu'ils sont paramétrés pour chercher (un schéma TBML sophistiqué passe souvent inaperçu car les flux ressemblent à du commerce légitime).

L'**analyste FININT en CRF** doit comprendre cette mécanique : une DS reflète ce que la banque a pu détecter avec ses outils et ses limites. L'absence de DS ne signifie pas l'absence d'anomalie — cela peut signifier que le monitoring n'a pas capté le schéma, que le seuil d'alerte n'a pas été atteint, ou que l'analyste compliance a classé l'alerte en faux positif à tort.

#### 2.3 Les directives européennes et le GAFI

Les directives européennes AML (4ème directive 2015, 5ème directive 2018, 6ème directive 2024 — évolution vers l'AMLA, l'autorité européenne AML basée à Francfort). Le GAFI/FATF (40 recommandations — le standard mondial, les évaluations mutuelles — un pays mal noté = facteur de risque pour les analystes, les listes — grise = surveillance renforcée, noire = haut risque).

---

### Chapitre 3 — Le système bancaire et financier pour l'investigateur

#### 3.1 Types de comptes et opérations

Les types de comptes (courant, épargne, dépôt à terme, titre, séquestre — chaque type a ses usages légitimes et ses détournements). Les moyens de paiement (virement SEPA — zone euro, domestique ; virement SWIFT — international, correspondent banking ; chèque — en déclin en Europe mais encore utilisé ; carte bancaire — traces exploitables ; espèces — le plus opaque).

#### 3.2 Le correspondent banking et SWIFT

Le **correspondent banking** est le mécanisme par lequel une banque française envoie un virement à une banque à Dubaï : la banque française n'a pas de compte à Dubaï, donc elle passe par une banque correspondante (une grande banque internationale — JPMorgan, Citibank, Deutsche Bank) qui a des comptes partout. Les **comptes nostro/vostro** (nostro = « notre compte chez vous », vostro = « votre compte chez nous ») sont les comptes que les banques correspondantes maintiennent les unes chez les autres pour faciliter les transferts. Cette architecture est un point de contrôle AML majeur — les banques correspondantes doivent vérifier que leurs clients (les banques locales) respectent les normes AML.

**SWIFT** (Society for Worldwide Interbank Financial Telecommunication) est le réseau de messagerie interbancaire mondial. Les messages SWIFT que l'analyste FININT doit savoir lire : **MT103** (virement client — donneur d'ordre, bénéficiaire, montant, devise, motif, banques intermédiaires), **MT202** (transfert interbancaire — mouvement de fonds entre banques correspondantes), **MT950** (relevé de compte — pour la reconstitution des flux). Le **BIC** identifie la banque dans le réseau SWIFT. L'**IBAN** identifie le compte.

#### 3.3 Les PSP, EME, fintech et rails de paiement modernes

*Ces acteurs sont devenus des rails de paiement centraux dans les schémas modernes de blanchiment — ils méritent une attention particulière.*

Les **PSP** (Payment Service Providers) et **EME** (Établissements de Monnaie Électronique) : Revolut, Wise (ex-TransferWise), N26, Monzo, et les dizaines de fintech régulées qui offrent des comptes, des cartes, et des virements internationaux rapides et à faible coût. Ils sont régulés (obligations AML applicables, agrément ACPR ou équivalent européen) mais la **supervision est parfois moins mature** que pour les banques traditionnelles — les effectifs compliance sont plus faibles, les systèmes de monitoring moins sophistiqués, et le volume de clients onboardés en ligne sans interaction physique est massif.

Les **IBANs « exotiques »** : la Lituanie et l'Estonie ont attiré de nombreuses fintech avec des réglementations favorables — résultat : des IBANs LT et EE apparaissent fréquemment dans les flux suspects (ce n'est pas intrinsèquement suspect — Revolut est lituanien — mais c'est un facteur contextuel). Les **cartes prépayées** (rechargeables, parfois anonymes sous certains seuils — utilisées pour le retrait de cash blanchi et les paiements courants avec de l'argent sale). Les **comptes de transit** (merchant accounts) utilisés par les commerçants pour recevoir les paiements par carte — un faux commerçant peut encaisser des paiements fictifs (acquiring fraud).

Les fintech comme outil de **layering rapide** : les virements instantanés entre comptes Revolut/Wise, la conversion multi-devises en un clic, et les virements internationaux à faible coût permettent un layering en heures là où les circuits bancaires classiques prennent des jours. Les criminels exploitent la rapidité : les fonds arrivent sur un compte fintech, sont immédiatement éclatés en 5 virements vers 5 autres comptes fintech dans 3 pays, puis convertis en crypto ou retirés en cash — le tout en moins de 24 heures.

Les **services de transfert de fonds** (Western Union, MoneyGram — cash-to-cash international, historiquement utilisés pour les remittances et les flux hawala).

#### 3.4 Fil rouge — CLEARSTREAM : les flux bancaires

> **💰 CLEARSTREAM — Épisode 2**
>
> Nassim analyse les relevés bancaires obtenus par droit de communication. Les virements entrants de Dubaï transitent par 2 banques correspondantes (une banque émiratie → Deutsche Bank Francfort → banque française). Les libellés sont vagues (« commercial services », « trade payment »). Les montants entrants sont systématiquement entre 45 000 € et 95 000 € — pas de seuil de détection automatique déclenché car chaque virement pris isolément est cohérent avec une activité de négoce. C'est l'accumulation sur 18 mois et la convergence de 14 DS de 8 établissements différents qui a permis de constituer le dossier. Les dépôts en espèces sur les comptes personnels de Haddad sont entre 9 500 € et 14 900 € — structuration classique sous le seuil de déclaration de 15 000 €. Et une partie des flux transite via un compte Wise (IBAN LT) avant d'arriver sur un exchange crypto.

---

### Chapitre 4 — La chaîne de valeur du renseignement financier

Le processus complet de la CRF. **Réception** (les DS arrivent des assujettis — banques, PSP, notaires ; le volume est massif — la CRF doit trier et prioriser). **Enrichissement** (la CRF a accès aux bases fiscales — DGFIP, aux bases de sécurité sociale, au fichier FICOBA — tous les comptes bancaires en France, aux fichiers de police — TAJ, aux registres fonciers, et aux bases internes — DS antérieures, dossiers en cours ; l'enrichissement est ce qui transforme une DS isolée en dossier exploitable). **Analyse** (l'analyste reconstitue les flux, identifie les schémas, évalue la gravité, et produit le renseignement). **Dissémination** (transmission au parquet si les éléments justifient une enquête judiciaire, ou à un service partenaire — DGSI, DNRED/Douanes, services étrangers via Egmont). **Feedback** (les suites données — enquête ouverte, classement, saisie — alimentent l'amélioration continue).

Les **droits de communication** de la CRF : en France, TRACFIN peut demander des informations à tout assujetti sans que le client en soit informé. Le **droit d'opposition** permet à TRACFIN de bloquer une opération suspecte pendant 10 jours ouvrés, le temps de transmettre au parquet. L'articulation avec l'autorité judiciaire : la CRF ne conduit pas d'enquête judiciaire — elle produit du **renseignement** qui oriente les investigations du parquet et de la PJ. Ce renseignement n'est pas directement une preuve — il doit être corroboré par des actes d'enquête judiciaire (réquisitions, auditions, expertises) pour devenir exploitable devant un tribunal.

---

## PARTIE II — CRIMINALITÉ FINANCIÈRE : TYPOLOGIES ET SCHÉMAS

*Comprendre les schémas criminels est la compétence centrale de l'analyste FININT — chaque typologie a ses red flags, ses flux caractéristiques, et ses méthodes d'investigation.*

---

### Chapitre 5 — Le blanchiment d'argent : les 3 phases et les secteurs vulnérables

#### 5.1 Le modèle en 3 phases

Le **placement** est l'introduction de l'argent sale dans le système financier : dépôts en espèces fractionnés (structuration/smurfing — montants juste en dessous du seuil de déclaration, multiples dépôts dans différentes agences), achat de biens en cash (véhicules, bijoux, montres), utilisation de commerces cash-intensive (le restaurant qui déclare 300 couverts/jour pour 50 réels), et conversion en instruments monétaires (mandats, chèques de banque, cartes prépayées).

Le **layering** est l'opacification : virements entre comptes dans plusieurs juridictions, sociétés écrans en cascade (A → B → C → D — chaque maillon dans un pays différent), prêts back-to-back (déposer l'argent sale dans une banque offshore, la banque prête le même montant via une structure « propre »), surfacturation/sous-facturation commerciale (TBML — Ch.6), nesting (une institution financière étrangère utilise le compte d'une banque correspondante pour accéder au système financier de manière opaque), et conversions crypto (Ch.22 et cours OSINT Crypto).

L'**intégration** est la réintroduction dans l'économie légale : achat immobilier (le véhicule d'intégration le plus courant — via des SCI, des sociétés offshore, ou des prêts hypothécaires fictifs), investissements dans des entreprises « légitimes », placements financiers, dépenses de luxe, et financement de projets immobiliers (promotion, construction).

#### 5.2 Les red flags universels

Les flux incohérents avec l'activité déclarée, les opérations sans justification économique apparente, la structuration (montants récurrents juste en dessous des seuils), la multiplication de sociétés sans substance, les flux circulaires (A → B → C → A), les PEP avec patrimoine incohérent, l'utilisation de juridictions à risque (GAFI liste grise/noire), les libellés vagues ou incohérents sur les virements, et les opérations urgentes sans raison apparente.

#### 5.3 Les secteurs vulnérables

*Une lecture par secteur aide l'analyste à contextualiser les flux — chaque secteur a ses vulnérabilités spécifiques.*

L'**immobilier** est le secteur le plus utilisé pour l'intégration : achat via des SCI ou des sociétés offshore (opacification de l'UBO), sous-évaluation à l'achat puis revente au prix réel (la différence est « blanchie »), prêts hypothécaires fictifs, et investissement locatif comme couverture de revenus. Les montants sont élevés, la régulation AML des agents immobiliers et notaires est encore insuffisante dans beaucoup de juridictions.

Le **commerce international** (import/export) est le terrain du TBML (Ch.6) : surfacturation, sous-facturation, phantom shipments. Les zones de libre-échange (Jebel Ali/Dubaï, Singapour) facilitent la circulation opaque de biens.

Les **commerces cash-intensive** (restaurants, bars, salons de coiffure, laveries, stations de lavage, marchés) sont les véhicules classiques de placement : les recettes en espèces sont gonflées artificiellement pour intégrer du cash illicite dans le chiffre d'affaires déclaré.

Les **fintech et PSP** (Ch.3) offrent des rails de layering rapide — virements instantanés, multi-devises, low-cost. Les **art, antiquités et biens de luxe** (marché opaque, évaluations subjectives, transactions en espèces encore fréquentes, free ports). Le **gaming** (casinos physiques — achat de jetons en cash, jeu minimal, encaissement de jetons « propres » ; gaming en ligne — dépôts, jeu minimal, retrait ; mondes virtuels et NFT — achats d'actifs numériques à des prix artificiels). Les **associations et ONG** (détournement de fonds caritatifs, financement du terrorisme sous couvert humanitaire — particulièrement surveillé dans le cadre du FT). Et l'**import-export de métaux précieux** (or, diamants — valeur concentrée, facilement transportable, marchés parallèles actifs en Afrique et au Moyen-Orient).

---

### Chapitre 6 — Trade-Based Money Laundering (TBML)

Le TBML est la technique de blanchiment la plus sophistiquée et la moins détectée — le GAFI le considère comme la plus grande vulnérabilité du système financier mondial. Le principe : utiliser des transactions commerciales réelles ou fictives pour transférer de la valeur à travers les frontières.

Les techniques : la **surfacturation** (exporter un bien à 100 000 € alors qu'il en vaut 30 000 → 70 000 € de valeur transférée), la **sous-facturation** (importer un bien à 30 000 € alors qu'il en vaut 100 000 → 70 000 € transférés à l'exportateur), la **surfacturation des quantités** (facturer 1 000 unités alors que 100 sont livrées), les **phantom shipments** (facturer des marchandises qui n'existent pas — documents commerciaux falsifiés, certificats d'origine frauduleux), et le **multiple invoicing** (facturer la même marchandise plusieurs fois à différentes entités).

Les red flags TBML : prix incohérents avec les prix de marché (vérifiables via les bases douanières — Comext, UN Comtrade, Global Trade Atlas, Import Genius), volumes irréalistes pour la taille de l'entreprise, routes commerciales atypiques (un négociant français qui importe du textile via Dubaï et la Turquie alors que la production est en Asie), divergence entre le type de marchandise et le secteur déclaré, et intermédiaires multiples sans valeur ajoutée.

Les sources d'investigation : données douanières (DGDDI en France, déclarations en douane), bases de prix de référence, et OSINT (vérifier l'existence physique de l'entreprise, les locaux, les employés, l'activité visible). Fil rouge : Nassim analyse les factures de Haddad — des « matières premières agricoles » achetées à Dubaï et revendues au Bénin à un prix 4 fois supérieur au prix de marché. Les documents de transport sont incohérents avec les volumes déclarés.

---

### Chapitre 7 — Fraude fiscale, carrousels TVA et abus de biens sociaux

La **fraude fiscale** comme criminalité financière : dissimulation de revenus (comptes non déclarés à l'étranger — avant l'EAR/CRS, c'était le schéma le plus courant), montages d'optimisation abusive, et utilisation de structures offshore. L'articulation fraude fiscale / blanchiment : la fraude fiscale est un crime prédécesseur (predicate offense) — les fonds non déclarés doivent être blanchis.

Le **carrousel TVA** : fraude massive exploitant le mécanisme de TVA intracommunautaire. Le principe : une société A achète hors TVA à un fournisseur européen (acquisition intracommunautaire), revend TTC à une société B en France (facture avec TVA collectée), encaisse la TVA collectée, et disparaît sans la reverser (missing trader). La société B déduit la TVA et le cycle recommence. Les montants sont considérables (estimés à 50 Mrd€/an de pertes dans l'UE). Red flags : sociétés récemment créées avec un CA très élevé, même type de marchandise (souvent électronique, téléphones, composants), chaîne de revente sans valeur ajoutée, disparition rapide de la société « manquante ».

L'**abus de biens sociaux** (ABS) : utilisation des fonds de la société à des fins personnelles. Red flags : paiements personnels depuis le compte société (voiture, immobilier, voyages), rémunérations incohérentes, prêts sans conditions de marché à des entités liées aux dirigeants.

---

### Chapitre 8 — Corruption, financement du terrorisme et criminalité organisée

La **corruption** comme schéma financier : pots-de-vin, commissions illicites, rétrocommissions, trafic d'influence. Les montages (société de conseil fictive facturant des « services de conseil » = paiement déguisé, trust ou fondation opaque, intermédiaires en cascade). Les PEP comme indicateur de risque (patrimoine incohérent avec les revenus déclarés). L'investigation : patrimoine réel vs revenus déclarés, réseau de sociétés, mandats, flux vers les juridictions opaques.

Le **financement du terrorisme** : les montants sont souvent faibles (quelques milliers d'euros) — la détection est plus difficile. Les vecteurs : virements vers des zones de conflit, systèmes de transfert informels (hawala — Ch.9), collectes via associations caritatives détournées, et crypto (cf. cours OSINT Crypto Ch.17 et Ch.28).

La **criminalité organisée** et ses flux : trafic de stupéfiants (le cash est roi — placement via commerces cash-intensive), traite des êtres humains, trafic d'armes, et cybercriminalité financière (renvoi cours OSINT Crypto et cours Écosystèmes).

---

### Chapitre 9 — Systèmes de transfert informels : hawala et compensation

Le **hawala** est un système de transfert de valeur informel, sans mouvement physique de fonds. Un donneur d'ordre remet du cash à un hawaladar A dans le pays d'origine. Le hawaladar B dans le pays de destination remet le même montant au bénéficiaire. La compensation entre les deux hawaladars se fait ultérieurement via des flux commerciaux légitimes ou d'autres transactions. Le système est utilisé légitimement par les diasporas (remittances — plus rapide et moins cher que les circuits bancaires) mais aussi pour le blanchiment et le financement du terrorisme (opacité totale — pas de trace bancaire).

Les **systèmes de compensation** (fei-ch'ien chinois, systèmes similaires dans d'autres cultures). Les **alternatives modernes** (néo-banques et services de paiement utilisés comme hawala numérique — transferts entre particuliers qui s'apparentent à de la compensation). L'investigation : les flux hawala ne laissent pas de trace bancaire directe — l'investigation repose sur l'OSINT (identification des hawaladars), les rapprochements comptables (les flux commerciaux de compensation sont visibles), et la coopération internationale. Fil rouge : Nassim soupçonne qu'une partie des fonds de Haddad transite via un réseau hawala entre le Liban et la France.

---

## PARTIE III — ANALYSE DE FLUX ET COMPTABILITÉ FORENSIQUE

---

### Chapitre 10 — Analyse de flux bancaires : lire, interpréter et reconstituer

Lire un relevé bancaire d'investigation (les relevés obtenus par droit de communication contiennent : BIC/IBAN des contreparties, libellés complets, références SWIFT). Construire le **diagramme de flux** (qui paie qui, combien, quand, avec quel libellé — l'outil central de l'analyste ; les flux visualisés en graphe avec montants, directions, et patterns temporels). Identifier les patterns anormaux (virements circulaires A → B → C → A, structuration, pics d'activité, flux sans contrepartie économique, libellés vagues). L'analyse temporelle (les flux sont-ils cohérents avec l'activité déclarée ?). Les outils d'analyse de flux (i2 Analyst's Notebook, Palantir, Excel/pandas, Gephi/networkx pour les graphes). L'articulation avec les données fiscales (en CRF, le croisement flux bancaires / déclarations fiscales révèle les incohérences).

---

### Chapitre 11 — Comptabilité forensique : lire un bilan pour détecter l'anormal

*L'analyste FININT n'est pas comptable — mais il doit pouvoir lire des comptes publiés et détecter les incohérences.*

Le **bilan** (actif/passif — postes à surveiller : créances clients anormalement élevées — fictives ? stocks gonflés ? immobilisations incorporelles surévaluées ? capitaux propres négatifs ?). Le **compte de résultat** (produits/charges — CA incohérent avec le secteur, charges de personnel très faibles pour le CA, charges de sous-traitance très élevées — facturation fictive ?, résultat faible malgré un CA élevé — marges aspirées par des charges suspectes). Les **red flags comptables** : CA en forte croissance sans explication, marge brute incohérente avec le secteur, charges de « conseil » à des sociétés liées, prêts intragroupe sans conditions de marché, flux de trésorerie négatifs malgré un résultat positif, et absence de commissaire aux comptes au-delà des seuils. Les sources : Infogreffe (France), Companies House (UK), SEC EDGAR (US), Orbis/BvD (international).

---

### Chapitre 12 — Investigation immobilière, patrimoniale et de train de vie

L'immobilier comme véhicule de blanchiment (achat en cash ou via sociétés écrans, surévaluation/sous-évaluation, prêts hypothécaires fictifs, investissement locatif comme couverture). Les sources immobilières (Patrim — valeurs foncières France, publicité foncière, Land Registry UK, registres étrangers). L'investigation patrimoniale globale (immobilier + véhicules + bateaux + avions + comptes bancaires + placements + crypto = patrimoine réel — à comparer avec les revenus déclarés). L'investigation de **train de vie** (les dépenses visibles — voyages, hôtels, restaurants, vêtements, écoles privées — sont des indicateurs de revenus réels ; OSINT sur les réseaux sociaux — Instagram, Facebook — comme source). Fil rouge : Haddad possède 3 biens immobiliers en France (1,2 M€), un appartement à Dubaï via OMEGA HOLDINGS, et une Porsche Cayenne — pour 48 K€/an de revenus déclarés.

---

### Chapitre 13 — Structures juridiques opaques et montages internationaux

Les véhicules d'opacification : sociétés écrans (BVI, Panama, Seychelles, Delaware), trusts (séparation propriété légale/bénéficiaire), fondations (Liechtenstein, Panama), LLP (UK). Les montages complexes : cascade de sociétés, prêts back-to-back, mirror trading (Deutsche Bank/Russie 2015 — $10 Mrd), round-tripping. Les zones de libre-échange (Jebel Ali/Dubaï, Singapour, Hong Kong — entrepôts francs, circulation sans contrôle douanier, stockage opaque de biens de valeur). Fil rouge : Nassim reconstitue le montage — NEXUS SAS (France) → OMEGA HOLDINGS (Chypre) → trust chypriote (UBO = Haddad) → compte Suisse.

---

## PARTIE IV — OUTILS ET MÉTHODES D'INVESTIGATION

---

### Chapitre 14 — Sources de données et droits d'accès de l'analyste

Les sources bancaires (relevés de comptes, données SWIFT MT103/MT202, données KYC). Les sources fiscales (déclarations de revenus, déclarations de patrimoine IFI, déclarations de comptes à l'étranger EAR/CRS, fichier FICOBA). Les sources judiciaires et policières (casier, fichiers de police TAJ, procédures en cours). Les sources ouvertes et OSINT (registres d'entreprises, presse, réseaux sociaux, leaks — renvoi cours OSINT Crypto et OSINT Mastery). Les sources partenaires (DS d'autres assujettis, renseignement Egmont, signalements services de renseignement). Le cadre juridique des accès (chaque source a un cadre — droit de communication TRACFIN, réquisition judiciaire, échange Egmont ; l'analyste documente le cadre d'accès pour chaque donnée utilisée).

---

### Chapitre 15 — Outils d'analyse et de visualisation

IBM **i2 Analyst's Notebook** (la référence pour la visualisation de réseaux, flux et timelines — utilisé par les LEA et CRF du monde entier). **Palantir** (analyse de données massives, intégration multi-sources — utilisé par les agences US et certaines CRF européennes). **Maltego** (pivoting OSINT avec transforms financiers). Traitement de données (Excel/LibreOffice pour les volumes simples, Python/pandas pour les volumes importants et l'automatisation, SQL pour les bases internes). Visualisation (Gephi, yEd — graphes de liens ; Plotly/Matplotlib — graphiques de flux temporels). Articulation avec les outils crypto (quand les flux passent par la blockchain — renvoi cours OSINT Crypto Ch.15).

---

### Chapitre 16 — Méthodologie d'investigation financière

Le processus structuré. **Cadrage** (formuler les questions de renseignement — « d'où vient l'argent ? », « comment est-il blanchi ? », « où va-t-il ? », « qui sont les acteurs ? »). **Collecte** (mobiliser les sources — DS, relevés, données fiscales, OSINT, partenaires). **Reconstitution des flux** (diagramme de flux complet). **Analyse du schéma** (quelle typologie ? les flux sont-ils cohérents avec une activité légitime ?). **Identification des acteurs** (qui joue quel rôle — organisateur, prête-nom, facilitateur, complice, bénéficiaire final). **Analyse patrimoniale** (patrimoine réel vs revenus déclarés). **Production** (note d'analyse avec niveaux de confiance, recommandations). La **discipline analytique** : chaque conclusion porte un niveau de confiance (fait observé, inférence probable, inférence possible, hypothèse), les limites sont explicites, et les hypothèses alternatives sont considérées.

---

### Chapitre 17 — Techniques d'analyse avancées

L'**analyse de réseau** (network analysis — identifier les nœuds centraux/hubs et les bridges/facilitateurs). L'**analyse temporelle** (time series — patterns récurrents = activité commerciale probable ; pics irréguliers = blanchiment événementiel ; structuration = montants sous les seuils à intervalles réguliers). L'**analyse comparative** (benchmarking — les flux de cette société sont-ils cohérents avec ceux d'entreprises similaires ?). Le **suivi des fonds** (follow the money — tracer chaque euro depuis la source jusqu'à la destination). L'**ACH** (Analysis of Competing Hypotheses — H1 blanchiment organisé, H2 optimisation fiscale agressive mais légale, H3 activité commerciale légitime atypique — tester chaque hypothèse contre les évidences). Et l'**analyse de récurrence** (les mêmes montants, les mêmes dates, les mêmes contreparties reviennent-ils ? les patterns de récurrence sont souvent la signature d'un schéma automatisé).

---

## PARTIE V — COOPÉRATION INTERNATIONALE ET CADRE JURIDIQUE

---

### Chapitre 18 — Coopération internationale : Egmont, GAFI, Europol et MLA

Le réseau **Egmont** (166 CRF membres — canal d'échange de renseignement financier, plus rapide que la MLA). Les échanges sont spontanés (une CRF partage proactivement) ou sur demande. **Le renseignement Egmont est soumis à des règles d'usage strictes** : il ne peut pas être utilisé directement comme preuve judiciaire sans l'autorisation de la CRF émettrice, il ne peut être transmis à un tiers sans accord, et son usage est limité à la finalité pour laquelle il a été partagé. Cette distinction renseignement/preuve est fondamentale — l'analyste doit la maîtriser.

**FIU.NET** (réseau sécurisé d'échange entre les CRF de l'UE — intégré à Europol, analyse cross-border automatisée). La **MLA** (Mutual Legal Assistance — commission rogatoire internationale pour les preuves judiciaires ; processus lent — mois à années — mais nécessaire pour les preuves admissibles en justice). **Europol** (EFECC — European Financial and Economic Crime Centre ; EMPACT — priorités criminelles européennes ; Europol ne conduit pas d'enquêtes mais coordonne, analyse, et appuie). **CARIN/Camden** (réseau interagences pour le recouvrement d'actifs transfrontalier).

---

### Chapitre 19 — Gel, saisie et confiscation : l'asset recovery

Le **gel** (mesure conservatoire — bloquer les fonds/biens ; en France : gel TRACFIN — 10 jours ouvrés renouvelables, gel judiciaire — ordonnance du juge, gel dans le cadre des sanctions — DGTI). La **saisie** (transfert de la détention à l'autorité — saisie pénale : AGRASC en France ; saisie de comptes bancaires, de biens immobiliers, de véhicules, de crypto-actifs — cf. cours OSINT Crypto Ch.20). La **confiscation** (transfert définitif de propriété à l'État après condamnation ; confiscation en valeur si le bien original n'est plus disponible). L'asset recovery international (reconnaissance mutuelle en UE, MLA pour les pays tiers, conventions bilatérales).

La distinction renseignement/preuve est critique ici : le renseignement FININT identifie les biens à saisir, mais la saisie elle-même nécessite une décision judiciaire fondée sur des preuves. L'analyste recommande le gel et la saisie — le magistrat décide.

---

### Chapitre 20 — Régulations émergentes et évolutions

L'**AMLA** (Anti-Money Laundering Authority — future autorité européenne AML, Francfort, opérationnelle 2026). Le **registre des bénéficiaires effectifs** européen (directive UE, accès, arrêt CJUE 2022, rétablissement partiel). L'**EAR/CRS** (Échange Automatique de Renseignements — les comptes à l'étranger sont automatiquement déclarés — 100+ juridictions, neutralisation du secret bancaire). Le **DAC6/DAC7/DAC8** (directives sur la transparence — montages transfrontaliers, plateformes numériques, transactions crypto). L'articulation crypto (MiCA, travel rule — renvoi cours OSINT Crypto Ch.16).

---

### Chapitre 21 — Cadre juridique de l'investigation financière

Le **blanchiment** comme infraction (article 324-1 Code pénal français — infraction autonome : on peut poursuivre le blanchiment sans avoir prouvé l'infraction prédécesseur). Les **infractions prédécesseurs** (trafic de stupéfiants, fraude fiscale aggravée, corruption, ABS, escroquerie, traite, cybecriminalité). La **charge de la preuve** (le ministère public doit prouver que les fonds proviennent d'une activité criminelle ET que le suspect le savait — la preuve est souvent circonstancielle, fondée sur l'accumulation d'indices concordants).

La **distinction renseignement / preuve** en détail : le renseignement FININT (note d'analyse, rapport de flux, dissémination Egmont) n'est pas une preuve au sens du Code de procédure pénale. Il oriente l'enquête et identifie les pistes. La transformation en preuve nécessite des **actes d'enquête** (réquisitions judiciaires — les relevés bancaires obtenus par le juge, pas par la CRF, sont des preuves ; auditions — les déclarations du suspect devant un OPJ sont des preuves ; expertises — l'analyse comptable par un expert judiciaire est une preuve). L'analyste FININT doit calibrer son écriture : la note d'analyse dit « les flux observés sont compatibles avec un schéma de blanchiment de type TBML » (renseignement), pas « Haddad est coupable de blanchiment » (preuve, qui relève du tribunal).

Le **secret professionnel** et ses exceptions (le secret bancaire cède devant la DS, le secret des avocats a des limites spécifiques). La **protection du déclarant** (l'assujetti qui fait une DS ne peut pas être poursuivi pour violation du secret professionnel si la DS est faite de bonne foi).

---

## PARTIE VI — CONVERGENCE FININT-CYBER ET INVESTIGATION INTÉGRÉE

---

### Chapitre 22 — Quand la criminalité financière rencontre le cyber

La convergence : les **produits de la cybecriminalité doivent être blanchis** (les rançons de ransomware payées en BTC, les fonds volés par BEC, les revenus de la fraude en ligne → tous doivent être convertis en fiat et intégrés dans l'économie légale → les techniques FININT s'appliquent). Et les **criminels financiers utilisent le cyber** (les APT étatiques volent des crypto pour financer des programmes — DPRK/Lazarus → le traçage combine blockchain et flux bancaires — cf. cours APT Ch.30).

Le **BEC** (Business Email Compromise — fraude au président, fraude au fournisseur) : les fonds virés vers des comptes de mules sont distribués en cascade → l'investigation FININT reconstitue le réseau de mules et les flux de cashout (virements, retraits espèces, conversion crypto). L'articulation FININT-SOC-IR (quand un incident cyber a une dimension financière — le SOC détecte l'incident, l'IR contient la compromission, et le FININT trace les fonds).

---

### Chapitre 23 — Investigation intégrée : FININT + OSINT + crypto

Le workflow complet quand une investigation combine les 3 dimensions. Le modèle en couches : **couche financière traditionnelle** (flux bancaires, comptabilité, patrimoine — ce cours), **couche OSINT** (registres, réseaux sociaux, OSINT technique — cours OSINT Mastery et OSINT Crypto Partie II), **couche blockchain** (traçage crypto, DeFi, stablecoins — cours OSINT Crypto Parties III-IV). La corrélation inter-couches (le même individu apparaît comme gérant d'une société suspecte ET propriétaire d'un wallet Ethereum ET destinataire de virements SWIFT). La production d'une note intégrée (un document qui synthétise les 3 couches avec des niveaux de confiance par source).

Fil rouge : Nassim intègre les 3 dimensions — les flux bancaires (virements Dubaï → France → Bénin), l'OSINT (sociétés écrans, patrimoine incohérent), et le volet crypto (conversion via exchange → traçage blockchain renvoyé au cours OSINT Crypto).

---

### Chapitre 24 — Production de renseignement FININT : notes, rapports et dissémination

La **note d'analyse FININT** : en-tête (référence, date, classification, auteur, demandeur), objet, contexte/sollicitation, méthodologie/sources (avec cadre juridique d'accès pour chaque source), reconstitution des flux (diagramme annoté), analyse du schéma (typologie identifiée), profil des acteurs, analyse patrimoniale, conclusions (niveaux de confiance pour chaque conclusion), lacunes (sources non consultées, juridictions non couvertes, données manquantes), et recommandations (signalement au parquet, gel, saisie, dissémination Egmont, investigations complémentaires).

La **discipline renseignement vs preuve** dans la rédaction : la note d'analyse utilise un vocabulaire calibré. « Les flux observés sont compatibles avec... » (pas « prouvent que... »). « Le patrimoine de X paraît incohérent avec ses revenus déclarés » (pas « X est un blanchisseur »). « L'hypothèse d'un schéma de TBML est retenue avec une confiance modérée » (pas « il s'agit de TBML »). Les faits sont distingués des inférences, les inférences des hypothèses, et les lacunes sont explicites. Cette rigueur protège l'analyste, le service, et l'exploitabilité ultérieure du renseignement.

Le **rapport de flux** (graphe annoté avec montants, directions, dates, contreparties identifiées, niveaux de confiance). La **dissémination internationale** (via Egmont — avec les contraintes d'usage : le renseignement transmis ne peut être utilisé comme preuve sans autorisation, ne peut être retransmis à un tiers sans accord, et son usage est limité à la finalité déclarée). La **restitution au magistrat** (pas de jargon bancaire, scénario clair, graphe simplifié, montants synthétiques, conclusions actionnables).

---

## PARTIE VII — ÉTUDES DE CAS

---

### Chapitre 25 — Cas complet : synthèse CLEARSTREAM

Synthèse du fil rouge. Le schéma complet reconstitué par Nassim.

**L'argent sale** provient du trafic de stupéfiants (cannabis, résine) entre le Liban et l'Europe — identifié par recoupement avec des procédures judiciaires en cours et du renseignement DGSI.

**Le placement** : dépôts en espèces structurés (< 15 000 €) sur les comptes personnels de Haddad et de 3 prête-noms, via 4 agences bancaires différentes en Île-de-France.

**Le layering** combine 3 techniques : (1) **TBML** — négoce fictif de « matières premières agricoles » surfacturées entre Dubaï (société d'achat contrôlée par Haddad) et le Bénin (société de revente avec prête-nom béninois), les flux transitent par les comptes de NEXUS SAS en France, les marchandises sont soit fictives soit surévaluées de 300 %. (2) **Cascade de sociétés** — NEXUS SAS (France) → OMEGA HOLDINGS (Chypre) → trust chypriote (UBO = Haddad) → compte en Suisse (UBS, via un gestionnaire de fortune). (3) **Conversion crypto partielle** — une partie des fonds (environ 800 K€) est convertie en BTC via un exchange européen, puis blanchie via les blockchains (renvoi cours OSINT Crypto pour le traçage détaillé).

**L'intégration** : achat immobilier en France (3 biens, 1,2 M€ via des prêts hypothécaires en partie fictifs — les apports personnels proviennent du circuit blanchi), achat immobilier à Dubaï (via OMEGA HOLDINGS), et dépenses de train de vie (véhicule, voyages, écoles privées).

**Le réseau d'acteurs** : Haddad (organisateur, UBO), 3 prête-noms (gérants des sociétés de négoce au Bénin et à Dubaï), 1 comptable complice (établit les factures fictives), 1 gestionnaire de fortune suisse (qui n'a pas fait de DS malgré les anomalies), et 1 réseau hawala entre le Liban et la France (pour les flux non bancaires).

**Recommandations** : transmission au PNF pour enquête judiciaire, gel des comptes français (droit d'opposition TRACFIN), saisie des biens immobiliers (AGRASC), dissémination Egmont vers les CRF chypriote, émiratie, suisse, béninoise et libanaise, et signalement du gestionnaire de fortune à la FINMA (autorité suisse).

---

### Chapitre 26 — Cas complet : carrousel TVA intracommunautaire

Un réseau de 12 sociétés dans 5 pays (France, Belgique, Pays-Bas, Allemagne, Pologne) opère un carrousel TVA sur des composants électroniques. Montant : 8 M€ de TVA non reversée en 18 mois. Les sociétés « manquantes » sont créées, encaissent la TVA pendant 2-3 mois, puis disparaissent. L'investigation reconstitue le circuit commercial (marchandises en boucle entre les mêmes entrepôts), identifie le réseau d'acteurs (prête-noms roumains et bulgares, organisateur à Bruxelles), et trace les fonds (TVA encaissée → virements vers Pologne → retraits en espèces). Coopération internationale (FIU.NET, Eurojust).

---

### Chapitre 27 — Cas complet : corruption internationale et PEP

Un ancien ministre d'un pays d'Afrique de l'Ouest soupçonné d'avoir reçu $15M de commissions illicites sur des marchés publics. Flux : sociétés de conseil BVI → Panama → Suisse → Luxembourg → SCI Paris (immobilier 16ème). L'investigation reconstitue les flux (réquisitions suisses via MLA, données EAR sur les comptes luxembourgeois, OSINT immobilier parisien), identifie les intermédiaires (cabinet de conseil suisse, avocat parisien), et produit le renseignement pour une transmission PNF + dissémination Egmont.

---

### Chapitre 28 — Cas complet : BEC (Business Email Compromise) et réseau de mules

Une entreprise française victime d'une fraude au fournisseur : 380 K€ virés vers l'Espagne après compromission email. L'investigation trace les fonds (compte mule espagnol → éclatement en 8 virements → réseau de mules → conversion crypto via Revolut → retraits cash). Le cas illustre la convergence cyber-FININT (compromission email = SOC/IR, traçage des fonds = FININT, conversion crypto = OSINT Crypto) et la nécessité de rapidité (gel dans les 24h pour être efficace).

---

## PARTIE VIII — MATURITÉ, VEILLE ET EXERCICES

---

### Chapitre 29 — Construire et piloter un pôle FININT

*Ce chapitre ne se limite pas à « recruter des analystes » — il décrit le fonctionnement opérationnel d'un vrai pôle FININT.*

#### 29.1 Organisation et profils

Les profils d'un pôle FININT : **analyste FININT junior** (traitement des DS, enrichissement, reconstitution de flux sous supervision — 0-3 ans), **analyste FININT senior** (dossiers complexes, multi-juridictions, production de renseignement, mentorat des juniors — 3-7 ans), **analyste OSINT/Crypto** (renseignement numérique et blockchain — compétence complémentaire, cf. cours OSINT Crypto), **analyste de conformité** (screening, monitoring, contrôle de qualité des DS — profil orienté compliance), et **coordinateur international** (coopération Egmont, FIU.NET, disséminations, MLA — profil senior avec expérience internationale).

#### 29.2 Workflow d'équipe et triage

Le **triage des DS** est le premier goulot d'étranglement : avec 180 000 DS/an à TRACFIN (et des volumes similaires dans les CRF majeures), le tri est une compétence organisationnelle critique. Le **scoring de complexité** (évaluation rapide à la réception : nombre de DS convergentes, nombre de juridictions, montants, présence de PEP, dimension crypto → score de complexité qui détermine l'allocation analyste junior/senior). La **priorisation** (les dossiers sont priorisés par : risque de dissipation des avoirs — les fonds vont-ils disparaître si on n'agit pas vite ?, gravité présumée du schéma, et potentiel d'exploitation judiciaire — un dossier bien documenté a plus de chances d'aboutir). La **gestion du backlog** (le volume de DS dépasse toujours la capacité d'analyse — il faut accepter que certains dossiers ne seront pas traités, et documenter les critères de non-traitement pour l'amélioration continue).

#### 29.3 Qualité et peer review

Le **peer review** (4 yeux minimum sur chaque note d'analyse avant dissémination — un second analyste vérifie la cohérence des flux, la pertinence des conclusions, l'exactitude des niveaux de confiance, et la conformité du vocabulaire renseignement/preuve). Le **QA** (Quality Assurance — revue périodique des notes produites par le pôle : les conclusions sont-elles étayées ? les lacunes sont-elles documentées ? le vocabulaire est-il calibré ? les recommandations sont-elles actionnables ?). Les **retex** sur les dossiers aboutis (quand une enquête judiciaire est ouverte sur la base d'un renseignement FININT : qu'est-ce qui a fonctionné ? quelles informations étaient les plus utiles au magistrat ? qu'est-ce qui manquait ?).

#### 29.4 Indicateurs de performance

Le nombre de notes produites (volume), le taux de transmission au parquet (les dossiers jugés suffisants pour une enquête judiciaire — indicateur de qualité), les montants saisis/confisqués (impact concret — l'indicateur le plus parlant pour la hiérarchie et les tutelles), le délai moyen de traitement (de la réception du dossier à la production de la note), et le feedback des services d'enquête (le renseignement était-il exploitable ? suffisant ? pertinent ?).

---

### Chapitre 30 — Veille et évolution des typologies

Les typologies émergentes : NFT pour le blanchiment (achat/vente à des prix artificiels), gaming et mondes virtuels (achat de biens virtuels avec de l'argent sale), plateformes de crowdfunding comme vecteur de placement, DeFi comme outil de layering (cf. cours OSINT Crypto Ch.14), néo-banques et fintech comme canal de blanchiment rapide, stablecoins sur TRON comme rail dominant en Asie, et les réseaux de mules recrutés via les réseaux sociaux (« money mule » — souvent des jeunes recrutés avec des promesses de revenus faciles).

Les sources de veille : rapports GAFI (typologies, évaluations mutuelles), rapports annuels des CRF (TRACFIN publie un rapport annuel avec des cas anonymisés — lecture obligatoire pour l'analyste français), Chainalysis/Elliptic/TRM Labs (crypto crime), Europol SOCTA/IOCTA, et la communauté professionnelle (ACAMS, Cambridge Economic Crime Symposium).

---

### Chapitre 31 — Exercice : analyse d'un dossier de DS

Un exercice complet non guidé. L'étudiant reçoit 3 DS fictives de 2 banques + 1 DS d'un notaire concernant un individu et son réseau de sociétés. Il doit : cadrer les questions de renseignement, reconstituer les flux, identifier les red flags, formuler des hypothèses (ACH), identifier les sources complémentaires, et produire la note d'analyse avec niveaux de confiance et recommandations. Grille d'auto-évaluation fournie.

---

### Chapitre 32 — Exercice : investigation intégrée FININT + OSINT + crypto

Un exercice avancé combinant les 3 dimensions. Scénario : un réseau soupçonné de blanchir les produits de la cybecriminalité (ransomware) via un mélange de flux bancaires traditionnels (virements SWIFT vers des sociétés de « conseil IT » à Dubaï et en Estonie) et de flux crypto (BTC → mixers → USDT → OTC desk). L'étudiant mobilise les techniques FININT (analyse de flux, investigation corporate) ET les techniques OSINT Crypto (traçage blockchain — renvoi cours OSINT Crypto), produit une note intégrée, et recommande les actions de gel/saisie/coopération. Ce cas-pont illustre la complémentarité des deux cours.

---

## ANNEXES

---

### Annexe A — Glossaire FININT

| Terme | Définition |
|-------|-----------|
| **ABS** | Abus de Biens Sociaux — utilisation des fonds de la société à des fins personnelles |
| **ACPR** | Autorité de Contrôle Prudentiel et de Résolution — superviseur bancaire français |
| **AGRASC** | Agence de Gestion et de Recouvrement des Avoirs Saisis et Confisqués |
| **AML** | Anti-Money Laundering — lutte anti-blanchiment |
| **AMLA** | Anti-Money Laundering Authority — future autorité européenne AML (Francfort, 2026) |
| **BEC** | Business Email Compromise — fraude au président / fraude au fournisseur |
| **BIC** | Bank Identifier Code — identifie une banque dans le réseau SWIFT |
| **CARIN** | Camden Asset Recovery Inter-Agency Network — recouvrement transfrontalier |
| **CFT** | Combating the Financing of Terrorism — lutte contre le financement du terrorisme |
| **Correspondent banking** | Système par lequel les banques accèdent au réseau financier international via des comptes chez d'autres banques |
| **CRF / FIU** | Cellule de Renseignement Financier / Financial Intelligence Unit |
| **CRS / EAR** | Common Reporting Standard / Échange Automatique de Renseignements — comptes à l'étranger |
| **DAC6/7/8** | Directives européennes sur la transparence fiscale et financière |
| **DGDDI** | Direction Générale des Douanes et Droits Indirects |
| **DS / SAR** | Déclaration de Soupçon / Suspicious Activity Report |
| **EFECC** | European Financial and Economic Crime Centre (Europol) |
| **Egmont** | Réseau mondial de 166 CRF pour l'échange de renseignement financier |
| **EME** | Établissement de Monnaie Électronique |
| **EMPACT** | European Multidisciplinary Platform Against Criminal Threats |
| **FATF / GAFI** | Financial Action Task Force / Groupe d'Action Financière Internationale |
| **FICOBA** | Fichier national des Comptes Bancaires et assimilés (France) |
| **FinCEN** | Financial Crimes Enforcement Network (CRF américaine) |
| **FININT** | Financial Intelligence — renseignement financier |
| **FIU.NET** | Réseau sécurisé d'échange entre les CRF de l'UE |
| **Hawala** | Système informel de transfert de valeur sans mouvement physique de fonds |
| **IBAN** | International Bank Account Number — identifie un compte bancaire |
| **Intégration** | 3ème phase du blanchiment — réintroduction dans l'économie légale |
| **KYC** | Know Your Customer — vérification d'identité et connaissance du client |
| **Layering** | 2ème phase du blanchiment — opacification des flux |
| **LCB-FT** | Lutte Contre le Blanchiment et le Financement du Terrorisme |
| **MiCA** | Markets in Crypto-Assets — réglementation crypto UE 2024 |
| **Mirror trading** | Ordres d'achat/vente identiques sur deux marchés pour transférer de la valeur |
| **MLA** | Mutual Legal Assistance — commission rogatoire internationale |
| **MT103** | Message SWIFT pour les virements clients internationaux |
| **MT202** | Message SWIFT pour les transferts interbancaires |
| **Mule** | Personne qui prête son compte bancaire pour faire transiter des fonds illicites |
| **Nesting** | Une institution financière étrangère accède au système via le compte d'une correspondante |
| **Nominee** | Tiers prêtant son nom comme dirigeant ou actionnaire |
| **Nostro / Vostro** | Comptes que les banques correspondantes maintiennent les unes chez les autres |
| **PEP** | Politically Exposed Person — personne politiquement exposée |
| **Phantom shipment** | Marchandise facturée mais jamais expédiée |
| **Placement** | 1ère phase du blanchiment — introduction dans le système financier |
| **PNF** | Parquet National Financier (France) |
| **Predicate offense** | Infraction prédécesseur — le crime qui génère les fonds blanchis |
| **PSP** | Payment Service Provider — prestataire de services de paiement |
| **Round-tripping** | Fonds envoyés offshore puis réinjectés comme investissement étranger |
| **SCI** | Société Civile Immobilière — véhicule d'investissement immobilier français |
| **Shell company** | Société écran sans activité réelle |
| **Smurfing** | Structuration — fractionnement des dépôts sous les seuils de déclaration |
| **Structuration** | Fractionnement des opérations pour éviter les seuils de surveillance |
| **SWIFT** | Society for Worldwide Interbank Financial Telecommunication |
| **TBML** | Trade-Based Money Laundering — blanchiment par le commerce |
| **TLP** | Traffic Light Protocol (RED/AMBER/GREEN/CLEAR) |
| **TRACFIN** | Traitement du Renseignement et Action contre les Circuits FINanciers clandestins (CRF française) |
| **Trust** | Structure juridique séparant propriété légale et bénéficiaire |
| **UBO** | Ultimate Beneficial Owner — bénéficiaire effectif réel |
| **VASP** | Virtual Asset Service Provider — prestataire de services crypto |

---

### Annexe B — Typologies GAFI de référence

| Typologie | Description | Red flags | Secteurs |
|-----------|-------------|-----------|----------|
| Structuration / Smurfing | Fractionnement sous les seuils | Montants récurrents < seuil, agences multiples | Bancaire, espèces |
| Sociétés écrans en cascade | Chaîne A→B→C→D multi-juridictions | Sociétés sans substance, nominees, juridictions opaques | Corporate, offshore |
| TBML — Surfacturation | Export à prix gonflé | Prix > marché, volumes irréalistes, routes atypiques | Commerce international |
| TBML — Phantom shipments | Marchandises facturées non livrées | Documents falsifiés, pas de trace logistique | Commerce international |
| Prêts back-to-back | Dépôt offshore → prêt « propre » | Prêt sans conditions de marché, même banque | Bancaire, offshore |
| Round-tripping | Fonds offshore → investissement « étranger » | Flux circulaires, mêmes dates, mêmes montants | Corporate, investissement |
| Commerce cash-intensive | Gonflement des recettes en espèces | CA incohérent, marge anormale, charges faibles | Restauration, retail |
| Immobilier | Achat via SCI/offshore, surévaluation | Apport en cash, société sans substance, PEP | Immobilier |
| Carrousel TVA | Missing trader dans chaîne intracommunautaire | Sociétés éphémères, même marchandise, CA immédiat | Commerce intra-UE |
| Mirror trading | Ordres identiques sur deux marchés | Transactions simultanées, mêmes montants, mêmes parties | Marchés financiers |
| Corruption via sociétés de conseil | Facturation fictive de « services » | Prestations non documentées, PEP, juridictions opaques | Conseil, BTP, énergie |
| Hawala / compensation | Transfert sans mouvement bancaire | Flux commerciaux incohérents, mouvements d'espèces | Informel, diaspora |
| BEC / fraude au virement | Compromission email → virement détourné | Changement de RIB, urgence, montant inhabituel | Entreprises |
| Réseau de mules | Distribution via comptes de particuliers | Multiples virements entrants/sortants, jeunes comptes | Bancaire, fintech |
| Crypto → fiat | Conversion crypto en espèces ou virements | Flux depuis exchanges, OTC desks, structuration | Crypto, bancaire |

---

### Annexe C — Lire un message SWIFT MT103

```
Structure d'un message MT103 (virement client international)

:20:  Référence de la transaction (unique)
:23B: Code opération (CRED = crédit)
:32A: Date valeur + Montant + Devise
      Exemple : 250315EUR95000,00  →  15/03/2025, 95 000 €
:50K: Donneur d'ordre (ordering customer)
      Nom, adresse, numéro de compte/IBAN
:52A: Banque du donneur d'ordre (ordering institution)
      BIC de la banque d'origine
:53A: Banque correspondante de l'expéditeur (sender's correspondent)
      BIC de la banque intermédiaire côté expéditeur
:54A: Banque correspondante du bénéficiaire (receiver's correspondent)
      BIC de la banque intermédiaire côté bénéficiaire
:57A: Banque du bénéficiaire (account with institution)
      BIC de la banque du bénéficiaire
:59:  Bénéficiaire (beneficiary customer)
      Nom, adresse, numéro de compte/IBAN
:70:  Motif du paiement (remittance information)
      Libellé libre — souvent vague dans les cas suspects
:71A: Frais (OUR/SHA/BEN)
      OUR = expéditeur paie tout, SHA = partagé, BEN = bénéficiaire paie
:72:  Informations complémentaires

CE QUE L'ANALYSTE CHERCHE :
- :50K et :59: — qui paie qui ?
- :52A, :53A, :54A, :57A — par quelles banques transitent les fonds ?
- :32A — combien, quand, quelle devise ?
- :70: — le motif est-il cohérent avec l'activité déclarée ?
- La chaîne de correspondants — y a-t-il des intermédiaires inhabituels ?
```

---

### Annexe D — Red flags par catégorie

| Catégorie | Red flag | Exemple | Détection |
|-----------|----------|---------|-----------|
| **Blanchiment général** | Flux incohérents avec l'activité | Compte perso avec virements internationaux 200K€ | Monitoring bancaire |
| | Structuration | Dépôts espèces 9 800 €, 14 500 €, 12 300 € | Scénario AML |
| | Flux circulaires | A → B → C → A même montants | Analyse de flux CRF |
| | PEP avec patrimoine incohérent | Ancien ministre, 5 appartements Paris | OSINT + données fiscales |
| **TBML** | Prix incohérent avec le marché | Composants électroniques à 10x le prix de marché | Données douanières |
| | Volume irréaliste | 10 000 tonnes exportées par une société de 2 personnes | Registre + douanes |
| | Route commerciale atypique | Textile France → Dubaï → Bénin | Factures, BL |
| **Fraude fiscale** | Comptes non déclarés | Compte UBS Suisse non déclaré à la DGFIP | EAR/CRS |
| | Sociétés offshore sans substance | BVI company, pas d'employés, pas de site web | OSINT + registres |
| **Corruption** | Facturation de « conseil » sans prestation | Société BVI facture 2M€ de « strategic advisory » | Comptabilité forensique |
| | Commissions sur marchés publics | 10% du montant du marché → société offshore | Analyse de flux |
| **FT** | Flux vers zones de conflit | Virements vers Syrie, Irak, Somalie | Screening géographique |
| | Collectes via associations | ONG avec flux incohérents avec l'objet social | DS, OSINT |
| **Fintech/PSP** | Layering rapide multi-comptes | 5 virements Revolut en 2h vers 5 pays | Monitoring PSP |
| | IBAN exotique sans justification | Compte LT/EE pour un résident français sans lien | KYC, monitoring |
| | Cartes prépayées en volume | Achat de 20 cartes prépayées 250€ en cash | Point de vente |
| **BEC** | Changement de RIB fournisseur | « Nouveau RIB, merci de virer sur ce compte » | Procédure interne |
| | Urgence inhabituelle | « Virement urgent ordre du PDG, confidentiel » | Sensibilisation |

---

### Annexe E — Templates de livrables FININT

#### Note d'analyse FININT (structure)

```
EN-TÊTE
  Référence : [FININT-2025-XXXX]
  Date : [JJ/MM/AAAA]
  Classification : [TLP:RED/AMBER/GREEN/CLEAR]
  Auteur : [Nom, fonction]
  Demandeur : [Département / sollicitation / auto-saisine]
  Version : [1.0]

OBJET
  Résumé en 2-3 lignes

CONTEXTE
  Sollicitation, DS de référence, périmètre, délai

MÉTHODOLOGIE
  Sources consultées (avec cadre juridique d'accès pour chaque)
  Outils utilisés
  Période d'analyse
  Blockchains analysées (le cas échéant — renvoi rapport crypto)

RECONSTITUTION DES FLUX
  Diagramme de flux annoté (graphe)
  Tableau des transactions clés (date, montant, émetteur, bénéficiaire, libellé)

ANALYSE DU SCHÉMA
  Typologie identifiée (blanchiment, TBML, carrousel, corruption...)
  Phases identifiées (placement, layering, intégration)
  Cohérence / incohérence avec une activité légitime

PROFIL DES ACTEURS
  Pour chaque acteur : identité, rôle dans le schéma, sociétés liées, patrimoine

ANALYSE PATRIMONIALE
  Patrimoine identifié vs revenus déclarés
  Sources des acquisitions

CONCLUSIONS
  Réponse aux questions de renseignement
  Niveau de confiance pour chaque conclusion (fait / inférence / hypothèse)

LACUNES
  Sources non consultées, juridictions non couvertes, données manquantes

RECOMMANDATIONS
  Signalement au parquet (oui/non, motifs)
  Gel (droit d'opposition, comptes/biens visés)
  Saisie (AGRASC, biens visés)
  Dissémination Egmont (CRF destinataires, informations partagées)
  Investigations complémentaires (réquisitions, OSINT, crypto)

ANNEXES
  Graphe de flux, graphe de liens, timeline, tableaux d'adresses
```

#### Rapport de flux (structure)

```
EN-TÊTE : Référence | Date | Classification
PÉRIMÈTRE : Comptes analysés, période, sources
DIAGRAMME DE FLUX : Graphe annoté (montants, directions, dates, services)
TABLEAU DES FLUX : Date | Émetteur (nom+IBAN) | Bénéficiaire (nom+IBAN) | Montant | Devise | Libellé | Observations
PATTERNS IDENTIFIÉS : Structuration, circularité, récurrence, anomalies
SERVICES BANCAIRES : Banques impliquées, correspondants, PSP/fintech
CONCLUSIONS : Schéma de flux global, volume total, direction dominante
NIVEAUX DE CONFIANCE : Par attribution et par conclusion
```

---

### Annexe F — Mapping de la bibliothèque

| Thématique | Cours principal | Cours complémentaires |
|-----------|----------------|----------------------|
| Investigation financière traditionnelle | **Ce cours (FININT)** | — |
| Investigation OSINT + blockchain | **Cours OSINT Crypto** | FININT (Ch.22-23 convergence, Ch.25 volet crypto) |
| OSINT techniques générales | **Cours OSINT Mastery** | FININT (Ch.14 sources OSINT, Ch.12 OSINT patrimoine) |
| Intelligence économique | **Cours IE** | FININT (Ch.5-6 montages financiers, Ch.13 structures opaques) |
| CTI (renseignement de menace) | **Cours CTI** | FININT (Ch.16-17 méthodologie analytique — même rigueur) |
| Écosystèmes cybercriminels | **Cours Écosystèmes** | FININT (Ch.22 convergence cyber-FININT, Ch.28 BEC) |
| Dark web | **Cours Dark Web** | FININT (Ch.17 darknet markets — dimension financière) |
| APT | **Cours APT** | FININT (Ch.22 DPRK/Lazarus financement) |
| SOC / IR | **Cours SOC / IR** | FININT (Ch.22 BEC — articulation SOC→FININT) |
| GRC | **Cours GRC** | FININT (Ch.2 compliance AML, Ch.20 régulations) |

---

### Annexe G — Ressources et formation

#### Formations et certifications

| Formation | Organisme | Focus |
|-----------|----------|-------|
| CAMS (Certified Anti-Money Laundering Specialist) | ACAMS | AML compliance — la certification de référence mondiale |
| ICA Diploma in AML | International Compliance Association | AML avancé — reconnu en Europe |
| Certified Financial Crime Specialist (CFCS) | ACFCS | Investigation financière globale |
| Certified Cryptocurrency Investigator | Chainalysis | Traçage blockchain (complément crypto) |
| SANS FOR498 | SANS | OSINT formalisé (complément OSINT) |
| CFE (Certified Fraud Examiner) | ACFE | Fraude et investigation |

#### Institutions de référence

| Institution | Rôle | Ressources |
|------------|------|-----------|
| GAFI / FATF | Normes AML/CFT mondiales | 40 recommandations, typologies, évaluations mutuelles |
| TRACFIN | CRF française | Rapport annuel (cas anonymisés), tendances |
| Egmont Group | Réseau mondial de CRF | Best practices, typologies |
| Europol EFECC | Criminalité financière européenne | SOCTA, IOCTA, opérations |
| AGRASC | Recouvrement d'actifs (France) | Rapport annuel, statistiques saisies |
| PNF | Parquet financier (France) | Affaires emblématiques, jurisprudence |
| ACPR | Supervision bancaire (France) | Sanctions, recommandations AML |

#### Rapports annuels de référence

| Rapport | Éditeur | Contenu |
|---------|---------|---------|
| Rapport annuel TRACFIN | TRACFIN | Cas anonymisés, tendances, statistiques DS |
| GAFI Typologies Reports | FATF | Schémas de blanchiment documentés |
| Europol SOCTA | Europol | Évaluation des menaces criminelles EU |
| Europol IOCTA | Europol | Menaces cyber organisées |
| Chainalysis Crypto Crime Report | Chainalysis | Criminalité crypto, tendances |
| TRM Labs Illicit Finance Report | TRM Labs | Blanchiment crypto, sanctions |
| UNODC World Drug Report | UNODC | Trafic de stupéfiants mondial — flux financiers |

#### Conférences et communautés

| Événement | Focus |
|-----------|-------|
| ACAMS Annual Conference | AML compliance, investigation financière |
| Cambridge Economic Crime Symposium | Criminalité économique, recherche |
| Chatham House Financial Crime | Politique et régulation |
| Europol Financial Intelligence Group | Coopération LEA |
| Chainalysis LINKS | Investigation crypto |

---

> **Note de clôture**
>
> Ce cours a été conçu pour former à l'investigation financière comme discipline de renseignement — la capacité à suivre l'argent dans l'économie réelle, à travers les banques, les sociétés écrans, les juridictions opaques, les systèmes informels, et les rails de paiement modernes.
>
> L'opération CLEARSTREAM illustre la réalité opérationnelle d'une investigation FININT : 14 DS convergentes, 5 juridictions, 3 techniques de blanchiment combinées (TBML, cascade de sociétés, conversion crypto), et un réseau d'acteurs qui va du prête-nom béninois au gestionnaire de fortune suisse. L'analyste qui maîtrise les flux bancaires, la comptabilité forensique, les structures opaques, et la coopération internationale peut reconstituer ces schémas — et recommander les actions qui mènent au gel, à la saisie, et à la confiscation.
>
> Le cours assume trois convictions. Première : le renseignement n'est pas une preuve — la rigueur dans la distinction entre ce que l'on sait, ce que l'on infère, et ce que l'on suppose protège l'analyste, le service, et l'exploitabilité ultérieure du renseignement. Deuxième : le blanchiment est une discipline technique — les schémas sont sophistiqués mais ils laissent des traces, et l'analyste formé sait où les chercher. Troisième : le FININT ne travaille jamais seul — la convergence avec l'OSINT, la crypto-investigation, et la coopération internationale est ce qui transforme un faisceau d'indices en renseignement actionnable.
>
> *Suivre l'argent • Reconstituer les schémas • Produire le renseignement — avec rigueur et discernement.*

