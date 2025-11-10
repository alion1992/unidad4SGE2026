<h1> Instalar  sqlalchemy </h1>

```bash
pip install sqlalchemy psycopg2
```

<h2>Crear clase agente</h2>

Inicializa la conexión y permite que cualquier parte del proyecto pueda acceder a la base de datos.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://franciscoaliahernandez:@localhost:5432/Tienda")

Session = sessionmaker(bind=engine)
session = Session()
```

<h2>Modelos</h2>

Esta carpeta contiene las clases Python que representan las tablas reales de la base de datos.
Cada archivo mapea una tabla, por ejemplo:

rol.py → tabla scrum.rol

programadores.py → tabla scrum.programadores

tareas.py → tabla scrum.tareas

```python
#Ejemplo de la clase models de Rol
from sqlalchemy import Column, Integer, BigInteger, String, Numeric, Text, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Rol(Base):
    __tablename__ = "rol"
    __table_args__ = {'schema': 'scrum'}

    id = Column(Integer, primary_key=True)
    nombre = Column(String(20), unique=True, nullable=False)

```

<h2>Ejemplos</h2>

### Tipos de datos más comunes en SQLAlchemy

| Tipo SQLAlchemy | Equivalente en PostgreSQL | Uso común |
|-----------------|---------------------------|-----------|
| `Integer`       | INTEGER                   | Números enteros pequeños/medios (id, cantidades, estados) |
| `BigInteger`    | BIGINT                    | Enteros grandes (id autoincrementales, claves externas grandes) |
| `SmallInteger`  | SMALLINT                  | Enteros muy pequeños (catálogos, flags) |
| `Numeric(p,s)`  | NUMERIC(p,s) / DECIMAL    | Precios, horas, dinero, valores exactos en decimal |
| `Float`         | REAL / DOUBLE PRECISION   | Valores con coma flotante (no exactos) |
| `Boolean`       | BOOLEAN                   | true / false |
| `String(n)`     | VARCHAR(n)                | Cadenas de longitud limitada |
| `Text`          | TEXT                      | Cadenas largas sin límite |
| `Date`          | DATE                      | Solo fecha |
| `Time`          | TIME                      | Solo hora |
| `DateTime`      | TIMESTAMP                 | Fecha + hora |
| `LargeBinary`   | BYTEA                     | Archivos binarios (imágenes, pdf, bytes) |
| `Enum(...)`     | ENUM                      | Listas de valores fijos (ACTIVO, INACTIVO, etc.) |
| `JSON` / `JSONB`| JSON / JSONB              | Datos estructurados en formato JSON |


###  Campos relacionados con claves
| Tipo | Uso |
|------|-----|
| `ForeignKey("tabla.columna")` | Crea clave foránea a otra tabla |
| `PrimaryKeyConstraint`        | Define clave primaria compuesta |
| `UniqueConstraint`            | Restricción UNIQUE en una o varias columnas |

###  Ejemplo básico en un modelo

```python
from sqlalchemy import Column, Integer, String, Date, Numeric, Boolean

class Producto(Base):
    __tablename__ = "producto"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Numeric(10,2), nullable=False)
    stock = Column(Integer, default=0)
    disponible = Column(Boolean, default=True)
    fecha_alta = Column(Date)

```

###  Ejemplo modelo con relaciones en un modelo

```python
from sqlalchemy import (
    Column, Integer, String, Date, Numeric, ForeignKey,
    UniqueConstraint
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(120), nullable=False, unique=True)   

    # Relación 1:N con Pedido
    pedidos = relationship("Pedido", back_populates="cliente")

    def __repr__(self):
        return f"<Cliente(id={self.id}, nombre='{self.nombre}')>"


class Pedido(Base):
    __tablename__ = "pedido"

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    total = Column(Numeric(10,2), default=0)

    # Clave foránea
    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)

    # Relación inversa
    cliente = relationship("Cliente", back_populates="pedidos")

    def __repr__(self):
        return f"<Pedido(id={self.id}, total={self.total})>"
```

<h1>CONSULtAS CON FILTER</h1>

### Obtener todos los registros de una tabla (.all)

```python
productos = session.query(Producto).all()

for p in productos:
    print(p.id, p.nombre, p.precio)
```

Esto equivale a 

```sql
SELECT * FROM producto;
```

#### filter() + all()

```python
productos_baratos = session.query(Producto).filter(Producto.precio < 10).all()

for p in productos_baratos:
    print(p.nombre, p.precio)
```
Esto equivale a 

```sql
SELECT * FROM producto WHERE precio < 10;
```
### filter con igualdad

```python
teclados = session.query(Producto).filter(Producto.nombre == "Teclado").all()
```

### first() vs all()

First devuelve el primero o None

All devuelve una lista sobre la que iterar

### Order by

```python 
productos = session.query(Producto).order_by(Producto.precio.desc()).all()
```

### limit y offset

```python
            while True:
                resp = input("¿Quieres otras dos?")

                if resp.lower() == "no":
                    print("adios")
                    break

                if resp.lower() == "si":
                    dosSiguientes = session.query(Tarea).filter(Tarea.estimacion_horas > 2).offset(2).limit(2).all()
                    for tarea in dosSiguientes:
                        print(f"{tarea.titulo}")
                else:
                    print("No has introducido la respuesta")
```

### Select con columnas específicas

```python
productos_especificos = session.query(Producto.nombre, Producto.precio).all()
```
### Join 

```python
tareas = (
    session.query(Tarea, Programador)
    .join(Programador, Tarea.programador_id == Programador.id)
    .filter(Programador.nombre == "Ana García")
    .all()
)

for tarea, programador in tareas:
    print(tarea.titulo, "-", programador.nombre)
```




