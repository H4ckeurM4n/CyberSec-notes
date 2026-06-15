#!/bin/bash

chercher_fichier() {
    local file
    local emplacement
    
    read -p "Quel est le fichier ? " file

    if [[ -z "$file" ]]; then
        read -p "Indique un fichier stttp : " file
        if [[ -z "$file" ]]; then
            echo "tant pis le script se ferme, la prochaine fois fais un effort et indique un fichier"
            exit 1
        fi
    fi

    emplacement=$(find / -type f -iname "$file" 2>/dev/null) 

    if [[ -z "$emplacement" ]]; then
        echo "Aucun fichier trouvé pour : $file !"
    else 
        echo -e "$file se trouve à \n$emplacement"
    fi
}

echo "Que veux-tu faire bg ?"
select choix in "Mais où qu'il est ce fichier ??" "Update Discord" "Quitter"; do
    case $choix in
        "Mais où qu'il est ce fichier ??") chercher_fichier ;;
        "Update Discord") sudo nano /usr/share/discord/resources/build_info.json ;;
        "Quitter") echo "Asta la vista baby ! <3" ; break ;;
        *) echo "Fais un choix non ?"
    esac
done
