import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file not in instance.data:
        instance.enqueue(path_file)
    lines = txt_importer(path_file)
    return sys.stdout.writelines([
        f"'nome_do_arquivo': '{path_file}'",
        f"'qtd_linhas': {len(lines)}",
        f"'linhas_do_arquivo': {lines}",
    ])


def remove(instance):
    if instance.length == 0:
        return sys.stdout.write('Não há elementos\n')
    removed_file = instance.dequeue()
    return sys.stdout.write(f'Arquivo {removed_file} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        return process(file, instance)
    except IndexError:
        return sys.stderr.write('Posição inválida')
