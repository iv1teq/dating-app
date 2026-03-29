const logo = document.getElementById('my-logo');

document.addEventListener('mousemove', (e) => {
    const rect = logo.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;

    const dx = e.clientX - centerX;
    const dy = e.clientY - centerY;
    const angle = Math.atan2(dy, dx) * (180 / Math.PI);

    logo.style.transform = `rotate(${angle}deg)`;
});