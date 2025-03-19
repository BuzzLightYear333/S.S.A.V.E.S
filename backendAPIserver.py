from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/exchange', methods=['POST'])
def exchange():
    data = request.get_json()
    sender = data.get('sender')
    recipient = data.get('recipient')
    amount = data.get('amount')

    # Simulate smart contract interaction
    response = {"message": f"Exchange successful: {amount} sent from {sender} to {recipient}"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)