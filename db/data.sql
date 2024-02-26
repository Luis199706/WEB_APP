CREATE TABLE data(
id INT NOT NULL,
name varchar(100),
email varchar(100),
phone varchar (100),
PRIMARY KEY (id)
);

CREATE TABLE users(
id INT NOT NULL AUTO_INCREMENT,
name varchar(100),
apellido_p varchar(100),
apellido_m varchar(100),
persona varchar(10),
estado varchar(5),
curp varchar(50),
PRIMARY KEY (id)
);

CREATE TABLE estados(
id INT NOT NULL,
nombre varchar(40),
clave varchar(5),
PRIMARY KEY (id)
);


INSERT INTO estados (id, nombre, clave) VALUES 
	(1,'Aguascalientes','AGS'),
	(2,'Baja California','BC'),
	(3,'Baja California Sur','BJS'),
	(4,'Campeche','CAM'),
	(5,'Chiapas','CHI'),
	(6,'Chihuahua','CHH'),
	(7,'Coahuila','COA'),
	(8,'Colima','COL'),
	(9,'Ciudad de México','CMDX'),
	(10,'Durango','DUR'),
	(11,'Estado de México','EDO'),
	(12,'Guanajuato','GUA'),
	(13,'Guerrero','GRO'),
	(14,'Hidalgo','HGO'),
	(15,'Jalisco','JAL'),
	(16,'Michoacán','MICH'),
	(17,'Morelos','MOR'),
	(18,'Nayarit','NAY'),
	(19,'Nuevo León','NLO'),
	(20,'Oaxaca','OAX'),
	(21,'Puebla','PUE'),
	(22,'Querétaro','QRO'),
	(23,'Quintana Roo','QROO'),
	(24,'San Luis Potosí','SLP'),
	(25,'Sinaloa','SIN'),
	(26,'Sonora','SON'),
	(27,'Tabasco','TAB'),
	(28,'Tamaulipas','TAM'),
	(29,'Tlaxcala','TLAX'),
	(30,'Veracruz','VER'),
	(31,'Yucatán','YUT'),
	(32,'Zacatecas','ZAC');


select  u.name, 
        u.apellido_p, 
        u.apellido_m, 
        u.persona, 
        es.nombre , 
        u.curp 
from estados es inner join users u on (es.id = u.estado)