from collections import defaultdict
from Tokenizador_completo import tokenize

# ----------- DEFINIÇÃO DA GRAMÁTICA -----------
gramatica = {
    "P": [["D", "P"], []],
    "D": [["T", "ID", "SYM_EQUAL", "E", "SYM_PV"], ["KW_IF", "SYM_LPAREN", "C", "SYM_RPAREN", "B"]],
    "T": [["KW_INT"], ["KW_CHAR"]],
    "B": [["D"], ["SYM_LBRACE", "DL", "SYM_RBRACE"]],
    "DL": [["D", "DL"], []],
    "C": [["ID", "OPREL", "E"]],
    "E": [["T1", "E'"]],
    "E'": [["SYM_PLUS", "T1", "E'"], ["SYM_MINUS", "T1", "E'"], []],
    "T1": [["F", "T1'"]],
    "T1'": [["SYM_MULT", "F", "T1'"], ["SYM_DIV", "F", "T1'"], []],
    "F": [["ID"], ["NUMBER"]],
    "OPREL": [["SYM_GT"], ["SYM_LT"], ["SYM_GTE"], ["SYM_LTE"], ["SYM_EQ"], ["SYM_NEQ"]]
}

terminais = {"KW_INT", "KW_CHAR", "KW_IF", "SYM_LPAREN", "SYM_RPAREN", "SYM_EQUAL", "SYM_PLUS", "SYM_MINUS",
             "SYM_MULT", "SYM_DIV", "SYM_PV", "SYM_LBRACE", "SYM_RBRACE", "ID", "NUMBER",
             "SYM_GT", "SYM_LT", "SYM_GTE", "SYM_LTE", "SYM_EQ", "SYM_NEQ", "$"}

nao_terminais = list(gramatica.keys())

# ----------- CÁLCULO DO FIRST -----------
FIRST = defaultdict(set)

def calcula_first():
    mudanca = True
    while mudanca:
        mudanca = False
        for nt in gramatica:
            for producao in gramatica[nt]:
                i = 0
                while i < len(producao):
                    simbolo = producao[i]
                    if simbolo in terminais:
                        if simbolo not in FIRST[nt]:
                            FIRST[nt].add(simbolo)
                            mudanca = True
                        break
                    else:
                        antes = len(FIRST[nt])
                        FIRST[nt].update(FIRST[simbolo] - {''})
                        if '' not in FIRST[simbolo]:
                            break
                        i += 1
                        if i == len(producao):
                            FIRST[nt].add('')
                        mudanca = mudanca or len(FIRST[nt]) > antes
                if not producao:
                    if '' not in FIRST[nt]:
                        FIRST[nt].add('')
                        mudanca = True

# ----------- CÁLCULO DO FOLLOW -----------
FOLLOW = defaultdict(set)
FOLLOW['P'].add('$')

def calcula_follow():
    mudanca = True
    while mudanca:
        mudanca = False
        for A in gramatica:
            for producao in gramatica[A]:
                for i, B in enumerate(producao):
                    if B in nao_terminais:
                        beta = producao[i+1:]
                        first_beta = set()
                        if not beta:
                            first_beta.add('')
                        else:
                            j = 0
                            while j < len(beta):
                                s = beta[j]
                                if s in terminais:
                                    first_beta.add(s)
                                    break
                                else:
                                    first_beta.update(FIRST[s] - {''})
                                    if '' in FIRST[s]:
                                        j += 1
                                        if j == len(beta):
                                            first_beta.add('')
                                    else:
                                        break
                        antes = len(FOLLOW[B])
                        FOLLOW[B].update(first_beta - {''})
                        if '' in first_beta:
                            FOLLOW[B].update(FOLLOW[A])
                        mudanca = mudanca or len(FOLLOW[B]) > antes

# ----------- TABELA M -----------
tabela_m = defaultdict(dict)

def gera_tabela_m():
    for nt in gramatica:
        for producao in gramatica[nt]:
            first = set()
            if producao:
                i = 0
                while i < len(producao):
                    simb = producao[i]
                    if simb in terminais:
                        first = {simb}
                        break
                    else:
                        first.update(FIRST[simb] - {''})
                        if '' in FIRST[simb]:
                            i += 1
                        else:
                            break
                else:
                    first.add('')
            else:
                first.add('')

            for t in first:
                if t != '':
                    tabela_m[nt][t] = producao
            if '' in first:
                for f in FOLLOW[nt]:
                    tabela_m[nt][f] = producao

# ----------- ANALISADOR SINTÁTICO DESCENDENTE -----------
def parser(tokens):
    pilha = ['$', 'P']
    entrada = [token[2] for token in tokens] + ['$']
    i = 0

    while pilha:
        topo = pilha.pop()
        atual = entrada[i]

        if topo == atual == '$':
            print("✓ Código aceito pela linguagem!")
            return True
        elif topo in terminais:
            if topo == atual:
                i += 1
            else:
                print(f"Erro: esperava '{topo}' mas encontrou '{atual}'")
                return False
        elif topo in nao_terminais:
            producao = tabela_m.get(topo, {}).get(atual)
            if producao is not None:
                for simbolo in reversed(producao):
                    if simbolo != '':
                        pilha.append(simbolo)
            else:
                print(f"Erro de sintaxe próximo de '{atual}'")
                return False
        else:
            print(f"Símbolo inválido na pilha: '{topo}'")
            return False

    return False

# ----------- EXECUÇÃO -----------
if __name__ == "__main__":
    code = '''
    int a = 134;
    int b = 23;
    if(b > 30)
        int c = b + a;
    if(a > 100) {
        int c = a - b;
        int d = a * a + c;
    }
    '''

    tokens, _ = tokenize(code)

    calcula_first()
    calcula_follow()
    gera_tabela_m()

    print("FIRST:")
    for nt in nao_terminais:
        print(f"FIRST({nt}) = {FIRST[nt]}")

    print("\nFOLLOW:")
    for nt in nao_terminais:
        print(f"FOLLOW({nt}) = {FOLLOW[nt]}")

    print("\n--- Analisando código ---")
    parser(tokens)
