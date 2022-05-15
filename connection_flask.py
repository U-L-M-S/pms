from flask import Flask, request, jsonify
import main

app = Flask(__name__)

@app.route('/gpw', methods = ['POST'])# block GET
def gpw():
    req_data = request.get_json()
    quantily_pws = req_data.get("quantity", "")
    quantily_pws = int(quantily_pws)
    pw_list = main.gpw(quantily_pws)

    return jsonify({"status": "ok"}), 201

@app.route('/hibp', methods = ['POST'])
def hibp():
    req_data = request.get_json()
    pw = req_data.get("pw", "")
    pw = str(pw)
    pw_return = main.hibp(pw)

    return jsonify({"status": "ok"}), 201
