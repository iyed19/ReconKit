import os
import subprocess
import ipaddress
import shutil
import re



# ===================
#   Terminal Colors
# ===================

RED     = "\033[31m"
BRIGHT_RED  = "\033[91m"
GREEN   = "\033[32m"
BRIGHT_GREEN = "\033[92m"
YELLOW  = "\033[33m"
BRIGHT_YELLOW = "\033[93m"
BLUE    = "\033[34m"
BRIGHT_BLUE  = "\033[94m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

RESET   = "\033[0m"




def show_banner():
    # \033[36m sets the color to Cyan
    # \033[0m resets the formatting back to default
    banner = """\033[92m
 ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗  ██╗██╗████████╗
 ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║██║ ██╔╝██║╚══██╔══╝
 ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║█████╔╝ ██║   ██║   
 ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║██╔═██╗ ██║   ██║   
 ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██║  ██╗██║   ██║   
 ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝   ╚═╝   
\033[0m"""
    print(banner)
    #print("                          Eyad Mnassri")
    
    
    
def check_tool(tool):
    if shutil.which(tool):
        #print(f"\n [{BRIGHT_GREEN}+{RESET}] {tool} {BRIGHT_GREEN}is installed. {RESET}")
        return True
    else:
        print(f"\n [{BRIGHT_RED}-{RESET}] {tool} {RED}is not installed. {RESET}")
        return False



def is_root():
    return hasattr(os, "geteuid") and os.geteuid() == 0



def require_root(scan_name):
    if not is_root():
        print(f"\n [{BRIGHT_RED}-{RESET}] {scan_name} requires {BRIGHT_RED}root{RESET} privileges. Run ReconKit with {GREEN}sudo{RESET}.")
        return False
    return True



def valid_target(target):
    # Reject empty targets, whitespace, and anything nmap would read as an option
    if not target or target.startswith("-") or re.search(r"\s", target):
        print(f"\n [{BRIGHT_RED}-{RESET}] Invalid target")
        return False
    return True

    
    
def nmap_scan(target_ip):
    
    while True:
        print ("\n What do you want to do ? ")
        print ("\n [1] Scan a network ")
        print ("\n [2] Run default scripts + service version ")
        print ("\n [3] Run default scripts + service version + vulnerability scripts ")
        print ("\n [4] Run a specific script ")
        print ("\n [5] Scan all ports (1 to 65535) ")
        print ("\n [6] Scan a specific port ")
        print ("\n [7] Scan UDP ports ")
        print ("\n [8] OS detection ")
        print ("\n [9] Spoof resource IP ")
        print ("\n [10] Stealth scan (TCP SYN) ")
        print ("\n [0] Back to Main Menu ")
        
        nmap_choice = input("\n Your choice (0-10) : ")
        
        if nmap_choice == "1" :
            network_scan(target_ip)
        elif nmap_choice == "2" :
            default_scripts_and_service_version_scan(target_ip)
        elif nmap_choice == "3" :
            default_and_vuln_scripts_and_version_scan(target_ip)
        elif nmap_choice == "4" :
            specific_script(target_ip)
        elif nmap_choice == "5" :
            all_ports_scan(target_ip)
        elif nmap_choice == "6" :
            specific_port_scan(target_ip)
        elif nmap_choice == "7" :
            udp_scan(target_ip)
        elif nmap_choice == "8" :
            os_scan(target_ip)
        elif nmap_choice == "9" :
            spoof_resource_ip(target_ip)
        elif nmap_choice == "10" :
            stealth_scan(target_ip)
        elif nmap_choice == "0" :
            return
        else :
            print ("\n Invalid choice!")
    


def web_scan(target_ip):
    
    while True:
        print ("\n What do you want to do ? ")
        print ("\n [1] Web page and directory brute force ")
        print ("\n [2] HTTP/HTTPS Headers ")
        print ("\n [3] Detect and identify WAFs")
        print ("\n [4] Identify web technologies used")
        print ("\n [5] All-in one web reconnaissance")
        print ("\n [0] Back to Main Menu ")
        
        web_choice = input("\n Your choice (0-5) : ")
        
        if web_choice == "1" :
            if (check_tool("gobuster") == True) :
                web_pages_bruteforce(target_ip)
            else:
                print("\n Please install [ gobuster ] to proceed in this function")
                break
        elif web_choice == "2" :
            http_headers_scan(target_ip)
        elif web_choice == "3" :
            if (check_tool("wafw00f") == True) :
                waf_check(target_ip)
            else:
                print("\n Please install [ wafw00f ] to proceed in this function")
                break
        elif web_choice == "4" :
            if (check_tool("whatweb") == True) :
                web_tech_check(target_ip)
            else:
                print("\n Please install [ whatweb ] to proceed in this function")
                break
        elif web_choice == "5" :
            if (check_tool("finalrecon") == True) :
                web_complete_check(target_ip)
            else:
                print("\n Please install [ finalrecon ] to proceed in this function")
                break
        elif web_choice == "0" :
            return
        else :
            print ("\n Invalid choice!")
            
            
 
def dns_scan(target_ip):
    
    while True:
        print ("\n What do you want to do ? ")
        print ("\n [1] Subdomain passive discovery ")
        print ("\n [2] Subdomain brute force - Gobuster ")
        print ("\n [3] Subdomain brute force - DNSEnum ")
        print ("\n [4] Record enumeration")
        print ("\n [0] Back to Main Menu ")
        
        dns_choice = input("\n Your choice (0-4) : ")
        
        if dns_choice == "1" :
            if (check_tool("subfinder") == True) :
                subdomain_passive(target_ip)
            else:
                print("\n Please install [ subfinder ] to proceed in this function")
                break
        elif dns_choice == "2" :
            if (check_tool("gobuster") == True) :
                subdomain_bruteforce(target_ip, dns_choice)
            else:
                print("\n Please install [ gobuster ] to proceed in this function")
                break
        elif dns_choice == "3" :
            if (check_tool("dnsenum") == True) :
                subdomain_bruteforce(target_ip, dns_choice)
            else:
                print("\n Please install [ dnsenum ] to proceed in this function")
                break
        elif dns_choice == "4" :
            if (check_tool("dnsrecon") == True) :
                record_enum(target_ip)
            else:
                print("\n Please install [ dnsrecon ] to proceed in this function")
                break
        elif dns_choice == "0" :
            return
        else :
            print ("\n Invalid choice!")
            
            
            
def common_services_scan(target_ip):
    
    while True:
        print ("\n What do you want to do ? ")
        print ("\n 1. SMB ")
        print ("\n 2. SQL Databases ")
        print ("\n 3. SMTP/IMAP/POP3 ")
        print ("\n 4. FTP ")
        print ("\n 5. RDP ")
        print ("\n 0. Back to Main Menu ")
        
        srvc_choice = input("\n Your choice (0-5) : ")
        
        if srvc_choice == "1" :
            break
        elif srvc_choice == "2" :
            break
        elif srvc_choice == "3" :
            break
        elif srvc_choice == "4" :
            break
        elif srvc_choice == "5" :
            break
        elif srvc_choice == "0" :
            return
        else :
            print ("\n Invalid choice!")
            
            

def file_scan():
    
    while True:
        print ("\n What do you want to do ? ")
        print ("\n 1. Read Metadata of a local file ")
        #print ("\n 2. . ")
        #print ("\n 3. . ")
        print ("\n 0. Back to Main Menu ")
        
        file_scan_choice = input("\n Your choice (0-1) : ")
        
        if file_scan_choice == "1" :
            if (check_tool("exiftool") == True) :
                exiftool_metadata_extract()
            else:
                print("\n Please install [ exiftool ] to proceed in this function")
                break
        #elif file_scan_choice == "2" :
            #break
        #elif file_scan_choice == "3" :
            #break
        elif file_scan_choice == "0" :
            return
        else :
            print ("\n Invalid choice!")
   
   
   
def run_scan(options, target_ip):
    if not valid_target(target_ip):
        return
    output_args = save_result()
    run_tool(["nmap"] + options + output_args + [target_ip])


def run_network_scan(target_ip, subnet):
    try:
        network = ipaddress.ip_network(f"{target_ip}/{subnet}", strict=False)
    except ValueError:
        print("\n Network scans need an IP address (e.g. 192.168.1.10), not a domain name.")
        return

    if network.prefixlen < 16:
        confirm = input(f"\n {network} is very large ({network.num_addresses} addresses). Continue? (y/n): ")
        if confirm.strip().lower() != "y":
            return

    output_args = save_result()
    run_tool(["nmap", "-sn"] + output_args + [str(network)])


def save_result():

    folder = "results"
    os.makedirs(folder, exist_ok=True)

    while True:
        save_q = input("\n Save results? (y/n): ").strip()

        if save_q.lower() == "y":

            # basename() strips any path parts so the file stays inside results/
            file_name = os.path.basename(input("File name: ").strip())
            if file_name == "":
                print("Invalid file name")
                continue

            while True:
                print("\n Format : ")
                print("\n [1] Normal (.nmap) ")
                print("\n [2] XML (.xml) ")
                print("\n [3] Grepable (.gnmap) ")
                print("\n [4] All (-oA) ")

                format_choice = input("\n Your choice (1-4) : ")

                if format_choice == "1":
                    return ["-oN", os.path.join(folder, file_name + ".nmap")]
                elif format_choice == "2":
                    return ["-oX", os.path.join(folder, file_name + ".xml")]
                elif format_choice == "3":
                    return ["-oG", os.path.join(folder, file_name + ".gnmap")]
                elif format_choice == "4":
                    return ["-oA", os.path.join(folder, file_name)]
                else:
                    print("\n Invalid choice!")

        elif save_q.lower() == "n":
            return []
        else:
            print("\n Invalid answer!")


def all_ports_scan(target_ip):
    print("\n Executing all ports scan ...")
    run_scan(["-p-", "-Pn"], target_ip)


def specific_port_scan(target_ip):
    while True:
        port = input("\n Enter one port (0 to cancel) : ").strip()
        if port == "0":
            return
        if port.isdigit() and 1 <= int(port) <= 65535:
            run_scan(["-p", port, "-Pn"], target_ip)   # was: target (NameError)
            return
        print("\n Enter a valid port (1-65535)")


def udp_scan(target_ip):
    print("\n Executing UDP scan ...")
    if require_root("UDP scan"):
        run_scan(["-sU", "-Pn"], target_ip)


def os_scan(target_ip):
    print("\n Executing OS detection scan ...")
    if require_root("OS detection"):
        run_scan(["-O", "-Pn"], target_ip)


def default_scripts_and_service_version_scan(target_ip):
    print("\n Executing default nmap scripts and service version scan ...")
    run_scan(["-sV", "-sC", "-Pn"], target_ip)


def default_and_vuln_scripts_and_version_scan(target_ip):
    print("\n Executing default and vulnerability scripts and version scan ...")
    run_scan(["-sV", "-sC", "--script", "vuln", "-Pn"], target_ip)


def specific_script(target_ip):
    script = input("\n Enter your script name : ").strip()

    # Allow only normal script names/categories/wildcards, e.g. http-title, "default,safe", "smb-*"
    if not re.fullmatch(r"[A-Za-z0-9_.,*\-]+", script) or script.startswith("-"):
        print("\n Invalid script name")
        return

    print("\n Executing", script, "scan ...")
    run_scan(["--script", script, "-Pn"], target_ip)


def spoof_resource_ip(target_ip):
    spoof_ip = input("\n Enter your spoof IP : ").strip()
    try:
        ipaddress.ip_address(spoof_ip)
    except ValueError:
        print("\n Invalid IP address")
        return

    interface = input("\n Network interface (e.g. eth0) : ").strip()
    if not re.fullmatch(r"[A-Za-z0-9_.\-]+", interface) or interface.startswith("-"):
        print("\n Invalid interface")
        return

    print("\n Note: replies go to the spoofed IP, so you will likely not see results.")
    if require_root("Spoofed scan"):
        run_scan(["-S", spoof_ip, "-e", interface, "-sV", "-sC", "-Pn"], target_ip)


def stealth_scan(target_ip):
    print("\n Executing SYN scan ...")
    if require_root("SYN scan"):
        run_scan(["-sS"], target_ip)



def web_pages_bruteforce(target_ip):
    
    SECLISTS = "/usr/share/seclists"
    if not os.path.exists(SECLISTS):
        print("\n")
        print("=" * 32)
        print("   SecLists is not installed.")
        print("=" * 32)
        return
    
    while True:
        print ("\n What do you want to do ? ")
        print ("\n [1] Run quick pages scan ")
        print ("\n [2] Run balanced pages scan ")
        print ("\n [3] Run deep pages scan ")
        print ("\n [4] Run very deep pages scan (takes so much time!) ")
        print ("\n [0] Back to Main Menu ")
        
        scan_choice = input("\n Your choice (0-4) : ")
        
        if scan_choice == "1":
            web_pg_bf(target_ip,"/usr/share/seclists/Discovery/Web-Content/common.txt")
        elif scan_choice == "2":
            web_pg_bf(target_ip,"/usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt")
        elif scan_choice == "3":
            web_pg_bf(target_ip,"/usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt")
        elif scan_choice == "4":
            web_pg_bf(target_ip,"/usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-big.txt")
        elif scan_choice == "0" :
            return
        else :
            print ("\n Invalid choice!")
    
    

def subdomain_bruteforce(target_ip, dns_choice):
    
    SECLISTS = "/usr/share/seclists"
    if not os.path.exists(SECLISTS):
        print("\n")
        print("=" * 32)
        print("   SecLists is not installed.")
        print("=" * 32)
        return
    
    while True:
        print ("\n What do you want to do ? ")
        print ("\n [1] Run quick subdomains scan ")
        print ("\n [2] Run balanced subdomains scan ")
        print ("\n [3] Run deep subdomains scan ")
        print ("\n [4] Run very deep subdomains scan (takes so much time!) ")
        print ("\n [0] Back to Main Menu ")
        
        scan_choice = input("\n Your choice (0-4) : ")
        
        if dns_choice == "2":
            if scan_choice == "1":
                subdomain_gobuster_bf(target_ip,"/usr/share/seclists/Discovery/DNS/services-names.txt")
            elif scan_choice == "2":
                subdomain_gobuster_bf(target_ip,"/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt")
            elif scan_choice == "3":
                subdomain_gobuster_bf(target_ip,"/usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt")
            elif scan_choice == "4":
                subdomain_gobuster_bf(target_ip,"/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt")
            elif scan_choice == "0" :
                return
            else :
                print ("\n Invalid choice!")
        elif dns_choice == "3":
            if scan_choice == "1":
                subdomain_dnsenum_bf(target_ip,"/usr/share/seclists/Discovery/DNS/services-names.txt")
            elif scan_choice == "2":
                subdomain_dnsenum_bf(target_ip,"/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt")
            elif scan_choice == "3":
                subdomain_dnsenum_bf(target_ip,"/usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt")
            elif scan_choice == "4":
                subdomain_dnsenum_bf(target_ip,"/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt")
            elif scan_choice == "0" :
                return
            else :
                print ("\n Invalid choice!")
        
            
            

def subdomain_passive(target_ip):
    
    command = [
        "subfinder",
        "-d", target_ip
    ]
    
    colored_tool = f"{CYAN}subfinder {RESET}"
    colored_options = f"{GREEN}-d {RESET}"
    colored_ip = f"{RESET}{target_ip}"

    full_cmd_display = colored_tool + colored_options + colored_ip

    run_tool(command, full_cmd_display)
        
        
        
def record_enum(target_ip):
    
    save_name = f"dns_records_{target_ip}"
    
    command = [
        "dnsrecon",
        "-d", target_ip,
        "-c", save_name
    ]
    
    colored_tool = f"{CYAN}dnsrecon {RESET}"
    colored_option1 = f"{GREEN}-d {RESET}"
    colored_ip = f"{RESET}{target_ip}"
    colored_option2 = f"{GREEN} -c {RESET}"
    colored_file_name = f"{RESET}{save_name}"

    full_cmd_display = colored_tool + colored_option1 + colored_ip + colored_option2 + colored_file_name

    run_tool(command, full_cmd_display)



def waf_check(target_ip):
    
    command = [
        "wafw00f",
        target_ip
    ]
    
    colored_tool = f"{CYAN}wafw00f {RESET}"
    colored_ip = f"{RESET}{target_ip}"

    full_cmd_display = colored_tool + colored_ip

    run_tool(command, full_cmd_display)



def web_tech_check(target_ip):
    
    command = [
        "whatweb",
        target_ip
    ]
    
    colored_tool = f"{CYAN}whatweb {RESET}"
    colored_ip = f"{RESET}{target_ip}"

    full_cmd_display = colored_tool + colored_ip

    run_tool(command, full_cmd_display)
        
        
        
def web_complete_check(target_ip):
    
    while True:
        protocol = input("\n Protocol (http/https) : ").strip()
        
        if protocol == "http" :
            url = f"http://{target_ip}"
            break   
        elif protocol == "https":
            url = f"https://{target_ip}"
            break
        else:
            print ("\n Invalid answer!")
            
    command = [
        "finalrecon",
        "--full",
        "--url", url
    ]
    
    colored_tool = f"{CYAN}finalrecon {RESET}"
    colored_options = f"{GREEN}--full --url {RESET}"
    colored_ip = f"{RESET}{url}"

    full_cmd_display = colored_tool + colored_options + colored_ip

    run_tool(command, full_cmd_display)
    
    
    
def web_pg_bf(target_ip, wordlist):

    while True:
        protocol = input("\n Protocol (http/https) : ").strip()
        
        if protocol == "http" :
            url = f"http://{target_ip}"
            break   
        elif protocol == "https":
            url = f"https://{target_ip}"
            break
        else:
            print ("\n Invalid answer!")
            
    command = [
        "gobuster",
        "dir",
        "-u", url,
        "-w", wordlist,
        "-x", "html,js,php,txt,zip,aspx",
        "-t", "30"
    ]

    colored_tool = f"{CYAN}gobuster {RESET}"
    colored_dir = "dir "
    colored_opt1 = f"{GREEN}-u {RESET}{url}"
    colored_opt2 = f"{GREEN} -w {RESET}"
    colored_opt3 = f"{GREEN} -x {RESET}html,js,php,txt,zip,aspx"
    colored_opt4 = f"{GREEN} -t {RESET}30 "

    full_cmd_display = colored_tool + colored_dir + colored_opt1 + colored_opt2 + wordlist + colored_opt3 + colored_opt4 

    run_tool(command, full_cmd_display)

        
        
        
def subdomain_gobuster_bf(target_ip, wordlist):
            
    command = [
        "gobuster",
        "dns",
        "--do", target_ip,
        "-w", wordlist,
        "--no-error"
    ]
    
    colored_tool = f"{CYAN}gobuster {RESET}"
    colored_dns = "dns "
    colored_opt1 = f"{GREEN}--do {RESET}"
    colored_opt2 = f"{GREEN} -w {RESET}"
    colored_opt3 = f"{GREEN} --no-error{RESET}"
    colored_ip = f"{RESET}{target_ip}"

    full_cmd_display = colored_tool + colored_dns + colored_opt1 + colored_ip + colored_opt2 + wordlist + colored_opt3

    run_tool(command, full_cmd_display)
        
        
        
def subdomain_dnsenum_bf(target_ip, wordlist):
            
    command = [
        "dnsenum",
        "--enum", target_ip,
        "-f", wordlist,
        "-r"
    ]
    
    colored_tool = f"{CYAN}dnsenum {RESET}"
    colored_opt1 = f"{GREEN}--enum {RESET}"
    colored_opt2 = f"{GREEN} -f {RESET}"
    colored_opt3 = f"{GREEN} -r{RESET}"
    colored_ip = f"{RESET}{target_ip}"

    full_cmd_display = colored_tool + colored_opt1 + colored_ip + colored_opt2 + wordlist + colored_opt3

    run_tool(command, full_cmd_display)
        
        
        
def network_scan(target_ip):
    
    while True:
        print ("\n What do you want to scan ? ")
        print ("\n [1] Scan default /24 network ")
        print ("\n [2] Scan /25 network ")
        print ("\n [3] Scan /26 network ")
        print ("\n [4] Scan /27 network ")
        print ("\n [5] Enter custom subnet ")
        print ("\n [0] Back to Main Menu ")
        
        net_scan_choice = input("\n Your choice (0-5) : ")
        
        if net_scan_choice == "1" :
            run_network_scan(target_ip, "24")
        elif net_scan_choice == "2" :
            run_network_scan(target_ip, "25")
        elif net_scan_choice == "3" :
            run_network_scan(target_ip, "26")
        elif net_scan_choice == "4" :
            run_network_scan(target_ip, "27")
        elif net_scan_choice == "5" :
            
            custom_subnet = input ("\n Enter custom subnet 0-32 : ").strip()
            
            if not custom_subnet.isdigit():
                print("\n Invalid subnet")  
            else :
                subnet_val = int(custom_subnet)
                if subnet_val < 0 or subnet_val > 32:
                    print("\n Subnet must be between 0 and 32")
                else :
                    run_network_scan(target_ip, str(subnet_val))
            
        elif net_scan_choice == "0" :
            return
        else :
            print ("\n Invalid choice!")
            
            
            
def http_headers_scan(target_ip):
    
    while True:
        
        if target_ip.startswith("http://") or target_ip.startswith("https://") :
            url = target_ip
            break
        else:
            protocol = input("\n Protocol (http/https) : ").strip()
            
            if protocol == "http" :
                url = f"http://{target_ip}"
                break   
            elif protocol == "https":
                url = f"https://{target_ip}"
                break
            else:
                print ("\n Invalid answer!")
            
    command = ["curl", "-I", url]
    
    colored_tool = f"{CYAN}curl {RESET}"
    colored_opt1 = f"{GREEN}-I {RESET}"
    colored_ip = f"{RESET}{target_ip}"

    full_cmd_display = colored_tool + colored_opt1 + colored_ip

    run_tool(command, full_cmd_display)
    
    
    
def exiftool_metadata_extract():
    
    file_location = input("\n Paste here the file full location (exp : /home/user01/img.jpg) : ")
        
    command = ["exiftool", file_location]
    
    colored_tool = f"{CYAN}exiftool {RESET}{file_location}"

    run_tool(command, colored_tool)
    
    

def format_command(command):
    tool, *args = command
    parts = [f"{CYAN}{tool}{RESET}"]
    for arg in args:
        parts.append(f"{GREEN}{arg}{RESET}" if arg.startswith("-") else arg)
    return " ".join(parts)


def run_tool(command, full_cmd_display=None):
    # Build the display automatically if the caller didn't give a string
    if not isinstance(full_cmd_display, str):
        full_cmd_display = format_command(command)

    line = " ".join(command)
    print("\n" + "=" * (len(line) + 18))
    print(f"     Running: {full_cmd_display}")
    print("=" * (len(line) + 18))

    try:
        proc = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
    except FileNotFoundError:
        print(f"\n [{BRIGHT_RED}-{RESET}] {command[0]} {BRIGHT_RED}is not installed.{RESET}")
        print(f"\n Please install [ {command[0]} ] to proceed in this function")
        return

    try:
        for out in proc.stdout:
            print(out, end="")
        proc.wait()
        
    except KeyboardInterrupt:
        proc.terminate()
        proc.wait()
        print(f"\n [{YELLOW}!{RESET}] {YELLOW}Operation aborted by user (Ctrl+C). Returning to menu...{RESET}")
        
    


def main():
    
    show_banner()
    
    print("=" * 64)
    print (f"                {BRIGHT_GREEN}Welcome to Recon automator tool.{RESET}")
    print (" Only use on systems you own or have written permission to test")
    print("=" * 64)
    
    target_ip = input("Enter target IP/Name/URL : ").strip()
    
    while True :
        print ("\n Current target : ", target_ip)
        print ("\n What do you want to do ? ")
        print ("\n [1] Target & Host Discovery ")
        print ("\n [2] Web Reconnaissance ")
        print ("\n [3] DNS Reconnaissance ")
        print ("\n [4] Enumerating common services ")
        print ("\n [5] People OSINT ")
        print ("\n [6] File & Metadata Reconnaissance ")
        print ("\n [7] Change the target IP/Name/URL")
        print ("\n [8] Quit ")
        choice = input("\n Your choice (1-8) : ")
        
        if choice == "1" :
            nmap_scan(target_ip) #prsk kamla
        elif choice == "2" :
            web_scan(target_ip) #prsk kamla
        elif choice == "3" :
            dns_scan(target_ip) #prsk kamla
        elif choice == "4" :
            #common_services_scan(target_ip)
            print ("\n Not implemented yet")
        elif choice == "5" :
            print ("\n Not implemented yet")
        elif choice == "6" :
            file_scan() #faha kan metadata
        elif choice == "7" :
            target_ip = input("Enter new target IP/Name/URL: ").strip()
        elif choice == "8":
            print ("\n GoodBye! ")
            break
        else :
            print ("\n Invalid choice!")
            


if __name__ == "__main__":
    main()