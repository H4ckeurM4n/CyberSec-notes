# Maintien en Condition de Sécurité (MCS)
## Connaître, décider, corriger, maintenir, prouver et financer la sécurité dans la durée

**Document intégral — 7 parties, 40 chapitres, 3 cas de synthèse, 12 annexes**
*Version 1.1 · données vérifiées au 30 juillet 2026*

---

## Table des matières

- [En-tête de maintenance](#en-tête-de-maintenance)
- [Matrice de parcours par profil](#matrice-de-parcours-par-profil)
  - [Comment lire les blocs de ce cours](#comment-lire-les-blocs-de-ce-cours)
- [PARTIE I — Fondations, socle technique et maintenabilité](#partie-i--fondations-socle-technique-et-maintenabilité)
  - [Chapitre 1 — Ce qu'est réellement le MCS](#chapitre-1--ce-quest-réellement-le-mcs)
  - [Chapitre 2 — Socle technique 1 : systèmes, paquets, cycles de support, réseau, identité](#chapitre-2--socle-technique-1--systèmes-paquets-cycles-de-support-réseau-identité)
  - [Chapitre 3 — Socle technique 2 : virtualisation, conteneurs, cloud, IaC, OT et micrologiciels](#chapitre-3--socle-technique-2--virtualisation-conteneurs-cloud-iac-ot-et-micrologiciels)
  - [Chapitre 4 — Socle vulnérabilités : identifiants, scores, écosystème](#chapitre-4--socle-vulnérabilités--identifiants-scores-écosystème)
  - [Chapitre 5 — Socle processus : changement, risque, propriété, normes, preuve](#chapitre-5--socle-processus--changement-risque-propriété-normes-preuve)
  - [Chapitre 6 — Architecture maintenable : le MCS *by design*](#chapitre-6--architecture-maintenable--le-mcs-by-design)
- [PARTIE II — Cadre, périmètre et gouvernance](#partie-ii--cadre-périmètre-et-gouvernance)
  - [Chapitre 7 — Doctrine et politique MCS](#chapitre-7--doctrine-et-politique-mcs)
  - [Chapitre 8 — Cadre réglementaire et normatif applicable](#chapitre-8--cadre-réglementaire-et-normatif-applicable)
  - [Chapitre 9 — Gouvernance, rôles et comitologie](#chapitre-9--gouvernance-rôles-et-comitologie)
  - [Chapitre 10 — Inventaire et cartographie](#chapitre-10--inventaire-et-cartographie)
  - [Chapitre 11 — Exposition et chemins d'attaque](#chapitre-11--exposition-et-chemins-dattaque)
  - [Chapitre 12 — Cycle de vie, obsolescence et dette technique](#chapitre-12--cycle-de-vie-obsolescence-et-dette-technique)
  - [Chapitre 13 — MCS délégué : infogérance, prestataires, éditeurs](#chapitre-13--mcs-délégué--infogérance-prestataires-éditeurs)
- [PARTIE III — Le cœur opérationnel](#partie-iii--le-cœur-opérationnel)
  - [Chapitre 14 — Veille et sources de constats](#chapitre-14--veille-et-sources-de-constats)
  - [Chapitre 15 — Détection technique de l'exposition](#chapitre-15--détection-technique-de-lexposition)
  - [Chapitre 16 — Triage et priorisation défendables](#chapitre-16--triage-et-priorisation-défendables)
  - [Chapitre 17 — Workflow de remédiation et gestion du *backlog*](#chapitre-17--workflow-de-remédiation-et-gestion-du-backlog)
  - [Chapitre 18 — Le processus de correctif de bout en bout](#chapitre-18--le-processus-de-correctif-de-bout-en-bout)
  - [Chapitre 19 — Outillage de déploiement par plateforme](#chapitre-19--outillage-de-déploiement-par-plateforme)
  - [Chapitre 20 — Quand on ne peut pas patcher : les mesures compensatoires](#chapitre-20--quand-on-ne-peut-pas-patcher--les-mesures-compensatoires)
  - [Chapitre 21 — Crise vulnérabilité : la cinétique 24 h / 72 h / 30 j](#chapitre-21--crise-vulnérabilité--la-cinétique-24-h--72-h--30-j)
- [PARTIE IV — Configuration, dépendances et couches oubliées](#partie-iv--configuration-dépendances-et-couches-oubliées)
  - [Chapitre 22 — Durcissement et référentiels de configuration](#chapitre-22--durcissement-et-référentiels-de-configuration)
  - [Chapitre 23 — Dérive de configuration, IaC et immutabilité](#chapitre-23--dérive-de-configuration-iac-et-immutabilité)
  - [Chapitre 24 — Identités, secrets et cryptographie](#chapitre-24--identités-secrets-et-cryptographie)
  - [Chapitre 25 — MCS des applications, de la chaîne logicielle et des dépendances](#chapitre-25--mcs-des-applications-de-la-chaîne-logicielle-et-des-dépendances)
  - [Chapitre 26 — Bases de données, middlewares et *runtimes*](#chapitre-26--bases-de-données-middlewares-et-runtimes)
  - [Chapitre 27 — Couches basses et périphéries](#chapitre-27--couches-basses-et-périphéries)
  - [Chapitre 28 — Environnements non productifs et actifs d'administration](#chapitre-28--environnements-non-productifs-et-actifs-dadministration)
- [PARTIE V — Contextes spécialisés](#partie-v--contextes-spécialisés)
  - [Chapitre 29 — MCS en environnement industriel (OT / ICS)](#chapitre-29--mcs-en-environnement-industriel-ot--ics)
  - [Chapitre 30 — MCS du cloud : infrastructure, plateforme et services managés](#chapitre-30--mcs-du-cloud--infrastructure-plateforme-et-services-managés)
  - [Chapitre 31 — MCS des services en ligne, extensions et intégrations](#chapitre-31--mcs-des-services-en-ligne-extensions-et-intégrations)
  - [Chapitre 32 — Systèmes contraints, legacy et sanctuarisation](#chapitre-32--systèmes-contraints-legacy-et-sanctuarisation)
  - [Chapitre 33 — MCS côté produit : PSIRT, divulgation coordonnée et obligations réglementaires](#chapitre-33--mcs-côté-produit--psirt-divulgation-coordonnée-et-obligations-réglementaires)
  - [Chapitre 34 — MCS des outils de sécurité, du contenu de détection et des sauvegardes](#chapitre-34--mcs-des-outils-de-sécurité-du-contenu-de-détection-et-des-sauvegardes)
- [PARTIE VI — Fin de vie, industrialisation et soutenabilité](#partie-vi--fin-de-vie-industrialisation-et-soutenabilité)
  - [Chapitre 35 — Décommissionnement sécurisé](#chapitre-35--décommissionnement-sécurisé)
  - [Chapitre 36 — Automatisation, orchestration et limites](#chapitre-36--automatisation-orchestration-et-limites)
  - [Chapitre 37 — Économie du MCS, charge de travail et facteur humain](#chapitre-37--économie-du-mcs-charge-de-travail-et-facteur-humain)
  - [Chapitre 38 — Indicateurs, tableaux de bord et maturité](#chapitre-38--indicateurs-tableaux-de-bord-et-maturité)
  - [Chapitre 39 — Audit, contrôle et production de preuve](#chapitre-39--audit-contrôle-et-production-de-preuve)
- [PARTIE VII — Mise en œuvre](#partie-vii--mise-en-œuvre)
  - [Chapitre 40 — Construire un programme MCS de zéro à douze mois](#chapitre-40--construire-un-programme-mcs-de-zéro-à-douze-mois)
- [Cas de synthèse](#cas-de-synthèse)
  - [Cas de synthèse A — 0-day activement exploitée sur la passerelle d'accès distant](#cas-de-synthèse-a--0-day-activement-exploitée-sur-la-passerelle-daccès-distant)
  - [Cas de synthèse B — Sortie d'obsolescence sous contrainte et préparation d'un contrôle](#cas-de-synthèse-b--sortie-dobsolescence-sous-contrainte-et-préparation-dun-contrôle)
  - [Cas de synthèse C — Le correctif urgent qui casse la production](#cas-de-synthèse-c--le-correctif-urgent-qui-casse-la-production)
- [ANNEXES](#annexes)
  - [Plan d'accès — trouver la bonne annexe en dix secondes](#plan-daccès--trouver-la-bonne-annexe-en-dix-secondes)
- [Annexe A — Glossaire](#annexe-a--glossaire)
- [Annexe B — Cheat sheets par plateforme](#annexe-b--cheat-sheets-par-plateforme)
  - [B.1 Windows](#b1-windows)
  - [B.2 Linux — famille Debian](#b2-linux--famille-debian)
  - [B.3 Linux — famille RHEL](#b3-linux--famille-rhel)
  - [B.4 macOS et mobiles](#b4-macos-et-mobiles)
  - [B.5 Conteneurs et orchestration](#b5-conteneurs-et-orchestration)
  - [B.6 Réseau et sécurité](#b6-réseau-et-sécurité)
  - [B.7 Hyperviseurs et plans de gestion](#b7-hyperviseurs-et-plans-de-gestion)
  - [B.8 Cloud](#b8-cloud)
  - [B.9 Services en ligne](#b9-services-en-ligne)
  - [B.10 Industriel](#b10-industriel)
  - [B.11 Bases de données, middlewares et *runtimes*](#b11-bases-de-données-middlewares-et-runtimes)
  - [B.12 Applications tierces du poste](#b12-applications-tierces-du-poste)
- [Annexe C — Matrices de priorisation et de délais](#annexe-c--matrices-de-priorisation-et-de-délais)
  - [C.1 Comparatif des signaux](#c1-comparatif-des-signaux)
  - [C.2 Arbre de décision de référence](#c2-arbre-de-décision-de-référence)
  - [C.3 Matrice délais × classe](#c3-matrice-délais--classe)
  - [C.4 Grille d'acceptation de risque](#c4-grille-dacceptation-de-risque)
- [Annexe D — Templates opérationnels](#annexe-d--templates-opérationnels)
  - [D.1 — Politique MCS](#d1--politique-mcs)
  - [D.2 — Table des classes de service](#d2--table-des-classes-de-service)
  - [D.3 — RACI du MCS](#d3--raci-du-mcs)
  - [D.4 — Fiche de dérogation](#d4--fiche-de-dérogation)
  - [D.5 — Demande de changement urgent](#d5--demande-de-changement-urgent)
  - [D.6 — Critères go / no-go](#d6--critères-go--no-go)
  - [D.7 — Plan de retour arrière](#d7--plan-de-retour-arrière)
  - [D.8 — Fiche d'obsolescence d'actif](#d8--fiche-dobsolescence-dactif)
  - [D.9 — Clauses contractuelles MCS](#d9--clauses-contractuelles-mcs)
  - [D.10 — Questionnaire fournisseur](#d10--questionnaire-fournisseur)
  - [D.11 — Journal de crise vulnérabilité](#d11--journal-de-crise-vulnérabilité)
  - [D.12 — Matrice de responsabilité cloud](#d12--matrice-de-responsabilité-cloud)
  - [D.13 — Dossier de preuves](#d13--dossier-de-preuves)
  - [D.14 — Procès-verbal de décommissionnement](#d14--procès-verbal-de-décommissionnement)
- [Annexe E — Familles d'outils et exemples de référence](#annexe-e--familles-doutils-et-exemples-de-référence)
  - [E.1 Comment lire les modèles de licence](#e1-comment-lire-les-modèles-de-licence)
  - [E.2 Les familles](#e2-les-familles)
  - [E.3 Critères de sélection, par ordre d'importance](#e3-critères-de-sélection-par-ordre-dimportance)
- [Annexe F — Cadre réglementaire et normatif comparatif](#annexe-f--cadre-réglementaire-et-normatif-comparatif)
- [Annexe G — Catalogue des faux positifs, pièges et illusions](#annexe-g--catalogue-des-faux-positifs-pièges-et-illusions)
  - [G.1 Scan et détection](#g1-scan-et-détection)
  - [G.2 Triage et pilotage](#g2-triage-et-pilotage)
  - [G.3 Déploiement](#g3-déploiement)
  - [G.4 Configuration et identités](#g4-configuration-et-identités)
  - [G.5 Périmètre et couverture](#g5-périmètre-et-couverture)
  - [G.6 Contractuel et fournisseurs](#g6-contractuel-et-fournisseurs)
  - [G.7 Industriel, cloud, services en ligne, produit](#g7-industriel-cloud-services-en-ligne-produit)
- [Annexe H — Calendrier des échéances et ressources](#annexe-h--calendrier-des-échéances-et-ressources)
  - [H.1 Échéances datées](#h1-échéances-datées)
  - [H.2 Échéances récurrentes sans date fixe](#h2-échéances-récurrentes-sans-date-fixe)
  - [H.3 Sources de veille et cadence](#h3-sources-de-veille-et-cadence)
  - [H.4 Formations et certifications](#h4-formations-et-certifications)
  - [H.5 Ressources et communautés](#h5-ressources-et-communautés)
- [Annexe I — Modèle de données MCS](#annexe-i--modèle-de-données-mcs)
  - [I.1 Entité ACTIF](#i1-entité-actif)
  - [I.2 Entités liées](#i2-entités-liées)
  - [I.3 Relations](#i3-relations)
  - [I.4 Périmètre maître et populations éligibles](#i4-périmètre-maître-et-populations-éligibles)
  - [I.5 Règles de qualité et contrôles](#i5-règles-de-qualité-et-contrôles)
  - [I.6 Exemple d'enregistrement](#i6-exemple-denregistrement)
- [Annexe J — Workflow et modèle de ticket de remédiation](#annexe-j--workflow-et-modèle-de-ticket-de-remédiation)
  - [J.1 États et transitions](#j1-états-et-transitions)
  - [J.2 Droits de transition](#j2-droits-de-transition)
  - [J.3 Champs obligatoires par état](#j3-champs-obligatoires-par-état)
  - [J.4 Les deux horloges](#j4-les-deux-horloges)
  - [J.5 Règles de déduplication et modèle parent / enfants](#j5-règles-de-déduplication-et-modèle-parent--enfants)
  - [J.6 Réouverture ou nouvelle occurrence](#j6-réouverture-ou-nouvelle-occurrence)
  - [J.7 Escalade — paramétrable par classe](#j7-escalade--paramétrable-par-classe)
  - [J.8 Issues et preuve exigée](#j8-issues-et-preuve-exigée)
- [Annexe K — Dictionnaire d'indicateurs et modèle de maturité](#annexe-k--dictionnaire-dindicateurs-et-modèle-de-maturité)
  - [K.1 Fiches d'indicateurs](#k1-fiches-dindicateurs)
  - [K.2 Règles de publication](#k2-règles-de-publication)
  - [K.3 Modèle de maturité — critères de preuve par niveau](#k3-modèle-de-maturité--critères-de-preuve-par-niveau)
  - [K.4 Grille d'auto-évaluation par domaine](#k4-grille-dauto-évaluation-par-domaine)
- [Annexe L — Checklists de cycle de vie](#annexe-l--checklists-de-cycle-de-vie)
  - [L.1 Mise en production](#l1-mise-en-production)
  - [L.2 Campagne périodique](#l2-campagne-périodique)
  - [L.3 Correctif urgent](#l3-correctif-urgent)
  - [L.4 Système non patchable](#l4-système-non-patchable)
  - [L.5 Mise à jour hors ligne (industriel)](#l5-mise-à-jour-hors-ligne-industriel)
  - [L.6 Renouvellement de certificat](#l6-renouvellement-de-certificat)
  - [L.7 Migration de version majeure](#l7-migration-de-version-majeure)
  - [L.8 Changement de fournisseur](#l8-changement-de-fournisseur)
  - [L.9 Décommissionnement](#l9-décommissionnement)
- [Ce que vous savez faire](#ce-que-vous-savez-faire)
  - [Vous savez établir un périmètre et le défendre](#vous-savez-établir-un-périmètre-et-le-défendre)
  - [Vous savez décider](#vous-savez-décider)
  - [Vous savez corriger sans casser](#vous-savez-corriger-sans-casser)
  - [Vous savez traiter ce qui ne se corrige pas](#vous-savez-traiter-ce-qui-ne-se-corrige-pas)
  - [Vous savez réagir](#vous-savez-réagir)
  - [Vous savez prouver et financer](#vous-savez-prouver-et-financer)
  - [Vous savez ce que vous ne savez pas](#vous-savez-ce-que-vous-ne-savez-pas)
- [Annexe M — Registre de sources](#annexe-m--registre-de-sources)
  - [M.1 Comment lire une entrée](#m1-comment-lire-une-entrée)
  - [M.2 Réglementation européenne et française](#m2-réglementation-européenne-et-française)
  - [M.3 Normes et référentiels](#m3-normes-et-référentiels)
  - [M.4 Écosystème des vulnérabilités](#m4-écosystème-des-vulnérabilités)
  - [M.5 Cycles de vie produits](#m5-cycles-de-vie-produits)
  - [M.6 Ce qui n'est pas sourcé, et l'est assumé](#m6-ce-qui-nest-pas-sourcé-et-lest-assumé)
  - [M.7 Sources à revérifier en priorité](#m7-sources-à-revérifier-en-priorité)
- [Journal des modifications](#journal-des-modifications)

---

## En-tête de maintenance

| Champ | Valeur |
|---|---|
| **Version du document** | 1.1 |
| **Dernière vérification factuelle** | 30 juillet 2026 |
| **Prochaine revue recommandée** | 31 janvier 2027, ou à la survenue d'un déclencheur ci-dessous |
| **Déclencheurs de revue anticipée** | Promulgation du texte français de transposition de NIS2 · publication d'une version définitive du ReCyF · nouvelle version majeure d'un modèle de score (EPSS, CVSS) · évolution du fonctionnement ou du financement des bases publiques de vulnérabilités · modification d'un calendrier de support étendu majeur · échéances CRA du 11/09/2026 et du 11/12/2027 |
| **Sources officielles surveillées** | cyber.gouv.fr et CERT-FR · digital-strategy.ec.europa.eu · enisa.europa.eu · legifrance.gouv.fr et dossiers législatifs · nvd.nist.gov · cve.org · first.org/epss · cisa.gov · learn.microsoft.com/lifecycle · pages de cycle de vie des éditeurs cités |
| **Sections périssables** *(à réviser en priorité)* | §4.9 · chapitre 8 (intégralité) · §12.4-12.5 · chapitre 19 · chapitre 30 · §33.5-33.7 · annexes B, E, F et H |
| **Noyau durable** *(révision rare)* | Chapitres 1-3, 5-7, 9-11, 13-18, 20-29, 31-32, 34-40 et cas de synthèse |
| **Journal des modifications** | En fin de document |

> **Règle de lecture.** Tout fait externe et périssable — calendrier réglementaire, version courante, état d'un programme de support, tarification — figure dans un bloc ⏱ **ÉTAT DE L'ART** daté et sourcé, ou dans une annexe versionnée. Les dates du cas fil rouge sont fictives. Le reste du texte est écrit pour rester valable au-delà de ces échéances.

---

## Matrice de parcours par profil

Le document dépasse les cent mille mots : cette matrice le rend navigable. Elle indique les chapitres à lire **en profondeur** ; le reste reste utile en survol.

| Profil | Parcours prioritaire |
|---|---|
| Débutant technique | 1-5, 7, 9-10, 14-21, 38-40 + cas A |
| Administrateur systèmes / sysops | 1-28, 34-40 + cas A et C |
| Responsable exploitation / production | 1-21, 26-28, 34-40 + les trois cas |
| RSSI | 1, 4-17, 20-21, 30-40 + les trois cas |
| Responsable OT / automatismes | 1-21, 27-29, 32, 34-40 + cas B |
| DevSecOps / responsable produit | 1-6, 11, 14-21, 23-26, 28, 30, 33-40 + cas C |
| Auditeur / consultant conformité | 1, 5, 7-17, 20, 35, 38-40 + cas B |
| Contexte PME (< 200 actifs) | Parcours socle + chapitre 40 et variantes PME des cas |

**Niveau visé** : débutant technique vers intermédiaire avancé. Aucun prérequis en gestion des vulnérabilités ni en conformité ; une culture informatique générale est recommandée. La Partie I rend autonome sur le MCS — elle ne remplace pas un cours de systèmes, de réseau, de cloud ou de développement, et le dit explicitement (§2.10).

**Fil rouge** : le cas HELIOMED court d'octobre 2025 à janvier 2029, à raison d'un épisode par chapitre. Tout y est fictif ; rien n'y est irréaliste.

---

### Comment lire les blocs de ce cours

| Bloc | Signification |
|---|---|
| 🖼 **SCHÉMA** | Emplacement d'un visuel à produire en mise en page. Le texte reste autonome sans lui |
| 🏢 **VU EN RÉUNION** | Situation réelle typique, en quelques lignes. Illustre un mécanisme, ne remplace pas son explication |
| 🔴 **FIL ROUGE** | Épisode du cas fil rouge HELIOMED, daté, avec une décision et un livrable |
| 🧪 **EN PRATIQUE** | Commande, procédure, workflow ou extrait de configuration réutilisable |
| ⚠️ **PIÈGE** | Erreur fréquente, faux sentiment de sécurité, faux positif classique |
| 📌 **LIMITES** | Ce qui ne fonctionne pas, ce qui n'est pas couvert, coût réel |
| ✅ **BONNE PRATIQUE** | Recommandation priorisée P0 (vital) / P1 (important) / P2 (confort) |
| ⚖️ **CADRE** | Obligation réglementaire, contractuelle ou normative |
| ⏱ **ÉTAT DE L'ART** | Donnée datée, avec sa source et sa date de vérification. **Périssable.** |

**Règle éditoriale.** Tout **fait externe et périssable** — calendrier réglementaire, version courante d'un produit, état d'un programme de support, tarification, politique d'un éditeur — est placé dans un bloc ⏱ ou dans une annexe versionnée, avec sa source et sa date de vérification. En revanche, les dates du cas fil rouge (fictives), les numéros de version utilisés comme exemples de mécanisme et les repères historiques durables figurent normalement dans le corps du texte.
Si vous relisez ce document dans deux ans : les blocs ⏱ et les annexes versionnées sont à réviser, le reste est écrit pour rester valable.

---

## PARTIE I — Fondations, socle technique et maintenabilité

Cette première partie a un objectif précis : vous rendre autonome sur le reste du cours. Elle ne suppose aucune expérience préalable en gestion des vulnérabilités, en conformité ou en exploitation de parc. Elle suppose en revanche une culture informatique générale — vous savez ce qu'est un serveur, un réseau, une application.

Elle ne remplace pas un cours de systèmes, de réseau, de cloud ou de développement, et le dit franchement à chaque fois que le sujet dépasse son périmètre.

---

### Chapitre 1 — Ce qu'est réellement le MCS

#### 1.1 Définition, origine et périmètre

##### Le modèle mental d'abord

Commençons par une image qui va vous servir pendant tout le cours.

Imaginez que vous installiez aujourd'hui un serveur neuf. Système à jour, configuration soignée, mots de passe robustes, aucune faille connue. Ce jour-là, son niveau de sécurité est le meilleur que vous puissiez connaître et valider. Appelons cela le jour J.

Le lendemain, vous ne touchez à rien. Personne ne s'y connecte, aucune configuration ne change, aucune ligne de code n'est modifiée. Et pourtant, la validité de votre évaluation a **déjà commencé à s'éroder**.

Pourquoi ? Parce que ce n'est pas le serveur qui a changé, c'est le monde autour de lui :

- un chercheur a publié une faille dans une bibliothèque qu'il utilise ;
- un attaquant a mis au point une technique qui contourne une de ses protections ;
- l'éditeur a annoncé que la version installée ne serait plus supportée dans dix-huit mois ;
- un certificat qu'il présente à ses clients a perdu un jour de sa durée de vie ;
- une autorité de certification dont dépend son démarrage sécurisé s'est rapprochée de sa date d'expiration.

C'est le point de départ de tout : **la sécurité n'est pas un état que l'on atteint, c'est un niveau qui se dégrade tout seul.** Sans effort continu, un système parfaitement sécurisé le jour J devient vulnérable, non par négligence ponctuelle, mais par simple écoulement du temps.

Le **maintien en condition de sécurité (MCS)** est l'ensemble des mesures techniques et organisationnelles qui compensent cette dégradation, pendant toute la durée de vie du système — de sa mise en service jusqu'à son retrait définitif.

##### La définition de travail

Retenez celle-ci, elle sera utilisée dans tout le cours :

> **MCS** : ensemble des activités techniques et organisationnelles visant à maintenir, et si possible améliorer, le niveau de sécurité d'un système d'information pendant tout son cycle de vie, y compris son décommissionnement — et à en apporter la preuve.

Trois éléments de cette définition méritent qu'on s'y arrête.

**« techniques *et* organisationnelles ».** Le MCS n'est pas un problème d'outil. Une organisation peut disposer du meilleur scanner de vulnérabilités du marché et n'appliquer aucun correctif, faute de savoir qui est responsable du serveur concerné. Nous verrons au §1.4 que les causes d'échec les plus fréquentes ne sont presque jamais techniques.

**« pendant tout son cycle de vie, y compris son décommissionnement ».** Un serveur éteint mais dont l'enregistrement DNS existe toujours, dont le compte de service reste actif et dont la sauvegarde reste restaurable n'est pas décommissionné : c'est un actif fantôme, et c'est un problème de MCS. Le chapitre 35 y est entièrement consacré.

**« et à en apporter la preuve ».** Une activité de MCS non traçable est presque impossible à piloter, à défendre en audit et à financer. C'est une exigence à part entière, pas une formalité administrative ajoutée après coup. Nous y reviendrons constamment, et le chapitre 39 la traite pour elle-même.

##### La boucle qui structure tout le cours

Un seul schéma suffit à décrire le métier. Chaque partie de ce cours travaille un segment de cette boucle, et chaque chapitre indique lequel.

```
                 ┌──────────────────────────────────────────┐
                 │                                          │
                 ▼                                          │
        ①  CONNAÎTRE ────► ②  OBSERVER ────► ③  DÉCIDER     │
        inventaire         veille,            triage,        │
        exposition         détection          priorisation   │
        propriété                                            │
                                     │                       │
                                     ▼                       │
        ⑥  PROUVER ◄──── ⑤  VÉRIFIER ◄──── ④  CORRIGER      │
        preuve,          état constaté,     ou compenser,    │
        indicateurs,     traîne longue      ou déroger       │
        audit                                                │
             │                                               │
             └───────────────────────────────────────────────┘
                        amélioration continue
```

| Segment | Question | Parties du cours |
|---|---|---|
| ① **Connaître** | Qu'est-ce que je dois maintenir, et qui en répond ? | I, II (ch. 10-13) |
| ② **Observer** | Qu'est-ce qui a changé, et cela me concerne-t-il ? | III (ch. 14-15) |
| ③ **Décider** | Que traiter, dans quel ordre, dans quel délai ? | III (ch. 16-17) |
| ④ **Corriger** | Appliquer, ou compenser, ou déroger | III, IV (ch. 18-28) |
| ⑤ **Vérifier** | Le code corrigé s'exécute-t-il vraiment ? | III (ch. 18) |
| ⑥ **Prouver** | Puis-je le démontrer dans six mois ? | VI (ch. 38-39) |

⚠️ **La boucle échoue toujours au même endroit** : au segment ①. Une organisation qui observe, décide, corrige et vérifie parfaitement sur un périmètre qu'elle ne connaît qu'à 70 % obtient d'excellents indicateurs sur 70 % de son parc — et ignore les 30 % restants, qui sont statistiquement les moins maintenus (§10.1).

🖼 **SCHÉMA — La boucle du MCS en six segments.** *Diagramme circulaire, six nœuds, flèche de retour « amélioration continue ». Chaque nœud porte son numéro de partie.*

##### Où se situe le MCS parmi les métiers voisins

Le MCS est régulièrement confondu avec trois fonctions voisines. Le tableau suivant sert de référence pour tout le cours.

| Fonction | Question centrale | Horizon | Ce qu'elle produit |
|---|---|---|---|
| **SOC / détection** | *Sommes-nous attaqués en ce moment ?* | Minutes à heures | Des alertes qualifiées |
| **CERT / CSIRT** | *Comment reprendre le contrôle ?* | Heures à jours | Une réponse à incident |
| **Exploitation** | *Est-ce que ça fonctionne ?* | Continu | Un service disponible |
| **MCS** | *Le niveau de sécurité tient-il dans la durée, et puis-je le prouver ?* | **Mois à années** | Un parc maintenu **et démontrable** |

**Les recouvrements sont réels et voulus.** Le MCS fournit au SOC un inventaire et une exposition à jour (ch. 10-11) ; le SOC fournit au MCS le signal d'exploitation (§14.5) ; le CERT hérite du MCS la capacité à savoir ce qui tournait où (§21.3). Ce qui distingue le MCS, c'est **l'horizon** : il est le seul de ces quatre métiers dont le succès se mesure sur plusieurs années.

##### Une journée type

Pour rendre le métier concret avant d'en décrire les mécanismes :

| Moment | Activité | Chapitre |
|---|---|---|
| 8 h 30 | Lecture de la veille : avis éditeurs, bulletins, signaux d'exploitation. Vingt minutes, tous les jours | 14 |
| 9 h 00 | Qualification des constats arrivés : fait vérifié, hypothèse, piste. Écarter les faux positifs de rétroportage | 14, 15 |
| 10 h 00 | Triage : passage dans l'arbre de décision. Ce qui part en urgence, en campagne, en surveillance | 16 |
| 11 h 00 | Comité de changement : défendre deux demandes, négocier une fenêtre | 5, 9 |
| 14 h 00 | Suivi des campagnes : relances, échecs d'installation, traîne longue à qualifier | 17, 18 |
| 15 h 30 | Une dérogation à instruire avec un propriétaire métier réticent | 7, 20 |
| 16 h 30 | Production de preuve : extraction, échantillon vérifié, archivage | 2, 39 |
| 17 h 00 | Une heure imprévue : un correctif qui casse, ou une alerte d'exploitation | 18, 21 |

**Ce que cette journée montre** : moins de la moitié du temps est technique. Le reste est de la qualification, de la négociation et de la preuve — ce qui explique la structure de ce cours.

##### Le vocabulaire du terrain

Ce cours emploie un vocabulaire rigoureux, parce que la précision évite des malentendus coûteux — notamment entre *couverture* et *conformité*, ou entre *dérogation* et *acceptation de risque*. En réunion, vous entendrez rarement ces mots. Voici la table de correspondance, à garder en tête tout au long du cours.

| Terme du cours | Ce que vous entendrez en réunion | Nuance à ne pas perdre |
|---|---|---|
| Correctif | « **le patch** », « la MAJ » | Un correctif est publié par un éditeur ; une « MAJ » peut aussi être une montée de version fonctionnelle |
| Campagne de correction | « **la campagne de patching** », « le patch tuesday » | — |
| Fenêtre de maintenance | « **la fenêtre** », « le créneau », « la patch window » | — |
| Ensemble des constats ouverts | « **le backlog** », « la pile », « les restes » | Le backlog n'est pas une file d'attente : il contient aussi des décisions prises de ne pas traiter |
| Constat | « **un finding** », « une vulné », « une CVE » | Un constat n'a pas nécessairement d'identifiant CVE — c'est tout le §14.2 |
| Dérogation | « **une exception** », « une déro », « un waiver » | « Exception » désigne aussi une exclusion d'outil : deux choses très différentes (§15.6) |
| Demande de changement | « **le change** », « la RFC », « le ticket de change » | — |
| Procédure d'exploitation | « **le runbook** », « la doc d'exploit » | — |
| Retour arrière | « **le rollback** » | — |
| Délai d'observation | « **le bake time** », « on laisse reposer » | — |
| Déploiement témoin | « **le canary** », « le pilote » | — |
| Durcissement | « **le hardening** » | — |
| Propriétaire d'actif | « **l'owner** », « le référent », « le responsable » | Le cours distingue propriétaire métier et technique : « l'owner » les confond souvent (§5.5) |
| Dette de sécurité | « **la dette** », « le legacy », « les vieilleries » | — |
| Gain rapide | « **un quick win** » | — |
| Périmètre de référence | « **le parc** », « le scope » | « Le parc » désigne souvent ce que l'outil connaît, pas le périmètre réel (§10.1) |

⚠️ **La règle à retenir** : parlez la langue de votre interlocuteur, mais **écrivez** la langue précise. Un compte rendu de comité qui dit « on a mis une exception sur la préprod » ne permet à personne, six mois plus tard, de savoir s'il s'agissait d'une dérogation signée, d'une exclusion de scan ou d'un risque accepté — et ces trois situations n'appellent ni le même suivi ni le même signataire.

##### D'où vient le terme

L'expression est une spécificité française. Elle est apparue par calque du **maintien en condition opérationnelle (MCO)**, terme d'origine militaire puis industrielle désignant l'ensemble des actions garantissant qu'un équipement reste disponible et fonctionnel. On la rencontre principalement :

- dans la doctrine et les guides de l'ANSSI (Agence nationale de la sécurité des systèmes d'information) ;
- dans les cahiers des charges de marchés publics, souvent sous la forme d'une clause « MCO/MCS » imposée au titulaire ;
- dans les dossiers d'homologation de sécurité, où le MCS conditionne le maintien de la décision d'homologation dans le temps.

Il n'existe pas d'équivalent unique en anglais. Le périmètre du MCS est couvert par plusieurs notions partiellement recouvrantes : *vulnerability management*, *patch management*, *security maintenance*, *continuous compliance*, *security operations*. Aucune ne correspond exactement, et c'est important : le MCS est **plus large que le patch management** et **plus étroit que « la sécurité »**.

⚠️ **PIÈGE — confondre MCS et gestion des correctifs**
C'est l'erreur la plus répandue du domaine, y compris chez des professionnels expérimentés. Un programme de MCS réduit aux correctifs laissera intacts : les configurations qui dérivent, les certificats qui expirent, les comptes de service jamais revus, les dépendances applicatives obsolètes, les micrologiciels jamais mis à jour, les règles de détection périmées, les systèmes retirés du service mais toujours joignables. Le §1.3 dresse la liste complète.

> ### 📌 Les quatre idées à retenir de ce chapitre
>
> Le chapitre 1 contient beaucoup de notions fondatrices. Si vous n'en gardez que quatre :
>
> 1. **La sécurité se dégrade toute seule.** Ce n'est pas le système qui change, c'est le monde autour de lui. Le MCS compense cette dégradation.
> 2. **Le MCS est plus large que la gestion des correctifs.** Dix familles d'objets se dégradent, et les versions logicielles n'en sont qu'une.
> 3. **Les cinq causes d'échec ne sont pas techniques** : inventaire, propriété, fenêtres, preuve, financement.
> 4. **Le MCS ne remplace ni la détection, ni la sauvegarde, ni l'architecture.** Il réduit la probabilité qu'une attaque connue réussisse. C'est tout, et c'est beaucoup.
>
> Le reste du chapitre est du contexte utile. Ces quatre points sont réutilisés dans les trente-neuf chapitres suivants.

#### 1.2 MCO et MCS : deux maintiens, un conflit structurel

Le MCO répond à la question : *est-ce que ça marche ?*
Le MCS répond à la question : *est-ce que c'est encore sûr ?*

Ces deux questions sont portées par les mêmes équipes, sur les mêmes machines, dans les mêmes fenêtres d'intervention, avec le même budget. Elles entrent en conflit régulièrement, et ce conflit n'est ni un dysfonctionnement ni un problème de personnes : il est **structurel**.

| Situation | Ce que dicte le MCO | Ce que dicte le MCS |
|---|---|---|
| Correctif de sécurité disponible, non testé | Attendre : le risque de régression est réel | Appliquer vite : la faille est peut-être exploitée |
| Version majeure en fin de support, applicatif métier incompatible | Ne pas migrer : l'application casserait | Migrer : plus aucun correctif ne sera publié |
| Redémarrage nécessaire en pleine période d'activité | Reporter au prochain arrêt planifié | Le report allonge la fenêtre d'exposition |
| Équipement fonctionnel mais hors support constructeur | Il fonctionne, on le garde | Il ne recevra plus jamais de correctif |

La conséquence pratique est simple à énoncer et difficile à vivre : **le MCS ne s'impose jamais contre le MCO, il se négocie avec lui**. Toute organisation qui prétend faire du MCS en ignorant les contraintes de production produit soit du conflit permanent, soit des décisions non appliquées. Le chapitre 9 (gouvernance) et le chapitre 37 (facteur humain) traitent cette négociation comme un objet d'ingénierie à part entière, pas comme un problème relationnel.

> **Encadré terminologique — les termes qu'on vous opposera**
> Vous rencontrerez d'autres expressions : **MCP** (maintien en condition de performance), **MCF** (maintien en condition fonctionnelle), *continuous compliance*. Aucune n'est normalisée, et leur périmètre varie fortement d'une organisation à l'autre et d'un appel d'offres à l'autre.
> **Recommandation** : ne les importez pas. Si votre organisation les utilise, définissez-les explicitement dans votre politique interne, avec leur périmètre et leur propriétaire. Un terme non défini dans un contrat de prestation est une source de litige : chacun l'interprétera dans son intérêt le jour où quelque chose ne sera pas fait.

#### 1.3 Le périmètre réel du MCS : dix objets qui se dégradent

**Ces dix familles ont un point commun**, et c'est lui qui les rassemble : elles perdent progressivement leur niveau de sécurité si personne ne les entretient, **indépendamment de toute action de votre part**. Voici ce qui, dans un système d'information, se dégrade avec le temps. La liste n'est pas exhaustive ; elle couvre l'essentiel de ce qu'un programme de MCS doit adresser. Chaque ligne correspond à un ou plusieurs chapitres du cours.

| Objet maintenu | Ce qui se dégrade | Rythme typique de dégradation | Traité au |
|---|---|---|---|
| **Versions logicielles** | Failles publiées, fin de support | Continu, accéléré à chaque publication de correctif | Ch. 15-19 |
| **Configurations** | Dérive par intervention manuelle, urgence, restauration | Lent mais irréversible sans contrôle | Ch. 22-23 |
| **Identités et droits** | Comptes orphelins, délégations héritées, droits accumulés | Très lent, jamais spontanément réversible | Ch. 24 |
| **Secrets** | Vieillissement, diffusion, absence de rotation | Se dégrade à chaque départ de collaborateur | Ch. 24 |
| **Certificats et confiance** | Expiration, algorithmes dépréciés, autorités qui expirent | Échéance **datée et connue à l'avance** | Ch. 24, 27 |
| **Dépendances logicielles** | Failles de composants tiers, projets abandonnés | Continu, hors de votre contrôle | Ch. 25 |
| **Micrologiciels** | Failles de bas niveau, fin de support matériel | Lent, mais correctifs rares et risqués | Ch. 27 |
| **Contenu de détection** | Signatures, règles, listes de blocage périmées | Quotidien | Ch. 34 |
| **Documentation et procédures** | Écart croissant avec la réalité | Se dégrade à chaque changement non documenté | Ch. 39 |
| **Compétences des personnes** | Départs, perte de savoir non transmis | Brutal (un départ) | Ch. 37 |

Deux observations sur ce tableau, qui structureront toute votre approche.

**Première observation : toutes ces échéances ne sont pas de même nature.** Une distinction utile, et souvent mal faite :

- **L'expiration d'un certificat est intrinsèque.** Elle est encodée dans l'objet lui-même, dès son émission, et elle est absolue : à la seconde près, le certificat cesse d'être valide, quoi que décide qui que ce soit. C'est la seule échéance que personne ne peut déplacer.
- **Une fin de support est une échéance éditoriale ou contractuelle.** Elle est décidée par un tiers, annoncée à l'avance, et **elle peut être modifiée** — prolongée, raccourcie, assortie de conditions nouvelles. Planifier dessus est indispensable, mais il faut la resurveiller.
- **Les autres échéances sont des décisions internes** : rotation de clé, migration planifiée, fin de contrat. Elles ne s'imposent que si quelqu'un les tient.

L'ironie du domaine est que la catégorie la plus prévisible — l'expiration cryptographique — reste l'une des premières causes d'interruption de service. La raison est presque toujours la même : personne ne tient l'inventaire de ce qui expire.

⏱ **ÉTAT DE L'ART — l'illustration de l'année 2026 (vérifié le 30/07/2026)**
Les certificats Microsoft utilisés par le démarrage sécurisé (*Secure Boot*), émis en 2011 pour quinze ans, sont arrivés à échéance en juin 2026, une troisième suivant en octobre 2026. Les machines concernées continuent de démarrer et de recevoir leurs mises à jour habituelles ; elles perdent en revanche, silencieusement, la capacité de recevoir de futures protections de la chaîne de démarrage. Le mécanisme complet, les trois certificats et les cinq enseignements de MCS que ce cas contient sont traités au **§3.8**.
📎 [S-25]

**Seconde observation : aucun outil ne couvre les dix lignes.** Ne cherchez pas la plateforme unique. Elle n'existe pas, et les fournisseurs qui la promettent couvrent en réalité trois ou quatre lignes correctement, les autres superficiellement. Votre travail consiste à savoir *quelle ligne est couverte par quoi*, et surtout **quelle ligne n'est couverte par rien**.

#### 1.4 Les cinq causes récurrentes d'échec

Les retours d'expérience du domaine convergent vers un constat stable : les programmes de MCS échouent le plus souvent pour les mêmes raisons, et généralement dans le même ordre. Aucune n'est **exclusivement** technique.

**1. L'inventaire.** On ne maintient pas ce qu'on ne connaît pas. Un écart de 15 à 30 % entre l'inventaire théorique et la réalité est la norme, pas l'exception, dans une organisation qui n'a jamais fait ce travail. Tant que cet écart n'est pas mesuré et réduit, tous les indicateurs de MCS sont faux — non pas imprécis : **faux**, parce que leur dénominateur est inconnu. → Chapitre 10.

**2. La propriété.** Pour chaque actif, une question doit avoir une réponse nominative : *qui décide qu'on l'arrête pour le corriger ?* En l'absence de réponse, le correctif attend. Ce n'est pas un problème de bonne volonté : c'est un vide de décision, et personne ne prend spontanément une décision dont il n'a pas le mandat. → Chapitres 5 et 9.

**3. Les fenêtres.** Corriger suppose souvent d'interrompre. Si l'organisation n'a pas négocié à l'avance des créneaux d'interruption acceptés par les métiers, chaque correctif devient une négociation individuelle — donc un coût, donc un report. → Chapitres 5, 18 et 37.

**4. La preuve.** Sans traçabilité, vous ne pouvez ni démontrer un progrès, ni justifier un budget, ni répondre à un auditeur, ni savoir si un correctif a réellement été appliqué sur les 2 300 postes concernés ou seulement sur les 1 800 qui étaient allumés ce soir-là. → Chapitres 38 et 39.

**5. Le financement.** Sortir de l'obsolescence coûte cher, et ce coût est visible immédiatement alors que le bénéfice est invisible et différé. Sans dossier d'investissement construit, l'arbitrage budgétaire est perdu d'avance, chaque année, indéfiniment. → Chapitre 37.

✅ **BONNE PRATIQUE — l'ordre d'attaque (P0)**
Si vous démarrez un programme de MCS, traitez ces cinq causes **dans cet ordre**. Investir dans l'outillage de déploiement avant d'avoir un inventaire fiable et des propriétaires nommés est l'erreur de séquencement la plus coûteuse du domaine : vous automatiserez le traitement d'un périmètre que vous ne connaissez pas, et vous produirez des tableaux de bord verts sur un dénominateur faux. Le chapitre 40 détaille la feuille de route complète.

#### 1.5 Le MCS dans le cycle de vie : *build → run → sunset*

Le MCS est habituellement perçu comme une activité du *run* — la phase d'exploitation. C'est incomplet, et cette incomplétude coûte cher.

**Phase *build* (conception et construction).** Les décisions d'architecture prises ici déterminent le coût de tout le MCS futur. Un système sans redondance ne pourra jamais être corrigé sans interruption. Une application couplée à une version précise de son environnement d'exécution bloquera toutes les montées de version. Un produit sans mécanisme de mise à jour signé ne pourra jamais être corrigé chez le client en confiance. Le chapitre 6 est entièrement consacré à cette phase, sous le nom de *MCS by design*.

**Phase *run* (exploitation).** C'est le cœur du cours : veille, détection, triage, remédiation, configuration, preuve. Parties II à V.

**Phase *sunset* (fin de vie et retrait).** Elle commence bien avant l'arrêt : dès l'annonce de fin de support par l'éditeur, une trajectoire doit exister. Elle se termine par un décommissionnement complet et vérifié. Chapitres 12 et 35.

L'enseignement structurant tient en une phrase : **le coût du MCS d'un système est majoritairement déterminé pendant la phase où l'on n'y pense pas.**

#### 1.6 La dette de sécurité comme grandeur mesurable

⚠️ **Une confusion à écarter d'emblée** : la dette de sécurité n'est pas le stock de vulnérabilités non corrigées. Elle comprend aussi les systèmes hors support, les configurations dérivées, les comptes jamais revus, les certificats non inventoriés, les dérogations accumulées et les architectures non interruptibles. Un parc sans aucune vulnérabilité ouverte peut porter une dette considérable.

L'analogie financière est ici juste, et pas seulement décorative.

Quand vous reportez une mise à jour, vous contractez une dette. Vous obtenez un bénéfice immédiat (pas d'interruption, pas de risque de régression, pas de charge de travail) contre un coût futur. Et comme toute dette, elle produit des **intérêts** : plus vous attendez, plus la migration devient difficile, parce que l'écart de versions grandit, que les chemins de migration directs disparaissent, que les compétences se perdent et que le nombre de failles cumulées augmente.

C'est ce qui explique un phénomène que vous observerez : le coût d'une migration ne croît pas proportionnellement au délai de report, il croît plus vite. Les mécanismes en sont identifiables un par un — chemins de migration directs qui disparaissent et imposent des étapes intermédiaires, matériel devenu incompatible, compétences perdues, dépendances applicatives qui se sont multipliées entre-temps. L'ampleur exacte dépend entièrement du contexte : ce qui est généralisable, c'est le mécanisme, pas un facteur multiplicateur.

Quatre grandeurs suffisent à rendre cette dette visible. Elles sont définies rigoureusement au chapitre 38 et détaillées en Annexe K ; à ce stade, retenez l'idée :

- le **nombre d'actifs hors support**, pondéré par leur criticité ;
- le **nombre de vulnérabilités critiques dont le délai de correction est dépassé** ;
- le **nombre et l'ancienneté des dérogations ouvertes** — une dérogation est une dette formalisée ;
- l'**âge moyen des constats non traités**, qui mesure la vitesse réelle de l'organisation.

⚠️ **PIÈGE — la dette invisible est la plus dangereuse**
Une organisation qui ne mesure pas ces grandeurs n'a pas moins de dette : elle a la même dette, sans le savoir. Et une dette non mesurée ne se finance jamais, puisqu'elle n'apparaît dans aucun arbitrage budgétaire.

#### 1.7 Ce que le MCS ne résout pas

Un cours honnête doit énoncer clairement les limites de son sujet. Le MCS **ne protège pas** contre :

- **une vulnérabilité inconnue de tous** (*0-day*) : par définition, aucun correctif n'existe. Le MCS réduit la surface disponible et raccourcit le délai de réaction quand le correctif arrive ; il n'empêche pas l'attaque ;
- **l'hameçonnage et l'ingénierie sociale** : un poste parfaitement à jour n'empêche pas un utilisateur de saisir ses identifiants sur un site frauduleux ;
- **un défaut d'architecture** : un système à jour mais exposé sans nécessité sur Internet reste une cible. Fermer l'exposition est souvent plus efficace que corriger — c'est l'objet du chapitre 11 ;
- **l'usage légitime détourné** : un attaquant disposant d'identifiants valides n'a besoin d'aucune faille ;
- **une erreur de conception de sécurité** : une fonctionnalité dangereuse par construction ne sera pas corrigée par une mise à jour, puisqu'elle fonctionne comme prévu.

Le MCS se positionne donc comme **une couche parmi d'autres** : il réduit la probabilité qu'une attaque connue réussisse, il ne remplace ni la détection, ni la sauvegarde, ni la segmentation, ni l'architecture.

⚠️ **PIÈGE — les quatre illusions les plus coûteuses**

| Illusion | Ce qui cloche |
|---|---|
| « On applique tous les correctifs, donc on est à jour » | Vous appliquez les correctifs *des actifs que vous connaissez*, *que votre outil couvre*, *et qui étaient joignables*. Les trois filtres se cumulent |
| « Le tableau de bord est à 98 % de conformité » | 98 % de quel dénominateur ? Calculé quand ? Avec quelles exclusions ? Voir §38.3 |
| « C'est du cloud / du SaaS, c'est maintenu par le fournisseur » | Le fournisseur maintient sa couche. La vôtre — configuration, identités, extensions, intégrations — reste entièrement à votre charge. Chapitres 30 et 31 |
| « Le scanner ne remonte rien sur cette machine » | Peut-être qu'elle n'est pas vulnérable. Peut-être qu'elle n'a pas été scannée. Ce n'est pas la même information, et la distinction est traitée au §15.8 |

#### 1.8 ⏱ État de l'art du domaine au 30 juillet 2026

*Bloc périssable. Vérifié le 30/07/2026. À réviser en priorité lors de la prochaine revue du cours.*

**Ce qui a changé récemment**

- **La priorisation par la seule gravité technique n'est plus défendable.** Le raisonnement « je corrige tout ce dont le score de gravité dépasse 7 » conduit à traiter plus de la moitié des vulnérabilités publiées, dont l'écrasante majorité ne sera jamais exploitée. Les approches par exploitation observée et par exposition réelle se sont imposées. Chapitre 16.
- **L'écosystème public de données de vulnérabilités s'est fragmenté.** Le NIST a annoncé qu'à compter du 15 avril 2026, l'enrichissement des fiches du NVD serait priorisé (vulnérabilités connues comme exploitées, logiciels utilisés par l'administration fédérale américaine, logiciels critiques), les autres pouvant porter la mention *Not Scheduled*. Attention à la formulation exacte : **toutes les vulnérabilités continuent d'être enregistrées** ; c'est l'enrichissement, c'est-à-dire l'analyse complémentaire, qui devient sélectif. En parallèle, la base européenne EUVD de l'ENISA est montée en charge et d'autres initiatives d'identification sont apparues. Chapitre 4. 📎 [S-16] [S-22]
- **La réglementation est passée du système d'information au produit.** Le Cyber Resilience Act européen impose des obligations aux fabricants de produits comportant des éléments numériques, y compris en matière de notification de vulnérabilités activement exploitées. Chapitres 8 et 33. 📎 [S-04] [S-05]

**Ce qui émerge**

- L'accélération de la découverte de vulnérabilités, notamment par des méthodes assistées par intelligence artificielle, accroît la pression sur la vitesse de remédiation plus que sur la qualité du triage. Chapitre 36.
- La généralisation progressive des inventaires de composants logiciels (SBOM) sous l'effet réglementaire, avec un usage réel encore très en retard sur la production de ces documents. Chapitre 25.

**Ce qui reste stable, et le restera**

L'inventaire, la propriété d'actif, la négociation des fenêtres, la preuve et le financement. Ces cinq points étaient les causes d'échec il y a vingt ans, ils le sont aujourd'hui, ils le seront encore quand les outils cités dans ce cours auront disparu.

**Ce qui devient obsolète**

- La campagne mensuelle unique et uniforme comme seule doctrine de correction, sans traitement différencié de l'urgence.
- Le pilotage par le nombre brut de vulnérabilités détectées, indicateur qui récompense l'inaction (ne rien scanner produit d'excellents chiffres).
- La dépendance à une source unique de données de vulnérabilités.

#### 1.9 Comment lire ce cours

Le cours compte 40 chapitres, 3 cas de synthèse et 12 annexes. Il n'est pas conçu pour être lu intégralement d'un trait.

- **Partie I (ch. 1-6)** : à lire dans l'ordre. Elle installe le vocabulaire et le socle technique.
- **Parties II à VI** : consultables par thème. Chaque chapitre est autonome et renvoie explicitement aux autres.
- **Partie VII** : à traiter en dernier, en situation, avec les annexes ouvertes à côté.
- **Annexes** : ce sont des outils de travail, pas des compléments. Les annexes I (modèle de données), J (workflow de remédiation), K (indicateurs) et L (listes de contrôle) sont directement réutilisables.

Une matrice de parcours par profil figure en tête du document. Si vous découvrez le domaine, suivez le parcours « débutant technique » : il vous mènera à un niveau opérationnel sans passer par les chapitres de spécialisation.

🔴 **FIL ROUGE — octobre 2025 : la surprime**

*Le fil rouge de ce cours suit une organisation fictive, le groupe HELIOMED. Tout y est inventé — l'entreprise, les personnes, les incidents — mais rien n'y est irréaliste. Vous n'avez rien à connaître de ce contexte : il est décrit au fur et à mesure.*

HELIOMED est une entreprise de taille intermédiaire française : 1 380 salariés, 240 M€ de chiffre d'affaires. Elle fabrique des dispositifs médicaux connectés — des pompes à perfusion PX-40 — et édite une plateforme de télésuivi, HelioLink, complétée d'une passerelle hospitalière, HelioBox, et d'une application mobile de bien-être, HelioMove. Trois sites : Lyon (siège et direction des systèmes d'information), Saint-Étienne (usine), Nantes (recherche et développement logiciel).

Claire Nadeau prend son poste de responsable de la sécurité des systèmes d'information en octobre 2025. Elle est rattachée à la direction générale. Sa première semaine ne se passe pas comme prévu.

Le courtier en assurance appelle : l'assureur cyber ne renouvellera pas le contrat aux conditions précédentes. La cause tient en une ligne du rapport d'analyse : *absence de processus de gestion des correctifs démontrable*. Surprime demandée : 34 %.

Claire demande à voir le processus. Il existe. Il est écrit. Malik Ferhaoui, responsable de l'exploitation, applique consciencieusement les correctifs Microsoft chaque mois sur les serveurs. Ce qui n'existe pas, c'est :

- la liste exhaustive des actifs concernés — personne ne sait combien de serveurs sont réellement en service ;
- la trace de ce qui a été appliqué, où, et quand ;
- le traitement de tout ce qui n'est pas un serveur Windows : équipements réseau, hyperviseurs, automates de l'usine, applications hébergées chez des tiers ;
- une réponse à la question « qui décide d'arrêter tel serveur pour le corriger ? ».

Autrement dit : les cinq causes d'échec du §1.4, toutes présentes simultanément. Le processus n'est pas mauvais, il est *invisible* et *partiel*.

**Décision prise.** Claire ne lance pas d'appel d'offres outillage. Elle demande six semaines pour produire trois livrables : un inventaire réel du périmètre, une liste nominative de propriétaires d'actifs, et une mesure de l'écart entre ce que l'entreprise croit maintenir et ce qu'elle maintient effectivement.

**Livrable de l'épisode.** Une note d'une page à la direction générale, qui ne parle ni de vulnérabilités ni d'outils, et pose une seule question : *combien d'actifs devons-nous maintenir, et qui en est responsable ?*

→ La suite en 🔴 §2.9, où cette question rencontre son premier obstacle technique.

#### Synthèse mentale du chapitre 1

La sécurité d'un système se dégrade sans qu'on y touche, parce que c'est le monde qui change autour de lui. Le MCS est l'ensemble des activités — techniques **et** organisationnelles — qui compensent cette dégradation sur tout le cycle de vie, décommissionnement compris, et qui en apportent la preuve. Il est plus large que la gestion des correctifs : dix objets se dégradent, dont les configurations, les identités, les certificats, les micrologiciels et le contenu de détection. Il est en tension permanente avec le maintien en condition opérationnelle, et cette tension se négocie, elle ne se tranche pas par autorité. Cinq causes expliquent la plupart des échecs — inventaire, propriété, fenêtres, preuve, financement — et aucune n'est technique. Enfin, le MCS ne protège ni contre une faille inconnue, ni contre l'hameçonnage, ni contre un défaut d'architecture : c'est une couche parmi d'autres.

**Trois questions de vérification**

1. Un serveur installé et parfaitement à jour, auquel personne ne touche pendant six mois, est-il toujours au même niveau de sécurité ? Justifiez en citant au moins trois des dix objets du §1.3.
2. Une organisation affiche 98 % de conformité aux correctifs. Quelles trois questions posez-vous avant d'accorder la moindre valeur à ce chiffre ?
3. Parmi les cinq causes d'échec du §1.4, laquelle doit être traitée en premier, et pourquoi investir dans l'outillage avant elle est-il une erreur de séquencement ?

---

### Chapitre 2 — Socle technique 1 : systèmes, paquets, cycles de support, réseau, identité

Ce chapitre installe les mécanismes concrets. Il ne suppose aucune expérience préalable d'administration, mais il ne survole rien : ces mécanismes expliquent la quasi-totalité des malentendus, des faux positifs et des échecs de correction que vous rencontrerez ensuite.

#### 2.1 Anatomie d'un système à maintenir

Quand quelqu'un affirme « ce serveur est à jour », l'affirmation est ambiguë. Un système est un empilement de couches, mises à jour par des mécanismes différents, à des rythmes différents, souvent par des personnes différentes.

| Couche | Contenu | Qui la met à jour | Nécessite un redémarrage ? |
|---|---|---|---|
| Micrologiciel | BIOS/UEFI, contrôleur de gestion à distance, cartes | Constructeur, via un outil séparé | Oui, souvent complet |
| Noyau | Cœur du système d'exploitation | Éditeur du système | Oui, sauf correction à chaud |
| Bibliothèques partagées | Code commun réutilisé par de nombreux programmes | Éditeur du système | Non, mais redémarrage des services qui les utilisent |
| Services système | Serveur web, base de données, service d'annuaire | Éditeur du système ou éditeur tiers | Redémarrage du service |
| Applications | Logiciels métier, souvent installés hors gestionnaire de paquets | Éditeur métier, parfois manuellement | Variable |
| Agents | Sécurité, sauvegarde, supervision, gestion de parc | Console centrale correspondante | Variable |
| Environnements d'exécution embarqués | Machine virtuelle applicative, interpréteur livré avec l'application | Souvent **personne** | Variable |

⚠️ **PIÈGE — la couche que personne ne met à jour**
La dernière ligne est le trou noir classique. Une application métier livrée avec sa propre copie d'un environnement d'exécution ou d'une bibliothèque de chiffrement ne sera mise à jour par **aucun** mécanisme système. Le système d'exploitation sera parfaitement à jour, le scanner ne verra peut-être rien, et le composant vulnérable sera là depuis trois ans. Le chapitre 26 traite entièrement cette couche.

Point essentiel à retenir : **une bibliothèque partagée corrigée sur disque continue d'être exécutée dans sa version vulnérable par tous les processus déjà lancés**, jusqu'à leur redémarrage. Corriger et redémarrer sont deux actes distincts, et seul le second termine le travail. C'est la raison d'être des outils présentés au §2.6.

#### 2.2 Comment un correctif est réellement produit et distribué

C'est le mécanisme le plus important du chapitre. Il explique à lui seul une grande partie des faux positifs que vous rencontrerez.

**Le trajet complet d'une correction :**

```
1. Découverte de la faille          → chercheur, éditeur, attaquant
2. Correction dans le code source   → projet « amont » (upstream)
3. Publication d'une version amont  → ex. version 3.2.4 du projet
4. Reprise par l'éditeur du système → décision : nouvelle version, ou backport
5. Construction du paquet           → compilation, tests, numérotation
6. Signature cryptographique        → l'éditeur signe le paquet
7. Publication sur un dépôt         → dépôt officiel, miroirs
8. Récupération par votre machine   → le client vérifie la signature
9. Installation                     → écriture des fichiers
10. Redémarrage du composant        → le code corrigé s'exécute enfin
```

Une correction devient effective **lorsque le code corrigé est réellement chargé et exécuté**. Dans certains cas, l'installation suffit — un binaire lancé à chaque exécution est corrigé immédiatement. Dans beaucoup d'autres, il faut redémarrer le processus, le service, voire le système. Un programme de MCS qui s'arrête à l'étape 9 sans vérifier l'étape 10 laisse donc, dans un nombre de cas non négligeable, du code vulnérable en cours d'exécution.

🖼 **SCHÉMA — Le trajet d'un correctif, de l'amont au chargement effectif.** *Chaîne linéaire à dix étapes, avec l'étape 10 (redémarrage) mise en évidence et la bifurcation « backport » à l'étape 4.*

##### Le *backport* : la notion qui fausse tous les scanners

À l'étape 4, l'éditeur d'un système à support long a deux options. Soit il livre la nouvelle version amont — ce qui risque de casser les applications de ses utilisateurs. Soit il **extrait uniquement le correctif de sécurité et l'applique à la version ancienne** qu'il distribue déjà. Cette seconde option s'appelle le *backport*, et c'est le fonctionnement normal de toutes les distributions à support long.

Conséquence directe, et contre-intuitive : **le numéro de version affiché ne reflète plus la présence ou l'absence de la faille.**

🎯 **CE QUE ÇA CHANGE POUR VOUS** — Votre scanner vous signalera des vulnérabilités déjà corrigées, en volume, sur tout votre parc à support long. Si vous lancez une campagne sur ce signal sans vérifier, vous consommerez des fenêtres, des redémarrages et du temps d'équipe pour rien — et vous prendrez un risque de régression sans aucune contrepartie. C'est exactement ce qui arrive au §15.13, sur 42 serveurs.

**Exemple simplifié — volontairement fictif, pour isoler le mécanisme.** Une faille est corrigée en amont dans la version 3.0.15 d'une bibliothèque. Votre serveur affiche la version 3.0.11. Un scanner qui raisonne sur le seul numéro amont conclut : vulnérable. Or le paquet installé porte le numéro complet `3.0.11-1+deb12u3` : le suffixe indique une révision de sécurité de l'éditeur, qui contient précisément le correctif rétroporté. La machine n'est pas vulnérable, et le scanner a produit un **faux positif structurel**.

Deux précisions, parce que ce mécanisme est souvent mal reproduit :
- La **syntaxe varie selon le paquet et la distribution**. On rencontre aussi bien les formes `+debXuY` que `~debXuY`, et les familles RPM utilisent une numérotation de publication différente. Ne cherchez pas un motif universel : cherchez la révision propre à l'éditeur.
- Le raisonnement vaut pour les distributions à support long. Sur une distribution à version continue, le numéro amont redevient une information fiable.

🧪 **EN PRATIQUE — vérifier si un correctif est réellement présent**

```bash
# Famille Debian / Ubuntu : version exacte du paquet installé
dpkg -l | grep openssl
apt-cache policy openssl

# Le journal des modifications du paquet cite les CVE corrigées
zcat /usr/share/doc/openssl/changelog.Debian.gz | head -40
# ou, si le dépôt source est configuré :
apt changelog openssl | head -40

# Famille RHEL / Rocky / Alma : le changelog du paquet cite les CVE
rpm -q --changelog openssl | grep -i CVE-2024 | head

# Mises à jour disponibles
dnf updateinfo list security   # famille RHEL : filtre réellement sur la sécurité
apt list --upgradable          # famille Debian : TOUTES les mises à jour, pas seulement la sécurité
```

⚠️ **PIÈGE — deux sources qu'on prend à tort pour des preuves**
`apt list --upgradable` liste l'ensemble des mises à jour disponibles, **sans distinguer** ce qui relève de la sécurité. Ne le présentez jamais comme une liste de correctifs de sécurité dans un rapport.
De même, un journal des modifications local est un **indice**, pas une preuve : il peut être incomplet, tronqué à l'installation, ou ne pas mentionner l'identifiant de la faille. La **source de vérité** est l'avis de sécurité publié par la distribution ou l'éditeur, associé à l'état officiel du paquet dans son suivi de sécurité.

La règle opérationnelle : **ne jamais conclure à une vulnérabilité sur le seul numéro de version amont d'un système à support long**, et ne jamais conclure à l'absence de vulnérabilité sur le seul journal local. Croisez avis de sécurité de la distribution et version de paquet installée. Cette vérification est au cœur du chapitre 15 (interprétation des rapports de scan).

##### Ce qui se passe quand l'éditeur ne reprend pas la correction

L'étape 4 peut aussi ne jamais avoir lieu. Trois cas fréquents :

- la version que vous utilisez n'est plus supportée : la correction existe en amont, elle ne viendra jamais chez vous ;
- l'éditeur juge la faille non applicable à sa configuration : c'est parfois justifié, parfois discutable, et cela doit être documenté ;
- le composant est fourni par un éditeur métier qui ne suit pas l'amont : vous dépendez alors entièrement de son bon vouloir, ce qui est un sujet contractuel (chapitre 13).

#### 2.3 Chaînes de confiance : pourquoi vous pouvez installer ce paquet

Vous téléchargez du code exécutable depuis Internet et vous l'installez avec les privilèges les plus élevés du système. Ce qui rend cette opération acceptable, c'est une chaîne de confiance cryptographique.

**Le mécanisme.** L'éditeur signe ses paquets, ou l'index qui décrit les paquets, avec une clé privée. Votre machine détient la clé publique correspondante, installée à la mise en service. Avant toute installation, le gestionnaire de paquets vérifie que la signature correspond. Si elle ne correspond pas, l'installation échoue.

Ce mécanisme protège contre trois attaques : la modification d'un paquet en transit, la compromission d'un miroir de distribution, et la substitution d'un dépôt.

**Ce qu'il ne protège pas.** Il n'atteste **ni de la qualité, ni de l'innocuité** du contenu. Une signature valide signifie « ce paquet vient bien de cet éditeur », pas « ce paquet est sûr ». Si l'éditeur lui-même est compromis, la signature reste parfaitement valide — c'est le principe des attaques sur la chaîne d'approvisionnement, traitées au chapitre 25.

⚠️ **PIÈGE — les trois ruptures de confiance les plus fréquentes**

| Rupture | Comment elle se produit | Conséquence |
|---|---|---|
| Vérification désactivée | Options du type « ignorer la signature » ajoutées pour débloquer une installation, puis jamais retirées | Toute la chaîne s'effondre silencieusement |
| Dépôt tiers non maîtrisé | Ajout d'un dépôt externe pour obtenir un logiciel précis | Ce dépôt peut mettre à jour **n'importe quel** paquet du système |
| Clé expirée ou non renouvelée | La clé de signature du dépôt arrive à expiration | Les mises à jour s'arrêtent, souvent sans alerte visible |

La troisième mérite une attention particulière : **l'arrêt des mises à jour est silencieux**. La machine ne signale pas « je ne reçois plus de correctifs » ; elle signale, au mieux, une erreur dans un journal que personne ne lit. C'est exactement le type de dégradation que le §2.9 apprend à détecter.

#### 2.4 Modèles de support : lire une matrice de cycle de vie

Chaque éditeur définit une politique de support. En comprendre le vocabulaire évite des erreurs de planification à plusieurs centaines de milliers d'euros.

| Modèle | Principe | Implication MCS |
|---|---|---|
| **Support long (LTS)** | Une version figée, maintenue par *backport* pendant 5 à 10 ans | Stabilité maximale, mais numéros de version trompeurs (§2.2) |
| **Version continue** (*rolling*) | Mise à jour permanente vers l'amont | Toujours à jour, mais chaque mise à jour est un changement fonctionnel |
| **Canal long terme** (LTSC) | Équivalent Windows du support long, sans nouvelles fonctionnalités | Adapté aux postes techniques figés, pas au parc bureautique |
| **Support étendu payant** (ESU/ELS/ESM) | Correctifs de sécurité au-delà de la fin de support normale | Solution transitoire, coûteuse, **au périmètre strictement conditionné** |

Trois dates différentes coexistent dans une matrice de cycle de vie, et les confondre est une erreur classique :

- **fin de vie fonctionnelle** : plus de nouvelles fonctionnalités ;
- **fin de support** : plus de correctifs, y compris de sécurité — c'est la seule date qui compte pour le MCS ;
- **fin de support étendu** : après souscription d'une offre spécifique.

⚠️ **PIÈGE — l'éligibilité au support étendu**
Une offre de support étendu n'est jamais universelle. Elle est conditionnée : édition du produit, version précise, mode de gestion de la machine, type de licence, parfois zone géographique. Budgéter une prolongation sans avoir vérifié **ligne à ligne** l'éligibilité de son propre parc est une erreur fréquente et coûteuse : elle se découvre au moment où l'échéance est déjà là, sans plan B.

⏱ **ÉTAT DE L'ART — le cas d'école (vérifié le 30/07/2026)**
Windows 10 est en fin de support depuis le 14 octobre 2025. Microsoft a prolongé fin juin 2026 son programme de support étendu **grand public** jusqu'au 12 octobre 2027 — mais ce programme est réservé aux **appareils personnels** et exclut explicitement les machines jointes à un annuaire d'entreprise ou gérées par une solution de gestion de flotte. Un parc professionnel géré n'est donc **pas** couvert par cette prolongation et relève d'une offre commerciale distincte, payante, dont la tarification augmente à chaque année reconduite. Deux autres échéances sont à distinguer soigneusement : Windows 10 Entreprise LTSB 2016 (13 octobre 2026) et Windows Server 2016 (12 janvier 2027).
La leçon dépasse le cas Microsoft : **une option de support ne se budgète jamais avant d'avoir vérifié précisément son périmètre et ses conditions d'éligibilité.**
📎 [S-24] — pages officielles de cycle de vie et de support étendu, consultées le 30/07/2026.

#### 2.5 Le monde Windows : ce qu'il faut comprendre du mécanisme

**Le rythme.** Microsoft publie ses correctifs de sécurité le deuxième mardi de chaque mois. Des correctifs hors cycle sont publiés en cas d'urgence. Cette régularité est un avantage : elle permet de planifier des fenêtres récurrentes plutôt que de négocier chaque intervention.

**Le format.** Depuis plusieurs années, les correctifs sont **cumulatifs** : un paquet mensuel contient toutes les corrections des mois précédents. Vous ne « manquez » donc pas un correctif ancien en installant le plus récent. En contrepartie, le paquet est indivisible : vous ne pouvez pas choisir de n'appliquer qu'une seule correction.

**La réversibilité n'est pas garantie.** Le paquet cumulatif intègre également la mise à jour de la pile de maintenance, laquelle n'est pas désinstallable. Cela ne signifie pas que toute mise à jour cumulative soit impossible à retirer : la réversibilité réelle dépend du paquet concerné, de l'état du magasin de composants, des opérations de nettoyage déjà effectuées sur la machine, des prérequis installés et de la nature exacte de la régression rencontrée.

La doctrine opérationnelle qui en découle est prudente, et elle vaut d'être retenue telle quelle :

> **Ne construisez jamais un plan de retour arrière en supposant qu'une mise à jour Windows sera désinstallable.**

Si la désinstallation fait partie de votre plan, **vérifiez-la avant le déploiement**, sur une machine représentative. Et gardez comme plan principal un mécanisme qui ne dépend pas d'elle : instantané de machine virtuelle, sauvegarde restaurable, redéploiement à partir d'une image. Ce point est déterminant au chapitre 18.

🧪 **EN PRATIQUE — connaître l'état réel d'une machine Windows**

```powershell
# Ce que les correctifs installés racontent (liste souvent incomplète)
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10

# La vérité : version + numéro de build + révision (UBR)
Get-ComputerInfo -Property OsName, OsVersion, OsBuildNumber
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" |
    Select-Object ProductName, DisplayVersion, CurrentBuild, UBR

# Redémarrage en attente ? (contrôle partiel : un seul des signaux possibles)
Test-Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending"
```

Le couple **build + révision (UBR)** est l'indicateur principal du niveau de mise à jour cumulative du système. Il ne couvre en revanche ni les applications, ni les composants facultatifs, ni l'environnement de récupération, ni les pilotes, ni les micrologiciels — chacun se vérifie séparément. La liste des correctifs installés, elle, est incomplète sur les versions récentes et ne doit pas servir de preuve.

**Le mécanisme durable : la correction à chaud.** Certaines corrections peuvent être appliquées directement au code en cours d'exécution en mémoire, sans redémarrer. Le principe général est toujours le même : une mise à jour cumulative de référence, avec redémarrage, est installée périodiquement ; entre deux références, les correctifs de sécurité sont appliqués à chaud. Le bénéfice porte sur la disponibilité, pas sur la couverture : certaines catégories de mises à jour restent hors périmètre et continuent d'exiger un redémarrage.

⏱ **ÉTAT DE L'ART — la correction à chaud Windows Server (vérifié le 30/07/2026)**
Pour Windows Server 2025 (éditions Standard et Datacenter), la correction à chaud est disponible sur les machines rattachées à Azure Arc, y compris hors Azure — sur site, en périphérie ou chez un autre fournisseur cloud. **Depuis le 19 mai 2026, ce service est fourni sans coût additionnel** : la facturation par cœur qui s'appliquait auparavant a été supprimée, y compris pour les machines déjà inscrites. Les éditions *Datacenter: Azure Edition* en bénéficient nativement.
Cadence : les mois de référence (janvier, avril, juillet, octobre) installent une mise à jour cumulative complète **avec redémarrage** ; les deux mois suivants reçoivent des correctifs à chaud sans redémarrage — soit environ quatre redémarrages planifiés par an au lieu de douze.
Prérequis notables : version minimale du système, sécurité basée sur la virtualisation activée, et démarrage sécurisé — ce qui relie directement ce dispositif au §3.8.
📌 Hors périmètre de la correction à chaud : plusieurs catégories de mises à jour, notamment les pilotes, les micrologiciels et certains composants applicatifs. La correction à chaud réduit le nombre de redémarrages ; elle ne les supprime pas et ne couvre pas tout le système.
⚠️ Ce bloc illustre pourquoi les offres commerciales ne doivent pas figurer dans le corps du cours : la même fonctionnalité était facturée par cœur onze mois plus tôt. Le **mécanisme** est stable, le **modèle économique** ne l'est pas.
📎 [S-26] — documentation officielle, consultée le 30/07/2026.

#### 2.6 Le monde Linux : paquets, redémarrages et correction à chaud

**Deux grandes familles.** Les distributions dérivées de Debian utilisent le format `.deb` et les outils `apt`/`dpkg` ; celles dérivées de Red Hat utilisent le format `.rpm` et l'outil `dnf`. Les principes sont identiques, la syntaxe diffère.

**La numérotation.** Un numéro de paquet complet se lit ainsi : `1.2.3-4+deb12u2`. La partie `1.2.3` est la version amont, `-4` la révision de l'empaquetage, `+deb12u2` la révision de sécurité de l'éditeur. C'est cette dernière partie qui bouge lors d'un correctif de sécurité, et c'est elle que vous devez comparer (voir §2.2).

Un mécanisme piège existe également : la notion d'**époque**, un préfixe rarement visible (`1:1.2.3`) qui prend le pas sur tout le reste dans les comparaisons de version. Un outil de corrélation qui l'ignore peut conclure à tort qu'un paquet est plus ancien qu'il ne l'est.

**Le redémarrage des services.** C'est le point le plus souvent négligé sous Linux, précisément parce que le système, lui, n'a pas besoin de redémarrer.

🧪 **EN PRATIQUE — identifier ce qui doit être redémarré après une mise à jour**

```bash
# Famille Debian / Ubuntu
sudo apt install needrestart
sudo needrestart -r l          # liste les services utilisant du code obsolète

# Famille RHEL / Rocky / Alma
sudo dnf install dnf-utils
needs-restarting -s            # services concernés
needs-restarting -r            # le système requiert-il un redémarrage complet ?

# Vérification indépendante : processus utilisant des fichiers supprimés
sudo lsof -n | grep -i 'DEL.*\.so' | awk '{print $1, $2}' | sort -u
```

**La correction à chaud du noyau.** Plusieurs éditeurs proposent d'appliquer des correctifs de sécurité au noyau **sans redémarrer**, via un abonnement. C'est un outil précieux pour les systèmes à forte contrainte de disponibilité, mais son périmètre est étroit et doit être compris :

📌 **LIMITES — ce que la correction à chaud du noyau ne fait pas**
- Elle ne couvre **que le noyau**, pas les bibliothèques ni les services applicatifs, qui représentent la majorité des vulnérabilités exploitées.
- Elle ne couvre qu'une **partie** des vulnérabilités du noyau : certaines corrections sont structurellement inapplicables à chaud.
- Elle **diffère** le redémarrage, elle ne le supprime pas : un redémarrage reste nécessaire à échéance, et une machine qui n'a pas redémarré depuis 700 jours pose d'autres problèmes (dérive de configuration non testée, démarrage non validé, systèmes de fichiers jamais vérifiés).
- Elle repose sur un **abonnement payant** dont le périmètre de versions couvertes doit être vérifié.

✅ **BONNE PRATIQUE (P1)** — Traitez la correction à chaud comme un moyen de **gagner du temps sur la fenêtre**, pas comme une dispense de redémarrage. Fixez une durée maximale de fonctionnement sans redémarrage (par exemple 90 jours) et suivez-la comme un indicateur à part entière.

#### 2.7 Équipements réseau et de sécurité : le maintien le plus risqué

Pare-feu, routeurs, commutateurs, passerelles d'accès distant, répartiteurs de charge : ces équipements concentrent trois caractéristiques qui en font le point le plus délicat du MCS.

**Ils sont exposés.** Beaucoup sont, par construction, joignables depuis Internet. C'est précisément leur fonction.

**Ils sont monolithiques.** Vous ne corrigez pas un composant : vous remplacez l'image logicielle complète. Toute mise à jour est donc une montée de version, avec son risque fonctionnel propre.

**Ils imposent une interruption.** Le redémarrage est presque toujours nécessaire, et il coupe le trafic.

Deux mécanismes atténuent ce dernier point.

**La double partition d'image.** La plupart des équipements professionnels stockent deux images logicielles. Vous installez la nouvelle sur la partition inactive, vous basculez au redémarrage, et en cas d'échec vous revenez à la précédente. C'est le seul véritable retour arrière du domaine, et il faut le tester avant d'en dépendre.

**La haute disponibilité.** Sur un couple d'équipements redondants, la séquence est toujours la même : mettre à jour le membre passif, vérifier, basculer le trafic, mettre à jour l'ancien membre actif, rebasculer. Cette séquence n'est **pas** sans effet : selon la conception du cluster et le degré de synchronisation d'état entre les membres, la bascule peut entraîner la perte des sessions établies — certains équipements synchronisent les tables de sessions, d'autres non, et le comportement diffère souvent selon les protocoles. Par ailleurs, les deux membres fonctionnent temporairement dans des versions différentes, ce que tous les constructeurs ne supportent pas. Ces deux points se vérifient dans la documentation **avant** l'intervention, pas pendant.

⚠️ **PIÈGE — la doctrine « toujours N-1 » appliquée sans nuance**
Beaucoup d'organisations se donnent pour règle de rester une version derrière la dernière publiée, afin d'éviter les régressions. La règle est raisonnable en régime normal. Elle devient dangereuse dans deux cas : quand la version N-1 est justement celle qui contient la faille exploitée, et quand l'écart s'installe et devient N-3 ou N-4 sans que personne ne le mesure. **Une doctrine de version doit être une décision datée et revue, pas une habitude.**

#### 2.8 Identité : ce qu'un correctif ne corrigera jamais

Les services d'annuaire — annuaire d'entreprise sur site, annuaire d'identité en ligne — appellent une distinction fondamentale.

**Ce qu'un correctif corrige** : les vulnérabilités du logiciel d'annuaire lui-même.

**Ce qu'un correctif ne corrige pas** : tout ce qui s'est accumulé dans les données de l'annuaire depuis sa création. Comptes de personnes parties depuis des années, comptes de service créés pour un projet abandonné, délégations d'administration accordées lors d'une migration en 2014, appartenances à des groupes privilégiés jamais revues, protocoles d'authentification anciens laissés actifs pour un logiciel qui n'existe plus.

Cette accumulation porte un nom dans ce cours : la **dette de configuration d'annuaire**. Elle ne se dégrade pas toute seule, elle **croît** toute seule, à chaque projet, à chaque incident résolu dans l'urgence, à chaque migration. Aucune mise à jour ne la réduira. Le chapitre 24 y est consacré.

⚠️ **PIÈGE — le correctif à activation différée**
Certaines corrections de sécurité importantes ne s'activent pas à l'installation. L'éditeur les livre d'abord en mode « observation » — la nouvelle règle est appliquée mais les cas non conformes sont seulement journalisés, pour ne pas casser les environnements — puis annonce une date à laquelle le mode « application » deviendra obligatoire.

Ces déploiements en plusieurs phases sont un piège classique : l'organisation installe le correctif, coche la case, et découvre plusieurs mois plus tard, à la date d'application forcée, que des authentifications échouent parce que le travail intermédiaire — analyser les journaux, corriger les cas non conformes — n'a jamais été fait.

✅ **BONNE PRATIQUE (P0)** — Pour tout correctif comportant un calendrier d'application en plusieurs phases, créez immédiatement **deux** échéances dans votre suivi : la date d'installation, et la date de bascule en mode application. Entre les deux, une tâche explicite d'analyse des journaux d'observation, avec un propriétaire nommé. Un correctif resté en mode observation peut apporter une protection partielle — certaines vérifications sont déjà actives — mais **il n'apporte pas encore la protection complète attendue**, et c'est bien celle-ci que vous croyez avoir déployée.

#### 2.9 La journalisation minimale pour prouver qu'un correctif est appliqué

Nous arrivons à l'exigence la plus négligée du socle technique. Vous devez pouvoir répondre, plusieurs mois après, à cette question : *cette correction a-t-elle été appliquée sur cet actif, et quand ?*

> **Un journal n'est pas une preuve parce qu'il existe.** Il devient une preuve lorsqu'on peut établir son intégrité, son périmètre et son contexte — c'est-à-dire ce qu'il couvre, ce qu'il ne couvre pas, et qu'il n'a pas été modifié.

**Trois niveaux de preuve, de la plus faible à la plus forte :**

| Niveau | Nature | Valeur | Faiblesse |
|---|---|---|---|
| 1 — Déclaratif | « Nous appliquons les correctifs chaque mois » | Nulle en audit | Aucune donnée |
| 2 — Console centrale | Rapport de l'outil de déploiement | Correcte | Ne couvre que les actifs connus de l'outil, et masque les machines injoignables |
| 3 — État constaté sur l'actif | Version ou révision relevée directement sur la machine, horodatée | Forte | Nécessite une collecte propre |

L'état constaté sur l'actif est **généralement la preuve technique la plus forte**, parce qu'il est indépendant de l'outil qui a réalisé le déploiement. Cela ne disqualifie pas le niveau 2 : un rapport de console constitue une preuve parfaitement recevable dès lors que trois conditions sont établies — le **périmètre** couvert par l'outil est défini et rapproché du périmètre de référence, l'**intégrité** du rapport est assurée (extraction datée, non retouchée), et la **liste des actifs non joignables** est fournie. Ce qui n'est pas recevable, c'est un rapport de console présenté sans ces trois éléments.

🧪 **EN PRATIQUE — les sources de preuve natives**

```bash
# Debian / Ubuntu : journal complet des opérations de paquets
grep -E "upgrade|install" /var/log/dpkg.log | tail -20
zcat -f /var/log/apt/history.log* | grep -A3 "Start-Date"

# RHEL / Rocky / Alma : historique des transactions
dnf history list | head -20
dnf history info <ID>          # contenu détaillé d'une transaction
```

```powershell
# Windows : journal d'installation des mises à jour
Get-WinEvent -LogName Setup -MaxEvents 50 |
    Where-Object { $_.Id -in 1,2,4 } |
    Select-Object TimeCreated, Id, Message
```

✅ **BONNE PRATIQUE (P0) — les six champs d'une preuve exploitable**
Identifiant de l'actif · état constaté (version, révision) · date et heure de la constatation · méthode de collecte · périmètre couvert par la collecte · **liste explicite des actifs non joignables au moment de la collecte**.
Le dernier champ est celui qu'on oublie, et c'est celui que l'auditeur demandera. Un rapport indiquant « 100 % conforme » sur les machines répondantes, sans mentionner les 140 machines injoignables, n'est pas une preuve : c'est une omission.

🔴 **FIL ROUGE — décembre 2025 : trois chiffres qui ne concordent pas**

Six semaines après la note de Claire Nadeau à la direction générale (§1.9), Malik Ferhaoui rend son premier inventaire. Il a croisé trois sources.

| Source | Ce qu'elle mesure | Effectif |
|---|---|---|
| **C** — Base de gestion de configuration (tenue manuellement) | Ce que l'entreprise **croit** posséder | 187 |
| **K** — Console de déploiement des correctifs | Ce qui est **effectivement géré** par le canal de correction | 164 |
| **D** — Découverte réseau + inventaire de l'hyperviseur | Ce qui **répond** réellement | 210 |

Trois sources, trois chiffres. Le réflexe naturel est de demander « lequel est le bon ? ». C'est la mauvaise question : aucun ne l'est, et c'est la **structure des écarts** qui porte l'information.

**Table de réconciliation des ensembles**

| Ensemble | Description | Effectif |
|---|---|---|
| K ⊆ C | Déclarées **et** gérées par la console | 164 |
| C ∩ D, hors K | Déclarées et actives, mais **jamais atteintes** par la console | 12 |
| C \ D | Déclarées mais ne répondant plus : éteintes sans décommissionnement | 11 |
| **C** (total) | 164 + 12 + 11 | **187** |
| C ∩ D | Déclarées et actives (164 + 12) | 176 |
| D \ C | Actives mais **non déclarées** | 34 |
| **D** (total) | 176 + 34 | **210** |
| **C ∪ D — périmètre de référence** | 176 actives déclarées + 34 actives non déclarées + 11 à décommissionner | **221** |

Les **23 machines** présentes dans la base de gestion mais absentes de la console se décomposent donc en deux populations très différentes : **12 machines actives** qui n'ont jamais reçu de correctif par ce canal — dont trois serveurs de préproduction contenant une copie des données de production (chapitre 28) — et **11 machines éteintes** dont les enregistrements réseau et les comptes de service existent toujours (chapitre 35).

Les **34 machines actives non déclarées** se répartissent en 19 machines créées pour des tests et jamais enregistrées, 13 appliances virtuelles livrées par des éditeurs métier (§3.1), et 2 serveurs appartenant à une filiale rattachée en 2022.

**Le chiffre qui compte, et les trois qu'on lui préfère habituellement.** La console affiche 97 % de conformité. Ce chiffre est exact — et il ne veut presque rien dire tant qu'on ne précise pas son dénominateur.

| Indicateur | Calcul | Valeur |
|---|---|---|
| Conformité **dans la population mesurée** | 159 conformes / 164 gérées | **97 %** |
| **Couverture** de la console sur les actifs en service | 164 gérées / 210 actives | **78 %** |
| **Ratio confirmé conforme** sur les actifs en service | 159 / 210 | **≈ 76 %** |
| **Ratio confirmé conforme** sur le périmètre maître | 159 / 221 | **≈ 72 %** |
| **Non mesuré** | 46 actifs en service, hors console | **22 % des actifs en service** |

⚠️ Les deux lignes de ratio sont **conservatrices** : elles traitent tout actif non mesuré comme non conforme. C'est une hypothèse de prudence, pas une mesure — la conformité réelle des 46 machines hors console est **inconnue**, et c'est précisément l'information qui manque (Annexe K.2).

⚠️ Notez le glissement de vocabulaire, qui est l'erreur la plus fréquente du domaine : **couverture** et **conformité** ne sont pas la même chose. La couverture mesure ce que l'outil atteint ; la conformité mesure l'état de ce qu'il atteint. Une organisation peut afficher 100 % de conformité sur 40 % de couverture, et l'annoncer de bonne foi. Les définitions rigoureuses de ces deux indicateurs figurent au §38.2 et en Annexe K.

**Décision prise.** Aucun achat d'outil. Trois règles sont posées : le périmètre de référence sera désormais l'union des sources, jamais l'une d'elles seule ; tout indicateur devra afficher son dénominateur et le nombre d'actifs non joignables ; et les mots « couverture » et « conformité » ne seront plus employés l'un pour l'autre dans aucun document interne.

**Livrable de l'épisode.** Un fichier de réconciliation à trois colonnes, avec pour chaque écart une cause identifiée et un propriétaire nommé — c'est exactement l'exercice du mini-lab 2, au chapitre 10.

→ La suite en 🔴 §3.9, quand l'inventaire rencontre les environnements que la découverte réseau ne voit pas.

#### 2.10 📌 Ce que ce cours ne couvre pas, et où l'acquérir

Par honnêteté envers le lecteur débutant, voici ce que ce chapitre suppose acquis ou n'enseigne pas :

| Domaine | Ce que le cours suppose | Où combler |
|---|---|---|
| Administration système | Savoir se connecter à une machine et lire un journal | Cours d'administration Linux/Windows |
| Réseau | Comprendre adressage, routage, filtrage | Cours réseau généraliste |
| Développement | Rien n'est supposé ; les notions utiles sont expliquées aux ch. 6 et 25 | — |
| Cryptographie | Rien n'est supposé ; les notions utiles sont expliquées au ch. 24 | — |
| Gestion de vulnérabilités | **Rien n'est supposé** : c'est l'objet du chapitre 4 | — |

Le cours est autonome sur son sujet. Il ne l'est pas sur les disciplines voisines, et prétendre le contraire vous desservirait.

#### Synthèse mentale du chapitre 2

Un système est un empilement de couches mises à jour par des mécanismes différents, à des rythmes différents, souvent par des personnes différentes — et la couche embarquée dans les applications n'est mise à jour par personne. Un correctif suit un trajet long, de l'amont jusqu'au chargement effectif du code corrigé, et il n'est efficace qu'au bout de ce trajet. Le rétroportage explique qu'un numéro de version amont ne dit rien de la présence d'une faille sur une distribution à support long : c'est la source de faux positifs la plus structurelle du domaine. Les chaînes de confiance cryptographiques garantissent l'origine d'un paquet, pas son innocuité, et leur rupture est silencieuse. Sous Windows, la réversibilité d'un correctif ne se suppose jamais ; sous Linux, l'installation ne suffit pas sans redémarrage des services concernés. Un annuaire ne se corrige pas par mise à jour : sa dette de configuration croît toute seule. Enfin, une preuve exploitable comporte six champs, dont la liste des actifs non joignables — celui qu'on oublie et que l'auditeur demandera.

**Trois questions de vérification**

1. Un scanner signale une bibliothèque en version 3.0.11 alors que la faille est corrigée en 3.0.15 amont. Quelles vérifications faites-vous, dans quel ordre, et quelle source fait finalement foi ?
2. Vous venez d'appliquer un correctif de bibliothèque sur cinquante serveurs Linux. Le travail est-il terminé ? Que vérifiez-vous, et avec quelle commande ?
3. Votre plan de retour arrière pour une campagne de correctifs Windows repose sur la désinstallation du paquet. Pourquoi est-ce fragile, et par quoi le remplacez-vous ?

---

### Chapitre 3 — Socle technique 2 : virtualisation, conteneurs, cloud, IaC, OT et micrologiciels

Le chapitre 2 décrivait le maintien d'une machine. Celui-ci décrit le maintien de tout ce qui n'est plus une machine : couches d'abstraction, environnements éphémères, ressources dont vous ne possédez pas le matériel, et systèmes industriels qui obéissent à d'autres lois.

**Ces technologies n'ont rien en commun techniquement.** L'hyperviseur, le conteneur, l'orchestrateur, le cloud, l'automate et le micrologiciel appartiennent à des mondes séparés, avec des équipes, des outils et des cultures différentes. Ce qui les rassemble ici est ailleurs : **chacune modifie la façon dont le maintien est réalisé, et déplace la ligne qui sépare ce que vous devez faire de ce qu'un autre fait pour vous.**

Le fil conducteur est donc unique : **à chaque couche d'abstraction ajoutée correspond une frontière de responsabilité, et c'est toujours sur ces frontières que le MCS échoue.**

#### 3.1 Hyperviseurs et appliances virtuelles

Un hyperviseur héberge des dizaines de machines virtuelles. Il faut y distinguer **quatre objets à maintenir**, souvent confondus :

| Objet | Ce que c'est | Interruption induite |
|---|---|---|
| L'hôte | Le système de l'hyperviseur lui-même | Migration à chaud des machines, puis redémarrage de l'hôte |
| Les invités | Les systèmes des machines virtuelles | Chacun selon sa nature (voir ch. 2) |
| Le plan de gestion | La console qui pilote l'ensemble | Interruption de l'administration, pas de la production |
| Le micrologiciel du matériel | Serveur physique sous l'hyperviseur | Redémarrage physique complet |

**Le bon côté.** La migration à chaud permet de déplacer les machines virtuelles d'un hôte à l'autre sans interruption, donc de mettre à jour les hôtes sans coupure de service. C'est l'un des rares cas où le MCS ne coûte pas de disponibilité — à condition d'avoir provisionné la capacité nécessaire pour fonctionner avec un hôte en moins.

**Le mauvais côté.** Le plan de gestion est un actif de **niveau 0** : quiconque le contrôle contrôle toutes les machines virtuelles, leurs disques et leurs sauvegardes. Il est régulièrement en retard de plusieurs versions, parce que le mettre à jour « n'apporte rien aux métiers » et interrompt l'outil que les administrateurs utilisent tous les jours. C'est une inversion complète des priorités : cet actif doit être parmi les premiers maintenus, pas parmi les derniers.

⚠️ **PIÈGE — l'appliance virtuelle**
Une *appliance* virtuelle est une machine virtuelle préconstruite livrée par un éditeur. Elle contient un système d'exploitation complet que **vous ne maintenez pas** : l'éditeur interdit généralement d'y appliquer les correctifs du système, et fournit ses propres mises à jour, souvent moins fréquentes. Vous héritez donc de son rythme, de ses composants tiers et de ses éventuels retards. Traitez chaque appliance comme un actif dont le MCS est délégué, avec les exigences contractuelles correspondantes (chapitre 13).

#### 3.2 Conteneurs : on ne corrige pas, on reconstruit

Un conteneur est un processus isolé, exécuté à partir d'une **image** : une pile de couches en lecture seule contenant le système de fichiers minimal nécessaire à l'application.

Le changement de paradigme est total, et il faut le comprendre pour le reste du cours :

> **On ne met pas à jour un conteneur. On reconstruit son image, et on remplace le conteneur.**

Se connecter à un conteneur en fonctionnement pour y lancer une mise à jour est possible techniquement, et à proscrire : la correction disparaîtra au premier redémarrage, et l'écart entre l'image de référence et la réalité en production deviendra invisible.

**La chaîne de correction devient donc :**

```
Correctif publié pour un composant
   → mise à jour de l'image de base
   → reconstruction de l'image applicative
   → nouvelle version publiée dans le registre
   → redéploiement progressif des conteneurs
```

Cette chaîne est bien plus rapide et plus fiable qu'une correction classique — quand elle est automatisée. Elle est catastrophique quand elle ne l'est pas : une image construite il y a deux ans et jamais reconstruite accumule silencieusement toutes les vulnérabilités publiées depuis, et rien dans le système d'exploitation hôte ne le signalera.

⚠️ **PIÈGE — l'étiquette mouvante**
Une étiquette d'image comme `:latest` ne désigne pas un contenu figé : elle pointe vers ce que le registre considère comme la dernière version, à un instant donné. Deux déploiements « identiques » à une semaine d'écart peuvent donc contenir des composants différents. Inversement, une étiquette figée pour garantir la reproductibilité gèle aussi les vulnérabilités.
**La bonne pratique** consiste à référencer une empreinte immuable pour la reproductibilité, **et** à disposer d'un processus qui met à jour cette référence à cadence maîtrisée. La reproductibilité sans cadence de reconstruction est une machine à fabriquer de l'obsolescence.

✅ **BONNE PRATIQUE (P1)** — Définissez et suivez une **cadence maximale de reconstruction** des images (par exemple : toute image en production a été reconstruite il y a moins de 30 jours). Cet indicateur préventif remplace avantageusement des dizaines de constats individuels dans le pilotage courant — sans dispenser de l'analyse de vulnérabilités : une image reconstruite hier peut embarquer une dépendance vulnérable, et une image plus ancienne peut porter un correctif rétroporté.

#### 3.3 Kubernetes : la cadence vous est imposée

Kubernetes orchestre des conteneurs sur un ensemble de machines. Trois particularités le rendent structurant pour le MCS.

**Un rythme de publication soutenu et un support court.** Le projet publie environ trois versions mineures par an. Chaque version mineure reçoit **environ douze mois de support standard, suivis d'environ deux mois de maintenance limitée** — soit près de quatorze mois avant la fin de vie de la branche. Concrètement : **rester sur une version pendant deux ans n'est pas une option**, c'est une sortie de support. Le MCS d'un cluster n'est pas une activité occasionnelle, c'est un processus permanent, à inscrire au calendrier au même titre qu'une campagne de correctifs.
Les offres managées appliquent leurs propres calendriers, parfois plus courts, parfois assortis d'un support étendu payant : ce point est traité au chapitre 30. 📎 [S-27]

**Un écart de version encadré.** Les composants d'un cluster ne peuvent pas diverger arbitrairement : les règles d'écart autorisé entre le serveur d'API et les nœuds imposent un ordre de mise à jour et un nombre maximal de versions de retard. On met à jour le plan de contrôle d'abord, les nœuds ensuite, jamais l'inverse, et jamais en sautant plusieurs versions d'un coup.

**Des ruptures d'interface programmées.** Chaque version retire des interfaces dépréciées. Une mise à jour peut donc casser des déploiements parfaitement fonctionnels, non par régression, mais parce que le format de description qu'ils utilisent n'existe plus. Ce risque est **prévisible et annoncé longtemps à l'avance** : c'est un travail d'anticipation, pas un aléa.

📌 **LIMITES — ce qu'un service managé ne vous enlève pas**
Un cluster managé chez un fournisseur cloud prend en charge le plan de contrôle. Restent intégralement à votre charge : le choix du moment de la montée de version (dans la fenêtre imposée), la mise à jour des images de nœuds, les composants additionnels installés dans le cluster, la compatibilité de vos propres déploiements, et la migration des interfaces dépréciées. Et si vous ne décidez pas dans la fenêtre, **le fournisseur décidera pour vous** : c'est le sujet du chapitre 30.

#### 3.4 Cloud : la frontière de responsabilité, service par service

Le modèle dit de « responsabilité partagée » est souvent cité et rarement décodé. Voici sa traduction opérationnelle.

| Modèle | Le fournisseur maintient | Vous maintenez |
|---|---|---|
| **Infrastructure (IaaS)** | Matériel, hyperviseur, réseau physique | **Tout** le système invité, comme une machine classique |
| **Plateforme (PaaS)** | Système et environnement d'exécution | Le **choix de version** et sa migration avant fin de support, votre code, vos dépendances, la configuration |
| **Logiciel (SaaS)** | L'application entière | Configuration, identités, droits, extensions, intégrations tierces, données |
| **Fonctions (*serverless*)** | Exécution et système | Version de l'environnement d'exécution, dépendances applicatives, permissions attachées |

🖼 **SCHÉMA — Empilement des couches et frontières de responsabilité.** *Pile verticale : matériel · micrologiciel · hyperviseur · système · runtime · bibliothèque · application, avec une ligne de démarcation mobile selon le modèle d'exécution.*

##### Le tableau à mémoriser

| Modèle d'exécution | Qui met à jour quoi |
|---|---|
| **Machine physique** | Vous : micrologiciel, système, applications |
| **Machine virtuelle** | Vous pour l'invité · l'équipe hyperviseur pour l'hôte et le plan de gestion |
| **Conteneur** | Vous reconstruisez l'image · l'équipe plateforme maintient les nœuds |
| **Infrastructure cloud (IaaS)** | Vous : tout l'invité · le fournisseur : matériel et hyperviseur |
| **Plateforme cloud (PaaS)** | Le fournisseur : système et exécution · **vous : le choix de version et sa migration avant échéance** |
| **Logiciel en ligne (SaaS)** | Le fournisseur : l'application · **vous : configuration, identités, extensions, intégrations** |
| **Fonctions (serverless)** | Le fournisseur : exécution · vous : version d'environnement, dépendances, permissions |
| **Appliance fournisseur** | Le fournisseur, à son rythme · vous : rien, sauf l'exposition |
| **Système industriel** | Le constructeur valide · vous appliquez pendant les arrêts |

⚠️ Les deux lignes qui produisent le plus d'angles morts sont **PaaS** — on croit que le fournisseur gère la version alors qu'il ne gère que l'exécution — et **appliance**, où l'on n'a aucune prise sauf sur l'exposition.

Trois enseignements en découlent.

**1. La responsabilité diminue, elle ne disparaît jamais.** Même en SaaS pur, la configuration du service, les comptes d'administration, les autorisations accordées à des applications tierces et les connecteurs restent à vous — et c'est précisément là que se produisent la majorité des incidents cloud. Chapitre 31.

**2. En PaaS, vous ne choisissez plus *si* vous migrez, seulement *quand*.** Le fournisseur annonce la fin de support d'une version d'environnement d'exécution ou de moteur de base de données, puis — selon le service et le contrat — impose une échéance, applique lui-même la migration, propose un support étendu payant, ou laisse le service fonctionner sans support. L'anticipation est le seul levier disponible dans les quatre cas.

**3. Les frontières se déplacent sans vous.** Un fournisseur peut modifier un comportement par défaut, retirer une option ou réinitialiser un paramètre de sécurité lors d'une mise à jour de son service. Votre configuration validée l'an dernier n'est pas garantie identique aujourd'hui. La veille sur les notes de version des services utilisés est une activité de MCS à part entière, traitée au chapitre 31.

#### 3.5 Infrastructure décrite par le code et immutabilité

Deux idées, souvent confondues, qui changent profondément la façon de corriger.

**L'infrastructure décrite par le code** consiste à définir les ressources dans des fichiers versionnés plutôt que par des actions manuelles. Bénéfice pour le MCS : la configuration devient lisible, comparable et reproductible. Vous pouvez répondre à la question « quelle est la configuration de référence ? » — ce qui est impossible dans un environnement construit à la main.

**L'immutabilité** consiste à ne jamais modifier un serveur en fonctionnement : pour appliquer un correctif, on construit une nouvelle image, on déploie de nouvelles instances, et on retire les anciennes. C'est le modèle des conteneurs, transposé aux machines.

Ce que l'immutabilité apporte au MCS est considérable : la dérive de configuration locale disparaît largement, le retour arrière est simplifié — redéployer l'image précédente, à condition que données, schémas et dépendances restent compatibles —, et la correction devient un acte de déploiement standard plutôt qu'une opération d'exception.

⚠️ **PIÈGE — le code d'infrastructure est lui-même un actif à maintenir**
Les modules réutilisés, les connecteurs vers les fournisseurs cloud et les outils de description ont leurs propres versions, leurs propres vulnérabilités et leurs propres fins de support. Par ailleurs, l'écart entre ce que décrit le code et ce qui existe réellement — les ressources créées à la main dans l'urgence — est une forme de dérive particulièrement trompeuse, parce que le code donne l'illusion de la maîtrise. Chapitre 23.

#### 3.6 Chaînes de construction et dépendances applicatives

Dans une application moderne, une part souvent importante — parfois majoritaire — du code exécuté n'a pas été écrite par l'équipe qui la maintient : bibliothèques externes, elles-mêmes dépendantes d'autres bibliothèques. La proportion exacte varie fortement selon le langage, l'écosystème et la maturité du projet ; ce qui est constant, c'est que cette part est rarement inventoriée.

**Deux notions à connaître dès maintenant.**

Le **fichier de verrouillage** enregistre la version exacte de chaque dépendance effectivement utilisée. Il garantit que la construction d'aujourd'hui produit le même résultat que celle d'il y a six mois. C'est indispensable à la reproductibilité — et c'est aussi un mécanisme de gel des vulnérabilités, exactement comme l'étiquette d'image figée du §3.2. Même remède : une cadence de mise à jour maîtrisée.

Les **dépendances transitives** sont celles que vous n'avez jamais choisies : votre application utilise A, qui utilise B, qui utilise C. La faille sera dans C. Vous ne pourrez la corriger qu'en attendant que B mette à jour C, sauf à forcer une résolution, ce qui comporte son propre risque.

**Les machines de construction sont des actifs à maintenir.** Les agents d'exécution des chaînes d'intégration disposent souvent d'accès étendus : registres d'images, environnements de déploiement, secrets. Ce sont des cibles de premier ordre, et ils échappent presque toujours à l'inventaire du parc. Le chapitre 28 leur est consacré.

#### 3.7 Systèmes industriels (OT / ICS) : d'autres lois

Le monde industriel — automates, supervision, systèmes d'exécution de la production — obéit à des contraintes qui inversent plusieurs réflexes du monde bureautique.

**Le modèle de référence.** Le modèle de Purdue décrit une architecture en niveaux, du plus proche du terrain au plus proche de la bureautique :

```
Niveau 0   Capteurs, actionneurs — le procédé physique
Niveau 1   Automates, régulation
Niveau 2   Supervision (IHM), conduite locale
Niveau 3   Gestion de la production (MES), historisation
Niveau 3,5 Zone démilitarisée industrielle
Niveau 4/5 Systèmes d'information de gestion, bureautique
```

L'enjeu de MCS est concentré sur les niveaux 1 à 3, et sur l'étanchéité du niveau 3,5.

**Ce qui change fondamentalement.**

| Dimension | Informatique de gestion | Systèmes industriels |
|---|---|---|
| Contraintes dominantes | Confidentialité et intégrité | **Sûreté des personnes et disponibilité** — l'intégrité y est souvent directement liée à la sûreté |
| Durée de vie d'un équipement | 3 à 7 ans | **15 à 25 ans** |
| Fenêtre d'interruption | Nuit, week-end | **Arrêt de production annuel** |
| Validation d'un correctif | Interne | **Par le constructeur**, sous peine de perte de garantie |
| Conséquence d'une panne | Perte de service | **Risque physique** |

> **Le MCS ne change pas de principes en environnement industriel ; il change de contraintes.** Connaître, observer, décider, corriger, vérifier, prouver : la boucle est identique. Ce sont les fenêtres, les validations et les conséquences d'une erreur qui diffèrent.

**La conséquence pratique.** Appliquer un correctif non validé par le constructeur sur un automate peut faire tomber la garantie, invalider une certification, et — dans le pire des cas — perturber un procédé physique. La démarche du MCS industriel n'est donc pas « corriger plus vite », mais : **maîtriser l'exposition, préparer les correctifs longtemps à l'avance, et les appliquer pendant les arrêts planifiés.** Le chapitre 29 traite ce sujet en profondeur, y compris la chaîne complète de mise à jour hors ligne.

⚠️ **PIÈGE — le scan actif sur réseau industriel**
Un scan de vulnérabilités classique, banal en informatique de gestion, peut faire basculer un automate ancien en défaut : ces équipements ont des piles réseau minimalistes qui supportent mal les sollicitations inattendues. **Ne lancez pas de scan actif sur un réseau industriel sans validation explicite du constructeur ou de l'exploitant, sans test préalable et sans procédure d'arrêt.** La doctrine est : *passif par défaut, actif sous procédure* — un scan actif contrôlé reste possible, il ne s'improvise pas.

#### 3.8 Micrologiciels, objets connectés et chaîne de démarrage

C'est la couche la plus basse, la moins visible, et celle où le retard est le plus important dans la plupart des organisations.

**Ce dont on parle.** Micrologiciel de carte mère (BIOS/UEFI), contrôleur de gestion à distance des serveurs, micrologiciels de disques et de cartes réseau, équipements connectés d'entreprise (impression, vidéosurveillance, contrôle d'accès, visioconférence).

**Pourquoi c'est critique.** Un composant qui s'exécute **avant** le système d'exploitation ne peut pas être surveillé par les protections qui s'exécutent **dans** le système d'exploitation. Une compromission à ce niveau survit à une réinstallation complète.

**Pourquoi c'est négligé.** La mise à jour est risquée (un échec peut rendre la machine inutilisable), rarement automatisable à grande échelle, souvent invisible des outils d'inventaire, et sans propriétaire clairement désigné entre l'équipe système, l'équipe poste de travail et les achats.

**Les mécanismes de protection à connaître.**

- **Le démarrage sécurisé** vérifie la signature de chaque composant chargé au démarrage, à partir de bases de certificats stockées dans le micrologiciel : une base d'autorisation et une base de révocation.
- **La signature des mises à jour** empêche l'installation d'un micrologiciel non authentique.
- **La protection contre le retour en arrière** empêche de réinstaller une version antérieure vulnérable — mécanisme indispensable, car sans lui un attaquant pourrait simplement « rétrograder » le composant pour retrouver une faille corrigée.

⏱ **ÉTAT DE L'ART — un cas d'école en cours (vérifié le 30/07/2026)**
Les certificats Microsoft de démarrage sécurisé émis en 2011 arrivent à expiration au terme de leurs quinze ans de validité : **KEK CA 2011** le 24 juin 2026, **UEFI CA 2011** le 27 juin 2026, **Windows Production PCA 2011** le 19 octobre 2026. Des certificats émis en 2023 les remplacent.

Ce cas mérite d'être étudié parce qu'il contient à lui seul cinq enseignements de MCS :

1. **La dégradation est silencieuse.** Une machine non mise à jour continue de démarrer normalement. Elle perd seulement la capacité de recevoir de futures révocations — donc toute protection contre les prochains logiciels malveillants de démarrage. Aucun tableau de bord de correctifs ne montrera ce manque.
2. **L'échéance était connue quinze ans à l'avance.** C'est le cas typique du §1.3 : la seule catégorie de dégradation entièrement prévisible est aussi celle qu'on découvre en retard.
3. **La correction dépend d'un tiers.** Sur une partie du parc, la mise à jour requiert une mise à jour de micrologiciel du constructeur. Sans elle, le processus reste en attente.
4. **Forcer la correction peut casser.** Contourner l'attente par une modification manuelle peut provoquer un échec de démarrage ou une demande de clé de récupération de chiffrement de disque. C'est l'illustration exacte du conflit MCO/MCS du §1.2.
5. **L'impact déborde l'éditeur concerné.** Les systèmes non-Windows dont le chargeur de démarrage est signé par la même autorité sont également concernés — une dépendance que peu d'organisations avaient cartographiée.

📎 [S-25] — documentation officielle et billet technique de l'éditeur, consultés le 30/07/2026.

✅ **BONNE PRATIQUE (P1)** — Créez une ligne d'inventaire dédiée aux micrologiciels, avec un propriétaire nommé, et traitez leur mise à jour par anneaux de déploiement comme n'importe quel correctif à risque (chapitre 18). Un parc dont aucun micrologiciel n'a jamais été mis à jour n'a pas « zéro vulnérabilité de micrologiciel » : il a **zéro visibilité**.

#### 3.9 ⚠️ Les cinq endroits systématiquement oubliés

Synthèse des chapitres 2 et 3. Ces cinq zones échappent à presque tous les programmes de MCS naissants, et chacune a fait l'objet d'incidents majeurs documentés.

| # | Zone oubliée | Pourquoi elle échappe | Traité au |
|---|---|---|---|
| 1 | Environnements d'exécution et bibliothèques **embarqués dans les applications** | Hors gestionnaire de paquets, invisibles du système | Ch. 26 |
| 2 | **Plans de gestion** : hyperviseur, console de sauvegarde, outil de déploiement | « Ce n'est pas de la production » — alors que ce sont des actifs de niveau 0 | Ch. 28, 34 |
| 3 | **Micrologiciels** et chaîne de démarrage | Pas d'inventaire, pas de propriétaire, mise à jour risquée | Ch. 27 |
| 4 | **Modèles et images de référence** : images maîtres, modèles de machines virtuelles, instantanés | Une machine neuve naît vulnérable si son modèle ne l'est pas | Ch. 28 |
| 5 | **Configuration des services en ligne** : paramètres, extensions, connecteurs, autorisations déléguées | « C'est du SaaS, c'est maintenu » | Ch. 31 |

🔴 **FIL ROUGE — janvier 2026 : ce que la découverte réseau ne voyait pas**

L'inventaire de décembre (§2.9) aboutissait à un périmètre de référence de 221 actifs, dont 210 en service. En janvier, Claire Nadeau demande une seconde passe, orientée cette fois par les cinq zones ci-dessus plutôt que par le balayage réseau. Le résultat modifie l'échelle du problème.

- **Nantes (recherche et développement)** : quatre agents d'exécution de la chaîne d'intégration, créés par l'équipe de développement, hors du domaine, disposant d'un accès en écriture au registre d'images. Aucun n'apparaissait dans les 210 actifs en service : ils sont créés et détruits automatiquement, et n'existent souvent pas au moment où l'inventaire passe.
- **Saint-Étienne (usine)** : Thomas Berger, responsable maintenance, fournit un inventaire papier. Onze postes de supervision, dont deux sur des systèmes dont le support a pris fin en 2020, et trois automates dont le fournisseur ne publie plus de mise à jour depuis 2019. Aucun n'a jamais été scanné — et Thomas est formel : aucun ne le sera sans validation préalable.
- **Applications hébergées** : le service achats recense 38 abonnements à des services en ligne. Sept disposent de connecteurs avec accès en lecture à la messagerie de l'entreprise, autorisés entre 2019 et 2023, jamais revus depuis.
- **Modèles de machines virtuelles** : le modèle utilisé pour créer tout nouveau serveur Windows date de mars 2024. Chaque serveur créé depuis naît avec vingt-deux mois de correctifs de retard, rattrapés — quand ils le sont — au premier passage de la console de déploiement.
- **Micrologiciels** : aucune donnée. Le sujet n'a jamais eu de propriétaire.

**La décision qui compte.** Claire ne cherche pas à tout traiter. Elle formule une règle qui structurera tout le programme : *un actif sans propriétaire nommé n'est pas un actif maintenu, quelle que soit la qualité de l'outillage.* Chaque zone découverte reçoit un nom de propriétaire avant toute action technique — Malik pour les modèles et les micrologiciels, Yann Prigent pour les agents de construction, Thomas Berger pour l'usine, le service achats pour les abonnements en ligne.

**Livrable de l'épisode.** Un périmètre de référence en cinq domaines, avec un propriétaire par domaine, et une case explicite « micrologiciels : non couvert, propriétaire désigné, échéance de première mesure ». Déclarer un domaine non couvert **est** un livrable : c'est ce qui le rend finançable.

→ La suite en 🔴 §4.11, quand il faudra qualifier les premiers constats issus de ce périmètre.

#### Synthèse mentale du chapitre 3

Chaque couche d'abstraction ajoute une frontière de responsabilité, et c'est sur ces frontières que le MCS échoue. Un hyperviseur impose de distinguer quatre objets à maintenir, dont un plan de gestion de niveau 0 souvent laissé en retard. Un conteneur ne se corrige pas : on reconstruit son image, ce qui rend la cadence de reconstruction plus informative que des dizaines de constats individuels. Un cluster d'orchestration impose son propre rythme, avec un support d'environ quatorze mois par version mineure et des ruptures d'interface annoncées à l'avance. Dans le cloud, la responsabilité diminue avec le niveau de service mais ne disparaît jamais, et les frontières se déplacent sans vous. L'infrastructure décrite par le code et l'immutabilité transforment la correction en déploiement standard — au prix de maintenir le code d'infrastructure lui-même. Le monde industriel inverse les priorités : disponibilité et sûreté des personnes d'abord, équipements sur quinze à vingt-cinq ans, correctifs validés par le constructeur, fenêtres annuelles. Enfin, la couche des micrologiciels est la plus basse, la plus critique et la moins inventoriée : sans propriétaire désigné, elle n'a pas zéro vulnérabilité, elle a zéro visibilité.

**Trois questions de vérification**

1. Votre organisation utilise une base de données managée chez un fournisseur cloud. Citez trois activités de MCS qui restent intégralement à votre charge.
2. Une image de conteneur en production a été construite il y a quatorze mois et n'a jamais été reconstruite. Le système d'exploitation des nœuds est parfaitement à jour. Où est le problème, et quel indicateur unique l'aurait révélé ?
3. Un responsable d'usine refuse tout scan de vulnérabilités sur son réseau industriel. A-t-il tort ? Que proposez-vous à la place, et quelle est la contrepartie de votre proposition ?

---


### Chapitre 4 — Socle vulnérabilités : identifiants, scores, écosystème

> ⚠️ **Avant de commencer.** Ce chapitre présente une dizaine de sigles en quelques pages. **N'essayez pas de les mémoriser à la première lecture.** Quatre d'entre eux suffisent au travail quotidien — ils sont identifiés au §4.10 — et les autres se consultent au besoin. Ce qui compte ici n'est pas de retenir les acronymes, c'est de comprendre **quelle question chacun répond, et laquelle il ne répond pas**.

Ce chapitre est le pivot du cours. Il installe le vocabulaire que tout le reste utilise, et il vous apprend surtout à **ne pas croire les chiffres** que produit cet écosystème — non parce qu'ils mentent, mais parce qu'ils ne mesurent presque jamais ce qu'on croit qu'ils mesurent.

Aucune connaissance préalable n'est supposée. Si vous n'avez jamais lu un bulletin de sécurité, vous saurez le faire à la fin.

#### 4.1 Vocabulaire : six mots qu'on confond en permanence

| Terme | Définition précise | Ce qu'il n'est pas |
|---|---|---|
| **Faiblesse** | Un type de défaut de conception ou de programmation, décrit indépendamment de tout produit — par exemple « absence de vérification des droits avant une action » | Ce n'est pas une faille dans un logiciel précis |
| **Vulnérabilité** | L'instance concrète d'une faiblesse dans un produit et une version donnés | Ce n'est pas un risque : elle peut être inatteignable chez vous |
| **Exposition** | Le fait qu'un attaquant puisse **atteindre** le composant vulnérable | Une vulnérabilité sans exposition n'est pas exploitable |
| **Exploit** | Le code ou la procédure qui transforme la vulnérabilité en effet concret | Son existence publique ne prouve pas qu'il fonctionne partout |
| **Exploitation active** | L'observation, dans le monde réel, d'attaquants utilisant cette vulnérabilité | Ce n'est pas la simple existence d'un exploit |
| **Risque** | La combinaison vulnérabilité × exposition × exploitation × impact métier | Ce n'est jamais un score technique isolé |

Deux termes de calendrier viennent s'y ajouter, souvent employés à contresens :

- **0-day** : vulnérabilité pour laquelle **aucun correctif n'existe** au moment où elle est connue ou exploitée. L'éditeur a eu « zéro jour » pour corriger. Ce n'est pas synonyme de « très grave ».
- **n-day** : vulnérabilité pour laquelle un correctif existe depuis n jours. C'est **l'écrasante majorité des compromissions réelles** : les attaquants exploitent surtout ce qui est corrigé mais non appliqué. Retenez cette asymétrie, elle justifie à elle seule l'existence de ce cours.

⚠️ **PIÈGE — « c'est une 0-day » comme justification d'inaction**
Beaucoup d'organisations se rassurent en se disant qu'elles ne peuvent rien contre les 0-day. C'est vrai — et hors sujet, parce que ce n'est pas par là qu'elles se font attaquer. Le MCS traite les n-day, c'est-à-dire le cas où **vous aviez le correctif et ne l'avez pas appliqué**.

#### 4.2 CVE : comment un identifiant naît, et pourquoi sa qualité varie

**Le besoin.** Sans identifiant commun, votre scanner, votre éditeur, votre prestataire et votre auditeur parlent de la même faille avec quatre noms différents. Le programme CVE (*Common Vulnerabilities and Exposures*) résout ce problème : un identifiant unique, de la forme `CVE-2026-12345`.

**Ce qu'un identifiant CVE est, exactement.** Une **clé de dédoublonnage**. Rien de plus. Il ne dit pas si la faille est grave, ni si elle est exploitée, ni si elle vous concerne.

**Qui les attribue.** Des organisations accréditées appelées **CNA** (*CVE Numbering Authorities*) : éditeurs de logiciels pour leurs propres produits, centres de réponse aux incidents, projets open source, chercheurs. Elles reçoivent un bloc d'identifiants et les attribuent de façon autonome.

C'est ce point qui explique la variabilité de qualité, et il faut le comprendre pour ne pas s'étonner ensuite :

| Ce qui varie selon la CNA | Conséquence pratique |
|---|---|
| Le niveau de détail de la description | Certaines fiches disent tout, d'autres une ligne vague |
| La présence et la justesse des versions affectées | Sans versions précises, aucune corrélation automatique n'est possible |
| L'attribution ou non d'un score de gravité | Deux CNA peuvent scorer différemment la même classe de défaut |
| La rapidité de publication | Certaines publient avant le correctif, d'autres bien après |
| La granularité | Un éditeur peut regrouper dix défauts sous un identifiant, un autre en créer dix |

**Le cycle de vie d'une fiche.** Réservation d'un identifiant → publication de la fiche → enrichissements successifs (versions, références, scores) → parfois contestation, rejet ou fusion. Une fiche consultée le jour de sa publication et la même fiche trois semaines plus tard peuvent être très différentes.

✅ **BONNE PRATIQUE (P1)** — Ne figez jamais une décision de triage sur la première version d'une fiche publiée dans les 48 heures. Prévoyez explicitement un **rejeu** des constats récents : ce qui semblait mineur lundi peut être requalifié vendredi.

#### 4.3 Nommer les produits : CWE, CPE, purl — et pourquoi la corrélation échoue

Trois nomenclatures cohabitent, avec des rôles distincts.

**CWE — la nature du défaut.** Un catalogue de *types* de faiblesses : injection, débordement, mauvaise gestion des droits, condition de course. Une CVE peut être rattachée à une ou plusieurs CWE lorsque la nature de la faiblesse est connue et correctement renseignée — ce qui n'est pas systématique : certaines fiches n'ont pas de rattachement fiable, d'autres portent une catégorie générique, d'autres encore sont enrichies après publication. Utilité pour le MCS : repérer qu'un même type de défaut revient chez le même fournisseur, ce qui est un signal de qualité du produit — et un argument contractuel (chapitre 13).

**CPE — l'identification d'un produit.** Une chaîne normalisée décrivant éditeur, produit, version, édition. C'est ce qui permet à un outil de dire « la CVE affecte ce produit, or ce produit est installé ici ».

📌 **LIMITES — pourquoi la corrélation par CPE produit tant de bruit**
- Le nom du produit dans la fiche CVE et le nom du paquet installé sur votre machine ne se ressemblent pas toujours.
- Les intervalles de versions affectées sont souvent exprimés de manière imprécise, ou pas du tout.
- Le rétroportage (§2.2) rend la comparaison de version fausse par construction sur les systèmes à support long.
- Un même logiciel peut exister sous plusieurs identifiants selon qui l'a déclaré.
- Les composants embarqués dans une application n'ont généralement aucun identifiant produit.

**purl — l'identification d'un paquet logiciel.** Une notation plus récente et beaucoup plus adaptée aux écosystèmes de développement, de la forme `pkg:type/espace-de-noms/nom@version`. Elle décrit sans ambiguïté un paquet dans son écosystème d'origine. Il est largement utilisé dans les inventaires de composants logiciels modernes (§4.8), là où CPE reste le format historique des bases de vulnérabilités — avec une couverture qui varie selon les formats et les outils.

Retenez la conséquence opérationnelle : **une part importante des faux positifs de vos scanners ne vient pas de leur mauvaise qualité, mais de l'impossibilité structurelle de faire correspondre parfaitement deux nomenclatures conçues pour des usages différents.** Le chapitre 15 en fait un chapitre entier.

#### 4.4 CVSS : ce que le score mesure, et ce qu'on lui fait dire

**CVSS** (*Common Vulnerability Scoring System*) attribue une note de 0 à 10. C'est le chiffre que tout le monde connaît, et le plus mal utilisé du domaine.

**Ce qu'il mesure.** La **gravité technique intrinsèque** d'une vulnérabilité : à quel point elle est difficile à exploiter, quels privilèges elle exige, quelle interaction utilisateur elle suppose, et quels impacts elle produit sur la confidentialité, l'intégrité et la disponibilité du composant touché.

**La structure, en quatre groupes.**

| Groupe | Contenu | Qui le renseigne |
|---|---|---|
| **Base** | Caractéristiques intrinsèques et invariantes de la vulnérabilité | L'éditeur ou la CNA |
| **Menace** | Maturité du code d'exploitation à un instant donné | Rarement renseigné en pratique |
| **Environnement** | Adaptation à **votre** contexte : criticité de l'actif, mesures déjà en place | **Vous** — et presque personne ne le fait |
| **Complémentaire** | Informations qualitatives (sûreté, automatisabilité, récupérabilité) | Optionnel |

La version 4 du standard a notamment clarifié la distinction entre l'impact sur le **système vulnérable** et l'impact sur les **systèmes en aval**, et introduit une notation explicite indiquant quels groupes ont été utilisés — un score « base seule » n'a pas le même statut qu'un score enrichi de la menace et de l'environnement.

⚠️ **PIÈGE — les cinq erreurs d'interprétation les plus coûteuses**

| Erreur | Pourquoi c'est faux |
|---|---|
| « Score 9,8 = à corriger en priorité » | Le score de base ignore totalement votre exposition. Une faille 9,8 sur un service désactivé n'est pas un risque |
| « Score 5,3 = pas urgent » | Certaines failles de gravité moyenne sont massivement exploitées parce qu'elles sont triviales à automatiser |
| « Le score est objectif » | Il est calculé à partir de choix humains dans une grille. Deux analystes peuvent diverger |
| « Le score évolue avec la menace » | Le groupe Base est conçu pour être stable dans le temps : il ne reflète pas l'apparition d'un exploit public. Un vecteur publié peut néanmoins être corrigé ou révisé par son émetteur |
| « C'est la même chose qu'un niveau de risque » | Il manque l'exposition, la criticité métier et l'impact organisationnel |

> ### 🎯 La phrase à retenir de ce chapitre
> **CVSS décrit la gravité technique d'une vulnérabilité. Il ne décrit pas votre priorité opérationnelle.**
> Toute la suite du cours découle de cette distinction.

**Le bon usage.** CVSS mesure une **sévérité**, pas un risque — la documentation du standard le dit explicitement 📎 [S-18]. Il répond à la question « **quelle est la gravité technique si cette faille est exploitée ?** ». C'est une entrée utile parmi d'autres. Il ne répond ni à « est-ce exploité ? », ni à « suis-je atteignable ? », ni à « qu'est-ce que ça me coûte ? ».

#### 4.5 EPSS : la probabilité, et ses angles morts

**EPSS** (*Exploit Prediction Scoring System*) répond à une question différente et complémentaire : **quelle est la probabilité que cette vulnérabilité soit exploitée dans les trente prochains jours ?**

Le résultat est un nombre entre 0 et 1, accompagné d'un **percentile** indiquant la position relative de la vulnérabilité par rapport à toutes les autres.

**Ce qui change tout.** La distribution est extrêmement asymétrique : l'immense majorité des vulnérabilités publiées ont une probabilité d'exploitation très faible, et une petite fraction concentre presque tout le risque réel. C'est précisément ce qui rend une priorisation par gravité seule inefficace : elle traite comme équivalentes des milliers de vulnérabilités qui ne seront jamais exploitées et quelques dizaines qui le seront.

🧪 **EN PRATIQUE — lire correctement un couple de valeurs**
Une vulnérabilité à 0,08 de probabilité et 96ᵉ percentile signifie : *il y a environ 8 % de chances qu'elle soit exploitée dans les trente jours, et elle est malgré tout plus menaçante que 96 % des autres.* Les deux informations sont nécessaires : la probabilité pour dimensionner l'effort, le percentile pour arbitrer entre constats.

📌 **LIMITES — ce qu'EPSS ne sait pas**
- Il prédit l'exploitation **dans le monde**, pas chez vous. Il ignore totalement votre exposition et votre criticité métier.
- Il repose sur des signaux observables : une exploitation ciblée, discrète, contre un petit nombre d'organisations est mal captée par construction.
- La **transparence est partielle** : la méthode générale et les principes du modèle sont publics, mais le consommateur ne dispose ni des données d'entraînement, ni des poids, ni des signaux ayant produit un score donné — il ne peut donc ni reproduire ni auditer une valeur particulière.
- La probabilité est **volatile** : elle monte brutalement à la publication d'un exploit, puis redescend. Un score consulté il y a trois semaines n'a pas de valeur.

⚠️ **PIÈGE — la discontinuité entre versions de modèle**
Le modèle évolue par versions successives, et un changement de version **déplace tous les scores en même temps**. Conséquence directe et sous-estimée : une série temporelle qui traverse un changement de version n'est pas comparable. Si votre indicateur « nombre de vulnérabilités à forte probabilité » chute de 30 % en une semaine sans qu'aucun correctif n'ait été appliqué, cherchez d'abord un changement de modèle avant de féliciter vos équipes.

⏱ **ÉTAT DE L'ART (vérifié le 30/07/2026)** — La version 5 du modèle a commencé à publier ses scores le **15 juin 2026**. Toute série historique franchissant cette date doit être signalée comme discontinue dans vos tableaux de bord. 📎 [S-17]

#### 4.6 Les catalogues d'exploitation avérée

Un troisième signal, de nature complètement différente : non plus une prédiction, mais un **constat**.

L'agence américaine de cybersécurité maintient un catalogue de vulnérabilités **connues comme exploitées** (couramment appelé catalogue KEV). Trois critères d'inscription : un identifiant CVE attribué, une **preuve fiable d'exploitation active**, et une action de remédiation claire disponible.

**Pourquoi c'est un signal très fort.** Il n'y a ni probabilité, ni modèle, ni interprétation : quelqu'un a observé l'exploitation. En pratique, l'appartenance à ce catalogue est l'un des meilleurs déclencheurs d'une procédure d'urgence — mais pas un déclencheur suffisant à lui seul, puisqu'il ne couvre ni immédiatement les campagnes ciblées, ni les vulnérabilités sans identifiant.

📌 **LIMITES — ce que le catalogue ne dit pas**
- **Il est incomplet par construction.** Il recense ce qui a été observé **et** publié. Les attaques ciblées contre un secteur, ou celles détectées sans être divulguées, n'y figurent pas.
- **Il est en retard.** L'inscription suit l'observation, qui suit l'exploitation. Ne pas y figurer ne signifie pas « pas exploité », mais « pas encore observé publiquement ».
- **Il est orienté par son public.** Il sert d'abord les administrations américaines ; les produits dominants dans d'autres marchés peuvent y être sous-représentés.
- **Il ne dit rien de votre exposition.** Une vulnérabilité massivement exploitée sur un produit que vous n'utilisez pas ne vous concerne pas.

⚠️ Ne construisez jamais une doctrine du type « nous ne traitons en urgence que ce qui figure au catalogue ». Vous obtiendriez un processus lisible, défendable — et systématiquement en retard sur les campagnes visant votre secteur.

#### 4.7 Décider plutôt que scorer : les approches par arbre de décision

Un score produit un nombre ; il faut ensuite décider quoi en faire. Les approches par **arbre de décision** franchissent directement l'étape suivante : elles produisent une **action**.

Le principe est simple et transposable à n'importe quelle organisation. On pose quelques questions binaires ou ternaires, dans un ordre fixé, et chaque combinaison de réponses mène à une décision explicite.

🧪 **EN PRATIQUE — la structure d'un arbre de décision de remédiation**

```
1. Exploitation observée ?        aucune / démonstration publique / active
2. Automatisable à grande échelle ?              oui / non
3. Impact technique en cas de succès ?      partiel / total
4. Effet sur les missions et les personnes ?  faible / … / critique
                       ↓
       Surveiller · Surveiller de près · Traiter · Agir en urgence
```

L'intérêt majeur de cette forme est qu'elle est **auditable** : on ne discute plus d'un chiffre, on discute des réponses aux questions. Et le jour où vous devez justifier de ne pas avoir corrigé, vous produisez le chemin parcouru dans l'arbre plutôt qu'un seuil arbitraire.

Une approche complémentaire, plus récente, consiste à estimer la probabilité qu'une vulnérabilité **ait déjà été exploitée par le passé**, en agrégeant l'historique des prédictions plutôt qu'en regardant leur valeur du jour. Elle répond à une limite réelle des catalogues d'exploitation avérée — leur incomplétude — sans prétendre la supprimer.

✅ **BONNE PRATIQUE (P0)** — Quelle que soit la méthode retenue, **écrivez-la**. Une règle de priorisation non écrite est une règle qui varie selon la personne, la fatigue et le mois. Le modèle complet est construit au chapitre 16 et formalisé en Annexe C.

#### 4.8 De l'inventaire logiciel à l'exploitabilité déclarée : SBOM, VEX, CSAF

Trois briques récentes, souvent confondues, qui répondent à trois questions distinctes.

| Brique | Question à laquelle elle répond | Produite par |
|---|---|---|
| **SBOM** | *Que contient ce logiciel ?* | Le fournisseur, ou vous, à la construction |
| **VEX** | *Ce composant vulnérable rend-il ce produit exploitable ?* | Le fournisseur du produit |
| **CSAF** | *Comment publier un avis de sécurité lisible par une machine ?* | L'éditeur qui publie l'avis |

**SBOM** — l'inventaire des composants d'un logiciel, avec leurs versions et leurs relations de dépendance. Deux formats principaux coexistent, tous deux largement outillés. L'enjeu n'est pas de choisir : c'est de savoir **quoi en faire**. Un inventaire de composants que personne ne rapproche d'une base de vulnérabilités est un document mort.

**VEX** — la réponse à un problème très concret. Votre outil détecte un composant vulnérable dans un produit ; le fournisseur sait, lui, que le code vulnérable n'est jamais appelé dans son produit. Un document VEX transporte cette information sous une forme exploitable, avec quatre états possibles : *non affecté*, *affecté*, *corrigé*, *en cours d'analyse* — et, pour l'état « non affecté », une justification normalisée.

**CSAF** — le format d'avis de sécurité lisible par une machine. Il permet d'automatiser ce qui est aujourd'hui fait à la main : lire un bulletin, en extraire les produits et versions concernés, les rapprocher de l'inventaire.

📌 **LIMITES — l'écart entre la promesse et la réalité de terrain**
La production de ces documents progresse plus vite que leur consommation. Beaucoup d'organisations reçoivent des inventaires de composants qu'elles archivent sans jamais les exploiter, faute d'outillage ou de processus. Un inventaire fourni n'est utile que s'il est **à jour**, **rapproché de l'inventaire d'actifs**, et **rejoué à chaque nouvelle vulnérabilité publiée** — trois conditions rarement réunies. Le chapitre 25 traite la mise en œuvre réelle.

#### 4.9 ⏱ L'écosystème des données de vulnérabilités au 30 juillet 2026

*Bloc périssable. Vérifié le 30/07/2026.*

Le point à comprendre est structurel, et il survivra aux détails ci-dessous : **l'écosystème s'est fragmenté**, et la dépendance à une source unique est devenue un risque opérationnel.

**Ce qui a changé.**

- Le NIST a annoncé qu'à compter du **15 avril 2026**, l'enrichissement des fiches de sa base nationale serait **priorisé** : vulnérabilités connues comme exploitées, logiciels utilisés par l'administration fédérale américaine, logiciels critiques. Formulation exacte, importante : **toutes les vulnérabilités continuent d'être enregistrées** ; ce sont les analyses complémentaires — scores, correspondances produit, classification — qui deviennent sélectives, les autres fiches pouvant porter la mention *non programmé*.
- L'agence européenne de cybersécurité a mis en service une **base européenne de vulnérabilités**, alimentée notamment par les CSIRT nationaux, qui constitue désormais une source alternative crédible.
- D'autres initiatives d'attribution d'identifiants, indépendantes du programme historique, ont vu le jour et sont utilisables en complément.

📎 [S-16] pour l'évolution du NVD · [S-22] pour la base européenne.

**Ce que ça change pour vous, concrètement.**

| Si votre processus repose sur… | Alors |
|---|---|
| Le score de gravité fourni par une base unique | Une part croissante de vos constats arrivera sans score |
| La correspondance automatique produit fournie par cette base | Cette correspondance sera absente pour une partie des fiches |
| Un seuil du type « traiter au-dessus de 7 » | Ce seuil devient inapplicable sur les fiches non enrichies |

✅ **BONNE PRATIQUE (P0)** — Construisez votre chaîne de veille sur **au moins trois sources de nature différente** : l'avis de l'éditeur du produit concerné (source de vérité sur les versions), une base agrégée (dédoublonnage et couverture), et un signal d'exploitation avérée. Le détail opérationnel est au chapitre 14.

#### 4.10 📌 Ce qu'aucun score ne saura jamais : votre exposition

Récapitulons ce que chaque signal apporte, et surtout ce qu'aucun n'apporte.

| Signal | Répond à | Ne répond pas à |
|---|---|---|
| Gravité technique | Si elle est exploitée, quel dégât ? | Est-elle exploitée ? Suis-je atteignable ? |
| Probabilité d'exploitation | Sera-t-elle exploitée dans le monde ? | Chez moi ? Sur cet actif ? |
| Catalogue d'exploitation avérée | A-t-elle été observée en exploitation ? | Suis-je concerné ? Suis-je exposé ? |
| Arbre de décision | Que dois-je faire ? | *(il faut lui fournir l'exposition en entrée)* |

Les trois premiers signaux sont produits **hors de chez vous**. Aucun ne connaît :

- si le service vulnérable est activé sur vos machines ;
- s'il est joignable depuis Internet, depuis le réseau bureautique, ou depuis nulle part ;
- si une mesure de contournement est déjà en place ;
- si l'actif porte une donnée critique ou un procédé industriel ;
- si sa compromission ouvre l'accès à d'autres actifs.

**C'est vous qui apportez la moitié manquante de l'équation, et personne d'autre ne peut le faire à votre place.**

##### Ce que vous manipulerez réellement au quotidien

Sur la dizaine de notions présentées dans ce chapitre, quatre seulement interviennent chaque jour :

| Au quotidien | Pourquoi |
|---|---|
| **L'avis de l'éditeur** du produit concerné | La seule source de vérité sur « suis-je affecté, et quelle version corrige » |
| **Le signal d'exploitation avérée** | Le déclencheur d'urgence le plus fiable |
| **Votre cartographie d'exposition** | Elle transforme un constat en priorité |
| **Votre inventaire enrichi de criticité** | Il transforme une priorité en décision |

Les autres — nomenclatures de produits, modèles de probabilité, formats d'inventaire et d'exploitabilité — sont des **outils de soutien** : utiles quand vous en avez besoin, à consulter plutôt qu'à mémoriser. C'est aussi pour cela que les deux dernières lignes du tableau, qui ne dépendent d'aucun fournisseur, sont les plus robustes de tout le dispositif. C'est aussi la raison pour laquelle le chapitre 11 (exposition et chemins d'attaque) est placé avant le chapitre 16 (triage) : sans connaissance de l'exposition, la meilleure méthode de priorisation du monde travaille sur une entrée manquante.

#### 4.11 🔬 Mini-lab 1 — Qualifier dix constats hétérogènes

**Objectif** — Typer un constat avant de le prioriser, et reconnaître ceux qui n'ont pas d'identifiant de vulnérabilité.
**Durée** 30 min · **Difficulté** 🟢 débutant · **Prérequis** §4.1 à §4.7, §14.7 · **Livrable** tableau de qualification typée.
**Compétences validées** — ✔ distinguer les origines de constats ✔ identifier la source de vérité d'un constat ✔ qualifier en fait / hypothèse / piste ✔ repérer un constat qui n'a pas d'identifiant de vulnérabilité

**Énoncé.** Voici dix constats arrivés la même semaine dans la boîte de réception d'une équipe de sécurité. Pour chacun : (a) de quel **type de constat** s'agit-il ? (b) quelle est sa **source de vérité** ? (c) quelle **information manque** pour décider ? (d) fait vérifié, hypothèse probable ou piste exploratoire ?

| # | Constat |
|---|---|
| 1 | Le scanner remonte une bibliothèque de chiffrement en version antérieure à la version corrigée en amont, sur 42 serveurs à support long |
| 2 | Un bulletin d'éditeur annonce une « faille critique d'exécution de code », sans identifiant CVE, avec une version corrigée |
| 3 | Un rapport de test d'intrusion signale une interface d'administration accessible sans authentification sur un port non standard |
| 4 | Une vulnérabilité de gravité 5,3 vient d'entrer au catalogue d'exploitation avérée |
| 5 | L'équipe de développement signale qu'une dépendance transitive de l'application métier est marquée vulnérable par l'outil d'analyse de composition |
| 6 | Un fournisseur SaaS annonce qu'un paramètre de sécurité par défaut change à la prochaine mise à jour |
| 7 | Le service comptable a reçu une facture pour un abonnement à un service en ligne inconnu de la DSI |
| 8 | Un chercheur signale par courriel une faille dans votre produit, avec une preuve de concept fonctionnelle et un délai de 90 jours |
| 9 | La supervision remonte que 14 agents de sécurité n'ont pas mis à jour leur base de détection depuis 21 jours |
| 10 | Une vulnérabilité de gravité 9,8 est publiée sur un composant présent dans votre parc, mais uniquement exploitable en accès physique local |

**Corrigé commenté**

| # | Type | Source de vérité | Information manquante | Statut |
|---|---|---|---|---|
| 1 | Vulnérabilité de composant, **probable faux positif de rétroportage** | Avis de sécurité de la distribution + révision du paquet installée | La révision éditeur réelle sur les 42 serveurs (§2.2) | Piste exploratoire tant que la révision n'est pas vérifiée |
| 2 | Vulnérabilité sans identifiant — **le MCS ne se réduit pas aux CVE** | L'avis de l'éditeur lui-même | Versions exactes déployées ; l'absence de CVE n'atténue rien | Fait vérifié sur l'existence, hypothèse sur l'impact |
| 3 | Écart de configuration / **exposition**, pas une vulnérabilité logicielle | Le rapport de test, rejoué et confirmé | Qui possède cet actif ? Depuis quand ? Traces d'accès ? | Fait vérifié — et probablement le constat le plus grave des dix |
| 4 | Vulnérabilité **à exploitation avérée** | Le catalogue + l'avis éditeur | Suis-je exposé ? La gravité modérée est ici sans importance | Fait vérifié — traitement en urgence malgré le 5,3 |
| 5 | Vulnérabilité de **dépendance transitive** | Inventaire de composants + déclaration d'exploitabilité du fournisseur | Le code vulnérable est-il atteignable dans l'application ? (§25.12) | Hypothèse probable |
| 6 | **Changement fournisseur** — activité de MCS à part entière (§3.4) | Les notes de version du fournisseur | Quels paramètres, quel effet sur ma configuration validée ? | Fait vérifié, impact à instruire |
| 7 | **Actif orphelin** découvert par une source non technique | La facture, puis la confirmation métier | Quelles données ? Quel connecteur ? Quel propriétaire ? | Fait vérifié sur l'existence |
| 8 | **Divulgation coordonnée** reçue en tant que fabricant | Le chercheur, puis la reproduction interne | Reproductible ? Quelles versions livrées ? Horloge des 90 jours (ch. 33) | Hypothèse jusqu'à reproduction |
| 9 | **Dégradation du contenu de détection**, pas une vulnérabilité (§1.3, ch. 34) | La console de l'outil, recoupée sur les postes | Pourquoi 21 jours ? Agents muets ou machines éteintes ? | Fait vérifié |
| 10 | Vulnérabilité grave mais **non atteignable à distance** | L'avis éditeur, lu jusqu'au vecteur d'accès | Existe-t-il des accès physiques non maîtrisés ? | Fait vérifié — priorité basse malgré le 9,8 |

**Les trois erreurs attendues.** Trier ces dix constats par gravité technique — cela placerait le n° 10 en tête et le n° 3 en queue, exactement à l'envers. Écarter les constats 6, 7 et 9 comme « hors sujet MCS » — ils en font pleinement partie. Traiter le n° 1 comme un fait avant vérification de la révision éditeur — et engager 42 interventions inutiles.

🔴 **FIL ROUGE — février 2026 : la semaine des 4 300 constats**

Le premier scan authentifié sur le périmètre réconcilié (§2.9) produit 4 312 constats. Malik Ferhaoui applique la règle qu'il connaît : gravité supérieure ou égale à 7. Il obtient 1 176 constats à traiter. À raison de vingt minutes par constat pour deux personnes, cela représente près de deux ans de travail.

Claire Nadeau demande un autre découpage, en trois questions seulement : *est-ce observé en exploitation ? est-ce atteignable depuis l'extérieur ? l'actif est-il critique ?*

| Filtre | Constats restants |
|---|---|
| Total brut | 4 312 |
| Gravité ≥ 7 (méthode initiale) | 1 176 |
| Exploitation avérée, tous niveaux de gravité confondus | 31 |
| … dont sur un actif joignable depuis Internet | **7** |
| … dont sur un actif de niveau 0 ou critique métier | **3** |

Les sept constats exposés incluent une vulnérabilité de gravité 5,9 sur la passerelle d'accès distant, que la méthode initiale écartait. Elle sera au cœur du cas de synthèse A.

**Décision prise.** La priorisation ne sera plus fondée sur la gravité seule. Trois entrées obligatoires : exploitation observée, exposition, criticité de l'actif. Et une règle qui deviendra un principe de la maison : *un constat que l'on choisit de ne pas traiter doit être écrit, daté et signé — pas oublié dans un rapport.*

**Livrable de l'épisode.** Un premier arbre de décision d'une page, imparfait, appliqué dès la semaine suivante. La version aboutie est construite au chapitre 16.

→ La suite en 🔴 §5.5, quand il faudra désigner qui décide d'arrêter une machine.

#### Synthèse mentale du chapitre 4

Un identifiant de vulnérabilité est une clé de dédoublonnage, pas un jugement : sa qualité dépend entièrement de l'organisation qui l'a attribué. La gravité technique mesure les dégâts en cas d'exploitation, jamais la probabilité qu'elle survienne ni votre exposition. La probabilité d'exploitation comble une partie du manque mais reste mondiale, volatile et discontinue entre versions de modèle. Les catalogues d'exploitation avérée sont le signal le plus fort et le plus incomplet : ne pas y figurer ne veut pas dire ne pas être exploité. Les approches par arbre de décision produisent directement une action et se défendent en audit, ce qu'un seuil chiffré ne fait pas. Les inventaires de composants, les déclarations d'exploitabilité et les avis lisibles par machine sont produits plus vite qu'ils ne sont consommés. Enfin, l'écosystème s'est fragmenté : dépendre d'une source unique est devenu un risque, et la moitié de l'équation — votre exposition — n'est produite par personne d'autre que vous.

**Trois questions de vérification**

1. Une vulnérabilité de gravité 5,3 vient d'entrer dans un catalogue d'exploitation avérée ; une autre est notée 9,8 mais n'exige aucun privilège et n'est exploitable qu'en accès physique. Laquelle traitez-vous en premier, et avec quel argument devant un comité ?
2. Votre tableau de bord « vulnérabilités à forte probabilité d'exploitation » chute de 30 % en une semaine sans aucun déploiement. Quelles sont les deux causes à vérifier avant de communiquer ce résultat ?
3. Un fournisseur vous transmet un inventaire des composants de son produit. Quelles trois conditions doivent être réunies pour que ce document ait une valeur opérationnelle chez vous ?

---

### Chapitre 5 — Socle processus : changement, risque, propriété, normes, preuve

Les chapitres 2 à 4 ont installé la technique. Celui-ci installe ce qui, dans la pratique, décide de tout : **qui a le droit de faire quoi, quand, et comment on le prouve**. C'est le chapitre le moins spectaculaire du cours et l'un des plus déterminants — les cinq causes d'échec du §1.4 sont toutes ici.

#### 5.1 La gestion du changement, alliée ou frein

**Le principe.** Dans toute organisation structurée, modifier un système en production suppose une autorisation. Cette discipline existe pour une bonne raison : la première cause d'indisponibilité, statistiquement, n'est pas l'attaque, c'est le changement mal maîtrisé.

**Les trois catégories universelles.**

| Catégorie | Définition | Autorisation | Usage en MCS |
|---|---|---|---|
| **Changement standard** | Pré-autorisé, procédure connue, risque évalué une fois pour toutes | Aucune validation au cas par cas | **C'est ici que doit vivre le MCS courant** |
| **Changement normal** | Nouveau ou risqué, examiné individuellement | Comité de validation | Montées de version majeures, changements d'architecture |
| **Changement d'urgence** | Traité hors délai normal, régularisé après | Validation restreinte, souvent a posteriori | Correctif de crise (chapitre 21) |

**L'erreur de conception la plus répandue.** Faire passer chaque campagne de correctifs mensuelle en changement normal. Le résultat est mécanique : le comité devient un goulot d'étranglement, les délais s'allongent, et les équipes finissent par contourner le processus — ce qui détruit à la fois la traçabilité et la confiance.

✅ **BONNE PRATIQUE (P0) — faire du MCS courant un changement standard**
Construisez un dossier de changement standard couvrant votre campagne récurrente : périmètre, procédure, tests, critères d'arrêt, plan de retour arrière, fenêtre. Faites-le valider **une fois**. Ensuite, chaque campagne s'exécute sans repasser en comité, et seuls les cas sortant du cadre y remontent. Vous transformez un frein en accélérateur, sans perdre la traçabilité — au contraire, elle devient homogène.

🏢 **VU EN RÉUNION** — Un comité de changement examine une campagne mensuelle de correctifs. Le représentant métier demande la liste des serveurs concernés, puis : « et si ça casse ? ». L'exploitation répond « on a un instantané ». Le comité valide. Personne n'a demandé combien de temps prend la restauration d'un instantané sur ces serveurs — la réponse était de quarante minutes, et le service avait un engagement de disponibilité de quinze minutes. Le §18.8 existe à cause de ce genre de séance.

⚠️ **PIÈGE — le changement d'urgence qui devient la norme**
Quand le processus standard est trop lourd, tout devient une urgence. Symptôme mesurable : la part des changements d'urgence dans le total. Au-delà de 15 à 20 %, ce n'est plus un indicateur de réactivité, c'est le signe que votre processus normal ne fonctionne pas. Suivez ce ratio (chapitre 38).

#### 5.2 Fenêtres, gels et calendriers métier

**La fenêtre de maintenance** est un créneau pendant lequel une interruption est acceptée par les métiers. C'est une ressource rare, et le MCS n'en est pas le seul consommateur : projets, montées de version applicatives, opérations d'infrastructure s'y disputent la place.

**Trois principes de négociation qui fonctionnent.**

1. **Négocier des fenêtres récurrentes, pas des interventions.** Obtenir « le deuxième jeudi de chaque mois, de 22 h à 2 h » une seule fois vaut mieux que douze négociations annuelles. Chaque négociation individuelle a un coût, et ce coût produit du report.
2. **Différencier par criticité.** Un actif de niveau 0 mérite une fenêtre courte et fréquente ; un serveur secondaire peut se contenter d'une fenêtre trimestrielle plus large. Les classes de service du chapitre 7 formalisent ce découpage.
3. **Prévoir la fenêtre d'urgence dès maintenant.** Le jour de la crise, personne n'a le temps de négocier. Faites acter à l'avance : *en cas de vulnérabilité exploitée sur un actif exposé, l'interruption est autorisée sous délai de X heures, par décision de Y.* C'est une décision de gouvernance qui se prend à froid (chapitre 9).

**Les gels de production.** Périodes où tout changement est interdit : clôture comptable, campagne commerciale, fin d'année, pic saisonnier. Elles sont légitimes et non négociables sur le principe. Deux points d'attention :

- Un gel n'est **jamais** absolu en sécurité : il doit comporter une clause explicite de levée pour vulnérabilité exploitée, avec le décideur nommé.
- L'accumulation des gels peut réduire l'année à quelques semaines réellement disponibles. Faites le calcul et présentez-le : *« nous disposons de 14 semaines exploitables sur 52 »* est un argument autrement plus efficace qu'une demande de moyens.

#### 5.3 Analyse de risque appliquée au MCS

Vous n'avez pas besoin d'être expert en analyse de risque pour faire du MCS. Vous avez besoin de trois notions.

**Le risque résiduel.** Ce qui reste après application des mesures. Il n'est jamais nul, et le reconnaître explicitement est un acte de maturité, pas un aveu de faiblesse. Un programme de MCS qui prétend supprimer le risque est un programme qui ment à sa direction.

**L'acceptation formalisée.** Décider de ne pas corriger est une décision légitime — **à condition** qu'elle soit prise par la bonne personne, écrite, datée, bornée dans le temps, assortie de mesures compensatoires et revue à échéance. Non formalisée, c'est un oubli ; formalisée, c'est une décision de gestion. La différence entre les deux est ce que regarde un auditeur, et ce que regarde un juge.

**La méthode structurée, quand elle est utile.** Les démarches d'analyse de risque par ateliers successifs — cadrage et socle de sécurité, identification des sources de risque, scénarios stratégiques, scénarios opérationnels, traitement — apportent au MCS deux choses précises : elles obligent à nommer **qui** vous attaquerait et **pourquoi**, ce qui oriente la priorisation vers les chemins réellement plausibles ; et elles produisent une échelle de gravité **métier**, indispensable pour transformer une criticité technique en criticité d'actif.

⚠️ **PIÈGE — l'analyse de risque comme préalable bloquant**
N'attendez pas une analyse complète pour démarrer un programme de MCS. Une classification de criticité à trois niveaux, imparfaite mais appliquée, vaut infiniment mieux qu'une analyse exhaustive attendue pendant dix-huit mois. Commencez avec ce que vous avez, affinez ensuite.

#### 5.4 Lire une exigence de conformité : la grille en trois niveaux

Vous allez rencontrer des référentiels — normes, réglementations, référentiels sectoriels, questionnaires clients. Une seule grille de lecture suffit à ne jamais s'y perdre.

| Niveau | Question | Exemple générique | Qui le fixe |
|---|---|---|---|
| **Exigence** | Que dois-je obtenir ? | « Les vulnérabilités techniques doivent être identifiées et traitées en temps utile » | Le texte |
| **Objectif de sécurité** | Quel résultat concret cela suppose-t-il ? | « Détecter les vulnérabilités du parc et les corriger selon des délais définis par criticité » | Le référentiel d'application |
| **Moyen de conformité** | Comment je le fais chez moi ? | « Scan authentifié mensuel, arbre de décision, délais de 7/30/90 jours, dérogations tracées » | **Vous** |

**Les deux erreurs symétriques.**

- **Confondre exigence et moyen** : croire qu'un texte impose un outil ou une fréquence précise. C'est presque toujours faux — les textes fixent des résultats, pas des implémentations. Cela vous laisse une liberté que beaucoup n'exploitent pas.
- **Croire que le moyen suffit** : avoir un scanner et une procédure ne démontre rien. Ce qui est évalué, c'est le **résultat** et sa **preuve**.

Le principe de **proportionnalité** figure dans la plupart des référentiels modernes : les mesures attendues sont proportionnées à la taille de l'organisation, à son exposition et à la criticité de ses activités. C'est un levier de négociation légitime, à condition d'être capable de **justifier** votre calibrage — donc de l'avoir écrit.

#### 5.5 La propriété d'actif : la question qui débloque tout

Nous arrivons à la cause d'échec n° 2 du §1.4, et sans doute à la phrase la plus utile de ce cours.

> Pour chaque actif, une seule question doit avoir une réponse **nominative** : *qui décide qu'on l'arrête pour le corriger ?*

**Pourquoi cette formulation.** « Qui est responsable de ce serveur ? » obtient des réponses floues et collectives. « Qui décide de l'arrêter ? » n'admet qu'un nom. Et c'est exactement la décision qui bloque en pratique.

**Les cinq rôles à distinguer**, parce que les confondre produit l'essentiel des blocages :

| Rôle | Ce qu'il fait | Ce qu'il ne fait pas |
|---|---|---|
| **Propriétaire métier** | Décide de l'interruption, arbitre le risque, porte le budget | Il n'exécute pas |
| **Propriétaire technique** | Exploite, applique, vérifie, produit la preuve | Il ne décide pas de l'arrêt |
| **Éditeur / constructeur** | Produit le correctif, définit les prérequis | Il ne connaît pas votre contexte |
| **Intégrateur** | A construit le système, connaît ses dépendances | Il n'est souvent plus là |
| **Infogérant** | Exécute selon contrat | **Il ne porte jamais la décision d'accepter un risque** (chapitre 13) |

⚠️ **PIÈGE — la propriété collective**
« C'est l'équipe infrastructure » n'est pas une réponse. Une équipe ne prend pas de décision d'interruption à 3 h du matin ; une personne le fait. Exigez un nom, et un suppléant. Sans cela, votre programme s'arrêtera au premier arbitrage.

✅ **BONNE PRATIQUE (P0) — la campagne de désignation**
Nommer les propriétaires est un exercice de trois à six semaines, pas un projet. Méthode qui fonctionne : extraire la liste des actifs, proposer un propriétaire pressenti pour chacun, envoyer la liste aux responsables concernés avec une règle explicite — *sans retour sous quinze jours, la désignation proposée est réputée acceptée*. Le silence devient une acceptation, et la liste se remplit. Les actifs pour lesquels personne ne se reconnaît sont votre priorité réelle : ce sont les **actifs orphelins**, et ils sont presque toujours ceux qui posent problème.

🔴 **FIL ROUGE — mars 2026 : trois noms et un refus**

Claire Nadeau lance la campagne de désignation sur les 221 actifs du périmètre de référence. Trois retours illustrent tout le chapitre.

**Le cas simple.** Sonia Weber, directrice des systèmes d'information, accepte d'être propriétaire métier des serveurs d'infrastructure centraux et désigne Malik Ferhaoui comme propriétaire technique. Fenêtre récurrente négociée : deuxième jeudi du mois, 22 h - 2 h. Pour ces actifs, le MCS devient un changement standard dès avril.

**Le cas de la négociation.** Thomas Berger refuse d'être désigné propriétaire des onze postes de supervision de l'usine tant qu'aucune fenêtre n'est définie : « je ne peux pas m'engager sur quelque chose que je n'ai pas le droit d'arrêter ». Il a raison, et sa réponse est plus constructive qu'une acceptation de façade. La discussion aboutit à un compromis : il devient propriétaire, avec une fenêtre unique lors de l'arrêt de production d'août, et l'engagement écrit que toute intervention hors de cette fenêtre relève d'une décision de la direction générale, pas de la sécurité.

**Le cas révélateur.** Vingt-neuf actifs ne trouvent aucun propriétaire — l'essentiel des machines de test non déclarées et des appliances virtuelles d'éditeurs. Personne ne les revendique, et personne ne demande non plus leur arrêt. Claire applique une règle qui deviendra structurante : *tout actif orphelin depuis plus de trente jours entre dans une procédure d'extinction programmée, avec préavis de quinze jours diffusé largement.* Sur les vingt-neuf, onze trouvent immédiatement un propriétaire — le préavis a réveillé leurs utilisateurs. Huit sont éteints sans conséquence. Dix relèvent d'un décommissionnement en règle (chapitre 35).

**Décision prise.** La désignation nominative devient un prérequis d'entrée en production : aucun nouvel actif n'est mis en service sans propriétaire métier et propriétaire technique nommés.

**Livrable de l'épisode.** Le référentiel de propriété, intégré à la base d'inventaire — les champs correspondants figurent en Annexe I.

→ La suite en 🔴 §6.15, quand ces engagements rencontrent une architecture qui ne permet pas de les tenir.

#### 5.6 Ce qui a valeur de preuve, et ce qui n'en a pas

Le §2.9 a posé les six champs d'une preuve technique. Élargissons au niveau organisationnel.

| Élément | Valeur probante | Condition |
|---|---|---|
| Politique écrite et validée | Faible seule, indispensable en support | Datée, versionnée, approuvée nominativement |
| Compte rendu de comité | Bonne pour les **décisions** | Décisions explicites, pas un relevé de discussion |
| Extraction d'outil | Bonne pour l'**état** | Datée, périmètre défini, non retouchée, actifs injoignables listés |
| Journal système | Forte | Horodaté, intègre, conservé |
| Fiche de dérogation | Forte pour justifier une **non-action** | Signataire, durée, mesure compensatoire, date de revue |
| Déclaration orale ou courriel | Nulle | — |

**La règle qui résume tout** : une preuve répond à *qui, quoi, quand, sur quel périmètre, et qu'est-ce qui manque*. Le dernier terme est celui qui distingue un professionnel d'un amateur — un rapport qui n'énonce pas ses trous est un rapport qu'on ne peut pas croire.

#### 5.7 Trois familles d'indicateurs à ne pas confondre

Dernière notion du socle, et source d'innombrables tableaux de bord inutiles.

| Famille | Question | Exemple | Piège |
|---|---|---|---|
| **Activité** | Qu'avons-nous fait ? | Nombre de correctifs déployés ce mois | Récompense l'agitation ; ne dit rien du résultat |
| **Résultat** | Où en sommes-nous ? | Part des actifs critiques conformes, sur périmètre de référence | Nécessite un dénominateur solide |
| **Risque** | Que craignons-nous ? | Nombre d'actifs exposés portant une vulnérabilité exploitée | Le seul qui parle à une direction générale |

⚠️ **PIÈGE — l'indicateur qui récompense l'inaction**
« Nombre de vulnérabilités détectées » est un indicateur d'activité déguisé en indicateur de risque. Il s'améliore quand vous scannez moins. C'est l'archétype de la métrique qu'il ne faut pas présenter à un comité — le chapitre 38 en recense une dizaine d'autres, et l'Annexe K fournit les définitions rigoureuses.

→ **Chapitre 6 — Architecture maintenable : le MCS *by design*** : la conception — parce que le coût du MCS se décide avant la mise en service.

#### Synthèse mentale du chapitre 5

Le MCS courant doit vivre en changement standard, pré-autorisé une fois pour toutes : le faire passer en comité à chaque campagne transforme la gouvernance en goulot d'étranglement et pousse les équipes à contourner le processus. Les fenêtres se négocient de façon récurrente et différenciée par criticité, et la fenêtre d'urgence se décide à froid, jamais pendant la crise. Décider de ne pas corriger est légitime dès lors que la décision est prise par la bonne personne, écrite, bornée, compensée et revue — c'est ce qui sépare un oubli d'une décision de gestion. Face à un référentiel, distinguez l'exigence, l'objectif et le moyen : les textes fixent des résultats, le moyen vous appartient, et c'est le résultat prouvé qui est évalué. La question qui débloque le plus de situations n'est pas « qui est responsable ? » mais « qui décide qu'on l'arrête ? », et elle n'admet qu'un nom. Enfin, une preuve dit qui, quoi, quand, sur quel périmètre — et ce qui manque.

**Trois questions de vérification**

1. Votre campagne mensuelle de correctifs passe en comité de validation à chaque itération et accuse trois semaines de retard moyen. Que changez-vous, et qu'obtenez-vous en échange de cette simplification ?
2. Un référentiel exige que « les vulnérabilités techniques soient traitées en temps utile ». Votre direction vous demande quel outil il faut acheter. Que répondez-vous ?
3. Quinze actifs de votre parc n'ont aucun propriétaire identifié depuis quatre mois. Quelle procédure appliquez-vous, et pourquoi le préavis est-il l'élément clé du dispositif ?

---

### Chapitre 6 — Architecture maintenable : le MCS *by design*

#### 6.1 La thèse du chapitre

Les chapitres précédents décrivaient comment maintenir ce qui existe. Celui-ci change de moment : il traite des décisions prises **avant** la mise en service, et qui déterminent le coût de tout le reste.

> **Un système mal conçu pour être mis à jour produira de la dette de sécurité, quelle que soit la qualité du processus de MCS qui s'y applique.**

Ce n'est pas une opinion, c'est une conséquence mécanique. Si arrêter un système coûte 40 000 € de production perdue, aucune politique de correctifs ne convaincra qui que ce soit de l'arrêter chaque mois. Si une application est couplée à une version précise de son environnement d'exécution, aucun outil ne permettra de faire évoluer cet environnement. Si aucun retour arrière n'existe, chaque correctif restera une prise de risque non couverte, et sera reporté.

Le corollaire est encourageant : **les gains les plus importants du MCS ne s'obtiennent pas en exploitation, ils s'obtiennent en conception** — et ils ne coûtent presque rien s'ils sont décidés au bon moment.

Ce chapitre s'adresse à trois publics : ceux qui conçoivent des systèmes, ceux qui les achètent ou les font réaliser, et ceux qui les exploitent et doivent expliquer pourquoi ils n'y arrivent pas.

#### 6.2 La maintenabilité comme exigence opposable

Le problème pratique : la maintenabilité de sécurité n'apparaît dans aucun cahier des charges, donc personne n'y répond, donc elle n'existe pas.

La solution consiste à la formuler comme une exigence explicite, vérifiable en revue de conception et opposable à un fournisseur. Sept exigences suffisent à couvrir l'essentiel.

| # | Exigence | Formulation opposable |
|---|---|---|
| 1 | Interruptibilité | « Le système supporte l'arrêt d'un composant sans interruption de service pour l'utilisateur » |
| 2 | Découplage de version | « Le système n'impose pas une version figée de son système d'exploitation, de son environnement d'exécution ou de sa base de données » |
| 3 | Réversibilité | « Toute mise à jour dispose d'une procédure de retour arrière documentée et testée » |
| 4 | Observabilité du changement | « Le système expose des indicateurs permettant de constater un effet de bord dans les minutes suivant une mise à jour » |
| 5 | Cadence supportée | « Le système supporte l'application de correctifs de sécurité à une cadence mensuelle » |
| 6 | Inventoriabilité | « Le système déclare ses composants et leurs versions de manière lisible par une machine » |
| 7 | Fin de vie | « Le fournisseur s'engage sur une durée de support et un préavis de fin de support » |

✅ **BONNE PRATIQUE (P0)** — Insérez ces sept exigences dans vos cahiers des charges et vos grilles de revue d'architecture. Elles ne coûtent rien à écrire, elles se négocient au moment où vous avez encore un levier — avant la signature — et elles vous éviteront des années de dérogations. Les exigences 2, 3 et 7 sont celles qui produisent le plus d'effet.

#### 6.3 Redondance et haute disponibilité réellement compatibles avec la mise à jour

**L'idée de base.** Si un service tourne sur deux instances au lieu d'une, vous pouvez en arrêter une pour la corriger pendant que l'autre continue de servir. La redondance transforme une interruption de service en simple réduction de capacité. C'est le levier le plus direct entre architecture et MCS.

**Ce qui la rend inopérante en pratique.** Il existe beaucoup de redondances de façade.

⚠️ **PIÈGE — les cinq faux clusters**

| Configuration | Pourquoi ça ne tient pas |
|---|---|
| Deux instances, mais capacité dimensionnée pour deux | En arrêter une sature l'autre : vous ne pouvez plus jamais patcher aux heures ouvrées |
| Deux instances, une base de données unique | La base reste un point unique de panne — et c'est elle qu'il faut corriger |
| Redondance active/passive jamais basculée | La bascule n'a pas été testée depuis 2021 ; personne n'ose |
| Instances redondées, session utilisateur non partagée | Chaque bascule déconnecte les utilisateurs : les métiers refusent |
| Redondance sur le service, pas sur ses dépendances | Le service est doublé, l'annuaire ou le stockage ne l'est pas |

**Le test de vérité**, à poser en revue d'architecture : *pouvez-vous arrêter un membre de ce cluster, maintenant, en pleine journée, sans prévenir personne ?* Si la réponse n'est pas un oui franc, la redondance existe pour la panne, pas pour la maintenance — et c'est une distinction que beaucoup d'organisations découvrent trop tard.

#### 6.4 Trois stratégies de déploiement, et quand chacune vaut son coût

| Stratégie | Principe | Coût | Retour arrière | Adaptée à |
|---|---|---|---|---|
| **Progressive** (*rolling*) | Remplacement instance par instance | Faible | Lent (repasser en sens inverse) | Services sans état, nombreuses instances |
| **Bleu / vert** | Deux environnements complets, bascule du trafic | Élevé (double infrastructure) | **Immédiat** | Systèmes critiques, fenêtres impossibles |
| **Témoin** (*canary*) | Une petite fraction du trafic sur la nouvelle version | Moyen | Rapide | Tout ce dont on veut mesurer l'effet réel |

**Ce qu'il faut vraiment retenir.** Ces stratégies ne servent pas seulement à déployer des fonctionnalités : elles sont l'outil qui permet d'appliquer un correctif **sans pari**. Le déploiement témoin en particulier répond exactement au dilemme du chapitre 18 — corriger vite tout en limitant l'impact d'une régression.

📌 **LIMITES** — Aucune de ces stratégies ne s'applique telle quelle à un composant à état : une base de données, un annuaire, un automate industriel. Elles supposent que l'on peut faire coexister deux versions, ce qui nous amène au point suivant.

#### 6.5 Découpler le déploiement de l'activation

Un mécanisme simple change profondément la gestion du risque : séparer **installer le code** de **activer le comportement**.

Un interrupteur de fonctionnalité (*feature flag*) est un paramètre qui active ou désactive un comportement sans redéployer. Le bénéfice pour le MCS est direct et sous-estimé :

- vous déployez la nouvelle version avec le nouveau comportement désactivé, donc sans risque fonctionnel ;
- vous activez ensuite progressivement, sur une population réduite ;
- en cas de problème, vous **désactivez en quelques secondes** au lieu de redéployer l'ancienne version.

C'est aussi le mécanisme qui rend possible une mesure compensatoire propre : désactiver une fonctionnalité vulnérable en attendant le correctif, sans arrêter le service (chapitre 20).

⚠️ **PIÈGE** — Les interrupteurs s'accumulent. Un système comptant 400 interrupteurs dont personne ne connaît l'état est devenu impossible à raisonner, et les combinaisons non testées deviennent la norme. Fixez une durée de vie : un interrupteur temporaire qui dépasse six mois est soit supprimé, soit promu en paramètre de configuration documenté.

#### 6.6 Compatibilité entre versions et contrats d'interface

Pour qu'un déploiement progressif fonctionne, deux versions doivent **coexister** — au moins quelques minutes, parfois plusieurs jours. Cela impose une discipline.

**La compatibilité descendante** : la nouvelle version doit continuer à comprendre ce que produit l'ancienne. **La compatibilité ascendante**, plus rarement pensée : l'ancienne version ne doit pas se casser en recevant ce que produit la nouvelle.

**Les règles pratiques qui suffisent dans 90 % des cas :**

- ajouter un champ, jamais en supprimer ni en renommer dans la même version ;
- ne jamais changer le sens d'un champ existant ;
- déprécier avant de supprimer, avec un délai annoncé et mesuré ;
- versionner explicitement les interfaces exposées à d'autres équipes ou à des clients ;
- traiter un point d'accès déprécié comme un actif à décommissionner (chapitre 35), avec une date.

**Le lien avec le MCS est direct** : une interface sans compatibilité impose un déploiement synchronisé de tous les composants, donc une interruption globale, donc une fenêtre rare, donc du report.

#### 6.7 Migrations de schéma : le point de non-retour

C'est le cas le plus dangereux du chapitre, parce qu'il annule silencieusement votre plan de retour arrière.

**Le mécanisme.** Une mise à jour applicative modifie la structure de la base de données. Le code applicatif, lui, se réinstalle facilement en version antérieure. Les **données**, non : elles ont été transformées. Vous pouvez redéployer l'ancienne version du code, elle ne saura plus lire la base.

**Ce que ça implique.** Le retour arrière cesse d'être une opération technique de quelques minutes pour devenir une **restauration de sauvegarde**, avec perte de toutes les transactions depuis la migration. La différence, en durée d'indisponibilité, est d'un facteur cent.

🧪 **EN PRATIQUE — la migration en expansion / contraction**

La méthode qui préserve la réversibilité consiste à découper en trois temps ce qu'on fait habituellement en un seul :

```
Étape 1 — Expansion   : ajouter la nouvelle structure, SANS retirer l'ancienne
                        → les deux versions du code fonctionnent
Étape 2 — Migration   : le nouveau code écrit dans les deux structures
                        → réversible à tout moment
Étape 3 — Contraction : retirer l'ancienne structure, une fois la stabilité confirmée
                        → point de non-retour, franchi consciemment et à froid
```

Entre l'étape 1 et l'étape 3, le retour arrière reste trivial. Le point de non-retour n'est pas supprimé, il est **déplacé** à un moment que vous choisissez, au calme, plutôt que subi en pleine nuit.

✅ **BONNE PRATIQUE (P1)** — Toute demande de changement impliquant une migration de schéma doit indiquer explicitement, dans son plan de retour arrière : *à partir de quel instant précis le retour arrière ne sera plus possible sans restauration de données*. Cette seule ligne change la nature de la discussion en comité.

#### 6.8 Observabilité et critères d'arrêt automatiques

Déployer progressivement ne sert à rien si vous ne savez pas détecter que ça se passe mal. C'est pourtant la situation la plus fréquente : on déploie sur 5 % du parc, puis on attend « un peu », puis on continue — sans critère.

**Ce qu'il faut mesurer, avant / pendant / après.** Trois familles suffisent :

| Famille | Exemples | Ce qu'elle détecte |
|---|---|---|
| Santé technique | Taux d'erreur, temps de réponse, redémarrages inattendus, consommation mémoire | Régression franche |
| Santé fonctionnelle | Nombre de transactions métier abouties par minute | Régression silencieuse : le service répond, mais ne fait plus son travail |
| Santé du déploiement | Taux d'échec d'installation, actifs non joignables, écarts de version | Problème de la campagne elle-même |

La deuxième ligne est celle qu'on oublie, et c'est la plus importante. Un service qui répond « 200 OK » à toutes les requêtes tout en ayant cessé d'enregistrer les commandes passe tous les contrôles techniques.

**Le critère d'arrêt automatique.** Un déploiement doit s'interrompre **tout seul** quand un seuil est franchi, sans attendre qu'un humain regarde un écran. Formulez-le à l'avance et de manière chiffrée : *si le taux d'erreur dépasse X sur Y minutes, ou si le volume de transactions abouties baisse de Z %, la campagne s'arrête et alerte.*

⚠️ **PIÈGE — le seuil défini après le déploiement**
Un seuil discuté pendant l'incident sera toujours interprété dans le sens de « on continue » : personne n'aime arrêter une campagne à moitié faite. Le seuil doit être écrit dans la demande de changement, avant.

#### 6.9 Le retour arrière : ce qui est réellement réversible

Reprenons le §2.5 et généralisons.

| Objet | Réversibilité réelle | Mécanisme à privilégier |
|---|---|---|
| Application sans état | Élevée | Redéploiement de la version antérieure |
| Conteneur | Très élevée | Redéploiement de l'image précédente |
| Machine virtuelle | Élevée | Instantané pris avant l'intervention |
| Correctif de système d'exploitation | **Variable, à vérifier** | Instantané ou redéploiement, jamais la désinstallation seule |
| Micrologiciel | Faible à nulle | Double partition d'image quand elle existe (§2.7) |
| Migration de schéma | **Nulle après contraction** | Découpage expansion/contraction (§6.7) |
| Modification d'annuaire | Faible | Sauvegarde autorisée + procédure documentée |

**La règle unique** : un plan de retour arrière **non testé** n'est pas un plan, c'est une intention. Testez-le sur un environnement représentatif, chronométrez-le, et notez sa durée dans la demande de changement — parce que c'est cette durée, et non la probabilité de l'incident, qui déterminera si vous osez déployer.

#### 6.10 Images immuables : la correction devient un déploiement ordinaire

Le §3.5 a présenté le principe. Voici ce qu'il change concrètement pour le MCS.

Dans un modèle mutable, corriger consiste à intervenir sur un système en fonctionnement : opération d'exception, à risque, difficile à répéter à l'identique, et qui laisse le système dans un état légèrement différent de tous les autres.

Dans un modèle immuable, corriger consiste à **reconstruire l'image de référence et à redéployer**. Autrement dit : la correction emprunte exactement le même chemin, les mêmes tests et les mêmes automatismes qu'une livraison applicative ordinaire. Elle cesse d'être un sujet à part.

Quatre bénéfices, tous directement mesurables :

1. la dérive de configuration disparaît par construction (chapitre 23) ;
2. le retour arrière devient trivial : redéployer l'image précédente ;
3. la preuve devient triviale : l'identifiant d'image porte l'information de version ;
4. le nombre de constats individuels s'effondre au profit d'un seul indicateur — l'âge de l'image.

📌 **LIMITES** — Le modèle ne s'applique pas à tout : composants à état, systèmes industriels, matériel physique, appliances fournisseur. Et il déplace la charge vers la chaîne de construction, qui devient elle-même un actif critique à maintenir (chapitre 28).

#### 6.11 Concevoir un mécanisme de mise à jour sécurisé

Cette section concerne ceux qui **fabriquent** un produit installé chez des clients — matériel connecté, logiciel embarqué, appliance, application déployée sur site. Elle est reprise et approfondie au chapitre 33.

Un mécanisme de mise à jour est un chemin d'exécution privilégié offert au fournisseur. Mal conçu, il devient un chemin d'exécution privilégié offert à un attaquant. Six propriétés le rendent sûr.

| Propriété | Ce qu'elle empêche |
|---|---|
| **Authenticité** | Le produit vérifie la signature de la mise à jour avant installation — sinon n'importe qui peut livrer du code |
| **Intégrité** | Empreinte vérifiée, transport protégé — contre l'altération en chemin |
| **Protection contre le retour en arrière** | Refus d'installer une version antérieure vulnérable — sinon l'attaquant « rétrograde » pour retrouver une faille |
| **Atomicité** | Installation complète ou nulle, jamais à moitié — une coupure de courant ne doit pas produire un équipement inutilisable |
| **Repli sûr** | En cas d'échec, retour automatique à la version précédente fonctionnelle |
| **Traçabilité** | Le produit sait dire quelle version il exécute, et le fournisseur sait quelles versions sont déployées |

⚠️ **PIÈGE — le mécanisme qui n'existe pas**
Beaucoup de produits industriels et connectés se mettent à jour par intervention manuelle sur site, avec un support amovible. C'est un choix de conception dont la conséquence est mécanique : la cadence de correction sera annuelle au mieux. Si vous **achetez** un tel produit, sachez-le avant, pas après — c'est l'exigence n° 5 du §6.2. Si vous le **fabriquez**, c'est une dette qui deviendra réglementaire (chapitre 33).

#### 6.12 Des environnements de test réellement représentatifs

Toutes les stratégies de ce chapitre supposent qu'on puisse tester avant. Or c'est le maillon le plus faible en pratique.

**Les cinq écarts qui font qu'un test ne prouve rien :**

| Écart | Ce qu'il laisse passer |
|---|---|
| Volume de données sans commune mesure | Les régressions de performance, invisibles sur 200 lignes |
| Versions différentes de celles de production | Le test valide autre chose que ce que vous déploierez |
| Intégrations tierces simulées | Tout ce qui casse à la frontière — c'est-à-dire l'essentiel |
| Configuration divergente | Les effets liés au durcissement, aux droits, au réseau |
| Environnement figé depuis des mois | Il ne représente plus rien, y compris sa propre sécurité (chapitre 28) |

✅ **BONNE PRATIQUE (P1)** — Plutôt que de viser un environnement de recette parfait — objectif rarement atteint —, mesurez et affichez l'**écart** entre recette et production sur quatre axes : versions, volumétrie, intégrations, configuration. Un écart connu se compense par un déploiement témoin plus prudent ; un écart ignoré produit de la fausse confiance, ce qui est bien pire que pas de test du tout.

#### 6.13 Le coût réel d'un système impossible à arrêter

Voici l'argument à porter en comité, parce qu'il transforme une exigence technique en décision économique.

**La formulation.** Un système non interruptible impose un coût récurrent qui n'apparaît dans aucun budget :

- l'interruption est repoussée jusqu'à une fenêtre annuelle, donc le délai moyen de correction se compte en mois ;
- chaque intervention devient un projet, avec préparation, validation, mobilisation nocturne, astreinte ;
- l'exposition prolongée impose des mesures compensatoires, qui ont leur propre coût de mise en œuvre et de surveillance (chapitre 20) ;
- le risque résiduel est porté par l'organisation pendant toute la période.

**La comparaison à présenter.** Mettez face à face le coût d'ajout de la redondance — souvent une instance supplémentaire et quelques jours d'ingénierie — et le coût annuel du non-interruptible : heures d'astreinte, mesures compensatoires, surveillance dédiée, temps de négociation, et le montant du risque accepté. Dans la plupart des cas, l'écart est spectaculaire, et il n'a jamais été calculé.

C'est l'un des rares arguments de MCS qui se gagne sur le terrain financier plutôt que sur le terrain du risque. Le chapitre 37 en fait un outil de dossier d'investissement.

#### 6.14 ✅ Livrable — Grille d'évaluation de la maintenabilité sécurisée

À utiliser en revue d'architecture, en évaluation d'un progiciel, ou en état des lieux d'un système existant. Notation : **0** absent · **1** partiel · **2** satisfaisant.

| # | Critère | Question de vérification | Prio |
|---|---|---|---|
| 1 | Interruptibilité | Peut-on arrêter un composant en journée sans impact utilisateur ? | **P0** |
| 2 | Redondance effective | La capacité restante suffit-elle avec un membre en moins ? | **P0** |
| 3 | Bascule testée | Quand la dernière bascule a-t-elle été réalisée, et par qui ? | **P0** |
| 4 | Retour arrière | Existe-t-il, est-il documenté, a-t-il été chronométré ? | **P0** |
| 5 | Point de non-retour | Est-il identifié et écrit dans la demande de changement ? | **P0** |
| 6 | Découplage de version | Le système impose-t-il une version figée d'un composant sous-jacent ? | **P0** |
| 7 | Cadence supportée | Le système supporte-t-il une correction mensuelle ? | P1 |
| 8 | Stratégie de déploiement | Progressive, bleu/vert ou témoin — laquelle, et est-elle outillée ? | P1 |
| 9 | Critères d'arrêt | Sont-ils chiffrés et automatiques ? | P1 |
| 10 | Observabilité fonctionnelle | Sait-on détecter un service qui répond mais ne fait plus son travail ? | P1 |
| 11 | Compatibilité d'interface | Deux versions peuvent-elles coexister ? | P1 |
| 12 | Inventaire des composants | Le système déclare-t-il ses composants et versions ? | P1 |
| 13 | Représentativité de la recette | L'écart avec la production est-il mesuré sur quatre axes ? | P1 |
| 14 | Mécanisme de mise à jour | Signé, atomique, avec repli et protection contre le retour en arrière ? | P1 |
| 15 | Engagement de support | Durée et préavis de fin de support contractualisés ? | P2 |
| 16 | Décommissionnement | La procédure de retrait est-elle prévue dès la conception ? | P2 |

**Lecture du résultat.** Un seul critère P0 à 0 suffit à qualifier le système de non maintenable en sécurité — et cette qualification doit figurer dans le dossier, avec ses conséquences chiffrées, plutôt que d'être découverte trois ans plus tard par l'équipe d'exploitation.

#### 6.15 🔴 FIL ROUGE — avril 2026 : la revue d'architecture d'HelioLink

La grille du §6.14 est appliquée pour la première fois chez HELIOMED, non pas sur un système existant, mais sur la refonte de la plateforme de télésuivi HelioLink, dont le développement démarre à Nantes.

**Ce que la grille révèle en deux heures de réunion.**

| Critère | Note | Constat |
|---|---|---|
| Interruptibilité | 0 | Une seule instance applicative ; toute mise à jour coupe le service de télésuivi |
| Redondance effective | 0 | Base de données unique, non répliquée |
| Point de non-retour | 0 | Les migrations de schéma sont appliquées en une passe, sans découpage |
| Découplage de version | 1 | L'application impose une version précise d'un environnement d'exécution, déjà en fin de support dans 14 mois |
| Observabilité fonctionnelle | 0 | Supervision technique uniquement ; rien ne mesure les remontées de télésuivi abouties |

Yann Prigent, responsable produit, oppose l'argument habituel et parfaitement recevable : ajouter de la redondance représente quatre semaines d'ingénierie et une instance supplémentaire, alors que la mise sur le marché est déjà tendue.

**L'argument qui emporte la décision** n'est pas un argument de sécurité. Claire Nadeau applique le §6.13 et présente deux colonnes : le coût de la redondance, contre le coût annuel prévisionnel d'un système non interruptible sur un service de télésuivi médical — interventions nocturnes obligatoires, astreinte, fenêtres à négocier avec les établissements de santé clients, et surtout **impossibilité de corriger rapidement une vulnérabilité exposée sur un service traitant des données de santé**. La comparaison n'est pas serrée.

**Décisions prises.**

1. Redondance applicative et réplication de base de données ajoutées au périmètre initial — quatre semaines de décalage acceptées par la direction générale.
2. Découpage systématique des migrations de schéma en expansion / contraction, inscrit dans les règles de développement.
3. Deux indicateurs fonctionnels créés avant la mise en production, avec seuils d'arrêt automatique chiffrés.
4. Le point de découplage de l'environnement d'exécution est traité comme une dette datée, avec échéance inscrite au plan d'obsolescence (chapitre 12) — c'est un report assumé et tracé, pas un oubli.

**Livrable de l'épisode.** La grille du §6.14 devient un document de revue obligatoire pour tout nouveau projet chez HELIOMED, avec une règle simple : un critère P0 à zéro ne bloque pas le projet, mais impose une décision explicite de la direction générale, écrite et datée.

→ La suite en 🔴 §7.7, quand ces principes doivent devenir une politique applicable à l'ensemble du parc existant.

→ **Chapitre 7 — Doctrine et politique MCS** : la doctrine : transformer ces principes en une politique réellement applicable.

#### Synthèse mentale du chapitre 6

Le coût du MCS se décide en conception, pas en exploitation : un système qu'on ne peut pas arrêter ne sera pas corrigé, quelle que soit la politique. Sept exigences de maintenabilité, écrites dans un cahier des charges, se négocient tant qu'on a encore un levier — avant la signature. La redondance ne sert le MCS que si elle survit au test « peut-on en arrêter un membre maintenant, en pleine journée » : les faux clusters sont nombreux. Les stratégies progressive, bleu/vert et témoin permettent de corriger sans pari, et les interrupteurs de fonctionnalité découplent le déploiement de l'activation, ce qui offre aussi une mesure compensatoire propre. Les migrations de schéma détruisent silencieusement la réversibilité : le découpage expansion/contraction déplace le point de non-retour à un moment choisi. Un déploiement doit s'arrêter tout seul sur des seuils chiffrés à l'avance, dont au moins un indicateur fonctionnel — un service peut répondre parfaitement tout en ayant cessé de faire son travail. Enfin, un plan de retour arrière non testé n'est pas un plan, et le coût d'un système non interruptible se démontre en euros, pas en risque.

**Trois questions de vérification**

1. Votre architecte affirme que le service est redondé et donc corrigeable sans interruption. Quelle question unique posez-vous pour vérifier, et quelles sont les trois réponses évasives typiques ?
2. Une mise à jour applicative comporte une migration de base de données. Que devez-vous obtenir avant d'autoriser le changement, et pourquoi cette information change-t-elle la nature du plan de retour arrière ?
3. Un chef de projet refuse d'ajouter une seconde instance pour cause de budget. Construisez l'argument économique en quatre postes de coût récurrent.

---

---

> ### 🎓 À ce stade de la Partie I, vous savez…
>
> - **distinguer** le MCS du maintien opérationnel, et nommer les cinq causes récurrentes d'échec — dont aucune n'est exclusivement technique ;
> - **expliquer** pourquoi un numéro de version amont ne dit rien de la présence d'une faille sur un système à support long, et le vérifier en trois commandes ;
> - **situer** une frontière de responsabilité sur n'importe quelle couche d'abstraction : hyperviseur, conteneur, orchestrateur, cloud, industriel, micrologiciel ;
> - **lire** un constat de vulnérabilité sans confondre gravité, probabilité, exploitation avérée et exposition — et savoir laquelle de ces informations personne ne produira à votre place ;
> - **qualifier** une information en fait vérifié, hypothèse probable ou piste exploratoire ;
> - **poser** la question qui débloque le plus de situations : *qui décide qu'on l'arrête pour le corriger ?* ;
> - **évaluer** la maintenabilité d'un système en conception, et chiffrer le coût d'un système impossible à arrêter.
>
> **Ce que vous ne savez pas encore** : sur quoi exactement porte votre dispositif, qui arbitre, et ce que l'extérieur exige. C'est l'objet de la Partie II.


## PARTIE II — Cadre, périmètre et gouvernance

La Partie I a installé le socle : ce qu'est le MCS, comment fonctionnent les mécanismes techniques, quel vocabulaire décrit les vulnérabilités, quels processus encadrent le changement, et comment concevoir des systèmes qu'on puisse maintenir.

La Partie II répond à trois questions d'organisation : **sur quoi s'applique le MCS** (périmètre, inventaire, exposition, obsolescence), **qui décide** (doctrine, gouvernance), et **ce que l'extérieur exige** (cadre réglementaire, contrats de délégation).

---

### Chapitre 7 — Doctrine et politique MCS

#### 7.1 Ce qui distingue une politique appliquée d'un document mort

La plupart des organisations ont déjà une politique de sécurité qui mentionne les correctifs. La plupart de ces mentions ne sont pas appliquées. La différence entre les deux situations ne tient pas à la qualité rédactionnelle, mais à trois propriétés très concrètes.

**Une politique appliquée est décidable.** Chaque phrase doit permettre de trancher un cas réel. « Les correctifs de sécurité sont appliqués dans les meilleurs délais » ne permet de trancher aucun cas : quel délai, sur quel actif, décidé par qui. À l'inverse, « les correctifs concernant une vulnérabilité exploitée sur un actif exposé à Internet sont appliqués sous 72 heures, y compris hors fenêtre, sur décision du propriétaire technique » se vérifie et s'oppose.

**Une politique appliquée est finançable.** Si elle impose un scan authentifié mensuel du parc alors qu'aucune licence ni aucun temps homme n'y sont affectés, elle organise sa propre violation. Une politique qui dépasse les moyens engagés génère une non-conformité permanente, ce qui est pire que l'absence de politique : cela habitue tout le monde à ce que la règle ne soit pas tenue.

**Une politique appliquée prévoit sa propre transgression.** C'est le point le plus contre-intuitif et le plus important. Il existera toujours des situations où corriger est impossible. Si la politique ne prévoit pas de chemin légitime pour ces cas — la dérogation du §7.4 — les équipes emprunteront un chemin illégitime : le silence.

**Structure recommandée.** Un document court, de huit à douze pages, en sept sections :

| Section | Contenu | Longueur indicative |
|---|---|---|
| 1. Objet et périmètre | Ce qui est couvert, ce qui ne l'est pas et pourquoi | ½ page |
| 2. Définitions | Vocabulaire arrêté, notamment actif, propriétaire, couverture, conformité | 1 page |
| 3. Rôles et responsabilités | Renvoi au RACI, décideurs nommés par catégorie | 1 page |
| 4. Classes de service | Le cœur du document (§7.2) | 2-3 pages |
| 5. Processus | Veille, détection, triage, correction, vérification, preuve | 2-3 pages |
| 6. Dérogations | Procédure, durée, signataires, revue (§7.4) | 1 page |
| 7. Mesure et contrôle | Indicateurs, fréquence, destinataires | 1 page |

⚠️ **PIÈGE — la politique qui liste des outils**
Une politique qui nomme des produits devient obsolète au premier changement d'outillage, et elle transforme un document de doctrine en documentation technique. Les outils vivent dans les procédures d'exploitation, qui se modifient sans passer par le circuit d'approbation de la politique.

#### 7.2 Les classes de service : le cœur du dispositif

C'est la section qui rend une politique opérationnelle. L'idée : **on ne traite pas tous les actifs de la même façon**, et cette différenciation doit être écrite, pas improvisée.

**Construire les classes.** Trois à quatre classes suffisent — au-delà, plus personne ne sait dans laquelle ranger un actif. Le critère de classement combine deux dimensions : la **criticité métier** (que se passe-t-il si cet actif tombe ou fuit ?) et l'**exposition** (qui peut l'atteindre ?).

| Classe | Définition | Exemples typiques |
|---|---|---|
| **C1 — Critique exposé** | Actif de niveau 0, ou joignable depuis Internet, ou portant une donnée sensible | Passerelle d'accès distant, annuaire, hyperviseur, console de sauvegarde, service public |
| **C2 — Important** | Actif métier significatif, non exposé directement | Serveurs applicatifs internes, bases de données métier |
| **C3 — Courant** | Actif dont l'indisponibilité est tolérable | Postes de travail standard, serveurs de fichiers secondaires |
| **C4 — Contraint** | Actif que l'on ne peut pas corriger normalement | Systèmes industriels, legacy sous contrat figé, appliances fermées |

La classe C4 est indispensable et souvent oubliée. Sans elle, ces actifs sont classés dans une catégorie dont ils violeront en permanence les règles, ce qui pollue tous les indicateurs. Les nommer explicitement permet de leur appliquer un régime différent — compensation obligatoire plutôt que correction — et de mesurer honnêtement.

**Ce que chaque classe définit.** Pour chaque classe, six paramètres, et pas un de plus :

| Paramètre | C1 | C2 | C3 | C4 |
|---|---|---|---|---|
| Délai de correction — vulnérabilité exploitée | 72 h | 7 j | 30 j | Compensation sous 72 h |
| Délai de correction — critique non exploitée | 15 j | 30 j | 60 j | Compensation ou dérogation |
| Délai — reste | 30 j | 90 j | 180 j | Selon fenêtre constructeur |
| Fréquence de vérification | Hebdomadaire | Mensuelle | Mensuelle | Trimestrielle |
| Niveau de test avant déploiement | Recette + témoin | Témoin | Anneau pilote | Validation fournisseur |
| Fenêtre | Récurrente hebdomadaire + urgence autorisée | Mensuelle | Mensuelle | Arrêt planifié |

*Les valeurs ci-dessus sont un point de départ réaliste pour une organisation de taille intermédiaire, pas une norme. Ce qui compte n'est pas le chiffre, c'est qu'il soit **écrit, tenable et mesuré**.*

✅ **BONNE PRATIQUE (P0)** — Calibrez vos délais sur ce que vous pouvez réellement tenir, pas sur ce qui fait bien. Une politique annonçant 48 h que vous tenez trois fois par an vous met en position de non-conformité permanente devant un auditeur, un assureur ou un client. Une politique annonçant 15 jours et tenue à 92 % est infiniment plus solide — et vous pourrez la resserrer ensuite, ce qui est un progrès démontrable.

#### 7.3 Le contrat interne entre sécurité et production

Le conflit MCO/MCS du §1.2 ne se résout pas par autorité. Il se résout par un engagement **réciproque**, formalisé dans la politique, et c'est la réciprocité qui le rend applicable.

**Ce que la sécurité s'engage à fournir :**

- un périmètre et une priorisation stables, pas une liste de 4 000 constats à trier soi-même ;
- un volume de demandes compatible avec les moyens de l'exploitation, avec un plafond mensuel assumé ;
- une qualification préalable de chaque demande urgente — exposition mesurée, exploitation vérifiée, pas de fausse alerte ;
- l'acceptation formelle du risque lorsqu'un report est décidé, portée par la sécurité et non par l'exploitant.

**Ce que la production s'engage à fournir :**

- des fenêtres récurrentes garanties, pas renégociées mensuellement ;
- l'application dans les délais définis par classe de service ;
- la remontée d'une preuve exploitable, pas une confirmation verbale ;
- l'alerte immédiate en cas d'impossibilité, plutôt que le silence — c'est la contrepartie de l'existence d'une procédure de dérogation.

Ce dernier point est le pivot. **Le silence est le pire résultat possible** : il produit un écart invisible, donc non compensé, donc non financé. Une organisation qui punit les remontées d'impossibilité fabrique mécaniquement son propre angle mort.

#### 7.4 La procédure de dérogation

Une dérogation est une décision formelle de ne pas appliquer la règle, pour un actif, une vulnérabilité et une durée déterminés. Bien conçue, c'est un instrument de pilotage. Mal conçue, c'est une machine à dissimuler.

**Les sept champs obligatoires** — repris de la logique du §5.3 et développés au chapitre 20 :

| Champ | Pourquoi il est indispensable |
|---|---|
| Objet précis | Quel actif, quelle vulnérabilité, quel correctif — jamais « les serveurs de l'usine » |
| Motif | Technique, contractuel, métier, budgétaire — le motif oriente la solution |
| **Date d'expiration** | Une dérogation sans date est une renonciation |
| Mesure compensatoire | Obligatoire ; une dérogation nue n'est pas acceptable |
| Moyen de vérification | Comment saura-t-on que la compensation est toujours en place ? |
| Signataire | Le propriétaire métier, pas la sécurité — celui qui porte le risque le signe |
| Condition de sortie | Quel événement met fin à la dérogation |

⚠️ **PIÈGE — la dérogation renouvelée par défaut**
Le mécanisme de dégradation est toujours le même : la dérogation arrive à échéance, rien n'a changé, on reconduit. Trois ans plus tard, elle est devenue un état permanent que plus personne n'interroge.
**Le garde-fou qui fonctionne** : le renouvellement d'une dérogation exige une signature de **niveau supérieur** à la précédente. Le premier renouvellement remonte au directeur des systèmes d'information, le second à la direction générale. Le coût politique croissant force l'arbitrage — soit on corrige, soit on assume au bon niveau.

✅ **BONNE PRATIQUE (P1)** — Suivez l'**âge moyen des dérogations ouvertes** comme indicateur de premier plan (chapitre 38). C'est la mesure la plus honnête de la dette de sécurité réellement acceptée par l'organisation, et elle est plus parlante en comité que n'importe quel décompte de vulnérabilités.

#### 7.5 Obtenir le sponsor : construire l'argumentaire

Un programme de MCS sans soutien explicite de la direction générale échouera sur le premier arbitrage sérieux. Voici les quatre leviers qui fonctionnent, par ordre d'efficacité constatée.

**1. L'exigence externe.** Un assureur, un client, un auditeur ou un régulateur qui demande une preuve crée une obligation que la sécurité seule ne peut pas créer. C'est le levier le plus rapide, et il est souvent déjà disponible — il suffit de le lire.

**2. L'incident sectoriel.** Un concurrent ou un pair touché, publiquement, avec un vecteur d'entrée documenté que vous partagez. La fenêtre d'attention est courte : quelques semaines. Préparez le dossier à l'avance pour pouvoir le sortir au bon moment.

**3. Le coût du non-fait, chiffré.** L'approche du §6.13, appliquée à l'échelle du programme : coût des interventions en urgence, des mesures compensatoires, du support étendu, des heures d'astreinte, comparé au coût de la mise à niveau. Ce levier est le plus solide dans la durée, parce qu'il ne dépend pas de l'émotion.

**4. Le risque, en dernier.** Contre-intuitif, mais l'expérience est constante : l'argument « nous pourrions être attaqués » est le moins efficace des quatre auprès d'une direction générale, parce qu'il est invérifiable et que tout le monde l'a déjà entendu.

📌 **LIMITES** — Aucun de ces leviers ne produit un budget pérenne à lui seul. Ce qui pérennise, c'est la **démonstration de progrès mesuré** : un indicateur de résultat qui s'améliore trimestre après trimestre transforme une dépense en investissement aux yeux d'un directeur financier. C'est pourquoi le chapitre 38 arrive avant le chapitre 40.

#### 7.6 ⚠️ Les politiques mort-nées : symptômes, causes, réanimation

| Symptôme observable | Cause profonde | Ce qui la réanime |
|---|---|---|
| Personne ne peut citer un délai de correction | Politique trop générale, non décidable | Réécrire la section classes de service, supprimer le reste |
| Aucune dérogation enregistrée depuis un an | Ce n'est pas que tout est corrigé : c'est que les écarts sont invisibles | Rendre la dérogation facile, rapide et non punitive |
| Les indicateurs sont excellents et personne n'y croit | Dénominateur faux (§2.9) | Publier le périmètre de référence avec le chiffre |
| Le document date de trois ans | Aucun propriétaire ni revue planifiée | Nommer un propriétaire et une date de revue annuelle |
| Elle s'applique à « tous les systèmes » | Aucune classe C4 : les cas contraints violent la règle en permanence | Créer la classe des actifs contraints et l'assumer |

#### 7.7 🔴 FIL ROUGE — mai 2026 : la politique MCS v1 et ses trois compromis

Claire Nadeau rédige la première politique MCS d'HELIOMED. Onze pages. Trois compromis y sont assumés explicitement, et c'est ce qui la rend applicable.

**Compromis n° 1 — des délais volontairement modestes.** Le premier projet annonçait 24 h pour une vulnérabilité exploitée en classe C1. Malik Ferhaoui démontre chiffres à l'appui que l'équipe, à deux personnes, ne peut pas le tenir en dehors d'une mobilisation exceptionnelle. Le délai retenu est **72 h**, avec un engagement de révision à 48 h une fois l'outillage d'anneaux en place. Claire préfère un engagement tenu à un affichage flatteur.

**Compromis n° 2 — l'usine sort du régime commun.** Les actifs de Saint-Étienne entrent en classe C4 : régime de compensation et non de correction, fenêtre unique lors de l'arrêt de production d'août, revue trimestrielle. Thomas Berger signe, parce que la règle correspond enfin à ce qu'il peut réellement faire. Les indicateurs les distinguent désormais du reste du parc — le taux de conformité global cesse d'être pollué par des actifs qu'on savait non corrigeables.

**Compromis n° 3 — le parc infogéré reste hors périmètre de mesure, temporairement.** Les 620 postes gérés par le prestataire Numeria ne peuvent pas être mesurés faute d'accès aux données de la console du prestataire. Plutôt que de publier un chiffre inventé, la politique déclare explicitement : *périmètre non mesuré, échéance de mise sous contrôle au 31/12/2026, traité par avenant contractuel.* Ce trou déclaré deviendra l'un des deux leviers de la renégociation du chapitre 13.

**La clause qui déclenche le plus de discussion** est celle du renouvellement de dérogation avec signature de niveau supérieur. Deux responsables y voient une marque de défiance. Pierre Vasseur, directeur général, tranche en trois phrases : si une exception est justifiée, la signer ne coûte rien ; si elle ne l'est pas, il vaut mieux qu'il l'apprenne maintenant.

**Livrable de l'épisode.** La politique MCS v1, plus une annexe d'une page listant les périmètres explicitement non couverts avec leur échéance de mise sous contrôle. Cette annexe, apparemment un aveu de faiblesse, sera l'élément le mieux noté lors de la revue de janvier 2027 (chapitre 39).

→ La suite en 🔴 §8.10, quand un référentiel publié en mars vient confronter cette politique à une grille externe.

→ **Chapitre 8 — Cadre réglementaire et normatif applicable** : ce que l'extérieur exige, et comment lire un référentiel sans s'y perdre.

#### Synthèse mentale du chapitre 7

Une politique MCS n'est utile que si chacune de ses phrases permet de trancher un cas réel, si les moyens de l'appliquer sont engagés, et si elle prévoit un chemin légitime pour les cas où corriger est impossible — faute de quoi les équipes emprunteront le chemin du silence. Son cœur est la table des classes de service : trois à quatre classes croisant criticité métier et exposition, dont une classe explicite pour les actifs contraints qu'on sait ne pas pouvoir corriger. Les délais doivent être calibrés sur ce qu'on tient réellement, pas sur ce qui impressionne. Le conflit avec la production se résout par un engagement réciproque dont le pivot est la remontée immédiate des impossibilités. Une dérogation comporte sept champs, dont une date d'expiration et une mesure compensatoire, et son renouvellement doit coûter politiquement plus cher que le précédent. Enfin, l'argument qui obtient un sponsor est rarement le risque : c'est l'exigence externe, l'incident sectoriel ou le coût chiffré du non-fait.

**Trois questions de vérification**

1. Votre politique annonce un délai de correction de 48 heures que vous tenez trois fois par an. Pourquoi est-ce plus dangereux que d'annoncer 15 jours, et devant qui ?
2. Aucune dérogation n'a été enregistrée dans votre organisation depuis douze mois. Quelle est l'interprétation optimiste, quelle est l'interprétation réaliste, et comment tranchez-vous ?
3. Pourquoi une classe de service dédiée aux actifs non corrigeables améliore-t-elle la qualité de vos indicateurs plutôt que de la dégrader ?

---

### Chapitre 8 — Cadre réglementaire et normatif applicable

> ⏱ **Chapitre entièrement périssable.** Toutes les données de ce chapitre ont été vérifiées le **30 juillet 2026**. Le raisonnement, la méthode de lecture et la matrice du §8.8 restent valables ; les statuts, dates et échéances doivent être revérifiés à chaque revue du cours. Les déclencheurs de revue anticipée figurent en tête du document.

Ce chapitre n'a pas vocation à faire de vous un juriste. Il répond à trois questions pratiques : **qu'est-ce qui m'oblige, à quoi exactement, et quelle preuve devrai-je produire ?** La grille de lecture exigence / objectif / moyen du §5.4 s'applique de bout en bout.

#### 8.1 NIS2 et la transposition française

**Ce dont il s'agit.** La directive européenne dite NIS2 élargit considérablement le périmètre des organisations soumises à des obligations de cybersécurité, par rapport au dispositif précédent. Elle introduit deux catégories — **entités essentielles** et **entités importantes** — définies par secteur d'activité et par taille, avec des régimes de contrôle différents : supervision *a priori* pour les premières, contrôle *a posteriori* sur signalement pour les secondes. Les sanctions prévues sont significatives et la responsabilité des dirigeants est explicitement engagée.

Pour une entreprise privée, les obligations opérationnelles sont principalement mises en œuvre par le droit national de transposition. Le statut exact et les effets d'une directive non transposée dans les délais doivent être vérifiés dans chaque juridiction concernée — ce cours retient la lecture pratique : tant que le texte national n'est pas publié, les obligations opposables restent celles du droit existant.

⏱ **ÉTAT DE L'ART — le statut en France au 30/07/2026**
Le véhicule législatif français de transposition — le projet de loi relatif à la résilience des infrastructures critiques et au renforcement de la cybersécurité, couramment appelé « loi Résilience » — **n'était pas promulgué** à cette date ; le dossier législatif restait ouvert. Le calendrier de transposition européen était donc largement dépassé.
📎 [S-01] [S-02] — directive et dossier législatif public, consultés le 30/07/2026.

**Ce que cela change pour votre programme de MCS — et c'est le point important du chapitre.** L'absence de texte national applicable ne suspend rien, pour trois raisons :

1. Les délais de mise en conformité, une fois le texte publié, sont courts au regard du temps nécessaire pour construire un inventaire fiable et une propriété d'actif. Une organisation qui attend le texte pour commencer aura déjà perdu.
2. Vos **clients** vous imposeront des exigences avant le régulateur. Une entité soumise doit maîtriser sa chaîne de sous-traitance : les questionnaires arrivent donc en amont de la loi, et ils arrivent déjà.
3. Les mesures attendues sont, dans leur substance, celles que ce cours décrit — inventaire, gestion des vulnérabilités, gestion des correctifs, maîtrise de la chaîne d'approvisionnement, gestion des incidents. Elles sont utiles indépendamment du texte qui les rendra obligatoires.

✅ **BONNE PRATIQUE (P0)** — Traitez l'incertitude réglementaire comme une **donnée de pilotage**, pas comme un motif d'attente. Concrètement : construisez le dispositif sur la base du projet de référentiel disponible (§8.2), documentez vos choix de calibrage, et prévoyez une revue d'écart à la publication du texte définitif. C'est exactement la position tenable devant un comité de direction qui demande « faut-il attendre ? ».

#### 8.2 Le ReCyF : le référentiel d'application

**Ce dont il s'agit.** Un texte de loi énonce des exigences générales. Il faut un référentiel intermédiaire pour traduire ces exigences en objectifs de sécurité vérifiables. C'est le rôle du ReCyF — référentiel d'exigences de cybersécurité destiné aux entités françaises concernées — élaboré par l'ANSSI.

**Sa structure, et pourquoi elle est bien conçue.** Le référentiel s'organise en une vingtaine d'**objectifs de sécurité**, chacun décliné en exigences, avec pour chacune :

- une **modulation selon la catégorie** de l'entité (essentielle ou importante) ;
- des **moyens acceptables de conformité**, c'est-à-dire des exemples de mise en œuvre reconnus — sans être les seuls admis ;
- l'application du principe de **proportionnalité** : les mesures attendues tiennent compte de la taille, de l'exposition et de la criticité de l'activité.

Cette structure est exactement la grille du §5.4, et elle vous laisse une liberté de mise en œuvre que beaucoup d'organisations n'exploitent pas — à condition de savoir **justifier** son calibrage, donc de l'avoir écrit.

**Ce qui touche directement le MCS.** Sans citer un découpage qui évoluera, les familles d'objectifs qui concernent ce cours sont : la connaissance et la maîtrise du patrimoine informationnel (inventaire, cartographie), la gestion des vulnérabilités et des mises à jour, la maîtrise des configurations, la gestion des accès et des comptes à privilèges, la maîtrise de la sous-traitance, la journalisation et la détection, la gestion des incidents, et la continuité.

⏱ **ÉTAT DE L'ART (vérifié le 30/07/2026)** — Le ReCyF était diffusé en **version de travail**, la dernière datant du **17 mars 2026**. Un document portant explicitement cette mention n'a pas de valeur opposable : il indique la direction, pas l'obligation.
📎 [S-03] — publication de l'agence, consultée le 30/07/2026. Les numéros d'objectifs cités dans ce cours devront être revérifiés contre la version définitive.

✅ **BONNE PRATIQUE (P1) — l'analyse d'écart anticipée**
Menez dès maintenant une analyse d'écart objectif par objectif, avec trois colonnes : *ce que nous faisons* · *ce que l'objectif attend* · *effort estimé*. Deux bénéfices immédiats, indépendants du calendrier réglementaire : vous obtenez une feuille de route priorisée, et vous disposez d'un document à présenter à un client ou à un assureur qui demande où vous en êtes.

#### 8.3 Le Cyber Resilience Act : la réglementation passe au produit

**Le changement de nature.** Toutes les réglementations précédentes s'adressent à l'organisation qui **exploite** un système d'information. Le règlement européen sur la cyberrésilience s'adresse à celui qui **met un produit sur le marché**. C'est un déplacement majeur : il crée des obligations de MCS pour les fabricants et éditeurs, sur des produits installés chez leurs clients.

**Le calendrier par paliers.**

| Étape | Date | Portée |
|---|---|---|
| Entrée en vigueur | 10 décembre 2024 | Le règlement existe, l'essentiel des obligations est différé |
| Chapitre relatif aux organismes d'évaluation de la conformité | 11 juin 2026 | Mise en place du dispositif d'évaluation |
| **Obligations de signalement** | **À compter du 11 septembre 2026** | Vulnérabilités activement exploitées et incidents graves |
| Application générale | 11 décembre 2027 | Exigences essentielles de sécurité, marquage, documentation |

**Les délais de signalement, formulés précisément** — c'est le point le plus souvent mal restitué :

| Échéance | Contenu | Point de départ |
|---|---|---|
| **≤ 24 h** | Alerte précoce | Prise de connaissance |
| **≤ 72 h** | Notification, avec les éléments connus et les mesures correctives ou d'atténuation | Prise de connaissance |
| **≤ 14 jours** | Rapport final, pour une **vulnérabilité activement exploitée** | **La mise à disposition d'une mesure corrective ou d'atténuation** — et non la découverte |
| **≤ 1 mois** | Rapport final, pour un **incident grave** | La notification initiale |

Le signalement s'effectue via une plateforme unique de déclaration au niveau européen, avec routage vers le CSIRT compétent.

⚠️ **PIÈGE — croire qu'il s'agit d'une obligation de paperasse**
Un délai de 24 heures pour l'alerte précoce n'est pas un problème de formulaire : c'est une **exigence de capacité organisationnelle**. Pour le tenir, il faut être capable de détecter qu'une vulnérabilité de son produit est activement exploitée chez des clients, de qualifier le périmètre affecté rapidement, et de disposer d'une chaîne de décision pré-autorisée — y compris un week-end d'août. Cette capacité se construit en mois, pas en jours. Le chapitre 33 en fait un module complet.

**Les exclusions de périmètre, et la méthode.** Certains produits sont exclus parce qu'ils relèvent d'un autre régime européen qui leur est propre : c'est notamment le cas des dispositifs médicaux couverts par la réglementation qui leur est applicable, et de plusieurs autres secteurs réglementés.

⚠️ La conséquence pratique est contre-intuitive et coûte cher aux organisations qui la manquent : **l'exclusion ne s'analyse pas par gamme commerciale, mais produit par produit**. Une même entreprise peut commercialiser un dispositif exclu, une passerelle incluse et une application mobile incluse. Et exclusion ne signifie pas absence d'exigences : le régime alternatif comporte ses propres obligations de cybersécurité. La grille d'analyse figure au §33.8.

#### 8.4 ISO/IEC 27001 et 27002 : les mesures qui portent le MCS

**Ce dont il s'agit.** Une norme internationale de management de la sécurité de l'information, certifiable. Elle n'est obligatoire pour personne, mais elle est massivement demandée par les clients — ce qui la rend contraignante en pratique.

**Ce qui compte pour ce cours.** Quatre mesures de l'annexe portent directement le MCS :

| Mesure | Objet | Chapitre du cours |
|---|---|---|
| **8.8** — Gestion des vulnérabilités techniques | Obtenir l'information sur les vulnérabilités, évaluer l'exposition, prendre les mesures | Ch. 14 à 18 |
| **8.9** — Gestion des configurations | Définir, documenter, appliquer et surveiller les configurations | Ch. 22 et 23 |
| **8.19** — Installation de logiciels sur les systèmes en exploitation | Encadrer ce qui est installé et par qui | Ch. 22, 26 |
| **8.32** — Gestion des changements | Encadrer les modifications de l'environnement de traitement | Ch. 5, 18 |

📎 [S-10] — ISO/IEC 27001:2022 annexe A et ISO/IEC 27002:2022.

**Ce qu'un auditeur regarde réellement**, sur ces quatre mesures : l'existence d'un processus documenté, la **preuve de son application** sur un échantillon d'actifs, la cohérence entre le périmètre déclaré et le périmètre mesuré, le traitement des exceptions, et la revue de direction. C'est-à-dire, très exactement, les livrables décrits aux chapitres 38 et 39.

📌 **LIMITES** — Une certification atteste qu'un système de management existe et fonctionne. Elle n'atteste pas que votre parc est à jour. Une organisation certifiée peut porter des actifs hors support, dès lors que c'est identifié, tracé, décidé et revu — mais un niveau élevé peut constituer une non-conformité selon le périmètre certifié, le traitement du risque retenu et l'efficacité démontrée des mesures. Ne confondez jamais certification et niveau de sécurité — et ne laissez personne le faire dans votre organisation.

#### 8.5 Le paysage sectoriel

Selon votre activité, d'autres textes s'ajoutent. Voici ce que chacun exige **spécifiquement** en matière de maintien.

| Cadre | Qui est concerné | Ce qu'il exige en propre pour le MCS |
|---|---|---|
| **Série IEC 62443** | Systèmes d'automatisation industriels : exploitants, intégrateurs, fabricants | Une gestion des correctifs adaptée au contexte industriel, la définition de zones et de conduits, et — côté fabricant — un cycle de développement sécurisé incluant la gestion des mises à jour de sécurité. Chapitre 29 |
| **Hébergement de données de santé** | Hébergeurs de données de santé à caractère personnel, et leurs clients par ricochet | Certification de l'hébergeur, exigences de maintien et de traçabilité, obligations contractuelles vers le client |
| **Qualification SecNumCloud** | Fournisseurs de services cloud visant les usages sensibles | Exigences détaillées de maintien en condition de sécurité, de gestion des vulnérabilités et de transparence vers le client |
| **PCI DSS** | Traitement de données de cartes de paiement | Le plus **prescriptif** de tous : délais chiffrés d'application des correctifs critiques, exigences de scan périodique interne et externe, exigences de gestion des changements |
| **DORA** | Secteur financier européen | Gestion du risque informatique, dont l'identification et le traitement des vulnérabilités, les tests, et la maîtrise renforcée des prestataires tiers critiques |

**L'enseignement transversal.** Ces cadres divergent sur la forme et convergent sur le fond : connaître son parc, détecter les vulnérabilités, les traiter selon des délais définis, tracer les exceptions, et prouver. Si vous construisez un dispositif solide, l'adaptation à un cadre supplémentaire relève surtout de la mise en forme documentaire. C'est le meilleur argument contre la construction d'un dispositif par référentiel.

#### 8.6 Le règlement général sur la protection des données

Souvent oublié dans les discussions de MCS, alors qu'il est le texte le plus universellement applicable.

Son article relatif à la sécurité du traitement impose des mesures techniques et organisationnelles appropriées au risque, en tenant compte de l'état de l'art. Les autorités de contrôle ont retenu à plusieurs reprises, dans des décisions publiées, qu'un **défaut de mise à jour d'un composant présentant une vulnérabilité connue et corrigée** pouvait caractériser un manquement, dès lors que ce défaut avait contribué à une violation de données. Chaque décision s'apprécie au cas d'espèce ; il convient de se référer aux délibérations publiées de l'autorité compétente plutôt qu'à une règle générale.

⚖️ **CADRE — ce qu'il faut en retenir opérationnellement**
Trois éléments sont regardés en cas de contrôle après incident : la vulnérabilité était-elle **connue et corrigée** au moment des faits ; l'organisation disposait-elle d'un **processus** permettant de la traiter ; et l'écart était-il **identifié et décidé**, ou simplement ignoré ? Une dérogation formalisée et compensée place l'organisation dans une position radicalement différente d'une absence totale de trace. C'est un argument de plus, et le plus concret, en faveur du §7.4.

#### 8.7 Un modèle méthodologique utile — et ses limites d'applicabilité

⏱ **ÉTAT DE L'ART (vérifié le 30/07/2026)** — L'agence américaine de cybersécurité a publié le **10 juin 2026** une directive opérationnelle contraignante (référencée BOD 26-04) organisant la priorisation des mises à jour de sécurité **par le risque** plutôt que par la seule gravité technique : prise en compte de l'exploitation observée, de l'exposition à Internet, et application d'une méthode par arbre de décision, avec des délais de remédiation différenciés.

⚠️ **Portée juridique — à ne jamais confondre.** Ce type de directive est **contraignant uniquement pour les agences civiles fédérales américaines**. Elle ne crée **aucune obligation** pour une organisation française ou européenne, publique ou privée.

📎 [S-21]

**Pourquoi elle figure malgré tout dans ce cours.** Parce qu'elle constitue un **modèle méthodologique documenté et public**, produit par une autorité qui gère un parc considérable, et qu'elle valide la même orientation que celle enseignée au chapitre 16 : la gravité technique seule ne suffit plus à prioriser. Vous pouvez vous en inspirer pour calibrer vos propres délais et défendre votre méthode — en citant une référence publique plutôt qu'une intuition. Vous ne pouvez pas vous en réclamer comme d'une obligation.

#### 8.8 ⚖️ Matrice « exigence → objectif → preuve attendue »

C'est le livrable de ce chapitre. Il fonctionne quel que soit le référentiel qui vous est opposé.

| Exigence type | Objectif de sécurité correspondant | Preuve à constituer |
|---|---|---|
| Connaître son patrimoine | Inventaire exhaustif, à jour, avec propriétaires | Périmètre de référence daté, sources réconciliées, écarts expliqués, taux de complétude (ch. 10) |
| Identifier les vulnérabilités | Détection périodique sur l'ensemble du périmètre | Rapports datés, couverture calculée et prouvée, liste des actifs non scannés (ch. 15) |
| Traiter en temps utile | Délais définis par criticité et tenus | Politique avec classes de service, mesure du respect des délais, historique (ch. 7, 38) |
| Gérer les exceptions | Décisions formalisées, bornées, compensées | Registre des dérogations avec signataires, dates, compensations, revues (ch. 7, 20) |
| Maîtriser les configurations | Référentiel de configuration appliqué et contrôlé | Baseline versionnée, résultats de contrôle, traitement des écarts (ch. 22) |
| Maîtriser la sous-traitance | Exigences contractuelles et vérification | Clauses, rapports du prestataire, contrôles réalisés (ch. 13) |
| Gérer les incidents | Procédure et capacité de réaction | Journal de crise, chronologies, retours d'expérience (ch. 21) |
| Piloter | Indicateurs suivis et revus par la direction | Tableaux de bord historisés, comptes rendus de comité avec décisions (ch. 38, 39) |

✅ **BONNE PRATIQUE (P0)** — Constituez le dossier de preuves **une fois**, dans cette structure, puis projetez-le sur chaque référentiel qui vous est opposé. L'erreur classique consiste à construire un dossier par certification, par client et par audit : vous multipliez la charge par le nombre d'interlocuteurs, et vous produisez des versions divergentes des mêmes faits.

#### 8.9 📌 Limites : la conformité n'est pas la sécurité

Trois avertissements, à garder présents chaque fois que ce chapitre sert d'argument.

**Aucun texte ne dit comment faire.** Ils fixent des résultats. Le savoir-faire — quels outils, quelle cadence, quelle méthode de triage, quel anneau de déploiement — est le sujet des chapitres 14 à 23, et il n'est écrit dans aucun référentiel.

**La conformité est un plancher, pas un objectif.** Une organisation peut être parfaitement conforme et se faire compromettre le lendemain par un chemin que le référentiel n'adresse pas.

**La conformité peut détourner les moyens.** Le risque le plus concret est de consacrer l'essentiel du budget à la production documentaire au détriment de la remédiation. Un indicateur simple permet de le suivre : la part du temps de l'équipe consacrée à produire de la preuve, rapportée au temps consacré à corriger. Aucun seuil universel n'existe — mais une croissance continue de ce ratio, sans amélioration des indicateurs de résultat, mérite un examen.

#### 8.10 🔴 FIL ROUGE — juin 2026 : l'analyse d'écart

Claire Nadeau conduit l'analyse d'écart d'HELIOMED contre le référentiel disponible, un mois après la publication de la politique MCS v1. Vingt objectifs passés en revue, quatre demi-journées de travail avec Sonia Weber et Malik Ferhaoui.

**Le résultat global est meilleur qu'attendu** — le travail d'inventaire et de propriété des mois précédents couvre à lui seul une part importante des attentes. Trois écarts concentrent l'essentiel de l'effort restant.

**Écart n° 1 — la maîtrise de la sous-traitance.** HELIOMED ne dispose d'aucune donnée sur l'état de mise à jour des 620 postes gérés par son infogérant, ni d'aucune clause lui permettant de l'exiger. C'est le trou déclaré de la politique v1 (§7.7), et le référentiel le range parmi les attentes les plus structurantes. Effort estimé : un avenant contractuel, et une négociation.

**Écart n° 2 — la journalisation.** Les journaux de l'usine de Saint-Étienne ne sont pas centralisés et sont conservés sept jours. En cas de suspicion de compromission d'un poste de supervision, il serait impossible de conclure — ce qui renvoie très exactement à la règle du §21.3 : l'absence de preuve de compromission n'est pas la preuve de l'absence de compromission.

**Écart n° 3 — la qualification produit.** Personne chez HELIOMED n'a encore déterminé lesquels de ses produits relèvent du règlement européen sur la cyberrésilience. L'échéance de signalement du 11 septembre est dans dix semaines.

C'est l'écart le plus urgent des trois, et il est traité comme tel : Yann Prigent et Hélène Fabre conduisent une **qualification de première intention en six semaines**, suffisante pour identifier les produits concernés et mettre en service un dispositif de signalement minimal — point de contact publié, chaîne de décision pré-autorisée, modèles de notification. Ce dispositif est opérationnel le 1er septembre 2026.

Il est **volontairement incomplet** : la qualification retient l'hypothèse la plus contraignante partout où le doute existe, le PSIRT se réduit à deux personnes et une procédure d'astreinte, et l'inventaire des versions déployées chez les clients n'existe pas. C'est un dispositif de conformité minimale assumée, pas un dispositif abouti.

La revue de maturité complète — qualification argumentée produit par produit, exercice à blanc, inventaire des versions clients — est planifiée pour 2028. Elle fait l'objet du **chapitre 33**.

**La décision qui structure la suite.** Plutôt que de traiter les vingt objectifs en parallèle, Claire propose de séquencer sur douze mois en fonction de deux critères : effort d'une part, effet sur le risque réel d'autre part. Trois objectifs sont traités au trimestre suivant, sept sont planifiés, et **deux sont explicitement reportés à 2027 avec une justification écrite**. Ce dernier point est celui que Pierre Vasseur retient : il ne demande pas que tout soit fait, il demande à savoir ce qui ne le sera pas.

**Livrable de l'épisode.** Une analyse d'écart de six pages, une feuille de route à douze mois, et deux reports assumés et datés. Le tout constituera le socle du dossier de preuves de janvier 2027.

→ La suite en 🔴 §9.7, quand il faut désigner qui arbitrera ces priorités mois après mois.

→ **Chapitre 9 — Gouvernance, rôles et comitologie** : qui arbitre, à quel rythme, avec quel mandat.

#### Synthèse mentale du chapitre 8

Une directive européenne doit être transposée pour s'appliquer, et l'attente du texte national n'est jamais une stratégie : les clients exigent avant le régulateur, les délais de mise en conformité sont courts, et les mesures attendues sont utiles indépendamment du texte. Un référentiel d'application traduit les exigences en objectifs assortis de moyens acceptables de conformité et d'un principe de proportionnalité — ce qui vous laisse une liberté de calibrage, à condition de savoir la justifier par écrit. Le règlement sur la cyberrésilience déplace la réglementation de l'exploitant vers le fabricant, avec des délais de signalement qui sont d'abord une exigence de capacité organisationnelle, pas de formulaire, et des exclusions qui s'analysent produit par produit. Les normes et cadres sectoriels divergent sur la forme et convergent sur le fond : connaître, détecter, traiter dans des délais, tracer les exceptions, prouver. Une directive étrangère peut servir de modèle méthodologique sans jamais constituer une obligation. Enfin, la conformité est un plancher, et le temps consacré à produire de la preuve doit rester une fraction du temps consacré à corriger.

**Trois questions de vérification**

1. Votre direction demande s'il faut attendre la publication du texte national avant d'engager le programme. Donnez trois arguments qui ne reposent pas sur la crainte de la sanction.
2. Un client vous oppose une directive publiée par une autorité étrangère et exige que vous vous y conformiez. Comment répondez-vous sans être ni fermé ni juridiquement imprudent ?
3. Vous êtes certifié selon une norme de management de la sécurité et 40 % de votre parc est hors support. Est-ce compatible ? Qu'est-ce que cela vous apprend sur ce qu'une certification atteste ?

---

### Chapitre 9 — Gouvernance, rôles et comitologie

Le chapitre 7 a produit une doctrine, le chapitre 8 a identifié ce que l'extérieur attend. Reste la question qui décide de leur application réelle : **qui arbitre, à quel rythme, et avec quel mandat ?**

Un programme de MCS meurt rarement d'un défaut technique. Il meurt d'un arbitrage jamais rendu.

#### 9.1 Trois niveaux, trois horizons, trois types de décision

La gouvernance du MCS se structure sur trois étages. Les confondre est l'erreur la plus fréquente : on remonte des sujets techniques au niveau stratégique, qui ne sait pas les traiter, et on laisse des arbitrages métier au niveau opérationnel, qui n'a pas le mandat pour les rendre.

| Niveau | Qui | Rythme | Décisions typiques |
|---|---|---|---|
| **Stratégique** | Direction générale, direction des systèmes d'information, RSSI | Semestriel ou trimestriel | Budget pluriannuel, acceptation des risques majeurs, sortie d'obsolescence, arbitrage entre projets et maintien |
| **Tactique** | Comité MCS : RSSI, exploitation, représentants métier, prestataires | Mensuel | Priorisation des campagnes, validation des dérogations, revue des indicateurs, escalades |
| **Opérationnel** | Exploitation, propriétaires techniques | Hebdomadaire ou quotidien | Exécution, qualification des constats, planification des fenêtres, traitement des échecs |

**La règle de circulation** qui rend le dispositif fluide : chaque niveau ne traite que ce que le niveau inférieur ne peut pas trancher **avec son mandat**. Un correctif refusé par un métier n'est pas un problème technique : il remonte. Un correctif qui échoue sur douze machines n'est pas un sujet de comité : il reste au niveau opérationnel.

#### 9.2 Le RACI de référence

Un RACI attribue quatre rôles à chaque activité : **R**éalise, **A**pprouve (le décideur, unique), **C**onsulté, **I**nformé. Voici la matrice de base du MCS, à adapter mais dont la logique est stable.

| Activité | RSSI | Exploitation | Propriétaire métier | Direction SI | Prestataire |
|---|---|---|---|---|---|
| Définir la politique et les classes de service | R | C | C | **A** | I |
| Tenir l'inventaire et le périmètre de référence | C | **R/A** | C | I | R |
| Veille et qualification des vulnérabilités | **R/A** | C | I | I | C |
| Priorisation et délais | **R** | C | C | **A** | I |
| Planifier et exécuter la correction | I | **R/A** | C | I | R |
| Décider d'une interruption de service | C | C | **A** | I | I |
| Accorder une dérogation | R | C | **A** | C | I |
| Produire la preuve | C | **R** | I | I | R |
| Escalader une impossibilité | C | **R** | C | **A** | R |
| Contrôler l'application | **R/A** | C | I | I | I |

**Trois points structurants dans ce tableau, souvent inversés dans la réalité.**

**Le RSSI n'approuve pas la correction.** Il qualifie, priorise et contrôle. La décision d'arrêter un service appartient à celui qui en porte la valeur métier — sinon, la sécurité devient responsable de l'indisponibilité qu'elle provoque, ce qui la rend structurellement timide.

**Le propriétaire métier approuve la dérogation.** Pas la sécurité. Celui qui accepte le risque le signe. Faire signer la sécurité revient à lui transférer un risque qu'elle n'a pas les moyens de porter, et cela déresponsabilise le métier.

**L'escalade est une obligation de l'exploitation, pas une faveur.** Elle doit être explicitement inscrite comme un livrable attendu, avec un délai. Une impossibilité non escaladée est un écart invisible, et c'est ce que le contrat interne du §7.3 vise à empêcher.

#### 9.3 Le comité MCS : format, ordre du jour, décisions

C'est l'instance centrale. Sa qualité détermine celle du programme.

**Format.** Une heure, mensuel, même date chaque mois. Participants : RSSI (animation), responsable exploitation, un représentant par grand domaine métier concerné, représentant du prestataire d'infogérance si le périmètre le justifie, et un invité tournant selon les sujets.

**Ordre du jour type, en cinq points et dans cet ordre :**

| Point | Durée | Contenu | Sortie attendue |
|---|---|---|---|
| 1. Indicateurs | 10 min | Trois à cinq indicateurs de résultat, avec leur dénominateur | Constat partagé, aucune discussion technique |
| 2. Escalades | 15 min | Impossibilités remontées depuis le dernier comité | **Décision** : correction forcée, dérogation, ou report daté |
| 3. Dérogations | 10 min | Nouvelles demandes, et surtout celles arrivant à échéance | **Décision** : clôture, renouvellement au niveau supérieur, ou correction |
| 4. Campagne à venir | 15 min | Périmètre, fenêtres, risques identifiés | Validation ou ajustement |
| 5. Sujets de fond | 10 min | Un seul sujet par comité : obsolescence, outillage, contrat | Orientation, à instruire |

⚠️ **PIÈGE — le comité qui devient une revue technique**
Symptôme : on passe quarante minutes sur le cas particulier d'un serveur. Cause : les décisions attendues ne sont pas préparées, donc on remplit avec du détail. Remède : chaque point d'escalade et de dérogation arrive au comité avec **une décision proposée** et ses conséquences, pas avec une question ouverte. Le comité valide, amende ou refuse — il n'instruit pas.

✅ **BONNE PRATIQUE (P0) — le relevé de décisions**
Le compte rendu ne relate pas les discussions : il liste les décisions, avec pour chacune l'objet, la décision, le décideur nommé, la date et l'échéance de revue. Une page. C'est ce document qui aura valeur de preuve (§5.6 et chapitre 39), et c'est aussi ce qui protège l'équipe le jour où une décision de report est contestée après incident.

**Ce qui remonte au niveau stratégique.** Quatre choses seulement, et il faut résister à la tentation d'en remonter davantage :

1. les risques dont l'acceptation dépasse le mandat du comité — typiquement une exposition majeure non corrigeable ;
2. les besoins budgétaires, notamment de sortie d'obsolescence ;
3. les arbitrages entre projets et maintien, quand les mêmes équipes sont mobilisées ;
4. la tendance des indicateurs de risque, sur plusieurs trimestres — pas le détail du mois.

#### 9.4 Articuler sécurité, exploitation et métiers sans arbitrage permanent

Le conflit d'objectifs du §1.2 est structurel. Une bonne gouvernance ne le supprime pas : elle en **réduit la fréquence**, en pré-arbitrant à froid ce qui sinon devrait être tranché à chaud, à chaque fois.

**Les quatre pré-arbitrages qui suppriment l'essentiel des conflits :**

| Pré-arbitrage | Formulation type | Ce qu'il évite |
|---|---|---|
| Fenêtres récurrentes acquises | « Deuxième jeudi, 22 h - 2 h, sans redemander » | Douze négociations par an |
| Seuil d'urgence pré-autorisé | « Vulnérabilité exploitée sur actif exposé : interruption autorisée sous 72 h, décision du propriétaire technique » | Une négociation en pleine crise |
| Plafond de charge mensuel | « Au plus N heures d'intervention MCS par mois ; au-delà, arbitrage en comité » | Le conflit permanent sur la charge |
| Règle de levée de gel | « Les gels de production comportent une clause de levée pour vulnérabilité exploitée, décidée par X » | Le blocage total pendant six semaines |

**Le principe général**, valable bien au-delà du MCS : *tout arbitrage récurrent doit être transformé en règle une fois pour toutes*. Si vous tranchez trois fois la même question, c'est qu'elle appelle une règle, pas un quatrième arbitrage.

#### 9.5 Organisations décentralisées, filiales et entités acquises

Le modèle ci-dessus suppose une organisation unifiée. Beaucoup ne le sont pas.

**Le principe applicable** : la gouvernance du MCS suit la gouvernance générale de l'organisation. Tenter d'imposer un modèle centralisé à un groupe décentralisé produit un dispositif de façade — des règles écrites au siège que personne n'applique en local.

**Le modèle qui fonctionne le plus souvent** est mixte, avec une répartition explicite :

| Défini centralement | Décidé localement |
|---|---|
| Les classes de service et les délais associés | Les fenêtres et les modalités d'exécution |
| Le format de la preuve et des indicateurs | L'outillage, quand une raison locale le justifie |
| La procédure de dérogation et les niveaux de signature | Les dérogations elles-mêmes, dans le cadre défini |
| Le périmètre minimal à inventorier | La conduite de l'inventaire |

⚠️ **PIÈGE — l'entité acquise**
Une société rachetée arrive avec son propre parc, ses propres pratiques, souvent son propre annuaire, et une interconnexion réalisée en urgence pour les besoins de l'intégration. C'est statistiquement l'un des chemins d'entrée les plus fréquents dans les groupes. Deux règles : **l'inventaire de l'entité acquise fait partie de la diligence d'acquisition**, pas de l'intégration à venir ; et **l'interconnexion est traitée comme une exposition** (chapitre 11) tant que le niveau de maintien n'est pas connu et mesuré.

#### 9.6 ⚠️ Le RSSI propriétaire du MCS : pourquoi c'est un anti-pattern

C'est une configuration extrêmement répandue, et elle échoue de manière prévisible.

**La configuration.** Le RSSI détecte les vulnérabilités, décide des priorités, demande les corrections, relance, et se voit reprocher les retards. Il est de fait responsable d'un résultat dont il ne contrôle aucun des moyens.

**Pourquoi cela ne peut pas fonctionner.**

- Le RSSI ne dispose ni des accès, ni des compétences d'exploitation, ni des fenêtres, ni du budget d'infrastructure.
- Sa position devient adversariale : il demande, l'exploitation subit. L'information circule mal, les impossibilités sont dissimulées.
- La responsabilité et l'autorité sont dissociées, ce qui est la définition même d'une position intenable.
- Effet secondaire fréquent : le RSSI, faute de pouvoir corriger, finit par mesurer moins — parce que chaque constat supplémentaire aggrave un retard dont on le tient pour responsable.

**La configuration qui fonctionne** est celle du RACI du §9.2 : le MCS est une **activité d'exploitation**, dont la sécurité définit les exigences, qualifie les priorités et contrôle l'application. Autrement dit, la sécurité est **prescriptrice et contrôleuse**, l'exploitation est **réalisatrice**, le métier est **décideur** sur l'interruption et le risque.

📌 **LIMITES — le cas des petites organisations**
Dans une structure de trente personnes, les trois rôles sont parfois tenus par la même personne. La séparation reste utile, mais elle devient une discipline mentale : *quand j'écris cette dérogation, j'agis comme propriétaire métier, et je la signe en tant que tel.* Le formalisme allégé ne dispense pas de la traçabilité, il en réduit seulement le volume — une ligne dans un tableau tenu à jour suffit à la place d'un formulaire.

#### 9.7 🔴 FIL ROUGE — juillet 2026 : le premier comité MCS et le désaccord Berger / Ferhaoui

Le comité MCS d'HELIOMED se réunit pour la première fois le premier mardi de juillet. Présents : Claire Nadeau, Sonia Weber, Malik Ferhaoui, Thomas Berger, un représentant du service commercial, et un chargé de compte de l'infogérant Numeria.

**Les indicateurs, en dix minutes.** Le taux de conformité global sur le périmètre de référence est passé de 72 % en décembre à 84 %. Personne ne conteste le chiffre, parce que son dénominateur est affiché — c'est le bénéfice direct de la décision de §2.9.

**L'escalade qui occupe le comité.** Malik demande l'autorisation de mettre à jour le micrologiciel de deux commutateurs cœur de réseau de l'usine, sur lesquels une vulnérabilité exploitée a été identifiée. L'opération suppose une coupure réseau de quinze minutes. Thomas Berger refuse : une coupure réseau non planifiée pendant un cycle de production peut mettre une ligne à l'arrêt pour trois heures, avec des lots à rebuter.

Le désaccord n'est pas un conflit de personnes : chacun défend correctement son mandat. Les deux ont raison, et c'est exactement la situation que le comité existe pour trancher.

**Le déroulement de l'arbitrage.**

1. Claire qualifie : vulnérabilité au catalogue d'exploitation avérée, mais équipements **non joignables depuis Internet**. L'exploitation supposerait un accès préalable au réseau interne. Le risque est réel mais pas immédiat.
2. Malik propose une alternative : réaliser l'opération pendant la relève d'équipe du samedi matin, créneau de quarante minutes sans production, avec Thomas présent.
3. Thomas accepte, sous deux conditions écrites : validation préalable du constructeur sur la version cible, et retour arrière préparé et testé sur un commutateur de rechange avant l'intervention.
4. Sonia Weber valide la mobilisation des deux personnes le samedi.

**Ce que le comité produit vraiment**, au-delà de la décision du jour : deux règles générales, qui n'existaient pas avant.

- *Toute intervention sur le réseau industriel se réalise pendant une relève d'équipe, créneau désormais identifié comme fenêtre récurrente de classe C4.* Le pré-arbitrage du §9.4 est né d'un cas concret.
- *Un correctif de micrologiciel sur équipement industriel exige une validation constructeur écrite et un matériel de secours préparé.* La condition devient une règle, applicable sans repasser en comité.

**Le point de friction non résolu.** Le représentant de Numeria ne peut fournir aucune donnée sur l'état des 620 postes. Il indique que le contrat ne prévoit pas cette restitution. Claire inscrit le point à l'ordre du jour du comité stratégique : ce n'est pas un sujet technique, c'est un sujet contractuel — traité au chapitre 13.

**Livrable de l'épisode.** Un relevé de décisions d'une page : quatre décisions, deux règles générales créées, un point escaladé au niveau stratégique, chacun avec un nom et une date.

→ La suite en 🔴 §10.11, quand le comité demande sur quoi, exactement, portent les 84 % annoncés.

→ **Chapitre 10 — Inventaire et cartographie** : le socle non négociable : savoir ce qu'on doit maintenir.

#### Synthèse mentale du chapitre 9

Un programme de MCS meurt d'un arbitrage jamais rendu, pas d'un défaut technique. La gouvernance se structure sur trois niveaux dont chacun ne traite que ce que le niveau inférieur ne peut trancher avec son mandat. Trois attributions de rôles sont contre-intuitives et décisives : la sécurité n'approuve pas la correction, le propriétaire métier signe la dérogation parce qu'il porte le risque, et l'escalade d'une impossibilité est une obligation de l'exploitation, pas une faveur. Le comité mensuel produit des décisions, pas des discussions : chaque point y arrive avec une décision proposée, et le relevé d'une page vaut preuve. Les conflits récurrents se suppriment par pré-arbitrage à froid — fenêtres acquises, seuil d'urgence pré-autorisé, plafond de charge, clause de levée de gel — selon le principe que tout arbitrage rendu trois fois appelle une règle. Enfin, faire du RSSI le propriétaire du MCS dissocie la responsabilité de l'autorité : c'est une position intenable, dont l'effet secondaire le plus pervers est qu'elle pousse à mesurer moins.

**Trois questions de vérification**

1. Votre comité MCS passe quarante minutes sur le cas d'un serveur particulier. Quel est le symptôme, quelle est la cause réelle, et quelle règle de préparation le corrige ?
2. Pourquoi faire signer les dérogations par la sécurité plutôt que par le métier affaiblit-il l'ensemble du dispositif, y compris du point de vue de la sécurité elle-même ?
3. Votre groupe rachète une société de 80 personnes et l'interconnecte au réseau en six semaines. Citez les deux règles à appliquer avant l'interconnexion, et à quel moment du processus d'acquisition elles auraient dû intervenir.

---

### Chapitre 10 — Inventaire et cartographie

#### 10.1 Pourquoi tout programme de MCS échoue d'abord ici

C'est la cause d'échec n° 1 du §1.4, et elle mérite d'être formulée sans détour : **tant que le dénominateur est inconnu, aucun indicateur de MCS n'a de sens.**

Reprenons le raisonnement de bout en bout, parce qu'il est souvent accepté du bout des lèvres puis oublié dès la première présentation :

- vous ne corrigez que ce que vous connaissez ;
- vous ne mesurez que ce que votre outil atteint ;
- vous ne présentez donc, dans le meilleur des cas, qu'un pourcentage calculé sur les actifs connus **et** atteints ;
- or les actifs inconnus ne sont pas répartis au hasard : ce sont statistiquement les plus anciens, les moins gérés, les moins documentés — donc les plus vulnérables.

Autrement dit, votre indicateur est non seulement incomplet, il est **biaisé dans le sens favorable**. Les machines qui manquent sont précisément celles qui feraient chuter le chiffre.

⚠️ **PIÈGE — l'inventaire parfait comme préalable**
La conclusion inverse est tout aussi fausse : attendre un inventaire exhaustif avant de commencer à corriger. L'exhaustivité n'existe pas, elle est asymptotique. Ce qu'il faut atteindre rapidement, c'est un inventaire **suffisant, mesuré et honnête** : un périmètre de référence dont vous connaissez le taux de complétude estimé et les zones d'ombre déclarées. Le §10.9 fournit le chemin en trente jours.

#### 10.2 Les sources de découverte et leur complémentarité

Aucune source ne voit tout. Chacune a un angle mort structurel, et c'est leur **croisement** qui produit l'information — pas leur addition.

| Source | Ce qu'elle voit bien | Son angle mort structurel |
|---|---|---|
| Base de gestion de configuration | Ce que l'organisation a déclaré | Tout ce qui a été créé sans déclaration ; les machines éteintes y restent |
| Annuaire d'entreprise | Machines jointes au domaine | Serveurs hors domaine, équipements réseau, systèmes industriels, machines de développement |
| Découverte réseau active | Ce qui répond, sur les plages scannées | Machines éteintes au moment du passage, réseaux non scannés, équipements qui ne répondent pas |
| Inventaire d'hyperviseur | Toutes les machines virtuelles, allumées ou non | Le physique, le cloud, les conteneurs |
| Interfaces des fournisseurs cloud | Les ressources cloud, exhaustivement | Tout ce qui est sur site |
| Agents installés | État détaillé de la machine | Les machines sans agent — c'est-à-dire celles qui posent problème |
| Gestion de flotte mobile | Postes et mobiles enrôlés | Les appareils non enrôlés |
| Résolution de noms et baux d'adresses | Ce qui s'est connecté récemment | Peu structuré, beaucoup de bruit |
| **Comptabilité fournisseurs** | **Les abonnements payés** | Ne dit rien du technique — mais révèle le shadow IT |
| Découverte externe | Ce qui est publié sur Internet à votre nom | Rien de ce qui est interne |

**Le point qui surprend toujours** : la comptabilité fournisseurs est l'une des sources les plus rentables d'un premier inventaire. Une facture correspond à un service réel, utilisé par quelqu'un, contenant probablement des données — et souvent inconnu de la direction des systèmes d'information. Le rapport effort/découverte y est excellent.

✅ **BONNE PRATIQUE (P0)** — Utilisez au minimum **quatre sources de nature différente**, dont une non technique. Trois sources techniques partagent souvent le même angle mort ; une source non technique ne le partage jamais.

#### 10.3 La réconciliation : lire les écarts plutôt que les chiffres

C'est la compétence centrale de ce chapitre. Face à plusieurs sources donnant des chiffres différents, la mauvaise question est « lequel est le bon ? ». La bonne question est : **que signifie chaque écart ?**

**La méthode, en quatre étapes.**

**1. Choisir un identifiant pivot.** Le nom d'hôte est instable, l'adresse IP est mouvante, l'adresse matérielle change avec le matériel. En pratique, on utilise une combinaison : nom d'hôte normalisé + identifiant unique de machine + adresse matérielle, avec des règles de rapprochement documentées. L'identifiant pivot doit être **choisi et écrit**, pas improvisé à chaque extraction.

**2. Construire les ensembles.** Pour chaque paire de sources : présent dans les deux, présent seulement dans A, présent seulement dans B.

**3. Interpréter chaque écart.** C'est ici que se trouve toute la valeur, et chaque catégorie appelle une action différente :

| Type d'écart | Signification probable | Action |
|---|---|---|
| Déclaré mais ne répond pas | Machine éteinte, décommissionnée à moitié, ou nom obsolète | Vérifier, puis décommissionner en règle (ch. 35) |
| Répond mais non déclaré | Création hors processus, appliance livrée, entité rattachée | Trouver un propriétaire ou éteindre (§5.5) |
| Déclaré, actif, mais hors outil de gestion | **N'a jamais reçu de correctif** | Priorité maximale : c'est le plus dangereux des trois |
| Présent dans deux sources avec des attributs contradictoires | Données obsolètes dans l'une | Définir laquelle fait foi, par attribut |

**4. Publier le résultat avec ses trous.** Le livrable n'est pas un nombre, c'est un tableau d'ensembles avec les causes identifiées. C'est cela qui donne de la crédibilité au chiffre annoncé ensuite.

⚠️ **PIÈGE — le troisième type d'écart**
La ligne « déclaré, actif, mais absent de l'outil de gestion » est la plus grave et la moins visible. Ces machines apparaissent dans tous les documents officiels, sont considérées comme gérées par tout le monde, et n'ont jamais reçu un seul correctif par le canal prévu. Elles sont invisibles à la fois pour l'inventaire *et* pour les indicateurs de conformité, puisqu'elles ne figurent pas dans le dénominateur de l'outil.

#### 10.4 Les attributs minimaux d'un actif maintenable

Un inventaire qui ne contient que des noms de machines ne sert à rien pour le MCS. Voici le jeu minimal — le modèle complet figure en **Annexe I**.

| Attribut | Pourquoi il est indispensable au MCS |
|---|---|
| Identifiant unique et stable | Sans lui, aucune réconciliation ni aucun historique |
| Type et rôle | Détermine la méthode de correction |
| **Propriétaire métier** | Qui décide de l'interruption (§5.5) |
| **Propriétaire technique** | Qui exécute et produit la preuve |
| **Criticité** | Détermine la classe de service (§7.2) |
| **Exposition** | Internet, réseau interne, isolé — détermine la priorité réelle (ch. 11) |
| Environnement | Production, recette, développement, laboratoire (ch. 28) |
| Système et version | Base de la corrélation avec les vulnérabilités |
| **Statut et date de fin de support** | Base du plan d'obsolescence (ch. 12) |
| Fournisseur et contrat | Qui doit corriger, et sous quel délai contractuel (ch. 13) |
| Fenêtre de maintenance | Quand on peut intervenir |
| Outils de gestion et de scan | Permet de calculer la couverture réelle |
| Dépendances | Qui casse si on l'arrête |
| Dérogations en cours | Dette formalisée attachée à l'actif |
| Dernière preuve de conformité | Date et nature |

**Le test de qualité de votre inventaire** tient en une question : pouvez-vous produire, en moins de dix minutes, la liste des actifs **exposés à Internet, hors support, sans propriétaire nommé** ? Si oui, votre inventaire est exploitable. Sinon, il est documentaire.

#### 10.5 Dépendances applicatives et effets de bord

Connaître les actifs ne suffit pas : il faut savoir **ce qui casse quand on en arrête un**. C'est ce qui transforme une intervention planifiée en incident.

**Trois niveaux de cartographie, par effort croissant.**

| Niveau | Méthode | Effort | Ce que ça donne |
|---|---|---|---|
| Déclaratif | Demander aux propriétaires | Faible | Incomplet mais immédiat ; révèle surtout ce que les gens croient |
| Observé | Analyse des flux réseau réels sur une période représentative | Moyen | Fiable sur ce qui a effectivement communiqué |
| Modélisé | Cartographie applicative maintenue | Élevé | Complet, mais se dégrade vite sans propriétaire |

✅ **BONNE PRATIQUE (P1)** — Ne visez pas la cartographie complète. Cartographiez d'abord les **dépendances des actifs de niveau 0** (annuaire, résolution de noms, hyperviseur, sauvegarde, authentification, temps) : ce sont eux dont l'arrêt produit des effets en cascade imprévus, et ils représentent moins de 5 % du parc.

⚠️ **PIÈGE — la dépendance temporelle**
Certaines dépendances ne se manifestent qu'à des moments précis : traitement de nuit, clôture mensuelle, sauvegarde hebdomadaire, échange avec un partenaire. Une analyse de flux menée sur trois jours ouvrés les manquera. Observez sur au moins un cycle métier complet — un mois, si votre activité a une clôture mensuelle.

#### 10.6 Shadow IT et services en ligne non déclarés

Les services souscrits hors du circuit de la direction des systèmes d'information sont une part significative du périmètre réel, et ils sont particulièrement pertinents pour le MCS : ils contiennent des données, ils disposent souvent d'accès à d'autres systèmes via des connecteurs, et personne ne suit leur configuration.

**Les quatre méthodes de détection, par rentabilité décroissante :**

1. **La comptabilité.** Extraire les lignes de dépense correspondant à des abonnements logiciels. Simple, non technique, extrêmement productif.
2. **Le fournisseur d'identité.** Lister les applications ayant reçu une autorisation de connexion via l'authentification unique, et les autorisations déléguées accordées à des applications tierces. C'est aussi ce qui révèle les connecteurs disposant d'accès à la messagerie ou aux fichiers (chapitre 31).
3. **Les journaux de navigation ou de proxy.** Détectent l'usage, pas le contrat.
4. **L'enquête directe.** Demander aux équipes ce qu'elles utilisent, sans posture punitive. Le rendement dépend entièrement du climat : une organisation qui sanctionne le shadow IT ne le découvre jamais.

📌 **LIMITES** — Aucune de ces méthodes ne détecte un service gratuit, souscrit avec une adresse personnelle, utilisé par une seule personne. Ce cas relève de la sensibilisation et de la politique d'usage, pas de l'inventaire technique.

#### 10.7 Maintenir l'inventaire vivant

Un inventaire est un actif périssable : il se dégrade dès le jour de sa constitution. Quatre mécanismes le maintiennent.

| Mécanisme | Principe | Effet |
|---|---|---|
| **Intégration au cycle de vie** | Aucune mise en production sans déclaration ; aucun décommissionnement sans retrait | Empêche la dégradation à la source |
| **Réconciliation périodique automatisée** | Rejouer le croisement de sources chaque mois | Détecte les écarts qui réapparaissent |
| **Contrôles de complétude** | Règles de qualité : actif sans propriétaire, sans criticité, sans date de fin de support | Mesure la qualité de la donnée, pas seulement sa quantité |
| **Indicateur de dérive** | Nombre de nouveaux écarts par mois | Mesure si le processus tient ou se dégrade |

✅ **BONNE PRATIQUE (P0)** — L'intégration au cycle de vie est la seule mesure structurelle ; les trois autres sont des rattrapages. Concrètement : la déclaration d'un actif, avec ses deux propriétaires, devient une **condition de mise en production**, au même titre que la sauvegarde. C'est une décision de gouvernance, pas un projet d'outillage.

#### 10.8 📌 Ce qu'aucun outil de découverte ne verra

Soyons explicites sur les limites, parce que les ignorer produit une fausse assurance.

- **Les systèmes industriels muets**, qui ne répondent pas à une sollicitation réseau, et qu'il ne faut de toute façon pas interroger activement (§3.7).
- **Les environnements séparés physiquement**, par construction.
- **Les composants embarqués** dans les applications, qui n'ont pas d'existence réseau propre (chapitre 26).
- **Les actifs éphémères** — conteneurs, agents de construction, instances à mise à l'échelle automatique — qui n'existent pas au moment où l'inventaire passe. Pour eux, l'inventaire doit interroger l'orchestrateur, pas le réseau.
- **Les actifs détenus par un prestataire** pour votre compte, qui ne sont pas sur vos réseaux (chapitre 13).
- **Les micrologiciels**, qui ne sont presque jamais remontés par les outils d'inventaire standard (§3.8).

Pour chacune de ces catégories, la seule réponse honnête est de la **déclarer non couverte**, avec un propriétaire et une échéance de première mesure — exactement comme dans la politique du §7.7.

#### 10.9 ✅ Inventaire minimal viable en trente jours

| Prio | Action | Résultat attendu |
|---|---|---|
| **P0** | Croiser quatre sources dont une non technique | Périmètre de référence, avec ses écarts identifiés |
| **P0** | Attribuer criticité et exposition à chaque actif, même grossièrement | Base du classement en classes de service |
| **P0** | Lancer la campagne de désignation des propriétaires (§5.5) | Actifs orphelins identifiés |
| **P0** | Publier le périmètre **avec ses zones non couvertes déclarées** | Crédibilité de tous les indicateurs ultérieurs |
| P1 | Calculer et publier la couverture de chaque outil sur ce périmètre | Vision honnête de ce qui est réellement géré |
| P1 | Cartographier les dépendances des actifs de niveau 0 | Prévention des effets en cascade |
| P1 | Extraire les abonnements en ligne depuis la comptabilité | Détection du shadow IT |
| P2 | Automatiser la réconciliation mensuelle | Maintien dans la durée |
| P2 | Intégrer la déclaration au processus de mise en production | Arrêt de la dégradation à la source |

#### 10.10 🔬 Mini-lab 2 — Réconciliation d'inventaire

**Objectif** — Construire un périmètre de référence à partir de sources contradictoires, en déduire les indicateurs corrects, et repérer le piège de vocabulaire.
**Durée** 45 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §10.3, §10.4, annexe I.4 · **Livrable** table de réconciliation + quatre indicateurs.
**Compétences validées** — ✔ construire un périmètre maître à partir de sources divergentes ✔ interpréter un écart selon son type ✔ choisir le bon dénominateur par indicateur ✔ distinguer couverture, conformité et ratio conservateur

**Données fournies.** Une filiale de 3 sites. Quatre sources ont été extraites le même jour.

| Source | Effectif |
|---|---|
| **C** — Base de gestion de configuration | 96 |
| **K** — Console de déploiement des correctifs | 71 |
| **D** — Découverte (réseau + hyperviseur + interface cloud) | 118 |
| **F** — Extraction comptable des abonnements en ligne | 14 abonnements |

Éléments de recoupement communiqués par l'équipe :

- toutes les machines de la console figurent dans la base de gestion ;
- 9 machines de la base de gestion ne répondent plus depuis plus de 60 jours ;
- 31 machines découvertes ne figurent pas dans la base de gestion ;
- la console rapporte 68 machines conformes sur les 71 qu'elle gère ;
- parmi les 14 abonnements en ligne, 5 ne sont connus d'aucune équipe technique.

**Questions.**

1. Construisez la table de réconciliation complète des ensembles.
2. Quel est le périmètre de référence ?
3. Calculez : conformité interne à la console · couverture de la console · conformité globale sur les actifs en service · conformité globale sur le périmètre de référence.
4. Quel sous-ensemble représente le risque le plus élevé, et pourquoi ?
5. Le responsable d'exploitation propose d'annoncer « 96 % de conformité » au comité. Que lui répondez-vous ?
6. Comment traitez-vous les 5 abonnements inconnus ?

**Corrigé commenté**

**1 et 2 — Table de réconciliation**

| Ensemble | Calcul | Effectif |
|---|---|---|
| Gérées par la console (K ⊆ C) | donné | 71 |
| Déclarées, actives, hors console (C ∩ D, hors K) | 96 − 71 − 9 | 16 |
| Déclarées mais ne répondant plus (C \ D) | donné | 9 |
| **Total base de gestion (C)** | 71 + 16 + 9 | **96** |
| Déclarées et actives (C ∩ D) | 71 + 16 | 87 |
| Actives non déclarées (D \ C) | donné | 31 |
| **Total découvert actif (D)** | 87 + 31 | **118** |
| **Périmètre de référence (C ∪ D)** | 87 + 9 + 31 | **127** |

Les 14 abonnements en ligne s'ajoutent au périmètre en tant qu'actifs de service — ils ne se comptent pas avec les machines, mais ils ne s'en excluent pas non plus. Le périmètre complet comporte donc **127 actifs techniques et 14 actifs de service**.

**3 — Indicateurs**

| Indicateur | Calcul | Valeur |
|---|---|---|
| Conformité interne à la console | 68 / 71 | **96 %** |
| Couverture de la console | 71 / 118 | **60 %** |
| **Ratio confirmé conforme**, actifs en service | 68 / 118 | **58 %** |
| **Ratio confirmé conforme**, périmètre maître | 68 / 127 | **54 %** |
| **Non mesuré** | 47 actifs en service | **40 %** |

**4 — Le sous-ensemble le plus risqué.** Les **16 machines déclarées, actives, mais hors console**. Ce ne sont pas les 31 non déclarées — celles-là, tout le monde sait qu'on ne les connaît pas. Les 16 sont pires : elles figurent dans tous les documents officiels, chacun les croit gérées, et elles n'ont **jamais** reçu de correctif par le canal prévu. C'est l'écart de type 3 du §10.3.

**5 — La réponse à faire.** Le chiffre de 96 % est exact et il décrit **la conformité interne d'un outil qui couvre 60 % du parc actif**. L'annoncer sans son dénominateur n'est pas une erreur de calcul, c'est une erreur de vocabulaire aux conséquences durables : le comité prendra ses décisions sur une base fausse, et le jour où le chiffre réel apparaîtra — audit, incident, changement d'équipe — la crédibilité de toute la fonction sera atteinte. La formulation correcte tient en une phrase : *« 96 % de conformité sur 60 % de couverture, soit 58 % de conformité réelle sur les actifs en service »*.

**6 — Les cinq abonnements inconnus.** Ils ne relèvent pas d'un traitement technique en première intention. La séquence est : identifier le payeur via la comptabilité → identifier l'utilisateur → déterminer les données traitées → déterminer les connecteurs et autorisations accordés (chapitre 31) → décider de régulariser ou de résilier. Aucune de ces étapes n'est technique, et c'est le point du chapitre.

**Les trois erreurs attendues.** Additionner les sources (96 + 118 = 214), ce qui compte deux fois les machines communes. Exclure les 9 machines éteintes du périmètre, alors qu'elles portent des comptes de service et des enregistrements réseau actifs et relèvent d'un décommissionnement en règle. Et écarter les abonnements en ligne au motif qu'il ne s'agit pas de machines.

#### 10.11 🔴 FIL ROUGE — août 2026 : sur quoi portent les 84 % ?

Au comité de juillet (§9.7), Claire Nadeau a annoncé 84 % de conformité. Le représentant commercial pose au comité suivant une question simple : *84 % de quoi ?*

Claire l'attendait. La réponse tient en un tableau de quatre lignes, projeté en séance.

| Population | Effectif | Conformes | Taux |
|---|---|---|---|
| Serveurs et postes gérés par la console interne | 176 | 158 | 90 % |
| Actifs de classe C4 — usine, régime de compensation | 14 | *sans objet* | *compensation vérifiée : 12/14* |
| Postes gérés par l'infogérant | 620 | **non mesuré** | **—** |
| Actifs orphelins en cours d'extinction | 10 | 0 | 0 % |

Les 84 % portaient sur la première ligne uniquement. Rapportés à l'ensemble du périmètre connu, postes infogérés compris, ils tomberaient sous 25 % — non parce que ces postes seraient mal maintenus, mais parce que **personne n'en sait rien**.

**La réaction du comité est celle qu'espérait Claire.** Personne ne conteste le travail réalisé. La discussion se déplace immédiatement là où elle est utile : *comment obtient-on la mesure des 620 postes ?* Le sujet devient contractuel, il est porté au comité stratégique, et il obtient un mandat de négociation — ce que six mois de relances n'avaient pas produit.

**Décision prise.** Tous les indicateurs d'HELIOMED seront désormais publiés en quatre populations distinctes, avec la mention **« non mesuré »** partout où c'est le cas. La règle est explicite : *un périmètre non mesuré s'affiche comme non mesuré, jamais comme conforme, et jamais comme absent du tableau.*

**Livrable de l'épisode.** Le tableau de bord en quatre populations, qui deviendra le format de référence du chapitre 38 — et la fiche de réconciliation d'inventaire figurant en Annexe I.

→ La suite en 🔴 §11.12, quand l'inventaire ne suffira plus et qu'il faudra savoir ce qui est réellement atteignable.

→ **Chapitre 11 — Exposition et chemins d'attaque** : la différence entre ce qui existe et ce qui peut être atteint.

#### Synthèse mentale du chapitre 10

Tant que le dénominateur est inconnu, aucun indicateur n'a de sens — et le biais joue toujours dans le sens favorable, puisque les actifs manquants sont statistiquement les moins maintenus. Aucune source de découverte ne voit tout : c'est leur croisement qui produit l'information, et une source non technique comme la comptabilité fournisseurs a le meilleur rapport effort/découverte. La compétence centrale n'est pas de choisir le bon chiffre mais de lire les écarts, dont le plus dangereux est celui des machines déclarées, actives et absentes de l'outil de gestion : tout le monde les croit gérées et elles n'ont jamais reçu de correctif. Un inventaire exploitable se teste en une question — peut-on sortir en dix minutes la liste des actifs exposés, hors support et sans propriétaire ? Il se maintient par intégration au cycle de vie, la seule mesure structurelle ; le reste est du rattrapage. Enfin, tout ce qui n'est pas couvert doit être déclaré non couvert, avec un propriétaire et une échéance.

**Trois questions de vérification**

1. Trois de vos sources d'inventaire donnent trois chiffres différents. Quelle est la mauvaise question, quelle est la bonne, et quel type d'écart traitez-vous en premier ?
2. Pourquoi un taux de conformité calculé sur les seuls actifs connus est-il biaisé dans le sens favorable, et pas simplement incomplet ?
3. Votre inventaire est complet mais ne comporte ni criticité, ni exposition, ni propriétaire. Que pouvez-vous en faire concrètement pour piloter le MCS ?

---

### Chapitre 11 — Exposition et chemins d'attaque

#### 11.1 L'inventaire dit ce qui existe, l'exposition dit ce qui peut être atteint

Le chapitre 10 a produit une liste. Cette liste ne suffit pas, parce qu'elle traite comme équivalents deux actifs qui ne le sont pas du tout : un serveur portant une vulnérabilité critique mais joignable uniquement depuis un réseau d'administration restreint, et le même serveur publié sur Internet.

**La différence est d'un facteur considérable sur le risque réel, et elle n'apparaît dans aucun score de gravité** (§4.10). C'est vous, et personne d'autre, qui apportez cette information.

**Le modèle mental.** Une vulnérabilité est une porte fermée à clé. L'exposition détermine s'il y a un couloir qui mène jusqu'à cette porte, et qui peut l'emprunter. Une porte fragile au fond d'une pièce fermée n'est pas le même problème qu'une porte fragile sur la rue.

**Trois questions définissent l'exposition d'un actif :**

1. **Depuis où est-il joignable ?** Internet, réseau bureautique, réseau d'administration, réseau industriel, nulle part.
2. **Par qui ?** Anonyme, utilisateur authentifié quelconque, utilisateur privilégié, prestataire.
3. **Vers quoi mène-t-il ?** Un actif compromis donne accès à quoi d'autre — c'est la question des chemins d'attaque (§11.4).

Les deux premières questions relèvent de la surface d'exposition. La troisième change la nature de l'exercice : elle transforme une liste d'actifs en **graphe**.

#### 11.2 Les familles d'approche, et ce qu'elles apportent réellement

| Approche | Point de vue | Ce qu'elle apporte | Ce qu'elle ne voit pas |
|---|---|---|---|
| **Découverte externe** | Depuis Internet, sans rien savoir de vous | Ce qui est réellement publié à votre nom, y compris ce que vous ignorez | Tout l'interne |
| **Consolidation de la vue des actifs** | Agrégation de vos propres sources | Une vue unifiée exploitable, avec les écarts (ch. 10) | Ce qu'aucune de vos sources ne connaît |
| **Analyse de chemins d'attaque** | Le point de vue de l'attaquant | Les enchaînements entre actifs, identités et droits | Ce qui n'est pas modélisé dans ses sources |
| **Test d'intrusion** | Un attaquant réel, sur un périmètre borné | La démonstration concrète, avec preuve | Le reste du périmètre, et l'instant d'après |

**Le principe fondateur de la découverte externe** mérite d'être compris, parce qu'il explique son rendement : elle part de ce que **l'extérieur** peut savoir de vous — noms de domaine, enregistrements publics, certificats émis à votre nom, blocs d'adresses, mentions publiques — et reconstruit votre surface. Elle trouve donc précisément ce que votre inventaire interne ne connaît pas : le site créé par une équipe marketing chez un hébergeur externe, l'environnement de démonstration monté pour un salon en 2023, la ressource cloud d'un projet abandonné.

⚠️ **PIÈGE — les certificats comme source de découverte**
Les certificats émis publiquement sont enregistrés dans des journaux consultables par tous. Quand vous publiez un service sous un nom, ce nom devient public — y compris pour un environnement de recette ou d'administration que vous pensiez discret. Ce n'est pas une faille, c'est le fonctionnement normal du dispositif, et c'est une des premières sources qu'utilise un attaquant. Nommer un service `admin-preprod.exemple.fr` n'a donc rien de discret.

#### 11.3 L'exposition Internet : ce qu'il faut chercher en premier

Par ordre de gravité constatée, voici ce qui se trouve réellement lors d'un premier exercice de découverte externe.

| Découverte | Pourquoi c'est grave | Fréquence constatée |
|---|---|---|
| **Interface d'administration publiée** | Conçue pour un réseau de confiance, souvent sans authentification forte | Très fréquente |
| **Service oublié** | Plus de propriétaire, donc plus de correctifs depuis des années | Très fréquente |
| Environnement de recette exposé | Données parfois réelles, durcissement moindre (ch. 28) | Fréquente |
| Stockage cloud ouvert | Fuite de données sans aucune intrusion | Fréquente |
| Accès distant secondaire | Mis en place en urgence, jamais retiré | Fréquente |
| Équipement réseau avec interface publiée | Cible de premier choix, très recherchée | Moins fréquente, très grave |

**La première tâche d'un programme de MCS**, avant même de corriger quoi que ce soit, consiste à établir cette liste. Elle est courte, elle se constitue en quelques jours, et elle produit presque toujours des fermetures immédiates — c'est-à-dire une réduction de risque sans correctif, sans fenêtre et sans négociation.

🖼 **SCHÉMA — Chemin d'attaque type en six étapes.** *Graphe orienté du poste bureautique jusqu'à la console de sauvegarde, chaque arête annotée par ce qui la rend praticable (mot de passe local partagé, session privilégiée, joignabilité réseau).*

#### 11.4 Chemins d'attaque : de la liste au graphe

Une vulnérabilité isolée est rarement l'histoire complète. Une compromission réelle est un **enchaînement** : entrée par un actif exposé, récupération d'identifiants, déplacement vers un actif de plus grande valeur, élévation de privilèges, atteinte de l'objectif.

**Les trois dimensions à croiser** — et c'est le croisement qui fait l'information :

| Dimension | Question |
|---|---|
| **Réseau** | Depuis cet actif, qu'est-ce qui est joignable ? |
| **Identité** | Quels comptes existent ou peuvent être obtenus sur cet actif, et où sont-ils valables ailleurs ? |
| **Vulnérabilité** | Que permet techniquement chaque étape ? |

**L'exemple canonique**, qu'on retrouve dans une grande partie des compromissions documentées :

```
Poste bureautique compromis (hameçonnage — aucune vulnérabilité exploitée)
    → un compte d'administration local partage son mot de passe avec 400 autres postes
    → déplacement vers un serveur de fichiers
    → un compte de service à privilèges élevés y a laissé une session ouverte
    → récupération de ce compte
    → accès à la console de sauvegarde
    → accès à l'ensemble des données, y compris les sauvegardes
```

**Ce que cet exemple enseigne au MCS.** Aucune des étapes ne dépend d'une vulnérabilité au sens du chapitre 4, sauf éventuellement la première. Ce qui rend le chemin praticable, ce sont des **choix de configuration et d'identité** : mot de passe local partagé, compte de service surprivilégié, console de sauvegarde joignable depuis le réseau bureautique. C'est précisément le périmètre des chapitres 22 et 24 — et la démonstration que réduire le MCS aux correctifs laisse ce chemin entièrement ouvert.

#### 11.5 Combinaisons toxiques

Une **combinaison toxique** est un ensemble d'éléments individuellement acceptables dont la conjonction crée un risque majeur.

| Élément 1 | Élément 2 | Élément 3 | Résultat |
|---|---|---|---|
| Vulnérabilité de gravité moyenne | Actif joignable depuis Internet | Compte à privilèges élevés présent sur l'actif | Compromission du domaine |
| Machine hors support | Aucune segmentation | Copie de données de production | Fuite de données par un actif « secondaire » |
| Compte de service | Mot de passe inchangé depuis 2019 | Droits d'administration sur 200 machines | Propagation immédiate |
| Recette exposée | Mêmes identifiants qu'en production | Journalisation absente | Compromission indétectable |

**Le point qui rend ces combinaisons dangereuses en pratique** : chaque élément pris isolément passe sous les seuils. La vulnérabilité moyenne n'est pas prioritaire, l'exposition seule paraît acceptable, le compte à privilèges est justifié par un besoin d'exploitation. Aucun outil raisonnant constat par constat ne les remontera. Il faut **croiser**, et le croisement est un travail d'analyse, pas d'outillage.

✅ **BONNE PRATIQUE (P1)** — Faites une revue trimestrielle des combinaisons, sur une liste courte et fixe de règles écrites : *actif exposé + compte à privilèges*, *hors support + non segmenté*, *recette + données de production*, *compte de service + droits étendus + mot de passe ancien*. Quatre requêtes sur votre inventaire enrichi suffisent, et elles trouvent ce qu'aucun scanner ne remonte.

#### 11.6 Atteignabilité : de la présence du composant à l'exécution du code vulnérable

Une nuance qui divise le volume de travail par un facteur important, et qui devient centrale au chapitre 25.

Un outil détecte la **présence** d'un composant vulnérable. Il ne détecte pas si le **code vulnérable est réellement atteignable** dans le contexte d'exécution. Trois niveaux :

| Niveau | Question | Effet sur la priorité |
|---|---|---|
| Présent | Le composant est installé | Signal faible |
| Chargé | Le composant est effectivement utilisé par l'application | Signal moyen |
| **Atteignable** | La fonction vulnérable peut être appelée par une entrée contrôlable par un attaquant | **Signal fort** |

**Deux applications concrètes :**

- Une bibliothèque vulnérable dont la fonction fautive n'est jamais appelée par l'application ne constitue pas un risque exploitable. Le fournisseur peut le déclarer formellement — c'est l'objet des déclarations d'exploitabilité du §4.8.
- Un service vulnérable installé mais **désactivé** n'est pas exposé. Vérifier l'état d'activation avant de traiter un constat évite une part significative du travail — et c'est une vérification de trente secondes.

📌 **LIMITES** — L'analyse d'atteignabilité est coûteuse et imparfaite : elle dépend de la qualité de l'analyse du code, elle traite mal les appels dynamiques, et elle peut donner une fausse assurance. Utilisez-la pour **déprioriser de façon documentée**, jamais pour clore définitivement un constat. La distinction entre déprioriser et clore est traitée au chapitre 17.

#### 11.7 Actifs d'entrée et actifs de niveau 0

Deux catégories méritent un traitement distinct de tout le reste du parc.

**Les actifs d'entrée** — tout ce par quoi un attaquant peut arriver : passerelles d'accès distant, portails publiés, serveurs de messagerie, postes de travail, interfaces d'échange avec des partenaires. Leur particularité : ils sont exposés **par conception**, on ne peut pas fermer leur exposition sans supprimer leur fonction. Le seul levier disponible est donc la **vitesse de correction**. Ce sont eux qui justifient la classe C1 du §7.2.

**Les actifs de niveau 0** — ceux dont la compromission donne le contrôle d'un ensemble d'autres actifs : annuaire, autorité de certification, plan de gestion de virtualisation, console de sauvegarde, outil de déploiement de correctifs, coffre-fort de secrets, chaîne de construction logicielle, outillage d'administration.

⚠️ **PIÈGE — le paradoxe du niveau 0**
Ces actifs sont statistiquement parmi les plus en retard du parc, pour trois raisons convergentes : leur mise à jour « n'apporte rien aux métiers », elle interrompt l'outil que les administrateurs utilisent quotidiennement, et ils sont souvent considérés comme protégés parce qu'ils ne sont pas exposés à Internet. Or leur compromission ne nécessite pas d'exposition externe : elle se produit par un chemin interne (§11.4). **Le fait de ne pas être exposé à Internet ne rend pas un actif secondaire.**

✅ **BONNE PRATIQUE (P0)** — Établissez la liste nominative de vos actifs de niveau 0. Elle tient sur une page. Placez-les tous en classe C1, avec fenêtre récurrente et propriétaire nommé. C'est la mesure de MCS ayant le meilleur rapport effort/réduction de risque de tout ce cours.

#### 11.8 Fermer l'exposition plutôt que corriger

Voici l'un des enseignements les plus rentables de ce cours, et l'un des moins appliqués.

Face à une vulnérabilité sur un actif exposé, deux actions sont possibles : corriger, ou **retirer l'exposition**. Comparons-les honnêtement.

| Critère | Corriger | Fermer l'exposition |
|---|---|---|
| Délai | Heures à semaines | **Minutes à heures** |
| Risque de régression | Réel | Faible, et immédiatement réversible |
| Fenêtre nécessaire | Souvent | Rarement |
| Effet sur les **futures** vulnérabilités du même actif | Aucun | **Protège aussi contre celles à venir** |
| Effet métier | Nul si tout va bien | Peut supprimer un usage légitime |

La quatrième ligne est décisive et rarement formulée : fermer une exposition inutile protège contre toutes les vulnérabilités futures du service concerné, y compris celles qui ne sont pas encore découvertes. C'est la seule action de ce cours qui produise un effet durable sans effort récurrent.

**Les questions à poser systématiquement** devant un actif exposé :

1. Cette exposition est-elle **nécessaire** aujourd'hui, ou héritée d'un besoin passé ?
2. Peut-elle être **restreinte** — à des plages d'adresses connues, derrière une authentification, via un accès distant maîtrisé ?
3. L'interface d'administration a-t-elle besoin d'être publiée, ou seulement le service métier ?

En pratique, une part significative des expositions constatées lors d'un premier inventaire externe ne correspond plus à aucun besoin actif. Les fermer coûte une demi-journée et retire du périmètre à surveiller des actifs entiers.

#### 11.9 Suivre l'exposition dans le temps

L'exposition n'est pas un état, c'est un flux : chaque projet en crée, chaque urgence en ajoute, chaque décommissionnement incomplet en laisse.

**Les trois indicateurs utiles**, définis rigoureusement au chapitre 38 :

- **nombre d'actifs exposés à Internet**, avec son évolution — la tendance importe plus que la valeur absolue ;
- **délai moyen entre l'apparition d'une exposition et sa détection** — mesure la réactivité de votre découverte externe ;
- **nombre de réapparitions** — une exposition fermée qui revient signale un problème de processus, pas de configuration : quelqu'un la recrée, et il faut comprendre pourquoi.

⚠️ **PIÈGE — l'exposition temporaire**
« On ouvre pour la migration, on referme après. » La règle qui fonctionne : **toute ouverture temporaire porte une date de fermeture dans la demande de changement**, et un contrôle automatique vérifie la fermeture à cette date. Sans cela, la statistique est constante : une part importante de ces ouvertures reste en place des années.

#### 11.10 📌 Ce que chaque approche ne voit pas

| Approche | Angle mort |
|---|---|
| Inventaire interne | Ce que vous ne savez pas posséder — ressources hébergées ailleurs, environnements montés hors processus |
| Scanner de vulnérabilités | La joignabilité réelle depuis l'extérieur ; il scanne depuis là où il est placé |
| Découverte externe | L'interne ; et elle peut attribuer à tort un actif qui ne vous appartient pas |
| Analyse de chemins d'attaque | Ce qui n'est pas dans ses sources : systèmes industriels, environnements séparés, applications propriétaires |
| Test d'intrusion | Tout ce qui n'était pas dans le périmètre, et tout ce qui a changé depuis |

**La conséquence méthodologique** : ces approches ne se substituent pas, elles se croisent. Un actif remonté par la découverte externe et absent de l'inventaire interne est le constat le plus riche que produise ce chapitre — il signale à la fois une exposition et un trou d'inventaire.

#### 11.11 ✅ Livrable — Carte des actifs exposés et matrice des chemins critiques

**Partie 1 — Carte des actifs exposés.** Une ligne par actif joignable depuis l'extérieur.

| Actif | Service publié | Depuis quand | Propriétaire | Nécessité confirmée | Restriction possible | Classe | Décision |
|---|---|---|---|---|---|---|---|

**Partie 2 — Matrice des chemins critiques.** Une ligne par enchaînement plausible, limité aux chemins menant à un actif de niveau 0.

| Point d'entrée | Étape intermédiaire | Cible finale | Élément qui rend le chemin praticable | Rupture la moins coûteuse | Prio |
|---|---|---|---|---|---|

**La colonne décisive est l'avant-dernière.** Pour chaque chemin, on ne cherche pas à tout corriger : on cherche **le maillon le moins cher à rompre**. Souvent, ce n'est pas un correctif — c'est une règle de filtrage, un mot de passe local unique par machine, un compte de service dont on retire des droits, ou une console qu'on retire du réseau bureautique.

**Priorisation recommandée** : **P0** pour tout chemin menant à un actif de niveau 0 en trois étapes ou moins ; **P1** au-delà de trois étapes ; **P2** pour les chemins nécessitant un accès physique ou un privilège initial élevé.

#### 11.12 🔴 FIL ROUGE — septembre 2026 : l'interface publiée depuis 2022

Claire Nadeau fait réaliser un premier exercice de découverte externe sur les noms de domaine d'HELIOMED. Trois jours de travail, résultat en une page.

**Ce qui est trouvé.**

| Découverte | Origine | Décision |
|---|---|---|
| Interface d'administration de la passerelle d'accès distant, publiée sur Internet | Ouverture réalisée en mars 2022 pendant une période de télétravail massif, jamais refermée | **Fermeture immédiate**, restriction à deux plages d'adresses |
| Environnement de démonstration d'HelioLink, monté pour un salon en 2023 | Hébergé chez un fournisseur externe, facturé sur la carte du service commercial | Contient une copie de données de test réalistes. Extinction sous 15 jours |
| Deux sous-domaines pointant vers des ressources cloud désallouées | Reliquat d'un projet abandonné | Suppression des enregistrements de noms |
| Trois noms d'environnements internes découverts via les journaux de certificats publics | Nommage explicite : recette, administration, sauvegarde | Aucune exposition réelle, mais information offerte à un attaquant. Politique de nommage revue |

**Le chemin d'attaque qui change la priorisation.** L'interface d'administration de la passerelle porte la vulnérabilité de gravité 5,9 identifiée en février (§4.11) — celle que la méthode initiale, fondée sur la gravité, avait écartée. En croisant avec l'exposition, le constat change de nature : vulnérabilité **présente au catalogue d'exploitation avérée**, sur une interface **d'administration**, **publiée sur Internet**, sur un actif d'**entrée**. Trois des quatre critères de la classe C1 sont réunis.

La fermeture de l'exposition est réalisée le jour même, en quarante minutes, sans fenêtre et sans risque de régression pour les utilisateurs — l'accès métier n'était pas concerné. La correction, elle, est planifiée sous 72 heures.

**Ce que Claire présente au comité.** Non pas « nous avons corrigé une vulnérabilité », mais : *nous avons retiré du périmètre exposé quatre actifs, dont un portait une vulnérabilité activement exploitée, et cette fermeture nous protège également des vulnérabilités futures de ces mêmes services*. La distinction n'est pas rhétorique — c'est celle du §11.8, et c'est ce qui débloque le budget de l'exercice de découverte externe récurrent.

**Livrable de l'épisode.** La carte des actifs exposés, la première matrice de chemins d'attaque d'HELIOMED, et une règle de nommage interdisant les noms explicites sur les enregistrements publics.

**Ce qui se joue sans que personne le sache encore.** La passerelle a été exposée pendant quatre ans et demi. La question de savoir si quelqu'un en a profité pendant cette période n'est pas posée en septembre. Elle le sera brutalement au chapitre 21, et elle constitue le point de départ du cas de synthèse A.

→ La suite en 🔴 §12.8, quand il faudra financer la sortie d'obsolescence de ce que cet inventaire a révélé.

→ **Chapitre 12 — Cycle de vie, obsolescence et dette technique** : l'obsolescence, seule menace dont la date est annoncée à l'avance.

#### Synthèse mentale du chapitre 11

L'inventaire dit ce qui existe, l'exposition dit ce qui peut être atteint — et cette information n'est produite par aucun score, elle vient de vous seul. Trois questions la définissent : depuis où, par qui, et vers quoi cet actif mène-t-il. La troisième transforme la liste en graphe, car une compromission réelle est un enchaînement dont la plupart des étapes ne reposent sur aucune vulnérabilité mais sur des choix de configuration et d'identité. Les combinaisons toxiques échappent à tout outil raisonnant constat par constat : quatre règles écrites et une revue trimestrielle les trouvent. Les actifs de niveau 0 sont statistiquement les plus en retard, précisément parce qu'on les croit protégés par leur absence d'exposition externe. Enfin, fermer une exposition inutile est la seule action qui protège aussi contre les vulnérabilités futures du service : elle coûte des minutes, ne nécessite pas de fenêtre, et une part significative des expositions constatées ne correspond plus à aucun besoin actif.

**Trois questions de vérification**

1. Deux serveurs portent la même vulnérabilité critique ; l'un est publié sur Internet, l'autre joignable uniquement depuis un réseau d'administration. Le score de gravité est identique. Qu'est-ce qui doit différencier votre traitement, et d'où vient cette information ?
2. Reconstruisez un chemin d'attaque en quatre étapes qui ne repose sur aucune vulnérabilité logicielle. Quel est le maillon le moins coûteux à rompre ?
3. Votre équipe demande l'ouverture temporaire d'un accès pour une migration de trois semaines. Quelle condition posez-vous, et pourquoi la formuler au moment de la demande plutôt qu'après ?

---

### Chapitre 12 — Cycle de vie, obsolescence et dette technique

#### 12.1 Le vocabulaire des fins de support, et ses pièges contractuels

L'obsolescence est la seule menace de ce cours dont la date est **annoncée à l'avance**. C'est aussi celle qui produit le plus de situations subies. Le décalage s'explique en grande partie par un vocabulaire flou, que les éditeurs n'ont aucun intérêt à clarifier.

| Terme | Ce qu'il signifie réellement | Ce que les gens comprennent |
|---|---|---|
| **Fin de commercialisation** | On ne peut plus l'acheter | Souvent confondu avec la fin de support |
| **Fin de vie fonctionnelle** | Plus de nouvelles fonctionnalités, mais correctifs de sécurité maintenus | « C'est fini » — alors que non |
| **Fin de support** | **Plus aucun correctif, y compris de sécurité.** La seule date qui compte pour le MCS | Souvent découverte après coup |
| **Support étendu** | Correctifs de sécurité uniquement, contre paiement, sous conditions strictes | « On pourra prolonger » — sans vérifier l'éligibilité |
| **Fin de support étendu** | Terme absolu | Rarement anticipée |
| **Support de sécurité prolongé par un tiers** | Un acteur autre que l'éditeur maintient des correctifs | Confondu avec un support officiel |

⚠️ **PIÈGE — les cinq clauses qui se découvrent trop tard**

1. **L'éligibilité conditionnelle.** Un support étendu est presque toujours réservé à certaines éditions, certaines versions minimales, certains modes de gestion, certains types de licence. La vérification doit être faite **actif par actif**, pas au niveau du produit.
2. **La tarification croissante.** Beaucoup de programmes voient leur tarif augmenter à chaque année reconduite, souvent en doublant. Un budget calculé sur la première année sous-estime gravement une prolongation de trois ans.
3. **Le prérequis d'état.** Certaines offres exigent que la machine soit déjà à jour d'un niveau de correctif précis au moment de la souscription. Une machine trop en retard peut être **inéligible**, ce qui supprime l'option de repli.
4. **La couverture partielle.** Le support étendu ne couvre en général que les vulnérabilités jugées critiques par l'éditeur, selon ses propres critères. Ce n'est pas un support normal prolongé.
5. **La date de décision.** Souscrire après la fin de support coûte souvent la rétroactivité complète des périodes écoulées — la procrastination est facturée.

✅ **BONNE PRATIQUE (P0)** — Pour chaque option de support étendu envisagée, produisez une note d'une page avant tout arbitrage budgétaire : périmètre exact d'éligibilité **vérifié sur votre parc**, coût sur toute la durée envisagée, ce qui est couvert et ce qui ne l'est pas, et date limite de décision. Cette note évite l'essentiel des mauvaises surprises du domaine.

#### 12.2 Construire et tenir un référentiel de fin de support

**L'objectif** : pouvoir répondre à tout moment à la question *« combien d'actifs sortent du support dans les 24 prochains mois, et lesquels ? »*. Sans cette capacité, aucun plan pluriannuel n'est possible.

**Les sources, par fiabilité décroissante :**

| Source | Fiabilité | Remarque |
|---|---|---|
| Page officielle de cycle de vie de l'éditeur | **Fait vérifié** | Seule source opposable ; à consulter, pas à mémoriser |
| Contrat de support signé | Fait vérifié | Peut différer de la politique publique |
| Bases publiques agrégeant les dates de fin de vie | Hypothèse probable | Très pratiques pour le dégrossissage, à confirmer sur les décisions engageantes |
| Connaissance des équipes | Piste exploratoire | Souvent périmée |

**La méthode, en trois temps :**

1. **Extraire** de l'inventaire la liste des systèmes, versions et modèles matériels distincts. Cette liste est bien plus courte que le parc — souvent quelques dizaines de lignes pour plusieurs centaines d'actifs.
2. **Documenter** pour chaque ligne les trois dates : fin de support, fin de support étendu si applicable, source et date de vérification.
3. **Réinjecter** ces dates dans l'inventaire, au niveau de l'actif, pour pouvoir croiser avec la criticité et l'exposition.

⚠️ **PIÈGE — l'obsolescence par composant plutôt que par machine**
Le raisonnement s'arrête trop souvent au système d'exploitation. Or l'obsolescence frappe aussi les moteurs de bases de données, les environnements d'exécution applicatifs, les bibliothèques embarquées, les versions de clusters, les modèles de matériel, les micrologiciels et les certificats. Une machine dont le système est parfaitement supporté peut porter quatre composants hors support — c'est le sujet du chapitre 26.

#### 12.3 Le plan de sortie d'obsolescence

Un plan de sortie d'obsolescence n'est pas une liste : c'est une **trajectoire financée**, avec des jalons et un séquencement.

**Les cinq composants d'un plan crédible :**

| Composant | Contenu | Erreur fréquente |
|---|---|---|
| **Trajectoire** | Quels lots, dans quel ordre, sur quels exercices | Tout traiter la même année |
| **Séquencement technique** | Dépendances : migrer l'annuaire avant les applications qui s'y appuient | Découvrir la dépendance en cours de migration |
| **Financement** | Coût par lot, réparti sur les exercices | Un montant global qui ne passe aucun arbitrage |
| **Jalons de décision** | Dates auxquelles une décision doit être prise, y compris de report | Absence de point de contrôle |
| **Plan de repli** | Que fait-on si le lot n'est pas prêt à l'échéance ? | Aucun — donc report subi |

**Le critère de séquencement qui fonctionne.** Ne triez pas par date de fin de support, triez par **produit criticité × exposition × effort**. Un actif hors support depuis deux ans mais isolé et peu critique passe après un actif exposé qui sortira du support dans six mois. La date n'est qu'une des trois entrées.

✅ **BONNE PRATIQUE (P1) — la règle du lot suivant**
À tout moment, le lot en cours doit être financé **et** le lot suivant doit être chiffré. Sans cette règle, chaque lot se négocie isolément et le plan pluriannuel n'existe que sur le papier.

#### 12.4 ⏱ Panorama des échéances structurantes

*Bloc périssable, vérifié le 30/07/2026. Le calendrier complet et actualisé figure en **Annexe H**.*

**Les échéances majeures du poste de travail et du serveur Windows :**

| Objet | Date | Point d'attention |
|---|---|---|
| Windows 10 — fin de support | 14 octobre 2025 | Échéance **passée** |
| Windows 10 Entreprise LTSB 2016 — fin de support | 13 octobre 2026 | À ne pas confondre avec le Windows 10 grand public |
| Windows Server 2016 — fin de support étendu | 12 janvier 2027 | Souvent sous-estimée dans les parcs |

**Les échéances récurrentes à surveiller sans date fixe** — et c'est la partie la plus utile de cette section, parce qu'elle reste vraie quand les dates ci-dessus auront été franchies :

- **distributions Linux à support long** : cycles de 5 à 10 ans, avec des options de prolongation par abonnement ;
- **moteurs de bases de données** : cycles de 5 à 8 ans, avec des versions intermédiaires au support beaucoup plus court ;
- **environnements d'exécution applicatifs** : cycles souvent **très courts**, de 2 à 4 ans, et c'est la principale source d'obsolescence invisible (chapitre 26) ;
- **versions de clusters d'orchestration** : de l'ordre de quatorze mois (§3.3) ;
- **équipements réseau et de sécurité** : la fin de support **de sécurité** est souvent antérieure à la fin de vie matérielle — les deux dates doivent être suivies séparément ;
- **matériel serveur** : fin de support des micrologiciels, souvent 5 à 7 ans après la commercialisation.

#### 12.5 ⏱ L'économie du support étendu, et un cas d'école

*Bloc périssable, vérifié le 30/07/2026.*

Le cas Windows 10 constitue actuellement l'illustration la plus complète des cinq pièges du §12.1, et il mérite d'être détaillé pour cette raison — le mécanisme vaut bien au-delà de cet éditeur.

**La situation.** Windows 10 est en fin de support depuis le 14 octobre 2025. Deux programmes de prolongation coexistent, et ils n'ont ni le même public, ni le même coût, ni la même échéance.

| Programme | Public | Échéance | Coût |
|---|---|---|---|
| Support étendu **grand public** | Appareils **personnels** | Prolongé jusqu'au 12 octobre 2027 | Gratuit ou faible, selon modalité d'inscription |
| Support étendu **commercial** | Organisations | Jusqu'à trois années après la fin de support | Payant, tarif croissant d'année en année |

⚠️ **LE PIÈGE, et il est majeur.** Le programme grand public **exclut explicitement les machines jointes à un annuaire d'entreprise ou gérées par une solution de gestion de flotte**. Autrement dit : un parc professionnel géré n'est **pas** couvert par la prolongation à octobre 2027, quelle que soit l'édition installée. Une organisation qui lit l'annonce de prolongation et en conclut qu'elle dispose d'un an de plus se trompe de programme — et le découvrira au moment où il sera trop tard pour arbitrer.

📎 [S-24]

**La leçon généralisable, qui survivra à ce cas particulier :**

> Une option de support ne se budgète jamais avant d'avoir vérifié, sur son propre parc et actif par actif, son périmètre d'éligibilité et ses conditions.

**Le calcul à faire systématiquement.** Comparez trois scénarios sur la durée complète, pas sur la première année :

| Scénario | Coûts à intégrer |
|---|---|
| Support étendu sur N années | Coût croissant par actif × N + coût de la migration ensuite, qui reste à payer |
| Migration immédiate | Licences, matériel, tests de compatibilité applicative, formation, charge projet |
| Ne rien faire | Mesures compensatoires, surveillance renforcée, risque accepté, position en cas d'incident ou de contrôle |

Le troisième scénario doit **toujours** figurer dans le tableau, chiffré. C'est en le voyant que les directions arbitrent, et son absence est la raison la plus fréquente pour laquelle un dossier d'obsolescence n'obtient pas de financement.

#### 12.6 Mesurer la dette et la présenter à une direction

Le §1.6 a posé le principe. Voici la mise en œuvre.

**Les quatre grandeurs, et leur formulation.**

| Grandeur | Définition | Ce qu'elle démontre |
|---|---|---|
| **Actifs hors support, pondérés par la criticité** | Nombre d'actifs sans correctif disponible, pondéré C1 ×5, C2 ×3, C3 ×1 | L'ampleur structurelle |
| **Vulnérabilités critiques échues** | Constats critiques dont le délai de la classe de service est dépassé | Le retard opérationnel |
| **Dérogations ouvertes et leur âge** | Nombre et ancienneté moyenne | La dette **formellement acceptée** |
| **Âge moyen des constats non traités** | Durée depuis la première détection | La vitesse réelle de l'organisation |

**La présentation qui fonctionne en comité de direction**, en trois diapositives et pas une de plus :

1. **La trajectoire.** L'évolution de la dette sur quatre à huit trimestres. Une direction ne réagit pas à un niveau, elle réagit à une **pente**.
2. **Le point de bascule.** À quelle date, sans décision, la situation se dégrade mécaniquement — typiquement la prochaine échéance de fin de support majeure.
3. **Les trois options chiffrées.** Support étendu, migration, statu quo — avec pour chacune le coût et le risque résiduel.

⚠️ **PIÈGE — présenter la dette sans option**
Une présentation qui expose un problème sans proposer d'options chiffrées produit de l'anxiété, puis de l'évitement. La direction ne peut pas arbitrer ce qu'elle ne peut pas comparer, et l'arbitrage par défaut est le report.

#### 12.7 ⚠️ « On migrera l'année prochaine » : mécanique du report perpétuel

Le report est rationnel du point de vue de chaque acteur pris isolément, et c'est pour cela qu'il est si difficile à casser.

| Acteur | Sa logique locale | Pourquoi elle est rationnelle pour lui |
|---|---|---|
| Le métier | « Ça marche, ne touchons à rien » | Il porte le risque d'interruption, pas le risque de sécurité |
| L'exploitation | « Nous n'avons pas la charge disponible » | C'est vrai, et la migration s'ajoute au reste |
| La direction financière | « Décalons d'un exercice » | Un décalage améliore le résultat de l'année en cours |
| L'éditeur métier | « Notre version compatible arrive bientôt » | Il n'a pas d'incitation à accélérer |
| La sécurité | Elle alerte, sans mandat pour trancher | Son alerte n'est pas une décision |

**La somme de comportements localement rationnels produit un résultat collectivement absurde.** Ce n'est pas un problème de personnes, et le traiter comme tel garantit l'échec.

**Les quatre leviers qui cassent réellement le cycle :**

1. **La date de bascule visible.** Rendre publique une date après laquelle le report devient une décision explicite de la direction générale, avec signature. Le report cesse d'être un non-choix.
2. **Le coût du report chiffré chaque année.** Support étendu, mesures compensatoires, heures supplémentaires. Un montant qui réapparaît chaque exercice finit par être comparé au coût de la migration.
3. **L'exigence externe.** Un client, un assureur ou un auditeur qui refuse de valider un système hors support (§7.5).
4. **Le lot pilote.** Migrer un périmètre restreint démontre la faisabilité et produit un chiffrage réel. L'argument « c'est trop risqué » ne résiste pas à une migration déjà réalisée ailleurs dans la maison.

#### 12.8 🔴 FIL ROUGE — octobre 2026 : 620 postes et une échéance dans quinze jours

Le 13 octobre 2026 approche. HELIOMED est concerné par trois échéances distinctes, et Claire Nadeau commence par les séparer — parce qu'elles ont été confondues pendant six mois.

| Population | Échéance | Situation réelle |
|---|---|---|
| Banc de test de Saint-Étienne, sous Windows 10 Entreprise LTSB 2016 | **13 octobre 2026** | 1 poste, critique pour la validation des pompes PX-40 |
| 620 postes bureautiques Windows 10, joints au domaine, gérés par l'infogérant | Fin de support depuis le 14/10/2025 | **Non éligibles** au programme grand public |
| 11 serveurs Windows Server 2016 | 12 janvier 2027 | Dont 3 portant des applications métier |

**La découverte qui change tout.** Le chargé de compte de l'infogérant Numeria avait indiqué en juin que « la prolongation annoncée par l'éditeur couvre le parc jusqu'en octobre 2027 ». Malik Ferhaoui vérifie ligne à ligne les conditions d'éligibilité, comme le recommande le §12.1 : le programme invoqué est le programme **grand public**, qui exclut les machines jointes au domaine. Les 620 postes n'ont **jamais** été couverts, et ne recevaient plus de correctifs de sécurité depuis douze mois.

Le sujet cesse d'être un sujet de calendrier. Il devient un sujet de responsabilité contractuelle — traité au chapitre suivant.

**Les trois options présentées au comité stratégique.**

| Option | Coût | Risque résiduel |
|---|---|---|
| Support étendu commercial, 2 ans, sur 620 postes | Coût par poste croissant d'une année sur l'autre + coût de la migration ensuite, qui reste dû | Correctifs critiques uniquement, aucun autre bénéfice |
| Migration en trois lots sur 9 mois | Renouvellement partiel du matériel, tests applicatifs, charge projet | Élevé pendant la période de transition, nul ensuite |
| Statu quo | Zéro budget affiché | 620 postes sans correctif, position intenable en cas d'incident ou de contrôle |

Karim Lebrun, directeur financier, tranche en quinze minutes une fois le tableau posé : la première option coûte, sur deux ans, une part significative du coût de la migration — sans en produire aucun bénéfice durable. La deuxième est retenue, avec un support étendu **partiel** limité à 140 postes portant des applications métier non encore validées sur le nouveau système : c'est un pont, chiffré et daté, pas une solution.

**Le cas du banc de test.** Un seul poste, non migrable — l'outil de validation constructeur n'existe pas sur une version plus récente, et le fournisseur a disparu. La décision relève du chapitre 32 : sanctuarisation, retrait du réseau, transferts par support maîtrisé, dérogation signée par le directeur général avec revue semestrielle. Coût de la solution : quelques milliers d'euros de segmentation, contre le coût d'un remplacement complet de la chaîne de validation.

**Livrable de l'épisode.** Un plan de sortie d'obsolescence sur dix-huit mois, en trois lots financés, avec un pont chiffré, une sanctuarisation documentée, et — ce que Claire considère comme le point le plus important — **une note écrite établissant que les 620 postes n'ont pas reçu de correctifs pendant douze mois**, avec sa cause. Cette note sera au cœur de la négociation contractuelle.

→ La suite en 🔴 §13.9, pour la renégociation du contrat d'infogérance.

→ **Chapitre 13 — MCS délégué : infogérance, prestataires, éditeurs** : ce qui se passe quand le maintien est confié à un tiers.

#### Synthèse mentale du chapitre 12

L'obsolescence est la seule menace dont la date est annoncée à l'avance, et pourtant celle qui produit le plus de situations subies — un vocabulaire flou y contribue, que les éditeurs n'ont pas intérêt à clarifier. Cinq clauses se découvrent trop tard : éligibilité conditionnelle, tarification croissante, prérequis d'état, couverture partielle et rétroactivité. Un référentiel de fin de support se construit sur la liste des versions distinctes, bien plus courte que le parc, et doit couvrir les composants autant que les systèmes. Un plan crédible est une trajectoire financée avec des jalons, séquencée par criticité × exposition × effort plutôt que par date. Le report perpétuel résulte de comportements localement rationnels, ce qui interdit de le traiter comme un problème de personnes : il se casse par une date de bascule visible, un coût de report chiffré chaque année, une exigence externe et un lot pilote. Enfin, tout dossier d'obsolescence doit présenter trois options chiffrées, dont le statu quo — son absence est la première cause de non-financement.

**Trois questions de vérification**

1. Un éditeur annonce la prolongation du support de votre système d'exploitation. Quelles vérifications faites-vous avant d'inscrire cette prolongation dans votre plan, et sur quel niveau de granularité ?
2. Pourquoi trier un plan de sortie d'obsolescence par date de fin de support conduit-il à de mauvaises priorités ? Par quoi remplacez-vous ce critère ?
3. Votre direction a reporté la même migration trois années de suite, chaque fois pour de bonnes raisons. Quels leviers activez-vous, et lequel ne dépend pas d'elle ?

---

### Chapitre 13 — MCS délégué : infogérance, prestataires, éditeurs

#### 13.1 Ce qui est délégable, et ce qui ne l'est jamais

La délégation est la norme, pas l'exception : parc bureautique confié à un infogérant, applications hébergées chez un éditeur, systèmes industriels maintenus par un constructeur, infrastructure chez un fournisseur cloud. Un programme de MCS qui ne traite que ce que vous exploitez vous-même couvre souvent moins de la moitié du périmètre.

**La distinction fondatrice, à poser une fois pour toutes :**

| Délégable | Jamais délégable |
|---|---|
| L'**exécution** : appliquer les correctifs, tester, redémarrer | La **décision** d'accepter un risque |
| La **détection** : scanner, remonter les constats | La définition des **exigences** : délais, périmètre, criticité |
| La **production de preuve** : rapports, journaux | Le **contrôle** que ces exigences sont tenues |
| L'**expertise** technique sur une plateforme | La **responsabilité** vis-à-vis de vos clients et du régulateur |

**La conséquence pratique**, à énoncer clairement devant toute direction qui pense avoir transféré le sujet avec le contrat : vous pouvez déléguer le travail, vous ne pouvez pas déléguer d'en répondre. Un incident causé par un défaut de mise à jour chez votre prestataire reste votre incident vis-à-vis de vos clients, de vos utilisateurs et de l'autorité de contrôle. Le contrat organise le recours entre vous et lui ; il ne vous exonère pas devant les tiers.

#### 13.2 Lire un contrat d'infogérance sous l'angle du MCS

La plupart des contrats d'infogérance sont construits autour de la **disponibilité**. C'est ce que le client demande et ce que le prestataire sait mesurer. La sécurité y figure souvent de manière générale, sans obligation vérifiable.

**Les quatre questions à poser à un contrat existant** — l'exercice prend deux heures et produit systématiquement des surprises :

| Question | Réponse fréquente | Ce qu'elle signifie |
|---|---|---|
| Quel **délai** de correction est engagé, par criticité ? | Aucun, ou « dans les meilleurs délais » | Aucune obligation opposable |
| Quel **périmètre** exact est couvert ? | Flou : « le parc bureautique » | Les exclusions apparaissent au moment du litige |
| Quelles **données** le prestataire doit-il restituer, à quelle fréquence ? | Un rapport de disponibilité mensuel | Vous ne pouvez pas mesurer votre propre conformité |
| Que se passe-t-il en cas de **manquement** ? | Rien de spécifique | L'obligation sans sanction est une intention |

🏢 **VU EN RÉUNION** — Point mensuel avec un infogérant. Le chargé de compte présente 99,94 % de disponibilité, félicitations générales. Le RSSI demande le taux d'application des correctifs. Réponse : « ce n'est pas un indicateur que nous produisons ». Ce n'était pas un refus : personne ne le lui avait jamais demandé, et le contrat ne le prévoyait pas.

⚠️ **PIÈGE — le taux de disponibilité comme indicateur de sécurité**
Un prestataire tenu à 99,9 % de disponibilité a une incitation **contraire** à l'application rapide des correctifs : chaque redémarrage consomme son budget d'indisponibilité, chaque correctif crée un risque de régression dont il porte la pénalité. Sans engagement de sécurité symétrique, le contrat pousse structurellement au report. Ce n'est pas de la mauvaise volonté, c'est le contrat qui produit ce comportement.

#### 13.3 Les clauses à exiger

Voici le jeu minimal, formulé de manière directement réutilisable. Le modèle complet figure en **Annexe D**.

| # | Clause | Formulation |
|---|---|---|
| 1 | **Délais par criticité** | « Le prestataire applique les correctifs selon les délais suivants, décomptés à partir de la publication du correctif : [reprendre les classes de service du §7.2] » |
| 2 | **Périmètre nominatif** | « Le périmètre couvert est défini par la liste des actifs annexée, mise à jour trimestriellement et contradictoirement » |
| 3 | **Restitution de données** | « Le prestataire fournit mensuellement, dans un format exploitable, l'état de mise à jour de chaque actif du périmètre, **y compris la liste des actifs non joignables** » |
| 4 | **Notification de vulnérabilité** | « Le prestataire notifie sous 24 heures toute vulnérabilité activement exploitée affectant un actif du périmètre, ainsi que toute impossibilité de correction » |
| 5 | **Transparence des versions** | « Le prestataire communique sur demande les versions déployées et son propre calendrier d'obsolescence » |
| 6 | **Droit d'audit** | « Le client peut faire réaliser, à sa charge, un contrôle technique du périmètre, avec un préavis de X jours » |
| 7 | **Sous-traitance en cascade** | « Le prestataire déclare ses propres sous-traitants intervenant sur le périmètre et leur impose les mêmes obligations » |
| 8 | **Escalade des impossibilités** | « Toute impossibilité de correction est notifiée sous 5 jours ouvrés, avec sa cause et une proposition de mesure compensatoire » |
| 9 | **Réversibilité** | « En fin de contrat, le prestataire restitue l'inventaire complet, l'historique de mise à jour et la documentation d'exploitation » |
| 10 | **Sanction** | « Le non-respect des délais donne lieu à [pénalité / plan de retour à la conformité sous contrôle] » |

**Les trois clauses qui produisent le plus d'effet**, si vous ne pouvez en obtenir que trois : la **restitution de données** (3), sans laquelle vous ne pouvez rien mesurer ; l'**escalade des impossibilités** (8), qui transforme le silence en obligation ; et la **transparence sur le périmètre** (2), qui empêche le débat sur ce qui était inclus.

✅ **BONNE PRATIQUE (P0)** — La clause 3 est celle à obtenir en priorité, y compris en la négociant seule et en cours de contrat. Sans donnée restituée, votre indicateur affiche « non mesuré » (§10.11) — ce qui est honnête, mais ne réduit aucun risque. Avec la donnée, vous pouvez piloter, y compris sans les autres clauses.

#### 13.4 Les référentiels de prestation d'administration et de maintenance

**Le besoin auquel ils répondent.** Un prestataire d'infogérance dispose des accès les plus privilégiés de votre système d'information : comptes d'administration, outils de déploiement, accès distants permanents. Il constitue à ce titre un actif de niveau 0 externalisé — et un chemin d'attaque de premier ordre. Plusieurs compromissions majeures documentées ont emprunté cette voie : compromettre un prestataire pour atteindre l'ensemble de ses clients.

**Ce que ces référentiels encadrent**, indépendamment du schéma considéré : la sécurisation des postes et des accès d'administration du prestataire, la gestion et la traçabilité des comptes à privilèges, le cloisonnement entre les clients, la journalisation des actions d'administration, et les compétences et l'organisation du prestataire.

⏱ **ÉTAT DE L'ART (à vérifier lors de chaque revue)** — En France, un référentiel dédié aux prestataires d'administration et de maintenance sécurisées a été élaboré par l'ANSSI. **Le statut exact du schéma de qualification et la liste des prestataires éventuellement qualifiés doivent être vérifiés directement sur le site de l'agence** : ce type de dispositif évolue, et une information périmée sur ce point peut orienter à tort un choix de prestataire. 📎 [S-15]

**Ce que vous pouvez en faire même sans qualification formelle.** Le référentiel constitue une **grille d'exigences réutilisable** dans un appel d'offres ou un questionnaire fournisseur, indépendamment de tout schéma de certification. Cinq questions en tirent l'essentiel :

1. Les postes utilisés pour administrer notre parc sont-ils dédiés à l'administration, ou servent-ils aussi à la messagerie et à la navigation ?
2. Comment sont gérés les comptes à privilèges utilisés chez nous, et sont-ils propres à notre organisation ?
3. Comment est assuré le cloisonnement entre vos clients ?
4. Les actions d'administration sont-elles journalisées, et pouvons-nous obtenir ces journaux ?
5. Quel est votre propre niveau de maintien en condition de sécurité, et comment le démontrez-vous ?

La cinquième question est celle qui met le plus souvent mal à l'aise. C'est aussi la plus légitime.

#### 13.5 Maîtriser le MCS de l'administrateur externe

Le prestataire, en tant que chemin d'accès, mérite un traitement à part — au même titre que les actifs de niveau 0 du §11.7.

**Les cinq points de contrôle :**

| Point | Ce qu'il faut obtenir | Pourquoi |
|---|---|---|
| **Postes d'administration** | Postes dédiés, durcis, à jour, sans usage bureautique | Un poste d'administration qui lit des courriels est un point d'entrée direct vers vos droits les plus élevés |
| **Comptes** | Comptes nominatifs, propres à votre organisation, avec authentification forte | Un compte partagé entre plusieurs clients propage une compromission |
| **Accès distant** | Accès à la demande, borné dans le temps, journalisé | Un accès permanent est une exposition permanente |
| **Journalisation** | Journaux d'actions d'administration accessibles **de votre côté** | Sans cela, vous ne pouvez rien reconstituer après incident |
| **Retrait** | Procédure de retrait des accès au départ d'un intervenant | Les comptes d'anciens intervenants sont un classique des audits |

⚠️ **PIÈGE — l'accès permanent hérité**
Beaucoup d'organisations découvrent, lors d'un premier inventaire des accès, des comptes de prestataires dont le contrat s'est terminé il y a plusieurs années. Le mécanisme est toujours le même : personne ne détient la procédure de retrait, parce qu'elle n'a jamais été écrite. C'est un sujet du chapitre 24, et c'est aussi un sujet de décommissionnement (chapitre 35).

#### 13.6 Éditeurs et fournisseurs de services

La délégation ne s'arrête pas à l'infogérance. Chaque éditeur d'application métier, chaque fournisseur de service en ligne, chaque constructeur d'équipement porte une part de votre MCS.

**Les cinq questions à poser à tout fournisseur**, en évaluation comme en revue périodique :

1. **Quelle est votre politique de publication de correctifs de sécurité ?** Fréquence, canaux, délai entre découverte et publication.
2. **Combien de versions maintenez-vous simultanément, et pendant combien de temps ?** C'est ce qui détermine si vous serez contraint à des montées de version subies.
3. **Quel préavis donnez-vous avant une fin de support ?** Six mois est court pour une application métier critique.
4. **Comment nous notifiez-vous une vulnérabilité affectant votre produit ?** Un fournisseur qui ne notifie pas vous laisse découvrir par la presse.
5. **Quels composants tiers votre produit embarque-t-il ?** C'est la question de l'inventaire de composants (§4.8), et elle deviendra réglementaire pour de nombreux produits.

⚠️ **PIÈGE — le prérequis figé**
Certains éditeurs métier conditionnent leur support à une version précise du système d'exploitation, du moteur de base de données ou de l'environnement d'exécution. Vous héritez alors de **leur** calendrier, et vous ne pouvez plus corriger sans perdre le support. C'est l'exigence n° 2 du §6.2 — et elle se négocie avant la signature, jamais après. Une fois l'application déployée et le métier dépendant, votre pouvoir de négociation est nul.

#### 13.7 Ce que la réglementation change dans les deux sens

Un effet notable des évolutions réglementaires est de faire circuler les exigences le long de la chaîne d'approvisionnement, dans les deux sens.

**Vers l'amont — ce que vous devez demander.** Si vous êtes soumis à des obligations de maîtrise de votre chaîne d'approvisionnement, vous devez pouvoir démontrer que vous imposez des exigences à vos fournisseurs et que vous les contrôlez. Les clauses du §13.3 ne sont plus seulement de bonne gestion : elles deviennent un élément de preuve.

**Vers l'aval — ce qu'on va vous demander.** Symétriquement, vos clients vous adresseront les mêmes questionnaires. C'est déjà le cas, souvent avant toute obligation légale (§8.1).

✅ **BONNE PRATIQUE (P1) — le dossier fournisseur réutilisable**
Constituez **une fois** un dossier de réponse standard : votre politique MCS, vos classes de service et délais, votre couverture mesurée, votre traitement des exceptions, votre organisation de gestion des incidents. Vous répondrez à 80 % des questionnaires clients par extraction plutôt que par rédaction. C'est le même dossier de preuves que celui du §8.8 — d'où l'intérêt de le construire dans une structure unique.

#### 13.8 📌 Limites : l'asymétrie de pouvoir

Tout ce chapitre suppose une capacité de négociation. Elle n'existe pas toujours, et le nier serait malhonnête.

| Situation | Ce qui est réellement possible |
|---|---|
| Fournisseur dominant, contrat d'adhésion non négociable | Aucune clause spécifique. Reste : documenter le risque accepté, exploiter ce que le fournisseur publie déjà, préparer une alternative |
| Petit client d'un grand infogérant | Peu de pouvoir individuel. Levier : le renouvellement, et le groupement avec d'autres clients |
| Éditeur métier en situation de monopole fonctionnel | Négociation faible. Levier : le contrat de maintenance annuel, et la trace écrite des demandes refusées |
| Prestataire en difficulté financière | Le rapport de force s'inverse contre vous : il faut anticiper la réversibilité |

**Ce qui reste toujours possible, quelle que soit l'asymétrie :**

1. **Écrire.** Une demande formalisée, refusée par écrit, change radicalement votre position juridique et votre position en audit.
2. **Mesurer par vous-même** ce que le prestataire ne restitue pas — un scan authentifié de votre côté, si le contrat le permet.
3. **Déclarer non couvert** ce que vous ne pouvez ni mesurer ni imposer (§7.7). C'est ce qui rend le sujet finançable.
4. **Préparer la réversibilité** : un fournisseur qu'on ne peut pas quitter est un fournisseur avec qui on ne négocie pas.

#### 13.9 🔴 FIL ROUGE — novembre 2026 : la renégociation

Munie de la note établissant que 620 postes n'ont reçu aucun correctif de sécurité pendant douze mois (§12.8), Claire Nadeau conduit avec Sonia Weber la renégociation du contrat Numeria, dix mois avant son échéance.

**La position initiale du prestataire.** Le contrat de 2023 ne comporte aucun engagement de délai de correction. Le chargé de compte le rappelle : ce qui n'était pas au contrat n'était pas dû. Juridiquement, il n'a pas tort.

**Le levier qui déplace la discussion.** Claire ne conteste pas ce point. Elle expose deux faits : l'information transmise en juin sur l'éligibilité au programme de support étendu était **inexacte**, et cette inexactitude a fondé une décision de report chez HELIOMED. Le sujet cesse d'être « qui devait patcher » pour devenir « quelle information avons-nous reçue ». La négociation change de terrain.

**Ce qui est obtenu à l'avenant, et ce qui ne l'est pas.**

| Demande | Résultat |
|---|---|
| Restitution mensuelle de l'état de mise à jour, actifs non joignables inclus | **Obtenu**, format exploitable, à compter de janvier 2027 |
| Délais de correction par criticité, alignés sur les classes de service | **Obtenu partiellement** : 7 jours pour les vulnérabilités exploitées, 30 jours pour les critiques. Pas d'engagement sur le reste |
| Notification sous 24 h des vulnérabilités exploitées et des impossibilités | **Obtenu** |
| Périmètre nominatif annexé, révisé trimestriellement | **Obtenu** |
| Droit d'audit technique | **Obtenu**, avec préavis de 30 jours et à la charge d'HELIOMED |
| Pénalités financières | **Refusé.** Remplacé par un plan de retour à la conformité sous contrôle en cas de manquement constaté deux mois consécutifs |
| Déclaration des sous-traitants | **Obtenu** |

**La contrepartie.** Numeria obtient une revalorisation d'environ 6 % du contrat, justifiée par la charge de production des rapports et l'engagement de délais. Karim Lebrun valide sans difficulté : le coût annuel supplémentaire représente une fraction de ce qu'aurait coûté le support étendu sur deux ans (§12.8).

**Ce que Claire retient de la négociation**, et qu'elle formalise en règle interne : *aucun périmètre délégué n'entre en service sans clause de restitution de données*. Sans mesure, il n'y a pas de pilotage — seulement de la confiance, ce qui n'est pas une méthode.

**Livrable de l'épisode.** L'avenant contractuel, et la grille de dix clauses du §13.3 versée au référentiel achats d'HELIOMED pour tout futur contrat d'infogérance ou d'hébergement.

→ La suite en 🔴 §14.11, quand la chaîne de veille devra couvrir un périmètre devenu beaucoup plus large que le parc interne.

→ **Chapitre 14 — Veille et sources de constats** : savoir qu'un problème existe — et distinguer les quinze origines de constats.

#### Synthèse mentale du chapitre 13

On délègue l'exécution, la détection et la production de preuve ; on ne délègue jamais la décision d'accepter un risque, la définition des exigences, le contrôle, ni la responsabilité devant les tiers. Un contrat construit sur la seule disponibilité pousse structurellement au report des correctifs, puisque chaque redémarrage consomme le budget d'indisponibilité du prestataire — ce n'est pas de la mauvaise volonté, c'est le contrat qui produit ce comportement. Dix clauses couvrent le sujet, dont trois sont décisives : restitution de données, escalade des impossibilités, périmètre nominatif. Le prestataire d'administration est un actif de niveau 0 externalisé : postes dédiés, comptes propres à votre organisation, accès bornés, journaux accessibles de votre côté, procédure de retrait écrite. Un prérequis de version imposé par un éditeur métier se négocie avant la signature, jamais après. Enfin, quand l'asymétrie interdit toute négociation, quatre actions restent toujours possibles : écrire, mesurer soi-même, déclarer non couvert, et préparer la réversibilité.

**Trois questions de vérification**

1. Votre infogérant tient un engagement de disponibilité de 99,9 % et n'a aucun engagement de sécurité. Expliquez pourquoi cette configuration retarde mécaniquement les correctifs, sans mettre en cause sa bonne foi.
2. Vous ne pouvez obtenir qu'une seule clause supplémentaire à votre contrat. Laquelle demandez-vous, et pourquoi celle-là plutôt que des pénalités ?
3. Un fournisseur de service en ligne refuse toute modification contractuelle. Que faites-vous concrètement, en quatre actions ?

---

---

> ### 🎓 À ce stade de la Partie II, vous savez…
>
> - **rédiger** une politique MCS décidable, finançable, et qui prévoit un chemin légitime pour les cas où corriger est impossible ;
> - **construire** des classes de service avec des délais calibrés sur une capacité mesurée, dont une classe explicite pour les actifs non corrigeables ;
> - **lire** un référentiel réglementaire selon la grille exigence / objectif / moyen, et distinguer ce qui oblige de ce qui inspire ;
> - **répartir** les rôles sans faire du RSSI le propriétaire de l'exécution, et pré-arbitrer les conflits récurrents plutôt que les trancher à chaque fois ;
> - **construire** un périmètre de référence en croisant plusieurs sources, et **lire les écarts** plutôt que choisir un chiffre ;
> - **distinguer** ce qui existe de ce qui est atteignable, et reconnaître qu'une fermeture d'exposition protège aussi contre les vulnérabilités futures ;
> - **bâtir** un plan de sortie d'obsolescence financé, et exiger d'un prestataire les trois clauses qui rendent la mesure possible.
>
> **Ce que vous ne savez pas encore** : comment faire tourner la chaîne au quotidien. C'est l'objet de la Partie III.


## PARTIE III — Le cœur opérationnel

Les deux premières parties ont construit le socle et le cadre. Celle-ci décrit la chaîne d'exécution, dans l'ordre où elle se déroule réellement : **savoir qu'il existe un problème** (ch. 14), **savoir s'il vous concerne** (ch. 15), **décider quoi traiter** (ch. 16), **piloter le traitement** (ch. 17), **corriger** (ch. 18 et 19), **faire quand on ne peut pas corriger** (ch. 20), et **réagir quand tout s'accélère** (ch. 21).

C'est la partie la plus dense du cours, et celle à laquelle vous reviendrez le plus souvent.

---

### Chapitre 14 — Veille et sources de constats

#### 14.1 Cartographier ses besoins de veille à partir de l'inventaire

L'erreur de départ la plus commune consiste à s'abonner d'abord à des sources, puis à chercher ce qui, dans le flux reçu, pourrait concerner l'organisation. Le résultat est prévisible : un volume ingérable, une fatigue rapide, et paradoxalement des angles morts — parce que les sources choisies reflètent ce qu'on connaît déjà.

**La démarche inverse.** Partez de l'inventaire (chapitre 10), extrayez la liste des **technologies distinctes** présentes dans votre parc, et construisez la veille à partir de cette liste.

🧪 **EN PRATIQUE — la matrice de couverture de veille**

| Technologie présente | Nb d'actifs | Criticité max | Source de veille | Canal | Vérifié le |
|---|---|---|---|---|---|
| Système serveur A | 118 | C1 | Avis officiel éditeur | Flux + courriel | 30/07/2026 |
| Pare-feu constructeur B | 6 | C1 | Portail sécurité constructeur | Compte à créer | — |
| Progiciel métier C | 1 | C1 | **Aucune source identifiée** | — | — |
| Automate D | 12 | C4 | Bulletin constructeur, publication irrégulière | Courriel | 30/07/2026 |

**Ce que cette matrice révèle immédiatement**, et qui justifie à elle seule l'exercice : les lignes sans source. Elles correspondent presque toujours à des progiciels métier, des équipements industriels et des services en ligne — c'est-à-dire souvent des actifs critiques. Un flux de veille abondant sur les systèmes d'exploitation ne compense en rien ces trous ; il les masque en donnant le sentiment d'être informé.

✅ **BONNE PRATIQUE (P0)** — Construisez cette matrice avant de vous abonner à quoi que ce soit. Elle tient sur deux pages pour un parc de taille intermédiaire, et elle transforme la veille d'un flux subi en une couverture mesurable — avec un indicateur associé : *part des technologies du parc couvertes par au moins une source identifiée*.

#### 14.2 Le MCS n'est pas la gestion des CVE

C'est l'un des points les plus importants de tout le cours, et il découle directement du §1.3 : dix objets se dégradent, et les vulnérabilités logicielles n'en sont qu'un.

**La typologie complète des constats** qui doivent entrer dans votre chaîne de traitement :

| Origine | Exemple de constat | A-t-il un identifiant de vulnérabilité ? |
|---|---|---|
| Avis d'éditeur | Correctif de sécurité publié | Souvent, pas toujours |
| Bulletin d'un centre de réponse aux incidents | Alerte sur une exploitation en cours | Généralement |
| **Test d'intrusion** | Interface d'administration sans authentification | **Non** |
| **Audit de configuration** | Écart à la baseline sur 40 serveurs | **Non** |
| **Programme de récompense / divulgation** | Faille signalée par un chercheur externe | Pas encore |
| **Incident** | Compte compromis, chemin d'entrée identifié | **Non** |
| **Recherche de menace proactive** | Persistance découverte sur un poste | **Non** |
| **Mauvaise configuration cloud** | Stockage ouvert publiquement | **Non** |
| **Secret exposé** | Clé d'accès trouvée dans un dépôt de code | **Non** |
| **Chemin d'attaque** | Compte de service surprivilégié (ch. 11) | **Non** |
| **Revue d'architecture** | Système non interruptible (ch. 6) | **Non** |
| **Obsolescence** | Composant hors support | **Non** |
| **Contenu de détection périmé** | Agents sans mise à jour depuis 21 jours | **Non** |
| Vulnérabilité matérielle | Faille de processeur ou de micrologiciel | Parfois |

⚠️ **PIÈGE — l'organisation qui ne traite que ce qui a un identifiant**
Le symptôme est facile à repérer : le processus de remédiation est branché sur le scanner de vulnérabilités, et sur lui seul. Les rapports de test d'intrusion finissent dans un dossier partagé, les écarts de configuration dans un tableur, les constats d'audit dans un plan d'action distinct. Résultat : plusieurs files de traitement parallèles, des priorités incomparables entre elles, et un constat majeur — l'interface d'administration exposée du mini-lab 1 — qui progresse moins vite qu'une vulnérabilité mineure de bibliothèque, uniquement parce qu'elle est arrivée par le mauvais canal.

✅ **BONNE PRATIQUE (P0) — la file unique**
Tous les constats, quelle que soit leur origine, entrent dans **la même file de traitement**, avec la même méthode de priorisation (chapitre 16) et le même cycle de vie (chapitre 17). C'est la décision d'organisation qui produit le plus d'effet dans tout ce cours, et elle ne coûte rien d'autre qu'une décision.

#### 14.3 Les sources primaires

Une source primaire est celle qui produit l'information d'origine. Elle fait foi.

| Source | Ce qu'elle apporte | Précaution |
|---|---|---|
| **Avis de sécurité de l'éditeur du produit** | La vérité sur les versions affectées et corrigées | C'est **la** source de vérité sur « suis-je vulnérable » (§2.2) |
| **Avis de sécurité de votre distribution** | L'état du paquet chez elle, correctifs rétroportés inclus | Indispensable sur les systèmes à support long |
| **Bulletins des centres de réponse nationaux** | Contexte, criticité, exploitation observée, recommandations | Généralement le meilleur point d'entrée quotidien |
| **Listes de diffusion sécurité des projets** | Information brute, souvent la plus rapide | Volume élevé, peu de mise en forme |
| **Avis lisibles par machine** | Automatisation du rapprochement (§4.8) | Adoption inégale selon les éditeurs |

✅ **BONNE PRATIQUE (P1)** — Pour chaque produit de classe C1 de votre parc, identifiez et **testez** le canal officiel de notification de l'éditeur. Beaucoup d'organisations découvrent au premier incident que l'adresse de contact enregistrée chez le fournisseur est celle d'un administrateur parti depuis trois ans. Vérifiez que vous recevez réellement, et faites-le figurer dans la matrice du §14.1.

#### 14.4 Les sources agrégées, et pourquoi la redondance est devenue nécessaire

Les bases agrégées collectent, dédoublonnent et enrichissent l'information issue des sources primaires. Elles apportent la couverture et l'exploitabilité automatique ; elles ajoutent une latence et un risque de dépendance.

**Ce qui a changé** (§4.9) : l'écosystème s'est fragmenté, l'enrichissement d'une base majeure est devenu sélectif, une base européenne est montée en charge, et d'autres initiatives d'identification existent. Une architecture de veille qui reposait sur une source unique enrichie ne fonctionne plus telle quelle.

**L'architecture de veille recommandée**, en trois étages complémentaires :

```
Étage 1 — Vérité produit     : avis de l'éditeur et de la distribution
                               → répond à « suis-je affecté, et quelle version corrige ? »
Étage 2 — Couverture          : base agrégée, quelle qu'elle soit
                               → répond à « qu'est-ce qui existe, sans rien manquer ? »
Étage 3 — Signal d'exploitation : catalogue d'exploitation avérée + renseignement
                               → répond à « est-ce réellement utilisé par des attaquants ? »
```

Les trois étages répondent à trois questions différentes, et aucun ne remplace les autres. C'est cette structure, et non le choix d'un fournisseur particulier, qui rend une veille robuste au changement.

#### 14.5 Le renseignement sur la menace appliqué au MCS

Beaucoup d'organisations consomment du renseignement sur la menace sans savoir qu'en faire. Pour le MCS, son apport se ramène à trois usages précis, et il faut se limiter à ceux-là.

| Usage | Question à laquelle il répond | Effet concret |
|---|---|---|
| **Exploitation observée** | Cette vulnérabilité est-elle utilisée en ce moment ? | Entrée directe dans la priorisation (ch. 16) |
| **Ciblage sectoriel** | Des campagnes visent-elles mon secteur, avec quels vecteurs ? | Priorise les technologies visées, avant l'entrée dans un catalogue public |
| **Comportement des attaquants** | Quels chemins empruntent-ils ? | Oriente la cartographie des chemins d'attaque (ch. 11) |

**Les sources sectorielles** — centres de réponse sectoriels, communautés de partage entre pairs, groupements professionnels — sont particulièrement utiles ici, parce qu'elles voient ce qui vise **votre** secteur avant que cela n'apparaisse dans les catalogues généralistes. C'est la seule réponse partielle à la limite structurelle du §4.6 : un catalogue public est en retard sur les campagnes ciblées.

📌 **LIMITES** — Le renseignement sur la menace ne dit rien de votre exposition, se prête mal à l'automatisation directe, et son coût peut être élevé pour une valeur ajoutée faible si l'organisation n'a pas d'abord traité l'inventaire et l'exposition. **Ne l'achetez pas avant d'avoir fait les chapitres 10 et 11.**

#### 14.6 Automatiser la veille

L'automatisation consiste à rapprocher automatiquement les avis reçus et l'inventaire, pour ne présenter à un humain que ce qui concerne réellement le parc.

**La chaîne type :**

```
Avis reçus (flux, courriels, formats structurés)
   → normalisation (identifiant, produit, versions affectées, versions corrigées)
   → rapprochement avec l'inventaire enrichi (ch. 10)
   → filtrage : ne concerne aucun actif → archivé, pas supprimé
   → constats candidats → file unique de traitement (ch. 17)
```

⚠️ **PIÈGE — les quatre défaillances du rapprochement automatique**

| Défaillance | Effet | Atténuation |
|---|---|---|
| Nom de produit divergent entre l'avis et l'inventaire | Faux négatif : l'avis vous concerne, vous ne le voyez pas | Table de correspondance maintenue, revue périodique |
| Intervalle de versions imprécis dans l'avis | Faux positif ou faux négatif | Confirmation par l'avis éditeur |
| Rétroportage (§2.2) | Faux positif massif | Comparer la révision éditeur, pas la version amont |
| Composant embarqué non déclaré dans l'inventaire | Faux négatif silencieux | Inventaire de composants (ch. 25) |

**Le faux négatif est le vrai danger.** Un faux positif coûte du temps ; un faux négatif produit une exposition dont personne n'a connaissance. C'est pourquoi la règle est d'**archiver** ce qui est écarté automatiquement plutôt que de le supprimer : le jour où un avis écarté à tort refait surface, vous pouvez comprendre pourquoi il a été manqué et corriger la règle.

#### 14.7 Qualifier une alerte : fait, hypothèse, piste

Une discipline de langage qui évite beaucoup d'erreurs de décision, et qui sera reprise dans tout le cours.

| Statut | Définition | Ce qu'on peut en faire |
|---|---|---|
| **Fait vérifié** | Constaté directement, ou établi par une source de vérité | Fonder une décision engageante |
| **Hypothèse probable** | Cohérent avec plusieurs indices, non confirmé | Déclencher une vérification, préparer une action |
| **Piste exploratoire** | Possible, non étayé | Investiguer, ne rien décider |

**L'exemple type.** Un scanner remonte une vulnérabilité sur 42 serveurs. Statut réel : **piste exploratoire**, tant que la révision du paquet n'est pas vérifiée (§2.2). Après vérification sur trois machines représentatives : **hypothèse probable** pour les 39 autres. Après vérification exhaustive ou confirmation par l'avis de la distribution : **fait vérifié**.

✅ **BONNE PRATIQUE (P1)** — Faites figurer ce statut dans chaque communication interne, et particulièrement dans les remontées à la direction. « Nous avons 1 176 vulnérabilités critiques » est une affirmation non qualifiée ; « nous avons 1 176 constats candidats, dont 31 confirmés comme activement exploités et 7 sur des actifs exposés » est une information sur laquelle on peut décider. La différence de crédibilité est considérable, et elle se construit une fois.

#### 14.8 La cadence humaine

Une chaîne de veille automatisée ne dispense pas d'un dispositif humain. Trois questions doivent avoir une réponse écrite.

| Question | Réponse type |
|---|---|
| **Qui lit quoi, et quand ?** | Un rôle nommé, une plage horaire, une liste de sources — pas « l'équipe sécurité » |
| **Quel est le délai maximal de prise en compte ?** | Par exemple : 4 h ouvrées pour une alerte d'exploitation active, 24 h pour le reste |
| **Que se passe-t-il en dehors des heures ouvrées, en congés, en arrêt ?** | Suppléance nommée, ou acceptation explicite du délai |

⚠️ **PIÈGE — la veille reposant sur une personne**
Configuration extrêmement courante : une personne, passionnée, suit tout, et le dispositif fonctionne remarquablement — jusqu'à son départ, son arrêt maladie ou ses congés d'août. Deux mesures suffisent : une **suppléance nommée** et une **procédure écrite d'une page** décrivant les sources, les accès et le critère de déclenchement. Les crises de vulnérabilité majeures des dernières années se sont produites, statistiquement, aussi souvent en août et fin décembre qu'en mars.

#### 14.9 📌 Limites de la veille

- **Le délai structurel.** Entre l'exploitation réelle et sa publication, il s'écoule un temps incompressible. Une veille parfaite est en retard sur les attaquants, par construction.
- **Les vulnérabilités sans identifiant.** Corrigées silencieusement par un éditeur, elles n'apparaissent dans aucune base. C'est un argument fort pour appliquer les correctifs même sans avis, et pour suivre les notes de version.
- **Les avis inexacts.** Versions affectées incomplètes, correctifs annoncés mais non publiés, avis révisés après coup. La vérification vaut mieux que la confiance.
- **La surcharge.** Une veille trop large produit une fatigue qui dégrade la qualité de traitement de ce qui compte. Mieux vaut couvrir complètement les actifs C1 que partiellement tout le parc.

#### 14.10 🔬 Mini-lab 3 — Qualifier un bulletin éditeur ambigu

**Objectif** — Décider avec une information incomplète, et distinguer ce qui se fait le soir même de ce qui attend.
**Durée** 20 min · **Difficulté** 🟢 débutant · **Prérequis** §14.7, §16.4 · **Livrable** décision argumentée + demande écrite au fournisseur.
**Compétences validées** — ✔ décider avec une information incomplète ✔ identifier l'information manquante déterminante ✔ formuler une demande fournisseur traçable ✔ poser une décision par défaut

**Énoncé.** Vous recevez, un vendredi à 17 h 40, le bulletin suivant d'un éditeur d'un progiciel métier utilisé par votre service comptable :

> *« Une vulnérabilité de sécurité importante a été identifiée dans notre plateforme. Nous recommandons à tous nos clients d'appliquer la mise à jour 8.4.2 dès que possible. Cette mise à jour corrige plusieurs problèmes de sécurité et de stabilité. Contactez votre référent en cas de question. »*

Aucun identifiant de vulnérabilité. Aucune version affectée précisée. Aucun vecteur d'accès. Vous êtes en version 8.3.7. Le progiciel est accessible depuis le réseau interne uniquement, utilisé par onze personnes, et traite des données de paie.

**Questions.** (a) Quel est le statut de ce constat ? (b) Quelles informations manquent, et par quel moyen les obtenir ? (c) Que faites-vous ce vendredi soir ? (d) Quelle est la décision par défaut si vous n'obtenez aucune réponse avant lundi ?

**Corrigé commenté**

**(a) Statut : hypothèse probable.** Le fait qu'un correctif de sécurité existe est vérifié — l'éditeur le dit. Que vous soyez affecté est probable, puisque votre version est antérieure, mais non confirmé faute de liste de versions affectées. La gravité réelle est une piste exploratoire : « importante » est un qualificatif commercial, pas une évaluation.

**(b) Cinq informations manquantes, et comment les obtenir :**

| Information | Moyen |
|---|---|
| Versions affectées, dont la 8.3.7 | Appel ou courriel au support, avec demande de réponse écrite |
| Vecteur d'accès : distant ou local, authentifié ou non | Même canal. C'est l'information la plus déterminante |
| Exploitation observée | Support, et vérification dans les sources d'exploitation avérée |
| Prérequis de la mise à jour, régressions connues | Notes de version, forum client |
| Existence d'une mesure de contournement | Support |

Le vecteur d'accès est celui qui change tout : une faille exploitable sans authentification depuis le réseau interne, sur une application traitant des données de paie, n'est pas du même ordre qu'une élévation de privilèges nécessitant un compte local.

**(c) Ce que vous faites vendredi soir — trois actions, vingt minutes :**

1. Enregistrer le constat dans la file unique, avec son statut, ce qui est connu et ce qui manque. Il existe désormais et ne dépend plus de votre mémoire.
2. Envoyer la demande écrite au support, avec les cinq questions. L'horodatage compte : il documente votre diligence.
3. Vérifier l'exposition réelle de l'application — qui peut l'atteindre, avec quels comptes. Cette vérification ne dépend d'aucune réponse de l'éditeur, et elle est souvent la plus informative.

Ce que vous ne faites **pas** : déployer la 8.4.2 en urgence un vendredi soir sur une application de paie, sans test ni fenêtre, sur la base d'un bulletin non qualifié. Le risque de régression est ici probablement supérieur au risque de la vulnérabilité — et cette comparaison est exactement le sujet du cas de synthèse C.

**(d) La décision par défaut, sans réponse avant lundi.** Traiter comme un constat de criticité moyenne sur un actif interne peu exposé : planification de la mise à jour dans la fenêtre normale suivante, avec test préalable. **Et** documenter que l'éditeur n'a pas répondu — c'est un élément d'évaluation fournisseur (§13.6), et un argument pour la prochaine renégociation.

**Les deux erreurs attendues.** Ne rien faire au motif que le bulletin est trop vague — le constat disparaît alors dans une boîte de réception. Ou déployer immédiatement en urgence — en transformant un risque incertain en indisponibilité certaine.

#### 14.11 🔴 FIL ROUGE — décembre 2026 : la matrice de couverture de veille

Claire Nadeau applique la matrice du §14.1 au périmètre élargi d'HELIOMED — parc interne, périmètre infogéré désormais mesurable (§13.9), usine, services en ligne et produits.

**Le résultat, en une page.**

| Domaine | Technologies distinctes | Couvertes par une source | Taux |
|---|---|---|---|
| Systèmes et bureautique | 14 | 14 | 100 % |
| Réseau et sécurité | 6 | 6 | 100 % |
| Bases de données et environnements d'exécution | 9 | 5 | 56 % |
| **Progiciels métier** | **7** | **2** | **29 %** |
| **Systèmes industriels (Saint-Étienne)** | **8** | **1** | **13 %** |
| Services en ligne | 38 | 4 | 11 % |
| Composants embarqués dans les produits HELIOMED | inconnu | — | **non mesuré** |

**Ce que le tableau démontre.** La veille d'HELIOMED était excellente là où elle était facile, et quasi inexistante là où les actifs sont les plus critiques. L'usine, dont les postes de supervision pilotent une ligne de production de dispositifs médicaux, était couverte à 13 %.

**Trois décisions prises.**

1. **Progiciels métier** : une clause de notification de vulnérabilité est ajoutée à chaque renouvellement de contrat de maintenance, en reprenant la clause 4 du §13.3. Cinq contrats sont concernés en 2027.
2. **Systèmes industriels** : Thomas Berger obtient un accès nominatif au portail sécurité de deux constructeurs — accès qui existait depuis toujours, sans que personne n'ait fait la demande. Pour les trois automates dont le fournisseur a disparu, la couverture est déclarée **impossible**, et la compensation est portée au chapitre 29.
3. **Services en ligne** : la veille éditeur n'est pas mise en place pour les 38 abonnements — ce serait ingérable. Elle l'est pour les 4 traitant des données sensibles ou disposant d'un connecteur vers la messagerie. Les 34 autres sont couverts par une revue annuelle de configuration (chapitre 31).

**Ce que Claire ne fait pas**, et qu'elle explique au comité : chercher à atteindre 100 % partout. La matrice sert à choisir où investir, pas à produire un objectif de complétude. La ligne « composants embarqués : non mesuré » restera telle quelle jusqu'au chapitre 25.

**Livrable de l'épisode.** La matrice de couverture de veille, avec son indicateur associé — *part des technologies de classe C1 couvertes par au moins une source identifiée* — qui entre au tableau de bord du comité MCS.

→ La suite en 🔴 §15.13, quand le premier scan authentifié complet fera perdre trois semaines à l'équipe.

→ **Chapitre 15 — Détection technique de l'exposition** : savoir s'il vous concerne, et pourquoi les outils se trompent si souvent.

#### Synthèse mentale du chapitre 14

La veille se construit à partir de l'inventaire, jamais l'inverse : la matrice de couverture révèle immédiatement les technologies sans source, qui sont presque toujours les progiciels métier, l'industriel et les services en ligne — c'est-à-dire des actifs critiques. Le MCS ne se réduit pas aux vulnérabilités identifiées : une quinzaine d'origines produisent des constats, dont la majorité n'a aucun identifiant, et la décision d'organisation la plus rentable du cours consiste à les faire toutes entrer dans une file unique avec la même priorisation. L'architecture de veille tient en trois étages complémentaires — vérité produit, couverture, signal d'exploitation — dont aucun ne remplace les autres. Dans le rapprochement automatique, le faux négatif est le vrai danger, d'où la règle d'archiver plutôt que supprimer ce qui est écarté. Qualifier chaque constat en fait vérifié, hypothèse probable ou piste exploratoire change radicalement la qualité des décisions et la crédibilité des remontées. Enfin, une veille reposant sur une seule personne fonctionne parfaitement jusqu'au mois d'août.

**Trois questions de vérification**

1. Votre flux de veille est abondant et vous êtes informé quotidiennement. Comment vérifiez-vous que cette abondance ne masque pas des angles morts, et par quel indicateur ?
2. Un rapport de test d'intrusion signale une interface d'administration exposée. Pourquoi ce constat progresse-t-il souvent moins vite qu'une vulnérabilité mineure de bibliothèque, et quelle décision d'organisation corrige cela ?
3. Vous recevez un bulletin sans identifiant, sans versions affectées et sans vecteur d'accès. Quelle est la seule information à obtenir en priorité, et pourquoi celle-là ?

---

### Chapitre 15 — Détection technique de l'exposition

Le chapitre 14 vous informe qu'une vulnérabilité existe. Celui-ci répond à la question suivante : **est-elle présente chez moi, et où exactement ?** C'est le chapitre des outils — et surtout de ce qu'ils ne savent pas faire.

#### 15.1 Les familles d'outils et ce que chacune peut savoir

| Famille | Principe | Ce qu'elle peut établir | Ce qu'elle ne peut pas |
|---|---|---|---|
| **Scan réseau non authentifié** | Interroge les services exposés depuis le réseau | Ce qui répond, bannières, comportements observables | L'état interne de la machine |
| **Scan authentifié** | Se connecte avec un compte et inventorie | Versions exactes, correctifs installés, configuration | Ce qui n'est pas accessible au compte utilisé |
| **Agent installé** | Programme résident qui remonte l'état en continu | État permanent, y compris hors réseau | L'état des machines sans agent |
| **Analyse de composition logicielle** | Lit les dépendances déclarées d'une application | Composants tiers et versions | L'atteignabilité réelle du code (§11.6) |
| **Analyse d'image de conteneur** | Inspecte les couches d'une image | Composants embarqués avant déploiement | Ce qui est ajouté à l'exécution |
| **Découverte externe** | Vue depuis Internet | La surface réellement publiée (ch. 11) | Tout l'interne |
| **Validation d'exploitabilité** | Tente une exploitation contrôlée | La démonstration qu'un chemin fonctionne | Le reste du parc, et le risque de l'essai |

**Le principe de complémentarité, à retenir.** Ces familles ne se substituent pas. Un agent ne dit rien de l'exposition réseau ; un scan externe ne dit rien de l'état interne ; une analyse de composition ne voit pas ce que le système d'exploitation embarque. Une organisation qui n'utilise qu'une famille a nécessairement un angle mort structurel, et il est prévisible.

#### 15.2 Ce qu'un scan non authentifié ne peut pas savoir

Le scan non authentifié observe un système de l'extérieur, sans identifiants. Il en déduit des informations à partir de ce que les services exposés laissent voir.

**Sa méthode d'inférence, et sa fragilité.** Il lit une bannière annonçant une version, observe un comportement caractéristique, teste une réponse. Puis il conclut à partir d'une base de correspondance version ↔ vulnérabilité.

**Les quatre sources de faux positifs structurels** :

| Cause | Mécanisme |
|---|---|
| **Rétroportage** | La bannière annonce une version amont ancienne, le correctif est présent (§2.2). C'est la première cause, et de loin |
| **Bannière modifiée** | Certaines configurations masquent ou falsifient la version annoncée |
| **Composant présent mais désactivé** | Le module vulnérable est installé, non chargé |
| **Correspondance approximative** | Le produit détecté n'est pas exactement celui de la base (§4.3) |

**Ce qu'il détecte que rien d'autre ne détecte**, et qui justifie son usage malgré tout : ce qui est **réellement joignable**. Un scan authentifié vous dira qu'un service est installé ; seul un scan non authentifié depuis un point donné du réseau vous dira qu'il répond depuis cet endroit. C'est une information d'exposition (chapitre 11), pas de vulnérabilité — et c'est sa vraie valeur.

#### 15.3 Le scan authentifié, et la protection de ses secrets

Le scan authentifié se connecte à la machine avec un compte et lit directement l'état du système : paquets installés, révisions, correctifs, configuration. Il est **incomparablement plus fiable** et devrait constituer le mode par défaut sur tout le parc que vous administrez.

**Le compte de scan est un actif de niveau 0.** Il dispose d'un accès en lecture privilégié sur l'ensemble du parc, et ses identifiants sont stockés dans l'outil de scan. Quiconque compromet cet outil obtient un accès à tout le périmètre scanné.

✅ **BONNE PRATIQUE (P0) — les six règles du compte de scan**

1. Un compte **dédié**, jamais un compte d'administration existant réutilisé.
2. Les **privilèges minimaux** nécessaires à la lecture — pas d'administration complète quand la lecture suffit.
3. **Interdiction d'ouverture de session interactive** pour ce compte.
4. **Rotation** régulière du secret, et vérification que la rotation est bien répercutée dans l'outil (§24.10).
5. **Surveillance** de son usage : toute utilisation en dehors des fenêtres de scan est une alerte.
6. **Cloisonnement** : idéalement, un compte distinct par zone de sécurité, pour qu'une compromission ne donne pas tout le parc.

#### 15.4 La sécurité de l'outil lui-même

Prolongement direct du point précédent, et l'un des angles morts les plus fréquents.

Un outil de scan de vulnérabilités concentre : les identifiants privilégiés du §15.3, la **cartographie complète** de vos faiblesses, et souvent une capacité d'exécution à distance. C'est un actif de niveau 0 au sens du §11.7, et il est fréquemment traité comme un outil secondaire — installé une fois, rarement mis à jour, avec une interface d'administration accessible largement.

⚠️ **PIÈGE — la console de sécurité oubliée**
Le raisonnement implicite est toujours le même : « c'est un outil de sécurité, donc il est sécurisé ». Il n'y a aucun lien logique entre les deux. Les outils de sécurité — scanners, consoles de protection des postes, plateformes de journalisation, consoles de sauvegarde — figurent régulièrement parmi les composants les plus en retard d'un parc. Le chapitre 34 leur est consacré.

#### 15.5 La fraîcheur de la base de détection

Un scanner ne détecte que ce qu'il sait détecter. Entre la publication d'un avis et la disponibilité du contrôle correspondant dans votre outil, il s'écoule un délai.

**Trois délais s'additionnent**, et c'est leur somme qui compte :

```
Publication de l'avis
   → l'éditeur de l'outil développe le contrôle          (heures à jours)
   → il le publie dans sa base                            (selon son rythme)
   → vous mettez à jour votre instance                    (selon VOTRE processus)
   → le prochain scan passe                               (selon votre cadence)
```

Le troisième délai est le seul que vous contrôlez entièrement, et c'est souvent le plus long. Une instance dont la base de détection date de trois semaines ne détectera aucune des vulnérabilités publiées depuis.

✅ **BONNE PRATIQUE (P0)** — Suivez la fraîcheur de la base de détection comme un indicateur à part entière, et rendez sa mise à jour automatique. C'est exactement le sujet du §1.3, ligne « contenu de détection » : votre outil de détection est lui-même un objet qui se dégrade quotidiennement.

⚠️ Pour toute vulnérabilité en crise (chapitre 21), **ne présumez jamais** que votre scanner la détecte. Vérifiez que le contrôle existe dans votre base, à sa version installée. Sinon, la vérification se fait autrement : requête sur l'inventaire par version, ou vérification directe sur un échantillon.

#### 15.6 La couverture réelle : la calculer et la prouver

Le §10.11 a posé le principe ; voici la mise en œuvre.

**La formule**, qui suppose le périmètre de référence du chapitre 10 :

```
Couverture de scan = actifs scannés avec succès / actifs du périmètre de référence
```

**Les cinq populations à distinguer**, parce que les confondre produit la totalité des malentendus sur ce chiffre :

| Population | Signification | Traitement |
|---|---|---|
| Scannés avec succès, authentifiés | Donnée fiable | Base des indicateurs |
| Scannés, mais authentification échouée | Donnée dégradée, faux positifs probables | À corriger en priorité : compte, droits, filtrage |
| Non joignables au moment du scan | Éteints, nomades, intermittents | **À lister explicitement**, jamais à ignorer |
| Exclus volontairement | Systèmes industriels, actifs fragiles | Exclusion **documentée**, avec son motif et sa compensation |
| Hors périmètre de l'outil | Cloud, services en ligne, produits | Couverts par un autre moyen, ou déclarés non couverts |

⚠️ **PIÈGE — l'exclusion silencieuse**
Le mécanisme le plus insidieux de tout ce chapitre. Un actif provoque des dysfonctionnements pendant un scan ; on l'exclut « temporairement » ; l'exclusion n'est jamais revue. Deux ans plus tard, il ne figure plus dans aucun rapport — et comme il ne remonte aucune vulnérabilité, il améliore même les indicateurs.
**Le garde-fou** : la liste des exclusions est un document de gouvernance, revu au comité MCS, avec pour chacune un motif, un propriétaire, une compensation et une date de revue. Une exclusion sans date de revue est une dérogation déguisée qui échappe au processus du §7.4.

#### 15.7 Identifiants d'actifs, historique et continuité

Un problème banal qui détruit silencieusement toute capacité de mesure dans la durée.

Les outils identifient les actifs par une clé interne, construite à partir du nom, de l'adresse, d'un identifiant matériel ou d'une combinaison. Quand cette clé change — machine renommée, redéploiement, changement d'adresse, réinstallation d'agent — l'outil crée un **nouvel actif** et perd l'historique de l'ancien.

**Les conséquences concrètes :**

- l'ancienneté d'un constat est réinitialisée, ce qui embellit artificiellement l'indicateur d'âge du *backlog* ;
- le nombre d'actifs augmente sans que le parc change, faussant tous les dénominateurs ;
- l'ancien actif reste dans l'outil, sans être scanné, et finit par disparaître des rapports ;
- une vulnérabilité récurrente (§17.9) apparaît comme nouvelle à chaque redéploiement.

✅ **BONNE PRATIQUE (P1)** — Définissez une règle d'identification stable, réconciliée avec l'inventaire du chapitre 10, et suivez deux indicateurs simples : le nombre d'actifs créés et supprimés dans l'outil par mois, et le nombre d'actifs présents dans l'outil mais absents du périmètre de référence. Une variation anormale de l'un ou de l'autre signale un problème d'identification, pas un changement de parc.

#### 15.8 ⚠️ « Non détecté », « non vulnérable », « non scanné »

C'est la distinction la plus coûteuse du domaine quand elle n'est pas faite, et elle mérite d'être affichée dans les bureaux.

| Formulation | Ce que ça signifie vraiment |
|---|---|
| **Non vulnérable** | L'outil a examiné cet actif et a établi qu'il n'est pas affecté. **Information positive.** |
| **Non détecté** | L'outil a examiné l'actif et n'a rien trouvé — ce qui peut vouloir dire qu'il ne sait pas chercher cela. **Absence d'information.** |
| **Non scanné** | L'outil n'a pas examiné l'actif : injoignable, authentification échouée, exclu, hors périmètre. **Absence totale d'information.** |

**Les trois se présentent identiquement dans un rapport** : la ligne est vide, l'actif n'apparaît pas dans la liste des vulnérables. Un tableau de bord qui ne les distingue pas transforme une absence d'information en information rassurante.

🧪 **EN PRATIQUE — les trois questions à poser devant tout rapport de scan**

1. Combien d'actifs du **périmètre de référence** ce rapport couvre-t-il ?
2. Parmi eux, combien ont été scannés **avec authentification réussie** ?
3. Où est la liste des actifs **non scannés**, avec le motif ?

Un rapport qui ne permet pas de répondre à ces trois questions n'est pas exploitable pour piloter, et il n'a aucune valeur probante en audit (§5.6).

#### 15.9 Cas particuliers par type d'environnement

| Environnement | Contrainte | Approche recommandée |
|---|---|---|
| **Systèmes industriels** | Le scan actif peut provoquer un défaut (§3.7) | Écoute passive du trafic, extraction depuis les outils d'ingénierie, inventaire manuel assumé (ch. 29) |
| **Équipements réseau et de sécurité** | Peu ou pas d'accès pour un scan authentifié | Inventaire de versions par requête d'administration, corrélation avec les avis constructeurs |
| **Hyperviseurs et appliances** | Accès restreint par l'éditeur | Interface de gestion, versions déclarées, avis fournisseur |
| **Conteneurs** | Éphémères, l'exécution n'est pas le bon moment | Analyse à la construction et dans le registre, pas sur les conteneurs en cours d'exécution |
| **Cloud** | Le scan réseau classique ne voit pas la configuration | Interrogation des interfaces du fournisseur, contrôle de posture (ch. 30) |
| **Postes nomades** | Rarement présents au moment du scan | Agent, obligatoirement — un scan réseau les manquera systématiquement |
| **Services en ligne** | Aucun accès technique | Revue de configuration, déclarations du fournisseur (ch. 31) |

⚠️ **PIÈGE — la saturation des cibles**
Un scan agressif peut dégrader ou faire tomber des services fragiles : équipements anciens, imprimantes, systèmes embarqués, applications à ressources limitées. La règle est de **calibrer l'intensité par zone** et de tester sur un échantillon avant de généraliser. Un scan qui provoque un incident coûte bien plus que sa valeur informative — et il produit surtout un refus durable des équipes, qui vous fermera l'accès pendant des années.

#### 15.10 Interpréter un rapport : les sept réflexes

| # | Réflexe | Ce qu'il évite |
|---|---|---|
| 1 | Vérifier le périmètre et le taux d'authentification avant tout | Raisonner sur un échantillon inconnu |
| 2 | Contrôler la révision éditeur avant de conclure sur une version | Le faux positif de rétroportage (§2.2) |
| 3 | Vérifier si le composant est **activé** | Traiter des services installés mais désactivés |
| 4 | Distinguer sévérité **héritée** de la base et sévérité contextuelle | Prioriser sur un score sans exposition (§4.10) |
| 5 | Repérer les doublons : même constat, plusieurs entrées | Compter plusieurs fois le même travail |
| 6 | Identifier les constats **déjà corrigés par l'éditeur** mais non redétectés | Rouvrir un sujet clos |
| 7 | Chercher ce qui **manque** : machines absentes du rapport | La fausse assurance du §15.8 |

#### 15.11 ⚠️ Les dix faux positifs les plus coûteux en temps

| # | Faux positif | Comment le lever |
|---|---|---|
| 1 | Rétroportage non pris en compte | Comparer la révision de l'éditeur, consulter l'avis de la distribution |
| 2 | Service installé mais désactivé | Vérifier l'état d'activation |
| 3 | Composant présent mais non chargé par l'application | Analyse d'atteignabilité (§11.6), déclaration du fournisseur |
| 4 | Bannière modifiée ou générique | Scan authentifié |
| 5 | Correspondance produit erronée | Vérifier le produit réel, corriger la table de correspondance |
| 6 | Vulnérabilité affectant une configuration non utilisée | Lire les conditions d'exploitation dans l'avis |
| 7 | Détection sur un appareil qui n'est pas le vôtre (adresse réattribuée) | Réconcilier avec l'inventaire |
| 8 | Constat sur une image de base, déjà corrigé dans l'image dérivée | Analyser l'image finale, pas seulement la base |
| 9 | Doublon entre agent et scan réseau | Règle de déduplication par identifiant pivot |
| 10 | Constat sur un actif décommissionné mais toujours présent dans l'outil | Nettoyage périodique, réconciliation d'inventaire |

📌 **La leçon transversale.** Ces dix causes n'ont presque rien à voir avec la qualité de l'outil. Elles viennent de l'écart entre ce qu'un outil peut observer et ce qu'est réellement votre système. Changer d'outil n'en supprime aucune ; améliorer l'inventaire et la vérification en supprime la majorité.

#### 15.12 📌 Limites et coûts réels

| Dimension | Ce à quoi s'attendre |
|---|---|
| **Modèle de licence** | Le plus souvent par actif, ou par volume analysé. Le coût croît avec la découverte — inventorier mieux augmente la facture, ce qui crée une incitation perverse à ne pas chercher |
| **Charge d'exploitation** | L'outil demande du temps : maintien des comptes, des exclusions, des correspondances, traitement des échecs d'authentification |
| **Dépendance éditeur** | Les données historiques sont rarement portables. Un changement d'outil fait perdre l'antériorité, donc la démonstration de progrès |
| **Qualité du reporting** | Très inégale. Beaucoup d'outils rendent difficile le calcul honnête du §15.6, précisément parce qu'il n'est pas flatteur |
| **Périmètre non couvert** | Systèmes industriels, services en ligne, composants embarqués, produits — c'est-à-dire une part importante du périmètre réel |

✅ **BONNE PRATIQUE (P1)** — Exigez, dès l'évaluation d'un outil, la capacité d'**exporter les données brutes** et l'historique dans un format ouvert. C'est ce qui vous permettra de calculer vos propres indicateurs (chapitre 38), de constituer une preuve indépendante de l'outil (§5.6), et de changer de fournisseur sans repartir de zéro.

#### 15.13 🔴 FIL ROUGE — janvier 2027 : trois semaines perdues

Le premier scan authentifié couvrant l'ensemble du périmètre élargi d'HELIOMED remonte, parmi 3 800 constats, une vulnérabilité critique sur une bibliothèque de chiffrement présente sur **42 serveurs** de classe C1 et C2.

Malik Ferhaoui lance la campagne de correction. Elle prend trois semaines : planification, fenêtres, tests, déploiement en anneaux, vérification. Le travail est bien fait.

**Le problème.** À la fin de la campagne, un contrôle de routine sur trois serveurs révèle que la version installée **avant** la campagne contenait déjà le correctif. La distribution avait rétroporté la correction six mois plus tôt ; le numéro de version amont, lui, n'avait pas bougé. Les 42 serveurs n'ont jamais été vulnérables.

**Ce que coûte l'erreur.** Trois semaines de deux personnes, six fenêtres de maintenance consommées, deux redémarrages de serveurs de production hors nécessité — et, plus grave, une régression mineure sur une application métier lors de la montée de version, qui a occupé l'équipe applicative pendant deux jours.

**La cause racine, et elle n'est pas technique.** Le réflexe n° 2 du §15.10 n'était écrit nulle part. Malik connaissait le mécanisme du rétroportage — il l'avait lu — mais rien dans le processus ne l'obligeait à vérifier avant de lancer une campagne de 42 serveurs.

**Les trois mesures prises.**

1. **Un point de contrôle obligatoire** dans le processus : toute campagne portant sur plus de dix actifs exige une vérification préalable sur **trois actifs représentatifs**, avec preuve jointe au dossier de campagne. Coût : trente minutes. Le pilote du chapitre 18 est né de cet incident.
2. **Une règle de qualification** : un constat issu d'un scan sur système à support long reste au statut *piste exploratoire* (§14.7) tant que la révision éditeur n'est pas vérifiée. Il ne peut pas déclencher de campagne à ce statut.
3. **Un signalement à l'éditeur de l'outil**, avec demande de prise en compte des révisions de distribution. Réponse reçue : la fonctionnalité existe et n'était pas activée sur leur instance. Elle l'est depuis.

**Ce que Claire Nadeau retient**, et qu'elle formule au comité en une phrase que l'équipe reprendra ensuite : *le coût d'un faux positif n'est pas le temps perdu à l'analyser, c'est le travail inutile qu'il déclenche quand personne ne l'analyse.*

**Livrable de l'épisode.** Le point de contrôle des trois actifs représentatifs, intégré au dossier de campagne standard — il figure en Annexe L.

→ La suite en 🔴 §16.11, quand il faudra prioriser les 3 800 constats restants.

→ **Chapitre 16 — Triage et priorisation défendables** : décider quoi traiter, et pourquoi un seuil de gravité ne suffit pas.

#### Synthèse mentale du chapitre 15

Les familles d'outils ne se substituent pas : un agent ignore l'exposition réseau, un scan externe ignore l'état interne, une analyse de composition ignore ce que le système embarque — n'en utiliser qu'une crée un angle mort prévisible. Le scan non authentifié produit du faux positif structurel, mais il est le seul à établir ce qui est réellement joignable depuis un point donné. Le compte de scan et l'outil lui-même sont des actifs de niveau 0, et ils comptent régulièrement parmi les composants les plus en retard d'un parc. La fraîcheur de la base de détection est un objet qui se dégrade quotidiennement, et le délai que vous contrôlez est souvent le plus long. La couverture se calcule sur le périmètre de référence, en distinguant cinq populations, dont les exclusions — qui sont des dérogations déguisées si elles n'ont ni motif, ni propriétaire, ni date de revue. Enfin, « non vulnérable », « non détecté » et « non scanné » se présentent identiquement dans un rapport et signifient trois choses radicalement différentes : les confondre transforme une absence d'information en information rassurante.

**Trois questions de vérification**

1. Un rapport indique 0 vulnérabilité critique sur un ensemble de serveurs. Quelles trois questions posez-vous avant d'en tirer la moindre conclusion ?
2. Pourquoi le compte utilisé par votre scanner mérite-t-il un traitement de niveau 0, et quelles règles lui appliquez-vous ?
3. Une machine provoque un incident pendant un scan et vous l'excluez. Que devez-vous produire au même moment pour que cette exclusion ne devienne pas un angle mort permanent ?

---

### Chapitre 16 — Triage et priorisation défendables

#### 16.1 Pourquoi « tout ce qui dépasse 7 » ne fonctionne pas

Commençons par la démonstration chiffrée, parce que l'argument théorique ne convainc personne tant que les nombres ne sont pas posés.

**Le point de départ.** Un parc de taille intermédiaire produit, lors d'un premier scan authentifié complet, de l'ordre de plusieurs milliers de constats. Reprenons les chiffres du fil rouge : 4 312 constats, dont 1 176 de gravité supérieure ou égale à 7.

**Le calcul de capacité.** Comptez vingt minutes par constat — qualification, recherche du correctif, planification, suivi, vérification. C'est une estimation basse pour un constat non trivial.

```
1 176 constats × 20 min            = 392 heures
392 h / 2 personnes                = 196 h par personne
196 h à ~75 h disponibles par mois ≈ 2,6 mois de traitement
```

Deux mois et demi pour résorber le stock initial : à ce stade, la situation paraît tenable. **C'est le flux qui la rend impossible.**

**Le calcul qui compte est celui du régime permanent.** Un parc de cette taille produit typiquement 250 à 400 nouveaux constats par mois, dont une proportion comparable dépasse le seuil de gravité retenu — soit environ 70 à 110 constats mensuels à traiter selon cette règle.

```
90 nouveaux constats/mois × 20 min   ≈ 30 h/mois
Capacité disponible                   ≈ 150 h/mois pour deux personnes
Reste pour le stock initial           ≈ 120 h/mois
392 h de stock / 120 h                ≈ 3,3 mois
```

**Sur le papier, cela passe.** Dans la réalité, deux hypothèses de ce calcul sont fausses :

- Les 75 heures mensuelles supposent que la moitié du temps est consacrée au MCS. La mesure du §37.9 donne un ordre de grandeur bien plus faible une fois déduits l'exploitation courante, les changements, les incidents et les astreintes.
- Les 20 minutes par constat ne couvrent que le triage. Elles n'incluent ni la planification, ni la fenêtre, ni le déploiement, ni la vérification, ni la preuve — c'est-à-dire l'essentiel de la charge réelle (§37.9).

Avec des hypothèses réalistes, le stock ne se résorbe pas : il se stabilise à un niveau élevé, ou il croît. **Et c'est le meilleur des cas**, celui où le flux est régulier : une campagne d'exploitation sur un produit très déployé peut ajouter plusieurs centaines de constats en une semaine.

**Le second problème, plus grave que le premier.** Cette méthode ne se contente pas de produire trop de travail : elle produit le **mauvais** travail. Elle écarte des constats réellement dangereux — la vulnérabilité de gravité 5,9 activement exploitée sur une interface d'administration exposée du fil rouge — et inclut des milliers de constats qui ne seront jamais exploités. Elle est simultanément trop large et trop étroite.

**La conclusion, qui structure tout le chapitre.** Le seuil de gravité seul échoue parce qu'il utilise **une seule des cinq informations** nécessaires à une décision. Il connaît la gravité technique ; il ignore l'exploitation observée, l'exposition, la criticité métier et l'effort de correction.

#### 16.2 Construire une fonction de priorisation

**Les cinq entrées**, et ce que chacune apporte :

| Entrée | Question | Source | Qui la détient |
|---|---|---|---|
| **Gravité technique** | Quels dégâts si c'est exploité ? | Score de gravité (§4.4) | Externe |
| **Exploitation** | Est-ce utilisé par des attaquants ? | Catalogue d'exploitation avérée, renseignement (§4.6) | Externe |
| **Probabilité** | Est-ce susceptible de l'être ? | Modèle de prédiction (§4.5) | Externe |
| **Exposition** | Est-ce atteignable, et par qui ? | Votre cartographie (ch. 11) | **Vous seul** |
| **Criticité** | Que vaut cet actif pour l'organisation ? | Votre inventaire (ch. 10) | **Vous seul** |

Une sixième entrée intervient à l'arbitrage, sans entrer dans l'évaluation du risque : l'**effort de correction**. Elle ne change pas la priorité d'un constat, elle change l'ordre dans lequel on traite des constats de priorité comparable — et elle justifie de regrouper (§16.7).

⚠️ **PIÈGE — la formule pondérée**
La tentation est forte de construire un score unique en pondérant les cinq entrées. C'est une mauvaise idée pour trois raisons : les pondérations sont arbitraires et indéfendables en audit ; un score composite masque le raisonnement au lieu de l'expliciter ; et une entrée manquante — cas fréquent depuis la fragmentation de l'écosystème (§4.9) — rend le score incalculable au lieu de simplement dégrader la décision. **Préférez un arbre de décision** : il produit une action, il se lit, il se discute, et il fonctionne même avec une information incomplète.

🖼 **SCHÉMA — Arbre de décision de triage.** *Arbre à six nœuds de décision et cinq feuilles colorées par urgence. C'est le visuel le plus utilisé du cours : à soigner particulièrement.*

#### 16.3 L'arbre de décision opérationnel

Voici un arbre utilisable tel quel, à calibrer sur vos classes de service (§7.2).

```
① La vulnérabilité est-elle activement exploitée ?
   ├─ OUI ─→ ② L'actif est-il joignable depuis Internet ?
   │          ├─ OUI ─→ ████ AGIR EN URGENCE  (72 h, hors fenêtre autorisée)
   │          └─ NON ─→ ③ L'actif est-il de niveau 0 ou critique métier ?
   │                     ├─ OUI ─→ ███ TRAITER EN PRIORITÉ  (7 j)
   │                     └─ NON ─→ ██ TRAITER  (30 j)
   └─ NON ─→ ④ Probabilité d'exploitation élevée OU gravité critique ?
              ├─ OUI ─→ ⑤ Exposé ou actif critique ?
              │          ├─ OUI ─→ ██ TRAITER  (30 j)
              │          └─ NON ─→ █ PLANIFIER  (prochaine campagne)
              └─ NON ─→ ⑥ Corrigeable dans une campagne groupée ?
                         ├─ OUI ─→ █ PLANIFIER  (campagne trimestrielle)
                         └─ NON ─→ ░ SURVEILLER  (revue semestrielle)
```

**Les quatre propriétés qui en font un bon outil**, et qu'un score composite n'a pas :

1. **Il produit une action**, pas un nombre : chaque feuille correspond à un délai et à un mode de traitement.
2. **Il est auditable.** En cas de contestation, on ne discute pas d'une pondération, on relit le chemin parcouru : « exploitation non observée, non exposé, actif non critique ». C'est vérifiable.
3. **Il tolère l'information manquante.** Si la probabilité d'exploitation n'est pas disponible pour ce constat, la question ④ se résout sur la gravité seule. La décision est dégradée, pas bloquée.
4. **Il place les deux informations que vous seul détenez au cœur du raisonnement** : l'exposition et la criticité apparaissent à trois nœuds sur six.

✅ **BONNE PRATIQUE (P0)** — Écrivez votre arbre, faites-le valider en comité MCS, et **datez-le**. C'est le document que vous produirez le jour où l'on vous demandera pourquoi tel constat n'a pas été traité en priorité. Un arbre validé et appliqué est une défense solide ; une décision au cas par cas ne l'est pas.

#### 16.4 Exploitabilité contextuelle

Le §11.6 a posé la notion. Trois vérifications rapides, à faire avant d'engager toute campagne, retirent une part significative du volume :

| Vérification | Durée | Question |
|---|---|---|
| **Activation** | 1 minute | Le service ou module vulnérable est-il actif sur cet actif ? |
| **Configuration requise** | 5 minutes | L'avis mentionne-t-il une condition — option activée, mode particulier — que vous n'avez pas ? |
| **Atteignabilité du code** | Variable | La fonction vulnérable est-elle appelable ? (déclaration du fournisseur, analyse) |

**Le résultat de ces vérifications ne clôt pas le constat**, il le **dépriorise avec justification** — nuance essentielle traitée au §16.6 et au chapitre 17. La distinction est ce qui vous protège le jour où la configuration change et où le service désactivé est réactivé par un autre projet.

#### 16.5 Fixer des délais tenables

Les délais des classes de service (§7.2) doivent satisfaire trois contraintes simultanées, et c'est leur conjonction qui est difficile.

| Contrainte | Question |
|---|---|
| **Cohérence avec le risque** | Un délai de 30 jours sur un actif exposé portant une vulnérabilité exploitée est indéfendable |
| **Tenabilité** | Un délai que vous ne tenez pas produit une non-conformité permanente (§7.2) |
| **Justifiabilité** | Vous devez pouvoir expliquer d'où viennent ces chiffres |

**Sur le troisième point**, trois sources de justification acceptables : les délais imposés par un référentiel qui vous est applicable (chapitre 8) ; les délais issus d'un modèle méthodologique public reconnu, en le citant comme référence et non comme obligation (§8.7) ; ou votre propre calibrage documenté, fondé sur une mesure de votre capacité réelle. La troisième est parfaitement recevable — à condition d'être écrite.

**La méthode de calibrage par la capacité**, qui produit des chiffres tenables :

```
1. Mesurez le volume mensuel réel de constats atteignant chaque feuille de l'arbre
2. Mesurez le temps réellement consommé par constat, par catégorie
3. Confrontez à la capacité disponible
4. Ajustez soit les délais, soit la capacité — jamais l'affichage seul
```

L'étape 4 est un arbitrage de direction, pas une décision technique. Si la capacité ne permet pas des délais cohérents avec le risque, c'est un **constat à remonter** au comité stratégique (§9.3), avec les trois options du chapitre 12 : plus de moyens, moins de périmètre, ou plus de risque accepté.

#### 16.6 La dépriorisation défendable

Décider de ne pas traiter maintenant est une décision normale et fréquente. Ce qui la rend acceptable, c'est sa **traçabilité**.

**Les quatre motifs légitimes**, avec ce qui doit être écrit pour chacun :

| Motif | À documenter | Risque associé |
|---|---|---|
| Non atteignable dans votre contexte | Le fait vérifié qui l'établit, et sa date | La configuration peut changer |
| Faible probabilité et exposition nulle | Les valeurs constatées et la date | Les deux peuvent évoluer |
| Correction groupée à venir | La campagne cible et sa date | La campagne peut glisser |
| Effort disproportionné au risque | La comparaison chiffrée | Jugement contestable |

⚠️ **PIÈGE — la dépriorisation qui devient un oubli**
Un constat déprioritisé sans **date de revue** disparaît. La règle est simple : toute dépriorisation porte une date de réexamen, et le réexamen est automatique — pas dépendant de la mémoire de quelqu'un. Les trois premiers motifs ci-dessus reposent sur un état du monde qui peut changer ; ils sont valables jusqu'à réexamen, pas définitivement.

**Dépriorisation ≠ clôture.** Un constat déprioritisé reste **ouvert** dans la file, avec une échéance repoussée. Un constat clos n'existe plus. Confondre les deux fait disparaître de votre pilotage la dette que vous venez d'accepter — et c'est ce que le chapitre 17 formalise.

#### 16.7 Traiter la volumétrie : penser en campagnes

Le triage réduit la file ; il ne la vide pas. Le second levier consiste à changer d'unité de travail.

**Raisonner par constat individuel est la source principale d'inefficacité.** Trois regroupements produisent des gains considérables :

| Regroupement | Principe | Gain typique |
|---|---|---|
| **Par correctif** | Un correctif cumulatif corrige souvent des dizaines de constats sur le même actif | Le travail est celui d'un correctif, pas de trente |
| **Par actif** | Traiter tous les constats d'un actif en une intervention | Une seule fenêtre, un seul test, un seul redémarrage |
| **Par montée de version** | Passer à une version supportée règle simultanément le présent et le futur | Supprime des constats à venir |

**Le changement de perspective à opérer**, et il est plus profond qu'il n'y paraît : *ne mesurez pas votre travail en nombre de vulnérabilités fermées, mesurez-le en nombre d'actifs ramenés à un état de référence.* Un actif à jour ne produit plus de constats. C'est aussi ce qui rend l'approche immuable du §3.5 si efficace : la cadence de reconstruction remplace des centaines de traitements individuels.

#### 16.8 ⏱ Reconstruire ce que l'on recevait gratuitement

*Bloc périssable, vérifié le 30/07/2026.*

La fragmentation de l'écosystème (§4.9) a une conséquence directe et concrète sur le triage : une part croissante des constats arrive **sans enrichissement** — sans score, sans correspondance produit fiable, parfois sans description exploitable.

**Les trois stratégies d'adaptation**, par ordre de robustesse :

| Stratégie | Principe | Effort |
|---|---|---|
| **Basculer le poids sur ce que vous détenez** | Faire porter la décision sur l'exposition et la criticité plutôt que sur le score reçu | Faible, et c'est déjà la bonne pratique |
| **Multiplier les sources** | Croiser plusieurs bases, dont une européenne, plus les avis éditeurs (§14.4) | Moyen |
| **Enrichir en interne** | Attribuer soi-même une gravité aux constats non enrichis, selon une grille écrite | Élevé, réservé aux actifs C1 |

**Le point encourageant**, et il vaut d'être souligné : une organisation qui a fait le travail des chapitres 10 et 11 est **beaucoup moins exposée** à cette fragmentation qu'une organisation qui dépendait entièrement d'un score externe. L'exposition et la criticité ne dépendent d'aucun fournisseur. C'est un argument de plus pour l'ordre de séquencement du §1.4.

#### 16.9 📌 Limites du triage

- **Le triage ne crée aucune capacité de remédiation.** Il permet de dépenser au bon endroit une capacité qui reste constante. Si votre capacité est structurellement insuffisante, le triage la rend visible, il ne la résout pas.
- **Le risque de sur-ingénierie est réel.** Un dispositif de triage sophistiqué peut consommer plus de temps que la correction elle-même. Si votre arbre nécessite plus de cinq minutes par constat, il est trop complexe.
- **Les entrées externes sont volatiles.** Un constat déprioritisé aujourd'hui peut devenir urgent demain, sans qu'aucune information interne ne change. D'où l'obligation de rejeu périodique (§16.6).
- **Le triage ne remplace pas la correction de fond.** Un parc dont les images de référence sont anciennes reproduira les mêmes constats indéfiniment. Le triage traite le symptôme.

#### 16.10 🔬 Mini-lab 4 — Construire une matrice de triage

**Objectif** — Appliquer l'arbre de décision et mesurer l'écart avec un tri par gravité.
**Durée** 40 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §16.3, §11.7, §7.2 · **Livrable** priorisation argumentée des 10 constats.
**Compétences validées** — ✔ appliquer un arbre de décision ✔ intégrer exposition et criticité au triage ✔ reconnaître un actif de niveau 0 ✔ déprioriser avec justification et date de revue

**Données fournies.** Vingt-cinq constats issus d'un scan. Extrait représentatif de dix d'entre eux :

| # | Gravité | Exploitation observée | Probabilité | Actif | Exposition | Criticité |
|---|---|---|---|---|---|---|
| 1 | 9,8 | Non | Faible | Serveur de test | Interne | C3 |
| 2 | 5,9 | **Oui** | Élevée | Passerelle d'accès distant | **Internet** | C1 |
| 3 | 8,1 | Non | Faible | Poste bureautique ×340 | Interne | C3 |
| 4 | 7,5 | Non | Moyenne | Contrôleur de domaine | Interne | **C1 — niveau 0** |
| 5 | 6,1 | **Oui** | Élevée | Automate de production | Réseau industriel isolé | C4 |
| 6 | 9,1 | Non | Faible | Bibliothèque, service désactivé | Interne | C2 |
| 7 | 4,3 | Non | Faible | Serveur de fichiers | Interne | C2 |
| 8 | 8,8 | Non | **Élevée** | Serveur web public | **Internet** | C1 |
| 9 | 7,2 | Non | Faible | Console de sauvegarde | Interne | **C1 — niveau 0** |
| 10 | 9,4 | Non | Moyenne | Hyperviseur | Réseau d'administration | **C1 — niveau 0** |

**Questions.** (a) Classez ces dix constats avec l'arbre du §16.3. (b) Classez-les par gravité décroissante. (c) Comparez les cinq premiers de chaque classement. (d) Quels constats méritent une vérification avant tout traitement ? (e) Le constat n° 5 relève d'une classe particulière : que faites-vous ?

**Corrigé commenté**

**(a) Classement par l'arbre :**

| Rang | # | Chemin dans l'arbre | Décision |
|---|---|---|---|
| 1 | **2** | Exploitée → exposée Internet | **AGIR EN URGENCE — 72 h** |
| 2 | **5** | Exploitée → non exposée → actif critique (C4) | **TRAITER EN PRIORITÉ — mais régime C4 : compensation** |
| 3 | **8** | Non exploitée → probabilité élevée → exposé | **TRAITER — 30 j** |
| 4 | **10** | Non exploitée → gravité critique → actif de niveau 0 | **TRAITER — 30 j** |
| 5 | **4** | Non exploitée → gravité critique → niveau 0 | **TRAITER — 30 j** |
| 6 | **9** | Non exploitée → gravité élevée → niveau 0 | TRAITER — 30 j |
| 7 | **3** | Non exploitée → gravité élevée → non exposé, C3 | PLANIFIER — campagne, mais volume : 340 postes |
| 8 | **1** | Non exploitée → gravité critique → non exposé, C3 | PLANIFIER |
| 9 | **6** | Service désactivé | **DÉPRIORISER avec justification et date de revue** |
| 10 | **7** | Faible partout | SURVEILLER |

**(b) Classement par gravité décroissante :** 1 (9,8) · 10 (9,4) · 6 (9,1) · 8 (8,8) · 3 (8,1) · 4 (7,5) · 9 (7,2) · 5 (6,1) · 2 (5,9) · 7 (4,3).

**(c) La comparaison, et c'est tout l'objet du lab.**

| Méthode | Cinq premiers |
|---|---|
| Arbre de décision | **2, 5, 8, 10, 4** |
| Gravité seule | **1, 10, 6, 8, 3** |

Deux constats seulement sont communs. Surtout : le tri par gravité place en **première position** le constat n° 1 — un serveur de test interne, non exposé, non exploité — et relègue en **avant-dernière** le n° 2, la seule vulnérabilité activement exploitée sur un actif publié sur Internet. Il place également en troisième position le n° 6, dont le service est désactivé.

**(d) Les vérifications préalables :** le n° 6 (état d'activation — déjà connu ici, à confirmer sur l'ensemble du parc), le n° 3 (340 postes : appliquer le point de contrôle des trois actifs représentatifs du §15.13), et le n° 1 (vérifier qu'il s'agit bien d'un serveur de test, et surtout **ce qu'il contient** — un serveur de test portant une copie de données de production n'est pas un actif C3, voir chapitre 28).

**(e) Le constat n° 5.** Vulnérabilité exploitée sur un automate en classe C4. Le régime applicable n'est pas la correction mais la **compensation sous 72 h** (§7.2) : vérifier l'isolation du réseau industriel, restreindre les accès, renforcer la surveillance, et planifier le correctif validé par le constructeur pour le prochain arrêt de production. La décision est écrite et signée par le propriétaire métier. C'est le chapitre 29.

**Les trois erreurs attendues.** Traiter le n° 5 comme un constat C1 et exiger une correction immédiate, ce qui est irréaliste et détruira la relation avec l'exploitant industriel. **Clore** le n° 6 au lieu de le dépriorer. Et sous-estimer le n° 3 en le voyant comme un constat unique alors qu'il représente 340 actifs, donc une campagne à part entière.

#### 16.11 🔴 FIL ROUGE — février 2027 : la refonte du triage, un an après

Un an après la première tentative (§4.11), Claire Nadeau et Malik Ferhaoui formalisent l'arbre de décision d'HELIOMED et mesurent l'effet sur les 3 800 constats du scan de janvier.

**Le résultat, en une page.**

| Feuille de l'arbre | Constats | Charge estimée |
|---|---|---|
| Agir en urgence — 72 h | 4 | 1 jour |
| Traiter en priorité — 7 j | 19 | 4 jours |
| Traiter — 30 j | 143 | 3 semaines |
| Planifier — campagne | 1 890 | **21 campagnes groupées**, dont 6 montées de version |
| Surveiller | 1 604 | Revue semestrielle |
| Déprioritisé avec justification | 140 | Réexamen trimestriel automatique |

**Ce qui change réellement.** Ce ne sont pas les 4 constats urgents — ils auraient été traités de toute façon. C'est la ligne « Planifier » : 1 890 constats deviennent **21 campagnes**, parce que le regroupement par correctif et par actif (§16.7) transforme des milliers de traitements individuels en quelques dizaines d'interventions. Six de ces campagnes sont des montées de version qui supprimeront aussi les constats à venir.

La charge annuelle estimée passe de « impossible » à « tenable avec deux personnes, à condition de ne pas ajouter de périmètre ». Ce dernier point est écrit noir sur blanc dans la note au comité.

**La décision la plus discutée.** Les 1 604 constats en surveillance représentent 42 % du total, et le représentant commercial demande si l'on peut « laisser 1 604 vulnérabilités ouvertes ». Claire répond en trois points : elles ne sont ni exploitées, ni exposées, ni sur des actifs critiques ; elles sont **suivies et réexaminées**, pas oubliées ; et la majorité disparaîtra sans traitement individuel lors des campagnes de montée de version. Le comité valide, et la formulation retenue au compte rendu est celle qui compte : *« 1 604 constats en surveillance active, réexamen semestriel, aucun sur actif exposé ou critique »*.

**Ce qui n'était pas prévu.** En appliquant l'arbre, deux constats atteignent la feuille « urgence » sur des actifs de l'infogérant — les premiers depuis que la restitution mensuelle de données fonctionne (§13.9). Le délai contractuel de 7 jours s'applique. C'est la première fois qu'HELIOMED peut opposer un délai à son prestataire sur une base documentée.

**Livrable de l'épisode.** L'arbre de décision d'HELIOMED, daté et validé en comité, et la matrice de triage figurant en Annexe C.

→ La suite en 🔴 §17.14, quand ces 21 campagnes devront être suivies sans se perdre.

→ **Chapitre 17 — Workflow de remédiation et gestion du *backlog*** : piloter le traitement entre la décision et la correction.

#### Synthèse mentale du chapitre 16

Un seuil de gravité échoue pour deux raisons cumulées : il produit un volume arithmétiquement intraitable, et il produit le mauvais travail — simultanément trop large et trop étroit. Cinq entrées sont nécessaires à une décision, dont deux que vous seul détenez : l'exposition et la criticité. Préférez un arbre de décision à un score composite, parce qu'il produit une action, se relit en audit, tolère l'information manquante et place au cœur du raisonnement ce que vous êtes seul à savoir. Trois vérifications de quelques minutes — activation, condition de configuration, atteignabilité — retirent une part importante du volume, mais elles déprioritisent, elles ne closent pas. Les délais se calibrent sur la capacité mesurée, et l'écart entre capacité et risque est un constat à remonter, pas à absorber. Enfin, le levier le plus puissant n'est pas le triage mais le changement d'unité de travail : ne comptez pas les vulnérabilités fermées, comptez les actifs ramenés à un état de référence.

**Trois questions de vérification**

1. Démontrez en quatre lignes de calcul pourquoi une règle « corriger tout ce qui dépasse 7 » est intenable sur un parc de 200 serveurs, puis expliquez pourquoi ce n'est pas le problème principal de cette règle.
2. Pourquoi un score composite pondéré est-il plus fragile qu'un arbre de décision, notamment depuis la fragmentation des sources de données ?
3. Un constat porte sur un service installé mais désactivé. Quelle est la bonne décision, en quoi diffère-t-elle d'une clôture, et que devez-vous prévoir pour que cette décision reste valable dans six mois ?

---

### Chapitre 17 — Workflow de remédiation et gestion du *backlog*

#### 17.1 Pourquoi la décision ne suffit pas

Le chapitre 16 a produit une décision pour chaque constat. Entre cette décision et la correction effective, il se passe des semaines — parfois des mois — pendant lesquelles le constat doit **exister quelque part**, avec un propriétaire, une échéance et un état.

C'est ce que la plupart des organisations ne font pas. Le triage est soigné, la correction est bien exécutée, et **entre les deux il n'y a qu'un tableur**. Les symptômes sont toujours les mêmes :

- personne ne sait combien de constats sont réellement en cours de traitement ;
- un même problème est traité deux fois par deux personnes différentes ;
- un constat affecté à quelqu'un qui a quitté l'entreprise n'est jamais réaffecté ;
- une vulnérabilité corrigée réapparaît trois mois plus tard sans que personne ne s'en étonne ;
- on ne peut pas répondre à la question « depuis combien de temps ce constat est-il ouvert ? ».

**Le principe de ce chapitre** : le constat est un **objet de gestion** avec un cycle de vie, pas une ligne dans un rapport. C'est ce cycle de vie qui rend le MCS pilotable, mesurable et démontrable.

#### 17.2 De la détection au ticket : agrégation et déduplication

Un scan produit des constats, pas des tickets. Créer un ticket par constat est une erreur qui noie l'organisation : 3 800 constats produiraient 3 800 tickets, dont personne ne ferait rien.

**La structure à adopter — le modèle parent / enfants :**

```
CONSTAT PARENT : « Vulnérabilité X dans le composant Y »
   ├─ Actif A  (version, état, échéance)
   ├─ Actif B
   ├─ … 42 actifs
   └─ Décision de triage, propriétaire, échéance : portés par le PARENT
```

Un ticket par **problème**, avec la liste des actifs concernés en pièces attachées. La décision, l'échéance et le propriétaire s'attachent au parent ; l'état d'avancement se mesure sur les enfants.

**Les quatre règles de déduplication**, qui évitent la majorité du bruit :

| Règle | Effet |
|---|---|
| Un même identifiant de vulnérabilité sur plusieurs actifs → **un** ticket parent | Divise le volume par un facteur important |
| Plusieurs constats corrigés par le **même correctif** → un ticket | Aligne le ticket sur l'unité de travail réelle |
| Constat remonté par deux outils différents → un ticket, deux sources | Évite le double traitement (§15.11, faux positif n° 9) |
| Constat réapparaissant sur un actif redéployé → **réouverture**, pas nouveau ticket | Préserve l'historique et révèle la récurrence (§17.9) |

⚠️ **PIÈGE — la déduplication trop agressive**
Regrouper des constats qui ne se corrigent pas de la même façon crée un ticket impossible à clore : il reste ouvert parce qu'un actif sur quarante-deux résiste. Le critère de regroupement doit être **l'action de correction**, pas la ressemblance du constat.

#### 17.3 Campagnes ou traitement à l'unité

Deux modes de travail coexistent, et les confondre coûte cher.

| Mode | Quand l'employer | Unité |
|---|---|---|
| **À l'unité** | Constats urgents, actifs de niveau 0, cas particuliers | Le constat parent |
| **En campagne** | Volume, correctifs cumulatifs, montées de version | Un lot d'actifs, une fenêtre, un objectif d'état |

**La campagne est un objet de gestion distinct**, avec ses propres attributs : périmètre d'actifs, objectif d'état cible, fenêtre, anneaux de déploiement, critères d'arrêt, propriétaire, plan de retour arrière. Elle **absorbe** un ensemble de tickets, qui se ferment collectivement à sa vérification.

✅ **BONNE PRATIQUE (P1)** — Un tableau de bord de MCS mature affiche **deux compteurs distincts** : les constats en traitement unitaire, et les campagnes en cours avec leur avancement. Mélanger les deux dans un unique décompte de vulnérabilités ouvertes produit un chiffre qui n'a aucun sens opérationnel.

#### 17.4 Propriétaires, refus d'affectation et constats orphelins

**L'affectation** relie le ticket au propriétaire technique de l'actif, issu de l'inventaire (§5.5 et §10.4). Si l'inventaire porte cette information, l'affectation est automatique — c'est l'un des bénéfices les plus concrets du travail des chapitres 5 et 10.

**Trois situations à traiter explicitement**, faute de quoi elles bloquent silencieusement la file :

| Situation | Traitement |
|---|---|
| **Aucun propriétaire** | Le constat porte sur un actif orphelin. Ce n'est pas un problème de remédiation, c'est un problème d'inventaire : il remonte au processus de désignation (§5.5), avec la procédure d'extinction programmée en dernier recours |
| **Refus d'affectation** | Le propriétaire estime que l'actif ne relève pas de lui. Délai de contestation borné — par exemple 5 jours ouvrés — puis arbitrage au comité. **Sans délai, le ticket reste en suspens indéfiniment** |
| **Propriétaire indisponible** | Départ, congé long, réorganisation. Règle de suppléance automatique, sinon le ticket vieillit sans que personne ne le sache |

🏢 **VU EN RÉUNION** — Un constat critique traîne depuis onze semaines. En comité, chacun explique de bonne foi pourquoi il ne s'agit pas de son périmètre : l'exploitation dit que c'est applicatif, l'équipe applicative dit que c'est système, le métier dit qu'il n'a pas été saisi. Tous ont raison. Ce qui manquait n'était pas de la bonne volonté, c'était un **délai de contestation borné** et une escalade automatique.

⚠️ **PIÈGE — le ticket affecté à une équipe**
Affecter à « l'équipe infrastructure » revient à n'affecter à personne : c'est la version outillée du problème du §5.5. L'affectation nominative est un prérequis, et le suivi de l'âge du *backlog* par personne révèle très vite les affectations fictives.

#### 17.5 Échéances : départ du compteur et suspensions légitimes

**La question qui doit être tranchée une fois pour toutes** : à partir de quand court le délai ?

| Point de départ possible | Avantage | Inconvénient |
|---|---|---|
| Publication du correctif par l'éditeur | Reflète le risque réel | Vous pénalise pour un scan tardif |
| **Détection par votre outil** | Mesurable, sous votre contrôle | Récompense un scan peu fréquent |
| Création du ticket | Simple | Décale artificiellement le délai |

**La recommandation** : mesurer **les deux premiers**, et les présenter séparément. Le délai depuis la publication mesure le temps écoulé **depuis qu'une correction était disponible** ; le délai depuis la détection mesure votre **réactivité**. L'écart entre les deux mesure la fraîcheur de votre détection (§15.5) — un troisième indicateur, gratuit, et souvent le plus instructif.

⚠️ **Aucun des deux ne mesure la durée d'exposition réelle**, qui commence à l'introduction de la vulnérabilité dans votre parc — souvent des années plus tôt, comme le montre le cas de synthèse A. Ne présentez jamais le délai depuis la publication comme « l'exposition » : c'est une borne inférieure.

##### Les deux horloges

C'est la distinction qui empêche de rendre le retard invisible.

| Horloge | Départ | Se suspend ? | Ce qu'elle mesure |
|---|---|---|---|
| **Horloge de risque** | Connaissance pertinente, ou disponibilité d'une correction ou d'une mesure d'atténuation | **Jamais** | Le temps pendant lequel le risque est porté |
| **Horloge de traitement (SLA)** | Idem | Oui, dans des cas limitativement définis | Le respect de l'engagement opérationnel |

**Pourquoi les deux sont nécessaires.** Un gel de production, une attente de correctif éditeur ou une demande d'information suspendent légitimement l'**engagement opérationnel** — l'équipe n'est pas en faute. Mais **le risque, lui, continue de courir**. Une organisation qui ne publie que l'horloge de traitement affiche des délais tenus tout en portant une exposition croissante qu'aucun indicateur ne montre.

✅ **BONNE PRATIQUE (P0)** — Publiez les deux. L'horloge de traitement pilote l'équipe ; l'horloge de risque pilote la direction. Un écart croissant entre les deux est le signal le plus honnête d'un problème structurel — capacité, dépendance fournisseur ou gels trop nombreux.

**Les suspensions légitimes de l'horloge de traitement**, à définir limitativement :

| Motif | Condition |
|---|---|
| Attente d'un correctif éditeur | Le correctif n'existe pas encore — documenté, relance périodique, **et mesure compensatoire engagée** (ch. 20) |
| Attente d'une information demandée à un tiers | Demande écrite et horodatée (§14.10), avec date de relance |
| Fenêtre de gel de production | Prévue par la politique, avec sa clause de levée (§9.4) |

⚠️ **Une suspension ne suspend jamais le risque.** Toute suspension de plus de quelques jours doit s'accompagner d'une mesure compensatoire ou d'une acceptation formelle — sinon vous avez seulement rendu le retard invisible.

⚠️ **PIÈGE — la suspension comme échappatoire**
Sans liste limitative, la suspension devient le moyen de faire disparaître les retards des indicateurs. **Deux garde-fous** : le temps passé en suspension est mesuré et affiché séparément, et une suspension de plus de N jours déclenche une escalade automatique.

🖼 **SCHÉMA — Cycle de vie d'un constat.** *Machine à états, sept états principaux, transitions fléchées, états terminaux distingués des états ouverts (dérogation, dépriorisé).*

#### 17.6 Le modèle d'états

Un cycle de vie en sept états, avec des transitions contrôlées. C'est le **livrable de référence** du chapitre, détaillé en Annexe J.

```
   NOUVEAU
      │  qualification (statut §14.7, vérifications §16.4)
      ▼
   QUALIFIÉ ──────────────────► FAUX POSITIF (clos, avec preuve)
      │  décision de triage (§16.3)
      ▼
   AFFECTÉ ───────────────────► DÉPRIORISÉ (ouvert, date de revue)
      │  propriétaire accepte
      ▼
   PLANIFIÉ ──────────────────► DÉROGATION (ouvert, §7.4)
      │  fenêtre, campagne
      ▼
   EN CORRECTION
      │  action réalisée
      ▼
   À VÉRIFIER ────────────────► ÉCHEC → retour à PLANIFIÉ
      │  preuve obtenue
      ▼
   CLOS ◄───────────────────── RÉOUVERTURE si réapparition
```

**Les champs obligatoires par état** — c'est ce qui empêche un ticket d'avancer sans le travail correspondant :

| État | Champs exigés pour y entrer |
|---|---|
| Qualifié | Statut de qualification, actifs confirmés, vérification d'activation |
| Affecté | Propriétaire nominatif, échéance, décision de triage |
| Planifié | Fenêtre ou campagne de rattachement, plan de retour arrière |
| À vérifier | Date d'action, méthode de vérification prévue |
| Clos | **Preuve** conforme au §2.9 |
| Déprioritisé | Motif parmi les quatre du §16.6, **date de revue** |
| Dérogation | Les sept champs du §7.4 |

#### 17.7 Les issues possibles, et la preuve attendue pour chacune

| Issue | Signification | Preuve exigée |
|---|---|---|
| **Corrigé** | Le correctif est appliqué et effectif | État constaté sur l'actif, postérieur à l'action (§2.9) |
| **Atténué** | Le risque est réduit sans correction | Description de la mesure, vérification qu'elle est active, **date d'expiration** |
| **Dérogation** | Décision de ne pas corriger, bornée | Fiche complète signée par le propriétaire métier |
| **Faux positif** | Le constat était erroné | **Démonstration**, pas affirmation : révision vérifiée, capture, avis éditeur |
| **Risque accepté** | Décision définitive de ne pas traiter | Signature au niveau approprié, revue périodique |
| **Sans objet** | L'actif n'existe plus | Preuve de décommissionnement (ch. 35) |

⚠️ **PIÈGE — le faux positif déclaré sans démonstration**
C'est la fuite la plus commune d'un processus de remédiation. Un constat gênant est marqué « faux positif » et disparaît. Sans preuve jointe, cette issue devient un moyen de vider la file sans travailler. **La règle** : un faux positif se clôt avec une démonstration vérifiable par un tiers, et un échantillon de faux positifs est recontrôlé chaque trimestre.

#### 17.8 Vérification et clôture

La règle est brutale et sans exception : **on ne clôt pas sur déclaration, on clôt sur preuve**.

| Méthode de vérification | Fiabilité | Usage |
|---|---|---|
| Nouveau scan de l'actif | Bonne | Méthode par défaut |
| Relevé direct de l'état (§2.9) | **Meilleure** | Actifs critiques, campagnes importantes |
| Rapport de l'outil de déploiement | Correcte, sous les trois conditions du §2.9 | Volume |
| Déclaration du propriétaire | **Insuffisante seule** | Jamais comme unique preuve |

**Le délai de vérification** doit être borné : un ticket qui reste en état « à vérifier » plus de X jours est en réalité non clos, et il pollue les indicateurs en donnant l'illusion que le travail est fait. Suivez cet état comme un indicateur à part entière.

#### 17.9 Réouverture et récurrence

**Une vulnérabilité corrigée qui réapparaît** est l'un des signaux les plus riches du MCS, et l'un des moins exploités.

**Les cinq causes racines**, avec leur remède :

| Cause | Mécanisme | Remède |
|---|---|---|
| **Image de référence non corrigée** | Chaque nouvelle machine naît vulnérable | Corriger le modèle, pas les instances (ch. 28) |
| **Restauration de sauvegarde** | Retour à un état antérieur au correctif | Contrôle post-restauration systématique |
| **Redéploiement automatique** | La définition déployée pointe une version ancienne | Corriger la définition, pas l'instance |
| **Retour arrière non suivi** | Un retour arrière a annulé le correctif sans que le ticket soit rouvert | Lier retour arrière et réouverture automatique |
| **Réinstallation manuelle** | Procédure d'installation obsolète | Mettre à jour la procédure |

**Le point d'organisation décisif** : une réapparition doit **rouvrir le ticket d'origine**, pas en créer un nouveau. Sinon la récurrence est invisible — chaque occurrence semble être un problème neuf — et la cause racine n'est jamais traitée. Un ticket rouvert trois fois est un signal, un ticket créé trois fois est du bruit.

✅ **BONNE PRATIQUE (P1)** — Suivez le **taux de récurrence** : constats réapparus rapportés aux constats clos sur la période. Un taux élevé n'indique pas une mauvaise exécution de la correction, il indique presque toujours un problème d'image de référence ou de processus de déploiement — donc un gain considérable si vous le traitez.

#### 17.10 Piloter le *backlog*

Le *backlog* est l'ensemble des constats ouverts. Trois lectures en donnent l'état réel.

**Le vieillissement.** Répartition des constats ouverts par tranche d'ancienneté :

| Tranche | Lecture |
|---|---|
| < 30 j | Flux normal |
| 30-90 j | Zone d'attention |
| 90-180 j | Difficulté structurelle : dépendance externe, effort sous-estimé, propriétaire absent |
| > 180 j | **Ce ne sont plus des constats, ce sont des dérogations non formalisées** |

La dernière ligne est la plus importante du chapitre. Un constat ouvert depuis plus de six mois sans décision formelle est une acceptation de risque **de fait**, prise par personne, revue par personne. La bonne action n'est pas de le corriger en urgence : c'est de le **qualifier** — dérogation, dépriorisation, ou correction planifiée avec engagement.

**L'écoulement.** Comparer entrées et sorties par période. Trois régimes possibles : la file se résorbe, elle est stable, elle grossit. Un *backlog* qui grossit malgré un travail intense signale un problème de capacité ou de périmètre, pas d'effort — et c'est un constat pour le comité stratégique.

**L'escalade.** Trois déclencheurs automatiques, sans intervention humaine : dépassement d'échéance, âge supérieur à un seuil, suspension prolongée. L'escalade suit les niveaux du §9.1.

#### 17.11 Synchroniser scanner, outil de tickets et inventaire

Trois systèmes, trois référentiels d'actifs, trois vérités possibles. Les ruptures classiques :

| Rupture | Symptôme | Prévention |
|---|---|---|
| Identifiants d'actifs divergents | Le même serveur apparaît sous trois noms | Identifiant pivot commun (§10.3, §15.7) |
| Constat corrigé, ticket toujours ouvert | Le scan a détecté la correction, le ticket ne le sait pas | Synchronisation périodique de l'état |
| Ticket clos, constat toujours présent | Clôture sans vérification (§17.8) | Interdire la clôture sans preuve |
| Actif décommissionné, tickets orphelins | Tickets sur une machine qui n'existe plus | Chaînage avec le processus de décommissionnement (ch. 35) |
| Historique perdu au changement d'outil | Impossible de démontrer un progrès | Export périodique en format ouvert (§15.12) |

✅ **BONNE PRATIQUE (P0)** — **L'inventaire fait autorité.** Le scanner et l'outil de tickets s'y réfèrent, ils ne créent pas d'actifs. Toute divergence est un écart d'inventaire à traiter selon le §10.3, pas une bizarrerie d'outil à contourner.

#### 17.12 📌 Ce qu'un outil de gestion ne réglera jamais

- **L'absence de propriétaire.** Un outil qui ne sait pas à qui affecter produit une file d'attente, pas une remédiation.
- **L'insuffisance de capacité.** Un *backlog* qui grossit ne se résout pas par une meilleure gestion du *backlog*.
- **La qualité de la preuve.** Un outil enregistre ce qu'on lui donne ; il ne vérifie rien.
- **Le contournement.** Si le processus est trop lourd, les corrections se feront hors outil, et vous perdrez à la fois la trace et la mesure. Le formalisme doit rester proportionné : dans une petite structure, une ligne dans un tableau tenu à jour vaut mieux qu'un outil que personne ne remplit.

#### 17.13 ✅ Livrable — Le workflow de remédiation

**Ce qui doit être écrit et validé**, et qui constitue l'Annexe J :

1. Le **modèle d'états** du §17.6 et ses transitions autorisées.
2. Les **champs obligatoires** par état.
3. Les **règles de déduplication** et le modèle parent / enfants.
4. Les **règles d'échéance** : point de départ, suspensions limitatives, seuils d'escalade.
5. Les **issues possibles** et la preuve exigée pour chacune.
6. Les **règles de réouverture**.
7. Le **contrat de service interne** : délai de contestation d'affectation, délai de réponse, suppléance.

#### 17.14 🔴 FIL ROUGE — mars 2027 : 3 800 constats, 21 campagnes, 187 tickets

Les 3 800 constats du scan de janvier, triés en février (§16.11), doivent maintenant être suivis. Malik Ferhaoui applique le modèle parent / enfants.

**La transformation du volume :**

| Étape | Volume |
|---|---|
| Constats bruts | 3 800 |
| Après déduplication par identifiant de vulnérabilité | 612 |
| Après regroupement par correctif | 244 |
| Après extraction des campagnes | **187 tickets + 21 campagnes** |

Les 187 tickets se répartissent en 23 en traitement unitaire, 140 déprioritisés avec date de revue, et 24 en attente d'un correctif éditeur — compteur suspendu, relance mensuelle.

**Le vieillissement révèle ce que le triage ne montrait pas.** Onze tickets dépassent 180 jours : ils datent des premiers scans de février 2026 et n'ont jamais été traités ni qualifiés. Ils concernent tous le même progiciel métier, dont l'éditeur exige une montée de version majeure facturée. Personne n'avait pris la décision — le sujet flottait entre l'exploitation, le métier et les achats.

Claire applique la règle du §17.10 : ce ne sont pas des constats en retard, ce sont des **dérogations non formalisées**. Elle les transforme en une dérogation unique, motivée, compensée par une restriction d'accès réseau, signée par le propriétaire métier, avec une date d'expiration alignée sur le budget 2028. Le *backlog* perd onze lignes ; l'organisation gagne une décision.

**Une découverte inattendue.** Le taux de récurrence sur les postes de travail atteint 18 % : près d'un constat clos sur cinq réapparaît dans les trois mois. L'analyse des cinq causes du §17.9 en identifie une seule : le modèle de machine virtuelle de mars 2024 (§3.9), jamais mis à jour. Chaque nouveau serveur créé depuis reproduit mécaniquement les mêmes constats. Corriger le modèle prend une demi-journée et supprime une source permanente de travail — ce que trois campagnes successives n'avaient pas réussi à faire.

**Ce que le comité retient.** Le nombre de « vulnérabilités ouvertes » a cessé d'être l'indicateur de référence. Il est remplacé par trois mesures : campagnes en cours et leur avancement, tickets dépassant leur échéance, et âge du plus ancien constat non qualifié. Ce dernier chiffre, en particulier, ne peut pas être embelli.

**Livrable de l'épisode.** Le workflow de remédiation d'HELIOMED, avec son modèle d'états et ses règles d'escalade — Annexe J.

→ La suite en 🔴 §18.14, lors de la nuit du déploiement raté sur le cluster de bases de données.

→ **Chapitre 18 — Le processus de correctif de bout en bout** : la chaîne complète d'un correctif, de la qualification à la preuve.

#### Synthèse mentale du chapitre 17

Entre la décision de triage et la correction effective, le constat doit exister comme objet de gestion, avec un propriétaire, une échéance et un état — faute de quoi le travail se perd, se duplique et ne se démontre pas. Le modèle parent/enfants et quatre règles de déduplication transforment des milliers de constats en dizaines de tickets, à condition de regrouper par action de correction et non par ressemblance. Mesurez deux délais séparément : depuis la publication du correctif, qui donne votre exposition réelle, et depuis la détection, qui donne votre réactivité — leur écart mesure gratuitement la fraîcheur de votre détection. Chaque issue exige sa preuve, et le faux positif déclaré sans démonstration est la fuite la plus commune d'un processus de remédiation. Une réapparition rouvre le ticket d'origine, sinon la récurrence reste invisible et sa cause racine — presque toujours une image de référence — n'est jamais traitée. Enfin, un constat ouvert depuis plus de six mois sans décision formelle est une acceptation de risque prise par personne : la bonne action est de le qualifier, pas de le corriger en urgence.

**Trois questions de vérification**

1. Votre file contient 3 800 constats. Décrivez les quatre étapes qui la ramènent à un nombre de tickets gérable, et le critère qui doit gouverner tout regroupement.
2. Un constat est clos comme faux positif. Que devez-vous exiger avant d'accepter cette clôture, et quel contrôle périodique mettez-vous en place ?
3. 18 % des constats clos sur les postes réapparaissent dans les trois mois. Quelles causes racines examinez-vous, dans quel ordre, et pourquoi corriger l'instance est-il ici une perte de temps ?

---

### Chapitre 18 — Le processus de correctif de bout en bout

#### 18.1 La chaîne complète

Neuf étapes, dont trois sont systématiquement escamotées : la qualification du correctif, la vérification post-déploiement, et la production de preuve.

```
1. Identification   → le constat existe et est qualifié (ch. 14-16)
2. Qualification    → que contient ce correctif, et qu'est-ce qu'il casse ?
3. Acquisition      → obtenir le correctif par un canal de confiance (§2.3)
4. Validation       → tester sur un environnement représentatif (§6.12)
5. Planification    → fenêtre, anneaux, plan de retour arrière
6. Déploiement      → progressif, avec critères d'arrêt
7. Vérification     → l'état constaté a-t-il changé ? (§2.9)
8. Clôture          → issue et preuve (§17.7)
9. Preuve           → archivage exploitable en audit (ch. 39)
```

**La règle de proportionnalité.** Les neuf étapes ne s'appliquent pas avec la même profondeur à tout. Un correctif de navigateur sur un poste C3 et une montée de version d'hyperviseur C1 suivent le même chemin, avec des exigences très différentes à chaque étape. La classe de service (§7.2) détermine cette profondeur — c'est à cela qu'elle sert.

#### 18.2 Qualifier un correctif avant de le déployer

**Les six questions**, dont les réponses se trouvent dans les notes de version, la base de connaissances de l'éditeur et les retours de la communauté :

| Question | Où chercher | Pourquoi |
|---|---|---|
| Que corrige-t-il exactement ? | Notes de version | Vérifier qu'il traite bien votre constat |
| Quels **prérequis** exige-t-il ? | Notes de version | Un correctif qui exige un niveau antérieur non installé échouera silencieusement |
| Quelles **régressions** sont signalées ? | Base de connaissances, forums, retours communautaires | C'est l'information la plus rentable de la liste |
| Nécessite-t-il un **redémarrage** ? | Notes de version | Détermine la fenêtre nécessaire |
| Est-il **désinstallable** ? | Documentation, test | Détermine le plan de retour arrière (§2.5) |
| Y a-t-il un **effet différé** ? | Notes de version | Le correctif à activation différée du §2.8 |

⚠️ **PIÈGE — le correctif déjà connu comme problématique**
Beaucoup de régressions sont signalées publiquement dans les 48 à 72 heures suivant la publication. Une organisation qui déploie systématiquement dans les 24 heures s'expose à des problèmes que d'autres ont déjà documentés. C'est l'argument principal en faveur d'un **délai d'observation** avant le premier anneau — sauf urgence caractérisée (chapitre 21), où le calcul s'inverse.

#### 18.3 Valider : environnements et jeux de tests

Le §6.12 a posé le problème de la représentativité. Voici la mise en œuvre.

**Trois niveaux de validation**, selon la classe de service :

| Niveau | Contenu | Pour quelle classe |
|---|---|---|
| **Aucune** | Déploiement direct en anneau pilote | C3, correctifs de sécurité courants |
| **Fonctionnelle** | Tests métier sur environnement de recette | C2 |
| **Complète** | Recette + tests de non-régression + validation métier formelle | C1, montées de version |

**Le délai d'observation** est un outil distinct des tests, et souvent plus efficace : laisser passer un temps défini entre la publication et le déploiement, pendant lequel les régressions apparaissent chez d'autres. Un délai de 3 à 7 jours capte l'essentiel des problèmes signalés publiquement, pour un coût nul.

✅ **BONNE PRATIQUE (P1)** — Formalisez ce délai dans la politique, avec sa dérogation : *délai d'observation de 5 jours, sauf vulnérabilité activement exploitée où il est ramené à zéro*. Cela transforme un comportement implicite en règle explicite, et cela évite la discussion à chaque campagne.

🖼 **SCHÉMA — Anneaux de déploiement et critères de passage.** *Cinq anneaux concentriques ou en cascade, avec la durée d'observation et le critère de passage entre chacun.*

#### 18.4 Le déploiement par anneaux

**Le principe.** Découper le parc en populations successives, avec un critère de passage entre chacune.

| Anneau | Population | Taille indicative | Durée d'observation |
|---|---|---|---|
| 0 — Laboratoire | Machines de test | Quelques unités | 1 à 3 jours |
| 1 — Pilote | Volontaires, équipe informatique | 2 à 5 % | 3 à 5 jours |
| 2 — Représentatif | Échantillon couvrant tous les profils métier | 10 à 20 % | 3 à 7 jours |
| 3 — Général | Le reste | 75 à 85 % | — |
| 4 — Sensibles | Actifs critiques, cas particuliers | Quelques unités | Traitement unitaire |

**Les deux erreurs de conception des anneaux :**

1. **L'anneau pilote non représentatif.** Composé uniquement de machines de l'équipe informatique, il ne teste ni les applications métier, ni les configurations réelles, ni les usages. Il valide qu'un correctif s'installe, pas qu'il ne casse rien.
2. **L'absence de critère de passage.** On passe à l'anneau suivant « parce que ça semble aller ». Le critère doit être écrit, mesurable et vérifié : taux d'installation réussie, absence d'incident déclaré, indicateurs fonctionnels stables (§6.8).

**Les critères d'arrêt automatiques**, définis avant le déploiement :

```
Arrêt de la campagne si l'une de ces conditions est atteinte :
  · taux d'échec d'installation      > 5 %
  · incidents déclarés liés          ≥ 3 sur l'anneau
  · indicateur fonctionnel           baisse > 10 % sur 30 min
  · redémarrages inattendus          ≥ 2 machines
```

#### 18.5 Ordre des opérations et dépendances

**Redémarrer quoi ?** Trois niveaux, du moins au plus coûteux : le **processus** (rechargement du binaire), le **service** (arrêt et relance du démon), le **système** (redémarrage complet). Le §2.6 fournit les commandes pour savoir lequel est nécessaire. Choisir le niveau minimal suffisant divise le coût d'une campagne.

**L'ordre entre composants.** Une chaîne applicative se met à jour dans un ordre déterminé par les dépendances : en général, du plus profond au plus superficiel — base de données, puis services applicatifs, puis frontaux — sauf indication contraire de l'éditeur. Un ordre inversé produit des erreurs de compatibilité pendant la transition.

**Les quatre opérations connexes** systématiquement oubliées dans les plans de campagne :

| Opération | Pourquoi elle compte |
|---|---|
| **Drainage des connexions** | Arrêter un service avec des sessions actives produit des erreurs visibles côté utilisateur |
| **Invalidation de cache** | Un cache contenant l'ancien comportement peut annuler l'effet du correctif ou produire des incohérences |
| **Bascule de cluster** | Ordre, temporisation, vérification de la synchronisation avant de basculer le second membre (§2.7) |
| **Réindexation ou migration de données** | Peut prendre des heures et n'est pas interruptible |

#### 18.6 Contraintes d'infrastructure

Trois contraintes physiques qui font échouer des campagnes correctement conçues :

- **La bande passante.** Un correctif cumulatif de plusieurs centaines de mégaoctets multiplié par le nombre de postes d'un site distant saturera la liaison. Remède : cache local, distribution entre pairs, ou déploiement échelonné par site.
- **Le démarrage massif simultané.** Programmer le redémarrage de centaines de machines virtuelles à la même minute sature le stockage et allonge le démarrage de plusieurs dizaines de minutes. Remède : échelonnement aléatoire sur une plage.
- **La capacité en mode dégradé.** Corriger un cluster suppose de fonctionner temporairement avec un membre en moins (§6.3). Si la capacité restante ne suffit pas, la campagne provoque une dégradation de service.

#### 18.7 Migrations et correctifs non réversibles

Le §6.7 a traité les migrations de schéma. Deux règles opérationnelles en découlent :

1. **Identifier le point de non-retour avant de commencer**, et l'écrire dans la demande de changement. La question exacte : *à partir de quel instant un retour arrière exigera-t-il une restauration de données ?*
2. **Vérifier la réversibilité réelle du correctif** (§2.5) sur une machine représentative, avant la campagne — pas pendant l'incident.

#### 18.8 Le plan de retour arrière

| Élément | Exigence |
|---|---|
| Mécanisme | Nommé explicitement : instantané, sauvegarde, redéploiement, désinstallation vérifiée |
| **Durée mesurée** | Chronométrée lors du test. C'est cette durée qui décide si vous osez déployer |
| Point de non-retour | Identifié et daté |
| Décideur | Qui décide du retour arrière, et sur quel critère |
| Vérification post-retour | Comment s'assurer que l'état antérieur est bien restauré |

⚠️ **PIÈGE — le plan de retour arrière jamais testé**
Un plan non testé n'est pas un plan. Le test doit être fait au moins une fois par type d'actif et par mécanisme, et refait après tout changement significatif de l'environnement.

#### 18.9 Vérification post-déploiement

Trois vérifications distinctes, souvent confondues :

| Vérification | Question | Méthode |
|---|---|---|
| **Technique** | Le correctif est-il appliqué ? | État constaté (§2.9) |
| **Effectivité** | Le code corrigé s'exécute-t-il ? | Redémarrage confirmé (§2.6) |
| **Fonctionnelle** | Le service fait-il toujours son travail ? | Indicateur fonctionnel (§6.8) |

La troisième est celle qui manque presque toujours, et c'est celle qui détecte les régressions silencieuses.

#### 18.10 La traîne longue

Toute campagne laisse un résidu : machines éteintes, nomades absents, actifs en échec, cas particuliers. Ce résidu représente typiquement 2 à 5 % du parc, et il concentre une part disproportionnée des risques.

**Le traitement à trois niveaux :**

1. **Relance automatique** pendant une période définie — la majorité du résidu se résorbe seule.
2. **Traitement manuel** du reste, actif par actif, avec identification de la cause.
3. **Qualification formelle** de ce qui résiste : dérogation (§7.4) ou décommissionnement (chapitre 35).

**La règle** : une campagne n'est pas close tant que sa traîne longue n'est pas qualifiée. Une campagne « terminée à 97 % » avec 3 % non qualifiés est une campagne dont la partie la plus risquée n'a pas été traitée.

#### 18.11 ⚠️ Quand le correctif casse

Les mises à jour défectueuses existent, y compris chez les éditeurs majeurs, et y compris sur des correctifs de sécurité. La doctrine à tenir n'est ni la naïveté ni l'immobilisme.

| Ce qui ne marche pas | Ce qui marche |
|---|---|
| Déployer immédiatement partout | Anneaux + délai d'observation + critères d'arrêt |
| Ne jamais déployer avant plusieurs mois | Délai borné et différencié par classe |
| Décider au cas par cas dans l'urgence | Doctrine écrite, avec dérogation prévue pour l'urgence |

**Le calcul à faire dans chaque cas**, et il est explicite : comparer le risque du correctif (probabilité de régression × impact de l'indisponibilité) et le risque du non-correctif (probabilité d'exploitation × impact de la compromission). Ce calcul est le sujet entier du cas de synthèse C.

#### 18.12 🔬 Mini-lab 5 — Concevoir des anneaux de déploiement

**Objectif** — Découper un parc en anneaux réellement représentatifs et définir des critères de passage vérifiables.
**Durée** 45 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §18.4, §6.8 · **Livrable** tableau d'anneaux + grille de critères (D.6).
**Compétences validées** — ✔ composer un anneau pilote représentatif ✔ écrire des critères de passage vérifiables ✔ traiter une population intermittente ✔ arbitrer une échéance intenable plutôt que la subir

**Données fournies — parc de 340 postes**

| Population | Nb | Particularités | Applications métier critiques | Connexion réseau interne |
|---|---|---|---|---|
| Siège — bureautique | 180 | Poste standard, droits utilisateur | Gestion commerciale, paie (RH only) | Permanente |
| Siège — direction et RH | 22 | Données sensibles | Paie, gestion documentaire | Permanente |
| R&D Nantes | 90 | Droits d'administration locaux, environnements de développement, machines puissantes | Chaîne de développement, outils de build | Permanente |
| Commerciaux nomades | 40 | Se connectent 2 à 6 fois/mois | Gestion commerciale, hors ligne partiel | **Intermittente** |
| Site industriel — bureautique | 19 | Horaires 3×8, arrêts de ligne à éviter | Suivi de production (lecture) | Permanente |
| Site industriel — supervision | 11 | **Classe C4**, validation constructeur requise | Conduite de ligne | Réseau industriel |

**Contraintes** : la campagne doit être terminée en 21 jours · l'équipe dispose de 2 personnes · le correctif exige un redémarrage · deux régressions sur la gestion commerciale ont été signalées publiquement dans les 48 h suivant la publication.

**Questions**
(a) Proposez un découpage en anneaux, avec effectifs et justification.
(b) Écrivez les critères de passage entre anneaux.
(c) Traitez les nomades.
(d) Traitez les 11 postes de supervision.
(e) La contrainte de 21 jours est-elle tenable ? Que faites-vous si elle ne l'est pas ?

---

**Corrigé commenté**

**(a) Découpage proposé**

| Anneau | Composition | Nb | Durée d'observation | Justification |
|---|---|---|---|---|
| **0 — Laboratoire** | 4 machines de test, dont 1 image R&D | 4 | 1 j | Valide l'installation, pas l'usage |
| **1 — Pilote représentatif** | 6 siège bureautique · 4 R&D · **2 commerciaux** · 1 industriel bureautique | 13 | 3 j | **Les quatre profils dès le pilote** |
| **2 — Élargi** | 40 siège · 20 R&D · 10 commerciaux · 6 industriel | 76 | 5 j | Couvre les applications métier en usage réel |
| **3 — Général** | Reste siège (134) + reste R&D (66) | 200 | — | Volume |
| **4 — Sensibles et contraints** | 22 direction/RH · 12 industriel bureautique restant | 34 | Unitaire | Données sensibles, horaires 3×8 |
| **Hors anneaux** | 11 supervision C4 | 11 | — | Régime distinct |
| **Population séparée** | 28 nomades restants | 28 | Suivi propre | Voir (c) |

**Pourquoi la direction et les RH en anneau 4 et non en anneau 1** : ils portent les données les plus sensibles, et une régression sur la paie a un coût politique disproportionné. Ils bénéficient de l'observation faite sur les 289 postes précédents.

**(b) Critères de passage — formulaire D.6 rempli**

| Indicateur | Seuil d'arrêt | Mesuré par | Fenêtre |
|---|---|---|---|
| Taux d'échec d'installation | `> 5 %` | Console de déploiement | Continu |
| Incidents déclarés liés | `≥ 3 sur l'anneau` | Support N1 | 24 h |
| **Transactions abouties — gestion commerciale** | `baisse > 10 % sur 30 min` | Supervision applicative | Continu |
| **Éditions de paie abouties** | `tout échec` | Supervision applicative | Continu (anneau 4) |
| Redémarrages inattendus | `≥ 2 machines` | Supervision poste | Continu |

**Critère de passage** : tous les seuils respectés pendant la durée d'observation **et** aucun incident bloquant ouvert **et** validation explicite du référent métier de la gestion commerciale pour le passage à l'anneau 3.

Le dernier point est ajouté à cause des deux régressions signalées publiquement : il est justifié ici, et ne le serait pas sur un correctif sans antécédent.

**(c) Les nomades — trois mesures**

1. **Deux d'entre eux dès l'anneau 1.** C'est là que se révèlent les problèmes de déploiement hors réseau interne : téléchargement sur liaison lente, échec de reprise, interruption pendant l'installation.
2. **Mécanisme fonctionnant sur Internet**, sans passage obligatoire par le réseau interne.
3. **Population suivie séparément**, avec une échéance plus longue (`J+45` au lieu de `J+21`) mais **mesurée**. Ils ne sont ni fondus dans le taux global, ni exclus silencieusement (§15.6).

⚠️ Une erreur fréquente consiste à leur appliquer l'échéance générale et à constater un taux de conformité dégradé chaque mois, sans jamais traiter la cause.

**(d) Les 11 postes de supervision**

Régime C4 : hors campagne. Correctif soumis à validation constructeur, application lors de la fenêtre de relève d'équipe ou de l'arrêt de production. Dans l'intervalle, compensation selon le §20.2. Ils figurent au tableau de bord comme **population distincte**, avec leur propre indicateur de compensation vérifiée — jamais fondus dans le taux général (§10.11).

**(e) La contrainte de 21 jours**

Elle n'est **pas tenable** telle quelle : 1 + 3 + 5 jours d'observation = 9 jours avant l'anneau 3, auxquels s'ajoutent le déploiement sur 200 postes, l'anneau 4 unitaire, et la traîne longue. Le calendrier réaliste est de 28 à 32 jours pour l'ensemble, hors nomades.

**Trois réponses possibles, à arbitrer explicitement** :

| Option | Effet | Coût |
|---|---|---|
| Compresser les durées d'observation à 1 j / 3 j | Gain de 4 jours | Augmente le risque de régression massive — inacceptable ici vu les antécédents |
| Paralléliser les anneaux 3 et 4 | Gain de 3 jours | Prive l'anneau 4 du bénéfice de l'observation |
| **Négocier l'échéance à 30 jours** | Calendrier tenable | Documenter le dépassement et sa justification |

La troisième est la bonne réponse dans ce cas : le constat n'est pas exploité, et le §16.5 rappelle qu'un délai qu'on ne tient pas produit une non-conformité permanente. **Un délai renégocié et documenté vaut mieux qu'un délai affiché et manqué.**

**Les trois erreurs attendues**
1. Composer l'anneau 1 uniquement de postes de l'équipe informatique : le correctif s'installera parfaitement, et la régression sur la gestion commerciale apparaîtra en anneau 3, sur 200 postes.
2. Placer la direction et les RH en anneau 1 « parce qu'ils sont peu nombreux ».
3. Accepter les 21 jours sans le dire, et livrer un taux dégradé un mois plus tard sans explication.

#### 18.13 🔬 Mini-lab 6 — Produire la preuve d'une campagne

**Objectif** — Constituer un dossier de preuve recevable en audit et distinguer preuve recevable, contestable et irrecevable.
**Durée** 40 min · **Difficulté** 🔴 avancé · **Prérequis** §2.9, §18.9, §15.6 · **Livrable** dossier de preuve en six pièces (D.13).
**Compétences validées** — ✔ constituer un dossier de preuve recevable ✔ identifier le vrai dénominateur d'une campagne ✔ vérifier un état sur échantillon ✔ classer une preuve en recevable / contestable / irrecevable

**Données fournies**

Campagne `CAMP-2027-04`, correctif système sur serveurs Linux. Extraits bruts fournis :

*Extrait 1 — rapport de la console de déploiement, exporté le 22/04/2027 à 09 h 14*
```
Campagne CAMP-2027-04 — cible : groupe "SRV-LINUX-PROD"
  Succès ................ 168
  Échec ................. 5
  Non joignable ......... 3
  Total ciblé ........... 176
```

*Extrait 2 — périmètre de référence, extraction du 01/04/2027*
```
Serveurs Linux, environnement = production ....... 181
   dont couverts par la console de déploiement ... 176
   dont hors console (motif non renseigné) ....... 5
```

*Extrait 3 — détail des échecs, journal de la console*
```
srv-app-07   ERR_DISK_SPACE      /var 98% plein
srv-app-11   ERR_DISK_SPACE      /var 97% plein
srv-bdd-03   ERR_LOCK            paquet verrouillé par une transaction en cours
srv-web-09   ERR_DEPENDENCY      prérequis manquant
srv-int-02   ERR_TIMEOUT         pas de réponse après 3 tentatives
```

*Extrait 4 — non joignables*
```
srv-lab-04   dernier contact 12/02/2027
srv-old-01   dernier contact 30/11/2026
srv-tst-06   dernier contact 19/04/2027
```

**Questions**
(a) Quelles six pièces produisez-vous ?
(b) Quel est le vrai dénominateur, et que vaut le taux de réussite annoncé ?
(c) Quelle est la faiblesse d'un rapport de console seul, et comment la comblez-vous ?
(d) Traitez les 8 actifs restants **et** les 5 hors console.
(e) Classez trois formulations en preuve recevable, contestable, irrecevable.

---

**Corrigé commenté**

**(a) Le dossier en six pièces**

| # | Pièce | Contenu pour ce cas |
|---|---|---|
| 1 | Périmètre | 181 serveurs éligibles, dont 176 ciblés et **5 hors console — motif à documenter** |
| 2 | Décision | Ticket de triage, chemin dans l'arbre, échéance |
| 3 | Exécution | Extrait 1 daté et non retouché, avec les trois populations |
| 4 | **Vérification indépendante** | État constaté sur 18 serveurs tirés au sort (≈ 10 %), horodaté, méthode décrite |
| 5 | Traîne longue | Les 8 en échec ou non joignables + les 5 hors console, avec cause et échéance |
| 6 | Clôture | Date, responsable, issue, preuve rattachée |

**(b) Le dénominateur**

| Formulation | Valeur | Statut |
|---|---|---|
| « 95 % de réussite » (168/176) | 95 % | **Réussite de la campagne dans sa cible** |
| Sur les serveurs éligibles | 168/181 = **93 %** | Le chiffre à publier |
| Non mesuré | 5 hors console + 3 non joignables = **8 (4,4 %)** | À publier séparément |

Les 5 serveurs hors console sont le point le plus important de l'exercice : ils n'apparaissent **ni** dans le numérateur, **ni** dans le dénominateur de la console. C'est l'écart de type 3 du §10.3 — déclarés, actifs, jamais atteints.

**(c) La faiblesse du rapport de console**

Il rapporte ce que l'outil **croit** avoir fait. Il n'établit ni que le code corrigé s'exécute — un redémarrage a-t-il eu lieu ? — ni que la console couvre bien le périmètre éligible.

Les trois conditions de recevabilité (§2.9) : périmètre défini et rapproché du périmètre de référence · intégrité de l'extraction (datée, non retouchée) · liste des non joignables fournie. L'échantillon vérifié indépendamment est ce qui transforme un rapport en preuve.

🧪 **La vérification à réaliser sur l'échantillon**

```bash
# Sur chacun des 18 serveurs tirés au sort
dnf history info $(dnf history list | awk 'NR==3{print $1}')   # ou dpkg/apt selon la famille
uptime -s                                                       # date du dernier démarrage
needs-restarting -r ; echo "code retour : $?"                   # redémarrage encore requis ?
```

Le troisième contrôle est le plus important : un correctif installé sans redémarrage laisse le code vulnérable en mémoire (§2.6).

**(d) Traitement des 13 actifs**

| Groupe | Cause | Action | Échéance |
|---|---|---|---|
| srv-app-07, srv-app-11 | Espace disque | Libérer `/var`, relancer. **Cause racine** : aucune supervision de l'espace disque sur ces serveurs | 48 h |
| srv-bdd-03 | Transaction verrouillée | Relancer hors fenêtre de traitement | 48 h |
| srv-web-09 | Prérequis manquant | Installer le prérequis puis relancer. Vérifier si d'autres serveurs sont concernés | 5 j |
| srv-int-02 | Pas de réponse | Vérifier l'état de la machine — agent, réseau, ou machine arrêtée | 5 j |
| srv-lab-04, srv-old-01 | Sans contact depuis 2 et 5 mois | **Candidats au décommissionnement** (§10.3) — vérifier l'existence, sinon PV | 15 j |
| srv-tst-06 | Sans contact depuis 3 jours | Probablement éteint temporairement : relance automatique | 15 j |
| **5 serveurs hors console** | **Motif non renseigné** | **Priorité maximale** : les rattacher à la console ou documenter l'exclusion | 10 j |

**(e) Recevable, contestable, irrecevable**

| Formulation | Statut | Pourquoi |
|---|---|---|
| « Rapport de console du 22/04/2027 09 h 14, périmètre 176 serveurs rapproché des 181 éligibles, 3 non joignables listés, complété d'un relevé d'état horodaté sur 18 serveurs tirés au sort » | **Recevable** | Périmètre, intégrité, non joignables, vérification indépendante |
| « Rapport de console : 95 % de réussite » | **Contestable** | Exact, mais sans périmètre ni dénominateur : l'auditeur demandera les 5 % et les 5 serveurs hors console |
| « L'équipe confirme que la campagne s'est bien déroulée » | **Irrecevable** | Déclaration sans donnée (§5.6) |

**Les deux erreurs attendues**
1. Publier 95 % sans mentionner les 5 serveurs hors console — le chiffre est exact et le périmètre est faux.
2. Considérer la campagne close à 95 % : les 4,4 % non traités concentrent l'essentiel du risque résiduel (§18.10).

#### 18.14 🔴 FIL ROUGE — avril 2027 : la nuit du déploiement raté

Campagne de montée de version mineure sur le cluster de bases de données d'HelioLink — trois nœuds, classe C1. Correctif de sécurité, vulnérabilité non exploitée mais gravité élevée, échéance à 30 jours.

**Ce qui était prévu.** Fenêtre samedi 22 h - 2 h. Test préalable en recette : concluant. Retour arrière annoncé par instantané des trois machines virtuelles. Malik Ferhaoui et un ingénieur d'astreinte.

**Ce qui s'est passé.** À 22 h 40, le premier nœud est mis à jour et redémarre normalement. À 22 h 55, la réplication ne repart pas : les deux versions ne se synchronisent pas. Le correctif embarquait une modification du format de réplication, mentionnée en dernière ligne des notes de version, sous une rubrique que personne n'avait lue.

À 23 h 10, décision de retour arrière. L'instantané est restauré : le nœud revient à sa version antérieure. Mais la réplication ne repart toujours pas — le nœud restauré est désormais en retard de quarante minutes de transactions, et le mécanisme de rattrapage automatique refuse de s'engager au-delà d'un certain écart.

À 1 h 20, après une resynchronisation complète manuelle, le service est rétabli. Aucune donnée perdue. Quatre heures d'indisponibilité de la plateforme de télésuivi, un dimanche matin — période de faible usage, mais deux établissements clients ont appelé le support.

**Les quatre causes racines identifiées au retour d'expérience :**

| Cause | Ce qui aurait évité |
|---|---|
| Notes de version lues en diagonale | La qualification en six questions du §18.2, notamment « quels prérequis » |
| Test en recette sur un **nœud unique**, pas sur un cluster | L'écart de représentativité du §6.12, non mesuré |
| Plan de retour arrière testé sur une machine isolée | Le test du §18.8 sur un actif **représentatif**, cluster inclus |
| Aucun critère d'arrêt écrit | La décision de retour arrière a pris 15 minutes de discussion |

**Ce qui n'a pas mal fonctionné**, et que Claire Nadeau tient à souligner au comité : la fenêtre était correcte, l'astreinte était en place, l'instantané existait, et aucune donnée n'a été perdue. L'incident aurait pu être bien pire sans ces éléments.

**Les trois mesures.**

1. La qualification en six questions devient un **champ obligatoire** du dossier de campagne pour toute classe C1 — avec la référence exacte de la section des notes de version consultée.
2. Le test de retour arrière doit être réalisé **sur une topologie représentative**. L'écart entre recette et production est désormais mesuré sur les quatre axes du §6.12 et affiché dans le dossier de campagne.
3. Les critères d'arrêt et le décideur sont écrits **avant** l'intervention, dans la demande de changement.

**Livrable de l'épisode.** Le dossier de campagne standard d'HELIOMED, en Annexe D : qualification, écart de représentativité, anneaux, critères d'arrêt, plan de retour arrière chronométré, décideur nommé.

→ La suite en 🔴 §19.11, quand il faudra choisir l'outillage capable de porter tout cela.

→ **Chapitre 19 — Outillage de déploiement par plateforme** : l'outillage — familles, critères de choix et limites structurelles.

#### Synthèse mentale du chapitre 18

Neuf étapes composent la chaîne, dont trois sont systématiquement escamotées : qualifier le correctif, vérifier après déploiement, produire la preuve. La qualification en six questions coûte quinze minutes et évite l'essentiel des incidents — la question des régressions déjà signalées est la plus rentable. Le délai d'observation est un outil distinct des tests, et souvent plus efficace pour un coût nul. Les anneaux échouent pour deux raisons : un pilote non représentatif, qui valide qu'un correctif s'installe et non qu'il ne casse rien, et l'absence de critère de passage écrit. Le plan de retour arrière doit être chronométré, car c'est sa durée mesurée qui décide si vous osez déployer. La vérification fonctionnelle est celle qui manque toujours et qui détecte les régressions silencieuses. Enfin, une campagne n'est pas close tant que sa traîne longue n'est pas qualifiée : ces 3 % concentrent une part disproportionnée du risque.

**Trois questions de vérification**

1. Citez les trois étapes de la chaîne les plus souvent escamotées et, pour chacune, la conséquence concrète de son absence.
2. Votre anneau pilote est composé des postes de l'équipe informatique. Qu'est-ce que cela valide réellement, et qu'est-ce que cela laisse passer ?
3. Une campagne affiche 97 % de réussite. Pourquoi ne pouvez-vous pas la clore, et que devez-vous produire sur les 3 % restants ?

---

### Chapitre 19 — Outillage de déploiement par plateforme

> **Note de lecture.** Ce chapitre traite des **familles d'outils**, de leurs mécanismes et de leurs limites structurelles. Les outils nommés, leurs modèles de licence et leurs limites propriétaires figurent en **Annexe E**, qui est datée et versionnée. Cette séparation est délibérée : les mécanismes ci-dessous resteront valables quand les produits auront changé.

#### 19.1 La grille de choix, indépendante des produits

Neuf critères suffisent à évaluer n'importe quel outil de déploiement, et à comprendre pourquoi aucun ne suffit seul.

| Critère | Question | Piège fréquent |
|---|---|---|
| **Couverture** | Quels systèmes, quelles applications tierces, quels micrologiciels ? | La couverture annoncée inclut rarement les applications métier |
| **Hors domaine** | Gère-t-il les machines non jointes à l'annuaire ? | C'est précisément là que sont les actifs à risque |
| **Itinérance** | Fonctionne-t-il sans réseau interne ? | Sinon, les nomades décrochent (§18.12) |
| **Bande passante** | Cache local, distribution entre pairs, limitation ? | Sites distants saturés |
| **Granularité** | Peut-on cibler par anneau, par attribut, par exclusion ? | Sans cela, pas d'anneaux (§18.4) |
| **Critères d'arrêt** | Peut-on suspendre automatiquement une campagne ? | Rarement natif ; souvent à construire |
| **Reporting** | Peut-on exporter les données brutes, avec les non joignables ? | Le calcul honnête du §15.6 est souvent impossible nativement |
| **Réversibilité** | Peut-on revenir en arrière, et l'outil le trace-t-il ? | Dépend surtout de la plateforme (§2.5) |
| **Coût et dépendance** | Modèle de licence, portabilité de l'historique | L'historique est rarement exportable |

**Le critère décisif à long terme est le septième.** Un outil qui ne permet pas d'exporter ses données brutes vous empêche de calculer vos propres indicateurs (chapitre 38), de constituer une preuve indépendante (§2.9), et de changer de fournisseur sans perdre votre antériorité.

#### 19.2 Écosystème Windows

**Les mécanismes.** Quatre approches coexistent, souvent combinées dans un même parc :

| Approche | Principe | Adaptée à |
|---|---|---|
| **Service de mise à jour interne** | Un serveur relaie et approuve les correctifs de l'éditeur | Parcs sur site, contrôle fin des approbations |
| **Gestion de configuration d'entreprise** | Déploiement centralisé, applications tierces incluses | Grands parcs, besoins de granularité |
| **Gestion de flotte depuis le cloud** | Politiques appliquées aux machines où qu'elles soient | Nomades, hors domaine, parcs distribués |
| **Anneaux natifs de l'éditeur** | Découpage et échelonnement gérés par le service de l'éditeur | Postes standards, faible charge d'administration |

**Les trois points d'attention propres à Windows :**

1. **Les applications tierces ne sont pas couvertes par défaut.** Navigateurs, lecteurs, environnements d'exécution, clients d'accès distant représentent une part majeure des vulnérabilités exploitées sur poste, et exigent un mécanisme complémentaire (§19.5).
2. **Le redémarrage se pilote séparément** du déploiement. Un correctif installé et jamais redémarré n'est pas effectif — et les machines qui ne redémarrent jamais sont fréquentes.
3. **La réversibilité ne se présume pas** (§2.5).

#### 19.3 Écosystème Linux

| Mécanisme | Principe | Point d'attention |
|---|---|---|
| **Dépôts internes et miroirs** | Vous maîtrisez ce qui est publié et quand | Le miroir doit lui-même être maintenu et synchronisé |
| **Mise à jour non supervisée** | Le système applique seul les correctifs de sécurité | Efficace sur C3 ; à encadrer sur C1 (redémarrages, régressions) |
| **Gestion de configuration** | Un outil applique un état désiré sur un parc | Le plus flexible ; exige des compétences et du maintien |
| **Orchestration des redémarrages** | Détection et planification des redémarrages nécessaires | C'est ici que les campagnes Linux échouent (§2.6) |

⚠️ **PIÈGE — la mise à jour automatique sans orchestration du redémarrage**
Configuration très répandue : les correctifs s'appliquent automatiquement, personne ne redémarre les services, et l'organisation croit son parc à jour. Les bibliothèques corrigées sur disque continuent d'être exécutées en version vulnérable, parfois pendant des mois.

#### 19.4 macOS et mobiles

Trois particularités : les mises à jour sont **imposées par l'éditeur** avec peu de latitude de report ; le déploiement passe par une solution de gestion de flotte, sans équivalent des dépôts internes ; et l'utilisateur conserve souvent un pouvoir de report, ce qui rend la conformité dépendante de son comportement.

**La conséquence pour le MCS** : sur ces plateformes, vous pilotez surtout par la **politique** (exiger une version minimale pour accéder aux ressources) plutôt que par le déploiement. L'accès conditionnel fondé sur le niveau de mise à jour est le levier réel — traité au §28.8.

#### 19.5 Applications tierces : le trou noir du poste de travail

**Le constat.** Une part majeure des vulnérabilités réellement exploitées sur les postes concerne des applications tierces : navigateurs et leurs extensions, lecteurs de documents, environnements d'exécution, outils de compression, clients d'accès distant, utilitaires métier.

**Pourquoi elles échappent au dispositif :** elles ne sont pas couvertes par le mécanisme natif du système ; elles sont souvent installées hors processus ; leur inventaire est incomplet ; et elles se mettent à jour chacune selon son propre mécanisme, parfois en demandant des droits d'administration.

**Les trois approches**, par efficacité :

| Approche | Principe | Limite |
|---|---|---|
| Gestionnaire de paquets pour Windows | Catalogue centralisé, déploiement et mise à jour scriptables | Couverture du catalogue variable selon les applications métier |
| Module de mise à jour d'applications tierces intégré à l'outil de déploiement | Cohérence avec le reste du dispositif | Souvent une option payante, catalogue limité |
| Mise à jour automatique native de l'application | Aucun effort | Aucun contrôle, aucune visibilité, aucune preuve |

✅ **BONNE PRATIQUE (P0)** — Commencez par **inventorier** les applications tierces installées sur un échantillon de postes. La liste est presque toujours plus longue et plus ancienne qu'attendu, et cet inventaire suffit à justifier le budget du mécanisme de déploiement correspondant.

#### 19.6 Réseau, sécurité et hyperviseurs

Ces plateformes se distinguent par l'absence d'outil de déploiement au sens classique : la mise à jour est une opération d'administration, unitaire ou orchestrée par la console du constructeur.

| Point | Exigence |
|---|---|
| Cadence | Doctrine de version écrite et datée (§2.7), pas une habitude |
| Séquence | Passif, vérification, bascule, actif — avec les précautions du §2.7 |
| Retour arrière | Double partition d'image, testée |
| Preuve | Version relevée directement sur l'équipement, pas dans un tableur |
| Micrologiciels | Traités comme une campagne à part entière, par anneaux (§3.8) |

#### 19.7 Conteneurs et cloud

Le paradigme change complètement : on ne déploie pas un correctif, on **reconstruit et on remplace** (§3.2).

| Objet | Mécanisme de correction | Indicateur pertinent |
|---|---|---|
| Image de conteneur | Reconstruction depuis une image de base à jour | **Âge de l'image** en production |
| Nœuds de cluster | Remplacement des nœuds par de nouvelles images | Version des nœuds, écart avec le plan de contrôle |
| Instances cloud | Redéploiement depuis une image mise à jour | Âge de l'image, part d'instances hors modèle |
| Services managés | Fenêtre de mise à jour du fournisseur | Versions dépréciées et échéances (ch. 30) |

**Le déplacement du travail** est ici essentiel : le MCS ne se joue plus au déploiement mais dans la **chaîne de construction** — donc dans un périmètre souvent détenu par les équipes de développement, pas par l'exploitation. C'est un sujet d'organisation autant que d'outillage (chapitre 28).

#### 19.8 ⏱ Consolider le reporting multi-outils

Une organisation de taille intermédiaire utilise couramment cinq à huit mécanismes de déploiement distincts. Chacun produit son propre rapport, avec son propre périmètre, son propre vocabulaire et son propre calcul.

**Le problème du chiffre unique.** Additionner ces rapports produit un nombre faux, pour trois raisons : les périmètres se recouvrent partiellement, les définitions de « conforme » diffèrent d'un outil à l'autre, et les actifs non couverts par aucun outil n'apparaissent nulle part.

✅ **BONNE PRATIQUE (P0) — la consolidation par le périmètre, pas par les outils**
Partez du **périmètre de référence** (chapitre 10), et pour chaque actif, indiquez quel outil le couvre et quel est son état. Les actifs couverts par aucun outil apparaissent alors explicitement — c'est l'information la plus importante que produise cette consolidation, et celle qu'aucun rapport d'outil ne donnera jamais.

#### 19.9 📌 Limites communes à toutes les familles

- **Le coût croît avec la découverte.** Les licences par actif créent une incitation perverse : mieux inventorier augmente la facture.
- **Aucun outil ne couvre tout le périmètre réel.** Systèmes industriels, services en ligne, composants embarqués, produits livrés aux clients restent hors champ.
- **Le reporting natif est rarement honnête.** Il présente le taux de conformité sur les actifs que l'outil connaît — c'est-à-dire le chiffre flatteur du §10.11.
- **La dépendance à l'éditeur est forte**, et l'historique rarement portable.
- **L'outil ne crée pas de fenêtre.** La contrainte dominante reste organisationnelle.

#### 19.10 ✅ Recommandations priorisées

| Prio | Taille d'organisation | Recommandation |
|---|---|---|
| **P0** | Toutes | Un mécanisme couvrant les systèmes d'exploitation, avec reporting exportable |
| **P0** | Toutes | Un mécanisme pour les applications tierces du poste de travail |
| **P0** | Toutes | La consolidation par le périmètre de référence (§19.8) |
| P1 | > 200 actifs | Anneaux et critères d'arrêt outillés (§18.4) |
| P1 | Parc distribué | Mécanisme fonctionnant hors réseau interne |
| P1 | Toutes | Orchestration des redémarrages, avec indicateur de temps sans redémarrage |
| P2 | > 500 actifs | Automatisation de la vérification post-déploiement |
| P2 | Environnements cloud | Reconstruction périodique automatisée des images |

#### 19.11 🔴 FIL ROUGE — mai 2027 : l'inventaire des mécanismes

Avant tout achat, Claire Nadeau demande l'inventaire des mécanismes de déploiement réellement en usage chez HELIOMED. Le résultat surprend tout le monde.

| Mécanisme | Périmètre couvert | Reporting exportable |
|---|---|---|
| Console interne de l'exploitation | 176 serveurs Windows et Linux | Oui |
| Console de l'infogérant | 620 postes | Oui, depuis janvier (§13.9) |
| Mise à jour automatique native, non supervisée | 34 serveurs Linux découverts en 2026 | **Non** |
| Consoles constructeurs | 6 équipements réseau | Non — relevé manuel |
| Chaîne de construction de Nantes | Images de conteneurs | Oui, mais non rattachée au périmètre MCS |
| Aucun | **11 postes de supervision, 3 automates, 38 services en ligne, tous les micrologiciels** | — |

**Six mécanismes, aucune vue consolidée.** Le taux annoncé au comité provenait des deux premiers, soit 796 actifs sur un périmètre de référence en comptant nettement plus.

**Les trois décisions.**

1. **Pas d'achat.** Les deux mécanismes principaux couvrent l'essentiel ; le problème n'est pas l'outillage, c'est la consolidation. Une extraction mensuelle rapprochée du périmètre de référence est mise en place — quelques jours de travail, aucun coût de licence.
2. **Les 34 serveurs en mise à jour automatique non supervisée** sont rattachés à la console interne. Le contrôle révèle au passage que 12 d'entre eux appliquaient bien les correctifs mais n'avaient pas redémarré depuis plus de 400 jours — le piège exact du §19.3.
3. **Les applications tierces du poste de travail** deviennent le seul vrai sujet d'investissement. L'inventaire sur 30 postes remonte 47 applications distinctes, dont 9 hors support. C'est la ligne budgétaire retenue pour 2028.

**Ce que Claire écrit dans sa note.** *Nous n'avions pas un problème d'outil, nous avions un problème de dénominateur. L'achat d'un outil supplémentaire aurait produit un septième rapport partiel.*

**Livrable de l'épisode.** La consolidation par périmètre, et l'inventaire des applications tierces — première ligne du budget 2028.

→ La suite en 🔴 §20.11, quand une ligne d'assemblage ne pourra pas être arrêtée avant novembre.

→ **Chapitre 20 — Quand on ne peut pas patcher : les mesures compensatoires** : que faire quand corriger est impossible.

#### Synthèse mentale du chapitre 19

Neuf critères évaluent n'importe quel outil de déploiement, et le plus décisif à long terme est l'exportabilité des données brutes : sans elle, pas d'indicateur propre, pas de preuve indépendante, pas de changement de fournisseur sans perte d'antériorité. Sous Windows, les applications tierces échappent au mécanisme natif alors qu'elles concentrent une part majeure des vulnérabilités exploitées sur poste. Sous Linux, la mise à jour automatique sans orchestration des redémarrages produit un parc que l'on croit à jour et qui exécute encore du code vulnérable. Sur les mobiles, on pilote par la politique d'accès plutôt que par le déploiement. Dans le cloud et les conteneurs, le MCS se déplace vers la chaîne de construction, souvent détenue par d'autres équipes. Enfin, additionner les rapports de cinq outils produit un chiffre faux : la consolidation part du périmètre de référence, et son résultat le plus précieux est la liste des actifs couverts par aucun outil.

**Trois questions de vérification**

1. Vous évaluez un outil de déploiement. Quel critère privilégiez-vous pour l'horizon à cinq ans, et quelles trois capacités perdez-vous s'il n'est pas rempli ?
2. Votre parc Linux applique automatiquement les correctifs de sécurité. Quelle vérification faites-vous avant de le considérer comme à jour ?
3. Cinq outils rapportent chacun plus de 95 % de conformité. Pourquoi ne pouvez-vous pas en déduire un taux global, et comment procédez-vous ?

---

### Chapitre 20 — Quand on ne peut pas patcher : les mesures compensatoires

#### 20.1 Taxonomie des impossibilités

« On ne peut pas patcher » recouvre cinq situations très différentes, qui n'appellent ni les mêmes réponses ni les mêmes interlocuteurs. Le premier travail consiste à identifier laquelle vous avez en face de vous.

| Type | Description | Qui peut la lever | Horizon |
|---|---|---|---|
| **Technique** | Le correctif n'existe pas, ou casse une dépendance | L'éditeur | Incertain |
| **Contractuelle** | La garantie ou la certification interdit la modification | Le constructeur, le contrat | Négociable |
| **Métier** | L'interruption n'est pas acceptée | Le propriétaire métier | Négociable |
| **Budgétaire** | La correction suppose une migration non financée | La direction | Cycle budgétaire |
| **Temporelle** | Fenêtre trop éloignée | La planification | Court terme |

⚠️ **PIÈGE — le motif générique**
« C'est un système critique, on ne peut pas y toucher » n'est pas un motif : c'est un refus non qualifié. Exiger le type exact d'impossibilité change la conversation, parce que chaque type a un interlocuteur et un horizon différents. Beaucoup d'impossibilités déclarées techniques se révèlent temporelles ou métier une fois qualifiées.

🖼 **SCHÉMA — Hiérarchie des compensations.** *Pyramide inversée à six rangs, du plus protecteur au moins protecteur, avec le coût récurrent en regard.*

#### 20.2 La hiérarchie des mesures compensatoires

Toutes les compensations ne se valent pas. Voici l'ordre d'efficacité décroissante, à parcourir de haut en bas.

| Rang | Mesure | Effet | Coût récurrent |
|---|---|---|---|
| 1 | **Supprimer l'exposition** | Le chemin d'attaque disparaît, y compris pour les vulnérabilités futures (§11.8) | Nul |
| 2 | **Isoler** | L'actif n'est atteignable que depuis un périmètre restreint | Faible |
| 3 | **Désactiver la fonction vulnérable** | La vulnérabilité n'est plus atteignable | Nul si la fonction est inutile |
| 4 | **Filtrer** | Les tentatives connues sont bloquées en amont | Maintien des règles |
| 5 | **Renforcer la détection** | On ne bloque pas, on voit | **Élevé** — charge d'analyse permanente |
| 6 | **Accepter le risque** | Rien n'est fait, la décision est formalisée | Nul, mais le risque est porté |

**La règle d'or** : ne descendez d'un rang que si le rang supérieur est réellement impossible, et écrivez pourquoi. La majorité des organisations sautent directement au rang 5, qui est le plus coûteux et le moins protecteur — parce que c'est le seul qui ne demande de négociation avec personne.

#### 20.3 La correction virtuelle

Bloquer l'exploitation d'une vulnérabilité en amont de l'actif, sans le modifier : règle de filtrage applicatif, signature de sonde réseau, restriction de protocole.

| Ce que ça apporte | Ce que ça n'apporte pas |
|---|---|
| Un délai — souvent quelques jours à quelques semaines | Une protection durable |
| Une couverture de masse rapide sur plusieurs actifs | Une garantie : les contournements de signature sont fréquents |
| Une trace des tentatives, précieuse en investigation | Une protection contre un attaquant déjà à l'intérieur du périmètre filtré |

📌 **LIMITES** — Une règle de correction virtuelle protège contre les **variantes connues** d'une exploitation. Elle est écrite à partir des exploits observés ; une variante suffisante la contourne. Traitez-la comme un **délai acheté**, jamais comme une correction, et donnez-lui une date d'expiration comme à toute compensation.

#### 20.4 Réduire la surface

Souvent la mesure la plus efficace et la moins employée : la vulnérabilité concerne un composant que vous n'utilisez pas.

**Les quatre gestes**, par ordre d'application :

1. **Désactiver le service** — si personne ne l'utilise, il n'a pas à tourner.
2. **Désactiver le module ou l'extension** vulnérable, quand le service est nécessaire mais pas cette fonction.
3. **Désactiver le protocole** — protocoles hérités, versions anciennes, méthodes d'authentification faibles.
4. **Restreindre les droits** du compte sous lequel s'exécute le service, pour limiter l'effet d'une exploitation réussie.

**La vérification préalable indispensable** : mesurer l'usage réel avant de désactiver. Un service qui semble inutilisé peut porter un traitement mensuel ou une intégration partenaire (§10.5, dépendance temporelle). Observez sur un cycle métier complet.

#### 20.5 Isolation d'urgence : ce qui est faisable en 24 heures

| Mesure | Délai réaliste | Effet | Risque métier |
|---|---|---|---|
| Restreindre l'accès à des plages d'adresses connues | 1 à 4 h | Fort | Faible si le besoin est bien cerné |
| Placer l'actif derrière un accès distant authentifié | 4 à 24 h | Fort | Modéré : change l'usage |
| Couper l'exposition externe | **Minutes** | Total sur ce vecteur | Selon l'usage |
| Isoler dans un segment réseau dédié | Jours à semaines | Fort | Élevé : dépendances à recenser |
| Segmentation générale du réseau | Mois | Structurel | Projet |

**Les trois premières lignes sont réalisables dans la journée** et couvrent la majorité des besoins d'urgence. La segmentation générale est un projet d'architecture : utile, mais elle ne répond pas à une crise en cours.

#### 20.6 La surveillance renforcée comme compensation

Elle est légitime, et son coût est systématiquement sous-estimé.

**Ce qu'elle exige réellement** : une règle de détection écrite et testée, une source de journaux couvrant l'actif, quelqu'un pour analyser les alertes, une procédure de réaction, et une durée de vie définie.

⚠️ **PIÈGE — la surveillance sans destinataire**
Une règle de détection dont les alertes arrivent dans une boîte que personne ne lit ne constitue pas une compensation. C'est la forme la plus courante de compensation fictive : elle coche la case, ne protège de rien, et donne une fausse assurance à toute la chaîne de décision.

**La question à poser avant d'accepter cette compensation** : *qui regarde, quand, et que fait-il exactement s'il voit quelque chose ?* Sans réponse nominative, la mesure n'est pas recevable.

#### 20.7 Les sept attributs obligatoires

C'est le cœur du chapitre, et la règle qui empêche le pourrissement. **Toute mesure compensatoire porte ces sept attributs**, sans exception.

| # | Attribut | Pourquoi |
|---|---|---|
| 1 | **Propriétaire nommé** | Quelqu'un répond de son maintien |
| 2 | **Date de début** | Point de départ du décompte |
| 3 | **Date d'expiration** | Sans elle, la mesure devient permanente par défaut |
| 4 | **Moyen de vérification** | Comment sait-on qu'elle est toujours active ? |
| 5 | **Coût opérationnel** | Charge récurrente, à comparer au coût de la correction |
| 6 | **Condition de sortie** | Quel événement met fin à la compensation |
| 7 | **Contrôle périodique** | Fréquence de la vérification effective |

**Le quatrième attribut est celui qu'on oublie**, et c'est le plus important en pratique. Une règle de filtrage supprimée lors d'une refonte réseau, une isolation annulée par un nouveau routage, une surveillance désactivée lors d'un changement d'outil : la compensation disparaît sans que personne ne le sache, et le risque revient sans qu'aucune alerte ne se déclenche.

✅ **BONNE PRATIQUE (P0)** — Le contrôle périodique de l'existence effective des compensations est un **point d'ordre du jour du comité MCS** (§9.3). Cinq minutes par mois. C'est ce qui distingue une compensation d'une intention.

#### 20.8 Formaliser l'acceptation de risque

Quand aucune compensation n'est possible, reste l'acceptation formelle. Les sept champs de la dérogation (§7.4) s'appliquent, avec trois exigences supplémentaires :

- le **signataire** est le propriétaire métier, à un niveau proportionné à l'enjeu (§9.2) ;
- le **risque est décrit en termes métier**, pas techniques : « une compromission de ce serveur exposerait les données de paie de 1 380 salariés » et non « exécution de code à distance » ;
- la **revue est datée**, et le renouvellement remonte d'un niveau (§7.4).

#### 20.9 ⚠️ Le compensatoire permanent

**La mécanique du pourrissement**, en cinq étapes qui se répètent partout :

```
1. Correction impossible → compensation mise en place, durée 3 mois
2. À 3 mois, rien n'a changé → prolongation « le temps de »
3. La personne qui l'a mise en place change de poste
4. La compensation n'est plus vérifiée : personne ne sait si elle est active
5. Deux ans plus tard, l'actif est considéré comme « traité »
```

**Les trois garde-fous** qui cassent ce cycle : l'attribut n° 4 (moyen de vérification) contrôlé périodiquement ; le renouvellement remontant d'un niveau hiérarchique (§7.4) ; et l'indicateur **âge moyen des compensations actives**, présenté au comité — c'est la mesure la plus honnête de la dette réellement portée par l'organisation.

#### 20.10 🔬 Mini-lab 7 — Rédiger une dérogation auditable

**Objectif** — Produire une fiche complète, défendable en audit, et arbitrer le niveau de signature.
**Durée** 40 min · **Difficulté** 🟠 intermédiaire · **Prérequis** §7.4, §20.2, §20.7, annexe C.4 · **Livrable** formulaire D.4 rempli.
**Compétences validées** — ✔ parcourir la hiérarchie des compensations ✔ écrire un risque en termes métier ✔ choisir le bon signataire ✔ aligner une date d'expiration sur un événement décisionnel ✔ distinguer horloge de risque et horloge de traitement

**Dossier fourni**

| Élément | Donnée |
|---|---|
| Actif | `SRV-CRM-02`, serveur applicatif, environnement production |
| Constat | Vulnérabilité critique sur un composant web · exploitable **à distance sans authentification** · exploitation non observée à ce jour |
| Correction disponible | Oui, mais elle exige la montée en version majeure de l'application métier |
| Coût de la correction | 40 k€ facturés par l'éditeur, **non budgétés sur l'exercice** |
| Délai éditeur | Version compatible disponible sous 3 mois après commande |
| Exposition | Réseau bureautique interne · **non publié sur Internet** |
| Utilisateurs | 60 personnes du service commercial |
| Données | Fichier clients — 2 800 enregistrements, données à caractère personnel |
| Classe de service | C2 · délai politique pour critique non exploitée : 30 jours |
| Journalisation | Accès applicatifs conservés 90 jours, exportés vers la plateforme centrale |
| Contexte | Exercice budgétaire clos ; vote du budget suivant en mars |

**Questions**
(a) Rédigez la fiche D.4 complète.
(b) Qui signe, et pourquoi ?
(c) Quelle date d'expiration retenez-vous, et sur quoi l'alignez-vous ?
(d) Que devient l'horloge de risque pendant la dérogation ?
(e) Quelles conditions de révocation anticipée écrivez-vous ?

---

**Corrigé commenté — fiche D.4 remplie**

| Champ | Contenu |
|---|---|
| **Identifiant** | `DER-2027-018` · version 1.0 · émise le 12/06/2027 |
| **Objet** | `SRV-CRM-02` · vulnérabilité `[identifiant]` sur composant web · correction nécessitant la montée en version majeure de l'application de gestion commerciale |
| **Type d'impossibilité** | ☑ **Budgétaire** — le correctif existe et est techniquement applicable |
| **Analyse de risque, en termes métier** | Un poste bureautique compromis permettrait à un attaquant d'atteindre ce serveur sans authentification et d'accéder au fichier clients : 2 800 enregistrements comportant nom, coordonnées et historique commercial. Conséquences : notification de violation de données, atteinte à la relation client, exposition contractuelle vis-à-vis de trois grands comptes dont le contrat comporte une clause de sécurité. Exploitation non observée à ce jour dans le monde. |
| **Exposition mesurée** | ☑ réseau bureautique — ☐ Internet · joignable depuis 340 postes avant compensation |
| **Exploitation observée** | ☑ non |
| **Mesures compensatoires** | **1.** Restriction d'accès réseau : le serveur n'est joignable que depuis les 60 postes du service commercial (rang 2 de la hiérarchie §20.2). **2.** Règle de filtrage applicatif bloquant les motifs d'exploitation publiés (rang 4). **3.** Alerte sur toute tentative d'accès depuis une origine non autorisée, destinataire nommé (rang 5). **Rangs écartés** : rang 1 — l'exposition interne est nécessaire à l'usage ; rang 3 — la fonction vulnérable est celle utilisée par l'application. |
| **Moyen de vérification** | Test mensuel d'accès depuis un poste hors périmètre autorisé — **doit échouer** · vérification de la présence effective de la règle de filtrage · test d'alerte trimestriel avec accusé de traitement |
| **Fréquence du contrôle** | Mensuelle, inscrite à l'ordre du jour du comité MCS |
| **Coût opérationnel** | ≈ 2 h/mois de vérification + charge d'analyse des alertes |
| **Propriétaire de la compensation** | `[responsable exploitation]` |
| **Signataire** | `[directeur commercial]` — propriétaire métier |
| **Date de début** | 12/06/2027 |
| **Date d'expiration** | **31/03/2028** |
| **Conditions de sortie** | Migration réalisée · **ou** exploitation de cette vulnérabilité observée dans le monde · **ou** compromission avérée d'un poste du service commercial |
| **Conditions de révocation anticipée** | Publication d'un exploit fonctionnel · entrée de la vulnérabilité dans un catalogue d'exploitation avérée · modification de l'exposition du serveur · incident de sécurité touchant le service commercial |
| **Nombre de renouvellements** | 0 |
| **Date de revue** | Trimestrielle — 12/09/2027, 12/12/2027, 12/03/2028 |

**(b) Le signataire — arbitrage**

Le propriétaire métier, ici le directeur commercial. **Trois raisons** :

1. C'est lui qui **porte le risque** : ce sont ses données clients et sa relation commerciale.
2. C'est lui qui **détient le levier** : le budget de 40 k€ relève de son arbitrage ou de son plaidoyer.
3. Faire signer la sécurité lui transférerait un risque qu'elle n'a pas les moyens de porter, et déresponsabiliserait le métier (§9.2).

⚠️ **Le cas limite** : si les données concernées relevaient d'un régime sensible — données de santé, données de paiement —, la grille C.4 imposerait une signature au niveau de la direction générale, indépendamment du fait que l'actif soit interne et de classe C2.

**(c) La date d'expiration**

Le **31 mars 2028**, alignée sur le vote du budget suivant. C'est le point du §7.4 : une date d'expiration doit correspondre à un **événement décisionnel réel**, pas à une durée arbitraire.

| Date envisageable | Évaluation |
|---|---|
| « jusqu'à la migration » | ❌ Ce n'est pas une date. Rejet automatique |
| 12/12/2027 — 6 mois | ⚠️ Tombe avant tout arbitrage budgétaire : le renouvellement sera mécanique |
| **31/03/2028 — vote du budget** | ✅ Le renouvellement coïncide avec le moment où quelque chose peut changer |
| 31/12/2028 | ❌ Trop long : 18 mois sans point de décision |

**(d) L'horloge de risque**

Elle **continue de courir** (§17.5). La dérogation suspend l'horloge de traitement — l'équipe n'est pas en faute — mais le risque est porté chaque jour. Concrètement :

- l'horloge SLA est suspendue au 12/06/2027, avec motif « dérogation `DER-2027-018` » ;
- l'horloge de risque affiche, au comité de décembre, **183 jours de risque porté** ;
- ce chiffre est celui qui apparaît au tableau de bord de direction, pas le taux de respect des délais.

C'est ce qui empêche la dérogation de rendre le retard invisible.

**(e) Les conditions de révocation anticipée**

Elles sont distinctes des conditions de sortie : la sortie met fin à la dérogation parce que le problème est résolu ; la **révocation** y met fin parce que l'hypothèse sur laquelle elle reposait a changé. Ici, l'hypothèse centrale est *« exploitation non observée »*. Les quatre conditions écrites la surveillent directement.

**Les quatre erreurs attendues**
1. Pas de date d'expiration, ou date exprimée comme un événement flou.
2. Compensations non vérifiables — « surveillance renforcée » sans destinataire ni test (§20.6).
3. Signature par la sécurité au lieu du métier.
4. Risque décrit en termes techniques — « exécution de code à distance » ne permet à aucun directeur commercial de décider en connaissance de cause.

#### 20.11 🔴 FIL ROUGE — juin 2027 : la ligne 2 de Saint-Étienne

Une vulnérabilité activement exploitée est publiée sur le système de supervision de la ligne d'assemblage 2 — le constat n° 5 du mini-lab 4, désormais réel. Classe C4.

**Les faits.** Le correctif existe. Le constructeur ne l'a pas validé pour la configuration installée ; l'appliquer sans validation fait tomber la garantie et invalide la qualification du procédé, ce qui a des conséquences réglementaires sur la production de dispositifs médicaux. Le prochain arrêt de production est en novembre — cinq mois.

**Le parcours de la hiérarchie du §20.2.**

| Rang | Examiné ? | Résultat |
|---|---|---|
| 1 — Supprimer l'exposition | Oui | Le poste n'est pas exposé à Internet. Déjà acquis |
| 2 — **Isoler** | **Oui** | **Retenu** : le poste communiquait avec le réseau bureautique pour un export de données de production. L'export est basculé en dépôt de fichiers unidirectionnel |
| 3 — Désactiver la fonction | Oui | Impossible : la fonction vulnérable est celle utilisée par la supervision |
| 4 — **Filtrer** | **Oui** | **Retenu** : règle de filtrage sur le conduit entre zones industrielles |
| 5 — Détection renforcée | Oui | Retenue en complément, avec destinataire nommé et procédure |
| 6 — Accepter | — | Non atteint |

**Ce qui a rendu la solution possible.** Thomas Berger savait que l'export vers la bureautique n'était plus utilisé depuis dix-huit mois — l'outil qui le consommait avait été remplacé. Personne n'avait jamais posé la question. La suppression de ce flux, décidée en vingt minutes, retire le principal chemin d'accès au poste.

**La fiche produite.** Compensation valable jusqu'au 30 novembre 2027, date de l'arrêt de production. Propriétaire : Thomas Berger. Vérification mensuelle : test d'accès depuis le réseau bureautique — doit échouer — et contrôle de la règle de filtrage. Signataire : le directeur industriel. Condition de sortie : correctif validé par le constructeur et appliqué pendant l'arrêt de novembre.

**Le point que Claire Nadeau porte au comité.** La compensation n'est pas un pis-aller subi : dans ce cas précis, l'isolation obtenue est **plus protectrice que le correctif** n'aurait été, puisqu'elle protège aussi contre les vulnérabilités futures du même poste (§11.8). Elle sera maintenue **après** l'application du correctif en novembre.

**Livrable de l'épisode.** La fiche de compensation avec ses sept attributs, et une revue systématique des flux entrants des postes de supervision — qui révélera en juillet trois autres flux devenus inutiles.

→ La suite en 🔴 §21.11, quand une vulnérabilité sur la passerelle d'accès distant ne laissera pas cinq mois pour décider.

→ **Chapitre 21 — Crise vulnérabilité : la cinétique 24 h / 72 h / 30 j** : réagir quand tout s'accélère.

#### Synthèse mentale du chapitre 20

« On ne peut pas patcher » recouvre cinq impossibilités distinctes, avec des interlocuteurs et des horizons différents : les qualifier change la conversation, et beaucoup d'impossibilités déclarées techniques se révèlent temporelles ou métier. La hiérarchie des compensations se parcourt de haut en bas — supprimer l'exposition, isoler, désactiver, filtrer, détecter, accepter — et l'on ne descend d'un rang qu'en écrivant pourquoi le précédent est impossible. La plupart des organisations sautent directement à la détection renforcée, la plus coûteuse et la moins protectrice, parce qu'elle ne demande de négociation avec personne. La correction virtuelle achète un délai, jamais une protection durable. Sept attributs rendent une compensation réelle, dont le moyen de vérification, celui qu'on oublie et qui empêche la disparition silencieuse de la mesure. Enfin, une compensation bien choisie peut être plus protectrice qu'un correctif, puisqu'elle couvre aussi les vulnérabilités futures du même actif.

**Trois questions de vérification**

1. Un exploitant vous répond « c'est un système critique, on ne peut pas y toucher ». Quelle est votre question suivante, et pourquoi change-t-elle la nature de la discussion ?
2. Pourquoi la surveillance renforcée est-elle simultanément la compensation la plus choisie et la moins protectrice ?
3. Une compensation mise en place il y a dix-huit mois est-elle encore active ? Comment le savez-vous, et qu'auriez-vous dû prévoir au moment de la décision ?

---

### Chapitre 21 — Crise vulnérabilité : la cinétique 24 h / 72 h / 30 j

#### 21.1 Ce qui distingue une crise vulnérabilité d'un incident

| | Crise vulnérabilité | Incident de sécurité |
|---|---|---|
| Point de départ | Une faille est publiée ou exploitée **ailleurs** | **Vous** êtes touché |
| Question centrale | Suis-je exposé, et depuis quand ? | Que s'est-il passé, et jusqu'où ? |
| Objectif | Réduire l'exposition avant d'être atteint | Contenir, éradiquer, reconstruire |
| Horloge | Course contre l'automatisation des attaques | Course contre la progression de l'attaquant |

**Le lien entre les deux, et il est essentiel** : une crise vulnérabilité sur un actif exposé depuis plusieurs jours **peut déjà être un incident** sans que vous le sachiez. C'est le §21.3, et c'est ce qui distingue une réaction professionnelle d'une réaction naïve.

#### 21.2 L'échelle de qualification en cinq niveaux

Toutes les vulnérabilités graves ne déclenchent pas une crise. Cinq niveaux, avec une réponse propre à chacun.

| Niveau | Situation | Réponse |
|---|---|---|
| **1** | Vulnérabilité critique, aucune preuve d'exploitation | Processus normal, délai de la classe de service |
| **2** | Exploitation active observée dans le monde | Accélération : arbre de décision, feuille « urgence » (§16.3) |
| **3** | Exploitation observée **dans votre secteur** | Déclenchement de la cellule, hypothèse de ciblage |
| **4** | Indices de compromission **chez vous** | Bascule en gestion d'incident |
| **5** | **Journalisation insuffisante pour conclure** | **Traiter comme le niveau 4 jusqu'à preuve du contraire** |

Le niveau 5 est celui que les organisations traitent le plus mal, parce qu'il n'y a rien à voir — et l'absence de signal est confondue avec l'absence d'événement.

#### 21.3 La règle qu'il faut enseigner explicitement

> **L'absence de preuve de compromission n'est pas la preuve de l'absence de compromission — a fortiori quand la journalisation est insuffisante.**

**Pourquoi c'est capital en pratique.** Après la publication d'un exploit sur un équipement exposé, la question n'est pas seulement « corrigeons-nous ? » mais « avons-nous déjà été atteints ? ». Corriger ferme la porte ; cela ne fait pas sortir celui qui serait entré avant. Sur les équipements de bordure en particulier, les compromissions **persistent au-delà du correctif** : implants dans le micrologiciel, comptes créés, configurations modifiées, sessions volées.

**Les trois questions à poser dès la première heure :**

1. Depuis combien de temps cet actif est-il exposé et vulnérable ?
2. De quels journaux disposons-nous sur cette période, et à quelle granularité ?
3. Ces journaux permettraient-ils de **détecter** ce type d'exploitation, ou seulement de constater une indisponibilité ?

Si la réponse à la troisième question est négative, vous êtes au niveau 5. Il faut le dire dans ces termes à la direction : *« nous ne pouvons pas établir que nous n'avons pas été compromis »*. C'est une formulation inconfortable, et c'est la seule honnête.

#### 21.4 Critères de déclenchement

Écrits à l'avance, sans discussion possible au moment des faits :

```
DÉCLENCHEMENT DE LA CELLULE si TOUTES ces conditions sont réunies :
   · vulnérabilité activement exploitée (source vérifiée)
   · au moins un actif du périmètre est affecté
   · cet actif est exposé à Internet OU de niveau 0 OU critique métier

DÉCLENCHEMENT si l'une de ces conditions est réunie :
   · indices de compromission sur un actif affecté
   · impossibilité d'établir l'absence de compromission (niveau 5)
   · demande d'une autorité ou d'un client majeur
```

#### 21.5 La cellule de crise vulnérabilité

**Composition minimale** : un pilote qui décide et arbitre, un responsable technique qui conduit les actions, un référent métier pour les décisions d'interruption, un référent communication, et un **greffier** dont le seul rôle est de tenir le journal.

**Le rythme** : points fixes toutes les deux heures les premières douze heures, puis toutes les quatre à six heures. Points courts — dix minutes — avec trois questions invariables : qu'a-t-on appris, que décide-t-on, qui fait quoi d'ici au prochain point.

**Le journal de décision** est le livrable central de la crise. Pour chaque entrée : horodatage, information reçue et sa source, décision prise, décideur, action engagée. Il sert pendant la crise à éviter les redites et les contradictions ; après, il constitue la preuve, la base du retour d'expérience, et l'élément qui vous protège si les décisions sont contestées.

⚠️ **PIÈGE — le greffier improvisé**
Sans rôle dédié, personne ne tient le journal : tout le monde agit. Trois jours plus tard, il est impossible de reconstituer qui a décidé quoi, quand, et sur quelle information. Le greffier est le rôle le plus facile à supprimer sous pression, et celui dont l'absence coûte le plus cher après.

#### 21.6 Les six premières heures

| Heure | Action | Livrable |
|---|---|---|
| H+0 | Vérifier l'information à la source (avis éditeur, pas un article de presse) | Constat qualifié (§14.7) |
| H+0 à H+1 | **Mesurer l'exposition** : quels actifs, joignables d'où, depuis quand | Liste nominative |
| H+1 | Vérifier l'existence d'un correctif et d'un contournement officiel | Options disponibles |
| H+1 à H+2 | **Décider d'une mesure d'urgence** : fermeture d'exposition en priorité (§11.8) | Décision tracée |
| H+2 à H+4 | Engager la recherche de compromission préalable (§21.7) | Périmètre d'investigation |
| H+4 à H+6 | Informer la direction, préparer la communication | Note de situation |

**La décision la plus fréquente et la plus efficace à H+2** n'est pas d'appliquer le correctif — il n'est pas toujours disponible, testé ni déployable en deux heures. C'est de **fermer l'exposition** : couper la publication Internet, restreindre à des plages d'adresses connues, désactiver le service. Quelques minutes, réversible, et cela arrête l'horloge.

#### 21.7 La recherche de compromission préalable

**L'hypothèse de travail par défaut**, pour tout équipement de bordure exposé et exploité : *considérer qu'une compromission a pu avoir lieu, jusqu'à preuve raisonnable du contraire.*

**Les cinq vérifications de premier niveau :**

| Vérification | Ce qu'on cherche |
|---|---|
| Comptes | Comptes créés, modifiés, réactivés depuis la date d'exposition |
| Configuration | Écarts par rapport à la référence (§22.3) : règles, redirections, accès |
| Persistance | Tâches planifiées, services, scripts de démarrage inconnus |
| Journaux d'accès | Connexions depuis des origines inhabituelles, horaires atypiques |
| Trafic sortant | Communications vers des destinations inhabituelles |

**Quand basculer en gestion d'incident** : dès qu'une de ces vérifications produit un résultat non explicable. La bascule est une décision du pilote de cellule, et elle change la nature des opérations — l'objectif devient la préservation des traces et la reconstruction, ce qui peut **contredire** l'urgence de correction. Ce point doit être compris à l'avance : sur un équipement compromis, appliquer le correctif peut détruire les preuves.

#### 21.8 Le correctif d'urgence

**Le principe.** Contourner le processus normal sans détruire ce qui le rend fiable.

| Étape normale | En urgence |
|---|---|
| Délai d'observation | **Supprimé** — le calcul de risque s'inverse (§18.11) |
| Validation en recette | Réduite à un test fonctionnel minimal |
| Anneaux | Conservés, mais compressés : pilote de quelques heures |
| Critères d'arrêt | **Conservés intégralement** — c'est ce qui rend la compression acceptable |
| Plan de retour arrière | **Conservé intégralement** |
| Demande de changement | Émise **a posteriori**, sous 48 h, avec le journal de décision |
| Preuve | Conservée intégralement |

**Ce qu'on ne supprime jamais** : les critères d'arrêt, le retour arrière et la preuve. Ce sont les trois éléments qui permettent de se tromper sans catastrophe — précisément ce dont on a besoin quand on va vite.

#### 21.9 Communication

| Destinataire | Quand | Contenu |
|---|---|---|
| Direction générale | H+4 à H+6 | Situation, exposition, décisions prises, ce qui n'est pas encore su |
| Métiers concernés | Avant toute interruption | Ce qui va être coupé, quand, pour combien de temps |
| Utilisateurs | Si effet visible | Fait, durée, contournement |
| Clients | Si leur service est affecté, ou si contractuellement prévu | Factuel, sans spéculation |
| Assureur | Selon contrat, souvent sous 48-72 h | Déclaration conservatoire |
| Autorités | Selon obligations applicables (ch. 8, ch. 33) | Délais réglementaires, à connaître **avant** |

⚠️ **PIÈGE — annoncer trop tôt une conclusion**
« Nous n'avons pas été compromis » prononcé à H+6 est presque toujours prématuré, et devient très difficile à corriger si l'investigation dit l'inverse. Formulation à privilégier : *« à ce stade, les vérifications réalisées n'ont pas mis en évidence de compromission ; l'investigation se poursuit »*.

#### 21.10 Sortie de crise et retour d'expérience

**Les critères de sortie**, à énoncer explicitement : correctif appliqué et vérifié sur l'ensemble du périmètre affecté · recherche de compromission conclue · mesures d'urgence soit levées, soit converties en compensations formelles (§20.7) · communication close.

**Le retour d'expérience utile** tient en cinq questions, et il porte sur le processus, jamais sur les personnes :

1. Quel a été le **délai de détection** — entre la publication et notre prise de connaissance ?
2. Quel a été le **délai de mesure d'exposition** — et pourquoi ?
3. Quelle information nous a **manqué**, et comment l'obtenir la prochaine fois ?
4. Quelle décision a été **retardée**, et par quel manque de mandat ?
5. Que faut-il **pré-arbitrer** pour ne plus reprendre cette discussion à chaud (§9.4) ?

#### 21.11 🔴 FIL ROUGE — juillet 2027 : ce que la passerelle avait vécu

Le 9 juillet 2027, un avis constructeur publie une vulnérabilité critique sur la passerelle d'accès distant d'HELIOMED. Exploitation active confirmée dans les heures qui suivent.

**H+0 — la qualification.** Malik Ferhaoui vérifie à la source. La version installée est affectée. Un correctif existe depuis six heures.

**H+1 — l'exposition.** L'interface d'administration a été fermée en septembre 2026 (§11.12). Le service d'accès distant lui-même, lui, reste nécessairement publié : c'est sa fonction. 210 collaborateurs l'utilisent quotidiennement.

**H+2 — la décision.** Fermer l'exposition signifierait couper l'accès distant de 210 personnes un mercredi matin. Claire Nadeau applique le pré-arbitrage du §9.4 : le seuil d'urgence autorise l'interruption sur décision du propriétaire technique. Elle ne coupe pas — elle **restreint** : accès limité aux plages d'adresses des sites HELIOMED et aux connexions déjà établies, le temps du correctif. Sept collaborateurs en déplacement sont impactés et prévenus individuellement.

**H+3 — la question qui change tout.** Le greffier note une remarque de Malik : *« depuis quand cette version est-elle installée ? »* Réponse : mars 2022. Et l'interface d'administration, celle qui porte la fonction vulnérable, a été publiée sur Internet de mars 2022 à septembre 2026 — **quatre ans et demi**.

La vulnérabilité publiée aujourd'hui existait dans le code depuis la version de 2021.

**H+4 — le niveau 5.** Claire pose les trois questions du §21.3. Les journaux de la passerelle sont conservés 30 jours. Il n'existe **aucune donnée** sur la période 2022-2026. La question « avons-nous été compromis pendant ces quatre ans et demi ? » n'a pas de réponse possible.

Elle informe Pierre Vasseur dans ces termes exacts : *nous ne pouvons pas établir que nous n'avons pas été compromis.* C'est la phrase la plus difficile de tout le fil rouge, et c'est la seule honnête.

**H+6 à J+3 — les opérations.** Correctif appliqué la nuit suivante, en urgence, avec critères d'arrêt et retour arrière conservés. Recherche de compromission sur les cinq axes du §21.7 : deux comptes locaux non documentés sont découverts sur la passerelle. Leur date de création n'est pas déterminable. Ils sont supprimés, et l'équipement est intégralement reconstruit à partir d'une configuration de référence plutôt que corrigé — décision prise en application du §21.7.

**J+3 à J+30.** Investigation étendue : recherche des mêmes indicateurs sur les actifs joignables depuis la passerelle, rotation complète des secrets susceptibles d'avoir transité, revue des accès distants. Aucune trace d'activité malveillante n'est établie — ce qui, comme le rappelle Claire au comité, ne prouve rien sur la période non journalisée.

**Les quatre décisions structurelles issues du retour d'expérience.**

1. **Journalisation** : conservation portée à 12 mois pour tous les actifs de bordure et de niveau 0, avec export vers un système indépendant de l'équipement.
2. **Doctrine de version** sur les équipements de bordure : au plus N-1, revue trimestrielle, avec date (§2.7).
3. **Reconstruction plutôt que correction** pour tout équipement de bordure ayant subi une exploitation potentielle.
4. **Pré-arbitrage complété** : le seuil d'urgence distingue désormais *restreindre* et *couper*, avec un décideur différent pour chacun.

**Ce que Claire écrit en conclusion du retour d'expérience**, et qui vaut pour tout le cours : *la crise de juillet 2027 n'a pas commencé le 9 juillet. Elle a commencé en mars 2022, le jour où une exposition temporaire n'a pas été refermée, et où personne n'a écrit de date de fin.*

→ Le scénario complet, avec ses données et ses décisions à prendre, constitue le **cas de synthèse A**.

→ **Chapitre 22 — Durcissement et référentiels de configuration** : la configuration, qui annule l'effet des correctifs quand elle est mauvaise.

#### Synthèse mentale du chapitre 21

Une crise vulnérabilité se distingue d'un incident par son point de départ, mais l'une peut être l'autre sans que vous le sachiez : sur un actif exposé depuis plusieurs jours, la question n'est pas seulement « corrigeons-nous » mais « avons-nous déjà été atteints ». Cinq niveaux de qualification, dont le cinquième — journalisation insuffisante pour conclure — se traite comme une compromission probable. L'absence de preuve de compromission n'est pas la preuve de l'absence de compromission, et cette phrase doit pouvoir être prononcée devant une direction. La décision la plus efficace des deux premières heures n'est pas d'appliquer le correctif mais de fermer ou restreindre l'exposition : quelques minutes, réversible, et l'horloge s'arrête. En urgence, on comprime le délai d'observation et la validation, jamais les critères d'arrêt, le retour arrière et la preuve — ce sont eux qui permettent de se tromper sans catastrophe. Enfin, sur un équipement de bordure potentiellement compromis, corriger ne suffit pas : on reconstruit.

**Trois questions de vérification**

1. Un équipement exposé porte une vulnérabilité exploitée depuis trois semaines. Quelles trois questions posez-vous avant même de parler du correctif, et que faites-vous si la réponse à la troisième est négative ?
2. Quelles étapes du processus normal comprimez-vous en urgence, lesquelles conservez-vous intégralement, et pourquoi cette distinction précise ?
3. Votre direction vous demande à H+6 si vous avez été compromis. Formulez la réponse exacte que vous donnez, et expliquez pourquoi chaque mot compte.

---

---

> ### 🎓 À ce stade de la Partie III, vous savez…
>
> - **construire** une veille à partir de l'inventaire, et faire entrer tous les constats — pentest, audit, configuration, secret, obsolescence — dans une file unique ;
> - **interpréter** un rapport de scan, calculer une couverture honnête, et ne jamais confondre « non détecté », « non vulnérable » et « non scanné » ;
> - **prioriser** par arbre de décision plutôt que par seuil de gravité, et défendre une dépriorisation devant un comité ;
> - **piloter** un constat de bout en bout : parent et occurrences, deux horloges, escalade automatique, preuve par type d'issue ;
> - **conduire** une campagne : qualification en six questions, anneaux représentatifs, critères d'arrêt chiffrés, retour arrière chronométré, traîne longue qualifiée ;
> - **compenser** quand corriger est impossible, en parcourant la hiérarchie de haut en bas et en attachant les sept attributs ;
> - **conduire** une crise vulnérabilité, y compris quand la journalisation ne permet pas de conclure.
>
> **Ce que vous ne savez pas encore** : tout ce qui se dégrade en dehors des versions logicielles. C'est l'objet de la Partie IV.


## PARTIE IV — Configuration, dépendances et couches oubliées

La Partie III traitait la chaîne de correction des versions. Cette partie traite tout le reste de ce qui se dégrade : les configurations, les identités, les secrets, la cryptographie, le code applicatif et ses dépendances, les couches intermédiaires, les couches basses, et les environnements que personne ne regarde.

C'est ici que se joue la différence entre un programme de gestion des correctifs et un véritable maintien en condition de sécurité.

---

### Chapitre 22 — Durcissement et référentiels de configuration

#### 22.1 Pourquoi une version à jour mal configurée reste vulnérable

Un correctif supprime un défaut de code. Il ne touche pas à la façon dont vous avez configuré le produit — et l'essentiel des compromissions réelles emprunte des chemins de configuration, pas des failles de code (§11.4).

**Les cinq configurations qui annulent l'effet de tous vos correctifs :**

| Configuration | Effet |
|---|---|
| Protocole ou méthode d'authentification héritée laissée active | Contournement possible des protections modernes |
| Compte par défaut conservé, ou mot de passe local identique partout | Propagation immédiate d'une compromission |
| Service exposé qui n'a pas besoin de l'être | Surface d'attaque inutile (ch. 11) |
| Droits excessifs sur un compte de service | Transforme une intrusion mineure en compromission majeure |
| Journalisation absente ou insuffisante | Interdit toute investigation (§21.3) |

**Le rapport coût/effet est très favorable** : ces cinq points se traitent par configuration, sans fenêtre de correction, sans risque de régression majeure, et une fois pour toutes.

#### 22.2 Choisir et adapter un référentiel

| Type de référentiel | Origine | Caractéristique |
|---|---|---|
| Guides d'agences nationales | Autorités publiques | Contexte réglementaire proche, souvent en français, exigences justifiées |
| Référentiels communautaires | Consortiums | Très détaillés, couverture large, niveaux de sévérité gradués |
| Guides de durcissement gouvernementaux | Administrations | Les plus stricts, parfois inapplicables en entreprise |
| Guides constructeurs | Éditeurs | Fiables sur le produit, silencieux sur ce qui gêne le produit |

**La méthode d'adoption, en quatre étapes :**

1. **Choisir un référentiel de base** — n'en cumulez pas plusieurs, vous produiriez des exigences contradictoires.
2. **Le dériver** : chaque point est retenu, adapté ou écarté, et **chaque écart est motivé par écrit**. C'est ce document dérivé qui devient votre référence, pas le référentiel d'origine.
3. **Le versionner** : votre *baseline* est un artefact avec un numéro de version, un propriétaire et une date de revue.
4. **Le décliner par classe de service** : un niveau d'exigence pour C1, un autre pour C3.

⚠️ **PIÈGE — appliquer un référentiel sans dérivation**
Un référentiel appliqué intégralement, sans adaptation, produit systématiquement des ruptures fonctionnelles. L'équipe désactive alors les contrôles gênants un par un, sans les documenter, et la *baseline* devient une fiction. **La dérivation motivée n'est pas un affaiblissement : c'est ce qui rend la baseline applicable, donc réellement appliquée.**

#### 22.3 Construire et maintenir une *baseline*

| Élément | Contenu |
|---|---|
| Référentiel source | Nom et version |
| Périmètre | Quels systèmes, quelles classes |
| Points retenus | Avec leur paramétrage exact |
| **Écarts motivés** | Point écarté, raison, risque accepté, revue |
| Méthode d'application | Modèle, script, politique centralisée |
| Méthode de contrôle | Comment on vérifie |
| Propriétaire et revue | Nom, fréquence |

**La question du niveau d'exigence** se tranche par classe de service, jamais globalement. Une exigence appliquée uniformément à tout le parc sera soit trop faible pour les actifs critiques, soit inapplicable aux actifs courants.

#### 22.4 Automatiser le contrôle

Trois familles de mécanismes, complémentaires :

| Mécanisme | Principe | Fréquence réaliste |
|---|---|---|
| **Contrôle par script ou format standardisé** | Vérification périodique de chaque point de la *baseline* | Hebdomadaire à mensuelle |
| **Politiques centralisées natives** | La plateforme applique et vérifie en continu | Continu |
| **Contrôle dans la chaîne de construction** | L'image est vérifiée avant d'être publiée | À chaque construction |

**Le troisième est le plus efficace** : contrôler à la construction empêche la non-conformité d'exister, plutôt que de la constater après coup. C'est la traduction du principe du §10.7 — traiter à la source plutôt que rattraper.

#### 22.5 Mesurer la conformité de configuration

**Deux mesures distinctes, à ne jamais fondre en un seul chiffre.**

Une *instance de contrôle* est la vérification d'un point de la *baseline* sur un actif donné. Si votre *baseline* comporte 80 points applicables et que vous contrôlez 120 serveurs, vous évaluez 9 600 instances.

```
                         Instances de contrôle conformes
Conformité (%)  =  ──────────────────────────────────────── × 100
                        Instances de contrôle applicables

                         Actifs éligibles effectivement évalués
Couverture (%)  =  ──────────────────────────────────────────── × 100
                         Actifs éligibles du périmètre
```

**Quatre valeurs à publier ensemble**, faute de quoi le chiffre ne veut rien dire :

| Valeur | Rôle |
|---|---|
| **Couverture** | Sur quelle part du périmètre éligible la mesure porte-t-elle |
| **Conformité dans la population mesurée** | L'état de ce qui a été évalué |
| **Points critiques non conformes** | En **valeur absolue**, sans pondération : dix écarts mineurs et un compte administrateur par défaut ne se compensent pas |
| **Actifs non évaluables** | Avec leur motif — non applicable, injoignable, exclu documenté |

⚠️ Le dénominateur de la conformité porte sur les points **applicables après dérivation** (§22.2), pas sur ceux du référentiel d'origine. Un point écarté et motivé n'est pas une non-conformité : il ne fait pas partie de la population éligible.

#### 22.6 ⚠️ Le durcissement qui casse la production

C'est le principal frein à l'adoption, et il est légitime : contrairement à un correctif, un durcissement modifie **intentionnellement** le comportement du système.

**La méthode qui fonctionne**, en cinq étapes :

1. **Mesurer avant d'appliquer.** Beaucoup de contrôles peuvent être évalués en mode observation : on journalise ce qui serait bloqué, sans bloquer.
2. **Appliquer par lots** de points, pas la *baseline* entière d'un coup — sinon un incident ne peut être imputé à aucun point précis.
3. **Utiliser les anneaux** du §18.4 : le durcissement est un changement comme un autre.
4. **Prévoir le retour arrière** point par point.
5. **Documenter les écarts découverts** : un point qui casse une application métier devient un écart motivé, pas un contrôle silencieusement désactivé.

#### 22.7 📌 Limites

- **Les référentiels génériques ne couvrent pas les applications métier**, qui portent souvent les configurations les plus risquées. Pour elles, il faut construire ses propres points de contrôle.
- **Le coût de maintenance d'une baseline** est réel : chaque version majeure du système la rend partiellement obsolète.
- **La conformité de configuration ne dit rien de l'exposition.** Un serveur parfaitement durci mais publié inutilement reste un problème (ch. 11).
- **Le durcissement ne remplace pas les correctifs**, et l'inverse est également vrai. Ce sont deux couches distinctes.

#### 22.8 ✅ Recommandations priorisées

| Prio | Action |
|---|---|
| **P0** | Traiter les cinq configurations du §22.1 sur les actifs C1, indépendamment de toute *baseline* complète |
| **P0** | Mots de passe d'administration locaux uniques par machine |
| **P0** | Désactiver les protocoles et méthodes d'authentification hérités, après mesure en mode observation |
| P1 | Dériver une *baseline* versionnée à partir d'un référentiel unique, avec écarts motivés |
| P1 | Contrôle automatisé mensuel, avec indicateur de points critiques non conformes |
| P1 | Intégrer le contrôle de configuration à la chaîne de construction des images |
| P2 | Étendre aux applications métier avec des points de contrôle propres |

→ **Chapitre 23 — Dérive de configuration, IaC et immutabilité** : la dérive, propriété inévitable des systèmes vivants.

#### Synthèse mentale du chapitre 22

Un correctif supprime un défaut de code, il ne touche pas à votre configuration — et l'essentiel des compromissions réelles emprunte des chemins de configuration. Cinq réglages annulent à eux seuls l'effet de tous vos correctifs, et ils se traitent sans fenêtre ni risque majeur. N'adoptez qu'un seul référentiel de base, et dérivez-le en motivant chaque écart : la dérivation n'affaiblit pas la baseline, c'est ce qui la rend applicable donc réellement appliquée. Contrôler à la construction empêche la non-conformité d'exister plutôt que de la constater. Mesurez séparément les points critiques non conformes, car dix écarts mineurs ne compensent pas un compte administrateur par défaut. Enfin, un durcissement modifie intentionnellement le comportement du système : il s'applique par lots, en anneaux, après mesure en mode observation.

**Trois questions de vérification**

1. Votre parc est parfaitement à jour et un attaquant progresse quand même du poste bureautique jusqu'à la console de sauvegarde. Quelles configurations examinez-vous en premier ?
2. Pourquoi appliquer un référentiel de durcissement sans dérivation produit-il presque toujours une baseline fictive ?
3. Vous affichez 94 % de conformité de configuration. Quelles trois précautions de calcul devez-vous avoir prises pour que ce chiffre signifie quelque chose ?

---

### Chapitre 23 — Dérive de configuration, IaC et immutabilité

#### 23.1 Les mécanismes de la dérive

Une configuration conforme le jour J ne le reste pas. Six mécanismes la dégradent, tous parfaitement légitimes pris isolément :

| Mécanisme | Illustration |
|---|---|
| **Intervention manuelle** | Un paramètre modifié pour résoudre un problème, jamais reversé |
| **Résolution d'urgence** | Un contrôle désactivé pendant un incident, jamais réactivé |
| **Intervention d'un prestataire** | Un tiers applique sa propre configuration de référence |
| **Mise à jour applicative** | L'installeur remet des valeurs par défaut |
| **Restauration** | Retour à un état antérieur à un durcissement |
| **Nouveau projet** | Une exigence projet contredit la *baseline*, sans arbitrage |

**Le point commun** : aucun de ces mécanismes n'est malveillant ni négligent. La dérive n'est pas un problème de discipline, c'est une propriété des systèmes vivants. Elle se traite par la détection et la convergence, pas par la réprimande.

#### 23.2 Détecter la dérive

| Méthode | Principe | Signal / bruit |
|---|---|---|
| **Contrôle de conformité périodique** | Rejouer les points de la *baseline* (§22.4) | Bon, si la *baseline* est bien dérivée |
| **Empreinte de configuration** | Comparer un état complet à une référence | Bruit élevé : tout change tout le temps |
| **Détection de changement en temps réel** | Alerter sur modification de fichiers ou de paramètres sensibles | Excellent si le périmètre est **étroit** |
| **Comparaison code / réalité** | Écart entre la description et l'existant | Bon, limité au périmètre décrit |

⚠️ **PIÈGE — la détection de changement à périmètre trop large**
Surveiller « toutes les modifications de configuration » produit des milliers d'alertes quotidiennes légitimes, que personne ne traite. Ciblez : comptes à privilèges, règles de filtrage, paramètres d'authentification, tâches planifiées, points de démarrage. Vingt éléments bien choisis valent mieux que la surveillance exhaustive.

#### 23.3 Corriger par convergence

Un outil de gestion de configuration applique un état désiré et le **réapplique périodiquement**. La dérive est corrigée automatiquement, sans intervention.

| Bénéfice | Effet pervers correspondant |
|---|---|
| La configuration revient toujours à la référence | Une correction manuelle légitime est écrasée sans prévenir |
| L'état désiré est documenté dans le code | Le code devient un actif critique à maintenir (§3.5) |
| Le déploiement est reproductible | Une erreur dans le code se propage à tout le parc en quelques minutes |
| L'écart est mesurable | Ce qui n'est pas décrit n'est pas surveillé — et donne une fausse assurance |

**Les deux règles qui évitent les effets pervers** : appliquer le code de configuration **par anneaux**, comme tout déploiement (§18.4) ; et prévoir un mécanisme d'exclusion explicite et tracé pour les actifs devant diverger temporairement.

#### 23.4 L'approche immuable

Ne jamais modifier un système en fonctionnement : reconstruire et remplacer (§3.5, §6.10).

**Ce que cela change pour la dérive** : elle devient **impossible par construction** sur la durée de vie de l'instance, qui est courte. Une instance vit quelques jours ou semaines, puis est remplacée par une instance neuve issue d'une image à jour et conforme.

**Les trois conditions de faisabilité**, souvent sous-estimées : les données doivent être externalisées de l'instance ; la reconstruction doit être automatisée et rapide ; et l'application doit tolérer le remplacement de ses instances.

**Le déplacement du problème** : la conformité se joue entièrement dans la **construction de l'image**. C'est là que doivent porter les contrôles (§22.4), et c'est là qu'un défaut se propage à l'ensemble du parc.

#### 23.5 Le MCS du code d'infrastructure

Le code qui décrit votre infrastructure est lui-même un actif :

| Objet | Ce qui se dégrade | Traitement |
|---|---|---|
| Modules réutilisés | Vulnérabilités, abandon du mainteneur | Versionnement, revue, mise à jour périodique (ch. 25) |
| Connecteurs vers les fournisseurs | Fins de support, changements d'interface | Suivi des versions supportées |
| Fichier d'état | Contient des secrets, décrit toute l'infrastructure | **Actif de niveau 0** : chiffrement, accès restreint, journalisation |
| Écart code / réalité | Ressources créées à la main | Détection périodique et réconciliation |

⚠️ **PIÈGE — l'illusion de maîtrise**
Un environnement décrit par du code **donne le sentiment** d'être maîtrisé. Mais si 30 % des ressources ont été créées manuellement en dehors du code, la description est fausse — et plus dangereusement fausse qu'une absence de description, parce qu'on lui fait confiance.

#### 23.6 Gérer les exceptions et les actifs non convergeables

Certains actifs ne peuvent pas converger : systèmes industriels, appliances fermées, applications imposant une configuration propre, matériel spécialisé.

**Le traitement** : les identifier explicitement, les rattacher à la classe C4 (§7.2), leur appliquer un contrôle manuel périodique documenté, et **les compter séparément** dans les indicateurs. Ce qui n'est pas acceptable, c'est qu'ils disparaissent silencieusement du périmètre contrôlé — c'est le mécanisme de l'exclusion silencieuse du §15.6.

#### 23.7 🔴 FIL ROUGE — août 2027 : le serveur d'impression de 2019

Le premier contrôle de conformité automatisé d'HELIOMED, déployé sur les 176 serveurs internes, remonte un résultat global de 87 % — et sept serveurs sous 40 %.

**Le cas le plus instructif** : SRV-PRINT-01, serveur d'impression, 31 % de conformité. L'analyse retrace son histoire.

En novembre 2019, un incident bloque les impressions du siège pendant une demi-journée. Pour rétablir le service, l'administrateur de l'époque — parti depuis — élargit les droits d'un compte de service, désactive deux contrôles d'authentification, et ouvre l'accès depuis l'ensemble du réseau. Le service repart. L'incident est clos.

Rien n'a été reversé. Huit ans plus tard, le compte de service dispose de droits d'administration sur 34 serveurs, l'authentification héritée est toujours active, et le serveur est joignable depuis n'importe quel poste du groupe.

**Ce que révèle le croisement avec le chapitre 11.** SRV-PRINT-01 apparaît dans la matrice des chemins d'attaque comme **étape intermédiaire de trois chemins distincts** menant à des actifs de niveau 0. Il n'avait jamais été identifié comme critique : c'est un serveur d'impression.

**Les décisions.**

1. **Traitement immédiat** des trois points critiques : réduction des droits du compte de service, désactivation de l'authentification héritée après mesure en mode observation (§22.6), restriction de l'accès réseau.
2. **Règle de processus** : toute modification de configuration réalisée pendant un incident est enregistrée dans le journal de l'incident et **fait l'objet d'un ticket de reversion** à la clôture. Sans reversion possible, elle devient un écart motivé et documenté.
3. **Convergence** : le serveur d'impression entre dans le périmètre de l'outil de gestion de configuration, qui n'y avait jamais été déployé.

**Ce que Claire Nadeau retient**, et qu'elle formule au comité : *nous cherchions les serveurs critiques dans la liste des applications métier. Le chemin le plus court vers nos données passait par l'imprimante.*

**Livrable de l'épisode.** La règle de reversion post-incident, intégrée à la procédure de gestion des incidents, et l'extension du périmètre de convergence.

→ La suite en 🔴 §24.11, quand la revue des comptes de service révélera l'ampleur du sujet.

→ **Chapitre 24 — Identités, secrets et cryptographie** : les identités, les secrets et la cryptographie — ce qu'aucun correctif ne réduit.

#### Synthèse mentale du chapitre 23

La dérive n'est pas un problème de discipline mais une propriété des systèmes vivants : six mécanismes la produisent, tous légitimes pris isolément, et elle se traite par la détection et la convergence plutôt que par la réprimande. Surveiller toutes les modifications produit un bruit ingérable ; vingt éléments bien choisis — comptes à privilèges, règles de filtrage, authentification, tâches planifiées, points de démarrage — valent mieux que l'exhaustivité. La convergence automatique corrige la dérive mais écrase les corrections légitimes et propage les erreurs en quelques minutes : elle s'applique par anneaux. L'approche immuable rend la dérive impossible par construction, et déplace toute la conformité vers la construction de l'image. Enfin, une infrastructure décrite par du code donne un sentiment de maîtrise qui devient dangereux dès qu'une part significative des ressources a été créée manuellement — une description fausse à laquelle on fait confiance est pire qu'une absence de description.

**Trois questions de vérification**

1. Un contrôle a été désactivé pendant un incident il y a trois ans. Quel mécanisme de processus aurait empêché qu'il le reste, et à quel moment précis s'applique-t-il ?
2. Pourquoi la surveillance exhaustive des changements de configuration produit-elle moins de sécurité qu'une surveillance de vingt éléments ?
3. Votre infrastructure est décrite par du code à 70 %. En quoi cette situation est-elle plus risquée qu'une absence totale de description ?

---

### Chapitre 24 — Identités, secrets et cryptographie

#### 24.1 La dette d'annuaire

Le §2.8 a posé le principe : un annuaire accumule, et aucune mise à jour ne réduit cette accumulation. Voici ce qu'elle contient.

| Objet accumulé | Origine | Risque |
|---|---|---|
| Comptes de personnes parties | Départs sans processus de sortie | Accès valides sans porteur |
| Comptes de service de projets abandonnés | Créations sans date de fin | Souvent surprivilégiés, mots de passe anciens |
| Délégations d'administration héritées | Migrations, réorganisations | Droits invisibles dans les vues standard |
| Appartenances à des groupes privilégiés | Ajouts temporaires jamais retirés | Élévation permanente |
| Protocoles d'authentification hérités | Compatibilité avec un logiciel disparu | Contournement des protections modernes |
| Relations d'approbation entre domaines | Fusions, acquisitions (§9.5) | Chemins d'attaque transverses |

**La méthode de réduction**, par ordre de rendement :

1. **Comptes inactifs** : identifier ceux sans authentification depuis 90 jours, désactiver avant de supprimer, observer 30 jours. Rendement immédiat, risque faible.
2. **Groupes privilégiés** : lister les membres, faire valider nominativement par un responsable, retirer les non confirmés.
3. **Délégations** : les extraire — elles n'apparaissent pas dans les vues courantes — et les faire valider.
4. **Protocoles hérités** : mesurer l'usage réel en mode observation, puis désactiver.

#### 24.2 Comptes de service et comptes à privilèges

Les comptes de service sont le premier vecteur de propagation interne (§11.4).

| Problème | Pourquoi il persiste | Traitement |
|---|---|---|
| Mot de passe inchangé depuis des années | La rotation casse l'application qui l'utilise | Inventaire des consommateurs avant rotation (§24.10) |
| Droits d'administration sur de nombreux serveurs | Attribués « pour que ça marche » | Réduction progressive, mesurée en observation |
| Compte partagé entre plusieurs applications | Facilité de création | Un compte par usage |
| Aucun propriétaire | L'application a changé d'équipe | Rattachement obligatoire à un propriétaire (§10.4) |

**Les comptes de secours** — comptes d'urgence permettant d'accéder au système quand les mécanismes normaux échouent — méritent un traitement distinct : secret déposé de façon sécurisée, usage journalisé et alerté, test périodique de fonctionnement, et rotation après chaque usage. Un compte de secours non testé ne fonctionnera pas le jour où on en aura besoin ; un compte de secours non surveillé est une porte dérobée légitime.

#### 24.3 Les secrets

**Le cycle de vie d'un secret** : création, distribution, stockage, usage, rotation, révocation. Chacune de ces étapes peut fuir.

| Localisation typique | Risque |
|---|---|
| Code source et dépôts | Persistance dans l'historique même après suppression |
| Fichiers de configuration | Lisibles par tout compte ayant accès au serveur |
| Code d'infrastructure et fichiers d'état | Souvent en clair, largement accessibles (§23.5) |
| Chaînes d'intégration | Accessibles aux agents d'exécution (ch. 28) |
| Documentation et messagerie | Copiés une fois, jamais retirés |
| Coffre-fort de secrets | Concentration : devient un actif de niveau 0 |

⚠️ **PIÈGE — la rotation non répercutée**
Le scénario le plus fréquent et le plus douloureux : le secret est modifié dans le coffre-fort, mais une application le lit depuis un fichier de configuration copié deux ans plus tôt. La rotation « réussit », l'ancien secret reste valide et utilisé. **Une rotation n'est effective que si l'ancien secret est révoqué** — et la révocation est ce qui casse les consommateurs oubliés. C'est douloureux, et c'est précisément l'intérêt : c'est ainsi qu'on les découvre.

#### 24.4 Identités applicatives et autorisations déléguées

Dans les environnements en ligne, les identités non humaines sont devenues aussi nombreuses que les humaines, et bien moins surveillées.

| Objet | Risque spécifique |
|---|---|
| Identité d'application | Souvent créée avec des droits larges « en attendant », jamais réduits |
| Autorisation déléguée à une application tierce | Accorde un accès permanent aux données, sans mot de passe |
| Jeton de longue durée | Valable des mois, souvent stocké en clair |
| Identité de service managé | Pratique, mais l'attribution de droits est rarement revue |

✅ **BONNE PRATIQUE (P0)** — Faites l'inventaire des **autorisations déléguées** accordées à des applications tierces sur votre environnement de messagerie et de fichiers. C'est un exercice d'une demi-journée qui produit presque toujours des découvertes : connecteurs autorisés il y a plusieurs années, applications dont personne ne connaît l'usage, portées d'accès très supérieures au besoin. C'est le prolongement direct du §10.6 et du chapitre 31.

#### 24.5 Les clés d'accès distant

Les clés d'authentification pour l'administration distante posent un problème particulier : elles sont **créées par les utilisateurs**, sans processus central, et ne périment pas.

Quatre questions à poser à votre parc : combien de clés autorisées existent sur vos serveurs ? à qui appartiennent-elles ? depuis quand ? combien appartiennent à des personnes ayant quitté l'organisation ? Dans une organisation qui n'a jamais fait cet inventaire, la quatrième réponse est rarement zéro.

**Le traitement** : centraliser la distribution, imposer une durée de validité, rattacher chaque clé à un propriétaire, et intégrer la révocation au processus de départ.

#### 24.6 Certificats et infrastructure de confiance

**Le problème est double.** L'expiration provoque une interruption de service — c'est la seule échéance intrinsèque du §1.3. Et un certificat compromis ou mal émis permet l'usurpation.

| Objet | Ce qu'il faut savoir |
|---|---|
| Certificats de service | Inventaire, dates d'expiration, renouvellement automatisé |
| Certificats internes | Souvent oubliés, souvent de longue durée |
| Autorités de certification internes | **Actif de niveau 0** : leur compromission permet d'émettre n'importe quel certificat |
| Certificats de signature de code | Compromission = code malveillant signé par vous |
| Certificats de composants d'infrastructure | Expirations produisant des pannes difficiles à diagnostiquer |

✅ **BONNE PRATIQUE (P0)** — Constituez un inventaire des certificats avec leurs dates d'expiration et une alerte à 60, 30 et 7 jours. C'est l'une des mesures au meilleur rapport effort/incidents évités de tout le cours. Le renouvellement automatisé, là où il est possible, supprime le problème plutôt que de l'alerter.

#### 24.7 Magasins de confiance

Chaque système, chaque application, chaque environnement d'exécution embarque sa propre liste d'autorités de confiance. Trois sujets de MCS en découlent :

- **Les mises à jour** de ces listes ne suivent pas le même canal que les correctifs, et sont souvent oubliées — le cas du §3.8 en est l'illustration ;
- **les ajouts internes** — autorité interne, certificat de test ajouté un jour et jamais retiré — élargissent la confiance sans que personne ne le sache ;
- **les révocations** ne se propagent pas toujours, notamment sur les systèmes isolés ou anciens.

#### 24.8 Agilité cryptographique

**Le principe** : votre capacité à changer d'algorithme, de taille de clé ou de protocole **sans reconstruire vos applications**.

**Ce qui est actionnable aujourd'hui**, indépendamment de toute échéance future :

| Action | Effort | Bénéfice |
|---|---|---|
| Inventorier où la cryptographie est utilisée et laquelle | Moyen | Prérequis de tout le reste |
| Désactiver les suites et protocoles obsolètes | Faible | Immédiat |
| Réduire la durée de vie des certificats | Faible | Force l'automatisation du renouvellement |
| Éviter les algorithmes codés en dur dans les applications | Moyen | Rend le changement futur possible |
| Exiger l'agilité cryptographique dans les cahiers des charges | Nul | Structurant (§6.2) |

**Ce qui relève de la trajectoire** : la transition vers des algorithmes résistants aux futurs calculateurs quantiques est engagée au niveau des standards, avec des calendriers pluriannuels. Pour la quasi-totalité des organisations, l'action actionnable aujourd'hui n'est pas de migrer, c'est de **savoir où l'on utilise quoi** — c'est-à-dire la première ligne du tableau. Sans inventaire cryptographique, aucune migration future ne sera pilotable.

#### 24.9 Accès distants et d'administration

Statistiquement le vecteur d'entrée dominant. Quatre exigences, sans lesquelles le reste importe peu :

1. **Authentification multifacteur** sur tous les accès distants et d'administration, sans exception tolérée.
2. **Postes d'administration dédiés**, sans messagerie ni navigation (§13.5, ch. 28).
3. **Accès bornés dans le temps** plutôt que permanents, pour les prestataires notamment.
4. **Journalisation** des actions d'administration, exportée hors de l'équipement administré.

#### 24.10 Vérifier que les procédures fonctionnent

Un thème récurrent de ce chapitre : les procédures d'identité échouent silencieusement.

| Procédure | Test |
|---|---|
| Rotation de secret | Vérifier que l'ancien secret est **refusé** après rotation |
| Révocation de compte | Tenter une authentification après désactivation |
| Compte de secours | L'utiliser périodiquement, en conditions réelles |
| Renouvellement de certificat | Vérifier le certificat effectivement présenté par le service |
| Processus de départ | Auditer un échantillon de départs récents |

✅ **BONNE PRATIQUE (P1)** — Un test trimestriel sur un échantillon de chaque procédure. Trente minutes par procédure. C'est ce qui distingue une procédure qui existe d'une procédure qui fonctionne.

#### 24.11 🔴 FIL ROUGE — septembre 2027 : la revue des comptes de service

L'incident du serveur d'impression (§23.7) déclenche une revue complète des comptes de service d'HELIOMED. Trois semaines de travail, conduites par Malik Ferhaoui avec l'appui de l'infogérant.

**L'état des lieux : 213 comptes de service.**

| Constat | Nombre |
|---|---|
| Sans propriétaire identifié | 94 |
| Mot de passe inchangé depuis plus de 5 ans | 61 |
| Membres d'un groupe d'administration du domaine | 17 |
| Aucune authentification depuis plus de 12 mois | 38 |
| Utilisés par plusieurs applications distinctes | 22 |

**Le traitement, en trois vagues.**

*Vague 1 — les 38 inactifs.* Désactivation, observation 30 jours. Trois réactivations : deux traitements annuels de clôture, et un connecteur d'échange avec un partenaire dont l'usage est trimestriel — la dépendance temporelle du §10.5. Les 35 autres sont supprimés.

*Vague 2 — les 17 comptes d'administration du domaine.* Chacun est instruit individuellement. Onze n'avaient aucun besoin réel de ce niveau de droits : les droits sont réduits, sans incident. Quatre nécessitent des droits élevés mais sur un périmètre restreint : délégation ciblée. Deux relèvent d'applications métier dont l'éditeur exige l'administration complète du domaine — exigence documentée, contestée par écrit auprès de l'éditeur (§13.8), et compensée par une restriction d'usage et une surveillance dédiée dans l'attente.

*Vague 3 — la rotation des secrets.* C'est la plus douloureuse. La rotation des 61 comptes anciens est menée par lots de dix, avec un inventaire préalable des consommateurs. **Neuf incidents applicatifs** malgré cet inventaire : autant de consommateurs non documentés, découverts exactement comme le prévoit le §24.3 — par la révocation.

**Ce que la revue révèle en passant.** Deux comptes de service portaient encore le nom d'un prestataire dont le contrat s'était achevé en 2021. Ils étaient actifs, disposaient de droits sur le serveur de fichiers, et leur mot de passe n'avait jamais changé.

**Les trois mesures pérennes.**

1. **Aucun compte de service sans propriétaire ni date de revue** — même règle que pour les actifs (§5.5). Contrôle automatisé mensuel.
2. **Rotation obligatoire** avec inventaire préalable des consommateurs, par lots, avec fenêtre déclarée.
3. **Intégration au processus de départ** : la fin d'un contrat de prestation déclenche une revue des comptes associés.

**Ce que Claire Nadeau écrit dans sa note de synthèse** : *nous avons passé dix-huit mois à corriger des vulnérabilités logicielles. La revue des comptes de service a réduit davantage notre exposition réelle que les six dernières campagnes de correctifs réunies.*

→ La suite en 🔴 §25.22, quand la R&D de Nantes découvrira ce que contient réellement son application.

→ **Chapitre 25 — MCS des applications, de la chaîne logicielle et des dépendances** : le code applicatif et ses dépendances, y compris celui que vous avez écrit.

#### Synthèse mentale du chapitre 24

Un annuaire accumule et aucune mise à jour ne réduit cette accumulation : comptes orphelins, délégations héritées, groupes privilégiés, protocoles anciens forment une dette que seule une revue explicite traite. Les comptes de service sont le premier vecteur de propagation interne, et une rotation n'est effective que si l'ancien secret est révoqué — ce qui casse les consommateurs oubliés, et c'est précisément ainsi qu'on les découvre. Les identités non humaines et les autorisations déléguées à des applications tierces sont désormais aussi nombreuses que les identités humaines et bien moins surveillées : leur inventaire est un exercice d'une demi-journée qui produit toujours des découvertes. Les certificats sont la seule dégradation à échéance intrinsèque, et leur inventaire avec alertes est l'une des mesures au meilleur rapport effort/incidents évités du cours. En cryptographie, l'action actionnable aujourd'hui n'est pas de migrer mais de savoir où l'on utilise quoi. Enfin, les procédures d'identité échouent silencieusement : seul un test périodique distingue une procédure qui existe d'une procédure qui fonctionne.

**Trois questions de vérification**

1. Vous effectuez la rotation d'un secret et l'opération est déclarée réussie. Qu'est-ce qui n'est pas encore prouvé, et quel test le prouve ?
2. Pourquoi les autorisations déléguées à des applications tierces constituent-elles un angle mort plus important qu'un compte utilisateur oublié ?
3. Votre direction vous demande de préparer la transition cryptographique post-quantique. Quelle est la seule action réellement utile à engager cette année, et pourquoi les autres en dépendent-elles ?

---

### Chapitre 25 — MCS des applications, de la chaîne logicielle et des dépendances

> **Angle mort corrigé dans ce chapitre.** Une application peut être vulnérable **sans qu'aucune de ses dépendances ne le soit**. Le MCS applicatif ne se réduit pas à mettre à jour des bibliothèques : il commence par le code que vous avez écrit vous-même.

---

#### A — Le code détenu par l'organisation

#### 25.1 Les vulnérabilités du code propriétaire

Elles n'ont pas d'identifiant, ne figurent dans aucune base, et aucun scanner du chapitre 15 ne les remontera. Elles constituent pourtant une part importante des chemins d'entrée réels.

| Famille | Ce que c'est | Comment on la découvre |
|---|---|---|
| **Défaut d'autorisation** | Un utilisateur accède à des données qui ne sont pas les siennes en modifiant un identifiant | Test d'intrusion, signalement client |
| **Injection** | Une entrée utilisateur est interprétée comme instruction | Analyse statique, test d'intrusion |
| **Erreur de logique métier** | Le processus permet une opération non prévue — remise cumulée, étape sautée | Test métier, incident |
| **Contrôle d'entrée insuffisant** | Données non validées côté serveur | Analyse, test |
| **Fuite d'information** | Messages d'erreur détaillés, données superflues dans une réponse | Test, observation |
| **Faiblesse cryptographique propre** | Algorithme inadapté, aléa prévisible, secret codé en dur | Revue de code |
| **Point d'administration exposé** | Fonction technique accessible sans contrôle | Découverte externe (ch. 11) |
| **Code historique non maintenu** | Fonctionnalité ancienne que plus personne ne comprend | Revue, incident |

**Le défaut d'autorisation mérite une mention particulière** : il figure de façon constante en tête des classements de vulnérabilités applicatives établis par les référentiels du domaine, sa détection automatique est difficile — elle dépend entièrement des règles et des jeux de tests utilisés —, et il ne produit aucune anomalie technique — l'application fonctionne parfaitement, elle répond simplement à des demandes auxquelles elle ne devrait pas répondre.

#### 25.2 Les sources de constats applicatifs

| Source | Ce qu'elle trouve bien | Ce qu'elle manque |
|---|---|---|
| **Analyse statique du code** | Injections, secrets codés en dur, motifs dangereux | Logique métier, autorisation |
| **Analyse dynamique** | Comportements observables sur l'application en fonctionnement | Ce qui n'est pas atteint par les tests |
| **Test d'intrusion applicatif** | **Autorisation, logique métier, enchaînements** | Ce qui est hors périmètre ou hors budget |
| **Programme de récompense** | Ce qu'un attaquant réel trouverait | Nécessite maturité et budget |
| **Revue de code** | Faiblesses de conception | Coûteuse, non exhaustive |
| **Retours clients et incidents** | Le réel | Trop tard |

**La règle du §14.2 s'applique intégralement** : tous ces constats entrent dans **la même file** que les vulnérabilités de composants, avec la même priorisation. C'est ce qui évite qu'un défaut d'autorisation découvert en test d'intrusion progresse moins vite qu'une bibliothèque à mettre à jour.

#### 25.3 Affecter un constat applicatif

La difficulté est différente de celle du chapitre 17 : le correcteur n'est pas un exploitant mais une **équipe de développement**, dont la charge est planifiée par sprints et arbitrée par un responsable produit.

**Les trois frictions caractéristiques :**

| Friction | Manifestation | Traitement |
|---|---|---|
| Concurrence avec le fonctionnel | Le correctif de sécurité concurrence des fonctionnalités attendues | Réserver une capacité fixe par cycle (10 à 20 %), négociée une fois |
| Absence de propriétaire de composant | Le code appartient à « l'équipe » | Propriété nominative par composant, comme pour les actifs (§5.5) |
| Constat mal formulé | « Vulnérabilité XSS » sans contexte | Fournir : chemin de reproduction, impact métier, correction attendue |

✅ **BONNE PRATIQUE (P0)** — Négociez une **capacité de sécurité récurrente** dans la planification des équipes de développement, plutôt que de négocier chaque correctif. C'est exactement le pré-arbitrage du §9.4 transposé au développement, et cela supprime la discussion à chaque constat.

#### 25.4 Le cycle de remédiation applicative

```
Constat
   ↓  reproduire — sinon on corrige à l'aveugle
Reproduction documentée
   ↓  analyser la cause racine — pas seulement le symptôme
Cause racine identifiée
   ↓  corriger le code
Correction
   ↓  test de sécurité : le chemin de reproduction échoue-t-il désormais ?
Test de sécurité passé
   ↓  test de non-régression fonctionnelle
Validation
   ↓  déploiement progressif (§6.4)
Déploiement
   ↓  vérification en production
Vérifié
   ↓  AJOUT D'UN TEST PERMANENT
Clos
```

**La dernière étape est celle qui distingue une correction d'une correction durable.** Le test qui reproduisait la vulnérabilité entre dans la suite de tests automatisés. Il échouera si quelqu'un réintroduit le défaut — dans six mois, lors d'une refactorisation, par une autre personne. Sans lui, la même vulnérabilité réapparaîtra, et vous la découvrirez au prochain test d'intrusion, deux ans plus tard.

**L'analyse de cause racine** mérite d'être conduite au-delà du cas isolé : si un défaut d'autorisation existe sur un point d'accès, la question est *combien d'autres points d'accès présentent le même défaut ?* Corriger un cas et ignorer la classe est le gaspillage le plus courant du domaine.

#### 25.5 Branches de maintenance et rétroportage

Si votre produit est déployé chez des clients en plusieurs versions, corriger la version courante ne suffit pas.

| Question | Décision à formaliser |
|---|---|
| Combien de versions maintenez-vous en sécurité ? | Deux ou trois au maximum — au-delà, la charge devient ingérable |
| Rétroportez-vous les correctifs de sécurité ? | Oui pour les versions maintenues, avec le mécanisme du §2.2 |
| Publiez-vous un correctif ponctuel ou une version complète ? | Le correctif ponctuel accélère l'adoption ; la version complète simplifie la maintenance |
| Comment les clients apprennent-ils qu'ils doivent mettre à jour ? | C'est le chapitre 33 |

#### 25.6 Mesures temporaires côté applicatif

Quand la correction demande du temps, la hiérarchie du §20.2 s'applique avec des moyens propres au logiciel :

| Mesure | Délai | Réversibilité |
|---|---|---|
| Désactiver la fonctionnalité concernée | Minutes si un interrupteur existe (§6.5) | Immédiate |
| Restreindre l'accès à la fonctionnalité | Heures | Immédiate |
| Ajouter une validation supplémentaire en amont | Heures à jours | Simple |
| Règle de filtrage applicatif en frontal | Heures | Immédiate |
| Surveillance ciblée sur le chemin vulnérable | Heures | — |

**Les sept attributs du §20.7 s'appliquent intégralement**, et notamment la date d'expiration. Un interrupteur de fonctionnalité désactivé « en attendant le correctif » rejoint sinon les 400 interrupteurs oubliés du §6.5.

---

#### B — Politique de versions applicatives

#### 25.7 Définir la politique

Sept décisions à prendre une fois, et à écrire :

| Décision | Question |
|---|---|
| Version courante | Laquelle est la référence ? |
| Versions supportées en sécurité | Combien, et lesquelles ? |
| Nombre maximal de branches | Au-delà, chaque correctif coûte N fois |
| Durée de support | Combien de temps après la publication d'une version ? |
| Critères de fin de support | Date fixe, nombre de versions ultérieures, seuil d'adoption ? |
| Préavis | Combien de temps avant la fin de support d'une version ? |
| Obligation de migration | Le support est-il conditionné à une version minimale ? |

#### 25.8 Interfaces anciennes et compatibilité

Les points d'accès dépréciés sont des actifs à part entière : ils portent du code, souvent ancien, souvent moins protégé que les nouveaux, et souvent maintenus « parce qu'un client les utilise encore ».

**Le traitement** : les inventorier, mesurer leur usage réel, publier une date de retrait, et les traiter comme un décommissionnement (chapitre 35) — avec préavis, communication et vérification qu'ils ne sont plus appelés.

#### 25.9 La dette de version applicative

Elle se mesure, comme la dette d'obsolescence du §12.6 : nombre de clients sur une version non supportée, ancienneté moyenne des versions déployées, nombre de branches maintenues, charge consommée par le rétroportage.

**L'argument à porter en interne** : chaque branche supplémentaire maintenue multiplie le coût de chaque correctif de sécurité. Réduire le nombre de branches n'est pas un confort d'équipe de développement, c'est une mesure de MCS.

---

#### C — Chaîne logicielle et dépendances

#### 25.10 Le code que vous n'avez pas écrit

Dans une application moderne, une part souvent importante — parfois majoritaire — du code exécuté provient de bibliothèques externes, elles-mêmes dépendantes d'autres bibliothèques (§3.6). Cette part est rarement inventoriée, et c'est le problème.

**Trois conséquences directes pour le MCS :**

1. Votre surface d'attaque comprend le code de dizaines d'organisations que vous ne connaissez pas.
2. Vous ne contrôlez ni le rythme de correction, ni la qualité, ni la pérennité de ces composants.
3. Une vulnérabilité dans une bibliothèque très répandue vous concerne **en même temps que des dizaines de milliers d'autres organisations** — donc dans un contexte où l'exploitation automatisée démarre en quelques heures.

#### 25.11 L'inventaire des composants logiciels en pratique

| Question | Réponse opérationnelle |
|---|---|
| **Quand le générer ?** | À la construction, automatiquement. Un inventaire produit manuellement est périmé le jour de sa production |
| **Quelle granularité ?** | Composants directs **et** transitifs, avec versions exactes |
| **Où le stocker ?** | Associé à l'artefact produit, versionné, conservé aussi longtemps que la version est déployée |
| **Comment l'exploiter ?** | Rapproché en continu des sources de vulnérabilités, **rejoué à chaque nouvelle publication** |

⚠️ **PIÈGE — l'inventaire produit et jamais consommé**
C'est la situation la plus fréquente : l'organisation génère des inventaires de composants parce qu'un client ou un texte l'exige, les archive, et ne les rapproche jamais d'une base de vulnérabilités. Le document existe, la capacité n'existe pas. **La question qui tranche** : quand une vulnérabilité majeure est publiée dans une bibliothèque très répandue, combien de temps vous faut-il pour répondre « suis-je concerné, sur quels produits, dans quelles versions ? » Si la réponse dépasse quelques heures, votre inventaire ne sert à rien.

#### 25.12 Analyse de composition et atteignabilité

L'analyse de composition rapproche vos dépendances déclarées des vulnérabilités connues. Elle produit beaucoup de bruit, pour des raisons structurelles :

| Cause de bruit | Mécanisme |
|---|---|
| Dépendances transitives | La vulnérabilité est à trois niveaux de profondeur, vous ne l'avez pas choisie |
| Composant non chargé | Présent dans les dépendances, jamais utilisé à l'exécution |
| Fonction non atteignable | Le composant est utilisé, mais pas la fonction vulnérable (§11.6) |
| Version corrigée par l'écosystème | Résolution de version différente de la déclaration |

**Le traitement** : appliquer l'arbre du §16.3, en utilisant l'atteignabilité comme critère de dépriorisation documentée — jamais de clôture (§16.6).

#### 25.13 Politique de mise à jour des dépendances

| Approche | Principe | Risque |
|---|---|---|
| **Automatisée avec tests** | Un mécanisme propose les montées de version, les tests décident | Le meilleur rapport effort/résultat, si les tests existent |
| **Périodique groupée** | Une campagne mensuelle de mise à jour des dépendances | Simple, mais le retard s'accumule entre deux campagnes |
| **À la demande** | On met à jour quand une vulnérabilité l'impose | Chaque mise à jour devient une montée de plusieurs versions, donc risquée |

**Le cercle vicieux à connaître** : moins on met à jour, plus l'écart grandit, plus chaque mise à jour devient risquée, donc moins on met à jour. La mise à jour fréquente et automatisée est **moins risquée** que la mise à jour rare, contrairement à l'intuition — chaque saut est petit.

#### 25.14 La santé d'une dépendance

Une dépendance saine aujourd'hui peut devenir un problème demain. Six signaux à surveiller sur les composants critiques :

| Signal | Ce qu'il annonce |
|---|---|
| Fréquence de publication en baisse | Projet en perte de vitesse |
| **Un seul mainteneur actif** | Fragilité majeure : maladie, lassitude, changement de vie |
| Signalements de sécurité sans réponse | Le projet ne traitera pas vos vulnérabilités |
| Changement de mainteneur ou de propriétaire | À examiner : plusieurs compromissions ont emprunté cette voie |
| Archivage ou dépréciation annoncée | Migration à planifier |
| Absence de politique de sécurité déclarée | Aucun canal pour signaler ou recevoir |

✅ **BONNE PRATIQUE (P1)** — Identifiez vos dix à vingt dépendances les plus critiques — celles dont l'abandon vous poserait un vrai problème — et surveillez ces six signaux. C'est un exercice annuel, pas continu.

#### 25.15 Les attaques sur la chaîne d'approvisionnement

| Technique | Principe | Défense principale |
|---|---|---|
| **Typosquattage** | Un paquet au nom proche d'un paquet légitime | Verrouillage des versions, registre interne, revue des ajouts |
| **Confusion de dépendances** | Un paquet public prend la place d'un paquet interne homonyme | Espaces de noms réservés, priorité explicite du registre interne |
| **Compromission de mainteneur** | Le compte légitime publie une version malveillante | Verrouillage, délai avant adoption d'une version, vérification de provenance |
| **Compromission de la chaîne de construction** | L'attaquant modifie l'artefact produit | Protection des agents (ch. 28), attestations de provenance |
| **Dépendance abandonnée reprise** | Un tiers reprend un paquet inactif | Surveillance des changements de mainteneur (§25.14) |

**La défense la plus efficace et la moins coûteuse** : un **délai avant adoption** des nouvelles versions de dépendances — quelques jours suffisent à ce que la communauté détecte la majorité des paquets malveillants. C'est le délai d'observation du §18.3, transposé aux dépendances.

#### 25.16 Provenance et intégrité

| Mécanisme | Ce qu'il garantit |
|---|---|
| Verrouillage des versions | Vous obtenez exactement ce que vous avez validé |
| Registre interne avec approbation | Vous contrôlez ce qui entre |
| Vérification d'empreinte ou de signature | L'artefact n'a pas été modifié |
| Attestation de provenance | L'artefact vient bien de la chaîne de construction attendue |
| Construction reproductible | La même source produit le même artefact — permet la vérification indépendante |

**L'ordre d'adoption réaliste** : verrouillage d'abord (immédiat, gratuit), registre interne ensuite (structurant), vérification et attestations après. Les constructions reproductibles sont un objectif exigeant, à ne pas placer en tête d'un programme.

#### 25.17 Images de base et registres

Une image de conteneur hérite de tout ce que contient son image de base. Trois règles suffisent :

1. **Choisir des images de base minimales** — moins de composants, moins de vulnérabilités, moins de reconstruction.
2. **Fixer une cadence de reconstruction** (§3.2) : c'est l'indicateur qui remplace des centaines de constats individuels.
3. **Contrôler à la publication** dans le registre, pas à l'exécution : une image non conforme ne doit pas pouvoir être publiée (§22.4).

#### 25.18 Protéger la chaîne de construction

Traité en profondeur au chapitre 28. Trois points à retenir ici : les agents d'exécution disposent d'accès étendus et échappent souvent à l'inventaire ; les secrets de la chaîne sont un objectif de premier ordre ; et une compromission de la chaîne contamine **tous** les artefacts produits, y compris ceux livrés à vos clients.

#### 25.19 Déclarations d'exploitabilité et avis lisibles par machine

Le §4.8 a présenté les formats. Voici l'usage réel, dans les deux sens :

**En consommation.** Un fournisseur vous déclare qu'un composant vulnérable présent dans son produit n'est pas exploitable. Cela vous permet de dépriorer sans analyser — à condition de conserver la déclaration comme justification, et de la réexaminer si le contexte change.

**En production.** Si vous éditez un produit, ces déclarations vous évitent de recevoir cent fois la même question de vos clients à chaque vulnérabilité majeure d'une bibliothèque répandue. C'est un gain considérable pour le PSIRT (chapitre 33).

📌 **LIMITES** — La maturité de l'outillage reste inégale, et l'adoption est très variable selon les éditeurs. Ne construisez pas un processus qui **dépend** de la réception de ces déclarations : traitez-les comme un enrichissement quand elles arrivent.

#### 25.20 ⚖️ Ce que la réglementation produit impose sur les composants

Pour les fabricants de produits numériques, les obligations émergentes portent notamment sur : la fourniture d'un inventaire des composants, la gestion des vulnérabilités affectant les composants tiers, la mise à disposition de correctifs pendant une durée déterminée, et la notification des vulnérabilités activement exploitées. Le détail et le calendrier figurent au chapitre 33.

**La conséquence pratique**, même sans être fabricant : ces exigences se propagent le long de la chaîne (§13.7). Vos fournisseurs devront vous fournir ces éléments, et vos clients vous les demanderont.

#### 25.21 📌 Limites

- **Le code sans propriétaire** : une application dont l'équipe a été dissoute ne sera pas corrigée, quelle que soit la qualité du constat.
- **L'éditeur métier non coopératif** : vous détectez, il ne corrige pas. C'est un sujet contractuel (ch. 13), pas technique.
- **L'application sans jeu de tests** : corriger devient un pari, et le pari est souvent perdu — d'où le report systématique.
- **Le coût d'un correctif dans du code non testé** peut dépasser celui d'une réécriture partielle. Cela doit être dit, chiffré, et arbitré.

#### 25.22 🔴 FIL ROUGE — octobre 2027 : ce que contenait HelioLink

La R&D de Nantes produit son premier inventaire complet des composants d'HelioLink, dans le cadre de la préparation réglementaire produit.

**Les chiffres.**

| Élément | Nombre |
|---|---|
| Dépendances directes déclarées | 87 |
| Dépendances totales, transitives incluses | **1 412** |
| Portant une vulnérabilité connue | 156 |
| Après analyse d'atteignabilité | **12 réellement problématiques** |
| Composants sans mainteneur actif depuis > 2 ans | 9 |
| Composants dont le mainteneur a changé en 2026-2027 | 3 |

**Le rapport 156 → 12** est ce qui frappe l'équipe. L'analyse d'atteignabilité et les déclarations d'exploitabilité de trois fournisseurs éliminent 92 % du volume. Les 12 restants sont traités en trois semaines.

**Mais ce n'est pas la découverte importante du mois.**

En parallèle, le test d'intrusion applicatif annuel — commandé pour la première fois sur HelioLink — remonte un **défaut d'autorisation** : en modifiant un identifiant dans une requête, un utilisateur authentifié d'un établissement de santé peut consulter les données de télésuivi des patients d'un **autre** établissement.

Aucun scanner ne l'aurait trouvé. Aucun inventaire de composants ne l'aurait signalé. Le code fonctionne exactement comme il a été écrit. Et la vulnérabilité existe depuis la première version, mise en service en 2023.

**Le traitement, selon le §25.4.**

1. **Reproduction** documentée en une heure.
2. **Cause racine** : le contrôle d'appartenance à l'établissement est effectué à l'affichage, côté interface, mais pas dans le service qui sert les données.
3. **Extension de l'analyse** — et c'est le point décisif : combien d'autres points d'accès présentent le même défaut ? Réponse après revue : **quatre autres**, dont deux exposant des données de santé.
4. **Correction** des cinq points, avec contrôle centralisé plutôt que répété.
5. **Test permanent** ajouté à la suite automatisée : cinq tests vérifient désormais qu'un utilisateur d'un établissement ne peut pas accéder aux données d'un autre.
6. **Mesure temporaire** pendant les onze jours de développement : journalisation renforcée et alerte sur tout accès inter-établissements, avec destinataire nommé.

**La question qui occupe le comité de direction.** Léa Cassin, déléguée à la protection des données, pose la question inévitable : cette faille a existé quatre ans ; a-t-elle été exploitée ? Les journaux d'accès applicatifs sont conservés 90 jours. Sur cette période, aucun accès anormal n'est constaté. Sur les quatre années précédentes, **la question reste sans réponse** — exactement comme en juillet (§21.11), et pour la même raison.

**Ce que la direction décide.** Journalisation applicative portée à 24 mois sur HelioLink, avec export indépendant. Test d'intrusion applicatif annuel inscrit au budget récurrent. Et une capacité de sécurité de 15 % réservée dans chaque cycle de développement (§25.3).

**Ce que Yann Prigent écrit dans son rapport** : *nous avons passé six mois à surveiller 1 412 dépendances. La vulnérabilité la plus grave de notre produit, nous l'avions écrite nous-mêmes.*

→ La suite en 🔴 §26.13, quand un progiciel métier imposera son environnement d'exécution.

→ **Chapitre 26 — Bases de données, middlewares et *runtimes*** : la couche intermédiaire, source d'obsolescence invisible.

#### Synthèse mentale du chapitre 25

Une application peut être vulnérable sans qu'aucune de ses dépendances ne le soit : le défaut d'autorisation, le plus fréquemment exploité en conditions réelles, est invisible à l'analyse automatique et ne produit aucune anomalie technique. Les constats applicatifs entrent dans la même file que les vulnérabilités de composants, et la friction propre au développement se traite par une capacité de sécurité réservée dans chaque cycle plutôt que par une négociation à chaque constat. Le cycle de remédiation applicative se termine par l'ajout d'un test permanent — sans lui, la même vulnérabilité réapparaîtra lors d'une refactorisation dans six mois. L'analyse de cause racine doit s'étendre à la classe entière : corriger un cas et ignorer les quatre autres points d'accès identiques est le gaspillage le plus courant. Côté dépendances, la mise à jour fréquente et automatisée est moins risquée que la mise à jour rare, contrairement à l'intuition, et un délai de quelques jours avant adoption d'une nouvelle version est la défense la plus rentable contre les paquets malveillants. Enfin, un inventaire de composants qui ne permet pas de répondre en quelques heures à « suis-je concerné » n'a aucune utilité.

**Trois questions de vérification**

1. Votre analyse de composition est parfaite et votre parc de dépendances est à jour. Quelle catégorie de vulnérabilité reste entièrement invisible, et comment la découvre-t-on ?
2. Pourquoi mettre à jour ses dépendances rarement est-il plus risqué que les mettre à jour souvent ?
3. Un défaut d'autorisation est corrigé sur un point d'accès. Quelles deux actions restent indispensables avant de clore le constat ?

---

### Chapitre 26 — Bases de données, middlewares et *runtimes*

#### 26.1 La couche intermédiaire : à jour côté système, vulnérable côté applicatif

C'est le cas le plus fréquent d'obsolescence invisible : le système d'exploitation est parfaitement à jour, les correctifs sont appliqués chaque mois, les indicateurs sont au vert — et l'application s'exécute sur un environnement dont le support a pris fin il y a deux ans.

**Pourquoi cette couche échappe au dispositif**, pour quatre raisons cumulées :

1. Elle est souvent **installée hors gestionnaire de paquets**, par l'éditeur métier ou par l'équipe applicative.
2. Elle est **embarquée dans l'application** : une même machine peut porter trois versions différentes d'un même environnement d'exécution.
3. Ses **cycles de support sont courts** — souvent deux à quatre ans, contre cinq à dix pour un système d'exploitation.
4. Elle n'appartient à personne : trop applicative pour l'exploitation, trop technique pour le métier.

#### 26.2 Bases de données

| Objet | Ce qui se dégrade | Point d'attention |
|---|---|---|
| Version majeure | Fin de support, souvent 5 à 8 ans | Migration lourde : compatibilité applicative, tests |
| Version mineure | Correctifs de sécurité réguliers | Souvent différée par crainte d'indisponibilité |
| Moteur et extensions | Modules additionnels avec leur propre cycle | Rarement inventoriés |
| Configuration | Comptes par défaut, chiffrement, journalisation | Souvent la vulnérabilité réelle (ch. 22) |

**La spécificité opérationnelle** : une base de données est un composant **à état**. Les stratégies du §6.4 ne s'y appliquent pas directement, et le point de non-retour du §6.7 y est central. Trois configurations de correction, par ordre de préférence :

| Configuration | Interruption | Condition |
|---|---|---|
| Réplication avec bascule | Quelques secondes à minutes | Compatibilité entre versions pendant la transition (§2.7) |
| Fenêtre planifiée | Durée de l'opération | Standard, mais impose la fenêtre |
| Migration avec bascule applicative | Variable | Réservée aux montées de version majeures |

#### 26.3 Compatibilité applicative et schémas

Ce qui bloque réellement une montée de version de base de données n'est presque jamais la base : c'est l'**application** qui s'appuie dessus.

| Blocage | Manifestation |
|---|---|
| Certification de l'éditeur métier | L'application n'est supportée que sur une version précise |
| Fonctionnalité dépréciée utilisée | Le code applicatif emploie une syntaxe supprimée |
| Comportement modifié | Tri, encodage, gestion des valeurs nulles : l'application fonctionne différemment |
| Pilote d'accès | Le connecteur ne supporte pas la nouvelle version |

**La conséquence pour le MCS** : la montée de version de base de données est un **projet applicatif**, pas une opération d'infrastructure. Elle se planifie avec l'équipe applicative et l'éditeur, avec le délai correspondant — souvent six à douze mois. D'où l'importance de l'anticipation du chapitre 12.

#### 26.4 Serveurs web, mandataires et serveurs d'applications

Ces composants sont **exposés par nature** et traitent des entrées non fiables. Ils appartiennent presque toujours à la classe C1.

**Trois points spécifiques :**

- **Les modules et extensions** ont leur propre cycle : un serveur web à jour peut charger un module vulnérable non maintenu.
- **La configuration prime souvent sur la version** : en-têtes, méthodes autorisées, gestion des erreurs, limites de taille. Un serveur à jour mal configuré expose davantage qu'un serveur légèrement en retard bien configuré.
- **Le mandataire inverse est un point de contrôle privilégié** : c'est là que se placent les mesures compensatoires du §20.3, ce qui en fait aussi un actif critique.

#### 26.5 Brokers, caches, moteurs de recherche, ordonnanceurs

Composants d'infrastructure applicative, souvent installés pour un besoin technique et jamais revus.

⚠️ **PIÈGE — le composant installé sans authentification**
Beaucoup de ces produits s'installent par défaut **sans authentification**, sur le principe qu'ils ne seront joignables que depuis un réseau de confiance. Cette hypothèse est fausse dès qu'un poste du réseau est compromis (§11.4). Ce sont des cibles de choix : ils contiennent souvent des données applicatives complètes, et parfois des secrets.

**Les trois vérifications** à mener sur chacun : authentification activée ? exposition réelle mesurée ? version supportée ?

#### 26.6 Les *runtimes* applicatifs

Machines virtuelles applicatives, plateformes d'exécution, interpréteurs : c'est la source d'obsolescence invisible la plus fréquente.

| Caractéristique | Conséquence |
|---|---|
| Cycles de support courts | Une version sort du support avant que le projet ne soit terminé |
| Plusieurs versions cohabitent sur une même machine | L'inventaire par machine ne suffit pas |
| Souvent embarqué avec l'application | Aucun mécanisme système ne le met à jour |
| Version imposée par l'éditeur métier | Vous héritez de son calendrier (§13.6) |

✅ **BONNE PRATIQUE (P0)** — Inventoriez les environnements d'exécution **par application**, pas par machine, avec leur version et leur date de fin de support. C'est un exercice d'une à deux journées qui révèle presque toujours plusieurs composants hors support ignorés jusque-là.

#### 26.7 Les bibliothèques natives embarquées

Le composant que personne ne déclare : bibliothèques de chiffrement, de compression, d'analyse de formats, livrées **à l'intérieur** d'une application, sans passer par le gestionnaire de paquets.

**Pourquoi c'est un angle mort complet** : le scanner système ne les voit pas (elles ne sont pas des paquets), l'analyse de composition ne les voit pas (elles ne sont pas dans les dépendances déclarées), et l'éditeur métier ne les mentionne pas. Elles n'apparaissent que dans un inventaire de composants fourni par l'éditeur — d'où l'importance de l'exiger (§13.6).

#### 26.8 Pilotes, agents, extensions et greffons

Toute la surface ajoutée sur une machine par des besoins ponctuels : pilotes matériels, agents de supervision, extensions de navigateur, greffons applicatifs, utilitaires métier.

**Le traitement réaliste** : on n'inventorie pas tout. On inventorie ce qui s'exécute avec des privilèges élevés — pilotes et agents — et ce qui traite des entrées non fiables — extensions de navigateur, greffons de traitement de documents. Le reste relève de la maîtrise de ce qui est installé (§22.1).

#### 26.9 Clients lourds et postes utilisateurs

Les postes portent eux aussi des environnements d'exécution et des bibliothèques embarquées, souvent installés par des applications métier et jamais mis à jour. C'est le prolongement du §19.5 : le trou noir du poste de travail ne se limite pas aux applications visibles.

#### 26.10 Négocier la montée de version avec un éditeur métier

Situation la plus fréquente : votre environnement d'exécution est hors support, et l'éditeur de l'application refuse de supporter une version plus récente.

**La séquence qui fonctionne :**

1. **Écrire la demande**, avec la date de fin de support du composant et la référence de la source (§13.8).
2. **Demander un engagement daté** : à quelle date une version compatible sera-t-elle disponible ?
3. **En l'absence de réponse ou d'engagement**, formaliser une dérogation (§7.4) dont le signataire est le propriétaire métier, et dont le motif est explicitement *« l'éditeur ne fournit pas de version compatible »*.
4. **Inscrire le sujet au renouvellement contractuel** — c'est le seul moment où vous disposez d'un levier.
5. **Compenser** dans l'intervalle (chapitre 20).

**Ce que produit cette séquence**, au-delà de la protection technique : elle transforme un problème technique subi par l'exploitation en une décision de gestion assumée par le métier, avec une trace. C'est ce qui débloque, tôt ou tard, le budget de migration.

#### 26.11 Environnements de développement, recette et préproduction

Ces environnements portent les mêmes composants intermédiaires que la production, et sont traités au chapitre 28. Un point ici : un environnement de recette dont l'environnement d'exécution diverge de la production **invalide les tests** (§6.12). L'écart de version fait partie des quatre axes à mesurer.

#### 26.12 📌 Limites

- **Applications non maintenues** : l'éditeur a disparu, le code source n'est pas disponible. La seule voie est la sanctuarisation (chapitre 32).
- **Prérequis figés par contrat** : traité au §26.10, avec une issue souvent budgétaire.
- **Multiplicité des versions** : une organisation peut porter cinq versions d'un même environnement d'exécution pour cinq applications. La rationalisation est un projet en soi, dont le bénéfice de MCS est considérable.
- **Absence de propriétaire** : c'est la cause racine la plus fréquente. Cette couche doit être explicitement rattachée à un propriétaire technique (§10.4).

#### 26.13 🔴 FIL ROUGE — novembre 2027 : l'application de gestion commerciale

L'inventaire des environnements d'exécution **par application** (§26.6) est mené chez HELIOMED sur les 176 serveurs internes. Une journée et demie de travail.

**Le résultat.**

| Composant | Applications concernées | Statut |
|---|---|---|
| Environnement d'exécution A, version ancienne | 3 applications, dont la gestion commerciale | **Hors support depuis 2023** |
| Environnement d'exécution A, version courante | 9 applications | Supporté |
| Moteur de base de données, version N-2 | 2 applications | Fin de support dans 7 mois |
| Serveur d'applications, version ancienne | 1 application | **Hors support depuis 2024** |
| Bibliothèque de chiffrement embarquée | Inconnue — non déclarée par l'éditeur | **Non mesuré** |

**Le cas central : l'application de gestion commerciale.** Utilisée par 60 personnes, elle porte le fichier clients. Elle s'exécute sur un environnement hors support depuis 2023 — c'est celle du mini-lab 7 (§20.10), dont la dérogation expire le 31 mars 2028.

L'éditeur a été relancé trois fois depuis juin. Réponse obtenue en novembre, par écrit : une version compatible existe, elle est facturée 40 k€, et la version actuelle ne sera plus supportée du tout à compter de septembre 2028.

**Ce que change la réponse écrite.** Le sujet cesse d'être un arbitrage technique. Trois faits sont désormais établis et datés : le composant est hors support depuis quatre ans, une solution existe et son prix est connu, et une seconde échéance arrive en septembre 2028. Karim Lebrun inscrit les 40 k€ au budget 2028 en quinze minutes — ce que dix-huit mois de discussions techniques n'avaient pas obtenu.

**La découverte annexe, plus préoccupante.** Le serveur d'applications hors support depuis 2024 porte une application développée en interne en 2019, dont l'équipe a été dissoute lors d'une réorganisation. Personne ne sait la reconstruire. Le code source existe, mais aucune chaîne de construction fonctionnelle. C'est le cas limite du §26.12, et il est renvoyé au chapitre 32.

**La ligne « non mesuré ».** La bibliothèque de chiffrement embarquée dans le progiciel métier n'est pas déclarée par l'éditeur. La demande d'inventaire des composants est intégrée au courrier de renouvellement contractuel, en application du §13.6 — première application concrète de l'effet de propagation réglementaire du §25.20.

**Livrable de l'épisode.** L'inventaire des composants intermédiaires par application, versé au référentiel d'obsolescence du chapitre 12, avec trois échéances datées et une ligne non mesurée assumée.

→ La suite en 🔴 §27.7, quand la question des micrologiciels reviendra sans avoir jamais eu de propriétaire.

→ **Chapitre 27 — Couches basses et périphéries** : les couches basses, les moins visibles et les plus en retard.

#### Synthèse mentale du chapitre 26

La couche intermédiaire — bases de données, serveurs d'applications, environnements d'exécution, bibliothèques embarquées — est la source d'obsolescence invisible la plus fréquente : système parfaitement à jour, indicateurs au vert, et une application qui s'exécute sur un composant hors support depuis deux ans. Quatre raisons se cumulent : installation hors gestionnaire de paquets, embarquement dans l'application, cycles de support courts, et absence de propriétaire. Ce qui bloque une montée de version de base de données n'est presque jamais la base mais l'application : c'est donc un projet applicatif de six à douze mois, pas une opération d'infrastructure. Les brokers, caches et moteurs de recherche s'installent souvent sans authentification, sur l'hypothèse d'un réseau de confiance qui devient fausse au premier poste compromis. Enfin, l'inventaire doit se faire **par application** et non par machine, et la négociation avec un éditeur métier récalcitrant se gagne par une demande écrite, un engagement daté et une dérogation signée par le métier — pas par la persuasion technique.

**Trois questions de vérification**

1. Vos serveurs affichent 98 % de conformité aux correctifs système. Quelle question posez-vous pour savoir si vos applications s'exécutent sur des composants supportés ?
2. Pourquoi une montée de version de base de données se planifie-t-elle sur six à douze mois plutôt que sur une fenêtre de maintenance ?
3. Un éditeur métier refuse de supporter une version récente de l'environnement d'exécution. Décrivez les cinq étapes de la séquence à suivre, et expliquez ce que produit l'étape 3 au-delà de la protection technique.

---

### Chapitre 27 — Couches basses et périphéries

#### 27.1 Micrologiciels : inventaire, déploiement, risque

Le §3.8 a posé les mécanismes. Voici la mise en œuvre.

**Ce qui compose réellement cette couche**, et qui est presque toujours sous-estimé :

| Objet | Où il se trouve | Fréquence de mise à jour constatée |
|---|---|---|
| Micrologiciel de carte mère | Tout serveur, tout poste | Rarement, souvent jamais |
| Contrôleur de gestion à distance | Serveurs physiques | Presque jamais — et c'est un accès privilégié complet |
| Micrologiciel de disque, de contrôleur de stockage | Serveurs, baies | Uniquement lors d'incidents |
| Cartes réseau, cartes d'extension | Serveurs | Jamais |
| Micrologiciel d'équipement réseau | Commutateurs, points d'accès | Traité au §19.6 |
| Périphériques | Imprimantes, caméras, contrôle d'accès | Jamais |

⚠️ **Le contrôleur de gestion à distance mérite un traitement particulier.** Il permet d'allumer, éteindre, réinstaller et prendre la main sur un serveur, indépendamment du système d'exploitation. Il dispose de sa propre pile réseau, de sa propre interface d'administration et de ses propres comptes — souvent les comptes par défaut du constructeur. C'est un **actif de niveau 0** au sens du §11.7, et il est presque systématiquement absent des inventaires.

**Les trois vérifications prioritaires** sur ces contrôleurs : sont-ils sur un réseau d'administration séparé ? les comptes par défaut ont-ils été changés ? à quelle version sont-ils ?

**Le déploiement**, quand il est décidé : il suit les anneaux du §18.4, avec deux précautions supplémentaires — un micrologiciel interrompu en cours d'écriture peut rendre le matériel inutilisable, et l'ordre entre composants importe (contrôleur de gestion avant carte mère, généralement).

#### 27.2 Le risque *pre-boot*

Un composant qui s'exécute avant le système d'exploitation ne peut pas être surveillé par les protections qui s'exécutent dedans. Une compromission à ce niveau survit à une réinstallation complète, et parfois au remplacement du disque.

**Ce qui protège réellement, dans l'ordre :**

1. **Le démarrage sécurisé activé** — sans lui, les autres mécanismes ne servent à rien.
2. **Les bases de certificats à jour** — c'est le cas du §3.8, dont la dégradation est silencieuse.
3. **Le mot de passe de configuration du micrologiciel** — sans lui, quiconque a un accès physique désactive le reste.
4. **Le chiffrement du disque avec liaison au matériel** — rend inefficace l'extraction du disque.
5. **La protection contre le retour en arrière** du micrologiciel.

📌 **LIMITES** — Ces mesures se décident **à l'achat et au déploiement initial**. Les activer sur un parc existant est possible mais coûteux, et certaines opérations — activer le démarrage sécurisé, changer le mode de démarrage — peuvent nécessiter une réinstallation. C'est un cas typique où le MCS *by design* du chapitre 6 se paie très cher quand il a été négligé.

#### 27.3 Équipements réseau et de sécurité : la fin de support de sécurité

Le §19.6 a traité le déploiement. Un point spécifique mérite d'être isolé, parce qu'il est méconnu et coûteux.

**Trois dates coexistent** sur un équipement réseau, et elles ne sont pas simultanées :

| Date | Signification |
|---|---|
| Fin de commercialisation | On ne peut plus l'acheter |
| **Fin de support de sécurité** | **Plus aucun correctif de sécurité — la seule qui compte pour le MCS** |
| Fin de support matériel | Plus de remplacement, plus d'assistance |

La fin de support de sécurité est souvent **antérieure de plusieurs années** à la fin de support matériel. Un équipement sous contrat de maintenance actif, remplacé en cas de panne, peut ne plus recevoir aucun correctif depuis longtemps. L'organisation, elle, a le sentiment d'un équipement « sous contrat ».

✅ **BONNE PRATIQUE (P0)** — Suivez la date de fin de support **de sécurité** dans votre référentiel d'obsolescence (§12.2), distinctement des autres. C'est cette date qui déclenche le remplacement, pas la panne.

#### 27.4 Appliances et boîtiers fournisseur

Une appliance est une boîte noire dont vous ne maîtrisez ni le système, ni les composants, ni le calendrier.

| Caractéristique | Conséquence pour le MCS |
|---|---|
| Système d'exploitation non accessible | Vous ne pouvez ni scanner, ni corriger, ni durcir |
| Composants tiers non déclarés | Vous ne savez pas ce qu'elle embarque (§26.7) |
| Correctifs au rythme du fournisseur | Vous héritez de son délai |
| Mises à jour parfois imposées | Un changement peut survenir sans votre accord |
| Fin de vie décidée par le fournisseur | Parfois brutale, avec préavis court |

**Les quatre exigences à porter au contrat** (§13.3) : délai d'application des correctifs de sécurité par le fournisseur, notification des vulnérabilités affectant le produit, inventaire des composants, et préavis de fin de support.

**En l'absence de ces exigences** — cas fréquent sur les équipements déjà installés — le traitement est celui du chapitre 20 : mesurer l'exposition, isoler, surveiller, et documenter le risque accepté.

#### 27.5 Périphériques et objets connectés d'entreprise

Imprimantes multifonctions, caméras, contrôle d'accès, visioconférence, affichage dynamique, capteurs de bâtiment.

**Pourquoi ils comptent réellement** :

- Ils sont **nombreux** et souvent connectés au réseau bureautique sans segmentation.
- Ils disposent de **fonctions étendues** : stockage, numérisation vers messagerie, comptes d'annuaire configurés, historiques de documents.
- Ils sont **rarement mis à jour** et parfois hors support depuis des années.
- Ils appartiennent souvent aux **services généraux**, pas à l'informatique.

**Le traitement réaliste**, sans prétendre à l'exhaustivité :

| Prio | Action |
|---|---|
| **P0** | Les inventorier et identifier un propriétaire — souvent hors DSI (§5.5) |
| **P0** | Changer les comptes par défaut, désactiver les services inutiles |
| **P0** | Les segmenter : aucun besoin d'être joignables depuis tout le réseau |
| P1 | Vérifier les comptes d'annuaire qu'ils utilisent — souvent surprivilégiés |
| P1 | Suivre leur fin de support avec le reste du parc |
| P2 | Mettre à jour les micrologiciels, par lots |

#### 27.6 ⚠️ Les équipements de sécurité comme cible privilégiée

Un constat désormais établi : les équipements de sécurité exposés — passerelles d'accès distant, pare-feu, contrôleurs d'accès réseau — figurent parmi les cibles les plus recherchées.

**Les raisons sont structurelles**, et il faut les comprendre plutôt que les subir :

1. Ils sont **exposés par conception** — c'est leur fonction.
2. Ils disposent d'**accès étendus** au système d'information.
3. Ils sont **peu surveillés de l'intérieur** : on y installe rarement des agents de détection.
4. Ils sont **difficiles à corriger** : interruption de service, fenêtre rare, doctrine de version prudente (§2.7).
5. Une compromission y est **persistante** : elle survit souvent au correctif.

**Ce que cela impose au MCS**, et qui découle directement du fil rouge de juillet (§21.11) :

| Exigence | Prio |
|---|---|
| Classe C1 sans discussion, fenêtre récurrente dédiée | **P0** |
| Interface d'administration jamais publiée sur Internet | **P0** |
| Journalisation exportée hors de l'équipement, conservée longtemps | **P0** |
| Doctrine de version écrite, datée, revue (§2.7) | P1 |
| Après exploitation potentielle : **reconstruction**, pas correction | P1 |
| Configuration de référence permettant une reconstruction rapide | P1 |

#### 27.7 🔴 FIL ROUGE — décembre 2027 : la ligne « micrologiciels : non mesuré »

Depuis janvier 2026, la ligne « micrologiciels » du périmètre d'HELIOMED porte la mention *non couvert, propriétaire désigné, échéance de première mesure* (§3.9). Vingt-trois mois plus tard, Claire Nadeau la traite enfin — et elle explique au comité pourquoi elle l'a laissée en attente aussi longtemps.

**Le raisonnement assumé.** L'inventaire, l'exposition, la propriété d'actif, les comptes de service et le code applicatif produisaient chacun une réduction de risque supérieure pour un effort moindre. La ligne micrologiciels était déclarée, datée et visible : elle n'était pas oubliée, elle était **priorisée en dernier**, et cette décision figurait au compte rendu de chaque comité.

**La première mesure, en deux jours.**

| Constat | Résultat |
|---|---|
| Contrôleurs de gestion à distance des serveurs | 41 équipements, **tous sur le réseau bureautique**, 12 avec le compte constructeur par défaut |
| Micrologiciels de cartes mères serveurs | Version d'origine sur 38 des 41 |
| Micrologiciels des postes | Non mesurés — l'infogérant ne les remonte pas |
| Imprimantes multifonctions | 22 équipements, dont 6 hors support, 4 avec numérisation vers messagerie configurée avec un compte de service (§24.11) |
| Certificats de démarrage sécurisé | 214 postes n'ont pas reçu la mise à jour de 2026 |

**Ce qui est traité immédiatement, et ce qui ne l'est pas.**

*Traité en deux semaines, coût quasi nul* : les 12 comptes par défaut des contrôleurs de gestion, la segmentation des 41 contrôleurs sur un réseau d'administration séparé, et la désactivation de la numérisation vers messagerie sur les 4 imprimantes concernées.

*Planifié en 2028* : la mise à jour des micrologiciels de cartes mères, par lots, à l'occasion des redémarrages programmés. Aucune urgence identifiée, risque de brique réel, bénéfice modéré au regard de l'effort.

*Reporté avec justification* : le remplacement des 6 imprimantes hors support, inscrit au budget de renouvellement des services généraux pour 2029.

*Ajouté au contrat* : la remontée de l'état des micrologiciels des postes, dans le prochain avenant Numeria.

**Le point le plus instructif de l'épisode.** La segmentation des 41 contrôleurs de gestion à distance — deux jours de travail, aucun coût de licence — retire du réseau bureautique 41 accès permettant de prendre le contrôle complet de serveurs, indépendamment de leur système d'exploitation. Aucune de ces machines n'apparaissait dans les scans de vulnérabilités, aucune ne figurait dans les indicateurs, et aucune n'aurait jamais été détectée par le dispositif construit pendant deux ans.

**Ce que Claire écrit en conclusion.** *Déclarer un périmètre non mesuré ne le rend pas sûr. Mais cela garantit qu'il sera traité un jour, et qu'entre-temps personne ne croira qu'il l'a été.*

→ La suite en 🔴 §28.10, quand un agent d'exécution de la chaîne de construction se révélera administrateur du cluster.

→ **Chapitre 28 — Environnements non productifs et actifs d'administration** : les environnements que personne ne regarde.

#### Synthèse mentale du chapitre 27

Le contrôleur de gestion à distance des serveurs est un actif de niveau 0 : il permet d'allumer, réinstaller et prendre la main indépendamment du système d'exploitation, dispose de ses propres comptes — souvent ceux du constructeur — et est presque systématiquement absent des inventaires. Le risque avant démarrage échappe à toutes les protections logicielles, et les mesures qui le traitent se décident à l'achat : les rétrofitter coûte très cher. Sur les équipements réseau, la fin de support **de sécurité** précède souvent de plusieurs années la fin de support matériel, ce qui donne le sentiment trompeur d'un équipement « sous contrat ». Les appliances sont des boîtes noires dont on hérite du calendrier : les quatre exigences se portent au contrat, avant l'installation. Enfin, les équipements de sécurité exposés sont des cibles privilégiées pour cinq raisons structurelles, et la conséquence opérationnelle est nette : après exploitation potentielle, on reconstruit plutôt qu'on corrige.

**Trois questions de vérification**

1. Vos scans de vulnérabilités ne remontent rien d'anormal sur vos serveurs. Quel équipement, présent sur chacun d'eux, échappe pourtant entièrement à cette mesure, et pourquoi est-il critique ?
2. Un équipement réseau est sous contrat de maintenance actif. Que devez-vous vérifier avant d'en conclure qu'il est maintenu en sécurité ?
3. Une passerelle d'accès distant a été exposée avec une vulnérabilité exploitable. Le correctif est appliqué. Pourquoi n'est-ce pas suffisant ?

---

### Chapitre 28 — Environnements non productifs et actifs d'administration

#### 28.1 Pourquoi la non-production doit être maintenue

L'argument « ce n'est que de la préproduction » repose sur une hypothèse implicite fausse : que ces environnements ne contiennent rien d'intéressant et ne mènent nulle part.

**Les quatre raisons pour lesquelles ils comptent autant que la production :**

| Raison | Mécanisme |
|---|---|
| **Données de production copiées** | La recette est alimentée par une copie de la base réelle, sans anonymisation dans la majorité des cas |
| **Pivot** | Ces environnements sont souvent joignables depuis et vers la production |
| **Secrets persistants** | Les mêmes comptes de service, les mêmes clés, parfois les mêmes mots de passe |
| **Durcissement moindre** | Configuration relâchée « pour faciliter les tests », journalisation absente |

**La question qui tranche**, à poser à toute équipe défendant l'exclusion d'un environnement : *contient-il des données réelles, et depuis quelles machines est-il joignable ?* Dans une majorité de cas, la réponse fait entrer l'environnement dans le périmètre de classe C2 au minimum.

#### 28.2 Cartographier l'oublié

| Environnement | Ce qu'il contient souvent | Pourquoi il échappe |
|---|---|---|
| Préproduction / recette | Copie de production | Considéré comme non critique |
| Développement | Données partielles, secrets | Géré par les équipes de développement |
| Laboratoire technique | Configurations expérimentales | Créé et oublié |
| Environnement de formation | Données factices ou réelles | Utilisé quelques jours par an |
| Démonstrateur commercial | **Données réalistes, exposé** | Hébergé hors DSI (§11.12) |
| Environnement de secours | Copie complète de la production | Non maintenu car « inactif » |

**L'environnement de secours mérite une attention particulière** : maintenu à l'identique de la production pour pouvoir la remplacer, il est souvent oublié des campagnes de correctifs parce qu'il n'est pas en service. Le jour où l'on bascule dessus, on bascule sur un système en retard de plusieurs mois — au moment précis où l'on est le plus vulnérable.

#### 28.3 Postes de développement et chaînes d'intégration

| Actif | Risque spécifique |
|---|---|
| **Poste de développeur** | Droits locaux étendus, outils nombreux, code source, secrets, accès aux dépôts |
| **Agent d'exécution de la chaîne** | Accès aux registres, aux environnements de déploiement, aux secrets de construction |
| **Serveur de gestion de sources** | Contient tout votre code et son historique, y compris les secrets qui y ont transité |
| **Registre d'artefacts** | Une image compromise se propage à toute la production |

⚠️ **PIÈGE — l'agent d'exécution éphémère**
Les agents créés à la demande et détruits après usage n'apparaissent dans aucun inventaire réseau (§10.8). Ils sont pourtant souvent les actifs les plus privilégiés de l'organisation : ils déploient en production. L'inventaire doit se faire **depuis l'orchestrateur**, pas depuis le réseau, et leur configuration de référence doit être traitée avec le niveau d'exigence d'un actif de niveau 0.

#### 28.4 Les actifs d'administration

Ce sont les premiers à maintenir, et ils sont souvent parmi les derniers traités.

| Actif | Pourquoi il est critique |
|---|---|
| **Poste d'administration** | Porte les sessions privilégiées ; sa compromission donne accès à tout ce qu'il administre |
| **Rebond / passerelle d'administration** | Point de passage obligé, donc cible concentrée |
| **Serveur de déploiement** | Capable d'exécuter du code sur l'ensemble du parc |
| **Console de gestion de virtualisation** | Contrôle de toutes les machines virtuelles (§3.1) |
| **Console de sauvegarde** | Accès à toutes les données, y compris historiques |
| **Coffre-fort de secrets** | Concentration de tous les accès |
| **Outil de scan** | Identifiants privilégiés et cartographie des faiblesses (§15.4) |

✅ **BONNE PRATIQUE (P0) — le poste d'administration dédié**
La mesure au meilleur rapport effort/risque de tout ce chapitre : les tâches d'administration se réalisent depuis un poste **dédié**, qui ne sert ni à la messagerie, ni à la navigation, ni à la bureautique. La raison est mécanique : un poste qui ouvre des pièces jointes et une session d'administration du domaine ne doivent pas être la même machine. Cette mesure ne coûte que de la rigueur, et elle casse le chemin d'attaque le plus fréquent (§11.4).

#### 28.5 Modèles et images de référence

**Le mécanisme** : une machine créée à partir d'un modèle ancien naît avec tout le retard du modèle. Elle sera peut-être rattrapée par la campagne suivante — ou non, si elle est éphémère.

| Objet | Question à se poser |
|---|---|
| Modèle de machine virtuelle | De quand date-t-il ? Qui le met à jour, à quelle fréquence ? |
| Image de référence de poste | Idem |
| Image de conteneur de base | Cadence de reconstruction (§3.2) |
| Modèle d'infrastructure décrite par code | Versions des modules et connecteurs (§23.5) |
| Procédure d'installation manuelle | Encore plus problématique : elle vieillit sans que personne ne s'en aperçoive |

✅ **BONNE PRATIQUE (P0)** — Fixez une **cadence maximale de reconstruction des modèles**, suivez leur âge comme indicateur, et intégrez le contrôle de conformité à leur production (§22.4). C'est le remède à la récurrence du §17.9, et il traite la cause au lieu du symptôme.

#### 28.6 Instantanés et supports de restauration

Un instantané pris avant une intervention et conservé six mois est une machine vulnérable en attente d'être réactivée.

| Objet | Risque | Traitement |
|---|---|---|
| Instantané de machine virtuelle | Restauration = retour à un état non corrigé | Durée de vie limitée, purge automatique |
| Sauvegarde restaurée | Réintroduit l'état d'origine | Contrôle de conformité systématique après restauration |
| Machine clonée pour test | Duplique les vulnérabilités et les secrets | Inventaire, durée de vie, suppression |
| Support d'installation | Contient une version ancienne | Régénération périodique |

**La règle** : toute restauration ou tout clonage déclenche un **contrôle de conformité** avant remise en service. C'est l'une des cinq causes de récurrence du §17.9, et c'est la plus facile à traiter.

#### 28.7 Actifs intermittents

Postes nomades rarement connectés, matériel de secours stocké, équipements saisonniers, machines de laboratoire éteintes la plupart du temps, pièces de rechange préparées.

**Le problème commun** : ils ne sont pas là au moment des campagnes, et ils reviennent en service avec un retard proportionnel à leur absence.

**Les trois traitements** :

1. **Agent plutôt que scan réseau** : c'est la seule façon de les atteindre quand ils sont connectés, où qu'ils soient.
2. **Contrôle à la reconnexion** : une machine absente depuis plus de N jours passe par une phase de mise à jour avant d'accéder aux ressources.
3. **Mise à jour avant stockage** pour le matériel de secours — et acceptation qu'il vieillira quand même, d'où l'intérêt des pièces prépatchées du chapitre 29.

#### 28.8 L'accès conditionnel fondé sur le niveau de mise à jour

**Le principe** : subordonner l'accès aux ressources à l'état de conformité de la machine. Une machine en retard de correctifs voit son accès restreint jusqu'à régularisation.

| Ce que cela apporte | Ce que cela ne règle pas |
|---|---|
| Traite les actifs intermittents sans campagne dédiée | Ne fonctionne que sur les machines enrôlées |
| Rend la conformité visible pour l'utilisateur | Ne dit rien des machines qui n'accèdent à rien |
| Déplace l'effort de la relance vers le mécanisme | Peut être contourné par des chemins d'accès non couverts |

⚠️ **PIÈGE — le blocage sans échappatoire**
Un mécanisme qui bloque brutalement provoque deux réactions : des tickets massifs au support, et la recherche de contournements par les utilisateurs. La mise en œuvre progressive — avertissement, puis restriction partielle, puis blocage — avec une procédure d'exception traçable, est la seule qui tienne dans la durée.

#### 28.9 ⚠️ « Ce n'est que de la préprod » : reconstitution du chemin réel

```
Serveur de préproduction, non durci, non surveillé, hors périmètre de scan
   → contient une copie de la base de production de janvier
   → le compte de service applicatif y est le MÊME qu'en production
   → ce compte dispose de droits de lecture sur le serveur de fichiers de production
   → le serveur de fichiers contient les sauvegardes de configuration des équipements réseau
   → ces configurations contiennent les secrets d'administration
```

Cinq étapes, aucune vulnérabilité logicielle exploitée après la première. Chaque étape résulte d'une décision de commodité parfaitement rationnelle prise isolément — c'est la combinaison toxique du §11.5.

**Les trois ruptures les moins coûteuses** dans cette chaîne : des comptes de service **distincts** entre production et non-production ; l'anonymisation des données copiées en recette ; l'absence de joignabilité directe entre les deux environnements.

#### 28.10 🔴 FIL ROUGE — janvier 2028 : l'agent d'exécution de Nantes

Les quatre agents d'exécution de la chaîne d'intégration de Nantes, identifiés en janvier 2026 (§3.9), n'avaient jamais été traités autrement que par la désignation d'un propriétaire — Yann Prigent. Deux ans plus tard, la revue des actifs d'administration les remet sur la table.

**Ce que l'analyse établit.**

| Constat | Détail |
|---|---|
| Configuration | Agents créés à la demande depuis une image construite en 2024 |
| Droits | Un jeton d'accès permanent avec droits d'écriture sur le registre d'images **et** droits de déploiement sur le cluster de production |
| Réseau | Joignables depuis le réseau de développement, non segmentés |
| Secrets | Trois secrets de production accessibles pendant la construction |
| Journalisation | Aucune : les agents sont détruits après usage, leurs journaux avec |
| Inventaire | Absents du périmètre de référence — créés et détruits automatiquement (§10.8) |

**Le chemin d'attaque reconstitué**, en quatre étapes : poste de développeur compromis → accès au dépôt de code → modification d'un fichier de définition de construction → l'agent exécute le code modifié avec ses droits de déploiement en production.

Aucune vulnérabilité logicielle n'intervient après la première étape. C'est exactement le schéma du §25.18 et du §28.9.

**Les décisions, en trois vagues.**

*Immédiat.* Le jeton permanent est remplacé par une identité à durée de vie courte, obtenue à l'exécution et limitée au strict nécessaire. Les droits de déploiement en production sont retirés des agents de construction : le déploiement devient une étape distincte, avec une approbation humaine pour la production.

*Sous un mois.* Segmentation du réseau des agents. Journalisation exportée avant destruction de l'agent. Reconstruction de l'image des agents, et cadence de reconstruction fixée à 30 jours (§28.5).

*Structurel.* Les agents d'exécution entrent au périmètre de référence, inventoriés **depuis l'orchestrateur** et non depuis le réseau. Ils sont classés C1, au titre d'actifs d'administration.

**La discussion la plus difficile.** L'équipe de développement conteste initialement l'approbation humaine avant déploiement en production, qui ralentit la livraison. L'arbitrage retenu, en comité, est un pré-arbitrage au sens du §9.4 : approbation requise pour la production uniquement, automatique pour tous les autres environnements, et déléguée à un rôle et non à une personne pour ne pas créer de goulot. La livraison perd quelques minutes ; la chaîne cesse d'être un chemin direct vers la production.

**Ce que Claire Nadeau note au comité.** *Nous avons mis deux ans à traiter quatre machines qui n'existent que quelques minutes à la fois, et qui disposaient de plus de droits que n'importe quel administrateur de l'entreprise.*

→ **Fin de la Partie IV.** La suite en 🔴 §29.11, avec l'arbitrage sur la ligne 2 de Saint-Étienne.

→ **Chapitre 29 — MCS en environnement industriel (OT / ICS)** : l'industriel, où toutes les règles précédentes s'inversent.

#### Synthèse mentale du chapitre 28

« Ce n'est que de la préproduction » repose sur une hypothèse fausse : ces environnements contiennent des copies de données réelles, partagent les mêmes comptes de service, sont joignables depuis et vers la production, et sont moins durcis. L'environnement de secours est le cas le plus perfide : maintenu à l'identique pour remplacer la production, il est exclu des campagnes parce qu'il n'est pas en service — et l'on bascule dessus au moment où l'on est le plus vulnérable. Les agents d'exécution des chaînes de construction sont souvent les actifs les plus privilégiés de l'organisation et n'apparaissent dans aucun inventaire réseau : ils s'inventorient depuis l'orchestrateur. Le poste d'administration dédié est la mesure au meilleur rapport effort/risque du chapitre : un poste qui ouvre des pièces jointes et une session d'administration du domaine ne doivent pas être la même machine. Enfin, toute restauration ou clonage doit déclencher un contrôle de conformité — c'est la cause de récurrence la plus facile à traiter.

**Trois questions de vérification**

1. Une équipe demande d'exclure la préproduction du périmètre de scan. Quelles deux questions posez-vous, et quelle réponse ferait basculer l'environnement en classe C2 ?
2. Reconstituez en cinq étapes un chemin d'attaque partant d'un serveur de préproduction et aboutissant aux secrets d'administration réseau. Quelles sont les trois ruptures les moins coûteuses ?
3. Vos agents de construction sont créés à la demande et détruits après usage. Pourquoi n'apparaissent-ils dans aucun inventaire, et où faut-il aller les chercher ?

---

---

> ### 🎓 À ce stade de la Partie IV, vous savez…
>
> - **dériver** un référentiel de durcissement en motivant chaque écart, et mesurer une conformité de configuration sans produire un chiffre faux ;
> - **traiter** la dérive comme une propriété des systèmes vivants, par détection et convergence plutôt que par réprimande ;
> - **réduire** la dette d'annuaire, faire une rotation de secret qui soit réellement effective, et inventorier ce qui expire ;
> - **traiter** les vulnérabilités du code que vous avez écrit vous-même — celles qu'aucun outil de composition ne verra ;
> - **inventorier** les composants intermédiaires par application, et négocier une montée de version avec un éditeur récalcitrant ;
> - **atteindre** les couches que les outils ne remontent pas : micrologiciels, contrôleurs de gestion, périphériques ;
> - **traiter** les environnements que personne ne regarde : non-production, agents de construction, actifs d'administration.
>
> **Ce que vous ne savez pas encore** : comment adapter tout cela quand les règles changent. C'est l'objet de la Partie V.


## PARTIE V — Contextes spécialisés

Les parties précédentes ont construit un dispositif complet. Celle-ci le confronte à cinq contextes où ses règles ne s'appliquent pas telles quelles : l'industriel, le cloud, le logiciel en ligne, le legacy irréductible, et le produit livré à des clients. Chacun conserve le même niveau d'exigence — cas concret, livrable, erreur fréquente, limite explicite.

---

### Chapitre 29 — MCS en environnement industriel (OT / ICS)

#### 29.1 Ce qui change fondamentalement

Le §3.7 a posé les repères. Voici ce que cela implique concrètement pour un programme de MCS.

| Dimension | Informatique de gestion | Industriel |
|---|---|---|
| Priorité | Confidentialité, intégrité | **Sûreté des personnes, puis disponibilité** |
| Durée de vie | 3 à 7 ans | 15 à 25 ans |
| Fenêtre | Nuit, week-end | **Arrêt de production planifié, souvent annuel** |
| Validation du correctif | Interne | **Constructeur**, sous peine de perte de garantie et de qualification |
| Conséquence d'une erreur | Perte de service | **Risque physique, rebut de production, arrêt de ligne** |
| Qui décide | DSI, métier | **Responsable de production et responsable sûreté** |

🏢 **VU EN ATELIER** — Première visite d'un RSSI sur un site de production. Il demande quand la ligne peut être arrêtée pour appliquer des correctifs. Le responsable de production répond : « en août, pendant trois jours, et il faudra me dire lequel des trois ». Ce n'était pas de l'obstruction : c'était la réponse exacte à la question posée.

**Le renversement à intégrer.** En informatique de gestion, l'argument « il faut corriger » l'emporte généralement sur « ça risque de casser ». En industriel, c'est l'inverse — et c'est **légitime** : une ligne à l'arrêt a un coût immédiat et mesurable, un défaut sur un automate peut avoir des conséquences physiques, et une modification non validée peut invalider une qualification réglementaire.

Un responsable sécurité qui arrive dans un environnement industriel avec ses réflexes bureautiques échoue en trois semaines. La démarche n'est pas « corriger plus vite », c'est **maîtriser l'exposition, préparer longtemps à l'avance, et appliquer pendant les arrêts**.

#### 29.2 Le cadre normatif appliqué au maintien

La série de normes de sécurité des systèmes d'automatisation industriels fournit une structure directement utilisable, indépendamment de toute certification.

| Concept | Définition | Usage en MCS |
|---|---|---|
| **Zone** | Ensemble d'actifs partageant les mêmes exigences de sécurité | Détermine le périmètre d'une compensation |
| **Conduit** | Chemin de communication entre zones | C'est là que se placent les mesures de filtrage (§20.2) |
| **Niveau de sécurité** | Niveau de résistance attendu d'une zone | Calibre l'effort |
| **Répartition des rôles** | Exploitant / intégrateur / fabricant | Détermine **qui doit corriger** |

**L'apport principal pour le MCS** : la répartition des responsabilités. Beaucoup de blocages industriels viennent de ce que personne n'a établi qui, de l'exploitant, de l'intégrateur ou du fabricant, doit produire, valider et appliquer un correctif. Poser la question dans ces termes débloque plus de situations qu'une discussion technique.

#### 29.3 L'inventaire industriel

Le chapitre 10 s'applique, avec des méthodes différentes.

| Méthode | Applicabilité | Précaution |
|---|---|---|
| **Écoute passive du trafic** | Méthode par défaut | Aucun risque pour le procédé ; nécessite un point de capture |
| **Extraction depuis les outils d'ingénierie** | Très riche : versions d'automates, programmes, configurations | Nécessite l'accès et la coopération de l'équipe automatisme |
| **Inventaire manuel** | Toujours possible | Chronophage, mais souvent le plus fiable sur les équipements anciens |
| **Documentation d'installation** | Fournie par l'intégrateur | Souvent périmée, mais c'est un point de départ |
| Scan actif | **Passif par défaut, actif sous procédure** | Validation explicite, test préalable, procédure d'arrêt, de préférence hors production (§3.7) |

✅ **BONNE PRATIQUE (P0)** — Commencez par l'inventaire manuel réalisé **avec** l'équipe de maintenance, pas par un outil. Deux journées passées avec le responsable automatisme produisent un inventaire plus fiable et plus utile qu'un mois d'outillage — et elles construisent la relation sans laquelle rien ne se fera ensuite.

#### 29.4 Les correctifs industriels

**Le cycle réel**, très différent de celui du chapitre 18 :

```
Vulnérabilité publiée par le constructeur ou un centre de réponse
   → le constructeur qualifie l'applicabilité à VOTRE configuration
   → il publie (ou non) un correctif validé
   → l'intégrateur valide sur votre installation spécifique
   → planification sur le prochain arrêt de production
   → application, avec matériel de secours prêt
   → tests fonctionnels et de sûreté
   → remise en production, qualification si nécessaire
```

Ce cycle prend **des mois**. Entre la publication et l'application, la compensation n'est pas une solution dégradée : c'est le mode normal de traitement.

**Les trois cas de figure :**

| Cas | Fréquence | Traitement |
|---|---|---|
| Correctif validé par le constructeur | Minoritaire | Planification sur arrêt |
| Correctif existant, non validé | Fréquent | Compensation jusqu'à validation, relance du constructeur par écrit |
| Aucun correctif — produit hors support | Fréquent sur les équipements anciens | Compensation permanente et plan de remplacement (ch. 32) |

🖼 **SCHÉMA — Chaîne de mise à jour hors ligne.** *Flux linéaire à huit étapes, de la source officielle à la preuve d'installation, avec les points de double contrôle signalés.*

#### 29.5 La chaîne complète de mise à jour hors ligne

C'est le livrable technique central du chapitre. Un environnement industriel n'est pas connecté à Internet ; les correctifs doivent donc y entrer par un chemin maîtrisé.

```
① SOURCE OFFICIELLE
   Portail constructeur, compte nominatif, canal identifié
        ↓
② POSTE DE TÉLÉCHARGEMENT CONTRÔLÉ
   Poste dédié, durci, à jour, hors du réseau industriel
        ↓
③ VÉRIFICATION D'INTÉGRITÉ
   Signature ou empreinte publiée par le constructeur — comparée, pas supposée
        ↓
④ ANALYSE ET VALIDATION
   Analyse antimalware multi-moteurs · vérification du contenu · validation fonctionnelle
        ↓
⑤ SUPPORT AMOVIBLE MAÎTRISÉ
   Support dédié, identifié, effacé avant usage, jamais utilisé ailleurs
        ↓
⑥ SAS DE TRANSFERT
   Station de décontamination ou poste dédié en zone intermédiaire
        ↓
⑦ ENVIRONNEMENT INDUSTRIEL
   Application selon la procédure constructeur, matériel de secours prêt
        ↓
⑧ PREUVE D'INSTALLATION
   Relevé de version, journal de transfert, procès-verbal signé
```

**La gouvernance de cette chaîne**, sans laquelle elle ne tient pas :

| Règle | Raison |
|---|---|
| **Double contrôle** aux étapes ③ et ④ | Deux personnes valident l'intégrité et l'analyse |
| **Journal des transferts** | Qui a transféré quoi, quand, vers quel équipement |
| **Supports dédiés et identifiés** | Marqués physiquement, stockés sous contrôle |
| **Interdiction stricte des supports personnels** | Vecteur d'entrée historique le plus documenté en industriel |
| **Dépôt miroir hors ligne** | Évite de retélécharger, conserve l'historique des versions validées |
| **Procédure de retour arrière** | Version précédente conservée et testée |
| **Pièces de rechange prépatchées** | Un équipement de remplacement stocké depuis trois ans porte une version ancienne (§28.7) |

⚠️ **PIÈGE — la clé USB du prestataire**
Le scénario le plus fréquent et le mieux documenté : un technicien du constructeur intervient pour une maintenance, connecte son propre support à un automate, et introduit ce qui s'y trouve. La règle — supports fournis par l'exploitant, analysés, dédiés — doit figurer dans le contrat de maintenance et être vérifiée à chaque intervention, pas seulement écrite.

#### 29.6 La maintenance à distance des fournisseurs

Beaucoup d'installations industrielles disposent d'un accès distant permanent pour le constructeur. C'est souvent le chemin d'entrée le plus direct vers la zone industrielle.

**Les cinq exigences** :

1. **Accès à la demande**, activé pour une intervention, désactivé après — jamais permanent.
2. **Authentification multifacteur** et compte nominatif, pas un compte partagé du constructeur.
3. **Traçabilité** : enregistrement des sessions, journal accessible de votre côté.
4. **Supervision** : l'intervention est accompagnée côté exploitant.
5. **Contractualisation** : ces règles figurent au contrat de maintenance (§13.3).

#### 29.7 Compensations spécifiques à l'industriel

| Mesure | Applicabilité |
|---|---|
| **Segmentation par zones et conduits** | Mesure structurante n° 1 |
| Filtrage sur les conduits | Contrôle des protocoles autorisés entre zones |
| **Suppression des flux devenus inutiles** | Souvent le gain le plus rapide (§20.11) |
| Postes d'ingénierie durcis et dédiés | Vecteur d'entrée majeur |
| Contrôle des supports amovibles | Voir §29.5 |
| Surveillance passive du trafic industriel | Détecte les anomalies sans perturber |
| Diodes de données | Pour les flux strictement sortants |

#### 29.8 ✅ Livrable — Le plan de MCS industriel pluriannuel

Structuré par **arrêts de production**, et non par mois :

| Section | Contenu |
|---|---|
| Inventaire | Équipements, versions, statut de support, criticité procédé |
| Vulnérabilités connues | Par équipement, avec statut de validation constructeur |
| Compensations en place | Avec les sept attributs du §20.7 |
| Planification par arrêt | Ce qui sera appliqué au prochain arrêt, et pourquoi |
| Équipements sans correctif | Plan de remplacement ou sanctuarisation (ch. 32) |
| Relances constructeurs | Demandes écrites en cours, avec dates |
| Pièces de rechange | Versions stockées, plan de mise à niveau |

#### 29.9 ⚠️ Les erreurs fréquentes

| Erreur | Conséquence |
|---|---|
| Scan actif sur réseau industriel sans validation | Défaut d'automate, arrêt de ligne, et perte durable de la confiance |
| Correctif appliqué hors validation constructeur | Perte de garantie, invalidation de qualification |
| Confondre sûreté et sécurité | Les systèmes de sûreté relèvent d'un régime propre, à ne jamais modifier sans processus dédié |
| Imposer les délais bureautiques | Rejet immédiat, et fin de la coopération |
| Traiter l'industriel comme un sous-ensemble de l'informatique | Erreur de posture : ce sont deux métiers |
| Négliger la relation humaine | Sans le responsable maintenance, aucun accès, aucune information, aucun résultat |

#### 29.10 📌 Limites

- **Le temps long est irréductible.** Un cycle de validation constructeur ne se comprime pas ; il s'anticipe.
- **Certains équipements ne seront jamais corrigés.** Le fournisseur a disparu, ou le produit est hors support depuis dix ans. C'est le chapitre 32.
- **La visibilité restera partielle.** L'écoute passive ne voit que ce qui communique.
- **Le budget dépend de la production**, pas de la DSI. Les arbitrages se font dans un autre circuit, avec d'autres critères.

#### 29.11 🔴 FIL ROUGE — février 2028 : le bilan de l'arrêt de novembre

L'arrêt de production de novembre 2027 a permis d'appliquer, sur la ligne 2 de Saint-Étienne, le correctif compensé depuis juin (§20.11). Thomas Berger et Claire Nadeau font le bilan de deux ans de MCS industriel chez HELIOMED.

**Ce qui a été réalisé.**

| Action | Résultat |
|---|---|
| Inventaire manuel avec l'équipe maintenance | 11 postes de supervision, 14 automates, 3 réseaux distincts documentés pour la première fois |
| Segmentation en zones et conduits | 4 zones définies, flux inter-zones réduits de 23 à 9 |
| Suppression des flux inutiles | 6 flux supprimés, dont l'export vers la bureautique (§20.11) |
| Chaîne de mise à jour hors ligne | Formalisée, testée, appliquée en novembre |
| Accès distants constructeurs | 3 accès permanents supprimés, remplacés par des accès à la demande |
| Correctifs appliqués | 4, pendant l'arrêt de novembre |
| Équipements sans correctif possible | 3 automates, fournisseur disparu — compensation permanente |

**Ce que révèle le bilan.** Sur deux ans, **4 correctifs ont été appliqués**. Rapporté aux standards de l'informatique de gestion, le chiffre paraît dérisoire. Mais la réduction d'exposition réelle vient d'ailleurs : suppression de 14 flux inter-zones, suppression de 3 accès distants permanents, et maîtrise des supports amovibles. Aucune de ces actions n'est un correctif.

**L'incident évité, et il est instructif.** En septembre, un technicien d'un constructeur se présente pour une intervention planifiée avec son propre support amovible contenant une mise à jour. La procédure du §29.5 est appliquée : refus du support, téléchargement depuis le portail officiel par HELIOMED, vérification d'empreinte, analyse. **L'empreinte ne correspond pas** à celle publiée par le constructeur. Après échange, il s'avère que le fichier du technicien datait d'une intervention précédente chez un autre client et avait été modifié localement. Aucune malveillance — mais un fichier non conforme, non tracé, qui aurait été installé sur un automate de production.

**Ce que Thomas Berger dit en comité**, et que Claire cite ensuite régulièrement : *« Il y a deux ans, j'aurais dit non à tout, parce qu'on me demandait d'appliquer des règles qui n'ont pas de sens ici. Aujourd'hui je dis oui à ce qui est validé, dans mes fenêtres, avec mes procédures. Ce qui a changé, ce n'est pas ma position, c'est qu'on me l'a demandé dans mes termes. »*

**Livrable de l'épisode.** Le plan de MCS industriel pluriannuel d'HELIOMED, calé sur les arrêts de production de 2028 et 2029, et la chaîne de mise à jour hors ligne documentée — Annexe L.

→ La suite en 🔴 §30.11, quand le fournisseur cloud imposera une échéance sans négociation possible.

→ **Chapitre 30 — MCS du cloud : infrastructure, plateforme et services managés** : le cloud, où vous pilotez l'anticipation plutôt que la correction.

#### Synthèse mentale du chapitre 29

En industriel, la sûreté des personnes et la disponibilité priment, les équipements vivent quinze à vingt-cinq ans, les fenêtres sont annuelles et les correctifs doivent être validés par le constructeur : arriver avec des réflexes bureautiques garantit l'échec en trois semaines. La démarche n'est pas de corriger plus vite mais de maîtriser l'exposition, préparer très à l'avance, et appliquer pendant les arrêts — la compensation n'est pas un pis-aller, c'est le mode normal de traitement. L'inventaire commence par deux journées avec l'équipe de maintenance, pas par un outil : elles produisent plus d'information et construisent la relation sans laquelle rien ne se fera. La chaîne de mise à jour hors ligne en huit étapes, avec double contrôle, journal des transferts et supports dédiés, est le livrable technique central. Enfin, la réduction d'exposition réelle vient rarement des correctifs : elle vient de la suppression des flux inutiles, des accès distants permanents et de la maîtrise des supports.

**Trois questions de vérification**

1. Un responsable de production refuse toute intervention sur ses automates. Qu'avez-vous probablement mal formulé, et comment reprenez-vous la discussion ?
2. Décrivez les huit étapes de la chaîne de mise à jour hors ligne, et indiquez à quelles étapes le double contrôle s'applique.
3. En deux ans, vous n'avez appliqué que quatre correctifs sur votre parc industriel. Comment démontrez-vous à votre direction que le risque a néanmoins fortement diminué ?

---

### Chapitre 30 — MCS du cloud : infrastructure, plateforme et services managés

#### 30.1 La responsabilité partagée, décodée

Le §3.4 a posé le principe. Voici les zones grises, celles où les incidents se produisent.

| Zone grise | Question | Réponse fréquente |
|---|---|---|
| Image de machine fournie par le fournisseur | Qui la met à jour ? | **Vous**, dès l'instant où vous l'instanciez |
| Version mineure d'un service managé | Appliquée automatiquement ? | Souvent oui, dans une fenêtre que vous choisissez partiellement |
| Version majeure d'un service managé | Qui décide ? | Vous — **jusqu'à la date limite**, ensuite le fournisseur |
| Configuration de sécurité par défaut | Sécurisée ? | Non : les défauts privilégient la mise en service |
| Journalisation | Activée ? | Rarement par défaut, souvent facturée |
| Correctifs du système sous-jacent en plateforme | Qui ? | Le fournisseur, sans préavis systématique |

✅ **BONNE PRATIQUE (P0) — la matrice de responsabilité signée**
Pour chaque service que vous utilisez, une ligne : *qui maintient quoi, qui décide de la fenêtre, quel préavis, quelle preuve fournie*. C'est le livrable du §30.10, et sa vertu principale est de forcer la question là où personne ne se la pose — c'est-à-dire précisément dans les zones grises ci-dessus.

#### 30.2 Images et instances

**Le mécanisme central** : une instance créée à partir d'une image porte tout le retard de cette image (§28.5). Dans le cloud, ce mécanisme est amplifié par la mise à l'échelle automatique — une montée en charge peut créer vingt instances à partir d'une image vieille de six mois.

| Objet | Traitement |
|---|---|
| Catalogue d'images | Images validées, versionnées, avec une cadence de reconstruction |
| Instances longue durée | Traitées comme des serveurs classiques, ou remplacées (§3.5) |
| Groupes à mise à l'échelle | **La correction passe par l'image**, jamais par l'instance |
| Instances éphémères | N'apparaissent pas dans un inventaire réseau : inventaire par l'interface du fournisseur |

**L'indicateur préventif central** dans ce contexte : **l'âge de l'image** en service. Une organisation qui maintient toutes ses images à moins de 30 jours réduit fortement le volume de constats individuels à traiter — sans supprimer le besoin d'analyse de vulnérabilités ni de mesure d'exposition, puisqu'une image récente peut embarquer un composant vulnérable.

#### 30.3 Bases de données et services managés

| Événement | Ce que vous contrôlez |
|---|---|
| Correctif mineur | La fenêtre, parfois le report de quelques semaines |
| Version majeure disponible | Le moment de la migration, **jusqu'à une date limite** |
| Fin de support d'une version | Rien : la migration devient forcée |
| Changement de comportement par défaut | Rien, sauf à lire les annonces |

**La conséquence pour le MCS** : sur ces services, **vous ne pilotez pas la correction, vous pilotez l'anticipation**. Le travail consiste à connaître les échéances de fin de support des versions utilisées, et à planifier les migrations avant la date limite — faute de quoi elles seront subies, au moment choisi par le fournisseur.

✅ **BONNE PRATIQUE (P0)** — Intégrez les versions de services managés à votre référentiel d'obsolescence (§12.2), au même titre que les systèmes d'exploitation. C'est l'oubli le plus fréquent des programmes de MCS en environnement cloud.

#### 30.4 Orchestrateurs managés et exécution sans serveur

| Objet | Contrainte | Anticipation nécessaire |
|---|---|---|
| Version du plan de contrôle | Support d'environ quatorze mois (§3.3), fenêtre imposée par le fournisseur | Planifier deux à trois montées par an |
| Images des nœuds | À votre charge | Cadence de remplacement |
| Interfaces dépréciées | Ruptures annoncées à l'avance | Inventaire des usages, migration progressive |
| Composants additionnels installés | Leur propre cycle | Souvent oubliés |
| Environnements d'exécution de fonctions | Support court, dépréciation forcée | Suivi par fonction, pas globalement |

⚠️ **PIÈGE — la version d'environnement d'exécution des fonctions**
Une organisation peut avoir déployé plusieurs centaines de fonctions au fil des années, chacune avec sa version d'environnement d'exécution. Quand le fournisseur déprécie une version, toutes les fonctions concernées doivent être migrées — et l'inventaire n'existe généralement pas. Constituez-le **avant** l'annonce de dépréciation, pas après.

#### 30.5 Ce que le fournisseur corrige, et le prix

**Ce qu'il apporte** : les correctifs de l'infrastructure et, selon le service, du système et de l'environnement d'exécution, appliqués à une échelle et avec une rapidité qu'aucune organisation ne peut atteindre seule.

**Ce qu'il coûte** :

| Contrepartie | Manifestation |
|---|---|
| Perte du choix du moment | Les fenêtres sont imposées ou fortement contraintes |
| Changements sans préavis proportionné | Un comportement par défaut change à une date choisie par le fournisseur |
| Absence de retour arrière | Une fois la migration appliquée, elle n'est pas réversible |
| Preuve limitée | Vous ne pouvez pas produire de preuve technique sur la couche du fournisseur (§30.11) |

#### 30.6 Identités et droits cloud

La dette d'autorisations est au cloud ce que la dette d'annuaire est au monde classique (§24.1), avec deux aggravations : les droits sont **plus fins et plus nombreux**, et ils sont **attribués par des équipes techniques** sans processus de revue.

| Objet | Risque |
|---|---|
| Rôles trop permissifs | Attribués « pour débloquer », jamais réduits |
| Clés d'accès de longue durée | Souvent dans du code, des scripts, des fichiers d'état (§23.5) |
| Identités de service | Pratiques, mais leurs droits sont rarement revus |
| Rôles hérités entre comptes ou abonnements | Chemins d'accès transverses invisibles |
| Accès de prestataires | Configurés une fois, jamais retirés (§13.5) |

**La mesure la plus rentable** : identifier les identités disposant de droits d'administration sur un abonnement ou un projet entier, et les réduire. Elles sont peu nombreuses, et ce sont elles qui transforment un incident en catastrophe.

#### 30.7 Configuration et dérive de *tenant*

Le cloud a déplacé une part importante du risque de la vulnérabilité vers la **configuration** : stockage ouvert, base de données accessible publiquement, règle de filtrage trop large, journalisation désactivée, chiffrement non activé.

| Mécanisme | Rôle |
|---|---|
| **Contrôle de posture** | Détecte les configurations non conformes, en continu |
| **Garde-fous préventifs** | Empêchent la création d'une ressource non conforme — plus efficace que la détection |
| Description par code | Rend la configuration lisible et reproductible (§23.5) |
| Revue périodique | Traite ce que l'automatisme ne couvre pas |

✅ **BONNE PRATIQUE (P0)** — Privilégiez les **garde-fous préventifs** aux contrôles détectifs. Empêcher la création d'un stockage public coûte une politique ; détecter et corriger des stockages publics coûte un processus permanent. C'est le principe du §22.4 appliqué au cloud.

#### 30.8 Écart entre le code et la réalité

Le §23.5 s'applique avec une acuité particulière : dans le cloud, créer une ressource à la main prend trente secondes, et la tentation est constante en situation d'urgence.

**Les trois mesures** : détection périodique des ressources non décrites par le code ; interdiction de la création manuelle en production, avec une procédure d'exception tracée ; et réconciliation systématique après tout incident ayant nécessité une action manuelle (règle de reversion du §23.7).

#### 30.9 Multi-cloud et zones d'atterrissage

Une **zone d'atterrissage** est un socle standardisé — comptes, réseau, identités, journalisation, garde-fous — sur lequel les projets se déploient.

**Son intérêt pour le MCS** est direct : elle fait de la conformité un état par défaut plutôt qu'un contrôle *a posteriori*. Tout nouveau projet hérite des garde-fous, de la journalisation et des politiques d'identité.

📌 **LIMITES** — Le multi-cloud multiplie les référentiels, les mécanismes de correction, les calendriers de dépréciation et les compétences nécessaires. Chaque fournisseur supplémentaire ajoute un dispositif complet de MCS à maintenir, pas une simple extension.

#### 30.10 ✅ Livrable — Matrice de responsabilité MCS par service

| Service utilisé | Modèle | Ce que le fournisseur maintient | Ce que nous maintenons | Fenêtre imposée | Préavis | Preuve disponible | Propriétaire |
|---|---|---|---|---|---|---|---|

**Comment l'utiliser** : la renseigner service par service, la faire valider par l'équipe qui exploite le service, et l'annexer aux dossiers de conformité (§8.8). Les lignes où la colonne « preuve disponible » est vide sont vos zones à déclarer non mesurées (§7.7).

#### 30.11 🔴 FIL ROUGE — mars 2028 : l'échéance qu'on ne négocie pas

Le fournisseur cloud d'HELIOMED annonce la fin de support d'une version majeure de moteur de base de données utilisée par la plateforme HelioLink. Date limite : **quatre mois**. Passé ce délai, la migration sera appliquée automatiquement, dans une fenêtre choisie par le fournisseur.

**Ce que découvre l'équipe.** L'annonce a été publiée **onze mois plus tôt** dans les notes de service du fournisseur. Personne ne les suivait : la veille d'HELIOMED couvrait les éditeurs de logiciels et les constructeurs, pas les annonces de services cloud. C'est un trou identifié dans la matrice de couverture de décembre 2026 (§14.11), ligne « services en ligne : 11 % ».

**L'analyse d'impact.** La migration implique un changement de comportement sur le tri de certaines requêtes, ce qui affecte deux fonctionnalités d'HelioLink. Un test est nécessaire. Le développement correspondant représente trois semaines.

**Ce qui n'est pas négociable, et ce qui l'est.** La date limite ne se négocie pas. En revanche, le fournisseur accepte de fixer la fenêtre de migration à une date et une heure choisies par HELIOMED, dans la limite du délai. C'est le seul levier disponible, et il est réel.

**La séquence appliquée** : migration réalisée en environnement de recette dès la semaine suivante, correction des deux fonctionnalités, tests de non-régression, puis migration de production planifiée un samedi de juin — six semaines avant la date limite, pour conserver une marge en cas de problème.

**Les trois décisions structurelles.**

1. **La veille des services cloud** est intégrée à la matrice du §14.1, avec un responsable nommé et une revue mensuelle des annonces de service. C'était la ligne à 11 %.
2. **Les versions de services managés** entrent au référentiel d'obsolescence (§30.3), avec leurs dates de fin de support — comme n'importe quel système.
3. **La matrice de responsabilité** du §30.10 est constituée pour les onze services cloud utilisés. Elle révèle au passage deux autres échéances à moins de douze mois, jusque-là ignorées.

**Ce que Sonia Weber retient**, et qu'elle formule devant le comité : *« Nous avons passé deux ans à construire un dispositif pour décider quand nous corrigeons. Sur cette couche, la seule décision qui nous reste est celle de l'heure. »*

**Livrable de l'épisode.** La matrice de responsabilité MCS par service cloud, et l'intégration des échéances de services managés au plan d'obsolescence.

→ La suite en 🔴 §31.12, quand un connecteur autorisé en 2021 refera surface.

→ **Chapitre 31 — MCS des services en ligne, extensions et intégrations** : les services en ligne, où la configuration remplace le correctif.

#### Synthèse mentale du chapitre 30

La responsabilité diminue avec le niveau de service mais ne disparaît jamais, et les incidents se produisent dans les zones grises — images fournies mais instanciées par vous, versions majeures que vous choisissez jusqu'à une date limite, configurations par défaut qui privilégient la mise en service. Dans le cloud, l'indicateur qui remplace des centaines de constats individuels est l'âge de l'image en service. Sur les services managés, vous ne pilotez pas la correction mais l'anticipation : leurs versions doivent entrer au référentiel d'obsolescence au même titre que les systèmes d'exploitation, ce qui est l'oubli le plus fréquent. Le risque s'est largement déplacé de la vulnérabilité vers la configuration, et les garde-fous préventifs coûtent une politique là où la détection coûte un processus permanent. Enfin, chaque fournisseur supplémentaire n'ajoute pas une extension mais un dispositif complet de MCS à maintenir.

**Trois questions de vérification**

1. Votre fournisseur annonce la fin de support d'une version de service managé dans quatre mois. Qu'est-ce qui est négociable, qu'est-ce qui ne l'est pas, et quel processus aurait dû vous alerter onze mois plus tôt ?
2. Un groupe d'instances à mise à l'échelle automatique porte une vulnérabilité. Pourquoi corriger les instances est-il une perte de temps, et quel indicateur unique aurait prévenu la situation ?
3. Pourquoi un garde-fou préventif est-il structurellement supérieur à un contrôle de posture détectif, et dans quel cas le second reste-t-il indispensable ?

---

### Chapitre 31 — MCS des services en ligne, extensions et intégrations

#### 31.1 La perte de maîtrise assumée

Sur un service en ligne, vous ne choisissez ni la version, ni la date, ni le contenu de la mise à jour. Le fournisseur applique ce qu'il veut, quand il veut, à tous ses clients simultanément.

**Ce que cela change pour le MCS** : la gestion des correctifs du service lui-même sort de votre périmètre. Elle y reste pour tout ce qui l'accompagne — clients lourds, agents, connecteurs, extensions, composants auto-hébergés et interfaces que vous appelez. Ce qui la remplace est **plus difficile à outiller et plus facile à négliger** :

| Ce qui disparaît | Ce qui le remplace |
|---|---|
| Application de correctifs | Veille sur les changements du fournisseur |
| Gestion des versions | Anticipation des ruptures annoncées |
| Durcissement système | **Configuration du service** — l'objet central du chapitre |
| Gestion des accès locaux | Comptes d'administration, identités applicatives, autorisations déléguées |
| Scan de vulnérabilités | Revue de configuration et contrôle des intégrations |

**La conséquence pratique** : sur un parc de quarante services en ligne, le travail de MCS n'est pas quarante fois la même chose. C'est une **revue de configuration périodique** sur les services qui comptent, et une **surveillance des intégrations** sur tous.

#### 31.2 La veille éditeur sur les services en ligne

C'est la ligne la plus faible de la plupart des matrices de couverture (§14.1), et l'épisode du §30.11 en montre le coût.

| Source | Contenu | Difficulté |
|---|---|---|
| Notes de version du service | Changements fonctionnels et de sécurité | Volume élevé, tri nécessaire |
| Annonces de dépréciation | Fonctions et interfaces retirées | Le signal le plus important, souvent le moins visible |
| Bulletins de sécurité du fournisseur | Vulnérabilités et incidents | Publication inégale selon les fournisseurs |
| Page d'état du service | Incidents en cours | Utile en exploitation, pas en MCS |
| Communications commerciales | Évolutions d'offre, fins de vie | À ne pas négliger : une fin d'offre est une échéance |

✅ **BONNE PRATIQUE (P1) — la veille proportionnée**
Ne cherchez pas à suivre quarante services. Classez-les : ceux qui traitent des données sensibles, ceux qui disposent d'un connecteur vers votre messagerie ou vos fichiers, et ceux dont l'indisponibilité arrête une activité. Sur ceux-là — souvent cinq à dix — la veille est nominative et mensuelle. Sur les autres, une revue annuelle suffit.

#### 31.3 Les changements unilatéraux

| Type de changement | Effet possible |
|---|---|
| Fonctionnalité retirée | Un contournement de sécurité que vous aviez mis en place disparaît |
| **Paramètre de sécurité réinitialisé** | Votre configuration validée n'est plus celle que vous croyez |
| Comportement modifié | Une règle d'accès ne produit plus le même effet |
| Nouvelle fonctionnalité activée par défaut | Partage externe, intégration, assistance automatique : surface ajoutée sans décision de votre part |
| Modification des conditions d'usage | Localisation des données, sous-traitants, rétention |

⚠️ **PIÈGE — la nouvelle fonctionnalité activée par défaut**
C'est le mécanisme le plus fréquent d'élargissement involontaire de surface. Un fournisseur active une capacité de partage externe, d'intégration ou d'assistance sur l'ensemble des locataires, avec une option de désactivation que personne ne remarque. Votre configuration n'a pas changé ; votre exposition, si.
**La contre-mesure** : une revue de configuration périodique comparée à un état de référence documenté (§31.4), et non une revue « quand quelque chose change ».

#### 31.4 La configuration du locataire comme objet de MCS

C'est le cœur opérationnel du chapitre. Sur un service en ligne, votre configuration **est** votre posture de sécurité.

**Les huit familles de paramètres à documenter et contrôler :**

| Famille | Exemples |
|---|---|
| Authentification | Facteurs exigés, exceptions, durée des sessions |
| Autorisations | Rôles d'administration, délégations, accès invités |
| Partage externe | Qui peut partager quoi, avec qui, avec quelle expiration |
| Intégrations | Applications tierces autorisées, portées accordées |
| Rétention et suppression | Durées, corbeilles, restauration |
| Journalisation | Événements collectés, durée, export |
| Chiffrement et clés | Gestion des clés, chiffrement au repos et en transit |
| Restrictions d'accès | Origines autorisées, conformité des appareils (§28.8) |

**La méthode** : établir un **état de référence documenté** pour chacune de ces familles, puis le comparer périodiquement à l'état réel. C'est exactement la *baseline* du chapitre 22, appliquée à un service dont vous ne maîtrisez pas le socle.

#### 31.5 Extensions, places de marché et intégrations tierces

La surface que vous ajoutez vous-même, et la moins surveillée.

| Objet | Risque |
|---|---|
| Extension installée depuis une place de marché | Code tiers s'exécutant dans votre environnement, avec les droits accordés |
| Connecteur entre deux services | Fait transiter vos données par un troisième acteur |
| Application tierce autorisée par un utilisateur | Accès permanent, sans mot de passe, souvent surdimensionné |
| Automatisation créée par un utilisateur | Peut exfiltrer, transformer, republier des données en dehors de tout contrôle |

⚠️ **PIÈGE — l'autorisation accordée par un utilisateur**
Dans la plupart des environnements, un utilisateur ordinaire peut autoriser une application tierce à accéder à sa messagerie et à ses fichiers, en un clic, sans validation. L'accès est **permanent**, survit au changement de mot de passe, et n'apparaît dans aucun inventaire d'application.
**Les deux mesures** : restreindre le consentement utilisateur en imposant une validation administrative, et faire l'inventaire des autorisations déjà accordées (§24.4).

#### 31.6 Autorisations déléguées et jetons

Le mécanisme mérite d'être compris, parce qu'il est contre-intuitif pour qui vient du monde des mots de passe.

Une autorisation déléguée accorde à une application un accès à des ressources **au nom d'un utilisateur ou d'une organisation**, matérialisé par un jeton. Trois propriétés en découlent :

1. **La rotation du mot de passe ne révoque rien.** Le jeton reste valide.
2. **La portée est souvent excessive.** Une application qui n'a besoin que de lire un agenda demande fréquemment un accès complet à la messagerie.
3. **La durée est longue**, et le renouvellement automatique.

**La révocation** est le seul moyen de mettre fin à un accès. Elle doit figurer dans le processus de départ d'un collaborateur et dans le décommissionnement d'un service (chapitre 35).

#### 31.7 Comptes d'administration et accès invités

| Objet | Vérification |
|---|---|
| Comptes d'administration du service | Combien, nominatifs, avec authentification renforcée, revus quand ? |
| Comptes de secours | Existent-ils, sont-ils testés, sont-ils surveillés (§24.2) ? |
| Comptes de prestataires | À la demande ou permanents (§13.5) ? |
| Accès invités | Combien, depuis quand, encore justifiés ? |
| Comptes d'application | Rattachés à un propriétaire, avec des droits proportionnés ? |

**Les accès invités sont l'angle mort le plus courant** : accordés pour un projet, ils survivent des années, et donnent accès à des espaces de travail entiers.

#### 31.8 Journalisation

Trois questions à poser à chaque service en ligne, et à documenter dans la matrice du §30.10 :

1. **Quels événements** sont journalisés — connexions, accès aux données, modifications de configuration, actions d'administration ?
2. **Pendant combien de temps**, et à quel niveau de licence ? La rétention par défaut est souvent de quelques mois, parfois de quelques jours.
3. **Peut-on les exporter** vers votre propre système de collecte ?

⚠️ La question de la rétention est celle qui décide, le jour d'un incident, si vous pourrez conclure ou non (§21.3). Une rétention de 90 jours signifie que toute question portant sur une période antérieure restera sans réponse — comme dans le fil rouge du §25.22.

#### 31.9 La preuve fournie par le fournisseur

Les rapports d'audit tiers et attestations fournis par les prestataires en ligne ont une valeur réelle, et des limites précises. Ils **ne suffisent pas à eux seuls** à établir la correction de votre configuration :

| Ce qu'ils établissent | Ce qu'ils n'établissent pas |
|---|---|
| Le fournisseur dispose d'un dispositif de sécurité audité | Que **votre** configuration est correcte |
| Le périmètre audité est décrit | Que ce périmètre couvre le service que vous utilisez |
| Les contrôles ont été testés à une date | L'état actuel |

**Ce qu'il faut lire dans un tel rapport** : le périmètre exact, la période couverte, les exceptions relevées, et la liste des contrôles laissés à la charge du client — cette dernière section est celle qui vous concerne directement, et c'est celle que personne ne lit.

#### 31.10 Fin de vie d'une offre et réversibilité

Un fournisseur peut arrêter un service, être racheté, ou modifier son modèle. Trois questions à traiter **avant** la souscription, jamais après :

1. **Comment récupérer nos données ?** Format, exhaustivité, délai, coût.
2. **Quel préavis** en cas d'arrêt du service ?
3. **Que se passe-t-il pour les données à la fin du contrat ?** Suppression, délai, preuve.

#### 31.11 ⚠️ « C'est du SaaS, c'est maintenu »

Récapitulatif de ce qui reste intégralement à votre charge :

| Domaine | Ce qui reste à vous |
|---|---|
| Configuration | Intégralement |
| Identités et droits | Intégralement |
| Extensions et intégrations | Intégralement |
| Autorisations déléguées | Intégralement |
| Données | Classification, rétention, partage |
| Journalisation | Activation, export, exploitation |
| Veille sur les changements | Intégralement |
| Décision d'usage | Quel service, pour quelles données |

#### 31.12 🔴 FIL ROUGE — avril 2028 : le connecteur de 2021

La revue des autorisations déléguées, engagée par Claire Nadeau sur l'environnement collaboratif d'HELIOMED, produit une liste de 47 applications tierces disposant d'un accès.

**La répartition.**

| Catégorie | Nombre |
|---|---|
| Applications validées et connues de la DSI | 9 |
| Applications métier autorisées par un responsable, non déclarées | 14 |
| Applications autorisées par un utilisateur unique | 21 |
| **Applications dont plus personne ne connaît l'usage** | **3** |

**Le cas central.** Un outil de signature électronique, autorisé en mars 2021 par un utilisateur du service commercial pour un besoin ponctuel. L'application dispose d'un accès **en lecture à l'ensemble des messageries de l'organisation** — une portée accordée au moment du consentement, jamais réduite. L'utilisateur qui l'a autorisée a quitté l'entreprise en 2023 ; l'autorisation, elle, est restée active.

Trois faits aggravent le constat : l'éditeur de l'outil a été racheté en 2024 par une société dont HELIOMED ignore tout ; les journaux ne permettent pas de savoir si l'accès a été utilisé, et sur quelle période ; et l'application n'apparaissait dans aucun inventaire — ni celui du chapitre 10, ni celui des abonnements payés, puisque la version utilisée était gratuite.

**Les décisions.**

*Immédiat.* Révocation des 3 autorisations sans usage identifié, dont celle-ci. Aucun impact : personne ne signale de dysfonctionnement.

*Sous quinze jours.* Restriction du consentement utilisateur : toute nouvelle autorisation d'application tierce passe désormais par une validation administrative. Les 21 autorisations utilisateur existantes sont examinées une par une ; 12 sont révoquées, 6 conservées avec portée réduite, 3 régularisées.

*Structurel.* Les autorisations déléguées entrent au périmètre de référence comme **actifs de service**, avec propriétaire, date d'octroi et date de revue — au même titre que les machines (§10.4). Revue semestrielle.

**La question sans réponse.** Léa Cassin, déléguée à la protection des données, pose la même question qu'en juillet 2027 et en octobre 2027 : cet accès a-t-il été utilisé, et pour quoi ? Les journaux d'autorisation applicative ne sont conservés que 90 jours. **Sur sept ans, la question reste sans réponse.**

**Ce que Claire écrit dans sa note.** *C'est la troisième fois en un an que nous découvrons une exposition ancienne dont nous ne pouvons pas mesurer les conséquences. Le point commun n'est pas technique : à chaque fois, quelqu'un a accordé un accès sans date de fin.*

**Livrable de l'épisode.** L'inventaire des autorisations déléguées, la restriction du consentement utilisateur, et l'ajout des actifs de service au périmètre de référence.

→ La suite en 🔴 §32.7, avec le banc de test qu'on ne peut ni migrer ni remplacer.

→ **Chapitre 32 — Systèmes contraints, legacy et sanctuarisation** : les systèmes qu'on ne peut ni corriger ni migrer.

#### Synthèse mentale du chapitre 31

Sur un service en ligne, la gestion des correctifs disparaît de votre périmètre et ce qui la remplace est plus difficile à outiller : veille sur les changements, configuration du locataire, contrôle des intégrations. Le mécanisme le plus fréquent d'élargissement involontaire de surface est la fonctionnalité activée par défaut chez tous les clients — votre configuration n'a pas changé, votre exposition si, d'où la nécessité d'un état de référence comparé périodiquement. Une autorisation déléguée accordée par un simple utilisateur crée un accès permanent que la rotation du mot de passe ne révoque pas, souvent surdimensionné, et invisible de tout inventaire d'application. Les rapports d'audit du fournisseur n'établissent jamais que votre configuration est correcte, et leur section la plus utile — les contrôles laissés à la charge du client — est celle que personne ne lit. Enfin, la rétention des journaux décide, le jour d'un incident, si vous pourrez conclure.

**Trois questions de vérification**

1. Votre configuration d'un service collaboratif n'a pas été modifiée depuis six mois. Pourquoi votre exposition a-t-elle pu changer, et comment le détectez-vous ?
2. Un collaborateur quitte l'entreprise. Son compte est désactivé et son mot de passe changé. Qu'est-ce qui reste potentiellement actif, et comment y met-on fin ?
3. Un fournisseur vous transmet son rapport d'audit tiers. Quelle section lisez-vous en priorité, et pourquoi celle-là ?

---

### Chapitre 32 — Systèmes contraints, legacy et sanctuarisation

#### 32.1 Typologie et décision structurante

Tout parc comporte des systèmes qu'on ne peut ni corriger, ni migrer. Ce chapitre traite ce cas de front, parce qu'il est universel et rarement documenté.

| Type | Cause | Espoir de résolution |
|---|---|---|
| Éditeur disparu | Faillite, rachat, abandon | Nul |
| Matériel spécifique indissociable | Le logiciel pilote un équipement unique | Nul sans remplacement de l'équipement |
| Application interne non reconstructible | Équipe dissoute, chaîne de construction perdue (§26.13) | Faible |
| Certification métier figée | Toute modification invalide une qualification | Long, réglementaire |
| Coût de migration disproportionné | Remplacement supérieur à la valeur de l'usage | Budgétaire |
| Dépendance externe bloquante | Partenaire ou client imposant une version | Contractuel |

**La décision structurante**, à prendre explicitement pour chaque cas, et à réexaminer périodiquement :

```
REMPLACER   → migration ou reconstruction, avec budget et échéance
ISOLER      → sanctuarisation, avec compensations permanentes
ASSUMER     → maintien en l'état, risque accepté et documenté
```

⚠️ **PIÈGE — la non-décision**
Le cas le plus fréquent n'est aucune de ces trois options : c'est l'absence de décision. Le système reste en service, sans compensation particulière, sans dérogation, sans plan — parce que personne n'a été mis en position de trancher. C'est le §17.10 appliqué à un actif entier.

#### 32.2 Sanctuariser : ce que cela signifie réellement

Sanctuariser, c'est réduire un système à un périmètre d'usage minimal, strictement contrôlé.

**Les six dimensions à traiter**, aucune ne suffisant seule :

| Dimension | Mesure |
|---|---|
| **Réseau** | Flux réduits au strict nécessaire, dans les deux sens, avec liste explicite |
| **Accès humain** | Comptes nominatifs, nombre minimal, authentification renforcée |
| **Supports amovibles** | Interdits ou strictement contrôlés (§29.5) |
| **Données** | Ce qui entre, ce qui sort, sous quel format, avec quelle vérification |
| **Surveillance** | Toute connexion et toute modification alertent |
| **Maintenance** | Procédure écrite, intervenants identifiés, traçabilité |

**Ce qui fuit toujours**, et qu'il faut anticiper : les interventions de maintenance, les échanges de fichiers, les comptes de service utilisés par d'autres systèmes, les sauvegardes, et les supports de restauration. Une sanctuarisation qui ne traite pas ces cinq points est une sanctuarisation de façade.

#### 32.3 La rupture physique

L'isolement physique complet est souvent invoqué et rarement réel.

| Mythe | Réalité |
|---|---|
| « Le système est isolé, il n'y a aucun risque » | Les transferts de fichiers et les interventions restent des vecteurs |
| « Rien n'entre ni ne sort » | Il faut bien exporter les données de production et importer les mises à jour |
| « L'isolement dispense de maintenir » | Un système isolé mais compromis reste compromis, et la détection y est plus faible |
| « C'est irréversible » | Une connexion temporaire est ajoutée un jour, pour un besoin ponctuel, et reste |

**Ce qui rend l'isolement réel** : une procédure de transfert écrite et appliquée (§29.5), un contrôle périodique de l'absence de connexion, et l'interdiction documentée d'ajouter une liaison sans processus formel.

#### 32.4 Systèmes sous certification métier

Cas particulier fréquent dans la santé, l'industrie réglementée, l'aéronautique, la sûreté : toute modification du système invalide une qualification obtenue au prix d'un processus long et coûteux.

**Ce qu'il faut établir, et qui est souvent supposé à tort :**

1. La qualification porte-t-elle réellement sur la version du logiciel, ou sur la configuration du procédé ? Les deux cas existent, et la réponse change tout.
2. Existe-t-il une procédure de **requalification allégée** pour les correctifs de sécurité ? Beaucoup de référentiels sectoriels en prévoient une.
3. Le fournisseur propose-t-il des versions **pré-qualifiées** intégrant les correctifs de sécurité ?

⚠️ Beaucoup d'impossibilités invoquées au nom d'une certification n'ont jamais été vérifiées auprès de l'organisme concerné. Poser la question par écrit produit régulièrement une réponse plus favorable qu'attendu — et, dans le cas contraire, une justification écrite qui vaut mieux qu'une supposition.

#### 32.5 Le plan de fin de vie

Sanctuariser sans plan de sortie revient à assumer indéfiniment. Un plan de fin de vie comporte cinq éléments :

| Élément | Contenu |
|---|---|
| Jalons | Étapes datées : étude, choix, migration, décommissionnement |
| Financement | Par exercice, avec la règle du lot suivant (§12.3) |
| Points de non-retour | Moments après lesquels le report devient impossible ou très coûteux |
| Déclencheurs de réexamen | Événements imposant de revoir la décision : exploitation observée, incident, évolution réglementaire |
| Conditions de sortie de la sanctuarisation | Ce qui met fin au régime d'exception |

#### 32.6 ⚖️ La responsabilité de maintenir un système obsolète en connaissance de cause

Trois éléments sont regardés en cas d'incident ou de contrôle (§8.6) :

1. Le risque était-il **identifié** ? Un système obsolète non inventorié est une négligence ; un système obsolète documenté est une décision.
2. La décision a-t-elle été **prise au bon niveau** ? Une acceptation signée par un technicien n'engage pas l'organisation de la même façon qu'une décision de direction.
3. Des **mesures proportionnées** ont-elles été prises ? C'est le rôle des compensations du chapitre 20.

**La conclusion opérationnelle** : maintenir un système obsolète n'est pas fautif en soi. Le faire sans l'avoir identifié, décidé et compensé l'est. La dérogation formalisée du §7.4 n'est pas un exercice administratif — c'est ce qui distingue les deux situations.

#### 32.7 🔴 FIL ROUGE — mai 2028 : le banc de test et le serveur sans chaîne de construction

Deux cas de systèmes contraints arrivent au comité MCS le même mois, et ils se traitent différemment — ce qui est l'essentiel de ce chapitre.

**Cas 1 — le banc de test de validation des pompes PX-40.**

Un poste unique, sous un système hors support depuis des années, pilotant un banc de mesure indispensable à la validation réglementaire des dispositifs médicaux. Le logiciel de pilotage n'existe pas sur une version plus récente ; son éditeur a cessé son activité en 2019. Remplacer le banc complet est chiffré à environ 300 k€ et représente dix-huit mois, requalification comprise.

*Décision : **ISOLER**.* Sanctuarisation complète — retrait de tout réseau, transferts par support dédié selon la procédure du §29.5, deux comptes nominatifs, journal papier des interventions, contrôle trimestriel de l'absence de connexion. Coût total : environ 14 k€, essentiellement du matériel réseau et deux jours d'ingénierie.

*La dérogation* est signée par le directeur général, avec revue semestrielle et trois déclencheurs de réexamen : panne matérielle du poste, évolution de l'exigence réglementaire, ou disponibilité d'une solution de remplacement. Une provision est inscrite au plan pluriannuel pour le remplacement du banc à l'horizon 2031.

**Cas 2 — le serveur d'applications sans chaîne de construction.**

Application développée en interne en 2019, portée par un serveur d'applications hors support depuis 2024 (§26.13). L'équipe a été dissoute, le code source existe, mais aucune chaîne de construction fonctionnelle — personne ne sait produire un binaire à partir des sources.

*L'analyse d'usage change tout.* Avant de décider, Malik Ferhaoui mesure l'usage réel : l'application est consultée par **onze personnes**, environ deux fois par mois, pour accéder à des données historiques de 2015 à 2019.

*Décision : **REMPLACER**, mais pas comme prévu.* Plutôt que de reconstruire l'application — plusieurs mois de développement pour un usage marginal —, les données historiques sont exportées vers un espace de consultation en lecture seule sur l'infrastructure existante. Trois semaines de travail. L'application et son serveur sont **décommissionnés** en juillet, selon le processus du chapitre 35.

**Ce que la comparaison enseigne, et c'est le point du chapitre.** Deux systèmes contraints, deux décisions opposées, et dans les deux cas la décision correcte a été rendue possible par une information qui n'était pas technique : le coût de remplacement du banc, et **le nombre réel d'utilisateurs** de l'application. Aucune analyse de vulnérabilité n'aurait produit ces deux décisions.

**Ce que Claire Nadeau formule en comité** : *avant de se demander comment protéger un système qu'on ne peut pas corriger, il faut se demander à quoi il sert encore. La réponse rend parfois la question inutile — et cela ne coûte qu'une mesure d'usage.*

**Livrable de l'épisode.** Deux fiches de systèmes contraints : une sanctuarisation avec plan de fin de vie daté, un décommissionnement planifié.

→ La suite en 🔴 §33.13, avec la qualification réglementaire des produits HELIOMED.

→ **Chapitre 33 — MCS côté produit : PSIRT, divulgation coordonnée et obligations réglementaires** : le maintien d'un produit livré chez des clients.

#### Synthèse mentale du chapitre 32

Tout parc comporte des systèmes qu'on ne peut ni corriger ni migrer, et trois décisions seulement existent : remplacer, isoler, assumer. Le cas le plus fréquent n'est aucune des trois, c'est l'absence de décision — le système reste en service sans compensation, sans dérogation et sans plan, parce que personne n'a été mis en position de trancher. Sanctuariser suppose de traiter six dimensions, et ce qui fuit toujours ce sont les interventions de maintenance, les échanges de fichiers, les comptes de service, les sauvegardes et les supports de restauration. Beaucoup d'impossibilités invoquées au nom d'une certification n'ont jamais été vérifiées auprès de l'organisme concerné : poser la question par écrit produit souvent une réponse plus favorable qu'attendu. Maintenir un système obsolète n'est pas fautif en soi ; le faire sans l'avoir identifié, décidé et compensé l'est. Enfin, avant de chercher comment protéger un système non corrigeable, mesurez son usage réel : la réponse rend parfois la question inutile, pour un coût dérisoire.

**Trois questions de vérification**

1. Un système ne peut être ni corrigé ni migré et reste en service depuis quatre ans. Quelle est la question qui n'a probablement jamais été posée, et à qui ?
2. Quelles cinq voies d'entrée subsistent malgré une sanctuarisation réseau apparemment complète ?
3. En quoi une dérogation formalisée change-t-elle la situation juridique d'une organisation maintenant un système obsolète ?

---

### Chapitre 33 — MCS côté produit : PSIRT, divulgation coordonnée et obligations réglementaires

> 🎓 **MODULE AVANCÉ — fabricants et éditeurs de produits numériques.**
> Ce chapitre ne concerne pas le maintien de votre système d'information, mais celui d'un **produit que vous mettez sur le marché** et qui s'exécute chez vos clients. Il n'est pas requis pour un parcours d'exploitation. Il est en revanche indispensable si votre organisation vend un logiciel, un équipement connecté, une application ou une appliance — et il le devient réglementairement.

#### 33.1 Une différence de nature, pas de degré

| | Maintenir son SI | Maintenir un produit chez ses clients |
|---|---|---|
| Périmètre | Vos actifs | Toutes les versions déployées, chez tous les clients |
| Décision de corriger | Vous | Vous produisez le correctif, **le client décide de l'appliquer** |
| Délai | Le vôtre | Le vôtre **plus** celui d'adoption par le client |
| Visibilité | Vous voyez votre parc | Vous ne savez souvent pas qui utilise quelle version |
| Information | Vous recevez des avis | **Vous devez en publier** |
| Conséquence d'un défaut | Votre risque | Le risque de tous vos clients, simultanément |

**La conséquence structurante** : votre produit devient un composant du MCS de vos clients. Tout ce que ce cours leur enseigne à exiger de leurs fournisseurs (§13.6), ils vous le demanderont.

#### 33.2 Construire un PSIRT

Un PSIRT — l'équipe qui traite la sécurité des produits — n'est pas nécessairement une équipe dédiée. Dans une organisation de taille intermédiaire, c'est un **rôle attribué** à deux ou trois personnes, avec un processus écrit.

**Les six fonctions à couvrir** :

| Fonction | Contenu |
|---|---|
| **Réception** | Point de contact unique, joignable, surveillé — y compris hors heures ouvrées |
| **Qualification** | Reproduire, évaluer l'impact, déterminer les versions affectées |
| **Coordination** | Faire corriger par les équipes de développement, arbitrer les priorités |
| **Publication** | Rédiger et diffuser l'avis de sécurité |
| **Notification** | Informer clients et autorités selon les obligations applicables |
| **Suivi** | Mesurer l'adoption du correctif chez les clients |

**Les trois décisions à prendre au démarrage**, et à écrire :

1. **Qui décide** de publier un avis, et selon quels critères ?
2. **Quel délai** vous engagez-vous à tenir entre la réception d'un signalement et la première réponse ?
3. **Qui est joignable** un samedi d'août, et comment ?

⚠️ **PIÈGE — le point de contact qui n'existe pas**
Beaucoup d'organisations découvrent, au premier signalement, qu'un chercheur a tenté de les contacter pendant trois semaines via le formulaire commercial du site, sans réponse. Le signalement finit alors publié sans coordination. **La mesure élémentaire** : une adresse de contact sécurité publiée, surveillée, avec un accusé de réception automatique et un délai de réponse annoncé.

#### 33.3 La politique de divulgation coordonnée

**Le principe** : organiser la relation avec les personnes qui découvrent des vulnérabilités dans votre produit, de façon à ce que la correction précède la publication.

**Ce qu'une politique publiée doit contenir** :

| Élément | Contenu |
|---|---|
| Point de contact | Adresse dédiée, et moyen de chiffrer si nécessaire |
| Périmètre | Quels produits, quelles versions, ce qui est hors périmètre |
| Engagements | Délai d'accusé de réception, de qualification, de correction |
| Délai de publication | Le temps que vous demandez avant divulgation publique |
| Engagement de non-poursuite | Pour les recherches menées de bonne foi dans le périmètre |
| Reconnaissance | Mention du chercheur dans l'avis, si souhaité |

**Le fichier de découverte automatique** — un fichier `security.txt` normalisé par la **RFC 9116**, placé sous `/.well-known/security.txt` — est le geste le moins coûteux et le plus efficace : il permet à un chercheur de trouver comment vous joindre en dix secondes. Il comporte au minimum un champ `Contact` et un champ `Expires` [S-19].

**Sur les délais** : un délai de 90 jours entre le signalement et la publication est l'usage le plus répandu. Le chercheur peut publier au-delà, que vous ayez corrigé ou non. Négocier une prolongation est possible **si vous communiquez** — le silence est ce qui déclenche les publications anticipées.

#### 33.4 Attribuer des identifiants

Deux voies : devenir vous-même autorité d'attribution pour vos produits, ou passer par un tiers.

| | Devenir autorité | Passer par un tiers |
|---|---|---|
| Maîtrise du calendrier | Totale | Dépendante |
| Charge | Processus, formation, obligations de qualité | Faible |
| Crédibilité | Signal de maturité | Neutre |
| Pertinent si | Publication régulière d'avis | Quelques avis par an |

Dans les deux cas, l'important n'est pas l'identifiant mais **l'avis** : un identifiant sans avis exploitable ne sert à rien à vos clients.

#### 33.5 ⚖️ ⏱ Les obligations de signalement

*Bloc périssable, vérifié le 30/07/2026.*

Le règlement européen sur la cyberrésilience impose aux fabricants de produits comportant des éléments numériques des obligations de signalement — **article 14 du règlement** — applicables **à compter du 11 septembre 2026**, soit, à la date de vérification de ce bloc, une échéance encore à venir.

**Deux déclencheurs seulement**, et il faut les connaître précisément car ils sont plus étroits qu'on ne le croit :
1. le fabricant **a connaissance** d'une vulnérabilité de son produit **activement exploitée** ;
2. un **incident grave** affecte la sécurité du produit.

Une vulnérabilité découverte et corrigée avant toute exploitation, un correctif de routine ou une mise à jour préventive **ne relèvent pas** de l'article 14.

| Échéance | Objet | Point de départ |
|---|---|---|
| **≤ 24 h** | Alerte précoce | Prise de connaissance |
| **≤ 72 h** | Notification, avec les éléments connus et les mesures correctives ou d'atténuation disponibles | Prise de connaissance |
| **≤ 14 jours** | Rapport final, pour une **vulnérabilité activement exploitée** | **La mise à disposition d'une mesure corrective ou d'atténuation** |
| **≤ 1 mois** | Rapport final, pour un **incident grave** affectant la sécurité du produit | La notification initiale |

Le signalement s'effectue simultanément auprès de l'ENISA et du CSIRT désigné coordinateur, via la **plateforme unique de déclaration prévue à l'article 16**.

**Une obligation complémentaire souvent manquée** : l'article 14 impose également d'**informer les utilisateurs impactés** de la vulnérabilité ou de l'incident, et le cas échéant des mesures d'atténuation qu'ils peuvent déployer — de préférence dans un format structuré lisible par machine. C'est ce qui relie l'article 14 aux avis de sécurité du §33.10.

⚠️ **Ce que l'article 14 n'impose pas au 11 septembre 2026** : ni la publication d'une politique de divulgation coordonnée, ni la tenue d'un inventaire de composants, ni un processus complet de gestion des vulnérabilités. Ces exigences relèvent de l'**article 13**, applicable au 11 décembre 2027. Confondre les deux conduit à sur-dimensionner l'échéance de 2026 — ou, plus grave, à croire que l'article 14 se prépare seul.

📎 **Sources** — [S-04], [S-05], [S-06].

#### 33.6 ⏱ Ce que ces délais exigent réellement en amont

C'est le point le plus important de ce chapitre, et le plus sous-estimé : **un délai de 24 heures n'est pas une obligation de formulaire, c'est une exigence de capacité organisationnelle.**

**Ce qu'il faut avoir construit avant** :

| Capacité | Sans elle |
|---|---|
| **Détecter** qu'une vulnérabilité de votre produit est activement exploitée | Vous ne déclencherez jamais le compteur, et vous serez informé par un client ou par la presse |
| **Qualifier rapidement** le périmètre affecté : quelles versions, quels clients | Vous ne pourrez pas remplir la notification |
| **Décider sans chaîne d'approbation longue** | Vingt-quatre heures ne suffisent pas pour un circuit de validation classique |
| **Rédiger vite et correctement** | Modèles préparés à l'avance |
| **Joindre les bonnes personnes** un jour férié | Astreinte, suppléance, coordonnées à jour |

✅ **BONNE PRATIQUE (P0) — l'exercice à blanc**
Réalisez au moins une fois par an un exercice : *une vulnérabilité de notre produit est signalée comme activement exploitée, un vendredi à 18 h*. Mesurez le temps réel nécessaire pour identifier les versions affectées, joindre le décideur, et produire un projet de notification. Le résultat du premier exercice est presque toujours très supérieur à 24 heures — et c'est précisément pourquoi il faut le faire avant, pas pendant.

#### 33.7 ⏱ Les autres obligations structurantes

| Obligation | Contenu | Ce qu'elle implique |
|---|---|---|
| **Période de support** | Fournir des correctifs de sécurité pendant une durée déterminée après la mise sur le marché | Politique de versions (§25.7), et un modèle économique qui la finance |
| **Gestion des vulnérabilités du produit** | Processus documenté de traitement, y compris des composants tiers | Les chapitres 14 à 18, appliqués au produit |
| **Inventaire des composants** | Documenter les composants du produit | Le §25.11, automatisé à la construction |
| **Documentation et conformité** | Documentation technique, évaluation, marquage | Processus de conformité produit |
| **Application générale** | Échéance du **11 décembre 2027** pour l'essentiel des exigences | Le calendrier de mise en conformité se construit maintenant |

#### 33.8 ⚖️ La méthode de qualification du périmètre

**Le principe** : certains produits sont exclus parce qu'ils relèvent d'un autre régime européen qui leur est propre — notamment les dispositifs médicaux couverts par la réglementation applicable, et plusieurs autres secteurs réglementés.

⚠️ **L'exclusion ne s'analyse jamais par gamme commerciale. Elle s'analyse produit par produit.**

**La grille de questions à instruire pour chaque objet de votre offre :**

| # | Question | Pourquoi elle compte |
|---|---|---|
| 1 | Comment le produit est-il commercialisé et **mis à disposition sur le marché** ? | Détermine l'applicabilité de principe |
| 2 | **Qui est juridiquement le fabricant** ? | Marque blanche, fabrication pour compte de tiers, sous-traitance de développement changent la réponse |
| 3 | Le **service distant** associé est-il nécessaire au fonctionnement du produit, ou constitue-t-il un service autonome ? | C'est la question la plus délicate, et celle qui décide pour les plateformes en ligne associées à un équipement |
| 4 | Ces composants forment-ils **un seul produit ou plusieurs produits distincts** ? | Un ensemble commercial peut relever de plusieurs régimes |
| 5 | Une partie relève-t-elle d'un **autre règlement qui s'applique effectivement** ? | L'exclusion suppose que l'autre régime s'applique réellement, pas qu'il pourrait s'appliquer |
| 6 | La conclusion est-elle **documentée et datée** ? | Elle est opposable, et devra être justifiée |

⚠️ **Point d'attention majeur.** Une solution en ligne n'entre pas dans le champ au seul motif qu'elle est **vendue avec** un équipement. Son rôle fonctionnel doit être analysé : un service dont dépend le fonctionnement du produit ne se traite pas comme un service autonome commercialisé séparément.

#### 33.9 ⚠️ Les erreurs de qualification les plus fréquentes

| Erreur | Conséquence |
|---|---|
| Raisonner par gamme commerciale | Un produit exclu masque plusieurs produits inclus |
| **Confondre exclusion et absence d'exigences** | Le régime alternatif — notamment médical — impose ses propres exigences de cybersécurité |
| Traiter uniformément les produits **déjà mis sur le marché** | Distinction fixée par l'**article 69** : le paragraphe 2 prévoit que les produits mis sur le marché avant le 11/12/2027 ne relèvent des exigences générales qu'en cas de **modification substantielle** postérieure à cette date ; le paragraphe 3 y **déroge explicitement pour l'article 14**, dont les obligations de signalement s'appliquent à l'ensemble des produits déjà sur le marché. Un produit livré en 2020 et jamais modifié depuis doit donc disposer d'une capacité de signalement sous 24 h dès septembre 2026 [S-05] |
| Considérer la qualification comme définitive | Un changement de produit, d'usage ou de texte la remet en cause |
| Faire porter l'analyse par la seule équipe technique | C'est une analyse juridique et réglementaire, à conduire conjointement |

#### 33.10 Les avis de sécurité produit

**Ce qu'un avis exploitable contient** — et c'est exactement ce que vos clients attendent pour alimenter les chapitres 14 et 16 :

| Élément | Pourquoi |
|---|---|
| Identifiant | Dédoublonnage (§4.2) |
| **Versions affectées et versions corrigées, précisément** | Sans cela, le client ne peut rien corréler (§14.6) |
| Description de la vulnérabilité et de son impact | Qualification |
| **Vecteur d'accès et conditions d'exploitation** | L'information la plus déterminante (§14.10) |
| Gravité, avec son mode de calcul | Priorisation |
| Exploitation observée, le cas échéant | Déclenche l'urgence |
| Mesures d'atténuation en attendant la mise à jour | Permet de compenser (ch. 20) |
| Date de publication et historique des révisions | Traçabilité |

**Publier un avis lisible par machine** (§4.8) démultiplie l'utilité de tout ce qui précède : vos clients peuvent l'intégrer automatiquement.

⚠️ **La cohérence entre ce que vous publiez et ce que vous corrigez** est un point de vigilance : corriger silencieusement une vulnérabilité sans publier d'avis prive vos clients de l'information dont ils ont besoin pour prioriser leur mise à jour. C'est un choix qui se retourne systématiquement contre le fournisseur au premier incident.

#### 33.11 Maintenir les versions déployées chez les clients

| Sujet | Question |
|---|---|
| Matrice de support | Quelles versions recevront ce correctif ? |
| Rétroportage | Corrigez-vous les versions antérieures, et lesquelles (§25.5) ? |
| Mécanisme de mise à jour | Est-il sûr, atomique, réversible (§6.11) ? |
| Adoption | **Savez-vous combien de clients ont appliqué le correctif ?** |
| Clients refusant la mise à jour | Que faites-vous, et qu'avez-vous tracé ? |

**La question de l'adoption est celle que la plupart des éditeurs ne savent pas traiter.** Publier un correctif ne réduit le risque de personne tant qu'il n'est pas appliqué. Deux leviers : mesurer l'adoption quand le produit le permet, et **communiquer directement** aux clients concernés plutôt que de se contenter d'une publication passive.

**Le client qui refuse** relève du même raisonnement que le §32.6 : la trace écrite de votre notification, et de son refus, détermine la répartition des responsabilités le jour de l'incident.

#### 33.12 📌 Limites

- **Marque blanche et fabrication pour compte de tiers** : qui publie l'avis, qui notifie ? À régler contractuellement, avant l'incident.
- **Composants intégrés fournis par des tiers** : vous dépendez de leur délai de correction, et vos clients dépendent du vôtre.
- **Sous-traitance de développement** : la responsabilité reste au fabricant, quel que soit l'auteur du code.
- **Produits anciens encore déployés** : la période de support engagée doit être tenue même si le produit n'est plus commercialisé.

#### 33.13 🔴 FIL ROUGE — juin 2028 : la qualification produit par produit

Vingt et un mois après la mise en service du dispositif minimal de septembre 2026 (§8.10), HELIOMED conduit sa **revue de maturité produit**. Yann Prigent et le docteur Hélène Fabre reprennent la qualification réglementaire des quatre produits, cette fois avec un appui juridique externe et le temps de l'argumenter. Deux semaines de travail, une note de neuf pages.

**Ce que la revue confirme** : la qualification prudente de 2026 était correcte sur les trois cas tranchés. **Ce qu'elle corrige** : le statut d'HelioLink, traité par défaut comme inclus, méritait une analyse distinguant ses deux modes de commercialisation. **Ce qu'elle révèle** : le dispositif de 2026 n'aurait pas tenu un délai de 24 heures — c'est l'objet de l'exercice à blanc ci-dessous.

> ⚠️ **Les conclusions ci-dessous découlent des caractéristiques fictives décrites dans ce cas.** Elles illustrent une **méthode d'analyse**, non un résultat transposable : chaque produit réel doit faire l'objet de sa propre qualification.

**Les quatre produits, et leur traitement.**

| Produit | Description retenue dans le cas | Conclusion | Motif |
|---|---|---|---|
| **PX-40** — pompe à perfusion | Dispositif médical au sens de la réglementation applicable, marqué à ce titre | **Exclu du règlement cyberrésilience** | Le régime médical s'applique effectivement — question 5 de la grille |
| **HelioBox** — passerelle hospitalière | Équipement connecté générique, commercialisé séparément, non revendiqué comme dispositif médical | **Dans le périmètre** | Produit avec éléments numériques mis sur le marché — questions 1 et 4 |
| **HelioMove** — application mobile de bien-être | Application grand public, sans revendication médicale | **Dans le périmètre** | Logiciel mis sur le marché |
| **HelioLink** — plateforme de télésuivi | **Statut ouvert** | **À trancher** | Question 3 : le service est-il autonome, ou nécessaire au fonctionnement de HelioBox ? |

**Le cas HelioLink occupe l'essentiel de l'analyse.** La plateforme est commercialisée sous deux formes : un abonnement autonome souscrit par des établissements de santé, et une offre couplée où HelioBox ne fonctionne qu'avec elle. Selon la forme, le raisonnement diffère. La note conclut en distinguant explicitement les deux cas d'usage et retient l'hypothèse la plus contraignante pour la conception du dispositif — décision de prudence assumée et documentée.

**Ce que la qualification déclenche concrètement.**

1. **PSIRT** : le rôle minimal de 2026 est structuré — deux suppléants au lieu d'un, politique de divulgation coordonnée publiée avec un délai de 90 jours, fichier de découverte automatique conforme à la spécification en vigueur ajouté sur les sites.
2. **Capacité de notification** : modèles de notification préparés, chaîne de décision pré-autorisée — Yann peut déclencher une notification sans validation préalable de la direction générale, avec information immédiate.
3. **Exercice à blanc** : réalisé en juillet. Résultat du premier essai : **31 heures** pour produire un projet de notification exploitable, contre 24 exigées. Les deux points de blocage identifiés sont l'inventaire des versions déployées chez les clients, et la joignabilité du responsable juridique un dimanche. Corrigés en septembre ; le second exercice descend à 9 heures.
4. **Inventaire des versions déployées** : c'était le trou principal. HELIOMED ne savait pas quelle version de HelioBox tournait chez quel client. Un mécanisme de remontée de version est ajouté au produit — avec l'accord des clients, et avec une analyse d'impact sur les données personnelles conduite par Léa Cassin.
5. **Inventaire des composants** : généré automatiquement à la construction pour HelioLink et HelioBox (§25.11), conservé par version publiée.

**Le point le plus révélateur.** L'exercice à blanc montre que l'obstacle n'était ni juridique, ni technique : c'était l'**absence d'inventaire des versions déployées chez les clients**. HELIOMED savait maintenir son propre parc depuis deux ans ; elle ne savait pas ce qui tournait chez les siens.

**Ce que Yann Prigent écrit en conclusion de la note** : *nous avons appliqué à nos clients ce que nous reprochions à nos fournisseurs.*

→ La suite en 🔴 §34.12, quand la console de sauvegarde révélera son propre retard.

→ **Chapitre 34 — MCS des outils de sécurité, du contenu de détection et des sauvegardes** : les outils de sécurité eux-mêmes, souvent les plus en retard.

#### Synthèse mentale du chapitre 33

Maintenir un produit chez ses clients diffère en nature du maintien de son SI : vous produisez le correctif, le client décide de l'appliquer, et vous ignorez souvent quelle version tourne chez qui. Un PSIRT n'est pas nécessairement une équipe mais un rôle attribué couvrant six fonctions, dont la première — un point de contact réellement surveillé — manque à la plupart des organisations au moment du premier signalement. Les délais de notification réglementaires ne sont pas une obligation de formulaire mais une exigence de capacité organisationnelle : détecter l'exploitation, qualifier le périmètre, décider sans circuit long, et joindre les bonnes personnes un jour férié. L'exclusion du champ réglementaire s'analyse produit par produit, jamais par gamme, et exclusion ne signifie pas absence d'exigences. Enfin, publier un correctif ne réduit le risque de personne tant qu'il n'est pas appliqué : la mesure de l'adoption chez les clients est le sujet que la plupart des éditeurs ne traitent pas.

**Trois questions de vérification**

1. Une vulnérabilité de votre produit est signalée comme activement exploitée un vendredi à 18 h. Listez les cinq capacités que vous devez déjà posséder pour tenir un délai de 24 heures.
2. Votre gamme comprend un dispositif réglementé, un équipement générique et une application mobile. Pourquoi ne pouvez-vous pas conclure d'un seul examen, et quelles questions instruisez-vous pour chaque objet ?
3. Vous publiez un correctif de sécurité pour votre produit. Pourquoi le risque n'a-t-il pas encore diminué, et que faites-vous ?

---

### Chapitre 34 — MCS des outils de sécurité, du contenu de détection et des sauvegardes

#### 34.1 Pourquoi les outils de sécurité sont les plus en retard

Le constat est régulier, et contre-intuitif : les outils censés protéger le système d'information figurent souvent parmi ses composants les moins maintenus.

**Les cinq mécanismes qui produisent ce retard**, tous parfaitement rationnels pris isolément :

| Mécanisme | Raisonnement implicite |
|---|---|
| « C'est un outil de sécurité, donc il est sécurisé » | Aucun lien logique, mais le raisonnement est répandu |
| Mettre à jour interrompt la protection | Pendant la mise à jour, la surveillance est dégradée — argument réel |
| L'outil est utilisé quotidiennement par l'équipe | L'interrompre gêne ceux qui décident de l'interrompre |
| Aucun métier ne le réclame | Il ne figure sur aucune feuille de route |
| Il n'est pas exposé à Internet | Confusion entre exposition et criticité (§11.7) |

**Le rappel qui tranche** : ces outils sont des **actifs de niveau 0**. La console de sauvegarde accède à toutes les données, l'outil de déploiement exécute du code partout, le scanner détient les identifiants privilégiés du parc (§15.3), le coffre-fort concentre les accès. Leur compromission n'est pas un incident de sécurité parmi d'autres : c'est la fin de la partie.

#### 34.2 Deux objets distincts : le logiciel et le contenu

C'est la distinction structurante du chapitre, et elle est presque toujours confondue.

| | Le logiciel | Le contenu |
|---|---|---|
| De quoi s'agit-il | Console, agents, serveurs | Signatures, règles, modèles, listes |
| Rythme de mise à jour | Mensuel à trimestriel | **Quotidien, parfois horaire** |
| Ce qui se dégrade | Vulnérabilités, fin de support | **Pertinence de la détection** |
| Comment on le mesure | Version installée | **Date du dernier contenu appliqué** |
| Qui s'en occupe | Exploitation | Souvent personne explicitement |

**Une console à jour dont les règles datent de trois mois dégrade fortement la couverture des menaces récentes.** Et symétriquement, un contenu parfaitement à jour sur un logiciel hors support s'exécute sur une base vulnérable. Les deux doivent être suivis séparément.

#### 34.3 Maintenir le contenu de détection

**Les dix objets à suivre**, avec leur cadence propre :

| Objet | Cadence attendue | Indicateur |
|---|---|---|
| Signatures et moteur antimalware | Quotidienne | Âge du dernier contenu, par machine |
| Politiques de protection des postes | Mensuelle | Date de dernière revue |
| Règles de détection et de corrélation | Continue | Nombre de règles, date de dernière modification |
| Règles de filtrage applicatif | Continue | Couverture, faux positifs |
| Signatures de sonde réseau | Quotidienne à hebdomadaire | Âge du contenu |
| Listes de blocage et flux de réputation | Quotidienne | Fraîcheur, taux d'erreur |
| Base de détection du scanner | Quotidienne | Âge (§15.5) |
| Analyseurs de journaux | À chaque changement de format source | Taux d'événements non analysés |
| Connecteurs d'orchestration | À chaque évolution d'API | Taux d'échec |
| Certificats de confiance de la chaîne d'outillage | Selon expiration | Inventaire (§24.6) |

**Les deux lignes les plus négligées** sont les analyseurs de journaux et les connecteurs. Un changement de format de journal côté source casse silencieusement l'analyse : les événements arrivent, ne sont plus interprétés, et disparaissent des règles de détection. Le tableau de bord reste vert.

✅ **BONNE PRATIQUE (P0)** — Suivez le **taux d'événements non analysés** par source. Une hausse soudaine signale un changement de format, donc une perte de détection invisible à tous les autres indicateurs.

#### 34.4 Le cycle de vie des exclusions

**Le mécanisme.** Une application métier déclenche des faux positifs ; on ajoute une exclusion pour débloquer la production. L'exclusion est légitime. Elle n'est jamais revue.

**Ce que produit l'accumulation**, après quelques années : des répertoires entiers exclus de l'analyse, parfois des extensions de fichiers, parfois des processus complets. Un attaquant qui découvre ces exclusions dispose d'un espace où déposer et exécuter ce qu'il veut sans être détecté.

**Le traitement**, identique à celui des dérogations (§7.4) :

| Exigence | Contenu |
|---|---|
| Inventaire | Liste complète des exclusions, tous outils confondus |
| Justification | Pourquoi, pour quelle application, sur demande de qui |
| Portée minimale | Un processus précis plutôt qu'un répertoire entier |
| Date d'expiration | Et revue à échéance |
| Compensation | Surveillance spécifique de la zone exclue |

⚠️ Une exclusion **large et permanente** sur un répertoire accessible en écriture par des comptes ordinaires est l'une des configurations les plus dangereuses qu'on rencontre en audit.

#### 34.5 Vérifier que la protection fonctionne encore

Un agent installé n'est pas un agent qui fonctionne. Cinq états à distinguer, qui se ressemblent tous dans un tableau de bord mal conçu :

| État | Signification |
|---|---|
| Actif et à jour | Situation nominale |
| Actif, contenu ancien | Protection dégradée |
| Installé, service arrêté | **Aucune protection** |
| Installé, ne communique plus avec la console | Aucune visibilité — et souvent aucune protection |
| Non installé | Absent des indicateurs de l'outil |

**Le dernier état est le plus dangereux** : une machine sans agent n'apparaît pas dans la console, donc pas dans le taux de conformité. C'est très exactement le problème du dénominateur (§10.11), appliqué aux outils de sécurité. La couverture se calcule **sur le périmètre de référence**, jamais sur ce que l'outil connaît.

✅ **BONNE PRATIQUE (P1)** — Réalisez périodiquement un **test de fonctionnement contrôlé** : déposer sur un échantillon de machines un fichier de test standard prévu à cet effet, et vérifier que la détection remonte bien jusqu'à la console. Cela vérifie la chaîne complète — agent, communication, console, alerte — et non la seule présence du logiciel.

#### 34.6 Sauvegardes : maintenir l'infrastructure qui vous sauvera

L'infrastructure de sauvegarde est simultanément le dernier recours et une cible privilégiée.

| Objet | Point d'attention |
|---|---|
| Console de sauvegarde | Actif de niveau 0 : accès à toutes les données. Jamais joignable depuis le réseau bureautique |
| Agents de sauvegarde | Présents sur toutes les machines, souvent privilégiés, rarement mis à jour |
| Support de stockage | Immuabilité : une sauvegarde modifiable par un attaquant n'est pas une sauvegarde |
| Comptes de service | Droits étendus par nature, mots de passe souvent anciens (§24.2) |
| Copies hors ligne | Le seul recours contre une compromission de l'infrastructure elle-même |

⚠️ **PIÈGE — la sauvegarde restaurée qui réintroduit la vulnérabilité**
Une restauration ramène le système à son état d'origine, correctifs compris — c'est-à-dire non compris. C'est l'une des cinq causes de récurrence du §17.9. **Tout retour à un état antérieur déclenche un contrôle de conformité** avant remise en service.

**Le test de restauration** est à la sauvegarde ce que le test de retour arrière est au correctif (§18.8) : sans lui, vous avez une intention, pas une capacité. Il se planifie, se chronomètre, et son résultat se documente.

#### 34.7 Articulation avec la continuité d'activité

| Ce que la sauvegarde compense | Ce qu'elle ne compense pas |
|---|---|
| Perte de données | La compromission elle-même : restaurer un système compromis le restaure compromis |
| Destruction d'un système | Le temps de reconstruction, souvent très supérieur aux attentes |
| Erreur humaine | La fuite de données : une donnée exfiltrée reste exfiltrée |
| Défaillance matérielle | Une vulnérabilité présente dans la sauvegarde |

**La conclusion pour le MCS** : la sauvegarde n'est pas une alternative au maintien en condition de sécurité. Une organisation qui néglige le MCS en comptant sur ses sauvegardes découvre, le jour de l'incident, qu'elle restaure des systèmes vulnérables dans un environnement où l'attaquant est peut-être encore présent.

#### 34.8 Remédiation après compromission : corriger ou reconstruire

C'est la question centrale d'un retour à un état de confiance, et elle a été rencontrée deux fois dans le fil rouge (§21.11).

| Situation | Décision |
|---|---|
| Vulnérabilité corrigée avant toute exploitation | Correction suffisante |
| Exploitation possible, aucune preuve de compromission, journalisation suffisante | Correction + recherche approfondie |
| Exploitation possible, **journalisation insuffisante** | **Reconstruction**, sauf si un état de confiance peut être démontré autrement |
| Compromission avérée | Reconstruction, après préservation des éléments d'enquête |
| Équipement de bordure ayant subi une exploitation | Reconstruction — la persistance y est fréquente et difficile à détecter |

**L'ordre des opérations** en cas de compromission avérée : préserver les traces avant toute action ; comprendre le périmètre avant de reconstruire ; reconstruire à partir d'une source de confiance, pas d'une sauvegarde postérieure à la compromission ; changer les secrets susceptibles d'avoir été exposés ; et rétablir la surveillance avant la remise en service.

⚠️ **Le conflit à connaître à l'avance** : corriger vite peut détruire les preuves. Sur un équipement suspecté compromis, la décision de préserver ou de corriger doit être prise consciemment, par le pilote de crise (§21.7), et non subie par réflexe.

#### 34.9 Le MCS pendant une crise majeure

Pendant un incident majeur, le MCS courant doit être suspendu et repriorisé, sinon il consomme des ressources indispensables ailleurs.

| Décision | Contenu |
|---|---|
| **Gel du MCS courant** | Les campagnes en cours sont suspendues, sauf celles qui traitent le vecteur de l'incident |
| **Priorité au vecteur** | Le chemin d'entrée est corrigé partout, en priorité absolue |
| **Reconstruction propre** | Les systèmes reconstruits le sont à un niveau de correctif à jour, pas à l'état antérieur |
| **Reprise progressive** | Le MCS courant reprend après stabilisation, avec un rattrapage planifié |

**Le point de vigilance** : la reconstruction en urgence produit des configurations non conformes et des exceptions temporaires. Elles doivent être **inventoriées pendant la crise** — le journal de décision du §21.5 y sert — pour être traitées après, plutôt que découvertes deux ans plus tard comme le serveur d'impression du §23.7.

#### 34.10 📌 Limites

- **La protection des postes ne remplace pas les correctifs** : elle détecte des comportements, elle ne supprime pas les vulnérabilités.
- **La détection dépend de la journalisation** : sans journaux, pas de règles, quel que soit l'outil.
- **Les outils de sécurité augmentent la surface** : agents privilégiés, consoles, connecteurs. Chaque outil ajouté est un actif de niveau 0 supplémentaire à maintenir.
- **Le contenu de détection ne couvre que le connu** : c'est utile, et insuffisant seul.

#### 34.11 ✅ Recommandations priorisées

| Prio | Action |
|---|---|
| **P0** | Classer tous les outils de sécurité et plans de gestion en C1, avec fenêtre récurrente |
| **P0** | Retirer les consoles d'administration du réseau bureautique |
| **P0** | Suivre séparément la version du logiciel et l'âge du contenu de détection |
| **P0** | Calculer la couverture des agents sur le **périmètre de référence**, pas sur la console |
| P1 | Inventorier et borner les exclusions, avec compensation |
| P1 | Test de fonctionnement contrôlé périodique |
| P1 | Contrôle de conformité systématique après toute restauration |
| P1 | Test de restauration chronométré et documenté |
| P2 | Suivi du taux d'événements non analysés par source |

#### 34.12 🔴 FIL ROUGE — juillet 2028 : la console de sauvegarde

La revue des outils de sécurité et des plans de gestion d'HELIOMED, conduite en juillet, produit le tableau suivant.

| Outil | Version | Retard | Exposition |
|---|---|---|---|
| Console de sauvegarde | N-4 | **14 mois** | Joignable depuis l'ensemble du réseau bureautique |
| Console de protection des postes | N-1 | 3 mois | Réseau d'administration |
| Outil de scan | N-2 | 7 mois | Réseau d'administration |
| Plateforme de journalisation | N-1 | 4 mois | Réseau d'administration |
| Console de virtualisation | N-3 | 11 mois | Réseau d'administration |

**Le cas de la console de sauvegarde.** Quatorze mois de retard, deux vulnérabilités critiques publiées sur cette version dont une figurant au catalogue d'exploitation avérée, et un accès depuis n'importe quel poste du siège. La console dispose d'un accès en lecture à l'intégralité des données sauvegardées — c'est-à-dire à tout.

**Pourquoi elle n'avait jamais été traitée**, et l'analyse est instructive : elle n'était pas exposée à Internet, donc n'apparaissait dans aucune priorisation fondée sur l'exposition externe ; sa mise à jour interrompt les sauvegardes, donc nécessitait une fenêtre que personne n'avait demandée ; et elle appartenait à l'équipe exploitation, qui la considérait comme son outil de travail plutôt que comme un actif à maintenir. Les trois mécanismes du §34.1, simultanément.

**Les décisions.**

*Immédiat, en deux jours* : la console est retirée du réseau bureautique et placée sur le réseau d'administration, accessible uniquement depuis les postes d'administration dédiés (§28.4). Cette seule mesure supprime le chemin d'attaque principal, sans aucune interruption de sauvegarde.

*Sous trois semaines* : mise à jour des cinq outils, par ordre de criticité, avec fenêtres dédiées. La console de sauvegarde d'abord.

*Structurel* : les cinq outils entrent en classe C1 avec fenêtre récurrente mensuelle. Un indicateur dédié — **âge de version des outils de sécurité et plans de gestion** — entre au tableau de bord du comité MCS.

**La découverte annexe.** L'inventaire des exclusions de la protection des postes remonte **37 exclusions**, dont 9 portant sur des répertoires complets, et 4 sans aucune justification documentée. L'une d'elles, ajoutée en 2022, exclut un répertoire de dépôt de fichiers accessible en écriture par tous les utilisateurs du siège. Elle est supprimée le jour même ; les 8 autres exclusions larges sont réduites à des processus précis en trois semaines.

**Le test de fonctionnement**, réalisé pour la première fois sur un échantillon de 30 postes : 27 détections remontées à la console, **3 machines sans réaction**. Analyse : deux agents dont le service était arrêté depuis plusieurs mois, un agent ne communiquant plus avec la console depuis un changement de configuration réseau en 2027. Aucune de ces trois machines n'apparaissait comme non conforme — elles n'apparaissaient simplement plus du tout.

**Ce que Claire Nadeau écrit au comité.** *Nous avons passé deux ans et demi à réduire notre exposition. Le chemin le plus direct vers l'ensemble de nos données passait par l'outil chargé de les protéger, et il était ouvert depuis le premier jour.*

→ **Fin de la Partie V.** La suite en 🔴 §35.14, avec le décommissionnement des systèmes que ces deux années ont rendus inutiles.

→ **Chapitre 35 — Décommissionnement sécurisé** : retirer proprement ce qui ne sert plus.

#### Synthèse mentale du chapitre 34

Les outils de sécurité figurent régulièrement parmi les composants les moins maintenus, pour cinq raisons rationnelles prises isolément — dont la confusion entre exposition externe et criticité. Ce sont pourtant des actifs de niveau 0 : leur compromission n'est pas un incident parmi d'autres. Deux objets distincts doivent être suivis séparément, le logiciel et le contenu : une console à jour dont les règles datent de trois mois ne détecte rien de récent. Les exclusions s'accumulent sans jamais être revues et créent des zones où un attaquant peut opérer sans être vu ; elles se traitent comme des dérogations, avec portée minimale et date d'expiration. Une machine sans agent n'apparaît pas dans la console, donc pas dans le taux de conformité : la couverture se calcule sur le périmètre de référence. Enfin, la sauvegarde n'est pas une alternative au MCS — restaurer un système compromis le restaure compromis, et restaurer un système vulnérable réintroduit la vulnérabilité.

**Trois questions de vérification**

1. Votre console de protection des postes affiche 99 % de conformité. Quelles deux populations ce chiffre ignore-t-il structurellement, et comment les retrouvez-vous ?
2. Pourquoi une exclusion antimalware large et permanente est-elle plus dangereuse qu'une vulnérabilité critique non corrigée sur le même serveur ?
3. Un équipement de bordure a pu être exploité, mais vos journaux ne remontent que 30 jours. Corrigez-vous ou reconstruisez-vous, et sur quel critère tranchez-vous ?

---

---

> ### 🎓 À ce stade de la Partie V, vous savez…
>
> - **aborder** un environnement industriel sans réflexes bureautiques, et construire une chaîne de mise à jour hors ligne gouvernée ;
> - **piloter** l'anticipation plutôt que la correction sur les services managés, et placer leurs versions au référentiel d'obsolescence ;
> - **traiter** un service en ligne par sa configuration, ses intégrations et ses autorisations déléguées, faute de pouvoir le corriger ;
> - **trancher** entre remplacer, isoler et assumer sur un système contraint — après avoir mesuré son usage réel ;
> - **construire** une capacité de signalement produit, et qualifier un périmètre réglementaire produit par produit ;
> - **maintenir** les outils de sécurité eux-mêmes, en distinguant le logiciel du contenu de détection.
>
> **Ce que vous ne savez pas encore** : comment faire tenir tout cela dans la durée. C'est l'objet de la Partie VI.


## PARTIE VI — Fin de vie, industrialisation et soutenabilité

Cette partie traite ce qui fait tenir un programme de MCS dans la durée : retirer proprement ce qui ne sert plus, automatiser ce qui peut l'être, financer et rendre le travail soutenable, mesurer, et prouver.

---

### Chapitre 35 — Décommissionnement sécurisé

#### 35.1 Le cycle de vie ne s'achève pas à « migration effectuée »

Un système remplacé mais non retiré cumule tous les défauts : il n'est plus maintenu puisqu'il n'est plus utilisé, il reste joignable puisque personne ne l'a débranché, et il conserve ses comptes, ses secrets et ses accès. C'est l'actif idéal pour un attaquant : privilégié, oublié, et surveillé par personne.

**Les cinq résidus typiques d'un décommissionnement incomplet** :

| Résidu | Conséquence |
|---|---|
| Enregistrement de nom toujours actif | Le service semble exister ; une réattribution d'adresse peut créer une confusion exploitable |
| Compte de service toujours valide | Accès conservé sur d'autres systèmes |
| Règle de filtrage toujours ouverte | Un chemin réseau subsiste vers ce qui remplace l'ancien système |
| Sauvegardes restaurables | Les données existent encore, sans propriétaire |
| Machine éteinte mais non supprimée | Rallumée un jour « pour vérifier quelque chose », dans un état d'il y a trois ans |

**Le décommissionnement est donc un acte de MCS à part entière**, au même titre que l'application d'un correctif — et il figure explicitement dans la définition du §1.1.

#### 35.2 La décision de retrait

| Élément | Contenu |
|---|---|
| Déclencheur | Migration terminée, usage nul, fin de support, fin de contrat |
| **Mesure de l'usage réel** | Avant tout, comme au §32.7 : qui l'utilise, à quelle fréquence ? |
| Décideur | Propriétaire métier (§9.2) |
| Communication | Préavis proportionné, diffusé largement |
| Période d'observation | Extinction avant suppression, pour révéler les usages non déclarés |

✅ **BONNE PRATIQUE (P0) — l'extinction avant la suppression**
Éteignez avant de supprimer, et observez. Une à quatre semaines selon la criticité. C'est la méthode la plus fiable pour découvrir les dépendances non documentées — celles que §10.5 ne trouve pas, notamment les traitements mensuels ou annuels. Le préavis, lui, réveille les utilisateurs : dans le fil rouge du §5.5, il avait suffi à faire réapparaître onze propriétaires sur vingt-neuf.

#### 35.3 Identifier les dépendances

| Type | Comment le trouver |
|---|---|
| Flux entrants | Analyse des connexions sur une période représentative (§10.5) |
| Flux sortants | Idem — souvent oubliés |
| Tâches planifiées ailleurs | Recherche du nom d'hôte dans les configurations et les scripts |
| Intégrations applicatives | Recherche dans les fichiers de configuration des applications |
| Comptes utilisés ailleurs | Le compte de service de cette machine sert-il sur d'autres systèmes ? |
| Certificats | Émis pour ce service, utilisés par un autre ? |
| Documentation et procédures | Références au système dans les procédures d'exploitation |

⚠️ **PIÈGE — la dépendance annuelle**
Une analyse de flux sur trois semaines manque le traitement de clôture annuelle. C'est la raison pour laquelle la période d'observation en extinction doit couvrir, pour un système ancien, au moins un cycle métier — ou être assortie d'une recherche documentaire explicite.

#### 35.4 Traitement des données

| Étape | Exigence |
|---|---|
| Inventaire des données | Quelles données, quelle sensibilité, quelle durée de conservation légale ou contractuelle |
| Migration ou archivage | Vers où, sous quel format, avec quelle vérification d'intégrité |
| **Vérification de lisibilité** | Un archivage illisible dans cinq ans n'est pas un archivage |
| Effacement | Méthode adaptée au support et à la sensibilité |
| **Preuve d'effacement** | Attestation, journal, certificat de destruction |

**Le point souvent manqué** : l'effacement doit couvrir **toutes** les copies — instantanés, environnements de recette alimentés par une copie (§28.1), exports temporaires, et sauvegardes selon leur politique de rétention.

#### 35.5 Retrait des points d'entrée

| Objet | Action |
|---|---|
| Enregistrements de résolution de noms | Suppression, y compris les alias et les entrées internes |
| Publications externes | Retrait de la publication, vérification depuis l'extérieur (ch. 11) |
| Règles de filtrage | Suppression, pas seulement désactivation |
| Entrées de répartiteur de charge | Retrait de la grappe |
| Certificats | Révocation, retrait des magasins où ils étaient déclarés |
| Références dans d'autres configurations | Recherche systématique du nom et de l'adresse |

#### 35.6 Révocations

C'est la section la plus oubliée, et celle qui produit les résidus les plus dangereux.

| Objet | Action |
|---|---|
| Comptes utilisateurs locaux | Suppression |
| **Comptes de service** | Suppression, après vérification qu'ils ne servent nulle part ailleurs (§24.11) |
| Clés d'accès distant | Retrait des clés autorisées, sur ce système **et** sur ceux qu'il administrait |
| Clés d'API et jetons | Révocation côté fournisseur, pas seulement suppression locale |
| Secrets dans les coffres-forts | Suppression, avec vérification des consommateurs |
| **Autorisations déléguées** | Révocation côté service concerné (§31.6) |
| Certificats clients | Révocation |
| Appartenances à des groupes | Retrait |

⚠️ **La révocation côté fournisseur** est le point critique : supprimer une clé d'un fichier de configuration ne l'invalide pas. Tant qu'elle n'est pas révoquée à la source, elle reste utilisable par quiconque en détient une copie.

#### 35.7 Retrait de l'outillage

| Outil | Action | Effet si oublié |
|---|---|---|
| Supervision | Retrait des sondes | Alertes permanentes que l'on finit par ignorer |
| Scanner de vulnérabilités | Retrait du périmètre | Constats sur un actif inexistant (§15.11, faux positif n° 10) |
| Protection des postes | Désinstallation de l'agent, retrait de la console | Licence consommée, machine fantôme dans les indicateurs |
| Sauvegarde | Arrêt des travaux, décision sur les sauvegardes existantes | Sauvegardes orphelines, coût de stockage |
| Gestion de configuration | Retrait du périmètre de convergence | Erreurs récurrentes |
| Outil de déploiement | Retrait | Actif compté dans le dénominateur, jamais joignable |
| **Inventaire** | Passage au statut « décommissionné », **sans suppression de l'historique** | Perte de la trace |

#### 35.8 Sauvegardes existantes

Question à trancher explicitement : que fait-on des sauvegardes d'un système retiré ?

| Option | Quand |
|---|---|
| Conservation jusqu'à expiration de la rétention normale | Cas général |
| Conservation prolongée pour raison légale | Obligation de conservation identifiée |
| Suppression anticipée | Données sensibles sans obligation de conservation |

**Dans tous les cas** : la décision est documentée, une date de suppression effective est fixée, et un propriétaire en répond. Une sauvegarde restaurable d'un système décommissionné il y a quatre ans est un risque sans bénéfice.

#### 35.9 Matériel et licences

Récupération des licences réaffectables, effacement des supports de stockage avec preuve, destruction ou restitution du matériel avec traçabilité, retrait du parc et de l'assurance. Pour le matériel loué ou repris par un tiers, l'effacement doit être vérifié **avant** la restitution, pas supposé.

#### 35.10 Clôture contractuelle

Résiliation des contrats de support associés, arrêt des abonnements liés, retrait des accès du fournisseur (§13.5), récupération des données détenues par le fournisseur, et confirmation écrite de la suppression de son côté.

#### 35.11 Vérification finale

**La règle** : un décommissionnement se **vérifie**, il ne se déclare pas.

| Contrôle | Méthode |
|---|---|
| Absence de réponse réseau | Test depuis plusieurs points du réseau |
| Absence dans les sources d'inventaire | Rejeu de la réconciliation (§10.3) |
| Absence d'exposition externe | Nouvelle passe de découverte externe (ch. 11) |
| Absence de comptes actifs | Recherche par nom dans l'annuaire |
| Absence de références résiduelles | Recherche du nom d'hôte dans les configurations |
| **Délai d'observation** | 30 à 90 jours, pour détecter les usages résiduels |

#### 35.12 ✅ Livrable — Procès-verbal de décommissionnement

| Section | Contenu |
|---|---|
| Identification | Actif, propriétaires, date de mise en service |
| Décision | Motif, décideur, date, préavis diffusé |
| Dépendances | Identifiées, traitées, avec preuve |
| Données | Migrées, archivées, effacées — avec attestation |
| Points d'entrée | Retirés, avec vérification |
| Révocations | Liste des comptes, clés, secrets, autorisations révoqués |
| Outillage | Retraits effectués |
| Sauvegardes | Décision, date de suppression prévue |
| Matériel et licences | Traitement, preuve de destruction ou de restitution |
| Contrats | Résiliations |
| **Vérification finale** | Contrôles réalisés, date, résultat |
| Signature | Propriétaire métier et propriétaire technique |

#### 35.13 🔬 Mini-lab 8 — Décommissionner un serveur

**Objectif** — Repérer les oublis d'un décommissionnement déclaré terminé, et produire le PV manquant.
**Durée** 45 min · **Difficulté** 🔴 avancé · **Prérequis** §35.5 à §35.11, §24.5 · **Livrable** formulaire D.14 rempli + actions correctives.
**Compétences validées** — ✔ identifier les résidus d'un décommissionnement ✔ révoquer du bon côté ✔ décider d'une révocation de certificat selon le contexte ✔ mesurer le risque transféré par une réattribution d'adresse

**Dossier fourni**

*Pièce 1 — compte rendu de l'équipe*
> « Le serveur `SRV-APP-07` a été éteint le 12 mars. L'application a été migrée vers `SRV-APP-12` le 5 mars, les utilisateurs ont été informés, et les données ont été reprises. La machine virtuelle a été supprimée de l'hyperviseur le 20 mars. Le ticket est clos. »

*Pièce 2 — extrait de l'inventaire, `SRV-APP-07`*
```
mis_en_service      : 2016-09-14
statut_cycle_vie    : décommissionné
environnement       : production
certificats         : 2 (expiration 2029-04-30, 2028-11-12)
comptes_service     : svc-app07-batch, svc-app07-sql
cles_ssh_autorisees : 3 (dont 1 utilisée pour administrer SRV-BDD-01 et SRV-BDD-02)
sauvegardes         : politique 7 ans, dernière le 2027-03-11
```

*Pièce 3 — extrait DNS, 10 avril*
```
srv-app-07.interne.exemple      A      10.42.7.18
app-crm.interne.exemple         CNAME  srv-app-07.interne.exemple
crm-legacy.interne.exemple      CNAME  srv-app-07.interne.exemple
```

*Pièce 4 — règles de filtrage, extrait*
```
ALLOW  10.42.7.18 -> 10.42.9.0/24  tcp/1433   "SRV-APP-07 vers bases"
ALLOW  10.20.0.0/16 -> 10.42.7.18  tcp/443    "accès utilisateurs CRM"
```

*Pièce 5 — supervision*
```
srv-app-07 : 412 alertes "hôte injoignable" depuis le 12 mars — notification désactivée le 3 avril
```

**Questions**
(a) Identifiez les oublis et l'action manquante pour chacun.
(b) Lequel présente le risque le plus élevé, et pourquoi ?
(c) L'adresse `10.42.7.18` a été réattribuée le 2 avril à un poste de test. Quelles conséquences ?
(d) Faut-il révoquer les deux certificats ?
(e) Que manque-t-il au compte rendu, indépendamment de toute action technique ?

---

**Corrigé commenté**

**(a) Les neuf oublis**

| # | Oubli | Preuve dans le dossier | Action manquante |
|---|---|---|---|
| 1 | **Enregistrements de noms** | Pièce 3 : 1 entrée A + 2 alias actifs le 10 avril | Suppression des trois entrées |
| 2 | **Comptes de service** | Pièce 2 : 2 comptes | Vérifier leur usage ailleurs (§24.11), puis supprimer |
| 3 | **Clés SSH** | Pièce 2 : 1 clé administre `SRV-BDD-01` et `-02` | Retirer la clé **sur les deux bases** — l'accès subsiste dans l'autre sens |
| 4 | **Règles de filtrage** | Pièce 4 : 2 règles actives | Suppression, pas désactivation |
| 5 | **Certificats** | Pièce 2 : 2, dont un jusqu'en 2029 | Voir (d) |
| 6 | **Retrait des outils** | Pièce 5 : notification désactivée, sonde conservée | Retrait de la supervision, du scanner, de la sauvegarde, de la protection des postes |
| 7 | **Sauvegardes** | Pièce 2 : rétention 7 ans, aucune décision | Décision documentée, date de suppression, propriétaire |
| 8 | **Effacement et preuve** | Absent | Attestation d'effacement, **y compris instantanés et copies en recette** |
| 9 | **Vérification finale** | Absente | Contrôles du §35.11 après délai d'observation |

**(b) Le risque le plus élevé : la clé SSH (oubli n° 3)**

Les autres oublis laissent des traces exploitables ; celui-ci laisse un **accès actif vers deux serveurs de bases de données toujours en service**. La suppression de `SRV-APP-07` n'y change rien : la clé est déclarée du côté des bases, pas du côté du serveur retiré. C'est le mécanisme du §35.6 — la révocation se fait **là où l'accès est reconnu**, pas là où il était utilisé.

Le compte de service `svc-app07-sql` présente le même défaut, avec la même cause.

**(c) La réattribution d'adresse — deux conséquences**

1. **Confusion d'inventaire.** Le poste de test hérite d'une adresse portant trois entrées DNS pointant vers un serveur applicatif de production. Tout outil raisonnant sur l'adresse ou le nom l'identifiera comme `SRV-APP-07` (§15.11, faux positif n° 8).
2. **Exposition réelle.** La règle `ALLOW 10.20.0.0/16 -> 10.42.7.18 tcp/443` autorise désormais **l'ensemble du réseau bureautique** à joindre un poste de test sur le port 443. Ce n'était pas l'intention, et personne ne l'a décidé.

C'est l'illustration la plus concrète de ce que produit un décommissionnement incomplet : le risque n'est pas resté sur l'actif retiré, il a été **transféré** à un autre actif.

**(d) Les certificats — la réponse n'est pas automatique**

| Cas | Décision |
|---|---|
| Clé privée détruite avec la machine, aucune copie | Révocation **non nécessaire** : documenter la destruction de la clé et le retrait du service |
| Clé privée présente dans une sauvegarde, un instantané ou un coffre | **Révocation nécessaire** |
| Clé privée exportée à un moment quelconque, sans certitude | **Révocation** — le doute impose la prudence |
| Certificat déclaré dans un magasin de confiance tiers | Retrait de la déclaration, en plus de la révocation |

Ici, la pièce 2 indique une sauvegarde du 11/03/2027 avec rétention 7 ans : la clé privée est **probablement restaurable**. Décision retenue : révocation des deux certificats, et rattachement de la question au traitement des sauvegardes (oubli n° 7).

**(e) Ce qui manque au compte rendu, et qui n'est pas technique**

Aucun propriétaire nommé, aucune signature, aucune vérification. **Personne ne répond de ce décommissionnement.** Dans dix-huit mois, quand la clé SSH sera découverte lors d'un audit, aucun nom ne sera associé à la décision — et c'est exactement ce qui s'est produit dans le fil rouge du §35.14.

Le PV D.14 corrige cela par construction : quinze lignes de contrôle, une preuve par ligne, et **deux signatures**.

**Les deux erreurs attendues**
1. Considérer que la suppression de la machine virtuelle achève le processus. Elle supprime le système, pas ce qui gravite autour — et c'est ce qui gravite autour qui constitue le risque résiduel.
2. Traiter la révocation des certificats comme un réflexe automatique, sans se demander où se trouve la clé privée.

#### 35.14 🔴 FIL ROUGE — août 2028 : les résidus de décembre 2026

Claire Nadeau fait vérifier les neuf serveurs décommissionnés en décembre 2026 (§1.9 et suivants), vingt mois plus tard, dans le cadre de la préparation du dossier de preuves.

**Le résultat.**

| Contrôle | Résultat |
|---|---|
| Machines supprimées de l'hyperviseur | 9 sur 9 |
| Enregistrements de noms supprimés | **6 sur 9** — 3 entrées subsistent |
| Comptes de service supprimés | **8 sur 9** — 1 compte actif, avec droits de lecture sur le serveur de fichiers |
| Règles de filtrage supprimées | 7 sur 9 |
| Certificats révoqués | **4 sur 9** — 5 certificats valides, dont 2 expirant en 2029 |
| Sauvegardes traitées | **0 sur 9** — aucune décision prise, sauvegardes conservées par défaut |
| Preuve d'effacement | Aucune |
| Procès-verbal signé | Aucun |

**Le compte de service survivant** est celui qui préoccupe le plus. Créé en 2017, il dispose de droits de lecture sur le serveur de fichiers, son mot de passe n'a jamais été modifié, et il n'apparaît dans aucun inventaire d'application — puisque l'application n'existe plus. Il figurait pourtant parmi les 94 comptes sans propriétaire identifiés en septembre 2027 (§24.11), et il avait alors été classé « à investiguer ».

**Ce que l'épisode démontre**, et c'est pourquoi il clôt cette partie : le décommissionnement de décembre 2026 avait été considéré comme fait. Il l'était à 70 %. Les 30 % restants ont produit, vingt mois plus tard, un compte privilégié orphelin, cinq certificats valides sans porteur, trois entrées de résolution de noms, et un volume de sauvegardes conservé sans décision.

**Les trois mesures.**

1. Le **procès-verbal de décommissionnement** (§35.12) devient obligatoire, avec double signature. Un décommissionnement sans procès-verbal n'est pas clos.
2. Une **vérification à J+90** est ajoutée systématiquement, avec les contrôles du §35.11.
3. Les neuf décommissionnements de 2026 et les quatre de 2027 sont **repris intégralement** — six jours de travail.

**Ce que Claire écrit au comité.** *Nous avons construit un dispositif capable de détecter une vulnérabilité sur un serveur en vingt-quatre heures. Il nous a fallu vingt mois pour découvrir qu'un compte privilégié survivait à un serveur que nous avions nous-mêmes éteint.*

→ La suite en 🔴 §36.8, sur ce qui peut réellement être automatisé.

→ **Chapitre 36 — Automatisation, orchestration et limites** : automatiser dans le bon ordre, et savoir où s'arrêter.

#### Synthèse mentale du chapitre 35

Un système remplacé mais non retiré cumule tous les défauts : plus maintenu, toujours joignable, comptes et secrets intacts — c'est l'actif idéal pour un attaquant. Le décommissionnement est donc un acte de MCS à part entière. Il commence par la mesure de l'usage réel et par une extinction avant suppression, seule méthode fiable pour révéler les dépendances non documentées, notamment annuelles. La section la plus oubliée est celle des révocations, et le point critique y est la révocation **côté fournisseur** : supprimer une clé d'un fichier de configuration ne l'invalide pas. Un décommissionnement se vérifie après un délai d'observation, il ne se déclare pas, et il se clôt par un procès-verbal signé — faute de quoi personne ne répond des résidus découverts deux ans plus tard.

**Trois questions de vérification**

1. Une machine virtuelle a été supprimée de l'hyperviseur. Citez six objets qui peuvent lui survivre, et lequel présente le risque le plus élevé.
2. Pourquoi une analyse de flux de trois semaines est-elle insuffisante pour décider du retrait d'un système ancien ?
3. Que signifie exactement « révoquer » une clé d'API, et en quoi cela diffère-t-il de la supprimer de la configuration ?

---

### Chapitre 36 — Automatisation, orchestration et limites

#### 36.1 Que faut-il automatiser en premier

L'ordre importe, et l'intuition conduit généralement au mauvais.

| Rang | Objet | Pourquoi cet ordre |
|---|---|---|
| **1** | **La collecte** — inventaire, versions, états | Sans donnée fiable, tout le reste est faux (§10.1) |
| **2** | **La corrélation** — rapprocher avis et inventaire | Supprime le travail manuel le plus ingrat, sans risque |
| **3** | **La vérification** — contrôler que l'état a changé | Automatiser la preuve libère du temps et améliore l'audit |
| **4** | **Le déploiement** — appliquer les correctifs | Efficace, mais requiert anneaux et critères d'arrêt |
| **5** | **La décision** — prioriser automatiquement | En dernier, et jamais totalement |

**Pourquoi la décision arrive en dernier.** La priorisation dépend de l'exposition et de la criticité métier (§16.2), c'est-à-dire d'informations contextuelles que l'automatisme n'établit pas seul. Un arbre de décision peut être outillé — il l'est utilement — mais ses entrées doivent être fiables, ce qui suppose que les rangs 1 et 2 soient déjà solides.

⚠️ **L'erreur de séquencement la plus fréquente** consiste à automatiser le déploiement en premier, parce que c'est le plus visible. On obtient alors un mécanisme efficace appliqué à un périmètre inconnu — les tableaux de bord verts du §1.4.

#### 36.2 Automatiser la remédiation

| Élément | Exigence |
|---|---|
| **Condition de déclenchement** | Écrite, précise, testée : quel type de constat, sur quelle classe d'actif |
| **Périmètre** | Explicitement borné, avec liste d'exclusions |
| **Déploiement témoin** | Obligatoire, même en automatique |
| **Critères d'arrêt** | Chiffrés, évalués automatiquement (§18.4) |
| **Journal** | Chaque action automatique tracée comme une action humaine |
| **Interruption manuelle** | Un moyen d'arrêter immédiatement, connu de l'astreinte |

**Le principe directeur** : l'automatisation ne doit pas retirer de garde-fou. Elle exécute plus vite ce qu'un humain ferait, avec les mêmes protections — anneaux, critères d'arrêt, retour arrière, preuve.

#### 36.3 Auto-remédiation : où c'est raisonnable, où c'est dangereux

| Périmètre | Automatisation | Raison |
|---|---|---|
| Postes de travail, correctifs courants | **Raisonnable** | Volume élevé, impact unitaire faible, retour arrière par redéploiement |
| Images et modèles | **Raisonnable** | Corrige la source, effet démultiplié (§28.5) |
| Serveurs C3 non critiques | Raisonnable avec anneaux | Impact limité |
| Serveurs C1 et actifs de niveau 0 | **Déconseillé** | Un incident affecte tout le reste |
| Bases de données | **Déconseillé** | Point de non-retour (§6.7) |
| Équipements réseau | **Déconseillé** | Une erreur coupe l'accès au moyen de la corriger |
| Systèmes industriels | **Proscrit** | Validation constructeur obligatoire (ch. 29) |

**Le critère unique qui résume ce tableau** : automatisez là où **le retour arrière est simple et testé**. Partout ailleurs, l'automatisation transfère un risque humain vers un risque systémique.

#### 36.4 La chaîne outillée type

```
Inventaire (source d'autorité, §17.11)
   ↓ enrichi de criticité, exposition, propriétaires
Veille automatisée (§14.6)
   ↓ corrélation, archivage de ce qui est écarté
Constats candidats
   ↓ arbre de décision outillé (§16.3)
Tickets et campagnes (§17.6)
   ↓ affectation automatique par propriétaire d'actif
Déploiement (§18.4)
   ↓ anneaux, critères d'arrêt automatiques
Vérification (§18.9)
   ↓ contrôle de l'état constaté
Preuve archivée (§2.9)
   ↓
Indicateurs (ch. 38)
```

**Les deux points de rupture** les plus fréquents dans cette chaîne : entre l'inventaire et les outils, faute d'identifiant pivot commun (§15.7) ; et entre le déploiement et la vérification, quand la clôture se fait sur déclaration plutôt que sur preuve (§17.8).

#### 36.5 L'assistance par intelligence artificielle

**Les usages réellement utiles aujourd'hui**, dans le périmètre de ce cours :

| Usage | Valeur | Précaution |
|---|---|---|
| Résumer un avis technique long | Gain de temps réel | Vérifier les versions affectées à la source |
| Reformuler un constat technique en termes métier | Utile pour les dérogations (§20.10) | Relecture obligatoire |
| Aider à rédiger une règle de détection ou un script | Accélération | Tester avant déploiement |
| Explorer un jeu de données de constats | Aide à l'analyse | Ne pas fonder une décision sur la seule sortie |
| Préparer une communication de crise | Gain de temps sous pression | Validation par le pilote |

**Le risque spécifique** : une sortie plausible mais fausse est plus dangereuse qu'une absence de réponse, parce qu'elle ne déclenche aucune vérification. Une version affectée inexacte, un identifiant inventé, une conclusion sur l'exploitabilité non fondée peuvent orienter une décision entière.

✅ **BONNE PRATIQUE (P0)** — Toute information issue d'une assistance automatisée et destinée à fonder une décision engageante doit être **vérifiée à la source**, et le statut du §14.7 s'applique : ce qui n'est pas vérifié reste une hypothèse.

#### 36.6 ⏱ Tendance : volumétrie et vitesse

*Bloc daté, vérifié le 30/07/2026.*

La découverte de vulnérabilités s'accélère, notamment sous l'effet de méthodes de recherche assistées. Trois conséquences pour le dimensionnement des processus, sans dramatisation :

1. **La pression porte sur la vitesse de remédiation**, pas sur la qualité du triage. Une organisation capable de décider vite mais lente à déployer sera limitée par le déploiement.
2. **Le regroupement devient plus rentable que le traitement unitaire** (§16.7) : la montée de version et la reconstruction d'image absorbent le volume, le traitement constat par constat ne le peut pas.
3. **L'exposition redevient le levier principal** : réduire la surface protège indépendamment du volume de vulnérabilités publiées (§11.8).

**Ce qui ne change pas** : l'inventaire, la propriété, les fenêtres, la preuve et le financement. Une organisation qui n'a pas ces cinq bases ne sera pas sauvée par l'automatisation — elle produira simplement plus vite des chiffres faux.

#### 36.7 ⚠️ Le risque systémique de l'automatisation

Une mise à jour défectueuse, déployée manuellement, touche quelques machines avant qu'on ne l'arrête. Déployée automatiquement sans garde-fou, elle touche l'ensemble du parc en quelques minutes.

**Les quatre garde-fous non négociables** :

| Garde-fou | Rôle |
|---|---|
| **Déploiement progressif** | Un incident touche un anneau, pas le parc |
| **Critères d'arrêt automatiques** | La campagne s'interrompt sans attendre une décision humaine |
| **Retour arrière testé** | Chronométré, connu de l'astreinte (§18.8) |
| **Interruption manuelle** | Un moyen d'arrêter immédiatement, documenté et connu |

**La règle qui les résume** : *plus le déploiement est rapide, plus les garde-fous doivent être stricts.* L'automatisation sans anneaux n'est pas une accélération, c'est une amplification.

#### 36.8 📌 Limites de l'automatisation

- **La dette d'outillage** : chaque automatisme est un actif à maintenir — scripts, connecteurs, règles. Une chaîne outillée non maintenue casse silencieusement.
- **La fragilité des connecteurs** : un changement d'interface côté fournisseur interrompt une intégration, souvent sans alerte.
- **L'effet « tableau de bord vert »** : un automatisme qui échoue silencieusement produit une absence de signal interprétée comme une absence de problème (§15.8).
- **L'automatisation ne crée pas de capacité de décision** : les arbitrages métier, les fenêtres et les dérogations restent humains.
- **Le coût d'intégration** est souvent supérieur au coût de la licence.

✅ **BONNE PRATIQUE (P1)** — Surveillez vos automatismes eux-mêmes : date de dernière exécution réussie, taux d'échec, volume traité. Un automatisme qui ne s'exécute plus est plus dangereux qu'un processus manuel qu'on sait manuel.

→ **Chapitre 37 — Économie du MCS, charge de travail et facteur humain** : financer le dispositif et le rendre soutenable.

#### Synthèse mentale du chapitre 36

L'ordre d'automatisation compte, et l'intuition conduit au mauvais : collecte, corrélation, vérification, déploiement, décision — automatiser le déploiement en premier produit un mécanisme efficace appliqué à un périmètre inconnu. L'automatisation ne doit retirer aucun garde-fou : elle exécute plus vite ce qu'un humain ferait, avec les mêmes anneaux, critères d'arrêt et preuves. Le critère qui décide où automatiser est unique : là où le retour arrière est simple et testé. L'assistance automatisée est utile pour résumer, reformuler et explorer, mais une sortie plausible et fausse est plus dangereuse qu'une absence de réponse, car elle ne déclenche aucune vérification. Face à l'accélération de la volumétrie, le regroupement et la réduction d'exposition sont les seuls leviers qui passent à l'échelle. Enfin, un automatisme qui échoue silencieusement transforme une absence de signal en fausse assurance : surveillez vos automatismes comme vous surveillez vos actifs.

**Trois questions de vérification**

1. Votre direction veut automatiser le déploiement des correctifs avant tout le reste. Quel est le problème, et par quoi proposez-vous de commencer ?
2. Sur quel critère unique décidez-vous qu'un périmètre peut recevoir de l'auto-remédiation ?
3. Pourquoi une chaîne d'automatisation non surveillée est-elle plus dangereuse qu'un processus manuel équivalent ?

---

### Chapitre 37 — Économie du MCS, charge de travail et facteur humain

#### 37.1 Chiffrer le MCS

Un programme non chiffré n'est pas arbitrable, et un programme non arbitré est financé par défaut — c'est-à-dire mal.

**Les six postes de coût**, dont trois sont presque toujours omis :

| Poste | Contenu | Souvent omis ? |
|---|---|---|
| Personnel | ETP consacrés à la veille, au triage, au déploiement, à la preuve | Non |
| Licences et outillage | Scan, déploiement, gestion, journalisation | Non |
| **Coût d'interruption** | Production perdue pendant les fenêtres | **Oui** |
| **Coût de test** | Environnements, jeux de données, temps métier de validation | **Oui** |
| Dette d'obsolescence | Support étendu, migrations à venir | Parfois |
| **Coût des compensations** | Charge récurrente des mesures compensatoires (§20.7, attribut 5) | **Oui** |

**Les trois postes omis sont ceux qui rendent visible le coût de ne pas faire.** Ils apparaissent ailleurs dans les budgets — production, projets, exploitation — et jamais dans la ligne « sécurité », ce qui fausse tous les arbitrages.

#### 37.2 Construire un dossier d'investissement

**La structure qui fonctionne**, en quatre parties :

| Partie | Contenu |
|---|---|
| **1. Situation** | Où nous en sommes, avec les indicateurs de résultat et leur tendance |
| **2. Point de bascule** | À quelle date, sans décision, la situation se dégrade mécaniquement |
| **3. Trois options chiffrées** | Sur la durée complète, jamais sur la première année |
| **4. Recommandation** | Une option, avec son risque résiduel assumé |

**Les trois options doivent toujours inclure le statu quo**, chiffré (§12.5). Une direction n'arbitre pas ce qu'elle ne peut pas comparer, et l'absence de troisième option est la première cause de non-décision.

**Le calcul du coût de ne rien faire** comprend : le coût des compensations maintenues, le surcoût des interventions en urgence, le coût du support étendu, la charge d'astreinte, l'écart de prime d'assurance, et le risque résiduel exprimé en termes métier — jours d'arrêt possibles, données concernées, conséquences contractuelles.

#### 37.3 L'assurance cyber

Pour de nombreuses organisations, les questionnaires d'assurance constituent l'un des leviers les plus efficaces pour obtenir un arbitrage sur le MCS (§7.5) — souvent devant l'argument du risque.

**Ce qu'ils exigent typiquement**, et ce que ce cours vous permet de démontrer :

| Exigence du questionnaire | Chapitre correspondant |
|---|---|
| Processus documenté de gestion des correctifs | 7 |
| Délais de correction par criticité, et leur respect mesuré | 7, 38 |
| Inventaire des actifs | 10 |
| Part du parc hors support | 12 |
| Authentification multifacteur sur les accès distants | 24 |
| Sauvegardes testées et immuables | 34 |
| Gestion des accès à privilèges | 24 |
| Délai de détection et de réaction | 21 |

⚠️ **PIÈGE — la déclaration inexacte**
Répondre par l'affirmative à une exigence non tenue peut, en cas de sinistre, fonder un refus de garantie. La réponse honnête assortie d'un plan daté est préférable à une réponse flatteuse — et, en pratique, mieux reçue par les assureurs qu'on ne le croit.

#### 37.4 Dimensionner l'équipe

**La méthode par la capacité**, seule fiable, en quatre étapes (§16.5) :

```
1. Mesurer le volume mensuel réel par catégorie de traitement
2. Mesurer le temps réel par unité — pas le temps théorique
3. Calculer la charge, en incluant la preuve et le suivi
4. Confronter à la capacité disponible, en déduisant l'incompressible
```

**Les quatre postes de charge incompressible**, systématiquement sous-estimés : les réunions et le reporting, les urgences non planifiées, la relance des propriétaires, et le traitement de la traîne longue (§18.10).

**Les seuils de rupture à connaître** :

| Signal | Ce qu'il indique |
|---|---|
| Le *backlog* grossit malgré une activité constante | Capacité structurellement insuffisante (§17.10) |
| La part de changements d'urgence dépasse 15-20 % | Le processus normal ne fonctionne pas (§5.1) |
| Les vérifications post-déploiement sont abandonnées | Premier symptôme de surcharge — et le plus coûteux |
| La preuve n'est plus produite | Second symptôme : le pilotage devient impossible |

**Cet ordre s'observe fréquemment** : sous pression, une équipe abandonne souvent d'abord la vérification, puis la preuve, puis la qualification. Elle continue à déployer — l'activité visible — tout en perdant la capacité de démontrer quoi que ce soit. C'est le signal à surveiller.

#### 37.5 Astreintes, nuits et week-ends

Le MCS consomme du temps hors horaires : fenêtres nocturnes, interventions de week-end, astreintes de crise.

| Point | Traitement |
|---|---|
| **Prévisibilité** | Fenêtres récurrentes plutôt qu'interventions négociées (§5.2) |
| **Rotation** | Jamais les mêmes personnes ; une astreinte concentrée sur deux personnes est une dépendance critique |
| **Compensation** | Récupération effective, pas théorique |
| **Réduction du besoin** | Redondance, correction à chaud, déploiement progressif (ch. 6) — c'est l'argument économique du §6.13 |

**Le point rarement fait explicitement** : investir dans l'architecture réduit le travail de nuit. C'est un argument qui parle aux équipes et à la direction des ressources humaines autant qu'à la direction financière.

#### 37.6 La fatigue de la vulnérabilité

**Le mécanisme.** Une file qui ne se vide jamais, des constats en volume ininterrompu, et l'impression que l'effort ne produit aucun résultat visible. C'est une cause de démotivation documentée, et elle est **structurelle**, pas individuelle.

| Cause structurelle | Remède |
|---|---|
| File infinie | Priorisation qui **exclut** explicitement (§16.3), et campagnes plutôt que constats (§16.7) |
| Absence de résultat visible | Indicateurs de résultat, tendance sur plusieurs trimestres (§38.1) |
| Travail invisible des autres | Communication interne sur ce qui a été évité |
| Responsabilité sans autorité | Le RACI du §9.2 |
| Constats non traités qui s'accumulent | Qualification systématique : dérogation ou dépriorisation, jamais l'oubli (§17.10) |

**Le remède le plus efficace, et le moins coûteux** : mesurer et montrer les **actifs ramenés à un état de référence** plutôt que les vulnérabilités fermées (§16.7). La première mesure progresse et se voit ; la seconde donne l'impression de vider la mer.

#### 37.7 Compétences et transmission

| Risque | Traitement |
|---|---|
| Dépendance à une personne clé | Suppléance nommée sur chaque rôle (§14.8) |
| Savoir non documenté | Procédures d'exploitation à jour, testées par une autre personne |
| Perte au départ | Passation formalisée, avec période de recouvrement |
| Outils maîtrisés par une seule personne | Formation croisée, documentation d'administration |

**Le test qui révèle la dépendance** : une personne est absente trois semaines. Que devient le processus ? Si la réponse est « il s'arrête », vous avez une dépendance critique, pas une équipe.

#### 37.8 Communiquer vers les métiers

| Situation | Ce qui fonctionne |
|---|---|
| Annoncer une interruption | Préavis, créneau, durée, ce qui se passe si on ne le fait pas |
| Gérer un refus | Qualifier le motif (§20.1), proposer une alternative, formaliser si le refus persiste |
| Après un incident évité | Le dire — c'est la seule occasion où le travail devient visible |
| Demander un budget | Termes métier, options chiffrées, jamais le vocabulaire technique |

🏢 **VU EN RÉUNION** — Présentation d'un plan de sortie d'obsolescence au comité de direction. Le RSSI ouvre sur le nombre de vulnérabilités critiques. Au bout de quatre minutes, le directeur financier interrompt : « combien ça coûte, et qu'est-ce qui se passe si on ne le fait pas ? ». Ces deux questions figuraient en diapositive onze. Depuis, elles sont en diapositive deux.

⚠️ **PIÈGE — la communication par la peur**
Elle fonctionne une fois. À la deuxième, elle produit de la lassitude ; à la troisième, du discrédit. La communication qui tient dans la durée est factuelle, chiffrée, et propose des options.

#### 37.9 🔴 FIL ROUGE — septembre 2028 : 62 heures par mois

Lors de l'entretien annuel, Malik Ferhaoui expose à Sonia Weber une mesure qu'il tient depuis six mois : **62 heures par mois** consacrées au MCS, sur un temps de travail théorique de 151 heures. Soit 41 % de son temps, pour une mission qui n'est pas dans sa fiche de poste.

**La décomposition qu'il présente.**

| Activité | Heures/mois |
|---|---|
| Qualification et triage des constats | 12 |
| Planification et coordination des campagnes | 14 |
| Exécution — dont 9 h hors horaires ouvrés | 18 |
| Vérification et production de preuve | 8 |
| Relance des propriétaires d'actifs | **7** |
| Comité, reporting, documentation | 3 |

**La ligne qui déclenche la discussion** est la cinquième : sept heures par mois passées à relancer des personnes qui ne répondent pas. Ce n'est pas du travail technique, c'est le symptôme d'un défaut de gouvernance — les propriétaires sont nommés (§5.5), mais l'affectation d'un ticket ne les engage à rien tant qu'aucun délai de contestation ni aucune escalade automatique n'existe (§17.4).

**Les quatre décisions, et leur effet mesuré trois mois plus tard.**

| Décision | Effet |
|---|---|
| Escalade automatique à J+5 sans réponse du propriétaire, vers son responsable | Relances : 7 h → **1 h** |
| Regroupement des campagnes de C3 en une seule fenêtre mensuelle | Planification : 14 h → 9 h |
| Automatisation de la vérification et de l'export de preuve (§36.1, rang 3) | Vérification : 8 h → 3 h |
| Recrutement d'un alternant en apprentissage sur le suivi et la preuve | Capacité ajoutée, et suppléance créée |

Total après trois mois : **62 h → 37 h**. Aucune de ces mesures n'a réduit le périmètre ni le niveau d'exigence.

**Ce que Sonia Weber retient**, et qu'elle porte au comité stratégique : le poste de charge le plus lourd n'était ni la technique ni le volume, c'était **l'absence de mécanisme d'engagement**. Sept heures mensuelles de relance représentaient, sur deux ans, l'équivalent de plus de vingt jours de travail consacrés à demander à des gens de répondre.

**Le point que Claire Nadeau ajoute.** Les 9 heures mensuelles hors horaires ouvrés ne diminuent pas : elles tiennent aux systèmes non interruptibles. Elles constituent la ligne d'argumentation du dossier d'investissement en redondance présenté au budget 2029 — l'application directe du §6.13, appuyée cette fois sur une mesure et non sur un principe.

**Livrable de l'épisode.** La mesure de charge par activité, reconduite trimestriellement, et l'escalade automatique intégrée au workflow de remédiation (Annexe J).

→ La suite en 🔴 §38.9, quand le directeur financier posera une question sur les indicateurs.

→ **Chapitre 38 — Indicateurs, tableaux de bord et maturité** : mesurer sans produire de chiffres faux.

#### Synthèse mentale du chapitre 37

Trois postes de coût du MCS sont presque toujours omis — interruption, test, compensations — et ce sont précisément ceux qui rendent visible le coût de ne rien faire, parce qu'ils apparaissent dans d'autres budgets. Un dossier d'investissement présente toujours trois options chiffrées sur la durée complète, dont le statu quo : son absence est la première cause de non-décision. Les questionnaires d'assurance sont devenus le premier levier réel du MCS, et une réponse honnête assortie d'un plan daté vaut mieux qu'une réponse flatteuse qui peut fonder un refus de garantie. Sous surcharge, une équipe abandonne dans un ordre constant : d'abord la vérification, puis la preuve, puis la qualification — elle continue à déployer tout en perdant la capacité de démontrer quoi que ce soit. La fatigue de la vulnérabilité est structurelle, et son remède le moins coûteux consiste à mesurer les actifs ramenés à un état de référence plutôt que les vulnérabilités fermées. Enfin, le poste de charge le plus lourd est souvent l'absence de mécanisme d'engagement : la relance manuelle se remplace par une escalade automatique.

**Trois questions de vérification**

1. Votre direction estime que le MCS coûte cher. Quels trois postes de coût lui manquent probablement, et où apparaissent-ils actuellement ?
2. Votre équipe déploie toujours autant de correctifs mais ne produit plus de preuve. Que se passe-t-il, et quel symptôme l'a précédé ?
3. Une personne passe sept heures par mois à relancer des propriétaires d'actifs. Est-ce un problème de charge ou de gouvernance, et que corrigez-vous ?

---

### Chapitre 38 — Indicateurs, tableaux de bord et maturité

#### 38.1 Ce qu'un indicateur doit permettre de décider

Un indicateur qui ne change aucune décision n'a pas d'utilité, quel que soit son intérêt apparent. Trois questions à poser avant d'en créer un :

1. **Quelle décision** cet indicateur permet-il de prendre, et par qui ?
2. **Quel seuil** déclenche une action ?
3. **Que fait-on** exactement quand ce seuil est franchi ?

Sans réponse aux trois, l'indicateur est décoratif — et il consommera du temps de production chaque mois.

#### 38.2 Le dictionnaire d'indicateurs

C'est le livrable central du chapitre. **Chaque indicateur doit être défini par huit attributs**, faute de quoi deux personnes calculeront deux valeurs différentes.

| Attribut | Rôle |
|---|---|
| Formule | Le calcul exact |
| Numérateur | Ce qui est compté |
| **Dénominateur** | Sur quoi c'est rapporté — l'attribut le plus important |
| Périmètre | Quels actifs, quelles classes |
| Période | Sur quel intervalle |
| **Exclusions** | Ce qui est retiré, et pourquoi |
| Source | D'où viennent les données |
| Propriétaire | Qui le produit et en répond |

**Les dix indicateurs de référence** — la fiche complète de chacun figure en **Annexe K** :

| # | Indicateur | Formule | Ce qu'il mesure |
|---|---|---|---|
| 1 | **Couverture d'inventaire** | actifs identifiés / actifs estimés du périmètre | La fiabilité de tout le reste |
| 2 | **Couverture de scan** | actifs scannés avec succès / périmètre de référence | Ce que l'on voit réellement |
| 3 | **Conformité de correctifs** | actifs conformes / actifs éligibles | L'état du parc |
| 4 | **Respect des délais** | constats clos dans le délai / constats arrivés à échéance | La tenue des engagements |
| 5 | **Âge moyen du *backlog*** | moyenne des durées depuis la première détection | La vitesse réelle |
| 6 | **Dette critique échue** | constats critiques dont le délai est dépassé | Le retard qui compte |
| 7 | **Âge des dérogations** | ancienneté moyenne des dérogations ouvertes | La dette formellement acceptée |
| 8 | **Taux de récurrence** | constats réapparus / constats clos | Un problème de source (§17.9) |
| 9 | **Taux de retour arrière** | déploiements annulés / déploiements réalisés | La qualité de la validation |
| 10 | **Taux d'échec de déploiement** | actifs en échec / actifs ciblés | La santé de la chaîne |

**Les indicateurs 1 et 2 conditionnent tous les autres**, et leur combinaison appelle une précaution de vocabulaire.

Le produit *conformité × couverture* — 95 % × 60 % = 57 % — est le **ratio conservateur d'actifs confirmés conformes sur le périmètre**. Il suppose implicitement que **tout actif non mesuré est non conforme**. C'est une hypothèse de prudence, pas une mesure : il ne décrit pas la conformité réelle, qui reste **inconnue** sur les 40 % non mesurés.

✅ **Publier quatre valeurs, jamais une seule** :

| Valeur | Exemple |
|---|---|
| Couverture | 60 % |
| Conformité **dans la population mesurée** | 95 % |
| **Ratio confirmé conforme sur périmètre** | 57 % |
| **Non mesuré** | 40 % |

La dernière ligne est celle qui appelle une décision. Les trois premières décrivent ce que vous savez ; la quatrième décrit ce que vous ignorez.

#### 38.3 Les pièges de calcul

| Piège | Mécanisme | Contre-mesure |
|---|---|---|
| **Dénominateur mouvant** | Le périmètre change d'un mois à l'autre, la tendance devient illisible | Périmètre de référence figé, avec ses variations documentées |
| **Exclusions non déclarées** | Les actifs difficiles sortent silencieusement (§15.6) | Liste d'exclusions publiée avec l'indicateur |
| **Agrégation trompeuse** | Un taux global masque une population entière | Publication par population (§10.11) |
| **Moyenne qui masque la traîne** | L'âge moyen cache les constats très anciens | Publier aussi la médiane et le maximum |
| **Indicateur récompensant l'inaction** | Le nombre de vulnérabilités détectées baisse si l'on scanne moins | Toujours associer volume et couverture |
| **Remise à zéro d'historique** | Un actif recréé perd son ancienneté (§15.7) | Identifiant pivot stable |

#### 38.4 ⚠️ La discontinuité de modèle comme piège de reporting

Un cas particulier qui mérite d'être isolé, car il produit des conclusions entièrement fausses.

Les modèles de score externes évoluent par versions, et **un changement de version déplace tous les scores simultanément** (§4.5). Conséquence : un indicateur fondé sur un seuil de score peut varier fortement sans qu'aucun correctif n'ait été appliqué et sans qu'aucune vulnérabilité n'ait changé.

**La règle** : toute série temporelle traversant un changement de modèle doit être **marquée comme discontinue** sur le graphique, et l'interprétation doit le mentionner. Avant de célébrer une amélioration soudaine, vérifiez d'abord ce qui a changé dans les données d'entrée.

#### 38.5 Concevoir un tableau de bord par audience

| Audience | Nombre d'indicateurs | Contenu | Fréquence |
|---|---|---|---|
| **Exploitation** | 8 à 12 | Opérationnels : échecs, traîne, campagnes en cours, échéances proches | Hebdomadaire |
| **Comité MCS** | 5 à 8 | Résultat : conformité par population, respect des délais, dérogations, dette | Mensuelle |
| **Direction générale** | **3 à 5** | Risque : dette critique, actifs hors support, tendance sur 4 à 8 trimestres | Trimestrielle |
| **Auditeur** | Le dossier de preuves | Définitions, périmètres, exclusions, historique (ch. 39) | À la demande |

**La règle de la direction générale** : trois à cinq indicateurs, une tendance, et une décision demandée. Un comité de direction ne réagit pas à un niveau, il réagit à une **pente** — et il ne peut arbitrer que ce qui lui est présenté sous forme d'options (§12.6).

#### 38.6 Le modèle de maturité

Un modèle de maturité sert à situer une organisation et à définir la prochaine étape. Il devient cosmétique dès qu'il sert à s'auto-évaluer favorablement.

| Niveau | Nom | Caractéristique |
|---|---|---|
| **0** | Inexistant | Aucun processus ; les correctifs s'appliquent au gré des incidents |
| **1** | Réactif | On corrige quand un problème survient ; pas d'inventaire fiable |
| **2** | Documenté | Politique écrite, inventaire constitué, propriétaires nommés |
| **3** | Piloté | Délais définis et mesurés, dérogations tracées, indicateurs suivis |
| **4** | Industrialisé | Automatisation, campagnes, preuve produite systématiquement |
| **5** | Adaptatif et fondé sur le risque | Priorisation par exposition et exploitation, boucle d'amélioration, MCS *by design* |

**L'usage utile** : identifier le niveau atteint **par domaine** — inventaire, veille, remédiation, configuration, identités, preuve — et non globalement. Une organisation est rarement au même niveau partout, et un domaine critique faible **plafonne** la maturité de tout ce qui en dépend. La grille par domaine figure en Annexe K.

#### 38.7 Historisation et conservation

Sans historique, aucun progrès n'est démontrable — et la démonstration de progrès est ce qui pérennise un budget (§7.5).

| Exigence | Contenu |
|---|---|
| Conservation | Valeurs mensuelles conservées plusieurs années, indépendamment des outils |
| **Indépendance des outils** | Export périodique en format ouvert (§15.12) |
| Traçabilité des définitions | Un changement de formule est daté et documenté |
| Marquage des ruptures | Changement de périmètre, d'outil ou de modèle (§38.4) |

#### 38.8 🔬 Mini-lab 9 — Construire un tableau de bord MCS

**Objectif** — Produire un tableau de bord exploitable et repérer les métriques trompeuses.
**Durée** 45 min · **Difficulté** 🔴 avancé · **Prérequis** §38.2, §38.3, annexes I.4 et K · **Livrable** deux tableaux de bord (comité, direction) + trois métriques trompeuses identifiées.
**Compétences validées** — ✔ définir un indicateur par ses huit attributs ✔ adapter le tableau de bord à son audience ✔ repérer une métrique trompeuse ✔ publier une population non mesurée sans la faire disparaître

**Données fournies.**

| Source | Contenu |
|---|---|
| Inventaire | Périmètre de référence : 340 actifs, dont 28 hors support, 12 sans propriétaire |
| Scans | 268 actifs scannés avec authentification, 31 en échec d'authentification, 41 non scannés (dont 14 exclus documentés) |
| Constats | 1 240 ouverts, dont 38 critiques échus ; âge moyen 74 jours, médiane 21 jours, maximum 610 jours |
| Tickets | 96 ouverts, 14 dépassant leur échéance, 9 sans propriétaire accepté |
| Dérogations | 17 ouvertes, âge moyen 8 mois, dont 4 renouvelées au moins une fois |
| Campagnes | 6 en cours, 2 en retard, taux d'échec moyen 4 % |
| Conformité | 241 actifs conformes sur les 268 scannés avec succès |

**Questions.** (a) Proposez 5 à 8 indicateurs avec leur formule et leur périmètre. (b) Produisez la version comité MCS et la version direction générale. (c) Identifiez trois métriques trompeuses que ces données invitent à produire.

**Corrigé commenté**

**(a) Les indicateurs retenus**

| Indicateur | Formule | Valeur | Commentaire |
|---|---|---|---|
| Couverture de scan | 268 / 340 | **79 %** | Le chiffre qui conditionne tous les autres |
| Conformité interne au scan | 241 / 268 | 90 % | À ne jamais publier seul |
| **Ratio confirmé conforme** | 241 / 340 | **71 %** | Conservateur : traite les 72 non mesurés comme non conformes |
| **Non mesuré** | 72 / 340 | **21 %** | La valeur qui appelle une décision |
| Actifs hors support | 28 / 340 | 8,2 % | Dette structurelle |
| Dette critique échue | 38 constats | 38 | En valeur absolue, pas en taux |
| Âge du *backlog* | médiane / maximum | 21 j / **610 j** | La médiane rassure, le maximum informe |
| Âge des dérogations | moyenne, dont renouvelées | 8 mois, 4 renouvelées | Dette acceptée |
| Actifs sans propriétaire | 12 | 12 | Blocage structurel |

**(b) Les deux versions**

*Comité MCS* — les huit ci-dessus, avec les 41 actifs non scannés détaillés (14 exclus documentés, 27 à traiter) et les 9 tickets sans propriétaire accepté.

*Direction générale* — quatre lignes seulement :
1. Ratio confirmé conforme : **71 %**, avec 21 % non mesuré — tendance sur quatre trimestres.
2. Actifs hors support : **28**, dont X exposés — avec le plan et son coût.
3. Constats critiques échus : **38** — avec la cause principale.
4. Dette acceptée : **17 dérogations**, dont 4 renouvelées — décision demandée sur celles-ci.

**(c) Les trois métriques trompeuses**

| Métrique | Pourquoi elle trompe |
|---|---|
| **« 90 % de conformité »** | C'est la conformité **dans la population mesurée**, sur 79 % de couverture. Le ratio confirmé conforme est de 71 %, et 21 % du périmètre reste **non mesuré** — c'est-à-dire ni conforme ni non conforme (Annexe K.2) |
| **« Âge moyen du *backlog* : 74 jours »** | La moyenne est tirée par un maximum à 610 jours. La médiane à 21 jours décrit le flux normal, le maximum décrit le problème. Publier la seule moyenne ne décrit ni l'un ni l'autre |
| **« 1 240 constats ouverts »** | Volume brut sans priorisation ni couverture. Il baisserait si l'on scannait moins, et il n'indique aucune décision (§5.7) |

**L'erreur attendue** : produire un tableau de bord de quinze indicateurs pour la direction générale. Le nombre d'indicateurs est inversement proportionnel au niveau hiérarchique.

#### 38.9 🔴 FIL ROUGE — octobre 2028 : la question du directeur financier

Claire Nadeau présente au comité de direction le tableau de bord trimestriel. Quatre indicateurs, une tendance sur huit trimestres.

| Indicateur | T4 2026 | T4 2028 |
|---|---|---|
| Conformité globale, périmètre de référence | 72 % | **94 %** |
| Actifs hors support | 41 | **9** |
| Constats critiques échus | 61 | **7** |
| Dérogations ouvertes | 3 | **19** |

**La question de Karim Lebrun** porte sur la dernière ligne : *« Les trois premiers indicateurs s'améliorent nettement. Le quatrième a été multiplié par six. Comment interprétez-vous cela ? »*

**La réponse de Claire**, et c'est le point de cet épisode : les 3 dérogations de 2026 ne signifiaient pas que l'organisation n'avait que trois exceptions. Elles signifiaient qu'elle n'en formalisait que trois. Les autres existaient — sous forme de constats jamais traités, de systèmes ignorés, de compensations informelles. Les 19 dérogations de 2028 sont la **partie enfin visible** d'une dette qui a en réalité diminué.

Elle le démontre par un chiffre complémentaire : les constats ouverts depuis plus de 180 jours et non qualifiés — les dérogations non formalisées du §17.10 — sont passés de **47 à 2**.

**Ce que Karim Lebrun demande alors**, et qui devient la meilleure question de tout le fil rouge : *« Alors comment saurai-je, l'an prochain, si 19 dérogations est un bon ou un mauvais chiffre ? »*

**La réponse construite en séance**, qui donnera lieu à deux indicateurs supplémentaires : le nombre de dérogations n'est pas interprétable seul. Ce qui compte est leur **âge moyen** — une dette qui vieillit est une dette qui pourrit (§20.9) — et le **nombre de renouvellements**, qui mesure combien d'exceptions ont échoué à se résoudre.

**Les décisions du comité.**

1. Ajout de deux indicateurs au tableau de bord de direction : âge moyen des dérogations, et nombre de dérogations renouvelées au moins une fois.
2. Revue annuelle en comité de direction des dérogations renouvelées deux fois ou plus — application du §7.4.
3. La progression 72 % → 94 % est communiquée à l'assureur, avec le dossier de preuves associé. La surprime de 34 % d'octobre 2025 (§1.9) fait l'objet d'une renégociation.

**Ce que Claire note en conclusion.** *Le meilleur indicateur de maturité d'une organisation n'est pas son taux de conformité. C'est l'écart entre ce qu'elle sait de ses propres écarts et ce qu'elle en montre.*

→ La suite en 🔴 §39.8, avec la revue interne et la constitution du dossier de preuves.

→ **Chapitre 39 — Audit, contrôle et production de preuve** : prouver, c'est-à-dire résister à un contrôle.

#### Synthèse mentale du chapitre 38

Un indicateur qui ne change aucune décision est décoratif, et il coûte du temps de production chaque mois. Huit attributs le définissent, dont le dénominateur, sans lequel deux personnes calculeront deux valeurs différentes. La couverture d'inventaire et la couverture de scan conditionnent tous les autres indicateurs : 95 % de conformité sur 60 % de couverture vaut 57 %. Les moyennes masquent la traîne — publiez médiane et maximum —, et un indicateur de volume brut récompense l'inaction puisqu'il baisse quand on scanne moins. Une série traversant un changement de modèle de score doit être marquée discontinue : vérifiez ce qui a changé dans les données avant de célébrer une amélioration soudaine. Le nombre d'indicateurs est inversement proportionnel au niveau hiérarchique : trois à cinq pour une direction générale, avec une tendance et une décision demandée. Enfin, une hausse du nombre de dérogations peut signaler une amélioration : ce qui compte est leur âge, leur distribution et leur nombre de renouvellements.

**Trois questions de vérification**

1. Votre tableau de bord affiche 90 % de conformité. Quelles deux valeurs devez-vous connaître pour savoir ce que ce chiffre décrit réellement ?
2. Votre indicateur de vulnérabilités à forte probabilité chute de 30 % en une semaine sans aucun déploiement. Que vérifiez-vous avant toute communication ?
3. Le nombre de dérogations de votre organisation a été multiplié par six en deux ans. Est-ce un bon ou un mauvais signe, et quels indicateurs complémentaires permettent de trancher ?

---

### Chapitre 39 — Audit, contrôle et production de preuve

#### 39.1 Ce que « prouver son MCS » signifie

Prouver, ce n'est ni affirmer ni montrer un tableau de bord. C'est établir quatre choses, et l'ordre compte :

| # | Ce qu'il faut établir | Sans quoi |
|---|---|---|
| 1 | **Le périmètre** : sur quoi porte le dispositif, et ce qui en est exclu | Tout le reste est invérifiable |
| 2 | **La règle** : ce que l'organisation s'engage à faire, écrit et daté | On ne peut mesurer aucun écart |
| 3 | **L'application** : ce qui a effectivement été fait, avec des données datées | L'engagement reste théorique |
| 4 | **Le traitement des écarts** : ce qui n'a pas été fait, et pourquoi c'est décidé | La preuve devient une fiction |

**Le quatrième point est celui qui distingue un dossier crédible d'un dossier de façade.** Un dossier sans écart n'est pas un bon dossier, c'est un dossier incomplet — aucune organisation n'applique 100 % de sa politique sur 100 % de son parc. Ce que regarde un auditeur, c'est si les écarts sont **connus, décidés et suivis**.

#### 39.2 Le dossier de preuves

Structuré une fois, projeté ensuite sur chaque référentiel (§8.8). Onze pièces.

| # | Pièce | Contenu | Chapitre |
|---|---|---|---|
| 1 | **Périmètre de référence daté** | Sources, réconciliation, écarts expliqués, zones déclarées non couvertes | 10 |
| 2 | Politique MCS | Version, date, approbation nominative, classes de service | 7 |
| 3 | RACI et comitologie | Rôles, décideurs, fréquence | 9 |
| 4 | Arbre de décision de triage | Daté, validé | 16 |
| 5 | **Journaux de campagne** | Périmètre, exécution, échecs, traîne longue qualifiée | 18 |
| 6 | **Preuves d'état** | Relevés horodatés sur échantillon, indépendants des outils | 2 |
| 7 | Registre des dérogations | Sept champs, signataires, revues | 7, 20 |
| 8 | Registre des exclusions | Scan, protection des postes, avec motif et compensation | 15, 34 |
| 9 | Comptes rendus de comité | **Décisions**, pas discussions | 9 |
| 10 | Indicateurs historisés | Définitions, séries, ruptures marquées | 38 |
| 11 | Procès-verbaux de décommissionnement | Signés, avec vérification | 35 |

✅ **BONNE PRATIQUE (P0)** — Constituez ce dossier **en continu**, pas à l'approche d'un contrôle. Un dossier reconstitué après coup se voit immédiatement : les dates de production sont groupées, les preuves d'état sont postérieures aux campagnes qu'elles documentent, et les comptes rendus manquent d'aspérités.

#### 39.3 Se préparer à un contrôle

| Type de contrôle | Ce qui est regardé en priorité |
|---|---|
| **Certification** | Existence et fonctionnement du système de management ; échantillonnage |
| **Autorité** | Conformité aux obligations applicables, traitement des incidents |
| **Client** | Ce qui concerne **son** périmètre : sa donnée, son service, ses délais |
| **Assureur** | Les points du questionnaire, et leur cohérence avec la réalité (§37.3) |
| **Audit interne** | Écart entre la règle et la pratique |

**Les six constats les plus fréquents**, et le chapitre qui les traite :

| Constat | Origine | Traité au |
|---|---|---|
| Périmètre non défini ou incohérent entre documents | Inventaire absent ou non réconcilié | 10 |
| Indicateurs sans dénominateur | Reporting produit par l'outil | 38 |
| Exceptions non formalisées | Constats anciens jamais qualifiés | 17, 20 |
| Absence de preuve d'application | Clôture sur déclaration | 17, 18 |
| Exclusions non documentées | Actifs difficiles sortis silencieusement | 15, 34 |
| Prestataires non contrôlés | Contrat sans clause de restitution | 13 |

#### 39.4 L'audit interne du MCS

Se contrôler soi-même avant qu'un tiers ne le fasse, avec une méthode d'échantillonnage plutôt qu'une revue exhaustive.

**Le plan de contrôle type**, six tests par sondage :

| Test | Méthode | Ce qu'il révèle |
|---|---|---|
| **Test de périmètre** | Prendre 20 actifs au hasard dans une source non utilisée pour le reporting, vérifier leur présence dans le périmètre | Trous d'inventaire |
| **Test d'état** | Vérifier directement sur 15 actifs l'état déclaré conforme | Écart entre déclaration et réalité |
| **Test de délai** | Prendre 10 constats clos, recalculer le délai réel | Fiabilité de l'indicateur |
| **Test de preuve** | Demander la preuve de 10 clôtures | Clôtures sur déclaration |
| **Test de dérogation** | Vérifier que les compensations de 5 dérogations sont **effectivement actives** | Compensations disparues (§20.7) |
| **Test de décommissionnement** | Vérifier les résidus de 5 décommissionnements anciens | Le §35.14 |

**Le cinquième test est le plus productif** : il vérifie une chose que personne ne vérifie jamais, et qui échoue souvent.

#### 39.5 Homologation et réhomologation

Dans les contextes où une décision formelle d'autorisation d'usage est requise, le MCS conditionne le maintien de cette décision dans le temps.

| Élément | Ce que le MCS doit fournir |
|---|---|
| Dossier initial | État du système, dispositif de maintien prévu |
| **Maintien** | Preuve que le dispositif fonctionne — c'est le dossier du §39.2 |
| Changements significatifs | Ce qui déclenche un réexamen |
| Réhomologation | Bilan sur la période, écarts, plan |

**Le point pratique** : une homologation prononcée sur la base d'un dispositif de MCS qui n'a pas fonctionné devient contestable. C'est un argument utile en interne pour obtenir les moyens du maintien, et non seulement ceux de la mise en service.

#### 39.6 ⚠️ Les preuves qui ne prouvent rien

| Preuve produite | Pourquoi elle ne vaut rien |
|---|---|
| Capture d'écran non datée | Ni date, ni périmètre, ni intégrité |
| Extraction d'outil sans périmètre | On ignore sur quoi elle porte (§15.8) |
| Chiffre agrégé sans dénominateur | Interprétation impossible |
| Politique non approuvée | Un projet n'engage personne |
| Compte rendu relatant des discussions | Aucune décision traçable |
| Déclaration d'un prestataire sans donnée | Confiance, pas preuve (§13.3) |
| Rapport présentant 100 % de conformité | Possible sur un petit périmètre maîtrisé, mais doit déclencher un examen du périmètre, des exclusions et des actifs non joignables |
| Dossier constitué en trois jours | Les métadonnées le montrent |

#### 39.7 Conserver la preuve

| Exigence | Contenu |
|---|---|
| Durée | Alignée sur les obligations applicables et la durée de vie des actifs — souvent 3 à 5 ans |
| **Intégrité** | Horodatage, stockage non modifiable, ou signature |
| **Indépendance des outils** | Export en format ouvert : un changement d'outil ne doit pas effacer l'antériorité (§15.12) |
| Accessibilité | Retrouvable en heures, pas en jours |
| Continuité | Les changements de définition et de périmètre sont documentés (§38.7) |

#### 39.8 🔴 FIL ROUGE — janvier 2029 : la revue interne

Trois ans après l'arrivée de Claire Nadeau, HELIOMED conduit sa première revue interne complète du dispositif de MCS, avec un auditeur externe mandaté par la direction générale — en préparation d'une exigence client et de la renégociation d'assurance.

**Le dossier présenté** : les onze pièces du §39.2, constituées en continu depuis 2026.

**Les quatre écarts constatés.**

| # | Écart | Origine |
|---|---|---|
| 1 | **12 actifs du périmètre de référence absents de tout outil de gestion** | Machines de laboratoire de Nantes, créées après la dernière réconciliation |
| 2 | **Compensations de 2 dérogations sur 5 testées non actives** | Une règle de filtrage supprimée lors d'une refonte réseau en juin 2028, sans que la dérogation ne soit alertée |
| 3 | **Preuve d'état manquante sur 3 campagnes de 2027** | Clôtures fondées sur le rapport de console seul, sans échantillon vérifié |
| 4 | **Registre des exclusions de la protection des postes incomplet** | 6 exclusions ajoutées après la revue de juillet 2028, non enregistrées |

**Ce que l'auditeur relève comme point fort**, et c'est ce que Claire retient : *« L'organisation connaît ses écarts. Les quatre constats de cet audit portent sur des dispositifs qui existent et qui ont partiellement failli, pas sur des dispositifs absents. Le point le plus favorable du dossier est l'annexe des périmètres déclarés non couverts, tenue depuis 2026. »*

C'est l'annexe d'une page ajoutée à la politique v1 en mai 2026 (§7.7) — celle qui ressemblait à un aveu de faiblesse.

**L'écart n° 2 est celui qui préoccupe le plus l'équipe.** Une compensation disparue signifie qu'un risque accepté sous condition était en réalité porté sans condition, pendant sept mois, sans que personne ne le sache. C'est très exactement le mécanisme du §20.7, attribut 4 — le moyen de vérification existait sur la fiche, mais le contrôle mensuel n'avait pas été réalisé depuis mars.

**Les corrections décidées.**

1. **Contrôle des compensations** inscrit comme point d'ordre du jour permanent du comité MCS, avec test effectif et non déclaratif — cinq minutes par mois (§20.7).
2. **Réconciliation d'inventaire** portée de trimestrielle à mensuelle, automatisée (§10.7).
3. **Échantillon de preuve d'état** rendu obligatoire pour toute campagne de plus de 20 actifs, avec le point de contrôle du §15.13.
4. **Registre des exclusions** rattaché au workflow : aucune exclusion ne peut être ajoutée sans ticket (§34.4).

**Le résultat externe.** L'assureur accepte de ramener la surprime de 34 % à 6 %, sur la base du dossier de preuves et de la trajectoire sur huit trimestres. Le gain annuel dépasse le coût cumulé de l'outillage acquis depuis 2026.

**Ce que Pierre Vasseur dit en clôture du comité**, et qui referme le fil rouge ouvert au §1.9 : *« En octobre 2025, on nous a reproché de ne pas pouvoir démontrer un processus qui existait. Aujourd'hui, on nous reproche quatre écarts dans un processus que nous démontrons. C'est exactement la différence que je voulais. »*

→ **Fin de la Partie VI.** La suite en Partie VII, avec la construction d'un programme complet et les trois cas de synthèse.

→ **Chapitre 40 — Construire un programme MCS de zéro à douze mois** : mettre tout cela en séquence sur douze mois.

#### Synthèse mentale du chapitre 39

Prouver son MCS suppose d'établir quatre choses dans l'ordre : le périmètre, la règle, l'application, et le traitement des écarts. Le quatrième distingue un dossier crédible d'un dossier de façade — un dossier sans écart n'est pas bon, il est incomplet, car aucune organisation n'applique 100 % de sa politique sur 100 % de son parc. Onze pièces composent le dossier, à constituer en continu : reconstitué après coup, il se voit immédiatement. L'audit interne se conduit par sondages, et le test le plus productif est celui que personne ne fait jamais — vérifier que les compensations des dérogations sont effectivement actives. Enfin, un rapport annonçant 100 % de conformité est statistiquement invraisemblable : il signale que les actifs non joignables ont été omis.

**Trois questions de vérification**

1. Un auditeur vous demande de démontrer votre gestion des correctifs. Quelles quatre choses devez-vous établir, et dans quel ordre ?
2. Pourquoi un dossier de preuves ne comportant aucun écart est-il un mauvais signe plutôt qu'un bon ?
3. Parmi les six tests d'audit interne, lequel échoue le plus souvent, et pourquoi personne ne le réalise-t-il spontanément ?

---

---

> ### 🎓 À ce stade de la Partie VI, vous savez…
>
> - **retirer** un système proprement, et vérifier qu'il ne survit pas dans les comptes, les clés, les certificats et les sauvegardes ;
> - **automatiser** dans le bon ordre, et reconnaître le seul critère qui autorise l'auto-remédiation ;
> - **chiffrer** le MCS, construire un dossier d'investissement à trois options, et repérer les seuils de rupture d'une équipe ;
> - **définir** un indicateur avec sa population éligible et son dénominateur, et distinguer une mesure d'un ratio conservateur ;
> - **constituer** un dossier de preuves en continu, et conduire un audit interne par sondages.
>
> **Ce qu'il vous reste** : mettre tout cela en séquence, et l'éprouver sur des cas. C'est l'objet de la Partie VII.


## PARTIE VII — Mise en œuvre

---

### Chapitre 40 — Construire un programme MCS de zéro à douze mois

#### 40.1 Le diagnostic en quinze jours : six questions

Avant tout plan, situez l'organisation. Six questions suffisent, et les réponses se trouvent en deux semaines.

| # | Question | Ce que la réponse révèle |
|---|---|---|
| 1 | **Combien d'actifs devons-nous maintenir ?** Et quel est l'écart entre vos sources ? | La fiabilité de tout indicateur futur (ch. 10) |
| 2 | **Qui décide qu'on arrête tel actif pour le corriger ?** | L'existence ou non d'une propriété d'actif (§5.5) |
| 3 | **Quels actifs sont joignables depuis Internet ?** | Le risque réel immédiat (ch. 11) |
| 4 | **Quand a-t-on appliqué le dernier correctif, et comment le prouve-t-on ?** | La capacité à produire une preuve (§2.9) |
| 5 | **Que fait-on quand on ne peut pas corriger ?** | L'existence d'un chemin légitime pour les écarts (§7.4) |
| 6 | **Combien d'actifs sont hors support, et qu'a-t-on décidé ?** | La dette et sa reconnaissance (ch. 12) |

**La lecture des réponses.** Si les questions 1 et 2 n'ont pas de réponse, ne commencez rien d'autre. Si la question 3 n'a pas de réponse, c'est votre première action — elle produit des fermetures immédiates (§11.8). Si la question 5 n'a pas de réponse, votre organisation dissimule ses écarts sans le savoir.

#### 40.2 Jours 0-30 : établir le socle

| Prio | Action | Livrable |
|---|---|---|
| **P0** | Croiser 4 sources d'inventaire, dont une non technique | Périmètre de référence avec ses écarts |
| **P0** | Attribuer criticité et exposition, même grossièrement | Base des classes de service |
| **P0** | Lancer la campagne de désignation des propriétaires | Liste nominative, actifs orphelins identifiés |
| **P0** | Exercice de découverte externe | Carte des actifs exposés |
| **P0** | **Fermer les expositions inutiles** | Réduction de risque immédiate, sans correctif |
| **P0** | Publier le périmètre **avec ses zones non couvertes** | Crédibilité de tous les chiffres ultérieurs |
| P1 | Identifier les actifs de niveau 0 | Liste d'une page (§11.7) |
| P1 | Vérifier les cinq configurations du §22.1 sur ces actifs | Gains rapides sans fenêtre |

**Ce qu'on ne fait pas pendant ce mois** : acheter un outil, publier un taux de conformité, lancer une campagne de correctifs massive.

#### 40.3 Jours 30-90 : poser la règle

| Prio | Action | Livrable |
|---|---|---|
| **P0** | Rédiger la politique MCS avec ses classes de service | Politique v1, délais tenables (§7.2) |
| **P0** | Créer la procédure de dérogation | Chemin légitime pour les écarts |
| **P0** | Constituer la matrice de couverture de veille | Trous identifiés (§14.1) |
| **P0** | Écrire l'arbre de décision de triage | Priorisation défendable (§16.3) |
| P1 | Mettre en place le workflow de remédiation | File unique, états, échéances (ch. 17) |
| P1 | Installer la comitologie | Comité MCS mensuel avec relevé de décisions |
| P1 | **Premier cycle complet mesuré** | De la détection à la preuve, sur un périmètre restreint |

**Le premier cycle complet est le livrable clé de cette phase.** Mieux vaut un cycle entier réussi sur 40 actifs qu'un cycle partiel sur 400 : il révèle tous les points de rupture de la chaîne, à faible coût.

#### 40.4 Jours 90-180 : industrialiser

| Prio | Action |
|---|---|
| **P0** | Consolider le reporting **par le périmètre**, pas par les outils (§19.8) |
| **P0** | Traiter le trou des applications tierces du poste de travail (§19.5) |
| P1 | Mettre en place les anneaux de déploiement et les critères d'arrêt |
| P1 | Dériver une *baseline* de configuration et automatiser son contrôle |
| P1 | Constituer le référentiel de fin de support et le plan d'obsolescence |
| P1 | Publier les premiers indicateurs, avec leurs définitions |
| P1 | Revue des comptes de service et des accès à privilèges (ch. 24) |
| P2 | Négocier les clauses MCS avec les prestataires (§13.3) |

#### 40.5 Jours 180-365 : étendre et prouver

| Prio | Action |
|---|---|
| **P0** | Étendre aux périmètres déclarés non couverts, dans l'ordre de leur risque |
| **P0** | Constituer le dossier de preuves en continu (§39.2) |
| P1 | Traiter l'industriel, avec l'équipe de maintenance (ch. 29) |
| P1 | Traiter le cloud et les services en ligne (ch. 30, 31) |
| P1 | Traiter la non-production et les actifs d'administration (ch. 28) |
| P1 | Mettre en place le décommissionnement avec procès-verbal (ch. 35) |
| P1 | Automatiser collecte, corrélation et vérification (§36.1) |
| P2 | Module produit, si applicable (ch. 33) |
| P2 | Premier audit interne par sondages (§39.4) |

#### 40.6 Adapter au contexte

| Contexte | Ce qui change |
|---|---|
| **PME (< 200 actifs)** | Formalisme allégé : un tableau tenu à jour remplace un outil. Les rôles se cumulent, mais restent distingués mentalement (§9.6). Priorité absolue à l'exposition et aux actifs de niveau 0 |
| **ETI** | Le modèle décrit ici. Le point critique est la propriété d'actif et la comitologie |
| **Groupe multi-sites** | Modèle mixte : classes, délais et format de preuve définis centralement ; exécution locale (§9.5) |
| **Parc entièrement infogéré** | Le programme démarre par le contrat (ch. 13), pas par la technique. Sans clause de restitution, aucune mesure n'est possible |
| **Organisation industrielle** | Deux programmes parallèles, avec des rythmes différents (ch. 29). Ne jamais imposer le rythme bureautique à l'usine |

#### 40.7 Les erreurs de séquencement les plus coûteuses

| Erreur | Conséquence |
|---|---|
| **Acheter un outil avant l'inventaire** | Automatiser un périmètre inconnu, tableaux de bord verts sur dénominateur faux |
| Publier un taux de conformité avant de connaître son dénominateur | Perte de crédibilité irréversible au premier audit |
| Lancer une campagne massive avant d'avoir des propriétaires | Blocage au premier refus, découragement de l'équipe |
| Écrire une politique avant de mesurer sa capacité | Non-conformité permanente (§7.2) |
| Traiter l'industriel avec les méthodes bureautiques | Rejet, et perte durable de l'accès (ch. 29) |
| Négliger les actifs de niveau 0 parce qu'ils ne sont pas exposés | Le chemin le plus court reste ouvert (§34.12) |
| Reporter la preuve à plus tard | Impossible à reconstituer, et budget non pérennisé |

#### 40.8 ✅ Feuille de route consolidée

**P0 — sans quoi rien ne fonctionne**

1. Périmètre de référence, croisé sur plusieurs sources, publié avec ses zones non couvertes.
2. Propriétaires nommés, avec procédure pour les actifs orphelins.
3. Carte des actifs exposés, et fermeture des expositions inutiles.
4. Liste des actifs de niveau 0, tous en classe C1.
5. Politique avec classes de service et délais **tenables**.
6. Procédure de dérogation, avec date d'expiration et compensation.
7. Arbre de décision de triage, écrit et daté.
8. Preuve d'état sur échantillon, indépendante des outils.

**P1 — ce qui rend le dispositif durable**

9. File unique et workflow de remédiation avec escalade automatique.
10. Anneaux de déploiement et critères d'arrêt chiffrés.
11. Matrice de couverture de veille, et traitement des trous.
12. Référentiel de fin de support et plan d'obsolescence financé.
13. *Baseline* de configuration dérivée et contrôlée.
14. Revue des comptes de service, des secrets et des certificats.
15. Clauses contractuelles avec les prestataires, dont la restitution de données.
16. Indicateurs définis, historisés, publiés par population.

**P2 — ce qui fait la différence dans la durée**

17. Automatisation de la collecte, de la corrélation et de la vérification.
18. Décommissionnement avec procès-verbal et vérification à J+90.
19. Exigences de maintenabilité dans les cahiers des charges (§6.2).
20. Audit interne périodique par sondages.

🖼 **SCHÉMA — La chaîne complète du MCS.** *Poster récapitulatif pleine page reprenant les six segments avec leurs chapitres. Destiné à l'impression séparée.*

#### 40.9 La chaîne complète, en une page

Le schéma directeur du §1.1, déplié avec ses chapitres. C'est la page à garder sous la main.

```
  ┌─ ① CONNAÎTRE ──────────────────────────────────────────────────┐
  │  Inventaire (10) ─► Propriété (5) ─► Criticité + Exposition (11)│
  │  Obsolescence (12) ─► Délégué (13)                              │
  └──────────────────────────────┬─────────────────────────────────┘
                                 ▼
  ┌─ ② OBSERVER ───────────────────────────────────────────────────┐
  │  Veille toutes origines (14) ─► Détection technique (15)        │
  │  Faits / hypothèses / pistes (14.7)                             │
  └──────────────────────────────┬─────────────────────────────────┘
                                 ▼
  ┌─ ③ DÉCIDER ────────────────────────────────────────────────────┐
  │  Arbre de décision (16) ─► File unique, 2 horloges (17)         │
  │  Exploitation × Exposition × Criticité                          │
  └──────────────────────────────┬─────────────────────────────────┘
                                 ▼
  ┌─ ④ CORRIGER, COMPENSER OU DÉROGER ─────────────────────────────┐
  │  Campagne : qualifier ─► tester ─► anneaux ─► arrêt auto (18-19)│
  │  Impossible ? hiérarchie des compensations (20)                 │
  │  Configuration (22-23) · Identités (24) · Code (25-26)          │
  │  Couches basses (27) · Non-production (28)                      │
  │  Contextes : OT (29) · Cloud (30) · SaaS (31) · Legacy (32)     │
  │  Urgence ? réduire l'exposition d'abord (21)                    │
  └──────────────────────────────┬─────────────────────────────────┘
                                 ▼
  ┌─ ⑤ VÉRIFIER ───────────────────────────────────────────────────┐
  │  Technique ─► effectivité (redémarrage) ─► fonctionnelle (18.9) │
  │  Traîne longue qualifiée (18.10)                                │
  └──────────────────────────────┬─────────────────────────────────┘
                                 ▼
  ┌─ ⑥ PROUVER ────────────────────────────────────────────────────┐
  │  Preuve d'état (2.9) ─► Indicateurs (38) ─► Dossier (39)        │
  │  Décommissionnement (35) ─► retour au périmètre ①               │
  └──────────────────────────────┬─────────────────────────────────┘
                                 │
      ┌──────────────────────────┴──────────────────────────┐
      │  EN PERMANENCE                                       │
      │  Gouvernance (9) · Économie et soutenabilité (37)     │
      │  Automatisation (36) · MCS by design (6)              │
      └──────────────────────────────────────────────────────┘
```

**Les six règles qui résument tout le cours**

1. On ne maintient pas ce qu'on ne connaît pas — et le dénominateur inconnu rend tous les indicateurs faux, dans le sens favorable.
2. Un actif sans propriétaire nommé n'est pas un actif maintenu ; il reste dans le périmètre.
3. L'exposition et la criticité métier ne sont produites par personne d'autre que vous.
4. Fermer une exposition inutile protège aussi contre les vulnérabilités futures.
5. Un délai accordé par la politique est une ressource, pas un retard.
6. Ce qui n'est pas prouvé ne se pilote pas, ne se finance pas, et ne se défend pas.

#### Synthèse mentale du chapitre 40

Six questions suffisent à situer une organisation en quinze jours, et deux d'entre elles sont bloquantes : combien d'actifs, et qui décide de les arrêter. Le premier mois établit le socle sans acheter d'outil, sans publier de taux et sans lancer de campagne massive — il ferme en revanche les expositions inutiles, ce qui produit une réduction de risque immédiate. Le premier cycle complet, de la détection à la preuve, vaut mieux réussi sur quarante actifs que partiel sur quatre cents : il révèle tous les points de rupture à faible coût. Les erreurs de séquencement les plus coûteuses consistent à outiller avant d'inventorier, à publier un taux avant d'en connaître le dénominateur, et à reporter la preuve — laquelle est impossible à reconstituer après coup. Enfin, dans un parc infogéré, le programme démarre par le contrat et non par la technique.

**Trois questions de vérification**

1. Vous prenez un poste de responsable sécurité dans une organisation sans dispositif de MCS. Quelles sont vos deux premières questions, et pourquoi bloquent-elles tout le reste ?
2. Votre direction veut voir un taux de conformité dès le premier mois. Que répondez-vous, et que proposez-vous à la place ?
3. Pourquoi vaut-il mieux réussir un cycle complet sur quarante actifs qu'un cycle partiel sur quatre cents ?

---

## Cas de synthèse

Les trois cas qui suivent se travaillent en situation, les annexes ouvertes. Chacun reprend le fil rouge HELIOMED à un moment précis, fournit les données disponibles à cet instant, et demande des décisions. Les corrigés commentent aussi les **erreurs volontairement insérées** dans les scénarios.

---

### Cas de synthèse A — 0-day activement exploitée sur la passerelle d'accès distant

> **Format** — Cas à traiter en situation, annexes ouvertes. Durée estimée : **3 heures** en individuel, une demi-journée en groupe.
> **Livrables attendus** : journal de crise (D.11) · demande de changement urgent (D.5) · critères go/no-go (D.6) · note à la direction · retour d'expérience.
> **Prérequis** : chapitres 11, 14, 16, 18, 20, 21, 27, 34.

---

#### A.1 Le dossier initial

**Vous êtes** Claire Nadeau, RSSI du groupe HELIOMED. Nous sommes le **jeudi 9 juillet 2027, 8 h 40**.

##### Artefact 1 — l'alerte reçue

> **CERT sectoriel — Alerte ALT-2027-0714 — 09/07/2027 07:52 UTC — Niveau : critique**
>
> Une vulnérabilité affectant les passerelles d'accès distant du constructeur `[X]` fait l'objet d'une **exploitation active** confirmée chez plusieurs entités européennes du secteur de la santé. La vulnérabilité permet une exécution de code à distance **sans authentification préalable** sur l'interface d'administration du produit.
>
> Versions affectées : `4.2.x` antérieures à `4.2.19`, `4.4.x` antérieures à `4.4.7`.
> Correctif : publié par le constructeur le 09/07/2027 à 02:10 UTC.
> Contournement : restriction d'accès à l'interface d'administration.
>
> Le CERT recommande une vérification immédiate des équipements exposés et une recherche d'indicateurs de compromission.

##### Artefact 2 — extrait de l'inventaire, `GW-VPN-01` / `GW-VPN-02`

```yaml
id_actif: GW-VPN-01              # couple haute disponibilité avec GW-VPN-02
type: securite
modele: passerelle d'accès distant
version_logicielle: "4.2.11"
mis_en_service: 2022-03-14
derniere_mise_a_jour: 2025-11-08
criticite: C1
exposition: internet
proprietaire_metier: s.weber
proprietaire_technique: m.ferhaoui
fenetre_maintenance: "mardi 22h-02h, urgence pré-autorisée sous 72h"
journalisation: locale, rétention 30 jours, PAS d'export externe
utilisateurs_actifs_30j: 210
outils_couverture: [scan:non — appliance fermée]
```

##### Artefact 3 — configuration réseau publiée

```
# Règles de publication, extraction du 09/07/2027 08:15

ALLOW  0.0.0.0/0        -> gw-vpn.heliomed.fr:443/tcp   "service accès distant"      [active depuis 2022-03-14]
DENY   0.0.0.0/0        -> gw-vpn.heliomed.fr:8443/tcp  "interface administration"   [modifiée le 2026-09-22]
ALLOW  10.0.0.0/8       -> gw-vpn.heliomed.fr:8443/tcp  "administration interne"     [active depuis 2026-09-22]
```

##### Artefact 4 — journal des changements de l'équipement

```
2022-03-14  Mise en service, version 4.2.3
2022-03-14  Publication 443/tcp et 8443/tcp — demande CHG-2022-0341
            motif : "télétravail massif, accès administration depuis l'extérieur"
            durée demandée : "temporaire, le temps de la période"
2023-06-02  Mise à jour 4.2.3 -> 4.2.7
2025-11-08  Mise à jour 4.2.7 -> 4.2.11
2026-09-22  Fermeture 8443/tcp depuis Internet — suite exercice de découverte externe
2027-07-09  [aucune action]
```

##### Artefact 5 — état de la journalisation

| Source | Rétention | Export externe | Contenu |
|---|---|---|---|
| Journaux de la passerelle | **30 jours**, sur l'équipement | **Non** | Connexions, authentifications, actions d'administration |
| Journaux du pare-feu amont | 12 mois, exportés | Oui | Flux, sans contenu applicatif |
| Journaux d'annuaire | 12 mois, exportés | Oui | Authentifications des utilisateurs |

##### Artefact 6 — contraintes du jour

- 210 collaborateurs utilisent l'accès distant, dont **7 en déplacement** ce jour (2 en clientèle hospitalière, 5 sur un salon professionnel).
- L'équipe disponible : Malik Ferhaoui, un ingénieur d'astreinte, vous-même.
- Le comité MCS du mois a lieu le mardi suivant.
- La police d'assurance impose une déclaration conservatoire **sous 72 h** en cas d'incident de sécurité présumé.

---

#### A.2 Les questions à traiter

| # | Question | Livrable |
|---|---|---|
| 1 | Que faites-vous entre H+0 et H+2 ? Justifiez chaque décision. | Journal D.11, premières lignes |
| 2 | Quelle question devez-vous poser que les artefacts ne posent pas ? | — |
| 3 | Quel niveau de qualification retenez-vous, et pourquoi ? | — |
| 4 | Rédigez la phrase exacte que vous dites à la direction générale. | Note de situation |
| 5 | Que comprimez-vous du processus normal, que conservez-vous ? | D.5 + D.6 |
| 6 | Corriger ou reconstruire ? Sur quel critère ? | Décision tracée |
| 7 | Quatre erreurs sont volontairement présentes dans le dossier. Lesquelles ? | — |
| 8 | Variante : mêmes faits, organisation de 40 personnes sans astreinte. | — |

---

#### A.3 Corrigé — heures 0 à 2

##### H+0 — qualifier à la source

**Ce qu'il ne faut pas faire** : agir sur la foi de l'alerte relayée. **Ce qu'il faut faire** : ouvrir l'avis du constructeur et comparer.

| Vérification | Résultat |
|---|---|
| Version installée `4.2.11` dans la plage affectée `< 4.2.19` ? | **Oui** |
| Correctif disponible ? | Oui, `4.2.19`, publié il y a 6 h |
| Contournement officiel ? | Oui : restreindre l'accès à l'interface d'administration |
| Statut de qualification (§14.7) | **Fait vérifié** |

⚠️ Le second équipement `GW-VPN-02` doit être vérifié **séparément** : rien ne garantit que les deux membres du couple portent la même version. C'est une vérification de trente secondes que la pression fait sauter.

##### H+1 — mesurer l'exposition

Les trois questions du §11.1 appliquées aux artefacts 2 et 3 :

| Question | Réponse | Source |
|---|---|---|
| **Depuis où est-il joignable ?** | Le service d'accès distant `443/tcp` est publié sur Internet. L'interface d'administration `8443/tcp` **ne l'est plus depuis le 22/09/2026** | Artefact 3 |
| **Par qui ?** | Anonyme sur `443`, réseau interne sur `8443` | Artefact 3 |
| **Vers quoi mène-t-il ?** | Réseau interne complet — c'est une passerelle d'accès | Fonction du produit |

**Le point décisif** : la vulnérabilité porte sur **l'interface d'administration**, qui n'est plus publiée. L'exposition directe depuis Internet a donc été fermée dix mois plus tôt.

⚠️ Cela ne clôt rien, pour deux raisons :
1. Il faut **vérifier depuis l'extérieur** que la règle `DENY` est effective — une règle écrite n'est pas une règle appliquée. Un test depuis une adresse externe prend cinq minutes.
2. Un attaquant ayant obtenu un accès au réseau interne par un autre chemin (§11.4) atteint toujours `8443`.

##### H+2 — la décision structurante

Le réflexe est de corriger. La bonne action est de **réduire encore l'exposition**, parce qu'elle prend quelques minutes et n'attend ni test ni fenêtre (§21.6).

| Option | Effet | Coût métier | Délai |
|---|---|---|---|
| Couper `443` — le service entier | Protection totale | **210 personnes sans accès distant**, un jeudi | 2 min |
| **Restreindre `443` aux plages des sites HELIOMED** | Forte : ne reste que le trafic depuis les sites | **7 personnes** en déplacement | 15 min |
| Restreindre `8443` aux seuls postes d'administration | Réduit le chemin interne | Nul | 15 min |
| Ne rien faire jusqu'au correctif | Aucune | Nul | — |

**Décision retenue : options 2 et 3 combinées.** Les 7 collaborateurs en déplacement sont prévenus individuellement et basculés sur un moyen alternatif — pour les 5 du salon, une connexion depuis le poste d'un partenaire est écartée (elle créerait un chemin non maîtrisé), au profit d'un report des tâches concernées.

**Pourquoi pas la coupure totale** : la vulnérabilité porte sur `8443`, pas sur `443`. Couper le service métier ne réduirait pas le risque lié à cette vulnérabilité — c'est une réaction disproportionnée qui coûterait la crédibilité du dispositif pour la prochaine crise.

🧪 **Journal D.11 — premières lignes**

| Heure | Information | Source | Statut | Décision | Décideur |
|---|---|---|---|---|---|
| 08:40 | Alerte CERT ALT-2027-0714 | CERT sectoriel | Piste | Vérifier à la source | C. Nadeau |
| 08:55 | Version `4.2.11` affectée, sur les deux membres | Avis constructeur | **Fait** | Ouvrir la cellule | C. Nadeau |
| 09:20 | `8443` non publié depuis 22/09/2026, confirmé par test externe | Test depuis IP externe | **Fait** | Ne pas couper `443` | C. Nadeau |
| 09:40 | 7 utilisateurs en déplacement identifiés | Annuaire + journaux | Fait | Restreindre `443` aux sites, prévenir individuellement | S. Weber |
| 10:05 | Restriction appliquée et vérifiée | Test externe | Fait | — | M. Ferhaoui |

---

#### A.4 Corrigé — la question que le dossier ne pose pas

**H+3.** Le greffier consigne une remarque de Malik Ferhaoui : *« depuis quand cette version est-elle installée ? »*

Les artefacts 2 et 4 donnent la réponse, et personne ne l'avait rapprochée :

```
2022-03-14  Mise en service, version 4.2.3
2022-03-14  Publication 8443/tcp — "temporaire, le temps de la période"
2026-09-22  Fermeture 8443/tcp
```

**L'interface d'administration a été publiée sur Internet du 14 mars 2022 au 22 septembre 2026 — quatre ans et six mois.** Et la vulnérabilité publiée aujourd'hui existe dans le code depuis la branche `4.2`, soit depuis la mise en service.

**Les trois questions du §21.3 s'imposent alors :**

| Question | Réponse | Source |
|---|---|---|
| Depuis combien de temps l'actif est-il exposé et vulnérable ? | **4 ans et 6 mois** | Artefact 4 |
| Quels journaux couvrent cette période ? | **30 jours**, sur l'équipement lui-même | Artefact 5 |
| Ces journaux permettraient-ils de détecter ce type d'exploitation ? | **Non** — et ceux du pare-feu ne portent pas le contenu applicatif | Artefact 5 |

##### Le niveau de qualification

Sur l'échelle du §21.2, la tentation est de retenir le **niveau 2** — exploitation active observée dans le monde, aucun indice chez nous. C'est faux.

La bonne réponse est le **niveau 5** : *journalisation insuffisante pour conclure*. Non parce qu'il y a des indices de compromission, mais parce qu'il est **impossible d'établir qu'il n'y en a pas** sur 98 % de la période d'exposition.

⚠️ **La distinction que ce cas enseigne** : le niveau 5 ne décrit pas la gravité de la menace, il décrit votre **degré de confiance dans votre propre évaluation**. Ce sont deux axes différents, et les confondre conduit à sous-réagir.

---

#### A.5 Corrigé — ce qu'on dit à la direction

L'exercice le plus difficile du cas. Quatre formulations, une seule correcte.

| Formulation | Évaluation |
|---|---|
| « Nous n'avons pas été compromis. » | **Faux.** Invérifiable, et très difficile à corriger si l'investigation dit l'inverse |
| « Nous avons probablement été compromis. » | **Excessif.** Aucun indice ne l'établit ; produit une panique injustifiée |
| « Nous enquêtons. » | **Insuffisant.** N'informe pas du problème réel et retarde une décision |
| « Nous ne pouvons pas établir que nous n'avons pas été compromis, parce que nos journaux ne couvrent que trente jours sur une exposition de quatre ans et demi. » | **Correcte** |

**Pourquoi chaque mot de la quatrième compte** :

- *« Nous ne pouvons pas établir »* — décrit une limite de connaissance, pas un fait sur le monde.
- *« que nous n'avons pas été compromis »* — la double négation est inconfortable et exacte ; la remplacer par « nous avons peut-être été compromis » déplace l'affirmation sur le terrain factuel.
- *« parce que nos journaux ne couvrent que trente jours »* — donne immédiatement la cause, donc l'action corrective.
- *« sur une exposition de quatre ans et demi »* — donne l'ordre de grandeur, qui rend la décision de porter la rétention à douze mois évidente.

**Note de situation — structure attendue**

```
1. Ce qui s'est passé      : vulnérabilité, exploitation active confirmée
2. Ce que nous avons fait  : restriction d'exposition à 10h05, correctif planifié cette nuit
3. Ce que nous savons      : 8443 non publié depuis septembre 2026
4. CE QUE NOUS NE SAVONS PAS : ce qui a pu se produire entre mars 2022 et septembre 2026
5. Ce que nous engageons   : investigation, reconstruction, rétention portée à 12 mois
6. Ce que nous demandons   : validation de l'interruption de service de cette nuit
```

⚠️ La section 4 est celle qu'on supprime sous pression. C'est celle qui a le plus de valeur.

---

#### A.6 Corrigé — le correctif d'urgence

##### Ce qu'on comprime, ce qu'on conserve

| Étape normale | En urgence | Justification |
|---|---|---|
| Délai d'observation (5 j) | **Supprimé** | Le calcul de risque s'inverse : exploitation active confirmée (§18.11) |
| Validation en recette | **Réduite** à un test fonctionnel sur le membre passif | Pas d'environnement de recette pour une appliance |
| Anneaux | **Conservés, compressés** : membre passif → observation 2 h → membre actif | La haute disponibilité fournit l'anneau naturel |
| **Critères d'arrêt** | **Conservés intégralement** | C'est ce qui rend la compression acceptable |
| **Plan de retour arrière** | **Conservé intégralement** | Double partition d'image (§2.7), testée |
| Demande de changement | **Émise a posteriori sous 48 h**, avec le journal | Traçabilité préservée |
| **Preuve** | **Conservée intégralement** | Relevé de version sur les deux membres |

🧪 **Critères go/no-go (D.6) — remplis avant l'intervention**

| Indicateur | Seuil d'arrêt | Mesuré par |
|---|---|---|
| Le membre passif redémarre en `4.2.19` | Tout échec | Console constructeur |
| Synchronisation du couple rétablie sous 10 min | `> 10 min` | Console |
| Sessions actives après bascule | `perte > 20 %` | Supervision |
| Authentifications abouties | `baisse > 10 % sur 15 min` | Journaux d'annuaire |
| Décideur du retour arrière | **M. Ferhaoui**, sans validation supplémentaire | — |

##### La séquence en haute disponibilité

```
1. Sauvegarde de configuration des deux membres, vérifiée
2. Mise à jour du membre PASSIF -> 4.2.19
3. Vérification : version, démarrage, synchronisation
4. Observation 2 h en état passif
5. Bascule du trafic vers le membre à jour
6. Observation 1 h — critères go/no-go
7. Mise à jour de l'ancien membre actif
8. Rebascule, ou maintien selon la configuration
```

⚠️ **Le piège du §2.7** : les deux membres fonctionnent en versions différentes pendant les étapes 2 à 7. Vérifier dans la documentation constructeur que cette configuration est supportée — **avant** l'intervention, pas pendant.

---

#### A.7 Corrigé — corriger ou reconstruire

##### La recherche de compromission préalable

Les cinq axes du §21.7, appliqués aux deux membres :

| Axe | Résultat |
|---|---|
| Comptes | **Deux comptes locaux non documentés** : `svc_mon` et `admin2`. Date de création non déterminable — l'équipement n'horodate pas la création de comptes locaux |
| Configuration | Écart de deux règles par rapport à la configuration de référence de 2025 ; les deux s'expliquent par des changements tracés |
| Persistance | Aucune tâche planifiée inconnue |
| Journaux d'accès | 30 jours : rien d'anormal |
| Trafic sortant | Analyse des journaux de pare-feu sur 12 mois : aucune destination inhabituelle **détectée** — la granularité ne permet pas d'exclure un canal discret |

##### La décision

| Critère | Évaluation |
|---|---|
| Exposition prolongée avérée | **Oui — 4,5 ans** |
| Journalisation permettant de conclure | **Non** |
| Anomalies non explicables | **Oui — 2 comptes locaux** |
| État de confiance démontrable autrement | **Non** |

→ **Reconstruction**, pas correction.

**Pourquoi.** Le correctif ferme la porte ; il ne fait pas sortir celui qui serait entré avant. Sur un équipement de bordure, la persistance est fréquente et difficile à détecter — comptes créés, configuration modifiée, dans certains cas implant au niveau du micrologiciel (§27.2). Les deux comptes non documentés suffisent à basculer la décision, **même sans preuve de malveillance** : c'est le principe du §34.8, on reconstruit quand l'état de confiance ne peut pas être démontré.

**Ordre des opérations** :
1. **Préserver** : export de la configuration, des journaux disponibles, image de l'équipement si le constructeur le permet.
2. Reconstruire à partir de la **configuration de référence**, pas de la configuration courante.
3. Appliquer `4.2.19` sur l'équipement reconstruit.
4. **Rotation de tous les secrets** ayant transité : comptes de service, certificats, secrets d'authentification.
5. Rétablir la surveillance avant remise en service.

⚠️ **Le conflit à arbitrer consciemment** : préserver les preuves ralentit la remise en service. La décision appartient au pilote de cellule, elle est tracée, et elle n'est pas subie par réflexe.

##### Jours 3 à 30

Recherche des mêmes indicateurs sur les actifs joignables depuis la passerelle · rotation complète des secrets · revue des accès distants · surveillance renforcée 90 jours.

**Résultat** : aucune activité malveillante établie. Ce qui **ne prouve rien** sur la période non journalisée — et cette phrase figure telle quelle dans le retour d'expérience.

---

#### A.8 Corrigé — les quatre erreurs volontairement insérées

| # | Erreur | Où | Ce qu'elle produit |
|---|---|---|---|
| 1 | **Journalisation stockée sur l'équipement lui-même, sans export** | Artefact 5 | Un attaquant ayant compromis l'équipement efface les traces. Même sur 30 jours, la preuve n'est pas fiable |
| 2 | **Ouverture « temporaire » sans date de fin** | Artefact 4, ligne 2022-03-14 | 4,5 ans d'exposition. C'est le §11.9 : toute ouverture temporaire porte une date de fermeture dans la demande de changement |
| 3 | **Fermeture de 2026 sans requalification rétrospective** | Artefact 4, ligne 2026-09-22 | L'exposition a été fermée sans que la question « qu'a-t-il pu se passer pendant ces 4 ans ? » ne soit posée. Elle se pose aujourd'hui, dans l'urgence |
| 4 | **Aucune configuration de référence exploitable** | Implicite — la reconstruction s'appuie sur une configuration de 2025 partiellement obsolète | La reconstruction prend 6 h au lieu de 2 h |

**Une cinquième faiblesse, non fautive mais coûteuse** : l'appliance n'est couverte par aucun outil de scan (artefact 2). Le suivi de version repose entièrement sur un relevé manuel. C'est normal pour ce type d'équipement (§27.4), et cela impose un contrôle périodique explicite plutôt qu'une confiance dans l'outillage.

---

#### A.9 Livrables et décisions structurelles

| Livrable | Contenu |
|---|---|
| Journal de crise D.11 | Horodaté, avec sources et décideurs, encadré « état de la connaissance » rempli |
| Demande de changement urgent D.5 | Émise à J+2, avec D.6 et D.7 joints |
| Note à la direction | Six sections, dont « ce que nous ne savons pas » |
| Déclaration à l'assureur | Conservatoire, sous 72 h |
| Retour d'expérience | Les cinq questions du §21.10 |

**Les cinq décisions structurelles issues du retour d'expérience** :

1. **Journalisation** portée à 12 mois sur les actifs de bordure et de niveau 0, **exportée hors de l'équipement**.
2. **Doctrine de version** écrite et datée pour les équipements de bordure, revue trimestriellement (§2.7).
3. **Reconstruction plutôt que correction** après exploitation potentielle sur un équipement de bordure, avec configuration de référence maintenue et testée.
4. **Pré-arbitrage complété** : le seuil d'urgence distingue désormais *restreindre* et *couper*, avec un décideur pour chacun.
5. **Toute ouverture temporaire porte une date de fermeture** dans la demande de changement, avec contrôle automatique à cette date.

---

#### A.10 Critères d'évaluation

| Critère | Pts | Attendu |
|---|---|---|
| Qualification à la source, et des **deux** membres | 10 | Ne pas agir sur l'alerte relayée |
| Distinction `443` / `8443` dans l'analyse d'exposition | 15 | La vulnérabilité porte sur l'administration, pas sur le service |
| Réduction d'exposition **avant** correction | 15 | Restreindre plutôt que couper, avec justification |
| **Question sur la durée d'exposition** | 20 | Le cœur du cas : rapprocher les artefacts 2 et 4 |
| Qualification en niveau 5 | 10 | Confiance dans l'évaluation, pas gravité de la menace |
| Formulation à la direction | 15 | Les quatre nuances du §A.5 |
| Décision de reconstruire, avec critère explicite | 10 | Et préservation des preuves avant action |
| Identification d'au moins 3 des 4 erreurs | 5 | — |

**Seuil de réussite** : 70/100. **Élimination** : annoncer à la direction l'absence de compromission.

---

#### A.11 Variantes

##### Variante 1 — aucun correctif disponible

L'avis constructeur annonce un correctif « sous 10 jours ». Ce qui change :

| Élément | Traitement |
|---|---|
| Réduction d'exposition | **Identique**, et devient la mesure principale |
| Contournement officiel | Appliquer, et **vérifier** qu'il est effectif |
| Compensation | Les sept attributs du §20.7, avec date d'expiration = date du correctif attendu |
| Surveillance | Renforcée sur `8443`, avec destinataire nommé |
| Relance constructeur | Écrite, hebdomadaire, tracée |
| Direction | Informée que l'exposition résiduelle est portée pendant 10 jours, avec compensation |

**Le piège** : traiter les 10 jours comme une attente passive. Ils doivent être un **régime de compensation formalisé**, révocable si l'exploitation s'intensifie.

##### Variante 2 — organisation de 40 personnes, sans SOC ni astreinte

| Ce qui reste faisable | Ce qui ne l'est pas |
|---|---|
| Restreindre l'exposition — 15 min | La recherche de compromission approfondie |
| Vérifier la version à la source | L'analyse des journaux de pare-feu sur 12 mois |
| Appliquer le correctif dans la journée | La surveillance renforcée sur 90 jours |
| **Poser les trois questions du §21.3** | La reconstruction sans configuration de référence |
| **Documenter honnêtement l'incertitude** | — |

**Les deux investissements préalables qui changent réellement l'issue**, et qui sont accessibles à une petite structure :

1. Une **configuration de référence exportée et testée** — trente minutes par an, et elle transforme une reconstruction impossible en opération de deux heures.
2. Un **export des journaux hors de l'équipement**, même vers un simple espace de stockage — quelques euros par mois, et il rend la question du §21.3 traitable.

**Ce que le cas enseigne aux petites structures** : les deux actions les plus rentables — restreindre l'exposition, et écrire ce qu'on ne peut pas savoir — ne coûtent presque rien et ne dépendent d'aucun outil.

---

### Cas de synthèse B — Sortie d'obsolescence sous contrainte et préparation d'un contrôle

> **Format** — Cas de pilotage, à traiter avec un tableur ouvert. Durée estimée : **3 heures**.
> **Livrables attendus** : trois options chiffrées (D.8) · plan de lots · fiche de sanctuarisation (D.4) · note d'arbitrage au comité de direction · préparation d'entretien de contrôle.
> **Prérequis** : chapitres 7, 8, 12, 13, 32, 39.

---

#### B.1 Le dossier initial

**Nous sommes le lundi 5 octobre 2026.** Vous préparez le comité stratégique du 15 octobre.

##### Artefact 1 — état du parc concerné

| Population | Nb | Système | Statut | Contexte |
|---|---|---|---|---|
| Postes bureautiques siège | 340 | Windows 10 22H2 | Hors support depuis le 14/10/2025 | Joints au domaine, gérés par l'infogérant |
| Postes R&D Nantes | 90 | Windows 10 22H2 | Idem | Idem |
| Postes commerciaux nomades | 40 | Windows 10 22H2 | Idem | Idem |
| Postes site industriel (bureautique) | 19 | Windows 10 22H2 | Idem | Idem |
| Postes de supervision industrielle | 11 | Windows 10 IoT LTSB 2016 | **Fin de support le 13/10/2026** | Classe C4, validation constructeur |
| Banc de test PX-40 | 1 | Windows 10 Entreprise LTSB 2016 | **Fin de support le 13/10/2026** | Validation réglementaire des pompes |
| Serveurs | 11 | Windows Server 2016 | **Fin de support le 12/01/2027** | Dont 3 portant des applications métier |

**Total postes hors support : 620** (340 + 90 + 40 + 19 + 11 + 1 arrondi au périmètre géré) · **11 serveurs**.

##### Artefact 2 — courriel de l'infogérant, 12 juin 2026

> *« Concernant votre question sur Windows 10 : l'éditeur a annoncé la prolongation du programme de mises à jour de sécurité étendues jusqu'en octobre 2027. Votre parc est donc couvert et il n'y a pas d'urgence à planifier une migration cette année. Nous restons à votre disposition. »*

##### Artefact 3 — extrait des conditions d'éligibilité du programme grand public

> Le programme de mises à jour de sécurité étendues destiné aux **appareils personnels** est disponible pour les appareils exécutant Windows 10 version 22H2. **Les appareils joints à un domaine Active Directory ou à Microsoft Entra, ainsi que les appareils gérés par une solution de gestion des appareils mobiles, ne sont pas éligibles à ce programme.** Les organisations doivent souscrire au programme commercial.

##### Artefact 4 — compatibilité applicative

| Application | Postes concernés | Validée sur Windows 11 | Remarque |
|---|---|---|---|
| Suite bureautique | 620 | Oui | — |
| Gestion commerciale | 480 | Oui, depuis v9.2 | Migration applicative requise : v9.0 installée |
| Outil de paie | 22 | **Non** | Éditeur : « validation prévue T2 2027 » |
| Chaîne de développement | 90 | Oui | — |
| Suivi de production (lecture) | 19 | Oui | — |
| Conduite de ligne | 11 | **Non — et jamais** | Constructeur : produit en fin de vie |
| Logiciel de banc de test | 1 | **Non** | **Éditeur disparu en 2019** |

##### Artefact 5 — contraintes financières et matérielles

- Budget d'investissement 2026 : **engagé à 94 %**. Reste disponible : 38 k€.
- Vote du budget 2027 : **mars 2027**.
- Parc matériel : 210 postes de plus de 5 ans, **incompatibles** avec le nouveau système sans remplacement.
- Coût unitaire de remplacement d'un poste : ordre de grandeur `[à renseigner selon votre contexte]`.
- Coût du support étendu commercial : facturation **par poste et par an**, avec un tarif **croissant chaque année** — le principe est stable, les montants doivent être obtenus par devis.

##### Artefact 6 — contexte de contrôle

- Un client hospitalier majeur annonce un **audit de sécurité fournisseur au premier trimestre 2027**, portant sur la chaîne HelioLink.
- La police d'assurance est en renouvellement en février 2027.
- Le référentiel applicable comporte un objectif explicite sur la maîtrise de l'obsolescence.

---

#### B.2 Les questions à traiter

| # | Question | Livrable |
|---|---|---|
| 1 | L'affirmation de l'infogérant est-elle exacte ? Comment le vérifiez-vous ? | — |
| 2 | Construisez les trois options chiffrées. | D.8 |
| 3 | Proposez un plan de lots avec dépendances. | Tableau de lots |
| 4 | Traitez les 11 postes de supervision et le banc de test. | D.4 |
| 5 | Rédigez la note d'arbitrage au comité de direction. | Note 1 page |
| 6 | Préparez l'entretien de contrôle : six questions et vos réponses. | Grille |
| 7 | Que faites-vous du courriel du 12 juin ? | — |

---

#### B.3 Corrigé — la vérification qui renverse la situation

**L'affirmation de l'infogérant est inexacte**, et la vérification prend quinze minutes : lire les conditions d'éligibilité du programme invoqué (artefact 3).

| Programme | Public | Éligibilité du parc HELIOMED |
|---|---|---|
| Support étendu **grand public** | Appareils **personnels** | **Non éligible** — parc joint au domaine et géré |
| Support étendu **commercial** | Organisations | Éligible, **payant**, tarif croissant |

**Conséquence** : les 620 postes n'ont **jamais** été couverts et ne reçoivent plus de correctifs de sécurité depuis le **14 octobre 2025**, soit près de **douze mois** au moment du constat.

⚠️ **La leçon du §12.1, piège n° 1** : une option de support ne se budgète jamais avant d'avoir vérifié, **actif par actif**, son périmètre d'éligibilité. Ici, la vérification n'avait pas été faite parce que l'information venait d'un tiers de confiance — ce qui ne dispense de rien.

**Ce que la découverte change** : le sujet cesse d'être un arbitrage de calendrier pour devenir un sujet de **responsabilité contractuelle** et de **documentation d'un écart de douze mois**.

---

#### B.4 Corrigé — les trois options chiffrées

> Les montants ci-dessous sont exprimés en **structure de coût**, non en valeurs absolues : les tarifs de support étendu et de matériel se négocient et se périment. La méthode est ce qui compte.

##### Fiche D.8 remplie

| Champ | Contenu |
|---|---|
| Population | 620 postes + 11 serveurs |
| Composant | Système d'exploitation |
| Date de fin de support | 14/10/2025 (postes) · 13/10/2026 (LTSB) · 12/01/2027 (serveurs) |
| Source et vérification | Pages officielles de cycle de vie, consultées le 05/10/2026 |
| Criticité / exposition | C2-C3 pour les postes · C1 pour 3 serveurs |
| **Éligibilité au support étendu** | ☑ **Vérifiée actif par actif** — programme grand public **non applicable** |

##### Comparaison des options

| | **Option 1 — support étendu 2 ans** | **Option 2 — migration en 3 lots** | **Option 3 — statu quo** |
|---|---|---|---|
| **Coûts directs** | 620 postes × tarif an 1 + 620 × tarif an 2 (**croissant**) | 210 postes à remplacer + migration applicative gestion commerciale + charge projet | 0 |
| **Coûts indirects** | Coût de la migration, **qui reste dû** après les 2 ans | Tests, formation, support renforcé pendant 9 mois | Compensations · surveillance · urgences · astreinte |
| **Couverture** | Correctifs **critiques uniquement**, selon les critères de l'éditeur | Complète et durable | **Nulle** |
| **Risque résiduel** | Vulnérabilités non critiques non corrigées | Élevé pendant la transition, nul ensuite | 620 postes sans correctif |
| **Position en contrôle** | Défendable si daté et borné | Excellente | **Intenable** |
| **Position en assurance** | Acceptable avec plan | Excellente | Risque de refus de garantie |
| **Faisabilité** | Immédiate | 9 mois | Immédiate |

⚠️ **L'option 3 doit figurer au tableau, chiffrée.** Son absence est la première cause de non-décision (§12.6). Ici, elle est **techniquement disponible mais contractuellement indisponible** : l'audit client de T1 2027 et le renouvellement d'assurance de février la rendent inacceptable. Ce point s'écrit, il ne se sous-entend pas.

##### Décision recommandée

**Option 2, avec un pont ciblé** :

- Migration en trois lots sur neuf mois.
- Support étendu commercial limité à **140 postes** — ceux portant l'outil de paie (22) et une partie de la gestion commerciale en attente de validation (118).
- Le pont est **daté, borné et chiffré** : il se termine au T4 2027, à la migration du lot 3.

**Ce qui rend cette option supérieure** : sur deux ans, l'option 1 représente une fraction significative du coût de la migration **sans produire aucun bénéfice durable** — et la migration reste à financer ensuite. L'arbitrage se fait en quinze minutes une fois le tableau posé.

---

#### B.5 Corrigé — le plan de lots

| Lot | Périmètre | Nb | Échéance | Prérequis | Dépendances |
|---|---|---|---|---|---|
| **0 — Pilote** | 15 postes, 4 profils représentés | 15 | Nov. 2026 | Aucun | Valide le processus et produit le chiffrage réel |
| **1** | Postes bureautiques standards, matériel compatible | 200 | T1 2027 | Lot 0 concluant | Aucune |
| **2** | Postes avec gestion commerciale, matériel compatible | 265 | T2 2027 | **Migration applicative v9.0 → v9.2** | Bloquant : à lancer **immédiatement** |
| **3** | Postes à remplacer + paie | 140 | T4 2027 | Budget 2027 voté · **validation éditeur paie (T2 2027)** | Sous pont de support étendu |
| **Hors lots** | 11 supervision + 1 banc de test | 12 | — | — | Voir §B.6 |

##### Le séquencement, et pourquoi il ne suit pas les dates

La date de fin de support est **identique** pour les 620 postes. Le critère du §12.3 s'applique : **criticité × exposition × effort**.

- Le **lot 0** part en premier pour produire un chiffrage réel — c'est le levier n° 4 du §12.7 contre le report perpétuel : l'argument « c'est trop risqué » ne résiste pas à une migration déjà réalisée en interne.
- Le **lot 1** regroupe le plus simple : matériel compatible, aucune dépendance applicative. Il fait chuter le volume rapidement.
- Le **lot 2** est conditionné par une migration applicative de neuf semaines. **Elle doit être lancée dès octobre 2026** — le §26.10 rappelle que la négociation avec un éditeur métier doit démarrer six mois avant l'échéance.
- Le **lot 3** dépend d'un budget non voté et d'une validation éditeur non acquise : c'est lui qui porte le pont.

⚠️ **L'erreur de séquencement à éviter** : commencer par les cas difficiles « parce qu'ils sont les plus risqués ». Le lot 3 en premier bloquerait le programme sur une dépendance externe pendant six mois, sans qu'aucun poste ne soit migré.

---

#### B.6 Corrigé — les deux systèmes contraints

##### Cas 1 — les 11 postes de supervision

| Élément | Décision |
|---|---|
| Décision structurante (§32.1) | **Remplacer** — mais à l'échelle du système de conduite, pas du poste |
| Contrainte | Le constructeur a placé le produit en fin de vie ; aucune version compatible n'existera |
| Horizon | Renouvellement du système de conduite : projet industriel pluriannuel, hors périmètre DSI |
| **Traitement intérimaire** | **Isoler** : régime C4, réseau industriel séparé, compensation selon §20.2, fenêtre lors des arrêts de production |
| Dérogation | Signée par le directeur industriel, revue semestrielle |
| Provision | Inscrite au plan pluriannuel industriel |

##### Cas 2 — le banc de test PX-40 (fiche D.4)

| Champ | Contenu |
|---|---|
| Objet | `BANC-PX40-01` · système hors support au 13/10/2026 · logiciel de pilotage sans version récente |
| Type d'impossibilité | ☑ **Technique** — éditeur disparu en 2019, aucun correctif ne viendra jamais |
| Analyse de risque en termes métier | Le banc valide la conformité réglementaire des pompes PX-40. Sa compromission pourrait altérer des résultats de validation, avec des conséquences sur la conformité des dispositifs mis sur le marché et sur la sécurité des patients. Le poste ne contient pas de données à caractère personnel. |
| Exposition avant compensation | Réseau industriel, joignable depuis 11 postes de supervision |
| **Décision structurante** | **ISOLER** — remplacer le banc complet représente ~300 k€ et 18 mois, requalification comprise |
| Compensations | **1.** Retrait de tout réseau (rang 1, §20.2). **2.** Transferts par support dédié, chaîne du §29.5. **3.** Deux comptes nominatifs, journal papier des interventions. **4.** Contrôle trimestriel de l'absence de connexion. |
| Moyen de vérification | Contrôle physique trimestriel : absence de câble, absence d'interface sans fil active, relevé du journal papier |
| Coût de la solution | ~14 k€ — matériel réseau et deux jours d'ingénierie |
| Signataire | **Directeur général** — la grille C.4 impose ce niveau : impact potentiel sur la conformité de dispositifs médicaux |
| Date d'expiration | 31/12/2028, alignée sur la revue du plan pluriannuel |
| Conditions de révocation anticipée | Panne matérielle du poste · évolution de l'exigence réglementaire de validation · disponibilité d'une solution de remplacement qualifiée |
| Provision | Remplacement du banc inscrit au plan pluriannuel, horizon 2031 |

**Le point à retenir** : deux systèmes également non corrigeables, deux décisions différentes. Ce qui les distingue n'est pas technique — c'est le **rapport entre le coût du remplacement et la valeur de l'usage**, et la disponibilité d'une trajectoire.

---

#### B.7 Corrigé — la note d'arbitrage au comité de direction

> **Note — Sortie d'obsolescence du parc bureautique — 8 octobre 2026 — 1 page**
>
> **1. Situation.** 620 postes de travail ne reçoivent plus de correctifs de sécurité depuis le 14 octobre 2025. Le programme de prolongation évoqué en juin ne s'applique pas aux parcs professionnels gérés : la vérification des conditions d'éligibilité, réalisée le 5 octobre, l'établit sans ambiguïté. L'écart porte donc sur douze mois.
>
> **2. Ce que cela signifie.** Toute vulnérabilité publiée depuis un an sur ce système reste non corrigée sur l'ensemble du parc bureautique. Deux échéances externes rendent cette situation intenable : un audit de sécurité d'un client hospitalier au premier trimestre 2027, et le renouvellement de la police d'assurance en février.
>
> **3. Trois options.** *(tableau du §B.4)*
>
> **4. Recommandation.** Migration en trois lots sur neuf mois, avec un pont de support étendu commercial limité à 140 postes, daté et borné au quatrième trimestre 2027. Sur deux ans, l'option de support étendu seule représente une part significative du coût de la migration sans en produire aucun bénéfice durable, et la migration resterait à financer.
>
> **5. Ce que nous demandons.** L'inscription au budget 2027 du remplacement de 210 postes et du pont de support étendu · le lancement immédiat de la migration applicative de la gestion commerciale, prérequis bloquant du lot 2 · la signature de la dérogation relative au banc de test de validation.
>
> **6. Ce qui reste non résolu.** La validation de l'outil de paie par son éditeur est annoncée pour le deuxième trimestre 2027 sans engagement contractuel. En cas de retard, 22 postes resteront sous pont au-delà du quatrième trimestre 2027. Ce risque est identifié, il n'est pas maîtrisé par nous.

⚠️ **La section 6 est celle qui fait la différence.** Une note qui ne présente que des problèmes résolus n'est pas crédible. Celle-ci nomme ce qui échappe à l'organisation, et elle le nomme **avant** que cela ne se produise.

---

#### B.8 Corrigé — l'entretien de contrôle

| Question du contrôleur | Réponse attendue | Pièce du dossier |
|---|---|---|
| « Combien d'actifs sont hors support ? » | Le chiffre, **avec son dénominateur** et la répartition par population : 620 postes sur 941 actifs du périmètre, 11 serveurs sur 187 | Périmètre daté (D.13, pièce 1) |
| « Depuis quand ? » | 14/10/2025 pour les postes. **Et la cause** : une information d'éligibilité inexacte reçue d'un tiers, non vérifiée à la source jusqu'au 05/10/2026 | Note interne datée |
| « Qu'avez-vous décidé ? » | Les trois options chiffrées, l'option retenue, le décideur, la date de décision | D.8 + note d'arbitrage |
| « Qu'est-ce qui n'est pas couvert ? » | L'annexe des périmètres non couverts, tenue depuis 2026 : banc de test, postes de supervision, avec compensations et échéances | Annexe de D.1 |
| « Comment le prouvez-vous ? » | Périmètre daté, journaux de campagne par lot, échantillon de preuve d'état sur chaque lot | D.13, pièces 1, 5, 6 |
| « Et si le lot 3 glisse ? » | Le risque est identifié dans la note du 08/10/2026, section 6. Le pont de support étendu est prolongeable, avec son coût connu | Note d'arbitrage |

##### Ce qui fait la différence dans cet entretien

L'organisation **ne prétend pas être conforme**. Elle démontre trois choses :

1. Elle **connaît** ses écarts, et les chiffre avec leur dénominateur.
2. Elle les a **décidés au bon niveau**, avec une trace datée.
3. Elle en **suit** l'évolution, avec des échéances et un financement.

C'est exactement le §39.1. Un dossier qui prétendrait à 100 % de conformité sur ce parc serait immédiatement suspect.

##### Barème d'évaluation de l'entretien

| Critère | Pts |
|---|---|
| Chiffres donnés avec dénominateur et population | 20 |
| Cause de l'écart assumée, sans dissimulation ni mise en cause | 15 |
| Trois options présentées, dont le statu quo | 20 |
| Périmètres non couverts présentés spontanément | 20 |
| Preuves produites, datées, avec périmètre | 15 |
| Risque non maîtrisé nommé avant d'être découvert | 10 |

**Élimination** : présenter le taux de conformité de la console de l'infogérant sans mentionner les 620 postes.

---

#### B.9 Corrigé — le courriel du 12 juin

Trois usages, dans cet ordre.

1. **Contractuel.** L'information transmise était inexacte et a fondé une décision de report. Le sujet n'est plus « qui devait patcher » — le contrat ne comportait aucun engagement de délai — mais « quelle information avons-nous reçue ». C'est ce déplacement qui rend la renégociation possible (§13.9).
2. **Documentaire.** Le courriel devient une pièce du dossier de preuves : il établit la cause de l'écart de douze mois, ce qui est très différent d'une négligence non expliquée (§39.1).
3. **Préventif.** Il justifie l'ajout au contrat d'une clause de restitution de données et d'une clause d'escalade des impossibilités (D.9, clauses 3 et 8). Sans donnée restituée, l'organisation ne pouvait pas détecter elle-même que le parc n'était pas couvert.

⚠️ **Ce qu'il ne faut pas en faire** : un instrument de mise en cause personnelle. L'objectif est d'obtenir des clauses, pas d'avoir raison.

---

#### B.10 Bilan à douze mois et ce qui n'a pas fonctionné

| Indicateur | Oct. 2026 | Oct. 2027 |
|---|---|---|
| Postes hors support | 620 | **140** (sous pont daté) |
| Serveurs hors support | 11 | **2** |
| Ratio confirmé conforme, parc bureautique | 34 % | **89 %** |
| Contrôle client T1 2027 | — | Passé, deux observations mineures |
| Surprime d'assurance | 34 % | Renégociée |

**Ce qui n'a pas fonctionné**, et qui doit figurer au retour d'expérience :

1. **Le lot 2 a glissé de six semaines.** La migration applicative de la gestion commerciale a démarré en novembre au lieu d'octobre : la commande a attendu une validation d'achat non anticipée. Le §26.10 aurait dû être appliqué six mois plus tôt.
2. **Deux postes du lot 1 ont dû être repris.** Du matériel incompatible n'avait pas été détecté à l'inventaire — les caractéristiques matérielles ne figuraient pas dans les attributs suivis (Annexe I.1).
3. **Le pont a coûté plus que prévu.** Le tarif de la deuxième année n'avait pas été intégré au chiffrage initial, alors que le §12.1 le signale explicitement.

---

### Cas de synthèse C — Le correctif urgent qui casse la production

> **Format** — Cas d'arbitrage, à traiter en deux temps : la décision *avant*, puis l'analyse *après*. Durée estimée : **2 h 30**.
> **Livrables attendus** : instruction des deux risques · demande de changement (D.5) · critères go/no-go (D.6) · plan de retour arrière (D.7) · chronologie · compte rendu d'incident · plan d'amélioration.
> **Prérequis** : chapitres 6, 16, 18, 20, 26.

---

#### C.1 Le dossier initial

**Nous sommes le vendredi 12 novembre 2027, 14 h 00.**

##### Artefact 1 — l'avis reçu

> **Avis de sécurité éditeur — moteur de base de données — 12/11/2027 08:00 UTC**
>
> Une vulnérabilité affectant le traitement des connexions authentifiées permet à un utilisateur disposant de droits limités d'exécuter du code avec les privilèges du service.
> Gravité : **élevée**. Exploitation observée : **aucune à ce jour**.
> Versions affectées : `15.x` antérieures à `15.4.2`.
> Correctif : `15.4.2`, publié le 12/11/2027 à 06:00 UTC.
>
> *Notes de version — extrait, page 4, section « Modifications internes » :*
> *« Le format de journal de réplication passe en version 3. Les instances en version 3 ne peuvent pas répliquer vers des instances en version 2. Une mise à jour simultanée de tous les membres d'un groupe de réplication est requise. »*

##### Artefact 2 — le cluster concerné

```yaml
id_actif: CLU-HELIOLINK-BDD
type: base_de_donnees
role: stockage principal de la plateforme de télésuivi HelioLink
version: "15.3.1"
topologie: 3 nœuds — 1 primaire, 2 réplicas synchrones
criticite: C1
exposition: administration        # non publié sur Internet
joignable_depuis: serveurs applicatifs HelioLink (eux-mêmes exposés)
fenetre_maintenance: "samedi 22h-02h"
proprietaire_metier: y.prigent
proprietaire_technique: m.ferhaoui
utilisateurs_finaux: 34 établissements de santé, ~4 200 patients suivis
```

##### Artefact 3 — l'environnement de recette

```yaml
id_actif: REC-HELIOLINK-BDD
version: "15.3.1"
topologie: 1 nœud unique — PAS de réplication
volumetrie: 2 % de la production
integrations: 3 sur 7 simulées
configuration: dérive non mesurée depuis 2026
derniere_synchronisation_donnees: 2027-04-15
```

##### Artefact 4 — la politique applicable

| Classe | Délai — critique non exploitée |
|---|---|
| **C1** | **15 jours** |

##### Artefact 5 — la proposition de l'équipe

> *Courriel de M. Ferhaoui, 12/11/2027 14 h 12 :*
> « Vulnérabilité élevée sur le cluster HelioLink, correctif dispo. Je propose de l'appliquer demain soir dans la fenêtre habituelle, pour ne pas laisser traîner. C'est une version mineure, ça devrait bien se passer. »

##### Artefact 6 — antécédents

- Le correctif a été publié il y a **6 heures**. Aucun retour communautaire n'est encore disponible.
- Le dernier retour arrière testé sur ce cluster date de **mars 2026**, sur un nœud isolé.
- La plateforme HelioLink dispose de deux indicateurs fonctionnels : *remontées de télésuivi abouties par minute* et *sessions établissement actives*.

---

#### C.2 Les questions à traiter

| # | Question | Livrable |
|---|---|---|
| 1 | Instruisez les deux risques **en parallèle**. | Tableau à deux colonnes |
| 2 | Quelle décision prenez-vous le vendredi 12 à 17 h ? | Décision tracée |
| 3 | Le scénario applique le correctif le samedi. Reconstituez ce qui se passe. | Chronologie |
| 4 | Identifiez les causes racines, et ce qui a bien fonctionné. | Compte rendu |
| 5 | Rédigez le plan d'amélioration. | Plan daté |
| 6 | Distinguez erreur humaine, erreur de conception, erreur de processus. | Analyse |

---

#### C.3 Corrigé — instruire les deux risques en parallèle

C'est la méthode centrale du cas. On n'instruit pas « faut-il corriger ? », mais **deux questions symétriques**, dans deux colonnes, avec les mêmes exigences de preuve.

| **Risque de NE PAS corriger** | **Risque de corriger maintenant** |
|---|---|
| Exploitation observée ? **Non** (artefact 1) | Correctif publié depuis **6 h** — retours communautaires ? **Aucun** |
| Exposition directe ? **Non** — cluster non publié | Recette représentative ? **Non** : 1 nœud contre 3, **pas de réplication** |
| Exposition indirecte ? **Oui** — via les serveurs applicatifs exposés | Volumétrie de recette : **2 %** de la production |
| Privilèges requis ? **Compte authentifié à droits limités** | Intégrations : **3 sur 7 simulées** |
| Actif critique ? **Oui** — C1, données de santé, 34 établissements | Retour arrière testé sur cette topologie ? **Non** — dernier test en 2026, sur un nœud isolé |
| Délai politique disponible ? **15 jours** | Notes de version lues intégralement ? **À faire** |
| Que se passe-t-il si on attend 10 jours ? Risque marginal supplémentaire **faible** | Que se passe-t-il si ça casse ? **Indisponibilité d'un service de télésuivi médical** |

##### La lecture

Le déséquilibre est net. La colonne de gauche ne présente **aucune urgence caractérisée** : pas d'exploitation, pas d'exposition directe, privilèges préalables requis. La colonne de droite présente **quatre inconnues et une lacune avérée** — la recette ne représente pas la production sur la dimension exacte que le correctif touche.

**La décision correcte est d'utiliser le délai disponible.**

⚠️ **Le biais à nommer explicitement.** L'artefact 5 dit *« pour ne pas laisser traîner »*. C'est une préférence psychologique, pas une analyse de risque. Elle est l'erreur symétrique du report perpétuel du §12.7 — et elle est bien moins souvent dénoncée, parce qu'elle a l'apparence de la diligence.

**La formulation à retenir** : *un délai accordé par la politique est une ressource, pas un retard. Il existe précisément pour permettre de tester. L'utiliser n'est pas de la négligence.*

##### Ce qui aurait renversé la décision

Il est important de savoir ce qui aurait justifié d'agir samedi :

| Élément | Effet |
|---|---|
| Exploitation observée dans le monde | Bascule vers la feuille « traiter » à 7 jours |
| Exploitation observée dans le secteur santé | Bascule vers l'urgence |
| Cluster directement exposé | Bascule vers l'urgence |
| Recette représentative disponible | Le risque de changement chute — samedi devient raisonnable |

---

#### C.4 Corrigé — la lecture des notes de version

L'information décisive est à la **page 4, section « Modifications internes »** de l'artefact 1 :

> *« Le format de journal de réplication passe en version 3. Les instances en version 3 ne peuvent pas répliquer vers des instances en version 2. »*

**Ce que cela signifie concrètement** : la mise à jour nœud par nœud — la méthode standard sur un cluster — **est impossible** sur ce correctif. Elle produit un cluster dont les membres ne peuvent plus se synchroniser.

C'est exactement la question n° 2 de la qualification en six questions du §18.2 : *quels prérequis exige-t-il ?* La réponse était disponible dès 8 h du matin, dans un document de quatre pages.

⚠️ **Pourquoi cette ligne se rate.** Elle ne figure ni dans le résumé, ni dans la section sécurité, ni dans les correctifs listés : elle est dans une rubrique « modifications internes » que rien ne signale comme critique. C'est le cas général — **la qualification consiste à lire les notes de version en entier, pas à les parcourir**.

---

#### C.5 Corrigé — la chronologie du samedi

Le scénario applique le correctif malgré tout. Voici ce qui se produit.

| Heure | Événement | Ce qui manquait |
|---|---|---|
| 22:00 | Début de la fenêtre. Instantanés des trois machines virtuelles pris | — |
| 22:40 | Nœud réplica 2 mis à jour en `15.4.2`, redémarre normalement | — |
| **22:55** | **La réplication ne repart pas.** Le nœud en v3 refuse de se synchroniser depuis le primaire en v2 | La ligne de la page 4 |
| 23:00 | Diagnostic : recherche dans les journaux, puis dans les notes de version | Qualification préalable |
| **23:10** | **Décision de retour arrière — après 15 minutes de discussion** | Critères d'arrêt écrits, décideur nommé |
| 23:25 | Instantané restauré sur le réplica 2. Le nœud revient en `15.3.1` | — |
| **23:30** | **La réplication ne repart toujours pas** : le nœud restauré accuse 40 minutes de retard de transactions, au-delà du seuil de rattrapage automatique | Test du retour arrière sur topologie représentative |
| 23:45 | Décision : resynchronisation complète du réplica depuis le primaire | — |
| 00:10 | Resynchronisation en cours. Le cluster fonctionne en mode dégradé — un seul réplica | — |
| 01:20 | Resynchronisation terminée, cluster nominal, service rétabli | — |

**Bilan** : **4 heures d'indisponibilité partielle** de la plateforme de télésuivi, un dimanche matin. **Aucune donnée perdue.** Deux établissements clients ont appelé le support.

##### Ce qui aurait pu être pire

Le scénario s'arrête au réplica. Si la séquence avait commencé par le **primaire**, l'indisponibilité aurait été **totale**, et le retour arrière aurait exigé une restauration de sauvegarde avec perte des transactions depuis l'instantané — c'est-à-dire des données de télésuivi de 34 établissements.

**Le choix de commencer par un réplica est la seule décision de la nuit qui relève de la bonne pratique.** Elle mérite d'être nommée dans le retour d'expérience.

---

#### C.6 Corrigé — causes racines et ce qui a fonctionné

##### Les quatre causes racines

| # | Cause | Ce qui l'aurait évitée | Coût de la prévention |
|---|---|---|---|
| 1 | **Notes de version parcourues, pas lues** | Qualification en six questions du §18.2, avec référence de la section consultée | 20 minutes |
| 2 | **Recette non représentative sur la dimension touchée** | Mesure de l'écart sur les quatre axes du §6.12, **déclarée dans la demande de changement** | 1 h, puis constat bloquant |
| 3 | **Retour arrière testé sur une topologie non représentative** | Test sur cluster, chronométré (§18.8) | 1/2 journée, une fois |
| 4 | **Aucun critère d'arrêt écrit, aucun décideur nommé** | Formulaire D.6 rempli avant l'intervention | 15 minutes |

**La cause 2 est la cause dominante.** Les causes 1, 3 et 4 aggravent, mais c'est l'écart de recette qui rend l'incident inévitable : aucun test sur un nœud unique ne pouvait révéler un problème de réplication.

##### Ce qui a bien fonctionné — à nommer explicitement

| Élément | Pourquoi c'est important |
|---|---|
| La fenêtre était correcte | Samedi soir, usage minimal |
| L'astreinte était présente | Deux personnes, jusqu'à 1 h 20 |
| Les instantanés existaient et étaient récents | Sans eux, restauration de sauvegarde |
| **La séquence a commencé par un réplica** | A évité une indisponibilité totale |
| Aucune donnée n'a été perdue | Le pire scénario a été évité |
| La resynchronisation a fonctionné | Le mécanisme de secours était opérationnel |

⚠️ **Un retour d'expérience qui ne liste que les défaillances produit deux effets pervers** : il décourage l'équipe, et il fait disparaître les pratiques à préserver. La prochaine campagne pourrait « optimiser » en commençant par le primaire.

---

#### C.7 Corrigé — ce qu'il aurait fallu faire

| Moment | Action | Livrable |
|---|---|---|
| **Ven. 14:00** | Qualification en six questions. **Lire les notes de version en entier** | Fiche de qualification |
| Ven. 15:30 | Constat : mise à jour simultanée requise, pas de mise à jour nœud par nœud | — |
| Ven. 16:00 | Mesure de l'écart recette/production sur les quatre axes. Constat : **bloquant** | Section de D.5 |
| **Ven. 17:00** | **Décision : utiliser le délai de 15 jours.** Tracée, avec justification | Décision datée |
| Ven. 17:15 | Compensation dans l'intervalle : restreindre l'accès au cluster aux seuls serveurs applicatifs · surveillance des connexions authentifiées inhabituelles · destinataire nommé | Fiche §20.7 |
| Sem. 1 | Monter un cluster de recette à **3 nœuds** avec réplication | Environnement |
| Sem. 1 | Tester le correctif **et le retour arrière** sur cette topologie. Chronométrer | D.7 rempli |
| Sem. 2 | Écrire les critères go/no-go, avec les deux indicateurs fonctionnels | D.6 rempli |
| **Sam. sem. 2** | Déploiement en fenêtre, séquence validée par le test | Chronologie |
| Après | Écart de recette inscrit au plan d'amélioration | Plan daté |

##### Les livrables remplis

**D.6 — critères go/no-go**

| Indicateur | Seuil d'arrêt | Mesuré par |
|---|---|---|
| Réplication rétablie après mise à jour d'un nœud | `> 5 min` | Console du moteur |
| **Remontées de télésuivi abouties/min** | `baisse > 10 % sur 15 min` | Supervision applicative |
| **Sessions établissement actives** | `baisse > 5 %` | Supervision applicative |
| Erreurs applicatives | `> 20/min` | Journaux |
| **Décideur du retour arrière** | **M. Ferhaoui**, sans validation supplémentaire | — |

**D.7 — plan de retour arrière**

| Champ | Contenu |
|---|---|
| Mécanisme | Instantané des trois machines virtuelles + resynchronisation depuis le primaire |
| **Testé le** | `[date]` — sur cluster 3 nœuds représentatif |
| **Durée mesurée** | `[hh:mm]` — chronométrée lors du test |
| Périmètre couvert | Binaires, configuration, **format de réplication** |
| **Point de non-retour** | **Mise à jour du primaire** : au-delà, tout retour arrière exige une restauration de sauvegarde |
| Ce que le retour arrière ne restaure pas | Transactions depuis l'instantané · état des connexions établissement |

---

#### C.8 Corrigé — erreur humaine, de conception, de processus

C'est la question la plus importante du cas, et la plus mal traitée en pratique.

| Type | Ce qui s'est passé | Le bon niveau de traitement |
|---|---|---|
| **Erreur humaine** | Malik Ferhaoui n'a pas lu la page 4 des notes de version | Aucune sanction n'est appropriée : il a suivi une procédure qui ne l'exigeait pas |
| **Erreur de conception** | L'environnement de recette ne reproduit pas la topologie de production | Décision d'investissement — c'est le §6.12 et le §6.13 |
| **Erreur de processus** | La qualification n'était pas un champ obligatoire · les critères d'arrêt n'étaient pas exigés · le retour arrière n'avait pas à être testé sur topologie représentative | **C'est ici que se corrige l'incident** |

##### Le principe à retenir

> Un retour d'expérience porte sur le **processus**, jamais sur les personnes. Quand une personne compétente, appliquant la procédure existante, produit un incident, le défaut est dans la procédure.

**Le test qui tranche** : *une autre personne, à la place de Malik, aurait-elle fait autrement ?* Ici, non — rien dans le processus ne l'y obligeait. Le défaut est donc structurel.

⚠️ **Le contre-exemple**, pour ne pas tomber dans l'excès inverse : si la procédure avait exigé la qualification en six questions et qu'elle avait été délibérément contournée pour gagner du temps, ce serait une erreur d'application — qui appelle un traitement différent, mais toujours pas une sanction en première intention : la question devient *pourquoi la procédure a-t-elle paru contournable ?*

---

#### C.9 Le plan d'amélioration

| # | Action | Prio | Échéance | Propriétaire |
|---|---|---|---|---|
| 1 | Qualification en six questions rendue **champ obligatoire** du dossier de campagne C1, avec référence de la section des notes de version consultée | **P0** | Immédiat | RSSI |
| 2 | Critères d'arrêt et décideur du retour arrière écrits **avant** toute intervention C1 (D.6) | **P0** | Immédiat | Exploitation |
| 3 | **Écart recette/production mesuré sur les quatre axes** et déclaré dans chaque demande de changement | **P0** | 1 mois | Exploitation |
| 4 | Cluster de recette à 3 nœuds pour HelioLink | P1 | T1 2028 | DSI — budget |
| 5 | Retour arrière testé sur topologie représentative, **chronométré**, une fois par an et après tout changement d'architecture | P1 | T1 2028 | Exploitation |
| 6 | Point de non-retour identifié et écrit dans toute demande de changement touchant un composant à état | P1 | 1 mois | Exploitation |
| 7 | Les deux indicateurs fonctionnels HelioLink intégrés aux critères d'arrêt par défaut | P2 | T1 2028 | Produit |

---

#### C.10 Critères d'évaluation

| Critère | Pts | Attendu |
|---|---|---|
| Instruction des **deux** risques en colonnes symétriques | 20 | Ne pas se contenter d'évaluer la vulnérabilité |
| Détection de la ligne des notes de version | 15 | Lire l'artefact 1 en entier |
| Décision d'utiliser le délai, **avec justification écrite** | 20 | Le cœur du cas |
| Compensation posée pendant l'attente | 10 | Attendre n'est pas ne rien faire |
| Identification de l'écart de recette comme cause dominante | 15 | Distinguer cause dominante et facteurs aggravants |
| Ce qui a bien fonctionné, nommé | 10 | Notamment le choix de commencer par un réplica |
| Distinction des trois types d'erreur | 10 | Le défaut est dans la procédure |

**Seuil de réussite** : 70/100. **Élimination** : conclure que l'incident résulte d'une faute individuelle.

---

#### C.11 Variante — la même situation avec exploitation active

Mêmes artefacts, sauf l'artefact 1 : *« exploitation active observée dans le secteur de la santé »*.

**Ce qui change, et ce qui ne change pas** :

| Élément | Sans exploitation | Avec exploitation active |
|---|---|---|
| Décision | Utiliser les 15 jours | **Agir sous 72 h** |
| Lecture des notes de version | Obligatoire | **Toujours obligatoire** — c'est ce qui prend 20 minutes et évite l'incident |
| Écart de recette | Motif de report | **Motif de prudence accrue**, pas de report |
| Séquence | Testée d'abord | Réplica d'abord, observation courte, primaire ensuite |
| Critères d'arrêt | Écrits | **Toujours écrits** — leur suppression n'est jamais un gain de temps |
| Compensation | Pendant l'attente | **Pendant l'intervention** : restriction d'accès maintenue jusqu'à vérification |
| Retour arrière | Testé avant | **Non testable faute de temps** — le déclarer explicitement comme risque assumé, et le dire à la direction |

**Le point que cette variante enseigne** : l'urgence comprime le délai d'observation et la validation, **jamais la qualification, les critères d'arrêt ni la preuve** (§21.8). Ces trois éléments coûtent moins d'une heure au total, et ce sont eux qui permettent de se tromper sans catastrophe.

---

## ANNEXES

### Plan d'accès — trouver la bonne annexe en dix secondes

| J'ai besoin de… | Annexe |
|---|---|
| Comprendre un terme ou un acronyme | **A** — glossaire |
| Savoir quoi vérifier sur une plateforme donnée | **B** — cheat sheets |
| Prioriser un constat, ou fixer un délai | **C** — matrices et arbre de décision |
| Un formulaire à remplir : politique, dérogation, changement, PV | **D** — 14 templates |
| Choisir une famille d'outil, ou comprendre un modèle de licence | **E** — outils *(versionnée)* |
| Savoir ce qu'un texte exige et quelle preuve il attend | **F** — réglementaire *(versionnée)* |
| Vérifier si je suis en train de tomber dans un piège connu | **G** — 53 pièges classés |
| Retrouver une échéance, une source de veille, une formation | **H** — calendrier et ressources *(versionnée)* |
| Concevoir ou corriger un inventaire | **I** — modèle de données |
| Définir un cycle de vie de constat, des états, des escalades | **J** — workflow de remédiation |
| Définir un indicateur, ou m'auto-évaluer | **K** — KPI et maturité |
| Une liste à cocher avant une action | **L** — 9 checklists |
| Vérifier d'où vient une affirmation datée du cours | **M** — registre de sources *(versionnée)* |

**Cours ou documentation ?** Les annexes A, C, G et K servent à **apprendre** et se lisent. Les annexes B, D, I, J et L servent à **consulter** et se remplissent. Les annexes E, F, H et M servent à **vérifier** et se périment — ce sont elles qui portent la maintenance du document.

---

Les annexes de ce cours sont conçues comme une **boîte à outils active**, utilisable sans relire les chapitres. Quatre d'entre elles — E, F, H et M — sont **versionnées et datées** : elles contiennent des données périssables et doivent être révisées à chaque revue du document.

---

## Annexe A — Glossaire

**Accès conditionnel** — Mécanisme subordonnant l'accès aux ressources à l'état de conformité de l'appareil. §28.8
**Actif** — Élément matériel, logiciel, informationnel, humain ou de service ayant une valeur pour l'organisation ou participant au fonctionnement de son système d'information. Un actif sans propriétaire nommé est un actif *orphelin*, pas un non-actif.
**Actif de niveau 0** — Actif dont la compromission donne le contrôle d'un ensemble d'autres actifs : annuaire, hyperviseur, sauvegarde, coffre-fort, chaîne de construction. §11.7
**Actif d'entrée** — Actif par lequel un attaquant peut arriver, exposé par conception. §11.7
**Actif éphémère** — Actif créé et détruit automatiquement, absent des inventaires réseau. §10.8
**Actif maintenu** — Actif disposant d'un propriétaire nommé, d'une classe de service et d'une preuve de conformité.
**Actif orphelin** — Actif réel du périmètre, sans propriétaire désigné. Jamais exclu du dénominateur.
**Agent** — Programme résident remontant l'état d'une machine à une console centrale. §15.1
**Agilité cryptographique** — Capacité à changer d'algorithme ou de protocole sans reconstruire les applications. §24.8
**Anneau de déploiement** — Population successive recevant un correctif, avec critère de passage. §18.4
**Appliance** — Équipement ou machine virtuelle préconstruite dont le système n'est pas maintenable par le client. §3.1
**Arbre de décision** — Suite de questions ordonnées produisant une action plutôt qu'un score. §16.3
**Atteignabilité** — Possibilité effective d'appeler le code vulnérable dans un contexte donné. §11.6
**Autorisation déléguée** — Accès accordé à une application tierce au nom d'un utilisateur, matérialisé par un jeton, non révoqué par un changement de mot de passe. §31.6
**Backlog** — Ensemble des constats ouverts. §17.10
**Baseline** — Référentiel de configuration dérivé et versionné, propre à l'organisation. §22.3
**Bleu / vert** — Stratégie de déploiement à deux environnements complets, avec bascule du trafic. §6.4
**Chaîne de confiance** — Mécanisme cryptographique garantissant l'origine d'un paquet ou d'un micrologiciel. §2.3
**Chemin d'attaque** — Enchaînement d'étapes menant d'un point d'entrée à une cible. §11.4
**Classe de service** — Regroupement d'actifs partageant délais, fenêtres et niveau de test. §7.2
**CNA** — Organisation accréditée pour attribuer des identifiants de vulnérabilité. §4.2
**Combinaison toxique** — Ensemble d'éléments individuellement acceptables dont la conjonction crée un risque majeur. §11.5
**Compte de secours** — Compte d'urgence permettant l'accès quand les mécanismes normaux échouent. §24.2
**Conduit** — Chemin de communication entre zones, au sens des normes industrielles. §29.2
**Conformité** — Part des actifs se trouvant dans l'état attendu. Toujours accompagnée de son dénominateur. §38.2
**Constat** — Toute observation appelant une décision de remédiation : vulnérabilité, écart de configuration, résultat d'audit, secret exposé. §14.2
**Contrôleur de gestion à distance** — Composant permettant d'administrer un serveur indépendamment de son système d'exploitation. Actif de niveau 0. §27.1
**Convergence** — Réapplication périodique d'un état désiré par un outil de gestion de configuration. §23.3
**Correctif** — Modification publiée par un éditeur corrigeant un défaut.
**Correction virtuelle** — Blocage de l'exploitation en amont, sans modifier l'actif. §20.3
**Couverture** — Part du périmètre de référence atteinte par un outil ou un processus. §38.2
**CPE** — Nomenclature d'identification de produits, historique des bases de vulnérabilités. §4.3
**Critère d'arrêt** — Seuil chiffré interrompant automatiquement un déploiement. §18.4
**CSAF** — Format d'avis de sécurité lisible par machine. §4.8
**CVE** — Identifiant unique de vulnérabilité ; clé de dédoublonnage, pas jugement de gravité. §4.2
**CVSS** — Système de notation de la gravité technique intrinsèque d'une vulnérabilité. §4.4
**CWE** — Catalogue de types de faiblesses, indépendant des produits. §4.3
**Défaut d'autorisation** — Vulnérabilité applicative permettant d'accéder à des données d'autrui ; invisible à l'analyse automatique. §25.1
**Délai d'observation** — Temps volontairement laissé entre publication et déploiement pour que les régressions apparaissent ailleurs. §18.3
**Dénominateur** — Ensemble sur lequel un indicateur est rapporté ; l'attribut le plus important d'une mesure. §38.2
**Dépendance transitive** — Dépendance d'une dépendance, non choisie directement. §3.6
**Dépriorisation** — Décision documentée de ne pas traiter maintenant, avec date de revue. Un constat déprioritisé reste ouvert. §16.6
**Dérive de configuration** — Écart croissant entre l'état réel et la référence. §23.1
**Dérogation** — Décision formalisée, datée, bornée et compensée de ne pas appliquer la règle. §7.4
**Dette de sécurité** — Somme mesurable des corrections différées et de l'obsolescence. §1.6
**Découverte externe** — Cartographie de la surface exposée, réalisée depuis Internet. §11.2
**Démarrage sécurisé** — Vérification de la signature des composants chargés au démarrage. §3.8
**Effacement sécurisé** — Suppression de données avec preuve, sur tous les supports et copies. §35.4
**Époque** — Préfixe de version prenant le pas sur le reste dans les comparaisons de paquets. §2.6
**EPSS** — Modèle prédisant la probabilité d'exploitation d'une vulnérabilité à court terme. §4.5
**Exclusion** — Retrait volontaire d'un actif ou d'un chemin du périmètre d'un outil. Dérogation déguisée sans motif ni date de revue. §15.6, §34.4
**Exploit** — Code ou procédure transformant une vulnérabilité en effet concret. §4.1
**Exploitation active** — Observation réelle d'attaquants utilisant une vulnérabilité. §4.1
**Exposition** — Possibilité pour un attaquant d'atteindre un composant vulnérable. §11.1
**Faiblesse** — Type de défaut décrit indépendamment de tout produit. §4.1
**Fait vérifié / hypothèse probable / piste exploratoire** — Échelle de qualification d'une information. §14.7
**Fenêtre de maintenance** — Créneau pendant lequel une interruption est acceptée. §5.2
**Fichier de verrouillage** — Fichier figeant les versions exactes des dépendances. §3.6
**Fin de support** — Date après laquelle aucun correctif n'est publié, y compris de sécurité. §12.1
**Fin de support de sécurité** — Sur les équipements réseau, souvent antérieure à la fin de support matériel. §27.3
**Gel de production** — Période d'interdiction de changement, avec clause de levée pour vulnérabilité exploitée. §5.2
**Golden image** — Image de référence servant à créer les instances. §28.5
**Homologation** — Décision formelle autorisant l'usage d'un système, dont le maintien dépend du MCS. §39.5
**Immutabilité** — Principe de ne jamais modifier un système en service : reconstruire et remplacer. §3.5
**Interrupteur de fonctionnalité** — Paramètre activant ou désactivant un comportement sans redéploiement. §6.5
**Inventaire de composants (SBOM)** — Liste des composants d'un logiciel avec leurs versions. §4.8
**KEV (catalogue d'exploitation avérée)** — Recensement des vulnérabilités observées en exploitation. §4.6
**Live patching** — Application de correctifs au noyau sans redémarrage, à périmètre limité. §2.6
**MCO** — Maintien en condition opérationnelle : garantir que le système fonctionne. §1.2
**MCS** — Maintien en condition de sécurité : maintenir le niveau de sécurité sur tout le cycle de vie, preuve incluse. §1.1
**Mesure compensatoire** — Réduction de risque appliquée quand la correction est impossible ; sept attributs obligatoires. §20.7
**Micrologiciel** — Logiciel de bas niveau exécuté avant ou sous le système d'exploitation. §3.8
**Modèle de Purdue** — Découpage en niveaux d'une architecture industrielle. §3.7
**Non détecté / non vulnérable / non scanné** — Trois états distincts apparaissant identiquement dans un rapport. §15.8
**Périmètre de référence (périmètre maître)** — Union des sources d'inventaire, incluant orphelins et actifs à décommissionner. Point de départ du choix de dénominateur, **pas dénominateur universel** : chaque indicateur définit sa population éligible. §10.3, Annexe I.4
**Population éligible** — Sous-ensemble du périmètre maître auquel un contrôle donné s'applique effectivement. Annexe I.4
**Non mesuré** — Actif éligible à un contrôle mais non évalué. Ne devient jamais conforme par défaut. Annexe I.4
**N/A (non applicable)** — Actif hors de la population éligible d'un contrôle, avec motif documenté. Annexe I.4
**Horloge de risque** — Décompte du temps pendant lequel le risque existe ; ne se suspend jamais, contrairement au délai opérationnel de traitement. §17.5
**Ratio conservateur** — Taux calculé en traitant tout actif non mesuré comme non conforme. Hypothèse de prudence, pas mesure. Annexe K.2
**Point de non-retour** — Instant après lequel un retour arrière exige une restauration de données. §6.7
**Preuve d'état** — Version ou révision relevée directement sur l'actif, horodatée. §2.9
**Propriétaire métier** — Personne décidant de l'interruption et portant le risque. §5.5
**Propriétaire technique** — Personne exécutant la correction et produisant la preuve. §5.5
**Protection contre le retour en arrière** — Refus d'installer une version antérieure vulnérable. §6.11
**PSIRT** — Fonction traitant la sécurité des produits mis sur le marché. §33.2
**purl** — Nomenclature d'identification de paquets logiciels dans leur écosystème. §4.3
**Récurrence** — Réapparition d'un constat clos ; signale presque toujours un problème d'image de référence. §17.9
**Rétroportage (backport)** — Application d'un correctif à une version ancienne sans changer son numéro amont. §2.2
**Rolling update** — Déploiement progressif instance par instance. §6.4
**Sanctuarisation** — Réduction d'un système à un périmètre d'usage minimal, strictement contrôlé. §32.2
**Sas de transfert** — Étape contrôlée d'entrée de fichiers dans une zone industrielle. §29.5
**SSVC** — Approche de priorisation par arbre de décision. §4.7
**Support étendu** — Correctifs de sécurité au-delà de la fin de support, payants et conditionnés. §12.1
**Suspension de compteur** — Arrêt légitime et limitativement défini du décompte d'un délai. §17.5
**Témoin (canary)** — Déploiement sur une fraction du trafic ou du parc, avec mesure. §6.4
**Traîne longue** — Résidu d'actifs non traités en fin de campagne ; concentre une part disproportionnée du risque. §18.10
**VEX** — Déclaration d'exploitabilité d'un composant vulnérable dans un produit donné. §4.8
**Zone** — Ensemble d'actifs industriels partageant les mêmes exigences de sécurité. §29.2
**0-day** — Vulnérabilité sans correctif disponible. §4.1
**n-day** — Vulnérabilité corrigée mais non appliquée ; à l'origine de l'écrasante majorité des compromissions. §4.1

---

## Annexe B — Cheat sheets par plateforme

> ⏱ **Annexe versionnée — vérifiée le 1er août 2026.** Elle contient des commandes et des cadences susceptibles d'évoluer.
>
> **Format uniforme pour les douze fiches** : périmètre · contrôles · privilèges requis · lecture du résultat · preuve produite · limites · source de vérité · piège spécifique · cadence.

---

### B.1 Windows

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Postes et serveurs Windows, système et composants natifs |
| **Contrôles** | `Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" \| Select ProductName, DisplayVersion, CurrentBuild, UBR` · `Get-HotFix \| Sort InstalledOn -Descending` · `Test-Path "HKLM:\...\Component Based Servicing\RebootPending"` · `Get-WinEvent -LogName Setup` |
| **Privilèges** | Lecture locale suffisante ; administrateur pour le journal Setup |
| **Lecture du résultat** | Le couple **build + UBR** identifie le niveau de mise à jour cumulative |
| **Preuve produite** | Relevé build+UBR horodaté, avec identifiant d'actif (§2.9) |
| **Limites** | Ne couvre ni les applications, ni les composants facultatifs, ni l'environnement de récupération, ni les pilotes, ni les micrologiciels. La clé `RebootPending` n'est **qu'un** des signaux de redémarrage |
| **Source de vérité** | Portail de sécurité de l'éditeur, pour les versions affectées et corrigées |
| **Piège** | La réversibilité d'un correctif cumulatif ne se présume jamais (§2.5) |
| **Cadence** | Mensuelle, hors cycle en urgence |

---

### B.2 Linux — famille Debian

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Distributions dérivées de Debian, paquets système |
| **Contrôles** | `apt-cache policy <paquet>` · `zcat /usr/share/doc/<paquet>/changelog.Debian.gz \| head -40` · `needrestart -r l` · `/var/log/dpkg.log`, `/var/log/apt/history.log` |
| **Privilèges** | Lecture pour la version ; root pour `needrestart` complet |
| **Lecture du résultat** | La **révision éditeur** (`+debXuY`, `~debXuY`) porte le correctif, pas le numéro amont |
| **Preuve produite** | Version complète du paquet + date, + confirmation de redémarrage du service |
| **Limites** | `apt list --upgradable` ne filtre **pas** sur la sécurité · le journal local est un indice, pas une preuve |
| **Source de vérité** | Avis de sécurité de la distribution et suivi officiel du paquet |
| **Piège** | La notion d'**époque** (`1:`) prend le pas sur le reste dans les comparaisons de version |
| **Cadence** | Quotidienne pour la veille, mensuelle pour les campagnes |

---

### B.3 Linux — famille RHEL

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Distributions dérivées de Red Hat |
| **Contrôles** | `dnf updateinfo list security` · `rpm -q --changelog <paquet> \| grep CVE` · `needs-restarting -s` (services) · `needs-restarting -r` (système) · `dnf history list` / `dnf history info <ID>` |
| **Privilèges** | Lecture pour l'inventaire ; root pour `needs-restarting -r` |
| **Lecture du résultat** | `dnf updateinfo` filtre réellement sur la sécurité, contrairement à l'équivalent Debian |
| **Preuve produite** | Transaction `dnf history` datée + relevé de version |
| **Limites** | Le changelog RPM ne mentionne pas systématiquement l'identifiant de la faille |
| **Source de vérité** | Avis de sécurité de la distribution |
| **Piège** | Correctif appliqué sans redémarrage de service : le code vulnérable reste chargé (§2.6) |
| **Cadence** | Idem Debian |

---

### B.4 macOS et mobiles

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Postes macOS, terminaux mobiles gérés |
| **Contrôles** | Version minimale exigée par la politique d'accès · délai de report autorisé à l'utilisateur · population non enrôlée |
| **Privilèges** | Console de gestion de flotte |
| **Lecture du résultat** | La conformité dépend en partie du **comportement de l'utilisateur**, pas seulement du déploiement |
| **Preuve produite** | État de conformité par appareil, avec date de dernier contact |
| **Limites** | Ne couvre que les appareils **enrôlés** — les autres n'apparaissent nulle part |
| **Source de vérité** | Notes de version de l'éditeur du système |
| **Piège** | On pilote ici par la **politique d'accès**, pas par le déploiement (§19.4) |
| **Cadence** | Mensuelle, avec contrôle à la reconnexion |

---

### B.5 Conteneurs et orchestration

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Images, registres, clusters d'orchestration |
| **Contrôles** | Âge de l'image en production · référence par empreinte immuable et non par étiquette · version du plan de contrôle · écart plan de contrôle / nœuds · inventaire des interfaces dépréciées utilisées |
| **Privilèges** | Lecture sur le registre et l'orchestrateur |
| **Lecture du résultat** | L'âge de l'image est un **indicateur préventif central**, à compléter par l'analyse de vulnérabilités |
| **Preuve produite** | Empreinte d'image déployée + date de construction |
| **Limites** | Ne voit pas ce qui est ajouté au conteneur à l'exécution · les actifs éphémères échappent à l'inventaire réseau |
| **Source de vérité** | Registre d'images et politique de support du projet |
| **Piège** | Une image reconstruite hier peut embarquer une dépendance vulnérable ; une image plus ancienne peut porter un rétroportage corrigé |
| **Cadence** | Reconstruction ≤ 30 j · montée de version du cluster 2 à 3 fois/an |

---

### B.6 Réseau et sécurité

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Pare-feu, routeurs, commutateurs, passerelles d'accès distant |
| **Contrôles** | Version d'image active et de secours · **date de fin de support de sécurité** · interface d'administration non publiée (vérification **depuis l'extérieur**) · export des journaux hors équipement |
| **Privilèges** | Compte d'administration en lecture |
| **Lecture du résultat** | Relevé de version directement sur l'équipement, pas dans un tableur |
| **Preuve produite** | Sortie de commande de version, horodatée |
| **Limites** | Rarement couvert par un scan authentifié : suivi manuel assumé |
| **Source de vérité** | Portail de sécurité du constructeur |
| **Piège** | La fin de support **de sécurité** précède souvent de plusieurs années la fin de vie matérielle (§27.3) |
| **Cadence** | Trimestrielle, doctrine de version datée et revue |

---

### B.7 Hyperviseurs et plans de gestion

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Hôtes, plan de gestion, micrologiciel du matériel sous-jacent |
| **Contrôles** | Version de l'hôte · version du plan de gestion · **exposition réseau du plan de gestion** · version du micrologiciel serveur |
| **Privilèges** | Administration de la plateforme |
| **Lecture du résultat** | Quatre objets distincts à suivre séparément (§3.1) |
| **Preuve produite** | Inventaire de versions exporté depuis la console |
| **Limites** | Les appliances virtuelles fournisseur ne sont pas maintenues par vous |
| **Source de vérité** | Matrice de compatibilité et avis de l'éditeur |
| **Piège** | Le plan de gestion est un **actif de niveau 0** régulièrement laissé en retard |
| **Cadence** | Trimestrielle, avec fenêtre récurrente dédiée |

---

### B.8 Cloud

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Ressources, images, services managés, identités, configuration |
| **Contrôles** | Âge des images du catalogue · **versions de services managés et leurs dates de fin de support** · identités à droits étendus · garde-fous préventifs actifs · écart entre code d'infrastructure et réalité |
| **Privilèges** | Lecture sur les interfaces du fournisseur |
| **Lecture du résultat** | Sur les services managés, vous pilotez l'**anticipation**, pas la correction |
| **Preuve produite** | Export d'inventaire de ressources + versions, horodaté |
| **Limites** | Aucune preuve technique possible sur la couche du fournisseur |
| **Source de vérité** | Notes de service et calendriers de dépréciation du fournisseur |
| **Piège** | Les versions de services managés doivent entrer au référentiel d'obsolescence (§30.3) — l'oubli le plus fréquent |
| **Cadence** | Mensuelle pour les annonces, trimestrielle pour l'inventaire |

---

### B.9 Services en ligne

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Configuration du locataire, identités, extensions, intégrations |
| **Contrôles** | État de référence sur les huit familles de paramètres (§31.4) · inventaire des autorisations déléguées · consentement utilisateur restreint · rétention des journaux connue |
| **Privilèges** | Administration du service |
| **Lecture du résultat** | Comparaison à un état de référence documenté, pas à la mémoire |
| **Preuve produite** | Export de configuration daté + liste des applications autorisées |
| **Limites** | Aucun accès technique au socle · rapports d'audit du fournisseur insuffisants seuls |
| **Source de vérité** | Notes de version et annonces de dépréciation du fournisseur |
| **Piège** | Une fonctionnalité activée par défaut modifie votre exposition sans que votre configuration change |
| **Cadence** | Mensuelle sur les services sensibles, annuelle sur les autres |

---

### B.10 Industriel

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Automates, supervision, systèmes d'exécution de production |
| **Contrôles** | Écoute passive du trafic · extraction depuis les outils d'ingénierie · inventaire manuel avec l'équipe de maintenance |
| **Privilèges** | Accès aux outils d'ingénierie, avec accompagnement |
| **Lecture du résultat** | L'inventaire manuel est souvent le plus fiable sur les équipements anciens |
| **Preuve produite** | Relevé de version signé, journal de transfert (§29.5) |
| **Limites** | L'écoute passive ne voit que ce qui communique |
| **Source de vérité** | Avis du constructeur, avec validation écrite pour tout correctif |
| **Piège** | Doctrine : **passif par défaut, actif sous procédure** — un scan actif contrôlé reste possible, il ne s'improvise pas |
| **Cadence** | Alignée sur les arrêts de production |

---

### B.11 Bases de données, middlewares et *runtimes*

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Moteurs de bases, serveurs d'applications, environnements d'exécution, bibliothèques embarquées |
| **Contrôles** | Inventaire **par application** et non par machine · versions majeures et mineures suivies séparément · authentification activée sur brokers, caches et moteurs de recherche |
| **Privilèges** | Lecture applicative et système |
| **Lecture du résultat** | Le blocage vient presque toujours de l'application, pas du moteur |
| **Preuve produite** | Tableau composant / version / date de fin de support / source |
| **Limites** | Les bibliothèques natives embarquées n'apparaissent ni au scan système, ni à l'analyse de composition |
| **Source de vérité** | Pages de cycle de vie de chaque éditeur, et inventaire de composants fourni |
| **Piège** | Système parfaitement à jour, application sur un composant hors support depuis deux ans (§26.1) |
| **Cadence** | Trimestrielle pour l'inventaire, annuelle pour la trajectoire de version |

---

### B.12 Applications tierces du poste

| Rubrique | Contenu |
|---|---|
| **Périmètre** | Navigateurs et extensions, lecteurs, environnements d'exécution, utilitaires métier |
| **Contrôles** | Inventaire sur un **échantillon** de postes avant tout achat d'outil · liste des applications hors support |
| **Privilèges** | Lecture locale ou console de gestion |
| **Lecture du résultat** | La liste est presque toujours plus longue et plus ancienne qu'attendu |
| **Preuve produite** | Inventaire applicatif par poste, daté |
| **Limites** | Non couvert par les mécanismes natifs du système |
| **Source de vérité** | Éditeur de chaque application |
| **Piège** | La mise à jour automatique native ne donne ni contrôle, ni visibilité, ni preuve (§19.5) |
| **Cadence** | Mensuelle, avec un inventaire complet semestriel |

---

## Annexe C — Matrices de priorisation et de délais

### C.1 Comparatif des signaux

| Signal | Répond à | Ne répond pas à | Volatilité |
|---|---|---|---|
| Gravité technique | Quels dégâts si exploitée ? | Est-ce exploité ? Suis-je atteignable ? | Nulle (base fixe) |
| Probabilité d'exploitation | Sera-t-elle exploitée dans le monde ? | Chez moi ? Sur cet actif ? | **Élevée** — et discontinue entre versions de modèle |
| Exploitation avérée | A-t-elle été observée ? | Suis-je concerné et exposé ? | Cumulative |
| Arbre de décision | **Que dois-je faire ?** | *(nécessite l'exposition en entrée)* | Stable |
| **Exposition** | Est-ce atteignable, par qui ? | — | Change à chaque projet |
| **Criticité métier** | Que vaut cet actif ? | — | Stable |

Les deux dernières lignes sont produites **par vous seul**.

### C.2 Arbre de décision de référence

```
① Exploitation active ?
   ├─ OUI → ② Joignable depuis Internet ?
   │         ├─ OUI → AGIR EN URGENCE (72 h, hors fenêtre autorisée)
   │         └─ NON → ③ Niveau 0 ou critique métier ?
   │                   ├─ OUI → TRAITER EN PRIORITÉ (7 j)
   │                   └─ NON → TRAITER (30 j)
   └─ NON → ④ Probabilité élevée OU gravité critique ?
             ├─ OUI → ⑤ Exposé ou critique ?
             │         ├─ OUI → TRAITER (30 j)
             │         └─ NON → PLANIFIER (campagne)
             └─ NON → ⑥ Corrigeable en campagne groupée ?
                       ├─ OUI → PLANIFIER (trimestrielle)
                       └─ NON → SURVEILLER (revue semestrielle)
```

### C.3 Matrice délais × classe

| | C1 exposé/critique | C2 important | C3 courant | C4 contraint |
|---|---|---|---|---|
| Exploitée | 72 h | 7 j | 30 j | **Compensation sous 72 h** |
| Critique non exploitée | 15 j | 30 j | 60 j | Compensation ou dérogation |
| Autres | 30 j | 90 j | 180 j | Selon fenêtre constructeur |
| Vérification | Hebdo | Mensuelle | Mensuelle | Trimestrielle |
| Test préalable | Recette + témoin | Témoin | Anneau pilote | Validation fournisseur |

*Valeurs de départ pour une organisation de taille intermédiaire. Calibrez sur votre capacité mesurée (§16.5).*

### C.4 Grille d'acceptation de risque

| Niveau de risque résiduel | Signataire |
|---|---|
| Actif C3, non exposé | Propriétaire technique |
| Actif C2 | Propriétaire métier |
| Actif C1 ou exposé | Directeur des systèmes d'information |
| Actif de niveau 0, ou données sensibles | **Direction générale** |
| Renouvellement d'une dérogation | **Niveau supérieur au précédent** (§7.4) |

---

## Annexe D — Templates opérationnels

> **Quatorze formulaires remplissables.** Chacun porte un identifiant, une version et une date. Les champs `[ ]` sont à compléter, les champs marqués **(O)** sont obligatoires, **(F)** facultatifs. Les règles de validation indiquent ce qui bloque l'acceptation du document.
>
> ⚠️ Les valeurs numériques proposées (délais, seuils, durées) constituent un **modèle de référence de ce cours**, à adapter et faire approuver par votre organisation. Elles ne sont ni une norme ni une exigence externe.

---

### D.1 — Politique MCS

**Identifiant** `POL-MCS-[nn]` · **Version** `[x.y]` · **Date** `[jj/mm/aaaa]` · **Approbateur** `[nom, fonction]` · **Revue** `[annuelle]`

| § | Section | Contenu attendu | Longueur |
|---|---|---|---|
| 1 | Objet et périmètre | Ce qui est couvert · **ce qui ne l'est pas, et pourquoi** | ½ p. |
| 2 | Définitions | Actif · propriétaire · couverture · conformité · population éligible · non mesuré | 1 p. |
| 3 | Rôles | Renvoi au RACI D.3, décideurs nommés par type de décision | 1 p. |
| 4 | Classes de service | Le formulaire D.2 intégré | 2-3 p. |
| 5 | Processus | Veille · détection · triage · remédiation · vérification · preuve | 2-3 p. |
| 6 | Dérogations | Renvoi à D.4, niveaux de signature, règle de renouvellement | 1 p. |
| 7 | Mesure et contrôle | Indicateurs publiés, fréquence, destinataires | 1 p. |
| Ann. | **Périmètres non couverts** | Tableau ci-dessous | 1 p. |

**Annexe obligatoire — périmètres déclarés non couverts**

| Périmètre | Motif de non-couverture | Propriétaire désigné | Échéance de première mesure | Compensation en place |
|---|---|---|---|---|
| `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |

**Règles de validation** — La politique ne peut être approuvée si : un délai annoncé n'a pas été confronté à une mesure de capacité (§16.5) · la procédure de dérogation est absente · l'annexe des périmètres non couverts est vide sans justification écrite.

---

### D.2 — Table des classes de service

**Identifiant** `CLS-[nn]` · **Version** `[ ]` · **Approbateur** `[DSI]`

| Paramètre | C1 — critique/exposé | C2 — important | C3 — courant | C4 — contraint |
|---|---|---|---|---|
| **Définition** (O) | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| **Exemples d'actifs** (O) | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Délai — vulnérabilité exploitée (O) | `[72 h]` | `[7 j]` | `[30 j]` | `[compensation 72 h]` |
| Délai — critique non exploitée (O) | `[15 j]` | `[30 j]` | `[60 j]` | `[compensation/dérogation]` |
| Délai — autres (O) | `[30 j]` | `[90 j]` | `[180 j]` | `[fenêtre constructeur]` |
| Fréquence de vérification (O) | `[hebdo]` | `[mensuelle]` | `[mensuelle]` | `[trimestrielle]` |
| Niveau de test (O) | `[recette + témoin]` | `[témoin]` | `[anneau pilote]` | `[validation fournisseur]` |
| Fenêtre (O) | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Délai d'observation (F) | `[0-3 j]` | `[5 j]` | `[5 j]` | `[n/a]` |

**Validation** — Chaque délai doit être accompagné de la mesure de capacité qui le justifie. Un délai non tenu trois mois consécutifs déclenche une révision de la classe ou de la capacité.

---

### D.3 — RACI du MCS

**Identifiant** `RACI-MCS-[nn]` · **Version** `[ ]` · **Périmètre** `[IT / OT / cloud / produit]`

**R** réalise · **A** approuve (un seul par ligne) · **C** consulté · **I** informé

| Activité | RSSI | Exploitation | Propr. métier | DSI | Prestataire |
|---|---|---|---|---|---|
| Définir la politique et les classes | `[R]` | `[C]` | `[C]` | `[A]` | `[I]` |
| Tenir l'inventaire | `[C]` | `[R/A]` | `[C]` | `[I]` | `[R]` |
| Veille et qualification | `[R/A]` | `[C]` | `[I]` | `[I]` | `[C]` |
| Prioriser et fixer les délais | `[R]` | `[C]` | `[C]` | `[A]` | `[I]` |
| Planifier et exécuter | `[I]` | `[R/A]` | `[C]` | `[I]` | `[R]` |
| **Décider d'une interruption** | `[C]` | `[C]` | `[A]` | `[I]` | `[I]` |
| **Accorder une dérogation** | `[R]` | `[C]` | `[A]` | `[C]` | `[I]` |
| Produire la preuve | `[C]` | `[R]` | `[I]` | `[I]` | `[R]` |
| Escalader une impossibilité | `[C]` | `[R]` | `[C]` | `[A]` | `[R]` |
| Contrôler l'application | `[R/A]` | `[C]` | `[I]` | `[I]` | `[I]` |

**Validation** — Un seul **A** par ligne. Toute case **A** doit correspondre à une personne nommée disposant du mandat correspondant, pas à une entité collective.

---

### D.4 — Fiche de dérogation

**Identifiant** `DER-[aaaa]-[nnn]` · **Version** `[ ]` · **Date d'émission** `[ ]`

| Champ | | Valeur |
|---|---|---|
| Objet précis | (O) | `[actif(s) · vulnérabilité ou écart · correctif concerné]` |
| Type d'impossibilité | (O) | `[ ] technique  [ ] contractuelle  [ ] métier  [ ] budgétaire  [ ] temporelle` |
| **Analyse de risque, en termes métier** | (O) | `[ce qui se passe si le risque se réalise : données, service, personnes, conséquences contractuelles]` |
| Exposition mesurée | (O) | `[ ] Internet  [ ] réseau bureautique  [ ] réseau d'administration  [ ] isolé` |
| Exploitation observée | (O) | `[ ] non  [ ] dans le monde  [ ] dans le secteur  [ ] indices chez nous` |
| Mesures compensatoires | (O) | `[1. ]  [2. ]  [3. ]` — hiérarchie du §20.2, en indiquant les rangs écartés et pourquoi |
| **Moyen de vérification** | (O) | `[test précis prouvant que la compensation est active]` |
| Fréquence du contrôle | (O) | `[mensuelle]` |
| Coût opérationnel | (O) | `[h/mois]` |
| Propriétaire de la compensation | (O) | `[nom]` |
| **Signataire** | (O) | `[nom, fonction — selon la grille C.4]` |
| Date de début | (O) | `[ ]` |
| **Date d'expiration** | (O) | `[date du calendrier, alignée sur un événement décisionnel réel]` |
| Conditions de sortie | (O) | `[correction réalisée]  [exploitation observée]  [changement d'exposition]` |
| **Conditions de révocation anticipée** | (O) | `[événements imposant de mettre fin immédiatement à la dérogation]` |
| Nombre de renouvellements | (O) | `[0]` — chaque renouvellement remonte d'un niveau de signature |
| Date de revue | (O) | `[trimestrielle]` |

**Règles de validation** — Rejet automatique si : pas de date d'expiration ou date exprimée en événement flou · compensation sans moyen de vérification · signataire non conforme à la grille C.4 · risque décrit en termes techniques uniquement.

**Quatre notions que le terrain confond, et qu'il faut séparer par écrit**

| Notion | Nature | Durée | Signataire | Ce qui la clôt |
|---|---|---|---|---|
| **Dérogation** | Exception temporaire à une règle existante | **Bornée** | Propriétaire métier, niveau selon C.4 | La correction, ou une condition de sortie |
| **Acceptation de risque** | Décision durable de porter un risque résiduel | **Non bornée**, mais revue | Niveau supérieur, selon C.4 | Une revue qui change la décision |
| **N/A** | La règle ne s'applique pas à cet actif | Permanente tant que le contexte tient | Propriétaire technique | Un changement de contexte |
| **Faux positif** | Le constat était erroné | Définitive | Analyste, **avec démonstration** | — |

⚠️ **Le mot « exception » recouvre les quatre dans le langage courant**, et il désigne en plus les exclusions d'outil (§15.6, §34.4). C'est la principale source d'ambiguïté d'un registre de dérogations. La règle interne : le mot « exception » ne figure dans aucun document formel de ce dispositif — on écrit toujours laquelle des cinq choses on désigne.

---

### D.5 — Demande de changement urgent

**Identifiant** `CHG-U-[aaaa]-[nnn]` · **Émission** `[date, heure]` · **Régularisation attendue sous** `[48 h]`

| Section | Contenu |
|---|---|
| Constat et qualification | `[identifiant · statut : fait vérifié / hypothèse / piste · source]` |
| Exposition mesurée | `[nombre d'actifs · joignables depuis · depuis quand]` |
| Chemin dans l'arbre de décision | `[reproduire les réponses aux questions ① à ⑥]` |
| Justification de l'urgence | `[critère de déclenchement satisfait]` |
| Périmètre de l'intervention | `[liste ou requête d'actifs]` |
| **Écart recette / production** | `[versions · volumétrie · intégrations · configuration — chacun qualifié]` |
| **Critères go/no-go** | Renvoi D.6, **joints obligatoirement** |
| **Plan de retour arrière** | Renvoi D.7, **joint obligatoirement** |
| Point de non-retour | `[instant précis]` ou `[aucun]` |
| Décideur nommé | `[nom]` |
| Décideur du retour arrière | `[nom]` — peut différer |
| Communication prévue | `[direction] [métiers] [utilisateurs] [clients] [assureur] [autorités]` |
| Preuve à produire | `[nature · échantillon · responsable]` |

**Validation** — Le changement ne peut être exécuté sans D.6 et D.7 joints, ni sans décideur nommé pour le retour arrière.

---

### D.6 — Critères go / no-go

**Identifiant** `GNG-[aaaa]-[nnn]` · **Rattaché à** `[CHG-...]` · **Écrit le** `[avant l'intervention]`

| Indicateur | Seuil d'arrêt | Mesuré par | Fenêtre d'observation |
|---|---|---|---|
| Taux d'échec d'installation | `[> 5 %]` | `[outil]` | `[continu]` |
| Incidents déclarés liés | `[≥ 3 sur l'anneau]` | `[support]` | `[24 h]` |
| **Indicateur fonctionnel métier** (O) | `[baisse > 10 % sur 30 min]` | `[supervision]` | `[continu]` |
| Redémarrages inattendus | `[≥ 2 machines]` | `[supervision]` | `[continu]` |
| Temps de réponse | `[+ 50 % sur 15 min]` | `[supervision]` | `[continu]` |

**Critère de passage à l'anneau suivant** : `[tous les seuils respectés pendant [n] jours ET aucun incident bloquant ouvert]`

**Validation** — Au moins un indicateur **fonctionnel** est obligatoire : un service peut répondre correctement tout en ayant cessé de faire son travail (§6.8). Un formulaire rempli après le début de l'intervention est irrecevable.

---

### D.7 — Plan de retour arrière

**Identifiant** `RB-[aaaa]-[nnn]` · **Rattaché à** `[CHG-...]`

| Champ | Valeur |
|---|---|
| Mécanisme retenu | `[ ] instantané  [ ] sauvegarde  [ ] redéploiement d'image  [ ] désinstallation vérifiée  [ ] double partition  [ ] bascule bleu/vert` |
| **Testé le** (O) | `[date]` — sur `[topologie représentative : oui/non, écarts]` |
| **Durée mesurée** (O) | `[hh:mm]` |
| Périmètre couvert | `[ ] binaires  [ ] configuration  [ ] schéma de données  [ ] caches  [ ] files de messages  [ ] effets externes` |
| **Point de non-retour** (O) | `[instant précis]` ou `[aucun]` |
| Ce que le retour arrière **ne restaure pas** | `[transactions depuis l'instantané · état des systèmes tiers · notifications déjà émises]` |
| Critère de déclenchement | `[renvoi D.6]` |
| Décideur | `[nom]` |
| Vérification post-retour | `[contrôles à réaliser pour confirmer l'état antérieur]` |

**Validation** — Un plan dont la durée n'a pas été chronométrée sur une topologie représentative n'est pas un plan : c'est une intention (§18.8).

---

### D.8 — Fiche d'obsolescence d'actif

**Identifiant** `OBS-[aaaa]-[nnn]`

| Champ | Valeur |
|---|---|
| Actif ou population | `[ ]` · Nombre `[ ]` |
| Composant concerné | `[système / base de données / runtime / matériel / micrologiciel]` |
| **Date de fin de support** | `[ ]` · Type : `[ ] fonctionnelle [ ] support [ ] support de sécurité [ ] support étendu` |
| **Source et date de vérification** | `[page officielle, consultée le ...]` |
| Criticité / exposition | `[C1-C4]` / `[ ]` |
| Éligibilité au support étendu | `[ ] vérifiée actif par actif — résultat : [ ]` |

**Trois options chiffrées, sur la durée complète** *(le statu quo est obligatoire)*

| Option | Coût total | Risque résiduel | Faisabilité |
|---|---|---|---|
| Support étendu `[n]` ans | `[ ]` | `[ ]` | `[ ]` |
| Migration / remplacement | `[ ]` | `[ ]` | `[ ]` |
| **Statu quo** | `[compensations + urgences + astreinte + risque]` | `[ ]` | `[ ]` ou `[indisponible : motif]` |
| Retrait du service | `[ ]` | `[ ]` | `[ ]` |

**Décision** `[option]` · **Décideur** `[nom]` · **Date** `[ ]` · **Financement** `[exercice, montant]` · **Jalons** `[ ]` · **Point de non-retour** `[ ]`

---

### D.9 — Clauses contractuelles MCS

**Identifiant** `CLA-MCS-[nn]` — à insérer en annexe technique du contrat.

| # | Clause | Texte type | Obtenue |
|---|---|---|---|
| 1 | Délais par criticité | « Le Prestataire applique les correctifs de sécurité selon les délais figurant en annexe [X], décomptés à partir de la publication du correctif par l'éditeur. » | `[ ]` |
| 2 | Périmètre nominatif | « Le périmètre couvert est défini par la liste d'actifs annexée, mise à jour trimestriellement et contradictoirement. » | `[ ]` |
| 3 | **Restitution de données** | « Le Prestataire fournit mensuellement, dans un format exploitable et exportable, l'état de mise à jour de chaque actif du périmètre, **y compris la liste des actifs non joignables et leur motif**. » | `[ ]` |
| 4 | Notification | « Le Prestataire notifie sous 24 heures toute vulnérabilité activement exploitée affectant un actif du périmètre. » | `[ ]` |
| 5 | Transparence des versions | « Le Prestataire communique sur demande les versions déployées et son propre calendrier d'obsolescence. » | `[ ]` |
| 6 | Droit d'audit et de test | « Le Client peut faire réaliser un contrôle technique du périmètre, avec un préavis de [30] jours. » | `[ ]` |
| 7 | Sous-traitance | « Le Prestataire déclare ses sous-traitants intervenant sur le périmètre et leur impose les mêmes obligations. » | `[ ]` |
| 8 | **Escalade des impossibilités** | « Toute impossibilité de correction est notifiée sous [5] jours ouvrés, avec sa cause et une proposition de mesure compensatoire. » | `[ ]` |
| 9 | Accès aux preuves | « Le Prestataire met à disposition les journaux d'administration et les preuves d'application relatifs au périmètre. » | `[ ]` |
| 10 | Réversibilité | « En fin de contrat, le Prestataire restitue l'inventaire complet, **l'historique de mise à jour** et la documentation d'exploitation, dans un format ouvert. » | `[ ]` |
| 11 | Assistance au décommissionnement | « Le Prestataire assiste au retrait des accès, comptes et secrets le concernant, et en fournit la preuve. » | `[ ]` |
| 12 | Conséquence d'un manquement | « Le non-respect constaté deux mois consécutifs déclenche un plan de retour à la conformité sous contrôle du Client. » | `[ ]` |

**Priorité si vous ne pouvez en obtenir que trois** : 3, 8, 2.
**En cas de refus** : consigner la demande et le refus **par écrit** (§13.8), documenter le risque accepté, préparer l'architecture de sortie.

---

### D.10 — Questionnaire fournisseur

**Identifiant** `QF-[aaaa]-[nnn]` · **Fournisseur** `[ ]` · **Produit/service** `[ ]` · **Date** `[ ]`

| # | Question | Réponse | Preuve fournie |
|---|---|---|---|
| 1 | Politique de publication des correctifs de sécurité : fréquence, canaux, délai entre découverte et publication | `[ ]` | `[ ]` |
| 2 | Combien de versions maintenez-vous en sécurité, et pendant combien de temps ? | `[ ]` | `[ ]` |
| 3 | Quel préavis donnez-vous avant une fin de support ? | `[ ]` | `[ ]` |
| 4 | Comment nous notifiez-vous une vulnérabilité affectant votre produit ? | `[ ]` | `[ ]` |
| 5 | Fournissez-vous un inventaire des composants du produit ? Sous quel format ? | `[ ]` | `[ ]` |
| 6 | Publiez-vous des déclarations d'exploitabilité ? | `[ ]` | `[ ]` |
| 7 | Les postes utilisés pour administrer notre périmètre sont-ils **dédiés** à l'administration ? | `[ ]` | `[ ]` |
| 8 | Les comptes utilisés chez nous nous sont-ils propres ? | `[ ]` | `[ ]` |
| 9 | Comment cloisonnez-vous vos clients ? | `[ ]` | `[ ]` |
| 10 | Les actions d'administration sont-elles journalisées, et pouvons-nous obtenir ces journaux ? | `[ ]` | `[ ]` |
| 11 | **Quel est votre propre niveau de MCS, et comment le démontrez-vous ?** | `[ ]` | `[ ]` |
| 12 | Quelles données conservez-vous, où, et comment les restituez-vous en fin de contrat ? | `[ ]` | `[ ]` |

**Cotation** : `[ ]` réponse documentée avec preuve · `[ ]` réponse déclarative · `[ ]` sans réponse. Toute question sans réponse devient une ligne de risque documentée.

---

### D.11 — Journal de crise vulnérabilité

**Identifiant** `CRI-[aaaa]-[nnn]` · **Pilote** `[nom]` · **Greffier** `[nom]` · **Ouverture** `[date, heure]`

| Heure | Information reçue | **Source** | Statut | Décision | Décideur | Action | Responsable | Échéance |
|---|---|---|---|---|---|---|---|---|
| `[hh:mm]` | `[ ]` | `[ ]` | `[fait/hypothèse/piste]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` |

**Encadré permanent — état de la connaissance**

| Question | Réponse à l'instant `[hh:mm]` |
|---|---|
| Depuis quand l'actif est-il exposé et vulnérable ? | `[ ]` |
| Quels journaux couvrent cette période ? | `[ ]` |
| Permettraient-ils de détecter ce type d'exploitation ? | `[ ]` |
| **Peut-on établir l'absence de compromission ?** | `[ ] oui  [ ] non — préciser` |

**Clôture** : critères de sortie atteints `[ ]` · mesures d'urgence levées ou converties en compensations `[ ]` · retour d'expérience planifié le `[ ]`

---

### D.12 — Matrice de responsabilité cloud

**Identifiant** `RESP-CLOUD-[nn]` · **Revue** `[semestrielle]`

| Service | Modèle | Le fournisseur maintient | Nous maintenons | Fenêtre imposée | Préavis | **Preuve disponible** | Propriétaire |
|---|---|---|---|---|---|---|---|
| `[ ]` | `[IaaS/PaaS/SaaS/fonctions]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ] oui [ ] non` | `[ ]` |

**Ligne obligatoire par service** : version actuellement utilisée `[ ]` · **date de fin de support de cette version** `[ ]` · source `[ ]`.

**Validation** — Toute ligne dont la colonne « preuve disponible » est vide alimente l'annexe des périmètres non couverts de D.1.

---

### D.13 — Dossier de preuves

**Identifiant** `PRV-[aaaa]` · **Constitué en continu** · **Responsable** `[nom]`

| # | Pièce | Présente | Date de la dernière mise à jour | Emplacement |
|---|---|---|---|---|
| 1 | Périmètre de référence daté, avec sources réconciliées et zones non couvertes | `[ ]` | `[ ]` | `[ ]` |
| 2 | Politique MCS approuvée (D.1) | `[ ]` | `[ ]` | `[ ]` |
| 3 | RACI et comitologie (D.3) | `[ ]` | `[ ]` | `[ ]` |
| 4 | Arbre de décision de triage, daté et validé | `[ ]` | `[ ]` | `[ ]` |
| 5 | Journaux de campagne, dont traîne longue qualifiée | `[ ]` | `[ ]` | `[ ]` |
| 6 | **Preuves d'état sur échantillon**, indépendantes des outils | `[ ]` | `[ ]` | `[ ]` |
| 7 | Registre des dérogations (D.4) | `[ ]` | `[ ]` | `[ ]` |
| 8 | Registre des exclusions (scan, protection des postes) | `[ ]` | `[ ]` | `[ ]` |
| 9 | Comptes rendus de comité, avec **décisions** | `[ ]` | `[ ]` | `[ ]` |
| 10 | Indicateurs historisés, avec définitions et ruptures marquées | `[ ]` | `[ ]` | `[ ]` |
| 11 | Procès-verbaux de décommissionnement (D.14) | `[ ]` | `[ ]` | `[ ]` |

**Contrôle de crédibilité** — Si les dates de production de plus de la moitié des pièces sont groupées sur moins d'un mois, le dossier a été reconstitué : cela se voit, et cela se retourne contre vous (§39.2).

---

### D.14 — Procès-verbal de décommissionnement

**Identifiant** `PVD-[aaaa]-[nnn]` · **Actif** `[ ]` · **Mis en service le** `[ ]`

| # | Étape | Fait | Date | Preuve | Responsable |
|---|---|---|---|---|---|
| 1 | Usage réel mesuré avant décision | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 2 | Décision de retrait et préavis diffusé | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 3 | **Extinction avant suppression**, observation ≥ 1 cycle métier | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 4 | Dépendances identifiées et traitées | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 5 | Données migrées / archivées / **effacées avec attestation** | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 6 | Enregistrements de noms et alias supprimés | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 7 | Publications externes retirées, vérifiées depuis l'extérieur | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 8 | Règles de filtrage supprimées | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 9 | **Comptes, clés, secrets, jetons, autorisations déléguées révoqués côté fournisseur** | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 10 | Certificats traités (révocation **ou** destruction de clé documentée) | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 11 | Retrait des outils, **historiques préservés** | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 12 | Décision sur les sauvegardes, avec date de suppression | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 13 | Matériel et licences traités | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 14 | Contrats résiliés | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| 15 | **Vérification à J+[90]** — contrôles du §35.11 | `[ ]` | `[ ]` | `[ ]` | `[ ]` |

**Signatures** — Propriétaire métier `[nom, date]` · Propriétaire technique `[nom, date]`

**Validation** — Le décommissionnement n'est pas clos tant que la ligne 15 n'est pas renseignée. Un PV sans double signature est irrecevable.

---

## Annexe E — Familles d'outils et exemples de référence

> ⏱ **Annexe versionnée — vérifiée le 30 juillet 2026.** Péremption recommandée : **12 mois**.
> Organisée par **famille**, avec deux à trois exemples représentatifs. **Aucun tarif détaillé** : les prix sont négociés, dépendants des offres groupées, régionaux et rapidement obsolètes. Seuls les *modèles* de facturation figurent ici, car eux seuls sont structurants pour un budget. Aucun outil n'est une solution universelle.

### E.1 Comment lire les modèles de licence

| Modèle | Ce qu'il implique pour le budget |
|---|---|
| **Gratuit / open source** | Gratuit à l'acquisition ; l'exploitation, l'intégration et le maintien restent à financer — souvent le poste principal |
| **Par actif** | Le coût croît avec la découverte : mieux inventorier augmente la facture (incitation perverse, §19.9) |
| **Par volume analysé** | Coût lié au nombre d'analyses, d'images ou de charges de travail |
| **À la consommation** | Coût lié aux appels, aux données ou à la durée |
| **Sur devis** | Prix non public, fortement dépendant du périmètre et de la négociation |

### E.2 Les familles

| Famille | Exemples représentatifs | Modèle | Limites concrètes |
|---|---|---|---|
| **Scan de vulnérabilités** | Solutions commerciales de scan authentifié (Tenable, Qualys, Rapid7) · alternative libre : OpenVAS/Greenbone | Par actif · libre | Faux positifs de rétroportage · historique rarement portable · systèmes industriels et services en ligne hors champ |
| **Découverte externe** | Modules EASM des mêmes éditeurs · services spécialisés | Par domaine · sur devis | Peut attribuer à tort des actifs · ne voit rien de l'interne |
| **Déploiement Windows** | Configuration Manager · Intune · Windows Update for Business · WSUS (en fin de cycle) | Inclus dans des offres groupées · par poste | Applications tierces non couvertes nativement · reporting difficilement exportable |
| **Déploiement Linux** | Ansible · Red Hat Satellite · Landscape · SUSE Manager · dépôts internes | Libre · par nœud · abonnement | Orchestration des redémarrages à construire |
| **Applications tierces** | Gestionnaires de paquets Windows (winget, Chocolatey) · modules tiers des outils de déploiement | Libre · option payante | Couverture du catalogue variable sur les applications métier |
| **Gestion de flotte** | Intune · Jamf · solutions équivalentes | Par appareil | Ne couvre que les appareils enrôlés |
| **Analyse de composition** | Dependabot/Renovate · Snyk · OWASP Dependency-Check · Trivy | Libre · par développeur · par dépôt | Bruit élevé sans analyse d'atteignabilité |
| **Analyse d'images** | Trivy · Grype · modules de registres | Libre · inclus | Ne voit pas ce qui est ajouté à l'exécution |
| **Contrôle de configuration** | OpenSCAP · outils natifs de politique · Ansible | Libre · inclus | Référentiels génériques inadaptés aux applications métier |
| **Posture cloud** | Modules natifs des fournisseurs · solutions tierces | À la consommation · par ressource | Multi-cloud = dispositifs multiples à maintenir |
| **Gestion de secrets** | HashiCorp Vault · coffres natifs des fournisseurs | Libre · à la consommation | Devient un actif de niveau 0 · rotation à répercuter |
| **Inventaire / CMDB** | Modules ITSM · GLPI · solutions CAASM | Par actif · libre | Vaut ce que valent ses sources |
| **Ticketing / workflow** | Jira · GLPI · modules ITSM | Par utilisateur | Ne règle ni l'absence de propriétaire ni la capacité |
| **Journalisation** | Solutions SIEM · piles ouvertes (OpenSearch, Loki) | Par volume ingéré · libre | Le coût croît avec la rétention — arbitrage à faire tôt |
| **Découverte industrielle** | Solutions d'écoute passive OT | Sur devis | Ne voit que ce qui communique |

### E.3 Critères de sélection, par ordre d'importance

1. **Exportabilité des données brutes** et de l'historique en format ouvert — le critère décisif à cinq ans (§19.1).
2. Capacité à calculer la couverture sur **votre** périmètre de référence, pas sur le sien.
3. Granularité de ciblage : anneaux, exclusions documentées, populations.
4. Couverture réelle des applications tierces et des composants intermédiaires.
5. Fonctionnement hors réseau interne.
6. Coût total : licence **plus** intégration **plus** exploitation.

---

## Annexe F — Cadre réglementaire et normatif comparatif

> ⏱ **Annexe versionnée — vérifiée le 30 juillet 2026.** Les statuts évoluent ; revérifier à chaque revue.

| Texte | Qui est concerné | Exigence MCS principale | Preuve attendue | Statut au 30/07/2026 |
|---|---|---|---|---|
| **NIS2** (directive UE) | Entités essentielles et importantes, par secteur et taille | Gestion des risques, dont vulnérabilités et correctifs | Politique, inventaire, mesure, incidents | Transposition française **non promulguée** ; dossier législatif ouvert |
| **ReCyF** (ANSSI) | Entités visées par la transposition | Une vingtaine d'objectifs, avec moyens acceptables de conformité et proportionnalité | Analyse d'écart, preuve par objectif | **Version de travail** du 17/03/2026 — non opposable |
| **Cyber Resilience Act** — règlement (UE) 2024/2847 | **Fabricants** de produits à éléments numériques (voir aussi importateurs, distributeurs, art. 19-20) | **Art. 13** : gestion des vulnérabilités, période de support, inventaire des composants · **Art. 14** : signalement · **Art. 16** : plateforme unique · **Art. 69** : régime transitoire | Documentation technique, avis publiés, notifications via la plateforme | En vigueur (10/12/2024) · chapitre relatif aux organismes d'évaluation depuis le 11/06/2026 · **art. 14 à compter du 11/09/2026** · application générale au 11/12/2027 [S-04] [S-05] [S-06] |
| **ISO/IEC 27001 / 27002** | Volontaire, souvent exigé par les clients | Gestion des vulnérabilités techniques, des configurations, des changements | Processus documenté + preuve d'application sur échantillon | Version 2022 en vigueur |
| **IEC 62443** | Systèmes industriels : exploitants, intégrateurs, fabricants | Gestion des correctifs adaptée au contexte industriel, zones et conduits | Plan de MCS industriel, répartition des rôles | Série en vigueur |
| **Hébergement de données de santé** | Hébergeurs, et clients par ricochet | Maintien et traçabilité, obligations contractuelles | Certification, rapports | En vigueur |
| **SecNumCloud** | Fournisseurs cloud pour usages sensibles | Exigences détaillées de MCS et de transparence client | Qualification, rapports | En vigueur — vérifier la version applicable |
| **PCI DSS** | Traitement de données de paiement | Le plus prescriptif : délais chiffrés, scans périodiques internes et externes | Rapports de scan, journaux de correction | Version 4.x en vigueur |
| **DORA** | Secteur financier européen | Gestion du risque informatique, tests, maîtrise des tiers critiques | Registre des prestataires, tests, incidents | En vigueur |
| **RGPD art. 32** | Tout responsable de traitement | Mesures appropriées à l'état de l'art | Traçabilité des décisions et des écarts | En vigueur |
| **BOD 26-04 (CISA)** | **Agences civiles fédérales américaines uniquement** | Priorisation par le risque, délais différenciés | — | Publiée le 10/06/2026. **Modèle méthodologique, aucune obligation en Europe** |

**Ce qui reste incertain au 30/07/2026** : le calendrier de promulgation du texte français de transposition · la version définitive du ReCyF et l'éventuelle évolution de ses objectifs · les modalités pratiques d'exercice des obligations de signalement produit.

---

## Annexe G — Catalogue des faux positifs, pièges et illusions

*Classé par domaine. Pour chacun : le mécanisme, et le contrôle qui le détecte.*

### G.1 Scan et détection

| # | Piège | Mécanisme | Détection |
|---|---|---|---|
| 1 | Faux positif de rétroportage | Le numéro amont ne bouge pas | Comparer la révision éditeur + avis de la distribution |
| 2 | Service installé mais désactivé | Présence ≠ exécution | Vérifier l'état d'activation |
| 3 | Composant non chargé | Dépendance déclarée, jamais appelée | Atteignabilité, déclaration du fournisseur |
| 4 | Bannière modifiée | Version annoncée fausse | Scan authentifié |
| 5 | Correspondance produit erronée | Nomenclatures divergentes | Table de correspondance maintenue |
| 6 | Doublon agent / scan réseau | Deux sources, un actif | Identifiant pivot |
| 7 | Constat sur actif décommissionné | Nettoyage non fait | Réconciliation d'inventaire |
| 8 | Adresse réattribuée | L'actif détecté n'est pas le vôtre | Réconciliation |
| 9 | Constat sur image de base déjà corrigé | Analyse de la mauvaise couche | Analyser l'image finale |
| 10 | Base de détection périmée | L'outil ne sait pas chercher | Suivre l'âge du contenu |
| 11 | **« Non scanné » lu comme « non vulnérable »** | Trois états identiques dans un rapport | Les trois questions du §15.8 |
| 12 | Exclusion silencieuse | Actif retiré « temporairement » | Registre des exclusions revu en comité |

### G.2 Triage et pilotage

| # | Piège | Mécanisme |
|---|---|---|
| 13 | Seuil de gravité seul | Ignore exposition et exploitation |
| 14 | Score composite pondéré | Pondérations indéfendables ; bloque si une entrée manque |
| 15 | Discontinuité de modèle de score | Tous les scores bougent sans qu'aucun correctif ne soit appliqué |
| 16 | Dépriorisation sans date de revue | Devient un oubli |
| 17 | Faux positif déclaré sans preuve | Vide la file sans travailler |
| 18 | Constat ouvert depuis 6 mois | Dérogation non formalisée, décidée par personne |
| 19 | Compter les vulnérabilités fermées | Récompense l'agitation, pas le résultat |

### G.3 Déploiement

| # | Piège | Mécanisme |
|---|---|---|
| 20 | Correctif installé, service non redémarré | Code vulnérable toujours en mémoire |
| 21 | Correctif en mode observation jamais activé | Protection incomplète, croyance complète |
| 22 | Anneau pilote non représentatif | Valide l'installation, pas la non-régression |
| 23 | Critères d'arrêt discutés pendant l'incident | Toujours interprétés « on continue » |
| 24 | Retour arrière jamais testé | Une intention, pas un plan |
| 25 | Point de non-retour non identifié | Migration de schéma franchie sans le savoir |
| 26 | Traîne longue non qualifiée | Les 3 % les plus risqués |
| 27 | Recette non représentative | Fausse confiance, pire que pas de test |

### G.4 Configuration et identités

| # | Piège | Mécanisme |
|---|---|---|
| 28 | Référentiel appliqué sans dérivation | Contrôles désactivés un par un, baseline fictive |
| 29 | Contrôle désactivé pendant un incident | Jamais reversé |
| 30 | Rotation non répercutée | Ancien secret toujours valide |
| 31 | Autorisation déléguée | Survit au changement de mot de passe |
| 32 | Compte de service partagé | Une compromission se propage |
| 33 | Compte de secours non testé | Ne fonctionnera pas le jour venu |
| 34 | Certificat interne oublié | Expiration = panne difficile à diagnostiquer |

### G.5 Périmètre et couverture

| # | Piège | Mécanisme |
|---|---|---|
| 35 | Taux calculé sur les actifs connus | Biaisé **dans le sens favorable** |
| 36 | Actif déclaré, actif, hors outil de gestion | Tout le monde le croit géré |
| 37 | Machine éteinte non décommissionnée | Comptes et enregistrements survivants |
| 38 | Agent absent | La machine n'apparaît pas comme non conforme, elle n'apparaît plus |
| 39 | Additionner les rapports de plusieurs outils | Périmètres recouvrants, définitions divergentes |
| 40 | Actif éphémère | Absent des inventaires réseau |

### G.6 Contractuel et fournisseurs

| # | Piège | Mécanisme |
|---|---|---|
| 41 | SLA de disponibilité seul | Pousse structurellement au report des correctifs |
| 42 | Éligibilité au support étendu supposée | Programme grand public ≠ parc géré |
| 43 | Prérequis de version imposé par un éditeur | Vous héritez de son calendrier |
| 44 | Accès prestataire permanent | Exposition permanente |
| 45 | Déclaration fournisseur sans donnée | Confiance, pas preuve |

### G.7 Industriel, cloud, services en ligne, produit

| # | Piège | Mécanisme |
|---|---|---|
| 46 | Scan actif sur réseau industriel | Défaut d'automate, perte durable de confiance |
| 47 | Support amovible du prestataire | Vecteur d'entrée historique |
| 48 | Pièce de rechange non prépatchée | Remise en service en version ancienne |
| 49 | Version de service managé hors référentiel d'obsolescence | Migration subie |
| 50 | Fonctionnalité activée par défaut par le fournisseur | Exposition élargie sans décision |
| 51 | « C'est du SaaS, c'est maintenu » | Configuration, identités, intégrations restent à vous |
| 52 | Correctif produit publié sans mesure d'adoption | Le risque client ne diminue pas |
| 53 | Qualification réglementaire par gamme | Un produit exclu masque des produits inclus |

---

## Annexe H — Calendrier des échéances et ressources

> ⏱ **Annexe versionnée — vérifiée le 30 juillet 2026.** C'est l'annexe la plus périssable du document.

### H.1 Échéances datées

| Date | Objet |
|---|---|
| 14/10/2025 | Fin de support de Windows 10 |
| 15/04/2026 | Priorisation de l'enrichissement des fiches du NVD par le NIST |
| 11/06/2026 | Applicabilité du chapitre du CRA relatif aux organismes d'évaluation de la conformité |
| 15/06/2026 | Début de publication des scores EPSS v5 — **rupture de série** |
| 24 et 27/06/2026 | Expiration des certificats de démarrage sécurisé émis en 2011 (KEK CA, UEFI CA) |
| 11/09/2026 | Applicabilité des obligations de signalement du CRA |
| 13/10/2026 | Fin de support de Windows 10 Entreprise / IoT LTSB 2016 |
| 19/10/2026 | Expiration du certificat Windows Production PCA 2011 |
| 12/01/2027 | Fin de support étendu de Windows Server 2016 |
| 12/10/2027 | Fin du programme de support étendu **grand public** de Windows 10 — **exclut les machines gérées** |
| 11/12/2027 | Application générale du CRA |

### H.2 Échéances récurrentes sans date fixe

*À intégrer au référentiel d'obsolescence (§12.2), avec vérification à la source.*

| Objet | Cycle typique |
|---|---|
| Distributions Linux à support long | 5 à 10 ans, prolongations par abonnement |
| Moteurs de bases de données | 5 à 8 ans (versions majeures) |
| **Environnements d'exécution applicatifs** | **2 à 4 ans** — principale source d'obsolescence invisible |
| Versions d'orchestrateur de conteneurs | ~14 mois (12 standard + 2 limités) |
| Services managés cloud | Variable, annoncé plusieurs mois à l'avance |
| Équipements réseau — fin de support **de sécurité** | Souvent antérieure de plusieurs années à la fin de vie matérielle |
| Micrologiciels serveurs | 5 à 7 ans après commercialisation |
| Certificats publics | Durées en réduction progressive |

### H.3 Sources de veille et cadence

| Source | Cadence | Usage |
|---|---|---|
| Avis des éditeurs de vos produits C1 | Quotidienne | **Source de vérité** sur les versions |
| Avis des distributions | Quotidienne | Révisions rétroportées |
| Bulletins des centres de réponse nationaux | Quotidienne | Point d'entrée principal |
| Centres de réponse et communautés sectoriels | Hebdomadaire | Ciblage de votre secteur |
| Catalogues d'exploitation avérée | Quotidienne | Déclencheur d'urgence |
| Bases agrégées | Quotidienne | Couverture |
| **Notes de version des services cloud et en ligne** | **Mensuelle** | La ligne la plus faible de la plupart des dispositifs |
| Pages de cycle de vie des éditeurs | Trimestrielle | Référentiel d'obsolescence |
| Publications des agences nationales | Mensuelle | Doctrine, guides, référentiels |

### H.4 Formations et certifications

*Aucune certification ne porte spécifiquement sur le MCS. Les plus utiles au regard de ce cours :*

| Domaine | Utilité réelle |
|---|---|
| Management de la sécurité de l'information | Utile pour la partie gouvernance, preuve et audit |
| Sécurité industrielle | Indispensable si votre périmètre comprend de l'OT |
| Administration système et cloud | Le socle technique des chapitres 2, 3, 30 |
| Gestion des vulnérabilités (certifications éditeurs) | Utile sur l'outil, peu transférable |
| Analyse de risque (méthodes reconnues) | Utile pour la criticité et l'acceptation de risque |

⚠️ Une certification atteste d'une connaissance, pas d'une pratique. Les compétences réellement déterminantes de ce cours — négocier une fenêtre, obtenir un propriétaire, écrire une dérogation défendable — ne s'enseignent pas en formation.

### H.5 Ressources et communautés

Publications des agences nationales de cybersécurité · centres de réponse aux incidents nationaux et sectoriels · groupements professionnels de RSSI · communautés d'utilisateurs de vos outils · conférences sécurité généralistes et sectorielles · publications des éditeurs sur les incidents et les retours d'expérience.

---

## Annexe I — Modèle de données MCS

> Modèle relationnel minimal. Types : `str` texte · `enum` valeur contrôlée · `date` · `bool` · `ref` référence · `int`. Cardinalité : `1` obligatoire unique · `0..1` optionnel · `0..n` multiple.

### I.1 Entité ACTIF

| Champ | Type | Card. | Valeurs contrôlées / format | Obligatoire à la création |
|---|---|---|---|---|
| `id_actif` | str | 1 | Identifiant interne stable, **jamais réutilisé** | Oui |
| `ids_sources` | str | 0..n | `{source}:{identifiant natif}` — un par outil | Non |
| `nom` | str | 1 | Nom d'usage | Oui |
| `type` | enum | 1 | serveur · poste · mobile · réseau · sécurité · hyperviseur · conteneur · industriel · périphérique · service_en_ligne · identité_applicative · certificat | Oui |
| `proprietaire_metier` | ref | 0..1 | Personne ou rôle géré | Non — un actif découvert s'enregistre **sans** propriétaire |
| `suppleant_metier` | ref | 0..1 | | Non |
| `proprietaire_technique` | ref | 0..1 | | Non |
| `suppleant_technique` | ref | 0..1 | | Non |
| `criticite` | enum | 0..1 | C1 · C2 · C3 · C4 | Non |
| `exposition` | enum | 0..1 | internet · bureautique · administration · industriel · isolé · inconnue | Non |
| `environnement` | enum | 1 | production · recette · développement · laboratoire · formation · secours | Oui |
| `classification_donnees` | enum | 0..1 | publique · interne · confidentielle · sensible | Non |
| `perimetre_reglementaire` | enum | 0..n | santé · paiement · industriel · produit · aucun | Non |
| `systeme` / `version` | str | 0..1 | | Non |
| `composants` | ref | 0..n | → COMPOSANT | Non |
| `statut_support` | enum | 0..1 | supporté · support_étendu · hors_support · inconnu | Non |
| `date_fin_support` | date | 0..1 | | Non |
| `source_fin_support` | str | 0..1 | Référence + date de consultation | Si `date_fin_support` renseignée |
| `fournisseur` / `contrat` | ref | 0..1 | | Non |
| `fenetre_maintenance` | str | 0..1 | Expression récurrente | Non |
| `outils_couverture` | ref | 0..n | → OUTIL, avec rôle (déploiement / scan / protection / sauvegarde) | Non |
| **`first_seen`** | date | 1 | Première observation, toutes sources | Oui (automatique) |
| **`last_seen`** | date | 1 | Dernière observation | Oui (automatique) |
| **`confiance`** | enum | 1 | confirmée · probable · à_vérifier | Oui |
| **`source_decouverte`** | enum | 1 | cmdb · annuaire · scan · agent · hyperviseur · api_cloud · orchestrateur · comptabilité · déclaration · manuel | Oui |
| **`statut_cycle_vie`** | enum | 1 | découvert · en_service · orphelin · en_extinction · décommissionné | Oui |
| `motif_disparition` | enum | 0..1 | décommissionné · renommé · migré · perdu_de_vue · doublon | Si statut = décommissionné |
| `derniere_tentative_scan` | date | 0..1 | | Non |
| `dernier_succes_scan` | date | 0..1 | **Distinct du précédent** | Non |
| `derniere_preuve_conformite` | ref | 0..1 | → PREUVE | Non |
| `derogations_en_cours` | ref | 0..n | → DEROGATION | Non |

⚠️ **Aucun champ de propriété n'est obligatoire à la création.** Un actif découvert sans propriétaire doit pouvoir être enregistré avec `statut_cycle_vie = orphelin` — le rejeter par contrainte de champ obligatoire revient à effacer précisément ce qu'on cherche à découvrir.

### I.2 Entités liées

| Entité | Champs clés |
|---|---|
| **COMPOSANT** | `id` · `actif` (ref) · `type` (base_de_données / runtime / serveur_applicatif / bibliothèque / micrologiciel / pilote) · `nom` · `version` · `statut_support` · `date_fin_support` · `proprietaire_couche` (ref) |
| **CONSTAT** | `id` · `origine` (scan / avis / pentest / audit / incident / bug_bounty / configuration / secret / architecture) · `identifiant_externe` (0..1) · `statut_qualification` · `actifs` (0..n) · `decision_triage` · `horloge_risque_debut` · `horloge_sla_debut` · `temps_suspendu` |
| **DEROGATION** | Les champs de D.4 · `actifs` (0..n) · `nb_renouvellements` · `signataire` · `date_expiration` |
| **PREUVE** | `id` · `type` (état_constaté / rapport_console / journal / attestation) · `date_collecte` · `perimetre` · `methode` · `actifs_non_joignables` · `empreinte` |
| **OUTIL** | `id` · `nom` · `role` · `perimetre_theorique` · `date_derniere_extraction` · `format_export` |
| **CONTRAT** | `id` · `fournisseur` · `perimetre` · `delais_engages` · `restitution_donnees` (bool) · `date_echeance` |

### I.3 Relations

| Relation | Cardinalité |
|---|---|
| ACTIF `dépend de` ACTIF | 0..n |
| ACTIF `est construit depuis` MODELE | 0..1 |
| ACTIF `est couvert par` OUTIL | 0..n, avec rôle |
| ACTIF `porte` COMPOSANT | 0..n |
| ACTIF `utilise` COMPTE | 0..n |
| CONSTAT `affecte` ACTIF | 1..n |
| DEROGATION `couvre` CONSTAT | 1..n |
| PREUVE `atteste` ACTIF `pour` CONSTAT | 1..n |

### I.4 Périmètre maître et populations éligibles

Le périmètre de référence est le **périmètre maître** : l'union de tout ce qui est connu.

```
Périmètre maître = ∪ (toutes les sources d'inventaire)
   incluant : actifs orphelins · actifs en extinction · actifs de service
   excluant : rien — les exclusions sont documentées, jamais retirées
```

⚠️ **Le périmètre maître n'est pas le dénominateur de tout indicateur.** Un service en ligne n'est pas éligible à un indicateur de correctif système ; un automate n'est pas éligible au scan actif ; un actif arrêté en cours de décommissionnement n'est pas éligible à la conformité aux correctifs ; un certificat ne s'évalue pas avec les contrôles d'un serveur. Utiliser le périmètre maître comme dénominateur universel produit des taux artificiellement bas et indéfendables.

| Notion | Définition | Champ correspondant |
|---|---|---|
| **Périmètre maître** | Tout ce qui est connu, sans exclusion silencieuse | tous les ACTIF |
| **Population éligible** | Sous-ensemble auquel le contrôle **s'applique** | filtre explicite par indicateur |
| **Population mesurée** | Actifs éligibles effectivement évalués | `dernier_succes_scan` renseigné |
| **N/A** | Hors population éligible, **avec motif** | `motif_na` |
| **Non mesuré** | Éligible mais non évalué. **Jamais conforme par défaut** | éligible ∧ `dernier_succes_scan` vide |

### I.5 Règles de qualité et contrôles

| # | Règle | Requête | Fréquence |
|---|---|---|---|
| 1 | Aucun actif en service sans deux propriétaires | `statut = en_service ∧ (prop_metier vide ∨ prop_tech vide)` | Mensuelle |
| 2 | Aucun actif en service sans criticité ni exposition | `statut = en_service ∧ (criticite vide ∨ exposition vide)` | Mensuelle |
| 3 | Date de fin de support renseignée ou motif | `date_fin_support vide ∧ motif vide` | Trimestrielle |
| 4 | Couverture ou exclusion documentée | `outils_couverture vide ∧ exclusion vide` | Mensuelle |
| 5 | Actif décommissionné avec PV | `statut = décommissionné ∧ pv vide` | Trimestrielle |
| 6 | Actif non revu depuis N jours | `last_seen < aujourd'hui - 90` | Mensuelle |
| 7 | Écart entre sources supérieur au seuil | Réconciliation (§10.3) | Mensuelle |
| 8 | Orphelin depuis plus de 30 jours | `statut = orphelin ∧ first_seen < -30 j` | Mensuelle |

### I.6 Exemple d'enregistrement

```yaml
id_actif: SRV-0142
ids_sources: [cmdb:CI00873, scan:asset-51190, hyperviseur:vm-2201]
nom: srv-app-crm-02
type: serveur
proprietaire_metier: directeur.commercial
proprietaire_technique: m.ferhaoui
criticite: C2
exposition: bureautique
environnement: production
classification_donnees: confidentielle
systeme: "Linux LTS 12"
version: "12.7"
composants:
  - {type: runtime, nom: "runtime applicatif A", version: "8.3", statut_support: hors_support,
     date_fin_support: 2023-03-31, proprietaire_couche: equipe.applicative}
statut_support: supporté
date_fin_support: 2028-06-30
source_fin_support: "page officielle éditeur, consultée le 30/07/2026"
first_seen: 2019-04-11
last_seen: 2026-07-29
confiance: confirmée
source_decouverte: cmdb
statut_cycle_vie: en_service
dernier_succes_scan: 2026-07-28
derogations_en_cours: [DER-2027-014]
```

---

## Annexe J — Workflow et modèle de ticket de remédiation

### J.1 États et transitions

```
NOUVEAU ──qualification──► QUALIFIÉ ──────► FAUX POSITIF (clos + démonstration)
                              │
                         triage (§16.3)
                              ▼
                          AFFECTÉ ◄──────► CONFLIT DE PROPRIÉTÉ (délai borné)
                              │                      │
                      acceptation propriétaire       └──► arbitrage comité
                              ▼
                          PLANIFIÉ ────────► DÉROGATION (ouvert, D.4)
                              │              RISQUE ACCEPTÉ (ouvert, durable)
                              ▼              N/A (clos, motif)
                       EN CORRECTION
                              ▼
                        À VÉRIFIER ────────► ÉCHEC ──► retour à PLANIFIÉ
                              ▼
                            CLOS ◄────────── NOUVELLE OCCURRENCE (ticket lié)
```

### J.2 Droits de transition

| Transition | Qui peut la déclencher |
|---|---|
| Nouveau → Qualifié | Analyste sécurité |
| Qualifié → Faux positif | Analyste sécurité, **avec démonstration jointe** |
| Qualifié → Affecté | Automatique, depuis le propriétaire d'actif |
| Affecté → Conflit de propriété | Propriétaire désigné, sous 5 j ouvrés |
| Conflit → Affecté | Comité MCS uniquement |
| Planifié → Dérogation | Propriétaire métier (signature D.4) |
| Planifié → Risque accepté | Selon grille C.4 |
| À vérifier → Clos | **Seulement avec preuve rattachée** |
| Clos → réouverture | Interdite : créer une **nouvelle occurrence liée** (J.6) |

### J.3 Champs obligatoires par état

| État | Exigences |
|---|---|
| Qualifié | Statut de qualification · actifs confirmés · vérification d'activation · **origine du constat** |
| Affecté | Propriétaire nominatif · échéance SLA · **chemin dans l'arbre reproduit** |
| Planifié | Fenêtre ou campagne · plan de retour arrière (D.7) |
| En correction | Date de début · intervenant |
| À vérifier | Date d'action · méthode de vérification prévue |
| Clos | **Preuve** conforme aux six champs du §2.9 |
| Dérogation | Les champs de D.4 |
| Risque accepté | Signataire selon C.4 · date de revue · **pas de date d'expiration** (c'est ce qui le distingue de la dérogation) |
| N/A | Motif documenté · population éligible d'origine |

### J.4 Les deux horloges

| Élément | Règle |
|---|---|
| **Horloge de risque** | Départ : connaissance pertinente ou disponibilité d'une correction. **Ne se suspend jamais.** Publiée à la direction |
| **Horloge de traitement (SLA)** | Même départ, suspensions limitativement définies. Pilote l'équipe |
| Compteur complémentaire | Depuis la **détection** → réactivité de la veille |
| Suspensions admises (SLA uniquement) | Attente de correctif éditeur · attente d'information demandée par écrit · gel de production |
| Condition d'une suspension > 5 j | **Mesure compensatoire engagée ou acceptation formelle** |
| Temps suspendu | **Mesuré et affiché séparément** |
| Écart entre les deux horloges | Indicateur de premier plan : sa croissance signale un problème structurel |

### J.5 Règles de déduplication et modèle parent / enfants

| Règle | Application |
|---|---|
| Même identifiant sur plusieurs actifs | **Un** ticket parent, une occurrence enfant par actif |
| Constats corrigés par le **même correctif** | Un ticket parent |
| Même constat remonté par deux outils | Un ticket, deux sources tracées |
| Actifs de propriétaires, fenêtres ou criticités différents | **Occurrences enfants distinctes**, avec leurs propres échéances |

⚠️ Le parent porte la décision de triage et la cause racine ; **les enfants portent l'échéance, le propriétaire et la preuve**. Un parent ne se clôt que lorsque toutes ses occurrences sont closes ou qualifiées.

### J.6 Réouverture ou nouvelle occurrence

| Situation | Traitement |
|---|---|
| Le constat n'avait jamais été réellement corrigé | **Réouverture** de l'occurrence : le délai continue de courir |
| Le constat réapparaît après une correction vérifiée | **Nouvelle occurrence**, liée au ticket parent et à l'occurrence précédente |

Le second cas préserve la justesse des indicateurs de délai tout en rendant la **récurrence visible** : trois occurrences liées sur le même parent signalent une cause racine non traitée (§17.9), presque toujours un modèle ou une image de référence.

### J.7 Escalade — paramétrable par classe

| Déclencheur | C1 | C2 | C3 | Destinataire |
|---|---|---|---|---|
| Pas de réponse du propriétaire | 2 j | 5 j | 10 j | Responsable hiérarchique |
| Conflit de propriété non résolu | 3 j | 5 j | 10 j | Comité MCS |
| Échéance SLA dépassée | Immédiat | 5 j | 15 j | Comité MCS |
| Suspension prolongée | 10 j | 20 j | 30 j | Comité MCS |
| Constat non qualifié depuis | 90 j | 180 j | 180 j | **DSI — requalification obligatoire** |

### J.8 Issues et preuve exigée

| Issue | Nature | Preuve |
|---|---|---|
| **Corrigé** | Définitive | État constaté postérieur à l'action |
| **Atténué** | Temporaire | Mesure décrite, vérifiée active, **date d'expiration** |
| **Dérogation** | Temporaire, bornée | Fiche D.4 signée |
| **Risque accepté** | Durable | Signature C.4, revue périodique, **horloge de risque toujours active** |
| **N/A** | Définitive | Motif et population éligible d'origine |
| **Faux positif** | Définitive | **Démonstration vérifiable par un tiers** |
| **Sans objet** | Définitive | PV de décommissionnement (D.14) |

---

## Annexe K — Dictionnaire d'indicateurs et modèle de maturité

### K.1 Fiches d'indicateurs

*Format complet : formule · numérateur · **population éligible** · dénominateur publié · période · exclusions et N/A · source · propriétaire · fréquence · seuils.*

⚠️ La population éligible se définit **par indicateur** (Annexe I.4). Le périmètre maître est le point de départ, jamais le dénominateur par défaut.

---

**K1 — Couverture d'inventaire**
Formule : `actifs identifiés / actifs estimés du périmètre × 100` · Numérateur : actifs enregistrés · Population éligible : tous types · Dénominateur : estimation argumentée du parc réel · Période : instantané mensuel · Exclusions : aucune · Source : réconciliation multi-sources · Propriétaire : exploitation · Seuils : `< 90 %` alerte, `< 80 %` blocage de tout autre indicateur.

**K2 — Couverture de scan**
Formule : `actifs scannés avec succès / actifs éligibles au scan × 100` · Numérateur : `dernier_succes_scan` dans la période · **Population éligible : actifs scannables** — exclut services en ligne, industriels non scannables, certificats · Dénominateur : population éligible, publié · Exclusions : documentées, listées avec l'indicateur · N/A : motif obligatoire · Fréquence : mensuelle · Seuils : `< 90 %` alerte.

**K3 — Conformité de correctifs**
Formule : `actifs conformes / actifs mesurés × 100` · **Population éligible** : actifs porteurs du composant concerné · Trois valeurs à publier ensemble : conformité dans la population mesurée · **ratio confirmé conforme sur périmètre** (K3 × K2) · **part non mesurée** · Fréquence : mensuelle.

**K4 — Respect des délais**
Formule : `constats clos dans le délai / constats arrivés à échéance × 100` · Population éligible : constats avec échéance SLA dans la période · Exclusions : suspendus — **mais leur horloge de risque reste publiée** · Publier : médiane, **P90**, maximum, volume · Seuils : `< 85 %` alerte.

**K5 — Âge du backlog**
Formule : distribution des durées depuis la première détection · Publier : **médiane · P90 · P95 · maximum · volume de population** · Population éligible : constats ouverts · Piège : la moyenne masque la traîne, le maximum peut être dominé par un cas aberrant.

**K6 — Dette critique échue**
Formule : nombre absolu de constats critiques dont le délai est dépassé · **Jamais en taux** · Population éligible : constats de gravité critique · Fréquence : hebdomadaire · Seuil : toute valeur `> 0` sur actif exposé déclenche une revue.

**K7 — Dérogations**
Trois valeurs : nombre ouvert · **âge moyen et P90** · **nombre renouvelées ≥ 1 fois** · Le nombre seul n'est pas interprétable (§38.9) · Fréquence : mensuelle · Seuil : toute dérogation renouvelée deux fois remonte en comité de direction.

**K8 — Taux de récurrence**
Formule : `occurrences réapparues / occurrences closes sur la période × 100` · Population éligible : occurrences closes il y a plus de 30 jours · Interprétation : signale une cause racine (modèle, image, restauration), pas une mauvaise exécution · Seuil : `> 10 %` déclenche une analyse de cause racine.

**K9 — Taux de retour arrière**
Formule : `déploiements annulés / déploiements réalisés × 100` · Piège : un taux **nul** peut signaler qu'on ne teste pas ou qu'on n'ose pas revenir en arrière · Seuils : `> 10 %` qualité de validation insuffisante ; `= 0 %` sur 12 mois, examiner.

**K10 — Taux d'échec de déploiement**
Formule : `actifs en échec / actifs ciblés × 100` · **Les non-joignables comptent au dénominateur** et sont publiés séparément · Fréquence : par campagne.

**Indicateurs complémentaires** : âge des images et modèles · temps sans redémarrage (P90) · part de changements d'urgence (seuil 15-20 %) · fraîcheur du contenu de détection · nombre d'actifs exposés et tendance · nombre d'orphelins · part des technologies couvertes par une source de veille · âge des exclusions · **écart entre horloge de risque et horloge SLA**.

### K.2 Règles de publication

1. Tout taux est publié **avec son dénominateur, sa population éligible et sa date**.
2. Les populations non mesurées apparaissent comme **« non mesuré »**, jamais comme conformes ni comme absentes.
3. Les exclusions et les N/A sont listés avec l'indicateur, avec leur motif.
4. Les ruptures — périmètre, outil, modèle de score — sont **marquées sur la série**. Lorsque c'est possible, recalculer la période de transition avec l'ancien et le nouveau modèle et publier les deux.
5. Les délais se publient en **médiane, P90 ou P95, maximum et volume**.
6. Le nombre d'indicateurs est **inversement proportionnel** au niveau hiérarchique.
7. Un produit *conformité × couverture* est un **ratio conservateur**, nommé comme tel.
8. Le temps suspendu au titre du SLA reste compté par **l'horloge de risque**.

### K.3 Modèle de maturité — critères de preuve par niveau

| Niveau | Nom | **Preuve exigée pour l'atteindre** |
|---|---|---|
| 0 | Inexistant | — |
| 1 | Réactif | Traces de corrections réalisées, sans processus documenté |
| 2 | Documenté | Politique approuvée · inventaire constitué et daté · propriétaires nommés sur ≥ 80 % du périmètre |
| 3 | Piloté | Délais définis **et mesurés** · registre de dérogations tenu · indicateurs publiés avec dénominateurs · comptes rendus de comité avec décisions |
| 4 | Industrialisé | Automatisation de la collecte, corrélation et vérification · campagnes tracées avec critères d'arrêt · **preuve d'état sur échantillon produite systématiquement** |
| 5 | Adaptatif | Priorisation par exposition et exploitation documentée · MCS *by design* en revue d'architecture · boucle d'amélioration démontrée sur ≥ 4 trimestres · audit interne par sondages |

### K.4 Grille d'auto-évaluation par domaine

| Domaine | Niveau | Preuve citée | Facteur limitant ? |
|---|---|---|---|
| Inventaire et périmètre | `[0-5]` | `[ ]` | `[ ]` |
| Exposition et chemins d'attaque | `[ ]` | `[ ]` | `[ ]` |
| Veille et sources de constats | `[ ]` | `[ ]` | `[ ]` |
| Triage et priorisation | `[ ]` | `[ ]` | `[ ]` |
| Remédiation et workflow | `[ ]` | `[ ]` | `[ ]` |
| Configuration et dérive | `[ ]` | `[ ]` | `[ ]` |
| Identités, secrets, certificats | `[ ]` | `[ ]` | `[ ]` |
| Applications et dépendances | `[ ]` | `[ ]` | `[ ]` |
| Obsolescence et décommissionnement | `[ ]` | `[ ]` | `[ ]` |
| Contextes spécialisés | `[ ]` | `[ ]` | `[ ]` |
| Mesure et preuve | `[ ]` | `[ ]` | `[ ]` |
| Gouvernance et financement | `[ ]` | `[ ]` | `[ ]` |

**Lecture** — Un niveau élevé dans dix domaines ne compense pas un niveau 1 sur l'inventaire : celui-ci **plafonne** la maturité de tout ce qui en dépend. Identifiez les domaines **critiques pour votre contexte** et traitez-les comme facteurs limitants ; la moyenne des douze notes n'a aucune valeur informative.

---

## Annexe L — Checklists de cycle de vie

### L.1 Mise en production
☐ Déclaré à l'inventaire · ☐ Deux propriétaires nommés · ☐ Criticité et exposition attribuées · ☐ Classe de service · ☐ Couvert par un outil de déploiement et de scan · ☐ Fenêtre définie · ☐ Journalisation activée et exportée · ☐ Sauvegarde configurée et testée · ☐ Grille de maintenabilité du §6.14 renseignée · ☐ Fin de support des composants connue.

### L.2 Campagne périodique
☐ Périmètre défini et rapproché du périmètre de référence · ☐ **Vérification préalable sur 3 actifs représentatifs** · ☐ Qualification du correctif en 6 questions · ☐ Écart recette/production mesuré · ☐ Anneaux définis · ☐ **Critères d'arrêt chiffrés, écrits** · ☐ Plan de retour arrière chronométré · ☐ Décideur nommé · ☐ Vérification post-déploiement · ☐ **Traîne longue qualifiée** · ☐ Preuve archivée.

### L.3 Correctif urgent
☐ Information vérifiée à la source · ☐ Exposition mesurée · ☐ **Réduction d'exposition envisagée en premier** · ☐ Cellule constituée avec greffier · ☐ Délai d'observation supprimé — **critères d'arrêt, retour arrière et preuve conservés** · ☐ Recherche de compromission préalable · ☐ Communication direction et métiers · ☐ Demande de changement régularisée sous 48 h · ☐ Retour d'expérience.

### L.4 Système non patchable
☐ Type d'impossibilité qualifié (5 types) · ☐ **Usage réel mesuré** · ☐ Hiérarchie des compensations parcourue de haut en bas · ☐ Compensation avec les 7 attributs · ☐ Dérogation signée par le propriétaire métier · ☐ Date d'expiration · ☐ Contrôle périodique inscrit au comité · ☐ Plan de fin de vie ou de remplacement.

### L.5 Mise à jour hors ligne (industriel)
☐ Source officielle, compte nominatif · ☐ Poste de téléchargement dédié et durci · ☐ **Vérification de signature ou d'empreinte** (double contrôle) · ☐ Analyse antimalware multi-moteurs (double contrôle) · ☐ Support dédié, effacé, identifié · ☐ Sas de transfert · ☐ Validation constructeur écrite · ☐ Matériel de secours prêt · ☐ Application selon procédure · ☐ Tests fonctionnels et de sûreté · ☐ **Preuve d'installation et journal de transfert**.

### L.6 Renouvellement de certificat
☐ Inventaire à jour · ☐ Alertes à 60/30/7 jours · ☐ Renouvellement automatisé si possible · ☐ Déploiement sur **tous** les points d'usage · ☐ Vérification du certificat effectivement présenté · ☐ Ancien certificat révoqué · ☐ Magasins de confiance mis à jour.

### L.7 Migration de version majeure
☐ Fin de support de la version source confirmée à la source · ☐ Compatibilité applicative validée par l'éditeur, **par écrit** · ☐ Recette représentative sur les 4 axes · ☐ Migration de schéma découpée en expansion/contraction · ☐ **Point de non-retour identifié et écrit** · ☐ Plan de retour arrière testé sur topologie représentative · ☐ Fenêtre et communication · ☐ Vérification fonctionnelle post-migration.

### L.8 Changement de fournisseur
☐ Clauses MCS du §13.3 dans le nouveau contrat · ☐ **Restitution de données obtenue** · ☐ Périmètre nominatif annexé · ☐ Inventaire et historique récupérés de l'ancien prestataire · ☐ Accès de l'ancien prestataire révoqués · ☐ Comptes et clés associés supprimés · ☐ Documentation d'exploitation transférée.

### L.9 Décommissionnement
☐ Usage réel mesuré · ☐ Décision et préavis · ☐ **Extinction avant suppression, observation ≥ 1 cycle métier** · ☐ Dépendances identifiées et traitées · ☐ Données migrées/archivées/effacées avec preuve · ☐ Enregistrements de noms supprimés · ☐ Règles de filtrage supprimées · ☐ **Comptes, clés, secrets, jetons, autorisations déléguées révoqués côté fournisseur** · ☐ Certificats révoqués · ☐ Retrait de tous les outils · ☐ Décision sur les sauvegardes, avec date · ☐ Matériel et licences traités · ☐ Contrats résiliés · ☐ **Vérification à J+90** · ☐ Procès-verbal signé par les deux propriétaires.

---

## Ce que vous savez faire

Un cours ne se juge pas à ce qu'il a exposé, mais à ce que son lecteur est capable de faire ensuite. Voici la liste, formulée en actes plutôt qu'en connaissances. Elle sert aussi de grille d'auto-évaluation avant une prise de poste ou un entretien.

### Vous savez établir un périmètre et le défendre

☐ Croiser quatre sources d'inventaire dont une non technique, et **interpréter les écarts** plutôt que choisir un chiffre
☐ Identifier les actifs orphelins et conduire une campagne de désignation de propriétaires
☐ Établir la carte des actifs réellement exposés, et fermer ce qui ne sert plus
☐ Nommer les actifs de niveau 0 de votre organisation — la liste tient sur une page
☐ Déclarer un périmètre non couvert **plutôt que de le laisser invisible**

### Vous savez décider

☐ Qualifier une information en fait vérifié, hypothèse probable ou piste exploratoire
☐ Écarter un faux positif de rétroportage avant de lancer une campagne de 42 serveurs
☐ Appliquer un arbre de décision, et **expliquer votre chemin** devant un comité qui conteste
☐ Défendre une dépriorisation, et savoir ce qui la distingue d'un oubli
☐ Reconnaître qu'un délai accordé par la politique est une ressource, et l'utiliser sans culpabilité

### Vous savez corriger sans casser

☐ Qualifier un correctif en six questions, en lisant les notes de version **en entier**
☐ Composer un anneau pilote qui teste l'usage réel, pas seulement l'installation
☐ Écrire des critères d'arrêt chiffrés **avant** l'intervention, avec un décideur nommé
☐ Identifier un point de non-retour et le déclarer dans la demande de changement
☐ Chronométrer un retour arrière sur une topologie représentative
☐ Qualifier une traîne longue au lieu de clore une campagne à 97 %

### Vous savez traiter ce qui ne se corrige pas

☐ Qualifier une impossibilité parmi ses cinq types, et identifier le bon interlocuteur
☐ Parcourir la hiérarchie des compensations de haut en bas, en écrivant pourquoi vous descendez
☐ Rédiger une dérogation avec ses sept champs, et la faire signer au bon niveau
☐ Vérifier, six mois plus tard, qu'une compensation est **encore active**

### Vous savez réagir

☐ Poser les trois questions qui déterminent si vous pouvez conclure quoi que ce soit
☐ Réduire une exposition en quinze minutes, avant même de parler de correctif
☐ Dire à une direction générale que vous ne pouvez pas établir l'absence de compromission
☐ Comprimer un processus en urgence sans supprimer les garde-fous qui permettent de se tromper
☐ Décider de reconstruire plutôt que corriger, sur un critère explicite

### Vous savez prouver et financer

☐ Publier un taux avec sa population éligible, son dénominateur et sa part non mesurée
☐ Distinguer une mesure d'un ratio conservateur, et nommer chacun correctement
☐ Constituer un dossier de preuves en continu, en onze pièces
☐ Répondre à six questions d'auditeur sans prétendre être conforme
☐ Construire un dossier d'investissement à trois options, dont le statu quo chiffré

### Vous savez ce que vous ne savez pas

C'est la compétence la plus difficile, et celle que ce cours travaille le plus.

☐ Reconnaître qu'un rapport à 100 % de conformité doit déclencher un examen, pas une satisfaction
☐ Identifier ce que votre journalisation ne vous permettra jamais d'établir
☐ Écrire « non mesuré » dans un tableau de bord plutôt que de laisser une case vide
☐ Nommer un risque non maîtrisé **avant** qu'il ne se réalise, dans une note à la direction

---

**Ce que ce cours ne vous a pas appris**, et qu'il faut aller chercher ailleurs : administrer un système, concevoir un réseau, développer une application, conduire une investigation numérique, plaider un dossier juridique. Le MCS s'appuie sur ces métiers ; il ne les remplace pas, et ce document ne prétend pas les enseigner (§2.10).

**Ce qui vous manquera encore après ce cours**, et que seule la pratique donne : le sens du moment où une négociation peut aboutir, la capacité à sentir qu'un chiffre est faux avant de savoir pourquoi, et la patience nécessaire pour obtenir en dix-huit mois ce qui paraissait évident dès le premier jour. Le fil rouge HELIOMED existe pour rendre cette durée sensible : trois ans, une centaine de décisions, et quatre écarts au dernier audit.

---

## Annexe M — Registre de sources

> ⏱ **Annexe versionnée — dernière vérification : 1er août 2026.**
> Chaque fait périssable du cours renvoie à une entrée de ce registre. Le **niveau de source** indique la force de la référence : `T` texte juridique · `D` documentation officielle de l'éditeur ou de l'organisme · `N` norme ou standard · `S` source secondaire (presse spécialisée, cabinet, analyse tierce).

### M.1 Comment lire une entrée

```
[S-nn]  Organisme — Titre exact du document ou de la page
        Version ou date de publication · Article, section ou contrôle précis
        Niveau : T / D / N / S · Vérifié le : jj/mm/aaaa
        Utilisé au : §x.y, annexe Z
```

### M.2 Réglementation européenne et française

**[S-01]** — Union européenne — *Directive (UE) 2022/2555 (NIS2)*
Niveau `T` · Vérifié le 30/07/2026 · Utilisé au §8.1, annexe F.
*Point de vigilance* : pour une entreprise privée, les obligations opérationnelles résultent principalement du droit national de transposition. Le statut exact doit être vérifié dans chaque juridiction.

**[S-02]** — République française — *Projet de loi relatif à la résilience des infrastructures critiques et au renforcement de la cybersécurité* — dossier législatif public
Niveau `T` · Vérifié le 30/07/2026 · **Non promulgué à cette date** · Utilisé au §8.1, §8.10, annexe F.
*À revérifier en priorité* : c'est le déclencheur de revue anticipée n° 1 du document.

**[S-03]** — ANSSI — *Référentiel d'exigences de cybersécurité (ReCyF)*
Version de travail du **17/03/2026** · Niveau `D` · Vérifié le 30/07/2026 · Utilisé au §8.2, §8.10, annexe F.
*Point de vigilance* : le document porte explicitement la mention « version de travail ». Il n'est pas opposable en l'état. Les numéros d'objectifs cités dans le cours doivent être revérifiés contre la version définitive.

**[S-04]** — Union européenne — *Règlement (UE) 2024/2847 relatif à des exigences horizontales de cybersécurité pour les produits comportant des éléments numériques (Cyber Resilience Act)*
Niveau `T` · Vérifié le 01/08/2026 · Articles utilisés :
- **art. 13** — exigences de gestion des vulnérabilités, applicable au 11/12/2027 → §33.7
- **art. 14** — obligations de signalement, applicable au 11/09/2026 → §33.5, §8.3
- **art. 16** — plateforme unique de signalement → §33.5
- **art. 69 §2 et §3** — régime transitoire des produits déjà mis sur le marché → §33.9
- annexes relatives à la documentation technique → §33.7

**[S-05]** — Commission européenne — *Cyber Resilience Act — Reporting obligations*, page officielle « Shaping Europe's digital future »
Niveau `D` · Vérifié le 01/08/2026 · Utilisé au §33.5, §33.9, annexe F.
*Contenu retenu* : applicabilité au 11/09/2026 · alerte précoce sous 24 h · notification sous 72 h · rapport final sous 14 jours après disponibilité d'une mesure corrective pour une vulnérabilité activement exploitée, sous un mois pour un incident grave.

**[S-06]** — Analyses juridiques concordantes sur la portée de l'article 14 et du régime transitoire de l'article 69
Niveau `S` · Vérifié le 01/08/2026 · Utilisé au §33.5, §33.6, §33.9.
*Usage* : ces sources secondaires confirment la lecture des articles et précisent que l'article 14 **n'impose pas** en lui-même la publication d'une politique de divulgation coordonnée, ni la tenue d'un inventaire de composants — obligations relevant de l'article 13. **Toute décision engageante doit être prise sur le texte [S-04], pas sur ces analyses.**

**[S-07]** — Union européenne — *Règlement (UE) 2016/679 (RGPD)*, article 32
Niveau `T` · Vérifié le 30/07/2026 · Utilisé au §8.6, annexe F.
*Point de vigilance* : les affirmations du cours sur la pratique des autorités de contrôle doivent être rattachées, dans votre contexte, aux **délibérations publiées** de l'autorité compétente. Le cours ne cite aucune décision particulière et présente une tendance, pas une règle.

**[S-08]** — Union européenne — *Règlement (UE) 2022/2554 (DORA)* · **[S-09]** — *Règlement (UE) 2017/745 (MDR)* et *2017/746 (IVDR)*
Niveau `T` · Vérifiés le 30/07/2026 · Utilisés au §8.5, §33.8, annexe F.

### M.3 Normes et référentiels

**[S-10]** — ISO/IEC 27001:2022 et ISO/IEC 27002:2022
Niveau `N` · Vérifié le 30/07/2026 · Contrôles utilisés au §8.4 :
- **8.8** — gestion des vulnérabilités techniques
- **8.9** — gestion des configurations
- **8.19** — installation de logiciels sur les systèmes en exploitation
- **8.32** — gestion des changements

**[S-11]** — Série IEC 62443 — sécurité des systèmes d'automatisation et de contrôle industriels
Niveau `N` · Vérifié le 30/07/2026 · Utilisé au §29.2, annexe F.
*Point de vigilance* : la série comporte plusieurs parties aux publics différents (exploitant, intégrateur, fabricant). Le cours en retient la logique de zones, conduits et répartition des rôles, sans citer de partie particulière.

**[S-12]** — PCI DSS, version 4.x · **[S-13]** — Référentiel HDS · **[S-14]** — Référentiel SecNumCloud
Niveau `N` · Vérifiés le 30/07/2026 · Utilisés au §8.5, annexe F.
*Point de vigilance* : pour chacun, la **version applicable** et les exigences précises doivent être identifiées selon votre périmètre. Le cours ne cite aucun numéro d'exigence.

**[S-15]** — ANSSI — référentiel relatif aux **prestataires d'administration et de maintenance sécurisées (PAMS)**
Niveau `D` · Vérifié le 30/07/2026 · Utilisé au §13.4.
*Point de vigilance* : **le statut du schéma de qualification et la liste des prestataires éventuellement qualifiés doivent être vérifiés directement sur le site de l'agence.** Une information périmée sur ce point peut orienter à tort un choix de prestataire.

### M.4 Écosystème des vulnérabilités

**[S-16]** — NIST — annonce relative à la **priorisation de l'enrichissement du NVD** à compter du **15/04/2026**
Niveau `D` · Vérifié le 30/07/2026 · Utilisé au §1.8, §4.9, §16.8.
*Formulation exacte à conserver* : toutes les vulnérabilités continuent d'être enregistrées ; c'est l'**enrichissement** — scores, correspondances produit, classification — qui devient sélectif, priorisé sur les vulnérabilités connues comme exploitées, les logiciels utilisés par l'administration fédérale américaine et les logiciels critiques. Les autres fiches peuvent porter la mention *Not Scheduled*.

**[S-17]** — FIRST — **EPSS**, documentation du modèle et calendrier de versions
Niveau `D` · Vérifié le 30/07/2026 · Utilisé au §4.5, §38.4, annexe H.
*Fait retenu* : la version 5 du modèle a commencé à publier ses scores le **15/06/2026** — date de **rupture de série** pour tout indicateur fondé sur un seuil de score.

**[S-18]** — FIRST — **CVSS v4.0**, spécification et guide d'utilisation
Niveau `N` · Vérifié le 30/07/2026 · Utilisé au §4.4, annexe C.
*Fait retenu* : la documentation du standard indique explicitement que CVSS mesure une **sévérité**, non un risque.

**[S-19]** — IETF — **RFC 9116**, *A File Format to Aid in Security Vulnerability Disclosure* (`security.txt`)
Niveau `N` · Vérifié le 01/08/2026 · Utilisé au §33.3.

**[S-20]** — CISA — **catalogue des vulnérabilités connues comme exploitées** · **[S-21]** — CISA — **BOD 26-04**, publiée le 10/06/2026
Niveau `D` · Vérifiés le 30/07/2026 · Utilisés au §4.6, §8.7.
*Point de vigilance majeur* : une directive opérationnelle contraignante de cette autorité s'impose **aux seules agences civiles fédérales américaines**. Elle constitue pour une organisation européenne un **modèle méthodologique**, jamais une obligation.

**[S-22]** — ENISA — **base européenne de vulnérabilités (EUVD)**
Niveau `D` · Vérifié le 30/07/2026 · Utilisé au §4.9, §14.4.

**[S-23]** — Formats d'inventaire et d'exploitabilité : **CycloneDX**, **SPDX**, **CSAF**, **VEX**
Niveau `N` · Vérifiés le 30/07/2026 · Utilisés au §4.8, §25.11, §25.19.

### M.5 Cycles de vie produits

**[S-24]** — Microsoft — pages officielles de **cycle de vie** et de **support étendu Windows 10**
Niveau `D` · Vérifiées le 30/07/2026 · Utilisées au §2.4, §12.4, §12.5, cas B, annexe H.
*Faits retenus* : fin de support de Windows 10 le **14/10/2025** · programme de support étendu **grand public** prolongé jusqu'au **12/10/2027**, **excluant explicitement les appareils joints à un annuaire d'entreprise ou gérés par une solution de gestion de flotte** · programme **commercial** distinct, payant, à tarif croissant · Windows 10 Entreprise/IoT LTSB 2016 le **13/10/2026** · Windows Server 2016 le **12/01/2027**.

**[S-25]** — Microsoft — documentation relative à l'**expiration des certificats de démarrage sécurisé** émis en 2011
Niveau `D` · Vérifiée le 30/07/2026 · Utilisée au §1.3, §3.8, annexe H.
*Faits retenus* : KEK CA 2011 le **24/06/2026** · UEFI CA 2011 le **27/06/2026** · Windows Production PCA 2011 le **19/10/2026** · remplacement par les certificats émis en 2023 · les machines non mises à jour continuent de démarrer mais perdent la capacité de recevoir de futures révocations.

**[S-26]** — Microsoft Learn — **correction à chaud (hotpatching) sur machines rattachées à Azure Arc**
Niveau `D` · Vérifiée le 30/07/2026 · Utilisée au §2.5.
*Faits retenus* : disponible pour Windows Server 2025 éditions Standard et Datacenter · **sans coût additionnel depuis le 19/05/2026** (facturation par cœur supprimée) · cadence de mise à jour de référence trimestrielle avec redémarrage, suivie de deux mois de correctifs à chaud · prérequis dont la sécurité basée sur la virtualisation et le démarrage sécurisé · pilotes, micrologiciels et certains composants **hors périmètre**.

**[S-27]** — Projet Kubernetes — **politique de support des versions**
Niveau `D` · Vérifiée le 30/07/2026 · Utilisée au §3.3, §30.4, annexe H.
*Faits retenus* : environ trois versions mineures par an · environ **douze mois de support standard** suivis d'environ **deux mois de maintenance limitée** · les offres managées appliquent leurs propres calendriers.

### M.6 Ce qui n'est pas sourcé, et l'est assumé

Les éléments suivants relèvent d'une **doctrine proposée par ce cours**, et non d'une exigence externe. Ils sont marqués comme tels dans le texte et doivent être adaptés puis approuvés par votre organisation :

| Élément | Où |
|---|---|
| Les sept attributs obligatoires d'une mesure compensatoire | §20.7 |
| La règle de signature au niveau supérieur à chaque renouvellement de dérogation | §7.4 |
| Les délais 72 h / 7 j / 30 j des classes de service | §7.2, annexe C |
| Le délai d'observation de 3 à 7 jours | §18.3 |
| Les alertes certificat à 60/30/7 jours | §24.6 |
| Le délai d'observation de 90 jours après décommissionnement | §35.11 |
| La capacité de sécurité de 10 à 20 % réservée en développement | §25.3 |
| Le délai de 90 jours de divulgation coordonnée | §33.3 — **pratique courante**, non règle |
| Les seuils d'escalade et les tailles d'échantillon d'audit | annexe J, §39.4 |
| Les cycles de support par famille de produits (5-10 ans, 2-4 ans…) | annexe H — **ordres de grandeur indicatifs**, non sourcés |

⚠️ **Le principe** : mieux vaut une doctrine interne explicitement assumée et approuvée qu'une valeur présentée comme une norme externe qu'elle n'est pas. Un auditeur accepte parfaitement une règle interne motivée ; il n'accepte pas une exigence attribuée à tort à un référentiel.

### M.7 Sources à revérifier en priorité

| Priorité | Source | Motif |
|---|---|---|
| **1** | [S-02] | Promulgation attendue — change le statut de toute la Partie II |
| **1** | [S-03] | Version définitive attendue — les objectifs cités peuvent être renumérotés |
| **2** | [S-24] | Calendriers de support étendu susceptibles d'évoluer |
| **2** | [S-16], [S-17] | Évolutions de l'écosystème et des modèles de score |
| **3** | [S-15] | Statut du schéma de qualification |
| **3** | [S-26], [S-27] | Modèles économiques et calendriers de support |

---

## Journal des modifications

| Version | Date | Nature |
|---|---|---|
| 1.0 | 30/07/2026 | Première rédaction : 7 parties, 40 chapitres, 3 cas de synthèse, 9 mini-labs, 12 annexes |
| 1.1 | 01/08/2026 | Passe de fiabilisation après revue. Corrections factuelles et mathématiques : démonstration de capacité du §16.1 · formule de conformité de configuration du §22.5 · temps verbal et portée transitoire des échéances CRA (§33.5, §33.9, annexe F) · réconciliation de la chronologie produit du fil rouge (§8.10, §33.13). Doctrine : distinction périmètre maître / population éligible / non mesuré / N/A (annexe I.4, §38.2, annexe K) · requalification des produits couverture × conformité en ratio conservateur · introduction des deux horloges, risque et traitement (§17.5, annexe J). Éditorial : restauration de l'en-tête de maintenance et de la matrice de parcours · régénération de la table des matières hors blocs de code · hiérarchie du chapitre 25 · niveau de titre des annexes · renumérotation de 33.8 bis. |
| 1.1 | 01/08/2026 | Passe de fiabilisation après revue. Corrections factuelles et mathématiques : démonstration de capacité du §16.1 · formule de conformité de configuration du §22.5 · temps verbal et portée transitoire des échéances CRA (§33.5, §33.9, annexe F) · réconciliation de la chronologie produit du fil rouge (§8.10, §33.13). Doctrine : distinction périmètre maître / population éligible / non mesuré / N/A (annexe I.4, §38.2, annexe K) · requalification des produits couverture × conformité en ratio conservateur · introduction des deux horloges, risque et traitement (§17.5, annexe J). Éditorial : restauration de l'en-tête de maintenance et de la matrice de parcours · régénération de la table des matières hors blocs de code · hiérarchie du chapitre 25 · niveau de titre des annexes · renumérotation de 33.8 bis. |
| 1.1 | 01/08/2026 | Passe de fiabilisation après revue. Corrections factuelles et mathématiques : démonstration de capacité du §16.1 · formule de conformité de configuration du §22.5 · temps verbal et portée transitoire des échéances CRA (§33.5, §33.9, annexe F) · réconciliation de la chronologie produit du fil rouge (§8.10, §33.13). Doctrine : distinction périmètre maître / population éligible / non mesuré / N/A (annexe I.4, §38.2, annexe K) · requalification des produits couverture × conformité en ratio conservateur · introduction des deux horloges, risque et traitement (§17.5, annexe J). Éditorial : restauration de l'en-tête de maintenance et de la matrice de parcours · régénération de la table des matières hors blocs de code · hiérarchie du chapitre 25 · niveau de titre des annexes · renumérotation de 33.8 bis. |
| 1.1 | 01/08/2026 | Passe de fiabilisation après revue. Corrections factuelles et mathématiques : démonstration de capacité du §16.1 · formule de conformité de configuration du §22.5 · temps verbal et portée transitoire des échéances CRA (§33.5, §33.9, annexe F) · réconciliation de la chronologie produit du fil rouge (§8.10, §33.13). Doctrine : distinction périmètre maître / population éligible / non mesuré / N/A (annexe I.4, §38.2, annexe K) · requalification des produits couverture × conformité en ratio conservateur · introduction des deux horloges, risque et traitement (§17.5, annexe J). Éditorial : restauration de l'en-tête de maintenance et de la matrice de parcours · régénération de la table des matières hors blocs de code · hiérarchie du chapitre 25 · niveau de titre des annexes · renumérotation de 33.8 bis. |
| 1.6 | 01/08/2026 | Passe de hierarchisation et de memorisation. Ajout de **la doctrine du cours en sept principes**, en tete de document, chacun rattache au chapitre qui le demontre. Encadre *les quatre idees a retenir* au chapitre 1. Phrases reperes isolees visuellement : CVSS decrit la gravite technique et non la priorite operationnelle · un journal n'est pas une preuve parce qu'il existe · le MCS ne change pas de principes en environnement industriel, il change de contraintes. Rapprochement systematique mecanisme puis **ce que ca change pour vous**. Fil conducteur du chapitre 3 rendu explicite. Avertissement sur les sigles et identification des **quatre reperes du quotidien** au chapitre 4. Clarification dette de securite contre stock de vulnerabilites. Ajout d'un **plan d'acces aux annexes** avec distinction apprendre / consulter / verifier. Ajout de la section finale **Ce que vous savez faire** : trente-deux competences formulees en actes, plus ce que le cours n'enseigne pas et ce que seule la pratique donne. |
| 1.5 | 01/08/2026 | Passe de vocabulaire et de navigation, apres audit mesure. Audit de terminologie sur huit familles de termes : la coherence est confirmee (correctif 348 / patch 2, remedier 0, findings 0, CMDB 4). Ajout d'une table **vocabulaire du cours / vocabulaire du terrain** en §1.1, avec la nuance a ne pas perdre pour chaque terme. Clarification en quatre lignes de derogation / acceptation de risque / N-A / faux positif, et regle interne bannissant le mot « exception » des documents formels. Ajout de cinq micro-exemples 🏢 **VU EN REUNION**. Ajout de 35 amorces « Chapitre suivant » en fin de chapitre, completant les six encadres de fin de partie. |
| 1.4 | 01/08/2026 | Passe de finition. **Vérification mécanique complète des renvois** : 856 renvois de section, 40 renvois de chapitre, renvois d'annexes, templates D.n et sources [S-nn] — **aucune cible manquante**, et contrôle sémantique des vingt renvois les plus fréquents. Ajout du champ *compétences validées* aux neuf mini-labs. Pose de dix marqueurs SCHÉMA identifiant les emplacements de visuels à produire en mise en page, le texte restant autonome sans eux. Annexe B homogénéisée : douze fiches au format uniforme — périmètre, contrôles, privilèges requis, lecture du résultat, preuve produite, limites, source de vérité, piège spécifique, cadence. |
| 1.3 | 01/08/2026 | Passe pedagogique. Schema directeur de la boucle en six segments (1.1) avec renvoi par partie · tableau de positionnement MCS / SOC / CERT / exploitation · journee type · tableau « qui met a jour quoi » par modele d'execution (3.4) · six encadres de fin de partie « a ce stade vous savez » · en-tetes normalises des neuf mini-labs (duree, difficulte, prerequis, livrable) et tableau recapitulatif · schema recapitulatif complet et six regles de synthese (40.9). |
| 1.2 | 01/08/2026 | Matérialisation des livrables et sourçage. Annexe D transformée en 14 formulaires remplissables avec règles de validation · annexes I, J et K reconstruites en modèles complets (types, cardinalités, droits de transition, fiches d'indicateurs, critères de preuve par niveau de maturité) · mini-labs 5 à 8 développés avec dossiers de données bruts, barèmes et erreurs attendues · trois cas de synthèse développés avec artefacts, corrigés argumentés, critères d'évaluation et variantes · **création de l'annexe M — registre de sources**, avec références d'articles précises pour le CRA (art. 13, 14, 16, 69) et les contrôles ISO · 37 formulations absolues assouplies. |

**Prochaine revue recommandée** : 31 janvier 2027, ou à la survenue d'un déclencheur listé en tête de document.

**Sections à réviser en priorité** : ch. 4 §4.9 · ch. 8 (intégralité) · ch. 12 §12.4-12.5 · ch. 19 · ch. 30 · ch. 33 §33.5-33.7 · annexes E, F, H.

---

*Fin du document.*
