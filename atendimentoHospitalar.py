print("Bem vindo ao atendimento hospitalar Carelife!")

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
telefone = input("Digite seu telefone:")
endereco = input("Digite seu Endereço:")

doencasCronicas = input("Você possui alguma doença Crônica?[sim/não]")
marcadorAlterado = input("Você possui algum marcador alterado?(Temperatura, Pressão...)[sim/não]")

def dados(prioridadeDeAtendimento):
    print(" ")
    print("--------Prontuário do Paciente--------")
    print("Nome do paciente: " + nome)
    print("Idade do paciente: " + str(idade))
    print("Telefone do paciente: " + telefone)
    print("Endereço do paciente: " + endereco)
    print("Doenças Crônicas: " + doencasCronicas)
    print("Marcadores Alterados: " + marcadorAlterado)
    print("Prioridade de atendimento: " + prioridadeDeAtendimento)

def criarProntuario(prioridadeDeAtendimento):
    arquivo = open("Prontuario", 'w+')
    arquivo.write('--------Prontuário do Paciente--------\n')
    arquivo.write("Nome do paciente: " + nome + '\n')
    arquivo.write("Idade do paciente: " + str(idade) + '\n')
    arquivo.write("Telefone do paciente: " + telefone + '\n')
    arquivo.write("Endereço do paciente: " + endereco + '\n')
    arquivo.write("Doenças Crônicas: " + doencasCronicas + '\n')
    arquivo.write("marcadorAlterado: " + marcadorAlterado + '\n')
    arquivo.write("Prioridade de atendimento: " + prioridadeDeAtendimento)
    arquivo.close()

if idade > 60 and marcadorAlterado != "sim" and doencasCronicas != "sim":
    dados("Prioridade")
    criarProntuario("Prioridade")
elif marcadorAlterado == "sim" and doencasCronicas != "sim":
    dados("Emergência")
    criarProntuario("Emergência")
elif doencasCronicas == "sim":
    dados("Urgência")
    criarProntuario("Urgência")
else:
    dados("Mal...mas passa bem")
    criarProntuario("Mal...mas passa bem")