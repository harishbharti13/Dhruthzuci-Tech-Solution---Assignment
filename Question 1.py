import json
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/find_symbols_in_names', methods=['PUT'])



def match_symbol():
    data = {
            "chemicals": ['Amazon', 'Microsoft', 'Google'],
            "symbols": ['I', 'Am', 'cro', 'Na', 'le', 'abc']
         }

    import re
    combined = []

    for s in data['symbols']:
        for c in data['chemicals']:
            r = re.search(s, c)
            if r:
                jasonify(combined.append(re.sub(s, "[{}]".format(s), c)))
    d = match_symbol()
    return jasonify(d.combined)
app.run(debug=True)

