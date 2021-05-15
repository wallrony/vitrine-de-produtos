function addProductRequest(dto, token) {
    const formData = new FormData()

    formData.append('name', dto['name'])
    formData.append('price', dto['price'])
    formData.append('description', dto['description'])
    formData.append('category', dto['category'])

    for (let i = 0 ; i < dto['images'].length; i++) {
        formData.append(`img${i}`, dto['images'][i])
    }

    const xhr = new XMLHttpRequest()

    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            if (xhr.status === 201) {
                window.location.href = '/manager/products'
            }

            hideLoadingCircle()
        }
    }
    xhr.open(
        'POST',
        `${window.location.origin}/api/core/products/`,
        true
    )
    xhr.setRequestHeader('Authorization', `Token ${token}`)
    xhr.send(formData)
}

function editProductRequest(dto, token) {
    const xhr = new XMLHttpRequest()

    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                window.location.href = '/manager/products'
            }

            hideLoadingCircle()
        }
    }
    xhr.open(
        'PUT',
        `${window.location.origin}/api/core/products/${dto['id']}`,
        true
    )
    xhr.setRequestHeader('Authorization', `Token ${token}`)
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.send(JSON.stringify(dto))
}

function loginRequest(dto, responseFun) {
    const xhr = new XMLHttpRequest()

    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                const data = JSON.parse(xhr.response)

                if(data['role'] === 2) {
                    responseFun(data)

                    window.location.href = '/manager/products'
                }
            }

            hideLoadingCircle()
        }
    }
    xhr.open(
        'POST',
        `${window.location.origin}/api/accounts/login/`,
        true
    )
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.send(JSON.stringify(dto))
}

function deleteProductRequest(productId, token) {
    const xhr = new XMLHttpRequest()

    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                window.location.reload()
            }

            hideLoadingCircle()
        }
    }
    xhr.open(
        'DELETE',
        `${window.location.origin}/api/core/products/${productId}`,
        true
    )
    xhr.setRequestHeader('Authorization', `Token ${token}`)
    xhr.send()
}

function deleteImageRequest(imgId, token) {
    const xhr = new XMLHttpRequest()

    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                window.location.reload()
            }

            hideLoadingCircle()
        }
    }
    xhr.open(
        'DELETE',
        `${window.location.origin}/api/core/products/images/${imgId}`,
        true
    )
    xhr.setRequestHeader('Authorization', `Token ${token}`)
    xhr.send()
}

function uploadImageRequest(productId, file, token) {
    const formData = new FormData()

    formData.append('img0', file)

    const xhr = new XMLHttpRequest()

    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            if (xhr.status === 201) {
                window.location.reload()
            }

            hideLoadingCircle()
        }
    }
    xhr.open(
        'POST',
        `${window.location.origin}/api/core/products/${productId}/images`,
        true
    )
    xhr.setRequestHeader('Authorization', `Token ${token}`)
    xhr.send(formData)
}

function saveCategoryRequest(dto, token, edit = false) {
    let method = 'POST'
    let path = `${window.location.origin}/api/core/category/`

    if (edit) {
        method = 'PUT'
        path = `${window.location.origin}/api/core/category/${dto['id']}`

        delete dto['id']
    }

    const xhr = new XMLHttpRequest()

    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                window.location.reload()
            }

            hideLoadingCircle()
        }
    }
    xhr.open(
        method,
        path,
        true
    )
    xhr.setRequestHeader('Authorization', `Token ${token}`)
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.send(JSON.stringify(dto))
}

function deleteCategoryRequest(catId, token) {
    const xhr = new XMLHttpRequest()

    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                window.location.reload()
            }

            hideLoadingCircle()
        }
    }
    xhr.open(
        'DELETE',
        `${window.location.origin}/api/core/category/${catId}`,
        true
    )
    xhr.setRequestHeader('Authorization', `Token ${token}`)
    xhr.send()
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
