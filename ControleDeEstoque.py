import json
import os

path = './Estoque.json'

if(os.path.isfile(path) == False):
    with open("Estoque.json", "w") as file:
        file.write("{\n\n}")
        file.close()
    

repeat = True

class product:
    def __init__(self, id_Prod, nome_Prod, valor_Prod, estoqueMinimo_Prod, estoqueAtual_Prod, estoqueStatus_Prod, departamento_Prod, perdas_Prod):
        self.id_Prod = id_Prod
        self.tempObject = {
            str(id_Prod): {
                "nome_Prod": nome_Prod,
                "valor_Prod": valor_Prod,
                "estoqueMinimo_Prod": estoqueMinimo_Prod,
                "estoqueAtual_Prod": estoqueAtual_Prod,
                "estoqueStatus_Prod": estoqueStatus_Prod,
                "departamento_Prod": departamento_Prod,
                "perdas_Prod": perdas_Prod
            }
        }
    def Insert(self):
        with open("Estoque.json") as file:
            tempData = json.load(file)

        tempData.update(self.tempObject)

        with open("Estoque.json", "w") as file:
            json.dump(tempData, file, indent=4)
            file.close()


while repeat:
    repeatAction = True

    print("Bem Vindo ao SetStock!\n")
    print("Qual Operação você gostaria de realizar:")
    print(" 1)Adicionar Produtos \n 2)Verificar Estoque \n 3)Atualizar Produto \n 4)Deletar Produto \n 5)Sair \n")
    option = int(input("Selecione uma Opção: \n"))

    match(option):
        case 1:
            while repeatAction:
                id_Prod = int(input("Id do Produto:"))
                nome_Prod = input("Nome do Produto:")
                valor_Prod = float(input("Valor do Produto:"))
                estoqueMinimo_Prod = int(input("Estoque Minimo do Produto:"))
                estoqueAtual_Prod = int(input("Estoque Atual do Produto:"))
                estoqueStatus_Prod = input("Status do Estoque:")
                departamento_Prod =input("Departamento do Produto:")
                perdas_Prod = input("Perdas do Produto:")
                
                prod = product(id_Prod, nome_Prod, valor_Prod, estoqueMinimo_Prod, estoqueAtual_Prod, estoqueStatus_Prod, departamento_Prod, perdas_Prod)
                prod.Insert()
                print("Dados Cadastrados com Sucesso!")

                repeatAgain = input("Deseja Cadastrar outro Produto?[s/n]")

                if(repeatAgain != "s"):
                    repeatAction = False
        case 5:
            exit()
        case _:
            exit()
