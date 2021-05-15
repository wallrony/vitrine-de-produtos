function validateLogin(formId) {
    const validations = {
        'email': validateEmail,
        'password': validatePswd
    }

    return getFormValues(validations, formId)
}

function validateSaveProduct(formId) {
    const validations = {
        'name': simpleMandatoryValidate,
        'description': undefined,
        'price': validateProdPrice,
        'category': simpleMandatoryValidate
    }

    const values = getFormValues(validations, formId)

    const imageList = document.getElementById('image-list')

    values['images'] = validateProdImages(imageList)

    return values
}

function validateSaveCategory(formId) {
    const validations = {
        'id': undefined,
        'name': simpleMandatoryValidate,
    }

    return getFormValues(validations, formId)
}

function getFormValues(validations, formId) {
    const form = document.getElementById(formId)

    const formGroups = form.getElementsByClassName('form-group')

    let values = {}

    for (let i = 0 ; i < formGroups.length; i++) {
        const group = formGroups[i]

        let input = group.getElementsByTagName('input')[0]

        if (!input) input = group.getElementsByTagName('select')[0]
        if (!input) input = group.getElementsByTagName('textarea')[0]
        if (!input) continue

        const validateFunc = validations[input.name]

        let error;

        if (validateFunc) {
            error = validateFunc(input.value)
        }

        if (error) {
            highlightInput(input)
            showError(group, error, input)

            values = undefined
            break
        } else {
            values[input.name] = input.value
        }
    }

    return values
}

// Auth Validators
function validateEmail(value) {
    if (!value.length) {
        return 'Este campo é obrigatório'
    } else if (!value.includes('@')) {
        return 'E-mail inválido!'
    }

    return undefined;
}

function validatePswd(value) {
    if (!value.length) {
        return 'Este campo é obrigatório'
    }

    return undefined
}

// Save Product Validators
function validateProdPrice(value) {
    if (!value.length) {
        return 'Este campo é obrigatório'
    } else if (Number(value) < .5) {
        return 'O preço minimo sao 50 centavos.'
    }

    return undefined
}

function validateProdImages(imageList) {
    const files = imageList
        .getElementsByTagName('input')

    const selectedImages = []

    for(let i = 0 ; i < files.length; i++) {
        if(files[i].name.includes('img')) {
            selectedImages.push(files[i].files[0])
        }
    }

    return selectedImages
}

function simpleMandatoryValidate(value) {
    if (!value.length) {
        return 'Este campo é obrigatório'
    }

    return undefined
}

function highlightInput(input) {
    input.style.borderColor = '#FD0000'

    input.focus()

    setTimeout(() => {
        input.style.borderColor = 'transparent'
    }, 1000)
}

function showError(group, error, input) {
    const errorParagraph = document.createElement('p')
    errorParagraph.innerText = error;
    errorParagraph.className = 'error-paragraph'

    group.append(errorParagraph)

    input.oninput = () => hideError(errorParagraph, input)
    input.onchange = () => hideError(errorParagraph, input)
}

function hideError(errorParagraph, input) {
    errorParagraph.remove()

    input.onchange = undefined
}
