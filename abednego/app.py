from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"

DATABASE = "abednego.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Página inicial redireciona para a listagem de projetos
# @app.route("/", methods=["GET"])
# def home():
#     return redirect(url_for("list_projects"))
@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/projects", methods=["GET"])
def list_projects():
    search_query = request.args.get("search", "")
    conn = get_db_connection()
    if search_query:
        projects = conn.execute(
            "SELECT * FROM projects WHERE name LIKE ?", (f"%{search_query}%",)
        ).fetchall()
    else:
        projects = conn.execute("SELECT * FROM projects").fetchall()
    conn.close()
    return render_template("list_projects.html", projects=projects, search_query=search_query)

@app.route("/projects/new", methods=["GET", "POST"])
def create_project():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        project_type = request.form["type"]
        is_active = 1 if "active" in request.form else 0

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO projects (name, description, project_type, is_active, created_by, created_at) "
            "VALUES (?, ?, ?, ?, ?, datetime('now'))",
            (name, description, project_type, is_active, 1),
        )
        conn.commit()
        conn.close()
        flash("Project created successfully!", "success")
        return redirect(url_for("list_projects"))

    return render_template("create_project.html")

@app.route("/projects/edit/<int:id>", methods=["GET", "POST"])
def edit_project(id):
    conn = get_db_connection()
    project = conn.execute("SELECT * FROM projects WHERE id = ?", (id,)).fetchone()

    if not project:
        flash("Project not found.", "danger")
        return redirect(url_for("list_projects"))

    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        project_type = request.form["type"]
        is_active = 1 if "active" in request.form else 0

        conn.execute(
            "UPDATE projects SET name = ?, description = ?, project_type = ?, is_active = ?, updated_at = datetime('now') WHERE id = ?",
            (name, description, project_type, is_active, id),
        )
        conn.commit()
        conn.close()
        flash("Project updated successfully!", "success")
        return redirect(url_for("list_projects"))

    conn.close()
    return render_template("edit_project.html", project=project)

@app.route("/projects/delete/<int:id>", methods=["POST"])
def delete_project(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM projects WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    flash("Project deleted successfully!", "success")
    return redirect(url_for("list_projects"))

@app.route('/dashboard', methods=["GET"])
def dashboard():
    return render_template('dashboard.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)
