document.addEventListener('DOMContentLoaded', function () {
    // Efeito de scroll suave para os links da navbar
    document.querySelectorAll('.navbar-link').forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            window.scrollTo({
                top: targetSection.offsetTop,
                behavior: 'smooth'
            });
        });
    });
});
