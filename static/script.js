document.addEventListener('DOMContentLoaded', () => {
    const colorPicker = document.getElementById('setcolor');
    const content = document.getElementById('topbarR');
    const image = document.querySelector('#topbarL img');

    const applySavedColor = () => {
        const savedColor = localStorage.getItem('selectedColor');
        if (savedColor) {
            content.style.color = savedColor;
            image.style.backgroundColor = savedColor;
            colorPicker.value = savedColor;
        }
    };

    applySavedColor();
    colorPicker.addEventListener('input', (event) => {
        const selectedColor = event.target.value;
        content.style.color = selectedColor;
        image.style.backgroundColor = selectedColor;
        localStorage.setItem('selectedColor', selectedColor); 
    });
});
