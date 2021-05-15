function nextCarousellImage(carousellId) {
    const carousell = document.getElementById(carousellId)
    const indicators = carousell.getElementsByTagName('div')[3]

    console.log(indicators)

    const images = carousell.getElementsByTagName('img')
    const spans = indicators.getElementsByTagName('span')

    for (let i =  0 ; i < images.length; i++) {
        if (images[i].classList.contains('active') && i < images.length - 1) {
            images[i].classList.remove('active')
            images[i + 1].classList.add('active')

            spans[i].classList.remove('active')
            spans[i + 1].classList.add('active')
        }
    }
}

function previousCarousellImage(carousellId) {
    const carousell = document.getElementById(carousellId)
    const indicators = carousell.getElementsByTagName('div')[3]

    const images = carousell.getElementsByTagName('img')
    const spans = indicators.getElementsByTagName('span')

    for (let i =  0 ; i < images.length; i++) {
        if (images[i].classList.contains('active') && i > 0) {
            images[i].classList.remove('active')
            images[i - 1].classList.add('active')

            spans[i].classList.remove('active')
            spans[i - 1].classList.add('active')
        }
    }
}
