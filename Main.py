import random
import os

def limpar_tela():
    os.system('cls')
    
def limpar_tela_enter():
    input("Pressione [ENTER]...")
    os.system('cls')

# --- CONFIGURAÇÕES E PLACAR ---
jogadores = ["BRUNO", "JULIA", "LUAN", "GIOVANA"]
lista_votacao = []
placar = {}
#Definindo a estrutura do placar
for i, nome in enumerate(jogadores):
       placar.setdefault(nome, 0)

impostor = random.choice(jogadores)
print(f"{impostor}")
limpar_tela_enter()
"""
while True:
    print("Jogo do Impostor\n1 - Adicionar Jogador.\n2 - Remover Jogador\n3 - Iniciar o Jogo.")
    if len(jogadores) != 0:
       print(*jogadores, sep=", ")
    escolha = int(input("\nEscolha um numero: "))
    
    match escolha:
        case 1:
            nome = input("Nome do Jogador para adicionar: ")
            jogadores.append(nome)
            limpar_tela()
        case 2: 
            nome = input("Nome do Jogador para remover: ")
            if nome in jogadores:
                jogadores.remove(nome)
                limpar_tela()
            else:
                print("Nome do jogador não encontrado na lista de jogadores") 
                limpar_tela_enter()
        case 3:
            if len(jogadores) < 3:
                print("Quantidade de jogadores minima não atingida.")
                limpar_tela_enter()
            else:
                break




comidas = [

    "Pizza", "Sushi", "Hambúrguer", "Sopa", 
    "Churrasco", "Salada", "Sorvete"
]

perguntas = [
    "Você costuma comer isso com as mãos ou precisa obrigatoriamente de talheres?", 
    "Isso é melhor servido bem quente, gelado ou em temperatura ambiente?", 
    "Dá para preparar isso rapidinho no micro-ondas ou exige um bom tempo de fogão/forno?",
    "Qual o ingrediente mais estranho que você já colocou nisso?"
]

# --- 1. SORTEIO INICIAL ---
impostor = random.choice(jogadores)
comida_sorteada = random.choice(comidas)

limpar_tela()
print("--- O JOGO VAI COMEÇAR ---")

# --- 2. FASE DE REVELAÇÃO (SEGREDOS) ---
for jogador in jogadores:
    input(f"\nPasse a tela para {jogador.title()} e aperte [ENTER] para revelar seu segredo...")
    limpar_tela()
    
    print(f"👁️ --- SEGREDO DE {jogador.upper()} --- 👁️\n")
    
    if jogador == impostor:
        print("🚨 VOCÊ É O IMPOSTOR! 🚨")
        print("Tente descobrir qual é a comida da rodada através das perguntas!")
    else:
        print("✅ VOCÊ É UM CIDADÃO!")
        print(f"A comida da rodada é: ---> {comida_sorteada} <---")
        print("Cuidado para não ser muito óbvio e o impostor descobrir!")
        
    input("\nAperte [ENTER] para esconder a tela...")
    limpar_tela()

# --- 3. FASE DE PERGUNTAS ---
# Cria a roda de perguntas
perguntadores = random.sample(jogadores, len(jogadores))
respondedores = perguntadores[1:] + [perguntadores[0]]
perguntas_sorteadas = random.sample(perguntas, len(jogadores))

print("====================================")
print("🎲 HORA DAS PERGUNTAS! 🎲")
print("====================================\n")

for quem_pergunta, quem_responde, pergunta in zip(perguntadores, respondedores, perguntas_sorteadas):
    input("Aperte [ENTER] para ver a próxima pergunta...")
    limpar_tela()
    
    print(f"🎙️ {quem_pergunta.title()} pergunta para {quem_responde.title()}:")
    print(f"   💬 {pergunta}\n")
"""
limpar_tela()
# --- 4. FASE DE VOTAÇÃO ---   

# Cria um dicionário zerado para contar os votos que cada jogador vai receber
votos_recebidos = {jogador: 0 for jogador in jogadores}

print("====================================")
print("HORA DA VOTAÇÃO!")
print("====================================\n")
limpar_tela_enter()

for jogador in jogadores:
    print(f"Vez de: {jogador}")
    limpar_tela_enter()

    # O impostor agora vota normalmente, então removemos o "if jogador == impostor" que pulava a vez

    # Cria a lista de opções excluindo o jogador atual
    opcoes_voto = [j for j in jogadores if j != jogador]

    while True:
        print("Lista de jogadores para votar:")
        for indice, nome in enumerate(opcoes_voto):
            print(f"{indice} - {nome}")
        
        try:
            voto_indice = int(input("Digite o número de quem quer votar: "))
            
            # Valida se o voto está dentro do limite da lista
            if 0 <= voto_indice < len(opcoes_voto):
                voto_nome = opcoes_voto[voto_indice]
                
                # 1. Registra o voto que o jogador alvo recebeu
                votos_recebidos[voto_nome] += 1
                
                # 2. Contagem de pontos (Placar): 
                # Só ganha ponto se votou no impostor E se quem está votando NÃO for o próprio impostor
                if voto_nome == impostor and jogador != impostor:
                    placar[jogador] += 1
                    
                limpar_tela_enter()
                break # Encerra o turno deste jogador
            
            else:
                print("Voto inválido. Escolha um número da lista.")
                limpar_tela_enter()
                
        except ValueError:
            # Evita que o programa quebre se o usuário digitar uma letra
            print("Entrada inválida. Por favor, digite apenas números.")
            limpar_tela_enter()


# --- APURAÇÃO DA VOTAÇÃO ---
limpar_tela()
print("====================================")
print("RESULTADO DA VOTAÇÃO DA CASA")
print("====================================\n")

# Exibe quantos votos cada um recebeu
for nome, qtd_votos in votos_recebidos.items():
    print(f"{nome}: {qtd_votos} voto(s)")

print("-" * 30)

# Descobre qual foi o número máximo de votos recebidos por alguém
max_votos = max(votos_recebidos.values())

# Filtra quem recebeu esse número máximo de votos (pode haver empate)
mais_votados = [nome for nome, votos in votos_recebidos.items() if votos == max_votos]

# Exibe o resultado final
if len(mais_votados) > 1:
    print(f"Houve um empate! Os mais votados foram: {', '.join(mais_votados)} com {max_votos} votos.")
else:
    print(f"O jogador mais expulso/votado foi: {mais_votados[0]} com {max_votos} votos.")

# Verifica se a casa conseguiu votar no impostor
if impostor in mais_votados:
    print("\n🎯 A casa conseguiu identificar e eliminar o impostor!")
else:
    placar[impostor] += 2
    print(f"\n❌ A casa eliminou um inocente! O impostor era {impostor}.")

limpar_tela_enter()
    
# --- 5. PONTOS DE CADA JOGADOR ---
print("\n====================================")
print("PLACAR FINAL")
print("====================================\n")

# Ordena o placar do maior para o menor (reverse=True)
placar_ordenado = sorted(placar.items(), key=lambda item: item[1], reverse=True)

# Exibe o placar formatado com a posição de cada um
for posicao, (nome, pontos) in enumerate(placar_ordenado, start=1):
    print(f"{posicao}º Lugar | {nome}: {pontos} ponto(s)")