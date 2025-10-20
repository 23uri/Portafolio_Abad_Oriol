// Use IntersectionObserver to add 'animate' class when elements enter the viewport.
// Fallback to scroll-based checks if IntersectionObserver is not available.

document.addEventListener('DOMContentLoaded', function() {
    const selector = '.about-image img, .about-text h2, .card, .cta h2';
    let elements = Array.from(document.querySelectorAll(selector)).filter(el => !el.classList.contains('animate'));

    if ('IntersectionObserver' in window) {
        const io = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate');
                    // one-shot: stop observing after first intersection
                    observer.unobserve(entry.target);
                }
            });
        }, {
            root: null,
            rootMargin: '0px 0px -10% 0px', // trigger slightly before fully visible
            threshold: 0.12
        });

        elements.forEach(el => io.observe(el));
    } else {
        // Fallback: basic in-viewport check and scroll/resize listeners
        function isInViewport(el) {
            const rect = el.getBoundingClientRect();
            const vh = window.innerHeight || document.documentElement.clientHeight;
            return rect.top < vh * 0.9 && rect.bottom >= 0; // partially visible
        }

        function applyFallback() {
            // iterate a copy since we'll remove items from the array
            for (let i = elements.length - 1; i >= 0; i--) {
                const el = elements[i];
                if (isInViewport(el)) {
                    el.classList.add('animate');
                    // remove from array so we don't check it again
                    elements.splice(i, 1);
                }
            }
            // if no elements left to observe, remove listeners
            if (elements.length === 0) {
                window.removeEventListener('scroll', applyFallback);
                window.removeEventListener('resize', applyFallback);
            }
        }

        applyFallback();
        window.addEventListener('scroll', applyFallback, { passive: true });
        window.addEventListener('resize', applyFallback);
    }
});
