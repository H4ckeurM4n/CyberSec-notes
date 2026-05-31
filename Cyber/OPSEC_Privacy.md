# OPSEC & Privacy : sécurité numérique personnelle, anonymat, compartimentation et réduction d’exposition

*Manuel de sécurité numérique défensive pour journalistes d’investigation, sources, activistes, dirigeants, professionnels exposés et particuliers exigeants (2025-2026)*

-----

## Avant-propos

### Pourquoi ce cours

La plupart des guides de sécurité numérique grand public oscillent entre deux postures stériles : la liste de courses (« installez Signal, prenez un VPN, mettez à jour vos appareils ») et la promesse fantasmatique (« devenez invisible en 30 jours »). Aucune ne forme à raisonner. La première oublie que sans modèle de menace, un outil mal employé est un faux sentiment de sécurité ; la seconde oublie que l’anonymat absolu n’existe pas, et que prétendre le contraire est non seulement faux mais dangereux pour ceux qui en dépendent réellement.

Ce cours prend une troisième voie. Il enseigne **à raisonner** : modéliser sa menace, identifier ses actifs, hiérarchiser les risques, choisir les outils adaptés à un contexte précis, comprendre leurs limites, construire une compartimentation soutenable, et accepter que la sécurité parfaite n’existe pas — mais que la sécurité *suffisante pour son threat model* est atteignable, et durable.

### Public visé

Le cours s’adresse à toute personne ayant des raisons sérieuses de réduire son exposition numérique :

- **Journalistes d’investigation** et **sources** : protection des communications, des documents, des contacts.
- **Lanceurs d’alerte** et **avocats** travaillant sur des sujets sensibles.
- **Activistes** et personnes engagées politiquement, particulièrement dans des contextes répressifs ou ciblés.
- **Personnalités publiques** (politiques, dirigeants, créateurs médiatisés) exposées au doxxing, au harcèlement coordonné ou à l’espionnage économique.
- **Professionnels cyber** (RSSI, analystes, chercheurs en sécurité, threat hunters) qui doivent compartimenter recherche, lab, veille et vie personnelle.
- **Agents** travaillant dans des environnements à contrainte de discrétion.
- **Particuliers exigeants** souhaitant atteindre un haut niveau d’hygiène numérique sans s’enchaîner à un activisme paranoïaque.
- **Victimes potentielles d’adversaires de proximité** (ex-partenaire abusif, harceleur, employeur intrusif) — un threat model souvent ignoré par les cours « cyber » trop orientés État ou APT.

### Ce que ce cours **n’est pas**

- Ce n’est pas un guide pour commettre des infractions ni pour échapper à des autorités judiciaires légitimes.
- Ce n’est pas un manuel d’anonymisation absolue.
- Ce n’est pas une suite de recettes prêtes à l’emploi : chaque chapitre force à réfléchir avant d’agir.
- Ce n’est pas un cours offensif (red team, OSINT investigatif, intrusion). Il est exclusivement défensif.

### Cadre légal et éthique (à lire dès maintenant)

La protection de la vie privée est un droit fondamental garanti par la Convention européenne des droits de l’homme (article 8), la Charte des droits fondamentaux de l’Union européenne (articles 7 et 8) et, en droit français, l’article 9 du Code civil. Le chiffrement est légal en France depuis la LCEN (article 30). Le secret des sources des journalistes est protégé par la loi du 4 janvier 2010 et renforcé par le règlement (UE) 2024/1083 dit *European Media Freedom Act* (EMFA), qui protège notamment les sources journalistiques contre l’usage abusif de spyware par les États membres.

Ces droits ne sont **pas absolus**. Ils s’inscrivent dans un cadre de proportionnalité : ordre public, enquête judiciaire, sécurité nationale peuvent fonder des restrictions, sous contrôle d’un juge. Ce cours respecte intégralement ce cadre. Il n’enseigne pas à dissimuler des activités illicites. Il enseigne à exercer un droit légitime : celui de la confidentialité, de la sécurité personnelle, et de la liberté d’enquête, d’information et d’expression.

Le cadre légal complet est traité au **chapitre 37**.

### Comment lire ce cours

Le cours est conçu pour être lu **dans l’ordre** : chaque partie installe les concepts utilisés par la suivante. Une lecture par picorage est possible mais réduit la valeur des renvois croisés et de la progression du fil rouge narratif.

Les **trois capstones intermédiaires** sont des exercices de mise en pratique. Les **quatre cas de synthèse** finaux mobilisent l’ensemble du cours dans des scénarios complets. Les **neuf annexes** sont des outils opérationnels (matrices, templates, architectures de référence, cadre juridique, cas d’échec OPSEC célèbres, ressources).

### Le fil rouge

Le cours est traversé par un récit. **Léa Martens**, journaliste d’investigation freelance basée à Bruxelles (34 ans), démarre une enquête sensible pour un consortium européen de journalistes : un dossier de corruption transeuropéen impliquant un commissaire européen, une société de surveillance privée et un oligarque proche du Kremlin. Léa commence le cours avec une hygiène numérique « grand public » : Gmail, iPhone non durci, WhatsApp, mots de passe réutilisés, présence active sur LinkedIn et X. Son durcissement progresse au fil des chapitres, avec des erreurs corrigées en cours de route.

Cinq personnages secondaires apparaissent quand un chapitre se prête mieux à un autre profil : **Karim B.**, lanceur d’alerte interne dans une autorité administrative française ; **Sophie R.**, activiste climatique exposée à une surveillance administrative ; **Olivier M.**, dirigeant d’une PME tech cible d’espionnage économique ; **Yann T.**, RSSI d’une ONG des droits humains basée à Genève ; **Anya V.**, opposante politique russe en exil à Berlin.

Le fil rouge n’est pas décoratif. Il illustre les concepts au moment où ils sont abordés.

> 🟨 **Avertissement** : Léa, Karim, Sophie, Olivier, Yann, Anya, Catherine et tous les autres personnages et scénarios du cours (y compris dans les cas de synthèse finaux) sont **fictifs**, même lorsqu’ils s’inspirent de situations réalistes documentées dans la presse et les rapports d’ONG. Toute ressemblance avec des personnes réelles serait fortuite. Les cas nommément cités (Ross Ulbricht, Eldo Kim, Reality Winner, John McAfee, etc.) en Annexe 8 sont, eux, des cas réels publics et judiciairement clos, traités à des fins pédagogiques sur la base de documentation publique.

-----

## Table des matières

### Partie 1 — Fondations conceptuelles et threat modeling

- Chapitre 1 — Concepts fondamentaux et notions transverses
- Chapitre 2 — Threat modeling personnel
- Chapitre 3 — Taxonomie des adversaires
- Chapitre 4 — Cartographie de l’empreinte et grands modèles d’exposition

### Partie 2 — Identité, compartimentation et hygiène comportementale

- Chapitre 5 — OSINT défensif : auditer son propre profil
- Chapitre 6 — Data brokers, courtiers de données et désinscription effective
- Chapitre 7 — Doxxing : mécanique, prévention et réponse
- Chapitre 8 — Réseaux sociaux et exposition publique
- Chapitre 9 — Compartimentation et hygiène comportementale
- 🟦 *Capstone 1 — Construire son architecture de compartimentation*

### Partie 3 — Sécurité matérielle, racine de confiance et isolation

- Chapitre 10 — Sécurité matérielle : choix, supply chain, intégrité physique
- Chapitre 11 — Firmware, UEFI, Secure Boot, TPM et chaîne de démarrage
- Chapitre 12 — Chiffrement complet du disque
- Chapitre 13 — Air gap, appareils dédiés et environnements isolés
- Chapitre 14 — Durcissement Windows, macOS et Linux pour le quotidien
- Chapitre 15 — Mobile : iOS durci, Android, GrapheneOS

### Partie 4 — Environnements de session sensible

- Chapitre 16 — Machines virtuelles, live USB et environnements jetables
- Chapitre 17 — Tails, Whonix et Qubes OS : choisir le bon modèle d’isolation
- Chapitre 18 — Qubes OS en pratique : compartimentation avancée et workflows sensibles
- 🟦 *Capstone 2 — Chaîne complète de session sensible*

### Partie 5 — Réseau, anonymat et navigation web

- Chapitre 19 — Pile réseau : ce que voit chaque acteur
- Chapitre 20 — VPN : utilité réelle, limites, choix
- Chapitre 21 — Tor : architecture, bridges, services onion, OPSEC
- Chapitre 22 — Wi-Fi, Bluetooth, cellulaire, MAC, IMSI
- Chapitre 23 — AdTech, tracking web,  fingerprinting et ADINT : mécanismes profonds
- Chapitre 24 — Navigateurs, moteurs de recherche et stratégies anti-fingerprint

### Partie 6 — Communications, comptes et données

- Chapitre 25 — Cryptographie appliquée aux communications
- Chapitre 26 — Messageries chiffrées
- Chapitre 27 — Email, PGP et limites structurelles
- Chapitre 28 — Partage sécurisé de fichiers et documents
- Chapitre 29 — Comptes critiques, authentification et secrets
- Chapitre 30 — Cloud, sauvegardes et chiffrement côté client
- Chapitre 31 — Métadonnées et nettoyage de fichiers
- Chapitre 32 — Paiements, traçabilité financière et cryptomonnaies
- 🟦 *Capstone 3 — Auditer et durcir une chaîne source-journaliste*

### Partie 7 — OPSEC humaine, opérationnelle et continuité

- Chapitre 33 — Social engineering, phishing ciblé et spyware mercenaire
- Chapitre 34 — IA générative, LLM, deepfakes et privacy
- Chapitre 35 — OPSEC humaine : entourage, photos, voix, stylométrie, traces comportementales
- Chapitre 36 — Voyage, frontières et appareils temporaires
- Chapitre 37 — Cadre juridique et éthique
- Chapitre 38 — Maintenance opérationnelle, réponse à incident et architectures par profil

### Cas de synthèse finaux

- Cas A — Journaliste d’investigation (clôture du fil rouge)
- Cas B — Activiste avant manifestation
- Cas C — Dirigeant cible d’espionnage économique
- Cas D — Particulier face à un ex-conjoint abusif

### Annexes

- Annexe 1 — Glossaire (100+ termes)
- Annexe 2 — Cheat sheets opérationnels
- Annexe 3 — Matrice d’outils de référence
- Annexe 4 — Matrices de décision
- Annexe 5 — Architectures de référence par profil
- Annexe 6 — Templates opérationnels
- Annexe 7 — Cadre juridique comparé (FR / UE / US / UK / CH)
- Annexe 8 — Cas célèbres d’échec OPSEC : leçons défensives
- Annexe 9 — Ressources, formations, communautés

-----

## Partie 1 — Fondations conceptuelles et threat modeling

> **Objectif** : poser le vocabulaire, démonter les confusions courantes, installer le réflexe « threat model d’abord, outil ensuite ». Cette partie ne contient presque aucun nom d’outil. C’est volontaire : avant de choisir, il faut savoir contre quoi on se défend.

-----

### Chapitre 1 — Concepts fondamentaux et notions transverses

#### 1.1 Privacy, sécurité, anonymat, pseudonymat, secret : les confusions qui tuent

Cinq mots qui désignent cinq choses différentes, constamment mélangés dans la conversation publique. Cette confusion n’est pas anecdotique : elle conduit à choisir le mauvais outil pour le mauvais problème.

**Privacy** (vie privée) est le contrôle qu’on exerce sur l’information qui circule à son sujet. Tu fermes la porte des toilettes non pas parce que tu caches un secret, mais parce que tu veux décider qui sait quoi de ton intimité. La privacy est un droit ; elle n’implique aucune dissimulation d’activité.

**Sécurité** est la capacité à protéger l’intégrité, la confidentialité et la disponibilité de ses actifs (données, comptes, appareils) contre des menaces. Tu peux être *sécurisé* sans être *anonyme* : ton compte bancaire est à ton nom, mais protégé par MFA. Tu peux être *anonyme* sans être *sécurisé* : un pseudonyme sur un forum dont la base de données fuit ne te protège plus.

**Anonymat** est l’impossibilité, pour un observateur, d’attribuer une action à une identité — y compris une identité pseudonyme. C’est le degré le plus exigeant et le plus rare. L’anonymat *absolu* n’existe pas ; on parle d’anonymat *contre un modèle d’adversaire donné*.

**Pseudonymat** est l’usage d’un nom de substitution stable. @GamerGuy12 est un pseudonyme : ce n’est pas anonyme, parce que le pseudo est persistant et peut être corrélé avec le temps à un comportement, des habitudes, des contacts, voire à une identité civile. La plupart des « anonymes » sur internet sont en réalité des pseudonymes.

**Secret** désigne une information qu’on cache activement. Tout secret est privé, mais toute information privée n’est pas secrète. Tu ne caches pas que tu prends une douche ; tu protèges l’image de toi nu sous la douche. La privacy est une question de *contexte* (qui voit quoi dans quel cadre), le secret est une question de *contenu* (cette information ne doit être vue par personne d’autre).

**OPSEC** (Operational Security) est la discipline qui consiste à identifier, contrôler et protéger les *indicateurs* qui, agrégés, permettraient à un adversaire de déduire des informations sensibles. C’est une métadiscipline : elle s’applique à tout ce qui précède.

> 🟨 **Pourquoi ces distinctions sont opérationnelles**
> Un journaliste qui veut protéger une **source** a besoin que personne ne puisse établir un *lien* entre lui et cette personne. C’est de l’anonymat (de la relation), pas du secret du contenu : peu importe ce qui est dit, ce qui compte, c’est que personne ne sache que la conversation a eu lieu. Or beaucoup de journalistes confondent les deux et chiffrent fortement le *contenu* sur des canaux qui révèlent massivement les *métadonnées de relation*. C’est une erreur de cadrage qui annule la protection.

#### 1.2 OPSEC : héritage militaire, cycle en 5 étapes, transposition civile

L’OPSEC est née dans l’armée américaine pendant la guerre du Vietnam (opération Purple Dragon, 1966) après le constat que les Nord-Vietnamiens anticipaient les opérations sans avoir besoin de casser les codes : ils observaient des indicateurs (mouvements logistiques, communications radio routinières, rotations de personnel) qui, agrégés, révélaient les intentions. La parade fut de cesser de raisonner en *secrets* et de commencer à raisonner en *indicateurs*.

Le cycle OPSEC formalisé comporte cinq étapes :

1. **Identification des informations critiques** — qu’est-ce qui, si appris par l’adversaire, lui donnerait un avantage décisif ? Pour un individu : son adresse, ses contacts sensibles, sa localisation en temps réel, ses identifiants, sa relation à une source.
1. **Analyse des menaces** — qui est l’adversaire, quelles sont ses capacités, sa motivation, ses méthodes ?
1. **Analyse des vulnérabilités** — quels indicateurs, dans mes routines, mes communications, mon comportement, révèlent ces informations critiques ?
1. **Évaluation des risques** — probabilité × impact, hiérarchisation.
1. **Application de contre-mesures** — réduire les indicateurs, masquer les corrélations, compartimenter, etc.

La transposition civile ne change pas le cycle, elle change l’échelle : un individu n’a pas les ressources d’une armée. Cela impose des arbitrages de soutenabilité : une posture OPSEC qui détruit la vie sociale ou professionnelle finit par s’effondrer. **La meilleure OPSEC est celle qu’on tient dans la durée**, pas celle qu’on tient brillamment trois semaines avant de craquer.

#### 1.3 Confidentialité du contenu vs confidentialité des métadonnées

Distinction fondamentale, et probablement la plus sous-estimée du domaine.

Le **contenu** d’une communication, c’est ce qui est dit. Les **métadonnées** sont tout le reste : qui parle à qui, quand, depuis où, combien de temps, à quelle fréquence, avec quel volume de données, depuis quel appareil. Le chiffrement de bout en bout (E2EE) protège typiquement le contenu. Il ne protège presque jamais les métadonnées.

Or l’attaquant sérieux préfère les métadonnées. Le général Michael Hayden, ancien directeur de la NSA, l’a résumé brutalement : *« We kill people based on metadata. »* Les drones américains ne lisent pas les conversations, ils lient des numéros à des positions à des contacts à des routines, et tirent.

À l’échelle d’un individu non militaire, la même mécanique tient : un harceleur qui sait avec qui tu communiques tous les soirs à 23h connaît probablement ta liaison ; un employeur qui voit que tu écris à un journaliste sait probablement que tu es la source ; un service de renseignement qui voit deux téléphones se géolocaliser quotidiennement au même endroit la nuit a établi une relation, indépendamment du contenu des messages.

**Conséquence pratique** : protéger le contenu sans protéger les métadonnées, c’est mettre un coffre-fort blindé dans une vitrine. Une partie significative de ce cours est consacrée à la réduction des métadonnées : choix de messageries qui les minimisent (Ch 25-26), routage anonymisé du trafic (Ch 21), compartimentation des canaux (Ch 9), et hygiène du comportement répétitif (Ch 9 et 35).

#### 1.4 Surface d’attaque, surface d’exposition, surface de corrélation

Trois notions cousines qu’il faut tenir distinctes.

La **surface d’attaque** est l’ensemble des points par lesquels un adversaire peut tenter de t’atteindre techniquement : ports réseau ouverts, applications installées, services en écoute, comptes existants. Plus elle est large, plus il y a de vulnérabilités potentielles. La réduire, c’est minimiser ce qu’on installe, ce qu’on ouvre, ce qu’on expose.

La **surface d’exposition** est l’ensemble des informations qu’un adversaire peut collecter sur toi *sans avoir à t’attaquer* : ce que tu publies, ce que les data brokers compilent, ce que les fuites de données ont déjà révélé, ce que ton entourage rend public. La réduire, c’est réfléchir avant de publier et nettoyer rétroactivement (Ch 5 à 8).

La **surface de corrélation** est l’ensemble des points par lesquels deux identités, deux activités ou deux comptes peuvent être *reliés*. Un même numéro de téléphone sur deux comptes les corrèle. Un même style d’écriture sur deux pseudos les corrèle. Une même IP, un même fingerprint navigateur, une même heure de connexion les corrèlent. La compartimentation (Ch 9) vise précisément à réduire cette surface.

Ces trois surfaces interagissent. Réduire la surface d’attaque sans réduire la surface d’exposition ne sert qu’à demi : un attaquant motivé n’a plus besoin de hacker quand l’information est déjà publique.

#### 1.5 Défense en profondeur, moindre privilège, need-to-know

Trois principes importés de la sécurité d’entreprise, parfaitement applicables à un individu.

**Défense en profondeur** : ne jamais miser sur une seule barrière. Si ton mot de passe est ta seule défense, sa compromission est totale. Si tu as un mot de passe fort + MFA matériel + alertes de connexion + sessions audités + procédure de récupération hors-ligne, la compromission de l’un ne renverse pas tout. Cela vaut pour les communications (E2EE + appareil durci + vérification d’identité), pour les données (chiffrement disque + chiffrement fichier + sauvegarde chiffrée hors-site), et pour la posture globale (compartimentation + minimisation + détection).

**Moindre privilège** : ne donner à chaque application, chaque compte, chaque service que les droits strictement nécessaires. L’application météo n’a pas besoin de tes contacts. Le compte que tu utilises pour une newsletter n’a pas besoin d’être le compte qui contient ta vie. Le téléphone que tu emportes en manifestation n’a pas besoin d’avoir accès à ton coffre-fort de mots de passe principal.

**Need-to-know** : ne partager une information sensible qu’avec ceux qui en ont strictement besoin pour leur rôle. Ton avocat a besoin de savoir, ton voisin non. Ta source a besoin de savoir comment te joindre, pas comment tu vis. Cette discipline, banale dans le renseignement, est rare dans la vie civile — mais elle est l’une des plus efficaces.

#### 1.6 Identification, corrélation, attribution : la chaîne adversaire

Comprendre comment un adversaire passe d’une information à l’identité d’une personne est essentiel pour savoir où couper la chaîne.

1. **Identification** : associer un élément observable (pseudonyme, adresse email, appareil, numéro de téléphone, photo) à une autre information.
1. **Corrélation** : relier plusieurs identifications. Le pseudo @LunaB37 utilise le même téléphone que l’email luna.b@protonmail.com qui se connecte depuis la même IP qu’un compte Twitter sous nom civil.
1. **Attribution** : conclure, avec un niveau de confiance donné, que telle action est l’œuvre de telle personne réelle.

La défense ne consiste pas à empêcher l’identification (souvent impossible) mais à **casser les corrélations** : faire en sorte que les éléments identifiés n’appartiennent pas tous à la même chaîne. C’est l’objet de la compartimentation.

#### 1.7 Le mythe de l’outil magique et le mythe de l’anonymat absolu

Deux croyances symétriques, toutes deux fausses, toutes deux dangereuses.

Le **mythe de l’outil magique** : « j’utilise X (Signal, Tor, VPN, GrapheneOS, Qubes), donc je suis protégé ». Un outil est une fonction, pas une posture. Signal protège le contenu d’un message, pas le fait que tu communiques avec cette personne ; Tor anonymise la couche réseau, pas tes habitudes ; un VPN déplace la confiance, il ne crée pas d’anonymat ; GrapheneOS durcit un téléphone, il ne t’empêche pas de te connecter à Facebook depuis ce téléphone.

Le **mythe de l’anonymat absolu** : « il est possible de disparaître totalement ». Non. Tout est question d’adversaire et de ressources. Contre un voisin curieux : trivial. Contre un employeur intrusif : faisable. Contre un harceleur déterminé : exigeant mais possible. Contre un État motivé avec budget et patience : extraordinairement difficile, et plus on essaie d’effacer ses traces de façon visible, plus on attire l’attention. La meilleure stratégie est de **rendre l’attaque coûteuse**, pas de viser l’invisibilité.

Ce cours postule en permanence que la protection est *probabiliste* et *contextuelle*. Aucune affirmation absolue n’y est faite sur ce qu’un outil garantit.

#### 1.8 L’argument « rien à cacher » : démontage opérationnel et philosophique

L’argument « si tu n’as rien à cacher, tu n’as rien à craindre » se réfute sur trois niveaux.

**Niveau philosophique** : tu fermes la porte des toilettes, tu ne lis pas tes mails de famille devant inconnus, tu ne dictes pas ton mot de passe à voix haute en réunion. Personne ne vit comme s’il n’avait rien à cacher. La privacy n’est pas l’aveu d’un secret, c’est la condition d’une vie digne et d’une autonomie individuelle.

**Niveau juridique** : la vie privée est un *droit*, pas une faveur conditionnée à la conformité. L’inverser, c’est inverser la charge de la preuve : ce n’est pas à toi de prouver que tu mérites la vie privée, c’est aux États et aux entreprises de prouver qu’ils ont un motif légitime d’y porter atteinte.

**Niveau opérationnel** : ce qui est anodin aujourd’hui peut devenir compromettant demain. Une opinion politique légale dans un pays démocratique peut être criminalisée après bascule autoritaire. Une orientation sexuelle banale ici peut être létale ailleurs. Une opinion religieuse, une grossesse, une consultation médicale, une lecture, une association : tout cela est légal aujourd’hui, dans ton pays, dans ton contexte. Réduire ses traces, ce n’est pas cacher des fautes, c’est protéger des futurs qu’on ne contrôle pas.

> 🟩 **À retenir du chapitre 1**
> 
> - Cinq mots, cinq concepts : privacy, sécurité, anonymat, pseudonymat, secret. OPSEC est le métaconcept.
> - Métadonnées > contenu dans la plupart des modèles d’adversaire sérieux.
> - Trois surfaces : attaque, exposition, corrélation. Toutes trois à réduire.
> - Trois principes : défense en profondeur, moindre privilège, need-to-know.
> - La défense efficace coupe la **corrélation**, pas l’identification.
> - Pas d’outil magique, pas d’anonymat absolu. La protection est probabiliste et contextuelle.

-----

### Chapitre 2 — Threat modeling personnel

#### 2.1 Les cinq questions fondatrices

L’Electronic Frontier Foundation a formalisé un cadre minimal de threat modeling personnel en cinq questions. Elles sont simples, mais leur mise en œuvre rigoureuse change tout.

1. **Que veux-je protéger ?** (mes actifs)
1. **Contre qui ?** (mes adversaires)
1. **Quelle est la probabilité que je doive le protéger ?** (le risque)
1. **Quelles sont les conséquences si j’échoue ?** (l’impact)
1. **Combien de difficultés suis-je prêt(e) à accepter pour empêcher cela ?** (le coût acceptable)

La cinquième est la plus importante et la plus souvent oubliée. Elle ancre la réflexion dans le réel : sans elle, on dérive vers des architectures théoriquement parfaites mais inapplicables dans la vraie vie.

#### 2.2 Inventaire des actifs

Un actif est une chose à laquelle tu tiens et que tu veux protéger. Pour un individu, ce sont généralement :

- **Identité** : nom, photo, voix, adresse, état civil, nationalités.
- **Comptes** : email principal (centre de gravité, cf. Ch 29), réseaux sociaux, comptes bancaires, comptes professionnels, comptes cloud, comptes administratifs (impôts, sécurité sociale).
- **Données** : fichiers personnels, photos, documents professionnels, dossiers médicaux, contrats, journaux, correspondance.
- **Appareils** : téléphone(s), ordinateur(s), tablettes, IoT, clés de sécurité, cartes SIM.
- **Relations** : carnet d’adresses, liens familiaux, sources journalistiques, contacts professionnels, réseaux d’engagement (associatif, politique, religieux).
- **Localisation** : domicile, lieux de travail, déplacements habituels, voyages.
- **Réputation** : image publique, dossiers passés, opinions exprimées, contenus produits.
- **Présence physique** : sécurité personnelle, intégrité corporelle, accès au domicile.

Liste tes actifs *avant* de penser aux outils. Pour chacun, note : où est-il stocké, qui y a accès, qu’est-ce qui empêche aujourd’hui un tiers d’y accéder. La plupart des gens découvrent à ce stade que l’« email principal » concentre les clés de tout le reste (récupération de mot de passe, MFA SMS, factures).

#### 2.3 Identifier ses adversaires sans inflation ni déni

Deux travers symétriques empoisonnent l’exercice.

L’**inflation** consiste à se croire la cible de la NSA quand on est un militant climatique local. C’est flatteur, c’est anxiogène, c’est inefficace : on construit des architectures sur-dimensionnées qui détournent l’attention des vraies menaces (un employeur qui surveille les emails, un ex qui a gardé un mot de passe, un harceleur qui scrute les réseaux sociaux). On se prépare à Pegasus alors qu’on est vulnérable à un simple phishing.

Le **déni** est l’inverse : « je ne suis personne, qui voudrait m’attaquer ? ». Or beaucoup d’attaques sont *opportunistes* (phishing de masse, vol de crédentials, ransomware). Tu n’as pas besoin d’intéresser quelqu’un personnellement pour être ciblé statistiquement. Et certaines menaces sont *de proximité* (ex-partenaire, employeur intrusif) : il suffit d’une relation à problèmes pour avoir un adversaire réel.

Le bon réflexe : lister les adversaires *plausibles* compte tenu de qui tu es et de ce que tu fais. Un journaliste d’investigation a comme adversaires réalistes : États visés par ses enquêtes, sociétés visées, criminalité organisée si pertinent, harceleurs en ligne (notamment femmes journalistes), employeurs (sécurité industrielle des médias). Une activiste a : forces de l’ordre nationales, infiltrés, contre-mouvements organisés, harceleurs. Un dirigeant : concurrents (espionnage économique), fraudeurs ciblés, criminalité organisée si secteur exposé. Un particulier durci typique : criminalité de masse, employeur, ex-partenaire, plateformes elles-mêmes (capitalisme de surveillance).

#### 2.4 Capacité × motivation × probabilité

Chaque adversaire doit être caractérisé par trois paramètres :

- **Capacité** : quelles ressources techniques, juridiques, humaines, financières ? Un service de renseignement étatique a accès à des zero-days, à de la coopération inter-services, à des contraintes judiciaires sur les opérateurs. Un harceleur isolé a accès à Google, des forums, peut-être un peu d’OSINT manuel. La capacité borne le *plafond* de la menace.
- **Motivation** : quel intérêt l’adversaire a-t-il à m’attaquer, *moi spécifiquement* ? Forte (une enquête qui le compromet) ou faible (statistique, sans personnalisation) ?
- **Probabilité** : sachant capacité et motivation, quelle est la probabilité d’occurrence ?

Une matrice utile :

|                      |Faible capacité   |Capacité moyenne|Forte capacité              |
|----------------------|------------------|----------------|----------------------------|
|**Faible motivation** |Risque négligeable|Risque faible   |Risque modéré (opportuniste)|
|**Motivation moyenne**|Risque faible     |Risque modéré   |Risque élevé                |
|**Forte motivation**  |Risque modéré     |Risque élevé    |Risque critique             |

Les défenses doivent être calibrées sur les cases à *risque modéré et plus*. Les cases à risque négligeable n’imposent rien de spécifique.

#### 2.5 Coût acceptable de la défense

C’est l’arbitrage permanent. Trois dimensions :

- **Coût financier** : prix des appareils, abonnements (VPN, gestionnaire de mots de passe), clés matérielles.
- **Coût cognitif** : apprendre, mémoriser, configurer, maintenir.
- **Coût social et ergonomique** : friction au quotidien, perte de fonctionnalités, isolement par rapport aux usages dominants.

Une mesure trop coûteuse sur l’une des trois dimensions finit abandonnée. La vraie question n’est pas « quelle est la meilleure configuration ? » mais « quelle est la meilleure configuration que je suis capable de maintenir 18 mois sans relâcher ? ».

Un exemple : Qubes OS offre une compartimentation excellente, mais demande un matériel adapté, deux heures d’installation, une discipline opérationnelle, et une acceptation de friction quotidienne. Si la personne, après deux semaines, repasse à Windows par fatigue, le bénéfice net est négatif (elle a perdu du temps et n’a pas amélioré sa posture). Pour cette personne, un Linux durci + gestionnaire de mots de passe + clé FIDO2 est *meilleur* que Qubes, parce que c’est ce qu’elle tiendra.

#### 2.6 Trois niveaux de posture : N1 / N2 / N3

Pour éviter le sur-dimensionnement (et le sous-dimensionnement) qui sont les deux travers symétriques du threat modeling individuel, ce cours propose trois niveaux de posture explicites. Chaque chapitre indiquera, quand pertinent, à quel niveau telle mesure se rapporte.

**Niveau 1 — Hygiène essentielle**

- *Pour qui* : tout adulte connecté, sans contexte de menace personnalisée. La grande majorité des lecteurs.
- *Objectif* : réduire significativement la surface d’exposition au capitalisme de surveillance, à la criminalité opportuniste, aux fuites de credentials, aux harcèlements de bas niveau.
- *Stack type* : gestionnaire de mots de passe (Bitwarden) + MFA matériel (YubiKey) ou TOTP pour comptes critiques + Signal pour communications + chiffrement disque (BitLocker / FileVault / LUKS) + mises à jour disciplinées + sauvegardes 3-2-1 + uBlock Origin + DNS chiffré + ADP iCloud si Apple.
- *Coût* : 50-200 € de matériel (YubiKey, abonnement gestionnaire éventuel), 2-3 h de configuration initiale, 15-30 min par mois de maintenance.
- *Ce que ce niveau fait* : élimine 90 % du risque statistique.

**Niveau 2 — Profil exposé**

- *Pour qui* : journaliste, militant identifié, dirigeant d’entreprise sensible, personnalité publique modérée, professionnel du droit ou de la santé manipulant des dossiers sensibles, personne ayant un adversaire de proximité connu et motivé.
- *Objectif* : ajouter une compartimentation forte et une résistance aux attaques ciblées de niveau intermédiaire.
- *Stack type* : N1 + GrapheneOS sur Pixel dédié *ou* iPhone avec Lockdown Mode + SimpleX pour canaux les plus sensibles + Tails sur USB pour sessions ponctuelles + Mullvad VPN permanent + Mullvad Browser quotidien + email Proton avec alias + procédures BEC si pro + reboot quotidien des appareils sensibles.
- *Coût* : 500-1500 € (Pixel, USB Tails, abonnements), 1-2 jours de configuration initiale + apprentissage continu, 1-2 h par mois de maintenance disciplinée.

**Niveau 3 — HVT / source / journaliste sensible / cible documentée**

- *Pour qui* : journaliste avec enquête en cours sur acteurs ressourcés, lanceur d’alerte avant divulgation, opposant politique en exil, dissident, avocat de la défense sur dossier sensible, personne ayant reçu une *Threat Notification* d’Apple/Google/Meta.
- *Objectif* : résister aux attaques par spyware mercenaire, à l’analyse forensique avancée, à la coercition juridique transfrontière.
- *Stack type* : N2 + Qubes OS sur laptop principal + Whonix dans Qubes + GrapheneOS avec profils multiples + air-gap pour secrets long terme + MVT mensuel + iVerify + audit forensique périodique + plan d’incident documenté + équipe juridique mobilisable + relation établie avec Access Now / Citizen Lab.
- *Coût* : 2000-5000 € (matériel adapté Qubes, multiples appareils), 2-4 semaines d’apprentissage initial, 4-8 h par mois de maintenance, discipline opérationnelle continue.

**Note critique** : un niveau plus élevé ne se substitue pas à un niveau plus bas. Le Niveau 3 *contient* le Niveau 1. Une posture Niveau 3 mal entretenue sur les fondamentaux N1 (mot de passe réutilisé sur un compte de récupération) est moins solide qu’une posture N1 disciplinée. **Aucun lecteur ne devrait viser directement le N3 sans avoir maîtrisé le N1.**

**Anti-pattern à éviter** : se dimensionner en N3 par fascination technique alors que le threat model réel est N1. La friction qui en résulte épuise et conduit à abandonner *en bloc*, sortant alors en N0 (rien). Mieux vaut un N1 tenu dix ans qu’un N3 abandonné en deux mois.

#### 2.7 Matrice STRIDE/LINDDUN adaptée au particulier

Pour un audit plus structuré, deux taxonomies de menaces sont utiles.

**STRIDE** (Microsoft, focalisée sécurité) :

- **S**poofing — usurpation d’identité (compte piraté, SIM swap, faux mail au nom de…)
- **T**ampering — altération de données (modification de fichiers, faux documents)
- **R**epudiation — possibilité de nier une action (qui a fait quoi sur un appareil partagé ?)
- **I**nformation disclosure — fuite d’informations
- **D**enial of service — déni de service (compte bloqué, appareil rendu inutilisable)
- **E**levation of privilege — élévation de privilèges (admin sur ton appareil)

**LINDDUN** (focalisée privacy) :

- **L**inkability — possibilité de relier deux activités
- **I**dentifiability — possibilité d’identifier une personne derrière une activité
- **N**on-repudiation — impossibilité de nier une action (problème côté privacy)
- **D**etectability — possibilité de détecter qu’une activité a eu lieu
- **D**isclosure of information — divulgation d’information
- **U**nawareness — l’utilisateur ignore ce qui se passe avec ses données
- **N**oncompliance — non-conformité aux règles applicables

LINDDUN est particulièrement utile pour penser privacy plutôt que sécurité pure. *Linkability* notamment recoupe la surface de corrélation discutée au Ch 1.

#### 2.8 L’erreur « threat model trop complexe »

Privacy Guides a identifié un anti-pattern récurrent : la personne qui construit un threat model d’opposant politique alors qu’elle fait du tricot. Trois symptômes :

- Empilement d’outils dont la combinaison crée de nouvelles surfaces d’attaque (un VPN qui fuit, branché derrière un Tor mal configuré, sur un OS compromis).
- Procédures qui exigent une discipline permanente impossible à tenir (rotation manuelle de comptes hebdomadaire).
- Adversaires fantasmés qui justifient des mesures, en ignorant les adversaires réels.

Le bon test : *« Si l’adversaire que je redoute me ciblait demain, que ferait-il en premier ? »* La réponse, dans 90 % des cas, n’est pas un zero-day Pegasus. C’est un phishing, une réutilisation de mot de passe, une question de récupération de compte mal protégée, une publication imprudente d’un proche. Commence par ça.

#### 2.9 Définir ce qui est hors périmètre

Un threat model honnête liste explicitement ce qu’il *ne couvre pas* :

- « Je ne cherche pas à résister à une perquisition judiciaire en France. »
- « Je ne cherche pas à empêcher que ma banque sache combien j’ai sur mon compte. »
- « Je ne cherche pas l’anonymat sur LinkedIn, qui est mon outil professionnel. »
- « Je ne cherche pas à protéger contre un voleur qui aurait mon téléphone allumé et déverrouillé en main. »

Cette explicitation a deux vertus. D’abord, elle décharge la conscience : tu n’as pas à porter le poids de défenses contre tout. Ensuite, elle clarifie où placer les efforts.

#### 2.10 *Fil rouge* — Léa construit son premier threat model en 90 minutes

Léa Martens, journaliste freelance à Bruxelles, démarre son enquête en consortium. Elle s’assied avec un carnet et trois colonnes : actifs, adversaires, mesures.

**Actifs critiques** :

- Identité de ses sources (priorité absolue — la révéler les met en danger physique).
- Documents reçus (priorité haute — base de l’enquête).
- Carnet d’adresses (priorité haute — révèle ses relations).
- Communications avec ses sources (contenu *et* métadonnées).
- Son matériel et son domicile (sécurité personnelle).

**Adversaires plausibles** :

- Le commissaire visé (capacité moyenne via cabinet, motivation forte si l’enquête sort).
- La société de surveillance privée (capacité technique élevée — c’est leur métier — motivation modérée à élevée selon avancement).
- L’oligarque (capacité élevée via services achetés, motivation élevée).
- Services russes (capacité très élevée, motivation modérée à élevée si l’enquête touche).
- Trolls et harceleurs en ligne (capacité faible, motivation possible si l’enquête sort).

**Hors périmètre explicite** :

- Résistance à une saisie judiciaire belge ou française légale (Léa s’engage à respecter la loi locale et fera appel à son avocat si besoin).
- Anonymat sur LinkedIn et auprès de sa rédaction.
- Protection contre criminalité opportuniste classique (couverte par hygiène standard, pas spécifique à l’enquête).

**Mesures prioritaires identifiées** (à creuser dans les chapitres suivants) :

- Compartimentation stricte : un appareil enquête séparé du quotidien.
- Canal source ne passant pas par Gmail/WhatsApp.
- Réduction d’empreinte publique sur les réseaux sociaux *pendant* l’enquête.
- Audit de son entourage proche pour ne pas créer de fuite indirecte.
- Préparation à un possible voyage en pays sensible.

Le document tient sur deux pages. Léa le date, le chiffre dans son gestionnaire de mots de passe (qu’elle vient de mettre en place — cf. Ch 29), et se promet de le réviser tous les trimestres.

> 🟦 **Exercice du chapitre**
> Produis ton propre threat model en une page : 3 actifs prioritaires, 3 adversaires plausibles, 3 mesures réalistes, 3 éléments explicitement hors périmètre. Date-le, range-le, prévois sa relecture à 3 mois.

-----

### Chapitre 3 — Taxonomie des adversaires

Un adversaire n’est pas un autre. Confondre les catégories conduit à mal calibrer la défense. Voici les grandes familles, du moins ciblé au plus ciblé, avec leurs capacités, motivations et méthodes typiques.

#### 3.1 Surveillance de masse étatique

**Acteurs** : agences de renseignement (NSA, GCHQ, DGSE, BND, FSB, etc.), services de signalisation (SIGINT), partenariats inter-services (Five Eyes, Nine Eyes, Fourteen Eyes).

**Capacités** : collecte passive massive (interception de câbles sous-marins, points d’échange internet), rétention de métadonnées sur des durées variables selon les juridictions, accès légal aux opérateurs (réquisitions, lettres de sécurité nationale), capacité de déchiffrement limitée (la crypto moderne tient — c’est l’OPSEC et les endpoints qui tombent), et exploitation de zero-days lorsque ciblage justifié.

**Modèle** : surveillance *non ciblée par défaut*, ciblage *à la demande* lorsqu’une personne devient pertinente. Tu n’es pas écouté *spécifiquement* aujourd’hui, mais tes métadonnées circulent dans des bases dont la rétention varie.

**Méthodes pertinentes pour toi** : collecte de métadonnées (qui parle à qui, quand), géolocalisation cellulaire, analyse de graphes sociaux, exploitation des relations entre individus.

**Ce contre quoi protéger** : minimisation des métadonnées (messageries adaptées, Tor), compartimentation des identités, prudence sur les graphes de relation.

**Limite réaliste** : si tu es activement ciblé par un service étatique majeur, tu ne pourras pas gagner seul cette guerre. Ton objectif est de *rendre coûteux* le suivi et de minimiser ce qu’ils ont déjà.

#### 3.2 Capitalisme de surveillance

**Acteurs** : data brokers (Acxiom, LexisNexis, Spokeo, Intelius, Whitepages), ad-tech (Google, Meta, The Trade Desk, Criteo), courtiers de localisation (X-Mode, Cuebiq, Veraset — souvent revendus à des agences gouvernementales).

Une évolution préoccupante de ce modèle est l’ADINT (Advertising Intelligence) : l’exploitation des données et mécanismes publicitaires à des fins de renseignement. Des données initialement collectées pour le ciblage marketing — identifiants publicitaires, localisation, applications utilisées, signaux comportementaux — peuvent être revendues, agrégées ou exploitées pour suivre des individus, cartographier des groupes ou préparer des actions ciblées. L’ADINT illustre la porosité entre publicité, courtage de données, surveillance privée et renseignement étatique.

**Capacités** : agrégation massive de données issues d’applications mobiles, de cookies, de programmes de fidélité, de fuites, de registres publics, de réseaux sociaux. Construction de profils détaillés vendus à des fins publicitaires, mais aussi à des fins de scoring (crédit, assurance), de vérification (background check), voire à des forces de l’ordre via achat plutôt que mandat.

**Modèle** : profit par accumulation. Tu n’es pas la cible, tu es la marchandise.

**Méthodes** : SDK publicitaires dans les apps, cookies tiers (en déclin), fingerprinting (en croissance, cf. Ch 23), achat de bases de données fuitées, agrégation cross-device.

**Ce contre quoi protéger** : navigateurs anti-fingerprint (Ch 24), désinscription data brokers (Ch 6), minimisation des permissions mobiles (Ch 15), email aliasing (Ch 27), paiements compartimentés (Ch 32).

**Spécificité** : c’est l’adversaire le plus probable de tout lecteur. Et pourtant le moins fantasmé. La discipline anti-tracking quotidienne est le bénéfice immédiat de ce cours pour la grande majorité des gens.

#### 3.3 Plateformes elles-mêmes : Google, Meta, Apple, Microsoft, TikTok

**Acteurs** : les géants du numérique. Statut hybride entre fournisseurs et adversaires : tu leur confies des données pour utiliser leurs services, et eux les exploitent.

**Capacités** : accès intégral à ce que tu leur confies (emails Gmail, photos Google Photos, contacts iCloud, messages WhatsApp côté métadonnées, etc.). Capacité de réquisition judiciaire à laquelle ils répondent selon les juridictions et les procédures. Capacité d’analyse comportementale fine (Apple Intelligence, Gemini sur Android, etc.).

**Modèle** : variable selon la plateforme. Apple revendique un modèle moins intrusif (et Advanced Data Protection chiffre certaines données de bout en bout, cf. Ch 14 et 30). Google et Meta vivent du ciblage publicitaire. Microsoft est entre les deux. TikTok pose des questions spécifiques liées à sa juridiction.

**Méthodes pertinentes** : ce que tu leur donnes volontairement (essentiellement tout, si tu utilises leurs services sans précaution), enrichi par l’IA générative côté Microsoft Copilot et Apple Intelligence (Ch 34).

**Ce contre quoi protéger** : chiffrement côté client par-dessus le cloud (Ch 30), email auto-hébergé ou chez fournisseur E2EE (Ch 27), ADP iCloud activée si Apple, minimisation des comptes Google rattachés au principal.

#### 3.4 Censure et restriction d’accès

**Acteurs** : États autoritaires (Chine, Iran, Russie, Émirats, Vietnam, etc.) mais aussi démocratiques sur certains contenus (filtrage DNS au RU et en France pour terrorisme et pédocriminalité, etc.), FAI qui appliquent les ordres, plateformes qui appliquent les politiques.

**Capacités** : blocage DNS, blocage IP, deep packet inspection (DPI), perturbation de protocoles (Tor, VPN), obligation d’enregistrement, sanctions pénales pour les contournements.

**Ce contre quoi protéger** : VPN (Ch 20), Tor avec bridges (Ch 21), DNS chiffré (Ch 19), résolveurs alternatifs.

**Cadre légal** : varie radicalement selon les juridictions. En Iran, l’usage de VPN est techniquement illégal mais massif. En Chine, le contournement du Great Firewall expose à des sanctions. En France, le RGPD protège l’usage privé d’outils légitimes.

#### 3.5 Attaques ciblées : APT étatiques, mercenaires

**Acteurs étatiques** : APT chinois (APT10, APT41), russes (APT28, APT29, Turla), nord-coréens (Lazarus), iraniens (APT34, Charming Kitten), occidentaux aussi mais moins publiquement documentés. Les APT visent typiquement entreprises, gouvernements, ONG sensibles, dissidents.

**Acteurs mercenaires** : NSO Group (Pegasus), Intellexa (Predator), Paragon Solutions (Graphite), QuaDream, Candiru, Hacking Team (historique). Ces sociétés vendent à des États (parfois autoritaires) du spyware mobile de pointe.

**Capacités** : zero-days iOS/Android (zero-click parfois), exploits chaînés, infrastructure C2 résiliente, capacité de pivot et d’exfiltration.

**Cibles documentées par Citizen Lab et Amnesty Security Lab** : journalistes d’investigation, activistes des droits humains, avocats de la défense, leaders d’opposition, proches de cibles. Cas confirmés dans des dizaines de pays.

**Méthodes** : zero-click iMessage/WhatsApp (cas Pegasus FORCEDENTRY, cas Paragon Graphite 2024-2025), liens piégés ciblés, installation physique en transit, infection via Wi-Fi infrastructure compromise.

**Ce contre quoi protéger** : Lockdown Mode iOS (Ch 15), GrapheneOS, redémarrage régulier (zero-clicks souvent non persistants), MVT et iVerify (Ch 33), notifications Apple/WhatsApp/Google.

**Coût** : déploiement d’un spyware mercenaire coûte entre 10k$ et plusieurs millions selon la cible. *Tu n’es pas ciblé par défaut.* Si tu l’es, tu le sauras probablement par les notifications des plateformes.

#### 3.6 Criminalité opportuniste

**Acteurs** : groupes de cybercriminalité organisée, opérateurs ransomware, vendeurs de credentials, brokers d’accès, phishers de masse.

**Capacités** : kits de phishing prêts à l’emploi, base de credentials achetée sur forums, malware as a service, infrastructure botnet.

**Modèle** : volume. Tu n’es pas ciblé, tu es statistique. Si tu cliques sur le bon lien le bon jour, tu paies.

**Ce contre quoi protéger** : MFA fort, gestionnaire de mots de passe (Ch 29), méfiance des liens, mises à jour à jour, sauvegardes 3-2-1 (Ch 30).

#### 3.7 Adversaires de proximité

**Acteurs** : ex-partenaire (cas particulièrement fréquent et dangereux, notamment dans les contextes de violences conjugales), harceleur (stalker), famille intrusive ou hostile, employeur intrusif, journaliste hostile, voisin curieux.

**Capacités** : faibles techniquement, mais **élevées en connaissance préalable** — ils savent ton anniversaire, le nom de ton chien (souvent ton mot de passe), tes habitudes, tes lieux de passage. Ils ont parfois eu accès physique à tes appareils (voir spyware *stalkerware* commercial : mSpy, FlexiSpy, etc.).

**Modèle** : motivation très forte, capacité technique faible mais compensée par la proximité.

**Méthodes** : devinette de mot de passe, accès physique, stalkerware installé pendant la relation, observation OSINT classique, exploitation des proches.

**Ce contre quoi protéger** : changement complet de credentials après rupture, audit des appareils (cf. annexe 8 ressources Coalition Against Stalkerware), MFA matériel, séparation des comptes Apple/Google, sortie des comptes partagés, prudence Find My et localisation.

> 🟧 **À noter** : ce threat model est sous-traité dans la plupart des cours de cybersécurité, qui se focalisent sur l’étatique. Or pour une fraction significative de la population, l’adversaire principal est dans son entourage. Le **Cas D** en fin de cours traite spécifiquement ce scénario.

#### 3.8 Adversaires accidentels : l’entourage qui dénonce sans le savoir

Catégorie particulière. Ton frère qui te tague sur une photo Instagram à un anniversaire de famille révèle ta localisation à un harceleur. Ton collègue qui répond à un appel de prétexte donne ton emploi du temps à un ingénieur social. Tes parents qui rendent publique ta date de naissance et le nom de jeune fille de ta mère mettent la sécurité de tes questions de récupération en danger.

L’entourage n’est pas hostile mais constitue un vecteur d’exposition que tu ne contrôles pas. Une partie de la défense consiste à *éduquer* discrètement les personnes proches (Ch 35).

#### 3.9 HVT (High Value Targets) : qui est vraiment ciblé, qui se croit ciblé

**HVT réels** : journalistes d’investigation publiant sur des dossiers critiques, leaders d’opposition dans des régimes autoritaires, lanceurs d’alerte avant publication, avocats de la défense sur des dossiers sensibles, militants sur des sujets visés (climat radical, droits humains dans certains pays). Catégories documentées par Citizen Lab et Amnesty Security Lab comme cibles répétées de spyware mercenaire.

**HVT autoperçus mais peu probables** : la plupart des « privacy enthusiasts », des professionnels cyber non exposés professionnellement, des particuliers durcis. Ils auraient *tout intérêt* à concentrer leurs efforts sur les menaces réelles (capitalisme de surveillance, criminalité opportuniste, doxxing), plus probables et plus traitables.

**Test honnête de HVT-ness** : as-tu publiquement, et dans le dernier exercice de ton activité, produit une information qui mette en danger un acteur capable et motivé ? Si non, tu n’es probablement pas HVT. Si oui, tu l’es peut-être — et il est temps de durcir sérieusement.

> 🟩 **À retenir du chapitre 3**
> 
> - Le capitalisme de surveillance est l’adversaire le plus probable de tout le monde.
> - Les adversaires de proximité sont sous-évalués et particulièrement dangereux car ils ont de la connaissance préalable.
> - Les attaques mercenaires (Pegasus & co) sont réelles mais ciblent un nombre restreint de profils ; ne pas dimensionner sa défense sur ce seul axe.
> - Définir honnêtement son profil de HVT-ness conditionne tout le reste.

-----

### Chapitre 4 — Cartographie de l’empreinte et grands modèles d’exposition

L’objectif de ce chapitre est de produire une cartographie systématique de ce qui, depuis toi, s’échappe vers le monde extérieur. Sans cette cartographie, toute mesure défensive est aveugle.

#### 4.1 Empreinte volontaire, involontaire et héritée

L’**empreinte volontaire** est ce que tu publies consciemment : posts, photos, opinions, profil professionnel, contributions GitHub, articles. Elle est, en théorie, sous ton contrôle. En pratique, sa permanence (Wayback Machine, archives, captures) la rend irréversible.

L’**empreinte involontaire** est ce qui fuit sans intention : métadonnées de fichiers, géolocalisation de photos, fingerprints navigateur, requêtes DNS, données vendues par des applications.

L’**empreinte héritée** est ce que d’autres exposent sur toi : photos taguées par des amis, mentions dans des publications, témoignages, registres publics, données vendues par des courtiers qui t’ont profilé sans ton accord.

Les trois s’accumulent. Et seule la première est en théorie sous ton contrôle.

#### 4.2 Exposition par les comptes

L’email principal est le **centre de gravité** de l’identité numérique. Il est utilisé pour récupérer les mots de passe de la plupart des autres comptes. Sa compromission donne accès à la quasi-totalité de la vie numérique. Inversement, sa perte (faille, oubli, suspension par le fournisseur) cascade en perte massive.

L’audit des comptes consiste à dresser la liste de tous les services où tu as un compte. La plupart des gens, à cet exercice, en découvrent entre 100 et 500. Outils utiles : recherche dans les emails reçus (« welcome », « confirm your email »), historique de gestionnaire de mots de passe, vérification HaveIBeenPwned avec ton email principal.

Pour chaque compte critique, note : email associé, MFA activé ou non, type de MFA, dernière connexion, mot de passe unique ou non, données stockées.

#### 4.3 Exposition par les appareils

Chaque appareil collecte et transmet :

- Identifiants matériels : adresse MAC (Wi-Fi, Bluetooth), IMEI pour les téléphones, numéros de série, identifiants TPM, identifiants publicitaires (Advertising ID Android, IDFA iOS — désactivables).
- Capteurs : GPS, accéléromètre (qui révèle des modes de transport, des activités physiques), microphone, caméra.
- Connectivité : Wi-Fi probing (le téléphone qui hurle les noms des réseaux passés), Bluetooth/BLE beacons.
- Logiciels installés : chaque application installe son SDK, qui collecte typiquement plus que ce que l’application semble faire.

#### 4.4 Exposition par les applications

Les applications mobiles sont des vecteurs sous-estimés. Une appli météo typique demande accès à la localisation précise (raisonnable), au stockage (douteux), aux contacts (suspect), à l’identifiant publicitaire (mauvais signe). Beaucoup d’applis intègrent 5 à 30 SDK tiers, chacun avec ses propres flux de données.

**Test pratique** : sur ton téléphone, ouvre les paramètres → confidentialité → audit des permissions. Combien d’applis ont accès à ta localisation en arrière-plan ? À tes contacts ? À ton micro ? Réponse moyenne : beaucoup trop.

#### 4.5 Exposition par le réseau

Chaque connexion réseau révèle :

- **IP source** : identifie ton FAI et ta localisation grossière (souvent ville).
- **Requête DNS** : révèle les noms de domaine que tu consultes (sauf DoH/DoT — Ch 19).
- **SNI** (Server Name Indication) : révèle l’hôte que tu joins, même en HTTPS (sauf ECH — Ch 19).
- **Métadonnées TLS** : horodatages, suites cryptographiques, taille des échanges.
- **Wi-Fi et Bluetooth** : émissions radio en clair de probes et de beacons.

Le FAI voit *tout* ce qui passe par sa box (sauf si VPN). Les opérateurs cellulaires aussi. Les exploitants de Wi-Fi public également.

#### 4.6 Exposition par le cloud

La synchronisation automatique est la fuite cloud la plus massive. Les photos iCloud/Google Photos s’uploadent automatiquement avec leurs métadonnées EXIF (Ch 31). Les contacts iCloud/Google synchronisent ton carnet d’adresses chez Apple/Google. Les sauvegardes WhatsApp dans iCloud/Google Drive ne sont pas chiffrées de bout en bout par défaut (et le sont seulement si activées explicitement).

Quand Apple Advanced Data Protection (ADP) est activée, une partie significative des données iCloud devient chiffrée de bout en bout (photos, sauvegardes iCloud, notes, rappels, signets Safari, etc.). Mais : les contacts, le calendrier, et les mails iCloud restent accessibles à Apple pour des raisons d’interopérabilité (Ch 14 et 30).

#### 4.7 Exposition par les métadonnées

Les métadonnées sont le gisement le plus sous-estimé. À traiter en profondeur au Ch 31, mais à mentionner ici :

- **EXIF photo** : coordonnées GPS, modèle d’appareil, numéro de série, horodatage, profil ICC personnalisé qui peut identifier l’écran de prise de vue ou de retouche.
- **PDF** : auteur, logiciel de création, historique de révisions, objets cachés, signatures invisibles.
- **Office (DOCX/XLSX/PPTX)** : auteur, commentaires, suivi des modifications activé sans en avoir conscience.
- **Audio/vidéo** : tags, codecs, traces de montage, voire artefacts d’enregistrement (gyroscope révélant le modèle exact d’iPhone).

#### 4.8 Exposition par l’entourage

Le graphe social est un identifiant en soi. Deux personnes ayant 15 contacts en commun sont probablement reliées d’une façon ou d’une autre. Les plateformes (Facebook, LinkedIn, Instagram, Snapchat) construisent ces graphes en permanence. Le « people you may know » est l’application directe de cette analyse.

Tes proches publient à ton sujet sans en mesurer l’impact : photo de famille géolocalisée, mention de ton lieu de travail dans un post de félicitations professionnelles, lien social public sur Facebook.

#### 4.9 Exposition par les habitudes

L’analyse comportementale identifie des motifs : tu te connectes à Tor tous les jeudis à 22h ; tu écris en moyenne 60 mots par minute avec un certain rythme ; tu utilises certaines tournures (cf. stylométrie, Ch 35) ; tu consultes certains sites à certaines heures. Pris isolément, chaque indicateur est insignifiant. Agrégés, ils forment une signature.

**Conséquence opérationnelle** : si tu ouvres un nouveau pseudonyme et que tu le pratiques avec les mêmes habitudes que ton identité connue, le pseudonyme se corrélera à terme.

#### 4.10 Exposition par les fuites

HaveIBeenPwned recense, en 2025-2026, plus de 13 milliards de credentials exposées issues de fuites passées. Si tu utilises internet depuis plus de cinq ans, ton email principal a presque certainement été inclus dans au moins une fuite. Le contenu varie : email + mot de passe (le plus courant), email + numéro de téléphone, profil complet (LinkedIn 2021), informations bancaires (rares mais existantes).

Ces fuites alimentent :

- Le *credential stuffing* : tentative automatisée de réutilisation des mots de passe fuités sur d’autres services. Première cause de compromission de comptes pour la majorité des utilisateurs.
- L’OSINT : un attaquant peut croiser ton email avec une fuite pour obtenir d’autres infos (numéro de téléphone, anciens mots de passe pouvant révéler des motifs).
- Le *doxxing* : agrégation pour produire un dossier ciblé.

#### 4.11 Méthode d’audit personnel en 10 étapes

À faire une première fois sérieusement, puis à répéter tous les six mois.

1. **Lister ses comptes** : recherche dans email principal des termes “welcome”, “verify your email”, “confirm”. Compléter avec le gestionnaire de mots de passe.
1. **Tester son email principal sur HaveIBeenPwned** : noter les fuites confirmées.
1. **Audit des permissions mobiles** : sur iOS Réglages → Confidentialité ; sur Android Paramètres → Confidentialité → Gestionnaire d’autorisations.
1. **Recherche de son nom et email** sur les moteurs (Google, Bing, DuckDuckGo) — sans être connecté, sur navigateur privé.
1. **Reverse image search** sur ses photos publiques (Yandex Images, PimEyes, Google Lens).
1. **Audit des réseaux sociaux** : qui peut voir quoi, qui sont mes amis, qu’ai-je publié au cours de la dernière année, mes photos sont-elles taguées ?
1. **Audit des sessions actives** sur Google, Apple, Microsoft, Facebook : appareils connectés, dernière activité, sessions à révoquer.
1. **Audit du gestionnaire de mots de passe** : mots de passe réutilisés, mots de passe faibles, comptes sans MFA.
1. **Audit cloud** : que synchronise mon téléphone ? Mon ordinateur ? Ai-je activé ADP (Apple) ou équivalent ?
1. **Recherche de soi sur data brokers** : Spokeo, BeenVerified, Whitepages, Pages Jaunes (FR), Société.com.

À l’issue de cet audit, tu auras une carte. Le reste du cours t’apprendra à la réduire.

#### 4.12 *Fil rouge* — Audit complet de Léa

Léa fait l’exercice. Ses résultats, en synthèse :

**Top 20 des fuites identifiées** :

1. Email professionnel dans 7 fuites HaveIBeenPwned (dont LinkedIn 2021 et Adobe 2013).
1. Numéro de téléphone trouvable sur LinkedIn (paramètre par défaut).
1. Adresse postale visible via une ancienne souscription à une association (avant RGPD).
1. Date d’anniversaire publique sur Facebook (paramètre par défaut).
1. Nom de jeune fille de sa mère trouvable via un faire-part de mariage scanné en ligne.
1. Photos d’enfance avec géolocalisation EXIF intacte sur Flickr (compte oublié de 2010).
1. Adresse email principale utilisée pour 200+ services (centre de gravité absolu).
1. Aucun MFA sur Gmail (récupération par SMS uniquement).
1. iCloud sans ADP activée.
1. WhatsApp synchronisé dans iCloud, sauvegardes non chiffrées par défaut.
1. Carnet d’adresses iCloud → contient les numéros de plusieurs sources potentielles.
1. Compte Twitter/X avec géotag occasionnel activé.
1. Account-pivoted via PimEyes : photos professionnelles publiques permettent reverse image vers comptes personnels.
1. Identifiants publicitaires actifs sur téléphone (IDFA + Android ID secondaire).
1. Réutilisation d’un même pseudo « LeaM » sur trois forums professionnels, dont un lié à son identité civile.
1. Présence Strava active avec parcours de course incluant son domicile et son bureau.
1. GitHub avec son nom civil et email pro, contributions horodatées révélant son rythme de travail.
1. Mailing-list professionnelle archivée publiquement avec ses anciennes adresses.
1. Photos taguées par son frère sur Instagram révèlent vacances, famille, lieux fréquentés.
1. Adresse postale et téléphone fixe dans le registre du commerce belge (entreprise individuelle).

**Décision** : avant tout outil de chiffrement, Léa décide de consacrer deux week-ends à réduire cette empreinte. Le reste du cours l’accompagne dans cette démarche.

> 🟩 **À retenir du chapitre 4**
> 
> - L’empreinte numérique a trois dimensions : volontaire, involontaire, héritée.
> - Neuf vecteurs d’exposition à auditer systématiquement.
> - L’audit personnel en 10 étapes est le préalable à toute action de durcissement.
> - L’email principal est le centre de gravité : sa protection prime sur tout.
> - Beaucoup de gens découvrent à l’audit que leurs « gros risques perçus » sont moins critiques que des fuites banales déjà acquises.

-----

## Partie 2 — Identité, compartimentation et hygiène comportementale

> **Objectif** : passer de la cartographie à l’action. Avant de durcir des appareils ou de chiffrer des canaux, il faut réduire ce qui fuit déjà, contrôler ce qu’on expose, et architecturer la séparation entre les compartiments de sa vie.

-----

### Chapitre 5 — OSINT défensif : auditer son propre profil

#### 5.1 Pourquoi s’OSINTer soi-même est l’étape zéro

Un attaquant qui s’intéresse à toi commence par une recherche ouverte. Tant que tu n’as pas fait cette recherche à sa place, tu défends à l’aveugle. L’OSINT défensif inverse la posture : tu te mets dans la peau de l’adversaire, tu reproduis sa démarche, tu mesures ce qu’il trouvera, puis tu réduis. Ce chapitre est le miroir défensif du cours OSINT Mastery (voir cours dédié pour la méthode offensive complète).

#### 5.2 Méthode systématique en six axes

L’OSINT défensif sérieux suit une méthode. Improviser conduit à manquer des angles.

**Axe 1 — Identité civile** : recherche par nom + prénom + ville sur Google, Bing, DuckDuckGo. Pas connecté à un compte. En navigation privée. Avec et sans guillemets. Puis variantes orthographiques. Puis combinaison nom + employeur, nom + ancien lieu d’études.

**Axe 2 — Emails** : tester chaque email connu sur HaveIBeenPwned, Intelligence X, DeHashed (limites légales selon juridictions). Identifier dans quelles fuites tu apparais, quelles données ont été exposées.

**Axe 3 — Pseudonymes** : faire la liste de tous tes pseudonymes (Twitter, Reddit, GitHub, forums, gaming, dating). Pour chacun, recherche directe et username pivot avec des outils comme WhatsMyName ou Sherlock.

**Axe 4 — Numéros de téléphone** : recherche du numéro sur Google, mais aussi sur Truecaller, Sync.me (gardez en tête : ces services sont eux-mêmes intrusifs ; recherchez via un compte temporaire ou via un proche).

**Axe 5 — Photos** : reverse image sur Yandex Images (souvent le plus efficace pour les visages), Google Lens, TinEye, PimEyes (payant, contestable éthiquement), FaceCheck.ID. Tester ses photos professionnelles, ses photos de profil, ses photos publiques.

**Axe 6 — Documents publics** : registres du commerce, archives administratives, listes électorales (selon pays), publications scientifiques, contributions GitHub, mailing-lists archivées.

#### 5.3 Outils de référence (2025-2026)

- **HaveIBeenPwned** (gratuit, référence) : fuites de credentials.
- **Intelligence X** (freemium) : recherche dans des dumps, paste sites, Tor.
- **Epieos** (freemium) : recherche par email, téléphone, nom.
- **Hunter.io** : recherche d’emails par domaine (utile pour vérifier ce qu’on expose côté professionnel).
- **Wayback Machine** : archives du web ; vérifier ce qui de toi a été archivé.
- **WhatsMyName, Sherlock** (gratuits) : recherche de pseudonyme sur des centaines de plateformes.
- **PimEyes, FaceCheck.ID** : reverse image faciale (à utiliser avec une photo *non* affiliée à tes comptes principaux pour éviter d’alimenter leurs bases).

**Limite éthique et légale** : certains de ces outils opèrent en zone grise. PimEyes a été condamné en plusieurs juridictions. L’usage à des fins d’audit défensif sur soi-même est généralement légitime ; l’usage sur des tiers sans consentement ne l’est pas. Ce cours ne couvre pas l’usage offensif.

#### 5.4 Cartographier les liens entre comptes

Le danger n’est pas chaque compte individuellement, c’est leur connexion. Si l’attaquant prouve que @LeaMartens (Twitter) et lea.martens@gmail.com et leam94 (GitHub) appartiennent à la même personne, il a un graphe complet. La carte que tu produis doit donc inclure ces ponts : reuse d’email entre comptes, photo identique sur deux profils, même biographie, références croisées (« mon GitHub : leam94 » dans le profil Twitter), mêmes contacts mutuels.

#### 5.5 Limites de l’auto-OSINT

Tu ne trouveras pas tout ce qu’un attaquant motivé trouvera. Tes angles morts incluent : bases de données vendues qui ne sont pas publiquement indexées, données obtenues par requête judiciaire ou réquisition, données dans des forums fermés, données issues d’OSINT humain (questions posées à ton entourage). L’OSINT défensif est nécessaire mais pas suffisant. Il borne ce que *tout adversaire* trouvera trivialement — pas ce qu’un adversaire ressourcé reconstituera.

#### 5.6 *Fil rouge* — Léa fait son OSINT

Léa applique la méthode. Découvertes notables :

- Une vieille photo de classe lycée scannée par une ancienne camarade et postée publiquement sur Facebook, indexée par Google Images, retrouvée par reverse image à partir de sa photo LinkedIn.
- Un mémo professionnel PDF, mis en ligne par un ancien employeur, contenant son nom dans les métadonnées XMP même si retiré du texte visible.
- Un compte de forum nutrition (2014, pseudo lea.m_94) avec son adresse email principale, son alimentation, et ses lieux fréquentés.
- Trois pages d’archives de mailing-lists journalistiques où son adresse pro apparaît en clair.

Elle constate que l’attaquant compétent reconstituerait son identité civile, sa carrière, ses fréquentations professionnelles, et un certain nombre de détails personnels en moins d’une heure. Elle priorise.

-----

### Chapitre 6 — Data brokers, courtiers de données et désinscription effective

#### 6.1 Anatomie du marché

Les data brokers compilent, à partir de sources légales (registres publics, programmes de fidélité, applications mobiles vendant leurs données, fuites achetées, données dérivées des plateformes), des profils détaillés revendus à des annonceurs, des assureurs, des banques, et — point critique — à des forces de l’ordre via achat plutôt que mandat judiciaire (cas documenté aux États-Unis : ICE achète à des courtiers ce qu’ils ne pourraient obtenir sans mandat).

Aux États-Unis, l’industrie est florissante (Acxiom, LexisNexis, Spokeo, BeenVerified, Whitepages, Intelius, ID Analytics, etc.). En Europe, le RGPD limite — sans empêcher — la pratique. En France, des courtiers existent (Société.com, Pages Jaunes Pro, Easyfichiers, etc.) sur des bases plus limitées.

#### 6.2 Cas français et européens

En France et en Europe, les sources principales de profilage sont :

- Le registre du commerce et des sociétés (gérants, adresses, capitaux).
- Les annuaires (Pages Jaunes, Pages Blanches — désinscription possible).
- Les listes électorales (consultables sous conditions).
- Les annonces légales (publications obligatoires).
- Le BODACC pour les dirigeants.
- Les sites de fuites agrégant des bases européennes.
- Les anciens annuaires d’écoles et d’universités.

Le RGPD permet d’invoquer le droit à l’effacement (article 17) et le droit d’opposition (article 21). Ces droits sont opposables à tout responsable de traitement basé en UE ou ciblant des résidents UE.

#### 6.3 Désinscription manuelle vs services payants

Les services type DeleteMe (US), Optery, Incogni, Privacy Bee automatisent la désinscription auprès de centaines de courtiers. Avantages : gain de temps. Limites : couverture incomplète (surtout courtiers européens), efficacité partielle (certains courtiers réinscrivent), modèle économique qui suppose une renouvellement (les courtiers re-collectent en continu), confiance à accorder au service lui-même (qui reçoit en bonus une liste de tes données).

La désinscription manuelle reste l’option maximaliste : long, fastidieux, mais traçable. Pour la France, deux types de courriers utiles :

- Demande de droit à l’effacement (article 17 RGPD) avec justificatif d’identité, à adresser au DPO du courtier.
- Demande d’opposition (article 21) avec motif (généralement : « finalité de prospection commerciale »).

En cas de refus ou de non-réponse sous un mois : réclamation à la CNIL.

#### 6.4 Le piège : la désinscription qui re-confirme

Certains courtiers exigent, pour te désinscrire, que tu confirmes ton identité et tes données déjà détenues. Cela peut paradoxalement *enrichir* leur base si tu fournis des données qu’ils n’avaient pas. Règle : fournis le strict minimum exigé légalement, et conserve une copie de tes envois.

Autre piège : la désinscription via un courtier *re-confirme* qu’un humain réel se cache derrière ce profil. Pour certains courtiers, c’est plus précieux que la donnée brute.

#### 6.5 Maintenance : le ré-empilage et la routine semestrielle

Les courtiers ré-acquièrent constamment de nouvelles données (achats de bases, agrégation depuis applications). Une désinscription n’est pas définitive. Il faut prévoir un cycle semestriel ou annuel :

1. Recherche de soi sur les principaux courtiers.
1. Identification des nouveaux apparitions.
1. Réémission des demandes RGPD.
1. Suivi des réponses.

C’est un travail à organiser, à dater, à documenter. Sans cette routine, tout reflue en six mois.

#### 6.6 Limite réelle

Tu ne nettoieras jamais à 100 %. Certaines bases ne sont pas indexables, certaines fuites sont irrécupérables (une fois sur Telegram, une donnée y reste), certaines juridictions n’appliquent pas le RGPD. La désinscription est *complémentaire* à la compartimentation, pas un substitut. Pour les nouveaux comptes, tu créeras une nouvelle empreinte ; à toi de l’architecturer mieux.

-----

### Chapitre 7 — Doxxing : mécanique, prévention et réponse

#### 7.1 Définition et formes

Le **doxxing** (parfois orthographié *doxing*) consiste à révéler publiquement des informations personnelles identifiantes (nom réel, adresse, employeur, contacts familiaux, photos privées) sur une cible, dans une intention nuisible : harcèlement, intimidation, atteinte professionnelle, violences physiques par procuration.

Formes principales :

- **Doxxing classique** : publication d’une fiche identifiante.
- **Swatting** : appel des forces d’intervention à l’adresse de la cible sous prétexte fallacieux. Documenté avec des morts aux États-Unis. Risque croissant en Europe.
- **Harcèlement coordonné** : campagne organisée (raid sur un compte, signalements coordonnés, messages massifs).
- **Doxxing par deepfake** : association de la cible à des contenus fabriqués (cf. Ch 34).
- **Doxxing patrimonial** : révélation d’informations sur la famille, les enfants, l’école, le lieu de travail.

#### 7.2 Anatomie d’une opération de doxxing

Une opération typique suit cinq phases :

1. **Trigger** : action de la cible (publication, prise de position, conflit en ligne) qui motive l’attaque.
1. **Reconnaissance** : OSINT sur la cible (cf. Ch 5 inversé).
1. **Compilation** : assemblage d’une fiche avec les informations agrégées.
1. **Publication** : sur un forum hostile, un site dédié, ou via des canaux de chat.
1. **Amplification** : appel à harcèlement de masse.

La défense efficace agit aux phases 2 et 3 : réduire ce qui est trouvable, casser les corrélations qui permettent l’assemblage.

#### 7.3 Profils particulièrement ciblés

Les données disponibles (rapports PEN America, Online Harassment Field Manual, Coalition Against Online Violence) identifient comme cibles surreprésentées : femmes journalistes, journalistes traitant de l’extrême-droite ou des questions de genre, activistes LGBTQ+, chercheurs sur les mouvements extrémistes, victimes de gamergates et de raids ciblés, témoins dans des affaires sensibles.

#### 7.4 Prévention structurelle

Sept axes prioritaires :

1. **Adresse postale alternative** : boîte postale, domiciliation commerciale (légale, ~15-30€/mois), ou adresse d’un proche consentant. À utiliser pour tout enregistrement public, livraisons sensibles.
1. **Téléphone séparé** : un numéro pro distinct du numéro principal — eSIM, MVNO, ou service comme MySudo (US), JMP.chat. Ce numéro filtre les contacts professionnels.
1. **Hygiène photo** : éviter les arrière-plans identifiants, les marquages industriels (entreprises locales), les vues par fenêtre permettant la géolocalisation visuelle (cf. Ch 35).
1. **Audit de l’entourage** : tes proches publient-ils ton nom, ton adresse, tes photos ? Conversation diplomatique recommandée.
1. **Compartimentation des plateformes** : ton compte professionnel n’a pas besoin de mentionner ton compte personnel, et inversement.
1. **Filtrage des questions de récupération** : pas de question dont la réponse est dans tes posts publics (« nom de ton chien »).
1. **Surveillance proactive** : Google Alerts sur ton nom, monitoring HaveIBeenPwned (notifications automatiques de nouvelles fuites).

#### 7.5 Réponse à doxxing en cours

Si tu es la cible d’un doxxing actif :

1. **Documenter** : captures d’écran, URLs, horodatages. Préserver les preuves avant suppression éventuelle.
1. **Signaler aux plateformes** : la plupart ont des procédures spécifiques anti-doxxing (X, Reddit, GitHub, Discord, etc.).
1. **Contacter les hébergeurs** (si nécessaire) : un site dédié peut être signalé à son hébergeur, à son registrar, et à son CDN.
1. **Évaluer la menace physique** : si l’adresse est publiée et qu’il y a menace crédible, prévenir les autorités, envisager un changement temporaire de logement.
1. **Soutien psychologique et juridique** : pas un détail. Le doxxing est traumatisant. PEN America, GIJN, RSF, La Quadrature, Reporters Sans Frontières proposent des aides selon les profils.
1. **Plainte** : en France, le doxxing peut tomber sous plusieurs qualifications (atteinte à la vie privée, violation du secret des correspondances, mise en danger délibérée, harcèlement). PHAROS pour le signalement.

#### 7.6 *Fil rouge* — Léa découvre son adresse sur un forum

Trois semaines après une publication intermédiaire sur son enquête, Léa reçoit une capture d’écran d’un canal Telegram : son adresse postale, son numéro de téléphone, et le nom de son père y sont publiés, avec « cette journaliste mérite une visite ». Application immédiate de la procédure ci-dessus. Mise en alerte de son entourage proche. Dépôt de plainte. Et surtout, leçon : son adresse était dans le registre du commerce belge (entreprise individuelle) — elle bascule en SCI avec domiciliation commerciale dans la semaine.

-----

### Chapitre 8 — Réseaux sociaux et exposition publique

#### 8.1 Le modèle économique = surveillance

Les paramètres « privacy » des plateformes ne neutralisent pas le modèle : la plateforme te surveille toujours en interne (clics, durée de visualisation, position du pouce, contacts, photos, métadonnées). Ce qu’ils contrôlent, c’est ce que d’autres utilisateurs voient de toi. Ne pas confondre les deux.

#### 8.2 Audit de présence

Avant de durcir, mesure. Pour chaque plateforme où tu as un compte :

- Date de création, fréquence d’usage.
- Quelles informations sont publiques sur ton profil (nom, date de naissance, employeur, ville, école, téléphone).
- Quelles photos sont publiques et taguées.
- Quelles relations sont publiques (followers, amis, contacts).
- Quel historique de publication est public et combien remonte.
- Quels paramètres de confidentialité par défaut sont actifs.

Pour Facebook spécifiquement, utiliser l’outil intégré « Apparaître en tant que » pour voir ton profil comme un inconnu le voit. Découverte fréquente : ce que tu croyais privé est public.

#### 8.3 Paramétrage défensif par plateforme

**Facebook / Meta** : profil verrouillé (public uniquement nom et photo), audience par défaut « Amis », désactivation de la reconnaissance faciale, désactivation du tagging automatique, restriction des recherches par email/téléphone, vérification de l’historique de publications.

**Instagram** : compte privé si possible, désactivation du suggéré, désactivation de la synchronisation des contacts (Instagram aspire ton carnet d’adresses si activé), audit des photos taguées.

**X (Twitter)** : protéger les tweets si pertinent, désactiver la découverte par email/téléphone, désactiver les DM ouverts si pas indispensable.

**LinkedIn** : limitation de la visibilité du profil aux moteurs (paramètre dédié), choix de ce qui apparaît au public vs aux connexions, suppression des notifications publiques de changements (« John updated his profile »), désactivation du « people you may know ».

**TikTok** : compte privé, désactivation du téléchargement de tes vidéos par d’autres, restriction des duets/stitch.

**Bluesky, Mastodon** : décentralisé, mais ton serveur (instance) voit tout. Choisir une instance de confiance. Comportement à publication reste sous ton contrôle.

#### 8.4 Photos et tagging

Les photos sont le vecteur sous-estimé. Quatre risques :

1. **Géolocalisation** : EXIF + arrière-plan + indices visuels.
1. **Identification croisée** : la même photo sur deux comptes les corrèle.
1. **Reconnaissance faciale** : PimEyes et FaceCheck.ID indexent en continu.
1. **Tagging par des tiers** : tu n’as pas le contrôle de ce que tes proches publient avec toi.

Mesures : photos de profil dédiées (jamais utilisées ailleurs), demande explicite à tes proches de ne pas te taguer, désactivation des suggestions de tag automatique, audit régulier des photos publiées par d’autres.

#### 8.5 Métadonnées invisibles côté plateforme

Même quand une plateforme retire les EXIF côté serveur (la plupart le font), elle conserve en interne : horodatage exact, géolocalisation au moment de l’upload, modèle d’appareil. Ces données ne sont pas publiques mais sont accessibles à la plateforme et, sur réquisition, aux autorités.

#### 8.6 Silence stratégique

Ce que tu **ne publies pas** compte autant que ce que tu publies :

- Pas de photos de vacances en temps réel (signale ta maison vide).
- Pas de check-in dans des lieux récurrents (signale tes habitudes).
- Pas d’humeur en temps réel sur tes opinions politiques clivantes si tu vis dans un contexte risqué.
- Pas de mention de tes proches sans leur consentement.
- Pas d’achat coûteux affiché (signale la valeur de ton logement).

#### 8.7 Suppression vs désactivation vs anonymisation

**Désactivation** : compte invisible mais récupérable. Tes données restent chez la plateforme.

**Suppression** : effacement (en théorie) après un délai de grâce (30 jours typiquement). En pratique, les sauvegardes plateformes peuvent conserver certaines données plus longtemps. Les archives publiques (Wayback, ArchiveTeam) conservent ce qu’elles ont aspiré.

**Anonymisation progressive** : changer nom, photo, biographie, mais garder le compte. Permet de conserver l’historique de relations sans afficher l’identité. Utile sur les comptes anciens.

#### 8.8 Alternatives décentralisées

Mastodon et Bluesky proposent un modèle fédéré qui change la juridiction (instance choisie) et le modèle économique (souvent associatif). Mais :

- Tes posts sont publics par design.
- Ton instance voit tout (administrateur compris).
- La fédération expose certaines données à d’autres instances.

Ce ne sont pas des refuges privacy, ce sont des alternatives au modèle économique. Pas la même chose.

-----

### Chapitre 9 — Compartimentation et hygiène comportementale

#### 9.1 Principe directeur

La compartimentation consiste à structurer ta vie numérique en compartiments étanches, tels que la compromission de l’un n’expose pas les autres. C’est l’architecture défensive la plus puissante disponible à un individu, et celle qui demande le plus de discipline.

Règle : *deux choses qui ne doivent pas être reliées ne doivent jamais l’être par un identifiant commun*. Email, téléphone, photo, appareil, IP, mot de passe, style d’écriture, horaire — chacun peut être un pont.

#### 9.2 Niveaux d’identité

Cinq niveaux typiques à distinguer :

1. **Identité légale** : nom civil, état civil, documents administratifs. Pour les démarches officielles, le travail, les contrats, les comptes bancaires.
1. **Identité professionnelle** : nom (peut différer si pseudonyme journalistique), email pro, présence professionnelle. Compartiment majeur pour beaucoup de profils.
1. **Pseudonyme stable** : présence en ligne sous nom de plume, militante, communautaire. Pas anonyme (long terme), mais distinct de l’identité civile.
1. **Pseudonyme jetable** : compte créé pour un usage ponctuel, abandonné après.
1. **Identité anonyme** : pour des actions où l’attribution doit être impossible (sources sensibles, lanceurs d’alerte avant divulgation).

Tous les niveaux n’ont pas le même besoin de défense. Mais ceux qui doivent rester séparés doivent l’être *complètement*.

#### 9.3 Compartimenter par dimension

Cinq dimensions de compartimentation :

|Dimension          |Compartimentation faible            |Compartimentation forte                           |
|-------------------|------------------------------------|--------------------------------------------------|
|**Appareil**       |Profils OS séparés                  |Appareils physiquement distincts                  |
|**Compte**         |Comptes séparés sur même fournisseur|Fournisseurs différents par usage                 |
|**Numéro**         |Cartes SIM différentes              |Réseaux différents (eSIM + physique + service IP) |
|**Paiement**       |Cartes virtuelles différentes       |Cartes physiques + cash + dénoués géographiquement|
|**Lieu et horaire**|Distinction maison/bureau           |Lieux totalement disjoints, horaires distincts    |

Le niveau adéquat dépend du threat model. Un journaliste enquêtant sur la criminalité organisée a besoin d’une compartimentation forte de la dimension *appareil* et *numéro* au minimum.

#### 9.4 Réutilisation : les corrélateurs silencieux

Les corrélations les plus efficaces ne demandent aucune compétence technique. La réutilisation d’un même identifiant entre deux compartiments les corrèle automatiquement :

- Même email : trivial à corréler.
- Même mot de passe entre comptes : la fuite de l’un dévoile l’autre.
- Même pseudo : `whatsmyname.app` te trouve sur 300 services en quelques secondes.
- Même numéro de téléphone : agrégateurs (Truecaller, Sync.me) corrèlent à grande échelle.
- Même photo de profil : reverse image trouve en quelques minutes.
- Même biographie textuelle : recherche exacte sur Google.

#### 9.5 Corrélation par style, contacts, métadonnées

Au-delà des identifiants explicites, des corrélations probabilistes :

- **Style d’écriture** (stylométrie, Ch 35) : longueur de phrases, virgules, expressions, fautes typiques.
- **Horaires de connexion** : ton compte « anonyme » se connecte aux mêmes heures que ton compte nominal.
- **Contacts communs** : deux comptes qui suivent les mêmes 50 personnes sont probablement la même.
- **Appareil/navigateur** : même fingerprint navigateur (cf. Ch 23) = même session probable.
- **IP** : connexion depuis le même réseau domestique sur deux comptes les corrèle (à moins de VPN).
- **Métadonnées de fichiers** : un document publié sous pseudonyme avec l’auteur metadata DOCX = nom civil dans le PDF.

#### 9.6 L’erreur ponctuelle qui suffit

La compartimentation rigoureuse, c’est une discipline continue. **Une seule erreur peut la détruire**. Trois exemples historiques :

- Ross Ulbricht (Silk Road) : pseudonyme « altoid » sur un forum cryptographique posté avec son email gmail au format `rossulbricht@gmail.com`. Cf. Annexe 8.
- Hector Monsegur (Sabu, LulzSec) : connexion une seule fois à IRC sans Tor depuis son IP domestique. Cf. Annexe 8.
- Cas Reality Winner : impression d’un document classifié sur l’imprimante de son employeur. Les yellow dots (Ch 31) identifiaient l’imprimante, la date, l’heure. Cf. Annexe 8.

Conséquence opérationnelle : **les routines tuent les erreurs**. Si un comportement sensible est automatique (par exemple : impossibilité physique de se connecter au compte sensible depuis le téléphone quotidien parce qu’aucune appli n’est installée), l’erreur est structurellement empêchée.

#### 9.7 Fatigue OPSEC, impulsivité, urgence

La compartimentation est attaquée de l’intérieur par trois ennemis humains :

- **Fatigue** : maintenir deux téléphones, plusieurs comptes, plusieurs gestionnaires de mots de passe, c’est lourd. Au bout de six mois, on relâche.
- **Impulsivité** : « juste cette fois, je me connecte vite à mon compte X depuis ce téléphone ». Une fois suffit pour casser la séparation.
- **Urgence** : un événement (deadline, alerte familiale, opportunité professionnelle) pousse à enfreindre les règles « pour cette fois ».

Défenses : (a) automatiser et désautoriser ; (b) accepter que la friction est le prix de la sécurité ; (c) prévoir des protocoles d’urgence qui ne nécessitent pas d’enfreindre la compartimentation.

#### 9.8 Routines pour limiter les erreurs

- Démarrer chaque session sensible par une checklist physique (carte plastifiée, post-it).
- Avoir un appareil dédié physiquement distinct, jamais le « téléphone du moment ».
- Établir des règles non négociables : « jamais cet email sur cet appareil », « jamais ce compte sans VPN ».
- Audit trimestriel des dérives.

#### 9.9 Cadrage éthique

La compartimentation et le pseudonymat sont des outils défensifs *légitimes*. Un journaliste qui utilise un pseudonyme pour ses enquêtes, un lanceur d’alerte qui sépare ses canaux, une victime de violences conjugales qui restructure ses comptes pour échapper à un ex-partenaire abusif : tous exercent des droits.

Ce n’est pas le sujet de ce cours d’aborder l’usurpation d’identité, la création de faux profils trompeurs, ou la fraude à pseudonymes. Ces pratiques sont pénalement répréhensibles dans la plupart des juridictions et ne relèvent pas de la sécurité défensive.

-----

> 🟦 **Capstone 1 — Construire son architecture de compartimentation**
> 
> **Objectif** : produire pour soi une matrice de compartimentation opérationnelle, applicable dans les 7 jours.
> 
> **Livrable** : un tableau cinq colonnes (Identité / Appareils / Comptes / Paiements / Canaux) pour chacun de tes compartiments principaux. Pour chaque ligne, identifier les ponts existants (ce qui *relie* deux compartiments) et les éliminer un à un.
> 
> **Exemple — Léa, fin de capstone** :
> 
> |Compartiment         |Identité                            |Appareils                      |Comptes                                |Paiements              |Canaux                                   |
> |---------------------|------------------------------------|-------------------------------|---------------------------------------|-----------------------|-----------------------------------------|
> |Vie civile et famille|Léa Martens (nom civil)             |iPhone perso, MacBook Air perso|iCloud personnel, Gmail perso          |CB BNP perso           |iMessage, WhatsApp avec proches          |
> |Vie pro publique     |Léa Martens journaliste             |MacBook Pro pro                |Proton Mail pro, comptes sociaux pro   |CB pro                 |Email, Signal pro                        |
> |Enquête sensible     |Pseudo non utilisé (compte distinct)|Pixel 8a + GrapheneOS dédié    |Compte SimpleX dédié, Proton avec alias|Cash + cartes prépayées|SimpleX, OnionShare, Signal compartimenté|
> 
> **Ponts à éliminer identifiés par Léa** :
> 
> - Carnet d’adresses iCloud personnel contient des numéros de sources potentielles → migration vers carnet pro.
> - Synchronisation iCloud des photos perso pourrait remonter à des photos pro accidentelles → désactivation de la sync auto, tri manuel.
> - Même MacBook Air pour usage perso et certains comptes pro → bascule vers MacBook Pro pour tout pro.
> - Compte Twitter perso suit le pseudo qui sera utilisé pour publication d’enquête → désabonnement préalable.

## Partie 3 — Sécurité matérielle, racine de confiance et isolation

> **Objectif** : descendre dans la pile, du silicium au bureau, pour comprendre ce qu’on défend réellement. La sécurité applicative ne tient que si la base tient. Ce qui se passe avant le système d’exploitation conditionne ce qui se passe après.

-----

### Chapitre 10 — Sécurité matérielle : choix, supply chain, intégrité physique

#### 10.1 Modèle d’attaque physique

L’attaquant physique est radicalement plus dangereux que l’attaquant distant. S’il a accès à ton appareil, même brièvement, la plupart des défenses logicielles s’effondrent. Quatre scénarios :

- **Vol opportuniste** : sac arraché, ordinateur oublié au café. Adversaire faible, mais accès total à l’appareil éteint puis allumé.
- **Evil maid** : accès temporaire pendant ton absence (chambre d’hôtel, bureau, frontière). Adversaire compétent : modification de firmware, ajout de keylogger matériel, clonage de disque, implantation de backdoor.
- **Saisie** : douane, perquisition, arrestation. Adversaire étatique avec accès quasi illimité à l’appareil.
- **Coercition** : tu es présent et contraint de fournir codes et accès. Aucune défense technique pure n’y résiste totalement.

Le chiffrement complet (Ch 12) protège contre vol et saisie *si l’appareil est en BFU (Before First Unlock)*. Il protège peu contre evil maid (qui agit sur l’appareil éteint mais peut pré-installer des éléments qui s’activeront après ton déverrouillage). Il ne protège pas contre coercition.

#### 10.2 Choix de matériel : coprocesseurs de sécurité

Les laptops modernes intègrent souvent un coprocesseur dédié à la sécurité, qui isole les opérations cryptographiques sensibles du processeur principal :

- **Apple Silicon (M1/M2/M3/M4)** : Secure Enclave intégré au SoC, gère les clés de chiffrement FileVault, Touch ID, déverrouillage. Architecture mature et auditée.
- **Microsoft Pluton** : disponible sur certains processeurs AMD Ryzen et Intel récents (à partir de 2022, généralisé en 2024-2025). Coprocesseur sécurisé directement dans le CPU.
- **Google Titan M2** sur Pixel : équivalent Secure Enclave côté Android, gère le déverrouillage, l’attestation, le stockage de clés.
- **TPM 2.0 discret** : sur la majorité des laptops Windows depuis 2021. Moins intégré qu’un coprocesseur dédié mais offre des garanties cryptographiques sérieuses (Ch 11).

**Conséquence pratique** : un Pixel récent + GrapheneOS, un MacBook Apple Silicon, ou un laptop Windows avec Pluton offrent aujourd’hui de bien meilleures garanties matérielles qu’un laptop générique sans TPM.

#### 10.3 ThinkPad, Framework et le choix Linux

Pour ceux qui veulent du Linux durci, deux choix s’imposent en 2025-2026 :

- **ThinkPad** récents (T14, X1 Carbon, P-series) : bon support Linux, TPM 2.0, qualité industrielle, certaines références supportent Coreboot ou Heads (cf. Ch 11).
- **Framework Laptop** : modulaire, support Linux excellent, choix éthique sur la réparabilité.

Risque commun : les **mises à jour firmware** dépendent du constructeur. Sur ThinkPad, fwupd/LVFS gère bien. Sur d’autres marques, les firmwares restent obscurs et rarement mis à jour côté Linux.

#### 10.4 Supply chain

L’attaquant peut intercepter ton matériel entre la commande et la livraison. Cas documentés : NSA TAO interceptait des routeurs Cisco avant livraison pour y implanter des backdoors (révélations Snowden). Pour un individu :

- Acheter directement en magasin physique limite l’interception postale.
- L’achat d’occasion expose à un matériel déjà compromis ou modifié.
- Le refurbishing professionnel certifié réduit ce risque sans l’éliminer.
- Pour les cibles à haut risque : achat en personne, dans un magasin choisi au dernier moment, paiement cash.

#### 10.5 Détection d’intrusion physique

Tu ne peux pas empêcher l’evil maid si l’attaquant est compétent. Tu peux le *détecter*, ce qui change la stratégie défensive : un appareil suspecté de compromission n’est plus utilisé pour le sensible.

Techniques élémentaires :

- **Vis non standard** sur les panneaux d’accès (Torx Security, etc.).
- **Vernis à ongles glittery** sur les vis et joints du boîtier : motif unique, photographié pour comparaison ultérieure.
- **Photo macro** de la disposition des composants internes lors de l’achat, pour comparaison.
- **Scellés** sur les ports USB inutilisés.
- **Câble Kensington** ou solution équivalente quand l’appareil est en lieu non sûr.

Aucune de ces techniques n’arrête un attaquant gouvernemental sérieux, mais elles arrêtent l’attaquant moyen et imposent un coût supérieur au reste.

#### 10.6 Disposal sécurisé

Quand un appareil sort de ton circuit (revente, recyclage, défaillance), il emporte tes données. Trois niveaux :

- **Disque mécanique (HDD)** : effacement multipasses (DBAN, NIST 800-88 Clear) reste valide.
- **SSD** : l’effacement logique est moins fiable (wear leveling). La commande `cryptographic erase` via le firmware SSD (souvent `hdparm --security-erase`) est plus efficace. En dernier recours : broyage physique. ANSSI recommande la destruction physique pour les SSD contenant des secrets sensibles.
- **Téléphones** : reset usine + chiffrement actif est généralement suffisant. Sur GrapheneOS, la procédure inclut un effacement complet du stockage chiffré.

#### 10.7 Périphériques non fiables

USB et ports d’extension sont les vecteurs sous-estimés. BadUSB (Hak5 Rubber Ducky et clones) émule un clavier et tape des commandes à grande vitesse dès le branchement. Les câbles peuvent être piégés (O.MG cables).

Règles : ne jamais brancher un USB inconnu ; pour le chargement public, préférer un câble *data-only-off* (ou un USB condom comme PortaPow) ; sur Linux, paquet `usbguard` qui bloque les périphériques USB non whitelistés ; sur Windows, Device Guard et Credential Guard.

#### 10.8 Webcam, micro, capteurs

Couverture caméra physique : trivial, efficace. Apple le déconseille sur MacBook (risque d’écraser le mécanisme), mais une fine pellicule autocollante reste sans risque. Pour le micro : sur certains laptops, un interrupteur matériel (Framework, certains ThinkPad). Sinon, désactivation logicielle (qui peut être contournée par malware) ou retrait physique du module si nécessaire.

Sur smartphone, les modes « micro/caméra coupés au niveau OS » de iOS (indicateurs verts) et GrapheneOS (toggle système) offrent des garanties matérielles. Sur Android stock, ces indicateurs existent mais l’OS reste contournable par exploits.

> 🟩 **À retenir du chapitre 10**
> 
> - Attaquant physique > attaquant distant. Le matériel est la racine.
> - Coprocesseurs de sécurité (Secure Enclave, Pluton, Titan M2) changent la donne.
> - Tu ne peux pas empêcher l’evil maid compétent, tu peux le détecter.
> - Disposal sécurisé : SSD = effacement crypto ou broyage.
> - Le minimum réaliste pour la plupart : laptop récent avec TPM 2.0, BitLocker/FileVault/LUKS, vis vernies, vigilance sur les USB.

-----

### Chapitre 11 — Firmware, UEFI, Secure Boot, TPM et chaîne de démarrage

#### 11.1 Qu’est-ce que le firmware et pourquoi c’est critique

Le **firmware** est le code qui s’exécute avant ton système d’exploitation, et qui le charge. Il vit dans une puce de la carte mère, accessible avant tout antivirus, tout chiffrement, tout système de détection. Un firmware compromis = persistance totale, invisible, irrémédiable par réinstallation du système.

UEFI a remplacé le BIOS historique en apportant : démarrage plus rapide, prise en charge de disques > 2 To, et surtout *Secure Boot*, qui vérifie cryptographiquement chaque étape de la chaîne de démarrage.

#### 11.2 Secure Boot : principe et limites

Secure Boot vérifie que chaque composant chargé (bootloader, noyau, drivers) est signé par une autorité de confiance. Ce qui n’est pas signé ne s’exécute pas. Cela bloque les rootkits qui s’injectaient au démarrage.

Mais Secure Boot a été attaqué :

- **BlackLotus** (2022-2023) : bootkit UEFI capable de bypass Secure Boot via une signature légitime mais vulnérable de bootloader Windows.
- **LogoFAIL** (2023) : exploit dans le parsing d’images BMP/PNG affichées au démarrage permettant l’exécution de code avant Secure Boot.

Conséquence : Secure Boot est *nécessaire* mais pas *suffisant*. Sa désactivation laisse une fenêtre d’attaque ouverte ; son activation, sans mise à jour firmware, laisse aussi des fenêtres connues.

#### 11.3 TPM 2.0

Le **Trusted Platform Module** est une puce dédiée au stockage de clés cryptographiques et à la mesure de l’état du système. Il est utilisé typiquement pour :

- Stocker la clé de déchiffrement disque (FileVault, BitLocker, LUKS+systemd-cryptenroll).
- Mesurer la chaîne de démarrage (Measured Boot) et libérer ces clés *seulement* si l’état correspond à un état attendu.
- Attester à un service distant que l’appareil n’a pas été modifié.

**Effet pratique** : avec TPM 2.0 et déverrouillage automatique du disque, ton ordinateur déverrouille tout seul s’il démarre dans un état attendu, mais si quelqu’un a modifié le firmware, le bootloader ou les paramètres TPM, le déverrouillage échoue et tu es prévenu d’une intrusion. C’est puissant — mais cela suppose que tu surveilles les échecs (souvent un échec TPM est interprété par l’utilisateur comme un bug à contourner, ce qui annule la protection).

#### 11.4 Coreboot, Heads, Pureboot

Pour qui veut sortir du firmware constructeur (souvent opaque) :

- **Coreboot** : firmware open source minimaliste, supporté sur certains ThinkPad et autres modèles.
- **Heads** : firmware sécurisé basé sur Coreboot, conçu pour la sécurité physique (vérification cryptographique de tout le boot + clé GPG matérielle).
- **PureBoot** : commercial (Purism), basé sur Coreboot + Heads.

Ces options sont réservées à un public technique et acceptant une perte de fonctionnalités (suspend parfois cassé, certaines fonctions matérielles indisponibles).

#### 11.5 Mises à jour firmware

Sur Linux, **fwupd** + le LVFS (Linux Vendor Firmware Service) permettent des mises à jour automatiques de firmware pour les marques compatibles (Dell, Lenovo récents, HP, Framework, certains autres). C’est l’un des chantiers les plus aboutis de Linux desktop ces dernières années.

Sur Windows, les mises à jour firmware passent par Windows Update pour les marques OEM intégrées.

Sur macOS, les mises à jour firmware sont incluses dans les mises à jour système.

Sur Android, dépend du constructeur. Pixel et iPhone reçoivent les mises à jour rapidement. Marques moyennes : variable. Marques basses : souvent rien après deux ans.

#### 11.6 Limites : Intel ME, AMD PSP

Tous les CPU Intel récents intègrent un **Management Engine** (ME), tous les AMD un **Platform Security Processor** (PSP). Ce sont des sous-systèmes propriétaires fonctionnant à un niveau supérieur au système d’exploitation, avec accès complet à la mémoire, au réseau, à tous les périphériques.

Ils sont *nécessaires* au fonctionnement (gestion d’énergie, boot, etc.) et *non désactivables* complètement par l’utilisateur. Certains laptops permettent de neutraliser partiellement Intel ME (`me_cleaner`), au prix de fonctionnalités. Pour la plupart des usages : on vit avec, en sachant que le matériel n’est pas totalement transparent.

#### 11.7 *Fil rouge* — Olivier soupçonne une modification UEFI

Olivier M., dirigeant d’une PME de chiffrement, rentre d’un séjour à Pékin où son laptop a passé deux heures hors de sa vue à l’hôtel. À son retour, il constate que l’écran de démarrage met deux secondes de plus à afficher. Possible coïncidence, possible LogoFAIL. Il :

1. N’utilise pas l’appareil pour quoi que ce soit de sensible.
1. Compare la photo macro qu’il avait prise du boîtier interne avant départ avec une nouvelle photo.
1. Sort le disque et le déchiffre depuis un autre poste sain pour récupérer ses documents.
1. Retire le SSD, le détruit physiquement, considère le laptop comme grillé.

Le coût (un MacBook) est inférieur à l’incertitude.

-----

### Chapitre 12 — Chiffrement complet du disque

#### 12.1 Pourquoi le chiffrement de session ne suffit pas

Un mot de passe utilisateur sans chiffrement disque est un théâtre. Quiconque démonte le disque accède aux fichiers via un autre système. Le chiffrement complet du disque (Full Disk Encryption, FDE) rend les données illisibles sans la clé de déchiffrement.

#### 12.2 LUKS / dm-crypt sous Linux

**LUKS** (Linux Unified Key Setup) est la norme Linux. AES-XTS 256 bits par défaut, multiples slots de clés, possibilité d’utiliser TPM via `systemd-cryptenroll` pour déverrouillage automatique. Configuration typique : volume chiffré contenant un volume LVM, avec partition racine et home.

LUKS2 (2018+) apporte Argon2id pour la dérivation de clé — résistance aux attaques par force brute matérielle.

**Déni plausible** : LUKS ne le propose pas nativement. VeraCrypt (hérité de TrueCrypt) propose des volumes cachés, mais leur efficacité dépend du modèle d’adversaire. Si l’adversaire sait que VeraCrypt est installé, l’existence d’un volume caché est probable, ce qui peut tourner contre toi.

#### 12.3 BitLocker

BitLocker chiffre les volumes Windows. AES-XTS 128 ou 256 bits, intégré au TPM 2.0. Trois modes :

- **TPM only** (par défaut sur Windows 11 Home) : déverrouillage automatique. Vulnérable à attaque physique BFU si attaquant compétent (extraction de clé via debug du TPM ou contournement contextuel).
- **TPM + PIN** : ajout d’un code court tapé au démarrage. Bien plus solide.
- **Startup key** sur USB : variation rare.

**Récupération** : par défaut, la clé de récupération est sauvegardée dans ton compte Microsoft cloud. C’est un compromis : tu n’es pas verrouillé hors de tes données si oubli du mot de passe, mais Microsoft (et qui le force) peut accéder à ta clé. Pour profil sensible : désactiver la sauvegarde cloud de la clé et la stocker hors ligne.

#### 12.4 FileVault

FileVault chiffre les volumes macOS. AES-XTS 128 bits, intégré au Secure Enclave sur Apple Silicon. La clé est protégée par le Secure Enclave : impossible à extraire même avec accès physique total (à l’état de l’art public).

**Récupération** : par défaut, optionnel via iCloud ou clé de récupération imprimable. Choix : iCloud = confort, clé = autonomie.

#### 12.5 Pre-Boot Authentication vs auto-déverrouillage TPM

**Pre-Boot Authentication (PBA)** : tu tapes le mot de passe au démarrage, avant que l’OS charge. Plus sécurisé, moins ergonomique.

**Auto-déverrouillage TPM** : le TPM libère la clé si l’état du système est conforme. Plus ergonomique. Le compromis : un attaquant qui maintient la cohérence d’état (par exemple en clonant l’appareil) peut potentiellement déverrouiller hors de ta présence.

Profil journaliste/HVT : PBA. Profil quotidien : TPM + PIN.

#### 12.6 Conteneurs chiffrés

Au-dessus du chiffrement disque, des outils pour conteneurs individuels :

- **VeraCrypt** : conteneurs portables, support multi-OS, volumes cachés.
- **Cryptomator** : focalisé cloud (chiffre des dossiers destinés à Dropbox, Google Drive, etc.).
- **gocryptfs / EncFS** : montage chiffré transparent sous Linux.
- **Zed!** (Prim’X) : usage spécifique francophone (justice, AAI, secteur public) ; conteneurs auto-extractibles chiffrés ; reconnu CC EAL3+ et qualifié ANSSI ; pratique pour transmettre un dossier sensible à un correspondant non technique.

#### 12.7 Attaques connues contre FDE

- **Cold boot attack** : la RAM conserve les données quelques secondes après extinction. Avec spray refroidisseur (azote ou simplement air comprimé inversé), ce délai s’étend à plusieurs minutes. Attaque réelle démontrée contre des laptops saisis allumés. Défense : utiliser des modes de sommeil profond qui purgent la RAM, privilégier l’extinction complète pour un appareil non utilisé, et choisir un OS qui efface la clé maître à la mise en veille (FileVault et BitLocker récents le font dans certaines configurations).
- **DMA via Thunderbolt / FireWire (historique)** : attaque par accès direct mémoire via port physique. Thunderbolt expose un canal DMA qui, mal configuré, permet à un périphérique connecté de lire la RAM. Démontrée par les attaques *Thunderspy* (2020) contre Thunderbolt 1/2/3. Mitigations : Intel a introduit Kernel DMA Protection sur les machines modernes ; macOS et Windows ont des modes d’autorisation des périphériques Thunderbolt. Défense additionnelle : désactiver Thunderbolt si non nécessaire, ou configurer IOMMU. Sur Linux, vérifier que IOMMU est actif (`dmesg | grep -i iommu`).
- **Sleep mode** : sur certains OS et configurations, le sleep maintient les clés de chiffrement disque en RAM pour permettre une reprise rapide. Saisir un laptop en sleep est donc proche de le saisir en AFU. La protection ne tient pleinement que sur appareil **éteint complètement**. Sur macOS, la commande `pmset -a destroyfvkeyonstandby 1` détruit la clé FileVault à l’entrée en hibernation. Sur Linux avec LUKS, `cryptsetup luksSuspend` purge la clé pendant le sleep. Sur Windows, BitLocker en mode TPM seul est vulnérable au démarrage sans intervention ; activer BitLocker avec PIN renforce.
- **Direct Memory Access via FireWire (obsolète mais culture utile)** : ancienne attaque sur laptops anciens, désormais rare.
- **Évolution récente — attaques sur TPM bus** : démontré par Andrew Tierney (Pen Test Partners, 2021) et chercheurs en 2023-2024, certains TPM discrets (puce séparée sur la carte mère) exposent les communications avec le CPU sur un bus LPC ou SPI qui peut être sniffé physiquement par un attaquant disposant du matériel. La clé BitLocker (en mode TPM seul) peut alors être extraite. Les TPM firmware (intégrés au CPU comme Pluton ou la Secure Enclave Apple) ne sont pas vulnérables à cette attaque. **Conséquence** : sur laptop Windows avec TPM 2.0 discret, BitLocker + PIN est meilleur que BitLocker TPM-only.
- **Côté SSD** : certains SSD revendiquent un chiffrement matériel transparent (self-encrypting drives, SED). Plusieurs travaux (Meijer & van Gastel, 2018) ont démontré que des implémentations SED commerciales étaient gravement défaillantes. Conclusion pratique : ne pas se reposer sur le chiffrement matériel SSD seul ; utiliser BitLocker / FileVault / LUKS par-dessus.

#### 12.8 BFU vs AFU

**BFU (Before First Unlock)** : l’appareil a été redémarré et n’a pas encore été déverrouillé. La plupart des données utilisateur sont chiffrées avec une clé non encore dérivée. C’est l’état le plus sécurisé.

**AFU (After First Unlock)** : l’appareil a été déverrouillé au moins une fois depuis le démarrage. Beaucoup de clés sont en mémoire ou dans le keychain. Un appareil saisi en AFU est largement plus accessible aux outils forensiques (Cellebrite, GrayKey).

**Conséquence opérationnelle critique** : avant une frontière, une manifestation, une situation à risque de saisie — *éteindre complètement* l’appareil, pas seulement le verrouiller. La différence BFU/AFU est l’un des arbitrages les plus importants du quotidien sécurisé. iPhone : maintenir bouton + volume jusqu’à arrêt complet. Android : même principe. Une fonction « Lockdown Mode » sur certaines versions Android entraîne aussi un mode équivalent à BFU partiel.

#### 12.9 Quand le chiffrement ne sert à rien

Si l’appareil est saisi *allumé et déverrouillé*, le chiffrement disque est sans effet : les clés sont actives, les fichiers sont en clair pour le système. C’est pourquoi la coercition (saisie avec personne consciente, déverrouillage par biométrie sans consentement actif) est si efficace, et pourquoi les juridictions divergent fortement sur l’admissibilité de l’usage forcé de biométrie (cf. Ch 37).

-----

### Chapitre 13 — Air gap, appareils dédiés et environnements isolés

#### 13.1 Ce qu’est vraiment un air gap

Un **air gap** est l’isolation physique d’un système : aucune connexion réseau, aucune liaison sans fil active, idéalement aucune connexion Bluetooth, NFC, USB en service. L’air gap est une mesure radicale, utile pour des actifs cryptographiques d’extrême sensibilité : clés PGP maîtres, clés de signature de logiciels, semences de portefeuilles cryptomonnaie, archives ultra-sensibles.

L’air gap n’est pas la solution du quotidien. Il a un coût opérationnel élevé (transfert manuel par USB ou QR code, maintenance des mises à jour, latence d’usage). Il est valable seulement pour des cas où la valeur protégée justifie ce coût.

#### 13.2 Cas d’usage légitimes

- **Clés PGP de signature** : si tu signes des logiciels distribués à grande échelle, la compromission de ta clé est catastrophique. Une station offline pour générer et utiliser cette clé est rationnelle.
- **Cold wallet cryptomonnaie** : la même logique. La majorité des vols de crypto provient de wallets connectés.
- **Archives sensibles** : documents source d’une enquête, exemplaires de référence.
- **Génération de secrets long terme** : clés racines, phrases de récupération.

#### 13.3 Limites pratiques

Le transfert de données vers/depuis l’air gap est le maillon faible. Trois options :

- **USB** : risque BadUSB, malware. Mitigation : ne brancher sur l’air gap que des USB neuves, marquées, jamais re-circulées.
- **QR code** : pour de petits volumes (clé publique, transaction crypto signée). Sécurité visuelle.
- **Data diode** : matériel unidirectionnel (transfert que dans un sens). Existe commercialement, coûteux. Utilisé en environnement industriel et gouvernemental.

#### 13.4 TEMPEST et side channels : culture générale

Les **side channels** sont des fuites d’information par des canaux non prévus : émissions électromagnétiques (écran, câble), acoustique (clavier audible), thermique, consommation électrique. La discipline TEMPEST (NSA / OTAN) standardise les mesures de blindage.

Pour un individu : ces attaques sont rares et coûteuses. Elles deviennent réalistes pour des HVT extrêmes. Mesures basiques de prudence : pas de travail sensible visible par fenêtre, pas de clavier proche de micro non sécurisé, pas de transmission radio (Wi-Fi/Bluetooth) sur l’air gap.

#### 13.5 Quand l’air gap est utile, inutile ou dangereux

**Utile** : protection d’un secret extrêmement coûteux à recréer, dont la compromission est catastrophique.

**Inutile** : protection d’usages quotidiens (mail, navigation). L’air gap pour tout = inopérant.

**Dangereux** : faux sentiment de sécurité. Un air gap mal entretenu (USB infectés, mises à jour absentes, manipulation imprudente) peut être pire qu’une station sécurisée connectée, parce qu’on ne le surveille pas.

#### 13.6 Workflow d’un appareil dédié

Un appareil air-gap typique :

1. **Acquisition** : matériel acheté en personne, payé cash idéalement (au moins pour profils Niveau 3), ouvert et photographié à l’achat. Pour des HVT extrêmes : achat dans un magasin choisi au dernier moment, après plusieurs heures de marche sans téléphone, dans une ville différente de la résidence.
1. **Installation initiale** : système d’exploitation minimal (Linux durci comme Debian ou Tails persisté, Qubes vault, OpenBSD pour profil exotique sérieux), aucun service réseau actif. Désactiver Bluetooth et Wi-Fi *au niveau matériel* si possible (cartes amovibles retirées physiquement sur certains laptops). Effacer le module Bluetooth/Wi-Fi de la BIOS-UEFI.
1. **Mise en service** : génération des secrets directement sur l’appareil. **Jamais d’import** depuis un autre système, car cela mettrait les secrets en contact avec un environnement non éprouvé. Pour une clé PGP maîtresse : `gpg --full-generate-key` avec 4096 bits RSA ou Ed25519, après avoir vérifié que l’entropie est suffisante.
1. **Sous-clés et révocation** : générer des sous-clés (signature, chiffrement, authentification) avec expiration courte (6-12 mois) qui seront exportées vers un appareil connecté pour usage quotidien. La clé maîtresse reste sur l’air gap. **Générer immédiatement le certificat de révocation** et le stocker hors-ligne (papier dans coffre, par exemple) : il sera la seule façon de révoquer la clé en cas de compromission ou de perte de l’air gap.
1. **Transfert sécurisé** : entrée des données par canal contrôlé.
- **USB neuve** : marquer la clé physiquement, n’écrire qu’une fois, formater en read-only après écriture, jamais réutiliser entre l’air gap et un autre système après une seule rotation.
- **QR code** : pour de petits volumes (clé publique, transaction crypto signée). Sécurité visuelle, scan via caméra du système connecté qui reste isolé du système air-gap.
- **Audio modem** (rare, profil HVT extrême) : transfert de petite quantité par audio entre deux machines.
- **Data diode** : matériel unidirectionnel commercial (Owl Cyber Defense, Waterfall Security) ; coûte plusieurs k€, utilisé en environnements industriels et gouvernementaux.
1. **Stockage** : coffre-fort physique, ou faraday bag, dans un lieu non public. Plusieurs copies dans des lieux distincts pour résilience (un exemplaire chez l’avocat ou parent de confiance) pour les secrets critiques (clés maîtres, semences crypto). Les copies doivent être identiques et l’usage doit garder la traçabilité.
1. **Audit** : périodicité régulière (semestrielle pour Niveau 3), vérification d’intégrité physique (vis, photos macro internes comparées), test de fonctionnement.
1. **Mise à jour** : difficulté structurelle de l’air gap. Soit on accepte de ne pas mettre à jour (et on accepte le risque CVE), soit on prépare une procédure de mise à jour disciplinée : téléchargement signé du paquet sur un système séparé, vérification de signature, transfert par USB neuve, application, retrait de l’USB. Cette procédure introduit un risque résiduel d’evil USB ; à arbitrer selon le threat model.
1. **Retraite** : effacement par `shred` sur tous les disques (HDD), `cryptographic erase` sur SSD via `hdparm --security-erase` ou équivalent, puis destruction physique (broyage, perçage de chaque plateau ou puce). Documentation de la destruction pour audit.

> 🟧 **Note de niveau** : l’air gap est typiquement une mesure Niveau 3. Pour Niveau 1, c’est inutile et excessif. Pour Niveau 2, c’est utile pour quelques secrets long terme (clé maître PGP de journaliste, semence d’un cold wallet familial conséquent) mais pas pour des opérations courantes.

-----

### Chapitre 14 — Durcissement Windows, macOS et Linux pour le quotidien

> **Niveau de posture (cf. Ch 2.6)** : ce chapitre couvre essentiellement le **Niveau 1** (hygiène essentielle de l’OS quotidien) avec des extensions vers le **Niveau 2** (sandboxing applicatif sérieux, AppArmor/SELinux personnalisés, Lockdown Mode macOS). Le **Niveau 3** se construit sur la base d’un OS durci selon ce chapitre, puis ajoute la compartimentation Qubes (Ch 17-18), Tails ou Whonix.

#### 14.1 Windows 11 : baseline raisonnable

**Édition** : Pro ou Enterprise pour avoir BitLocker complet, Hyper-V, Windows Sandbox, et plus de contrôle sur la télémétrie. Home est limité.

**Compte** : préférer un compte local (contournement possible à l’installation en désactivant le Wi-Fi avant l’écran de connexion Microsoft, ou via `oobe\BypassNRO`). Si compte Microsoft requis, dissocier le compte cloud de l’usage local autant que possible.

**Télémétrie** : Group Policy `Allow Telemetry = Security` sur Enterprise, `Basic` ailleurs. Désactivation via Settings → Privacy. Limites : Microsoft conserve un niveau de télémétrie irréductible.

**Defender, SmartScreen, Tamper Protection** : activés, par défaut, fonctionnent bien sur Windows 11. Ne pas les désactiver sauf raison spécifique.

**Audit minimal** : sessions Microsoft account, audit `Sysmon` si tu es technique, désactivation des services inutiles via `services.msc` (avec prudence).

#### 14.2 macOS

**FileVault** : activer dès la première utilisation.

**Gatekeeper et SIP** : laisser activés. Gatekeeper vérifie les signatures des applications installées. SIP (System Integrity Protection) empêche même root de modifier certaines parties système.

**XProtect** : antivirus intégré, mis à jour silencieusement. Pas de scan visible, mais protections actives.

**Lockdown Mode** (macOS Sonoma et plus, Ventura partiel) : conçu pour cibles à haut risque. Désactive certaines fonctionnalités (pièces jointes complexes en Messages, certaines APIs JS dans Safari, certains profils de configuration). Active uniquement si HVT.

**iCloud** : activer **Advanced Data Protection** dans Réglages → ton nom → iCloud → Protection avancée des données. Cela bascule en E2EE : iCloud Drive, photos, sauvegardes iCloud, notes, rappels, signets Safari, Mémos, et plus. Restent en non-E2EE : Mail, Contacts, Calendrier (pour raisons d’interopérabilité). ADP nécessite tous tes appareils sous version récente et une clé de récupération à conserver.

**Audit en 30 min** : Système → Confidentialité (revue des permissions par catégorie), Système → Sécurité (FileVault, Firewall, Lockdown Mode), désactivation des notifications sur écran verrouillé pour comptes sensibles.

#### 14.3 Linux : choix de distribution

- **Debian stable** : ennuyeux au bon sens du terme. Stable, sûr, ennuyeux. Recommandé pour serveur ou usage discipliné.
- **Fedora Workstation** : récent, sécurité par défaut sérieuse (SELinux, sandboxing), bonne intégration GNOME.
- **Ubuntu LTS** : pragmatique, large communauté, certaines préoccupations sur Snap.
- **Kicksecure** : Debian durcie au démarrage (config sécurisée par défaut, plus de durcissement kernel). Base technique de Whonix. Pour usage régulier hors anonymat Tor.
- **Arch** : pour qui veut tout contrôler. Coût d’apprentissage élevé.
- **NixOS, Fedora Silverblue** : intéressants conceptuellement (système immuable, rollback). Pour utilisateurs avancés.

Le choix est moins important que la discipline qui suit.

#### 14.4 AppArmor / SELinux : contrôle d’accès obligatoire

Linux moderne propose des modèles de **Mandatory Access Control** : règles obligatoires que même root respecte.

- **AppArmor** (Debian, Ubuntu, SUSE) : profils par application, syntaxe accessible.
- **SELinux** (Fedora, RHEL, CentOS) : plus puissant, syntaxe plus complexe.

Pour la plupart des utilisateurs : laisser le profil par défaut, sans désactiver. Pour usage durci : créer ou raffiner des profils pour les applications sensibles (navigateur, gestionnaire de mots de passe).

#### 14.5 Sandboxing applicatif

- **Flatpak + bubblewrap** : isolement par défaut des applications Flatpak. Utile pour navigateurs (Firefox flatpak isolé), clients de messagerie.
- **Firejail** : sandbox basée sur namespaces et seccomp. Profils existants pour la plupart des applications courantes. Limite réelle de Firejail signalée par certains audits : peut élever des privilèges si mal configuré. Préférer Flatpak quand possible.
- **systemd-nspawn** : conteneurs légers, utile pour usages avancés.
- **Windows Sandbox** : sur Windows 11 Pro/Enterprise, environnement jetable pour test rapide.

#### 14.6 Pare-feu local

Sortant souvent oublié. Les pare-feux par défaut bloquent l’entrant. Le sortant est par défaut autorisé : une application compromise peut exfiltrer.

- **Linux** : nftables (moderne) ou firewalld (Fedora) avec règles sortantes explicites pour applications sensibles. `OpenSnitch` propose un pare-feu interactif type Little Snitch.
- **macOS** : Little Snitch (commercial, référence) ou LuLu (open source) pour contrôler le sortant par application.
- **Windows** : Windows Defender Firewall permet règles sortantes (peu utilisé en pratique). GlassWire pour vue ergonomique.

#### 14.7 Wayland vs X11

X11, hérité des années 80, n’isole pas les fenêtres entre elles : toute application connectée au serveur X peut lire les frappes clavier de toutes les autres, capturer l’écran, simuler des entrées. C’est un keylogger structurel.

**Wayland**, son remplaçant, isole. La plupart des distributions Linux desktop sont passées à Wayland par défaut (GNOME, KDE, Fedora). Pour usage durci : vérifier que tu es sur Wayland (`echo $XDG_SESSION_TYPE` → `wayland`).

#### 14.8 Audit post-installation : checklist 30 minutes

1. Vérifier chiffrement disque actif.
1. Activer le pare-feu (par défaut Linux/macOS, vérifier Windows).
1. Auditer les comptes utilisateurs (un seul admin nécessaire, sessions sécurisées).
1. Désactiver les services non utilisés (Bluetooth si pas utilisé, Wi-Fi si filaire, partage SMB).
1. Activer les mises à jour automatiques pour le système et les drivers/firmware.
1. Configurer le gestionnaire de mots de passe (Ch 29).
1. Auditer les permissions de microphone, caméra, localisation pour chaque application.

#### 14.9 Mention culturelle : OpenBSD, Fedora Silverblue, NixOS

- **OpenBSD** : focalisé sécurité depuis 30 ans, code audité, ergonomie spartiate. Pour serveurs ou utilisateurs convaincus.
- **Fedora Silverblue** : système immuable, rollback transactionnel. Concept séduisant, ergonomie en progression.
- **NixOS** : configuration entièrement déclarative, reproductibilité totale. Courbe d’apprentissage élevée.

Aucun n’est requis pour un cours générique. Les mentionner permet aux profils techniques d’explorer plus loin.

-----

### Chapitre 15 — Mobile : iOS durci, Android, GrapheneOS

> **Niveau de posture (cf. Ch 2.6)** : iPhone à jour + ADP + permissions auditées + reboot hebdomadaire = **Niveau 1**. iPhone + Lockdown Mode + reboot quotidien + Contact Key Verification, *ou* GrapheneOS sur Pixel dédié avec profils = **Niveau 2**. GrapheneOS avec profils stricts + MVT mensuel + iVerify + reboot biquotidien + sans aucune app Google Play Services privilégiée = **Niveau 3**.

#### 15.1 Le constat brutal

Le smartphone est, pour la plupart des gens, le plus gros risque privacy. Il contient :

- L’historique de localisation continu.
- Les contacts et leurs métadonnées de communication.
- Les photos avec EXIF.
- Les comptes bancaires et messageries.
- La biométrie (empreinte, visage).
- Le microphone et la caméra (potentiellement actifs).

Aucun durcissement ne compense l’usage d’un smartphone non sécurisé pour des activités sensibles. Le choix de la plateforme et de sa configuration est plus important que l’ordinateur.

#### 15.2 Identifiants mobiles

- **IMEI** : identifiant matériel du téléphone, transmis à chaque connexion cellulaire.
- **IMSI** : identifiant de la SIM, transmis au réseau (IMSI catchers le captent).
- **Numéro de téléphone** : visible à chaque appel/SMS.
- **eSIM** : équivalent fonctionnel à SIM physique, gérée logiciellement.
- **Wi-Fi MAC, BT MAC** : adresses uniques, randomisées sur les OS modernes (Ch 22).
- **Advertising ID** (IDFA iOS, AAID Android) : désactivables.

Les identifiants publicitaires mobiles — IDFA sur iOS, AAID sur Android, plus généralement MAID — ne doivent pas être vus comme de simples paramètres marketing. Dans l’écosystème publicitaire, ils peuvent servir de pivots de corrélation entre applications, lieux, horaires et comportements. Dans une logique ADINT, un identifiant publicitaire peut devenir un quasi-identifiant de renseignement : il ne donne pas directement le nom civil de la personne, mais permet souvent de la réidentifier par ses routines, ses lieux de vie, ses lieux de travail et ses déplacements récurrents. 

À côté des identifiants publicitaires fournis par l’OS, il faut également surveiller les initiatives d’identification publicitaire portées par les opérateurs télécoms. Des systèmes comme Utiq illustrent une tendance post-cookie : exploiter des signaux opérateur et des jetons pseudonymes pour permettre du ciblage publicitaire sans s’appuyer uniquement sur les cookies tiers ou les identifiants publicitaires classiques. Pour l’OPSEC, cela confirme qu’un téléphone personnel connecté à son abonnement mobile habituel reste un fort pivot de corrélation.

Pour un téléphone sensible, la règle est simple : moins il contient d’applications financées par la publicité, moins il émet de signaux exploitables. Un téléphone destiné à une manifestation, un rendez-vous source, une mission terrain ou une réunion confidentielle ne devrait pas contenir d’applications grand public à SDK publicitaires.

#### 15.3 Localisation

Cinq sources, agrégées :

- **GPS** : précision 5-10 m.
- **Wi-Fi** : géolocalisation par triangulation des SSID environnants (bases Google, Apple, Skyhook).
- **Bluetooth/BLE** : beacons commerciaux dans les magasins, AirTags.
- **Cellulaire** : antennes-relais, précision 100 m à 1 km en zone dense.
- **Magnétomètre, baromètre** : utilisés pour étage dans bâtiment.

Désactiver le « Service de localisation » d’un cran n’éteint pas les couches passives. Wi-Fi et Bluetooth peuvent renseigner sur ta position même avec GPS coupé.

#### 15.4 iOS comme baseline

**Code long** : 6 chiffres minimum, alphanumérique idéalement. Face ID/Touch ID = confort, mais peuvent être contournés sous coercition.

**Lockdown Mode** (iOS 16+) : désactive des fonctionnalités exploitées par les spyware mercenaires : pièces jointes complexes en Messages, certaines APIs WebKit (JIT JavaScript), profils de configuration, accessoires filaires sur appareil verrouillé, etc. Coût ergonomique modéré, gain de sécurité réel. **À activer** pour les HVT (journalistes, dissidents, lanceurs d’alerte, avocats sensibles).

**Restrictions sur écran verrouillé** : désactiver les notifications, Siri, contrôle USB en lock screen, Wallet, retour d’appel.

**iCloud** : ADP activée (cf. Ch 14).

**Permissions** : audit Réglages → Confidentialité → revue par catégorie (Localisation, Contacts, Photos, Micro, Caméra, Suivi). Le « Tracking » d’apps (ATT) est désactivable globalement.

#### 15.5 Advanced Data Protection iCloud

ADP, depuis fin 2022 (US) et étendu mondialement en 2023, bascule en chiffrement de bout en bout les catégories suivantes :

- iCloud Drive
- Photos
- Sauvegardes iCloud de l’appareil (incluant les sauvegardes WhatsApp si stockées dans iCloud)
- Notes, Rappels
- Signets et historique Safari
- Mémos vocaux
- et plusieurs autres catégories (Apple liste précisément sur https://support.apple.com)

**Important — ce qui reste NON chiffré de bout en bout, même avec ADP activé** : iCloud Mail, Contacts iCloud, et Calendrier iCloud restent accessibles à Apple. Apple le documente explicitement : ces trois services utilisent des standards d’interopérabilité (SMTP/IMAP pour Mail, CalDAV/CardDAV pour Calendrier et Contacts) qui imposent que les serveurs Apple traitent les contenus en clair pour pouvoir communiquer avec les autres fournisseurs et appareils tiers. Si la confidentialité de Mail, Contacts ou Calendrier est critique, il faut soit utiliser un autre fournisseur (Proton Mail, Proton Contacts, Proton Calendar), soit accepter que ces données restent visibles à Apple et exposées en cas de réquisition judiciaire.

**Conditions d’activation** : tous tes appareils Apple doivent être sur une version récente (iOS 16.2+, macOS 13.1+). Une clé de récupération doit être conservée (sinon perte totale des données ADP en cas d’oubli du code d’appareil et impossibilité d’utiliser un appareil de confiance). Apple ne peut plus aider à la récupération une fois ADP activé — c’est l’objet même du dispositif.

#### 15.6 Android stock vs OEM

Android **AOSP** (Android Open Source Project) : propre, mais aucun OEM ne livre AOSP pur.

**Google Pixel + Android stock** : meilleure version d’Android pour mises à jour rapides, sécurité, mais entièrement intégré aux services Google.

**Samsung, Xiaomi, Oppo, Vivo, Huawei…** : surcouches OEM avec collecte propre, télémétrie additionnelle, apps préinstallées. Mises à jour de sécurité variables. Pour les Chinois (Xiaomi, Oppo, Vivo, Honor, Huawei) : préoccupations spécifiques liées à la juridiction d’origine et à des cas documentés de collecte excessive.

#### 15.7 GrapheneOS

**Philosophie** : OS Android dégooglisé, durci, focalisé privacy et sécurité. Développement actif, mise à jour rapide des patches Android upstream.

**Caractéristiques** :

- Hardening kernel et userspace.
- Sandboxed Google Play : les services Google Play installés dans une sandbox utilisateur normale, pas en privilégié système. Tu peux utiliser des apps qui en dépendent sans donner à Google les privilèges habituels.
- **Profils utilisateurs** : isolation forte entre profils. Idéal pour séparer pro/perso/sensible.
- **Storage Scopes** : permission granulaire « cette app peut accéder à *ce dossier* seulement », alternative à « toutes les photos ».
- **Contact Scopes** : équivalent pour les contacts.
- **Network permission** : un toggle pour empêcher une app d’accéder au réseau, indépendamment du fait qu’elle le demande.
- Verified Boot avec clés signées par GrapheneOS, attestable.

**Limites** :

- Pixel uniquement (Pixel 6 et supérieurs sont privilégiés).
- Certaines apps (banking, gouvernementales) refusent de fonctionner sur ROM custom (anti-tampering).
- Pas de Google Wallet (Google Pay) — paiement sans contact via app bancaire dépend des apps.
- Carplay/Android Auto support limité.

**Pour qui** : tous ceux qui veulent un mobile sérieusement durci et peuvent vivre avec les contraintes. Recommandé pour journalistes, activistes, dirigeants exposés, professionnels cyber.

#### 15.8 CalyxOS, LineageOS (et le cas DivestOS)

- **CalyxOS** : alternative à GrapheneOS, philosophie similaire mais MicroG préinstallé (réimplémentation libre des Google Play Services). Moins de hardening que GrapheneOS, mais position éthique intéressante. Maintenu activement.
- **LineageOS** : Android communautaire générique. Pas focalisé sécurité, mais utile pour prolonger la vie d’appareils non supportés par OEM. Important : LineageOS sans signatures Verified Boot du constructeur réduit la sécurité matérielle. À utiliser pour des appareils secondaires non sensibles.
- **DivestOS** : fork LineageOS focalisé sécurité, supportait plus de modèles que GrapheneOS. **Le projet a annoncé son arrêt fin 2024**, le développeur principal ayant cessé la maintenance active. À ne plus utiliser comme recommandation pour un déploiement nouveau ; les utilisateurs existants doivent planifier une migration vers une plateforme maintenue (GrapheneOS si Pixel disponible, CalyxOS sinon, ou retour à un OS constructeur à jour selon profil).

#### 15.9 Choix matériel et support

GrapheneOS exige du **Pixel récent** (Pixel 6+). Pixel 8 et Pixel 8a sont actuellement (2025-2026) de bons points d’entrée : support OEM jusqu’en 2030-2031, Titan M2, performances correctes.

**Durée de mises à jour** : Pixel 8/8a → 7 ans (2030 pour le 8). iPhone → environ 6-7 ans en pratique. Samsung → 7 ans (Galaxy S22+ et plus). Reste du marché : 2-4 ans.

Acheter un téléphone sans support de mises à jour pour 5+ ans est une erreur d’investissement sécuritaire.

#### 15.10 Permissions et hygiène applicative

- **Claviers tiers** : SwiftKey, Gboard avec sync cloud → mauvaise idée pour usage sensible. Pour GrapheneOS : utiliser le clavier intégré, ou AnySoftKeyboard sans cloud.
- **Presse-papiers** : surveillance possible par apps en arrière-plan. iOS 14+ alerte. Android 12+ aussi. Vigilance.
- **Trackers dans applis** : la plupart des applis grand public en intègrent. Outil utile : **Exodus Privacy** (analyse des trackers d’une app).
- **Permissions à scopes** : sur GrapheneOS, Storage Scopes et Contact Scopes ; sur iOS, sélection de photos précises plutôt que photo library complète.

#### 15.11 Séparation pro/perso/sensible

Sur GrapheneOS : profils utilisateurs distincts. Chaque profil a son propre espace, ses apps, ses comptes. Bascule par swipe down.

Sur iOS : pas de profils utilisateurs (limitation iOS persistante). Solution : appareils distincts pour usages sensibles, ou « Focus Modes » avec filtres d’apps.

#### 15.12 Reboot quotidien

Les spyware mercenaires modernes (Pegasus, Predator, Graphite) reposent souvent sur des exploits **non persistants** : un redémarrage les efface. L’attaquant doit alors re-infecter, ce qui multiplie ses traces et son coût.

Le **reboot quotidien** (ou hebdomadaire pour les moins exposés) est l’une des mesures les plus simples et les plus efficaces contre les attaques avancées. Cinq secondes par jour. À adopter systématiquement pour les HVT.

#### 15.13 *Fil rouge* — Léa migre vers Pixel 8a + GrapheneOS

Léa, après son audit, achète un Pixel 8a en magasin (cash, anonymement), flashe GrapheneOS le soir même, et configure :

- **Profil principal** : usage quotidien sans Google, Signal, Proton Mail, navigateur Vanadium.
- **Profil pro** : son compte journalistique, Slack rédaction, outils pros.
- **Profil enquête** : compartiment dédié, SimpleX, Tor Browser sur mobile, aucun compte personnel.

Elle conserve son iPhone perso pour la vie civile (banque, photos famille), avec ADP activée. Reboot quotidien le matin. Six semaines de transition pour s’habituer.

> 🟩 **À retenir de la Partie 3**
> 
> - Hardware = racine de confiance. Tout ce qui suit en dépend.
> - Secure Boot + TPM = colonne vertébrale de la sécurité moderne. À activer, à comprendre, à mettre à jour.
> - FDE est indispensable, mais ne protège pas si l’appareil est saisi AFU.
> - Air gap : pour des secrets rares, pas pour le quotidien.
> - Mobile = plus gros risque privacy. iPhone durci ou GrapheneOS sont aujourd’hui les meilleurs choix.
> - Reboot quotidien : 5 secondes, gain réel.

-----

## Partie 4 — Environnements de session sensible

> **Objectif** : aller au-delà du durcissement quotidien pour les sessions qui exigent une compartimentation forte ou une isolation réseau. Comprendre que Tails, Whonix et Qubes OS répondent à *trois besoins différents*, et choisir lequel s’applique à quel cas.

-----

### Chapitre 16 — Machines virtuelles, live USB et environnements jetables

#### 16.1 Principe : enveloppe jetable autour d’une activité

Les machines virtuelles et les environnements live permettent d’exécuter un système isolé du système hôte. L’activité sensible se déroule dans cette enveloppe, qui est jetée à la fin. C’est l’inverse de la logique « durcir l’OS principal pour tout » : on accepte que l’OS principal n’est pas immunisé, on l’utilise pour ce qui ne risque pas, et on bascule en environnement séparé pour ce qui risque.

#### 16.2 Hyperviseurs courants

- **VirtualBox** (Oracle) : gratuit, multi-plateforme, populaire. Performances modestes. Récents soucis de support sur Apple Silicon.
- **KVM/QEMU** (Linux) : intégré au noyau, performant. virt-manager pour interface graphique.
- **Hyper-V** (Windows Pro/Enterprise) : intégré, bonne intégration.
- **VMware Workstation Pro** (devenu gratuit en 2024 pour usage personnel) : commercial historique, performant.
- **UTM** (macOS, gratuit) : surcouche QEMU, support Apple Silicon, références pour macOS.

#### 16.3 Snapshots et restauration

Le **snapshot** capture un état complet de la VM. Avant chaque session sensible : snapshot. Après : revert au snapshot propre. Cela garantit qu’aucun artefact (cookies, fichiers, malware potentiel) ne survit à la session.

Discipline minimale : un snapshot « propre » initial, un revert systématique en fin de session, jamais d’usage long terme sans rotation.

#### 16.4 Limites de l’isolation par VM

- **Évasion de VM** : sortir d’une VM pour compromettre l’hôte est techniquement possible mais reste rare. Demande typiquement un zero-day sur l’hyperviseur, ressources et motivation. Des CVE existent régulièrement (Xen, KVM, VMware, VirtualBox) — la pratique défensive est de garder l’hyperviseur à jour et de ne pas utiliser une VM seule comme barrière critique pour activité ultra-sensible.
- **Évasion par périphérique partagé** : USB passthrough, audio, presse-papiers, clipboard partagé entre VM et hôte sont des vecteurs de fuite. Sur VirtualBox et VMware, désactiver le partage clipboard et drag-and-drop par défaut. Sur Qubes, ces canaux sont gérés explicitement par qrexec avec validation utilisateur à chaque transfert.
- **Fuites matérielles** : information CPU (CPUID, modèle, microcode), adresse MAC virtuelle qui peut être prévisible, configuration réseau de la VM peuvent renseigner sur l’hôte. Une VM ne te rend pas anonyme — elle isole l’application.
- **Performance** : émulation graphique, accélération limitée. Pas pour gaming sensible ou tâches GPU-intensives. Pour usages standard (bureautique, navigation), KVM/QEMU avec virtio est très performant.
- **Sortie réseau** : la VM utilise par défaut le réseau de l’hôte. Pour anonymat, ajouter Tor (cf. Whonix Ch 17). Pour isolation forte, configurer la VM en NAT (et non bridged) pour éviter l’exposition directe au LAN.
- **Side channels** : Spectre, Meltdown et leurs successeurs ont permis dans certaines conditions à une VM de lire de la mémoire hôte. Patches kernel et microcode CPU restent indispensables. Pour profil Niveau 3 : préférer la compartimentation par appareil physique aux VMs pour les secrets vraiment critiques.

#### 16.5 Cas d’usage typiques

- **Ouverture de document suspect** : reçu d’une source inconnue, lien Telegram non vérifié, PDF d’apparence douteuse → VM jetable, revert immédiat.
- **Navigation à risque** : exploration de site OSINT borderline, test de comportement applicatif → VM avec snapshot.
- **Environnement de développement séparé** : projets clients distincts isolés.

#### 16.6 Dangerzone

**Dangerzone** (Freedom of the Press Foundation) automatise le scénario « j’ai reçu un PDF, je veux le lire sans risquer mon système ». Le PDF est converti dans un conteneur isolé en image puis re-rendu en PDF propre. Tous les éléments actifs (JavaScript, formulaires, liens malveillants) disparaissent. Pratique pour journalistes recevant des documents.

#### 16.7 Live USB

Booter depuis une clé USB un OS qui n’écrit rien sur le disque local. Le système est en RAM et meurt à l’extinction. Tails et Kicksecure proposent des images live. Avantages : trivial à déployer, aucune persistance. Inconvénients : pas de configuration personnalisée sauvegardée (sauf persistance chiffrée Tails), démarrage lent.

#### 16.8 Erreur fréquente

Une VM **ne cache pas ton IP**. Elle ne te rend pas anonyme. Elle isole l’application. Confondre les deux conduit à utiliser une VM pour « être sûr d’être anonyme sur ce site », ce qui ne fonctionne pas. Pour anonymat réseau, il faut Tor (Ch 21) ou Whonix.

-----

### Chapitre 17 — Tails, Whonix et Qubes OS : choisir le bon modèle d’isolation

#### 17.1 Trois outils, trois logiques différentes

Ces trois noms reviennent constamment ensemble dans la littérature privacy. Ils ne sont pas concurrents : ils répondent à des besoins distincts.

|Besoin                                         |Outil approprié                       |
|-----------------------------------------------|--------------------------------------|
|Action ponctuelle sensible, faible trace locale|**Tails**                             |
|Identité pseudonyme durable, anonymat réseau   |**Whonix**                            |
|Séparation durable d’activités multiples       |**Qubes OS**                          |
|Profil HVT, journaliste, ONG sensible          |**Qubes + Whonix**                    |
|Quotidien grand public durci                   |*Aucun des trois — un OS durci suffit*|

#### 17.2 Tails : session temporaire, live USB, amnésie

**Tails** est un système live, basé sur Debian, qui démarre depuis une clé USB. Il ne touche pas au disque local. Tout le trafic réseau est routé via Tor (sauf paramétrage avancé). À l’extinction, la RAM est purgée et il ne reste rien de la session.

**Persistance chiffrée optionnelle** : sur la même clé USB, une partition chiffrée peut stocker certains éléments (bookmarks, clés PGP, configuration Tor, certains fichiers). C’est un opt-in conscient.

**Workflow complet** :

1. Télécharger l’image Tails depuis tails.net.
1. Vérifier la signature GPG.
1. Flasher la clé USB (avec balenaEtcher ou `dd`).
1. Démarrer depuis l’USB sur n’importe quel ordinateur (BIOS/UEFI).
1. Travailler. Tout passe par Tor.
1. Éteindre. Tout disparaît.

**Cas d’usage idéaux** : journaliste en mission ponctuelle reçoit un document d’une source ; lanceur d’alerte transmet des fichiers ; opposant utilise un cybercafé.

**Limites** :

- Tails ne protège pas contre un adversaire local actif (firmware compromis, BIOS implanté, keylogger matériel).
- L’usage répétitif sur la même machine peut laisser des artefacts dans la RAM persistante de certains modèles, et dans les logs du modem cellulaire si connexion 4G/5G.
- Tor a ses propres limites (Ch 21).
- L’usage de Tails depuis chez soi sans précaution réseau (FAI voit du Tor) peut signaler ton activité même si le contenu reste protégé.

**Fil rouge** : Karim B., lanceur d’alerte, utilise Tails depuis un cybercafé pour transmettre à Léa des documents. Une seule session, jamais réutilisée. Le cybercafé est choisi loin de son domicile et de son travail, payé cash.

#### 17.3 Whonix : anonymat Tor persistant via Gateway / Workstation

**Whonix** est conçu pour l’anonymat réseau durable. Architecture en **deux VMs** :

- **Gateway** : seul accès réseau, force tout le trafic via Tor. C’est un point d’isolation.
- **Workstation** : l’environnement de travail, qui ne peut sortir que via la Gateway.

**Effet** : même si la Workstation est compromise par un malware, ce malware ne peut pas révéler l’IP réelle, parce qu’il n’y a pas de chemin réseau direct. Le seul trafic possible passe par la Gateway, donc par Tor.

**Streaming isolation** : Whonix configure des circuits Tor distincts par destination, ce qui réduit la corrélation cross-services.

**Usage** : sur VirtualBox/KVM en VM normale, ou en qubes sur Qubes OS (la combinaison ultime).

**Limites** :

- La Workstation peut être compromise par malware (l’IP reste cachée, mais les autres données peuvent fuiter par d’autres canaux : credentials, contenus).
- L’hôte n’est pas protégé : si l’OS hôte est compromis avant la VM, Whonix n’aide pas.
- Performance Tor : latence et débit limités.

#### 17.4 Qubes OS : compartimentation par VM (vue rapide, détail Ch 18)

**Qubes OS** est un système d’exploitation basé sur Xen, qui compartimente *tout* en VMs séparées. Chaque activité tourne dans son propre qube : un qube pour le travail, un qube pour le perso, un qube pour le banking, un qube pour le suspect.

**Ce n’est pas un outil d’anonymat**. Qubes compartimente, il n’anonymise pas. Combiné à Whonix (un qube Whonix), il offre les deux.

Le détail de Qubes est traité au chapitre 18.

#### 17.5 Qubes + Whonix : la combinaison avancée

Pour les profils les plus exposés : Qubes OS comme système hôte, avec un qube `sys-whonix` (Gateway) et des qubes `anon-whonix` (Workstations) pour les activités nécessitant anonymat réseau. Les autres activités (perso, pro non sensible) restent dans leurs qubes propres, sans Tor (parce que Tor pour tout est *contre-productif* — usage repérable, comptes nominaux exposés).

#### 17.6 Comparaison par ergonomie, coût, complexité

|Critère                   |Tails                                 |Whonix             |Qubes                                 |
|--------------------------|--------------------------------------|-------------------|--------------------------------------|
|**Persistance**           |Amnésie par défaut, persistance opt-in|Persistante        |Persistante                           |
|**Matériel requis**       |Tout PC moderne + USB                 |PC raisonnable + VM|PC avec ≥ 16 GB RAM, virtualisation HW|
|**Courbe d’apprentissage**|Modérée                               |Modérée            |Élevée                                |
|**Coût**                  |Gratuit                               |Gratuit            |Gratuit                               |
|**Ergonomie quotidienne** |Inadaptée                             |Possible           |Friction réelle                       |
|**Anonymat réseau**       |Tor par défaut                        |Tor par défaut     |Aucun (sauf qube Whonix)              |
|**Compartimentation**     |Faible                                |Modérée            |Forte                                 |

#### 17.7 Erreurs fréquentes

- **Utiliser Tails comme OS quotidien** : impossible à tenir. Tails est conçu pour des sessions, pas pour de la durée.
- **Croire que Qubes anonymise** : Qubes compartimente. Si tu utilises Firefox dans un qube non-Tor sur ton compte Facebook, Facebook te voit avec ton IP normale.
- **Croire que Whonix protège l’hôte** : Whonix protège l’identité réseau de la VM Workstation. Si l’hôte est compromis, Whonix ne peut rien.
- **Empiler les trois sans comprendre** : Tails dans une VM, Whonix dans Tails, Qubes en VM sur autre Qubes → architecture inopérante et probablement contre-productive.

#### 17.8 Matrice de décision finale

- **Action one-shot sensible, sans persistance** → Tails.
- **Identité pseudonyme durable, anonymat réseau permanent** → Whonix.
- **Compartimentation forte de plusieurs activités** → Qubes.
- **Profil HVT avec besoin des deux** → Qubes + Whonix.
- **Usage quotidien grand public** → ni l’un ni les autres : un OS durci (Ch 14) + GrapheneOS ou iOS durci + bonnes pratiques.

-----

### Chapitre 18 — Qubes OS en pratique : compartimentation avancée et workflows sensibles

#### 18.1 Architecture

Qubes OS repose sur Xen. **Dom0** est le qube administrateur, isolé, sans réseau direct. Au-dessus, des **templates** (Fedora, Debian, Whonix Gateway, Whonix Workstation) servent de base aux **app qubes**, légers, qui partagent le template mais ont leurs propres `/home`.

Trois qubes système :

- **sys-net** : gère les interfaces réseau physiques. C’est le seul qube avec accès direct aux périphériques réseau.
- **sys-firewall** : entre sys-net et les app qubes, applique des règles de pare-feu.
- **sys-usb** : isole les périphériques USB. Aucun USB ne touche dom0.

#### 18.2 Qubes critiques

- **vault** : qube *offline* (aucune connexion réseau autorisée), stocke gestionnaire de mots de passe, clés GPG, secrets. Communication avec autres qubes via copier-coller contrôlé ou qrexec.
- **work** : usage professionnel.
- **personal** : usage personnel.
- **banking** : un qube par institution si paranoïaque, isolé.
- **anon-whonix** : un qube Workstation Whonix pour navigation anonyme.
- **disposable VMs** (dispVM) : qubes éphémères, créés à la demande, détruits à la fermeture. Idéal pour ouvrir un fichier suspect.

#### 18.3 Workflow « ouvrir un fichier suspect »

Tu reçois un PDF de provenance douteuse. Sur Qubes :

1. Fichier reçu dans `personal`.
1. Clic droit → « Open in DisposableVM ».
1. Un qube jetable Fedora se crée, ouvre le PDF.
1. Si le PDF contient un exploit, seule la dispVM est compromise.
1. Tu ferme la fenêtre → la dispVM est détruite.
1. Ton `personal` est intact.

#### 18.4 Workflow « identités séparées »

Tu sépares pseudo et identité civile. Sur Qubes :

- `personal` : compte Google, Facebook, identité civile, réseau via sys-firewall direct.
- `journalist-pub` : ton compte Twitter de plume publique, ProtonMail dédié, idem.
- `journalist-anon` : qube relié à sys-whonix, pour les comptes vraiment anonymes (Tor pour tout).

Chaque identité a son qube. Tu ne mélanges jamais.

#### 18.5 Qubes + Whonix en production

Configuration :

- **sys-whonix** : Gateway, route le trafic via Tor.
- **anon-whonix** : Workstation, configuré pour utiliser sys-whonix comme réseau. Navigation Tor Browser, comptes pseudonymes.
- Autres qubes (banking, personal) routent via sys-firewall (réseau direct, pas Tor) — parce que tu ne veux *pas* de Tor pour ton banking.

#### 18.6 Modèle de menace contre lequel Qubes est efficace

- Malware classique : confiné à un qube, ne se propage pas.
- Exploit navigateur : confiné au qube qui héberge le navigateur.
- Compromission d’une app spécifique : la dispVM est jetée.
- Erreur humaine : ouvrir un fichier dans le mauvais qube est plus difficile, parce que les qubes sont visuellement codés par couleur.

#### 18.7 Modèle de menace contre lequel Qubes n’est PAS efficace

- Compromission de **dom0** : si dom0 tombe, tout tombe. Donc dom0 doit rester minimaliste, sans réseau, sans installation tierce.
- Exploit de l’hyperviseur Xen : possible mais rare. Mises à jour critiques.
- Attaques matérielles (Spectre, Meltdown, et successeurs) : nécessitent attention et patches.
- Attaque physique avec accès non détecté : Qubes ne change pas la donne.

#### 18.8 Coût et ergonomie

- **Matériel** : 16 GB RAM minimum (32 recommandé), CPU avec virtualisation et IOMMU, GPU compatible, SSD rapide.
- **Apprentissage** : compter 2-4 semaines pour fluidité opérationnelle.
- **Friction quotidienne** : copier-coller inter-qubes intentionnel, gestion réseau par qubes, raccourcis à apprendre.
- **Compatibilité** : pas de Wayland pour l’instant, certaines applis graphiques moins fluides.

#### 18.9 Architectures de référence

- **Journaliste exposé** : dom0 + sys-net + sys-firewall + sys-usb + sys-whonix + personal + work + journalist-pub + anon-whonix + vault + dispVM template.
- **RSSI / cyber pro** : dom0 + sys-* + work + lab + research + analysis + vault.
- **Profil ultra-compartimenté HVT** : multiples qubes Whonix avec rotation, vault offline, disposables pour tout fichier externe, qube banking isolé.

#### 18.10 *Fil rouge* — Yann déploie Qubes pour son équipe terrain

Yann T., RSSI d’une ONG des droits humains à Genève, déploie Qubes sur les laptops de cinq enquêteurs terrain qui travaillent en Asie centrale et au Moyen-Orient. Configuration standardisée : qubes par projet, sys-whonix pour les comptes pseudonymes, vault offline pour les clés PGP, dispVM templates Fedora et Debian. Formation : 2 jours sur place + manuel interne. Six mois plus tard, il constate que la principale source de friction est la gestion des pièces jointes (les enquêteurs envoient beaucoup de PDF). Solution déployée : un workflow dispVM + Dangerzone systématique.

-----

> 🟦 **Capstone 2 — Chaîne complète de session sensible**
> 
> **Scénario** : Tu reçois sur Signal un message d’une nouvelle source. Elle annonce avoir des documents. Elle propose de les envoyer via un lien Onion en clic-bouton. Tu sais qu’elle est exposée et que les documents sont sensibles. Comment procèdes-tu, étape par étape ?
> 
> **Procédure attendue** :
> 
> 1. **Vérifier l’identité de la source** sur Signal (Safety Number, cf. Ch 26) avant tout échange substantiel.
> 1. **Préparer un environnement jetable** : Tails sur USB dédiée à cette enquête, ou un qube disposable sur Qubes si tu travailles sur Qubes au quotidien.
> 1. **Routage Tor** : Tails route tout via Tor par défaut ; pour Qubes, utiliser anon-whonix.
> 1. **Téléchargement** : depuis l’environnement isolé, accéder au lien Onion et récupérer les fichiers.
> 1. **Vérification d’intégrité** : si la source a fourni un hash (SHA-256), le vérifier hors bande (canal Signal ou téléphone). Sinon, accepter le risque.
> 1. **Sas de transition** : passer les fichiers par Dangerzone (Ch 16) pour produire des PDF propres.
> 1. **Archivage chiffré** : chiffrer les fichiers source (avec GPG + clé PGP de stockage, ou conteneur VeraCrypt/Cryptomator) avant de les sortir de l’environnement isolé.
> 1. **Stockage** : sur un disque chiffré séparé, idéalement dans un qube vault si Qubes, ou sur un disque externe chiffré rangé physiquement.
> 1. **Destruction des traces** : si Tails, redémarrage = traces effacées ; si dispVM Qubes, fermeture = destruction.
> 1. **Documentation** : noter dans un journal d’enquête (chiffré) : date, source, hash des fichiers, environnement utilisé. Pour traçabilité interne, pas pour partage.
> 
> Léa, dans le fil rouge, applique cette procédure quand Karim B. lui transmet son premier paquet de documents : Tails sur USB neuve achetée pour cette enquête, ouverture des PDF via Dangerzone, archivage dans un conteneur VeraCrypt sur disque externe rangé dans un coffre.

-----

## Partie 5 — Réseau, anonymat et navigation web

> **Objectif** : comprendre ce qui fuit au niveau réseau et navigateur, et choisir ses outils en fonction du threat model — sans mythologie. Cette partie est traversée par un seul fil conducteur : *qui voit quoi à chaque saut ?*

-----

### Chapitre 19 — Pile réseau : ce que voit chaque acteur

#### 19.1 Anatomie d’une requête web

Tu tapes `https://example.org` dans ton navigateur. Voilà ce qui se passe, et ce qui fuit à chaque étape :

1. **Résolution DNS** : ton OS demande à un résolveur DNS l’adresse IP de `example.org`. Sans DNS chiffré, cette requête est en clair sur le réseau local et le FAI voit le nom de domaine.
1. **Établissement TCP** : connexion à l’IP du serveur. Visible : IP source, IP destination.
1. **Négociation TLS** : ton navigateur envoie un *ClientHello* contenant, entre autres, le **SNI** (Server Name Indication) — c’est-à-dire le nom de domaine que tu joins, *en clair*, même si tu utilises HTTPS. C’est pour permettre à un serveur hébergeant plusieurs sites de savoir lequel servir.
1. **Échange chiffré** : à partir de là, contenu chiffré.

Conséquence : même en HTTPS, ton FAI sait **quel site tu visites** (via DNS et SNI), juste pas *ce que tu fais* sur ce site.

#### 19.2 DNS en clair : mouchard universel

Le DNS classique (port 53, UDP) est en clair. Toute personne sur le chemin (FAI, opérateur Wi-Fi, employeur sur réseau d’entreprise) voit chaque résolution. C’est trivial à intercepter, à enregistrer, à monétiser, à censurer.

#### 19.3 DoH, DoT, DNSCrypt, DNSSEC

Trois protocoles modernes de DNS chiffré :

- **DoH (DNS over HTTPS)** : DNS dans des requêtes HTTPS. Avantage : indiscernable du trafic HTTPS normal, contournement de certains blocages. Inconvénient : nécessite un résolveur DoH configurable, parfois géré par un acteur centralisé (Cloudflare 1.1.1.1, Google 8.8.8.8, Quad9, NextDNS, Mullvad DNS).
- **DoT (DNS over TLS)** : DNS dans une connexion TLS dédiée sur port 853. Détectable comme « DNS chiffré » (donc bloquable spécifiquement) mais propre techniquement.
- **DNSCrypt** : alternative open source plus ancienne, support variable.
- **DNSSEC** : signe cryptographiquement les réponses DNS pour vérifier leur intégrité (pas leur confidentialité). Complémentaire, pas substitut.

**Choix du résolveur** : Cloudflare est rapide et propose des audits, mais centralise massivement. **Quad9** (Suisse) ou **Mullvad DNS** sont des alternatives plus respectueuses. **NextDNS** offre filtrage personnalisable. Self-hosting d’un résolveur DoH (sur ton propre serveur via Pi-hole + Unbound) est l’option maximale pour qui peut.

#### 19.4 SNI et ECH

Même avec DNS chiffré, le **SNI** trahit ta destination. Le **ECH (Encrypted Client Hello)** chiffre le SNI dans le ClientHello TLS, en s’appuyant sur une clé publique du serveur récupérée via DNS (typiquement via un enregistrement HTTPS / SVCB).

**État du déploiement (2025-2026)** :

- Côté client : Firefox supporte ECH depuis la version 118 (active par défaut depuis fin 2023 quand le serveur le supporte). Chrome supporte ECH derrière flag. Safari supporte partiellement. Tor Browser inclut ECH.
- Côté serveur : Cloudflare a activé ECH par défaut pour ses clients en 2023 ; Fastly et certains autres CDN ont suivi. Le déploiement reste partiel pour le web non-CDN.
- Effet réel : ECH ne fonctionne que si *les deux extrémités* le supportent **et** si le résolveur DNS retourne les enregistrements HTTPS contenant la clé ECH. Sans DNS chiffré (DoH/DoT), l’enregistrement HTTPS lui-même peut être altéré par un attaquant sur le chemin, désactivant ECH.

**Bonne pratique** : activer ECH dans le navigateur, utiliser un résolveur DoH qui supporte les enregistrements HTTPS (Cloudflare 1.1.1.1, NextDNS, Mullvad DNS), comprendre que le bénéfice réel dépend des sites visités.

#### 19.5 QUIC et HTTP/3

**QUIC** est un protocole de transport conçu par Google et standardisé par l’IETF (RFC 9000+) en 2021. Il remplace TCP+TLS pour les nouveaux usages : intégration native du chiffrement TLS 1.3, établissement de connexion en 1-RTT (voire 0-RTT), multiplexage sans head-of-line blocking, migration de connexion sans rupture (utile pour mobile en bascule Wi-Fi → 4G).

**HTTP/3** est HTTP au-dessus de QUIC. Adopté par Cloudflare, Google, Facebook, Akamai. Représente une part croissante du trafic web (≈ 30 % du trafic des grands sites en 2025).

**Implications privacy** :

- **Plus difficile à observer en surface** que TCP/TLS classique : QUIC chiffre une partie des en-têtes de transport, pas seulement l’application.
- **Fingerprint** : QUIC introduit un nouveau vecteur de fingerprinting (paramètres de connexion, comportement). JA4 est l’évolution de JA3 qui couvre QUIC.
- **Blocage par DPI** : QUIC en UDP/443 est plus difficile à classifier que TCP/443. Certains États (Russie, Iran) ont périodiquement bloqué UDP/443 dans son ensemble.
- **Pour les VPN** : WireGuard est en UDP par nature ; ECH+QUIC complète le tableau de protocoles modernes.

#### 19.6 Fuites IP : WebRTC, IPv6, captive portals

- **WebRTC** : protocole de communication temps réel (visio, voix) qui peut révéler ton IP réelle même derrière un VPN, parce qu’il négocie des connexions P2P. À désactiver ou contrôler dans le navigateur.
- **IPv6 mal géré** : ton VPN tunnelise peut-être seulement IPv4 ; les requêtes IPv6 contournent le tunnel. À tester. À forcer IPv4-only si le VPN ne gère pas bien IPv6.
- **Captive portals** (Wi-Fi hôtel, café) : le navigateur tente de joindre des URLs de test pour détecter le portail. Ces requêtes révèlent ta présence avant que tu sois authentifié.
- **mDNS** (multicast DNS) : annonce des services locaux. Peut fuiter le nom de ton machine sur le réseau local.

#### 19.7 Ce que voit chacun

|Acteur                 |Voit                                                                    |Ne voit pas                              |
|-----------------------|------------------------------------------------------------------------|-----------------------------------------|
|**FAI** (sans VPN)     |IP, DNS (sauf DoH), SNI (sauf ECH), métadonnées (volumes, timing)       |Contenu HTTPS                            |
|**VPN**                |IP source réelle, IP destination, SNI (sauf ECH), métadonnées           |Contenu HTTPS                            |
|**Site visité**        |IP source (FAI ou VPN), User-Agent, fingerprint, cookies, contenu envoyé|Identité réelle si pas de compte connecté|
|**App mobile**         |Tout ce qu’elle demande comme permission + traffic                      |(selon permissions)                      |
|**Réseau Wi-Fi public**|Mêmes choses que FAI, sur ton trafic clair                              |Contenu HTTPS                            |

> 🟧 **Évolution récente : l’opérateur comme acteur AdTech**
> 
> Les opérateurs télécoms ne sont pas seulement des transporteurs de trafic. Avec des initiatives comme Utiq, certains opérateurs européens cherchent à valoriser leur position dans l’infrastructure réseau pour proposer des identifiants publicitaires post-cookie. Cela ne signifie pas que l’opérateur lit le contenu HTTPS, mais cela rappelle qu’il dispose d’une position privilégiée : relation contractuelle avec l’abonné, attribution d’IP, connaissance du réseau d’accès, signaux mobiles, et capacité à participer à des mécanismes d’identification publicitaire sous consentement.

Cette table cadre toutes les décisions des chapitres suivants.

#### 19.8 Corrélation par horaires, volumes, destinations

Au-delà des contenus, l’analyse statistique des métadonnées révèle énormément :

- Tu te connectes tous les jeudis à 22h à un même service (timing + destination = profil de comportement).
- Tu envoies un gros volume juste après avoir reçu un message (corrélation conversation/envoi).
- Tu ouvres une session de 3 heures sur Wikipedia (intérêt approfondi sur un sujet).

Cette analyse est faite à l’échelle massive par les FAI et les agences. Elle est à la base de la « surveillance par métadonnées » (cf. Ch 1).

#### 19.9 Outils de diagnostic

- **dnsleaktest.com** : vérifie que tes requêtes DNS passent par où tu crois.
- **browserleaks.com** : audit complet (WebRTC, IPv6, fonts, canvas, etc.).
- **ipleak.net** : autre référence.
- **AmIUnique.org** : mesure le caractère unique de ton fingerprint navigateur (cf. Ch 23).
- **dnscheck.tools** (Mullvad) : utile pour valider config.

À tester systématiquement après installation d’un VPN, d’un navigateur, d’une config DNS.

-----

### Chapitre 20 — VPN : utilité réelle, limites, choix

#### 20.1 Ce qu’un VPN fait vraiment

Un VPN établit un tunnel chiffré entre toi et un serveur distant. Tout ton trafic transite par ce tunnel. Du point de vue des sites distants, ton IP est celle du serveur VPN. Du point de vue de ton FAI, il ne voit qu’une connexion chiffrée vers le VPN.

**Effet net** : tu **déplaces** la confiance du FAI au fournisseur VPN. Tu ne supprimes pas la confiance, tu la transfères.

#### 20.2 Ce qu’un VPN ne fait pas

- **Il n’anonymise pas**. Si tu te connectes à ton compte Gmail via VPN, Google sait toujours qui tu es.
- **Il ne chiffre pas tes données chez les services**. Le contenu envoyé à un service distant est en clair pour ce service.
- **Il ne te protège pas contre le fingerprinting** (cf. Ch 23). Le navigateur reste identifiable.
- **Il ne te protège pas contre un malware sur ton appareil**.

#### 20.3 Critères de choix

1. **Juridiction** : siège du fournisseur. Suisse, Suède, Panama sont préférables aux US (Patriot Act), au RU (RIPA), à la France (lois antiterrorisme).
1. **No-logs prouvés** : politique no-logs vérifiée par audit indépendant *et*, idéalement, par contraintes judiciaires passées où le fournisseur n’a rien pu fournir. Mullvad et IVPN ont des historiques solides.
1. **Audits indépendants** : Cure53, Radically Open Security, etc. Récents (annuels).
1. **Paiement** : possibilité de paiement anonyme (cash par courrier pour Mullvad, Monero pour certains).
1. **Killswitch** : interruption du trafic si le tunnel tombe. Indispensable.
1. **Leak protection** : protection contre fuites IPv6, DNS, WebRTC.

#### 20.4 Trois familles à ne pas confondre : VPN privacy, mixnet, VPN anti-censure

Tous les outils présentés comme des « VPN privacy » ne répondent pas au même besoin. Avant de comparer des services comme Mullvad, Proton VPN, NymVPN ou AmneziaVPN, il faut distinguer les grandes familles fonctionnelles.

Un VPN ne doit pas être choisi parce qu’il est dans une liste de « meilleurs VPN », mais parce qu’il correspond au problème opérationnel à résoudre : cacher son trafic à son FAI, réduire son exposition sur Wi-Fi public, éviter le tracking IP, contourner la censure, réduire les métadonnées, ou créer une infrastructure personnelle.

#### 20.4.1 Les VPN privacy classiques

Les VPN privacy classiques sont les VPN au sens le plus courant : ils créent un tunnel chiffré entre l’utilisateur et un serveur VPN. Le FAI ne voit plus les destinations finales ; les sites visités voient l’adresse IP du serveur VPN au lieu de l’adresse IP réelle de l’utilisateur.

Leur intérêt principal est de **déplacer la confiance** du FAI vers un fournisseur VPN considéré comme plus fiable. Ils sont utiles pour :

- réduire l’exposition au FAI ;
- sécuriser une connexion sur Wi-Fi public ;
- masquer son IP réelle aux sites consultés ;
- compartimenter certains usages réseau ;
- limiter certains blocages géographiques ou filtrages simples.

Mais ils ne rendent pas anonyme. Si l’utilisateur se connecte à son compte Google, Apple, Facebook, bancaire ou professionnel, le service sait toujours qui il est. Le VPN protège la couche réseau, pas l’identité applicative.

Dans cette famille, on peut distinguer deux sous-profils :

**VPN privacy minimalistes** : Mullvad, IVPN.  
Ils privilégient la minimisation de données, l’absence de compte nominatif, les audits, la simplicité et la cohérence OPSEC. Mullvad est l’exemple typique : compte numéroté, pas d’email nécessaire, paiement possible en cash ou Monero, politique de logs très restrictive.

**VPN privacy grand public / écosystème** : Proton VPN.  
Proton VPN est solide, suisse, audité, confortable et bien intégré à l’écosystème Proton. Il est très pertinent pour un usage général privacy + confort, mais il est moins minimaliste qu’un service comme Mullvad, notamment parce qu’il s’inscrit dans un écosystème plus large : Proton Mail, Proton Drive, Proton Pass, Proton Calendar.

**Usage recommandé** : privacy quotidienne, Wi-Fi public, navigation classique, réduction de l’exposition au FAI.

**Limite principale** : le VPN voit techniquement une partie de ce que le FAI ne voit plus. Le problème de confiance est déplacé, pas supprimé.

#### 20.4.2 Les réseaux orientés métadonnées et mixnet

Cette famille répond à un problème plus avancé : les métadonnées réseau.

Même lorsqu’un trafic est chiffré, il laisse des traces : horaires de connexion, volumes de données, régularité, durée des sessions, taille des paquets, points d’entrée et de sortie. Un adversaire capable d’observer ces signaux peut parfois corréler deux activités sans lire le contenu.

Les mixnets cherchent à réduire cette corrélation en mélangeant les flux, en ajoutant de la latence, en multipliant les sauts et parfois en ajoutant du bruit réseau. L’objectif n’est pas seulement de cacher l’IP, mais de rendre plus difficile l’analyse du trafic.

**NymVPN** appartient à cette logique. Il propose un mode rapide en deux sauts et un mode anonyme en cinq sauts via le mixnet Nym. Le mode anonyme vise à réduire la corrélation par métadonnées, au prix d’une latence plus importante.

Ce type d’outil est pertinent pour :

- des recherches sensibles ;
- des communications où les métadonnées comptent autant que le contenu ;
- des usages crypto ou financiers où la corrélation réseau est problématique ;
- des profils exposés qui veulent tester une couche supplémentaire contre l’analyse de trafic.

**Usage recommandé** : protection avancée contre la corrélation de métadonnées.

**Limite principale** : plus de complexité, plus de latence, moins de maturité qu’un VPN centralisé classique. Ce n’est pas forcément le meilleur choix pour le quotidien, le streaming ou les téléchargements lourds.

#### 20.4.3 Les VPN anti-censure et protocoles obfusqués

Cette famille répond à un autre problème : non pas « qui voit mon IP ? », mais « est-ce que mon trafic VPN est détecté ou bloqué ? ».

Dans certains pays ou réseaux, les VPN classiques sont détectés par DPI, blocage IP, blocage protocolaire ou active probing. WireGuard et OpenVPN peuvent être bloqués ou fortement ralentis. Dans ce contexte, le besoin prioritaire est de **masquer la signature du VPN** pour le faire ressembler à du trafic web ordinaire ou difficilement classifiable.

**AmneziaVPN** est particulièrement pertinent dans cette famille. Il permet d’utiliser plusieurs protocoles orientés anti-censure, notamment AmneziaWG, XRay Reality, Shadowsocks et OpenVPN over Cloak.

- **AmneziaWG** est une variante de WireGuard conçue pour rendre le trafic plus difficile à identifier par DPI.
- **XRay Reality** vise à mieux résister à la détection et à l’active probing dans les pays à forte censure.
- **Shadowsocks** est un proxy chiffré largement utilisé dans les environnements censurés.
- **OpenVPN over Cloak** ajoute une couche d’obfuscation pour masquer OpenVPN.

Ce type d’outil est pertinent pour :

- pays censurés ;
- réseaux universitaires ou professionnels filtrants ;
- blocage de VPN classiques ;
- contournement de DPI ;
- préparation de voyage en environnement restrictif.

**Usage recommandé** : anti-censure, contournement réseau, résilience en pays restrictif.

**Limite principale** : l’anti-censure n’est pas l’anonymat. Un outil qui contourne le blocage VPN ne garantit pas que l’utilisateur soit anonyme.

#### 20.4.4 Les VPN self-hosted

Le self-host consiste à déployer son propre serveur VPN sur un VPS ou une machine personnelle. L’intérêt est de ne pas dépendre directement d’un fournisseur VPN commercial pour l’infrastructure.

**AmneziaVPN** est aussi pertinent ici, car il facilite la création d’un VPN personnel sur un VPS avec plusieurs protocoles.

Le self-host peut être intéressant pour :

- avoir un serveur personnel stable ;
- contourner certains blocages ;
- maîtriser la configuration ;
- créer un accès privé à ses ressources ;
- fournir un accès VPN à quelques personnes de confiance.

Mais il faut comprendre la limite OPSEC : en self-host, l’adresse IP de sortie est souvent beaucoup plus unique qu’une IP Mullvad, Proton ou IVPN partagée par de nombreux utilisateurs. L’utilisateur ne se fond donc pas dans une grande foule. De plus, la confiance est déplacée vers le fournisseur VPS.

**Usage recommandé** : infrastructure personnelle, contournement, accès privé, usages techniques.

**Limite principale** : moins bon pour se fondre dans la masse ; confiance déplacée vers l’hébergeur VPS.

#### 20.4.5 Les réseaux d’anonymat : Tor, Whonix, Tails

Tor, Whonix et Tails ne doivent pas être classés comme de simples VPN. Ils appartiennent à une autre famille : les réseaux et environnements d’anonymat.

**Tor** route le trafic à travers plusieurs relais et permet l’accès aux services onion.  
**Whonix** force le trafic d’une machine de travail à passer par une passerelle Tor.  
**Tails** fournit un système live amnésique qui route tout via Tor.

Ces outils sont plus adaptés aux usages où l’anonymat réseau est prioritaire : contact source, SecureDrop, OnionShare, publication pseudonyme, session sensible ponctuelle.

**Usage recommandé** : anonymat réseau, services onion, journalisme sensible, lanceurs d’alerte.

**Limite principale** : latence, friction, risque de mauvaise OPSEC. Tor ne protège pas contre une connexion à un compte nominatif, un navigateur mal utilisé ou une erreur comportementale.

#### 20.4.6 Règle finale

Un VPN privacy classique protège surtout contre le FAI, les réseaux locaux et l’exposition IP.  
Un mixnet cherche à réduire l’analyse des métadonnées.  
Un VPN anti-censure cherche à passer à travers des réseaux hostiles.  
Un self-host donne du contrôle, mais réduit souvent l’anonymat par la foule.  
Tor, Whonix et Tails restent les références pour l’anonymat réseau structuré.

Le bon choix n’est donc pas « quel est le meilleur VPN ? », mais : **quel problème réseau est-ce que je cherche à résoudre ?**

#### 20.5 Acteurs principaux (2025-2026)

- **Mullvad** : référence privacy. Suède. VPN privacy classique, centralisé, mais très minimaliste : compte numéroté sans email, paiement possible en cash ou Monero, politique no-log détaillée, orientation forte vers la minimisation de données. C’est un bon choix de base pour réduire la visibilité du FAI, éviter l’exposition de son IP réelle aux sites, sécuriser les réseaux Wi-Fi publics et compartimenter des usages.
- **IVPN** : Gibraltar. Audits Cure53. Très privacy-friendly. Tier business pour multi-appareils.
- **Proton VPN** : Suisse, opéré par Proton. Bonne réputation, intégration avec l’écosystème Proton. Plan gratuit existant.
- **NymVPN** : service plus récent et conceptuellement différent d’un VPN classique. NymVPN propose un mode **Fast** en deux sauts, basé sur une architecture décentralisée et AmneziaWG, et un mode **Anonymous** en cinq sauts via le mixnet Nym avec ajout de bruit. À classer comme outil de réduction des métadonnées et de corrélation, davantage que comme simple VPN de confort. Bon candidat pour profils exposés qui veulent tester une approche plus robuste contre l’analyse de trafic, mais à manier avec prudence : réseau plus jeune, latence plus forte en mode anonymous, et modèle plus complexe qu’un VPN centralisé mature.
- **AmneziaVPN** : outil hybride : client open source multi-protocoles, service Premium, et surtout solution de self-hosting VPN. Surtout pertinent dans les contextes de censure, de filtrage ou de DPI agressif. Il permet soit d’utiliser une offre VPN classique, soit de déployer son propre VPN sur un serveur VPS, avec des protocoles comme AmneziaWG, XRay Reality, Shadowsocks ou OpenVPN over Cloak. Son intérêt principal n’est pas l’anonymat par foule d’utilisateurs, mais la capacité à contourner des blocages et à masquer la signature du trafic VPN. Moins adapté comme « VPN privacy puriste » si utilisé en self-host : l’utilisateur déplace alors la confiance vers son fournisseur VPS, et son IP de sortie peut être beaucoup plus unique qu’une IP partagée par des milliers d’utilisateurs chez un gros fournisseur. À privilégier pour voyage en pays restrictif, filtrage réseau, DPI, ou besoin de serveur VPN personnel.
- **NordVPN, ExpressVPN, Surfshark** : grands acteurs commerciaux. Marketing privacy mais à examiner par juridiction et structure de propriété.
  - **ExpressVPN** a rejoint **Kape Technologies** en 2021 (Kape opérant aussi CyberGhost, Private Internet Access et Zenmate, et historiquement associé à des activités contestées d’adware au début des années 2010, depuis une réorganisation et un changement de direction).
  - **NordVPN** et **Surfshark** ont annoncé en 2022 une fusion opérationnelle au sein du groupe Nord Security, tout en restant commercialisés comme deux marques distinctes avec des audits séparés.
  - Ces fournisseurs restent acceptables pour des cas d’usage simples (contournement géographique, protection sur Wi-Fi public). Pour les profils sensibles ou HVT, les acteurs spécifiquement focalisés privacy (Mullvad, IVPN, Proton VPN) sont préférables en raison de juridiction, ancienneté de l’engagement privacy et historique d’audits ciblés.
- **VPN gratuits** : presque toujours pires que rien. Modèles économiques typiquement basés sur la revente de données ou l’insertion d’ads.

#### 20.6 Protocoles : WireGuard vs OpenVPN

- **WireGuard** : moderne, rapide, code compact (< 4000 lignes), cryptographie up-to-date. Adopté en standard par la plupart des fournisseurs. Limite historique : IPs statiques par client (donc moins anonyme structurellement) — résolu par les fournisseurs sérieux qui rotationnent.
- **OpenVPN** : éprouvé, lent comparativement, complexe à auditer. Reste utile pour contourner certaines détections (TCP 443 indistinguable de HTTPS).
- **Shadowsocks, V2Ray, autres protocoles obfusqués** : pour contourner DPI agressifs (Chine, Iran). À combiner avec VPN ou Tor.
- **AmneziaWG** : fork de WireGuard conçu pour rendre le trafic VPN plus difficile à détecter par des systèmes de DPI. AmneziaWG ajoute des mécanismes d’obfuscation autour de la négociation et du profil réseau, afin que le trafic ressemble moins à du WireGuard standard. Ce n’est pas une garantie d’invisibilité, mais c’est une réponse pratique au blocage de WireGuard dans certains environnements censurés.
- **XRay Reality / VLESS Reality** : famille de protocoles utilisée dans les contextes de contournement de censure. Le principe est de rendre le trafic plus proche d’un trafic TLS web classique, avec résistance à l’active probing. C’est utile dans les pays où les censeurs testent activement les serveurs suspects pour déterminer s’ils hébergent un proxy ou un VPN.
- **OpenVPN over Cloak** : combinaison d’OpenVPN et d’un plugin d’obfuscation. Cloak masque le trafic VPN comme du trafic web et peut présenter une fausse façade en cas de probing non autorisé. Plus lourd qu’un WireGuard classique, mais pertinent dans des environnements où la simple utilisation d’un VPN est détectée ou bloquée.

#### 20.7 Configuration

- **Killswitch activé** systématiquement.
- **Leak protection** : DNS, IPv6, WebRTC.
- **Multihop** (chaînage de deux serveurs) si threat model l’exige : Mullvad et IVPN proposent. Coût en latence et débit.
- **Split tunneling** : certaines apps hors VPN, d’autres dans. Utile pour banque qui bloque les IPs VPN.

#### 20.8 Erreurs fréquentes

- **VPN + comptes nominaux** : ton VPN cache ton IP, mais ton compte Facebook révèle qui tu es. Pour des actions sensibles, séparer.
- **VPN « gratuits »** : risque très supérieur au bénéfice.
- **Compter sur le VPN seul pour la confidentialité** : sans navigateur durci, sans hygiène applicative, le VPN est un placebo coûteux.
- **VPN d’entreprise pour activité personnelle sensible** : ton employeur voit tout ce que voyait ton FAI avant. Pire.

#### 20.9 Matrice de décision rapide

| Besoin principal                      | Famille pertinente                      | Exemples                                    |
| ------------------------------------- | --------------------------------------- | ------------------------------------------- |
| Réduire l’exposition au FAI           | VPN privacy classique                   | Mullvad, IVPN, Proton VPN                   |
| Privacy quotidienne minimaliste       | VPN privacy minimaliste                 | Mullvad, IVPN                               |
| Privacy + confort + écosystème        | VPN privacy grand public                | Proton VPN                                  |
| Réduction des métadonnées réseau      | Mixnet / réseau orienté métadonnées     | NymVPN                                      |
| Pays censuré / DPI agressif           | VPN anti-censure / obfuscation          | AmneziaVPN, AmneziaWG, XRay Reality         |
| VPN personnel sur VPS                 | VPN self-hosted                         | AmneziaVPN self-hosted                      |
| Session source / journalisme sensible | Réseau d’anonymat / environnement isolé | Tor, Tails, Whonix                          |
| HVT durable                           | Compartimentation + anonymat            | Qubes + Whonix, Tor, outils complémentaires |

-----

### Chapitre 21 — Tor : architecture, bridges, services onion, OPSEC

> **Niveau de posture (cf. Ch 2.6)** : Tor n’est *pas* requis au Niveau 1 (la majorité des lecteurs n’en ont pas besoin pour leur posture quotidienne). Au Niveau 2, Tor Browser est utilisé ponctuellement pour navigation anonyme (recherches sensibles, accès à services onion légitimes, premières prises de contact source). Au Niveau 3, Tor devient routage par défaut pour certaines identités via Whonix, avec bridges et transports obfusqués si l’environnement le requiert. Tor n’est pas toujours protecteur — l’utiliser depuis un environnement qui t’identifie localement peut être contre-productif (cf. cas Eldo Kim, Annexe 8.2).

#### 21.1 Architecture Tor en bref

Tor (The Onion Router) route ton trafic à travers **trois relais successifs** :

1. **Guard** : connaît ton IP réelle mais pas la destination.
1. **Middle** : ne connaît ni l’origine ni la destination.
1. **Exit** : connaît la destination mais pas l’origine.

Chaque couche est chiffrée de manière à ce qu’aucun relais individuel n’ait l’image complète. C’est l’essence du *onion routing*.

#### 21.2 Limites du modèle

- **Corrélation de trafic** : un adversaire qui observe à la fois l’entrée *et* la sortie peut, par analyse statistique de volumes et timings, corréler les deux. Les services de renseignement majeurs (NSA et leurs équivalents) ont cette capacité partielle. C’est la principale limite de Tor pour les profils HVT.
- **Exit malveillant** : un nœud de sortie peut espionner le trafic non chiffré qui passe par lui. D’où : **toujours HTTPS** sur Tor.
- **Performances** : latence élevée, débit limité. Tor n’est pas pour le streaming.

#### 21.3 Bridges et transports obfusqués

Dans les pays qui bloquent Tor (Chine, Iran, Russie, etc.), les IPs publiques des relais Tor sont bannies. Les **bridges** (relais non publiés) permettent un point d’entrée alternatif. Les **transports obfusqués** déguisent le trafic Tor en autre chose :

- **obfs4** : trafic indistinguable de trafic aléatoire. Le plus déployé.
- **meek** : trafic camouflé en HTTPS vers un CDN (Azure, Google, Amazon). Lourd mais très résistant.
- **Snowflake** : utilise des proxys volontaires via WebRTC. Rotatif, résistant à la censure récente.

Pour obtenir des bridges : `bridges.torproject.org`, ou via email (`bridges@torproject.org`), ou via Telegram bot (`@GetBridgesBot`).

#### 21.4 Services onion v3

Les **services onion** (anciennement « hidden services ») permettent à un serveur d’être accessible *uniquement* via Tor, sous une adresse `.onion`. L’adresse onion est dérivée de la clé publique du serveur. Avantages :

- **Anonymat du serveur**, pas seulement du client.
- **Authentification cryptographique** intégrée : pas besoin de TLS pour vérifier qu’on parle au bon serveur (l’adresse onion *est* la clé).
- **Pas de sortie sur le réseau public** : le trafic ne passe pas par un exit node.

Usages : SecureDrop (Ch 28), partage de fichiers OnionShare, sites publiquement militants en environnement hostile (Facebook, NY Times et BBC ont des miroirs onion), Tor Browser lui-même.

#### 21.5 OPSEC Tor

Tor *peut* être cassé par mauvais usage applicatif :

- **Ne pas mélanger** : tu ne te connectes pas à ton compte Gmail nominal via Tor. Ça ne sert à rien et ça t’identifie.
- **Tor Browser uniquement** : ne pas utiliser Tor avec Firefox normal, qui n’a pas le hardening fingerprint nécessaire (cf. Ch 24).
- **Pas de plugins** : Flash (historique), JavaScript non contrôlé, PDF viewers vulnérables = casse Tor.
- **Time zone** : Tor Browser force UTC ; si tu modifies, tu te révèles.
- **Identité dans le contenu** : tu peux être anonyme techniquement mais écrire « moi journaliste à Bruxelles 35 ans », ce qui annule l’effort.

#### 21.6 Tor seul, VPN+Tor, Tor+VPN

Configurations possibles et leurs implications :

- **Tor seul** : configuration standard, recommandée pour la plupart.
- **VPN avant Tor (VPN→Tor)** : le VPN voit que tu utilises Tor ; le guard Tor ne voit pas ton IP réelle. Utile si tu veux cacher *à ton FAI* l’utilisation de Tor. Coût : tu fais confiance au VPN.
- **Tor avant VPN (Tor→VPN)** : presque toujours **mauvaise idée**. Casse le modèle Tor, identifie tes sessions au VPN.

**Recommandation** : Tor seul, ou Tor avec bridges si environnement bloquant.

#### 21.7 Tests de fuite

- **check.torproject.org** : valide que tu es bien sur Tor.
- **dnsleaktest** depuis Tor Browser : valide que DNS passe par Tor.
- **AmIUnique** : pour vérifier le fingerprint.

#### 21.8 Cas d’utilisateurs démasqués

- **Eldo Kim**, étudiant Harvard 2013 : envoie une fausse alerte à la bombe via Tor + Guerrilla Mail. Identifié parce qu’il était le seul étudiant connecté à Tor depuis le réseau Harvard à ce moment-là. Corrélation triviale. Cf. Annexe 8.
- **Ross Ulbricht** : son arrestation ne tient *pas* à un cassage de Tor, mais à une erreur OPSEC (pseudo réutilisé entre forum technique et identité civile, gmail nominatif). Cf. Annexe 8.

Leçon constante : **Tor tient techniquement, l’OPSEC casse**.

#### 21.9 *Fil rouge* — Anya publie via Tor

Anya V., opposante russe en exil à Berlin, publie ses analyses politiques sur un blog. Stack : Tor Browser sur un laptop dédié, hébergement chez un fournisseur acceptant Tor, paiement en cryptomonnaies achetées en Allemagne. Pseudonymat stable mais isolation stricte de son identité civile berlinoise. Elle utilise le même mail Proton via Tor exclusivement, depuis le même appareil, depuis sa zone géographique habituelle (cohérence). Elle évite les heures de connexion suspectes (régularité = identifiable).

-----

### Chapitre 22 — Wi-Fi, Bluetooth, cellulaire, MAC, IMSI

#### 22.1 Le téléphone éteint qui n’est pas éteint

Le modem baseband d’un smartphone fonctionne souvent même en mode avion (selon implémentation OEM et version OS). Sur certains téléphones, retirer la batterie était la seule garantie d’isolement radio — mais les batteries modernes sont rarement amovibles. La seule garantie d’isolement physique aujourd’hui : **faraday bag** (sac de Faraday qui bloque les ondes).

#### 22.2 IMSI catchers et générations cellulaires

Un **IMSI catcher** (Stingray, DRT box, Hailstorm) simule une antenne-relais légitime. Le téléphone du sujet, par fonctionnement normal du protocole cellulaire, se connecte à l’antenne offrant le meilleur signal sans authentifier en retour cette antenne — c’est l’asymétrie d’authentification historique du GSM. L’IMSI catcher capture les IMSI (identifiants SIM) des téléphones présents, peut downgrader la connexion vers du 2G (où le chiffrement est faible ou absent), et selon les variantes, intercepter ou injecter des SMS/appels.

**Génération par génération** :

- **2G (GSM)** : authentification du téléphone par le réseau, *pas* d’authentification du réseau par le téléphone. IMSI catcher trivial. Chiffrement A5/1 et A5/2 cassables.
- **3G (UMTS)** : authentification mutuelle introduite. IMSI catchers doivent forcer un downgrade vers 2G ou exploiter des failles. Beaucoup d’opérateurs en 2025 ont éteint la 2G ; le downgrade devient plus difficile.
- **4G (LTE)** : authentification mutuelle. IMSI catchers 4G existent mais plus complexes (capture du TMSI plutôt que de l’IMSI dans certaines configurations).
- **5G NSA (Non Standalone)** : architecture mixte qui réutilise le cœur 4G ; pas de réelle protection IMSI supplémentaire en pratique.
- **5G SA (Standalone)** : chiffre l’IMSI (devenu SUPI) à l’aide d’une clé publique du réseau (SUCI). Réellement protecteur si l’opérateur déploie en mode SA, ce qui reste partiel en Europe (déploiement progressif 2024-2026, plus avancé en Asie).

**Usages documentés des IMSI catchers** : forces de l’ordre (US, Allemagne, France pour terrorisme et certaines enquêtes graves, Suisse, etc.), services de renseignement, criminalité organisée (cas documentés, notamment au Mexique). Déploiement sur manifestations rapporté en plusieurs pays. ACLU et La Quadrature du Net ont documenté l’usage en juridictions diverses.

**Détection** : applications comme AIMSICD (Android), SnoopSnitch (Android, nécessite un modem Qualcomm spécifique et un téléphone rooté) tentent de détecter par anomalies du réseau cellulaire. Fiabilité limitée et taux de faux positifs élevé. Sur iOS, pas d’option utilisateur (l’accès au baseband est verrouillé).

**Défenses** :

- Vérifier si l’opérateur propose 5G SA et basculer si possible.
- Éteindre complètement la radio en zone à risque (faraday bag, *vrai* mode avion vérifié).
- Pour profils Niveau 3 : usage d’un téléphone sans SIM (Wi-Fi only via routeur de voyage VPN), ou téléphone burner avec eSIM jetable.

#### 22.3 MAC randomization

L’adresse MAC d’une interface réseau (Wi-Fi, Bluetooth) est en théorie unique et permanente. Les OS modernes la **randomisent** par défaut pour réduire le tracking :

- **iOS** : MAC aléatoire par SSID depuis iOS 14.
- **Android 10+** : MAC aléatoire par SSID.
- **Windows 10+** : option à activer manuellement.
- **macOS** : randomisation depuis Big Sur.
- **Linux** : via NetworkManager (option `wifi.cloned-mac-address=random`) ou `macchanger`.

**Limite** : MAC aléatoire *par SSID*, pas à chaque connexion. Donc deux connexions au même réseau gardent la même MAC randomisée → corrélation locale possible.

#### 22.4 Wi-Fi probing

Quand le Wi-Fi est activé, ton téléphone émet en continu des **probe requests** pour rechercher les réseaux qu’il connaît : « Hé, le réseau ‹MaisonJean› est-il là ? Et ‹BureauX› ? Et ‹AirportDubai› ? ». Cette liste de SSID *que tu connais* est en clair dans l’air. Elle révèle ton historique de lieux.

**Mitigation** : iOS et Android modernes randomisent et limitent ces probes. Mais l’historique reste parfois exploitable par appareils de surveillance Wi-Fi. **Action** : sur appareils sensibles, désactiver Wi-Fi quand non utilisé, et supprimer périodiquement les SSID enregistrés.

#### 22.5 Bluetooth et BLE beacons

Le Bluetooth Low Energy (BLE) permet aux magasins, aéroports, transports de te tracker passivement via beacons. AirTags d’Apple et équivalents (Tile, Samsung) permettent aussi le tracking. Apple et Google ont introduit des protections (alertes en cas de tracker inconnu qui te suit), mais elles ne sont pas parfaites.

**Cas d’usage offensif** : un harceleur peut glisser un AirTag dans tes affaires. iOS et Android alertent (depuis 2024-2025), mais le délai peut être de plusieurs heures.

#### 22.6 Hotspots Wi-Fi publics

Vraies vs fausses menaces 2025 :

- **Faux Wi-Fi (« evil twin »)** : reste un risque. Atténué par HTTPS partout.
- **Sniffing** : la quasi-totalité du trafic est en HTTPS aujourd’hui. Le risque a baissé.
- **Captive portal** : peut injecter des cookies ou rediriger.
- **Réinjection MITM sur applications mal configurées** : applications mobiles avec certificat pinning défaillant.

Le Wi-Fi public est moins dangereux qu’il y a 10 ans. Un VPN reste utile pour cacher le trafic à l’opérateur du Wi-Fi, et pour éviter les captive portals intrusifs.

#### 22.7 Routeur domestique et box opérateur

La box opérateur est une boîte noire dont le firmware est contrôlé par l’opérateur. Pour profil sérieusement durci : remplacer par un routeur sous OpenWrt ou pfSense en pont, et reléguer la box à un rôle minimal de modem.

Configuration minimale du routeur :

- Wi-Fi WPA3 si supporté, WPA2-AES sinon.
- SSID non identifiable (pas ton nom).
- Réseau invité séparé pour visiteurs.
- DNS chiffré au niveau routeur (DNS via DoH/DoT vers résolveur de confiance).
- Pas d’UPnP (ouverture automatique de ports) sauf si vraiment nécessaire.
- Firmware à jour.

#### 22.8 Routeur de voyage

Pour voyage à risque, un **routeur de voyage** (GL.iNet, Mango, Slate) peut faire un VPN au niveau routeur, fournir un Wi-Fi local à tes appareils, et router tout via VPN ou Tor (avec firmware OpenWrt). Tu te connectes à *un seul* routeur, tes appareils restent simples.

#### 22.9 Segmentation réseau domestique

Quatre VLANs typiques :

- **Pro** : appareils de travail.
- **Perso** : appareils personnels.
- **IoT** : tout l’IoT (TV connectée, thermostat, etc.) isolé.
- **Invités** : pour visiteurs.

Aucune communication entre VLANs sauf règles explicites. La TV connectée compromise ne peut pas joindre ton laptop.

#### 22.10 Modes avion, faraday bag, isolation

- **Mode avion logiciel** : suffit pour 99 % des usages, mais peut laisser des fonctions actives sur certains OS.
- **Faraday bag** : garantie physique. Pour manifestation, frontière, contexte à haut risque.
- **Retrait de batterie** : ancienne mesure ultime. Plus possible sur la plupart des téléphones modernes.

#### 22.11 *Fil rouge* — Sophie en manifestation

Sophie R., activiste, prépare une manifestation à risque d’arrestation. Configuration :

- Téléphone secondaire (vieux Pixel avec GrapheneOS, profil dédié manifestation), aucune donnée personnelle, contacts limités à 3 numéros essentiels.
- Téléphone principal **laissé à la maison**, vraiment éteint (longueur d’extinction complète vérifiée).
- Dans son sac, le téléphone secondaire en faraday bag, sorti seulement si nécessaire.
- Une carte SIM prépayée non liée à son identité (jurisprudence locale à vérifier : en France et Belgique, achat anonyme de SIM prépayée n’est plus possible depuis 2017-2021).
- Numéros importants notés sur papier (avocat, contact d’urgence, hotline juridique).

-----

### Chapitre 23 — AdTech, tracking web,  fingerprinting et ADINT : mécanismes profonds

> **Niveau de posture (cf. Ch 2.6)** : ce chapitre concerne **tous les niveaux**. L’AdTech est l’adversaire avec lequel chaque lecteur a une interaction quotidienne, indépendamment de son threat model. Au N1, désactiver les MAID + uBlock Origin + DNS chiffré apporte un bénéfice immédiat. Au N2, ajout de la compartimentation des comptes et de Mullvad Browser. Au N3, ce chapitre devient essentiel par sa convergence avec l’ADINT (achats gouvernementaux de données publicitaires).

#### 23.1 Pourquoi l’AdTech mérite son propre chapitre

L’industrie publicitaire numérique — l’**AdTech** — est, statistiquement, l’adversaire le plus actif de tout lecteur. Pas le plus dangereux dans une attaque ponctuelle, mais le plus _constant_ : à chaque page web chargée, à chaque application ouverte, à chaque session de streaming, des dizaines d’acteurs commerciaux observent, profilent, enchérissent sur ton attention en quelques dizaines de millisecondes.

Trois propriétés en font un sujet OPSEC à part entière :

- **Légalité majoritaire / Cadre commercial** : les données circulent souvent dans un cadre publicitaire présenté comme licite, sans intrusion technique directe. On ne te hacke pas, on t’achète. La formule est volontairement brutale : elle signifie que la menace vient souvent de l’achat légal ou semi-légal de données déjà collectées par l’écosystème publicitaire, plutôt que d’un piratage. Cette différence avec un malware est précisément ce qui rend la menace moins visible et plus durable.
- **Universalité** : à la différence d’un spyware mercenaire (qui cible des dizaines à quelques milliers de personnes par an), l’AdTech voit _des milliards_ d’utilisateurs en continu.
- **Convergence renseignement** : depuis 2020 environ, le pont entre données publicitaires et achats par agences gouvernementales est massivement documenté. C’est l’**ADINT** (Advertising Intelligence), traitée en 23.5.

Ce chapitre traite donc trois plans qui se complètent : l’**écosystème industriel** (acteurs, flux, identifiants) ; les **mécaniques techniques** (RTB, fingerprinting, tracking comportemental) ; et les **ponts vers le renseignement étatique**.

#### 23.2 Architecture de l’écosystème AdTech

Le vocabulaire est barbare. Sans le maîtriser, on ne comprend pas où circulent les données.

**Acteurs centraux** :

- **Publisher** : l’éditeur du site ou de l’application qui vend de l’espace publicitaire (un média en ligne, un blog, une application gratuite, un service de streaming).
- **Annonceur** : l’organisation qui veut diffuser une publicité (constructeur automobile, grande distribution, éditeur de jeu mobile). Il paie pour atteindre une audience.
- **SSP (Supply-Side Platform)** : est la plateforme utilisée côté éditeur pour vendre automatiquement ses espaces publicitaires, qui gère l’inventaire publicitaire du publisher. Elle met aux enchères les emplacements disponibles. Acteurs principaux : Google Ad Manager, Magnite (ex-Rubicon Project), Index Exchange, OpenX, PubMatic, Xandr (Microsoft).
- **DSP (Demand-Side Platform)**  est la plateforme utilisée côté annonceur pour acheter automatiquement des emplacements publicitaires pour le compte des annonceurs. Acteurs : The Trade Desk, Google DV360, Amazon DSP, Yahoo, Adform, Criteo.
- **Ad Exchange** :  la place de marché automatisée où se rencontrent l’offre publicitaire des éditeurs et la demande des annonceurs. Google AdX, AppNexus (devenu Xandr), exchanges open-RTB-compatibles.
- **Les DMP/CDP** (_Data Management Platform_ / _Customer Data Platform_) servent à centraliser, segmenter et activer des données utilisateur pour mieux cibler les campagnes.
- **DMP (Data Management Platform)** : enrichit les profils avec des données tierces. Oracle BlueKai (retrait annoncé fin 2024), Adobe Audience Manager, Lotame.
- **CDP (Customer Data Platform)** : centralise les données _first-party_ d’un annonceur ou publisher. Segment (Twilio), Tealium, mParticle.
- **CMP (Consent Management Platform)** : sont les bandeaux et interfaces qui gèrent le consentement RGPD et qui demandent à l’utilisateur d’accepter ou refuser certains traitements publicitaires. Elles sont censées formaliser le consentement, mais elles peuvent aussi devenir un point de passage supplémentaire dans la chaîne du tracking. OneTrust, Didomi, Sourcepoint, Quantcast Choice.
- **Ad Server** : est le système qui décide quelle publicité afficher, à quel moment, à quel emplacement, et qui mesure l’affichage ou le clic. Google Campaign Manager, Adform, Equativ.
- **Verification / Brand Safety** : vérifie que la publicité a bien été affichée à un humain, dans un contexte adapté. IAS (Integral Ad Science), DoubleVerify, Moat (Oracle).
- **Data brokers** :  et fournisseurs de données enrichissent les profils avec des informations issues de sources multiples : navigation, achats, localisation, données déclaratives, programmes de fidélité, applications mobiles, fuites de données, registres publics. Agrégateurs tiers (LiveRamp, Acxiom, Experian, Equifax). Cf. Ch 6 — voisinage proche, recouvrement partiel.
- **Les SDK publicitaires** sont des composants intégrés dans les applications mobiles. Une application gratuite peut contenir plusieurs SDK tiers, chacun capable de collecter des signaux techniques, publicitaires ou comportementaux.

L’utilisateur final ne voit presque rien de cette chaîne. Il voit une publicité. En arrière-plan, plusieurs dizaines d’acteurs peuvent avoir participé à la décision d’affichage, à la mesure ou à l’enrichissement du profil.

**Header bidding vs waterfall** :

- _Waterfall_ : la SSP appelle les DSP les unes après les autres jusqu’à trouver un acheteur. Lent, moins rentable pour le publisher.
- _Header bidding_ : appel parallèle à plusieurs DSP simultanément. Plus rentable pour le publisher, mais structurellement plus de fuites de données — chaque DSP non-gagnante a quand même vu tes données et les conserve dans ses logs.

Le passage massif au header bidding dans les années 2017-2020 a _augmenté_ la dispersion du bidstream data. Ce qu’on appelait alors un « gain pour les éditeurs » est aussi mécaniquement un gain d’exposition pour les utilisateurs.

##### 23.3 RTB et bidstream data : enchères publicitaires en temps réel

Le mécanisme central de l’AdTech moderne est le **RTB** (_Real-Time Bidding_), c’est-à-dire les enchères publicitaires en temps réel.

Lorsqu’un utilisateur ouvre une page web ou une application financée par la publicité, un espace publicitaire devient disponible. En quelques millisecondes, une enchère automatisée peut être déclenchée. Des informations sur l’utilisateur, le contexte et l’appareil sont transmises à différents acteurs publicitaires, qui décident s’ils veulent enchérir pour afficher une publicité.

Dans une logique marketing, ces données servent à cibler un segment : âge estimé, zone géographique, type d’appareil, langue, centres d’intérêt supposés ou contexte de navigation. Dans une logique ADINT, ces mêmes signaux peuvent devenir une source de renseignement. L’objectif n’est plus nécessairement de vendre un produit, mais de repérer un appareil, confirmer une présence, suivre une routine ou enrichir un profil.

Les signaux transmis peuvent inclure :

- l’adresse IP ou une localisation approximative ;
- le type d’appareil ;
- le système d’exploitation ;
- le navigateur ou l’application utilisée ;
- la langue et le fuseau horaire ;
- le contexte de la page ou de l’application ;
- un identifiant publicitaire mobile ;
- un cookie ou identifiant pseudonyme ;
- des segments d’intérêt supposés ;
- des informations de localisation plus ou moins précises selon le contexte ;
- des signaux issus de partenaires, courtiers ou plateformes tierces.

Ces informations sont souvent appelées **bidstream data**. Leur fonction officielle est publicitaire : permettre aux annonceurs de décider s’ils souhaitent acheter l’emplacement. Leur sensibilité vient du fait qu’elles peuvent révéler, directement ou indirectement, où se trouve un appareil, quelles applications il utilise, à quels moments il est actif et dans quels contextes il apparaît.

##### 23.4 Pourquoi l’AdTech est un problème privacy

L’AdTech pose un problème privacy parce qu’elle repose sur une logique d’identification probabiliste et de corrélation continue.

L’utilisateur n’a pas besoin de donner son nom pour être suivi. Il suffit parfois qu’un identifiant stable, un fingerprint, une adresse IP, un identifiant publicitaire mobile ou un jeton opérateur soit réobservé dans différents contextes.

Un signal isolé peut sembler anodin. Mais une répétition de signaux permet de reconstruire des habitudes :

- lieux de vie ;
- lieux de travail ;
- horaires d’activité ;
- centres d’intérêt ;
- applications utilisées ;
- sites consultés ;
- sensibilité politique ou religieuse supposée ;
- situation familiale ;
- niveau socio-économique ;
- état de santé probable ;
- déplacements réguliers.

L’AdTech ne produit donc pas seulement de la publicité ciblée. Elle produit des profils.
#### 23.5 Cycle de vie d’une impression et bidstream data

Voici ce qui se passe à chaque chargement de page financée par la publicité :

1. **T+0 ms** : tu charges une page (par exemple un article de presse).
2. **T+5–20 ms** : le JavaScript adtech démarre. Il lit les cookies first-party, le contexte de la page, identifie le navigateur, peut commencer le fingerprinting (cf. 23.10).
3. **T+20 ms** : envoi d’une _bid request_ au SSP. Cette requête contient typiquement :
    - IP source (et donc géolocalisation approximative à la ville voire au quartier) ;
    - User-Agent, taille d’écran, langue, fuseau horaire ;
    - Cookie ID (ou un identifiant de remplacement, cf. 23.4) ;
    - URL de la page, mots-clés contextuels, position de l’emplacement publicitaire ;
    - sur mobile : MAID (IDFA/AAID), modèle d’appareil, app ID.
4. **T+30–80 ms** : la SSP propage la bid request à 10 à 30 DSP en parallèle (header bidding). Chaque DSP peut interroger sa DMP pour enrichir le profil.
5. **T+80–120 ms** : les DSP retournent leurs enchères. La SSP désigne le gagnant.
6. **T+120–200 ms** : la créative est servie, le pixel d’impression est chargé, l’impression est validée.

**Conséquence opérationnelle** : à _chaque_ page chargée, **30+ acteurs voient tes données** — pas seulement le DSP qui gagne l’enchère. Les _losers_ gardent les données dans leurs logs pour segmentation, modélisation, identity resolution, revente. C’est le **bidstream data leak structurel**. En pratique, l’industrie l’opère sous couvert de consentement utilisateur via des CMP, mais sa conformité réelle dépend de la validité du consentement, des finalités déclarées, de la durée de conservation et des responsabilités de chaque acteur. C’est précisément l’un des points les plus contestés de l’AdTech européenne.

Sur 24 heures, un utilisateur actif peut déclencher des centaines, voire davantage, de bid requests selon ses usages web, mobiles et CTV, et expose ses signaux à plusieurs centaines de serveurs adtech distincts. Multiplié par la durée d’une vie numérique active, le volume cumulé est astronomique.

Ce flux de bid requests produit ce qu’on appelle les **bidstream data** : des données techniques, contextuelles et comportementales générées à chaque enchère publicitaire. Leur finalité officielle est marketing, mais leur valeur réelle dépasse largement la publicité : elles deviennent une matière première pour la corrélation, le profilage et, dans certains cas, l’ADINT.

#### 23.6 First-party, third-party et illusion du consentement

Une donnée **first-party** est collectée directement par le service que l’utilisateur utilise : par exemple, un média qui observe les articles lus sur son propre site.

Une donnée **third-party** est collectée ou exploitée par un tiers : régie publicitaire, tracker, SDK, data broker, plateforme d’analyse, outil de mesure.

La frontière est devenue moins lisible. Beaucoup de sites et d’applications utilisent des dizaines de partenaires tiers. L’utilisateur croit souvent interagir avec un seul service, alors qu’il alimente indirectement une chaîne d’acteurs.

Le consentement est censé redonner du contrôle. En pratique, les bandeaux de consentement sont souvent complexes, asymétriques, fatigants ou conçus pour pousser à l’acceptation. Le problème n’est donc pas seulement technique, mais aussi ergonomique et politique : un consentement obtenu par friction, fatigue ou obscurité n’a pas la même valeur qu’un consentement réellement éclairé.

#### 23.7 Identifiants publicitaires : cookies, MAID, hashed email, identity resolution

Historiquement, le web publicitaire s’est largement appuyé sur les **cookies tiers**. Un cookie tiers permettait à un acteur publicitaire de reconnaître un navigateur sur plusieurs sites différents. Les navigateurs modernes les bloquent de plus en plus, ou les rendent moins efficaces.

**Cookies tiers** : en déclin. Bloqués par défaut sur Safari (ITP depuis 2017), Firefox (ETP depuis 2019), Brave. Pour Chrome, Google a successivement annoncé leur dépréciation, puis a reculé en juillet 2024, et a confirmé en avril 2025 le maintien d’une approche par « choix utilisateur » sans dépréciation par défaut (cf. 23.6).

**Cookies first-party détournés** : utilisés pour profiler et partagés entre acteurs via des techniques de contournement (CNAME cloaking, server-side tracking via sous-domaine, etc.). De plus en plus courants pour compenser la perte des cookies tiers, et juridiquement plus difficiles à attaquer parce qu’ils semblent légitimes.

**MAID (Mobile Advertising ID)** :
Sur mobile, l’équivalent fonctionnel est l’**identifiant publicitaire mobile**, souvent appelé **MAID** (_Mobile Advertising ID_). Sur iOS, on parle d’IDFA ; sur Android, d’AAID. 
Ces identifiants sont conçus pour permettre le suivi publicitaire entre applications sans utiliser directement le nom civil de l’utilisateur. Mais cette pseudonymisation a des limites. Un identifiant publicitaire observé régulièrement la nuit dans une zone résidentielle, en journée dans un bâtiment professionnel, puis ponctuellement dans un lieu sensible — manifestation, lieu de culte, bâtiment administratif, base militaire, cabinet d’avocat, rédaction, ambassade — peut parfois être rattaché à une personne ou à une fonction avec un niveau de confiance significatif..

- **IDFA** (iOS) : désactivable depuis iOS 14.5 (App Tracking Transparency, ATT). En pratique, une majorité importante des utilisateurs iOS refuse le suivi lorsqu’une invite ATT s’affiche, ce qui a fortement réduit l’accès effectif à l’IDFA depuis 2021. Effet massif sur les revenus publicitaires mobiles à partir de 2021-2022, notamment pour Meta (pertes estimées à plusieurs milliards de dollars annuels).
- **AAID** (Android) : encore actif par défaut sur Android stock. Désactivable manuellement (Paramètres → Confidentialité → Annonces → Supprimer l’ID publicitaire). Google a introduit un Privacy Sandbox mobile en 2024-2025, mais l’AAID reste central pour la majorité des apps.

**Hashed Email** : ton email transformé en SHA-256 (ou autre fonction de hachage). Présenté comme « pseudonyme » mais en réalité c’est un identifiant déterministe et stable. L’espace des emails effectivement utilisés est fini et largement connu — tout courtier disposant d’une grande base peut faire la jointure trivialement. Vecteur dominant 2023-2026 pour les _people-based identifiers_.

**Identity resolution** : les _cookies tiers_ de nouvelle génération qui prennent le relais.

- **LiveRamp RampID** : identifiant déterministe lié aux emails hachés. Présent dans les principaux DSP et CDP.
- **The Trade Desk Unified ID 2.0 (UID2)** : standard ouvert porté par The Trade Desk, basé sur emails hachés. Adoption massive côté DSP en 2023-2025.
- **ID5** : société européenne, identifiant probabiliste agrégant plusieurs signaux.
- **Yahoo ConnectID, Criteo ID, Lotame Panorama ID, Merkle Merkury ID**, et autres.

Ces identifiants reposent sur ton email (ou ton numéro de téléphone) que tu as donné à des sites — et qui circule maintenant comme un _cookie permanent_ à travers l’écosystème, indépendamment de tout navigateur ou appareil.

**Conversion API (CAPI) côté serveur** : flux server-to-server qui contournent le navigateur.

- **Meta CAPI** : les marchands envoient les conversions (achats, inscriptions, etc.) directement aux serveurs Meta, sans passer par le navigateur. Bypass des bloqueurs de publicité et des restrictions navigateur. Déploiement explosif depuis 2021 en réponse à ATT.
- **Google Enhanced Conversions** : équivalent.
- **TikTok Events API, LinkedIn CAPI** : idem.

Ces flux sont structurellement invisibles côté utilisateur. Bloquer les trackers dans son navigateur ne suffit plus : ce qui circule entre le serveur du marchand et celui de Meta ou Google ne passe pas par ton appareil.

##### 23.8 AdTech, data brokers et plateformes

L’AdTech ne fonctionne pas seule. Elle s’articule avec trois autres écosystèmes.

D’abord, les **plateformes** : Google, Meta, TikTok, Amazon, Microsoft, Apple. Elles disposent de données first-party massives et de capacités de ciblage internes. Elles n’ont pas toujours besoin de cookies tiers, car elles contrôlent directement l’environnement utilisateur.

Ensuite, les **data brokers** : ils agrègent des données issues de multiples sources et revendent des segments, scores ou profils. Ils peuvent enrichir la publicité, mais aussi alimenter l’assurance, le crédit, le recrutement, l’investigation privée ou la surveillance commerciale.

Enfin, les **applications mobiles** : beaucoup d’applications gratuites intègrent des SDK publicitaires et analytiques. Ces SDK peuvent collecter des signaux très sensibles : localisation, modèle d’appareil, identifiant publicitaire, événements d’usage, horaires, langue, réseau, parfois données déclaratives.

C’est cette combinaison qui rend le modèle si robuste : même si un canal de tracking devient moins efficace, un autre prend le relais.

#### 23.9 ADINT : De la publicité au renseignement, exploitation opérationnelle des données publicitaires

L’**ADINT** (_Advertising Intelligence_) apparaît lorsque les mécanismes de l’écosystème publicitaire sont utilisés comme source de renseignement plutôt que comme support marketing. Les mêmes bid requests, les mêmes MAID, les mêmes bases de localisation qui servent à cibler une publicité peuvent servir à **identifier, suivre, corréler ou caractériser une personne, un groupe ou un lieu**.

Dans une logique marketing, ces données servent à vendre une publicité. Dans une logique ADINT, elles peuvent servir à identifier un appareil, suivre une routine, cartographier une présence dans un lieu sensible, enrichir un profil ou préparer une attaque ciblée.

La différence n’est pas toujours dans la donnée collectée, mais dans l’usage qui en est fait. Un identifiant publicitaire mobile, une donnée de localisation ou une bidstream data peuvent être banals dans un tableau de bord marketing, mais sensibles dans les mains d’un acteur qui cherche à identifier une source, un diplomate, un militaire, un activiste ou un journaliste.

L’ADINT illustre une idée centrale en OPSEC : une donnée collectée pour une finalité commerciale peut devenir exploitable pour une finalité de renseignement.

* géolocaliser ou suivre un appareil à partir de signaux publicitaires ;
* identifier des routines : domicile, travail, déplacements, lieux fréquentés ;
* cartographier des présences dans un lieu donné : institution, site militaire, événement politique, manifestation, lieu de culte ;
* déduire des attributs sensibles à partir des applications utilisées ou des lieux visités ;
* enrichir un profil avant une attaque ciblée : phishing, harcèlement, surveillance, compromission ;
* diffuser une publicité piégée ou rediriger vers un site malveillant dans certains scénarios de malvertising ou de watering hole.

Le sujet est devenu massif à partir de 2020. Le sénateur démocrate **Ron Wyden** (Oregon), membre du Senate Intelligence Committee, a été le premier élu américain à documenter publiquement, par lettres officielles aux agences, l’achat de données de localisation auprès de courtiers privés par DHS, ICE, IRS, FBI, DEA, US Military et d’autres entités fédérales. Sa série d’investigations 2020-2025 a fait sortir publiquement l’ampleur du phénomène.

##### 23.10.1 Le contournement juridique au cœur de l’ADINT

Aux États-Unis, l’arrêt **Carpenter v. United States (2018)** de la Cour suprême a établi que les forces de l’ordre doivent obtenir un mandat pour accéder aux Cell Site Location Information (CSLI) — les données de localisation cellulaire détenues par les opérateurs téléphoniques.

**Mais Carpenter ne couvre pas les achats de données auprès de brokers privés.** Les agences ont rapidement identifié ce contournement : pourquoi demander un mandat pour obtenir des données auprès de Verizon, alors qu’on peut acheter des données similaires (voire plus précises) auprès de courtiers qui les ont collectées via des SDK publicitaires dans des applications mobiles ?

Le résultat : entre 2017 et 2024, plusieurs dizaines de millions de dollars de contrats publics américains ont été identifiés pour l’achat de données de localisation provenant de l’écosystème adtech. Le sénateur Wyden a introduit le **Fourth Amendment Is Not For Sale Act (FANFSA)** pour fermer ce contournement, voté à la Chambre en 2024 mais bloqué au Sénat à la rédaction de ce cours.

En Europe, le cadre RGPD diffère structurellement : le traitement à des fins de renseignement par les autorités publiques est encadré par des directives sectorielles (LED — Law Enforcement Directive) et par les législations nationales sur le renseignement. Des zones grises persistent, notamment sur les transferts hors UE et sur le statut des achats par des services de renseignement nationaux auprès de courtiers américains. Ce sujet est peu documenté publiquement en Europe par rapport à la situation américaine.

##### 23.10.2 Cas Babel Street / Locate X

**Babel Street** est une société d’analyse de données fondée en 2014, basée en Virginie. Son produit phare **Locate X** agrège des données de localisation provenant de SDK adtech intégrés dans des applications mobiles, et permet à des analystes (typiquement gouvernementaux) de retracer les déplacements d’appareils dans le temps et l’espace.

Documenté pour la première fois par le journaliste Joseph Cox (Motherboard, puis 404 Media) en 2020 : Locate X était utilisé par CBP (US Customs and Border Protection), ICE (Immigration and Customs Enforcement), Secret Service, US Marshals, US Army, **sans mandat judiciaire**.

En 2024, 404 Media et l’EFF ont publié des enquêtes documentant que Locate X reste accessible à des acteurs n’ayant pas toujours fait l’objet de vérifications strictes, et qu’il a été utilisé pour démontrer publiquement la capacité à retracer :

- les déplacements d’un Marine vers les abords d’une base classifiée ;
- les habitudes hebdomadaires d’un juge fédéral ;
- les visites de personnes vers des cliniques d’avortement, dans un contexte post-arrêt Dobbs où ces déplacements sont devenus pénalement sensibles dans plusieurs États.

L’objectif éditorial de ces démonstrations journalistiques était de montrer publiquement qu’un outil officiellement commercial permet à toute partie disposant des bons accès d’atteindre des données de surveillance qui requerraient autrement un mandat judiciaire.

##### 23.10.3 Cas Anomaly Six (A6)

**Anomaly Six**, société de Virginie fondée par d’anciens membres de la communauté du renseignement américaine, opère dans un registre similaire : agréger des données de SDK adtech mobiles à grande échelle.

L’investigation marquante est celle publiée par le **Wall Street Journal en avril 2022**. Lors d’une démonstration à des journalistes, A6 a montré sa capacité à :

- géolocaliser un téléphone _à Moscou_ (vraisemblablement un téléphone russe) ;
- tracer un appareil dont les déplacements correspondaient à ceux d’un employé d’une agence de renseignement américaine ;
- le tout en exploitant **environ trois milliards de mouvements** d’appareils par jour dans sa base.

A6 est l’exemple paradigmatique de l’« intelligence-as-a-service » : une entreprise commerciale qui vend à des États (ou à d’autres entreprises) ce qui aurait autrefois nécessité une agence de renseignement entière. Le tout sans hacker quoi que ce soit — purement par exploitation de l’écosystème adtech légal.

##### 23.10.4 Cas Venntel / Gravy Analytics et sanction FTC 2024

**Venntel** est une filiale de **Gravy Analytics**, société de location data agrégeant les flux de centaines d’applications mobiles via SDK. Vendait géolocalisation à CBP, ICE, DEA, IRS, FBI, Département de la Défense américain.

L’IRS Inspector General (TIGTA) a publié en 2023 un rapport critique sur les achats sans mandat. La FTC a sanctionné Gravy Analytics et sa concurrente **Mobilewalla** par consent order en décembre 2024 — première sanction publique majeure contre des location brokers en lien avec le contournement de mandats.

**Janvier 2025 — la fuite Gravy Analytics** : un attaquant a exfiltré des dizaines de téraoctets de logs de localisation depuis l’infrastructure de Gravy. Révélation publique par 404 Media. Les données exposées permettaient de cartographier les déplacements de millions d’appareils, et d’identifier les apps sources — révélant par effet de bord la liste partielle des partenaires SDK de Gravy : applications météo, jeux mobiles, dating, applications religieuses ou de prière, traduction, fitness, et d’autres catégories grand public.

Cet incident a deux portées :

1. confirmer empiriquement que les données circulant dans l’adtech sont sensibles et identifiantes — pas seulement « pseudonymes » ;
2. démontrer que ces données sont elles-mêmes mal sécurisées chez les courtiers, exposant les utilisateurs à un risque double : commercial _et_ en cas de compromission du broker.

##### 23.10.5 Cas X-Mode / Outlogic et la sanction FTC 2024

**X-Mode Social** était l’un des principaux brokers de location data SDK. Bannie par Apple et Google en décembre 2020 après une enquête de Motherboard révélant des contrats avec des sous-traitants militaires et des ventes à des organismes gouvernementaux. Rebrand en **Outlogic** en 2021, qui a continué l’activité.

**Janvier 2024 — sanction FTC contre X-Mode/Outlogic** : _première fois_ qu’une autorité de régulation interdisait à un broker de vendre des données de localisation sensibles (visites à des cliniques de santé reproductive, lieux de culte, manifestations, locaux syndicaux, etc.). Consent order incluant l’effacement de catalogues entiers de données et l’interdiction permanente de vendre certaines catégories de localisation sensible.

Cette sanction a marqué un tournant régulatoire, mais l’écosystème reste massif et la majorité des acteurs continuent d’opérer.

**Synthèse des cas ADINT** : ces affaires montrent que l’ADINT n’est pas une hypothèse théorique. Des données collectées par des applications ordinaires — météo, jeux, dating, prière, traduction — via des SDK et des mécanismes publicitaires standards, peuvent être agrégées, revendues à des acteurs commerciaux ou gouvernementaux, puis utilisées pour produire une capacité de surveillance géospatiale opérationnelle. Le point critique n’est pas la précision d’une donnée isolée prise individuellement, mais la capacité à **agréger des signaux faibles sur la durée** jusqu’à reconstituer routines, identités et liens.

##### 23.10.6 Profils particulièrement exposés et limites des contre-mesures

Tous les utilisateurs peuvent être concernés par l’ADINT, mais certains profils sont structurellement plus sensibles : journalistes d’investigation et sources ; diplomates, militaires, policiers, magistrats ; dirigeants d’entreprise et cadres exposés ; activistes et opposants politiques ; chercheurs en cybersécurité ; personnels d’ONG travaillant dans des zones sensibles ; personnes victimes de harcèlement ou d’un adversaire de proximité.

Le risque devient particulièrement important lorsque l’appareil personnel est emporté dans des lieux sensibles. Un téléphone contenant de nombreuses applications gratuites financées par la publicité peut devenir un traceur involontaire, sans qu’il soit nécessaire de compromettre techniquement l’appareil.

##### 23.10.7 Pourquoi l'ADINT est difficile à contrer 

L’ADINT est difficile à neutraliser parce qu’elle exploite un écosystème **légal, massif et opaque**. Les acteurs publicitaires collectent déjà ces données pour le ciblage commercial. Des acteurs spécialisés peuvent ensuite s’insérer dans cette chaîne comme annonceurs, intermédiaires, courtiers ou prestataires d’analyse.

Le problème ne vient donc pas uniquement d’un malware ou d’une intrusion technique classique. Il vient aussi du modèle économique lui-même : applications financées par la publicité, SDK tiers, courtiers de données, enchères en temps réel, revente et agrégation de signaux.

Il n’existe pas de protection technique clé en main permettant de neutraliser totalement ce risque ; les mesures disponibles relèvent de la **réduction d’exposition**, de la **compartimentation** et, pour les profils les plus exposés, du **contrôle physique des appareils** (cf. 23.14). C’est précisément l’illustration que **ce n’est pas toujours une donnée isolée qui identifie, mais la répétition et la corrélation des signaux**.

#### 23.11 Privacy Sandbox, cookies tiers et recomposition post-cookie

Annoncée en 2019, la **Privacy Sandbox** de Google se présentait comme la réponse technologique au déclin des cookies tiers. Plutôt que tracker via des cookies cross-site, Chrome devait proposer des API on-device :

- **Topics API** : Chrome catégorise ton historique en « topics » (intérêts : sport, cuisine, voyages, etc., environ 380 catégories) et expose chaque semaine 3-5 topics aux sites.
- **Protected Audience API** (ex-FLEDGE) : enchères publicitaires _on-device_ basées sur tes « interest groups ».
- **Attribution Reporting API** : mesure des conversions sans tracking cross-site, avec bruit différentiel.

**La trajectoire 2024-2025 est celle d’un abandon partiel de l’ambition initiale** :

- **Juillet 2024** : Google annonce que Chrome **ne déprécie plus les cookies tiers par défaut**. La proposition est de basculer vers un choix utilisateur, sans précision sur la forme exacte.
- **Avril 2025** : Google confirme officiellement le maintien de cette approche « choix utilisateur ». Aucune dépréciation des cookies tiers n’est planifiée. Les API Privacy Sandbox restent disponibles en coexistence.
- **Octobre 2025** : Google annonce le **retrait progressif de plusieurs API Privacy Sandbox** — notamment Topics, Protected Audience et Attribution Reporting — pour faible adoption industrielle. D’autres briques de la Sandbox (notamment **CHIPS** pour les cookies partitionnés et **FedCM** pour la fédération d’identité) restent maintenues. La transition annoncée en 2019 comme une refondation de la publicité web se solde donc en abandon partiel de son ambition initiale, plutôt qu’en démantèlement complet.

Cette trajectoire est instructive en soi. Elle montre que **les standards de privacy poussés par les acteurs dominants restent dépendants de leurs intérêts commerciaux**. L’industrie publicitaire a refusé d’adopter massivement Privacy Sandbox, jugée trop limitante ; les autorités antitrust (notamment la CMA britannique) ont par ailleurs maintenu une pression critique sur le risque de renforcement du monopole Google. Résultat net : les cookies tiers persistent sur Chrome (environ 60-65 % du marché web mondial), l’identity resolution par hashed email progresse (cf. 23.4), et le fingerprinting reste un vecteur structurel.

**Critiques permanentes de la Privacy Sandbox** :

- **EFF, Brave, Mozilla** : Topics API peut servir de signal supplémentaire dans le fingerprint, et la catégorisation n’est pas anonyme à l’usage. Brave et Mozilla n’ont jamais implémenté Topics côté navigateur.
- **CMA (Competition and Markets Authority, UK)** : enquête depuis 2021 sur le risque que Privacy Sandbox renforce la position dominante de Google dans la publicité numérique.
- **Apple** : a refusé d’adopter ces standards, préférant son propre modèle (ITP, ATT, Private Relay).

**Pour l’utilisateur** : les API Privacy Sandbox encore actives peuvent être désactivées dans les paramètres Chrome (Paramètres → Confidentialité et sécurité → Confidentialité des publicités). Sur Brave, désactivées par défaut. Sur Firefox et Safari, non implémentées.

#### 23.12 SDK AdTech in-app mobile

Le tracking mobile diffère structurellement du tracking web. Sur le web, du JavaScript est injecté dans la page et peut être bloqué par uBlock Origin, NoScript, ou des configurations navigateur. Sur mobile, le tracking se fait via des **SDK natifs** embarqués dans l’application — du code compilé qui s’exécute avec les permissions de l’application elle-même.

**Top SDK adtech mobiles** :

- **AppsFlyer, Adjust, Singular, Branch** : attribution marketing (savoir d’où vient un utilisateur, mesurer l’efficacité d’une campagne).
- **OneSignal** : notifications push, intègre du tracking comportemental.
- **Mixpanel, Amplitude** : product analytics, avec capacités de fingerprinting et de cohort tracking.
- **Firebase Analytics / Google Analytics for Firebase** : par défaut dans la plupart des apps Android et iOS.
- **Meta SDK** : intégré dans des millions d’apps pour authentification Facebook + tracking conversion.
- **Smaato, Vungle, ironSource, AppLovin** : SDK de monétisation publicitaire.

Audit : **Exodus Privacy** (cf. Ch 15) liste les trackers présents dans une app Android donnée. Une application gratuite typique en intègre 5 à 30. Une application météo standard peut en intégrer plus de 20. Un jeu mobile « free-to-play » dépasse souvent 40 trackers actifs.

**iOS** : ATT (App Tracking Transparency) a réduit l’IDFA effectif, mais l’attribution probabiliste via fingerprint (SKAdNetwork est l’API officielle Apple, mais des techniques de probabilistic matching contournent partiellement le refus ATT) compense pour les annonceurs.

**Android** : AAID toujours actif par défaut sur Android stock. Le Privacy Sandbox for Android (annoncé 2022, déploiement progressif 2024-2025) propose des équivalents Topics API / Protected Audience API ; son avenir suit celui de la Privacy Sandbox web (cf. 23.6) et reste incertain à la rédaction.

**GrapheneOS** : pas de Google Play Services privilégiés, MAID minimisé, permission réseau granulaire par app, isolation forte entre apps via profils utilisateur. La plateforme mobile la mieux durcie contre les SDK adtech à 2026.

#### 23.13 CTV, Smart TV, ACR et retail media

L’AdTech ne se limite plus au web et au mobile. Trois fronts récents méritent attention.

**CTV (Connected TV)** : les applications de streaming (Netflix avec ads, Prime Video, Hulu, Disney+, YouTube TV, Pluto TV, Tubi) sont devenues des supports publicitaires majeurs depuis 2022-2023. La CTV ad voit typiquement :

- IP du foyer ;
- compte utilisateur (identifié et nominatif) ;
- modèle de TV ou device (Chromecast, Apple TV, Roku, Fire Stick) ;
- historique de visionnage dans l’app ;
- sur certaines plateformes, des MAID dédiés CTV (Roku Advertising Identifier, Samsung TIFA, Vizio IFA, etc.).

**ACR (Automatic Content Recognition)** : la TV elle-même regarde ce que toi tu regardes. Elle capture régulièrement des images de l’écran, les compare à une base de fingerprints visuels, et identifie le contenu joué — y compris depuis une console de jeu, une clé USB, ou la TNT. Acteurs : **Samba TV, Inscape** (Vizio), **iSpot.tv**, **TVision**, **VIDAA** (Hisense).

**Cas FTC vs Vizio (2017)** : Vizio condamné à 2,2 M$ d’amende pour avoir collecté de l’ACR sans consentement et l’avoir revendu à des courtiers. Pratique persistante chez la plupart des fabricants ; généralement désactivable mais activée par défaut.

**Désactiver l’ACR** :

- Samsung : Réglages → Général → Confidentialité → Services Smart Hub → désactiver « Données de visionnage ».
- LG : Réglages → Général → À propos → Politiques d’utilisation et de confidentialité → Refuser.
- Vizio : Réglages → Système → Reset & Admin → Smart Interactivity → Off.
- Roku : Réglages → Confidentialité → Smart TV Experience → désactiver « Use info from TV inputs ».

Pour profils sensibles : préférer une TV utilisée comme moniteur passif (HDMI uniquement, sans connexion réseau), avec un Apple TV ou un Nvidia Shield séparé qui peut être plus facilement audité.

**Retail Media Networks** : l’AdTech qui colonise les enseignes physiques.

- **Amazon Ads** : plus grand retail media network mondial, croissance fulgurante depuis 2021.
- **Walmart Connect, Target Roundel, Kroger Precision Marketing** (US).
- **Carrefour Links, Casino RelevenC** (FR, déploiement croissant), Tesco Media, Sainsbury’s Nectar360 (UK).

Le modèle : le distributeur (qui sait _exactement_ ce que tu achètes via ta carte de fidélité) revend des segments d’audience à des marques, qui peuvent alors te toucher en publicité sur le site du distributeur _et_ via des partenariats off-site. Ton achat de paracétamol chez Carrefour peut influencer la publicité que tu vois ailleurs sur le web — non pas via le tracking web classique, mais via la jointure cookie/email côté distributeur.

**Pour l’utilisateur** : la carte de fidélité, longtemps perçue comme une question commerciale anodine, est devenue un identifiant adtech majeur. Pour profils sensibles : carte de fidélité au pseudonyme, ou pas de carte du tout, ou paiement cash systématique pour les achats à isoler (cf. Ch 32).

#### 23.14 Le tracking n’est plus seulement les cookies

L’ère des cookies tiers se ferme (Chrome retarde mais Safari et Firefox les bloquent par défaut). En parallèle, le fingerprinting est devenu massif. Et l’identifiant publicitaire mobile reste actif.
Contrairement au cookie, qui est un fichier stocké localement et que l’utilisateur peut supprimer ou bloquer, le fingerprinting repose sur des caractéristiques plus structurelles de l’environnement : navigateur, système d’exploitation, résolution, paramètres régionaux, rendu graphique, configuration matérielle. L’utilisateur ne “supprime” donc pas son fingerprint comme il supprime un cookie ; il doit soit réduire les signaux collectables, soit se fondre dans un groupe d’utilisateurs au profil standardisé.
Le retour du fingerprinting s’inscrit dans la recomposition de l’AdTech post-cookies tiers. À mesure que les navigateurs limitent les cookies tiers, certains acteurs publicitaires cherchent des signaux alternatifs plus difficiles à bloquer. Le risque est de remplacer un tracking visible, stocké localement et partiellement contrôlable par l’utilisateur, par un tracking plus diffus, plus passif et moins maîtrisable.

#### 23.15 Tracking par infrastructure opérateur : cas Utiq

Le développement récent des initiatives publicitaires fondées sur des signaux opérateur/télécom, comme **Utiq**, illustrent une évolution importante : le tracking ne se limite plus au navigateur.

Utiq est une plateforme AdTech européenne portée par plusieurs grands opérateurs télécoms. Son objectif affiché est de proposer une alternative européenne aux cookies tiers et aux identifiants publicitaires dominés par les grandes plateformes américaines, en s’appuyant sur des signaux opérateur et un mécanisme de consentement utilisateur.

Le point important, pour un cours OPSEC, n’est pas de savoir si Utiq est légal ou illégal, ni de le présenter comme un spyware. Le sujet est plus subtil : Utiq illustre le déplacement du tracking vers une couche plus basse de l’infrastructure. Là où les cookies tiers étaient stockés dans le navigateur, et où l’identifiant publicitaire mobile dépendait du système d’exploitation, les solutions de type Utiq s’appuient sur la relation entre l’abonné, l’opérateur télécom, l’accès réseau et les sites ou applications partenaires.

Cela confirme que supprimer ses cookies ou changer de navigateur ne suffit pas toujours à maîtriser son exposition. Le tracking moderne doit être pensé en couches : navigateur, application, appareil, identifiant publicitaire, réseau, opérateur, plateforme, courtier de données.

Ce changement est important pour trois raisons.

Premièrement, l’opérateur télécom occupe une position privilégiée dans la chaîne réseau. Il connaît l’abonné, la ligne, la carte SIM, l’adresse IP attribuée, le type d’accès et certains paramètres de connexion. Même si le système prétend utiliser des jetons pseudonymes et un consentement explicite, la logique reste sensible : l’infrastructure d’accès à Internet devient aussi une infrastructure publicitaire.

Deuxièmement, la pseudonymisation ne doit pas être confondue avec l’anonymat. Un jeton publicitaire, même temporaire ou spécifique à un site, peut devenir un pivot de corrélation s’il est associé à des horaires, des lieux, des habitudes de navigation, des applications utilisées ou des événements récurrents. Comme toujours en privacy, le risque ne vient pas seulement de la donnée isolée, mais de sa répétition et de sa corrélation.

Troisièmement, ce type de mécanisme contourne partiellement l’intuition classique de l’utilisateur : supprimer ses cookies, changer de navigateur ou bloquer certains scripts ne suffit plus nécessairement à comprendre toute la chaîne de tracking. Le tracking moderne peut combiner plusieurs couches : navigateur, application, identifiant publicitaire mobile, fingerprint, IP, opérateur, consent management platform, bidstream data et données de courtage.

Utiq doit donc être compris comme un exemple de **tracking post-cookie** : un modèle où l’industrie publicitaire cherche de nouveaux identifiants parce que les cookies tiers deviennent moins fiables. Utiq revendique de son côté un modèle fondé sur le consentement utilisateur, des jetons spécifiques par site et un service de gestion (« Consenthub ») permettant de retirer son consentement. Le sujet OPSEC n’est donc pas d’assimiler Utiq à un spyware, mais de constater que l’identification publicitaire remonte vers une couche télécom — plus difficile à percevoir et à neutraliser pour l’utilisateur qu’un cookie navigateur.

Pour un utilisateur courant, le risque principal est l’extension du profilage publicitaire à une couche d’infrastructure plus difficile à percevoir. Pour un profil exposé — journaliste, source, activiste, dirigeant, diplomate, militaire, chercheur cyber — l’enjeu est que les signaux opérateur peuvent contribuer à la corrélation entre identité civile, appareil, localisation approximative, comportement réseau et consultation de contenus sensibles.

#### 23.16 Fingerprinting : mécanique

Un **fingerprint** est une signature dérivée de caractéristiques de ton navigateur ou de ton appareil, ramassées par un script JavaScript ou un SDK. Caractéristiques typiques :

- **User-Agent** : navigateur, version, OS.
- **Résolution écran**, profondeur de couleur.
- **Liste de polices installées** (par énumération CSS ou test).
- **Langue, fuseau horaire, locale**.
- **Plugins installés**.
- **Canvas fingerprint** : rendu d’une image cachée, qui varie par GPU et drivers.
- **WebGL fingerprint** : rendu 3D, qui varie selon le GPU.
- **AudioContext fingerprint** : signature audio produite par l’API AudioContext.
- **TLS fingerprint** (JA3/JA4) : combinaison de paramètres TLS qui identifie ton implémentation.
- **HTTP/2 fingerprint** : structure des frames.

Combinées, ces caractéristiques produisent une signature largement unique. EFF Cover Your Tracks et AmIUnique mesurent ce caractère unique. L’EFF avait montré dès 2010 (étude Panopticlick devenue Cover Your Tracks) que la quasi-totalité des navigateurs sont uniquement identifiables, ce qui rend le fingerprinting structurellement efficace.

Contrairement aux cookies, qui sont stockés localement et peuvent être supprimés, le fingerprint repose sur des caractéristiques structurelles. L’utilisateur ne peut donc pas simplement « effacer » son fingerprint ; il doit soit limiter les signaux exposés, soit utiliser un navigateur conçu pour se fondre dans un groupe d’utilisateurs standardisé.

Pour un tracker, un fingerprint utile doit être :

- **Unique** : distinguer les utilisateurs.
- **Stable** : durer dans le temps (sinon, perte de continuité).
- **Difficile à modifier** : sinon, l’utilisateur s’en échappe trivialement.

Le fingerprinting peut aussi servir des finalités légitimes — détection de fraude bancaire, statistiques de crash applicatif — ce qui rend la frontière entre fonctionnement légitime, sécurité antifraude et tracking publicitaire souvent invisible pour l’utilisateur.

L’EFF avait montré dès 2010 (étude Panopticlick devenue Cover Your Tracks) que la quasi-totalité des navigateurs sont uniquement identifiables, ce qui rend le fingerprinting structurellement efficace.

#### 23.17 Tracking comportemental

Au-delà des caractéristiques techniques, l’analyse comportementale exploite :

- **Mouvements de souris** : signature gestuelle.
- **Rythme de frappe** : keystroke dynamics.
- **Patterns de scrolling**.
- **Temps passé par section**.

Utilisé en détection de fraude (bonne intention) et en tracking publicitaire (intention plus ambiguë).

#### 23.18 Stratégies anti-fingerprint : blend in ou block

**Intuition fausse** : « si je change mon User-Agent pour celui de Chrome standard, je ressemble à plein de monde ». En réalité : Safari iOS est _intrinsèquement_ peu identifiable (peu de variation hardware). Si tu changes ton User-Agent vers Chrome Windows mais que ton canvas fingerprint reste Safari iOS, tu deviens **plus** unique, pas moins.

D’où la règle : **ne pas personnaliser les paramètres anti-fingerprint sauf si tu sais exactement ce que tu fais**. Utiliser des navigateurs conçus pour blend in (Ch 24).

Deux stratégies complémentaires :

**Stratégie 1 — Blend in** : ressembler à la masse. Tor Browser et Mullvad Browser appliquent : tous les utilisateurs ont la même résolution écran (par redimensionnement), la même police, le même User-Agent, le même fuseau horaire (UTC), le même canvas (rendu uniformisé). Chaque utilisateur est interchangeable, donc non identifiable individuellement.

**Stratégie 2 — Block** : bloquer les scripts de tracking. uBlock Origin, Privacy Badger, etc. Bloque la majorité des trackers connus. Mais ne bloque pas le fingerprinting first-party (par le site lui-même), et certains trackers passent.

Les deux stratégies sont complémentaires en théorie ; en pratique, Tor Browser / Mullvad Browser appliquent la première, et la seconde est utile pour navigateurs quotidiens.

#### 23.19 Cadre juridique : RGPD, TCF, DSA, DMA

L’écosystème adtech est encadré par plusieurs strates juridiques en Europe. Cette section donne les repères principaux ; le détail des décisions et le cadre comparé international sont traités au Ch 37.

**RGPD** : tout traitement à des fins publicitaires repose normalement sur le consentement (art. 6(1)(a)) ou l’intérêt légitime (art. 6(1)(f), interprétation restrictive). Le consentement doit être libre, spécifique, éclairé, univoque. En pratique, l’industrie a développé le **TCF** pour gérer ces consentements à l’échelle.

**TCF (Transparency and Consent Framework)** de IAB Europe : standard de facto pour les bannières de consentement adtech en Europe. La **version 2.2** (mai 2023) inclut 11 finalités et 10 fonctionnalités spéciales, communiquées via une chaîne technique standardisée (**TC String**) qui voyage avec les bid requests.

**CJUE, 7 mars 2024, C-604/22 — IAB Europe** : décision majeure. La Cour a jugé que la TC String peut constituer une donnée personnelle lorsqu’elle peut être associée à un identifiant comme l’adresse IP ou un cookie, et a précisé les conditions dans lesquelles IAB Europe peut être considérée comme responsable conjoint du traitement. Conséquences en cascade : les acteurs adtech qui s’appuient sur TCF doivent traiter chaque TC String comme une donnée personnelle, avec les obligations associées (information, finalité, durée de conservation, droit d’accès). La décision a été renvoyée à la juridiction belge pour application.

**Décisions nationales notables** : sanctions CNIL contre Google (150 M€, 2022) et Meta (60 M€, 2022) pour dark patterns dans les bannières cookies ; sanction APD belge contre IAB Europe (2022) à l’origine de la procédure CJUE ; multiples sanctions ultérieures 2023-2025 contre des CMP non conformes. **NOYB / Max Schrems** porte la majeure partie du contentieux par plaintes coordonnées multi-États.

**Digital Services Act (DSA, 2022, application 2024)** : transparence des publicités sur les _very large online platforms_ (VLOPs) — archives publicitaires publiques (Meta Ad Library, Google Ads Transparency Center), **interdiction du ciblage publicitaire des mineurs**, **interdiction du profilage publicitaire sur données sensibles** (religion, orientation sexuelle, opinion politique, santé).

**Digital Markets Act (DMA, 2022, application 2024)** : interdit aux _gatekeepers_ (Google, Meta, Apple, Amazon, Microsoft, ByteDance) certains croisements de données sans consentement explicite — notamment l’interdiction pour Meta de combiner les données de Facebook, Instagram et WhatsApp sans opt-in explicite. Effet réel partiel à 2026, contentieux en cours sur l’interprétation du « consentement libre » dans un contexte de gatekeepers.

**ePrivacy / dérogation CSAM** : le règlement ePrivacy attendu depuis 2017 n’est toujours pas adopté à 2026. Concernant la dérogation temporaire (règlement UE 2021/1232) permettant à certains services de communications interpersonnelles de détecter volontairement des contenus pédocriminels en ligne, le calendrier 2026 a été tendu : le Parlement européen a d’abord soutenu, le 11 mars 2026, une extension limitée jusqu’au 3 août 2027, avec un champ réduit et l’exclusion explicite des communications E2EE. Mais les négociations interinstitutionnelles avec le Conseil n’ont pas abouti : le 26 mars 2026, le Parlement a voté contre l’extension finale. **La dérogation a expiré le 3-4 avril 2026**, laissant les fournisseurs sans base juridique européenne harmonisée pour la détection volontaire de CSAM en communications privées. Les négociations sur le règlement permanent (« Chat Control 2.0 ») se poursuivent. Cf. Ch 26.12 sur Chat Control pour le suivi détaillé.

#### 23.20 Stratégie défensive en couches

Aucune mesure isolée ne neutralise l’AdTech. La défense réaliste opère par couches superposées, chacune réduisant l’exposition sans la supprimer entièrement.

**Couche navigateur** :

- Firefox + uBlock Origin (+ arkenfox pour profil technique), Brave Shields à _Aggressive_, ou Safari durci — pour le **Niveau 1**.
- Mullvad Browser pour recherches sensibles ou navigation privée renforcée — **Niveau 2**.
- Tor Browser pour sessions où l’anonymat réseau est central — **Niveau 2-3**.
- Ne pas être connecté à ses comptes Google/Meta dans le navigateur quotidien — multi-comptes containers Firefox ou profils Chrome distincts.

**Couche OS** :

- iOS : ATT à « Demander aux apps de ne pas suivre » par défaut ; Réglages → Confidentialité → Publicité Apple → Annonces personnalisées désactivé.
- Android stock : Paramètres → Confidentialité → Annonces → Supprimer l’identifiant publicitaire (effacement définitif depuis Android 12-13 sur certains constructeurs).
- GrapheneOS : pas de Google Play Services par défaut (donc pas d’Advertising ID Google exposé par défaut via Play Services) ; si l’utilisateur installe les Google Play Services sandboxés, un AAID peut exister selon la configuration du profil — vérifier et réinitialiser dans ce cas, ou éviter d’installer GPS dans les profils sensibles. Permission réseau granulaire par app, profils utilisateur isolés.
- macOS / Windows : limiter la télémétrie (cf. Ch 14).

**Couche application** :

- Audit Exodus Privacy avant installation d’une app Android.
- Préférer apps payantes ou open source (F-Droid) aux apps gratuites financées par la publicité.
- Désinstaller les apps gratuites « pourries de SDK » : météo, lampe torche, jeux gratuits, applications de prière, applications de rencontre — toutes catégories sur-représentées dans les fuites Gravy Analytics et autres.
- Limiter strictement la géolocalisation en arrière-plan.

**Couche réseau** :

- DNS chiffré avec filtre adtech : **NextDNS** (configurable), **AdGuard DNS**, ou **Pi-hole** auto-hébergé.
- VPN ponctuel pour masquer l’IP sur sessions sensibles (mais le VPN ne bloque pas le tracking applicatif ni le fingerprinting).

**Couche compartimentation** :

- Profils navigateur séparés par usage.
- Comptes Apple/Google séparés entre identités si Niveau 2-3.
- Email distinct pour les services gratuits financés par la publicité — usage d’alias (SimpleLogin, Addy.io).

**Couche physique** :

- Pour Niveau 3 : téléphone burner sans MAID actif, sans apps publicitaires, sans compte personnel, dans les lieux sensibles. Téléphone principal laissé hors zone.
- Cf. Capstone 1 (compartimentation) et Ch 38 (architectures par profil).

**Couche carte de fidélité / retail** :

- Pas de carte de fidélité au nom civil pour les achats à isoler.
- Cash pour les achats sensibles (Ch 32).
- Si carte indispensable, pseudonyme et adresse de domiciliation alternative (cf. Ch 7).

#### 23.21 Contre-mesures réalistes

Il n’existe pas de bouton unique permettant de sortir totalement de l’AdTech. La défense repose sur la réduction d’exposition.

Mesures utiles :

- refuser les cookies et finalités publicitaires non nécessaires ;
- utiliser un bloqueur de contenus sérieux comme uBlock Origin ;
- limiter les applications gratuites financées par la publicité ;
- privilégier les applications open source, payantes ou sans SDK publicitaires ;
- désactiver ou limiter l’identifiant publicitaire mobile ;
- refuser le tracking inter-applications sur iOS ;
- réinitialiser périodiquement l’identifiant publicitaire sur Android si l’usage l’exige ;
- limiter strictement la géolocalisation en arrière-plan ;
- séparer les profils mobiles lorsque l’OS le permet ;
- utiliser des navigateurs distincts par usage ;
- éviter de rester connecté à ses comptes Google, Meta ou Microsoft dans le navigateur utilisé pour des recherches sensibles ;
- utiliser Tor Browser, Tails ou Whonix pour les sessions où l’anonymat réseau est central ;
- éviter d’emporter son téléphone personnel dans des lieux sensibles ;
- pour les profils exposés, utiliser un appareil dédié minimaliste sans applications publicitaires.

Le point clé est qu’aucune couche n’est suffisante seule, mais que **leur empilement réduit fortement l’exposition**. Un utilisateur Niveau 1 appliquant disciplinement les couches navigateur, OS, DNS filtrant et audit applicatif réduit déjà très significativement son exposition par rapport à une configuration par défaut, sans entrer dans la compartimentation avancée de Niveau 2 ou 3.

Le tracking ne se limite plus au navigateur : il s’étend à l’écosystème publicitaire, aux applications, aux courtiers de données, aux identifiants mobiles, à la TV connectée, aux distributeurs, et désormais à certains signaux issus de l’infrastructure télécom. Dans une logique OPSEC, il faut raisonner en couches : appareil, application, navigateur, réseau, opérateur, plateforme, courtier de données.

-----

### Chapitre 24 — Navigateurs, moteurs de recherche et stratégies anti-fingerprint

#### 24.1 Le navigateur : ton plus gros vecteur

Le navigateur exécute du code (JavaScript) reçu de tiers, dispose d’accès à ton réseau, à ton stockage local, à ton fingerprint. C’est *l’application la plus dangereuse* sur ton appareil, et celle que tu utilises le plus. Son choix et sa configuration sont disproportionnellement importants.

#### 24.2 Tor Browser

**Modèle** : Firefox modifié pour anonymat maximal, intégré à Tor. Configuration standard : pas de plugins, JavaScript désactivable par niveau de sécurité (Standard/Safer/Safest), résolution standardisée, fingerprint uniformisé.

**Règle absolue** : **ne pas modifier Tor Browser**. Chaque modification te rend unique parmi les utilisateurs Tor, donc identifiable. Pas d’extensions ajoutées, pas de redimensionnement de fenêtre (Tor Browser uniformise par lettering), pas de changement de fuseau.

**Usage** : navigation anonyme ponctuelle, accès aux services onion, accès à des sites depuis des comptes anonymes.

#### 24.3 Mullvad Browser

Lancé en 2023 par Mullvad et Tor Project en partenariat. **C’est Tor Browser, sans Tor**. Même hardening anti-fingerprint, mais le trafic passe par où tu veux (VPN, ou rien).

**Pour qui** : utilisateurs qui veulent l’anti-fingerprinting du Tor Browser sans la latence Tor, et qui acceptent l’idée d’être dans un « pool Mullvad Browser » d’utilisateurs uniformisés.

**Recommandation forte** : Mullvad Browser pour navigation privée quotidienne, Tor Browser pour anonymat.

#### 24.4 Brave

Brave est un fork Chromium avec protections natives : bloqueur de trackers, anti-fingerprinting, mode Tor intégré (limité, à ne pas confondre avec Tor Browser).

**Avantages** : compatibilité Chromium (sites qui marchent partout), protections par défaut décentes, alternative Chrome pour qui ne peut pas Firefox.

**Limites** :

- Brave Rewards / Brave Search / Brave Ads : Brave a un modèle économique qui inclut sa propre régie publicitaire. Désactivable, mais à savoir.
- Modifications opaques par moments (par ex. ajout de référents dans certaines URLs cryptocurrency, fix dans 2020-2021).
- Mode Tor intégré : utilise le réseau Tor mais sans le hardening de Tor Browser. À ne pas utiliser comme substitut.

#### 24.5 Firefox + arkenfox / LibreWolf

**Firefox** standard : bon, surtout en activant Enhanced Tracking Protection (Strict), bloquant les cookies tiers, désactivant la télémétrie.

**arkenfox/user.js** : ensemble de configurations Firefox durcies, maintenu par la communauté. Pour profils techniques qui veulent ajuster Firefox finement.

**LibreWolf** : fork Firefox avec hardening arkenfox par défaut, télémétrie supprimée. Plus simple si tu veux du Firefox durci sans toucher à user.js.

**Limite** : Firefox + arkenfox ne donne pas le même « blend in » que Mullvad Browser ; tu restes individuellement identifiable. Bon pour bloquer, pas pour anonymiser.

#### 24.6 Safari, Vanadium

- **Safari** : intégration Apple, antitracking ITP correct, fingerprint relativement uniforme (du fait du peu de variation hardware iOS). Pas le plus configurable, mais pas le pire.
- **Vanadium** : navigateur intégré à GrapheneOS, basé sur Chromium avec hardening additionnel. Pas Firefox, donc différent profil de fuites mais bonne sécurité.

#### 24.7 Multi-navigateurs par usage

La pratique gagnante : **plusieurs navigateurs pour des usages distincts**.

- **Quotidien (banking, mail, services connectés)** : Brave ou Firefox.
- **Recherche/exploration** : Mullvad Browser, déconnecté.
- **Anonymat** : Tor Browser.
- **Travail sensible** : navigateur dans un environnement isolé (qube Qubes, Tails).

#### 24.8 Extensions : minimum utile

La règle est contre-intuitive : **moins tu installes d’extensions, mieux c’est**. Chaque extension :

- Te rend plus identifiable (signature unique).
- Est un vecteur potentiel de compromission (extension vendue, mise à jour malveillante).
- Augmente la surface d’attaque.

Le minimum viable :

- **uBlock Origin** : bloqueur de trackers et publicités, gold standard. À ne pas remplacer par AdBlock Plus (modèle « acceptable ads »).

Le reste est optionnel : NoScript pour contrôle granulaire JavaScript (mais lourd), HTTPS Everywhere (devenu inutile, HTTPS par défaut), Privacy Badger (utile en complément, parfois redondant avec uBlock).

Une extension de protection peut bloquer certains trackers, mais elle devient elle-même un signal de fingerprinting si elle modifie le comportement du navigateur d’une manière rare. L’objectif n’est donc pas d’empiler les extensions, mais d’utiliser un profil cohérent et commun à d’autres utilisateurs.

#### 24.9 Profils, containers, sessions séparées

Firefox supporte des **Multi-Account Containers** : onglets séparés avec cookies isolés. Tu peux avoir un onglet « personnel » et un onglet « travail » qui se croient sur des navigateurs différents. Très utile pour ne pas connecter accidentellement tes comptes.

Sur tous les navigateurs : utiliser plusieurs profils utilisateur (Chrome, Brave, Firefox supportent) pour des compartiments différents.

#### 24.10 Moteurs de recherche

- **Google Search** : profil publicitaire massif. Évite, ou ne l’utilise que connecté à ton identité civile pour les recherches non sensibles.
- **DuckDuckGo** : ne tracke pas par défaut. Bing en arrière-plan pour résultats. Acceptable mais incidents passés sur tracking Microsoft.
- **Brave Search** : propre index, modèle publicitaire séparé.
- **Startpage** : Google sans tracking (revend les requêtes anonymisées à Google).
- **SearXNG** : méta-moteur open source, agrège plusieurs moteurs. À auto-héberger ou utiliser sur instance de confiance.
- **Kagi** : payant, sans publicité. Modèle qui change l’incitatif : Kagi te facture, donc n’a pas besoin de vendre tes données. Recommandé pour qui peut payer.

Aucun moteur n’est parfait. Le choix dépend du compromis confidentialité/qualité/coût.

#### 24.11 Comptes connectés : perte d’anonymat instantanée

Tant que tu es connecté à un compte (Google, Facebook, Microsoft) dans un navigateur, *toute l’activité de ce navigateur* est rattachable à ce compte. Pas seulement les actions sur le site du compte. Les pixels et trackers du site qui te tracent en arrière-plan croisent ta navigation avec ton identité.

**Conséquence** : *ne pas* utiliser le navigateur où tu es connecté à ton Google personnel pour activité sensible. Multi-navigateurs ou containers.

#### 24.12 *Fil rouge* — Léa adopte Mullvad Browser

Léa configure son environnement de navigation :

- **MacBook Pro pro** : Firefox pour usage rédaction, Brave pour navigation rapide, Mullvad Browser pour recherche enquête.
- **Profil enquête sur GrapheneOS** : Vanadium pour mobile, Tor Browser disponible pour cas anonymes.
- **Pour les sessions Tails** : Tor Browser par défaut, jamais modifié.

Test post-config : AmIUnique et browserleaks sur chaque navigateur. Résultats : Mullvad Browser et Tor Browser sont en « pool » (similarité élevée à d’autres utilisateurs), Firefox + uBlock est intermédiaire, Brave varie selon Shields.

-----

## Partie 6 — Communications, comptes et données

> **Objectif** : protéger l’information à l’usage, au transit, au repos. Cette partie est la plus dense parce qu’elle couvre ce qui sera utilisé tous les jours.

-----

### Chapitre 25 — Cryptographie appliquée aux communications

#### 25.1 Chiffrement de bout en bout (E2EE) : promesse et limites

L’**E2EE** signifie : seul l’émetteur et le destinataire peuvent lire le contenu. Les serveurs intermédiaires (fournisseur de messagerie, opérateur, FAI) voient du chiffré indéchiffrable. C’est la propriété fondatrice de Signal, WhatsApp (contenu), iMessage (avec Contact Key Verification), Proton Mail (côté E2EE entre comptes Proton), etc.

**Ce que l’E2EE protège** : le *contenu* des messages contre les intermédiaires.

**Ce que l’E2EE ne protège pas** :

- Les **métadonnées** (qui parle à qui, quand, combien).
- Les **endpoints** : un téléphone compromis lit les messages en clair après déchiffrement local.
- Le **destinataire** : si la personne avec qui tu parles fait une capture d’écran ou transfère, l’E2EE n’y change rien.
- Les **sauvegardes non chiffrées** : WhatsApp sauvegardé sur iCloud sans chiffrement, c’est le contenu en clair côté Apple/Google.

#### 25.2 Forward secrecy

La **forward secrecy** (PFS) garantit qu’une clé compromise *aujourd’hui* ne permet pas de déchiffrer les messages *du passé*. Chaque session/message utilise une clé éphémère dérivée d’un échange Diffie-Hellman, puis détruite.

Sans forward secrecy : si l’attaquant capte aujourd’hui ta clé privée, il peut déchiffrer toutes tes communications passées qu’il aurait stockées en attendant. C’est exactement ce que font certaines agences avec leur stratégie « collect now, decrypt later ».

**Signal Protocol** (utilisé par Signal, WhatsApp, Wire) implémente la forward secrecy par double ratchet. **PGP/GPG** ne l’implémente pas (cf. Ch 27, l’une des grandes limites de PGP).

#### 25.3 Post-compromise security

La **post-compromise security** (PCS) ou *future secrecy* : si l’attaquant a compromis ta clé à un moment T, le protocole peut « se réparer » : un nouvel échange de clés rétablit la confidentialité pour les messages futurs.

Le double ratchet de Signal combine forward secrecy et PCS. C’est l’état de l’art en 2025.

#### 25.4 Deniability

La **deniability** (déniabilité) : tu peux nier de manière crédible avoir envoyé un message, parce que le protocole ne produit pas de preuve cryptographique irréfutable d’authorship. OTR (Off-the-Record) historique l’implémentait fortement. Signal Protocol l’implémente partiellement.

**Pour qui c’est important** : lanceurs d’alerte, sources, témoins. Si tu reçois une menace ou une preuve, tu ne veux pas qu’on puisse prouver mathématiquement qui te l’a envoyée. Pour la majorité, c’est un détail.

#### 25.5 Métadonnées de communication

Le vrai enjeu opérationnel. Une messagerie peut avoir une E2EE parfaite et révéler massivement :

- Numéro de téléphone (identifiant).
- Carnet d’adresses uploadé sur le serveur.
- Horodatage de chaque message.
- Type (texte, image, audio, fichier) et taille.
- Statut en ligne, dernière connexion.

Hiérarchie 2025 sur la réduction de métadonnées :

1. **SimpleX** : pas d’identifiant utilisateur du tout.
1. **Briar** : peer-to-peer via Tor, pas de serveur central.
1. **Signal** : sealed sender, minimisation côté serveur, mais numéro de téléphone toujours requis (atténué par les usernames depuis 2024).
1. **Matrix (auto-hébergé)** : tu contrôles ton serveur, mais les métadonnées y sont visibles à l’admin (toi).
1. **WhatsApp** : contenu E2EE, métadonnées chez Meta.
1. **iMessage** : E2EE, métadonnées chez Apple (avec ADP, certaines plus protégées).

#### 25.6 Vérification d’identité des contacts

L’E2EE ne sert à rien si tu communiques avec un imposteur. Les protocoles modernes proposent une vérification :

- **Safety Numbers (Signal)** : une chaîne de 60 chiffres dérivée des clés. À comparer manuellement, en personne ou par canal hors bande (vocal, vidéo). Si elle change, tu es alerté.
- **Contact Key Verification (iMessage)** : depuis iOS 17.2. Vérification cryptographique des clés iMessage entre contacts.
- **Fingerprints PGP** : à comparer hors bande.

Ces vérifications sont *à faire activement* pour les contacts critiques. La plupart des gens ne le font jamais. Pour un journaliste avec une source : c’est non négociable.

#### 25.7 Compromission des endpoints

Le chiffrement E2EE ne sauve pas un appareil compromis. Si ton téléphone est infecté par Pegasus, l’attaquant lit Signal en clair après déchiffrement local — comme toi.

C’est pourquoi la sécurité des appareils (Ch 14-15) et la détection de compromission (Ch 33) priment sur le choix de la messagerie. Une messagerie parfaitement chiffrée sur un téléphone compromis = aucune protection.

#### 25.8 Renvoi croisé

Le détail des primitives cryptographiques (AES, ECDH, double ratchet, etc.) est dans le cours dédié à la cryptographie de la bibliothèque. Ce chapitre s’arrête au niveau des propriétés, suffisant pour choisir des outils.

-----

### Chapitre 26 — Messageries chiffrées

> **Niveau de posture (cf. Ch 2.6)** : Signal pour tout + WhatsApp avec sauvegarde E2EE activée pour cercle qui ne migrera pas = **Niveau 1**. Signal avec username + iMessage avec Contact Key Verification pour cercle Apple + SimpleX pour quelques contacts particulièrement sensibles = **Niveau 2**. SimpleX comme canal primary + Signal sur GrapheneOS profil dédié + Briar pour offline / manifestations + vérification active des Safety Numbers en personne pour tous les contacts critiques = **Niveau 3**.

#### 26.1 Anatomie d’une messagerie chiffrée

À évaluer pour chaque option :

- Protocole de chiffrement et ses propriétés (E2EE par défaut ou opt-in ? Forward secrecy ? Open source ?).
- Identifiant utilisateur requis (numéro, email, pseudonyme, rien).
- Métadonnées exposées au serveur.
- Juridiction du fournisseur.
- Audits indépendants.
- Maturité et adoption (réseau utile).

#### 26.2 Signal

**Référence E2EE depuis 2014**. Signal Protocol open source, audité, déployé à 100+ millions d’utilisateurs. Propriétés :

- E2EE par défaut.
- Forward secrecy et PCS via double ratchet.
- Sealed sender : minimise l’information dont le serveur dispose (l’expéditeur d’un message ne lui est visible que sous certaines conditions).
- Numéros de téléphone historiquement requis ; depuis 2024, les **usernames** permettent de partager un identifiant de contact sans révéler le numéro. À comprendre précisément : **l’enregistrement initial du compte requiert toujours un numéro de téléphone** (lié à une SIM/eSIM, donc à un opérateur, donc en pratique à une identité civile dans la plupart des juridictions européennes). Ce que les usernames changent, c’est le partage de l’identifiant entre utilisateurs : tu peux donner ton @username à un nouveau contact sans lui dévoiler ton numéro. **Mais** les personnes qui ont déjà ton numéro dans leur carnet d’adresses continuent de te voir associé à ce numéro selon les réglages côté serveur Signal et le contexte. Pour réduire encore cette exposition, dans les paramètres Signal : « Téléphone » → « Qui peut me trouver par mon numéro » → *Personne*. Cela découple le numéro de la découverte sociale, mais l’enregistrement reste numérocentrique.
- **Disappearing messages** : expiration automatique configurable par conversation.
- **Safety Numbers** : vérification d’identité.

**Limites** :

- Service centralisé : Signal Foundation, basée aux États-Unis. Subpoena possible mais Signal a prouvé en justice ne posséder presque aucune donnée à fournir.
- L’enregistrement nécessite encore un numéro de téléphone (lié à un compte SIM, donc à un opérateur, donc à une identité).
- Apple/Google Play Store : la version officielle passe par eux ; alternative sur le site Signal pour Android.

**Pour qui** : tout le monde. C’est le minimum de l’hygiène 2025-2026.

#### 26.3 SimpleX

**Modèle radicalement différent** : pas d’identifiant utilisateur global. Tu communiques via des liens de connexion ou QR codes que tu partages. Aucune base centrale ne sait que tu existes.

**Propriétés** :

- E2EE par défaut (double ratchet, similaire à Signal).
- **Pas de carnet d’adresses uploadé**.
- **Pas de numéro de téléphone** requis.
- Architecture en relais : tu choisis tes serveurs (incluant possibilité d’auto-hébergement).

**Contraintes** :

- UX moins fluide que Signal pour le grand public.
- Cercle social plus restreint (effet réseau plus faible).
- Découverte de nouveaux contacts par échange de lien (frottement à chaque nouvelle relation).

**Pour qui** : journalistes-sources, lanceurs d’alerte, profils où le numéro de téléphone est une corrélation à éviter absolument.

#### 26.4 Briar

**Architecture P2P**, sans serveur central. Communications via Tor (par défaut) ou Bluetooth/Wi-Fi local (hors-ligne). Conçu pour environnements répressifs et coupures réseau.

**Cas d’usage** : manifestation, contexte sans internet, isolement réseau. Avec Briar, deux téléphones en proximité Bluetooth peuvent communiquer même sans aucun internet.

**Limites** : pas d’historique cloud, donc perte de téléphone = perte de tout. UX plus complexe. Pas d’appels (que des messages texte et forums).

#### 26.5 Matrix / Element

**Décentralisé fédéré**. Chaque utilisateur a un compte sur un *homeserver* (hébergeur). Les homeservers fédèrent : tu peux échanger entre serveurs comme avec email.

**Propriétés** :

- E2EE possible (à activer par salon).
- Auto-hébergement possible (synapse, dendrite).
- Pas de numéro de téléphone requis.

**Limites** :

- E2EE non par défaut historiquement (en train de changer, mais à vérifier).
- Métadonnées : ton homeserver voit tout. Si tu utilises matrix.org, c’est l’organisation Matrix.
- Complexité opérationnelle de l’auto-hébergement.
- Historique des messages côté serveur (selon configuration).

**Pour qui** : communautés open source, ONG avec capacité d’auto-héberger, équipes techniques.

#### 26.6 WhatsApp

**Le plus utilisé au monde (~3 milliards d’utilisateurs)**. Signal Protocol (E2EE) pour le contenu des messages. Mais :

- Métadonnées chez Meta (relations, fréquences, timings, statut en ligne).
- Carnet d’adresses uploadé sur les serveurs Meta (par défaut).
- Sauvegardes iCloud/Google Drive **non E2EE par défaut**. À activer manuellement (« Sauvegarde chiffrée de bout en bout ») depuis 2021.
- Intégration profonde aux services Meta.

**Pour qui** : usage avec contacts qui ne migreront jamais ailleurs. Ne pas y faire transiter du sensible. Activer la sauvegarde E2EE.

#### 26.7 Telegram

**Confusion fréquente**. Telegram n’est PAS E2EE par défaut. Seuls les **« Secret Chats »** le sont, et :

- Disponibles uniquement en 1-à-1, pas en groupe.
- Pas de synchronisation multi-appareil pour les Secret Chats.
- Protocole maison (MTProto) critiqué par les cryptographes.

Tous les autres chats Telegram (groupes, channels) sont chiffrés en transit *vers les serveurs Telegram*, qui peuvent les lire. Telegram a coopéré sélectivement avec des forces de l’ordre.

**Pour qui** : ne pas y faire transiter du sensible. Telegram est un outil de diffusion (canaux publics, larges groupes), pas une messagerie privée.

#### 26.8 iMessage

E2EE par défaut pour les iMessage (textos entre iPhones). SMS classiques (vers Android) : non E2EE.

**Contact Key Verification** (iOS 17.2+) : vérifie cryptographiquement les clés de tes contacts iMessage. Indispensable pour HVT.

**Limites** :

- Écosystème Apple uniquement (avec RCS support partiel en 2024-2025 mais pas E2EE).
- Sauvegardes iCloud : non-E2EE sans ADP activée (Ch 14).
- Pas d’audit indépendant du protocole côté Apple.

**Pour qui** : utilisateurs Apple-only, avec ADP activée et Contact Key Verification. Acceptable pour conversation modérément sensible entre Apple/Apple.

#### 26.9 Session, Threema, Wire

- **Session** : fork de Signal sans numéro de téléphone, route via réseau Loki (similaire à Tor). Modèle intéressant, adoption modeste.
- **Threema** : commercial suisse, payant unique, pas de numéro requis. Bonne réputation, niche.
- **Wire** : suisse également, support entreprise. Plus orienté pro.

#### 26.10 Choix par threat model

|Profil                |Stack recommandée                                                           |
|----------------------|----------------------------------------------------------------------------|
|Grand public durci    |Signal pour tout, WhatsApp si nécessaire avec sauvegarde E2EE               |
|Journaliste-source    |SimpleX pour canal source, Signal pour le reste                             |
|Activiste avant action|Signal avec disappearing messages, Briar pour offline                       |
|Dirigeant exposé      |Signal + iMessage avec ADP, vérification active des contacts                |
|HVT                   |SimpleX + Signal sur GrapheneOS, vérification systématique, reboot quotidien|

#### 26.11 OPSEC messagerie : pratiques

- **Disappearing messages** : activer par défaut sur conversations sensibles. Durée selon contexte (24h, 7 jours, 1 mois).
- **View-once** : pour photos/vidéos. Signal et WhatsApp supportent. Note : capture d’écran possible, défense imparfaite.
- **Safety Numbers** : vérifier en première rencontre avec contact sensible.
- **Audit des contacts** : périodiquement, qui a accès à quoi. Suppression des contacts non utilisés.
- **Notification preview** : désactiver sur écran verrouillé, ou minimiser (nom de l’expéditeur seulement, pas le contenu).

#### 26.12 Chat Control / CSAR UE : état du débat 2025-2026

La proposition de règlement « Chat Control » (CSAR — Child Sexual Abuse Regulation) circule en Europe depuis 2022, avec des versions successives. L’idée centrale : obliger les fournisseurs de messageries à scanner les contenus *avant* chiffrement E2EE pour détecter du CSAM (matériel pédopornographique).

**Position des cryptographes** : techniquement impossible sans casser l’E2EE. Le scanning côté client (« client-side scanning ») revient à insérer une backdoor, accessible à toute partie qui contrôlerait le mécanisme à terme. Signal a indiqué qu’il se retirerait de l’UE plutôt que d’introduire un tel scanning. ProtonMail, Threema et la plupart des fournisseurs E2EE européens ont des positions similaires.

**État au moment de la rédaction (2026)** : le dossier reste mouvant et hautement politique. Le Conseil de l’UE a adopté en novembre 2025 une orientation générale ouvrant la porte à un scanning « volontaire » étendu et discutant de plusieurs options sur le scanning obligatoire. En mars 2026, le Parlement européen a soutenu l’extension temporaire de la dérogation ePrivacy (qui autorise déjà certains scans volontaires de contenus non E2EE) jusqu’en août 2027, afin d’éviter un vide juridique pendant que les négociations se poursuivent. Les positions nationales restent contrastées — certains États (notamment l’Allemagne et l’Autriche pendant plusieurs phases) ont exprimé des réserves fortes sur l’atteinte à l’E2EE ; d’autres (France, Espagne, Italie sur certaines périodes) ont soutenu une version exigeante. La présidence tournante du Conseil influence fortement le calendrier.

**Implication pratique pour le lecteur** :

- Le risque que l’E2EE européenne soit affaiblie n’est pas conjuré.
- Le calendrier exact et la forme finale (scanning obligatoire, volontaire étendu, ciblé seulement) restent ouverts.
- Suivi recommandé via *European Digital Rights* (EDRi, https://edri.org), *La Quadrature du Net*, *Patrick Breyer* (eurodéputé qui suit le dossier de près sur https://patrick-breyer.de), et *Center for Democracy & Technology*.
- Pour profils sensibles : ne pas baser sa stack uniquement sur des fournisseurs européens E2EE sans plan B (SimpleX, Briar, hébergement en Suisse hors UE, etc.).

#### 26.13 *Fil rouge* — Léa et Karim choisissent SimpleX

Léa reçoit, via une rédaction tierce, un signal que Karim B. veut entrer en contact. Premier échange via une boîte morte ProtonMail. Léa propose : SimpleX, parce que ni Karim ni elle n’ont besoin de révéler leur numéro de téléphone. Karim installe SimpleX sur un téléphone d’occasion qu’il a acheté cash. Première rencontre numérique : Léa envoie un lien d’invitation via le canal ProtonMail. Connexion établie. Vérification : ils s’appellent par appel SimpleX et se lisent les Safety Numbers. Puis, basculement en disappearing messages 24h pour toute la conversation.

-----

### Chapitre 27 — Email, PGP et limites structurelles

#### 27.1 Pourquoi l’email est intrinsèquement mauvais pour la confidentialité

L’email a 50 ans. Il a été conçu avant la confidentialité moderne. Conséquences structurelles :

- **Métadonnées en clair** : expéditeur, destinataire, objet, horodatage. Tous visibles à chaque relais.
- **Transit en clair entre serveurs** : si l’expéditeur ou le destinataire utilise un service sans TLS systématique, le mail circule en clair sur certains hops. TLS opportuniste signifie « si possible » ; MTA-STS et DANE améliorent, sans garantir.
- **Pas de chiffrement par défaut** : sauf si tu utilises PGP/S-MIME (qui couvrent le contenu mais pas l’objet et pas les métadonnées).
- **Pas de forward secrecy** : la compromission de ta clé PGP permet de relire tous tes mails passés.

L’email reste indispensable (interopérabilité universelle). Pour les communications réellement sensibles, il faut autre chose (Ch 26 ou 28).

#### 27.2 SMTP, headers, métadonnées

Un email arrive avec des en-têtes :

- `From`, `To`, `Cc`, `Date`, `Subject` (objet).
- `Received` : chaîne de serveurs traversés, avec IPs et horodatages — utile en forensique mais révèle ton parcours.
- `X-Originating-IP` : sur certains fournisseurs, ton IP au moment de l’envoi.
- `Message-ID`, `References` : identifiants uniques.
- `User-Agent` : ton client mail.

Tout ceci est visible à tout intermédiaire.

#### 27.3 PGP / GPG : modèle, utilité, complexité

**PGP** (Pretty Good Privacy) ou son équivalent libre **GPG** chiffre le contenu d’un message avec la clé publique du destinataire. Modèle de confiance : *web of trust* (chaque utilisateur certifie les clés d’autres en qui il a confiance).

**Utilité** : pour communications sensibles entre parties techniques. Pour signature de logiciels, signature de mails, vérification d’identité.

**Limites majeures** :

- **Pas de forward secrecy** : la clé privée compromise expose toute la correspondance.
- **Complexité opérationnelle** : génération, gestion d’expiration, révocation, distribution. La plupart des utilisateurs s’y perdent.
- **Erreurs structurelles documentées** : EFAIL (2018) a montré qu’une mauvaise intégration côté client peut permettre exfiltration via images chargées.
- **Métadonnées non protégées** : objet, expéditeur, destinataire, horodatage restent en clair.
- **UX hostile** : presque toutes les implémentations grand public ont des frottements importants.

**Pour qui** : profils techniques qui peuvent vraiment maintenir une stack PGP. Pour les autres, Signal/SimpleX est mille fois préférable.

#### 27.4 PGP en pratique

Outils :

- **Thunderbird** : intégration PGP native depuis 78+, avec gestion du trousseau, signature, chiffrement, vérification.
- **gpg en CLI** : pour profils techniques, complet.
- **Smartcards / clés matérielles** : YubiKey, Nitrokey supportent PGP. Clé privée jamais sur l’ordinateur, opérations cryptographiques sur la carte. Pour profil sensible : génération sur air gap (Ch 13), import sur Smartcard.

Cycle de vie d’une clé PGP :

1. Génération sur machine sûre (idéalement air gap), 4096 bits RSA ou Ed25519.
1. Sous-clés séparées pour signature et chiffrement, sous-clés avec expiration courte (1 an).
1. Sauvegarde de la clé maître en lieu sûr, hors ligne.
1. Diffusion de la clé publique (keyserver, site web, GitHub, mails de signature).
1. Renouvellement annuel des sous-clés.
1. Révocation prête à l’emploi en cas de compromission.

#### 27.5 Proton Mail, Tuta, Mailbox.org, Fastmail

- **Proton Mail** : Suisse, E2EE entre comptes Proton (transparent pour l’utilisateur), bridging IMAP/SMTP local pour clients tiers, alias, hébergement sous juridiction protectrice. Modèle freemium. Audit Cure53. Référence pour la plupart.
- **Tuta (anciennement Tutanota)** : Allemagne, E2EE de bout en bout (y compris objet, ce que ne fait pas Proton historiquement). Recherche dans mails chiffrés côté client. Pas de support IMAP (limite).
- **Mailbox.org** : Allemagne, focalisé service mail propre et stable, bon support PGP.
- **Fastmail** : Australie, juridiction moins idéale (Five Eyes), mais excellent service et propre. Pas d’E2EE par défaut.

**Pour qui** : Proton ou Tuta pour profil privacy. Mailbox.org si tu veux du PGP propre dans un service européen sérieux.

#### 27.6 Alias email

Un **alias** est une adresse email qui forwarde vers ta vraie adresse, sans révéler celle-ci.

- **SimpleLogin** (acquis par Proton) : adresses aléatoires ou personnalisées, gestion par projet. Intégré dans Proton si tu y es.
- **Addy.io** (anciennement Anonaddy) : open source, similaire.
- **Hide My Email** (Apple) : intégré iCloud+, alias par site.
- **DuckDuckGo Email Protection** : gratuit, transformation des trackers en plus du forward.

**Usage** : un alias par service. Quand le service fuite (et il fuitera), tu sais lequel a fuité, tu peux le retirer, et ton email principal reste intact.

#### 27.7 Architecture multi-emails

Une bonne architecture email :

- **Email principal nominatif** : seulement pour services administratifs et professionnels critiques. Jamais utilisé ailleurs.
- **Email admin secondaire** : pour comptes utilitaires (services publics, opérateurs).
- **Email pro public** : pour ta présence professionnelle visible.
- **Email pseudonyme** : pour ton compartiment pseudonyme stable, si applicable.
- **Aliases par service** : pour tout le reste (commerce, newsletters, inscriptions).

Le centre de gravité (Ch 4 et Ch 29) est l’email principal. Sa protection prime.

#### 27.8 Chiffrement de pièces jointes quand PGP exclu

Si ton destinataire ne sait pas utiliser PGP : chiffrer la pièce jointe avant envoi.

- **Cryptomator** : conteneur dossier (Ch 30), partageable comme dossier zippé.
- **7z avec mot de passe** : universellement lisible, AES-256, mot de passe partagé hors bande.
- **Zed!** : conteneurs auto-extractibles chiffrés (cas francophone, secteur public, justice). Le destinataire reçoit un exécutable qui demande un mot de passe pour extraire — pratique pour non-techniques. Mot de passe transmis par SMS, appel, hors bande.

Le mot de passe **ne doit pas circuler par email**. C’est l’erreur de débutant classique.

#### 27.9 OPSEC email

- **Never reply** : ne pas répondre directement à un mail sensible (laisse une trace de la conversation). Plutôt initier un nouveau canal (Signal, appel).
- **Objets neutres** : pas « Documents confidentiels Acme Corp » mais « Suite à notre conversation ».
- **Signatures professionnelles** : standard, sans révéler l’organigramme interne.
- **Pas de footer corporatif systématique** sur les comptes pseudonymes.

#### 27.10 *Fil rouge* — Léa configure son écosystème email

Léa migre :

- **Email principal Gmail** → Proton Mail, avec migration progressive (notification de nouvel email aux contacts important sur 3 mois). Gmail reste actif comme « catch-all » pour les services anciens, et désactivé pour récupérations d’autres services.
- **Aliases SimpleLogin** : un par service nouveau.
- **Email pro public** : `lea.martens@[domaine du consortium]`, hébergé par eux, PGP activé.
- **Email pseudonyme** : nouveau compte Proton, jamais croisé avec l’identité civile (créé via Tor, depuis Tails, paiement Monero).

Une semaine de configuration. Un mois pour stabiliser les habitudes.

-----

### Chapitre 28 — Partage sécurisé de fichiers et documents

#### 28.1 OnionShare

**OnionShare** crée un service onion temporaire sur ton ordinateur. Tu choisis un fichier ou dossier, OnionShare génère une adresse `.onion`. Tu communiques cette adresse à ton destinataire, qui télécharge via Tor Browser. Le transfert est :

- Direct (P2P en pratique, via Tor).
- Anonyme côté serveur (tu) et côté client (destinataire).
- Temporaire (le service tombe à la fermeture).

**Cas d’usage** : envoi de documents par un journaliste à un correspondant, par un lanceur d’alerte. Très utile et sous-utilisé.

**Limites** : ton ordinateur doit rester allumé pendant le transfert ; le destinataire doit avoir Tor Browser ; vitesse limitée par Tor.

#### 28.2 SecureDrop

**SecureDrop** est une plateforme open source pour rédactions, permettant aux lanceurs d’alerte de soumettre anonymement des documents. Initialement conçue par Aaron Swartz et Kevin Poulsen sous le nom DeadDrop, reprise et durcie par la *Freedom of the Press Foundation* (FPF) à partir de 2013, elle est devenue le standard de facto pour les soumissions anonymes aux médias.

**Architecture** : trois machines distinctes, isolées physiquement.

- **Source server** : serveur public accessible *uniquement* via une adresse `.onion` Tor. Reçoit les soumissions, les chiffre par GPG vers la clé publique de la rédaction.
- **Journalist workstation** : utilisée par les journalistes pour consulter (en lecture seule) les soumissions chiffrées via une connexion authentifiée.
- **Secure viewing station (SVS)** : machine air-gapped où les documents sont déchiffrés et examinés. Connectée à aucun réseau. Tails par défaut. Les transferts depuis la journalist workstation se font par USB neuve.

**Cas d’usage documentés** : Le Monde, Mediapart, The Guardian, The Intercept, The Washington Post, The New York Times, Süddeutsche Zeitung, ProPublica, USA Today, AP, Bloomberg, NPR, et plusieurs dizaines d’autres rédactions opèrent un SecureDrop. La liste publique est maintenue sur https://securedrop.org/directory/.

**Workflow source** :

1. La source télécharge Tor Browser depuis https://torproject.org sur un appareil qu’elle considère propre.
1. Elle se rend à l’URL `.onion` du SecureDrop de la rédaction (URL communiquée publiquement par la rédaction sur son site, vérifiable).
1. À la première visite, le système génère un nom de code unique (codename) à mémoriser ou noter de manière sécurisée. Ce codename remplace toute identité — le système ne demande aucune info personnelle.
1. La source soumet documents et message. Tout est chiffré côté serveur avec la clé publique de la rédaction.
1. La source peut revenir ultérieurement (avec son codename) pour recevoir des réponses des journalistes.

**Workflow journaliste** :

1. Connexion à la journalist workstation, authentification.
1. Téléchargement des soumissions chiffrées.
1. Passage des fichiers sur USB neuve vers la SVS air-gapped.
1. Déchiffrement et examen sur la SVS, dans Tails.
1. Réponse éventuelle à la source via le codename (sans connaître son identité).

**Limites** :

- Déploiement complexe (matériel dédié, formation, maintenance). Pas pour une rédaction isolée sans budget cyber.
- Latence d’usage (consultation des soumissions sur machine air-gap).
- Pas pour particulier — c’est une infrastructure organisationnelle.
- L’identité de la source reste vulnérable à des erreurs OPSEC côté source (utilisation depuis le bureau, métadonnées des documents non purgées, etc.). SecureDrop protège le canal, pas l’OPSEC opérationnelle de la source.

**Pour qui** : rédactions et ONG sérieuses ; soutien FPF disponible pour le déploiement initial. **Pour une source qui veut joindre une rédaction qui a SecureDrop** : utiliser leur lien `.onion` officiel via Tor Browser, idéalement depuis Tails, depuis un lieu non identifiable, en respectant les principes OPSEC du Capstone 3.

#### 28.3 GlobaLeaks

**GlobaLeaks** est l’équivalent open source pour ONG, autorités anti-corruption, structures juridiques. Modèle similaire à SecureDrop, déploiement plus accessible.

**Exemples** : Whistleblowing Italia, plusieurs structures européennes anti-corruption.

#### 28.4 CryptPad

**CryptPad** est un suite collaborative chiffrée de bout en bout. Édition de documents (texte, tableur, présentations, kanban, code, formulaires) sans que le serveur ne lise le contenu. Open source, instance officielle française (CryptPad.fr) hébergée par XWiki, auto-hébergement possible.

**Pour qui** : collaboration sensible (rédaction d’une note avec une source, ONG, journalistes en équipe). Excellent positionnement E2EE pour des cas où Google Docs n’est pas envisageable.

#### 28.5 Liens temporaires

Pour partage one-shot non sensible :

- **Bitwarden Send** : intégré au gestionnaire de mots de passe Bitwarden, fichier ou texte chiffré, expiration configurable. Limite gratuite à 500 MB par fichier (1 GB pour Premium).
- **Firefox Send (mort)** : Mozilla a retiré le service en 2020.
- **0bin, PrivateBin** : pour partager du texte / code, E2EE côté client, paste sites auto-hébergeables.

Tous ces outils sont **chiffrés côté client** : la clé est dans l’URL (fragment après `#`), jamais envoyée au serveur.

#### 28.6 Chiffrement avant envoi

Quand tu utilises un canal non confiance (email, cloud, partage de fichier), chiffrer avant envoi. La hiérarchie :

- **GPG asymétrique** si destinataire l’utilise.
- **Conteneur Cryptomator** ou **VeraCrypt** pour gros volumes, mot de passe transmis hors bande.
- **7z avec mot de passe AES-256** pour cas généralistes.
- **Zed!** pour secteur public francophone.

#### 28.7 Vérification d’intégrité

Quand tu reçois un fichier important d’une source, vérifier qu’il n’a pas été modifié :

- Hash SHA-256 calculé par la source et envoyé hors bande (Signal, vocal).
- Comparaison locale : `sha256sum fichier.pdf` (Linux/macOS), `Get-FileHash` (PowerShell).
- Si correspondance, intégrité confirmée.

#### 28.8 Menaces liées aux documents reçus

Un PDF reçu peut contenir :

- JavaScript malveillant.
- Exploits de visionneuses (Adobe Reader a un long historique).
- Pixels traceurs (en cas d’ouverture en ligne).
- Métadonnées qui révèlent l’auteur, le logiciel, l’environnement.

Procédure défensive :

1. **Jamais ouvrir dans le client mail** (preview désactivée).
1. **Téléverser dans un environnement isolé** (VM jetable, Tails, dispVM Qubes).
1. **Passer par Dangerzone** pour produire un PDF propre.
1. **Auditer les métadonnées** avec ExifTool ou MAT2 (Ch 31).

#### 28.9 *Fil rouge* — Léa met en place un point de contact OnionShare

Léa annonce sur son site professionnel (page « Comment me joindre confidentiellement ») :

- Sa clé PGP publique.
- Le lien `.onion` de son SecureDrop personnel (déployé avec aide technique d’un confrère).
- Son numéro Signal (username, pas son téléphone).
- Une mention claire : « Pour documents sensibles, contactez-moi d’abord, on choisit le canal ».

Le canal Signal sert au premier contact ; OnionShare/SecureDrop pour les transferts effectifs.

-----

### Chapitre 29 — Comptes critiques, authentification et secrets

> **Note pédagogique** : ce chapitre est long. Il est structuré en trois sous-blocs majeurs : (A) comptes critiques et récupération, (B) mots de passe et coffres, (C) MFA, passkeys et clés physiques. Chacun peut être lu indépendamment, mais ensemble ils forment l’architecture d’authentification personnelle.

#### A. Comptes critiques et récupération

#### 29.1 L’email principal comme centre de gravité

L’email principal n’est pas un compte parmi d’autres. C’est le **pivot** :

- Récupération de mot de passe de la quasi-totalité des services.
- Réception des codes MFA par email (à éviter, mais courant).
- Notifications de connexion suspectes.
- Identifiant de récupération de comptes Apple/Google/Microsoft.

**Sa compromission cascade en compromission massive**. Sa protection prime sur tout.

Mesures concrètes :

- Mot de passe unique et long (gestionnaire obligatoire, Ch 29.7).
- MFA matériel ou TOTP (jamais SMS pour ce compte).
- Audit régulier des sessions actives.
- Surveillance des notifications de connexion (paramétrer alertes).
- Récupération configurée mais audit régulier (méthodes de récupération, contacts de récupération, codes).

#### 29.2 Comptes pivots : Apple ID, Google, Microsoft

Selon l’écosystème, ces comptes contiennent : iCloud (photos, contacts, sauvegardes, mails, Keychain), Google (Gmail, Drive, photos, contacts, Android backup), Microsoft (OneDrive, Office, BitLocker recovery). Leur compromission = perte d’une grande partie de la vie numérique.

Mesures :

- Vérification en 2 étapes activée (FIDO2 idéalement).
- Clés de sécurité matérielles enregistrées.
- Mode protection avancée Google (Advanced Protection Program — pour cibles à risque).
- ADP iCloud activée.

#### 29.3 Récupération de compte : le maillon faible

La compromission d’un compte sécurisé passe presque toujours par **la récupération**, pas par l’attaque directe :

- SIM swap pour intercepter les SMS de récupération.
- Réponse à questions de sécurité devinées (par OSINT sur la cible).
- Accès au mail de récupération.
- Social engineering du support client.

Audit régulier :

- Numéro de téléphone de récupération : à jour, sécurisé (cf. anti-SIM swap).
- Email de récupération : sur compte sérieusement sécurisé.
- Questions de sécurité : réponses **fausses** mais mémorisables (« nom de jeune fille de ta mère » → ne pas répondre la vraie ; répondre une chaîne aléatoire stockée dans le gestionnaire).
- Contacts de récupération (Apple « Account Recovery Contacts ») : choisir précautionneusement.

#### 29.4 Sessions actives et appareils

Tous les services majeurs proposent une vue « appareils connectés » ou « sessions actives ». À auditer mensuellement :

- Quelles sessions sont actives ?
- Sur quels appareils, depuis où, depuis quand ?
- Y a-t-il des sessions inconnues ?
- Révoquer les sessions inactives ou suspectes.

#### 29.5 Anti-SIM swap

Le SIM swap consiste, pour un attaquant, à convaincre ton opérateur de lui donner ta ligne sur sa SIM. Tous les SMS et appels arrivent chez lui. La récupération de comptes par SMS devient sienne. Cas documentés en Belgique, France, US, partout.

Défenses :

- **PIN opérateur** : pour appeler ton opérateur et faire un changement de SIM, exiger ce PIN. À mettre en place auprès de l’opérateur, à mémoriser, à ne jamais réutiliser.
- **eSIM** : moins facile à transférer (lié à un appareil, opérations généralement à distance avec auth forte).
- **MVNO sérieux** : certains opérateurs sont plus stricts sur les procédures.
- **Filtre par questions** : tes informations de contact sécurité avec l’opérateur ne sont pas dérivables d’OSINT.

#### B. Mots de passe et coffres

#### 29.6 Unicité > complexité mémorisée

L’ère du « mot de passe complexe à mémoriser » est révolue. Un mot de passe par service, généré aléatoirement, stocké dans un gestionnaire. C’est la seule approche soutenable :

- **Unicité** : la réutilisation est la première cause de compromission de comptes. Quand un service fuite (et il fuitera), tous tes autres comptes avec le même mot de passe tombent.
- **Longueur > complexité** : 20+ caractères aléatoires > 8 caractères « complexes ». Un gestionnaire les génère.
- **Mot de passe maître** : ton unique mot de passe humainement mémorisable. Doit être long, unique, aléatoire dans une certaine mesure. Phrase de passe Diceware (6-8 mots aléatoires) recommandé.

#### 29.7 Gestionnaires : Bitwarden, KeePassXC, 1Password, Proton Pass

- **Bitwarden** : open source, freemium, cloud par défaut (auto-hébergement via Vaultwarden possible). Audits Cure53 réguliers. Standard pour la plupart.
- **KeePassXC** : open source, 100 % local. Base chiffrée à synchroniser manuellement si multi-appareil (Syncthing, Nextcloud, Dropbox+Cryptomator). Pour profils techniques privacy-maximalistes.
- **1Password** : commercial, propre, cloud propre. Bonne UX. Audits réguliers. Canadien (juridiction acceptable). Plan famille.
- **Proton Pass** : nouveau, intégré à Proton, alias email intégrés.

**Anti-recommandation** : LastPass, après les fuites de 2022-2023 (compromission des coffres clients, exfiltration des données chiffrées qui permettent un brute-force offline). À éviter.

#### 29.8 Vaultwarden self-hosted

**Vaultwarden** est une réimplémentation serveur compatible avec les clients Bitwarden. Auto-héberger sur un VPS ou un serveur domestique te donne :

- Contrôle total des données chiffrées.
- Latence faible.
- Pas de dépendance à un fournisseur externe.

Coût : maintenance technique (mises à jour, sauvegardes du serveur, monitoring). Si tu n’es pas en mesure de gérer cela, Bitwarden cloud est préférable.

#### 29.9 KDF : Argon2id, scrypt, PBKDF2

La **Key Derivation Function** transforme ton mot de passe maître en clé de chiffrement. Sa résistance détermine la difficulté du brute-force offline en cas de fuite du coffre.

- **Argon2id** : référence 2025, résistant aux ASIC et GPU. À privilégier.
- **scrypt** : bonne alternative, plus ancienne.
- **PBKDF2** : ancienne génération, moins résistante. Par défaut historique de Bitwarden, qui a migré vers Argon2id en option en 2023.

Configurer son gestionnaire avec Argon2id et paramètres élevés (mémoire ≥ 64 MB, itérations ≥ 3, parallélisme ≥ 4). Compromis : un déverrouillage plus lent (quelques secondes) mais beaucoup plus de résistance.

#### C. MFA, passkeys et clés physiques

#### 29.10 MFA : hiérarchie de sécurité

|MFA                                         |Sécurité                              |Recommandation              |
|--------------------------------------------|--------------------------------------|----------------------------|
|**SMS**                                     |Faible (SIM swap, MITM)               |À éviter                    |
|**Email**                                   |Faible (cascade si mail compromis)    |À éviter                    |
|**TOTP** (Authenticator, Aegis, Raivo)      |Bon                                   |Acceptable                  |
|**Push notification** (Microsoft, Duo)      |Bon, mais vulnérable à « MFA fatigue »|Acceptable                  |
|**FIDO2 / WebAuthn**                        |Excellent (résistant phishing)        |**Recommandé**              |
|**Clé matérielle FIDO2** (YubiKey, Nitrokey)|Excellent (hardware-bound)            |**Recommandé pour critique**|

#### 29.11 Passkeys

**Passkeys** sont l’implémentation grand public de WebAuthn. Une passkey est une paire de clés cryptographiques, stockée sur ton appareil (ou dans un trousseau cloud E2EE), qui s’authentifie auprès d’un service sans mot de passe.

Deux types :

- **Synchronisées** (via iCloud Keychain, Google Password Manager, Bitwarden, 1Password) : disponibles sur tous tes appareils, mais dépendantes du trousseau.
- **Device-bound** (sur clé physique FIDO2) : ne sortent jamais de la clé. Maximum de sécurité.

Adoption en 2025-2026 : Google, Apple, Microsoft, GitHub, Amazon, beaucoup d’autres supportent. Migration progressive.

#### 29.12 Clés physiques : YubiKey, Nitrokey, SoloKey

- **YubiKey 5 series** : référence commerciale. Multiples protocoles (FIDO2/WebAuthn, FIDO U2F, OTP, OpenPGP smartcard, PIV). Pas open source côté firmware. Différents form factors (USB-A, USB-C, NFC).
- **Nitrokey 3** : open source matériel et logiciel. Allemagne. Bon pour profil sensible/transparence.
- **SoloKey** : open source, plus militante. Adoption modeste.

**Stratégie à deux clés** : toujours avoir une clé principale et une clé de secours, enregistrées toutes deux sur tes comptes critiques. La principale au quotidien, la secondaire dans un coffre. La perte d’une clé est gérable si la seconde existe.

#### 29.13 Procédure en cas de compromission

Tu suspectes ton compte compromis :

1. **Changer immédiatement le mot de passe** depuis un appareil sain.
1. **Révoquer toutes les sessions actives**.
1. **Audit des modifications récentes** : email de récupération changé ? Filtre mail nouveau qui efface des notifications ? Méthodes MFA ajoutées par un tiers ?
1. **Vérifier les logs** (Google Account → Activité, Apple ID → Appareils, etc.).
1. **Si compromission confirmée du gestionnaire de mots de passe** : changer *tous* les mots de passe critiques, considérer le coffre comme exposé.
1. **Communication** : prévenir les contacts si phishing depuis ton compte ; déclarer aux plateformes ; déposer plainte si pertinent.

-----

### Chapitre 30 — Cloud, sauvegardes et chiffrement côté client

#### 30.1 Les trois états de la donnée

- **At rest** (au repos) : sur ton disque, sur un serveur cloud. Protégée par chiffrement disque/conteneur.
- **In transit** (en transit) : sur le réseau. Protégée par TLS/HTTPS.
- **In use** (en utilisation) : en RAM, déchiffrée, exploitable par un processus. Plus dur à protéger (TEE, enclaves matérielles).

Chaque état appelle des défenses différentes. Une chaîne complète doit traiter les trois.

#### 30.2 Cloud par défaut : ce que Google Drive, OneDrive, Dropbox, iCloud peuvent lire

Sans précaution :

- **Google Drive** : Google peut lire (clé contrôlée par Google).
- **OneDrive** : Microsoft peut lire.
- **Dropbox** : Dropbox peut lire.
- **iCloud Drive** : Apple peut lire (sauf ADP activé).

Tous ces fournisseurs chiffrent les données au repos sur leurs serveurs (protection physique des serveurs), mais ils détiennent les clés. Conséquences :

- Réquisition judiciaire = accès complet.
- Faille interne ou attaquant qui compromet le fournisseur = accès complet.
- Politique de scanning automatique (CSAM, malware) = traitement du contenu.

#### 30.3 Apple ADP : conditions et limites

Cf. Ch 14.6. Rappel : ADP active l’E2EE pour la majorité des données iCloud. Pas pour mail, contacts, calendrier.

**Conditions** : tous les appareils Apple à version récente, clé de récupération à conserver (perte = perte de données définitive).

**Pour qui** : tout utilisateur Apple avec données dans iCloud. À activer.

#### 30.4 Cloud E2EE par design : Proton Drive, Tresorit, Mega

- **Proton Drive** : Suisse, E2EE par design, intégré écosystème Proton. Capacité variable selon plan.
- **Tresorit** : Suisse, E2EE par design, focalisé pro et entreprise, audits réguliers. Plus cher.
- **Mega** : Nouvelle-Zélande, E2EE par design. Capacité gratuite généreuse, historique controversé (Kim Dotcom) mais sécurité côté client réputée correcte.

**Pour qui** : utilisateurs voulant E2EE par défaut sans setup technique. Choisir selon juridiction et budget.

#### 30.5 Chiffrement côté client par-dessus cloud généraliste

Tu veux garder Google Drive ou Dropbox pour des raisons d’écosystème, mais chiffrer ce que tu y mets ? Solutions :

- **Cryptomator** : conteneur de dossier transparent. Tu pointes Cryptomator vers un dossier dans Google Drive, il y crée une structure de fichiers chiffrés. Tu déverrouilles avec un mot de passe, ton OS voit un dossier monté. Multi-plateforme, open source, libre.
- **gocryptfs / EncFS** (Linux/macOS) : similaire, ligne de commande.
- **rclone + crypt backend** : pour scripts, sauvegardes automatisées vers cloud chiffré.

Tu peux utiliser le cloud que tu veux comme tu veux, et lui n’a plus accès au contenu. C’est l’option pragmatique pour beaucoup.

#### 30.6 Nextcloud self-hosted

**Nextcloud** est un cloud privé auto-hébergé. Tu installes sur un VPS ou serveur domestique, tu as Drive + Calendrier + Contacts + Mail + plus.

**Avantages** : contrôle total, juridiction de ton choix, fonctionnalités étendues.

**Limites** :

- L’E2EE Nextcloud officielle a un historique mitigé. Pour E2EE sérieuse, combiner avec Cryptomator au-dessus.
- Maintenance technique nécessaire (mises à jour, sauvegardes, monitoring).
- Bande passante limitée à ta connexion.

#### 30.7 Syncthing

**Syncthing** synchronise des dossiers entre appareils en peer-to-peer, sans cloud intermédiaire. Configuration sur chaque appareil, échange par identifiants. Chiffré bout-en-bout, open source.

Cas d’usage : sync notes entre laptop et téléphone sans aucun fournisseur tiers. Synchronisation continue.

#### 30.8 Sauvegarde : règle 3-2-1

- **3 copies** des données importantes.
- **2 supports** différents (disque local + cloud, ou disque interne + externe).
- **1 hors site** (hors de chez toi).

Pour profils exposés : **3-2-1-1-0** ajoute :

- **1 sauvegarde immuable** (write-once, hors atteinte ransomware).
- **0 erreur** : tests de restauration réguliers.

#### 30.9 Sauvegardes locales chiffrées

- **restic** : open source, déduplication, chiffrement par défaut. Backends multiples (local, S3, Backblaze B2, SFTP). Préférée pour script et automatisation.
- **Borg / BorgBackup** : similar à restic, déduplication efficace, communauté solide.
- **Time Machine** (macOS) + FileVault activé = sauvegarde chiffrée. Pratique pour utilisateurs Apple.
- **Windows Backup / File History** : moins puissant, OK pour basique.

#### 30.10 Photos : sync auto et fuites

La synchronisation auto des photos vers iCloud/Google Photos remonte tout, avec EXIF, à chaque déclenchement. Pour profils sensibles :

- Désactiver la synchronisation auto.
- Tri manuel avant upload.
- Effacement EXIF avant publication (Ch 31).
- Pour photos sensibles d’enquête : jamais dans le cloud personnel.

#### 30.11 Test de restauration

**La sauvegarde non testée n’existe pas**. Une fois par an au minimum : test de restauration complète sur appareil neuf. Sinon, tu découvres au moment critique que ton backup est corrompu, incomplet, ou inutilisable.

#### 30.12 Sauvegarde des secrets

Clés PGP, codes de récupération, clé de récupération ADP, codes 2FA backup : ne pas oublier de sauvegarder.

Options :

- **Coffre matériel** : YubiKey backup avec mêmes clés que la principale.
- **Papier + coffre physique** : impression des codes, dans une enveloppe scellée, en coffre à la banque ou chez un avocat.
- **Cryptomator + cloud** : conteneur avec tous tes secrets, sauvegardé dans plusieurs clouds.

#### 30.13 Plan en cas de perte ou vol

Préparé à l’avance :

1. **Effacement à distance** : Find My iPhone, Android Find My Device, Microsoft Find My Device.
1. **Révocation des sessions** sur tous les comptes.
1. **Désactivation des passkeys et certificats** liés à l’appareil.
1. **Notification de l’opérateur** pour bloquer la SIM si applicable.
1. **Déclaration de vol** (police, assureur).
1. **Restauration sur appareil neuf** depuis sauvegarde chiffrée.
1. **Audit** : changement préventif des mots de passe critiques si suspicion de compromission de l’appareil avant l’effacement.

-----

### Chapitre 31 — Métadonnées et nettoyage de fichiers

#### 31.1 Métadonnées : ce que c’est

Les métadonnées sont les données qui décrivent les données. Souvent invisibles, presque toujours révélatrices. Elles s’agrègent silencieusement à chaque création de fichier, à chaque modification, à chaque transmission. Plus dangereuses parce que sous-estimées.

#### 31.2 EXIF photo et métadonnées image étendues

Standard EXIF (Exchangeable Image File Format), embarqué dans la plupart des formats image (JPEG, TIFF, certains RAW) :

- **Coordonnées GPS** (latitude, longitude, altitude, parfois cap et vitesse au moment de la prise).
- **Date et heure** de prise, avec fuseau horaire.
- **Modèle d’appareil** et numéro de série de l’appareil (sur certains modèles haut de gamme, c’est un identifiant unique par appareil — un signal forensique fort).
- **Paramètres techniques** (ouverture, ISO, focale, exposition, balance des blancs).
- **Orientation** physique au moment de la prise (capteur gyroscopique).

**Métadonnées image étendues, souvent négligées** :

- **Profil ICC personnalisé** : si tu utilises un écran calibré ou un workflow professionnel, le profil ICC embarqué peut identifier ton matériel ou ton studio.
- **Vignettes** : mini-images embarquées dans la version finale. Si tu retouches une photo (par exemple pour caviarder un visage), la vignette peut conserver la version originale non retouchée. Plusieurs scandales journalistiques ont reposé sur cette erreur. ExifTool peut extraire les vignettes avec `exiftool -b -ThumbnailImage`.
- **XMP** (Extensible Metadata Platform) : couche métadonnées étendue, utilisée par Adobe et autres. Peut contenir auteur, copyright, historique de modifications, mots-clés ajoutés par le logiciel de gestion (Lightroom, Photo Mechanic).
- **Maker Notes** : zone propriétaire dans laquelle chaque constructeur (Canon, Nikon, Sony, Apple, Samsung) stocke des informations supplémentaires. Sur iPhone, Apple stocke des données HEIC qui incluent parfois l’orientation gyroscopique fine.
- **CRS (Camera Raw Settings)** : pour les fichiers RAW retouchés, peut révéler la version du logiciel utilisé.

**Cas réel** : John McAfee en 2012 — photo prise par un journaliste de *Vice* avec son iPhone, EXIF GPS intact, révèle au monde la localisation au Guatemala. Arrestation suivie dans les jours. Cf. Annexe 8.6.

**Cas moins connu** : plusieurs analystes d’OSINT ont géolocalisé des reportages de guerre en croisant l’angle du soleil dans la photo avec l’horodatage EXIF — sans même besoin du GPS, à condition que le téléphone n’ait pas modifié l’horloge.

#### 31.3 PDF

- **Auteur**, **Producteur** (logiciel), **Créateur** (logiciel d’export), **Mots-clés**, **Sujet**.
- **Historique de révisions** : versions précédentes embarquées si non purgées.
- **Objets cachés** : commentaires invisibles, annotations, formulaires masqués.
- **XMP** (Extensible Metadata Platform) : couche métadonnées additionnelle.
- **JavaScript embarqué** : si présent, exécutable à l’ouverture.

#### 31.4 Office (DOCX, XLSX, PPTX)

- **Auteur** initial et dernier modificateur.
- **Date de création**, dernière modification, dernière impression.
- **Commentaires** et suivi des modifications, parfois conservés sans en avoir conscience.
- **Texte caché** (formatage en blanc, sections masquées).
- **Vignettes** des slides PPTX.

Office propose un « Inspecter le document » qui retire la plupart, mais pas tout. Vérifier toujours après nettoyage.

#### 31.5 Audio / vidéo

- **Tags ID3** sur MP3 : artiste, album, paroles, image cover.
- **Métadonnées MP4/MOV** : géolocalisation pour vidéos téléphoniques, gyroscope, codecs.
- **Traces de montage** : marqueurs invisibles laissés par certains logiciels.
- **Gyroscope iPhone vidéo** : peut révéler modèle d’iPhone exact.

#### 31.6 Yellow dots : tracking imprimantes

**Cas Reality Winner, 2017** : analyste NSA, fuite d’un document classifié au média The Intercept. Le document est scanné et publié. Sur l’impression : des **micro-points jaunes** quasi invisibles à l’œil nu, formant un code dérivé de la **machine spécifique**, **date** et **heure** d’impression. Le FBI remonte à l’imprimante de la NSA, à l’heure d’impression, à Reality Winner. Arrestation en quelques jours.

**Mécanisme** : la quasi-totalité des imprimantes couleur professionnelles intègrent depuis les années 2000 un système de marquage forensique. Les patterns varient selon le constructeur, mais le principe est universel. Non documenté par les constructeurs, mais documenté par EFF (« Machine Identification Code »).

**Défense** :

- Pour publication anonyme : ne pas imprimer.
- Si impression nécessaire : imprimer dans des lieux multiples non identifiables, ou utiliser des imprimantes sans MIC (rares).
- Pour transmission de document scanné : ré-imprimer après scan via une voie qui retire les artefacts (re-générer le PDF depuis le contenu, jamais re-scanner).

#### 31.7 Outils de nettoyage

- **MAT2** : Metadata Anonymisation Toolkit v2 (Tails inclut). Multi-format, automatique. `mat2 fichier.jpg` nettoie en place.
- **ExifTool** : référence pour lire et écrire métadonnées. Plus puissant, plus complexe. `exiftool -all= fichier.jpg`.
- **« Inspecter le document »** (Word, PowerPoint, Excel) : intégré, bon mais incomplet.
- **Acrobat Pro « Suppression d’informations cachées »** : payant mais efficace sur PDF.

#### 31.8 Dangerzone

Cf. Ch 16. Méthode différente : reconversion complète du PDF dans un conteneur isolé, qui produit un PDF *nettoyé par reconstruction*. Plus radical que MAT2 (qui retire les métadonnées sur le fichier existant) parce qu’il *recrée* le fichier à partir de l’image rendue. Aucun objet caché, aucun JavaScript, aucune révision n’y survit.

#### 31.9 Zed!

Cf. Ch 12. Conteneur chiffré auto-extractible, secteur public francophone. Utile pour transmettre un dossier complet à un correspondant non technique en environnement français.

#### 31.10 Redaction destructive vs masquage

Pour caviarder un nom dans un PDF :

- **Mauvaise méthode** : rectangle noir par-dessus le texte dans Acrobat → le texte est toujours là, sous le rectangle. Copier-coller révèle.
- **Bonne méthode** : redaction destructive (Acrobat Pro propose, ou re-générer le PDF depuis source). Le texte est physiquement supprimé.

**Cas réel** : documents Manning publiés par Le Monde et The Guardian — premières versions avec caviardage non destructif, noms révélés par copier-coller. Correctifs et leçons apprises depuis.

#### 31.11 Workflow avant publication

1. Travailler dans un environnement isolé si document sensible.
1. Avant export final : passer par Dangerzone (PDF) ou MAT2 (autres formats).
1. Vérifier visuellement : ouvrir le résultat dans un visualiseur différent, examiner les métadonnées.
1. Tester copier-coller du contenu : ce qui ne devrait pas y être ne doit pas y être.
1. Vérifier les vignettes embarquées.
1. **Ne jamais publier directement depuis le logiciel de création**.

#### 31.12 *Fil rouge* — Léa nettoie un PDF et découvre un nom

Léa s’apprête à publier un document de l’enquête. Avant publication, application du workflow :

- Ouverture du PDF dans ExifTool : champ XMP « Author » contient le nom de la source. Erreur d’export.
- Vérification visuelle : tout est OK sur l’image.
- Vérification métadonnées : `exiftool -all` → champ « Producer » indique « Microsoft Word 2019 - Bureau de [nom de la source dans son administration] ». Si publié, identifie la source.
- Action : reconstruction via Dangerzone, vérification, publication.

Sans cette étape, la source aurait pu être identifiée par n’importe quel lecteur attentif.

-----

### Chapitre 32 — Paiements, traçabilité financière et cryptomonnaies

> **Cadre éditorial préalable** : ce chapitre est strictement éducatif et défensif. Il ne couvre pas le blanchiment, l’évasion fiscale, le contournement KYC ou la dissimulation d’origine illicite. Il aide à comprendre la traçabilité financière pour mieux protéger sa vie privée légitime, exercer sa liberté d’expression journalistique, ou se prémunir contre un harceleur exploitant tes traces de paiement.

#### 32.1 Pourquoi le paiement est une fuite massive

Chaque transaction révèle :

- L’achat (objet, montant, lieu, heure).
- Le compte source (ton identité bancaire).
- Le compte destinataire (commerce, identité).
- Le contexte (carte fidélité ?, code postal, IP en ligne).

Agrégés, les paiements dessinent ta vie : où tu vis, où tu travailles, ce que tu manges, qui tu fréquentes, quelles consultations médicales tu as, quelles opinions tu soutiens (dons), quels médias tu consommes.

Les **banques** voient tout. Les **réseaux de paiement** (Visa, Mastercard) voient tout. Les **agrégateurs** (Plaid, Tink) si tu utilises des apps bancaires tierces voient tout. Les **commerçants** voient leurs achats, certains revendent.

#### 32.2 Cartes et virements SEPA

CB classique : tracée intégralement, votre banque conserve l’historique.
Virement SEPA : motif transmis, libre. Traçabilité complète.
Prélèvement automatique : récurrence de fait, signal de relation contractuelle.

#### 32.3 Cartes virtuelles

- **Revolut, N26, Lydia, Boursorama** : cartes virtuelles à usage unique ou jetables.
- **Privacy.com** (US) : cartes virtuelles à plafond, expirables.
- **Apple Card / Apple Pay** : tokenisation (le commerçant ne voit pas ton vrai numéro).

**Avantages** : limite la traçabilité commerciale, isole les fuites en cas de compromission du commerçant.
**Limites** : le fournisseur de la carte (Revolut, etc.) voit tout. Tu déplaces la confiance, tu ne l’élimines pas.

#### 32.4 Cartes prépayées et cash en France/UE

L’achat anonyme de cartes prépayées avec montants substantiels n’est plus possible en UE depuis l’AMLD5 (2020) : KYC obligatoire au-delà de 150 € en physique, 50 € en ligne. AMLD6 a renforcé.

**Cash** : retrouve une valeur stratégique pour des achats que tu ne veux pas tracés. Limites légales : en France, les paiements professionnels > 1000 € sont interdits en cash ; entre particuliers, pas de limite spécifique mais déclaration au-delà de 10 000 €.

#### 32.5 Cryptomonnaies : Bitcoin et Ethereum sont traçables

**Mythe à déconstruire** : Bitcoin et Ethereum ne sont **PAS** anonymes. Ils sont **pseudonymes**. Toutes les transactions sont publiques sur la blockchain. La société d’analyse Chainalysis et autres construisent des graphes complets liant adresses à identités via :

- Exchanges KYC-ed.
- Heuristiques d’analyse (multi-input, change address).
- Recoupement avec adresses connues.

**Cas réels** : nombreux ; les autorités américaines tracent quasi quotidiennement des transactions Bitcoin de criminalité.

#### 32.6 Monero et Zcash

**Monero (XMR)** : confidentialité par défaut via ring signatures, stealth addresses, RingCT. Les transactions ne révèlent ni montant, ni expéditeur, ni destinataire. État actuel : pas d’analyse de chaîne efficace publiée à grande échelle (état de l’art 2025).

**Zcash (ZEC)** : confidentialité opt-in via zk-SNARKs (shielded addresses). Si tu utilises les shielded pools, confidentialité forte. Si tu utilises les transparent addresses, traçable comme Bitcoin.

**Limites réglementaires** :

- **MiCA** (Markets in Crypto-Assets) UE entré en vigueur 2024-2025 : transactions impliquant cryptomonnaies privacy-focused (Monero, Zcash shielded) seront plus restreintes sur exchanges régulés.
- **Travel Rule** : exchanges doivent partager certaines infos de bénéficiaires au-delà de seuils.
- **Delistings** : Monero retiré de Binance pour la plupart des marchés en 2024.

#### 32.7 Cadre réglementaire 2025-2026

- **France** : déclaration de comptes crypto à l’étranger (formulaire 3916), imposition des plus-values, KYC sur exchanges français.
- **UE (MiCA)** : régulation harmonisée.
- **Sanctions** : adresses sanctionnées (OFAC US) inutilisables sur exchanges régulés.

#### 32.8 La ligne rouge

Ce cours ne couvre **pas** :

- Le blanchiment d’argent.
- L’évasion fiscale.
- Le contournement délibéré de la procédure KYC.
- L’usage de cryptomonnaies pour dissimuler des activités illicites.

Tout cela est pénalement répréhensible.

Ce que ce cours couvre :

- Comprendre que tes paiements sont des données personnelles.
- Utiliser des moyens légaux pour limiter ta surface d’exposition financière commerciale (cash, cartes virtuelles, alias).
- Comprendre le cadre des cryptomonnaies pour des cas légitimes (don anonyme à un journaliste, soutien à une ONG dans un pays répressif, paiement d’un VPN par Monero parce que tu ne veux pas que ton VPN sache qui tu es).

#### 32.9 Achats sensibles légitimes

Cas où limiter la traçabilité est légitime :

- **Santé** : consultations sensibles (IVG, addiction, santé mentale, IST).
- **Journalisme** : matériel pour mission, frais d’enquête.
- **Sécurité personnelle** : abonnement VPN, achat de matériel sécurité pour victime de violences.
- **Engagement politique** : adhésion partis, dons associatifs (les listes peuvent être indirectement révélées).
- **Recherche** : achat de livres, accès à bases qui révèlent un intérêt sensible.

#### 32.10 Don anonyme à un journaliste / ONG

Plusieurs modèles légaux :

- **Cash en personne** : ancien et toujours fonctionnel.
- **Cash par courrier** : Mullvad VPN accepte (par exemple). Pour ONG, certaines aussi.
- **Cryptomonnaies** : Bitcoin avec wallet créé spécifiquement, jamais lié à exchange KYC. Monero pour confidentialité par défaut.
- **Intermédiaires** : certaines structures permettent dons anonymisés (fondations).

#### 32.11 Paiement d’un VPN : le cas Mullvad, NymVPN et AmneziaVPN

Le paiement d’un VPN est une fuite OPSEC souvent ignorée. Si un utilisateur paie son VPN avec sa carte bancaire nominative, le fournisseur VPN ou son prestataire de paiement peut relier l’achat à une identité civile, même si le trafic réseau n’est pas journalisé.

**Mullvad VPN** est particulièrement intéressant sur ce point : le service utilise des comptes numérotés sans email et accepte le paiement en cash par courrier ainsi qu’en Monero. C’est l’une des approches les plus cohérentes pour réduire le lien entre identité civile, paiement et usage du VPN.

**NymVPN** met en avant une logique de paiement unlinkable via mécanismes zero-knowledge et accepte plusieurs cryptomonnaies. C’est cohérent avec son objectif général : réduire non seulement l’exposition IP, mais aussi les liens entre paiement, compte et usage réseau.

**AmneziaVPN** dépend du mode d’usage. Avec Amnezia Premium, l’utilisateur reste dans un modèle de fournisseur VPN classique. Avec Amnezia self-hosted, le paiement du VPN disparaît en partie, mais il est remplacé par le paiement du VPS. La fuite OPSEC peut donc simplement se déplacer vers l’hébergeur du serveur.

**Règle pratique** : pour un VPN privacy, le paiement doit être pensé comme une métadonnée sensible. Un VPN payé par carte bancaire nominative reste utile contre le FAI, mais il n’offre pas la même séparation qu’un compte payé en cash ou via une méthode mieux compartimentée.

-----

> 🟦 **Capstone 3 — Auditer et durcir une chaîne source-journaliste**
> 
> **Scénario** : Tu es journaliste. Une source potentielle veut entrer en contact pour transmettre des documents sensibles concernant un dossier de corruption. Tu n’as jamais communiqué avec elle. Comment structures-tu la chaîne complète, de la prise de contact à l’archivage des documents, en mobilisant les chapitres précédents ?
> 
> **Procédure attendue** :
> 
> 1. **Avant tout contact** : avoir un canal public annonçant comment te joindre confidentiellement (Ch 28). Publié sur ton site, redirigé depuis tes profils.
> 1. **Premier contact** : la source utilise ton canal annoncé. Idéal : SimpleX (numéros invisibles) ou SecureDrop si tu en as un. Mauvais : ton email professionnel public.
> 1. **Vérification d’identité** : avant de continuer, vérification mutuelle. Toi : preuve que tu es bien la journaliste annoncée (clé PGP signée, présence publique cohérente). La source : tu ne peux pas vérifier qu’elle est qui elle dit, mais tu peux évaluer la plausibilité (cohérence du récit, accès à des éléments non publics, recoupements).
> 1. **Canal stable** : après prise de contact, établir un canal pérenne. Signal avec usernames ou SimpleX. Vérifier les Safety Numbers en personne ou par canal hors bande (vocal — la voix est difficile à falsifier face à un humain qui la connaît, sauf deepfake).
> 1. **Compartimentation** : appareil dédié pour cette enquête (Ch 9, Ch 15). Pas ton téléphone perso. GrapheneOS sur Pixel ou iPhone séparé.
> 1. **Reception des documents** : via OnionShare ou via le canal Signal lui-même. Téléchargement dans environnement isolé (Tails ou dispVM Qubes).
> 1. **Vérification d’intégrité** : hash SHA-256 confirmé par la source hors bande.
> 1. **Sas de purification** : passage par Dangerzone pour les PDF. Nettoyage des métadonnées avec MAT2 ou ExifTool sur les autres formats.
> 1. **Archivage chiffré** : conteneur VeraCrypt ou Cryptomator sur disque externe. Stocké physiquement en coffre ou lieu sûr. Sauvegarde redondante dans cloud E2EE (Proton Drive).
> 1. **Audit avant publication** : nouveau passage MAT2 / ExifTool / Dangerzone sur tout document destiné à publication. Le caviardage est destructif. Vérification finale en environnement isolé.
> 1. **Communication post-publication** : préparation d’un canal pour suite (la source peut avoir besoin de soutien juridique, de mise à l’abri ; cf. lanceurs d’alerte Ch 37).
> 
> **Léa et Karim, fil rouge** : application complète de cette procédure sur trois mois. Karim transmet par paquets successifs. Chaque paquet suit le workflow. Trois mois après le premier contact, l’enquête est solidifiée, prête à publication. Cf. cas A en fin de cours.

-----

## Partie 7 — OPSEC humaine, opérationnelle et continuité

> **Objectif** : ce qui reste quand la technique est en place. Les attaques modernes contournent rarement la crypto — elles contournent l’humain, les routines, les frontières, les chaînes d’approvisionnement, les angles morts juridiques. Cette partie traite ce que les outils ne couvrent pas.

-----

### Chapitre 33 — Social engineering, phishing ciblé et spyware mercenaire

> **Niveau de posture (cf. Ch 2.6)** : la vigilance phishing concerne **tous les niveaux** (le phishing est l’attaque la plus statistiquement probable, indépendamment du profil). Lockdown Mode iOS, GrapheneOS et reboot quotidien relèvent du **Niveau 2** quand un indicateur de ciblage existe (publication sensible, contexte politique, threat notification reçue). MVT et iVerify systématiques, audit forensique périodique, plan de réponse spyware = **Niveau 3** réservé aux cibles documentées (journalistes investigation actuelle, opposants politiques, défenseurs droits humains exposés).

> **Note critique** : ne pas se dimensionner au Niveau 3 par fascination ou anxiété. Recevoir une vraie *Threat Notification* d’Apple, Google ou Meta est rare et conservateur. Les notifications de ce type sont envoyées à des cibles confirmées. Si tu n’en as jamais reçu et que ton profil ne correspond pas aux cibles documentées par Citizen Lab et Amnesty Security Lab, ton temps est mieux investi sur N1 et N2.

#### 33.1 Pourquoi l’humain reste le maillon faible

La cryptographie moderne tient. Les protocoles aussi. Ce qui se casse, c’est l’humain : il clique sur le lien, il fait confiance à la voix au téléphone, il branche la clé USB trouvée au sol, il déverrouille son téléphone parce qu’il a peur de manquer un appel important. Les attaquants sérieux investissent dans l’ingénierie sociale parce qu’elle est *plus rentable* que les exploits techniques.

#### 33.2 Phishing : taxonomie

- **Phishing de masse** : email générique envoyé à des millions. Faible taux de succès individuel mais volume.
- **Spear phishing** : message ciblé, personnalisé avec OSINT préalable (nom du destinataire, contexte professionnel, vocabulaire interne). Beaucoup plus efficace.
- **Whaling** : spear phishing visant un cadre supérieur ou une personne haut placée. Effets de levier importants (autorisation de virement, ouverture d’accès).
- **Smishing** : phishing par SMS. En croissance avec faux livreurs, fausses banques, faux opérateurs.
- **Vishing** : phishing vocal. Le téléphone légitime l’autorité ressentie.
- **Quishing** : phishing par QR code. Affichage en lieu public d’un QR qui pointe vers site malveillant.

#### 33.3 BEC : Business Email Compromise

Variante professionnelle. Un attaquant compromet (ou usurpe) le compte d’un dirigeant. Envoie au comptable une demande de virement urgent, plausible, semblant venir du DG. Le comptable exécute. Pertes annuelles mondiales : milliards.

Mitigation : procédures internes exigent confirmation par canal séparé (téléphone interne, en personne) pour tout virement au-dessus d’un seuil. Formation systématique. Vérification des en-têtes email (SPF, DKIM, DMARC).

#### 33.4 Reconnaissance préalable et OSINT offensif

Avant un spear phishing sérieux, l’attaquant a typiquement passé heures voire jours sur ta présence publique : LinkedIn, X, articles, slides de conférences, contributions GitHub, mentions dans la presse. Il connaît tes collègues, ton vocabulaire, tes projets en cours.

Conséquence : ta réduction d’empreinte publique (Ch 5-8) est *aussi* une mesure anti-phishing structurelle.

#### 33.5 Indicateurs et détection

À l’œil :

- **Domaine légèrement modifié** : `proton-mail.com` au lieu de `proton.me`, `microsoft0nline.com` au lieu de `microsoft.com`. Survoler les liens, lire l’URL réelle.
- **Sense d’urgence artificielle** : « action immédiate requise », « votre compte sera suspendu dans 24h ».
- **Émotion stimulée** : peur (« sécurité compromise »), curiosité (« document confidentiel pour vous »), cupidité (« vous avez gagné »), serviabilité (« j’ai besoin d’aide »).
- **Demande inhabituelle** : action que tu ne ferais normalement pas dans ce contexte.
- **Discordance signal/canal** : ton patron ne t’envoie jamais des emails à 22h pour des virements urgents.

Au-delà :

- **Vérification du sender** : analyser les en-têtes complets (Received, Authentication-Results).
- **Vérification du domaine** : `whois` du domaine, ancienneté (un domaine créé hier est suspect).
- **Bac à sable** pour pièces jointes (Ch 16).

#### 33.6 Spyware mercenaire : Pegasus, Predator, Graphite

**Pegasus (NSO Group)** : spyware iOS/Android le plus documenté. Capacités révélées par Citizen Lab, Amnesty Security Lab : exfiltration complète (messages, photos, contacts, localisation), activation du micro et de la caméra, contournement du chiffrement E2EE (lecture après déchiffrement local).

Vecteurs documentés :

- **Zero-click iMessage** (FORCEDENTRY, 2021) : exploit envoyé en iMessage qui s’exécute sans interaction. Patch Apple ultérieur.
- **Zero-click WhatsApp** (2019) : appel WhatsApp qui infecte même sans décrocher.
- **One-click via lien** : SMS contenant un lien qui exploite WebKit.
- **Réseau** : injection via opérateur cellulaire compromis.

**Predator (Intellexa / Cytrox)** : concurrent grec, capacités similaires, déploiement documenté en Grèce, Égypte, Vietnam, Madagascar, Soudan.

**Graphite (Paragon Solutions)** : plus récent (2024-2025), capacités équivalentes, déploiement contesté (révélations Citizen Lab fin 2024, WhatsApp a notifié des journalistes et activistes en janvier 2025).

**QuaDream, Candiru** : autres acteurs, plus en retrait.

**Cibles documentées 2020-2025** : journalistes (dont Jamal Khashoggi avant son assassinat — un des proches était sous Pegasus), activistes (Forbidden Stories Pegasus Project), avocats, opposants politiques, proches de cibles. Cas confirmés sur 6 continents.

#### 33.7 Lockdown Mode, GrapheneOS, durcissement

**Lockdown Mode iOS** (cf. Ch 15) désactive des fonctionnalités spécifiquement exploitées par les spyware mercenaires. Études de cas Citizen Lab montrent qu’il aurait bloqué plusieurs exploits documentés. Pour HVT : activation systématique.

**GrapheneOS** : durcissement kernel, sandboxing renforcé, attestation. N’élimine pas le risque mais relève la barre.

**Reboot quotidien** : la plupart des spyware modernes ne persistent pas au redémarrage. Cinq secondes par jour de discipline = grandes leçons d’élévation du coût pour l’attaquant.

#### 33.8 Détection : MVT, iVerify, notifications plateformes

- **MVT (Mobile Verification Toolkit)** : développé et maintenu par *Amnesty Security Lab*, open source (https://github.com/mvt-project/mvt). Analyse les sauvegardes iPhone (iTunes/iCloud-style local backups, *pas* iCloud chiffré) et les *full filesystem dumps* Android pour détecter des indicateurs de compromission (IOCs) Pegasus, Predator, Graphite, QuaDream et d’autres familles documentées. Plus efficace en post-mortem (sur un appareil suspecté) qu’en temps réel. Les IOCs sont publiés et mis à jour par Amnesty et Citizen Lab à mesure de leurs investigations.
  
  *Limites* : MVT détecte les IOCs *connus*. Une variante neuve d’un spyware mercenaire peut ne pas être détectée. L’absence de détection ne prouve pas l’absence d’infection. C’est néanmoins un outil de référence — la majorité des cas Pegasus publiquement confirmés l’ont été après analyse MVT par Amnesty ou Citizen Lab.
  
  *Workflow typique* : sauvegarde locale iTunes du iPhone (cryptée, mais MVT peut traiter), import dans MVT, scan automatique contre les IOCs, génération d’un rapport. Pour Android, plus complexe (full image dump requis, possibilité de root requis).
- **iVerify** : outil commercial développé par *Trail of Bits* puis par une équipe dédiée. Application iOS / Android. Heuristiques pour détecter spywares connus, audit de la posture de sécurité de l’appareil (versions à jour, Lockdown Mode actif, services à risque), alertes en cas d’anomalie. Pratique au quotidien pour profils HVT — c’est un complément de MVT, pas un substitut. Modèle freemium, plans pro pour journalistes/ONG accessibles via partenariats avec Access Now.
- **Notifications plateformes** :
  - **Apple Threat Notifications** envoyées depuis 2021. Le wording standard est « Apple a détecté que vous êtes potentiellement la cible d’une attaque parrainée par un État ». Apple ne précise pas le vecteur, mais publie les critères généraux. Ces notifications sont conservatrices — Apple privilégie d’alerter à risque légèrement avéré plutôt que tarder à le faire.
  - **Google Threat Analysis Group (TAG)** envoie des notifications équivalentes sur Gmail et Workspace pour ciblage par acteurs étatiques.
  - **Meta** alerte via WhatsApp dans les cas de zero-click exploit (cas Paragon Graphite, janvier 2025 : ~90 utilisateurs notifiés dans plusieurs pays dont l’Italie).
  - **Si tu reçois une telle notification** : prends-la au sérieux. C’est rare. Ces notifications sont quasi systématiquement validées par des éléments concrets côté plateforme. Application immédiate de la procédure 33.9.

#### 33.9 Procédure post-compromission suspectée

1. **Isolation** : passer l’appareil en mode avion (vrai mode avion, vérifié). Faraday bag si disponible.
1. **Ne pas redémarrer** (perdrait des artefacts forensiques) — sauf si tu n’as pas accès à un analyste forensique.
1. **Contact d’experts** : Access Now Digital Security Helpline (gratuit pour HVT), Citizen Lab, Amnesty Security Lab.
1. **Sauvegarde** pour analyse (`idevicebackup2` ou Quicktime pour iOS sans iCloud).
1. **En attendant analyse** : appareil neuf, comptes audités, mots de passe critiques renouvelés, contacts prévenus.
1. **Long terme** : changement de modèle de menace, formation, montée en posture.

#### 33.10 *Fil rouge* — Anya reçoit une notification Apple

Anya V. reçoit un mail d’Apple Threat Notification : « Apple détecte que vous êtes potentiellement la cible d’une attaque par un attaquant parrainé par un État ». Elle :

1. Met immédiatement son iPhone en mode avion, le glisse dans une pochette Faraday.
1. Contacte la Digital Security Helpline d’Access Now.
1. Avec leur aide, fait une sauvegarde via Mac, soumet à analyse Citizen Lab.
1. Diagnostic : présence d’IOC Predator. Confirmation après 10 jours.
1. Change tous ses comptes critiques depuis appareils propres. Bascule définitivement sur GrapheneOS. Communique publiquement, ce qui est sa stratégie : la publicité protège.

-----

### Chapitre 34 — IA générative, LLM, deepfakes et privacy

#### 34.1 Quatre vagues qui changent le paysage

L’IA générative 2023-2026 a modifié quatre vecteurs :

- **Création de contenu falsifié** plausible (texte, image, vidéo, voix) à coût marginal nul.
- **Capacité d’attaque automatisée** (phishing personnalisé à grande échelle, génération de pretext crédibles).
- **Aspiration de données** : modèles entraînés sur du contenu massif incluant des données personnelles.
- **Intégration dans les appareils** (Apple Intelligence, Gemini sur Android, Copilot dans Windows) : nouvelles surfaces d’exposition.

#### 34.2 LLM cloud : ce que ton fournisseur voit

Quand tu utilises ChatGPT, Claude, Gemini, Mistral Le Chat depuis le navigateur ou l’app, tu envoies tes prompts à leurs serveurs. Conséquences :

- **Stockage** : par défaut, les conversations sont stockées et utilisables pour amélioration des modèles.
- **Logs** : disponibles à l’opérateur, accessibles sur réquisition légale.
- **Pas d’E2EE** : du contenu en clair entre toi et le fournisseur.
- **Sensitivity** : un prompt révèle ton sujet d’intérêt, ton vocabulaire, ton style, ton contexte professionnel.

**Comportements à éviter** : envoyer à un LLM cloud des informations personnelles identifiantes sensibles (numéros, noms de sources, contenus internes confidentiels, dossiers médicaux).

#### 34.3 Modes « privacy » des fournisseurs

Plusieurs fournisseurs proposent des options :

- **ChatGPT « Temporary Chat »** : pas de stockage long terme. À activer manuellement.
- **Claude.ai** : politique de non-entraînement sur conversations consumer par défaut depuis 2024-2025.
- **API mode** vs **interface chat** : l’API offre généralement de meilleures garanties contractuelles (pas d’entraînement, rétention configurable). Pour usage pro sérieux.
- **Plans entreprise** : politiques de rétention contrôlées contractuellement.

Lire la politique du fournisseur à jour est indispensable, les choses bougent vite.

#### 34.4 LLM locaux : Ollama, LM Studio, llama.cpp

L’alternative privacy : faire tourner un LLM **sur ta machine**. Le prompt ne quitte jamais ton appareil.

- **Ollama** : runner simple pour modèles ouverts (Llama, Mistral, Qwen, etc.). Installation en quelques commandes, modèles téléchargés localement.
- **LM Studio** : interface graphique, profil grand public.
- **llama.cpp** : moteur d’inférence efficace, base de plusieurs solutions.

**Performance** : sur Mac M-series ou laptop avec GPU récent, modèles 7-13B donnent qualité utilisable. Modèles 70B exigent matériel sérieux mais possibles. Qualité légèrement inférieure aux frontières (GPT-4, Claude 4, Gemini 2.5) mais en progression rapide.

**Pour qui** : profils qui traitent des informations confidentielles et veulent rester maîtres. Excellent pour analyse de documents sensibles, brainstorming privé, drafting de notes confidentielles.

#### 34.5 Connecteurs IA (MCP, plug-ins, agents)

L’année 2024-2025 a vu se généraliser les **connecteurs** entre LLM et données utilisateur : MCP (Model Context Protocol), plug-ins, agents qui lisent ton calendrier, tes emails, tes documents.

**Risques** :

- **Élargissement de surface** : l’agent peut accéder à tes données plus largement que tu ne le réalises.
- **Prompt injection** : un document piégé peut faire faire des actions à un agent (exfiltration, modifications, envoi de messages). Vecteur d’attaque actif documenté en 2024-2025.
- **Persistance** : agent qui s’authentifie une fois et tourne en arrière-plan.
- **Données exposées au fournisseur LLM** : tout ce que l’agent lit, le LLM l’a vu.

**Pratique défensive** :

- Privilégier connecteurs avec accès *en lecture* uniquement quand possible.
- Limiter la portée (scope minimal sur OAuth).
- Audit régulier des autorisations.
- Pour profil sensible : pas de connecteur sur comptes critiques.

#### 34.6 Apple Intelligence, Microsoft Copilot, Gemini sur Android

Intégrations IA system-level. Spécificités :

- **Apple Intelligence** : revendique « Private Cloud Compute » avec architecture attestable. Pour requêtes locales (Siri reformulation, etc.) : on-device. Pour requêtes complexes : Apple Cloud Compute en E2EE attestable. Garanties techniques sérieuses mais auditabilité limitée pour utilisateur externe.
- **Microsoft Copilot dans Windows et Recall** : Recall est annoncée comme une fonctionnalité réservée aux **Copilot+ PCs** (matériel récent intégrant un NPU dédié), **opt-in** au niveau de l’utilisateur (la fonctionnalité n’est pas activée par défaut depuis le re-lancement), avec snapshots stockés localement et index présentés par Microsoft comme chiffrés et liés au Secure Enclave de la machine. La fonctionnalité avait été initialement déployée sans ces garanties en 2024, ce qui avait suscité une vague de critiques de chercheurs en sécurité ; Microsoft a suspendu puis re-lancé Recall fin 2024 avec ces protections additionnelles. Les critiques de fond persistent : capture régulière de l’écran indexée par IA crée par construction une base d’informations sensibles, dont la sécurité repose entièrement sur la robustesse de la TEE locale et l’absence d’exploitation de la machine. Pour profils sensibles : laisser Recall désactivé.
- **Gemini sur Android** : intégration profonde aux services Google, transmission cloud par défaut.

**Pour profils sensibles** : désactiver autant que possible les fonctionnalités IA système qui transmettent du contenu hors appareil.

#### 34.7 Aspiration de données par entraînement

Les modèles LLM ont été entraînés sur des corpus massifs incluant du contenu public (web crawl) et parfois privé (litiges en cours sur sources illégales). Conséquence : il existe des cas documentés où des modèles **regurgitent** verbatim du contenu d’entraînement, y compris des données personnelles.

**Mitigation côté utilisateur** :

- Limiter ta présence publique (Ch 5-8) limite ce qui peut être ingéré.
- Demandes d’opt-out auprès des fournisseurs (parfois disponibles, parfois théoriques).
- Surveiller les outputs sur ton propre nom dans les LLM publics.

#### 34.8 Robots.txt, ai.txt, droit à l’opposition au scraping

Pour qui produit du contenu en ligne et veut limiter son ingestion :

- **robots.txt** : standard historique, respecté par Google et Bing, ignoré par certains crawlers d’entraînement.
- **ai.txt** : standard émergent 2024-2025, plus spécifique pour exclure entraînement IA.
- **Méta-tags HTML** : `<meta name="robots" content="noai, noimageai">` (efficacité variable).
- **Cloudflare AI bot blocking** : depuis 2024, option dans Cloudflare pour bloquer les bots IA identifiés.
- **Cadre légal** : le RGPD (art. 21) permet l’opposition au traitement, applicable au scraping pour entraînement selon une lecture progressivement reconnue. La directive sur le droit d’auteur de 2019 (art. 4) prévoit le « opt-out » pour le data mining commercial.

#### 34.9 Deepfakes vidéo : état 2025-2026

La qualité des deepfakes vidéo a passé en 2024-2025 le seuil de plausibilité pour observateur non averti. Outils : Sora (OpenAI), Veo (Google), Gen-3 (Runway), HeyGen, D-ID, plus une cohorte open source.

Cas documentés :

- Faux Zelensky annonçant capitulation (2022, peu convaincant à l’époque).
- Faux Macron en mai 2024 (deepfake politique en période électorale).
- Sextorsion par deepfake en croissance, particulièrement contre femmes (cf. Sensity, Cyber Civil Rights Initiative).
- Faux call vidéo CFO Arup, Hong Kong, début 2024 : virement de 25 M$ après deepfake convaincant en réunion vidéo.

#### 34.10 Deepfakes audio : voice cloning

Encore plus mature que la vidéo. Outils : ElevenLabs, Resemble AI, plus solutions open source. **Trois secondes** d’enregistrement de voix suffisent pour cloner avec qualité plausible.

Cas en croissance :

- Faux appels « ton enfant a un accident, envoie de l’argent » utilisant la voix clonée.
- Faux PDG demandant virement urgent.
- Phishing vocal personnalisé.

#### 34.11 Biométrie vocale et auth téléphonique

Implication : la sécurité par « reconnaissance de la voix » au téléphone (utilisée par certaines banques, services administratifs, parfois Apple ID via Siri) est devenue **structurellement faible**. Les institutions qui en dépendent migrent ou doivent.

**Pour toi** : si une institution te propose auth vocale comme seule MFA, refuser. Demander alternative.

#### 34.12 Procédures anti-deepfake en réunion

Pour réunions sensibles à distance :

- **Codes hors bande** : convenir d’un mot de passe convenu en personne, à prononcer en début de visio pour authentifier.
- **Vidéo conférencière** : un deepfake en temps réel est aujourd’hui difficile à maintenir sous gestures complexes ; demander à la personne de poser une main de manière inattendue, tourner la tête vivement, montrer une pièce d’identité — peut révéler artefacts.
- **Rappel sur canal vérifié** : si doute, raccrocher et rappeler sur le numéro connu.

#### 34.13 Détection de deepfake : état de l’art

Outils en croissance, fiabilité partielle :

- **Sensity AI, Reality Defender, Truepic** : commerciaux, focalisés enterprise.
- **Académiques** : suite d’outils universitaires (FaceForensics++, DFDC).
- **Limites** : course à l’armement permanente entre génération et détection. Pas de garantie.

**Stratégie défensive** : ne pas dépendre uniquement de détection ; combiner avec vérification hors bande systématique.

#### 34.14 Watermarking : C2PA, SynthID

- **C2PA (Coalition for Content Provenance and Authenticity)** : standard de provenance cryptographique d’images, vidéos, documents. Adobe, Microsoft, Sony, BBC. Embarque dans le fichier l’historique de capture/modifications, signé. Pour authentifier l’origine d’un contenu.
- **SynthID** (Google DeepMind) : watermark invisible dans contenus générés par IA Google. Détectable par outils dédiés.
- **Limites** : volontaire, supprimable, partiellement déployé. Utile mais pas suffisant.

#### 34.15 IA dans la pile attaquant

Du côté offensif :

- **Phishing personnalisé** : un LLM rédige des emails sur mesure à partir d’OSINT préalable. Qualité linguistique, registre, vocabulaire — quasi parfaits.
- **Vocal phishing** : voice cloning + LLM = conversation crédible.
- **Reconnaissance** : LLM analyse vastes corpus de données fuitées pour identifier patterns exploitables.
- **Génération de pretext** : LLM produit scénarios de social engineering convaincants.

**Conséquence** : la qualité moyenne des attaques augmente. Les indicateurs traditionnels (fautes, formulation maladroite) sont moins fiables. Le filtrage se déplace vers le **comportement** et le **canal** plutôt que le contenu.

#### 34.16 IA dans la pile défenseur

Du côté défensif :

- **Détection d’anomalies** : LLM dans EDR pour analyse comportementale.
- **Triage automatique** : assistance pour analystes SOC.
- **Génération de leurres** (honeypots intelligents).
- **Aide à la rédaction de procédures, formation, sensibilisation**.

L’asymétrie en 2026 : l’IA aide les deux camps à l’avantage de l’attaquant *à court terme* (l’attaque scale plus facilement que la défense), mais à l’avantage du défenseur à moyen terme si déploiement systématique.

#### 34.17 Cadre éthique : usage de l’IA dans son propre travail

Ce cours postule un usage IA éthique : compréhension, rédaction, analyse, formation. Pas de génération de contenu trompeur, pas d’impersonation, pas d’utilisation pour harceler. Le droit (loi française de 2024 sur deepfakes, AI Act UE) sanctionne désormais explicitement plusieurs usages malveillants.

#### 34.18 *Fil rouge* — Léa face à un deepfake de sa source

Trois mois après sa première rencontre avec Karim, Léa reçoit un appel vidéo Signal. Voix et image de Karim, ton paniqué : « Léa, j’ai besoin que tu rendes les documents, ils savent, c’est dangereux pour ma famille. » Léa ressent le malaise — le ton n’est pas tout à fait celui de Karim. Elle applique le protocole pré-convenu : « Karim, peux-tu me redire le proverbe qu’on a échangé la première fois ? ». Silence côté appel, puis raccrochage. Léa contacte ensuite Karim sur leur canal SimpleX par texte : Karim répond, c’est bien lui, et il n’a pas appelé. Tentative de deepfake confirmée. Bascule en alerte, audit complet des canaux, vérification que la stack tient toujours.

-----

### Chapitre 35 — OPSEC humaine : entourage, photos, voix, stylométrie, traces comportementales

#### 35.1 Entourage : maillon souvent ignoré

Ton meilleur OPSEC tombe si ton entourage publie ton anniversaire le jour, te tague sur une photo géolocalisée, ou répond à un appel de pretext en donnant ton emploi du temps.

**Mesures** :

- **Conversation explicite** avec les proches importants : pas de tag, pas de mention par nom, pas de photo en ligne sans accord, pas de réponse à des questions sur toi sans vérification.
- **Documents partagés** : ne pas mettre tes infos perso dans les listes Excel familiales partagées sur Google Sheets.
- **Réseaux familiaux** : ta mère a publié ton adresse sur Facebook ? Discussion privée, sans drame, avec aide à modifier les paramètres.
- **Enfants** : pas de prénom + école visible publiquement. Pas de photo géolocalisée.

#### 35.2 Photos : géolocalisation visuelle

Au-delà de l’EXIF (Ch 31), une photo révèle par son contenu visuel :

- Vue par la fenêtre permettant de trianguler le quartier.
- Arrière-plan industriel ou architectural identifiable.
- Plaques d’immatriculation visibles.
- Marquages d’entreprise locale.
- Reflets sur surfaces brillantes (vitre, miroir, écran, œil).

**OSINT géo-visuel** est une discipline mature (Bellingcat, GeoGuessr). Un combinaison d’indices banaux permet une géolocalisation au quartier voire au bâtiment.

**Pour la publication** : examiner chaque photo en imaginant ce qu’un attaquant motivé peut déduire. Recadrer, flouter agressivement les éléments contextuels.

#### 35.3 Voix : empreinte vocale et clonage

Cf. Ch 34. Implications spécifiques :

- Tes interviews publiques, conférences vidéo, podcasts sont des échantillons exploitables pour cloner ta voix.
- Stratégie : pour HVT, limiter la diffusion publique de longs échantillons vocaux. Pour usage public (journaliste qui doit témoigner), accepter et compenser par codes hors bande.

#### 35.4 Stylométrie : signature d’écriture

Ton style d’écriture est une empreinte. Caractéristiques :

- Longueur moyenne des phrases.
- Distribution des virgules, points-virgules, deux-points.
- Vocabulaire spécifique (mots favoris, tics).
- Formulations récurrentes.
- Erreurs typographiques personnelles.
- Préférences orthographiques (français de Belgique vs France, anglicismes).

Cas Bitcoin et Satoshi Nakamoto : analyses stylométriques ont éliminé/proposé plusieurs candidats sur la base du seul style.

**Quand c’est important** : pour publication sous pseudonyme stable, si l’attaquant peut soupçonner qui tu es, comparer ton écriture pseudonyme à ton écriture connue est trivial. Le pseudonyme tombe.

**Mitigations** :

- **Réécriture par LLM** : faire passer ton texte par un LLM pour reformulation neutre. Atténue ta signature.
- **Discipline volontaire** : raccourcir ou allonger systématiquement les phrases par rapport à ton naturel, modifier ponctuation. Coût cognitif élevé, durabilité limitée.
- **Pseudonymes à publication courte** : moins d’échantillons = moins de signature stable détectable.

#### 35.5 Traces comportementales : horaires, lieux, routines

Tu es prévisible. Tu te connectes à certaines heures. Tu visites certains sites. Tu écris à certaines personnes. Tu commandes la même chose. Tu prends le même chemin. Cette routine est une signature.

Pour une identité compartimentée : les routines doivent se compartimenter aussi. Le compte « anonyme » qui se connecte aux mêmes heures que ton compte nominal est trivialement corrélable.

**Pratique** :

- Pour compartiments sensibles, varier les fenêtres temporelles, les lieux de connexion, les rythmes.
- Pour rester crédible, ne pas adopter un comportement *trop* différent (qui devient un autre type de signature).

#### 35.6 Métadonnées comportementales hors numérique

- **Achats** : régularité, lieux, types (cf. Ch 32).
- **Déplacements** : transports en commun avec carte nominative (Navigo, Métro), péages, parking surveillé.
- **Présence physique** : caméras (CCTV public et privé), reconnaissance faciale en croissance dans certains pays.
- **Smart home** : assistants vocaux qui enregistrent, thermostats connectés qui révèlent présence/absence.

#### 35.7 Discipline du « jamais en ligne quand X »

Une discipline simple à grande efficacité : *ne jamais* utiliser le compte sensible quand tu es identifiable autrement. Si ton téléphone perso est allumé chez toi, ton compte sensible ne se connecte pas en même temps depuis ton FAI domestique — corrélation triviale.

Schéma :

- Compte sensible utilisé exclusivement depuis lieux/réseaux/appareils distincts.
- Téléphone perso physiquement absent de ces sessions (laissé chez soi, en faraday bag, etc.).
- Pas de cross-contamination horaire.

#### 35.8 *Fil rouge* — Léa adopte une routine stricte

Sur l’enquête, Léa s’impose :

- Téléphone perso laissé chez elle (chargeur sur la table, comme si elle ne sortait pas) les jours d’enquête sensible.
- Travail enquête uniquement depuis le bureau séparé (loué via le consortium), ou Tails sur laptop dédié dans un lieu calme.
- Horaires d’enquête : afternoon et soir, jamais matin (qui est son créneau pro public).
- Communications avec Karim : créneaux convenus, jamais réponse impulsive.

-----

### Chapitre 36 — Voyage, frontières et appareils temporaires

#### 36.1 Modèle de menace voyageur

La frontière est un lieu particulier : l’État a légalement le droit d’inspecter tes appareils dans des limites variables. Les douanes US peuvent demander à examiner ton téléphone et ordinateur, parfois à les retenir plusieurs jours. Singapour, Israël, certains pays asiatiques également. Européen entrant aux US : la liberté de refuser est limitée (refus = refus d’entrée).

Pour les voyages en pays à forte censure ou à DPI agressif, le choix du VPN doit être fait **avant le départ**. Installer un outil de contournement une fois sur place peut être impossible si les sites officiels, stores ou dépôts sont bloqués.

**Procédure** : installer, tester et documenter au moins deux options avant le départ : un VPN privacy classique, un outil anti-censure obfusqué, et Tor Browser avec bridges. Ne pas dépendre d’un seul canal.

Trois questions à se poser avant tout voyage :

1. **Ai-je vraiment besoin** de mes données habituelles sur cet appareil ?
1. **Que se passe-t-il si l’appareil est saisi, cloné, ou rendu après accès** ?
1. **Quelles sont les règles douanières spécifiques** au pays d’entrée ?

#### 36.2 BFU vs AFU à la frontière (CRITICAL)

**Avant de passer une frontière** : éteindre complètement les appareils. Pas de verrouillage, pas de sommeil. **Vraie extinction**.

Effet : les appareils sont en BFU (Before First Unlock). La plupart des données utilisateur sont protégées par des clés dérivées du code de déverrouillage, qui ne sont pas en mémoire. Les outils forensics professionnels (Cellebrite UFED, GrayKey) sont **significativement moins efficaces** sur un appareil en BFU que sur un appareil en AFU.

Cinq secondes de discipline avant chaque passage frontalier = écart énorme en posture forensique.

#### 36.3 Burner devices

Pour voyages sensibles (frontière hostile, pays à risque) : appareils dédiés au voyage, distincts du quotidien.

- **Téléphone de voyage** : ancien Pixel, GrapheneOS minimal, comptes burner (email dédié, Signal dédié), aucune photo ni contact personnel. Au retour : reset complet ou destruction.
- **Laptop de voyage** : Chromebook ou laptop minimal, comptes burner, données non sensibles uniquement, pas de cookies de session, pas de fichiers locaux. Si besoin d’accès, données récupérées via cloud E2EE après arrivée.

#### 36.4 Procédures pre-voyage

1. **Audit** : qu’est-ce qui ne doit absolument pas franchir la frontière ?
1. **Cloud E2EE** des données nécessaires (Proton Drive, etc.), accessibles depuis l’arrivée.
1. **Backup** complet avant départ.
1. **Effacement des comptes sociaux non essentiels** sur l’appareil de voyage.
1. **Déconnexion** de tous les comptes critiques sur l’appareil de voyage (sessions révoquées, à reconnecter à l’arrivée si besoin).
1. **Compte burner** prêt pour communications de voyage.

#### 36.5 À l’arrivée

- Vérifier l’intégrité physique (vis, scellés, comparaison photos).
- Si soupçon de manipulation : ne pas reconnecter aux comptes principaux, considérer l’appareil comme suspect.
- Reset à neuf si possible.
- Reconnexion progressive aux comptes nécessaires, en surveillant les notifications de connexion suspecte.

#### 36.6 Au retour

- Reset complet de l’appareil de voyage, ou destruction physique si haut risque.
- Audit des appareils restés au domicile (intrusion physique pendant absence ?).
- Audit des comptes : sessions de l’étranger ? Connexions inhabituelles ?
- Changement préventif des credentials critiques si profil HVT.

#### 36.7 Cas particuliers

- **Activistes vers Iran, Russie, Chine, certains pays Moyen-Orient** : VPN nécessaires mais souvent bloqués (utiliser Tor avec bridges, ou VPN avec protocoles obfusqués). Risques pénaux selon pays. Consulter ONG spécialisées (Access Now, EFF, RSF, Front Line Defenders) avant départ.
- **Journalistes en zones de conflit** : protocoles CPJ Digital Safety Kit, RSF guide journaliste, formations dédiées (Hostile Environment Awareness Training).
- **Dirigeants en mission commerciale Asie** : ANSSI publie des guides ; programme de sécurité économique gouvernemental français.

#### 36.8 *Fil rouge* — Léa voyage à Kiev pour enquête terrain

Préparation :

- iPhone perso laissé à Bruxelles.
- Pixel 8a GrapheneOS avec profil enquête, contenant : Signal pro, SimpleX pour Karim, OnionShare, navigateur Vanadium, rien d’autre.
- Laptop dédié enquête (MacBook Air séparé), FileVault, Mullvad VPN, Tails sur clé USB de secours.
- Backup chiffré complet de toute son enquête sur Proton Drive avant départ.
- Compte SimpleX accessible depuis n’importe quel appareil avec ses clés.
- Numéro Signal communiqué à 3 contacts d’urgence : avocate, rédaction, ami de confiance.

À l’arrivée :

- Vérification matérielle : pas de manipulation visible.
- Premier contact local par téléphone non lié, lieu choisi par sa source locale.

Au retour :

- Reset complet du téléphone et laptop.
- Audit des comptes : aucune connexion suspecte.
- Documents rapatriés via Proton Drive en mode E2EE.

-----

### Chapitre 37 — Cadre juridique et éthique

> **Note** : cette section est informative et générale, pas un avis juridique. Le droit évolue rapidement (Chat Control, AI Act, transpositions diverses). En cas d’enjeu réel, consulter un avocat spécialisé.

#### 37.1 Vie privée et CEDH article 8

L’article 8 de la Convention européenne des droits de l’homme garantit le droit au respect de la vie privée et familiale, du domicile et de la correspondance. Restrictions admises sous trois conditions cumulatives :

- **Prévue par la loi**.
- **Légitime** (sécurité nationale, ordre public, etc.).
- **Nécessaire dans une société démocratique** (proportionnée).

Jurisprudence CEDH abondante. Toute mesure de surveillance massive doit passer ce triple test ; plusieurs régimes nationaux ont été retoqués (UK GCHQ, France IOC, etc.).

#### 37.2 RGPD : droits utilisables

Articles directement utilisables par un individu :

- **Article 15** : droit d’accès. Tu peux demander à tout responsable de traitement quelle donnée il détient sur toi.
- **Article 17** : droit à l’effacement (« droit à l’oubli »).
- **Article 21** : droit d’opposition au traitement.
- **Article 20** : droit à la portabilité.

Recours : CNIL (FR), équivalent national (APD en Belgique, AEPD en Espagne, etc.), avec amendes croissantes en cas de violation.

#### 37.3 LCEN : chiffrement libre en France

L’article 30 de la loi sur la confiance dans l’économie numérique (LCEN, 2004) consacre la liberté d’usage des moyens de cryptologie en France. Le chiffrement personnel est **légal et garanti**. L’État ne peut pas l’interdire pour l’usage privé.

Limites : obligations de déclaration pour les fournisseurs de moyens de cryptologie ; régime spécifique pour l’exportation ; obligation de déchiffrer sur réquisition judiciaire (cf. 37.5).

#### 37.4 Secret des sources des journalistes

Loi française du 4 janvier 2010 sur la protection du secret des sources : pas d’atteinte au secret des sources sans impératif prépondérant d’intérêt public, et selon procédures strictes.

Règlement (UE) 2024/1083 dit *European Media Freedom Act* (EMFA) : renforcement, harmonisation européenne, encadrement strict de l’usage du spyware contre journalistes, droit d’opposition à la révélation des sources, protection contre les pressions économiques sur les rédactions. Le texte n’est pas une directive (qui aurait laissé une marge de transposition nationale) mais un règlement directement applicable.

**En pratique** : protégé en droit, mais des affaires (Édouard Tétreau, Le Monde, Mediapart vs renseignement) ont montré les fragilités. L’OPSEC technique du journaliste reste un complément indispensable à la protection légale.

#### 37.5 Obligation de remettre une convention secrète de déchiffrement

Cas français : l’article 434-15-2 du Code pénal sanctionne le **refus de remettre aux autorités judiciaires une convention secrète de déchiffrement d’un moyen de cryptologie susceptible d’avoir été utilisé pour préparer, faciliter ou commettre un crime ou un délit**. Peines : trois ans d’emprisonnement et 270 000 € d’amende ; aggravées à cinq ans et 450 000 € si le refus a empêché la prévention d’un crime ou délit.

Le Conseil constitutionnel a, à plusieurs reprises (notamment 2018 et 2025), validé le dispositif sous réserves d’interprétation, en précisant notamment les conditions dans lesquelles ce délit peut être retenu. La jurisprudence reste cependant nuancée :

- Distinction entre la **convention secrète** (clé cryptographique, mot de passe d’un volume chiffré) et le **code utilisateur** d’un appareil (qui sert à déverrouiller mais ne constitue pas en soi une convention de déchiffrement) — distinction qui a fait l’objet de jurisprudences contradictoires.
- Conditions de l’obligation : la convention doit concerner un moyen de cryptologie « susceptible d’avoir été utilisé » pour un crime ou délit, ce qui suppose un faisceau d’indices, et non une simple suspicion généralisée.
- Pratique des juridictions très variable selon contexte et selon avocats engagés.

**Cas comparés** :

- **Royaume-Uni** : RIPA section 49 prévoit une obligation équivalente (jusqu’à deux ans de prison pour refus, cinq ans pour terrorisme ou pédocriminalité).
- **États-Unis** : le Cinquième Amendement protège contre l’auto-incrimination forcée ; la jurisprudence sur l’usage forcé de la biométrie par rapport au code mémoire mémorisé reste mouvante (plusieurs décisions divergentes selon circuits fédéraux).
- **Suisse** : pas d’obligation équivalente à 434-15-2 ; position structurellement plus protectrice.

**Implication pratique** : il ne revient pas à ce cours de recommander une attitude (refuser ou non) face à une demande de communication d’une convention de déchiffrement, ni d’évaluer ce qui constitue ou non une telle convention dans un cas concret. Ces questions relèvent d’une analyse juridique individuelle. **Si tu es confronté à une telle demande, la seule action raisonnable est de consulter immédiatement un avocat spécialisé** (droit pénal, droit numérique, ou droit de la presse selon contexte). Refus mal calibré comme communication imprudente peuvent l’un et l’autre aggraver la situation.

Au plan opérationnel préventif, en revanche, ce cours observe que :

- Le code utilisateur **mémorisé** (non biométrique) est structurellement plus difficile à obtenir d’une personne sous contrainte qu’une empreinte digitale ou un visage qui peuvent être utilisés sans coopération active.
- L’état BFU (cf. Ch 12.8) protège les données mieux que l’état AFU contre les outils forensics commerciaux, indépendamment de la question juridique.

#### 37.6 Sapin II : lanceurs d’alerte en France

Loi Sapin II (2016), modifiée par la loi du 21 mars 2022 transposant la directive UE 2019/1937.

Protection accordée aux personnes signalant des faits :

- **Crimes ou délits**.
- **Violations graves de la loi**.
- **Menaces ou préjudices** pour l’intérêt général.

Procédure :

1. **Signalement interne** (en premier lieu, sauf exceptions).
1. **Signalement externe** : autorité compétente (Défenseur des droits, AAI sectorielle).
1. **Divulgation publique** : possible si signalements précédents sans suites, ou risque imminent.

Protections : non-licenciement, non-représailles, confidentialité de l’identité, soutien juridique du Défenseur des droits.

**Limite** : les sanctions effectives contre représailles restent partielles. Beaucoup de lanceurs d’alerte ont payé un prix professionnel et personnel important malgré la loi.

#### 37.7 Anti-doxxing

En France, plusieurs qualifications mobilisables :

- **Atteinte à la vie privée** (art. 226-1 CP).
- **Mise en danger** (si publication d’adresse avec menace).
- **Harcèlement moral** ou en meute (art. 222-33-2-2 CP).
- **Loi du 21 mars 2022** : aggravation des peines pour révélation d’information privée mettant en danger.

Signalement PHAROS. Plainte au parquet. Recours civil pour cessation et indemnisation.

#### 37.8 Chat Control / CSAR : suivi

Cf. Ch 26.12 pour le détail. État de synthèse : dossier toujours en négociation à la rédaction (2026). Le Conseil a pris position en novembre 2025 ; le Parlement européen a soutenu en mars 2026 l’extension temporaire de la dérogation ePrivacy jusqu’en août 2027, ce qui maintient la fenêtre légale actuelle pour les scans volontaires hors-E2EE pendant que les négociations sur le règlement principal continuent. Les positions nationales évoluent au gré des présidences tournantes et des élections.

Si la version finale impose un scanning côté client sur l’E2EE, l’impact serait majeur pour la disponibilité de la messagerie E2EE européenne grand public.

#### 37.9 AI Act UE

Règlement UE 2024/1689 (« AI Act ») : encadrement de l’IA dans l’UE, entré en vigueur progressivement 2024-2026. Pertinence privacy :

- **Article 5** : interdictions (notation sociale, certaines reconnaissances biométriques en temps réel par autorités).
- **Article 6+** : systèmes à haut risque, dont certains usages de reconnaissance faciale.
- **Article 50** : obligation de marquage des contenus IA (deepfakes).

Sanctions importantes pour fournisseurs IA.

#### 37.10 Comparaison FR / UE / US / UK / CH (synthèse)

|Aspect                  |France           |UE                   |US                   |UK               |Suisse                |
|------------------------|-----------------|---------------------|---------------------|-----------------|----------------------|
|**Chiffrement libre**   |Oui (LCEN 30)    |Oui (RGPD compatible)|Oui (constitutionnel)|Oui mais RIPA    |Oui (forte protection)|
|**Obligation clé**      |Oui (434-15-2 CP)|Variable             |5e amendement protège|Oui (RIPA s.49)  |Non                   |
|**Surveillance massive**|LRM 2015, ajustée|Encadrée (CJUE)      |FISA, NSL            |IPA 2016         |Forte protection      |
|**Anti-doxxing**        |Oui (loi 2022)   |Variable national    |Variable état        |Oui (M.Comms Act)|Oui                   |
|**Lanceurs d’alerte**   |Sapin II / 2022  |Directive 2019       |Patchwork sectoriel  |PIDA             |LWB                   |

#### 37.11 Cadre éthique du cours

Ce cours forme à des compétences défensives. Il ne couvre pas :

- Attaque, intrusion, exploitation.
- Contournement d’une enquête judiciaire légitime.
- Dissimulation d’activités illicites.
- Doxxing, harcèlement, fraude à pseudonymes.
- Usurpation d’identité.

Le pseudonymat, le chiffrement, l’anonymat sont des droits exercés dans un cadre légal. Leur usage à des fins illicites engage la responsabilité pénale de l’auteur, indépendamment de l’efficacité technique de l’outil.

-----

### Chapitre 38 — Maintenance opérationnelle, réponse à incident et architectures par profil

#### 38.1 La sécurité est un processus, pas un état

Une posture sécurisée installée en une semaine et jamais entretenue s’érode en six mois. Les mises à jour ne s’appliquent pas, les comptes oubliés s’accumulent, les habitudes glissent, les outils deviennent obsolètes. La maintenance n’est pas optionnelle.

#### 38.2 Routines : hebdo, mensuelle, trimestrielle, annuelle

**Hebdomadaire (15 minutes)** :

- Vérifier que les mises à jour OS et apps sont appliquées.
- Audit rapide des notifications de connexion suspecte.
- Vérification du fonctionnement des sauvegardes automatiques.
- Reboot des appareils sensibles (si pas quotidien).

**Mensuelle (1 heure)** :

- Audit des sessions actives sur comptes critiques (Google, Apple, Microsoft, Signal).
- Vérification HaveIBeenPwned sur emails principaux.
- Audit des permissions d’apps mobiles (revue de ce qui a accès localisation, micro, photos).
- Test rapide de restauration sauvegarde (juste vérifier qu’elle se monte et que les fichiers s’ouvrent).
- Mise à jour firmware si pas auto.

**Trimestrielle (2-3 heures)** :

- Audit complet OSINT défensif (Ch 5).
- Désinscription data brokers nouvellement apparus (Ch 6).
- Audit des appareils : intégrité physique, configuration, comptes connectés.
- Revue du threat model : a-t-il évolué ? Mes adversaires ont-ils changé ?
- Test de restauration complet (sur appareil neuf ou VM).
- Renouvellement des sous-clés PGP si applicable.

**Annuelle (1 jour)** :

- Audit complet de tous les comptes (suppression des inutilisés).
- Renouvellement des clés matérielles si signe d’usure.
- Revue de la stratégie globale : architecture, outils, threat model, formation.
- Documentation à jour (procédures personnelles, contacts d’urgence, codes de récupération).
- Décisions stratégiques : migration vers nouvel OS, nouveau matériel, nouvelle compartimentation.

#### 38.3 Réponse à incident : framework PICERL

Hérité de la cybersécurité d’entreprise, applicable au particulier :

- **P**reparation : avant tout incident, avoir une procédure documentée, contacts d’urgence, backups, outils prêts.
- **I**dentification : détecter qu’un incident a lieu. Notifications plateformes, alertes, comportement anormal.
- **C**ontainment : limiter la propagation. Isoler appareil, révoquer sessions, changer credentials des comptes touchés.
- **E**radication : éliminer la cause. Reset appareil, retrait de malware, fermeture des accès illégitimes.
- **R**ecovery : restaurer le fonctionnement normal. Restauration depuis backup propre, reconfiguration.
- **L**essons learned : analyse post-incident, mise à jour des procédures.

#### 38.4 Procédures par scénario

**Téléphone perdu/volé** :

1. Localisation à distance (Find My iPhone / Android Find My Device) si possible.
1. Effacement à distance si non récupérable.
1. Désactivation SIM auprès de l’opérateur.
1. Révocation sessions des comptes critiques.
1. Désinscription des passkeys liées à l’appareil.
1. Déclaration de vol (police, assureur).
1. Restauration sur appareil neuf depuis sauvegarde.

**Compte compromis** :

1. Changer immédiatement le mot de passe depuis appareil sain.
1. Révoquer toutes les sessions actives.
1. Audit : modifications récentes, filtre mail, méthodes MFA ajoutées.
1. Activer MFA matériel si pas déjà.
1. Vérifier comptes liés (cascade depuis email principal).
1. Communiquer aux contacts si phishing envoyé depuis ton compte.
1. Déposer plainte si dommages.

**Spyware suspecté** :

1. Mode avion + faraday bag immédiatement.
1. Ne pas redémarrer.
1. Contact Access Now Digital Security Helpline (+1-888-414-0100).
1. Sauvegarde pour analyse (iTunes/Quicktime pour iOS).
1. Soumission à Citizen Lab / Amnesty Security Lab pour confirmation.
1. Bascule appareil neuf, comptes audités, threat model révisé.

**Doxxing en cours** :

1. Documentation (captures, URLs, horodatages).
1. Signalement plateformes hébergeantes.
1. Évaluation menace physique, mise à l’abri si nécessaire.
1. Support psychologique et juridique (PEN America, RSF, La Quadrature selon profil).
1. Plainte (PHAROS, parquet).

#### 38.5 Architectures de référence par profil

**Profil 1 : particulier durci grand public**

- iPhone à jour avec ADP iCloud activée.
- Mac ou PC Windows 11 Pro avec chiffrement disque.
- Bitwarden + clés YubiKey (principal + backup).
- Signal pour communications, WhatsApp pour social, Proton Mail principal + alias.
- Mullvad ou IVPN.
- Routines mensuelles + trimestrielles appliquées.

**Profil 2 : journaliste freelance**

- Pixel 8a + GrapheneOS + iPhone perso séparé (ADP).
- MacBook Pro pro + MacBook Air enquête.
- Bitwarden + YubiKey 5 (principal + backup au coffre).
- Signal + SimpleX + Proton Mail pro + alias.
- Tails sur USB pour sessions ponctuelles ultra-sensibles.
- Mullvad VPN, Mullvad Browser quotidien, Tor Browser anonyme.
- Page « comment me joindre confidentiellement » publique.
- Routines complètes appliquées.

**Profil 3 : activiste, manifestation à risque**

- GrapheneOS sur Pixel d’occasion dédié manifestation.
- Aucune donnée personnelle, contacts limités à 3 numéros essentiels.
- Faraday bag.
- Numéros de hotline juridique et avocat sur papier.
- Procédure d’arrestation préparée (qui appeler, qui prévenir).
- Vrai téléphone perso laissé chez soi.

**Profil 4 : dirigeant PME exposé**

- MacBook avec ADP iCloud, FileVault, Lockdown Mode en voyage sensible.
- iPhone idem.
- 1Password famille (partage avec direction).
- Signal pour interne sensible, iMessage avec Contact Key Verification pour exec team.
- Compartimentation pro/perso strictes.
- Formation périodique des collaborateurs (BEC, phishing).
- Politique d’entreprise : MFA obligatoire, MDM Apple Business Manager / Intune.

**Profil 5 : opposant politique en exil (modèle Anya)**

- GrapheneOS dédié, profils stricts.
- Qubes OS pour travail public.
- Tor par défaut pour publications.
- Signal/SimpleX selon contacts.
- Liens hebdomadaires avec Citizen Lab / Access Now.
- Préparation à un éventuel ciblage spyware (MVT installé, iVerify).
- Documentation publique de la situation = stratégie protectrice.

**Profil 6 : RSSI ONG terrain (modèle Yann)**

- Qubes OS sur laptops équipe.
- Procédures écrites et formation continue.
- Cloud E2EE collectif (Proton Drive Business ou Tresorit).
- Stack messageries unifiée (Signal pour interne, Wire pour partenaires).
- Audit annuel par tiers de confiance.

**Profil 7 : particulier face à ex-conjoint abusif (cas D)**

- Changement complet de credentials après séparation.
- Nouveau téléphone, nouveau Apple ID / Google.
- Audit physique du domicile (caméras cachées, AirTags, stalkerware).
- Coalition Against Stalkerware ressources.
- Soutien : association locale, juriste, psychologue.
- Compartimentation totale avec l’ancien partenaire (canaux, comptes, lieux).

**Profil 8 : profil HVT extrême (combinaison)**

- Qubes OS + GrapheneOS combinés.
- Tor + VPN obfusqué.
- Multiples appareils air-gap pour secrets long terme.
- Procédures forensiques mensuelles (MVT auto-vérification).
- Réseau de soutien (avocats, ONG, contacts médias).
- Documentation publique stratégique.

#### 38.6 Quand simplifier

L’inverse de l’élévation de posture est aussi nécessaire à savoir gérer : quand l’enquête se termine, quand le threat ne s’applique plus, quand on quitte un poste à risque. Démantèlement contrôlé :

- Décommissioning des appareils dédiés.
- Fusion progressive des comptes si justifié.
- Effacement des secrets de l’enquête (en gardant copies légales et archives).
- Retour à un standard durci mais soutenable.

Le sur-durcissement permanent sans justification est aussi une faute opérationnelle.

-----

> 🟩 **À retenir de la Partie 7**
> 
> - L’humain est le principal vecteur d’attaque moderne. Le travail sur soi et son entourage compte autant que la technique.
> - L’IA générative a déplacé les seuils : phishing personnalisé indiscernable, deepfakes audio/vidéo accessibles.
> - Frontières : éteindre vraiment (BFU), burner devices pour pays sensibles.
> - Le droit protège, mais sa connaissance et son usage actif sont nécessaires. Pas d’OPSEC sans cadre légal éclairé.
> - La sécurité est un processus. Routines hebdo/mensuelle/trimestrielle/annuelle.
> - Architectures par profil : la posture suit le threat model, pas le mode.

-----

## Cas de synthèse finaux

> **Pourquoi ces cas** : les chapitres précédents ont introduit briques et concepts. Les cas montrent comment ces briques se combinent dans des scénarios réalistes complets. Chaque cas mobilise plusieurs parties du cours et fait l’objet de renvois croisés explicites. Le **Cas A** clôt le fil rouge de Léa. Les **Cas B, C, D** déploient les autres profils annoncés en avant-propos.

-----

### Cas A — Léa Martens : journaliste d’investigation, enquête transeuropéenne

**Clôture du fil rouge.** Mobilise les Parties 1-7. Renvois explicites entre chapitres.

#### A.1 Contexte

Léa Martens, 34 ans, journaliste freelance à Bruxelles, accréditée auprès du Parlement européen, membre d’un consortium international (12 médias partenaires sur 8 pays). Enquête : dossier de corruption impliquant un commissaire européen actuellement en exercice, une société israélienne de surveillance privée (qui aurait fourni des outils à des États tiers en violation du régime européen d’exportation de biens à double usage), et un oligarque russe en exil sous sanctions UE, qui aurait financé indirectement l’opération en échange de protection politique.

Durée prévue de l’enquête : 14 mois. Publication coordonnée prévue à T+12 mois. Diffusion simultanée sur les 12 médias partenaires. Léa porte la coordination technique des sources francophones et flamandes.

Sources principales :

- **Karim B.** : fonctionnaire dans une autorité administrative française, accès indirect aux échanges avec la société israélienne via dossier export. Lanceur d’alerte interne. Identité absolument à protéger.
- **Maria C.** : avocate roumaine, dossiers civils contre filiale locale de la société de surveillance. Source plus formelle, identité connue dans l’enquête mais nom à protéger dans la publication.
- **Trois autres sources** : ex-employés (deux de la société israélienne, un du cabinet du commissaire). Identité à compartimenter.

Adversaires plausibles :

- **Le commissaire et son cabinet** : capacité moyenne via réseau professionnel, motivation très forte à mesure que l’enquête se précise.
- **La société israélienne** : capacité technique élevée (c’est leur métier), accès commercial à du spyware mercenaire dans l’écosystème de leur cluster (Israël est l’épicentre du secteur).
- **L’oligarque russe** : capacité élevée via services achetés (réseau Wagner-style, ex-FSB privés). Motivation élevée.
- **Services russes** : capacité très élevée, motivation modérée à élevée selon avancement de l’enquête.
- **Trolls et harcèlement coordonné** : capacité faible mais effet réel d’épuisement et de doxxing à la publication.

Hors périmètre explicite :

- Résistance à une saisie judiciaire belge légale (Léa s’engage à respecter la procédure et à faire appel à son avocat).
- Anonymat auprès de sa rédaction et auprès des partenaires consortium.
- Protection contre criminalité opportuniste banale (couverte par hygiène standard).

#### A.2 Architecture déployée

À l’issue des 14 mois, Léa opère sur trois compartiments séparés.

**Compartiment 1 — Vie civile (Léa Martens, perso)** :

- iPhone 15 Pro perso avec ADP iCloud activée, Lockdown Mode désactivé (usage quotidien banal).
- MacBook Air perso, FileVault, comptes Apple iCloud familiaux, photos famille, vie courante.
- Email principal Proton Mail (migration progressive depuis Gmail terminée après 4 mois).
- Bitwarden + YubiKey 5C NFC principale + YubiKey backup au coffre familial.
- Mullvad VPN sur usage routier (cafés, voyages courts).
- Signal et iMessage avec famille et amis.

**Compartiment 2 — Vie professionnelle publique (journaliste freelance)** :

- MacBook Pro pro, FileVault, compte Apple distinct (sans liaison avec le perso).
- Email pro `lea.martens@[domaine consortium]`, PGP activé avec sous-clés tournantes annuelles, clé maître en air-gap (cf. infra).
- Bitwarden pro distinct (avec YubiKey distincts également).
- Réseaux sociaux pro publics (X, LinkedIn, Bluesky) maintenus activement, avec hygiène (pas de géotag, pas de routines visibles, pas de photo de famille).
- Signal pro (avec username, numéro de téléphone non communiqué publiquement), iMessage activé avec Contact Key Verification pour ses 30 contacts pro principaux.
- Page « comment me joindre confidentiellement » sur son site pro : clé PGP, lien SecureDrop du consortium, son username Signal, mention « pour transmissions sensibles, contactez-moi d’abord, on choisit ensemble le canal ».
- Mullvad Browser quotidien, Firefox + uBlock + arkenfox pour usage rédactionnel, Brave secondaire.

**Compartiment 3 — Enquête sensible (compartiment 3, sans pseudonyme distinct)** :

- Pixel 8a + GrapheneOS, acheté cash en magasin (Léa a marché 30 minutes pour aller au point de vente choisi au dernier moment, payé en liquide).
- Trois profils utilisateur GrapheneOS sur le Pixel : profil principal vide et utilisé seulement pour communication d’urgence ; profil « enquête » avec Signal/SimpleX/Vanadium ; profil « voyage » pour déplacements terrain.
- MacBook Air dédié enquête, FileVault, jamais connecté au compte Apple personnel, OS et apps minimales, mises à jour disciplinées.
- Tails sur deux clés USB neuves achetées en deux fois, en deux lieux différents : usage pour sessions sensibles ponctuelles (premier contact source, ouverture de documents particulièrement à risque).
- Stack messageries enquête : SimpleX (canal source primary avec Karim), Signal avec username (canaux source secondary avec Maria et autres sources), Proton Mail avec alias SimpleLogin (un alias par source pour les très rares occasions où l’email est utilisé).
- Air-gap minimal : un Mac Mini ancien acheté d’occasion, déconnecté de tout réseau, déconnecté physiquement quand non utilisé, dans un coffre. Sert à stocker la clé maître PGP utilisée pour signer les sous-clés annuelles, et à archiver les documents les plus sensibles.
- VPN Mullvad sur tous les terminaux enquête, plus Tor Browser pour navigation anonyme.
- Routine de reboot quotidien du Pixel.

**Stratégie cloud** :

- Documents quotidiens d’enquête : Proton Drive (E2EE par design), avec dossiers compartimentés.
- Archives ultra-sensibles : conteneurs VeraCrypt sur disque externe chiffré, en coffre.
- Sauvegarde 3-2-1-1-0 : 3 copies (Proton Drive + disque local chiffré + disque externe en coffre), 2 supports différents, 1 hors site (le disque externe est chez une avocate de confiance), 1 immuable (snapshot mensuel signé), 0 erreur (test de restauration trimestriel).
- Sauvegardes WhatsApp désactivées (Léa n’utilise pas WhatsApp pour l’enquête, et a activé sauvegarde E2EE pour son WhatsApp perso).

#### A.3 Stack source-journaliste avec Karim

Karim, fonctionnaire AAI française, alerte interne. Premier contact via une rédaction tierce (Mediapart, qui sert d’intermédiaire neutre). Mediapart envoie un message à Léa : « Une personne souhaite te joindre confidentiellement, voici son indicateur de référence ».

Léa et Karim établissent leur canal :

- **Premier échange** : Léa publie un message dans un thread public sur son compte X pro contenant un détail spécifique qu’elle a convenu avec Mediapart. Karim, en voyant ce détail, reçoit la confirmation que Léa est bien la personne qu’il cherche.
- **Initialisation SimpleX** : Karim installe SimpleX sur un téléphone d’occasion qu’il a acheté cash dans un magasin choisi loin de ses lieux habituels (cf. Ch 9, Ch 15). Il crée un compte SimpleX sans numéro de téléphone.
- **Échange du lien** : Léa et Karim échangent leur lien de connexion SimpleX via le canal Mediapart, qui ne voit pas le contenu (la rédaction relaie un blob chiffré PGP fourni par Léa, déchiffré par Karim avec sa clé qu’il a générée pour l’occasion sur Tails).
- **Vérification d’identité** : premier appel SimpleX vocal court. Léa et Karim ne se connaissent pas physiquement. Ils ont convenu d’un proverbe à prononcer pour authentifier ; le vrai test est dans la cohérence de leur récit et le savoir détenu par Karim (informations vérifiables auprès de Léa).
- **Régime opérationnel** : disappearing messages 24 h pour toute la conversation. Vérification mutuelle hebdomadaire (Léa demande à Karim un détail convenu à l’avance qui change chaque semaine). Transferts de documents via OnionShare exclusivement, pas SimpleX (les fichiers SimpleX restent sur les serveurs SimpleX un temps).

#### A.4 Workflow de réception et traitement des documents

À chaque paquet de documents reçu de Karim (3-7 paquets sur 14 mois) :

1. Réception du lien OnionShare via SimpleX.
1. Léa boot Tails sur sa clé USB enquête principale, depuis le MacBook Air dédié.
1. Téléchargement via Tor Browser à l’intérieur de Tails. Vérification du hash SHA-256 fourni hors-bande par Karim (sur SimpleX, message court non lié au transfert).
1. Passage des PDF par Dangerzone (dans Tails, ou re-importé dans une dispVM Qubes sur le Mac quand Léa migre vers Qubes au mois 8).
1. Audit métadonnées : ExifTool sur chaque fichier. À deux reprises sur les 14 mois, Léa trouve des métadonnées qui auraient révélé l’auteur : un PDF avec « Author = [nom de Karim au format administratif officiel] » dans le XMP, et un DOCX avec un commentaire interne contenant un nom de personne mentionnée dans le bureau de Karim. À chaque fois, nettoyage avant tout transfert ultérieur.
1. Archivage chiffré : import dans conteneur VeraCrypt sur disque externe, déchiffré uniquement lors de sessions de travail sur l’enquête. Le mot de passe du conteneur est un Diceware 8-mots, dérivé via Argon2id (memory ≥ 1 GiB, t=4, p=4).
1. Documentation : log interne (dans le conteneur) — date, source, hash, environnement utilisé, notes contextuelles. Pas pour partage, pour traçabilité d’enquête et audit interne du consortium.

#### A.5 Incident — la tentative de spear phishing à T+5 mois

À cinq mois d’enquête, Léa reçoit sur son email pro un message d’apparence légitime, qui semble venir d’un correspondant d’un des médias partenaires du consortium. L’objet : « Suite à notre échange à la conférence Bruxelles — documents complémentaires ». Pièce jointe : un PDF.

Léa, par discipline, ne clique pas en client mail (la preview est désactivée par défaut sur sa stack). Elle examine les en-têtes : DKIM signature présente mais sur un domaine très proche du domaine légitime (`partner-media-org.com` au lieu de `partnermediaorg.com`). Récente création de domaine (Whois indique enregistrement il y a 9 jours). L’expéditeur n’est pas dans son carnet d’adresses vérifié.

Elle ne télécharge pas le PDF en environnement de quotidien. Elle bascule vers son MacBook Air enquête, isole le fichier dans un dispVM (Léa est passée à Qubes 2 mois plus tôt sur ce laptop), l’ouvre dans la dispVM. Le PDF, à l’œil nu, contient quelques lignes neutres. Mais l’analyse via ExifTool révèle un objet JavaScript embarqué. Léa n’exécute pas ; soumission du PDF anonymisé à un confrère analyste malware (via OnionShare). Diagnostic : tentative d’exploit, probablement non-zero-day, ciblant une ancienne version d’Acrobat Reader. La pièce jointe contient une chaîne d’infection plausible.

Léa documente. Préviens son consortium. Vérification : aucun autre membre du consortium n’a reçu un message similaire ce mois-là — ciblage individuel donc, pas spray-and-pray. C’est un signal important : *quelqu’un sait que je travaille sur l’enquête*. Threat model révisé. Bascule vers Lockdown Mode aussi sur l’iPhone perso (qu’elle n’utilisait pas pour l’enquête, mais qui contient son carnet d’adresses personnel). Audit physique des appareils — rien d’anormal.

À ce stade, l’enquête continue mais Léa adopte une discipline encore renforcée : SimpleX uniquement pour Karim (plus aucun mail), tests MVT mensuels sur le Pixel (rien détecté), reboot deux fois par jour du Pixel, et iVerify installé sur l’iPhone perso (rien détecté).

#### A.6 Tentative de deepfake à T+9 mois

Cf. fil rouge Ch 34. Trois mois après l’incident phishing, Léa reçoit un appel vidéo SimpleX. Voix et image de Karim, ton paniqué : « Léa, j’ai besoin que tu rendes les documents, ils savent, c’est dangereux pour ma famille. » Léa applique le protocole pré-convenu : un proverbe convenu avec Karim au début de la relation, qu’elle lui demande de redire. Silence. Raccrochage côté appelant.

Léa contacte Karim sur SimpleX par texte. Karim répond : « Je n’ai pas appelé. Tout va bien. » Confirmation : deepfake. Léa et Karim audit complet de la stack — quelqu’un a obtenu des échantillons de la voix de Karim (possiblement via interception passive d’un appel téléphonique non sécurisé qu’il a passé à un proche, ou via achat de bases). L’image vidéo provient probablement de photos publiques de Karim (LinkedIn, photo officielle de son service).

Conséquences :

- Vérification que SimpleX lui-même n’est pas compromis : il ne l’est pas, l’attaquant n’a pas réussi à intercepter le canal, il a tenté un *appel sortant frauduleux* en se faisant passer pour Karim depuis un autre compte SimpleX en utilisant le lien public connu par certains tiers. Ce vecteur a été corrigé par SimpleX dans les versions ultérieures.
- Karim renforce sa discipline : aucun appel téléphonique avec proches sur sujets sensibles, audit téléphonique de son entourage qui pourrait être leveraged.
- Léa rappelle dans le protocole : *toute* communication d’urgence inattendue exige double vérification par canal séparé.

#### A.7 Publication coordonnée à T+12 mois

Préparation des 3 derniers mois :

- Caviardage destructif des documents publiés. Vérification croisée par deux confrères du consortium.
- Identification des éléments qui pourraient permettre par recoupement de remonter à Karim. Décision éditoriale : certaines informations sont retirées de la publication parce que trop révélatrices de la source — quitte à affaiblir certaines preuves. Le consortium adopte cette discipline collectivement.
- Préparation de Karim : mise en relation avec l’association *Maison des Lanceurs d’Alerte* en France, premier RDV avec un avocat spécialisé. Karim sait que son identité ne sera pas révélée publiquement par les médias, mais l’enquête interne dans son administration suite à la publication est probable.
- Soutien juridique pour Léa : convention écrite avec un avocat spécialisé en droit des médias, accessible 24/7 dans les 72h post-publication.

Publication simultanée sur les 12 médias partenaires à 06:00 CET. Couverture massive. Réaction politique : démissions, ouverture d’enquêtes parlementaires.

#### A.8 Post-publication : ce qui s’est passé

**Trois premiers jours** :

- Tentatives de doxxing de Léa sur deux canaux Telegram identifiés. Ses informations personnelles principales (adresse, téléphone) ne sont pas trouvables (domiciliation commerciale en place depuis 10 mois, ligne fixe résiliée 6 mois plus tôt). Quelques informations correctes mais anciennes circulent (poste précédent il y a 4 ans, photo d’identité publique). Effet limité.
- Harcèlement coordonné modéré sur X. Léa avait préparé : DMs fermés sauf abonnés, monitoring par un confrère, ne répond pas, archive pour preuves.
- Une notification Apple Threat Notification arrive sur son iPhone perso. Léa applique la procédure : isolement, contact Access Now, soumission Citizen Lab. Diagnostic 12 jours plus tard : présence d’IOCs Predator. Bascule iPhone neuf, threat model révisé en HVT permanent.

**Mois suivants** :

- Trois plaintes en diffamation contre le consortium, toutes rejetées en référé.
- Karim, identifié en interne (mais pas publiquement), placardisé puis détaché. Procédure aux prud’hommes pour licenciement abusif (lanceur d’alerte protégé). Soutien Maison des Lanceurs d’Alerte. Procédure en cours.
- Léa maintient sa stack durcie. Refus pendant 6 mois de toute interview ou apparition publique non strictement nécessaire. Reprend progressivement à 9 mois post-publication.

**12 mois post-publication** :

- Le commissaire visé est démissionnaire (a démissionné « pour raisons personnelles » à T+1 mois post-publication).
- Procédure pénale ouverte au niveau européen, ouverte également en Belgique et en France.
- Léa nominée à plusieurs prix journalistiques. Refuse une médiatisation personnelle excessive — discipline OPSEC en partie incompatible avec exposition.
- Karim, après procédure, obtient des indemnités significatives et une reconversion accompagnée. Son identité reste protégée publiquement.

#### A.9 Renvois croisés mobilisés

- **Threat modeling** : Ch 2 (cadre EFF), Ch 3 (taxonomie adversaires).
- **Réduction empreinte** : Ch 4 (cartographie), Ch 5-7 (OSINT défensif, data brokers, doxxing), Ch 8 (réseaux sociaux).
- **Compartimentation** : Ch 9 + Capstone 1.
- **Matériel et systèmes** : Ch 10-15 (Pixel cash, FDE, GrapheneOS, MacBook Air dédié).
- **Sessions sensibles** : Ch 16-18 + Capstone 2 (Tails, Qubes après bascule).
- **Réseau et navigation** : Ch 19-24 (Mullvad, Tor Browser, fingerprinting, multi-navigateurs).
- **Communications** : Ch 25-32 + Capstone 3 (SimpleX avec Karim, OnionShare pour transferts, PGP pour pivots, métadonnées rigoureusement traitées).
- **OPSEC humaine et juridique** : Ch 33-38 (phishing détecté, deepfake déjoué, Sapin II pour Karim, voyage, maintenance disciplinée).

-----

### Cas B — Sophie Roussel : activiste climat avant manifestation

#### B.1 Contexte

Sophie Roussel, 28 ans, activiste climatique française, exposée à une surveillance administrative et policière régulière en raison de sa participation à des mouvements visés par des dispositifs de renseignement de prévention. Participe à des manifestations dont certaines ont été qualifiées d’« interdites » ces dernières années. Domicile en colocation, vie sociale très active sur les réseaux sociaux militants. Elle s’apprête à participer à une manifestation à Paris contre un projet d’extension d’aéroport régional, manifestation que les organisateurs annoncent comme « pacifique mais désobéissante » — risque élevé d’arrestations, possibilité d’interpellations préventives, présence policière massive annoncée.

Adversaires plausibles :

- **Forces de l’ordre françaises** : capacité élevée localement, ordres judiciaires accessibles, IMSI catchers déployés régulièrement en manifestations (cas documentés par La Quadrature et amicus brief CEDH), reconnaissance faciale en croissance.
- **Infiltrés ou indicateurs** : capacité humaine, fait partie du modèle traditionnel français.
- **Contre-mouvements radicaux** : capacité faible, motivation modérée (harcèlement sur RS si Sophie est identifiée).
- **Employeur futur potentiel** : screening en cas de candidature, mais hors périmètre immédiat.

Hors périmètre :

- Résistance à un mandat de perquisition légal au domicile.
- Anonymat total dans son cercle militant.
- Empêcher la captation par caméra publique.

#### B.2 Préparation 72h avant manifestation

**Configuration de l’appareil de manifestation** :

- Pixel 4a d’occasion acheté il y a 18 mois (Sophie l’utilise spécifiquement pour les actions). GrapheneOS depuis l’achat.
- Profil utilisateur dédié manifestation : aucun compte personnel, contacts limités à : 1) avocat collectif activiste, 2) hotline juridique du Syndicat de la Magistrature, 3) un seul proche désigné référent (son colocataire), 4) le numéro d’urgence collectif de la manifestation.
- Apps : Signal (compte burner, créé avec une carte SIM prépayée — Sophie a vérifié que les SIM prépayées avec petit montant nominal restent achetables anonymement sous certaines conditions ; en pratique en France et Belgique, depuis 2017-2021, l’identité est demandée pour activation). Solution alternative : eSIM via service IP comme JMP.chat, financée en Monero. Signal username préféré.
- Briar installé en sauvegarde : permet communication Bluetooth/Wi-Fi local entre activistes voisins même si le réseau est coupé (cas en manifestation).
- Aucune photo, aucun document, aucun mail.
- Code de déverrouillage : 8 chiffres aléatoires, non lié à des données personnelles, *non biométrique* (Sophie a délibérément désactivé l’empreinte sur ce téléphone — la jurisprudence française permet à un officier de police de demander une biométrie, contraint à fournir code reste juridiquement nuancé).
- BFU forcé : Sophie va éteindre complètement le téléphone avant le départ et ne le déverrouillera que si nécessaire.

**Configuration physique** :

- Sac avec pochette Faraday (achetée chez un fournisseur sérieux, testée — un téléphone en pochette Faraday correcte doit perdre 100 % du signal cellulaire et Wi-Fi).
- Téléphone secondaire et utilitaire (clés perso, etc.) restés au domicile, vraiment éteints.
- Bloc-notes papier dans le sac : numéros importants (avocat, hotline, référent) en clair. Si l’appareil est saisi, ces numéros restent accessibles à Sophie via la mémoire ou ce papier.
- Ne porte pas son portefeuille personnel — porte uniquement une CB prépayée chargée avec 60 € en cash dans une carte distincte, et 100 € en espèces.

**Configuration personnelle** :

- Pas de bijoux distinctifs, pas de tatouage visible (sans contrainte vestimentaire excessive), vêtements anonymes (sweat à capuche, masque selon contexte).
- Sac à dos générique sans signe distinctif personnel.
- Pas d’agenda imprimé contenant des noms.

#### B.3 Brief avant manifestation

Sophie participe à un brief avec son collectif la veille au soir, en présentiel dans un local fermé, téléphones dans une pile à l’entrée (« phone stack ») pour éviter écoute et géolocalisation partagée. Au brief :

- Plan de déplacement, lieux de rendez-vous, points de regroupement en cas de dispersion.
- Identification des sympathisants membres du collectif vs participants extérieurs (vigilance infiltrés).
- Procédure en cas d’arrestation : utiliser le droit au silence, ne rien dire avant arrivée de l’avocat, appeler le numéro de hotline juridique (mémorisé).
- Rappel des règles : pas de photo du visage des camarades sans accord explicite, pas de live sur les RS personnelles.

#### B.4 Le jour J

Sophie part du domicile avec :

- Téléphone manifestation, éteint complètement, en pochette Faraday dans son sac.
- Bloc-notes papier avec numéros essentiels.
- 100 € cash + CB prépayée.
- Bouteille d’eau, lunettes (utiles contre gaz lacrymogène), masque, badge de presse non — Sophie n’est pas journaliste.

Au point de rendez-vous, elle sort le téléphone de la pochette Faraday, le démarre (toujours en BFU à ce stade puisqu’elle ne l’a pas déverrouillé). Active le mode avion. Ne déverrouille que si elle doit envoyer un signal au référent ou contacter l’avocat. Reste majoritairement en BFU pendant la manifestation.

À 14h30, premiers heurts. Charge des forces de l’ordre. Sophie se replie. Plus tard, elle est interpellée en bord de cortège, malgré son comportement défensif (elle ne portait pas d’arme et n’avait pas commis de délit). Interpellation préventive : maintenue en garde à vue 24h pour vérification.

#### B.5 Procédure d’arrestation

- Téléphone éteint, en BFU. Saisie possible mais accès des outils forensics commerciaux structurellement plus difficile en BFU qu’en AFU.
- Au commissariat, les officiers demandent à Sophie de communiquer son code de déverrouillage. Sophie connaît l’enjeu juridique : l’article 434-15-2 du Code pénal sanctionne le refus de remettre une convention secrète de déchiffrement (jusqu’à 3 ans et 270 000 €). La jurisprudence sur le statut exact du code de déverrouillage d’un téléphone par rapport à une « convention secrète » au sens du texte est nuancée et a varié selon les juridictions et les faits (cf. Ch 37.5). Sophie ne tente pas d’apprécier seule cette question juridique.
- Elle indique aux officiers qu’elle souhaite consulter son avocat avant de répondre à toute demande, et invoque son droit au silence sur les éléments pénalement intéressants en attendant. Son colocataire, prévenu à H+2 par la procédure d’urgence, a contacté la hotline juridique du collectif. L’avocat collectif activiste arrive après quelques heures.
- En présence de l’avocat, Sophie discute des suites à donner à la demande de code, en tenant compte de la nature des faits qui lui sont reprochés (le motif initial d’interpellation), des conséquences possibles d’une communication ou d’un refus, et de la stratégie pénale globale. La décision est une décision juridique individuelle prise en conseil — ce cours n’a pas vocation à la recommander dans un sens ou dans l’autre.
- Le téléphone est saisi pour analyse forensique. Garde à vue prolongée à 48h. Libération sans poursuites au-delà de la qualification résiduelle qui sera examinée ultérieurement.

#### B.6 Post-arrestation

- Le téléphone n’est pas restitué immédiatement (rétention pour expertise). Sophie considère le téléphone comme **brûlé** : ne sera plus jamais utilisé même si restitué (pour ne pas le réintégrer compromis dans sa stack).
- Sophie poursuit la procédure avec son avocat. Continue ses communications collectives via le téléphone du colocataire pour la suite.
- Audit de son domicile : son colocataire vérifie qu’il n’y a pas eu visite (les vis du laptop perso de Sophie ont leur vernis intact, photo macro inchangée).
- Procédure : selon l’évolution juridique du dossier, Sophie peut être convoquée ultérieurement pour audition sur différents motifs. L’analyse juridique reste menée par son avocat, qui décide avec elle de la stratégie au fur et à mesure.

#### B.7 Leçons

1. **BFU vraiment.** Le téléphone vraiment éteint à l’arrivée fait la différence forensique : ce qui se passe en garde à vue dépend en partie de l’état dans lequel l’appareil est saisi.
1. **Code mémorisé > biométrie** structurellement. Sous coercition (ou simplement face à une demande d’un officier qui peut techniquement utiliser une empreinte sans coopération active), le code mémorisé non biométrique reste plus difficile à obtenir.
1. **Préparation collective**. La hotline juridique, l’avocat collectif, le référent désigné : la résilience repose sur le réseau, pas sur l’individu seul. Toute question juridique en garde à vue se traite avec un avocat, pas seule.
1. **Téléphone brûlé après saisie**, jamais réintégré dans la stack.
1. **Compartimentation totale** : la vie quotidienne de Sophie n’a pas été affectée. Son téléphone personnel, ses comptes personnels, son ordinateur restent intacts et utilisables.

-----

### Cas C — Olivier Mercier : dirigeant de PME tech, cible d’espionnage économique

#### C.1 Contexte

Olivier Mercier, 47 ans, dirigeant d’une PME française de 80 salariés, secteur chiffrement matériel (HSM, modules pour le secteur bancaire et défense). Capital majoritairement détenu par lui et deux cofondateurs. Carnet de commandes croissant, partenariats avec deux grands groupes français du secteur défense. Récemment, intérêt commercial de la part d’acteurs étrangers (chinois, américain), avec offres de rachat non sollicitées.

Adversaires plausibles :

- **Concurrents internationaux** : capacité d’espionnage économique élevée (services étatiques chinois APT documentés visant la cybersécurité européenne, hacking commercial américain également).
- **Services russes** : capacité très élevée, motivation modérée à élevée (le secteur intéresse).
- **Concurrents européens directs** : capacité moyenne.
- **Criminalité financière** : capacité moyenne, motivation forte si visibilité Olivier (médias spécialisés ont publié son nom).
- **Insiders mécontents** : capacité variable, motivation possible (en cas de conflit interne, peu probable actuellement).

Hors périmètre :

- Espionnage industriel par voie commerciale légitime (intelligence économique standard).
- Diligence raisonnable d’acheteurs potentiels (avec accords NDA).

#### C.2 Posture initiale et audit

À T0, posture standard de PME française : Microsoft 365 entreprise, Windows 11 sur la plupart des postes, quelques Mac chez l’équipe créa/dev. Compte O365 admin global tenu par le DSI. Pas de MFA matériel généralisé. Pas de procédure formelle anti-BEC. Backups Veeam dans le DC local. Pas de Pegasus Test (jamais évoqué).

Audit par RSSI externe à T0+2 mois (Olivier a sollicité après les premières offres de rachat) :

- Vulnérabilités identifiées : MFA SMS sur certains comptes, exposition VPN historique, partage de mots de passe entre dirigeants, comptes Apple ID familiaux mélangés.
- Hygiène réseau : VLAN absent, IoT corporate (impression, salle de réunion) sur même VLAN que postes admin.
- Manque de procédures : pas de processus anti-BEC, pas de Threat Modeling formalisé.
- Surface email externe : Olivier accessible via 4 emails publics, signatures professionnelles riches en information (téléphone direct, fonctions, organigramme implicite).

Plan d’action à 6 mois validé en CODIR.

#### C.3 Architecture cible déployée

**Niveau dirigeants (Olivier + 2 cofondateurs)** :

- iPhones 15 Pro avec Lockdown Mode activé. ADP iCloud. Contact Key Verification entre dirigeants et exec team.
- MacBooks Pro avec FileVault, Lockdown Mode en voyage. Mises à jour disciplinées via Apple Business Manager.
- 1Password Famille + Business (partage de credentials sensibles avec audit). YubiKey 5C NFC (chacun avec 2 clés).
- Signal entre dirigeants (vérification Safety Numbers en présentiel). iMessage en backup.
- Email pro avec MFA matériel obligatoire.
- Travel kit : MacBook Air burner pour voyages sensibles (Chine, US sensibles), GrapheneOS sur Pixel burner.

**Niveau exec team (12 personnes)** :

- Même stack mais sans MacBook burner systématique.
- Formation BEC obligatoire trimestrielle.
- Procédure : tout virement > 10 k€ doit être validé par appel téléphonique sur ligne connue, jamais sur la seule base d’un email.

**Niveau salariés** :

- MFA via Microsoft Authenticator (push) sur tous les comptes O365.
- Politique de chiffrement disque automatique (BitLocker via Intune).
- Filtre email Microsoft Defender + sandbox pour pièces jointes.
- Formation phishing trimestrielle.

**Niveau infrastructure** :

- Segmentation VLAN : production / corporate / IoT / invités.
- Pare-feu sortant restrictif depuis le segment R&D.
- Bastion pour accès admin, journalisation.
- EDR (Microsoft Defender for Endpoint) déployé.
- SOC managé externalisé pour monitoring nuit/weekend.
- Backup 3-2-1 avec immutabilité + tests trimestriels.

**Politique BYOD** : pas de BYOD pour l’accès aux données sensibles. Mobile management via Intune sur les téléphones pro.

#### C.4 Incident à T+8 mois — tentative de BEC sophistiquée

Olivier est en déplacement à Tokyo pour un partenariat. Pendant son absence, la directrice financière (Sophie L.) reçoit un email d’Olivier. L’adresse semble correcte. Le sujet : « URGENT - virement Kazakhstan partenaire confidentiel ». Le message demande un virement de 380 000 € sur un IBAN kazakh, sous prétexte d’un acompte sur partenariat strictement confidentiel à conclure ce jour-là. Le ton est cohérent avec celui d’Olivier. Le mail est suivi 30 minutes plus tard d’un appel téléphonique sur ligne fixe de Sophie, prétendument d’Olivier, voix très similaire (deepfake vocal), insistant : « C’est confidentiel, ne dis rien aux autres, exécute. »

Sophie applique la procédure interne : tout virement > 10 k€ doit être validé par appel sur ligne *connue*. Sophie raccroche, appelle Olivier sur son numéro habituel — pas de réponse (Olivier est en réunion). Sophie attend. Olivier rappelle 2 heures plus tard sur sa ligne habituelle. Confirmation : il n’a rien demandé.

Investigation :

- Email envoyé depuis un domaine sosie (`mercieretassocies-fr.com` au lieu de `mercieretassocies.fr`). DKIM signé sur le domaine sosie.
- Appel téléphonique : numéro spoofé, voix probablement clonée (le SOC retrouve plus tard que la voix d’Olivier est disponible dans plusieurs interviews de presse sectorielle, suffisamment pour un voice clone qualité).
- Reconnaissance préalable : LinkedIn de Sophie L. comme DAF, mention publique du partenariat Tokyo prévu (Olivier l’avait évoqué en conférence 2 mois plus tôt), nom et numéro de Sophie public sur le site corporate.

Effet : pas de perte financière. Investigation par le SOC en lien avec ANSSI (PME stratégique secteur sécurité). Plainte déposée. Identification partielle : infrastructure compromise dans un pays tiers, attribution incertaine.

Réponse :

- Suppression du téléphone direct de Sophie du site corporate.
- Procédure renforcée : tout virement > 50 k€ exige double validation (Sophie + Olivier ou cofondateurs) avec hot-pin vocal convenu en présentiel, à renouveler trimestriellement.
- Communication interne : tous les collaborateurs sont informés du modus operandi. Formation spécifique BEC avec exemples concrets.
- Coordination avec ANSSI sur le partage d’IOCs (l’attaque cible peut être réutilisée sur d’autres entreprises du secteur).

#### C.5 Incident à T+11 mois — voyage Chine

Olivier doit se rendre à Shenzhen pour rencontrer un partenaire potentiel. Préparation :

- MacBook burner installé spécifiquement pour ce voyage, OS frais, aucun document d’entreprise, accès cloud E2EE (Proton Drive) à la demande.
- Pixel burner avec GrapheneOS, profil voyage. Aucun mail pro, aucun compte personnel. Signal username connu de 3 personnes (sa femme, son DSI, son associé).
- Pas de YubiKey emportée (laissée chez le DSI en France).
- Documents physiques minimaux. Notes professionnelles sur papier, à brûler à l’aéroport au retour.
- Avant départ : Olivier informe son DSI et son associé. Plan de communication : un check-in quotidien sur Signal à heure fixe. Si pas de check-in, escalade après 24h.

Pendant le voyage :

- À l’hôtel à Shenzhen, le MacBook burner reste en chambre uniquement quand il est dans le coffre de la chambre (modéré sécurisé, mais pas zero risque). Olivier le porte avec lui le plus souvent.
- Constatation au matin J+2 : la pochette de transport du MacBook a été manipulée (le pli systématique qu’Olivier fait sur la fermeture est défait). Pas de marquage évident sur le laptop lui-même.
- Olivier suspend l’usage du MacBook. Ne l’utilise plus pour les réunions sensibles ce jour. Bascule sur prise de notes papier.

Au retour en France :

- Le MacBook est livré directement à l’analyste forensique externe.
- Investigation : analyse du firmware, du SSD, des logs. Trace d’une connexion physique externe en heures non opérables (3h du matin local), pas de modification système identifiable (ou modification trop fine pour outils d’analyse standard).
- Décision conservative : le MacBook est physiquement détruit. Reset matériel impossible à garantir.
- Coût total du voyage en pertes matérielles : ~3 500 €. Coût en information sensible exfiltrée : zéro (le MacBook ne contenait aucun document sensible).

#### C.6 Posture à T+18 mois

L’entreprise a maintenant :

- Une posture cyber sérieuse, auditée annuellement.
- Une culture interne où la BEC est connue de tous, l’OPSEC voyage est partagée.
- Une relation établie avec l’ANSSI (programme DI/DCI pour entreprises stratégiques).
- Un budget annuel sécurité représentant 4-5 % du CA, contre 1 % à T0.

Les offres de rachat continuent. Olivier les évalue. Aucune compromission documentée. L’entreprise valorise sa posture cyber comme un actif (les acheteurs potentiels du secteur défense font des due diligences cyber poussées ; une bonne posture augmente la valorisation).

#### C.7 Leçons

1. **BEC > APT** comme threat principal pour PME, statistiquement et par retour d’expérience.
1. **Procédures de virement** : code anti-BEC, double validation par canal séparé. Non négociable.
1. **Voyage hostile = burner device**. Le coût d’un burner est inférieur au coût d’une compromission.
1. **Formation continue** des collaborateurs : sans la directrice financière disciplinée, l’entreprise aurait perdu 380 k€.
1. **Relation institutionnelle** : ANSSI pour la France, équivalents nationaux ailleurs. Une PME stratégique a accès à du conseil gratuit.
1. **Trade-off sécurité-business** : le sur-durcissement détruit l’agilité commerciale. La posture doit être proportionnée et soutenable.

-----

### Cas D — Particulier face à un ex-conjoint abusif

#### D.1 Contexte

Catherine, 39 ans, sépare de son conjoint Marc après 8 ans de relation marquée par violences psychologiques et économiques croissantes. Marc, ingénieur informatique de formation, a eu accès à tous les comptes et appareils du couple pendant la relation. Il a installé des outils de tracking sur ses appareils (Catherine suspecte mais ne l’a pas vérifié), connaît les mots de passe de la plupart des comptes, est ajouté comme contact de récupération sur plusieurs services, a accès au compte iCloud familial. Catherine quitte le domicile conjugal pour s’installer dans un studio. Elle craint :

- Que Marc accède à ses communications et localisation.
- Que Marc utilise leurs comptes joint contre elle dans la procédure judiciaire en cours.
- Que Marc l’agresse physiquement (un incident a déjà eu lieu, plainte déposée).
- Que Marc fasse pression sur leurs enfants (garde partagée en cours d’attribution).

Adversaires plausibles :

- **Marc lui-même** : capacité technique réelle, motivation très forte, accès historique considérable.
- **Cercle social et familial de Marc** : capacité variable, motivation modérée.
- **Plateformes et services** : non hostiles mais procédures de récupération exploitables par Marc.

Hors périmètre :

- Disparition complète (Catherine doit rester atteignable juridiquement, dans l’intérêt des enfants).
- Anonymat sur les comptes nominatifs (bancaires, administratifs).

**Particularité éditoriale** : ce profil est sous-traité dans la majorité des cours cyber, qui se focalisent sur l’étatique. Pour une fraction non négligeable de la population — femmes essentiellement — c’est *le* threat model réel.

#### D.2 Procédure d’urgence (J0-J7)

**Jour 0 (jour de la séparation effective)** :

- Catherine quitte le domicile avec ses affaires essentielles. Elle conserve son téléphone actuel pour le moment, mais avec discipline (ne pas s’y connecter à des comptes nouveaux).
- Établissement d’un téléphone neuf, acheté cash dans un magasin, opérateur différent (nouveau numéro non communiqué à Marc).
- Ce téléphone neuf reçoit immédiatement une nouvelle SIM nominale Catherine (KYC normal, pas tentative d’anonymisation — Catherine veut être joignable juridiquement, et c’est plus discret de fonctionner avec un compte normal).

**Jour 1** :

- Audit du téléphone précédent par une personne tierce de confiance (un cousin technicien). Recherche de stalkerware : examen des applications installées (sur Android avec écran de gestion des apps en mode usage avancé ; sur iOS, gestion des profils MDM installés). Résultat : présence d’une application déguisée en « calculatrice » (mSpy renommé), profil MDM Apple installé permettant suivi de localisation. Marc avait installé.
- Catherine décide : *ne pas* effacer immédiatement le téléphone (preuves utiles pour la procédure pénale en cours sur violences). Photos des installations malveillantes, dépôt de plainte additionnelle pour violation de vie privée et installation de logiciel espion (cf. art. 226-1 et 323-1 CP).

**Jour 2-3** :

- **Tous les mots de passe critiques changés** depuis le nouveau téléphone (ou depuis un cybercafé sécurisé) :
  - Apple ID Catherine (sortie du « Family Sharing » avec Marc, création nouveau compte distinct si elle migre vers iPhone neuf).
  - Compte Google.
  - Compte Microsoft.
  - Comptes bancaires (et procédure spécifique avec la banque pour bloquer Marc de l’accès en ligne sur comptes joints).
  - Messageries : Signal, WhatsApp réinstallés sur nouveau téléphone, anciennes sessions révoquées.
  - Réseaux sociaux : changement de mots de passe, retrait de Marc des contacts (Facebook, Instagram, LinkedIn).
  - Compte impôts, sécurité sociale, et autres administratifs.
  - Email principal (Gmail Catherine) : mot de passe, MFA, contacts de récupération vérifiés (retrait de Marc s’il était listé), questions de récupération mises à jour.
- **Contacts de récupération audités** : Apple Account Recovery Contacts (retrait de Marc s’il l’avait été), Google (idem).
- **Numéro de récupération** : remplacement par le nouveau numéro.
- **Comptes joints non clos immédiatement** (procédure légale en cours pour le partage), mais surveillés activement et logs préservés.

**Jour 4-5** :

- **Réseau social** : Facebook → profil verrouillé, audit des amis (suppression du cercle de Marc), publications passées masquées, retrait de toutes les photos taguées par Marc.
- **Localisation** : audit Find My iPhone et services Google (retrait du partage de localisation avec Marc s’il existait). Catherine a constaté qu’elle partageait sa localisation avec Marc sur Google Maps : retiré.
- **AirTags et trackers** : Catherine fait scan de ses affaires (sac, voiture, vêtements neufs) avec son téléphone neuf qui détecte les AirTags inconnus. iOS et Android (depuis 2023-2024) alertent en cas de tracker tiers suivant. Catherine trouve un AirTag dans sa voiture (Marc avait accès au véhicule). Retrait et archivage pour la procédure pénale.

**Jour 6-7** :

- Achat d’un PC neuf si ressources le permettent (laptop d’entrée de gamme, FileVault/BitLocker activés immédiatement, comptes neufs).
- Configuration d’un gestionnaire de mots de passe (Bitwarden gratuit) avec mots de passe nouveaux et uniques pour tous les comptes.
- Configuration de MFA matériel ou TOTP partout où possible (YubiKey si Catherine peut investir, sinon Aegis Authenticator sur le téléphone neuf).

#### D.3 Mois 1-3 : stabilisation

**Audit physique du studio** :

- Vérification absence de caméras cachées (achetée pour 30 € sur Amazon, détecteur RF + lentille caméra). Aucune trouvée.
- Vérification absence d’écoute (microphones discrets) — généralement par scan RF et inspection visuelle.
- Serrure changée (responsabilité du bailleur, demandée explicitement).

**Audit numérique continu** :

- Connexions inhabituelles sur comptes ? Catherine surveille hebdomadaire les sessions actives.
- Alertes de tentative de connexion ? Activées sur tous les comptes principaux.
- Email principal en monitoring HaveIBeenPwned (notification de nouvelle fuite — particulièrement utile si Marc tenterait de la doxxer).

**Communications avec les enfants** :

- Les enfants utilisent leurs propres téléphones (avec accord parental). Catherine et eux communiquent via Signal avec disappearing messages 30 jours pour les conversations non essentielles. Pas de discussion juridique avec les enfants par messages.
- En garde partagée, Catherine n’écrit pas aux enfants sur des sujets sensibles via canaux que Marc pourrait surveiller.

**Soutien externe** :

- Association locale (CIDFF en France, équivalents locaux) pour soutien juridique et psychologique.
- Avocate spécialisée violences conjugales.
- Psychologue spécialisée trauma post-séparation.
- Réseau de soutien (deux amies, une sœur) — un seul cercle de confiance restreint, choisi soigneusement (les autres « amis » communs avec Marc ne sont pas mis dans le secret).
- Coalition Against Stalkerware ressources internationales.

#### D.4 Incident à M+4 — tentative d’accès au compte Gmail

Catherine reçoit une notification : « Une tentative de connexion à votre compte Google a été refusée. Emplacement : [ville de Marc]. Heure : 22h17 ». Plus tard, deuxième notification similaire. Marc tente d’accéder. La MFA matérielle (YubiKey configurée) bloque.

Réponse :

- Catherine vérifie qu’aucune session n’est active.
- Changement préventif du mot de passe.
- Documentation de l’incident : capture des notifications, ajout au dossier juridique.
- Signalement à l’avocate qui transmet à l’instruction.

#### D.5 Incident à M+8 — tentative de doxxing

Marc, dans le contexte de la procédure de divorce conflictuel et de garde, publie sur un blog familial accessible au cercle élargi des informations privées de Catherine : sa nouvelle adresse, son nom d’employeur, des éléments de sa vie privée. Tentative manifeste d’intimidation.

Réponse :

- Capture immédiate (preuve), avec horodatage notarié si possible.
- Signalement à la plateforme.
- Dépôt de plainte additionnelle (atteinte à la vie privée, art. 226-1 ; et possiblement harcèlement).
- Demande de droit à l’effacement au blog hébergeur.
- Communication contrôlée avec l’employeur (Catherine prévient son N+1 de la situation pour qu’il sache à quoi s’attendre, sans détails).

Effet : le blog est retiré sous 72h après signalement à l’hébergeur. La plainte avance, le dossier de violences conjugales se renforce.

#### D.6 Mois 12+ : nouvelle normalité

Un an après la séparation, Catherine a :

- Une stack cyber complètement renouvelée, indépendante de Marc.
- Une procédure judiciaire qui avance (Marc condamné pour les violences initiales, garde partagée modifiée en sa défaveur).
- Une posture de monitoring qui devient routine sans plus être anxiogène.
- Un soutien externe pérenne.

Elle peut commencer à relâcher progressivement la vigilance (sans baisser la garde sur l’hygiène cyber de base), à reconstruire sa vie sociale et professionnelle.

#### D.7 Leçons

1. **L’adversaire de proximité est sous-évalué**. Marc avait des capacités modérées techniquement mais une connaissance préalable totale qui compensait largement.
1. **La rupture cyber doit accompagner la rupture sentimentale**. Sans cela, l’ex-conjoint conserve un accès massif.
1. **La détection de stalkerware** doit être une étape précoce, pas une découverte tardive. Coalition Against Stalkerware fournit ressources et outils.
1. **Les preuves comptent** : ne pas effacer trop vite les éléments compromis qui constituent des preuves utiles à la procédure pénale.
1. **Le soutien collectif** : associations, avocate, psychologue, réseau de proches choisis. Ne pas s’isoler. La défense individuelle pure ne suffit pas.
1. **Patience et durée** : la stabilisation prend des mois, pas des semaines. La posture doit être soutenable sur la durée.

-----

## Annexes

-----

### Annexe 1 — Glossaire (120+ termes)

**A**

**ADINT (Advertising Intelligence)** — Exploitation de l’écosystème publicitaire numérique comme source de renseignement. Utilise notamment le ciblage publicitaire, le RTB, les identifiants publicitaires mobiles, les données de localisation et les bidstream data pour profiler, suivre ou cibler des personnes ou groupes.

**AFU (After First Unlock)** — État d’un appareil mobile après le premier déverrouillage depuis allumage. Beaucoup de clés sont en mémoire ; vulnérabilité forensique élevée par rapport à BFU.

**Advanced Data Protection (ADP)** — Mode iCloud chiffrant en E2EE la majorité des données (Drive, photos, sauvegardes, notes, signets). Hors-périmètre : mail, contacts, calendrier. Nécessite tous les appareils Apple à jour et une clé de récupération.

**Adversary** — Acteur dont les actions contre toi sont à anticiper. Caractérisé par capacité, motivation, probabilité.

**Adversary of proximity** — Adversaire proche (ex-conjoint, harceleur, employeur intrusif). Faible capacité technique typique, mais forte connaissance préalable.

**Air gap** — Isolation physique d’un système (aucune connexion réseau). Mesure forte pour secrets long terme, coûteuse au quotidien.

**AmneziaVPN** — Client VPN open source multi-protocoles permettant d’utiliser Amnezia Premium ou de déployer un VPN self-hosted sur un VPS. Pertinent surtout pour l’anti-censure, le contournement de DPI et les configurations utilisant AmneziaWG, XRay Reality, Shadowsocks ou OpenVPN over Cloak.

**AmneziaWG** — Fork de WireGuard conçu pour rendre le trafic plus difficile à détecter et bloquer par des systèmes de DPI. Utile en environnement censuré, mais ne transforme pas un VPN en réseau d’anonymat.

**AppArmor** — Modèle de Mandatory Access Control sous Linux (Debian, Ubuntu, SUSE). Profils par application.

**APT (Advanced Persistent Threat)** — Acteur étatique ou paraétatique avec capacité, ressource et patience pour campagnes ciblées longues.

**Argon2id** — Fonction de dérivation de clé (KDF) moderne, résistante aux ASIC. À privilégier dans gestionnaires de mots de passe et FDE.

**Attribution** — Conclusion qu’une action est l’œuvre de telle personne ou entité. Niveau de confiance variable.

**B**

**BFU (Before First Unlock)** — État d’un appareil après redémarrage, avant déverrouillage. La plupart des clés sont scellées. Forensiquement le plus protecteur.

**Bidstream data** — Données transmises dans l’écosystème publicitaire lors des enchères en temps réel : appareil, IP, localisation, contexte, application, langue, horaires, segments d’intérêt, etc. Ces données peuvent être utilisées à des fins publicitaires, mais aussi détournées à des fins de renseignement.

**BEC (Business Email Compromise)** — Fraude par usurpation d’identité d’un dirigeant pour demande de virement. Pertes mondiales en milliards.

**BlackLotus** — Bootkit UEFI (2022-2023) contournant Secure Boot via signature vulnérable. Illustre que Secure Boot n’est pas inviolable.

**Bridge (Tor)** — Relais Tor non publié, utilisé pour contourner le blocage des relais publics dans pays censurés.

**C**

**C2PA (Coalition for Content Provenance and Authenticity)** — Standard de provenance cryptographique pour images/vidéos.

**Canvas fingerprint** — Technique de fingerprinting basée sur le rendu d’une image cachée. Variations GPU et drivers produisent signature unique.

**Capitalisme de surveillance** — Modèle économique fondé sur la collecte et exploitation massive de données personnelles.

**Chat Control / CSAR** — Proposition de règlement UE visant le scan des communications avant E2EE. Bloqué depuis 2022 en négociation.

**Cold boot attack** — Extraction de clés depuis la RAM peu après extinction (mémoire persiste quelques secondes).

**Compartmentation (compartimentation)** — Architecture défensive consistant à séparer les activités en compartiments étanches.

**Contact Key Verification** — Mécanisme iMessage (iOS 17.2+) de vérification cryptographique des clés contacts.

**Coreboot** — Firmware open source remplaçant les firmwares constructeur sur certains matériels.

**Corrélation (surface de)** — Ensemble des points par lesquels deux identités ou activités peuvent être reliées.

**Cryptomator** — Outil de chiffrement de dossier côté client, transparent, multi-plateforme.

**D**

**Dangerzone** — Outil FPF qui reconvertit un PDF en PDF propre via conteneur isolé, supprimant tout contenu actif et métadonnée.

**Deepfake** — Contenu synthétique (image, vidéo, audio) généré par IA, imitant une personne réelle.

**Disposable VM (dispVM)** — VM Qubes éphémère, créée à la demande, détruite à la fermeture.

**DKIM (DomainKeys Identified Mail)** — Signature cryptographique des emails par domaine émetteur, pour vérifier authenticité.

**DMARC (Domain-based Message Authentication, Reporting and Conformance)** — Politique de validation email combinant SPF et DKIM, avec gestion des échecs.

**DoH / DoT (DNS over HTTPS / DNS over TLS)** — Protocoles de DNS chiffré, à privilégier pour confidentialité des résolutions.

**Double ratchet** — Algorithme combinant forward secrecy et post-compromise security. Base de Signal Protocol.

**Doxxing** — Publication malveillante d’informations personnelles identifiantes sur une cible.

**DRM (Digital Rights Management)** — Hors périmètre privacy mais souvent confondu. Note : certains DRM (Widevine, etc.) collectent des données.

**E**

**E2EE (End-to-End Encryption)** — Chiffrement bout en bout : seuls expéditeur et destinataire peuvent lire le contenu.

**ECH (Encrypted Client Hello)** — Extension TLS qui chiffre le SNI dans le ClientHello.

**EXIF (Exchangeable Image File Format)** — Métadonnées intégrées aux photos (GPS, modèle, date).

**ExifTool** — Outil de référence pour lire/écrire les métadonnées de fichiers.

**Evil maid** — Attaque par accès physique temporaire (typiquement chambre d’hôtel) modifiant l’appareil.

**F**

**FDE (Full Disk Encryption)** — Chiffrement complet du disque (BitLocker, FileVault, LUKS).

**FIDO2 / WebAuthn** — Standard d’authentification cryptographique forte, base des passkeys.

**Fingerprint (navigateur)** — Signature unique dérivée des caractéristiques de ton navigateur et appareil.

**Forward secrecy** — Propriété cryptographique : la compromission d’une clé ne permet pas de déchiffrer le passé.

**fwupd** — Outil Linux pour mises à jour firmware via le LVFS.

**G**

**GrapheneOS** — OS Android durci et dégooglisé, sur Pixel exclusivement.

**Guard (Tor)** — Premier relais d’un circuit Tor, connaît ton IP réelle.

**H**

**Hardening (durcissement)** — Renforcement de la configuration sécurité d’un système.

**HaveIBeenPwned** — Service de référence pour identifier si un email/téléphone apparaît dans des fuites publiques.

**Heads** — Firmware sécurisé basé sur Coreboot, avec vérification cryptographique au démarrage.

**HVT (High Value Target)** — Cible à forte valeur pour adversaire ressourcé.

**I**

**IDFA / AAID** — Identifiants publicitaires iOS et Android. Désactivables.

**IMSI catcher** — Faux relais cellulaire captant les IMSI à proximité (Stingray, DRT box).

**IOC (Indicator of Compromise)** — Marqueur technique permettant d’identifier une compromission.

**iVerify** — Application de monitoring de sécurité iOS/Android, détection de spyware connus.

**K**

**KDF (Key Derivation Function)** — Fonction transformant un mot de passe en clé cryptographique. Argon2id, scrypt, PBKDF2.

**Killswitch (VPN)** — Interruption du trafic si le tunnel VPN tombe. Indispensable.

**L**

**LCEN** — Loi française de 2004 consacrant la liberté de cryptographie pour usage personnel.

**LinkedIn (réseau social)** — Plateforme professionnelle, source OSINT majeure.

**Linkability** — Possibilité de relier deux activités à la même entité (dimension LINDDUN).

**LINDDUN** — Taxonomie de menaces privacy (Linkability, Identifiability, Non-repudiation, Detectability, Disclosure, Unawareness, Noncompliance).

**Lockdown Mode (iOS)** — Mode haute sécurité iOS désactivant des fonctionnalités exploitées par spyware mercenaires.

**LogoFAIL** — Vulnérabilité firmware (2023) dans le parsing d’images au démarrage, contournant Secure Boot.

**LUKS** — Standard Linux de chiffrement de disque.

**M**

**MAC randomization** — Génération d’adresses MAC aléatoires par les OS modernes pour réduire le tracking Wi-Fi/BT.

**MAID (Mobile Advertising ID)** — Identifiant publicitaire mobile. IDFA sur iOS, AAID sur Android. Conçu pour le ciblage publicitaire, mais exploitable comme pivot de corrélation dans des scénarios ADINT.

**Malvertising** — Usage de publicités en ligne pour diffuser du contenu malveillant, rediriger vers un site piégé ou préparer une attaque ciblée.

**Mandatory Access Control (MAC)** — Modèle de contrôle d’accès obligatoire (AppArmor, SELinux).

**Matrix** — Protocole de messagerie fédérée open source.

**MAT2 (Metadata Anonymisation Toolkit v2)** — Outil de nettoyage de métadonnées de fichiers.

**Mercenary spyware** — Spyware vendu commercialement à des États (Pegasus, Predator, Graphite).

**Mixnet** — Réseau d’anonymisation qui mélange les flux, ajoute de la latence et parfois du bruit réseau pour réduire l’analyse de trafic. Différent de Tor : Tor route en oignon avec trois relais ; un mixnet cherche surtout à réduire la corrélation temporelle et volumétrique.

**MFA (Multi-Factor Authentication)** — Authentification multifacteurs. Hiérarchie : FIDO2 > TOTP > SMS.

**Mullvad** — Fournisseur VPN suédois, référence privacy. Sans compte utilisateur.

**MVT (Mobile Verification Toolkit)** — Outil Amnesty pour détecter spyware (Pegasus, Predator) dans sauvegardes mobiles.

**N**

**Need-to-know** — Principe : partager une information sensible uniquement avec ceux qui en ont besoin pour leur rôle.

**Nextcloud** — Cloud auto-hébergé open source.

**NymVPN** — VPN décentralisé basé sur l’écosystème Nym. Propose un mode Fast en deux sauts et un mode Anonymous en cinq sauts via mixnet avec ajout de bruit. Pertinent pour la protection contre l’analyse de métadonnées réseau, avec un coût en latence selon le mode.

**O**

**OnionShare** — Outil de partage de fichiers via service onion temporaire.

**OPSEC (Operational Security)** — Discipline d’identification, contrôle et protection des indicateurs sensibles.

**OSINT (Open Source Intelligence)** — Collecte d’information via sources ouvertes.

**OSINT défensif** — Audit de soi-même par OSINT pour mesurer son exposition publique.

**P**

**Passkey** — Implémentation grand public de WebAuthn (clés cryptographiques remplaçant les mots de passe).

**Pegasus** — Spyware mercenaire de NSO Group, déployé contre journalistes, activistes, opposants.

**PGP / GPG** — Standard de chiffrement asymétrique pour email et fichiers.

**Phishing** — Tentative d’usurpation pour obtenir credentials ou exécution. Variantes : spear, whaling, smishing, vishing, quishing.

**Pluton (Microsoft)** — Coprocesseur de sécurité Microsoft intégré dans CPU récents.

**Post-compromise security (PCS)** — Capacité d’un protocole à se rétablir après compromission de clé.

**Predator** — Spyware mercenaire d’Intellexa/Cytrox, concurrent de Pegasus.

**Proton (Mail, Drive, VPN)** — Suite suisse de services E2EE par design.

**Pseudonymat** — Usage d’un nom de substitution stable. Distinct de l’anonymat.

**Q**

**Qubes OS** — OS basé Xen compartimentant chaque activité en VMs séparées.

**R**

**Recall (Microsoft)** — Fonctionnalité Windows 11 sur Copilot+ PCs, opt-in, capturant régulièrement l’écran et indexant le contenu par IA pour recherche ultérieure. Snapshots et index stockés localement, chiffrés et liés à la TEE. Controversée pour les implications privacy structurelles d’une telle base.

**Ring signature** — Primitive cryptographique de Monero pour masquer l’expéditeur.

**RGPD** — Règlement Général sur la Protection des Données (UE).

**RTB (Real-Time Bidding)** — Système d’enchères publicitaires en temps réel. Lorsqu’un utilisateur ouvre une page ou une application, des informations sur son profil publicitaire sont transmises à des annonceurs potentiels, qui enchérissent automatiquement pour afficher une publicité.

**S**

**Safety Numbers (Signal)** — Chaîne dérivée des clés permettant de vérifier l’identité d’un contact.

**Sandbox** — Isolement d’une application dans un environnement contrôlé (Flatpak, Firejail, Windows Sandbox).

**Sapin II** — Loi française de protection des lanceurs d’alerte (2016, modifiée 2022).

**Secure Boot** — Vérification cryptographique de la chaîne de démarrage UEFI.

**Secure Enclave** — Coprocesseur de sécurité Apple intégré aux SoC Apple Silicon.

**SecureDrop** — Plateforme open source pour soumission anonyme de documents aux rédactions.

**SELinux** — Modèle MAC sous Linux (Fedora, RHEL).

**SimpleX** — Messagerie E2EE sans identifiant utilisateur global.

**SIM swap** — Fraude consistant à faire transférer ta ligne sur la SIM d’un attaquant.

**Signal** — Référence E2EE, protocole open source audité, déployé à 100M+ utilisateurs.

**SNI (Server Name Indication)** — Extension TLS qui transmet en clair le nom de domaine joint.

**Snowflake** — Transport obfusqué Tor utilisant des proxys volontaires WebRTC.

**Spoofing** — Usurpation d’identité (catégorie STRIDE).

**Stalkerware** — Logiciel espion commercial visant le tracking de partenaires (mSpy, FlexiSpy).

**STRIDE** — Taxonomie de menaces sécurité (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege).

**Stylométrie** — Analyse statistique du style d’écriture pour identification d’auteur.

**Surface d’attaque** — Ensemble des points par lesquels un adversaire peut t’attaquer techniquement.

**Surface d’exposition** — Ensemble des informations collectables sur toi sans attaque.

**Surveillance, capitalisme de** — Cf. capitalisme de surveillance.

**T**

**Tails** — OS live amnésique routant tout via Tor.

**Threat model** — Modèle structuré décrivant actifs, adversaires, mesures.

**TLS (Transport Layer Security)** — Protocole de chiffrement en transit, base de HTTPS.

**Tor** — Réseau d’anonymisation par routage en oignon à trois sauts.

**TOTP (Time-based One-Time Password)** — Code MFA généré par algorithme synchronisé en temps (Authenticator apps).

**TPM (Trusted Platform Module)** — Coprocesseur de sécurité pour stockage de clés et mesure de boot.

**Truecaller** — Service tiers révélant les identités derrière numéros de téléphone (intrusif).

**V**

**Vanadium** — Navigateur intégré à GrapheneOS, Chromium durci.

**Vault qube** — Qube Qubes offline pour secrets (gestionnaire de mots de passe, clés PGP).

**Vault7 (Wikileaks)** — Fuite de capacités CIA (2017), illustre capacités étatiques.

**VeraCrypt** — Conteneur chiffré portable, héritier de TrueCrypt.

**Vishing** — Phishing par appel vocal.

**VLAN (Virtual LAN)** — Segmentation réseau logique.

**VPN (Virtual Private Network)** — Tunnel chiffré vers serveur distant.

**Vulnerability** — Faiblesse exploitable d’un système.

**W**

**Wayland** — Protocole de gestion d’affichage Linux remplaçant X11, avec isolation des fenêtres.

**WebAuthn** — Standard d’authentification web cryptographique.

**Whaling** — Spear phishing visant un dirigeant.

**Whonix** — OS d’anonymisation Tor en architecture Gateway/Workstation.

**WireGuard** — Protocole VPN moderne, rapide, compact.

**Y**

**Yellow dots** — Micro-points jaunes invisibles imprimés par imprimantes couleur pour tracking forensique.

**YubiKey** — Clé matérielle FIDO2 / WebAuthn / OpenPGP.

**Z**

**Zed!** — Conteneur chiffré francophone, secteur public/justice.

**Zero-click** — Exploit nécessitant aucune interaction utilisateur (typique des spywares mercenaires sur iMessage, WhatsApp).

**Zero-day** — Vulnérabilité non publique, sans patch disponible.

-----

### Annexe 2 — Cheat sheets opérationnels

#### 2.1 Audit initial en 90 minutes

1. HaveIBeenPwned : emails principaux + numéros de téléphone.
1. Google / Bing / DuckDuckGo : recherche nom complet, email, pseudos.
1. Sherlock ou WhatsMyName : recherche pseudonymes.
1. Reverse image (Yandex, Google Lens) sur photos publiques.
1. Audit Google Account → Sécurité (sessions, MFA, récupération).
1. Audit Apple ID → Appareils.
1. Audit iCloud → ADP activée ? Backup E2EE ?
1. Audit permissions mobiles (Localisation, Micro, Caméra, Photos, Contacts).
1. Audit gestionnaire de mots de passe : doublons, faibles, sans MFA.
1. Liste des comptes critiques sans MFA matériel.

#### 2.2 Préparation manifestation

- Téléphone dédié GrapheneOS, profil manifestation, BFU avant départ.
- Code de déverrouillage 8 chiffres, biométrie désactivée.
- Faraday bag dans le sac.
- Numéros importants sur papier.
- Téléphone perso vraiment éteint chez soi.
- 100 € cash + CB prépayée.
- Pas de carte d’identité contenant adresse précise inutile.

#### 2.3 Préparation voyage frontalier sensible

- Burner device (ou device durci, ADP, Lockdown Mode, FileVault).
- Données sensibles évacuées en cloud E2EE (Proton Drive).
- Sessions critiques révoquées.
- BFU absolu avant passage frontière.
- Photos macro des composants internes pour comparaison retour.
- Vis vernies pour détection d’intrusion physique.

#### 2.4 Réception document sensible

1. Vérifier provenance (Safety Numbers, canal authentifié).
1. Hash SHA-256 confirmé hors bande.
1. Environnement isolé (Tails ou dispVM).
1. Dangerzone pour PDF.
1. ExifTool / MAT2 pour métadonnées.
1. Archivage chiffré.

#### 2.5 Compte compromis suspecté

1. Mot de passe changé depuis appareil sain.
1. Toutes sessions actives révoquées.
1. Audit modifications récentes (mail récup, MFA, filtres).
1. MFA matériel activé.
1. Comptes liés vérifiés.
1. Communication aux contacts si phishing envoyé.
1. Plainte si dommages.

#### 2.6 Spyware mercenaire suspecté

1. Mode avion immédiat + faraday bag.
1. Ne pas redémarrer (perte d’IOC).
1. Access Now Digital Security Helpline.
1. Sauvegarde locale (iTunes/Quicktime).
1. Soumission MVT et Citizen Lab.
1. Appareil neuf, comptes audités, threat model révisé.

#### 2.7 Sauvegarde 3-2-1 minimale

- Disque local (chiffré).
- Cloud E2EE (Proton Drive, Tresorit, ou chiffré côté client).
- Externe en lieu sûr (chez avocat, parent, coffre).
- Test de restauration trimestriel.

-----

### Annexe 3 — Matrice d’outils de référence (2025-2026)

#### Communication

|Outil             |Type               |Usage                 |Notes                                               |
|------------------|-------------------|----------------------|----------------------------------------------------|
|**Signal**        |Messagerie E2EE    |Quotidien             |Référence. Username permet de ne plus exposer numéro|
|**SimpleX**       |Messagerie E2EE    |Sources, HVT          |Pas d’identifiant utilisateur global                |
|**Briar**         |Messagerie P2P     |Manifestation, offline|Bluetooth/Tor, sans serveur                         |
|**iMessage**      |E2EE (Apple)       |Quotidien Apple       |Contact Key Verification recommandée                |
|**Matrix/Element**|Fédéré             |Communautés           |E2EE optionnelle, métadonnées chez homeserver       |
|**WhatsApp**      |E2EE (Meta)        |Compatibilité large   |Métadonnées chez Meta. Sauvegarde E2EE à activer    |
|**Telegram**      |Pas E2EE par défaut|Diffusion             |Seuls Secret Chats E2EE                             |

#### Email

|Outil                    |Type                       |Notes                             |
|-------------------------|---------------------------|----------------------------------|
|**Proton Mail**          |E2EE entre Proton          |Suisse. Alias SimpleLogin intégrés|
|**Tuta**                 |E2EE complet (objet inclus)|Allemagne. Pas d’IMAP             |
|**Mailbox.org**          |Email propre + PGP         |Allemagne                         |
|**Fastmail**             |Mail propre sans E2EE      |Australie (Five Eyes)             |
|**SimpleLogin / Addy.io**|Alias email                |À ajouter en front de tout        |

#### Navigateurs

|Outil                          |Usage                                |
|-------------------------------|-------------------------------------|
|**Tor Browser**                |Anonymat (ne jamais modifier)        |
|**Mullvad Browser**            |Anti-fingerprint quotidien (sans Tor)|
|**Brave**                      |Quotidien Chromium durci             |
|**Firefox + uBlock + arkenfox**|Quotidien Firefox durci              |
|**LibreWolf**                  |Firefox durci pré-configuré          |
|**Vanadium**                   |Mobile GrapheneOS                    |

#### VPN

| Outil                               | Usage principal                                      | Notes                                                                                                                                                    |
| ----------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mullvad VPN**                     | Privacy quotidienne                                  | Suède. Compte numéroté sans email. Paiement cash/Monero possible. No-log détaillé. Très bon choix par défaut.                                            |
| **IVPN**                            | Privacy quotidienne                                  | Gibraltar. Audits réguliers. Cure53. Très bon positionnement privacy.                                                                                    |
| **Proton VPN**                      | Privacy + confort                                    | Suisse. Bon compromis grand public, écosystème Proton, plan gratuit sérieux.                                                                             |
| **NymVPN**                          | Métadonnées / mixnet                                 | VPN décentralisé. Fast mode 2-hop, Anonymous mode 5-hop mixnet. Plus ambitieux contre l’analyse de trafic, mais plus jeune et potentiellement plus lent. |
| **AmneziaVPN**                      | Anti-censure / self-host                             | Multi-protocoles. AmneziaWG, XRay Reality, Shadowsocks, OpenVPN over Cloak. Très pertinent contre DPI et blocage VPN.                                    |
| **À éviter pour profils sensibles** | NordVPN/ExpressVPN pour HVT, VPN gratuits, Surfshark | Risque de logs, revente de données, juridiction opaque, propriété complexe.                                                                              |

#### Gestionnaires de mots de passe

|Outil          |Notes                                                          |
|---------------|---------------------------------------------------------------|
|**Bitwarden**  |Open source. Audits réguliers. Vaultwarden self-hosted possible|
|**KeePassXC**  |100 % local, sync manuelle                                     |
|**1Password**  |Commercial canadien. UX excellent                              |
|**Proton Pass**|Intégré Proton                                                 |
|**À éviter**   |LastPass (fuites 2022-2023)                                    |

#### Clés matérielles

|Outil               |Notes                           |
|--------------------|--------------------------------|
|**YubiKey 5 series**|Référence commerciale           |
|**Nitrokey 3**      |Open source hardware (Allemagne)|
|**SoloKey**         |Open source plus militant       |

#### Cloud E2EE

|Outil                      |Notes                               |
|---------------------------|------------------------------------|
|**Proton Drive**           |Suisse, E2EE par design             |
|**Tresorit**               |Suisse, focalisé pro                |
|**Mega**                   |Nouvelle-Zélande                    |
|**Cryptomator**            |Surcouche E2EE sur cloud generaliste|
|**Nextcloud + Cryptomator**|Self-hosted                         |

#### OS sensible

|Outil         |Usage                        |
|--------------|-----------------------------|
|**Tails**     |Sessions ponctuelles anonymes|
|**Whonix**    |Anonymat Tor persistant      |
|**Qubes OS**  |Compartimentation forte      |
|**GrapheneOS**|Mobile durci sur Pixel       |
|**Kicksecure**|Debian durcie au démarrage   |

#### Détection / monitoring

|Outil             |Notes                                 |
|------------------|--------------------------------------|
|**MVT**           |Détection Pegasus/Predator post-mortem|
|**iVerify**       |Monitoring iOS/Android au quotidien   |
|**HaveIBeenPwned**|Notifications de fuites               |
|**Exodus Privacy**|Audit trackers d’apps Android         |

#### Métadonnées et fichiers

|Outil         |Notes                                 |
|--------------|--------------------------------------|
|**MAT2**      |Nettoyage automatique métadonnées     |
|**ExifTool**  |Référence lecture/écriture métadonnées|
|**Dangerzone**|Reconstruction PDF propre             |

#### Partage de fichiers

|Outil             |Notes                   |
|------------------|------------------------|
|**OnionShare**    |Service onion temporaire|
|**SecureDrop**    |Plateforme rédactions   |
|**GlobaLeaks**    |Équivalent ONG          |
|**CryptPad**      |Suite collaborative E2EE|
|**Bitwarden Send**|Lien temporaire chiffré |

-----

### Annexe 4 — Matrices de décision

#### 4.1 Quelle messagerie pour quel usage ?

|Usage                         |Premier choix         |Second choix                                     |
|------------------------------|----------------------|-------------------------------------------------|
|Famille / amis grand public   |Signal                |iMessage (Apple) ou WhatsApp avec sauvegarde E2EE|
|Source journalistique sensible|SimpleX               |Signal avec username                             |
|Manifestation, offline        |Briar                 |Signal avec disappearing messages                |
|Équipe pro (ONG, rédaction)   |Signal                |Wire ou Matrix                                   |
|Profil ultra-HVT              |SimpleX sur GrapheneOS|Signal sur GrapheneOS avec username              |

#### 4.2 Quel environnement de session sensible ?

|Besoin                                       |Choix                        |
|---------------------------------------------|-----------------------------|
|Action ponctuelle, traces nulles             |Tails                        |
|Identité pseudonyme durable + anonymat réseau|Whonix                       |
|Séparation durable plusieurs activités       |Qubes OS                     |
|HVT avec tous les besoins                    |Qubes + Whonix               |
|Quotidien grand public durci                 |OS durci classique (Ch 14-15)|

#### 4.3 Quelle MFA ?

|Compte                                 |MFA recommandée                    |
|---------------------------------------|-----------------------------------|
|Email principal                        |FIDO2 matériel (YubiKey)           |
|Comptes financiers                     |FIDO2 matériel + TOTP secondaire   |
|Réseaux sociaux                        |FIDO2 ou TOTP                      |
|Comptes utilitaires (boutique en ligne)|TOTP                               |
|Services SMS-only                      |Tenter de migrer ou minimum d’usage|

#### 4.4 Quel chiffrement disque selon OS ?

|OS               |Chiffrement               |Notes                                 |
|-----------------|--------------------------|--------------------------------------|
|macOS            |FileVault                 |Activer dès première utilisation      |
|Windows          |BitLocker (Pro/Enterprise)|TPM + PIN si profil sensible          |
|Linux            |LUKS2                     |Argon2id, systemd-cryptenroll pour TPM|
|Multi-OS portable|VeraCrypt                 |Conteneurs portables                  |

#### 4.5 Quel cloud selon profil ?

|Profil                               |Recommandation                                 |
|-------------------------------------|-----------------------------------------------|
|Grand public Apple                   |iCloud + ADP activée                           |
|Grand public privacy                 |Proton Drive                                   |
|Cloud générique gardé pour écosystème|Cryptomator par-dessus                         |
|Self-hosting                         |Nextcloud + Cryptomator pour E2EE additionnelle|
|Profil pro très sensible             |Tresorit (Suisse, entreprise)                  |

#### 4.6 Quel routage réseau selon contexte ?

| Contexte                               | Choix                                                     |
| -------------------------------------- | --------------------------------------------------------- |
| Quotidien grand public                 | DNS chiffré (DoH/DoT) + + navigateur durci + uBlock       |
| Wi-Fi public                           | + VPN (Mullvad/IVPN)                                      |
| Recherche anonyme                      | Mullvad Browser sur VPN ou Tor Browser                    |
| Action anonyme                         | Tor Browser sur Tor seul                                  |
| Environnement bloquant (Iran, etc.)    | Tor avec bridges obfs4 ou Snowflake                       |
| HVT durable                            | Whonix sur Qubes                                          |
| Navigation privacy quotidienne         | Mullvad Browser + Mullvad VPN                             |
| Session source / journalisme sensible  | Tor Browser sur Tails ou Whonix                           |
| Réduction de métadonnées réseau        | NymVPN Anonymous mode                                     |
| Usage rapide avec routage décentralisé | NymVPN Fast mode                                          |
| Pays censuré / DPI agressif            | AmneziaVPN avec AmneziaWG, XRay Reality ou Cloak          |
| Self-host VPN personnel                | AmneziaVPN sur VPS                                        |
| HVT durable                            | Qubes + Whonix ; VPN seulement comme outil complémentaire |


-----

### Annexe 5 — Architectures de référence par profil (récapitulatif synthétique)

> Renvoi détaillé : Chapitre 38. Cette annexe en propose la forme synthétique tabulaire.

|Profil                            |Mobile                                 |Laptop                              |Stack messageries         |Email                            |VPN                     |OS sensible             |MFA                            |Spécificités                               |
|----------------------------------|---------------------------------------|------------------------------------|--------------------------|---------------------------------|------------------------|------------------------|-------------------------------|-------------------------------------------|
|**Particulier grand public durci**|iPhone + ADP, Lockdown Mode off        |macOS ou Win11 Pro + FDE            |Signal + WhatsApp E2EE    |Proton Mail + alias              |Mullvad ponctuel        |–                       |YubiKey                        |Routines mensuelles                        |
|**Journaliste freelance**         |Pixel + GrapheneOS dédié + iPhone perso|MacBook Pro + MacBook Air enquête   |SimpleX (sources) + Signal|Proton + alias + PGP             |Mullvad permanent       |Tails + Qubes possible  |YubiKey x2                     |Page contact confidentiel publique         |
|**Activiste manifestation**       |Pixel GrapheneOS burner                |Laptop classique perso (non emporté)|Signal + Briar            |Standard                         |Mullvad mobile          |–                       |TOTP                           |Faraday bag, BFU absolu, papier d’urgence  |
|**Dirigeant PME tech**            |iPhone Lockdown + GrapheneOS voyage    |MacBook + burner voyage             |Signal + iMessage CKV     |Pro corporate + perso Proton     |Mullvad                 |–                       |YubiKey x2 + 1Password Business|Procédure anti-BEC, formation équipe       |
|**Opposant politique exil**       |GrapheneOS strict                      |Qubes OS                            |Signal + SimpleX          |Proton via Tor                   |Mullvad + Tor           |Qubes + Whonix          |YubiKey                        |MVT/iVerify mensuel, documentation publique|
|**RSSI ONG terrain**              |iPhone ou Pixel selon contexte         |Qubes OS sur laptops équipe         |Signal Business + Wire    |Proton Drive Business ou Tresorit|Mullvad ou IVPN business|Qubes standardisé       |Clés matérielles équipe        |Formation continue, audits annuels         |
|**Victime ex-partenaire abusif**  |Téléphone neuf cash                    |Laptop neuf si possible             |Signal + Briar urgence    |Email neuf E2EE                  |Mullvad                 |–                       |YubiKey                        |Audit stalkerware, soutien associatif      |
|**HVT extrême**                   |GrapheneOS + reboot 2x/jour            |Qubes OS + air-gap                  |SimpleX + Signal          |Proton via Tor permanent         |Tor + VPN obfusqué      |Qubes + Whonix + air-gap|YubiKey                        |Forensique mensuelle, équipe juridique     |

-----

### Annexe 6 — Templates opérationnels

#### 6.1 Template — Threat model personnel

```
[DATE] — [VERSION X.Y]
À RELIRE À : [DATE + 3 MOIS]

QUI JE SUIS (CONTEXTE) :
- Profession :
- Contexte spécifique (enquête, engagement, mission, situation) :
- Profil HVT-ness honnête (oui / non / partiel) :

ACTIFS PRIORITAIRES (top 5) :
1.
2.
3.
4.
5.

ADVERSAIRES PLAUSIBLES (top 5, par probabilité × capacité × motivation) :
1. [Nom] | Capacité : | Motivation : | Méthodes typiques :
2.
3.
4.
5.

HORS PÉRIMÈTRE EXPLICITE :
- 
- 
- 

MESURES PRIORITAIRES ACTUELLES :
1.
2.
3.
4.
5.

POINTS D'ATTENTION (à surveiller) :
- 
- 

SIGNATURE :
```

#### 6.2 Template — Brief manifestation

```
[DATE] — [LIEU] — [HEURE DE DÉBUT]

CONTEXTE :
- Nature de la manifestation :
- Risques anticipés (interpellations, gaz, charges, présence drones) :
- Présence de presse :

ÉQUIPE (présents au brief) :
-
-
-

RÉFÉRENT :
- Personne désignée hors manif :
- Procédure d'alerte si silence > X heures :

HOTLINE JURIDIQUE :
- Numéro :
- Avocat de garde :

CHECKLIST PERSONNELLE :
[ ] Téléphone manif chargé, BFU, faraday bag
[ ] Téléphone perso laissé éteint chez soi
[ ] Papier avec numéros essentiels
[ ] Cash + CB prépayée
[ ] Vêtements anonymes
[ ] Lunettes / protection
[ ] Pas de document compromettant

CHECKLIST RETOUR :
[ ] Compter les présents
[ ] Communication référent OK
[ ] Téléphone non saisi
[ ] Si saisie : protocole brûlure
[ ] Audit appareils (si perquisition possible)
```

#### 6.3 Template — Plan IR personnel

```
PROCÉDURE D'INCIDENT — VERSION [X.Y] — [DATE]

CONTACTS D'URGENCE :
- Avocat : [nom, téléphone]
- Référent technique (si applicable) : 
- Famille de confiance :
- Association de soutien :
- Hotline crisis : Access Now Digital Security Helpline +1 888 414 0100

EN CAS DE TÉLÉPHONE PERDU / VOLÉ :
1. Localisation à distance via [iCloud / Google] : [étapes]
2. Effacement à distance si nécessaire
3. Opérateur : [numéro support pour bloquer SIM]
4. Comptes à révoquer en priorité : Apple / Google / Microsoft / banques / messageries
5. Plainte police (numéro IMEI fourni à l'opérateur — noté dans 1Password sous "Matériel")

EN CAS DE COMPTE COMPROMIS :
1. Mot de passe changé depuis [appareil sain — préciser lequel]
2. Sessions actives révoquées
3. Audit modifications (mail récup, MFA, filtres)
4. Comptes liés vérifiés
5. Communication aux contacts si nécessaire

EN CAS DE SPYWARE SUSPECTÉ :
1. Mode avion + faraday
2. NE PAS REDÉMARRER
3. Access Now Helpline
4. MVT / Citizen Lab

EN CAS DE DOXXING :
1. Captures + horodatages
2. Signalement plateformes
3. Évaluation menace physique
4. Avocat + plainte
5. Soutien : [association locale]

CODES DE RÉCUPÉRATION :
- Stockés : [coffre — où exactement]
- Apple ID : ____
- Google : ____
- Bitwarden : ____
- 2FA backup codes : ____
```

#### 6.4 Template — Audit trimestriel

```
TRIMESTRE [TX] — [DATE]

OSINT DÉFENSIF :
[ ] Recherche nom complet sur Google / Bing / DDG
[ ] HaveIBeenPwned sur emails principaux
[ ] Reverse image sur photo de profil
[ ] WhatsMyName sur pseudonymes
[ ] Data brokers nouveaux apparus

SÉCURITÉ COMPTES :
[ ] Audit sessions Google / Apple / Microsoft
[ ] Audit MFA sur 20 comptes critiques
[ ] Revue gestionnaire de mots de passe (doublons, faibles)
[ ] Codes de récupération à jour

APPAREILS :
[ ] Mises à jour OS et firmware
[ ] Intégrité physique des appareils (vis, photos comparatives)
[ ] Permissions mobiles auditées
[ ] Reboot complet

SAUVEGARDES :
[ ] Test de restauration mini (un fichier)
[ ] Cloud E2EE fonctionnel
[ ] Disque externe en lieu sûr OK
[ ] Sauvegarde immuable mensuelle OK

THREAT MODEL :
[ ] Toujours pertinent ?
[ ] Évolutions à acter ?

NOTES :
```

#### 6.5 Template — Page « comment me joindre confidentiellement »

```
COMMENT ME JOINDRE CONFIDENTIELLEMENT

Je travaille sur des dossiers parfois sensibles. Si vous souhaitez 
me contacter de manière sécurisée, voici les canaux que je vérifie :

1. SECUREDROP : [lien .onion]
   À utiliser via Tor Browser (https://torproject.org).
   Anonyme. Préféré pour transmission de documents.

2. SIGNAL : @username (pas de numéro de téléphone)
   Pour discussion préalable et coordination.
   Vérification : Safety Numbers à comparer.

3. EMAIL CHIFFRÉ : email@domain.org
   Clé PGP : [fingerprint] — disponible sur Keys.OpenPGP.org
   Pour échanges techniques.

4. SIMPLEX : Sur demande, je peux fournir un lien d'invitation.

Avant tout envoi de documents sensibles, contactez-moi d'abord 
pour que nous choisissions ensemble le canal adapté.

Précautions à prendre de votre côté :
- Ne pas utiliser un appareil professionnel pour me contacter.
- Considérer Tor Browser sur Tails pour confidentialité maximale.
- Ne jamais transmettre depuis un réseau de votre employeur.

Cette page est à jour au [date].
```

-----

### Annexe 7 — Cadre juridique comparé (FR / UE / US / UK / CH)

#### 7.1 Chiffrement personnel

|Pays  |Légalité usage       |Obligation déchiffrer     |Notes                                           |
|------|---------------------|--------------------------|------------------------------------------------|
|France|Oui (LCEN art. 30)   |Oui (CP 434-15-2)         |3 ans / 270 k€ refus                            |
|UE    |Oui                  |Variable par État         |Pas d’harmonisation                             |
|US    |Oui (constitutionnel)|5e amendement = protection|Biométrie vs code mémoire jurisprudence mouvante|
|UK    |Oui                  |Oui (RIPA s. 49)          |2 ans / 5 ans selon contexte                    |
|Suisse|Oui (Cst. art. 13)   |Non                       |Forte protection                                |

#### 7.2 Surveillance des communications

|Pays  |Cadre                                                 |Contrôle               |Spécificités                                         |
|------|------------------------------------------------------|-----------------------|-----------------------------------------------------|
|France|LRM 2015, ajustée 2017, 2021                          |CNCTR + Conseil d’État |Algorithmes prédictifs, géolocalisation temps réel   |
|UE    |E-Privacy Regulation (en cours), CJUE limite rétention|Cours nationales + CJUE|Plusieurs régimes nationaux retoqués                 |
|US    |FISA section 702, NSL                                 |FISC                   |Loi étrangers + extension citoyens                   |
|UK    |IPA 2016                                              |IPCO                   |« Snooper’s Charter », interception massive autorisée|
|Suisse|LRens 2016                                            |DDPS                   |Surveillance plus strictement encadrée               |

#### 7.3 Protection des journalistes / sources

|Pays  |Cadre                                |Notes                                                    |
|------|-------------------------------------|---------------------------------------------------------|
|France|Loi 4 janvier 2010 + dir. UE 2024    |Secret protégé sauf impératif prépondérant intérêt public|
|UE    |Directive 2024 (Media Freedom Act)   |Limite spyware contre journalistes                       |
|US    |Shield laws variables par État       |Pas de loi fédérale unifiée                              |
|UK    |Sources Protection (limited)         |RIPA peut être invoqué                                   |
|Suisse|Forte protection légale et culturelle|–                                                        |

#### 7.4 Anti-doxxing

|Pays  |Cadre                                                                          |
|------|-------------------------------------------------------------------------------|
|France|CP 226-1 (vie privée), 222-33-2-2 (harcèlement), loi 2022 (aggravation), PHAROS|
|UE    |Variable national. Digital Services Act 2024 (modération)                      |
|US    |Variable par État. Pas de loi fédérale spécifique                              |
|UK    |Malicious Communications Act, Online Safety Act 2023                           |
|Suisse|Atteinte à l’honneur et à la personnalité                                      |

#### 7.5 Lanceurs d’alerte

|Pays  |Cadre                                                                 |
|------|----------------------------------------------------------------------|
|France|Sapin II (2016, mod. 2022) — Maison des Lanceurs d’Alerte             |
|UE    |Directive 2019/1937                                                   |
|US    |Whistleblower Protection Act, sectorielle (Sarbanes-Oxley, Dodd-Frank)|
|UK    |PIDA 1998                                                             |
|Suisse|LWB (récente)                                                         |

#### 7.6 RGPD et droits utilisables

Articles RGPD invocables comme particulier dans l’UE/EEE :

- **Art. 15** : droit d’accès (demander quelle donnée détenue).
- **Art. 16** : droit de rectification.
- **Art. 17** : droit à l’effacement (« droit à l’oubli »).
- **Art. 18** : droit à la limitation du traitement.
- **Art. 20** : droit à la portabilité.
- **Art. 21** : droit d’opposition.
- **Art. 22** : droit de ne pas faire l’objet d’une décision automatisée.

Recours : autorité de contrôle nationale (CNIL en France), avec amendes croissantes pour violation.

#### 7.7 AI Act UE (2024/1689)

- **Article 5** : interdictions absolues (notation sociale, certaines reconnaissances biométriques en temps réel par autorités).
- **Article 6+** : régime des « systèmes à haut risque ».
- **Article 50** : obligation de marquage des contenus IA (deepfakes).
- Sanctions importantes pour fournisseurs.

#### 7.8 Spécificité française : LRM et CNCTR

Loi sur le renseignement (2015, ajustée 2017, 2021) :

- Cadre des techniques de renseignement (interceptions, géolocalisation, balisage, algorithmes).
- Commission nationale de contrôle (CNCTR) : avis consultatif.
- Conseil d’État : juridiction de recours.

Critiques persistantes : asymétrie entre capacités et contrôle effectif. Plusieurs décisions du Conseil constitutionnel et CEDH ont contraint des ajustements.

-----

### Annexe 8 — Cas célèbres d’échec OPSEC : leçons défensives

> **Méthode** : chaque cas est traité selon le format **Contexte / Chaîne d’erreurs OPSEC / Mécanismes de corrélation et attribution / Leçons défensives transposables / Renvois croisés**. Un encart « Ce que ce cas n’enseigne pas » corrige les sur-généralisations classiques quand pertinent.
> 
> **Cadre éditorial** : ces cas sont publics, documentés, judiciairement clos. Leur étude pédagogique est légitime. L’objectif est défensif : comprendre les mécanismes pour les neutraliser, pas reproduire les opérations sous-jacentes.

-----

#### Annexe 8.1 — Ross Ulbricht / Silk Road (2013)

**Contexte**

Ross Ulbricht, opérateur du marché noir Silk Road sous le pseudonyme « Dread Pirate Roberts », arrêté en octobre 2013 à la Glen Park Library de San Francisco par le FBI. Silk Road, marché Tor accessible via service onion, avait facilité de 2011 à 2013 des transactions illicites en Bitcoin pour estimé à plus d’un milliard de dollars. Condamné à perpétuité en 2015. Sa peine a été commuée en janvier 2025.

**Chaîne d’erreurs OPSEC**

1. **Réutilisation de pseudonyme entre identités** : « altoid » utilisé en mars 2011 sur le forum Bitcoin Talk pour promouvoir Silk Road, *avant* qu’Ulbricht ne devienne « Dread Pirate Roberts ». Le pseudo « altoid » avait été utilisé peu de temps avant sur des forums de magic mushrooms.
1. **Email civil rattaché à un compte technique** : sur un forum Stack Overflow, Ulbricht a posé une question technique liée à Silk Road (en omettant ce contexte) sous son pseudonyme. Mais il a corrigé son post sous son nom réel `rossulbricht@gmail.com` peu après.
1. **OPSEC physique défaillante** : ordinateur portable ouvert et déverrouillé au moment de l’arrestation (par tactique du FBI qui a créé une diversion à la bibliothèque, des agents l’ont saisi en flagrant état AFU).
1. **Documentation incriminante non chiffrée** : journaux personnels, listes de tâches détaillées sur les opérations Silk Road, conservés en clair sur son ordinateur.
1. **Mauvaise hygiène des transactions** : commande de fausses pièces d’identité livrées à son adresse réelle pour tester un fournisseur.
1. **Confidences à des contacts** : conversations confidentielles avec des associés (dont des informateurs FBI infiltrés).

**Mécanismes de corrélation et attribution exploités**

Le FBI et la DEA ont remonté à Ulbricht non par un cassage de Tor mais par chaînage de signaux :

- Recherche du pseudonyme « altoid » sur Google par l’agent IRS Gary Alford → premiers posts retrouvés.
- Corrélation altoid/Stack Overflow → adresse Gmail réelle.
- Surveillance physique → identification.
- Saisie en AFU → accès complet aux journaux et clés.

Tor a tenu techniquement. L’OPSEC humaine et applicative a cédé sur six points indépendants.

**Leçons défensives transposables**

1. **Compartimentation absolue** entre identités. Un pseudonyme ne doit jamais croiser un identifiant civil (Ch 9). « Une seule erreur suffit. »
1. **Documentation chiffrée** systématique. Pas de journal d’opérations en clair (Ch 12).
1. **Ne pas tenir l’appareil sensible en AFU** dans un lieu public. BFU avant tout déplacement (Ch 12.8).
1. **Audit régulier de réutilisation de pseudonyme** via WhatsMyName / Sherlock (Ch 5).
1. **Minimalisme dans la confidence** : need-to-know strict (Ch 1.5).

**Ce que ce cas n’enseigne pas**

- ❌ « Tor est cassé. » Faux. Tor a tenu. Ce sont les erreurs applicatives qui ont fait tomber Ulbricht.
- ❌ « Bitcoin est anonyme et a permis Silk Road. » Faux. Bitcoin n’a jamais été anonyme. Les analyses de chaîne ont contribué à l’enquête.

**Renvois croisés** : Ch 1 (concepts), Ch 5 (OSINT défensif), Ch 9 (compartimentation), Ch 12 (chiffrement disque et BFU/AFU), Ch 21 (Tor OPSEC), Ch 32 (cryptomonnaies traçables).

-----

#### Annexe 8.2 — Eldo Kim / Harvard bomb threat (2013)

**Contexte**

Eldo Kim, 20 ans, étudiant à Harvard, envoie le 16 décembre 2013 une fausse alerte à la bombe via le service email anonyme Guerrilla Mail à l’administration de Harvard, dans le but de différer un examen final pour lequel il était mal préparé. Identifié et arrêté en quelques heures. A plaidé coupable. A bénéficié d’un sursis.

**Chaîne d’erreurs OPSEC**

1. **Usage de Tor depuis le réseau Harvard** : Kim a utilisé Tor depuis le Wi-Fi du campus. Or il était le **seul utilisateur de Tor sur le réseau Harvard à ce moment précis**.
1. **Coïncidence temporelle évidente** : l’envoi du mail anonyme correspondait exactement à la fenêtre de la connexion Tor.
1. **Identification par registre WPA d’authentification** : Harvard a corrélé les logs WPA enterprise (qui exigeaient login étudiant) avec les logs de session Tor sortant.

**Mécanismes de corrélation et attribution exploités**

Le mail a été envoyé via Guerrilla Mail à travers Tor. Les en-têtes du mail indiquaient l’IP du nœud de sortie Tor, comme prévu. Mais Harvard, en examinant ses propres logs réseau, a identifié quel(s) utilisateur(s) avai(en)t utilisé Tor pendant la fenêtre pertinente. Un seul étudiant : Kim. Confrontation rapide, aveux.

**Leçons défensives transposables**

1. **Tor protège contre l’observation à distance, mais pas contre la corrélation locale**. Si tu utilises Tor depuis un réseau qui peut t’identifier individuellement, le bénéfice est nul.
1. **Bridges et Snowflake** pour environnements où l’usage de Tor lui-même est observable et incriminant (Ch 21.3).
1. **Diversification des points de sortie** : ne pas utiliser Tor depuis chez soi pour activité dont la fenêtre est unique et identifiable.
1. **Ne pas faire d’OPSEC pour des actes illégaux** : ce cas illustre aussi qu’au-delà de la technique, l’opération elle-même était mal pensée — une fausse alerte n’a aucune justification, et le seul utilisateur Tor sur un réseau spécifique est trivialement identifiable.

**Renvois croisés** : Ch 21 (Tor OPSEC), Ch 9 (compartimentation horaires).

-----

#### Annexe 8.3 — Hector Monsegur / « Sabu » / LulzSec (2011)

**Contexte**

Hector Xavier Monsegur, alias « Sabu », figure centrale du collectif hacktiviste LulzSec et co-fondateur d’AntiSec. Identifié par le FBI en juin 2011, retourné comme informateur, a coopéré pendant plusieurs mois pour identifier d’autres membres du collectif (Jeremy Hammond entre autres).

**Chaîne d’erreurs OPSEC**

1. **Connexion à IRC sans Tor depuis IP domestique** : à une occasion, Sabu s’est connecté à un serveur IRC où LulzSec se coordonnait sans utiliser Tor. Son adresse IP réelle (NYC, immeuble HLM) a été enregistrée dans les logs IRC.
1. **Mauvaise hygiène opérationnelle** : utilisation de Twitter sous le pseudo Sabu pour communications publiques, occasionnellement croisé avec des éléments traçables.
1. **Identification croisée** : informations personnelles cohérentes à travers plusieurs sessions, dont une mention de famille reconnaissable.

**Mécanismes de corrélation et attribution exploités**

Le FBI surveillait IRC. La connexion non-Tor a fourni l’IP. Identification rapide via l’opérateur. Surveillance physique pour confirmation. Arrestation et retournement.

**Leçons défensives transposables**

1. **Une seule erreur ponctuelle suffit**. La compartimentation absolue ne tolère pas l’exception « juste cette fois » (Ch 9.6).
1. **Automatiser pour empêcher l’erreur** : configurer le client IRC pour refuser toute connexion non-Tor (proxy système, killswitch).
1. **Threat model honnête** : si tu es publiquement engagé dans des activités illégales (par exemple ici, intrusions), tu es structurellement vulnérable. La discipline OPSEC ne compense pas un threat model irréaliste.

**Renvois croisés** : Ch 9 (compartimentation), Ch 20 (VPN/killswitch), Ch 21 (Tor OPSEC).

-----

#### Annexe 8.4 — Paul Le Roux (2012)

**Contexte**

Paul Calder Le Roux, programmeur sud-africain originaire de Rhodésie, ancien créateur du logiciel de chiffrement E4M (puis TrueCrypt), opérait à partir des années 2000 une organisation criminelle internationale impliquée dans trafic de drogue, armes, et homicides commandités. Arrêté à Monrovia (Liberia) en septembre 2012 dans le cadre d’une opération de la DEA, retourné comme informateur, a permis l’arrestation de plusieurs collaborateurs.

**Chaîne d’erreurs OPSEC**

1. **Compartimentation insuffisante** entre la facette légale (entrepreneur informatique) et la facette criminelle (commerce de méthamphétamine, armes).
1. **Confidences à des associés** dont certains ont été retournés ou ont coopéré.
1. **Mouvements financiers traçables** : malgré l’usage de société offshore et de transferts informels, des traces ont permis aux enquêteurs de remonter.
1. **Géographie compromise** : présence régulière dans certaines juridictions où la DEA opérait (Philippines, Liberia).

**Mécanismes de corrélation et attribution exploités**

Coopération internationale entre DEA et services locaux. Témoins-clés retournés. Surveillance physique. L’opération s’étend sur années — l’OPSEC sur la durée est exponentiellement plus difficile que pour un acte ponctuel.

**Leçons défensives transposables**

Le cas Le Roux est éducatif principalement sur les **limites de l’OPSEC face à un threat model lourd dans la durée** :

1. **L’OPSEC ne compense pas un threat model intenable** : si on a comme adversaires des services de police internationale motivés et coopérants, sur une décennie, la probabilité d’échec tend vers 1.
1. **Le facteur humain reste le maillon faible** : les associés finissent souvent par coopérer.
1. **Compartimentation des facettes de vie** : c’est applicable à des contextes légitimes (journaliste-source, activiste-vie civile) qui empruntent les mêmes mécaniques sans la dimension illégale.

**Ce que ce cas n’enseigne pas**

- ❌ « TrueCrypt est compromis. » Faux. Le Roux a été l’un des programmeurs initiaux d’E4M (prédécesseur), mais cela n’a aucune implication pour la sécurité de TrueCrypt/VeraCrypt actuel.

**Renvois croisés** : Ch 1 (limites), Ch 9 (compartimentation), Ch 35 (OPSEC humaine).

-----

#### Annexe 8.5 — Reality Winner / Yellow dots (2017)

**Contexte**

Reality Leigh Winner, analyste de renseignement pour la NSA (sous contrat avec Pluribus International), a transmis en mai 2017 au média *The Intercept* un document classifié top-secret concernant des opérations cybernétiques russes contre les élections américaines de 2016. Arrêtée le 3 juin 2017, condamnée à 5 ans et 3 mois.

**Chaîne d’erreurs OPSEC**

1. **Impression du document sensible sur l’imprimante de son employeur** : laisser des traces forensiques imprimées (Machine Identification Code — yellow dots).
1. **Photographie ou scan du document imprimé** : transmise à The Intercept telle quelle, sans nettoyage des yellow dots.
1. **The Intercept a publié le document avec ses yellow dots intacts** sur leur site, permettant à toute personne d’extraire les métadonnées (identifiant d’imprimante, date, heure).
1. **Audit interne NSA rapide** : l’imprimante avait été utilisée par 6 personnes, dont Reality Winner. Croisement avec ses logs d’email récents (elle avait communiqué avec The Intercept), arrestation.

**Mécanismes de corrélation et attribution exploités**

Le **Machine Identification Code** (MIC) est un système de marquage par micro-points jaunes presque invisibles, généré par la quasi-totalité des imprimantes couleur professionnelles depuis ~2000. Les yellow dots encodent :

- Numéro de série de l’imprimante.
- Date et heure d’impression.

Documenté par l’EFF dès 2005, mais largement ignoré par le public.

**Leçons défensives transposables**

1. **Ne pas imprimer un document à publier** depuis une imprimante traçable (Ch 31.6).
1. **Re-générer le PDF depuis le texte plutôt que scanner un document imprimé** : élimine yellow dots et métadonnées originales.
1. **Audit des métadonnées avant publication** : ExifTool, MAT2, Dangerzone (Ch 31.7, 31.8).
1. **Responsabilité de la rédaction** : The Intercept a partagé un document non nettoyé, contribuant directement à l’identification. Procédures rédactionnelles à durcir, voir SecureDrop avec workflow approprié (Ch 28.2).

**Ce que ce cas n’enseigne pas**

- ❌ « Les imprimantes sont compromises et inutilisables. » Faux. Pour usage banal, les yellow dots sont sans importance. C’est dans le contexte d’une publication anonyme qu’ils deviennent critiques.

**Renvois croisés** : Ch 28 (partage sécurisé), Ch 31 (métadonnées et yellow dots), Ch 37 (cadre lanceurs d’alerte).

-----

#### Annexe 8.6 — John McAfee / EXIF Vice photo (2012)

**Contexte**

John McAfee, fondateur de l’antivirus éponyme, fuyait depuis le Belize après être soupçonné dans le meurtre de son voisin Gregory Faull (novembre 2012). En décembre 2012, Vice Magazine publie une photo de McAfee prise par un journaliste avec son iPhone. La photo contient les métadonnées EXIF GPS intactes, révélant la localisation précise au Guatemala. McAfee est arrêté par les autorités guatémaltèques dans les jours qui suivent. (Il s’est ultérieurement suicidé en prison en Espagne en 2021.)

**Chaîne d’erreurs OPSEC**

1. **EXIF GPS activé sur l’iPhone du journaliste**.
1. **Publication de la photo sans audit des métadonnées** par Vice.
1. **McAfee, lui-même célèbre pour son passé sécurité, n’a pas vérifié l’OPSEC de son interlocuteur journaliste**.

**Mécanismes de corrélation et attribution exploités**

Trivial. Tout utilisateur curieux pouvait télécharger la photo et lire les EXIF avec n’importe quel outil (ExifTool, ou simplement le clic-droit Propriétés sur Windows). Coordonnées GPS → localisation McAfee.

**Leçons défensives transposables**

1. **EXIF avant publication, toujours**. Vérifier avec ExifTool ou MAT2 (Ch 31.2).
1. **Audit du collaborateur** : ton OPSEC ne dépend pas que de toi. Si tu accordes une interview, vérifier ce que le journaliste va publier, demander à voir avant.
1. **Plateformes professionnelles** retirent généralement EXIF côté serveur (Instagram, Facebook, Twitter), mais beaucoup de petits sites et magazines ne le font pas. Ne pas présumer.

**Renvois croisés** : Ch 31 (métadonnées EXIF), Ch 35 (OPSEC humaine, entourage).

-----

#### Annexe 8.7 — Patron du Drug Enforcement (DOJ insider, 2015-2018)

**Contexte agrégé**

Plusieurs cas, anonymisés par regroupement, d’insiders DOJ/DEA/agences fédérales US ayant vendu des informations à des cartels ou à la criminalité organisée entre 2015 et 2018. Identifiés par audits internes croisant accès aux bases de données et patterns de consultations inhabituelles (queries sur des cibles sans dossier ouvert correspondant), corrélés avec mouvements financiers personnels suspects.

**Chaîne d’erreurs OPSEC commune**

1. **Consultations de bases internes pour des intérêts personnels** sans dossier officiel ouvert (laisse trace forensique sur les logs).
1. **Communications opérationnelles** avec contacts criminels via canaux non maîtrisés (téléphones personnels, comptes mail civils).
1. **Mouvements financiers** détectables (déclarations fiscales incohérentes, achats luxueux).
1. **Imprudences sociales** : confidences à proches, ostentation.

**Mécanismes de corrélation et attribution exploités**

Audit interne automatisé par les agences elles-mêmes, croisé avec analyses financières (FinCEN). UEBA (User and Entity Behavior Analytics).

**Leçons défensives transposables (légitimes)**

Cette série de cas n’a pas de transposition défensive directe pour un usage légitime. Elle est mentionnée pour rappel :

1. **Les organisations modernes monitor leurs employés** sur les accès aux données sensibles. Un salarié légitime ne peut pas masquer une consultation inhabituelle à terme.
1. **Pour un journaliste qui travaille avec un lanceur d’alerte interne d’une telle agence** : la fenêtre d’opportunité pour la source est courte. Procédures rapides, minimisation des traces, soutien légal avant divulgation.

**Renvois croisés** : Ch 37 (cadre lanceurs d’alerte, Sapin II).

-----

#### Annexe 8.8 — Cas Roman Storm / Tornado Cash (2023-2024)

**Contexte**

Roman Storm, co-développeur de Tornado Cash (un *mixer* Ethereum d’anonymisation), arrêté en août 2023 par les autorités américaines pour conspiration de blanchiment et violation de sanctions. Procès en 2024-2025.

**Particularité du cas**

Ce cas n’est pas un échec d’OPSEC personnelle au sens strict — Roman Storm vivait ouvertement et publiquement. C’est un cas d’**incertitude juridique du développeur d’outils privacy**.

**Leçons (juridiques, pas techniques)**

1. **Les développeurs d’outils privacy/anonymat opèrent dans une zone légale qui peut être contestée**, particulièrement aux États-Unis où le rattachement à des opérations sanctionnées (OFAC) peut entraîner des poursuites.
1. **Distinction code vs opération** : la défense Storm argumente que Tornado Cash est code open source publié, sans intermédiation active. La poursuite argumente qu’il y avait gestion opérationnelle.
1. **Implications pour les utilisateurs** : un service technique disponible aujourd’hui peut être sanctionné demain. Pour usages légitimes (don anonyme à un journaliste, par exemple), considérer cette volatilité juridique.

**Renvois croisés** : Ch 32 (cryptomonnaies), Ch 37 (cadre juridique).

-----

### Annexe 9 — Ressources, formations, communautés

#### 9.1 Documentation de référence (anglais)

- **EFF Surveillance Self-Defense** (https://ssd.eff.org) : référence pédagogique, threat modeling, guides par profil.
- **Privacy Guides** (https://privacyguides.org) : outils recommandés, philosophie, guides techniques.
- **The Practical Guide to Threat Modeling** (Adam Shostack) : pour profils techniques.
- **NIST SP 800-63 (Digital Identity Guidelines)** : authentification.
- **The Hitchhiker’s Guide to Online Anonymity** (AnonyPla) : ressource exhaustive sur l’anonymat, à utiliser avec recul critique.

#### 9.2 Documentation francophone

- **CNIL** (https://cnil.fr) : RGPD, droits, guides.
- **ANSSI** (https://ssi.gouv.fr) : guides cyber, recommandations.
- **La Quadrature du Net** (https://laquadrature.net) : veille libertés numériques en France.
- **Nothing2Hide** (https://nothing2hide.org) : formation journalistes / activistes francophones.
- **Bortzmeyer, blog** : technique réseau, DNS, Internet (https://www.bortzmeyer.org).
- **CECIL** (https://lececil.org) : libertés et internet.

#### 9.3 Organisations de soutien aux journalistes et sources

- **Reporters sans frontières (RSF)** : guide journaliste, hotline sécurité numérique.
- **Committee to Protect Journalists (CPJ)** : Digital Safety Kit, formations.
- **Forbidden Stories** : continuité d’enquêtes en cas de blocage.
- **Freedom of the Press Foundation (FPF)** : SecureDrop, Dangerzone, formations.
- **Global Investigative Journalism Network (GIJN)** : ressources investigation.
- **Tactical Tech** : Data Detox, formation activistes/journalistes.

#### 9.4 Organisations de soutien activistes et défenseurs

- **Access Now Digital Security Helpline** (+1 888 414 0100, https://accessnow.org/help) : assistance gratuite 24/7 pour profils à risque (journalistes, activistes, défenseurs droits humains).
- **Front Line Defenders** : protection physique et numérique des défenseurs.
- **EFF** (https://eff.org) : litiges stratégiques, ressources.
- **La Quadrature du Net** : recours juridiques France.
- **Privacy International** : recherche et litiges UK/international.

#### 9.5 Soutien lanceurs d’alerte (France)

- **Maison des Lanceurs d’Alerte** (https://mlalerte.org) : accompagnement juridique, psychologique, pratique.
- **Défenseur des droits** : autorité administrative pour signalements externes.
- **Whistleblower Network News** : ressources internationales.

#### 9.6 Soutien victimes violences conjugales et stalkerware

- **Coalition Against Stalkerware** (https://stopstalkerware.org) : ressources, outils, partenaires.
- **France : 3919** (numéro national violences conjugales).
- **CIDFF** (Centres d’information sur les droits des femmes et des familles).
- **Solidarité Femmes** (réseau associatif).
- **EFF Surveillance Self-Defense, section « Domestic Abuse Survivors »**.

#### 9.7 Analyse forensique mobile suspicion spyware

- **Citizen Lab** (Université de Toronto, https://citizenlab.ca) : recherche et analyse forensique, soumission de cas via Access Now.
- **Amnesty Security Lab** : recherches Pegasus, Predator. MVT outil officiel (https://github.com/mvt-project/mvt).
- **iVerify** (commercial) : application Android/iOS de monitoring.

#### 9.8 Communautés et apprentissage

- **r/privacy, r/privacytoolsIO, r/qubes, r/Tor (Reddit)** : discussions techniques (modération variable).
- **Privacy Guides forum** : technique, modéré.
- **Tor mailing-lists** : pour profils techniques.
- **Local CryptoParties** : ateliers d’initiation locaux, mouvement international.
- **Tactical Tech, Internews, Open Briefing** : formations professionnelles.

#### 9.9 Lectures pour aller plus loin

**Techniques** :

- Bruce Schneier, *Secrets and Lies*, *Data and Goliath*.
- Adam Shostack, *Threat Modeling: Designing for Security*.

**Sociologiques / politiques** :

- Shoshana Zuboff, *The Age of Surveillance Capitalism*.
- Glenn Greenwald, *No Place to Hide*.
- Bruce Schneier, *Click Here to Kill Everybody*.

**Reportages / enquêtes** :

- *Pegasus Project* (Forbidden Stories + 17 médias, 2021).
- *Predator Files* (Mediapart + EIC, 2023).

**Histoire** :

- Steven Levy, *Crypto: How the Code Rebels Beat the Government — Saving Privacy in the Digital Age*.
- David Kahn, *The Codebreakers*.

-----

> 🟩 **Mot final**
> 
> La sécurité parfaite n’existe pas. La sécurité *suffisante pour ton threat model, soutenable dans le temps*, est atteignable.
> 
> Ce cours t’a appris à raisonner. Les outils changeront, les protocoles évolueront, les adversaires se transformeront. Le raisonnement, lui, dure.
> 
> Trois principes à retenir au-delà de tous les chapitres :
> 
> 1. **Threat model d’abord, outil ensuite.** Toujours.
> 1. **Compartimentation et minimisation** sont plus puissantes que tout outil magique.
> 1. **Durer**. Une posture brillante trois semaines puis abandonnée vaut moins qu’une posture moyenne tenue dix ans.
> 
> Bonne route.

-----

*Fin du cours.*

*Version 1.0 — Manuel collectif, mis à jour 2025-2026. Pour signaler une erreur, suggérer un complément, contribuer : voir page de contact.*

*Le cours est diffusé sous licence Creative Commons BY-NC-SA 4.0. Reproduction libre à condition de citer la source, sans usage commercial, et de partager dans les mêmes conditions.*
