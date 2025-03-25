------------- INSERCCIONES ----------------
USE hospital; 

INSERT INTO paciente (dni, nombre, edad, doctor_asignado, ingresado_actualmente, motivo_ingreso, gravedad_ingreso, historial) VALUES
('98765432A', 'Carlos Martínez', 35, '12345678A', TRUE, 'Dolor en el pecho', 4, 'Hipertensión arterial, antecedentes familiares de enfermedades cardíacas'),
('87654321B', 'Laura Fernández', 28, '23456789B', FALSE, 'Dolores de cabeza persistentes', 3, 'Migraña crónica'),
('76543210C', 'Pedro González', 60, '34567890C', TRUE, 'Fractura de pierna', 2, 'Accidente doméstico, osteoporosis'),
('65432109D', 'Sofía López', 50, '45678901D', FALSE, 'Esguince de tobillo', 1, 'Recuperación de cirugía de ligamento');

INSERT INTO doctor (dni, nombre, edad, especialidad, contrasenya) VALUES
('12345678A', 'Juan Pérez', 45, 'Cardiología', '1234M'),
('23456789B', 'Ana Gómez', 38, 'Neurología', '123A'),
('34567890C', 'Luis Rodríguez', 50, 'Pediatría', '12B'),
('45678901D', 'Marta Sánchez', 40, 'Traumatología', 'ABC4');

