------------------
CREATE TABLE Logs (
    cod_accion INT NOT NULL AUTO_INCREMENT,
    descripcion VARCHAR(50) NOT NULL,
    usuario varchar(50) not null,
    fecha DATETIME NOT NULL,
    PRIMARY key(cod_accion)
)

----triggers tabla clientes
----after insert
DROP TRIGGER IF EXISTS TgInsertarClienteLog;
DELIMITER $$
CREATE TRIGGER TgInsertarClienteLog AFTER INSERT ON clientes
FOR EACH ROW
BEGIN
INSERT INTO Logs (descripcion, usuario, fecha)
VALUES (
    "Inserto cliente",
    CURRENT_USER,
    NOW());
END;
$$
DELIMITER ;

--- after update

DROP TRIGGER IF EXISTS TgUpdateClienteLog;
DELIMITER $$
CREATE TRIGGER TgUpdateClienteLog AFTER UPDATE ON clientes
FOR EACH ROW
BEGIN
INSERT INTO Logs (descripcion, usuario, fecha)
VALUES (
    "Se actualizo el cliente",
    CURRENT_USER,
    NOW());
END;
$$
DELIMITER ;


--- after delete

DROP TRIGGER IF EXISTS TgDeleteClienteLog;
DELIMITER $$
CREATE TRIGGER TgDeleteClienteLog AFTER DELETE ON clientes
FOR EACH ROW
BEGIN
INSERT INTO Logs (descripcion, usuario, fecha)
VALUES (
    "Se ELIMINO un cliente",
    CURRENT_USER,
    NOW());
END;
$$
DELIMITER ;

--- para probar triggers
INSERT INTO clientes VALUES(1, 'Fernando', 'Lopez', '12324354sc', '77414741', 'Av Luis Ortiz');
INSERT INTO clientes VALUES(2, 'Jose Luis', 'Lopez', '12326733sc', '77111741', 'Av Luis Ortiz');
INSERT INTO clientes VALUES(3, 'jorge Luis', 'Sanchez', '11126733sc', '77222741', 'Av Luis Ortiz');
UPDATE clientes SET nombre="Evo" where id_cliente = 1;



------ stored procedures


--- clientes

drop procedure insertar_cliente;

DELIMITER //
create procedure insertar_cliente(in _nombre varchar(50), in _apellidos varchar(50), in _nro_carnet varchar(50), in _telefono varchar(8), in _direccion varchar(255))
begin
    INSERT INTO clientes (nombre, apellidos, nro_carnet, telefono, direccion)
    VALUES (_nombre, _apellidos, _nro_carnet, _telefono, _direccion);
end//


drop procedure eliminar_cliente;

DELIMITER //
create procedure eliminar_cliente(in _id_cliente int)
begin
    DELETE FROM clientes where id_cliente = _id_cliente;
end//

call insertar_cliente('Robert', 'Lewandowski', '12459578sc', '77487487', 'Av Alemana');
call eliminar_cliente(4);