from pyfiglet import Figlet 

banner = Figlet(font="standard")
print(banner.renderText("Salut, gros bg !"))

true_hash = input("Entre le hash officiel           : ").strip().upper()
app_hash = input("Entre le hash du soft téléchargé : ").strip().upper()

if true_hash == app_hash:
    print("[+] Okkk ça semble safe, le fichier DL correspond bien au hash officiel !")
else:
    print("[!] Oulah va falloir faire attention ce ne sont pas les mêmes !!")

# Aide :
# Penser à installer bibliothèque : python -m pip install pyfiglet
# Windows : Get-FileHash <chemin_du_fichier> -Algorithm SHA256 | Format-List