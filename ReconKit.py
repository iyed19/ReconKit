import os
import subprocess


    
def run_scan(options, target_ip):
    
    print ("\n" + "=" * 60)
    print ("          Running:", " ".join(["nmap"] + options + [target_ip]))
    print ("=" * 60)
    
    output_args = save_result()

    command = ["nmap"] + options + output_args + [target_ip]

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
    
    
    
def default_scan(target_ip):
    
    print ("\n Executing default scan ...")
    run_scan([], target_ip)
    


def all_ports_scan(target_ip):
    
    print ("\n Executing all ports scan ...")
    run_scan(["-p-"], target_ip)
    
    
  
def specific_port_scan(target_ip):
    
    port = input("\n Enter one port").strip()
    
    if not port.isdigit():
        print("Invalid port")
        return

    print ("\n Executing scan on port : ", port," ...")
    run_scan(["-p", port], target_ip)
    


def udp_scan(target_ip):
    
    print ("\n Executing UDP scan ...")
    run_scan(["-sU"], target_ip)
    
    

def os_scan(target_ip):
    
    print ("\n Executing OS detection scan ...")
    run_scan(["-O"], target_ip)
    
    
    
def service_version_scan(target_ip):
    
    print ("\n Executing service version scan ...")
    run_scan(["-sV"], target_ip)
    
    

def default_scripts_scan(target_ip):
    
    print ("\n Executing default scripts scan ...")
    run_scan(["-sC"], target_ip)



def default_scripts_and_service_version_scan(target_ip):
    
    print ("\n Executing default scripts and service version scan ...")
    run_scan(["-sV", "-sC"], target_ip)
    
    
    
def vuln_scan(target_ip):
    
    print ("\n Executing vulnerability scripts scan ...")
    run_scan(["--script", "vuln"], target_ip)
    
    

def default_and_vuln_scripts_scan(target_ip):
    
    print ("\n Executing default and vulnerability scripts scan ...")
    run_scan(["-sC", "--script", "vuln"], target_ip)
    


def default_and_vuln_scripts_and_version_scan(target_ip):
    
    print ("\n Executing default and vulnerability scripts and version scan ...")
    run_scan(["-sV", "-sC", "--script", "vuln"], target_ip)
    
    
    
def specific_script(target_ip):
    
    script = input("\n Enter your script name").strip()
    
    print ("Executing ", script," scan ...")
    run_scan(["--script", script], target_ip)
    


def spoof_resource_ip(target_ip):
    
    spoof_ip = input("\n Enter your spoof IP ").strip()
    
    print ("Executing scan with IP = ", spoof_ip, " ...")
    run_scan(["-S", spoof_ip], target_ip)
    
    
    
def stealth_scan(target_ip):
    
    print ("\n Executing stealth scan ...")
    run_scan(["-sS"], target_ip)
    
    


def main():
    
    print("=" * 28)
    print (" Welcome to Nmap Automator.")
    print("=" * 28)
    
    target_ip = input("Enter target IP : ").strip()
    
    while True :
        print ("\n Current target : ", target_ip)
        print ("\n What do you want to do ? ")
        print ("\n 1. Default scan (Top 1000 ports) ")
        print ("\n 2. Scan all ports (1 to 65535) ")
        print ("\n 3. Scan a specific port ")
        print ("\n 4. Scan UDP ports ")
        print ("\n 5. OS detection ")
        print ("\n 6. Scan service version ")
        print ("\n 7. Run default scripts ")
        print ("\n 8. Run default scripts + service version ")
        print ("\n 9. Run vulnerability scripts ")
        print ("\n 10. Run default + vulnerability scripts ")
        print ("\n 11. Run default + vulnerability scripts + service version")
        print ("\n 12. Run a specific script ")
        print ("\n 13. Spoof resource IP ")
        print ("\n 14. Stealth scan (TCP SYN) ")
        print ("\n 15. Change the target IP")
        print ("\n 16. Quit ")
        choice = input("\n Your choice (1-16) : ")
        
        if choice == "1" :
            default_scan(target_ip)
        elif choice == "2" :
            all_ports_scan(target_ip)
        elif choice == "3" :
            specific_port_scan(target_ip)
        elif choice == "4" :
            udp_scan(target_ip)
        elif choice == "5" :
            os_scan(target_ip)
        elif choice == "6" :
            service_version_scan(target_ip)
        elif choice == "7" :
            default_scripts_scan(target_ip)
        elif choice == "8" :
            default_scripts_and_service_version_scan(target_ip)
        elif choice == "9" :
            vuln_scan(target_ip)
        elif choice == "10" :
            default_and_vuln_scripts_scan(target_ip)
        elif choice == "11" :
            default_and_vuln_scripts_and_version_scan(target_ip)
        elif choice == "12" :
            specific_script(target_ip)
        elif choice == "13" :
            spoof_resource_ip(target_ip)
        elif choice == "14" :
            stealth_scan(target_ip)
        elif choice == "15" :
            target_ip = input("Enter new target IP: ").strip()
        elif choice == "16":
            print ("\n GoodBye! ")
            break
        else :
            print ("\n Invalid choice!")
            


if __name__ == "__main__":
    main()