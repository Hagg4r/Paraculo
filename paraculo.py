import os
import time
import random

# Proxy da usare
proxies = [
    "socks5://10.10.1.1:9050",
    "socks5://10.10.1.2:9050",
    "socks5://10.10.1.3:9050",
    "socks5://10.10.1.4:9050"
]

# Funzione per cancellare il terminale
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Animazione del pianeta Terra rotante con segnali lampeggianti
def animate_earth():
    frames = [
        """
        .         .        .            .
       _____      _______      _______      _____
      /     \\    /       \\    /       \\    /     \\
     |  o o  |  |  o o o  |  | o o o o |  |  o o  |
      \\_____/    \\_______/    \\_______/    \\_____/
        .            .          .          .  
     """,
        """
        .         .        .            .
       _____      _______      _______      _____
      /     \\    /       \\    /       \\    /     \\
     | o o o |  | o o o o |  | o o o o |  | o o o |
      \\_____/    \\_______/    \\_______/    \\_____/
        .            .          .          .  
     """,
        """
        .         .        .            .
       _____      _______      _______      _____
      /     \\    /       \\    /       \\    /     \\
     | o o o |  | o o o o |  | o o o o |  | o o o |
      \\_____/    \\_______/    \\_______/    \\_____/
        .            .          .          .  
     """,
    ]

    # Mostra l'animazione per 10 secondi
    start_time = time.time()
    while time.time() - start_time < 10:
        for frame in frames:
            clear_terminal()
            print(frame)
            time.sleep(0.5)

# Funzione per configurare il proxy
def set_proxy():
    # Seleziona un proxy casuale dalla lista
    selected_proxy = random.choice(proxies)
    print(f"\nImpostando proxy: {selected_proxy}")
    
    # Imposta le variabili d'ambiente per l'uso di proxy (SOCKS5)
    os.environ['http_proxy'] = selected_proxy
    os.environ['https_proxy'] = selected_proxy
    os.environ['ftp_proxy'] = selected_proxy
    os.environ['socks_proxy'] = selected_proxy

    print("\nProxy impostato correttamente. Ora il traffico sarà instradato attraverso il proxy.")

# Menu per installazione su diversi OS
def install_menu():
    print("Seleziona il tuo sistema operativo per configurare Tor e ProxyChains:")
    print("1. Windows")
    print("2. iSH (iOS)")
    print("3. Termux (Android)")
    print("4. Kali Linux")
    print("5. Parrot OS")
    print("6. Predator OS")
    print("7. Oscar OS")
    
    choice = input("\nInserisci il numero del tuo sistema operativo: ")
    
    if choice == '1':
        install_windows()
    elif choice == '2':
        install_ish()
    elif choice == '3':
        install_termux()
    elif choice == '4':
        install_kali()
    elif choice == '5':
        install_parrot()
    elif choice == '6':
        install_predator()
    elif choice == '7':
        install_oscar()
    else:
        print("Scelta non valida, riprova.")

# Funzioni di installazione per diversi OS
def install_windows():
    print("\nInstallazione su Windows...")
    os.system('winget install Tor')
    os.system('winget install ProxyChains')
    print("Installazione completata su Windows.")

def install_ish():
    print("\nInstallazione su iSH...")
    os.system('apk add tor proxychains')
    print("Installazione completata su iSH.")

def install_termux():
    print("\nInstallazione su Termux...")
    os.system('pkg install tor proxychains')
    print("Installazione completata su Termux.")

def install_kali():
    print("\nInstallazione su Kali Linux...")
    os.system('apt-get install tor proxychains')
    print("Installazione completata su Kali Linux.")

def install_parrot():
    print("\nInstallazione su Parrot OS...")
    os.system('apt-get install tor proxychains')
    print("Installazione completata su Parrot OS.")

def install_predator():
    print("\nInstallazione su Predator OS...")
    os.system('apt-get install tor proxychains')
    print("Installazione completata su Predator OS.")

def install_oscar():
    print("\nInstallazione su Oscar OS...")
    os.system('apt-get install tor proxychains')
    print("Installazione completata su Oscar OS.")

# Funzione principale per eseguire tutto
def main():
    clear_terminal()
    
    # Mostra animazione del pianeta Terra rotante
    animate_earth()
    
    # Esegui il menu di installazione per configurare Tor e ProxyChains
    install_menu()
    
    # Configura il proxy casuale
    set_proxy()

    # Avvio di Tor e ProxyChains
    print("\nAvvio di Tor e ProxyChains per instradare il traffico in modo sicuro...")
    os.system('service tor start')  # Avvia il servizio Tor
    os.system('proxychains curl http://check.torproject.org')  # Test connessione con ProxyChains

if __name__ == "__main__":
    main()
