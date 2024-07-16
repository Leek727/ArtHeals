for (let i = 0; i < 100; i++) {
    try {
        // Get modal button and modal
        const modalButton = document.getElementById('modal-button' + i);
        const modal = document.getElementById('my-modal' + i);

        // Get close button and modal background
        const closeButton = document.getElementById('modal-close' + i);
        const modalBackground = document.getElementById('modal-background');

        // When the user clicks the modal button, open the modal
        modalButton.addEventListener('click', () => {
            modal.classList.add('is-active');
        });

        // When the user clicks the close button or modal background, close the modal
        closeButton.addEventListener('click', () => {
            modal.classList.remove('is-active');
        });

        modalBackground.addEventListener('click', () => {
            modal.classList.remove('is-active');
        });
    }catch(e) {}

}

