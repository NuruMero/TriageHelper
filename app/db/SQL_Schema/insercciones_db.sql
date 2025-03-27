------------- INSERCCIONES ----------------
USE hospital; 

-- Inserciones de pacientes
INSERT INTO paciente (dni, nombre, edad, doctor_asignado, ingresado_actualmente, motivo_ingreso, gravedad_ingreso, historial) VALUES
-- Pacientes de Juan Pérez (Cardiología)
('98765432A', 'Carlos Martínez', 35, '12345678A', TRUE, 'Dolor en el pecho', 4, 'Hipertensión arterial, antecedentes familiares de enfermedades cardíacas'),
('11223344E', 'María Ruiz', 30, '12345678A', FALSE, 'Dificultades respiratorias', 5, 'Asma y alergias estacionales'),
('55667788I', 'Carmen Díaz', 45, '12345678A', TRUE, 'Infarto leve', 5, 'Enfermedad cardiovascular'),
('99001122M', 'Lucía Pérez', 37, '12345678A', FALSE, 'Dificultad para respirar', 4, 'Neumonía leve, antecedente de asma'),
('87654321B', 'Laura Fernández', 28, '23456789B', FALSE, 'Dolores de cabeza persistentes', 3, 'Migraña crónica'),
('22334455F', 'Javier Martínez', 42, '23456789B', TRUE, 'Ataque de migraña severo', 3, 'Migraña crónica, insomnio'),
('66778899J', 'Raúl Sánchez', 35, '23456789B', FALSE, 'Cefalea crónica', 3, 'Migraña, hipertensión controlada'),
('76543210C', 'Pedro González', 60, '34567890C', TRUE, 'Fractura de pierna', 2, 'Accidente doméstico, osteoporosis'),
('33445566G', 'Isabel Fernández', 60, '34567890C', FALSE, 'Infección respiratoria', 2, 'Historia de neumonía, bronquitis'),
('77889900K', 'Paula Jiménez', 27, '34567890C', TRUE, 'Accidente de tráfico', 2, 'Traumatismos múltiples'),
('65432109D', 'Sofía López', 50, '45678901D', FALSE, 'Esguince de tobillo', 1, 'Recuperación de cirugía de ligamento'),
('44556677H', 'Antonio García', 58, '45678901D', TRUE, 'Fractura de muñeca', 4, 'Accidente laboral'),
('12131455P', 'Victor Herrera', 65, '45678901D', TRUE, 'Fractura de costillas', 4, 'Caída accidental, osteoporosis'),
('10111233N', 'Esteban Gómez', 55, '45678901D', TRUE, 'Parálisis facial', 2, 'Accidente cerebrovascular');


INSERT INTO doctor (dni, nombre, edad, especialidad, contrasenya) VALUES
('12345678A', 'Juan Pérez', 45, 'Cardiología', '1234M'),
('23456789B', 'Ana Gómez', 38, 'Neurología', '123A'),
('34567890C', 'Luis Rodríguez', 50, 'Pediatría', '12B'),
('45678901D', 'Marta Sánchez', 40, 'Traumatología', 'ABC4');

