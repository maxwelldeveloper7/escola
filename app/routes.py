from flask import render_template, redirect
from app import app, conectar_db
from flask import request

@app.route('/escolas')
def listar_escolas():
    with conectar_db() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM escolas")
        escolas = cur.fetchall()
    return render_template('escolas.html', escolas=escolas)

@app.route('/adicionar_aluno', methods=['GET', 'POST'])
def adicionar_aluno():
    if request.method == 'POST':
        nome_completo = request.form['nome_completo']
        data_nascimento = request.form['data_nascimento']
        codigo_censo = request.form['codigo_censo']
        etapa = request.form['etapa']
        id_familia = request.form['id_familia']
        
        with conectar_db() as conn:
            cur = conn.cursor()
            cur.execute('''
                        INSERT INTO escola_alunos (
                            codigo_censo,
                            etapa,
                            nome_completo,
                            data_nascimento,
                            id_familia
                        )
                        VALUES (?, ?, ?, ?, ?)
                        ''', (
                            codigo_censo,
                            etapa,
                            nome_completo,
                            data_nascimento,
                            id_familia
                        ))
            conn.commit()
        return redirect('/escolas')
    with conectar_db() as conn:
        cur = conn.cursor()
        cur.execute("SELECT codigo_censo, nome_escola FROM escolas order by nome_escola")
        escolas = cur.fetchall()
        cur.execute("SELECT id_familia, nome_mae FROM familia order by nome_mae")
        familias = cur.fetchall()
    return render_template('adicionar_aluno.html', escolas=escolas, familias=familias)
        