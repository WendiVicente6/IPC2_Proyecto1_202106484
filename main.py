def menu():
    print("")
    
    opcion = ''
    print("""------------------------------ ROBOT R2E2 ------------------------------""")
    while opcion != '6':
        print("")
        print("""Menú principal:
1. Cargar archivo
2. Procesar archivo
3. Escribir archivo XML de salida 
4. Mostrar datos del estudiante
5. Generar gráfica
6. Salida
        """)

        opcion = input("Ingrese una opcion: ")

        if opcion == '1':
            filename = input("Ingrese el archivo: ")

        
        

if __name__ == '__main__':
    menu()