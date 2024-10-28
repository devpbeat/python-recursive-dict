"""
Dado el siguiente diccionario, 
realiza una función recursiva para imprimir la estructura ordenada 
por indentación (cada indentación es de 4 espacios)
"""
complex_dict = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': {
                'f': {
                    'g': 3,
                    'h': 4
                },
                'i': 5
            },
            'j': 6
        }
    },
    'k': {
        'l': {
            'm': 7,
            'n': {
                'o': 8,
                'p': {
                    'q': 9
                }
            }
        }
    }
}

def print_ident_dictionary(dictionary, indent=0):
    for key, value in dictionary.items():
        print(" " * indent + str(key) + ":")
        if isinstance(value, dict):
            print_ident_dictionary(value, indent + 4)
        else:
            print(" " * (indent + 4) + str(value))

print_ident_dictionary(complex_dict)
