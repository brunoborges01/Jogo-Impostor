"""
import random
import os

def limpar_tela():
    os.system('cls')
    
def limpar_tela_enter():
    input("\nPressione [ENTER] para continuar...")
    os.system('cls')

limpar_tela()

# --- CONFIGURAÇÕES INICIAIS ---
jogadores = ["Bruno", "Julia", "Celina"]
placar = {}
historico_impostores = [] 
parar_jogo = 0

comidas = ["Açaí", "Alfajor", "Arroz Doce", "Bacon", "Batata Frita", "Beijinho", "Bicho de Pé", "Bife à Parmegiana", "Bolo de Cenoura", "Bolo de Chocolate", "Brigadeiro", "Brownie", "Cachorro Quente", "Cajuzinho", "Canjica", "Cheesecake", "Churros", "Cocada", "Coxinha", "Croissant", "Doce de Leite", "Empanada", "Esfiha", "Farofa", "Feijoada", "Frango Assado", "Frango Frito", "Goiabada", "Hambúrguer", "Kibe", "Lasanha", "Macarrão", "Mandioca Frita", "Misto Quente", "Mousse", "Nhoque", "Omelete", "Paçoca", "Pamonha", "Panqueca", "Pastel", "Pão Francês", "Pão de Alho", "Pão de Mel", "Pão de Queijo", "Pé de Moleque", "Picanha", "Pipoca", "Pizza", "Polenta", "Pudim", "Purê de Batata", "Risoto", "Salada", "Sanduíche Natural", "Sashimi", "Sonho", "Sopa", "Sorvete", "Strogonoff", "Sushi", "Suspiro", "Tacos", "Tapioca", "Temaki", "Torresmo", "Torta de Limão", "Trufa", "Waffle", "Yakisoba"]
perguntas = ["Você prefere comer isso no café da manhã, almoço, janta ou na madrugada?", "É o tipo de comida que você divide com os outros ou come escondido para não dar um pedaço?", "Isso combina mais com um refrigerante trincando, um suco natural ou uma cerveja?", "Qual o molho que não pode faltar de jeito nenhum na hora de comer isso?", "Você acha que essa comida fica melhor no dia seguinte, depois de 'curtir' na geladeira?", "Isso faz muita sujeira para comer ou dá para comer no sofá de boa sem sujar nada?", "Você tem alguma memória de infância ligada a essa comida?", "Dá para comer isso todo dia ou é daquelas coisas que enjoam fácil?", "Você prefere a versão caseira ou a comprada pronta no restaurante/fast-food?", "Se você tivesse que comer isso pelo resto da vida, você aguentaria?", "É melhor comer isso quando está chovendo e fazendo frio, ou num dia ensolarado?", "Você já tentou fazer isso em casa e a receita deu completamente errado?", "Qual o acompanhamento perfeito que eleva essa comida para outro nível?", "Isso é comida de fim de semana ou é o que salva na correria da semana?", "Você come isso puro ou gosta de misturar tudo no prato antes de dar a primeira garfada?", "Tem alguma versão 'gourmet' disso que você acha pura frescura e prefere a tradicional?", "É o tipo de coisa que você come quando está triste para dar aquela melhorada no humor?", "Você costuma pedir isso no delivery ou prefere sair de casa para comer na hora?", "Já passou mal de tanto comer isso e prometeu que nunca mais ia comer (mas voltou)?", "Se tivesse que tirar um ingrediente clássico dessa receita para sempre, qual você tiraria?", "Você acha que essa comida é superestimada (famosa à toa) ou merece mesmo a fama que tem?", "Combina mais assistir a um filme comendo isso no sofá ou numa mesa conversando com amigos?", "Você gosta disso com muita pimenta ou prefere zero ardência?", "É uma comida que pesa e enche rápido ou dá para comer um monte sem perceber?", "Você prefere as bordas e partes crocantes ou o meinho que é mais macio/cremoso?", "Como é o cheiro que essa comida deixa na casa quando está sendo preparada?", "Você costuma tacar queijo extra nisso ou acha que estraga o sabor original?", "Já comeu alguma versão vegana ou vegetariana disso que te surpreendeu de verdade?", "Isso é o tipo de prato que você só sabe fazer lendo a receita passo a passo ou faz de olho?", "Qual a bebida que menos combina com isso e que estragaria toda a sua experiência?", "Você tem algum jeito esquisito ou diferente da maioria das pessoas na hora de comer isso?", "É uma comida que te dá aquele sono pesado depois de comer ou te dá energia?", "Você acha que a aparência dessa comida importa ou sendo gostosa é o que vale, mesmo sendo feia?", "Isso para você funciona como o prato principal ou serve mais como um petisco/entrada?", "Qual o maior crime ou erro que alguém pode cometer na hora de preparar isso?", "Você prefere a textura mais firme e crocante ou aquela que derrete na boca?", "Essa comida te lembra alguma viagem específica ou lugar que você já visitou?", "Você costuma raspar o prato ou a panela até o final quando come isso?", "É o tipo de coisa que você come com pressa de pé ou gosta de sentar e saborear cada mordida?", "Você já comeu isso em alguma barraca de rua pós-festa de madrugada?", "Qual a pior versão ou sabor bizarro dessa comida que você já teve o desprazer de provar?", "Você costuma afogar isso no ketchup e na maionese ou prefere manter o gosto original?", "Dá para levar isso na marmita para o trabalho ou fica com gosto de geladeira depois de requentar?", "Você acha que essa comida costuma ser cara para o que oferece ou é um bom custo-benefício?", "Isso realmente mata a sua fome de leão ou você come só pela pura gula de mastigar algo?", "Qual o tamanho ideal da porção disso para você sair da mesa 100% satisfeito?", "Você gosta de comer isso misturado com coisas doces (pegada agridoce) ou acha isso bizarro?", "Essa é a comida que você pediria como sua 'última refeição' se pudesse escolher?", "Você prefere comprar os ingredientes soltos e montar do seu jeito ou comprar o kit todo pronto?", "É fácil achar um lugar bom que venda isso na sua cidade ou é quase uma caça ao tesouro?"]

# --- MENU PRINCIPAL ---
while True:
    print("Jogo do Impostor\n1 - Adicionar Jogador.\n2 - Remover Jogador\n3 - Iniciar o Jogo.")
    if jogadores: print(f"Lista de Jogadores: {', '.join(jogadores)}")
    try:
        escolha = int(input("\nEscolha um numero: "))
        match escolha:
            case 1: 
                nome = (input("Nome: ").title())
                if nome in jogadores:
                    print(f"Jogador {nome}, já existe.")
                    limpar_tela_enter()
                else:
                    jogadores.append(nome)
                limpar_tela()
            case 2:
                nome = input("Nome a remover: ").title()
                if nome in jogadores: 
                    jogadores.remove(nome)
                else:
                    print("Não existe esse jogador")
                    limpar_tela_enter()
            case 3:
                if len(jogadores) < 3: print("Mínimo 3 jogadores."); limpar_tela_enter()
                else: break
    except ValueError: print("Digite apenas números."); limpar_tela_enter()

# Prepara o placar antes do loop iniciar
for nome in jogadores: 
    placar[nome] = 0

comidas_usadas = []

# --- LOOP DE RODADAS ---
while True:
    # verifica as comidas já utilizadas:
    comidas_disponiveis = []
    for c in comidas:
        if c not in comidas_usadas:
            comidas_disponiveis.append(c)

    # verifica se a lista está vazia
    if not comidas_disponiveis: 
        print("Acabaram as comidas!"); break
    
    comida_sorteada = random.choice(comidas_disponiveis) # sorteia a comida
    comidas_usadas.append(comida_sorteada) # coloca a comida sorteada na lista de comidas já utilizadas
    
    # --- LÓGICA DO IMPOSTOR (MÁX 2 VEZES SEGUIDAS) ---
    candidatos_impostor = jogadores.copy()
    
    # Verifica se já ocorreram pelo menos 2 rodadas
    if len(historico_impostores) >= 2:
        ultimo = historico_impostores[-1]
        penultimo = historico_impostores[-2]
        
        # Se a mesma pessoa foi impostora nas duas últimas rodadas seguidas
        if ultimo == penultimo and ultimo in candidatos_impostor:
            candidatos_impostor.remove(ultimo) # Fica de fora do sorteio SÓ nesta rodada
            
    # Sorteia o impostor e salva no histórico
    impostor = random.choice(candidatos_impostor)
    historico_impostores.append(impostor)
    # -----------------------------------------

    votos_recebidos = {}  # Cria um dicionário vazio
    for jogador in jogadores:
        votos_recebidos[jogador] = 0  # Adiciona o jogador com 0 votos
    
    # Revelação
    for jogador in jogadores:
        input(f"\nPasse a tela para {jogador} e aperte [ENTER]..."); limpar_tela()
        print(f"--- SEGREDO DE {jogador.upper()} ---\n")
        if jogador == impostor: print("🚨 VOCÊ É O IMPOSTOR! 🚨")
        else: print(f"✅ VOCÊ É CIDADÃO!\nComida: {comida_sorteada}")
        input("\n[ENTER] para esconder..."); limpar_tela()
    
    # Perguntas
    p = random.sample(jogadores, len(jogadores)) # random.sample -> sorteia o jogador apenas 1 vez e coloca como primeiro
    r = p[1:] + [p[0]] # pega a primeira pessoa e joga lá pro final da lista
    perguntas_sort = random.sample(perguntas, len(jogadores)) # (lista de itens que serão utilizados , quantidade de itens a serem sorteados)
    
    input("Hora das perguntas...")
    total_perguntas = len(perguntas_sort)
    # O enumerate cria um contador 'i' que começa no 0, 1, 2...
    for i, (qp, qr, perg) in enumerate(zip(p, r, perguntas_sort)):
        limpar_tela()
        print(f"🎙️ {qp} pergunta para {qr}:\n 💬 {perg}\n")
            
        # Se a volta atual (i) for diferente da última volta...
        if i != (total_perguntas - 1): 
            input("\nAperte enter para a próxima pergunta...")
        else:
            input("Hora da votação.")
    limpar_tela()
    
    # Votação Corrigida
    for jogador in jogadores:
        print(f"\nVez de: {jogador}")
        # List Compression: opcoes = [j for j in jogadores if j != jogador]
        opcoes = []
        for j in jogadores:
            if j != jogador:
                opcoes.append(j) # no list compreesion, ele mesmo adiciona

        while True: # Adicionamos um loop para garantir que o voto seja válido
            for i, nome in enumerate(opcoes): 
                print(f"{i} - {nome}")
            
            try:
                voto = int(input("Número: "))
                # Valida se o número está dentro das opções disponíveis
                if 0 <= voto < len(opcoes):
                    alvo = opcoes[voto]
                    votos_recebidos[alvo] += 1
                    if alvo == impostor and jogador != impostor: 
                        placar[jogador] += 1
                    break # Sai do while apenas se o voto for válido
                else:
                    print("Número inválido! Escolha um da lista acima.")
                    limpar_tela_enter()
            except ValueError:
                print("Entrada inválida! Digite apenas o número.")
        
        limpar_tela()

    # Resultado e Mecânicas do Impostor
    max_votos = max(votos_recebidos.values()) # max -> pega o maior valor da lista
    mais_votados = []  # 1. Começamos criando uma lista vazia
    for j, v in votos_recebidos.items():  # 2. Passamos por cada par de jogador (j) e seus votos (v)
        if v == max_votos:                # 3. Verificamos se os votos dele são iguais à pontuação máxima
            mais_votados.append(j)        # 4. Se for, adicionamos o nome dele na nossa lista

    # BÔNUS: Impostor ganha +2 se não for a maioria dos votos
    if impostor not in mais_votados:
        print("🎉 O Impostor sobreviveu à votação e ganhou 2 pontos!")
        placar[impostor] += 2
        eliminado = mais_votados[0]
        print(f"🔥 Eliminado: {eliminado}")
        
    elif len(mais_votados) > 1:
        print(f"⚖️ EMPATE entre {', '.join(mais_votados)}")
        if impostor in mais_votados:
            print("🎉 O Impostor sobreviveu à votação no empate e ganhou 2 pontos!")
            placar[impostor] += 2  
            
    else:
        print(f"🚨 A casa caiu! O Impostor {impostor} foi descoberto pela maioria.")
            
    
    # Palpite do Impostor
    print(f"\n🤐 O Impostor era: {impostor}")
    opcoes_palpite = random.sample([c for c in comidas if c != comida_sorteada], 4) + [comida_sorteada]
    random.shuffle(opcoes_palpite)
    
    print(f"\n{impostor}, você foi descoberto! Qual era a comida secreta?")
    for i, c in enumerate(opcoes_palpite): print(f"{i} - {c}")
    
    # Loop para garantir uma entrada válida
    while True:
        try:
            palpite = int(input("Escolha o número da comida (0-4): "))
            if 0 <= palpite <= 4:
                if opcoes_palpite[palpite] == comida_sorteada:
                    print("🎯 ACERTOU! O impostor ganha +1 ponto!")
                    placar[impostor] += 1
                else:
                    print(f"❌ Errou! A comida era {comida_sorteada}.")
                break # Sai do while se a entrada for válida
            else:
                print("Por favor, digite um número entre 0 e 4.")
        except ValueError:
            print("Entrada inválida! Digite apenas o número correspondente.")

    print("\n🏆 PLACAR 🏆")
    for pos, (nome, pts) in enumerate(sorted(placar.items(), key=lambda x: x[1], reverse=True), 1):
        print(f"{pos}º | {nome}: {pts} ponto(s)")

    # Decisão de continuar SEM RESTRIÇÕES DE LIMITE
    parar_jogo += 1
    if ( parar_jogo >= len(jogadores)): 
        break
    else:
        resposta = input("\nJogar mais uma? (s/n): ").lower() 
        if ( resposta != 's' ) :
            break
    
        
    limpar_tela()
    """