#!/bin/bash

chercher_fichier() {
    read -p "Quel est le fichier ? " file

    if [[ -z "$file" ]]; then
        read -p "Indique un fichier stttp : " file
        if [[ -z "$file" ]]; then
            echo "tant pis le script se ferme, la prochaine fois fais un effort et indique un fichier"
            exit 1
        fi
    fi

    emplacement=$(find / -type f -name "$file" 2>/dev/null) 

    if [[ -z "$emplacement" ]]; then
        echo "$file n'existe pas !"
    else 
        echo -e "$file se trouve à \n$emplacement"
    fi
}

echo "Que veux-tu faire bg ?"
select choix in "Mais où qu'il est ce fichier ??" "Update Discord"; do
    case $choix in
        "Mais où qu'il est ce fichier ??") chercher_fichier ;;
        "Update Discord") sudo nano /usr/share/discord/resources/build_info.json ;;
        *) echo "Fais un choix non ?"
    esac
done
