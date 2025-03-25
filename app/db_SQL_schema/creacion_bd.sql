CREATE DATABASE hospital;

USE hospital; 

CREATE TABLE paciente (
    dni VARCHAR(9) PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL, 
    edad INT,
    doctor_asignado VARCHAR(9),
    ingresado_actualmente BOOLEAN DEFAULT FALSE,
    motivo_ingreso TEXT NOT NULL,
    gravedad_ingreso INT CHECK (gravedad_ingreso BETWEEN 1 AND 5),
    historial TEXT
)

CREATE TABLE doctor (
    dni VARCHAR(9) PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL, 
    edad INT,
    especialidad VARCHAR(20),
    contrasenya VARCHAR(255)
)