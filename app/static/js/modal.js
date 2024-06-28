document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('modal');
    const modalContent = document.getElementById('modal-body');
    const closeBtn = document.querySelector('.close-btn');

    closeBtn.addEventListener('click', function () {
        modal.style.display = 'none';
        modalContent.innerHTML = '';
    });

    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
            modalContent.innerHTML = '';
        }
    });

    document.querySelectorAll('.btn-edit, .btn-delete').forEach(button => {
        button.addEventListener('click', function () {
            const itemId = this.dataset.itemId;
            modalContent.innerHTML = `<p>Item ID: ${itemId}</p>`;
            modal.style.display = 'block';
        });
    });
});
