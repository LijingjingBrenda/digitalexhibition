// Smooth scroll handled by CSS scroll-behavior; only override for nav clicks for older browsers
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === '#' || href.length < 2) return;
        const target = document.querySelector(href);
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// Active nav link highlight on scroll
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a');

function highlightNavigation() {
    const scrollY = window.pageYOffset;
    sections.forEach(section => {
        const top = section.offsetTop - 120;
        const bottom = top + section.offsetHeight;
        const id = section.getAttribute('id');
        if (scrollY >= top && scrollY < bottom) {
            navLinks.forEach(link => {
                link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
            });
        }
    });
}

window.addEventListener('scroll', highlightNavigation, { passive: true });
highlightNavigation();
