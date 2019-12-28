import dns_operations as do
import dns_record as dr
import os
from flask import Flask, jsonify, request

def touch(fname):
    if os.path.exists(fname):
        os.utime(fname, None)
    else:
        open(fname, 'a').close()

def save_hosts_db(records, path):
    do.DNSOperations.store_dns_file(records, path)

def load_hosts_db(path):
    if not os.path.exists(path):
        touch(path)
    return do.DNSOperations.load_dns_file(path)

app = Flask(__name__)
records_db_path = "./records.db"
records_db = load_hosts_db(records_db_path)

@app.route('/dns_records', methods=['GET'])
def dns_records():
    return jsonify({
        "records": [record.as_dict() for record in records_db]
    })

@app.route('/dns_record/<str:ip>', methods=['GET'])
def dns_record(ip):
    return jsonify({
        "records": map(lambda record: record.as_dict(),
                        filter(lambda record: record.get_ip() == ip, records_db))
    })

@app.route('/add_dns_record', methods=['POST'])
def add_dns_record():
    if not request.json or 'ip' not in request.json or 'hosts' not in request.json:
        abort(400)
    records_db.append(dr.DNSRecord(request.json['ip'], request.json['hosts']))
    save_hosts_db(records_db, records_db_path)
    return jsonify({"result": "success"})

@app.route('/add_dns_record_hosts', methods=['POST'])
def add_dns_record_hosts():
    if not request.json or 'ip' not in request.json or 'hosts' not in request.json:
        abort(400)
    result_message = 'ip not found'
    for record in records_db:
        if record.get_ip() == request.json['ip']:
            record.add_hosts(request.json['hosts'])
            result_message = 'success'
    save_hosts_db(records_db, records_db_path)
    return jsonify({"result": result_message})

@app.route('/remove_dns_record/<str:ip>', methods=['DELETE'])
def remove_dns_record(ip):
    records_db = filter(lambda record: record.get_ip() != ip, records_db)
    save_hosts_db(records_db, records_db_path)
    return jsonify({"result": "success"})

@app.route('/clear_dns_records', methods=['DELETE'])
def clear_dns_records():
    records_db = []
    save_hosts_db(records_db, records_db_path)
    return jsonify({"result": "success"})

if __name__ == "__main__":
    app.run(debug=True)