import re
from ting_file_management.file_management import txt_importer

text_exists_word = [
    {
        "palavra": "pedro",
        "arquivo": "statics/nome_pedro.txt",
        "ocorrencias": [{"linha": 1}, {"linha": 3}],
    }
]


def exists_word(word, instance):
    appearances = []
    for file in instance.data:
        appearance = {
            'palavra': word,
            'arquivo': file,
            'ocorrencias': []
        }
        for index, line in enumerate(txt_importer(file)):
            words = re.split(r'\W+', line)
            lower_case_words = [line_word.lower() for line_word in words]
            print(lower_case_words)
            if word.lower() in lower_case_words:
                appearance['ocorrencias'].append({'linha': index + 1})
                print(appearance['ocorrencias'])
        if len(appearance['ocorrencias']) > 0:
            appearances.append(appearance)

    return appearances


def search_by_word(word, instance):
    appearances = []
    for file in instance.data:
        appearance = {
            'palavra': word,
            'arquivo': file,
            'ocorrencias': []
        }
        for index, line in enumerate(txt_importer(file)):
            words = re.split(r'\W+', line)
            lower_case_words = [line_word.lower() for line_word in words]
            print(lower_case_words)
            if word.lower() in lower_case_words:
                appearance['ocorrencias'].append({
                    'linha': index + 1,
                    'conteudo': line
                })
                print(appearance['ocorrencias'])
        if len(appearance['ocorrencias']) > 0:
            appearances.append(appearance)

    return appearances
