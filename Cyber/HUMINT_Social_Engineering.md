# HUMINT et Social Engineering — Élicitation, manipulation et contre-ingénierie sociale

**Cours de référence — Niveau expert opérationnel**
**Version 2025-2026**

---

> **Positionnement dans la bibliothèque**
> Le cours *Cybersécurité du quotidien* traite le social engineering du point de vue de la victime (reconnaître, se protéger). Le cours *Intelligence économique* traite l'HUMINT d'entreprise légal (salons, debriefing). Le présent cours adopte le prisme méthodologique complet du praticien — red teamer, testeur d'intrusion physique, analyste en contre-ingénierie sociale, enquêteur — avec la dimension offensive (techniques) ET défensive (détection, formation, résilience).

---

## Table des matières

**PARTIE I — FONDATIONS**
- Chapitre 1 — Le facteur humain : pourquoi les humains sont le maillon
- Chapitre 2 — Psychologie de la manipulation : les mécanismes profonds
- Chapitre 3 — Le HUMINT dans le monde du renseignement
- Chapitre 4 — Les profils vulnérables et les facteurs de risque
- Chapitre 5 — Reconnaissance et OSINT préparatoire

**PARTIE II — SOCIAL ENGINEERING NUMÉRIQUE**
- Chapitre 6 — Phishing : méthodologie et sophistication
- Chapitre 7 — Vishing : l'arme de la voix
- Chapitre 8 — Smishing, messageries, collaboration et vecteurs alternatifs
- Chapitre 9 — BEC (Business Email Compromise) et fraude au président
- Chapitre 10 — Intrusion numérique par social engineering : identité, SSO, MFA et workflows
- Chapitre 11 — Capstone Partie II : campagne de social engineering numérique complète

**PARTIE III — SOCIAL ENGINEERING PHYSIQUE**
- Chapitre 12 — Reconnaissance physique et planification
- Chapitre 13 — Techniques d'intrusion physique
- Chapitre 14 — Élicitation en face-à-face
- Chapitre 15 — Manipulation psychologique avancée : de la théorie à l'opérationnel
- Chapitre 16 — Capstone Partie III : test d'intrusion physique et élicitation

**PARTIE IV — L'ATTAQUANT : PERSPECTIVES OFFENSIVES**
- Chapitre 17 — Le social engineering dans les APT
- Chapitre 18 — L'ingénierie sociale dans la fraude et la criminalité organisée
- Chapitre 19 — Red team social engineering : méthodologie professionnelle et OPSEC du praticien
- Chapitre 20 — Capstone Partie IV : planification d'un red team SE complet

**PARTIE V — DÉFENSE ET CONTRE-INGÉNIERIE SOCIALE**
- Chapitre 21 — Sensibilisation : au-delà du e-learning annuel
- Chapitre 22 — Contre-élicitation et protection des informations
- Chapitre 23 — Défense technique contre le social engineering
- Chapitre 24 — Réponse à un incident de social engineering
- Chapitre 25 — Capstone Partie V : incident de social engineering — de la détection au retex

**PARTIE VI — DIMENSIONS AVANCÉES**
- Chapitre 26 — Social engineering et IA : la révolution en cours
- Chapitre 27 — Sécurité physique avancée : au-delà du badge
- Chapitre 28 — Élicitation, investigation et contre-ingérence : usages encadrés et expertise

**PARTIE VII — SYNTHÈSE ET CAS PRATIQUES**
- Chapitre 29 — Cas de synthèse : opération de social engineering multi-vecteurs
- Chapitre 30 — Le métier d'expert en social engineering

**ANNEXES**
- Annexe A — Glossaire (80+ termes)
- Annexe B — Cheat sheets
- Annexe C — Tableau d'outils de référence
- Annexe D — Templates opérationnels
- Annexe E — Ressources et formation
- Annexe F — Cadre juridique
- Annexe G — Mapping de la bibliothèque

---

## PARTIE I — FONDATIONS

---

### Chapitre 1 — Le facteur humain : pourquoi les humains sont le maillon

#### 1.1 La vulnérabilité humaine comme constante

Le social engineering ne repose pas sur l'exploitation d'une faiblesse individuelle. Il exploite des réponses cognitives normales, câblées par l'évolution, que chaque être humain partage : la tendance à faire confiance, le désir de coopérer, la sensibilité à l'autorité, l'aversion au conflit. Un employé qui tient la porte à un inconnu portant un gilet haute visibilité ne fait pas preuve de négligence — il fait preuve de civilité. C'est précisément cette normalité qui rend le social engineering si redoutable : il détourne des comportements sociaux sains pour atteindre des objectifs malveillants.

Aucune technologie ne peut éliminer le facteur humain. Les pare-feux bloquent des paquets, les antivirus détectent des signatures, les systèmes de détection d'intrusion analysent du trafic — mais aucun de ces dispositifs ne peut empêcher un ingénieur R&D de répondre à un faux recruteur sur LinkedIn, ni un comptable de valider un virement demandé par une voix qui ressemble à celle du directeur général. La surface d'attaque humaine n'est pas un résidu de mauvaise hygiène informatique : c'est une constante structurelle de toute organisation qui emploie des êtres humains.

Cette constante ne signifie pas que la défense est impossible. Elle signifie que la défense ne peut pas reposer uniquement sur la technologie. La résilience d'une organisation face au social engineering se construit sur trois piliers : la sensibilisation ciblée (comprendre les mécanismes, pas réciter des règles), les processus vérifiés (double validation, callback, séparation des tâches) et la culture de sécurité (un environnement où signaler un doute est valorisé, pas puni). Le présent cours développe ces trois piliers dans leur dimension offensive et défensive.

#### 1.2 Le social engineering dans le spectre des menaces

Le social engineering n'est pas synonyme de phishing. Le phishing est un vecteur — le plus visible, le plus documenté, le plus mesuré — mais il ne représente qu'une fraction du spectre. Le social engineering est un corpus structuré de techniques qui couvre l'ensemble des interactions humaines exploitables : communication numérique (email, téléphone, messagerie), interaction physique (intrusion, tailgating, impersonation), relation interpersonnelle (élicitation, cultivation, recrutement).

Les chiffres sont sans ambiguïté. Selon le Verizon Data Breach Investigations Report (DBIR), le facteur humain est impliqué dans environ 68 % des violations de données confirmées. Le rapport Unit 42 2025 de Palo Alto Networks confirme que plus d'un tiers des cas de réponse à incident traités au cours de l'année écoulée ont débuté par une tactique de social engineering — sans zero-day, sans malware sophistiqué, mais par l'exploitation de la confiance. Les pertes financières liées au seul BEC (Business Email Compromise) dépassent les 2,9 milliards de dollars aux États-Unis selon l'IC3/FBI, ce qui en fait la catégorie de cybercriminalité la plus coûteuse, loin devant les ransomwares en termes de pertes directes.

L'évolution de la menace est marquée par deux tendances convergentes. D'une part, l'industrialisation : les campagnes de phishing sont automatisées, les kits de phishing-as-a-service sont accessibles à des acteurs peu qualifiés, les techniques de contournement MFA (Evilginx, reverse proxy) se démocratisent. D'autre part, la sophistication ciblée : les groupes APT investissent des semaines dans la construction de relations de confiance avant l'envoi du premier payload, les deepfakes vocaux permettent des fraudes au président d'un réalisme inédit, et l'IA générative permet de produire des leurres personnalisés à l'échelle.

#### 1.3 Le spectre du social engineering : matrice de positionnement

Pour naviguer dans ce cours, il est essentiel de distinguer clairement les différentes dimensions du social engineering et les disciplines connexes. La matrice ci-dessous pose les fondations terminologiques du cours.

| Dimension | Définition | Exemples | Chapitre(s) de référence |
|---|---|---|---|
| **Social engineering numérique** | Obtenir un accès, une action ou une information par manipulation via un canal numérique | Phishing, vishing, smishing, BEC, quishing | Ch.6-11 |
| **Social engineering physique** | Obtenir un accès physique ou une information par manipulation en personne | Tailgating, impersonation, dumpster diving | Ch.12-16 |
| **Élicitation** | Extraction d'information dans une conversation apparemment normale — la cible ne sait pas qu'elle est interrogée | Conversation de salon, faux recruteur, debriefing informel | Ch.14, 22, 28 |
| **HUMINT** | Collecte structurée de renseignement par des sources humaines — relation dans la durée | Repérage, développement, recrutement, exploitation d'une source | Ch.3, 17 |
| **Contre-ingénierie sociale** | Détection, interruption, signalement, protection et résilience face aux tentatives de SE | Contre-élicitation, formation, processus de vérification, culture de signalement | Ch.21-25 |
| **Red team SE** | Simulation autorisée de techniques de SE dans un cadre contractuel et éthique | Test d'intrusion physique, campagne de phishing contrôlée | Ch.19-20 |
| **Attaquant réel** | Exploitation malveillante des mêmes techniques sans cadre ni consentement | APT, BEC criminel, fraude, espionnage | Ch.17-18 |

Cette matrice n'est pas décorative. Elle structure l'ensemble du cours. Chaque technique abordée sera positionnée sur ce spectre, avec les implications éthiques et juridiques correspondantes. La même technique d'élicitation utilisée par un red teamer dans un cadre autorisé et par un agent de renseignement étranger sans consentement de la cible relève de deux réalités juridiques et éthiques totalement différentes, même si le mécanisme psychologique exploité est identique.

#### 1.4 Éthique et cadre légal : la ligne entre test autorisé et manipulation

Le social engineering opère dans un espace éthique et juridique sous tension permanente. Les mêmes techniques qui permettent à un red teamer de tester les défenses d'une organisation sont celles qu'utilise un attaquant réel pour compromettre cette même organisation. La différence ne réside pas dans la technique, mais dans le cadre.

**Le cadre du test autorisé.** Un test de social engineering légitime repose sur quatre piliers indissociables. Premièrement, une autorisation écrite explicite signée par un représentant habilité de l'organisation (généralement le dirigeant ou le RSSI, avec validation juridique). Cette lettre de mission doit définir le scope (quels sites, quels employés, quels vecteurs sont autorisés), la durée, les objectifs et les limites. Deuxièmement, un scope clairement borné : les techniques autorisées sont listées, les lignes rouges sont explicites. Troisièmement, un protocole d'urgence : un « safe word » ou un contact de référence permettant au red teamer de s'identifier immédiatement s'il est intercepté ou si une situation dégénère. Quatrièmement, une clause de confidentialité des résultats individuels : les résultats du test évaluent les processus et la culture, pas les individus.

**Les limites absolues.** Même dans un cadre autorisé, certaines techniques sont proscrites. Le red teamer ne doit jamais exploiter des vulnérabilités personnelles réelles (problèmes de santé, difficultés financières, addictions, situations familiales). Il ne doit jamais recourir au chantage, à l'intimidation réelle, ni créer de détresse psychologique durable. Il ne doit jamais établir de relation intime ou affective avec une cible dans le cadre d'un test. Ces limites ne sont pas des recommandations : ce sont des lignes rouges non négociables qui distinguent le professionnel éthique du manipulateur.

**Le cadre juridique.** En droit français, le social engineering malveillant relève de plusieurs infractions : escroquerie (art. 313-1 du Code pénal), usurpation d'identité (art. 226-4-1), accès frauduleux à un système de traitement automatisé de données (art. 323-1 et suivants), atteinte au secret des correspondances. Le RGPD encadre strictement le traitement des données personnelles collectées, y compris dans un contexte de test autorisé. Le droit du travail impose des limites sur la surveillance des employés et les sanctions disciplinaires pouvant résulter d'un test (le cadre juridique complet est détaillé au Ch.19 et à l'Annexe F).

#### 1.5 Articulation avec la bibliothèque

Ce cours s'inscrit dans un écosystème de cours spécialisés avec lesquels il entretient des renvois croisés explicites, sans créer de dépendance forte. Chaque cours reste exploitable seul.

Le cours *Cybersécurité du quotidien* adopte le prisme de la victime : reconnaître une tentative de phishing, protéger ses comptes, adopter les bons réflexes. Le présent cours explique comment ces attaques sont construites, pourquoi elles fonctionnent et comment les tester et les détecter à l'échelle d'une organisation.

Le cours *Intelligence économique* traite l'HUMINT d'entreprise légal : collecte d'information en salon professionnel, debriefing de collaborateurs, veille concurrentielle. Le présent cours approfondit les techniques d'élicitation, les étend au contexte du renseignement étatique et traite la dimension contre-ingérence.

Le cours *APT* traite le social engineering comme vecteur d'accès initial dans les campagnes de menaces avancées. Le présent cours détaille les techniques elles-mêmes, leur construction et leur défense.

Le cours *OSINT Mastery* fournit les méthodes de reconnaissance en sources ouvertes. Le présent cours montre comment cette reconnaissance alimente directement la crédibilité des pretextes de social engineering (voir Ch.5).

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 1**
>
> **Contexte.** Nathan Vilar, 32 ans, consultant en sécurité offensive (red team) au sein du cabinet de conseil en cybersécurité CyberEdge Partners, reçoit un appel de Lucie Ferraro, RSSI d'Helios Aéronautique. Helios est un équipementier aéronautique de 1 200 employés, réparti sur trois sites en France : siège social à Toulouse (direction, commercial, RH, finance), site de production à Bordeaux (atelier, logistique, qualité) et bureau R&D à Paris (ingénierie, prototypage, brevets).
>
> **Le mandat.** Helios vient de remporter un contrat de sous-traitance pour un programme de défense européen. Le comité de direction, alerté par les retours de la DGSI sur les risques d'ingérence économique dans le secteur aéronautique, décide de mandater un test d'intrusion physique et social engineering complet. La lettre de mission est signée par le DG (Marc Tessier) et la RSSI. Le scope couvre les trois sites, tous les employés (y compris le comité de direction), et toutes les techniques de social engineering sauf le chantage et l'exploitation de vulnérabilités personnelles (santé, finance, vie privée). Durée : 6 semaines. Budget : 45 000 € HT.
>
> Nathan constitue son équipe : lui-même (lead, élicitation, intrusion physique), Yasmine Berrada (phishing, vishing, OSINT) et Thomas Schaeffer (infrastructure technique, implants). Première étape : la reconnaissance.

---

### Chapitre 2 — Psychologie de la manipulation : les mécanismes profonds

#### 2.1 Les principes de Cialdini approfondis

Robert Cialdini a identifié six principes fondamentaux de l'influence, documentés dans *Influence: The Psychology of Persuasion* (1984) puis enrichis dans *Pre-Suasion* (2016) avec un septième principe (l'unité). Ces principes ne sont pas des « astuces » : ce sont des mécanismes cognitifs profonds, forgés par l'évolution, que tout être humain partage. Comprendre ces mécanismes est la base de toute pratique de social engineering, qu'elle soit offensive (exploitation) ou défensive (détection).

**La réciprocité.** Quand quelqu'un fait quelque chose pour nous, nous ressentons une obligation de rendre la pareille. Ce mécanisme est si puissant qu'il fonctionne même lorsque le « cadeau » initial est non sollicité ou de faible valeur. En social engineering, la réciprocité est exploitée de multiples façons : le faux technicien IT qui « aide » un employé à résoudre un problème (réel ou fabriqué) avant de demander un accès ; le « recruteur » LinkedIn qui partage un article intéressant ou une opportunité professionnelle avant de poser des questions sur les projets internes ; l'attaquant qui fournit un mot de passe « pour vérification » afin d'obtenir le vrai mot de passe en retour (le partage réciproque). La défense repose sur la capacité à reconnaître les obligations artificiellement créées et à les refuser sans culpabilité.

**L'engagement et la cohérence.** Une fois qu'un individu s'est engagé dans une direction — même par un acte minime — il tend à rester cohérent avec cet engagement initial. C'est le fondement de la technique du « pied dans la porte » (détaillée au Ch.15) : obtenir un premier « oui » (une petite demande anodine) augmente considérablement la probabilité d'obtenir un « oui » à une demande plus importante. En vishing, l'attaquant commence par des questions de vérification simples (« pouvez-vous confirmer votre nom ? ») avant d'escalader vers des demandes sensibles (« et votre identifiant employé ? »). Chaque réponse renforce l'engagement de la cible dans la conversation et rend le refus psychologiquement plus coûteux.

**La preuve sociale.** En situation d'incertitude, les individus se tournent vers le comportement des autres pour guider le leur. Si « tout le monde le fait », cela doit être correct. L'attaquant exploite ce principe en invoquant des précédents (« vos collègues du 3e étage ont déjà fait la mise à jour »), en simulant une activité normale (se comporter comme si l'on appartenait à l'environnement) ou en créant de faux consensus (« la direction a validé cette procédure »). La preuve sociale est particulièrement efficace dans les grandes organisations où les employés ne connaissent pas personnellement tous leurs collègues et où le comportement des autres sert de boussole sociale.

**L'autorité.** La tendance à obéir aux figures d'autorité est l'un des mécanismes les plus documentés en psychologie sociale, depuis les expériences de Stanley Milgram (1963). En social engineering, l'autorité n'a pas besoin d'être réelle — elle doit être perçue. Un titre (« directeur technique »), un uniforme (gilet haute visibilité, costume), un jargon technique maîtrisé, un ton assuré suffisent à activer le mécanisme de déférence. La fraude au président exploite directement ce principe : l'employé reçoit un ordre de virement d'une personne qu'il perçoit comme son supérieur hiérarchique, et la chaîne de commandement fait le reste.

**La sympathie (liking).** Nous sommes plus enclins à accéder aux demandes de personnes que nous trouvons sympathiques. La sympathie est activée par la similarité perçue (mêmes intérêts, même parcours, même langage), la flatterie, la familiarité et l'attractivité physique. En élicitation, l'attaquant construit un rapport rapide en identifiant des points communs (« vous aussi vous avez fait l'INSA ? »), en validant les opinions de la cible et en adoptant un langage corporel ouvert et accueillant. La sympathie désarme la vigilance parce qu'elle active un mode de traitement cognitif coopératif plutôt que critique.

**La rareté.** Ce qui est rare est perçu comme plus précieux. L'urgence temporelle (« cette offre expire dans 2 heures ») et la disponibilité limitée (« il ne reste que 3 places ») sont les leviers les plus courants. En phishing, l'urgence artificielle est le levier le plus fréquemment utilisé : « votre compte sera désactivé dans 24h », « validation requise avant 17h ». En vishing, le temps réel amplifie l'effet : la cible n'a pas le temps de réfléchir, de vérifier, de consulter un collègue. La rareté fonctionne parce qu'elle active le système de pensée rapide (System 1 de Kahneman) au détriment du système analytique (System 2).

#### 2.2 Au-delà de Cialdini : les leviers complémentaires

Les six principes de Cialdini constituent le socle, mais le praticien de social engineering dispose de leviers complémentaires tout aussi opérationnels.

**La curiosité.** L'être humain est câblé pour résoudre les lacunes informationnelles. Un email dont l'objet est « Vos résultats d'évaluation annuelle » ou « Photos de la soirée d'entreprise » exploite la curiosité — le clic n'est pas un acte de négligence, c'est une réponse cognitive automatique. Les clés USB déposées dans un parking (baiting) exploitent le même mécanisme : « qu'y a-t-il dessus ? ».

**La peur.** La peur court-circuite l'analyse rationnelle. Les scareware (« votre ordinateur est infecté ! ») et les emails menaçant une désactivation de compte exploitent la peur de perdre l'accès, de subir une sanction, d'être exposé. La peur est un levier particulièrement efficace lorsqu'elle est combinée avec l'urgence : la cible doit agir vite pour éviter une conséquence négative, ce qui laisse peu de place à la vérification.

**La fatigue décisionnelle.** À mesure que la journée avance et que les décisions s'accumulent, la qualité du jugement se dégrade. Les attaquants le savent : les campagnes de phishing envoyées le lundi matin (accumulation d'emails du week-end) ou le vendredi après-midi (fatigue de fin de semaine, envie de conclure rapidement) ont des taux de réussite significativement supérieurs à celles envoyées à d'autres moments.

**L'ego et la flatterie.** Être reconnu comme expert, comme la personne indispensable, comme le seul à comprendre un système — cette flatterie est un puissant désinhibiteur. En élicitation, affirmer « vous êtes la seule personne qui comprenne vraiment ce système » transforme la cible en source volontaire. La flatterie fonctionne même lorsqu'elle est perçue comme telle, parce que l'ego apprécie la reconnaissance indépendamment de son authenticité.

**Le sentiment d'obligation professionnelle.** Les cultures d'entreprise qui valorisent la réactivité, le service client ou la disponibilité créent un terreau fertile pour le social engineering. Un helpdesk formé à « résoudre le problème du client le plus vite possible » est structurellement vulnérable au pretexting : le technicien qui refuse d'aider un « collègue bloqué » viole la norme professionnelle qu'on lui a inculquée.

#### 2.3 Les biais cognitifs en profondeur

Au-delà des principes d'influence, plusieurs biais cognitifs rendent les individus particulièrement vulnérables au social engineering.

**Le biais d'optimisme** (« ça n'arrive qu'aux autres ») est le plus destructeur en matière de sensibilisation. Les employés qui ont suivi une formation reconnaissent le phishing en théorie, mais croient sincèrement qu'ils ne se feront pas piéger en pratique. Ce biais explique pourquoi les campagnes de sensibilisation par quiz ont un impact limité : réussir un quiz ne modifie pas la perception du risque personnel.

**Le biais de confirmation** amène les individus à interpréter les informations de manière cohérente avec leurs croyances préexistantes. Si un employé s'attend à recevoir un email de la RH sur les congés, il sera moins vigilant face à un phishing qui utilise ce prétexte. L'attaquant ne crée pas la crédibilité ex nihilo — il s'appuie sur les attentes existantes de la cible.

**L'effet de halo** fait qu'une impression positive sur un attribut (apparence soignée, titre prestigieux, langage professionnel) se généralise à l'ensemble de la personne. Le red teamer en costume qui arrive avec un clipboard et un badge d'entreprise bénéficie de l'effet de halo : son apparence professionnelle le rend crédible avant même qu'il n'ouvre la bouche.

**Le biais de normalité** (« ce comportement est normal dans notre entreprise ») explique pourquoi le tailgating fonctionne si bien. Dans une entreprise où « on tient la porte » est la norme sociale, refuser de tenir la porte à un inconnu est un acte de déviance sociale. L'attaquant ne pirate pas un système — il s'insère dans un système de normes sociales existant.

#### 2.4 La charge cognitive comme vulnérabilité

La vigilance n'est pas un état permanent. C'est une ressource limitée qui se dégrade sous l'effet du stress, de la fatigue, du multitâche et de la surcharge informationnelle. Un employé qui gère simultanément une deadline projet, 200 emails non lus et un appel téléphonique inattendu n'a tout simplement pas les ressources cognitives nécessaires pour analyser critiquement une demande suspecte.

Les attaquants créent artificiellement la surcharge cognitive. Le visher qui appelle avec une urgence fabriquée (« votre compte a été compromis, il faut agir maintenant ») ne transmet pas seulement une fausse information — il active le mode de traitement d'urgence du cerveau, qui privilégie la rapidité d'action au détriment de l'analyse. L'email de phishing qui arrive pendant une réunion importante sera traité en mode « multi-tâche » avec une attention réduite. Le pretexte qui combine autorité et urgence (« le DG a besoin de ce virement avant 17h ») crée une double pression qui réduit drastiquement la capacité de jugement.

Cette réalité a une implication directe pour la défense : les processus de sécurité qui reposent sur la vigilance individuelle sont structurellement fragiles. Un processus robuste est un processus qui fonctionne même quand l'individu est fatigué, stressé ou distrait — c'est-à-dire un processus qui impose des vérifications automatiques (callback, double validation) plutôt que de compter sur l'analyse critique de chaque demande.

#### 2.5 Persuasion et manipulation : le continuum éthique

La distinction entre persuasion et manipulation n'est pas binaire — c'est un continuum. À une extrémité, la persuasion légitime : un commercial qui argumente sur les mérites de son produit, un manager qui motive son équipe, un médecin qui convainc un patient de suivre un traitement. À l'autre extrémité, la coercition : menaces, chantage, violence. Entre les deux, un spectre de pratiques dont la légitimité dépend du contexte, de l'intention et du consentement.

L'influence se situe au milieu de ce spectre : elle oriente le comportement de l'autre en utilisant des leviers psychologiques, sans que l'autre soit nécessairement conscient de ces leviers. La manipulation va plus loin : elle oriente le comportement de l'autre contre ses propres intérêts, en exploitant des vulnérabilités cognitives ou émotionnelles, souvent avec un élément de tromperie.

Pour le praticien de social engineering, cette distinction a des implications concrètes. Le red teamer utilise la manipulation dans un cadre autorisé et borné : les mêmes techniques, utilisées par un attaquant réel, constituent des délits. Le formateur en sensibilisation utilise la compréhension de la manipulation pour enseigner la détection. L'analyste en contre-ingénierie sociale utilise la connaissance des leviers pour identifier les tentatives en cours. Dans tous les cas, la compréhension profonde des mécanismes est un prérequis — mais la façon dont cette compréhension est utilisée détermine si le praticien est du côté de la défense ou de l'attaque.

---

### Chapitre 3 — Le HUMINT dans le monde du renseignement

#### 3.1 Définition et cadre

HUMINT (Human Intelligence) désigne la collecte de renseignement par l'intermédiaire de sources humaines. C'est le plus ancien des « INTs » — bien avant l'existence de SIGINT (interception de communications), IMINT (imagerie satellite) ou OSINT (sources ouvertes), les espions recueillaient de l'information par la conversation, l'observation et la relation interpersonnelle. Le HUMINT reste, en 2025, irremplaçable pour certains types d'information : les intentions d'un décideur, les projets non encore documentés, les arbitrages internes d'une organisation, les vulnérabilités d'un processus qui n'apparaissent dans aucun système.

Le HUMINT ne se confond pas avec le social engineering, même si les deux disciplines partagent des techniques communes (élicitation, pretexting, rapport building). Le social engineering vise généralement un objectif tactique précis (obtenir un mot de passe, un accès, une action) dans un temps court. Le HUMINT s'inscrit dans une logique stratégique, souvent sur des mois ou des années, avec un objectif de collecte continue. Le social engineering peut être le premier acte d'une opération HUMINT, mais le HUMINT est un processus structuré qui va bien au-delà.

#### 3.2 Le cycle HUMINT

Le cycle HUMINT suit une progression méthodique en cinq phases. Chaque phase a ses techniques, ses risques et ses contre-mesures.

**Le repérage (spotting).** C'est l'identification de cibles potentielles — des individus qui ont accès à l'information recherchée et qui présentent des facteurs de vulnérabilité exploitables. Le repérage repose massivement sur l'OSINT : profils LinkedIn, publications professionnelles, présence en conférence, réseau social. Un ingénieur R&D qui publie régulièrement sur ses projets, participe à des conférences internationales et affiche un réseau LinkedIn ouvert est une cible de repérage évidente. Le repérage évalue aussi les facteurs de motivation : insatisfaction professionnelle, ambition bloquée, difficultés financières, ego surdimensionné.

**Le développement (development).** C'est l'établissement du contact et la construction progressive de la relation. Le « developmental contact » est conçu pour paraître naturel : rencontre en conférence, connexion LinkedIn via un intérêt commun, invitation à un séminaire, proposition de collaboration académique. L'objectif n'est pas d'obtenir de l'information immédiatement — c'est de créer un lien de confiance qui sera exploité ultérieurement. La patience est l'arme fondamentale du HUMINT : des semaines ou des mois de contacts apparemment anodins avant la première demande significative.

**Le recrutement (recruitment).** C'est la transformation du contact en source active. Le recrutement peut être explicite (la source sait qu'elle collabore avec un service de renseignement) ou implicite (la source livre de l'information sans réaliser la nature réelle de son interlocuteur). Le recrutement exploite les leviers classiques du modèle MICE : Money (rémunération), Ideology (adhésion à une cause), Coercion (chantage, compromission), Ego (reconnaissance, flatterie). Dans la pratique contemporaine, le recrutement par l'ego et la rémunération est bien plus courant que le recrutement par la coercition — cette dernière étant plus risquée et moins stable.

**L'exploitation.** C'est la phase de collecte structurée. La source fournit de l'information selon un cadre défini par le traitant : questions ciblées, documents, accès à des réunions, identification d'autres cibles potentielles. L'exploitation est gérée avec soin pour ne pas « brûler » la source (ne pas la mettre en danger en demandant trop ou trop vite).

**La gestion (handling).** C'est la maintenance de la relation et de la sécurité opérationnelle : canaux de communication sécurisés, rendez-vous discrets, rémunération, soutien psychologique, gestion des crises (si la source est soupçonnée). La gestion est souvent la phase la plus longue et la plus délicate du cycle HUMINT.

#### 3.3 Les services de renseignement et l'élicitation d'entreprise

Les services de renseignement étrangers ciblent activement les employés des entreprises stratégiques et des administrations. Ce n'est pas une menace théorique : la DGSI publie régulièrement des alertes sur les tentatives d'ingérence économique visant les entreprises françaises dans les secteurs de la défense, de l'aéronautique, de l'énergie, des télécommunications et de la recherche.

Les vecteurs de contact les plus fréquents sont les salons professionnels internationaux (où les cibles sont accessibles, ouvertes au networking et éloignées de leur cadre de sécurité habituel), les plateformes professionnelles en ligne (LinkedIn est devenu le terrain de chasse principal pour le repérage et le contact initial), les invitations à des séminaires académiques ou professionnels dans certains pays, et les approches par des « journalistes », « consultants » ou « recruteurs » dont l'identité est difficile à vérifier.

Les signaux d'alerte d'une tentative d'élicitation par un service de renseignement incluent : des questions inhabituellement spécifiques sur des projets ou des technologies internes, une insistance à déplacer la conversation vers un canal privé (WhatsApp, Signal), une progression relationnelle rapide (invitation à dîner dès le premier contact), des propositions de rémunération pour des « consultations » ou des « expertises » vagues, un intérêt disproportionné pour le réseau professionnel de la cible, et un profil difficile à vérifier (entreprise opaque, parcours incohérent, photos de profil douteuses). Les techniques de contre-élicitation sont détaillées au Ch.22.

#### 3.4 HUMINT d'entreprise vs HUMINT de renseignement

L'HUMINT d'entreprise — collecte d'information concurrentielle par des moyens humains légaux — partage des techniques avec l'HUMINT de renseignement (élicitation, observation, debriefing) mais opère dans un cadre juridique et éthique radicalement différent.

L'HUMINT d'entreprise légal se limite à la collecte d'informations disponibles ou accessibles par des moyens licites : conversations en salon professionnel (sans faux pretexte), debriefing de collaborateurs après un événement, analyse des déclarations publiques de concurrents, observation du marché. Il ne recourt ni à la tromperie, ni à l'usurpation d'identité, ni au recrutement de sources internes chez un concurrent. Le cadre est celui de la veille concurrentielle et de l'intelligence économique (renvoi vers le cours IE, Ch.8).

La ligne de démarcation est claire dans le principe, mais parfois floue dans la pratique. Une conversation spontanée en conférence où un concurrent partage volontairement des informations est de l'intelligence économique légitime. La même conversation, si elle est orchestrée sous un faux pretexte (se faire passer pour un journaliste ou un universitaire pour obtenir des informations concurrentielles), bascule dans l'illégalité.

#### 3.5 Le rôle de l'OSINT dans le HUMINT

La reconnaissance en sources ouvertes est la phase préparatoire obligatoire de toute opération HUMINT. Aucun professionnel sérieux — qu'il soit red teamer, analyste en contre-ingérence ou agent de renseignement — n'aborde une cible sans avoir préalablement collecté et analysé toute l'information disponible en source ouverte.

L'OSINT alimente le HUMINT à chaque étape du cycle. En phase de repérage, elle identifie les cibles potentielles et évalue leur accessibilité (profil LinkedIn ouvert vs fermé, présence en conférence, publications). En phase de développement, elle fournit les éléments de personnalisation du contact (intérêts communs, parcours partagé, sujets de conversation). En phase d'exploitation, elle permet de formuler des questions d'élicitation pertinentes et de valider les réponses obtenues.

La qualité de la reconnaissance OSINT détermine directement la crédibilité du pretexte et donc le taux de succès de l'opération de social engineering. Un phishing générique envoyé à 10 000 adresses aura un taux de clic de 2 à 5 %. Un spear-phishing construit à partir d'une reconnaissance OSINT approfondie (terminologie interne, noms de projets, prestataires identifiés) aura un taux de clic de 20 à 40 %. La reconnaissance est le multiplicateur de force du social engineering. Les méthodes de reconnaissance OSINT sont détaillées au Ch.5 (renvoi vers le cours OSINT Mastery pour la profondeur méthodologique).

---

### Chapitre 4 — Les profils vulnérables et les facteurs de risque

#### 4.1 Qui est vulnérable ? Tout le monde

Le mythe de la victime naïve est l'un des plus dangereux en social engineering. Il crée un faux sentiment de sécurité chez les individus qui se considèrent trop informés, trop intelligents ou trop expérimentés pour être piégés. La réalité est exactement inverse : les experts se font piéger aussi souvent que les novices — simplement par des techniques adaptées à leur profil.

Un RSSI qui détectera un phishing grossier peut se laisser piéger par un spear-phishing hautement personnalisé qui exploite son ego professionnel (« votre expertise est reconnue dans le secteur, nous aimerions vous inviter comme keynote speaker »). Un ingénieur R&D qui ignore les emails suspects peut succomber à une élicitation de face-à-face menée par un faux chercheur universitaire qui parle son langage technique. Un dirigeant qui se méfie des appels inconnus peut être vulnérable à une fraude au président menée par deepfake vocal lors d'une visioconférence apparemment légitime.

La vulnérabilité n'est pas une caractéristique personnelle — c'est une situation. Le même individu peut être vigilant dans un contexte et vulnérable dans un autre. Comprendre les facteurs de risque contextuels est bien plus utile que de profiler des « victimes types ».

#### 4.2 Les facteurs de risque contextuels

Certaines situations augmentent significativement la vulnérabilité au social engineering, indépendamment de la compétence ou de l'intelligence de l'individu.

**Le nouveau poste.** Un employé récemment arrivé ne connaît pas encore les procédures, les visages, les habitudes de l'organisation. Il est en mode d'adaptation et d'apprentissage, ce qui le rend réceptif aux demandes de personnes qui semblent connaître l'entreprise mieux que lui. Le pretexting classique « je suis de l'IT, je dois configurer votre poste » est particulièrement efficace sur les nouveaux arrivants.

**Le voyage professionnel.** L'isolement géographique, la désorientation culturelle, le décalage horaire et l'absence du cadre de sécurité habituel (collègues de confiance, procédures connues) créent une fenêtre de vulnérabilité. Les services de renseignement exploitent systématiquement les voyages professionnels dans certains pays : chambre d'hôtel surveillée, contacts « spontanés » dans les bars d'hôtel, invitations à des événements sociaux (voir Ch.22 pour les contre-mesures).

**Le salon professionnel.** L'ouverture sociale est la norme : échanger des cartes de visite, discuter de ses projets, nouer des contacts est le but même de la participation. Cette ouverture crée un environnement idéal pour l'élicitation : les barrières sociales habituelles sont abaissées, la curiosité intellectuelle est stimulée, et le contexte professionnel légitime les questions sur l'activité de l'entreprise.

**La période de stress ou de conflit professionnel.** Un employé en conflit avec sa hiérarchie, menacé de licenciement, sous-estimé ou frustré dans ses ambitions est plus réceptif aux approches extérieures — qu'il s'agisse d'un faux recruteur qui propose une « opportunité de carrière » ou d'un interlocuteur qui offre reconnaissance et écoute. Ce facteur est l'un des leviers classiques du recrutement de sources par les services de renseignement.

**La transition de carrière.** Un employé en fin de contrat, en pré-retraite ou en recherche active d'emploi est structurellement réceptif aux propositions professionnelles — et donc aux approches de faux recruteurs.

#### 4.3 Le modèle MICE et ses extensions

Le modèle MICE (Money, Ideology, Coercion, Ego) est le cadre classique du renseignement pour analyser les motivations d'un individu à collaborer comme source. Il reste pertinent en 2025, mais il a été étendu pour mieux refléter la diversité des leviers.

**Money.** La motivation financière reste un levier puissant, particulièrement pour les individus qui perçoivent un décalage entre leur contribution et leur rémunération, ou qui traversent des difficultés financières. Les « consultations rémunérées » proposées par de faux cabinets de conseil sont un vecteur classique.

**Ideology.** L'adhésion à une cause — politique, environnementale, religieuse, nationaliste — peut motiver la divulgation d'informations. Ce levier est moins fréquent en contexte d'entreprise qu'en contexte étatique, mais il existe (lanceurs d'alerte convaincus de servir l'intérêt public, employés politisés ciblés par des acteurs étrangers partageant apparemment les mêmes convictions).

**Coercion.** Le chantage, la compromission (kompromat) et les menaces constituent le levier le plus risqué et le moins stable — une source recrutée par la coercition est une source hostile qui cherchera à se libérer. En contexte de red team, ce levier est formellement interdit.

**Ego.** La flatterie, la reconnaissance, le sentiment d'être un interlocuteur privilégié sont des leviers extrêmement efficaces, en particulier auprès d'experts techniques qui manquent de reconnaissance dans leur organisation. Le modèle RASCLS (Reciprocity, Authority, Scarcity, Commitment, Liking, Social proof) étend l'analyse des leviers aux principes d'influence de Cialdini, offrant une grille d'analyse plus fine.

**Revenge.** La vengeance est un levier ajouté par les praticiens contemporains : un employé qui se sent trahi par son employeur (licenciement perçu comme injuste, promotion ratée, conflit avec la hiérarchie) peut être motivé par le désir de « punir » l'organisation.

#### 4.4 Les insiders involontaires

La distinction entre insider malveillant et insider involontaire est fondamentale. L'insider malveillant agit délibérément contre les intérêts de son organisation (vol de données, sabotage). L'insider involontaire est un employé légitime, loyal et bien intentionné, qui divulgue des informations ou accorde des accès sans réaliser qu'il est manipulé.

L'insider involontaire est la cible privilégiée du social engineering et de l'élicitation. Il ne sait pas qu'il participe à une opération hostile. Le « recruteur » LinkedIn avec qui il échange depuis trois mois lui semble être un contact professionnel légitime. Le « technicien de maintenance » à qui il a tenu la porte dans le couloir avait un badge qui ressemblait au bon. L'email qui lui demandait de « mettre à jour ses identifiants » venait d'une adresse qui ressemblait à celle de la DSI.

La détection des insiders involontaires passe par la formation (reconnaître les signaux d'élicitation), les processus (vérification des demandes sensibles) et la surveillance comportementale (détection d'accès anormaux), mais aussi par une culture où le signalement d'un doute est encouragé sans conséquence négative pour celui qui signale.

#### 4.5 Le profilage éthique en contexte red team

Dans un test de social engineering autorisé, le red teamer évalue la vulnérabilité des individus pour déterminer les cibles les plus probables et les pretextes les plus efficaces. Ce profilage est nécessaire — mais il doit respecter des limites strictes.

**Ce qu'on observe et exploite** : le rôle dans l'organisation (accès, responsabilités), le comportement professionnel observable (présence en conférence, publications, activité LinkedIn), les habitudes de travail visibles (horaires, déplacements, habitudes de pause), le niveau de familiarité avec les procédures de sécurité.

**Ce qu'on n'observe pas et n'exploite jamais** : les problèmes personnels (santé, finances, vie sentimentale, addictions), les situations de vulnérabilité individuelle (deuil, divorce, problèmes familiaux), les opinions politiques ou religieuses, les données sensibles au sens du RGPD.

La ligne est claire dans le principe, mais elle peut être floue en pratique. Un red teamer qui découvre, au cours de sa reconnaissance OSINT, qu'un employé traverse un divorce difficile (information visible sur les réseaux sociaux) ne doit pas utiliser cette information pour personnaliser son approche, même si un attaquant réel le ferait. Le red teamer teste les défenses de l'organisation, pas les faiblesses personnelles des individus.

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 2**
>
> **Phase de reconnaissance.** Nathan et Yasmine lancent la reconnaissance OSINT sur Helios Aéronautique. En trois jours, ils collectent un volume d'information considérable.
>
> **LinkedIn** : 350 profils identifiés, dont 42 cadres et 28 ingénieurs R&D. L'organigramme est reconstitué à 80 %. Le DSI s'appelle Frédéric Morin. Le responsable de la production à Bordeaux est Jean-Marc Duval. Trois ingénieurs R&D publient régulièrement sur des conférences techniques. Le prestataire de maintenance informatique est identifié grâce à un post LinkedIn d'un de ses techniciens mentionnant une intervention chez Helios.
>
> **Offres d'emploi** : 12 annonces en cours révèlent la stack technique (Microsoft 365, Azure AD, SAP, SolidWorks, un ERP maison) et les compétences recherchées (ingénieur simulation, technicien qualité, développeur .NET).
>
> **Réseaux sociaux personnels** : photos de la soirée d'entreprise sur Instagram → badges visibles sur 4 photos (format, couleur, logo, puce RFID apparente). Post Facebook d'un employé : « Super formation incendie ce matin, on a tous évacué par la sortie Est ». Géolocalisation de posts TikTok par deux jeunes employés → identification de l'entrée fumoir côté parking.
>
> **Site web et presse** : communiqué de presse sur le contrat de sous-traitance défense (confirme l'enjeu stratégique), photos du siège (architecture, entrées, parking), rapport RSE mentionnant le prestataire de ménage et le traiteur de la cantine.
>
> Nathan rédige le dossier de reconnaissance et commence à construire les pretextes.

---

### Chapitre 5 — Reconnaissance et OSINT préparatoire

#### 5.1 L'OSINT comme préalable obligatoire

Toute opération de social engineering commence par la reconnaissance. C'est un axiome, pas une recommandation. La qualité de l'information collectée en phase de reconnaissance détermine directement la crédibilité du pretexte, le choix de la cible et le taux de succès de l'opération. Un pretexte construit sans reconnaissance est un pretexte générique — et un pretexte générique échoue face à un employé moyennement vigilant.

L'OSINT (Open Source Intelligence) fournit au social engineer trois types d'information critiques : l'information organisationnelle (structure, processus, culture d'entreprise), l'information individuelle (profils, intérêts, vulnérabilités professionnelles des cibles potentielles) et l'information technique (systèmes utilisés, configurations de sécurité, vecteurs d'attaque potentiels). Le cours OSINT Mastery de la bibliothèque couvre en profondeur les méthodologies de collecte — le présent chapitre se concentre sur l'application spécifique de l'OSINT au social engineering.

#### 5.2 Reconnaissance organisationnelle

La reconnaissance organisationnelle vise à comprendre l'entreprise cible comme un système : sa structure, ses processus, sa culture, ses partenaires et ses vulnérabilités structurelles.

**L'organigramme.** LinkedIn est la source principale. En croisant les profils des employés, le red teamer reconstitue l'organigramme fonctionnel : qui dirige quoi, qui reporte à qui, quels sont les liens hiérarchiques et fonctionnels. Les signatures d'emails (collectées via des interactions légitimes ou des fuites) complètent le tableau. L'organigramme identifie les cibles à haute valeur (accès à des informations sensibles, pouvoir de décision sur les virements) et les cibles à basse résistance (nouveaux arrivants, postes à fort turnover, prestataires).

**La terminologie interne.** Chaque organisation a son jargon : noms de projets, acronymes internes, noms de systèmes, appellations de services. Maîtriser cette terminologie est un marqueur de crédibilité majeur. Un phishing qui mentionne « le projet Vega » ou « la migration vers SAP S/4HANA » sera infiniment plus crédible qu'un email générique. Les sources de terminologie incluent les offres d'emploi (qui décrivent les outils et les projets), les publications des employés (articles LinkedIn, présentations en conférence), les documents publics (rapports annuels, communiqués de presse) et les fuites involontaires (photos de tableaux blancs sur les réseaux sociaux).

**Les prestataires et fournisseurs.** Les prestataires sont des vecteurs d'intrusion majeurs — ils ont souvent un accès physique ou logique aux locaux et aux systèmes sans être soumis aux mêmes contrôles que les employés internes. Identifier les prestataires (IT, ménage, maintenance, restauration, sécurité) permet de construire des pretextes d'impersonation crédibles. Les sources incluent LinkedIn (employés des prestataires mentionnant leurs clients), les réseaux sociaux (photos de véhicules de prestataires sur le parking), les offres d'emploi des prestataires eux-mêmes et les documents publics (appels d'offres, marchés publics pour les entreprises du secteur public).

**Le calendrier.** Les périodes de vulnérabilité sont prévisibles : fin de trimestre (pression sur les résultats), période de vacances (effectifs réduits, intérimaires moins formés), événements d'entreprise (soirées, séminaires — ouverture sociale accrue), audits prévus (les employés s'attendent à des demandes inhabituelles).

#### 5.3 Reconnaissance individuelle

La reconnaissance individuelle cible les personnes spécifiques qui seront approchées pendant l'opération.

**LinkedIn.** C'est la mine d'or du social engineer. Un profil LinkedIn complet fournit : le poste exact et les responsabilités, le parcours professionnel (ancienneté dans l'entreprise, postes précédents), les compétences techniques (outils maîtrisés, certifications), le réseau professionnel (collègues, anciens collègues, contacts communs exploitables pour le name-dropping), les publications et partages (intérêts professionnels, opinions, expertise revendiquée), les recommandations (relations de confiance identifiées) et la photo (reconnaissance visuelle pour l'intrusion physique). La restriction de visibilité d'un profil LinkedIn n'est que partiellement efficace : les noms, les titres et les entreprises restent souvent visibles même pour les profils restreints.

**Réseaux sociaux personnels.** Facebook, Instagram, Twitter/X, TikTok fournissent des informations complémentaires sur les centres d'intérêt (sport, voyage, cuisine — autant de sujets pour construire un rapport), les habitudes (horaires, lieux fréquentés), l'environnement personnel (famille, animaux) et les opinions. Ces informations permettent de personnaliser l'approche et de créer une connexion rapide. Un red teamer qui découvre que sa cible est passionnée de course à pied peut se présenter comme coureur pour établir un lien. L'exploitation de ces informations est légitime en red team (information publique) mais doit rester dans les limites éthiques (ne pas exploiter de données sensibles).

**Publications professionnelles.** Articles de blog, interventions en conférence, brevets, publications académiques révèlent l'expertise de la cible et fournissent un vocabulaire technique précis pour l'élicitation. Un faux chercheur universitaire qui cite les travaux publiés de sa cible gagne immédiatement en crédibilité.

#### 5.4 Reconnaissance technique

La reconnaissance technique alimente les vecteurs d'attaque numériques et physiques.

**Domaines et email.** L'identification du format d'adresse email (prenom.nom@helios-aero.fr vs p.nom@helios-aero.fr) est critique pour le spear-phishing. Les outils de collecte d'emails (Hunter.io, Snov.io — attention aux limites de quotas et aux conditions d'utilisation) et les fuites de données (Have I Been Pwned, Dehashed) permettent de confirmer les formats et d'identifier des comptes potentiellement compromis.

**Technologies.** Les offres d'emploi sont la source la plus riche : une annonce pour un « Administrateur Microsoft 365 / Azure AD » révèle la stack d'identité. Les en-têtes d'email (SPF, DKIM, DMARC — ou leur absence) indiquent le niveau de protection email. Les sous-domaines (vpn.helios-aero.fr, owa.helios-aero.fr) révèlent les services exposés.

**Contrôle d'accès physique.** Les photos sur les réseaux sociaux sont une source sous-estimée. Une photo de badge visible sur une selfie d'employé peut révéler le format du badge (taille, couleur, logo, position de la puce), le type de technologie (RFID, NFC — la présence d'une antenne circulaire visible indique du HF 13,56 MHz ; une puce simple du LF 125 kHz), le niveau de personnalisation (photo, nom, service) et le système de contrôle d'accès (les lecteurs visibles sur les photos d'entrée identifient souvent le fabricant).

#### 5.5 Les limites de la reconnaissance

La reconnaissance en sources ouvertes opère dans un cadre éthique et juridique qui diffère selon le contexte.

En **contexte red team**, l'OSINT est réalisée dans le cadre de la lettre de mission. Toute information publiquement accessible est exploitable, mais l'exploitation doit rester dans le scope autorisé (par exemple, la reconnaissance sur les réseaux sociaux personnels des employés peut être autorisée pour construire des pretextes, mais l'exploitation de données sensibles — santé, opinions politiques, vie sexuelle — est exclue même si ces informations sont publiques).

En **contexte attaquant réel**, aucune limite n'est respectée. L'attaquant exploitera toute information disponible, y compris les données personnelles les plus intimes. Cette asymétrie est l'une des difficultés fondamentales de la défense : le red teamer opère avec des contraintes éthiques que l'attaquant n'a pas. Le test autorisé sous-estime donc systématiquement la surface d'attaque réelle.

En **contexte défensif** (contre-ingérence, évaluation de la surface d'exposition), la reconnaissance est réalisée sur sa propre organisation pour identifier les informations exposées et réduire la surface d'attaque. C'est l'une des actions les plus rentables en matière de défense contre le social engineering : savoir ce que l'attaquant sait de vous avant qu'il ne s'en serve.


---

## PARTIE II — SOCIAL ENGINEERING NUMÉRIQUE

---

### Chapitre 6 — Phishing : méthodologie et sophistication

#### 6.1 Anatomie d'un email de phishing

Un email de phishing est un système de composantes interdépendantes, chacune contribuant à la crédibilité globale du leurre. Comprendre ces composantes est essentiel pour le praticien — qu'il construise un test autorisé ou qu'il analyse une attaque en cours.

**L'expéditeur.** C'est le premier élément évalué par le destinataire — souvent le seul, sur mobile. L'attaquant dispose de plusieurs techniques pour simuler un expéditeur légitime. Le spoofing d'adresse exploite l'absence ou la mauvaise configuration de SPF/DKIM/DMARC pour envoyer un email qui affiche une adresse légitime dans le champ « From ». Le typosquatting utilise un domaine visuellement similaire (helios-aero.fr → heIios-aero.fr avec un « I » majuscule à la place du « l », ou helios-aer0.fr avec un zéro). Le display name spoofing modifie le nom affiché sans toucher à l'adresse réelle : « Marc Tessier - DG Helios » <attaquant@domaine-malveillant.com> — sur mobile, seul le display name est visible par défaut. La compromission d'email légitime (reply-chain attack) est la technique la plus difficile à détecter : l'attaquant compromet une boîte mail réelle et s'insère dans un fil de conversation existant.

**L'objet.** L'objet détermine l'ouverture de l'email. Les objets les plus efficaces combinent pertinence contextuelle et urgence modérée : « Mise à jour obligatoire — Portail RH » est plus efficace que « URGENT !!! Votre compte sera supprimé !!! » (trop agressif, signaux d'alerte). Les objets qui exploitent la curiosité (« Résultats évaluation annuelle 2025 ») ou l'intérêt professionnel (« Invitation keynote — Congrès Aéronautique Lyon ») ont des taux d'ouverture supérieurs.

**Le corps.** Le corps doit être cohérent avec l'expéditeur et l'objet, utiliser la terminologie de l'entreprise cible, et inclure un appel à l'action clair mais non agressif. Les erreurs de langue, autrefois marqueur fiable de phishing, sont en voie de disparition grâce aux LLM qui génèrent des textes grammaticalement parfaits et stylistiquement adaptés au contexte culturel.

**Le lien ou la pièce jointe.** C'est le vecteur technique : URL vers une landing page de collecte d'identifiants, document piégé (macro Office, fichier HTA, fichier ISO/IMG contenant un exécutable), QR code redirigeant vers un site malveillant, ou pièce jointe légitime (document PDF inoffensif) dans une reply-chain attack où le vrai piège est l'établissement de la confiance pour une demande ultérieure (BEC).

**La landing page.** Pour le credential harvesting, la landing page reproduit l'interface de connexion de la cible (Microsoft 365, Google Workspace, VPN d'entreprise, portail RH). Les kits de phishing modernes reproduisent ces interfaces pixel par pixel, y compris les certificats TLS (Let's Encrypt fournit des certificats gratuits — le cadenas vert ne garantit plus rien). Les techniques de reverse proxy (Evilginx, Modlishka) capturent non seulement les identifiants mais aussi les tokens de session, contournant ainsi le MFA classique (voir Ch.10 pour le détail).

#### 6.2 Niveaux de sophistication

Le phishing n'est pas une technique unique — c'est un spectre de sophistication dont chaque niveau a ses techniques, ses cibles et ses contre-mesures.

**Le phishing de masse (spray & pray).** Campagnes non ciblées envoyées à des dizaines de milliers d'adresses. Faible taux de réussite individuel (1-3 %), mais rentable par le volume. Les leurres sont génériques : notification de livraison, facture impayée, mise à jour de sécurité bancaire. Contre-mesures : filtrage email, sensibilisation de base, DMARC strict.

**Le spear-phishing.** Campagnes ciblées sur un groupe restreint (une entreprise, un service, un groupe de projet). Les leurres sont personnalisés : terminologie interne, noms de projets, références aux supérieurs hiérarchiques. Taux de réussite significativement supérieur (15-40 % selon la qualité de la personnalisation). Contre-mesures : filtrage avancé avec analyse comportementale, sensibilisation ciblée, bannières « email externe », simulation de phishing régulière.

**Le BEC/whaling.** Attaques ciblées de haute valeur (dirigeants, DAF, comptabilité). Pas de malware, pas de lien malveillant — pure manipulation par email. L'attaquant usurpe l'identité d'un dirigeant, d'un avocat ou d'un fournisseur pour obtenir un virement ou une information sensible. Taux de réussite variable mais impact unitaire très élevé (dizaines de milliers à dizaines de millions d'euros par incident). Contre-mesures : processus de double validation pour les virements, callback sur numéro connu, culture de la vérification. Le BEC est traité en détail au Ch.9.

#### 6.3 Construction d'un lure crédible

La crédibilité d'un lure de phishing repose sur quatre piliers : le contexte, le timing, la personnalisation et l'urgence calibrée.

**Le contexte.** Le meilleur lure s'inscrit dans un contexte que la cible attend ou connaît. Si l'entreprise est en pleine migration vers Microsoft 365, un email sur la mise à jour des identifiants sera perçu comme normal. Si une conférence sectorielle approche, une invitation de dernière minute sera crédible. La reconnaissance OSINT (Ch.5) fournit ces contextes.

**Le timing.** Le lundi matin (accumulation d'emails du week-end, traitement rapide), le vendredi après-midi (fatigue, volonté de conclure la semaine), la veille de vacances (stress de dernière minute, départs précipités), la période de clôture comptable (pression, urgence des validations) sont des fenêtres de vulnérabilité documentées.

**La personnalisation.** L'utilisation du nom du destinataire, de son service, de son manager, d'un projet sur lequel il travaille, d'un événement récent (formation, séminaire, réorganisation) augmente la crédibilité de manière exponentielle. Un email qui mentionne « suite à votre réunion avec Frédéric Morin hier » est perçu comme interne avant même d'être analysé.

**L'urgence calibrée.** L'urgence doit être suffisante pour déclencher une action rapide mais insuffisante pour paraître suspecte. « Veuillez valider avant fin de journée » est plus efficace que « URGENT — action immédiate requise !!!». L'urgence fonctionne en réduisant le temps disponible pour la réflexion et la vérification.

#### 6.4 L'infrastructure de phishing

La construction d'une infrastructure de phishing crédible est un savoir-faire technique qui évolue rapidement.

**Domaines lookalike et typosquatting.** L'enregistrement de domaines similaires à celui de la cible (heIios-aero.fr, helios-aero.com, helios-aeronautique.fr) permet de créer des adresses email et des URLs visuellement proches de l'original. Les domaines internationalisés (IDN — utilisant des caractères Unicode visuellement identiques aux caractères ASCII) ajoutent une couche de sophistication. Contre-mesure : surveillance proactive des enregistrements de domaines similaires, DMARC en mode « reject ».

**Compromission d'email légitime (reply-chain attack).** L'attaquant compromet une boîte mail réelle (par phishing préalable, credential stuffing ou achat sur le darkweb) et s'insère dans un fil de conversation existant. Cette technique est extrêmement difficile à détecter car l'email provient d'une adresse légitime, dans un fil de conversation légitime, avec un historique de conversation réel.

**Contournement de SPF/DKIM/DMARC.** SPF vérifie que le serveur d'envoi est autorisé par le domaine. DKIM signe cryptographiquement l'email. DMARC combine les deux et définit une politique de rejet. En configuration stricte (DMARC p=reject), ces protocoles bloquent le spoofing direct du domaine. Mais ils ne protègent pas contre le typosquatting, les domaines lookalike, le compromission d'email légitime ou le display name spoofing. La protection email est une défense en profondeur, pas une solution unique.

#### 6.5 Red team phishing vs attaquant réel

Le red teamer et l'attaquant réel utilisent les mêmes techniques — mais dans un cadre radicalement différent. Le red teamer documente chaque étape (emails envoyés, taux de clic, identifiants collectés, temps avant signalement), ne compromet pas réellement les systèmes (les identifiants collectés sont stockés de manière sécurisée et jamais exploités), produit un rapport factuel et constructif, et forme les employés sur les mécanismes exploités. L'attaquant réel exploite immédiatement les identifiants collectés, latéralise dans le réseau, exfiltre des données et peut persister pendant des mois. Cette différence de finalité est fondamentale, mais les techniques sont identiques — ce qui permet au red team d'évaluer la vulnérabilité réelle de l'organisation.

---

### Chapitre 7 — Vishing : l'arme de la voix

#### 7.1 Pourquoi le vishing est plus dangereux que le phishing

Le vishing (voice phishing) est, de l'avis consensuel des praticiens de red team, le vecteur de social engineering le plus efficace. Plusieurs facteurs expliquent cette efficacité supérieure au phishing par email.

La voix crée un lien personnel et immédiat. Un email est un objet passif que le destinataire peut analyser à son rythme, comparer avec des exemples connus, transférer à un collègue pour avis. Un appel téléphonique est une interaction en temps réel qui engage émotionnellement le destinataire et ne lui laisse pas le temps de la réflexion distanciée.

La pression est exercée en temps réel. L'attaquant ajuste son discours en fonction des réponses de la cible : s'il perçoit une hésitation, il renforce l'urgence ; s'il perçoit de la méfiance, il change d'angle ; s'il perçoit de la coopération, il escalade. Cette adaptabilité en temps réel est impossible par email.

L'autorité vocale est puissante. Un ton assuré, un vocabulaire technique maîtrisé, un rythme de parole contrôlé projettent une autorité que le texte écrit reproduit difficilement. L'expérience de Milgram a démontré que la présence physique (ou vocale) de la figure d'autorité augmente significativement la compliance.

La documentation est plus difficile. Un email suspect peut être transféré au SOC pour analyse (headers, URLs, pièces jointes). Un appel téléphonique ne laisse pas de trace exploitable (sauf enregistrement — qui pose des questions légales dans de nombreuses juridictions). Le signalement d'un appel suspect repose sur la mémoire et le récit de l'employé.

#### 7.2 Les pretextes classiques du vishing

Les pretextes de vishing les plus efficaces exploitent des situations où un appel téléphonique est attendu ou normal.

**Le support IT.** « Bonjour, je suis Paul de l'équipe support informatique. Nous avons détecté une activité suspecte sur votre compte — je dois vérifier quelques informations avec vous pour sécuriser votre accès. » Ce pretexte est redoutablement efficace parce qu'il combine autorité (IT), urgence (activité suspecte) et bienveillance (sécuriser votre compte). Le rapport Unit 42 2025 documente de nombreux cas où ce pretexte a permis le reset de credentials MFA via le helpdesk.

**Le prestataire ou fournisseur.** Après avoir identifié le prestataire IT par OSINT, l'attaquant se présente comme un technicien de ce prestataire pour une intervention planifiée ou d'urgence. La crédibilité est renforcée par la connaissance du nom du prestataire, du contrat en cours, des interlocuteurs habituels.

**La direction.** « Bonjour, je suis l'assistante de Marc Tessier. Il est en déplacement et il a besoin que vous fassiez un virement urgent — je vous envoie les coordonnées par email. » La combinaison appel + email (social engineering multi-canal, détaillé au Ch.8) renforce la crédibilité.

**Le recruteur.** Approche LinkedIn suivie d'un appel : « Suite à votre profil que j'ai trouvé très intéressant, j'ai une opportunité confidentielle à vous présenter. » Ce pretexte est le vecteur préféré des groupes APT comme Lazarus (opération « Dream Job ») et des services de renseignement pour l'élicitation (voir Ch.3 et Ch.17).

#### 7.3 Techniques vocales

La voix est un outil qui se travaille. Les red teamers expérimentés maîtrisent plusieurs techniques vocales qui augmentent l'efficacité du vishing.

**Le matching de ton.** Adapter son registre au profil de la cible : formel et technique avec un ingénieur, chaleureux et empathique avec une réceptionniste, directif et pressé avec un cadre. Le ton doit être cohérent avec le pretexte — un technicien IT qui parle comme un commercial ou un DG qui parle comme un stagiaire crée une dissonance cognitive qui active la vigilance.

**Le name-dropping.** Mentionner des noms de personnes réelles de l'organisation (collectés par OSINT) est l'un des marqueurs de crédibilité les plus puissants. « Frédéric Morin m'a demandé de vous appeler » ou « j'ai vu avec Lucie Ferraro hier » crée un lien implicite avec l'organisation qui désarme la méfiance.

**Le « oui building ».** Commencer par des questions auxquelles la réponse est évidemment « oui » (« c'est bien le poste de [nom] ? », « vous êtes bien dans le service [service] ? ») avant d'escalader vers la demande réelle. Chaque « oui » renforce l'engagement de la cible dans la conversation (principe d'engagement et de cohérence, Ch.2).

**Le silence stratégique.** Après avoir posé une question sensible, ne pas combler le silence. La plupart des gens sont mal à l'aise avec le silence dans une conversation téléphonique et le comblent en parlant — souvent en fournissant plus d'information que ce qui leur était demandé. Le silence est l'une des techniques d'élicitation les plus sous-estimées.

#### 7.4 Caller ID spoofing

Le caller ID spoofing permet à l'attaquant d'afficher un numéro de téléphone arbitraire sur l'écran de la cible. Des services en ligne (SpoofCard, SpoofTel — attention, l'usage est réglementé dans de nombreuses juridictions et interdit pour fraude) et des services VoIP configurables permettent de simuler le numéro du standard de l'entreprise, du prestataire IT ou même du supérieur hiérarchique.

Le protocole STIR/SHAKEN (Secure Telephony Identity Revisited / Signature-based Handling of Asserted information using toKENs), déployé aux États-Unis depuis 2021 et en cours de déploiement en Europe, vise à authentifier l'identité de l'appelant au niveau du réseau téléphonique. En 2025, son déploiement reste inégal et contournable dans certains contextes (appels internationaux, réseaux VoIP non conformes). La contre-mesure la plus fiable reste le callback de vérification : ne jamais agir sur la base d'un appel entrant sans rappeler l'interlocuteur sur un numéro de référence connu (annuaire interne, site web officiel).

#### 7.5 Le vishing AI-enabled : deepfake vocal

Le clonage vocal par IA représente la menace émergente la plus sérieuse en matière de vishing. En 2025, plusieurs plateformes permettent de cloner une voix à partir d'échantillons de quelques secondes à quelques minutes (ElevenLabs, Respeecher, technologies open source). La qualité est suffisante pour tromper un interlocuteur non prévenu dans un appel téléphonique standard.

Les cas documentés se multiplient. En 2024, une entreprise de Hong Kong a perdu 25 millions de dollars dans une fraude utilisant un deepfake vidéo et vocal du CFO en visioconférence (plusieurs « participants » étaient des deepfakes en temps réel). Des cas de vishing par deepfake vocal ciblant des DAF pour des virements urgents ont été rapportés par plusieurs cabinets d'incident response.

Les défenses sont encore immatures. Les détecteurs de deepfake vocal existent mais sont peu fiables en conditions réelles (environnement bruité, compression téléphonique, variété des technologies de synthèse). La défense la plus efficace reste procédurale : pour toute demande sensible (virement, reset de credentials, communication d'informations confidentielles), imposer une vérification out-of-band (callback sur numéro connu, confirmation par un second canal, validation hiérarchique). La technologie seule ne suffit pas — le processus est la dernière ligne de défense.

---

### Chapitre 8 — Smishing, messageries, collaboration et vecteurs alternatifs

#### 8.1 SMS et smishing

Le smishing (SMS phishing) exploite les spécificités du canal SMS : messages courts, contexte limité, URLs raccourcies qui masquent la destination réelle, et confiance instinctive dans les SMS (perçus comme plus personnels et plus fiables que les emails). Le spoofing d'expéditeur SMS (sender ID spoofing) permet d'afficher un nom d'entreprise (« Helios-RH », « IT-Support ») au lieu d'un numéro, ce qui renforce la crédibilité.

Les pretextes classiques incluent : notification de livraison avec lien de suivi, alerte bancaire avec demande de vérification, message RH sur les congés ou la paie, et alerte de sécurité (« accès suspect à votre compte »). Les taux de clic sur SMS sont généralement supérieurs à ceux sur email, parce que les utilisateurs mobiles sont moins entraînés à la vigilance sur ce canal et que les indicateurs de fraude (URL complète, en-têtes, adresse d'expéditeur) sont moins visibles sur un écran de smartphone.

#### 8.2 Messageries chiffrées et réseaux sociaux

WhatsApp, Signal, Telegram et les messageries intégrées des réseaux sociaux sont devenus des vecteurs de social engineering à part entière. Leur utilisation par les attaquants s'explique par plusieurs facteurs : le chiffrement de bout en bout complique la surveillance et l'analyse par les équipes de sécurité, le sentiment de confidentialité encourage le partage d'informations sensibles, et les fonctionnalités de messages éphémères réduisent les traces.

**LinkedIn InMail** est le vecteur de choix pour le ciblage professionnel. Les faux recruteurs (vecteur utilisé par le groupe APT Lazarus dans l'opération « Dream Job » et par des services de renseignement pour l'élicitation) exploitent la norme de la plateforme : recevoir un InMail d'un recruteur est un événement normal et positif sur LinkedIn. La transition vers WhatsApp ou Signal (« pour discuter plus librement ») isole la cible du contexte professionnel et élimine les contrôles de la plateforme.

**Les groupes** sur Telegram, Discord et WhatsApp sont exploités pour le social engineering de masse ciblé : infiltrer un groupe professionnel ou communautaire permet de gagner de la crédibilité par la présence dans un espace de confiance, de collecter de l'information en écoutant les conversations, et d'approcher des cibles individuelles avec un pretexte renforcé (« on est dans le même groupe sur le forum X »).

#### 8.3 Suites collaboratives : Teams, Slack, Google Workspace

Les plateformes de collaboration d'entreprise sont devenues des vecteurs de social engineering majeurs depuis la généralisation du travail hybride. Le rapport Unit 42 2025 documente plusieurs cas d'intrusions initiées via ces plateformes.

**Microsoft Teams.** L'ouverture des communications externes (External Access) permet à un attaquant d'envoyer des messages à des employés depuis un tenant Microsoft 365 externe. L'interface Teams affiche un avertissement « externe » souvent ignoré. Les pretextes incluent : partage de document « urgent » (lien vers une landing page de phishing), invitation à une réunion (lien Zoom/Meet malveillant), et prise de contact par un faux collègue d'un autre site ou d'un partenaire.

**Faux partages de documents.** Les notifications OneDrive/SharePoint/Google Drive « [Nom] a partagé un document avec vous » sont exploitées pour le phishing. L'attaquant crée un document sur sa propre instance et le partage avec la cible. Le lien pointe vers une page de connexion légitime (Microsoft ou Google) qui capture les identifiants ou les tokens de session. La difficulté est que le mécanisme de partage est identique au mécanisme légitime — seule l'analyse de l'expéditeur et du contexte permet de distinguer un partage légitime d'un phishing.

**OAuth consent phishing (consent grant attack).** L'attaquant crée une application OAuth malveillante qui demande des permissions d'accès au compte de la cible (lecture des emails, accès aux fichiers, accès au calendrier). La cible est redirigée vers une page de consentement légitime (Microsoft ou Google) et autorise l'accès — l'attaquant obtient alors un token d'accès persistant qui survit au changement de mot de passe et au MFA. Cette technique est particulièrement insidieuse parce que la page de consentement est une page légitime de Microsoft ou Google, pas une page de phishing. La défense repose sur la restriction des applications tierces autorisées (Azure AD : désactiver le consentement utilisateur, imposer l'approbation admin) et la surveillance des grants OAuth.

**Faux bots et automatisations.** Les plateformes comme Slack et Teams permettent l'intégration de bots et de workflows automatisés. Un attaquant qui compromet un workspace ou obtient un accès admin peut créer un faux bot (« Security-Bot », « HR-Assistant ») qui collecte des informations auprès des employés sous un pretexte automatisé.

#### 8.4 QR codes malveillants (quishing)

Le quishing exploite les QR codes comme vecteur de redirection. L'utilisation massive des QR codes depuis 2020 (menus de restaurant, documents administratifs, affiches événementielles) a normalisé le scan de QR codes inconnus — ce qui constitue un vecteur d'attaque sous-estimé.

Les vecteurs de distribution incluent : QR codes physiques collés sur des panneaux légitimes (parking d'entreprise, accueil, salles de réunion), QR codes inclus dans des emails de phishing (contournant les filtres URL qui ne scannent pas les images), QR codes dans des documents imprimés (faux courriers RH, fausses affiches d'événement). La redirection pointe vers une landing page de credential harvesting ou un téléchargement de malware mobile.

La défense passe par la sensibilisation (ne pas scanner de QR code sans vérifier l'URL de destination — les smartphones modernes affichent l'URL avant la navigation), l'utilisation de QR codes sécurisés pour les communications légitimes de l'entreprise, et l'inspection physique régulière des QR codes affichés dans les locaux.

#### 8.5 Social engineering multi-canal

La combinaison de plusieurs vecteurs dans une même opération augmente considérablement la crédibilité et le taux de succès. Le schéma typique est : email préparatoire → appel téléphonique → SMS de confirmation, ou approche LinkedIn → transition WhatsApp → appel téléphonique → demande par email.

Chaque canal renforce la crédibilité du précédent. Un email seul peut être analysé froidement. Mais un email suivi d'un appel téléphonique (« je vous appelle suite à l'email que je vous ai envoyé ce matin ») crée un effet de convergence qui désarme la vigilance — la cible perçoit une cohérence entre deux canaux distincts, ce qui renforce la perception de légitimité. Le rapport Unit 42 2025 documente cette hybridation croissante des tactiques où les techniques conventionnelles de social engineering sont de plus en plus complétées par des composantes multi-canaux.

---

### Chapitre 9 — BEC (Business Email Compromise) et fraude au président

#### 9.1 Le BEC comme menace n°1 en pertes financières

Le Business Email Compromise est la forme de cybercriminalité la plus coûteuse au monde en termes de pertes financières directes. Les données de l'IC3 (Internet Crime Complaint Center) du FBI indiquent des pertes cumulées de plusieurs milliards de dollars par an aux États-Unis seuls. En France, les pertes liées à la fraude au président et aux arnaques au fournisseur se chiffrent en centaines de millions d'euros annuellement.

Le BEC est redoutable parce qu'il ne repose sur aucun composant technique sophistiqué : pas de malware, pas de vulnérabilité logicielle, pas de zero-day. C'est une attaque de pure manipulation humaine — un email suffisamment crédible pour déclencher un virement vers un compte contrôlé par l'attaquant. La détection technique est donc intrinsèquement limitée : l'email ne contient ni lien malveillant ni pièce jointe piégée — seulement du texte convaincant.

#### 9.2 Les variantes du BEC

**La fraude au président (CEO fraud).** L'attaquant usurpe l'identité du dirigeant de l'entreprise et ordonne un virement urgent et confidentiel au responsable financier ou au comptable. Les éléments clés sont : l'urgence (« c'est pour une acquisition confidentielle, il faut agir avant 17h »), la confidentialité (« n'en parlez à personne d'autre — c'est stratégique et sensible »), l'autorité (le DG qui s'adresse directement à un subordonné en court-circuitant la hiérarchie normale) et la pression émotionnelle (« je compte sur vous personnellement »).

**La fraude au fournisseur (vendor email compromise).** L'attaquant se fait passer pour un fournisseur existant et envoie une facture avec des coordonnées bancaires modifiées. La technique est souvent précédée par la compromission de la boîte mail du fournisseur réel (reply-chain) ou par l'enregistrement d'un domaine lookalike. La détection est rendue difficile par le fait que la relation commerciale est réelle — seul l'IBAN a changé.

**La compromission de boîte mail (reply-chain BEC).** L'attaquant compromet une boîte mail interne ou celle d'un partenaire et s'insère dans des fils de conversation existants pour demander des virements ou des modifications de coordonnées bancaires. Cette variante est la plus difficile à détecter parce que l'email provient d'une adresse légitime avec un historique de conversation réel.

**Le faux avocat.** L'attaquant se présente comme un avocat ou un conseiller juridique intervenant dans le cadre d'une transaction confidentielle (acquisition, règlement de litige). La confidentialité est utilisée comme arme : « en raison de la sensibilité juridique de cette opération, je vous demande de ne pas en discuter avec vos collègues ». Cette tactique isole la cible et neutralise le réflexe de vérification.

#### 9.3 La construction de l'arnaque

Le BEC réussi repose sur une reconnaissance approfondie. L'attaquant identifie : l'organigramme (qui a le pouvoir de valider un virement, qui est le supérieur hiérarchique direct), les processus de validation financière (seuils, doubles signatures, circuits de validation), les habitudes de communication du dirigeant usurpé (ton, style, formules de politesse, horaires d'envoi), et les fenêtres d'opportunité (déplacement du DG — vérifiable par LinkedIn, agenda public, conférences ; absence du DAF ; périodes de clôture comptable).

Le timing est critique. Le vendredi après-midi (les virements envoyés le vendredi ne sont pas vérifiés avant lundi), la veille de vacances, les périodes de déplacement du dirigeant (impossible de vérifier en personne) sont les fenêtres les plus exploitées.

#### 9.4 Deepfake et BEC

L'utilisation de deepfakes vidéo et vocaux dans les BEC représente une évolution qualitative de la menace. Le cas de Hong Kong de début 2024, où une entreprise a perdu l'équivalent de 25 millions de dollars suite à une visioconférence entièrement composée de deepfakes en temps réel, illustre le potentiel destructeur de cette convergence. L'employé ciblé a participé à un appel vidéo où plusieurs participants — dont le CFO — étaient des deepfakes générés en temps réel. La qualité était suffisante pour ne pas éveiller de soupçon pendant toute la durée de l'appel.

Cette évolution remet en question les défenses traditionnelles du BEC. Le callback vocal était considéré comme une contre-mesure fiable — mais si la voix de l'interlocuteur peut être clonée, le callback perd son pouvoir de vérification. La réponse passe par des vérifications multi-facteurs non reproductibles par l'IA : question de sécurité personnelle, vérification physique en présentiel, code de confirmation envoyé par un canal distinct et préétabli.

#### 9.5 Défense contre le BEC

La défense contre le BEC est fondamentalement procédurale, pas technologique. Les solutions techniques (détection d'anomalies dans les emails, alerte sur les changements de comportement d'expéditeur) sont utiles mais insuffisantes face à des attaques qui n'utilisent aucun indicateur technique malveillant.

**P0 — Processus de double validation pour tout virement inhabituel.** Aucun virement supérieur à un seuil défini ne peut être exécuté sans validation par deux personnes distinctes, dont au moins une par callback sur un numéro de référence connu (annuaire interne, pas le numéro indiqué dans l'email).

**P0 — Procédure de vérification des changements de coordonnées bancaires.** Tout changement d'IBAN (fournisseur, prestataire, client) fait l'objet d'un callback au fournisseur sur un numéro de référence connu, indépendamment du canal par lequel le changement a été demandé.

**P1 — Formation ciblée.** Les profils à risque (DAF, comptabilité, assistantes de direction, service achats) reçoivent une formation spécifique sur les scénarios de BEC avec des simulations réalistes.

**P1 — Alertes techniques.** Règles email signalant les emails d'expéditeurs externes utilisant des display names identiques à ceux de dirigeants internes, bannières « email externe » clairement visibles, alertes sur les domaines lookalike.

**P2 — Culture de la vérification.** Créer un environnement où vérifier une demande — même du DG — est perçu comme professionnel, pas comme de l'insubordination.

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 3**
>
> **Campagne de phishing.** Yasmine lance la campagne de phishing ciblé depuis l'infrastructure de test (domaine enregistré : heIios-rh.fr — « I » majuscule au lieu de « l »). Deux pretextes sont utilisés :
>
> **Pretexte 1** — « Mise à jour obligatoire du portail RH — Entretien annuel 2025 ». Email reproduisant le template visuel d'Helios (couleurs et logo récupérés sur le site web), renvoyant vers une page de connexion Microsoft 365 factice. Envoyé à 80 employés du siège et de Bordeaux le lundi matin à 8h15.
>
> **Pretexte 2** — « Invitation conférence Aéronautique & Défense — Lyon, juin 2025 ». Email ciblé sur 40 ingénieurs R&D et cadres, exploitant l'intérêt professionnel et la curiosité.
>
> **Résultats après 72h** : sur 120 emails envoyés, 34 clics (28,3 %), 18 identifiants collectés (15 %), dont 2 comptes avec des privilèges administrateurs IT (un admin Exchange et un admin Azure AD). Taux de signalement au SOC : 3 emails signalés (2,5 %) — tous dans les 4 premières heures, puis plus rien.
>
> Lucie Ferraro, la RSSI, est surprise par les résultats : « On fait des campagnes de sensibilisation e-learning chaque trimestre depuis deux ans. Les scores au quiz sont bons. » Nathan explique : « Le quiz mesure la reconnaissance théorique des signaux de phishing dans un contexte d'examen. Notre campagne mesure le comportement réel face à un leurre crédible, en conditions de stress et de multitâche. Ce sont deux choses différentes. »

---

### Chapitre 10 — Intrusion numérique par social engineering : identité, SSO, MFA et workflows

#### 10.1 Social engineering du helpdesk

Le helpdesk est la surface d'attaque la plus sous-estimée en matière de social engineering numérique. Les techniciens de support sont formés à résoudre les problèmes rapidement et avec courtoisie — deux objectifs qui entrent en conflit direct avec la sécurité lorsqu'un attaquant appelle en se faisant passer pour un employé bloqué.

Le scénario classique est le reset de credentials. L'attaquant appelle le helpdesk en se faisant passer pour un employé dont il a collecté les informations par OSINT (nom, poste, manager, identifiant employé si disponible) et demande un reset de mot de passe ou un reset de MFA. Si les procédures de vérification d'identité du helpdesk sont faibles (questions auxquelles les réponses sont trouvables en OSINT — date de naissance, nom du manager, identifiant employé), l'attaquant obtient un accès légitime au compte de l'employé.

Le rapport Unit 42 2025 documente plusieurs cas graves. Dans un cas, un attaquant a contacté le helpdesk à plusieurs reprises, chaque appel affinant le pretexte avec les informations glanées lors des appels précédents. Après avoir passé les vérifications d'identité, il a obtenu un reset MFA qui lui a donné accès aux systèmes internes. L'ensemble des actions post-compromission mimait un comportement utilisateur légitime, évitant de déclencher les alertes EDR.

**Défense P0** : les procédures de helpdesk pour les resets de credentials doivent inclure des vérifications que l'attaquant ne peut pas contourner par OSINT. Exemples : callback sur le numéro de téléphone enregistré dans l'annuaire (pas celui fourni par l'appelant), vérification en personne pour les comptes à privilèges, validation par le manager direct, utilisation de codes de vérification préétablis.

#### 10.2 Le détournement de MFA

Le MFA (Multi-Factor Authentication) est une défense essentielle, mais il n'est pas infaillible face au social engineering.

**Le phishing en temps réel (reverse proxy).** Des outils comme Evilginx2, Modlishka et Muraena permettent de créer des proxies qui s'interposent entre la cible et le service légitime (Microsoft 365, Google Workspace). La cible saisit ses identifiants et son code MFA sur ce qui semble être la page de connexion légitime — mais le proxy capture le token de session authentifié. L'attaquant peut alors utiliser ce token pour accéder au compte sans avoir besoin de re-passer le MFA. Cette technique contourne toutes les formes de MFA basées sur des codes (OTP, push notification) — seul le MFA résistant au phishing (FIDO2/WebAuthn, qui vérifie l'origine du domaine) est immunisé.

**La push fatigue (MFA bombing).** L'attaquant, qui possède déjà les identifiants de la cible (obtenus par phishing, credential stuffing ou achat sur le darkweb), déclenche des demandes de validation MFA push en série. Submergé par les notifications, l'employé finit par approuver une demande — soit par lassitude, soit par erreur, soit pour « faire cesser les notifications ». Certains systèmes modernes (Microsoft Authenticator, Duo) ont implémenté des contre-mesures : number matching (l'utilisateur doit saisir un code affiché à l'écran, pas simplement approuver) et limitation du nombre de notifications.

**Le device code phishing.** Cette technique exploite le flux d'authentification « device code flow » de OAuth2, conçu pour les appareils sans navigateur (TV connectées, IoT). L'attaquant génère un code de device et envoie un lien à la cible (par phishing, vishing ou messagerie) en lui demandant de s'authentifier avec ce code. La cible se connecte sur une page Microsoft ou Google légitime et saisit le code — l'attaquant obtient un token d'accès. Cette technique est particulièrement insidieuse parce que la page d'authentification est 100 % légitime.

#### 10.3 Exploitation des processus d'onboarding et d'offboarding

Les processus d'arrivée (onboarding) et de départ (offboarding) sont des fenêtres de vulnérabilité structurelles.

En phase d'onboarding, un attaquant peut se présenter comme un nouvel employé ou un nouveau prestataire pour obtenir des identifiants, un badge d'accès ou un poste de travail. Si le processus d'onboarding ne comporte pas de vérification robuste de l'identité (photo sur le contrat, validation par le manager, vérification d'identité officielle), l'usurpation est possible. Les cas de DPRK IT workers (travailleurs nord-coréens utilisant des identités fictives pour se faire embaucher comme freelances dans des entreprises technologiques) illustrent cette menace à un niveau de sophistication extrême.

En phase d'offboarding, les comptes non désactivés, les accès VPN non révoqués, les sessions OAuth non terminées constituent des portes d'entrée pour un attaquant qui a obtenu les identifiants d'un ancien employé (par social engineering de l'ancien employé lui-même, ou par achat de credentials).

#### 10.4 La compromission de la supply chain humaine

La supply chain humaine — l'ensemble des prestataires, fournisseurs et sous-traitants qui ont un accès physique ou logique aux systèmes de l'organisation — est une surface d'attaque souvent négligée.

Le nettoyage de nuit a accès à tous les bureaux. La maintenance informatique a accès aux locaux serveurs. Le traiteur a accès à la cuisine et souvent aux couloirs. Le prestataire de reprographie a accès à des documents confidentiels. Cibler ces prestataires (par social engineering direct ou par compromission de leurs systèmes) permet un accès indirect à l'organisation cible avec un niveau de contrôle souvent inférieur à celui appliqué aux employés internes.

#### 10.5 Red team scenarios et résultats typiques

Les résultats des tests de social engineering numérique sont systématiquement supérieurs aux attentes des commanditaires. Les taux de clic sur les campagnes de spear-phishing bien construites se situent typiquement entre 15 % et 40 %. Les taux de soumission d'identifiants (credential harvesting) entre 8 % et 25 %. Les tentatives de reset de credentials via le helpdesk réussissent dans 30 % à 60 % des cas si les procédures ne sont pas renforcées. Ces chiffres ne reflètent pas l'incompétence des employés — ils reflètent la qualité de la personnalisation et la puissance des leviers psychologiques exploités.

---

### Chapitre 11 — Capstone Partie II : campagne de social engineering numérique complète

**Exercice intégrateur.** L'étudiant doit planifier et documenter une campagne de social engineering numérique multi-vecteurs contre une organisation fictive (entreprise de services financiers, 500 employés, 2 sites).

**Livrables attendus :**
1. Dossier de reconnaissance OSINT (sources exploitées, informations collectées, organigramme reconstitué, terminologie interne identifiée)
2. Construction de 3 pretextes (1 phishing, 1 vishing, 1 smishing) avec justification du choix de chaque pretexte et analyse des leviers psychologiques exploités
3. Infrastructure technique (domaines, landing pages, caller ID — description, pas déploiement)
4. Scénario d'exécution (chronologie, séquence multi-canal, points de décision)
5. Estimation des résultats attendus (taux de clic, taux de compromission) avec justification
6. Rapport type red team (résultats, impact potentiel si exploitation réelle, recommandations P0/P1/P2)

**Erreur fréquente** : produire un plan trop ambitieux (trop de vecteurs, trop de cibles) sans profondeur sur chaque composante. Un bon plan de campagne est focalisé et réaliste, pas exhaustif.


---

## PARTIE III — SOCIAL ENGINEERING PHYSIQUE

---

### Chapitre 12 — Reconnaissance physique et planification

#### 12.1 La reconnaissance du site

La reconnaissance physique complète la reconnaissance OSINT et fournit les informations nécessaires à la planification de l'intrusion. Elle se conduit en plusieurs passes, idéalement sur plusieurs jours et à différentes heures.

**Le périmètre.** Identifier toutes les entrées (accueil principal, livraisons, parking souterrain, accès technique, sortie de secours), leur niveau de contrôle (gardien, badge, interphone, portique, tourniquet), et les zones de transition (fumoir, parking, accès cantine externe). Les sorties de secours, souvent équipées d'alarme mais pas toujours surveillées, sont des points d'intérêt fréquents pour les red teamers.

**Les systèmes de contrôle d'accès.** Observer le type de lecteur (RFID basse fréquence 125 kHz — HID ProxCard, facile à cloner ; RFID haute fréquence 13.56 MHz — MIFARE, iCLASS, plus résistant ; NFC mobile), la présence de biométrie (empreintes, iris — rare en entreprise standard), les sas anti-piggyback (tourniquets, portiques à verrouillage unitaire). Les caméras : identifier leur emplacement, leur angle de couverture, la présence de zones d'ombre, et déterminer si elles sont en monitoring live (opérateur présent) ou en enregistrement passif (consultation a posteriori uniquement).

**Les horaires et les flux.** Les heures d'arrivée (8h-9h30 — flux maximum, contrôles relâchés) et de départ (17h-18h30), les pauses (12h-14h — mouvements entre bâtiments, accès cantine), les livraisons (généralement matin, accès souvent moins contrôlé). Le créneau idéal pour une intrusion physique est souvent 10h-11h ou 14h-15h : assez de monde dans les locaux pour ne pas être remarqué, mais assez calme pour éviter les flux où un inconnu serait plus visible.

#### 12.2 L'observation comportementale

Au-delà de l'infrastructure physique, le red teamer observe les comportements des employés, qui constituent souvent la vulnérabilité principale.

**Le badge.** Les employés portent-ils leur badge de manière visible (autour du cou, au revers) ? Ou le gardent-ils dans leur poche/portefeuille et le présentent uniquement au lecteur ? Un environnement où le badge n'est pas porté visiblement est un environnement où un intrus sans badge ne sera pas immédiatement repéré.

**Le tailgating naturel.** Les employés tiennent-ils la porte aux personnes derrière eux ? Vérifient-ils le badge de la personne qui les suit ? Dans la grande majorité des entreprises, la norme sociale est de tenir la porte — refuser est perçu comme impoli.

**La vérification des visiteurs.** Les visiteurs sont-ils systématiquement accompagnés ? Ou sont-ils libres de se déplacer après le passage à l'accueil ? Les badges visiteurs sont-ils visuellement distincts des badges employés ? Sont-ils récupérés en fin de visite ?

**Les zones informelles.** Le fumoir, le café, la cantine sont des zones de socialisation où les barrières de sécurité sont naturellement abaissées. Ce sont les points de contact idéaux pour l'élicitation (Ch.14).

#### 12.3 Le dumpster diving

La fouille des poubelles (dumpster diving) reste une technique de reconnaissance basique mais efficace. Les poubelles extérieures (sur le trottoir ou dans la zone de collecte) ne sont généralement pas protégées juridiquement (la jurisprudence varie selon les pays — en France, la fouille de poubelles sur la voie publique n'est pas constitutive d'une infraction ; en revanche, pénétrer dans une propriété privée pour accéder aux poubelles constitue une violation de domicile).

Les trouvailles typiques incluent : documents imprimés non déchiquetés (organigrammes, listes de diffusion, procès-verbaux de réunion, rapports intermédiaires), badges expirés (qui peuvent servir de modèle pour la fabrication d'un faux badge visuellement crédible), post-its avec des mots de passe ou des codes, matériel informatique mis au rebut (disques durs non effacés, clés USB, téléphones), et emballages de matériel révélant les technologies utilisées (cartons de serveurs, de switches, d'équipements de sécurité).

**Défense** : politique de destruction documentaire (déchiqueteuse cross-cut minimum — les déchiqueteuses en bandes sont reconstructibles), bennes fermées et cadenassées, sensibilisation au risque des documents jetés sans précaution.

#### 12.4 Le matériel du red teamer

La préparation matérielle est critique pour la crédibilité du pretexte et le succès de l'opération.

**La tenue.** Adaptée au pretexte : costume et cravate pour un « auditeur » ou un « consultant », polo logotypé et jean pour un « technicien IT », bleu de travail et gilet haute visibilité pour un « prestataire de maintenance ». Le gilet haute visibilité est l'un des outils les plus puissants du social engineering physique : il confère une légitimité quasi automatique et réduit les questions.

**Le faux badge.** Les badges d'entreprise sont rarement vérifiés visuellement en détail au-delà de la couleur et de la présence d'un logo. Un badge imprimé sur un support similaire (même taille, même orientation, couleur cohérente, logo de l'entreprise récupéré en OSINT) suffit dans la majorité des cas pour l'examen visuel. Le badge ne passera pas un contrôle RFID si la technologie n'est pas clonée (Ch.27), mais dans les environnements où le badge est présenté visuellement (à un gardien) plutôt qu'électroniquement (sur un lecteur), la version imprimée est suffisante.

**Le clipboard.** Le « bouclier social » par excellence. Une personne qui se déplace dans des locaux avec un clipboard (ou un ordinateur portable et une mine concentrée) n'est presque jamais questionnée. Le clipboard projette l'image de quelqu'un en mission, qui a quelque chose à faire et qui sait où il va.

**Les outils techniques.** Dans le cadre d'un red team autorisé : implants réseau (LAN Turtle, rogue access point WiFi), clé USB malveillante (Rubber Ducky, Bash Bunny), keylogger hardware, lecteur RFID (Proxmark3 pour le clonage — voir Ch.27). Ces outils sont transportés discrètement et déployés une fois l'accès physique obtenu.

#### 12.5 Le plan d'intrusion

Le plan d'intrusion est un document opérationnel qui couvre : les objectifs (accès à une zone spécifique, connexion d'un implant réseau, accès à un poste de travail, vol simulé d'un document classifié), le timing (jour, heure, durée maximale de présence), les pretextes (principal + au moins un pretexte de secours en cas d'échec du premier), le matériel nécessaire, le plan d'exfiltration (comment quitter les lieux proprement), et le protocole d'urgence.

Le **protocole d'urgence** est indispensable. Si le red teamer est intercepté, confronté ou arrêté par la sécurité, il doit pouvoir s'identifier immédiatement comme testeur autorisé. Le « safe word » est un mot ou une phrase convenu avec le commanditaire qui, prononcé au téléphone avec le contact de référence, confirme instantanément la légitimité de la mission. Le contact de référence (RSSI, DG, ou personne désignée) doit être joignable 24/7 pendant la durée du test.

---

### Chapitre 13 — Techniques d'intrusion physique

#### 13.1 Le tailgating et le piggybacking

Le tailgating (suivre un employé à travers une porte contrôlée) est la technique d'intrusion physique la plus simple et statistiquement la plus efficace. Les gens tiennent la porte par politesse — c'est une norme sociale profondément ancrée que même les programmes de sensibilisation les plus rigoureux peinent à modifier.

La technique est élémentaire : attendre qu'un employé badge et ouvre une porte, puis le suivre en maintenant un flux naturel. Le succès dépend du timing (arriver juste derrière, pas trop loin pour ne pas être remarqué), du comportement (confiant, pressé, naturel — ne pas hésiter, ne pas regarder autour de soi de manière suspecte), et de l'apparence (tenue cohérente avec l'environnement).

Le piggybacking est une variante où le red teamer engage activement la conversation avec l'employé pendant l'approche de la porte, créant un lien social qui rend le refus d'accès encore plus improbable (« après vous — vous avez vu, ils ont encore changé le code du parking ! »).

**Contre-mesures** : tourniquets unitaires (sas qui ne laissent passer qu'une personne par badge), portiques de sécurité avec détection anti-passback, sensibilisation ciblée du personnel (autorisation de refuser poliment — « désolé, c'est la procédure, chacun doit badger »), culture où la vérification n'est pas perçue comme impolie.

#### 13.2 L'impersonation

L'impersonation — se faire passer pour quelqu'un d'autre — est le cœur du social engineering physique. La crédibilité du pretexte est tout. Les pretextes les plus efficaces exploitent des rôles qui ont un accès légitime aux locaux et qui ne sont pas questionnés.

**Le prestataire IT.** Après identification du prestataire par OSINT, le red teamer se présente comme un technicien de ce prestataire pour une intervention planifiée ou d'urgence. Crédibilité renforcée par : un polo ou un gilet aux couleurs du prestataire (imprimé pour l'occasion), un faux bon d'intervention, le name-dropping du responsable IT interne et du responsable de compte chez le prestataire.

**L'inspecteur.** Inspecteur incendie, inspecteur sanitaire, auditeur qualité, contrôleur réglementaire — ces rôles confèrent une autorité qui réduit les questions. L'inspecteur est attendu, ou il arrive par surprise — dans les deux cas, il est rarement refusé.

**L'employé d'un autre site.** Dans les organisations multi-sites, les employés ne connaissent pas personnellement les collègues des autres sites. « Je suis Thomas du bureau de Paris, je suis venu pour la réunion avec Jean-Marc Duval — je ne retrouve pas la salle de réunion 3B » est un pretexte simple et efficace.

**Le visiteur.** Un faux rendez-vous avec un responsable identifié par OSINT, annoncé la veille par un appel de « l'assistante » (complice) au standard. Si le rendez-vous est enregistré dans le système de gestion des visiteurs, le red teamer reçoit un badge visiteur légitime.

#### 13.3 La manipulation des gardiens et réceptionnistes

Les gardiens et réceptionnistes sont la première ligne de défense physique — et souvent la plus vulnérable. Ils sont formés à l'accueil et à la courtoisie, rarement au contre-social engineering.

Les techniques de manipulation incluent : le **name-dropping** (« je viens voir Frédéric Morin, on a un rendez-vous à 14h »), la **création d'urgence** (« mon technicien est déjà à l'intérieur, il m'attend dans le local serveur — c'est urgent, on a une panne de production »), l'**appel de confirmation** (un complice appelle le standard pendant que le red teamer est à l'accueil et confirme sa venue : « oui, c'est le technicien qu'on attend, faites-le monter »), et la **sympathie** (« je suis vraiment désolé de vous embêter, j'ai un problème de badge, ça fait 20 minutes que je suis bloqué dehors — vous pouvez m'ouvrir le temps que l'IT me refasse un badge ? »).

#### 13.4 L'exploitation des badges

Le clonage de badges RFID est une technique de red team courante dont la faisabilité dépend fortement de la technologie utilisée.

**RFID basse fréquence (125 kHz)** — HID ProxCard, EM4100 : facilement clonable avec un Proxmark3, un Flipper Zero ou même des lecteurs/graveurs basiques disponibles en ligne. La lecture peut se faire à distance de quelques centimètres (suffisant pour lire un badge dans la poche d'un employé qui passe près de vous) et la copie sur un badge vierge prend quelques secondes.

**RFID haute fréquence (13.56 MHz)** — MIFARE Classic, MIFARE DESFire, iCLASS : plus résistant au clonage. MIFARE Classic a des faiblesses cryptographiques connues qui permettent le clonage avec un Proxmark3, mais les versions plus récentes (DESFire EV2/EV3) utilisent un chiffrement robuste. iCLASS Standard est également vulnérable, mais iCLASS SE est significativement plus résistant.

**NFC mobile et badges virtuels** — Apple Wallet, Google Wallet : difficiles à cloner car protégés par la cryptographie du smartphone. C'est l'une des raisons de la migration progressive vers les badges mobiles dans les entreprises à sécurité renforcée.

La défense contre le clonage passe par la migration vers des technologies résistantes (DESFire EV2+, badges mobiles), la combinaison badge + biométrie pour les zones sensibles, la détection des anomalies d'accès (même badge utilisé à deux endroits simultanément, accès à des heures inhabituelles) et l'audit régulier du parc de badges.

#### 13.5 Le non-verbal et la crédibilité comportementale

En social engineering physique, le corps et le comportement comptent autant que le scénario. Un pretexte parfait sera ruiné par un comportement hésitant, un regard fuyant ou une posture qui trahit le stress.

**La proxémie.** La gestion de la distance interpersonnelle est culturellement déterminée, mais en contexte professionnel français, une distance de 80 cm à 1,2 m est la norme pour une interaction professionnelle. Trop proche : inconfort et suspicion. Trop loin : désengagement et manque de crédibilité.

**La posture.** Dos droit, épaules ouvertes, démarche assurée, regard droit. Le red teamer qui se déplace comme s'il connaissait les lieux ne sera pas questionné. Celui qui hésite à un croisement, regarde les plaques de porte, ou consulte son téléphone avec l'air perdu sera immédiatement repéré par un gardien attentif.

**Le tempo.** La vitesse de déplacement doit être cohérente avec le pretexte. Un « technicien en intervention urgente » se déplace vite et avec détermination. Un « auditeur en visite » se déplace calmement et observe. Un « employé qui va au café » est décontracté.

**La gestion du regard.** Contact visuel bref et naturel avec les personnes croisées (ni évitement ni insistance). Un hochement de tête accompagné d'un « bonjour » suffit à créer un micro-rapport qui désarme la suspicion.

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 4**
>
> **Intrusion physique — Site de Bordeaux.** Nathan se présente à l'entrée du site de production de Bordeaux le mardi à 10h30. Tenue : polo gris avec logo brodé de « NetServ Solutions » (le prestataire de maintenance informatique identifié par OSINT — le polo a été imprimé la veille). Badge visiteur visuellement crédible (format Helios, photo de Nathan, nom « T. Beaumont — NetServ Solutions »). Clipboard avec un faux bon d'intervention mentionnant « vérification connectique baie serveur B2 — ref. ticket #NS-2025-0847 ».
>
> Le gardien, Jean-Pierre, vérifie la liste des interventions planifiées. Nathan n'y figure pas. « C'est bizarre, j'ai le ticket ici, c'est Jean-Marc Duval qui l'a ouvert vendredi. Il y a un switch qui pose problème dans la baie B2 depuis la semaine dernière. » Jean-Pierre hésite. Nathan sort son téléphone : « Attendez, je vais appeler mon responsable de compte. » Il appelle Thomas (son complice), qui répond : « Oui, c'est l'intervention NT-0847 pour Helios Bordeaux, technicien Beaumont. C'est bien planifié chez nous, peut-être un oubli de validation côté client. » Jean-Pierre consulte son écran une dernière fois, puis : « Allez-y, vous connaissez le chemin vers le local serveur ? — Oui, bâtiment B, au fond à droite. Merci Jean-Pierre. »
>
> En 45 minutes, Nathan connecte un implant réseau (Raspberry Pi configuré comme rogue access point) dans la baie serveur, prend des photos de trois salles de réunion (post-its sur les écrans avec mots de passe WiFi et codes de salle visioconférence), et photographie le tableau d'affichage du couloir RH (planning des absences, organigramme du site, numéros de téléphone internes).

---

### Chapitre 14 — Élicitation en face-à-face

#### 14.1 Définition et fondements

L'élicitation est l'extraction d'information dans le cadre d'une conversation apparemment normale et non menaçante. La cible ne sait pas qu'elle est interrogée — elle pense participer à une conversation ordinaire. C'est précisément ce qui rend l'élicitation si efficace et si difficile à détecter : il n'y a ni demande explicite suspecte, ni canal d'attaque technique, ni pièce jointe à analyser — seulement une conversation.

L'agence américaine NSA définit l'élicitation comme « l'extraction subtile d'information au cours d'une conversation apparemment normale et innocente ». Cette définition est opérationnellement exacte : le succès de l'élicitation repose sur le fait que la cible perçoit l'échange comme naturel, réciproque et bienveillant.

L'élicitation fonctionne pour des raisons psychologiques documentées : la plupart des gens souhaitent être perçus comme compétents et bien informés (ego), désirent aider un interlocuteur sympathique (réciprocité, politesse), sont mal à l'aise avec le silence et le comblent en parlant (anxiété sociale), et ne mentent pas spontanément quand la conversation semble anodine (honnêteté par défaut).

#### 14.2 Les techniques d'élicitation

**La question ouverte.** « Comment se passe le projet de migration ? » La question ouverte invite un développement libre — la cible choisit les détails qu'elle partage, ce qui donne l'impression de contrôle alors que l'éliciteur oriente la conversation vers les sujets d'intérêt.

**La provocation (deliberate false statement).** Affirmer volontairement quelque chose de faux pour provoquer une correction. « J'ai entendu dire que vous migriez vers SAP S/4HANA ? » Si la réponse est « Non, on est sur Oracle depuis janvier, c'est tout nouveau », l'éliciteur a obtenu une information technique spécifique sans l'avoir demandée — la cible l'a « corrigé » spontanément. Cette technique exploite le besoin de précision et la difficulté à laisser une erreur non corrigée.

**La flatterie ciblée.** « Vous êtes probablement la personne la mieux placée pour comprendre ce sujet dans l'entreprise. » La flatterie active le mécanisme de réciprocité (la cible se sent valorisée et veut « mériter » le compliment en démontrant sa compétence) et l'ego (plaisir de la reconnaissance).

**Le partage réciproque.** Offrir une information (réelle ou fabriquée) pour créer une obligation de réciprocité. « Chez nous, on a eu un mal fou avec la certification DO-178C — et vous ? » L'éliciteur qui partage d'abord crée un précédent d'ouverture et une attente de réciprocité.

**Le silence stratégique.** Après avoir posé une question, ne pas combler le silence. La plupart des gens sont mal à l'aise avec le vide conversationnel et le comblent en développant — souvent au-delà de ce qu'ils avaient initialement prévu de partager. Le silence stratégique est l'un des outils les plus puissants et les plus sous-utilisés de l'élicitation.

**L'expression de l'ignorance.** « Je ne comprends pas du tout comment fonctionne votre système de badgeage — ça a l'air complexe. » L'ignorance affichée active le besoin d'expliquer et de démontrer sa compétence.

#### 14.3 La gestion de la conversation

L'élicitation réussie suit une progression contrôlée : création du rapport → conversation anodine → transition naturelle vers les sujets d'intérêt → extraction d'information → désengagement propre.

**Créer le rapport.** Le rapport (relation de confiance conversationnelle) se construit par le mirroring (reproduire subtilement la posture, le rythme de parole, le vocabulaire de la cible), l'écoute active (reformulation, signaux d'attention — hochements de tête, « je vois », « intéressant »), l'identification de points communs (parcours, intérêts, expériences partagées) et le respect du tempo de la cible (ne pas presser, laisser la conversation se développer naturellement).

**Orienter sans diriger.** L'éliciteur guide la conversation par des questions de relance (« et comment ça se passe concrètement ? »), des ponts thématiques (« en parlant de sécurité, d'ailleurs... ») et des manifestations d'intérêt sélectif (approfondir les sujets utiles, survoler les autres). La cible ne doit jamais avoir l'impression d'être interrogée.

**Escalader progressivement.** Commencer par des sujets anodins (l'entreprise en général, le secteur, l'actualité professionnelle), puis avancer vers des sujets plus spécifiques (le projet en cours, les outils utilisés, les défis techniques) et enfin vers les sujets sensibles (les failles de sécurité, les informations confidentielles, les projets non annoncés). Chaque palier valide que la cible est à l'aise avant de monter au suivant.

**Désengager proprement.** La fin de la conversation doit être naturelle et ne pas éveiller de soupçons. Prétexte de départ (« je dois aller à ma prochaine réunion »), remerciement chaleureux, échange de coordonnées (renforce la perception de normalité de l'échange). La cible doit quitter la conversation en se sentant bien — pas en se demandant pourquoi on lui a posé autant de questions.

#### 14.4 Les contextes d'élicitation

**Salon professionnel et conférence.** L'environnement idéal pour l'élicitation : la norme sociale est au networking, les barrières sont abaissées, les participants sont en mode « ouverture » et « échange ». Les pauses café, les cocktails et les dîners de gala sont les moments les plus propices. Le bar d'hôtel après une journée de conférence est le terrain de chasse classique de l'élicitation — fatigue, alcool et décompression réduisent la vigilance.

**Voyage professionnel.** Avion, train, salle d'attente d'aéroport — les voyages créent des opportunités de conversation prolongée avec une cible isolée de son contexte habituel. Les vols long-courriers offrent plusieurs heures de conversation potentielle.

**Événement d'entreprise.** Soirée de Noël, séminaire d'équipe, pot de départ — les événements internes mélangent registres professionnel et social, ce qui facilite l'élicitation (la conversation est à la fois professionnelle et personnelle, ce qui rend les questions sur le travail naturelles).

#### 14.5 L'élicitation par les services de renseignement étrangers : signaux et continuum

Les services de renseignement utilisent l'élicitation comme technique de base pour évaluer les cibles potentielles et collecter de l'information avant une éventuelle tentative de recrutement. Le processus suit un continuum identifiable : spotting (identification de la cible), assessment (évaluation de l'accès et de la vulnérabilité), developmental contact (établissement d'un lien), cultivation (renforcement progressif de la relation), elicitation ladder (montée en sensibilité des sujets abordés), et potentiellement tentative de recrutement.

Les signaux d'alerte incluent : un interlocuteur dont le profil ou l'entreprise est difficile à vérifier, des questions qui semblent anodines mais qui portent systématiquement sur des sujets sensibles (projets R&D, contrats, technologies), une transition rapide vers un canal de communication privé (WhatsApp, Signal), des propositions de « consulting » ou de « collaboration académique » rémunérées mais vagues, un intérêt disproportionné pour le réseau professionnel de la cible, et une relation qui progresse anormalement vite (invitation à dîner dès la première rencontre).

Les techniques de contre-élicitation sont détaillées au Ch.22. Les cas d'ingérence documentés par la DGSI sont un excellent support de formation.

---

### Chapitre 15 — Manipulation psychologique avancée : de la théorie à l'opérationnel

Ce chapitre est le pendant opérationnel du Ch.2. Là où le Ch.2 explique *pourquoi* les leviers psychologiques fonctionnent (cognition, biais, mécanismes), le présent chapitre explique *comment* le praticien les met en œuvre concrètement en situation.

#### 15.1 Le pied dans la porte et la porte au nez

**Le pied dans la porte.** Commencer par une petite demande à laquelle la cible accède facilement, puis escalader vers la demande réelle. La première compliance crée un engagement psychologique qui rend le refus de la demande suivante plus coûteux. En red team : « Est-ce que vous pouvez me montrer où sont les toilettes ? » (petite demande, accès au couloir) → « Au fait, vous savez où est la salle serveur ? Mon collègue m'attend là-bas pour l'intervention » (demande réelle).

**La porte au nez.** Commencer par une demande excessive que la cible refusera, puis proposer une demande modérée (la vraie demande) qui sera perçue comme un compromis raisonnable. « Je dois vérifier tous les postes de travail de l'étage — ça va prendre la journée. » Refus. « Bon, au minimum je dois vérifier le poste du responsable, ça prendra 5 minutes. » Acceptation. La concession de l'éliciteur crée une obligation de concession réciproque.

#### 15.2 La création de rapport rapide

Le rapport — cette connexion interpersonnelle qui crée un sentiment de confiance et de sympathie — peut être construit en quelques minutes avec des techniques documentées.

**Le mirroring.** Reproduire subtilement les gestes, la posture, le rythme de parole et le vocabulaire de l'interlocuteur. Le mirroring active les neurones miroirs et crée un sentiment de similarité inconscient. Il doit être subtil — un mirroring trop évident est perçu comme moquerie et détruit le rapport.

**Le pacing-leading.** S'aligner d'abord sur l'état émotionnel et le rythme de la cible (pacing), puis progressivement l'amener vers l'état souhaité (leading). Si la cible est stressée, commencer par un tempo rapide et une énergie élevée (pacing), puis ralentir progressivement (leading) pour créer un état de calme et d'ouverture.

**Les limites éthiques.** Le rapport est un outil, pas une fin en soi. Le red teamer ne crée pas de relation affective réelle — il simule une connexion pour atteindre un objectif opérationnel. La distinction est fondamentale : le rapport de red team est une technique temporaire et bornée. Un red teamer qui développe une relation personnelle authentique avec une cible franchit une ligne éthique.

#### 15.3 Le pretexting avancé et la résistance au questionnement

Un pretexte avancé n'est pas une simple identité fictive — c'est un personnage complet avec une histoire, des mannerisms, des réponses aux questions imprévues, et une cohérence interne suffisante pour résister à un interrogatoire léger.

La construction d'un pretexte robuste inclut : une identité complète (nom, entreprise, poste, ancienneté, parcours), une backstory cohérente (comment et pourquoi cette personne est là aujourd'hui), des détails sensoriels (vêtements, accessoires, matériel — cohérents avec le rôle), une préparation aux questions (« qui vous a envoyé ? », « quel est votre numéro de ticket ? », « comment s'appelle votre responsable ? »), et un plan de sortie si le pretexte est mis en doute.

La durée d'un pretexte varie de quelques minutes (interaction avec un gardien) à plusieurs semaines (opération d'élicitation prolongée, faux profil LinkedIn maintenu sur des mois). Plus la durée augmente, plus le risque de démasquage est élevé et plus la maintenance du pretexte consomme de ressources.

#### 15.4 Gestion de la résistance et de la confrontation

Quand la cible dit non, hésite ou exprime de la suspicion, le praticien dispose de plusieurs options.

**Le pivoting.** Changer d'angle d'approche sans changer de pretexte. Si la demande directe échoue, reformuler indirectement. « Je ne peux pas vous donner accès au réseau » → « Pas de problème, je comprends — je peux juste utiliser le WiFi visiteur pour envoyer un email à mon responsable ? » (le WiFi visiteur peut révéler des informations sur l'infrastructure réseau).

**Le recadrage.** Réinterpréter le refus dans un cadre favorable. « Non, je ne suis pas autorisé à donner cette information » → « Bien sûr, je comprends parfaitement — votre politique de sécurité est impressionnante. Justement, c'est ce que je veux documenter dans mon rapport d'audit. »

**L'abandon gracieux.** Quand la résistance est trop forte ou la suspicion trop élevée, se retirer proprement sans éveiller davantage de soupçons. « Pas de souci, je vais rappeler mon responsable pour clarifier. Merci de votre temps. » Un abandon gracieux préserve la possibilité d'une seconde tentative par un autre vecteur.

**La lecture des signaux de gêne.** Reconnaître quand la cible passe de la coopération à l'inconfort : changement de posture (bras croisés, recul), regard fuyant, réponses plus courtes, changement de sujet, vérification du badge. Ces signaux indiquent que la vigilance de la cible est activée et que l'escalade risque la confrontation.

#### 15.5 Les limites absolues du red team

Certaines techniques sont absolument proscrites en red team, même si un attaquant réel les utiliserait. L'exploitation de vulnérabilités personnelles (addiction, maladie, problèmes financiers, détresse émotionnelle), les menaces, le chantage, l'intimidation réelle, l'établissement d'une relation intime ou sentimentale avec une cible, et toute action susceptible de causer une détresse psychologique durable sont des lignes rouges non négociables. Un red teamer qui franchit ces lignes cause un préjudice réel à des individus réels — ce qui est contraire à l'objectif même du test, qui est d'améliorer la sécurité, pas de traumatiser des employés.

---

### Chapitre 16 — Capstone Partie III : test d'intrusion physique et élicitation

**Exercice intégrateur.** L'étudiant planifie un test d'intrusion physique complet sur un site industriel fictif (usine de production pharmaceutique, 400 employés, 1 site).

**Livrables attendus :**
1. Reconnaissance physique documentée (plan du site, accès identifiés, systèmes de contrôle d'accès, flux, horaires, comportements observés)
2. Construction de 2 pretextes d'intrusion physique (pretexte principal + pretexte de secours) avec justification
3. Liste du matériel nécessaire
4. Plan d'action (chronologie minute par minute, points de décision, objectifs intermédiaires)
5. Protocole d'urgence (safe word, contact de référence, procédure si confrontation)
6. Script d'élicitation : simulation d'une conversation d'élicitation en contexte salon professionnel (dialogue complet + analyse des techniques utilisées à chaque étape)
7. Grille d'évaluation de la sécurité physique observée (avec recommandations P0/P1/P2)

**Erreur fréquente** : négliger le protocole d'urgence. Un plan d'intrusion sans protocole d'extraction n'est pas un plan professionnel — c'est une improvisation dangereuse.


---

## PARTIE IV — L'ATTAQUANT : PERSPECTIVES OFFENSIVES

---

### Chapitre 17 — Le social engineering dans les APT

#### 17.1 Les techniques APT de social engineering

Les groupes APT (Advanced Persistent Threat) utilisent le social engineering comme vecteur d'accès initial avec un niveau de sophistication et de patience sans commune mesure avec la cybercriminalité opportuniste.

**Le spear-phishing sur mesure.** APT28 (Fancy Bear / GRU russe) est connu pour ses campagnes de spear-phishing ciblant les institutions gouvernementales, les organisations militaires et les médias, avec des leurres construits à partir d'une reconnaissance approfondie du contexte politique et institutionnel de la cible. APT35 (Charming Kitten / MOIS iranien) cible les chercheurs, les diplomates et les journalistes spécialisés Moyen-Orient avec des approches par email se faisant passer pour des pairs académiques ou des organisateurs de conférences.

**Les faux profils professionnels.** Le groupe Lazarus (DPRK / Corée du Nord) a industrialisé l'utilisation de faux profils LinkedIn dans son opération « Dream Job » : des recruteurs fictifs de grandes entreprises technologiques (Google, Meta, défense) contactent des développeurs et des ingénieurs pour leur proposer des opportunités d'emploi fictives. La conversation se déplace vers WhatsApp ou email, et le candidat reçoit un « test technique » ou un « document de description de poste » qui est en réalité un malware. Cette technique est redoutablement efficace parce qu'elle exploite un comportement professionnel normal (répondre à un recruteur) et que le pretexte (offre d'emploi attractive) est un puissant levier motivationnel.

**L'impersonation de journalistes et chercheurs.** APT35 se fait régulièrement passer pour des journalistes de médias crédibles (Wall Street Journal, CNN) ou des chercheurs d'universités prestigieuses pour approcher des cibles. L'approche initiale est une demande d'interview ou une invitation à contribuer à une publication — activités normales et flatteuses pour la cible. La conversation s'étend sur des jours ou des semaines avant l'envoi du payload.

#### 17.2 Le social engineering de longue durée

La patience est la signature des opérations APT de social engineering. Là où le cybercriminel opportuniste veut des résultats en heures, l'acteur APT investit des semaines ou des mois dans la construction d'une relation de confiance.

Le modèle APT35 est illustratif : le faux journaliste contacte sa cible, échange des emails polis sur plusieurs semaines, partage des articles intéressants (vrais articles, pas de malware — la phase de cultivation ne contient aucun élément malveillant), demande un premier entretien téléphonique (élicitation — collecte d'information sur les projets, les contacts, l'environnement de travail), puis finalement propose l'envoi d'un « document de travail » ou d'un « lien vers la plateforme d'interview » qui est le véritable vecteur d'attaque.

Cette approche contourne les défenses techniques (le premier email n'est pas malveillant, donc il passe les filtres) et psychologiques (la relation de confiance est établie avant la demande risquée). Elle est également très difficile à détecter par les équipes de sécurité : les emails sont légitimes dans leur contenu, la relation est construite progressivement, et la cible ne signale pas un échange professionnel qui lui semble normal.

#### 17.3 Le supply chain humain dans les APT

Le ciblage des prestataires et des partenaires est une technique APT en expansion. Plutôt que d'attaquer directement une cible hautement sécurisée (entreprise de défense, agence gouvernementale), l'attaquant cible un maillon faible de la chaîne humaine : le prestataire IT (qui a accès VPN aux systèmes de la cible), le fournisseur de services cloud (qui gère les environnements de production), le cabinet de conseil (qui a accès à des documents confidentiels), ou l'assistant personnel d'un dirigeant (qui a accès à l'agenda, aux emails, aux contacts).

Les cas de DPRK IT workers représentent une évolution radicale : des agents nord-coréens utilisent des identités fictives complètes (CV fabriqués, profils LinkedIn artificiels, photos deepfake) pour se faire embaucher comme développeurs freelances dans des entreprises technologiques occidentales. Une fois en poste, ils ont un accès légitime aux systèmes internes et au code source. Le rapport Unit 42 2025 documente la construction d'identités synthétiques multi-couches incluant faux CV et profils sociaux pour soutenir ces infiltrations.

#### 17.4 L'insider recruitment par les services de renseignement

Le recrutement d'insiders par les services de renseignement suit le cycle HUMINT décrit au Ch.3, mais appliqué au contexte industriel et technologique.

Les phases sont identifiables : repérage (identification d'individus ayant accès à l'information recherchée — souvent via LinkedIn), assessment (évaluation de la vulnérabilité — motivation financière, ego, frustration professionnelle), developmental contact (approche sous couvert de networking professionnel, proposition de consulting, invitation à un séminaire), cultivation (renforcement de la relation, petits avantages — invitation à dîner, cadeaux, rémunération pour des « consultations » anodines), escalade (demandes progressivement plus sensibles), et éventuellement recrutement formel ou maintien dans un état d'ignorance quant à la nature réelle de l'interlocuteur.

Les signaux d'alerte pour l'employeur incluent : un employé qui développe des contacts inhabituels avec des interlocuteurs étrangers non identifiés, des changements de comportement (accès à des documents hors de son périmètre, horaires de travail inhabituels, utilisation de dispositifs de stockage personnels), et des signes de vie au-dessus de ses moyens. Les dispositifs de détection et de signalement sont traités au Ch.22 et Ch.24.

#### 17.5 Cas documentés

**Lazarus « Dream Job » (2020-2025).** Ciblage systématique d'ingénieurs et développeurs dans les secteurs défense, aérospatial et crypto-monnaie via de faux recruteurs LinkedIn. Des centaines de victimes dans le monde. L'opération a évolué : en 2023-2025, les faux recruteurs utilisent des deepfakes vidéo en entretien d'embauche.

**DPRK IT Workers (2022-2025).** Des milliers de travailleurs nord-coréens opérant sous des identités fictives sont employés comme freelances dans des entreprises américaines et européennes. Revenu estimé : des centaines de millions de dollars reversés au régime nord-coréen.

**APT35 — Faux journalistes (2019-2025).** Campagnes récurrentes ciblant des chercheurs, diplomates et journalistes spécialisés. Pretextes d'interview et de collaboration académique. Durée de cultivation : 2 à 8 semaines avant l'envoi du payload.

---

### Chapitre 18 — L'ingénierie sociale dans la fraude et la criminalité organisée

#### 18.1 La fraude au président : modèle opérationnel

La fraude au président est une industrie criminelle structurée. Les groupes opèrent à partir de « call centers » organisés (principalement en Afrique de l'Ouest, Europe de l'Est, Asie du Sud-Est) avec une répartition des rôles : les « researchers » collectent l'OSINT sur les cibles, les « callers » exécutent les appels de vishing, les « email operators » gèrent les communications email, et les « money mules » blanchissent les fonds via des chaînes de comptes bancaires.

Le modèle opérationnel suit une séquence : reconnaissance OSINT (identification de la cible et du circuit de validation financière) → approche initiale (email et/ou appel) → manipulation (urgence, confidentialité, autorité) → exfiltration des fonds (virement vers un compte contrôlé) → blanchiment (transfert rapide vers d'autres comptes, conversion en crypto-monnaie). La chaîne complète peut se dérouler en quelques heures — la vitesse est critique pour devancer les mécanismes de rappel de virement.

#### 18.2 Les romance scams et le pig butchering

Les romance scams (arnaques sentimentales) ont évolué vers un modèle industriel appelé « pig butchering » (sha zhu pan) : la victime est « engraissée » (cultivée pendant des semaines ou des mois) avant d'être « abattue » (escroquée de sommes importantes, souvent en investissements crypto frauduleux).

Le modèle repose sur des « compound » en Asie du Sud-Est (Cambodge, Myanmar, Laos) où des victimes de traite humaine sont forcées d'opérer comme scammers. Les conversations sont gérées via des scripts et, de plus en plus, assistées par des chatbots IA qui maintiennent des conversations cohérentes sur la durée. Les pertes individuelles sont typiquement de 5 000 à 500 000 € et les pertes globales se chiffrent en milliards.

#### 18.3 Le SIM swapping

Le SIM swapping est une technique de social engineering ciblant les opérateurs télécom. L'attaquant contacte l'opérateur mobile de la victime (par téléphone ou en boutique) et, en utilisant des informations personnelles collectées par OSINT (nom, adresse, date de naissance, dernier montant facturé), convainc l'opérateur de transférer le numéro de téléphone vers une nouvelle carte SIM contrôlée par l'attaquant.

L'objectif est de prendre le contrôle du numéro de téléphone pour intercepter les codes MFA envoyés par SMS. Une fois le numéro transféré, l'attaquant peut reset les mots de passe de tous les comptes liés au numéro (email, banque, réseaux sociaux, crypto). Les pertes financières peuvent être considérables, en particulier dans le monde des crypto-monnaies.

**Défense** : ne pas utiliser le SMS comme second facteur pour les comptes critiques (préférer une app d'authentification ou une clé FIDO2), activer les protections anti-SIM swap de l'opérateur (code PIN, alerte sur les changements de SIM), utiliser un numéro de téléphone dédié et non public pour le MFA.

#### 18.4 L'évolution avec l'IA

L'IA transforme l'industrie du social engineering criminel de trois manières convergentes.

**La personnalisation à l'échelle.** Les LLM permettent de générer des emails de phishing personnalisés pour chaque cible à partir de données OSINT, dans n'importe quelle langue, avec une qualité linguistique native. Ce qui nécessitait auparavant un opérateur humain qualifié est maintenant automatisable.

**Le deepfake vocal et vidéo.** Le clonage vocal en temps réel permet des vishings d'un réalisme sans précédent. La vidéo deepfake en temps réel permet des visioconférences frauduleuses (cas de Hong Kong). Le coût de ces technologies diminue rapidement et leur accessibilité augmente.

**Les chatbots de social engineering.** Des agents conversationnels autonomes capables de maintenir des conversations d'élicitation ou de romance scam sur des jours ou des semaines, avec une cohérence et une adaptabilité que les scripts manuels ne permettaient pas. C'est le passage à l'échelle de l'ingénierie sociale relationnelle.

---

### Chapitre 19 — Red team social engineering : méthodologie professionnelle et OPSEC du praticien

#### 19.1 Le cadre du red team

Le red team social engineering est une prestation professionnelle encadrée par un contrat, une lettre de mission et des rules of engagement qui définissent précisément ce qui est autorisé et ce qui ne l'est pas.

**La lettre de mission** est le document fondateur. Elle doit être signée par un représentant habilité de l'organisation (pouvoir de signature vérifié juridiquement) et doit couvrir : l'identité du prestataire et des testeurs, le scope géographique (quels sites), le scope humain (quels employés — tous, un service, des profils spécifiques), le scope technique (quels vecteurs — phishing, vishing, intrusion physique, élicitation), la durée, les objectifs, les limites explicites, le protocole d'urgence (safe word, contact de référence), et la clause de confidentialité.

**Les rules of engagement** complètent la lettre de mission avec les détails opérationnels : horaires autorisés, zones interdites (zones classifiées, locaux syndicaux, infirmerie), techniques exclues, procédure de communication avec le commanditaire (reports intermédiaires, alertes), gestion des découvertes incidentes (si le red team découvre une intrusion réelle pendant le test — qui prévenir et comment).

#### 19.2 La planification

La planification couvre : les objectifs opérationnels (mesurables et réalistes), la reconnaissance (OSINT + reconnaissance physique), la construction des pretextes (chaque pretexte avec un pretexte de secours), l'infrastructure technique (domaines, landing pages, implants, communications sécurisées), la logistique (déplacements, tenues, matériel, hébergement si test multi-sites), la timeline (séquencement des phases — reconnaissance, phishing, vishing, intrusion physique, élicitation), et les points de décision (go/no-go à chaque phase).

#### 19.3 L'exécution

L'exécution d'un test de social engineering est une opération à haute tension. Le red teamer est lui-même sous pression (risque d'être intercepté, nécessité de maintenir le pretexte en temps réel, gestion du stress de l'imposture) et doit prendre des décisions en quelques secondes (pivoter si le pretexte ne fonctionne pas, abandonner si le risque est trop élevé, escalader si l'opportunité se présente).

**La documentation en temps réel** est critique : photos (discrètes), notes, horodatage de chaque action, enregistrements audio/vidéo si autorisés par la lettre de mission et la législation locale. Chaque élément de documentation sera utilisé dans le rapport pour démontrer les vulnérabilités identifiées et proposer des remédiations.

**L'adaptation en temps réel** est la compétence la plus difficile à acquérir. Les plans ne survivent pas au contact — un gardien plus vigilant que prévu, un employé qui pose une question inattendue, une porte fermée qui devait être ouverte. Le red teamer doit improviser tout en maintenant la cohérence de son pretexte.

#### 19.4 Le rapport

Le rapport de red team social engineering est le livrable final et le document qui justifie l'investissement du commanditaire. Il doit être factuel, constructif et actionnable.

**Structure type** : résumé exécutif (une page — résultats clés, risques majeurs, recommandations prioritaires), méthodologie (vecteurs utilisés, timeline, outils), résultats par vecteur (phishing : taux de clic, taux de compromission, temps de signalement ; vishing : taux de succès, informations obtenues ; intrusion physique : accès obtenus, temps de présence non détecté, implants posés), évaluation de l'impact (ce qu'un attaquant réel aurait pu faire avec les accès obtenus — sans les contraintes éthiques du red team), recommandations classées P0/P1/P2.

**Le ton** : le rapport documente des faits et propose des améliorations. Il ne blâme pas les individus, ne nomme pas les employés qui se sont fait piéger (sauf exception justifiée et avec l'accord du commanditaire), et ne ridiculise pas les défenses existantes. Un rapport humiliant ne produit pas de changement — il produit de la résistance.

#### 19.5 L'éthique du red teamer

Le red teamer a un pouvoir de manipulation — et la responsabilité qui va avec est non négociable. Le debriefing post-test est une obligation éthique : les employés qui ont été piégés doivent être informés (individuellement ou collectivement, selon le format choisi avec le commanditaire), le mécanisme exploité doit être expliqué (pas le nom de l'employé, mais la technique), et la finalité doit être claire (améliorer les défenses, pas sanctionner les individus).

La confidentialité des résultats individuels est un impératif. Le rapport ne doit pas permettre au commanditaire d'identifier et de sanctionner un employé spécifique sur la base de sa vulnérabilité au social engineering — sauf si cette vulnérabilité révèle un manquement grave et délibéré aux procédures (ce qui est différent d'un échec face à un social engineering sophistiqué).

#### 19.6 OPSEC du praticien

L'OPSEC (Operational Security) du praticien est un aspect souvent négligé de la formation au red team social engineering. Le praticien doit protéger sa propre sécurité, sa couverture opérationnelle et la traçabilité de sa mission.

**Préparation de la légende.** Chaque pretexte nécessite une identité crédible et compartimentée. Le red teamer ne doit jamais utiliser sa vraie identité pendant un test (sauf en phase de rapport). Les éléments de la légende (nom, entreprise, carte de visite, numéro de téléphone dédié, adresse email de pretexte, profils en ligne si nécessaire) doivent être préparés et testés avant le début de l'opération.

**La compartimentation.** Les identités de pretexte ne doivent pas être croisables entre elles ni traçables vers l'identité réelle du red teamer. Téléphones dédiés (burner ou SIM dédiée), adresses email distinctes, profils en ligne séparés, véhicule sans lien avec l'entreprise de red team.

**La gestion des supports.** Les photos, enregistrements, notes de terrain et copies de documents collectés pendant le test doivent être stockés de manière sécurisée (chiffrement), transmis au commanditaire via un canal sécurisé, et détruits après la livraison du rapport final (sauf obligation de conservation contractuelle). La perte d'un dispositif contenant des preuves de test peut constituer une fuite de données sensibles.

**La gestion de la confrontation.** Si le red teamer est intercepté, arrêté ou confronté par la sécurité ou les forces de l'ordre, il doit pouvoir s'identifier immédiatement comme testeur autorisé. La lettre de mission et le contact du commanditaire doivent être accessibles en permanence (version papier dans une poche intérieure, version numérique sur le téléphone). Le safe word doit être connu de toute l'équipe et du contact de référence.

**Les limites légales.** Le red teamer doit connaître le cadre juridique local. En France, même avec une lettre de mission signée par le DG, certaines actions restent juridiquement risquées si elles sont mal encadrées : l'enregistrement de conversations sans consentement est illégal (sauf dans le cadre strictement défini de la lettre de mission qui vaut consentement de l'employeur), la fabrication de faux documents peut constituer une infraction si elle est utilisée en dehors du cadre du test, l'usurpation de l'identité d'un vrai prestataire (et non d'un prestataire fictif) peut entraîner des complications juridiques. Le cadre juridique est détaillé à l'Annexe F.

---

### Chapitre 20 — Capstone Partie IV : planification d'un red team SE complet

**Exercice intégrateur.** L'étudiant produit un plan de mission red team social engineering complet pour un scénario donné (groupe pharmaceutique, 3 sites, 800 employés, programme de R&D sensible, contexte de fusion-acquisition récente).

**Livrables attendus :**
1. Analyse du scope et des contraintes (lettre de mission rédigée, rules of engagement, limites éthiques explicites)
2. Plan de reconnaissance (OSINT + physique, sources, méthodologie, timeline)
3. Matrice des pretextes (par vecteur : phishing, vishing, intrusion physique, élicitation — pretexte principal et pretexte de secours pour chaque)
4. Timeline d'exécution (6 semaines, séquencement des phases)
5. Liste du matériel et de l'infrastructure
6. Plan OPSEC (légendes, compartimentation, gestion des preuves)
7. Protocole d'urgence (safe word, contacts, procédure de désescalade)
8. Modèle de rapport (structure, métriques, format de recommandations)

**Erreur fréquente** : produire un plan techniquement solide mais éthiquement fragile (limites floues, absence de protocole d'urgence, oubli de la gestion des résultats individuels).

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 5**
>
> **L'incident réel.** En parallèle du red team, Lucie Ferraro alerte Nathan. Un ingénieur R&D senior du bureau parisien, Alexandre Petit, 45 ans, spécialiste des systèmes de navigation inertielle, a été contacté il y a trois mois sur LinkedIn par un certain « David Chen », se présentant comme recruteur chez « Meridian Consulting Asia ». Les échanges ont débuté par des compliments sur les publications d'Alexandre et une proposition de « consulting rémunéré » pour un client asiatique du secteur aéronautique.
>
> La conversation s'est déplacée vers WhatsApp. David Chen est passé progressivement de questions générales sur le secteur à des questions de plus en plus spécifiques : « Quelles sont les principales innovations en navigation inertielle actuellement ? », « Votre entreprise travaille sur des systèmes MEMS ou fibre optique ? », « Quels sont les principaux défis techniques du programme européen ? ». Alexandre a d'abord répondu avec enthousiasme (flatterie, intérêt professionnel, perspective de rémunération), puis a commencé à avoir des doutes quand David Chen a proposé un « rendez-vous confidentiel » lors d'un salon à Singapour.
>
> Nathan analyse les échanges et reconnaît un schéma d'élicitation classique : spotting (LinkedIn), assessment (publications, poste clé), developmental contact (connexion LinkedIn, flattery), cultivation (échanges WhatsApp, proposition de consulting), et escalade (questions de plus en plus spécifiques, proposition de rendez-vous physique). La progression suit le continuum HUMINT décrit au Ch.3. Le profil LinkedIn de David Chen présente des incohérences : photo qui ne retourne aucun résultat sur les recherches d'image inversée (probablement générée par IA), entreprise « Meridian Consulting Asia » sans présence web vérifiable, parcours professionnel vague.
>
> Nathan recommande d'alerter la DGSI (ingérence économique potentielle) et de débriefer Alexandre sans le blâmer — il est un insider involontaire, pas un traître. L'ingénieur est débriefé par la RSSI et Nathan : explication du mécanisme d'élicitation, rappel des signaux d'alerte, aucune sanction. La DGSI est informée et ouvre une enquête.

---

## PARTIE V — DÉFENSE ET CONTRE-INGÉNIERIE SOCIALE

---

### Chapitre 21 — Sensibilisation : au-delà du e-learning annuel

#### 21.1 Pourquoi la sensibilisation classique ne fonctionne pas

Les formations de sensibilisation e-learning annuelles — un module en ligne de 30 minutes suivi d'un quiz à choix multiples — ont un impact démontrablement limité sur le comportement réel des employés. Les études montrent que le taux de clic sur les campagnes de phishing diminue faiblement (5-10 %) après une formation e-learning et que cet effet s'estompe en quelques semaines.

Les raisons de cet échec sont identifiées. Le biais d'optimisme (« je sais maintenant, donc je ne me ferai pas piéger ») est renforcé par la réussite au quiz — l'employé a la preuve qu'il « connaît le phishing ». Le transfert d'apprentissage est faible : reconnaître un phishing dans un contexte d'examen (où on s'attend à un phishing) est radicalement différent de reconnaître un phishing dans le flux quotidien de 200 emails alors qu'on est pressé par un deadline. Et la formation traite le phishing comme un problème de connaissance (« si vous savez, vous ne cliquerez pas ») alors que c'est un problème de comportement en situation de charge cognitive (« même en sachant, vous cliquerez si les conditions sont réunies »).

#### 21.2 Les formations qui fonctionnent

**Les simulations réalistes.** Les campagnes de phishing simulé (envoyées sans avertissement préalable, avec des leurres crédibles personnalisés) sont significativement plus efficaces que les formations théoriques. Le retour individualisé après le clic (« vous avez cliqué parce que l'email exploitait le mécanisme X — voici comment le détecter ») est l'élément pédagogique clé. Important : le retour doit être explicatif et bienveillant, jamais punitif.

**Les exercices de vishing.** Les simulations d'appels téléphoniques de social engineering (par le red team interne ou un prestataire) testent la résistance des employés au pretexting vocal — une compétence que les formations e-learning ne développent pas du tout.

**Les micro-formations ciblées.** Sessions courtes (15-20 min) sur un sujet spécifique, adaptées au profil de risque : BEC pour les DAF et la comptabilité, pretexting helpdesk pour l'IT support, tailgating pour la réception et la sécurité, élicitation pour les ingénieurs R&D et les dirigeants. La pertinence thématique augmente l'engagement et le transfert.

**Les exercices tabletop.** Scénarios d'incident de social engineering discutés en groupe (comité de direction, équipe de sécurité, service concerné) : « un employé reçoit cet appel — que fait-il ? que fait son manager ? que fait le SOC ? ». Les exercices tabletop développent les réflexes collectifs et identifient les failles de processus.

#### 21.3 La formation par profil de risque

Tout le monde n'a pas besoin de la même formation. Les profils à risque doivent recevoir une formation spécifique adaptée aux menaces qui les ciblent.

| Profil | Menace principale | Formation prioritaire |
|---|---|---|
| DAF / Comptabilité | BEC, fraude au fournisseur | Processus de vérification, callback, double validation |
| Assistants de direction | Fraude au président, impersonation du dirigeant | Vérification des demandes urgentes, procédure de validation |
| Helpdesk / IT Support | Pretexting, reset de credentials, MFA manipulation | Procédures de vérification d'identité renforcées |
| Ingénieurs R&D | Élicitation, faux recruteurs, ingérence étrangère | Contre-élicitation, signaux d'alerte HUMINT, protection en conférence |
| Réception / Sécurité | Tailgating, impersonation, intrusion physique | Procédures de vérification des visiteurs, refus poli |
| Dirigeants | Ciblage personnel, deepfake, spear-phishing VIP | Surface d'exposition personnelle, sécurité des communications |

#### 21.4 Mesurer l'efficacité

Les métriques classiques (taux de clic sur le phishing simulé) sont nécessaires mais insuffisantes. Un programme de mesure complet inclut : le taux de clic (en baisse au fil des campagnes ?), le taux de signalement (en hausse ? — plus important que le taux de clic, car il mesure la culture de sécurité), le temps de signalement (les employés signalent-ils dans les minutes ou les heures ?), le taux de récidive (les employés qui ont cliqué une fois cliquent-ils encore ?), et les résultats qualitatifs des exercices de vishing et d'intrusion physique.

**Limite importante** : les métriques de phishing ne mesurent pas la résistance au vishing, à l'élicitation ou à l'intrusion physique. Un employé qui ne clique jamais sur les phishings simulés peut se faire piéger par un appel téléphonique convaincant ou une élicitation de face-à-face. La mesure doit être multi-vecteurs.

#### 21.5 La culture de sécurité

La culture de sécurité est l'objectif final — au-delà de la formation et des processus, c'est l'environnement humain qui détermine la résilience d'une organisation face au social engineering.

Une culture de sécurité efficace se caractérise par : le signalement encouragé (signaler un email, un appel ou un comportement suspect est perçu comme un acte positif, jamais comme une perte de temps ou une preuve de paranoïa), la vérification normalisée (vérifier l'identité d'un interlocuteur, même s'il se présente comme un supérieur hiérarchique, est un acte professionnel, pas un acte de défiance), la transparence (les résultats des tests de social engineering sont partagés avec les employés — sans nommer les individus — pour démontrer la réalité de la menace), et le renforcement positif (les employés qui signalent sont remerciés publiquement, pas les employés qui « ne se font jamais piéger » — car ceux qui ne signalent jamais ne sont pas nécessairement plus vigilants, ils sont peut-être simplement moins exposés).

---

### Chapitre 22 — Contre-élicitation et protection des informations

#### 22.1 Reconnaître une tentative d'élicitation

La détection d'une élicitation en cours est difficile précisément parce que l'élicitation est conçue pour ressembler à une conversation normale. Les signaux d'alerte sont subtils et contextuels.

**Questions inhabituellement spécifiques.** Une conversation de salon professionnel qui passe de « dans quel secteur travaillez-vous ? » à « quels algorithmes utilisez-vous pour la compensation inertielle ? » en quelques minutes présente une escalade de spécificité anormale.

**Flatterie excessive.** « Vous êtes vraiment la personne la plus compétente que j'ai rencontrée sur ce sujet » — en provenance d'un inconnu rencontré il y a 10 minutes — doit activer un signal d'alerte.

**Réciprocité forcée.** L'interlocuteur partage ostensiblement des informations (réelles ou fabriquées) sur son propre travail et attend visiblement un échange réciproque.

**Demande de confidentialité.** « Je préférerais qu'on continue cette discussion en dehors du cadre officiel » ou « pourrait-on en discuter par WhatsApp plutôt que par email professionnel ? » — la transition vers un canal non contrôlé est un signal fort.

**Intérêt disproportionné pour le réseau.** « Est-ce que vous connaissez le responsable du programme X ? » ou « pourriez-vous me mettre en contact avec votre collègue qui travaille sur Y ? » — l'utilisation de la cible comme vecteur vers d'autres cibles.

#### 22.2 Les techniques de contre-élicitation

**Le pont.** Répondre à une question par une question. « Et vous, dans quel domaine travaillez-vous exactement ? » Le pont renverse la dynamique de l'élicitation et permet d'évaluer l'interlocuteur.

**La déviation.** Changer de sujet naturellement. « C'est intéressant. Au fait, vous avez vu la keynote de ce matin ? » La déviation n'éveille pas de soupçon si elle est exécutée avec fluidité.

**La réponse vague.** Donner l'impression de répondre sans rien dire d'exploitable. « On travaille sur des sujets similaires à ce qui se fait dans le secteur, avec les contraintes que vous pouvez imaginer. » La cible a l'impression d'avoir répondu, l'éliciteur n'a rien obtenu de spécifique.

**Le signalement discret.** Si l'interlocuteur est identifié comme une menace potentielle (signaux forts d'élicitation, profil incohérent, insistance), le signalement doit être fait au retour : briefing au RSSI ou au responsable sécurité, avec autant de détails que possible (nom, entreprise, carte de visite, sujets abordés, questions posées).

#### 22.3 Protection en salon et en conférence

La protection des informations en contexte de salon professionnel repose sur un dispositif en trois temps : brief avant départ (quelles informations sont communicables, quelles informations sont interdites, quels sont les pays et les interlocuteurs à risque), comportement sur place (messages autorisés, gestion des sollicitations, utilisation des dispositifs numériques), et debriefing au retour (avec qui avez-vous échangé ? quelles questions vous ont été posées ? avez-vous observé quelque chose d'inhabituel ?). Ce dispositif est détaillé dans le cours Intelligence Économique (Ch.8) — il est repris ici dans sa dimension spécifique à la contre-ingénierie sociale.

#### 22.4 Protection en voyage professionnel

Certains pays présentent des risques d'ingérence particulièrement élevés. Sans nommer de pays spécifiques (les listes évoluent et sont publiées par les services compétents — DGSI, ANSSI, services homologues), les risques incluent : la surveillance des communications (chambres d'hôtel, réseaux WiFi), les approches physiques (contacts « spontanés » dans les hôtels, les bars, les événements), et le ciblage des dispositifs numériques (inspection aux frontières, clonage de téléphone). Les règles de protection incluent : ne jamais laisser de dispositifs sans surveillance, utiliser un téléphone dédié (sans données sensibles), chiffrer les communications, ne pas discuter de sujets sensibles en public, et signaler toute approche suspecte au retour.

#### 22.5 Protection des VIP et des cibles à haute valeur

Les dirigeants, les responsables R&D, les cadres travaillant sur des programmes sensibles, et les personnels ayant des habilitations de sécurité nécessitent un dispositif de protection adapté sans être transformés en paranoïaques. Le dispositif inclut : une évaluation de la surface d'exposition personnelle (OSINT sur eux-mêmes — que trouverait un attaquant ?), des recommandations de sécurité des réseaux sociaux (paramètres de confidentialité, gestion du contenu professionnel et personnel), un protocole de communication sécurisé pour les sujets sensibles, et une sensibilisation spécifique aux techniques d'élicitation et de ciblage qui visent leur profil.

---

### Chapitre 23 — Défense technique contre le social engineering

#### 23.1 Défense email

**DMARC en mode « reject ».** La configuration DMARC p=reject empêche l'usurpation directe du domaine de l'entreprise (un attaquant ne peut pas envoyer un email qui semble venir de @helios-aero.fr depuis un serveur non autorisé). C'est une mesure P0 — mais elle ne protège pas contre le typosquatting, les domaines lookalike ou la compromission d'email légitime.

**Bannières « email externe ».** L'ajout d'une bannière visible sur tous les emails provenant de l'extérieur de l'organisation (« ATTENTION : cet email provient d'un expéditeur externe ») est une mesure simple mais efficace qui réduit significativement le taux de réussite des phishings par display name spoofing.

**Passerelles anti-phishing.** Les solutions de sécurité email modernes (Proofpoint, Mimecast, Microsoft Defender for Office 365) analysent les URLs, les pièces jointes (sandboxing), le comportement de l'expéditeur et le contenu pour détecter les phishings. Leur efficacité est réelle mais non absolue — les emails de BEC (texte seul, pas de lien ni de pièce jointe) passent souvent les filtres.

**Simulation de phishing continue.** Les campagnes de phishing simulé régulières (mensuelles ou bimestrielles) avec retour individualisé constituent une couche de défense active qui maintient la vigilance.

#### 23.2 Défense téléphonique

**Callback verification.** Pour toute demande sensible reçue par téléphone, rappeler l'interlocuteur sur un numéro de référence connu (annuaire interne, site web officiel) — jamais sur le numéro affiché (qui peut être spoofé) ni sur un numéro fourni par l'appelant.

**Procédures de helpdesk renforcées.** Les demandes de reset de credentials par téléphone doivent être soumises à une vérification d'identité robuste : callback sur le numéro enregistré, validation par le manager, code de vérification préétabli, ou vérification en personne pour les comptes à privilèges.

**STIR/SHAKEN.** Le protocole d'authentification de l'identité de l'appelant est en cours de déploiement mais reste incomplet en 2025. Il réduit le spoofing sur les réseaux conformes mais ne l'élimine pas.

#### 23.3 Défense d'accès physique

**Contrôle d'accès multi-couches.** Badge seul pour les zones communes, badge + code pour les zones intermédiaires, badge + biométrie pour les zones sensibles (salle serveur, R&D, direction). La biométrie (empreintes, reconnaissance faciale) est résistante au clonage mais pose des questions RGPD (les données biométriques sont des données sensibles au sens du RGPD — leur traitement nécessite une base légale spécifique).

**Anti-tailgating.** Tourniquets unitaires, sas à passage unique, portiques à détection de double passage. Ces dispositifs sont efficaces mais nécessitent un investissement significatif et modifient les flux de circulation (impact sur l'ergonomie et l'acceptabilité par les employés).

**Politique visiteurs.** Accompagnement systématique des visiteurs par un employé de l'arrivée au départ, badge visiteur visuellement distinct (couleur, format), registre des visites, récupération du badge en fin de visite.

#### 23.4 Gestion des identités et des accès

**MFA résistant au phishing.** Le déploiement de FIDO2/WebAuthn (clés de sécurité physiques ou passkeys) élimine les risques de phishing en temps réel (Evilginx) parce que l'authentification est liée au domaine — la clé ne s'active que sur le domaine légitime. C'est la mesure technique la plus efficace contre le credential harvesting par phishing. En 2025, le déploiement de FIDO2 est en forte accélération mais reste minoritaire dans les entreprises.

**Principe du moindre privilège.** Chaque utilisateur ne dispose que des accès nécessaires à ses fonctions. Cela limite l'impact d'une compromission : un identifiant d'employé standard compromis par phishing donne accès aux ressources de l'employé, pas aux ressources de l'ensemble de l'organisation.

**Surveillance des accès anormaux.** UEBA (User and Entity Behavior Analytics) et ITDR (Identity Threat Detection and Response) détectent les comportements anormaux après compromission : connexion depuis une géolocalisation inhabituelle, accès à des ressources hors du périmètre habituel, escalade de privilèges.

#### 23.5 Les processus métier

**Validation multi-niveaux pour les virements.** Tout virement supérieur à un seuil défini nécessite la validation de deux personnes distinctes, dont au moins une vérification par callback. Les changements de coordonnées bancaires sont soumis à la même procédure.

**Séparation des tâches.** La personne qui initie un virement ne peut pas être la même personne qui le valide. La séparation des tâches élimine le scénario du BEC où un seul employé suffit pour déclencher un virement frauduleux.

---

### Chapitre 24 — Réponse à un incident de social engineering

#### 24.1 Détection

La détection d'un incident de social engineering repose sur trois sources : le signalement par l'employé (scénario optimal — c'est pourquoi la culture de signalement est la première défense), la détection technique (connexion anormale, alertes EDR, détection de credentials compromis, analyse de sessions) et la notification externe (un partenaire alerte, un service de renseignement notifie, un chercheur en sécurité signale).

Le temps de détection est critique, en particulier pour le BEC (un virement frauduleux peut être irrécupérable en quelques heures) et pour les intrusions utilisant des credentials compromis (l'attaquant latéralise et exfiltre rapidement).

#### 24.2 Qualification

La qualification de l'incident détermine la réponse. Les scénarios principaux sont : phishing réussi simple (credentials compromis — impact limité si le compte n'a pas de privilèges élevés), BEC en cours (virement initié — nécessite une action bancaire urgente pour bloquer le transfert), intrusion physique (implant posé — nécessite une recherche physique et réseau), élicitation de renseignement (fuite d'information — difficile à quantifier, nécessite une évaluation de l'impact).

#### 24.3 Containment

Le containment dépend du type d'incident : reset des credentials compromis (tous les comptes affectés), révocation des sessions actives, blocage des accès à risque, recherche de persistence (l'attaquant a-t-il installé des backdoors ou créé des comptes additionnels ?), isolement du segment réseau si un implant physique est suspecté, et pour le BEC, gel du virement via la banque (la rapidité est déterminante — les fonds transférés à l'étranger sont souvent irrécupérables après 24-48h).

#### 24.4 Investigation

L'investigation d'un incident de social engineering combine forensique technique et analyse humaine. Forensique email (headers complets, analyse de la landing page, identification de l'infrastructure de phishing), identification de l'acteur (phishing de masse vs spear-phishing ciblé vs APT — la sophistication et la personnalisation sont des indicateurs), évaluation de l'impact (quels accès ont été compromis, quelles données ont potentiellement été exfiltrées, quelle est la persistance de l'attaquant), et analyse de la chaîne de compromission (comment l'attaquant est passé de l'accès initial à ses objectifs finaux).

#### 24.5 Retex et amélioration

Le retex (retour d'expérience) post-incident est une obligation, pas une option. Il doit suivre le modèle « no blame post-mortem » : l'objectif est d'identifier les défenses qui ont échoué et de les améliorer, pas de blâmer l'employé qui a cliqué.

Le retex couvre : la chronologie de l'incident (de la première action de l'attaquant à la détection et au containment), les défenses qui ont fonctionné (qu'est-ce qui a alerté ou ralenti l'attaquant ?), les défenses qui ont échoué (pourquoi le phishing n'a pas été filtré ? pourquoi le helpdesk a procédé au reset sans vérification suffisante ?), les recommandations d'amélioration (classées P0/P1/P2), et le plan d'action avec responsable et échéance pour chaque recommandation.

---

### Chapitre 25 — Capstone Partie V : incident de social engineering — de la détection au retex

**Scénario.** Un employé du service comptabilité signale un appel téléphonique suspect au SOC : un interlocuteur se présentant comme le prestataire comptable a demandé l'envoi d'un fichier de paie « pour vérification ». L'employé a d'abord envoyé le fichier, puis a eu un doute et a signalé.

**Livrables attendus :**
1. Fiche de qualification de l'incident (type, gravité, impact potentiel)
2. Plan de containment immédiat
3. Protocole d'investigation (forensique email, analyse de l'appel, évaluation de l'impact)
4. Rapport d'incident (chronologie, analyse, impact, recommandations P0/P1/P2)
5. Plan de retex (format no-blame, actions correctives, responsables, échéances)

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 6**
>
> **Convergence.** L'enquête sur « David Chen » confirme le diagnostic de Nathan. La vérification du profil LinkedIn révèle : photo générée par IA (confirmé par analyse des artefacts — pas de résultat en recherche d'image inversée, symétrie anormale des oreilles), entreprise « Meridian Consulting Asia » sans enregistrement commercial vérifiable dans les registres consultés, numéro WhatsApp enregistré dans un pays tiers, et parcours professionnel avec des incohérences (dates, entreprises non vérifiables).
>
> L'analyse des échanges WhatsApp montre un schéma d'élicitation structuré : 3 premières semaines de conversation générale (flattery, intérêt professionnel, réciprocité), semaine 4-6 escalade vers des questions techniques spécifiques, semaine 7-8 proposition de consulting rémunéré et de rencontre physique. Alexandre Petit a divulgué, sans s'en rendre compte, des informations sur les orientations technologiques de son programme, les noms de ses collègues et les partenaires du consortium.
>
> La DGSI est alertée et prend le relais de l'investigation (ingérence économique étrangère). Alexandre est débriefé sans sanction — il est informé des mécanismes exploités et reçoit une formation de contre-élicitation. Nathan intègre ce cas réel dans son rapport de red team comme illustration de la menace de niveau étatique qui pèse sur Helios.


---

## PARTIE VI — DIMENSIONS AVANCÉES

---

### Chapitre 26 — Social engineering et IA : la révolution en cours

#### 26.1 Le phishing AI-powered

Les LLM (Large Language Models) transforment le phishing de deux manières fondamentales. Premièrement, la personnalisation à l'échelle : un LLM peut générer des centaines d'emails de spear-phishing, chacun personnalisé à partir du profil OSINT de la cible (poste, entreprise, intérêts, publications récentes), dans n'importe quelle langue, avec une qualité linguistique indistinguable d'un email humain. La barrière d'entrée qui protégeait les cibles francophones (les phishings en mauvais français étaient faciles à détecter) a disparu. Deuxièmement, l'adaptation culturelle : le LLM adapte le registre, le ton et les conventions de communication au contexte culturel de la cible — un email de phishing destiné à un cadre allemand ne ressemblera pas à celui destiné à un ingénieur japonais.

Le rapport Unit 42 2025 confirme cette tendance : dans plusieurs investigations, les acteurs de la menace ont utilisé l'IA générative pour créer des leurres hautement personnalisés à partir d'informations publiques, avec un niveau de ton et de timing qui nécessitait auparavant un opérateur humain qualifié.

**Implications pour la défense** : les marqueurs linguistiques de phishing (fautes, registre inapproprié, formulations inhabituelles) ne sont plus des indicateurs fiables. La défense doit se reporter sur les indicateurs structurels (domaine d'expéditeur, headers, comportement de l'email) et les processus de vérification (callback, double validation).

#### 26.2 Le vishing deepfake

Le clonage vocal en temps réel atteint en 2025 un niveau de maturité opérationnelle. Les plateformes comme ElevenLabs ou les modèles open source (XTTS, Bark) permettent de cloner une voix à partir d'échantillons audio courts (30 secondes à quelques minutes suffisent pour un clone de qualité acceptable). L'intégration en temps réel dans un appel téléphonique est techniquement possible avec une latence de quelques centaines de millisecondes — souvent indétectable sur un réseau téléphonique standard.

Les cas d'utilisation offensifs documentés incluent : fraude au président par deepfake vocal (l'attaquant clone la voix du DG à partir d'interviews publiques et appelle le DAF), confirmation téléphonique pour renforcer un BEC email (le « DG » rappelle pour confirmer son email de demande de virement), et vishing de helpdesk avec la voix d'un employé légitime.

**Détection** : les détecteurs de deepfake vocal sont en cours de développement mais restent peu fiables en conditions réelles (compression téléphonique, bruit ambiant, diversité des technologies de synthèse). La défense la plus efficace reste procédurale : pour toute demande sensible par téléphone, vérification out-of-band obligatoire (callback sur un autre canal, validation en personne, code de vérification préétabli).

#### 26.3 La vidéo deepfake en temps réel

La visioconférence deepfake en temps réel a franchi le seuil de l'opérationnel. Le cas de Hong Kong (début 2024) — 25 millions de dollars volés via une visioconférence où plusieurs participants étaient des deepfakes — est le cas le plus médiatisé, mais d'autres cas moins spectaculaires ont été rapportés par des cabinets de réponse à incident.

En 2025, la génération vidéo deepfake en temps réel est accessible via des plateformes commerciales et des outils open source. La qualité est variable mais suffisante pour une visioconférence de résolution standard, en particulier si l'attaquant simule une connexion internet de mauvaise qualité (réduction de la résolution et du framerate, ce qui masque les artefacts).

**Défense** : demander à l'interlocuteur un geste imprévu (tourner la tête, montrer ses mains, placer un objet devant le visage) peut révéler les artefacts des deepfakes actuels — mais cette parade deviendra obsolète à mesure que la technologie progresse. La vérification d'identité multi-facteur (question de sécurité, code préétabli, confirmation par un second canal) reste la défense la plus robuste.

#### 26.4 Les chatbots de social engineering

L'IA agentic appliquée au social engineering représente la prochaine frontière. Des agents conversationnels autonomes, capables de maintenir des conversations cohérentes sur des jours ou des semaines, de s'adapter au style de leur interlocuteur, de gérer les objections et de progresser méthodiquement vers un objectif (collecte d'identifiants, élicitation d'information, construction d'une relation de confiance), permettent le passage à l'échelle de techniques qui étaient auparavant limitées par la disponibilité d'opérateurs humains qualifiés.

Le rapport Unit 42 2025 identifie l'IA agentic comme une couche émergente dans le paysage des menaces, avec des systèmes capables d'exécuter de manière autonome des tâches en plusieurs étapes avec un minimum d'intervention humaine. Bien que l'adoption reste limitée à ce jour, les cas observés incluent la reconnaissance multi-plateforme automatisée et la distribution de messages coordonnée.

Les implications sont considérables pour les romance scams (un seul opérateur peut gérer des centaines de « relations » simultanées via des chatbots IA), pour l'élicitation (des agents conversationnels capables de mener des conversations d'élicitation structurées en salon professionnel virtuel), et pour le phishing conversationnel (des agents qui répondent aux questions de la cible et adaptent leur pretexte en temps réel).

#### 26.5 La course aux armements

La défense face à la menace IA s'organise autour de trois axes : la détection (analyse comportementale des communications, détection d'anomalies dans le style d'écriture, détecteurs de deepfake audio et vidéo — tous avec des taux de faux positifs significatifs en 2025), les processus (vérification out-of-band, double validation, codes de confirmation préétablis — les défenses procédurales sont agnostiques à la technologie utilisée par l'attaquant), et la sensibilisation (former les employés à la réalité de la menace deepfake et IA, sans verser dans l'alarmisme — l'objectif est la vigilance, pas la paranoïa).

L'enjeu stratégique est que l'IA avantage structurellement l'attaquant : l'attaquant n'a besoin de réussir qu'une fois, tandis que le défenseur doit réussir à chaque fois. L'IA permet à l'attaquant de multiplier les tentatives avec une qualité constante et un coût marginal décroissant. La seule réponse durable est de construire des processus qui fonctionnent même quand la manipulation est parfaite — c'est-à-dire des processus qui ne reposent pas sur la capacité d'un individu isolé à détecter une tromperie.

---

### Chapitre 27 — Sécurité physique avancée : au-delà du badge

#### 27.1 Les systèmes de contrôle d'accès en profondeur

**RFID basse fréquence (125 kHz).** Technologies HID ProxCard, EM4100 — largement déployées, facilement clonables. L'investissement minimal (Proxmark3 — environ 300 €, Flipper Zero — environ 200 €) permet le clonage en quelques secondes à une distance de quelques centimètres. Ces technologies ne devraient plus être utilisées pour le contrôle d'accès de zones sensibles, mais restent massivement déployées par inertie dans de nombreuses organisations.

**RFID haute fréquence (13.56 MHz).** MIFARE Classic (vulnérable — attaques connues sur le chiffrement Crypto-1), MIFARE DESFire EV2/EV3 (robuste — chiffrement AES 128 bits, authentification mutuelle), iCLASS Standard (vulnérable), iCLASS SE/SEOS (robuste). La migration vers DESFire EV2+ ou SEOS est la recommandation de référence pour les organisations à risque élevé.

**Badges mobiles (NFC/BLE).** Apple Wallet, Google Wallet, applications dédiées (HID Mobile Access, SALTO JustIN) — protégés par la cryptographie du smartphone (enclave sécurisée), résistants au clonage à distance. L'avantage opérationnel est considérable : révocation à distance (en cas de perte ou de départ), provisioning sans contact physique, audit détaillé des accès. Les inconvénients : dépendance au smartphone (batterie, panne), compatibilité variable entre les fabricants de téléphones et les systèmes de contrôle d'accès, et le fait que certains sites sensibles interdisent les smartphones.

**Biométrie.** Empreintes digitales, reconnaissance faciale, reconnaissance de l'iris — offrent un facteur d'authentification non transférable (en théorie). En pratique, les systèmes biométriques ont des taux de faux rejet (l'employé légitime est refusé — frustration et contournement) et de faux acceptation (un attaquant est accepté — plus rare mais possible avec des attaques de présentation). Les considérations RGPD sont significatives : les données biométriques sont des données sensibles qui nécessitent une base légale spécifique et une analyse d'impact.

#### 27.2 Le crochetage et le bypass physique

Dans le cadre d'un red team autorisé, les techniques de bypass physique complètent le social engineering quand l'accès par manipulation humaine échoue ou n'est pas applicable.

**Lock picking.** Le crochetage de serrures à goupilles standard est une compétence de base du red teamer physique. Les serrures à goupilles standard (cylindres européens de base) peuvent être crochetées en quelques minutes avec un jeu de crochets (tension wrench + pick). Les serrures haute sécurité (Abloy, Mul-T-Lock, Medeco) sont significativement plus résistantes et nécessitent des compétences et du matériel spécialisés.

**Bypass de serrures électriques.** Les serrures électriques à ventouse (maglocks) peuvent souvent être contournées en passant un objet fin (shim card) entre la porte et le cadre pour actionner le capteur de demande de sortie (REX — Request to Exit). Les serrures à gâche électrique sont vulnérables à des techniques similaires si elles sont en mode « fail-safe » (déverrouillées en cas de coupure de courant).

**Les faiblesses architecturales.** Faux plafonds (passage entre deux pièces par le plénum), gaines techniques (passage par les conduits de câblage ou de ventilation), fenêtres non verrouillées aux étages supérieurs, cloisons légères (certaines cloisons de bureau sont en plaque de plâtre et peuvent être traversées). Un audit de sécurité physique sérieux inclut l'évaluation de ces vecteurs.

#### 27.3 Les implants physiques

Les implants physiques sont des dispositifs matériels déployés par le red teamer pour maintenir un accès persistant après l'intrusion physique.

**Clé USB drop.** Rubber Ducky (émule un clavier et exécute des commandes en quelques secondes), Bash Bunny (multi-payload, émulation de périphériques multiples), O.MG Cable (câble USB avec implant intégré — visuellement indistinguable d'un câble normal). En contexte offensif, la clé USB est déposée dans un lieu où elle sera trouvée et branchée (parking, accueil, salle de réunion) — le baiting exploite la curiosité.

**Implant réseau.** LAN Turtle (implant réseau passif se branchant sur un port Ethernet — fournit un accès distant au réseau interne), rogue access point WiFi (Raspberry Pi ou device dédié émettant un réseau WiFi qui capture les connections ou fournit un accès au réseau filaire), keylogger hardware (se place entre le clavier et le port USB — capture toutes les frappes).

La documentation de chaque implant déployé (localisation, horodatage, durée de présence, données collectées) est une obligation du rapport de red team. Tous les implants doivent être retirés à la fin du test — un implant oublié constitue une vulnérabilité réelle.

#### 27.4 Conception d'un site résistant au social engineering physique

La sécurité physique contre le social engineering se conçoit dès l'architecture du site, pas comme un ajout après coup.

**Flux de circulation.** Les visiteurs et les prestataires doivent emprunter des circuits distincts des employés, avec accompagnement systématique. Les zones sensibles (R&D, salle serveur, direction) doivent être physiquement séparées des zones communes (accueil, réfectoire, salles de réunion visiteurs) avec un contrôle d'accès intermédiaire.

**Zone d'accueil comme sas de sécurité.** L'accueil ne doit pas être une simple réception — c'est un sas de sécurité qui vérifie l'identité, contacte l'hôte, émet le badge visiteur et assure l'accompagnement. Le gardien/réceptionniste doit être formé au contre-social engineering (détection des pretextes, refus poli, procédure d'escalade).

**Surveillance intégrée.** Caméras aux points d'accès et de circulation, avec monitoring en direct (pas seulement enregistrement). Détection d'anomalies (accès en horaires inhabituels, badge utilisé simultanément à deux endroits, tentatives d'accès répétées échouées).

---

### Chapitre 28 — Élicitation, investigation et contre-ingérence : usages encadrés et expertise

#### 28.1 L'élicitation comme outil d'investigation

Les techniques d'élicitation ne sont pas réservées aux attaquants et aux services de renseignement. Elles sont utilisées légalement dans de nombreux contextes professionnels.

**Les enquêteurs privés** utilisent l'élicitation dans le cadre d'investigations autorisées (fraude interne, compliance, due diligence). Le cadre juridique est strict : l'enquêteur ne peut pas usurper une identité officielle (force de l'ordre, administration), ne peut pas recourir à la contrainte, et doit respecter la vie privée. Les techniques d'élicitation conversationnelle (questions ouvertes, partage réciproque, silence stratégique) sont permises tant qu'elles ne constituent pas un stratagème déloyal au sens de la jurisprudence.

**Les journalistes d'investigation** utilisent des techniques proches de l'élicitation pour obtenir des informations de sources. Le droit français protège le secret des sources journalistiques, ce qui crée un cadre juridique spécifique.

**Les compliance officers** utilisent l'entretien structuré (distinct de l'élicitation — l'entretien est consenti et identifié) dans le cadre d'enquêtes internes sur des suspicions de fraude, de corruption ou de violation de conformité.

#### 28.2 Le pretexting dans les enquêtes : cadre légal

Le pretexting — l'utilisation d'un faux pretexte pour obtenir des informations — est juridiquement encadré de manière stricte.

En France, la fabrication et l'utilisation de faux documents sont des infractions pénales (art. 441-1 et suivants du Code pénal). L'usurpation d'identité est un délit (art. 226-4-1). L'enregistrement d'une conversation sans le consentement des participants est interdit (art. 226-1). Ces restrictions limitent significativement les techniques disponibles pour les enquêteurs privés et les compliance officers par rapport aux pratiques anglo-saxonnes (aux États-Unis, le pretexting est plus largement toléré dans certains contextes d'investigation).

Le red team autorisé par lettre de mission constitue une exception encadrée : le pretexting est autorisé dans le cadre et les limites définis par la lettre de mission, qui vaut consentement de l'employeur. Mais cette autorisation ne couvre que les interactions avec les employés de l'organisation mandataire, pas avec des tiers (prestataires, visiteurs, voisins).

#### 28.3 Investigation sur les arnaques de social engineering

L'investigation post-incident sur une arnaque de social engineering combine analyse technique et analyse relationnelle.

**Analyse technique.** Forensique email (headers, infrastructure de phishing — domaines, hébergement, certificats), analyse de la landing page (code source, exfiltration des données), traçage des flux financiers (pour le BEC — les fonds transitent typiquement par plusieurs comptes avant d'être convertis en crypto-monnaie ou retirés en liquide).

**Analyse OSINT.** Investigation sur les éléments identifiants de l'attaquant : numéros de téléphone (opérateur, géolocalisation), domaines (Whois, historique DNS, hébergement), profils en ligne (analyse de la fabrication des faux profils, recherche d'image inversée), et croisement avec les bases de données d'incidents connus.

**Coopération.** Avec les plateformes (signalement des faux profils, demande de désactivation), avec les banques (gel de fonds, traçage des virements), avec les forces de l'ordre (dépôt de plainte, transmission des éléments techniques), et avec les agences de renseignement si l'incident relève de l'ingérence étrangère (DGSI en France).

#### 28.4 L'entretien et l'interrogatoire

Les techniques d'entretien professionnel (modèle PEACE — Preparation and Planning, Engage and Explain, Account, Closure, Evaluate) et l'entretien cognitif sont des outils d'investigation légaux distincts de l'élicitation.

La différence fondamentale : l'entretien est consenti et identifié (la personne sait qu'elle est interrogée et accepte de répondre), l'élicitation est clandestine (la personne ne sait pas qu'elle est interrogée). Cette distinction a des implications juridiques et éthiques majeures.

Le modèle PEACE, développé au Royaume-Uni, privilégie la collecte d'un récit libre (laisser le sujet raconter sa version sans interruption), la recherche de précisions par des questions non suggestives, et l'identification des incohérences par recoupement — plutôt que la confrontation directe ou les techniques d'interrogatoire agressives (qui produisent des faux aveux et des informations peu fiables).

#### 28.5 Le témoignage de l'expert

L'expert en social engineering peut être amené à intervenir dans un cadre judiciaire : rapport d'expertise (analyse technique d'une arnaque, évaluation de la sophistication de l'attaque, évaluation de la responsabilité de la victime), expertise judiciaire (désigné par un tribunal pour éclairer une décision de justice), et contre-expertise (analyse critique d'un rapport d'expertise adverse).

L'expert doit être capable d'expliquer des concepts techniques complexes (phishing, deepfake, élicitation) à un public non technique (magistrats, jurés) de manière claire, rigoureuse et neutre. La crédibilité de l'expert repose sur ses qualifications, son expérience, la rigueur de sa méthodologie et sa capacité à distinguer fait établi, hypothèse probable et piste exploratoire.

---

## PARTIE VII — SYNTHÈSE ET CAS PRATIQUES

---

### Chapitre 29 — Cas de synthèse : opération de social engineering multi-vecteurs

**Scénario complet.** L'étudiant analyse une opération de social engineering reconstituée couvrant l'ensemble du spectre : reconnaissance OSINT → spear-phishing → vishing → intrusion physique → élicitation → exploitation → détection → investigation → remédiation.

**Contexte.** Un cabinet d'avocats d'affaires parisien (150 employés, données clients hautement confidentielles, associés voyageant fréquemment) est ciblé par un groupe criminel spécialisé dans le BEC. L'opération se déroule sur 4 semaines.

**Phase 1 — Reconnaissance.** Le groupe collecte les profils LinkedIn des associés et des assistants, identifie les dossiers en cours (via les communiqués de presse et les annonces de transactions), cartographie l'organigramme et les processus de communication interne.

**Phase 2 — Spear-phishing ciblé.** Un email de phishing se faisant passer pour le service IT du cabinet est envoyé à 8 assistants. 3 cliquent. Les identifiants de 2 assistants sont capturés.

**Phase 3 — Reply-chain BEC.** Les identifiants d'une assistante sont utilisés pour accéder à sa boîte mail. Le groupe lit les échanges récents avec un client sur une transaction immobilière de 2 millions d'euros. Un email est inséré dans le fil de conversation demandant un virement vers de nouvelles coordonnées bancaires, en invoquant un changement de domiciliation bancaire du notaire.

**Phase 4 — Vishing de confirmation.** Le groupe appelle l'assistante en se faisant passer pour le « cabinet du notaire » pour confirmer le changement d'IBAN et presser l'exécution du virement.

**Phase 5 — Détection et réponse.** Le virement est exécuté. 48h plus tard, le vrai notaire contacte le cabinet pour relancer le règlement. L'arnaque est découverte. Investigation, plainte, tentative de gel de fonds (partiellement réussie — 40 % des fonds récupérés).

**Analyse attendue.** L'étudiant identifie chaque technique utilisée, les leviers psychologiques exploités à chaque étape, les défenses qui auraient pu prévenir l'attaque (DMARC, bannière email externe, processus de vérification des changements d'IBAN, callback au notaire sur un numéro connu, formation des assistants au BEC), et rédige un rapport post-incident avec recommandations P0/P1/P2.

---

### Chapitre 30 — Le métier d'expert en social engineering

#### 30.1 Les métiers

Le social engineering professionnel couvre plusieurs métiers distincts.

**Red teamer SE / pentester spécialisé.** Exécution de tests d'intrusion social engineering (phishing, vishing, intrusion physique, élicitation) pour des organisations clientes. Travail en cabinet de conseil en cybersécurité ou en équipe interne de sécurité offensive.

**Consultant en sensibilisation.** Conception et délivrance de programmes de formation adaptés aux profils de risque. Développement de simulations réalistes (campagnes de phishing, exercices de vishing, tabletop exercises).

**Analyste en contre-ingénierie sociale.** Détection et analyse des tentatives de social engineering ciblant l'organisation. Veille sur les menaces, coordination avec les services de renseignement (DGSI pour l'ingérence étrangère), investigation sur les incidents.

**Formateur.** Enseignement des techniques de social engineering et de contre-ingénierie sociale dans un contexte académique ou professionnel.

**Enquêteur spécialisé.** Investigation post-incident, analyse forensique de campagnes de phishing, expertise judiciaire.

#### 30.2 Les compétences

Le profil du praticien en social engineering est par nature transversal : psychologie appliquée (compréhension des biais, des leviers d'influence, des dynamiques interpersonnelles), communication (aisance orale, capacité d'adaptation, gestion du stress en situation d'imposture), OSINT (maîtrise des techniques de reconnaissance en sources ouvertes), technique (compréhension des systèmes email, des protocoles d'authentification, des technologies de contrôle d'accès, des outils d'infrastructure), rédaction (capacité à produire des rapports clairs, factuels et actionnables), et éthique (discernement, intégrité, capacité à tracer et respecter des limites).

#### 30.3 Les certifications

Plusieurs certifications couvrent le social engineering, avec des niveaux de profondeur variables.

**SANS SEC567 — Social Engineering for Penetration Testers.** La formation de référence pour le red team social engineering (phishing, vishing, impersonation, pretexting). Coûteuse (formation SANS) mais reconnue.

**OSCP (Offensive Security Certified Professional).** L'OSCP couvre le pentesting global avec un volet social engineering limité — c'est une certification de pentesting technique plus que de social engineering.

**GPEN (GIAC Penetration Tester).** Couvre le pentesting incluant les aspects de social engineering dans une perspective globale.

**Certified Social Engineer (Social-Engineer.org).** Certification spécialisée en social engineering développée par Christopher Hadnagy. Pertinente mais moins largement reconnue que les certifications SANS/GIAC.

L'état du marché des certifications SE en 2025 est en évolution : la demande de compétences en social engineering augmente, mais les certifications spécialisées restent rares comparées aux certifications de pentesting technique. L'expérience pratique (campagnes réelles, rapports de red team, portfolio de missions) reste le critère de différenciation principal pour les recruteurs.

#### 30.4 L'éthique comme compétence fondamentale

Le praticien de social engineering possède un savoir-faire de manipulation interpersonnelle. Cette compétence confère un pouvoir — et la responsabilité qui l'accompagne est non négociable. L'éthique n'est pas une contrainte externe imposée au praticien : c'est une compétence interne qui guide chaque décision opérationnelle.

Les questions éthiques récurrentes incluent : jusqu'où aller dans la manipulation pendant un test autorisé ? Comment gérer la découverte de vulnérabilités personnelles d'un employé (addiction, problèmes financiers) pendant la reconnaissance ? Comment rédiger un rapport qui améliore les défenses sans humilier les individus ? Comment gérer la pression d'un commanditaire qui demande des résultats individuels nominatifs pour sanctionner des employés ?

La réponse à ces questions n'est pas dans un code de conduite abstrait — elle est dans le discernement professionnel du praticien, formé par l'expérience, la réflexion et le dialogue avec ses pairs.

#### 30.5 Perspectives de carrière

La demande de compétences en social engineering est en croissance structurelle. Les entreprises réalisent que la technologie seule ne suffit pas à protéger contre une menace qui exploite le facteur humain. Les réglementations (NIS2, DORA pour le secteur financier) renforcent les obligations de test de résilience, y compris les tests de social engineering. La menace IA (deepfakes, phishing personnalisé) renforce le besoin de praticiens capables de tester et de former.

Les trajectoires de carrière incluent : le consulting (missions de red team SE pour des clients variés), le poste en interne (responsable de la sensibilisation, responsable du red team interne, analyste en contre-ingérence), le management (direction d'un service de sécurité offensive, RSSI avec une spécialité en facteur humain), et la formation/recherche (enseignement, publication, conférences — DEF CON SE Village, Black Hat, les conférences SANS).

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode final**
>
> **Le rapport.** Après 6 semaines de test, Nathan livre son rapport à Marc Tessier (DG) et Lucie Ferraro (RSSI) lors d'une restitution de 2 heures en comité restreint.
>
> **Résultats :**
> - **Phishing** : taux de clic 28,3 % (34/120), 18 identifiants collectés dont 2 comptes admin
> - **Vishing** : 4 tentatives d'appel au helpdesk pour reset de credentials — 2 réussies (50 %), dont 1 reset MFA sur un compte à privilèges
> - **Intrusion physique** : réussie sur 2 sites sur 3 (Bordeaux et Paris — échec à Toulouse où le gardien a refusé l'accès et appelé le responsable sécurité)
> - **Élicitation** : 4 réussites sur 6 tentatives en contexte informel (cantine, fumoir, café)
> - **Implant réseau** : déployé à Bordeaux, actif 72h avant détection par l'équipe réseau (alerte sur un nouveau device inconnu)
> - **Taux de signalement** : 2,5 % (3 emails signalés au SOC sur 120 envoyés)
>
> **Impact potentiel si exploitation réelle :** les 2 comptes admin compromis auraient permis l'accès au tenant Azure AD, à l'ensemble des emails (Exchange Online), aux fichiers SharePoint (dont les documents du programme de défense) et au VPN. L'implant réseau aurait permis l'exfiltration de données depuis le réseau de production de Bordeaux.
>
> **Cas du « recruteur » étranger :** Nathan intègre le cas de David Chen dans le rapport comme illustration de la menace de niveau étatique. Le rapport souligne que la même vulnérabilité humaine (réceptivité à la flatterie, absence de contre-élicitation) a été exploitée par le red team (exercice contrôlé) et par un acteur de renseignement étranger (menace réelle).
>
> **Recommandations P0 :** (1) Déployer FIDO2 sur tous les comptes à privilèges, (2) Renforcer les procédures de helpdesk (callback obligatoire, interdiction des resets MFA par téléphone seul), (3) Mettre en place une procédure de double validation pour les virements > 5 000 €.
>
> **Recommandations P1 :** (4) Formation ciblée par profil de risque (ingénieurs R&D : contre-élicitation, DAF : BEC, helpdesk : pretexting, réception : intrusion physique), (5) Migration vers DESFire EV2 pour le contrôle d'accès physique, (6) Tourniquets anti-tailgating aux accès principaux.
>
> **Recommandations P2 :** (7) Programme de simulation de phishing mensuel avec retour individualisé, (8) Brief systématique avant les salons professionnels et les voyages, (9) Audit OSINT de la surface d'exposition de l'entreprise (informations accessibles en source ouverte).
>
> Helios lance un programme de remédiation sur 12 mois. Nathan conclut sa restitution : « La meilleure défense technique ne vaut rien si un humain tient la porte. Et la meilleure formation ne vaut rien si la culture d'entreprise punit ceux qui signalent un doute plutôt que de les remercier. »


---

## ANNEXES

---

### Annexe A — Glossaire (80+ termes)

| Terme | Définition |
|---|---|
| **APT (Advanced Persistent Threat)** | Groupe de menace étatique ou para-étatique menant des campagnes d'intrusion sophistiquées et persistantes |
| **Assessment** | Phase HUMINT d'évaluation d'une cible potentielle (accès, motivation, vulnérabilité) |
| **Baiting** | Technique consistant à laisser un support piégé (clé USB, CD) dans un lieu où il sera trouvé et utilisé |
| **Bash Bunny** | Outil d'intrusion USB multi-payload émulant divers périphériques |
| **BEC (Business Email Compromise)** | Compromission de messagerie d'entreprise — arnaque par email ciblant les processus financiers |
| **Callback verification** | Contre-mesure consistant à rappeler un interlocuteur sur un numéro de référence connu avant d'agir |
| **Caller ID spoofing** | Falsification du numéro affiché lors d'un appel téléphonique |
| **CIB (Coordinated Inauthentic Behavior)** | Comportement inauthentique coordonné sur les réseaux sociaux |
| **Cialdini (principes de)** | Six (puis sept) principes d'influence : réciprocité, engagement, preuve sociale, autorité, sympathie, rareté, unité |
| **Clonage RFID** | Copie d'un badge RFID légitime sur un support vierge |
| **Consent phishing** | Attaque exploitant les mécanismes OAuth pour obtenir des permissions d'accès persistantes |
| **Contre-élicitation** | Ensemble de techniques pour détecter et neutraliser une tentative d'élicitation |
| **Credential harvesting** | Collecte d'identifiants (login/mot de passe) via un formulaire frauduleux |
| **Cultivation** | Phase HUMINT de renforcement progressif de la relation avec une cible |
| **Deepfake** | Contenu audio ou vidéo synthétique généré par IA imitant une personne réelle |
| **DESFire** | Technologie de carte à puce RFID haute fréquence (13,56 MHz) avec chiffrement AES |
| **Device code phishing** | Attaque exploitant le flux OAuth2 device code pour obtenir des tokens d'accès |
| **DGSI** | Direction Générale de la Sécurité Intérieure — service de renseignement français (contre-espionnage, contre-ingérence) |
| **DKIM (DomainKeys Identified Mail)** | Protocole de signature cryptographique des emails |
| **DMARC** | Protocole d'authentification email combinant SPF et DKIM avec politique de rejet |
| **Dream Job (opération)** | Campagne du groupe Lazarus utilisant de faux recruteurs LinkedIn |
| **Dumpster diving** | Fouille des poubelles à la recherche d'informations exploitables |
| **Élicitation** | Extraction d'information dans une conversation apparemment normale |
| **Evilginx** | Outil de phishing reverse proxy capturant les tokens de session MFA |
| **FIDO2 / WebAuthn** | Standard d'authentification résistant au phishing basé sur la cryptographie à clé publique |
| **Flipper Zero** | Outil multi-protocole portable (RFID, NFC, IR, Sub-GHz) |
| **Fraude au président** | Variante de BEC où l'attaquant usurpe l'identité du dirigeant |
| **Fraude au fournisseur** | Variante de BEC exploitant un changement frauduleux de coordonnées bancaires |
| **HUMINT (Human Intelligence)** | Collecte de renseignement par des sources humaines |
| **IDN (Internationalized Domain Name)** | Domaine utilisant des caractères Unicode — exploitable pour le typosquatting |
| **Impersonation** | Fait de se faire passer pour une autre personne |
| **Implant** | Dispositif matériel ou logiciel déployé pour maintenir un accès persistant |
| **Insider involontaire** | Employé manipulé qui divulgue des informations sans réaliser la manipulation |
| **Insider malveillant** | Employé agissant délibérément contre les intérêts de son organisation |
| **ITDR (Identity Threat Detection and Response)** | Technologie de détection des menaces liées à l'identité |
| **LAN Turtle** | Implant réseau se branchant sur un port Ethernet |
| **Lettre de mission** | Document contractuel autorisant un test d'intrusion et définissant son scope |
| **Lock picking** | Crochetage de serrure mécanique |
| **Lure** | Appât — le message ou le pretexte utilisé pour tromper la cible |
| **MFA (Multi-Factor Authentication)** | Authentification multifacteur |
| **MFA bombing / push fatigue** | Attaque par envoi massif de demandes de validation MFA |
| **MICE** | Modèle d'analyse des motivations de recrutement : Money, Ideology, Coercion, Ego |
| **Mirroring** | Technique de rapport : reproduire subtilement le comportement de l'interlocuteur |
| **Name-dropping** | Mention de noms de personnes connues de la cible pour renforcer la crédibilité |
| **NFC (Near Field Communication)** | Communication en champ proche — technologie sans contact à courte distance |
| **No-blame post-mortem** | Retex sans blâme individuel, focalisé sur l'amélioration des processus |
| **OAuth** | Protocole d'autorisation permettant à des applications tierces d'accéder à des ressources |
| **OPSEC (Operational Security)** | Sécurité opérationnelle — protection des informations sur ses propres opérations |
| **OSINT (Open Source Intelligence)** | Renseignement en sources ouvertes |
| **Pacing-leading** | Technique de rapport : s'aligner sur l'interlocuteur puis le guider |
| **PEACE (modèle)** | Modèle d'entretien professionnel britannique (non confrontationnel) |
| **Phishing** | Hameçonnage — tentative de collecte d'informations via un message frauduleux |
| **Pig butchering** | Modèle industriel d'arnaque sentimentale avec « engraissement » de la victime |
| **Piggybacking** | Variante du tailgating avec interaction sociale active |
| **Pretexting** | Construction et utilisation d'un scénario fictif (pretexte) pour manipuler une cible |
| **Proxmark3** | Outil de recherche et de test RFID/NFC |
| **Quishing** | Phishing via QR code |
| **RASCLS** | Extension du modèle MICE : Reciprocity, Authority, Scarcity, Commitment, Liking, Social proof |
| **Red team** | Équipe simulant un adversaire pour tester les défenses d'une organisation |
| **Reply-chain attack** | Attaque par insertion dans un fil de conversation email légitime |
| **Reverse proxy phishing** | Phishing interceptant la communication entre la cible et le service légitime (Evilginx) |
| **RFID** | Identification par radiofréquence — technologie de badges sans contact |
| **Rubber Ducky** | Clé USB émulant un clavier pour exécuter des commandes |
| **Rules of engagement** | Règles d'engagement — cadre opérationnel d'un test d'intrusion |
| **Safe word** | Mot de passe convenu permettant l'identification immédiate du red teamer |
| **SIM swapping** | Transfert frauduleux d'un numéro de téléphone vers une nouvelle carte SIM |
| **Smishing** | Phishing par SMS |
| **Spear-phishing** | Phishing ciblé sur un individu ou un groupe restreint |
| **Spoofing** | Usurpation technique (adresse email, numéro de téléphone, adresse IP) |
| **Spotting** | Phase HUMINT d'identification de cibles potentielles |
| **SPF (Sender Policy Framework)** | Protocole définissant les serveurs autorisés à envoyer des emails pour un domaine |
| **STIR/SHAKEN** | Protocole d'authentification de l'identité de l'appelant dans les réseaux téléphoniques |
| **Supply chain humaine** | Ensemble des prestataires et partenaires ayant un accès physique ou logique |
| **Tailgating** | Suivre un employé à travers une porte contrôlée sans badger |
| **Typosquatting** | Enregistrement de domaines avec des fautes de frappe imitant un domaine légitime |
| **UEBA** | User and Entity Behavior Analytics — analyse comportementale des utilisateurs |
| **Vishing** | Phishing vocal — social engineering par téléphone |
| **Voice cloning** | Clonage vocal par IA — synthèse d'une voix imitant une personne réelle |
| **Watering hole** | Compromission d'un site web fréquenté par les cibles |
| **Whaling** | Phishing ciblant les dirigeants et cadres supérieurs |

---

### Annexe B — Cheat sheets

#### B.1 Pretextes classiques par vecteur

| Vecteur | Pretexte | Levier psychologique | Cible type |
|---|---|---|---|
| **Phishing** | Mise à jour portail RH | Obligation, urgence | Tous employés |
| **Phishing** | Invitation conférence | Curiosité, ego | Cadres, ingénieurs |
| **Phishing** | Facture / bon de commande | Routine, urgence | Comptabilité, achats |
| **Phishing** | Partage de document OneD/SharePoint | Normalité, confiance | Utilisateurs M365 |
| **Vishing** | Support IT — incident de sécurité | Autorité, peur, urgence | Tous employés |
| **Vishing** | Prestataire — intervention planifiée | Autorité, normalité | Helpdesk, réception |
| **Vishing** | Direction — demande urgente | Autorité, urgence, pression | DAF, assistants |
| **Vishing** | Recruteur — opportunité de carrière | Ego, cupidité | Ingénieurs, cadres |
| **Physique** | Technicien prestataire IT | Autorité, normalité | Gardien, réception |
| **Physique** | Inspecteur (incendie, qualité) | Autorité | Gardien, employés |
| **Physique** | Employé autre site | Normalité, sympathie | Employés, réception |
| **Élicitation** | Chercheur universitaire intéressé | Flatterie, réciprocité | Ingénieurs R&D |
| **Élicitation** | Consultant secteur / networking | Réciprocité, normalité | Cadres en salon |
| **Smishing** | Notification livraison | Curiosité, urgence | Tous |

#### B.2 Signaux d'alerte par technique

| Technique | Signaux d'alerte |
|---|---|
| **Phishing** | Expéditeur externe avec display name interne, urgence excessive, URL raccourcie ou lookalike, demande de credentials, pièce jointe inattendue |
| **Vishing** | Appel non sollicité demandant des informations sensibles, urgence, impossibilité de rappeler sur un numéro vérifié, name-dropping non vérifiable |
| **BEC** | Demande de virement urgente par email, confidentialité exigée, changement d'IBAN, pression hiérarchique anormale |
| **Intrusion physique** | Personne inconnue sans badge visible, pretexte de prestataire non vérifié, tentative de tailgating, comportement hésitant |
| **Élicitation** | Questions inhabituellement spécifiques, flatterie excessive, réciprocité forcée, transition vers canal privé, profil difficile à vérifier |

#### B.3 Checklist red team SE

- [ ] Lettre de mission signée par représentant habilité
- [ ] Rules of engagement documentées
- [ ] Scope (sites, employés, vecteurs, limites) défini
- [ ] Protocole d'urgence (safe word, contact de référence)
- [ ] Reconnaissance OSINT complétée
- [ ] Reconnaissance physique complétée
- [ ] Pretextes construits (principal + secours)
- [ ] Infrastructure technique déployée
- [ ] OPSEC praticien validé (légendes, compartimentation)
- [ ] Matériel préparé
- [ ] Documentation en temps réel planifiée
- [ ] Rapport final livré avec recommandations P0/P1/P2
- [ ] Debriefing commanditaire réalisé
- [ ] Implants physiques retirés
- [ ] Données de test détruites après livraison

---

### Annexe C — Tableau d'outils de référence

| Catégorie | Outil | Gratuit/Payant | Usage | Limites |
|---|---|---|---|---|
| **Phishing simulation** | GoPhish | Gratuit (open source) | Simulation de campagnes de phishing | Nécessite infrastructure, pas de support commercial |
| **Phishing simulation** | KnowBe4 | Payant (SaaS) | Simulation + formation + métriques | Coût, dépendance SaaS |
| **Phishing simulation** | Cofense PhishMe | Payant | Simulation + signalement + analyse | Coût |
| **Phishing infrastructure** | Evilginx2 | Gratuit (open source) | Reverse proxy phishing (bypass MFA) | Usage offensif uniquement en cadre autorisé |
| **OSINT** | Maltego | Freemium | Cartographie de relations | Quotas version gratuite, coût version pro |
| **OSINT** | SpiderFoot | Gratuit (open source) | Reconnaissance automatisée | Nécessite configuration, quotas API |
| **OSINT** | theHarvester | Gratuit | Collecte d'emails, sous-domaines | Limité sans API keys |
| **RFID/NFC** | Proxmark3 | ~300 € | Lecture, analyse, clonage de badges | Compétence technique requise |
| **RFID/NFC** | Flipper Zero | ~200 € | Multi-outil portable (RFID, NFC, IR) | Capacités RFID limitées vs Proxmark3 |
| **Implants USB** | Rubber Ducky | ~80 € | Injection de frappes clavier | Détectable par EDR avancés |
| **Implants USB** | Bash Bunny | ~120 € | Multi-payload, émulation périphériques | Détectable par EDR avancés |
| **Implant réseau** | LAN Turtle | ~60 € | Accès réseau distant via Ethernet | Nécessite accès physique, détectable par NAC |
| **Caller ID spoofing** | SpoofCard | Payant | Spoofing numéro appelant | Réglementé, illégal pour fraude |
| **Deepfake vocal** | ElevenLabs | Freemium | Clonage vocal | Limites éthiques, coût à l'échelle |
| **Deepfake détection** | Hive Moderation | Payant | Détection de contenu généré par IA | Faux positifs, taux variable |
| **Vishing** | SET (Social Engineering Toolkit) | Gratuit (open source) | Cadre de social engineering | Nécessite Kali Linux, maintenance inégale |

> **⚠️ Avertissement** : ces outils sont listés à titre de référence pour les praticiens autorisés. Leur utilisation en dehors d'un cadre légal (test autorisé, recherche en sécurité) constitue une infraction pénale.

---

### Annexe D — Templates opérationnels

#### D.1 Structure de lettre de mission red team SE

1. Identification des parties (commanditaire, prestataire, testeurs nommés)
2. Objet de la mission
3. Scope géographique (sites concernés)
4. Scope humain (employés concernés — tous ou profils spécifiques)
5. Vecteurs autorisés (phishing, vishing, smishing, intrusion physique, élicitation)
6. Techniques exclues (chantage, exploitation de vulnérabilités personnelles, etc.)
7. Durée de la mission (dates de début et de fin)
8. Objectifs mesurables
9. Protocole d'urgence (safe word, contact de référence joignable 24/7)
10. Confidentialité des résultats individuels
11. Livrables attendus (rapport, restitution)
12. Conditions financières
13. Signatures (commanditaire habilité, prestataire)

#### D.2 Fiche de signalement d'un incident de social engineering

- Date et heure de l'incident / de la tentative
- Vecteur (email, téléphone, physique, messagerie, autre)
- Description de l'incident (qui, quoi, quand, comment)
- Actions effectuées par l'employé (a cliqué, a transmis des informations, a donné un accès)
- Informations sur l'attaquant (nom affiché, numéro de téléphone, adresse email, description physique)
- Impact potentiel (credentials compromis, information divulguée, accès accordé)
- Actions correctives immédiates prises
- Signalement transmis à (SOC, RSSI, manager)

#### D.3 Checklist de protection en salon professionnel

**Avant le départ :**
- [ ] Brief avec le RSSI : messages autorisés, informations interdites
- [ ] Identification des interlocuteurs à risque (pays, secteurs, profils)
- [ ] Dispositifs numériques sécurisés (téléphone dédié si risque élevé, VPN, chiffrement)
- [ ] Cartes de visite avec informations limitées (pas de numéro personnel)

**Pendant le salon :**
- [ ] Ne jamais laisser un dispositif sans surveillance
- [ ] Ne pas discuter de projets sensibles en public
- [ ] Appliquer les techniques de contre-élicitation si nécessaire (pont, déviation, réponse vague)
- [ ] Noter les contacts inhabituels (nom, entreprise, questions posées)

**Au retour :**
- [ ] Debriefing avec le RSSI
- [ ] Signalement des contacts suspects
- [ ] Vérification des dispositifs numériques (pas de malware, pas de modification)

#### D.4 Grille de formation par profil de risque

| Profil | Menaces prioritaires | Contenu de formation | Fréquence | Format |
|---|---|---|---|---|
| Tous employés | Phishing, tailgating | Sensibilisation générale, signalement | Annuelle | E-learning + simulation |
| DAF / Comptabilité | BEC, fraude fournisseur | Processus de vérification, callback | Semestrielle | Atelier + simulation |
| Helpdesk | Pretexting, MFA manipulation | Vérification d'identité renforcée | Trimestrielle | Exercice vishing |
| Ingénieurs R&D | Élicitation, faux recruteurs | Contre-élicitation, protection en salon | Annuelle | Atelier interactif |
| Réception / Sécurité | Intrusion physique, impersonation | Vérification visiteurs, refus poli | Semestrielle | Exercice pratique |
| Dirigeants | Ciblage personnel, deepfake, spear-phishing | Surface d'exposition, sécurité des communications | Annuelle | Briefing individuel |

---

### Annexe E — Ressources et formation

#### E.1 Certifications

| Certification | Organisme | Focus SE | Coût indicatif | Pertinence |
|---|---|---|---|---|
| SEC567 — Social Engineering for Pentesters | SANS | Élevé (dédié SE) | ~8 000 € (formation + examen) | Référence pour le red team SE |
| GPEN | GIAC | Moyen (SE dans pentest global) | ~3 000 € (examen seul) | Pentest généraliste |
| OSCP | Offensive Security | Faible (SE marginal) | ~1 600 € | Pentest technique |
| Certified Social Engineer | Social-Engineer.org | Élevé (dédié SE) | Variable | Spécialisé mais reconnaissance limitée |
| CEH | EC-Council | Faible | ~1 200 € | Entrée de gamme, couverture SE superficielle |

#### E.2 Conférences

- **DEF CON — Social Engineering Village** : la communauté de référence mondiale pour le SE. Compétitions de SE en direct (SECTF — Social Engineering Capture the Flag), présentations, ateliers.
- **Black Hat** : présentations techniques incluant régulièrement des tracks sur le social engineering.
- **BSides** : conférences communautaires locales avec des tracks SE.
- **Wild West Hackin' Fest** : conférence fondée par SANS avec un focus pratique.

#### E.3 Livres de référence

- **Christopher Hadnagy** — *Social Engineering: The Science of Human Hacking* (2e édition, Wiley, 2018) : le livre de référence pour les praticiens.
- **Christopher Hadnagy** — *Phishing Dark Waters* (Wiley, 2016) : focus sur le phishing offensif et défensif.
- **Kevin Mitnick** — *The Art of Deception* (Wiley, 2002) : classique fondateur, récits d'ingénierie sociale réels.
- **Robert Cialdini** — *Influence: The Psychology of Persuasion* (1984, rééditions multiples) : fondements psychologiques.
- **Robert Cialdini** — *Pre-Suasion* (2016) : le 7e principe (unité) et les techniques de pré-persuasion.
- **Joe Navarro** — *What Every BODY is Saying* (2008) : communication non verbale pour les praticiens.

#### E.4 Communautés

- **Social-Engineer.org** : ressources, podcast, framework, formation (Christopher Hadnagy).
- **SECTF** : Social Engineering Capture the Flag — compétitions DEF CON.
- **r/SocialEngineering** (Reddit) : discussions communautaires (qualité variable).

---

### Annexe F — Cadre juridique

#### F.1 France

| Infraction | Article du Code pénal | Peine maximale | Application au SE |
|---|---|---|---|
| Escroquerie | Art. 313-1 | 5 ans + 375 000 € | Fraude au président, BEC, phishing |
| Usurpation d'identité | Art. 226-4-1 | 1 an + 15 000 € | Impersonation (y compris en ligne) |
| Accès frauduleux à un STAD | Art. 323-1 | 3 ans + 100 000 € | Intrusion informatique post-phishing |
| Atteinte au secret des correspondances | Art. 226-15 | 1 an + 45 000 € | Compromission de boîte mail |
| Fabrication/usage de faux | Art. 441-1 | 3 ans + 45 000 € | Faux documents, faux badges |
| Violation de domicile | Art. 226-4 | 1 an + 15 000 € | Intrusion physique non autorisée |
| Collecte frauduleuse de données personnelles | Art. 226-18 | 5 ans + 300 000 € | Credential harvesting |

**Le red team autorisé** : la lettre de mission signée par un représentant habilité constitue le fondement juridique de l'autorisation. Elle ne crée pas un « droit à commettre des infractions » mais établit le consentement de l'organisation — ce qui élimine l'un des éléments constitutifs de la plupart des infractions (le caractère frauduleux, non autorisé ou sans le consentement de la victime). La lettre de mission doit être juridiquement robuste (rédaction par un avocat recommandée) et couvrir explicitement chaque technique utilisée.

**RGPD.** Les données personnelles collectées pendant un test de SE (identifiants, informations personnelles, photos) sont soumises au RGPD. Le traitement doit avoir une base légale (l'intérêt légitime du responsable de traitement, avec l'analyse d'impact correspondante), les données doivent être minimisées, sécurisées et détruites après la fin de la mission.

#### F.2 Comparatif international

| Aspect | France | Union européenne | États-Unis |
|---|---|---|---|
| Usurpation d'identité en ligne | Délit spécifique (art. 226-4-1) | Variable selon les États membres | Federal : 18 USC § 1028, variable selon les États |
| Enregistrement de conversations | Interdit sans consentement (art. 226-1) | Variable (certains pays autorisent avec une seule partie consentante) | Variable selon les États (one-party vs two-party consent) |
| Red team autorisé | Encadré par lettre de mission | Encadré par le droit national des États membres | Encadré par contrat, jurisprudence CFAA |
| Pretexting dans les enquêtes privées | Limité (pas de faux documents officiels) | Variable | Plus largement toléré (sauf pour obtenir des données financières — GLBA) |

---

### Annexe G — Mapping de la bibliothèque

| Cours de la bibliothèque | Articulation avec le présent cours |
|---|---|
| **Cybersécurité du quotidien** | Prisme victime (reconnaître, se protéger). Le présent cours explique comment les attaques sont construites et testées. |
| **Intelligence économique** | HUMINT d'entreprise légal, protection en salon. Le présent cours approfondit les techniques d'élicitation et la contre-ingérence. |
| **APT** | SE comme vecteur d'accès initial. Le présent cours détaille les techniques elles-mêmes. |
| **OSINT Mastery** | Méthodes de reconnaissance. Le présent cours montre l'application au SE. |
| **CTI** | Attribution et analyse des groupes de menace utilisant le SE. Le présent cours détaille les TTPs. |
| **GRC** | Cadre réglementaire, conformité. Le présent cours traite le cadre juridique spécifique au SE et au red team. |
| **Cryptographie** | Technologies de protection (FIDO2, chiffrement). Le présent cours explique les contournements par SE. |
| **Active Directory / Infrastructure IT** | Surface d'attaque technique. Le présent cours montre comment le SE fournit l'accès initial qui permet l'exploitation technique. |
| **Forensic** | Investigation post-incident. Le présent cours traite la dimension humaine de l'investigation SE. |

---

*Fin du cours — HUMINT et Social Engineering — Élicitation, manipulation et contre-ingénierie sociale*
*Version 2025-2026*

