from flask import Flask, jsonify


todo = Flask('__name__')

students = [
    {
        'id': 1,
        'student_name': 'std1',
        'age': 20,
        'email': 'higuys23@gmail.com'
    },
    {
        'id': 2,
        'student_name': 'std2',
        'age': 23,
        'email': 'hello3@gmail.com'
    },
    {
        'id': 3,
        'student_name': 'std3',
        'age': 25,
        'email': 'higuys2@gmail.com'
    }
]

@todo.route('/students_list')
def students_list():

    return jsonify(students)




@todo.route('/student/get/<int:id>')
def student_get_by_id(id):
    for std in students:
        if std['id'] == id:

            return jsonify(std)
    return "id not found"








if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5005,
        debug=True
    )
