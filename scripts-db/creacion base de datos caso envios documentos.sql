
------------------
CREATE TABLE Documentos (
    id_documento int not null AUTO_INCREMENT,
    descripcion varchar(50) NOT NULL,
    PRIMARY KEY (id_documento)
);

--- insert commands

insert into Documentos (descripcion) VALUES ('Sobre');
insert into Documentos (descripcion) VALUES ('Archivador');
insert into Documentos (descripcion) VALUES ('Libro');
insert into Documentos (descripcion) VALUES ('Otros');


CREATE TABLE Clientes (
    id_cliente int not null AUTO_INCREMENT,
    nombre varchar(50) not null,
    apellidos varchar(50) not null,
    nro_carnet varchar(20) not null,
    telefono varchar(20) not null,
    direccion varchar(255) not null,
    tipo varchar(50) not null,
    PRIMARY KEY(id_cliente)
);
--- inser clientes

INSERT INTO clientes values (1, 'Miguel', 'Sanchez', '12411898sc', '77411598', 'Av Landivar', 'Emisor');
INSERT INTO clientes values (2, 'Jose Luis', 'Lufin', '12227898sc', '77422598', 'Av Roca y Coronado', 'Receptor');
INSERT INTO clientes values (3, 'Alcides Miguel', 'Lambert', '13357898sc', '73387598', 'Av Alemana', 'Receptor');
INSERT INTO clientes values (4, 'Roberto', 'Godoy', '12457844sc', '77487448', 'Av Pirai', 'Emisor');
INSERT INTO clientes values (5, 'Alex', 'Franzlo', '12457554sc', '77487558', 'Av Pirai', 'Emisor');


CREATE TABLE Motociclistas (
    id_motociclista int not null AUTO_INCREMENT,
    nombre varchar(50) not null,
    apellidos varchar(50) not null,
    nro_carnet varchar(20) not null,
    telefono varchar(20) not null,
    direccion varchar(255) not null,
    placa varchar(10) not null,
    latitud float DEFAULT '0.00',
    longitud float DEFAULT '0.00',
    PRIMARY KEY(id_motociclista)
);

CREATE TABLE Pagos (
    id_pago int not null AUTO_INCREMENT,
    descripcion varchar(50) not null,
    PRIMARY KEY(id_pago)
)

--- pagos
insert into pagos (descripcion) VALUES ('Pagado');
insert into pagos (descripcion) VALUES ('Por Pagar');



CREATE TABLE Lugares (
    id_lugar int not null AUTO_INCREMENT,
    direccion varchar(255) not null, 
    latitud float not null,
    longitud float not null,
    PRIMARY KEY(id_lugar)
)
--- insert lugares
insert into lugares values (1, 'Calle robore pasillo #3', -17.786852, -63.196409);

CREATE TABLE Envios(
    id_envio int not null AUTO_INCREMENT,
    id_cliente_emisor int not null,
    id_cliente_receptor int not null,
    id_lugar_recojo int not null,
    id_lugar_entrega int not null,
    id_motociclista int not null,
    id_pago int not null,
    id_documento int not null,
    estado varchar(50),
    PRIMARY KEY(id_envio),
    foreign key(id_cliente_emisor) references Clientes(id_cliente),
    foreign key(id_cliente_receptor) references Clientes(id_cliente),
    foreign key(id_lugar_recojo) references Lugares(id_lugar),
    foreign key(id_lugar_entrega) references Lugares(id_lugar),
    foreign key(id_motociclista) references Motociclistas(id_motociclista),
    foreign key(id_pago) references Pagos(id_pago),
    foreign key(id_documento) references Documentos(id_documento)
)







+ id_motociclista int
+ nombre:varchar(50)
+ apellidos:varchar(50)
+ nro_carnet:varchar(20)
+ telefono:varchar(8)
+ direccion:varchar(255)
+ placa:varchar(10)
+ latitud:float
+ longitud:float




+ id_envio int 
+ id_cliente int 
+ id_motociclista int 
+ id_pago int 
+ id_documento int 
+ estado varchar(50),
    