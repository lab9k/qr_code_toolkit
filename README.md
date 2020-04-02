# Qr-code toolkit

The generic toolkit is located in 'qr_kit' and 'qr_kit_api'

## prerequisites

* python 3.8

## installation

```bash
$ pip install -r requirements.txt
$ python manage.py migrate
```

## running the development server

```bash
$ python manage.py runserver 
```

### TODO

* Remove UUID in favor of CharField, this way we can have fully custom (and short urls). When using the registration tool, there should never be a collision.