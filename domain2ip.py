import os
import socket
import concurrent.futures
from colorama import Fore, Style, init

init(autoreset=True)

banner = """
   ██████  ██    ██ ██████      ██████  ███████ ███    ███  ██████  ██    ██ ███████
   ██   ██ ██    ██ ██   ██     ██   ██ ██      ████  ████ ██    ██ ██    ██ ██
   ██   ██ ██    ██ ██████      ██████  █████   ██ ████ ██ ██    ██ ██    ██ █████
   ██   ██ ██    ██ ██          ██   ██ ██      ██  ██  ██ ██    ██  ██  ██  ██
   ██████   ██████  ██          ██   ██ ███████ ██      ██  ██████    ████   ███████

                   --------------------------------------
                   |                                    |
                   |            VERSION 1.0             |
                   | DUPLICATE SITE REMOVER BY GRAYBYT3 |
                   |                                    |
                   --------------------------------------
# Graybyt3 - Ex-Blackhat 🖤 | Ex Super Mod of Team_CC.
# Now securing systems as a Senior Security Expert 🛡️.
# I hack servers for fun, patch them to torture you.
#
# "My life is a lie, and i'm living in this only truth.- Graybyt3"
#
# WARNING: This code is for educational and ethical purposes only.
# I am not responsible for any misuse or illegal activities.
#
# WARNING: Steal my code, and I'll call you Pappu — there's no worse shame in this world than being called Pappu.
# #FuCk_Pappu
"""

print("\n\n\n")
print(f"{Fore.RED}░█▀▀█ {Fore.GREEN}░█▀▀█ {Fore.YELLOW}─█▀▀█ {Fore.BLUE}░█──░█ {Fore.MAGENTA}░█▀▀█ {Fore.CYAN}░█──░█ {Fore.RED}▀▀█▀▀ {Fore.GREEN}░█▀▀▀ {Fore.YELLOW}　 {Fore.BLUE}░█▀▀▄ {Fore.MAGENTA}　 {Fore.CYAN}█▀█ {Fore.RED}　 {Fore.GREEN}▀█▀ {Fore.YELLOW}░█▀▀█")
print(f"{Fore.RED}░█─▄▄ {Fore.GREEN}░█▄▄▀ {Fore.YELLOW}░█▄▄█ {Fore.BLUE}░█▄▄▄█ {Fore.MAGENTA}░█▀▀▄ {Fore.CYAN}░█▄▄▄█ {Fore.RED}─░█── {Fore.GREEN}░█▀▀▀ {Fore.YELLOW}　 {Fore.BLUE}░█─░█ {Fore.MAGENTA}　 {Fore.CYAN}─▄▀ {Fore.RED}　 {Fore.GREEN}░█─ {Fore.YELLOW}░█▄▄█")
print(f"{Fore.RED}░█▄▄█ {Fore.GREEN}░█─░█ {Fore.YELLOW}░█─░█ {Fore.BLUE}──░█── {Fore.MAGENTA}░█▄▄█ {Fore.CYAN}──░█── {Fore.RED}─░█── {Fore.GREEN}░█▄▄▄ {Fore.YELLOW}　 {Fore.BLUE}░█▄▄▀ {Fore.MAGENTA}　 {Fore.CYAN}█▄▄ {Fore.RED}　 {Fore.GREEN}▄█▄ {Fore.YELLOW}░█───{Style.RESET_ALL}")
print("\n\n\n")

ENCODINGS = ['utf-8', 'latin-1', 'ascii', 'utf-16', 'iso-8859-1']

def read_domains(file):
    for encoding in ENCODINGS:
        try:
            with open(file, 'r', encoding=encoding) as f:
                return [line.strip() for line in f if line.strip()]
        except (UnicodeDecodeError, FileNotFoundError):
            continue
    print(f"{Fore.RED}[-] Failed to read {file} with any encoding{Style.RESET_ALL}")
    return []

def domain_to_ip(domain, output_file):
    try:
        socket.setdefaulttimeout(2)
        ip = socket.gethostbyname(domain)
        print(f"\033[4m{Fore.GREEN}[+] {domain} > {ip}{Style.RESET_ALL}")
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(ip + '\n')
        return ip
    except (socket.gaierror, socket.timeout):
        print(f"{Fore.RED}[-] {domain} > FuCK{Style.RESET_ALL}")
        return None

def resolve_domains_to_ips(domains, thread_count, output_file):
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
        executor.map(lambda domain: domain_to_ip(domain, output_file), domains)

def write_unique_ips(input_file, unique_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        ips = [line.strip() for line in f if line.strip()]
    unique_ips = sorted(set(ips))
    with open(unique_file, 'w', encoding='utf-8') as f:
        f.writelines(ip + '\n' for ip in unique_ips)

def main():
    input_file = input("Enter the input filename (e.g., sites.txt): ")
    thread_count = int(input("Enter the number of threads: "))
    domains = read_domains(input_file)
    if domains:
        open('ip.txt', 'w').close()
        resolve_domains_to_ips(domains, thread_count, 'ip.txt')
        write_unique_ips('ip.txt', 'unique.txt')

if __name__ == '__main__':
    main()
