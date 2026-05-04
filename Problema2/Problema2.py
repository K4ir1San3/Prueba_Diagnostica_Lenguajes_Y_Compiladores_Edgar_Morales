
import re

def validar_fen(fen):
    campos = fen.split(' ')
    if len(campos) != 6:
        return "ERROR: Faltan campos (deben ser 6)"

    posicion, turno, enroque, al_paso, media_jugada, nro_jugada = campos

    # 1: Validación de las posiciones
    filas = posicion.split('/')
    if len(filas) != 8:
        return "ERROR: El tablero debe tener 8 filas"
    
    for fila in filas:
        casillas_contadas = 0
        for caracter in fila:
            if caracter.isdigit():
                casillas_contadas += int(caracter)
            elif caracter.lower() in 'ptcadr':
                casillas_contadas += 1
            else:
                return f"ERROR: Carácter inválido '{caracter}' en el tablero"
        
        if casillas_contadas != 8:
            return "ERROR: Una fila no suma 8 casillas"

    # 2: Validación del turno
    if turno not in ['w', 'b']:
        return "ERROR: Turno inválido"

    # 3: Validación de enroques
    if not re.fullmatch(r'-|[RDrd]+', enroque):
        return "ERROR: Formato de enroque inválido"

    # 4: Validación de captura al paso
    if not re.fullmatch(r'-|[a-h][36]', al_paso):
        return "ERROR: Casilla 'al paso' inválida"

    # 5: Validación de contadores numéricos 
    if not (media_jugada.isdigit() and nro_jugada.isdigit()):
        return "ERROR: Los contadores deben ser números"

    return "CADENA FEN (ESPAÑOL) VÁLIDA"



# ERROR 1:
print(validar_fen("trcadcrt/pppppppp/8/8/8/9/PPPPPPPP/TRCADCRT w RDrd - 0 1"))

# ERROR 2:
print(validar_fen("trcadcrt/pppppppp/8/8/8/8/PPPPPPPP/TRCADCRT v RDrd - 0 1"))

