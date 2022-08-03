import sqlite3, json
from flask import Flask, jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tables.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.drop_all()

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    email = db.Column(db.String(40))
    role_ = db.Column(db.String(300))
    phone = db.Column(db.Integer)
    orders = relationship('Order')

db.create_all()

with open(f"users.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
    for dict in data:
        user = User(
            id=dict['id'],
            first_name=dict['first_name'],
            last_name=dict['last_name'],
            age=dict['age'],
            email=dict['email'],
            role_=dict['role'],
            phone=dict['phone'],
        )
        db.session.add(user)
        db.session.commit()



class Offer(db.Model):
    __tablename__ = 'Offer'
    id = db.Column(db.Integer, unique=True,  primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    orders = db.relationship("Order")
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship('User')

db.create_all()

with open(f"offers.json", 'r', encoding='utf-8') as file_:
    data_ = json.load(file_)
    for dict in data_:
        offer = Offer(
            id=dict['id'],
            order_id=dict['order_id'],
            executor_id=dict['executor_id'],
            )
        db.session.add(offer)
        db.session.commit()



class Order(db.Model):
    __tablename__ = 'Order'
    id = db.Column(db.Integer, unique=True,  primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(30))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    adress = db.Column(db.String(300))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship('User')

db.create_all()

with open(f"orders.json", 'r', encoding='utf-8') as file__:
    data = json.load(file__)
    for dict in data:
        order = Order(
            id=dict['id'],
            name=dict['name'],
            description=dict['description'],
            start_date=dict['start_date'],
            end_date=dict['end_date'],
            address=dict['address'],
            price=dict['price'],
            customer_id=dict['customer_id'],
            executor_id=dict['executor_id'],
            )
        db.session.add(offer)
        db.session.commit()

db.create_all()

@app.route("/users")
def get_all_users():
    users = User.query.all()
    return jsonify(users)

@app.route("/users/<int:id>")
def get_one_user_by_id():
    user = User.query.get(id)
    return jsonify(user)

@app.route("/orders")
def get_all_orders():
    orders = Order.query.all()
    return jsonify(orders)

@app.route("/orders/<int:id>")
def get_one_order_by_id():
    order = Order.query.get(id)
    return jsonify(order)

@app.route("/offers")
def get_all_offers():
    offers = Offer.query.all()
    return jsonify(offers)

@app.route("/offers/<int:id>")
def get_one_offer_by_id():
    offer = Offer.query.get(id)
    return jsonify(offer)

