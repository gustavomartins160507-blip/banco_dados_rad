import tkinter as tk  # importa a biblioteca tkinter para criar interfaces gráficas
from tkinter import messagebox  # importa o messagebox para exibir caixas de diálogo

# função executada ao clicar no botão "Submeter"
def submit():
    nome = nome_entry.get()       # pega o texto digitado no campo nome
    email = email_entry.get()     # pega o texto digitado no campo email
    linguagem = linguagem_var.get()  # pega a linguagem selecionada no radio button
    print("Nome: ", nome)
    print("Email: ", email)
    # exibe uma caixa de diálogo com os dados preenchidos
    messagebox.showinfo(
        "dados submetidos",
        f"Nome: {nome}\nEmail: {email}\nLinguagem preferida: {linguagem}"
    )

# função executada ao clicar no botão "Apagar Campo"
def apagar():
    nome = nome_entry.get()   # guarda o nome antes de apagar para exibir na mensagem
    email = email_entry.get() # guarda o email antes de apagar para exibir na mensagem
    email_entry.delete(0, tk.END)  # apaga todo o conteúdo do campo email
    nome_entry.delete(0, tk.END)   # apaga todo o conteúdo do campo nome
    # exibe confirmação com os dados que foram apagados
    messagebox.showinfo(
        "dados apagados com sucesso",
        f"Nome: {nome}\nEmail: {email}"
    )

# função executada ao clicar no botão "Somar"
def somar():
    primeiro_numero = int(primeiro_numero_entry.get())   # pega e converte o primeiro número para inteiro
    segundo_numero = int(segundo_numero_entry.get())     # pega e converte o segundo número para inteiro
    resultado = primeiro_numero + segundo_numero         # realiza a soma dos dois números
    # exibe o resultado da soma em uma caixa de diálogo
    messagebox.showinfo(
        "Resultado",
        f"Soma: {resultado}"
    )
    primeiro_numero_entry.delete(0, tk.END)  # limpa o campo do primeiro número
    segundo_numero_entry.delete(0, tk.END)   # limpa o campo do segundo número

# cria a janela principal da aplicação
root = tk.Tk()
root.title("Formulário de inscrição")  # define o título da janela
root.resizable(False, False)           # impede o redimensionamento da janela

# cria um frame (contêiner) para organizar os widgets dentro da janela
frame = tk.Frame(root)
frame.pack(padx=150, pady=150)  # adiciona espaçamento externo ao frame

# labels (textos descritivos dos campos)
nome_label = tk.Label(frame, text="Nome:")
nome_label.grid(row=0, column=1)  # posiciona na linha 0, coluna 1

email_label = tk.Label(frame, text="Email:")
email_label.grid(row=1, column=1)  # posiciona na linha 1, coluna 1

primeiro_numero_label = tk.Label(frame, text="Digite o primeiro número:")
primeiro_numero_label.grid(row=5, column=1)  # posiciona na linha 5, coluna 1

segundo_numero_label = tk.Label(frame, text="Digite o segundo número:")
segundo_numero_label.grid(row=6, column=1)  # posiciona na linha 6, coluna 1

# campos de entrada de texto
nome_entry = tk.Entry(frame)
nome_entry.grid(row=0, column=2)  # campo nome na linha 0, coluna 2

email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=2)  # campo email na linha 1, coluna 2

primeiro_numero_entry = tk.Entry(frame)
primeiro_numero_entry.grid(row=5, column=2)  # campo primeiro número na linha 5, coluna 2

segundo_numero_entry = tk.Entry(frame)
segundo_numero_entry.grid(row=6, column=2)  # campo segundo número na linha 6, coluna 2

# radio buttons para escolha da linguagem preferida
linguagem_var = tk.StringVar(value="python")  # variável que armazena a opção selecionada, padrão "python"

python_radio = tk.Radiobutton(
    frame,
    value="python",        # valor atribuído ao selecionar esta opção
    variable=linguagem_var,  # vincula ao mesmo grupo de seleção
    text="Python"
)
python_radio.grid(row=2, column=1)  # posiciona na linha 2, coluna 1

js_radio = tk.Radiobutton(
    frame,
    value="javascript",
    variable=linguagem_var,
    text="JavaScript"
)
js_radio.grid(row=2, column=2)  # posiciona na linha 2, coluna 2

# botões de ação
submit_button = tk.Button(frame, text="Submeter", command=submit)  # chama a função submit ao clicar
submit_button.grid(row=7, column=1, pady=10)

apagar_campo = tk.Button(frame, text="Apagar Campo", command=apagar)  # chama a função apagar ao clicar
apagar_campo.grid(row=7, column=2, pady=10)

somar_campo = tk.Button(frame, text="Somar", command=somar)  # chama a função somar ao clicar
somar_campo.grid(row=7, column=3, pady=10)

# inicia o loop principal da interface gráfica, mantendo a janela aberta
root.mainloop()