from database import get_connection

# Criar livro
def adicionar_livro(titulo, autor, ano, genero):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livros (titulo, autor, ano, genero) VALUES (?, ?, ?, ?)",
                   (titulo, autor, ano, genero))
    conn.commit()
    conn.close()

# Listar livros
def listar_livros():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    conn.close()
    return livros

# Buscar por título
def buscar_livro(titulo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros WHERE titulo LIKE ?", (f"%{titulo}%",))
    livros = cursor.fetchall()
    conn.close()
    return livros

# Atualizar livro
def atualizar_livro(id, novo_titulo, novo_autor, novo_ano, novo_genero):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""UPDATE livros 
                      SET titulo=?, autor=?, ano=?, genero=? 
                      WHERE id=?""",
                   (novo_titulo, novo_autor, novo_ano, novo_genero, id))
    conn.commit()
    conn.close()

# Remover livro
def remover_livro(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livros WHERE id=?", (id,))
    conn.commit()
    conn.close()
