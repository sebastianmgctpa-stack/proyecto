// Mostrar un mensaje de alerta en la página
function mostrarMensaje(mensaje, tipo = "info") {
    const alerta = document.getElementById("alerta");
    alerta.className = `alert alert-${tipo}`;
    alerta.textContent = mensaje;
    alerta.style.display = "block";
    // Ocultar el mensaje después de 4 segundos
    setTimeout(() => alerta.style.display = "none", 4000);
}

// Confirmar la eliminación de un evento
function confirmarEliminar(codigo) {
    return confirm(`¿Está seguro de eliminar el evento ${codigo}?`);
}

// Limpiar los campos del formulario
function limpiarFormulario(idFormulario) {
    document.getElementById(idFormulario).reset();
    mostrarMensaje("Los campos se han limpiado.", "info");
}

// Obtener la fecha y hora actual (formato legible)
function fechaActual() {
    return new Date().toLocaleString("es-CR");
}