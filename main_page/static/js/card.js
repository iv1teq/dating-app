const cards = document.querySelectorAll('.card-style');

cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width;
        const y = (e.clientY - rect.top) / rect.height;

        const rotY =  (x - 0.5) * 30;
        const rotX = -(y - 0.5) * 30;

        card.style.transform = `rotateX(${rotX}deg) rotateY(${rotY}deg) scale(1.04)`;
    });

    card.addEventListener('mouseleave', () => {
        card.style.transform = 'rotateX(0deg) rotateY(0deg) scale(1)';
    });
});