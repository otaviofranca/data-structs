class Pessoa:
    def __init__(self, nome, idade, grupo_prioritario):
        self.nome = nome
        self.idade = idade
        self.grupo_prioritario = grupo_prioritario
        self.prioridade = self.definir_prioridade()

    def definir_prioridade(self):
        if self.idade >= 100:
            return "Centenário"
        elif self.idade >= 90:
            return "Nonagenário"
        elif self.idade >= 80:
            return "Octogenário"
        elif self.idade >= 70:
            return "Septuagenário"
        elif self.idade >= 60:
            return "Sexagenário"
        elif self.idade <60:
            return "Prioridae por Urgência ou Comodidade" 
        else:
            return "Outros"

class FilaPrioridades:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self, pessoa):
        novo_no = No(pessoa)
        if not self.inicio:
            self.inicio = novo_no
            self.fim = novo_no
        elif pessoa.grupo_prioritario:
            atual = self.inicio
            anterior = None
            while atual and atual.pessoa.grupo_prioritario and atual.pessoa.idade >= pessoa.idade:
                anterior = atual
                atual = atual.proximo
            if not anterior:
                novo_no.proximo = self.inicio
                self.inicio = novo_no
            else:
                anterior.proximo = novo_no
                novo_no.proximo = atual
                if not atual:
                    self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def desenfileirar(self):
        if not self.inicio:
            return None
        pessoa_atendida = self.inicio.pessoa
        self.inicio = self.inicio.proximo
        if not self.inicio:
            self.fim = None
        return pessoa_atendida
    
    def listar(self):
        atual = self.inicio
        while atual:
            print(f'Nome: {atual.pessoa.nome}, Idade: {atual.pessoa.idade}, Prioridade: {atual.pessoa.grupo_prioritario}')
            atual = atual.proximo

    def tamanho(self):
        tamanho = 0
        atual = self.inicio
        while atual:
            tamanho += 1
            atual = atual.proximo
        return tamanho

    def estatisticas(self):
        total_atendimentos = self.tamanho()
        if total_atendimentos == 0:
            return 0, 0, 0, 0

        total_prioritarios = 0
        total_normais = 0
        atual = self.inicio
        while atual:
            if atual.pessoa.grupo_prioritario:
                total_prioritarios += 1
            else:
                total_normais += 1
            atual = atual.proximo
        
        percent_prioritarios = (total_prioritarios / total_atendimentos) * 100
        percent_normais = (total_normais / total_atendimentos) * 100

        return percent_prioritarios, percent_normais, total_prioritarios, total_normais


class No:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.proximo = None
