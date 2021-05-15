function getFile(inputId) {
    document.getElementById(inputId).click()
    document.getElementById(inputId).onchange = (e) => {
        e.stopPropagation();

        const files = e.target.files

        addImageInList('image-list', files)

        e.target.value = undefined
    }
}

function addImageInList(divId, files) {
    const division = document.createElement('div')
    division.className = 'selected-image'

    const imgElement = document.createElement('img')
    imgElement.src = URL.createObjectURL(files[0])

    const imgQtd = document.getElementById(divId)
        .getElementsByTagName('img')
        .length

    const fileInput = document.createElement('input')
    fileInput.type = 'file'
    fileInput.name = `img${imgQtd}`
    fileInput.style.display = 'none'
    fileInput.files = files

    const removeBtn = document.createElement('button')
    removeBtn.className = 'app-btn danger remove-product-image'
    removeBtn.innerHTML = '🞩'

    removeBtn.onclick = () => division.remove()

    division.append(removeBtn)
    division.append(imgElement)
    division.append(fileInput)

    document.getElementById(divId).append(division)
}

function setProductCategory(selectId, categoryId) {
    document.getElementById(selectId).value = categoryId
}

function setUserNameInAside() {
    let user = localStorage.getItem('VP@USER')

    try {
        user = JSON.parse(user)
    } catch { }

    if (user) {
        document.getElementById('user-name').innerText = `Olá, ${user['name']}`
    }
}

function showAppModal(modalId) {
    const modal = document.getElementById(modalId)

    modal.classList.add('prepare')

    setTimeout(() => {
        modal.classList.remove('prepare')
        modal.classList.add('show')
    }, 100)
}

function hideAppModal(modalId) {
    const modal = document.getElementById(modalId)

    modal.classList.add('prepare')
    modal.classList.remove('show')

    setTimeout(() => {
        modal.classList.remove('prepare')
    }, 350)
}

function toggleAsideMenu() {
    const menu = document.getElementById('app-aside-menu')

    if (menu.classList.contains('show')) {
        menu.classList.remove('show')
    } else {
        menu.classList.add('show')
    }
}
