from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_connection, Student, db
import uuid

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
db.init_app(app)

def create_or_update_student(data):
    student = Student.query.filter_by(
        first_name=data['first_name'],
        last_name=data['last_name'],
        city=data['city']
    ).first()

    if student:
        # update
        student.address = data['address']
        student.monitored_by = data['monitored_by']
    else:
        # create
        student = Student(
            student_id=str(uuid.uuid4()),
            first_name=data['first_name'],
            last_name=data['last_name'],
            address=data['address'],
            city=data['city'],
            monitored_by=data['monitored_by']
        )
        db.session.add(student)

    db.session.commit()

@app.route('/')
def home():
    return jsonify({"message": "School API is running"})

@app.route('/students', methods=['POST'])
def add_student():
    try:
        data = request.get_json()
        create_or_update_student(data)
        return jsonify({"message": "Student created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)

