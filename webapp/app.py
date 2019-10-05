from flask import Flask, render_template, redirect, url_for, request

import hs_student

students = []

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def students_page():
    if request.method == "POST":
        new_student_id = request.form.get("student-id", "")
        new_student_name = request.form.get("name", "")
        new_student_last_name = request.form.get("last-name", "")

        new_student = hs_student.HighSchoolStudent(name=new_student_name, student_id=new_student_id,
                                                   last_name=new_student_last_name)
        students.append(new_student)

        return redirect(url_for("students_page"))

    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
