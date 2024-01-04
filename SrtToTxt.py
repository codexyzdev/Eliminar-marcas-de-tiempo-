import re

def eliminar_marcas_de_tiempo(srt_file, txt_file):
    with open(srt_file, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    subtitles = []
    current_subtitle = ""

    for line in lines:
        # Buscar líneas que contengan marcas de tiempo (00:00:00,000 --> 00:00:00,000)
        if re.match(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', line):
            # Ignorar líneas de marcas de tiempo
            pass
        elif re.match(r'\d+', line):
            # Si la línea contiene solo números, probablemente sea un número de subtítulo
            # Agregar la línea actual a la lista de subtítulos
            subtitles.append(current_subtitle.strip())
            # Reiniciar la cadena de subtítulo actual
            current_subtitle = ""
        else:
            # Agregar líneas de texto al subtítulo actual
            current_subtitle += line

    # Agregar el último subtítulo
    subtitles.append(current_subtitle.strip())

    # Guardar los subtítulos en un archivo de texto
    with open(txt_file, 'w', encoding='utf-8') as output_file:
        for subtitle in subtitles:
            output_file.write(subtitle + '\n')

if __name__ == "__main__":
    # Reemplaza 'input.srt' y 'output.txt' con tus nombres de archivo deseados
    eliminar_marcas_de_tiempo('text.srt', 'text.txt')
