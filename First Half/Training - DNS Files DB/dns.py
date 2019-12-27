import dns_operations as do
import dns_record as dr
import os
import sys
import platform

def clear_screen():
    if 'Windows' in platform.system():
        os.system("cls") # For windows
    else:
        os.system("clear") # For linux

def print_hosts(records):
    for record in records:
        print(str(record))
    raw_input("Press Enter to continue...")

def add_host(records):
    ip = raw_input("Please write the IP:\n")
    hosts = raw_input("Please write the hosts list delimited by spaces\n").split()
    for record in records:
        if record.get_ip() == ip:
            record.add_hosts(hosts)
            return
    records.append(dr.DNSRecord(ip, hosts))

def remove_host(records):
    host = raw_input("Please write the host you wanna remove:\n")
    for record in records:
        record.remove_host(host)

def remove_ip(records):
    ip = raw_input("Please write the ip you wanna remove:\n")
    return filter(lambda record: record.get_ip() != ip, records)

def save_hosts(records, path):
    do.DNSOperations.store_dns_file(records, path)

if __name__ == "__main__":
    records = []
    path = ""
    while True:
        print("Please write a command number")
        print("1. Load hosts file")
        print("2. Create a new hosts file")
        print("3. Exit")
        cmd = raw_input()
        if cmd == '1':
            path = raw_input("Please write the file path:\n")
            records = do.DNSOperations.load_dns_file(path)
            break
        elif cmd == '2':
            path = raw_input("Please write where to output the hosts file:\n")
            break
        elif cmd == '3':
            print("Goodbye")
            sys.exit(0)
        else:
            print("Invalid input, try again")
    clear_screen()
    while True:
        print("Please write a command number")
        print("1. Print hosts")
        print("2. Add host")
        print("3. Remove host")
        print("4. Remove ip")
        print("5. Save")
        print("6. Save and Exit")
        print("7. Exit")
        cmd = raw_input()
        print(type(cmd))
        if type(cmd) != int:
            print("Invalid input, try again")
            clear_screen()
        if cmd == '1':
            print_hosts(records)
        elif cmd == '2':
            add_host(records)
        elif cmd == '3':
            remove_host(records)
        elif cmd == '4':
            records = remove_ip(records)
        elif cmd == '5':
            save_hosts(records, path)
        elif cmd == '6':
            save_hosts(records, path)
            print("Goodbye")
            sys.exit(0)
        elif cmd == '7':
            print("Goodbye")
            sys.exit(0)
        else:
            print("Invalid input, try again")
            clear_screen()
