// Selecionar todos os links que começam com '#'
const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');

smoothScrollLinks.forEach(link => {
    link.addEventListener('click', (event) => {
        event.preventDefault(); // Previne o comportamento padrão

        const targetId = link.getAttribute('href');
        const targetElement = document.querySelector(targetId);

        // Rolagem suave
        targetElement.scrollIntoView({
            behavior: 'smooth'
        });
    });
});
