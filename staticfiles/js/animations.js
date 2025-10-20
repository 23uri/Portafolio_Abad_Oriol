// Función para detectar si un elemento está en el viewport
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Función para activar animaciones cuando los elementos entran en el viewport
function handleScrollAnimations() {
    const animatedElements = document.querySelectorAll('.about-image img, .about-text h2, .card, .cta h2');
    
    animatedElements.forEach(element => {
        if (isInViewport(element)) {
            element.classList.add('animate');
        } else {
            // Removemos la clase cuando el elemento sale del viewport
            element.classList.remove('animate');
        }
    });
}

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
    // Activar animaciones iniciales
    handleScrollAnimations();
    
    // Activar animaciones al hacer scroll
    window.addEventListener('scroll', handleScrollAnimations);
    
    // Activar animaciones al cambiar el tamaño de la ventana
    window.addEventListener('resize', handleScrollAnimations);
});
