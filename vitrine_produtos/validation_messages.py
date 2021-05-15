def create_message(message):
    return {
        'message': message
    }


def invalid_email():
    return create_message('O e-mail insnerido é inválido.')


def email_already_used():
    return create_message('O e-mail inserido já está sendo utilizado.')


def user_successfully_created():
    return create_message('Conta cadastrada com sucesso!')


def field_is_missing(field):
    return create_message(f'É necessário informar o campo {field}!')

def image_upload_error():
    return create_message(
        'Houve um erro ao salvar as imagens do produto. '
        'Por favor, procure o produto cadastro e tente novamente.'
    )
