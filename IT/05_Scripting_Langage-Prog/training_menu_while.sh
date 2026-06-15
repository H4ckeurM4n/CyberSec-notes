#!/bin/bash

pause(){

	read -p "Appuyer sur la touche [Enter] pour continuer..." key
    
}

liste_all_txt(){
    local list

    list=$(find . -type f -name "*.txt" 2>/dev/null)

    if [[ -z "$list" ]]; then
        echo "Il n'y a aucun fichier .txt dans le répertoire actuel ni dans les sous-dossiers"
    else
        echo -e "Voici la liste des fichiers .txt \n "$list""
    fi
    pause

}

compter_nbr_lignes(){
    local file
    local file_lignes

    read -p "Quel fichier voulez-vous analyser ? " file

    if [[ -z "$file" ]]; then
        echo "Veuillez renseigner un fichier"
    elif [[ ! -f "$file" ]]; then
        echo "Erreur : ce fichier n'existe pas"
    else
        file_lignes=$(<"$file" wc -l)
        echo -e "Nombre de ligne(s) dans "$file" : "$file_lignes"" 
    fi
    pause

}

while true; do
    # Affiche menu
    clear
    echo "---------------------------------"
	echo "	     M A I N - M E N U"
	echo "---------------------------------"
    echo "1. Lister tous les fichiers .txt dans le répertoire courant et en-dessous"
    echo "2. Compter le nombre de lignes dans un fichier donné"
    echo "3. Quitter"
    echo "---------------------------------"
    read -r -p "Quel est votre choix ? " choix

    
    case $choix in
        -l|lister|1) liste_all_txt ;;
        -n|number|2) compter_nbr_lignes ;;
        -q|quit|3) echo "Au revoir." ; break ;;
        *) echo "Sélectionnez votre choix"; pause ;;
    esac
done