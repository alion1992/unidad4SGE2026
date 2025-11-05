-- ================================
-- Catálogos base
-- ================================
INSERT INTO scrum.rol (nombre) VALUES
('DEV'), ('TEST'), ('LEAD');

INSERT INTO scrum.prioridad (nombre) VALUES
('LOW'), ('MEDIUM'), ('HIGH'), ('CRITICAL');

INSERT INTO scrum.estado (nombre) VALUES
('TODO'), ('DOING'), ('REVIEW'), ('DONE');

-- ================================
-- Programadores
-- ================================
INSERT INTO scrum.programadores (nombre, email, rol_id, capacidad_horas) VALUES
('Ana García',   'ana@empresa.com',   (SELECT id FROM scrum.rol WHERE nombre='DEV'),   30),
('Luis Pérez',   'luis@empresa.com',  (SELECT id FROM scrum.rol WHERE nombre='LEAD'),  40),
('Marta López',  'marta@empresa.com', (SELECT id FROM scrum.rol WHERE nombre='TEST'),  25),
('Sergio Ruiz',  'sergio@empresa.com',(SELECT id FROM scrum.rol WHERE nombre='DEV'),   35);

-- ================================
-- Etiquetas
-- ================================
INSERT INTO scrum.etiquetas (nombre) VALUES
('backend'),
('frontend'),
('bug'),
('api'),
('ux');

-- ================================
-- Sprints
-- ================================
INSERT INTO scrum.sprints (nombre, objetivo, fecha_inicio, fecha_fin, estado_sprint) VALUES
('Sprint 1', 'Implementación del login y registro', CURRENT_DATE, CURRENT_DATE + 14, 'ACTIVE'),
('Sprint 2', 'Mejoras en interfaz y pruebas unitarias', CURRENT_DATE + 15, CURRENT_DATE + 30, 'PLANNED');

-- ================================
-- Tareas
-- ================================
INSERT INTO scrum.tareas
(titulo, descripcion, story_points, prioridad_id, estado_id, estimacion_horas, horas_invertidas, sprint_id, programador_id)
VALUES
('Login básico', 'Pantalla de login y endpoint /login', 3,
 (SELECT id FROM scrum.prioridad WHERE nombre='HIGH'),
 (SELECT id FROM scrum.estado WHERE nombre='DOING'),
 8, 2,
 (SELECT id FROM scrum.sprints WHERE nombre='Sprint 1'),
 (SELECT id FROM scrum.programadores WHERE nombre='Ana García')
),

('Registro de usuarios', 'Validación de email y endpoint /register', 5,
 (SELECT id FROM scrum.prioridad WHERE nombre='MEDIUM'),
 (SELECT id FROM scrum.estado WHERE nombre='TODO'),
 12, 0,
 (SELECT id FROM scrum.sprints WHERE nombre='Sprint 1'),
 (SELECT id FROM scrum.programadores WHERE nombre='Luis Pérez')
),

('Diseño UI', 'Maquetación UI con Figma', 2,
 (SELECT id FROM scrum.prioridad WHERE nombre='LOW'),
 (SELECT id FROM scrum.estado WHERE nombre='REVIEW'),
 6, 4,
 (SELECT id FROM scrum.sprints WHERE nombre='Sprint 1'),
 (SELECT id FROM scrum.programadores WHERE nombre='Marta López')
),

('Corrección bug login', 'Error 500 al iniciar sesión con usuario inexistente', 1,
 (SELECT id FROM scrum.prioridad WHERE nombre='CRITICAL'),
 (SELECT id FROM scrum.estado WHERE nombre='TODO'),
 3, 0,
 (SELECT id FROM scrum.sprints WHERE nombre='Sprint 1'),
 (SELECT id FROM scrum.programadores WHERE nombre='Sergio Ruiz')
),

('Refactor backend', 'Cambiar lógica de autentificación', 8,
 (SELECT id FROM scrum.prioridad WHERE nombre='HIGH'),
 (SELECT id FROM scrum.estado WHERE nombre='TODO'),
 14, 0,
 (SELECT id FROM scrum.sprints WHERE nombre='Sprint 2'),
 (SELECT id FROM scrum.programadores WHERE nombre='Ana García')
);

-- ================================
-- Relación Tareas <-> Etiquetas
-- ================================
INSERT INTO scrum.tareas_etiquetas (tarea_id, etiqueta_id) VALUES
((SELECT id FROM scrum.tareas WHERE titulo='Login básico'),
 (SELECT id FROM scrum.etiquetas WHERE nombre='backend')),

((SELECT id FROM scrum.tareas WHERE titulo='Login básico'),
 (SELECT id FROM scrum.etiquetas WHERE nombre='api')),

((SELECT id FROM scrum.tareas WHERE titulo='Diseño UI'),
 (SELECT id FROM scrum.etiquetas WHERE nombre='ux')),

((SELECT id FROM scrum.tareas WHERE titulo='Corrección bug login'),
 (SELECT id FROM scrum.etiquetas WHERE nombre='bug')),

((SELECT id FROM scrum.tareas WHERE titulo='Refactor backend'),
 (SELECT id FROM scrum.etiquetas WHERE nombre='backend'));
