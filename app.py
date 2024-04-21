import tkinter as tk
from tkinter import messagebox
from adt import FilaPrioridades, Pessoa

class AplicacaoCliente:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Fila com Prioridades")
        self.fila_prioridades = FilaPrioridades()

        self.criar_widgets()

    def criar_widgets(self):
        
        self.frame = tk.Frame(self.master, padx=20, pady=20)
        self.frame.pack()
       
        tk.Label(self.frame, text="Nome:").grid(row=0, column=0, sticky="w")
        tk.Label(self.frame, text="Idade:").grid(row=1, column=0, sticky="w")
        
        self.nome_entry = tk.Entry(self.frame)
        self.nome_entry.grid(row=0, column=1)
        self.idade_entry = tk.Entry(self.frame)
        self.idade_entry.grid(row=1, column=1)

        self.chegada_normal_btn = tk.Button(self.frame, text="Atendimento Normal", command=self.chegada_normal)
        self.chegada_normal_btn.grid(row=2, column=0, pady=5)
        self.chegada_prioritaria_btn = tk.Button(self.frame, text="Atendimento Prioritário", command=self.chegada_prioritaria)
        self.chegada_prioritaria_btn.grid(row=2, column=1, pady=5)
        self.atendimento_btn = tk.Button(self.frame, text="Atendimento", command=self.atendimento)
        self.atendimento_btn.grid(row=3, column=0, columnspan=2, pady=5)
        self.listar_btn = tk.Button(self.frame, text="Listar", command=self.listar)
        self.listar_btn.grid(row=4, column=0, columnspan=2, pady=5)
        self.estatisticas_btn = tk.Button(self.frame, text="Estatísticas", command=self.estatisticas)
        self.estatisticas_btn.grid(row=5, column=0, columnspan=2, pady=5)
        self.sair_btn = tk.Button(self.frame, text="Sair", command=self.sair)
        self.sair_btn.grid(row=6, column=0, columnspan=2, pady=5)

        self.output_text = tk.Text(self.frame, height=10, width=50)
        self.output_text.grid(row=7, column=0, columnspan=2)

    def chegada_normal(self):
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        if nome and idade:
            pessoa = Pessoa(nome, int(idade), grupo_prioritario=False)
            self.fila_prioridades.enfileirar(pessoa)
            self.output_text.insert(tk.END, f"Pessoa {nome} adicionada à fila normal.\n")
            self.limpar_campos_entrada()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def chegada_prioritaria(self):
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        if nome and idade:
            pessoa = Pessoa(nome, int(idade), True)
            self.fila_prioridades.enfileirar(pessoa)
            self.output_text.insert(tk.END, f"Pessoa {nome} adicionada à fila prioritária.\n")
            self.limpar_campos_entrada()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def atendimento(self):
        pessoa_atendida = self.fila_prioridades.desenfileirar()
        if pessoa_atendida:
            self.output_text.insert(tk.END, f"Atendendo a pessoa: {pessoa_atendida.nome}\n")
        else:
            self.output_text.insert(tk.END, "Não ha pessoas para atender.\n")

    def listar(self):
        self.output_text.delete(1.0, tk.END)
        atual = self.fila_prioridades.inicio
        while atual:
            self.output_text.insert(tk.END, f'Nome: {atual.pessoa.nome}, Idade: {atual.pessoa.idade}, Prioridade: {atual.pessoa.grupo_prioritario}\n')
            atual = atual.proximo

    def estatisticas(self):
        percent_prioritarios, percent_normais, total_prioritarios, total_normais = self.fila_prioridades.estatisticas()
        self.output_text.insert(tk.END, "\nEstatisticas:\n")
        self.output_text.insert(tk.END, f"% Atendimentos Prioritarios: {percent_prioritarios:.2f}%\n")
        self.output_text.insert(tk.END, f"% Atendimentos Normais: {percent_normais:.2f}%\n")
        self.output_text.insert(tk.END, f"Tamanho da fila Prioritaria: {total_prioritarios}\n")
        self.output_text.insert(tk.END, f"Tamanho da fila Normal: {total_normais}\n")

    def sair(self):
        if self.fila_prioridades.tamanho() == 0:
            self.master.destroy()
        else:
            messagebox.showinfo("Aviso", "Ainda ha pessoas na fila. Por favor, atenda todas antes de sair.")

    def limpar_campos_entrada(self):
        self.nome_entry.delete(0, tk.END)
        self.idade_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacaoCliente(root)
    root.mainloop()
