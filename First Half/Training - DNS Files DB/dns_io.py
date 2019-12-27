import os
import dns_record as dr

def load_dns_file(file_path):
    if not os.path.exists(file_path):
        raise Exception("Invalid file path")

    dns_file_record_lines = open(file_path, 'r').readlines()
    dns_records = []
    for line in dns_file_record_lines:
        # Split line by spaces, default split is spaces and tabs
        dns_record_info = line.split()
        dns_records.append(dr.DNSRecord(dns_record_info[0], dns_record_info[1:]))
    return dns_records

def store_dns_file(dns_records, file_path):
    # Check if the folder exist and create it otherwise
    file_path = os.path.abspath(file_path)
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    # Doesnt matter if the file exists, we will overwrite it
    dns_file = open(file_path, "w")
    dns_file.write('\n'.join([str(record) for record in dns_records]))
    dns_file.close()