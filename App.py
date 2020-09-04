from flask import Flask, send_from_directory, request, render_template, redirect, url_for, jsonify, session, Markup
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash as checkph
from werkzeug.security import generate_password_hash as genph
from uuid import uuid4

app = Flask(__name__, template_folder="fronted/public")

#----Config-App----
app.config["SECRET_KEY"] = "fd088ae4-3447-4505-8337-580314fec6b2"

#---------MySQL----
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "mijoro02"
app.config["MYSQL_DB"] = "app-task"

mysql = MySQL(app)

#----functions-MySQL----

def getQuery(query):
	cursor = mysql.connection.cursor()
	cursor.execute(query)
	return cursor.fetchall()

def executeQuery(query):
	cursor = mysql.connection.cursor()
	cursor.execute(query)
	mysql.connection.commit()

#----Ni-idea-de-como-se-llamen-la-app

@app.before_request
def before_request():
	session.permanent = True

#----Routers----

@app.route("/login")
@app.route("/tasks")
@app.route("/register")
@app.route("/home")
def index():

	if "username" in session:
		if request.path == "/login":
			return redirect("/home")
		
		username = session["username"]
		idUser = session["id"]
		script = (f"<script type='text/javascript'>"
				  f"let Globallog = '{ username }';"
				  f"let Globallogid = '{ idUser }'"
				   "</script>")
	else:
		script = ("<script type='text/javascript'>\n"
				  "let Globallog = false;\n"
				  "let Globallogid = false;\n"
				  "</script>")

	return render_template("index.html", script = Markup(script))

@app.route("/link")
def link():
	return "<a href='https://www.mediafire.com/file/7cyate92ydr8nzt/SRVE.Shader_v0.5_%281%29.mcpack/file'><h1>Descargar</h1></a>"

@app.route("/auth")
def authication():
	if "username" in session:
		return jsonify(code = 0, username = session["username"])
	else:
		return jsonify(code = 1)

#----Api-Back-End----

@app.route("/api/create/<uuid:id>", methods = ["POST"])
def createNewTask(id):
	if request.method == "POST":
		title = Markup.escape(request.form["title"])
		desc = Markup.escape(request.form["description"])
		priority = request.form["priority"]

		executeQuery("INSERT INTO tasks (idUserFk, titleTask, descriptionTask, valueTask) VALUES ('{0}', '{1}', '{2}', '{3}')".format(id, title, desc, priority))

		return jsonify(message = "Ta bien")

@app.route("/api/deleteTask/<int:id>", methods = ["DELETE"])
def deleteTask(id):
	if request.method == "DELETE":
		executeQuery(f"DELETE FROM tasks WHERE idTask = {id}")
		return jsonify(message = "ta bien", code = 0)

@app.route("/api/edit/<int:id>", methods = ["PUT"])
def editTask(id):
	if request.method == "PUT":
		title = Markup.escape(request.form["title"])
		desc = Markup.escape(request.form["description"])
		priority = request.form["priority"]
		executeQuery("UPDATE tasks SET titleTask = '{0}', descriptionTask = '{1}', valueTask = '{2}' WHERE idTask = '{3}'".format(title, desc, priority, id))
		return jsonify(message = "ta bien", code = 0)

@app.route("/api/getTasks/<uuid:id>")
def getTasks(id):

	tasks = getQuery("SELECT * FROM tasks WHERE idUserFk = '{0}'".format(id))

	if len(tasks) > 0:
		return jsonify(message = "Ta bien", code = 0,tasks = [{"id": i[0],"title": i[2], "description": i[3], "value": i[4]} for i in tasks])

	return jsonify(message = "No hay", code = 1)

@app.route("/api/register", methods = ["POST"])
def register():
	if request.method == "POST":
		print(request.form)
		try:
			newName = Markup.escape(request.form["username"])
			newEmail = Markup.escape(request.form["email"])
			newPass = genph(request.form["password"])
			newID = uuid4()

			executeQuery("INSERT INTO users (idUser, nameUser, emailUser, passUser) VALUES ('{0}', '{1}', '{2}', '{3}')".format(newID, newName, newEmail, newPass))
		except Exception as e:
			
			print("Error: ",e)
			return jsonify(message = "No ta bien", code = 1)


		return jsonify(message = "Ta bien", code = 0)

@app.route("/api/logout")
def logout():
	session.clear()
	return jsonify(code = 0)

@app.route("/api/login", methods = ["POST"])
def login():
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]

		userList = getQuery("SELECT * FROM users WHERE nameUser = '{0}'".format(Markup.escape(username)))

		if (len(userList) > 0):
			hashPass = userList[0][3]
			
			if (checkph(hashPass, password)):
				session["username"] = username
				session["id"] = userList[0][0]
				return jsonify(message = "Ta bien", code = 0)
			else:
				return jsonify(message = "No ta bien", code = 2)
		else:
			return jsonify(message = "No ta bien", code = 1)

@app.route("/<path:path>")
def paths(path):
	return send_from_directory("fronted/public", path)

@app.errorhandler(404)
def err404(e):
	return redirect(url_for("index"))

if __name__=='__main__':
	app.run(host = "192.168.0.4", debug=True)