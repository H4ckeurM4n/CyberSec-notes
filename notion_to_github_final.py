#!/usr/bin/env python3
"""
Script final pour convertir exports Notion en Markdown GitHub
Avec contrôle de la profondeur des accordéons imbriqués
"""

import re
import sys
from pathlib import Path

class NotionToGitHub:
    def __init__(self, max_depth=3):
        """
        max_depth : Profondeur maximale des accordéons
        0 = headers ### seulement
        1 = headers ### + listes niveau 0
        2 = + listes niveau 1 (4 espaces)
        3 = + listes niveau 2 (8 espaces)
        etc.
        """
        self.max_depth = max_depth
        self.result = []
        self.open_details = []
        
    def get_indent_level(self, line):
        """Calcule le niveau d'indentation"""
        if not line or not line.startswith(' '):
            # Ligne non indentée ou header
            if line.strip().startswith('###'):
                return -1  # Headers sont niveau -1 (au-dessus de tout)
            return 0
        
        # Compter les espaces
        spaces = 0
        for char in line:
            if char == ' ':
                spaces += 1
            else:
                break
        return spaces // 4
    
    def should_create_accordion(self, line, level):
        """Détermine si on doit créer un accordéon pour cette ligne"""
        # Si on dépasse la profondeur max, pas d'accordéon
        if level > self.max_depth:
            return False, None
        
        stripped = line.lstrip()
        
        # Headers ### toujours transformés
        if stripped.startswith('###'):
            title = stripped.replace('###', '').strip()
            return True, title
        
        # Ignorer markdown bold
        if stripped.startswith('- **'):
            return False, None
        
        # Détection titres avec ":"
        if re.match(r'^- (.+?):', stripped):
            match = re.match(r'^- (.+?):', stripped)
            title = match.group(1).strip()
            
            # Filtres pour éviter les faux positifs
            if len(title) < 4:
                return False, None
            
            # Liste noire de petits mots
            blacklist = ['ex', 'exemple', 'linux', 'windows', 'macos', 'pc', 'serveur']
            if title.lower() in blacklist:
                return False, None
            
            # Ignorer si c'est une commande
            if re.match(r'^[a-z_\-\s]+$', title):
                return False, None
            
            return True, title
        
        # Titres longs sans ":" (ex: "- Modèle OSI")
        if re.match(r'^- [A-Z]', stripped) and len(stripped) > 20 and ':' not in stripped[:30]:
            match = re.match(r'^- (.+)$', stripped)
            title = match.group(1).strip()
            # Éviter phrases descriptives
            desc_words = ['permettant', 'indique', 'responsable', 'gère', 'permet', 'assure', 'garantit']
            if any(word in title.lower() for word in desc_words):
                return False, None
            return True, title
        
        return False, None
    
    def close_details_until_level(self, target_level):
        """Ferme les accordéons jusqu'au niveau cible"""
        while self.open_details and self.open_details[-1]['level'] >= target_level:
            self.result.append('</details>')
            self.result.append('')
            self.open_details.pop()
    
    def get_emoji_for_level(self, level):
        """Emoji par niveau"""
        emojis = {
            -1: '🔹',  # Headers ###
            0: '📖',   # Liste niveau 0
            1: '🔸',   # Liste niveau 1
            2: '▫️',   # Liste niveau 2
            3: '•',    # Liste niveau 3
            4: '◦'     # Liste niveau 4+
        }
        return emojis.get(level, '◦')
    
    def process_content(self, lines):
        """Traite le contenu"""
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Niveau d'indentation
            level = self.get_indent_level(line)
            
            # Vérifier si on doit créer un accordéon
            should_create, title = self.should_create_accordion(line, level)
            
            if should_create and title:
                # Fermer les sections de niveau >= current
                self.close_details_until_level(level)
                
                # Ouvrir nouvel accordéon
                emoji = self.get_emoji_for_level(level)
                self.result.append('<details>')
                self.result.append(f'<summary>{emoji} {title}</summary>')
                self.result.append('')
                
                # Ajouter contenu après ":" si présent
                if ':' in line:
                    parts = line.split(':', 1)
                    if len(parts) > 1 and parts[1].strip():
                        indent_str = ' ' * (level * 4) if level >= 0 else ''
                        self.result.append(f'{indent_str}- {parts[1].strip()}')
                
                # Tracker l'accordéon
                self.open_details.append({
                    'level': level,
                    'title': title
                })
            else:
                # Ligne normale
                self.result.append(line)
            
            i += 1
        
        # Fermer tous les accordéons restants
        while self.open_details:
            self.result.append('</details>')
            self.result.append('')
            self.open_details.pop()
        
        return '\n'.join(self.result)

def process_file(input_file, output_file=None, max_depth=3):
    """Traite le fichier avec profondeur max spécifiée"""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    parser = NotionToGitHub(max_depth=max_depth)
    processed = parser.process_content(lines)
    
    if output_file is None:
        input_path = Path(input_file)
        output_file = input_path.parent / f"{input_path.stem}_github{input_path.suffix}"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(processed)
    
    print(f"✅ Fichier traité : {output_file}")
    print(f"📊 Profondeur max accordéons : {max_depth}")
    print(f"📏 {len(lines)} lignes → {len(processed.split(chr(10)))} lignes")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 notion_to_github_final.py <fichier.md> [profondeur_max]")
        print("")
        print("Profondeur max des accordéons (défaut: 3):")
        print("  0 = Headers ### seulement")
        print("  1 = Headers + listes principales")
        print("  2 = + sous-listes (4 espaces)")
        print("  3 = + sous-sous-listes (8 espaces)")
        print("  99 = Tout")
        print("")
        print("Exemples:")
        print("  python3 notion_to_github_final.py notes.md     # Profondeur 3 (défaut)")
        print("  python3 notion_to_github_final.py notes.md 2   # Profondeur 2")
        print("  python3 notion_to_github_final.py notes.md 99  # Tous les niveaux")
        sys.exit(1)
    
    input_file = sys.argv[1]
    max_depth = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    
    if not Path(input_file).exists():
        print(f"❌ Fichier introuvable : {input_file}")
        sys.exit(1)
    
    process_file(input_file, max_depth=max_depth)
