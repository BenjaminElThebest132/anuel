proyecto = input("Ingrese el tamaño del proyecto \n-Grande \n-Mediano \n-Pequeño \n--> ").lower()
lenguaje = input("En que lenguaje lo hara \n-java \n-python \n-html \n--> ")
if proyecto=="grande":
    if lenguaje == "python":
         print("El proyecto tardara 2 meses")
    elif lenguaje == "java":
         print("Tardara 3 meses")
    elif lenguaje == "html":
         print("Ni idea jaja")
    else:
         print("Se desconoce la practica")     
         
if proyecto =="mediano":
    if lenguaje == "python":
         print("El proyecto tardara 2 semanas")
    elif lenguaje == "java":
         print("Tardara 3 semanas")
    elif lenguaje == "html":
         print("Ni idea jaja")
    else:
         print("Se desconoce la practica") 

if proyecto =="pequeño":
    if lenguaje == "python":
         print("El proyecto tardara 2 dias")
    elif lenguaje == "java":
         print("Tardara 3 dias")
    elif lenguaje == "html":
         print("Ni idea jaja")
    else:
         print("Se desconoce la practica") 