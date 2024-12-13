def hex_to_rgb(hex_color):
    """Convierte un color hexadecimal a RGB."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    """Convierte un color RGB a hexadecimal."""
    return f"#{''.join(f'{max(0, min(c, 255)):02X}' for c in rgb_color)}"  # Asegura rango 0-255

def mezclar_colores(pesos):
    """
    Mezcla los colores asociados a NEG, NEU, POS basado en los pesos.
    pesos: diccionario con probabilidades {'NEG': x, 'NEU': y, 'POS': z}
    """
    colores = {
        "NEG": "#2A0000",  # Muy negativo (oscuro)
        "NEU": "#800000",  # Neutral (intermedio)
        "POS": "#FF5E5E"   # Positivo (claro)
    }

    # Convertir colores a RGB
    colores_rgb = {k: hex_to_rgb(v) for k, v in colores.items()}

    # Mezclar los colores basado en los pesos
    color_resultante = [
        int(sum(colores_rgb[c][i] * pesos[c] for c in pesos)) for i in range(3)
    ]

    # Convertir el resultado a hexadecimal
    return rgb_to_hex(color_resultante)
