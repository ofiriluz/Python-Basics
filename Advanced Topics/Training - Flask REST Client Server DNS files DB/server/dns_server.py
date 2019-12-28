import dns_operations as do
import dns_record as dr
import os
from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

DEFAULT_RECORDS_DB_PATH = "./records.db"
DEFAULT_ALLOWED_USERS = {
    "prod": "prod"
}
app = Flask(__name__)

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

@auth.verify_password
def verify_password(username, password):
    return username in DEFAULT_ALLOWED_USERS and password == DEFAULT_ALLOWED_USERS[username]

@app.route('/dns_records', methods=['GET'])
@auth.login_required
def dns_records():
    global records_db
    return jsonify({
        "records": [record.as_dict() for record in records_db]
    })

@app.route('/dns_record/<ip>', methods=['GET'])
@auth.login_required
def dns_record(ip):
    global records_db
    return jsonify({
        "records": map(lambda record: record.as_dict(),
                        filter(lambda record: record.get_ip() == ip, records_db))
    })

@app.route('/add_dns_record', methods=['POST'])
@auth.login_required
def add_dns_record():
    global records_db
    if not request.json or 'ip' not in request.json or 'hosts' not in request.json:
        abort(400)
    records_db.append(dr.DNSRecord(request.json['ip'], request.json['hosts']))
    save_hosts_db(records_db, DEFAULT_RECORDS_DB_PATH)
    return jsonify({"result": "success"})

@app.route('/add_dns_record_hosts', methods=['POST'])
@auth.login_required
def add_dns_record_hosts():
    global records_db
    if not request.json or 'ip' not in request.json or 'hosts' not in request.json:
        abort(400)
    result_message = 'ip not found'
    for record in records_db:
        if record.get_ip() == request.json['ip']:
            record.add_hosts(request.json['hosts'])
            result_message = 'success'
    save_hosts_db(records_db, DEFAULT_RECORDS_DB_PATH)
    return jsonify({"result": result_message})

@app.route('/remove_dns_record/<ip>', methods=['DELETE'])
@auth.login_required
def remove_dns_record(ip):
    global records_db
    records_db = filter(lambda record: record.get_ip() != ip, records_db)
    save_hosts_db(records_db, DEFAULT_RECORDS_DB_PATH)
    return jsonify({"result": "success"})

@app.route('/remove_dns_record_host/<host>', methods=['DELETE'])
@auth.login_required
def remove_dns_record_host(host):
    global records_db
    for record in records_db:
        record.remove_host(host)
    save_hosts_db(records_db, DEFAULT_RECORDS_DB_PATH)
    return jsonify({"result": "success"})

@app.route('/clear_dns_records', methods=['DELETE'])
@auth.login_required
def clear_dns_records():
    global records_db
    records_db = []
    save_hosts_db(records_db, DEFAULT_RECORDS_DB_PATH)
    return jsonify({"result": "success"})

if __name__ == "__main__":
    global records_db
    records_db = load_hosts_db(DEFAULT_RECORDS_DB_PATH)
    app.run(debug=True)