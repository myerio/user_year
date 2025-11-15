from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_users():
    year = request.args.get("year", type=int)
    result = []

    try:
        with open("users.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line or "," not in line:
                    continue
                name, birth_year = line.split(",")
                if int(birth_year) > year:
                    result.append(name)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)