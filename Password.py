import secrets
import string

longitud = int(input("Introduce la longitud para la contraseña: "))

def generar_password(longitud):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(longitud))
    return password

password = generar_password(longitud)
print(password)
