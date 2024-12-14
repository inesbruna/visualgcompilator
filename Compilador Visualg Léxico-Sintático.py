import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import filedialog as fd
import webbrowser
import sys


# --------------------------------------------------------------------------
# ---------------------------- Transição Léxica ----------------------------

transicao_lexico = {
     'q0': {'A': 'qf1',
             'B': 'qf1',
             'C': 'qf1',
             'D': 'qf1',
             'E': 'qf1',
             'F': 'qf1',
             'G': 'qf1',
             'H': 'qf1',
             'I': 'qf1',
             'J': 'qf1',
             'K': 'qf1',
             'L': 'qf1',
             'M': 'qf1',
             'N': 'qf1',
             'O': 'qf1',
             'P': 'qf1',
             'Q': 'qf1',
             'R': 'qf1',
             'S': 'qf1',
             'T': 'qf1',
             'U': 'qf1',
             'V': 'qf1',
             'W': 'qf1',
             'X': 'qf1',
             'Y': 'qf1',
             'Z': 'qf1',
             'a': 'qf1',
             'b': 'qf1',
             'c': 'qf1',
             'd': 'qf1',
             'e': 'qf1',
             'f': 'qf1',
             'g': 'qf1',
             'h': 'qf1',
             'i': 'qf1',
             'j': 'qf1',
             'k': 'qf1',
             'l': 'qf1',
             'm': 'qf1',
             'n': 'qf1',
             'o': 'qf1',
             'p': 'qf1',
             'q': 'qf1',
             'r': 'qf1',
             's': 'qf1',
             't': 'qf1',
             'u': 'qf1',
             'v': 'qf1',
             'w': 'qf1',
             'x': 'qf1',
             'y': 'qf1',
             'z': 'qf1',
             '_': 'qf1',
             '0': 'qf3',
             '1': 'qf3',
             '2': 'qf3',
             '3': 'qf3',
             '4': 'qf3',
             '5': 'qf3',
             '6': 'qf3',
             '7': 'qf3',
             '8': 'qf3',
             '9': 'qf3',
             '-': 'qf5',
             '.': 'q2',
             '=': 'qf12',
             '*': 'qf12',
             '/': 'qf12',
             '%': 'qf12',
             '>': 'qf7',
             '<': 'qf6',
             '+': 'qf12',
             ',': 'qf12',
             ';': 'qf12',
             '(': 'qf12',
             ')': 'qf12',
             '{': 'qf12',
             '}': 'qf12',
             '[': 'qf12',
             ']': 'qf12',
             ':': 'qf12',
             '^': 'qf12',
             '"': 'q9'},
      'q1': {'0': 'qf4',
             '1': 'qf4',
             '2': 'qf4',
             '3': 'qf4',
             '4': 'qf4',
             '5': 'qf4',
             '6': 'qf4',
             '7': 'qf4',
             '8': 'qf4',
             '9': 'qf4'},
      'q2': {'.': 'qf12'},
      'qf1': {'A': 'qf1',
              'B': 'qf1',
              'C': 'qf1',
              'D': 'qf1',
              'E': 'qf1',
              'F': 'qf1',
              'G': 'qf1',
              'H': 'qf1',
              'I': 'qf1',
              'J': 'qf1',
              'K': 'qf1',
              'L': 'qf1',
              'M': 'qf1',
              'N': 'qf1',
              'O': 'qf1',
              'P': 'qf1',
              'Q': 'qf1',
              'R': 'qf1',
              'S': 'qf1',
              'T': 'qf1',
              'U': 'qf1',
              'V': 'qf1',
              'W': 'qf1',
              'X': 'qf1',
              'Y': 'qf1',
              'Z': 'qf1',
              'a': 'qf1',
              'b': 'qf1',
              'c': 'qf1',
              'd': 'qf1',
              'e': 'qf1',
              'f': 'qf1',
              'g': 'qf1',
              'h': 'qf1',
              'i': 'qf1',
              'j': 'qf1',
              'k': 'qf1',
              'l': 'qf1',
              'm': 'qf1',
              'n': 'qf1',
              'o': 'qf1',
              'p': 'qf1',
              'q': 'qf1',
              'r': 'qf1',
              's': 'qf1',
              't': 'qf1',
              'u': 'qf1',
              'v': 'qf1',
              'w': 'qf1',
              'x': 'qf1',
              'y': 'qf1',
              'z': 'qf1',
              '0': 'qf1',
              '1': 'qf1',
              '2': 'qf1',
              '3': 'qf1',
              '4': 'qf1',
              '5': 'qf1',
              '6': 'qf1',
              '7': 'qf1',
              '8': 'qf1',
              '9': 'qf1',
              '_': 'qf1'},
      'qf3': {'0': 'qf3',
             '1': 'qf3',
             '2': 'qf3',
             '3': 'qf3',
             '4': 'qf3',
             '5': 'qf3',
             '6': 'qf3',
             '7': 'qf3',
             '8': 'qf3',
             '9': 'qf3',
             '.': 'q1'},
      'qf4': {'0': 'qf4',
              '1': 'qf4',
              '2': 'qf4',
              '3': 'qf4',
              '4': 'qf4',
              '5': 'qf4',
              '6': 'qf4',
              '7': 'qf4',
              '8': 'qf4',
              '9': 'qf4'},
      'qf5': {'0': 'qf3',
              '1': 'qf3',
              '2': 'qf3',
              '3': 'qf3',
              '4': 'qf3',
              '5': 'qf3',
              '6': 'qf3',
              '7': 'qf3',
              '8': 'qf3',
              '9': 'qf3'},
      'qf6': {'-': 'qf12',
              '=': 'qf12',
              '>': 'qf12'},
      'qf7': {'=': 'qf12'},
      'q9': {'A': 'q11', 'B': 'q11', 'C': 'q11', 'D': 'q11', 'E': 'q11', 'F': 'q11', 'G': 'q11', 'H': 'q11', 'I': 'q11', 'J': 'q11', 'K': 'q11', 'L': 'q11', 'M': 'q11', 'N': 'q11',
           'O': 'q11', 'P': 'q11', 'Q': 'q11', 'R': 'q11', 'S': 'q11', 'T': 'q11', 'U': 'q11', 'V': 'q11', 'W': 'q11', 'X': 'q11', 'Y': 'q11', 'Z': 'q11', 'a': 'q11', 'b': 'q11',
           'c': 'q11', 'd': 'q11', 'e': 'q11', 'f': 'q11', 'g': 'q11', 'h': 'q11', 'i': 'q11', 'j': 'q11', 'k': 'q11', 'l': 'q11', 'm': 'q11', 'n': 'q11', 'o': 'q11', 'p': 'q11',
           'q': 'q11', 'r': 'q11', 's': 'q11', 't': 'q11', 'u': 'q11', 'v': 'q11', 'w': 'q11', 'x': 'q11', 'y': 'q11', 'z': 'q11', '0': 'q10', '1': 'q10', '2': 'q10', '3': 'q10',
           '4': 'q10', '5': 'q10', '6': 'q10', '7': 'q10', '8': 'q10', '9': 'q10', '_': 'q11', '-': 'q10', '.': 'q10', '=': 'q10', '*': 'q10', '/': 'q10', '%': 'q10', '>': 'q10',
           '<': 'q10', '+': 'q10', ',': 'q10', ';': 'q10', '(': 'q10', ')': 'q10', '{': 'q10', '}': 'q10', '[': 'q10', ']': 'q10', ':': 'q10', '^': 'q10', '`': 'q10', '´': 'q10',
           '§': 'q10', 'º': 'q10', '|': 'q10', '\\': 'q10', 'ª': 'q10', '°': 'q10', '&': 'q10', 'ç': 'q10', '#': 'q10', '!': 'q10', '@': 'q10', 'Ç': 'q10', '¹': 'q10', '²': 'q10',
           '³': 'q10', '¬': 'q10', '£': 'q10', '¢': 'q10', '$': 'q10', "'": 'q10', '¨': 'q10', '?': 'q10', '~': 'q10',
           'á':'q10', 'é':'q10', 'í':'q10', 'ó':'q10', 'ú':'q10',
           'Á':'q10', 'É':'q10', 'Í':'q10', 'Ó':'q10', 'Ú':'q10',
           'à':'q10', 'è':'q10', 'ì':'q10', 'ò':'q10', 'ù':'q10',
           'À':'q10', 'È':'q10', 'Ì':'q10', 'Ò':'q10', 'Ù':'q10',
           'Â':'q10', 'Ê':'q10', 'Î':'q10', 'Ô':'q10', 'Û':'q10',
           'â':'q10', 'ê':'q10', 'î':'q10', 'ô':'q10', 'û':'q10',
           'ä':'q10', 'ë':'q10', 'ï':'q10', 'ö':'q10', 'ü':'q10',
           'Ä':'q10', 'Ë':'q10', 'Ï':'q10', 'Ö':'q10', 'Ü':'q10',
           'Ã':'q10', 'ã':'q10', 'Õ':'q10', 'õ':'q10',
           '"': 'qf13'},
      'q10': {'A': 'q10', 'B': 'q10', 'C': 'q10', 'D': 'q10', 'E': 'q10', 'F': 'q10', 'G': 'q10', 'H': 'q10', 'I': 'q10', 'J': 'q10',
            'K': 'q10', 'L': 'q10', 'M': 'q10', 'N': 'q10',
            'O': 'q10', 'P': 'q10', 'Q': 'q10', 'R': 'q10', 'S': 'q10', 'T': 'q10', 'U': 'q10',
            'V': 'q10', 'W': 'q10', 'X': 'q10', 'Y': 'q10', 'Z': 'q10', 'a': 'q10', 'b': 'q10', 'c': 'q10', 'd': 'q10',
            'e': 'q10', 'f': 'q10', 'g': 'q10', 'h': 'q10', 'i': 'q10', 'j': 'q10', 'k': 'q10', 'l': 'q10', 'm': 'q10', 'n': 'q10', 'o': 'q10',
            'p': 'q10', 'q': 'q10', 'r': 'q10', 's': 'q10', 't': 'q10', 'u': 'q10', 'v': 'q10', 'w': 'q10', 'x': 'q10', 'y': 'q10', 'z': 'q10',
            '0': 'q10', '1': 'q10', '2': 'q10', '3': 'q10', '4': 'q10', '5': 'q10', '6': 'q10', '7': 'q10', '8': 'q10', '9': 'q10', '_': 'q10',
            '-': 'q10', '.': 'q10', '=': 'q10', '*': 'q10', '/': 'q10', '%': 'q10', '>': 'q10', '<': 'q10', '+': 'q10', ',': 'q10', ';': 'q10',
            '(': 'q10', ')': 'q10', '{': 'q10', '}': 'q10', '[': 'q10', ']': 'q10', ':': 'q10', '^': 'q10', '`': 'q10', '´': 'q10', '§': 'q10', 'º': 'q10',
            '|': 'q10', '\\': 'q10', 'ª': 'q10', '°': 'q10', '&': 'q10', 'ç': 'q10', '#': 'q10', '!': 'q10', '@': 'q10', 'Ç': 'q10', '¹': 'q10', '²': 'q10',
            '³': 'q10', '¬': 'q10', '£': 'q10', '¢': 'q10', '$': 'q10', "'": 'q10', '¨': 'q10', '?': 'q10', '~': 'q10',
            'á':'q10', 'é':'q10', 'í':'q10', 'ó':'q10', 'ú':'q10',
            'Á':'q10', 'É':'q10', 'Í':'q10', 'Ó':'q10', 'Ú':'q10',
            'à':'q10', 'è':'q10', 'ì':'q10', 'ò':'q10', 'ù':'q10',
            'À':'q10', 'È':'q10', 'Ì':'q10', 'Ò':'q10', 'Ù':'q10',
            'Â':'q10', 'Ê':'q10', 'Î':'q10', 'Ô':'q10', 'Û':'q10',
            'â':'q10', 'ê':'q10', 'î':'q10', 'ô':'q10', 'û':'q10',
            'ä':'q10', 'ë':'q10', 'ï':'q10', 'ö':'q10', 'ü':'q10',
            'Ä':'q10', 'Ë':'q10', 'Ï':'q10', 'Ö':'q10', 'Ü':'q10',
            'Ã':'q10', 'ã':'q10', 'Õ':'q10', 'õ':'q10', '"': 'qf13'},
     'q11': {'A': 'q11', 'B': 'q11', 'C': 'q11', 'D': 'q11', 'E': 'q11', 'F': 'q11', 'G': 'q11', 'H': 'q11', 'I': 'q11', 'J': 'q11',
            'K': 'q11', 'L': 'q11', 'M': 'q11', 'N': 'q11', 'O': 'q11', 'P': 'q11', 'Q': 'q11', 'R': 'q11', 'S': 'q11',
            'T': 'q11', 'U': 'q11', 'V': 'q11', 'W': 'q11', 'X': 'q11', 'Y': 'q11', 'Z': 'q11', 'a': 'q11', 'b': 'q11',
            'c': 'q11', 'd': 'q11', 'e': 'q11', 'f': 'q11', 'g': 'q11', 'h': 'q11', 'i': 'q11', 'j': 'q11', 'k': 'q11',
            'l': 'q11', 'm': 'q11', 'n': 'q11', 'o': 'q11', 'p': 'q11', 'q': 'q11', 'r': 'q11', 's': 'q11', 't': 'q11',
            'u': 'q11', 'v': 'q11', 'w': 'q11', 'x': 'q11', 'y': 'q11', 'z': 'q11', '0': 'q11', '1': 'q11', '2': 'q11',
            '3': 'q11', '4': 'q11', '5': 'q11', '6': 'q11', '7': 'q11', '8': 'q11', '9': 'q11', '_': 'q11', '-': 'q11',
            '.': 'q11', '=': 'q11', '*': 'q11', '/': 'q11', '%': 'q11', '>': 'q11', '<': 'q11', '+': 'q11', ',': 'q11',
            ';': 'q11', '(': 'q11', ')': 'q11', '{': 'q11', '}': 'q11', '[': 'q11', ']': 'q11', ':': 'q11', '^': 'q11',
            '`': 'q11', '´': 'q11', '§': 'q11', 'º': 'q11', '|': 'q11', '\\': 'q11', 'ª': 'q11', '°': 'q11', '&': 'q11',
            'ç': 'q11', '#': 'q11', '!': 'q11', '@': 'q11', 'Ç': 'q11', '¹': 'q11', '²': 'q11', '³': 'q11', '¬': 'q11', '£': 'q11', '¢': 'q11', '$': 'q11',
            "'": 'q11', '¨': 'q11', '?': 'q11', '~': 'q11',
            'á':'q11', 'é':'q11', 'í':'q11', 'ó':'q11', 'ú':'q11',
            'Á':'q11', 'É':'q11', 'Í':'q11', 'Ó':'q11', 'Ú':'q11',
            'à':'q11', 'è':'q11', 'ì':'q11', 'ò':'q11', 'ù':'q11',
            'À':'q11', 'È':'q11', 'Ì':'q11', 'Ò':'q11', 'Ù':'q11',
            'Â':'q11', 'Ê':'q11', 'Î':'q11', 'Ô':'q11', 'Û':'q11',
            'â':'q11', 'ê':'q11', 'î':'q11', 'ô':'q11', 'û':'q11',
            'ä':'q11', 'ë':'q11', 'ï':'q11', 'ö':'q11', 'ü':'q11',
            'Ä':'q11', 'Ë':'q11', 'Ï':'q11', 'Ö':'q11', 'Ü':'q11',
            'Ã':'q11', 'ã':'q11', 'Õ':'q11', 'õ':'q11', '"':'qf14'} 
    
     
}  # Fecha dicionário

# -------------------------------------------------------------------
# ------------------------ Palavras reservadas ----------------------

reservadas = [
    'algoritmo', 'inicio',
    'fimalgoritmo', 'var',
    'inteiro', 'real', 'caractere',
    'logico', 'escreva', 'escreval', 'leia',
    'para', 'fimpara', 'faca', 'enquanto',
    'fimenquanto', 'repita', 'ate', 'interrompa',
    'fimrepita', 'de', 'passo', 'se', 'entao', 'fimse', 'senao',
    'escolha', 'caso', 'outrocaso', 'fimescolha',
    'e', 'ou', 'nao', 'VERDADEIRO', 'FALSO', 'xou', 'abs',
    'exp', 'quad', 'raizq', 'randi', 'funcao', 'fimfuncao',
    'procedimento', 'fimprocedimento', 'retorne', 'MOD',
    'vetor'
]

# Definição Léxico

def lexico(lista):
    tabela_simbolos = []
    for palavra in lista:
        estado = 'q0'
        try:
            for letra in palavra:
                estado = transicao_lexico[estado][letra]
            if not estado.startswith('qf'):
                messagebox.showerror("Erro", f'Erro na palavra: {palavra}')
                return None
        except:
            messagebox.showerror("Erro", f'Erro na palavra: {palavra}')
            return None

        if (estado == 'qf1'):
            if (palavra in reservadas):
                tabela_simbolos.append([palavra, palavra.upper()])
            else:
                tabela_simbolos.append([palavra, 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO'])
        elif (estado == 'qf3'):
            tabela_simbolos.append([palavra, 'VALOR_INT'])
        elif (estado == 'qf4'):
            tabela_simbolos.append([palavra, 'VALOR_REAL'])
        elif (estado == 'qf5'):
            tabela_simbolos.append([palavra, 'OP_ARIT'])
        elif (estado == 'qf6'):
            tabela_simbolos.append([palavra, 'OP_REL'])
        elif (estado == 'qf7'):
            tabela_simbolos.append([palavra, 'OP_REL'])
        elif (estado == 'qf12'):
            if (palavra == '<-'):
                tabela_simbolos.append([palavra, 'OP_ATRIB'])
            elif (palavra == ':'):
                tabela_simbolos.append([palavra, 'OP_DELIMITACAO'])
            elif (palavra == '('):
                tabela_simbolos.append([palavra, 'ABRE_PARENTESES'])
            elif (palavra == ')'):
                tabela_simbolos.append([palavra, 'FECHA_PARENTESES'])
            elif (palavra == '{'):
                tabela_simbolos.append([palavra, 'ABRE_CHAVE'])
            elif (palavra == '}'):
                tabela_simbolos.append([palavra, 'FECHA_CHAVE'])
            elif (palavra == '['):
                tabela_simbolos.append([palavra, 'ABRE_COLCHETE'])
            elif (palavra == ']'):
                tabela_simbolos.append([palavra, 'FECHA_COLCHETE'])
            elif (palavra in ['=', '>=', '<=', '<>']):
                tabela_simbolos.append([palavra, 'OP_REL'])
            elif (palavra == '='):
                tabela_simbolos.append([palavra, 'ASPAS'])
            elif (palavra == ','):
                tabela_simbolos.append([palavra, 'OP_SEP_MESMO_TIPO'])
            elif (palavra == ';'):
                tabela_simbolos.append([palavra, 'OP_SEP_DIFERENTE_TIPO'])
            elif (palavra == '..'):
                tabela_simbolos.append([palavra, 'OP_DIMENSAO_VETOR'])
            elif (palavra == '+'):
                tabela_simbolos.append([palavra, 'OP_ARIT/OP_CARACTERE'])
            else:
                tabela_simbolos.append([palavra, 'OP_ARIT'])
        elif (estado == 'qf13'):
            tabela_simbolos.append([palavra, 'VALOR_LITERAL'])
        elif (estado == 'qf14'):
            tabela_simbolos.append([palavra, 'NOME_ALGORITMO/VALOR_LITERAL'])
    return tabela_simbolos

# ----------------------------------------------------------
# ------------------ Transição Sintático -------------------

transicao_sintatico = {
    'ALGORITMO': {
        'S': ['NOME_ALGORITMO/VALOR_LITERAL', 'INICIAR', 'COMANDOS']
    },

    'INICIO': {
        'INICIAR': []
    },

    # FUNCAO

    'FUNCAO': {
        'S': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FUNCAO_INICIAR', 'TIPO_DADO', 'INICIAR', 'FUNCAO_COMANDOS']
    },

    'FIMFUNCAO': {
        'FUNCAO_COMANDOS': ['S'],
        'FUNCAO_MAISEXPRESSAO': ['S']
    },

    # PROCEDIMENTO

    'PROCEDIMENTO': {
        'S': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'PROCEDIMENTO_INICIAR', 'INICIAR', 'PROCEDIMENTO_COMANDOS']
    },

    'FIMPROCEDIMENTO': {
        'PROCEDIMENTO_COMANDOS': ['S'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['S']
    },

    'VAR': {
        'INICIAR': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'COMPLEMENTAR', 'TIPO_DADO', 'INICIAR'],
        'PROCEDIMENTO_INICIAR': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'COMPLEMENTAR', 'TIPO_DADO'],
    },

    'OP_DELIMITACAO': {
        'OP_DELIMITACAO': [],
        'FUNCAO_INICIAR': [],
        'MAISPARAMETROS': ['TIPO_DADO'],
        'COMPLEMENTAR': []
    },

    'OP_SEP_MESMO_TIPO': {
        'COMPLEMENTAR': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'COMPLEMENTAR'], 
        'COMPLEMENTAR2': ['VALOR_INT', 'OP_DIMENSAO_VETOR', 'VALOR_INT', 'FECHA_COLCHETE'],
        'ESCOLHA_COMANDOS': ['VALOR_ESCOLHA', 'ESCOLHA_COMANDOS'],
        'MAISESCRITA': ['ESCRITA'],
        'ALGO_TALVEZ': ['ESCRITA'],
        
        
        'OP_SEP_MESMO_TIPO': [],
        'MAISPARAMETROS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'MAISPARAMETROS'],
        #Provavelmente tem que derivar vazio para passar para a continuação do próximo parâmetro
        'MAISEXPRESSAO_FUNCAO2PARAMETRO': [],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_PARA': [],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITA': [],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO': [],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE': [],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': [],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': [],

        'POSSIVEL_CONTINUE':['VALOR_INT', 'FECHA_COLCHETE'],
        'POSSIVEL_CONTINUE_COLCHETE_ESCRITA':['VALOR_INT', 'FECHA_COLCHETE_ESCRITA']
    },

    'OP_REL': { 
        'OP_REL': ['OPERANDO'],
        'ATE_REL': ['ATE_OPERANDO'],
        'ATE_PARENTESES_REL': ['ATE_PARENTESES_OPERANDO']
    },

    'VETOR': {
        'TIPO_DADO': ['LIMITADOR']
    },

    'INTEIRO': {
        'TIPO_DADO': [], 
        'TIPO_DADO_BASICO': []
    },

    'REAL': {
        'TIPO_DADO': [], 
        'TIPO_DADO_BASICO': []
    },

    'CARACTERE': {
        'TIPO_DADO': [], 
        'TIPO_DADO_BASICO': []
    },

    'LOGICO': {
        'TIPO_DADO': [], 
        'TIPO_DADO_BASICO': []
    },

    'ABRE_COLCHETE': {
        'LIMITADOR': ['VALOR_INT', 'OP_DIMENSAO_VETOR', 'VALOR_INT', 'COMPLEMENTAR2', 'DE', 'TIPO_DADO_BASICO'],
        'OP_ATRIB': ['VALOR_INT','POSSIVEL_CONTINUE', 'OP_ATRIB3'],
        'ALGO_TALVEZ': ['VALOR_INT', 'POSSIVEL_CONTINUE_COLCHETE_ESCRITA']

        #Só não pode isso, por causa da existência de funções
        #'MAISEXPRESSAO': ['VALOR_INT','FECHA_COLCHETE', 'MAISEXPRESSAO']    
    },

    'OP_SEP_DIFERENTE_TIPO': {
        'OP_SEP_DIFERENTE_TIPO': [],
        'MAISFUNCAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'MAISPARAMETROS', 'MAISFUNCAO'],
        'MAISPROCEDIMENTO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'MAISPARAMETROS', 'MAISPROCEDIMENTO']
    },

    'FECHA_COLCHETE': {
        'COMPLEMENTAR2': [], 
        'FECHA_COLCHETE': [],
        'POSSIVEL_CONTINUE':[],
        'POSSIVEL_CONTINUE_COLCHETE_ESCRITA':['MAISESCRITA'],
        'FECHA_COLCHETE_ESCRITA':['MAISESCRITA']
    },

    'OP_DIMENSAO_VETOR': {
        'OP_DIMENSAO_VETOR': []
    },

    'DE': {
        'DE': []
    },

    # ABS
    'ABS':{ 
        'EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO'],
        'PARENTESES': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','PARENTESES', 'FECHANDO_PARENTESES_FUNCAO1PARAMETRO'],
        'EXPRESSAO_FUNCAO1PARAMETRO': ['PARENTESES', 'MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': [ 'PARENTESES', 'ENQUANTO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PARA': [ 'PARENTESES', 'PARA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITA': [ 'PARENTESES', 'REPITA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['PARENTESES', 'SENAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': ['PARENTESES', 'SE_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': [ 'PARENTESES', 'ESCOLHA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': [ 'PARENTESES', 'OUTROCASO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['PARENTESES', 'FUNCAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['PARENTESES', 'PROCEDIMENTO_MAISEXPRESSAO'],
        
        'EXPRESSAO_FUNCAO2PARAMETRO': ['PARENTESES', 'MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ 'PARENTESES', 'ENQUANTO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ 'PARENTESES', 'PARA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ 'PARENTESES', 'REPITA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['PARENTESES', 'SENAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': ['PARENTESES', 'SE_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [ 'PARENTESES', 'ESCOLHA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'PARENTESES', 'OUTROCASO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['PARENTESES', 'FUNCAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['PARENTESES', 'PROCEDIMENTO_MAISEXPRESSAO'],

 
        'ENQUANTO_EXPRESSAO' : ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'PARA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'REPITA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'SENAO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'SE_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'ESCOLHA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'OUTROCASO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'FUNCAO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'PROCEDIMENTO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO']
    },

    #QUAD
    'QUAD':{ 
        'EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO'],
        'PARENTESES': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','PARENTESES','FECHANDO_PARENTESES_FUNCAO1PARAMETRO'],
        'EXPRESSAO_FUNCAO1PARAMETRO': ['PARENTESES', 'MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': [ 'PARENTESES', 'ENQUANTO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PARA': [ 'PARENTESES', 'PARA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITA': [ 'PARENTESES', 'REPITA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['PARENTESES', 'SENAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': ['PARENTESES', 'SE_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': [ 'PARENTESES', 'ESCOLHA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': [ 'PARENTESES', 'OUTROCASO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['PARENTESES', 'FUNCAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['PARENTESES', 'PROCEDIMENTO_MAISEXPRESSAO'],


                
        'EXPRESSAO_FUNCAO2PARAMETRO': ['PARENTESES', 'MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ 'PARENTESES', 'ENQUANTO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ 'PARENTESES', 'PARA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ 'PARENTESES', 'REPITA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['PARENTESES', 'SENAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': ['PARENTESES', 'SE_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [ 'PARENTESES', 'ESCOLHA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'PARENTESES', 'OUTROCASO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['PARENTESES', 'FUNCAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['PARENTESES', 'PROCEDIMENTO_MAISEXPRESSAO'],
        
        'ENQUANTO_EXPRESSAO' : ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'PARA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'REPITA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'SENAO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'SE_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'ESCOLHA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'OUTROCASO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'FUNCAO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'PROCEDIMENTO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO']
    },

    #RAIZQ
    'RAIZQ':{ 
        'EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO'],
        'PARENTESES': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO', 'PARENTESES', 'FECHANDO_PARENTESES_FUNCAO1PARAMETRO'],
        'EXPRESSAO_FUNCAO1PARAMETRO': ['PARENTESES', 'MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': [ 'PARENTESES', 'ENQUANTO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PARA': [ 'PARENTESES', 'PARA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITA': [ 'PARENTESES', 'REPITA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['PARENTESES', 'SENAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': ['PARENTESES', 'SE_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': [ 'PARENTESES', 'ESCOLHA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': [ 'PARENTESES', 'OUTROCASO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['PARENTESES', 'FUNCAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['PARENTESES', 'PROCEDIMENTO_MAISEXPRESSAO'],

        
        'EXPRESSAO_FUNCAO2PARAMETRO': ['PARENTESES', 'MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ 'PARENTESES', 'ENQUANTO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ 'PARENTESES', 'PARA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ 'PARENTESES', 'REPITA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['PARENTESES', 'SENAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': ['PARENTESES', 'SE_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [ 'PARENTESES', 'ESCOLHA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'PARENTESES', 'OUTROCASO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['PARENTESES', 'FUNCAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['PARENTESES', 'PROCEDIMENTO_MAISEXPRESSAO'],

        
        'ENQUANTO_EXPRESSAO' : ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'PARA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'REPITA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'SENAO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'SE_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'ESCOLHA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'OUTROCASO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'FUNCAO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'PROCEDIMENTO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],
    },

              


    #EXP
    #1PARAMETRO significa que faltará 1 parametro para encerrar a função, função com total de 2
    #'ABRINDO_PARENTESES_FUNCAO1PARAMETRO' pode ser reutilizado, já que é um parenteses "normal"
  
   
    'EXP':{ 
        'EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO', 'EXPRESSAO_FUNCAO1PARAMETRO' ],
        #'PARENTESES': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO', 'PARENTESES', 'FECHANDO_PARENTESES_FUNCAO1PARAMETRO'],
        'PARENTESES': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO', 'EXPRESSAO_FUNCAO2PARAMETRO', 'PARENTESES', 'FECHANDO_PARENTESES_FUNCAO1PARAMETRO'],
        'EXPRESSAO_FUNCAO1PARAMETRO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO', 'PARENTESES', 'FECHA_PARENTESES_ANTERIOR', 'MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO', 'EXPRESSAO_FUNCAO1PARAMETRO', 'FECHA_PARENTESES_ANTERIOR' ],    
        'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO', 'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PARA': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_PARA', 'EXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITA': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_REPITA', 'EXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_SENAO', 'EXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_SE', 'EXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA', 'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO', 'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO', 'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO', 'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],

        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO', 'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_PARA', 'EXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_REPITA', 'EXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_SENAO', 'EXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_SE', 'EXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA', 'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO', 'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO', 'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO', 'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],
              
        'ENQUANTO_EXPRESSAO' : ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO', 'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'PARA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_PARA', 'EXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'REPITA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_REPITA', 'EXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'SENAO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_SENAO', 'EXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'SE_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_SE', 'EXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'ESCOLHA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA', 'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'OUTROCASO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO', 'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'FUNCAO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO', 'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'PROCEDIMENTO_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO', 'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO']
    },

    #RANDI
    'RANDI':{ 
        'EXPRESSAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHAR_PARENTESES_RANDI'],
        'PARENTESES':['ABRIR_PARENTESES_RANDI','VALOR_INTEIRO/VARIAVEL', 'FECHAR_PARENTESES_RANDI_SITUACAO2'],
        'ENQUANTO_EXPRESSAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHAR_PARENTESES_RANDI_ENQUANTO'],
        'PARA_EXPRESSAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHAR_PARENTESES_RANDI_PARA'],
        'REPITA_EXPRESSAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHAR_PARENTESES_RANDI_REPITA'],
        'SENAO_EXPRESSAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHAR_PARENTESES_RANDI_SENAO'],
        'SE_EXPRESSAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHAR_PARENTESES_RANDI_SE'],
        'ESCOLHA_EXPRESSAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHAR_PARENTESES_RANDI_ESCOLHA'],
        'OUTROCASO_EXPRESSAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHAR_PARENTESES_RANDI_OUTROCASO'],
        'FUNCAO_EXPRESSAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHAR_PARENTESES_RANDI_FUNCAO'],
        'PROCEDIMENTO_EXPRESSAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHAR_PARENTESES_RANDI_PROCEDIMENTO'],

        'EXPRESSAO_FUNCAO1PARAMETRO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_ENQUANTO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PARA': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_PARA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITA': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_REPITA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_SENAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_SE'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_ESCOLHA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_OUTROCASO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_FUNCAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_PROCEDIMENTO'],

        'EXPRESSAO_FUNCAO2PARAMETRO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_ENQUANTO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_PARA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_REPITA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_PROCEDIMENTO'],
    },

    'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO': {
        # COMANDOS
        'COMANDOS': ['OP_ATRIB', 'EXPRESSAO'],
        'ATE_COMANDOS': ['OP_ATRIB', 'EXPRESSAO'],
        'REPITA_COMANDOS': ['OP_ATRIB', 'REPITA_EXPRESSAO'],
        'SE_COMANDOS': ['OP_ATRIB', 'SE_EXPRESSAO'],
        'SENAO_COMANDOS': ['OP_ATRIB', 'SENAO_EXPRESSAO'],
        'PARA_COMANDOS': ['OP_ATRIB', 'PARA_EXPRESSAO'],
        'ENQUANTO_COMANDOS': ['OP_ATRIB', 'ENQUANTO_EXPRESSAO'],
        'ESCOLHA_COMANDOS': ['OP_ATRIB', 'ESCOLHA_EXPRESSAO'],
        'OUTROCASO_COMANDOS': ['OP_ATRIB', 'OUTROCASO_EXPRESSAO'],
        'FUNCAO_COMANDOS': ['OP_ATRIB', 'FUNCAO_EXPRESSAO'],
        'PROCEDIMENTO_COMANDOS': ['OP_ATRIB', 'PROCEDIMENTO_EXPRESSAO'],

        # EXPRESSAO
        'EXPRESSAO': ['MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PARA': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITA': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],

        'EXPRESSAO_FUNCAO2PARAMETRO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],

        'REPITA_EXPRESSAO': ['REPITA_MAISEXPRESSAO'],
        'SE_EXPRESSAO': ['SE_MAISEXPRESSAO'],
        'SENAO_EXPRESSAO': ['SENAO_MAISEXPRESSAO'],
        'PARA_EXPRESSAO': ['PARA_MAISEXPRESSAO'],
        'ENQUANTO_EXPRESSAO': ['ENQUANTO_MAISEXPRESSAO'],
        'ESCOLHA_EXPRESSAO': ['ESCOLHA_MAISEXPRESSAO'],
        'OUTROCASO_EXPRESSAO': ['OUTROCASO_MAISEXPRESSAO'],
        'FUNCAO_EXPRESSAO': ['FUNCAO_MAISEXPRESSAO'],
        'PROCEDIMENTO_EXPRESSAO': ['PROCEDIMENTO_MAISEXPRESSAO'], 

        # MAISEXPRESSAO

        'MAISEXPRESSAO': ['OP_ATRIB', 'EXPRESSAO'],
        'REPITA_MAISEXPRESSAO': ['OP_ATRIB', 'REPITA_EXPRESSAO'],
        'SE_MAISEXPRESSAO': ['OP_ATRIB', 'SE_EXPRESSAO'],
        'SENAO_MAISEXPRESSAO': ['OP_ATRIB', 'SENAO_EXPRESSAO'],
        'PARA_MAISEXPRESSAO': ['OP_ATRIB', 'PARA_EXPRESSAO'],
        'ENQUANTO_MAISEXPRESSAO': ['OP_ATRIB', 'ENQUANTO_EXPRESSAO'],
        'ESCOLHA_MAISEXPRESSAO': ['OP_ATRIB', 'ESCOLHA_EXPRESSAO'],
        'OUTROCASO_MAISEXPRESSAO': ['OP_ATRIB', 'OUTROCASO_EXPRESSAO'],
        'FUNCAO_MAISEXPRESSAO': ['OP_ATRIB', 'FUNCAO_EXPRESSAO'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['OP_ATRIB', 'PROCEDIMENTO_EXPRESSAO'],

        'VALOR_INTEIRO/VARIAVEL': [],

        'ESCRITA': ['ALGO_TALVEZ'],
       
        'OPERANDO': [],
        'ATE_OPERANDO': ['ATE_COMANDOS'],
        'ATE_PARENTESES_OPERANDO': [],
        'OP_ARIT/OP_CARACTERE': [], 
        'OP_ARIT': [],

        'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO': [],

        'COMPARACAO': ['OP_REL'],
        'INICIO_COMPARACAO': ['OP_REL'],

        'ATE_EXPRESSAO': ['ATE_REL'],
        'ATE_MAISEXPRESSAO': ['ATE_REL'],

        'ATE_PARENTESES_EXPRESSAO': ['ATE_PARENTESES_REL'],
        'ATE_PARENTESES_MAISEXPRESSAO': ['ATE_PARENTESES_REL'],

        'PARENTESES': ['FECHAPARENTESES']
    },

    'ABRE_PARENTESES': {
        
        'EXPRESSAO': ['PARENTESES', 'MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO1PARAMETRO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PARA': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITA': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': [ 'PARENTESES', 'MAISEXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],


        'EXPRESSAO_FUNCAO2PARAMETRO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [ 'PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],

        
        'REPITA_EXPRESSAO': ['PARENTESES', 'REPITA_MAISEXPRESSAO'],
        'SE_EXPRESSAO': ['PARENTESES', 'SE_MAISEXPRESSAO'],
        'SENAO_EXPRESSAO': ['PARENTESES', 'SENAO_MAISEXPRESSAO'],
        'PARA_EXPRESSAO': ['PARENTESES', 'PARA_MAISEXPRESSAO'],
        'ENQUANTO_EXPRESSAO': ['PARENTESES', 'ENQUANTO_MAISEXPRESSAO'],
        'ESCOLHA_EXPRESSAO': ['PARENTESES', 'ESCOLHA_MAISEXPRESSAO'], 
        'OUTROCASO_EXPRESSAO': ['PARENTESES', 'OUTROCASO_MAISEXPRESSAO'],
        'FUNCAO_EXPRESSAO': ['PARENTESES', 'FUNCAO_MAISEXPRESSAO'], 
        'PROCEDIMENTO_EXPRESSAO': ['PARENTESES', 'PROCEDIMENTO_MAISEXPRESSAO'], 

        'FUNCAO_INICIAR': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'MAISPARAMETROS', 'MAISFUNCAO'],
        'PROCEDIMENTO_INICIAR': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'MAISPARAMETROS', 'MAISPROCEDIMENTO'],
        'PARENTESES': ['PARENTESES', 'FECHAPARENTESES'],
        'ABRINDO_PARENTESES_FUNCAO1PARAMETRO': [],
        
        'COMPARACAO': ['COMPARACAO', 'FECHAPARENTESES'],
        'INICIO_COMPARACAO': ['COMPARACAO', 'FECHAPARENTESES'],

        'ATE_EXPRESSAO': ['ATE_PARENTESES_EXPRESSAO', 'FECHAPARENTESES', 'ATE_COMANDOS'],
        'ATE_MAISEXPRESSAO': ['ATE_PARENTESES_EXPRESSAO', 'FECHAPARENTESES', 'ATE_COMANDOS'],

        'ATE_PARENTESES_EXPRESSAO': ['ATE_PARENTESES_EXPRESSAO', 'FECHAPARENTESES'],
        'ATE_PARENTESES_MAISEXPRESSAO': ['ATE_PARENTESES_EXPRESSAO', 'FECHAPARENTESES'],

        'ABREPARENTESES': [],

        'ABRIR_PARENTESES_RANDI': [ ]
    },

    'FECHA_PARENTESES': {
        'FECHAPARENTESES': [],
        'FECHANDO_PARENTESES_ANTERIOR': [],
        'FECHANDO_PARENTESES_FUNCAO1PARAMETRO': [],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO': ['MAISEXPRESSAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': ['ENQUANTO_MAISEXPRESSAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_PARA': ['PARA_MAISEXPRESSAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITA': ['REPITA_MAISEXPRESSAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['SENAO_MAISEXPRESSAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_SE': ['SE_MAISEXPRESSAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': ['ESCOLHA_MAISEXPRESSAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': ['OUTROCASO_MAISEXPRESSAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['FUNCAO_MAISEXPRESSAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['PROCEDIMENTO_MAISEXPRESSAO'],

#       'MAISEXPRESSAO_FUNCAO2PARAMETRO': [],
#       'MAISEXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [],
#       'MAISEXPRESSAO_FUNCAO2PARAMETRO_PARA': [],
#       'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITA': [],
#       'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO': [],
#       'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE': [],
#       'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [],
#       'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [],
#       'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': [],
#       'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': [],

        'FECHA_PARENTESES_ANTERIOR': [],
        'FECHAR_PARENTESES_RANDI_SITUACAO2': ['FECHA_PARENTESES_ANTERIOR'],
        'ALGO_TALVEZ':[],
        'MAISESCRITA': [],
        
        'MAISFUNCAO': ['OP_DELIMITACAO'],
        'MAISPROCEDIMENTO': [],

        'FECHAR_PARENTESES_RANDI': ['MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_ENQUANTO': ['ENQUANTO_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_PARA': ['PARA_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_REPITA': ['REPITA_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_SENAO': ['SENAO_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_SE': ['SE_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_ESCOLHA': ['ESCOLHA_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_OUTROCASO': ['OUTROCASO_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_FUNCAO': ['FUNCAO_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_PROCEDIMENTO': ['PROCEDIMENTO_MAISEXPRESSAO'],

        'FECHA_PARENTESES_ESPECIAL': ['MAISEXPRESSAO_FUNCAO1PARAMETRO'],
        'FECHA_PARENTESES_ESPECIAL_ENQUANTO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'FECHA_PARENTESES_ESPECIAL_PARA': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'FECHA_PARENTESES_ESPECIAL_REPITA': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'FECHA_PARENTESES_ESPECIAL_SENAO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'FECHA_PARENTESES_ESPECIAL_SE': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'FECHA_PARENTESES_ESPECIAL_ESCOLHA': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'FECHA_PARENTESES_ESPECIAL_OUTROCASO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'FECHA_PARENTESES_ESPECIAL_FUNCAO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'FECHA_PARENTESES_ESPECIAL_PROCEDIMENTO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO']
    },

    'VALOR_INT': {
        'EXPRESSAO': ['MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PARA': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITA': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],

        'EXPRESSAO_FUNCAO2PARAMETRO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],
       
        
        'REPITA_EXPRESSAO': ['REPITA_MAISEXPRESSAO'],
        'SE_EXPRESSAO': ['SE_MAISEXPRESSAO'],
        'SENAO_EXPRESSAO': ['SENAO_MAISEXPRESSAO'],
        'PARA_EXPRESSAO': ['PARA_MAISEXPRESSAO'],
        'ENQUANTO_EXPRESSAO': ['ENQUANTO_MAISEXPRESSAO'],
        'ESCOLHA_EXPRESSAO': ['ESCOLHA_MAISEXPRESSAO'],
        'OUTROCASO_EXPRESSAO': ['OUTROCASO_MAISEXPRESSAO'],
        'FUNCAO_EXPRESSAO': ['FUNCAO_MAISEXPRESSAO'],
        'PROCEDIMENTO_EXPRESSAO': ['PROCEDIMENTO_MAISEXPRESSAO'], 

        'PARENTESES': ['FECHAPARENTESES'],

        'OPERANDO': [],
        'ATE_OPERANDO': ['ATE_COMANDOS'],
        'ATE_PARENTESES_OPERANDO': [],
        'VALOR_ESCOLHA': [],
        'OP_ARIT/OP_CARACTERE': [], 
        'OP_ARIT': [], 
        'MOD': [], 
        'VALOR_INT': [],
        'ESCRITA': ['MAISESCRITA'],
        
        #VALOR_INTEIRO/VARIAVEL
        'VALOR_INTEIRO/VARIAVEL' : []
    },

    'VALOR_REAL': {
        'EXPRESSAO': ['MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PARA': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITA': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],

        'EXPRESSAO_FUNCAO2PARAMETRO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],
        
        'REPITA_EXPRESSAO': ['REPITA_MAISEXPRESSAO'],
        'SE_EXPRESSAO': ['SE_MAISEXPRESSAO'],
        'SENAO_EXPRESSAO': ['SENAO_MAISEXPRESSAO'],
        'PARA_EXPRESSAO': ['PARA_MAISEXPRESSAO'],
        'ENQUANTO_EXPRESSAO': ['ENQUANTO_MAISEXPRESSAO'],
        'ESCOLHA_EXPRESSAO': ['ESCOLHA_MAISEXPRESSAO'],
        'OUTROCASO_EXPRESSAO': ['OUTROCASO_MAISEXPRESSAO'],
        'FUNCAO_EXPRESSAO': ['FUNCAO_MAISEXPRESSAO'],
        'PROCEDIMENTO_EXPRESSAO': ['PROCEDIMENTO_MAISEXPRESSAO'], 

        'PARENTESES': ['FECHAPARENTESES'],

        'OPERANDO': [],
        'ATE_OPERANDO': ['ATE_COMANDOS'],
        'ATE_PARENTESES_OPERANDO': [],
        'OP_ARIT/OP_CARACTERE': [], 
        'OP_ARIT': [], 
        'MOD': [], 
        'VALOR_REAL': [],
        'ESCRITA': ['MAISESCRITA']
    },

    'VALOR_LITERAL': {
        'EXPRESSAO': ['MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PARA': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITA': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],

        'EXPRESSAO_FUNCAO2PARAMETRO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],
        
        'REPITA_EXPRESSAO': ['REPITA_MAISEXPRESSAO'],
        'SE_EXPRESSAO': ['SE_MAISEXPRESSAO'],
        'SENAO_EXPRESSAO': ['SENAO_MAISEXPRESSAO'],
        'PARA_EXPRESSAO': ['PARA_MAISEXPRESSAO'],
        'ENQUANTO_EXPRESSAO': ['ENQUANTO_MAISEXPRESSAO'],
        'ESCOLHA_EXPRESSAO': ['ESCOLHA_MAISEXPRESSAO'],
        'OUTROCASO_EXPRESSAO': ['OUTROCASO_MAISEXPRESSAO'],
        'FUNCAO_EXPRESSAO': ['FUNCAO_MAISEXPRESSAO'],
        'PROCEDIMENTO_EXPRESSAO': ['PROCEDIMENTO_MAISEXPRESSAO'], 

        'PARENTESES': ['FECHAPARENTESES'],
        'OPERANDO': [],
        'ATE_OPERANDO': ['ATE_COMANDOS'],
        'ATE_PARENTESES_OPERANDO': [],
        'OP_ARIT/OP_CARACTERE': [], 
        'OP_ARIT': [], 
        'MOD': [], 
        'VALOR_LITERAL': [],
        'ESCRITA': ['MAISESCRITA']
    },


    'VERDADEIRO': {
        'EXPRESSAO': ['MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PARA': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITA': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],

        'EXPRESSAO_FUNCAO2PARAMETRO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],
        
        'REPITA_EXPRESSAO': ['REPITA_MAISEXPRESSAO'],
        'SE_EXPRESSAO': ['SE_MAISEXPRESSAO'],
        'SENAO_EXPRESSAO': ['SENAO_MAISEXPRESSAO'],
        'PARA_EXPRESSAO': ['PARA_MAISEXPRESSAO'],
        'ENQUANTO_EXPRESSAO': ['ENQUANTO_MAISEXPRESSAO'],
        'ESCOLHA_EXPRESSAO': ['ESCOLHA_MAISEXPRESSAO'],
        'OUTROCASO_EXPRESSAO': ['OUTROCASO_MAISEXPRESSAO'],
        'FUNCAO_EXPRESSAO': ['FUNCAO_MAISEXPRESSAO'],
        'PROCEDIMENTO_EXPRESSAO': ['PROCEDIMENTO_MAISEXPRESSAO'],  

        'ATE_EXPRESSAO': ['ATE_COMANDOS'],

        'ATE_PARENTESES_EXPRESSAO': [],
        'ATE_PARENTESES_MAISEXPRESSAO': [],

        'PARENTESES': ['FECHAPARENTESES'],
        'OP_ARIT/OP_CARACTERE': [], 
        'OP_ARIT': [], 
        'MOD': [], 
        'VALOR_LOGICO': [],
        'ESCRITA':['MAISESCRITA']
    },

    'FALSO': {
        'EXPRESSAO': ['MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PARA': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITA': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],

        'EXPRESSAO_FUNCAO2PARAMETRO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],
        
        'REPITA_EXPRESSAO': ['REPITA_MAISEXPRESSAO'],
        'SE_EXPRESSAO': ['SE_MAISEXPRESSAO'],
        'SENAO_EXPRESSAO': ['SENAO_MAISEXPRESSAO'],
        'PARA_EXPRESSAO': ['PARA_MAISEXPRESSAO'],
        'ENQUANTO_EXPRESSAO': ['ENQUANTO_MAISEXPRESSAO'],
        'ESCOLHA_EXPRESSAO': ['ESCOLHA_MAISEXPRESSAO'],
        'OUTROCASO_EXPRESSAO': ['OUTROCASO_MAISEXPRESSAO'],
        'FUNCAO_EXPRESSAO': ['FUNCAO_MAISEXPRESSAO'],
        'PROCEDIMENTO_EXPRESSAO': ['PROCEDIMENTO_MAISEXPRESSAO'],  

        'ATE_EXPRESSAO': ['ATE_COMANDOS'],

        'ATE_PARENTESES_EXPRESSAO': [],
        'ATE_PARENTESES_MAISEXPRESSAO': [],

        'PARENTESES': ['FECHAPARENTESES'],
        'OP_ARIT/OP_CARACTERE': [], 
        'OP_ARIT': [], 
        'MOD': [], 
        'VALOR_LOGICO': [],
        'ESCRITA': ['MAISESCRITA']
    },

    'NOME_ALGORITMO/VALOR_LITERAL': {
        'NOME_ALGORITMO/VALOR_LITERAL': [],
        'EXPRESSAO': ['MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PARA': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITA': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],

        'EXPRESSAO_FUNCAO2PARAMETRO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],

        
        'REPITA_EXPRESSAO': ['REPITA_MAISEXPRESSAO'],
        'SE_EXPRESSAO': ['SE_MAISEXPRESSAO'],
        'SENAO_EXPRESSAO': ['SENAO_MAISEXPRESSAO'],
        'PARA_EXPRESSAO': ['PARA_MAISEXPRESSAO'],
        'ENQUANTO_EXPRESSAO': ['ENQUANTO_MAISEXPRESSAO'],
        'ESCOLHA_EXPRESSAO': ['ESCOLHA_MAISEXPRESSAO'],
        'OUTROCASO_EXPRESSAO': ['OUTROCASO_MAISEXPRESSAO'],
        'FUNCAO_EXPRESSAO': ['FUNCAO_MAISEXPRESSAO'],
        'PROCEDIMENTO_EXPRESSAO': ['PROCEDIMENTO_MAISEXPRESSAO'],  

        'PARENTESES': ['FECHAPARENTESES'],
        'ESCRITA': ['MAISESCRITA'],
        
        'OPERANDO': [],
        'ATE_OPERANDO': ['ATE_COMANDOS'],
        'ATE_PARENTESES_OPERANDO': [],
        'VALOR_ESCOLHA': [],
        'OP_ARIT/OP_CARACTERE': [], 
        'OP_ARIT': [], 
        'MOD': []
    },

    'OP_ARIT/OP_CARACTERE': {
        'FECHAPARENTESES': ['PARENTESES'],
        #Funciona, faltava antes
        'FECHANDO_PARENTESES_FUNCAO1PARAMETRO': ['PARENTESES'],
        
        'MAISEXPRESSAO': ['EXPRESSAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO': ['EXPRESSAO_FUNCAO1PARAMETRO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': ['EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_PARA': ['EXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITA': ['EXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['EXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_SE': ['EXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': ['EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': ['EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],

        'MAISEXPRESSAO_FUNCAO2PARAMETRO': ['EXPRESSAO_FUNCAO2PARAMETRO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': ['EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_PARA': ['EXPRESSAO_FUNCAO2PARAMETRO_PARA'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITA': ['EXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['EXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE': ['EXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': ['EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': ['EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],
        
        'REPITA_MAISEXPRESSAO': ['REPITA_EXPRESSAO'],
        'SE_MAISEXPRESSAO': ['SE_EXPRESSAO'],
        'SENAO_MAISEXPRESSAO': ['SENAO_EXPRESSAO'],
        'PARA_MAISEXPRESSAO': ['PARA_EXPRESSAO'],
        'ENQUANTO_MAISEXPRESSAO': ['ENQUANTO_EXPRESSAO'],
        'ESCOLHA_MAISEXPRESSAO': ['ESCOLHA_EXPRESSAO'],
        'OUTROCASO_MAISEXPRESSAO': ['OUTROCASO_EXPRESSAO'],
        'FUNCAO_MAISEXPRESSAO': ['FUNCAO_EXPRESSAO'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['PROCEDIMENTO_EXPRESSAO'],
        

        'MAISESCRITA': ['ESCRITA'],
        'ALGO_TALVEZ': ['ESCRITA']
    },

    'OP_ARIT': {
        'FECHAPARENTESES': ['PARENTESES'],
        #Funciona, faltava antes
        'FECHANDO_PARENTESES_FUNCAO1PARAMETRO': ['PARENTESES'],
        
        'MAISEXPRESSAO': ['EXPRESSAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO': ['EXPRESSAO_FUNCAO1PARAMETRO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': ['EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_PARA': ['EXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITA': ['EXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['EXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_SE': ['EXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': ['EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': ['EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],


        'MAISEXPRESSAO_FUNCAO2PARAMETRO': ['EXPRESSAO_FUNCAO2PARAMETRO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': ['EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_PARA': ['EXPRESSAO_FUNCAO2PARAMETRO_PARA'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITA': ['EXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['EXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE': ['EXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': ['EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': ['EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],


        
        'REPITA_MAISEXPRESSAO': ['REPITA_EXPRESSAO'],
        'SE_MAISEXPRESSAO': ['SE_EXPRESSAO'],
        'SENAO_MAISEXPRESSAO': ['SENAO_EXPRESSAO'],
        'PARA_MAISEXPRESSAO': ['PARA_EXPRESSAO'],
        'ENQUANTO_MAISEXPRESSAO': ['ENQUANTO_EXPRESSAO'],
        'ESCOLHA_MAISEXPRESSAO': ['ESCOLHA_EXPRESSAO'],
        'OUTROCASO_MAISEXPRESSAO': ['OUTROCASO_EXPRESSAO'],
        'FUNCAO_MAISEXPRESSAO': ['FUNCAO_EXPRESSAO'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['PROCEDIMENTO_EXPRESSAO'],
        'MAISESCRITA': ['ESCRITA'],
         'ALGO_TALVEZ': ['ESCRITA']
    },

    'MOD': {
        'FECHAPARENTESES': ['PARENTESES'],
        #Funciona, faltava antes
        'FECHANDO_PARENTESES_FUNCAO1PARAMETRO': ['PARENTESES'],
        'MAISEXPRESSAO': ['EXPRESSAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO': ['EXPRESSAO_FUNCAO1PARAMETRO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO': ['EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_PARA': ['EXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITA': ['EXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['EXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_SE': ['EXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': ['EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': ['EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],

        'MAISEXPRESSAO_FUNCAO2PARAMETRO': ['EXPRESSAO_FUNCAO2PARAMETRO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': ['EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_PARA': ['EXPRESSAO_FUNCAO2PARAMETRO_PARA'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITA': ['EXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['EXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE': ['EXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': ['EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': ['EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],

        'REPITA_MAISEXPRESSAO': ['REPITA_EXPRESSAO'],
        'SE_MAISEXPRESSAO': ['SE_EXPRESSAO'],
        'SENAO_MAISEXPRESSAO': ['SENAO_EXPRESSAO'],
        'PARA_MAISEXPRESSAO': ['PARA_EXPRESSAO'],
        'ENQUANTO_MAISEXPRESSAO': ['ENQUANTO_EXPRESSAO'],
        'ESCOLHA_MAISEXPRESSAO': ['ESCOLHA_EXPRESSAO'],
        'OUTROCASO_MAISEXPRESSAO': ['OUTROCASO_EXPRESSAO'],
        'FUNCAO_MAISEXPRESSAO': ['FUNCAO_EXPRESSAO'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['PROCEDIMENTO_EXPRESSAO'],
         'MAISESCRITA': ['ESCRITA'],
         'ALGO_TALVEZ': ['ESCRITA']
    },

    'OP_ATRIB': {
        'OP_ATRIB': [],
        'OP_ATRIB2': [],
        'OP_ATRIB3': []
    },

    'FIMALGORITMO': {
        'MAISEXPRESSAO': [],
        'ATE_COMANDOS': [],
        'COMANDOS': []
    },

    # Operadores Lógicos

    'E': { 
        'MAISCOMPARACAO': ['COMPARACAO', 'MAISCOMPARACAO'],
        'ATE_COMANDOS': ['ATE_EXPRESSAO'],

        'FECHAPARENTESES': ['PARENTESES'],

        'MAISEXPRESSAO': ['EXPRESSAO'],
        'REPITA_MAISEXPRESSAO': ['REPITA_EXPRESSAO'],
        'SE_MAISEXPRESSAO': ['SE_EXPRESSAO'],
        'SENAO_MAISEXPRESSAO': ['SENAO_EXPRESSAO'],
        'PARA_MAISEXPRESSAO': ['PARA_EXPRESSAO'],
        'ENQUANTO_MAISEXPRESSAO': ['ENQUANTO_EXPRESSAO'],
        'ESCOLHA_MAISEXPRESSAO': ['ESCOLHA_EXPRESSAO'],
        'OUTROCASO_MAISEXPRESSAO': ['OUTROCASO_EXPRESSAO'],
        'FUNCAO_MAISEXPRESSAO': ['FUNCAO_EXPRESSAO'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['PROCEDIMENTO_EXPRESSAO'],
    },

    'OU': { 
        'MAISCOMPARACAO': ['COMPARACAO', 'MAISCOMPARACAO'],
        'ATE_COMANDOS': ['ATE_EXPRESSAO'],

        'FECHAPARENTESES': ['PARENTESES'],

        'MAISEXPRESSAO': ['EXPRESSAO'],
        'REPITA_MAISEXPRESSAO': ['REPITA_EXPRESSAO'],
        'SE_MAISEXPRESSAO': ['SE_EXPRESSAO'],
        'SENAO_MAISEXPRESSAO': ['SENAO_EXPRESSAO'],
        'PARA_MAISEXPRESSAO': ['PARA_EXPRESSAO'],
        'ENQUANTO_MAISEXPRESSAO': ['ENQUANTO_EXPRESSAO'],
        'ESCOLHA_MAISEXPRESSAO': ['ESCOLHA_EXPRESSAO'],
        'OUTROCASO_MAISEXPRESSAO': ['OUTROCASO_EXPRESSAO'],
        'FUNCAO_MAISEXPRESSAO': ['FUNCAO_EXPRESSAO'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['PROCEDIMENTO_EXPRESSAO']      
    },

    'XOU': { 
        'MAISCOMPARACAO': ['COMPARACAO', 'MAISCOMPARACAO'],
        'ATE_COMANDOS': ['ATE_EXPRESSAO'],

        'FECHAPARENTESES': ['PARENTESES'],

        'MAISEXPRESSAO': ['EXPRESSAO'],
        'REPITA_MAISEXPRESSAO': ['REPITA_EXPRESSAO'],
        'SE_MAISEXPRESSAO': ['SE_EXPRESSAO'],
        'SENAO_MAISEXPRESSAO': ['SENAO_EXPRESSAO'],
        'PARA_MAISEXPRESSAO': ['PARA_EXPRESSAO'],
        'ENQUANTO_MAISEXPRESSAO': ['ENQUANTO_EXPRESSAO'],
        'ESCOLHA_MAISEXPRESSAO': ['ESCOLHA_EXPRESSAO'],
        'OUTROCASO_MAISEXPRESSAO': ['OUTROCASO_EXPRESSAO'],
        'FUNCAO_MAISEXPRESSAO': ['FUNCAO_EXPRESSAO'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['PROCEDIMENTO_EXPRESSAO']     
    },

    'NAO': { 
        'COMPARACAO': ['INICIO_COMPARACAO'],
        'EXPRESSAO': ['EXPRESSAO'],
        'PARENTESES': ['PARENTESES'],
        'ATE_EXPRESSAO': ['ATE_MAISEXPRESSAO'],
        'ATE_PARENTESES_EXPRESSAO': ['ATE_PARENTESES_MAISEXPRESSAO']
    },

    # LEIA
    
    'LEIA': { 
        'COMANDOS': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'COMANDOS'],
        'ATE_COMANDOS': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'COMANDOS'],
        'REPITA_COMANDOS': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'REPITA_COMANDOS'],
        'SE_COMANDOS': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'SE_COMANDOS'],
        'SENAO_COMANDOS': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'SENAO_COMANDOS'],
        'PARA_COMANDOS': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'PARA_COMANDOS'],
        'ENQUANTO_COMANDOS': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'ENQUANTO_COMANDOS'],
        'ESCOLHA_COMANDOS': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'ESCOLHA_COMANDOS'],
        'OUTROCASO_COMANDOS': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'OUTROCASO_COMANDOS'],
        'FUNCAO_COMANDOS': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_COMANDOS': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'PROCEDIMENTO_COMANDOS'],

        'MAISEXPRESSAO': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'COMANDOS'],
        'REPITA_MAISEXPRESSAO': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'REPITA_COMANDOS'],
        'SE_MAISEXPRESSAO': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'SE_COMANDOS'],
        'SENAO_MAISEXPRESSAO': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'SENAO_COMANDOS'],
        'PARA_MAISEXPRESSAO': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'PARA_COMANDOS'],
        'ENQUANTO_MAISEXPRESSAO': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'ENQUANTO_COMANDOS'],
        'ESCOLHA_MAISEXPRESSAO': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'ESCOLHA_COMANDOS'],
        'OUTROCASO_MAISEXPRESSAO': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'OUTROCASO_COMANDOS'],
        'FUNCAO_MAISEXPRESSAO': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'PROCEDIMENTO_COMANDOS']
    },

    # ESCREVA - ESCREVAL

    'ESCREVA': { 
        'COMANDOS': ['ABREPARENTESES', 'ESCRITA', 'COMANDOS'],
        'ATE_COMANDOS': ['ABREPARENTESES', 'ESCRITA', 'COMANDOS'],
        'REPITA_COMANDOS': ['ABREPARENTESES', 'ESCRITA', 'REPITA_COMANDOS'],
        'SE_COMANDOS': ['ABREPARENTESES', 'ESCRITA', 'SE_COMANDOS'],
        'SENAO_COMANDOS': ['ABREPARENTESES', 'ESCRITA', 'SENAO_COMANDOS'],
        'PARA_COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'PARA_COMANDOS'],
        'ENQUANTO_COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'ENQUANTO_COMANDOS'],
        'ESCOLHA_COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'ESCOLHA_COMANDOS'],
        'OUTROCASO_COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'OUTROCASO_COMANDOS'],
        'FUNCAO_COMANDOS': ['ABREPARENTESES', 'ESCRITA', 'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_COMANDOS': ['ABREPARENTESES', 'ESCRITA', 'PROCEDIMENTO_COMANDOS'],

        'MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA', 'COMANDOS'],
        'REPITA_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA', 'REPITA_COMANDOS'],
        'SE_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA', 'SE_COMANDOS'],
        'SENAO_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA', 'SENAO_COMANDOS'],
        'PARA_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA', 'PARA_COMANDOS'],
        'ENQUANTO_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA', 'ENQUANTO_COMANDOS'],
        'ESCOLHA_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA', 'ESCOLHA_COMANDOS'],
        'OUTROCASO_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA', 'OUTROCASO_COMANDOS'],
        'FUNCAO_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA', 'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA', 'PROCEDIMENTO_COMANDOS']
    },

    'ESCREVAL': { 
        'COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'COMANDOS'],
        'ATE_COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'COMANDOS'],
        'REPITA_COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'REPITA_COMANDOS'],
        'SE_COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'SE_COMANDOS'],
        'SENAO_COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'SENAO_COMANDOS'],
        'PARA_COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'PARA_COMANDOS'],
        'ENQUANTO_COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'ENQUANTO_COMANDOS'],
        'ESCOLHA_COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'ESCOLHA_COMANDOS'],
        'OUTROCASO_COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'OUTROCASO_COMANDOS'],
        'FUNCAO_COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'PROCEDIMENTO_COMANDOS'],

        'MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA',  'COMANDOS'],
        'REPITA_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA',  'REPITA_COMANDOS'],
        'SE_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA',  'SE_COMANDOS'],
        'SENAO_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA',  'SENAO_COMANDOS'],
        'PARA_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA',  'PARA_COMANDOS'],
        'ENQUANTO_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA',  'ENQUANTO_COMANDOS'],
        'ESCOLHA_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA',  'ESCOLHA_COMANDOS'],
        'OUTROCASO_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA',  'OUTROCASO_COMANDOS'],
        'FUNCAO_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA',  'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA',  'PROCEDIMENTO_COMANDOS']
    },


    # PARA - FACA 

    'PARA': {
        'COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'COMANDOS'],
        'ATE_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'COMANDOS'],
        'REPITA_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'REPITA_COMANDOS'],
        'SE_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'SE_COMANDOS'],
        'SENAO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'SENAO_COMANDOS'],
        'PARA_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'PARA_COMANDOS'],
        'ENQUANTO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'ENQUANTO_COMANDOS'],
        'ESCOLHA_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'ESCOLHA_COMANDOS'],
        'OUTROCASO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'OUTROCASO_COMANDOS'],
        'FUNCAO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'PROCEDIMENTO_COMANDOS'],

        'MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'COMANDOS'],
        'REPITA_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'REPITA_COMANDOS'],
        'SE_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'SE_COMANDOS'],
        'SENAO_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'SENAO_COMANDOS'],
        'PARA_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'PARA_COMANDOS'],
        'ENQUANTO_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'ENQUANTO_COMANDOS'],
        'ESCOLHA_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'ESCOLHA_COMANDOS'],
        'OUTROCASO_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'OUTROCASO_COMANDOS'],
        'FUNCAO_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'PROCEDIMENTO_COMANDOS'],
    },

    'ATE': {
        'PARA_ATE': [],
        'REPITA_COMANDOS': ['ATE_EXPRESSAO'],
        'REPITA_MAISEXPRESSAO': ['ATE_EXPRESSAO'],
        'ATE_COMANDOS': ['ATE_EXPRESSAO'],
        'ATE_MAISEXPRESSAO': ['ATE_EXPRESSAO'],
    },

    'FACA': {
        'FACA_PASSO': [],
        'FACA': [],
        'MAISCOMPARACAO': []
    },

    'PASSO': {
        'FACA_PASSO': ['VALOR_INT', 'FACA']
    },
    
    'FIMPARA': {
        'PARA_MAISEXPRESSAO': [],
        'PARA_COMANDOS': []
    },

    # ENQUANTO

    'ENQUANTO': {
        'COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'COMANDOS'],
        'ATE_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'COMANDOS'],
        'REPITA_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'REPITA_COMANDOS'],
        'SE_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'SE_COMANDOS'],
        'SENAO_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'SENAO_COMANDOS'],
        'PARA_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'PARA_COMANDOS'],
        'ENQUANTO_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'ENQUANTO_COMANDOS'],
        'ESCOLHA_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'ESCOLHA_COMANDOS'],
        'OUTROCASO_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'OUTROCASO_COMANDOS'],
        'FUNCAO_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'PROCEDIMENTO_COMANDOS'],

        'MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'COMANDOS'],
        'REPITA_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'REPITA_COMANDOS'],
        'SE_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'SE_COMANDOS'],
        'SENAO_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'SENAO_COMANDOS'],
        'PARA_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'PARA_COMANDOS'],
        'ENQUANTO_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'ENQUANTO_COMANDOS'],
        'ESCOLHA_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'ESCOLHA_COMANDOS'],
        'ENQUANTO_OC_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'ENQUANTO_OC_COMANDOS'],
        'FUNCAO_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'PROCEDIMENTO_COMANDOS']
    },

    'FIMENQUANTO': {
        'ENQUANTO_MAISEXPRESSAO': [],
        'ENQUANTO_COMANDOS': []
    },
    
    # ESCOLHA

    'ESCOLHA': {
        'COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'COMANDOS'],
        'ATE_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'COMANDOS'],
        'REPITA_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'REPITA_COMANDOS'],
        'SE_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'SE_COMANDOS'],
        'SENAO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'SENAO_COMANDOS'],
        'PARA_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'PARA_COMANDOS'],
        'ENQUANTO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'ENQUANTO_COMANDOS'],
        'ESCOLHA_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'ESCOLHA_COMANDOS'],
        'OUTROCASO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'OUTROCASO_COMANDOS'],
        'FUNCAO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'PROCEDIMENTO_COMANDOS'],

        'MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'COMANDOS'],
        'REPITA_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'REPITA_COMANDOS'],
        'SE_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'SE_COMANDOS'],
        'SENAO_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'SENAO_COMANDOS'],
        'PARA_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'PARA_COMANDOS'],
        'ENQUANTO_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'ENQUANTO_COMANDOS'],
        'ESCOLHA_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'ESCOLHA_COMANDOS'],
        'OUTROCASO_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'OUTROCASO_COMANDOS'], 
        'FUNCAO_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'PROCEDIMENTO_COMANDOS']
    },

    'CASO': {
        'CASO': [],
        'ESCOLHA_COMANDOS': ['VALOR_ESCOLHA', 'ESCOLHA_COMANDOS'],
        'ESCOLHA_MAISEXPRESSAO': ['VALOR_ESCOLHA', 'ESCOLHA_COMANDOS']
    },

    'OUTROCASO': {
        'ESCOLHA_COMANDOS': ['OUTROCASO_COMANDOS'],
        'ESCOLHA_MAISEXPRESSAO': ['OUTROCASO_COMANDOS']
    },

    'FIMESCOLHA': {
        'OUTROCASO_COMANDOS': [],
        'OUTROCASO_MAISEXPRESSAO': []
    },

    # SE - ENTAO - SENAO

    'SE': {    
        'COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'COMANDOS'],
        'ATE_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'COMANDOS'],
        'SE_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'SE_COMANDOS'],
        'SENAO_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'FIMSE'],
        'REPITA_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'REPITA_COMANDOS'],
        'PARA_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'PARA_COMANDOS'],
        'ENQUANTO_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'ENQUANTO_COMANDOS'],
        'ESCOLHA_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'ESCOLHA_COMANDOS'],
        'OUTROCASO_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'OUTROCASO_COMANDOS'],
        'FUNCAO_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'PROCEDIMENTO_COMANDOS'],

        'MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'COMANDOS'],
        'SE_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS'],
        'SENAO_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'FIMSE'],
        'REPITA_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'REPITA_COMANDOS'],
        'PARA_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'PARA_COMANDOS'],
        'ENQUANTO_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'ENQUANTO_COMANDOS'],
        'ESCOLHA_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'ESCOLHA_COMANDOS'],
        'OUTROCASO_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'OUTROCASO_COMANDOS'],
        'FUNCAO_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'PROCEDIMENTO_COMANDOS']
    },

    'ENTAO': {
        'MAISCOMPARACAO': []
    },

    'SENAO': {
        'SE_COMANDOS': ['SENAO_COMANDOS'],
        'SE_MAISEXPRESSAO': ['SENAO_COMANDOS'] # SENAO_COMANDOS -> Ramifica duas oportunidades (utilizar o se e continuar os comandos ou não utilizar o se e esperar um fimse no final)
    },

    'FIMSE':{
        'SE_COMANDOS': [],
        'SE_MAISEXPRESSAO': [],
        'SENAO_COMANDOS': [],
        'SENAO_MAISEXPRESSAO': [],
        'FIMSE': []
    },

    # REPITA - ATE 

    'REPITA': { 
        'COMANDOS': ['REPITA_COMANDOS'],
        'ATE_COMANDOS': ['REPITA_COMANDOS'],
        'REPITA_COMANDOS': ['REPITA_COMANDOS'], 
        'SE_COMANDOS': ['REPITA_COMANDOS'], 
        'SENAO_COMANDOS': ['REPITA_COMANDOS'], 
        'PARA_COMANDOS': ['REPITA_COMANDOS'], 
        'ENQUANTO_COMANDOS': ['REPITA_COMANDOS'], 
        'ESCOLHA_COMANDOS': ['REPITA_COMANDOS'], 
        'OUTROCASO_COMANDOS': ['REPITA_COMANDOS'], 
        'FUNCAO_COMANDOS': ['REPITA_COMANDOS'],
        'PROCEDIMENTO_COMANDOS': ['REPITA_COMANDOS'],

        'MAISEXPRESSAO': ['REPITA_COMANDOS'],
        'REPITA_MAISEXPRESSAO': ['REPITA_COMANDOS'], 
        'SE_MAISEXPRESSAO': ['REPITA_COMANDOS'], 
        'SENAO_MAISEXPRESSAO': ['REPITA_COMANDOS'], 
        'PARA_MAISEXPRESSAO': ['REPITA_COMANDOS'], 
        'ENQUANTO_MAISEXPRESSAO': ['REPITA_COMANDOS'], 
        'ESCOLHA_MAISEXPRESSAO': ['REPITA_COMANDOS'], 
        'OUTROCASO_MAISEXPRESSAO': ['REPITA_COMANDOS'],
        'FUNCAO_MAISEXPRESSAO': ['REPITA_COMANDOS'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['REPITA_COMANDOS']     
    },

    'FIMREPITA': { 
        'REPITA_COMANDOS': ['COMANDOS'],
        'REPITA_MAISEXPRESSAO': ['COMANDOS']
    },

    # INTERROMPA

    'INTERROMPA': { 
        'COMANDOS': ['COMANDOS'],
        'ATE_COMANDOS': ['COMANDOS'],
        'REPITA_COMANDOS': ['REPITA_COMANDOS'], 
        'SE_COMANDOS': ['SE_COMANDOS'], 
        'SENAO_COMANDOS': ['SENAO_COMANDOS'], 
        'PARA_COMANDOS': ['PARA_COMANDOS'], 
        'ENQUANTO_COMANDOS': ['ENQUANTO_COMANDOS'], 
        'ESCOLHA_COMANDOS': ['ESCOLHA_COMANDOS'], 
        'OUTROCASO_COMANDOS': ['OUTROCASO_COMANDOS'], 
        'FUNCAO_COMANDOS': ['FUNCAO_COMANDOS'],
        'PROCEDIMENTO_COMANDOS': ['PROCEDIMENTO_COMANDOS'],

        'MAISEXPRESSAO': ['COMANDOS'],
        'REPITA_MAISEXPRESSAO': ['REPITA_COMANDOS'],
        'SE_MAISEXPRESSAO': ['SE_COMANDOS'],
        'SENAO_MAISEXPRESSAO': ['SENAO_COMANDOS'],
        'PARA_MAISEXPRESSAO': ['PARA_COMANDOS'],
        'ENQUANTO_MAISEXPRESSAO': ['ENQUANTO_COMANDOS'],
        'ESCOLHA_MAISEXPRESSAO': ['ESCOLHA_COMANDOS'],
        'OUTROCASO_MAISEXPRESSAO': ['OUTROCASO_COMANDOS'],
        'FUNCAO_MAISEXPRESSAO': ['FUNCAO_COMANDOS'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['PROCEDIMENTO_COMANDOS']
    },
    
    # RETORNE

    'RETORNE': { 
        'COMANDOS': ['EXPRESSAO'],
        'ATE_COMANDOS': ['EXPRESSAO'], 
        'REPITA_COMANDOS': ['REPITA_EXPRESSAO'], 
        'SE_COMANDOS': ['SE_EXPRESSAO'],
        'SENAO_COMANDOS': ['SENAO_EXPRESSAO'],
        'PARA_COMANDOS': ['PARA_EXPRESSAO'],
        'ENQUANTO_COMANDOS': ['ENQUANTO_EXPRESSAO'],
        'ESCOLHA_COMANDOS': ['ESCOLHA_EXPRESSAO'],
        'OUTROCASO_COMANDOS': ['OUTROCASO_EXPRESSAO'],
        'FUNCAO_COMANDOS': ['FUNCAO_EXPRESSAO'],
        'PROCEDIMENTO_COMANDOS': ['PROCEDIMENTO_EXPRESSAO'],
        
        'MAISEXPRESSAO':  ['EXPRESSAO'],
        'REPITA_MAISEXPRESSAO':  ['REPITA_EXPRESSAO'],
        'SE_MAISEXPRESSAO':  ['SE_EXPRESSAO'],
        'SENAO_MAISEXPRESSAO':  ['SENAO_EXPRESSAO'],
        'PARA_MAISEXPRESSAO':  ['PARA_EXPRESSAO'],
        'ENQUANTO_MAISEXPRESSAO':  ['ENQUANTO_EXPRESSAO'],
        'ESCOLHA_MAISEXPRESSAO':  ['ESCOLHA_EXPRESSAO'],
        'OUTROCASO_MAISEXPRESSAO':  ['OUTROCASO_EXPRESSAO'],
        'FUNCAO_MAISEXPRESSAO':  ['FUNCAO_EXPRESSAO'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['PROCEDIMENTO_EXPRESSAO'],
    }

}  # Fecha Dicionário

# Tratamento de Erros

def trata_erro_token(topo, terminal, pilha):
    return f'Erro: Palavra não esperada "{terminal}", Token Esperado: {topo}, \n\n\nPilha: "{pilha}"'
    
def trata_erro_estado(terminal, pilha):
    token = pilha.pop()
    return f'Erro: Faltam palavras, após a palavra "{terminal}", Token Esperado: {token}, \n\n\nPilha: "{pilha}"'
    
# Definição Sintático

def sintatico(cadeia):
    estado = 'q1'
    pilha = ['S']

    try:
        for terminal in cadeia:
            topo = pilha.pop()
            pilha.extend(reversed(transicao_sintatico[terminal][topo]))
        if len(pilha) == 0:
            estado = 'qf'
        if estado != 'qf':
            return trata_erro_estado(terminal, pilha)
    except Exception:
        return trata_erro_token(topo, terminal, pilha)
    return "aceito."

# Compilar a parte léxica

def compilarLexico():
    codigo = editor_texto.get("1.0", tk.END).strip()
    if not codigo:
        messagebox.showwarning("Aviso", "O editor de código está vazio.")
        return None
    
    linhas = codigo.splitlines()
    tabela_simbolos = []
    for linha in linhas:
        resultado = lexico(linha.split())
        if resultado is None:
            return None
        tabela_simbolos.extend(resultado)

    # Exibir resultado na área de saída
    area_resultado.config(state=tk.NORMAL)
    area_resultado.delete("1.0", tk.END)
    for simbolo in tabela_simbolos:
        area_resultado.insert(tk.END, f"{simbolo[0]}: {simbolo[1]}\n")
    area_resultado.config(state=tk.DISABLED)
    
    return tabela_simbolos # Retorna a tabela de símbolos para o sintático


# Compilar a parte sintática

def compilar():
    tabela_simbolos = compilarLexico()  # Gera a tabela de símbolos a partir do léxico
    if tabela_simbolos is None:
        return
    
    # Cria uma cadeia de entrada para o sintático a partir dos tipos dos tokens
    cadeia = [simbolo[1] for simbolo in tabela_simbolos] # List Comprehension
    
    resultado = sintatico(cadeia)

    # Exibir o resultado
    area_resultado.config(state=tk.NORMAL)
    area_resultado.delete("1.0", tk.END)
    area_resultado.insert(tk.END, f"Resultado: {resultado}")
    area_resultado.config(state=tk.DISABLED)
    

def arquivo():
    filename = fd.askopenfilename()

    # Passar arquivo para a área de entrada
    try:
        editor_texto.config(state=tk.NORMAL)
        editor_texto.delete("1.0", tk.END)
        with open(filename, "r") as arquivo:
            for linha in arquivo:
                editor_texto.insert(tk.END, f"{linha}")
            arquivo.close()
           
    except:
        messagebox.showwarning("Aviso", "Nenhum arquivo selecionado")

def salvarArquivo():
    root = tk.Tk()
    root.withdraw()
 
    codigo = editor_texto.get("1.0", tk.END).strip()
    if not codigo:
        messagebox.showwarning("Aviso", "O editor de código está vazio.")
        
    filename = fd.asksaveasfilename(
        title="Salvar Como",
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt"), ("All Files", "*.*")]
    )
    try:
        linhas = codigo.splitlines()
        with open(filename, 'w') as f:
            for linha in linhas:
                f.write(f'{linha}\n')
            f.close()
    except:
        messagebox.showwarning("Aviso", "Nenhum nome de arquivo selecionado")

def limpar():
    editor_texto.config(state=tk.NORMAL)
    editor_texto.delete("1.0", tk.END)
    area_resultado.config(state=tk.NORMAL)
    area_resultado.delete("1.0", tk.END)

def ajuda():
    webbrowser.open("https://www.acad.cefetmg.br/uploads/MATERIAIS_AULAS/340988-A_Linguagem_de_Programa%C3%A7%C3%A3o_do_VisuAlg.pdf")
    

def sair():
    janela.destroy()
        

        
       
        

# Configuração da janela principal
janela = tk.Tk()
janela.title("Compilador")
janela.geometry("1400x700")
janela['bg'] = '#03C04A' 

frame_buttons = tk.Frame(janela)
frame_buttons.pack(side="top", fill=tk.BOTH)
frame_buttons['bg'] ='silver'

# Botão compilar
botao_compilar = tk.Button(frame_buttons, text="Compilar", command=compilar, bg='#9A7B4F', font = "bold")
botao_compilar.pack(side="left", pady=5)

# Botão arquivo
botao_arquivo = tk.Button(frame_buttons, text="Carregar Arquivo", command=arquivo, bg="light blue", font = "bold")
botao_arquivo.pack(side="left",pady=5)

# Botão Salvar Arquivo
botao_salvar_arquivo = tk.Button(frame_buttons, text="Guardar em um Arquivo", command=salvarArquivo, bg="orange", font = "bold")
botao_salvar_arquivo.pack(side="left", pady=5)

# Botão Limpar
botao_limpar = tk.Button(frame_buttons, text="Limpar", command=limpar, bg="red", font = "bold")
botao_limpar.pack(side="left", pady=5)


# Botão Ajuda
botao_ajuda = tk.Button(frame_buttons, text="Ajuda", command=ajuda, bg="gold", font = "bold")
botao_ajuda.pack(side="left", pady=5)

# Botão Sair
botao_ajuda = tk.Button(frame_buttons, text="Sair", command=sair, bg="purple", font = "bold")
botao_ajuda.pack(side="left", pady=5)


frame_scrolledtexts = tk.Frame(janela)
frame_scrolledtexts.pack(side="top",expand=True, fill=tk.BOTH)
frame_scrolledtexts['bg'] = '#03C04A'

# Editor de texto
editor_texto = scrolledtext.ScrolledText(frame_scrolledtexts, wrap=tk.WORD, width = 30, height=10, bg = "#B2D3C2", font = "bold")
editor_texto.pack(side="left", expand=True, pady=10, padx=10, fill=tk.BOTH)

# Mostrar resultado
area_resultado = scrolledtext.ScrolledText(frame_scrolledtexts, wrap=tk.WORD, width = 30, height=10, state=tk.DISABLED, bg = "#B2D3C2", font="bold")
area_resultado.pack(side = "left", expand=True, pady=10, padx=10, fill=tk.BOTH)

            
statusbar =tk.Label(janela, text="Copyright © 2024 Bruna da Silva Ines, Fernando Felix Nunes Teixeira, Uriel Manoel da Silva. All right reserved", bd=1, relief=tk.SUNKEN, anchor = tk.W)
statusbar.pack(side=tk.BOTTOM, fill = tk.X)




janela.mainloop()
