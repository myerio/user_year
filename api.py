from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_users():
    year = request.args.get("year", type=int)
    result = []

    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Name FROM Users WHERE BirthYear > ?", (year,))
        rows = cursor.fetchall()
        result = [row[0] for row in rows]
        conn.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)