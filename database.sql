CREATE DATABASE IF NOT EXISTS users_db;
use users_db;

CREATE TABLE notas(
    id  int(25) auto_increment not null,
    usuario_id  int(25) not null,
    titulo varchar(255) not null,
    descripcion    MEDIUMTEXT,
    password varchar(255),
    fecha date not null,
    CONSTRAINT pk_notas PRIMARY KEY (id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;