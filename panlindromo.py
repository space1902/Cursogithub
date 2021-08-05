def palindromo(palabra):
    palabra = palabra.replace(" " , "")
    palabra = palabra.lower()
    nueva_palabra = palabra[::-1]
    if nueva_palabra == palabra:
        return True
    else:
        return False




def main():
    palabra = input("Escribe una palabra : ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")

if __name__ == '__main__':
    main() 


