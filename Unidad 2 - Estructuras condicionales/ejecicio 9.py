magnitud_terremoto = int(input("ingrese la magnitud del terremoto"))
if magnitud_terremoto <= 3:
    print("muy leve, imperceptible")
elif magnitud_terremoto >=3 and magnitud_terremoto <=4:
    print("leve, legeramente perceptible")
elif magnitud_terremoto >=4 and magnitud_terremoto <=5:
    print("moderado, sentido por personas pero generalmente no causa daños")
elif magnitud_terremoto >=5 and magnitud_terremoto <=6:
    print("fuerte, puede causar daños en estructuras debiles")
elif magnitud_terremoto >=6 and magnitud_terremoto <=7:
    print("Muy fuerte, puede causar daños significativos")
else:
    print("Extremo, puede causar graves daños a gran escala")


