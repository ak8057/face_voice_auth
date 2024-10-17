from flask import Flask, request, jsonify
from voice_recorder import record_voice
from create_profile import create_user_profile
from authenticate_user import authenticate_user


app = Flask(__name__)

# API endpoint for recording voice
@app.route('/api/record_voice', methods=['POST'])
def api_record_voice():
    data = request.get_json()
    username = data.get('username')
    duration = data.get('duration', 5)  # Default to 5 seconds if not provided
    file_name = f"./voice_files/{username}_voice.wav"
    
    if not username:
        return jsonify({"error": "Username is required"}), 400

    record_voice(file_name, duration)
    return jsonify({"message": f"Voice recorded successfully for {username}", "file": file_name}), 200


# API endpoint for creating user profile
@app.route('/api/create_profile', methods=['POST'])
def api_create_profile():
    data = request.get_json()
    username = data.get('username')
    file_name = data.get('file_name')

    if not username or not file_name:
        return jsonify({"error": "Username and file name are required"}), 400
    
    file_path = f'./voice_files/{file_name}'

    try:
        create_user_profile(username, file_path)
        return jsonify({"message": f"Profile created for {username}"}), 201
    except FileNotFoundError:
        return jsonify({"error": f"File {file_path} not found."}), 404



# API endpoint for authenticating voice
@app.route('/api/authenticate_voice', methods=['POST'])
def api_authenticate_voice():
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    authentication_result = authenticate_user(username)

    if authentication_result:
        return jsonify({"success": True, "message": "Voice Authentication Successful"}), 200
    else:
        return jsonify({"success": False, "message": "Voice Authentication Failed"}), 401


if __name__ == "__main__":
    app.run(debug=True)
