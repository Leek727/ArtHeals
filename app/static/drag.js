document.addEventListener('DOMContentLoaded', () => {
    const container = document.querySelector('.columns.is-multiline');
    const updateOrderBtn = document.getElementById('update-order-btn');

    if (container) {
        new Sortable(container, {
            animation: 150
        });

        if (updateOrderBtn) {
            updateOrderBtn.addEventListener('click', () => {
                let order = [];
                document.querySelectorAll('.columns.is-multiline .column').forEach((el, index) => {
                    const id = el.querySelector('a').getAttribute('id').replace('modal-button', '');
                    order.push({ id: id, order: index });
                });

                fetch('/update_order', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(order)
                }).then(response => {
                    if (response.ok) {
                        alert('Order updated successfully!');
                    } else {
                        console.error('Failed to update order');
                        alert('Failed to update order');
                    }
                });
            });
        }

        document.querySelectorAll('[id^="save-button"]').forEach(button => {
            button.addEventListener('click', () => {
                const index = button.getAttribute('data-index');
                const card = document.querySelector(`#modal-button${index} .card`);
                const title = card.querySelector('.title.is-4').innerText;
                const price = card.querySelector('.subtitle.is-6:nth-of-type(1)').innerText;
                const desc = card.querySelector('.subtitle.is-6:nth-of-type(2)').innerText;
                const content = card.querySelector('.content').innerText;
                const imageFile = document.querySelector(`#image-upload${index}`).files[0];
                const formData = new FormData();

                formData.append('index', index);
                formData.append('title', title);
                formData.append('price', price);
                formData.append('desc', desc);
                formData.append('content', content);
                if (imageFile) {
                    formData.append('image', imageFile);
                }

                fetch('/update_card', {
                    method: 'POST',
                    body: formData
                }).then(response => {
                    if (response.ok) {
                        alert('Card updated successfully!');
                    } else {
                        console.error('Failed to update card');
                        alert('Failed to update card');
                    }
                });
            });
        });

        document.querySelectorAll('.image-upload').forEach(input => {
            input.addEventListener('change', (event) => {
                const index = event.target.id.replace('image-upload', '');
                const file = event.target.files[0];
                const reader = new FileReader();
                reader.onload = (e) => {
                    document.querySelector(`#card-image${index}`).src = e.target.result;
                    document.querySelector(`#modal-card-image${index}`).src = e.target.result;
                };
                reader.readAsDataURL(file);
            });
        });
    }
});
