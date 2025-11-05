<h1> Instalar  sqlalchemy </h1>

```bash
pip install sqlalchemy psycopg2

<h2>Crear clase agente</h2>

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://franciscoaliahernandez:@localhost:5432/Tienda")

Session = sessionmaker(bind=engine)
session = Session()



