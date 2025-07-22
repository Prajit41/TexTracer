from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/api/upload', methods=['POST'])
def upload_file():
    # Dummy processing
    return jsonify({
        "status": "success",
        "message": "File processed successfully",
        "highlights": ["Sample highlight 1", "Sample highlight 2"]
    })

@main.route('/api/results', methods=['GET'])
def get_results():
    return jsonify({
        "status": "success",
        "data": ["Result 1", "Result 2"]
    })
