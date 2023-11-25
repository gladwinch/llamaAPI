from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/llama', methods=['GET'])
def process_text():
    text = request.args.get('text', '')  # Get text from query parameter
    # Process the text as needed
    response = {
        'original_text': text,
        'processed_text': text.upper()  # Example processing
    }
    return jsonify(response)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return 'pong'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)