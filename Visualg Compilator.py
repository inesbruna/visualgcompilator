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
             '"': 'qf12'},
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
      'qf7': {'=': 'qf12'}
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




