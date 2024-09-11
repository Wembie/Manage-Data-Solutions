let botton = document.getElementById('botton1');
let div1 = document.getElementById('div1');
let enlace = document.getElementById('enlace1');

function bloqueo_enlace(event){
    event.preventDefault()
    alert('¡ENLACE DESABILITADO!')

}

function mostrarMensaje(event){
alert(event.target);
alert(event.currentTarget)



};
div1.addEventListener('click', mostrarMensaje)

enlace.addEventListener('click', bloqueo_enlace)