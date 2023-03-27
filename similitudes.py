import random
import os

# Nombre del archivo donde se guardarán los números
filename = "numeros.txt"

# Nombre del archivo donde se guardarán los resultados
resultados_filename = "resultados.txt"


for j in range(1):
    # Verificar si el archivo existe para decidir si se crea una nueva secuencia o se añade a la anterior
    if not os.path.exists(filename):
        # Abrir el archivo en modo escritura
        with open(filename, "w") as f:
            # Bucle de 1000000 ejecuciones
            for i in range(37):
                # Generar número aleatorio entre 0 y 36
                num = random.randint(0, 36)
                # Escribir número en el archivo separado por comas
                f.write(str(num) + ", ")
            # Agregar salto de línea al final de la secuencia
            f.write("\n")
    else:
        # Obtener el número de la última secuencia guardada
        with open(filename, "r") as f:
            num_secuencias = f.read().count("secuencia") + 1

        # Abrir el archivo en modo append (añadir al final)
        with open(filename, "a") as f:
            # Agregar salto de línea y etiqueta de la nueva secuencia
            f.write(f"\nsecuencia{num_secuencias}: ")
            # Bucle de 1000 ejecuciones
            for i in range(100):
                # Generar número aleatorio entre 0 y 36
                num = random.randint(0, 36)
                # Escribir número en el archivo separado por comas
                f.write(str(num) + ", ")
            # Agregar salto de línea al final de la secuencia
            f.write("\n")

        # Leer la última secuencia guardada
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in reversed(lines):
                if line.startswith("secuencia"):
                    last_sequence = line
                    break

        # Obtener los números y porcentajes de la última secuencia guardada sin contar repeticiones
        nums = last_sequence.split(":")[1].split(",")
        nums = [num.strip() for num in nums]
        unique_nums = list(set(nums))
        unique_nums = [int(num) for num in unique_nums if num]
        unique_nums.sort()
        counts = [nums.count(str(num)) for num in unique_nums]
        percentages = [count / float(len(nums)) * 100 for count in counts]

        # Escribir los números y porcentajes en el archivo de resultados
        with open(resultados_filename, "a") as f:
            f.write(f"Secuencia {num_secuencias}: ")
            for i in range(len(unique_nums)):
                num = unique_nums[i]
                percent = percentages[i]
                f.write(f"{num} ({percent:.2f}%), \n")
