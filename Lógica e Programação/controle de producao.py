import time

# --- 1. Constantes e Critérios de Qualidade ---
PESO_MIN = 95
PESO_MAX = 105
CORES_VALIDAS = ['azul', 'verde']
COMP_MIN = 10
COMP_MAX = 20
CAPACIDADE_CAIXA = 10

# --- 2. Classe para armazenar os dados da Peça ---
class Peca:
    """
    Armazena todos os dados de uma única peça de forma organizada.
    """
    def __init__(self, id_peca, peso, cor, comprimento, aprovada, razoes):
        self.id = id_peca
        self.peso = peso
        self.cor = cor
        self.comprimento = comprimento
        self.aprovada = aprovada  # Booleano (True/False)
        self.razoes = razoes    # Lista de motivos da reprovação

    def __str__(self):
        """
        Representação em string para facilitar a listagem.
        """
        if self.aprovada:
            status = "✅ APROVADA"
        else:
            motivos_str = ", ".join(self.razoes)
            status = f"❌ REPROVADA (Motivos: {motivos_str})"
        
        return (f"  [ID: {self.id}] | {status}\n"
                f"     (Peso: {self.peso}g, Cor: {self.cor}, Comp: {self.comprimento}cm)")

# --- 3. Funções de Lógica de Negócio ---

def avaliar_peca(peso, cor, comprimento):
    """
    Avalia a peça com base nos critérios de qualidade.
    Retorna (True/False, [lista_de_motivos]).
    """
    peca_aprovada = True
    razoes_reprovacao = []

    if not (PESO_MIN <= peso <= PESO_MAX):
        peca_aprovada = False
        razoes_reprovacao.append("Peso")
    if cor not in CORES_VALIDAS:
        peca_aprovada = False
        razoes_reprovacao.append("Cor")
    if not (COMP_MIN <= comprimento <= COMP_MAX):
        peca_aprovada = False
        razoes_reprovacao.append("Comprimento")

    return peca_aprovada, razoes_reprovacao

def obter_dado_numerico(prompt):
    """
    Função auxiliar robusta para garantir a entrada de um número (float).
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("   ERRO: Valor inválido. Digite um número.")

# --- 4. Funções do Menu Interativo ---

def exibir_menu(status_caixa_atual):
    """
    Exibe o menu principal de opções.
    """
    print("\n" + "="*45)
    print("      ⚙️ SISTEMA DE CONTROLE DE QUALIDADE ⚙️")
    print("="*45)
    print(f" (Peças na caixa atual: {status_caixa_atual}/{CAPACIDADE_CAIXA})")
    print("\n1. Cadastrar nova peça")
    print("2. Listar peças (Aprovadas/Reprovadas)")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("6. Sair")
    print("-"*45)

def cadastrar_nova_peca(db_pecas, caixa_atual, caixas_fechadas):
    """
    Opção 1: Pergunta os dados, avalia e armazena a peça.
    """
    print("\n--- 1. Cadastrar Nova Peça ---")
    id_peca = input("   ID da Peça (ex: 'p001'): ").lower()

    if id_peca == 'fim' or id_peca == '':
        print("   ID inválido.")
        return
    
    # Verifica se a peça já existe no nosso "banco de dados" (dicionário)
    if id_peca in db_pecas:
        print(f"   ERRO: A Peça com ID '{id_peca}' já foi cadastrada.")
        return

    # Obtém dados
    peso = obter_dado_numerico("   Peso (g): ")
    cor = input("   Cor: ").lower()
    comprimento = obter_dado_numerico("   Comprimento (cm): ")

    # Avalia
    aprovada, razoes = avaliar_peca(peso, cor, comprimento)

    # Cria o objeto Peca
    nova_peca = Peca(id_peca, peso, cor, comprimento, aprovada, razoes)

    # Armazena a peça no dicionário principal
    db_pecas[id_peca] = nova_peca

    if aprovada:
        print(f"\n   ➡️ RESULTADO: Peça {id_peca} APROVADA.")
        caixa_atual.append(id_peca)
        
        # Verifica se a caixa está cheia
        if len(caixa_atual) == CAPACIDADE_CAIXA:
            # Adiciona uma CÓPIA da caixa atual à lista de caixas fechadas
            caixas_fechadas.append(list(caixa_atual))
            caixa_atual.clear() # Limpa a caixa atual
            print(f"   *** 📦 CAIXA {len(caixas_fechadas)} FECHADA (Completa) ***")
    else:
        motivos_str = ", ".join(razoes)
        print(f"\n   ➡️ RESULTADO: Peça {id_peca} REPROVADA. (Motivos: {motivos_str})")

def listar_pecas(db_pecas):
    """
    Opção 2: Itera pelo dicionário e lista todas as peças,
    separadas por status.
    """
    print("\n--- 2. Listagem de Peças ---")
    if not db_pecas:
        print("   Nenhuma peça cadastrada ainda.")
        return

    # Separa as peças usando list comprehension
    pecas_aprovadas = [p for p in db_pecas.values() if p.aprovada]
    pecas_reprovadas = [p for p in db_pecas.values() if not p.aprovada]

    print("\n--- Peças Aprovadas ---")
    if pecas_aprovadas:
        for peca in pecas_aprovadas:
            print(peca)
    else:
        print("   (Nenhuma peça aprovada)")

    print("\n--- Peças Reprovadas ---")
    if pecas_reprovadas:
        for peca in pecas_reprovadas:
            print(peca)
    else:
        print("   (Nenhuma peça reprovada)")

def remover_peca(db_pecas, caixa_atual, caixas_fechadas):
    """
    Opção 3: Remove uma peça do dicionário principal e
    da caixa atual (se estiver nela).
    """
    print("\n--- 3. Remover Peça ---")
    id_remover = input("   Digite o ID da peça a ser removida: ").lower()

    if id_remover not in db_pecas:
        print(f"   ERRO: Peça com ID '{id_remover}' não encontrada.")
        return

    # Remove a peça do "banco de dados" principal
    peca_removida = db_pecas.pop(id_remover)
    print(f"\n   Peça '{peca_removida.id}' removida com sucesso.")

    # Se a peça estava na caixa atual, remove também
    if id_remover in caixa_atual:
        caixa_atual.remove(id_remover)
        print("   A peça também foi removida da caixa atual.")
    
    # Aviso se a peça já estava em uma caixa fechada
    elif peca_removida.aprovada:
        for caixa in caixas_fechadas:
            if id_remover in caixa:
                print("   AVISO: Esta peça já estava em uma CAIXA FECHADA (Caixa histórica).")
                print("   A remoção afeta o relatório, mas não altera a caixa já registrada.")
                break

def listar_caixas(caixas_fechadas):
    """
    Opção 4: Mostra o conteúdo de todas as caixas já fechadas.
    """
    print("\n--- 4. Listar Caixas Fechadas ---")
    if not caixas_fechadas:
        print("   Nenhuma caixa foi fechada ainda.")
        return

    for i, caixa in enumerate(caixas_fechadas, 1):
        print(f"\n--- Caixa {i} (Completa) ---")
        # Junta os IDs da lista 'caixa' com vírgulas
        ids_formatados = ", ".join(caixa)
        print(f"   Conteúdo: [ {ids_formatados} ]")

def gerar_relatorio_final(db_pecas, caixas_fechadas, caixa_atual):
    """
    Opção 5: Calcula as métricas com base nos dados
    atuais e exibe o relatório.
    """
    print("\n" + "="*40)
    print("     📊 RELATÓRIO DE PRODUÇÃO ATUAL 📊")
    print("="*40)

    # 1. Calcular totais de Aprovadas/Reprovadas
    total_aprovadas = 0
    total_reprovadas = 0
    motivos = {"peso": 0, "cor": 0, "comprimento": 0}

    for peca in db_pecas.values():
        if peca.aprovada:
            total_aprovadas += 1
        else:
            total_reprovadas += 1
            # Registra os motivos da reprovação
            if "Peso" in peca.razoes:
                motivos["peso"] += 1
            if "Cor" in peca.razoes:
                motivos["cor"] += 1
            if "Comprimento" in peca.razoes:
                motivos["comprimento"] += 1

    # 2. Calcular caixas
    total_caixas_fechadas = len(caixas_fechadas)
    pecas_caixa_final = len(caixa_atual)
    
    # Total de caixas usadas (fechadas + a atual, se não estiver vazia)
    if pecas_caixa_final > 0:
        total_caixas_usadas = total_caixas_fechadas + 1
    else:
        total_caixas_usadas = total_caixas_fechadas

    # 3. Exibir o Relatório
    print(f"\n✅ Total de Peças APROVADAS: {total_aprovadas}")
    print(f"❌ Total de Peças REPROVADAS: {total_reprovadas}")

    if total_reprovadas > 0:
        print("\n--- Detalhes da Reprovação ---")
        print(f"   Falhas por Peso:         {motivos['peso']}")
        print(f"   Falhas por Cor:          {motivos['cor']}")
        print(f"   Falhas por Comprimento:  {motivos['comprimento']}")

    print("\n--- Logística ---")
    print(f"📦 Total de Caixas Utilizadas: {total_caixas_usadas}")
    print(f"   (Sendo {total_caixas_fechadas} caixas cheias e 1 caixa atual com {pecas_caixa_final} peças)")

    print("\n" + "="*40)
    # Pausa para o usuário ler o relatório antes de voltar ao menu
    input("Pressione ENTER para voltar ao menu...")


# --- 5. Loop Principal (Main) ---

def main():
    """
    Função principal que gerencia o estado e o loop do menu.
    """
    
    # "Banco de dados" em memória
    # Dicionário armazena { "id_peca": ObjetoPeca }
    todas_as_pecas = {}
    
    # Listas de logística
    caixa_atual = [] # Armazena IDs de peças aprovadas
    caixas_fechadas = [] # Armazena listas de IDs (ex: [ ['p1', 'p2'], ['p3', 'p4'] ])

    while True:
        exibir_menu(len(caixa_atual))
        opcao = input("Escolha uma opção (1-6): ")

        if opcao == '1':
            cadastrar_nova_peca(todas_as_pecas, caixa_atual, caixas_fechadas)
            time.sleep(0.5) # Pequena pausa para fluidez

        elif opcao == '2':
            listar_pecas(todas_as_pecas)
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == '3':
            remover_peca(todas_as_pecas, caixa_atual, caixas_fechadas)
            time.sleep(0.5)

        elif opcao == '4':
            listar_caixas(caixas_fechadas)
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == '5':
            gerar_relatorio_final(todas_as_pecas, caixas_fechadas, caixa_atual)

        elif opcao == '6':
            print("\nEncerrando o sistema. Até logo!")
            break

        else:
            print("\nOpção inválida. Por favor, escolha de 1 a 6.")
            time.sleep(1)


# Garante que o script execute a função main() ao ser iniciado
if __name__ == "__main__":
    main()