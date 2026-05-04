
import re

def analizar_expresion(cadena):
    patrones = [
        ('NUMERO',    r'\d+(\.\d+)?'),
        ('OPERANDO',  r'[a-zA-Z_][a-zA-Z0-9_]*'),
        ('OPERADOR',  r'[\+\-\*/]'),
        ('PAREN_IZQ', r'\('),
        ('PAREN_DER', r'\)'),
        ('ESPACIO',   r'\s+'), # Mi agregado
        ('ERROR',     r'.'),
    ]
    
    regex_principal = '|'.join(f'(?P<{nombre}>{patron})' for nombre, patron in patrones)
    
    componentes_encontrados = []
    parentesis = 0
    error = False
    
    # print(regex_principal + "\n")
    
    for match in re.finditer(regex_principal, cadena):
        tipo = match.lastgroup
        valor = match.group(tipo)

        if tipo == 'ESPACIO':
            continue
        
        if tipo == 'PAREN_IZQ':
            parentesis += 1
        elif tipo == 'PAREN_DER':
            parentesis -= 1
        
        if parentesis < 0:
            error = True
            
        componentes_encontrados.append(f"{tipo} {valor}")

    balance = "PARÉNTESIS BALANCEADOS" if parentesis == 0 and not error else "PARÉNTESIS NO BALANCEADOS"
    
    return " ".join(componentes_encontrados) + f" {balance}."

# EJEMPLO:
entrada = '12+3*(4)'
print(f"Salida: {analizar_expresion(entrada)}")

 