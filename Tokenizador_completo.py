import re
import pandas as pd

PALAVRASCHAVE = { #palavras-chave que o analisador léxico entende
    "int": "KW_INT", 
    "if": "KW_IF", 
    "else": "KW_ELSE", 
    "while": "KW_WHILE", 
    "for": "KW_FOR", 
    "return": "KW_RETURN", 
    "void": "KW_VOID", 
    "char": "KW_CHAR", 
    "float": "KW_FLOAT", 
    "double": "KW_DOUBLE"
}

OPERADORES = { #operadores aritméticos e de atribuição
    "=": "SYM_EQUAL", 
    "+": "SYM_PLUS", 
    "-": "SYM_MINUS", 
    "*": "SYM_MULT", 
    "/": "SYM_DIV", 
    "%": "SYM_MOD"
    }

OPERADORES_RELACIONAIS = { #operadores relacionais
    ">": "SYM_GT", 
    "<": "SYM_LT", 
    ">=": "SYM_GTE", 
    "<=" : "SYM_LTE", 
    "==": "SYM_EQ", 
    "!=": "SYM_NEQ"
    }

SIMBOLOS_ESPECIAIS = { #símbolos especiais utilizados
    ";": "SYM_PV", 
    "{": "SYM_LBRACE", 
    "}": "SYM_RBRACE", 
    "(": "SYM_LPAREN", 
    ")": "SYM_RPAREN", 
    "[": "SYM_LBRACKET", 
    "]": "SYM_RBRACKET", 
    ",": "SYM_COMMA"
    }

#expressao regular para identificar tokens no código-fonte
REGEX = r"\b(?:" + "|".join(PALAVRASCHAVE.keys()) + r")\b|[a-zA-Z_][a-zA-Z0-9_]*|\d+|[=+\-*/%><!]=?|[{}();,\[\]]"

#Função para tokenizar um código-fonte
#Entrega uma lista de tokens identificados e um array formatado com os tokens
def tokenize(code):
    tokens = [] #array que armazenará os tokens identificados
    tokenized_array = [] #array formatada para exibição dos tokens
    token_id = 1 #id numérico dos tokens
    
    #encontra todos os tokens utilizando a expressão regular
    matches = re.findall(REGEX, code)
    
    #laço e condicionais que determina o tipo do token e seu valor associado
    for match in matches:
        if match in PALAVRASCHAVE:
            token_type = PALAVRASCHAVE[match]
            value = "-"
        elif match in OPERADORES:
            token_type = OPERADORES[match]
            value = "-"
        elif match in OPERADORES_RELACIONAIS:
            token_type = OPERADORES_RELACIONAIS[match]
            value = "-"
        elif match in SIMBOLOS_ESPECIAIS:
            token_type = SIMBOLOS_ESPECIAIS[match]
            value = "-"
        elif match.isdigit():
            token_type = "NUMBER"
            value = match
        else:
            token_type = "ID"
            value = "-"
        
        tokens.append((token_id, match, token_type, value)) #adiciona o token à lista de tokens
        tokenized_array.append(f"<{token_type}, {token_id}>") #adiciona o token formatado ao array tokenizado
        token_id += 1 #incrementa o identificador do token para continuar o laço
    
    return tokens, tokenized_array #retorna a lista de tokens e o array tokenizado

#codigo para análise léxica
code = """
int a = 134;
int b = 23;
if(b > 30)
    int c = b + a;
if(a > 100) {
    int c = a - b;
    int d = a * a + c;
}
"""

#tokeniza o código
tokens, tokenized_array = tokenize(code)

#cria um DataFrame para exibir a tabela de símbolos
df = pd.DataFrame(tokens, columns=["id", "lexema", "token", "valor"])
print(df) #imprimir tabela

#exibe a versão tokenizada do código
tokenized_output = " ".join(tokenized_array)
print("Código Tokenizado:", tokenized_output) #imprime o código tokenizado