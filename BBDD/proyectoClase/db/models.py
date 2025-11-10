#MAPEO DE LA BBDD CON PYTHON

from sqlalchemy import Column, Integer, BigInteger, String, Numeric, Text, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Rol(Base):
    __tablename__ = "rol"
    __table_args__ = {"schema": "scrum"}

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(20), nullable=False, unique=True)

    def __repr__(self):
        return f"<Rol id={self.id} nombre={self.nombre!r}>"


class Prioridad(Base):
    __tablename__ = "prioridad"
    __table_args__ = {"schema": "scrum"}

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(20), nullable=False, unique=True)

    def __repr__(self):
        return f"<Prioridad id={self.id} nombre={self.nombre!r}>"


class Estado(Base):
    __tablename__ = "estado"
    __table_args__ = {"schema": "scrum"}

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(20), nullable=False, unique=True)

    def __repr__(self):
        return f"<Estado id={self.id} nombre={self.nombre!r}>"


class Sprint(Base):
    __tablename__ = "sprints"
    __table_args__ = (
        UniqueConstraint("nombre", "fecha_inicio", name="uq_sprints_nombre_inicio"),
        {"schema": "scrum"},
    )

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    objetivo = Column(Text)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    estado_sprint = Column(String(10), nullable=False, default="PLANNED")

    # Relaciones
    tareas = relationship("Tarea", back_populates="sprint", cascade="all, delete-orphan", passive_deletes=True)

    def __repr__(self):
        return f"<Sprint id={self.id} nombre={self.nombre!r}>"


class Programador(Base):
    __tablename__ = "programadores"
    __table_args__ = (
        UniqueConstraint("nombre", "email", name="uq_programadores_nombre_email"),
        {"schema": "scrum"},
    )

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(120), nullable=False)
    rol_id = Column(BigInteger, ForeignKey("scrum.rol.id", onupdate="RESTRICT", ondelete="RESTRICT"), nullable=False)
    capacidad_horas = Column(Integer, nullable=False, default=0)

    rol = relationship("Rol")
    tareas = relationship("Tarea", back_populates="programador")

    def __repr__(self):
        return f"<Programador id={self.id} nombre={self.nombre!r} email={self.email!r}>"

class Etiqueta(Base):
    __tablename__ = "etiquetas"
    __table_args__ = {"schema": "scrum"}

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(40), nullable=False, unique=True)

    # Relación
    tareas_etiquetas = relationship("EtiquetaTarea", back_populates="etiqueta", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Etiqueta id={self.id} nombre={self.nombre!r}>"


class Tarea(Base):
    __tablename__ = "tareas"
    __table_args__ = (
        UniqueConstraint("sprint_id", "titulo", name="uq_tareas_sprint_titulo"),
        {"schema": "scrum"},
    )

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    titulo = Column(String(150), nullable=False)
    descripcion = Column(Text)

    story_points = Column(Integer, nullable=False, default=0)
    prioridad_id = Column(BigInteger, ForeignKey("scrum.prioridad.id", onupdate="RESTRICT", ondelete="RESTRICT"), nullable=False)
    estado_id = Column(BigInteger, ForeignKey("scrum.estado.id", onupdate="RESTRICT", ondelete="RESTRICT"), nullable=False)

    estimacion_horas = Column(Numeric(6, 2), nullable=False, default=0)
    horas_invertidas = Column(Numeric(6, 2), nullable=False, default=0)

    sprint_id = Column(BigInteger, ForeignKey("scrum.sprints.id", onupdate="CASCADE", ondelete="RESTRICT"), nullable=False)
    programador_id = Column(BigInteger, ForeignKey("scrum.programadores.id", onupdate="CASCADE", ondelete="RESTRICT"), nullable=False)

    # Relaciones
    sprint = relationship("Sprint", back_populates="tareas")
    programador = relationship("Programador", back_populates="tareas")
    prioridad = relationship("Prioridad")
    estado = relationship("Estado")
    tareas_etiquetas = relationship("EtiquetaTarea", back_populates="tarea", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Tarea id={self.id} titulo={self.titulo!r} sprint_id={self.sprint_id} programador_id={self.programador_id}>"


class EtiquetaTarea(Base):
    __tablename__ = "tareas_etiquetas"
    __table_args__ = (
        UniqueConstraint("tarea_id", "etiqueta_id", name="uq_tareas_etiquetas"),
        {"schema": "scrum"},
    )

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    tarea_id = Column(BigInteger, ForeignKey("scrum.tareas.id", ondelete="CASCADE"), nullable=False)
    etiqueta_id = Column(BigInteger, ForeignKey("scrum.etiquetas.id", ondelete="CASCADE"), nullable=False)

    tarea = relationship("Tarea", back_populates="tareas_etiquetas")
    etiqueta = relationship("Etiqueta", back_populates="tareas_etiquetas")

    def __repr__(self):
        return f"<EtiquetaTarea tarea_id={self.tarea_id} etiqueta_id={self.etiqueta_id}>"
