#Importar las libreria 

import sqlite3

#Establecer la conexión
conexion = sqlite3.connect('web2.sqlite3')
cursor = conexion.cursor()

#eliminar la tabla
cursor.execute("""
DROP TABLE IF EXISTS productos;
""")

#Crear la tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY,
    categoria TEXT NOT NULL, 
    marca TEXT NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL, 
    precio INTEGER NOT NULL 
);
""")

#Insertar los datos iniciales

datos = [
  (101, 'Smartwatch', 'Apple', 'Apple Watch Series 7', 'GPS, 32GB, Pantalla Retina Siempre Encendida, 4G LTE, Resistente al Agua', 699900),
  (104, 'Smartphone', 'Samsung', 'Galaxy Z Fold 4', '512GB+12GB RAM, Pantalla plegable 7.6p, Chip Exynos 2200, Cámaras 108MP+12MP+16MP', 2599990),
  (201, 'Portátil', 'Microsoft', 'Surface Laptop 5', 'Chip Intel Core i7 12th Gen, 16GB RAM, 1TB SSD, Pantalla táctil PixelSense de 14.4p', 2299990),
  (203, 'Portátil', 'Dell', 'XPS 15', 'Chip Intel Core i9 12th Gen, 32GB RAM, 2TB SSD, Pantalla InfinityEdge 4K+ OLED de 15.6p', 3799990),
  (207, 'Portátil', 'Acer', 'Swift 5', 'Chip Intel Core i7 12th Gen, 16GB RAM, 1TB SSD, Pantalla táctil Full HD de 14p, Peso ultraligero', 1699990),
  (208, 'Portátil', 'HP', 'Spectre x360', 'Chip Intel Core i7 12th Gen, 16GB RAM, 1TB SSD, Pantalla táctil AMOLED 4K de 13.3p, Convertible', 2699990),
  (301, 'Tablet', 'Samsung', 'Galaxy Tab S8', '256GB, Pantalla Super AMOLED de 11p, S Pen incluido, 5G, Dolby Atmos', 1399990),
  (302, 'Tablet', 'Lenovo', 'Tab P12 Pro', '128GB, Pantalla OLED de 12.6p, Snapdragon 8 Gen 1, Cuatro altavoces JBL con sonido Dolby Atmos', 1099990),
  (304, 'Tablet', 'Huawei', 'MatePad Pro 12.6', '256GB, Pantalla OLED de 12.6p, Kirin 9000E, Cámara de 13MP, M-Pencil incluido', 1799990),
]

cursor.executemany("""
INSERT INTO productos VALUES (?, ?, ?, ?, ?, ?);
""", datos)

# grabar
conexion.commit()
conexion.close()