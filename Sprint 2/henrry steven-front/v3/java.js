console.log("esta funcionando")
// Espera 
document.addEventListener("", function() {
    // botones de la paguina henrry
    const Inicio = document.getElementById('Inicio');
    const Trámites = document.getElementById('tramites');
    const Contactos = document.getElementById('Contactos');
    const Ayuda = document.getElementById('Ayuda');

    // eventos para los botones 
    Inicio.addEventListener('click', function() {
        contentSection.v2html = '<h3>Página de Inicio</h3><p>Bienvenido a la página de inicio de One Window.</p>';
        console.log("funciona")
    });

    Trámites.addEventListener('click', function() {
        contentSection.v2html = '<h3>Trámites</h3><p>Aquí puedes gestionar tus trámites.</p>';
        console.log("si funcionando")
    });

    Contactos.addEventListener('click', function() {
        contentSection.v2html = '<h3>Ayuda</h3><p>Encuentra respuestas a tus preguntas frecuentes.</p>';
        console.log("esta funcionando")
    });

    Ayuda.addEventListener('click', function() {
        contentSection.v2html = '<h3>Más Información</h3><p>Aquí puedes encontrar más detalles sobre nuestros servicios.</p>';
        console.log("funcionando")
    });
})