from flask import Flask, request, jsonify

app = Flask(__name__)

def read_users(file_path, year_threshold):
    with open(file_path, "r") as file:
        lines = file.readlines()
        result = []
        for line in lines:
            name, year = line.strip().split(",")
            if int(year) > year_threshold:
                result.append(name)
        return result

@app.route("/users", methods=["GET"])
def get_users():
    year = request.args.get("year", type=int)
    if year is None:
        return jsonify({"error": "Missing 'year' parameter"}), 400

    users = read_users("users.txt", year)
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)