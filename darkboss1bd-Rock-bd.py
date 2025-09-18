import os
import sys
import webbrowser

# Auto open your links on script start
try:
    webbrowser.open("https://t.me/darkvaiadmin")
    webbrowser.open("https://serialkey.top/")
except:
    pass  # Ignore if browser fails to open

# Set terminal title
os.system("printf '\033]2;darkboss1bd OSINT Tool v2.0 🔓\a'")

# Try importing required modules
try:
    import requests
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError as e:
    print("\n" + "="*60)
    print("⚠️  DEPENDENCY ERROR — MODULES NOT INSTALLED!")
    print("="*60)
    print("You need to install these modules first:")
    print(Fore.CYAN + "pip install requests colorama" + Style.RESET_ALL)
    print("\nRun the above command in your terminal, then restart this tool.")
    print("="*60)
    input("\nPress ENTER to exit...")
    sys.exit(1)

def mostrar_banner():
    banner = f"""
{Fore.GREEN}██████╗  █████╗ ██╗  ██╗███████╗ ██████╗ ██████╗ ███╗   ██╗
{Fore.GREEN}██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔═══██╗██╔══██╗████╗  ██║
{Fore.GREEN}██║  ██║███████║█████╔╝ █████╗  ██║   ██║██████╔╝██╔██╗ ██║
{Fore.GREEN}██║  ██║██╔══██║██╔═██╗ ██╔══╝  ██║   ██║██╔══██╗██║╚██╗██║
{Fore.GREEN}██████╔╝██║  ██║██║  ██╗███████╗╚██████╔╝██║  ██║██║ ╚████║
{Fore.GREEN}╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
{Style.RESET_ALL}
{Fore.WHITE}{Style.BRIGHT}== 🔍 darkboss1bd Infostealer Intelligence Tool (PRO) 👁 =={Style.RESET_ALL}
"""
    print(banner)
    spaces = 25
    print(f"{' ' * spaces}{Fore.WHITE}{Style.BRIGHT}By: darkboss1bd{Style.RESET_ALL}")
    print(f"{' ' * spaces}{Fore.CYAN}Telegram: @darkvaiadmin{Style.RESET_ALL}")
    print(f"{' ' * spaces}{Fore.CYAN}Website: serialkey.top{Style.RESET_ALL}\n")

def consultar_api(tipo, valor):
    base_urls = {
        'email': f'https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-email?email={valor}',
        'username': f'https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-username?username={valor}',
        'domain': f'https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-domain?domain={valor}',
        'urls-by-domain': f'https://cavalier.hudsonrock.com/api/json/v2/osint-tools/urls-by-domain?domain={valor}',
        'ip': f'https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-ip?ip={valor}'
    }

    url = base_urls.get(tipo)
    if not url:
        print(Fore.RED + "Invalid query type.")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print(Fore.CYAN + "\n--- Results ---")
        print_formato_plano(data)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Request failed: {e}")
    except ValueError:
        print(Fore.RED + "Invalid response received from server.")

def print_formato_plano(data, indent=0, in_stealers=False):
    excluded_fields = {'message', 'logo', 'is_shopify'}
    important_fields = {
        'total_corporate_services', 'total_user_services', 'date_compromised',
        'computer_name', 'operating_system', 'malware_path', 'ip',
        'top_passwords', 'top_logins', 'stealer_family', 'total',
        'totalStealers', 'employees', 'users', 'third_parties', 'totalUrls',
        'url', 'type', 'occurrence'
    }
    
    if isinstance(data, dict):
        if not in_stealers and 'stealers' in data:
            print_formato_plano(data['stealers'], indent, True)
            return
            
        for key, value in data.items():
            if key in excluded_fields:
                continue
                
            if key in important_fields:
                if key in ['top_passwords', 'top_logins']:
                    print("  " * indent + f"{Fore.RED}{key.upper()}:{Style.RESET_ALL}")
                else:
                    print("  " * indent + f"{Fore.YELLOW}{key}:{Style.RESET_ALL}")
                print_formato_plano(value, indent + 1, in_stealers)
            else:
                print_formato_plano(value, indent, in_stealers)
                
    elif isinstance(data, list):
        if in_stealers:
            for i, item in enumerate(data, 1):
                print("  " * indent + f"{Fore.GREEN}--- INFOSTEALER {i} ---{Style.RESET_ALL}")
                print_formato_plano(item, indent + 1, True)
        else:
            for item in data:
                print_formato_plano(item, indent, in_stealers)
    else:
        if data is not None and str(data).strip() not in ['', 'Not Found']:
            print("  " * indent + str(data))

def menu():
    print(f"\n{Fore.GREEN}[1]{Style.RESET_ALL} - Search by Email")
    print(f"{Fore.GREEN}[2]{Style.RESET_ALL} - Search by Username")
    print(f"{Fore.GREEN}[3]{Style.RESET_ALL} - Search by Domain")
    print(f"{Fore.GREEN}[4]{Style.RESET_ALL} - Search URLs by Domain")
    print(f"{Fore.GREEN}[5]{Style.RESET_ALL} - Search by IP Address")
    print(f"{Fore.GREEN}[0]{Style.RESET_ALL} - Exit")

    opcion = input(Fore.CYAN + "\nSelect an option: ").strip()

    if opcion == '1':
        valor = input("Enter email: ").strip()
        if valor: consultar_api('email', valor)
        else: print(Fore.RED + "Email cannot be empty.")
    elif opcion == '2':
        valor = input("Enter username: ").strip()
        if valor: consultar_api('username', valor)
        else: print(Fore.RED + "Username cannot be empty.")
    elif opcion == '3':
        valor = input("Enter domain: ").strip()
        if valor: consultar_api('domain', valor)
        else: print(Fore.RED + "Domain cannot be empty.")
    elif opcion == '4':
        valor = input("Enter domain: ").strip()
        if valor: consultar_api('urls-by-domain', valor)
        else: print(Fore.RED + "Domain cannot be empty.")
    elif opcion == '5':
        valor = input("Enter IP address: ").strip()
        if valor: consultar_api('ip', valor)
        else: print(Fore.RED + "IP cannot be empty.")
    elif opcion == '0':
        print(Fore.GREEN + "Goodbye! — darkboss1bd 💀")
        exit()
    else:
        print(Fore.RED + "Invalid option. Please try again.")

if __name__ == "__main__":
    mostrar_banner()
    while True:
        try:
            menu()
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n\nExiting gracefully... darkboss1bd out! 👾")
            break
        except Exception as e:
            print(Fore.RED + f"\nUnexpected error: {e}")
            input("Press ENTER to continue...")
