from flask import Blueprint, jsonify, request
from app.services.service import service as srv

bp = Blueprint('main', __name__)

@bp.route('/polls', methods=['POST'])
def create_poll():
    try:
        data = request.get_json()
        question = data.get('question')
        options = data.get('options')
        if not question or not options or not isinstance(options, list) or len(options) < 2 :
            return jsonify({"error": "Invalid input"}), 400
        poll_id = srv.create_poll(question, options)
        return jsonify({"message": "Poll created successfully", "poll_id": poll_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@bp.route("/polls/<poll_id>", methods=['GET'])
def get_poll(poll_id):
    try:
        poll, options = srv.get_poll(poll_id)
        if not poll:
            return jsonify({"error": "Poll not found"}), 404
        return jsonify({
            "poll_id": poll.poll_id,
            "question": poll.question,
            "options": [{"option_id": option.option_id, "option_text": option.option_text, "votes": option.votes} for option in options],
            "closes": poll.closes.isoformat(),
            "is_closed": poll.is_closed()
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@bp.route('/polls/<poll_id>/vote', methods=['POST'])
def cast_vote(poll_id):
    try:
        data=request.get_json()
        user_id=data.get('user_id')
        password=data.get('password')
        option=data.get('option')
        if not [user_id,password,option]:
            return jsonify({"error":"missing required feids"}),400
        return jsonify(srv.cast_vote(user_id,password,poll_id,option))
    except Exception as e :
        return jsonify({'error':str(e)}),500
        
@bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        user_id=data.get('user_id')
        password=data.get('password')
        salt = srv.generate_salt()
        password_hash = srv.hash_password(password, salt)
        if not user_id or not password:
            return jsonify({"error": "Missing user_id or password"}), 400
        if srv.user_exists(user_id):
            return jsonify({"error": "User already exists"}), 400
        srv.add_user(user_id, password_hash, salt)
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        