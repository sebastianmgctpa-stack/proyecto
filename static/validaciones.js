// Validar el formulario de registro de eventos
function validarRegistro() {
    // Obtener los valores de los campos
    const codigo = document.getElementById("codigo").value.trim();
    const tipo = document.getElementById("tipo").value;
    const equipo = document.getElementById("equipo").value.trim();
    const nivel = document.getElementById("nivel").value;
    const estado = document.getElementById("estado").value;

    // Validaciones
    if (codigo === "") {
        alert("Debe ingresar el código del evento.");
        document.getElementById("codigo").focus();
        return false;
    }

    if (equipo === "") {
        alert("Debe indicar el equipo o recurso afectado.");
        document.getElementById("equipo").focus();
        return false;
    }

    return true; // Si todo es correcto, permite enviar el formulario
}