def notas(*nota, sit=False):
    '''
    -> Funcão para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionario com várias informações sobre a situação da turma
    '''
    r = {}
    r['total'] = len(nota)
    r['maior'] = max(nota)
    r['menor'] = min(nota)
    r['media'] = sum(nota)/len(nota)
    if sit:
        if r['media'] > 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 6.5, sit=True)
print(resp)
