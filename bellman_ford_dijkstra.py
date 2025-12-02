"""
Algoritmos de Menor Caminho: Bellman-Ford e Dijkstra
=====================================================
Implementação dos algoritmos de Bellman-Ford e Dijkstra para encontrar
o menor caminho em grafos ponderados.

CONCEITOS:
----------
BELLMAN-FORD:
- Encontra o menor caminho de um vértice origem para todos os outros vértices.
- FUNCIONA com arestas de peso NEGATIVO.
- Detecta ciclos de peso negativo.
- Relaxa todas as arestas V-1 vezes (V = número de vértices).
- Complexidade: O(V * E), onde V = vértices e E = arestas.

DIJKSTRA:
- Encontra o menor caminho de um vértice origem para todos os outros vértices.
- NÃO funciona com arestas de peso negativo.
- Mais eficiente que Bellman-Ford quando não há pesos negativos.
- Usa uma fila de prioridade (heap) para selecionar o próximo vértice.
- Complexidade: O((V + E) * log V) com heap binário.

QUANDO USAR CADA UM:
-------------------
BELLMAN-FORD:
- Quando o grafo pode ter arestas de peso negativo
- Quando é necessário detectar ciclos negativos
- Grafos pequenos ou médios

DIJKSTRA:
- Quando todos os pesos são não-negativos (o caso mais comum)
- Quando é necessário alta performance
- Redes de computadores, GPS, roteamento

Autores: [COLOQUE OS NOMES DA EQUIPE AQUI]
Data: Dezembro 2025
"""

from typing import List, Dict, Optional, Tuple
import heapq
from grafo import Grafo


class BellmanFord:
    """
    Implementação do algoritmo de Bellman-Ford para encontrar o menor caminho.
    """
    
    @staticmethod
    def menor_caminho(grafo: Grafo, origem: int, destino: Optional[int] = None) -> Dict:
        """
        Encontra o menor caminho usando o algoritmo de Bellman-Ford.
        
        FUNCIONAMENTO:
        1. Inicializa distâncias: origem = 0, demais = infinito
        2. Relaxa todas as arestas V-1 vezes:
           - Para cada aresta (u, v) com peso w:
             Se dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                predecessor[v] = u
        3. Verifica ciclos negativos: tenta relaxar mais uma vez
           - Se conseguir relaxar alguma aresta, há ciclo negativo
        
        Args:
            grafo (Grafo): Grafo ponderado
            origem (int): Vértice de origem
            destino (Optional[int]): Vértice de destino (None para calcular para todos)
            
        Returns:
            Dict: Dicionário contendo:
                - 'distancia': distância mínima para cada vértice
                - 'predecessor': predecessor de cada vértice no caminho mínimo
                - 'caminho': caminho mínimo até o destino (se especificado)
                - 'tem_ciclo_negativo': True se há ciclo de peso negativo
                - 'custo': custo total do caminho (se destino especificado)
        """
        vertices = grafo.obter_vertices()
        
        # Inicialização
        distancia = {v: float('inf') for v in vertices}
        predecessor = {v: None for v in vertices}
        distancia[origem] = 0
        
        print(f"\n{'='*70}")
        print(f"EXECUTANDO BELLMAN-FORD - ALGORITMO DE MENOR CAMINHO")
        print(f"{'='*70}")
        print(f"Origem: {origem}")
        if destino is not None:
            print(f"Destino: {destino}")
        print(f"\nNúmero de vértices: {len(vertices)}")
        print(f"Número de iterações necessárias: {len(vertices) - 1}")
        
        print(f"\nInicialização:")
        print(f"  Distância[{origem}] = 0")
        print(f"  Distância[outros] = ∞")
        
        # Obtém todas as arestas
        arestas = grafo.obter_arestas()
        print(f"\nTotal de arestas a serem relaxadas: {len(arestas)}")
        
        # Relaxa todas as arestas V-1 vezes
        for iteracao in range(len(vertices) - 1):
            print(f"\n{'─'*70}")
            print(f"ITERAÇÃO {iteracao + 1}/{len(vertices) - 1}")
            print(f"{'─'*70}")
            
            atualizacoes = 0
            
            # Para cada aresta, tenta relaxar
            for u, v, peso in arestas:
                # Tenta relaxar a aresta u -> v
                if distancia[u] != float('inf') and distancia[u] + peso < distancia[v]:
                    distancia_antiga = distancia[v]
                    distancia[v] = distancia[u] + peso
                    predecessor[v] = u
                    atualizacoes += 1
                    
                    print(f"  Relaxando aresta {u} → {v} (peso: {peso})")
                    print(f"    Distância[{v}]: {distancia_antiga if distancia_antiga != float('inf') else '∞'} → {distancia[v]}")
            
            if atualizacoes == 0:
                print(f"  Nenhuma atualização nesta iteração. Algoritmo pode terminar mais cedo!")
                break
            else:
                print(f"  Total de atualizações: {atualizacoes}")
        
        # Verifica ciclos de peso negativo
        print(f"\n{'─'*70}")
        print(f"VERIFICAÇÃO DE CICLOS NEGATIVOS")
        print(f"{'─'*70}")
        
        tem_ciclo_negativo = False
        for u, v, peso in arestas:
            if distancia[u] != float('inf') and distancia[u] + peso < distancia[v]:
                tem_ciclo_negativo = True
                print(f"  ⚠ CICLO NEGATIVO DETECTADO!")
                print(f"  Aresta {u} → {v} ainda pode ser relaxada")
                break
        
        if not tem_ciclo_negativo:
            print(f"  ✓ Nenhum ciclo negativo detectado")
        
        # Mostra resultado final
        print(f"\n{'='*70}")
        print(f"DISTÂNCIAS FINAIS A PARTIR DA ORIGEM {origem}:")
        print(f"{'='*70}")
        
        for v in sorted(vertices):
            if distancia[v] == float('inf'):
                print(f"  Vértice {v}: ∞ (não alcançável)")
            else:
                print(f"  Vértice {v}: {distancia[v]}")
        
        # Reconstrói o caminho se um destino foi especificado
        caminho = None
        custo = None
        
        if destino is not None:
            if distancia[destino] == float('inf'):
                print(f"\n✗ Não há caminho de {origem} para {destino}")
            else:
                caminho = BellmanFord._reconstruir_caminho(predecessor, origem, destino)
                custo = distancia[destino]
                
                print(f"\n{'='*70}")
                print(f"MENOR CAMINHO DE {origem} PARA {destino}:")
                print(f"{'='*70}")
                print(f"  Caminho: {' → '.join(map(str, caminho))}")
                print(f"  Custo total: {custo}")
                
                # Mostra detalhes do caminho
                print(f"\n  Detalhes do caminho:")
                for i in range(len(caminho) - 1):
                    u, v = caminho[i], caminho[i + 1]
                    # Encontra o peso da aresta
                    peso_aresta = None
                    for vizinho, peso in grafo.obter_vizinhos(u):
                        if vizinho == v:
                            peso_aresta = peso
                            break
                    print(f"    {u} → {v}: peso = {peso_aresta}")
        
        return {
            'distancia': distancia,
            'predecessor': predecessor,
            'caminho': caminho,
            'tem_ciclo_negativo': tem_ciclo_negativo,
            'custo': custo
        }
    
    @staticmethod
    def _reconstruir_caminho(predecessor: Dict, origem: int, destino: int) -> List[int]:
        """Reconstrói o caminho do destino até a origem."""
        caminho = []
        atual = destino
        
        while atual is not None:
            caminho.append(atual)
            atual = predecessor[atual]
        
        caminho.reverse()
        return caminho


class Dijkstra:
    """
    Implementação do algoritmo de Dijkstra para encontrar o menor caminho.
    """
    
    @staticmethod
    def menor_caminho(grafo: Grafo, origem: int, destino: Optional[int] = None) -> Dict:
        """
        Encontra o menor caminho usando o algoritmo de Dijkstra.
        
        FUNCIONAMENTO:
        1. Inicializa distâncias: origem = 0, demais = infinito
        2. Adiciona origem na fila de prioridade (heap)
        3. Enquanto a fila não está vazia:
           a. Remove vértice com menor distância (u)
           b. Para cada vizinho v de u:
              Se dist[u] + peso(u,v) < dist[v]:
                 dist[v] = dist[u] + peso(u,v)
                 predecessor[v] = u
                 Adiciona v na fila de prioridade
        
        Args:
            grafo (Grafo): Grafo ponderado (pesos não-negativos)
            origem (int): Vértice de origem
            destino (Optional[int]): Vértice de destino (None para calcular para todos)
            
        Returns:
            Dict: Dicionário contendo:
                - 'distancia': distância mínima para cada vértice
                - 'predecessor': predecessor de cada vértice no caminho mínimo
                - 'caminho': caminho mínimo até o destino (se especificado)
                - 'custo': custo total do caminho (se destino especificado)
                - 'vertices_visitados': ordem de visita dos vértices
        """
        vertices = grafo.obter_vertices()
        
        # Inicialização
        distancia = {v: float('inf') for v in vertices}
        predecessor = {v: None for v in vertices}
        distancia[origem] = 0
        visitados = set()
        vertices_visitados = []
        
        # Fila de prioridade (heap): (distância, vértice)
        heap = [(0, origem)]
        
        print(f"\n{'='*70}")
        print(f"EXECUTANDO DIJKSTRA - ALGORITMO DE MENOR CAMINHO")
        print(f"{'='*70}")
        print(f"Origem: {origem}")
        if destino is not None:
            print(f"Destino: {destino}")
        print(f"\nNúmero de vértices: {len(vertices)}")
        
        print(f"\nInicialização:")
        print(f"  Distância[{origem}] = 0")
        print(f"  Distância[outros] = ∞")
        print(f"  Heap inicial: [(0, {origem})]")
        
        passo = 1
        
        # Loop principal
        while heap:
            # Remove o vértice com menor distância
            dist_u, u = heapq.heappop(heap)
            
            # Se já foi visitado, pula (pode haver duplicatas no heap)
            if u in visitados:
                continue
            
            visitados.add(u)
            vertices_visitados.append(u)
            
            print(f"\n{'─'*70}")
            print(f"PASSO {passo}")
            print(f"{'─'*70}")
            print(f"  Processando vértice: {u}")
            print(f"  Distância atual: {dist_u}")
            print(f"  Vértices restantes no heap: {len(heap)}")
            
            # Se chegou no destino, pode parar (otimização)
            if destino is not None and u == destino:
                print(f"\n  ✓ Destino {destino} alcançado! Parando busca.")
                break
            
            # Relaxa arestas dos vizinhos
            atualizacoes = 0
            for v, peso in grafo.obter_vizinhos(u):
                if v not in visitados:
                    nova_distancia = distancia[u] + peso
                    
                    if nova_distancia < distancia[v]:
                        distancia_antiga = distancia[v]
                        distancia[v] = nova_distancia
                        predecessor[v] = u
                        heapq.heappush(heap, (nova_distancia, v))
                        atualizacoes += 1
                        
                        print(f"  Relaxando aresta {u} → {v} (peso: {peso})")
                        print(f"    Distância[{v}]: {distancia_antiga if distancia_antiga != float('inf') else '∞'} → {nova_distancia}")
            
            if atualizacoes == 0:
                print(f"  Nenhum vizinho foi atualizado")
            else:
                print(f"  Total de atualizações: {atualizacoes}")
            
            passo += 1
        
        # Mostra resultado final
        print(f"\n{'='*70}")
        print(f"DISTÂNCIAS FINAIS A PARTIR DA ORIGEM {origem}:")
        print(f"{'='*70}")
        
        for v in sorted(vertices):
            if distancia[v] == float('inf'):
                print(f"  Vértice {v}: ∞ (não alcançável)")
            else:
                print(f"  Vértice {v}: {distancia[v]}")
        
        # Reconstrói o caminho se um destino foi especificado
        caminho = None
        custo = None
        
        if destino is not None:
            if distancia[destino] == float('inf'):
                print(f"\n✗ Não há caminho de {origem} para {destino}")
            else:
                caminho = Dijkstra._reconstruir_caminho(predecessor, origem, destino)
                custo = distancia[destino]
                
                print(f"\n{'='*70}")
                print(f"MENOR CAMINHO DE {origem} PARA {destino}:")
                print(f"{'='*70}")
                print(f"  Caminho: {' → '.join(map(str, caminho))}")
                print(f"  Custo total: {custo}")
                
                # Mostra detalhes do caminho
                print(f"\n  Detalhes do caminho:")
                for i in range(len(caminho) - 1):
                    u, v = caminho[i], caminho[i + 1]
                    # Encontra o peso da aresta
                    peso_aresta = None
                    for vizinho, peso in grafo.obter_vizinhos(u):
                        if vizinho == v:
                            peso_aresta = peso
                            break
                    print(f"    {u} → {v}: peso = {peso_aresta}")
        
        return {
            'distancia': distancia,
            'predecessor': predecessor,
            'caminho': caminho,
            'custo': custo,
            'vertices_visitados': vertices_visitados
        }
    
    @staticmethod
    def _reconstruir_caminho(predecessor: Dict, origem: int, destino: int) -> List[int]:
        """Reconstrói o caminho do destino até a origem."""
        caminho = []
        atual = destino
        
        while atual is not None:
            caminho.append(atual)
            atual = predecessor[atual]
        
        caminho.reverse()
        return caminho


# Função auxiliar para demonstração
def demonstrar_bellman_ford_dijkstra():
    """
    Função de demonstração dos algoritmos Bellman-Ford e Dijkstra.
    """
    from grafo import GrafoExemplos
    
    print("\n" + "="*70)
    print("DEMONSTRAÇÃO: ALGORITMOS BELLMAN-FORD E DIJKSTRA")
    print("="*70)
    
    # Cria um grafo de exemplo
    print("\nCriando grafo de exemplo (Mapa de Cidade com 20 vértices)...")
    grafo = GrafoExemplos.criar_mapa_cidade()
    nomes = GrafoExemplos.obter_nomes_mapa_cidade()
    
    print("\nGrafo criado com sucesso!")
    print(f"Todos os pesos são positivos (distâncias em km)")
    
    # Demonstração Bellman-Ford
    print("\n" + "="*70)
    print("EXEMPLO 1: BELLMAN-FORD")
    print("Encontrar menor caminho do Centro (0) ao Aeroporto (5)")
    print("="*70)
    resultado_bf = BellmanFord.menor_caminho(grafo, origem=0, destino=5)
    
    if resultado_bf['caminho']:
        print("\nCaminho com nomes dos locais:")
        caminho_nomes = [nomes[v] for v in resultado_bf['caminho']]
        print(f"  {' → '.join(caminho_nomes)}")
    
    # Demonstração Dijkstra
    print("\n" + "="*70)
    print("EXEMPLO 2: DIJKSTRA")
    print("Encontrar menor caminho do Centro (0) ao Aeroporto (5)")
    print("="*70)
    resultado_dijk = Dijkstra.menor_caminho(grafo, origem=0, destino=5)
    
    if resultado_dijk['caminho']:
        print("\nCaminho com nomes dos locais:")
        caminho_nomes = [nomes[v] for v in resultado_dijk['caminho']]
        print(f"  {' → '.join(caminho_nomes)}")
    
    # Comparação
    print("\n" + "="*70)
    print("COMPARAÇÃO DOS RESULTADOS")
    print("="*70)
    print(f"Bellman-Ford:")
    print(f"  Custo: {resultado_bf['custo']} km")
    print(f"  Caminho: {resultado_bf['caminho']}")
    print(f"\nDijkstra:")
    print(f"  Custo: {resultado_dijk['custo']} km")
    print(f"  Caminho: {resultado_dijk['caminho']}")
    
    if resultado_bf['custo'] == resultado_dijk['custo']:
        print(f"\n✓ Ambos encontraram o mesmo caminho ótimo!")
    
    print(f"\nObservações:")
    print(f"- Bellman-Ford: Funciona com pesos negativos, complexidade O(V*E)")
    print(f"- Dijkstra: Mais eficiente, mas requer pesos não-negativos, O((V+E)logV)")


if __name__ == "__main__":
    demonstrar_bellman_ford_dijkstra()
