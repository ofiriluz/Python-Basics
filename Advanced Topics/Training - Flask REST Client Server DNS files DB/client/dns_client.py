import argparse
import requests
import dns_requests as dr
import pprint

def send_request(request, dns_url, username, password):
    url = "{}/{}".format(dns_url, request.api_path())
    result = None
    headers = {"Content-Type": "application/json"}
    if request.method() == "GET":
        result = requests.get(url, headers=headers, auth=(username, password))
    elif request.method() == "POST":
        result = requests.post(url, json=request.data(), headers=headers, auth=(username, password))
    elif request.method() == "DELETE":
        result = requests.delete(url, headers=headers, auth=(username, password))
    if result == None or result.status_code != 200:
        if result != None:
            raise Exception("Failed request, {}".format(str(result.text)))
        else:
            raise Exception("Failed request")
    return result.json()

def do_add_record_command(args):
    return send_request(dr.AddDNSRecordRequest(args.ip, args.hosts.split()), args.dns_url, args.username, args.password)

def do_add_hosts_command(args):
    return send_request(dr.AddDNSRecordHostsRequest(args.ip, args.hosts.split()), args.dns_url, args.username, args.password)

def do_remove_host_command(args):
    return send_request(dr.RemoveDNSRecordHostRequest(args.host), args.dns_url, args.username, args.password)

def do_remove_record_command(args):
    return send_request(dr.RemoveDNSRecordRequest(args.ip), args.dns_url, args.username, args.password)

def do_list_records_command(args):
    return send_request(dr.ListDNSRecordsRequest(), args.dns_url, args.username, args.password)

def do_list_records_by_ip_command(args):
    return send_request(dr.ListDNSRecordsByIPRequest(args.ip), args.dns_url, args.username, args.password)

def do_clear_records_command(args):
    return send_request(dr.ClearDNSRecordsRequest(), args.dns_url, args.username, args.password)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dns-url", required=True)
    parser.add_argument("--username", required=True)
    parser.add_argument("--password", required=True)
    subparsers = parser.add_subparsers(dest='command')
    add_record_parser = subparsers.add_parser('add_record')
    add_hosts_parser = subparsers.add_parser('add_hosts')
    remove_host_parser = subparsers.add_parser('remove_host')
    remove_record_parser = subparsers.add_parser('remove_record')
    list_records_parser = subparsers.add_parser('list_records')
    list_records_by_ip_parser = subparsers.add_parser('list_records_by_ip')
    clear_records_parser = subparsers.add_parser('clear_records')

    add_record_parser.add_argument("--ip", required=True)
    add_record_parser.add_argument("--hosts", required=True)
    add_hosts_parser.add_argument("--ip", required=True)
    add_hosts_parser.add_argument("--hosts", required=True)
    remove_host_parser.add_argument("--host", required=True)
    remove_record_parser.add_argument('--ip', required=True)
    list_records_by_ip_parser.add_argument('--ip', required=True)

    args = parser.parse_args()

    # Do the command from globals based on the command name
    result = globals()["do_{cmd}_command".format(cmd=args.command)](args)
    print("Result is:")
    pprint.pprint(result)