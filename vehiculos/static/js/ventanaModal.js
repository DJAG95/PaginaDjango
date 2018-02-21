//Hace referencia al Div que va a enseñar
var modal = document.getElementById('myModal');

// Selecciona el botón que abre la ventana modal
var btn = document.getElementById("modalBtn");

// Selecciona el elemento que cierra el modal
var span = document.getElementsByClassName("close")[0];

// Abrir modal
function compartir(ejemplar) {
	document.getElementById("formComplete").innerHTML = "<input type='hidden' name='id_ejemplar' value="+ejemplar+"><input type='submit' class='btn btn-default' value='Confirmar'>";
    modal.style.display = "block";
}

// Cerrar cuando pulse la X
span.onclick = function() {
    modal.style.display = "none";
}

// Cerrar cuando haga click fuera de la ventana modal
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}