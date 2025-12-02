"""
Aplicações Práticas de Algoritmos em Grafos
============================================
Implementação de problemas reais para demonstrar a utilidade de cada algoritmo.

Autores: [COLOQUE OS NOMES DA EQUIPE AQUI]
Data: Dezembro 2025
"""

from grafo import Grafo
from bfs_dfs import BFS, DFS
from bellman_ford_dijkstra import BellmanFord, Dijkstra
from mst_kruskal_prim import Kruskal, Prim


class AplicacaoRedeSocial:
    """
    APLICAÇÃO: BFS - Rede Social
    Encontra o menor número de conexões entre duas pessoas.
    """
    
    @staticmethod
    def criar_rede():
        """
        Cria uma rede social com 20 pessoas.
        Todas as conexões têm peso 1 (uma amizade).
        """
        grafo = Grafo(direcionado=False)
        
        conexoes = [
            (0, 1), (0, 2), (1, 3), (2, 3), (3, 4),
            (5, 6), (5, 7), (6, 8), (7, 8), (8, 9),
            (10, 11), (10, 12), (11, 13), (12, 13), (13, 14),
            (15, 16), (15, 17), (16, 18), (17, 18), (18, 19),
            (4, 5), (9, 10), (14, 15), (19, 0),
            (2, 7), (6, 11), (12, 16)
        ]
        
        for u, v in conexoes:
            grafo.adicionar_aresta(u, v, 1)
        
        return grafo
    
    @staticmethod
    def obter_nomes():
        """Retorna nomes fictícios para as pessoas."""
        return {
            0: "Alice", 1: "Bruno", 2: "Carlos", 3: "Diana", 4: "Eduardo",
            5: "Fernanda", 6: "Gabriel", 7: "Helena", 8: "Igor", 9: "Julia",
            10: "Lucas", 11: "Maria", 12: "Nicolas", 13: "Olivia", 14: "Pedro",
            15: "Quésia", 16: "Rafael", 17: "Sofia", 18: "Thiago", 19: "Vitória"
        }
    
    @staticmethod
    def executar_exemplo():
        """Demonstra BFS para encontrar conexões."""
        print("=" * 80)
        print("🌐 APLICAÇÃO PRÁTICA: REDE SOCIAL - Encontrar Conexões")
        print("=" * 80)
        print("\nProblema: Quantos graus de separação existem entre duas pessoas?")
        print("Algoritmo: BFS (Breadth-First Search)")
        print("Por quê: BFS encontra o MENOR NÚMERO de conexões (todas têm peso 1)")
        print("\n" + "-" * 80)
        
        grafo = AplicacaoRedeSocial.criar_rede()
        nomes = AplicacaoRedeSocial.obter_nomes()
        
        origem = 0
        destino = 9
        
        print(f"\n🔍 Buscando conexão entre {nomes[origem]} e {nomes[destino]}...")
        print()
        
        resultado = BFS.buscar(grafo, origem, destino, mostrar_passos=False)
        
        if resultado['caminho']:
            print(f"\n✓ CONEXÃO ENCONTRADA!")
            print(f"  Graus de separação: {len(resultado['caminho']) - 1}")
            print(f"  Caminho de amizades:")
            
            for i, pessoa in enumerate(resultado['caminho']):
                if i < len(resultado['caminho']) - 1:
                    print(f"    {nomes[pessoa]} → conhece → {nomes[resultado['caminho'][i+1]]}")
            
            print(f"\n💡 Insight: {nomes[origem]} e {nomes[destino]} estão a {len(resultado['caminho']) - 1} amigos de distância!")
        
        print("\n" + "=" * 80)


class AplicacaoDependencias:
    """
    APLICAÇÃO: DFS - Sistema de Dependências
    Detecta ciclos em instalação de pacotes/bibliotecas.
    """
    
    @staticmethod
    def criar_sistema():
        """
        Cria um sistema de dependências de pacotes.
        Grafo direcionado: A → B significa "A depende de B"
        """
        grafo = Grafo(direcionado=True)
        
        dependencias = [
            (0, 1), (0, 2),
            (1, 3), (1, 4),
            (2, 5), (2, 4),
            (3, 6),
            (5, 4), (5, 7),
            (6, 8),
            (7, 4),
            (9, 10), (10, 11), (11, 12), (12, 13), (13, 14),
            (14, 15), (15, 16), (16, 17), (17, 9),
        ]
        
        for u, v in dependencias:
            grafo.adicionar_aresta(u, v, 1)
        
        return grafo
    
    @staticmethod
    def obter_nomes():
        """Retorna nomes dos pacotes."""
        return {
            0: "AppPrincipal", 1: "WebFramework", 2: "Database", 3: "HTTPClient",
            4: "Logger", 5: "ConnPool", 6: "SSLLibrary", 7: "ThreadMgr",
            8: "Crypto", 9: "PkgA", 10: "PkgB", 11: "PkgC", 12: "PkgD",
            13: "PkgE", 14: "PkgF", 15: "PkgG", 16: "PkgH", 17: "PkgI"
        }
    
    @staticmethod
    def detectar_ciclo(grafo, inicio=0):
        """Usa DFS para detectar ciclos."""
        visitados = set()
        pilha_recursao = set()
        ciclo_encontrado = []
        
        def dfs_ciclo(v, caminho):
            visitados.add(v)
            pilha_recursao.add(v)
            caminho.append(v)
            
            for vizinho, _ in grafo.obter_vizinhos(v):
                if vizinho not in visitados:
                    if dfs_ciclo(vizinho, caminho[:]):
                        return True
                elif vizinho in pilha_recursao:
                    idx = caminho.index(vizinho)
                    ciclo_encontrado.extend(caminho[idx:] + [vizinho])
                    return True
            
            pilha_recursao.remove(v)
            return False
        
        for vertice in grafo.obter_vertices():
            if vertice not in visitados:
                if dfs_ciclo(vertice, []):
                    return ciclo_encontrado
        
        return []
    
    @staticmethod
    def executar_exemplo():
        """Demonstra DFS para detectar ciclos."""
        print("=" * 80)
        print("📦 APLICAÇÃO PRÁTICA: SISTEMA DE DEPENDÊNCIAS - Detectar Ciclos")
        print("=" * 80)
        print("\nProblema: Evitar dependências circulares na instalação de pacotes")
        print("Algoritmo: DFS (Depth-First Search)")
        print("Por quê: DFS explora profundamente e detecta ciclos eficientemente")
        print("\n" + "-" * 80)
        
        grafo = AplicacaoDependencias.criar_sistema()
        nomes = AplicacaoDependencias.obter_nomes()
        
        print(f"\n🔍 Verificando dependências de {len(grafo.obter_vertices())} pacotes...")
        
        ciclo = AplicacaoDependencias.detectar_ciclo(grafo)
        
        if ciclo:
            print(f"\n⚠️  CICLO DETECTADO!")
            print(f"  Tamanho do ciclo: {len(ciclo) - 1} pacotes")
            print(f"  Dependência circular:")
            
            for i in range(len(ciclo) - 1):
                print(f"    {nomes[ciclo[i]]} → depende de → {nomes[ciclo[i+1]]}")
            
            print(f"\n❌ ERRO: Impossível instalar! Dependência circular detectada.")
            print(f"   Solução: Remover uma das dependências do ciclo.")
        else:
            print(f"\n✓ Sistema OK! Nenhum ciclo detectado.")
            print(f"  Instalação pode prosseguir normalmente.")
        
        print("\n" + "=" * 80)


class AplicacaoJogoRPG:
    """
    APLICAÇÃO: Dijkstra - Pathfinding em Jogo RPG
    Encontra melhor caminho considerando diferentes custos de terreno.
    """
    
    @staticmethod
    def criar_mapa():
        """
        Cria um mapa de jogo com diferentes tipos de terreno.
        Pesos representam custo de movimento (energia/tempo).
        """
        grafo = Grafo(direcionado=False)
        
        
        conexoes = [
            (0, 1, 1),
            (1, 2, 1),
            (2, 3, 3),
            (0, 4, 5),
            (4, 5, 5),
            (5, 6, 5),
            (6, 7, 3),
            (1, 8, 10),
            (8, 9, 10),
            (9, 10, 10),
            (10, 11, 5),
            
            (3, 12, 15),
            (12, 13, 15),
            (13, 14, 15),
            
            (7, 11, 3),
            (11, 14, 5),
            (6, 11, 5),
            (5, 8, 10),
            
            (14, 15, 3),
            (15, 16, 1),
            (16, 17, 3),
            (17, 0, 5),
        ]
        
        for u, v, peso in conexoes:
            grafo.adicionar_aresta(u, v, peso)
        
        return grafo
    
    @staticmethod
    def obter_nomes():
        return {
            0: "Vila", 1: "Cidade", 2: "Porto", 3: "Farol",
            4: "Floresta1", 5: "Floresta2", 6: "Clareira", 7: "Acampamento",
            8: "PéMontanha", 9: "MeioMontanha", 10: "Topo", 11: "Vale",
            12: "Pântano1", 13: "Pântano2", 14: "Ruínas", 15: "Templo",
            16: "Portal", 17: "Castelo"
        }
    
    @staticmethod
    def executar_exemplo():
        print("=" * 80)
        print("🎮 APLICAÇÃO PRÁTICA: JOGO RPG - Pathfinding com Terrenos")
        print("=" * 80)
        print("\nProblema: Encontrar caminho mais rápido considerando custos de terreno")
        print("Algoritmo: Dijkstra")
        print("Por quê: Encontra caminho de MENOR CUSTO com pesos positivos diferentes")
        print("\nLegenda de Terrenos:")
        print("  • Estrada (1): Rápido, fácil")
        print("  • Grama (3): Normal")
        print("  • Floresta (5): Lento, vegetação densa")
        print("  • Montanha (10): Muito lento, íngreme")
        print("  • Pântano (15): Extremamente lento, perigoso")
        print("\n" + "-" * 80)
        
        grafo = AplicacaoJogoRPG.criar_mapa()
        nomes = AplicacaoJogoRPG.obter_nomes()
        
        origem = 0 
        destino = 14
        
        print(f"\n🗺️  Missão: Ir de {nomes[origem]} até {nomes[destino]}")
        print()
        
        resultado = Dijkstra.menor_caminho(grafo, origem, destino, mostrar_passos=False)
        
        if resultado['caminho']:
            print(f"\n✓ MELHOR ROTA ENCONTRADA!")
            print(f"  Custo total de energia: {resultado['custo']:.1f} pontos")
            print(f"  Número de locais: {len(resultado['caminho'])}")
            print(f"\n  📍 Roteiro detalhado:")
            
            for i in range(len(resultado['caminho']) - 1):
                atual = resultado['caminho'][i]
                proximo = resultado['caminho'][i + 1]
                
                for viz, peso in grafo.obter_vizinhos(atual):
                    if viz == proximo:
                        terreno = "Estrada" if peso == 1 else \
                                 "Grama" if peso == 3 else \
                                 "Floresta" if peso == 5 else \
                                 "Montanha" if peso == 10 else "Pântano"
                        
                        print(f"    {i+1}. {nomes[atual]:15} → {nomes[proximo]:15} (Custo: {peso:2}, Terreno: {terreno})")
                        break
            
            print(f"\n💡 Dica: Rotas alternativas existem, mas custam mais energia!")
        
        print("\n" + "=" * 80)


class AplicacaoMercadoFinanceiro:
    @staticmethod
    def criar_mercado():
        """
        Cria um mercado de câmbio com taxas de conversão.
        Usamos -log(taxa) como peso para detectar arbitragem.
        """
        import math
        
        grafo = Grafo(direcionado=True)
        
        
        taxas = [
            (0, 1, 0.85),
            (0, 2, 5.30),
            (0, 3, 0.75),
            (0, 4, 110.5),
            
            (1, 0, 1.18),
            (1, 2, 6.24),
            (1, 3, 0.88),
            (1, 4, 130.2),  
            
            (2, 0, 0.189),
            (2, 1, 0.160),
            (2, 3, 0.142),
            (2, 4, 20.85),
            
            (3, 0, 1.33),
            (3, 1, 1.14),
            (3, 2, 7.05),
            (3, 4, 147.0),
            
            (4, 0, 0.00905),
            (4, 1, 0.00768),
            (4, 2, 0.0480),
            (4, 3, 0.00680),
            
            (0, 5, 0.92), (5, 0, 1.09),
            (0, 6, 1.35), (6, 0, 0.74),
            (0, 7, 1.27), (7, 0, 0.79),
            (0, 8, 7.85), (8, 0, 0.127),
            (0, 9, 10.5), (9, 0, 0.095),
            (0, 10, 0.91), (10, 0, 1.10),
            (0, 11, 16.8), (11, 0, 0.060),
            (0, 12, 4.32), (12, 0, 0.231),
            (0, 13, 1.41), (13, 0, 0.709),
            (0, 14, 82.5), (14, 0, 0.012),
            (0, 15, 3.67), (15, 0, 0.272),
            
            (5, 6, 1.47), (6, 7, 0.94), (7, 5, 0.73),
        ]
        
        import math
        for u, v, taxa in taxas:
            peso = -math.log(taxa)
            grafo.adicionar_aresta(u, v, peso)
        
        return grafo
    
    @staticmethod
    def obter_nomes():
        return {
            0: "USD", 1: "EUR", 2: "BRL", 3: "GBP", 4: "JPY",
            5: "CHF", 6: "AUD", 7: "CAD", 8: "HKD", 9: "SEK",
            10: "SGD", 11: "MXN", 12: "PLN", 13: "NZD", 14: "INR", 15: "AED"
        }
    
    @staticmethod
    def executar_exemplo():
        print("=" * 80)
        print("💰 APLICAÇÃO PRÁTICA: MERCADO FINANCEIRO - Arbitragem de Moedas")
        print("=" * 80)
        print("\nProblema: Detectar oportunidades de lucro em conversões de moeda")
        print("Algoritmo: Bellman-Ford")
        print("Por quê: Detecta CICLOS NEGATIVOS (lucro) e trabalha com pesos negativos")
        print("\nConceito: Arbitragem = converter moedas em ciclo e obter lucro")
        print("Exemplo: USD → EUR → GBP → USD com mais dólares que começou")
        print("\n" + "-" * 80)
        
        grafo = AplicacaoMercadoFinanceiro.criar_mercado()
        nomes = AplicacaoMercadoFinanceiro.obter_nomes()
        
        print(f"\n📊 Analisando {len(grafo.obter_vertices())} moedas no mercado...")
        print()
        
        origem = 0
        destino = 0
        
        resultado = BellmanFord.menor_caminho(grafo, origem, destino, mostrar_passos=False)
        
        if 'ciclo_negativo' in resultado and resultado['ciclo_negativo']:
            print(f"⚠️  OPORTUNIDADE DE ARBITRAGEM DETECTADA!")
            print(f"\n  Existe um ciclo onde é possível obter LUCRO!")
            print(f"  Ciclo negativo encontrado no grafo.")
            print(f"\n  💡 Estratégia: Converter moedas em ciclo repetidamente para lucro infinito")
            print(f"  ⚠️  Nota: Na prática, mercados corrigem rapidamente essas anomalias")
        else:
            print(f"✓ Mercado em equilíbrio")
            print(f"  Nenhuma oportunidade de arbitragem detectada no momento.")
        
        print("\n" + "=" * 80)


class AplicacaoRedeEletrica:
    """
    APLICAÇÃO: MST (Kruskal/Prim) - Rede Elétrica
    Conecta cidades com menor custo de cabeamento.
    """
    
    @staticmethod
    def criar_rede():
        """
        Cria uma rede de cidades para conectar energia elétrica.
        Pesos = custo de instalação de cabos (milhares de reais).
        """
        grafo = Grafo(direcionado=False)
        
        conexoes = [
            (0, 1, 12),  
            (0, 2, 15),  
            (1, 2, 8),   
            (1, 3, 20),  
            (2, 3, 18),  
            
            (3, 4, 25),   
            (3, 5, 30),   
            (4, 5, 22),   
            (4, 6, 28),   
            (5, 6, 24),   
            
            (6, 7, 35),
            (6, 8, 40),   
            (7, 8, 32),   
            (7, 9, 38),   
            (8, 9, 36),   
            
            (0, 4, 45),
            (1, 5, 42),   
            (2, 6, 48),   
            (3, 7, 50),   
            (5, 9, 44),   
            
            (9, 10, 30),
            (10, 11, 26), 
            (11, 12, 28), 
            (12, 13, 33), 
            (13, 14, 29), 
            (14, 15, 31), 
            (15, 16, 27), 
            (16, 17, 34), 
            
            (17, 0, 55),  
            (10, 6, 37),  
            (12, 8, 41),
        ]
        
        for u, v, custo in conexoes:
            grafo.adicionar_aresta(u, v, custo)
        
        return grafo
    
    @staticmethod
    def obter_nomes():
        return {
            0: "Capital", 1: "CidadeA", 2: "CidadeB", 3: "CidadeC",
            4: "CidadeD", 5: "CidadeE", 6: "CidadeF", 7: "VilaG",
            8: "VilaH", 9: "VilaI", 10: "DistritoJ", 11: "DistritoK",
            12: "PovoadoL", 13: "PovoadoM", 14: "FazendaN", 15: "SítioO",
            16: "ChácaraP", 17: "RanchoQ"
        }
    
    @staticmethod
    def executar_exemplo():
        print("=" * 80)
        print("⚡ APLICAÇÃO PRÁTICA: REDE ELÉTRICA - Conectar Cidades")
        print("=" * 80)
        print("\nProblema: Levar energia para todas as cidades com MENOR CUSTO total")
        print("Algoritmo: MST - Árvore Geradora Mínima (Kruskal ou Prim)")
        print("Por quê: Conecta TODOS os vértices sem ciclos e com menor custo")
        print("\nCustos em milhares de R$")
        print("\n" + "-" * 80)
        
        grafo = AplicacaoRedeEletrica.criar_rede()
        nomes = AplicacaoRedeEletrica.obter_nomes()
        
        print(f"\n🏙️  Projeto: Conectar {len(grafo.obter_vertices())} localidades")
        print(f"   Origem da energia: {nomes[0]}")
        print()
        
        print("📊 Calculando melhor configuração com Kruskal...")
        resultado_kruskal = Kruskal.mst(grafo, mostrar_passos=False)
        
        print(f"\n✓ PROJETO OTIMIZADO!")
        print(f"  Custo total: R$ {resultado_kruskal['custo_total']:.0f} mil")
        print(f"  Número de cabos: {len(resultado_kruskal['arestas'])}")
        print(f"\n  🔌 Conexões necessárias:")
        
        arestas_ordenadas = sorted(resultado_kruskal['arestas'], key=lambda x: x[2])
        
        for i, (u, v, custo) in enumerate(arestas_ordenadas[:10], 1):
            print(f"    {i:2}. {nomes[u]:12} ↔ {nomes[v]:12}  R$ {custo:.0f} mil")
        
        if len(arestas_ordenadas) > 10:
            print(f"    ... e mais {len(arestas_ordenadas) - 10} conexões")
        
        todas_arestas = grafo.obter_arestas()
        custo_total_completo = sum(peso for _, _, peso in todas_arestas)
        economia = custo_total_completo - resultado_kruskal['custo_total']
        
        print(f"\n💡 Economia: R$ {economia:.0f} mil")
        print(f"   (vs. construir todas as conexões possíveis)")
        
        print("\n" + "=" * 80)


def menu_principal():    
    aplicacoes = {
        '1': ("Rede Social (BFS)", AplicacaoRedeSocial.executar_exemplo),
        '2': ("Sistema de Dependências (DFS)", AplicacaoDependencias.executar_exemplo),
        '3': ("Jogo RPG (Dijkstra)", AplicacaoJogoRPG.executar_exemplo),
        '4': ("Mercado Financeiro (Bellman-Ford)", AplicacaoMercadoFinanceiro.executar_exemplo),
        '5': ("Rede Elétrica (MST)", AplicacaoRedeEletrica.executar_exemplo),
        '6': ("Executar TODAS as aplicações", None),
    }
    
    while True:
        print("\n" + "=" * 80)
        print("🌟 APLICAÇÕES PRÁTICAS DE ALGORITMOS EM GRAFOS")
        print("=" * 80)
        print("\nEscolha uma aplicação para demonstrar:\n")
        
        for key, (descricao, _) in aplicacoes.items():
            print(f"  [{key}] {descricao}")
        
        print(f"\n  [0] Sair")
        print("\n" + "=" * 80)
        
        escolha = input("\nDigite sua escolha: ").strip()
        
        if escolha == '0':
            print("\n👋 Até logo!")
            break
        elif escolha == '6':
                for key in ['1', '2', '3', '4', '5']:
                    print("\n\n")
                    aplicacoes[key][1]()
                    input("\n⏸️  Pressione ENTER para continuar...")
        elif escolha in aplicacoes and aplicacoes[escolha][1]:
            print("\n\n")
            aplicacoes[escolha][1]()
            input("\n⏸️  Pressione ENTER para voltar ao menu...")
        else:
            print("\n❌ Opção inválida!")


if __name__ == "__main__":
    menu_principal()
