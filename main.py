from colorama import Fore
import time
import webbrowser

print(Fore.CYAN + "[==============================]")
print(Fore.YELLOW + "    ANOS VIP PANEL DOWNLOAD "+Fore.YELLOW+"V1.0")
print(Fore.CYAN + "[==============================]")

print(Fore.WHITE+"1: Telecharger le panel ")
print(Fore.WHITE+"2: Contacter l'admin ")
choix = input(Fore.GREEN + "\nChoix: ")


match(choix):
	case "1":
		
		mdp = input(Fore.BLUE+"Mot de passe: ")
		if mdp =="Anos123":
			webbrowser.open("https://www.mediafire.com/file/eoybijq71kooxlk/Anosxyz.apk/file")
		else:
			print(Fore.RED+"Mot de passe incorrect !!")
			print("Redirection en cours")
			time.sleep(3)
			webbrowser.open("https://wa.me/23407071776576")
	case "2":
				webbrowser.open("https://wa.me/23407071776576")
			

