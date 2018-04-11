import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS','MENOR','MAYOR','DIFERENTE','MENORIGUAL','MAYORIGUAL' ]

reservadas = ['si']

t_ignore = ' \t\n'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_DIFERENTE = r'\!='
t_MENORIGUAL = r'\<='
t_MAYORIGUAL = r'\>='

algo = open("lexer.txt")
listaC = algo.readlines()

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer
for y in listaC:
    print y
    lex.input(y)
    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)
