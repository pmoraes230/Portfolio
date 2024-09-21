const typedText = document.querySelector('.typed-text')
const cursor = document.querySelector('cursor')

const textArray = ["Desenvolvedor Web.", "Criador de Soluções Futuristas.", "Especialista em Interfaces Modernas."]
const typingDelay = 100;
const erasingDelay = 50
const newTextDelay = 500
let textArrayIndex = 0
let charIndex = 0

function type() {
    if (charIndex < textArray[textArrayIndex].length) {
        typedText.textContent += textArray[textArrayIndex].charAt(charIndex);
        charIndex++;
        setTimeout(type, typingDelay);
    } else {
        setTimeout(erase, typingDelay)
    }

    function erase() {
        if (charIndex > 0) {
            typedText.textContent = textArray[textArrayIndex].substring(0, charIndex -1);
            charIndex++
            setTimeout(erase, erasingDelay);
        } else {
            textArrayIndex++;
            if (textArrayIndex >= textArray.length) textArrayIndex = 0;
            setInterval(type, typingDelay + 1100)
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    setTimeout(type, newTextDelay + 250)
})