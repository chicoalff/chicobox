import os
import sqlite3
import subprocess
import logging

# Configuração do log
logging.basicConfig(filename="setup_abednego.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Nome do projeto
project_name = "abednego"

# Estrutura do projeto
folders = [
    "app",
    "app/templates",
    "app/static/css",
    "app/static/js",
    "app/static/img",
    "migrations"
]

files = {
    "app/__init__.py": "from flask import Flask\n\napp = Flask(__name__)\nfrom app import routes\n",
    "app/routes.py": """from app import app\n\n@app.route('/')\ndef index():\n    return 'Welcome to Abednego!'\n""",
    "app/models.py": "",
    "app/forms.py": "",
    "app/templates/base.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Dashboard</a></li>
                <li><a href="{{ url_for('list_projects') }}">Projects</a></li>
                <li><a href="{{ url_for('list_contexts') }}">Contexts</a></li>
            </ul>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>""",
    "app/static/css/styles.css": "body { font-family: Arial, sans-serif; margin: 0; padding: 0; }",
    "requirements.txt": "flask\n",
    "app.py": """from app import app\n\nif __name__ == '__main__':\n    app.run(debug=True)\n"""
}

# Banco de dados e tabelas
db_file = f"{project_name}.db"
db_schema = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    project_type TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_by INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS contexts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_by INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS prompts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    context_id INTEGER NOT NULL,
    created_by INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (context_id) REFERENCES contexts (id),
    FOREIGN KEY (created_by) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS instructions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    instruction TEXT NOT NULL,
    prompt_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (prompt_id) REFERENCES prompts (id)
);
"""

def create_project_structure():
    """Cria a estrutura de pastas e arquivos do projeto."""
    os.makedirs(project_name, exist_ok=True)
    for folder in folders:
        path = os.path.join(project_name, folder)
        os.makedirs(path, exist_ok=True)
    for file_path, content in files.items():
        full_path = os.path.join(project_name, file_path)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
    logging.info("Estrutura de pastas e arquivos criada com sucesso.")
    print("Estrutura de pastas e arquivos criada com sucesso.")

def create_virtualenv():
    """Cria e ativa o ambiente virtual."""
    subprocess.run(["python3", "-m", "venv", os.path.join(project_name, "venv")])
    logging.info("Ambiente virtual criado.")
    print("Ambiente virtual criado.")

def activate_virtualenv():
    """Ativa o ambiente virtual."""
    activate_script = os.path.join(project_name, "venv", "bin", "activate")
    if os.name == "nt":  # Windows
        activate_script = os.path.join(project_name, "venv", "Scripts", "activate.bat")
    subprocess.run(["source", activate_script], shell=True)
    logging.info("Ambiente virtual ativado.")
    print("Ambiente virtual ativado.")

def install_dependencies():
    """Instala dependências no ambiente virtual."""
    subprocess.run(["pip", "install", "-r", os.path.join(project_name, "requirements.txt")])
    logging.info("Dependências instaladas.")
    print("Dependências instaladas.")

def create_database():
    """Cria o banco de dados e as tabelas."""
    conn = sqlite3.connect(os.path.join(project_name, db_file))
    cursor = conn.cursor()
    cursor.executescript(db_schema)
    conn.commit()
    conn.close()
    logging.info("Banco de dados criado e tabelas inicializadas.")
    print("Banco de dados criado e tabelas inicializadas.")

def main():
    """Executa todas as etapas do setup."""
    create_project_structure()
    create_virtualenv()
    activate_virtualenv()
    install_dependencies()
    create_database()
    print("Setup do projeto Abednego concluído com sucesso.")
    logging.info("Setup do projeto Abednego concluído com sucesso.")

if __name__ == "__main__":
    main()
