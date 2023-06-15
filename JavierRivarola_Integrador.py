import json

def iniciarSesion():
    usuarios = cargarUsuarios()

    usuario = input("Ingrese su nombre de usuario: ")
    if not any(u["nombre"] == usuario for u in usuarios):
        print("El usuario no existe.")
        return

    contrasena = input("Ingrese su contraseña: ")
    intentos = 3

    while intentos > 0:
        if any(u["nombre"] == usuario and u["contrasena"] == contrasena for u in usuarios):
            print("Inicio de sesión exitoso.")
            return

        intentos -= 1
        print("Contraseña incorrecta. Intentos restantes:", intentos)
        contrasena = input("Ingrese su contraseña: ")

    print("Se agotaron los intentos. Inicio de sesión fallido.")

def crearUsuario():
    usuarios = cargarUsuarios()

    nombre = input("Ingrese el nombre de usuario: ")
    if any(u["nombre"] == nombre for u in usuarios):
        print("El usuario ya existe. Intente nuevamente.")
        return

    contrasena = input("Ingrese la contraseña: ")

    usuario = {
        "nombre": nombre,
        "contrasena": contrasena
    }

    usuarios.append(usuario)

    guardarUsuarios(usuarios)
    print("Usuario creado exitosamente.")

def guardarUsuarios(usuarios):
    with open("usuarios.txt", "w") as file:
        json.dump(usuarios, file, indent=4)

def cargarUsuarios():
    try:
        with open("usuarios.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
        
def main():
    while True:
        print("\n--- Menú ---")
        print("1. Crear usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            crearUsuario()
        elif opcion == "2":
            iniciarSesion()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()