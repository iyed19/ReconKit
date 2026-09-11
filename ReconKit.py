import os
import subprocess
import ipaddress
import shutil



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




def check_tool(tool):
    if shutil.which(tool):
        #print(f"\n [{BRIGHT_GREEN}+{RESET}] {tool} {BRIGHT_GREEN}is installed. {RESET}")
        return True
    else:
        print(f"\n [{BRIGHT_RED}-{RESET}] {tool} {RED}is not installed. {RESET}")
        return False



def run_scan(options, target_ip):
    
    colored_nmap = f"{BLUE}nmap{RESET}"
    colored_options = [f"{GREEN}{opt}{RESET}" for opt in options]
    colored_ip = f"{RESET}{target_ip}"

    full_cmd_display = [colored_nmap] + colored_options + [colored_ip]

    print("\n" + "=" * 60)
    print("          Running:", " ".join(full_cmd_display))
    print("=" * 60)
    
    output_args = save_result()

    command = ["nmap"] + options + output_args + [target_ip]

    subprocess.run(command)
    
    
    
def run_network_scan(target_ip, subnet):
        
    output_args = save_result()

    network = ipaddress.ip_network(f"{target_ip}/{subnet}", strict=False)
    command = ["nmap", "-sn", str(network)]
    
    print ("\n" + "=" * 54)
    print ("          Running:", " ".join(command))
    print ("=" * 54)

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print ("Error:")
        print (result.stderr)
    
    print (result.stdout)
    
    

def save_result():
    
    folder = "results"
    os.makedirs(folder, exist_ok=True)

    while True:
        save_q = input("\n Save results? (y/n): ").strip()
        
        if save_q.lower() == "y" :
            
            file_name = input("File name: ").strip()
            if file_name == "":
                print("Invalid file name")
                continue
            
            while True:
                print ("\n Format : ")
                print ("\n 1. Normal (.nmap) ")
                print ("\n 2. XML (.xml) ")
                print ("\n 3. Grepable (.gnmap) ")
                print ("\n 4. All (-oA) ")
                
                format_choice = input("\n Your choice (1-4) : ")
                
                if format_choice == "1" :
                    return ["-oN", os.path.join(folder, file_name + ".nmap")]
                elif format_choice == "2" :
                    return ["-oX", os.path.join(folder, file_name + ".xml")]
                elif format_choice == "3" :
                    return ["-oG", os.path.join(folder, file_name + ".gnmap")]
                elif format_choice == "4" :
                    return ["-oA", os.path.join(folder, file_name)]
                else :
                    print ("\n Invalid choice!")
                
        elif save_q.lower() == "n":
            return []
        else:
            print ("\n Invalid answer!")
    
    
def nmap_scan(target_ip):
    
    while True:
        print ("\n What do you want to do ? ")
        print ("\n 1. Scan a network ")
        print ("\n 2. Run default scripts + service version ")
        print ("\n 3. Run default scripts + service version + vulnerability scripts ")
        print ("\n 4. Run a specific script ")
        print ("\n 5. Scan all ports (1 to 65535) ")
        print ("\n 6. Scan a specific port ")
        print ("\n 7. Scan UDP ports ")
        print ("\n 8. OS detection ")
        print ("\n 9. Spoof resource IP ")
        print ("\n 10. Stealth scan (TCP SYN) ")
        print ("\n 0. Back to Main Menu ")
        
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
        print ("\n 1. Web page and directory brute force ")
        print ("\n 2. HTTP/HTTPS Headers ")
        print ("\n 0. Back to Main Menu ")
        
        web_choice = input("\n Your choice (0-2) : ")
        
        if web_choice == "1" :
            if (check_tool("gobuster") == True) :
                web_pages_bruteforce(target_ip)
            else:
                print("\n Please install [ gobuster ] to proceed in this function")
                break
        elif web_choice == "2" :
            http_headers_scan(target_ip)
        elif web_choice == "0" :
            return
        else :
            print ("\n Invalid choice!")
            
            
 
def dns_scan(target_ip):
    
    while True:
        print ("\n What do you want to do ? ")
        print ("\n 1. Subdomain passive discovery - Subfinder ")
        print ("\n 2. Subdomain brute force - Gobuster ")
        print ("\n 0. Back to Main Menu ")
        
        dns_choice = input("\n Your choice (0-2) : ")
        
        if dns_choice == "1" :
            web_pages_bruteforce(target_ip)
        elif dns_choice == "2" :
            if (check_tool("curl") == True) :
                http_headers_scan(target_ip)
            else:
                print("\n Please install [ curl ] to proceed in this function")
                break
        elif dns_choice == "0" :
            return
        else :
            print ("\n Invalid choice!")
            
            
            
def common_services_scan(target_ip):
    
    while True:
        print ("\n What do you want to do ? ")
        print ("\n 1. SMB ")
        print ("\n 2. RDP ")
        print ("\n 3. SQL Databases ")
        print ("\n 4. SMTP/IMAP/POP3 ")
        print ("\n 5. FTP ")
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
            
def all_ports_scan(target_ip):
    
    print ("\n Executing all ports scan ...")
    run_scan(["-p-", "-Pn"], target_ip)
    
    
  
def specific_port_scan(target_ip):
    
    port = input("\n Enter one port").strip()
    
    if not port.isdigit():
        print("Invalid port")
        return

    print ("\n Executing scan on port : ", port)
    run_scan(["-p", port, "-Pn"], target_ip)
    


def udp_scan(target_ip):
    
    print ("\n Executing UDP scan ...")
    run_scan(["-sU", "-Pn"], target_ip)
    
    

def os_scan(target_ip):
    
    print ("\n Executing OS detection scan ...")
    run_scan(["-O", "-Pn"], target_ip)



def default_scripts_and_service_version_scan(target_ip):
    
    print ("\n Executing default nmap scripts and service version scan ...")
    run_scan(["-sV", "-sC", "-Pn"], target_ip)
    


def default_and_vuln_scripts_and_version_scan(target_ip):
    
    print ("\n Executing default and vulnerability scripts and version scan ...")
    run_scan(["-sV", "-sC", "--script", "vuln", "-Pn"], target_ip)
    
    
    
def specific_script(target_ip):
    
    script = input("\n Enter your script name : ").strip()
    
    print ("Executing ", script," scan ...")
    run_scan(["--script", script, "-Pn"], target_ip)
    


def spoof_resource_ip(target_ip):
    
    spoof_ip = input("\n Enter your spoof IP : ").strip()
    
    print ("Executing scan with IP = ", spoof_ip)
    run_scan(["-S", spoof_ip, "-sV", "-sC", "-Pn"], target_ip)
    
    
    
def stealth_scan(target_ip):
    
    print ("\n Executing stealth scan ...")
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
        print ("\n 1. Run quick pages scan ")
        print ("\n 2. Run balanced pages scan ")
        print ("\n 3. Run deep pages scan ")
        print ("\n 4. Run very deep pages scan (takes so much time!) ")
        print ("\n 0. Back to Main Menu ")
        
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

    print("\n" + "="*153)
    print("     Running:", " ".join(command))
    print("="*153)

    result = subprocess.run(command,capture_output=True,text=True)

    print(result.stdout)

    if result.stderr:
        print(result.stderr)
        
        
        
def network_scan(target_ip):
    
    while True:
        print ("\n What do you want to scan ? ")
        print ("\n 1. Scan default /24 network ")
        print ("\n 2. Scan /25 network ")
        print ("\n 3. Scan /26 network ")
        print ("\n 4. Scan /27 network ")
        print ("\n 5. Enter custom subnet ")
        print ("\n 0. Back to Main Menu ")
        
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
    
    print("\n" + "="*53)
    print(f"  Running: {BLUE}curl {GREEN}-I {RESET}{' '.join(command[2:])}")
    print("="*53)

    subprocess.run(command)
    
    
    
def exiftool_metadata_extract():
    
    file_location = input("\n Paste here the file full location (exp : /home/user01/img.jpg) : ")
        
    command = ["exiftool", file_location]

    print("\n" + "="*75)
    print("  Running:", " ".join(command))
    print("="*75)

    result = subprocess.run(command,capture_output=True,text=True)

    print(result.stdout)
    
            
    


def main():
    
    print("=" * 29)
    print (" Welcome to Recon Automator.")
    print("=" * 29)
    
    target_ip = input("Enter target IP/Name/URL : ").strip()
    
    while True :
        print ("\n Current target : ", target_ip)
        print ("\n What do you want to do ? ")
        print ("\n 1. Target & Host Discovery ")
        print ("\n 2. Web Reconnaissance ")
        print ("\n 3. DNS Reconnaissance ")
        print ("\n 4. Enumerating common services ")
        print ("\n 5. People OSINT ")
        print ("\n 6. File & Metadata Reconnaissance ")
        print ("\n 7. Change the target IP/Name/URL")
        print ("\n 8. Quit ")
        choice = input("\n Your choice (1-8) : ")
        
        if choice == "1" :
            nmap_scan(target_ip)
        elif choice == "2" :
            web_scan(target_ip)
        elif choice == "3" :
            dns_scan(target_ip)
        elif choice == "4" :
            common_services_scan(target_ip)
        elif choice == "5" :
            break
        elif choice == "6" :
            file_scan()
        elif choice == "7" :
            target_ip = input("Enter new target IP/Name/URL: ").strip()
        elif choice == "8":
            print ("\n GoodBye! ")
            break
        else :
            print ("\n Invalid choice!")
            


if __name__ == "__main__":
    main()