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

