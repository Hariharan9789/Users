from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="harianand420",
    database="user_db"
)

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    cursor = db.cursor()
    query = "INSERT INTO users (field1, field2, field3, field4, field5, field6, field7, field8, field9, field10) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (
        data['field1'], data['field2'], data['field3'], data['field4'], data['field5'],
        data['field6'], data['field7'], data['field8'], data['field9'], data['field10']
    )
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    return jsonify({'message': 'User created successfully'})

@app.route('/api/users', methods=['GET'])
def get_users():
    cursor = db.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = []
    for user in cursor.fetchall():
        users.append({
            'id': user[0],
            'field1': user[1],
            'field2': user[2],
            'field3': user[3],
            'field4': user[4],
            'field5': user[5],
            'field6': user[6],
            'field7': user[7],
            'field8': user[8],
            'field9': user[9],
            'field10': user[10]
        })
    cursor.close()
    return jsonify(users)

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    cursor = db.cursor()
    query = "UPDATE users SET field1 = %s, field2 = %s, field3 = %s, field4 = %s, field5 = %s, field6 = %s, field7 = %s, field8 = %s, field9 = %s, field10 = %s WHERE id = %s"
    data = request.get_json()
    cursor = db.cursor()
    query = "UPDATE users SET field1 = %s, field2 = %s, field3 = %s, field4 = %s, field5 = %s, field6 = %s, field7 = %s, field8 = %s, field9 = %s, field10 = %s WHERE id = %s"
    values = (
        data['field1'], data['field2'], data['field3'], data['field4'], data['field5'],
        data['field6'], data['field7'], data['field8'], data['field9'], data['field10'], user_id
    )
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    return jsonify({'message': 'User updated successfully'})


if __name__ == '__main__':
    app.run(port=3000)

