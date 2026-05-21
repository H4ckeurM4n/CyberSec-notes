# INVESTIGATION FINANCIÈRE & RENSEIGNEMENT FINANCIER — FININT

*Suivre l’argent dans l’économie réelle — Registres, sociétés, bénéficiaires effectifs, flux bancaires, criminalité financière et asset recovery*

**Cours complet — 10 parties • 70 chapitres + 1 chapitre 0 de mise à niveau • 14 annexes • 1 parcours express • 1 fil rouge • 3 parcours de lecture**

*Renseignement financier • OSINT financier • LCB-FT • Analyse de flux • Comptabilité forensique • Coopération internationale • Asset recovery*

-----

## Avant-propos

### À qui s’adresse ce cours

Ce cours est destiné à toute personne qui doit, dans son activité professionnelle ou en formation avancée, **comprendre et pratiquer le renseignement financier** : analystes en cellule de renseignement financier (CRF), enquêteurs financiers, analystes compliance et LCB-FT, auditeurs forensiques, journalistes d’investigation, analystes OSINT financiers, profils GRC, professionnels du contentieux fiscal et douanier, équipes de threat intelligence amenées à croiser cyber et finance, et plus largement toute personne en charge de qualifier des soupçons, de cartographier des structures économiques opaques ou de tracer des avoirs.

Ce cours **ne suppose aucune spécialisation préalable** en LCB-FT, en investigation financière, en comptabilité, en droit financier ou en économie. Il commence par un **chapitre 0 de mise à niveau** permettant à un lecteur débutant d’acquérir les repères essentiels (entreprise, flux financiers, documents, comptabilité minimale, acteurs d’un dossier, notions juridiques, types de sources) avant d’aborder les méthodes FININT. La progression est introductive dans son rythme et professionnelle dans sa profondeur : un débutant peut le suivre dans l’ordre, un praticien peut y revenir comme référence par chapitre.

### Ce que ce cours est — et ce qu’il n’est pas

Ce cours **est** : un manuel d’enquête, méthodologique, opérationnel, calibré pour une pratique réelle. Il fournit des modèles de fiches, des matrices, des checklists, des walkthroughs, des templates, des cas pratiques déroulés et des cas historiques exploités comme leçons. Il distingue systématiquement ce qui est observable, ce qui est inféré, ce qui est probable, ce qui est indémontrable et ce qui nécessite une autorité compétente. Il calibre la confiance par une échelle inspirée des Words of Estimative Probability et il apprend à écrire avec rigueur — *« compatible avec »*, *« cohérent avec »*, *« hypothèse calibrée »*, plutôt qu’affirmations péremptoires.

Ce cours **n’est pas** : un manuel pour commettre une infraction, un guide pour échapper à la traçabilité, un cours de comptabilité générale, un précis de droit pénal des affaires, un manuel de l’enquête judiciaire ou un catalogue d’outils. Il ne refait pas l’enquête blockchain (renvoi systématique au cours OSINT Crypto pour le volet on-chain), ni l’OSINT général (renvoi aux cours OSINT correspondants).

### Posture éthique et déontologique

Le FININT est une discipline qui touche aux libertés individuelles, au secret bancaire, à la vie privée, à la réputation et, dans certains cas, à la liberté de personnes. Une note d’analyse mal calibrée, un soupçon pris pour une preuve, une diffusion non maîtrisée, une confusion entre renseignement et accusation peuvent causer des dommages réels — y compris à des personnes innocentes ou non concernées. La rigueur méthodologique n’est pas un luxe académique : elle est la condition même de la légitimité de la discipline. Tout au long du cours, cette rigueur est présentée comme un réflexe, pas comme un appendice.

Le cours adopte une posture **strictement défensive, analytique, conformité et investigative**. Lorsqu’une typologie criminelle est expliquée, c’est sous l’angle de la compréhension, de la détection, de l’investigation, de la prévention, du signalement et de la coopération. Aucune section ne fournit de méthode pour blanchir, frauder ou échapper aux contrôles.

### Cohérence avec le reste du corpus

Ce cours est complémentaire d’un **cours OSINT Crypto** dédié à l’enquête on-chain (blockchains, wallets, mixers, bridges, DEX, privacy coins, cashout crypto). Quand un dossier comporte une branche crypto, le cours FININT cadre le contexte financier (KYB de l’exchange, mules, BEC, sociétés écrans, conformité du VASP) et **renvoie explicitement** vers OSINT Crypto pour le traçage on-chain détaillé. Cette séparation est volontaire : refaire le traçage blockchain ici diluerait la spécificité FININT.

Des renvois ponctuels existent également vers d’autres cours du corpus quand pertinent (OSINT général, CTI, GRC, Dark Web).

### Mode d’emploi du cours

- **Lecture linéaire** : la progression Partie I → X est conçue pour un apprentissage cumulatif. Les notions des Parties I et II sont mobilisées dans les suivantes.
- **Lecture par référence** : chaque chapitre est autonome ; l’index, la table des matières et le glossaire (annexe A) permettent un usage à la demande.
- **Parcours express** : pour produire une **première fiche FININT en 45 minutes** à partir d’un simple nom de société ou de personne — utile en formation initiale, en sollicitation urgente, ou en exercice d’auto-évaluation.
- **Fil rouge CLEARFLOW** : un cas fictif, réaliste, qui traverse l’ensemble du cours sous forme d’encadrés courts, et qui est synthétisé au chapitre 64.
- **Annexes opérationnelles** : 14 annexes prêtes à copier dans un dossier d’enquête (fiches, matrices, glossaire, modèle de note, registres par pays, outils par usage, cadres d’accès aux sources, bibliographie de sources primaires).

### Conventions de notation

Plusieurs conventions sont utilisées tout au long du cours :

- **Encadré CLEARFLOW** : illustration du chapitre courant via le fil rouge.
- **Méthode** : procédure étape par étape.
- **Erreurs fréquentes** : pièges identifiés, à éviter en pratique.
- **Limites** : ce que la méthode ne permet pas, ou seulement sous condition.
- **Renvoi** : pointeur vers un autre chapitre, une annexe ou un autre cours.
- **WEP** : niveau de confiance (échelle Words of Estimative Probability — chapitre 33).
- **Quasi-certain / Très probable / Probable / Possible / Peu probable / Très peu probable / Indéterminable** : niveaux WEP utilisés en pratique.

### Actualité

Le cours est calibré pour la période **2025-2026** : paquet AML européen et création de l’AMLA, transposition LCB-FT, MiCA et Travel Rule (uniquement quand elles croisent les crypto-actifs), évolutions GAFI, pratiques TRACFIN, sanctions OFAC/UE/ONU, accès aux registres UBO post-arrêt CJUE 2022, fraudes BEC modernes, néobanques, fintechs, stablecoins comme rail de blanchiment. Lorsqu’une donnée est susceptible d’évoluer rapidement, le cours le signale et oriente vers la source primaire.

-----

## Table des matières

- [Avant-propos](#avant-propos)
- [Chapitre 0 — Mise à niveau : les bases économiques, juridiques et financières indispensables](#chapitre-0--mise-à-niveau--les-bases-économiques-juridiques-et-financières-indispensables)
- [Parcours express — Lire un dossier financier en 45 minutes](#parcours-express--lire-un-dossier-financier-en-45-minutes)
- [Fil rouge — Opération CLEARFLOW](#fil-rouge--opération-clearflow)

**PARTIE I — COMPRENDRE LE RENSEIGNEMENT FINANCIER**

- Ch.0 — Mise à niveau : les bases économiques, juridiques et financières indispensables
- Ch.1 — Pourquoi le FININT est central aujourd’hui
- Ch.2 — Ce que le FININT permet vraiment
- Ch.3 — Ce que le FININT ne permet pas
- Ch.4 — Renseignement, soupçon, preuve et judiciarisation
- Ch.5 — FININT, OSINT financier, AML, CTI et OSINT Crypto

**PARTIE II — LE SYSTÈME FINANCIER POUR L’ENQUÊTEUR**

- Ch.6 — Le système bancaire et la circulation de l’argent
- Ch.7 — Rails de paiement : SWIFT, SEPA, TARGET2, Fedwire, ACH
- Ch.8 — PSP, EME, néobanques et fintechs
- Ch.9 — Comptes bancaires, relevés et opérations
- Ch.10 — Offshore, secret bancaire et juridictions opaques

**PARTIE III — SOURCES OSINT FINANCIÈRES**

- Ch.11 — Registres d’entreprises : France, UK, US
- Ch.12 — Registres d’entreprises : reste de l’Europe et du monde
- Ch.13 — Identifier les bénéficiaires effectifs
- Ch.14 — Comptes annuels, bilans et documents financiers
- Ch.15 — Marchés publics, subventions et appels d’offres
- Ch.16 — Contentieux, procédures collectives et sanctions administratives
- Ch.17 — Presse, adverse media et SOCMINT financier
- Ch.18 — Leaks financiers : ICIJ, OCCRP, Aleph, Panama/Pandora

**PARTIE IV — PERSONNES, SOCIÉTÉS ET CONTRÔLE**

- Ch.19 — Identifier une personne physique sans se tromper d’homonyme
- Ch.20 — Identifier une société et ses variantes internationales
- Ch.21 — Formes juridiques comparées
- Ch.22 — Dirigeants, mandataires et administrateurs
- Ch.23 — Actionnaires, UBO et contrôle indirect
- Ch.24 — Holdings, filiales et montages en cascade
- Ch.25 — Trusts, fondations, nominees et prête-noms
- Ch.26 — Sociétés écrans et sociétés dormantes

**PARTIE V — CARTOGRAPHIER LES RÉSEAUX FINANCIERS**

- Ch.27 — Construire une fiche personne
- Ch.28 — Construire une fiche société
- Ch.29 — Construire une fiche flux
- Ch.30 — Construire une fiche actif
- Ch.31 — Graphes relationnels FININT
- Ch.32 — Distinguer lien faible, lien fort et contrôle réel
- Ch.33 — Échelle de confiance WEP et hypothèses calibrées

**PARTIE VI — ANALYSE DE FLUX ET COMPTABILITÉ FORENSIQUE**

- Ch.34 — Lire un relevé bancaire
- Ch.35 — Reconstituer des flux financiers
- Ch.36 — Lire un bilan et un compte de résultat
- Ch.37 — Détecter anomalies comptables et signaux faibles
- Ch.38 — Factures, marges, marchandises et cohérence économique
- Ch.39 — Reconstitution patrimoniale et train de vie

**PARTIE VII — TYPOLOGIES DE CRIMINALITÉ FINANCIÈRE**

- Ch.40 — Blanchiment : placement, empilement, intégration
- Ch.41 — Trade-Based Money Laundering
- Ch.42 — Corruption, commissions occultes et PEP
- Ch.43 — Fraude fiscale, carrousel TVA et abus de biens sociaux
- Ch.44 — BEC, fraude au fournisseur et réseaux de mules
- Ch.45 — Contournement de sanctions et biens dual-use
- Ch.46 — Ponzi, pyramides et fraudes à l’investissement
- Ch.47 — Criminalité organisée et économie légale
- Ch.48 — Cybercriminalité, cashout et renvoi vers OSINT Crypto

**PARTIE VIII — OUTILS, WORKFLOW ET PRODUCTION**

- Ch.49 — Workflow complet d’une enquête FININT
- Ch.50 — Outils gratuits : registres, sanctions, presse, leaks
- Ch.51 — Outils professionnels : Sayari, Orbis, World-Check, Dow Jones, LexisNexis
- Ch.52 — Visualisation : Maltego, i2, Linkurious, Gephi, Graphistry
- Ch.53 — Chaîne de preuve, captures, horodatage, hash
- Ch.54 — Note FININT, rapport et diffusion

**PARTIE IX — CAS PRATIQUES DÉROULÉS**

- Ch.55 — Cas 1 : Société écran et fournisseur suspect
- Ch.56 — Cas 2 : Fraude au changement d’IBAN / BEC
- Ch.57 — Cas 3 : Corruption internationale et PEP
- Ch.58 — Cas 4 : Contournement de sanctions via pays tiers
- Ch.59 — Cas 5 : Asset tracing d’un dirigeant sous enquête

**PARTIE X — CAS HISTORIQUES, COOPÉRATION ET PROFESSIONNALISATION**

- Ch.60 — Panama Papers : leak, offshore et journalisme d’investigation
- Ch.61 — 1MDB : corruption, banques, luxe et asset recovery
- Ch.62 — Wirecard : fraude comptable et défaillance systémique
- Ch.63 — Danske Bank Estonia : blanchiment massif et supervision défaillante
- Ch.64 — Synthèse du fil rouge CLEARFLOW
- Ch.65 — Coopération internationale : Egmont, GAFI, Europol, FIU
- Ch.66 — Gel, saisie, confiscation et asset recovery
- Ch.67 — Cadre français : TRACFIN, ACPR, AMF, PNF, AGRASC
- Ch.68 — Éthique, RGPD, secret bancaire et limites
- Ch.69 — Construire une capacité FININT durable
- Ch.70 — Évolutions réglementaires 2024-2026 : mise à niveau

**ANNEXES**

- A — Glossaire opérationnel FININT
- B — Lire SWIFT MT103, MT202, MT940
- C — Modèle de fiche personne
- D — Modèle de fiche société
- E — Modèle de fiche flux
- F — Modèle de fiche actif
- G — Matrice des red flags FININT
- H — Matrice « ce que je peux conclure / ne peux pas conclure »
- I — Registres et sources par pays
- J — Outils par usage
- K — Modèle de note FININT
- L — Erreurs fréquentes + 5 mini-cas d’entraînement
- M — Cadres d’accès aux sources
- N — Bibliographie de sources primaires

**PARCOURS DE LECTURE RECOMMANDÉS** (placés après les annexes)

- Parcours débutant — première découverte du FININT
- Parcours analyste FININT — formation cœur
- Parcours expert / institutionnel — vision stratégique

-----

## Chapitre 0 — Mise à niveau : les bases économiques, juridiques et financières indispensables

### Objectif du chapitre

Donner à un lecteur débutant les bases nécessaires pour suivre le cours sans se sentir perdu. Ce chapitre ne transforme pas le lecteur en juriste, en comptable ou en banquier — il fournit les **repères indispensables** pour comprendre les chapitres FININT qui suivent. Un lecteur déjà familier de l’environnement économique, juridique et financier peut survoler ce chapitre ; un débutant y prend une heure ou deux pour s’installer dans le vocabulaire et les concepts.

-----

### 0.1 — Comprendre ce qu’est une entreprise

#### Personne physique et personne morale

Une **personne physique** est un être humain. Elle a un nom, une date de naissance, une nationalité, une adresse. Elle peut posséder des biens, signer des contrats, ouvrir un compte bancaire, et être tenue responsable de ses actes.

Une **personne morale** est une **entité juridique** créée par le droit. Elle n’a pas de corps physique mais elle est traitée par le droit comme un sujet de droits et d’obligations. Une société, une association, une fondation sont des personnes morales. Elles peuvent, comme les personnes physiques, posséder des biens, ouvrir un compte bancaire, signer des contrats, recevoir des paiements, et être poursuivies en justice.

> **À retenir** : derrière toute société, il y a des personnes physiques (dirigeants, associés, bénéficiaires effectifs). L’enquête FININT cherche souvent à comprendre **qui contrôle réellement cette personne morale**.

#### Les formes courantes d’entités

- **Société** : entité créée pour exercer une activité économique, généralement à but lucratif (SAS, SARL, SA, Ltd, GmbH, LLC, etc. — détaillé chapitre 21).
- **Association** : entité à but non lucratif. En France, association loi 1901.
- **Fondation** : entité dotée d’un patrimoine affecté à un but d’intérêt général ou privé (fondations Liechtenstein, Panama, etc. — chapitre 25).
- **Trust** : relation juridique de droit anglo-saxon où une personne (trustee) détient et gère des biens pour le compte d’autres personnes (bénéficiaires). Le trust **n’est pas** une entité juridique distincte au sens continental, mais il est traité par l’enquête FININT comme un acteur (chapitre 25).

#### Siège, établissement, filiale, holding

- **Siège social** : adresse officielle déclarée d’une société. Lieu juridique.
- **Établissement** : lieu physique où s’exerce une activité. Une société peut avoir plusieurs établissements (établissements secondaires).
- **Filiale** : société contrôlée par une autre société (la société mère).
- **Holding** : société dont l’activité principale est de détenir des participations dans d’autres sociétés (filiales). Pas (ou peu) d’activité opérationnelle propre.

#### Dirigeant, actionnaire, associé, mandataire

- **Dirigeant** : personne qui dirige la société (président, gérant, directeur général). Désigné selon la forme juridique.
- **Actionnaire** ou **associé** : personne (physique ou morale) qui détient le capital de la société. Un associé d’une SARL ou SAS, un actionnaire d’une SA.
- **Mandataire** : toute personne qui exerce un mandat dans la société (dirigeants, administrateurs, commissaires aux comptes, etc.).

#### Trois grandes catégories d’entités vues du FININT

- **Société opérationnelle** : exerce une activité économique réelle (vente de biens, prestation de services). Elle a des clients, des fournisseurs, des salariés, des locaux, du chiffre d’affaires.
- **Société holding** : détient des participations. Souvent peu ou pas d’activité propre, mais cela peut être légitime (gouvernance, optimisation, structuration).
- **Société écran** : entité juridique sans activité économique réelle propre, créée pour porter une finalité spécifique sans substance opérationnelle (chapitre 26). Peut être légitime (SPV, holding patrimonial) ou suspecte (transit financier, opacification).

> **Exemple simple** : une société est une personne morale. Elle peut avoir un compte bancaire, signer des contrats, acheter un bien immobilier, recevoir des paiements, et être poursuivie en justice. L’enquête FININT cherche souvent à comprendre **qui contrôle réellement** cette personne morale, et **dans quel but**.

-----

### 0.2 — Comprendre les flux financiers

#### Compte bancaire

Un **compte bancaire** est un compte ouvert au nom d’une personne (physique ou morale) auprès d’une banque ou d’un PSP. Il enregistre des **opérations** : crédits (entrées d’argent) et débits (sorties).

- **Solde** : montant disponible sur le compte à une date donnée.
- **Devise** : monnaie du compte (EUR, USD, GBP, CHF, JPY, etc.). Un même titulaire peut avoir des comptes en plusieurs devises.

#### Virement

Un **virement** est un transfert d’argent d’un compte vers un autre.

- **Donneur d’ordre** : celui qui ordonne le virement (le titulaire du compte débité).
- **Bénéficiaire** : celui qui reçoit (le titulaire du compte crédité).
- **Banque émettrice** : banque qui exécute l’ordre du donneur.
- **Banque réceptrice** : banque qui crédite le bénéficiaire.
- **Libellé** : texte associé au virement (ex. « paiement facture XXX », « salaire octobre », « prêt »). Le libellé est déclaré par le donneur d’ordre, il n’est pas vérifié par la banque.

#### IBAN et BIC

- **IBAN (International Bank Account Number)** : identifiant standardisé d’un compte bancaire. Commence par le code pays sur 2 lettres (FR pour France, ES pour Espagne, GB pour UK, etc.), suivi de chiffres et lettres. Exemple : `FR76 1234 5678 9012 3456 7890 123`.
- **BIC (Bank Identifier Code)** : identifiant SWIFT d’une banque (ex. `BNPAFRPP` pour BNP Paribas France).

#### Paiement national, européen, international

- **Paiement national** : entre deux comptes français. Rapide, peu cher.
- **Paiement européen — SEPA** : entre deux comptes de la zone SEPA (36 pays). Standard européen. Existe en version classique (SCT) et instantanée (SCT Inst, qui crédite le bénéficiaire en quelques secondes mais est irréversible).
- **Paiement international — SWIFT** : entre deux comptes dans des pays différents (notamment hors SEPA). Passe par des **banques correspondantes** qui relaient le paiement. Plus long, plus cher, plus complexe.

> **Exemple FININT** : si une société française reçoit 95 000 € depuis Dubaï avec le libellé « commercial services », l’analyste **ne conclut pas** que c’est suspect. Il se demande : qui paie ? pourquoi ? pour quelle prestation ? est-ce cohérent avec l’activité déclarée de la société ? Quel est le donneur d’ordre réel derrière le compte émetteur ? Cette discipline d’interrogation, sans jugement immédiat, est l’esprit du FININT.

-----

### 0.3 — Comprendre les documents de base

Voici les documents qu’un analyste FININT rencontre régulièrement, et leur rôle :

- **Extrait de registre d’entreprise** (Kbis en France, Companies House extract au UK, etc.) : document officiel attestant de l’existence d’une société, indiquant sa dénomination, son siège, sa forme juridique, ses dirigeants, sa date de création. C’est la « pièce d’identité » de la société.
- **Statuts** : document fondateur d’une société. Définit son objet social, sa gouvernance, le pouvoir de ses dirigeants, les règles de cession des parts, etc.
- **Facture** : document émis par un vendeur ou prestataire, demandant paiement à un client. Détaille la prestation, la quantité, le prix, la TVA, l’échéance.
- **Contrat** : document liant deux ou plusieurs parties par des obligations réciproques (vente, prestation de services, prêt, location, etc.).
- **Relevé bancaire** : document récapitulant les opérations d’un compte sur une période (mois, trimestre, année). Émis par la banque.
- **Bilan** : photographie du patrimoine de la société à une date (actif = ce qu’elle possède, passif = ce qu’elle doit).
- **Compte de résultat** : récapitulatif des produits et charges sur une période. Permet de calculer le résultat (bénéfice ou perte).
- **Déclaration de bénéficiaire effectif** : déclaration au registre des UBO précisant qui contrôle ultimement la société.
- **Article de presse** : source d’information journalistique, à recouper avec d’autres sources avant utilisation.
- **Décision de justice** : jugement, ordonnance, arrêt. Si public, source précieuse pour comprendre des contentieux passés.

> L’objectif du FININT n’est pas de faire un cours de comptabilité ou de droit, mais de **savoir à quoi sert chaque document** dans une enquête, et **où trouver l’information** dont on a besoin.

-----

### 0.4 — Comprendre la logique comptable minimale

Pas besoin d’être comptable pour faire du FININT. Mais quelques notions sont indispensables :

- **Chiffre d’affaires (CA)** : somme des ventes réalisées sur une période. Indicateur de la « taille » commerciale.
- **Charges** : ce que l’entreprise dépense (achats, salaires, loyers, frais financiers, etc.).
- **Bénéfice / perte (résultat)** : différence entre produits et charges. Bénéfice si positif, perte si négatif.
- **Actif** : tout ce que possède l’entreprise (immobilier, matériel, créances clients, trésorerie, participations, etc.).
- **Passif** : tout ce que doit l’entreprise (capital et réserves, dettes financières, dettes fournisseurs, dettes fiscales et sociales, etc.).
- **Trésorerie** : argent disponible immédiatement (sur les comptes bancaires, en caisse).
- **Dettes** : ce que l’entreprise doit à des tiers (banques, fournisseurs, État, etc.).
- **Créances** : ce qui est dû à l’entreprise (par ses clients, principalement).
- **Marge** : différence entre prix de vente et coût d’achat. Indique la rentabilité d’une activité.
- **Capital social** : apport initial des associés au lancement de la société. Inscrit au passif. Peut être très faible (1 € pour une SAS) ou substantiel.

> **Formulation simple** : le **compte de résultat** raconte ce que l’entreprise a gagné et dépensé pendant une période. Le **bilan** montre ce qu’elle possède et ce qu’elle doit à une date donnée. L’analyste FININT lit ces documents pour vérifier la **cohérence** entre l’activité déclarée et la réalité économique observable.

-----

### 0.5 — Comprendre les acteurs d’un dossier financier

Un dossier FININT mobilise un écosystème d’acteurs. Les principaux :

#### Acteurs économiques

- **Banque** : institution financière qui tient des comptes, exécute des paiements, accorde des crédits. **Assujettie** aux obligations LCB-FT.
- **PSP / fintech** : prestataire de services de paiement (Stripe, Revolut, Wise, etc.). Souvent **assujetti** également.
- **Client** : celui qui achète un bien ou une prestation.
- **Fournisseur** : celui qui vend un bien ou une prestation.

#### Acteurs structurels

- **Société écran** : entité juridique sans substance économique réelle.
- **Prête-nom** : personne qui apparaît officiellement (dirigeant, associé) sans exercer le contrôle réel.
- **Bénéficiaire effectif (UBO)** : personne physique qui contrôle ultimement une entité.

#### Acteurs institutionnels — France principalement

- **TRACFIN** : Cellule de Renseignement Financier française. Reçoit les déclarations de soupçon, produit du renseignement, transmet aux autorités compétentes.
- **Parquet** : magistrats du ministère public, dirigent l’enquête pénale. En France, le **PNF (Parquet National Financier)** est spécialisé sur la criminalité financière complexe.
- **Juge d’instruction** : magistrat indépendant chargé d’instruire un dossier pénal complexe.
- **Autorités fiscales** : en France, la **DGFiP (Direction Générale des Finances Publiques)**. Contrôlent et sanctionnent les manquements fiscaux.
- **Autorités douanières** : en France, la **DGDDI (Direction Générale des Douanes et Droits Indirects)**. Contrôlent les flux de marchandises et certains flux financiers.
- **Superviseurs financiers** : **ACPR** (banques, assurances), **AMF** (marchés financiers et PSAN/CASP). Veillent au respect des règles par les acteurs régulés.

#### Acteurs internationaux

- **CRF étrangères** : équivalents de TRACFIN dans d’autres pays. Coopération via Egmont et FIU.NET (UE).
- **Europol, Interpol, Eurojust, EPPO** : agences européennes ou internationales de coopération policière et judiciaire.

> Comprendre qui fait quoi évite beaucoup d’erreurs : un cabinet privé n’a pas les mêmes pouvoirs qu’un parquet, une banque n’est pas un policier, une CRF n’est pas un tribunal.

-----

### 0.6 — Comprendre les notions juridiques minimales

Quelques distinctions essentielles, que le cours développera ensuite :

- **Soupçon** : intuition étayée d’éléments objectifs. En LCB-FT, il a un **seuil légal** : il déclenche la déclaration de soupçon (DS) par les assujettis. **Le soupçon n’est ni la certitude, ni la preuve.**
- **Preuve** : élément établi de manière formelle, recevable en justice, susceptible de fonder une décision juridictionnelle. Obtenue par des actes d’enquête (réquisitions, auditions, expertises) sous autorité judiciaire.
- **Renseignement** : produit d’analyse qui éclaire une situation, oriente une action, sans avoir la valeur formelle d’une preuve. Le FININT produit du renseignement.
- **Infraction** : comportement interdit par la loi, sanctionné. Peut être un crime, un délit ou une contravention.
- **Blanchiment** : opération de dissimulation de l’origine illicite de fonds.
- **Fraude** : tromperie pour obtenir un avantage indu (fraude fiscale, fraude au virement, etc.).
- **Corruption** : obtention d’un avantage en échange d’un acte illicite par une personne en position de pouvoir.
- **Sanctions** : mesures restrictives imposées contre des personnes, entités, pays (gel d’avoirs, interdiction de transactions, embargos).
- **Gel** : mesure conservatoire empêchant l’usage d’un avoir.
- **Saisie** : mesure judiciaire retenant juridiquement un avoir.
- **Confiscation** : transfert définitif d’un avoir à l’État après condamnation.
- **Présomption d’innocence** : principe selon lequel toute personne est présumée innocente tant qu’elle n’a pas été déclarée coupable par une décision de justice définitive.

> Cette sous-partie prépare une distinction centrale du cours : le **FININT produit du renseignement**, pas automatiquement de la preuve judiciaire. Convertir le renseignement en preuve exige des actes d’enquête conduits sous autorité juridictionnelle. Cette distinction est revue en détail au chapitre 4.

-----

### 0.7 — Comprendre les sources

Les sources mobilisées en FININT n’ont pas toutes le même statut, ni la même accessibilité. Distinguer les catégories est l’une des disciplines essentielles du métier :

- **Source ouverte (OSINT)** : accessible publiquement (registre des sociétés, presse, réseaux sociaux, données ouvertes type DVF). Pas de restriction particulière à son usage par un analyste, hors RGPD et droit d’auteur.
- **Source payante professionnelle** : accessible par abonnement (Sayari, Orbis, World-Check, Factiva). Réservée aux organisations abonnées.
- **Source bancaire** : interne à une banque (KYC, monitoring, données clients). Accessible aux **assujettis LCB-FT** dans le cadre de leurs obligations.
- **Source CRF** : interne à une cellule de renseignement financier (DS reçues, FIU.NET, Egmont). Accessible aux CRF uniquement.
- **Source judiciaire** : accessible sous autorité juridictionnelle (réquisitions bancaires, FICOBA, perquisitions). Réservée aux magistrats et enquêteurs sous procédure.
- **Source fiscale** : accessible aux autorités fiscales (DGFiP), à l’occasion de leurs contrôles ou via les échanges internationaux (EAR/CRS).
- **Source issue d’un leak** : données dévoilées par lanceurs d’alerte (Pandora Papers, Panama Papers). Accessibles selon les modalités définies par les consortiums (ICIJ Offshore Leaks public partiel, Aleph pour journalistes).
- **Source journalistique** : enquêtes publiées par la presse. Soumise à recoupement par l’analyste.

> Comprendre cette typologie évite l’erreur fréquente du débutant : penser que **tout est accessible publiquement**. Beaucoup de données critiques (relevés bancaires détaillés, comptes étrangers, données fiscales) ne sont **pas en OSINT**. L’analyste opère **dans le cadre qui est le sien** (cabinet, banque, CRF, judiciaire) et avec les sources autorisées par ce cadre. L’annexe M détaille ce point sous forme de tableau.

-----

### 0.8 — Mini-exemple de mise en pratique

Pour mettre en pratique ces notions de base, voici un mini-cas très simple :

> **Situation** : une société française, **TRADEX SAS**, créée il y a 8 mois, reçoit un virement de **400 000 €** depuis une société étrangère basée aux Émirats. TRADEX a un **capital social de 1 000 €**, **pas de site web**, un **dirigeant unique** (M. P, 31 ans, sans expérience visible dans le secteur déclaré), et une **adresse de domiciliation** dans un cabinet parisien hébergeant 50 autres sociétés.

#### Ce qu’on peut dire à ce stade

- **Faits observables** : la société est récente (8 mois), à très faible capital, sans présence opérationnelle visible (pas de site, domiciliation), avec un dirigeant au profil incohérent avec une activité commerciale internationale supposée. Le flux entrant (400 000 €) est significatif au regard de la taille apparente.
- **Hypothèses calibrées** :
  - Société écran *probable* (signaux convergents).
  - Activité économique réelle *douteuse* à ce stade.
  - Le flux entrant est *à investiguer* : est-il cohérent avec une activité légitime ?

#### Ce qu’on **ne peut pas** dire à ce stade

- On **ne peut pas** affirmer que TRADEX est une société de blanchiment : ce serait une qualification juridique non démontrée.
- On **ne peut pas** désigner M. P comme un fraudeur : il pourrait être un dirigeant inexpérimenté mais légitime, un prête-nom, ou un débutant motivé.
- On **ne peut pas** qualifier la société étrangère sans investigation.

#### Sources à consulter en premier

1. **Pappers** ou INPI : confirmer l’identification de TRADEX (SIREN, statuts, dirigeant déclaré).
1. **RBE** : bénéficiaire effectif déclaré de TRADEX.
1. **Profil du dirigeant** : LinkedIn, presse, autres mandats déclarés (recherche par nom).
1. **Adresse de domiciliation** : autres sociétés à la même adresse, profil du cabinet de domiciliation.
1. **Société émettrice émiratie** : registre Dubaï (free zone ou mainland selon la juridiction), dirigeants, activité déclarée.

#### Conclusion provisoire

À ce stade, l’analyste produit une **mini-fiche d’alerte** : signaux convergents justifiant approfondissement, hypothèses calibrées en *probable* ou *possible*, lacunes documentées, sources à mobiliser. **Aucune conclusion** sur la nature licite ou illicite de l’opération.

C’est exactement ce que le cours va apprendre à faire, avec rigueur, sur des cas plus complexes.

-----

### Points clés à retenir du Chapitre 0

- **Personne physique vs morale** : derrière chaque société, il y a des humains à identifier.
- **Flux financiers** : donneur d’ordre, bénéficiaire, libellé, banques, devise — à toujours décortiquer.
- **Documents** : Kbis, statuts, facture, bilan, relevé, leak — chacun a une fonction et des limites.
- **Logique comptable** : bilan = photo, compte de résultat = film, marge = rentabilité, trésorerie = liquidité.
- **Acteurs** : économiques, structurels, institutionnels — chacun a un rôle et des pouvoirs distincts.
- **Notions juridiques** : soupçon ≠ preuve ; renseignement ≠ accusation ; toujours présomption d’innocence.
- **Sources** : OSINT, professionnelle, bancaire, CRF, judiciaire, fiscale, leak, presse — chacune a son cadre d’accès.
- **Discipline FININT** : observer, qualifier, calibrer, documenter les lacunes — pas conclure prématurément.

Vous êtes prêt(e) pour le **parcours express** qui vient ensuite, ou pour la **Partie I** si vous suivez la progression linéaire.

-----

## Parcours express — Lire un dossier financier en 45 minutes

> **Objectif** : à partir d’un simple nom de société ou de personne, produire en 45 minutes une **première fiche FININT exploitable** — qui ne tranche rien, mais qui pose les bases d’une analyse plus poussée.

Cette procédure ne remplace pas une enquête approfondie. Elle constitue un **premier filtre** : qualifier rapidement un dossier (faut-il s’y attarder ?), repérer les points saillants (quelles sont les zones d’ombre ?), formuler quelques hypothèses calibrées (qu’est-ce que je peux dire ? qu’est-ce que je ne peux pas dire ?), et produire un livrable court (une mini-note d’une à deux pages).

Le parcours est volontairement borné dans le temps. La discipline est la suivante : on ne cherche pas l’exhaustivité, on cherche la **première lecture** d’un dossier. Si un point mérite approfondissement, on le note comme tel et on y reviendra dans une seconde phase.

### Étape 1 — Identifier l’entité exacte (3 min)

Avant toute recherche, **stabiliser le périmètre**. Une recherche lancée sans cette étape produit du bruit (homonymes, sociétés homonymes, variantes orthographiques) qui pollue toute la suite.

Pour une **société** : récupérer la dénomination sociale exacte, la forme juridique, le numéro d’identification (SIREN/SIRET en France, Companies House Number au UK, EIN aux US, RCS, NIF, etc.). Croiser avec un registre officiel pour confirmer.

Pour une **personne physique** : nom, prénoms (tous, dans l’ordre), date de naissance approximative ou exacte, lieu de naissance si possible, nationalité connue. Sans ces éléments, le risque d’homonymie est élevé.

Notation : `Entité = [dénomination] | [identifiant officiel] | [forme] | [pays]` ou `Personne = [nom] [prénom] | né(e) [JJ/MM/AAAA ou approx] à [lieu] | nationalité [pays]`.

### Étape 2 — Vérifier le statut légal (3 min)

Confirmer que l’entité **existe**, est **active** et n’est pas en procédure. Pour une société : statut au registre (active / radiée / en liquidation / en redressement), date de création, dernière modification (changements récents = signal). Pour une personne : présence sur listes de sanctions internationales (OFAC SDN, UE, ONU, HM Treasury, sanctions spécifiques), statut PEP éventuel, mentions visibles dans des procédures.

Outils gratuits : registres publics nationaux (chapitres 11-12), portails de sanctions consolidés (OpenSanctions, Sanctions.io en lecture libre partielle), bases adverse media (presse).

### Étape 3 — Identifier dirigeants et mandataires (5 min)

Lister les personnes physiques exerçant une fonction déclarée : président, gérant, directeur général, administrateurs, membres du conseil de surveillance, secrétaire (UK), commissaires aux comptes, fondés de pouvoir. Pour chaque mandataire, noter la **date de prise de fonction** et la **durée** : un mandataire installé depuis 15 ans ne dit pas la même chose qu’un mandataire arrivé il y a 4 mois.

Repérer les **profils suspects** sans les diaboliser : mandataires multi-sociétés (« corporate service providers » professionnels), mandataires retraités ou très jeunes, mandataires à l’adresse identique à la société, mandataires figurant comme dirigeants de dizaines d’entités sans cohérence sectorielle.

### Étape 4 — Chercher actionnaires et bénéficiaires effectifs (5 min)

Distinguer **actionnariat déclaré** et **bénéficiaire effectif** (UBO). L’actionnariat est ce qui apparaît dans les statuts ou la liste d’associés ; l’UBO est la personne physique qui détient ou contrôle ultimement l’entité (seuils de 25 % en UE, mais le contrôle peut être indirect).

Sources : registres des bénéficiaires effectifs (accès variable selon les juridictions depuis l’arrêt CJUE 2022 — voir chapitre 13), Companies House (UK) avec registre PSC, OpenCorporates en agrégation, et bases professionnelles (Orbis, Sayari) si disponibles.

Si l’UBO n’est pas accessible via les sources ouvertes : noter l’opacité comme **fait** (pas comme faute), et formuler la question pour la suite.

### Étape 5 — Cartographier les sociétés liées (5 min)

Identifier les **liens** : sociétés ayant le même dirigeant, sociétés à la même adresse, sociétés détenues par la même holding, sociétés figurant dans les mêmes leaks. Ne pas chercher l’exhaustivité ; cibler les liens visibles en quelques requêtes.

Première représentation graphique mentale : un noyau (l’entité initiale), une couronne directe (sociétés liées de premier degré), une couronne indirecte (sociétés liées via un mandataire ou une adresse partagée). Cette esquisse sera affinée plus tard avec un outil dédié (Maltego, Linkurious, Gephi — chapitre 52).

### Étape 6 — Sanctions, PEP, adverse media (5 min)

Trois sources à interroger systématiquement.

**Sanctions** : OFAC SDN, sanctions UE consolidées, ONU, HM Treasury, et listes nationales spécifiques selon le pays. Une mention sur l’une de ces listes change radicalement la qualification du dossier.

**PEP** (Politiquement Exposée) : ancien ou actuel dirigeant politique, haut fonctionnaire, membre de la famille proche ou collaborateur connu. Statut PEP ≠ culpabilité, mais déclenche une vigilance renforcée.

**Adverse media** : presse économique généraliste (Le Monde, Les Échos, Reuters, Bloomberg, FT, WSJ), presse d’investigation (Mediapart, OCCRP, ICIJ), bases d’agrégation (Factiva, LexisNexis, Dow Jones Risk & Compliance — Ch.51).

### Étape 7 — Repérer les actifs visibles (5 min)

Première cartographie patrimoniale : biens immobiliers visibles (Patrim France, registres fonciers étrangers, données cadastrales si publiques), véhicules ou bateaux dont l’enregistrement est public dans certains pays, parts dans d’autres sociétés, signaux de train de vie (réseaux sociaux, presse mondaine — voir chapitre 17).

Mise en regard : actifs visibles vs revenus déclarés (lorsque les comptes annuels sont accessibles) vs activité observable. Une discordance massive est un signal — pas une preuve.

### Étape 8 — Identifier les incohérences (5 min)

Cinq familles d’incohérences à repérer rapidement :

1. **Économique** — chiffre d’affaires sans rapport avec la taille apparente de la société (1 employé, 50 M€ de CA), marges incohérentes avec le secteur, charges incohérentes avec l’activité.
1. **Géographique** — sociétés dans des juridictions sans rapport avec leur activité visible (négociant en produits agricoles d’Afrique de l’Ouest avec siège à Tortola).
1. **Temporelle** — créations en cascade, changements de dirigeants ou de dénomination juste avant un appel d’offres ou un signalement.
1. **Documentaire** — comptes non publiés, comptes publiés en retard, mentions « non significatives » récurrentes, absence de commissaire aux comptes au-delà des seuils.
1. **Déclarative** — UBO « inconnu » alors qu’une personne contrôle visiblement l’entité par d’autres canaux.

### Étape 9 — Formuler des hypothèses calibrées (5 min)

À ce stade, le réflexe à éviter est la **conclusion prématurée**. On ne cherche pas à dire *« c’est une société écran »*, mais *« les éléments observés sont compatibles avec X, Y ou Z, avec tel niveau de confiance pour chaque hypothèse »*.

Exemple de formulation :

- *H1 — Activité commerciale légitime atypique mais réelle. Compatible avec : siège à l’adresse du comptable, faible nombre d’employés (sous-traitance possible), liens sectoriels cohérents. Niveau de confiance : possible.*
- *H2 — Société écran utilisée à des fins d’opacification. Compatible avec : UBO masqué, adresse partagée avec 14 autres sociétés du même corporate service provider, comptes non publiés depuis 3 ans, aucune trace d’activité visible. Niveau de confiance : probable.*
- *H3 — Implication dans un schéma de fraude active. Compatible avec : … (à étayer). Niveau de confiance : insuffisant à ce stade.*

Toujours mentionner les **éléments qui contredisent** les hypothèses retenues. C’est la marque d’un raisonnement honnête.

### Étape 10 — Produire la mini-note (4 min)

La mini-note tient en une à deux pages. Structure proposée :

```
RÉFÉRENCE : [identifiant du dossier] | DATE : [JJ/MM/AAAA]
CLASSIFICATION : [TLP : X]

OBJET (2 lignes)
  Mini-fiche FININT initiale sur [entité ou personne].

ÉLÉMENTS RECUEILLIS (puces)
  - Identification stabilisée
  - Statut légal et présence sur listes
  - Dirigeants / UBO
  - Sociétés liées
  - Patrimoine visible
  - Incohérences relevées

HYPOTHÈSES CALIBRÉES
  H1 ... [niveau de confiance]
  H2 ... [niveau de confiance]
  H3 ... [niveau de confiance]

LACUNES
  Sources non consultées
  Juridictions non couvertes
  Données manquantes

RECOMMANDATIONS
  Approfondir : [oui / non / sous condition]
  Sollicitations utiles : [registres complémentaires / réquisition / OSINT approfondi / coopération]
```

La mini-note est un **livrable de cadrage**. Elle ne tranche pas. Elle permet à l’analyste, au demandeur ou à l’équipe de décider si le dossier mérite d’être approfondi, et avec quelle priorité.

### Erreurs fréquentes du parcours express

- **Conclure trop tôt** sur la base de quelques signaux. La règle d’or : tant que vous n’avez pas suivi les 10 étapes, vous n’avez pas une première lecture — vous avez une intuition.
- **Accumuler du bruit** : recherches « tout azimut » qui produisent un dossier illisible. Le parcours est borné dans le temps précisément pour éviter cela.
- **Ignorer l’homonymie** : sauter l’étape 1 conduit à attribuer à une cible des éléments qui ne la concernent pas. C’est l’erreur la plus dommageable et la plus fréquente.
- **Confondre opacité et culpabilité** : l’absence d’information n’est pas une preuve d’irrégularité. Elle est une *contrainte d’enquête*.
- **Ne pas documenter les sources** : une mini-note sans sources est inexploitable. Chaque élément doit pouvoir être reproduit.

### Limites

Le parcours express ne répond pas à des questions du type *« est-ce que cette personne blanchit ? »* — il répond à *« cette entité mérite-t-elle un examen approfondi ? »*. Pour des dossiers à enjeux (signalement parquet, gel, dissémination internationale), un workflow complet (chapitre 49) est nécessaire, avec des sources fermées (réquisitions, données fiscales, droits de communication CRF) qui ne sont mobilisables qu’en cadre légal approprié.

-----

## Fil rouge — Opération CLEARFLOW

> **Statut narratif** : ce fil rouge est une fiction pédagogique. Il accompagne le cours du chapitre 1 jusqu’à la synthèse en chapitre 64. Il est conçu pour illustrer concrètement chaque section, sans empiéter sur la matière théorique.

### Le contexte

Une **cellule de renseignement financier (CRF) européenne fictive**, inspirée du fonctionnement d’une CRF de type TRACFIN, traite quotidiennement plusieurs centaines de déclarations de soupçon (DS) provenant des assujettis (banques, PSP, notaires, marchands d’art, professions juridiques, VASP). La CRF fictive du fil rouge est un **environnement institutionnel inspiré**, pas une représentation officielle d’une CRF réelle.

Au sein du département « Analyse et renseignement », **Nassim Belhaj** est analyste senior FININT. Son profil : sept ans d’expérience, solide en LCB-FT, lecture des registres d’entreprises, analyse des flux bancaires, identification des bénéficiaires effectifs et analyse patrimoniale. Formation initiale en finance et en droit des affaires, certification CAMS, formation continue sur les typologies GAFI et l’analyse de réseaux.

### Le signalement initial

Sur six mois consécutifs, la CRF reçoit **dix-sept déclarations de soupçon convergentes** émanant de :

- 5 banques françaises (1 grande banque mutualiste, 2 grandes banques de réseau, 2 banques privées) ;
- 2 établissements de paiement européens (un PSP français et un EME lituanien) ;
- 1 notaire (DS lors d’une acquisition immobilière inhabituellement rapide) ;
- 1 marchand d’art (DS sur une vente aux enchères payée en cash partiel).

Les DS pointent un homme d’affaires franco-libanais, **Karim Haddad**, et un réseau d’environ une douzaine de sociétés gravitant autour de lui dans plusieurs juridictions : France, Chypre, Émirats arabes unis, Bénin, Côte d’Ivoire, Suisse, Liban.

Les anomalies signalées : virements entrants depuis des sociétés de négoce basées à Dubaï et Istanbul vers des comptes français pour des montants compris entre 45 000 € et 95 000 € (sous le seuil de surveillance interne renforcée), libellés vagues (« commercial services », « trade payment »), paiements sortants vers des fournisseurs ouest-africains pour des marchandises agricoles dont la réalité physique paraît douteuse, transferts vers des comptes personnels en Suisse et au Luxembourg, dépôts en espèces structurés sous le seuil de 15 000 €, conversions partielles en USDT via un exchange européen, et au moins une opération de marché public en Côte d’Ivoire suspectée d’avoir été remportée dans des conditions opaques.

Montant cumulé sur la période : **environ 22 M€** de flux non encore qualifiés.

### Le mandat de Nassim

Le pôle réception/traitement transmet le dossier à Nassim avec un mandat structuré :

1. **Reconstituer le périmètre** — toutes les sociétés et personnes physiques liées au noyau Haddad.
1. **Cartographier les flux** — origine, transit, destination, mécanismes d’opacification.
1. **Qualifier le ou les schémas** — typologie probable (TBML ? cascade de sociétés ? corruption de marché public ? contournement de sanctions ?).
1. **Identifier les acteurs et leurs rôles** — organisateur, prête-noms, facilitateurs, bénéficiaires.
1. **Recommander les suites** — signalement parquet, gel TRACFIN, dissémination internationale via Egmont, sollicitations complémentaires.

### Les questions de renseignement (QR)

Nassim formule, dès le cadrage, **quatre questions de renseignement** qui structureront son travail :

- **QR1** — D’où vient l’argent ? Quelle est l’infraction prédécesseur probable ?
- **QR2** — Comment est-il opacifié ? Quel est le ou les schémas combinés ?
- **QR3** — Où va-t-il ? Quel est le patrimoine réel de Haddad ?
- **QR4** — Qui participe ? Quel est le réseau d’acteurs (prête-noms, complices, facilitateurs) ?

Une cinquième question de gestion du dossier émerge rapidement :

- **QR5** — Quelles coopérations sont nécessaires ? Athéna Group (volet crypto), CRF étrangères (Chypre, Émirats, Suisse), services nationaux (DGSI, DGDDI, DGFiP) ?

### Coopérations prévues

Le dossier comporte une **branche crypto limitée** : conversions USDT identifiées, mais le traçage on-chain dépasse le périmètre méthodologique de la CRF fictive. Nassim sollicitera **Sarah Marin** (Athéna Group, analyste crypto-forensique senior, ancienne TRACFIN) dans le cadre d’une convention pré-existante : la CRF fictive dispose d’un **cadre contractuel et juridique** (marché public, habilitation des intervenants, clauses de confidentialité, traitement des données minimisées et journalisées) permettant, sous contrôle interne strict et secret professionnel, de solliciter Athéna Group pour une **expertise technique on-chain limitée**. Le rapport produit par Athéna est intégré comme **intrant analytique au renseignement**, non comme preuve judiciaire autonome. Tout le volet on-chain (traçage, clustering, attribution d’adresses, identification des cashout) sera traité dans ce cadre et renvoyé au cours OSINT Crypto pour la méthode.

Un **volet documentaire** secondaire pourrait apparaître plus tard : suspicion de fausses factures et de faux certificats d’origine. Si ce volet se confirme, **Lucas Ferreira** (collègue de Sarah chez Athéna, spécialisé Dark Web et faux documents) pourra être consulté ponctuellement. Cette branche reste secondaire dans le fil rouge.

### Distinction renseignement / preuve — fondamentale

> **À garder à l’esprit pendant tout le cours** : la note d’analyse de Nassim est du **renseignement**. Elle oriente l’enquête, identifie les pistes, recommande des actions. Elle n’est pas une preuve au sens du Code de procédure pénale. La transformation du renseignement en preuve nécessite des **actes d’enquête judiciaire** (réquisitions, auditions, expertises) conduits sous l’autorité d’un magistrat. L’analyste FININT doit, en permanence, savoir ce qu’il peut écrire, ce qui peut être disséminé, ce qui est exploitable judiciairement, et ce qui n’est qu’un faisceau d’indices à corroborer.

### Bilan attendu — sans happy ending

Le fil rouge sera synthétisé au chapitre 64. Le bilan, conformément à la réalité opérationnelle des dossiers FININT complexes, sera **honnête** :

- Schéma probable cartographié, hypothèses calibrées, recommandations transmises ;
- Une partie des flux identifiée avec un haut niveau de confiance, une autre seulement présumée ;
- Coopérations engagées avec délais réalistes (mois à années pour la MLA, plus rapide pour Egmont) ;
- Recouvrement éventuellement partiel, sur plusieurs années, sans garantie ;
- Quelques branches du dossier qui resteront ouvertes ou non concluantes — c’est la norme.

Pas de dénouement spectaculaire : le FININT, dans la réalité, produit du renseignement actionnable. Le reste appartient au judiciaire et au politique.

-----

## PARTIE I — COMPRENDRE LE RENSEIGNEMENT FINANCIER

*Cinq chapitres pour cadrer ce que le FININT est, ce qu’il permet, ce qu’il ne permet pas, et comment il s’articule avec les disciplines voisines. Cette partie est la fondation : sans elle, les techniques des parties suivantes seraient utilisées hors-cadre.*

-----

### Chapitre 1 — Pourquoi le FININT est central aujourd’hui

#### Objectif du chapitre

Comprendre pourquoi le renseignement financier — discipline relativement récente dans sa formalisation — est devenu un **levier central** des politiques de sécurité, des stratégies de conformité et de la compréhension de la criminalité organisée moderne. Ce chapitre n’expose pas une nostalgie historique : il pose les enjeux concrets qui justifient le poids actuel du FININT, et qui structurent la demande professionnelle adressée aux analystes.

#### Le concept

Le **Financial Intelligence (FININT)** est la discipline qui collecte, analyse et exploite l’information financière — bancaire, comptable, patrimoniale, commerciale, registrale — pour détecter, comprendre, entraver et documenter la criminalité économique et le financement d’activités illicites. Le FININT ne se limite pas à la lecture des relevés bancaires : il englobe toute la chaîne d’information qui permet de **suivre l’argent** dans l’économie réelle, depuis l’origine présumée des fonds jusqu’à leur intégration finale.

Le FININT s’enracine historiquement dans la **lutte contre le blanchiment de capitaux** (LCB), formalisée dans les années 1980-1990 (création du GAFI en 1989, réseau Egmont en 1995), et étendue après le 11 septembre 2001 à la lutte contre le **financement du terrorisme** (CFT). Ce socle initial, devenu LCB-FT, s’est progressivement élargi à la corruption transnationale (suite aux scandales Enron, FCPA, à la Convention de Mérida 2003), à la fraude fiscale internationale (lendemain de la crise 2008, montée en puissance de l’EAR/CRS), aux sanctions économiques (en particulier post-2014 et plus encore post-2022), et à la criminalité organisée transnationale dans son ensemble.

#### L’utilité opérationnelle

Plusieurs facteurs expliquent la centralité actuelle du FININT.

**Le suivi de l’argent est l’un des seuls leviers communs à toutes les criminalités.** Que l’on parle de trafic de stupéfiants, de cybercriminalité, de corruption, de fraude fiscale ou de financement du terrorisme, à un moment ou à un autre, l’argent doit circuler, être stocké, ou être intégré dans l’économie légale. C’est ce passage qui laisse des traces — et que le FININT exploite.

**Les sanctions économiques sont devenues un instrument de politique extérieure majeur.** L’OFAC, l’UE et l’ONU produisent et font évoluer en continu des listes de personnes et entités sanctionnées. La détection de contournements (via pays tiers, sociétés écrans, cryptos, intermédiaires complaisants) est devenue une priorité opérationnelle pour les États comme pour les institutions financières.

**La transparence financière s’est imposée comme une norme internationale.** L’EAR/CRS (échange automatique de renseignements fiscaux entre plus de 100 juridictions), les directives DAC successives en UE (DAC6, DAC7, DAC8), les registres des bénéficiaires effectifs, l’évolution post-MiCA pour les VASP, dessinent un environnement où le secret bancaire historique a perdu une grande partie de son efficacité — au moins en théorie. Les analystes savent exploiter ce nouveau paysage.

**La criminalité organisée s’est financiarisée.** Les groupes criminels modernes utilisent des structures sophistiquées : holdings, trusts, fondations, montages multi-juridictionnels, corporate service providers professionnels, réseaux de prête-noms. Les comprendre exige une compétence FININT — pas seulement une compétence judiciaire.

**La cybercriminalité a un débouché financier obligatoire.** Les rançons, les fonds volés via BEC, les revenus de la fraude en ligne, les produits de la traite, doivent tous être convertis et intégrés. Le FININT et la cybercriminalité convergent. Dans un dossier moderne, les analystes financiers et cyber doivent souvent coopérer (chapitre 48).

#### Méthode — comment se positionner intellectuellement face à un dossier FININT

Le FININT n’est pas un domaine où l’on accumule des informations « parce que c’est intéressant ». Il est strictement **finalisé** : chaque collecte, chaque analyse, chaque livrable répond à une question — une question de renseignement (QR). Cette discipline finalisée est la première compétence à acquérir.

**Cinq postures professionnelles** structurent l’approche :

1. **Postulat du doute calibré** — toute information non vérifiée est une hypothèse. Toute corrélation n’est pas causalité.
1. **Discipline d’attribution** — chaque élément retenu doit être traçable à sa source. La fiabilité de la conclusion dépend de la fiabilité de la source.
1. **Calibration de la confiance** — chaque conclusion porte un niveau de confiance explicite (chapitre 33).
1. **Distinction faits / inférences / hypothèses** — vocabulaire calibré, formulations prudentes.
1. **Recul méthodologique** — pourquoi cherche-t-on cette information ? que va-t-elle changer dans la note ?

#### Mini-walkthrough

Imaginons un mandat simple : *« Une équipe compliance d’une banque mutualiste signale qu’un client professionnel — une SAS de négoce de matériel agricole — reçoit depuis six mois des virements importants de Turquie, sans cohérence apparente avec l’activité déclarée. Que peut faire un analyste FININT ? »*.

Réponse opérationnelle : il **ne s’agit pas** de conclure que la SAS blanchit. Il s’agit de :

- formuler trois ou quatre questions de renseignement précises (QR1 : la SAS a-t-elle une activité réelle de négoce ? QR2 : qui sont les contreparties turques ? QR3 : quel est le profil du dirigeant ? QR4 : y a-t-il déjà des DS antérieures ou des éléments dans des leaks ?) ;
- identifier les sources mobilisables (registre français, registre turc, presse, leaks, OSINT sur la société, données bancaires si en cadre légal CRF) ;
- produire une **mini-note** à 45 minutes (parcours express) qui qualifie le dossier en *probable* / *à investiguer* / *peu d’éléments à ce stade* ;
- recommander si besoin l’approfondissement, ou la transmission à un autre service.

Tout l’art réside dans le passage de l’intuition (« ça sent mauvais ») à un livrable structuré et défendable.

#### Erreurs fréquentes

- **Confondre intuition et analyse** : un signal n’est pas une conclusion. Il déclenche une enquête, il ne la termine pas.
- **Croire au mythe de la donnée parfaite** : un analyste FININT travaille toujours avec des données partielles, biaisées, parfois contradictoires. La méthode est ce qui transforme cette imperfection en livrable utile.
- **Sur-promettre** : *« on va trouver toute la vérité »*. Non. On va produire du renseignement actionnable, dans un cadre légal, dans un temps borné, avec des limites explicites.
- **Sous-estimer le judiciaire** : la note FININT n’est pas la fin de l’histoire. Elle est un point de bascule potentiel vers une procédure. La rigueur du livrable conditionne l’exploitabilité ultérieure.

#### Limites

Le FININT ne **prouve pas** au sens judiciaire (chapitre 4). Il **oriente**. Il n’a pas accès direct aux moyens d’enquête réservés au judiciaire (perquisition, garde à vue, audition). Il dépend de la qualité des sources mobilisables — qui peuvent être fragmentaires, surtout dans les juridictions opaques (chapitre 10). Et il ne remplace pas l’expertise comptable, juridique, fiscale, sectorielle ; un analyste FININT travaille avec ces expertises, pas à leur place.

#### Lien avec le fil rouge

> **CLEARFLOW — Cadrage**
> 
> Lorsque le dossier Haddad arrive sur le bureau de Nassim, il représente déjà 17 DS, une douzaine de sociétés présumées, sept juridictions et environ 22 M€ de flux. Si Nassim cherchait *« la vérité complète »*, il s’enliserait. Il commence donc par poser ses cinq questions de renseignement (QR1 à QR5) et estime un budget temps : 6 à 8 semaines pour produire une première note d’analyse robuste, avec coopérations engagées en parallèle. La discipline de cadrage est ce qui distingue une enquête FININT d’une accumulation de documents.

#### Points clés à retenir

- Le FININT est une discipline **finalisée**, structurée par des questions de renseignement.
- Sa centralité actuelle découle de la convergence sanctions / transparence / financiarisation du crime / cyber.
- Le FININT produit du **renseignement orienté action**, pas de la connaissance pour la connaissance.
- Cinq postures professionnelles : doute calibré, attribution, calibration, distinction, recul.
- Les limites du FININT — non-preuve judiciaire, sources partielles, dépendance aux cadres légaux — sont à intégrer dès le cadrage.

-----

### Chapitre 2 — Ce que le FININT permet vraiment

#### Objectif du chapitre

Cartographier précisément les **résultats utiles** que le FININT peut produire, pour ajuster les attentes et structurer les livrables. Un analyste qui sait ce que sa discipline permet réellement écrit mieux et déçoit moins.

#### Le concept

Le FININT permet de produire **six grandes familles de résultats** opérationnels.

1. **Cartographies de réseaux** — qui détient quoi, qui dirige quoi, qui est lié à qui, par quel mécanisme (capital, mandat, parenté, adresse partagée, lien documentaire).
1. **Reconstitutions de flux** — d’où vient l’argent, par où transite-t-il, où va-t-il, sous quelle forme, à quels intervalles, avec quels libellés et quelles contreparties.
1. **Identifications de bénéficiaires effectifs** — la personne physique qui contrôle ultimement une structure, avec un niveau de confiance qualifié.
1. **Profils patrimoniaux** — comparaison entre actifs visibles, revenus déclarés, signaux de train de vie, et activité connue.
1. **Qualifications typologiques** — schéma X est compatible avec une typologie de blanchiment classique, de TBML, de carrousel TVA, de corruption, etc., avec un niveau de confiance.
1. **Recommandations actionnables** — signalement, gel, dissémination, sollicitations complémentaires, escalade vers le judiciaire.

Chaque résultat est livré avec une **traçabilité des sources** et un **niveau de confiance** : c’est ce qui le rend exploitable par d’autres acteurs (parquet, magistrat, équipe d’audit, comité de risque interne).

#### L’utilité opérationnelle

Selon le contexte, ces résultats servent des fonctions différentes :

- **En CRF** : alimenter une transmission au parquet, une dissémination Egmont, un gel TRACFIN, ou enrichir une analyse stratégique sectorielle.
- **En conformité bancaire** : qualifier ou écarter un soupçon avant DS, motiver une rupture de relation d’affaires, alimenter un dossier d’audit interne.
- **En due diligence** : établir un rapport KYC/KYB approfondi avant entrée en relation, lors d’une fusion-acquisition, ou avant un partenariat stratégique.
- **En investigation journalistique** : étayer un article ou une enquête longue.
- **En cabinet d’avocat ou expert** : préparer une procédure civile, fiscale, ou pénale ; soutenir un client victime ; assurer une défense documentée.
- **En recouvrement d’actifs** : localiser des biens dissimulés, soutenir une saisie conservatoire ou une exécution forcée à l’international.

#### Méthode — qu’est-ce qu’un livrable « utile »

Un livrable FININT utile vérifie cinq propriétés :

1. **Pertinent par rapport au mandat** — il répond aux questions de renseignement formulées au cadrage.
1. **Calibré en confiance** — chaque conclusion est accompagnée de son niveau de confiance.
1. **Sourcé** — chaque élément factuel est traçable.
1. **Actionnable** — il propose des suites, pas seulement des constats.
1. **Lisible par un non-expert** — un magistrat, un comité de risque ou un journaliste doit pouvoir l’exploiter sans avoir besoin de l’expliquer.

À l’inverse, un livrable FININT **non utile** : long, exhaustif, descriptif, sans conclusion claire, sans niveau de confiance, sans recommandation, illisible hors du cercle des analystes.

#### Mini-walkthrough

Une demande typique : *« Voici un dirigeant suspect, dis-moi ce que tu peux dire de son patrimoine ».* Que peut produire le FININT ?

- **Patrimoine immobilier identifié** (au degré accessible aux sources ouvertes ou aux droits de communication) : trois biens en France, un en Espagne, peut-être un à Dubaï via une société écran. Niveau de confiance : *probable* à *quasi-certain* selon les sources.
- **Patrimoine financier visible** : participations dans 5 sociétés (registres), 1 fonds d’investissement (presse), comptes étrangers présumés via EAR/CRS (sources fermées, accessibles en CRF uniquement).
- **Train de vie observable** : véhicule de luxe identifié, voyages réguliers visibles sur réseaux sociaux, école privée pour les enfants.
- **Discordance avec revenus déclarés** : oui, significative — *facteur de soupçon élevé*, mais explicable par des sources non identifiées (héritage non documenté ? activités antérieures ?).

Conclusion calibrée : *« Le patrimoine identifié dépasse de plusieurs ordres de grandeur les revenus déclarés sur la période. Les origines des fonds ne sont pas établies par les sources mobilisées. Hypothèses non exclusives : revenus non déclarés, héritage non documenté, prête-nom, financement par tiers. Recommandation : approfondir via […] »*.

#### Erreurs fréquentes

- **Promettre l’identification certaine d’un UBO masqué** dans une juridiction opaque sans sources fermées — souvent impossible.
- **Annoncer une « preuve de blanchiment »** : ce vocabulaire appartient au judiciaire, pas au renseignement.
- **Ignorer la dimension temporelle** : une cartographie est valable à une date. Six mois plus tard, l’organisation a peut-être muté.

#### Limites

Le FININT **ne dit pas** :

- *« cette personne est coupable »* — c’est le tribunal qui dit cela ;
- *« ce flux prouve le blanchiment »* — il *est compatible avec* un schéma de blanchiment ;
- *« cette société est une société écran »* — sauf à pouvoir le démontrer rigoureusement (chapitre 26) ;
- *« telle juridiction est complaisante »* — c’est un débat politique et diplomatique.

#### Lien avec le fil rouge

> **CLEARFLOW — Calibrage des attentes**
> 
> Au cadrage, Nassim explique au coordinateur du dossier ce qu’il pourra et ne pourra pas livrer. Il pourra reconstituer les flux observables, cartographier les sociétés et mandataires, identifier le patrimoine français visible, qualifier les schémas avec un niveau de confiance, et recommander les actions. Il ne pourra pas, sans coopération chypriote et émiratie, identifier de manière certaine les UBO finaux des structures offshore. Ce calibrage initial évite de promettre l’impossible.

#### Points clés à retenir

- Six familles de résultats : réseaux, flux, UBO, patrimoine, typologies, recommandations.
- Un livrable utile est pertinent, calibré, sourcé, actionnable, lisible.
- Le FININT répond à un mandat ; il ne produit pas de la connaissance hors mandat.
- Le vocabulaire des conclusions doit être prudent et calibré.

-----

### Chapitre 3 — Ce que le FININT ne permet pas

#### Objectif du chapitre

Tracer la **frontière des limites** du FININT. Cette frontière n’est pas un défaut de la discipline — elle est sa marque de sérieux. Connaître ses limites est ce qui permet de produire un livrable défendable et de ne pas conduire un demandeur à des décisions disproportionnées.

#### Le concept

Trois grandes catégories de limites se recoupent en pratique.

**Limites épistémiques** — des choses que le FININT ne peut pas savoir, faute de sources accessibles. Exemple : l’UBO d’un trust irrévocable régi par un droit étranger sans registre public.

**Limites légales** — des sources auxquelles l’analyste n’a pas accès en cadre ouvert (relevés bancaires détaillés, données fiscales individuelles, informations couvertes par le secret professionnel). Ces sources sont mobilisables uniquement par des autorités compétentes (CRF avec droits de communication, magistrats, services d’enquête).

**Limites méthodologiques** — un raisonnement par corrélation ne prouve pas la causalité. Un faisceau d’indices, même solide, n’est pas une preuve judiciaire.

#### L’utilité opérationnelle

Connaître ces limites évite trois erreurs lourdes :

1. **Promettre ce qu’on ne livrera pas** — sape la crédibilité du service auprès du demandeur.
1. **Conduire à une décision disproportionnée** — un gel, une rupture de relation, une dénonciation publique fondés sur du renseignement présenté comme une preuve peuvent entraîner des contentieux.
1. **Affaiblir l’exploitabilité judiciaire** — un livrable mal calibré, qui mélange faits, inférences et opinions, est difficilement exploitable par un magistrat.

#### Méthode — comment formaliser les limites dans un livrable

Toute note FININT comporte une section **« Lacunes »** explicite. Elle liste :

- Les **sources non consultées** (et pourquoi : indisponibilité, hors cadre légal, contrainte de temps).
- Les **juridictions non couvertes** (parce que l’enquête s’est bornée à un périmètre, ou parce qu’aucune coopération n’a été obtenue).
- Les **données manquantes** structurelles (registres opaques, secret bancaire local).
- Les **délais et conditions** sous lesquels certaines lacunes pourraient être levées (réquisition, MLA, dissémination Egmont).

Cette section n’est pas un aveu de faiblesse : c’est un **élément de qualité** qui permet au demandeur de calibrer ses propres décisions et qui rend l’analyste honnête.

#### Mini-walkthrough — trois exemples concrets

**Exemple 1 — Identification UBO en juridiction opaque.** Sans coopération internationale ou sans accès à des leaks pertinents, l’identification du bénéficiaire effectif d’une société aux Îles Vierges Britanniques (BVI) est généralement *indéterminable* à partir des seules sources ouvertes. Mention explicite à porter dans le livrable : *« UBO non identifié à partir des sources mobilisées ; identification effective conditionnée à une coopération via Egmont avec la CRF locale »*.

**Exemple 2 — Origine des fonds.** Sans accès aux relevés bancaires en amont (réquisition), il n’est pas possible d’établir avec certitude l’origine d’un dépôt de 500 000 € sur un compte. On peut au mieux émettre des hypothèses calibrées. Mention : *« Les éléments observés sont compatibles avec H1 [revenus professionnels non déclarés], H2 [héritage non documenté], H3 [prête-nom]. La résolution requiert une réquisition judiciaire des relevés du compte source »*.

**Exemple 3 — Intentionnalité.** Le FININT décrit des comportements et leur compatibilité avec des schémas. Il ne décrit pas les intentions internes des personnes. Affirmer *« X savait qu’il blanchissait »* relève du tribunal, sur la base de preuves d’intention (correspondances, témoignages, expertises).

#### Erreurs fréquentes

- **Présenter une corrélation comme une preuve** — *« Mr X et Mr Y figurent dans les Panama Papers, donc ils sont complices »*. Non — ils figurent dans une fuite documentaire ; cela alimente une hypothèse, pas une conclusion.
- **Attribuer une intention** sans preuve directe.
- **Considérer le silence comme une preuve** — l’absence de réponse à une sollicitation n’est pas un aveu.
- **Conclure à partir d’une seule source** — toute conclusion forte doit reposer sur **au moins deux sources indépendantes** (chapitre 33).

#### Limites — méta

Même les limites évoluent : un registre fermé peut s’ouvrir (pression réglementaire, leak), une source nouvelle peut apparaître (DAC8 pour les transactions crypto, base UBO post-AMLA), une décision de justice peut élargir l’accès. L’analyste maintient une veille permanente sur l’évolution des sources (chapitre 30 — non, en l’occurrence chapitre 50).

#### Lien avec le fil rouge

> **CLEARFLOW — Cartographier les zones d’ombre**
> 
> Avant même de commencer son analyse, Nassim dresse une carte des **zones d’ombre prévisibles** dans le dossier Haddad : (a) les UBO finaux des structures chypriote, émiratie et libanaise — accessibles seulement via Egmont ; (b) les flux non bancaires (espèces, hawala suspecté) — non observables directement ; (c) la qualification d’éventuels marchés publics ouest-africains opaques — accessible seulement via coopération locale. Il documente ces zones d’ombre dans son cadrage initial, ce qui permet au coordinateur de prioriser les coopérations à engager.

#### Points clés à retenir

- Trois familles de limites : épistémiques, légales, méthodologiques.
- Toute note FININT comporte une section **Lacunes** explicite.
- Une corrélation n’est pas une preuve ; un silence n’est pas un aveu ; une présence dans un leak n’est pas une condamnation.
- Calibrer les limites au cadrage initial protège l’analyste, le service et le demandeur.

-----

### Chapitre 4 — Renseignement, soupçon, preuve et judiciarisation

#### Objectif du chapitre

Maîtriser **les quatre étapes** d’une chaîne d’information financière, de la donnée brute à la preuve judiciaire — et savoir où se situe le FININT dans cette chaîne. C’est le socle de la rigueur analytique qui distingue un professionnel d’un commentateur.

#### Le concept

Quatre étapes hiérarchisées, chacune avec son **régime juridique** et son **régime de vérité**.

**1. La donnée.** Elle est ce qui est observable, factuel : un virement, une mention sur un registre, une déclaration de soupçon, une publication de presse. La donnée est le matériau brut. Elle peut être fiable ou non, complète ou non, datée ou non.

**2. Le soupçon.** Il naît quand la donnée présente des **éléments qualifiés** qui sortent de la normalité attendue. Le soupçon a un seuil légal en LCB-FT : il est l’élément déclencheur de la déclaration de soupçon (DS). Le seuil n’est ni la certitude ni la preuve — c’est un faisceau d’éléments objectifs qui justifie la déclaration. Le soupçon est une **lecture qualifiée** de la donnée.

**3. Le renseignement.** Il est produit par l’analyste à partir de plusieurs données et de plusieurs soupçons (DS convergentes, sources OSINT, sources fermées). Il **structure** une hypothèse, en évalue la confiance, identifie le réseau et les flux, et formule des recommandations. C’est le livrable FININT au sens strict.

**4. La preuve.** Elle est ce qui est **opposable devant un tribunal**. Elle doit avoir été obtenue dans un cadre légal admissible (réquisition judiciaire, audition, expertise judiciaire, perquisition autorisée). Le renseignement FININT n’est généralement pas une preuve directe : il est une **piste** qui oriente l’enquête judiciaire, laquelle, par ses propres actes, transforme certains éléments en preuves admissibles.

#### L’utilité opérationnelle

Cette distinction structure tout le travail :

- **Au cadrage** : quelles sources puis-je mobiliser ? Quel est leur régime juridique ?
- **Pendant l’analyse** : ce que je vois, qu’est-ce que c’est — donnée, soupçon, renseignement ?
- **Dans le livrable** : quel vocabulaire, quel niveau d’affirmation ?
- **À la sortie** : à qui je transmets, sous quelles conditions, et que peut-on en faire ?

Mal positionner une information dans la chaîne, c’est **faire un faux pas opérationnel** : présenter une preuve quand on n’a qu’un soupçon (sur-promettre, faire du mal), ou inversement présenter un soupçon quand on a déjà du renseignement structuré (sous-vendre, faire perdre du temps).

#### Méthode — la grille de qualification

Face à toute information, l’analyste applique une grille en quatre questions :

1. **Source** — qui est l’émetteur, dans quel cadre ai-je obtenu l’information ?
1. **Régime juridique** — l’information peut-elle être utilisée ouvertement, en interne, judiciairement ?
1. **Niveau de qualification** — donnée brute, soupçon, renseignement, preuve ?
1. **Niveau de confiance** — quasi-certain, probable, possible, indéterminable (chapitre 33) ?

Cette grille peut être tabulée pour chaque pièce du dossier. Elle accompagne ensuite la note d’analyse, comme matrice de sources.

#### Mini-walkthrough — la chaîne CLEARFLOW

Reprenons un fragment du dossier Haddad pour illustrer la chaîne complète :

|Étape        |Élément                                                                                                                                                                                                                  |Régime                                                           |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
|Donnée       |Un virement de 92 000 € de SOCIETE_DUBAI vers NEXUS_FRANCE le 14 mars                                                                                                                                                    |Observation                                                      |
|Soupçon      |Le virement s’inscrit dans une série de 18 virements similaires sur 6 mois, libellés vagues, contrepartie nouvelle, sans cohérence apparente avec l’activité déclarée → DS de la banque                                  |Déclaration LCB-FT                                               |
|Renseignement|Recoupé avec 16 autres DS et OSINT, le schéma est compatible avec une activité de TBML (probable, niveau de confiance modéré)                                                                                            |Note FININT, exploitable par autorités, non opposable au tribunal|
|Preuve       |Le procureur, sur la base du renseignement, ouvre une enquête. La réquisition judiciaire des relevés permet d’obtenir les pièces exploitables au tribunal. L’expertise comptable d’un expert judiciaire qualifie les flux|Pièces du dossier judiciaire                                     |

À chaque étape, ce qui change : la **qualification** (de l’observation à la qualification typologique à la qualification pénale), le **régime** (fait observable, déclaration légale, livrable analytique, pièce judiciaire), et l’**autorité** qui en est responsable (banque → analyste → magistrat).

#### Erreurs fréquentes

- **Confondre DS et preuve** : une DS est un signalement légal, pas une affirmation de culpabilité. Le déclarant n’a pas besoin d’être certain — il a besoin d’avoir un soupçon qualifié.
- **Présenter le renseignement comme « la vérité »** : le renseignement est une lecture qualifiée à un instant donné. Il peut être révisé.
- **Ne pas baliser ce qu’on transmet** : transmettre un livrable sans préciser sa nature (« renseignement », « pré-rapport », « note de cadrage ») expose à des malentendus.

#### Limites

Cette taxonomie est claire en théorie ; en pratique, certains éléments sont **ambigus** : une expertise privée commandée par une partie a-t-elle valeur de preuve ? Un rapport d’audit forensique peut-il être versé au dossier ? Un relevé obtenu en EAR/CRS est-il directement opposable ? Les réponses dépendent du droit national applicable et de l’usage qui en est fait. L’analyste consulte le juriste de son service en cas de doute.

#### Lien avec le fil rouge

> **CLEARFLOW — Posture de Nassim**
> 
> Sa note finale (chapitre 64) commencera par cette phrase : *« La présente note constitue un livrable de renseignement financier au sens de l’article L.561-29 CMF [équivalent fictif]. Elle vise à orienter l’enquête. Elle n’est pas opposable en l’état comme pièce judiciaire. Les éléments qu’elle expose sont calibrés en confiance ; les pièces sous-jacentes sont conservées dans le dossier de référence et peuvent être communiquées au magistrat sur demande, dans le cadre approprié. »* Cette phrase n’est pas une formalité : elle protège l’analyste, le service, et l’exploitabilité ultérieure.

#### Points clés à retenir

- Quatre étapes : donnée → soupçon → renseignement → preuve.
- Chaque étape a son régime juridique et son régime de vérité.
- Le FININT produit du renseignement ; il ne produit pas de preuve directe.
- La grille de qualification (source / régime / qualification / confiance) accompagne tout livrable sérieux.

-----

### Chapitre 5 — FININT, OSINT financier, AML, CTI et OSINT Crypto

#### Objectif du chapitre

Positionner le FININT par rapport aux disciplines voisines, pour éviter les confusions et exploiter au mieux les complémentarités. Beaucoup de dossiers modernes mobilisent plusieurs disciplines simultanément ; un analyste qui ne sait pas où il se situe ne sait pas non plus à qui s’adresser pour ce qu’il ne fait pas lui-même.

#### Le concept

Plusieurs disciplines coexistent et se recoupent :

- **AML / LCB-FT** (Anti-Money Laundering / Lutte contre le blanchiment et le financement du terrorisme) — discipline réglementaire centrée sur la **conformité** : KYC, KYB, monitoring, déclaration de soupçon, screening sanctions, gel. Elle est portée par les **assujettis** (banques, PSP, etc.) avec des obligations légales précises.
- **FININT** — discipline analytique et de **renseignement** centrée sur l’exploitation de l’information financière pour comprendre, détecter, qualifier et orienter l’action contre la criminalité économique. Pratiquée en CRF, en services d’enquête, en cabinets d’investigation, en compliance avancée.
- **OSINT financier** — sous-ensemble de l’OSINT spécialisé sur les **sources ouvertes financières et économiques** : registres, comptes annuels, presse, leaks, marchés publics, SOCMINT financier. C’est une **boîte à outils** mobilisée par le FININT.
- **CTI** (Cyber Threat Intelligence) — discipline de renseignement sur la **menace cyber** : acteurs, TTP, infrastructures, indicateurs. Lorsqu’une criminalité est cyber-financière (ransomware, BEC, hacks DeFi), CTI et FININT convergent.
- **OSINT Crypto** — discipline d’enquête **on-chain** : blockchains, transactions, wallets, mixers, bridges, DEX, privacy coins, cashout. C’est le complément naturel du FININT pour le volet crypto-actifs.

#### L’utilité opérationnelle

Concrètement, dans un dossier moderne :

- **AML** détecte et signale (banque émet une DS).
- **FININT** reçoit, recoupe, analyse, qualifie et oriente (CRF produit une note).
- **OSINT financier** alimente le FININT en sources ouvertes (registres, presse, leaks).
- **CTI** alimente quand le dossier comporte un volet cyber (acteur ransomware identifié, TTP connue).
- **OSINT Crypto** alimente quand le dossier comporte une branche on-chain.

Aucune de ces disciplines n’est « supérieure » aux autres. Elles **se complètent**. Un bon analyste FININT sait *quand* solliciter une autre discipline, et *comment* exploiter ce qu’elle lui rend.

#### Méthode — comment articuler les disciplines

Trois principes :

1. **Spécifier les questions adressées à chaque discipline.** Demander à un analyste OSINT Crypto *« est-ce qu’il blanchit ? »* est inopérant. Demander *« peux-tu tracer les fonds depuis cette adresse de dépôt sur l’exchange jusqu’aux destinations finales et identifier les off-ramps ? »* l’est. Le FININT pose des questions techniquement précises.
1. **Recevoir et intégrer les livrables.** Un rapport CTI, un rapport OSINT Crypto, un rapport AML interne d’une banque ne sont pas du renseignement FININT directement utilisable — ils sont des **intrants**. Le FININT les recoupe, en évalue la fiabilité, et les intègre dans une note unifiée.
1. **Documenter la chaîne d’attribution.** Quand le livrable FININT mobilise du renseignement crypto produit par un cabinet externe, le cours OSINT Crypto recommande explicitement (Chapitre 47) une calibration des sources — l’analyste FININT applique le même standard pour citer ces apports : *« L’analyse on-chain conduite par Athéna Group (rapport référencé X) conclut, avec un niveau de confiance “probable”, que les fonds atteignent un exchange non-KYC … »*.

#### Mini-walkthrough — qui fait quoi dans CLEARFLOW

|Question                                                   |Discipline              |Acteur                      |
|-----------------------------------------------------------|------------------------|----------------------------|
|Les DS de banques détectent-elles la structuration ?       |AML                     |Compliance des banques      |
|Quelle est la cartographie des sociétés liées à Haddad ?   |FININT + OSINT financier|Nassim                      |
|Y a-t-il des éléments dans les Panama/Pandora Papers ?     |OSINT financier (leaks) |Nassim, ICIJ Aleph          |
|Quelle est la trajectoire des USDT envoyés sur l’exchange ?|OSINT Crypto            |Sarah Marin (Athéna)        |
|Y a-t-il un exploit cyber dans le BEC suspecté ?           |CTI                     |Service partenaire ou Athéna|
|Quel rapport final pour le PNF ?                           |FININT (intégrateur)    |Nassim                      |

C’est le FININT qui **intègre** toutes les contributions et produit le livrable final unifié. Sans intégration, on a une collection de rapports déconnectés.

#### Erreurs fréquentes

- **Demander à une discipline ce qu’elle ne fait pas** — par exemple demander à un analyste OSINT Crypto une analyse des comptes annuels d’une SAS française.
- **Faire double emploi** — refaire dans le rapport FININT le détail blockchain qu’a déjà produit l’analyste crypto. Le rapport FININT renvoie, il ne refait pas.
- **Sous-utiliser l’OSINT financier** — beaucoup d’analystes FININT en CRF passent peu de temps sur les registres internationaux ou les leaks alors que les retours opérationnels y sont élevés.

#### Limites

La frontière entre disciplines n’est pas toujours nette. Un analyste FININT senior maîtrise une partie de l’OSINT financier classique. Un analyste OSINT Crypto avec passé TRACFIN maîtrise une partie du FININT classique (cas Sarah Marin). C’est plus souvent une **question de profil** que de discipline pure. L’organisation prime : qui livre quoi, à qui, sous quelle responsabilité.

#### Lien avec le fil rouge

> **CLEARFLOW — Architecture des coopérations**
> 
> Nassim dessine, dès le cadrage, l’architecture des coopérations : OSINT financier en interne (registres, leaks, presse), branche crypto sous-traitée à Athéna Group / Sarah Marin avec un mandat précis (« tracer USDT depuis l’exchange jusqu’aux off-ramps », pas « est-ce que c’est du blanchiment ? »), branche cyber éventuelle sous-traitée à un service partenaire si BEC se confirme, AML restant chez les banques déclarantes (Nassim ne refait pas leur monitoring). Cette architecture évite les redondances et les angles morts.

#### Points clés à retenir

- AML, FININT, OSINT financier, CTI, OSINT Crypto sont **complémentaires**, pas concurrents.
- Le FININT est la discipline **intégratrice** quand un dossier mobilise plusieurs angles.
- Les questions adressées aux disciplines voisines doivent être **techniquement précises**.
- Le livrable FININT renvoie, il ne refait pas — particulièrement pour la branche crypto (renvoi systématique au cours OSINT Crypto).

-----

## PARTIE II — LE SYSTÈME FINANCIER POUR L’ENQUÊTEUR

*Cinq chapitres pour comprendre l’infrastructure dans laquelle circule l’argent. Sans cette compréhension, l’analyste lit les flux comme on lit une langue étrangère.*

-----

### Chapitre 6 — Le système bancaire et la circulation de l’argent

#### Objectif du chapitre

Comprendre l’**architecture institutionnelle** du système bancaire — banques de détail, banques d’investissement, banques privées, correspondent banks, banques centrales — et la manière dont l’argent circule entre ces acteurs. C’est le socle sans lequel les flux observables n’ont pas de sens.

#### Le concept

Le système bancaire est organisé en **plusieurs strates**.

Les **banques commerciales de détail** sont l’interface du grand public et des entreprises : comptes courants, dépôts, crédits, moyens de paiement. En France : banques mutualistes (Crédit Agricole, Crédit Mutuel, BPCE), grands réseaux (BNP Paribas, Société Générale, Crédit du Nord), banques en ligne (Boursorama, Fortuneo). Au UK : Barclays, HSBC, NatWest, Lloyds. Aux US : JPMorgan Chase, Bank of America, Wells Fargo, Citibank.

Les **banques privées** (private banking) servent une clientèle aisée à très aisée (seuils variables, souvent 1 M€+ d’actifs). Elles cumulent gestion de patrimoine, conseil patrimonial, fiscalité internationale. En Suisse : UBS, Credit Suisse historiquement (absorbé par UBS en 2023), Pictet, Julius Baer, Lombard Odier. Au Luxembourg : Banque de Luxembourg, BIL. Une partie significative des dossiers FININT touchant à la fraude fiscale ou à la corruption transnationale impliquent des banques privées.

Les **banques d’investissement** opèrent sur les marchés financiers, financent les grandes entreprises, structurent les fusions-acquisitions, émettent les obligations souveraines. Goldman Sachs, Morgan Stanley, J.P. Morgan, Deutsche Bank, BNP Paribas CIB, Rothschild & Co.

Les **banques correspondantes** (correspondent banks) jouent un rôle clé : elles permettent à des banques sans présence directe dans une juridiction d’y opérer en passant par elles. Quasiment toutes les grandes banques occidentales offrent ce service. C’est par ces points de passage que transite la majorité du commerce international et des paiements transfrontaliers.

Les **banques centrales** (BCE, Fed, BoE, BNS) régulent la masse monétaire, fixent les taux directeurs et opèrent les systèmes de règlement de gros (TARGET2 en zone euro, Fedwire aux US). Pour l’analyste FININT, leur intérêt opérationnel est limité, sauf en supervision et statistiques.

Les **banques offshore** sont des établissements implantés dans des juridictions à fiscalité réduite et à secret bancaire historique (chapitre 10). Beaucoup ont des relations correspondantes avec les banques internationales.

#### L’utilité opérationnelle

Lire un flux suspect, c’est lire un parcours dans cette architecture.

Exemple : *« virement de 850 000 € depuis HSBC Hong Kong vers Crédit Agricole Île-de-France, transitant par Deutsche Bank Frankfurt »*. L’analyste voit immédiatement :

- une banque correspondante européenne (Deutsche Bank) — point de contrôle AML majeur ;
- un trajet HK → DE → FR — atypique pour un flux purement européen, ce qui interroge sur l’origine ;
- le passage par une banque privée à Hong Kong — clientèle particulière, vérifications KYC supposément renforcées.

Cette lecture en quelques secondes oriente les questions à poser au coordinateur du dossier.

#### Méthode — décoder un flux à partir des codes BIC/IBAN

Tout virement bancaire transite par des banques identifiables via leurs **codes BIC (Bank Identifier Code)** SWIFT et les comptes via leurs **IBAN (International Bank Account Number)**.

**BIC** : 8 ou 11 caractères, structuré ainsi `AAAA BB CC XXX` :

- 4 lettres : code banque (ex : `BNPA` pour BNP Paribas, `CHAS` pour JPMorgan Chase, `DEUT` pour Deutsche Bank).
- 2 lettres : code pays ISO (ex : `FR`, `DE`, `US`, `GB`, `CH`).
- 2 caractères : code lieu/ville (ex : `PP` pour Paris, `LL` pour Londres).
- 3 caractères optionnels : code agence ou département.

**IBAN** : longueur variable selon le pays, structuré `[Pays 2 lettres][Clé contrôle 2 chiffres][Identifiant national bancaire]`. En France, l’IBAN fait 27 caractères ; en Lituanie 20 ; au Luxembourg 20 ; en Suisse 21.

Pour l’analyste, l’IBAN livre :

- le **pays** (premier indice : un IBAN LT ou EE pour un résident français en BTP, sans lien évident, est un signal contextuel) ;
- le **code banque** (les 5 caractères suivant la clé en France pointent l’établissement) ;
- le **type d’établissement** par recoupement (banque traditionnelle vs PSP/EME — chapitre 8).

Outils gratuits utiles : annuaires SWIFT BIC publics (sites de banques centrales, services en ligne), validateurs IBAN, tables ISO 9362 et ISO 13616.

#### Mini-walkthrough

Un flux typique dans un dossier de TBML : *« 4 virements, libellés “trade payment”, 75 000 € à 95 000 € chacun, depuis IBAN AE [Émirats] via BIC HSBC Dubaï, passant par BIC HSBC Londres comme correspondant, vers IBAN FR d’une SAS de négoce agricole »*.

Lecture : (1) Émirats → UK → France, trajet avec étapes correspondantes en ligne avec les usages du commerce ; (2) HSBC est à la fois banque émettrice et correspondant — concentration sur un acteur donnant une bonne traçabilité par recoupement ; (3) montants tous sous le seuil de 100 000 € — pourrait être de la structuration intentionnelle ou un ordre de grandeur typique du secteur ; (4) libellés vagues, à creuser. Cette lecture rapide oriente la suite de l’analyse.

#### Erreurs fréquentes

- **Confondre un IBAN national « exotique » avec une fraude.** Beaucoup de fintechs européennes (Revolut, Wise) opèrent depuis la Lituanie ou l’Estonie pour des raisons réglementaires parfaitement légales. Un IBAN LT n’est pas suspect en soi.
- **Ignorer la distinction banque émettrice / banque réceptrice / banques correspondantes.** Une « banque » sur un virement n’est jamais évidente : il peut y avoir 2 à 4 banques impliquées dans la chaîne.
- **Lire le BIC sans vérifier le réseau de l’établissement.** Une grande marque sur une plaque ne garantit pas que la filiale locale ait le même standard de conformité que la maison mère.

#### Limites

L’analyse des codes ne dit rien sur l’**activité** bancaire (motifs réels du flux). Elle dit qui a transité, pas pourquoi. Le « pourquoi » exige les libellés, les contreparties, les volumes et le contexte économique du compte.

#### Lien avec le fil rouge

> **CLEARFLOW — Lecture rapide des chaînes**
> 
> Sur un échantillon de 60 virements entrants, Nassim repère que 80 % transitent par seulement 3 banques correspondantes : Deutsche Bank (Francfort), JPMorgan Chase (Londres), HSBC (Hong Kong). C’est un indice de structuration de la chaîne de paiement choisie par le réseau. Cela oriente les coopérations : un signalement à BaFin (DE) et à FCA (UK) pourrait éclairer les pratiques de KYC sur les flux concernés.

#### Points clés à retenir

- Le système bancaire est multi-strates : détail, privée, investissement, correspondant, centrale, offshore.
- Les banques correspondantes sont un point de passage — et de contrôle AML — majeur.
- Les codes BIC et IBAN permettent une lecture rapide des chaînes de paiement.
- Cette lecture oriente, mais ne conclut pas.

-----

### Chapitre 7 — Rails de paiement : SWIFT, SEPA, TARGET2, Fedwire, ACH

#### Objectif du chapitre

Connaître les **principaux rails de paiement** mondiaux, leurs caractéristiques techniques, leurs vitesses, leurs niveaux de surveillance, et la signification de leur usage dans un schéma observé.

#### Le concept

Un « rail de paiement » est l’**infrastructure technique** qui permet à un ordre de paiement émis par une banque d’arriver à une autre banque. Plusieurs rails coexistent, chacun avec son périmètre, sa vitesse, sa fiabilité et son niveau de transparence.

**SWIFT** (Society for Worldwide Interbank Financial Telecommunication). Réseau de **messagerie** sécurisée entre banques, utilisé pour les paiements internationaux et de gros. SWIFT n’est pas un rail de règlement : il transmet des *messages* qui déclenchent des règlements via les comptes correspondants ou des systèmes de règlement nationaux. Les messages SWIFT pertinents pour l’analyste FININT (annexe B pour la lecture détaillée) :

- **MT103** — virement client (single customer credit transfer). Le format de référence pour un virement international depuis un client donneur d’ordre vers un bénéficiaire dans une autre banque.
- **MT202** — transfert interbancaire (financial institution transfer). Mouvement de fonds entre banques correspondantes pour le compte de leurs clients ou pour leurs propres besoins de trésorerie.
- **MT940** — relevé de compte SWIFT (customer statement message). Utilisé pour la reconstitution de flux quand le compte est tenu par une banque tierce.

Depuis 2022-2024, SWIFT migre progressivement vers le format **ISO 20022** (richesse des données plus grande, structuration améliorée). C’est une bonne nouvelle pour l’analyse FININT (champs plus complets, structurés), à condition que les contreparties soient également migrées.

**SEPA** (Single Euro Payments Area). Espace de paiement européen unifié pour les virements en euros. Couvre 36 pays (UE + EEE + UK + Suisse + Andorre + Monaco + Saint-Marin + Vatican). Les rails :

- **SEPA Credit Transfer (SCT)** : virement standard, J+1.
- **SEPA Instant Credit Transfer (SCT Inst)** : virement instantané (10 secondes), 24/7, plafond historique 100 000 €, étendu en pratique. Depuis le règlement « Instant Payments » de 2024, les banques européennes doivent proposer ce service par défaut, avec une montée en charge progressive.
- **SEPA Direct Debit (SDD)** : prélèvement.

L’analyste FININT note : un virement instantané est **non-réversible** (sauf consentement du bénéficiaire) ; il est devenu un canal privilégié des fraudes au virement avec urgence (BEC, voir chapitre 44).

**TARGET2 / TARGET / T2** (Trans-European Automated Real-time Gross settlement Express Transfer system). Système de règlement de gros de la BCE. Règlements interbancaires de la zone euro pour gros montants. Utilisé pour les transferts entre banques centrales, les marchés monétaires, les opérations de politique monétaire. En 2023 a été remplacé techniquement par **TARGET / T2** (avec T2S pour les titres) — l’analyste retient surtout que TARGET2 est l’infrastructure de gros de la zone euro.

**Fedwire** (US). Système de règlement de gros de la Réserve fédérale. Équivalent fonctionnel de TARGET2.

**ACH** (Automated Clearing House) (US). Rail de paiement de détail (équivalent fonctionnel de SEPA). Utilisé pour les salaires, les paiements récurrents, les transferts inter-banques aux US. Lent (1 à 3 jours), bon marché, peu utilisé en transfrontalier.

**CHIPS** (Clearing House Interbank Payments System) (US). Système privé de règlement de gros aux US, complémentaire de Fedwire.

**FedNow** (US). Système de paiement instantané des banques américaines, lancé en 2023, équivalent fonctionnel de SCT Inst. Adoption progressive.

**FPS** (Faster Payments Service) (UK). Paiement instantané au UK depuis 2008, antérieur à SCT Inst.

**RTGS** (Real-Time Gross Settlement) — terme générique désignant les systèmes de règlement brut en temps réel des banques centrales (TARGET, Fedwire, RTGS de la BoE, etc.).

#### L’utilité opérationnelle

Le rail utilisé dit beaucoup de choses sur le flux :

- **SWIFT** = transfrontalier, gros montant typique, transit par correspondants (donc traces détaillées dans les MT).
- **SEPA SCT Inst** = euro, instantané, irréversible. Si vu en cascade, signal de layering rapide.
- **ACH** = US-domestique, lent, faible coût. Pas adapté à un layering rapide.
- **TARGET2 / Fedwire** = gros, institutionnel, peu visible aux particuliers.
- **FPS / FedNow** = équivalents nationaux instantanés.

Une fraude BEC moderne typique combine SCT Inst (pour la rapidité) puis transfert vers une PSP/EME, puis sortie cash ou crypto en moins de 6 heures. Le suivi exige une rapidité d’action (gel d’urgence) — voir chapitre 44.

#### Méthode — lire un flux et identifier le rail

À partir d’un relevé bancaire, le rail utilisé apparaît :

- via la mention explicite (« SCT Inst », « SEPA », « SWIFT », etc.) ;
- via la **vitesse** (heure de débit chez l’émetteur ↔ heure de crédit chez le bénéficiaire) ;
- via le **format de la référence** (références SWIFT MT distinctives, MMSCT pour SEPA) ;
- via les **frais** appliqués (un SCT est gratuit ou à coût marginal ; un SWIFT international peut coûter 15 à 50 € côté donneur d’ordre, plus côté correspondant).

#### Mini-walkthrough

Un dossier BEC : *« mardi 14h32, virement de 215 000 € depuis le compte d’une PME française vers un IBAN ES (Espagne) via SCT Inst. À 14h41, fractionné en 5 virements de 40 000 € à 45 000 € via SCT Inst vers 5 IBANs (3 au Portugal, 2 en Lituanie). À 16h12, l’ensemble converti en USDT sur un exchange via 5 dépôts. À 18h45, sortie depuis l’exchange vers un wallet auto-géré »*.

Lecture FININT : SCT Inst utilisé exclusivement (irréversibilité — fenêtre de gel quasi-nulle si la banque PME n’a pas réagi dans la minute), pattern de layering rapide multi-PSP, sortie crypto en moins de 4 heures. Le suivi du dossier exige : (a) immédiat contact avec la banque PME française et la banque espagnole pour gel, (b) saisine CRF française pour droit d’opposition, (c) ouverture d’un volet OSINT Crypto avec Sarah Marin pour le suivi blockchain.

#### Erreurs fréquentes

- **Croire que SWIFT « contrôle » les paiements.** SWIFT est un réseau de messages ; il ne valide pas les paiements (les banques le font). Les sanctions SWIFT (déconnexion d’une banque) sont une exception à valeur politique forte (cas Iran, Russie partielle 2022).
- **Sous-estimer la vitesse du SCT Inst.** Les fraudes modernes l’exploitent. Le réflexe « j’ai 24h pour réagir » est dépassé.
- **Confondre les rails.** Un transfert intra-zone euro entre deux particuliers en SCT Inst n’a rien à voir avec un transfert SWIFT inter-correspondants : la lecture, les leviers de gel, et les coopérations diffèrent.

#### Limites

L’analyse du rail ne dit rien sur la **légalité** du flux. Un SCT Inst de 200 000 € peut être un flux parfaitement légitime (achat immobilier, transaction commerciale) — c’est le contexte qui qualifie.

#### Lien avec le fil rouge

> **CLEARFLOW — Cartographie des rails**
> 
> Nassim recense les rails utilisés dans les 17 DS : majorité de SWIFT MT103 (virements depuis Émirats vers France, comme attendu pour du commerce international), un nombre significatif de SCT Inst depuis des comptes en France vers des IBANs LT et EE (signal d’un layering rapide via fintechs européennes), et une trace de SCT classique vers un compte Suisse (banque privée). Cette cartographie oriente les coopérations à demander en priorité.

#### Points clés à retenir

- SWIFT (international, MT103/MT202/MT940), SEPA (SCT, SCT Inst, SDD), TARGET2/Fedwire (gros), ACH (US-domestique), FPS/FedNow (instant nationaux).
- Le rail utilisé révèle la vitesse, la traçabilité et les leviers de gel disponibles.
- SCT Inst est aujourd’hui un canal privilégié des fraudes — avec une fenêtre de gel très étroite.
- ISO 20022 améliorera la richesse des données disponibles à l’analyse.

-----

### Chapitre 8 — PSP, EME, néobanques et fintechs

#### Objectif du chapitre

Comprendre l’écosystème des **prestataires de services de paiement** (PSP), des **établissements de monnaie électronique** (EME), des **néobanques** et des **fintechs** : ce qu’ils sont, comment ils sont régulés, où ils se situent dans la chaîne de paiement, et pourquoi ils figurent souvent dans les schémas modernes de blanchiment et de fraude.

#### Le concept

Le paysage est complexe et évolutif. Quelques distinctions clés.

Un **PSP** (Payment Service Provider) est un acteur agréé pour fournir des services de paiement (initiation, exécution, encaissement). Sa surface réglementaire est définie par la directive PSD2 (et bientôt PSR/PSD3). Tous les acteurs émettant des instruments de paiement ou opérant des comptes de paiement sont, à un titre ou un autre, PSP. Exemples : Stripe, Adyen, Worldline, PayPal, Mangopay, Lemon Way.

Un **EME** (Établissement de Monnaie Électronique) est agréé spécifiquement pour émettre de la monnaie électronique (e-money). Sa réglementation découle de la directive 2009/110/CE. Beaucoup de néobanques et fintechs sont juridiquement des EME plutôt que des banques. Exemples historiques : Revolut (initialement EME au UK puis banque), Wise (anciennement TransferWise — EME), Anytime, Qonto.

Une **néobanque** est une banque (ou EME ou hybride) opérant principalement en ligne, sans réseau d’agences physiques. Par abus de langage, le mot recouvre des statuts variés. N26 (banque allemande), Revolut (banque lituanienne pour ses comptes EU), Bunq (banque néerlandaise), Monzo et Starling (banques UK).

Une **fintech** est un terme générique qui désigne toute entreprise technologique opérant dans la finance — peut être un PSP, un EME, une néobanque, un agrégateur, un courtier, un assureur. Le terme n’a pas de portée réglementaire propre.

#### L’utilité opérationnelle

Pourquoi ces acteurs concentrent l’attention FININT ?

**Onboarding rapide et 100 % digital.** Création de compte en quelques minutes via un smartphone, vérification d’identité automatisée. Cela permet à un fraudeur de créer rapidement plusieurs comptes (ou à un prête-nom de faciliter cela), beaucoup plus difficilement qu’avec une banque traditionnelle.

**Vitesse des opérations.** Virements instantanés intra-réseau (Revolut → Revolut), conversions multi-devises en un clic, virements internationaux à coût faible. Le **layering** se fait en heures, là où le circuit traditionnel prenait des jours.

**Effectifs compliance plus tendus.** Beaucoup de PSP/EME ont scalé leur base clients très rapidement et leurs équipes compliance moins. Conséquences observables : taux d’alerte traités en backlog, faux négatifs, parfois des sanctions ACPR/FCA/BaFin.

**IBANs « exotiques ».** Revolut (LT), Wise (BE/UK selon les comptes), N26 (DE), Bunq (NL), etc. La réglementation européenne facilite le passporting : une fintech agréée en Lituanie peut opérer dans toute l’UE. Un IBAN LT pour un résident français n’est pas suspect en soi (surtout depuis Revolut, Wise, etc.) — c’est l’absence de cohérence avec l’activité du compte qui peut l’être.

**Cartes prépayées.** Certaines fintechs émettent des cartes prépayées (rechargeables en ligne, parfois anonymes sous certains seuils dans certaines juridictions). Vecteur de placement et de cashout.

**Intégration native crypto.** Plusieurs fintechs proposent l’achat-vente de cryptos directement dans leur application (Revolut, Bitpanda en partenariat). Le passage fiat-crypto se fait sans changer d’environnement, ce qui complique la chaîne de surveillance (chapitre 48 et OSINT Crypto).

#### Méthode — lire un flux fintech

Un flux passant par une fintech présente des spécificités :

1. **L’IBAN du compte fintech** est dans le pays de licence (LT pour Revolut, BE pour Wise, DE pour N26, NL pour Bunq). Le titulaire peut être résident dans n’importe quel pays UE (passporting).
1. **Les libellés sont parfois plus pauvres** que dans la banque traditionnelle, mais s’améliorent (depuis ISO 20022).
1. **Les transferts intra-réseau** (Revolut → Revolut, par username ou tag) ne laissent pas de trace SEPA visible aux contreparties extérieures — il faut une réquisition pour les obtenir.
1. **Les conversions multi-devises** apparaissent sur le relevé (par exemple : EUR → USD interne, puis virement USD).

L’analyste qui rencontre un flux passant par une fintech doit :

- Identifier précisément le statut juridique et l’agrément (banque, EME, PSP, et pays).
- Identifier l’autorité de supervision (ACPR pour France, BaFin pour Allemagne, Bank of Lithuania, FCA pour UK, Bank of Lithuania pour la majorité des comptes Revolut européens, etc.).
- Pour les sollicitations bancaires (réquisitions, droits de communication), passer par le canal compétent (banque licence-holder).

#### Mini-walkthrough

Un cas BEC : *« 215 000 € transitent depuis une PME française par 4 comptes Revolut (LT) → Wise (BE) → N26 (DE) → Bunq (NL) en 2 heures, avant conversion crypto »*.

Lecture FININT :

- Layering rapide multi-fintech, profil typique des fraudes BEC modernes.
- Quatre juridictions de licence, donc quatre coopérations potentielles avec les autorités locales (Banque de Lituanie, Banque nationale de Belgique, BaFin, DNB).
- Dans la pratique opérationnelle : la coopération via les autorités prend du temps. La réactivité passe par la **CRF** qui peut activer des canaux plus directs avec les compliance des fintechs concernées (FIU.NET en EU).
- Renvoi crypto pour la suite : vers Sarah Marin / OSINT Crypto.

#### Erreurs fréquentes

- **Considérer toutes les fintechs comme « suspectes ».** Elles sont des outils financiers majeurs et largement légitimes. Le profil de risque dépend de l’usage par l’utilisateur, pas de la marque.
- **Ne pas distinguer banque / EME / PSP.** Cela change le cadre réglementaire et la liste des autorités à solliciter.
- **Croire qu’un IBAN LT/EE/BE est nécessairement « offshore ».** Ces IBANs sont européens et soumis à la réglementation UE complète.
- **Sous-estimer la richesse des données fintech.** Les fintechs ont souvent des **logs très détaillés** (géolocalisation des sessions, device fingerprinting, IP) — exploités sur réquisition, ils sont parfois plus utiles que les relevés bancaires classiques.

#### Limites

La supervision peut varier en maturité d’une autorité nationale à l’autre. La **réactivité** dans la coopération aussi. L’analyste qui dépend de la coopération transfrontalière entre fintechs note les délais réels (parfois des semaines pour des demandes pourtant urgentes).

#### Lien avec le fil rouge

> **CLEARFLOW — Branche fintech**
> 
> Plusieurs flux du dossier Haddad transitent par des comptes Wise (au nom d’une société chypriote, IBAN BE). Nassim demande à la CRF de solliciter — via FIU.NET — les KYB associés (qui contrôle le compte ?), les logs de session (depuis où sont effectuées les opérations ?), et les patterns de transferts intra-Wise qui ne seraient pas visibles sur les relevés bancaires classiques. La réponse arrive en 11 jours — ce qui, pour une coopération européenne, est un délai correct.

#### Points clés à retenir

- PSP / EME / néobanque / fintech : termes recouvrant des statuts juridiques variés.
- L’écosystème est largement légitime ; l’attention FININT cible des **usages** spécifiques.
- Layering rapide, IBAN passportés, intégration crypto, cartes prépayées : facteurs typiques.
- La coopération exige d’identifier l’autorité de supervision compétente et le bon canal d’instruction.

-----

### Chapitre 9 — Comptes bancaires, relevés et opérations

#### Objectif du chapitre

Comprendre les **différents types de comptes**, la structure d’un **relevé bancaire**, et la grammaire des opérations courantes — pour savoir lire un relevé et y reconnaître l’anormal.

#### Le concept

**Types de comptes (vue analyste).**

- **Compte courant / compte de paiement** — usage quotidien, encaissements, virements, dépenses. Le compte « visible » d’un particulier ou d’une entreprise.
- **Compte d’épargne** (Livret A, LDDS, livrets bancaires, etc.) — dépôts rémunérés, plafonds, fiscalité spécifique en France.
- **Compte à terme / compte de dépôt à terme** — sommes immobilisées sur une durée, rémunération supérieure.
- **Compte titres / portefeuille** — détention d’instruments financiers (actions, obligations, OPCVM, ETF).
- **Compte sur livret de société** — pour entreprises, plus rare.
- **Compte de séquestre / escrow** — fonds bloqués au profit d’un tiers (notaire, avocat).
- **Compte de paiement chez une fintech / EME** — fonctionnellement proche d’un compte courant, mais juridiquement distinct.
- **Compte de cantonnement** — pour certains professionnels (avocats, agents immobiliers, agents de change), fonds reçus pour le compte de tiers.
- **Compte client / compte tiers** — fonds détenus par un professionnel pour ses clients.

**Structure d’un relevé bancaire (lecture FININT).**

Un relevé moderne contient typiquement, par ligne d’opération :

- **Date de l’opération** (date où l’opération est passée).
- **Date de valeur** (date à laquelle l’opération est prise en compte pour le calcul d’intérêts).
- **Libellé** — texte plus ou moins riche : référence SEPA, nom du donneur ou bénéficiaire, motif éventuel, référence interne.
- **Montant** (débit ou crédit, devise).
- **Solde après opération** (parfois).
- **Référence interne** — souvent utile pour relier les opérations.

Pour un compte d’entreprise, le relevé peut être enrichi : code analytique, journal comptable, rapprochement automatique.

**Grammaire des opérations courantes.**

- **Virement émis / reçu** (SEPA, SWIFT, instantané) — la trace la plus courante.
- **Prélèvement** (SDD) — paiement récurrent avec mandat (loyers, factures).
- **Carte bancaire — débit / paiement / retrait** — paiements en ligne ou physiques, retraits espèces.
- **Dépôt / versement d’espèces** — en agence, en automate.
- **Retrait d’espèces** — au DAB ou en agence.
- **Chèque — émis / reçu / encaissé / rejeté** — en déclin en Europe, encore courant en certains secteurs.
- **Effets de commerce / LCR / BOR** — papiers commerciaux entre entreprises.
- **Frais bancaires** — nombreux, souvent peu lus mais analytiquement utiles (un fort volume de frais sur découvert peut être signal de difficulté ; un volume anormalement élevé de frais SWIFT peut signaler une activité de transit).
- **Intérêts / agios** — produits ou charges financières.
- **Achats-ventes de titres** sur compte titre.

#### L’utilité opérationnelle

Le relevé est la **matière première** de l’analyse de flux. L’analyste le lit en plusieurs passes :

1. **Vue panoramique** — structure globale : combien d’opérations / mois ? combien d’entrées ? sorties ? quel est le solde moyen ? quel est le pic ?
1. **Vue temporelle** — distribution des opérations dans le temps : pics d’activité ? saisonnalité ? périodes de creux ?
1. **Vue par contreparties** — top 20 des contreparties émettrices, top 20 des bénéficiaires : qui paie qui, combien, sur quelle période ?
1. **Vue par type d’opération** — répartition virements / cartes / espèces / chèques.
1. **Vue par libellés** — détection de patterns dans les libellés (mots clés récurrents, formats répétitifs).
1. **Vue par cohérence économique** — les flux sont-ils compatibles avec l’activité déclarée (secteur, taille, géographie) ?

À chaque passe, l’analyste note les **anomalies** : montants ronds inhabituels, structuration sous des seuils, libellés vagues, contreparties géographiquement incohérentes, soldes nuls répétés (compte de transit), pics non expliqués.

#### Méthode — la lecture en 6 passes

Pour un relevé d’1 an d’opérations sur un compte courant typique (1 000 à 5 000 lignes) :

**Passe 1 — Profilage** (15 min). Statistiques globales. Outils : tableur ou pandas.

```
Période : 12 mois
Lignes : 3 247
Crédits : 1 421 — 4,2 M€
Débits : 1 826 — 4,1 M€
Solde moyen : 87 K€
Solde max : 542 K€ (pic le 18/03)
Nombre de contreparties uniques : 187
Top 5 émetteurs : 73 % du volume entrant
Top 5 bénéficiaires : 51 % du volume sortant
```

**Passe 2 — Concentrations**. Les top contreparties représentent quoi ? Sont-elles cohérentes avec l’activité ?

**Passe 3 — Anomalies temporelles**. Pics, creux, ruptures (changement de comportement).

**Passe 4 — Anomalies de contreparties**. Pays inhabituels, contreparties inconnues, contreparties créées récemment.

**Passe 5 — Libellés**. Mots clés vagues (« services », « paiement », « avance », « régularisation »), libellés répétés à l’identique, libellés contradictoires.

**Passe 6 — Cohérence économique**. Recoupement avec l’activité déclarée : pour une SAS de négoce, attendre des achats matières + ventes clients ; les virements perso massifs depuis le compte société sont anormaux (ABS — chapitre 43).

#### Mini-walkthrough

Un compte personnel d’un dirigeant français, secteur « consultant indépendant », revenus déclarés 80 K€/an :

- 87 % des entrées sur 6 mois proviennent de 2 sociétés étrangères (CY et AE) que l’OSINT identifie comme contrôlées par le même groupe ;
- Les libellés sont uniformément « consulting fees » ;
- Les sorties incluent : 240 K€ vers une SCI Paris (achat immobilier), 95 K€ vers un compte personnel suisse, dépôt récurrent de 8 500 € à 14 000 € en espèces (10 dépôts en 6 mois) ;
- Aucun frais professionnel apparent (pas de loyer bureau, pas de cotisations sociales pro, pas d’achat matériel).

Lecture FININT initiale : profil compatible avec **(H1)** prestation de conseil légitime mais à clientèle restreinte hors France ; **(H2)** rétrocommissions ou facturation de complaisance ; **(H3)** prête-nom pour le compte d’un tiers. Niveau de confiance : impossible à trancher sur les seules données du relevé. Sollicitations recommandées : coopération avec les CRF chypriote et émiratie pour qualifier les contreparties, OSINT sur l’activité réelle du « consultant », réquisition des libellés détaillés des dépôts cash si possible.

#### Erreurs fréquentes

- **Lire un relevé ligne à ligne sans vue panoramique préalable.** L’analyste se noie dans les détails et passe à côté du schéma.
- **Ignorer les frais bancaires.** Ils racontent une histoire (volume d’opérations, opérations rejetées, découverts).
- **Ne pas faire le rapprochement avec l’activité économique réelle** — un relevé bancaire ne se lit qu’avec le contexte du compte.

#### Limites

Le relevé bancaire est un point de vue **partiel** sur les flux d’une personne ou d’une entreprise. Une personne peut avoir 3 comptes dans 2 banques différentes ; une entreprise peut opérer via 5 comptes dans 4 juridictions. Une analyse complète exige la consolidation, qui est rarement possible sans réquisitions (FICOBA en France pour identifier les comptes ouverts par une personne).

#### Lien avec le fil rouge

> **CLEARFLOW — Premier relevé Haddad**
> 
> Nassim obtient, via les DS, un échantillon des relevés des comptes français de Haddad. Sur 18 mois : 1 421 lignes, 4,2 M€ de crédits totaux, 87 % concentrés sur 4 contreparties étrangères (Chypre, Émirats, Turquie, Suisse). Libellés à 75 % vagues (« services », « commercial », « avance »). Ratio comptes pro / perso anormal : 60 % des dépenses du compte société sont des transferts vers des comptes perso ou des entités liées. Le relevé seul ne prouve rien. Il pose le décor.

#### Points clés à retenir

- Relevé = matière première, lecture en 6 passes (profilage, concentrations, temps, contreparties, libellés, cohérence).
- Le relevé est partiel ; le FICOBA (et équivalents) permet de consolider.
- Les frais bancaires et les libellés sont des indices souvent négligés.
- Le relevé seul ne tranche pas — il oriente, en attendant le recoupement.

-----

### Chapitre 10 — Offshore, secret bancaire et juridictions opaques

#### Objectif du chapitre

Comprendre ce qu’est l’**offshore**, comment fonctionne le **secret bancaire**, quelles sont les **juridictions opaques** clés, et comment l’analyste FININT compose avec ces obstacles structurels.

#### Le concept

**Offshore.** Un terme imprécis qui désigne, dans le langage courant, les juridictions à fiscalité réduite et à régulation faible utilisées pour héberger des structures (sociétés, trusts, fondations) ou des comptes bancaires. Les analystes professionnels préfèrent le terme **« juridictions à risque »** ou **« juridictions à transparence limitée »** car il est plus précis et moins polémique.

**Secret bancaire.** Obligation légale faite aux banques de ne pas révéler à des tiers les informations sur leurs clients. Tous les pays ont une forme de secret bancaire, mais certaines juridictions l’ont historiquement renforcé au point d’en faire un argument commercial (Suisse, Liechtenstein, Luxembourg, Singapour, Hong Kong). Sous la pression internationale (GAFI, EAR/CRS, FATCA), le secret bancaire a perdu une grande partie de sa portée vis-à-vis des autorités fiscales étrangères, mais il reste opposable aux particuliers et à de nombreux acteurs privés.

**EAR/CRS** (Échange Automatique de Renseignements / Common Reporting Standard, OCDE). Mécanisme par lequel les juridictions adhérentes échangent automatiquement les informations sur les comptes bancaires détenus par des non-résidents. Plus de 100 juridictions adhérentes en 2025. La Suisse, le Liechtenstein, Singapour, Hong Kong, le Luxembourg, les BVI, les Cayman, sont parties au CRS. Les **non-adhérents** notables incluent les États-Unis (qui ont leur propre système, FATCA, asymétrique). En CRF, les données EAR/CRS reçues et envoyées sont une source primordiale.

**FATCA** (Foreign Account Tax Compliance Act, US). Obligation faite aux institutions financières étrangères de déclarer aux US les comptes détenus par des contribuables américains. Asymétrique (les US ne livrent pas l’équivalent en sortie).

**Listes GAFI.**

- **Liste noire** (« High-Risk Jurisdictions subject to a Call for Action »). Juridictions présentant des défaillances stratégiques en matière de LCB-FT. La liste évolue ; un analyste consulte le site officiel du GAFI au moment de l’analyse.
- **Liste grise** (« Jurisdictions under Increased Monitoring »). Juridictions sous surveillance renforcée mais coopérantes. La liste évolue plusieurs fois par an. Pour une donnée actuelle, consulter le site officiel du GAFI (fatf-gafi.org).

**Listes UE.** L’UE publie sa propre liste de juridictions tierces non coopératives à des fins fiscales. Liste mise à jour régulièrement, à consulter sur EUR-Lex et le site du Conseil.

#### L’utilité opérationnelle

Pour l’analyste, ces concepts servent à :

- **Qualifier le risque** d’un flux sortant ou entrant (juridiction du compte / pays de résidence du titulaire / activité du compte).
- **Calibrer la coopération** attendue (un EAR/CRS facilite ; un pays sur liste grise complique ; un pays sur liste noire ferme presque toutes les portes).
- **Anticiper les délais** de toute coopération internationale.
- **Identifier les secteurs vulnérables** (les juridictions à secret bancaire fort sont souvent des destinations finales de blanchiment).

#### Méthode — qualifier rapidement une juridiction

Pour toute juridiction inhabituelle apparaissant dans un dossier, l’analyste répond rapidement à :

1. **Statut GAFI** — pays sur liste noire, grise, ou hors liste ?
1. **Statut UE** — pays sur la liste UE des juridictions non coopératives ?
1. **Adhésion EAR/CRS** — oui / non ?
1. **Coopération via Egmont** — la CRF locale est-elle membre d’Egmont ? Active ?
1. **Type de structures fréquentes** — sociétés ? trusts ? fondations ? IBC (International Business Company) ? exemptes de fiscalité ? exemptes de comptes annuels publiés ?
1. **Registre des bénéficiaires effectifs** — existe-t-il ? est-il accessible ?

Outils gratuits : site GAFI, base UE, CRS country status (OCDE), Tax Justice Network (Financial Secrecy Index — académique, point de référence).

#### Mini-walkthrough — quelques juridictions emblématiques

**Suisse.** Place financière historique. Membre Egmont actif. Adhérente CRS (depuis 2017). Le secret bancaire absolu vis-à-vis des autorités fiscales étrangères a été levé pour les pays partenaires CRS. Reste opposable au public et à de nombreuses procédures civiles. Coopération via FINMA et MROS (la CRF suisse).

**Luxembourg.** Place financière européenne majeure. Membre UE et Egmont. Adhérente CRS. Coopération possible et structurée via la CRF luxembourgeoise. Mais la **densité de holdings, SOPARFI, fonds, et structures de gestion d’actifs** rend l’identification opérationnelle parfois lourde.

**Chypre.** Membre UE et Egmont. Adhérente CRS. Coopération via Mokas (CRF chypriote). Densité de sociétés détenues par des non-résidents (notamment liées à des intérêts russes pré-2022, libanais, turcs). Réformes post-2018 sous pression EU. Point d’attention pour les schémas d’opacification européens.

**Émirats arabes unis (EAU).** Place financière en croissance, hub commercial régional. Membre Egmont. Adhérente CRS. Sur liste grise GAFI 2022 (sortie en 2024 — vérifier la liste actuelle au moment de l’analyse). Coopération possible mais variable selon les émirats (Dubai vs Abu Dhabi vs autres). Free zones (Jebel Ali, DMCC, ADGM, DIFC) avec régimes spécifiques.

**British Virgin Islands (BVI).** Juridiction britannique d’outre-mer. Adhérente CRS. Densité historique d’IBC. Registre des bénéficiaires effectifs introduit progressivement (BOSS — Beneficial Ownership Secure Search), accessible aux autorités sous conditions.

**Cayman Islands.** Similaire BVI sur de nombreux aspects. Hub majeur des fonds d’investissement.

**Panama.** Juridiction historique des sociétés anonymes. Réputation lourdement atteinte par les Panama Papers (2016) et Pandora Papers (2021). Coopération améliorée mais inégale.

**Liechtenstein.** Petite juridiction, historiquement associée aux fondations privées (Stiftung) — véhicules de protection patrimoniale très opaques. Membre Egmont, adhérent CRS.

**Singapour, Hong Kong.** Centres financiers asiatiques. Adhérents CRS. Coopération possible mais avec des inflexions politiques notables (notamment HK depuis 2020).

**Delaware (US).** Sans être offshore au sens géographique, Delaware (et certains autres États US comme le Wyoming, le Nevada) propose des structures (LLC) à transparence très limitée — registre PSC limité, pas d’EAR/CRS sortant équivalent (FATCA asymétrique). C’est un point d’attention sous-estimé.

#### Erreurs fréquentes

- **Considérer toute juridiction non européenne comme « offshore ».** La nuance est essentielle.
- **Croire que CRS résout tout.** CRS échange des données fiscales entre administrations. Il ne les rend pas accessibles aux particuliers ni à toute autorité.
- **Sous-estimer Delaware / Nevada / Wyoming.** Une part significative des structures à risque dans les dossiers transatlantiques transitent par ces États US.
- **Ignorer le free zone factor.** Les free zones (Jebel Ali, DIFC, ADGM, etc.) ont des régimes fiscaux et réglementaires propres — distincts de la juridiction « parent ».

#### Limites

Les listes GAFI et UE évoluent. La liste précise à un instant donné doit être vérifiée à la source (sites officiels). Une juridiction sortie de la liste grise reste un facteur de risque pertinent dans une analyse — la sortie ne vaut pas absolution.

#### Lien avec le fil rouge

> **CLEARFLOW — Cartographie offshore**
> 
> Le dossier Haddad implique au moins 5 juridictions non-françaises : Chypre (UE, structurelle), Émirats (commerce + free zone), Bénin (intermédiaire), Suisse (banque privée), Liban (origine, suspicion d’infraction prédécesseur). Nassim qualifie chaque juridiction (statut GAFI/UE, EAR/CRS, Egmont) et anticipe les délais de coopération. Dès le cadrage, il prévoit que les éléments chypriotes seront accessibles en 2 à 4 semaines via Egmont, les émiratis en 4 à 8 semaines, les libanais à très long terme et avec un haut degré d’incertitude.

#### Points clés à retenir

- « Offshore » est imprécis ; préférer « juridiction à risque » et qualifier précisément.
- EAR/CRS, GAFI, listes UE structurent la qualification.
- Le secret bancaire moderne s’est érodé vis-à-vis des fiscs ; il reste fort vis-à-vis des particuliers et de nombreuses procédures civiles.
- Delaware / Nevada / Wyoming sont des points d’attention transatlantiques sous-estimés.

-----

## PARTIE III — SOURCES OSINT FINANCIÈRES

*Huit chapitres pour la cartographie complète des sources ouvertes financières — registres, comptes annuels, marchés publics, contentieux, presse, leaks, SOCMINT financier. Cette partie est la plus volumineuse de la phase « pré-réquisitions » d’une enquête.*

-----

### Chapitre 11 — Registres d’entreprises : France, UK, US

#### Objectif du chapitre

Maîtriser les **trois principaux registres** que tout analyste FININT consulte régulièrement : France (Infogreffe / INPI), Royaume-Uni (Companies House), États-Unis (registres fédéraux et étatiques, principalement Delaware, et SEC EDGAR pour les sociétés cotées).

#### Le concept

Un **registre du commerce et des sociétés** est la base officielle qui recense les entités juridiques d’un pays, leurs caractéristiques (forme, capital, dirigeants, siège), et publie certains actes (statuts, modifications, comptes annuels selon les seuils). C’est la source de premier niveau pour identifier une entité et pour ouvrir une enquête.

Tous les registres ne sont pas équivalents en richesse, en accessibilité et en gratuité. Trois pôles dominent les enquêtes occidentales modernes.

#### France — INPI / Infogreffe / RCS

Architecture actuelle (2025) :

- **INPI (Registre national des entreprises — RNE)** : depuis 2023, l’INPI centralise le RNE, qui regroupe les informations historiquement réparties entre RCS (commerçants) et autres registres (artisans, agricoles, libéraux). Accès gratuit et public à beaucoup de données via [data.inpi.fr](https://data.inpi.fr/) et le portail RNE.
- **Infogreffe** : portail des greffes de tribunaux de commerce. Accès payant pour certains actes, gratuit pour la fiche identité. Toujours utilisé en pratique pour les **actes** (statuts, comptes annuels, K-bis officiel).
- **Pappers** : agrégateur tiers gratuit, très ergonomique, qui republie une grande partie des données ouvertes (siret, dirigeants, comptes annuels jusqu’aux seuils, liens entre sociétés). Devenu un réflexe d’analyste.
- **Société.com, Verif.com, Manageo, Score3** : agrégateurs concurrents avec degrés de gratuité variables.
- **BODACC** (Bulletin officiel des annonces civiles et commerciales) : publications officielles (créations, radiations, procédures collectives). Accès gratuit en ligne.

**Ce que l’analyste obtient gratuitement :**

- Identification : SIREN/SIRET, dénomination, forme juridique, capital social, date de création, NAF/APE.
- Adresse du siège, et historique des sièges.
- Dirigeants : président, gérant, DG, directeurs, administrateurs (avec dates de nomination et de fin).
- Liste des établissements secondaires.
- Procédures collectives : sauvegarde, redressement, liquidation.
- Modifications du registre (changements de dénomination, de capital, de dirigeants, transferts de siège).
- **Comptes annuels** publiés (sociétés au-delà des seuils, dans la limite du droit à confidentialité demandé par certaines petites sociétés depuis 2014).

**Pour aller plus loin (réquisition / accès professionnel) :** liste des associés (rarement publique), informations bancaires.

#### Royaume-Uni — Companies House

[Companies House](https://www.gov.uk/government/organisations/companies-house) — registre officiel UK. C’est l’un des registres **les plus ouverts au monde**. Accès gratuit et complet à :

- Identification de la société (Company Number, denomination, forme, statut).
- Officers (directors, secretaries) — actuels et historiques, avec dates et adresses.
- **Persons with Significant Control (PSC)** — depuis 2016, le UK rend public le registre des personnes exerçant un contrôle significatif (équivalent UBO). Seuils : 25 % de capital ou de droits de vote, ou contrôle effectif. Accessible en ligne, gratuit, par société.
- Comptes annuels (filings) publiés pour la quasi-totalité des sociétés actives.
- Confirmations annuelles (Annual Confirmation Statement).
- Mortgages and charges (sûretés inscrites).

Cas particuliers : LLP (Limited Liability Partnership), Scottish Limited Partnership (SLP — historiquement utilisées pour le blanchiment, soumises au PSC depuis 2017).

**Limites du PSC** : déclaratif. Les fraudeurs déclarent parfois faux. Les sanctions pour fausse déclaration existent mais sont peu appliquées en pratique pour les petites entités. Reste, pour l’analyste FININT, l’une des sources les plus utiles au monde.

#### États-Unis — Delaware, SEC EDGAR, registres étatiques

Les US n’ont pas de registre fédéral des sociétés. Chaque État a son propre registre. Les principaux :

- **Delaware Division of Corporations** — siège juridique d’environ 60 % des sociétés cotées américaines et de la majorité des LLC US. La consultation publique est très limitée : nom, statut, type, et c’est à peu près tout. Pas de dirigeants publics. Pas d’UBO public (en attente de la mise en œuvre du **Corporate Transparency Act** — voir infra).
- **California Secretary of State, New York Department of State, Texas, Florida, Wyoming, Nevada** — chacun a son portail.
- **OpenCorporates** — agrégateur qui aspire les registres étatiques et offre une recherche unifiée. Très utile pour l’analyste FININT.

**SEC EDGAR** : pour les **sociétés cotées** ou émettrices de titres aux US, la SEC (Securities and Exchange Commission) publie via [EDGAR](https://www.sec.gov/edgar) les déclarations détaillées (10-K, 10-Q, 8-K, S-1, proxy statements, etc.). Source d’or pour les grandes entreprises et leurs filiales.

**Corporate Transparency Act (CTA)** : loi US de 2021 ayant obligé les LLC et corporations à déclarer leurs UBO à FinCEN. Trajectoire très instable en 2024-2025 (contestations judiciaires, décisions successives). **Depuis l’interim final rule FinCEN de mars 2025**, les sociétés domestiques américaines (« domestic reporting companies ») **ne sont plus tenues** de déclarer leurs bénéficiaires effectifs à FinCEN ; l’obligation subsiste principalement pour **certaines entités étrangères enregistrées pour faire des affaires aux États-Unis**. La situation reste sujette à évolution (textes, décisions, contentieux) — un analyste consulte la mise à jour la plus récente sur le site FinCEN avant toute conclusion.

**FinCEN files** : le leak FinCEN 2020 (BuzzFeed/ICIJ) a révélé que les SAR américains contenaient des éléments sur la criminalité financière mondiale. Pas une source courante mais à connaître (Chapitre 18).

#### L’utilité opérationnelle

Pour la majorité des dossiers FININT impliquant des entités françaises, britanniques ou américaines (cotées), ces trois registres couvrent l’essentiel du travail d’identification et de cartographie de premier niveau. La gratuité française et britannique permet un travail systématique sans budget. La gratuité partielle américaine est compensée par les agrégateurs (OpenCorporates) et SEC EDGAR pour les cotées.

#### Méthode — workflow d’identification

1. **France** : Pappers (vue rapide) + INPI/RNE (validation officielle) + Infogreffe (acte officiel si besoin) + BODACC (procédures).
1. **UK** : Companies House (everything) + recherche par directeur/PSC pour identifier les autres sociétés liées.
1. **US** : OpenCorporates (vue agrégée) + registre étatique pertinent (validation) + SEC EDGAR si coté + FinCEN si CTA en vigueur.

Toujours **archiver** les pages consultées (capture d’écran horodatée, hash si possible — chapitre 53).

#### Mini-walkthrough

Cible : *« NEXUS TRADING SAS, suspectée d’être une société écran française liée à un réseau franco-libanais. »*

- Pappers : SIREN, dénomination, capital 10 000 €, créée il y a 14 mois, dirigeant unique « Monsieur X », adresse à un cabinet de domiciliation, NAF 4690Z (commerce de gros non spécialisé). Comptes non publiés (1er exercice non clos).
- INPI : confirme + accès aux statuts initiaux.
- BODACC : aucune procédure.
- Recherche par dirigeant : Monsieur X est gérant de 7 autres SAS, toutes domiciliées à la même adresse, toutes créées entre 2023 et 2024, toutes en commerce de gros. **Pattern clair de gestionnaire multi-sociétés**.

Conclusion : à ce stade, NEXUS est **possible-à-probable** une société de façade ou un véhicule à usage spécifique. Le statut de « société écran » exige des éléments complémentaires (chapitre 26).

#### Erreurs fréquentes

- **Se fier uniquement à Pappers** sans aller voir les actes officiels (Pappers est utile mais peut être en retard sur certaines mises à jour).
- **Ignorer le BODACC** (les procédures collectives sont parfois la clé d’un dossier).
- **Oublier les agrégateurs internationaux** (OpenCorporates) quand l’enquête sort de France.
- **Ne pas archiver** : un registre peut être modifié ou une fiche supprimée. La capture horodatée fait foi.

#### Limites

Les registres sont **déclaratifs**. Les fraudeurs peuvent fausser les déclarations. Les modifications sont parfois en retard. L’UBO déclaré peut être un prête-nom. Croiser systématiquement avec d’autres sources.

#### Lien avec le fil rouge

> **CLEARFLOW — Cartographie initiale via registres**
> 
> Sur les 14 sociétés présumées liées à Haddad, Nassim identifie 4 SAS françaises via Pappers/INPI, 2 Limited UK via Companies House (avec PSC pointant deux personnes physiques distinctes — possible alignement de prête-noms), et 1 LLC Delaware via OpenCorporates (pas d’UBO accessible — limite documentée). Le travail registre prend environ 6 heures pour cette première vague et produit un premier graphe de liens (chapitre 31).

#### Points clés à retenir

- France : INPI/RNE + Pappers + Infogreffe + BODACC. Largement gratuit.
- UK : Companies House. Gratuit, riche, avec PSC.
- US : OpenCorporates + registres étatiques + SEC EDGAR. CTA à suivre.
- Toujours archiver. Toujours croiser.

-----

### Chapitre 12 — Registres d’entreprises : reste de l’Europe et du monde

#### Objectif du chapitre

Étendre la couverture aux **autres juridictions clés** : reste de l’UE, Suisse, juridictions offshore, pays émergents. La logique reste la même qu’au chapitre 11 ; les outils et les degrés d’ouverture varient.

#### Le concept

Hors France/UK/US, l’analyste mobilise plusieurs niveaux de sources :

1. **Registres nationaux directs** quand ils sont accessibles en ligne et en langue exploitable.
1. **Portails européens consolidés** (e-Justice, BRIS).
1. **Agrégateurs tiers** (OpenCorporates, Sayari, Orbis, Dun & Bradstreet — chapitres 50-51).
1. **Bases UBO européennes** (chapitre 13).

#### Méthode — registres clés par juridiction

**Allemagne — Handelsregister**. [handelsregister.de](https://www.handelsregister.de/) ou portail unifié. Accès payant à de nombreux actes mais informations de base souvent gratuites. La structure (GmbH, AG, KG, OHG) doit être maîtrisée (chapitre 21). Bundesanzeiger pour les comptes annuels publiés.

**Italie — Registro Imprese**. [registroimprese.it](https://www.registroimprese.it/) — via les chambres de commerce. Payant. La société italienne est riche en formes (S.p.A., S.r.l., S.a.s., S.n.c., cooperativa).

**Espagne — Registro Mercantil Central** (RMC). Accès en ligne payant ; agrégateurs (Axesor, Einforma) fournissent des données plus accessibles.

**Belgique — Banque-Carrefour des Entreprises (BCE / KBO)**. [kbopub.economie.fgov.be](https://kbopub.economie.fgov.be/). Recherche par numéro d’entreprise, accès gratuit aux infos publiques (statut, dirigeants visibles via les publications du Moniteur belge — annexes au Moniteur).

**Pays-Bas — KvK (Kamer van Koophandel)**. Registre des chambres de commerce néerlandaises. Très utilisé dans les schémas internationaux (les Pays-Bas sont une juridiction de holding très active).

**Luxembourg — Registre de Commerce et des Sociétés (RCS)**. [lbr.lu](https://www.lbr.lu/) — informations de base gratuites. Densité de SOPARFI et SCSp (sociétés de gestion d’actifs).

**Suisse — Zefix**. [zefix.ch](https://www.zefix.ch/) — registre fédéral. Accès gratuit aux infos de base (forme, siège, dirigeants, état). Accès aux actes par les registres cantonaux (Genève, Zurich, etc., souvent payant).

**Pologne — KRS (Krajowy Rejestr Sądowy)**. Accès en ligne, en polonais, gratuit. Important pour les schémas Europe centrale.

**Roumanie — ONRC (Oficiul Național al Registrului Comerțului)**. Accès en ligne, payant.

**Estonie, Lettonie, Lituanie**. Registres nationaux accessibles en ligne, en partie en anglais. Les baltes hébergent une part importante des structures Europe de l’Est.

**Russie — EGRUL**. Registre russe accessible en ligne. Depuis 2022, l’accès depuis l’UE est techniquement entravé pour des raisons de sanctions et politiques. Des copies / agrégateurs existent (par exemple via OpenCorporates pour les données antérieures).

**Ukraine — YouControl, Opendatabot**. Bases agrégées qui exploitent les registres ouverts ukrainiens (très ouverts depuis les réformes 2014+).

**Israël — Registrar of Companies**. Accès payant, en hébreu.

**Chine — National Enterprise Credit Information Publicity System** (NECIPS) ; **Qichacha**, **Tianyancha** (agrégateurs commerciaux populaires). Données souvent en chinois.

**Hong Kong — Companies Registry / ICRIS**. Accès en ligne, payant pour les actes. Une des juridictions à transparence relative en Asie.

**Singapour — ACRA (BizFile+)**. Accès en ligne, payant pour les rapports détaillés.

**Inde — Ministry of Corporate Affairs (MCA)**. Accès en ligne, partiellement gratuit.

**Émirats arabes unis — registres par émirat et par free zone** (DED Dubaï, ADGM, DIFC, DMCC, RAK ICC, JAFZA). Hétérogène. Le DIFC et l’ADGM sont les juridictions de droit anglais des Émirats, avec leurs propres registres.

**Liban, Iran, Soudan, Venezuela** etc. — registres souvent inaccessibles en ligne ou peu fiables. Coopération internationale et sources secondaires (presse, leaks) deviennent prépondérantes.

**Caraïbes (BVI, Cayman, Bahamas, Bermudes)** — registres avec accès très limité au public. UBO accessible aux autorités sous conditions (BOSS pour BVI). Le travail repose largement sur les leaks (Panama Papers, Pandora Papers) et la coopération internationale.

#### Portails européens consolidés

**BRIS (Business Registers Interconnection System)** — portail européen e-Justice qui interconnecte les registres nationaux des États membres. [e-justice.europa.eu](https://e-justice.europa.eu/). Recherche cross-border simplifiée.

**EBOCS (European Business Ownership and Control Service)** — agrégation des registres UE pour les analystes professionnels.

#### L’utilité opérationnelle

Pour un dossier multi-juridictionnel, la séquence type :

- **OpenCorporates** pour la vue agrégée initiale.
- **Registres nationaux directs** pour la validation et les actes.
- **BRIS** pour les recherches transfrontalières en UE.
- **Sayari, Orbis** (chapitres 50-51) si abonnement disponible — couverture internationale plus large et plus complète.

#### Mini-walkthrough

Cible : OMEGA HOLDINGS LTD, Chypre, identifiée dans une DS comme contrepartie d’un flux de 850 K€.

- OpenCorporates : trouvée — Cyprus, registered 2019, status active.
- Registre chypriote (Department of Registrar of Companies and Intellectual Property) : accès en ligne, partiellement gratuit. Identification confirmée. Directors visibles ; UBO **non public** (accès limité depuis l’arrêt CJUE 2022 — chapitre 13).
- Recherche complémentaire via leaks : présence d’OMEGA HOLDINGS dans Pandora Papers ? (chapitre 18).
- Sayari (si disponible) : recoupement avec dossiers similaires.

#### Erreurs fréquentes

- **Se contenter d’OpenCorporates.** Utile pour la vue agrégée mais souvent en retard sur les modifications récentes.
- **Ne pas tester plusieurs orthographes** dans les langues étrangères (translittérations, accents, articles initiaux).
- **Sous-estimer les agrégateurs locaux** (Qichacha en Chine, YouControl en Ukraine).

#### Limites

Beaucoup de registres asiatiques, africains, ou caribéens sont peu accessibles ou peu fiables. La coopération internationale (Egmont) et les leaks deviennent alors les principaux leviers.

#### Lien avec le fil rouge

> **CLEARFLOW — Multi-juridictions**
> 
> Nassim mobilise BRIS pour les sociétés européennes du dossier Haddad (CY, FR, DE, NL), OpenCorporates pour la vue agrégée, Sayari (licence du service) pour la validation et l’extension du graphe, registres locaux émiratis pour les sociétés Free Zone identifiées, et coopération via Egmont pour les juridictions inaccessibles (Liban). Le travail prend 4 à 5 jours pour la cartographie complète.

#### Points clés à retenir

- Hors France/UK/US, mobilisation d’un mix : registres nationaux + portails consolidés + agrégateurs.
- BRIS est le portail UE de référence pour la recherche multi-juridictions.
- Les juridictions caribéennes et certaines asiatiques exigent leaks + coopération.

-----

### Chapitre 13 — Identifier les bénéficiaires effectifs

#### Objectif du chapitre

Comprendre la notion de **bénéficiaire effectif (UBO)**, savoir mobiliser les registres UBO disponibles, anticiper leurs limites, et croiser pour identifier le ou les UBO réels d’une structure. C’est un objectif central du FININT, et l’un des plus difficiles dans les juridictions opaques.

#### Le concept

Le **bénéficiaire effectif** (UBO — Ultimate Beneficial Owner) d’une entité est, en droit européen :

- toute personne physique qui détient ou contrôle, directement ou indirectement, plus de **25 %** du capital ou des droits de vote ;
- ou exerce un contrôle par d’autres moyens (contrat, convention de vote, droit de nomination) ;
- ou, à défaut, occupe la fonction de dirigeant principal (UBO « de dernier recours », en France parfois appelé UBO « par défaut »).

Pour les **trusts et fondations**, l’UBO inclut : le constituant (settlor), le ou les trustee(s), le ou les protecteur(s), le ou les bénéficiaire(s) (ou catégorie de bénéficiaires), et toute autre personne contrôlant le trust.

#### Les registres UBO

Depuis la 4ème puis la 5ème directive AML, l’UE a imposé aux États membres de tenir des **registres des bénéficiaires effectifs**. Organisation et accès varient.

**France — Registre des bénéficiaires effectifs (RBE)** tenu par l’INPI. Toutes les entités juridiques françaises doivent déclarer leurs UBO. Accès au RBE :

- pour les autorités compétentes : sans restriction.
- pour les assujettis (banques, etc.) : dans le cadre de leurs obligations LCB-FT.
- pour le public : a été ouvert puis restreint suite à l’**arrêt CJUE du 22 novembre 2022** qui a invalidé l’accès public généralisé au motif de protection de la vie privée. La situation actuelle (2025) : accès maintenu pour les autorités, les assujettis, et certaines catégories spécifiquement justifiées (presse d’investigation sous conditions, certains professionnels). L’accès « grand public » direct est restreint. À vérifier auprès de la dernière communication de l’INPI au moment de l’enquête.

**UK — PSC (Persons with Significant Control)**. Public et gratuit via Companies House. Resté ouvert (UK hors UE depuis Brexit, donc non concerné par l’arrêt CJUE).

**Allemagne — Transparenzregister**. Accès très restreint au public depuis l’arrêt CJUE.

**Pays-Bas — UBO-register**. Idem, restreint.

**Luxembourg — Registre des bénéficiaires effectifs (RBE)**. Restreint depuis CJUE.

**Italie, Espagne, autres EU**. Situations variables, mais tendance générale au resserrement post-CJUE.

**En pratique, l’accès varie désormais fortement** selon les États membres, les catégories d’acteurs (autorités, assujettis LCB-FT, presse, chercheurs, professionnels avec intérêt légitime) et la justification d’un **intérêt légitime** à connaître l’UBO. L’analyste vérifie systématiquement l’état du droit dans chaque juridiction concernée par le dossier au moment de l’enquête.

**Pays tiers** (BVI, Cayman, Émirats, etc.) — registres existent mais accès quasi-systématiquement réservé aux autorités locales.

**AMLA et nouveau paquet AML européen (2024-2026)** : prévoit une **interconnexion européenne** des registres UBO et un encadrement plus précis de l’accès. Mise en œuvre progressive.

#### L’utilité opérationnelle

L’UBO est la **clé** d’une cartographie : sans UBO, on a une coquille juridique sans sa réalité humaine.

L’analyste cherche à :

- identifier l’UBO « déclaré » officiellement dans le registre ;
- vérifier sa **plausibilité** (cet UBO a-t-il les caractéristiques pour être réellement le contrôleur — capacité financière, expérience, lien avec l’activité ?) ;
- identifier d’éventuels signes de **prête-nom** (chapitre 25) ;
- recouper avec d’autres sources (leaks, presse, registres connexes) pour confirmer ou infirmer.

#### Méthode — démarche en 4 étapes

1. **Récupérer la déclaration UBO officielle** quand accessible (RBE France pour les autorités/assujettis, PSC UK public, etc.).
1. **Vérifier la cohérence** : profil, nationalité, adresse, antécédents. Un UBO de 22 ans déclaré contrôleur d’un groupe à 50 M€ de CA est invraisemblable.
1. **Croiser** avec : autres mandats déclarés, presse, leaks, réseaux sociaux, registres connexes.
1. **Calibrer la confiance** : UBO déclaré = *possible* ; UBO confirmé par recoupement = *probable* ; UBO confirmé par documents indépendants (réquisitions, EAR) = *quasi-certain*.

#### Mini-walkthrough

Cible : OMEGA HOLDINGS LTD (Chypre).

- Recherche RBE chypriote : restreint depuis CJUE.
- Companies House équivalent chypriote : directors visibles, UBO non.
- Sayari (licence) : indique un UBO possible, M. Y, basé à Beyrouth, avec un lien sur trois autres sociétés méditerranéennes.
- Recherche dans Pandora Papers (Aleph ICIJ) : OMEGA HOLDINGS apparaît, avec un settlor d’un trust chypriote. Le settlor est *distinct* de M. Y. **Hypothèse : M. Y est le directeur déclaré, mais le settlor du trust contrôle in fine** — UBO probable = settlor.
- Vérification du settlor : presse libanaise antérieure, fonctions dans des sociétés liées au commerce régional. Profil cohérent.
- Calibration : UBO probable = settlor (Karim Haddad ou personne associée), niveau de confiance *probable* sur la base du recoupement Pandora.
- Lacune : la liste exacte des bénéficiaires du trust est inaccessible — il faudrait Egmont avec Mokas ou MROS selon l’évolution.

#### Erreurs fréquentes

- **Croire l’UBO déclaré sans vérification.** Beaucoup d’UBO déclarés sont des prête-noms.
- **Conclure à un prête-nom sans preuve.** Inversement, ce n’est pas parce que l’UBO déclaré paraît modeste qu’il est nécessairement un prête-nom.
- **Ignorer le contrôle indirect.** Un UBO peut contrôler par convention, par usufruit, par contrat de gestion — pas seulement par % de capital.
- **Mélanger l’UBO d’une société et l’UBO d’un compte bancaire.** Ce ne sont pas toujours les mêmes (un compte peut être au nom d’une personne mandataire de la société, ou d’un fiduciaire).

#### Limites

L’identification de l’UBO réel d’une structure complexe **multi-juridictionnelle** opaque exige souvent : des leaks, des coopérations internationales, des réquisitions auprès de banques, et parfois reste **indéterminable** par le seul OSINT.

#### Lien avec le fil rouge

> **CLEARFLOW — Identification UBO progressive**
> 
> Pour les 4 SAS françaises : UBO déclarés au RBE = personnes physiques résidant en France. Pour 2 d’entre elles, l’UBO déclaré est un retraité français de 78 ans avec un patrimoine modeste — **alarme prête-nom probable**. Pour les Limited UK : PSC = M. Y (libanais, basé à Dubaï). Pour OMEGA Chypre : UBO déclaré = trustee professionnel (couverture). Pour la LLC Delaware : aucun UBO accessible (depuis l’interim final rule FinCEN de mars 2025, les LLC domestiques US sont exemptées de déclaration BOI à FinCEN). Conclusion : *probable* que Karim Haddad est l’UBO réel d’une partie significative du réseau, sous prête-noms et trustees, mais l’identification *quasi-certaine* exigerait coopération internationale et réquisitions.

#### Points clés à retenir

- UBO = personne physique qui détient/contrôle ultimement, seuils 25 % en UE (capital ou droits de vote).
- Registres UBO : accès restreint en UE depuis CJUE 2022. UK PSC reste public.
- Croiser systématiquement déclaration / cohérence / recoupements / leaks.
- L’UBO réel d’une structure complexe peut être *indéterminable* sans coopération.

-----

### Chapitre 14 — Comptes annuels, bilans et documents financiers

#### Objectif du chapitre

Savoir trouver et **lire les documents financiers publiés** par les entreprises pour en extraire des indicateurs de cohérence économique, des signaux d’anomalie, et étayer les hypothèses d’enquête. Le détail technique de l’analyse comptable sera couvert au chapitre 36 ; ici, on se concentre sur l’accès et la lecture rapide.

#### Le concept

Selon les juridictions et la taille des entreprises, les **comptes annuels** publiés varient en richesse :

- **Bilan** — photo du patrimoine à une date (actif / passif).
- **Compte de résultat** — flux d’activité sur une période (produits / charges / résultat).
- **Annexe** — explications, méthodes, tableaux complémentaires.
- **Tableau des flux de trésorerie** — variations de cash sur la période (très utile, mais pas obligatoire pour les petites sociétés).
- **Rapport de gestion** — narratif des dirigeants.
- **Rapport des commissaires aux comptes** (CAC) — quand la société y est tenue.

En France : seuils de publication. Au-delà des seuils (à la fois en CA, total bilan, effectif), publication obligatoire au greffe. Possibilité depuis 2014 pour les très petites sociétés de demander la **confidentialité** des comptes (publication avec accès restreint aux assujettis et autorités, pas au public). Chez Pappers et autres agrégateurs, on voit fréquemment la mention « comptes confidentiels ».

Au UK : la quasi-totalité des sociétés publient. Format selon la taille (statutory accounts, abridged, micro-entity).

Aux US : les sociétés non cotées ne publient pas en règle générale ; les sociétés cotées publient via SEC EDGAR (très riches : 10-K, 10-Q, 8-K).

En Allemagne, les sociétés publient au Bundesanzeiger ; en Belgique, au Moniteur belge ; en Italie, à la Camera di Commercio ; au Luxembourg, au RCS (avec certaines obligations spécifiques).

#### L’utilité opérationnelle

Lecture FININT d’un bilan / compte de résultat (pour le détail technique : chapitre 36) :

- **Cohérence sectorielle** : la marge brute est-elle cohérente avec le secteur ? Le ratio CA / effectif est-il vraisemblable ?
- **Évolution dans le temps** : les chiffres explosent-ils sans justification ? Sont-ils stables tandis que l’apparence opérationnelle change ?
- **Postes anormaux** : créances clients gigantesques (fictives ?), prêts intragroupe sans contrepartie, immobilisations incorporelles surévaluées, charges de « conseil » dominantes, charges de sous-traitance massives sans personnel propre ?
- **Engagements hors bilan** : garanties, cautions données — souvent dans l’annexe.
- **Écart résultat / trésorerie** : un beau résultat sans cash correspondant est suspect.

#### Méthode — récupération et lecture rapide

Pour une société française :

- Pappers : aperçu des comptes publiés.
- Infogreffe : téléchargement de l’acte officiel (PDF) — gratuit ou modique selon les actes.
- INPI/RNE : équivalent.

Pour une société UK : Companies House — téléchargement gratuit.

Pour une société US cotée : SEC EDGAR — téléchargement gratuit.

Pour une société non publique US ou hors UE : selon le pays. Souvent, comptes inaccessibles (juridiction opaque ou exemption). Mention explicite dans le livrable.

**Lecture rapide en 5 ratios clés** :

1. **Marge brute** = (CA - achats consommés) / CA. À comparer avec le secteur.
1. **Marge d’exploitation** = résultat d’exploitation / CA.
1. **Charges de personnel / CA** — donne l’intensité main-d’œuvre.
1. **Stock / CA** — rotation des stocks, anomalie si très élevé.
1. **Créances clients / CA** — délai de paiement clients, anomalie si très élevé (ventes fictives ou clients fragiles).

À comparer avec les ratios moyens du secteur (sources : INSEE, statistiques sectorielles, base de données des cabinets comptables).

#### Mini-walkthrough

NEXUS TRADING SAS (France), 1er exercice clos. Comptes publiés (non confidentiels).

- CA : 12,4 M€ — élevé pour un 1er exercice avec dirigeant unique.
- Achats consommés : 11,9 M€. Marge brute : 4 % — très faible pour le négoce de gros (5-10 % attendu).
- Charges de personnel : 32 K€ (un dirigeant, sans salariés). Cohérent avec un dirigeant unique et activité de pure intermédiation.
- Stock : 0 €. Cohérent avec une activité d’intermédiation sans détention.
- Créances clients : 280 K€ (≈ 8 % du CA, soit ~30 jours de délai — normal).
- Résultat d’exploitation : 80 K€. Faible mais positif.
- Trésorerie en fin d’exercice : 35 K€.

Lecture FININT : profil compatible avec une activité de **pure intermédiation commerciale** (pas de stock, pas de salariés autres que le dirigeant) sur un volume élevé pour un 1er exercice. Marge faible mais cohérente avec une intermédiation. Attention : un tel profil est aussi compatible avec une **société de transit** dans un schéma TBML (passage de fonds avec apparence commerciale). Ne tranche pas — élément de soupçon **possible**, à recouper avec la cohérence des contreparties et des marchandises.

#### Erreurs fréquentes

- **Lire les chiffres sans les comparer.** Un CA de 12 M€ ne dit rien sans le secteur, la taille, l’historique.
- **Ignorer l’annexe.** Beaucoup d’informations utiles y figurent (engagements, méthodes comptables, événements postérieurs).
- **Surinterpréter une faible marge.** Faible marge ≠ blanchiment automatique. Elle est cohérente avec le négoce de gros, l’intermédiation, certains modèles online.
- **Considérer la « confidentialité » comme un signal en soi.** Beaucoup de TPE françaises légitimes optent pour la confidentialité pour des raisons concurrentielles.

#### Limites

Les comptes annuels sont **historiques** (publiés généralement 6 à 12 mois après la clôture). Ils peuvent être **falsifiés** (sans CAC, le contrôle externe est minimal). L’analyste ne peut pas conclure sur les seuls comptes — il les croise.

#### Lien avec le fil rouge

> **CLEARFLOW — Lecture des comptes**
> 
> Sur les 4 SAS françaises du réseau Haddad, 2 ont publié des comptes (les 2 plus anciennes), 2 sont en 1er exercice. Sur celles qui ont publié : marges brutes faibles (3-5 %), charges de conseil à des sociétés liées chypriotes (cumulé 280 K€/an), prêts intragroupe sans intérêts apparents. Profil compatible avec un schéma de **transit avec rétention de marge minimale** et **transferts intragroupe possiblement de complaisance**. Soupçons : *probable* à *quasi-certain* sur le schéma de transit, *possible* sur la qualification fraude. Approfondissements requis.

#### Points clés à retenir

- Comptes annuels = source publique précieuse, surtout en France et UK.
- Lecture rapide en 5 ratios + comparaison sectorielle.
- Pas de conclusion sur les seuls comptes — toujours croiser.
- L’absence de comptes (confidentialité ou non publication) est documentée mais n’est pas un soupçon en soi.

-----

### Chapitre 15 — Marchés publics, subventions et appels d’offres

#### Objectif du chapitre

Connaître les **bases publiques de marchés publics, subventions et appels d’offres** comme source d’enquête, notamment pour les schémas de corruption (chapitre 42), de favoritisme et d’attribution douteuse.

#### Le concept

Les **marchés publics** (commande publique) sont, dans de nombreuses juridictions, soumis à des obligations de **publication** : annonces préalables, attributions, contrats. Ces données ouvertes sont une mine d’information pour l’analyste FININT enquêtant sur la corruption ou les schémas adressés à l’État ou à des collectivités.

#### Méthode — bases utiles par pays

**France** :

- **BOAMP** (Bulletin officiel des annonces de marchés publics) — publications obligatoires des marchés au-delà des seuils. Accès en ligne, gratuit.
- **JOUE / TED (Tenders Electronic Daily)** — équivalent UE.
- **data.gouv.fr** : datasets ouverts sur la commande publique (DECP — Données essentielles de la commande publique).
- **HATVP** (Haute Autorité pour la transparence de la vie publique) — déclarations de patrimoine et d’intérêts des responsables publics. Accès en ligne, partiellement public. **Périmètre à connaître** : toutes les fonctions publiques ne sont pas couvertes de la même manière. Le périmètre des assujettis HATVP est défini par fonctions et seuils (parlementaires, membres du gouvernement, élus locaux à partir de certains seuils, dirigeants d’organismes publics, etc.). Un élu local d’une petite commune n’est pas nécessairement couvert ; un parlementaire l’est. Vérifier la liste à jour des assujettis sur le site de la HATVP.
- **AIFE — Chorus Pro** (factures de l’État).

**UE** :

- **TED (Tenders Electronic Daily)** — toutes les annonces UE au-delà des seuils.
- **eForms** — format unifié à partir de 2024.
- **EU Funding & Tenders Portal** pour les financements européens (Horizon, FEDER, FSE, etc.).

**UK** :

- **Contracts Finder**, **Find a Tender Service**.

**US** :

- **SAM.gov** (System for Award Management) — base fédérale.
- **USAspending.gov** — dépenses fédérales.
- **State and local procurement portals**.

**Subventions** :

- France : data.gouv.fr (subventions associatives, aides aux entreprises).
- UE : Cohesion Open Data Platform.

#### L’utilité opérationnelle

L’analyste cherche à identifier :

- **Marchés attribués à des sociétés du réseau** sous enquête (lien direct avec le secteur public).
- **Schémas d’attribution suspects** : faible nombre de soumissionnaires, dérogations à appel d’offres, marchés découpés sous les seuils, marchés négociés sans publicité.
- **Liens entre attributaires et décideurs** (HATVP en France pour les conflits d’intérêts).
- **Sous-traitants en cascade** dont une partie peut être des sociétés écrans.

#### Mini-walkthrough

Une SARL de BTP en région française, dans un dossier de soupçon de corruption locale.

- BOAMP : la SARL a remporté 7 marchés sur 3 ans, dans 3 communes, pour un montant cumulé de 4,2 M€.
- DECP : on identifie les acheteurs publics (3 communes), les types de marchés (voirie, bâtiments scolaires).
- HATVP : le maire de la commune principale a déclaré un intérêt (ami / parent travaillant dans une société liée).
- Recoupement : on cherche dans les conseils municipaux, presse locale, des éléments confirmant ou infirmant.

Conclusion : signal de **conflit d’intérêts probable** à approfondir. Pas de qualification de corruption à ce stade — exige des éléments d’intentionnalité et de contrepartie.

#### Erreurs fréquentes

- **Lire un marché public comme une preuve.** Beaucoup de marchés sont gagnés légitimement par des entreprises locales — la concentration n’est pas la preuve.
- **Ignorer les seuils.** Les marchés sous certains seuils ne sont pas publiés — l’analyse est partielle.
- **Sous-utiliser HATVP** en France — c’est une source précieuse pour les liens entre décideurs et entreprises.

#### Limites

Les bases publiques ne couvrent pas tous les marchés (seuils). Elles ne disent rien des **marchés privés** (B2B), qui peuvent aussi être l’objet de corruption. La corruption se prouve par d’autres moyens (preuves d’intention, paiements traçables, témoignages).

#### Lien avec le fil rouge

> **CLEARFLOW — Marché ivoirien**
> 
> Une des sociétés du réseau Haddad, NEXUS NEGOCE (Côte d’Ivoire), a remporté un marché public ivoirien de fourniture de matériel agricole en 2023 pour 3,2 M€. Source : presse économique régionale + rapport de la Chambre des comptes ivoirienne. Profil du marché : faible nombre de soumissionnaires, attributaire créé moins d’un an avant l’attribution, lien possible avec un haut fonctionnaire ivoirien (presse). Le volet ivoirien sera renvoyé en coopération internationale (Egmont avec la CRF ivoirienne) — impossible à approfondir depuis la France sans ce levier.

#### Points clés à retenir

- BOAMP, TED, SAM.gov, Contracts Finder : bases ouvertes principales.
- HATVP : essentielle pour les liens décideurs / entreprises en France.
- Marchés publics ne prouvent pas la corruption : ils alimentent l’hypothèse.
- Les marchés privés et les marchés sous seuils sont des angles morts.

-----

### Chapitre 16 — Contentieux, procédures collectives et sanctions administratives

#### Objectif du chapitre

Mobiliser les **données de contentieux et de procédures** comme indicateurs de risque, de tension, ou d’historique d’anomalies. Une société ou une personne avec un passif contentieux significatif n’est pas nécessairement coupable — mais elle a un historique à intégrer.

#### Le concept

Plusieurs catégories de données :

**Procédures collectives** (sauvegarde, redressement judiciaire, liquidation judiciaire). En France : BODACC, Infogreffe. Au UK : The Gazette. Dans la majorité des juridictions, ces procédures sont publiques.

**Décisions de justice publiées** : selon les juridictions, certaines décisions sont publiées (avec ou sans anonymisation). En France : Légifrance, Doctrine, Dalloz, Lexbase. Plateformes payantes pour certains accès. Open data judiciaire en cours (depuis le décret « open data des décisions »).

**Sanctions administratives** :

- **AMF** (Autorité des marchés financiers) — sanctions sur les acteurs des marchés financiers en France.
- **ACPR** (Autorité de contrôle prudentiel et de résolution) — sanctions sur les banques, assurances, PSP, EME.
- **Commission des sanctions de l’AMF**, idem ACPR : décisions publiées.
- **CNIL** : sanctions RGPD.
- **Autorité de la concurrence**.
- Équivalents européens : ESMA, EBA, EIOPA.
- **OFAC**, **OFSI**, **DG Trésor — pôle sanctions financières internationales** : sanctions liées aux sanctions économiques.
- **SEC**, **DOJ**, **CFTC** aux US.

**Cybercrime / fraude** : décisions condamnatoires, signalements ANSSI, etc. (croisement CTI / FININT).

**Contentieux fiscaux** : majorations, redressements publiés, contentieux administratif.

#### L’utilité opérationnelle

Pour l’analyste :

- Une **procédure collective récente** sur une contrepartie est un signal de risque ;
- Un **passif contentieux** chargé sur un dirigeant ou une société est un facteur de réputation ;
- Une **sanction AMF/ACPR** sur un acteur financier renseigne sur ses pratiques antérieures ;
- Une **condamnation pénale** publique antérieure (selon les juridictions) est un facteur clé.

L’analyste construit ainsi une **fiche réputationnelle** pour chaque acteur clé.

#### Méthode — workflow rapide

1. **France** :
- BODACC pour les procédures collectives.
- Légifrance / Doctrine pour les décisions publiées.
- Site AMF (commission des sanctions) et site ACPR.
- Site Direction Générale du Trésor pour les sanctions économiques.
- Presse et adverse media (chapitre 17) pour les affaires non encore jugées ou anonymisées.
1. **UK** :
- The Gazette pour insolvency.
- BAILII et Caselaw.uk pour décisions.
- FCA register pour sanctions.
1. **US** :
- PACER (federal court records, payant).
- SEC press releases.
- DOJ press releases.
- CFTC.
- State courts.
1. **International** : ICIJ Aleph, OCCRP archives (chapitre 18).

#### Mini-walkthrough

Sur le dirigeant Monsieur X (gestionnaire des SAS françaises liées à Haddad) :

- BODACC : 2 procédures collectives sur des sociétés antérieurement dirigées par M. X (liquidations 2018 et 2020).
- Légifrance : pas de décision publique le concernant directement.
- AMF/ACPR : non.
- Presse : un article de 2019 mentionne sa mise en cause dans une affaire de carrousel TVA (instruction en cours, présomption d’innocence).

Conclusion : profil avec **historique contentieux significatif**, à mentionner dans la fiche personne (chapitre 27) avec niveau de confiance approprié et précautions sur la présomption d’innocence.

#### Erreurs fréquentes

- **Confondre instruction et condamnation.** La présomption d’innocence est un principe — l’analyste ne diabolise pas un mis en examen.
- **Ignorer les anonymisations.** Beaucoup de décisions modernes sont anonymisées (initials des parties) — l’identification exige souvent croisement.
- **Surinterpréter une procédure collective.** Beaucoup d’entreprises échouent sans fraude.

#### Limites

Beaucoup de contentieux ne sont pas publics, notamment dans les juridictions opaques. Les contentieux fiscaux sont rarement publics dans le détail. La donnée est donc **indicative**, pas exhaustive.

#### Lien avec le fil rouge

> **CLEARFLOW — Historique contentieux**
> 
> Le profil contentieux du réseau Haddad : 2 procédures collectives passées sur des sociétés du même gestionnaire (Monsieur X), une enquête fiscale française antérieure sur Haddad lui-même (réglée par transaction fiscale, presse 2018), aucune sanction AMF/ACPR. Le profil n’est pas immaculé. Cela alimente la fiche personne et oriente la priorisation du dossier.

#### Points clés à retenir

- BODACC, Légifrance, AMF, ACPR, presse — sources clés en France.
- Présomption d’innocence à respecter dans tout livrable.
- Historique contentieux = facteur réputationnel, pas une preuve.
- Beaucoup d’angles morts (anonymisation, confidentialité, juridictions opaques).

-----

### Chapitre 17 — Presse, adverse media et SOCMINT financier

#### Objectif du chapitre

Maîtriser l’**OSINT non-structuré** appliqué à la finance : presse économique, presse d’investigation, adverse media en bases agrégées, et **SOCMINT financier** (signaux issus des réseaux sociaux et de la présence en ligne des dirigeants et entités).

#### Le concept

**Presse économique généraliste** : Le Monde, Les Échos, La Tribune, FT, WSJ, Reuters, Bloomberg, Handelsblatt, Frankfurter Allgemeine, Financial Times Italia, El País Negocios, etc. Sources de fond, articles fouillés, dossiers thématiques, archives accessibles via abonnement institutionnel.

**Presse d’investigation** : Mediapart, Investigate Europe, Disclose, Le Canard Enchaîné, OpenDemocracy, OCCRP, ICIJ, ProPublica, The Guardian Investigations, Süddeutsche Zeitung Investigations, Reflets.info. Volume plus restreint mais profondeur d’enquête souvent supérieure.

**Bases d’agrégation professionnelles** : Factiva (Dow Jones), LexisNexis, Nexis Newsdesk, Dow Jones Risk & Compliance, Factiva Risk & Compliance — chapitre 51. Couvrent des milliers de titres mondiaux avec recherche en texte intégral.

**Bases adverse media gratuites ou freemium** : OpenSanctions (qui agrège PEP, sanctions, et adverse media), Aleph (ICIJ), ICIJ databases.

**Annuaires officiels et registres complémentaires** : registre des armes, registre des bateaux, registres aéronautiques (FAA, EASA), pour les actifs très visibles.

**SOCMINT financier** :

- **LinkedIn** : signal de carrière, parcours professionnel, trajectoire, fonctions actuelles et passées, employeurs, réseau visible. Utile pour profiler un dirigeant, identifier des liens entre personnes, repérer des changements d’employeur (passage à une société sous enquête).
- **Réseaux sociaux personnels** (Instagram, Facebook, X/Twitter, TikTok) : signaux de train de vie (voyages, biens, événements), réseau d’amis et de relations, géolocalisation visible (chapitre 39).
- **Blogs et sites professionnels personnels** : occasionnellement, des dirigeants laissent transparaître leurs activités, leurs projets, leurs partenaires.
- **Sites des sociétés cibles** : organisation, équipes, filiales, actualités, partenaires commerciaux affichés — souvent une source plus riche qu’attendue.
- **Annonces publicitaires et événements professionnels** : participations à salons, conférences, prises de parole.
- **Photographies d’événements publics** : croisements visuels (qui est avec qui, où, quand).

#### L’utilité opérationnelle

Trois usages majeurs dans une enquête FININT :

1. **Adverse media** : qualification du risque réputationnel d’une personne ou d’une entité — affaires antérieures, associations problématiques, mises en cause publiques.
1. **Profilage humain** (SOCMINT) : qui est cette personne au-delà de sa fiche registre — formation, parcours, réseau, train de vie, signaux de cohérence ou d’incohérence.
1. **Recoupement OSINT général** : croisement avec d’autres sources (presse d’un côté, marchés publics de l’autre, leak d’une troisième) pour bâtir un faisceau d’éléments solide.

#### Méthode — workflow presse + SOCMINT

**Presse / adverse media** :

1. **Recherche par nom** dans les agrégateurs. Tester orthographes, translittérations, variantes.
1. **Recherche par société** — actualités, contentieux, opérations corporate.
1. **Recherche thématique** — secteur d’activité + termes typologiques (« blanchiment », « fraude », « conflit d’intérêts », « offshore », etc.).
1. **Tri qualitatif** : presse de référence vs presse moins fiable. Agrégation des dates, recoupement entre titres.
1. **Archivage** des articles consultés (capture, hash si critique).

**SOCMINT financier (LinkedIn et réseaux pro)** :

1. **Identification précise** de la personne (cf. chapitre 19 — homonymie). Profil LinkedIn = un parcours complet possible.
1. **Cartographie des employeurs** : trajectoire historique, durée de chaque fonction, employeur actuel.
1. **Réseau visible** : connexions notables, recommandations.
1. **Cohérence / incohérence** : un dirigeant déclaré d’un groupe à 50 M€ qui sur LinkedIn affiche 4 ans d’expérience junior dans une PME locale = signal de prête-nom probable.
1. **Pour chaque profil consulté** : capture horodatée, archivage. Les profils LinkedIn changent fréquemment.

**SOCMINT financier (réseaux personnels)** :

1. **Présence proportionnée** : un dirigeant officiel discret qui affiche un train de vie démonstratif sur Instagram = source de signaux patrimoniaux.
1. **Géolocalisations** : voyages, présence dans certaines villes, séjours à l’étranger — recoupement avec mouvements financiers.
1. **Réseau visible** : qui aime, commente, est tagué — cartographie des relations personnelles.
1. **Limites RGPD et déontologie** : la consultation est légitime quand l’objet est public ; pas de phishing, pas de faux profils, pas d’intrusion.

#### Mini-walkthrough — adverse media sur Karim Haddad

- Factiva (sources françaises et internationales) : 14 articles depuis 2018. Mention dans une transaction fiscale française (2018, sans poursuite pénale), présence dans un dossier d’export contesté en 2021 (article Le Monde), contributions à une fondation philanthropique libanaise (presse libanaise, 2022-2023).
- Mediapart : un article de 2023 sur des allégations de favoritisme pour des marchés en Côte d’Ivoire (sans nommer Haddad explicitement, mais avec des détails recoupés par OSINT).
- OCCRP : pas d’article direct, mais mention d’une société liée dans un dossier régional.
- LinkedIn : profil officiel Haddad, parcours déclaré 1995-aujourd’hui dans le négoce, actuellement « Chairman » de plusieurs entités. Cohérence avec l’image publique.
- Instagram : présence modérée, voyages réguliers (Beyrouth, Dubaï, Genève, Paris), événements professionnels visibles.
- Recoupement : profil global cohérent avec un homme d’affaires international actif. Aucune affaire judiciaire majeure publiquement connue. Adverse media présent mais à distance des qualifications fortes (présomption d’innocence pour les volets en cours).

#### Mini-walkthrough — SOCMINT sur Monsieur X (gérant SAS françaises)

- LinkedIn : profil minimal, mention d’une « activité de conseil aux entreprises ». Pas d’expérience préalable affichée en cohérence avec la gestion de 8 SAS commerciales actives.
- Recherche image : photo de profil utilisée également sur un site de cabinet de domiciliation (corrélation forte).
- Conclusion : profil compatible avec un **professionnel multi-mandats** au service d’un cabinet de domiciliation. Pas une preuve, mais un facteur ajouté à l’hypothèse de prête-nom (chapitre 25).

#### Erreurs fréquentes

- **Considérer la presse comme preuve.** La presse est une source d’information ; certains articles peuvent être imprécis, partiels ou orientés.
- **Surinterpréter un voyage.** Les voyages sur Instagram peuvent être un facteur d’analyse mais pas une qualification.
- **Ne pas archiver.** Les profils LinkedIn et les réseaux personnels changent — capture horodatée systématique.
- **Croiser des homonymes** (chapitre 19) : un Monsieur X présent sur LinkedIn n’est pas nécessairement le Monsieur X gestionnaire de la SAS. Vérifier date de naissance, parcours, photo.
- **Risquer le phishing OSINT** : créer un faux profil pour entrer en contact avec la cible viole les règles déontologiques et peut violer le droit (en France, manœuvres frauduleuses pour obtenir des données).

#### Limites

La presse couvre principalement les acteurs visibles (grandes affaires, personnages publics). Les acteurs « moyens » d’un dossier complexe ne sont souvent pas couverts. Le SOCMINT est limité aux personnes qui ont une présence en ligne ; un homme d’affaires de l’ancienne génération ou opérant dans une culture peu numérique peut être quasi-invisible.

Le RGPD limite, en pratique, certaines exploitations en France et en UE — la donnée doit être collectée pour une finalité légitime, et le traitement doit être conforme. En CRF, le cadre légal autorise un traitement étendu ; en cabinet privé, les limites sont plus strictes (chapitre 68).

#### Lien avec le fil rouge

> **CLEARFLOW — Le SOCMINT élargit le réseau**
> 
> Sur LinkedIn, Nassim identifie 5 collaborateurs proches déclarés de Haddad (employés ou anciens employés des sociétés du réseau). Sur Instagram, plusieurs photos de Haddad lors d’événements caritatifs au Liban montrent des personnalités politiques et économiques régionales. Une photo prise en 2023 lors d’un dîner à Genève montre Haddad avec un ancien dirigeant d’une banque privée suisse — la même banque dans laquelle un compte personnel apparaît dans les DS. Ce recoupement, *quasi-certain* à la confirmation visuelle (recherche image inverse + métadonnées), nourrit l’hypothèse d’un canal financier privilégié. Ce n’est pas une preuve, mais un faisceau qui oriente la coopération suisse.

#### Points clés à retenir

- Presse économique + presse d’investigation + bases d’agrégation = adverse media solide.
- SOCMINT financier : LinkedIn pour le pro, réseaux perso pour le train de vie et le réseau humain.
- Croiser systématiquement plusieurs sources avant qualification.
- Présomption d’innocence et cadre RGPD à respecter.
- Toujours archiver — les profils en ligne changent vite.

-----

### Chapitre 18 — Leaks financiers : ICIJ, OCCRP, Aleph, Panama/Pandora

#### Objectif du chapitre

Maîtriser l’usage des **leaks financiers majeurs** comme source d’enquête FININT. Les leaks ne sont pas la totalité du métier, mais ils sont devenus une source de référence pour les structures opaques offshores et certaines révélations sectorielles.

#### Le concept

Un **leak** est une fuite documentaire massive d’informations financières, généralement :

- issue d’un cabinet juridique, fiduciaire ou d’une institution financière ;
- obtenue par un lanceur d’alerte ou un hack ;
- transmise à un consortium de journalistes (ICIJ ou OCCRP étant les plus connus) qui en mène l’analyse coordonnée et la publication.

Ces leaks ont **changé** le paysage du FININT en rendant accessible (avec des limites — voir infra) une partie des structures historiquement opaques (BVI, Panama, Bahamas, etc.).

#### Les principaux leaks et bases

**Panama Papers (2016)** — fuite de 11,5 millions de documents du cabinet Mossack Fonseca (Panama). Origine : un lanceur d’alerte anonyme (« John Doe ») au journaliste allemand Bastian Obermayer (Süddeutsche Zeitung), partagé avec ICIJ. Conséquence : révélation massive de structures offshores liées à des PEP, des hommes d’affaires, des criminels organisés. La base [Offshore Leaks](https://offshoreleaks.icij.org/) de l’ICIJ regroupe les structures identifiées et est consultable publiquement par nom.

**Paradise Papers (2017)** — fuite du cabinet Appleby (Bermudes) et de divers fournisseurs. ICIJ. Inclus dans la base Offshore Leaks.

**Pandora Papers (2021)** — fuite combinée de 14 prestataires offshore. ICIJ. Près de 12 millions de documents. Particulièrement riche sur les UBO et les bénéficiaires de trusts. Inclus dans la base Offshore Leaks.

**FinCEN Files (2020)** — fuite de SAR (Suspicious Activity Reports) américains. Différent des autres leaks : il s’agit de signalements internes de banques au régulateur US. Coordonné par BuzzFeed et ICIJ. Couvre 2 trillions USD de transactions suspectes.

**Suisse Secrets (2022)** — fuite de comptes Credit Suisse, coordonnée par OCCRP et plusieurs journaux européens.

**Cyprus Confidential (2023)** — fuite portant sur des prestataires de services chypriotes, ICIJ.

**Russian Asset Tracker (2022+)** — base OCCRP sur les actifs des oligarques russes sous sanctions.

**OCCRP Aleph** — plateforme **agrégée** de l’OCCRP qui regroupe des leaks, registres ouverts, sanctions, et bases de données journalistiques. Devenue une référence pour les analystes, accessible via partenariat avec OCCRP. Recherche unifiée, très utile.

**Aleph (instance ICIJ)** — moteur de recherche sur l’écosystème ICIJ. Accès journalistique principalement.

**Smaller leaks** : Bahamas Leaks (2016), Lux Leaks (2014), Swiss Leaks (HSBC, 2015), Malta Files, Glencore Leak, etc.

#### L’utilité opérationnelle

Pour un analyste FININT, les leaks permettent :

1. **Identification de structures cachées** : une société BVI dont l’UBO n’est pas accessible en registre peut figurer dans Panama/Pandora avec ses bénéficiaires.
1. **Recoupement de réseaux** : les liens entre personnes via des trusts ou des fondations sont souvent visibles dans les documents leakés.
1. **Profilage de prestataires** : certains cabinets de domiciliation ou trust companies apparaissent récurremment dans des dossiers à risque.
1. **Documentation historique** : les leaks couvrent souvent des périodes anciennes — utile pour reconstituer l’historique d’un montage.

#### Méthode — workflow leaks

1. **Recherche par nom de personne** dans Offshore Leaks (ICIJ) — gratuit, public.
1. **Recherche par nom de société** dans Offshore Leaks.
1. **Recherche dans Aleph (OCCRP)** si accès — agrège plus largement.
1. **Recherche dans les archives journalistiques** publiées (les articles ICIJ/OCCRP sont publics avec une partie des sources).
1. **Vérification croisée** : un nom dans un leak n’est pas un fait avéré — c’est un document supposé authentique. La présence ne vaut pas culpabilité (la détention d’une société offshore peut être parfaitement légale).
1. **Documentation** : capture, référence à l’article ou à la base, date de consultation.

#### Mini-walkthrough — Pandora dans CLEARFLOW

- Recherche dans Offshore Leaks par « Karim Haddad » : 1 résultat — un trust chypriote enregistré en 2019, dont le settlor est nommé Karim Haddad, et dont les bénéficiaires incluent une SAS française et une LLC Delaware (toutes deux du réseau du dossier).
- Recherche par « OMEGA HOLDINGS » : 2 résultats — la société chypriote elle-même + une mention dans une entité liée à Beyrouth.
- Aleph (OCCRP) : recoupement avec un article OCCRP de 2023 sur les flux entre Liban et Afrique de l’Ouest, mentionnant un homme d’affaires correspondant à Haddad sans le nommer.
- Calibration : la présence dans Pandora est *quasi-certaine* (document authentique, attribution claire). L’usage du trust pour des fins illicites n’est pas démontré par le seul leak — il est *compatible* avec, et nécessite recoupement des flux et de l’activité.

#### Erreurs fréquentes

- **Présence dans un leak = culpabilité.** Non. La détention d’une structure offshore peut être parfaitement légale (planification successorale, protection patrimoniale légitime, résidence à l’étranger).
- **Leak = source primaire complète.** Les leaks sont des extraits limités à ce qu’a obtenu le lanceur d’alerte. Ils peuvent omettre des éléments cruciaux.
- **Leak = preuve admissible.** En cadre judiciaire, l’admissibilité dépend du droit national et de l’origine. Certaines décisions (CEDH, en particulier) admettent les preuves issues de leaks sous conditions, d’autres non.
- **Surinterpréter une similitude de nom.** Un Karim Haddad dans un leak peut être un homonyme — vérifier les autres champs (date de naissance, adresse, autres mandats).

#### Limites

Les leaks sont **datés** : ils reflètent un instant. Une société leakée en 2016 peut avoir été liquidée en 2018, ou son UBO peut avoir changé. Les leaks couvrent les juridictions dont les prestataires ont été leakés — d’autres juridictions restent dans l’ombre. L’accès complet aux bases (au-delà des recherches publiques) est généralement réservé à la presse partenaire.

#### Lien avec le fil rouge

> **CLEARFLOW — Le leak comme accélérateur**
> 
> Sans le hit Pandora, l’identification de Haddad comme settlor du trust chypriote aurait demandé une coopération via Egmont avec Mokas — délai de plusieurs semaines, sans garantie. Le leak fournit *gratuitement* en quelques minutes une information dont la valeur opérationnelle est élevée. Nassim documente le hit et le qualifie *probable* à *quasi-certain* selon les recoupements. Cette information sera l’un des **piliers** de l’hypothèse centrale du dossier (chapitre 64).

#### Points clés à retenir

- Panama, Paradise, Pandora, FinCEN Files, Suisse Secrets : leaks majeurs.
- Offshore Leaks (ICIJ) et Aleph (OCCRP) : bases consultables.
- Présence dans un leak ≠ culpabilité ; mais signal de structure offshore avérée.
- Les leaks accélèrent considérablement les enquêtes sur les juridictions opaques.
- Vérification croisée et calibration de la confiance impératives.

-----

## PARTIE IV — PERSONNES, SOCIÉTÉS ET CONTRÔLE

*Huit chapitres pour identifier précisément les acteurs (personnes physiques, sociétés) et comprendre les structures de contrôle (formes juridiques, mandataires, actionnaires, UBO, holdings, trusts, sociétés écrans). C’est la grammaire fine du FININT : sans elle, les flux observés au chapitre suivant restent illisibles.*

-----

### Chapitre 19 — Identifier une personne physique sans se tromper d’homonyme

#### Objectif du chapitre

Maîtriser la **discipline d’identification** d’une personne physique. C’est l’erreur la plus courante et la plus dommageable en FININT : attribuer à une cible des éléments qui concernent en réalité un homonyme. Cette erreur peut détruire la crédibilité d’un livrable et causer un préjudice réel à un tiers innocent.

#### Le concept

L’**homonymie** est une réalité statistique. Pour des prénoms et noms courants, on compte des centaines, voire des milliers d’homonymes dans un pays. Pour des noms moins courants, ce risque baisse mais n’est jamais nul. L’identification rigoureuse repose sur la **convergence** de plusieurs attributs.

#### Les attributs d’identification

L’analyste cherche à stabiliser autant d’attributs que possible parmi :

- **Nom et prénoms** complets, dans l’ordre, avec orthographe précise.
- **Date de naissance** (jour, mois, année).
- **Lieu de naissance** (commune, pays).
- **Nationalité(s)** — peut être multiple.
- **Adresse(s) connue(s)** — actuelle, antérieures.
- **Numéro d’identification fiscale** (numéro fiscal de référence en France, NIF, NIN, etc.) — rarement accessible en OSINT, mais central en sources fermées.
- **Numéro de sécurité sociale** — non accessible en OSINT.
- **Numéro de passeport** — non accessible en OSINT sauf cas particuliers (leaks).
- **Photographie** — recoupement visuel.
- **Profil professionnel public** (LinkedIn, presse) — cohérence biographique.
- **Réseau familial** : conjoint, parents, frères et sœurs, enfants — souvent identifiable via presse ou réseaux sociaux.
- **Réseau professionnel** : associés, employeurs, mandats parallèles.

Plus le nombre d’attributs convergents, plus l’identification est solide. La règle pratique :

- 2 attributs forts (nom complet + date de naissance, ou nom + photo) = identification *possible*.
- 3-4 attributs convergents = identification *probable*.
- 5+ attributs convergents, dont des recoupements indépendants = identification *quasi-certaine*.

#### Les pièges classiques

**Translittération** : un même nom peut s’écrire de plusieurs façons selon la langue source. « Mohamed » vs « Mohammad » vs « Muhammad ». « Иванов » → « Ivanov », « Ivanoff », « Iwanow » selon les conventions. L’analyste teste systématiquement les variantes.

**Articles et particules** : « Van der Berg », « De la Cruz », « Al-Hadi » — selon les sources, certaines parties peuvent être omises ou attachées. « Karim Haddad » peut apparaître comme « Haddad, Karim », « Karim El-Haddad », « K. Haddad », etc.

**Initiales** : les comptes annuels et certains documents officiels n’utilisent parfois que l’initiale du prénom. Source d’ambiguïté.

**Diminutifs** : « William » ↔ « Bill », « James » ↔ « Jim », « Catherine » ↔ « Cathy » ou « Kate » — fréquents dans le monde anglophone.

**Changement de nom** : mariage, divorce, naturalisation, raisons personnelles. Une personne née sous un nom peut apparaître sous un autre dans certains documents.

**Confusion père/fils** : Karim Haddad Senior vs Karim Haddad Junior — même nom, attributs différents. Toujours vérifier la date de naissance.

#### Méthode — protocole d’identification en 6 étapes

1. **Collecter les attributs disponibles** : nom complet, date de naissance, lieu, nationalité, profession.
1. **Tester les variantes** : translittérations, articles, initiales, ordre.
1. **Croiser avec les sources** : registres (mandats déclarés), presse, leaks, réseaux sociaux.
1. **Identifier les homonymes potentiels** : combien de personnes avec ces attributs ?
1. **Valider par convergence** : la personne identifiée a-t-elle bien tous les attributs attendus ?
1. **Calibrer la confiance** : sur la base du nombre et de la qualité des recoupements.

#### Mini-walkthrough

Cible : « Karim Haddad », mentionné dans une DS comme dirigeant suspect.

- Recherche initiale : « Karim Haddad » → des centaines de résultats Google, plusieurs profils LinkedIn, plusieurs entrées registre dans plusieurs pays.
- Attributs initiaux fournis par la DS : âge approximatif (« la cinquantaine »), nationalité (franco-libanais), domaine d’activité (négoce et import-export).
- Recherche affinée : « Karim Haddad » + « négoce » + « Liban » ou « France ».
- 3 candidats émergent :
  - Karim Haddad A, né 1965, ingénieur télécoms à Beyrouth → exclu (profession différente).
  - Karim Haddad B, né 1968, négociant franco-libanais, dirigeant déclaré de plusieurs sociétés en France et au Liban → match probable.
  - Karim Haddad C, né 1981, journaliste basé à Paris → exclu (profession différente).
- Recoupement complémentaire : RBE des SAS françaises identifie un UBO Karim Haddad, né 1968 à Beyrouth, nationalité française. Convergence : nom + date + lieu + nationalité + profession + mandats → identification *quasi-certaine*.

#### Erreurs fréquentes

- **Conclure sur 2 attributs faibles** (nom + secteur) — risque homonyme élevé.
- **Ne pas tester les variantes orthographiques** — manque la cible si elle apparaît sous variante.
- **Ignorer les changements de nom** — femme mariée, naturalisation, etc.
- **Confondre père / fils** — toujours vérifier l’année de naissance précise.
- **Attribuer une photo sans recoupement** — un nom commun peut avoir plusieurs photos sur Internet, certaines non attribuables.

#### Limites

L’identification peut rester **indéterminable** dans certains cas : très peu d’attributs accessibles (personne discrète, juridiction opaque), risque homonyme élevé (nom très courant), absence de photo ou de date de naissance. L’analyste documente explicitement la limite : *« Identification de M. K. Haddad établie à un niveau de confiance probable. Une confirmation quasi-certaine nécessiterait l’accès au numéro fiscal ou à un document d’identité, hors périmètre des sources ouvertes mobilisées. »*

#### Lien avec le fil rouge

> **CLEARFLOW — Stabiliser Karim Haddad**
> 
> Avant toute autre analyse, Nassim consacre 2 heures à stabiliser l’identification : nom complet (Karim Élie Haddad), date de naissance (1968), lieux (Beyrouth puis Paris), nationalités (libanaise et française), parcours professionnel (négoce et import-export depuis 1995). Photo officielle récupérée via LinkedIn et site d’une chambre de commerce franco-libanaise. Cette stabilisation initiale conditionne tout le reste : sans elle, les attributions ultérieures seraient suspectes.

#### Points clés à retenir

- L’identification rigoureuse repose sur la **convergence** de plusieurs attributs.
- Pièges : translittération, particules, initiales, diminutifs, changements de nom, père/fils.
- 5+ attributs convergents = quasi-certain ; 2 attributs faibles = à approfondir.
- Documenter explicitement les limites quand l’identification reste incomplète.

-----

### Chapitre 20 — Identifier une société et ses variantes internationales

#### Objectif du chapitre

Maîtriser l’identification d’une **personne morale** : variantes orthographiques, sociétés de même nom dans plusieurs juridictions, sociétés homonymes, identifiants officiels permettant de stabiliser la référence.

#### Le concept

L’identification d’une société repose essentiellement sur son **identifiant officiel** dans la juridiction de son siège :

- **France** : SIREN (9 chiffres) ou SIRET (14 chiffres = SIREN + identifiant établissement).
- **UE** : EUID (European Unique Identifier) émergent ; chaque pays a son identifiant national (Numéro KvK aux Pays-Bas, Numéro d’entreprise belge, etc.).
- **UK** : Company Number (8 caractères : 2 lettres + 6 chiffres pour Scottish, sinon 8 chiffres).
- **US** : EIN (Employer Identification Number) au niveau fédéral, mais pas universel. Plus utile : numéro d’enregistrement de l’État (Delaware, etc.).
- **LEI** (Legal Entity Identifier) : code ISO 17442 à 20 caractères, attribué aux entités opérant sur les marchés financiers. Base mondiale [GLEIF](https://www.gleif.org/). Particulièrement utile pour les institutions financières et les contreparties cotées.
- **DUNS Number** : identifiant Dun & Bradstreet, utilisé largement dans la commande publique et l’évaluation de risque.
- **VAT Number** : numéro de TVA intracommunautaire (UE), vérifiable via VIES.

L’identifiant officiel est **clé** : il lève l’ambiguïté entre sociétés de même nom dans plusieurs juridictions.

#### Les pièges classiques

**Sociétés homonymes inter-juridictions** : « NEXUS TRADING » peut exister en France, en UK, à Chypre et à Dubaï — entités juridiques distinctes, parfois liées, parfois non. Toujours préciser la juridiction et l’identifiant.

**Variantes orthographiques** : « NEXUS TRADING SAS » vs « Nexus Trading » vs « N. Trading SAS » — le registre officiel a une dénomination exacte qui prévaut.

**Sociétés rebaptisées** : une société peut changer de dénomination plusieurs fois. L’identifiant SIREN/Company Number reste, mais la recherche par nom historique peut manquer la cible.

**Sociétés fusionnées / absorbées** : une société absorbée disparaît juridiquement ; son identifiant aussi. Continuité économique parfois trompeuse.

**Groupes vs filiales** : « TOTAL » peut désigner TotalEnergies SE, TotalEnergies Marketing France SAS, TotalEnergies E&P, etc. Préciser l’entité concernée.

**Marques vs sociétés** : une marque commerciale (« Apple ») peut correspondre à plusieurs sociétés juridiques (Apple Inc., Apple Operations International, Apple Sales International, etc.).

#### Méthode — protocole d’identification

1. **Recueillir tous les attributs** : dénomination, juridiction (pays + ville si possible), secteur d’activité, dirigeants connus, adresse.
1. **Recherche dans le registre national** (chapitres 11-12).
1. **Vérifier l’identifiant officiel** : SIREN / Company Number / autre.
1. **Vérifier l’historique** : changements de dénomination, fusions, transferts de siège.
1. **Identifier les entités liées** : filiales, sociétés sœurs, holding mère.
1. **Documenter** : fiche identification précise (annexe D).

#### Mini-walkthrough

Cible : « NEXUS HOLDINGS », mentionnée dans une DS comme contrepartie d’un flux de 1,2 M€ provenant de Chypre.

- Recherche initiale : Pappers, Companies House, OpenCorporates → 14 résultats sociétés contenant « Nexus » dans le nom, dans 9 juridictions.
- Affinage avec le contexte (Chypre + 2019 + dirigeant connu) : 2 candidats.
  - NEXUS HOLDINGS LTD (Chypre, registered 2019, directeur M. Y) → match probable.
  - NEXUS HOLDINGS LIMITED (BVI, registered 2010, directeurs trustees professionnels) → exclu (différents directeurs et antériorité).
- Identifiant officiel : Cyprus Company Registration Number HE-XXXXXX.
- Historique : pas de changement de dénomination depuis création.
- Entités liées : la société est associée majoritaire d’une SAS française et d’une LLC US — graphe à étendre.

#### Erreurs fréquentes

- **Confondre des sociétés de même nom dans des juridictions différentes** — c’est l’erreur n°1 dans les enquêtes multi-juridictionnelles.
- **Oublier de tester les translittérations** — « Sergei » vs « Sergey », « Loutchnikov » vs « Luchnikov ».
- **Confondre groupe et filiale** — un dossier sur « TOTAL » sans préciser l’entité juridique est ininterprétable.
- **Confondre dénomination commerciale et dénomination sociale** — la marque ne suffit pas.

#### Limites

Dans les juridictions opaques (BVI, Cayman, Panama, etc.), les recherches par nom peuvent ne pas être publiques. L’analyste s’appuie alors sur leaks (chapitre 18), agrégateurs et coopération internationale.

#### Lien avec le fil rouge

> **CLEARFLOW — Stabiliser les 14 entités**
> 
> Sur les 14 sociétés du réseau Haddad mentionnées dans les DS, Nassim stabilise chaque identification par juridiction et identifiant officiel. Une particularité émerge : 3 sociétés portent un nom proche (« Nexus Trading », « Nexus Holdings », « Nexus International ») mais sont dans 3 juridictions différentes (France, Chypre, Émirats). L’analyse confirme qu’elles sont liées (sociétés affiliées contrôlées par le même réseau), mais ce sont des entités juridiques distinctes — distinction à maintenir dans tout livrable pour éviter les amalgames.

#### Points clés à retenir

- L’identifiant officiel (SIREN, Company Number, LEI) prime sur le nom.
- Tester systématiquement les variantes orthographiques et les translittérations.
- Distinguer sociétés homonymes, groupes, filiales et marques.
- Documenter l’historique (changements de dénomination, fusions).

-----

### Chapitre 21 — Formes juridiques comparées

#### Objectif du chapitre

Connaître les **formes juridiques principales** rencontrées en FININT, leurs caractéristiques (responsabilité, transparence, capital, gouvernance), et leur signification dans une cartographie. La forme juridique d’une entité informe sur sa flexibilité, son opacité potentielle et ses obligations.

#### Le concept

Les formes juridiques varient considérablement par juridiction. Quelques familles structurantes.

**Sociétés de capitaux** : responsabilité limitée au capital. La grande majorité des entreprises modernes.

- **SAS / SASU** (France) — société par actions simplifiée (unipersonnelle si un seul associé). Flexible, gouvernance librement définie dans les statuts. Présidence par personne physique ou morale.
- **SARL / EURL** (France) — société à responsabilité limitée. Plus encadrée que la SAS. Gérée par un ou plusieurs gérants.
- **SA** (France) — société anonyme. Plus lourde (CAC obligatoire, conseil d’administration ou directoire + conseil de surveillance), capital minimum 37 000 €. Pour les grandes entreprises ou les sociétés cotées.
- **SCA** (France) — société en commandite par actions. Rare mais utilisée dans certains schémas familiaux ou patrimoniaux.
- **GmbH** (Allemagne) — équivalent SARL allemand. Très commune.
- **AG** (Allemagne) — équivalent SA. Pour les grandes entreprises et les cotées.
- **S.r.l.** (Italie) — équivalent SARL.
- **S.p.A.** (Italie) — équivalent SA.
- **S.L.** (Espagne) — équivalent SARL.
- **S.A.** (Espagne) — équivalent SA.
- **B.V.** (Pays-Bas) — Besloten Vennootschap, équivalent SARL. Très utilisée dans les holdings internationaux.
- **N.V.** (Pays-Bas, Belgique) — Naamloze Vennootschap, équivalent SA.
- **Ltd / Limited** (UK, Irlande) — équivalent SARL ; obligation de publier comptes et PSC.
- **PLC** (UK) — Public Limited Company, équivalent SA cotée.
- **LLC** (US, plusieurs États) — Limited Liability Company. Hybride entre société et partnership ; flexibilité fiscale ; très utilisée dans les structures opaques (Delaware, Wyoming, Nevada).
- **Inc. / Corporation** (US) — équivalent SA.
- **AG** (Suisse) — équivalent SA.
- **GmbH** (Suisse) — équivalent SARL.

**Sociétés de personnes** : responsabilité illimitée (généralement).

- **SNC** (France) — société en nom collectif. Associés indéfiniment et solidairement responsables.
- **Société civile** (France) — civile par défaut, fréquente pour gestion patrimoniale (SCI immobilière).
- **Partnership** (UK, US) — équivalent SNC.
- **LLP** (UK, US) — Limited Liability Partnership, hybride. UK : doit publier comme une Limited.

**Structures de holding et particulières** :

- **Soparfi** (Luxembourg) — Société de Participation Financière. Régime fiscal favorable pour les holdings.
- **SCSp** (Luxembourg) — Société en Commandite Spéciale, structure flexible pour les fonds.
- **IBC** (International Business Company) — typique des juridictions offshore caribéennes.
- **LP / Limited Partnership** (Scottish LP, Delaware LP, etc.) — historiquement opaque, désormais sous PSC au UK.

**Trusts et fondations** (chapitre 25, en détail) :

- **Trust** (Common law : UK, US, BVI, Cayman, Bahamas, etc.) — relation juridique entre settlor, trustee, bénéficiaires.
- **Fondation** (droit continental : Liechtenstein Stiftung, Panamanian Foundation, etc.) — entité juridique distincte du fondateur.

**Associations et structures sans but lucratif** :

- **Association loi 1901** (France).
- **Charity** (UK).
- **501(c)(3)** (US).

#### L’utilité opérationnelle

Pour l’analyste :

- **La forme oriente sur la transparence attendue.** Une SAS française publie ses comptes (au-delà des seuils) ; une LLC Delaware ne publie rien. Un trust BVI n’est pas une entité juridique publique.
- **La forme oriente sur la gouvernance.** Une SA a un conseil d’administration ou directoire + conseil de surveillance ; une SAS peut être pilotée par un président unique.
- **La forme oriente sur les obligations LCB-FT.** Certaines formes sont des assujettis (notaires, avocats sous certaines conditions, agents immobiliers), d’autres non.
- **La forme oriente sur les schémas typiques.** SCI pour la détention immobilière. SOPARFI pour les holdings. LLC Delaware pour les structures opaques. Trust pour la séparation patrimoniale.

Une cartographie de réseau qui ne distingue pas les formes juridiques est lacunaire.

#### Méthode — lecture d’une cartographie par forme

Sur un graphe avec 12 entités, l’analyste annote chaque nœud :

```
ENTITY 1 — SAS française, capital 10 K€, dirigeant unique
ENTITY 2 — Ltd UK, PSC déclaré, comptes publiés (micro)
ENTITY 3 — LLC Delaware, opacité maximale
ENTITY 4 — IBC BVI, UBO accessible aux autorités locales
ENTITY 5 — SOPARFI Luxembourg, holding intermédiaire
ENTITY 6 — Trust BVI, settlor identifié dans Pandora
ENTITY 7 — Stiftung Liechtenstein, fondateur dans Pandora
ENTITY 8 — Société libanaise, opaque
```

Cette annotation simple oriente immédiatement la stratégie d’investigation : où sont les zones d’opacité, où sont les leviers (PSC UK), où la coopération internationale est requise.

#### Mini-walkthrough — formes du réseau Haddad

- 4 SAS françaises : comptes publics, dirigeants visibles, UBO RBE (accès assujettis et autorités).
- 2 Limited UK : PSC public, comptes publics.
- 1 LLC Delaware : opacité forte, UBO inaccessible (CTA contesté).
- 1 SOPARFI Luxembourg : comptes publiés au RCS, mais structure de holding intermédiaire.
- 1 Ltd Chypre : registres limités, UBO non-public (post-CJUE).
- 1 IBC BVI : pas de comptes publics, UBO accessible aux autorités locales.
- 1 trust chypriote (identifié via Pandora) : structure non publique, settlor connu via leak.
- 2 sociétés émiraties (free zone) : registres limités.
- 1 société libanaise : informations limitées.

Une lecture : le réseau combine des **entités visibles** (UK et France, pour l’opérationnel et l’apparence légitime), des **véhicules opaques** (LLC US, IBC BVI, trust CY), et des **holdings intermédiaires** (SOPARFI Luxembourg) qui structurent le contrôle. Schéma classique d’**ingénierie offshore** sans préjuger de sa légalité.

#### Erreurs fréquentes

- **Considérer toutes les formes comme équivalentes.** Une LLC Delaware ≠ une SAS française ≠ un trust BVI. Les régimes et les transparences diffèrent radicalement.
- **Confondre forme et fonction.** Une « société de holding » peut être SARL, SA, SAS, SOPARFI, LLC, BV, etc. La forme dit la structure, pas la fonction.
- **Ignorer les particularités locales** : LP écossais, SCSp luxembourgeoise, fondation panaméenne — chacune a des spécificités à connaître pour comprendre la logique du montage.

#### Limites

La connaissance fine des formes juridiques de toutes les juridictions du monde dépasse les capacités d’un analyste. L’objectif est de connaître les formes courantes et d’identifier les formes spécifiques quand elles apparaissent (recherche à la demande). Les juristes spécialisés sont consultés quand un montage particulier exige une analyse poussée.

#### Lien avec le fil rouge

> **CLEARFLOW — Lecture juridique du réseau**
> 
> Nassim produit une fiche par entité avec sa forme juridique et ses implications. Cette annotation lui permet, en consolidation, d’expliquer dans la note finale : *« Le réseau s’appuie sur 4 SAS françaises (front opérationnel apparent), 2 Limited UK (présence visible mais activité réelle douteuse), 1 LLC Delaware (opacité), 1 SOPARFI luxembourgeoise (holding intermédiaire), 1 société chypriote contrôlée par un trust (structure de contrôle ultime probable). Le montage est typique d’une architecture multi-juridictionnelle combinant légitimité de façade et opacité de contrôle. »*

#### Points clés à retenir

- Formes courantes UE : SAS, SARL, SA, GmbH, BV, Ltd, SOPARFI.
- Formes opaques notables : LLC Delaware, IBC BVI/Cayman, fondations Liechtenstein, trusts.
- La forme oriente la transparence, la gouvernance, les obligations.
- Un graphe de réseau bien annoté en formes informe immédiatement la stratégie d’investigation.

-----

### Chapitre 22 — Dirigeants, mandataires et administrateurs

#### Objectif du chapitre

Cartographier les **personnes physiques exerçant des fonctions officielles** dans une entité : présidents, gérants, directeurs généraux, administrateurs, membres du conseil de surveillance, secrétaires (UK), commissaires aux comptes, fondés de pouvoir. Identifier les profils anormaux et les patterns suspects.

#### Le concept

Toute entité juridique a au moins une **personne physique** investie d’un mandat officiel — c’est le minimum pour qu’elle puisse être représentée. Ces mandats sont déclarés au registre et accessibles publiquement dans la plupart des juridictions.

**Mandats principaux selon les formes** :

- SAS française : président (et éventuellement DG, directeurs adjoints).
- SARL française : gérant(s).
- SA française : conseil d’administration (membres + président) et directeur général, OU directoire + conseil de surveillance.
- Limited UK : directors et secretary.
- GmbH allemande : Geschäftsführer.
- AG allemande : Vorstand (directoire) et Aufsichtsrat (conseil de surveillance).
- LLC américaine : member(s) ou manager(s).
- Trust : trustee(s), settlor, protecteur(s).

**Mandataires accessoires** : commissaires aux comptes (sociétés au-delà des seuils), fondés de pouvoir (pour certaines opérations), liquidateurs (en cas de procédure).

#### L’utilité opérationnelle

L’analyse des mandataires permet :

1. **Identifier les acteurs déclarés** — qui répond officiellement de l’entité.
1. **Détecter les profils anormaux** — multi-mandats, retraités âgés, jeunes sans expérience.
1. **Cartographier les liens entre entités** — un même dirigeant pour plusieurs entités = lien fort de contrôle ou de coordination.
1. **Identifier les corporate service providers** — cabinets qui fournissent des mandataires professionnels (« nominee directors ») dans le cadre d’une opacification.

#### Méthode — analyse des mandataires

1. **Récupérer la liste des mandataires actuels et passés** (registre).
1. **Profiler chacun** : date d’entrée en fonction, durée, autres mandats déclarés (recherche par nom), profession, profil LinkedIn.
1. **Repérer les patterns** :
- Mandataire avec 20+ mandats actifs dans des sociétés non liées sectoriellement.
- Mandataire âgé sans expérience apparente du secteur.
- Mandataire à l’adresse identique à la société.
- Mandataire d’une société de domiciliation connue.
- Rotation rapide des mandataires (changements multiples en peu de temps).
1. **Croiser avec sanctions, PEP, adverse media** (chapitre 17).

#### Mini-walkthrough — analyse des mandataires CLEARFLOW

**Sur les 4 SAS françaises** :

- 2 SAS : Monsieur X comme président, en fonction depuis la création (14 à 22 mois).
- 1 SAS : Mme Z comme présidente, en fonction depuis 11 mois.
- 1 SAS : société de domiciliation comme directeur (rare en France — admis pour certaines formes).

Profilage de Monsieur X :

- LinkedIn minimal, « activité de conseil aux entreprises ».
- 8 mandats actifs identifiés dans Pappers (croisement par nom + date de naissance).
- Tous les mandats dans des SAS de commerce de gros, créées 2022-2024.
- Toutes domiciliées à la même adresse (cabinet de domiciliation).
- Aucune expérience préalable visible dans le négoce.
- 2 procédures collectives sur des sociétés antérieurement gérées (chapitre 16).

→ Profil compatible avec un **gestionnaire multi-mandats au service d’un cabinet de domiciliation**. Niveau de confiance *probable* sur la qualification prête-nom.

Profilage de Mme Z :

- LinkedIn présent, parcours d’agente commerciale dans un autre secteur (parfumerie).
- 1 seul mandat actuel.
- Adresse personnelle distincte de la société.

→ Profil moins suspect, mais à recouper avec relation potentielle à Haddad (réseau personnel).

**Sur les 2 Limited UK** :

- Director déclaré : un Libanais résidant à Dubaï, M. Y.
- PSC : même M. Y (déclaré comme exerçant contrôle significatif via droits de vote).
- Profilage : LinkedIn affichant un parcours dans le négoce libanais, lien visible avec Haddad (employé de longue date selon presse).

→ Profil compatible avec un **collaborateur de confiance** plutôt qu’un prête-nom anonyme. La qualification UBO reste à confirmer (un collaborateur peut être lui-même un prête-nom).

#### Erreurs fréquentes

- **Conclure « prête-nom » sans recoupement.** Un mandataire avec plusieurs mandats peut être un gestionnaire légitime (cabinet d’expertise comptable, par exemple).
- **Ignorer les commissaires aux comptes.** Le choix d’un CAC reconnu vs un CAC inconnu peut être un signal.
- **Ne pas chercher les mandats antérieurs.** Les anciennes fonctions racontent l’histoire de la personne.

#### Limites

Les registres sont déclaratifs. Un mandataire peut être nominalement en fonction sans exercer réellement le contrôle. Inversement, le contrôle réel peut être exercé par une personne sans mandat déclaré (chapitre 23 sur le contrôle indirect).

#### Lien avec le fil rouge

> **CLEARFLOW — Cartographie des mandataires**
> 
> Nassim produit un tableau croisé : 12 personnes physiques exercent des mandats dans les 14 entités du réseau. 5 de ces personnes ont 3+ mandats, dont Monsieur X (gestionnaire français multi-mandats, profil prête-nom probable) et M. Y (libanais à Dubaï, collaborateur de confiance probable). Aucune n’est Karim Haddad lui-même : il **n’apparaît dans aucun mandat officiel** des entités françaises et UK du dossier. Ce constat est important — cela conforte l’hypothèse d’un contrôle indirect (chapitre 23) plutôt que d’une gestion directe.

#### Points clés à retenir

- Tous les mandataires des entités cibles sont à profiler.
- Patterns suspects : multi-mandats, profils inadaptés, adresses partagées, rotation rapide.
- Mandataire déclaré ≠ contrôle réel — vérifier par croisement avec UBO.
- Une cartographie « mandataires × entités » est l’un des livrables les plus utiles d’une enquête FININT.

-----

### Chapitre 23 — Actionnaires, UBO et contrôle indirect

#### Objectif du chapitre

Comprendre la **chaîne du contrôle** : actionnaires immédiats, sociétés interposées, UBO de dernier niveau, mécanismes de contrôle indirect au-delà du capital (conventions, usufruit, options, conventions de vote).

#### Le concept

Trois niveaux à distinguer :

1. **Actionnariat / association** : qui détient les titres ou les parts au capital de l’entité — souvent une autre société, parfois une personne physique directement.
1. **UBO** : qui contrôle ultimement (personne physique). Peut être direct (actionnaire personne physique) ou indirect (via chaîne de sociétés, trusts, conventions).
1. **Contrôle effectif** : qui décide réellement — peut être différent de l’UBO de droit. Par exemple, un actionnaire majoritaire qui a délégué le contrôle par convention à un tiers.

**Mécanismes de contrôle indirect** :

- **Chaîne de holdings** : société A détenue par société B, elle-même détenue par société C, elle-même détenue par M. X. Le contrôle est traçable mais demande à remonter la chaîne.
- **Trusts** : la société est détenue par un trust. Le settlor a apporté les actifs ; le trustee les gère ; les bénéficiaires en jouissent. Le contrôle peut être chez le settlor (trust révocable), chez le trustee (trust irrévocable), ou ailleurs (protecteur).
- **Fondations** : entité juridique qui détient les titres. Le fondateur a apporté ; le conseil de fondation gère ; les bénéficiaires en jouissent.
- **Nominees** : prête-noms officiels (déclarés comme tels en common law).
- **Conventions de vote** : un actionnaire minoritaire peut contrôler par convention si la majorité accepte de voter selon ses instructions.
- **Usufruit** : démembrement de propriété. Le nu-propriétaire détient le capital ; l’usufruitier exerce les droits.
- **Options et promesses de vente** : un investisseur peut avoir une option d’achat lui permettant de prendre le contrôle à tout moment.
- **Pactes d’actionnaires** : conventions privées qui modulent les droits formels.
- **Démembrement entre associés** : un dirigeant détient peu mais a une convention lui donnant un pouvoir étendu.

#### L’utilité opérationnelle

L’analyste cherche à répondre à : **qui contrôle réellement cette entité, et avec quel niveau de confiance ?**

Cela conditionne :

- L’identification du véritable décideur ;
- La compréhension de la stratégie économique ;
- L’attribution des responsabilités ;
- Le ciblage des coopérations et réquisitions.

#### Méthode — remonter la chaîne

1. **Identifier les associés immédiats** (registre, statuts).
1. **Pour chaque associé personne morale, remonter** : qui sont ses associés ? (récursion).
1. **Arriver à une personne physique** OU **arriver à une structure opaque** (trust, IBC offshore sans accès).
1. **Mobiliser les leaks** (chapitre 18) si arrêt sur structure opaque.
1. **Mobiliser la coopération internationale** si toujours bloqué.
1. **Calibrer la confiance** : UBO de droit identifié ≠ UBO réel automatique. Le contrôle effectif peut résider ailleurs (conventions, options, pacte).

#### Mini-walkthrough — chaîne CLEARFLOW (partielle)

Sur une des SAS françaises, NEXUS TRADING SAS :

- Associé unique au capital : NEXUS HOLDINGS LTD (Chypre).
- NEXUS HOLDINGS LTD : actionnaire majoritaire = OMEGA HOLDINGS TRUST (trust chypriote).
- OMEGA HOLDINGS TRUST : settlor = Karim Élie Haddad (identifié via Pandora Papers, chapitre 18). Trustee : cabinet professionnel chypriote (corporate service provider). Bénéficiaires : « la famille Haddad » (formulation typique d’un trust patrimonial — flou volontaire).

Chaîne : NEXUS FR ← NEXUS CY ← OMEGA TRUST ← Karim Haddad (settlor + bénéficiaire probable).

Niveau de confiance :

- Sur la chaîne juridique : *quasi-certain* (registres + leak).
- Sur l’identification de Haddad comme UBO réel : *probable* à *quasi-certain* selon recoupements ultérieurs (analyse de flux, contrôle effectif observable).

Lacunes : la formulation « famille Haddad » dans les bénéficiaires masque le pourcentage et la nature exacte du contrôle. Une coopération avec Mokas (CRF chypriote) serait nécessaire pour clarifier.

#### Erreurs fréquentes

- **S’arrêter au premier niveau.** Identifier un associé personne morale sans remonter = travail incomplet.
- **Confondre actionnaire principal et UBO.** Un actionnaire détenant 24,9 % peut ne pas être UBO au sens UE (seuil 25 %), mais peut être UBO de fait par convention.
- **Ignorer le contrôle effectif.** Les statuts juridiques ne disent pas toujours qui dirige réellement.

#### Limites

Lorsque la chaîne aboutit à une **structure opaque** (trust offshore, IBC sans accès), l’identification de l’UBO réel reste *probable* au mieux sur la base d’OSINT seul. La coopération internationale est nécessaire pour passer à *quasi-certain*.

#### Lien avec le fil rouge

> **CLEARFLOW — Mapping du contrôle**
> 
> En remontant systématiquement chaque chaîne, Nassim aboutit à 4 « racines » principales du réseau : Karim Haddad (settlor du trust chypriote, UBO probable de plusieurs entités), un proche collaborateur basé à Dubaï (M. Y, PSC de plusieurs Limited UK), une fondation libanaise (rôle réel non clarifié), et un cabinet de trustees professionnel (mandant véritable inconnu — possible interposition supplémentaire). Cette carte du contrôle est l’un des livrables les plus stratégiques de la note.

#### Points clés à retenir

- Distinguer associés / UBO / contrôle effectif.
- Remonter systématiquement la chaîne jusqu’à une personne physique ou une structure opaque.
- Mécanismes de contrôle indirect : trusts, fondations, nominees, conventions, options, usufruit.
- Niveau de confiance à calibrer à chaque étape de la chaîne.

-----

### Chapitre 24 — Holdings, filiales et montages en cascade

#### Objectif du chapitre

Comprendre la **logique économique** des montages en cascade (holding mère, filiales, sous-filiales), distinguer les montages légitimes des montages à finalité d’opacification ou d’optimisation discutable.

#### Le concept

Un **groupe** est un ensemble d’entités juridiques distinctes liées par des liens de capital ou de contrôle. La structuration typique :

- **Holding ultime** (parfois nommée « top holding ») — détient les autres entités.
- **Sous-holdings intermédiaires** — fonctions spécifiques (financement, gestion d’actifs, opérations dans une juridiction).
- **Filiales opérationnelles** — entités qui réalisent l’activité économique réelle.

**Pourquoi des holdings ?** Plusieurs raisons, légitimes et moins légitimes :

- **Optimisation fiscale légale** : régimes mère-filles, exonération des dividendes intra-groupe, traités fiscaux.
- **Séparation juridique des risques** : une activité risquée dans une filiale dédiée, protégée des autres.
- **Gouvernance** : structuration par métier, par géographie.
- **Pré-IPO ou opérations corporate** : préparer une cession ou une introduction en bourse.
- **Opacification** : ajouter des couches pour rendre le contrôle moins lisible.
- **Évitement fiscal agressif** : combinaisons exploitant les failles de traités (treaty shopping).
- **Blanchiment** : couches successives complexifiant le suivi des fonds (layering).

#### L’utilité opérationnelle

L’analyste cherche à comprendre :

- **La logique économique** du montage. Est-ce cohérent avec l’activité (groupe international légitime avec présence dans plusieurs pays) ou disproportionné (3 holdings pour une activité de PME locale) ?
- **Les juridictions choisies** et leur sens (chapitre 10) : Luxembourg pour holding (régime mère-filles favorable), Pays-Bas pour la même raison, Suisse pour la banque privée, BVI pour l’opacité, etc.
- **Les flux intra-groupe** : management fees, redevances de marque, prêts intragroupe, dividendes — autant de canaux pour faire circuler la valeur de manière préférentielle.
- **Les filiales dormantes** : présentes mais sans activité — coquilles à recycler ou réserves stratégiques.

#### Méthode — analyse d’un montage en cascade

1. **Construire le graphe** : qui détient qui, à quel pourcentage, dans quelle juridiction.
1. **Annoter chaque entité** : forme juridique, juridiction, activité déclarée, CA, effectif si connu.
1. **Identifier les flux intra-groupe** dans les comptes consolidés ou par les conventions visibles (notes annexes).
1. **Détecter les anomalies** : couches sans justification économique, juridictions opaques sans rationale, holdings sans substance économique.
1. **Calibrer** : montage cohérent avec activité internationale légitime ? Disproportionné ? Compatible avec optimisation fiscale agressive ? Avec opacification ?

#### Mini-walkthrough — montage Haddad

Cartographie progressive :

```
Karim Haddad (UBO probable)
  └─ OMEGA HOLDINGS TRUST (Chypre)
        └─ NEXUS HOLDINGS LTD (Chypre)
              ├─ NEXUS TRADING SAS (France) — opérations
              ├─ NEXUS INTERNATIONAL FZ (Émirats, free zone) — siège commercial
              ├─ NEXUS LOGISTICS LTD (UK) — logistique apparente
              ├─ NEXUS DELAWARE LLC (US, Delaware) — opacité
              └─ SOPARFI LUX SARL (Luxembourg) — holding intermédiaire
                    ├─ NEXUS NEGOCE SARL (Côte d'Ivoire) — opérations Afrique
                    └─ NEXUS LIBAN SAL (Liban) — racine régionale
```

Lecture FININT :

- **Top holding** : trust chypriote (opacification + planification patrimoniale plausible).
- **Sous-holding chypriote** : NEXUS HOLDINGS LTD — intermédiaire commercial typique.
- **Filiales opérationnelles** : SAS France, FZ Émirats, Limited UK — couvrent les zones d’activité commerciale.
- **Coquille opaque** : LLC Delaware — pas d’activité visible, fonction inconnue (à investiguer).
- **Sous-holding luxembourgeois** : SOPARFI — point intermédiaire pour les filiales africaines.
- **Filiales africaines et libanaise** : opérations locales.

Lacunes : substance économique réelle des holdings non-opérationnels (NEXUS HOLDINGS CY, SOPARFI LUX, LLC Delaware) ? Présence de personnel ? Locaux ? Cette substance distingue un montage légitime (présence économique réelle dans chaque juridiction) d’un montage de pure interposition.

Hypothèses :

- **H1 — Montage de structuration légitime** : groupe familial international avec présence multi-juridictionnelle légitime, optimisation fiscale aux limites du légal. *Possible.*
- **H2 — Montage d’opacification et d’optimisation agressive** : couches sans substance économique réelle, ingénierie pour brouiller le contrôle et minimiser la fiscalité. *Probable.*
- **H3 — Montage incluant des éléments de blanchiment** : certaines entités servent au transit de fonds illicites. *Possible, à confirmer par l’analyse de flux.*

#### Erreurs fréquentes

- **Confondre montage complexe et illégalité.** Beaucoup de groupes internationaux légitimes ont des montages très complexes.
- **Surinterpréter une juridiction.** Le Luxembourg est une juridiction européenne respectée ; sa présence n’est pas un signal d’illégalité en soi.
- **Ne pas chercher la substance économique** : la présence/absence de personnel, locaux, activité opérationnelle réelle distingue le légitime du fictif.

#### Limites

La substance économique des holdings offshore est souvent **invisible à l’OSINT seul**. La coopération internationale (CRF locales) ou les rapports sectoriels publiés sont nécessaires.

#### Lien avec le fil rouge

> **CLEARFLOW — Architecture du groupe**
> 
> Nassim conclut, après cartographie complète : le montage Haddad est **disproportionné** par rapport à l’activité commerciale visible (négoce de matériel agricole et services). Plusieurs entités sont des coquilles probables. La présence du trust chypriote au sommet et de la LLC Delaware en branche latérale sont des signaux d’opacification. Le SOPARFI luxembourgeois pourrait être légitime (régime mère-filles) ou pourrait être une couche additionnelle d’optimisation agressive. La qualification globale du montage : *probable* opacification, *possible* implication dans des schémas illicites — à confirmer par l’analyse de flux (Partie VI).

#### Points clés à retenir

- Les montages en cascade ont des justifications légitimes et illégitimes.
- Analyser : juridictions, substance économique, flux intra-groupe.
- Distinguer optimisation légale, optimisation agressive, opacification, blanchiment.
- La substance économique est souvent la clé.

-----

### Chapitre 25 — Trusts, fondations, nominees et prête-noms

#### Objectif du chapitre

Maîtriser les **structures de détention indirecte** : trusts, fondations privées, nominees, prête-noms — leurs mécanismes, leurs usages légitimes, leur exploitation dans l’opacification, et leur lecture en enquête FININT.

#### Le concept

**Trust** (common law). Une relation juridique tripartite :

- **Settlor** (constituant) : la personne qui apporte les actifs au trust.
- **Trustee** : la personne (physique ou morale, souvent un trust company) qui détient et gère légalement les actifs au profit des bénéficiaires.
- **Bénéficiaires** : personnes (nommées ou non) qui jouissent des actifs (revenus ou capital, selon les termes).
- **Protecteur** (parfois) : tiers chargé de surveiller le trustee et/ou de modifier le trust.

**Types de trusts** :

- **Trust révocable** : le settlor peut révoquer et récupérer les actifs. Faible opacification ; les actifs restent attribuables.
- **Trust irrévocable** : le settlor ne peut plus récupérer. Opacification renforcée ; mais le settlor est généralement listé.
- **Trust discrétionnaire** : le trustee a un pouvoir discrétionnaire sur la distribution. Souvent utilisé pour des montages opaques (qui sont les bénéficiaires effectifs ? le trustee décide).
- **Trust avec lettre de souhait** : le settlor laisse une « letter of wishes » non contraignante au trustee — outil d’opacification fréquent.

**Juridictions de trust** : UK, US, BVI, Cayman, Bahamas, Jersey, Guernsey, Île de Man, Singapour, Hong Kong, Suisse (admis depuis 2007 sous certaines conditions), New Zealand.

**Fondation privée** (droit continental). Entité juridique distincte. Mécanisme similaire au trust mais juridiquement différent :

- **Fondateur** : apporte les actifs.
- **Conseil de fondation** : gère.
- **Bénéficiaires** : reçoivent.

**Juridictions de fondations privées** : Liechtenstein (Stiftung), Panama, Pays-Bas (Stichting), Autriche, Suisse, certaines juridictions caribéennes.

**Nominee**. Prête-nom **officiel**, déclaré comme tel. Mécanisme courant en common law (nominee director, nominee shareholder). Le nominee détient au nom d’un bénéficiaire qu’il représente. La relation est formalisée par un contrat (declaration of trust, nominee agreement).

**Prête-nom (en droit continental)**. Personne qui apparaît officiellement comme dirigeant ou associé sans l’être réellement. À la différence du nominee, la relation est **dissimulée** dans la plupart des juridictions de droit continental. En France, le prête-nom est illicite quand il vise à frauder.

#### L’utilité opérationnelle

L’analyste doit savoir :

- **Identifier la présence** d’une telle structure dans une chaîne de contrôle (chapitre 23).
- **Comprendre les rôles** : qui est settlor / fondateur / trustee / bénéficiaire.
- **Identifier les UBO réels** : selon les directives AML, ce sont (pour les trusts) le settlor, les trustees, les protecteurs, les bénéficiaires identifiés ou la classe, et toute personne contrôlant.
- **Détecter les prête-noms** : signaux d’incohérence entre profil et fonction.

#### Méthode — analyser une structure de détention indirecte

1. **Récupérer les actes** quand accessibles (trust deed, statuts de fondation) — souvent indisponibles en sources ouvertes, possibles en leaks (Pandora particulièrement riche).
1. **Identifier les acteurs déclarés** : settlor, trustee, bénéficiaires, protecteurs.
1. **Profiler chacun** : le trustee est-il un cabinet professionnel ? Quels autres trusts gère-t-il ? Le settlor est-il visible publiquement ?
1. **Croiser avec leaks et presse** : Pandora et Paradise Papers contiennent souvent les éléments de trusts non publics.
1. **Identifier les bénéficiaires** : nommés ou catégorie ? Si « famille X », identifier les membres.
1. **Calibrer** : qui contrôle réellement ? Réversibilité ? Liens visibles entre settlor et bénéficiaires ?

**Détecter un prête-nom (signaux probabilistes)** :

- **Profil incohérent** : retraité de 80 ans dirigeant 7 SAS de négoce.
- **Absence d’expérience visible** dans le secteur.
- **Réseau personnel pauvre** sur LinkedIn et réseaux sociaux par rapport aux mandats officiels.
- **Domiciliation à l’adresse de la société** ou d’un cabinet de domiciliation.
- **Multi-mandats** dans des secteurs sans cohérence.
- **Rotation rapide** des mandats (entrées et sorties multiples).
- **Lien capillaire avec un autre acteur** identifié comme contrôleur réel possible.

Aucun de ces signaux ne suffit. **Plusieurs convergents** justifient le qualificatif *probable* prête-nom — jamais *quasi-certain* sans éléments documentaires (témoignages, actes contestés, aveux).

#### Mini-walkthrough — OMEGA HOLDINGS TRUST

- Identification dans Pandora Papers (chapitre 18) : trust chypriote constitué en 2019.
- **Settlor** : Karim Élie Haddad, identifié.
- **Trustee** : Cabinet Pancyprian Trustees Ltd (Chypre) — cabinet professionnel, identifié comme administrateur de plusieurs centaines de trusts dans Pandora.
- **Bénéficiaires** : « the family of the settlor » — formulation vague, à étendre.
- **Protecteur** : non identifié dans les documents disponibles.
- Type : trust irrévocable, mais avec letter of wishes mentionnée dans le trust deed (les souhaits du settlor sont à respecter par le trustee).

Lecture FININT : structure typique d’un trust patrimonial à finalité d’opacification du contrôle. Le settlor est identifié *quasi-certain* (leak Pandora). Le contrôle effectif est *probable* chez le settlor (letter of wishes), avec autonomie nominale du trustee. Les bénéficiaires (famille Haddad) restent à identifier précisément — recherche presse et OSINT sur l’entourage familial.

#### Erreurs fréquentes

- **Considérer tout trust comme illégal.** Les trusts sont des outils juridiques largement utilisés et légitimes, notamment en droit anglo-saxon (planification successorale, protection des incapables, donations conditionnelles, etc.).
- **Considérer tout prête-nom comme volontaire.** Certaines personnes peuvent être *abusées* (mules, identités usurpées).
- **Confondre nominee et prête-nom illicite.** Le nominee anglo-saxon est légal s’il est correctement déclaré.

#### Limites

La structure interne d’un trust ou d’une fondation est généralement **non publique** en l’absence de leak. La coopération internationale est nécessaire pour obtenir le trust deed, la liste des bénéficiaires, les distributions effectuées.

#### Lien avec le fil rouge

> **CLEARFLOW — Trust et prête-noms**
> 
> Nassim consolide : OMEGA TRUST = structure de contrôle ultime du réseau Haddad, settlor identifié, contrôle effectif probable. En parallèle, Monsieur X et 3 autres mandataires français sont *probables* prête-noms (profils convergents avec multi-mandats, cabinet de domiciliation, absence d’expérience sectorielle). Mme Z, présidente d’une SAS, n’est pas *probable* prête-nom — son profil est différent et un recoupement avec le réseau personnel de Haddad (presse libanaise antérieure) montre un lien amical. Hypothèse Mme Z : présidente nominale avec lien personnel à Haddad, sans qualification certaine de prête-nom. Calibration *possible*.

#### Points clés à retenir

- Trust : settlor + trustee + bénéficiaires + (protecteur). Fondation : fondateur + conseil + bénéficiaires.
- Tous les rôles sont, selon la 4e/5e directive AML, à considérer comme UBO.
- Prête-noms : détecter par convergence de signaux faibles, jamais sur un seul indice.
- Sources : leaks (Pandora particulièrement), coopération internationale.

-----

### Chapitre 26 — Sociétés écrans et sociétés dormantes

#### Objectif du chapitre

Comprendre la notion de **société écran**, distinguer les **sociétés dormantes**, et caractériser quand une structure est probablement écran sur la base d’un faisceau d’indices.

#### Le concept

**Société écran** (shell company). Notion ambiguë. En sens strict : entité juridique sans activité économique réelle, sans personnel, sans actifs autres que les titres de la société, créée pour porter une finalité spécifique sans substance opérationnelle propre.

**Société de façade**. Entité avec une activité économique de façade (apparente) mais dont la véritable fonction est tout autre (canal de blanchiment, fraude, etc.).

**Société dormante**. Entité existante mais qui n’exerce plus d’activité, ni de manière à façade. Distinct de la société écran : dormante = inactive, écran = active mais sans substance économique propre.

**Société boîte aux lettres** (mailbox company, letterbox company). Entité avec une simple adresse de domiciliation, sans présence opérationnelle. Souvent synonyme de société écran selon les contextes.

**Important** : toutes les sociétés écrans **ne sont pas illégales**. Beaucoup ont des usages légitimes :

- Holding de gestion patrimoniale.
- Véhicule de financement (SPV — Special Purpose Vehicle).
- Société de portage temporaire (M&A).
- Société pré-IPO.
- Société pour acquisition immobilière (SCI, REIT, etc.).

**Société écran à finalité illicite** : créée pour dissimuler des transactions, opacifier une chaîne, fictivement justifier des flux, ou frauder.

#### L’utilité opérationnelle

L’analyste cherche à qualifier : cette entité est-elle une société écran ? Si oui, à quelle finalité (légitime ou illicite) ?

**Indices d’écran à finalité illicite** :

1. **Absence de substance économique** : pas de personnel, pas de locaux propres, pas d’activité visible.
1. **Adresse de domiciliation** partagée avec de nombreuses autres entités.
1. **Dirigeant unique** avec multi-mandats (signal prête-nom probable).
1. **Création récente** (souvent juste avant la transaction d’intérêt).
1. **Capital social minimal** (1 €, 100 €, 10 000 €).
1. **Comptes non publiés** ou publiés en retard, ou « confidentiels » dès l’origine.
1. **Activité déclarée** (NAF/SIC code) très large et vague (« commerce de gros non spécialisé », « activités de holding »).
1. **Pas de présence web** ou site web vide / générique.
1. **Pas de comptes bancaires identifiables** dans la juridiction du siège, ou banque exotique disproportionnée.
1. **Transactions disproportionnées** avec la taille apparente (CA en M€ avec 1 employé et 1 € de capital).
1. **Liens avec d’autres entités du même profil** (cluster de coquilles).
1. **Présence dans des leaks** (Panama, Pandora) ou dans des bases adverse media.

Aucun indice n’est suffisant ; **plusieurs convergents** qualifient *probable* écran ; **beaucoup convergents + recoupements** approchent du *quasi-certain*.

#### Méthode — qualification d’une société écran

1. **Profil de base** : registre, comptes, dirigeants, UBO.
1. **Substance économique** : personnel ? locaux ? site web ? clientèle ? fournisseurs ?
1. **Cohérence sectorielle** : flux compatibles avec activité déclarée ?
1. **Liens à d’autres entités** : appartenance à un cluster ?
1. **Adresse de domiciliation** : combien d’autres sociétés à la même adresse ?
1. **Cumul d’indices** : 5+ indices convergents = *probable* écran.
1. **Calibrer la finalité** : écran légitime (holding patrimonial, SPV) ou écran suspect (canal de blanchiment, fraude, transit fictif) ?

#### Mini-walkthrough — NEXUS DELAWARE LLC

- Registre : LLC enregistrée à Delaware en 2022. UBO non accessible (CTA contesté).
- Substance économique : pas de personnel public, pas de site web, pas de présence physique identifiable.
- Adresse de domiciliation : un service de registered agent partagé avec des milliers d’autres LLC Delaware (standard, sans valeur diagnostique en soi).
- Activité : non identifiable.
- Comptes : non publiés (Delaware LLC, exemption).
- Flux observables (via DS) : 850 K€ reçus depuis Chypre, 800 K€ transférés vers un compte personnel suisse. Quelques jours d’écart.
- Lien à d’autres entités : appartient à la chaîne NEXUS du réseau Haddad.

Cumul d’indices : opacité, absence de substance visible, activité non identifiable, flux disproportionnés, cluster d’entités liées. *Probable* société écran à finalité de transit. La finalité (blanchiment ? optimisation ? simple holding ?) reste à confirmer par l’analyse globale des flux et la coopération.

#### Erreurs fréquentes

- **Qualifier « société écran » trop facilement.** Beaucoup de PME légitimes ont peu de personnel, un site web minimaliste, une faible présence en ligne.
- **Ignorer les usages légitimes** : SPV, holdings patrimoniaux, sociétés en cours de création.
- **Confondre dormante et écran.** Une société dormante peut être un actif stratégique non frauduleux.
- **Conclure sans cumul d’indices.** Un seul indice ne suffit jamais.

#### Limites

La qualification *quasi-certaine* d’écran à finalité illicite exige presque toujours des éléments judiciaires (réquisition des relevés bancaires montrant absence d’activité réelle, audition du dirigeant). L’analyste OSINT s’arrête à *probable*.

#### Lien avec le fil rouge

> **CLEARFLOW — Cartographie des écrans probables**
> 
> Sur les 14 entités du réseau Haddad, Nassim qualifie : 4 SAS françaises = *possible* écran (substance économique faible, mais activité commerciale apparente — nécessite confirmation par analyse de flux), NEXUS DELAWARE LLC = *probable* écran de transit, 2 Limited UK = *possible* écran (activité commerciale apparente mais déconnectée du réel à confirmer), entités libanaise et émiraties = données insuffisantes (*indéterminable*). Conclusion : présence d’écrans probables à des fins minimum d’opacification ; finalité illicite *possible* à *probable* selon la confirmation par les flux.

#### Points clés à retenir

- Société écran ≠ illégale par nature. Beaucoup d’usages légitimes.
- Société dormante ≠ écran.
- Qualification par **cumul d’indices** : substance économique, personnel, locaux, activité, cohérence, cluster.
- L’analyste OSINT atteint *probable*, rarement *quasi-certain* sans éléments judiciaires.

-----

## PARTIE V — CARTOGRAPHIER LES RÉSEAUX FINANCIERS

*Sept chapitres pour transformer les données collectées en livrables structurés : fiches par type d’objet, graphes relationnels, qualification des liens, calibration de la confiance. C’est le passage de la collecte brute à l’analyse présentable.*

-----

### Chapitre 27 — Construire une fiche personne

#### Objectif du chapitre

Maîtriser la **fiche personne FININT** : structure standardisée pour consolider, en un livrable réutilisable, tous les éléments collectés sur une personne physique. Le modèle complet est en annexe C ; ce chapitre expose la logique et les choix méthodologiques.

#### Le concept

Une fiche personne est un livrable **atomique** : elle concentre, sur une personne, l’ensemble des éléments d’identification, de profil, de mandats, de patrimoine, de relations et de contentieux. Elle est conçue pour être :

- **Autonome** : lisible sans contexte préalable.
- **Sourcée** : chaque élément factuel renvoie à sa source.
- **Calibrée** : niveau de confiance pour chaque élément non trivial.
- **Versionnée** : date de production, date de dernière mise à jour, version.
- **Actionnable** : conclusions et recommandations en fin.

#### Structure type d’une fiche personne

1. **En-tête** : référence, date, version, classification (TLP), auteur.
1. **Identification** : nom complet, date de naissance, lieu, nationalité(s), adresse(s), photo si disponible. Niveau de confiance global de l’identification.
1. **Profil** : parcours professionnel, formation, langues parlées (signaux d’enquête utiles), affiliations professionnelles, fonctions publiques antérieures, profil PEP éventuel.
1. **Mandats actuels** : liste des sociétés où la personne exerce un mandat, avec rôle, juridiction, période.
1. **Mandats antérieurs** : historique.
1. **UBO et contrôle indirect** : entités où la personne est UBO identifié, déclaré ou *probable*.
1. **Patrimoine identifié** : immobilier, financier, actifs particuliers (œuvres, véhicules, bateaux, etc.), train de vie observable.
1. **Réseau** : famille proche, collaborateurs réguliers, associés, personnes clés du dossier.
1. **Contentieux et réputation** : procédures publiques, condamnations, sanctions, adverse media.
1. **Sanctions et PEP** : présence sur listes, statut PEP, vérifications screening.
1. **Liens crypto** (si pertinent) : adresses ou attributions on-chain — renvoi vers OSINT Crypto pour le traitement détaillé.
1. **Hypothèses calibrées** : ce que l’analyste retient sur cette personne, avec niveaux de confiance.
1. **Sources** : liste exhaustive avec dates.
1. **Lacunes et actions complémentaires** : ce qui n’a pas pu être établi, et comment le faire.

#### L’utilité opérationnelle

La fiche personne est **réutilisable** : produite une fois, elle alimente plusieurs livrables (note FININT, dossier d’enquête, dossier compliance). Elle est **interopérable** : un format standardisé permet à différents analystes de se transmettre l’information sans perte.

Elle est aussi un **outil de discipline** : la rédiger oblige à expliciter ce qu’on sait et ce qu’on ne sait pas. C’est un puissant antidote aux conclusions précipitées.

#### Méthode — bonnes pratiques

- **Ne pas confondre fiche et résumé** : la fiche est exhaustive sur ce qui est connu, pas un résumé.
- **Sourcer chaque élément** : pas d’affirmation sans référence.
- **Calibrer chaque conclusion** : niveau de confiance.
- **Distinguer mandat déclaré et contrôle réel**.
- **Respecter la présomption d’innocence** : un mis en examen n’est pas un coupable.
- **Mentionner les lacunes** : la fiche ne fait pas semblant de tout savoir.

#### Mini-walkthrough — fiche Karim Haddad (extrait)

```
FICHE PERSONNE — KARIM ÉLIE HADDAD
Référence : CLEARFLOW/PER/001 | v1.3 | 14/03 | TLP:AMBER

IDENTIFICATION (quasi-certain)
- Né le 17/04/1968 à Beyrouth, Liban
- Nationalités : libanaise (par naissance), française (par naturalisation, 2006)
- Adresses : Paris 16e (résidence principale déclarée), Beyrouth (Achrafieh), Dubaï (DIFC apartments)
- Photo : LinkedIn, presse libanaise 2023

PROFIL (probable)
- Diplômé ESCP Paris (1992), parcours négoce international depuis 1995
- Langues : arabe, français, anglais
- Pas de fonction publique connue
- Pas de statut PEP au sens strict
- Affiliation : Chambre de commerce franco-libanaise (membre actif)

MANDATS ACTUELS DÉCLARÉS (quasi-certain)
- NEXUS LIBAN SAL — administrateur (Liban, depuis 2002)
- NEXUS INTERNATIONAL FZ — propriétaire (Émirats, free zone)
- (aucun mandat déclaré dans les 4 SAS françaises ni dans les 2 Limited UK)

UBO PROBABLE OU IDENTIFIÉ
- OMEGA HOLDINGS TRUST (Chypre) — settlor identifié via Pandora (quasi-certain)
- NEXUS HOLDINGS LTD (Chypre) — UBO probable via chaîne (probable)
- 4 SAS françaises — UBO réel probable via prête-noms (probable)
- LLC Delaware — non confirmé (indéterminable)
- (autres entités, voir fiche groupe)

PATRIMOINE IDENTIFIÉ
- Immobilier : 3 biens à Paris (SCI), 1 villa à Beyrouth, présence à Dubaï (location non confirmée)
- Financier : participations dans le groupe, comptes bancaires en France, présomé en Suisse (DS)
- Train de vie : voyages réguliers Paris-Beyrouth-Dubaï-Genève, événements caritatifs au Liban

RÉSEAU
- Famille : épouse française, 3 enfants. Frère installé à Dubaï (lien d'affaires).
- Collaborateurs identifiés : M. Y (Dubaï, dirigeant déclaré Limited UK), Mme Z (présidente d'une SAS, lien personnel)

CONTENTIEUX ET RÉPUTATION
- Transaction fiscale française 2018 (sans poursuite pénale ; presse)
- Aucune condamnation publique
- Adverse media : présence dans presse régionale, allégations 2023 (Côte d'Ivoire) sans nomination explicite

SANCTIONS / PEP
- Aucune sanction OFAC, UE, ONU, OFSI vérifiées
- Non-PEP au sens strict (pas de fonction publique)

LIENS CRYPTO
- Mentions USDT dans certaines DS — volet renvoyé à Athéna Group / Sarah Marin pour analyse on-chain

HYPOTHÈSES CALIBRÉES
- UBO réel d'une majorité des entités du réseau Haddad : probable.
- Implication dans schéma de transit financier multi-juridictionnel : probable.
- Implication directe dans blanchiment ou contournement de sanctions : possible à ce stade, à confirmer par flux et coopération.

LACUNES
- Comptes bancaires libanais et suisses : accès non obtenu (coopération en cours).
- Liste exhaustive des bénéficiaires d'OMEGA TRUST : non connue.
- Substance économique des entités émiraties : non vérifiée.

SOURCES (extrait)
- Pappers, INPI, RBE [04/03]
- Companies House, PSC [05/03]
- OpenCorporates, Sayari [05/03]
- ICIJ Pandora Papers, Aleph OCCRP [06/03]
- LinkedIn, presse [07/03]
- Patrim France [08/03]
- DS reçues par CRF (référencées en interne)
```

#### Erreurs fréquentes

- **Fiche incomplète sans mention des lacunes.** Un livrable lisse passe pour exhaustif et trompe le lecteur.
- **Mélanger les niveaux de confiance.** Tout n’est pas *quasi-certain*. La calibration explicite est obligatoire.
- **Ne pas dater chaque élément.** Les profils changent.

#### Limites

Une fiche ne remplace pas une analyse contextuelle. Elle l’alimente. Elle ne dit pas non plus *« cette personne est coupable »* — ce vocabulaire n’a pas sa place ici.

#### Lien avec le fil rouge

> **CLEARFLOW — La fiche au cœur du dossier**
> 
> La fiche Karim Haddad est le pivot du dossier de Nassim. Elle est mise à jour à chaque étape majeure. À la finale, elle sera produite en annexe de la note de transmission au PNF. Toute autre fiche du dossier (M. Y, Mme Z, M. X, etc.) suit le même modèle.

#### Points clés à retenir

- Fiche = livrable autonome, sourcé, calibré, versionné, actionnable.
- 14 sections type ; modèle complet en annexe C.
- Discipline d’explicitation des lacunes.
- Pas de conclusion de culpabilité dans une fiche.

-----

### Chapitre 28 — Construire une fiche société

#### Objectif du chapitre

Maîtriser la **fiche société FININT** — pendant de la fiche personne, structurée pour les entités juridiques. Modèle complet en annexe D.

#### Le concept

La fiche société consolide, sur une entité, tout ce que l’analyste sait : identification, juridiction, gouvernance, capital et UBO, activité, comptes, flux, contentieux, liens avec d’autres entités, hypothèses calibrées.

#### Structure type d’une fiche société

1. **En-tête** : référence, date, version, classification, auteur.
1. **Identification** : dénomination exacte, identifiant officiel, forme juridique, juridiction, capital, date de création.
1. **Adresse(s)** : siège, établissements secondaires, adresse réelle si différente du siège déclaré.
1. **Activité déclarée** : NAF/SIC/code sectoriel, libellé, sous-activités.
1. **Gouvernance** : dirigeants actuels, mandataires, historique.
1. **Actionnariat / Capital** : associés, pourcentages, classes d’actions.
1. **UBO** : déclaré (registre UBO) et identifié (analyse), avec niveaux de confiance.
1. **Substance économique** : personnel, locaux, site web, clientèle, fournisseurs, présence opérationnelle réelle.
1. **Comptes** : derniers comptes annuels publiés, principaux indicateurs, ratios, observations.
1. **Flux observables** : profil bancaire (si DS ou OSINT), contreparties principales.
1. **Contentieux** : procédures collectives, contentieux fiscaux, sanctions, adverse media.
1. **Liens** : entités liées (capital, dirigeants partagés, adresse partagée), trust ou fondation au sommet.
1. **Crypto si pertinent** : adresses, échanges utilisés — renvoi vers OSINT Crypto.
1. **Hypothèses calibrées** : qualification de la nature de l’entité (opérationnelle légitime, holding, intermédiaire, écran probable, etc.).
1. **Sources et lacunes**.

#### L’utilité opérationnelle

Comme pour la fiche personne, la fiche société est **réutilisable, sourcée, calibrée**. Elle permet de structurer un livrable complexe (note FININT couvrant plusieurs entités) en éléments atomiques cohérents.

#### Méthode — bonnes pratiques

- **Préciser la juridiction** dès l’identification (pas de confusion avec sociétés homonymes).
- **Annoter l’identifiant officiel** systématiquement.
- **Mettre la substance économique en évidence** : c’est souvent la clé.
- **Présenter les comptes en ratios** plus qu’en chiffres bruts, pour comparaison.
- **Documenter les liens** avec une référence à la fiche correspondante.

#### Mini-walkthrough — fiche NEXUS TRADING SAS (extrait)

```
FICHE SOCIÉTÉ — NEXUS TRADING SAS
Référence : CLEARFLOW/SOC/003 | v1.2 | 14/03 | TLP:AMBER

IDENTIFICATION (quasi-certain)
- Forme : SAS
- SIREN : 8XX XXX XXX
- Juridiction : France
- Capital : 10 000 €
- Date de création : 18/01/2023

ADRESSE(S)
- Siège : 12 rue Y, Paris 9e (cabinet de domiciliation, 47 entités à la même adresse)

ACTIVITÉ DÉCLARÉE
- NAF 4690Z : commerce de gros non spécialisé
- Activité opérationnelle visible : non identifiée (pas de site web, pas de catalogue, pas de référence client publique)

GOUVERNANCE
- Président : Monsieur X (depuis création) — multi-mandats, profil prête-nom probable (voir fiche personne)
- Aucun DG, aucun directeur, aucun salarié déclaré (URSSAF non accessible directement)

ACTIONNARIAT / CAPITAL
- Associé unique : NEXUS HOLDINGS LTD (Chypre)

UBO
- Déclaré au RBE : Monsieur X (par défaut, en tant que dirigeant)
- Identifié (probable) : Karim Élie Haddad, via chaîne CY → trust OMEGA → settlor

SUBSTANCE ÉCONOMIQUE
- Personnel : aucun salarié visible
- Locaux : domiciliation seule
- Site web : aucun
- Clientèle visible : aucune
- Fournisseurs visibles : aucune trace publique
→ Substance économique très faible. Écran probable.

COMPTES (1er exercice clos)
- CA : 12,4 M€
- Marge brute : 4 %
- Charges de personnel : 32 K€
- Résultat d'exploitation : 80 K€
- Trésorerie en fin d'exercice : 35 K€
→ Profil compatible avec activité de pure intermédiation OU société de transit.

FLUX OBSERVABLES (via DS)
- Entrées : 87 % depuis Émirats (sociétés liées au réseau Haddad) et Chypre
- Sorties : virements vers 4 sociétés du réseau + 22 % vers comptes personnels (M. X et liés)
→ Profil incompatible avec activité commerciale réelle de négoce.

CONTENTIEUX
- Aucune procédure collective.
- Aucun contentieux fiscal public.

LIENS
- Capital : 100 % NEXUS HOLDINGS LTD (CY)
- Dirigeants partagés : M. X = dirigeant de 7 autres SAS (cluster).
- Adresse partagée : 46 autres entités au même cabinet.
- Trust de contrôle : OMEGA HOLDINGS TRUST (CY).

HYPOTHÈSES CALIBRÉES
- Société écran à finalité de transit : probable.
- Implication dans schéma de blanchiment ou TBML : possible à probable (à confirmer par analyse de flux globale).
- UBO réel = Karim Haddad : probable.

LACUNES
- Substance opérationnelle réelle : non vérifiée par visite physique.
- Comptes détaillés (relevés bancaires) : accès en CRF, non encore mobilisé.

SOURCES
- Pappers, INPI, RBE
- Comptes annuels Infogreffe
- DS bancaires (interne CRF)
- Cartographie réseau (chapitre 31)
```

#### Erreurs fréquentes

- **Confondre dénomination commerciale et dénomination sociale.** Toujours utiliser la dénomination officielle.
- **Ne pas mentionner les lacunes sur la substance économique.** Sans visite physique ou témoignage, la substance reste *probable* à qualifier.
- **Lire les comptes sans contexte sectoriel.** Une faible marge en intermédiation peut être normale.

#### Limites

Beaucoup d’éléments de la fiche société exigent des sources fermées (comptes bancaires détaillés, contrats commerciaux, audits). En OSINT pur, la fiche est **partielle** et l’indique explicitement.

#### Lien avec le fil rouge

> **CLEARFLOW — 14 fiches société**
> 
> Nassim produit une fiche pour chacune des 14 entités du réseau Haddad. Cumulées, ces fiches forment le socle de la note de transmission. Elles permettent de répondre à la question « quelle est la nature de chaque entité dans le réseau ? » avec calibration de la confiance pour chaque qualification.

#### Points clés à retenir

- Fiche société : pendant structurel de la fiche personne, pour les entités.
- 15 sections type ; modèle complet en annexe D.
- Substance économique = section clé.
- Ratios > chiffres bruts pour la lecture rapide.

-----

### Chapitre 29 — Construire une fiche flux

#### Objectif du chapitre

Maîtriser la **fiche flux** : livrable structurel qui consolide, sur un flux financier ou un ensemble de flux liés, les éléments d’origine, de transit, de destination, et leur qualification typologique. Modèle en annexe E.

#### Le concept

Une fiche flux peut concerner :

- **Un flux unique** : un virement, un dépôt, une opération.
- **Une séquence** : plusieurs flux liés (cascade, fractionnement, layering).
- **Un schéma** : une typologie observée sur une période, impliquant plusieurs comptes et entités.

#### Structure type

1. **En-tête** : référence, date, version, classification.
1. **Description** : type de flux (virement, dépôt cash, paiement carte, opération crypto), montant, devise, date(s).
1. **Origine** : compte donneur d’ordre, banque, juridiction, titulaire, libellé.
1. **Transit** : banques correspondantes, comptes intermédiaires, rails utilisés (SWIFT, SEPA, SCT Inst, etc.).
1. **Destination** : compte bénéficiaire, banque, juridiction, titulaire, libellé reçu.
1. **Délai** : heure de débit, heure de crédit, délais inter-étapes.
1. **Contexte** : autres flux liés, comportement antérieur, motif déclaré.
1. **Cohérence économique** : flux compatible avec l’activité ? avec les comptes annuels ? avec le profil du titulaire ?
1. **Typologie possible** : à quel schéma ce flux est-il compatible (TBML, BEC, layering, structuration, etc.) ?
1. **Hypothèses calibrées** et niveaux de confiance.
1. **Sources** : DS, relevés (référence interne), OSINT.
1. **Lacunes** et actions complémentaires.

#### L’utilité opérationnelle

La fiche flux **isole un cas** pour qu’il puisse être analysé, présenté à un magistrat, ou intégré dans une typologie sectorielle. Elle est particulièrement utile dans les dossiers complexes où plusieurs typologies coexistent : isoler les flux par type permet une analyse plus claire.

#### Méthode

1. **Définir le périmètre** : un flux, une cascade, un schéma — préciser dès l’en-tête.
1. **Recueillir tous les attributs** (montants, dates, parties, rails).
1. **Identifier la cohérence ou l’anomalie**.
1. **Confronter à une typologie** : le flux ressemble-t-il à un schéma connu (chapitres 40-47) ?
1. **Calibrer**.

#### Mini-walkthrough — séquence BEC fictive (extrait fiche flux)

```
FICHE FLUX — SÉQUENCE BEC LAYERING 14/03
Référence : CLEARFLOW/FLX/021 | v1.0 | TLP:AMBER

DESCRIPTION
- Type : séquence SCT Inst + SCT Inst + dépôts USDT
- Montant total : 215 000 €
- Période : 14/03, 14h32 → 14/03, 18h45 (4h13)

ORIGINE
- Compte source : PME française "ALPHA INDUSTRIE SARL", banque XYZ, IBAN FR...
- Donneur d'ordre : signature du gérant, validation à 14h28
- Contexte : virement présenté comme paiement à un nouveau fournisseur, libellé "trade payment - facture XXXX"

TRANSIT
1. ALPHA SARL → IBAN ES (nouveau) "Iberica Trading SL" : 215 000 €, 14h32, SCT Inst, irréversible.
2. Iberica Trading SL → 5 IBANs (PT x3, LT x2) : fractionnement 40 000 € à 45 000 €, 14h35-14h41.
3. Comptes PT/LT → exchange A : 5 dépôts USDT, 16h12.
4. Exchange A → wallet auto-géré : sortie crypto, 18h45.

DÉLAI TOTAL
- Origine → wallet : 4h13. Fenêtre de gel : quasi-nulle (SCT Inst irréversible).

CONTEXTE
- ALPHA SARL avait reçu un email frauduleux 48h avant, simulant le gérant d'une société partenaire et demandant un changement d'IBAN.
- Le mail provenait d'un domaine très proche du vrai (typosquatting).

COHÉRENCE ÉCONOMIQUE
- Incompatible avec l'activité d'ALPHA (pas de relation antérieure avec Iberica, montant inhabituel, IBAN ES nouveau).

TYPOLOGIE POSSIBLE
- Fraude au virement (BEC) avec layering instantané et cashout crypto.

HYPOTHÈSES CALIBRÉES
- BEC : quasi-certain (séquence et contexte univoques).
- Cashout crypto : quasi-certain.
- Identification de l'auteur : indéterminable à ce stade ; volet on-chain renvoyé à Athéna Group.

SOURCES
- Plainte ALPHA SARL
- Relevés bancaires (réquisition en cours pour comptes ES, PT, LT)
- DS de la banque XYZ
- Analyse on-chain Athéna (en cours)

LACUNES
- Identification de l'attaquant.
- Lien éventuel avec d'autres cas (cluster d'attaques BEC).
```

#### Erreurs fréquentes

- **Mélanger plusieurs séquences dans une seule fiche.** Une fiche = un flux ou une séquence cohérente.
- **Ne pas mentionner le délai entre étapes.** La vitesse est un signal essentiel.
- **Conclure sur la typologie sans calibration.** Une « ressemblance » à un schéma TBML ne vaut pas typologie *quasi-certaine*.

#### Limites

Beaucoup d’éléments (libellés détaillés, références internes bancaires, métadonnées de l’opération) ne sont accessibles qu’en sources fermées (réquisition, droit de communication CRF).

#### Lien avec le fil rouge

> **CLEARFLOW — Une vingtaine de fiches flux**
> 
> Nassim produit, pour le dossier Haddad, environ 22 fiches flux : des séquences de virements depuis l’étranger vers la France, des transferts intra-groupe, des opérations vers la Suisse, des conversions USDT. Chaque fiche, isolée, est lisible ; cumulées, elles forment la base de l’analyse globale (chapitre 35).

#### Points clés à retenir

- Fiche flux : un flux ou une séquence cohérente, jamais davantage.
- Délai entre étapes = signal critique.
- Typologie possible = hypothèse, jamais conclusion sans calibration.
- Modèle complet en annexe E.

-----

### Chapitre 30 — Construire une fiche actif

#### Objectif du chapitre

Maîtriser la **fiche actif** : livrable centré sur un bien (immobilier, financier, mobilier de valeur), structurant son identification, ses détenteurs (juridiques et effectifs), son historique d’acquisition, sa valeur estimée, et sa pertinence dans l’enquête. Modèle en annexe F.

#### Le concept

Une fiche actif documente :

- **Identification** : nature du bien (immobilier, véhicule, bateau, œuvre, participation), localisation, identifiants.
- **Détenteurs** : propriétaire juridique (SCI, société, personne), UBO probable, financement.
- **Historique** : date d’acquisition, prix, mode de financement, transactions antérieures.
- **Valeur** : valorisation actuelle, source de l’estimation.
- **Pertinence** : pourquoi cet actif est dans le dossier, lien avec la personne ou la société cible.
- **Asset recovery** : susceptibilité de gel / saisie, juridiction, autorité compétente.

#### Types d’actifs traités

**Immobilier** : maisons, appartements, biens commerciaux. Sources : registres fonciers (variables selon pays), Patrim France (consultation administrative), DVF (Demandes de Valeurs Foncières en France, données ouvertes), bases de données commerciales (CityScan, RealCapital), presse mondaine pour les transactions remarquables.

**Véhicules** : voitures de luxe, supercars. Registre des véhicules selon pays.

**Bateaux et yachts** : registres internationaux (Lloyd’s Register, MarineTraffic pour le tracking AIS), pavillons (souvent Malte, Cayman, Bahamas, Marshall pour les yachts).

**Aéronefs** : FAA (US), EASA (UE), pavillon de l’aéronef, traçage ADS-B (FlightAware, ADS-B Exchange).

**Participations financières** : actions, parts sociales, obligations, OPCVM, ETF.

**Œuvres d’art, objets de collection** : registres internes des maisons de ventes (Sotheby’s, Christie’s), bases académiques (Art Loss Register), provenance.

**Comptes bancaires** : pas directement « actifs » mais véhicules de détention. Existence parfois traçable via EAR/CRS pour la CRF.

**Cryptos** : adresses on-chain (renvoi vers OSINT Crypto).

#### L’utilité opérationnelle

La fiche actif sert deux objectifs :

1. **Documenter le patrimoine** d’une personne ou d’un groupe — base de la reconstitution patrimoniale (chapitre 39).
1. **Préparer l’asset recovery** : gel, saisie, confiscation (chapitre 66) — l’identification précise et juridictionnellement qualifiée des actifs est la condition préalable.

#### Méthode

1. **Identifier le bien** par sources ouvertes (cadastre, DVF, AIS, presse).
1. **Identifier le propriétaire juridique** : personne physique, SCI, société.
1. **Remonter jusqu’à l’UBO** quand possible.
1. **Documenter l’historique** : date d’acquisition, prix, mode (cash, prêt, virement, mixte).
1. **Estimer la valeur actuelle**.
1. **Qualifier la cohérence** : ce bien est-il cohérent avec les revenus déclarés du détenteur ?
1. **Identifier la juridiction** et l’autorité compétente pour un éventuel asset recovery.

#### Mini-walkthrough — fiche actif (extrait)

```
FICHE ACTIF — APPARTEMENT PARIS 8e
Référence : CLEARFLOW/ACT/004 | v1.0 | TLP:AMBER

IDENTIFICATION
- Nature : appartement résidentiel
- Localisation : 5 rue X, Paris 8e
- Surface : ~280 m², 6e étage
- Identifiant cadastral : 75108-XXXX-XXXX

DÉTENTEUR JURIDIQUE (quasi-certain)
- SCI HADDAD INVESTISSEMENTS (France), détention 100 %
- Gérance : Mme Z (présidente d'une autre SAS du réseau, lien personnel à K. Haddad)

UBO PROBABLE
- Karim Élie Haddad, via SCI

HISTORIQUE
- Acquisition : 09/2019
- Prix d'acquisition (DVF) : 4,2 M€
- Financement : non transparent en OSINT. Pas de prêt notarié inscrit visible (vérifier hypothèques inscrites).

VALEUR ACTUELLE ESTIMÉE
- Estimation marché : 4,7 M€ (basé sur prix au m² du quartier — DVF récent)
- Source : DVF + cabinet d'estimation (à approfondir)

PERTINENCE
- Bien probablement détenu par K. Haddad via SCI.
- Cohérence avec revenus déclarés : à examiner (déclaration fiscale via réquisition).

ASSET RECOVERY
- Juridiction : France.
- Autorité compétente : AGRASC (gel/saisie/confiscation), sous procédure judiciaire.
- Réalisable si infraction qualifiée et procédure ouverte.

SOURCES
- DVF data.gouv.fr
- Registre foncier (consultation)
- Pappers (SCI)
```

#### Erreurs fréquentes

- **Confondre détenteur juridique et UBO.** Une SCI détient ; l’UBO contrôle la SCI.
- **Estimer la valeur sans source.** Mention explicite de la méthode et de la source.
- **Considérer un bien comme « confiscable » sans procédure.** L’asset recovery exige un cadre judiciaire.

#### Limites

L’estimation de la valeur est **indicative**. Les biens à l’étranger (Dubaï, Beyrouth, Genève) ne sont pas accessibles avec la même précision que les biens français.

#### Lien avec le fil rouge

> **CLEARFLOW — Cartographie patrimoniale**
> 
> Nassim identifie 11 actifs significatifs : 3 biens immobiliers à Paris (via SCI), 1 villa à Beyrouth (présomée, à confirmer), 1 yacht enregistré sous pavillon Malte (présent dans presse), 2 véhicules de luxe immatriculés à Paris, 4 participations dans des sociétés non encore consolidées dans la cartographie. Le total estimé : environ 18 M€ pour les actifs visibles français + 6 à 12 M€ pour les actifs étrangers présumés. À comparer aux revenus déclarés français (à obtenir via DGFiP).

#### Points clés à retenir

- Fiche actif : un bien, un livrable.
- Distinguer détenteur juridique et UBO.
- Estimation de valeur sourcée.
- Préparer l’éventuel asset recovery par juridiction.

-----

### Chapitre 31 — Graphes relationnels FININT

#### Objectif du chapitre

Comprendre la **représentation graphique** d’un réseau financier : nœuds (personnes, entités, actifs, flux), arcs (liens typés), et les usages opérationnels de cette représentation.

#### Le concept

Un graphe relationnel FININT est une représentation visuelle d’un réseau. Les **nœuds** sont des entités (personnes, sociétés, comptes, actifs, transactions). Les **arcs** (ou arêtes) sont les liens (capital, mandat, virement, propriété, etc.).

Les arcs sont typés : capital, mandat, paiement, propriété, parenté, adresse partagée. Chaque type a sa logique et son intensité.

**Outils** :

- **Maltego** : référence pour l’OSINT et le FININT, transforms multiples.
- **i2 Analyst’s Notebook** : standard du renseignement, lourd mais puissant.
- **Linkurious** : web-based, neo4j-backed, professionnel.
- **Gephi** : open source, analytique (centralités, communautés).
- **Graphistry** : web-based, GPU-accelerated, exploration interactive.
- **Neo4j** : base de données graphe sous-jacente.
- **Outils intégrés à Sayari, Orbis, Dow Jones** : graphes pré-construits sur leur référentiel.

#### L’utilité opérationnelle

Le graphe permet :

- **Détection de patterns** : clusters, structures en étoile, chaînes longues, ponts.
- **Identification de nœuds centraux** : qui est le « hub » du réseau ? — souvent l’UBO réel.
- **Détection de liens cachés** : ponts entre clusters apparemment indépendants.
- **Présentation visuelle** : un graphe bien construit communique en quelques secondes ce qui exige des pages de description.

#### Méthode — construire un graphe FININT

1. **Définir le périmètre** : périmètre initial (entités cibles), puis périmètres d’extension.
1. **Choisir les types de nœuds et d’arcs** :
- Nœuds : personnes, sociétés, comptes bancaires, adresses physiques, actifs significatifs, transactions clés.
- Arcs : capital (avec %), mandat (avec rôle), UBO (avec niveau de confiance), virement (avec montant et date), parenté (conjoint, enfant, fratrie), adresse partagée, employeur, contact réseau social.
1. **Charger les données** depuis les fiches (Ch.27-30) et les sources.
1. **Annoter** : libeller chaque arc avec son type, sa date, son intensité.
1. **Calculer des métriques** quand pertinent : centralité (degré, betweenness), communautés (Louvain), shortest paths.
1. **Itérer** : enrichir, déplacer, simplifier pour lisibilité.

#### Mini-walkthrough — graphe CLEARFLOW (description)

Le graphe central du dossier Haddad compte ~40 nœuds (14 sociétés, 12 personnes physiques, 11 actifs, et quelques nœuds techniques de transaction). Une fois construit dans Linkurious avec les liens typés, les patterns suivants émergent visuellement :

- **Cluster français** (4 SAS + dirigeants prête-noms probables) — fortement connecté en interne, faiblement à l’extérieur sauf via 1 arc capital vers le cluster chypriote.
- **Cluster chypriote** (NEXUS HOLDINGS + trust OMEGA) — au sommet, avec arc UBO probable vers Karim Haddad.
- **Cluster émirats / asiatique** (sociétés free zone, contacts à Dubaï) — autour de M. Y (PSC des Limited UK).
- **Branche Liban** — entités libanaises, faiblement visible mais positionnée à l’origine.
- **Branche Afrique de l’Ouest** (Bénin, Côte d’Ivoire) — débouchés opérationnels.
- **Karim Haddad** au centre : nœud de plus haute centralité dans le graphe (intuition confirmée par calcul de betweenness).

Cette représentation, présentée en réunion, communique en quelques secondes ce que 30 pages de note racontent.

#### Erreurs fréquentes

- **Graphe trop chargé** : illisible. Limiter à 30-50 nœuds visibles à la fois.
- **Arcs non typés** : ambiguïté.
- **Pas de date** : un lien actuel et un lien obsolète sont traités à l’identique.
- **Confondre forte connexité et causalité** : un nœud central peut être un facilitateur, pas un contrôleur.

#### Limites

Le graphe **résume** ; il ne **prouve** pas. Une représentation peut renforcer une hypothèse erronée si les nœuds sont mal qualifiés. Il doit accompagner une analyse écrite, jamais la remplacer.

#### Lien avec le fil rouge

> **CLEARFLOW — Le graphe en réunion de bilan**
> 
> Lors de la réunion de bilan du dossier, Nassim présente le graphe en première intention. En 2 minutes, le coordinateur et les collègues comprennent la structure du réseau, l’architecture du contrôle, et les zones d’incertitude. Le graphe accompagne la note dans le dossier transmis au PNF.

#### Points clés à retenir

- Graphe = représentation, pas preuve.
- Nœuds + arcs typés + dates + niveaux de confiance.
- Outils : Maltego, i2, Linkurious, Gephi, Graphistry.
- Métriques utiles : centralité (qui est central ?), communautés (clusters ?).

-----

### Chapitre 32 — Distinguer lien faible, lien fort et contrôle réel

#### Objectif du chapitre

Calibrer la **force des liens** dans un graphe FININT — éviter de surinterpréter une coïncidence comme un lien fort, et inversement de sous-estimer un lien faible qui s’avère structurant.

#### Le concept

Tous les liens ne se valent pas. Trois catégories :

**Lien faible** — coïncidence, adresse partagée, employeur commun lointain dans le temps, nom de famille identique (sans confirmation de parenté), interactions distantes sur réseaux sociaux. Niveau de confiance : *possible* à *probable* selon contexte. À documenter mais à manier avec prudence.

**Lien fort** — lien capital (>10 %), mandat conjoint (siéger ensemble dans un CA), virement direct récurrent, parenté avérée, conjoint, association professionnelle active, présence dans le même leak avec contexte similaire. Niveau de confiance : *probable* à *quasi-certain*.

**Contrôle réel** — UBO identifié *quasi-certain*, settlor de trust contrôlant les flux, dirigeant exécutif effectif. Distinct du lien fort : implique une **direction**.

#### L’utilité opérationnelle

Un graphe avec lien typé en force permet de :

- **Hiérarchiser** : qui est central vs périphérique.
- **Calibrer les hypothèses** : un lien fort soutient une attribution, un lien faible une simple suggestion.
- **Identifier les liens manquants** : où devrais-je trouver un lien et n’en trouve pas (peut signaler une zone d’opacification).
- **Détecter les liens cachés** : un lien faible récurrent dans plusieurs angles (LinkedIn + adresse + leak) devient fort par cumul.

#### Méthode — qualifier la force d’un lien

Pour chaque lien :

1. **Quelle est la source** ? (registre = fort ; presse = à recouper ; réseau social = variable ; leak = fort si authentique).
1. **Combien de recoupements indépendants** ? (1 source = à confirmer ; 2 sources indépendantes = probable ; 3+ = quasi-certain).
1. **Quelle est la nature du lien** ? (capital > mandat > parenté > adresse > présence partagée).
1. **Quelle est l’intensité dans le temps** ? (récent et durable > ancien ou ponctuel).
1. **Est-ce dans la même direction** que d’autres liens ? (cohérence d’un faisceau).

#### Mini-walkthrough — lien Haddad / Mme Z

- Source initiale : Mme Z est présidente d’une SAS du réseau (lien fort de mandat).
- Recoupement 1 : article de presse libanaise 2018 mentionne Mme Z lors d’un événement caritatif organisé par K. Haddad (lien fort de coreligionnaire).
- Recoupement 2 : photos LinkedIn 2022 montrent Mme Z et K. Haddad à un événement professionnel à Paris (lien fort de présence).
- Recoupement 3 : adresse domicile commune dans une ancienne année (registre foncier) — *quasi-certain* d’une cohabitation passée à un certain moment.

Calibration : lien personnel et professionnel fort entre K. Haddad et Mme Z, *quasi-certain*. Mais cela ne fait pas de Mme Z une prête-nom : elle pourrait être collaboratrice de confiance, partenaire dans certaines activités, ou amie. La nature exacte du lien (financier, amical, romantique) est *indéterminable* par OSINT seul.

#### Mini-walkthrough — lien faible mal interprété

Un analyste novice repère : K. Haddad et M. P étaient employés de la même entreprise en 2002 (LinkedIn). Tentation : « lien historique ». Calibration : *possible* mais lien faible — beaucoup de personnes ont travaillé pour les mêmes employeurs sans être en relation. Sans recoupement, ne pas mentionner comme un fait structurant.

#### Erreurs fréquentes

- **Surinterpréter un lien faible** : tirer une hypothèse forte d’une coïncidence.
- **Sous-estimer un cumul de liens faibles** : 4 ou 5 indices faibles convergents valent un lien probable.
- **Confondre lien fort et contrôle** : co-présence dans un CA = lien fort mais ne dit pas qui contrôle.

#### Limites

La force d’un lien n’est jamais binaire. C’est une **calibration**, pas un classement.

#### Lien avec le fil rouge

> **CLEARFLOW — Mme Z et le réseau**
> 
> Le lien Haddad / Mme Z, fort par cumul, alimente l’hypothèse que Mme Z est une présidente nominale agissant pour le compte de Haddad (mais avec autonomie et lien personnel — différent d’un prête-nom anonyme). Cette qualification nuancée se retrouve dans la fiche personne Mme Z, dans la fiche société de la SAS qu’elle préside, et dans la note finale.

#### Points clés à retenir

- Lien faible / lien fort / contrôle réel : trois catégories à distinguer.
- Calibrer par : source, recoupements, nature, durée, cohérence.
- Cumul de liens faibles convergents = potentiellement un lien fort.
- Lien fort ≠ contrôle automatique.

-----

### Chapitre 33 — Échelle de confiance WEP et hypothèses calibrées

#### Objectif du chapitre

Formaliser et appliquer l’**échelle de confiance** inspirée des **Words of Estimative Probability** (WEP) pour calibrer toutes les conclusions d’une note FININT. C’est la discipline qui distingue un livrable professionnel d’un texte affirmatif sans nuance.

#### Le concept

Les WEP sont une convention sémantique pour exprimer la confiance d’une affirmation. Origine : Sherman Kent, CIA, années 1960 — repris dans le renseignement civil et militaire et adapté en FININT.

**Échelle utilisée dans ce cours** :

|Niveau               |Plage  |Quand l’utiliser                                                           |
|---------------------|-------|---------------------------------------------------------------------------|
|**Quasi-certain**    |> 95 % |Multi-sources indépendantes, documents probants, recoupements convergents. |
|**Très probable**    |80-95 %|Plusieurs sources concordantes, hypothèses alternatives faibles.           |
|**Probable**         |60-80 %|Indices convergents mais incomplets, hypothèses alternatives moins fortes. |
|**Possible**         |40-60 %|Compatibilité avec les éléments, mais hypothèses alternatives équivalentes.|
|**Peu probable**     |15-40 %|Compatibilité faible, hypothèses alternatives dominantes.                  |
|**Très peu probable**|< 15 % |Quasi-exclusion.                                                           |
|**Indéterminable**   |n/a    |Données insuffisantes pour calibrer.                                       |

Cette échelle est utilisée systématiquement dans le cours, les fiches, les cas pratiques, la note FININT et les annexes.

#### L’utilité opérationnelle

Cinq usages :

1. **Discipline analytique** : forcer l’analyste à se demander, pour chaque conclusion, *« quelle est la solidité réelle de ce que j’écris ? »*.
1. **Communication précise** : le lecteur (magistrat, comité, partenaire) sait à quel point il peut s’appuyer sur chaque élément.
1. **Honnêteté épistémique** : ne pas faire semblant de savoir ce qu’on ne sait pas.
1. **Calibration des actions** : un gel d’avoirs sur la base d’un *quasi-certain* n’est pas la même décision qu’un signalement sur la base d’un *probable*.
1. **Comparabilité** : entre analystes, entre dossiers, entre périodes.

#### Méthode — calibrer une conclusion

1. **Identifier les sources** qui soutiennent la conclusion.
1. **Identifier les sources qui la contredisent** ou la nuancent.
1. **Identifier les hypothèses alternatives** : que d’autres explications restent compatibles avec les éléments ?
1. **Évaluer la solidité** : robustesse des sources, recoupements indépendants, cohérence avec le reste du dossier.
1. **Choisir le niveau** dans l’échelle.

#### Mini-walkthrough — calibration progressive

Hypothèse : *« Karim Haddad est l’UBO réel de NEXUS TRADING SAS (France) »*.

**Étape 1** : seul élément initial — chaîne de capital remonte à NEXUS HOLDINGS LTD (CY).
→ Calibration : *indéterminable* sur Haddad spécifiquement.

**Étape 2** : ajout du hit Pandora — settlor du trust OMEGA = Karim Haddad.
→ Calibration : *probable*. La chaîne est plausible mais formelle ; le contrôle effectif n’est pas démontré.

**Étape 3** : ajout des analyses de flux — Haddad reçoit personnellement des fonds en sortie du réseau et signe des opérations critiques.
→ Calibration : *très probable*.

**Étape 4** : coopération Mokas confirme la qualité de bénéficiaire principal de Haddad dans le trust, et témoignage du trustee si obtenu.
→ Calibration : *quasi-certain*.

À chaque étape, l’évolution de la calibration est documentée. La note finale présente la calibration *finale*, mais les annexes peuvent retracer l’évolution pour transparence.

#### Erreurs fréquentes

- **Utiliser un vocabulaire affirmatif sans calibration** : « c’est l’UBO », « il blanchit » — sans support, c’est faux ou exposé à contestation.
- **Sur-calibrer** par excès de prudence : tout est *possible* — devient ininterprétable.
- **Sous-calibrer** par enthousiasme : tout est *quasi-certain* — fait perdre la crédibilité.
- **Confondre absence de preuve et preuve d’absence** : si on ne trouve pas un élément, ce n’est pas qu’il n’existe pas — peut-être qu’on n’a pas la bonne source.

#### Limites

L’échelle WEP est une convention sémantique, pas une mesure objective. La calibration reste un **jugement informé**. Deux analystes peuvent diverger légèrement sur le niveau — c’est attendu et acceptable, à condition que chacun **justifie** son choix.

#### Lien avec le fil rouge

> **CLEARFLOW — Calibration systématique**
> 
> La note finale du dossier Haddad utilise systématiquement l’échelle WEP. Exemple d’extrait : *« La qualification de NEXUS DELAWARE LLC comme société écran de transit à finalité d’opacification est probable. La qualification de la finalité illicite (blanchiment) est possible à ce stade et nécessiterait, pour être qualifiée probable, la confirmation par audition de bénéficiaires de fonds et expertise comptable. La qualification du rôle de M. X comme prête-nom est probable. La qualification de K. Haddad comme UBO réel du réseau est très probable. »*

#### Points clés à retenir

- WEP : quasi-certain > très probable > probable > possible > peu probable > très peu probable > indéterminable.
- Utiliser systématiquement, dans fiches, notes, cas pratiques.
- Calibration = jugement informé, à justifier.
- Permet honnêteté, communication, discipline analytique.

-----

## PARTIE VI — ANALYSE DE FLUX ET COMPTABILITÉ FORENSIQUE

*Six chapitres pour passer de la lecture brute des relevés et bilans à une analyse structurée — détecter les anomalies, reconstituer les schémas, qualifier la cohérence économique, reconstituer le patrimoine.*

-----

### Chapitre 34 — Lire un relevé bancaire

#### Objectif du chapitre

Maîtriser la **lecture analytique d’un relevé bancaire** — au-delà de la simple consultation. Le chapitre 9 a posé la structure du relevé ; ici, on développe les techniques d’analyse en profondeur.

#### Le concept

Un relevé bancaire est une **série temporelle d’opérations**. Le lire analytiquement revient à le traiter comme un **dataset** : structurer les données, calculer des indicateurs, repérer des patterns, comparer à des références (sectorielles, historiques, comportementales).

#### Les passes d’analyse (approfondissement chapitre 9)

**Passe 1 — Profilage statistique global.**

Indicateurs clés à calculer :

- Nombre total d’opérations sur la période.
- Volume crédité, volume débité, ratio.
- Solde moyen, médian, maximum, minimum.
- Nombre de contreparties uniques.
- Top 5, 10, 20 des contreparties (entrants et sortants).
- Distribution des montants : nombre d’opérations par tranche (< 1 K€, 1-10 K€, 10-50 K€, 50-100 K€, > 100 K€).
- Saisonnalité : opérations par jour de la semaine, par heure, par mois.

Outils : tableur Excel ou LibreOffice, ou pandas (Python) pour les gros volumes.

**Passe 2 — Concentration et asymétrie.**

- Concentration : si les top 5 contreparties représentent > 70 % du volume, le compte est *concentré* — atypique pour la plupart des comptes personnels.
- Asymétrie crédit/débit : un compte qui reçoit beaucoup mais peu sortant accumule la valeur ; un compte qui passe (entrant = sortant en cycle court) est un compte de **transit**.
- Cycles : entrée 100 K€, sortie 95-99 K€ dans les 48h — pattern de transit.

**Passe 3 — Vue temporelle.**

- Activité par mois : pics, creux.
- Détection de **ruptures de comportement** : avant/après un événement (changement d’activité, début ou fin d’une fraude).
- Saisonnalité cohérente avec le secteur ? (un commerce saisonnier a un profil annuel marqué).

**Passe 4 — Contreparties.**

- Identification des principales contreparties : sociétés (croisement registres), particuliers, comptes propres.
- Nouvelles contreparties (n’apparaissant pas dans l’historique antérieur).
- Contreparties géographiquement incohérentes.
- Contreparties dans des juridictions à risque (chapitre 10).

**Passe 5 — Libellés et références.**

- Mots clés vagues : « services », « avance », « régularisation », « paiement », « contractuel ».
- Libellés répétés à l’identique sur plusieurs flux.
- Libellés faisant référence à des factures (chercher les factures correspondantes).
- Absence de libellé ou libellé pauvre.

**Passe 6 — Cohérence économique.**

- Flux compatible avec l’activité ?
- Ratios sectoriels respectés ?
- Transferts au dirigeant (compte personnel) en proportion raisonnable ?

#### Méthode — workflow type

Sur un relevé d’1 an, environ 3000-5000 lignes pour une PME active :

1. **Import** dans tableur ou pandas.
1. **Nettoyage** : harmonisation des libellés, parsing des montants.
1. **Catégorisation** : assigner chaque opération à une catégorie (CA encaissé, achats fournisseurs, salaires, charges fiscales, virements intra-groupe, dividendes, frais bancaires, prélèvements perso).
1. **Tableau de synthèse** : volume par catégorie, ratio, évolution.
1. **Tableau des contreparties** : top 20 en entrée, top 20 en sortie.
1. **Détection d’anomalies** : opérations sortant des patterns habituels.
1. **Annotation** : signaux faibles documentés.

#### Mini-walkthrough — relevé NEXUS TRADING SAS

Année 1 (1er exercice clos), compte principal :

- 1 421 crédits = 4,2 M€.
- 1 826 débits = 4,1 M€.
- Solde moyen 87 K€, max 542 K€.
- Top 5 entrées : 73 % du volume (4 sociétés étrangères + 1 compte personnel inconnu).
- Top 5 sorties : 51 % du volume (3 sociétés du réseau + 2 comptes personnels).

Vue temporelle : 3 pics d’activité en mars, juin, octobre — chaque pic précède de quelques jours un transfert vers la Suisse. Pattern de **cycles**.

Libellés : 75 % vagues, 22 % faisant référence à des factures non identifiables, 3 % explicites mais douteux.

Cohérence : la SAS déclare une activité de négoce de matériel agricole. Aucun fournisseur de matériel agricole identifié parmi les contreparties (entrants ou sortants). Aucun client final identifié. La SAS apparaît comme un compte de **pure intermédiation**, avec activité économique réelle non démontrée.

Hypothèses : transit financier (probable), TBML (possible à probable), pure structure d’opacification (probable).

#### Erreurs fréquentes

- **Lire ligne à ligne sans agrégation préalable.** L’analyste se perd.
- **Ignorer les frais bancaires** : ils racontent une histoire (volume d’opérations, opérations rejetées, descouverts).
- **Sous-estimer la temporalité** : un même montant à un mois différent peut être un signal différent.

#### Limites

Le relevé seul ne suffit jamais. Il faut croiser avec : comptes annuels, libellés détaillés (parfois enrichis par réquisition), correspondance entre flux et factures (chapitre 38), réquisitions des contreparties.

#### Lien avec le fil rouge

> **CLEARFLOW — Analyse système des relevés**
> 
> Nassim consolide les analyses des relevés des 4 SAS françaises. Cumulés, ces relevés couvrent ~5 600 opérations sur 18 mois, ~22 M€ de volume crédit, 16 M€ vers l’étranger. La signature globale : système de **transit multi-comptes avec cycles** intra-groupe, sortie principale vers Suisse et destinations offshore. Activité commerciale réelle douteuse. Sous réserve de coopération internationale pour les contreparties étrangères.

#### Points clés à retenir

- Relevé bancaire = série temporelle à traiter comme dataset.
- 6 passes d’analyse : profil, concentration, temps, contreparties, libellés, cohérence.
- Catégoriser, agréger, comparer.
- Tout pattern doit être confronté à l’activité économique réelle.

-----

### Chapitre 35 — Reconstituer des flux financiers

#### Objectif du chapitre

Passer de la lecture d’un compte isolé à la **reconstitution d’un schéma multi-comptes** — suivre l’argent à travers plusieurs banques, plusieurs juridictions, plusieurs entités, pour comprendre l’organisation d’ensemble.

#### Le concept

La reconstitution de flux consiste à **enchaîner les opérations** pour montrer le parcours de la valeur. Elle peut se faire dans deux directions :

- **Forward tracing** : partant d’une opération initiale, suivre où va l’argent.
- **Backward tracing** : partant d’une opération finale, remonter à l’origine.

Idéalement, les deux sont combinées pour valider mutuellement les chaînes.

#### L’utilité opérationnelle

Reconstituer les flux permet :

- Identifier l’**origine probable** des fonds (infraction prédécesseur en blanchiment).
- Identifier la **destination finale** (UBO bénéficiaire, intégration dans l’économie légale).
- Identifier les **points de passage critiques** (banques, juridictions, sociétés).
- Identifier les **techniques de layering** (fractionnement, complexification, conversion).
- Quantifier le volume total et le ventiler.

#### Méthode — workflow

1. **Identifier les comptes accessibles** : DS, réquisitions, EAR/CRS pour les comptes étrangers (en CRF).
1. **Construire un tableau de flux** : pour chaque opération, donneur, bénéficiaire, montant, devise, date, libellé, rail.
1. **Identifier les liens entre opérations** : opération A débite le compte 1 vers le compte 2, opération B (1-3 jours après) débite le compte 2 vers le compte 3, etc.
1. **Constituer des séquences** : chaîne d’opérations chronologiquement et économiquement liées.
1. **Construire le graphe de flux** : nœuds = comptes (ou entités), arcs = flux pondérés par montant.
1. **Calculer les agrégats** : total entré, total sorti, perte en route (différence = frais ou paiements masqués).

#### Walkthrough — séquence de transit

```
Schéma observé (sur 14 mois)

Société Y (Émirats) ──[3,8 M€ via 18 SWIFT MT103]──> SAS A (France)
SAS A (France) ──[3,2 M€ via 24 SCT vers]──> Sociétés liées du groupe
SAS A (France) ──[420 K€ via SCT Inst]──> Comptes personnels (M. X et liés)
SAS A (France) ──[300 K€ via 5 SWIFT MT103]──> Banque privée Suisse (compte K. Haddad présumé)

Détail temporel : entrées concentrées en début de mois, sorties dans les 7 jours.
```

Lecture FININT : le profil est compatible avec un **schéma de transit avec rétention de marge minimale** et **dilution dans le réseau** + **prélèvements personnels**. Le solde net de la SAS reste faible (~100 K€), cohérent avec un compte de passage.

Hypothèses : TBML (probable), corruption avec rétrocommissions (possible), simple optimisation fiscale agressive (peu probable seul à expliquer le schéma).

#### Erreurs fréquentes

- **Ne suivre qu’un sens.** Toujours combiner forward et backward.
- **Ignorer les frais bancaires** : ils peuvent expliquer une partie de la perte en route.
- **Confondre transit et accumulation** : un compte peut être les deux selon les périodes.
- **Sur-attribuer une intention.** Un schéma de transit peut être légitime (intermédiation commerciale réelle).

#### Limites

La reconstitution exige l’accès aux relevés détaillés de **chaque compte** dans la chaîne. Sans coopération internationale, des maillons restent inaccessibles, donc des hypothèses non confirmées.

#### Lien avec le fil rouge

> **CLEARFLOW — Reconstitution globale**
> 
> Nassim, après 5 semaines, produit une cartographie des flux du dossier Haddad : sur 18 mois, ~22 M€ entrants dans le réseau (origine multi-juridictionnelle), ~16 M€ sortants vers l’étranger, ~6 M€ stationnés ou consommés (dépenses, immobilier, autres). Sur les 22 M€ entrants, l’origine reste partiellement floue : ~12 M€ proviennent de sociétés du même groupe (transit interne sans origine externe identifiée pour cette portion), ~10 M€ proviennent de tiers commerciaux dont la réalité économique reste à confirmer (TBML probable). C’est cette analyse qui structure la note finale.

#### Points clés à retenir

- Forward + backward tracing combinés.
- Tableau de flux structuré, graphe de flux pondéré.
- Quantifier les totaux et les pertes en route.
- Identifier les techniques de layering.

-----

### Chapitre 36 — Lire un bilan et un compte de résultat

#### Objectif du chapitre

Maîtriser la **lecture analytique** des documents comptables clés — bilan, compte de résultat, annexe — pour détecter cohérence et incohérence dans le profil économique d’une entreprise.

#### Le concept

Le **bilan** est une photo à une date : actifs (ce que l’entreprise possède) = passifs (ce qu’elle doit, y compris ses fonds propres).

Le **compte de résultat** est un flux sur une période : produits (revenus) − charges (coûts) = résultat.

L’**annexe** explicite, contextualise, détaille.

#### Lecture du bilan

**Actif** :

- **Immobilisations** : incorporelles (fonds de commerce, brevets), corporelles (terrains, bâtiments, matériel), financières (participations, prêts).
- **Actif circulant** : stocks, créances clients, autres créances, trésorerie.

**Passif** :

- **Capitaux propres** : capital social, réserves, report à nouveau, résultat de l’exercice.
- **Provisions pour risques et charges**.
- **Dettes** : emprunts bancaires, dettes fournisseurs, dettes fiscales et sociales, dettes diverses.

Indicateurs clés :

- **Ratio d’endettement** = dettes / fonds propres. Un ratio très élevé peut signaler une fragilité ; très faible peut signaler une accumulation atypique.
- **Liquidité** = actif circulant / dettes à court terme.
- **Capacité d’autofinancement** : produit la capacité de l’entreprise à financer ses investissements et son remboursement de dette.

#### Lecture du compte de résultat

**Produits** :

- Chiffre d’affaires (ventes de marchandises, prestations de services).
- Production stockée et immobilisée.
- Subventions d’exploitation.
- Produits financiers, produits exceptionnels.

**Charges** :

- Achats consommés (matières premières, marchandises).
- Services extérieurs (sous-traitance, locations, honoraires, transports, etc.).
- Impôts et taxes.
- Charges de personnel (salaires, charges sociales).
- Dotations aux amortissements et provisions.
- Charges financières (intérêts), charges exceptionnelles.

**Soldes intermédiaires de gestion** :

- **Marge commerciale** = ventes − coût d’achat (pour les négoces).
- **Valeur ajoutée** = production de l’exercice − consommations en provenance des tiers.
- **EBE / Excédent Brut d’Exploitation** = VA − charges de personnel − impôts et taxes.
- **Résultat d’exploitation** = EBE − dotations.
- **Résultat courant avant impôts** = résultat d’exploitation + résultat financier.
- **Résultat net**.

#### L’utilité opérationnelle FININT

Les comptes annuels permettent à l’analyste :

- **Apprécier la cohérence sectorielle** : la marge, la productivité, l’intensité capitalistique sont-elles vraisemblables ?
- **Détecter les anomalies** : postes anormalement gonflés, charges récurrentes douteuses, créances clients fictives, stocks invraisemblables.
- **Évaluer la substance économique** : présence ou absence de moyens humains et matériels.
- **Comprendre la stratégie financière** : endettement, distribution de dividendes, conventions intragroupe.

#### Méthode — lecture rapide

1. **Vue d’ensemble** : taille (CA, total bilan), forme juridique, exercice, secteur.
1. **Ratios sectoriels** : marge commerciale, marge d’exploitation, productivité (CA/effectif), intensité capitalistique (immo/CA).
1. **Évolution** : sur 3 ans si disponibles — croissance, rupture, stabilité.
1. **Postes anormaux** : > 10 % de l’actif ou du résultat sans explication évidente.
1. **Annexe** : engagements hors bilan, conventions réglementées, événements postérieurs.

#### Mini-walkthrough — NEXUS TRADING SAS suite

Comptes 1er exercice :

- CA 12,4 M€, achats consommés 11,9 M€, marge commerciale 0,5 M€ (4 %).
- Charges de personnel 32 K€ (1 dirigeant, pas de salariés).
- Services extérieurs : 195 K€ (dont 140 K€ « conseil » à NEXUS HOLDINGS LTD CY).
- EBE : 273 K€.
- Résultat d’exploitation : 80 K€ (après dotations).
- Résultat financier : -8 K€ (frais bancaires SWIFT importants).
- Résultat net : 60 K€.

Bilan :

- Actif immobilisé : 12 K€ (équipement minimum).
- Actif circulant : 350 K€ (créances clients 280 K€, trésorerie 35 K€, autres 35 K€).
- Total actif : 362 K€.
- Capitaux propres : 70 K€ (capital 10 K€ + résultat).
- Dettes fournisseurs : 215 K€.
- Dettes fiscales et sociales : 25 K€.
- Comptes courants associés (NEXUS HOLDINGS CY) : 52 K€.

Lecture FININT : profil typique d’une **société d’intermédiation à très faible substance**. Charges de « conseil » à la holding chypriote représentent 70 % des services extérieurs — *probable* canal d’évasion de bénéfices vers la juridiction chypriote (à juridiction CRS, mais le levier de taxation peut être différent). Marge brute de 4 % cohérente avec intermédiation pure, ne tranche pas en soi. Le faible niveau d’immobilisations (12 K€) et l’absence de salariés signalent une coquille sans substance économique réelle propre.

#### Erreurs fréquentes

- **Lire les chiffres absolus** sans comparaison sectorielle ou ratiométrique.
- **Ignorer l’annexe** : conventions réglementées intragroupe, engagements, événements postérieurs y figurent.
- **Surinterpréter un seul exercice** : la cohérence se voit sur la trajectoire (3 ans+).

#### Limites

La comptabilité est **construite par l’entreprise** ; sans CAC, le contrôle externe est limité. Les comptes peuvent être falsifiés. Le forensique poussé exige un expert-comptable de formation forensique (chapitre 37).

#### Lien avec le fil rouge

> **CLEARFLOW — Analyse des 2 SAS publiantes**
> 
> Sur les 2 SAS françaises publiant des comptes, Nassim repère : pattern récurrent de charges de conseil à des entités liées (15-25 % du résultat brut diverté vers Chypre par exercice), faible substance économique propre, profils de marge cohérents avec intermédiation mais non démontratifs d’une activité commerciale réelle. Cumulé avec l’analyse de flux, l’hypothèse de **structures de transit avec évasion de bénéfices** est *probable* à *quasi-certaine*.

#### Points clés à retenir

- Bilan = photo ; compte de résultat = flux ; annexe = explication.
- Indicateurs : marge, EBE, résultat, ratios.
- Cohérence sectorielle et évolution sur 3 ans : essentiels.
- L’absence de substance économique (faible immo, pas de salariés) est un signal fort.

-----

### Chapitre 37 — Détecter anomalies comptables et signaux faibles

#### Objectif du chapitre

Connaître les **anomalies comptables typiques** et les **signaux faibles** qui orientent vers une enquête approfondie : ventes fictives, charges fictives, prêts intragroupe sans contrepartie, ajustements de fin d’exercice douteux.

#### Le concept

Une anomalie comptable est un poste, un mouvement ou une présentation qui s’écarte de ce qu’on attendrait pour une entreprise du secteur et de la taille concernée. Elle peut être :

- **Innocente** : choix méthodologique légitime, particularité sectorielle.
- **Suspecte** : indice d’un schéma à investiguer.
- **Frauduleuse** : preuve, après recoupement, d’une falsification.

L’analyste FININT cherche d’abord à identifier la suspicion, pas à conclure à la fraude.

#### Familles d’anomalies courantes

**Côté revenus** :

- **Ventes fictives** : factures sans contrepartie réelle (marchandise, prestation). Détectables par : créances clients qui ne se règlent pas, croissance disproportionnée du CA, ventes à des clients sans existence vérifiable, marges anormalement élevées.
- **Cut-off** : décalage de la reconnaissance du revenu pour gonfler l’exercice (revenu reconnu en année N alors qu’il aurait dû l’être en N+1, ou inversement).
- **Vente fictive de stocks** entre entités liées pour gonfler les ventes.
- **Subventions non rapportées au bon exercice**.

**Côté charges** :

- **Charges fictives** : factures payées à des fournisseurs fictifs ou à des sociétés liées sans contrepartie réelle. Vecteur classique d’abus de biens sociaux (ABS — chapitre 43).
- **Charges de conseil** disproportionnées à des entités liées (signal d’évasion de bénéfices).
- **Voyages et frais de représentation** disproportionnés à l’activité.
- **Sous-traitance massive** sans personnel ni équipement chez le sous-traitant (chaîne fictive).

**Côté bilan** :

- **Créances clients gonflées** : créances qui restent en bilan sans recouvrement (cachent une absence de revenu réel).
- **Stocks invraisemblables** : volumes ou valeurs sans rapport avec l’activité.
- **Provisions douteuses** : sur-provisionnement ou sous-provisionnement pour modeler le résultat.
- **Prêts intragroupe** : si faits sans intérêts, sans documentation, sans remboursement, signal de transfert occulte de valeur.
- **Compte courant d’associé** anormalement gros (le dirigeant a prêté ou retiré beaucoup).

**Présentation et publication** :

- **Comptes publiés en retard récurrent**.
- **Confidentialité demandée alors que la société dépasse les seuils**.
- **Changement de cabinet de CAC** sans justification claire.
- **Réserves dans le rapport du CAC**.

#### L’utilité opérationnelle

Détecter les anomalies oriente :

- La typologie probable du schéma (ABS, fraude fiscale, évasion, blanchiment).
- Les pièces à demander en réquisition (factures sous-jacentes, contrats, ordres de virement).
- Les acteurs à profiler (commissaire aux comptes, expert-comptable, dirigeants).

#### Méthode — protocole de détection

1. **Comparer les ratios** sectoriels et historiques.
1. **Examiner les postes principaux** ligne par ligne pour les postes représentant > 5 % du total.
1. **Lire systématiquement l’annexe**.
1. **Identifier les conventions réglementées** (transactions avec parties liées).
1. **Confronter avec les flux observables** (relevés bancaires).
1. **Documenter les signaux** dans la fiche société (chapitre 28).

#### Mini-walkthrough — anomalies NEXUS TRADING

- Charges de conseil à NEXUS HOLDINGS LTD CY = 140 K€ sur l’exercice. Disproportionné pour une SAS de 12,4 M€ de CA avec un seul dirigeant. Convention réglementée à l’origine ? Service réel rendu ? *Probable* signal de transfert de bénéfices vers la juridiction chypriote.
- Créances clients = 280 K€, soit ~30 jours de CA. Niveau normal pour le négoce. Pas d’anomalie ici.
- Compte courant associé NEXUS HOLDINGS CY = 52 K€. Faible niveau, pas alarmant.
- Stocks = 0 €. Cohérent avec intermédiation pure.

Signal principal : **les charges de conseil**. *Probable* mécanisme d’évasion de bénéfices vers la holding chypriote, à investiguer (substance des prestations, contrats sous-jacents).

#### Erreurs fréquentes

- **Considérer une anomalie comme une preuve.** L’anomalie est un signal d’investigation, pas une preuve.
- **Ignorer la perspective sectorielle.** Certaines anomalies apparentes sont des pratiques sectorielles courantes.
- **Ne pas chercher l’explication légitime** avant de conclure à la fraude.

#### Limites

Le détecteur d’anomalies suppose une connaissance sectorielle ; sans elle, l’analyste risque d’attribuer une anomalie là où il n’y en a pas, ou inversement.

#### Lien avec le fil rouge

> **CLEARFLOW — Signaux comptables consolidés**
> 
> Sur l’ensemble du réseau Haddad, Nassim recense 8 anomalies comptables convergentes : charges de conseil intragroupe disproportionnées (3 SAS), prêts intragroupe sans intérêts (5 entités), créances clients structurellement non recouvrées (1 SAS), absence systématique de stocks pour entités déclarées en négoce (4 SAS). Cumulés, ces signaux constituent un faisceau convergent de *probable* schéma d’évasion de bénéfices et de transferts intragroupe non justifiés économiquement.

#### Points clés à retenir

- Anomalies = signaux d’investigation, jamais preuves seules.
- Familles : ventes fictives, charges fictives, postes de bilan douteux, présentation.
- Comparaison sectorielle + cohérence avec flux = clés.
- Conventions réglementées et annexe sont des mines d’information.

-----

### Chapitre 38 — Factures, marges, marchandises et cohérence économique

#### Objectif du chapitre

Maîtriser la **vérification de la cohérence économique** : confronter les flux financiers à la réalité opérationnelle attendue — marchandises, marges, factures, transport, logistique.

#### Le concept

Une fraude moderne (notamment TBML — chapitre 41) repose sur la **dissociation entre flux financier et flux physique**. Une facture peut être payée sans contrepartie réelle de marchandise ; une marchandise peut être surfacturée ou sous-facturée ; un transport peut être déclaré sans avoir lieu.

L’analyse de cohérence économique cherche à confronter :

- **Le flux financier déclaré** (virement, facture).
- **La marchandise présumée** (nature, quantité, valeur de marché).
- **La logistique attendue** (transport, douane, certificats).
- **La marge réalisée** (cohérence avec les pratiques sectorielles).

#### L’utilité opérationnelle

Pour de nombreux schémas, c’est l’analyse de cohérence économique qui **trahit la fraude**. Une facture intracommunautaire de 800 K€ pour une marchandise dont la valeur de marché est de 200 K€ est un signal fort.

#### Méthode — vérifier la cohérence

1. **Identifier la marchandise** (nature, quantité, qualité) via la facture, le contrat, les documents douaniers.
1. **Estimer la valeur de marché** : sources sectorielles, comparables, expertise.
1. **Vérifier la cohérence du prix** : sur-facturation ? sous-facturation ?
1. **Vérifier la logistique** : la marchandise a-t-elle été transportée ? Quels documents (CMR, BL, EUR1, certificats d’origine) ?
1. **Vérifier les contreparties** : le fournisseur et le client ont-ils l’activité, la capacité, les références pour cette opération ?
1. **Confronter avec les flux bancaires** : le paiement correspond-il en montant, en date, en parties ?

#### Sources de référence pour les valeurs de marché

- **Indices sectoriels** : matières premières (LME, ICE, CME), agricoles (Bourse de Chicago, Euronext Paris), énergie.
- **Statistiques douanières** : Eurostat Comext (UE), UN Comtrade, customs databases (CBP US).
- **Bases B2B** : Alibaba, plateformes sectorielles (prix indicatifs).
- **Expertise sectorielle** : cabinets spécialisés.

#### Mini-walkthrough — TBML avec sur-facturation

Cas type : une SARL française importe du matériel agricole d’occasion (tracteurs) depuis un fournisseur émirati.

- Facture : 8 tracteurs Massey Ferguson 5710 SL d’occasion, 95 000 € chacun, soit 760 K€.
- Valeur de marché de référence (occasion, modèles 2018-2020) : environ 35-45 K€ pièce, soit 280-360 K€ pour 8 unités.
- Sur-facturation apparente : environ × 2.
- Documents : CMR sommaire, certificats d’origine douteux (mise en cause par presse régionale).

Lecture FININT : profil compatible avec une **sur-facturation TBML** où le surplus payé (~400 K€) est en réalité une **rétrocession** vers le payeur ou un destinataire désigné. C’est un schéma classique pour transférer de la valeur sous couvert de commerce.

#### Erreurs fréquentes

- **Confondre prix sur facture et valeur réelle** : prendre la facture au pied de la lettre.
- **Ignorer les particularités sectorielles** : un matériel sur-spécifié peut être légitimement plus cher.
- **Conclure trop vite sans expertise** : la cohérence économique fine exige parfois un sectoriste.

#### Limites

La vérification de cohérence économique exige une **expertise sectorielle** ou un accès à des bases de prix. Sans cela, l’analyste se borne à signaler une probable anomalie et propose une expertise.

#### Lien avec le fil rouge

> **CLEARFLOW — Le marché ivoirien réexaminé**
> 
> Le marché public ivoirien de fourniture de matériel agricole remporté par NEXUS NEGOCE (Côte d’Ivoire) en 2023 pour 3,2 M€ peut être réexaminé : les types de tracteurs livrés (selon les documents publics ivoiriens) valent au marché européen environ 1,5 M€. Sur-facturation apparente : ×2. Compatible avec un schéma combinant favoritisme (marché remporté dans des conditions discutées) et sur-facturation (rétrocommissions probables). Le volet ivoirien est renvoyé en coopération internationale ; depuis la France, on documente la *probable* sur-facturation comme élément du faisceau.

#### Points clés à retenir

- Dissociation flux financier / flux physique = vecteur classique de fraude.
- Vérifier marchandise, valeur de marché, logistique, contreparties.
- Sur-facturation et sous-facturation = signaux TBML.
- Expertise sectorielle souvent requise pour la qualification fine.

-----

### Chapitre 39 — Reconstitution patrimoniale et train de vie

#### Objectif du chapitre

Reconstituer le **patrimoine d’une personne** : actifs visibles, actifs présumés, train de vie observable, et confronter cette reconstitution aux revenus déclarés. C’est l’une des analyses les plus délicates et les plus stratégiques du FININT.

#### Le concept

Le patrimoine d’une personne se compose :

- **Actifs immobiliers** : biens en France (DVF, Patrim) et à l’étranger.
- **Actifs financiers** : participations dans sociétés, comptes bancaires, portefeuilles.
- **Actifs mobiliers de valeur** : véhicules, bateaux, aéronefs, œuvres, bijoux, montres, instruments de collection.
- **Cryptos** : adresses on-chain — renvoi à OSINT Crypto pour l’analyse détaillée.
- **Train de vie observable** : voyages, dépenses visibles, écoles privées, événements.

La **reconstitution patrimoniale** consiste à inventorier l’ensemble, l’évaluer, et le confronter aux revenus déclarés.

#### L’utilité opérationnelle

La reconstitution patrimoniale sert à :

- **Détecter un train de vie incohérent** avec les revenus officiels.
- **Préparer l’asset recovery** : identifier les biens susceptibles de gel/saisie/confiscation.
- **Étayer les soupçons** d’enrichissement illicite (corruption, fraude fiscale, etc.).
- **Mesurer le préjudice** à la collectivité (en cas d’évasion fiscale, de corruption, etc.).

#### Méthode — workflow de reconstitution

1. **Lister les actifs visibles** : sources ouvertes — DVF, Patrim, registres divers, presse, SOCMINT.
1. **Identifier les actifs présumés** : signaux visibles (voyages réguliers à Dubaï = possible résidence ; voiture de luxe sur Instagram = bien à identifier ; etc.).
1. **Estimer les valeurs** : recherche prix de marché, sources spécialisées.
1. **Lister les revenus déclarés** : presse (pour les dirigeants publics), déclarations HATVP, comptes annuels des sociétés détenues, distribution de dividendes traçable.
1. **Confronter** : patrimoine identifié versus revenus déclarés. Écart ? Plausibilité d’un héritage ? Activités antérieures ?
1. **Documenter les lacunes** : actifs étrangers non vérifiés, comptes bancaires inaccessibles, etc.

#### Mini-walkthrough — patrimoine Haddad

Actifs visibles français :

- 3 biens immobiliers à Paris (SCI HADDAD INVESTISSEMENTS) : valeur estimée 11 M€.
- 2 véhicules de luxe (immatriculations parisiennes) : ~280 K€.
- Total France visible : ~11,3 M€.

Actifs présumés à l’étranger :

- Villa à Beyrouth (presse libanaise, photos) : valeur estimée 3-5 M€.
- Présence à Dubaï : appartement éventuel, non confirmé (~1-3 M€ si confirmé).
- Yacht (pavillon Malte, présence dans presse mondaine) : valeur estimée 4-7 M€.
- Participations dans le groupe Haddad : valorisation complexe (probablement 8-15 M€).
- Compte bancaire suisse présumé (DS) : montant non connu.
- Total présumé : 16 à 30 M€ (très large fourchette).

Train de vie observable :

- 4-6 voyages internationaux par an (Paris-Beyrouth-Dubaï-Genève).
- Événements professionnels et caritatifs fréquents.
- Réseau social haut de gamme.

Revenus déclarés (présomé sans accès aux déclarations fiscales) :

- Activité de dirigeant de Nexus Liban SAL et NEXUS INTERNATIONAL FZ.
- Plusieurs sources de revenus non publiques.

Estimation : le patrimoine total (France + étranger) est *probable* à **25-40 M€**. La cohérence avec les revenus déclarés sur 30 ans d’activité de négoce international est *possible* — un négoce international peut générer ces patrimoines légitimement. Cependant, la fraction *attribuée à des fonds d’origine illicite* serait à qualifier, *indéterminable* sans coopération internationale et accès aux déclarations.

Hypothèse : patrimoine global cohérent avec une activité réussie ; sa **construction multi-juridictionnelle opaque** est un signal de *probable* contournement fiscal et possiblement d’autres schémas, à confirmer.

#### Erreurs fréquentes

- **Sous-estimer le patrimoine étranger.** Beaucoup de patrimoines de personnes d’affaires internationales sont majoritairement à l’étranger.
- **Surinterpréter le train de vie.** Un train de vie élevé peut être financé par des sources légitimes (héritage, succès commercial réel).
- **Confondre disponibilité de l’information et absence.** Un patrimoine non visible n’est pas un patrimoine nul.

#### Limites

La reconstitution patrimoniale rigoureuse exige des sources fermées : déclarations fiscales, EAR/CRS pour les comptes étrangers, coopération internationale. En OSINT seul, on aboutit à des fourchettes larges et des hypothèses calibrées.

#### Lien avec le fil rouge

> **CLEARFLOW — Patrimoine et asset recovery**
> 
> Sur la base de la reconstitution, Nassim identifie 11 M€ d’actifs français saisissables en théorie (sous procédure judiciaire) et présume 16-30 M€ étrangers à confirmer. La note finale recommande au PNF d’envisager des mesures conservatoires sur les actifs français, et de solliciter la coopération internationale pour qualifier et localiser les actifs étrangers.

#### Points clés à retenir

- Reconstitution = actifs immobiliers + financiers + mobiliers + crypto + train de vie.
- Sources ouvertes (DVF, Patrim, registres) + SOCMINT + leaks.
- Confronter aux revenus déclarés et à la trajectoire professionnelle.
- Préparer l’asset recovery par juridiction.

-----

## PARTIE VII — TYPOLOGIES DE CRIMINALITÉ FINANCIÈRE

*Neuf chapitres pour comprendre, sous l’angle défensif et investigatoire, les principaux schémas de criminalité financière modernes. L’objectif est la détection, l’analyse et la coopération, jamais le mode d’emploi pour commettre.*

-----

### Chapitre 40 — Blanchiment : placement, empilement, intégration

#### Objectif du chapitre

Maîtriser le **cadre conceptuel** du blanchiment de capitaux : trois phases (placement, empilement, intégration), typologies courantes, signaux de détection. C’est la matrice de référence pour la majorité des dossiers FININT.

#### Le concept

Le **blanchiment de capitaux** est l’opération par laquelle une personne dissimule l’origine illicite de fonds pour les introduire dans l’économie légale.

Le modèle classique en **trois phases** (popularisé par le GAFI dans les années 1990, encore utile pédagogiquement même s’il simplifie la réalité) :

**1. Placement.** Introduire les fonds illicites dans le système financier. Mécanismes : dépôts en espèces (souvent fractionnés sous les seuils — *structuration* ou *smurfing*), achats en cash de biens revendables, conversions en cryptos, infiltration dans des activités à forte composante cash (restauration, hôtellerie, salons de coiffure, lavages auto, bars-tabacs). C’est la phase la plus risquée pour le blanchisseur car la plus visible.

**2. Empilement (layering).** Multiplier les opérations et les juridictions pour brouiller la traçabilité. Mécanismes : virements multiples entre sociétés écrans, conversions de devises, allers-retours bancaires, fragmentation par plusieurs PSP, layering crypto via mixers ou bridges, transit par des juridictions à secret bancaire. Le but : créer une distance entre l’origine et la destination.

**3. Intégration.** Réinjecter les fonds blanchis dans l’économie légale sous une forme apparemment légitime : achat immobilier, acquisition d’entreprises, investissements dans des actifs financiers, achats de luxe.

#### Évolution moderne du modèle

Le modèle trois phases simplifie la réalité 2020+. Les schémas modernes :

- **Combinent rapidement** placement et layering (BEC + fintechs + crypto en quelques heures).
- **Intègrent la crypto** comme rail de placement et de layering (renvoi OSINT Crypto).
- **S’appuient sur des structures juridiques** (sociétés écrans, trusts) plus que sur les espèces.
- **Exploitent les jeux d’argent en ligne** comme couche.
- **Utilisent les marchés de l’art, des NFT, des cartes de collection** comme moyens d’intégration.

#### L’utilité opérationnelle

L’analyste cherche à :

- **Identifier la phase** dans laquelle se situe une opération observée.
- **Reconstituer la chaîne** : retrouver le placement initial à partir des indices de layering ou d’intégration.
- **Qualifier l’infraction prédécesseur** (qu’est-ce qui a généré les fonds : trafic, fraude, corruption ?).

#### Méthode — signaux par phase

**Placement** : dépôts d’espèces fréquents et fractionnés, activité incohérente avec le compte, achats en cash de biens revendables, onboarding rapide sur PSP/EME avec activité immédiate inhabituelle.

**Layering** : cascades de virements en cycle court, multiplication des juridictions sans rationale, conversions multiples de devises, transferts en cascade entre fintechs, sorties crypto avec mixers ou bridges.

**Intégration** : acquisitions immobilières disproportionnées, investissements dans des sociétés sans expérience préalable, acquisitions d’œuvres d’art à prix élevés, importations de biens de luxe, donations à des organismes avec retours indirects.

#### Mini-walkthrough — schéma observable

Un trafiquant accumule 1 M€ en espèces. **Placement** : dépôts par 10-50 mules de 5-9 K€ chacun en plusieurs agences. **Layering** : virements vers une SAS écran, puis société émirate, conversion USDT, transferts entre exchanges, reconversion en EUR sur fintech. **Intégration** : achat d’un appartement à Paris via SCI.

L’analyste qui intervient à un point quelconque doit reconstituer en amont et en aval pour identifier infraction prédécesseur et bénéficiaire final.

#### Erreurs fréquentes

- **Considérer toute opération inhabituelle comme blanchiment.** Beaucoup ont des explications légitimes.
- **Ignorer la phase d’intégration** : c’est souvent la plus visible et la plus exploitable judiciairement.
- **Sous-estimer le rôle des assujettis non bancaires** : notaires, avocats, marchands d’art, agents immobiliers, casinos.

#### Limites

La qualification *« blanchiment »* est une qualification juridique qui exige une **infraction prédécesseur** établie. En FININT, on parle de **schéma compatible avec un blanchiment** et l’on transmet à l’autorité compétente.

#### Lien avec le fil rouge

> **CLEARFLOW — Phases observables**
> 
> Dans le dossier Haddad, les phases sont mélangées. Le **placement** apparaît marginal (peu de cash visible). Le **layering** est central (transit multi-juridictionnel via sociétés écrans). L’**intégration** apparaît dans les acquisitions immobilières françaises et présumées étrangères. L’infraction prédécesseur n’est pas clairement établie ; les hypothèses retenues : corruption autour des marchés ouest-africains (probable), évasion fiscale et fraudes diverses (possible).

#### Points clés à retenir

- Modèle GAFI : placement → layering → intégration.
- Évolution moderne : phases mélangées, accélérées, intégrant crypto.
- L’analyste identifie la phase et reconstitue en amont/aval.
- Qualification juridique de blanchiment exige l’infraction prédécesseur.

-----

### Chapitre 41 — Trade-Based Money Laundering (TBML)

#### Objectif du chapitre

Comprendre le **blanchiment par le commerce international (TBML)** — l’une des typologies les plus utilisées et les plus difficiles à détecter, car elle s’appuie sur des flux commerciaux qui paraissent légitimes.

#### Le concept

Le **TBML** est le blanchiment via des opérations commerciales internationales : import-export, achats-ventes de marchandises, prestations de service. La dissimulation passe par le **décalage entre valeur déclarée et valeur réelle** de la marchandise, ou par la **fictivité totale** de l’opération.

#### Mécanismes courants

**Sur-facturation** : la marchandise est vendue à un prix supérieur à sa valeur réelle. Le payeur transfère ainsi un montant supérieur, l’excédent étant un canal de valeur déguisé.

**Sous-facturation** : la marchandise est vendue à un prix inférieur. Permet de minimiser les droits de douane à l’import, ou de transférer de la valeur via revente à valeur réelle.

**Facturation multiple** : la même marchandise est facturée plusieurs fois à des entités liées.

**Marchandise fictive** : facture sans contrepartie physique.

**Documents falsifiés** : certificats d’origine, bills of lading, CMR, certificats douaniers — donnent une apparence légitime à des flux fictifs.

**Transit par juridictions complaisantes** : la marchandise passe (ou semble passer) par des free zones (Dubai, Singapour) pour brouiller la traçabilité.

**Triangulation** : achat dans un pays A, vente dans un pays C, transit par un pays B intermédiaire — opportunité de surcouches.

#### L’utilité opérationnelle

Le TBML est particulièrement difficile à détecter parce qu’il imite des opérations commerciales légitimes. La détection repose sur l’analyse fine de la cohérence économique (chapitre 38).

#### Méthode — signaux de TBML

- Marges sur-prix marché significatives.
- Décalages valeur facture / valeur de marché (Eurostat Comext, UN Comtrade, indices sectoriels).
- Contreparties commerciales sans activité réelle vérifiable.
- Pays de transit sans rationale économique.
- Documents douaniers incohérents (ports d’embarquement, dates).
- Paiements en avance disproportionnée par rapport aux pratiques sectorielles.
- Flux financiers déconnectés des flux physiques observables.

#### Mini-walkthrough — schéma TBML simplifié

Une société A en France importe « 200 tonnes d’huile de palme » depuis une société B au Bénin, payée 850 K€. La société B est facturée par une société C en Côte d’Ivoire pour 350 K€.

- Si la marchandise existe : marge B = 500 K€ — atypique pour le marché.
- Vérification douanière française : aucune trace d’import enregistré pour A à ces volumes.
- Vérification logistique : aucun transport identifié.

Hypothèse forte : opération **fictive ou sur-facturée**, le flux de 850 K€ ayant une finalité de transfert de valeur déguisée. Probable TBML.

#### Erreurs fréquentes

- **Confondre marge atypique et TBML.** Certains secteurs (luxe, technologies de pointe) ont des marges très élevées légitimement.
- **Conclure sans vérification physique** : la vérification douanière (existence du transport) est souvent la clé.
- **Sous-estimer le rôle des free zones** : la traçabilité y est moindre.

#### Limites

La détection fine du TBML exige souvent une coopération douanière internationale (OMD, douanes nationales). En CRF, cette coopération est mobilisable mais lente.

#### Lien avec le fil rouge

> **CLEARFLOW — TBML hypothèse centrale**
> 
> Dans le dossier Haddad, plusieurs éléments convergent vers une hypothèse TBML *probable* : sur-facturation apparente sur le marché ivoirien (×2), incohérences entre flux financiers et flux physiques pour les imports déclarés français depuis le Bénin, transit Bénin → France sans rationale logistique. La qualification précise exigerait coopération douanière française et ivoirienne, prévue dans les recommandations.

#### Points clés à retenir

- TBML = blanchiment via flux commerciaux internationaux.
- Mécanismes : sur/sous-facturation, facturation multiple, marchandise fictive, documents falsifiés.
- Détection : cohérence valeur, contreparties, logistique.
- Coopération douanière internationale souvent nécessaire.

-----

### Chapitre 42 — Corruption, commissions occultes et PEP

#### Objectif du chapitre

Comprendre les **schémas de corruption** transnationale : commissions occultes, pots-de-vin, rétrocommissions, et le concept de **PEP** (Personne Politiquement Exposée).

#### Le concept

La **corruption** est l’obtention d’un avantage en échange d’un acte illicite par une personne en position de pouvoir. Variantes :

- **Corruption active** (celui qui offre) et **passive** (celui qui reçoit).
- **Corruption nationale** vs **transnationale** (régie par les conventions OCDE 1997, ONU Mérida 2003, loi Sapin II 2016 en France).
- **Trafic d’influence** : intermédiaire facilitant l’obtention d’un avantage.
- **Concussion** : exigence d’une rémunération non due par un agent public.
- **Prise illégale d’intérêts** : cumul d’intérêts privés et de fonctions publiques.
- **Favoritisme** : avantage indu dans la commande publique.

**PEP — Personne Politiquement Exposée.** Catégorie LCB-FT définie par la 4e/5e directive AML. Recouvre :

- Chefs d’État et de gouvernement, ministres, parlementaires.
- Membres de cours suprêmes et cours constitutionnelles.
- Membres de la haute hiérarchie militaire.
- Dirigeants de partis politiques significatifs.
- Dirigeants d’entreprises publiques significatives.
- Dirigeants d’organisations internationales.
- **Membres de la famille proche** (conjoint, parents, enfants, beaux-parents).
- **Collaborateurs étroits connus** (associés, prête-noms).

Le statut PEP ne fait pas du PEP un criminel ; il **déclenche une vigilance renforcée** (KYC renforcé, monitoring spécifique).

#### Schémas typiques

- **Rétrocommissions sur marché public** : marché remporté à prix surévalué, partie reversée au décideur ou à un proche, via structure offshore.
- **Cadeaux et invitations** : voyages, séjours, biens — formes plus subtiles.
- **Pacte de corruption** : facture de « conseil » à une société écran contrôlée par le décideur ou un proche.
- **Société de couverture** : le décideur crée une société (par prête-nom) qui « facture » des prestations fictives au fournisseur bénéficiaire.
- **Trust avec bénéficiaires politiquement exposés** : fonds parqués dans un trust dont le PEP ou ses proches sont bénéficiaires.

#### L’utilité opérationnelle

L’analyste cherche à :

- **Identifier le PEP** ou son entourage (PEP famille, PEP collaborateur).
- **Repérer les flux atypiques** (entrées depuis fournisseurs publics vers comptes personnels ou de proches).
- **Documenter les liens** entre décideurs et entreprises bénéficiaires.
- **Croiser avec marchés publics** (chapitre 15) et HATVP en France.

#### Méthode — signaux de corruption

- Flux entrants depuis fournisseurs de la commande publique vers comptes personnels ou de proches.
- Sociétés de « conseil » dont l’activité réelle est inidentifiable, facturant des entités publiques ou semi-publiques.
- Acquisitions patrimoniales disproportionnées par des proches.
- Train de vie incohérent avec les revenus déclarés.
- Présence du décideur dans HATVP avec déclarations partielles ou contradictoires.

#### Mini-walkthrough

Un haut fonctionnaire signe régulièrement des marchés publics avec une PME. Cette PME, par convention, verse 5 % de chaque marché à une « société de conseil » domiciliée à Chypre, dont l’UBO est l’oncle du fonctionnaire.

Lecture FININT : pattern de rétrocommissions probable. Vérification : marchés publics gagnés (BOAMP, DECP), flux PME → société de conseil (réquisition), UBO de la société (registre, leaks), lien familial fonctionnaire-oncle (état civil, presse, SOCMINT). Si tous les éléments se confirment, schéma *quasi-certain*.

#### Erreurs fréquentes

- **Considérer toute relation PEP / entreprise comme corruption.** Beaucoup sont parfaitement légales.
- **Surinterpréter une déclaration HATVP partielle.** Peut être omission, pas nécessairement fraude.
- **Diaboliser le statut PEP** : ce n’est pas un soupçon, c’est une exigence de vigilance.

#### Limites

La corruption transnationale est notoirement difficile à prouver : témoignages réticents, juridictions étrangères, secret bancaire résiduel. Les dossiers FININT débouchent souvent sur des recommandations à des autorités spécialisées (PNF, OCDE Working Group on Bribery, Interpol).

#### Lien avec le fil rouge

> **CLEARFLOW — Volet corruption ivoirien**
> 
> Sur le volet du marché public ivoirien, l’hypothèse de **favoritisme avec corruption** est *possible* à *probable*. Sans coopération ivoirienne, l’établissement précis est *indéterminable*. La note finale recommande au PNF d’engager les coopérations nécessaires.

#### Points clés à retenir

- Corruption : variantes nombreuses (active, passive, trafic d’influence, favoritisme).
- PEP : statut déclencheur de vigilance, pas d’accusation.
- Schémas typiques : rétrocommissions, sociétés de couverture, trusts avec bénéficiaires PEP.
- Coopération internationale souvent indispensable.

-----

### Chapitre 43 — Fraude fiscale, carrousel TVA et abus de biens sociaux

#### Objectif du chapitre

Comprendre les **principales typologies de fraude fiscale** : fraude TVA (notamment carrousel), évasion fiscale internationale, et l’**abus de biens sociaux** (ABS).

#### Le concept

**Fraude fiscale** : ensemble des comportements visant à éluder l’impôt par dissimulation, fausses déclarations, montages fictifs.

**Carrousel TVA** (intracommunautaire). Exploite l’exonération de TVA sur les livraisons intracommunautaires pour générer des crédits de TVA fictifs ou pour ne pas reverser la TVA collectée. Acteurs typiques :

- **Société de défaut** (« missing trader » ou « buffer ») : collecte la TVA des clients mais disparaît avant de la reverser.
- **Société écran intermédiaire** : crée la chaîne d’opérations.
- **Société de récupération** : récupère la TVA déductible.
- **Société de revente** : termine la chaîne.

Le carrousel fait tourner les opérations entre les mêmes acteurs sur de multiples cycles.

**Évasion fiscale internationale** : planification fiscale agressive franchissant la ligne du légal :

- Treaty shopping (utilisation de conventions fiscales hors objet initial).
- Transfert de bénéfices vers juridictions à faible imposition via prix de transfert non conformes.
- Domiciliation fictive dans une juridiction à faible imposition.
- Structures hybrides (mismatch entre qualifications fiscales nationales).
- Trusts et fondations utilisés à des fins de dissimulation fiscale.

**Abus de biens sociaux (ABS)**. Délit français consistant pour le dirigeant à utiliser les biens de la société à des fins personnelles ou pour favoriser une autre société. Mécanismes : prélèvements personnels masqués, factures personnelles payées par la société, voyages perso facturés, biens immobiliers à usage privé.

#### L’utilité opérationnelle

L’analyste cherche à :

- **Détecter le pattern** dans les flux (cycles, fragmentation, contreparties croisées).
- **Identifier les rôles** dans le schéma (buffer, intermédiaire, récupérateur).
- **Documenter les flux** entre la société et le dirigeant ou ses proches (ABS).
- **Quantifier le préjudice** (fiscal pour la fraude TVA, social pour l’ABS).

#### Méthode — signaux carrousel TVA

- Cycles d’opérations entre les mêmes acteurs.
- Sociétés sans substance économique faisant transit de marchandise.
- Crédits de TVA disproportionnés avec activité réelle.
- Sociétés disparaissant brutalement (radiation, dissolution rapide).
- Secteurs à risque historiquement : téléphonie, électronique grand public, métaux, parfums et cosmétiques, droits d’émission CO₂, énergie renouvelable, services digitaux.

#### Méthode — signaux d’évasion fiscale

- Charges de « conseil », « royalties », « management fees » à des entités liées en juridictions à faible imposition, disproportionnées.
- Prêts intragroupe sans intérêts ou à conditions anormales.
- Holding intermédiaire sans substance économique.
- Acquisitions de PI (marques, brevets) cédées à une entité offshore et reconcédées sous redevances.

#### Méthode — signaux d’ABS

- Virements de la société vers comptes personnels du dirigeant sans contrepartie évidente.
- Factures de fournisseurs personnels acquittées par la société.
- Biens (véhicules, immobilier) de la société à usage manifestement privé.
- Comptes courants associés gonflés (le dirigeant a « prêté » à la société mais la société est dépendante).

#### Mini-walkthrough — schéma fraude TVA simplifié

Trois sociétés A, B, C en cycle. A vend en intracommunautaire à B (exonéré TVA). B vend à C en national (TVA 20 % collectée). B disparaît avec la TVA. C revend à un client A (l’opération revient dans le pays d’origine). Crédit TVA de C illégitime ; perte fiscale = TVA non reversée par B.

Lecture FININT : pattern carrousel TVA classique. Vérification : registres (durée de vie des sociétés), comptes (TVA déclarée vs collectée), flux (cycles), liens entre A/B/C (mêmes UBO ou dirigeants partagés).

#### Erreurs fréquentes

- **Confondre optimisation fiscale légale et fraude fiscale.** La frontière est juridique et factuelle.
- **Sous-estimer l’ampleur du carrousel TVA** : c’est l’une des fraudes fiscales les plus massives en UE.
- **Confondre ABS et choix de gestion contestable** : tous les choix discutables d’un dirigeant ne sont pas ABS.

#### Limites

La qualification juridique de fraude fiscale et d’ABS appartient au judiciaire et à l’administration fiscale. Le FININT alimente. La coopération avec les services fiscaux nationaux (DGFiP en France) est centrale.

#### Lien avec le fil rouge

> **CLEARFLOW — Évasion fiscale et ABS**
> 
> Dans le réseau Haddad, l’évasion fiscale via charges de conseil intragroupe à Chypre est *probable*. L’ABS via prélèvements personnels disproportionnés depuis les comptes des SAS françaises est *probable* à *quasi-certain* (signal récurrent dans les relevés). Pas de signal clair de carrousel TVA. La note finale recommande coopération avec la DGFiP pour qualifier les volets fiscaux.

#### Points clés à retenir

- Trois familles : fraude TVA (carrousel), évasion fiscale internationale, ABS.
- Détection : flux, cycles, contreparties, substance économique.
- Coopération DGFiP / autorités fiscales étrangères centrale.
- Qualification juridique : pas du ressort du FININT seul.

-----

### Chapitre 44 — BEC, fraude au fournisseur et réseaux de mules

#### Objectif du chapitre

Comprendre les **fraudes au virement** modernes : Business Email Compromise (BEC), fraude au changement d’IBAN, fraude au président, et le rôle des **réseaux de mules** dans le cashout.

#### Le concept

**BEC (Business Email Compromise)** : famille d’attaques où un attaquant prend le contrôle (réel ou simulé) d’une adresse email professionnelle pour détourner un paiement. Variantes principales :

- **Fraude au président (CEO fraud)** : un faux email d’un dirigeant demande un virement urgent et confidentiel à un collaborateur des finances.
- **Fraude au changement d’IBAN** : un fournisseur légitime semble écrire à son client pour signaler un changement d’IBAN. Le client paie sur le nouveau RIB — au fraudeur.
- **Fraude au faux client** : un faux client semble passer commande, demande livraison, puis disparaît sans payer (à la marge du BEC, mais souvent traité ensemble).
- **Fraude à l’avocat** : un faux avocat ou notaire demande un virement urgent dans le cadre d’une fausse transaction.
- **Vendor email compromise** : compromission réelle de la boîte email d’un fournisseur, exploitée pour rediriger les paiements.

**Réseau de mules.** Les fonds détournés transitent par des comptes de personnes physiques (mules) avant cashout. Les mules sont :

- **Recrutées** via fausses offres d’emploi (« assistant financier », « agent de transfert »), réseaux sociaux, applications de rencontre, sites de petites annonces.
- **Volontaires** (rémunérées) ou **involontaires** (manipulées par phishing ou romance scam).
- **Utilisées** pour recevoir un virement frauduleux, retirer en cash ou retransférer vers le réseau, en quelques heures.

#### L’utilité opérationnelle

Le BEC est un volet majeur de la fraude moderne. Pour la victime (PME, ETI, grand groupe), les pertes sont fréquemment de 50 K€ à plusieurs millions. La récupération dépend de la rapidité du gel — typiquement quelques heures.

#### Méthode — détection et réponse

**En prévention** (au-delà du périmètre FININT pur) : double signature obligatoire pour les virements significatifs, validation par téléphone d’un changement d’IBAN, formation des équipes finances, vérifications techniques (SPF, DKIM, DMARC sur les emails).

**En détection** :

- Virement vers IBAN nouveau, montant inhabituel, libellé urgent.
- Demandes en dehors des heures ouvrées.
- Discrépance entre nom du bénéficiaire affiché et titulaire réel du compte (la **Verification of Payee** — VOP — devient progressivement obligatoire dans l’UE avec le règlement sur les paiements instantanés ; pour les PSP de la zone euro, l’échéance opérationnelle majeure est **octobre 2025** ; pour les PSP hors zone euro, **juillet 2027**. Au moment où l’analyste travaille, le déploiement effectif varie selon les PSP).
- Activité immédiate de fractionnement et de cashout sur le compte bénéficiaire.

**En réaction** (essentielle, urgente) :

- **Contact immédiat** avec la banque émettrice pour gel (fenêtre quasi-nulle en SCT Inst).
- **Plainte** auprès des autorités (en France : Plate-forme PHAROS, plainte en ligne, ou commissariat).
- **Coopération internationale** via CRF (signalement urgent à TRACFIN qui peut activer FIU.NET pour les comptes destinataires européens).
- **Volet crypto** si conversion crypto : renvoi vers OSINT Crypto pour le traçage on-chain.

#### Mini-walkthrough

Une PME française reçoit, le mardi 14h32, un email semblant venir de son fournisseur habituel, demandant le paiement d’une facture sur un nouvel IBAN espagnol. Le directeur financier paie 215 K€ via SCT Inst.

À 14h35-14h41 : le compte espagnol fractionne en 5 virements vers PT et LT.
À 16h12 : conversion USDT sur exchange.
À 18h45 : sortie vers wallet auto-géré.

La PME découvre la fraude le mercredi matin (le vrai fournisseur appelle pour réclamer le paiement). Délai : 18+ heures. Fenêtre de gel : pratiquement fermée pour la portion crypto. Pour les comptes PT et LT, gel possible si rapidité d’action de la CRF.

Bilan typique : récupération de 20 à 40 % du montant si action rapide ; recouvrement total très rare.

#### Erreurs fréquentes

- **Sous-estimer la vitesse.** Les fraudeurs exploitent la non-réversibilité de SCT Inst.
- **Croire que la victime est forcément négligente.** Beaucoup de BEC sont sophistiqués (compromission réelle d’email, manipulation contextuelle).
- **Ignorer le réseau de mules** : sans elles, le cashout est plus difficile. Identifier la mule peut conduire au recruteur.

#### Limites

Le BEC est rapide ; la coopération internationale est plus lente. La récupération totale est rare. Le travail FININT vise souvent à **identifier le réseau** (mules, recruteurs, organisateurs) pour démanteler, plus qu’à récupérer les fonds.

#### Lien avec le fil rouge

> **CLEARFLOW — Branche BEC limitée**
> 
> Une des entrées du dossier Haddad inclut un BEC : 215 K€ détournés d’une PME française vers le compte d’une SAS du réseau Haddad. La piste mule semble présente — la SAS pouvait être utilisée comme étape de layering pour des fonds frauduleux d’origine externe au réseau lui-même. Cette branche est secondaire dans le dossier mais documente que le réseau a pu fonctionner comme **infrastructure de service** pour des fraudes externes.

#### Points clés à retenir

- BEC = famille de fraudes au virement par compromission ou simulation d’email.
- SCT Inst rend le gel quasi impossible.
- Réseaux de mules : volontaires ou involontaires, recrutées en ligne.
- Réaction : rapidité critique, coopération CRF, renvoi crypto si pertinent.

-----

### Chapitre 45 — Contournement de sanctions et biens dual-use

#### Objectif du chapitre

Comprendre les **mécanismes de contournement de sanctions économiques** — sujet devenu central depuis 2022 — et les enjeux liés aux **biens à double usage** (dual-use).

#### Le concept

Les **sanctions économiques** sont des mesures restrictives imposées par des États ou organisations internationales contre des personnes, entités ou pays. Trois sources principales :

- **ONU** : sanctions de l’ONU, contraignantes pour tous les États membres.
- **UE** : sanctions UE consolidées, contraignantes pour tous les opérateurs UE et leurs filiales.
- **US** : sanctions OFAC, avec portée extraterritoriale forte (sanctions secondaires impactant les opérateurs non-US qui font affaire avec les personnes sanctionnées).
- **UK** : sanctions OFSI.
- **Sanctions nationales** spécifiques (France via la DGT).

**Catégories** :

- **Sanctions ciblées** (PEP, dirigeants, entités spécifiques) : gel d’avoirs, interdiction de transactions.
- **Sanctions sectorielles** (banques, énergie, défense, etc.).
- **Embargos** : interdictions générales de commerce avec un pays.
- **Restrictions à l’exportation** de biens (dual-use, militaires, technologiques).

**Contournement** : techniques utilisées pour échapper aux sanctions.

#### Mécanismes de contournement courants

- **Front companies** : société tierce non sanctionnée agit pour le compte d’une entité sanctionnée.
- **Sociétés écrans dans pays tiers** : Émirats, Turquie, Asie centrale, Caucase — par où transitent des flux et marchandises vers et depuis les juridictions sanctionnées.
- **Triangulation commerciale** : achat dans pays A, vente apparente vers pays B (non sanctionné), revente effective vers pays C (sanctionné).
- **Re-pavillonnement** : navires (notamment pétroliers), aéronefs sous pavillon de complaisance pour masquer l’identité réelle.
- **Falsification de documents** : certificats d’origine, bills of lading, documents douaniers.
- **Crypto** : utilisation de stablecoins pour les paiements (renvoi OSINT Crypto pour le détail on-chain).
- **Mixers et bridges** crypto pour brouiller la traçabilité.
- **AIS spoofing** ou éteignage : navires éteignent leur transpondeur AIS pour masquer leur trajectoire.

#### Biens dual-use

Biens à **double usage** civil et militaire (semi-conducteurs avancés, capteurs, lasers, équipements de cryptographie, certains logiciels, drones, équipements industriels lourds). Régulation UE par le règlement 2021/821. Listes mises à jour régulièrement.

Détection FININT : flux financiers vers fournisseurs de biens dual-use, contreparties dans des juridictions à risque, schémas de triangulation, sous-traitance suspecte.

#### L’utilité opérationnelle

Depuis 2022 (sanctions Russie), le contournement est un domaine en croissance forte. Les CRF dédient des ressources spécifiques. Les banques renforcent leur screening (filtres OFAC et UE).

#### Méthode — signaux de contournement

- Flux soudains et significatifs vers une juridiction tierce (Émirats, Turquie, Géorgie, Arménie, Asie centrale).
- Sociétés intermédiaires récemment créées en juridictions tierces.
- Bénéficiaires effectifs liés à des entités sanctionnées (recherche dans OFAC SDN, UE consolidated list).
- Activités d’import-export de biens dual-use ou de technologies sensibles.
- Schémas de triangulation incohérents économiquement.
- AIS spoofing repérable via plateformes de tracking maritime.

#### Mini-walkthrough — schéma simplifié

Une société turque récemment créée commence à recevoir des virements significatifs d’Europe pour « consulting services » et à envoyer des marchandises (semi-conducteurs) vers la Russie. L’UBO de la société turque est lié à une personne précédemment associée à une entreprise russe sanctionnée.

Lecture FININT : *probable* contournement de sanctions UE/US. Signalement et coopération sont prioritaires (CRF turque, sanctions UE et US, services nationaux dédiés).

#### Erreurs fréquentes

- **Considérer toute opération avec un pays tiers comme contournement.** La grande majorité du commerce avec Émirats, Turquie, Géorgie est légitime.
- **Sous-estimer la portée extraterritoriale des sanctions OFAC.** Un opérateur européen peut être impacté.
- **Confondre dual-use et militaire.** Le dual-use est civil mais soumis à autorisation.

#### Limites

Le contournement de sanctions est un domaine **politiquement sensible** et techniquement complexe. Les CRF travaillent en étroite collaboration avec services dédiés (DG Trésor — pôle sanctions financières, OFAC, OFSI, services douaniers).

#### Lien avec le fil rouge

> **CLEARFLOW — Volet sanctions exploratoire**
> 
> Le dossier Haddad contient des flux passant par Émirats, Turquie. À ce stade, aucun lien direct avec une entité sanctionnée n’est démontré. La possibilité que certains flux relèvent d’un contournement *opportuniste* (vente vers juridictions sous embargo via réseau commercial) reste *possible*. La note finale signale ce volet exploratoire au PNF et recommande coopération avec la DG Trésor — pôle sanctions financières.

#### Points clés à retenir

- Sanctions ONU, UE, OFAC, OFSI, nationales.
- Mécanismes de contournement : fronts, triangulation, crypto, re-pavillonnement.
- Dual-use = sujet sensible avec régulation propre.
- Coopération services dédiés (DG Trésor pôle sanctions, OFAC) essentielle.

-----

### Chapitre 46 — Ponzi, pyramides et fraudes à l’investissement

#### Objectif du chapitre

Comprendre les **schémas de fraude à l’investissement** : Ponzi, pyramides, fausses ICO/IDO, fraudes au trading, scams crypto.

#### Le concept

**Ponzi (schema)**. Le promoteur attire des investisseurs en promettant des rendements supérieurs au marché. Les « rendements » versés aux premiers investisseurs sont prélevés sur les apports des nouveaux investisseurs (et non sur une activité économique réelle). Le système s’effondre lorsque les retraits dépassent les nouveaux apports.

**Pyramide (MLM frauduleux)**. Variante : les investisseurs sont incités à recruter de nouveaux participants. Le revenu provient principalement du recrutement, pas d’un produit ou service réel.

**Fausses ICO / IDO / TGE** : émissions de tokens crypto sans projet réel, avec promesses irréalistes, abandon après collecte (« rug pull »).

**Scam pig butchering** : combinaison fraude sentimentale + fraude à l’investissement. La victime est manipulée pendant des mois par une fausse relation, puis incitée à « investir » dans une plateforme crypto qui semble fonctionner — jusqu’au retrait final impossible.

**Faux trading** : plateformes simulant un trading rentable, où la victime voit des « gains » virtuels mais ne peut pas retirer.

#### L’utilité opérationnelle

Les fraudes à l’investissement représentent des pertes massives pour les victimes (souvent l’épargne d’une vie). En CRF, les signalements convergents permettent de détecter et de signaler tôt.

#### Méthode — signaux

- Rendements promis très supérieurs au marché.
- Pression à recruter d’autres investisseurs (pyramide).
- Plateforme inconnue, juridiction obscure.
- Garanties auto-désignées, faux régulateurs.
- Présence de figures publiques (vraies ou usurpées) en endorsement.
- Difficulté ou refus de retrait dès qu’on dépasse certains seuils.
- Cashout difficile sur stablecoins, voire impossible.

#### Mini-walkthrough — pig butchering simplifié

Une victime française rencontre sur application de rencontre un faux ami sentimental basé prétendument à Hong Kong. Après plusieurs mois, le contact recommande une « opportunité d’investissement » sur une plateforme crypto. La victime investit 50 K€ qui sont convertis en USDT, transitent par plusieurs adresses, et atteignent rapidement un exchange asiatique non-KYC. Tentative de retrait : refus pour « frais bloquants ».

Lecture FININT : pig butchering quasi-certain. Volet on-chain renvoyé à OSINT Crypto (Athéna ou équivalent). Signalement à la PHAROS et au PNF JUNALCO (cybercriminalité). Le réseau organisé derrière ces opérations est souvent identifié à terme avec coopération internationale (notamment SE Asie).

#### Erreurs fréquentes

- **Sous-estimer la sophistication** des fraudes pig butchering modernes — équipes professionnelles, scripts éprouvés.
- **Blâmer la victime** : la manipulation est efficace même sur des personnes éduquées.

#### Limites

Les schémas se passent souvent partiellement à l’étranger ; la coopération internationale est lente. Le volet crypto est renvoyé à OSINT Crypto pour le traitement détaillé.

#### Lien avec le fil rouge

> **CLEARFLOW — Hors périmètre principal**
> 
> Le dossier Haddad ne comporte pas de volet Ponzi ou pig butchering identifié. Ce chapitre reste utile à la compréhension du contexte général des typologies modernes.

#### Points clés à retenir

- Ponzi, pyramides, fausses ICO, pig butchering : schémas distincts mais structure commune.
- Rendements promis disproportionnés = signal majeur.
- Coopération internationale (notamment SE Asie) lente mais nécessaire.
- Volet crypto traité par OSINT Crypto.

-----

### Chapitre 47 — Criminalité organisée et économie légale

#### Objectif du chapitre

Comprendre comment la **criminalité organisée** infiltre et instrumentalise l’**économie légale** : secteurs vulnérables, schémas de prise de contrôle, signaux d’enquête.

#### Le concept

La criminalité organisée moderne ne se limite pas à des activités strictement illicites (trafics, vols, extorsions). Elle réinvestit massivement dans l’économie légale via :

- **Restauration et hôtellerie** (forte composante cash, présentation légitime).
- **Bâtiment et travaux publics** (volumes financiers importants, sous-traitance opaque).
- **Transport routier et logistique** (couverture du déplacement de marchandises diverses).
- **Commerce de détail** (lavages auto, bars-tabacs, taxis, distributeurs).
- **Immobilier** (acquisition, location, montages SCI).
- **Trading commodities** (matières premières, métaux, agroalimentaire — TBML).
- **Jeux et paris en ligne** (couches de blanchiment).
- **Crypto et fintech** (rails de placement et layering).
- **Sport professionnel** (paris, transferts, agents).
- **Art et objets de collection** (intégration à valeur élevée).

#### L’utilité opérationnelle

L’analyste FININT travaillant sur la criminalité organisée cherche à :

- **Identifier la prise de contrôle** sur des sociétés légales.
- **Cartographier le réseau** : entreprises, personnes, flux.
- **Détecter le rôle de prête-noms** (chapitre 25).
- **Suivre l’argent** dans l’économie légale jusqu’à ses bénéficiaires réels.

#### Méthode — signaux

- Acquisition d’entreprises en difficulté à prix bas par des intermédiaires opaques.
- Dirigeants avec antécédents (presse, fichiers).
- Croissance soudaine et inexpliquée d’une petite société.
- Recrutement massif et anormal dans certains secteurs (sociétés de gardiennage, par exemple).
- Présence d’entités dans plusieurs juridictions sans rationale économique.

#### Mini-walkthrough

Un réseau acquiert plusieurs PME du BTP en région française, via plusieurs SARL intermédiaires. Les dirigeants des SARL sont des personnes ayant des liens familiaux mais sans expérience BTP. Les marchés gagnés progressent rapidement (BOAMP). Les flux montrent des paiements à des sous-traitants offshore dont l’activité réelle est douteuse.

Lecture FININT : *probable* infiltration de la criminalité organisée dans le BTP régional. Schémas combinés : faux salariat, sous-traitance fictive, fraude TVA. Coopération avec services spécialisés (JIRS, OCLCIFF en France).

#### Erreurs fréquentes

- **Stigmatiser un secteur entier.** La grande majorité des entreprises de chaque secteur sont parfaitement légales.
- **Confondre opacité et criminalité organisée.** Beaucoup d’opacités sont sans lien avec le crime organisé.

#### Limites

L’identification précise et la qualification exigent des moyens d’enquête judiciaire (écoutes, observations, perquisitions). Le FININT alimente, ne tranche pas.

#### Lien avec le fil rouge

> **CLEARFLOW — Hors périmètre**
> 
> Le dossier Haddad ne présente pas de signaux clairs de criminalité organisée au sens strict (mafia, narco, etc.). C’est un dossier de criminalité économique avec des éléments transnationaux. Mais la frontière est poreuse — un dossier qui commence en fraude fiscale peut révéler des connexions à terme.

#### Points clés à retenir

- La criminalité organisée infiltre l’économie légale (BTP, restauration, immobilier, etc.).
- Signaux : acquisitions opaques, croissance inexpliquée, dirigeants à profil suspect.
- Coopération avec services spécialisés (JIRS, OCLCIFF) centrale.
- FININT alimente, ne tranche pas.

-----

### Chapitre 48 — Cybercriminalité, cashout et renvoi vers OSINT Crypto

#### Objectif du chapitre

Comprendre l’**interaction cybercriminalité / criminalité financière** : ransomware, vol de cryptos, BEC, infostealers — et savoir quand renvoyer à OSINT Crypto pour le traitement on-chain.

#### Le concept

Toute cybercriminalité monétisée passe par un **cashout** : conversion des fonds illicites en valeur utilisable. Modalités :

- **Ransom en crypto** (BTC, Monero, USDT) — le plus courant.
- **Vol de fonds DeFi / exchanges** — flash loans, exploits, phishing wallet.
- **BEC** (chapitre 44) — virement fiat puis souvent conversion crypto.
- **Vente de données volées** sur darknet — paiement crypto.
- **Carding** : utilisation frauduleuse de cartes bancaires, cashout en cash, gift cards, biens.

Le cashout final passe souvent par :

- **Exchanges KYC dans juridictions à faible application** des règles.
- **P2P** (LocalBitcoins historiquement, Paxful, ou alternatives modernes).
- **Bureaux de change crypto** dans certaines villes.
- **Stablecoins** comme valeur intermédiaire avant cashout fiat.

#### Articulation FININT / OSINT Crypto

C’est le sujet typique où **FININT et OSINT Crypto coopèrent** :

- **FININT** : cadre le contexte (qui est la victime, qui est probablement derrière l’attaque, quel réseau de mules, quelles coopérations avec banques et autorités, quel suivi judiciaire).
- **OSINT Crypto** : trace les fonds on-chain depuis le wallet d’attaquant jusqu’aux off-ramps (exchanges, P2P), identifie les clusters, qualifie les services traversés (mixers, bridges).

Le rapport FININT **renvoie** à OSINT Crypto pour le détail on-chain. Il ne le refait pas.

#### L’utilité opérationnelle

Pour les dossiers ransomware, vol crypto, BEC majeur, fraude DeFi :

- FININT identifie victimes, impact, contexte, attribution probable (avec CTI).
- OSINT Crypto trace, identifie services, attribue.
- Coopération internationale est centrale (Europol EC3, FBI, services nationaux).

#### Méthode — workflow type

1. **Signalement / DS / incident** détecté.
1. **FININT** cadre : périmètre, victime, contexte.
1. **OSINT Crypto** (Sarah Marin / Athéna Group dans le fil rouge) prend le volet on-chain.
1. **Coopération** avec exchanges pour KYC sur off-ramps via réquisition.
1. **Synthèse** intégrée dans la note FININT.

#### Mini-walkthrough — ransomware sur PME

Une PME française est victime d’un ransomware. Rançon de 80 K€ demandée en USDT vers une adresse Tron. La PME paie (déconseillé, mais souvent fait).

FININT : identification de l’incident, signalement ANSSI/PHAROS, plainte, coopération avec CRF.
OSINT Crypto : traçage de l’adresse de paiement, identification du cluster (TRM Labs / Chainalysis / outils Athéna), suivi jusqu’aux off-ramps, possiblement attribution à un groupe ransomware connu.

Synthèse FININT : note de transmission au PNF JUNALCO et à Europol EC3, avec annexe technique d’OSINT Crypto, et recommandations (poursuite internationale, monitoring continu).

#### Erreurs fréquentes

- **Refaire OSINT Crypto dans le FININT** : duplication, perte de temps, risque d’erreur.
- **Ignorer le lien CTI** : l’attribution à un groupe ransomware (Akira, ALPHV, LockBit, etc.) éclaire le dossier.
- **Sous-estimer l’importance du cashout** : c’est le maillon faible des cybercriminels.

#### Limites

L’attribution finale d’une cybercriminalité est rarement *quasi-certaine* en pur on-chain. Elle exige souvent l’ajout d’éléments hors-chaîne (CTI, témoignages, arrestations).

#### Lien avec le fil rouge

> **CLEARFLOW — Volet crypto secondaire**
> 
> Dans le dossier Haddad, les conversions USDT identifiées ne relèvent pas de ransomware mais de cashout / layering crypto opportuniste. Le volet est confié à Sarah Marin (Athéna). Son rapport on-chain est annexé à la note finale, avec renvoi explicite au cours OSINT Crypto pour les méthodes utilisées.

#### Points clés à retenir

- Cybercriminalité = cashout obligatoire, souvent crypto.
- FININT cadre, OSINT Crypto trace on-chain.
- Coopération avec exchanges via réquisitions.
- Le rapport FININT renvoie à OSINT Crypto, ne refait pas.

-----

## PARTIE VIII — OUTILS, WORKFLOW ET PRODUCTION

*Six chapitres pour structurer la pratique : workflow d’enquête complet, outils gratuits, outils professionnels, visualisation, chaîne de preuve, livrables et diffusion. Cette partie transforme la méthode en pratique organisée.*

-----

### Chapitre 49 — Workflow complet d’une enquête FININT

#### Objectif du chapitre

Décrire un **workflow complet** d’enquête FININT, du signalement initial au livrable final. Ce workflow est une trame, pas un dogme : il s’adapte à chaque dossier mais en respecte la logique.

#### Le workflow en 9 phases

**Phase 1 — Réception et triage.** Le signalement arrive (DS, sollicitation, plainte, demande externe). Triage : urgence, ressources, périmètre approximatif, doublon avec dossier existant.

**Phase 2 — Cadrage initial.** L’analyste pose les questions de renseignement (QR), estime le budget temps, identifie les ressources nécessaires, identifie les coopérations à activer, documente les zones d’ombre prévisibles.

**Phase 3 — Stabilisation des identités.** Identification rigoureuse des entités et personnes (chapitres 19-20). Pas d’enquête de fond sans cette étape.

**Phase 4 — Collecte OSINT.** Registres, comptes annuels, marchés publics, presse, leaks, SOCMINT — tous les sources accessibles selon le périmètre (Partie III).

**Phase 5 — Mobilisation des sources fermées.** En CRF : droits de communication, EAR/CRS, FICOBA, coopérations Egmont. En cabinet : limites strictes.

**Phase 6 — Analyse.** Construction des fiches (personne, société, flux, actif). Graphes relationnels. Analyse de flux et comptabilité (Partie VI). Qualification typologique (Partie VII).

**Phase 7 — Calibration.** Application de l’échelle WEP. Distinction faits / inférences / hypothèses. Documentation des lacunes.

**Phase 8 — Rédaction.** Note FININT structurée (chapitre 54). Modèle K en annexe.

**Phase 9 — Diffusion et suivi.** Transmission aux autorités compétentes. Suivi des coopérations engagées. Mise à jour du dossier au fil des retours.

#### Durée typique

Pour un dossier de complexité moyenne (réseau de 10-15 entités, 3-5 juridictions, plusieurs DS convergentes) : 4 à 12 semaines de travail effectif, avec phases de relance lors des coopérations internationales (2 à 8 semaines additionnelles).

#### L’utilité opérationnelle

Le workflow structure :

- **Le temps de l’analyste** : pas de dispersion.
- **La qualité du livrable** : chaque phase a son output.
- **La coopération** : chaque acteur sait où on en est.
- **La répétabilité** : un même protocole pour différents dossiers permet apprentissage et amélioration.

#### Erreurs fréquentes

- **Sauter le cadrage initial** : on commence à collecter avant de savoir ce qu’on cherche.
- **Ne pas documenter les zones d’ombre** : le rapport devient lisse et trompeur.
- **Sous-estimer les coopérations internationales** : les délais sont structurellement longs.

#### Limites

Le workflow doit être adapté. Un dossier d’urgence (BEC en cours, asset recovery rapide) compresse les phases. Un dossier d’investigation profonde les étend.

#### Lien avec le fil rouge

> **CLEARFLOW — Workflow Nassim**
> 
> Nassim suit ce workflow strict : phases 1-2 en 3 jours (triage + cadrage), phase 3 en 2 jours (stabilisation), phase 4 sur 2-3 semaines (collecte OSINT), phase 5 en parallèle (coopérations), phase 6 sur 2-3 semaines (analyse), phase 7-8 sur 1 semaine (calibration et rédaction), phase 9 ouverte (suivi long). Le dossier est consolidé en environ 8 semaines.

#### Points clés à retenir

- 9 phases : réception, cadrage, stabilisation, collecte OSINT, sources fermées, analyse, calibration, rédaction, diffusion.
- Workflow = trame, à adapter.
- Documentation et traçabilité à chaque phase.

-----

### Chapitre 50 — Outils gratuits : registres, sanctions, presse, leaks

#### Objectif du chapitre

Recenser les **outils gratuits ou freemium** utilisables en FININT pour un travail solide sans budget.

#### Catalogue raisonné

**Registres d’entreprises (chapitres 11-12)** :

- France : Pappers, INPI/data.inpi.fr, Infogreffe (partiellement gratuit), BODACC.
- UK : Companies House.
- US : OpenCorporates, SEC EDGAR, registres étatiques.
- UE : BRIS via e-justice.europa.eu.
- Multi-pays : OpenCorporates (agrégateur, freemium).

**UBO et bénéficiaires effectifs (chapitre 13)** :

- France RBE : accès restreint depuis CJUE.
- UK PSC : Companies House.
- Pandora / Panama / Paradise / Pandora Papers : Offshore Leaks ICIJ.

**Sanctions et PEP** :

- OpenSanctions.org : base agrégée gratuite (sanctions OFAC, UE, ONU, OFSI, et plus).
- Site OFAC, UE consolidated list, ONU, OFSI.
- Sanctions.io : lecture libre partielle.

**Adverse media et presse** :

- Google News (avec limites).
- Médias référents accessibles en consultation gratuite.
- ICIJ Aleph (accès journalistique principalement).
- OCCRP Aleph (selon partenariats).

**Comptes annuels** :

- France : Pappers, Infogreffe.
- UK : Companies House.
- Allemagne : Bundesanzeiger.
- Belgique : Moniteur belge.

**Marchés publics** :

- BOAMP, data.gouv.fr (DECP), TED, SAM.gov, USAspending.gov.

**Patrimoine** :

- DVF (Demandes de valeurs foncières) data.gouv.fr.
- Patrim (accès via espace personnel impots.gouv.fr — limité aux usages personnels).
- Cadastre.gouv.fr.
- Bases yachts/maritime : MarineTraffic (free tier).
- Bases aéronefs : FlightAware, ADS-B Exchange.

**Visualisation gratuite** :

- Maltego (free tier, transforms limitées).
- Gephi (open source).
- Cytoscape.
- Excel/LibreOffice (graphes simples).

**Recherche d’images inverse** :

- Google Images.
- TinEye.
- Yandex.

**Archives web** :

- Web Archive (Wayback Machine).
- archive.today.

**OSINT général utile en FININT** :

- IntelTechniques (outils OSINT).
- OSINT Framework.
- Bellingcat investigations toolkit.

#### Méthode — workflow gratuit type

Pour un dossier sans budget, l’enchaînement standard :

1. Pappers + INPI + Companies House + OpenCorporates → identification + cartographie initiale.
1. ICIJ Offshore Leaks → recoupement leaks.
1. OpenSanctions → screening sanctions/PEP.
1. Google + agrégateurs gratuits → adverse media.
1. DVF + cadastre + MarineTraffic → patrimoine français visible.
1. Gephi → visualisation finale.

Couvre 70-80 % d’une enquête de complexité moyenne avec un budget de 0 €.

#### Erreurs fréquentes

- **Sous-estimer ce qu’on peut faire gratuitement.** Beaucoup d’analystes débutent en pensant que l’OSINT financier est inaccessible — c’est faux.
- **Surestimer la profondeur des outils gratuits.** Pour les juridictions opaques, le multi-juridictionnel intensif, l’agrégation à grande échelle, des outils professionnels sont nécessaires.

#### Limites

Les outils gratuits ont des **plafonds** (nombre de requêtes, profondeur de couverture, fréquence de mise à jour). Pour des dossiers complexes ou volumineux, les outils professionnels apportent une vraie valeur ajoutée.

#### Lien avec le fil rouge

> **CLEARFLOW — Phase OSINT gratuite**
> 
> Nassim utilise gratuitement Pappers, Companies House, OpenCorporates, OpenSanctions, Offshore Leaks pour le travail de cartographie initial. L’investissement dans Sayari (chapitre 51) intervient pour étendre la couverture sur les juridictions à risque où les outils gratuits sont insuffisants.

#### Points clés à retenir

- Beaucoup d’OSINT financier est accessible gratuitement.
- Catalogue raisonné par usage.
- Plafond des gratuits → bascule vers professionnels selon complexité.

-----

### Chapitre 51 — Outils professionnels : Sayari, Orbis, World-Check, Dow Jones, LexisNexis

#### Objectif du chapitre

Présenter les **principaux outils professionnels** utilisés en FININT, leurs forces, leurs usages, leur coût.

#### Catalogue raisonné

**Sayari** : référence moderne pour l’OSINT financier multi-juridictionnel. Agrège registres mondiaux, sanctions, leaks, contentieux. Particulièrement fort sur la cartographie de réseaux et l’identification d’UBO indirects. Tarif annuel : selon licence, allant de plusieurs milliers à plusieurs dizaines de milliers d’euros.

**Orbis** (Moody’s / Bureau van Dijk) : base massive de sociétés mondiales avec données financières, dirigeants, actionnariat, indicateurs de risque. Standard historique du due diligence. Tarif élevé.

**Dun & Bradstreet** : équivalent fonctionnel à Orbis, plus orienté évaluation de risque commercial.

**World-Check (Refinitiv / LSEG)** : base PEP, sanctions, adverse media. Standard de l’industrie financière pour le screening KYC.

**Dow Jones Risk & Compliance** : équivalent de World-Check, agrégateur de risque.

**LexisNexis Diligence** : équivalent, avec couverture juridique et adverse media plus large.

**Factiva (Dow Jones)** : base presse internationale, indispensable pour l’adverse media approfondi.

**Nexis Newsdesk** : équivalent presse.

**Refinitiv Eikon** : données marchés financiers, indispensable pour les analyses sur sociétés cotées.

**S&P Capital IQ** : équivalent.

**Bloomberg Terminal** : référence absolue (et chère) pour les marchés financiers.

**ICIJ Aleph** : accès professionnel (journalisme).

**OCCRP Aleph** : accès professionnel.

**Outils crypto pro** : Chainalysis Reactor, TRM Labs, Elliptic (renvoi OSINT Crypto).

#### L’utilité opérationnelle

Les outils professionnels apportent :

- **Couverture** plus large (juridictions, périodes, types de données).
- **Agrégation** : recherche unifiée sur des sources hétérogènes.
- **Détection d’UBO indirects** : algorithmes propriétaires de remontée de chaîne.
- **Mise à jour** : fréquence supérieure aux outils gratuits.
- **Garanties qualité** : sources vérifiées, méthodologies documentées.

#### Méthode — choix d’outil par usage

- **Cartographie de réseau multi-juridictionnel** : Sayari > Orbis.
- **Due diligence due process** : Orbis + Dun & Bradstreet + World-Check + Factiva.
- **Screening PEP/sanctions à grande échelle** : World-Check ou Dow Jones R&C.
- **Adverse media profond** : Factiva + LexisNexis.
- **Cotées et marchés** : Refinitiv Eikon, S&P, Bloomberg.
- **Crypto** : renvoi OSINT Crypto.

#### Erreurs fréquentes

- **Croire que l’outil remplace l’analyse.** Un graphe Sayari ne fait pas l’analyse à votre place.
- **Surinterpréter les scores de risque** propriétaires : ils sont des indicateurs, pas des conclusions.
- **Négliger les sources gratuites** une fois équipé professionnel : la complémentarité reste utile.

#### Limites

Tarifs élevés (10K à 100K+ EUR par an selon licence). Couverture inégale selon juridictions et secteurs. Confiance variable selon la maturité de l’outil sur un domaine particulier.

#### Lien avec le fil rouge

> **CLEARFLOW — Sayari pour les juridictions à risque**
> 
> Nassim mobilise Sayari pour étendre la cartographie sur Chypre, Émirats, Liban — là où les outils gratuits étaient insuffisants. Le retour est élevé : identification de plusieurs entités liées non repérées en OSINT gratuit, recoupements UBO précieux.

#### Points clés à retenir

- Sayari, Orbis, World-Check, Dow Jones R&C, LexisNexis, Factiva : outils professionnels de référence.
- Tarifs élevés, couverture supérieure.
- Choix par usage opérationnel.
- L’outil ne remplace pas l’analyste.

-----

### Chapitre 52 — Visualisation : Maltego, i2, Linkurious, Gephi, Graphistry

#### Objectif du chapitre

Maîtriser les **outils de visualisation** pour construire des graphes relationnels FININT exploitables.

#### Catalogue raisonné

**Maltego** : standard OSINT depuis 15+ ans. Forces : transforms multiples (intégrations natives avec dizaines de sources), modélisation de graphes, exploration interactive. Versions : Community (gratuite, limitée), Pro, Enterprise.

**i2 Analyst’s Notebook (IBM)** : standard du renseignement institutionnel et police. Forces : analyse de cas complexes, modèles temporels, intégration avec bases policières. Lourd à prendre en main mais très puissant. Coût élevé.

**Linkurious Enterprise** : plateforme web-based, backend Neo4j. Forces : exploration interactive grands graphes, collaboration multi-utilisateurs, audit. Adopté par certaines CRF et banques.

**Gephi** : open source, orienté analyse de données (centralités, communautés, layout). Excellent pour les graphes statiques de présentation.

**Graphistry** : web-based, accélération GPU pour très grands graphes. Forces : performance, exploration interactive, intégration analytique.

**Cytoscape** : open source, à l’origine biologique, utilisable pour réseaux financiers.

**Neo4j** : base de données graphe utilisée comme backend de plusieurs outils. Requêtes Cypher pour l’analyse.

**Excel / Power BI** : pour les analyses simples ou les présentations exécutives. Sous-estimé par les analystes techniques.

#### Méthode — choix d’outil par contexte

- **Exploration interactive, peu de nœuds (< 100)** : Maltego.
- **Cas complexe institutionnel, intégration policière** : i2.
- **Très grand graphe (1000+)** : Linkurious ou Graphistry.
- **Présentation finale propre** : Gephi (export image), Linkurious.
- **Analyse de centralités, communautés** : Gephi.
- **Public exécutif, simple** : Excel / PowerBI.

#### L’utilité opérationnelle

Le bon outil :

- **Accélère** la construction du graphe.
- **Permet la calculation** des métriques (centralité, communautés).
- **Communique** efficacement le résultat.

Le mauvais outil :

- **Ralentit** le travail (limites de performance).
- **Cache** la complexité (graphe illisible).
- **Trompe** par mauvais layout.

#### Erreurs fréquentes

- **Penser que la visualisation prouve quelque chose.** Elle illustre.
- **Surcharger** le graphe : 200 nœuds visibles = illisible.
- **Ne pas annoter** les arcs et les nœuds : ambiguïté.

#### Limites

Aucun outil ne fait l’analyse — l’analyste pose les bonnes questions et interprète.

#### Lien avec le fil rouge

> **CLEARFLOW — Linkurious pour le dossier**
> 
> Le dossier Haddad, avec ~40 nœuds principaux, est construit dans Linkurious (licence du service). Maltego sert pour l’exploration initiale, Gephi pour le graphe final présentable. Le travail visualisation prend environ 1 jour cumulé.

#### Points clés à retenir

- Maltego (OSINT standard), i2 (institutionnel), Linkurious (web grand graphe), Gephi (analyse + présentation), Graphistry (GPU).
- Choix par contexte.
- La visualisation illustre, ne prouve pas.

-----

### Chapitre 53 — Chaîne de preuve, captures, horodatage, hash

#### Objectif du chapitre

Maîtriser la **discipline de chaîne de preuve** : capture des sources, horodatage, hashing, archivage — pour que les éléments collectés restent exploitables et défendables.

#### Le concept

La **chaîne de preuve** (chain of custody) est la traçabilité des éléments d’enquête : qui a collecté, quand, où, comment, avec quelle modification, qui les a transmis, à qui. Une chaîne de preuve solide est nécessaire pour :

- Garantir l’**intégrité** des éléments.
- Permettre la **reproduction** par un tiers (juge, magistrat, expert).
- Éviter les contestations d’authenticité.

#### Bonnes pratiques

**Capture** : pour chaque élément OSINT collecté :

- Capture d’écran (PNG, PDF) ou enregistrement HTML brut.
- URL exacte de la source.
- Date et heure de capture (avec fuseau horaire).
- Identifiant de l’analyste.

**Horodatage** : utilisation de services d’horodatage tiers pour les éléments critiques (Tiers de confiance, service notarisation horaire). Pour la grande majorité des cas, l’horodatage interne (système de fichiers + journal de l’analyste) suffit.

**Hash** : pour les fichiers téléchargés (rapports, documents PDF, archives), calculer un hash SHA-256 (ou SHA-512) au moment du téléchargement. Le hash garantit l’intégrité.

**Archivage** : stockage dans un système de gestion de dossiers (DMS) avec contrôle d’accès, journalisation, sauvegarde. En CRF : système agréé. En cabinet : à minima répertoire sécurisé avec contrôle d’accès.

**Annotation** : chaque élément annoté de son contexte (pourquoi collecté, qu’apporte-t-il).

**Transmission** : transmission par canaux sécurisés (chiffrement bout en bout, courriers chiffrés, plateformes professionnelles).

#### Méthode — workflow type

À chaque collecte :

```
[date/heure] [analyste] capture [URL]
- Capture : nom_fichier.png (hash SHA-256)
- Archive HTML : nom_fichier.html
- PDF source : nom_fichier.pdf (hash)
- Note : pourquoi collecté, qu'apporte-t-il
- Tags : entité concernée, type de source
```

Outils utiles : extensions navigateur de capture (Singlefile pour HTML complet, Hunchly pour OSINT), gestionnaires de notes (Obsidian, Notion, Joplin), DMS internes.

#### Erreurs fréquentes

- **Pas de capture** : on s’appuie sur une URL qui change ou disparaît.
- **Pas d’horodatage** : on perd la séquence des collectes.
- **Pas de hash** : on ne peut pas prouver l’intégrité.
- **Stockage non sécurisé** : risque de fuite ou de perte.

#### Limites

La chaîne de preuve OSINT n’a pas la même valeur judiciaire qu’une saisie sous procédure. Mais une chaîne propre rend le livrable beaucoup plus crédible.

#### Lien avec le fil rouge

> **CLEARFLOW — Chain of custody Nassim**
> 
> Sur 8 semaines de travail, Nassim accumule environ 1 200 captures (HTML, PNG, PDF). Toutes archivées dans le DMS interne de la CRF, hashées, horodatées, tagées par entité. Cette discipline rend la note finale **reproductible** : un tiers peut suivre chaque chaîne.

#### Points clés à retenir

- Chaîne de preuve = intégrité + reproductibilité + non-contestation.
- Pratiques : capture, horodatage, hash, archivage, annotation, transmission sécurisée.
- Outils : Singlefile, Hunchly, Obsidian, DMS interne.

-----

### Chapitre 54 — Note FININT, rapport et diffusion

#### Objectif du chapitre

Maîtriser la **rédaction et la diffusion** d’une note FININT — livrable final du travail. Modèle complet en annexe K.

#### Structure type d’une note FININT

1. **En-tête** : référence, date, version, classification (TLP), auteur, destinataires.
1. **Résumé exécutif** : 10-15 lignes maximum, conclusions calibrées, recommandations.
1. **Mandat et questions de renseignement** : ce qu’on a cherché à établir.
1. **Méthodologie** : sources mobilisées, limites du périmètre.
1. **Analyse** : organisée par thèmes (entités, personnes, flux, typologie).
1. **Hypothèses calibrées** : explicitement formulées, avec niveau WEP.
1. **Lacunes** : ce qui n’a pas pu être établi, pourquoi, comment.
1. **Recommandations** : actions concrètes (signalement, gel, coopération, approfondissement).
1. **Annexes** : fiches personne, société, flux, actif ; graphes ; sources détaillées.

#### Style de rédaction

- **Phrases courtes**, claires.
- **Vocabulaire prudent** : « les éléments observés sont compatibles avec », « l’hypothèse la plus robuste est », « niveau de confiance probable ».
- **Pas de jargon non défini**.
- **Faits / inférences / hypothèses** distincts.
- **Sources** systématiquement référencées (par numéro, avec liste en annexe).

#### Classification TLP

Standard utilisé en renseignement :

- **TLP:WHITE** ou **TLP:CLEAR** — diffusion libre.
- **TLP:GREEN** — diffusion à la communauté (peers).
- **TLP:AMBER** — diffusion restreinte aux destinataires et à leur organisation.
- **TLP:AMBER+STRICT** — destinataires uniquement.
- **TLP:RED** — destinataires nominatifs uniquement.

La note FININT typique : TLP:AMBER.

#### Diffusion

- **Autorités judiciaires** : transmission via canal officiel (réquisitions, articles 40 CPP en France, équivalents internationaux).
- **CRF étrangères** : via FIU.NET (UE) ou Egmont Secure Web (mondial).
- **Services partenaires nationaux** : canaux établis (DGSI, DGDDI, DGFiP, etc.).
- **Communication interne** : selon le format et la classification.

#### L’utilité opérationnelle

La note FININT est le **point culminant** du travail. Sa qualité détermine son exploitation :

- Une note claire et calibrée est utilisée par les magistrats.
- Une note confuse ou non calibrée est mise de côté.

#### Erreurs fréquentes

- **Note trop longue** : un magistrat lit le résumé exécutif. S’il est obscur, le reste est ignoré.
- **Vocabulaire affirmatif sans calibration** : risque de contestation et de perte de crédibilité.
- **Pas de recommandations** : la note décrit mais ne propose pas.
- **Pas de lacunes** : sape la confiance.

#### Limites

La note est un livrable, pas une fin. Le suivi (coopérations, retours, mises à jour) continue après.

#### Lien avec le fil rouge

> **CLEARFLOW — Note finale**
> 
> Au terme des 8 semaines, Nassim produit une note de 24 pages (corps + 7 fiches personne, 14 fiches société, 22 fiches flux, 11 fiches actif, 1 graphe principal). Résumé exécutif d’1 page. Recommandations claires. Transmission au PNF, TRACFIN coordinateur, et coopérations internationales engagées en parallèle.

#### Points clés à retenir

- Note FININT = livrable structuré, calibré, sourcé, actionnable.
- Résumé exécutif essentiel.
- Classification TLP.
- Diffusion par canaux officiels.

-----

## PARTIE IX — CAS PRATIQUES DÉROULÉS

*Cinq cas pratiques fictifs mais réalistes, chacun déroulé comme une enquête complète : contexte → indices → cadrage → collecte → analyse → hypothèses → limites → livrable → bilan honnête. Les cas illustrent les méthodes des parties précédentes et préparent à la pratique. Tous les noms et données sont fictifs.*

-----

### Chapitre 55 — Cas 1 : Société écran et fournisseur suspect

#### Contexte

Une grande entreprise française du secteur BTP, **CONSTRUCT FRANCE SA**, fait appel à un cabinet de compliance externe à la suite d’une alerte du contrôle interne : un fournisseur récent, **BTP SERVICES INTERNATIONAL SARL**, basé en France, présente des caractéristiques inhabituelles. La compliance a déjà identifié plusieurs signaux mais sollicite une analyse FININT externe pour qualifier.

**Demande** : qualifier la nature et le risque associés à BTP SERVICES INTERNATIONAL.

#### Indices initiaux fournis

- Société française créée 11 mois avant le premier marché avec CONSTRUCT.
- Capital social 1 000 €.
- Dirigeant unique, ancien retraité du secteur agro-alimentaire.
- Domiciliation à un cabinet de domiciliation parisien.
- Aucun site web.
- Volume de prestations facturé sur 6 mois : 1,4 M€.
- Facturations très techniques (sous-traitance gros œuvre, ferraillage, étanchéité).
- Bénéficiaire effectif déclaré au RBE : le dirigeant unique.

#### Cadrage initial

**Questions de renseignement** :

- QR1 — La société a-t-elle une activité économique réelle ?
- QR2 — Quel est l’UBO réel ?
- QR3 — Quel est le réseau de relations de cette société ?
- QR4 — Quel est le profil de risque (fraude fiscale, ABS, blanchiment, fronting) ?

**Budget temps estimé** : 2 semaines.

**Limites prévisibles** : sans réquisition, accès limité aux relevés bancaires et à la comptabilité détaillée.

#### Collecte

**OSINT registres** :

- Pappers + INPI + Companies House (rien à l’étranger). SIREN, K-bis, statuts, comptes (1er exercice non clos).
- Recherche par dirigeant : la personne est gérante d’une seule société. Pas multi-mandats. Mais profil incohérent (retraité agro vs gros œuvre).
- BODACC : pas de procédure.

**OSINT divers** :

- LinkedIn du dirigeant : profil très minimal, aucune photo, aucune mention BTP.
- Adresse de domiciliation : 32 autres entités à la même adresse. Variées, peu de cohérence sectorielle.

**Sources adjacentes** :

- Le dirigeant a un fils. Recherche par nom : le fils, M. R, dirige une autre société de BTP en région parisienne, **R-CONSTRUCT SARL**, qui a connu une procédure collective il y a 3 ans (liquidation pour passifs URSSAF et fiscaux).
- Croisement : l’adresse personnelle déclarée par M. R correspond à celle du père (domiciliation familiale plausible).
- Recherche presse : un article local de 2021 mentionne un dossier de fraude TVA en BTP impliquant plusieurs sociétés en lien avec M. R (instruction en cours à l’époque ; pas d’information sur la suite).

**Compliance interne CONSTRUCT (partagé)** :

- Sur 6 mois, BTP SERVICES INTERNATIONAL a facturé 1,4 M€ à CONSTRUCT pour des prestations dont la traçabilité physique (présence de personnel sur chantier, signatures pointage) est faible voire absente.
- Les factures ont été acquittées par virements vers un compte de la société à la Banque XX (France).

#### Analyse

**Substance économique** : faible. Pas de personnel déclaré (URSSAF non accessible à l’externe), pas de matériel, pas de présence opérationnelle visible. Le dirigeant officiel n’a aucune compétence visible en BTP.

**UBO réel probable** : *probable* que M. R (le fils) soit l’UBO réel, via prête-nom paternel. Indices convergents : profil incohérent du dirigeant officiel, historique BTP de M. R, contentieux antérieur de M. R, adresse partagée, période de création (un an après la liquidation de R-CONSTRUCT — délai typique de reconstruction sous nouveau nom).

**Typologie probable** : compatible avec **fronting** (M. R, ayant des contentieux et difficultés antérieures, utilise une société au nom du père pour continuer ses activités) **et/ou** avec un schéma de **facturation fictive** au profit de CONSTRUCT (rétrocommissions, mise à disposition de travail au noir, fraude URSSAF). Sans accès aux relevés et au pointage de chantier, distinction *indéterminable* à ce stade.

#### Hypothèses calibrées

- **H1 — Fronting + activité réelle (M. R reprend une activité légale via prête-nom paternel)** : probable.
- **H2 — Facturation fictive et travail dissimulé** : possible à probable.
- **H3 — Schéma de blanchiment** : peu probable au vu des éléments (les flux sont entrants depuis CONSTRUCT, pas d’origine externe suspecte).
- **H4 — Société écran à finalité de carrousel TVA** : peu probable (pas de cycle observable, profil mono-client).

#### Limites

- Sans réquisition des relevés bancaires et des pointages de chantier, impossible de distinguer H1 de H2.
- Sans accès aux déclarations URSSAF, impossible de qualifier le travail dissimulé.
- L’UBO réel = M. R reste *probable*, pas *quasi-certain*.

#### Livrable

Rapport au client (CONSTRUCT) :

- Société présentant *probable* fronting.
- Risque de facturation fictive ou de travail dissimulé : *possible à probable*.
- Recommandations :
  - **Rupture progressive** de la relation commerciale, avec mention explicite du risque dans le dossier compliance.
  - **Plainte au procureur de la République** (article 40 CPP ne s’applique pas à une entreprise privée, mais une plainte est ouverte à toute personne morale victime ou témoin d’infractions) si éléments suffisants de facturation fictive ou d’escroquerie au préjudice de CONSTRUCT.
  - **Signalement à l’inspection du travail** pour le volet travail dissimulé.
  - **Signalement à l’URSSAF** et à la **DGFiP** selon les indices.
  - **Important** : une entreprise du BTP comme CONSTRUCT n’est **pas, en principe, assujettie LCB-FT** au sens du Code monétaire et financier. La déclaration de soupçon à TRACFIN concerne les **assujettis** (banques, PSP, notaires, certaines professions). CONSTRUCT ne peut donc pas faire de DS TRACFIN ; ses signalements passent par les voies évoquées ci-dessus (plainte, inspection, URSSAF, DGFiP). C’est sa **banque** qui, le cas échéant, sera assujettie et susceptible de produire une DS sur les flux observés.
  - **Audit interne** sur les processus de KYB fournisseurs.

#### Bilan honnête

L’enquête a permis de qualifier rapidement (2 semaines) un fournisseur à risque, sans coût ni outils professionnels lourds (gratuits : Pappers, Companies House, BODACC, LinkedIn, presse locale, recherches d’état civil partielles). La qualification reste à un niveau *probable* — la confirmation *quasi-certaine* exigerait des éléments accessibles seulement en cadre judiciaire ou inspection. C’est une qualification utile à CONSTRUCT : suffit à motiver des décisions internes (rupture commerciale, signalement) sans engager judiciairement CONSTRUCT au-delà de ses obligations.

#### Leçons FININT

- **Le profil du dirigeant** est souvent un signal de premier ordre. Un retraité agro à la tête d’une société de gros œuvre = signal fort.
- **L’antériorité familiale ou relationnelle** : un fronting via parent est un classique.
- **La cohérence sectorielle** : 32 entités domiciliées au même cabinet sans cohérence sectorielle = signal de cluster suspect.
- **Limites d’OSINT** : sans réquisition, on s’arrête à *probable*. C’est suffisant pour motiver une rupture commerciale ; insuffisant pour qualifier judiciairement.

-----

### Chapitre 56 — Cas 2 : Fraude au changement d’IBAN / BEC

#### Contexte

Une PME française du secteur agroalimentaire, **ALPHA INDUSTRIE SARL**, 28 employés, 6 M€ de CA annuel, est victime d’une fraude au virement le mardi 14 mars. Montant : **215 000 €**. La fraude est découverte le mercredi matin lors d’un appel du vrai fournisseur réclamant son paiement.

ALPHA dépose plainte le mercredi 15 mars matin et saisit son cabinet d’avocats. Le cabinet sollicite une expertise FININT pour le volet traçage et reconstitution.

**Demande** : reconstituer la séquence, identifier les acteurs, évaluer les chances de récupération, préparer les éléments pour la procédure judiciaire et la coopération internationale.

#### Indices initiaux fournis

- Le directeur financier d’ALPHA a reçu, le lundi 13 mars à 17h30, un email apparemment du dirigeant d’un fournisseur habituel (entreprise espagnole **TAIDA SL**), signalant un changement d’IBAN pour la prochaine facture.
- Le mardi 14 mars à 14h32, paiement effectif via SCT Inst de 215 K€ vers l’IBAN ES indiqué (compte au nom d’**IBERICA TRADING SL**, société espagnole).
- Le mercredi 15 mars vers 9h, le vrai TAIDA SL appelle ALPHA pour réclamer le paiement.
- L’examen de l’email frauduleux montre un domaine très proche du vrai TAIDA (typosquatting : `taida-sl.es` vs vrai `taidasl.es`).
- La banque d’ALPHA a tenté un rappel SCT Inst : refusé (compte récepteur a accepté l’opération ; SCT Inst irréversible sans accord).

#### Cadrage initial

**Questions de renseignement** :

- QR1 — Reconstituer la séquence en aval (où sont allés les 215 K€ ?).
- QR2 — Identifier l’attaquant (groupe organisé, isolé, niveau d’expérience).
- QR3 — Quels leviers pour récupération partielle ?
- QR4 — Quelles coopérations engager ?

**Budget temps** : 1 semaine pour le cœur du travail, plus suivi.

**Limites prévisibles** : sans réquisitions des banques étrangères, traçage des comptes étrangers limité. Volet crypto à confier à Athéna Group / OSINT Crypto.

#### Collecte

**OSINT sur IBERICA TRADING SL** :

- Registre espagnol (RMC) : société créée 4 mois avant les faits. Capital 3 000 €. Activité déclarée : « commerce de gros divers ». Dirigeant unique : un national espagnol d’environ 35 ans, sans expérience commerciale antérieure visible.
- Adresse : domiciliation à Madrid.
- Pas de site web. Pas de présence en ligne.
- Lecture : *probable* société de mule / shell créée pour l’opération.

**Compliance bancaire (via avocats)** :

- La banque d’IBERICA en Espagne, sollicitée, indique des transferts sortants rapides après le crédit de 215 K€.
- Détail (partiel, sous le cadre coopération européenne) :
  - 14h35-14h41 : 5 SCT Inst sortants depuis IBERICA vers 5 IBAN distincts (3 au Portugal, 2 en Lituanie).
  - Chaque sortie : 40 000 € à 45 000 €.
  - Bénéficiaires : 5 comptes ouverts récemment dans 3 banques différentes (Revolut LT, Wise via BE, et 3 banques portugaises moyennes).

**OSINT sur les 5 destinataires** : tous sont des personnes physiques (apparemment), avec profils minimaux. Aucun lien apparent entre elles. *Probable* réseau de mules.

**Volet crypto (confié à Sarah Marin / Athéna Group)** :

- Sur les 5 comptes en aval (LT, PT), 4 sur 5 ont rapidement (16h12-16h18) effectué des dépôts USDT sur un exchange A (basé hors UE, profil KYC ambigu).
- Les USDT sont sortis dans l’heure vers un wallet auto-géré, puis fragmentés via plusieurs adresses.
- Le rapport on-chain Athéna identifie une convergence : plusieurs des adresses finales correspondent à un cluster connu de cashout opérant sur des exchanges asiatiques non-KYC.
- *Quasi-certaine* attribution du cashout à un réseau organisé, mais identification individuelle des attaquants reste *indéterminable* au niveau on-chain seul.

#### Analyse

**Reconstitution de la séquence** :

```
T-48h (lundi 17h30) : email frauduleux reçu par DF ALPHA, taida-sl.es (typosquat).
T-0   (mardi 14h32) : SCT Inst ALPHA → IBERICA, 215 K€.
T+3min                : Fractionnement IBERICA → 5 IBAN (PT, LT), 40-45 K€ chacun.
T+1h40                : Dépôts USDT sur exchange A par 4 des 5 comptes.
T+2h45                : Sorties USDT vers wallet auto-géré.
T+4h15                : Fragmentation crypto, convergence vers cluster cashout asiatique.
T+18h (mercredi 9h)   : ALPHA découvre la fraude.
```

**Acteurs et rôles** :

- Attaquant initial : auteur de l’email, *probable* groupe organisé (la sophistication du typosquatting + la connaissance du nom du fournisseur réel + le timing avec date de facturation suggèrent un repérage préalable).
- IBERICA TRADING SL : société écran de réception (mule de premier niveau).
- 5 comptes en aval : mules de deuxième niveau.
- Cluster cashout asiatique : infrastructure de monétisation.

**Typologie** : BEC avec layering rapide multi-PSP et cashout crypto. Schéma classique 2023-2025.

#### Hypothèses calibrées

- BEC : quasi-certain.
- Réseau de mules organisé : quasi-certain.
- Attribution à un groupe spécifique : indéterminable au niveau du cabinet ; CTI / coopérations internationales nécessaires.
- Récupération totale : peu probable. Récupération partielle (50 000 € à 80 000 € si action très rapide sur comptes ES et PT non encore vidés) : possible.

#### Limites

- Identification précise des attaquants : *indéterminable* au niveau de l’enquête privée. Reste à l’enquête judiciaire et aux coopérations internationales (Europol EC3, INTERPOL).
- Récupération crypto : la portion convertie en USDT est *peu probable* à récupérer (cashout déjà effectué dans des juridictions à faible coopération).
- La portion encore en comptes ES/PT (si non vidés) : *possible* à geler par requête judiciaire urgente, avec saisine du parquet européen via le PNF si applicable.

#### Livrable

Rapport au client (ALPHA, via le cabinet d’avocats) :

- Reconstitution de la séquence.
- Cartographie des comptes et des juridictions.
- Pour la procédure : éléments à transmettre au parquet (déjà saisi par la plainte).
- Pour la récupération : actions immédiates (saisine du parquet européen pour gel des comptes ES et PT non vidés ; coopération via FIU.NET pour les comptes LT).
- Pour les leçons : audit des procédures internes (process de validation des changements d’IBAN, double signature, vérification téléphonique).

#### Bilan honnête

La fraude est constatée. La portion fiat (encore en comptes ES/PT) peut être partiellement gelée si action très rapide (24-48h après dépôt de plainte) — en pratique, les délais administratifs et judiciaires ramènent souvent ces espoirs à 10-25 % de récupération réelle. La portion crypto (~75 % du montant) est *quasi-certainement* perdue. L’identification des attaquants est *indéterminable* au niveau du cabinet ; elle dépend des coopérations internationales et des renseignements policiers (cluster connu = identification *possible* avec temps et coopération).

Le travail FININT et OSINT Crypto a un double rôle : (1) tenter de sauver la partie fiat encore mobilisable, (2) alimenter la procédure judiciaire et les coopérations pour démantèlement à terme du réseau.

#### Leçons FININT

- **La vitesse est centrale.** Au-delà de 24h, la majorité des fonds est partie.
- **FININT et OSINT Crypto se complètent.** Le partage du dossier est efficace.
- **Les mules ne sont pas l’objectif final** : elles sont des indicateurs vers les organisateurs.
- **Récupération vs identification** : deux objectifs différents, qui exigent des actions différentes.
- **Prévention vaut récupération** : un audit des procédures préviendrait l’écrasante majorité des BEC.

-----

### Chapitre 57 — Cas 3 : Corruption internationale et PEP

#### Contexte

Une banque privée européenne, **BANQUE-PARTNER** (fictive), procède à un examen LCB-FT approfondi d’un compte client significatif. Le client, **M. KAMBOU**, est un ancien ministre d’un pays d’Afrique de l’Ouest (statut PEP confirmé). Le compte présente une activité importante depuis 18 mois : crédits totaux de 12 M€ provenant de diverses sources internationales, débits vers immobilier européen et fonds d’investissement.

La banque, en application de la vigilance renforcée PEP, mandate un cabinet de conformité pour une **due diligence approfondie**.

**Demande** : qualifier la cohérence des fonds avec le profil et l’historique professionnel du client, identifier risques de corruption et recommander des suites.

#### Indices initiaux

- M. KAMBOU, ministre de l’Économie pendant 6 ans, sorti de fonctions il y a 4 ans.
- Patrimoine déclaré à l’entrée en relation : ~3,5 M€.
- Sources de revenus déclarées : conseils stratégiques pour des entreprises africaines et européennes, plus quelques participations.
- Comptes : ouverts depuis l’année qui a suivi la sortie des fonctions. Activité progressivement croissante.

#### Cadrage initial

**Questions de renseignement** :

- QR1 — Origine des fonds : conseils légitimes ou rétrocommissions de fonctions antérieures ?
- QR2 — Quel est le profil PEP étendu (famille, collaborateurs étroits) ?
- QR3 — Y a-t-il des liens visibles avec des marchés publics du pays d’origine ?
- QR4 — Quelle qualification du compte (à approfondir, rupture, signalement) ?

#### Collecte

**Sources ouvertes** :

- Wikipédia, presse africaine et internationale : parcours politique, déclarations de patrimoine durant le mandat, controverses éventuelles.
- Bases PEP commerciales (World-Check) : confirmation statut PEP, famille étendue identifiée (épouse, 3 enfants, plusieurs proches collaborateurs identifiés).
- Registres d’entreprises : sociétés détenues par M. KAMBOU et ses proches, locales et internationales.
- Pandora Papers : recherche par nom (et variantes) → 2 résultats : un trust enregistré à Jersey, contributeur M. KAMBOU, bénéficiaires sa famille étendue. Date de création : 6 mois avant la sortie de fonctions.
- Marchés publics du pays d’origine : presse, rapports d’organisations internationales (Transparency International, Global Witness, OECD Working Group). Plusieurs grands marchés (mines, infrastructures) attribués pendant le mandat de M. KAMBOU à des consortia étrangers.

**Adverse media** :

- 3 articles d’investigation (OCCRP, Reuters, presse locale) mentionnent M. KAMBOU dans le contexte de l’attribution de marchés contestés, sans poursuites formelles à ce stade.

**Profilage des sources de revenus déclarées (« conseil ») **:

- Sociétés clientes identifiées : 4 entités basées dans des juridictions de holding (Maurice, Luxembourg, Émirats). UBO de 2 de ces entités : liés à des consortia ayant remporté des marchés publics pendant le mandat de M. KAMBOU.

#### Analyse

**Cohérence revenus / activité de conseil** :

- Les « conseils » facturés totalisent 8 M€ sur 18 mois, à 4 entités.
- Aucune des entités clientes n’a de site web ni d’activité opérationnelle traçable autre que des participations dans les consortia.
- Les montants des facturations sont disproportionnés par rapport à un conseil stratégique standard.
- Lecture : *probable* mécanisme de rétrocommissions différé, où les bénéficiaires de marchés publics rémunèrent l’ancien ministre par contrat de conseil après sortie de fonctions.

**Lien avec marchés publics** :

- 2 des 4 entités clientes sont liées à des consortia ayant remporté des marchés publics sous le mandat de M. KAMBOU pour des valeurs cumulées > 200 M$.
- La temporalité est cohérente avec un schéma de rétrocommissions.

**Patrimoine actuel** :

- Patrimoine déclaré à l’entrée : 3,5 M€.
- Crédits cumulés sur 18 mois : 12 M€.
- Sortie majeure : 6,8 M€ vers immobilier européen (Suisse, Sud de la France, Londres).
- Solde actuel : ~4 M€ sur le compte + actifs financiers ~5 M€ + immobilier 6,8 M€ = ~15 M€.
- Évolution : patrimoine multiplié par > 4 en 4 ans hors-mandat.

#### Hypothèses calibrées

- **H1 — Rétrocommissions différées (corruption transnationale latente)** : probable.
- **H2 — Conseil stratégique légitime, à très haute valeur ajoutée** : peu probable, vu l’absence de traçabilité de l’activité de conseil réelle et la corrélation temporelle avec les marchés.
- **H3 — Combinaison de sources légitimes et illicites** : possible.

#### Limites

- Sans coopération internationale (notamment via Egmont avec la CRF du pays d’origine), la qualification définitive est *indéterminable*.
- La présomption d’innocence demeure : M. KAMBOU n’a pas été condamné.
- Les contrats de conseil peuvent être légalement formalisés, ce qui complique la qualification pénale.

#### Livrable

Rapport à la banque BANQUE-PARTNER :

- Le profil et l’activité du compte sont *probable* compatibles avec un schéma de rétrocommissions de corruption transnationale antérieures.
- Recommandations :
  - **Déclaration de soupçon à la CRF nationale** (TRACFIN équivalent local) : suffisamment d’éléments pour DS.
  - **Vigilance renforcée maximale** : limitation des opérations, demandes systématiques de justificatifs.
  - **Évaluer la rupture** de la relation d’affaires : décision banque selon politique interne et avis juridique.
  - **Coopérations Egmont** : la CRF pourra solliciter la CRF du pays d’origine pour qualifier les marchés publics.

#### Bilan honnête

Une enquête de due diligence approfondie ne **prouve pas** la corruption. Elle qualifie un **profil de risque** avec un niveau de confiance *probable* à élevé. La décision opérationnelle (rupture, signalement, vigilance) appartient à la banque. La qualification judiciaire éventuelle relève de la procédure pénale dans le pays d’origine ou via Convention OCDE Anti-Corruption (1997).

#### Leçons FININT

- Le **statut PEP** déclenche une vigilance, pas une accusation.
- La **temporalité** (sortie de fonctions → début de l’activité de conseil → flux entrants des bénéficiaires de marchés) est centrale.
- **Pandora et leaks** sont essentiels pour les volets offshore.
- La banque, dans ce cas, est **assujetti** et a une obligation de DS si soupçon ; le cabinet conseille mais ne décide pas.

-----

### Chapitre 58 — Cas 4 : Contournement de sanctions via pays tiers

#### Contexte

Une banque française, **BANQUE-X**, identifie via son monitoring un client commercial atypique : une SAS française récemment créée, **EUROFLUX SARL**, qui présente une explosion d’activité avec une contrepartie turque. Les flux sont importants (~3 M€ sur 2 mois) et la nature des opérations (négoce de matériel industriel sensible) attire l’attention.

La compliance déclenche une analyse FININT interne et sollicite TRACFIN via DS.

**Demande (interne CRF)** : qualifier le profil de risque, vérifier la possibilité d’un contournement de sanctions, recommander des suites.

#### Indices initiaux

- EUROFLUX SARL : créée 5 mois avant les premiers flux. Capital 5 K€. Dirigeant : un Français, 30 ans, parcours professionnel principalement dans la logistique générale.
- Contrepartie turque : ATLAS TECHNICAL TRADING (société turque créée 7 mois plus tôt).
- Flux observés : 3 M€ entrants depuis ATLAS, libellés « industrial equipment » et « technical components ».
- Sorties : achats auprès de fournisseurs européens (Allemagne, Italie, Pays-Bas) de matériel électronique sensible (CNC, composants industriels avancés).
- Destinations finales déclarées : exports vers Turquie (déclarations douanières).

#### Cadrage

**Questions de renseignement** :

- QR1 — Quel est le profil réel d’EUROFLUX et d’ATLAS ?
- QR2 — Les biens commercialisés sont-ils dual-use ?
- QR3 — Y a-t-il un soupçon de réexportation vers une juridiction sanctionnée ?
- QR4 — Quels UBO et liens entre EUROFLUX, ATLAS, et éventuelles entités sanctionnées ?

#### Collecte

**OSINT** :

- Pappers : EUROFLUX dirigée par M. T, sans expérience visible dans le secteur. UBO RBE : M. T lui-même.
- Recherche M. T : LinkedIn minimal, pas de réseau apparent dans la tech industrielle.
- Adresse EUROFLUX : cabinet de domiciliation parisien, 21 autres entités.
- Recherche ATLAS Technical Trading (Turquie) : registre turc accessible — UBO turc, M. Ö, 45 ans, parcours dans le négoce général à Istanbul.
- Recherche presse : ATLAS est mentionnée dans un article OCCRP de 2024 sur des sociétés turques utilisées pour acheminement de biens vers la Russie (sanctions UE et US).

**Sanctions et listes** :

- M. Ö (UBO d’ATLAS) : pas sur les listes OFAC, UE, OFSI.
- ATLAS : pas sur les listes.
- Sociétés liées (recherche par M. Ö) : plusieurs sociétés dirigées par M. Ö, dont une avait des liens commerciaux antérieurs avec une entreprise russe **désormais sanctionnée** depuis 2022.

**Nature des biens** :

- Liste détaillée des achats EUROFLUX auprès des fournisseurs européens : composants CNC, contrôleurs PLC, certains équipements de capteurs.
- Vérification dual-use : plusieurs des composants sont sur la **liste UE dual-use** (règlement 2021/821), exigeant licence d’exportation pour certaines destinations.

**Vérification douanière** :

- Déclarations douanières françaises : exports vers Turquie déclarés.
- Pas de vérification immédiate de la destination réelle après Turquie.

#### Analyse

**Profil EUROFLUX** : société créée récemment, dirigeant inexpérimenté, domiciliation, faible substance économique propre. *Probable* société écran ou opérationnelle pour un schéma spécifique.

**Profil ATLAS** : société turque créée récemment, mais avec un UBO qui a des liens antérieurs (sociétés liées) avec une entreprise russe désormais sanctionnée.

**Schéma probable** : EUROFLUX achète en Europe des biens dual-use, vend à ATLAS en Turquie. ATLAS réexporte (potentiellement) vers une destination sanctionnée (probablement Russie). Le schéma est typique d’un **contournement de sanctions UE/US** via pays tiers.

**Éléments confortants** :

- Nature des biens (dual-use).
- Lien historique UBO ATLAS / entité russe sanctionnée.
- Volume soudain (3 M€ en 2 mois pour une société de 5 K€ de capital).
- Pas d’activité économique antérieure d’EUROFLUX cohérente avec le secteur.

#### Hypothèses calibrées

- **H1 — Contournement de sanctions UE/US via pays tiers (Turquie)** : probable.
- **H2 — Schéma de commerce parallèle légal mais douteux** : possible.
- **H3 — Pure activité commerciale Europe-Turquie** : peu probable au vu de la nature des biens et du profil ATLAS.

#### Limites

- Sans vérification de la destination réelle après Turquie, le contournement reste *probable*, pas *quasi-certain*.
- Coopération douanière France-Turquie est complexe (Turquie n’est pas dans l’UE).
- Le volet renseignement avec services spécialisés (DG Trésor pôle sanctions, DGDDI, équivalent dans services de défense) est central.

#### Livrable

Note FININT interne CRF + signalement :

- Profil de risque *probable* de contournement de sanctions, biens dual-use.
- Recommandations :
  - DS validée et enrichie, transmission au PNF (équivalent fiction).
  - Saisine immédiate de la DG Trésor (pôle sanctions financières) (Direction Générale du Trésor — sanctions) et des services douaniers (DGDDI).
  - Coopération Egmont avec la CRF turque pour qualifier ATLAS et son réseau.
  - Possibilité de gel administratif si éléments suffisants confirment l’attribution sanctionnée.

#### Bilan honnête

Le contournement de sanctions est une typologie particulièrement sensible. La qualification définitive est souvent **politique** autant que judiciaire. Le rôle de la CRF est de produire un dossier solide et de saisir les autorités spécialisées. Les sanctions secondaires OFAC (impact sur les opérateurs européens) ajoutent une dimension géopolitique. Le dossier peut conduire à des suites variées : enquête judiciaire en France, sanctions sur les acteurs (gel), pression diplomatique sur la Turquie pour coopération.

#### Leçons FININT

- **Pays tiers** (Turquie, Émirats, Géorgie, Arménie, Asie centrale) sont des canaux d’attention prioritaire depuis 2022.
- **Biens dual-use** : connaître la liste UE, qui est mise à jour régulièrement.
- **UBO et liens passés** : un UBO non sanctionné mais lié historiquement à une entité sanctionnée = signal majeur.
- **Coordination inter-services** : sanctions ≠ FININT seul. DG Trésor (pôle sanctions financières internationales), DGDDI, MAE, parfois services de défense interviennent.

-----

### Chapitre 59 — Cas 5 : Asset tracing d’un dirigeant sous enquête

#### Contexte

Un magistrat instructeur français saisit, par réquisition, une cellule spécialisée pour l’**asset tracing** d’un dirigeant français, **M. RIVIÈRE**, mis en examen pour escroquerie aggravée à hauteur de 15 M€. Le magistrat soupçonne une dissipation patrimoniale en cours et souhaite **identifier les actifs susceptibles d’une mesure conservatoire** (gel, saisie).

L’enquête a déjà identifié les flux frauduleux principaux et certains comptes bancaires français. Mais le patrimoine étranger et les structures offshore éventuelles restent à identifier.

**Demande** : asset tracing complet pour mesure conservatoire urgente.

#### Indices initiaux

- M. RIVIÈRE, 55 ans, ancien dirigeant d’une PME en redressement.
- Mises en cause : ventes fictives via faux clients, fraude TVA et abus de biens sociaux. Préjudice estimé 15 M€.
- Comptes français : 6 comptes identifiés, soldes cumulés actuels ~280 K€. *Insuffisant* pour mesure conservatoire significative.
- Patrimoine français déclaré (déclarations fiscales) : 2 résidences, 1 SCI, ~2 M€ valeur.
- Signaux : voyages réguliers à Dubaï et Genève depuis 18 mois, train de vie présomé supérieur au patrimoine déclaré.

#### Cadrage

**Questions de renseignement** :

- QR1 — Quels actifs cachés ou indirects ? Immobilier étranger ? Comptes étrangers ? Structures offshore ?
- QR2 — Y a-t-il des prête-noms ou des structures interposées ?
- QR3 — Quelle est la trajectoire récente du patrimoine (dissipation ? consolidation ?) ?
- QR4 — Quels actifs sont juridiquement susceptibles de mesure conservatoire ?

**Délai** : 4 semaines (mesure conservatoire à décider rapidement).

#### Collecte

**Sources ouvertes** :

- DVF + cadastre : identification des biens français.
- Pappers : sociétés détenues par M. RIVIÈRE et ses proches.
- LinkedIn + presse + réseaux sociaux : profilage, identification de relations et de localisations.
- Patrim (accessible CRF) : revenus et patrimoine déclarés.
- Reverse image search : identification du yacht visible sur Instagram.

**Sources fermées (en cadre judiciaire)** :

- FICOBA : tous les comptes bancaires en France au nom de M. RIVIÈRE et de ses proches identifiés.
- FICOVIE : assurances-vie.
- EAR/CRS (via demande administrative en coopération avec DGFiP) : comptes étrangers déclarés.
- Réquisitions auprès de banques françaises : relevés détaillés.

**Coopérations internationales** :

- Egmont avec MROS (Suisse) : confirmation d’1 compte privé à Genève, soldes et historiques.
- Egmont avec CRF émiratie : identification de 2 sociétés free zone (Dubaï) liées à un proche collaborateur — *probable* UBO M. RIVIÈRE via prête-nom.
- Recherche presse mondaine : photos de M. RIVIÈRE devant un appartement à Dubaï (identifiable au quartier).

#### Analyse

**Cartographie patrimoniale consolidée** :

```
France
├─ 2 résidences (déclarées) — 2 M€
├─ SCI (déclarée) — 1 M€
├─ 6 comptes bancaires — 280 K€
└─ 2 contrats assurance-vie — 850 K€

Suisse
└─ 1 compte banque privée Genève — 3,2 M€ (EAR/CRS + coop MROS)

Émirats
├─ 1 LLC Dubaï détentrice apparente d'un appartement à Dubaï Marina — valeur estimée ~1,8 M€
├─ 1 autre LLC sans actifs clairs — possible société écran
└─ Pas d'autres comptes identifiés à ce stade

Yacht
└─ Pavillon Malte, valeur estimée 1,2 M€, propriété via société écran maltaise

Total identifié : ~10,4 M€ (vs préjudice 15 M€).
```

**Dissipation observable** : sur les 6 derniers mois (post-mise en examen), virements totaux de 1,8 M€ depuis comptes français vers Suisse et Dubaï. *Probable* dissipation active.

#### Hypothèses calibrées

- M. RIVIÈRE détient une fraction significative des fonds frauduleux dans des structures étrangères : quasi-certain.
- Une partie du patrimoine identifié (Suisse, Dubaï, yacht) est saisissable sous procédure judiciaire et coopérations internationales : probable.
- Dissipation active en cours : quasi-certain.

#### Livrable

Rapport au magistrat instructeur :

- Cartographie patrimoniale consolidée : ~10,4 M€ identifiés.
- Actifs prioritaires pour mesures conservatoires :
  - France : saisine AGRASC pour gel et saisie des biens immobiliers et comptes.
  - Suisse : demande d’entraide pour gel via MROS et coopération judiciaire.
  - Émirats : demande d’entraide judiciaire (plus complexe et plus longue).
  - Yacht : possible saisie sous pavillon Malte (coopération MLA).
- Recommandation d’urgence : geler immédiatement les comptes français pour stopper la dissipation, puis enchaîner les coopérations internationales en parallèle.

#### Bilan honnête

L’asset tracing a permis d’identifier ~10,4 M€ d’actifs (vs 15 M€ de préjudice). Le recouvrement réel dépend de :

- Réactivité des autorités (gel français immédiat).
- Vitesse des coopérations internationales (Suisse rapide, Émirats lent, Malte intermédiaire).
- Qualité juridique du dossier d’enquête (la mesure conservatoire repose sur la solidité de l’enquête pénale).

Récupération espérée : une **fraction significative** du patrimoine identifié si action rapide et coopération satisfaisante, sur le préjudice global, le recouvrement est **structurellement partiel**, sur 18 à 36 mois ou plus. Les ordres de grandeur donnés dans le cours sont **pédagogiques** ; la réalité varie fortement selon les juridictions, la qualité du dossier judiciaire, la coopération et les stratégies de protection adverses.

#### Leçons FININT

- L’**asset tracing** combine OSINT (signaux visibles), sources fermées (FICOBA, EAR/CRS), et coopération internationale.
- La **rapidité** d’action conditionne le résultat (dissipation possible en parallèle).
- La **coopération avec AGRASC** en France et équivalents étrangers est indispensable.
- Les juridictions varient en réactivité : Suisse, UK, Allemagne sont relativement coopératifs ; Émirats, Asie, Liban beaucoup moins.

-----

## PARTIE X — CAS HISTORIQUES, COOPÉRATION ET PROFESSIONNALISATION

*Dix chapitres pour clore le cours : quatre cas historiques exploités comme leçons méthodologiques, la synthèse du fil rouge CLEARFLOW, et cinq chapitres de professionnalisation (coopération internationale, asset recovery, cadre français, éthique, capacité durable).*

-----

### Chapitre 60 — Panama Papers : leak, offshore et journalisme d’investigation

#### Contexte et faits

En avril 2016, un consortium international de journalistes coordonné par l’**ICIJ** (International Consortium of Investigative Journalists), à l’initiative du quotidien allemand **Süddeutsche Zeitung**, publie l’enquête « Panama Papers ». Source : 11,5 millions de documents (2,6 To de données) couvrant 40 ans d’activité du cabinet juridique panaméen **Mossack Fonseca**, transmis par un lanceur d’alerte anonyme (« John Doe ») au journaliste Bastian Obermayer.

Le contenu : structures offshore créées pour des dizaines de milliers de clients à travers le monde, dont chefs d’État (Vladimir Poutine via son entourage, le Premier ministre islandais Sigmundur Davíð Gunnlaugsson, le roi Salmane d’Arabie saoudite, le président argentin Mauricio Macri), oligarques, hommes d’affaires, célébrités, et criminels.

#### Mécanisme financier

Le cabinet Mossack Fonseca offrait des **services de constitution et gestion** de structures offshore : sociétés écrans, fondations, trusts dans diverses juridictions (BVI, Panama, Bahamas, Seychelles, etc.). Selon les cas :

- Optimisation fiscale légale mais agressive.
- Dissimulation d’avoirs aux autorités fiscales.
- Contournement de sanctions.
- Dissimulation de proceeds de corruption.
- Évasion fiscale.

#### Méthodes d’enquête

L’ICIJ a coordonné **376 journalistes dans 76 pays**, avec :

- Hébergement et indexation des données.
- Plateforme commune (Blacklight, puis Aleph).
- Coordination temporelle des publications.
- Vérifications individuelles dans chaque pays.
- Confrontation des personnes citées avant publication.

L’enquête a duré **plus d’un an** avant publication. Les vérifications ont été menées avec rigueur méthodologique : croisement registres locaux, vérification des titulaires, confrontation aux concernés.

#### Conséquences

- **Démission du Premier ministre islandais.**
- **Démission du Premier ministre pakistanais Nawaz Sharif** (un an plus tard).
- Investigations dans plus de 80 pays.
- **Recouvrement d’environ 1,3 milliard USD** de taxes et amendes au niveau mondial (chiffres ICIJ).
- Réformes législatives sur la transparence des UBO (renforcement des directives AML UE notamment).
- Mossack Fonseca fermé en 2018.

#### Leçons FININT

- Les **leaks** sont devenus une source d’enquête majeure. Aujourd’hui, ICIJ Offshore Leaks reste consultable et utilisable (chapitre 18).
- La **coopération internationale** entre journalistes a été un modèle reproduit pour Paradise (2017), Pandora (2021), Cyprus Confidential (2023), etc.
- **Présence dans Panama ≠ culpabilité** : la majorité des clients de Mossack Fonseca avaient des motifs légaux. La nuance est essentielle.
- **Vitesse, échelle et discipline** : enquêter sur 2,6 To exige outils techniques, méthodologie, coordination.
- **Transparence post-leaks** : pression réglementaire accrue (registres UBO, EAR/CRS, AMLA).

-----

### Chapitre 61 — 1MDB : corruption, banques, luxe et asset recovery

#### Contexte et faits

**1MDB (1Malaysia Development Berhad)** est un fonds souverain malaisien créé en 2009 par le Premier ministre Najib Razak. Officiellement destiné à des investissements stratégiques. Réellement utilisé comme vecteur de détournement massif.

Estimation des fonds détournés : **environ 4,5 milliards USD** entre 2009 et 2014 (chiffres DOJ). Acteurs principaux : le Premier ministre Najib Razak, le financier malaisien **Jho Low**, et un réseau de complices et facilitateurs.

#### Mécanisme financier

Le détournement a combiné plusieurs typologies :

- **Emprunts obligataires** sur les marchés internationaux, organisés avec **Goldman Sachs** (commissions énormes versées à la banque, et fonds détournés au profit du réseau).
- **Faux investissements** dans des partenariats fictifs (Petrosaudi notamment).
- **Layering** via comptes et sociétés écrans en Suisse, Singapour, Luxembourg, Émirats, BVI.
- **Intégration** dans des actifs spectaculaires : œuvres d’art (Van Gogh, Monet, Picasso), bijoux, jets privés, propriétés à Beverly Hills et Londres, financement du film « Le Loup de Wall Street » (Leonardo DiCaprio).

#### Méthodes d’enquête

- **Banques privées** ont, dans plusieurs cas, été défaillantes en KYC et monitoring. **BSI Bank** (Suisse) sanctionnée et liquidée par la FINMA. **Falcon Bank** sanctionnée. **DBS Singapore** et **Standard Chartered** mises en cause.
- **Coopération internationale** : DOJ américain en pointe (poursuites civiles et pénales). Singapour, Suisse, Émirats, Luxembourg coopérants. Malaisie initialement réticente (après changement politique 2018, coopération accrue).
- **Asset tracing** : suivi des fonds depuis 1MDB jusqu’aux actifs finaux (œuvres, immobilier).
- **Témoignages** : Jho Low en fuite, plusieurs complices ayant collaboré contre réduction de peine.

#### Conséquences

- **Najib Razak** condamné en 2022 à 12 ans de prison.
- **Goldman Sachs** : amende de 2,9 milliards USD aux US et autres juridictions ; un ancien directeur poursuivi.
- **Récupération d’actifs** : plusieurs centaines de millions USD recouvrés (œuvres d’art, immobilier, fonds).
- **Réformes en Malaisie** et pression sur banques internationales pour renforcement compliance.
- **Jho Low** : fuite, soupçonné d’être en Chine, mandat international.

#### Leçons FININT

- **L’asset recovery** est un effort de plusieurs années, multi-juridictions, avec coopération essentielle.
- **Les banques privées** sont un point critique : leurs défaillances KYC/AML peuvent permettre des détournements massifs.
- **Les actifs spectaculaires** (art, immobilier de luxe) sont souvent l’étape d’intégration finale — ils laissent des traces (ventes aux enchères, registres immobiliers).
- **L’enchevêtrement banque / fonds souverain / politique** rend les dossiers extrêmement complexes.
- **La sanction des banques** (FINMA, MAS, autorités US) montre que les institutions sont responsables de leur compliance, pas seulement les clients.

-----

### Chapitre 62 — Wirecard : fraude comptable et défaillance systémique

#### Contexte et faits

**Wirecard AG** était un fleuron allemand du paiement digital. Coté au DAX, valorisé à plus de 24 milliards € en 2018. En juin 2020, la société reconnaît que **1,9 milliard €** de trésorerie déclarée aux Philippines et à Singapour **n’existe pas**. La société dépose le bilan. Son CEO Markus Braun est arrêté ; le COO Jan Marsalek prend la fuite et reste fugitif.

#### Mécanisme financier

Wirecard a, pendant des années, **gonflé son chiffre d’affaires et sa trésorerie** par des opérations fictives :

- Faux clients revendiqués en Asie du Sud-Est (notamment des « TPA » — Third Party Acquirers).
- Faux comptes bancaires bloqués (« escrow accounts ») prétendant détenir des liquidités.
- Faux audits, faux contrats.
- Activités probablement réelles dans des secteurs « adultes » et « jeux d’argent en ligne » mal documentés.

Le ratio entre flux financiers réels et flux déclarés était massivement dégradé. Le commissaire aux comptes (EY) a, pendant des années, accepté des documents non vérifiés.

#### Méthodes d’enquête

L’enquête a été déclenchée principalement par :

- **Le Financial Times** (Dan McCrum) qui a publié pendant 5 ans des enquêtes étayées, malgré pressions juridiques massives de Wirecard.
- **Vendeurs à découvert** (short sellers) qui ont identifié les anomalies et publié des analyses.
- **Lanceurs d’alerte internes**.

L’investigation officielle (Bafin, parquet de Munich) a longtemps **sous-estimé** ou **mal interprété** les signaux. La Bafin a même un temps **interdit les ventes à découvert** sur l’action Wirecard et porté plainte contre des journalistes du FT — réaction qui s’est avérée catastrophiquement à contre-courant.

#### Conséquences

- **Faillite de Wirecard** en juin 2020.
- **Markus Braun** poursuivi, jugé, condamné.
- **Jan Marsalek** : en fuite, soupçons d’activités de renseignement et liens avec services russes (révélations 2024+).
- **EY** : poursuites en cours, sanction probable des autorités d’audit.
- **Bafin** : réforme en profondeur, renforcement des pouvoirs.
- **Réformes** : législation allemande sur l’audit et la supervision financière.

#### Leçons FININT

- **Les analystes externes** (FT, short sellers, lanceurs d’alerte) peuvent voir ce que les autorités officielles ne voient pas — quand le système institutionnel est défaillant ou capturé.
- **La fraude comptable à grande échelle** peut prospérer des années même dans une juridiction développée, si auditeurs et régulateurs sont défaillants.
- **La pression juridique** sur les enquêteurs (procès en diffamation, harcèlement) est une **technique de défense classique** des fraudeurs — il faut savoir y résister.
- **La supervision** dépend autant des autorités que des contre-pouvoirs (presse, marchés, lanceurs d’alerte).
- **La dimension géopolitique** émerge a posteriori : Jan Marsalek et liens avec services russes — illustrant que la criminalité financière peut s’imbriquer avec d’autres enjeux.

-----

### Chapitre 63 — Danske Bank Estonia : blanchiment massif et supervision défaillante

#### Contexte et faits

**Danske Bank**, la principale banque danoise, exploitait une **succursale en Estonie**. Entre 2007 et 2015, cette succursale a transité environ **200 milliards € de flux non-résidents**, dont une part très significative (estimations 7 à 200 milliards selon les sources) jugée *suspecte* et probablement liée à des activités de blanchiment.

Origines majeures des flux : Russie, ex-URSS, divers réseaux criminels et de fraude fiscale.

#### Mécanisme financier

La succursale estonienne a :

- Acquis (en 2007) une banque locale (**Sampo Bank Estonia**) avec une clientèle internationale « non-résidents » importante.
- Maintenu cette clientèle malgré multiples alertes internes et externes (lanceurs d’alerte, audits, signalements).
- Géré les flux via un système séparé du système central de Danske, contournant les contrôles AML standard de la maison mère.

Le **layering** typique impliquait :

- Sociétés écrans britanniques (notamment Scottish Limited Partnerships avant 2017 — alors quasi-transparentes).
- Transits multi-banques.
- Bénéficiaires effectifs masqués.

#### Méthodes d’enquête

L’enquête a impliqué :

- **Lanceurs d’alerte internes** (notamment Howard Wilkinson, ancien dirigeant local).
- **Enquêtes journalistiques** (FT, OCCRP, médias danois).
- **Autorités** : FSA Danemark, banque centrale d’Estonie (BCE), DOJ US (le dollar a transité via banques US correspondantes).
- **Coopération internationale** : nombreuses CRF saisies (UK, US, Estonie, Lettonie, Danemark, Russie).

#### Conséquences

- **Sanction financière** : Danske Bank reconnaît la fraude. Amende DOJ US en 2022 : ~2 milliards USD (l’une des plus grosses amendes AML jamais infligées).
- **Démissions** : direction Danske.
- **Fermeture** de la succursale estonienne.
- **Réforme bancaire estonienne** et nordique.
- **Réformes UE** : impulsion vers AMLA (Anti-Money Laundering Authority européenne).
- **Le scandale a entraîné** des affaires connexes (Swedbank, Nordea) — révélant une faiblesse régionale de supervision.

#### Leçons FININT

- **La supervision** d’une succursale étrangère par la maison mère peut être déficiente — surtout quand elle est rentable.
- **Les lanceurs d’alerte** sont souvent les déclencheurs, malgré pressions et risques.
- **L’extraterritorialité** du dollar : tout flux en USD transite par des banques correspondantes US, ce qui donne juridiction au DOJ.
- **Les défaillances de supervision** ont conduit à la création de l’AMLA — institution européenne de supervision LCB-FT direct sur les grandes institutions.
- **L’échelle** peut être massive : 200 milliards € en 8 ans dans une seule succursale est une illustration de l’ampleur potentielle des défaillances.

-----

### Chapitre 64 — Synthèse du fil rouge CLEARFLOW

#### Reprise du dossier

Le dossier **CLEARFLOW** a commencé par 17 DS convergentes adressées à la cellule de renseignement financier (CRF) fictive — inspirée du fonctionnement de TRACFIN — sur un homme d’affaires franco-libanais, **Karim Élie Haddad**, et son réseau économique multi-juridictionnel.

#### Travail réalisé sur 8 semaines

**Stabilisation et identification** :

- 14 entités identifiées dans 7 juridictions : France (4 SAS), UK (2 Limited), Chypre (NEXUS HOLDINGS LTD + OMEGA TRUST), Émirats (NEXUS INTERNATIONAL FZ + autres free zone), Luxembourg (SOPARFI), Delaware (LLC), Liban (NEXUS LIBAN SAL), Bénin et Côte d’Ivoire (filiales opérationnelles).
- 12 personnes physiques avec mandats. Distinction *probable* prête-noms / *probable* collaborateurs de confiance / *quasi-certain* UBO réel (Karim Haddad).

**Coopérations engagées** :

- FIU.NET (UE) : retours sur fintechs.
- Egmont : Mokas (CY) — partiellement reçu, Liban (peu coopératif).
- Coopération bilatérale Émirats — en cours, lenteur.
- Athéna Group (Sarah Marin) : rapport on-chain reçu sur les conversions USDT (volet crypto secondaire).
- Coopération douanière France (DGDDI) : amorcée pour qualifier les flux physiques déclarés.

**Volumétrie analysée** :

- ~5 600 opérations sur 18 mois cumulées sur les 4 SAS françaises.
- ~22 M€ de flux entrants (multi-origines).
- ~16 M€ de flux sortants vers étranger (Suisse, Chypre, Émirats principalement).
- ~6 M€ de flux divers (acquisitions, dépenses, prélèvements personnels).

#### Hypothèses retenues et calibrées

- **H1 — Réseau de transit financier multi-juridictionnel à finalité d’opacification et d’évasion fiscale** : *quasi-certain*. Substance économique déficiente sur la majorité des entités, charges intragroupe disproportionnées, schéma typique d’évasion vers Chypre et offshore.
- **H2 — Schéma de TBML sur les imports déclarés depuis Bénin et exports vers Côte d’Ivoire** : *probable*. Incohérences valeur facture / valeur de marché, contreparties commerciales sans substance vérifiable.
- **H3 — Corruption autour des marchés publics ouest-africains (Côte d’Ivoire principalement)** : *probable*. Pattern de favoritisme, sur-facturation du marché ivoirien (×2), liens probables avec des hauts fonctionnaires ivoiriens (à confirmer en coopération).
- **H4 — Contournement opportuniste de sanctions via réseau commercial** : *possible* à ce stade. Aucun lien direct avec entité sanctionnée démontré ; à approfondir.
- **H5 — Branche BEC où les SAS françaises servent d’infrastructure de mules** : *possible*. Au moins un cas documenté (215 K€), à vérifier sur le périmètre complet.
- **H6 — Volet crypto comme rail de cashout secondaire** : *probable* sur la base du rapport Athéna ; pas le canal principal du réseau.

#### Identification de Karim Haddad comme UBO réel

Niveau de confiance final : **très probable** à **quasi-certain**.

- Settlor identifié du trust OMEGA (Pandora — quasi-certain).
- Chaîne de capital remontée jusqu’à Haddad sur 8 entités sur 14.
- Profil de contrôle effectif (signatures, voyages, présence aux événements professionnels).
- Bénéficiaire ultime des sorties principales du réseau (immobilier, comptes Suisse, train de vie).

#### Patrimoine identifié

- France visible : ~11,3 M€ (immobilier via SCI, véhicules).
- Suisse : ~3,2 M€ (compte banque privée).
- Émirats : ~3 M€ présumés (LLC, appartement).
- Yacht (Malte) : ~1,2 M€.
- Participations dans le groupe : 8-15 M€ (valorisation difficile).
- Total : 25 à 35 M€ — cohérent avec un négociant international à succès, mais avec construction multi-juridictionnelle opaque suggérant des fins de planification fiscale agressive et possiblement d’évasion fiscale.

#### Recommandations transmises

1. **Saisine du PNF (Parquet National Financier)** avec dossier complet : volet évasion fiscale, ABS, soupçons de TBML et corruption transnationale.
1. **Article 40 CPP** transmission aux autorités douanières et fiscales (DGDDI, DGFiP) pour quaifications spécifiques.
1. **Mesures conservatoires** sur les actifs français immédiatement (saisine AGRASC).
1. **Coopérations internationales** : poursuite des coopérations en cours et nouvelles sollicitations (Côte d’Ivoire, Liban, Suisse pour gel).
1. **Dissémination Egmont** vers les CRF concernées pour qualification des entités étrangères.
1. **Monitoring continu** sur les comptes français connus pour détecter dissipation.

#### Bilan honnête

Le dossier **n’aboutit pas** à un dénouement spectaculaire. Il aboutit à :

- Un **renseignement actionnable** transmis aux autorités compétentes.
- Une cartographie cohérente d’un réseau probablement structuré pour évasion / optimisation agressive.
- Des hypothèses calibrées sur des typologies plus graves (TBML, corruption) qui nécessitent confirmations judiciaires et coopérations à venir.
- Des recommandations opérationnelles immédiates (mesures conservatoires) et de long terme (coopérations).

Le **chemin judiciaire** ultérieur (mise en examen éventuelle, poursuites, jugement) prendra **plusieurs années**. Le **recouvrement éventuel** sera, comme dans la grande majorité des dossiers complexes multi-juridictionnels, **structurellement partiel** : tout dépend de la qualité du dossier judiciaire, de la rapidité du gel initial, et de la coopération des juridictions concernées. Une partie significative du dossier restera **non concluante** : volets ivoirien et libanais difficilement accessibles, branches secondaires non investiguées par contrainte de ressources.

C’est la **réalité opérationnelle** d’une enquête FININT complexe : ni triomphe ni échec, mais **production de renseignement utile** qui permet à d’autres acteurs (PNF, services nationaux, coopérations étrangères) de continuer le travail.

#### Leçons de CLEARFLOW

- **Discipline de cadrage** : sans QR précises, on s’égare.
- **Stabilisation des identités** avant toute analyse de fond.
- **Calibration WEP systématique** : la note finale est crédible parce qu’elle dit ce qu’elle sait et ce qu’elle ne sait pas.
- **Coopérations multiples** : aucune enquête multi-juridictionnelle n’avance sans elles.
- **Articulation FININT / OSINT Crypto** : chacun fait son métier, le rapport FININT renvoie.
- **Pas de happy ending** : le FININT produit du renseignement actionnable, pas la conclusion judiciaire.

-----

### Chapitre 65 — Coopération internationale : Egmont, GAFI, Europol, FIU

#### Objectif

Maîtriser les **principaux canaux de coopération internationale** mobilisables dans une enquête FININT — leurs périmètres, leurs limites, leurs délais.

#### Le concept

Aucune enquête FININT multi-juridictionnelle n’aboutit sans coopération. Plusieurs niveaux et canaux coexistent :

**Egmont Group** : réseau mondial des **Cellules de Renseignement Financier (CRF / FIU)**, créé en 1995, basé à Toronto. ~170 CRF membres. Coopération CRF-CRF par échange sécurisé via Egmont Secure Web (ESW). Demandes de renseignement, réponses, dissémination. Pas une autorité opérationnelle : un canal d’échange. Délais variables (jours à mois selon membres).

**FIU.NET** : réseau européen des CRF de l’UE et apparentés. Plus rapide et plus structuré qu’Egmont pour les coopérations UE. Adossé à Europol.

**GAFI / FATF** : organisme intergouvernemental (basé à Paris, OCDE), 40 recommandations sur LCB-FT, listes (noire, grise) des juridictions à risque, méthodologie d’évaluation. Pas un canal de coopération opérationnel, mais cadre normatif.

**Europol** : agence européenne de police, basée à La Haye. ECTC (Centre Européen Contre le Terrorisme), EC3 (Centre Européen de Cybercriminalité), EFECC (Centre Européen Économique et Financier). Coopération entre services nationaux d’enquête (police, gendarmerie).

**Interpol** : organisation mondiale de police, 196 États membres, basée à Lyon. Notices (red notice pour arrestation, blue notice pour information, etc.). Coopération entre forces de police nationales.

**Eurojust** : agence européenne de coopération **judiciaire** (procureurs, magistrats). Particulièrement utile pour l’asset recovery et les saisies transfrontalières.

**Parquet européen (EPPO)** : créé en 2021, compétent pour les infractions portant atteinte aux intérêts financiers de l’UE (fraude TVA, détournement de fonds européens, corruption transnationale). Procédure judiciaire harmonisée entre les 22 États membres participants.

**Réseau Camden Asset Recovery Inter-agency (CARIN)** : réseau informel pour l’asset recovery international.

**Conventions** :

- **Convention OCDE Anti-Corruption** (1997).
- **Convention ONU contre la Corruption** (Mérida, 2003).
- **Convention de Strasbourg** sur le blanchiment (1990, révisée Varsovie 2005).
- **Conventions bilatérales d’entraide judiciaire** (MLA — Mutual Legal Assistance).

#### Méthode — choix du canal selon le besoin

- **Renseignement entre CRF** : Egmont (mondial), FIU.NET (UE).
- **Coopération policière** : Europol, Interpol.
- **Coopération judiciaire** : Eurojust, EPPO si compétence, MLA bilatéral.
- **Asset recovery** : CARIN, MLA, Eurojust, EPPO selon contexte.
- **Standards et normes** : GAFI (cadre, pas opération).

#### Délais réalistes

- FIU.NET : quelques jours à 2 semaines pour réponse standard.
- Egmont : 1 à 8 semaines.
- MLA bilatéral : 3 à 18 mois (parfois plus).
- EPPO : variable, mais procédure intégrée plus rapide.
- Réquisitions judiciaires directes (sans MLA) : impossible dans la grande majorité des cas.

#### Mini-walkthrough

Dans CLEARFLOW, Nassim mobilise :

- FIU.NET pour fintechs européennes (réponse 8-11 jours).
- Egmont avec Mokas Chypre (réponse 3 semaines, partielle).
- Egmont avec CRF émiratie (réponse 6 semaines, partielle).
- Egmont avec Liban : pas de réponse exploitable.
- Préparation d’une MLA franco-suisse pour gel et coopération bancaire (délai estimé 3-6 mois).

#### Erreurs fréquentes

- **Confondre les canaux** : Interpol n’est pas une autorité judiciaire ; Egmont n’est pas une police.
- **Sous-estimer les délais** : un dossier qui dépend de 5 coopérations parallèles prend des mois.
- **Oublier les coopérations sectorielles** : douanes (OMD), fiscalité (OCDE), sanctions (OFAC liaisons).

#### Limites

La qualité et la rapidité de coopération varient énormément. Certaines juridictions sont coopératives (Suisse, UK, Allemagne, Pays-Bas) ; d’autres beaucoup moins (Liban, certains pays en conflit, juridictions opaques).

#### Points clés à retenir

- Egmont (CRF mondial), FIU.NET (CRF UE), Europol (police UE), Interpol (police mondiale), Eurojust + EPPO (judiciaire UE).
- Choix du canal selon objectif (renseignement / police / judiciaire / asset recovery).
- Délais réalistes à intégrer dans la planification.

-----

### Chapitre 66 — Gel, saisie, confiscation et asset recovery

#### Objectif

Comprendre les **étapes du recouvrement d’avoirs** : gel administratif, saisie pénale, confiscation, restitution.

#### Le concept

L’**asset recovery** est l’ensemble des procédures permettant de retirer aux criminels les produits de leurs infractions. Cycle :

1. **Identification** : asset tracing (chapitre 59).
1. **Gel** (mesure rapide, conservatoire, parfois administrative).
1. **Saisie** (mesure judiciaire, retient juridiquement l’actif).
1. **Confiscation** (transfert définitif à l’État après condamnation).
1. **Restitution / partage** : aux victimes, à l’État, ou partage international.

#### Cadre français

**Gel administratif** :

- **Gel TRACFIN** (article L.561-25 CMF) : opposition à l’exécution d’une opération pour 5 jours ouvrés (10 jours avec décision motivée), renouvelable.
- **Gel des avoirs sanctions** : par décret ou arrêté ministériel (sanctions UE, ONU, OFAC en partie).

**Saisie pénale** :

- **Article 706-141 et suivants du CPP** : saisie de tous biens, en valeur ou en nature.
- Conduite par le juge d’instruction ou le procureur sous autorité juridictionnelle.

**Confiscation** :

- Après condamnation, transfert à l’État (article 131-21 du Code pénal).
- **Confiscation élargie** : possibilité de confisquer les avoirs d’origine inconnue d’une personne condamnée pour certaines infractions, sans avoir à prouver le lien individuel.

**AGRASC** (Agence de Gestion et de Recouvrement des Avoirs Saisis et Confisqués) : gère les biens saisis pendant la procédure, organise leur vente, gère les flux financiers de l’AGRASC.

#### Coopération internationale

- **Saisie pénale internationale** : via MLA, EPPO, Eurojust.
- **Reconnaissance mutuelle UE** : décisions de saisie et de confiscation reconnues entre États membres (règlements 2018/1805).
- **Conventions** : OCDE, Mérida, Strasbourg / Varsovie organisent les coopérations en matière d’asset recovery.

#### Méthode — chaîne de l’asset recovery

1. **Identifier** : asset tracing rigoureux (chapitre 59).
1. **Documenter** : fiches actifs (chapitre 30) avec juridiction, valeur, support juridique.
1. **Prioriser** : actifs les plus saisissables d’abord (France, UE, pays coopératifs).
1. **Geler rapidement** : actions immédiates pour stopper la dissipation.
1. **Lancer les coopérations** : MLA, Egmont, Eurojust, EPPO selon contexte.
1. **Suivre dans le temps** : asset recovery est un effort de plusieurs années.

#### Mini-walkthrough — cas RIVIÈRE (cf. chapitre 59)

Sur les ~10,4 M€ identifiés :

- Gel français immédiat (~3,8 M€ immobilier + ~280 K€ comptes + 850 K€ assurance-vie = ~5 M€).
- Coopération MLA Suisse pour gel compte (~3,2 M€) : délai 3-6 mois.
- Coopération MLA Émirats : délai 6-18 mois, succès incertain.
- Yacht Malte : coopération MLA + reconnaissance mutuelle UE.

Estimation de recouvrement à 24 mois : ordre de grandeur de quelques millions d’euros (fourchette pédagogique, dépendant de la coopération suisse, émiratie et maltaise).

#### Erreurs fréquentes

- **Sous-estimer l’urgence** : la dissipation est rapide, l’asset recovery est lent. La vitesse de gel initial est critique.
- **Ne pas prioriser** : disperser ses efforts sur tous les actifs simultanément retarde tout.
- **Ignorer les frais et la dépréciation** : un yacht confisqué peut perdre 50 % de sa valeur entre saisie et vente.

#### Limites

L’asset recovery n’est jamais total. Les criminels les plus expérimentés ont des stratégies de protection (multi-juridictionnel, prête-noms, juridictions non coopératives). Un recouvrement **partiel** d’une fraction significative du préjudice est un résultat satisfaisant en pratique. Les pourcentages cités dans le cours sont **pédagogiques** ; la performance réelle dépend fortement du dossier.

#### Points clés à retenir

- Cycle : identification → gel → saisie → confiscation → restitution.
- France : AGRASC est l’acteur central.
- UE : reconnaissance mutuelle accélère les procédures.
- Coopération internationale = lente, à anticiper.
- Recouvrement partiel est la norme.

-----

### Chapitre 67 — Cadre français : TRACFIN, ACPR, AMF, PNF, AGRASC

#### Objectif

Connaître l’**architecture institutionnelle française** en matière de LCB-FT et de criminalité économique, pour savoir qui fait quoi et avec qui interagir.

#### Acteurs centraux

**TRACFIN** (Traitement du Renseignement et Action contre les Circuits Financiers clandestins) : la **CRF française**. Service à compétence nationale du ministère de l’Économie. Reçoit les DS des assujettis, produit du renseignement, transmet au parquet et aux services. Membre fondateur d’Egmont. ~250 agents.

**ACPR** (Autorité de Contrôle Prudentiel et de Résolution) : autorité de supervision des banques, assurances, EME, PSP en France. Adossée à la Banque de France. Pouvoir de sanction, contrôle des dispositifs LCB-FT.

**AMF** (Autorité des Marchés Financiers) : autorité de supervision des marchés financiers et — historiquement — des **PSAN** (Prestataires de Services sur Actifs Numériques, régime issu de la loi PACTE de 2019). Pouvoir de sanction. **Évolution majeure** : le règlement européen **MiCA** est entré en application le **30 décembre 2024** pour les nouveaux acteurs (désormais appelés **CASP** — Crypto-Asset Service Providers). Pour les acteurs déjà enregistrés ou agréés PSAN, une **période transitoire** est prévue jusqu’au **1er juillet 2026** pour basculer sous le régime MiCA. À terme, MiCA remplace le régime PSAN national pour la supervision européenne harmonisée des crypto-actifs.

**Direction Générale du Trésor (DG Trésor)** — service du ministère de l’Économie. Au sein de la DG Trésor, le **pôle sanctions financières internationales** publie et tient à jour le **registre national des gels** et coordonne la mise en œuvre des sanctions financières internationales en France. À distinguer de la **Banque de France** (banque centrale, distincte) et de l’**ACPR** (qui est adossée à la Banque de France mais qui supervise les acteurs financiers, pas les sanctions).

**PNF** (Parquet National Financier) : parquet spécialisé, créé en 2013. Compétence nationale pour les délits financiers complexes : grande corruption, fraude fiscale grave et complexe, manquements aux obligations de transparence des marchés.

**JUNALCO** (Juridiction Nationale de Lutte contre la Criminalité Organisée) : parquet et juge d’instruction pour la criminalité organisée et la cybercriminalité.

**JIRS** (Juridiction Interrégionale Spécialisée) : 8 JIRS en France, traitent la criminalité économique et financière complexe au niveau interrégional.

**OCLCIFF** (Office Central de Lutte contre la Corruption et les Infractions Financières et Fiscales) : office de police judiciaire spécialisé, sous la direction de la PJ.

**Service d’Enquêtes Judiciaires des Finances (SEJF)** : service du ministère de l’Économie, double tutelle (douanes + fiscalité), pour les infractions financières et fiscales graves.

**AGRASC** : déjà détaillée (chapitre 66).

**DGFiP — DNEF** (Direction Nationale des Enquêtes Fiscales) : enquêtes fiscales lourdes.

**DGDDI** (Direction Générale des Douanes et Droits Indirects) : enquêtes douanières, contrôles transfrontaliers.

**Tribunal Judiciaire de Paris — pôle financier** : juridiction de jugement des affaires complexes.

#### Coordination

- **Article 40 CPP** : tout agent public ayant connaissance d’un crime ou d’un délit doit informer le procureur. Vecteur d’entrée dans le judiciaire.
- **DS TRACFIN** : du périmètre des assujettis vers la CRF.
- **CSF** (Conseil de Stratégie Financière) : coordination interministérielle.
- **Réunions inter-services** : coordination opérationnelle.

#### Méthode — interactions selon profil

- **Cabinet conseil** : alerte client, accompagne déclaration de soupçon (via assujetti), conseille rupture commerciale.
- **Banque assujettie** : DS TRACFIN, KYC, monitoring, droit d’opposition.
- **CRF (TRACFIN)** : produit renseignement, transmet articles 40 CPP au parquet, dissémine internationalement.
- **Magistrat** : ouvre enquête / instruction, mandate police judiciaire (OCLCIFF, SEJF, JIRS), saisit AGRASC, dialogue avec EPPO si applicable.
- **Police judiciaire** : enquête, réquisitions, auditions, perquisitions.

#### Points clés à retenir

- TRACFIN = CRF française, point d’entrée renseignement.
- PNF = parquet financier spécialisé.
- ACPR + AMF = supervision financière.
- AGRASC = gestion des avoirs saisis.
- OCLCIFF + SEJF = police judiciaire spécialisée.

-----

### Chapitre 68 — Éthique, RGPD, secret bancaire et limites

#### Objectif

Cadrer la **dimension éthique et juridique** du FININT : respect du droit, du RGPD, du secret bancaire, de la présomption d’innocence, et de la protection des personnes.

#### Le concept

Le FININT manipule des **données sensibles** : identité, finances, vie privée, réputation, parfois liberté individuelle des personnes concernées. Toute pratique doit s’inscrire dans un cadre :

**Cadre juridique** :

- **Droit national** : code monétaire et financier (LCB-FT), code pénal, code de procédure pénale.
- **RGPD** : traitement de données personnelles avec base légale, finalité, proportionnalité, durée de conservation, droits des personnes.
- **Secret bancaire** : opposable aux particuliers, levable pour les autorités sous procédure.
- **Secret professionnel** : avocats, notaires, médecins, etc.
- **Droits fondamentaux** : Charte des droits fondamentaux UE, CESDH (CEDH).

**Cadre déontologique** :

- **Présomption d’innocence** : un mis en cause n’est pas un coupable.
- **Proportionnalité** : la collecte et l’usage doivent être proportionnés à la finalité.
- **Honnêteté épistémique** : ne pas écrire ce qu’on ne sait pas, calibrer les conclusions.
- **Respect de l’humanité** : derrière chaque entité, des personnes — y compris des innocents.

#### Différences selon cadres

**En CRF (TRACFIN ou équivalent)** : cadre légal large (loi LCB-FT), accès à des sources fermées (FICOBA, EAR/CRS, droits de communication), traitement à grande échelle autorisé sur base légale.

**En cabinet privé (conseil, due diligence, audit forensique)** : cadre strict, RGPD plein, base légale = intérêt légitime ou contrat, pas d’accès aux sources fermées sans procédure judiciaire.

**En journalisme d’investigation** : cadre spécifique (liberté de la presse), recoupements multiples, vérification stricte, accès parfois à des sources confidentielles (lanceurs d’alerte) avec protections juridiques.

**En enquête judiciaire** : cadre du CPP, sources fermées via réquisitions, contrôle juridictionnel.

#### Les limites à respecter

- **Pas de phishing OSINT** : créer un faux profil pour entrer en contact avec une cible est une **manœuvre frauduleuse** prohibée.
- **Pas de violation du secret bancaire** : accéder illégalement à des données bancaires est une infraction.
- **Pas de dénonciation calomnieuse** : diffuser des accusations non fondées peut engager la responsabilité civile et pénale.
- **Respect du RGPD** : conservation limitée, finalité respectée, droits des personnes (information, accès, opposition selon contexte).
- **Pas de diabolisation** des juridictions ou des communautés : analyse rigoureuse, pas de stigmatisation.

#### Lien avec le fil rouge

Tout le travail de Nassim sur le dossier Haddad respecte ces cadres : sources légales, calibration des conclusions, distinction faits / hypothèses, présomption d’innocence pour les personnes mises en cause, conservation et transmission selon cadre LCB-FT. Sans cette discipline, le travail serait juridiquement attaquable et déontologiquement contestable.

#### Points clés à retenir

- Le FININT est encadré : juridique + déontologique.
- RGPD applicable selon le cadre (CRF / cabinet / journalisme / judiciaire).
- Présomption d’innocence + proportionnalité + honnêteté épistémique.
- Pas de phishing OSINT, pas de violation du secret bancaire, pas de dénonciation calomnieuse.

-----

### Chapitre 69 — Construire une capacité FININT durable

#### Objectif

Au-delà des techniques individuelles, comment **construire et maintenir une capacité FININT durable** dans une organisation (CRF, banque, cabinet, service d’enquête).

#### Les dimensions de la capacité

**Humaine** :

- Recrutement de profils mixtes (finance, droit, OSINT, analyse de données, langues).
- Formation continue : LCB-FT, typologies, outils, juridictions, évolutions réglementaires.
- Certifications : CAMS (Certified Anti-Money Laundering Specialist), CFE (Certified Fraud Examiner), CFCS (Certified Financial Crime Specialist).
- Réseau professionnel : associations (ACAMS, ACFE), communautés.

**Méthodologique** :

- Procédures documentées (workflow, fiches, calibration WEP).
- Templates et modèles réutilisables.
- Revues régulières (lessons learned).
- Veille : GAFI, AMLA, évolutions sectorielles.

**Technologique** :

- Outils OSINT (gratuits + professionnels selon budget).
- Plateformes d’analyse (Maltego, Linkurious, etc.).
- DMS (Document Management System) avec chain of custody.
- Solutions de visualisation et reporting.

**Organisationnelle** :

- Coopérations établies (CRF, services, partenaires).
- Canaux de communication sécurisés.
- Politiques internes (déontologie, confidentialité, protection des données).
- Reporting interne (qualité des livrables, suivi des dossiers).

**Évolutive** :

- Capacité à intégrer les nouvelles typologies (crypto, cybercrime financier, sanctions modernes).
- Capacité à coopérer avec disciplines voisines (CTI, OSINT Crypto, audit forensique, droit).

#### Indicateurs de maturité

Une équipe FININT mature se reconnaît à :

- Documents standards utilisés systématiquement.
- Calibration WEP appliquée sans rappel.
- Délais respectés et planning intégré aux coopérations.
- Capacité d’auto-critique (revues post-dossier).
- Anticipation des évolutions (formation continue, veille).
- Coopérations multiples et fluides.

#### Erreurs fréquentes

- **Dépendance excessive aux outils** : un bon analyste fait beaucoup avec peu ; un outil ne fait pas l’analyse.
- **Sous-investissement en formation** : les typologies évoluent vite, la veille est essentielle.
- **Isolement** : sans réseau professionnel et coopérations, on s’épuise vite.
- **Rotation excessive** : la maturité FININT exige plusieurs années d’expérience.

#### Lien avec le fil rouge

Nassim, après 7 ans dans la CRF fictive et avec une certification CAMS + formation continue, illustre une capacité individuelle mature. La CRF elle-même illustre une capacité organisationnelle mature : workflows, coopérations, outils, équipes spécialisées par typologies.

#### Conclusion du cours

Le FININT, en 2025-2026, est une discipline en pleine évolution :

- Cadres réglementaires se renforcent (AMLA, AML Package).
- Typologies évoluent (sanctions massives post-2022, cybercrime financier).
- Coopérations s’intensifient (EPPO, AMLA).
- Outils progressent (IA pour le screening, graphes plus puissants).

L’analyste FININT compétent en 2025-2026 :

- Connaît la matière et les évolutions.
- Maîtrise les outils et les méthodes.
- Calibre rigoureusement et écrit clairement.
- Coopère avec disciplines voisines (OSINT général, OSINT Crypto, CTI, audit, droit).
- Respecte le cadre éthique et juridique.
- Apprend en continu.

Le chapitre 70 qui suit donne, en complément, une **mise à niveau des évolutions réglementaires majeures 2024-2026** que tout analyste doit avoir en tête. Les annexes fournissent ensuite les **outils opérationnels** prêts à utiliser dans la pratique : glossaire, fiches type, matrices, modèles de note, registres par pays, outils par usage, cadres d’accès aux sources, bibliographie de sources primaires, et erreurs à éviter.

#### Points clés à retenir

- Capacité FININT : humaine + méthodologique + technologique + organisationnelle + évolutive.
- Certifications (CAMS, CFE, CFCS) + formation continue + veille.
- L’analyste mûr fait beaucoup avec peu, calibre rigoureusement, coopère naturellement.
- La discipline évolue : restez en mouvement.

-----

### Chapitre 70 — Évolutions réglementaires 2024-2026 : mise à niveau

#### Objectif du chapitre

Synthétiser les **principales évolutions réglementaires** qui structurent ou structureront le cadre du FININT et de la LCB-FT sur la période 2024-2026 et au-delà. Ce chapitre est conçu comme un **aide-mémoire évolutif** : il sera périmé partiellement à mesure que les textes s’appliquent ; l’analyste consulte les sources primaires (annexe N) pour la situation à date.

#### 1. Le paquet AML européen et l’AMLA

L’**AML Package** européen a été publié au Journal officiel de l’UE le **19 juin 2024**. Il comprend principalement :

- **Le règlement AMLR** (Anti-Money Laundering Regulation) — règles harmonisées directement applicables.
- **La 6e directive AML** (AMLD6) — règles transposées par chaque État membre, encadrant notamment les supervisions nationales et les CRF.
- **Le règlement AMLA** — créant l’**Autorité européenne de lutte contre le blanchiment de capitaux et le financement du terrorisme** (AMLA), basée à Francfort.

**Frise chronologique simplifiée** :

- **19 juin 2024** : publication du paquet AML au JOUE.
- **26 juin 2024** : entrée en vigueur juridique de l’AMLA.
- **2025-2027** : montée en puissance institutionnelle de l’AMLA (recrutement, méthodes, sélection des entités).
- **À partir de 2028** : début de la **supervision directe** par l’AMLA des entités financières les plus risquées et complexes de l’UE (au nombre d’environ 40 selon les estimations en cours).
- **Parallèlement, jusqu’en 2027** : application progressive de l’AMLR et transposition d’AMLD6 dans les législations nationales.

**Conséquences opérationnelles pour l’analyste** :

- Harmonisation accrue des règles LCB-FT en UE.
- Standards de KYC, monitoring, déclaration de soupçon, vigilance renforcée plus convergents.
- Émergence de l’AMLA comme régulateur de référence pour les grandes institutions transfrontalières.
- Interconnexion européenne progressive des registres UBO (sous conditions strictes post-CJUE).
- Renforcement des coopérations entre CRF via FIU.NET et coordination AMLA.

#### 2. Verification of Payee (VOP) et règlement Instant Payments

Le **règlement européen sur les paiements instantanés** introduit l’obligation, pour les PSP de proposer un **service de vérification du nom du bénéficiaire** (Verification of Payee — VOP) avant l’exécution d’un virement.

**Calendrier** :

- **PSP de la zone euro** : obligation opérationnelle à compter d’**octobre 2025**.
- **PSP hors zone euro** dans l’UE : obligation à compter de **juillet 2027**.

**Conséquences pour la fraude au virement (BEC, fraude au changement d’IBAN)** :

- Le VOP devient un **garde-fou systémique** : discrépance entre le nom du bénéficiaire affiché et le titulaire réel du compte IBAN renvoyée à l’émetteur avant exécution.
- Les fraudes type BEC voient leur efficacité réduite — sans la disparaître (les fraudeurs adaptent, créent des comptes au nom du fournisseur, exploitent les transitions, manipulent les utilisateurs).
- L’analyste FININT doit suivre la pratique réelle des PSP au moment de l’enquête.

#### 3. Corporate Transparency Act (CTA) américain — trajectoire 2024-2025

Le **Corporate Transparency Act** de 2021 a connu une trajectoire **particulièrement instable** :

- 2024 : mise en œuvre démarrée par FinCEN. Obligation aux LLC et corporations US de déclarer leurs UBO à FinCEN.
- Fin 2024 - début 2025 : multiples décisions judiciaires contradictoires (injonctions, suspensions, levées).
- **Mars 2025 — interim final rule FinCEN** : les sociétés domestiques américaines (« domestic reporting companies ») sont **exemptées** de l’obligation de déclaration BOI à FinCEN. L’obligation **subsiste pour certaines entités étrangères enregistrées pour faire des affaires aux États-Unis**.
- Situation susceptible d’évolutions futures (contentieux, textes, administration).

**Conséquences pour l’analyste** :

- Les LLC Delaware, Wyoming, Nevada redeviennent quasi-totalement **opaques** sur l’UBO réel pour les analystes externes.
- L’accès à l’UBO de ces entités US passe presque exclusivement par les **enquêtes judiciaires** (réquisitions, coopérations DOJ).
- Vérifier l’état du droit FinCEN au moment de toute conclusion.

#### 4. MiCA et basculement PSAN → CASP

Le règlement européen **MiCA (Markets in Crypto-Assets)** structure le marché européen des crypto-actifs.

**Calendrier** :

- **30 décembre 2024** : application aux nouveaux acteurs (désormais appelés **CASP** — Crypto-Asset Service Providers).
- **Jusqu’au 1er juillet 2026** : **période transitoire** pour les acteurs déjà enregistrés ou agréés PSAN sous le régime français PACTE (2019). Ils peuvent continuer leur activité dans l’attente de leur basculement sous MiCA.

**Conséquences** :

- Harmonisation européenne du régime des prestataires de services crypto.
- Conditions d’agrément renforcées (capital, gouvernance, KYC, custody, marchés).
- Pour l’analyste FININT : le périmètre des PSAN/CASP susceptibles d’opérer en France et en UE devient plus clair et plus encadré ; les coopérations avec ces acteurs se professionnalisent.
- À combiner avec le **Travel Rule** (TFR — Transfer of Funds Regulation, 2023, applicable 30/12/2024 en synchronie avec MiCA) qui impose la traçabilité des informations émetteur/bénéficiaire pour les transferts de crypto-actifs au-delà de seuils.

#### 5. UBO post-CJUE : un paysage fragmenté

L’arrêt de la **CJUE du 22 novembre 2022** (affaires C-37/20 et C-601/20) a invalidé l’accès public généralisé aux informations UBO, au motif d’atteinte aux droits fondamentaux à la vie privée et à la protection des données.

**État du paysage 2025-2026** :

- **France (RBE)**, **Allemagne (Transparenzregister)**, **Luxembourg (RBE)**, **Pays-Bas (UBO-register)**, **Chypre**, etc. : accès public restreint. Accès maintenu pour autorités, assujettis LCB-FT, presse d’investigation sous conditions, professionnels avec intérêt légitime.
- **UK (PSC)** : non concerné par l’arrêt CJUE (hors UE depuis Brexit), reste **public et gratuit**.
- Variabilité d’application selon les États membres et les catégories d’acteurs.

**Conséquences** :

- L’analyste OSINT « grand public » a un accès **plus restreint** aux UBO européens qu’avant 2022.
- Les **journalistes d’investigation** peuvent dans certains pays bénéficier d’un accès au titre de l’intérêt légitime, sous conditions.
- L’**AMLA et l’interconnexion européenne** des registres devraient progressivement clarifier les modalités d’accès pour les catégories légitimes.

#### 6. Sanctions : intensification post-2022

L’invasion russe de l’Ukraine (février 2022) a entraîné une **intensification massive et continue** des sanctions UE, US (OFAC), UK (OFSI), Suisse, Canada, Australie, Japon contre la Russie, la Biélorussie et des entités liées. Conséquences :

- Multiplication des paquets de sanctions UE (12+ depuis 2022).
- Renforcement OFAC, élargissement progressif.
- Accent sur le **contournement** via pays tiers (Émirats, Turquie, Géorgie, Asie centrale, Caucase).
- Mobilisation forte des CRF, douanes, banques sur ces flux.
- Création de cellules spécialisées dans plusieurs États (REPO Task Force aux US, gel d’avoirs UE).

L’analyste FININT a, depuis 2022, un **volet sanctions** quasi-systématique à intégrer dans les dossiers internationaux.

#### 7. Veille à organiser

**Sources primaires à consulter régulièrement** (cf. annexe N — Bibliographie) :

- **GAFI / FATF** : recommandations, méthodologie, listes (noire, grise), rapports thématiques, mises à jour des typologies.
- **Egmont Group** : informations sur les coopérations, livrables annuels.
- **TRACFIN** : rapport annuel, tendances et analyses, points de vigilance, lignes directrices.
- **ACPR, AMF** : recommandations, sanctions publiques, lignes directrices LCB-FT.
- **DG Trésor — pôle sanctions financières internationales** : registre national des gels, communiqués sanctions.
- **FinCEN** : avis, alertes, mises à jour CTA, SAR statistics.
- **OFAC** : listes SDN, faqs, sanctions secondaires.
- **OFSI** : listes consolidées UK.
- **Commission européenne** : AML Package, MiCA, sanctions UE.
- **AMLA** (au fur et à mesure de sa montée en puissance) : méthodes de supervision, listes des entités sélectionnées.
- **Europol, Eurojust, EPPO** : rapports d’activité, tendances criminalité.
- **ICIJ, OCCRP** : leaks et investigations récentes.
- **Veille presse spécialisée** : Financial Times, Reuters, Bloomberg, Le Monde, Mediapart, OCCRP daily.

#### Lien avec le fil rouge

> **CLEARFLOW — Pertinence des évolutions**
> 
> Pour le dossier Haddad, plusieurs évolutions ont un impact direct : (1) l’AMLA et l’interconnexion progressive des registres UBO pourraient, à terme, accélérer les recoupements multi-juridictionnels qui ont coûté à Nassim plusieurs semaines de coopérations bilatérales ; (2) la trajectoire instable du CTA US justifie d’avoir traité la LLC Delaware comme une zone d’opacité ; (3) l’environnement sanctions post-2022 explique la vigilance accrue sur les flux Turquie ; (4) le VOP réduira (mais n’éliminera pas) la vulnérabilité aux BEC type ALPHA INDUSTRIE.

#### Points clés à retenir

- Paquet AML UE 2024 + AMLA opérationnelle à partir de 2028 (supervision directe).
- VOP obligatoire : oct. 2025 (zone euro), juill. 2027 (hors zone euro).
- CTA US : exemption des sociétés domestiques depuis mars 2025.
- MiCA en application 30/12/2024 ; transition PSAN→CASP jusqu’au 01/07/2026.
- UBO post-CJUE : paysage fragmenté, vérifier au cas par cas.
- Sanctions post-2022 : volet systématique des dossiers internationaux.
- Veille indispensable sur sources primaires.

-----

## ANNEXES

*Quatorze annexes fournissant les outils opérationnels du cours : glossaire, lecture des messages SWIFT, modèles de fiches, matrices red flags et de qualification, registres par pays, outils par usage, modèle de note FININT, erreurs fréquentes et mini-cas d’entraînement, cadres d’accès aux sources, bibliographie de sources primaires.*

-----

### Annexe A — Glossaire opérationnel FININT

*Sélection des termes les plus utilisés en FININT, version opérationnelle (définitions courtes, orientées pratique).*

**ABS** — Abus de biens sociaux. Délit français de détournement des biens d’une société par son dirigeant.

**ACAMS** — Association of Certified Anti-Money Laundering Specialists. Référence internationale du LCB-FT.

**ACPR** — Autorité de Contrôle Prudentiel et de Résolution. Superviseur français des banques et assurances.

**Adverse media** — Publications négatives publiques sur une personne ou entité (presse, ONG, rapports d’enquête).

**AGRASC** — Agence de Gestion et de Recouvrement des Avoirs Saisis et Confisqués (France).

**Aleph** — Plateforme d’investigation de l’OCCRP et de l’ICIJ, agrégeant leaks et bases publiques.

**AML / LCB-FT** — Anti-Money Laundering / Lutte Contre le Blanchiment et le Financement du Terrorisme.

**AMLA** — Anti-Money Laundering Authority (UE), nouvelle autorité européenne de supervision LCB-FT.

**AMF** — Autorité des Marchés Financiers (France).

**Article 40 CPP** — Obligation de tout agent public de signaler crimes et délits au procureur.

**Asset recovery** — Recouvrement d’avoirs criminels (identification → gel → saisie → confiscation → restitution).

**Asset tracing** — Identification des actifs d’une personne ou entité.

**Beneficial Owner / UBO** — Bénéficiaire effectif. Personne physique contrôlant ultimement une entité.

**BEC** — Business Email Compromise. Fraude au virement par compromission ou simulation d’email.

**BIC** — Bank Identifier Code, identifiant SWIFT d’une banque.

**BODACC** — Bulletin Officiel des Annonces Civiles et Commerciales (France).

**BVI** — British Virgin Islands. Juridiction offshore notable.

**CAC** — Commissaire aux comptes.

**CAMS** — Certified Anti-Money Laundering Specialist (certification ACAMS).

**CARIN** — Camden Asset Recovery Inter-agency Network.

**Cashout** — Conversion finale de fonds illicites en valeur utilisable.

**CFE** — Certified Fraud Examiner (certification ACFE).

**CFCS** — Certified Financial Crime Specialist (certification ACFCS).

**Chain of custody** — Chaîne de preuve. Traçabilité des éléments d’enquête.

**Cluster** — Groupe d’entités liées par capital, dirigeants, adresse, ou fonctionnalité.

**Companies House** — Registre du commerce du Royaume-Uni.

**Conventions de Mérida / OCDE / Strasbourg** — Conventions internationales sur la corruption et le blanchiment.

**CPP** — Code de Procédure Pénale (France).

**CRF / FIU** — Cellule de Renseignement Financier / Financial Intelligence Unit.

**CRS** — Common Reporting Standard. Échange automatique d’informations fiscales OCDE.

**CTI** — Cyber Threat Intelligence.

**Dark web / Deep web** — Internet non indexé (deep) ou accessible via outils spécifiques (dark : Tor, I2P).

**DECP** — Données Essentielles de la Commande Publique (France, data.gouv.fr).

**DGDDI** — Direction Générale des Douanes et Droits Indirects (France).

**DGFiP** — Direction Générale des Finances Publiques (France).

**DG Trésor** — Direction Générale du Trésor (France). Service du ministère de l’Économie. Au sein de la DG Trésor, le pôle sanctions financières internationales tient le registre national des gels et coordonne les sanctions financières internationales. À ne pas confondre avec la Banque de France (banque centrale).

**Diligence (due) approfondie / Enhanced Due Diligence** — KYC renforcé pour clients à risque.

**DMS** — Document Management System.

**DS** — Déclaration de Soupçon (vers la CRF).

**Dual-use** — Biens à double usage civil et militaire, soumis à régulation export.

**DVF** — Demandes de Valeurs Foncières (France, data.gouv.fr).

**EAR** — Échange Automatique de Renseignements (fiscal).

**Egmont Group** — Réseau mondial des CRF.

**EME** — Établissement de Monnaie Électronique.

**EPPO** — European Public Prosecutor’s Office. Parquet européen.

**Eurojust** — Agence européenne de coopération judiciaire.

**Europol** — Agence européenne de police.

**Évasion fiscale** — Soustraction illégale à l’impôt. À distinguer de l’**optimisation fiscale** (légale).

**FIBA** — Florida International Bankers Association (certification AMLCA).

**FICOBA** — Fichier des Comptes Bancaires (France, accessible aux autorités).

**FICOVIE** — Fichier des Contrats d’Assurance-Vie (France).

**FININT** — Financial Intelligence. Renseignement financier.

**FIU.NET** — Réseau européen des CRF.

**Forensic accounting** — Comptabilité forensique.

**Fronting** — Utilisation d’un tiers (prête-nom, société écran) pour dissimuler le véritable acteur.

**GAFI / FATF** — Groupe d’Action Financière / Financial Action Task Force.

**GLEIF** — Global Legal Entity Identifier Foundation (LEI).

**HATVP** — Haute Autorité pour la Transparence de la Vie Publique (France).

**IBAN** — International Bank Account Number.

**IBC** — International Business Company (juridictions offshore).

**ICIJ** — International Consortium of Investigative Journalists.

**Infogreffe** — Service du registre du commerce français.

**Intégration** — 3e phase du blanchiment (réinjection dans l’économie légale).

**INPI** — Institut National de la Propriété Industrielle. Données d’entreprises françaises.

**Interpol** — Organisation internationale de police criminelle.

**JIRS** — Juridiction Interrégionale Spécialisée (France).

**JUNALCO** — Juridiction Nationale de Lutte contre la Criminalité Organisée.

**KYC / KYB** — Know Your Customer / Know Your Business.

**Layering** — 2e phase du blanchiment (empilement, brouillage).

**LCB-FT** — Lutte Contre le Blanchiment et le Financement du Terrorisme.

**LEI** — Legal Entity Identifier. Code mondial d’identification d’entité.

**LLC** — Limited Liability Company (US et autres).

**MLA** — Mutual Legal Assistance. Entraide judiciaire bilatérale.

**MROS** — Money Laundering Reporting Office (CRF suisse).

**MT103 / MT202 / MT940** — Messages SWIFT (paiement client / interbancaire / relevé).

**Nominee** — Prête-nom officiel (common law).

**OCCRP** — Organized Crime and Corruption Reporting Project.

**OCDE** — Organisation de Coopération et de Développement Économique.

**OFAC** — Office of Foreign Assets Control (US, sanctions).

**OFSI** — Office of Financial Sanctions Implementation (UK).

**OpenCorporates** — Agrégateur mondial de registres d’entreprises.

**OpenSanctions** — Base publique agrégée de sanctions et PEP.

**OSINT** — Open Source Intelligence. Renseignement de sources ouvertes.

**Pandora Papers / Panama Papers / Paradise Papers** — Leaks majeurs ICIJ sur structures offshore.

**Pappers** — Service d’information sur entreprises françaises (gratuit / freemium).

**PEP** — Politically Exposed Person.

**Placement** — 1re phase du blanchiment (introduction dans le système).

**PNF** — Parquet National Financier (France).

**Prête-nom** — Personne apparaissant officiellement sans exercer le contrôle réel.

**PSAN / CASP** — Prestataire de Services sur Actifs Numériques (France, régime PACTE 2019) / Crypto-Asset Service Provider (terminologie MiCA). MiCA est entré en application le 30/12/2024 pour les nouveaux acteurs ; période transitoire jusqu’au 01/07/2026 pour les acteurs déjà enregistrés.

**PSC** — People with Significant Control (UK, équivalent UBO).

**PSP** — Prestataire de Services de Paiement.

**RBE** — Registre des Bénéficiaires Effectifs (France).

**Red flag** — Signal d’alerte (anomalie, indice à vérifier).

**RGPD / GDPR** — Règlement Général sur la Protection des Données.

**Sanctions secondaires** — Sanctions OFAC s’appliquant à des opérateurs non-US.

**Sayari** — Plateforme professionnelle OSINT financier.

**SCT / SCT Inst** — SEPA Credit Transfer / SEPA Credit Transfer Instant.

**SEJF** — Service d’Enquêtes Judiciaires des Finances (France).

**Shell company** — Société écran.

**SIREN / SIRET** — Identifiants d’entreprise et d’établissement (France).

**Smurfing** — Fractionnement de dépôts sous les seuils déclaratifs.

**Société écran** — Entité juridique sans activité économique réelle.

**SOPARFI** — Société de Participation Financière (Luxembourg).

**Stablecoin** — Crypto-actif adossé à une valeur stable (USDT, USDC, etc.).

**SWIFT** — Society for Worldwide Interbank Financial Telecommunication.

**TBML** — Trade-Based Money Laundering.

**TLP** — Traffic Light Protocol. Classification de diffusion (WHITE / GREEN / AMBER / RED).

**TRACFIN** — Traitement du Renseignement et Action contre les Circuits Financiers clandestins. CRF française.

**Trust** — Relation juridique (common law) entre settlor, trustee, bénéficiaires.

**TVA carrousel** — Fraude à la TVA intracommunautaire.

**UBO** — Ultimate Beneficial Owner. Bénéficiaire effectif ultime.

**VOP** — Verification of Payee. Vérification du nom du bénéficiaire SEPA. Déploiement progressif dans l’UE : obligatoire pour PSP zone euro à compter d’octobre 2025, et juillet 2027 pour PSP hors zone euro (règlement Instant Payments).

**WEP** — Words of Estimative Probability. Échelle de calibration de confiance.

**World-Check** — Base professionnelle Refinitiv pour PEP, sanctions, adverse media.

-----

### Annexe B — Lire un message SWIFT : MT103, MT202, MT940

*Lecture annotée des trois types de messages SWIFT les plus rencontrés en FININT.*

#### MT103 — Single Customer Credit Transfer (paiement client à client international)

Structure simplifiée :

```
{1: Basic header}
{2: Application header}
{4:
:20:REF1234567890         <- Référence unique du message
:23B:CRED                 <- Type de transaction
:32A:240315EUR12500,00    <- Date valeur + devise + montant
:50K:/FR7612345678901234567890123  <- Donneur d'ordre (IBAN + nom)
NEXUS TRADING SAS
12 RUE Y PARIS 9E
:52A:BNPAFRPP              <- Banque du donneur d'ordre (BIC)
:57A:CHASUS33              <- Banque correspondante intermédiaire (US ici)
:59:/CY01234567890123      <- Bénéficiaire (compte + nom)
NEXUS HOLDINGS LTD
NICOSIA CYPRUS
:70:TRADE PAYMENT INVOICE 0234  <- Libellé / référence
:71A:SHA                   <- Frais (SHA = partagés, OUR = donneur, BEN = bénéficiaire)
-}
{5: Trailer}
```

**Lecture FININT** :

- :20 référence unique du message.
- :32A donne **date + devise + montant** sur une seule ligne (format YYMMDD).
- :50 = donneur d’ordre. K = nom + adresse en clair. A = BIC.
- :52 = banque du donneur.
- :57 = banque correspondante (peut révéler un transit US si USD).
- :59 = bénéficiaire (IBAN + nom + adresse).
- :70 = libellé.
- :71 = qui paie les frais.

Signaux à surveiller : libellés vagues, banques correspondantes inattendues, donneur ou bénéficiaire dans juridictions à risque, références non vérifiables.

#### MT202 — General Financial Institution Transfer (transfert interbancaire)

Structure simplifiée :

```
:20:REF0987654321
:21:RELATED20240314
:32A:240315USD2500000,00
:52A:BSUICHGG            <- Banque émettrice
:57A:DEUTDEFF            <- Banque correspondante
:58A:CYNICY2N            <- Banque bénéficiaire
:72:/BNF/Pour client final NEXUS HOLDINGS
```

**Lecture FININT** :

- Transfert entre **banques** (pas entre clients).
- Volume typique : élevé.
- :72 peut contenir des informations sur le client final ; souvent succinctes.
- Utilisé par les banques pour leurs transferts ou pour le compte de clients de grande taille.

Le MT202 est plus opaque pour la traçabilité client. Combiné avec MT202COV (cover payment), il a été un canal historique du **stripping** (suppression de mentions de juridictions sanctionnées) — pratique sanctionnée massivement par OFAC (Standard Chartered, HSBC, BNP Paribas dans les années 2010).

#### MT940 — Customer Statement (relevé de compte)

Structure simplifiée :

```
:20:STATEMENT240315
:25:FR7612345678901234567890123      <- Compte concerné
:28C:00086/001                       <- Numéro de séquence
:60F:C240314EUR12345,67              <- Solde d'ouverture (C = créditeur)
:61:240315D12500,00NTRFREF...        <- Mouvement : date / D-C / montant / code type
:86:VIR EMIS NEXUS HOLDINGS LTD CY
:61:240315C85000,00NTRFREF...
:86:VIR REC ATLAS TECHNICAL TURKEY
:62F:C240315EUR84845,67              <- Solde de fermeture
```

**Lecture FININT** :

- Format standardisé des relevés interbancaires (transmission B2B).
- :60 et :62 = soldes d’ouverture et de fermeture.
- :61 = un mouvement (date, débit/crédit, montant, type de transaction).
- :86 = libellé associé.

Utile pour l’analyse de séries de mouvements. Les exports vers Excel ou pandas se font directement depuis MT940 (parsers disponibles).

-----

### Annexe C — Modèle de fiche personne

```
FICHE PERSONNE — [Nom Prénom]
Référence : [DOSSIER]/PER/[NUM] | Version : [vN.N] | Date : [JJ/MM/AAAA]
Classification : [TLP:CLEAR / GREEN / AMBER / RED]
Auteur : [Analyste] | Destinataires : [Liste]

────────────────────────────────────────────
1. IDENTIFICATION
────────────────────────────────────────────
- Nom complet : ...
- Date et lieu de naissance : ...
- Nationalité(s) : ...
- Adresse(s) connue(s) : ...
- Numéros d'identification (NIF, SS, passeport — si accessibles légalement) : ...
- Photo : [lien interne, hash]
- Niveau de confiance global identification : [WEP]

────────────────────────────────────────────
2. PROFIL
────────────────────────────────────────────
- Parcours professionnel : ...
- Formation : ...
- Langues : ...
- Fonctions publiques (passées / actuelles) : ...
- Statut PEP : [Oui / Non / PEP famille / PEP collaborateur]
- Affiliations significatives : ...

────────────────────────────────────────────
3. MANDATS ACTUELS DÉCLARÉS
────────────────────────────────────────────
| Entité | Rôle | Juridiction | Depuis | Niveau confiance |
| ...    | ...  | ...         | ...    | ...              |

────────────────────────────────────────────
4. MANDATS ANTÉRIEURS
────────────────────────────────────────────
[Historique]

────────────────────────────────────────────
5. UBO ET CONTRÔLE INDIRECT
────────────────────────────────────────────
| Entité | Type de contrôle | Niveau confiance |
| ...    | ...              | ...              |

────────────────────────────────────────────
6. PATRIMOINE IDENTIFIÉ
────────────────────────────────────────────
- Immobilier : ...
- Financier : ...
- Mobilier de valeur : ...
- Crypto (renvoi OSINT Crypto) : ...
- Train de vie observable : ...

────────────────────────────────────────────
7. RÉSEAU
────────────────────────────────────────────
- Famille proche : ...
- Collaborateurs : ...
- Associés : ...

────────────────────────────────────────────
8. CONTENTIEUX ET RÉPUTATION
────────────────────────────────────────────
- Procédures collectives, fiscales, pénales : ...
- Condamnations : ...
- Sanctions OFAC / UE / ONU / OFSI : ...
- Adverse media : ...

────────────────────────────────────────────
9. SANCTIONS / PEP / SCREENING
────────────────────────────────────────────
[Résultat de screening]

────────────────────────────────────────────
10. LIENS CRYPTO (RENVOI OSINT CRYPTO)
────────────────────────────────────────────
[Référence rapport on-chain partenaire]

────────────────────────────────────────────
11. HYPOTHÈSES CALIBRÉES
────────────────────────────────────────────
| Hypothèse | Niveau WEP | Justification |
| ...       | ...        | ...           |

────────────────────────────────────────────
12. LACUNES ET ACTIONS COMPLÉMENTAIRES
────────────────────────────────────────────
[Liste]

────────────────────────────────────────────
13. SOURCES
────────────────────────────────────────────
[Liste numérotée]
```

-----

### Annexe D — Modèle de fiche société

```
FICHE SOCIÉTÉ — [Dénomination]
Référence : [DOSSIER]/SOC/[NUM] | Version : [vN.N] | Date : [JJ/MM/AAAA]
Classification : [TLP]
Auteur : [Analyste] | Destinataires : [Liste]

────────────────────────────────────────────
1. IDENTIFICATION
────────────────────────────────────────────
- Dénomination exacte : ...
- Identifiant officiel (SIREN, Company Number, LEI) : ...
- Forme juridique : ...
- Juridiction : ...
- Capital : ...
- Date de création : ...

────────────────────────────────────────────
2. ADRESSE(S)
────────────────────────────────────────────
- Siège : ...
- Établissements secondaires : ...
- Adresse réelle (si différente) : ...
- Cohabitation avec autres entités à la même adresse : ...

────────────────────────────────────────────
3. ACTIVITÉ DÉCLARÉE
────────────────────────────────────────────
- Code NAF / SIC : ...
- Libellé : ...
- Activité opérationnelle visible : ...

────────────────────────────────────────────
4. GOUVERNANCE
────────────────────────────────────────────
- Dirigeants actuels : ...
- Historique des dirigeants : ...
- Profilage des dirigeants : ...

────────────────────────────────────────────
5. ACTIONNARIAT / CAPITAL
────────────────────────────────────────────
- Associés : ...
- Pourcentages : ...
- Classes d'actions : ...

────────────────────────────────────────────
6. UBO
────────────────────────────────────────────
- Déclaré au registre UBO : ...
- Identifié par analyse : ...
- Niveau de confiance : [WEP]

────────────────────────────────────────────
7. SUBSTANCE ÉCONOMIQUE
────────────────────────────────────────────
- Personnel : ...
- Locaux : ...
- Site web : ...
- Clientèle : ...
- Fournisseurs : ...
- Évaluation globale : ...

────────────────────────────────────────────
8. COMPTES
────────────────────────────────────────────
- Derniers comptes publiés (exercice clos le ...) :
  - CA : ...
  - Marge : ...
  - EBE : ...
  - Résultat net : ...
  - Total bilan : ...
  - Trésorerie : ...
- Observations : ...

────────────────────────────────────────────
9. FLUX OBSERVABLES
────────────────────────────────────────────
[Profils des entrants et sortants, contreparties principales]

────────────────────────────────────────────
10. CONTENTIEUX
────────────────────────────────────────────
- Procédures collectives : ...
- Contentieux fiscaux : ...
- Sanctions : ...
- Adverse media : ...

────────────────────────────────────────────
11. LIENS
────────────────────────────────────────────
- Capital : ...
- Dirigeants partagés : ...
- Adresse partagée : ...
- Trust / fondation au sommet : ...

────────────────────────────────────────────
12. CRYPTO (RENVOI OSINT CRYPTO)
────────────────────────────────────────────
[Référence rapport]

────────────────────────────────────────────
13. HYPOTHÈSES CALIBRÉES
────────────────────────────────────────────
| Hypothèse | Niveau WEP | Justification |
| ...       | ...        | ...           |

────────────────────────────────────────────
14. LACUNES ET ACTIONS
────────────────────────────────────────────
[Liste]

────────────────────────────────────────────
15. SOURCES
────────────────────────────────────────────
[Liste numérotée]
```

-----

### Annexe E — Modèle de fiche flux

```
FICHE FLUX — [Description courte]
Référence : [DOSSIER]/FLX/[NUM] | Version : [vN.N] | Date : [JJ/MM/AAAA]
Classification : [TLP]
Auteur : [Analyste]

────────────────────────────────────────────
1. DESCRIPTION
────────────────────────────────────────────
- Type : [virement / dépôt / opération crypto / etc.]
- Périmètre : [flux unique / séquence / schéma]
- Montant total : ...
- Devise(s) : ...
- Date(s) : ...

────────────────────────────────────────────
2. ORIGINE
────────────────────────────────────────────
- Compte donneur : ...
- Banque : ...
- Juridiction : ...
- Titulaire : ...
- Libellé émis : ...
- Donneur d'ordre réel (si distinct) : ...

────────────────────────────────────────────
3. TRANSIT
────────────────────────────────────────────
- Banques correspondantes : ...
- Comptes intermédiaires : ...
- Rails utilisés (SWIFT MT103/202, SEPA SCT, SCT Inst, crypto) : ...
- Étapes : ...

────────────────────────────────────────────
4. DESTINATION
────────────────────────────────────────────
- Compte bénéficiaire : ...
- Banque : ...
- Juridiction : ...
- Titulaire : ...
- Libellé reçu : ...

────────────────────────────────────────────
5. DÉLAI
────────────────────────────────────────────
- Heures de débit / crédit : ...
- Délais inter-étapes : ...

────────────────────────────────────────────
6. CONTEXTE
────────────────────────────────────────────
- Flux liés : ...
- Comportement antérieur : ...
- Motif déclaré : ...

────────────────────────────────────────────
7. COHÉRENCE ÉCONOMIQUE
────────────────────────────────────────────
- Compatibilité avec l'activité : ...
- Compatibilité avec les comptes annuels : ...
- Compatibilité avec le profil du titulaire : ...

────────────────────────────────────────────
8. TYPOLOGIE POSSIBLE
────────────────────────────────────────────
[Schéma compatible : TBML, BEC, layering, structuration, etc.]

────────────────────────────────────────────
9. HYPOTHÈSES CALIBRÉES
────────────────────────────────────────────
| Hypothèse | Niveau WEP | Justification |
| ...       | ...        | ...           |

────────────────────────────────────────────
10. SOURCES
────────────────────────────────────────────
[Liste]

────────────────────────────────────────────
11. LACUNES
────────────────────────────────────────────
[Liste]
```

-----

### Annexe F — Modèle de fiche actif

```
FICHE ACTIF — [Description courte]
Référence : [DOSSIER]/ACT/[NUM] | Version : [vN.N] | Date : [JJ/MM/AAAA]
Classification : [TLP]

────────────────────────────────────────────
1. IDENTIFICATION
────────────────────────────────────────────
- Nature : [immobilier / véhicule / yacht / aéronef / participation / œuvre / autre]
- Localisation : ...
- Identifiants (cadastral, immatriculation, IMO, registration) : ...
- Description : ...

────────────────────────────────────────────
2. DÉTENTEUR JURIDIQUE
────────────────────────────────────────────
- Personne physique ou morale : ...
- Forme et juridiction si entité : ...

────────────────────────────────────────────
3. UBO PROBABLE
────────────────────────────────────────────
[Personne physique, niveau WEP]

────────────────────────────────────────────
4. HISTORIQUE
────────────────────────────────────────────
- Date d'acquisition : ...
- Prix d'acquisition : ...
- Source de l'information : ...
- Mode de financement (si connu) : ...
- Transactions antérieures : ...

────────────────────────────────────────────
5. VALEUR ACTUELLE ESTIMÉE
────────────────────────────────────────────
- Estimation : ...
- Méthode et source : ...

────────────────────────────────────────────
6. PERTINENCE POUR LE DOSSIER
────────────────────────────────────────────
- Lien avec la cible : ...
- Cohérence avec les revenus déclarés : ...

────────────────────────────────────────────
7. ASSET RECOVERY
────────────────────────────────────────────
- Juridiction de saisie possible : ...
- Autorité compétente : ...
- Faisabilité estimée : ...

────────────────────────────────────────────
8. SOURCES
────────────────────────────────────────────
[Liste]
```

-----

### Annexe G — Matrice des red flags FININT (par typologie)

*Tableau synthétique des signaux d’alerte les plus courants, organisés par typologie. À utiliser comme grille de lecture rapide, non comme checklist mécanique : un red flag isolé ne prouve rien ; plusieurs convergents justifient l’investigation.*

|Typologie                        |Red flags principaux                                                                                                                                                                                                                                                                               |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**Blanchiment — placement**      |Dépôts cash fractionnés sous seuils, comptes alimentés par activités à forte composante cash incohérente avec profil client, onboarding rapide sur PSP/EME suivi d’activité immédiate inhabituelle, achats cash de biens revendables, multiplication de comptes de mules.                          |
|**Blanchiment — layering**       |Cascades de virements en cycle court, multi-juridictions sans rationale, conversions multiples de devises, transferts en cascade entre fintechs, sorties crypto via mixers/bridges, comptes courts (ouverts et clos rapidement), libellés vagues.                                                  |
|**Blanchiment — intégration**    |Acquisitions immobilières disproportionnées avec revenus, achats d’art à prix élevés, investissements dans sociétés sans expérience préalable, donations à organismes avec retours indirects, achats de luxe en cash ou crypto.                                                                    |
|**TBML**                         |Marges disproportionnées vs marché, décalages valeur facture / valeur de marché, contreparties sans activité réelle, transits par juridictions sans rationale, documents douaniers incohérents, paiements en avance disproportionnés, flux financiers déconnectés des flux physiques.              |
|**Corruption / PEP**             |Flux entrants depuis fournisseurs publics vers comptes personnels ou de proches, sociétés de conseil sans activité réelle, acquisitions disproportionnées par proches, train de vie incohérent, HATVP partielle ou contradictoire, lien temporel sortie de fonctions / début d’activité de conseil.|
|**Fraude TVA carrousel**         |Cycles d’opérations entre mêmes acteurs, sociétés sans substance faisant transit, crédits TVA disproportionnés, sociétés disparaissant brutalement, secteurs à risque (téléphonie, métaux, énergie, services digitaux).                                                                            |
|**Évasion fiscale**              |Charges intragroupe disproportionnées vers juridictions à faible imposition, prêts intragroupe sans intérêts, holdings intermédiaires sans substance, transferts de PI vers offshore + redevances.                                                                                                 |
|**ABS**                          |Virements société → comptes personnels du dirigeant sans contrepartie, factures personnelles payées par société, biens à usage privé, compte courant associé gonflé sans cohérence.                                                                                                                |
|**BEC / fraude au virement**     |IBAN nouveau et juridiction inhabituelle, libellé urgent, demande hors heures ouvrées, discrépance nom bénéficiaire / titulaire compte, activité immédiate de fractionnement et cashout sur compte récepteur, typosquatting d’email.                                                               |
|**Contournement de sanctions**   |Flux soudains vers juridictions tierces (Turquie, Émirats, Géorgie, Asie centrale), sociétés intermédiaires récemment créées, UBO lié à entité sanctionnée, activités dual-use, triangulation incohérente.                                                                                         |
|**Ponzi / pig butchering**       |Rendements promis très supérieurs au marché, pression à recruter, plateforme inconnue en juridiction obscure, retraits difficiles, garanties auto-désignées, endorsements suspects.                                                                                                                |
|**Criminalité organisée**        |Acquisitions opaques d’entreprises en difficulté, dirigeants à profil suspect, croissance soudaine inexpliquée, sous-traitance fictive, présence multi-juridictionnelle sans rationale.                                                                                                            |
|**Cybercriminalité / ransomware**|Paiements crypto urgents et significatifs, demandes en USDT/BTC/XMR, contextes d’incident IT en parallèle, conversions multiples sur exchanges asiatiques non-KYC.                                                                                                                                 |

-----

### Annexe H — Matrice “ce que je peux conclure / ce que je ne peux pas conclure”

*Aide-mémoire pour calibrer rigoureusement les conclusions selon les sources mobilisées et les éléments disponibles.*

|À partir de…                           |Je peux conclure (avec niveau WEP)                                                                                      |Je ne peux pas conclure                                                                    |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
|Registre du commerce + UBO RBE         |Mandats officiels (quasi-certain), UBO déclaré (quasi-certain), structure de capital (quasi-certain)                    |UBO réel si contrôle indirect, intention frauduleuse, substance économique                 |
|Comptes annuels publiés                |Profil financier (quasi-certain sous réserve de fiabilité comptable), ratios sectoriels (probable)                      |Réalité des transactions, ABS, fraude comptable sans expertise forensique                  |
|Adverse media (presse, ONG)            |Présence de soupçons publics (quasi-certain), réputation publique (quasi-certain)                                       |Culpabilité, faits non confirmés                                                           |
|Leaks (Pandora, Panama, etc.)          |Existence de structure offshore (quasi-certain si leak authentifié), settlor / bénéficiaires déclarés (quasi-certain)   |Finalité illicite sans recoupements, mise à jour post-leak                                 |
|Relevé bancaire                        |Flux observés (quasi-certain), patterns (probable), typologie compatible (probable au mieux)                            |Origine illicite des fonds sans infraction prédécesseur, intention, identification UBO réel|
|Analyse de réseau / graphe             |Liens formels (quasi-certain), centralités (quasi-certain), clusters (probable)                                         |Contrôle effectif, causalité, intention                                                    |
|Sanctions / PEP screening              |Présence sur listes (quasi-certain), statut PEP (quasi-certain)                                                         |Culpabilité, lien actif avec opérations sanctionnées                                       |
|OSINT crypto (Sarah Marin / partenaire)|Flux on-chain (quasi-certain), services traversés (probable à quasi-certain), identification cluster (probable)         |Identification individuelle de l’attaquant, attribution finale                             |
|Reconstitution patrimoniale            |Patrimoine identifié visible (quasi-certain), train de vie observable (probable)                                        |Cohérence avec revenus déclarés sans accès fiscal, patrimoine total réel                   |
|DS reçues en CRF                       |Faits déclarés par assujetti (quasi-certain), motifs de suspicion de l’assujetti (quasi-certain)                        |Réalité de l’infraction, qualification définitive                                          |
|Coopérations CRF étrangères (Egmont)   |Informations transmises (quasi-certain dans la limite de la coopération), faits confirmés par partenaire (quasi-certain)|Faits non couverts par la coopération, opacité juridictionnelle persistante                |

**Règle générale** : ce qu’on observe peut être *quasi-certain* ; ce qu’on déduit peut être *probable* à *très probable* avec recoupements ; ce qu’on attribue (intention, contrôle réel, infraction prédécesseur) est presque toujours *probable* au mieux, sauf documentation très solide.

-----

### Annexe I — Registres et sources par pays

*Liste opérationnelle des principaux registres et sources par juridiction. Non exhaustive ; mise à jour régulière nécessaire.*

|Pays                                                          |Registre entreprises                          |UBO / équivalent                                                                                     |Comptes annuels      |Notes                                     |
|--------------------------------------------------------------|----------------------------------------------|-----------------------------------------------------------------------------------------------------|---------------------|------------------------------------------|
|France                                                        |Pappers, INPI, Infogreffe, BODACC             |RBE (accès restreint depuis CJUE)                                                                    |Infogreffe, Pappers  |DVF + Patrim pour patrimoine              |
|Royaume-Uni                                                   |Companies House                               |PSC (public)                                                                                         |Companies House      |LP écossais sous PSC depuis 2017          |
|Allemagne                                                     |Handelsregister, Bundesanzeiger               |Transparenzregister                                                                                  |Bundesanzeiger       |Coopération solide                        |
|Italie                                                        |Registro Imprese, Telemaco                    |Registro UBO                                                                                         |Registro Imprese     |Accès complet payant                      |
|Espagne                                                       |Registro Mercantil Central                    |Registre UBO (en cours)                                                                              |RMC                  |Coopération solide                        |
|Belgique                                                      |BCE / KBO, Moniteur belge                     |UBO Register (accès restreint)                                                                       |Moniteur belge       |Coopération solide                        |
|Pays-Bas                                                      |KvK                                           |UBO Register (accès très restreint post-CJUE)                                                        |KvK                  |Riche en holdings                         |
|Luxembourg                                                    |RCS, Monitor Lëtzebuerg                       |RBE (restreint post-CJUE)                                                                            |RCS                  |Holdings, fonds, banque privée            |
|Suisse                                                        |Moneyhouse, Zefix                             |Pas d’UBO public, vigilance KYC                                                                      |Limité au public     |MROS (CRF) coopère via Egmont             |
|Autriche                                                      |Firmenbuch                                    |Wirtschaftliche Eigentümer (restreint)                                                               |Firmenbuch           |Coopération solide                        |
|Pologne                                                       |KRS                                           |CRBR (UBO)                                                                                           |KRS                  |Bonne accessibilité                       |
|République tchèque                                            |Justice OR                                    |UBO public                                                                                           |OR                   |Coopération                               |
|Irlande                                                       |CRO                                           |RBO (restreint)                                                                                      |CRO                  |Holdings et tech                          |
|Portugal                                                      |Portal da Justiça                             |RCBE (restreint)                                                                                     |Portal               |Coopération                               |
|Estonie                                                       |Ariregister                                   |UBO public                                                                                           |Ariregister          |Coopération solide                        |
|Lettonie                                                      |UR                                            |UBO public                                                                                           |UR                   |Coopération                               |
|Lituanie                                                      |Centre d’information                          |UBO (restreint)                                                                                      |Centre               |Coopération                               |
|Roumanie                                                      |ONRC                                          |UBO                                                                                                  |ONRC                 |Coopération                               |
|Bulgarie                                                      |TR                                            |UBO                                                                                                  |TR                   |Coopération                               |
|Hongrie                                                       |E-cégjegyzék                                  |Pas d’UBO public                                                                                     |E-cégjegyzék         |Coopération                               |
|Chypre                                                        |Cyprus Department of Registrar                |UBO (très restreint, post-CJUE)                                                                      |Limité               |Cluster offshore significatif             |
|Malte                                                         |MBR                                           |UBO (restreint)                                                                                      |MBR                  |Yachts, gaming                            |
|États-Unis                                                    |OpenCorporates, SEC EDGAR, registres étatiques|CTA exempte depuis mars 2025 les sociétés domestiques US ; subsiste pour certaines entités étrangères|SEC EDGAR pour cotées|LLC Delaware, Wyoming, Nevada très opaques|
|Canada                                                        |Corporations Canada, registres provinciaux    |UBO en déploiement                                                                                   |Variable             |Coopération solide                        |
|Royaume-Uni Crown Dependencies (Jersey, Guernsey, Isle of Man)|Variables                                     |Limités                                                                                              |Limités              |Trusts notables                           |
|BVI                                                           |Registry of Corporate Affairs                 |BOSS (autorités locales seulement)                                                                   |Non publics          |Cluster offshore majeur                   |
|Cayman                                                        |Registre                                      |Pas public                                                                                           |Pas publics          |Funds notamment                           |
|Bahamas                                                       |Registre                                      |Pas public                                                                                           |Pas publics          |Trusts                                    |
|Panama                                                        |Registro Público                              |Pas public                                                                                           |Limités              |Historique Panama Papers                  |
|Émirats Arabes Unis                                           |DED Dubai, ADCCI Abu Dhabi, free zones        |Limité                                                                                               |Limité               |Free zones (DIFC, ADGM) plus accessibles  |
|Liban                                                         |Registre commercial libanais                  |Faible                                                                                               |Faible               |Coopération difficile                     |
|Israël                                                        |Registre des sociétés                         |Faible                                                                                               |Limités              |Coopération solide via Egmont             |
|Turquie                                                       |MERSIS                                        |Faible                                                                                               |Limités              |Vigilance contournement sanctions         |
|Russie                                                        |EGRUL (accessible mais restrictions)          |Faible                                                                                               |EGRUL                |Vigilance sanctions                       |
|Chine                                                         |NECIPS                                        |Faible                                                                                               |Limités              |Coopération difficile                     |
|Hong Kong                                                     |Companies Registry                            |SCR (restreint)                                                                                      |Limités              |Place financière majeure                  |
|Singapour                                                     |ACRA / BizFile                                |UBO (autorités)                                                                                      |ACRA                 |Coopération solide                        |
|Australie                                                     |ASIC                                          |Faible                                                                                               |ASIC                 |Coopération solide                        |
|Afrique du Sud                                                |CIPC                                          |Faible                                                                                               |CIPC                 |Coopération via Egmont                    |
|Pays africains francophones                                   |Registres CGI / RCCM variables                |Très limités                                                                                         |Très limités         |Coopération hétérogène                    |
|Brésil                                                        |Receita Federal                               |Cadastre UBO                                                                                         |Limités              |Coopération                               |
|Mexique                                                       |RPC                                           |UBO en déploiement                                                                                   |Limités              |Coopération                               |
|Inde                                                          |MCA21                                         |Limités                                                                                              |MCA21                |Coopération                               |
|Japon                                                         |National Tax Agency / EDINET                  |Limités                                                                                              |EDINET pour cotées   |Coopération solide                        |

**Sources transversales** :

- OpenCorporates (multi-juridiction).
- Sayari (multi-juridiction professionnelle).
- Orbis (Moody’s / Bureau van Dijk).
- ICIJ Offshore Leaks (multi-leaks).
- OCCRP Aleph.

-----

### Annexe J — Outils par usage (catalogue raisonné)

*Liste organisée par usage opérationnel — accès gratuit, freemium ou professionnel.*

**Identification d’entreprises** :

- Gratuit : Pappers (France), Companies House (UK), Bundesanzeiger (Allemagne), OpenCorporates (multi), BRIS via e-justice (UE).
- Professionnel : Sayari, Orbis, Dun & Bradstreet.

**UBO et structures de contrôle** :

- Gratuit : RBE France (restreint), PSC UK (public), ICIJ Offshore Leaks.
- Professionnel : Sayari (analyse de chaînes), Orbis Ownership.

**Comptes annuels** :

- Gratuit : Pappers, Companies House, Bundesanzeiger.
- Professionnel : Orbis (multi-juridictions consolidées).

**Sanctions et PEP** :

- Gratuit : OpenSanctions, OFAC SDN, UE consolidated list, OFSI, ONU.
- Professionnel : World-Check (LSEG), Dow Jones Risk & Compliance, LexisNexis Bridger.

**Adverse media** :

- Gratuit : Google News (limité), OCCRP, ICIJ.
- Professionnel : Factiva, Nexis Newsdesk, LexisNexis Diligence.

**Patrimoine immobilier** :

- France : DVF (data.gouv.fr), Patrim (espace personnel impots.gouv.fr), cadastre.gouv.fr.
- UK : HM Land Registry.
- US : registres comtés, Zillow, Redfin pour estimations.

**Yachts et navires** :

- Gratuit : MarineTraffic (free tier), VesselFinder.
- Professionnel : Lloyd’s List Intelligence.

**Aéronefs** :

- Gratuit : FlightAware, ADS-B Exchange.
- Professionnel : Cirium Diio.

**Marchés publics** :

- Gratuit : BOAMP (France), DECP (data.gouv.fr), TED (UE), SAM.gov (US), USAspending.gov.

**Visualisation** :

- Gratuit : Maltego Community, Gephi, Cytoscape.
- Professionnel : Maltego Pro/Enterprise, i2 Analyst’s Notebook, Linkurious, Graphistry.

**Capture et chain of custody** :

- Gratuit : Singlefile (extension), Wayback Machine.
- Professionnel : Hunchly.

**Recherche d’images inverse** :

- Gratuit : Google Images, TinEye, Yandex Images.

**SOCMINT** :

- Gratuit : LinkedIn (avec compte), recherches publiques X / Facebook / Instagram.
- Professionnel : Maltego transforms SOCMINT, Bellingcat resources.

**Données fiscales et leaks** :

- Gratuit : ICIJ Offshore Leaks (Pandora, Panama, Paradise, Bahamas, FinCEN Files).
- Professionnel : Aleph OCCRP (accès journalistique).

**Crypto (renvoi OSINT Crypto)** :

- Gratuit : block explorers (Etherscan, Blockchain.com, Tronscan, etc.), Breadcrumbs.
- Professionnel : Chainalysis Reactor, TRM Labs, Elliptic.

-----

### Annexe K — Modèle de note FININT

```
[CLASSIFICATION : TLP:XXX]

NOTE FININT
Référence : [DOSSIER/AAAA/NUM]
Date : [JJ/MM/AAAA] | Version : [vN.N]
Auteur(s) : [Nom, fonction]
Destinataires : [Liste explicite]

────────────────────────────────────────────
1. RÉSUMÉ EXÉCUTIF (10-15 lignes)
────────────────────────────────────────────
[Objet de la note, conclusions calibrées principales, recommandations clés.
À lire en moins de 2 minutes.]

────────────────────────────────────────────
2. MANDAT ET QUESTIONS DE RENSEIGNEMENT
────────────────────────────────────────────
- Origine de la saisine : ...
- Périmètre : ...
- Questions de renseignement (QR) :
  - QR1 : ...
  - QR2 : ...
  - QR3 : ...

────────────────────────────────────────────
3. MÉTHODOLOGIE
────────────────────────────────────────────
- Sources mobilisées : OSINT (registres, leaks, presse, SOCMINT), CRF (DS, droits de communication, coopération internationale), partenaires (le cas échéant).
- Limites du périmètre : [explicites]
- Échelle de calibration utilisée : WEP.

────────────────────────────────────────────
4. CONTEXTE
────────────────────────────────────────────
[Présentation de la situation, des acteurs principaux, de la chronologie.]

────────────────────────────────────────────
5. ANALYSE
────────────────────────────────────────────
5.1 Entités identifiées
[Liste, avec renvoi vers fiches société en annexe]

5.2 Personnes physiques identifiées
[Liste, avec renvoi vers fiches personne en annexe]

5.3 Flux observés
[Synthèse, avec renvoi vers fiches flux en annexe]

5.4 Patrimoine et actifs identifiés
[Synthèse, avec renvoi vers fiches actif en annexe]

5.5 Typologies probables
[Qualification des schémas, calibration WEP]

────────────────────────────────────────────
6. HYPOTHÈSES CALIBRÉES
────────────────────────────────────────────
| Hypothèse | Niveau WEP | Justification synthétique |
| H1        | ...        | ...                       |
| H2        | ...        | ...                       |
| ...       | ...        | ...                       |

────────────────────────────────────────────
7. LACUNES IDENTIFIÉES
────────────────────────────────────────────
- Ce qui n'a pas pu être établi : ...
- Pourquoi : ...
- Comment le faire : ...

────────────────────────────────────────────
8. RECOMMANDATIONS
────────────────────────────────────────────
- Actions immédiates : [gel, signalement, coopérations urgentes]
- Actions à court terme : [coopérations, approfondissements]
- Actions à moyen / long terme : [coopérations internationales, monitoring]

────────────────────────────────────────────
9. ANNEXES
────────────────────────────────────────────
- Annexe A : Fiches personne (réf XXX/PER/...)
- Annexe B : Fiches société (réf XXX/SOC/...)
- Annexe C : Fiches flux (réf XXX/FLX/...)
- Annexe D : Fiches actif (réf XXX/ACT/...)
- Annexe E : Graphe principal du réseau
- Annexe F : Rapport on-chain partenaire (si applicable)
- Annexe G : Sources et chaîne de preuve

────────────────────────────────────────────
SOURCES
────────────────────────────────────────────
[Liste numérotée avec dates et chains of custody]
```

-----

### Annexe L — Erreurs fréquentes et 5 mini-cas d’entraînement

#### Top 12 erreurs fréquentes en FININT

1. **Conclure sur 2 attributs faibles** pour identifier une personne (homonymie).
1. **Confondre dénomination commerciale et dénomination sociale** (sociétés homonymes).
1. **Surinterpréter une présence dans un leak** sans qualification de la nature de la structure.
1. **Considérer toute société écran comme illégale** (beaucoup d’usages légitimes).
1. **Conclure « prête-nom » sans recoupement** (un cumul d’indices est nécessaire).
1. **Ignorer la cohérence sectorielle** lors de l’analyse comptable.
1. **Surcharger un graphe** au point de le rendre illisible.
1. **Confondre lien fort et contrôle** : co-présence dans un CA ne dit pas qui contrôle.
1. **Vocabulaire affirmatif sans calibration** : « il blanchit », « c’est l’UBO » sans WEP.
1. **Sous-estimer les délais** des coopérations internationales.
1. **Refaire OSINT Crypto** dans la note FININT au lieu de renvoyer au partenaire.
1. **Pas de mention des lacunes** : la note lisse trompe le lecteur.

#### 5 mini-cas d’entraînement

*Cas courts à traiter mentalement ou sur tableur, avec correction synthétique en fin.*

##### Mini-cas 1 — La SAS opportune

Une SAS française est créée il y a 6 mois. Capital 1 €. Président : un homme de 78 ans, ancien employé d’un garage automobile. Activité déclarée : « commerce de gros non spécialisé ». Domiciliation : cabinet parisien (89 autres entités). Sur 6 mois, CA déclaré (estimation via flux observables fournis) : 1,8 M€.

Que concluez-vous, et que faites-vous ?

*Éléments de réponse* : profil de signaux convergents (création récente, capital symbolique, dirigeant à profil incohérent, domiciliation cluster, CA disproportionné). Société probablement écran ou utilisée pour un schéma spécifique. Investigation : profil du dirigeant (fronting probable), flux observables (typologie), contreparties (cohérence sectorielle), liens à d’autres entités. À ce stade, qualification *probable* écran ; finalité (TBML, fraude TVA, BEC, blanchiment) *indéterminable* sans investigation des flux.

##### Mini-cas 2 — Le virement urgent

Le DAF d’une PME reçoit un email du président, depuis l’adresse habituelle, demandant un virement urgent et confidentiel de 480 K€ vers un IBAN slovaque pour finaliser une « acquisition stratégique ». Le DAF s’apprête à valider.

Que doit-il faire ?

*Éléments de réponse* : pattern classique de fraude au président. À faire : vérification téléphonique du président (sur numéro connu, pas celui de l’email), validation par double signature, vérification VOP de la cohérence nom bénéficiaire / titulaire IBAN, suspension du virement si moindre doute. Si fraude avérée et virement effectué : contact immédiat banque (gel), plainte, FININT/CRF.

##### Mini-cas 3 — Le marché public favori

Une PME du BTP remporte 12 marchés publics consécutifs dans une commune sur 4 ans, pour un total de 18 M€. La PME est dirigée par un cousin de l’adjointe aux travaux de la commune.

Que regardez-vous, et que concluez-vous ?

*Éléments de réponse* : pattern de favoritisme probable. Vérifications : conditions d’attribution (mode de passation, critères, concurrence réelle), valeur des marchés vs marché, déclarations d’intérêts de l’adjointe (HATVP, déport), liens familiaux confirmés. Si tout converge : signalement à l’AFA (Agence Française Anticorruption) et au PNF. Qualification *probable* favoritisme et prise illégale d’intérêts à ce stade ; *quasi-certain* sous condition de confirmation des éléments.

##### Mini-cas 4 — Le client PEP

Une banque privée européenne reçoit pour client un ancien ministre africain ayant déposé 8 M€ sur 6 mois, présentés comme produit de cessions d’actifs personnels. La documentation justificative est partielle.

Quelle posture pour la banque ?

*Éléments de réponse* : statut PEP confirmé → vigilance renforcée. Documentation insuffisante = obstacle au monitoring. Demande de justificatifs complets (déclarations fiscales, contrats de cession, identification des acquéreurs). Sans documentation satisfaisante : DS à la CRF, évaluer rupture commerciale. La présomption d’innocence du client demeure ; la banque ne décide pas de la culpabilité — elle décide de sa propre exposition.

##### Mini-cas 5 — Le pattern crypto

Un dossier en cours montre des conversions répétées EUR → USDT sur fintech européenne, puis transferts USDT vers wallets externes via plusieurs adresses. La banque sollicite votre analyse.

Comment procédez-vous ?

*Éléments de réponse* : FININT cadre (contexte client, comptes alimentant la fintech, motif déclaré). OSINT Crypto (partenaire ou interne) trace on-chain les USDT depuis dépôt sur fintech jusqu’aux off-ramps ou usages. Synthèse intégrée. Renvoi explicite vers OSINT Crypto pour les méthodes et résultats détaillés. La note FININT n’essaie pas de refaire l’analyse on-chain.

-----

### Annexe M — Cadres d’accès aux sources

*Tableau de synthèse pour clarifier, à chaque consultation, qui peut accéder à quoi. Le FININT mobilise plusieurs cadres ; les confondre crée des erreurs juridiques et déontologiques.*

|Type de source                       |Exemples                                                                                                                                                                           |Accessible par                                                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|**OSINT public gratuit**             |Pappers (gratuit), Companies House UK, OpenCorporates, OpenSanctions, ICIJ Offshore Leaks, DVF, BODACC, BOAMP, presse                                                              |Tout analyste, journaliste, cabinet, étudiant, particulier. Pas de restriction d’usage hors RGPD et droit.                                         |
|**OSINT freemium**                   |Pappers Premium, MarineTraffic Premium, agrégateurs partiellement payants                                                                                                          |Tout analyste ayant un compte payant. Conditions d’utilisation à respecter.                                                                        |
|**Sources professionnelles payantes**|Sayari, Orbis (Moody’s/BvD), Dun & Bradstreet, World-Check (LSEG), Dow Jones Risk & Compliance, LexisNexis Bridger / Diligence, Factiva, Bloomberg, Refinitiv Eikon, S&P Capital IQ|Organisations abonnées (banques, cabinets, institutions). Licence individuelle ou entreprise.                                                      |
|**Sources assujetti LCB-FT**         |KYC interne, monitoring transactions, données clientèle, droits de communication LCB-FT                                                                                            |Banques, PSP, assurances, casinos, notaires, avocats sous condition, agents immobiliers, etc. Cadre de la 5e/6e directive AML et CMF.              |
|**Sources CRF (FIU)**                |DS reçues, FIU.NET, Egmont Secure Web, coopérations CRF étrangères, droits de communication CRF (CMF)                                                                              |TRACFIN et CRF homologues uniquement. Cadre légal strict (CMF, lois LCB-FT).                                                                       |
|**Sources judiciaires**              |Réquisitions bancaires, FICOBA, FICOVIE, FIBEN (sous condition), perquisitions, auditions, MLA, EAR/CRS via DGFiP, écoutes (sous mandat)                                           |Magistrats (juge d’instruction, procureur) ; policiers et gendarmes sous procédure ; officiers de police judiciaire mandatés. Cadre du CPP.        |
|**Sources fiscales et douanières**   |DGFiP (DNEF), DGDDI, échanges fiscaux internationaux (DAC, EAR/CRS), bases douanières internes                                                                                     |Administrations fiscales et douanières. Coopération inter-administrations sur cadre légal.                                                         |
|**Sources sanctions**                |Listes OFAC SDN, listes UE consolidées, listes ONU, OFSI, registre national des gels DG Trésor                                                                                     |Public pour consultation des listes. Action de gel : autorités compétentes (DG Trésor — pôle sanctions financières en France).                     |
|**Sources HATVP**                    |Déclarations d’intérêts et de patrimoine publiques (selon fonctions et seuils)                                                                                                     |Public selon les fonctions concernées et les seuils. Pas toutes les fonctions publiques sont couvertes de la même manière (selon les seuils HATVP).|
|**Sources presse / leaks**           |ICIJ Aleph (accès journalistique principal), OCCRP Aleph, Pandora Papers via ICIJ portal                                                                                           |Journalistes partenaires (Aleph complet) ; public pour la version publique des leaks ; analystes peuvent consulter le portail public.              |
|**Sources OSINT Crypto**             |Etherscan, Tronscan, Chainalysis Reactor, TRM Labs, Elliptic, Breadcrumbs                                                                                                          |Public pour explorers ; abonnés pour outils pro. Cadre à vérifier selon les juridictions.                                                          |

**Règles essentielles** :

1. **Ne pas confondre OSINT et sources fermées** : un analyste OSINT pur ne dispose pas de FICOBA, EAR/CRS, FIU.NET. Il doit l’expliciter dans tout livrable.
1. **Cadre du dossier détermine les sources accessibles** : un dossier de due diligence cabinet ≠ dossier CRF ≠ dossier judiciaire. Ne pas mobiliser des sources hors périmètre.
1. **Documenter la source de chaque élément** : la chain of custody (chapitre 53) impose la traçabilité de la provenance.
1. **RGPD applicable** : pour les données personnelles, vérifier la base légale, la finalité, la conservation, les droits des personnes.
1. **Secret professionnel** : pour les CRF, magistrats, policiers, avocats, le secret applicable limite la diffusion.

Cette annexe est l’**amélioration pédagogique la plus importante** du cours : elle clarifie, pour chaque chapitre et chaque source citée, qui peut effectivement y accéder. À chaque mobilisation d’une source dans un livrable, l’analyste se demande : *« Mon cadre d’exercice m’autorise-t-il à utiliser cette source ? »*

-----

### Annexe N — Bibliographie de sources primaires

*Liste structurée des sources primaires à consulter pour approfondir le cours, vérifier les évolutions, et alimenter la veille. Non exhaustive ; mise à jour continue nécessaire.*

#### Cadres internationaux

- **GAFI / FATF** — Recommandations, méthodologie d’évaluation, rapports thématiques, listes (noire, grise). `https://www.fatf-gafi.org/`
- **Egmont Group** — Présentation du réseau mondial des CRF, principes opérationnels. `https://egmontgroup.org/`
- **OCDE** — Convention anti-corruption (1997), Working Group on Bribery, BEPS, Common Reporting Standard. `https://www.oecd.org/`
- **ONU** — Convention de Mérida contre la corruption (2003), Convention de Palerme contre le crime organisé (2000), sanctions ONU. `https://www.unodc.org/`
- **Conseil de l’Europe — GRECO** — Évaluations anticorruption européennes.
- **Conventions de Strasbourg / Varsovie** — Blanchiment.

#### Cadres européens

- **AML Package UE 2024** — Règlement AMLR, directive AMLD6, règlement AMLA. JOUE 19/06/2024.
- **MiCA — Règlement 2023/1114** — Markets in Crypto-Assets.
- **TFR — Règlement 2023/1113** — Travel Rule sur les transferts de crypto-actifs.
- **Instant Payments Regulation** — VOP.
- **Règlement 2021/821** — Biens à double usage.
- **Règlements de sanctions UE** — Consolidés sur le site des sanctions UE.
- **Règlement 2018/1805** — Reconnaissance mutuelle des décisions de gel et de confiscation en UE.

#### Autorités françaises

- **TRACFIN** — Rapport annuel, tendances, lignes directrices. `https://www.economie.gouv.fr/tracfin`
- **ACPR** — Lignes directrices LCB-FT, sanctions publiques. `https://acpr.banque-france.fr/`
- **AMF** — Régulation marchés et crypto-actifs. `https://www.amf-france.org/`
- **DG Trésor — Pôle sanctions financières internationales** — Registre national des gels, sanctions, lignes directrices. `https://www.tresor.economie.gouv.fr/`
- **AFA** — Agence Française Anticorruption.
- **HATVP** — Haute Autorité pour la Transparence de la Vie Publique.
- **AGRASC** — Agence de gestion et recouvrement des avoirs saisis et confisqués.
- **PNF, JUNALCO, JIRS** — Sources de jurisprudence et communiqués publics.

#### Autorités américaines

- **FinCEN** — Avis, alertes, SAR Statistics, mises à jour BOI/CTA. `https://www.fincen.gov/`
- **OFAC** — SDN List, FAQs, sanctions secondaires. `https://ofac.treasury.gov/`
- **DOJ** — Press releases (jurisprudence sanctionnée).
- **SEC** — EDGAR (cotées), enforcement actions.

#### Autorités UK

- **OFSI** — Sanctions financières UK. `https://www.gov.uk/government/organisations/office-of-financial-sanctions-implementation`
- **HMRC** — Coopération fiscale.
- **NCA** — National Crime Agency, UKFIU.

#### Coopérations européennes et internationales

- **Europol** — Rapports thématiques (IOCTA, SOCTA), Centres EC3, EFECC. `https://www.europol.europa.eu/`
- **Eurojust** — Coopération judiciaire UE. `https://www.eurojust.europa.eu/`
- **EPPO — Parquet européen** — Affaires PIF (Protection des Intérêts Financiers UE). `https://www.eppo.europa.eu/`
- **Interpol** — Notices, Project Stamp (corruption transnationale).
- **CARIN** — Réseau Camden Asset Recovery Inter-agency.

#### Sources d’investigation et leaks

- **ICIJ — International Consortium of Investigative Journalists** — Offshore Leaks, Pandora, Panama, Paradise, FinCEN Files. `https://www.icij.org/`
- **OCCRP — Organized Crime and Corruption Reporting Project** — Investigations, Aleph (accès journalistique). `https://www.occrp.org/`
- **Bellingcat** — Méthodes OSINT (investigation publique). `https://www.bellingcat.com/`
- **Transparency International** — Indices et rapports corruption. `https://www.transparency.org/`
- **Tax Justice Network** — Financial Secrecy Index, Corporate Tax Haven Index. `https://taxjustice.net/`

#### Cours et certifications

- **ACAMS** — Certification CAMS, ressources. `https://www.acams.org/`
- **ACFE** — Certification CFE. `https://www.acfe.com/`
- **ACFCS** — Certification CFCS. `https://www.acfcs.org/`

#### Presse spécialisée recommandée

- **Financial Times** (notamment Dan McCrum sur Wirecard et investigations).
- **Reuters** (investigations financières).
- **Bloomberg** (financial crime).
- **Le Monde — section enquêtes**.
- **Mediapart** (corruption, evasion fiscale en France).
- **Süddeutsche Zeitung** (à l’origine des Panama Papers).
- **The Guardian** (investigations transnationales).
- **OCCRP Daily** — Newsletter.

#### Veille recommandée

- **Lecture régulière** des rapports annuels TRACFIN, FATF, Europol IOCTA.
- **Suivi** des bulletins ACPR, AMF, DG Trésor.
- **Alertes** sur OpenSanctions pour mises à jour de listes.
- **Newsletters** spécialisées : Money Laundering Watch, Compliance Week, ACAMS Today.

-----

### Parcours de lecture recommandés

*Le cours est dense — 70 chapitres + 1 chapitre 0 de mise à niveau + 14 annexes. Selon le profil et l’objectif, trois parcours adaptés sont proposés.*

#### Parcours débutant — première découverte du FININT (8 à 12 heures)

Pour un lecteur sans bagage préalable, qui souhaite comprendre la discipline et acquérir des réflexes de base :

- Avant-propos et table des matières.
- **Chapitre 0 — Mise à niveau** (intégral, 1 à 2 heures) : bases économiques, juridiques et financières indispensables.
- **Parcours express 45 minutes** (intégral).
- Présentation du fil rouge CLEARFLOW.
- **Partie I complète** (Chapitres 1-5) : fondations.
- **Chapitre 11** : registres entreprises français.
- **Chapitre 13** : UBO.
- **Chapitres 19-20** : identification personnes et sociétés.
- **Chapitres 27-28** : fiches personne et société.
- **Chapitre 33** : échelle WEP et hypothèses calibrées.
- **Chapitre 54** : note FININT, rapport et diffusion.
- **Annexe A** : glossaire (à parcourir).
- **Annexe M** : cadres d’accès aux sources.

À la fin de ce parcours, le lecteur sait identifier une entité, calibrer une conclusion, structurer un livrable basique, et orienter une investigation simple.

#### Parcours analyste FININT — formation cœur (40 à 60 heures)

Pour un analyste en formation visant la pratique opérationnelle :

- Tout le parcours débutant.
- **Partie II complète** : système financier et flux.
- **Partie III complète** : sources OSINT.
- **Partie IV complète** : personnes, sociétés, contrôle.
- **Partie V complète** : cartographier les réseaux.
- **Partie VI complète** : analyse de flux et comptabilité forensique.
- **Partie VII** : sélection (Chapitres 40-43, 44, 48 prioritaires).
- **Partie VIII complète** : outils, workflow, production.
- **Partie IX complète** : cas pratiques 1-5.
- **Annexes A-L** : modèles, matrices, registres, outils.

À la fin, l’analyste est capable de conduire de bout en bout une enquête FININT complexe : cadrage, collecte, analyse, livrables, recommandations.

#### Parcours expert / institutionnel — vision stratégique (15 à 25 heures)

Pour un cadre dirigeant, magistrat, responsable conformité, ou décideur souhaitant la vision d’ensemble sans le détail méthodologique fin :

- Avant-propos.
- **Parcours express 45 minutes**.
- Présentation du fil rouge CLEARFLOW.
- **Partie X complète** : cas historiques (Panama, 1MDB, Wirecard, Danske Bank), coopération internationale, asset recovery, cadre français, éthique, capacité durable.
- **Chapitre 70** : évolutions réglementaires 2024-2026.
- **Synthèse fil rouge — Chapitre 64**.
- **Annexes G, H, M, N** : matrices red flags, qualification, cadres d’accès, bibliographie.

À la fin, le décideur a une vision claire de ce que peut et ne peut pas produire un service FININT, des coopérations à mobiliser, des évolutions à anticiper.

-----

## CLÔTURE

Ce cours a couvert le **renseignement financier (FININT)** de bout en bout : fondations conceptuelles, sources et registres, identification des personnes et des structures, cartographie des réseaux, analyse des flux et comptabilité forensique, typologies de criminalité financière, outils et workflow, cas pratiques fictifs et historiques, coopération internationale, asset recovery, cadre français, éthique, construction d’une capacité durable, et mise à niveau des évolutions réglementaires 2024-2026.

Le fil rouge **CLEARFLOW** a illustré, à travers le travail fictif de Nassim Belhaj dans une CRF inspirée de TRACFIN, les méthodes, les rythmes, les coopérations et les limites d’une enquête FININT complexe. Les quatorze annexes fournissent les outils opérationnels prêts à utiliser — dont, en particulier, l’**Annexe M (cadres d’accès aux sources)** qui clarifie ce que chaque type d’acteur peut effectivement consulter, et la **Bibliographie de sources primaires (Annexe N)** pour la veille continue.

Le FININT n’est ni la cybercriminalité, ni l’OSINT crypto, ni la conformité, ni l’audit forensique — mais il les **articule** tous. Il est l’angle d’attaque qui suit l’argent à travers les sociétés, les juridictions, les structures, les comptes, pour comprendre **qui** fait **quoi**, **pour qui** et **dans quel but**. Il est, en 2025-2026, l’une des disciplines les plus stratégiques pour la lutte contre la criminalité économique et financière sous toutes ses formes.

Pour le volet on-chain (cryptomonnaies, DeFi, NFT, mixers, bridges, exchanges), le cours **OSINT Crypto** complémentaire — pris en charge dans le fil rouge par Sarah Marin et Athéna Group, sous cadre contractuel et déontologique strict — apporte les méthodes spécifiques au suivi blockchain.

L’analyste FININT compétent en 2025-2026 maîtrise les fondamentaux exposés ici, les enrichit en continu par la veille et la formation, coopère avec les disciplines voisines, distingue rigoureusement les cadres d’accès aux sources, et exerce avec discipline, calibration et rigueur déontologique. La qualité du renseignement produit conditionne directement la qualité de l’action des autorités qui l’utilisent — c’est une responsabilité, et c’est la valeur du métier.

*Bonne pratique.*

-----

*Fin du cours.*
