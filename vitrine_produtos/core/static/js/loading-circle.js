function showLoadingCircle() {
    const circle = document.getElementById('loading-circle')

    circle.style.display = 'flex';
    circle.style.opacity = '1';
}

function hideLoadingCircle() {
    const circle = document.getElementById('loading-circle')

    setTimeout(() => {
        circle.style.opacity = '0';

        setTimeout(() => {
            circle.style.display = 'none'
        }, 100)
    },300)
}
