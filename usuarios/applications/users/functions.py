# funciones extra de la aplicacion users
import random
import string

def cod_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choices(char) for _ in range(size))