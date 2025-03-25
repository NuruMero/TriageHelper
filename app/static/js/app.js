// Datos de ejemplo
const patients = [
    { 
        name: "María López García",
        age: 35,
        severity: 3,
        diagnosis: "Fractura de fémur",
        admitted: true
    },
    {
        name: "Carlos Martínez Ruiz",
        age: 28,
        severity: 4,
        diagnosis: "Luxación de hombro",
        admitted: true
    },
    {
        name: "Ana Sánchez Gómez",
        age: 67,
        severity: 2,
        diagnosis: "Esguince de tobillo",
        admitted: false
    }
];

let currentSort = 'desc';
let selectedPatient = null;

function renderPatients() {
    const container = document.getElementById('patientsContainer');
    container.innerHTML = '';
    
    patients.sort((a, b) => currentSort === 'desc' ? b.severity - a.severity : a.severity - b.severity)
            .forEach(patient => {
        const patientElement = document.createElement('div');
        patientElement.className = `patient-item ${selectedPatient === patient ? 'selected' : ''}`;
        patientElement.innerHTML = `
            <div>
                <h3>${patient.name}</h3>
                <p>${patient.diagnosis} - ${patient.admitted ? 'Ingresado' : 'Alta médica'}</p>
            </div>
            <div class="severity" style="background-color: ${getSeverityColor(patient.severity)}">
                Gravedad ${patient.severity}
            </div>
        `;
        
        patientElement.addEventListener('click', () => {
            selectedPatient = patient;
            renderPatients();
        });
        
        container.appendChild(patientElement);
    });
}

function getSeverityColor(severity) {
    const colors = ['#28a745', '#ffc107', '#fd7e14', '#dc3545', '#6c757d'];
    return colors[severity - 1];
}

document.getElementById('sortButton').addEventListener('click', () => {
    currentSort = currentSort === 'desc' ? 'asc' : 'desc';
    renderPatients();
});

// Carga inicial
renderPatients();