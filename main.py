from database import create_tables
import controllers as ctrl

def menu():
    print("\n=== Gerenciador de Livros ===")
    print("1 - Adicionar Livro")
    print("2 - Listar Livros")
    print("3 - Buscar Livro por Título")
    print("4 - Atualizar Livro")
    print("5 - Remover Livro")
    print("0 - Sair")

if __name__ == "__main__":
    create_tables()

    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            genero = input("Gênero: ")
            ctrl.adicionar_livro(titulo, autor, ano, genero)

        elif opcao == "2":
            for livro in ctrl.listar_livros():
                print(livro)

        elif opcao == "3":
            titulo = input("Digite parte do título: ")
            for livro in ctrl.buscar_livro(titulo):
                print(livro)

        elif opcao == "4":
            id = int(input("ID do livro: "))
            novo_titulo = input("Novo título: ")
            novo_autor = input("Novo autor: ")
            novo_ano = int(input("Novo ano: "))
            novo_genero = input("Novo gênero: ")
            ctrl.atualizar_livro(id, novo_titulo, novo_autor, novo_ano, novo_genero)

        elif opcao == "5":
            id = int(input("ID do livro para remover: "))
            ctrl.remover_livro(id)

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")
