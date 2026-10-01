# Introduction aux journaux d’événements Windows

- Les **Windows Event Logs** enregistrent les événements générés par :
    - Windows ;
    - applications ;
    - services ;
    - drivers ;
    - mécanismes de sécurité.
# Stockage des Event Logs

Les journaux Windows sont généralement stockés dans :

```
C:\Windows\System32\winevt\Logs\
```
![|672x460](./assets/Windows%20Event%20Log%20Analysis/Windows%20Event%20Log%20Analysis-005.webp)

Extension :

```
.evtx
```

- Les fichiers `.evtx` utilisent le format **Windows Event Log**.
- Ils ne sont pas destinés à être lus directement avec un éditeur texte classique.

```
.evtx
→ Event Viewer / PowerShell / Forensic Tools
→ Human-readable Events
```

Outils possibles :

- Event Viewer ;
- PowerShell ;
- `wevtutil` ;
- outils DFIR / SIEM.