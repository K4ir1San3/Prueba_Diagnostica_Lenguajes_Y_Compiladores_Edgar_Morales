
def verificar_collatz(p, q):
    if q < 100 * p:
        return f"ERROR: El límite superior 'q' ({q}) debe ser al menos 100 veces 'p' ({p})."

    print(f"Demostrando conjetura en el intervalo [{p}, {q}]:\n")

    for n_original in range(p, q + 1):
        n = n_original
        secuencia = [str(n)]

        while n > 1:
            if n % 2 == 0:
                n = n // 2  # Para pares
            else:
                n = 3 * n + 1  # Para impares
            secuencia.append(str(n))
        
        print(f"n={n_original}: {' -> '.join(secuencia)}")

    return "\nDemostrado para todo el intervalo."

# EJEMPLO:
p_inicio = 6
q_fin = 800
resultado = verificar_collatz(p_inicio, q_fin)
print(resultado)

