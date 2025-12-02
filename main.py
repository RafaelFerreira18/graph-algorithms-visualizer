"""
Programa Principal - Sistema de Demonstração de Algoritmos em Grafos
=====================================================================
Sistema interativo para executar e demonstrar os algoritmos implementados:
- BFS (Busca em Largura)
- DFS (Busca em Profundidade)
- Bellman-Ford (Menor Caminho)
- Dijkstra (Menor Caminho)
- Kruskal (Árvore Geradora Mínima)
- Prim (Árvore Geradora Mínima)

Autores: [COLOQUE OS NOMES DA EQUIPE AQUI]
Data: Dezembro 2025
Disciplina: [NOME DA DISCIPLINA]
"""

import os
import sys
from grafo import Grafo, GrafoExemplos
from bfs_dfs import BFS, DFS
from bellman_ford_dijkstra import BellmanFord, Dijkstra
from mst_kruskal_prim import Kruskal, Prim


def limpar_tela():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa a execução e aguarda o usuário."""
    input("\n\nPressione ENTER para continuar...")


def exibir_cabecalho():
    """Exibe o cabeçalho do programa."""
    print("=" * 70)
    print(" " * 15 + "TRABALHO DE GRAFOS - PARTE 2")
    print(" " * 10 + "Algoritmos de Busca e Caminhamento em Grafos")
    print("=" * 70)
    print("\nAutores: [COLOQUE OS NOMES DA EQUIPE AQUI]")
    print("Disciplina: [NOME DA DISCIPLINA]")
    print("Data: Dezembro 2025")
    print("=" * 70)


def exibir_menu_principal():
    """Exibe o menu principal."""
    print("\n" + "=" * 70)
    print("MENU PRINCIPAL")
    print("=" * 70)
    print("\n1. Algoritmos de Busca (BFS e DFS)")
    print("2. Algoritmos de Menor Caminho (Bellman-Ford e Dijkstra)")
    print("3. Algoritmos de Árvore Geradora Mínima (Kruskal e Prim)")
    print("4. Visualizar Grafos Disponíveis")
    print("5. Executar Todas as Demonstrações")
    print("0. Sair")
    print("\n" + "=" * 70)


def exibir_menu_busca():
    """Exibe o menu de algoritmos de busca."""
    print("\n" + "=" * 70)
    print("ALGORITMOS DE BUSCA")
    print("=" * 70)
    print("\n1. BFS - Busca em Largura")
    print("2. DFS - Busca em Profundidade (Recursivo)")
    print("3. DFS - Busca em Profundidade (Iterativo)")
    print("4. Comparar BFS vs DFS")
    print("0. Voltar ao Menu Principal")
    print("\n" + "=" * 70)


def exibir_menu_menor_caminho():
    """Exibe o menu de algoritmos de menor caminho."""
    print("\n" + "=" * 70)
    print("ALGORITMOS DE MENOR CAMINHO")
    print("=" * 70)
    print("\n1. Bellman-Ford")
    print("2. Dijkstra")
    print("3. Comparar Bellman-Ford vs Dijkstra")
    print("0. Voltar ao Menu Principal")
    print("\n" + "=" * 70)


def exibir_menu_mst():
    """Exibe o menu de algoritmos de MST."""
    print("\n" + "=" * 70)
    print("ALGORITMOS DE ÁRVORE GERADORA MÍNIMA")
    print("=" * 70)
    print("\n1. Kruskal")
    print("2. Prim")
    print("3. Comparar Kruskal vs Prim")
    print("0. Voltar ao Menu Principal")
    print("\n" + "=" * 70)


def selecionar_grafo():
    """Permite ao usuário selecionar um grafo."""
    print("\n" + "=" * 70)
    print("SELEÇÃO DE GRAFO")
    print("=" * 70)
    print("\n1. Mapa de Cidade (20 vértices, não-direcionado)")
    print("2. Rede de Computadores (16 vértices, direcionado)")
    print("\n" + "=" * 70)
    
    while True:
        opcao = input("\nEscolha um grafo (1-2): ").strip()
        if opcao == "1":
            return GrafoExemplos.criar_mapa_cidade(), GrafoExemplos.obter_nomes_mapa_cidade(), False
        elif opcao == "2":
            return GrafoExemplos.criar_rede_computadores(), None, True
        else:
            print("Opção inválida! Tente novamente.")


def obter_vertices(grafo, nomes=None):
    """Solicita vértices de origem e destino."""
    vertices = grafo.obter_vertices()
    
    if nomes:
        print("\nVértices disponíveis:")
        for v in sorted(vertices):
            print(f"  {v}: {nomes[v]}")
    else:
        print(f"\nVértices disponíveis: {sorted(vertices)}")
    
    while True:
        try:
            origem = int(input("\nVértice de origem: "))
            if origem not in vertices:
                print(f"Vértice {origem} não existe! Tente novamente.")
                continue
            break
        except ValueError:
            print("Valor inválido! Digite um número.")
    
    usar_destino = input("Deseja especificar um destino? (s/n): ").strip().lower()
    destino = None
    
    if usar_destino == 's':
        while True:
            try:
                destino = int(input("Vértice de destino: "))
                if destino not in vertices:
                    print(f"Vértice {destino} não existe! Tente novamente.")
                    continue
                break
            except ValueError:
                print("Valor inválido! Digite um número.")
    
    return origem, destino


def executar_bfs():
    """Executa o algoritmo BFS."""
    limpar_tela()
    exibir_cabecalho()
    
    print("\n" + "=" * 70)
    print("ALGORITMO BFS - BUSCA EM LARGURA")
    print("=" * 70)
    
    grafo, nomes, _ = selecionar_grafo()
    origem, destino = obter_vertices(grafo, nomes)
    
    print("\n" + "=" * 70)
    print("EXECUTANDO BFS...")
    print("=" * 70)
    
    resultado = BFS.buscar(grafo, origem, destino)
    
    if resultado['caminho'] and nomes:
        print("\n" + "=" * 70)
        print("CAMINHO COM NOMES DOS LOCAIS:")
        print("=" * 70)
        caminho_nomes = [f"{v} ({nomes[v]})" for v in resultado['caminho']]
        print("  " + " → ".join(caminho_nomes))
    
    pausar()


def executar_dfs(recursivo=True):
    """Executa o algoritmo DFS."""
    limpar_tela()
    exibir_cabecalho()
    
    tipo = "RECURSIVO" if recursivo else "ITERATIVO"
    print("\n" + "=" * 70)
    print(f"ALGORITMO DFS - BUSCA EM PROFUNDIDADE ({tipo})")
    print("=" * 70)
    
    grafo, nomes, _ = selecionar_grafo()
    origem, destino = obter_vertices(grafo, nomes)
    
    print("\n" + "=" * 70)
    print(f"EXECUTANDO DFS {tipo}...")
    print("=" * 70)
    
    resultado = DFS.buscar(grafo, origem, destino, usar_recursao=recursivo)
    
    if resultado['caminho'] and nomes:
        print("\n" + "=" * 70)
        print("CAMINHO COM NOMES DOS LOCAIS:")
        print("=" * 70)
        caminho_nomes = [f"{v} ({nomes[v]})" for v in resultado['caminho']]
        print("  " + " → ".join(caminho_nomes))
    
    pausar()


def comparar_bfs_dfs():
    """Compara BFS e DFS."""
    limpar_tela()
    exibir_cabecalho()
    
    print("\n" + "=" * 70)
    print("COMPARAÇÃO: BFS vs DFS")
    print("=" * 70)
    
    grafo, nomes, _ = selecionar_grafo()
    origem, destino = obter_vertices(grafo, nomes)
    
    if destino is None:
        print("\nPara comparação, é necessário especificar um destino.")
        pausar()
        return
    
    print("\n" + "=" * 70)
    print("EXECUTANDO BFS...")
    print("=" * 70)
    resultado_bfs = BFS.buscar(grafo, origem, destino)
    
    print("\n" + "=" * 70)
    print("EXECUTANDO DFS (RECURSIVO)...")
    print("=" * 70)
    resultado_dfs = DFS.buscar(grafo, origem, destino, usar_recursao=True)
    
    print("\n" + "=" * 70)
    print("COMPARAÇÃO DOS RESULTADOS")
    print("=" * 70)
    
    print(f"\nBFS:")
    if resultado_bfs['caminho']:
        print(f"  Caminho: {resultado_bfs['caminho']}")
        print(f"  Número de arestas: {len(resultado_bfs['caminho']) - 1}")
    else:
        print(f"  Caminho não encontrado")
    
    print(f"\nDFS:")
    if resultado_dfs['caminho']:
        print(f"  Caminho: {resultado_dfs['caminho']}")
        print(f"  Número de arestas: {len(resultado_dfs['caminho']) - 1}")
    else:
        print(f"  Caminho não encontrado")
    
    print("\n" + "-" * 70)
    print("OBSERVAÇÕES:")
    print("-" * 70)
    print("• BFS sempre encontra o caminho com MENOR número de arestas")
    print("• DFS pode encontrar um caminho diferente (não necessariamente o menor)")
    print("• Ambos têm complexidade O(V + E)")
    
    if nomes and resultado_bfs['caminho']:
        print("\n" + "=" * 70)
        print("CAMINHOS COM NOMES:")
        print("=" * 70)
        print("\nBFS:")
        caminho_nomes = [f"{v} ({nomes[v]})" for v in resultado_bfs['caminho']]
        print("  " + " → ".join(caminho_nomes))
        
        if resultado_dfs['caminho']:
            print("\nDFS:")
            caminho_nomes = [f"{v} ({nomes[v]})" for v in resultado_dfs['caminho']]
            print("  " + " → ".join(caminho_nomes))
    
    pausar()


def executar_bellman_ford():
    """Executa o algoritmo Bellman-Ford."""
    limpar_tela()
    exibir_cabecalho()
    
    print("\n" + "=" * 70)
    print("ALGORITMO BELLMAN-FORD - MENOR CAMINHO")
    print("=" * 70)
    
    grafo, nomes, _ = selecionar_grafo()
    origem, destino = obter_vertices(grafo, nomes)
    
    print("\n" + "=" * 70)
    print("EXECUTANDO BELLMAN-FORD...")
    print("=" * 70)
    
    resultado = BellmanFord.menor_caminho(grafo, origem, destino)
    
    if resultado['caminho'] and nomes:
        print("\n" + "=" * 70)
        print("CAMINHO COM NOMES DOS LOCAIS:")
        print("=" * 70)
        caminho_nomes = [f"{v} ({nomes[v]})" for v in resultado['caminho']]
        print("  " + " → ".join(caminho_nomes))
        print(f"  Custo total: {resultado['custo']} km")
    
    pausar()


def executar_dijkstra():
    """Executa o algoritmo Dijkstra."""
    limpar_tela()
    exibir_cabecalho()
    
    print("\n" + "=" * 70)
    print("ALGORITMO DIJKSTRA - MENOR CAMINHO")
    print("=" * 70)
    
    grafo, nomes, _ = selecionar_grafo()
    origem, destino = obter_vertices(grafo, nomes)
    
    print("\n" + "=" * 70)
    print("EXECUTANDO DIJKSTRA...")
    print("=" * 70)
    
    resultado = Dijkstra.menor_caminho(grafo, origem, destino)
    
    if resultado['caminho'] and nomes:
        print("\n" + "=" * 70)
        print("CAMINHO COM NOMES DOS LOCAIS:")
        print("=" * 70)
        caminho_nomes = [f"{v} ({nomes[v]})" for v in resultado['caminho']]
        print("  " + " → ".join(caminho_nomes))
        print(f"  Custo total: {resultado['custo']} km")
    
    pausar()


def comparar_bellman_ford_dijkstra():
    """Compara Bellman-Ford e Dijkstra."""
    limpar_tela()
    exibir_cabecalho()
    
    print("\n" + "=" * 70)
    print("COMPARAÇÃO: BELLMAN-FORD vs DIJKSTRA")
    print("=" * 70)
    
    grafo, nomes, _ = selecionar_grafo()
    origem, destino = obter_vertices(grafo, nomes)
    
    if destino is None:
        print("\nPara comparação, é necessário especificar um destino.")
        pausar()
        return
    
    print("\n" + "=" * 70)
    print("EXECUTANDO BELLMAN-FORD...")
    print("=" * 70)
    resultado_bf = BellmanFord.menor_caminho(grafo, origem, destino)
    
    print("\n" + "=" * 70)
    print("EXECUTANDO DIJKSTRA...")
    print("=" * 70)
    resultado_dijk = Dijkstra.menor_caminho(grafo, origem, destino)
    
    print("\n" + "=" * 70)
    print("COMPARAÇÃO DOS RESULTADOS")
    print("=" * 70)
    
    print(f"\nBellman-Ford:")
    if resultado_bf['caminho']:
        print(f"  Caminho: {resultado_bf['caminho']}")
        print(f"  Custo: {resultado_bf['custo']}")
    else:
        print(f"  Caminho não encontrado")
    
    print(f"\nDijkstra:")
    if resultado_dijk['caminho']:
        print(f"  Caminho: {resultado_dijk['caminho']}")
        print(f"  Custo: {resultado_dijk['custo']}")
    else:
        print(f"  Caminho não encontrado")
    
    print("\n" + "-" * 70)
    print("OBSERVAÇÕES:")
    print("-" * 70)
    print("• Ambos encontram o caminho de menor custo (peso)")
    print("• Bellman-Ford: Funciona com pesos negativos, O(V*E)")
    print("• Dijkstra: Mais rápido, mas requer pesos não-negativos, O((V+E)logV)")
    
    if resultado_bf['custo'] == resultado_dijk['custo']:
        print("• ✓ Ambos encontraram caminhos de mesmo custo!")
    
    pausar()


def executar_kruskal():
    """Executa o algoritmo de Kruskal."""
    limpar_tela()
    exibir_cabecalho()
    
    print("\n" + "=" * 70)
    print("ALGORITMO DE KRUSKAL - ÁRVORE GERADORA MÍNIMA")
    print("=" * 70)
    
    print("\nEste algoritmo requer grafo não-direcionado.")
    print("Selecionando Mapa de Cidade...")
    
    grafo = GrafoExemplos.criar_mapa_cidade()
    nomes = GrafoExemplos.obter_nomes_mapa_cidade()
    
    input("\nPressione ENTER para iniciar...")
    
    print("\n" + "=" * 70)
    print("EXECUTANDO KRUSKAL...")
    print("=" * 70)
    
    resultado = Kruskal.mst(grafo)
    
    print("\n" + "=" * 70)
    print("INTERPRETAÇÃO DO RESULTADO:")
    print("=" * 70)
    print(f"\nA MST representa a rede de menor custo que conecta todos os locais.")
    print(f"Custo total: {resultado['custo_total']} km")
    print(f"\nAplicações práticas:")
    print(f"  • Construir rede de fibra ótica")
    print(f"  • Planejar sistema de transporte público")
    print(f"  • Instalar rede elétrica ou de água")
    print(f"  • Minimizar cabeamento em geral")
    
    pausar()


def executar_prim():
    """Executa o algoritmo de Prim."""
    limpar_tela()
    exibir_cabecalho()
    
    print("\n" + "=" * 70)
    print("ALGORITMO DE PRIM - ÁRVORE GERADORA MÍNIMA")
    print("=" * 70)
    
    print("\nEste algoritmo requer grafo não-direcionado.")
    print("Selecionando Mapa de Cidade...")
    
    grafo = GrafoExemplos.criar_mapa_cidade()
    nomes = GrafoExemplos.obter_nomes_mapa_cidade()
    
    vertices = grafo.obter_vertices()
    print(f"\nVértices disponíveis: {sorted(vertices)}")
    
    while True:
        try:
            origem = int(input("\nVértice inicial (ou Enter para usar o primeiro): ") or vertices[0])
            if origem not in vertices:
                print(f"Vértice {origem} não existe! Tente novamente.")
                continue
            break
        except ValueError:
            print("Valor inválido! Digite um número.")
    
    print("\n" + "=" * 70)
    print("EXECUTANDO PRIM...")
    print("=" * 70)
    
    resultado = Prim.mst(grafo, origem)
    
    print("\n" + "=" * 70)
    print("INTERPRETAÇÃO DO RESULTADO:")
    print("=" * 70)
    print(f"\nA MST representa a rede de menor custo que conecta todos os locais.")
    print(f"Custo total: {resultado['custo_total']} km")
    print(f"\nAplicações práticas:")
    print(f"  • Construir rede de fibra ótica")
    print(f"  • Planejar sistema de transporte público")
    print(f"  • Instalar rede elétrica ou de água")
    print(f"  • Minimizar cabeamento em geral")
    
    pausar()


def comparar_kruskal_prim():
    """Compara Kruskal e Prim."""
    limpar_tela()
    exibir_cabecalho()
    
    print("\n" + "=" * 70)
    print("COMPARAÇÃO: KRUSKAL vs PRIM")
    print("=" * 70)
    
    print("\nSelecionando Mapa de Cidade...")
    grafo = GrafoExemplos.criar_mapa_cidade()
    
    input("\nPressione ENTER para iniciar...")
    
    print("\n" + "=" * 70)
    print("EXECUTANDO KRUSKAL...")
    print("=" * 70)
    resultado_kruskal = Kruskal.mst(grafo)
    
    print("\n" + "=" * 70)
    print("EXECUTANDO PRIM...")
    print("=" * 70)
    resultado_prim = Prim.mst(grafo)
    
    print("\n" + "=" * 70)
    print("COMPARAÇÃO DOS RESULTADOS")
    print("=" * 70)
    
    print(f"\nKruskal:")
    print(f"  Custo total: {resultado_kruskal['custo_total']} km")
    print(f"  Número de arestas: {len(resultado_kruskal['arestas'])}")
    
    print(f"\nPrim:")
    print(f"  Custo total: {resultado_prim['custo_total']} km")
    print(f"  Número de arestas: {len(resultado_prim['arestas'])}")
    
    print("\n" + "-" * 70)
    print("OBSERVAÇÕES:")
    print("-" * 70)
    print("• Ambos encontram uma MST de custo mínimo")
    print("• Kruskal: Ordena arestas, usa Union-Find, O(E log E)")
    print("• Prim: Usa heap, expande a partir de um vértice, O((V+E)logV)")
    print("• As arestas podem ser diferentes, mas o custo é o mesmo!")
    
    if abs(resultado_kruskal['custo_total'] - resultado_prim['custo_total']) < 0.001:
        print("• ✓ Ambos encontraram MSTs de mesmo custo!")
    
    pausar()


def visualizar_grafos():
    """Visualiza informações sobre os grafos disponíveis."""
    limpar_tela()
    exibir_cabecalho()
    
    print("\n" + "=" * 70)
    print("GRAFOS DISPONÍVEIS")
    print("=" * 70)
    
    print("\n1. MAPA DE CIDADE (20 vértices)")
    print("   Tipo: Não-direcionado")
    print("   Descrição: Representa distâncias entre locais em uma cidade")
    
    grafo1 = GrafoExemplos.criar_mapa_cidade()
    nomes = GrafoExemplos.obter_nomes_mapa_cidade()
    
    print("\n   Locais:")
    for v in sorted(grafo1.obter_vertices()):
        print(f"     {v}: {nomes[v]}")
    
    print(f"\n   Total de arestas: {len(grafo1.obter_arestas())}")
    
    print("\n" + "-" * 70)
    
    print("\n2. REDE DE COMPUTADORES (16 vértices)")
    print("   Tipo: Direcionado")
    print("   Descrição: Representa latência entre servidores em uma rede")
    
    grafo2 = GrafoExemplos.criar_rede_computadores()
    vertices = grafo2.obter_vertices()
    
    print(f"\n   Vértices: {sorted(vertices)}")
    print(f"   Total de arestas: {len(grafo2.obter_arestas())}")
    
    print("\n   Hierarquia:")
    print("     0: Servidor Principal")
    print("     1-3: Servidores Regionais")
    print("     4-9: Servidores Locais")
    print("     10-15: Clientes")
    
    pausar()


def executar_todas_demonstracoes():
    """Executa todas as demonstrações sequencialmente."""
    limpar_tela()
    exibir_cabecalho()
    
    print("\n" + "=" * 70)
    print("EXECUTANDO TODAS AS DEMONSTRAÇÕES")
    print("=" * 70)
    print("\nEste modo executará todos os algoritmos com exemplos pré-configurados.")
    print("Isso pode levar alguns minutos.")
    
    input("\nPressione ENTER para iniciar...")
    
    # BFS e DFS
    from bfs_dfs import demonstrar_bfs_dfs
    demonstrar_bfs_dfs()
    pausar()
    
    # Bellman-Ford e Dijkstra
    from bellman_ford_dijkstra import demonstrar_bellman_ford_dijkstra
    demonstrar_bellman_ford_dijkstra()
    pausar()
    
    # MST (Kruskal e Prim)
    from mst_kruskal_prim import demonstrar_mst
    demonstrar_mst()
    pausar()
    
    limpar_tela()
    exibir_cabecalho()
    print("\n" + "=" * 70)
    print("TODAS AS DEMONSTRAÇÕES FORAM CONCLUÍDAS!")
    print("=" * 70)
    pausar()


def menu_busca():
    """Menu de algoritmos de busca."""
    while True:
        limpar_tela()
        exibir_cabecalho()
        exibir_menu_busca()
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            executar_bfs()
        elif opcao == "2":
            executar_dfs(recursivo=True)
        elif opcao == "3":
            executar_dfs(recursivo=False)
        elif opcao == "4":
            comparar_bfs_dfs()
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida! Tente novamente.")
            pausar()


def menu_menor_caminho():
    """Menu de algoritmos de menor caminho."""
    while True:
        limpar_tela()
        exibir_cabecalho()
        exibir_menu_menor_caminho()
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            executar_bellman_ford()
        elif opcao == "2":
            executar_dijkstra()
        elif opcao == "3":
            comparar_bellman_ford_dijkstra()
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida! Tente novamente.")
            pausar()


def menu_mst():
    """Menu de algoritmos de MST."""
    while True:
        limpar_tela()
        exibir_cabecalho()
        exibir_menu_mst()
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            executar_kruskal()
        elif opcao == "2":
            executar_prim()
        elif opcao == "3":
            comparar_kruskal_prim()
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida! Tente novamente.")
            pausar()


def main():
    """Função principal do programa."""
    while True:
        limpar_tela()
        exibir_cabecalho()
        exibir_menu_principal()
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            menu_busca()
        elif opcao == "2":
            menu_menor_caminho()
        elif opcao == "3":
            menu_mst()
        elif opcao == "4":
            visualizar_grafos()
        elif opcao == "5":
            executar_todas_demonstracoes()
        elif opcao == "0":
            limpar_tela()
            print("\n" + "=" * 70)
            print("Obrigado por usar o sistema!")
            print("=" * 70)
            print("\nAutores: [COLOQUE OS NOMES DA EQUIPE AQUI]")
            print("Disciplina: [NOME DA DISCIPLINA]")
            print("\n")
            sys.exit(0)
        else:
            print("\nOpção inválida! Tente novamente.")
            pausar()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nErro inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
