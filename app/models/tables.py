from app import db


class User(db.model):
    __tablename__ == "users"

    id = db.Column(db.Integer, primary_key=True)
    # sem definir tamanho, pega valor máximo. True=nao aceita nome igual
    username = db.Column(db.String, unique=True)
    # campo de texto, sem seguranca por enquanto
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    # construtor sempre recebe self
    def __init__(self, username, password, name, email)
    self.username = username
    self.password = password
    self.name = name
    self.email = email

    # funcao para apresentar o nome do usuario
    def __repr__(self)
    return "<User %r>" % set.username


class Post(db.model):
    __tablename__ = "posts"

    id = db.Colummn(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))

    # relacionamento
    user = db.relationship('User', foreign_key=user_id)

    def __init__(self, content, user_id)
    self.content = content
    self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.id


class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Colummn(db.Integer, primary_key=True)
    id_user = db.Colummn(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Colummn(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_key=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)
