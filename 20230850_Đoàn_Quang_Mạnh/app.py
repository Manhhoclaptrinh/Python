from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy  #Them thu vien SQLAlchemy de lam viec voi database
from datetime import datetime
import pytz

app = Flask(__name__)
# Khởi tạo Database SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///petuber.db'
db = SQLAlchemy(app)

# Model lưu trữ sự kiện của thú cưng
class PetEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.String(20), nullable=False)
    pet_type = db.Column(db.String(20))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/events', methods=['GET', 'POST'])
def handle_events():
    if request.method == 'POST':
        data = request.json
        new_event = PetEvent(title=data['title'], event_date=data['date'], pet_type=data['pet'])
        db.session.add(new_event)
        db.session.commit()
        return jsonify({"status": "success"})
    
    events = PetEvent.query.all()
    return jsonify([{"id": e.id, "title": e.title, "date": e.event_date, "pet": e.pet_type} for e in events])

@app.route('/api/delete_event/<int:id>', methods=['DELETE'])
def delete_event(id):
    event = PetEvent.query.get(id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({"status": "deleted"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)