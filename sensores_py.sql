CREATE TABLE `sensores` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `tipo_dato` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4

CREATE TABLE `valores` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `sensor_id` int(10) unsigned NOT NULL,
  `flotante` float DEFAULT NULL,
  `booleano` tinyint(4) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `valores_sensor_id` (`sensor_id`),
  CONSTRAINT `valores_sensor_id` FOREIGN KEY (`sensor_id`) REFERENCES `sensores` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4

INSERT INTO `sensores` (`nombre`,`tipo_dato`) VALUES ("Temperatura","flotante"), ("Humedad","flotante"), ("PIR","booleano"), ("Ultrasonico","flotante")
