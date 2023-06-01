class Contato:
    def __init__(self, nome, sobrenome, email, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone

class Agenda:
    def __init__(self):
        self.contatos = []

    def incluir_contato(self, contato):
        self.contatos.append(contato)
        print("Contato adicionado com sucesso!")

    def buscar_contato(self, chave, valor):
        contatos_encontrados = []
        for contato in self.contatos:
            if getattr(contato, chave) == valor:
                contatos_encontrados.append(contato)
        return contatos_encontrados

    def editar_contato(self, contato, chave, novo_valor):
        setattr(contato, chave, novo_valor)
        print("Contato editado com sucesso!")

    def excluir_contato(self, chave, valor):
        contatos_removidos = []
        for contato in self.contatos:
            if getattr(contato, chave) == valor:
                self.contatos.remove(contato)
                contatos_removidos.append(contato)
        return contatos_removidos

    def listar_contatos(self):
        if len(self.contatos) == 0:
            print("A agenda está vazia.")
        else:
            for contato in self.contatos:
                print(f"Nome: {contato.nome} {contato.sobrenome}")
                print(f"Email: {contato.email}")
                print(f"Telefone: {contato.telefone}")
                print("---------------------------")

def exibir_menu():
    print("----- Agenda de Contatos -----")
    print("1. Incluir novo contato")
    print("2. Buscar um contato")
    print("3. Editar um contato")
    print("4. Excluir um contato")
    print("5. Listar todos os contatos")
    print("6. Sair")

agenda = Agenda()

while True:
    exibir_menu()
    opcao = input("Digite o número da operação desejada: ")

    if opcao == "1":
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        novo_contato = Contato(nome, sobrenome, email, telefone)
        agenda.incluir_contato(novo_contato)

    elif opcao == "2":
        chave_busca = input("Digite o critério de busca (Nome, Sobrenome, Email ou Telefone): ")
        valor_busca = input("Digite o valor a ser buscado: ")
        contatos_encontrados = agenda.buscar_contato(chave_busca.lower(), valor_busca)
        if len(contatos_encontrados) > 0:
            for contato in contatos_encontrados:
                print(f"Nome: {contato.nome} {contato.sobrenome}")
                print(f"Email: {contato.email}")
                print(f"Telefone: {contato.telefone}")
                print("---------------------------")
        else:
            print("Nenhum contato encontrado.")

    elif opcao == "3":
        chave_edicao = input("Digite o critério de busca para editar o contato (Nome, Sobrenome, Email ou Telefone): ")
        valor_edicao = input("Digite o valor do contato a ser editado: ")
        contatos_encontrados = agenda.buscar_contato(chave_edicao1)
