from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home_page():
    return "You've reached the homepage!"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@coolmail.com"
    }

    extra = request.args.get("extra")

    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.post("/create-user")
def create_user():
    data = request.get_json()

    return jsonify({"message_re": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
