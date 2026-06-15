# Cours Complet d'Assembleur x86-64 sous Linux

## De zéro au reverse engineering débutant — Guide pour débutant absolu

---

> **Prérequis :** Aucun. Ce cours est conçu pour quelqu'un qui n'a jamais écrit une seule ligne de code, ne connaît pas l'algorithmique et ne connaît pas le fonctionnement interne d'un ordinateur.
> Tout ce dont tu as besoin, c'est un ordinateur avec Linux (Ubuntu/Debian recommandé) ou Windows avec WSL2.

---

## Avant de commencer — Lis ça

L'assembleur a une mauvaise réputation : "c'est trop dur", "c'est pour les génies", "c'est cryptique". **Ce n'est ni magique, ni réservé à une élite.**

Soyons honnête : l'assembleur est **plus exigeant** que Python ou Bash, parce qu'il demande de manipuler explicitement ce que les langages haut niveau te cachent — registres, mémoire, pile, tailles de données, appels système. La difficulté vient surtout du **niveau de détail**, pas d'une complexité inaccessible. Chaque ligne fait *une seule petite chose*. Ce qui rend l'assembleur intimidant, c'est :

1. Le **vocabulaire technique** qui s'accumule au début (registres, syscalls, flags, pile…) — ce cours t'introduit ces termes un par un, au bon moment.
2. Le fait qu'on ne voit **rien** par défaut (pas de `print()` automatique) — on apprend très vite à utiliser GDB pour voir ce qui se passe.
3. La **distance** avec ce qu'on connaît (cliquer, taper du texte) — ce cours fait sans cesse le pont avec Bash et Python.

> **Ce cours ne te transformera pas en hacker en 3 jours.** Il te donne les vraies fondations pour comprendre comment un ordinateur exécute du code, lire un binaire, comprendre GDB, et démarrer en reverse engineering. Le reste, c'est de la pratique.

---

## À qui s'adresse ce cours

- À quelqu'un qui n'a **jamais programmé**.
- À quelqu'un qui veut comprendre **comment un ordinateur fonctionne vraiment**.
- À quelqu'un qui s'intéresse à la **cybersécurité**, au **reverse engineering**, à l'**analyse de binaires** ou aux **CTF**.
- À quelqu'un qui a peur de GDB et veut le démystifier.

## Ce que ce cours n'est PAS

Pour rester pédagogique et accessible, certains sujets sont **volontairement exclus**. Ils méritent un cours à part, après celui-ci :

- ❌ Ce n'est **pas** un cours de **shellcode**.
- ❌ Ce n'est **pas** un cours d'**exploitation** (buffer overflow, ROP, format string…).
- ❌ Ce n'est **pas** un cours de **malware analysis** avancée.
- ❌ Ce n'est **pas** un cours de programmation **noyau** ou de drivers.
- ❌ Ce n'est **pas** un cours d'**optimisation CPU** (pipeline, cache, SIMD/SSE/AVX).
- ❌ Ce n'est **pas** un cours d'assembleur **Windows** (on reste sur Linux).
- ❌ Ce n'est **pas** un cours de **C inline assembly**.

Ces sujets peuvent venir **après**, une fois que les fondamentaux de ce cours sont acquis.

## 🎯 L'objectif final, concrètement

Pour que tu saches exactement où tu vas, voici ce que tu dois être capable de faire **à la fin de ce cours** :

- **Lire** un extrait d'assembleur simple et le comprendre.
- **Reconnaître** dans un désassemblage : une **condition** (`if`), une **boucle**, une **fonction**, un **appel à la libc** (`printf`, `strcmp`…).
- **Suivre les arguments** passés à une fonction dans GDB.
- **Résoudre un crackme débutant** (mot de passe en clair, comparaison caractère par caractère, transformation XOR simple).
- **Écrire** quelques petits programmes ASM, mais **ce n'est pas le but principal**. L'objectif réel est la **lecture** et la **reconnaissance de patterns**.

> Tu ne deviendras pas développeur assembleur professionnel avec ce cours, **et ce n'est pas le but**. Tu deviendras un **lecteur d'assembleur** compétent, ce qui est exactement ce dont tu as besoin pour le reverse, les CTF, le debug et la cybersécurité.

---

## Glossaire — Les mots à connaître

Avant de commencer, voici les termes que tu vas rencontrer tout au long du cours. Reviens ici si un mot te semble flou.

| Terme | Définition simple |
|-------|------------------|
| **CPU** | Le "cerveau" de l'ordinateur. Il exécute les instructions une par une |
| **RAM** | La mémoire vive, où sont stockées les données et le code pendant l'exécution |
| **Registre** | Une mini-case de stockage **dans** le CPU, ultra-rapide, qui contient une valeur (typiquement 64 bits) |
| **Instruction** | Un ordre élémentaire pour le CPU (`mov`, `add`, `jmp`…) |
| **Opcode** | La représentation **binaire** d'une instruction, telle que le CPU la voit |
| **Bit** | La plus petite unité d'information : 0 ou 1 |
| **Octet (byte)** | 8 bits, qui forment ensemble une valeur de 0 à 255 |
| **Binaire** | Système de numération à base 2 (0 et 1) |
| **Hexadécimal** | Système de numération à base 16 (0-9 puis A-F). Noté `0x...` |
| **Adresse mémoire** | Le numéro qui désigne une case précise dans la RAM |
| **Pointeur** | Une valeur qui contient une adresse mémoire |
| **Pile (stack)** | Une zone de mémoire spéciale où l'on empile et dépile des valeurs |
| **Syscall** | Une demande de service au noyau du système (afficher, lire, ouvrir un fichier…) |
| **Noyau (kernel)** | Le programme central de Linux qui gère le matériel et les processus |
| **Assembleur (langage)** | Le langage que tu vas apprendre |
| **Assembleur (logiciel)** | Le programme qui traduit ton code en code machine (NASM dans ce cours) |
| **NASM** | L'assembleur que nous utilisons (Netwide Assembler) |
| **Linker** | Le programme qui transforme un fichier objet en exécutable (`ld`, ou `gcc`) |
| **Exécutable** | Un fichier que le système peut lancer (en ELF sur Linux) |
| **ELF** | Le format des exécutables sous Linux (Executable and Linkable Format) |
| **GDB** | Le debugger : il permet de regarder un programme s'exécuter ligne par ligne |
| **Désassemblage** | L'opération inverse : prendre un binaire et retrouver de l'assembleur lisible |
| **Reverse engineering** | Comprendre un programme dont on n'a pas le code source |
| **ABI** | Les règles de communication entre fonctions (qui met quoi où) |
| **Fonction** | Un bloc de code réutilisable avec un nom, des arguments, un résultat |
| **Stack frame** | L'espace de travail d'une fonction sur la pile |
| **Flag (drapeau)** | Un mini-indicateur dans le CPU (0 ou 1) qui mémorise le résultat de la dernière opération |
| **Section** | Une zone du fichier `.asm` : code (`.text`), données (`.data`), réservées (`.bss`) |
| **Label (étiquette)** | Un nom que tu donnes à un endroit du code ou des données |
| **Syntaxe Intel** | La syntaxe utilisée dans ce cours : `mov destination, source` |
| **Syntaxe AT&T** | L'autre syntaxe (`mov source, destination`), qu'on apprendra **seulement à lire** plus tard |

---

## Comment penser un programme assembleur

Avant d'écrire la moindre ligne de code, il faut comprendre la logique de base. En Bash ou Python, tu raisonnes en termes de :

```
  ENTRÉE           TRAITEMENT           SORTIE
  Ce que le    →   Ce que le script  →  Ce que le script
  script reçoit    fait avec            produit comme résultat
```

En **assembleur**, le modèle mental change. Tu raisonnes en termes de **trois mondes** qui s'échangent des données :

```
  ┌─────────────┐    ┌─────────────┐    ┌──────────────────┐
  │  REGISTRES  │←──→│   MÉMOIRE   │←──→│ SYSCALLS/FONCTIONS│
  │    (CPU)    │    │    (RAM)    │    │     (SYSTÈME)     │
  └─────────────┘    └─────────────┘    └──────────────────┘
```

- Les **registres**, c'est ton bureau de travail (petit, rapide, mais limité).
- La **mémoire**, c'est ta bibliothèque (grande, plus lente, on y va chercher et on y range).
- Les **syscalls/fonctions**, c'est ton interface avec l'extérieur (afficher, lire, ouvrir un fichier).

Concrètement, **il n'y a que 10 briques de base** dans un programme assembleur :

1. **Charger** une valeur dans un registre.
2. **Déplacer** une valeur entre registres et mémoire.
3. **Calculer** dans les registres (addition, soustraction, multiplication…).
4. **Comparer** deux valeurs.
5. **Sauter** vers une autre partie du programme (selon le résultat d'une comparaison ou pas).
6. **Lire/écrire** via le système (afficher, lire au clavier, ouvrir un fichier).
7. **Empiler/dépiler** des valeurs sur la pile.
8. **Appeler/retourner** d'une fonction.
9. **Observer** ce qui se passe avec GDB.
10. **Lire** du code désassemblé pour comprendre un binaire.

Tous les programmes assembleur, même les plus complexes, sont une combinaison de ces 10 briques. Garde ça en tête à chaque chapitre.

---

## La grande différence avec Bash et Python

Si tu viens des cours Bash et Python de cette collection, **trois différences fondamentales** sont à comprendre :

### 1. Pas de variables typées

En Python, tu as `int`, `str`, `list`… En assembleur, **tout est des octets**. Que ce soit un nombre, une lettre ou une adresse, ce sont des octets. C'est toi qui décides comment les interpréter.

### 2. Pas d'affichage automatique

En Python, `print(x)` affiche `x`. En assembleur, il n'y a **rien** d'automatique. Pour afficher, il faut **demander au système** via un syscall. C'est pour ça qu'on apprend très vite GDB : pour **voir** les valeurs sans devoir les afficher.

### 3. Une seule micro-action par ligne

En Python, `c = a + b` fait deux choses en une ligne (calculer et stocker). En assembleur, il faut **deux instructions** : `mov rax, [a]` puis `add rax, [b]`. C'est plus verbeux, mais c'est aussi pour ça qu'on comprend exactement ce que le CPU fait.

> **À retenir :** l'assembleur n'est pas plus dur, il est plus **explicite et plus détaillé**. Ce que Python te cachait, l'assembleur te le montre. C'est précisément ce qui en fait un outil précieux pour la cybersécurité et le reverse.

---

## Méthode de travail recommandée

L'assembleur ne s'apprend pas en lisant — il s'apprend en **tapant** et en **observant**. Pour chaque programme du cours, applique systématiquement ce rituel en 6 étapes :

1. **Lire** le code et essayer de comprendre.
2. **Prédire** sur papier la valeur de chaque registre après chaque instruction.
3. **Recopier** à la main (pas copier-coller — ton cerveau retient mieux).
4. **Exécuter** normalement (vérifier `echo $?` ou la sortie).
5. **Exécuter dans GDB** (à partir du chapitre 9) et comparer avec ta prédiction.
6. **Modifier** une valeur, et **refaire l'observation**. Comprendre ce qui change.

> **Conseil important :** si un chapitre te paraît flou, **continue quand même**. Plusieurs notions ne s'éclairent qu'à la lumière du chapitre suivant. Reviens en arrière une fois que tu as vu la suite.

## Trois niveaux de maîtrise

Pour rester réaliste sur tes objectifs : il y a **trois niveaux** d'apprentissage de l'assembleur. Tu n'as pas besoin de tous les atteindre à 100 %.

| Niveau | Objectif | Importance pour ce cours |
|--------|----------|--------------------------|
| **Écrire** | Savoir produire un petit programme assembleur à la main | ⭐⭐ Important au début |
| **Lire** | Comprendre un extrait ASM qu'on te donne | ⭐⭐⭐ Cœur du cours |
| **Reconnaître** | Identifier un pattern (boucle, `if`, appel…) dans un binaire | ⭐⭐⭐ Objectif final |

> **L'objectif réaliste pour la cybersécurité : viser surtout "lire" et "reconnaître".** Très peu de gens écrivent de l'assembleur entier de nos jours. **Tout le monde**, en revanche, doit savoir le lire pour faire du reverse, du debug, du CTF.

## Sur la montée en difficulté

Le cours commence très doux (chapitres 1-9), puis devient progressivement plus dense. **À partir de la partie V** (entrées/sorties, conversions, fichiers), le cours reste accessible mais demande **plus de pratique**. Il est normal de devoir :

- Refaire un exemple plusieurs fois.
- Relire un chapitre à tête reposée.
- Bloquer sur la pile, les fonctions, ou le reverse — c'est **normal**.

Ne te juge pas. La patience compte plus que la vitesse.

---

## Table des matières

**PARTIE 0 — PRÉAMBULE** *(tu es ici)*

**PARTIE I — COMPRENDRE LA MACHINE**

1. [Qu'est-ce que l'assembleur et pourquoi l'apprendre ?](#chapitre-1--quest-ce-que-lassembleur-et-pourquoi-lapprendre)
2. [CPU, RAM, registres : le modèle mental minimum](#chapitre-2--cpu-ram-registres--le-modèle-mental-minimum)
3. [Binaire, hexadécimal, ASCII et tailles de données](#chapitre-3--binaire-hexadécimal-ascii-et-tailles-de-données)

**PARTIE II — INSTALLER, ÉCRIRE, EXÉCUTER**

4. [Environnement de travail et premier programme](#chapitre-4--environnement-de-travail-et-premier-programme)
5. [Anatomie d'un fichier .asm](#chapitre-5--anatomie-dun-fichier-asm)
6. [Premier affichage avec `write`](#chapitre-6--premier-affichage-avec-write)

**PARTIE III — REGISTRES, CALCULS ET OBSERVATION**

7. [Déplacer des données avec `mov`](#chapitre-7--déplacer-des-données-avec-mov)
8. [Calculer avec les registres](#chapitre-8--calculer-avec-les-registres)
9. [GDB pour observer les registres](#chapitre-9--gdb-pour-observer-les-registres)

**PARTIE IV — MÉMOIRE, ADRESSES ET CHAÎNES**

10. [Mémoire, adresses et variables](#chapitre-10--mémoire-adresses-et-variables)
11. [Chaînes de caractères et octets](#chapitre-11--chaînes-de-caractères-et-octets)
12. [`lea` et modes d'adressage](#chapitre-12--lea-et-modes-dadressage)

**PARTIE V — ENTRÉES, SORTIES ET CONVERSIONS**

13. [Lire au clavier avec `read`](#chapitre-13--lire-au-clavier-avec-read)
14. [Convertir texte et nombres](#chapitre-14--convertir-texte-et-nombres)
15. [Fichiers et syscalls utiles](#chapitre-15--fichiers-et-syscalls-utiles)

**PARTIE VI — LOGIQUE ET CONTRÔLE DE FLUX**

16. [Comparaisons, flags et sauts](#chapitre-16--comparaisons-flags-et-sauts)
17. [Boucles](#chapitre-17--boucles)

**PARTIE VII — PILE ET FONCTIONS**

18. [La pile avec `push`, `pop` et `rsp`](#chapitre-18--la-pile-avec-push-pop-et-rsp)
19. [Fonctions avec `call` et `ret`](#chapitre-19--fonctions-avec-call-et-ret)
20. [Stack frame, `rbp` et variables locales](#chapitre-20--stack-frame-rbp-et-variables-locales)

**PARTIE VIII — LIEN AVEC C ET LIBC**

21. [Appeler la libc depuis l'assembleur](#chapitre-21--appeler-la-libc-depuis-lassembleur)
22. [Du C vers l'assembleur](#chapitre-22--du-c-vers-lassembleur)

**PARTIE IX — LECTURE DE BINAIRES ET REVERSE DÉBUTANT**

23. [Désassembler un binaire ELF](#chapitre-23--désassembler-un-binaire-elf)
24. [Reverse engineering débutant avec GDB](#chapitre-24--reverse-engineering-débutant-avec-gdb)

**PARTIE X — SYNTHÈSE**

25. [Récapitulatif complet du débutant](#chapitre-25--récapitulatif-complet-du-débutant)

**ANNEXES**

- A. [Syntaxe AT&T pour la lecture](#annexe-a--syntaxe-att-pour-la-lecture)
- B. [x86 32 bits vs x86-64](#annexe-b--x86-32-bits-vs-x86-64)
- C. [Linux System V ABI vs Windows x64 ABI](#annexe-c--linux-system-v-abi-vs-windows-x64-abi)
- D. [Nombres signés, complément à deux et débordements](#annexe-d--nombres-signés-complément-à-deux-et-débordements)
- E. [Little-endian](#annexe-e--little-endian)
- F. [Makefile et commandes utiles](#annexe-f--makefile-et-commandes-utiles)
- G. [Glossaire assembleur / reverse](#annexe-g--glossaire-assembleur--reverse)
- H. [Panorama des outils de reverse](#annexe-h--panorama-des-outils-de-reverse)
- I. [Suite logique après ce cours](#annexe-i--suite-logique-après-ce-cours)

---

# PARTIE I — COMPRENDRE LA MACHINE

---

# Chapitre 1 — Qu'est-ce que l'assembleur et pourquoi l'apprendre

## Le minimum à savoir

### Les trois niveaux de langage

Quand tu écris un programme, il existe trois niveaux d'écriture, du plus humain au plus proche de la machine :

```
   PYTHON              C            ASSEMBLEUR        CODE MACHINE
 print("Hi")    printf("Hi");      mov rax, 1        01001000 10110000
                                   mov rdi, 1        00000001 ...
                                   mov rsi, msg
                                   mov rdx, 2
                                   syscall

  Très lisible    Moyennement      Une instruction    Que des 0 et 1
  pour l'humain   technique        par ligne          Que le CPU lit
```

- **Python**, c'est presque du français.
- **C**, c'est plus court mais déjà technique.
- **Assembleur**, c'est l'étape juste avant le code machine : chaque ligne correspond à **une instruction** que le CPU exécute.
- **Code machine**, c'est ce que la CPU lit vraiment : que des `0` et `1`. Personne n'écrit ça à la main.

### Qu'est-ce que l'assembleur, exactement ?

L'assembleur, c'est **le langage du CPU, mais écrit avec des mots** au lieu de chiffres binaires. Chaque instruction (`mov`, `add`, `cmp`…) correspond à **un opcode**, c'est-à-dire à un motif binaire précis que le CPU reconnaît.

> **Important :** Le mot "assembleur" désigne **deux choses** :
> - Le **langage** (les mots `mov`, `add`, `jmp`…).
> - Le **logiciel** qui traduit ce langage en code machine. Dans ce cours, ce logiciel s'appelle **NASM**.

### Pourquoi l'apprendre aujourd'hui ?

Tu te demandes peut-être : "Si Python existe, pourquoi apprendre quelque chose d'aussi bas niveau ?". Voici les vraies raisons :

| Cas d'usage | À quoi ça sert |
|-------------|----------------|
| **Reverse engineering** | Comprendre un programme dont tu n'as pas le code source (logiciel propriétaire, malware, binaire mystérieux) |
| **CTF / cybersécurité** | Les épreuves de catégorie "reverse" et "pwn" demandent toutes de lire de l'assembleur |
| **Debugging avancé** | Quand ton programme C plante avec un `segfault` cryptique, GDB te montre de l'assembleur |
| **Analyse de malware** | Les virus sont des binaires ; les analyser, c'est lire de l'assembleur |
| **Optimisation critique** | Dans certains cas (jeux, compression, crypto), connaître l'assembleur permet d'optimiser à l'extrême |
| **Comprendre les bugs "bizarres"** | Buffer overflow, integer overflow, race conditions… s'expliquent au niveau machine |
| **Curiosité légitime** | Comprendre comment ton ordinateur fonctionne *vraiment* |

### Écrire de l'ASM vs lire de l'ASM

Une distinction cruciale pour ce cours :

- **Écrire de l'assembleur** est rare. Très peu de gens écrivent des programmes entiers en ASM aujourd'hui.
- **Lire de l'assembleur** est très courant. Quiconque fait du reverse, du CTF, ou du debug profond le fait tous les jours.

> **Ce cours t'apprend à écrire d'abord, pour pouvoir lire ensuite.** Tu ne pourras jamais lire correctement un langage que tu ne sais pas écrire un minimum.

## Très utile en pratique

### Pourquoi l'ASM est "verbeux"

En Python, tu écris :

```python
c = a + b
```

C'est **une ligne**, et elle fait trois choses : lire `a`, lire `b`, additionner, stocker dans `c`.

En assembleur, ces quatre actions sont **explicites** :

```nasm
mov rax, [a]    ; 1. Charger la valeur de 'a' dans le registre rax
add rax, [b]    ; 2. Ajouter la valeur de 'b' à rax
mov [c], rax    ; 3. Ranger le résultat de rax dans 'c'
```

> **À retenir :** l'assembleur est verbeux parce qu'il **n'a rien à cacher**. Ce que Python te cache (le chargement, le stockage, l'allocation mémoire), l'assembleur te le montre.

### Le même programme à trois niveaux

Voici "Bonjour" en Python, C et assembleur. Tu ne dois rien comprendre, juste **regarder** :

**Python :**
```python
print("Bonjour")
```

**C :**
```c
#include <stdio.h>
int main() {
    printf("Bonjour\n");
    return 0;
}
```

**Assembleur (x86-64, Linux, syntaxe Intel) :**
```nasm
section .data
    msg db "Bonjour", 10
    len equ $ - msg

section .text
global _start
_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall

    mov rax, 60
    mov rdi, 0
    syscall
```

Plus on descend, plus c'est verbeux. **Et c'est normal.** Plus on descend, plus chaque opération est explicite.

## ❌ Erreur classique

```
Croire qu'il faut être électronicien pour apprendre l'ASM
→ Faux. On ne touche jamais à du matériel.

Croire que l'ASM va "remplacer" Python ou C
→ Faux. Ce sont des outils différents pour des usages différents.

Croire qu'il faut tout comprendre dès le premier programme
→ Faux. On recopie sans comprendre au début, on comprend après.

Croire que l'ASM est "magique" ou ésotérique
→ Faux. C'est juste verbeux et minutieux.
```

## Exercices

**Guidé :** En 3 phrases, explique à un ami fictif ce qu'est l'assembleur et pourquoi tu l'apprends.

**Autonome :** Cite **3 métiers ou situations** où savoir lire de l'assembleur est utile. Pour chacun, explique en une phrase pourquoi.

**Défi :** Reprends les trois versions du "Bonjour" ci-dessus. Compte le nombre de **lignes utiles** dans chaque version (sans les lignes vides). Que conclus-tu sur le rapport "lisibilité / nombre de lignes" ?

## ✅ Tu sais maintenant…

- Ce qu'est l'assembleur (langage **et** logiciel)
- Les trois niveaux de langage (Python, C, ASM)
- Pourquoi l'assembleur est verbeux
- À quoi sert l'ASM en cybersécurité et reverse
- La différence entre **écrire** et **lire** de l'assembleur

---

# Chapitre 2 — CPU, RAM, registres : le modèle mental minimum

## Le minimum à savoir

### Où vivent les données et le code ?

Pour comprendre l'assembleur, il faut un modèle mental clair de **ce qui se passe dans l'ordinateur** (version simplifiée — les CPU modernes font en réalité plein d'optimisations comme le pipelining et l'exécution spéculative, mais ce n'est pas le sujet ici). Inutile d'être ingénieur en électronique — il suffit d'avoir la bonne image en tête.

```
┌────────────────────────────────────────────────────────────┐
│                         ORDINATEUR                          │
│                                                             │
│   ┌──────────────────┐         ┌─────────────────────────┐ │
│   │       CPU        │         │          RAM            │ │
│   │                  │         │                         │ │
│   │  ┌────┬────┬───┐ │         │   ┌─────┬─────┬─────┐  │ │
│   │  │rax │rbx │...│ │ ←─────→ │   │ 0x1 │ 0x2 │ ... │  │ │
│   │  └────┴────┴───┘ │         │   └─────┴─────┴─────┘  │ │
│   │   (registres)    │         │   (adresses mémoire)    │ │
│   └──────────────────┘         └─────────────────────────┘ │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

- **Le CPU**, c'est la puce qui **exécute** les instructions. Une seule à la fois, mais des milliards par seconde.
- **La RAM**, c'est un immense tableau d'octets numérotés. Chaque numéro est une **adresse**. Le code et les données y vivent.
- **Les registres**, ce sont des mini-cases de stockage **à l'intérieur du CPU**. Ultra-rapides, mais peu nombreuses.

### L'analogie à garder en tête

```
RAM         = ta bibliothèque  (grande, mais il faut se lever pour y aller)
Registres   = ton bureau       (petit, mais tout sous la main)
CPU         = toi qui travailles
Instruction = une action que tu fais
```

> **Règle d'or :** en pratique, beaucoup d'opérations passent par les registres, et **une instruction x86-64 ne peut pas manipuler deux zones mémoire en même temps**. Tu peux lire depuis la mémoire (`add rax, [x]`) ou écrire vers la mémoire (`add [x], rax`), mais dès qu'il faut **combiner deux valeurs mémoire**, il faut d'abord en charger une dans un registre.

### Disque dur ≠ RAM ≠ Registres

C'est une confusion classique :

| Stockage | Capacité typique | Vitesse | Volatilité |
|----------|------------------|---------|------------|
| **Disque dur / SSD** | 500 Go - plusieurs To | Lent | Persistant (survit à l'extinction) |
| **RAM** | 8 Go - 64 Go | Rapide | Volatile (vidée à l'extinction) |
| **Registres** | 16 cases × 8 octets = 128 octets | Ultra-rapide | Volatile (vidée à l'extinction) |

Quand tu lances un programme, son fichier passe du **disque** vers la **RAM**. Puis le CPU **charge** des morceaux de la RAM dans ses **registres** pour les manipuler.

### Les principaux registres x86-64

Sur un CPU x86-64 (la grande majorité des PC modernes), il y a 16 registres généraux de 64 bits. Tu n'as pas besoin de tous les retenir tout de suite. Voici ceux qu'on va utiliser :

| Registre | Nom historique | Usage typique |
|----------|----------------|---------------|
| **`rax`** | **A**ccumulator | Résultats de calculs, valeur de retour de fonction |
| **`rbx`** | **B**ase | Variable générale (à préserver) |
| **`rcx`** | **C**ounter | Compteur de boucle |
| **`rdx`** | **D**ata | Données générales, partie haute des résultats |
| **`rsi`** | **S**ource **I**ndex | Adresse source (copies, chaînes) |
| **`rdi`** | **D**estination **I**ndex | Adresse destination, premier argument de fonction |
| **`rsp`** | **S**tack **P**ointer | **Pointeur de pile** (chapitre 18) — n'y touche pas pour l'instant |
| **`rbp`** | **B**ase **P**ointer | **Base de la pile** (chapitre 20) |
| **`r8`** à **`r15`** | (nouveaux en x86-64) | Registres généraux supplémentaires |
| **`rip`** | **I**nstruction **P**ointer | Pointe sur la **prochaine instruction à exécuter** (en debug, c'est celle affichée comme courante). On ne le modifie pas directement |

> **À retenir tout de suite :** `rax`, `rdi`, `rsi`, `rdx`. Ce sont ceux qu'on utilise dès le chapitre 6.

### Les sous-registres : `rax`, `eax`, `ax`, `al`

Chaque registre 64 bits peut être manipulé à différentes tailles. **Ce ne sont pas des registres séparés** : ce sont des **zooms** sur le même registre.

```
   ┌─────────────────────────────────────────────────────────────────┐
   │                          rax (64 bits)                          │
   │                                                                 │
   │                                ┌────────────────────────────────┤
   │                                │       eax (32 bits)            │
   │                                │                  ┌─────────────┤
   │                                │                  │ ax (16 bits)│
   │                                │                  ├──────┬──────┤
   │                                │                  │  ah  │  al  │
   │                                │                  │ (8b) │ (8b) │
   └────────────────────────────────┴──────────────────┴──────┴──────┘
```

| Taille | 64 bits | 32 bits | 16 bits | 8 bits hauts | 8 bits bas |
|--------|---------|---------|---------|--------------|------------|
| Registre A | `rax` | `eax` | `ax` | `ah` | `al` |
| Registre B | `rbx` | `ebx` | `bx` | `bh` | `bl` |
| Registre C | `rcx` | `ecx` | `cx` | `ch` | `cl` |
| Registre D | `rdx` | `edx` | `dx` | `dh` | `dl` |
| Source | `rsi` | `esi` | `si` | — | `sil` |
| Destination | `rdi` | `edi` | `di` | — | `dil` |
| Nouveaux | `r8`-`r15` | `r8d`-`r15d` | `r8w`-`r15w` | — | `r8b`-`r15b` |

> **À retenir :** si tu écris `mov al, 5`, tu modifies seulement les **8 bits bas** de `rax`. Le reste de `rax` n'est pas touché (sauf cas particulier en 32 bits, voir Annexe B).

## Très utile en pratique

### Comment voir les registres ?

Tu ne peux pas voir les registres en regardant ton écran. Il faut un **debugger** comme GDB. C'est exactement ce qu'on apprendra au chapitre 9.

### Combien de registres utilise un vrai programme ?

Un programme C compilé utilise typiquement **5 à 10 registres** différents à un moment donné. Les 16 disponibles suffisent largement pour des calculs. Quand on en a besoin de plus, on **passe par la mémoire** (la pile, plus tard).

### `rip` : le registre que tu ne touches jamais

`rip` (Instruction Pointer) contient l'adresse de la **prochaine instruction** à exécuter. Tu ne le modifies **jamais** directement avec `mov`. Il est modifié par :
- Le simple fait d'exécuter une instruction (`rip` avance automatiquement).
- Les instructions de saut (`jmp`, `je`, `call`, `ret`…) qu'on verra plus tard.

## ❌ Erreur classique

```
Confondre RAM et disque dur
→ Ton programme ne tourne pas depuis le disque, il tourne depuis la RAM.

Croire qu'un registre est une variable Python
→ Une variable Python vit en mémoire (RAM). Un registre vit dans le CPU.

Croire que rax et eax sont des registres différents
→ NON. eax = la moitié basse de rax. Modifier eax modifie aussi rax.

Modifier rip directement
→ Interdit. Utilise jmp, call, ret. Sinon, crash.

Croire qu'on peut faire mov [a], [b] (mémoire à mémoire direct)
→ Interdit en x86-64. Il faut passer par un registre pour combiner
   deux zones mémoire.
```

## Exercices

**Guidé :** Complète ce tableau dans ton cahier :

| Registre 64 bits | Sous-registre 32 bits | Sous-registre 8 bits bas |
|------------------|----------------------|--------------------------|
| `rax` | ? | ? |
| `rcx` | ? | ? |
| `r10` | ? | ? |

**Autonome :** Explique en 3 phrases, avec tes propres mots, la différence entre :
- un registre,
- une case mémoire (RAM),
- un fichier sur disque.

**Défi :** Si je dis `mov al, 0xFF`, quelle est la valeur de `rax` après, **sachant que `rax` valait 0 avant** ? Et si `rax` valait `0x1234567890ABCDEF` avant ?

> **Indice :** `mov al` ne touche que les 8 bits bas. (Réponse au chapitre 7.)

## ✅ Tu sais maintenant…

- Ce qu'est un **CPU**, une **RAM**, un **registre**
- La différence registre / mémoire / disque
- Les **principaux registres** x86-64 (`rax`, `rbx`, `rcx`, `rdx`, `rsi`, `rdi`, `r8`-`r15`, `rsp`, `rbp`, `rip`)
- Les **sous-registres** (`rax`, `eax`, `ax`, `al`)
- Que **les registres sont l'espace de travail principal** du CPU (même si certaines instructions peuvent lire ou modifier directement la mémoire)
- Pourquoi on ne peut pas faire un calcul mémoire-à-mémoire direct

---

# Chapitre 3 — Binaire, hexadécimal, ASCII et tailles de données

## Le minimum à savoir

### Bit et octet

- Un **bit**, c'est la plus petite unité d'information possible : `0` ou `1`.
- Un **octet** (en anglais : *byte*), c'est **8 bits** mis côte à côte.

Un octet peut donc prendre 2⁸ = 256 valeurs différentes, de 0 à 255.

```
   1 octet  =  8 bits
   ┌─┬─┬─┬─┬─┬─┬─┬─┐
   │1│0│1│1│0│1│0│1│   →   en décimal : 181
   └─┴─┴─┴─┴─┴─┴─┴─┘
```

### Binaire (base 2)

Le binaire utilise **seulement 0 et 1**. Chaque position vaut une puissance de 2 :

```
  Position :  7    6    5    4    3    2    1    0
  Valeur   : 128   64   32   16    8    4    2    1
  Bit      :  1    0    1    1    0    1    0    1   →  128+32+16+4+1 = 181
```

En NASM, on écrit le binaire avec le préfixe `0b` : `0b10110101`.

### Hexadécimal (base 16)

L'hexadécimal utilise **16 chiffres** : `0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F`.

| Hexa | Décimal | Binaire |
|------|---------|---------|
| `0` | 0 | `0000` |
| `1` | 1 | `0001` |
| `5` | 5 | `0101` |
| `9` | 9 | `1001` |
| `A` | 10 | `1010` |
| `B` | 11 | `1011` |
| `F` | 15 | `1111` |

En NASM, on écrit l'hexadécimal avec le préfixe `0x` : `0xFF`, `0x41`, `0x100`.

### Pourquoi l'hexadécimal partout en assembleur ?

Parce qu'**un octet = exactement 2 chiffres hexadécimaux**. C'est ultra-pratique.

```
  Binaire     :  1011 0101
  Hexadécimal :    B    5    →   0xB5
  Décimal     :    181
```

GDB, objdump, les dumps mémoire, les adresses : **tout** s'affiche en hexa. Tu vas en voir partout. Apprivoise-le maintenant.

### Conversions de base

#### Hexa → décimal

`0xFF` = 15 × 16 + 15 = 255
`0x10` = 1 × 16 + 0 = **16** (et non 10 !)
`0x100` = 1 × 256 + 0 + 0 = **256**

#### Décimal → hexa

42 = 2 × 16 + 10 → `0x2A`
255 = 15 × 16 + 15 → `0xFF`
1000 = 3 × 256 + 14 × 16 + 8 → `0x3E8`

> **Astuce :** Linux propose `printf "%x\n" 1000` qui te donne directement la conversion.

### Les tailles de données en x86-64

| Nom | Taille | Plage non signée | Exemples |
|-----|--------|------------------|----------|
| **byte** | 8 bits = 1 octet | 0 à 255 | un caractère ASCII |
| **word** | 16 bits = 2 octets | 0 à 65 535 | un petit entier |
| **dword** | 32 bits = 4 octets | 0 à 4 294 967 295 | un entier classique |
| **qword** | 64 bits = 8 octets | 0 à 18 446 744 073 709 551 615 | un long entier, une adresse |

> **À retenir :** sur x86-64, une **adresse mémoire** fait toujours **8 octets (qword)**. C'est pour ça que tous nos pointeurs feront 8 octets.

### ASCII : comment l'ordinateur stocke du texte

Un ordinateur ne sait pas ce qu'est une "lettre". Il ne sait stocker que des nombres. Pour stocker du texte, on utilise une **table de correspondance** : la table ASCII.

Chaque caractère correspond à un nombre de 0 à 127 :

| Caractère | Décimal | Hexa |
|-----------|---------|------|
| `' '` (espace) | 32 | `0x20` |
| `'0'` | 48 | `0x30` |
| `'9'` | 57 | `0x39` |
| `'A'` | 65 | `0x41` |
| `'Z'` | 90 | `0x5A` |
| `'a'` | 97 | `0x61` |
| `'z'` | 122 | `0x7A` |
| `'\n'` (saut de ligne) | 10 | `0x0A` |

**Quelques règles à retenir :**

- Les chiffres `'0'` à `'9'` se suivent : `0x30` à `0x39`.
- Les majuscules `'A'` à `'Z'` se suivent : `0x41` à `0x5A`.
- Les minuscules `'a'` à `'z'` se suivent : `0x61` à `0x7A`.
- Pour passer de majuscule à minuscule : **ajouter 32** (`0x20`).
- Pour transformer le caractère `'5'` en nombre `5` : **soustraire 48** (`0x30`).

> **Important :** Le caractère `'5'` (qui vaut 53 en mémoire) **n'est pas** le nombre 5 ! C'est une confusion classique qu'on revoit au chapitre 14.

## Très utile en pratique

### Lire un dump mémoire

Voici ce que GDB peut t'afficher pour une chaîne en mémoire :

```
0x404000:  48  65  6c  6c  6f  21  0a  00
```

Tu lis : `0x48 = 'H'`, `0x65 = 'e'`, `0x6c = 'l'`, `0x6c = 'l'`, `0x6f = 'o'`, `0x21 = '!'`, `0x0a = '\n'`, `0x00 = '\0'`.

Donc la chaîne en mémoire, c'est `"Hello!\n\0"`.

### Outils Linux pour convertir

```bash
printf "%x\n" 255          # Décimal → hexa  → ff
printf "%d\n" 0xff         # Hexa → décimal  → 255
printf "%d\n" 0b1010       # Binaire → décimal (selon bash)
echo "obase=2; 42" | bc    # Décimal → binaire  → 101010
```

## Bonus

### Aperçu rapide des nombres négatifs (complément à 2)

Comment représenter `-1` avec seulement des 0 et des 1 ? Réponse simple : `-1` (en 8 bits) est représenté par `0xFF` (255 non signé). Le CPU interprète différemment selon le contexte (instruction signée ou non signée). On creuse ça dans l'**Annexe D**. Pour l'instant, retiens que `-1` = `0xFFFFFFFFFFFFFFFF` en 64 bits.

### Little-endian (aperçu)

Quand on stocke un `qword` en mémoire, **les octets de poids faible sont écrits en premier**. C'est ce qu'on appelle **little-endian**. Donc le nombre `0x1234` en mémoire ressemble à `34 12 00 00 00 00 00 00`. Pas intuitif au début ! On en reparle dans l'**Annexe E**.

## ❌ Erreur classique

```
Lire 0x10 comme 10
→ NON. 0x10 = 16. Le préfixe 0x est essentiel.

Confondre bit et octet
→ Un octet = 8 bits. "8 Go" et "8 Gb" ne sont pas la même chose.

Confondre le caractère '5' et le nombre 5
→ '5' = 53 en mémoire. 5 = 5. Ils ne se manipulent pas pareil.

Croire qu'un nombre s'écrit "0F" sans préfixe
→ En NASM, écris 0x0F ou 0Fh. Sans préfixe, c'est ambigu.

Confondre b (binaire NASM) avec le b de bx (registre)
→ 0b1010 (binaire), bx (registre). Le contexte tranche.
```

## Exercices

**Guidé :** Convertis ces valeurs (à la main, puis vérifie avec `printf "%x"`) :

| Décimal | Hexadécimal | Binaire |
|---------|-------------|---------|
| 10 | ? | ? |
| 16 | ? | ? |
| 100 | ? | ? |
| 255 | ? | ? |
| 256 | ? | ? |

**Autonome :** Trouve le code ASCII de chaque lettre de ton prénom, en décimal puis en hexa. Vérifie avec :

```bash
echo -n "A" | xxd       # Affiche 41
```

**Défi :** En mémoire, tu vois la séquence d'octets `48 65 6c 6c 6f`. Quelle est la chaîne ? Et que devient-elle si tu **ajoutes 32** à chaque octet ?

## ✅ Tu sais maintenant…

- Ce qu'est un **bit**, un **octet**, un **word**, un **dword**, un **qword**
- Compter en **binaire**, en **décimal** et en **hexadécimal**
- Convertir entre les trois bases
- Pourquoi l'**hexadécimal** est partout en assembleur
- Le lien entre un **caractère** et son **code ASCII**
- Pourquoi `'5'` ≠ `5`
- (Aperçu) que les nombres négatifs et le little-endian seront vus en annexe

---


# PARTIE II — INSTALLER, ÉCRIRE, EXÉCUTER

---

# Chapitre 4 — Environnement de travail et premier programme

## Le minimum à savoir

### Ce qu'il te faut

Pour suivre ce cours, tu as besoin de **Linux**. Trois options :

1. **Linux natif** (Ubuntu, Debian, Fedora…). Idéal.
2. **WSL2 sous Windows** (recommandé Windows 10/11). Suis [https://learn.microsoft.com/windows/wsl/install](https://learn.microsoft.com/windows/wsl/install) puis installe Ubuntu.
3. **Machine virtuelle** (VirtualBox, VMware…) avec Ubuntu/Debian. Fonctionne très bien.

> **Note :** macOS n'est pas un bon choix pour ce cours. Les syscalls sont différents, l'ABI est différente, GDB est limité. Si tu es sur Mac, utilise une VM Linux.

### Les outils à installer

Sur Ubuntu/Debian, ouvre un terminal et tape :

```bash
sudo apt update
sudo apt install nasm binutils gcc gdb make
```

| Outil | À quoi ça sert |
|-------|----------------|
| **`nasm`** | L'assembleur : transforme ton `.asm` en `.o` (fichier objet) |
| **`binutils`** | Inclut `ld` (le linker) et `objdump` (qu'on verra plus tard) |
| **`gcc`** | Le compilateur C (qu'on utilisera comme linker plus tard) |
| **`gdb`** | Le debugger |
| **`make`** | L'outil de compilation automatisée |

Vérifie que tout est là :

```bash
nasm --version
ld --version
gcc --version
gdb --version
```

### (Recommandé) Installer pwndbg pour un GDB plus lisible

GDB par défaut, c'est austère. Avec **pwndbg**, c'est nettement plus pédagogique (registres affichés automatiquement, pile visible, etc.).

```bash
cd ~
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh
```

> **Alternative :** `gef` (https://github.com/hugsy/gef) fait à peu près la même chose. Choisis l'un OU l'autre.

### La chaîne de compilation : du `.asm` au programme

```
   mon_prog.asm        ───nasm──→   mon_prog.o     ───ld──→   mon_prog
   (ton code)                       (fichier               (programme
                                     objet)                 exécutable)
```

- **NASM** lit ton fichier source (`.asm`) et le transforme en **fichier objet** (`.o`). Ce fichier contient du code machine **mais n'est pas exécutable** : il manque les "branchements" finaux.
- **`ld`** (le linker) prend le `.o` et en fait un vrai **exécutable** que tu peux lancer.

### Ton premier programme : `exit.asm`

On ne commence **pas** par "Hello World" (trop d'éléments d'un coup). On commence par le programme le plus simple possible : un programme qui **ne fait rien**, sauf se terminer proprement avec un code de retour.

Crée un fichier `exit.asm` :

```nasm
; exit.asm — un programme qui se termine avec le code de retour 42

section .text
global _start

_start:
    mov rax, 60     ; numéro du syscall "exit"
    mov rdi, 42     ; code de retour
    syscall         ; demande au noyau de terminer le programme
```

### Assembler, linker, exécuter

Dans le terminal, tape **dans l'ordre** :

```bash
nasm -f elf64 exit.asm -o exit.o   # 1. assembler → exit.o
ld exit.o -o exit                   # 2. linker    → exit (exécutable)
./exit                              # 3. exécuter
echo $?                             # 4. afficher le code de retour
```

Si tout va bien, l'étape 4 affiche `42`.

**Explication ligne par ligne du `.asm` :**

- `; …` : commentaire (Bash : `#`, Python : `#`, NASM : `;`).
- `section .text` : section du **code exécutable**.
- `global _start` : on dit au linker que l'étiquette `_start` est visible de l'extérieur. C'est le **point d'entrée** par défaut sous Linux.
- `_start:` : l'étiquette du point d'entrée. Quand on lance le programme, le CPU commence ici.
- `mov rax, 60` : on met **60** dans `rax`. C'est le numéro du syscall **exit** sous Linux x86-64.
- `mov rdi, 42` : on met **42** dans `rdi`. C'est l'argument du syscall (le code de retour qu'on veut).
- `syscall` : on **appelle le noyau**. Il regarde `rax` pour savoir quel service demander.

> **Promesse :** tu n'as pas besoin de tout comprendre maintenant. À la fin du chapitre 6, ces lignes seront limpides.

## Très utile en pratique

### Un Makefile minimal

Pour ne pas retaper les commandes à chaque fois, crée un fichier `Makefile` (sans extension, et **avec une tabulation** devant les commandes, pas des espaces) :

```makefile
# Makefile générique pour ce cours

NASM = nasm
LD = ld
NASMFLAGS = -f elf64 -g -F dwarf

%.o: %.asm
	$(NASM) $(NASMFLAGS) $< -o $@

%: %.o
	$(LD) $< -o $@

clean:
	rm -f *.o
```

Maintenant, pour compiler `exit.asm`, tape juste :

```bash
make exit
./exit
```

### Le drapeau `-g -F dwarf` : indispensable pour GDB

Sans `-g -F dwarf`, GDB peut afficher le code mais ne sait pas relier les instructions à ton fichier source. **Toujours compiler avec ces options en mode pédagogique.**

## ❌ Erreur classique

```
Essayer d'exécuter le .o au lieu de l'exécutable
→ ./exit.o ne marche pas. Il faut linker d'abord.

Oublier "global _start"
→ Erreur du linker : "undefined reference to _start".

Mettre _start dans une mauvaise section
→ _start doit être dans .text, sinon erreur.

Tabulations vs espaces dans le Makefile
→ Make exige des tabulations. Pas d'espaces. Sinon "missing separator".

Confondre les étapes : nasm = assembler, ld = linker
→ Les deux sont nécessaires, dans cet ordre.

Vouloir faire "syscall" sans avoir mis le numéro dans rax
→ Le syscall ne sait pas quoi faire. Tu vas crasher ou faire n'importe quoi.
```

## Exercices

**Guidé :** Crée `exit.asm` comme ci-dessus. Compile-le, exécute-le, et vérifie que `echo $?` affiche bien 42.

**Autonome :** Modifie le programme pour qu'il retourne **123** au lieu de 42. Recompile, relance, vérifie.

**Défi :** Que se passe-t-il si tu mets `255` ? Et `256` ? Et `1000` ? **Indice :** le code de retour Unix est limité à 8 bits non signés (0-255). Au-delà, il "boucle".

## ✅ Tu sais maintenant…

- Installer **NASM, ld, gcc, GDB**
- (Optionnellement) installer **pwndbg**
- La chaîne : `.asm → .o → exécutable`
- Écrire un programme minimal avec `section .text`, `global _start`, `_start:` et `syscall`
- Utiliser **`nasm -f elf64`** et **`ld`** pour compiler
- Récupérer le code de retour avec **`echo $?`**
- Écrire un **Makefile** simple pour automatiser

---

# Chapitre 5 — Anatomie d'un fichier `.asm`

## Le minimum à savoir

### La structure d'un fichier NASM

Un fichier `.asm` est divisé en **sections**. Chaque section a un rôle précis :

```nasm
section .data       ; ← données initialisées (variables avec une valeur)
    ; ...

section .bss        ; ← données réservées non initialisées
    ; ...

section .text       ; ← le code exécutable
global _start
_start:
    ; ...
```

| Section | Rôle | Analogie |
|---------|------|----------|
| **`.text`** | Le code exécutable (les instructions) | Les **recettes** de cuisine |
| **`.data`** | Données initialisées (variables avec une valeur) | Les **ingrédients** déjà préparés |
| **`.bss`** | Espace réservé non initialisé (buffers vides) | Les **bols vides** pour plus tard |
| **`.rodata`** | Données en **lecture seule** (constantes) — optionnel | Les **étiquettes** sur les pots |

> **À retenir :** `.text` est obligatoire (sinon il n'y a pas de code). `.data` et `.bss` sont optionnels.

### Les labels (étiquettes)

Un **label** est un nom que tu donnes à un endroit du fichier (un emplacement de code OU une variable). Tu utilises ensuite ce nom au lieu d'une adresse.

```nasm
section .data
    age db 25              ; "age" est un label pointant vers un octet de valeur 25
    nom db "Alice", 0      ; "nom" est un label pointant vers la chaîne "Alice\0"

section .text
global _start
_start:                    ; "_start" est un label pointant vers le début du code
    mov al, [age]          ; on utilise le label "age"
    ; ...
boucle:                    ; un label dans le code pour les sauts
    ; ...
```

> **Règle :** un label se termine par `:` quand on le **définit**. Quand on l'**utilise**, pas de `:`.

### Les directives de données

Dans la section `.data`, on déclare des variables avec des **directives** :

| Directive | Taille | Usage |
|-----------|--------|-------|
| **`db`** | **b**yte (1 octet) | `nom db "Alice", 0` |
| **`dw`** | **w**ord (2 octets) | `pixel dw 0x1234` |
| **`dd`** | **d**ouble word (4 octets) | `version dd 12` |
| **`dq`** | **q**uad word (8 octets) | `gros dq 1234567890` |

Dans la section `.bss`, on **réserve** sans initialiser :

| Directive | Taille | Usage |
|-----------|--------|-------|
| **`resb N`** | N octets | `buffer resb 64` (réserve 64 octets) |
| **`resw N`** | N × 2 octets | `tab resw 10` |
| **`resd N`** | N × 4 octets | `tab resd 10` |
| **`resq N`** | N × 8 octets | `tab resq 10` |

Et pour les **constantes** (pas en mémoire, juste un nom pour une valeur fixe) :

```nasm
section .data
    msg db "Bonjour", 10
    LEN equ $ - msg        ; equ = "égal" : LEN devient une constante
```

> **`$` en NASM** = "l'adresse actuelle, ici, à cet endroit". Donc `$ - msg` = "la longueur entre `msg` et maintenant". Astuce pratique pour calculer une longueur de chaîne.

### La syntaxe Intel : destination à gauche, source à droite

NASM utilise la **syntaxe Intel**, qui est la plus lisible :

```nasm
mov rax, 5         ; rax = 5    (destination = source)
add rax, rbx       ; rax = rax + rbx
mov [var], rax     ; var en mémoire = rax
```

Le **premier opérande** est la **destination**, le **second** est la **source**. C'est comme `x = 5` en Python : ce qui reçoit est à gauche.

> **Note :** la syntaxe AT&T (utilisée par défaut dans GDB et `objdump`) inverse cet ordre. On la verra **en lecture uniquement** dans l'Annexe A. Pour ce cours, on reste à 100 % en Intel.

### Les commentaires

NASM utilise `;` pour les commentaires (comme Bash utilise `#`) :

```nasm
mov rax, 1     ; ceci est un commentaire de fin de ligne
; ceci est un commentaire pleine ligne
```

> **Conseil pédagogique :** commente **chaque ligne** au début. Ça force à expliquer ce que tu fais, et c'est la meilleure façon d'apprendre.

## Très utile en pratique

### Exemple complet annoté

Voici un fichier `.asm` minimal qui contient les trois sections et plusieurs déclarations :

```nasm
; structure.asm — Démonstration de la structure d'un fichier NASM

; ─────────── SECTION DATA : variables initialisées ───────────
section .data
    nb_petit    db  42                  ; 1 octet  : 42
    nb_moyen    dw  1000                ; 2 octets : 1000
    nb_grand    dd  100000              ; 4 octets : 100000
    nb_enorme   dq  1234567890123       ; 8 octets : très grand
    message     db  "Bonjour", 0        ; chaîne terminée par 0
    LEN_MSG     equ $ - message         ; longueur de "message" (constante)

; ─────────── SECTION BSS : variables non initialisées ───────────
section .bss
    buffer      resb 64                 ; 64 octets réservés (vides)
    tab_int     resq 10                 ; 10 qword (80 octets) réservés

; ─────────── SECTION TEXT : le code ───────────
section .text
global _start

_start:
    ; ... ici on mettra des instructions au prochain chapitre ...

    ; pour l'instant, on quitte proprement
    mov rax, 60     ; syscall exit
    mov rdi, 0      ; code de retour 0
    syscall
```

Compile et exécute :

```bash
nasm -f elf64 structure.asm -o structure.o
ld structure.o -o structure
./structure
echo $?           # → 0
```

### Récapitulatif visuel

```
   ┌─────────────────────────────────────────────────────────┐
   │                FICHIER .asm                             │
   ├─────────────────────────────────────────────────────────┤
   │                                                         │
   │   section .data    ← variables initialisées             │
   │     var1 db 5                                           │
   │     msg  db "Hi", 0                                     │
   │                                                         │
   │   section .bss     ← buffers vides                      │
   │     buf  resb 64                                        │
   │                                                         │
   │   section .text    ← code                               │
   │   global _start                                         │
   │   _start:                                               │
   │     ; instructions                                      │
   │                                                         │
   └─────────────────────────────────────────────────────────┘
```

## Bonus

### Le label `_start` et `main`

Sous Linux, le point d'entrée par défaut pour `ld` est `_start`. Quand on linke avec `gcc`, le point d'entrée devient `main` (parce que gcc fournit un `_start` qui appelle `main`). On reverra ça au chapitre 21.

### Pourquoi `.bss` plutôt que `.data` pour les buffers ?

Si tu déclares 1 Mo de buffer dans `.data`, **ton exécutable fera 1 Mo** (la valeur initiale est stockée dans le fichier). Si tu le déclares dans `.bss`, **le fichier reste minuscule** (le système réserve l'espace au lancement). Pour des buffers vides, toujours `.bss`.

## ❌ Erreur classique

```
Confondre db (data byte) et resb (reserve byte)
→ db : initialisé.    resb : réservé non initialisé.

Oublier les deux-points après un label
→ "_start" est traité comme une instruction → erreur.

Confondre une instruction et une directive
→ mov est une instruction (exécutée par le CPU).
→ db est une directive (gérée par NASM avant exécution).

Inverser destination et source
→ mov 5, rax  est faux. C'est mov rax, 5.

Mettre du code dans .data
→ NON. Le code va dans .text uniquement.

Oublier le 0 final d'une chaîne pour la libc
→ Pour les syscalls Linux, pas obligatoire (on donne la longueur).
→ Pour printf et autres fonctions C, OBLIGATOIRE.
```

## Exercices

**Guidé :** Crée `decla.asm` avec :
- une variable `age` de type byte initialisée à 25
- une variable `annee` de type dword initialisée à 2024
- une variable `nom` de type chaîne contenant "Bob" + un 0
- un buffer `buf` de 32 octets dans `.bss`
- un `_start` qui ne fait que quitter avec code 0

Compile-le et exécute-le. Ça doit afficher rien et `echo $?` doit donner `0`.

**Autonome :** Écris un fichier `.asm` qui contient :
- 5 constantes (avec `equ`) : `PI`, `E`, `MAX`, `MIN`, `ZERO` avec des valeurs au choix.
- 5 variables initialisées (utilisant `db`, `dw`, `dd`, `dq`).
- Un `_start` qui quitte avec le code de retour 7.

Vérifie que tout compile sans erreur.

**Défi :** Que vaut `LEN` ici, à ton avis (sans exécuter) ?

```nasm
section .data
    msg db "Hello!", 10, 0
    LEN equ $ - msg
```

> **Indice :** compte les octets. `"Hello!"` = 6 caractères + 1 retour ligne + 1 zéro = ?

## ✅ Tu sais maintenant…

- Les sections **`.text`**, **`.data`**, **`.bss`**
- Les directives de données **`db`, `dw`, `dd`, `dq`**
- Les directives de réservation **`resb`, `resw`, `resd`, `resq`**
- Les **constantes** avec `equ`
- Les **labels** et leur syntaxe (`:` à la définition)
- La **syntaxe Intel** : `instruction destination, source`
- Comment **commenter** avec `;`
- La règle `$ - label` pour calculer une longueur

---

# Chapitre 6 — Premier affichage avec `write`

## Le minimum à savoir

### Pourquoi il n'y a pas de `print()` en assembleur

En Python, `print("Bonjour")` semble magique. En réalité, sous le capot, Python finit par appeler une **fonction du système** qui écrit dans le terminal. Cette fonction s'appelle **`write`** sous Linux, et c'est un **syscall**.

> **À retenir :** en assembleur, on ne fait pas un `print` magique. On **demande directement au noyau** d'écrire pour nous. Cette demande s'appelle un **syscall** (system call).

### Qu'est-ce qu'un syscall ?

Un syscall, c'est une **demande de service au noyau** : "Noyau, je voudrais écrire ce texte sur l'écran", "ouvre-moi ce fichier", "donne-moi l'heure", etc.

**Analogie :** tu es au restaurant. Tu ne vas pas en cuisine — tu **commandes au serveur**. Le serveur (le noyau) va chercher ton plat (le service) et te le ramène. C'est exactement le rôle d'un syscall.

### La convention de syscall Linux x86-64

Sous Linux x86-64, pour faire un syscall, il faut **toujours** :

1. Mettre le **numéro du syscall** dans `rax`.
2. Mettre les **arguments** dans `rdi`, `rsi`, `rdx`, `r10`, `r8`, `r9` (dans cet ordre).
3. Exécuter l'instruction `syscall`.
4. Le **résultat** revient dans `rax`.

```
   ┌─────────────────────────────────────────────┐
   │   AVANT le syscall                          │
   │   ─────────────                             │
   │   rax = numéro du syscall                   │
   │   rdi = 1er argument                        │
   │   rsi = 2ème argument                       │
   │   rdx = 3ème argument                       │
   │   r10 = 4ème argument                       │
   │   r8  = 5ème argument                       │
   │   r9  = 6ème argument                       │
   │                                             │
   │   syscall                                   │
   │                                             │
   │   APRÈS le syscall                          │
   │   ──────────────                            │
   │   rax = valeur de retour                    │
   └─────────────────────────────────────────────┘
```

> **À retenir tout de suite :** `rax` = numéro, `rdi` = arg 1, `rsi` = arg 2, `rdx` = arg 3. **Toujours dans cet ordre.**

> **⚠️ Effet de bord important :** l'instruction `syscall` **détruit toujours** les registres `rcx` et `r11` (le CPU s'en sert pour mémoriser l'adresse de retour et les flags). Si tu utilises `rcx` ou `r11` autour d'un syscall, **tu dois les sauvegarder** :
> ```nasm
>     push rcx          ; sauvegarder
>     mov rax, 1
>     mov rdi, 1
>     mov rsi, msg
>     mov rdx, len
>     syscall           ; rcx et r11 sont écrasés ici
>     pop rcx           ; restaurer
> ```
> Tu verras ce pattern partout dans le cours, notamment au chapitre 17 (boucles).

### Le syscall `write` (numéro 1)

Le syscall **`write`** prend **3 arguments** :

1. **`rdi`** : le file descriptor (où écrire). `1` = sortie standard (le terminal).
2. **`rsi`** : l'adresse du début du texte à écrire.
3. **`rdx`** : le nombre d'octets à écrire.

| Argument | Registre | Exemple |
|----------|----------|---------|
| numéro de syscall | `rax` | `1` (= write) |
| file descriptor | `rdi` | `1` (= stdout) |
| adresse du buffer | `rsi` | `msg` (étiquette) |
| longueur en octets | `rdx` | `len` (constante) |

### Le syscall `exit` (numéro 60)

Pour **terminer proprement** un programme :

1. **`rax`** : `60` (numéro de `exit`).
2. **`rdi`** : le code de retour (0 = succès).

Sans `exit` à la fin, **ton programme va crasher** (le CPU continuerait à exécuter ce qu'il y a après, qui n'est pas du code valide).

### Ton premier "Hello, World!"

Crée `hello.asm` :

```nasm
; hello.asm — Premier programme qui affiche un message

section .data
    msg db "Bonjour Assembleur !", 10   ; le texte + retour ligne (10 = '\n')
    len equ $ - msg                      ; longueur calculée automatiquement

section .text
global _start

_start:
    ; ─── Appel write(1, msg, len) ───
    mov rax, 1          ; syscall write
    mov rdi, 1          ; file descriptor = stdout
    mov rsi, msg        ; adresse du message
    mov rdx, len        ; longueur
    syscall             ; demande au noyau d'écrire

    ; ─── Appel exit(0) ───
    mov rax, 60         ; syscall exit
    mov rdi, 0          ; code de retour 0
    syscall
```

Compile et exécute :

```bash
nasm -f elf64 hello.asm -o hello.o
ld hello.o -o hello
./hello
```

Sortie :

```
Bonjour Assembleur !
```

🎉 **Bravo. Tu viens d'écrire ton premier programme assembleur.**

## Très utile en pratique

### Pourquoi le `10` dans le message ?

`10` est le code ASCII du **retour ligne** (`\n`). Sans lui, ton message s'affiche, et le prompt du shell apparaît collé sur la même ligne. Tu peux d'ailleurs tester sans, pour voir.

### Pourquoi `len` plutôt que de compter à la main ?

Tu pourrais écrire `mov rdx, 21` à la main (en comptant les caractères). Mais :
- C'est fragile (si tu modifies le message, tu dois recompter).
- C'est source d'erreurs.
- `equ $ - msg` le calcule pour toi à la compilation.

### Les 4 file descriptors essentiels

| FD | Nom | Direction |
|----|-----|-----------|
| `0` | **stdin** | Entrée (clavier) |
| `1` | **stdout** | Sortie standard (écran) |
| `2` | **stderr** | Sortie d'erreur (écran aussi) |
| 3+ | fichiers ouverts | Fichiers que tu as toi-même ouverts |

Pour écrire un message d'erreur, on utilise `rdi = 2` au lieu de `rdi = 1`.

### Afficher plusieurs messages

Il suffit de répéter le pattern :

```nasm
section .data
    msg1 db "Premier message", 10
    len1 equ $ - msg1
    msg2 db "Deuxieme message", 10
    len2 equ $ - msg2

section .text
global _start

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, msg1
    mov rdx, len1
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, msg2
    mov rdx, len2
    syscall

    mov rax, 60
    mov rdi, 0
    syscall
```

> **Remarque :** c'est répétitif. Au chapitre 19, on transformera ce pattern en **fonction réutilisable**.

## Bonus

### Trouver les numéros de syscall

Sous Linux x86-64, la liste des syscalls est dans :

```bash
# Le chemin peut varier selon la distribution. Essaye dans l'ordre :
cat /usr/include/x86_64-linux-gnu/asm/unistd_64.h   # Ubuntu/Debian récents
cat /usr/include/asm/unistd_64.h                     # certaines distributions
# Ou plus directement :
grep __NR_write /usr/include/x86_64-linux-gnu/asm/unistd_64.h
man 2 syscalls
```

Voici les plus courants (à retenir progressivement) :

| Numéro | Nom | Description |
|--------|-----|-------------|
| 0 | `read` | Lire des octets |
| 1 | `write` | Écrire des octets |
| 2 | `open` | Ouvrir un fichier |
| 3 | `close` | Fermer un fichier |
| 8 | `lseek` | Se déplacer dans un fichier |
| 60 | `exit` | Quitter |

### Différence syscall vs fonction C

Plus tard (chapitre 21), tu utiliseras `printf` au lieu de `write`. Ce sont **deux choses différentes** :
- `write` est un **syscall** : demande directe au noyau.
- `printf` est une **fonction de la libc** : elle formate du texte, puis appelle `write`.

Pour l'instant, on reste sur `write` : c'est plus simple, plus bas niveau, et plus instructif.

## ❌ Erreur classique

```
Oublier de mettre rax = 1 avant write
→ Tu fais un syscall avec un mauvais numéro. Comportement indéterminé.

Oublier rdx (la longueur)
→ Le noyau ne sait pas combien d'octets écrire. Affichage corrompu ou rien.

Confondre msg et [msg]
→ Pour write, on veut l'ADRESSE du message, donc msg (sans crochets).
→ [msg] = la valeur stockée à cette adresse (le premier octet = 'B' = 66).

Oublier le retour ligne dans le message
→ Le prompt du shell s'affiche collé. Pas grave, mais moche.

Oublier le syscall exit final
→ Le programme va crasher (Segmentation fault).

Confondre fd 1 (stdout) et fd 2 (stderr)
→ stderr est utilisé pour les messages d'erreur.
```

## Exercices

**Guidé :** Crée `hello.asm` comme ci-dessus. Compile, exécute. Modifie ensuite le message et la longueur (mais utilise `equ $ - msg`, ne compte pas à la main).

**Autonome :** Crée un programme `info.asm` qui affiche **3 lignes successives** :

```
Nom    : Alice
Age    : 30
Metier : Developpeur
```

Utilise 3 syscalls `write` à la suite. Pas de boucle (on n'en a pas encore vu).

**Défi :** Crée un programme qui affiche le **même message sur stdout ET sur stderr**. Teste avec :

```bash
./monprog              # affiche tout
./monprog 2>/dev/null  # stderr supprimé → ne reste que stdout
./monprog 1>/dev/null  # stdout supprimé → ne reste que stderr
```

## 🧩 Mini-projet (chapitres 4-6) — Bannière

Crée un programme `banniere.asm` qui affiche cette bannière à l'écran :

```
==========================================
       BIENVENUE EN ASSEMBLEUR
       x86-64 sous Linux
==========================================
```

Chaque ligne est un message séparé, affiché avec un syscall `write` distinct. Le programme se termine avec `exit(0)`.

> **Bonus :** ajoute une ligne d'espacement au début et à la fin de la bannière.

## ✅ Tu sais maintenant…

- Ce qu'est un **syscall** et pourquoi il existe
- La **convention syscall** Linux x86-64 (`rax`, `rdi`, `rsi`, `rdx`, …)
- Utiliser **`write`** (n°1) pour afficher du texte
- Utiliser **`exit`** (n°60) pour quitter
- La différence **`msg`** (adresse) vs **`[msg]`** (contenu)
- Les file descriptors **0, 1, 2**
- Écrire ton premier programme **réellement utile**

---


# PARTIE III — REGISTRES, CALCULS ET OBSERVATION

---

# Chapitre 7 — Déplacer des données avec `mov`

## Le minimum à savoir

### L'instruction la plus importante de l'assembleur

`mov` est l'instruction que tu vas écrire **le plus souvent**. Elle sert à **copier** une valeur d'un endroit à un autre.

> **Attention au nom !** `mov` vient de "move", mais en réalité, **c'est une copie, pas un déplacement**. La source garde sa valeur. C'est trompeur, mais c'est comme ça historiquement.

### Les 4 formes de `mov`

| Forme | Exemple | Ce que ça fait |
|-------|---------|----------------|
| immédiate → registre | `mov rax, 42` | `rax = 42` |
| registre → registre | `mov rax, rbx` | `rax = rbx` (rbx inchangé) |
| mémoire → registre | `mov rax, [var]` | `rax = contenu à l'adresse var` |
| registre → mémoire | `mov [var], rax` | `var en mémoire = rax` |

### La règle qui te suivra partout : pas de mémoire → mémoire (avec `mov`)

**Tu ne peux PAS faire :**

```nasm
mov [a], [b]     ; ❌ INTERDIT
```

Cette instruction n'existe pas en x86-64. Il **faut toujours passer par un registre** :

```nasm
mov rax, [b]     ; charger b dans rax
mov [a], rax     ; ranger rax dans a
```

> **Règle pédagogique :** pour les instructions courantes (`mov`, `add`, `cmp`, `sub`, …), tu **ne peux pas** manipuler **deux opérandes mémoire explicites** en même temps.
>
> **Nuance :** il existe des instructions spécialisées de **copie mémoire-à-mémoire** comme `movsb`, `movsq`, `rep movsb` qui passent par des registres **implicites** (`rsi`, `rdi`, `rcx`). Tu les croiseras en reverse (souvent dans `memcpy` ou `strcpy` optimisés), mais on ne les utilisera pas dans ce cours.

### Choisir la bonne taille

`mov` ne sait pas tout seul si tu veux copier 1, 2, 4 ou 8 octets. Tu lui dis avec la **taille du registre** :

```nasm
mov rax, 5       ; 8 octets (qword)
mov eax, 5       ; 4 octets (dword)
mov ax,  5       ; 2 octets (word)
mov al,  5       ; 1 octet  (byte)
```

Pour la mémoire sans registre, tu dois préciser :

```nasm
mov byte  [var], 5     ; 1 octet
mov word  [var], 5     ; 2 octets
mov dword [var], 5     ; 4 octets
mov qword [var], 5     ; 8 octets
```

Sinon NASM se plaint : *"operation size not specified"*.

### `mov rax, var` vs `mov rax, [var]`

C'est **la** confusion classique du débutant. Lis attentivement :

```nasm
section .data
    var dq 42

section .text
    mov rax, var      ; rax = ADRESSE de var (un nombre genre 0x404000)
    mov rax, [var]    ; rax = CONTENU à cette adresse  → rax = 42
```

Les crochets `[…]` veulent dire **"le contenu à l'adresse"**. Sans crochets, on a juste l'**adresse**.

## Très utile en pratique

### Exemple détaillé avec plusieurs mov

```nasm
; mov_demo.asm — Démonstration des différentes formes de mov

section .data
    valeur dq 100

section .text
global _start

_start:
    mov rax, 42         ; rax = 42  (immédiate)
    mov rbx, rax        ; rbx = 42  (registre → registre)
    mov rcx, [valeur]   ; rcx = 100 (mémoire → registre)
    mov [valeur], rax   ; valeur en mémoire = 42 (registre → mémoire)
    mov rdx, valeur     ; rdx = adresse de valeur (un grand nombre)

    ; quitter
    mov rax, 60
    mov rdi, 0
    syscall
```

Tu ne **vois rien** quand tu exécutes ce programme. **C'est normal.** Au chapitre 9, on l'observera dans GDB pour voir tous les registres bouger.

### Les sous-registres en pratique

Reprends l'exemple du chapitre 2 :

```nasm
mov rax, 0                  ; rax = 0
mov al, 0xFF                ; al = 0xFF, donc rax = 0x00000000000000FF
```

Mais **attention** à un comportement piège en x86-64 :

```nasm
mov rax, 0x1234567890ABCDEF
mov eax, 5                  ; rax = 0x0000000000000005 (la partie haute est ZÉRO !)
```

> **Règle x86-64 :** écrire dans la version **32 bits** (`eax`, `ebx`, etc.) **efface automatiquement les 32 bits supérieurs**. Écrire dans les versions 8 et 16 bits, par contre, n'efface rien. C'est un piège.

## Bonus

### Réponse au défi du chapitre 2

Si `rax` valait `0x1234567890ABCDEF` et qu'on fait `mov al, 0xFF`, alors `rax` devient `0x1234567890ABCDFF`. Seuls les 8 bits bas changent.

### `mov` ne change jamais les flags

À l'inverse de `add` ou `sub`, l'instruction `mov` **ne modifie pas les flags du CPU**. On peut donc enchaîner plusieurs `mov` sans perdre l'état d'une comparaison faite avant. On reverra ça au chapitre 16.

## ❌ Erreur classique

```
Croire que mov "déplace" la source
→ Faux. mov COPIE. La source garde sa valeur.

Faire mov [a], [b]
→ Interdit en x86-64. Passe par un registre.

Oublier les crochets : mov rax, var au lieu de mov rax, [var]
→ Tu charges l'ADRESSE au lieu du CONTENU.

Ne pas spécifier la taille pour la mémoire
→ NASM crie : "operation size not specified".

Mélanger les tailles : mov rax, eax
→ Inconsistant. NASM crie : "mismatch in operand sizes".

Oublier que mov eax, 0 efface aussi les 32 bits hauts de rax
→ Piège classique. mov al, 0 ne fait pas pareil.
```

## Exercices

**Guidé :** Recopie et compile cet exemple. Tu n'auras pas de sortie visible (normal) :

```nasm
section .data
    a dq 10
    b dq 20

section .text
global _start
_start:
    mov rax, [a]
    mov rbx, [b]
    mov rcx, rax
    mov rdx, rbx
    mov rax, 60
    mov rdi, 0
    syscall
```

**Autonome :** Sans exécuter, **prédis sur papier** la valeur de `rax`, `rbx`, `rcx` après chaque ligne :

```nasm
mov rax, 100
mov rbx, 200
mov rcx, rax
mov rax, rbx
mov rbx, rcx
```

> **Question :** qu'est-ce que ce code vient de faire ? (Réponse en bas.)

**Défi :** Réécris ces lignes en assembleur :
- Python : `x = 5`, `y = 10`, `z = x`
- Suppose que `x`, `y`, `z` sont déclarés en `.data` avec `dq 0`.

> **Réponse autonome :** ce code **échange `rax` et `rbx`** (swap). C'est un pattern classique.

## ✅ Tu sais maintenant…

- Les **4 formes de `mov`** (immédiate, registre, mémoire, ou inverse)
- La règle d'or : **pas de mémoire → mémoire directe**
- La différence cruciale **`var`** (adresse) vs **`[var]`** (contenu)
- Comment **choisir la taille** (`rax`, `eax`, `al`, ou `byte/word/dword/qword`)
- Le **piège du 32 bits** qui efface les bits hauts
- Faire un **swap** entre deux registres

---

# Chapitre 8 — Calculer avec les registres

## Le minimum à savoir

### L'arithmétique de base

L'assembleur sait faire les 4 opérations classiques, plus quelques instructions utiles :

| Instruction | Effet | Exemple |
|-------------|-------|---------|
| **`add`** | addition | `add rax, rbx` → `rax = rax + rbx` |
| **`sub`** | soustraction | `sub rax, rbx` → `rax = rax - rbx` |
| **`inc`** | incrémenter de 1 | `inc rax` → `rax = rax + 1` |
| **`dec`** | décrémenter de 1 | `dec rax` → `rax = rax - 1` |
| **`neg`** | négation (opposé) | `neg rax` → `rax = -rax` |
| **`imul`** | multiplication signée | `imul rax, rbx` → `rax = rax * rbx` |

> **Format identique à `mov` :** destination à gauche, source à droite. La destination reçoit le résultat.

### Exemple complet

```nasm
section .text
global _start
_start:
    mov rax, 10
    mov rbx, 3
    add rax, rbx       ; rax = 10 + 3 = 13
    sub rax, 5         ; rax = 13 - 5 = 8
    inc rax            ; rax = 9
    dec rax            ; rax = 8
    imul rax, rbx      ; rax = 8 * 3 = 24
    neg rax            ; rax = -24

    ; on sort avec rax en code de retour (cf. ci-dessous)
    mov rdi, rax       ; copie le résultat dans rdi
    mov rax, 60        ; syscall exit
    syscall
```

> **Astuce pédagogique :** comme on ne sait pas encore afficher un nombre proprement (il faut le convertir en texte, ch. 14), on **utilise le code de retour comme canal de sortie** pour vérifier nos calculs.

Compile, exécute, regarde :

```bash
make calcul
./calcul
echo $?              # → 232  (parce que -24 en non signé sur 8 bits = 232)
```

Le code de retour est limité à 0-255 (8 bits non signés). Pour des résultats simples, ça suffit largement.

### La multiplication : `imul`

```nasm
mov rax, 6
mov rbx, 7
imul rax, rbx        ; rax = 42
```

Tu peux aussi faire :

```nasm
imul rax, rbx, 5     ; rax = rbx * 5  (trois opérandes !)
imul rax, 3          ; rax = rax * 3
```

> **`imul` vs `mul` :** `imul` est la multiplication **signée** (qui gère les nombres négatifs correctement). `mul` est la version non signée, à 1 opérande, et plus pénible. **Utilise `imul` par défaut.**

### La division : `idiv` (prudemment)

`idiv` est plus tordue. Elle divise un nombre **128 bits** (formé par `rdx:rax`) par son opérande.

```nasm
mov rax, 100
mov rdx, 0          ; ESSENTIEL pour des nombres POSITIFS : partie haute à 0
mov rbx, 7
idiv rbx            ; rax = 100 / 7 = 14, rdx = 100 % 7 = 2
```

**Avant un `idiv`, il faut préparer `rdx` :**

- Pour un dividende **positif** (le cas habituel en pédagogie) : `mov rdx, 0` ou `xor rdx, rdx`.
- Pour un dividende **signé** qui peut être négatif : utilise **`cqo`**. Cette instruction étend le bit de signe de `rax` dans `rdx` (donc `rdx` devient `0` si `rax > 0`, ou `0xFFFFFFFFFFFFFFFF` si `rax < 0`).

```nasm
mov rax, -100
cqo                 ; rdx = 0xFFFFFFFFFFFFFFFF (extension du signe)
mov rbx, 7
idiv rbx            ; rax = -100 / 7 = -14, rdx = -2
```

> **Piège classique :** si tu mets `rdx = 0` alors que `rax` est négatif, le CPU interprète `rdx:rax` comme un énorme nombre positif. Résultat erroné garanti. **Avec `idiv` et des négatifs, toujours `cqo`.**

| Après `idiv` | Contenu |
|--------------|---------|
| `rax` | **quotient** |
| `rdx` | **reste** (modulo) |

## Très utile en pratique

### Pourquoi pas d'affichage du résultat ?

Afficher un entier nécessite de le **convertir en texte** (chiffre par chiffre, en ASCII). On apprend cette conversion au chapitre 14. Pour l'instant :
- Soit on utilise `mov rdi, rax` puis `exit` pour voir le résultat dans `echo $?`.
- Soit on regarde dans GDB (chapitre suivant).

### Récapitulatif des opérandes

| Instruction | Opérandes valides |
|-------------|-------------------|
| `add rax, 5` | registre, immédiate ✓ |
| `add rax, rbx` | registre, registre ✓ |
| `add rax, [var]` | registre, mémoire ✓ |
| `add [var], rax` | mémoire, registre ✓ |
| `add [a], [b]` | ❌ INTERDIT comme pour `mov` |

La règle "pas de mémoire-à-mémoire directe" vaut pour **toutes** les instructions arithmétiques.

### Comparer avec Python

| Python | Assembleur |
|--------|------------|
| `a = 5` | `mov rax, 5` |
| `a = b` | `mov rax, rbx` |
| `a += b` | `add rax, rbx` |
| `a -= b` | `sub rax, rbx` |
| `a *= b` | `imul rax, rbx` |
| `a, b = b, a` | (chapitre 18 avec push/pop, ou 3 mov via rcx) |

## Bonus

### `lea` pour des additions rapides

Petite astuce qu'on creuse au chapitre 12 : `lea` permet de faire **`rax = rbx + rcx`** en une instruction :

```nasm
lea rax, [rbx + rcx]    ; rax = rbx + rcx  (sans toucher aux flags)
```

Tu verras `lea` partout en reverse engineering pour cette raison.

## ❌ Erreur classique

```
Croire que le résultat s'affiche
→ Non. On le met dans un registre. Pour voir : GDB ou code de retour.

Écraser un registre dont on a encore besoin
→ Classique : mov rax, calcul ; mov rax, autre_chose → premier résultat perdu.

Oublier rdx = 0 avant idiv
→ Bug silencieux ou crash. À retenir absolument.

Utiliser mul au lieu de imul pour des nombres positifs
→ mul est à 1 opérande et utilise rdx:rax. imul est plus simple.

Croire que add rax, [a], [b] existe
→ Non. add prend exactement 2 opérandes.

Confondre signé et non signé
→ -1 signé = 0xFFFFFFFFFFFFFFFF. En non signé, c'est un énorme nombre.
```

## Exercices

**Guidé :** Écris un programme qui calcule `(5 + 3) * 2` et place le résultat dans le code de retour. Vérifie avec `echo $?` que tu obtiens **16**.

**Autonome :** Écris un programme qui calcule `100 / 3` (quotient dans `rdi`) puis quitte. `echo $?` doit afficher **33**.

**Défi :** Calcule la suite : `((10 - 2) * 3 + 7) / 5`. Donne le résultat via le code de retour.

> **Réponse attendue :** `((10-2)*3+7)/5 = (24+7)/5 = 31/5 = 6` (reste 1).

## 🧩 Mini-projet (chapitres 7-8) — Mini-calculatrice

Écris `calc.asm` qui calcule sans aucune saisie (valeurs codées en dur) :

- Une variable `a dq 50` et `b dq 7`
- Affiche le code de retour égal à `(a + b) - (a / b)`

Étapes :
1. Charge `a` et `b` dans des registres.
2. Calcule `a + b` dans un registre.
3. Calcule `a / b` (attention `rdx = 0`) dans un autre.
4. Soustrais.
5. Mets le résultat dans `rdi` et appelle `exit`.

Résultat attendu : `(50 + 7) - (50 / 7) = 57 - 7 = 50`.

## ✅ Tu sais maintenant…

- Faire **addition, soustraction, multiplication, division**
- Utiliser **`inc`** et **`dec`** pour ±1
- Utiliser **`neg`** pour l'opposé
- La particularité d'**`idiv`** (quotient dans `rax`, reste dans `rdx`, `rdx = 0` avant pour des positifs, **`cqo` pour des signés négatifs**)
- Utiliser le **code de retour** comme canal de sortie temporaire
- Pourquoi on ne **voit pas** encore le résultat à l'écran

---

# Chapitre 9 — GDB pour observer les registres

## Le minimum à savoir

### Pourquoi GDB tout de suite

Tu codes "à l'aveugle" depuis le chapitre 6. Tu fais `mov rax, 5`, mais tu **ne vois pas** que `rax` vaut 5. GDB, c'est ce qui te permet de **voir** ce que ton programme fait, instruction par instruction.

> **À retenir :** GDB est à l'assembleur ce que `print()` est à Python. C'est **l'outil de visibilité**. Sans lui, tu codes à l'aveugle.

### Compiler avec les symboles de debug

Pour que GDB t'affiche un maximum d'informations, compile avec `-g -F dwarf` :

```bash
nasm -f elf64 -g -F dwarf mon_prog.asm -o mon_prog.o
ld mon_prog.o -o mon_prog
```

Si tu utilises le Makefile du chapitre 4, c'est déjà fait.

### Lancer GDB

```bash
gdb ./mon_prog
```

Tu arrives dans le prompt GDB (`(gdb)`). À ce stade, **rien n'est lancé**. Tu prépares la session.

### Les 7 commandes vitales pour démarrer

| Commande | Raccourci | Effet |
|----------|-----------|-------|
| `break _start` | `b _start` | Pose un **breakpoint** au début |
| `run` | `r` | **Lance** le programme |
| `stepi` | `si` | Avance d'**une instruction** |
| `info registers` | `i r` | Affiche **tous les registres** |
| `print /x $rax` | `p /x $rax` | Affiche `rax` en **hexa** |
| `disassemble` | `disas` | Affiche le **désassemblage** autour de l'instruction courante |
| `quit` | `q` | **Quitter** GDB |

### Un exemple pas-à-pas

Voici un programme et la session GDB qui va avec.

**Le programme `voir.asm` :**

```nasm
section .text
global _start
_start:
    mov rax, 10
    mov rbx, 32
    add rax, rbx       ; rax devrait valoir 42
    mov rdi, rax
    mov rax, 60
    syscall
```

**La session GDB :**

```
$ gdb ./voir
(gdb) break _start
Breakpoint 1 at 0x401000
(gdb) run
Breakpoint 1, _start () at voir.asm:3
3           mov rax, 10
(gdb) info registers rax rbx
rax  0x0    0
rbx  0x0    0

(gdb) stepi              # exécute mov rax, 10
(gdb) print /x $rax
$1 = 0xa

(gdb) stepi              # exécute mov rbx, 32
(gdb) print /x $rbx
$2 = 0x20

(gdb) stepi              # exécute add rax, rbx
(gdb) print /x $rax
$3 = 0x2a                # 0x2a = 42 ✓

(gdb) quit
```

🎉 Tu as **vu** les registres bouger en temps réel. C'est ça, GDB.

### Avec pwndbg : encore plus visuel

Si tu as installé pwndbg, à chaque `stepi`, GDB affiche **automatiquement** :
- Les **registres** (avec leur valeur en hexa et décimal).
- Le **désassemblage** autour de l'instruction courante.
- La **pile** (chapitre 18).
- Les **flags** (chapitre 16).

```
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
─[ REGISTERS / show-flags off / show-compact-regs off ]──
*RAX  0x2a
 RBX  0x20
 RCX  0x0
 ...
─[ DISASM / x86-64 / set emulate on ]──
   0x401000 <_start>      mov    rax, 0xa
   0x401007 <_start+7>    mov    rbx, 0x20
 ► 0x40100e <_start+14>   add    rax, rbx
   0x401011 <_start+17>   mov    rdi, rax
   ...
```

C'est **beaucoup** plus pédagogique. Installe-le si ce n'est pas fait.

## Très utile en pratique

### Voir un registre en plusieurs formats

```
(gdb) print $rax          # décimal      → 42
(gdb) print /x $rax       # hexadécimal  → 0x2a
(gdb) print /t $rax       # binaire      → 101010
(gdb) print /c $rax       # caractère    → '*'  (42 = '*')
```

### Voir la mémoire

```
(gdb) x/10gx 0x404000     # 10 qword en hexa à partir de cette adresse
(gdb) x/10bx &var         # 10 octets en hexa de la variable var
(gdb) x/s &msg            # une chaîne ASCII à partir de msg
```

Le format `x/COUNT SIZE FORMAT` :
- COUNT : combien d'éléments
- SIZE : `b` (byte), `w` (word), `d` (dword), `g` (qword)
- FORMAT : `x` (hexa), `d` (décimal), `s` (chaîne), `c` (caractère)

### Avancer plus vite

| Commande | Effet |
|----------|-------|
| `stepi` (`si`) | 1 instruction |
| `stepi 5` | 5 instructions |
| `continue` (`c`) | Continuer jusqu'au prochain breakpoint ou la fin |
| `nexti` (`ni`) | 1 instruction, **sans entrer dans les `call`** (utile plus tard) |

### Lister son code dans GDB

```
(gdb) disas _start        # désassemble la fonction _start
(gdb) layout asm          # ouvre une fenêtre dédiée au désassemblage
```

`layout asm` est très pratique : tu vois le code en haut et le prompt en bas. Pour quitter ce mode : `Ctrl+X A`.

## Bonus

### Quelques commandes utiles supplémentaires

| Commande | Effet |
|----------|-------|
| `info breakpoints` | Liste tous les breakpoints |
| `delete N` | Supprime le breakpoint N |
| `watch <expr>` | Casse quand `<expr>` change |
| `set $rax = 100` | **Modifie un registre** à la volée (cheat code) |
| `start` | Lance et casse à `main` (utile en C, ch. 21) |

### Modifier un registre à la volée

```
(gdb) set $rax = 999
```

Ça permet de tester "que se passerait-il si `rax` valait 999 ici ?". Très utile en reverse engineering quand on veut **forcer une condition**.

### Un `.gdbinit` personnalisé

Tu peux créer `~/.gdbinit` avec :

```
set disassembly-flavor intel
set print pretty on
```

Ça force GDB à afficher en **syntaxe Intel** par défaut (au lieu d'AT&T qui est cryptique). À faire **maintenant**, ça t'évitera des migraines.

## ❌ Erreur classique

```
Lancer "run" avant de poser un breakpoint
→ Le programme termine sans s'arrêter. Pose break _start AVANT.

Utiliser "step" au lieu de "stepi"
→ "step" attend des symboles source (pas en ASM pur).
→ Toujours "stepi" en assembleur.

Oublier de recompiler avec -g
→ GDB ne pourra pas relier les instructions aux lignes de l'.asm.

Sortir et relancer GDB pour chaque test
→ Tu peux relancer dans GDB avec "run" tout seul. Pas besoin de quitter.

Croire qu'AT&T == Intel
→ Si tu vois mov $5, %rax → c'est AT&T. mov rax, 5 → c'est Intel.
→ Pour passer en Intel : set disassembly-flavor intel
```

## Exercices

**Guidé :** Reprends le programme `voir.asm` ci-dessus. Lance-le dans GDB. Pose un breakpoint sur `_start`. Avance `stepi` après `stepi` et vérifie que :
- Après `mov rax, 10` : `rax = 10`
- Après `mov rbx, 32` : `rbx = 32`
- Après `add rax, rbx` : `rax = 42`

**Autonome :** Écris un programme `calculs.asm` qui fait 5 opérations arithmétiques d'affilée (au choix). **Avant** d'exécuter, écris sur papier ce que tu attends pour `rax` après chaque ligne. Vérifie au GDB.

**Défi :** Lance `voir.asm` dans GDB. Avant `add rax, rbx`, **force** `rbx = 100` avec `set $rbx = 100`. Continue avec `stepi`. Quelle est la valeur finale de `rax` ? (Réponse : 110, car 10 + 100.)

## 🧩 Mini-projet (chapitres 7-9) — Carnet d'observations

Écris `obs.asm` qui modifie `rax` exactement **6 fois** :

1. `mov rax, 1`
2. `add rax, 9`        → rax = 10
3. `imul rax, rax`     → rax = 100
4. `sub rax, 50`       → rax = 50
5. `inc rax`           → rax = 51
6. Sortir avec **`rax = 51`** comme code de retour

> **Attention à l'ordre des deux dernières instructions !** Si tu écris `mov rax, 60` en premier, tu écrases ton résultat (51). L'ordre correct est :
> ```nasm
>     ; après l'étape 5, rax = 51
>     mov rdi, rax       ; copier le résultat dans rdi AVANT d'écraser rax
>     mov rax, 60        ; puis seulement, numéro du syscall exit
>     syscall
> ```

Lance le programme dans GDB. **Note dans ton cahier** la valeur de `rax` après chaque `stepi` avant de regarder l'affichage GDB. Si tu te trompes, comprends pourquoi.

## ✅ Tu sais maintenant…

- Lancer un programme dans **GDB** : `gdb ./prog`
- Poser un **breakpoint** : `break _start`
- **Lancer** : `run`
- Avancer d'**une instruction** : `stepi`
- Afficher les **registres** : `info registers`, `print /x $rax`
- Afficher la **mémoire** : `x/10gx adresse`
- Désassembler : `disas`
- Modifier un registre à la volée : `set $rax = ...`
- Forcer la **syntaxe Intel** dans `.gdbinit`

À partir d'ici, **tous tes exercices se vérifient dans GDB**. C'est ta voix off.

---

## 🚩 Checkpoint — Fin de la Partie III

Avant de passer aux chapitres suivants, tu **dois** être capable de :

- [ ] Expliquer la différence entre `mov rax, x` et `mov rax, [x]` sans hésitation.
- [ ] Écrire un programme qui fait une addition entre deux registres.
- [ ] Compiler un `.asm` en exécutable (`nasm` puis `ld`).
- [ ] Lancer ce programme dans **GDB**, poser un breakpoint sur `_start`, et avancer avec `stepi`.
- [ ] Afficher la valeur de `rax`, `rbx`, `rsp` dans GDB.
- [ ] Lire un dump mémoire en hexadécimal et reconnaître quelques caractères ASCII.
- [ ] Utiliser le code de retour (`exit` + `echo $?`) pour vérifier un calcul simple.

Si tu coches tout, tu as les **vraies bases**. Si un point reste flou, **refais les exemples** avant de continuer. La suite suppose que ces réflexes sont acquis.

---


# PARTIE IV — MÉMOIRE, ADRESSES ET CHAÎNES

---

# Chapitre 10 — Mémoire, adresses et variables

## Le minimum à savoir

### Une "variable" en assembleur, c'est quoi ?

En Python, `x = 5` crée une **variable**. En assembleur, le concept est plus terre-à-terre :

> **Une variable assembleur, c'est juste un nom (label) qu'on donne à une adresse mémoire.** Rien de plus.

Quand tu écris :

```nasm
section .data
    x dq 5
```

NASM réserve **8 octets** quelque part en mémoire, y met la valeur `5`, et garde en tête que cet endroit s'appelle `x`. Plus tard, quand tu écris `mov rax, [x]`, NASM remplace `x` par cette adresse.

### Adresse vs contenu : LA confusion à comprendre

C'est la confusion **n°1** du débutant. Lis ça **plusieurs fois** :

```nasm
section .data
    x dq 42

section .text
    mov rax, x       ; rax = ADRESSE de x (par exemple 0x402000)
    mov rax, [x]     ; rax = CONTENU à l'adresse de x → rax = 42
```

| Forme | Signification |
|-------|---------------|
| **`x`** sans crochets | "L'adresse à laquelle vit la variable" |
| **`[x]`** avec crochets | "Le contenu stocké à cette adresse" |

> **Analogie postale :** `x` est l'**adresse** d'une maison (123 rue de la Paix). `[x]` est **ce qu'il y a dans la maison** (les habitants).

### Lire et écrire en mémoire

```nasm
section .data
    nombre dq 100

section .text
    mov rax, [nombre]    ; lire :   rax = 100
    add rax, 50          ; rax = 150
    mov [nombre], rax    ; écrire : la mémoire à l'adresse "nombre" = 150
```

À la fin, `nombre` en mémoire contient `150`. Tu peux le vérifier dans GDB avec `x/gd &nombre`.

### La règle d'or rappelée : pas de mémoire-à-mémoire

```nasm
section .data
    a dq 5
    b dq 10

section .text
    mov [a], [b]     ; ❌ INTERDIT
```

Comme au chapitre 7, tu **dois** passer par un registre :

```nasm
    mov rax, [b]     ; charger
    mov [a], rax     ; ranger
```

### Choisir la taille en mémoire

Tu peux lire ou écrire 1, 2, 4 ou 8 octets selon ce que tu veux :

```nasm
section .data
    valeur dq 0x123456789ABCDEF0    ; 8 octets

section .text
    mov al,  [valeur]     ; lit 1 octet  → 0xF0
    mov ax,  [valeur]     ; lit 2 octets → 0xDEF0
    mov eax, [valeur]     ; lit 4 octets → 0x9ABCDEF0
    mov rax, [valeur]     ; lit 8 octets → 0x123456789ABCDEF0
```

> **Pourquoi `al` lit-il `0xF0` et pas `0x12` ?** À cause du **little-endian** (Annexe E) : les octets de poids faible sont stockés en premier. Pour `0x123456789ABCDEF0`, le premier octet en mémoire est `0xF0`.

### Réserver un buffer dans `.bss`

Quand on veut juste **de la place vide** (par exemple pour stocker une saisie utilisateur), on utilise `.bss` :

```nasm
section .bss
    buffer  resb 64       ; 64 octets vides
    nb_lus  resq 1        ; 1 qword (8 octets) vide
```

C'est exactement comme `.data`, sauf qu'on **ne met pas de valeur initiale**.

### Tableaux simples

Un tableau en assembleur, c'est juste **plusieurs valeurs côte à côte** :

```nasm
section .data
    notes dq 10, 14, 18, 7, 12      ; 5 qword consécutifs
```

Pour accéder à un élément, on utilise l'**adresse + un décalage**, **en octets** :

```nasm
    mov rax, [notes]         ; 1er élément (index 0)  → 10
    mov rax, [notes + 8]     ; 2ème élément (index 1) → 14
    mov rax, [notes + 16]    ; 3ème élément (index 2) → 18
```

> **Attention :** le décalage est en **octets**, pas en éléments. Pour un tableau de `qword` (8 octets), c'est `+0`, `+8`, `+16`, `+24`, `+32`. Pour un tableau d'octets (`db`), ce serait `+0`, `+1`, `+2`…

### Indexation avec un registre

Pour parcourir un tableau (au chapitre 17), on utilisera l'**indexation par registre** :

```nasm
    mov rcx, 0                       ; index
    mov rax, [notes + rcx*8]         ; notes[0]
    mov rcx, 2                       ; index = 2
    mov rax, [notes + rcx*8]         ; notes[2] = 18
```

La syntaxe `[base + index * échelle]` est un **mode d'adressage** qu'on creuse au chapitre 12.

## Très utile en pratique

### Exemple complet

```nasm
; memoire.asm — Manipulation de variables en mémoire

section .data
    x dq 10
    y dq 7
    resultat dq 0

section .text
global _start
_start:
    mov rax, [x]            ; rax = 10
    add rax, [y]            ; rax = 10 + 7 = 17
    mov [resultat], rax     ; resultat en mémoire = 17

    ; Sortir avec resultat en code de retour
    mov rdi, [resultat]
    mov rax, 60
    syscall
```

Exécute, puis :

```bash
./memoire ; echo $?     # → 17
```

Vérifie dans GDB avec `x/gd &resultat` que la mémoire a bien été modifiée.

### Récapitulatif des opérandes mémoire

| Syntaxe | Effet |
|---------|-------|
| `mov rax, x` | `rax = adresse de x` |
| `mov rax, [x]` | `rax = contenu à l'adresse x` |
| `mov [x], rax` | Écrit `rax` à l'adresse `x` |
| `mov rax, [x + 8]` | Lit 8 octets après `x` |
| `mov rax, [x + rcx*8]` | Adressage indexé |
| `mov byte [x], 5` | Écrit l'octet `5` (précise la taille) |

## Bonus

### Little-endian en pratique

Si tu fais :

```nasm
section .data
    n dq 0x1234567890ABCDEF
```

Et que tu regardes la mémoire dans GDB avec `x/8bx &n`, tu verras :

```
0x404000:  0xef  0xcd  0xab  0x90  0x78  0x56  0x34  0x12
```

Les octets sont **dans l'ordre inverse de l'écriture**. C'est du little-endian. Le CPU s'y retrouve automatiquement quand tu fais `mov rax, [n]` : tu récupères bien `0x1234567890ABCDEF`.

> **À retenir :** lorsque tu vois un dump mémoire, **les octets sont à l'envers** par rapport à comment tu écris la valeur. Détails complets dans l'**Annexe E**.

## ❌ Erreur classique

```
Oublier les crochets : mov rax, x au lieu de mov rax, [x]
→ Tu charges l'adresse au lieu de la valeur. Confusion n°1.

Lire avec la mauvaise taille : mov al, [x] quand x est un qword
→ Tu n'auras que les 8 bits bas. Souvent un bug silencieux.

Indexer en éléments au lieu d'octets : [notes + 1] pour le 2ème élément
→ Ça lit 1 octet plus loin, pas 8. Pour un dq, c'est [notes + 8].

Écrire dans la section .text
→ Crash. .text est en lecture seule.

Lire dans .bss sans avoir mis quelque chose dedans
→ Tu lis des octets nuls (0). Pas grave, mais à savoir.

Confondre label et valeur : mov rdi, msg vs mov rdi, [msg]
→ Pour write(rsi = msg), on veut l'adresse. Pour exit(rdi = code),
  on veut la valeur. Distinguer selon le syscall.
```

## Exercices

**Guidé :** Crée un programme qui déclare `x dq 5` et `y dq 7`, calcule `x + y`, met le résultat dans `resultat dq 0`, puis sort avec ce résultat comme code de retour. Vérifie au GDB que `resultat` en mémoire vaut bien `12` après exécution.

**Autonome :** Déclare un tableau `nombres dq 10, 20, 30, 40, 50`. Charge le 3ème élément (valeur 30) dans `rax`. Multiplie-le par 2. Range-le dans le 5ème élément. Vérifie dans GDB que la mémoire a changé.

**Défi :** En partant de `valeur dq 0x12345678`, fais en sorte que `rax` ne contienne que les **2 octets du milieu** (`0x3456`). **Indice :** lecture en `word`, avec un décalage de 2 octets.

## 🧩 Mini-projet (chapitres 7-10) — Moyenne de notes

Crée `moyenne.asm` qui :

1. Déclare un tableau `notes dq 12, 14, 18, 16, 10` (5 notes).
2. Additionne les 5 notes dans `rax` (en lisant `[notes]`, `[notes + 8]`, etc. — sans boucle, on n'en a pas vu).
3. Divise par 5 (`idiv` avec `rdx = 0`).
4. Sort avec la moyenne comme code de retour.

Résultat attendu : `(12+14+18+16+10) / 5 = 70 / 5 = 14`. Donc `echo $?` doit afficher **14**.

## ✅ Tu sais maintenant…

- Qu'une **variable assembleur = un label sur une adresse**
- La différence cruciale **`x`** (adresse) vs **`[x]`** (contenu)
- Lire et écrire en mémoire avec **`mov`**
- Choisir la **taille** (`al`, `ax`, `eax`, `rax`)
- Réserver un **buffer** dans `.bss`
- Accéder à un **élément de tableau** avec un décalage en octets
- L'idée du **little-endian** (les octets stockés "à l'envers")

---

# Chapitre 11 — Chaînes de caractères et octets

## Le minimum à savoir

### Une chaîne, c'est juste une suite d'octets

En Python, `"Bonjour"` est un objet `str` avec plein de méthodes magiques. En assembleur, **une chaîne, c'est juste des octets côte à côte en mémoire**. Rien de plus.

```nasm
section .data
    msg db "Bonjour", 10
```

En mémoire, on a ces octets :

```
   B    o    n    j    o    u    r    \n
  0x42 0x6F 0x6E 0x6A 0x6F 0x75 0x72 0x0A
```

8 octets. C'est tout. Aucune "magie".

### Pourquoi `db` ?

`db` = **define byte**. Comme une chaîne, c'est un **flux d'octets**, on l'écrit avec `db`. Le compilateur transforme automatiquement chaque caractère en son **code ASCII**.

```nasm
msg db "AB"          ; équivalent à : msg db 0x41, 0x42
```

### Le retour ligne et le zéro final

Deux octets spéciaux à connaître :

- **`10`** (ou `0x0A`) = **retour ligne** (`\n`). On le met à la fin d'un message pour que la ligne suivante apparaisse.
- **`0`** (ou `0x00`) = **caractère NUL**. C'est le marqueur de fin de chaîne en C (mais **pas** pour les syscalls Linux).

```nasm
msg1 db "Hello", 10              ; pour les syscalls (write, etc.)
msg2 db "Hello", 0               ; pour les fonctions C (printf, etc.)
msg3 db "Hello", 10, 0           ; les deux, par sécurité
```

### Deux styles de chaînes : Linux vs C

| Style | Comment ça marque la fin | Usage |
|-------|--------------------------|-------|
| **Style Linux** | Par sa **longueur** explicite (passée en argument) | Syscalls `write`, `read` |
| **Style C** | Par un **octet 0** à la fin | Fonctions `printf`, `strlen`, `strcmp` |

En clair : pour `write`, on donne la longueur. Pour `printf`, on met un `0` à la fin et `printf` s'arrête tout seul en le voyant.

### Calculer la longueur avec `equ $ - msg`

```nasm
section .data
    msg db "Bonjour", 10
    len equ $ - msg          ; len = nombre d'octets de msg
```

`$` signifie "ici", l'**adresse actuelle**. Donc `$ - msg` = "la distance entre `msg` et maintenant" = la longueur en octets.

> **Astuce :** mets toujours `equ $ - label` **juste après** la chaîne. Si tu mets autre chose entre les deux, le calcul est faux.

### Modifier un caractère en mémoire

Comme `msg` est une suite d'octets, on peut en modifier un seul :

```nasm
section .data
    msg db "Bonjour", 10
    len equ $ - msg

section .text
global _start
_start:
    ; Remplacer le 'B' par 'X'
    mov byte [msg], 'X'         ; 'X' = 0x58 = 88
    ; ou : mov byte [msg], 0x58

    ; Afficher
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall

    mov rax, 60
    mov rdi, 0
    syscall
```

Sortie :

```
Xonjour
```

> **Le piège :** `mov [msg], 'X'` sans préciser `byte` donne une erreur ("operation size not specified"). En mémoire seule, NASM ne devine pas la taille.

### Accéder à un caractère par son index

```nasm
mov al, [msg]           ; al = 'B' = 0x42  (1er caractère)
mov al, [msg + 1]       ; al = 'o' = 0x6F  (2ème caractère)
mov al, [msg + 3]       ; al = 'j'         (4ème caractère)
```

Pour un tableau de caractères, l'index est **directement** le décalage (puisque chaque caractère fait 1 octet).

### Afficher une portion seulement

`write` prend une longueur — donc tu peux n'afficher que **5 caractères** :

```nasm
mov rax, 1
mov rdi, 1
mov rsi, msg
mov rdx, 5              ; n'afficher que 5 octets : "Bonjo"
syscall
```

### Compter les caractères jusqu'à un délimiteur

C'est l'équivalent de `strlen()`. Sans boucle, on ne peut pas encore le coder proprement (on le fera au chapitre 17). Mais l'idée est de **parcourir octet par octet jusqu'à tomber sur un `0`** (style C) ou un `10` (style retour ligne).

## Très utile en pratique

### Chaîne sur plusieurs lignes

```nasm
section .data
    menu db "1) Option A", 10
         db "2) Option B", 10
         db "3) Quitter",  10
    menu_len equ $ - menu
```

NASM concatène automatiquement les `db` successifs (puisque la mémoire est contiguë). Très pratique pour des menus.

### Construire une chaîne caractère par caractère

```nasm
section .bss
    buffer resb 32

section .text
    mov byte [buffer + 0], 'H'
    mov byte [buffer + 1], 'i'
    mov byte [buffer + 2], '!'
    mov byte [buffer + 3], 10
    ; afficher 4 octets de buffer
```

Plus tard, avec des boucles, on automatisera ça.

### Aperçu : pourquoi un `0` final pour la libc ?

Quand tu fais `printf("%s", msg)`, `printf` lit `msg` **caractère par caractère** jusqu'à rencontrer un octet `0`. Sans ce `0`, `printf` continuera à lire en mémoire **bien au-delà** de ta chaîne, affichant du garbage… jusqu'à crash. On en reparle au chapitre 21.

## Bonus

### Caractères spéciaux

| Caractère | Décimal | Hexa | Effet |
|-----------|---------|------|-------|
| `\n` (LF) | 10 | `0x0A` | Saut de ligne (Linux) |
| `\r` (CR) | 13 | `0x0D` | Retour chariot (Windows utilise `\r\n`) |
| `\t` (TAB) | 9 | `0x09` | Tabulation |
| `\0` (NUL) | 0 | `0x00` | Fin de chaîne C |
| `\\` | 92 | `0x5C` | Antislash |

En NASM, **dans les chaînes classiques entre guillemets `"..."`, `\n` n'est PAS interprété** comme un retour ligne. Tu dois écrire `10` explicitement :

```nasm
msg db "Hello\n"        ; ❌ Affichera littéralement "Hello\n", barre oblique comprise
msg db "Hello", 10      ; ✅ correct
```

> **Détail :** NASM accepte des **backquotes** (`\`...\``) qui, elles, interprètent les échappements comme `\n`, `\t`. Mais on ne les utilisera pas dans ce cours pour rester simple — préfère toujours `, 10` à la fin de la chaîne.

### Convertir une lettre majuscule/minuscule

Comme `'A' = 0x41` et `'a' = 0x61`, la différence est **0x20** = 32. Donc :

```nasm
; transformer 'A' en 'a'
mov al, 'A'              ; al = 0x41
add al, 0x20             ; al = 0x61 = 'a'

; transformer 'a' en 'A'
mov al, 'a'              ; al = 0x61
sub al, 0x20             ; al = 0x41 = 'A'
```

C'est précisément ce que fait `str.lower()` en Python, mais à la main, octet par octet.

## ❌ Erreur classique

```
Croire qu'une chaîne est un "type" comme en Python
→ Non, c'est juste une suite d'octets.

Écrire "Hello\n" en pensant que \n est interprété
→ NASM affichera "Hello\n" littéralement. Utilise "Hello", 10.

Oublier le 0 final pour printf
→ printf lira en dehors de la chaîne, comportement indéfini.

Confondre longueur et adresse
→ rdx = LONGUEUR (un nombre, genre 8). rsi = ADRESSE (un pointeur).

Mettre len = $ - msg mais APRÈS avoir mis d'autres données
→ Le calcul inclura ces autres données. Toujours juste après le msg.

Modifier byte [msg], 'X' sans préciser "byte"
→ Erreur NASM "operation size not specified".

Faire mov [msg], 'A' au lieu de mov byte [msg], 'A'
→ Pareil. Toujours préciser la taille pour la mémoire.
```

## Exercices

**Guidé :** Crée un programme `salut.asm` qui :
1. Déclare `msg db "Hello, World!", 10`.
2. Calcule `len equ $ - msg`.
3. Affiche le message via `write`.

**Autonome :** Modifie ton programme pour :
1. Remplacer le premier caractère par `'J'` avant d'afficher (→ "Jello, World!").
2. N'afficher que les **5 premiers caractères**.

**Défi :** Crée un programme qui affiche la lettre `'A'` seulement (1 octet, sans retour ligne). Puis modifie-le pour afficher la lettre `'A'` **puis** un retour ligne. Tu n'as droit qu'à 1 octet de buffer.

## 🧩 Mini-projet (chapitres 9-11) — Bannière dynamique

Crée `banniere2.asm` qui :

1. Déclare une chaîne `motif db "* * * BIENVENUE * * *", 10`.
2. Affiche la chaîne **trois fois** (3 syscalls write d'affilée).
3. **Bonus :** entre chaque affichage, modifie la première étoile en `'+'`.

> **Indice :** pour modifier, utilise `mov byte [motif], '+'`. Pour afficher, garde la même longueur.

## ✅ Tu sais maintenant…

- Qu'une **chaîne = suite d'octets** en mémoire
- Le rôle de **`db`** pour déclarer des octets
- La différence entre **style Linux (longueur)** et **style C (`0` final)**
- Les codes ASCII utiles : `10` pour `\n`, `0` pour la fin C
- Modifier un **caractère en mémoire** avec `mov byte [...]`
- Accéder à un caractère **par son index** (`[msg + N]`)
- Pourquoi NASM **n'interprète pas `\n`** dans une chaîne

---

# Chapitre 12 — `lea` et modes d'adressage

## Le minimum à savoir

### `lea` : "Load Effective Address"

`lea` est une instruction qu'on confond souvent avec `mov`. Elle a une particularité :

> **`lea` calcule une adresse mais ne lit pas la mémoire.**

```nasm
mov rax, [rbx]       ; rax = CONTENU à l'adresse rbx
lea rax, [rbx]       ; rax = rbx (juste copie l'adresse, ne lit rien)
```

Avec `mov`, les crochets veulent dire "lis la mémoire". Avec `lea`, ils signifient juste "calcule cette expression d'adresse". **Aucune lecture mémoire** n'est faite.

### Pourquoi `lea` est si fréquent en reverse engineering

Imagine que tu veux faire `rax = rbx + rcx*8 + 16`. Sans `lea`, ça prend plusieurs instructions :

```nasm
mov rax, rcx
imul rax, 8
add rax, rbx
add rax, 16
```

Avec `lea`, **une seule** instruction :

```nasm
lea rax, [rbx + rcx*8 + 16]
```

Du coup, les compilateurs C utilisent `lea` **partout**, même pour faire des additions simples. Tu verras `lea` en désassemblage **tout le temps**.

### Les modes d'adressage de x86-64

Quand tu vois des `[...]` en assembleur, ce qui est dedans peut être plus complexe qu'un simple registre. Voici les **modes d'adressage** possibles :

| Mode | Exemple | Calcul |
|------|---------|--------|
| Direct | `[var]` | adresse de `var` |
| Registre | `[rax]` | adresse contenue dans `rax` |
| Base + déplacement | `[rax + 8]` | `rax + 8` |
| Base + index | `[rax + rcx]` | `rax + rcx` |
| Base + index × échelle | `[rax + rcx*4]` | `rax + 4*rcx` |
| Forme complète | `[rax + rcx*8 + 16]` | `rax + 8*rcx + 16` |

L'**échelle** ne peut être que `1`, `2`, `4` ou `8` (souvent 8 pour les `qword`, 4 pour les `dword`, 1 pour les `byte`).

### Cas d'usage typique : parcourir un tableau

Si tu as `tableau dq 10, 20, 30, 40` et que tu veux l'élément à l'index `rcx` :

```nasm
mov rax, [tableau + rcx*8]   ; rax = tableau[rcx]
```

Si tu veux l'**adresse** de cet élément (et non son contenu) :

```nasm
lea rax, [tableau + rcx*8]   ; rax = &tableau[rcx]
```

C'est exactement comme **`&tab[i]` vs `tab[i]`** en C.

### `mov` ou `lea` ? Comparaison

```nasm
section .data
    x dq 42

section .text
    mov rax, x         ; rax = adresse de x (compile-time)
    lea rax, [x]       ; rax = adresse de x (équivalent, plus moderne)

    mov rbx, [x]       ; rbx = 42 (contenu)
    lea rbx, [x]       ; rbx = adresse de x (PAS le contenu)
```

> **Règle :** si tu veux **le contenu** → `mov reg, [...]`. Si tu veux **l'adresse** ou **une formule d'addition** → `lea reg, [...]`.

## Très utile en pratique

### `lea` pour des additions/multiplications rapides

Comme `lea` permet `base + index*échelle + déplacement`, on peut s'en servir pour des calculs sans `add`/`imul` :

```nasm
; rax = rbx + rcx
lea rax, [rbx + rcx]

; rax = rbx * 5  (= rbx + rbx*4)
lea rax, [rbx + rbx*4]

; rax = rbx * 3 + 7
lea rax, [rbx + rbx*2 + 7]
```

> **Avantage :** `lea` ne modifie **pas les flags** (contrairement à `add`). Ça permet de faire des calculs sans casser une comparaison en cours.

### Avec les chaînes

Tu peux récupérer l'adresse d'un octet précis d'une chaîne :

```nasm
section .data
    msg db "Hello", 0

section .text
    lea rax, [msg + 2]    ; rax pointe sur le 'l' (3ème caractère)
    mov al, [rax]         ; al = 'l'
```

## Bonus

### `lea` dans le code généré par gcc

Si tu compiles ceci en C :

```c
int f(int a, int b) {
    return a + b * 4 + 10;
}
```

`gcc -O0 -masm=intel -S` produit (extrait) :

```nasm
lea     eax, [rdi + rsi*4 + 10]
```

Une **seule instruction** au lieu de quatre. C'est pour ça que `lea` est partout. Comprendre `lea` = comprendre 30 % du code désassemblé.

### `RIP-relative addressing`

En x86-64, on voit souvent `[rel msg]` ou `[rip + ...]`. C'est l'**adressage relatif à `rip`** (le pointeur d'instruction). C'est ce que les exécutables modernes utilisent pour être déplaçables en mémoire (PIE). Pour ce cours, NASM gère ça automatiquement quand on compile avec `default rel` ou quand on lie un programme dynamique. Ne t'en préoccupe pas tant que tu fais des programmes statiques avec `ld`.

## ❌ Erreur classique

```
Croire que lea charge le contenu mémoire
→ NON. lea calcule l'adresse, ne lit rien.

Utiliser lea quand on voulait mov : lea rax, [x] alors qu'on voulait le contenu
→ Bug silencieux : tu as l'adresse, pas la valeur.

Utiliser une échelle interdite : [rax + rcx*3]
→ Échelle = 1, 2, 4 ou 8 uniquement. 3 est interdit.

Oublier que dans [tab + rcx*8], rcx est en éléments
→ Si tableau de qword, rcx*8 est correct.
→ Si tableau de dword, ce serait rcx*4.
→ Si tableau d'octets, ce serait rcx*1.

Confondre [tab + rcx] et [tab + rcx*8] pour un tableau de qword
→ La 1ère lit à l'octet rcx, la 2nde à l'élément rcx.
```

## Exercices

**Guidé :** Recopie et compile :

```nasm
section .data
    x dq 100

section .text
global _start
_start:
    mov rax, x          ; adresse
    lea rbx, [x]        ; adresse aussi
    mov rcx, [x]        ; contenu
    lea rdx, [x + 8]    ; adresse + 8

    mov rdi, 0
    mov rax, 60
    syscall
```

Lance dans GDB. Compare `rax` et `rbx` (devrait être identiques). Compare `rax` et `rcx`. Comprends `rdx`.

**Autonome :** Soit le tableau `tab dq 10, 20, 30, 40, 50`. Sans utiliser `add` ni `imul`, écris une instruction **unique** qui met dans `rax` l'adresse de `tab[3]` (= adresse du `40`).

**Défi :** Réécris ces lignes en utilisant `lea` au lieu de `mov`/`add` :

```nasm
; version classique
mov rax, rbx
add rax, rcx
add rax, 100

; → ta version avec un seul lea ?
```

> **Réponse :** `lea rax, [rbx + rcx + 100]`

## ✅ Tu sais maintenant…

- La différence entre **`mov`** (lit la mémoire) et **`lea`** (calcule juste une adresse)
- Les **modes d'adressage** : `[reg]`, `[reg + N]`, `[reg + reg*échelle]`, `[reg + reg*échelle + N]`
- Pourquoi **`lea` est partout** dans le code compilé
- Utiliser `lea` pour des **additions/multiplications rapides**
- Que les **échelles valides** sont 1, 2, 4 ou 8
- Reconnaître `lea` en **reverse engineering**

---


# PARTIE V — ENTRÉES, SORTIES ET CONVERSIONS

---

# Chapitre 13 — Lire au clavier avec `read`

## Le minimum à savoir

### Le syscall `read` (numéro 0)

Symétrique de `write`, le syscall **`read`** lit des octets depuis un file descriptor (généralement le clavier).

| Argument | Registre | Exemple |
|----------|----------|---------|
| numéro de syscall | `rax` | `0` (= read) |
| file descriptor | `rdi` | `0` (= stdin) |
| adresse du buffer | `rsi` | `buffer` |
| nombre max d'octets | `rdx` | `64` |

Après l'appel :
- **`rax`** contient le **nombre d'octets effectivement lus** (ou un nombre négatif en cas d'erreur).

### Préparer un buffer dans `.bss`

```nasm
section .bss
    buffer  resb 64       ; 64 octets vides pour stocker la saisie
```

### Lire et réafficher : ton premier programme interactif

Crée `echo.asm` :

```nasm
; echo.asm — Lit une ligne et la réaffiche

section .data
    prompt    db "Tape quelque chose : ", 0
    prompt_l  equ $ - prompt - 1     ; -1 pour ne pas inclure le 0 final

section .bss
    buffer    resb 64
    nb_lus    resq 1

section .text
global _start
_start:
    ; ─── Afficher le prompt ───
    mov rax, 1                ; write
    mov rdi, 1                ; stdout
    mov rsi, prompt
    mov rdx, prompt_l
    syscall

    ; ─── Lire la saisie ───
    mov rax, 0                ; read
    mov rdi, 0                ; stdin
    mov rsi, buffer
    mov rdx, 64               ; max 64 octets
    syscall

    ; rax contient maintenant le nombre d'octets lus
    mov [nb_lus], rax         ; on le mémorise

    ; ─── Réafficher ───
    mov rax, 1                ; write
    mov rdi, 1                ; stdout
    mov rsi, buffer
    mov rdx, [nb_lus]         ; on réutilise le nombre d'octets lus
    syscall

    ; ─── Quitter ───
    mov rax, 60
    mov rdi, 0
    syscall
```

Exécution :

```
$ ./echo
Tape quelque chose : Bonjour
Bonjour
```

> **Important :** quand tu tapes `Bonjour` + Entrée, le **retour ligne fait partie** des octets lus. C'est pour ça que la sortie se met à la ligne automatiquement.

### `rax` après `read` : c'est crucial

Tu **dois** récupérer `rax` après `read` parce que :
- Tu ne sais pas combien l'utilisateur a tapé.
- Tu vas vouloir afficher exactement cette quantité.
- Si tu mets `rdx = 64` pour le `write`, tu afficheras des **octets garbage** en plus de la saisie.

```nasm
mov rax, 0
mov rdi, 0
mov rsi, buffer
mov rdx, 64
syscall                ; rax = nombre lus (typiquement entre 1 et 64)

mov [nb_lus], rax      ; mémoriser pour plus tard
```

### Le retour ligne est lu

Si tu tapes `abc` + Entrée, le buffer contient `'a'`, `'b'`, `'c'`, `'\n'` (4 octets). Si tu veux **enlever** le retour ligne, il faut soustraire 1 à `nb_lus` ou modifier le buffer. Ça viendra avec les boucles (chapitre 17).

## Très utile en pratique

### Que faire si l'utilisateur ne tape rien ?

S'il appuie juste sur Entrée, `read` lit 1 octet (le `\n`) et retourne 1. Si stdin est fermé (Ctrl+D), `read` retourne 0. Si une erreur survient, `read` retourne une valeur **négative** (par exemple `-1`). On apprendra à tester ça au chapitre 16.

### Buffer trop petit ?

Si tu réserves 10 octets et que l'utilisateur tape 20 caractères, **seulement 10** seront lus. Les autres restent dans le tampon de stdin et seront lus à la prochaine lecture. Pas de crash, mais comportement à connaître.

### Buffer trop grand ?

Si tu réserves 1000 octets et que l'utilisateur tape "abc", `read` lit juste 4 octets (`abc\n`). `rax` te dit combien. **Aucun problème.**

## Bonus

### Lire un seul caractère

```nasm
mov rax, 0
mov rdi, 0
mov rsi, buffer
mov rdx, 1            ; max 1 octet
syscall
```

Pratique pour des menus simples (l'utilisateur tape `1`, `2`, `3`…).

### Lire silencieusement (ex: mots de passe)

Pas trivial en assembleur pur — il faut utiliser `tcsetattr` pour désactiver l'écho. Hors scope de ce cours, mais sache que c'est possible.

## ❌ Erreur classique

```
Oublier de récupérer rax après read
→ Tu ne sais pas combien d'octets sont valides dans le buffer.

Mettre rdx fixe pour le write au lieu de [nb_lus]
→ Tu affiches du garbage en plus de la saisie.

Buffer trop petit ET ne pas tester si nb_lus >= taille_max
→ Pas grave dans ce cours, mais à savoir pour la suite.

Lire avant d'avoir affiché le prompt
→ L'utilisateur ne sait pas qu'on attend une saisie. Toujours prompt → read.

Croire que read renvoie la chaîne directement
→ NON. Read remplit le buffer, et rax contient le nombre d'octets lus.

Oublier que '\n' est lu
→ Si l'utilisateur tape "abc", nb_lus = 4 (abc + \n).
```

## Exercices

**Guidé :** Recopie et exécute `echo.asm` ci-dessus. Vérifie que ce que tu tapes est bien réaffiché.

**Autonome :** Modifie `echo.asm` pour afficher d'abord `"Tu as ecrit : "` avant la saisie réaffichée.

**Défi :** Crée un programme qui affiche **deux fois** ce que l'utilisateur a tapé (en gros : `echo echo`).

## 🧩 Mini-projet (chapitre 13) — Mini-shell d'accueil

Crée `accueil.asm` qui :

1. Affiche `"Quel est ton prenom ? "` (sans retour ligne après).
2. Lit la saisie utilisateur.
3. Affiche `"Bonjour, "`.
4. Réaffiche le prénom saisi.

Exécution attendue :

```
$ ./accueil
Quel est ton prenom ? Alice
Bonjour, Alice
```

> **Note :** le retour ligne après "Alice" vient du `\n` qui a été lu avec la saisie. C'est OK.

## ✅ Tu sais maintenant…

- Utiliser le syscall **`read`** (n°0)
- La symétrie **`write`** ↔ **`read`** (même conventions)
- Le rôle du **file descriptor 0** (stdin)
- Pourquoi récupérer **`rax`** après `read`
- Préparer un **buffer dans `.bss`**
- Que le **retour ligne** fait partie de ce qui est lu
- Écrire un premier programme **interactif**

---

# Chapitre 14 — Convertir texte et nombres

## Le minimum à savoir

### Le problème : `'5'` ≠ `5`

Si l'utilisateur tape `5`, le buffer contient l'**octet 53** (le code ASCII de `'5'`), pas le nombre 5. Tenter de calculer `[buffer] + 1` te donnerait 54 (`'6'`), pas 6.

> **Confusion classique du débutant.** Mémorise : le caractère `'5'` vaut **53** en mémoire. Pour avoir le nombre 5, il faut **soustraire 48** (le code de `'0'`).

### Convertir un caractère en chiffre

```nasm
mov al, '5'          ; al = 0x35 = 53
sub al, '0'          ; al = 53 - 48 = 5
```

Ou de façon équivalente :

```nasm
sub al, 0x30
```

Ces deux écritures sont identiques. La 1ère est plus lisible.

### Convertir un chiffre en caractère

L'opération inverse :

```nasm
mov al, 7            ; al = 7
add al, '0'          ; al = 7 + 48 = 55 = '7'
```

### Vérifier que c'est bien un chiffre

Avant de soustraire `'0'`, il vaut mieux vérifier que c'est entre `'0'` et `'9'`. On verra comment au chapitre 16 (avec `cmp` et les sauts).

### Cas simple : lire et afficher un chiffre + 1

```nasm
; chiffre.asm — Lit un chiffre, ajoute 1, l'affiche

section .data
    prompt   db "Tape un chiffre (0-9) : ", 0
    prompt_l equ $ - prompt - 1

section .bss
    buffer  resb 4

section .text
global _start
_start:
    ; afficher le prompt
    mov rax, 1
    mov rdi, 1
    mov rsi, prompt
    mov rdx, prompt_l
    syscall

    ; lire 2 octets (un chiffre + le \n)
    mov rax, 0
    mov rdi, 0
    mov rsi, buffer
    mov rdx, 2
    syscall

    ; convertir le caractère en nombre
    mov al, [buffer]       ; al = code ASCII du chiffre
    sub al, '0'            ; al = chiffre réel (0-9)
    inc al                 ; al = chiffre + 1
    add al, '0'            ; al = code ASCII du résultat
    mov [buffer], al       ; remplacer le 1er octet du buffer

    ; afficher le résultat (1 octet)
    mov rax, 1
    mov rdi, 1
    mov rsi, buffer
    mov rdx, 1
    syscall

    ; un retour ligne pour faire propre
    mov byte [buffer], 10
    mov rax, 1
    mov rdi, 1
    mov rsi, buffer
    mov rdx, 1
    syscall

    mov rax, 60
    mov rdi, 0
    syscall
```

Sortie :

```
Tape un chiffre (0-9) : 4
5
```

🎉 **Tu viens de coder une mini-calculatrice à 1 chiffre.**

### Et pour plusieurs chiffres ?

Convertir une chaîne comme `"123"` en l'entier 123 demande **une boucle** : on parcourt chaque chiffre, on accumule. L'algorithme :

```
résultat = 0
pour chaque chiffre c :
    résultat = résultat * 10 + (c - '0')
```

Sans boucle (ch. 17), on ne peut pas encore le coder. On va y revenir.

### Algorithme inverse : nombre → chaîne

C'est encore plus tordu. Pour transformer 123 en `"123"` :

```
si nombre == 0 → afficher '0'
sinon, tant que nombre > 0 :
    chiffre = nombre % 10
    caractère = chiffre + '0'
    stocker dans buffer (à l'envers !)
    nombre = nombre / 10
puis afficher buffer dans l'ordre inverse
```

C'est pourquoi on dit qu'**afficher un nombre en ASM est non trivial**. On en fera un mini-projet de boucles (ch. 17).

## Très utile en pratique

### Code ASCII des chiffres : à connaître par cœur

| Caractère | Décimal | Hexa |
|-----------|---------|------|
| `'0'` | 48 | `0x30` |
| `'1'` | 49 | `0x31` |
| `'2'` | 50 | `0x32` |
| `'9'` | 57 | `0x39` |

Donc :
- Pour **caractère → chiffre** : `sub al, 48` (ou `sub al, '0'`).
- Pour **chiffre → caractère** : `add al, 48` (ou `add al, '0'`).

### Petite astuce mémo : la différence est toujours `0x30`

`'0' = 0x30`, `'1' = 0x31`, … `'9' = 0x39`. La différence entre le chiffre et son ASCII est **toujours 0x30 = 48**.

### Avec d'autres caractères

Même logique pour les lettres :

```nasm
; transformer 'A'..'Z' en 'a'..'z'
sub al, 'A'         ; al = 0..25
add al, 'a'         ; al = 'a'..'z'
; ou plus directement :
add al, 0x20        ; +32 = passe en minuscule
```

## Bonus

### Pourquoi `'0'` vaut 48 et pas 0 ?

Historiquement, ASCII range les caractères affichables après les codes de contrôle (0-31). Les chiffres viennent à `48-57`, les majuscules à `65-90`, les minuscules à `97-122`. La table est conçue pour que :
- Toutes les minuscules diffèrent de leur majuscule de exactement **32**.
- Les chiffres `'0'-'9'` se suivent.

C'est cette ergonomie qui rend les conversions si simples avec `sub` et `add`.

## ❌ Erreur classique

```
Additionner '5' + 3 et croire qu'on obtient '8'
→ '5' + 3 = 53 + 3 = 56 = '8'. OK !
→ Mais '5' + '3' = 53 + 51 = 104 ≠ '8'. Piège classique.

Oublier de convertir avant de faire un calcul
→ "5" en buffer = 53. "5" + 1 = 54 = '6' (heureusement, mais c'est par chance).

Oublier add '0' avant d'afficher un chiffre
→ Tu affiches un caractère de contrôle (invisible) au lieu d'un chiffre.

Croire que read renvoie un entier
→ NON. read renvoie un texte (octets). Toi de convertir.

Confondre la longueur du buffer et le nombre lu
→ Toujours utiliser rax (renvoyé par read) pour la longueur.
```

## Exercices

**Guidé :** Reprends et exécute `chiffre.asm` ci-dessus. Teste avec différents chiffres.

**Autonome :** Modifie le programme pour qu'il **double** le chiffre saisi (au lieu d'ajouter 1). Attention : si tu saisis 5, ça donne 10, qui ne tient plus sur un seul chiffre. **Limite ton test** à des saisies de 0 à 4 pour l'instant.

**Défi :** Écris un programme qui demande **deux** chiffres (en deux saisies successives via `read`) et affiche leur somme (si elle reste < 10).

## 🧩 Mini-projet (chapitres 13-14) — Addition à 1 chiffre

Crée `add_chiffres.asm` qui :

1. Affiche `"Premier chiffre : "`.
2. Lit (read avec rdx=2 pour avoir chiffre + \n).
3. Convertit (sub '0') et stocke dans une variable `a` en `.bss`.
4. Affiche `"Deuxieme chiffre : "`.
5. Lit, convertit, stocke dans `b`.
6. Calcule `a + b` (résultat dans `al`).
7. Reconvertit en ASCII (`add '0'`).
8. Affiche le résultat suivi d'un retour ligne.

> **Limitation :** ne fonctionnera correctement que si la somme est ≤ 9.

## ✅ Tu sais maintenant…

- Que `'5'` ≠ `5` : un caractère est un code ASCII
- Convertir **caractère → chiffre** avec `sub al, '0'`
- Convertir **chiffre → caractère** avec `add al, '0'`
- Lire un chiffre saisi et le manipuler comme un nombre
- Pourquoi convertir un **entier multi-chiffres** demande une boucle
- Que tu sais maintenant écrire des programmes **vraiment interactifs**

---

# Chapitre 15 — Fichiers et syscalls utiles

## Le minimum à savoir

### Au-delà de stdin/stdout

Tu sais lire le clavier et écrire à l'écran. Mais comment **lire un fichier** ou **écrire dans un fichier** ? Réponse : avec d'autres syscalls.

### Les 5 syscalls de gestion de fichiers

| Syscall | Numéro | Rôle |
|---------|--------|------|
| **`open`** | 2 | Ouvre un fichier, renvoie un file descriptor (fd) |
| **`read`** | 0 | Lit depuis un fd |
| **`write`** | 1 | Écrit dans un fd |
| **`close`** | 3 | Ferme un fd |
| **`lseek`** | 8 | Déplace le curseur dans un fichier |

### Le syscall `open` (numéro 2)

> **Note :** dans les programmes Linux modernes et dans la libc d'aujourd'hui, on rencontre **souvent `openat`** (syscall n°257) plutôt que `open` — notamment dans les programmes compilés avec une libc récente, où c'est devenu la norme. Le principe reste identique : obtenir un file descriptor pour un fichier. `openat` accepte juste un répertoire de base en argument supplémentaire. Pour ce cours, on reste sur `open` qui est plus simple à manipuler. **En reverse engineering moderne, sois prêt à croiser `openat` plus souvent que `open`.**

Arguments :

| Argument | Registre | Exemple |
|----------|----------|---------|
| numéro | `rax` | `2` |
| chemin du fichier | `rdi` | adresse de la chaîne du chemin (terminée par 0) |
| flags (mode d'ouverture) | `rsi` | voir tableau ci-dessous |
| permissions (si création) | `rdx` | `420` (= `0o644` en décimal) typiquement |

Valeurs courantes de `rsi` (flags) :

| Flag | Valeur | Effet |
|------|--------|-------|
| `O_RDONLY` | 0 | Lecture seule |
| `O_WRONLY` | 1 | Écriture seule |
| `O_RDWR` | 2 | Lecture/écriture |
| `O_CREAT` | 0x40 (= 64) | Créer si n'existe pas (combiner avec autre flag) |
| `O_TRUNC` | 0x200 (= 512) | Tronquer (vider) si existe |
| `O_APPEND` | 0x400 (= 1024) | Ajouter à la fin |

On les **combine avec OR bit-à-bit** (que NASM accepte avec `|`) :

```nasm
mov rsi, 1 | 64 | 512    ; O_WRONLY | O_CREAT | O_TRUNC
```

### `open` renvoie un fd

Après `open`, `rax` contient :
- Un **fd positif** (un entier ≥ 3) si tout s'est bien passé. **Mémorise-le**.
- Une **valeur négative** si erreur (`-1`, `-2`, etc.).

### Lire un fichier complet : `cat.asm`

```nasm
; cat.asm — Mini-cat : lit un fichier (chemin codé en dur) et l'affiche

section .data
    chemin db "/etc/hostname", 0

section .bss
    fd     resq 1
    buffer resb 1024

section .text
global _start
_start:
    ; ─── open(chemin, O_RDONLY) ───
    mov rax, 2              ; syscall open
    mov rdi, chemin
    mov rsi, 0              ; O_RDONLY
    mov rdx, 0
    syscall

    mov [fd], rax           ; mémoriser le fd

    ; ─── read(fd, buffer, 1024) ───
    mov rax, 0              ; syscall read
    mov rdi, [fd]
    mov rsi, buffer
    mov rdx, 1024
    syscall

    ; rax = nombre d'octets lus
    mov r12, rax            ; on sauvegarde dans r12

    ; ─── write(stdout, buffer, r12) ───
    mov rax, 1
    mov rdi, 1
    mov rsi, buffer
    mov rdx, r12
    syscall

    ; ─── close(fd) ───
    mov rax, 3
    mov rdi, [fd]
    syscall

    ; ─── exit(0) ───
    mov rax, 60
    mov rdi, 0
    syscall
```

Exécute :

```
$ ./cat
mon-pc
```

🎉 **Tu viens de coder un mini-`cat` qui lit un vrai fichier.**

### Écrire dans un fichier

Même principe, avec `O_WRONLY | O_CREAT | O_TRUNC` et un mode (permissions Unix `0644`, soit `420` en décimal) :

```nasm
section .data
    nom     db "sortie.txt", 0
    contenu db "Salut depuis l'assembleur !", 10
    contenu_l equ $ - contenu

section .bss
    fd resq 1

section .text
global _start
_start:
    ; open(nom, O_WRONLY|O_CREAT|O_TRUNC, 0644)
    mov rax, 2
    mov rdi, nom
    mov rsi, 1 | 64 | 512
    mov rdx, 420             ; permissions 0644 en décimal (rw-r--r--)
    syscall
    mov [fd], rax

    ; write(fd, contenu, len)
    mov rax, 1
    mov rdi, [fd]
    mov rsi, contenu
    mov rdx, contenu_l
    syscall

    ; close(fd)
    mov rax, 3
    mov rdi, [fd]
    syscall

    ; exit(0)
    mov rax, 60
    mov rdi, 0
    syscall
```

Après exécution :

```
$ cat sortie.txt
Salut depuis l'assembleur !
```

### Toujours fermer ce qu'on a ouvert

Comme en Python (`f.close()`), on **doit** fermer ce qu'on ouvre. Sinon, fuite de descripteurs (le système en a un nombre limité).

## Très utile en pratique

### Détecter une erreur de syscall

Tous les syscalls renvoient :
- Une **valeur positive ou zéro** en cas de succès (selon le syscall).
- Une **valeur négative** en cas d'erreur (entre -1 et environ -4095).

```nasm
mov rax, 2          ; open
mov rdi, chemin
mov rsi, 0
syscall

cmp rax, 0
jl erreur           ; saut si rax < 0 (chapitre 16)
```

Pour tester ça proprement, il faut connaître les sauts conditionnels (chapitre suivant).

### Buffers et lecture par blocs

Si tu lis un fichier plus grand que ton buffer, **un seul `read` ne suffira pas**. Il faut **boucler** :

```
tant que read renvoie > 0 :
    écrire ce qu'on a lu
    relancer read
```

C'est exactement ce que fait `cat`. On le fera proprement après les boucles (ch. 17).

## Bonus

### Le syscall `lseek` (numéro 8)

`lseek` permet de **déplacer le curseur** dans un fichier (utile pour relire le début ou sauter une portion).

| Argument | Registre |
|----------|----------|
| numéro | `rax = 8` |
| fd | `rdi` |
| décalage | `rsi` |
| origine | `rdx` (0 = début, 1 = position actuelle, 2 = fin) |

### Erreurs typiques de `open`

| Code (valeur) | Signification |
|---------------|---------------|
| `-2` | Fichier introuvable (ENOENT) |
| `-13` | Permission refusée (EACCES) |
| `-17` | Fichier existe déjà (EEXIST), avec O_CREAT \| O_EXCL |

## ❌ Erreur classique

```
Oublier le 0 final du chemin
→ open() reçoit une chaîne corrompue. Erreur de fichier introuvable.

Oublier de fermer un fichier
→ Fuite. Pas grave pour un petit programme, mais mauvaise habitude.

Ignorer la valeur de retour
→ Tu manipules un fd invalide. Comportement indéfini.

Mauvaises permissions (rdx mal mis)
→ Le fichier sera créé sans droits d'écriture. Embêtant.

Oublier O_TRUNC quand on écrit dans un fichier existant
→ Le nouveau contenu se mélange à l'ancien.

Ne pas mémoriser le fd dans une variable
→ Si tu fais d'autres opérations, rax aura changé. Stocke-le.
```

## Exercices

**Guidé :** Crée `cat.asm` comme ci-dessus, mais en lisant un fichier que tu crées avec `echo "Bonjour" > test.txt`. Adapte le chemin dans le `.asm`.

**Autonome :** Écris un programme qui crée un fichier `salut.txt` contenant la chaîne `"Salut\n"`. Vérifie avec `cat salut.txt` que ça fonctionne.

**Défi :** Écris un programme qui :
1. Ouvre `test.txt` en lecture.
2. Lit son contenu (jusqu'à 256 octets) dans un buffer.
3. **Écrit ce contenu** dans `copie.txt`.
4. Ferme les deux fichiers.

C'est l'équivalent de `cp test.txt copie.txt` (pour les petits fichiers).

## 🧩 Mini-projet (chapitres 13-15) — Mini-cat avec saisie

Crée `cat_input.asm` qui :

1. Demande à l'utilisateur de taper du texte.
2. Le lit avec `read`.
3. L'écrit dans un fichier nommé `sortie.txt`.
4. Affiche un message de confirmation à l'écran.

Exemple :

```
$ ./cat_input
Tape un texte : Bonjour le monde
Texte sauvegarde dans sortie.txt
$ cat sortie.txt
Bonjour le monde
```

> **Limitation :** ne gère qu'une seule ligne (jusqu'à 1024 octets). C'est OK.

## ✅ Tu sais maintenant…

- Ouvrir un fichier avec **`open`** (numéro 2)
- Comprendre les **flags** : `O_RDONLY`, `O_WRONLY`, `O_CREAT`, `O_TRUNC`, etc.
- Récupérer un **file descriptor** dans `rax`
- Le **mémoriser** dans une variable
- Lire et écrire dans un fichier via `read`/`write` avec ce fd
- **Fermer** proprement avec `close` (numéro 3)
- Détecter (à venir) une erreur via une **valeur négative**
- Coder un **mini-`cat`** en assembleur pur

---

## 🚩 Checkpoint — Fin de la Partie V

À ce stade, tu sais écrire un vrai programme interactif. Vérifie que tu peux :

- [ ] Lire une saisie utilisateur avec `read` et récupérer le nombre d'octets lus.
- [ ] Convertir un caractère ASCII en chiffre (et vice-versa).
- [ ] Ouvrir, lire, écrire et fermer un fichier avec `open`, `read`, `write`, `close`.
- [ ] Comprendre pourquoi `'5'` ≠ `5`.
- [ ] Mémoriser un file descriptor dans une variable `.bss`.
- [ ] Identifier qu'un syscall a échoué (valeur négative dans `rax`).

**Si tu sais faire tout ça, tu maîtrises les I/O bas niveau de Linux.** La suite (logique, fonctions, reverse) s'appuie là-dessus.

---


# PARTIE VI — LOGIQUE ET CONTRÔLE DE FLUX

---

# Chapitre 16 — Comparaisons, flags et sauts

## Le minimum à savoir

### Pourquoi ce chapitre est central

Jusqu'ici, tes programmes s'exécutent **toujours dans le même ordre**, de haut en bas. C'est ce qu'on appelle un programme **séquentiel**. Mais un vrai programme doit pouvoir **décider** : "si l'utilisateur tape oui, affiche ceci ; sinon, affiche cela". C'est ce qu'on appelle un **`if`** en Python ou Bash.

> **À retenir :** ce chapitre est **le pivot** du cours. Une fois que tu sais comparer et sauter, tu peux écrire de **vrais** programmes.

### `cmp` : la comparaison

L'instruction **`cmp a, b`** fait deux choses :

1. Elle calcule **`a - b`** mentalement.
2. Elle **ne stocke pas** le résultat — elle met juste à jour les **drapeaux (flags)** du CPU.

```nasm
cmp rax, rbx     ; compare rax et rbx (ne modifie rien)
```

C'est comme dire au CPU : "regarde ces deux valeurs, mémorise leur relation". Aucun registre n'est changé. Seuls les flags bougent.

### Les flags : les petits indicateurs du CPU

Le CPU a un **registre de flags** (`rflags`) avec plusieurs bits indicateurs. Les 4 importants pour démarrer :

| Flag | Nom | Signification |
|------|-----|---------------|
| **`ZF`** | Zero Flag | Mis à 1 si le résultat est **zéro** (donc si `a == b`) |
| **`SF`** | Sign Flag | Mis à 1 si le résultat est **négatif** (bit de signe = 1) |
| **`CF`** | Carry Flag | Mis à 1 en cas de **retenue** (utile pour les non signés) |
| **`OF`** | Overflow Flag | Mis à 1 en cas de **débordement signé** |

> **Pas de panique.** Tu n'as pas besoin de tout maîtriser. Les **sauts conditionnels** vont lire ces flags à ta place. Tu choisis juste le bon saut.

### `jmp` : saut inconditionnel

`jmp etiquette` saute **toujours** vers cette étiquette, peu importe les flags :

```nasm
    mov rax, 1
    jmp fin            ; saute par-dessus le code suivant
    mov rax, 999       ; ← jamais exécuté
fin:
    mov rax, 60
    syscall
```

### Sauts conditionnels : la suite logique

Après un `cmp`, tu peux sauter **selon le résultat** :

| Saut | Condition | Équivalent Python |
|------|-----------|-------------------|
| **`je`** | si égal (`==`) | `if a == b` |
| **`jne`** | si non égal (`!=`) | `if a != b` |
| **`jl`** | si **inférieur** (signé) | `if a < b` |
| **`jle`** | si inférieur ou égal | `if a <= b` |
| **`jg`** | si supérieur (signé) | `if a > b` |
| **`jge`** | si supérieur ou égal | `if a >= b` |
| **`jb`** | si inférieur (**non signé**) | (pour entiers non signés) |
| **`ja`** | si supérieur (**non signé**) | (pour entiers non signés) |

> **Règle d'or :** `jl/jg/jle/jge` pour les nombres **signés** (qui peuvent être négatifs). `jb/ja/jbe/jae` pour les nombres **non signés** (toujours positifs, ex : tailles, adresses).

### Premier `if` en assembleur

Voici l'équivalent ASM de :
```python
if x == 42:
    exit(1)
else:
    exit(0)
```

En assembleur :

```nasm
section .data
    x dq 42

section .text
global _start
_start:
    mov rax, [x]
    cmp rax, 42        ; comparer rax et 42
    je egal            ; si rax == 42, saute à 'egal'

    ; bloc "else"
    mov rdi, 0
    jmp sortie

egal:
    ; bloc "if"
    mov rdi, 1

sortie:
    mov rax, 60
    syscall
```

Exécution : `./prog ; echo $?` → affiche `1` (car `x == 42`). Change `x dq 41`, recompile : ça affichera `0`.

### Le piège du sens de `cmp`

`cmp a, b` fait `a - b`. Donc :

- `cmp rax, 10` + `jl ...` → saute si **`rax < 10`** (et non `10 < rax`).

Lis-le en français : "compare rax avec 10, saute si **rax est inférieur**". Comme `mov`, c'est destination/sujet à gauche, valeur de comparaison à droite.

### Pattern `if`/`else` classique

Voici le **squelette à mémoriser** :

```nasm
    cmp rax, rbx
    je egal            ; ← saute si vrai

    ; CODE DU "ELSE" ici
    ; ...
    jmp fin            ; ← ne pas exécuter le "if"

egal:
    ; CODE DU "IF" ici
    ; ...

fin:
    ; suite du programme
```

### Pattern `if` (sans `else`)

Si tu n'as pas de "sinon", c'est plus simple :

```nasm
    cmp rax, 0
    jne pas_zero       ; saute si rax != 0

    ; CODE SI rax == 0 ici
    ; ...

pas_zero:
    ; suite du programme
```

## Très utile en pratique

### Comparer un registre à zéro : `test`

Pour tester si un registre vaut 0, on utilise souvent **`test`** au lieu de `cmp` :

```nasm
test rax, rax          ; met ZF=1 si rax == 0
jz fin                 ; saute si rax == 0 (jz = je)
```

`test a, a` fait `a AND a`, ce qui donne `a`. Donc ZF=1 ssi `a == 0`. C'est un idiome **très courant** en reverse engineering. Quand tu vois `test eax, eax / je ...`, c'est `if (eax == 0)`.

### Tableau de correspondance complet

| Python | Assembleur |
|--------|------------|
| `if a == b: …` | `cmp a, b ; je …` |
| `if a != b: …` | `cmp a, b ; jne …` |
| `if a < b: …`  | `cmp a, b ; jl …` (signé) |
| `if a > b: …`  | `cmp a, b ; jg …` (signé) |
| `if a == 0: …` | `test a, a ; jz …` |
| `if a != 0: …` | `test a, a ; jnz …` |

### Détecter une erreur de syscall

Tu te souviens : les syscalls renvoient une valeur négative en cas d'erreur. Maintenant tu peux tester :

```nasm
mov rax, 2          ; open
mov rdi, chemin
mov rsi, 0
syscall

cmp rax, 0
jl erreur           ; rax < 0 → erreur

; suite normale
; ...
jmp fin

erreur:
; afficher un message d'erreur
; ...

fin:
```

## Bonus

### Voir les flags dans GDB

```
(gdb) info registers eflags
eflags  0x202  [ IF ]
```

Avec pwndbg, les flags sont **affichés en clair** à chaque pas, avec le nom des bits actifs (ZF, SF, CF, OF…). Encore une raison de l'installer.

### Sauts conditionnels rares mais utiles

| Saut | Effet |
|------|-------|
| `jz` / `jnz` | Synonymes de `je` / `jne` (saut si zéro / non zéro) |
| `js` / `jns` | Saut si négatif / positif (Sign Flag) |
| `jc` / `jnc` | Saut si Carry / no Carry |
| `jo` / `jno` | Saut si Overflow / no Overflow |

`jz`/`jnz` sont **identiques** à `je`/`jne` (juste un autre nom). Tu les verras tous les deux dans du code désassemblé.

## ❌ Erreur classique

```
Inverser les opérandes de cmp
→ cmp rax, 10 et "saute si inférieur" = rax < 10 (pas 10 < rax).

Utiliser jl quand il faut jb (ou inversement)
→ jl/jg pour signé, jb/ja pour non signé. Si tu manipules une taille
  ou une adresse, c'est jb/ja.

Oublier de sauter après le bloc "if" → tomber dans le "else"
→ Toujours mettre jmp fin à la fin du "if".

Confondre je et jmp
→ jmp = inconditionnel. je = seulement si égal.

Croire que cmp modifie un registre
→ Non, cmp modifie seulement les flags.

Faire un calcul entre cmp et le saut
→ Le calcul écrase les flags. Toujours cmp puis directement jXX.

Mettre des labels en double dans le même fichier
→ Erreur du linker. Utilise des labels uniques (préfixe avec un point
  pour les labels locaux : .boucle, .fin).
```

## Exercices

**Guidé :** Crée `if.asm` qui :
- charge `x dq 50`
- si `x > 30`, sort avec code 1
- sinon, sort avec code 0

Teste avec différentes valeurs de `x`.

**Autonome :** Crée un programme qui charge `x dq -5` (déclare-le comme `dq -5`) et :
- sort avec code 1 si `x < 0`
- sort avec code 2 si `x == 0`
- sort avec code 3 si `x > 0`

> **Indice :** deux `cmp` + sauts en cascade.

**Défi :** Modifie le mini-`cat` du chapitre 15 pour qu'il affiche `"Erreur"` (sur stderr) si `open` renvoie une valeur négative, au lieu de continuer.

## 🧩 Mini-projet (chapitre 16) — Comparaison de deux nombres

Crée `compare.asm` qui :

1. Déclare `a dq 25` et `b dq 17` dans `.data`.
2. Compare les deux valeurs.
3. Affiche un des trois messages :
   - `"A est plus grand"`
   - `"B est plus grand"`
   - `"A et B sont egaux"`
4. Quitte avec code 0.

Tu auras besoin de trois messages dans `.data`, et de **trois branches** (`jg`, `jl`, et le cas d'égalité par défaut).

## ✅ Tu sais maintenant…

- Ce qu'est un **flag** (ZF, SF, CF, OF)
- Comparer avec **`cmp a, b`** (qui calcule `a - b` et met à jour les flags)
- Sauter inconditionnellement avec **`jmp`**
- Sauter conditionnellement : **`je, jne, jl, jg, jle, jge, jb, ja, jbe, jae`**
- La différence **signé** (`jl, jg`) vs **non signé** (`jb, ja`)
- Le pattern **`test rax, rax / jz`** pour tester contre zéro
- Écrire un **`if/else` complet** en ASM

---

# Chapitre 17 — Boucles

## Le minimum à savoir

### Une boucle, c'est juste un `if` + un saut arrière

En Python :
```python
i = 0
while i < 10:
    print(i)
    i += 1
```

En assembleur, c'est l'**exact même schéma**, mais explicite :

```nasm
    mov rcx, 0          ; i = 0
.boucle:
    cmp rcx, 10
    jge .fin            ; si i >= 10, sortir
    ; ... corps de la boucle (utiliser rcx) ...
    inc rcx             ; i++
    jmp .boucle         ; recommencer
.fin:
```

> **À retenir :** une boucle = un **label de début**, une **condition de sortie**, un **corps**, une **mise à jour du compteur**, et un **saut arrière** vers le label.

### Les labels locaux `.foo`

NASM permet d'utiliser des labels **locaux** commençant par un point. Ces labels sont liés au dernier label "principal" :

```nasm
_start:
.boucle:           ; label local lié à _start
    ; ...
    jmp .boucle
.fin:

autre_fonction:
.boucle:           ; AUTRE label local, lié à 'autre_fonction'
    ; ...
```

Ça permet de réutiliser des noms comme `.boucle`, `.fin`, `.suivant` dans plusieurs endroits sans collision. **Utilise les labels locaux pour les boucles.**

### Boucle `for` : compter de 0 à N-1

Le pattern le plus courant :

```nasm
    mov rcx, 0          ; i = 0
.boucle:
    cmp rcx, 10
    jge .fin            ; condition de sortie
    ; ... corps ...
    inc rcx
    jmp .boucle
.fin:
```

### Boucle `while` : tant que…

Très similaire, mais la condition est différente :

```nasm
    mov rcx, [valeur]
.boucle:
    test rcx, rcx
    jz .fin             ; tant que rcx != 0
    ; ... corps ...
    dec rcx
    jmp .boucle
.fin:
```

### Boucle infinie (à éviter en accident !)

```nasm
.boucle:
    ; ... rien qui sorte ...
    jmp .boucle
```

Ça tourne pour toujours. Si tu lances ça sans le faire exprès : **Ctrl+C** pour tuer le programme.

### Exemple complet : compter de 0 à 9 avec affichage

```nasm
; compte.asm — Affiche les chiffres 0 à 9

section .bss
    chiffre resb 2          ; 1 octet pour le chiffre + 1 pour \n

section .text
global _start
_start:
    mov byte [chiffre + 1], 10    ; le \n est fixe

    mov rcx, 0
.boucle:
    cmp rcx, 10
    jge .fin

    ; convertir rcx (chiffre) en ASCII
    mov rax, rcx
    add al, '0'
    mov [chiffre], al

    ; afficher 2 octets (chiffre + \n)
    push rcx              ; ← sauvegarder rcx (write va l'écraser)
    mov rax, 1
    mov rdi, 1
    mov rsi, chiffre
    mov rdx, 2
    syscall
    pop rcx               ; ← restaurer rcx

    inc rcx
    jmp .boucle

.fin:
    mov rax, 60
    mov rdi, 0
    syscall
```

> **Tu remarques `push rcx` / `pop rcx` ?** C'est parce que `syscall` peut écraser `rcx`. Pour préserver notre compteur, on l'empile avant et on le récupère après. On approfondit la pile au **chapitre 18**.

Compile et exécute :

```
$ ./compte
0
1
2
3
4
5
6
7
8
9
```

### Parcourir un tableau

```nasm
section .data
    nombres dq 10, 20, 30, 40, 50
    taille  equ 5

section .text
global _start
_start:
    mov rcx, 0          ; index
    mov rax, 0          ; somme

.boucle:
    cmp rcx, taille
    jge .fin

    add rax, [nombres + rcx*8]   ; somme += nombres[rcx]
    inc rcx
    jmp .boucle

.fin:
    ; rax contient la somme = 150
    mov rdi, rax
    mov rax, 60
    syscall
```

`./prog ; echo $?` → `150`.

🎉 **Tu viens de coder ta première vraie boucle utile.**

## Très utile en pratique

### `break` et `continue` équivalents

Pas d'instructions dédiées comme en Python, mais on les simule avec `jmp` :

- `break` → `jmp .fin`
- `continue` → `jmp .boucle` (sans le `inc`, attention à ne pas créer une boucle infinie !)

### L'instruction `loop` (à connaître mais à éviter)

`loop etiquette` décrémente `rcx` et saute à `etiquette` si `rcx != 0`. C'est très compact :

```nasm
    mov rcx, 10
.boucle:
    ; ... corps ...
    loop .boucle        ; rcx-- puis saute si rcx != 0
```

> **Détail technique utile en reverse :** `loop` ressemble fortement à `dec rcx ; jnz`, mais **contrairement à `dec`, `loop` ne modifie pas les flags**. C'est parfois utile pour conserver l'état d'une comparaison précédente à travers la boucle.

Mais :
- Ça **impose** d'utiliser `rcx`.
- Ça oblige à compter **à l'envers** (10, 9, 8, …).
- C'est moins lisible et moins flexible.

> **Conseil :** retiens que `loop` existe (tu le verras en reverse), mais utilise le pattern `cmp + jXX` en pratique.

### Compter à l'envers

Souvent plus efficace en ASM :

```nasm
    mov rcx, 10
.boucle:
    ; corps qui utilise rcx (de 10 à 1)
    dec rcx
    jnz .boucle         ; saute si rcx != 0
```

Pas de `cmp` nécessaire : `dec` met `ZF=1` quand le résultat atteint 0. Idiome très courant.

## Bonus

### Boucles imbriquées

```nasm
    mov rcx, 0          ; boucle externe : i
.ext:
    cmp rcx, 3
    jge .fin_ext
    mov rdx, 0          ; boucle interne : j
.int:
    cmp rdx, 3
    jge .fin_int
    ; corps : utiliser rcx et rdx
    inc rdx
    jmp .int
.fin_int:
    inc rcx
    jmp .ext
.fin_ext:
```

> **Attention :** une boucle interne **ne doit pas écraser** le compteur de la boucle externe. Utilise des registres différents (`rcx`, `rdx`, `r12`, …).

### Convertir un entier en chaîne ASCII (algo complet)

Maintenant qu'on a les boucles, on peut afficher un entier multi-chiffres. L'algorithme :

```
buffer[20], i = 19
si nombre == 0 → buffer[i--] = '0'
sinon, tant que nombre > 0 :
    chiffre = nombre % 10
    buffer[i--] = chiffre + '0'
    nombre = nombre / 10
afficher buffer à partir de l'index i+1
```

C'est une excellente boucle pour s'entraîner — et c'est exactement le sujet du mini-projet final de ce chapitre.

## ❌ Erreur classique

```
Oublier l'incrément (inc rcx)
→ Boucle infinie. Ctrl+C.

Mauvais sens de saut : jge au lieu de jl
→ Boucle qui ne tourne jamais, ou qui ne s'arrête jamais.

Oublier d'initialiser le compteur
→ rcx contient une valeur aléatoire au départ.

Écraser rcx dans le corps (par un syscall, un imul, etc.)
→ La boucle perd son compte. Sauvegarde avec push/pop ou utilise r12-r15.

Confondre cmp rcx, 10 (sortir quand rcx >= 10) avec jl (sortir quand rcx < 10)
→ Toujours penser : "sous quelle condition je sors ?".

Indexer en éléments au lieu d'en octets : [tab + rcx] au lieu de [tab + rcx*8]
→ Bug classique pour les tableaux de qword.

Utiliser loop avec autre chose que rcx
→ Impossible : loop n'utilise que rcx.
```

## Exercices

**Guidé :** Crée `etoiles.asm` qui affiche **10 étoiles** sur la même ligne (`**********`) puis un retour ligne.

> **Indice :** utilise un buffer de 1 octet contenant `'*'`, et une boucle qui appelle `write` 10 fois. Plus un `write` final pour le `\n`.

**Autonome :** Crée un programme qui calcule **la somme des entiers de 1 à 100** dans `rax`. Renvoie le résultat comme code de retour modulo 256 (donc `5050 % 256 = 186` — vérifie avec `echo $?`).

**Défi :** Crée un programme qui calcule **factorielle(5)** = 1×2×3×4×5 = 120. Renvoie via le code de retour.

## 🧩 Mini-projet (chapitres 16-17) — Statistiques d'un tableau

Crée `stats.asm` qui :

1. Déclare `tab dq 42, 7, 89, 23, 56, 1, 100, 31, 4, 67` (10 nombres).
2. Calcule **la somme** dans `r12`.
3. Calcule **le maximum** dans `r13`.
4. Calcule **le minimum** dans `r14`.
5. Affiche le maximum comme code de retour (le minimum et la somme ne tiennent pas dans 0-255, on les regarde via GDB).

> **Indices :**
> - Une seule boucle qui parcourt le tableau.
> - Initialise `r13` (max) avec le premier élément avant la boucle.
> - Initialise `r14` (min) avec le premier élément aussi.
> - À chaque tour, `cmp rax, r13` puis `jle .pas_nouveau_max` etc.

Résultat attendu : `echo $?` → `100`.

## ✅ Tu sais maintenant…

- Construire une **boucle `for`** ou **`while`** en ASM
- Utiliser des **labels locaux** (`.boucle`, `.fin`)
- **Parcourir un tableau** avec un index dans un registre
- Faire des **boucles imbriquées**
- Préserver le compteur avec **`push`/`pop`** quand nécessaire
- Reconnaître l'instruction **`loop`** (mais préférer le pattern manuel)
- Compter à l'envers avec **`dec` + `jnz`**

---


# PARTIE VII — PILE ET FONCTIONS

---

# Chapitre 18 — La pile avec `push`, `pop` et `rsp`

## Le minimum à savoir

### C'est quoi, la pile ?

La **pile** (en anglais : *stack*) est une zone spéciale de la mémoire RAM. Elle fonctionne comme **une pile d'assiettes** :

```
        ┌─────────┐ ← sommet (la dernière déposée)
        │  100    │
        ├─────────┤
        │   42    │
        ├─────────┤
        │   17    │
        └─────────┘ ← base
```

- Tu peux **déposer** (push) une assiette sur le dessus.
- Tu peux **prendre** (pop) celle du dessus.
- Tu ne peux **pas** prendre celle du milieu sans enlever les autres.

C'est ce qu'on appelle une structure **LIFO** : *Last In, First Out* — la dernière entrée est la première à sortir.

### Le registre `rsp` : le sommet de la pile

`rsp` (Stack Pointer) contient **l'adresse du sommet de la pile**. À chaque `push`, il **diminue** ; à chaque `pop`, il **augmente**.

> **Particularité de x86-64 :** la pile **grandit vers les adresses basses**. C'est contre-intuitif :
> - `push` fait `rsp -= 8` (descend en mémoire).
> - `pop` fait `rsp += 8` (remonte).

```
   Adresses hautes
        ↑
        │  ┌──────┐  ← rsp avant push
        │  │      │
        │  │      │
        │  ├──────┤  ← rsp après push (rsp - 8)
        │  │  42  │
        │  └──────┘
        ↓
   Adresses basses
```

### `push` : empiler une valeur

```nasm
push rax        ; déposer rax sur la pile (rsp -= 8)
push 42         ; déposer la valeur 42
push qword [var] ; déposer le contenu de var
```

Effets :
1. `rsp = rsp - 8` (descend de 8 octets).
2. `[rsp] = valeur` (écrit la valeur au nouveau sommet).

### `pop` : dépiler

```nasm
pop rax         ; prendre la valeur du sommet et la mettre dans rax (rsp += 8)
```

Effets :
1. `valeur = [rsp]` (lit le sommet).
2. `rsp = rsp + 8` (remonte).

### Cas d'usage n°1 : sauvegarder temporairement

Tu as vu au chapitre 17 le pattern :

```nasm
push rcx        ; sauvegarder rcx
mov rax, 1      ; faire un syscall qui pourrait écraser rcx
mov rdi, 1
syscall
pop rcx         ; restaurer rcx
```

C'est l'utilisation la plus courante de la pile pour un débutant.

### Cas d'usage n°2 : intervertir deux valeurs

```nasm
push rax        ; mémoriser rax
push rbx        ; mémoriser rbx
pop rax         ; rax reçoit l'ancien rbx
pop rbx         ; rbx reçoit l'ancien rax
```

Plus simple qu'un swap avec un troisième registre, et très pratique.

### Voir la pile dans GDB

```
(gdb) x/10gx $rsp       ; afficher 10 qword à partir du sommet
```

Avec pwndbg, la pile est **affichée automatiquement** à chaque pas. Tu vois en direct ce qui s'empile/se dépile.

### Exemple complet annoté

```nasm
; pile.asm — Démonstration de push/pop

section .text
global _start
_start:
    mov rax, 42
    mov rbx, 17

    push rax            ; pile : [42]              rsp -= 8
    push rbx            ; pile : [42, 17]          rsp -= 8

    pop rcx             ; rcx = 17  pile : [42]    rsp += 8
    pop rdx             ; rdx = 42  pile : [ ]     rsp += 8

    ; Vérification : rcx vaut 17, rdx vaut 42
    mov rdi, rdx        ; renvoyer 42 comme code retour
    mov rax, 60
    syscall
```

`./prog ; echo $?` → `42`. Lance dans GDB et observe `rsp` qui descend et remonte.

## Très utile en pratique

### Règle d'or : push/pop équilibrés

Si tu fais `push rax`, tu **dois** faire un `pop` à un moment, sinon `rsp` est désaligné et la suite (notamment les `ret` qu'on verra au prochain chapitre) va planter.

> **Toujours autant de `push` que de `pop`.** Sinon, crash assuré.

### Préserver plusieurs registres

```nasm
push rax
push rbx
push rcx
; ... code ...
pop rcx           ; dans l'ORDRE INVERSE
pop rbx
pop rax
```

LIFO oblige : on dépile dans l'**ordre inverse** d'empilement.

### Ne pas modifier `rsp` à la main (sauf si tu sais)

Tu peux écrire `sub rsp, 16` pour réserver 16 octets sur la pile, ou `add rsp, 16` pour les libérer. C'est utile pour allouer des **variables locales** dans une fonction (chapitre 20). Mais **toujours par paire** : ce que tu réserves, tu dois le libérer avant de quitter.

### `rsp` est sacré

Si tu fais `mov rsp, 0` n'importe où dans ton programme, **tu détruis la pile** et tu crashes instantanément. Ne touche jamais à `rsp` directement, sauf de manière équilibrée (`sub` puis `add`).

## Bonus

### Pourquoi la pile grandit-elle "à l'envers" ?

Historique : à l'époque des systèmes avec peu de mémoire, on plaçait :
- Le code et les données initiales en **bas** de la mémoire.
- La pile en **haut**, qui grandissait vers le bas.

Comme ça, la pile et le tas pouvaient grandir **l'un vers l'autre**, maximisant l'utilisation de la mémoire disponible. Le sens "à l'envers" est resté par compatibilité.

### Aperçu : la pile et les fonctions

Quand tu fais `call fonction` (chapitre suivant), le CPU **empile l'adresse de retour** sur la pile, puis saute. C'est pour ça qu'on doit comprendre la pile **avant** les fonctions.

### Alignement à 16 octets

Pour le **chapitre 21** (appel à la libc), il faudra que `rsp` soit aligné sur 16 octets juste avant un `call`. Ça veut dire que `rsp` doit se terminer par `0` en hexa (donc divisible par 16). Sinon, certaines fonctions C plantent. Détails et trucs au chapitre 21.

## ❌ Erreur classique

```
Déséquilibrer push et pop
→ Crash à coup sûr, surtout si la fonction se termine par ret.

Dépiler dans le mauvais ordre
→ Les valeurs reviennent dans les mauvais registres.
   Exemple : push rax / push rbx
            pop rax / pop rbx  ← inversé ! rax reçoit l'ancien rbx.

Modifier rsp à la main de manière non équilibrée
→ La pile est corrompue, le programme crashe.

Croire que push fait rsp + 8
→ NON. push fait rsp - 8 (la pile descend).

Oublier que push écrit à la mémoire pointée par rsp
→ Ce n'est pas magique : la valeur va vraiment en RAM.

Croire que pop "efface" la valeur de la pile
→ Non. La valeur reste en mémoire, mais rsp avance, donc on l'ignore.
   Un nouveau push écrasera ces octets.
```

## Exercices

**Guidé :** Recopie et exécute `pile.asm` ci-dessus. Lance-le dans GDB. À chaque `push`/`pop`, regarde `rsp` (avec `print /x $rsp`) et le contenu de la pile (`x/4gx $rsp`).

**Autonome :** Écris un programme qui empile **3 valeurs** (`100`, `200`, `300`), puis les dépile dans `rax`, `rbx`, `rcx`. Quel registre contiendra quoi ?

> **Réponse :** dans l'ordre LIFO : `rax = 300`, `rbx = 200`, `rcx = 100`.

**Défi :** Sans utiliser de troisième registre, **inverse 4 valeurs** : empile `1, 2, 3, 4`, puis dépile dans `r12, r13, r14, r15`. Quelle sera la valeur de chaque registre ?

## ✅ Tu sais maintenant…

- Ce qu'est la **pile** (LIFO) et comment elle vit en mémoire
- Le rôle du registre **`rsp`** (pointeur de pile)
- Empiler avec **`push`** (et `rsp -= 8`)
- Dépiler avec **`pop`** (et `rsp += 8`)
- La règle des **push/pop équilibrés**
- Sauvegarder temporairement un registre
- Que la pile grandit vers les **adresses basses**
- Observer la pile dans GDB

---

# Chapitre 19 — Fonctions avec `call` et `ret`

## Le minimum à savoir

### Pourquoi des fonctions ?

Jusqu'ici, tu écris des programmes "tout en un bloc". Mais dès que tu fais quelque chose deux fois (afficher un message, calculer une somme…), tu **copies-colles**. Pénible et fragile.

Les **fonctions** sont des blocs de code **réutilisables**, qu'on appelle à plusieurs endroits. Comme `def` en Python ou les fonctions Bash.

> **À retenir :** une fonction en ASM, c'est juste un **label** où tu sautes, et duquel tu reviens.

### `call` et `ret` : aller et revenir

| Instruction | Effet |
|-------------|-------|
| **`call fn`** | (1) Empile l'adresse de l'instruction suivante, (2) saute à `fn` |
| **`ret`** | (1) Dépile une adresse, (2) saute à cette adresse |

```
     code principal              fonction
     ──────────────              ──────────
       mov rdi, 5                ma_fonction:
       call ma_fonction  ─┐         ; corps
       mov rax, rax       │         ret    ─┐
       ; ...            ◄─┘                  │
                                            ◄┘
```

Le couple **`call` / `ret`** utilise la pile pour mémoriser où retourner. C'est pour ça qu'on a appris la pile **avant** les fonctions.

### Une première fonction

```nasm
; Fonction qui renvoie 42 dans rax

ma_fonction:
    mov rax, 42
    ret

; Programme principal
_start:
    call ma_fonction        ; rax devient 42
    mov rdi, rax
    mov rax, 60
    syscall
```

`./prog ; echo $?` → `42`.

### La convention d'appel System V AMD64

Sous Linux x86-64, **toutes les fonctions** (les tiennes, celles de la libc, celles d'un programme compilé) suivent les **mêmes règles** pour passer des arguments et récupérer un résultat. C'est l'**ABI System V AMD64**.

| Élément | Registre(s) |
|---------|-------------|
| **1er argument** | `rdi` |
| **2ème argument** | `rsi` |
| **3ème argument** | `rdx` |
| **4ème argument** | `rcx` |
| **5ème argument** | `r8` |
| **6ème argument** | `r9` |
| Arguments suivants | sur la pile |
| **Valeur de retour** | `rax` |

> **Mémorise ces 6 registres dans l'ordre. C'est valable PARTOUT.** Pour appeler `printf`, `malloc`, ou ta propre fonction, c'est toujours pareil.

### Fonction `carre(x)` qui renvoie `x * x`

```nasm
; carre(x) : rax = x * x
carre:
    mov rax, rdi        ; rax = x
    imul rax, rax       ; rax = x * x
    ret

_start:
    mov rdi, 7          ; argument : 7
    call carre          ; rax = 49
    mov rdi, rax        ; mettre 49 en code de retour
    mov rax, 60
    syscall
```

`./prog ; echo $?` → `49`.

### Caller-saved et callee-saved

C'est **le concept** à comprendre pour les fonctions. Quand tu appelles une fonction, certains registres peuvent être **détruits** par elle, d'autres pas :

| Catégorie | Registres | Qui doit sauvegarder ? |
|-----------|-----------|------------------------|
| **Caller-saved** | `rax, rcx, rdx, rsi, rdi, r8, r9, r10, r11` | L'**appelant** (toi) avant `call` |
| **Callee-saved** | `rbx, rbp, r12, r13, r14, r15` | La **fonction** elle-même, si elle les modifie |

**Traduction pratique :**

- Si tu utilises `rcx` et tu appelles une fonction, **suppose qu'elle a détruit `rcx`**. Sauvegarde-le si tu veux le récupérer (`push rcx` / `pop rcx`).
- Si **tu écris** une fonction qui utilise `rbx`, **tu dois le préserver** (push au début, pop à la fin).

> **Pourquoi ?** C'est un **contrat** entre fonctions. Ça permet à n'importe quelle fonction d'appeler n'importe quelle autre sans tout casser.

### Squelette d'une fonction propre

```nasm
ma_fonction:
    ; (optionnel) sauvegarder les callee-saved utilisés
    push rbx

    ; ... corps de la fonction ...
    ; rdi = arg 1, rsi = arg 2, etc.
    ; résultat dans rax

    ; restaurer
    pop rbx
    ret
```

### Exemple : fonction `max(a, b)`

```nasm
; max(a, b) : rax = plus grand des deux
max:
    mov rax, rdi        ; rax = a
    cmp rdi, rsi
    jge .fin            ; si a >= b, garder rax = a
    mov rax, rsi        ; sinon rax = b
.fin:
    ret

_start:
    mov rdi, 17
    mov rsi, 42
    call max            ; rax = 42

    mov rdi, rax
    mov rax, 60
    syscall
```

### Appels en cascade

Une fonction peut **en appeler une autre**. Chaque `call` empile son adresse de retour, chaque `ret` la dépile. C'est récursif et ça marche **automatiquement** grâce à la pile.

```nasm
double:
    add rdi, rdi
    mov rax, rdi
    ret

quadruple:
    call double         ; rax = 2 * arg
    mov rdi, rax        ; nouvel arg = 2 * arg
    call double         ; rax = 4 * arg
    ret

_start:
    mov rdi, 5
    call quadruple      ; rax = 20
    mov rdi, rax
    mov rax, 60
    syscall
```

## Très utile en pratique

### Fonction `print_msg` réutilisable

```nasm
; print_msg(rdi = adresse, rsi = longueur)
print_msg:
    mov rdx, rsi        ; rdx = longueur
    mov rsi, rdi        ; rsi = adresse
    mov rdi, 1          ; stdout
    mov rax, 1          ; write
    syscall
    ret

_start:
    mov rdi, msg1
    mov rsi, len1
    call print_msg
    mov rdi, msg2
    mov rsi, len2
    call print_msg
    mov rax, 60
    mov rdi, 0
    syscall
```

Plus de copier-coller des 5 lignes de `write` ! C'est exactement le but d'une fonction.

> **Note importante :** comme `syscall` détruit `rcx` et `r11` (rappel du chapitre 6), une fonction comme `print_msg` qui contient un `syscall` **ne peut pas promettre de préserver `rcx` ou `r11`** à son appelant. Ce n'est pas grave ici : `rcx` et `r11` sont déjà **caller-saved** par convention System V. Mais si tu écris une fonction qui doit préserver `rcx` (parce qu'elle l'utilise comme compteur, par exemple), pense à le sauvegarder avec `push rcx` / `pop rcx` autour du `syscall`.

### `jmp` vs `call`

- **`jmp fn`** : saute à `fn`, mais **sans retour possible**.
- **`call fn`** : saute à `fn`, **et `ret` reviendra ici**.

Utilise `call` pour les fonctions, `jmp` pour les sauts internes (boucles, if/else).

## Bonus

### `ret` sans `call` ?

Si tu fais `ret` sans `call` préalable, le CPU dépile **ce qu'il y a au sommet de la pile** (peut-être n'importe quoi) et saute à cette adresse. Crash quasi-garanti. **Ne jamais faire `ret` sans avoir été `call`é** (ou en sauvegardant proprement la pile).

### Aperçu : pourquoi les buffer overflows existent ?

Quand tu fais `ret`, le CPU dépile une adresse et y saute. Si un attaquant arrive à **écraser cette adresse** sur la pile (par exemple via un débordement de buffer), il peut détourner le programme. C'est la base de l'exploitation par buffer overflow. **Hors scope de ce cours**, mais tu vois pourquoi la pile et les fonctions sont si critiques en sécurité.

## ❌ Erreur classique

```
Oublier ret à la fin de la fonction
→ Le CPU continue avec les instructions suivantes (ou des octets aléatoires).

Utiliser jmp au lieu de call
→ Pas de retour possible. La fonction continue dans la fonction suivante.

Ne pas respecter la convention d'appel
→ Tu mets l'arg dans rax au lieu de rdi → la fonction lit du garbage.

Modifier un registre callee-saved sans le sauvegarder
→ Quand tu reviens à l'appelant, son rbx (par ex) est cassé.

Appeler une fonction avec rsp désaligné
→ Pas grave pour tes propres fonctions, mais CRITIQUE pour la libc (ch. 21).

Mettre des labels en double : .fin dans deux fonctions
→ Si elles utilisent toutes deux .fin (label local), ça MARCHE car
   les labels locaux sont liés au label principal. C'est l'intérêt.

Confondre la valeur de retour avec un arg : "retourner dans rdi"
→ NON. Le retour est TOUJOURS dans rax.
```

## Exercices

**Guidé :** Crée une fonction `addition(a, b)` qui renvoie `a + b` dans `rax`. Appelle-la avec 30 et 12. Le résultat doit être `42` (à voir via le code de retour).

**Autonome :** Crée une fonction `est_pair(n)` qui renvoie `1` si `n` est pair, `0` sinon. **Indice :** `test rdi, 1` met `ZF=1` si le bit 0 est à 0 (donc pair).

**Défi :** Crée une fonction **récursive** `factorielle(n)` qui s'appelle elle-même. **Indice :** `factorielle(0) = 1`, sinon `factorielle(n) = n * factorielle(n-1)`. Attention à `push rdi` avant l'appel récursif.

## 🧩 Mini-projet (chapitre 19) — Bibliothèque mini

Crée `bib.asm` qui définit **quatre fonctions** et les utilise dans `_start` :

1. **`print_msg(adresse, longueur)`** : affiche un message.
2. **`addition(a, b)`** : renvoie `a + b`.
3. **`max(a, b)`** : renvoie le plus grand.
4. **`exit_success()`** : appelle `exit(0)`.

Dans `_start`, fais :
- Affiche un message d'accueil.
- Calcule et affiche `addition(15, 27)` (= 42).
- Calcule et affiche `max(8, 23)` (= 23).
- Appelle `exit_success()`.

> **Tu n'as pas encore d'afficheur d'entiers.** Pour ce mini-projet, mets juste un message statique "Resultat calcule" et vérifie les calculs dans GDB.

## ✅ Tu sais maintenant…

- Pourquoi on crée des **fonctions** : éviter la duplication
- Utiliser **`call`** pour appeler une fonction
- Utiliser **`ret`** pour en revenir
- Comment `call`/`ret` utilisent la pile sous le capot
- La **convention System V AMD64** : args dans `rdi, rsi, rdx, rcx, r8, r9`, retour dans `rax`
- La différence **caller-saved** / **callee-saved**
- Écrire une **fonction propre** avec préservation des registres
- Que tu peux **appeler des fonctions imbriquées** (récursivité comprise)

---

# Chapitre 20 — Stack frame, `rbp` et variables locales

## Le minimum à savoir

### Pourquoi des variables locales ?

Une fonction complexe a besoin de plus de "place de travail" que les 6 registres d'arguments. Et tu ne veux **pas** utiliser `.data` (qui est partagé, non-récursif). Solution : **allouer de la place sur la pile**, valable seulement pendant la durée de la fonction.

### Le stack frame : l'espace de travail d'une fonction

Quand une fonction s'exécute, elle se réserve un **cadre de pile** (stack frame) :

```
   Adresses hautes
       ↑
       │  ┌──────────────┐
       │  │ args 7+      │ (si plus de 6 arguments)
       │  ├──────────────┤
       │  │ adresse retour│ ← empilée par 'call'
       │  ├──────────────┤
       │  │ ancien rbp   │ ← sauvegardé par le prologue
       │  ├──────────────┤  ← rbp pointe ici
       │  │ var locale 1 │  ← [rbp - 8]
       │  ├──────────────┤
       │  │ var locale 2 │  ← [rbp - 16]
       │  ├──────────────┤
       │  │ ...          │  ← rsp pointe ici (sommet)
       │  └──────────────┘
       ↓
   Adresses basses
```

`rbp` est le **point de repère stable** du cadre. `rsp` peut bouger pendant la fonction. `rbp` ne bouge pas.

### Le prologue et l'épilogue : le squelette standard

Toute fonction qui utilise des locales suit ce squelette :

```nasm
ma_fonction:
    ; ─── PROLOGUE ───
    push rbp            ; sauvegarder l'ancien rbp
    mov rbp, rsp        ; nouveau cadre : rbp = sommet actuel
    sub rsp, 32         ; réserver 32 octets pour les locales (4 qword)

    ; ─── CORPS ───
    mov qword [rbp - 8], 100      ; locale 1 = 100
    mov qword [rbp - 16], 200     ; locale 2 = 200
    ; ... travailler ...

    ; ─── ÉPILOGUE ───
    mov rsp, rbp        ; libérer les locales
    pop rbp             ; restaurer l'ancien rbp
    ret
```

Mémorise ce **squelette par cœur**. C'est **exactement** ce que produit gcc, et **exactement** ce que tu verras en reverse engineering.

### Pourquoi `[rbp - 8]` et pas `[rbp + 8]` ?

Parce que la pile **descend**. Les variables locales sont **au-dessous** de `rbp` (vers les adresses basses), donc avec un décalage **négatif**.

| Décalage | Contenu |
|----------|---------|
| `[rbp + 16]` et +  | 7ème argument, 8ème, etc. (rares) |
| `[rbp + 8]` | adresse de retour (empilée par `call`) |
| `[rbp]` | ancien rbp |
| `[rbp - 8]` | **1ère variable locale** |
| `[rbp - 16]` | 2ème variable locale |
| `[rbp - 24]` | 3ème variable locale |

### Exemple complet : fonction avec locales

```nasm
; Fonction somme_carres(a, b) : rax = a*a + b*b
somme_carres:
    push rbp
    mov rbp, rsp
    sub rsp, 16                 ; 2 qword de locales

    mov [rbp - 8], rdi          ; locale1 = a
    mov [rbp - 16], rsi         ; locale2 = b

    mov rax, [rbp - 8]
    imul rax, rax               ; rax = a*a

    mov rcx, [rbp - 16]
    imul rcx, rcx               ; rcx = b*b

    add rax, rcx                ; rax = a*a + b*b

    mov rsp, rbp                ; libérer locales
    pop rbp
    ret

_start:
    mov rdi, 3
    mov rsi, 4
    call somme_carres           ; rax = 9 + 16 = 25
    mov rdi, rax
    mov rax, 60
    syscall
```

`./prog ; echo $?` → `25`.

### Stocker les arguments en locales : pourquoi ?

Tu remarques qu'on a copié `rdi` et `rsi` dans `[rbp - 8]` et `[rbp - 16]`. Pourquoi ne pas les utiliser directement depuis `rdi`/`rsi` ?

Plusieurs raisons (et c'est ce que fait gcc en `-O0`) :
- Si on **appelle une autre fonction**, `rdi`/`rsi` sont caller-saved → écrasés.
- Si on a besoin des arguments **plus tard** dans la fonction, c'est plus sûr.
- Ça rend la fonction plus **lisible** à debug.

En `-O2` (avec optimisations), gcc évite cette copie inutile. Mais en `-O0` (sans), c'est systématique.

## Très utile en pratique

### Reconnaître le prologue/épilogue en reverse

C'est **L'indice n°1** pour repérer une fonction dans un binaire :

```
push rbp
mov  rbp, rsp
sub  rsp, ...
```

= **début de fonction**.

```
mov  rsp, rbp     (ou leave)
pop  rbp
ret
```

= **fin de fonction**.

Quand tu lis du code désassemblé, **chaque** apparition de `push rbp ; mov rbp, rsp` est le **début d'une fonction**. Tu peux ainsi cartographier un binaire entier.

### L'instruction `leave`

`leave` est un raccourci pour `mov rsp, rbp ; pop rbp`. Tu verras donc souvent :

```
leave
ret
```

= épilogue compact. C'est exactement la même chose, juste un peu plus court.

### Combien d'espace réserver ?

Multiplie `nombre de locales × 8` (pour des qword) et arrondis à 16 si tu vas appeler une autre fonction (alignement, voir ch. 21).

```nasm
; 3 variables locales qword
sub rsp, 24            ; non aligné sur 16
sub rsp, 32            ; aligné sur 16 → préférable
```

### Plus de 6 arguments : sur la pile

Si une fonction a 8 arguments, les 6 premiers vont dans `rdi, rsi, rdx, rcx, r8, r9`, et les 7ème et 8ème sont **empilés par l'appelant** avant le `call`. Tu les lis avec `[rbp + 16]` et `[rbp + 24]`. Cas rare en pédagogie débutante.

## Bonus

### Variables locales : taille fine

Tu peux mélanger des tailles :

```nasm
sub rsp, 16
mov byte  [rbp - 1], 'A'           ; 1 octet
mov dword [rbp - 8], 12345         ; 4 octets
mov qword [rbp - 16], 999999       ; 8 octets
```

En pratique, en pédagogie, **alloue tout en qword** : c'est plus simple à raisonner.

### Pourquoi rbp ?

Sans `rbp`, tu devrais référencer tes locales avec `rsp`, qui **bouge** (à chaque `push`/`pop`). `rbp` reste **fixe** pendant toute la fonction, donc `[rbp - 8]` désigne **toujours** la même locale.

En `-O1` ou `-O2`, gcc peut omettre `rbp` (`-fomit-frame-pointer`). Le code devient plus dense, mais **plus dur à lire en reverse**. C'est une des raisons pour lesquelles le reverse est plus simple sur du `-O0`.

## ❌ Erreur classique

```
Oublier de restaurer rsp avant ret
→ Crash au ret (l'adresse de retour est mal localisée).

Confondre [rbp - 8] (locale) et [rbp + 8] (adresse de retour)
→ Modifier l'adresse de retour = corruption mémoire = crash ou exploit.

Réserver de l'espace mais pas le libérer
→ Chaque appel de la fonction "fuit" sur la pile. Crash après quelques appels.

Mauvais offset (oublier que c'est en octets)
→ Pour 3 qword consécutifs : [rbp-8], [rbp-16], [rbp-24]. PAS -1, -2, -3.

Modifier rbp dans le corps de la fonction
→ Tu casses ta propre référence aux locales.

Oublier push rbp au début et pop rbp à la fin
→ La fonction appelante ne retrouve plus son cadre.
```

## Exercices

**Guidé :** Recopie et compile l'exemple `somme_carres` ci-dessus. Lance-le dans GDB, mets un breakpoint sur `somme_carres`, et observe `rbp` et `rsp` après le prologue. Affiche les locales avec `x/2gx $rbp - 16`.

**Autonome :** Réécris la fonction `factorielle(n)` du chapitre 19 en utilisant un stack frame propre avec **`push rbp / mov rbp, rsp` / `leave / ret`**. Stocke `n` dans une locale `[rbp - 8]`.

**Défi :** Crée une fonction `moyenne_quatre(a, b, c, d)` qui prend 4 arguments (tous dans des registres), les stocke en 4 locales, calcule la somme, divise par 4, et renvoie le résultat. Vérifie `moyenne_quatre(10, 20, 30, 40) = 25`.

## 🧩 Mini-projet (chapitres 18-20) — Mini-application structurée

Crée `app.asm` avec :

1. Une fonction **`afficher(adresse, longueur)`** qui fait un `write` propre.
2. Une fonction **`carre(n)`** qui renvoie `n*n`, avec stack frame.
3. Une fonction **`max(a, b, c)`** qui renvoie le maximum des trois, avec stack frame et 3 locales.
4. Une fonction **`exit_avec(code)`** qui appelle `exit` avec le code donné.

Dans `_start` :
- Affiche `"Bienvenue dans l'app !"`.
- Calcule `carre(7)` (= 49).
- Calcule `max(carre(7), 50, 42)` (= 50).
- Appelle `exit_avec(<le max>)`.

`echo $?` doit afficher `50`.

## ✅ Tu sais maintenant…

- Construire un **stack frame** : prologue (`push rbp ; mov rbp, rsp ; sub rsp, N`)
- Le terminer : épilogue (`mov rsp, rbp ; pop rbp ; ret`) ou `leave / ret`
- Allouer des **variables locales** sur la pile
- Y accéder avec **`[rbp - offset]`**
- Distinguer **locale** (`[rbp - N]`) et **adresse de retour** (`[rbp + 8]`)
- Reconnaître un **prologue de fonction** dans du code désassemblé
- L'instruction **`leave`** comme raccourci

À partir d'ici, tu maîtrises **TOUT le langage de base** de l'assembleur x86-64. Les chapitres suivants te montrent comment l'utiliser avec C et comment **lire** les programmes compilés.

---

## 🚩 Checkpoint — Fin de la Partie VII

C'est **le checkpoint le plus important** du cours. Tu dois pouvoir :

- [ ] Empiler et dépiler des valeurs avec `push` et `pop`, en gardant la pile équilibrée.
- [ ] Comprendre que la pile descend vers les adresses basses.
- [ ] Écrire une fonction simple avec `call` et `ret`.
- [ ] Respecter la convention d'appel System V (args dans `rdi, rsi, rdx, rcx, r8, r9`, retour dans `rax`).
- [ ] Distinguer registres **caller-saved** et **callee-saved**.
- [ ] Construire un **stack frame** avec prologue (`push rbp ; mov rbp, rsp ; sub rsp, N`) et épilogue (`leave ; ret`).
- [ ] Accéder à une variable locale via `[rbp - N]`.
- [ ] **Reconnaître un prologue de fonction** dans du code désassemblé.

> **Si ce checkpoint est solide, tu es prêt pour le reverse engineering.** Les parties suivantes ne font qu'appliquer ces réflexes à du code que tu n'as pas écrit.

---


# PARTIE VIII — LIEN AVEC C ET LIBC

---

# Chapitre 21 — Appeler la libc depuis l'assembleur

## Le minimum à savoir

### Syscall vs fonction C : la différence

Tu sais utiliser `write` (syscall n°1) pour afficher du texte. Mais en C, on utilise plutôt **`printf`** : `printf("Bonjour\n")`. Quelle est la différence ?

| | Syscall (`write`, `read`, …) | Fonction libc (`printf`, `scanf`, …) |
|---|---|---|
| **Niveau** | Direct au noyau | Bibliothèque utilisateur |
| **Vitesse** | Plus rapide | Plus lent (mais plus pratique) |
| **Fonctionnalités** | Brutes (octets) | Formatage, conversion automatique |
| **Comment l'appeler** | `syscall` | `call` (comme une fonction normale) |
| **Convention** | `rax = num`, args dans `rdi, rsi, …` | Args dans `rdi, rsi, …`, retour dans `rax` |

> **À retenir :** une fonction libc comme `printf` **finit par appeler `write`** sous le capot. Elle ajoute juste tout le formatage (`%d`, `%s`…). C'est plus haut niveau.

### Linker avec gcc au lieu de ld

Pour utiliser des fonctions libc, on **doit** linker avec `gcc` (qui s'occupe d'ajouter la libc automatiquement) :

```bash
nasm -f elf64 prog.asm -o prog.o
gcc -no-pie prog.o -o prog       # linker avec gcc, pas ld
```

L'option `-no-pie` simplifie la pédagogie (sans elle, l'exécutable est PIE = Position Independent Executable, ce qui complique les adresses). Pour ce cours, garde `-no-pie`.

### Point d'entrée : `main` au lieu de `_start`

Quand on linke avec gcc, le `_start` est **fourni** par gcc (c'est lui qui appelle `main`). Tu dois donc nommer ton point d'entrée **`main`** :

```nasm
section .text
global main           ; au lieu de _start
extern printf         ; on déclare qu'on va utiliser printf

main:
    ; ...
    ret               ; ret au lieu de syscall exit
```

> **Important :** ne fais **pas** `mov rax, 60 ; syscall` à la fin. Fais juste `ret` : gcc retournera dans le `_start` qu'il a fourni, qui appellera `exit` pour toi.

### `extern` : déclarer les fonctions externes

Pour utiliser `printf`, tu dois dire à NASM qu'elle existe quelque part (dans la libc) :

```nasm
extern printf
extern scanf
extern exit
extern malloc
; ...
```

### L'alignement à 16 octets : la règle critique

C'est **LA** règle à retenir pour appeler la libc. La convention System V exige que **`rsp` soit aligné sur 16 octets juste avant un `call`**. Sinon, certaines fonctions (notamment `printf` quand il utilise du SSE) crashent.

**Pourquoi un prologue `push rbp ; mov rbp, rsp` règle la question :**

Quand `_start` (fourni par gcc) appelle ton `main`, l'instruction `call main` **empile l'adresse de retour** (8 octets). À l'entrée de ta fonction `main`, `rsp` est donc à **`8 mod 16`** (désaligné de 8 octets).

```
Avant call main :  rsp = ...0x00     (aligné sur 16)
Pendant call    :  rsp -= 8          (push adresse retour)
À l'entrée main :  rsp = ...0x08     (DÉSALIGNÉ : 8 mod 16)
Après push rbp  :  rsp -= 8 encore
                   rsp = ...0x00     (RÉALIGNÉ sur 16) ✓
```

C'est pour ça que **le prologue classique `push rbp ; mov rbp, rsp` est exactement ce qu'il faut**. Il préserve `rbp` ET il réaligne la pile. Quand tu fais ensuite `call printf`, `rsp` est aligné, tout va bien.

> **Règle pratique :** **mets toujours un prologue dans `main`** (et dans toute fonction qui appelle la libc) et tu n'auras pas de souci.
>
> **Cas piège :** si tu fais un `push` solo (par exemple `push rcx` pour le sauvegarder) **juste avant** un `call printf`, tu re-désalignes la pile et tu crashes. Solution : faire des push **par paires** ou utiliser `sub rsp, 8` après le push (puis `add rsp, 8` avant le pop).

### Premier `printf` : "Hello"

```nasm
; hello_c.asm — Hello World avec printf

section .data
    fmt db "Bonjour depuis l'asm !", 10, 0    ; chaîne C terminée par 0

section .text
global main
extern printf

main:
    push rbp
    mov rbp, rsp

    lea rdi, [rel fmt]    ; rdi = adresse de la chaîne (1er arg)
    xor rax, rax          ; rax = 0 (nombre de regs XMM utilisés)
    call printf

    xor rax, rax          ; retour 0
    leave
    ret
```

Compile et exécute :

```bash
nasm -f elf64 hello_c.asm -o hello_c.o
gcc -no-pie hello_c.o -o hello_c
./hello_c
```

Sortie :

```
Bonjour depuis l'asm !
```

### Le mystère du `xor rax, rax`

`xor rax, rax` est l'idiome compact pour `mov rax, 0` (un peu plus rapide et plus court). Pourquoi mettre 0 dans `rax` avant `printf` ?

**Parce que `printf` est variadique** (nombre d'arguments variable). La convention System V dit : avant d'appeler une fonction variadique, `rax` doit contenir **le nombre de registres XMM utilisés** (registres pour les flottants). Pour les `%d`, `%s`, etc., il n'y a aucun flottant, donc `rax = 0`.

> **Règle pratique :** avant `printf`, `scanf`, ou toute fonction variadique : **`xor rax, rax`**.

### Afficher un entier avec `printf`

```nasm
section .data
    fmt db "Resultat : %ld", 10, 0      ; %ld pour un long (qword), cohérent avec dq
    val dq 42

section .text
global main
extern printf

main:
    push rbp
    mov rbp, rsp

    lea rdi, [rel fmt]
    mov rsi, [val]        ; 2ème arg : valeur à afficher (qword)
    xor rax, rax
    call printf

    xor rax, rax
    leave
    ret
```

Sortie : `Resultat : 42`.

### Lire un entier avec `scanf`

```nasm
section .data
    prompt db "Tape un nombre : ", 0
    fmt_in db "%ld", 0          ; format pour un long (qword)
    fmt_out db "Tu as tape : %ld", 10, 0

section .bss
    nombre resq 1

section .text
global main
extern printf
extern scanf

main:
    push rbp
    mov rbp, rsp

    ; printf(prompt)
    lea rdi, [rel prompt]
    xor rax, rax
    call printf

    ; scanf("%ld", &nombre)
    lea rdi, [rel fmt_in]
    lea rsi, [rel nombre]       ; ADRESSE de nombre (scanf y écrira)
    xor rax, rax
    call scanf

    ; printf("Tu as tape : %d\n", nombre)
    lea rdi, [rel fmt_out]
    mov rsi, [nombre]
    xor rax, rax
    call printf

    xor rax, rax
    leave
    ret
```

🎉 **Tu peux maintenant lire et afficher des nombres "comme en C", proprement.**

> **Détail à connaître :** quand un prompt **ne se termine pas par `\n`** (comme `"Tape un nombre : "`), il peut **rester bufferisé** par la libc et ne s'afficher qu'après la saisie. Sur un terminal interactif classique, ça passe généralement, mais pas toujours. Si tu rencontres ce souci, deux solutions :
> - Mettre un `\n` à la fin du prompt (peu élégant pour un prompt).
> - Appeler **`fflush(stdout)`** juste après le `printf` (`extern fflush` + `mov rdi, [stdout]` ou plus simple : `xor rdi, rdi ; call fflush` qui vide tous les buffers).
>
> Pour ne pas complexifier ce cours, on ne traite pas ce point en détail.

## Très utile en pratique

### Récapitulatif : checklist pour appeler la libc

Avant chaque appel libc, vérifie :

- [ ] Tu as `global main` (pas `global _start`).
- [ ] Tu as `extern <fonction>` pour chaque fonction utilisée.
- [ ] `main` commence par `push rbp ; mov rbp, rsp` (alignement).
- [ ] Tu lies avec `gcc -no-pie`.
- [ ] Les chaînes sont **terminées par 0** (style C).
- [ ] Avant un appel variadique (`printf`, `scanf`), tu fais `xor rax, rax`.
- [ ] Tu termines `main` par `leave ; ret` (pas par `syscall exit`).

### Le `lea ..., [rel ...]`

Tu vois `lea rdi, [rel fmt]` au lieu de `mov rdi, fmt`. C'est un détail technique :
- En 64 bits, on utilise généralement des adresses **relatives à `rip`**.
- `[rel ...]` est la syntaxe NASM pour ça.
- `lea` calcule cette adresse sans la lire (rappel du ch. 12).

Mets `default rel` en haut de ton fichier pour ne plus avoir à écrire `rel` partout :

```nasm
default rel

section .data
    fmt db "Hello", 0

section .text
    lea rdi, [fmt]    ; au lieu de [rel fmt]
```

## Bonus

### Le warning `.note.GNU-stack`

Quand tu lies un objet NASM avec gcc, tu peux voir ce message :

```
warning: ... missing .note.GNU-stack section implies executable stack
```

**Ce n'est pas une erreur, ton programme tourne quand même.** C'est juste un avertissement de sécurité : sans cette section, le linker pense que ta pile pourrait être exécutable (ce qui est dangereux). Pour le faire taire, ajoute en haut de ton `.asm` :

```nasm
section .note.GNU-stack noalloc noexec nowrite progbits
```

Ce point n'est pas essentiel pour les premiers exercices, mais c'est bon à savoir pour ne pas s'inquiéter du warning.

### Autres fonctions libc utiles pour démarrer

| Fonction | Usage |
|----------|-------|
| `puts(s)` | Affiche la chaîne `s` + un `\n`. Plus simple que printf. |
| `strlen(s)` | Calcule la longueur d'une chaîne C. |
| `strcmp(s1, s2)` | Compare deux chaînes. 0 si égales. |
| `malloc(n)` | Alloue `n` octets, retourne l'adresse dans `rax`. |
| `free(p)` | Libère la mémoire pointée par `p`. |
| `atoi(s)` | Convertit la chaîne `s` en entier. |
| `exit(code)` | Quitte avec un code de retour. |

Toutes s'utilisent avec la convention System V : args dans `rdi, rsi, …`, retour dans `rax`.

> **⚠️ À connaître mais à ne PAS utiliser : `gets(s)`.** Cette fonction lisait une ligne **sans contrôle de taille**, ce qui en faisait une porte ouverte aux buffer overflows. Elle a été **retirée des standards C modernes**. Tu en entendras parler uniquement parce qu'on la rencontre dans :
> - de vieux programmes vulnérables ;
> - des CTF où c'est précisément la vulnérabilité à exploiter.
>
> Pour lire une chaîne proprement, utilise `fgets(buf, taille, stdin)` (qui prend une taille max).

### `puts` : encore plus simple

```nasm
section .data
    msg db "Hello", 0          ; PAS de \n : puts l'ajoute

section .text
global main
extern puts

main:
    push rbp
    mov rbp, rsp
    lea rdi, [rel msg]
    call puts                  ; pas de xor rax, rax : puts n'est PAS variadique
    xor rax, rax
    leave
    ret
```

## ❌ Erreur classique

```
Lier avec ld au lieu de gcc
→ Erreur "undefined reference to printf".

Oublier extern printf
→ NASM se plaint : "symbol `printf' undefined".

Oublier le 0 final dans le format de printf
→ printf lit en dehors. Comportement indéfini.

Oublier xor rax, rax avant printf variadique
→ Marche parfois, plante d'autres fois (selon le format).

Désaligner la pile avec un push solo avant le call
→ Crash dans printf (souvent un SIGSEGV).

Terminer main avec syscall exit au lieu de ret
→ Marche, mais ce n'est pas la convention.

Donner la valeur au lieu de l'adresse à scanf
→ scanf veut une ADRESSE où écrire. Toujours lea ..., [var].

Mettre l'argument variadique au mauvais endroit
→ Le format va dans rdi, puis les valeurs dans rsi, rdx, ...
```

## Exercices

**Guidé :** Crée `hello_c.asm` comme ci-dessus. Compile avec gcc, exécute.

**Autonome :** Crée un programme qui affiche **deux entiers** avec un seul `printf` : `printf("a=%d, b=%d\n", a, b)`. Mets `a` dans `rsi`, `b` dans `rdx`. Vérifie le résultat.

**Défi :** Écris un programme qui :
1. Demande un nombre à l'utilisateur (avec `scanf`).
2. Le **double**.
3. Affiche le résultat.

Si l'utilisateur tape 21, ça doit afficher 42.

## 🧩 Mini-projet (chapitre 21) — Calculatrice à 2 opérandes

Crée `calc.asm` qui :

1. Affiche `"Premier nombre : "`.
2. Lit `a` avec `scanf`.
3. Affiche `"Deuxieme nombre : "`.
4. Lit `b` avec `scanf`.
5. Affiche `a + b`, `a - b`, `a * b` avec des `printf` séparés.

Exemple :

```
$ ./calc
Premier nombre : 12
Deuxieme nombre : 5
12 + 5 = 17
12 - 5 = 7
12 * 5 = 60
```

## ✅ Tu sais maintenant…

- La différence **syscall** vs **fonction libc**
- Linker avec **`gcc -no-pie`**
- Utiliser **`global main`** et **`extern printf`** (etc.)
- L'alignement à **16 octets** avec `push rbp / mov rbp, rsp`
- L'idiome **`xor rax, rax`** avant les fonctions variadiques
- Afficher avec **`printf`**, lire avec **`scanf`**
- Que `scanf` veut une **adresse** (`lea`), pas une valeur
- Terminer `main` par **`xor rax, rax ; leave ; ret`** (préparer la valeur de retour, puis démonter le stack frame)

---

# Chapitre 22 — Du C vers l'assembleur

## Le minimum à savoir

### Pourquoi ce chapitre ?

Tu as appris à **écrire** de l'assembleur à la main. Mais en pratique, l'ASM que tu vas lire en reverse vient **presque toujours** d'un compilateur C. Ce chapitre te montre :

1. Comment un programme C devient de l'assembleur.
2. À quoi ressemblent un `if`, une boucle, une fonction **compilés**.
3. Pourquoi le reverse est **plus simple sur `-O0`** que sur `-O2`.

### Compiler un `.c` en `.s` (assembleur)

```bash
gcc -O0 -masm=intel -S monprog.c -o monprog.s
```

- **`-O0`** : pas d'optimisation (assembleur verbeux, lisible).
- **`-masm=intel`** : syntaxe **Intel** (compatible avec ce qu'on a appris).
- **`-S`** : produit `.s` au lieu de compiler en `.o`.

Tu obtiens `monprog.s` que tu peux **lire**.

### Exemple : un programme C minimal

**`exemple.c` :**
```c
int main() {
    int a = 5;
    int b = 7;
    int c = a + b;
    return c;
}
```

Compile : `gcc -O0 -masm=intel -S exemple.c -o exemple.s`. Voici ce que gcc produit (extrait simplifié) :

```nasm
main:
    push    rbp
    mov     rbp, rsp
    mov     DWORD PTR [rbp - 4],  5     ; int a = 5
    mov     DWORD PTR [rbp - 8],  7     ; int b = 7
    mov     edx, DWORD PTR [rbp - 4]    ; edx = a
    mov     eax, DWORD PTR [rbp - 8]    ; eax = b
    add     eax, edx                     ; eax = a + b
    mov     DWORD PTR [rbp - 12], eax   ; c = eax
    mov     eax, DWORD PTR [rbp - 12]   ; return c
    pop     rbp
    ret
```

**Tu reconnais tout ?**
- `push rbp ; mov rbp, rsp` : prologue (ch. 20).
- `[rbp - 4]`, `[rbp - 8]`, `[rbp - 12]` : variables locales (ch. 20).
- `eax` au lieu de `rax` : parce que `int` en C fait 32 bits, pas 64 (ch. 2).
- `add eax, edx` : addition (ch. 8).
- `pop rbp ; ret` : épilogue (ch. 20).

> **C'est ça, comprendre l'ASM compilé** : reconnaître tous les patterns appris dans ce cours.

### Un `if` compilé

**`exemple_if.c` :**
```c
int test(int x) {
    if (x > 10)
        return 1;
    else
        return 0;
}
```

Compile et regarde le `.s` :

```nasm
test:
    push    rbp
    mov     rbp, rsp
    mov     DWORD PTR [rbp - 4], edi   ; x dans une locale
    cmp     DWORD PTR [rbp - 4], 10    ; compare x à 10
    jle     .L2                         ; si x <= 10, saut "else"

    mov     eax, 1                      ; "if" : return 1
    jmp     .L3
.L2:
    mov     eax, 0                      ; "else" : return 0
.L3:
    pop     rbp
    ret
```

**Reconnaissance :**
- `cmp ... , 10 / jle ...` : test `if (x > 10)` (ch. 16).
- `.L2`, `.L3` : labels auto-générés par gcc.
- Le pattern **if/jmp/label/jmp/label** est le squelette `if/else` que tu connais déjà.

### Une boucle `for` compilée

**`exemple_for.c` :**
```c
int somme() {
    int s = 0;
    for (int i = 0; i < 10; i++)
        s = s + i;
    return s;
}
```

Sortie ASM (extrait) :

```nasm
somme:
    push    rbp
    mov     rbp, rsp
    mov     DWORD PTR [rbp - 4], 0      ; s = 0
    mov     DWORD PTR [rbp - 8], 0      ; i = 0
    jmp     .L2                          ; aller au test
.L3:                                    ; corps de boucle
    mov     eax, DWORD PTR [rbp - 8]    ; eax = i
    add     DWORD PTR [rbp - 4], eax    ; s += i
    add     DWORD PTR [rbp - 8], 1      ; i++
.L2:
    cmp     DWORD PTR [rbp - 8], 9      ; i <= 9 ?
    jle     .L3                          ; si oui, recommencer
    mov     eax, DWORD PTR [rbp - 4]    ; return s
    pop     rbp
    ret
```

**Reconnaissance :**
- Un **saut arrière** (`jle .L3`) → c'est une **boucle** (ch. 17).
- Un compteur incrémenté → variable de boucle.
- Le pattern **jmp test ; label_corps ; corps ; label_test ; cmp ; jXX label_corps** est l'écriture typique d'une boucle `for` en gcc.

> **Astuce reverse :** quand tu vois un saut **vers une adresse précédente** dans le code, c'est **un indice très fort** de boucle (c'est l'écriture la plus naturelle d'une boucle, et c'est ce que gcc produit en `-O0`). Garde une petite réserve mentale pour des cas plus exotiques (sauts arrière qui font partie de `goto` complexes, ou de patterns optimisés), mais en pratique débutante : **saut arrière → boucle**.

### Une fonction qui en appelle une autre

**`exemple_appel.c` :**
```c
int carre(int n) {
    return n * n;
}

int main() {
    int x = carre(7);
    return x;
}
```

ASM :

```nasm
carre:
    push    rbp
    mov     rbp, rsp
    mov     DWORD PTR [rbp - 4], edi    ; n dans locale
    mov     eax, DWORD PTR [rbp - 4]
    imul    eax, eax                     ; eax = n * n
    pop     rbp
    ret

main:
    push    rbp
    mov     rbp, rsp
    sub     rsp, 16
    mov     edi, 7                       ; arg pour carre
    call    carre                        ; rax = 49
    mov     DWORD PTR [rbp - 4], eax    ; x = rax
    mov     eax, DWORD PTR [rbp - 4]
    leave
    ret
```

**Reconnaissance :**
- `call carre` : appel de fonction (ch. 19).
- `mov edi, 7 ; call ...` : passage d'arg via `rdi` (ch. 19).
- `mov ..., eax` après le call : récupération de la valeur de retour (ch. 19).

### L'impact des optimisations

**Le même `exemple_if.c` compilé avec `-O2`** :

```nasm
test:
    xor     eax, eax              ; eax = 0
    cmp     edi, 10               ; x > 10 ?
    setg    al                    ; al = 1 si x > 10, 0 sinon
    ret
```

**Quatre instructions au lieu de douze.** Le `if/else` a disparu, remplacé par `setg` (set if greater) qui produit 0 ou 1 directement. C'est plus rapide, mais **beaucoup plus dur à lire**.

> **Pour le reverse engineering débutant : préfère analyser des binaires en `-O0`.** En `-O2`, les patterns sont méconnaissables et il faut une expérience plus large.

## Très utile en pratique

### Liste de patterns à reconnaître

| Pattern ASM | Construction C |
|-------------|----------------|
| `push rbp / mov rbp, rsp / sub rsp, N` | Début de fonction |
| `leave / ret` ou `mov rsp, rbp / pop rbp / ret` | Fin de fonction |
| `cmp ... , ... / jXX label` | `if (...)` |
| `cmp ... / jge label_corps` (saut arrière) | Boucle |
| `call fn` | Appel de fonction |
| `mov edi, X / call fn` | Appel avec arg |
| `mov [rbp - N], eax` | Affectation à une variable locale |
| `mov eax, [rbp - N]` | Lecture d'une variable locale |
| `test eax, eax / je ...` | `if (x == 0)` |
| `setg al / setl al / etc.` | Optimisation d'une comparaison (en `-O2`) |

### Comparer C et ASM côte à côte

L'outil **Godbolt Compiler Explorer** ([godbolt.org](https://godbolt.org)) affiche, en direct, l'ASM produit par un compilateur pour un code C. C'est **fantastique** pour s'entraîner :

1. Tape un petit C à gauche.
2. Choisis x86-64 gcc.
3. Ajoute `-O0 -masm=intel` dans les flags.
4. L'ASM apparaît à droite, avec un code-couleur reliant les lignes C aux lignes ASM.

**Indispensable** pour ce chapitre. Joue avec.

## Bonus

### Les niveaux d'optimisation

| Flag | Effet |
|------|-------|
| `-O0` | Aucune optimisation. ASM verbeux, lisible. **Pour debug et reverse pédagogique.** |
| `-O1` | Optimisations basiques. Élimine du code mort. |
| `-O2` | Optimisations standards. **Le défaut pour la prod.** |
| `-O3` | Optimisations agressives, parfois trop. |
| `-Os` | Optimise pour la **taille** du binaire. |

### Niveaux différents : ce qui change

Sur un même `if` :
- `-O0` : ~10 instructions, `cmp / jXX / mov / jmp / mov`.
- `-O2` : ~3 instructions, souvent `setXX` ou même expression mathématique sans saut.

Pour **commencer le reverse**, vise du `-O0`. Tu monteras en optimisation au fur et à mesure.

## ❌ Erreur classique

```
Croire que gcc traduit ligne à ligne
→ Faux. gcc applique des optimisations, réorganise, fusionne.

Lire du -O2 en croyant que c'est du brut
→ Tu te perds. Identifie toujours le niveau d'optimisation d'un binaire.

Ne pas mettre -masm=intel
→ Tu te retrouves avec de l'AT&T (mov $5, %eax) que tu ne sais pas lire.

Croire que toutes les variables C sont sur la pile
→ En -O2, gcc met les variables fréquentes dans des registres directement.

Ne pas savoir où est le main quand on lit un .s
→ Cherche le label "main:" tout simplement. Les autres labels (.LCO,
  .LFB0, .Letext0…) sont des labels internes de gcc.
```

## Exercices

**Guidé :** Écris ce `.c`, compile-le en `.s` avec `gcc -O0 -masm=intel -S`, et **lis le résultat**. Identifie le prologue, le calcul, l'épilogue.

```c
int double_plus_un(int n) {
    return 2 * n + 1;
}
```

**Autonome :** Écris un `.c` avec une fonction qui contient un **`if/else`**. Compile en `.s`. Repère le `cmp`, les sauts, les deux branches.

**Défi :** Écris un `.c` avec une **boucle `for` qui calcule une somme**. Compile en `-O0` et en `-O2`. Compare. Note les différences.

## 🧩 Mini-projet (chapitre 22) — Reverse mental

Écris en C un petit programme avec :
- Une fonction `f(int a, int b)` qui retourne `a * a + b`.
- Un `main` qui appelle `f(3, 4)` et affiche le résultat avec `printf`.

Compile en `-O0`. **Avant de lire le `.s`**, écris sur papier ce que tu **t'attendrais** à voir comme ASM (prologue, calculs, call, printf, épilogue).

Compare avec le `.s` réel. **Mesure ton intuition.**

## ✅ Tu sais maintenant…

- Compiler un C en ASM avec **`gcc -O0 -masm=intel -S`**
- Reconnaître les **patterns du compilateur** : prologue, locales, if, boucle, appel
- Comprendre que **les optimisations transforment le code**
- Préférer **`-O0`** pour apprendre le reverse
- Utiliser **Godbolt** pour s'entraîner
- Faire le pont entre **C** (que tu comprends grosso modo) et **ASM**

Ce chapitre est ton pont vers la **partie IX**, où tu vas plonger dans les binaires compilés sans avoir le `.c` sous les yeux.

---

## 🚩 Checkpoint — Fin de la Partie VIII (avant le reverse)

Dernier checkpoint avant de plonger dans le reverse. Tu dois pouvoir :

- [ ] Linker avec **`gcc -no-pie`** et utiliser `extern printf`.
- [ ] Appeler **`printf`** et **`scanf`** depuis l'assembleur.
- [ ] Comprendre **pourquoi** il faut `xor rax, rax` avant un appel variadique.
- [ ] Compiler un `.c` en `.s` avec `gcc -O0 -masm=intel -S`.
- [ ] **Reconnaître dans un `.s`** :
  - [ ] Un prologue de fonction.
  - [ ] Un `if/else`.
  - [ ] Une boucle (saut arrière).
  - [ ] Un appel de fonction avec son argument.
- [ ] Comprendre la différence d'aspect entre `-O0` et `-O2`.

**Si tu coches tout, tu as toutes les armes pour le reverse débutant.** La partie IX ne fait que t'apprendre à appliquer ces réflexes à un vrai binaire.

---

## 🧭 Méthode — Lire un désassemblage sans paniquer

Quand tu ouvres `objdump -d` sur un binaire pour la première fois, tu vois **des centaines de lignes**. Pas de panique. Voici une méthode en **5 étapes** à appliquer systématiquement :

### Étape 1 — Repérer les chaînes

```bash
strings ./binaire
```

Les chaînes te donnent des **indices énormes** : messages d'erreur, prompts, formats `printf`, parfois des mots de passe en clair. Note celles qui ont l'air pertinentes.

### Étape 2 — Repérer les appels libc

Cherche dans le désassemblage les `call <nom>@plt` :
- `printf@plt`, `puts@plt` → affichage.
- `scanf@plt`, `fgets@plt` → lecture utilisateur.
- **`strcmp@plt`, `memcmp@plt` → comparaison, souvent d'un mot de passe**.
- `malloc@plt`, `free@plt` → gestion mémoire.
- `system@plt`, `execve@plt` → exécution de commandes (méfiance).

C'est ta carte du programme.

### Étape 3 — Repérer `main`

Si le binaire n'est pas strippé : `nm ./bin | grep main`.

Sinon : passe par `_start` → `__libc_start_main` → l'adresse passée dans `rdi` juste avant. (Méthode vue au chapitre 23.)

### Étape 4 — Repérer conditions et boucles

Une fois dans `main`, balaye :
- Les **`cmp` + saut conditionnel vers une adresse en aval** → conditions (`if`).
- Les **sauts (conditionnels ou non) vers une adresse en amont** → boucles.
- Les **`call`** → appels de sous-fonctions à explorer ensuite.

### Étape 5 — Renommer mentalement (ou dans un cahier)

À mesure que tu comprends, **donne des noms** aux choses :
- `[rbp - 4]` → tu as compris que c'est un compteur ? Appelle-le `i` dans ta tête.
- `[rbp - 16]` → un buffer ? Appelle-le `password_buf`.
- `0x401200` (fonction sans nom) → appelle-la `check_password`.

> **C'est exactement ce que font Ghidra et IDA automatiquement.** Mais même à la main, ça transforme un désassemblage cryptique en un programme compréhensible. Garde un cahier ou un fichier `notes.md` à côté pendant tes analyses.

---

## 🔍 Boîte à patterns — ASM pour le reverse

Avant de plonger dans la partie IX, voici **les 12 patterns essentiels** à reconnaître dans n'importe quel désassemblage. Imprime ce tableau, garde-le sous les yeux pendant tes premières analyses :

| Pattern ASM | Signification probable |
|-------------|------------------------|
| `push rbp` puis `mov rbp, rsp` | **Début de fonction** |
| `leave ; ret` ou `mov rsp, rbp ; pop rbp ; ret` | **Fin de fonction** |
| `sub rsp, N` après le prologue | Réservation de **N octets de variables locales** |
| `cmp ... , ... ` suivi de `jXX` | **Une condition** (if, comparaison) |
| `test rax, rax ; je ...` | Test `if (x == 0)` (ou `if (ptr == NULL)`) |
| Saut conditionnel vers une **adresse plus basse** (en arrière) | **Une boucle** |
| `mov edi, X ; call fn` | **Appel de fonction avec 1 argument** (`X`) |
| `mov edi, ... ; mov esi, ... ; call fn` | Appel à 2 arguments |
| `lea rdi, [rip + ...]` puis `call puts/printf@plt` | **Affichage d'une chaîne** |
| `call strcmp@plt` ou `call memcmp@plt` | **Comparaison de chaînes** (souvent un mot de passe !) |
| `call malloc@plt` ; le retour dans `rax` | **Allocation mémoire** |
| `mov eax, 0` puis `ret` | `return 0;` — souvent en fin de `main` |

> **Méthode reverse débutant :** quand tu lis un désassemblage, ne lis pas chaque instruction — **cherche d'abord ces patterns**. Ils te donnent la structure globale du programme. Les détails viennent ensuite.

---


# PARTIE IX — LECTURE DE BINAIRES ET REVERSE DÉBUTANT

---

# Chapitre 23 — Désassembler un binaire ELF

## Le minimum à savoir

### Le grand changement

Jusqu'ici, tu **écrivais** du code et tu en **observais** l'exécution. À partir d'ici, on **inverse** : tu reçois un binaire **sans le code source**, et tu dois comprendre ce qu'il fait. C'est le **reverse engineering**.

> **Le reverse débutant, c'est lire du code.** Pas écraser, pas modifier, pas exploiter. Juste **comprendre**.

### Le format ELF

Sous Linux, **les exécutables binaires natifs sont généralement au format ELF** (Executable and Linkable Format) — les scripts (`#!/bin/bash`, `#!/usr/bin/env python3`, etc.) sont une autre histoire, gérée par le noyau via le shebang. C'est un format structuré, divisé en **sections** que tu connais déjà (`.text`, `.data`, …) et en **segments** (utilisés au chargement en mémoire).

### Les 5 outils essentiels

| Outil | Rôle |
|-------|------|
| **`file`** | Identifier le type d'un fichier |
| **`strings`** | Extraire les chaînes lisibles d'un binaire |
| **`readelf`** | Inspecter la structure ELF (entêtes, sections, symboles) |
| **`nm`** | Lister les **symboles** (noms de fonctions, variables) |
| **`objdump`** | **Désassembler** un binaire en assembleur |

Ils sont tous fournis par `binutils` (déjà installé au chapitre 4).

### `file` : qu'est-ce que c'est ?

```bash
$ file ./hello
hello: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, ...
```

Tu apprends :
- **ELF** : c'est bien un exécutable Linux.
- **64-bit, x86-64** : architecture.
- **dynamically linked** : il dépend de bibliothèques (libc, …). L'opposé serait **statically linked** (autonome).

### `strings` : les chaînes en clair

```bash
$ strings ./hello
/lib64/ld-linux-x86-64.so.2
libc.so.6
puts
__libc_start_main
GLIBC_2.34
Bonjour le monde !
GCC: (Ubuntu 11.4.0) ...
```

Les **chaînes affichables** apparaissent. Si un mot de passe ou un message d'erreur est en clair, tu le verras ici. **Premier réflexe en CTF.**

### `readelf -h` : l'entête ELF

```bash
$ readelf -h ./hello
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 ...
  Class:                             ELF64
  Type:                              EXEC (Executable file)
  Entry point address:               0x401040
  ...
```

Important :
- **Entry point address** : adresse où le programme commence (le `_start`).
- **Class** : 64 bits (ELF64) ou 32 bits (ELF32).
- **Type** : EXEC, DYN, …

### `readelf -S` : les sections

```bash
$ readelf -S ./hello
There are 30 section headers, starting at offset 0x3938:

Section Headers:
  [Nr] Name              Type             Address           Size
  [ 1] .interp           PROGBITS         0x000000000040038c
  [ 2] .note.gnu.property NOTE             0x00000000004003a8
  ...
  [12] .text             PROGBITS         0x0000000000401040    ← le code !
  [16] .rodata           PROGBITS         0x0000000000402000    ← les chaînes
  [22] .data             PROGBITS         0x0000000000404010    ← données initialisées
  [23] .bss              NOBITS           0x0000000000404020    ← données vides
```

| Section | Contenu | Permissions |
|---------|---------|-------------|
| **`.text`** | Code exécutable | Lecture + exécution |
| **`.rodata`** | Données en lecture seule (constantes, chaînes littérales) | Lecture seule |
| **`.data`** | Variables globales initialisées | Lecture + écriture |
| **`.bss`** | Variables globales non initialisées | Lecture + écriture |
| **`.plt`** / **`.got`** | Tables pour les appels libc | Spécial |

### `nm` : lister les symboles

```bash
$ nm ./hello
                 U __libc_start_main@GLIBC_2.34    ← fonction externe
0000000000404020 B __bss_start
0000000000401040 T _start                          ← point d'entrée
0000000000402000 R msg                             ← variable globale
0000000000401140 T main                            ← fonction main
0000000000401130 T addition                        ← une autre fonction
```

Lettres : **T** = code (`.text`), **R** = lecture seule, **B** = `.bss`, **U** = undefined (importé).

### Binaire strippé : quand les symboles disparaissent

```bash
$ strip ./hello       # enlève tous les symboles internes
$ nm ./hello
nm: ./hello: no symbols
```

Un binaire **strippé** garde ses fonctions, mais **sans nom** dans `nm`. Tu verras juste des adresses (`sub_401130`) en désassemblage. C'est **le cas courant** des binaires en production. Plus dur à reverser.

### `objdump -d -M intel` : le désassemblage

```bash
$ objdump -d -M intel ./hello
```

L'option **`-M intel`** est **cruciale** : sans elle, c'est de l'AT&T (cryptique). Sortie (extrait) :

```
0000000000401140 <main>:
  401140:       55                  push   rbp
  401141:       48 89 e5            mov    rbp,rsp
  401144:       48 8d 3d b9 0e 00..  lea    rdi, [rip+0xeb9]    # 402004 <msg>
  40114b:       e8 e0 fe ff ff      call   401030 <puts@plt>
  401150:       b8 00 00 00 00      mov    eax, 0x0
  401155:       5d                  pop    rbp
  401156:       c3                  ret
```

Lis-le comme tu lis ton propre code :
- **Adresses** : `401140`, `401141`, …
- **Opcodes** (octets bruts) : `55`, `48 89 e5`, …
- **Mnémoniques** (instructions lisibles) : `push rbp`, `mov rbp, rsp`, …
- **Commentaires automatiques** : `# 402004 <msg>` (l'adresse pointée est nommée).

> **Tu reconnais tout ?** Le prologue (`push rbp ; mov rbp, rsp`), un `lea` pour charger l'adresse d'une chaîne, un `call puts@plt` (appel à puts via la PLT), l'épilogue (`pop rbp ; ret`). **Exactement** ce que tu as appris.

## Très utile en pratique

### Trouver `main` dans un binaire

Si `nm` montre `main`, super. Sinon (binaire strippé) :

1. Cherche le **point d'entrée** : `readelf -h` te donne l'adresse (c'est `_start`).
2. **Attention :** sous Linux avec la libc, `_start` n'appelle **pas** directement `main`. Il prépare les arguments puis appelle **`__libc_start_main`**, qui se charge d'appeler `main` ensuite.
3. L'adresse de `main` est généralement passée en **premier argument** à `__libc_start_main`, donc dans **`rdi`** (convention System V).
4. En désassemblage, cherche dans `_start` une instruction du type :
   ```
   mov  rdi, <adresse>        ; ← adresse de main
   ; ou
   lea  rdi, [rip + ...]
   ```
   juste avant `call __libc_start_main@plt`. Cette adresse, c'est `main`.

Exemple typique dans `_start` :

```
   ...
   lea  rdi, [rip + 0x101]    ← main ! (l'adresse calculée pointe sur main)
   ...
   call __libc_start_main@plt
```

### Filtrer le désassemblage à une fonction

```bash
objdump -d -M intel --disassemble=main ./hello
```

Cible une seule fonction. Indispensable quand le binaire est gros.

### Désassembler la section `.text` seule

```bash
objdump -d -M intel ./hello | less
```

Avec `| less`, tu peux scroller. Cherche `main` avec `/main` puis Entrée.

### Voir les chaînes contextualisées

```bash
objdump -s -j .rodata ./hello
```

Affiche le **contenu hex + ASCII** de la section `.rodata`. Tu vois exactement quelles constantes sont stockées et où.

## Bonus

### Pourquoi `puts@plt` et pas juste `puts` ?

`puts` est dans la **libc**, chargée dynamiquement. Le binaire ne contient pas le code de `puts` — juste un **stub** dans la section `.plt` qui sait où trouver `puts` à l'exécution. D'où le `@plt` (Procedure Linkage Table).

C'est un détail technique mais c'est le genre de chose qu'on rencontre **tout le temps** en reverse. Mémorise juste : `<fonction>@plt` = un appel à une fonction libc.

### `radare2` : pour les curieux

`radare2` (commande `r2`) est un outil de reverse engineering interactif plus puissant que `objdump`. Très utile pour les CTF. Hors scope de ce cours, mais à explorer ensuite.

### `ghidra` et `IDA` : les pros

Ces outils proposent du **désassemblage interactif avec décompilation** : ils te montrent l'ASM **et** une approximation du C correspondant. Magnifique mais gros à apprendre. Pour plus tard.

## ❌ Erreur classique

```
Oublier -M intel
→ Tu te retrouves avec mov %rax, %rbx (AT&T) au lieu de mov rbx, rax.
   Apprendre AT&T juste pour ça est inutile.

Chercher un main dans un binaire strippé sans le repérer via _start
→ Sans symboles, suis le call du _start.

Confondre l'adresse virtuelle (à l'exécution) et l'offset fichier
→ objdump affiche l'adresse virtuelle (0x401140), pas l'offset dans le .ELF.

Croire que tout le code est dans .text
→ Les fonctions C peuvent appeler la libc (via PLT). Les "_init", "_fini"
   font partie des sections initialisation.

Lire les opcodes au lieu des mnémoniques
→ Les opcodes (55, 48 89 e5) sont là pour info. Ce qui compte, c'est
   les mnémoniques (push rbp, mov rbp, rsp).
```

## Exercices

**Guidé :** Recompile l'un de tes propres programmes (par exemple `hello_c.asm` du ch. 21) et applique successivement :
- `file ./hello_c`
- `strings ./hello_c`
- `nm ./hello_c`
- `readelf -h ./hello_c`
- `objdump -d -M intel ./hello_c | less`

Identifie le `main`, le prologue, l'épilogue, le `call printf@plt`.

**Autonome :** Écris un petit `.c` avec une fonction `secret` qui contient une chaîne `"motdepasse123"` (juste en local : `char s[] = "motdepasse123";`). Compile. **Avant de lancer le programme**, retrouve la chaîne via `strings ./prog`.

**Défi :** Sur le même binaire, lance `strip ./prog`, puis refais `nm` et `objdump`. Que vois-tu en moins ? Peux-tu encore retrouver `main` ? (Indice : via le point d'entrée du ELF.)

## ✅ Tu sais maintenant…

- Ce qu'est un **binaire ELF** et ses **sections** (`.text`, `.rodata`, `.data`, `.bss`)
- Utiliser **`file`** pour identifier un binaire
- Utiliser **`strings`** pour extraire ses chaînes
- Utiliser **`readelf -h`** et **`-S`** pour son entête et ses sections
- Utiliser **`nm`** pour ses symboles
- **Désassembler** avec **`objdump -d -M intel`**
- La différence binaire **strippé / non strippé**
- Reconnaître **`fonction@plt`** pour les appels libc

---

# Chapitre 24 — Reverse engineering débutant avec GDB

## Le minimum à savoir

### Le reverse dynamique vs statique

Tu peux analyser un binaire de deux façons :

| Approche | Outils | Avantage |
|----------|--------|----------|
| **Statique** | `strings`, `objdump`, ghidra | Tu lis sans exécuter |
| **Dynamique** | `gdb`, `ltrace`, `strace` | Tu vois le programme tourner |

Tu maîtrises déjà les bases du statique (ch. 23). Maintenant : le **dynamique avec GDB**, qui complète parfaitement. Souvent, on **combine** les deux : on lit avec objdump, on vérifie avec GDB.

### Charger un binaire inconnu

```bash
gdb ./inconnu
```

Si le binaire est strippé, certaines commandes auront moins d'info. Mais l'essentiel marche pareil.

### Poser des breakpoints sur des adresses

Sans symboles, tu casses sur des **adresses** :

```
(gdb) break *0x401140        ; étoile + adresse
```

Avec symboles, tu peux casser sur des **noms** :

```
(gdb) break main
(gdb) break printf
```

Tu peux aussi casser sur tous les `call` d'une fonction :

```
(gdb) disas main
; repère les "call ..." → casse à chacune si nécessaire
```

### `start` : casser au tout début

```
(gdb) start
```

Si le binaire a un `main`, GDB s'arrête à son tout début. C'est l'équivalent de `break main ; run`. Pratique.

### Observer un programme en cours d'exécution

Une fois arrêté à un breakpoint :

| Commande | Effet |
|----------|-------|
| `disas` | Désassembler autour de `$rip` |
| `info registers` | Voir tous les registres |
| `x/s $rdi` | Si `rdi` est un pointeur sur une chaîne, l'afficher |
| `x/10gx $rsp` | Voir la pile |
| `stepi` (`si`) | 1 instruction (entre dans les call) |
| `nexti` (`ni`) | 1 instruction (passe par-dessus les call) |
| `continue` (`c`) | Continuer jusqu'au prochain break |
| `finish` | Sortir de la fonction courante |

### Repérer un `if` dans le désassemblage

Voici un schéma. Tu vois :

```
0x401200:  cmp    DWORD PTR [rbp-4], 0x2a
0x401204:  jne    0x401218
0x401206:  mov    eax, 0x1
0x40120b:  jmp    0x40121d
0x401218:  mov    eax, 0x0
0x40121d:  ...
```

**Décodage :**
- `cmp [rbp-4], 42` → on compare une variable locale à 42.
- `jne 0x401218` → si différent, saute au "else".
- Sinon : `eax = 1` puis saut au "fin".
- `0x401218:` (else) : `eax = 0`.

C'est `if (var == 42) return 1; else return 0;`.

### Repérer une boucle dans le désassemblage

```
0x401300:  mov    rcx, 0
0x401307:  ; ...
0x40130d:  cmp    rcx, 0xa
0x401311:  jge    0x401330
0x401317:  ; ... corps ...
0x40131d:  inc    rcx
0x401320:  jmp    0x40130d        ← saut ARRIÈRE
0x401330:  ; ...
```

**Indice clé : le `jmp 0x40130d` saute en arrière** vers une adresse plus basse. C'est **un indice très fort** d'une boucle (et de loin le cas le plus fréquent en pratique).

### Repérer un appel de fonction et ses arguments

```
0x401400:  mov    edi, 0x5         ← 1er arg
0x401405:  mov    esi, 0xa         ← 2ème arg
0x40140a:  call   0x401200 <calc>  ← appel
0x40140f:  mov    [rbp-8], eax     ← stocker le retour
```

**Décodage :** appel de `calc(5, 10)`, résultat stocké dans une locale.

### Suivre une comparaison de mot de passe

Voici **l'objet d'un crackme classique** :

```
0x401500:  mov    rdi, ADDR1        ; ton entrée
0x401507:  mov    rsi, ADDR2        ; le mot de passe en mémoire
0x40150e:  call   strcmp@plt
0x401513:  test   eax, eax
0x401515:  jne    mauvais
0x40151b:  ; ... "Bon mot de passe !" ...
mauvais:
0x401530:  ; ... "Mauvais !" ...
```

**Si tu vois `strcmp`** → le mot de passe est probablement comparé brut. Examine ce qu'il y a à `ADDR2` (avec `x/s 0x...`). Bingo. Si c'est `memcmp`, idem.

## Très utile en pratique

### Forcer une condition pour explorer

Tu veux **voir** la branche "succès" sans connaître le mot de passe ? Avant le `jne`, force le flag :

```
(gdb) set $eflags |= (1 << 6)     ; force ZF = 1 → ils sont "égaux"
```

Ou plus simple : **modifie l'instruction de saut**. Mais c'est du patching, hors scope.

Plus simple encore : casse **après** le `jne`, force `$rip` à la bonne adresse :

```
(gdb) set $rip = 0x40151b      ; saute directement au "bon" message
(gdb) continue
```

### Examiner ce qui est dans `rdi` quand `printf` est appelé

Pose un breakpoint sur `printf` et regarde le format :

```
(gdb) break printf
(gdb) continue
; ... arrive sur printf ...
(gdb) x/s $rdi
0x402004: "Saisis un mot de passe : "
```

Tu vois ce que **`printf` est sur le point d'afficher**, sans laisser tourner le programme. Très instructif.

### Voir ce que `read`/`scanf` reçoit

Casse après `read` ou `scanf` et regarde le buffer :

```
(gdb) x/s <adresse_buffer>
```

Tu vois ce que l'utilisateur a tapé (idéal pour comprendre comment le programme traite l'entrée).

## Bonus

### `ltrace` et `strace`

Deux outils hors GDB :

- `strace ./prog` : affiche tous les **syscalls** que le programme fait. Tu vois `write(1, "...", 5)`, `read(0, ...)`, etc.
- `ltrace ./prog` : affiche tous les appels à des fonctions de la **libc**.

Pour un débutant qui veut comprendre **vite** ce qu'un binaire fait, c'est une mine d'or.

```bash
ltrace ./crackme
strcmp("monessai", "secret123") = -1
```

Devine quoi : tu viens de **trouver le mot de passe**.

## ❌ Erreur classique

```
Poser break main sur un binaire qui n'a pas le symbole main
→ Erreur "Function main not defined". Utilise break *0x... ou "start" si possible.

Utiliser step (et pas stepi) sur du binaire sans source
→ step suit les lignes source, qui n'existent pas. Toujours stepi/nexti.

Confondre stepi et nexti
→ stepi entre dans les call. nexti passe par-dessus. Choisis selon le besoin.

Croire qu'un saut vers une adresse plus haute = pas une boucle
→ Faux. Une boucle EST un saut arrière. Vérifie le sens (jXX vers plus bas).

Modifier rip à n'importe quelle adresse
→ Tu peux atterrir au milieu d'une instruction. Crash garanti. Choisis
  une adresse alignée sur le début d'une instruction.

Lire la pile sans connaître l'ABI
→ Sans la convention System V en tête, on ne sait pas où sont les args.
```

## Exercices

**Guidé :** Reprends un de tes binaires (`hello_c` du ch. 21). Lance `gdb ./hello_c`, fais `start`, puis `disas main`, puis `nexti` plusieurs fois en regardant `rdi` à chaque appel à `printf`.

**Autonome :** Compile un petit C qui demande un nombre et **affiche "OK" si == 42, sinon "KO"**. Sans regarder le `.c`, retrouve dans GDB où se trouve le `cmp ..., 42`.

**Défi :** Compile un petit C avec un mot de passe `"secret"` comparé par `strcmp`. Lance-le dans GDB, casse sur `strcmp`, et **affiche le 2ème argument** (le mot de passe attendu) avec `x/s $rsi`.

## 🧩 Mini-projets finaux — 3 Crackmes progressifs

Voici trois **mini-binaires** à reverser. Pour chacun, ton boulot : **trouver le mot de passe**.

Tu peux toi-même les **fabriquer** en compilant les sources C ci-dessous (ce qui te donne un terrain d'entraînement reproductible). En CTF, tu n'aurais que le binaire — mais le but pédagogique est le même.

### Crackme 1 — Le mot de passe en clair (`strings` suffit)

**Code source (`crackme1.c`) :**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char input[64];
    printf("Mot de passe : ");
    scanf("%63s", input);
    if (strcmp(input, "OpenSesame") == 0)
        printf("Bravo !\n");
    else
        printf("Refuse.\n");
    return 0;
}
```

**Compile et joue :**

```bash
gcc -O0 -no-pie crackme1.c -o crackme1
```

**Mission :**
1. Sans regarder le `.c` (imagine que tu ne l'as pas).
2. `strings ./crackme1` → trouve le mot de passe.
3. Vérifie : `./crackme1` → tape-le → ça affiche "Bravo !".

### Crackme 2 — Comparaison caractère par caractère

**Code source (`crackme2.c`) :**

```c
#include <stdio.h>

int main() {
    char input[8];
    printf("Code : ");
    scanf("%7s", input);

    if (input[0] != 'X') goto faux;
    if (input[1] != 'A') goto faux;
    if (input[2] != 'B') goto faux;
    if (input[3] != 'C') goto faux;
    if (input[4] != '\0') goto faux;
    printf("Bravo !\n");
    return 0;
faux:
    printf("Refuse.\n");
    return 1;
}
```

```bash
gcc -O0 -no-pie crackme2.c -o crackme2
```

**Mission :**
1. `strings ./crackme2` ne donne rien d'utile (les caractères sont éparpillés).
2. `objdump -d -M intel ./crackme2 | less`, cherche `main`.
3. Repère les **plusieurs `cmp ... , 0x??`** (comparaisons à des octets précis).
4. Reconstitue le mot de passe en convertissant les valeurs hexa en ASCII.
5. Vérifie.

> **Indice :** `0x58 = 'X'`, `0x41 = 'A'`, `0x42 = 'B'`, `0x43 = 'C'`. Le mot de passe est `XABC`.

### Crackme 3 — Transformation XOR simple

**Code source (`crackme3.c`) :**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char input[8];
    char attendu[] = {0x18, 0x05, 0x07, 0x02, 0x00};   // chiffré
    char cle = 0x42;

    printf("Code : ");
    scanf("%7s", input);

    for (int i = 0; i < 4; i++)
        input[i] ^= cle;

    if (memcmp(input, attendu, 4) == 0)
        printf("Bravo !\n");
    else
        printf("Refuse.\n");
    return 0;
}
```

```bash
gcc -O0 -no-pie crackme3.c -o crackme3
```

**Mission :**
1. Lance dans GDB. Casse sur `main`. `disas main`.
2. Tu vois une **boucle** (saut arrière) qui XORe chaque octet.
3. Identifie la **clé XOR** (cherche `0x42` dans le code, ou pose un breakpoint et regarde un registre).
4. Identifie les **octets attendus** (cherche un tableau initialisé : `0x18, 0x05, 0x07, 0x02`).
5. **Inverse l'opération** : applique `^= 0x42` aux octets attendus pour retrouver l'entrée correcte.
   - `0x18 ^ 0x42 = 0x5A = 'Z'`
   - `0x05 ^ 0x42 = 0x47 = 'G'`
   - `0x07 ^ 0x42 = 0x45 = 'E'`
   - `0x02 ^ 0x42 = 0x40 = '@'`
6. Le mot de passe est `ZGE@`.
7. Vérifie : `./crackme3` → tape `ZGE@` → "Bravo !".

> **Méthode XOR :** la propriété clé est `(a XOR k) XOR k = a`. Donc si l'entrée est XORée avec une clé puis comparée, **on inverse en XORant la valeur attendue avec la même clé**.

## ✅ Tu sais maintenant…

- Lancer un binaire **inconnu** dans GDB
- Poser un breakpoint sur **adresse** ou sur **nom**
- Naviguer avec **`start`, `stepi`, `nexti`, `continue`, `finish`**
- **Repérer un `if`** : `cmp + jXX` vers une adresse plus haute
- **Repérer une boucle** : `cmp + jXX` vers une adresse plus basse
- **Repérer un appel** : `mov edi, ... ; call ...`
- Suivre les **arguments** passés à `printf`, `scanf`, `strcmp`
- **Forcer un saut** avec `set $rip` pour explorer
- Résoudre des **mini-crackmes** : mot de passe en clair, comparaison caractère par caractère, transformation XOR

🎉 **Bravo. Tu sais maintenant lire et reverser un petit binaire.** Tu es prêt pour des CTF de catégorie reverse débutant.

---


# PARTIE X — SYNTHÈSE ET BOÎTE À OUTILS

---

# Chapitre 25 — Récapitulatif complet du débutant

## Le minimum à savoir

Tu as parcouru 24 chapitres. Tu sais maintenant **lire et écrire** de l'assembleur x86-64. Ce chapitre est une **boîte à outils** : des tableaux récapitulatifs à imprimer et à garder à portée.

## Cheat-sheet 1 — Instructions essentielles

| Instruction | Effet | Exemple |
|-------------|-------|---------|
| `mov d, s` | Copie `s` dans `d` | `mov rax, 42` |
| `lea d, [expr]` | Calcule une adresse, pas de lecture | `lea rax, [rbx + rcx*8]` |
| `add d, s` | `d = d + s` | `add rax, rbx` |
| `sub d, s` | `d = d - s` | `sub rax, 5` |
| `inc d` | `d = d + 1` | `inc rcx` |
| `dec d` | `d = d - 1` | `dec rcx` |
| `neg d` | `d = -d` | `neg rax` |
| `imul d, s` | `d = d * s` (signé) | `imul rax, rbx` |
| `idiv s` | `rax = rdx:rax / s`, `rdx = reste` | `mov rdx, 0 ; idiv rbx` |
| `cmp a, b` | Met à jour les flags (`a - b`) | `cmp rax, 10` |
| `test a, b` | Met à jour les flags (`a AND b`) | `test rax, rax` |
| `jmp lbl` | Saut inconditionnel | `jmp .fin` |
| `je / jne` | Saut si égal / différent | `je egal` |
| `jl / jg` | Saut si < / > (signé) | `jl negatif` |
| `jle / jge` | Saut si <= / >= (signé) | `jge positif` |
| `jb / ja` | Saut si < / > (non signé) | `jb plus_petit` |
| `jz / jnz` | Saut si zéro / non zéro | `jz fin` |
| `call lbl` | Appel de fonction | `call ma_fn` |
| `ret` | Retour de fonction | `ret` |
| `push s` | Empile `s` (rsp -= 8) | `push rax` |
| `pop d` | Dépile dans `d` (rsp += 8) | `pop rax` |
| `syscall` | Appel système Linux | `syscall` |
| `xor d, s` | OU exclusif | `xor rax, rax` (= mov rax, 0) |
| `and d, s` | ET bit-à-bit | `and rax, 0xFF` |
| `or d, s` | OU bit-à-bit | `or rax, 1` |
| `shl d, n` | Décalage à gauche (× 2ⁿ) | `shl rax, 3` (rax × 8) |
| `shr d, n` | Décalage à droite (÷ 2ⁿ) | `shr rax, 1` |
| `leave` | `mov rsp, rbp ; pop rbp` | (épilogue compact) |
| `nop` | Ne fait rien | (utile en patching) |

## Cheat-sheet 2 — Registres x86-64

| 64 bits | 32 bits | 16 bits | 8 bits | Rôle conventionnel |
|---------|---------|---------|--------|---------------------|
| `rax` | `eax` | `ax` | `al` | Valeur de retour, résultats |
| `rbx` | `ebx` | `bx` | `bl` | Variable (callee-saved) |
| `rcx` | `ecx` | `cx` | `cl` | Compteur, 4ème arg |
| `rdx` | `edx` | `dx` | `dl` | 3ème arg, reste de div |
| `rsi` | `esi` | `si` | `sil` | 2ème arg |
| `rdi` | `edi` | `di` | `dil` | 1er arg |
| `rsp` | `esp` | `sp` | `spl` | **Pointeur de pile** |
| `rbp` | `ebp` | `bp` | `bpl` | Base de pile (callee-saved) |
| `r8`-`r15` | `r8d`-`r15d` | `r8w`-`r15w` | `r8b`-`r15b` | 5ème/6ème args, etc. |
| `rip` | — | — | — | Pointeur d'instruction (lecture seule directe) |

## Cheat-sheet 3 — Convention d'appel System V (Linux x86-64)

| Élément | Registre(s) |
|---------|-------------|
| **Arguments 1 à 6** | `rdi, rsi, rdx, rcx, r8, r9` |
| **Arguments 7+** | Sur la pile (ordre inverse) |
| **Valeur de retour** | `rax` |
| **Caller-saved** (peuvent être détruits) | `rax, rcx, rdx, rsi, rdi, r8, r9, r10, r11` |
| **Callee-saved** (à préserver) | `rbx, rbp, r12, r13, r14, r15` |
| **Alignement pile** | 16 octets avant `call` |
| **`rax` avant variadique** | Nombre de regs XMM (0 si pas de flottant) |

## Cheat-sheet 4 — Syscalls Linux x86-64 utiles

| Numéro (`rax`) | Nom | `rdi` | `rsi` | `rdx` | Notes |
|----------------|-----|-------|-------|-------|-------|
| 0 | `read` | fd | buf | count | Retour = octets lus |
| 1 | `write` | fd | buf | count | Retour = octets écrits |
| 2 | `open` | chemin | flags | mode | Retour = fd |
| 3 | `close` | fd | — | — | |
| 8 | `lseek` | fd | offset | whence | |
| 9 | `mmap` | adr | longueur | prot | (avancé) |
| 12 | `brk` | adr | — | — | |
| 35 | `nanosleep` | req | rem | — | |
| 39 | `getpid` | — | — | — | |
| 57 | `fork` | — | — | — | |
| 59 | `execve` | chemin | argv | envp | |
| 60 | `exit` | code | — | — | |
| 62 | `kill` | pid | sig | — | |

**Liste complète :** `cat /usr/include/x86_64-linux-gnu/asm/unistd_64.h` (Ubuntu/Debian) ou `cat /usr/include/asm/unistd_64.h` (selon distribution) ou `man 2 syscalls`.

## Cheat-sheet 5 — Commandes GDB

| Commande | Effet |
|----------|-------|
| `gdb ./prog` | Lance GDB |
| `break <lbl>` / `b *0x...` | Pose un breakpoint |
| `info breakpoints` / `i b` | Liste les breakpoints |
| `delete N` | Supprime le breakpoint N |
| `run` / `r` | Lance le programme |
| `start` | Lance et casse à `main` |
| `continue` / `c` | Continue jusqu'au prochain break |
| `stepi` / `si` | 1 instruction (entre dans les call) |
| `nexti` / `ni` | 1 instruction (par-dessus les call) |
| `finish` | Sort de la fonction courante |
| `info registers` / `i r` | Affiche tous les registres |
| `print /x $rax` | Affiche `rax` en hexa |
| `print /d $rax` | Affiche en décimal |
| `print /t $rax` | Affiche en binaire |
| `x/10gx $rsp` | 10 qword en hexa à `rsp` |
| `x/s $rdi` | Affiche une chaîne |
| `x/8bx <adr>` | 8 octets en hexa |
| `disas` | Désassemble autour de `rip` |
| `disas <fn>` | Désassemble une fonction |
| `layout asm` | Vue divisée (asm + commande) |
| `set $rax = N` | Modifie un registre |
| `set $rip = 0x...` | Saute à une adresse |
| `set disassembly-flavor intel` | Force syntaxe Intel |
| `info functions` | Liste les fonctions |
| `info variables` | Liste les variables |
| `quit` / `q` | Quitter |

## Cheat-sheet 6 — Outils ELF / binaires

| Commande | Effet |
|----------|-------|
| `file ./prog` | Type de fichier |
| `strings ./prog` | Chaînes lisibles |
| `nm ./prog` | Symboles |
| `readelf -h ./prog` | Entête ELF |
| `readelf -S ./prog` | Sections |
| `readelf -s ./prog` | Symboles (alternative à `nm`) |
| `objdump -d -M intel ./prog` | Désassemblage Intel |
| `objdump -d -M intel --disassemble=main ./prog` | Désassemble juste `main` |
| `objdump -s -j .rodata ./prog` | Voir le contenu d'une section |
| `ltrace ./prog` | Trace les appels libc |
| `strace ./prog` | Trace les syscalls |
| `xxd ./prog` | Dump hex |
| `hexdump -C ./prog` | Dump hex + ASCII |
| `strip ./prog` | Enlève les symboles |

## Modèle 1 — Fichier `.asm` minimal (syscalls)

```nasm
; modele_syscall.asm — Squelette pour programmes basés syscalls

section .data
    msg db "Bonjour", 10
    len equ $ - msg

section .bss
    buffer resb 64

section .text
global _start

_start:
    ; ─── corps du programme ───

    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall

    ; ─── sortie ───
    mov rax, 60
    mov rdi, 0
    syscall
```

**Compilation :**

```bash
nasm -f elf64 -g -F dwarf modele_syscall.asm -o modele_syscall.o
ld modele_syscall.o -o modele_syscall
```

## Modèle 2 — Fichier `.asm` avec libc

```nasm
; modele_libc.asm — Squelette pour programmes avec libc

default rel

section .data
    fmt db "Resultat : %ld", 10, 0     ; %ld pour un long (qword), cohérent avec un mov rsi 64 bits

section .text
global main
extern printf

main:
    push rbp
    mov rbp, rsp

    ; ─── corps du programme ───
    lea rdi, [fmt]
    mov rsi, 42
    xor rax, rax
    call printf

    xor rax, rax            ; retour 0
    leave
    ret
```

**Compilation :**

```bash
nasm -f elf64 -g -F dwarf modele_libc.asm -o modele_libc.o
gcc -no-pie modele_libc.o -o modele_libc
```

## Modèle 3 — Makefile générique

```makefile
# Makefile générique pour les programmes ASM

NASM       = nasm
LD         = ld
GCC        = gcc
NASMFLAGS  = -f elf64 -g -F dwarf

# Pour les programmes purs syscalls
%.o: %.asm
	$(NASM) $(NASMFLAGS) $< -o $@

%: %.o
	$(LD) $< -o $@

# Pour les programmes avec libc, utiliser :
# make NAME_libc          (suffixe _libc dans le nom de la cible)
%_libc: %_libc.o
	$(GCC) -no-pie $< -o $@

clean:
	rm -f *.o
	@find . -maxdepth 1 -type f -executable ! -name '*.sh' -delete 2>/dev/null || true

.PHONY: clean
```

Usage :
```bash
make exit              # compile exit.asm en exécutable exit
make hello_libc        # compile hello_libc.asm avec gcc
make clean             # supprime tous les .o et exécutables
```

## Méthodologie — Analyser un petit binaire inconnu

Quand on te donne un binaire et qu'on te demande de le comprendre, suis **cet ordre** :

1. **`file ./bin`** → c'est quoi ? 64 bits ? statique ou dynamique ?
2. **`strings ./bin`** → des chaînes parlantes ? mot de passe ? URL ? format ?
3. **`nm ./bin`** → symboles visibles ? fonctions nommées ?
4. **`ltrace ./bin`** → quels appels libc fait-il ? `strcmp`, `memcmp`, `system` ?
5. **`strace ./bin`** → quels syscalls ? `open`, `read`, `connect` ?
6. **`objdump -d -M intel ./bin | less`** → désassemblage. Cherche `main`.
7. **GDB** → casse sur `main`, observe les registres, suis les arguments.
8. **Repère** : prologues, comparaisons, sauts arrière, appels à des fonctions clés.
9. **Hypothèse** → teste.

## Top 10 des erreurs classiques (transversal)

1. **Confondre adresse (`var`) et contenu (`[var]`).**
2. **Oublier les crochets dans `mov`.**
3. **Mémoire-à-mémoire direct interdit** (`mov [a], [b]`).
4. **Mauvaise taille** (`mov al, ...` quand on attendait un qword).
5. **Push/pop déséquilibrés** → crash.
6. **Oublier `rdx = 0` avant `idiv`** → reste corrompu.
7. **Oublier `ret`** dans une fonction.
8. **Ne pas respecter la convention d'appel** (arg dans `rax` au lieu de `rdi`).
9. **Pile désalignée** avant un `call` libc.
10. **Lire/écrire avec la mauvaise taille** (`mov al, [qword_var]` ne lit qu'un octet).

## ✅ Tu sais maintenant…

Tu as toutes les bases pour :
- **Écrire** des programmes assembleur x86-64 simples
- **Compiler** et **linker** avec NASM, ld, ou gcc
- **Déboguer** au GDB en suivant les registres et la pile
- **Comprendre** le code généré par un compilateur C
- **Désassembler** un binaire ELF avec objdump
- **Reverser** un mini-crackme débutant
- **Reconnaître** prologues, conditions, boucles, appels dans du code désassemblé

---

# ANNEXES

---

# Annexe A — Syntaxe AT&T pour la lecture

## Pourquoi cette annexe ?

Tu rencontreras forcément du code en **syntaxe AT&T** (default GDB sans config, certaines docs Linux). Pas pour **écrire**, juste pour **lire**.

## Différences principales avec Intel

| Aspect | Intel (NASM) | AT&T |
|--------|--------------|------|
| Ordre des opérandes | `mov dest, src` | `mov src, dest` (**inversé !**) |
| Registres | `rax`, `eax` | `%rax`, `%eax` (préfixe `%`) |
| Valeurs immédiates | `5`, `0x42` | `$5`, `$0x42` (préfixe `$`) |
| Indirection mémoire | `[rax + 8]` | `8(%rax)` |
| Indexation | `[rax + rcx*8]` | `(%rax,%rcx,8)` |
| Suffixe de taille | dans le registre (`al`, `ax`, `eax`, `rax`) | sur l'instruction (`movb`, `movw`, `movl`, `movq`) |

## Exemples de traduction

| Intel | AT&T |
|-------|------|
| `mov rax, 5` | `movq $5, %rax` |
| `mov rax, rbx` | `movq %rbx, %rax` |
| `mov rax, [rbx]` | `movq (%rbx), %rax` |
| `mov rax, [rbx + 8]` | `movq 8(%rbx), %rax` |
| `mov rax, [rbx + rcx*4]` | `movq (%rbx,%rcx,4), %rax` |
| `add rax, rbx` | `addq %rbx, %rax` |
| `cmp rax, 10` | `cmpq $10, %rax` |
| `jne loop` | `jne loop` (identique) |
| `call printf` | `call printf` (identique) |

## Le piège du sens : `cmp`

C'est **le piège n°1** :

- Intel : `cmp rax, 10` + `jl ...` → saute si **`rax < 10`**.
- AT&T : `cmpq $10, %rax` + `jl ...` → saute aussi si **`%rax < 10`** (même sens, car `cmp` calcule `dest - src`, et AT&T met le src en premier).

Donc même si la syntaxe inverse les opérandes, le **sens du test** reste le même. Mais c'est très perturbant au début.

## Comment forcer GDB en Intel

Dans `~/.gdbinit` :
```
set disassembly-flavor intel
```

Ou ponctuellement :
```
(gdb) set disassembly-flavor intel
```

**Fais-le.** Tu n'auras presque plus à lire de l'AT&T.

---

# Annexe B — x86 32 bits vs x86-64

## Différences principales

| Aspect | x86 (32 bits) | x86-64 (64 bits) |
|--------|---------------|------------------|
| Registres généraux | 8 : `eax`-`ebp`, `esp` | 16 : `rax`-`rsp`, `r8`-`r15` |
| Taille des registres | 32 bits | 64 bits |
| Nom du pointeur de pile | `esp` | `rsp` |
| Nom du pointeur d'instr. | `eip` | `rip` |
| Adresses | 32 bits (max 4 Go) | 64 bits |
| Convention d'appel Linux | Args sur la **pile** | Args dans registres (System V) |
| Numéro de syscall | dans `eax` | dans `rax` |
| Instruction syscall | `int 0x80` | `syscall` (plus rapide) |
| Pile | 4 octets par push | 8 octets par push |

## Tu rencontreras du 32 bits si...

- Tu analyses un vieux binaire (avant 2010 environ).
- Tu joues à des CTF "old school".
- Tu fais du reverse sur des programmes embarqués légers.

## Conseil

**Reste en 64 bits pour apprendre.** Les concepts sont identiques, et tout est plus moderne. Le 32 bits sera évident pour toi le jour où tu en croiseras.

---

# Annexe C — Linux System V ABI vs Windows x64 ABI

## Pourquoi ça change ?

L'ABI (Application Binary Interface) définit **comment** les fonctions communiquent : où vont les arguments, où va le retour, etc. Linux et Windows ont **deux ABI différentes** en x86-64.

## Différences principales

| Aspect | System V (Linux/macOS) | Microsoft x64 (Windows) |
|--------|-------------------------|-------------------------|
| Args 1-4 | `rdi, rsi, rdx, rcx` | `rcx, rdx, r8, r9` |
| Args 5+ | `r8, r9`, puis pile | Pile (avec espace réservé) |
| Espace réservé | Aucun | **32 octets** (shadow space) sur la pile avant chaque `call` |
| Caller-saved | `rax, rcx, rdx, rsi, rdi, r8-r11` | `rax, rcx, rdx, r8-r11` |
| Callee-saved | `rbx, rbp, r12-r15` | `rbx, rbp, rdi, rsi, r12-r15` |
| Retour | `rax` | `rax` |
| Alignement pile | 16 octets avant `call` | 16 octets avant `call` |

## Conséquence pratique

Un binaire **Linux** et un binaire **Windows** se reversent **différemment** :
- Sur Linux, le 1er arg est dans `rdi`.
- Sur Windows, le 1er arg est dans `rcx`.

Si tu fais du reverse Windows un jour, **renverse tes réflexes**. C'est tout.

---

# Annexe D — Nombres signés, complément à deux et débordements

## Le problème

Comment représenter `-1` en binaire avec **seulement des 0 et des 1** ? La solution adoptée par tous les CPU modernes : **le complément à deux**.

## Le complément à deux en quelques règles

### Représentation

Sur N bits, on peut représenter :
- Non signés : `0` à `2ᴺ - 1`.
- Signés (complément à deux) : `-2ᴺ⁻¹` à `2ᴺ⁻¹ - 1`.

Pour un octet (8 bits) :
- Non signé : 0 à 255.
- Signé : -128 à +127.

### Le bit de signe

Le **bit le plus à gauche** indique le signe :
- `0` → positif.
- `1` → négatif.

### Comment calculer `-N`

Pour obtenir le complément à deux de `N` :
1. **Inverser tous les bits** (complément à un).
2. **Ajouter 1**.

Exemple sur 8 bits, calcul de `-5` :
```
   5 = 0000 0101
  ~5 = 1111 1010   (inversion)
  -5 = 1111 1011   (+ 1) = 0xFB
```

Donc `-5` sur 8 bits = `0xFB` = `251` non signé.

Sur 64 bits, `-1` = `0xFFFFFFFFFFFFFFFF`.

## Conséquences

### Une même valeur, deux interprétations

`0xFF` sur 8 bits :
- Non signé : 255.
- Signé : -1.

**C'est le CPU qui choisit comment l'interpréter** selon l'instruction utilisée (`jl` pour signé, `jb` pour non signé). C'est pour ça que tu dois bien distinguer.

### Débordements (overflow)

Sur 8 bits non signés :
- `255 + 1 = 0` (débordement, le résultat "boucle").

Sur 8 bits signés :
- `127 + 1 = -128` (overflow signé).

Le CPU met le flag `OF` (Overflow Flag) pour signaler ça, mais ne plante pas.

## En reverse

Si tu vois un `cmp rax, -1` ou `cmp rax, 0xFFFFFFFFFFFFFFFF`, **c'est la même chose**. Souvent, c'est utilisé pour tester si une fonction a renvoyé une erreur.

---

# Annexe E — Little-endian

## Le concept

Quand on stocke un nombre multi-octets en mémoire, deux ordres sont possibles :

- **Big-endian** : l'octet de poids fort en premier (comme on écrit en français).
- **Little-endian** : l'octet de poids faible en premier (à l'envers).

**x86 et x86-64 sont little-endian.** Tous les PC modernes le sont.

## Exemple

Soit le nombre `0x12345678` (4 octets). En mémoire :

```
Adresse :  0x100  0x101  0x102  0x103
Big-endian :  12    34     56     78
Little-endian: 78    56     34     12   ← x86-64
```

## En GDB

```
(gdb) x/4bx &n
0x404000:  0x78  0x56  0x34  0x12
```

Tu lis le résultat **à l'envers** : la valeur est bien `0x12345678`.

Quand tu fais `x/wx &n`, GDB te le **réordonne** pour l'affichage :

```
(gdb) x/wx &n
0x404000:  0x12345678
```

C'est pour ça que `x/wx` est plus pratique que `x/bx` quand tu sais que c'est un dword.

## Conséquence

Quand tu débugges et que tu lis des octets bruts, **n'oublie pas que les nombres sont à l'envers**. Une suite `EF CD AB 90` à l'écran est en réalité le nombre `0x90ABCDEF`.

---

# Annexe F — Makefile et commandes utiles

## Makefile complet et commenté

```makefile
# ========================================
# Makefile pour cours d'assembleur x86-64
# ========================================

# Outils
NASM       = nasm
LD         = ld
GCC        = gcc

# Options
NASMFLAGS  = -f elf64 -g -F dwarf

# Règle générale pour les .o
%.o: %.asm
	$(NASM) $(NASMFLAGS) $< -o $@

# Programmes purs syscalls (linkés avec ld)
%: %.o
	$(LD) $< -o $@

# Programmes avec libc (linkés avec gcc, suffixe _libc)
%_libc: %_libc.o
	$(GCC) -no-pie $< -o $@

# Lancer un programme dans GDB
debug-%: %
	gdb ./$<

# Désassembler
disas-%: %
	objdump -d -M intel ./$< | less

# Nettoyer
clean:
	rm -f *.o
	@for f in *; do \
		[ -f "$$f" ] && [ -x "$$f" ] && [ "$${f%.*}" = "$$f" ] && rm "$$f" 2>/dev/null; \
	done || true

.PHONY: clean
```

## Commandes utiles à connaître par cœur

```bash
# Compilation
nasm -f elf64 -g -F dwarf prog.asm -o prog.o
ld prog.o -o prog
gcc -no-pie prog.o -o prog        # avec libc

# Exécution
./prog
echo $?                            # voir le code de retour

# Conversion de bases
printf "%x\n" 255                 # déc → hex
printf "%d\n" 0xff                # hex → déc
echo "obase=2; 42" | bc           # déc → bin

# Inspection rapide
file prog
strings prog
nm prog
readelf -h prog
readelf -S prog
objdump -d -M intel prog | less

# Tracing
strace ./prog
ltrace ./prog

# Compilation C → ASM
gcc -O0 -masm=intel -S prog.c -o prog.s
```

---

# Annexe G — Glossaire assembleur / reverse

| Terme | Définition |
|-------|------------|
| **ABI** | Application Binary Interface : règles d'appel de fonctions |
| **Adresse** | Numéro identifiant une case mémoire |
| **Adressage** | Manière d'exprimer une adresse (`[reg]`, `[reg + N]`, etc.) |
| **ASCII** | Table standard de correspondance caractère ↔ nombre |
| **ASM** | Assembleur (le langage) |
| **Big-endian** | Ordre des octets : poids fort en premier |
| **Bit** | Plus petite unité d'information : 0 ou 1 |
| **BSS** | Section pour variables non initialisées |
| **Buffer** | Zone mémoire pour stocker des données |
| **Caller-saved** | Registres qu'une fonction peut détruire |
| **Callee-saved** | Registres qu'une fonction doit préserver |
| **CFG** | Control Flow Graph : graphe des chemins d'exécution |
| **Complément à 2** | Représentation des entiers négatifs |
| **CPU** | Processeur central |
| **Crackme** | Petit binaire à reverser (avec un mot de passe par exemple) |
| **CTF** | Capture The Flag : compétition de sécurité |
| **Désassemblage** | Conversion binaire → assembleur lisible |
| **Drapeau (flag)** | Bit d'indicateur d'état dans le CPU |
| **dword** | Double word = 4 octets = 32 bits |
| **ELF** | Format des exécutables Linux |
| **Endianness** | Ordre des octets en mémoire |
| **Épilogue** | Code de fin de fonction (`leave ; ret`) |
| **GDB** | GNU Debugger |
| **ghidra** | Outil de reverse engineering NSA, gratuit |
| **Hexadécimal** | Base 16 (`0-9, A-F`), notée `0x...` |
| **IDA** | Outil de reverse propriétaire de référence |
| **Immédiate** | Valeur littérale (constante) dans une instruction |
| **Instruction** | Action élémentaire du CPU |
| **Kernel** | Noyau du système d'exploitation |
| **Label** | Nom symbolique pour une adresse |
| **`lea`** | Load Effective Address : calcul d'adresse sans lecture |
| **LIFO** | Last In, First Out (mode pile) |
| **Linker** | Programme qui combine fichiers objets en exécutable |
| **Little-endian** | Ordre des octets : poids faible en premier (x86) |
| **Loader** | Code qui charge un programme en mémoire |
| **MASM** | Microsoft Macro Assembler (Windows) |
| **NASM** | Netwide Assembler (utilisé dans ce cours) |
| **NOP** | "No Operation" — instruction qui ne fait rien |
| **NULL** | Pointeur invalide (généralement adresse 0) |
| **Octet (byte)** | 8 bits = 1 octet |
| **Opcode** | Représentation binaire d'une instruction |
| **PIE** | Position Independent Executable |
| **Pile (stack)** | Zone mémoire en mode LIFO |
| **PLT** | Procedure Linkage Table (appels libc dynamiques) |
| **Pointeur** | Variable contenant une adresse |
| **Prologue** | Code de début de fonction (`push rbp ; mov rbp, rsp`) |
| **qword** | Quad word = 8 octets = 64 bits |
| **`r2`/radare2** | Outil interactif de reverse engineering open-source |
| **RAM** | Mémoire vive |
| **Registre** | Mini-case de stockage dans le CPU |
| **Reverse engineering** | Analyser un programme sans son code source |
| **`rip`** | Instruction Pointer (adresse de la prochaine instruction) |
| **`rsp`** | Stack Pointer (sommet de la pile) |
| **`.bss`** | Section pour variables non initialisées |
| **`.data`** | Section pour variables initialisées |
| **`.rodata`** | Section read-only (constantes) |
| **`.text`** | Section du code exécutable |
| **Saut** | Instruction qui change `rip` |
| **Section** | Sous-partie d'un fichier `.asm` ou ELF |
| **Stack frame** | Cadre de pile d'une fonction |
| **Strip** | Enlever les symboles d'un binaire |
| **Symbole** | Nom associé à une adresse (fonction, variable globale) |
| **Syscall** | Demande de service au noyau |
| **System V** | ABI Unix/Linux standard |
| **Variadique** | Fonction à nombre variable d'arguments (`printf`) |
| **word** | 2 octets = 16 bits |

---

# Annexe H — Panorama des outils de reverse

Tu connais déjà **`objdump`** et **`GDB`** (vus aux chapitres 23-24). Mais en reverse, il existe d'autres outils qui complètent ces deux-là. Voici un panorama rapide, pour que tu saches lequel utiliser quand.

## Tableau de référence

| Outil | Type | Force principale | Faiblesse | Quand l'utiliser |
|-------|------|------------------|-----------|------------------|
| **`objdump`** | Statique | Rapide, scriptable, installé partout | Pas interactif, output brut | Premier coup d'œil, automatisation |
| **`GDB`** (+ pwndbg) | Dynamique | Voit le programme tourner, force les valeurs, modifie l'exécution | Pas de vue d'ensemble, pas de décompilation | Comprendre un comportement précis, contourner une protection |
| **`radare2`** / **Cutter** | Statique + dynamique | Très puissant, open-source, scriptable, graphe interactif | Courbe d'apprentissage raide | Reverse intermédiaire, CTF sérieux |
| **Ghidra** | Statique avec décompilation | **Décompile en pseudo-C** (très lisible), graphe, gratuit, open-source (NSA) | Lourd à lancer, interface Java | Comprendre vite un gros programme, lire du pseudo-C plutôt que de l'ASM |
| **IDA Free** | Statique avec décompilation | Référence historique, décompilation excellente | Version gratuite limitée (pas de x64 dans les vieilles versions), payant pour le reste | Reverse professionnel |
| **`strace`** | Dynamique syscalls | Voit tous les syscalls (`open`, `read`, `connect`…) | Pas de détail des calculs internes | Comprendre ce qu'un binaire **fait au système** |
| **`ltrace`** | Dynamique libc | Voit tous les appels libc avec leurs args | Mêmes limites que strace | **Souvent suffit pour trouver un mot de passe** (`strcmp("entrée", "secret")`) |
| **`xxd`** / **`hexdump -C`** | Statique brut | Voir le contenu hex + ASCII | Aucune interprétation | Inspecter un fichier inconnu, headers |

## Méthode recommandée pour un débutant

L'ordre dans lequel je te conseille de découvrir ces outils :

1. **Aujourd'hui (déjà fait dans ce cours) :** `objdump`, `GDB`, `strings`, `nm`, `readelf`.
2. **Étape suivante (1-2 mois) :** **`ltrace`** et **`strace`** — souvent les outils les plus rapides pour comprendre un petit binaire.
3. **Ensuite (3-6 mois) :** **Ghidra** — la décompilation transforme l'apprentissage. Tu vois du pseudo-C à la place de l'ASM.
4. **Plus tard :** **radare2** ou **Cutter** pour le reverse interactif et les CTF.
5. **Encore plus tard :** **IDA Free** ou **IDA Pro** si tu vises du reverse pro.

## Démarrage rapide avec Ghidra

Si tu n'es pas dépaysé par l'environnement Java :

```bash
# Sur Ubuntu/Debian
sudo apt install openjdk-17-jdk
# Télécharger Ghidra sur ghidra-sre.org, puis :
unzip ghidra_*.zip
cd ghidra_*
./ghidraRun
```

Crée un projet, importe ton binaire (`File → Import File`), double-clique pour l'analyser (laisse les options par défaut). En quelques secondes, tu auras :
- À gauche, la liste des fonctions.
- Au centre, le **désassemblage**.
- À droite, le **pseudo-C décompilé** correspondant.

> **Effet "wow" pédagogique :** après avoir lu de l'ASM brut pendant des heures, voir Ghidra te montrer `if (strcmp(input, "secret") == 0)` directement, c'est libérateur. Mais **n'utilise pas Ghidra trop tôt** — les bases ASM apprises dans ce cours te permettront de comprendre ce que Ghidra te montre, et surtout de **repérer ses erreurs** (Ghidra se trompe parfois).

---

# Annexe I — Suite logique après ce cours

Tu as fini ce cours ? Bravo. Voici la suite naturelle, par niveau de difficulté :

## Niveau 1 — Consolidation

- **Pratique sur picoCTF** (catégorie *Reverse Engineering* niveau débutant).
- **Refaire les chapitres 23-24** avec d'autres binaires que tu compiles toi-même.
- **Lire des `.s` produits par gcc** avec différents codes et différentes optimisations.
- **Comparer C et ASM sur [Godbolt](https://godbolt.org)** régulièrement.

## Niveau 2 — Approfondir l'ASM

- **Apprendre la syntaxe AT&T** en lecture profonde (utile sur certains systèmes).
- **Découvrir SIMD/SSE/AVX** (calcul vectoriel) pour les performances.
- **Programmation noyau Linux** (modules, drivers).

## Niveau 3 — Approfondir le reverse engineering

- **Apprendre `radare2`** (`r2`) ou **ghidra** ou **IDA Free**.
- **CTF intermédiaires** sur HackTheBox, pwn.college, root-me.
- **Analyser des binaires strippés** avec des optimisations agressives.

## Niveau 4 — Sécurité offensive (à approfondir prudemment)

- **C orienté mémoire** : pointeurs, allocation, bugs courants.
- **Introduction au pwn** : buffer overflow, format string, ROP.
- **Shellcode** : écrire des charges utiles minimalistes.
- **Sécurité défensive** : ASLR, DEP/NX, PIE, canaries.

## Niveau 5 — Malware analysis et reverse Windows

- **Architecture Windows x64** (ABI différente, voir Annexe C).
- **Analyse de PE** (équivalent ELF côté Windows).
- **Sandbox et désobfuscation**.
- **Outils** : x64dbg, Cuckoo, Cutter.

## Livres recommandés

- *Practical Reverse Engineering* — Bruce Dang et al.
- *Hacking: The Art of Exploitation* — Jon Erickson.
- *The Shellcoder's Handbook* — Anley et al.
- *Computer Systems: A Programmer's Perspective* (CS:APP) — Bryant & O'Hallaron (fondations académiques).

## Communautés

- Reddit : r/ReverseEngineering, r/AskNetsec, r/lowlevel
- Discord : NightCTF, pwn.college, divers serveurs CTF
- Conférences : DEF CON, BSides, Black Hat (vidéos sur YouTube)

---

# Conclusion

Tu as toutes les bases pour lire, écrire et comprendre l'assembleur x86-64 sous Linux :

- **Chapitres 1-3 :** Le modèle mental — CPU, mémoire, registres, hex
- **Chapitres 4-6 :** Premiers programmes — NASM, sections, syscalls
- **Chapitres 7-9 :** Registres et observation — mov, calculs, GDB
- **Chapitres 10-12 :** Mémoire — variables, chaînes, lea, modes d'adressage
- **Chapitres 13-15 :** I/O — read, conversions, fichiers
- **Chapitres 16-17 :** Logique — comparaisons, sauts, boucles
- **Chapitres 18-20 :** Structure — pile, fonctions, stack frame
- **Chapitres 21-22 :** Lien avec C — libc, du C à l'ASM
- **Chapitres 23-24 :** Reverse — objdump, GDB sur binaires inconnus, crackmes
- **Chapitre 25 :** Synthèse et boîte à outils

**Pour continuer à progresser :**

- Écris des programmes ASM pour le plaisir — c'est la meilleure façon d'apprendre.
- Quand tu es bloqué, **GDB est ton meilleur ami**. Observe, n'imagine pas.
- Compile du C en ASM, lis le résultat. C'est ton meilleur prof.
- Lis le code des autres, surtout sur Godbolt.
- Fais des CTF — la pratique forge l'intuition.
- N'aie pas peur. L'assembleur n'est pas magique, c'est juste verbeux.

Bon code, bon reverse, bonne curiosité !

