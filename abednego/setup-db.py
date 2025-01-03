import sqlite3

# Nome do arquivo do banco de dados
DATABASE = "abednego.db"

# Script de atualização do banco de dados
update_script = """
-- Atualizar a tabela de projetos para incluir data de atualização
ALTER TABLE projects ADD COLUMN updated_at DATETIME DEFAULT NULL;

-- Criar uma tabela de logs para auditoria
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    project_id INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (project_id) REFERENCES projects (id)
);

-- Adicionar campo "category" na tabela de projetos
ALTER TABLE projects ADD COLUMN category TEXT DEFAULT 'General';
"""

# Conexão com o banco de dados
def update_database():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.executescript(update_script)
        conn.commit()
        conn.close()
        print("Banco de dados atualizado com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar o banco de dados: {e}")

if __name__ == "__main__":
    update_database()
