"""
Algoritmos de Busca em Grafos: BFS e DFS
=========================================
Implementação dos algoritmos de Busca em Largura (BFS) e Busca em Profundidade (DFS).

CONCEITOS:
----------
BFS (Breadth-First Search - Busca em Largura):
- Explora o grafo nível por nível, visitando todos os vizinhos de um vértice
  antes de avançar para os vizinhos dos vizinhos.
- Utiliza uma FILA (queue) para controlar a ordem de visita.
- Garante encontrar o caminho com MENOR NÚMERO DE ARESTAS.
- Complexidade: O(V + E), onde V = vértices e E = arestas.

DFS (Depth-First Search - Busca em Profundidade):
- Explora o grafo seguindo um caminho o mais profundo possível antes de retroceder.
- Utiliza uma PILHA (stack) ou recursão para controlar a ordem de visita.
- Útil para detectar ciclos, ordenação topológica, componentes conectados.
- Complexidade: O(V + E), onde V = vértices e E = arestas.

APLICAÇÕES PRÁTICAS:
-------------------
BFS: Encontrar menor caminho em mapas, redes sociais (grau de separação),
     broadcasting em redes, Web crawlers.
DFS: Resolver labirintos, detectar ciclos, verificar conectividade,
     análise de dependências.

Autores: [COLOQUE OS NOMES DA EQUIPE AQUI]
Data: Dezembro 2025
"""

from collections import deque
from typing import List, Dict, Set, Optional, Tuple
from grafo import Grafo


class BFS:
    """
    Implementação do algoritmo de Busca em Largura (BFS).
    """
    
    @staticmethod
    def buscar(grafo: Grafo, origem: int, destino: Optional[int] = None) -> Dict:
        """
        Executa a busca em largura a partir de um vértice de origem.
        
        FUNCIONAMENTO:
        1. Marca o vértice origem como visitado e adiciona na fila
        2. Enquanto a fila não estiver vazia:
           a. Remove o primeiro vértice da fila
           b. Para cada vizinho não visitado:
              - Marca como visitado
              - Armazena o predecessor (para reconstruir caminho)
              - Adiciona na fila
        3. Se encontrar o destino, para a busca
        
        Args:
            grafo (Grafo): Grafo a ser explorado
            origem (int): Vértice de origem
            destino (Optional[int]): Vértice de destino (None para explorar todo o grafo)
            
        Returns:
            Dict: Dicionário contendo:
                - 'visitados': ordem de visita dos vértices
                - 'predecessor': mapa de predecessores
                - 'distancia': distância (em número de arestas) de cada vértice
                - 'caminho': caminho até o destino (se especificado)
                - 'encontrado': True se destino foi encontrado
        """
        visitados = []  # Ordem de visita dos vértices
        predecessor = {origem: None}  # Mapa de predecessores
        distancia = {origem: 0}  # Distância de cada vértice à origem
        fila = deque([origem])  # Fila para BFS
        
        print(f"\n{'='*60}")
        print(f"EXECUTANDO BFS - BUSCA EM LARGURA")
        print(f"{'='*60}")
        print(f"Origem: {origem}")
        if destino is not None:
            print(f"Destino: {destino}")
        print(f"\nIniciando busca...")
        
        passo = 1
        
        # Loop principal do BFS
        while fila:
            # Remove o primeiro vértice da fila
            vertice_atual = fila.popleft()
            visitados.append(vertice_atual)
            
            print(f"\nPasso {passo}:")
            print(f"  Visitando vértice: {vertice_atual}")
            print(f"  Distância da origem: {distancia[vertice_atual]}")
            print(f"  Fila atual: {list(fila)}")
            
            # Se encontrou o destino, pode parar
            if destino is not None and vertice_atual == destino:
                print(f"\n✓ Destino {destino} encontrado!")
                break
            
            # Explora todos os vizinhos
            vizinhos_nao_visitados = []
            for vizinho, peso in grafo.obter_vizinhos(vertice_atual):
                if vizinho not in predecessor:
                    # Marca como visitado
                    predecessor[vizinho] = vertice_atual
                    distancia[vizinho] = distancia[vertice_atual] + 1
                    fila.append(vizinho)
                    vizinhos_nao_visitados.append(vizinho)
            
            if vizinhos_nao_visitados:
                print(f"  Novos vizinhos adicionados à fila: {vizinhos_nao_visitados}")
            else:
                print(f"  Nenhum vizinho novo encontrado")
            
            passo += 1
        
        # Reconstrói o caminho se um destino foi especificado
        caminho = None
        encontrado = False
        if destino is not None and destino in predecessor:
            caminho = BFS._reconstruir_caminho(predecessor, origem, destino)
            encontrado = True
            print(f"\n{'='*60}")
            print(f"CAMINHO ENCONTRADO:")
            print(f"  {' -> '.join(map(str, caminho))}")
            print(f"  Número de arestas: {len(caminho) - 1}")
            print(f"{'='*60}")
        elif destino is not None:
            print(f"\n✗ Destino {destino} não foi encontrado (não há caminho)")
        
        print(f"\nVértices visitados na ordem: {visitados}")
        print(f"Total de vértices explorados: {len(visitados)}")
        
        return {
            'visitados': visitados,
            'predecessor': predecessor,
            'distancia': distancia,
            'caminho': caminho,
            'encontrado': encontrado
        }
    
    @staticmethod
    def _reconstruir_caminho(predecessor: Dict, origem: int, destino: int) -> List[int]:
        """
        Reconstrói o caminho do destino até a origem usando o mapa de predecessores.
        
        Args:
            predecessor (Dict): Mapa de predecessores
            origem (int): Vértice de origem
            destino (int): Vértice de destino
            
        Returns:
            List[int]: Caminho da origem ao destino
        """
        caminho = []
        atual = destino
        
        # Reconstrói o caminho de trás para frente
        while atual is not None:
            caminho.append(atual)
            atual = predecessor[atual]
        
        # Inverte o caminho para ficar da origem ao destino
        caminho.reverse()
        return caminho


class DFS:
    """
    Implementação do algoritmo de Busca em Profundidade (DFS).
    """
    
    @staticmethod
    def buscar(grafo: Grafo, origem: int, destino: Optional[int] = None, 
               usar_recursao: bool = True) -> Dict:
        """
        Executa a busca em profundidade a partir de um vértice de origem.
        
        FUNCIONAMENTO:
        1. Marca o vértice origem como visitado
        2. Para cada vizinho não visitado:
           a. Visita recursivamente o vizinho (versão recursiva)
           OU
           b. Adiciona o vizinho na pilha (versão iterativa)
        3. Se encontrar o destino, para a busca
        
        Args:
            grafo (Grafo): Grafo a ser explorado
            origem (int): Vértice de origem
            destino (Optional[int]): Vértice de destino (None para explorar todo o grafo)
            usar_recursao (bool): True para versão recursiva, False para iterativa
            
        Returns:
            Dict: Dicionário contendo:
                - 'visitados': ordem de visita dos vértices
                - 'predecessor': mapa de predecessores
                - 'caminho': caminho até o destino (se especificado)
                - 'encontrado': True se destino foi encontrado
        """
        if usar_recursao:
            return DFS._buscar_recursivo(grafo, origem, destino)
        else:
            return DFS._buscar_iterativo(grafo, origem, destino)
    
    @staticmethod
    def _buscar_recursivo(grafo: Grafo, origem: int, destino: Optional[int] = None) -> Dict:
        """
        Implementação recursiva do DFS.
        """
        visitados = []
        predecessor = {origem: None}
        encontrado = [False]  # Usar lista para permitir modificação na recursão
        
        print(f"\n{'='*60}")
        print(f"EXECUTANDO DFS - BUSCA EM PROFUNDIDADE (RECURSIVA)")
        print(f"{'='*60}")
        print(f"Origem: {origem}")
        if destino is not None:
            print(f"Destino: {destino}")
        print(f"\nIniciando busca...")
        
        def dfs_recursivo_helper(vertice: int, profundidade: int = 0):
            """Função auxiliar recursiva."""
            # Se já encontrou o destino, não precisa continuar
            if encontrado[0]:
                return
            
            visitados.append(vertice)
            print(f"\n{'  ' * profundidade}Visitando vértice: {vertice} (profundidade: {profundidade})")
            
            # Verifica se encontrou o destino
            if destino is not None and vertice == destino:
                print(f"\n{'  ' * profundidade}✓ Destino {destino} encontrado!")
                encontrado[0] = True
                return
            
            # Explora vizinhos não visitados
            vizinhos = grafo.obter_vizinhos(vertice)
            vizinhos_nao_visitados = [v for v, _ in vizinhos if v not in predecessor]
            
            if vizinhos_nao_visitados:
                print(f"{'  ' * profundidade}Explorando vizinhos: {vizinhos_nao_visitados}")
            
            for vizinho, peso in vizinhos:
                if vizinho not in predecessor and not encontrado[0]:
                    predecessor[vizinho] = vertice
                    dfs_recursivo_helper(vizinho, profundidade + 1)
        
        # Inicia a busca recursiva
        dfs_recursivo_helper(origem)
        
        # Reconstrói o caminho se um destino foi especificado
        caminho = None
        if destino is not None and destino in predecessor:
            caminho = DFS._reconstruir_caminho(predecessor, origem, destino)
            print(f"\n{'='*60}")
            print(f"CAMINHO ENCONTRADO:")
            print(f"  {' -> '.join(map(str, caminho))}")
            print(f"  Número de arestas: {len(caminho) - 1}")
            print(f"{'='*60}")
        elif destino is not None:
            print(f"\n✗ Destino {destino} não foi encontrado (não há caminho)")
        
        print(f"\nVértices visitados na ordem: {visitados}")
        print(f"Total de vértices explorados: {len(visitados)}")
        
        return {
            'visitados': visitados,
            'predecessor': predecessor,
            'caminho': caminho,
            'encontrado': encontrado[0]
        }
    
    @staticmethod
    def _buscar_iterativo(grafo: Grafo, origem: int, destino: Optional[int] = None) -> Dict:
        """
        Implementação iterativa do DFS usando pilha.
        """
        visitados = []
        predecessor = {origem: None}
        pilha = [origem]  # Pilha para DFS
        
        print(f"\n{'='*60}")
        print(f"EXECUTANDO DFS - BUSCA EM PROFUNDIDADE (ITERATIVA)")
        print(f"{'='*60}")
        print(f"Origem: {origem}")
        if destino is not None:
            print(f"Destino: {destino}")
        print(f"\nIniciando busca...")
        
        passo = 1
        
        # Loop principal do DFS iterativo
        while pilha:
            # Remove o último vértice da pilha (topo)
            vertice_atual = pilha.pop()
            
            # Se já foi visitado, pula
            if vertice_atual in visitados:
                continue
            
            visitados.append(vertice_atual)
            
            print(f"\nPasso {passo}:")
            print(f"  Visitando vértice: {vertice_atual}")
            print(f"  Pilha atual: {pilha}")
            
            # Se encontrou o destino, pode parar
            if destino is not None and vertice_atual == destino:
                print(f"\n✓ Destino {destino} encontrado!")
                break
            
            # Explora todos os vizinhos (adiciona na pilha em ordem reversa)
            vizinhos = grafo.obter_vizinhos(vertice_atual)
            vizinhos_nao_visitados = []
            
            for vizinho, peso in reversed(vizinhos):
                if vizinho not in visitados and vizinho not in [v for v in pilha]:
                    if vizinho not in predecessor:
                        predecessor[vizinho] = vertice_atual
                    pilha.append(vizinho)
                    vizinhos_nao_visitados.append(vizinho)
            
            if vizinhos_nao_visitados:
                print(f"  Novos vizinhos adicionados à pilha: {vizinhos_nao_visitados}")
            else:
                print(f"  Nenhum vizinho novo encontrado")
            
            passo += 1
        
        # Reconstrói o caminho se um destino foi especificado
        caminho = None
        encontrado = False
        if destino is not None and destino in predecessor:
            caminho = DFS._reconstruir_caminho(predecessor, origem, destino)
            encontrado = True
            print(f"\n{'='*60}")
            print(f"CAMINHO ENCONTRADO:")
            print(f"  {' -> '.join(map(str, caminho))}")
            print(f"  Número de arestas: {len(caminho) - 1}")
            print(f"{'='*60}")
        elif destino is not None:
            print(f"\n✗ Destino {destino} não foi encontrado (não há caminho)")
        
        print(f"\nVértices visitados na ordem: {visitados}")
        print(f"Total de vértices explorados: {len(visitados)}")
        
        return {
            'visitados': visitados,
            'predecessor': predecessor,
            'caminho': caminho,
            'encontrado': encontrado
        }
    
    @staticmethod
    def _reconstruir_caminho(predecessor: Dict, origem: int, destino: int) -> List[int]:
        """
        Reconstrói o caminho do destino até a origem usando o mapa de predecessores.
        
        Args:
            predecessor (Dict): Mapa de predecessores
            origem (int): Vértice de origem
            destino (int): Vértice de destino
            
        Returns:
            List[int]: Caminho da origem ao destino
        """
        caminho = []
        atual = destino
        
        # Reconstrói o caminho de trás para frente
        while atual is not None:
            caminho.append(atual)
            atual = predecessor.get(atual)
        
        # Inverte o caminho para ficar da origem ao destino
        caminho.reverse()
        return caminho


# Função auxiliar para demonstração
def demonstrar_bfs_dfs():
    """
    Função de demonstração dos algoritmos BFS e DFS.
    """
    from grafo import GrafoExemplos
    
    print("\n" + "="*70)
    print("DEMONSTRAÇÃO: ALGORITMOS BFS E DFS")
    print("="*70)
    
    # Cria um grafo de exemplo
    print("\nCriando grafo de exemplo (Mapa de Cidade com 20 vértices)...")
    grafo = GrafoExemplos.criar_mapa_cidade()
    nomes = GrafoExemplos.obter_nomes_mapa_cidade()
    
    print("\nGrafo criado com sucesso!")
    print(f"Locais disponíveis:")
    for id_local, nome in sorted(nomes.items()):
        print(f"  {id_local}: {nome}")
    
    # Demonstração BFS
    print("\n" + "="*70)
    print("EXEMPLO 1: BFS - Encontrar caminho do Centro ao Aeroporto")
    print("="*70)
    resultado_bfs = BFS.buscar(grafo, origem=0, destino=5)
    
    if resultado_bfs['caminho']:
        print("\nCaminho com nomes dos locais:")
        caminho_nomes = [nomes[v] for v in resultado_bfs['caminho']]
        print(f"  {' -> '.join(caminho_nomes)}")
    
    # Demonstração DFS Recursivo
    print("\n" + "="*70)
    print("EXEMPLO 2: DFS Recursivo - Encontrar caminho do Centro ao Aeroporto")
    print("="*70)
    resultado_dfs_rec = DFS.buscar(grafo, origem=0, destino=5, usar_recursao=True)
    
    if resultado_dfs_rec['caminho']:
        print("\nCaminho com nomes dos locais:")
        caminho_nomes = [nomes[v] for v in resultado_dfs_rec['caminho']]
        print(f"  {' -> '.join(caminho_nomes)}")
    
    # Demonstração DFS Iterativo
    print("\n" + "="*70)
    print("EXEMPLO 3: DFS Iterativo - Encontrar caminho do Centro ao Aeroporto")
    print("="*70)
    resultado_dfs_iter = DFS.buscar(grafo, origem=0, destino=5, usar_recursao=False)
    
    if resultado_dfs_iter['caminho']:
        print("\nCaminho com nomes dos locais:")
        caminho_nomes = [nomes[v] for v in resultado_dfs_iter['caminho']]
        print(f"  {' -> '.join(caminho_nomes)}")
    
    # Comparação
    print("\n" + "="*70)
    print("COMPARAÇÃO DOS RESULTADOS")
    print("="*70)
    print(f"BFS - Número de arestas no caminho: {len(resultado_bfs['caminho']) - 1 if resultado_bfs['caminho'] else 'N/A'}")
    print(f"DFS Recursivo - Número de arestas: {len(resultado_dfs_rec['caminho']) - 1 if resultado_dfs_rec['caminho'] else 'N/A'}")
    print(f"DFS Iterativo - Número de arestas: {len(resultado_dfs_iter['caminho']) - 1 if resultado_dfs_iter['caminho'] else 'N/A'}")
    print("\nObservação: BFS sempre encontra o caminho com MENOR número de arestas!")


if __name__ == "__main__":
    demonstrar_bfs_dfs()
