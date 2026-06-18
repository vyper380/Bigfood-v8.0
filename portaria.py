import csv
import datetime

ARQUIVO_DADOS = 'registros.csv'

def criar_arquivo():
    with open(ARQUIVO_DADOS, 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['ID', 'Nome', 'Entrada', 'Saída', 'Armário'])

def adicionar_registro(id, nome, entrada, saida, armario):
    with open(ARQUIVO_DADOS, 'a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([id, nome, entrada, saida, armario])

def pesquisar_registro(termo):
    with open(ARQUIVO_DADOS, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  # Saltar el encabezado
        print("Resultados de la búsqueda:")
        for linha in leitor:
            if termo.lower() in linha[1].lower():  # Buscar por nombre
                print(linha)

def registrar_entrada(id, nome):
    entrada = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    adicionar_registro(id, nome, entrada, None, None)
    print(f"Entrada registrada para {nome} con el ID {id}")

def registrar_saida(id):
    with open(ARQUIVO_DADOS, 'r') as archivo:
        leitor = csv.reader(archivo)
        registros = list(leitor)
    with open(ARQUIVO_DADOS, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(registros[0])  # Escribir el encabezado
        for registro in registros[1:]:
            if int(registro[0]) == id:
                registro[3] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            escritor.writerow(registro)
    print(f"Salida registrada para el ID {id}")

def entregar_chave(id, armario):
    with open(ARQUIVO_DADOS, 'r') as archivo:
        leitor = csv.reader(archivo)
        registros = list(leitor)
    with open(ARQUIVO_DADOS, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(registros[0])  # Escribir el encabezado
        for registro in registros[1:]:
            if int(registro[0]) == id:
                registro[4] = armario
            escritor.writerow(registro)
    print(f"Clave del armario {armario} entregada al ID {id}")

def devolver_chave(id):
    with open(ARQUIVO_DADOS, 'r') as archivo:
        leitor = csv.reader(archivo)
        registros = list(leitor)
    with open(ARQUIVO_DADOS, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(registros[0])  # Escribir el encabezado
        for registro in registros[1:]:
            if int(registro[0]) == id:
                registro[4] = ""
            escritor.writerow(registro)
    print(f"Clave del armario devuelta por el ID {id}")

# Crear el archivo si no existe
try:
    with open(ARQUIVO_DADOS, 'r') as archivo:
        pass
except FileNotFoundError:
    crear_archivo()

while True:
    print("\n--- Sistema de Portaría ---")
    print("1. Registrar entrada")
    print("2. Registrar salida")
    print("3. Entregar llave")
    print("4. Devolver llave")
    print("5. Buscar registro")
    print("6. Salir")

    opcion = int(input("Digite la opción deseada: "))

    if opcion == 1:
        id = int(input("Digite el ID de la persona: "))
        nombre = input("Digite el nombre de la persona: ")
        registrar_entrada(id, nombre)
    elif opcion == 2:
        id = int(input("Digite el ID de la persona: "))
        registrar_saida(id)
    elif opcion == 3:
        id = int(input("Digite el ID de la persona: "))
        armario = int(input("Digite el número de armario: "))
        entregar_chave(id, armario)
    elif opcion == 4:
        id = int(input("Digite el ID de la persona: "))
        devolver_chave(id)
    elif opcion == 5:
        termo = input("Digite el término de búsqueda (nombre): ")
        pesquisar_registro(termo)
    elif opcion == 6:
        break
    else:
        print("Opción inválida.")
        def registrar_entrada(id, nome):
    entrada = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Antes de adicionar o registro: id={id}, nome={nome}, entrada={entrada}")  # Nova linha para depuração
    adicionar_registro(id, nome, entrada, None, None)
    print(f"Entrada registrada para {nome} con el ID {id}")