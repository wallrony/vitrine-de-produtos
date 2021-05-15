import os
from datetime import date
from uuid import uuid4


def change_image_name(instance, filename):
    extension = filename.split('.')[-1]

    filename = f'{instance.product_id}_img_{uuid4().hex}.{extension}'

    today = date.today()

    return os.path.join(
        f'images/products/{today.year}/{today.month}/{today.day}',
        filename
    )


def get_req_url(request):
    protocol = request.build_absolute_uri().split('/')[0]
    url = request.build_absolute_uri().split('/')[2]

    return f'{protocol}//{url}'
