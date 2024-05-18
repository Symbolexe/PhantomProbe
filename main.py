import readline  # Enable tab completion
import subprocess
import os
import time
import itertools
import colorama
from colorama import Fore, Style

colorama.init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Banner display function
def display_banner():
    os.system('clear')
    banner = "[*] Starting the PhantomProbe Framework"
    for char in banner:
        print(char, end='', flush=True)
        time.sleep(0.1)
    time.sleep(3)
    os.system('clear')
    print(Fore.GREEN + Style.BRIGHT + """
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠿⠿⣷⡄⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⣀⣀⣿⣿⠀⠀⣀⣼⣿⢁⣤⣶⣿⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣶⣤⡀⠀⠀⠀⠀⣿⡿⠛⠛⢻⣿⣤⣾⠿⠛⠁⠙⠋⠁⠀⠀⠉⠙⠻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠟⠉⠀⠉⢻⣿⣦⡀⠀⢸⣿⠃⠀⠀⣠⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⠁⠀⠀⠀⣠⣿⠋⠹⣿⣦⡘⠟⠀⠀⢰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⠁⠀⠠⣶⣿⣿⣧⠀⠀⠈⢻⣷⡄⠀⠀⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣿⡿⠿⢿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠶⢶⣶⣤⣄⠈⢻⣷⠀⠀⠀⠙⣿⣦⣴⣿⣷⣶⣦⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⣠⣶⡿⠛⠁⠀⠀⢸⣿⠇⠈⠛⢿⣷⣄⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⡿⠋⠁⠀⠀⢸⣿⠙⠻⣿⣮⣿⡇⢀⣴⣿⠟⠋⠉⠁⠀⠈⠉⠉⠛⢿⠟⢁⡀⠀⠀⠀⢀⣾⡿⠋⠀⠀⠀⠀⠀⢸⣿⣤⣀⠀⠀⣹⣿⣷⡄⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⢀⣀⣿⡏⠀⠀⠀⠙⠻⣿⣿⣿⣇⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠋⠀⣀⣴⣿⣿⣶⣾⠿⠿⠿⢿⣶⣬⡉⠙⠿⣷⣾⡿⠃⠙⣿⣆⠀
                ⠀⠀⠀⠀⠀⠀⢀⣾⣿⣀⠀⠀⣴⣾⠿⠛⠿⢿⣶⣤⡀⠀⠀⣾⡿⠈⠛⠛⠿⠿⣿⣶⣄⠀⠀⠀⠀⠀⠀⣾⡿⠟⠛⠋⠁⠀⠀⣾⡇⠀⠀⠈⢻⣷⡀⠀⠈⠻⣷⣄⠀⢸⣿⠆
                ⠀⠀⠀⠀⠀⢠⣿⠏⠙⢿⣦⣾⠟⠁⠀⠀⠀⠀⠈⠛⠉⣀⣴⣿⡇⠀⠀⠀⠀⠀⠀⠉⠻⣷⣄⠀⠀⠀⠀⣿⡇⠀⠀⣤⣤⡀⠰⣿⣷⣤⡀⠀⢀⣻⣷⡄⠀⠀⠈⠻⠿⠿⠟⠀
                ⠀⠀⠀⠀⢠⣿⠏⠀⠀⣸⣿⠋⠀⠀⠀⠀⣀⣤⣴⣶⣿⠟⠛⣿⣧⣶⣶⣶⣦⡀⠀⠀⠀⠙⣿⣦⡀⠀⢀⣿⡇⠀⠀⠈⢻⣿⣦⡈⠉⠻⣿⣶⡿⠟⠹⣿⣄⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⢠⣿⣯⡀⠀⣰⣿⠃⠀⠀⢀⣴⣿⠟⠛⠙⢿⣦⣠⡄⣸⣿⠋⠀⣸⣿⠿⢿⣷⡄⠀⠈⠛⠿⣿⣿⡿⢿⣶⣤⣤⣾⠟⠹⣿⣆⠀⠹⣿⣄⠀⠀⠘⢿⣧⡀⠀⠀⠀⠀⠀
                ⠀⣀⣴⡿⠋⠙⢿⣷⣿⠃⠀⠀⣰⣿⠏⠁⠀⠀⢀⣼⣿⠟⠃⣿⡏⠀⢰⣿⠃⠀⢰⣿⢇⣀⣀⣤⣾⡿⠋⢠⣀⠈⠻⣿⣇⠀⠀⠙⣿⣆⠀⠘⢿⣷⡀⠀⣨⣿⣿⣦⣄⡀⠀⠀
                ⣾⡿⠋⠀⠀⢀⣴⣿⠏⠀⢠⣾⣿⣧⠀⠀⠀⢀⣾⡟⠁⠀⢀⣿⣄⠀⣾⡇⠀⠀⣼⡿⠸⠿⠛⣿⡇⠀⠀⣾⣿⠀⠀⠘⣿⣆⣀⣤⣾⣿⡄⠀⠈⠻⣿⣿⡟⠉⠀⠙⠛⢿⣷⠀
                ⢻⣷⣤⣴⣾⠿⠛⠁⠀⣴⣿⠋⠘⠿⣷⣶⡇⢸⣿⣧⣤⣴⣿⠛⠿⠿⣿⣧⣀⣠⣿⠃⠼⣷⣶⣿⡇⠀⣀⣿⣿⠀⠀⠀⢸⣿⠛⠋⠁⣿⣇⠀⠀⠀⠈⠻⣿⣦⣄⣀⣀⣼⣿⠀
                ⠀⠈⠉⠉⠀⠀⠀⢀⣼⡿⠁⠀⢀⣴⣿⠋⠀⣼⡏⠉⠉⣿⡏⠀⠀⠀⠈⠛⣿⣿⠋⠀⠀⣠⣿⣿⣿⠿⠿⣿⣿⠀⠀⠀⠘⣿⡆⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠁⠀
                ⠀⠀⠀⠀⠀⠀⢠⣿⡿⣿⣦⣠⣾⠟⠁⠀⢀⣿⠇⠀⠀⣿⠃⠀⠀⠀⠀⢠⣿⣧⣤⣀⣼⣿⠁⢸⣿⠀⠀⢸⣿⠀⠀⠀⠀⢿⣧⠀⠀⠀⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⣰⣿⠏⠀⠈⣻⣿⠏⠀⠀⠀⣸⣿⣷⣶⣶⡿⠀⠀⠀⠀⠀⢸⣿⠉⠛⠛⣿⠇⠀⢸⣿⠀⠀⣈⣛⠀⠀⠀⠀⠸⣿⣆⣤⣶⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⣰⣿⡏⠀⠀⣼⡿⠃⠀⠀⠀⣴⣿⠇⠀⢨⣿⠃⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⣿⠀⠀⢸⣿⡿⠿⠿⣿⡇⠀⠀⠀⠀⠹⣿⡏⠁⠀⢻⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⣰⣿⠻⣷⣦⣾⡿⠁⠀⠀⠀⠀⢿⣧⣀⣰⣿⠏⠀⠀⠀⠀⠀⠀⢸⣿⣶⣶⣴⣿⠀⠀⠘⣿⡇⠀⠀⣿⡇⠀⠀⠀⠀⠀⢻⣷⡄⠀⠀⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⢰⣿⠃⠀⢀⣿⡟⠁⠀⠀⠀⠀⠀⠈⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⢸⣿⡈⠉⠉⣿⡇⠀⠀⣿⡇⠀⠀⢻⣿⠀⠀⠀⠀⠀⠀⠹⣿⣦⣶⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠸⣿⣦⣠⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣤⣴⡿⠃⠀⠀⢿⣿⣀⣤⣶⣿⣇⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⢸⣿⡟⠉⠉⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡆⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣦⣴⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                              🕷 https://github.com/OxyopesLab/PhantomProbe 🕷
                                  🕸️ [ PhantomProbe v1.0.0-stable ] 🕸️
                                  ♡  [  Yasin Saffari - Symbolexe ]  ♡ 
    """ + Style.RESET_ALL)

def sublist3r(domain):
    subprocess.run(['python3', 'subenum/sublist3r/sublist3r.py', '-d', domain], check=True)

def subfinder(domain):
    subprocess.run(['subenum/subfinder', '-d', domain, '-all'], check=True)

def assetfinder(domain):
    subprocess.run(['subenum/assetfinder', '-subs-only', domain], check=True)

def cero(domain):
    subprocess.run(['subenum/cero-linux-amd64', domain], check=True)

def xorn(domain):
    subprocess.run(['subenum/xorn/xorn', '-d', domain, '-w', 'subdomains.txt', '--status-code', '--title'], check=True)

def csprecon(domain):
    subprocess.run(['recon/csprecon', '-u', "https://" + domain], check=True)

def lazyrecon(domain):
    subprocess.run(['bash', 'recon/lazyrecon.sh', '-d', domain], check=True)

def arjun(domain):
    subprocess.run(['arjun', '-u', "https://" + domain, '--passive'], check=True)

def dnsrecon(domain):
    subprocess.run(['dnsrecon', '-d', domain], check=True)

def dnsenum(domain):
    subprocess.run(['dnsenum', domain], check=True)

def nmap(domain):
    subprocess.run(['nmap', '-Pn', '-sV', '--open', '-sC', domain], check=True)

def wafdetect(domain):
    subprocess.run(['python3', 'scanning/wafw00f/identYwaf.py', '--random-agent', domain], check=True)

def naabu(domain):
    subprocess.run(['content/naabu', '-host', domain], check=True)

def whatweb(domain):
    subprocess.run(['content/whatweb/whatweb', '-a3', '-v', domain], check=True)

def httpx(domain):
    subprocess.run(['content/subfinder', '-d', domain, "-o", "subs.txt"], check=True)
    subprocess.run(['content/httpx', '-title', '-status-code', '-list', 'subs.txt'], check=True)

def katana(domain):
    subprocess.run(['content/katana', '-u', "https://" + domain], check=True)

def raven(domain):
    subprocess.run(['content/raven', "https://" + domain], check=True)

def gau(domain):
    subprocess.run(['content/gau', domain], check=True)

def gospider(domain):
    subprocess.run(['content/gospider', "-q", "-s", "https://" + domain], check=True)

def testssl(domain):
    subprocess.run(['testssl', domain], check=True)

def waybackurls(domain):
    subprocess.run(['content/waybackurls', domain], check=True)

def gdork(domain):
    subprocess.run(['python3', 'content/gdork.py', domain], check=True)

def secretfinder(domain):
    subprocess.run(['python3', 'secrets/SecretFinder/SecretFinder.py', '-i', "https://" + domain + "/", '-e'], check=True)

def theharvester(domain):
    subprocess.run(['python3', 'emails/theHarvester/theHarvester.py', '-d', domain, '-b', 'brave,bing,crtsh,duckduckgo,hackertarget,yahoo,dnsdumpster'], check=True)

def httpsmuggling(domain):
    subprocess.run(['python3', 'vuln/smuggler/smuggler.py', '-u', domain], check=True)

def sqlinjection(domain):
    subprocess.run(['python3', 'vuln/sqlmap/sqlmap.py', '--url', "https://" + domain, '--random-agent', '--risk=3', '--level=5', '--dbs'], check=True)

def commandinjection(domain):
    subprocess.run(['python3', 'vuln/commix/commix.py', "https://" + domain], check=True)

def wordpress(domain):
    subprocess.run(['wpscan', '--url', "https://" + domain, '-e', 'u'], check=True)

def complete(text, state):
    commands = ["use", "set", "run", "back", "help", "exit"]
    options = [
        "subenum/sublist3r", 
        "subenum/subfinder", 
        "subenum/assetfinder",
        "recon/csprecon",
        "recon/lazyrecon",
        "dns/dnsrecon",
        "parameter/arjun",
        "dns/dnsenum",
        "subenum/cero",
        "subenum/xorn",
        "scanning/nmap",
        "scanning/wafdetect",
        "content/naabu",
        "content/whatweb",
        "content/httpx",
        "content/katana",
        "content/raven",
        "content/gau",
        "content/gospider",
        "content/waybackurls",
        "content/gdork",
        "ssl/testssl",
        "secrets/SecretFinder",
        "emails/theharvester",
        "vuln/httpsmuggling",
        "vuln/sqlinjection",
        "vuln/commandinjection",
        "vuln/wordpress"
    ]
    matches = [c for c in commands if c.startswith(text)] + [o for o in options if o.startswith(text)]
    return matches[state] if state < len(matches) else None

def print_help():
    help_text = """
PhantomProbe Commands:
    use <tool_name>      - Select a tool to use
    set <parameter> <value> - Set parameter value (e.g., set domain google.com)
    run                  - Run the selected tool with the set parameters
    back                 - Deselect the current tool
    help                 - Show this help message
    exit                 - Exit the PhantomProbe framework
"""
    print(Fore.CYAN + help_text + Style.RESET_ALL)

def main():
    display_banner()
    print(Fore.GREEN + "Welcome to PhantomProbe Framework!" + Style.RESET_ALL)
    readline.parse_and_bind("tab: complete")
    readline.set_completer(complete)
    readline.set_history_length(1000)
    history_file = os.path.expanduser('~/.phantomprobe_history')
    
    try:
        readline.read_history_file(history_file)
    except FileNotFoundError:
        pass
    
    tool_map = {
        "subenum/sublist3r": sublist3r,
        "subenum/subfinder": subfinder,
        "subenum/assetfinder": assetfinder,
        "subenum/cero": cero,
        "subenum/xorn": xorn,
        "recon/csprecon": csprecon,
        "recon/lazyrecon": lazyrecon,
        "parameter/arjun": arjun,
        "dns/dnsrecon": dnsrecon,
        "dns/dnsenum": dnsenum,
        "scanning/nmap": nmap,
        "scanning/wafdetect": wafdetect,
        "content/naabu": naabu,
        "content/whatweb": whatweb,
        "content/httpx": httpx,
        "content/katana": katana,
        "content/raven": raven,
        "content/gau": gau,
        "content/gospider": gospider,
        "content/waybackurls": waybackurls,
        "content/gdork": gdork,
        "ssl/testssl": testssl,
        "secrets/SecretFinder": secretfinder,
        "emails/theharvester": theharvester,
        "vuln/httpsmuggling": httpsmuggling,
        "vuln/sqlinjection": sqlinjection,
        "vuln/commandinjection": commandinjection,
        "vuln/wordpress": wordpress
    }
    
    selected_tool = None
    domain = None
    base_prompt = "[PhantomProbe]> "
    tool_prompt = None
    
    try:
        while True:
            prompt = tool_prompt if tool_prompt else base_prompt
            user_input = input(prompt).strip()
            
            if not user_input:
                continue
            
            tokens = user_input.split()
            command = tokens[0]
            
            if command == "use":
                if len(tokens) < 2:
                    print(Fore.RED + "Usage: use <tool_name>" + Style.RESET_ALL)
                    continue
                tool_name = tokens[1]
                if tool_name in tool_map:
                    selected_tool = tool_map[tool_name]
                    tool_prompt = f"[PhantomProbe][{tool_name.split('/')[-1]}]> "
                else:
                    print(Fore.RED + "Invalid tool name" + Style.RESET_ALL)
            elif command == "set":
                if len(tokens) < 3:
                    print(Fore.RED + "Usage: set <parameter> <value>" + Style.RESET_ALL)
                    continue
                parameter = tokens[1]
                value = tokens[2]
                if parameter == "domain":
                    domain = value
                    print(Fore.YELLOW + f"[*] DOMAIN => {domain}" + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Invalid parameter" + Style.RESET_ALL)
            elif command == "run":
                if not selected_tool:
                    print(Fore.RED + "Please select a tool before running" + Style.RESET_ALL)
                elif not domain:
                    print(Fore.RED + "Please set a domain before running" + Style.RESET_ALL)
                else:
                    try:
                        selected_tool(domain)
                    except Exception as e:
                        print(Fore.RED + f"Error running tool: {e}" + Style.RESET_ALL)
            elif command == "back":
                selected_tool = None
                tool_prompt = None
            elif command == "help":
                print_help()
            elif command == "exit":
                print(Fore.GREEN + "Exiting PhantomProbe Framework. Goodbye!" + Style.RESET_ALL)
                break
            else:
                try:
                    subprocess.run(user_input, shell=True)
                except Exception as e:
                    print(Fore.RED + f"Error running system command: {e}" + Style.RESET_ALL)
    finally:
        readline.write_history_file(history_file)

if __name__ == '__main__':
    main()
