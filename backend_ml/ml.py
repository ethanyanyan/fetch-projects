from flask import Flask, jsonify
from receipt_analysis import data_analysis  
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get-receipt-data', methods=['GET'])
def get_receipt_data():
    data = data_analysis.get_monthly_predictions()
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000,debug=True)
