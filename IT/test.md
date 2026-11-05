# Guide de montée en compétences : IGC, certificats numériques, Rossignol, CMS, TPM, MOTUS et LICORNE

**Formation technique et opérationnelle — du niveau débutant à avancé**  
**Contexte : ministères économiques et financiers (MEF)**  
**Références publiques : novembre 2026**

> **Périmètre et prudence.** Ce guide associe les principes généraux des infrastructures à clés publiques aux informations documentées publiquement concernant les MEF. Les procédures exactes, les infrastructures internes et les configurations de MOTUS/LICORNE doivent être confirmées auprès des équipes et dans les référentiels habilités. Les exemples d'agents et les scénarios opérationnels sont fictifs.

## Objectifs de la formation

À l'issue de ce parcours, tu dois pouvoir :

- expliquer à quoi servent une IGC/PKI, une autorité de certification, une autorité d'enregistrement et un CMS ;
- distinguer un certificat X.509, une clé publique et une clé privée ;
- comprendre les supports : carte Rossignol, puce TPM, clé USB cryptographique et mobile ;
- suivre le cycle de vie d'une identité et de ses certificats : demande, validation, délivrance, renouvellement, révocation et remplacement ;
- comprendre l'authentification Windows, les applications web, les VPN et le Wi-Fi par certificat ;
- qualifier les incidents et savoir vers quel acteur les escalader ;
- lire une politique de certification et dialoguer avec les équipes IGC, CMS, SSI, poste de travail et mobilité.

---

# 1. Vue d'ensemble

## 1.1. Les cinq niveaux de l'écosystème

```text
                       IDENTITÉ DE L'AGENT
                    RH / annuaire / référentiel
                                |
                        Validation de l'identité
                                |
                   +------------+------------+
                   |                         |
            CMS / Self-Service CMS          IGC / PKI
             Cycle de vie               Certification
                   |                         |
                   +------------+------------+
                                |
                        Supports de clés
          +----------------+------+----------------+
          |                |      |                |
     Carte Rossignol      TPM   Token USB       Mobile
          |                |      |                |
          +----------------+------+----------------+
                                |
                    Preuve cryptographique
                                |
              AD / VPN / Wi-Fi / applications / SSO
                                |
                       Autorisation d'accès
```

*Ce dessin est un schéma conceptuel, pas l'architecture officielle du ministère.*

| Niveau | Question centrale |
|---|---|
| Identité | Qui est l'agent ? |
| Gestion | Qui lui attribue les cartes et certificats ? |
| Confiance | Qui certifie le lien entre son identité et sa clé publique ? |
| Support | Où la clé privée est-elle conservée et protégée ? |
| Utilisation | Comment l'identité est-elle vérifiée puis autorisée par un service ? |

**Idée clé :** l'IGC établit la confiance, le certificat représente une identité certifiée, la clé privée permet d'en prouver la possession, le support la protège et l'application décide de l'accès.

## 1.2. Ce qui est documenté pour les MEF

La documentation publique distingue notamment :

1. **Rossignol**, dispositif de carte agent multiservices, avec des certificats et des fonctions physiques et numériques.
2. **Le CMS Rossignol**, utilisé notamment pour la demande, la validation, la délivrance, la désactivation et le déblocage des cartes.
3. **Le Self-Service CMS**, mentionné pour installer, renouveler ou gérer des certificats sur le TPM du poste et sur les mobiles MOTUS et LICORNE.
4. **L'offre de certification Rossignol**, documentant des AC d'authentification/signature et de confidentialité, en version standard ou qualifiée selon les cas.
5. **L'IGC interne du Secrétariat général (IGC-SG)**, qui publie notamment des offres pour agents, prestataires, serveurs et services.

Les deux dernières offres sont présentes sur le portail public des MEF, mais il ne faut pas en conclure que tous les certificats relèvent de la même chaîne de certification.

**Références officielles :**

- [IGPDE — CMS Rossignol, délivrance par les opérateurs AIP (formation 102677)](https://catalogue.igpde.finances.gouv.fr/1952-cms-rossignol-delivrance-de-cartes-agent-multi-services-rossignol-par-les-operateurs-aip.html)
- [IGPDE — CMS Rossignol, demande et validation par les opérateurs RH (formation 102629)](https://catalogue.igpde.finances.gouv.fr/1903-cms-rossignol-demande-et-validation-de-cartes-agents-multiservices-par-les-operateurs-rh.html)
- [MEF — Offre de certification Rossignol](https://crl.igc1.finances.gouv.fr/rossignol.html)
- [MEF — IGC du Secrétariat général](https://crl.igc1.finances.gouv.fr/igc-sg.html)

---

# PARTIE I — Les fondamentaux techniques

# 2. Les prérequis informatiques

## 2.1. Identité, identification, authentification et autorisation

Ces quatre notions ne sont pas synonymes.

- **Identité :** ensemble d'attributs permettant de désigner une personne ou une entité.
- **Identification :** l'utilisateur annonce une identité, par exemple son nom de compte.
- **Authentification :** il apporte une preuve qu'il est bien le titulaire de cette identité.
- **Autorisation :** une application ou un service décide ce qu'il a le droit de faire.

Un agent peut avoir plusieurs identifiants : matricule RH, compte Active Directory, adresse professionnelle, UPN, identifiant de carte, numéro de terminal, identifiant interne dans un certificat.

**Exemple :** un certificat peut authentifier Sarah auprès d'un service. Celui-ci peut ensuite lui refuser une application parce qu'elle n'a pas l'habilitation correspondante. Le certificat n'est pas un « passe-partout » donnant automatiquement tous les droits.

## 2.2. Chiffrement symétrique, asymétrique et hachage

| Primitive | Principe | Exemple |
|---|---|---|
| Chiffrement symétrique | Une clé secrète sert au chiffrement et au déchiffrement | AES |
| Cryptographie asymétrique | Une clé privée et une clé publique mathématiquement liées | RSA, ECDSA, ECDH selon l'usage |
| Hachage | Calcul d'une empreinte de données | SHA-256 |

La PKI repose sur la cryptographie asymétrique, mais les systèmes sécurisés comme TLS utilisent plusieurs de ces techniques en combinaison.

## 2.3. Signature électronique et preuve cryptographique

Pour signer des données, un système utilise la clé privée du signataire. Une autre personne peut vérifier la signature à l'aide de la clé publique et du certificat associé.

La signature cryptographique donne des garanties sur l'intégrité et sur le fait que l'opération a utilisé la clé concernée. **Sa valeur juridique dépend d'autres critères** : type de signature, statut du certificat, vérification de l'identité, dispositif de signature et règles applicables.

## 2.4. Compétences Windows et réseau nécessaires

Il est utile de connaître les bases suivantes :

- Active Directory, comptes utilisateur et machine, domaine, contrôleur de domaine et GPO ;
- Kerberos, notamment PKINIT dans les scénarios d'authentification par certificat ;
- LDAP/LDAPS et référentiels d'identités ;
- DNS, HTTP, HTTPS/TLS, proxy et pare-feu ;
- magasins de certificats Windows et journaux d'événements ;
- notions de CSP, CNG, KSP, middleware et PKCS#11 ;
- protocoles d'enrôlement SCEP, EST et ACME ;
- mécanismes de révocation : CRL/LCR et OCSP.

Une panne réseau ou DNS peut provoquer un refus d'authentification qui ressemble, à première vue, à une erreur de certificat.

---

# 3. Les certificats numériques : comprendre le mécanisme

## 3.1. La paire de clés

Une identité cryptographique repose souvent sur deux éléments :

- **Clé publique :** peut être communiquée à des systèmes tiers. Elle est présente dans le certificat.
- **Clé privée :** doit rester protégée. Elle sert aux opérations cryptographiques autorisées.

**Le certificat ne contient pas la clé privée.** Il associe une identité ou une désignation à une clé publique au moyen d'une signature de l'autorité émettrice.

## 3.2. Exemple fictif de certificat X.509

| Champ | Exemple |
|---|---|
| Subject | `CN=Sarah DUPONT` |
| Issuer | `CN=AC-AGENTS-EXEMPLE` |
| Subject Public Key | Clé publique RSA ou elliptique |
| Extended Key Usage | Authentification client |
| Not Before / Not After | Dates de début et de fin de validité |
| Serial Number | Identifiant unique au sein de l'AC |
| Signature | Signature cryptographique de l'AC émettrice |

Ce certificat est **public**. La clé privée correspondante doit rester protégée sur la carte, le TPM, le token ou le téléphone, selon le mécanisme retenu.

## 3.3. Comment un certificat est utilisé pour s'authentifier

Dans un scénario classique :

1. Une application demande une authentification par certificat.
2. Le poste ou le support met à disposition un certificat compatible.
3. Une opération cryptographique est réalisée au moyen de la clé privée, éventuellement après saisie d'un PIN.
4. Le serveur vérifie la preuve à l'aide de la clé publique.
5. Il contrôle la chaîne de certification, les usages, les dates et la révocation conformément à sa politique.
6. Il associe l'identité certifiée à un compte puis vérifie les autorisations.

Les messages exacts diffèrent selon qu'il s'agit de TLS avec certificat client, de Kerberos/PKINIT ou d'un autre protocole. Il ne faut pas imaginer qu'un serveur envoie systématiquement un simple « défi » identique dans tous les scénarios.

## 3.4. Les champs X.509 à maîtriser

| Champ | Fonction |
|---|---|
| `Subject` | Identité désignée par le certificat |
| `Issuer` | Autorité de certification émettrice |
| `Serial Number` | Numéro de série du certificat |
| `Not Before / Not After` | Période de validité |
| `Subject Public Key Info` | Clé publique et algorithme |
| `Key Usage` | Usages cryptographiques autorisés |
| `Extended Key Usage (EKU)` | Usages applicatifs prévus |
| `Subject Alternative Name (SAN)` | Identités supplémentaires : DNS, UPN, e-mail, etc. |
| `Certificate Policies` | OID des politiques applicables |
| `CRL Distribution Points` | Adresses de listes de révocation |
| `Authority Information Access (AIA)` | Informations sur l'émetteur et, selon le profil, OCSP |
| `Signature Algorithm` | Algorithme de signature de l'AC |

Un **OID** (*Object Identifier*) est un identifiant numérique destiné à désigner, entre autres, un usage ou une politique de certification.

## 3.5. Chaîne de confiance

```text
Certificat de Sarah
        |
        v
AC intermédiaire
        |
        v
AC racine approuvée
```

Le vérificateur doit pouvoir construire et valider la chaîne applicable. Il doit également vérifier que le certificat est accepté pour l'usage demandé. Une chaîne techniquement valide n'implique pas qu'une application autorise automatiquement l'accès.

---

# 4. Le fonctionnement détaillé d'une IGC / PKI

## 4.1. Les composantes

| Composant | Rôle |
|---|---|
| Autorité de certification (AC/CA) | Émet et signe les certificats |
| Autorité d'enregistrement (AE/RA) | Vérifie l'identité et les conditions de délivrance |
| HSM | Protège les clés cryptographiques sensibles, notamment celles des AC |
| CMS | Orchestre le cycle de vie des supports et moyens d'authentification |
| Annuaire / IAM | Référence identités, comptes et habilitations |
| CRL/LCR | Publie les certificats révoqués |
| OCSP | Permet d'interroger le statut de révocation, lorsqu'il est utilisé |
| Dépôt de confiance | Distribue les certificats d'autorités et informations nécessaires |

**L'IGC n'est pas un serveur unique.** C'est un ensemble technique, organisationnel et procédural, incluant des responsabilités, des politiques et des moyens d'exploitation.

## 4.2. Hiérarchie de certification

```text
                  AC RACINE
            ancre de confiance
                       |
             +---------+---------+
             |                   |
    AC Authentification     AC Confidentialité
       / Signature            / Chiffrement
             |                   |
      Certificats agents   Certificats destinés
                          à la confidentialité
```

Ce schéma est un exemple ; le nombre d'AC, leur répartition et les politiques dépendent de l'infrastructure réelle.

La clé privée de l'AC racine est particulièrement sensible : sa compromission peut affecter l'ensemble de la hiérarchie correspondante. Dans une architecture sécurisée, on peut utiliser des HSM, des procédures contrôlées et une AC racine hors ligne.

## 4.3. Le processus de délivrance

1. **Demande :** une identité ou une machine est déclarée éligible.
2. **Vérification :** l'autorité d'enregistrement ou le système mandaté valide les éléments requis.
3. **Génération de clés :** le support ou un système habilité génère une paire de clés.
4. **Demande de certificat :** une CSR ou un protocole équivalent soumet la clé publique et les informations requises.
5. **Émission :** l'AC signe le certificat.
6. **Installation :** le certificat est associé à sa clé privée et rendu accessible par les interfaces autorisées.
7. **Exploitation :** le certificat est présenté à des applications ou services compatibles.
8. **Fin de vie :** renouvellement, remplacement, expiration ou révocation.

La clé privée peut être générée directement sur le support, ce qui facilite la non-exportabilité. Certaines architectures autorisent une génération centralisée et une injection sécurisée, selon les politiques.

## 4.4. Les trois usages principaux

| Usage | Ce qui est recherché |
|---|---|
| Authentification | Prouver l'identité ou la possession d'un credential |
| Signature | Garantir l'intégrité et l'origine cryptographique de données signées |
| Confidentialité | Permettre le chiffrement et le déchiffrement de données pour un destinataire |

Une même organisation peut délivrer des certificats différents pour ces usages.

## 4.5. Cycle de vie : vocabulaire précis

- **Émission :** création d'un certificat.
- **Renouvellement :** remplacement à l'approche de l'échéance, avec ou sans changement de paire de clés selon la politique.
- **Réémission :** nouvelle délivrance, par exemple après changement de support ou d'attributs.
- **Expiration :** fin de la validité temporelle.
- **Révocation :** invalidation anticipée.
- **Désactivation :** opération administrative ou technique qui peut concerner un support, un credential ou un service ; elle n'est pas toujours synonyme de révocation.
- **Déblocage :** rétablissement de l'utilisation d'un support ou de son mécanisme d'activation, par exemple un PIN bloqué.

Un certificat expiré peut rester présent sur le poste. Un certificat révoqué peut également rester présent : sa révocation est un **état de confiance**, pas nécessairement une suppression locale.

## 4.6. CRL et OCSP

Lorsqu'une carte est perdue ou compromise, l'IGC peut révoquer le certificat avant sa date d'expiration.

Un service peut vérifier cet état au moyen :

- d'une **CRL/LCR**, liste signée des certificats révoqués ;
- d'**OCSP**, protocole de consultation du statut de révocation lorsqu'il est déployé.

La disponibilité et la fraîcheur des informations de révocation sont critiques. En cas d'indisponibilité, le comportement de l'application dépend de sa politique de validation. Une infrastructure robuste doit superviser ces services.

**À retenir :** révoquer un certificat n'efface pas automatiquement sa clé privée, ne désactive pas obligatoirement un badge physique et ne ferme pas nécessairement les sessions déjà ouvertes.

---

# PARTIE II — Rossignol, CMS et supports ministériels

# 5. Rossignol : une carte agent multiservices

## 5.1. Deux familles d'usages

La documentation publique présente Rossignol comme un dispositif permettant d'articuler des fonctions physiques et numériques.

| Fonction | Technologie ou mécanisme | Exemple |
|---|---|---|
| Accès physique / services locaux | Interface sans contact, selon le support et le système | Contrôle d'accès aux locaux, autres services compatibles |
| Identité numérique | Puce cryptographique à contact et certificats | Authentification, signature, confidentialité |

Une carte multiservices peut donc réunir des usages qui ne partagent pas les mêmes secrets, les mêmes protocoles ni les mêmes gestionnaires d'habilitation.

La technologie sans contact ne doit pas être confondue avec le certificat X.509. Un droit d'entrer dans un bâtiment peut être géré par un système d'accès physique indépendant de l'IGC.

## 5.2. Authentification sur Windows avec une carte

Dans un environnement Windows compatible et configuré :

1. L'agent insère la carte dans un lecteur.
2. Windows, le pilote et le middleware identifient le support.
3. Un certificat d'authentification compatible est proposé.
4. Une authentification ou une opération cryptographique peut exiger la saisie du PIN.
5. La puce utilise la clé privée sans la divulguer.
6. Le service d'identité vérifie la preuve et associe le certificat au compte.
7. Si les politiques et habilitations le permettent, la session est ouverte.

La carte et le PIN constituent typiquement deux facteurs : possession et connaissance.

## 5.3. Authentification/signature et confidentialité

L'offre publique Rossignol expose des autorités et des politiques de certification distinctes, notamment pour :

- l'**authentification et la signature** ;
- la **confidentialité** (chiffrement/déchiffrement).

Il faut toujours vérifier les usages effectivement autorisés par les extensions du certificat et sa politique de certification.

### Les clés de confidentialité et le recouvrement

Un cas important : un agent chiffre un document puis perd sa carte.

Si la clé de déchiffrement n'est plus accessible, les informations peuvent devenir irrécupérables. Les politiques de confidentialité peuvent donc prévoir un **séquestre et un recouvrement encadré** de clés privées de déchiffrement.

Cela ne doit pas être confondu avec la gestion d'une clé de signature personnelle. La politique Rossignol qualifiée distingue les dispositions relatives à ces deux familles d'usages. Consulter sa PC pour connaître les conditions précises.

## 5.4. Générations 2022 et 2026

Le portail public Rossignol distingue notamment des générations de certificats qualifiés :

- **Génération 2022 :** documentation associée à des clés de 2 048 bits.
- **Génération 2026 :** documentation associée à des clés de 3 072 bits.

Ces valeurs concernent les offres précisément documentées ; elles ne permettent pas de généraliser à tous les certificats ministériels. Les générations de certificats peuvent coexister pendant les migrations et nécessiter une gestion coordonnée des chaînes de confiance, de la compatibilité applicative et des échéances.

La génération 2026 publie notamment les OID :

- `1.2.250.1.131.1.11.6.3.1.2` — politique d'authentification/signature qualifiée ;
- `1.2.250.1.131.1.11.7.3.1.2` — politique de confidentialité qualifiée.

[Source : portail public Rossignol](https://crl.igc1.finances.gouv.fr/rossignol.html)

---

# 6. Le CMS Rossignol et le Self-Service CMS

## 6.1. À quoi sert le CMS ?

Un **CMS** (*Card Management System* ou, selon les solutions, *Credential Management System*) gère le cycle de vie de cartes, de supports et de moyens d'authentification.

L'IGC certifie les clés publiques ; le CMS pilote ou orchestre les opérations métier nécessaires à l'attribution, à l'activation et à la gestion des moyens d'identité.

Le CMS peut, selon la solution et les rôles :

- exploiter les données administratives d'un agent ;
- enregistrer et valider une demande de carte ;
- suivre sa délivrance ;
- gérer des opérations de désactivation et de déblocage ;
- faciliter des opérations sur les certificats ;
- tenir une traçabilité des actions.

## 6.2. Les acteurs présents dans les formations IGPDE

| Rôle | Actions documentées |
|---|---|
| Opérateur RH / bureau RH de proximité | Vérifier les données, demander, valider ou rejeter une demande de carte, gérer certains remplacements de certificat |
| Opérateur AIP | Délivrer, désactiver, débloquer les cartes et accompagner les agents dans certaines opérations |
| Agent porteur | Recevoir la carte et utiliser les moyens d'authentification qui lui sont attribués |
| Équipes IGC, poste, mobilité, SSI | Interviennent en fonction de l'architecture et des responsabilités internes |

La formation RH mentionne explicitement les données liées à **Bercyprofil** et **OMEGA**, ainsi que les conséquences de certaines mobilités entraînant un changement d'adresse électronique. La signification organisationnelle exacte du sigle AIP et les périmètres de responsabilité de chaque équipe sont à confirmer dans le référentiel interne de ta direction.

## 6.3. Parcours type d'un nouvel agent

Prenons Sarah Dupont, nouvellement arrivée dans une direction des MEF :

1. **Identité RH :** ses données professionnelles sont enregistrées et vérifiées.
2. **Demande de carte :** un acteur habilité crée la demande dans le CMS.
3. **Validation :** la demande est validée ou rejetée selon les règles.
4. **Production/personnalisation :** le support est préparé et, selon le processus, ses credentials sont associés.
5. **Remise :** l'opérateur habilité remet la carte après les contrôles requis.
6. **Activation :** Sarah active les fonctionnalités et les mécanismes nécessaires.
7. **Utilisation :** elle s'en sert pour les usages autorisés.
8. **Vie du support :** une perte, une mobilité, un renouvellement ou un départ donne lieu à des actions adaptées.

Ce parcours est **pédagogique** ; les étapes et contrôles exacts doivent être confirmés dans la procédure officielle.

## 6.4. Différence CMS / Self-Service CMS

**CMS opérateur** : interface dédiée aux personnels habilités pour des opérations de gestion.

**Self-Service CMS** : interface ouverte au porteur pour certaines actions autorisées, notamment l'installation et la gestion de certificats sur supports complémentaires.

La formation IGPDE `102677` mentionne explicitement :

- l'installation de certificats sur la **puce TPM du poste de travail** via le Self-Service CMS ;
- la désactivation, le déblocage et le renouvellement dans ce parcours ;
- l'accompagnement pour des certificats sur mobiles **MOTUS** et **LICORNE**.

[Source : formation IGPDE 102677](https://catalogue.igpde.finances.gouv.fr/1952-cms-rossignol-delivrance-de-cartes-agent-multi-services-rossignol-par-les-operateurs-aip.html)

---

# 7. Les certificats stockés sur les postes avec TPM

## 7.1. Qu'est-ce que le TPM ?

Le **Trusted Platform Module** est une technologie de protection cryptographique associée au poste. Il peut notamment protéger des clés, participer à des mesures de confiance et servir à BitLocker ou à certains systèmes d'authentification.

Une distinction fondamentale :

- le **certificat public** se trouve généralement dans un magasin Windows ou est accessible à l'application ;
- la **clé privée** peut être protégée par le TPM et ne pas être exportable.

```text
Application Windows
        |
API cryptographique / CNG
        |
Microsoft Platform Crypto Provider (selon le cas)
        |
TPM : clé privée protégée

Magasin Windows : certificat X.509 public
```

Le nom du fournisseur de clés peut être un indice, mais il faut inspecter la configuration réelle pour déterminer comment une clé est protégée.

## 7.2. Enrôlement type d'un certificat TPM

1. Sarah s'identifie sur le service d'enrôlement autorisé.
2. Le CMS vérifie qu'elle est éligible.
3. Le poste génère une nouvelle paire de clés via le fournisseur cryptographique adapté.
4. La demande de certificat transmet la clé publique à l'IGC.
5. L'IGC émet un certificat.
6. Le certificat est installé dans Windows et associé à la clé privée TPM.
7. Sarah peut l'utiliser pour les applications compatibles.

Les gestes précis et les contrôles d'identité peuvent être différents dans le Self-Service CMS ministériel.

## 7.3. Que signifie « certificat dérivé » ?

Dans le contexte d'un dispositif de cartes et de supports complémentaires, le terme peut désigner **la délivrance d'un second moyen d'authentification fondé sur une identité déjà validée**.

Il ne faut pas en déduire que la clé privée de la carte est copiée sur le TPM.

```text
                 Même identité RH : Sarah
                         |
              +----------+----------+
              |                     |
     Carte Rossignol             Poste TPM
      Certificat A              Certificat B
      Clé privée A              Clé privée B
```

Ce modèle est compatible avec l'utilisation de clés non exportables propres à chaque support. Le mécanisme exact de dérivation doit être vérifié dans les procédures internes.

## 7.4. Conséquences opérationnelles

- **Changement de PC :** un certificat reposant sur une clé TPM non exportable nécessite généralement un nouvel enrôlement.
- **Réinstallation du système :** l'association clé/certificat peut être affectée ; les conséquences dépendent du stockage et des procédures.
- **Changement de carte mère ou effacement TPM :** peut rendre les clés précédentes inutilisables.
- **Certificat visible sans clé privée utilisable :** la présence du fichier public ne suffit pas pour s'authentifier.
- **PIN :** la présence d'un TPM n'implique pas à elle seule une demande de PIN à chaque opération.

Il faut également distinguer un certificat sur TPM d'une **carte à puce virtuelle basée sur TPM**, même si ces modèles peuvent être liés selon l'implémentation.

---

# 8. Cartes, tokens ypsID, pilotes et middleware

## 8.1. Où se situe le middleware ?

```text
Application (Windows, navigateur, outil de signature)
                         |
               CAPI / CNG / PKCS#11
                         |
                CSP / KSP / middleware
                         |
                 Pilote / minidriver
                         |
              Lecteur / carte / token USB
                         |
                   Clé privée protégée
```

Schéma simplifié : les différentes interfaces peuvent être alternatives ou coexister, et non former obligatoirement une seule chaîne linéaire.

## 8.2. Les notions essentielles

| Terme | Définition |
|---|---|
| PC/SC | Standard d'interaction entre les logiciels, lecteurs et cartes à puce |
| APDU | Unité de message échangée avec une carte à puce |
| PKCS#11 | API permettant d'accéder aux fonctions d'un module cryptographique |
| CSP | Fournisseur de services cryptographiques historique Windows |
| CNG | Architecture cryptographique Windows plus récente |
| KSP | Fournisseur de gestion et d'utilisation des clés dans CNG |
| Minidriver | Composant exposant les fonctionnalités d'une carte aux couches Windows |
| PIN | Secret ou mécanisme d'autorisation d'utilisation d'un support |
| PUK | Mécanisme éventuel de déblocage, selon le support |

Le middleware n'est pas une AC. Il permet à des logiciels d'utiliser le matériel et les clés qui y sont protégées.

## 8.3. Le cas ypsID

**ypsID** désigne historiquement une famille de cartes/tokens cryptographiques et de composants logiciels associés à Morpho/Sagem Orga. Des documents publics anciens mentionnent un middleware ypsID et un outil d'administration tel que Morpho Launcher.

Dans ce type d'environnement :

- la **clé USB/token** protège les clés ;
- le **middleware** les expose aux logiciels compatibles ;
- l'**outil de gestion** facilite certaines opérations locales, selon sa version et les droits ;
- l'**IGC** délivre ou valide les certificats selon son périmètre.

Il faut vérifier la référence exacte du matériel et la version installée dans ton service avant de déduire les fonctions effectivement disponibles. Une documentation historique n'est pas une preuve d'un déploiement actuel.

## 8.4. Pourquoi le navigateur peut poser problème

Un certificat peut être visible dans le magasin Windows mais inaccessible à une application qui utilise une autre interface cryptographique.

Pour diagnostiquer :

1. Le lecteur ou le token est-il détecté ?
2. Le certificat est-il visible dans la bonne application ?
3. Le middleware et le provider sont-ils présents et compatibles ?
4. La clé privée est-elle utilisable ?
5. Le certificat possède-t-il les usages attendus ?
6. Le navigateur sélectionne-t-il le bon certificat ?
7. Le serveur accepte-t-il la chaîne et l'identité ?

[Microsoft Learn — Architecture des cartes à puce](https://learn.microsoft.com/fr-fr/windows/security/identity-protection/smart-cards/smart-card-architecture)

---

# 9. Les certificats sur les mobiles MOTUS et LICORNE

## 9.1. Ce qui est confirmé

La formation IGPDE des opérateurs AIP mentionne l'accompagnement de l'installation de certificats sur des mobiles désignés **MOTUS** et **LICORNE** par le Self-Service CMS.

La documentation publique consultée **ne permet pas d'affirmer** quel MDM, quel système d'exploitation, quel protocole d'enrôlement, quelle application ou quel composant de stockage sécurisé est précisément utilisé pour chacun.

## 9.2. Modèle général d'enrôlement mobile

Dans une architecture d'entreprise, un scénario possible est :

1. Le terminal est préparé et associé à une identité dans un système de gestion.
2. Le service d'enrôlement vérifie l'éligibilité de l'utilisateur et de l'appareil.
3. Une paire de clés est créée sur le téléphone ou par un mécanisme approuvé.
4. Une demande de certification est transmise à l'IGC.
5. L'IGC délivre un certificat.
6. Le téléphone l'utilise pour une application, le Wi-Fi, un VPN ou un service interne.
7. Le renouvellement ou le retrait s'effectue conformément à la politique de l'organisation.

Selon les plateformes et la configuration, les clés peuvent bénéficier de mécanismes sécurisés tels que le Keystore Android, StrongBox ou des protections propres à Apple. **Toutes les clés mobiles ne sont pas automatiquement protégées matériellement.**

## 9.3. Les questions à poser en interne

- Quelle est la nature fonctionnelle de MOTUS et de LICORNE ?
- Quel système d'exploitation et quelle gamme de terminaux sont utilisés ?
- Le certificat est-il personnel ou associé au terminal ?
- Quelle est la solution de gestion mobile ?
- Le certificat est-il enrôlé via SCEP, ACME, un portail propriétaire ou un autre mécanisme ?
- Où réside exactement la clé privée ?
- Le porteur peut-il supprimer le certificat ?
- Quelles actions sont déclenchées en cas de perte ou de remplacement du téléphone ?
- La révocation est-elle synchronisée avec le départ ou la désactivation de l'agent ?

---

# 10. Les certificats et l'authentification aux services

## 10.1. Windows et Kerberos/PKINIT

Dans un environnement Active Directory utilisant une connexion par carte à puce :

```text
Carte et PIN
      |
Preuve de possession de la clé privée
      |
Contrôleur de domaine / Kerberos PKINIT
      |
Validation de la chaîne, usages, état et identité
      |
Association certificat <-> compte AD
      |
Ouverture de session si les contrôles réussissent
```

L'association entre le certificat et le compte est appelée **certificate mapping**.

Un certificat peut être parfaitement valide mais refusé parce que le domaine ne peut pas l'associer de manière sûre au compte correspondant.

### Liaison forte des certificats

Microsoft a renforcé cette association avec les changements associés à **KB5014754**. La mise en conformité renforcée est devenue la norme à partir des mises à jour de février 2025, et l'ancien mécanisme permettant le retour au mode de compatibilité a cessé d'être pris en charge avec les mises à jour de septembre 2025.

Dans le diagnostic, il faut examiner la configuration des mappings forts, les attributs et extensions applicables, ainsi que les journaux KDC ; l'UPN seul ne constitue pas nécessairement une preuve de liaison suffisante.

**Ne pas affaiblir la liaison des certificats pour contourner un incident.**

[Microsoft Support — KB5014754](https://support.microsoft.com/fr-fr/servicing/os/windows-server/2022/05/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers)

## 10.2. Applications web en mTLS

Dans une authentification TLS par certificat client :

1. Le navigateur établit une connexion TLS.
2. Le serveur demande un certificat client.
3. Le client choisit un certificat compatible.
4. Le support utilise la clé privée pour participer à la preuve cryptographique prévue par TLS.
5. Le serveur contrôle le certificat et la preuve.
6. L'application associe l'identité à un compte, puis vérifie les habilitations.

Selon l'architecture, un proxy, une passerelle d'identité ou un service SSO peut réaliser la première authentification. L'application finale peut ne jamais communiquer directement avec la carte.

## 10.3. Wi-Fi et EAP-TLS

Un certificat peut servir à authentifier un poste ou un utilisateur auprès d'une infrastructure Wi-Fi d'entreprise.

Un service RADIUS/NPS ou équivalent vérifie le certificat selon une politique réseau. Il faut distinguer certificat utilisateur et certificat machine : ils peuvent être utilisés à des étapes différentes et correspondre à des identités différentes.

## 10.4. VPN et applications métier

Un certificat peut être exigé pour établir un tunnel VPN ou accéder à une application interne. Il peut s'ajouter à d'autres contrôles : conformité du poste, politique d'accès conditionnel, second facteur, appartenance à un groupe ou validation des habilitations.

---

# PARTIE III — Exploitation, incidents et diagnostic

# 11. Les processus métiers à connaître

| Événement | Points de contrôle |
|---|---|
| Arrivée d'un agent | Identité, demande CMS, validation, remise, activation |
| Attribution d'un poste | Certificat TPM, provider, identité et accès aux applications |
| Attribution d'un téléphone | Enrôlement, stockage de la clé, MDM et accès aux services |
| Mobilité | Changement d'attributs, adresse e-mail, droits et certificats concernés |
| PIN bloqué | Procédure de déblocage prévue pour le support |
| Perte ou vol d'une carte | Accès physique, déclaration, révocation, remplacement |
| Changement de PC | Nouvelle paire de clés TPM et nouvel enrôlement si nécessaire |
| Départ d'un agent | Révocation ou retrait selon politique, désactivation des accès, traçabilité |

## 11.1. Cas pratique : carte Rossignol perdue

Le traitement doit distinguer les dimensions suivantes :

1. Signalement et vérification de l'identité du déclarant.
2. Traitement de l'accès physique aux bâtiments.
3. Révocation des certificats concernés, selon la procédure.
4. Évaluation des credentials complémentaires (TPM, mobile, autre carte).
5. Remplacement du support et contrôle de sa remise.
6. Traçabilité et éventuelle notification SSI.

La perte d'une carte ne signifie pas automatiquement que tous les certificats détenus par l'agent sur d'autres supports sont révoqués.

## 11.2. Cas pratique : mobilité administrative

Un changement de direction ou d'adresse professionnelle peut rendre des données du certificat obsolètes.

Il faut vérifier : les attributs affectés, les conditions de remplacement, l'identité de référence, le caractère nécessaire ou non d'une nouvelle paire de clés, et le moment où l'ancien certificat doit cesser d'être accepté.

La formation RH IGPDE mentionne explicitement les processus de remplacement de certificat après certaines mobilités administratives.

## 11.3. Cas pratique : changement de PC

Une clé privée TPM non exportable n'est normalement pas transférable vers un autre poste.

La procédure de prise de poste doit donc organiser le nouvel enrôlement, le contrôle de la bonne association clé/certificat, la vérification des accès et le traitement de l'ancien credential.

## 11.4. Cas pratique : certificat présent mais inutilisable

Ne pas se limiter à regarder la date de validité.

Le problème peut venir : du magasin Windows, du provider, de la clé privée, du PIN, du TPM, du middleware, de la chaîne de confiance, du contrôle de révocation, du certificate mapping ou des habilitations applicatives.

---

# 12. Méthode de diagnostic

## 12.1. Arbre de triage

```text
1. Le support est-il détecté ?
   NON -> lecteur / pilote / USB / TPM / middleware / carte
   OUI ->

2. Le certificat est-il visible et sélectionnable ?
   NON -> magasin / enrôlement / profil / application
   OUI ->

3. La clé privée est-elle accessible ?
   NON -> PIN / provider / droits / TPM / conteneur de clés
   OUI ->

4. La chaîne et les usages sont-ils valides ?
   NON -> AC / dates / EKU / révocation / DNS / CRL / OCSP
   OUI ->

5. L'identité est-elle correctement associée ?
   NON -> mapping / annuaire / KDC / SSO / fédération
   OUI ->

6. L'autorisation applicative est-elle accordée ?
   NON -> habilitations / politiques d'accès / groupes
   OUI -> examiner les autres dépendances du service
```

Ce triage est pédagogique et certaines vérifications peuvent être conduites en parallèle.

## 12.2. Tableau de symptômes

| Symptôme | Pistes principales |
|---|---|
| Carte non reconnue | Lecteur, câble, pilote, service Windows, middleware, carte |
| Certificat introuvable | Magasin, profil, enrôlement, sélection, middleware |
| PIN refusé | Mauvais PIN, verrouillage, support ou interface incompatibles |
| Clé privée inaccessible | Provider, autorisations, TPM, support, conteneur de clé |
| Chaîne non fiable | Racine/intermédiaire, politique, certificat non approuvé |
| Certificat révoqué | Statut de révocation et certificat effectivement sélectionné |
| Échec contrôle de révocation | CRL/OCSP, DNS, pare-feu, proxy, disponibilité |
| Ouverture Windows refusée | Mapping fort, compte AD, KDC, usages, politiques |
| Application refusée | Habilitations, SSO, règles applicatives, identité inattendue |
| Mobile non enrôlé | Gestion mobile, protocole, politique, réseau, application |

## 12.3. Réflexes du support

Avant toute action :

- relever l'heure exacte, le poste et l'application affectés ;
- recueillir le message d'erreur sans exposer de secrets ;
- identifier si l'incident est individuel ou généralisé ;
- rechercher les changements récents (certificat, poste, middleware, politique, réseau) ;
- déterminer l'étape de la chaîne qui échoue ;
- consulter les journaux adaptés et escalader à la bonne équipe ;
- documenter le diagnostic et l'action autorisée.

---

# 13. Outils Windows à maîtriser

## 13.1. Consoles graphiques

| Outil | Fonction |
|---|---|
| `certmgr.msc` | Magasins de certificats de l'utilisateur |
| `certlm.msc` | Magasins de certificats de l'ordinateur |
| `tpm.msc` | Informations sur le TPM |
| `eventvwr.msc` | Journaux d'événements |
| `mmc.exe` | Console d'administration modulaire |
| `services.msc` | État des services Windows |

## 13.2. Commandes d'observation

**Lister les certificats personnels de l'utilisateur :**

```powershell
Get-ChildItem Cert:\CurrentUser\My |
  Select-Object Subject, Issuer, NotAfter, Thumbprint
```

**Lister les certificats personnels de la machine :**

```powershell
Get-ChildItem Cert:\LocalMachine\My |
  Select-Object Subject, Issuer, NotAfter, Thumbprint
```

**Afficher les détails du magasin utilisateur :**

```powershell
certutil -user -store My
```

**Consulter les informations d'une carte à puce connectée :**

```powershell
certutil -scinfo
```

**Consulter l'état général du TPM :**

```powershell
Get-Tpm
```

Ces commandes sont destinées à un poste où tu es autorisé à réaliser le diagnostic. `Get-Tpm` ne suffit pas à prouver qu'une clé particulière est protégée par le TPM.

**Sécurité opérationnelle :** ne supprime pas de certificat, n'efface pas de TPM, ne manipule pas de clé privée et n'altère pas la configuration de confiance sans procédure et habilitation adaptées. Ne transmets pas de données internes sensibles ou nominatives à des services externes non autorisés.

## 13.3. Journaux utiles

Selon les besoins et les droits :

- journaux **CAPI2** pour certaines opérations de vérification cryptographique ;
- journaux **Smart Card** pour la détection et les problèmes de carte ;
- journaux **Kerberos / KDC** pour les refus de connexion et les mappings ;
- journaux **Sécurité Windows** pour les événements d'authentification ;
- journaux des applications, passerelles, serveurs ou composants IGC concernés.

---

# PARTIE IV — Sécurité, conformité et approfondissements

# 14. Les technologies à ne pas confondre

| Technologie | Rôle principal |
|---|---|
| Certificat X.509 | Lie une clé publique à une identité certifiée |
| TPM | Protège des clés et fournit des fonctions de confiance matérielle |
| BitLocker | Chiffre des volumes de stockage |
| Windows Hello for Business | Authentifie un utilisateur avec des credentials liés au poste, selon plusieurs modèles |
| FIDO2 / WebAuthn | Authentification par clés asymétriques résistante au phishing |
| Carte à puce | Support cryptographique sécurisé |
| HSM | Protection et usage de clés sensibles, notamment d'autorités de certification |

BitLocker peut utiliser le TPM sans recourir à un certificat personnel Rossignol. Windows Hello for Business peut utiliser des clés protégées matériellement sans imposer systématiquement un certificat X.509 utilisateur. FIDO2 et certificat X.509 sont deux modèles distincts, même si tous deux peuvent employer la cryptographie asymétrique.

# 15. RGS, eIDAS, PC et DPC

## 15.1. RGS

Le **Référentiel Général de Sécurité (RGS)** définit un cadre de sécurité pour les échanges électroniques des autorités administratives. Ses niveaux historiques doivent être replacés dans le contexte précis des exigences applicables.

## 15.2. eIDAS

Le règlement européen **eIDAS** encadre l'identification électronique et les services de confiance. Il faut distinguer :

- signature électronique simple ;
- signature électronique avancée ;
- signature électronique qualifiée.

Une signature qualifiée ne résulte pas automatiquement de l'utilisation d'un certificat présenté comme « qualifié » : la conformité du dispositif et du processus de signature compte également.

## 15.3. Politique de Certification et Déclaration des Pratiques

- **PC — Politique de Certification :** obligations, usages, identification, durées, révocation, protection des clés, responsabilités.
- **DPC — Déclaration des Pratiques de Certification :** modalités concrètes de mise en œuvre des exigences.

Une PC répond notamment à ces questions :

1. Qui peut recevoir ce certificat ?
2. Quels usages sont autorisés ?
3. Comment l'identité du titulaire est-elle vérifiée ?
4. Où peut se trouver la clé privée et peut-elle être exportée ?
5. Quelle est la durée de validité ?
6. Comment se déroule la révocation ?
7. Existe-t-il un mécanisme de séquestre/recouvrement pour le chiffrement ?
8. Qui répond de quelle opération ?

## 15.4. Les risques de sécurité majeurs

- compromission d'une clé d'AC ;
- délivrance frauduleuse ;
- mauvaise identification d'un porteur ;
- défaillance de publication des informations de révocation ;
- mauvaise configuration des usages ou des chaînes de confiance ;
- stockage inapproprié de clés exportables ;
- absence de séparation des rôles ;
- erreurs de désactivation lors des mobilités et départs ;
- défaut de supervision ou d'inventaire.

L'ANSSI a publié en août 2025 les **Essentiels — Infrastructure de gestion de clés**, ressource recommandée pour compléter ce guide.

[ANSSI — Les Essentiels : IGC](https://messervices.cyber.gouv.fr/guides/infrastructure-de-gestion-de-cles-igc)

---

# 16. Les sujets avancés à approfondir

| Domaine | Pourquoi l'apprendre ? |
|---|---|
| PKI hiérarchique et politiques de certificats | Comprendre les chaînes de confiance et les limites d'usage |
| HSM | Comprendre la protection des clés d'AC |
| Kerberos/PKINIT | Dépanner l'ouverture de session par certificat |
| Strong certificate mapping | Résoudre les rejets AD sans réduire la sécurité |
| mTLS | Comprendre l'authentification web avec certificat client |
| SCEP / EST / ACME | Comprendre la délivrance automatisée |
| PKCS#11, CSP, KSP, minidrivers | Comprendre les interactions entre logiciels et supports |
| MDM / EMM / UEM | Comprendre l'enrôlement et la gestion des mobiles |
| Fédération / SSO / IAM | Comprendre le lien entre identité certifiée et applications |
| CRL / OCSP / supervision | Comprendre la disponibilité et la révocation |
| Migration de PKI | Anticiper la coexistence de générations de certificats |
| PKCS#12, PEM, DER | Comprendre les formats et leurs implications |
| Gestion des changements | Éviter les interruptions lors des renouvellements et migrations |

---

# PARTIE V — Programme de prise de poste

# 17. Programme de progression sur 30 jours

## Semaine 1 — Fondations

- [ ] Expliquer la différence entre certificat, clé publique et clé privée.
- [ ] Décrire le rôle d'une AC, d'une AE, d'un HSM et d'un CMS.
- [ ] Comprendre les chaînes de confiance et les contrôles de révocation.
- [ ] Explorer les magasins de certificats Windows sur un environnement autorisé.
- [ ] Lire les portails publics IGC-SG et Rossignol.

## Semaine 2 — Rossignol et CMS

- [ ] Comprendre le parcours RH → demande CMS → validation → remise.
- [ ] Identifier les rôles des opérateurs RH et AIP.
- [ ] Observer une délivrance ou un renouvellement avec un référent.
- [ ] Étudier la différence entre authentification/signature et confidentialité.
- [ ] Lire une politique de certification Rossignol.

## Semaine 3 — TPM, mobiles et authentification

- [ ] Suivre un enrôlement TPM dans un environnement de test habilité.
- [ ] Comprendre CSP/KSP, CNG, middleware et PKCS#11.
- [ ] Observer un enrôlement MOTUS ou LICORNE.
- [ ] Comprendre Kerberos/PKINIT, mTLS et certificate mapping.
- [ ] Étudier les conséquences d'un changement de poste ou de terminal.

## Semaine 4 — Exploitation

- [ ] Documenter les principales procédures et acteurs responsables.
- [ ] Assister au traitement de plusieurs incidents.
- [ ] Savoir distinguer blocage, désactivation, expiration et révocation.
- [ ] Construire une fiche de diagnostic réutilisable.
- [ ] Réaliser une cartographie de ton périmètre et des dépendances techniques.

---

# 18. Les documents à demander dès l'arrivée

| Document interne | Objectif |
|---|---|
| Cartographie applicative Rossignol | Comprendre les interfaces entre outils |
| Architecture IGC/CMS | Identifier les composants et les flux |
| Matrice des rôles et habilitations | Savoir qui peut agir sur quoi |
| Procédure de délivrance | Connaître les contrôles de remise |
| Procédure de révocation | Réagir en cas de perte, vol ou compromission |
| Guide Self-Service CMS | Maîtriser le parcours utilisateur |
| Guide TPM | Connaître l'enrôlement, le renouvellement et le remplacement |
| Guides MOTUS/LICORNE | Connaître les procédures mobiles effectives |
| Référentiel des certificats | Associer AC, certificats, OID et usages |
| Guide de support et d'escalade | Identifier les équipes responsables |
| Supervision / inventaire | Comprendre les alertes et dépendances critiques |

## 18.1. Dix questions à poser à ton équipe

1. Quelles IGC sont actuellement utilisées et sur quels périmètres ?
2. Quels certificats relèvent de Rossignol et quels certificats relèvent de l'IGC-SG ?
3. Quel est le lien exact entre CMS, Self-Service CMS et autorités de certification ?
4. Comment les certificats TPM sont-ils générés, renouvelés et révoqués ?
5. Quelles sont les différences techniques entre MOTUS et LICORNE ?
6. Quels matériels, middlewares et gestionnaires de clés sont installés ?
7. Quelles applications consomment des certificats, et selon quels protocoles ?
8. Quelles actions sont automatisées lorsqu'une carte est désactivée ou révoquée ?
9. Quels incidents reviennent le plus souvent et comment sont-ils escaladés ?
10. Quelles migrations de certificats, d'AC ou de supports sont en cours ou prévues ?

---

# 19. Les ressources documentaires prioritaires

1. **IGPDE — Opérateurs AIP, CMS, TPM et mobiles** : [formation 102677](https://catalogue.igpde.finances.gouv.fr/1952-cms-rossignol-delivrance-de-cartes-agent-multi-services-rossignol-par-les-operateurs-aip.html).
2. **IGPDE — Opérateurs RH** : [formation 102629](https://catalogue.igpde.finances.gouv.fr/1903-cms-rossignol-demande-et-validation-de-cartes-agents-multiservices-par-les-operateurs-rh.html).
3. **MEF — Offre de certification Rossignol** : [politiques et chaînes de confiance](https://crl.igc1.finances.gouv.fr/rossignol.html).
4. **MEF — IGC du Secrétariat général** : [certificats agents, prestataires, serveurs et services](https://crl.igc1.finances.gouv.fr/igc-sg.html).
5. **ANSSI — Les Essentiels : IGC** : [guide de sécurité des PKI](https://messervices.cyber.gouv.fr/guides/infrastructure-de-gestion-de-cles-igc).
6. **Microsoft Learn — Architecture des cartes à puce** : [CSP, KSP, minidrivers](https://learn.microsoft.com/fr-fr/windows/security/identity-protection/smart-cards/smart-card-architecture).
7. **Microsoft Support — KB5014754** : [liaison forte des certificats et Active Directory](https://support.microsoft.com/fr-fr/servicing/os/windows-server/2022/05/kb5014754-certificate-based-authentication-changes-on-windows-domain-controllers).

---

# 20. Quiz de validation des acquis

**Question 1.** Un certificat est présent sur un nouveau PC mais sa clé privée était protégée par le TPM non exportable de l'ancien. Que faut-il généralement faire ?

A. Copier seulement le certificat public.  
B. Procéder à un nouvel enrôlement.  
C. Réinstaller l'AC racine.

**Question 2.** La révocation du certificat d'une carte Rossignol perdue désactive-t-elle automatiquement le badge d'accès physique ?

A. Oui, nécessairement.  
B. Non, les systèmes physiques et cryptographiques doivent être distingués.  
C. Seulement lorsque Windows est démarré.

**Question 3.** Un certificat est valide mais l'ouverture de session Windows est refusée. Quelle piste est importante ?

A. Le certificate mapping sur le contrôleur de domaine.  
B. La taille de l'écran.  
C. Le logiciel de traitement de texte.

**Question 4.** Le CMS et l'IGC remplissent-ils exactement le même rôle ?

A. Oui.  
B. Non, le CMS gère les processus et supports ; l'IGC certifie les clés publiques.  
C. Le CMS est uniquement un antivirus.

**Question 5.** Pourquoi peut-on prévoir le séquestre de clés de confidentialité ?

A. Pour permettre à tout le monde de signer à la place d'un agent.  
B. Pour permettre un recouvrement encadré de données chiffrées.  
C. Pour supprimer les certificats expirés.

### Corrigé

1. **B** — Le certificat public ne remplace pas la clé privée non exportable.
2. **B** — Les usages physiques et numériques peuvent être gérés indépendamment.
3. **A** — La liaison du certificat au compte AD doit être valide et suffisamment forte.
4. **B** — Le CMS orchestre la gestion ; l'IGC établit la confiance cryptographique.
5. **B** — Le recouvrement des clés de déchiffrement répond à des besoins de continuité encadrés.

---

# 21. Glossaire

| Sigle / terme | Définition |
|---|---|
| IGC / PKI | Infrastructure de gestion de clés / Public Key Infrastructure |
| AC / CA | Autorité de certification / Certificate Authority |
| AE / RA | Autorité d'enregistrement / Registration Authority |
| CMS | Card/Credential Management System selon le contexte |
| HSM | Hardware Security Module |
| TPM | Trusted Platform Module |
| X.509 | Standard de certificats à clés publiques |
| CSR | Certificate Signing Request |
| CRL / LCR | Certificate Revocation List / Liste de certificats révoqués |
| OCSP | Online Certificate Status Protocol |
| CSP / KSP | Fournisseurs de services cryptographiques Microsoft |
| CNG | Cryptography Next Generation |
| PKCS#11 | Interface standard d'utilisation d'un module cryptographique |
| PKCS#12 | Format de conteneur pour certificats et clés |
| EKU | Extended Key Usage |
| OID | Object Identifier |
| SAN | Subject Alternative Name |
| UPN | User Principal Name |
| PKINIT | Public Key Cryptography for Initial Authentication in Kerberos |
| MDM | Mobile Device Management |
| RGS | Référentiel Général de Sécurité |
| eIDAS | Règlement européen sur l'identification électronique et les services de confiance |
| PC | Politique de Certification |
| DPC | Déclaration des Pratiques de Certification |
| SSO | Single Sign-On, authentification unique |
| IAM | Identity and Access Management |
| EAP-TLS | Authentification réseau EAP fondée sur TLS et les certificats |

---

# 22. Quel niveau de maîtrise viser ?

### Niveau 1 — Compréhension

Savoir expliquer la PKI, les paires de clés, les certificats, le CMS, la carte Rossignol, le TPM et les usages mobiles, sans confondre identité, authentification et autorisation.

### Niveau 2 — Exploitation

Savoir suivre une demande, identifier les rôles, consulter un certificat, qualifier un incident, comprendre les procédures de renouvellement et orienter le traitement vers l'équipe adaptée.

### Niveau 3 — Expertise

Comprendre l'architecture des IGC, les politiques de certification, les mappings Active Directory, les protocoles, les providers cryptographiques, la supervision, les migrations et les risques de sécurité.

## Les quatre questions à poser devant tout certificat

1. **Qui certifie l'identité ?** → L'IGC et sa chaîne de certification.
2. **Qui détient et protège la clé privée ?** → Carte, TPM, token, mobile ou autre mécanisme.
3. **Quel logiciel permet de l'utiliser ?** → Windows, CSP/KSP, middleware, navigateur ou application.
4. **Quel service décide d'autoriser l'accès ?** → Contrôleur de domaine, IAM, VPN, application, politiques de sécurité.

**Conclusion.** La compétence qui fait la différence est la vision de bout en bout : identité administrative → validation métier → CMS → certification IGC → support cryptographique → preuve d'authentification → habilitation applicative → exploitation et révocation. En reconstituant cette chaîne pour un cas concret observé en environnement autorisé, tu peux passer des définitions théoriques à une compréhension directement utile au poste.
