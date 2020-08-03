from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/test', methods=["POST"])
def testEndPoint():
    string_to_cut = request.json['string_to_cut']
    try:
        every_third_letter = "".join([letter for idx, letter in enumerate(string_to_cut) if (idx + 1) % 3 == 0])
    except Exception as e:
        every_third_letter = f"something went wrong: ({e})"

    return {"return_string": every_third_letter}
    
