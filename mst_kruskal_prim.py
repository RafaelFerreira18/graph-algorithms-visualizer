"""
Algoritmos de Árvore Geradora Mínima (MST - Minimum Spanning Tree)
====================================================================
Implementação dos algoritmos de Kruskal e Prim para encontrar a
Árvore Geradora Mínima em grafos não-direcionados e ponderados.

CONCEITOS:
----------
ÁRVORE GERADORA MÍNIMA (MST):
- Uma árvore que conecta TODOS os vértices do grafo
- Usa o MENOR custo total possível (soma dos pesos das arestas)
- Possui exatamente V-1 arestas (onde V = número de vértices)
- Não contém ciclos

ALGORITMO DE KRUSKAL:
- Estratégia: Ordenar arestas por peso e adicionar a menor que não forma ciclo
- Usa estrutura Union-Find (Disjoint Set) para detectar ciclos
- Complexidade: O(E log E), onde E = número de arestas
- Funciona bem para grafos esparsos (poucas arestas)

ALGORITMO DE PRIM:
- Estratégia: Começar de um vértice e sempre adicionar a aresta de menor peso
  que conecta um vértice da árvore a um vértice fora dela
- Usa fila de prioridade (heap) para selecionar próxima aresta
- Complexidade: O((V + E) log V) com heap binário
- Funciona bem para grafos densos (muitas arestas)

APLICAÇÕES PRÁTICAS:
-------------------
- Projeto de redes (telefonia, elétrica, água)
- Redes de computadores (minimizar cabeamento)
- Clustering e análise de dados
- Construção de estradas conectando cidades
- Design de circuitos integrados

Autores: [COLOQUE OS NOMES DA EQUIPE AQUI]
Data: Dezembro 2025
"""

from typing import List, Dict, Tuple, Set
import heapq
from grafo import Grafo


class UnionFind:
    """
    Estrutura de dados Union-Find (Disjoint Set Union - DSU).
    Usada para detectar ciclos no algoritmo de Kruskal.
    """
    
    def __init__(self, vertices: List[int]):
        """
        Inicializa a estrutura Union-Find.
        
        Args:
            vertices (List[int]): Lista de vértices
        """
        # Cada vértice começa em seu próprio conjunto
        self.pai = {v: v for v in vertices}
        # Rank usado para otimização (union by rank)
        self.rank = {v: 0 for v in vertices}
    
    def find(self, v: int) -> int:
        """
        Encontra o representante (raiz) do conjunto que contém v.
        Usa compressão de caminho para otimização.
        
        Args:
            v (int): Vértice
            
        Returns:
            int: Representante do conjunto
        """
        if self.pai[v] != v:
            # Compressão de caminho: faz v apontar diretamente para a raiz
            self.pai[v] = self.find(self.pai[v])
        return self.pai[v]
    
    def union(self, u: int, v: int) -> bool:
        """
        Une os conjuntos que contêm u e v.
        
        Args:
            u (int): Primeiro vértice
            v (int): Segundo vértice
            
        Returns:
            bool: True se os conjuntos foram unidos, False se já estavam no mesmo conjunto
        """
        raiz_u = self.find(u)
        raiz_v = self.find(v)
        
        # Se já estão no mesmo conjunto, não une
        if raiz_u == raiz_v:
            return False
        
        # Union by rank: anexa a árvore menor à maior
        if self.rank[raiz_u] < self.rank[raiz_v]:
            self.pai[raiz_u] = raiz_v
        elif self.rank[raiz_u] > self.rank[raiz_v]:
            self.pai[raiz_v] = raiz_u
        else:
            self.pai[raiz_v] = raiz_u
            self.rank[raiz_u] += 1
        
        return True


class Kruskal:
    """
    Implementação do algoritmo de Kruskal para Árvore Geradora Mínima.
    """
    
    @staticmethod
    def mst(grafo: Grafo) -> Dict:
        """
        Encontra a Árvore Geradora Mínima usando o algoritmo de Kruskal.
        
        FUNCIONAMENTO:
        1. Ordena todas as arestas por peso (crescente)
        2. Inicializa Union-Find com todos os vértices
        3. Para cada aresta (u, v) em ordem:
           a. Se u e v estão em conjuntos diferentes:
              - Adiciona aresta à MST
              - Une os conjuntos de u e v
           b. Senão: ignora (adicionaria um ciclo)
        4. Para quando tiver V-1 arestas
        
        Args:
            grafo (Grafo): Grafo não-direcionado e ponderado
            
        Returns:
            Dict: Dicionário contendo:
                - 'arestas': lista de arestas na MST
                - 'custo_total': custo total da MST
                - 'passos': lista de passos da execução
        """
        if grafo.direcionado:
            raise ValueError("Algoritmo de Kruskal requer grafo não-direcionado")
        
        vertices = grafo.obter_vertices()
        arestas = grafo.obter_arestas()
        
        print(f"\n{'='*70}")
        print(f"EXECUTANDO KRUSKAL - ÁRVORE GERADORA MÍNIMA (MST)")
        print(f"{'='*70}")
        print(f"Número de vértices: {len(vertices)}")
        print(f"Número de arestas: {len(arestas)}")
        print(f"Arestas necessárias na MST: {len(vertices) - 1}")
        
        # Passo 1: Ordena arestas por peso
        print(f"\n{'─'*70}")
        print(f"PASSO 1: ORDENAR ARESTAS POR PESO")
        print(f"{'─'*70}")
        
        arestas_ordenadas = sorted(arestas, key=lambda x: x[2])
        
        print(f"Arestas ordenadas:")
        for u, v, peso in arestas_ordenadas:
            print(f"  {u} -- {v}: peso = {peso}")
        
        # Passo 2: Inicializa Union-Find
        print(f"\n{'─'*70}")
        print(f"PASSO 2: INICIALIZAR UNION-FIND")
        print(f"{'─'*70}")
        print(f"Cada vértice começa em seu próprio conjunto")
        
        uf = UnionFind(vertices)
        
        # Passo 3: Processa arestas
        print(f"\n{'─'*70}")
        print(f"PASSO 3: PROCESSAR ARESTAS E CONSTRUIR MST")
        print(f"{'─'*70}")
        
        mst_arestas = []
        custo_total = 0
        passos = []
        
        for i, (u, v, peso) in enumerate(arestas_ordenadas, 1):
            print(f"\nIteração {i}:")
            print(f"  Considerando aresta: {u} -- {v} (peso: {peso})")
            
            raiz_u = uf.find(u)
            raiz_v = uf.find(v)
            
            print(f"  Conjunto de {u}: representante = {raiz_u}")
            print(f"  Conjunto de {v}: representante = {raiz_v}")
            
            if raiz_u != raiz_v:
                # Adiciona aresta à MST
                mst_arestas.append((u, v, peso))
                custo_total += peso
                uf.union(u, v)
                
                print(f"  ✓ ACEITA - Conjuntos diferentes, aresta adicionada à MST")
                print(f"  Custo acumulado: {custo_total}")
                
                passos.append({
                    'aresta': (u, v, peso),
                    'aceita': True,
                    'motivo': 'Não forma ciclo'
                })
                
                # Verifica se já tem V-1 arestas
                if len(mst_arestas) == len(vertices) - 1:
                    print(f"\n  ✓ MST COMPLETA! Todas as {len(vertices) - 1} arestas necessárias foram adicionadas.")
                    break
            else:
                print(f"  ✗ REJEITADA - Formaria ciclo (vértices já estão conectados)")
                
                passos.append({
                    'aresta': (u, v, peso),
                    'aceita': False,
                    'motivo': 'Formaria ciclo'
                })
        
        # Resultado final
        print(f"\n{'='*70}")
        print(f"ÁRVORE GERADORA MÍNIMA (MST) - RESULTADO FINAL")
        print(f"{'='*70}")
        print(f"\nArestas na MST:")
        for u, v, peso in mst_arestas:
            print(f"  {u} -- {v}: peso = {peso}")
        
        print(f"\nCusto total da MST: {custo_total}")
        print(f"Número de arestas: {len(mst_arestas)}")
        
        # Verifica se a MST está completa
        if len(mst_arestas) == len(vertices) - 1:
            print(f"✓ MST está completa (conecta todos os vértices)")
        else:
            print(f"⚠ ATENÇÃO: Grafo não é conectado! MST incompleta.")
        
        return {
            'arestas': mst_arestas,
            'custo_total': custo_total,
            'passos': passos
        }


class Prim:
    """
    Implementação do algoritmo de Prim para Árvore Geradora Mínima.
    """
    
    @staticmethod
    def mst(grafo: Grafo, origem: int = None) -> Dict:
        """
        Encontra a Árvore Geradora Mínima usando o algoritmo de Prim.
        
        FUNCIONAMENTO:
        1. Começa com um vértice inicial (origem)
        2. Mantém conjunto de vértices já incluídos na MST
        3. Usa heap para encontrar a aresta de menor peso que conecta
           um vértice da MST a um vértice fora dela
        4. Adiciona aresta e vértice à MST
        5. Repete até todos os vértices estarem na MST
        
        Args:
            grafo (Grafo): Grafo não-direcionado e ponderado
            origem (int): Vértice inicial (se None, usa o primeiro vértice)
            
        Returns:
            Dict: Dicionário contendo:
                - 'arestas': lista de arestas na MST
                - 'custo_total': custo total da MST
                - 'vertices_visitados': ordem de inclusão dos vértices
        """
        if grafo.direcionado:
            raise ValueError("Algoritmo de Prim requer grafo não-direcionado")
        
        vertices = grafo.obter_vertices()
        
        if not vertices:
            return {'arestas': [], 'custo_total': 0, 'vertices_visitados': []}
        
        # Se origem não foi especificada, usa o primeiro vértice
        if origem is None:
            origem = vertices[0]
        
        print(f"\n{'='*70}")
        print(f"EXECUTANDO PRIM - ÁRVORE GERADORA MÍNIMA (MST)")
        print(f"{'='*70}")
        print(f"Número de vértices: {len(vertices)}")
        print(f"Vértice inicial: {origem}")
        print(f"Arestas necessárias na MST: {len(vertices) - 1}")
        
        # Inicialização
        mst_arestas = []
        custo_total = 0
        na_mst = set([origem])  # Vértices já incluídos na MST
        vertices_visitados = [origem]
        
        # Heap: (peso, vértice_origem, vértice_destino)
        # Adiciona todas as arestas do vértice inicial
        heap = []
        for vizinho, peso in grafo.obter_vizinhos(origem):
            heapq.heappush(heap, (peso, origem, vizinho))
        
        print(f"\n{'─'*70}")
        print(f"INICIALIZAÇÃO")
        print(f"{'─'*70}")
        print(f"Vértice inicial {origem} adicionado à MST")
        print(f"Arestas candidatas no heap: {len(heap)}")
        
        passo = 1
        
        # Loop principal
        while heap and len(mst_arestas) < len(vertices) - 1:
            print(f"\n{'─'*70}")
            print(f"PASSO {passo}")
            print(f"{'─'*70}")
            
            # Encontra a menor aresta que conecta MST a um vértice fora dela
            while heap:
                peso, u, v = heapq.heappop(heap)
                
                # Se v já está na MST, ignora esta aresta
                if v in na_mst:
                    print(f"  Ignorando aresta {u} -- {v} (peso: {peso}) - vértice {v} já está na MST")
                    continue
                
                # Aresta válida encontrada!
                print(f"  Menor aresta válida: {u} -- {v} (peso: {peso})")
                print(f"  Conecta vértice {u} (na MST) ao vértice {v} (fora da MST)")
                
                # Adiciona aresta à MST
                mst_arestas.append((u, v, peso))
                custo_total += peso
                na_mst.add(v)
                vertices_visitados.append(v)
                
                print(f"  ✓ Aresta adicionada à MST")
                print(f"  Custo acumulado: {custo_total}")
                print(f"  Vértices na MST: {sorted(na_mst)}")
                
                # Adiciona arestas do novo vértice ao heap
                novas_arestas = 0
                for vizinho, peso_viz in grafo.obter_vizinhos(v):
                    if vizinho not in na_mst:
                        heapq.heappush(heap, (peso_viz, v, vizinho))
                        novas_arestas += 1
                
                if novas_arestas > 0:
                    print(f"  Novas arestas candidatas adicionadas: {novas_arestas}")
                
                break
            
            passo += 1
        
        # Resultado final
        print(f"\n{'='*70}")
        print(f"ÁRVORE GERADORA MÍNIMA (MST) - RESULTADO FINAL")
        print(f"{'='*70}")
        print(f"\nArestas na MST:")
        for u, v, peso in mst_arestas:
            print(f"  {u} -- {v}: peso = {peso}")
        
        print(f"\nCusto total da MST: {custo_total}")
        print(f"Número de arestas: {len(mst_arestas)}")
        print(f"Ordem de inclusão dos vértices: {vertices_visitados}")
        
        # Verifica se a MST está completa
        if len(mst_arestas) == len(vertices) - 1:
            print(f"✓ MST está completa (conecta todos os vértices)")
        else:
            print(f"⚠ ATENÇÃO: Grafo não é conectado! MST incompleta.")
        
        return {
            'arestas': mst_arestas,
            'custo_total': custo_total,
            'vertices_visitados': vertices_visitados
        }


# Função auxiliar para demonstração
def demonstrar_mst():
    """
    Função de demonstração dos algoritmos de MST (Kruskal e Prim).
    """
    from grafo import GrafoExemplos
    
    print("\n" + "="*70)
    print("DEMONSTRAÇÃO: ALGORITMOS DE ÁRVORE GERADORA MÍNIMA (MST)")
    print("="*70)
    
    # Cria um grafo de exemplo
    print("\nCriando grafo de exemplo (Mapa de Cidade com 20 vértices)...")
    grafo = GrafoExemplos.criar_mapa_cidade()
    nomes = GrafoExemplos.obter_nomes_mapa_cidade()
    
    print("\nGrafo criado com sucesso!")
    print(f"Objetivo: Encontrar a MST (rede de menor custo conectando todos os locais)")
    
    # Demonstração Kruskal
    print("\n" + "="*70)
    print("EXEMPLO 1: ALGORITMO DE KRUSKAL")
    print("="*70)
    resultado_kruskal = Kruskal.mst(grafo)
    
    # Demonstração Prim
    print("\n" + "="*70)
    print("EXEMPLO 2: ALGORITMO DE PRIM")
    print("="*70)
    resultado_prim = Prim.mst(grafo, origem=0)
    
    # Comparação
    print("\n" + "="*70)
    print("COMPARAÇÃO DOS RESULTADOS")
    print("="*70)
    print(f"\nKruskal:")
    print(f"  Custo total: {resultado_kruskal['custo_total']} km")
    print(f"  Número de arestas: {len(resultado_kruskal['arestas'])}")
    
    print(f"\nPrim:")
    print(f"  Custo total: {resultado_prim['custo_total']} km")
    print(f"  Número de arestas: {len(resultado_prim['arestas'])}")
    
    if abs(resultado_kruskal['custo_total'] - resultado_prim['custo_total']) < 0.001:
        print(f"\n✓ Ambos os algoritmos encontraram MSTs de mesmo custo!")
        print(f"  (As arestas podem ser diferentes, mas o custo é o mesmo)")
    else:
        print(f"\n⚠ ATENÇÃO: Custos diferentes detectados!")
    
    print(f"\n{'='*70}")
    print(f"INTERPRETAÇÃO DO RESULTADO:")
    print(f"{'='*70}")
    print(f"A MST representa a rede de menor custo que conecta todos os {len(nomes)} locais.")
    print(f"Custo total: {resultado_kruskal['custo_total']} km")
    print(f"\nEsta seria a solução ótima para:")
    print(f"  - Construir rede de fibra ótica entre os locais")
    print(f"  - Planejar sistema de transporte público")
    print(f"  - Instalar rede elétrica ou de água")
    print(f"  - Minimizar qualquer tipo de conexão entre os pontos")


if __name__ == "__main__":
    demonstrar_mst()
