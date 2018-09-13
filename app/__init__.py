from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from config import Config
from app.models import User, UserSchema

app = Flask(__name__)
app.config.from_object(Config)
db.SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Routes --------------------------------------------------
# Create new user (POST)
@app.route('/user', methods=['POST'])
def add_user():
    username = request.json['username']
    email = request.json['email']

    new_user = User(username, email)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)

# Show all users (GET multiple)
@app.route('/user', methods=['GET'])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)

# Get user detail by id (GET single)
@app.route('/user/<id>', methods=['GET'])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

# Update a single user (PUT)
@app.route('/user/<id>', methods=['PUT'])
def user_update(id):
    user = User.query.get(id)    
    # Get info from PUT
    username = request.json['username']
    email = request.json['email']
    # Save info to DB
    user.email = email
    user.username = username
    db.session.commit()
    
    return user_schema.jsonify(user)

# Delete a single user (DEL)
@app.route('/user/<id>', methods=['DELETE'])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)