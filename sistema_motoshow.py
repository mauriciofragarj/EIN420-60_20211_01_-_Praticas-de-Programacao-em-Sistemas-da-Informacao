from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Sistema MotoShow')
root.iconbitmap('C:/Z_SANDBOX/projeto_sistema_motos/media/bike_icon.ico')
root.geometry("700x480")
#___________________________________________________________________________________________
conn = sqlite3.connect('banco_AP3.db')
c = conn.cursor()

def delete():
    conn = sqlite3.connect('banco_AP3.db')
    c = conn.cursor()
    c.execute("DELETE from clientes WHERE oid= " + delete_box.get())
    conn.commit()
    conn.close()

def submit():
    conn = sqlite3.connect('banco_AP3.db')
    c = conn.cursor()
    c.execute("INSERT INTO clientes VALUES (:nome_cliente, :telefone, :cpf, :email, :logradouro, :num_logradouro, :complemento, :cidade, :estado)",
              {'nome_cliente': nome_cliente.get(), 'telefone': telefone.get(), 'cpf': cpf.get(), 'email': email.get(),
               'logradouro': logradouro.get(), 'num_logradouro': num_logradouro.get(), 'complemento': complemento.get(), 'cidade': cidade.get(), 'estado': estado.get(),})
    conn.commit()
    conn.close()
    nome_cliente.delete(0, END)
    telefone.delete(0, END)
    cpf.delete(0, END)
    email.delete(0, END)
    logradouro.delete(0, END)
    num_logradouro.delete(0, END)
    complemento.delete(0, END)
    cidade.delete(0, END)
    estado.delete(0, END)

def query():
    conn = sqlite3.connect('banco_AP3.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM clientes")
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)
    conn.commit()
    conn.close()

nome_cliente = Entry(root, width=30)
nome_cliente.grid(row=1, column=1, padx=20)
telefone = Entry(root, width=30)
telefone.grid(row=2, column=1, padx=20)
cpf = Entry(root, width=30)
cpf.grid(row=3, column=1, padx=20)
email = Entry(root, width=30)
email.grid(row=4, column=1, padx=20)
logradouro = Entry(root, width=30)
logradouro.grid(row=5, column=1, padx=20)
num_logradouro = Entry(root, width=30)
num_logradouro.grid(row=6, column=1, padx=20)
complemento = Entry(root, width=30)
complemento.grid(row=7, column=1, padx=20)
cidade = Entry(root, width=30)
cidade.grid(row=8, column=1, padx=20)
estado = Entry(root, width=30)
estado.grid(row=9, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=13, column=1, pady=5)

titulo = Label(root, text="CADASTRO DE CLIENTES - MOTOSHOW").grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=154)
nome_cliente_label = Label(root, text="Nome Completo:")
nome_cliente_label.grid(row=1, column=0)
telefone_label = Label(root, text="Telefone:")
telefone_label.grid(row=2, column=0)
cpf_label = Label(root, text="CPF:")
cpf_label.grid(row=3, column=0)
email_label = Label(root, text="E-Mail:")
email_label.grid(row=4, column=0)
logradouro_label = Label(root, text="Logradouro:")
logradouro_label.grid(row=5, column=0)
num_logradouro_label = Label(root, text="Número:")
num_logradouro_label.grid(row=6, column=0)
complemento_label = Label(root, text="Complemento:")
complemento_label.grid(row=7, column=0)
cidade_label = Label(root, text="Cidade:")
cidade_label.grid(row=8, column=0)
estado_label = Label(root, text="Estado:")
estado_label.grid(row=9, column=0)
delete_box_label = Label(root, text="Deletar CPF")
delete_box_label.grid(row=13, column=0, pady=5)
submit_btn = Button(root, text="Salvar Dados", command=submit)
submit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=138)

query_btn = Button(root, text="Exibir / Atualizar Dados", command=query)
query_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=112)
delete_btn = Button(root, text="Deletar CPF do Cliente", command=delete)
delete_btn.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=135)
button_quit = Button(root, text="Sair do Sistema", command=root.quit)
button_quit.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=154)
#___________________________________________________________________________________________
conn.commit()
conn.close()
root.mainloop()