import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import filedialog as fd
import webbrowser
import sys


# --------------------------------------------------------------------
# ----------------------- função de transição ------------------------



transicao = {
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
    
     
}  # fecha o dicionário


# -------------------------------------------------------------------
# ------------------------- Palavra reservada -----------------------

reservadas = [
    'algoritmo', 'inicio',
    'fimalgoritmo', 'var',
    'inteiro', 'real', 'caractere',
    'logico', 'escreva', 'escreval', 'leia',
    'para', 'fimpara', 'faca', 'enquanto',
    'fimenquanto', 'repita', 'ate', 'interrompa',
    'fimrepita', 'de', 'passo', 'se', 'fimse', 'senao',
    'escolha', 'caso', 'outrocaso', 'fimescolha', 'mod',
    'e', 'ou', 'nao', 'VERDADEIRO', 'FALSO', 'xou', 'abs',
    'exp', 'quad', 'raizq', 'randi', 'funcao', 'fimfuncao',
    'procedimento', 'fimprocedimento', 'retorne', 'MOD',
    'vetor'
]

def lexico(lista):
    tabela_simbolos = []
    for palavra in lista:
        estado = 'q0'
        try:
            for letra in palavra:
                estado = transicao[estado][letra]
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
            elif (palavra == '"'):
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

def compilar():
    codigo = editor_texto.get("1.0", tk.END).strip()
    if not codigo:
        messagebox.showwarning("Aviso", "O editor de código está vazio.")
        
    linhas = codigo.splitlines()
    tabela_simbolos = []
    for linha in linhas:
        resultado = lexico(linha.split())
        if resultado is None:
            return
        tabela_simbolos.extend(resultado)

    # Exibir resultado na área de saída
    area_resultado.config(state=tk.NORMAL)
    area_resultado.delete("1.0", tk.END)
    for simbolo in tabela_simbolos:
        area_resultado.insert(tk.END, f"{simbolo[0]}: {simbolo[1]}\n")
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
botao_compilar = tk.Button(frame_buttons, text="Analisador Léxico", command=compilar, bg='#9A7B4F', font = "bold")
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




