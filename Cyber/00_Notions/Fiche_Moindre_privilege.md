---
format: fiche
termes:
  Moindre privilège: Accorder à chaque utilisateur, service ou processus uniquement les droits strictement nécessaires à sa fonction, et rien de plus.
---
# Moindre privilège

> Fiche notion assemblée à partir de mes notes (sources sous chaque bloc).

## En bref

**Définition.** Accorder à chaque utilisateur, service ou processus *uniquement* les droits strictement nécessaires à sa fonction, et rien de plus (Principle of Least Privilege, PoLP).

**Principe.** Réduit l'impact d'une compromission : un compte limité, une fois volé, ne donne accès qu'à peu de choses. Inclut la *limitation dans le temps* (droits temporaires, just-in-time) et dans le *périmètre*.

*↳ [[Taxonomie_Cyber|Taxonomie cyber]] (chapitre 12)*

## Comment l'expliquer

C'est le principe qui consiste à donner à chaque utilisateur, application ou processus uniquement les droits strictement nécessaires pour accomplir sa tâche, rien de plus. Un développeur n'a pas besoin d'être admin du domaine. Un compte de service n'a pas besoin d'accéder à toutes les bases de données. L'idée c'est de réduire la surface d'attaque : si un compte est compromis, l'attaquant n'a accès qu'à un périmètre limité. C'est un pilier de la sécurité qui s'applique partout — RBAC dans Kubernetes, IAM dans le cloud, GPO dans AD.

*↳ [[Questions_Entretien_Cyber_SysAdmin|Questions d'entretien]] (réponse type)*

## Exemples

🔧 **Exemple concret** — Une application web qui ne fait que *lire* une base ne doit pas avoir de droits d'*écriture* ni d'*administration*. Si elle est compromise par injection SQL, les dégâts restent limités à de la lecture.

*↳ [[Taxonomie_Cyber|Taxonomie cyber]] (chapitre 12)*

**Le principe de moindre privilège** : un compte applicatif ne devrait avoir que les permissions strictement nécessaires. Le compte qui sert le site web n’a pas besoin de pouvoir `DROP TABLE` ou `CREATE USER`.

*↳ [[SQL|SQL]]*

**Principe du moindre privilège.** Chaque utilisateur ne dispose que des accès nécessaires à ses fonctions. Cela limite l'impact d'une compromission : un identifiant d'employé standard compromis par phishing donne accès aux ressources de l'employé, pas aux ressources de l'ensemble de l'organisation.

*↳ [[HUMINT_Social_Engineering|HUMINT & social engineering]]*

> **À retenir pour un entretien :** “Le RBAC dans Kubernetes fonctionne par le principe de moindre privilège : chaque utilisateur et chaque service account ne doit avoir que les permissions strictement nécessaires. Le cluster-admin ne devrait être attribué qu’aux administrateurs du cluster.”

*↳ [[Containers_Docker_K8s|Conteneurs — Docker & Kubernetes]]*

## Dans la gouvernance

Les principes de gouvernance IAM : moindre privilège (ne donner que les droits nécessaires à la fonction), séparation des devoirs (l'approbateur n'est pas l'exécutant), besoin d'en connaître (l'accès à une information est conditionné par la nécessité fonctionnelle).

*↳ [[GRC|GRC]]*

## Erreur fréquente

⚠️ **Erreur fréquente** — Donner les droits administrateur « pour que ça marche tout de suite », puis ne jamais les retirer. L'accumulation de droits (privilege creep) est un fléau silencieux.

*↳ [[Taxonomie_Cyber|Taxonomie cyber]] (chapitre 12)*

## À retenir

🎯 **À retenir** — Le moindre privilège ne *prévient* pas l'intrusion, il en *limite l'impact*. C'est l'application de « assume breach ».

*↳ [[Taxonomie_Cyber|Taxonomie cyber]] (chapitre 12)*

## Voir aussi

[[Fiche_Defense_en_profondeur|Défense en profondeur]] · [[Fiche_Zero_Trust|Zero Trust]] · [[Fiche_Surface_d_attaque|Surface d'attaque]]
