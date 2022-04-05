import sys


def txt_importer(path_file):
    try:
        if path_file.split('.')[-1] != 'txt':
            return sys.stderr.write('Formato inválido\n')
        with open(path_file) as file:
            lines = []
            for line in file:
                lines.append(line.split('\n')[0])
            return lines
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
