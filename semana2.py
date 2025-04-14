edad = int(input("Ingresa tu edad: ") )

if edad < 0:
    mensaje = "La edad no puede ser negativa"
elif edad < 13:
    mensaje = "Eres un niño"
elif edad < 18:
    mensaje = "Eres un adolescente"
elif edad < 65:
    mensaje = "Eres un adulto"
else:
    mensaje = "Eres un adulto mayor"
