
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated user database
users = {
    "user@example.com": {"password": "password123", "wallet": 1000}
}

# Slot machine symbols
symbols = ["🍒", "🍋", "🔔", "⭐", "💎"]

import random

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    user = users.get(email)
    if user and user["password"] == password:
        return jsonify({"success": True, "wallet": user["wallet"]})
    return jsonify({"success": False, "message": "Invalid credentials"}), 401

@app.route("/api/wallet", methods=["GET"])
def wallet():
    email = request.args.get("email")
    user = users.get(email)
    if user:
        return jsonify({"wallet": user["wallet"]})
    return jsonify({"message": "User not found"}), 404

@app.route("/api/slot", methods=["POST"])
def slot():
    data = request.json
    email = data.get("email")
    bet = data.get("bet_amount", 0)
    user = users.get(email)
    if not user:
        return jsonify({"message": "User not found"}), 404
    if user["wallet"] < bet:
        return jsonify({"message": "Insufficient funds"}), 400

    # Simulate slot spin
    result = [random.choice(symbols) for _ in range(3)]
    win = result[0] == result[1] == result[2]
    payout = bet * 5 if win else 0
    user["wallet"] += payout - bet

    return jsonify({
        "result": result,
        "win": win,
        "payout": payout,
        "wallet": user["wallet"]
    })

if __name__ == "__main__":
    app.run(debug=True)
