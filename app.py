from flask import Flask, jsonify, request
from users import users

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"result": "success", "body": "index page"}), 200


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


@app.route("/user/<id>", methods=["GET", "PUT", "POST", "DELETE"])
def get_user(id):
    if request.method == "GET":
        for user in users:
            if user["id"] == id:
                return jsonify(user), 200
        return (
            jsonify({"result": "fail", "trace": "not found a user with id " + id}),
            404,
        )
    # updates a user
    elif request.method == "PUT":
        for user in users:
            if user["id"] == id:
                user["name"] = request.json["name"]
                user["lastname"] = request.json["lastname"]
                user["job"] = request.json["job"]

                return (
                    jsonify({"result": "success", "message": "user updated id: " + id}),
                    200,
                )
        return (
            jsonify({"result": "fail", "trace": "not found a user with id " + id}),
            404,
        )
    # creates a new user
    elif request.method == "POST":
        for user in users:
            if user["id"] == id:
                return (
                    jsonify(
                        {
                            "result": "faile",
                            "message": "a user exists with this id: " + id,
                        }
                    ),
                    500,
                )
        data = request.json
        data["id"] = id
        users.append(data)
        return (
            jsonify(
                {
                    "result": "success",
                    "message": "user created successfully with id: " + id,
                }
            ),
            200,
        )
    # deletes a user
    elif request.method == "DELETE":
        for user in users:
            if user["id"] == id:
                users.remove(user)
                return (
                    jsonify(
                        {
                            "result": "success",
                            "message": "user deleted with id:  " + id,
                        }
                    ),
                    200,
                )
        return (
            jsonify(
                {
                    "result": "failed",
                    "message": "no user found with id: " + id,
                }
            ),
            404,
        )


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
