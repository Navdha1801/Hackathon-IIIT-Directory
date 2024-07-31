from flask import Flask, render_template, request
import sqlite3


class DBclass:
    def __init__(self, path):
        self.path = path
        self.db = sqlite3.connect(path)
        self.cursor = self.db.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def commit(self):
        self.db.commit()


db = DBclass('data.db')


list = db.execute("SELECT * FROM students")
list_faculties = db.execute("SELECT * FROM faculty")
# = db.cursor.fetchall()
# print(list)


def search_by_rollno(rollno):
    list_to_return = []
    for item in list:
        rollno_list = str(list[0])
        rollno_list = rollno_list.lower()
        if rollno_list.count(rollno.lower()) > 0:
            list_to_return.append(item)
    return list_to_return


def search_name(name):
    list_to_return = []
    for item in list:
        name_list = str(list[1])
        name_list = name_list.lower()
        if name_list.count(name.lower()) > 0:
            list_to_return.append(item)
    return list_to_return


def search_email(email):
    list_to_return = []
    for item in list:
        email_list = str(list[2])
        email_list = email_list.lower()
        if email_list.count(email.lower()) > 0:
            list_to_return.append(item)
    return list_to_return


def search_branch(branch):
    list_to_return = []
    for item in list:
        branch_list = str(list[3])
        branch_list = branch_list.lower()
        if branch_list.count(branch.lower()) > 0:
            list_to_return.append(item)
    return list_to_return


def search_section(section):
    list_to_return = []
    for item in list:
        section_list = str(list[4])
        section_list = section_list.lower()
        if section_list.count(section.lower()) > 0:
            list_to_return.append(item)
    return list_to_return


def search_all(rollno, name, email, branch, section):
    list_to_return = []
    for item in list:
        rollno_list = str(list[0])
        rollno_list = rollno_list.lower()
        name_list = str(list[1])
        name_list = name_list.lower()
        email_list = str(list[2])
        email_list = email_list.lower()
        branch_list = str(list[3])
        branch_list = branch_list.lower()
        section_list = str(list[4])
        section_list = section_list.lower()
        if rollno_list.count(rollno.lower()) > 0 and name_list.count(name.lower()) > 0 and email_list.count(email.lower()) > 0 and branch_list.count(branch.lower()) > 0 and section_list.count(section.lower()) > 0:
            list_to_return.append(item)
    return list_to_return


def add_student_to_database(rollno, name, email, branch, section):
    insert_query = f"""INSERT INTO students VALUES ({rollno}, "{name}", "{email}", "{branch}", "{section}")"""
    db.execute(insert_query)
    db.commit()

# check insertion
# add_student_to_database(2000114001,"Priet","priet.test@iiit","CSE","A")


def delete_student_from_database(rollno):
    delete_query = f"""DELETE FROM students WHERE rollno = {rollno}"""
    db.execute(delete_query)
    db.commit()

# check deletion
# delete_student_from_database(2000114001)


def update_student_in_database(rollno, name, email, branch, section):
    update_query = f"""UPDATE students SET name = "{name}", email = "{email}", branch = "{branch}", section = "{section}" WHERE rollno = {rollno}"""
    db.execute(update_query)
    db.commit()

# check update
# update_student_in_database(2000114001,"PrietUkani","priet.test@iiit","CSE","A")


def get_student_from_database(rollno):
    select_query = f"""SELECT * FROM students WHERE rollno = {rollno}"""
    return db.execute(select_query)

# check get
# print(get_student_from_database(2000114001))


def get_all_students_from_database():
    select_query = f"""SELECT * FROM students"""
    return db.execute(select_query)

# check get all
# print(get_all_students_from_database())


def get_all_students_from_database_by_branch(branch):
    select_query = f"""SELECT * FROM students WHERE branch = "{branch}" """
    return db.execute(select_query)

# check get all by branch
# print(get_all_students_from_database_by_branch("CSE"))


def get_all_students_from_database_by_section(section):
    select_query = f"""SELECT * FROM students WHERE section = "{section}" """
    return db.execute(select_query)

# check get all by section
# print(get_all_students_from_database_by_section("A"))


def select_student_with_attributes(rollno=None, name=None, email=None, branch=None, section=None):
    select_query = f"""SELECT * FROM students WHERE """
    if rollno is not None:
        select_query += f"""rollno like {rollno} AND """
    if name is not None:
        select_query += f"""name like "%{name}%" AND """
    if email is not None:
        select_query += f"""email like "%{email}%" AND """
    if branch is not None:
        select_query += f"""branch like "%{branch}%" AND """
    if section is not None:
        select_query += f"""section like "%{section}%" AND """
    select_query = select_query[:-5]
    return db.execute(select_query)

# check select
# print(select_student_with_attributes(rollno=2022111039, section="A" ))


def get_faculty_from_database(faculty_id):
    select_query = f"""SELECT * FROM faculty WHERE id = {faculty_id}"""
    return db.execute(select_query)


# check get
# print(get_faculty_from_database(1))


def find_faculty_by_name(name):
    select_query = f"""SELECT * FROM faculty WHERE name like "%{name}%" """
    return db.execute(select_query)


# check find
# print(find_faculty_by_name("aftab")[0][0])


def get_all_faculty_from_database():
    select_query = f"""SELECT * FROM faculty"""
    return db.execute(select_query)


def insert_faculty_in_database(name, designation, study, research_areas, research_center, id):
    insert_query = f"""INSERT INTO faculty VALUES ("{name}", "{designation}", "{study}", "{research_areas}", "{research_center}",{id})"""
    db.execute(insert_query)
    db.commit()


# check insertion
# insert_faculty_in_database("Aftab","Assistant Professor","PhD","Machine Learning, Deep Learning, Computer Vision","IIIT Vadodara",10000)

def delete_faculty_from_database(faculty_id):
    delete_query = f"""DELETE FROM faculty WHERE id = {faculty_id}"""
    db.execute(delete_query)
    db.commit()

# check deletion
# delete_faculty_from_database(10000)


def update_faculty_in_database(name=None, designation=None, study=None, research_areas=None, research_center=None, id='0'):
    update_query = f"""UPDATE faculty SET """
    if name:
        update_query += f"""name = "{name}", """
    if designation:
        update_query += f"""designation = "{designation}", """
    if study:
        update_query += f"""study = "{study}", """
    if research_areas:
        update_query += f"""research_areas = "{research_areas}", """
    if research_center:
        update_query += f"""research_center = "{research_center}", """
    update_query = update_query[:-2]
    update_query += f""" WHERE id = {id}"""
    db.execute(update_query)
    db.commit()

# check update
# update_faculty_in_database(name="Aftabhusaain", designation="Assistant Professor", study="PhD", research_areas="Machine Learning, Deep Learning, Computer Vision", research_center="IIIT Vadodara", id=10000)


def select_faculty_with_attributes(name=None, designation=None, study=None, research_areas=None, research_center=None, id=None):
    select_query = f"""SELECT * FROM faculty WHERE """
    if name:
        select_query += f"""name like "%{name}%" AND """
    if designation:
        select_query += f"""designation like "%{designation}%" AND """
    if study:
        select_query += f"""study like "%{study}%" AND """
    if research_areas:
        select_query += f"""research_areas like "%{research_areas}%" AND """
    if research_center:
        select_query += f"""research_center like "%{research_center}%" AND """
    if id:
        select_query += f"""id like {id} AND """
    select_query = select_query[:-4]
    print(select_query)
    return db.execute(select_query)

# check select
# print(select_faculty_with_attributes(name="Aftabukani", designation="Assistant Professor", study="PhD", research_areas="Machine Learning, Deep Learning, Computer Vision", research_center="IIIT Vadodara", id=10000))


app = Flask(__name__)
app.config['DEBUG'] = True

# Home page


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/about.html', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/student_search.html', methods=['GET', 'POST'])
def student_search():
    if request.method == 'POST':
        # search_by = request.form['search-by']
        # rollno_filter = request.form['rollno-filter']
        # search_value = request.form['search-value']
        rollno_filter = request.form['rollno-filter']
        name_filter = request.form['name-filter']
        email_filter = request.form['email-filter']
        branch_filter = request.form['branch-filter']
        section_filter = request.form['section-filter']

        # Connect to SQLite database
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        # Query the database for all students with matching search value
        c.execute(
            f"SELECT * FROM students WHERE name like '%{name_filter}%' and rollno like '%{rollno_filter}%' and email like '%{email_filter}%' and branch like '%{branch_filter}%' and section like '%{section_filter}%'")
        results = c.fetchall()
        conn.close()
        # Render template with query results
        return render_template('result.html', students=results, rollno_filter=rollno_filter, name_filter=name_filter, email_filter=email_filter, branch_filter=branch_filter, section_filter=section_filter)
    else:
        return render_template('student_search.html')


@app.route('/faculty_search.html', methods=['GET', 'POST'])
def faculty_search():
    if request.method == "POST":
        id_filter = request.form['id-filter']
        name_filter = request.form['name-filter']
        designation_filter = request.form['designation-filter']
        study_filter = request.form['study-filter']
        research_areas_filter = request.form['research-areas-filter']
        research_lab_filter = request.form['research-lab-filter']

        conn= sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute(f"SELECT * FROM faculty WHERE name like '%{name_filter}%' and id like '%{id_filter}%' and designation like '%{designation_filter}%' and study like '%{study_filter}%' and research_areas like '%{research_areas_filter}%' and research_center like '%{research_lab_filter}%'")
        results = c.fetchall()
        for i in results:
            print(i[5])
        conn.close()
        return render_template('result_faculty.html',students=results, id_filter=id_filter, name_filter=name_filter, designation_filter=designation_filter, study_filter=study_filter, research_areas_filter=research_areas_filter, research_lab_filter=research_lab_filter)
    else:
        return render_template('faculty_search.html')



@app.route('/update_student.html', methods=['GET', 'POST'])
def update_student():
    if request.method == 'POST':

        rollno_filter = request.form['rollno-filter']
        name_filter = request.form['name-filter']
        email_filter = request.form['email-filter']
        branch_filter = request.form['branch-filter']
        section_filter = request.form['section-filter']

        # Connect to SQLite database
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        # Query the database for all students with matching search value
        c.execute("select * from students where rollno = ?", (rollno_filter,))
        results = c.fetchall()
        if len(results)==0:
            return render_template('error.html', error="No such student exists")
        if name_filter:
            c.execute("update students set name = ? where rollno = ?", (name_filter, rollno_filter))
        if email_filter != "":

            c.execute("update students set email = ? where rollno = ?", (email_filter, rollno_filter))
        if branch_filter != "":

            c.execute("update students set branch = ? where rollno = ?", (branch_filter, rollno_filter))
        if section_filter != "":

            c.execute("update students set section = ? where rollno = ?", (section_filter, rollno_filter))
        conn.commit()
        c.execute("select * from students where rollno = ?", (rollno_filter,))
        results = c.fetchall()
        conn.close()
        # Render template with query results
        return render_template('result.html', students=results, rollno_filter=rollno_filter, name_filter=name_filter, email_filter=email_filter, branch_filter=branch_filter, section_filter=section_filter)
    else:
        return render_template('update_student.html')


@app.route('/update_faculty.html', methods=['GET', 'POST'])
def update_faculty():
    if request.method == "POST":
        id_filter = request.form['id-filter']
        name_filter = request.form['name-filter']
        designation_filter = request.form['designation-filter']
        study_filter = request.form['study-filter']
        research_areas_filter = request.form['research-areas-filter']
        research_lab_filter = request.form['research-lab-filter']

        conn= sqlite3.connect('data.db')
        c = conn.cursor()
        # check if someone with id exists
        c.execute("select * from faculty where id = ?", (id_filter,))
        results = c.fetchall()
        if len(results)==0:
            return render_template('error.html', error="No such faculty exists")
        if name_filter!="":
            c.execute("update faculty set name = ? where id = ?", (name_filter, id_filter))
        if designation_filter!="":
            c.execute("update faculty set designation = ? where id = ?", (designation_filter, id_filter))
        if study_filter!="":
            c.execute("update faculty set study = ? where id = ?", (study_filter, id_filter))
        if research_areas_filter!="":
            c.execute("update faculty set research_areas = ? where id = ?", (research_areas_filter, id_filter))
        if research_lab_filter!="":
            c.execute("update faculty set research_center = ? where id = ?", (research_lab_filter, id_filter))
        conn.commit()
        c.execute("select * from faculty where id = ?", (id_filter,))
        results = c.fetchall()
        conn.close()
        # for i in results:
        #     print(i[5])
        # conn.close()
        return render_template('result_faculty.html',students=results, id_filter=id_filter, name_filter=name_filter, designation_filter=designation_filter, study_filter=study_filter, research_areas_filter=research_areas_filter, research_lab_filter=research_lab_filter)
    else:
        return render_template('update_faculty.html')

@app.route('/delete_student.html', methods=['GET', 'POST'])
def delete_student():
    if request.method == 'POST':
        rollno_filter = request.form['rollno-filter']

        # Connect to SQLite database
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("select * from students where rollno = ?", (rollno_filter,))
        # Query the database for all students with matching search value
        # Render template with query results
        result=c.fetchall()
        if len(result)>0:
            c.execute("select * from students where rollno = ?", (rollno_filter,))
            results = c.fetchall()
            conn.commit()
            c.execute("DELETE FROM students WHERE rollno = ?", (rollno_filter,))
            conn.commit()
            return render_template('delete_result.html', students=results)
        else:
            conn.close()
            return render_template('error.html', error="No student with given roll number exists")
        conn.close()
    else:
        return render_template('delete_student.html')


@app.route('/delete_faculty.html', methods=['GET', 'POST'])
def delete_faculty():
    if request.method == 'POST':
        id_filter = request.form['id-filter']

        # Connect to SQLite database
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("select * from faculty where id = ?", (id,))
        # Query the database for all students with matching search value
        # Render template with query results
        result=c.fetchall()
        if len(result)>0:
            c.execute("select * from faculty where id = ?", (id_filter,))
            results = c.fetchall()
            conn.commit()
            c.execute("DELETE FROM faculty WHERE rollno = ?", (id_filter,))
            conn.commit()
            return render_template('delete_result_faculty.html', students=results)
        else:
            conn.close()
            return render_template('error.html', error="No Faculty with given ID exists")
        conn.close()
    else:
        return render_template('delete_faculty.html')

@app.route('/insert_student.html', methods=['GET', 'POST'])
def insert_student():
    if request.method == 'POST':

        rollno_filter = request.form['rollno-filter']
        name_filter = request.form['name-filter']
        email_filter = request.form['email-filter']
        branch_filter = request.form['branch-filter']
        section_filter = request.form['section-filter']

        # Connect to SQLite database
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        # Query the database for all students with matching search value
        c.execute("select * from students where rollno = ?", (rollno_filter,))
        results = c.fetchall()
        if len(results)>0:
            conn.close()
            return render_template('error.html', error="Student with given roll number already exists")
        else:
            c.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", (rollno_filter, name_filter, email_filter, branch_filter, section_filter))
            conn.commit()
            c.execute("select * from students where rollno = ?", (rollno_filter,))
            results = c.fetchall()
            conn.close()
            return render_template('result.html', students=results)
        # Render template with query results
    else:
        return render_template('insert_student.html')



@app.route('/insert_faculty.html', methods=['GET', 'POST'])
def insert_faculty():
    if request.method == "POST":
        id_filter = request.form['id-filter']
        name_filter = request.form['name-filter']
        designation_filter = request.form['designation-filter']
        study_filter = request.form['study-filter']
        research_areas_filter = request.form['research-areas-filter']
        research_lab_filter = request.form['research-lab-filter']

        conn= sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("select * from faculty where id = ?", (id_filter,))
        results = c.fetchall()
        if len(results)>0:
            conn.close()
            return render_template('error.html', error="Faculty with given ID already exists")
        else:
            c.execute("INSERT INTO faculty VALUES (?, ?, ?, ?, ?, ?)", (name_filter, designation_filter, study_filter, research_areas_filter, research_lab_filter, id_filter))
            conn.commit()
            c.execute("select * from faculty where id = ?", (id_filter,))
            results = c.fetchall()
            conn.close()
            return render_template('result_faculty.html', students=results)
    else:
        return render_template('insert_faculty.html')


if __name__ == '__main__':
    app.run(debug=True)
