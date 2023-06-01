calcular = input("Desea calcular su edad? (Y/N) ")

if (calcular == "Y" or calcular == "y"):
    añoActual = 2023
    año = int(input("En que año le gustarìa saber su edad? "))
    edad = int(input("Ingrese su edad: "))
    if(año > añoActual):
        añoCalculo = año - añoActual
        edadCalculada = edad + añoCalculo
        print("Dentro de", añoCalculo, "años, su edad serà:", edadCalculada)
    elif(añoActual > año):
        añoCalculo = añoActual - año
        edadCalculada = edad - añoCalculo
        if(edadCalculada > 0):
            print("En", año, "su edad era:", edadCalculada)
        else :
            print("Usted aun no habia nacido")
    else:
        ("ingrese un valor valido")
else :
    print("gracias")