database = {
    "jose": "25957620",
    "milo": "52723751"
}

def login():
    username = input("Ingresa tu nombre de usuario: ")
    password = input("Ingresa tu Contraseña: ")

    if username in database and database[username] == password:
        print("Login Exitoso...")
    else: 
        print("Credenciales incorrectas. Por favor, intentalo de nuevo.")

login()

