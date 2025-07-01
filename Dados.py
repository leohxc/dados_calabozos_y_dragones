import random

dado_cuatro = [1, 2, 3, 4]
dado_seis = [1, 2, 3, 4, 5, 6]
dado_ocho = [1, 2, 3, 4, 5, 6, 7, 8]
dado_diez = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dado_doce = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dado_veinte = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
dados_caras = {
    4: dado_cuatro,
    6: dado_seis,
    8: dado_ocho,
    10: dado_diez,
    12: dado_doce,
    20: dado_veinte
}

def dados_dd():
    while True:
        opcion = input("Elegí una opción (4, 6, 8, 10, 12 o 20): ").strip()
        try:
            caras = int(opcion)
            if caras in dados_caras:
                resultado = random.choice(dados_caras[caras])
                print(f"Sacaste: {resultado}")
                break
            else:
                print("Opción inválida. Elegí entre 4, 6, 8, 10, 12 o 20.")
        except ValueError:
            print("Por favor, ingresá un número válido.")
def main():
    while True:
        dados_dd()
        seguir = input("¿Querés jugar otra vez? (s/n): ").lower()
        if seguir != 's':
            print("¡Gracias por jugar!")
            break
main()