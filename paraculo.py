import os
import time
import random

# Lista di proxy da usare
proxies = [
    "80.249.112.162:80",
    "4.236.183.37:8080",
    "168.119.141.135:80",
    "103.153.154.6:80",
    "178.128.113.118:23128",
    "84.252.74.190:4444",
    "43.255.113.232:8082",
    "197.255.125.12:80",
    # Altri proxy qui...
]

# Funzione per aggiornare il file di configurazione di ProxyChains
def update_proxychains_conf(proxy):
    config_path = "/etc/proxychains.conf"  # Cambia percorso se necessario
    try:
        with open(config_path, 'r') as file:
            lines = file.readlines()

        # Sostituisci l'ultima voce del proxy con il nuovo proxy
        with open(config_path, 'w') as file:
            for line in lines:
                if line.startswith("socks5") or line.startswith("http") or line.startswith("socks4"):
                    continue  # Rimuove i proxy esistenti
                file.write(line)

            # Aggiungi il nuovo proxy
            file.write(f"http {proxy}\n")

        print(f"ProxyChains configurato con il proxy: {proxy}")

    except Exception as e:
        print(f"Errore nella configurazione di ProxyChains: {e}")

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
    ]

    start_time = time.time()
    while time.time() - start_time < 10:
        for frame in frames:
            print(frame)
            time.sleep(0.5)

# Funzione per configurare il proxy casualmente
def set_random_proxy():
    proxy = random.choice(proxies)
    update_proxychains_conf(proxy)

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
    # Mostra animazione del pianeta Terra rotante
    animate_earth()
    
    # Imposta un proxy casuale e aggiorna la configurazione di ProxyChains
    set_random_proxy()

    # Esegui il menu di installazione per configurare Tor e ProxyChains
    install_menu()

if __name__ == "__main__":
    main()
