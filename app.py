from flask import Flask, render_template, request, redirect, url_for
from models import db, Student, Course, Marks, Attendance
from sqlalchemy import text 
app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize DB
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def view_students():
    students = Student.query.all()
    return render_template('students.html', students=students)
#new code
@app.route('/edit_student/<student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    student = Student.query.get_or_404(student_id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.email = request.form['email']
        
        db.session.commit()
        return redirect(url_for('view_students'))
    return render_template('edit_student.html', student=student)

@app.route('/delete_student/<student_id>')
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('view_students'))

@app.route('/edit_course/<course_id>', methods=['GET', 'POST'])
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    if request.method == 'POST':
        course.coursename = request.form['course_name']
        course.credits = request.form['credits']
        course.lecturerid = request.form['lecturer_id']
        db.session.commit()
        return redirect(url_for('view_courses'))
    return render_template('edit_course.html', course=course)

@app.route('/delete_course/<course_id>')
def delete_course(course_id):
    course = course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for('view_courses'))

#end
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        studentid = request.form['student_id']
        name = request.form['name']
        email = request.form['email']
        dob = request.form['dob']

        new_student = Student(studentid=studentid, name=name, email=email, dob=dob)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('view_students'))
    return render_template('add_student.html')

@app.route('/courses')
def view_courses():
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        courseid = request.form['course_id']
        coursename = request.form['course_name']
        credits = request.form['credits']
        lecturerid = request.form['lecturer_id']

        new_course = Course(courseid=courseid, coursename=coursename, credits=credits, lecturerid=lecturerid)
        db.session.add(new_course)
        db.session.commit()
        return redirect(url_for('view_courses'))
    return render_template('add_course.html')

@app.route('/reports')
def reports():
    # Top students based on average score
    top_students = (
        db.session.query(
            Student.studentid,
            Student.name,
            db.func.avg(Marks.score).label('average_score')
        )
        .join(Marks, Student.studentid == Marks.studentid)
        .group_by(Student.studentid, Student.name)
        .order_by(db.desc('average_score'))
        .limit(5)
        .all()
    )

    # Attendance percentage for each student
    attendance_data = (
        db.session.query(
            Student.studentid,
            Student.name,
            db.func.count(Attendance.attendanceid).label('total_classes'),
            db.func.sum(
                db.case(
                    (Attendance.status == 'Present', 1),
                    else_=0
                )
            ).label('present_count')
        )
        .join(Attendance, Student.studentid == Attendance.studentid)
        .group_by(Student.studentid, Student.name)
        .all()
    )

    # Process attendance percentage
    attendance = []
    for studentid, name, total_classes, present_count in attendance_data:
        if total_classes == 0:
            percentage = 0.0
        else:
            percentage = (present_count / total_classes) * 100.0
        attendance.append({
            'studentid': studentid,
            'name': name,
            'total_classes': total_classes,
            'attendance_percentage': round(percentage, 2)
        })

    return render_template('reports.html', top_students=top_students, attendance=attendance)



if __name__ == '__main__':
    app.run(debug=True)
