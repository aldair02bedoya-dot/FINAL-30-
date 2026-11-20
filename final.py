# Programa de cifrado César 

def encriptar(mensaje, n):
    texto_final = ""
    mensaje = mensaje.upper()
    
    for letra in mensaje:
        # Revisamos si es una letra entre A y Z usando su valor ASCII (65 a 90)
        if letra.isalpha() and 'A' <= letra <= 'Z':
            pos = ord(letra) - ord('A')
            nueva_pos = (pos + n) % 26
            texto_final += chr(nueva_pos + ord('A'))
        else:
            texto_final += letra
            
    return texto_final


def desencriptar(mensaje, n):
    texto_final = ""
    mensaje = mensaje.upper()
    
    for letra in mensaje:
        if letra.isalpha() and 'A' <= letra <= 'Z':
            pos = ord(letra) - ord('A')
            nueva_pos = (pos - n) % 26
            texto_final += chr(nueva_pos + ord('A'))
        else:
            texto_final += letra
            
    return texto_final


guardados = []
opcion = ""

while opcion != "4":
    print("\nSISTEMA DE CIFRADO CÉSAR ")
    print("=================================")
    print("1. Encriptar mensaje (Opción de Guardar mensaje (S/N))")
    print("2. Desencriptar mensaje")
    print("3. Imprimir mensajes guardados")
    print("4. Salir")
    print("=================================")
    
    opcion = input("Seleccione una opción: ").strip()
    
    if opcion == "1":
        msg = input("Ingrese el mensaje: ")
        try:
            n = int(input("Ingrese el desplazamiento N: "))
            if n < 0:
                print("El desplazamiento N debe ser mayor o igual a 0.")
            else:
                cifrado = encriptar(msg, n)
                print("Mensaje original:", msg.upper())
                print("Mensaje encriptado:", cifrado)
                
                resp = input("¿Desea guardar el mensaje? (S/N): ").strip().upper()
                if resp == "S":
                    guardados.append({
                        "original": msg.upper(),
                        "cifrado": cifrado,
                        "N": n
                    })
                    print("Mensaje guardado correctamente.")
                elif resp != "N":
                    print("Opción no válida, el mensaje no se guardó.")
        except ValueError:
            print("Error: debe ingresar un número entero para N.")
            
    elif opcion == "2":
        msg_cifrado = input("Ingrese el mensaje encriptado: ")
        try:
            n = int(input("Ingrese el desplazamiento N: "))
            if n < 0:
                print("El desplazamiento N debe ser mayor o igual a 0.")
            else:
                original = desencriptar(msg_cifrado, n)
                print("Mensaje desencriptado:", original)
        except ValueError:
            print("Error: debe ingresar un número entero para N.")
            
    elif opcion == "3":
        if len(guardados) == 0:
            print("No hay mensajes guardados")
        else:
            print("\nMENSAJES GUARDADOS")
            contador = 1
            for item in guardados:
                print(f"{contador}. Original: {item['original']}")
                print(f"   Encriptado: {item['cifrado']}")
                print(f"   Desplazamiento: {item['N']}")
                contador += 1
                
    elif opcion == "4":
        print("Gracias por utilizar el sistema.")
        
    else:
        print("Opción no válida, intente de nuevo.")