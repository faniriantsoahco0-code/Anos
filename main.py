from bs4 import BeautifulSoup
import time
from colorama import Fore, Style, init
import requests
import os



init(autoreset=True)




FICHIER = "anos.txt"

headers = {
    "User-Agent": "Mozilla/5.0 (Android; Mobile) AnosScrapingBot/1.0"
}




def scraper(url):

    print(Fore.YELLOW + "\nConnexion au site...")

    debut = time.perf_counter()

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        fin = time.perf_counter()

        temps = fin - debut

        print(Fore.GREEN + f"✓ Site récupéré")
        print(Fore.CYAN + f"Status HTTP : {response.status_code}")
        print(Fore.CYAN + f"Temps       : {temps:.3f} seconde(s)")
        print(Fore.CYAN + f"Taille      : {len(response.text)} caractères")

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        return soup

    except requests.exceptions.Timeout:
        print(Fore.RED + "✗ Temps d'attente dépassé.")

    except requests.exceptions.ConnectionError:
        print(Fore.RED + "✗ Impossible de se connecter au site.")

    except requests.exceptions.HTTPError as erreur:
        print(Fore.RED + f"✗ Erreur HTTP : {erreur}")

    except requests.exceptions.RequestException as erreur:
        print(Fore.RED + f"✗ Erreur : {erreur}")

    return None



url = input(
    Fore.BLUE + "Lien du site : " +
    Fore.GREEN
)

soup = scraper(url)



while True:

    print(Fore.GREEN + r"""
 █████╗ ███╗   ██╗ ██████╗ ███████╗
██╔══██╗████╗  ██║██╔═══██╗██╔════╝
███████║██╔██╗ ██║██║   ██║███████╗
██╔══██║██║╚██╗██║██║   ██║╚════██║
██║  ██║██║ ╚████║╚██████╔╝███████║
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝

        [ SCRAPING BOT v1.0 ]
        [ STATUS: ONLINE ]
    """)

    print(Fore.CYAN + "1. AFFICHER LE CODE SOURCE COMPLET")
    print(Fore.CYAN + "2. AFFICHER EN MODE WEB")
    print(Fore.CYAN + "3. AFFICHER LES BALISES")
    print(Fore.CYAN + "4. ENREGISTRER LE CODE DANS anos.txt")
    print(Fore.CYAN + "5. LIRE LE FICHIER anos.txt")
    print(Fore.CYAN + "6. RAFRAÎCHIR LE SITE")
    print(Fore.CYAN + "7. QUITTER")

    choix = input(
        Fore.YELLOW + "\nChoix : " +
        Fore.WHITE
    ).strip()


    

    if choix == "1":

        if soup is None:
            print(Fore.RED + "Aucune page chargée.")
            continue

        debut = time.perf_counter()

        print(Fore.WHITE + soup.prettify())

        fin = time.perf_counter()

        print(
            Fore.GREEN +
            f"\nTemps d'affichage : {fin - debut:.4f}s"
        )


    elif choix == "2":

        if soup is None:
            print(Fore.RED + "Aucune page chargée.")
            continue

        print(Fore.WHITE + soup.get_text(
            separator="\n",
            strip=True
        ))


    elif choix == "3":

        if soup is None:
            print(Fore.RED + "Aucune page chargée.")
            continue

        balise = input(
            Fore.YELLOW +
            "Nom de la balise (ex: a, p, img, div) : "
        ).strip()

        debut = time.perf_counter()

        resultats = soup.find_all(balise)

        fin = time.perf_counter()

        if resultats:

            print(
                Fore.GREEN +
                f"\n✓ {len(resultats)} balise(s) trouvée(s)"
            )

            print(
                Fore.CYAN +
                f"Temps de recherche : {fin - debut:.6f}s\n"
            )

            for i, element in enumerate(resultats, start=1):

                print(
                    Fore.GREEN +
                    f"\n========== BALISE {i} =========="
                )

                print(
                    Fore.WHITE +
                    element.prettify()
                )

        else:

            print(
                Fore.RED +
                f"\n✗ Balise <{balise}> introuvable."
            )


    elif choix == "4":

        if soup is None:
            print(Fore.RED + "Aucune page à enregistrer.")
            continue

        debut = time.perf_counter()

        with open(
            FICHIER,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(str(soup.prettify()))

        fin = time.perf_counter()

        print(
            Fore.GREEN +
            "\n✓ Code source enregistré avec succès !"
        )

        print(
            Fore.CYAN +
            f"Fichier : {FICHIER}"
        )

        print(
            Fore.CYAN +
            f"Temps : {fin - debut:.6f}s"
        )


    elif choix == "5":

        if not os.path.exists(FICHIER):

            print(
                Fore.RED +
                f"\n✗ Le fichier {FICHIER} n'existe pas."
            )

            continue

        debut = time.perf_counter()

        with open(
            FICHIER,
            "r",
            encoding="utf-8"
        ) as fichier:

            contenu = fichier.read()

        fin = time.perf_counter()

        print(Fore.WHITE + "\n")
        print(contenu)

        print(
            Fore.GREEN +
            f"\nTemps de lecture : {fin - debut:.6f}s"
        )


    elif choix == "6":

        soup = scraper(url)


    elif choix == "7":

        print(
            Fore.GREEN +
            "\nFermeture du Scraping Bot..."
        )

        break


    else:

        print(
            Fore.RED +
            "\n✗ Choix invalide."
        )


    input(
        Fore.YELLOW +
        "\nAppuie sur Entrée pour continuer..."
    )

    os.system("clear" if os.name != "nt" else "cls")
