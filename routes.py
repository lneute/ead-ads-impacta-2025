from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Produto

bp = Blueprint("routes", __name__)

# Listagem + busca
@bp.route("/", methods=["GET", "POST"])
def index():
    query = request.args.get("q")  # pega o parâmetro da busca
    if query:
        if query.isdigit():  # se for número, busca por id
            produtos = Produto.query.filter_by(id=int(query)).all()
        else:  # senão, busca no nome (case-insensitive)
            produtos = Produto.query.filter(Produto.nome.ilike(f"%{query}%")).all()
    else:
        produtos = Produto.query.all()

    return render_template("list_products.html", produtos=produtos, query=query)


# Adicionar produto
@bp.route("/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        quantidade = request.form["quantidade"]
        preco = request.form["preco"]

        novo = Produto(
            nome=nome,
            descricao=descricao,
            quantidade=int(quantidade),
            preco=float(preco)
        )
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for("routes.index"))
    return render_template("add_product.html")


# Editar produto
@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_product(id):
    produto = Produto.query.get_or_404(id)

    if request.method == "POST":
        produto.nome = request.form["nome"]
        produto.descricao = request.form["descricao"]
        produto.quantidade = int(request.form["quantidade"])
        produto.preco = float(request.form["preco"])
        db.session.commit()
        return redirect(url_for("routes.index"))

    return render_template("edit_product.html", produto=produto)


# Excluir produto
@bp.route("/delete/<int:id>")
def delete_product(id):
    produto = Produto.query.get(id)
    if produto:
        db.session.delete(produto)
        db.session.commit()
    return redirect(url_for("routes.index"))
