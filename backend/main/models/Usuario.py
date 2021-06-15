from .. import db
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    #Mail usado como nombre de usuario
    mail = db.Column(db.String(64), unique=True, index=True, nullable=False)
    telefono = db.Column(db.Integer, nullable=True)
    #Contraseña que será el hash de la pass en texto plano
    password = db.Column(db.String(128), nullable=False)
    #Rol (En el caso que existan diferentes tipos de usuarios con diferentes permisos)
    role = db.Column(db.String(10), nullable=False, default="cliente")
    #Relación
    compras = db.relationship("Compra", back_populates="usuario",cascade="all, delete-orphan")
    productos = db.relationship("Producto", back_populates="usuario",cascade="all, delete-orphan")

    #Getter de la contraseña plana no permite leerla
    @property
    def plain_password(self):
        raise AttributeError('Password cant be read')
    #Setter de la contraseña toma un valor en texto plano
    # calcula el hash y lo guarda en el atributo password
    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)
    #Método que compara una contraseña en texto plano con el hash guardado en la db
    def validate_pass(self,password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'{self.mail}'

    #Convertir objeto en JSON
    def to_json(self):
        usuario_json = {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono,
            'mail': self.mail,
            'role': self.role,

        }
        return usuario_json
    @staticmethod
    #Convertir JSON a objeto
    def from_json(usuario_json):
        id = usuario_json.get('id')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        telefono = usuario_json.get('telefono')
        mail = usuario_json.get('mail')
        password = usuario_json.get('password')
        role = usuario_json.get('role')
        return Usuario(id=id,
                    nombre=nombre,
                    apellido=apellido,
                    telefono=telefono,
                    mail=mail,
                    plain_password=password,
                    role=role,
                    )
