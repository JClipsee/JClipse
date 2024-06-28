document.addEventListener('DOMContentLoaded', function () {
    const navLinks = document.querySelectorAll('.sidebar__nav a');
    const sections = document.querySelectorAll('.section');

    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetSection = document.querySelector(this.getAttribute('href'));
            sections.forEach(section => {
                section.classList.remove('active');
            });
            targetSection.classList.add('active');
        });
    });
});
