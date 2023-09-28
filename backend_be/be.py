from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

# Store user points and transactions
user_points = {}
user_transactions = []

# Define API endpoints
@app.route('/add', methods=['POST'])
def add_points():
    data = request.get_json()
    payer = data['payer']
    points = int(data['points'])
    timestamp = datetime.datetime.strptime(data['timestamp'], '%Y-%m-%dT%H:%M:%SZ')

    # Update user points
    if payer not in user_points:
        user_points[payer] = 0
    user_points[payer] += points

    # Store transaction
    user_transactions.append({
        'payer': payer,
        'points': points,
        'timestamp': timestamp
    })

    return '', 200

@app.route('/spend', methods=['POST'])
def spend_points():
    data = request.get_json()
    points_to_spend = int(data['points'])

    # Sort transactions by timestamp (oldest first)
    sorted_transactions = sorted(user_transactions, key=lambda x: x['timestamp'])
    print(sorted_transactions)

    spent_points = []

    for transaction in sorted_transactions:
        print(user_points)
        if points_to_spend <= 0:
            break

        payer = transaction['payer']
        points = transaction['points']

        if user_points.get(payer, 0) >= abs(points) and points > 0:
            points_to_remove = min(points_to_spend, abs(points))
            user_points[payer] -= points_to_remove
            points_spend = -points_to_remove
            spent_points.append({'payer': payer, 'points': points_spend})
            points_to_spend -= points_to_remove
        if user_points.get(payer, 0) >= abs(points) and points < 0:
            user_points[payer] += abs(points)
            points_to_spend += abs(points)

    if points_to_spend > 0:
        return 'Not enough points to spend', 400

    return jsonify(spent_points), 200

@app.route('/balance', methods=['GET'])
def get_balance():
    return jsonify(user_points), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
