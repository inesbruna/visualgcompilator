import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import filedialog as fd
import webbrowser
import sys
import copy
import os  


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
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': [],
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
        'MAISATE_REL': ['MAISATE_OPERANDO'],
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
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': [ 'PARENTESES', 'REPITAMAIS_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['PARENTESES', 'SENAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': ['PARENTESES', 'SE_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': [ 'PARENTESES', 'ESCOLHA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': [ 'PARENTESES', 'OUTROCASO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['PARENTESES', 'FUNCAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['PARENTESES', 'PROCEDIMENTO_MAISEXPRESSAO'],
        
        'EXPRESSAO_FUNCAO2PARAMETRO': [ 'EXPRESSAO_FUNCAO2PARAMETRO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ 'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ 'EXPRESSAO_FUNCAO2PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ 'EXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': [ 'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['EXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': ['EXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [ 'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],

          #  '_EXPRESSAO_FUNCAO2PARAMETRO': [ '_EXPRESSAO_FUNCAO2PARAMETRO'],
     #   '_EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ '_EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ '_EXPRESSAO_FUNCAO2PARAMETRO_PARA'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ '_EXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': [ '_EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['_EXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_SE': ['_EXPRESSAO_FUNCAO2PARAMETRO_SE'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [ '_EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ '_EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['_EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['_EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],

 
        'ENQUANTO_EXPRESSAO' : ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'PARA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'REPITA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'REPITAMAIS_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': [ 'PARENTESES', 'REPITAMAIS_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['PARENTESES', 'SENAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': ['PARENTESES', 'SE_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': [ 'PARENTESES', 'ESCOLHA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': [ 'PARENTESES', 'OUTROCASO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['PARENTESES', 'FUNCAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['PARENTESES', 'PROCEDIMENTO_MAISEXPRESSAO'],


                
        'EXPRESSAO_FUNCAO2PARAMETRO': [ 'EXPRESSAO_FUNCAO2PARAMETRO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ 'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ 'EXPRESSAO_FUNCAO2PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ 'EXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': [ 'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['EXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': ['EXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [ 'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],

        
      #  '_EXPRESSAO_FUNCAO2PARAMETRO': [ '_EXPRESSAO_FUNCAO2PARAMETRO'],
     #   '_EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ '_EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ '_EXPRESSAO_FUNCAO2PARAMETRO_PARA'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ '_EXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': [ '_EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['_EXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_SE': ['_EXPRESSAO_FUNCAO2PARAMETRO_SE'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [ '_EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ '_EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['_EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
      #  '_EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['_EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],
        
        'ENQUANTO_EXPRESSAO' : ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'PARA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'REPITA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'REPITAMAIS_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': [ 'PARENTESES', 'REPITAMAIS_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['PARENTESES', 'SENAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': ['PARENTESES', 'SE_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': [ 'PARENTESES', 'ESCOLHA_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': [ 'PARENTESES', 'OUTROCASO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['PARENTESES', 'FUNCAO_MAISEXPRESSAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['PARENTESES', 'PROCEDIMENTO_MAISEXPRESSAO'],

        
        'EXPRESSAO_FUNCAO2PARAMETRO': [ 'EXPRESSAO_FUNCAO2PARAMETRO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ 'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ 'EXPRESSAO_FUNCAO2PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ 'EXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': [ 'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['EXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': ['EXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [ 'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],

        
     #   '_EXPRESSAO_FUNCAO2PARAMETRO': [ '_EXPRESSAO_FUNCAO2PARAMETRO'],
     #   '_EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ '_EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
    #    '_EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ '_EXPRESSAO_FUNCAO2PARAMETRO_PARA'],
     #   '_EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ '_EXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
     #   '_EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': [ '_EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
     #   '_EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['_EXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
     #   '_EXPRESSAO_FUNCAO2PARAMETRO_SE': ['_EXPRESSAO_FUNCAO2PARAMETRO_SE'],
     #   '_EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [ '_EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
     #   '_EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ '_EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
    #    '_EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['_EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
     #   '_EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['_EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],

        
        'ENQUANTO_EXPRESSAO' : ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'PARA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'REPITA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'REPITAMAIS_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS', 'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_SENAO', 'EXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_SE', 'EXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA', 'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO', 'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO', 'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO', 'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],

        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO', 'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_PARA', 'EXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS', 'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS', 'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_SENAO', 'EXPRESSAO_FUNCAO1PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_SE', 'EXPRESSAO_FUNCAO1PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA', 'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO', 'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO', 'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO', 'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO'],

    #    '_EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO', '_EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
   #     '_EXPRESSAO_FUNCAO2PARAMETRO_PARA': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_PARA', '_EXPRESSAO_FUNCAO2PARAMETRO_PARA'],
  #      '_EXPRESSAO_FUNCAO2PARAMETRO_REPITA': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS', '_EXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
   #     '_EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS', '_EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
    #    '_EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_SENAO', '_EXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
    #    '_EXPRESSAO_FUNCAO2PARAMETRO_SE': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_SE', '_EXPRESSAO_FUNCAO2PARAMETRO_SE'],
   #     '_EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA', '_EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
   #     '_EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO', '_EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
   #     '_EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO', 'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO', '_EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
    #    '_EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO', 'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO', '],
              
        'ENQUANTO_EXPRESSAO' : ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO', 'EXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'PARA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_PARA', 'EXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'REPITA_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_REPITA', 'EXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'REPITAMAIS_EXPRESSAO': ['ABRINDO_PARENTESES_FUNCAO1PARAMETRO','EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS', 'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'REPITAMAIS_EXPRESSAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHAR_PARENTESES_RANDI_REPITAMAIS'],
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
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_REPITAMAIS'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SENAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_SENAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_SE': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_SE'],
        'EXPRESSAO_FUNCAO1PARAMETRO_ESCOLHA': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_ESCOLHA'],
        'EXPRESSAO_FUNCAO1PARAMETRO_OUTROCASO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_OUTROCASO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_FUNCAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_FUNCAO'],
        'EXPRESSAO_FUNCAO1PARAMETRO_PROCEDIMENTO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_PROCEDIMENTO'],

        'EXPRESSAO_FUNCAO2PARAMETRO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_COMPLEMENTAR'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_ENQUANTO_COMPLEMENTAR'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PARA': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_PARA_COMPLEMENTAR'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITA': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_REPITA_COMPLEMENTAR'],
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_REPITAMAIS_COMPLEMENTAR'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_SENAO_COMPLEMENTAR'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_SE_COMPLEMENTAR'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_ESCOLHA_COMPLEMENTAR'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_OUTROCASO_COMPLEMENTAR'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_FUNCAO_COMPLEMENTAR'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['ABRIR_PARENTESES_RANDI', 'VALOR_INTEIRO/VARIAVEL', 'FECHA_PARENTESES_ESPECIAL_PROCEDIMENTO_COMPLEMENTAR'],
    },

    'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO': {
        # COMANDOS
        'COMANDOS': ['OP_ATRIB', 'EXPRESSAO'],
        'ATE_COMANDOS': ['OP_ATRIB', 'EXPRESSAO'],
        'REPITA_COMANDOS': ['OP_ATRIB', 'REPITA_EXPRESSAO'],
        'REPITAMAIS_COMANDOS': ['OP_ATRIB', 'REPITAMAIS_EXPRESSAO'],
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
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],

        'REPITA_EXPRESSAO': ['REPITA_MAISEXPRESSAO'],
        'REPITAMAIS_EXPRESSAO': ['REPITAMAIS_MAISEXPRESSAO'],
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
        'REPITAMAIS_MAISEXPRESSAO': ['OP_ATRIB', 'REPITAMAIS_EXPRESSAO'],
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
        'MAISATE_OPERANDO': [],
        'ATE_PARENTESES_OPERANDO': [],
        'OP_ARIT/OP_CARACTERE': [], 
        'OP_ARIT': [],

        'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO': [],

        'COMPARACAO': ['OP_REL'],
        'INICIO_COMPARACAO': ['OP_REL'],

        'ATE_EXPRESSAO': ['ATE_REL'],
        'ATE_MAISEXPRESSAO': ['ATE_REL'],

        'FIMREPITA': ['ATE_REL'],
        'MAISFIMREPITA': ['MAISATE_REL'],

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
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [ 'PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['PARENTESES', 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],

        
        'REPITA_EXPRESSAO': ['PARENTESES', 'REPITA_MAISEXPRESSAO'],
        'REPITAMAIS_EXPRESSAO': ['PARENTESES', 'REPITAMAIS_MAISEXPRESSAO'],
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

        'FIMREPITA': ['ATE_PARENTESES_EXPRESSAO', 'FECHAPARENTESES', 'ATE_COMANDOS'],

        'ATE_PARENTESES_EXPRESSAO': ['ATE_PARENTESES_EXPRESSAO', 'FECHAPARENTESES'],
        'ATE_PARENTESES_MAISEXPRESSAO': ['ATE_PARENTESES_EXPRESSAO', 'FECHAPARENTESES'],

        'ABREPARENTESES': [],

        'ABRINDO_PARENTESES_IMPORTANTE': [],

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
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': ['REPITAMAIS_MAISEXPRESSAO'],
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
        'FECHAR_PARENTESES_RANDI_SITUACAO2': ['FECHAPARENTESES'],
        
        'ALGO_TALVEZ':[],
        'MAISESCRITA': [],
        
        'MAISFUNCAO': ['OP_DELIMITACAO'],
        'MAISPROCEDIMENTO': [],

        'FECHAR_PARENTESES_RANDI': ['MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_ENQUANTO': ['ENQUANTO_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_PARA': ['PARA_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_REPITA': ['REPITA_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_REPITAMAIS': ['REPITAMAIS_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_SENAO': ['SENAO_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_SE': ['SE_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_ESCOLHA': ['ESCOLHA_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_OUTROCASO': ['OUTROCASO_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_FUNCAO': ['FUNCAO_MAISEXPRESSAO'],
        'FECHAR_PARENTESES_RANDI_PROCEDIMENTO': ['PROCEDIMENTO_MAISEXPRESSAO'],

        'FECHA_PARENTESES_ESPECIAL_COMPLEMENTAR': ['MAISEXPRESSAO_FUNCAO2PARAMETRO'],
        'FECHA_PARENTESES_ESPECIAL_ENQUANTO_COMPLEMENTAR': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_ENQUANTO'],
        'FECHA_PARENTESES_ESPECIAL_PARA_COMPLEMENTAR': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_PARA'],
        'FECHA_PARENTESES_ESPECIAL_REPITA_COMPLEMENTAR': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITA'],
        'FECHA_PARENTESES_ESPECIAL_REPITAMAIS_COMPLEMENTAR': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
        'FECHA_PARENTESES_ESPECIAL_SENAO_COMPLEMENTAR': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'FECHA_PARENTESES_ESPECIAL_SE_COMPLEMENTAR': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'FECHA_PARENTESES_ESPECIAL_ESCOLHA_COMPLEMENTAR': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'FECHA_PARENTESES_ESPECIAL_OUTROCASO_COMPLEMENTAR': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'FECHA_PARENTESES_ESPECIAL_FUNCAO_COMPLEMENTAR': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'FECHA_PARENTESES_ESPECIAL_PROCEDIMENTO_COMPLEMENTAR': ['MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],


        'FECHA_PARENTESES_ESPECIAL': ['MAISEXPRESSAO_FUNCAO1PARAMETRO'],
        'FECHA_PARENTESES_ESPECIAL_ENQUANTO': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_ENQUANTO'],
        'FECHA_PARENTESES_ESPECIAL_PARA': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_PARA'],
        'FECHA_PARENTESES_ESPECIAL_REPITA': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITA'],
        'FECHA_PARENTESES_ESPECIAL_REPITAMAIS': ['MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],
       
        
        'REPITA_EXPRESSAO': ['REPITA_MAISEXPRESSAO'],
        'REPITAMAIS_EXPRESSAO': ['REPITAMAIS_MAISEXPRESSAO'],
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
        'MAISATE_OPERANDO': [],
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
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],
        
        'REPITA_EXPRESSAO': ['REPITA_MAISEXPRESSAO'],
        'REPITAMAIS_EXPRESSAO': ['REPITAMAIS_MAISEXPRESSAO'],
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
        'MAISATE_OPERANDO': [],
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
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],
        
        'REPITA_EXPRESSAO': ['REPITA_MAISEXPRESSAO'],
        'REPITAMAIS_EXPRESSAO': ['REPITAMAIS_MAISEXPRESSAO'],
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
        'MAISATE_OPERANDO': [],
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
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],
        
        'REPITA_EXPRESSAO': ['REPITA_MAISEXPRESSAO'],
        'REPITAMAIS_EXPRESSAO': ['REPITAMAIS_MAISEXPRESSAO'],
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
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],
        
        'REPITA_EXPRESSAO': ['REPITA_MAISEXPRESSAO'],
        'REPITAMAIS_EXPRESSAO': ['REPITAMAIS_MAISEXPRESSAO'],
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
        'EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': [ 'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SENAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_SE': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': [  'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': [ 'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],

        
        'REPITA_EXPRESSAO': ['REPITA_MAISEXPRESSAO'],
        'REPITAMAIS_EXPRESSAO': ['REPITAMAIS_MAISEXPRESSAO'],
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
        'MAISATE_OPERANDO': [],
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
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': ['EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': ['EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['EXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE': ['EXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': ['EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': ['EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],
        
        'REPITA_MAISEXPRESSAO': ['REPITA_EXPRESSAO'],
        'REPITAMAIS_MAISEXPRESSAO': ['REPITAMAIS_EXPRESSAO'],
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
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': ['EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': ['EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['EXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE': ['EXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': ['EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': ['EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],


        
        'REPITA_MAISEXPRESSAO': ['REPITA_EXPRESSAO'],
        'REPITAMAIS_MAISEXPRESSAO': ['REPITAMAIS_EXPRESSAO'],
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
        'MAISEXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS': ['EXPRESSAO_FUNCAO1PARAMETRO_REPITAMAIS'],
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
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS': ['EXPRESSAO_FUNCAO2PARAMETRO_REPITAMAIS'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_SENAO': ['EXPRESSAO_FUNCAO2PARAMETRO_SENAO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_SE': ['EXPRESSAO_FUNCAO2PARAMETRO_SE'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA': ['EXPRESSAO_FUNCAO2PARAMETRO_ESCOLHA'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO': ['EXPRESSAO_FUNCAO2PARAMETRO_OUTROCASO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_FUNCAO': ['EXPRESSAO_FUNCAO2PARAMETRO_FUNCAO'],
        'MAISEXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO': ['EXPRESSAO_FUNCAO2PARAMETRO_PROCEDIMENTO'],

        'REPITA_MAISEXPRESSAO': ['REPITA_EXPRESSAO'],
        'REPITAMAIS_MAISEXPRESSAO': ['REPITAMAIS_EXPRESSAO'],
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
        'REPITAMAIS_MAISEXPRESSAO': ['REPITAMAIS_EXPRESSAO'],
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
        'REPITAMAIS_MAISEXPRESSAO': ['REPITAMAIS_EXPRESSAO'],
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
        'REPITAMAIS_MAISEXPRESSAO': ['REPITAMAIS_EXPRESSAO'],
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
        'REPITAMAIS_COMANDOS': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'REPITAMAIS_COMANDOS'],
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
        'REPITAMAIS_MAISEXPRESSAO': ['ABREPARENTESES', 'VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'FECHAPARENTESES', 'REPITAMAIS_COMANDOS'],
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
        'REPITAMAIS_COMANDOS': ['ABREPARENTESES', 'ESCRITA', 'REPITAMAIS_COMANDOS'],
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
        'REPITAMAIS_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA', 'REPITAMAIS_COMANDOS'],
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
        'REPITAMAIS_COMANDOS': ['ABREPARENTESES', 'ESCRITA',  'REPITAMAIS_COMANDOS'],
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
        'REPITAMAIS_MAISEXPRESSAO': ['ABREPARENTESES', 'ESCRITA',  'REPITAMAIS_COMANDOS'],
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
        'REPITAMAIS_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'REPITAMAIS_COMANDOS'],
        'SE_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'SE_COMANDOS'],
        'SENAO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'SENAO_COMANDOS'],
        'PARA_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'PARA_COMANDOS'],
        'ENQUANTO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'ENQUANTO_COMANDOS'],
        'ESCOLHA_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'ESCOLHA_COMANDOS'],
        'OUTROCASO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'OUTROCASO_COMANDOS'],
        'FUNCAO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'PROCEDIMENTO_COMANDOS'],

        'MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'COMANDOS'],
        'REPITA_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'REPITA_COMANDOS'],
        'REPITAMAIS_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'REPITAMAIS_COMANDOS'],
        'SE_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'SE_COMANDOS'],
        'SENAO_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'SENAO_COMANDOS'],
        'PARA_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'PARA_COMANDOS'],
        'ENQUANTO_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'ENQUANTO_COMANDOS'],
        'ESCOLHA_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'ESCOLHA_COMANDOS'],
        'OUTROCASO_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'OUTROCASO_COMANDOS'],
        'FUNCAO_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'FUNCAO_COMANDOS'],
        'PROCEDIMENTO_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'DE', 'VALOR_INT', 'PARA_ATE', 'VALOR_INT', 'FACA_PASSO', 'PARA_COMANDOS', 'PROCEDIMENTO_COMANDOS'],
    },

    'ATE': {
        'PARA_ATE': [],

        'REPITA_COMANDOS': ['ATE_EXPRESSAO'],
        'REPITA_MAISEXPRESSAO': ['ATE_EXPRESSAO'],

        'REPITAMAIS_COMANDOS': [],
        'REPITAMAIS_MAISEXPRESSAO': [],

        'ATE_COMANDOS': ['ATE_EXPRESSAO'],
        'ATE_MAISEXPRESSAO': ['ATE_EXPRESSAO'],

        'FIMREPITA': ['ATE_EXPRESSAO'],
        'MAISFIMREPITA': [],
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
        'ATE_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'ATE_COMANDOS'],
        'REPITA_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'REPITA_COMANDOS'],
        'REPITAMAIS_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'REPITAMAIS_COMANDOS'],
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
        'REPITAMAIS_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'ENQUANTO_COMANDOS', 'REPITAMAIS_COMANDOS'],
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
        'REPITAMAIS_COMANDOS': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'REPITAMAIS_COMANDOS'],
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
        'REPITAMAIS_MAISEXPRESSAO': ['VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO', 'CASO', 'VALOR_ESCOLHA', 'ESCOLHA_COMANDOS', 'REPITAMAIS_COMANDOS'],
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
        'REPITAMAIS_COMANDOS': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'REPITAMAIS_COMANDOS'],
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
        'REPITAMAIS_MAISEXPRESSAO': ['COMPARACAO', 'MAISCOMPARACAO', 'SE_COMANDOS', 'REPITAMAIS_COMANDOS'],
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
        'REPITA_COMANDOS': ['REPITAMAIS_COMANDOS', 'FIMREPITA'],
        'REPITAMAIS_COMANDOS': ['REPITAMAIS_COMANDOS', 'MAISFIMREPITA'],
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
        'FIMREPITA': ['COMANDOS'],
        'MAISFIMREPITA': [],

        'REPITAMAIS_COMANDOS': [],
        'REPITAMAIS_MAISEXPRESSAO': [],

        'REPITA_COMANDOS': [],
        'REPITA_MAISEXPRESSAO': [],

        'ATE_COMANDOS': ['ATE_COMANDOS']
    },

    # INTERROMPA

    'INTERROMPA': { 
        'COMANDOS': ['COMANDOS'],
        'ATE_COMANDOS': ['COMANDOS'],
        'REPITA_COMANDOS': ['REPITA_COMANDOS'],
        'REPITAMAIS_COMANDOS': ['REPITAMAIS_COMANDOS'], 
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
        'REPITAMAIS_MAISEXPRESSAO': ['REPITAMAIS_COMANDOS'],
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
        'REPITAMAIS_COMANDOS': ['REPITAMAIS_EXPRESSAO'],
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
        'REPITAMAIS_MAISEXPRESSAO':  ['REPITAMAIS_EXPRESSAO'],
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

def semantico(tabela_simbolos):
    manterVariavel = []

    resultadoSemantico = ""
    aux = "" #Variável auxiliar
    atribuicao = ""
    #manterTipo = ""
    contador = 0
    tabela_simbolos2 = []
    tabela_simbolos3 = copy.deepcopy(tabela_simbolos)
    #compilarLexico()
    area_resultado.config(state=tk.NORMAL)
    area_resultado.delete("1.0", tk.END)
    for simbolo in tabela_simbolos:
    #area_resultado.insert(tk.END, f"{simbolo[0]}: {simbolo[1]}\n")
    #variavelSemantico = simbolo[0]

                
        if((contador == 1 or contador == 2) and simbolo[0] != "," and simbolo[0] != ":"):
            manterVariavel.append(simbolo[0])
            contador = 2

        if(contador == 3):
            if(simbolo[0] == "inteiro" or simbolo[0] == "real" or simbolo[0] == "caractere" or simbolo[0] == "logico"):
                contador = 0
                manterTipo = simbolo[0]
                
                for i in manterVariavel:
                    for j in tabela_simbolos2:
                        if(i in j[0]):
                            #3) Se não houve a redefinição de tipo de uma variável
                            resultadoSemantico += "\nRecusado:\nVariável redefinida: " + i
                            break
                    tabela_simbolos2.append([i, manterTipo])
                manterVariavel = [ ]


        if(contador == 2 and simbolo[0] == ":"):
            contador = 3
      
        if(contador == 0 and simbolo[0] == "var"):
            contador = 1

        if(simbolo[0] == "inicio"):
            contador = 4

        if(contador == 4 and simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"):
            tipoVariavel = simbolo[1]    
            for j in tabela_simbolos2:
                if(simbolo[0] in j):
                    aux = "Ok"    
            if(aux == ""):
                #1) Se uma variável foi definida
                resultadoSemantico += "\nRecusado:\nVariável não definida: " + simbolo[0]
            aux = ""
    contadorAux = 0
    contadorAux2 = 0
    anteriorOperando = ""
    atualOperando = ""
    tipo = ""
    tipo2 = ""
    naoinicio = 0
    correto = ""
    tipo3 = ""
    listaPosicoes = [ ] 
    contandoPosicao = 0
    Posicao = 0
    primeiraAtribuicao = 0
    for simbolo in tabela_simbolos:
        contandoPosicao = contandoPosicao + 1
        
        if(primeiraAtribuicao == 1 and simbolo[0] != "<-" and simbolo[1] != "OP_ARIT" and simbolo[1] != "OP_ARIT/OP_CARACTERE" and simbolo[1] != "MOD" 
            and simbolo[1] != "ABRE_PARENTESES" and simbolo[1] != "FECHA_PARENTESES" and simbolo[1] != "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"
            and simbolo[1] != "VALOR_INT" and simbolo[1] != "ABS" and simbolo[1] != "RAIZQ" and simbolo[1] != "RANDI" and simbolo[1] != "EXP" and simbolo[1] != "QUAD"
            and simbolo[1] != "NOME_ALGORITMO/VALOR_LITERAL" and simbolo[1] != "VALOR_LITERAL" and simbolo[1] != "VERDADEIRO" and simbolo[1] != "FALSO" and simbolo[1] != "VALOR_REAL"
            and simbolo[1] != "E" and simbolo[1] != "XOU" and simbolo[1] != "OU" and simbolo[1] != "NAO" and simbolo[1] != "OP_SEP_DIFERENTE_TIPO" and simbolo[1] != "OP_SEP_MESMO_TIPO"):
            Posicao = contandoPosicao - 1
            tabela_simbolos3.insert(Posicao, ["---", "---"])
            listaPosicoes.append(Posicao)
            contandoPosicao = contandoPosicao + 1
            primeiraAtribuicao = 0
        if(primeiraAtribuicao == 1 and simbolo[0] == "<-"):
            Posicao = contandoPosicao - 2
            tabela_simbolos3.insert(Posicao, ["---", "---"]) #Não pode ser ["", ""], 
            listaPosicoes.append(Posicao)
            contandoPosicao = contandoPosicao + 1
            primeiraAtribuicao = 0
        if(primeiraAtribuicao == 0 and simbolo[0] == "<-"):
            primeiraAtribuicao = 1

    #2) Se o tipo da variável é condizente com a operação  na atribuição ( se a variável é inteira então deverá receber um valor inteiro, se for real um valor real)        
    for simbolo in tabela_simbolos3:
        if(simbolo[0] == "inicio" and contador == 4):
            contador = 5
        if(contador == 5):
            if(simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"):
                for j in tabela_simbolos2:
                    if(simbolo[0] in j):
                        variavel = simbolo[0]
                        tipo = j[1]
        if(simbolo[0] == "<-"):
            contador = 6
        if(contador == 6 and tipo == "inteiro" and 
            ( simbolo[1] == "RAIZQ" or  simbolo[1] == "EXP"  
            or simbolo[1] == "NOME_ALGORITMO/VALOR_LITERAL" or simbolo[1] == "VALOR_LITERAL" or simbolo[1] == "VERDADEIRO" or simbolo[1] == "FALSO" or simbolo[1] == "VALOR_REAL"
            or simbolo[1] == "E" or simbolo[1] == "OU" or simbolo[1] == "XOU" or simbolo[1] == "NAO"
                )
            ):
            resultadoSemantico += "\nRecusado:\nEsperado valor inteiro,  erro na atribuição para variável: " + variavel + ", erro em: " + simbolo[0]
        if(contador == 6 and tipo == "inteiro" and  simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"):
            for j in tabela_simbolos2:
                    if(simbolo[0] in j):
                        tipo2 = j[1]
                        if(tipo2 != "inteiro"):
                            resultadoSemantico += "\nRecusado:\nEsperado valor inteiro,  erro na atribuição para variável: " + variavel + ", erro em: " + simbolo[0]
                            
    
        if(contador == 6 and tipo == "logico" and 
            ( simbolo[1] == "RAIZQ" or  simbolo[1] == "EXP" or simbolo[1] == "RANDI" or simbolo[1] == "ABS" or simbolo[1] == "QUAD" or
                simbolo[1] == "OP_ARIT" or simbolo[1] == "OP_ARIT/OP_CARACTERE" or simbolo[1] == "MOD" or
            simbolo[1] == "NOME_ALGORITMO/VALOR_LITERAL" or simbolo[1] == "VALOR_LITERAL" or simbolo[1] == "VALOR_REAL" or simbolo[1] == "VALOR_INT"
                )
            ):
            resultadoSemantico += "\nRecusado:\nEsperado valor logico,  erro na atribuição para variável: " + variavel + ", erro em: " + simbolo[0]
        if(contador == 6 and tipo == "logico" and  simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"):
            for j in tabela_simbolos2:
                    if(simbolo[0] in j):
                        tipo2 = j[1]
                        if(tipo2 != "logico"):
                            resultadoSemantico += "\nRecusado:\nEsperado valor logico,  erro na atribuição para variável: " + variavel + ", erro em: " + simbolo[0]
                      


        if(contador == 6 and tipo == "real" and 
            ( simbolo[1] == "NOME_ALGORITMO/VALOR_LITERAL" or simbolo[1] == "VALOR_LITERAL" 
            or simbolo[1] == "E" or simbolo[1] == "OU" or simbolo[1] == "XOU" or simbolo[1] == "NAO" or simbolo[1] == "VERDADEIRO" or simbolo[1] == "FALSO"
                )
            ):
            resultadoSemantico += "\nRecusado:\nEsperado valor real,  erro na atribuição para variável: " + variavel + ", erro em: " + simbolo[0]
        if(contador == 6 and tipo == "real" and simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"):
            for j in tabela_simbolos2:
                    if(simbolo[0] in j):
                        tipo2 = j[1]
                        if(tipo2 != "real" and tipo2 != "inteiro"):
                            resultadoSemantico += "\nRecusado:\nEsperado valor real, erro na atribuição para variável: " + variavel + ", erro em: " + simbolo[0]
                           


        if(contador == 6 and tipo == "caractere" and 
            (simbolo[1] == "E" or simbolo[1] == "OU" or simbolo[1] == "XOU" or simbolo[1] == "NAO" or simbolo[1] == "VERDADEIRO" or simbolo[1] == "FALSO"
                or simbolo[1] == "VALOR_REAL" or simbolo[1] == "VALOR_INT" or simbolo[1] == "OP_ARIT" or simbolo[1] == "MOD" or simbolo[1] == "RAIZQ" or
                simbolo[1] == "EXP" or simbolo[1] == "RANDI" or simbolo[1] == "ABS" or simbolo[1] == "QUAD"
                )
            ):
            resultadoSemantico += "\nRecusado:\nEsperado valor do tipo caractere, erro na atribuição para variável: " + variavel + ", erro em: " + simbolo[0]
        if(contador == 6 and tipo == "caractere" and simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"):
            for j in tabela_simbolos2:
                    if(simbolo[0] in j):
                        tipo2 = j[1]
                        if(tipo2 != "caractere"):
                            resultadoSemantico += "\nRecusado:\nEsperado valor do tipo caractere, erro na atribuição para variável: " + variavel + ", erro em: " + simbolo[0]     
                                
        if(contador == 6 and simbolo[1] == "---" and simbolo[0] == "---"):
            contador = 5
            tipo = ""
            tipo2 = ""
                            
               
        
      
                            
         
            
          
    area_resultado.config(state=tk.DISABLED)


      


    if(resultadoSemantico == ""):
        resultadoSemantico = "Aceito"
    

    area_resultado.config(state=tk.NORMAL)
    area_resultado.delete("1.0", tk.END)
    area_resultado.insert(tk.END, f"Resultado: {resultadoSemantico}")
    area_resultado.config(state=tk.DISABLED)

    return resultadoSemantico

   
        
    

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

     #Exibir resultado na área de saída
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

    resultadoSemantico = ""
    #Semantico
    if(resultado == "aceito."):
        resultadoSemantico = semantico(tabela_simbolos)
    if(resultadoSemantico == "Aceito"):
        geradorDeCodigo()
        area_resultado.config(state=tk.NORMAL)
        area_resultado.delete("1.0", tk.END)
        area_resultado.insert(tk.END, f"Resultado: {resultadoSemantico}")
        area_resultado.config(state=tk.DISABLED)

    
    
        

def compilarLexicoESemantico():
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

        
    semantico(tabela_simbolos)


def geradorDeCodigo():
    tabela_simbolos = compilarLexico()  # Gera a tabela de símbolos a partir do léxico
    if tabela_simbolos is None:
        return
    
    # Cria uma cadeia de entrada para o sintático a partir dos tipos dos tokens
    #cadeia = [simbolo[1] for simbolo in tabela_simbolos] # List Comprehension
    
    #resultado = sintatico(cadeia)

    algoritmo = ""

    # Exibir o resultado
    
    auxAlgoritmo = 0
    auxVariavel = 0
    texto_sem_aspas = ""
    tabela_simbolos3 = copy.deepcopy(tabela_simbolos)
    listaPosicoes = [ ] 
    contandoPosicao = 0
    Posicao = 0
    primeiraAtribuicaoOuFuncaoOuProcedimento = 0
    primeiroVar = 0
    primeiroRetorne = 0
    primeiroCaso = 0

    manterVariavel = [ ]
    tabela_simbolos2 = [ ]
    simboloAnterior = ""
    contadorRegulador = 0
    dentroDeAlgoritmo = 0
    for simbolo in tabela_simbolos:
    #area_resultado.insert(tk.END, f"{simbolo[0]}: {simbolo[1]}\n")
    #variavelSemantico = simbolo[0]

        if(simbolo[0] == "algoritmo"):
            dentroDeAlgoritmo = 1
                
        if((contadorRegulador == 1 or contadorRegulador == 2) and simbolo[0] != "," and simbolo[0] != ":" and dentroDeAlgoritmo == 1):
            manterVariavel.append(simbolo[0])
            contadorRegulador = 2

        if(contadorRegulador == 3):
            if((simbolo[0] == "inteiro" or simbolo[0] == "real" or simbolo[0] == "caractere" or simbolo[0] == "logico") and dentroDeAlgoritmo == 1):
                contadorRegulador = 0
                manterTipo = simbolo[0]
                
                for i in manterVariavel:
                    tabela_simbolos2.append([i, manterTipo])
                manterVariavel = [ ]

        
        if(contadorRegulador == 2 and simbolo[0] == ":" and dentroDeAlgoritmo == 1):
            contadorRegulador = 3
      
        if(contadorRegulador == 0 and simbolo[0] == "var" and dentroDeAlgoritmo == 1):
            contadorRegulador = 1

        if(simbolo[0] == "inicio" and dentroDeAlgoritmo == 1):
            contadorRegulador = 4

    
    for simbolo in tabela_simbolos:
        contandoPosicao = contandoPosicao + 1
        if(primeiraAtribuicaoOuFuncaoOuProcedimento == 1 and simbolo[0] != "<-" and simbolo[1] != "OP_ARIT" and simbolo[1] != "OP_ARIT/OP_CARACTERE" and simbolo[1] != "MOD" 
            and simbolo[1] != "ABRE_PARENTESES" and simbolo[1] != "FECHA_PARENTESES" and simbolo[1] != "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"
            and simbolo[1] != "VALOR_INT" and simbolo[1] != "ABS" and simbolo[1] != "RAIZQ" and simbolo[1] != "RANDI" and simbolo[1] != "EXP" and simbolo[1] != "QUAD"
            and simbolo[1] != "NOME_ALGORITMO/VALOR_LITERAL" and simbolo[1] != "VALOR_LITERAL" and simbolo[1] != "VERDADEIRO" and simbolo[1] != "FALSO" and simbolo[1] != "VALOR_REAL"
            and simbolo[1] != "E" and simbolo[1] != "XOU" and simbolo[1] != "OU" and simbolo[1] != "NAO" and simbolo[1] != "OP_SEP_DIFERENTE_TIPO" and simbolo[1] != "OP_SEP_MESMO_TIPO"):
            Posicao = contandoPosicao - 1
            tabela_simbolos3.insert(Posicao, ["---", "---"])
            listaPosicoes.append(Posicao)
            contandoPosicao = contandoPosicao + 1
            primeiraAtribuicaoOuFuncaoOuProcedimento = 0
        if(primeiraAtribuicaoOuFuncaoOuProcedimento == 1 and simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO" and (simboloAnterior == "FECHA_PARENTESES" or
                                                                                                       simboloAnterior == "VERDADEIRO" or simboloAnterior == "NOME_ALGORITMO/VALOR_LITERAL"
                                                                                                       or simboloAnterior == "FALSO" or simboloAnterior == "VALOR_REAL" or
                                                                                                       simboloAnterior == "VALOR_INT" or simboloAnterior == "VALOR_LITERAL" or
                                                                                                       simboloAnterior == "OP_SEP_DIFERENTE_TIPO" or simboloAnterior == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO")):   
            Posicao = contandoPosicao - 1
            tabela_simbolos3.insert(Posicao, ["---", "---"]) #Não pode ser ["", ""], 
            listaPosicoes.append(Posicao)
            contandoPosicao = contandoPosicao + 1
            primeiraAtribuicaoOuFuncaoOuProcedimento = 0
        if(primeiraAtribuicaoOuFuncaoOuProcedimento == 0  and simbolo[0] == "<-" or ( ( ( simboloAnterior == "FECHA_PARENTESES"  or simboloAnterior == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO" or
                                                              simboloAnterior == "VERDADEIRO" or simboloAnterior == "NOME_ALGORITMO/VALOR_LITERAL"
                                                                                                       or simboloAnterior == "FALSO" or simboloAnterior == "VALOR_REAL" or
                                                                                                       simboloAnterior == "VALOR_INT" or simboloAnterior == "VALOR_LITERAL" 
                                                                                                        ) or ( simboloAnterior != "<-" and simboloAnterior != "OP_ARIT"
                                                                                                                                                         and simboloAnterior != "OP_ARIT/OP_CARACTERE" and
                                                                                                                                                         simboloAnterior != "MOD" and simboloAnterior != "ABRE_PARENTESES"  
            and simboloAnterior != "ABS" and simboloAnterior != "RAIZQ" and simboloAnterior != "RANDI" and simboloAnterior != "EXP" and simboloAnterior != "QUAD"
                                                            and simboloAnterior != "OP_REL"
                                                                                                               and simboloAnterior != "PARA"
                                                                                                                    and simboloAnterior != "DE"
                                                                                                               and simboloAnterior != "ATE"
                                                                                                               and simboloAnterior != "SE"
                                                                                                               and simboloAnterior != "ENQUANTO"
                                                                                                               and simboloAnterior != "CASO"
                                                                                                               and simboloAnterior != "ESCOLHA"
            and simboloAnterior != "E" and simboloAnterior != "XOU" and simboloAnterior != "OU" and simboloAnterior != "NAO" and simboloAnterior != "OP_SEP_DIFERENTE_TIPO" and simboloAnterior != "OP_SEP_MESMO_TIPO") )
            and simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"
                                                              )):
            primeiraAtribuicaoOuFuncaoOuProcedimento = 1
 

        
            
        if(primeiroVar == 1 and simbolo[0] == "var"):
             Posicao = contandoPosicao - 1
             tabela_simbolos3.insert(Posicao, ["---", "---"])
             listaPosicoes.append(Posicao)
             contandoPosicao = contandoPosicao + 1
             primeiroVar = 0
        if(primeiroVar == 0 and simbolo[0] == "var"):
            primeiroVar = 1
        if(primeiroRetorne == 1 and simbolo[0] != "<-" and simbolo[1] != "OP_ARIT" and simbolo[1] != "OP_ARIT/OP_CARACTERE" and simbolo[1] != "MOD" 
            and simbolo[1] != "ABRE_PARENTESES" and simbolo[1] != "FECHA_PARENTESES" and simbolo[1] != "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"
            and simbolo[1] != "VALOR_INT" and simbolo[1] != "ABS" and simbolo[1] != "RAIZQ" and simbolo[1] != "RANDI" and simbolo[1] != "EXP" and simbolo[1] != "QUAD"
            and simbolo[1] != "NOME_ALGORITMO/VALOR_LITERAL" and simbolo[1] != "VALOR_LITERAL" and simbolo[1] != "VERDADEIRO" and simbolo[1] != "FALSO" and simbolo[1] != "VALOR_REAL"
            and simbolo[1] != "E" and simbolo[1] != "XOU" and simbolo[1] != "OU" and simbolo[1] != "NAO" and simbolo[1] != "OP_SEP_DIFERENTE_TIPO" and simbolo[1] != "OP_SEP_MESMO_TIPO"):
            Posicao = contandoPosicao - 1
            tabela_simbolos3.insert(Posicao, ["---", "---"])
            listaPosicoes.append(Posicao)
            contandoPosicao = contandoPosicao + 1
            primeiroRetorne = 0

        if(primeiroRetorne == 1 and simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO" and (simboloAnterior == "FECHA_PARENTESES" or
                                                                                                       simboloAnterior == "VERDADEIRO" or simboloAnterior == "NOME_ALGORITMO/VALOR_LITERAL"
                                                                                                       or simboloAnterior == "FALSO" or simboloAnterior == "VALOR_REAL" or
                                                                                                       simboloAnterior == "VALOR_INT" or simboloAnterior == "VALOR_LITERAL" or
                                                                                                       simboloAnterior == "OP_SEP_DIFERENTE_TIPO" or simboloAnterior == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO")):
            Posicao = contandoPosicao - 1
            tabela_simbolos3.insert(Posicao, ["---", "---"]) 
            listaPosicoes.append(Posicao)
            contandoPosicao = contandoPosicao + 1
            primeiroRetorne = 0
        
        if(primeiroRetorne == 0 and simbolo[0] == "retorne"):
            primeiroRetorne = 1
        if(primeiroCaso == 1 and simbolo[0] != "<-" and simbolo[1] != "OP_ARIT" and simbolo[1] != "OP_ARIT/OP_CARACTERE" and simbolo[1] != "MOD" 
            and simbolo[1] != "ABRE_PARENTESES" and simbolo[1] != "FECHA_PARENTESES" and simbolo[1] != "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"
            and simbolo[1] != "VALOR_INT" and simbolo[1] != "ABS" and simbolo[1] != "RAIZQ" and simbolo[1] != "RANDI" and simbolo[1] != "EXP" and simbolo[1] != "QUAD"
            and simbolo[1] != "NOME_ALGORITMO/VALOR_LITERAL" and simbolo[1] != "VALOR_LITERAL" and simbolo[1] != "VERDADEIRO" and simbolo[1] != "FALSO" and simbolo[1] != "VALOR_REAL"
            and simbolo[1] != "E" and simbolo[1] != "XOU" and simbolo[1] != "OU" and simbolo[1] != "NAO" and simbolo[1] != "OP_SEP_DIFERENTE_TIPO" and simbolo[1] != "OP_SEP_MESMO_TIPO"):
            Posicao = contandoPosicao - 1
            tabela_simbolos3.insert(Posicao, ["-----", "-----"])
            listaPosicoes.append(Posicao)
            contandoPosicao = contandoPosicao + 1
            primeiroCaso = 0
        if(primeiroCaso == 1 and simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO" and (simboloAnterior == "FECHA_PARENTESES" or
                                                                                                       simboloAnterior == "VERDADEIRO" or simboloAnterior == "NOME_ALGORITMO/VALOR_LITERAL"
                                                                                                       or simboloAnterior == "FALSO" or simboloAnterior == "VALOR_REAL" or
                                                                                                       simboloAnterior == "VALOR_INT" or simboloAnterior == "VALOR_LITERAL" or
                                                                                                       simboloAnterior == "OP_SEP_DIFERENTE_TIPO" or simboloAnterior == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO")):
            Posicao = contandoPosicao - 1
            tabela_simbolos3.insert(Posicao, ["-----", "-----"]) 
            listaPosicoes.append(Posicao)
            
                
            contandoPosicao = contandoPosicao + 1
            primeiroCaso = 0
            
        
            
                                                                                                
        if(primeiroCaso == 0 and simbolo[0] == "caso"):
            primeiroCaso = 1
        simboloAnterior = simbolo[1]
            

    algoritmoFinal = ""
    tipoDaVariavel = ""
    variavelDeclarada = ""
    formarDeclaracao = ""
    iniciou = 0
    novoFor = 0
    manterVariavelFor = ""
    manterVariavel2For = ""
    manterVariavel3For = ""
    passoOuNao = 0
    estaEmFor = 0
    ateRepita = 0
    ateFor = 0
    valorAnterior = ""
    primeiroValor = 0
    primeiroValorAux = 0
    algoritmoAuxPrimeiroValor = ""
    facaEnquanto = 0
    escrita = 0
    #Indicar se precisará acrescentar biblioteca import java.util.Random;
    TemRandi = 0
    algoritmoIntermediario = ""
    algoritmoIntermediario2 = ""
    algoritmoIntermediario3 = ""
    positivoOuNao = ""
    novoEscolha = 0
    contarParenteses = 0
    listaParenteses = []
    quantosParenteses = 0
    quantosQuad = 0

    lendoValor = 0
    verTipo = ""
    FuncaoSim = 0
    FuncaoDeclaracao = 0
    irMantendo = ""
    irMantendoMelhor = ""
    verTipoFuncao = 0
    TemParametros = 0
    tipoDaFuncao = ""
    tipoDaVariavelDaFuncaoPresente = 0
    algoritmoFinalParteFuncaoOuProcedimento = ""
    nomeDaFuncao = ""
    regularDeclaracaoFuncao = 0
    adicionarParenteses = 0

    regularDeclaracaoProcedimento = 0
    ProcedimentoSim = 0
    ProcedimentoDeclaracao = 0
    nomeDoProcedimento = ""
    tipoDaVariavelDoProcedimentoPresente = 0
    for simbolo in tabela_simbolos3:
        if(primeiroValor == 1 and algoritmoAuxPrimeiroValor == ""):
            primeiroValor = 0
        if(primeiroValor == 0 and ateRepita == 1 and ( simbolo[0] == "FALSO" or simbolo[0] == "VERDADEIRO" )):
            primeiroValor = 1
        if(primeiroValor == 0 and ateRepita == 1 and simbolo[0] != "FALSO" and simbolo[0] != "VERDADEIRO" ):
            primeiroValorAux = 1
        if(simbolo[0] == "funcao"):
            FuncaoSim = 1
            FuncaoDeclaracao = 1

        if(simbolo[0] == "procedimento"):
            ProcedimentoSim = 1
            ProcedimentoDeclaracao = 1

        if(ProcedimentoSim == 1 and ProcedimentoDeclaracao == 1 and simbolo[0] != "procedimento"):
            if(simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO" and TemParametros == 0):
                nomeDoProcedimento = simbolo[0]
            if(simbolo[0] == "("):
                TemParametros = 1
                irMantendoMelhor += " " + "(" + " "
                irMantendo = ""
            if(simbolo[0] == ";" and TemParametros == 1):
                irMantendoMelhor += ","
            elif(simbolo[0] == "var" and TemParametros == 1):
                irMantendo += ""
            elif((simbolo[0] == "---" or simbolo[0] == "(") and TemParametros == 1):
                irMantendo += ""
            elif(simbolo[0] == ":" and TemParametros == 1):
                irMantendo += ""
                tipoDaVariavelDoProcedimentoPresente = 1
            elif(TemParametros == 1 and  tipoDaVariavelDoProcedimentoPresente == 0 and simbolo[0] != ")" and simbolo[0] != ":"):
                irMantendo += " " + simbolo[0] + " "
            if(simbolo[0] == "var" or simbolo[0] == "inicio" and TemParametros == 0 ):
                algoritmoFinalParteFuncaoOuProcedimento += "static void " + nomeDoProcedimento + "( )\n"
                ProcedimentoDeclaracao = 0
            if(tipoDaVariavelDoProcedimentoPresente == 1  and simbolo[0] != ")" and (simbolo[0] == "inteiro" or simbolo[0] == "real" or simbolo[0] == "logico" or simbolo[0] == "caractere" )):
                palavras = irMantendo.split()
                for palavra in palavras:
                    if(simbolo[0] == "inteiro" and palavra != ","):
                        irMantendoMelhor += " int " + palavra
                    if(simbolo[0] == "real" and palavra != ","):
                        irMantendoMelhor += " double " + palavra
                    if(simbolo[0] == "caractere" and palavra != ","):
                        irMantendoMelhor += " String " + palavra
                    if(simbolo[0] == "logico" and palavra != ","):
                        irMantendoMelhor += " boolean " + palavra
                    if(palavra == ","):
                        irMantendoMelhor += ", "    
                tipoDaVariavelDoProcedimentoPresente = 0
                irMantendo = ""
            if(simbolo[0] == ")"):
                irMantendoMelhor += " ) "
                algoritmoFinalParteFuncaoOuProcedimento += "static void " + nomeDoProcedimento + " " + irMantendoMelhor
                irMantendoMelhor = ""
                irMantendo = ""
                nomeDoProcedimento = ""
                ProcedimentoDeclaracao = 0
                tipoDaVariavelDoProcedimentoPresente = 0
                TemParametros = 0

                
        if(FuncaoSim == 1 and FuncaoDeclaracao == 1 and simbolo[0] != "funcao"):
            if(simbolo[0] == ":" and TemParametros == 0):
                verTipoFuncao = 1
                adicionarParenteses = 1
            if(simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO" and TemParametros == 0):
                nomeDaFuncao = simbolo[0]
            if(simbolo[0] == "("):
                TemParametros = 1
                irMantendoMelhor += " " + "(" + " "
                irMantendo = ""
            if(simbolo[0] == ";" and TemParametros == 1):
                irMantendoMelhor += ","
            elif(simbolo[0] == "var" and TemParametros == 1):
                irMantendo += ""
            elif((simbolo[0] == "---" or simbolo[0] == "(") and TemParametros == 1):
                irMantendo += ""
            elif(simbolo[0] == ":" and TemParametros == 1 and verTipoFuncao == 0):
                irMantendo += ""
                tipoDaVariavelDaFuncaoPresente = 1
            elif(TemParametros == 1 and  tipoDaVariavelDaFuncaoPresente == 0 and simbolo[0] != ")" and simbolo[0] != ":"):
                irMantendo += " " + simbolo[0] + " "
                
            if(tipoDaVariavelDaFuncaoPresente == 1  and simbolo[0] != ")" and (simbolo[0] == "inteiro" or simbolo[0] == "real" or simbolo[0] == "logico" or simbolo[0] == "caractere" )):
                palavras = irMantendo.split()
                for palavra in palavras:
                    if(simbolo[0] == "inteiro" and palavra != ","):
                        irMantendoMelhor += " int " + palavra 
                    if(simbolo[0] == "real" and palavra != ","):
                        irMantendoMelhor += " double " + palavra
                    if(simbolo[0] == "caractere" and palavra != "," ):
                        irMantendoMelhor += " String " + palavra
                    if(simbolo[0] == "logico" and palavra != ","):
                        irMantendoMelhor += " boolean " + palavra
                    if(palavra == ","):
                        irMantendoMelhor += ", "        
                tipoDaVariavelDaFuncaoPresente = 0
                irMantendo = ""    
            if(simbolo[0] == ")"):
                irMantendoMelhor += " ) "
                verTipoFuncao = 1
            if(verTipoFuncao == 1 and (simbolo[0] == "inteiro" or simbolo[0] == "real" or simbolo[0] == "logico" or simbolo[0] == "caractere" )):
                tipoDaFuncao = simbolo[0]
                if(tipoDaFuncao == "inteiro"):
                    if(adicionarParenteses == 1):
                        algoritmoFinalParteFuncaoOuProcedimento += "\nstatic int " + nomeDaFuncao + "( ) " + irMantendoMelhor
                        adicionarParenteses = 0
                    else:
                        algoritmoFinalParteFuncaoOuProcedimento += "\nstatic int " + nomeDaFuncao + irMantendoMelhor        
                if(tipoDaFuncao == "real"):
                    if(adicionarParenteses == 1):
                        algoritmoFinalParteFuncaoOuProcedimento += "\nstatic double " + nomeDaFuncao  + "( ) " + irMantendoMelhor
                        adicionarParenteses = 0
                    else:
                        algoritmoFinalParteFuncaoOuProcedimento += "\nstatic double " + nomeDaFuncao + irMantendoMelhor
                if(tipoDaFuncao == "logico"):
                    if(adicionarParenteses == 1):
                        algoritmoFinalParteFuncaoOuProcedimento += "\nstatic boolean " + nomeDaFuncao + "( ) " + irMantendoMelhor
                        adicionarParenteses = 0
                    else:
                        algoritmoFinalParteFuncaoOuProcedimento += "\nstatic boolean " + nomeDaFuncao + irMantendoMelhor
                if(tipoDaFuncao == "caractere"):
                    if(adicionarParenteses == 1):
                        algoritmoFinalParteFuncaoOuProcedimento += "\nstatic String " + nomeDaFuncao + "( ) " + irMantendoMelhor
                        adicionarParenteses = 0
                    else:
                        algoritmoFinalParteFuncaoOuProcedimento += "\nstatic String " + nomeDaFuncao + irMantendoMelhor
                        

                irMantendoMelhor = ""
                irMantendo = ""
                tipoDaFuncao = ""
                nomeDaFuncao = ""
                verTipoFuncao = 0
                FuncaoDeclaracao = 0
                tipoDaVariavelDaFuncaoPresente = 0
                TemParametros = 0

       
        
        
               
        if(simbolo[0] == "algoritmo"):
            algoritmo += "public class "
            auxAlgoritmo = 1
            FuncaoSim = 0
        if(auxAlgoritmo == 1 and simbolo[1] == "NOME_ALGORITMO/VALOR_LITERAL"):
            testo_com_aspas = simbolo[0]
            texto_sem_aspas = testo_com_aspas[1:-1] #Nome do arquivo
            algoritmo += texto_sem_aspas + " {\n"
            auxAlgoritmo = 0
        if(simbolo[0] == "var" and FuncaoSim == 0 and ProcedimentoSim == 0):
            auxVariavel = 1
            tipoDaVariavel += " static "
        if(simbolo[0] == "var" and FuncaoSim == 1 and FuncaoDeclaracao == 0):
            regularDeclaracaoFuncao = 1
        if(simbolo[0] == "var" and ProcedimentoSim == 1 and ProcedimentoDeclaracao == 0):
            regularDeclaracaoProcedimento = 1
        if(auxVariavel == 1):
            if(simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO" or simbolo[0] == ","):
                variavelDeclarada += simbolo[0] + " "
            if(simbolo[0] == "inteiro"):
                tipoDaVariavel += "int"
                formarDeclaracao += tipoDaVariavel + " " + variavelDeclarada + ";\n"
                variavelDeclarada = ""
                tipoDaVariavel = ""
                auxVariavel = 0
            if(simbolo[0] == "real"):
                tipoDaVariavel += "double"
                formarDeclaracao += tipoDaVariavel + " " + variavelDeclarada + ";\n"
                variavelDeclarada = ""
                tipoDaVariavel = ""
                auxVariavel = 0
            if(simbolo[0] == "logico"):
                tipoDaVariavel += "boolean"
                formarDeclaracao += tipoDaVariavel + " " + variavelDeclarada + ";\n"
                variavelDeclarada = ""
                tipoDaVariavel = ""
                auxVariavel = 0
            if(simbolo[0] == "caractere"):
                tipoDaVariavel += "String"
                formarDeclaracao += tipoDaVariavel + " " + variavelDeclarada + ";\n"
                variavelDeclarada = ""
                tipoDaVariavel = ""
                auxVariavel = 0

        if(regularDeclaracaoFuncao == 1):
            if(simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO" or simbolo[0] == ","):
                variavelDeclarada += simbolo[0] + " "
            if(simbolo[0] == "inteiro"):
                tipoDaVariavel += "int"
                formarDeclaracao += tipoDaVariavel + " " + variavelDeclarada + ";\n"
                variavelDeclarada = ""
                tipoDaVariavel = ""
                regularDeclaracaoFuncao = 0
            if(simbolo[0] == "real"):
                tipoDaVariavel += "double"
                formarDeclaracao += tipoDaVariavel + " " + variavelDeclarada + ";\n"
                variavelDeclarada = ""
                tipoDaVariavel = ""
                regularDeclaracaoFuncao = 0
            if(simbolo[0] == "logico"):
                tipoDaVariavel += "boolean"
                formarDeclaracao += tipoDaVariavel + " " + variavelDeclarada + ";\n"
                variavelDeclarada = ""
                tipoDaVariavel = ""
                regularDeclaracaoFuncao = 0
            if(simbolo[0] == "caractere"):
                tipoDaVariavel += "String"
                formarDeclaracao += tipoDaVariavel + " " + variavelDeclarada + ";\n"
                variavelDeclarada = ""
                tipoDaVariavel = ""
                regularDeclaracaoFuncao = 0

        if(regularDeclaracaoProcedimento == 1):
            if(simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO" or simbolo[0] == ","):
                variavelDeclarada += simbolo[0] + " "
            if(simbolo[0] == "inteiro"):
                tipoDaVariavel += "int"
                formarDeclaracao += tipoDaVariavel + " " + variavelDeclarada + ";\n"
                variavelDeclarada = ""
                tipoDaVariavel = ""
                regularDeclaracaoProcedimento = 0
            if(simbolo[0] == "real"):
                tipoDaVariavel += "double"
                formarDeclaracao += tipoDaVariavel + " " + variavelDeclarada + ";\n"
                variavelDeclarada = ""
                tipoDaVariavel = ""
                regularDeclaracaoProcedimento = 0
            if(simbolo[0] == "logico"):
                tipoDaVariavel += "boolean"
                formarDeclaracao += tipoDaVariavel + " " + variavelDeclarada + ";\n"
                variavelDeclarada = ""
                tipoDaVariavel = ""
                regularDeclaracaoProcedimento = 0
            if(simbolo[0] == "caractere"):
                tipoDaVariavel += "String"
                formarDeclaracao += tipoDaVariavel + " " + variavelDeclarada + ";\n"
                variavelDeclarada = ""
                tipoDaVariavel = ""
                regularDeclaracaoProcedimento = 0
        
                
            
        if(simbolo[0] == "inicio" and FuncaoSim == 0 and ProcedimentoSim == 0):
            algoritmoFinal += algoritmo + formarDeclaracao
            algoritmoFinal += algoritmoFinalParteFuncaoOuProcedimento
            algoritmoFinal += "public static void main(String[] args) {\n"
            iniciou = 1

        if(simbolo[0] == "inicio" and FuncaoSim == 1):
            algoritmoFinalParteFuncaoOuProcedimento += "{\n"
            algoritmoFinalParteFuncaoOuProcedimento += formarDeclaracao
            formarDeclaracao = ""
            variavelDeclarada = ""
            tipoDaVariavel = ""
            iniciou = 2

        if(simbolo[0] == "inicio" and ProcedimentoSim == 1):
            algoritmoFinalParteFuncaoOuProcedimento += "{\n"
            algoritmoFinalParteFuncaoOuProcedimento += formarDeclaracao
            formarDeclaracao = ""
            variavelDeclarada = ""
            tipoDaVariavel = ""
            iniciou = 2

            
        if(iniciou == 1):
            if(simbolo[1] != valorAnterior and valorAnterior != "" and ateRepita == 1):
                if(valorAnterior == "NOME_ALGORITMO/VALOR_LITERAL" or valorAnterior == "VALOR_LITERAL"
                   or valorAnterior == "FECHA_PARENTESES" or valorAnterior == "VALOR_REAL" or  valorAnterior == "VERDADEIRO" or  valorAnterior == "FALSO"
                   or valorAnterior == "VALOR_INT" or valorAnterior == "OP_SEP_DIFERENTE_TIPO" or valorAnterior == "OP_SEP_MESMO_TIPO" or valorAnterior == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"):
                    if(simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"):
                        if(primeiroValor == 1 and primeiroValorAux == 0):
                            if(algoritmoAuxPrimeiroValor == " false "):
                                algoritmoFinal += "true );\n"
                            if(algoritmoAuxPrimeiroValor == " true "):
                                algoritmoFinal += "false );\n"
                        else:
                            algoritmoFinal += ");\n"
                        primeiroValor = 0
                        primeiroValorAux = 0
                        algoritmoAuxPrimeiroValor = ""
                        ateRepita = 0
            valorAnterior = simbolo[1]
            
            if(ateRepita == 1 and (simbolo[0] != ">" and simbolo[0] != "<" and simbolo[0] != ">="and simbolo[0] != "<=" and simbolo[0] != "="
                                   and simbolo[0] != "<>" and simbolo[1] != "OP_ARIT" and simbolo[1] != "OP_ARIT/OP_CARACTERE" and simbolo[1] != "MOD" 
            and simbolo[1] != "ABRE_PARENTESES" and simbolo[1] != "FECHA_PARENTESES" and simbolo[1] != "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"
            and simbolo[1] != "VALOR_INT" and simbolo[1] != "ABS" and simbolo[1] != "RAIZQ" and simbolo[1] != "RANDI" and simbolo[1] != "EXP" and simbolo[1] != "QUAD"
            and simbolo[1] != "NOME_ALGORITMO/VALOR_LITERAL" and simbolo[1] != "VALOR_LITERAL" and simbolo[1] != "VERDADEIRO" and simbolo[1] != "FALSO" and simbolo[1] != "VALOR_REAL"
            and simbolo[1] != "E" and simbolo[1] != "XOU" and simbolo[1] != "OU" and simbolo[1] != "NAO" and simbolo[1] != "OP_SEP_DIFERENTE_TIPO" and simbolo[1] != "OP_SEP_MESMO_TIPO"
                                   and simbolo[1] != "OP_SEP_MESMO_TIPO")):
                if(primeiroValor == 1 and primeiroValorAux == 0):
                    if(algoritmoAuxPrimeiroValor == " false "):
                        algoritmoFinal += "true );\n"
                    if(algoritmoAuxPrimeiroValor == " true "):
                        algoritmoFinal += "false );\n"
                else:
                    algoritmoFinal += ");\n"
                primeiroValor = 0
                primeiroValorAux = 0
                algoritmoAuxPrimeiroValor = ""
                ateRepita = 0

            if(algoritmoAuxPrimeiroValor != ""):
                algoritmoFinal += algoritmoAuxPrimeiroValor
                algoritmoAuxPrimeiroValor = ""
                primeiroValor = 0

            
                
            if((simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO" or simbolo[1] == "VALOR_REAL" or simbolo[1] == "NOME_ALGORITMO/VALOR_LITERAL"
               or simbolo[1] == "VALOR_LITERAL" or simbolo[1] == "OP_ARIT" or simbolo[1] == "OP_ARIT/OP_CARACTERE" or
                (simbolo[1] == "FECHA_PARENTESES" and escrita == 0 and contarParenteses == 0 and lendoValor == 0)) and simbolo[0] != "^" ):
                algoritmoFinal += simbolo[0] + " "

            if(simbolo[1] == "ABRE_PARENTESES" and lendoValor == 0):
                algoritmoFinal += simbolo[0] + " "
                

            if(simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO" and lendoValor == 1):
                for j in tabela_simbolos2:
                    if(simbolo[0] == j[0]):
                        verTipo = j[1]

            if(verTipo == "inteiro" and lendoValor == 1 and simbolo[0] == ")"):
                lendoValor = 0
                algoritmoFinal += " = Integer.parseInt(System.console().readLine());\n"

            if(verTipo == "real" and lendoValor == 1 and simbolo[0] == ")"):
                lendoValor = 0
                algoritmoFinal += " = Double.parseDouble(System.console().readLine());\n"

            if(verTipo == "logico" and lendoValor == 1 and simbolo[0] == ")"):
                lendoValor = 0
                algoritmoFinal += " = Boolean.parseBoolean(System.console().readLine());\n"

            if(verTipo == "caractere" and lendoValor == 1 and simbolo[0] == ")"):
                lendoValor = 0
                algoritmoFinal += " = System.console().readLine();\n"

            if(contarParenteses == 1 and simbolo[1] == "ABRE_PARENTESES"):
                quantosParenteses = quantosParenteses + 1
                listaParenteses[0] = quantosParenteses

            if(contarParenteses == 1 and simbolo[1] == "FECHA_PARENTESES"):
                quantosParenteses = quantosParenteses - 1
                if(quantosParenteses == 0):
                    del listaParenteses[0]
                    contarParenteses = 0
                    algoritmoFinal += ", 2) "
                    quantosQuad = 0
                elif(quantosParenteses == ( quantosQuad - 1 )  and quantosQuad == 2):
                    algoritmoFinal += ", 2 "
                    quantosQuad -= 1
                elif(quantosParenteses == ( quantosQuad - 1 )  and quantosQuad > 1):
                    algoritmoFinal += ", 2 ) "
                    quantosQuad -= 1
                else:
                    listaParenteses[0] = quantosParenteses

            if(simbolo[1] == "FECHA_PARENTESES" and contarParenteses == 1 and quantosParenteses == 1):
                algoritmoFinal += simbolo[0] + " "
                
                
                
                

            if(simbolo[1] == "FECHA_PARENTESES" and escrita == 1):
                algoritmoFinal += simbolo[0] + ";\n"
                escrita = 0

                
                
            if(simbolo[1] == "VALOR_INT" and passoOuNao == 0 and ateFor == 0):
                 algoritmoFinal += simbolo[0] + " "
            if(simbolo[0] == "<-"):
                algoritmoFinal += " = "
            if(simbolo[0] == "," and escrita == 0):
                virgulaExp = 0
                algoritmoFinal += " , "
            if(simbolo[0] == "," and escrita == 1):
                algoritmoFinal += " + "
            if(simbolo[0] == "MOD"):
                algoritmoFinal += " % "
            if(simbolo[0] == "e"):
                algoritmoFinal += " && "
            if(simbolo[0] == "ou"):
                algoritmoFinal += " || "
            if(simbolo[0] == "nao"):
                algoritmoFinal += " ! "
            if(simbolo[0] == "xou"):
                algoritmoFinal += " ^ "
            if(simbolo[1] == "---"):
                algoritmoFinal += ";\n"
            if(primeiroValor == 0 or primeiroValorAux == 1):
                if(simbolo[0] == "FALSO"):
                    algoritmoFinal += " false "
                if(simbolo[0] == "VERDADEIRO"):
                    algoritmoFinal += " true "
            else:
                if(primeiroValor == 1 and primeiroValorAux == 0 and simbolo[0] == "FALSO"):
                    algoritmoAuxPrimeiroValor += " false "
                if(primeiroValor == 1 and primeiroValorAux == 0 and simbolo[0] == "VERDADEIRO"):
                    algoritmoAuxPrimeiroValor += " true "
                


            if(algoritmoAuxPrimeiroValor == ""):
                primeiroValor = 0
                    

            if(simbolo[0] == "para"):
                novoFor = 1
                algoritmoFinal += "for("
            if(novoFor == 1 and simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"):
                manterVariavelFor = simbolo[0]
                novoFor = 2

            if(novoFor == 3 and simbolo[1] == "VALOR_INT"):
                manterVariavel3For = simbolo[0]
                novoFor = 4
                if(int(manterVariavel3For) >=  int(manterVariavel2For)):
                    algoritmoIntermediario += " < " + manterVariavel3For
                    algoritmoIntermediario2 += " > " + manterVariavel3For
                if(int(manterVariavel3For) < int(manterVariavel2For)):
                    algoritmoIntermediario += " < " + manterVariavel3For
                    algoritmoIntermediario2 += " > " + manterVariavel3For
                ateFor = 0
                    
                
            if(novoFor == 2 and simbolo[1] == "VALOR_INT"):
                
                manterVariavel2For = simbolo[0]
                novoFor = 3

       
                
            if(simbolo[0] == "de"):
                algoritmoFinal += " = "
                estaEmFor = 1
            if(simbolo[0] == "ate" and estaEmFor == 1):
                
                algoritmoFinal += "; " + manterVariavelFor
                ateFor = 1

            if(simbolo[0] == "passo"):
                passoOuNao = 1
            if(passoOuNao == 1 and simbolo[1] == "VALOR_INT"):
                if(int(simbolo[0]) >= 0 ):
                    positivoOuNao = "sim"
                    algoritmoIntermediario3 = "; " + manterVariavelFor + " = " + manterVariavelFor + " + "  + simbolo[0]
                else:
                    positivoOuNao = "nao"
                    algoritmoIntermediario3 += "; " + manterVariavelFor + " = " + manterVariavelFor + " - " + str(abs(int(simbolo[0])))
            
            if(passoOuNao == 0 and simbolo[0] == "faca" and  facaEnquanto == 0):
                algoritmoFinal += algoritmoIntermediario
                algoritmoFinal += "; " + manterVariavelFor + "++" + "){\n"
                algoritmoIntermediario = ""
                algoritmoIntermediario2 = ""
                
                estaEmFor = 0
            if(passoOuNao == 1 and simbolo[0] == "faca"):
                if(positivoOuNao == "nao"):
                    algoritmoFinal += algoritmoIntermediario2 + algoritmoIntermediario3 
                else:
                    algoritmoFinal += algoritmoIntermediario + algoritmoIntermediario3 
                algoritmoIntermediario = ""
                algoritmoIntermediario2 = ""
                algoritmoIntermediario3 = ""
                algoritmoFinal += "){\n"
                positivoOuNao = ""
                passoOuNao = 0
                estaEmFor = 0

            if(simbolo[0] == "faca" and  facaEnquanto == 1):
                algoritmoFinal += "){\n"
                facaEnquanto = 0
            
            if(simbolo[0] == "fimpara"):
                algoritmoFinal += "}\n"
                
            if(simbolo[0] == "se"):
                algoritmoFinal += "if( "
            if(simbolo[0] == "entao"):
                algoritmoFinal += "){\n"
            if(simbolo[0] == "senao"):
                algoritmoFinal += "}\nelse{\n"
                
            if(simbolo[0] == "fimse"):
                algoritmoFinal += "}\n"

            if(ateRepita == 0):
                if(simbolo[0] == "="):
                    algoritmoFinal += " == "

                if(simbolo[0] == ">" or simbolo[0] == "<" or simbolo[0] == ">=" or simbolo[0] == "<="):
                    algoritmoFinal += " " + simbolo[0] + " "

                if(simbolo[0] == "<>"):
                    algoritmoFinal += " != "

            if(ateRepita == 1):
                if(simbolo[0] == "="):
                    algoritmoFinal += " != "

                if(simbolo[0] == ">"):
                    algoritmoFinal += " <= "

                if(simbolo[0] == "<"):
                    algoritmoFinal += " >= "

                if(simbolo[0] == ">="):
                    algoritmoFinal += " < "

                if(simbolo[0] == "<="):
                    algoritmoFinal += " > "
                    
                if(simbolo[0] == "<>"):
                    algoritmoFinal += " == "
            
                
            if(simbolo[0] == "repita"):
                algoritmoFinal += "do{\n"

            if(simbolo[0] == "ate" and estaEmFor == 0):
                algoritmoFinal += "}while( "
                ateRepita = 1


            if(simbolo[0] == "fimrepita"):
                algoritmoFinal += "}while(true);\n"

            if(simbolo[0] == "enquanto"):
                algoritmoFinal += "while( "
                facaEnquanto = 1

            if(simbolo[0] == "fimenquanto"):
                algoritmoFinal += "}\n"

            if(simbolo[0] == "escreva"):
                algoritmoFinal += "\nSystem.out.print"
                escrita = 1

            if(simbolo[0] == "escreval"):
                algoritmoFinal += "\nSystem.out.println"
                escrita = 1

            if(simbolo[0] == "interrompa"):
                algoritmoFinal += "\nbreak;\n"

            if(simbolo[0] == "retorne"):
                algoritmoFinal += "\nreturn "
                

            if(simbolo[0] == "abs"):
                algoritmoFinal += "Math.abs"

            if(simbolo[0] == "exp"):
                algoritmoFinal += "Math.pow"
                

            if(simbolo[0] == "raizq"):
                algoritmoFinal += "Math.sqrt"

            if(simbolo[0] == "randi"):
                algoritmoFinal += " new Random().nextInt"
                TemRandi = 1

            if(simbolo[0] == "quad"):
                algoritmoFinal += "Math.pow"
                if(contarParenteses == 0):
                    listaParenteses.insert(0, 0)
                contarParenteses = 1
                quantosQuad += 1
                
           
            if(simbolo[0] == "escolha"):
                algoritmoFinal += "switch( "
                novoEscolha = 1

            if(novoEscolha == 0 and simbolo[0] == "caso"):
                algoritmoFinal += "\nbreak;\n"
                algoritmoFinal += "case "
                possivelVirgulaCaso = 1

            if(novoEscolha == 1 and simbolo[0] == "caso"):
                algoritmoFinal += "){\n"
                algoritmoFinal += "case "
                novoEscolha = 0
                possivelVirgulaCaso = 1

            if(simbolo[0] == "outrocaso"):
                algoritmoFinal += "\nbreak;\n"
                algoritmoFinal += "\ndefault:\n"

            if(simbolo[0] == "fimescolha"):
                algoritmoFinal += "}\n"
                
            if(simbolo[1] == "-----"):
                algoritmoFinal += ":\n"

            if(simbolo[0] == "leia"):
                lendoValor = 1
                
        if(iniciou == 2):
            
            if(simbolo[1] != valorAnterior and valorAnterior != "" and ateRepita == 1):
                if(valorAnterior == "NOME_ALGORITMO/VALOR_LITERAL" or valorAnterior == "VALOR_LITERAL"
                   or valorAnterior == "FECHA_PARENTESES" or valorAnterior == "VALOR_REAL" or  valorAnterior == "VERDADEIRO" or  valorAnterior == "FALSO"
                   or valorAnterior == "VALOR_INT" or valorAnterior == "OP_SEP_DIFERENTE_TIPO" or valorAnterior == "OP_SEP_MESMO_TIPO" or valorAnterior == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"):
                    if(simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"):
                        if(primeiroValor == 1 and primeiroValorAux == 0):
                            if(algoritmoAuxPrimeiroValor == " false "):
                                algoritmoFinalParteFuncaoOuProcedimento += "true );\n"
                            if(algoritmoAuxPrimeiroValor == " true "):
                                algoritmoFinalParteFuncaoOuProcedimento += "false );\n"
                        else:
                            algoritmoFinalParteFuncaoOuProcedimento += ");\n"
                        primeiroValor = 0
                        primeiroValorAux = 0
                        algoritmoAuxPrimeiroValor = ""
                        ateRepita = 0
            valorAnterior = simbolo[1]
            
            if(ateRepita == 1 and (simbolo[0] != ">" and simbolo[0] != "<" and simbolo[0] != ">="and simbolo[0] != "<=" and simbolo[0] != "="
                                   and simbolo[0] != "<>" and simbolo[1] != "OP_ARIT" and simbolo[1] != "OP_ARIT/OP_CARACTERE" and simbolo[1] != "MOD" 
            and simbolo[1] != "ABRE_PARENTESES" and simbolo[1] != "FECHA_PARENTESES" and simbolo[1] != "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"
            and simbolo[1] != "VALOR_INT" and simbolo[1] != "ABS" and simbolo[1] != "RAIZQ" and simbolo[1] != "RANDI" and simbolo[1] != "EXP" and simbolo[1] != "QUAD"
            and simbolo[1] != "NOME_ALGORITMO/VALOR_LITERAL" and simbolo[1] != "VALOR_LITERAL" and simbolo[1] != "VERDADEIRO" and simbolo[1] != "FALSO" and simbolo[1] != "VALOR_REAL"
            and simbolo[1] != "E" and simbolo[1] != "XOU" and simbolo[1] != "OU" and simbolo[1] != "NAO" and simbolo[1] != "OP_SEP_DIFERENTE_TIPO" and simbolo[1] != "OP_SEP_MESMO_TIPO"
                                   and simbolo[1] != "OP_SEP_MESMO_TIPO")):
                if(primeiroValor == 1 and primeiroValorAux == 0):
                    if(algoritmoAuxPrimeiroValor == " false "):
                        algoritmoFinalParteFuncaoOuProcedimento += "true );\n"
                    if(algoritmoAuxPrimeiroValor == " true "):
                        algoritmoFinalParteFuncaoOuProcedimento += "false );\n"
                else:
                    algoritmoFinalParteFuncaoOuProcedimento += ");\n"
                primeiroValor = 0
                primeiroValorAux = 0
                algoritmoAuxPrimeiroValor = ""
                ateRepita = 0

            if(algoritmoAuxPrimeiroValor != ""):
                algoritmoFinalParteFuncaoOuProcedimento += algoritmoAuxPrimeiroValor
                algoritmoAuxPrimeiroValor = ""
                primeiroValor = 0

            
                
            if((simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO" or simbolo[1] == "VALOR_REAL" or simbolo[1] == "NOME_ALGORITMO/VALOR_LITERAL"
               or simbolo[1] == "VALOR_LITERAL" or simbolo[1] == "OP_ARIT" or simbolo[1] == "OP_ARIT/OP_CARACTERE" or
                (simbolo[1] == "FECHA_PARENTESES" and escrita == 0 and contarParenteses == 0 and lendoValor == 0)) and simbolo[0] != "^"  ):
                algoritmoFinalParteFuncaoOuProcedimento += simbolo[0] + " "

            if(simbolo[1] == "ABRE_PARENTESES" and lendoValor == 0):
                algoritmoFinalParteFuncaoOuProcedimento += simbolo[0] + " "
                

            if(simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO" and lendoValor == 1):
                for j in tabela_simbolos2:
                    if(simbolo[0] == j[0]):
                        verTipo = j[1]
                        

            if(verTipo == "inteiro" and lendoValor == 1 and simbolo[0] == ")"):
                lendoValor = 0
                algoritmoFinalParteFuncaoOuProcedimento += " = Integer.parseInt(System.console().readLine());\n"

            if(verTipo == "real" and lendoValor == 1 and simbolo[0] == ")"):
                lendoValor = 0
                algoritmoFinalParteFuncaoOuProcedimento += " = Double.parseDouble(System.console().readLine());\n"

            if(verTipo == "logico" and lendoValor == 1 and simbolo[0] == ")"):
                lendoValor = 0
                algoritmoFinalParteFuncaoOuProcedimento += " = Boolean.parseBoolean(System.console().readLine());\n"

            if(verTipo == "caractere" and lendoValor == 1 and simbolo[0] == ")"):
                lendoValor = 0
                algoritmoFinalParteFuncaoOuProcedimento += " = System.console().readLine();\n"

            if(contarParenteses == 1 and simbolo[1] == "ABRE_PARENTESES"):
                quantosParenteses = quantosParenteses + 1
                listaParenteses[0] = quantosParenteses

            if(contarParenteses == 1 and simbolo[1] == "FECHA_PARENTESES"):
                quantosParenteses = quantosParenteses - 1
                if(quantosParenteses == 0):
                    del listaParenteses[0]
                    contarParenteses = 0
                    algoritmoFinalParteFuncaoOuProcedimento += ", 2) "
                    quantosQuad = 0
                elif(quantosParenteses == ( quantosQuad - 1 )  and quantosQuad == 2):
                    algoritmoFinalParteFuncaoOuProcedimento += ", 2 "
                    quantosQuad -= 1
                elif(quantosParenteses == ( quantosQuad - 1 ) and quantosQuad > 1):
                    algoritmoFinalParteFuncaoOuProcedimento += ", 2) "
                    quantosQuad -= 1
                else:
                    listaParenteses[0] = quantosParenteses



            if(simbolo[1] == "FECHA_PARENTESES" and contarParenteses == 1 and quantosParenteses == 1):
                algoritmoFinalParteFuncaoOuProcedimento += simbolo[0] + " "
                
                
                
                

            if(simbolo[1] == "FECHA_PARENTESES" and escrita == 1):
                algoritmoFinalParteFuncaoOuProcedimento += simbolo[0] + ";\n"
                escrita = 0
                
                
            if(simbolo[1] == "VALOR_INT" and passoOuNao == 0 and ateFor == 0):
                 algoritmoFinalParteFuncaoOuProcedimento += simbolo[0] + " "
            if(simbolo[0] == "<-"):
                algoritmoFinalParteFuncaoOuProcedimento += " = "
            if(simbolo[0] == "," and escrita == 0):
                virgulaExp = 0
                algoritmoFinalParteFuncaoOuProcedimento += " , "
            if(simbolo[0] == "," and escrita == 1):
                algoritmoFinalParteFuncaoOuProcedimento += " + "
            if(simbolo[0] == "MOD"):
                algoritmoFinalParteFuncaoOuProcedimento += " % "
            if(simbolo[0] == "e"):
                algoritmoFinalParteFuncaoOuProcedimento += " && "
            if(simbolo[0] == "ou"):
                algoritmoFinalParteFuncaoOuProcedimento += " || "
            if(simbolo[0] == "nao"):
                algoritmoFinalParteFuncaoOuProcedimento += " ! "
            if(simbolo[0] == "xou"):
                algoritmoFinalParteFuncaoOuProcedimento += " ^ "
            if(simbolo[1] == "---"):
                algoritmoFinalParteFuncaoOuProcedimento += ";\n"
               
            
            if(primeiroValor == 0 or primeiroValorAux == 1):
                if(simbolo[0] == "FALSO"):
                    algoritmoFinalParteFuncaoOuProcedimento += " false "
                if(simbolo[0] == "VERDADEIRO"):
                    algoritmoFinalParteFuncaoOuProcedimento += " true "
            else:
                if(primeiroValor == 1 and primeiroValorAux == 0 and simbolo[0] == "FALSO"):
                    algoritmoAuxPrimeiroValor += " false "
                if(primeiroValor == 1 and primeiroValorAux == 0 and simbolo[0] == "VERDADEIRO"):
                    algoritmoAuxPrimeiroValor += " true "
                


            if(algoritmoAuxPrimeiroValor == ""):
                primeiroValor = 0
                    

            if(simbolo[0] == "para"):
                novoFor = 1
                algoritmoFinalParteFuncaoOuProcedimento += "for("
            if(novoFor == 1 and simbolo[1] == "VARIAVEL/NOME_DE_FUNCAO/NOME_DE_PROCEDIMENTO"):
                manterVariavelFor = simbolo[0]
                novoFor = 2

            if(novoFor == 3 and simbolo[1] == "VALOR_INT"):
                manterVariavel3For = simbolo[0]
                novoFor = 4
                if(int(manterVariavel3For) >=  int(manterVariavel2For)):
                    algoritmoIntermediario += " < " + manterVariavel3For
                    algoritmoIntermediario2 += " > " + manterVariavel3For
                if(int(manterVariavel3For) < int(manterVariavel2For)):
                    algoritmoIntermediario += " < " + manterVariavel3For
                    algoritmoIntermediario2 += " > " + manterVariavel3For
                ateFor = 0
                    
                
            if(novoFor == 2 and simbolo[1] == "VALOR_INT"):
                
                manterVariavel2For = simbolo[0]
                novoFor = 3

       
                
            if(simbolo[0] == "de"):
                algoritmoFinalParteFuncaoOuProcedimento += " = "
                estaEmFor = 1
            if(simbolo[0] == "ate" and estaEmFor == 1):
                
                algoritmoFinalParteFuncaoOuProcedimento += "; " + manterVariavelFor
                ateFor = 1

            if(simbolo[0] == "passo"):
                passoOuNao = 1
            if(passoOuNao == 1 and simbolo[1] == "VALOR_INT"):
                if(int(simbolo[0]) >= 0 ):
                    positivoOuNao = "sim"
                    algoritmoIntermediario3 = "; " + manterVariavelFor + " = " + manterVariavelFor + " + "  + simbolo[0]
                else:
                    positivoOuNao = "nao"
                    algoritmoIntermediario3 += "; " + manterVariavelFor + " = " + manterVariavelFor + " - " + str(abs(int(simbolo[0])))
            
            if(passoOuNao == 0 and simbolo[0] == "faca" and  facaEnquanto == 0):
                algoritmoFinalParteFuncaoOuProcedimento += algoritmoIntermediario
                algoritmoFinalParteFuncaoOuProcedimento += "; " + manterVariavelFor + "++" + "){\n"
                algoritmoIntermediario = ""
                algoritmoIntermediario2 = ""
                
                estaEmFor = 0
            if(passoOuNao == 1 and simbolo[0] == "faca"):
                if(positivoOuNao == "nao"):
                    algoritmoFinalParteFuncaoOuProcedimento += algoritmoIntermediario2 + algoritmoIntermediario3 
                else:
                    algoritmoFinalParteFuncaoOuProcedimento += algoritmoIntermediario + algoritmoIntermediario3 
                algoritmoIntermediario = ""
                algoritmoIntermediario2 = ""
                algoritmoIntermediario3 = ""
                algoritmoFinalParteFuncaoOuProcedimento += "){\n"
                positivoOuNao = ""
                passoOuNao = 0
                estaEmFor = 0

            if(simbolo[0] == "faca" and  facaEnquanto == 1):
                algoritmoFinalParteFuncaoOuProcedimento += "){\n"
                facaEnquanto = 0
            
            if(simbolo[0] == "fimpara"):
                algoritmoFinalParteFuncaoOuProcedimento += "}\n"
                
            if(simbolo[0] == "se"):
                algoritmoFinalParteFuncaoOuProcedimento += "if( "
            if(simbolo[0] == "entao"):
                algoritmoFinalParteFuncaoOuProcedimento += "){\n"
            if(simbolo[0] == "senao"):
                algoritmoFinalParteFuncaoOuProcedimento += "}\nelse{\n"
                
            if(simbolo[0] == "fimse"):
                algoritmoFinalParteFuncaoOuProcedimento += "}\n"

            if(ateRepita == 0):
                if(simbolo[0] == "="):
                    algoritmoFinalParteFuncaoOuProcedimento += " == "

                if(simbolo[0] == ">" or simbolo[0] == "<" or simbolo[0] == ">=" or simbolo[0] == "<="):
                    algoritmoFinalParteFuncaoOuProcedimento += " " + simbolo[0] + " "

                if(simbolo[0] == "<>"):
                    algoritmoFinalParteFuncaoOuProcedimento += " != "

            if(ateRepita == 1):
                if(simbolo[0] == "="):
                    algoritmoFinalParteFuncaoOuProcedimento += " != "

                if(simbolo[0] == ">"):
                    algoritmoFinalParteFuncaoOuProcedimento += " <= "

                if(simbolo[0] == "<"):
                    algoritmoFinalParteFuncaoOuProcedimento += " >= "

                if(simbolo[0] == ">="):
                    algoritmoFinalParteFuncaoOuProcedimento += " < "

                if(simbolo[0] == "<="):
                    algoritmoFinalParteFuncaoOuProcedimento += " > "
                    
                if(simbolo[0] == "<>"):
                    algoritmoFinalParteFuncaoOuProcedimento += " == "
            
                
            if(simbolo[0] == "repita"):
                algoritmoFinalParteFuncaoOuProcedimento += "do{\n"

            if(simbolo[0] == "ate" and estaEmFor == 0):
                algoritmoFinalParteFuncaoOuProcedimento += "}while( "
                ateRepita = 1


            if(simbolo[0] == "fimrepita"):
                algoritmoFinalParteFuncaoOuProcedimento += "}while(true);\n"

            if(simbolo[0] == "enquanto"):
                algoritmoFinalParteFuncaoOuProcedimento += "while( "
                facaEnquanto = 1

            if(simbolo[0] == "fimenquanto"):
                algoritmoFinalParteFuncaoOuProcedimento += "}\n"

            if(simbolo[0] == "escreva"):
                algoritmoFinalParteFuncaoOuProcedimento += "\nSystem.out.print"
                escrita = 1

            if(simbolo[0] == "escreval"):
                algoritmoFinalParteFuncaoOuProcedimento += "\nSystem.out.println"
                escrita = 1

            if(simbolo[0] == "interrompa"):
                algoritmoFinalParteFuncaoOuProcedimento += "\nbreak;\n"

            if(simbolo[0] == "retorne"):
                algoritmoFinalParteFuncaoOuProcedimento += "\nreturn "

            if(simbolo[0] == "abs"):
                algoritmoFinalParteFuncaoOuProcedimento += "Math.abs"

            if(simbolo[0] == "exp"):
                algoritmoFinalParteFuncaoOuProcedimento += "Math.pow"
                

            if(simbolo[0] == "raizq"):
                algoritmoFinalParteFuncaoOuProcedimento += "Math.sqrt"

            if(simbolo[0] == "randi"):
                algoritmoFinalParteFuncaoOuProcedimento += " new Random().nextInt"
                TemRandi = 1

            if(simbolo[0] == "quad"):
                algoritmoFinalParteFuncaoOuProcedimento += "Math.pow"
                if(contarParenteses == 0):
                    listaParenteses.insert(0, 0)
                contarParenteses = 1
                quantosQuad += 1
                
           
            if(simbolo[0] == "escolha"):
                algoritmoFinalParteFuncaoOuProcedimento += "switch( "
                novoEscolha = 1

            if(novoEscolha == 0 and simbolo[0] == "caso"):
                algoritmoFinalParteFuncaoOuProcedimento += "\nbreak;\n"
                algoritmoFinalParteFuncaoOuProcedimento += "case "
                possivelVirgulaCaso = 1

            if(novoEscolha == 1 and simbolo[0] == "caso"):
                algoritmoFinalParteFuncaoOuProcedimento += "){\n"
                algoritmoFinalParteFuncaoOuProcedimento += "case "
                novoEscolha = 0
                possivelVirgulaCaso = 1

            if(simbolo[0] == "outrocaso"):
                algoritmoFinalParteFuncaoOuProcedimento += "\nbreak;\n"
                algoritmoFinalParteFuncaoOuProcedimento += "\ndefault:\n"

            if(simbolo[0] == "fimescolha"):
                algoritmoFinalParteFuncaoOuProcedimento += "}\n"
                
            if(simbolo[1] == "-----"):
                algoritmoFinalParteFuncaoOuProcedimento += ":\n"

            if(simbolo[0] == "leia"):
                lendoValor = 1

            if(simbolo[0] == "fimfuncao"):
                algoritmoFinalParteFuncaoOuProcedimento += "}\n"
                iniciou = 0
                FuncaoSim = 0

            if(simbolo[0] == "fimprocedimento"):
                algoritmoFinalParteFuncaoOuProcedimento += "}\n"
                iniciou = 0
                ProcedimentoSim = 0
            
        if(simbolo[0] == "fimalgoritmo"):
            algoritmoFinal += "}\n" + "}\n" 
            

    algoritmoFinalComImports = ""
    if(TemRandi == 1):
        algoritmoFinalComImports += "import java.util.Random;\n"
        
    algoritmoFinalComImports += algoritmoFinal

    area_resultado.config(state=tk.NORMAL)
    area_resultado.delete("1.0", tk.END)
    area_resultado.insert(tk.END, f"{algoritmoFinalComImports}")
    area_resultado.config(state=tk.DISABLED)
            
    #semantico(tabela_simbolos)
    print(algoritmoFinalComImports)



    with open(texto_sem_aspas + ".java", 'w') as f:
        f.write(algoritmoFinalComImports)
    
    
    try:
        os.system('cmd /k "javac ' + texto_sem_aspas + '.java && java ' + texto_sem_aspas + '"')
        print("Execução realizada com sucesso.")
    except subprocess.CalledProcessError as e:
        print("Erro na execução do código")
    
    

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

# Botão Analisador Semântico
botao_compilar = tk.Button(frame_buttons, text="Analisador Semântico", command=compilarLexicoESemantico, bg='white', font = "bold")
botao_compilar.pack(side="left", pady=5)

# Botão Gerador de Código
botao_compilar = tk.Button(frame_buttons, text="Gerador de Código", command=geradorDeCodigo, bg='green', font = "bold")
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
