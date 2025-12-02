"""
Módulo de Estrutura de Dados: Grafo
====================================
Este módulo contém a implementação da estrutura de dados Grafo,
que será utilizada por todos os algoritmos do trabalho.

Autores: [COLOQUE OS NOMES DA EQUIPE AQUI]
Data: Dezembro 2025
"""

from collections import defaultdict, deque
from typing import List, Dict, Set, Tuple, Optional
import heapq


class Grafo:
    """
    Classe que representa um Grafo usando lista de adjacência.
    
    Atributos:
        vertices (int): Número de vértices no grafo
        adj (dict): Dicionário de listas de adjacência
        direcionado (bool): Indica se o grafo é direcionado ou não
    """
    
    def __init__(self, vertices: int = 0, direcionado: bool = False):
        """
        Inicializa um grafo.
        
        Args:
            vertices (int): Número de vértices
            direcionado (bool): True se o grafo é direcionado, False caso contrário
        """
        self.vertices = vertices
        self.adj = defaultdict(list)  # Lista de adjacência
        self.direcionado = direcionado
        
    def adicionar_aresta(self, origem: int, destino: int, peso: float = 1.0):
        """
        Adiciona uma aresta ao grafo.
        
        Args:
            origem (int): Vértice de origem
            destino (int): Vértice de destino
            peso (float): Peso da aresta (padrão: 1.0)
        """
        self.adj[origem].append((destino, peso))
        
        # Se o grafo não é direcionado, adiciona aresta reversa
        if not self.direcionado:
            self.adj[destino].append((origem, peso))
    
    def obter_vertices(self) -> List[int]:
        """
        Retorna a lista de todos os vértices do grafo.
        
        Returns:
            List[int]: Lista de vértices
        """
        vertices_set = set()
        for v in self.adj.keys():
            vertices_set.add(v)
            for vizinho, _ in self.adj[v]:
                vertices_set.add(vizinho)
        return sorted(list(vertices_set))
    
    def obter_vizinhos(self, vertice: int) -> List[Tuple[int, float]]:
        """
        Retorna os vizinhos de um vértice.
        
        Args:
            vertice (int): Vértice a ser consultado
            
        Returns:
            List[Tuple[int, float]]: Lista de tuplas (vizinho, peso)
        """
        return self.adj[vertice]
    
    def obter_arestas(self) -> List[Tuple[int, int, float]]:
        """
        Retorna todas as arestas do grafo.
        
        Returns:
            List[Tuple[int, int, float]]: Lista de tuplas (origem, destino, peso)
        """
        arestas = []
        visitados = set()
        
        for origem in self.adj:
            for destino, peso in self.adj[origem]:
                if self.direcionado:
                    arestas.append((origem, destino, peso))
                else:
                    # Para grafos não direcionados, evita duplicatas
                    aresta = tuple(sorted([origem, destino]))
                    if aresta not in visitados:
                        arestas.append((origem, destino, peso))
                        visitados.add(aresta)
        
        return arestas
    
    def __str__(self) -> str:
        """
        Representação em string do grafo.
        
        Returns:
            str: Representação do grafo
        """
        resultado = f"Grafo {'Direcionado' if self.direcionado else 'Não Direcionado'}\n"
        resultado += f"Vértices: {len(self.obter_vertices())}\n"
        resultado += "Arestas:\n"
        
        for origem in sorted(self.adj.keys()):
            for destino, peso in self.adj[origem]:
                if self.direcionado:
                    resultado += f"  {origem} -> {destino} (peso: {peso})\n"
                else:
                    if origem <= destino:  # Evita duplicatas
                        resultado += f"  {origem} -- {destino} (peso: {peso})\n"
        
        return resultado


class GrafoExemplos:
    """
    Classe que contém exemplos de grafos prontos para testes.
    Todos os grafos têm pelo menos 16 vértices, conforme requisito.
    """
    
    @staticmethod
    def criar_mapa_cidade() -> Grafo:
        """
        Cria um grafo representando um mapa de cidade com 20 pontos de interesse.
        Este exemplo simula distâncias entre locais em uma cidade (em km).
        
        Pontos de interesse:
        0: Centro, 1: Shopping, 2: Universidade, 3: Hospital, 4: Parque
        5: Aeroporto, 6: Estádio, 7: Teatro, 8: Museu, 9: Biblioteca
        10: Restaurante, 11: Hotel, 12: Escola, 13: Mercado, 14: Farmácia
        15: Posto de Gasolina, 16: Cinema, 17: Academia, 18: Banco, 19: Correios
        
        Returns:
            Grafo: Grafo não direcionado representando o mapa
        """
        g = Grafo(20, direcionado=False)
        
        # Conexões do Centro (0) - hub principal
        g.adicionar_aresta(0, 1, 2.5)   # Centro -> Shopping
        g.adicionar_aresta(0, 2, 3.0)   # Centro -> Universidade
        g.adicionar_aresta(0, 3, 1.8)   # Centro -> Hospital
        g.adicionar_aresta(0, 18, 0.5)  # Centro -> Banco
        
        # Shopping (1) - área comercial
        g.adicionar_aresta(1, 10, 1.2)  # Shopping -> Restaurante
        g.adicionar_aresta(1, 16, 0.8)  # Shopping -> Cinema
        g.adicionar_aresta(1, 13, 1.5)  # Shopping -> Mercado
        
        # Universidade (2) - área educacional
        g.adicionar_aresta(2, 9, 0.6)   # Universidade -> Biblioteca
        g.adicionar_aresta(2, 12, 2.0)  # Universidade -> Escola
        g.adicionar_aresta(2, 8, 1.5)   # Universidade -> Museu
        
        # Hospital (3) - área de saúde
        g.adicionar_aresta(3, 14, 0.4)  # Hospital -> Farmácia
        g.adicionar_aresta(3, 11, 2.2)  # Hospital -> Hotel
        
        # Parque (4) - área de lazer
        g.adicionar_aresta(4, 6, 3.5)   # Parque -> Estádio
        g.adicionar_aresta(4, 17, 1.0)  # Parque -> Academia
        g.adicionar_aresta(4, 7, 2.8)   # Parque -> Teatro
        
        # Aeroporto (5) - transporte
        g.adicionar_aresta(5, 11, 1.5)  # Aeroporto -> Hotel
        g.adicionar_aresta(5, 15, 2.0)  # Aeroporto -> Posto
        g.adicionar_aresta(5, 0, 12.0)  # Aeroporto -> Centro
        
        # Estádio (6)
        g.adicionar_aresta(6, 15, 1.8)  # Estádio -> Posto
        g.adicionar_aresta(6, 10, 2.5)  # Estádio -> Restaurante
        
        # Teatro (7)
        g.adicionar_aresta(7, 8, 0.7)   # Teatro -> Museu
        g.adicionar_aresta(7, 16, 1.3)  # Teatro -> Cinema
        
        # Museu (8)
        g.adicionar_aresta(8, 9, 0.5)   # Museu -> Biblioteca
        
        # Biblioteca (9)
        g.adicionar_aresta(9, 12, 1.8)  # Biblioteca -> Escola
        
        # Restaurante (10)
        g.adicionar_aresta(10, 11, 0.9) # Restaurante -> Hotel
        
        # Hotel (11)
        g.adicionar_aresta(11, 19, 1.1) # Hotel -> Correios
        
        # Escola (12)
        g.adicionar_aresta(12, 13, 0.8) # Escola -> Mercado
        
        # Mercado (13)
        g.adicionar_aresta(13, 14, 0.6) # Mercado -> Farmácia
        
        # Farmácia (14)
        g.adicionar_aresta(14, 18, 1.0) # Farmácia -> Banco
        
        # Posto de Gasolina (15)
        g.adicionar_aresta(15, 19, 2.3) # Posto -> Correios
        
        # Cinema (16)
        g.adicionar_aresta(16, 17, 1.4) # Cinema -> Academia
        
        # Academia (17)
        g.adicionar_aresta(17, 18, 1.6) # Academia -> Banco
        
        # Banco (18)
        g.adicionar_aresta(18, 19, 0.7) # Banco -> Correios
        
        return g
    
    @staticmethod
    def criar_rede_computadores() -> Grafo:
        """
        Cria um grafo direcionado representando uma rede de computadores.
        Simula latência entre servidores (em ms).
        
        Returns:
            Grafo: Grafo direcionado representando a rede
        """
        g = Grafo(16, direcionado=True)
        
        # Servidor Principal (0) -> Servidores Regionais
        g.adicionar_aresta(0, 1, 10)
        g.adicionar_aresta(0, 2, 15)
        g.adicionar_aresta(0, 3, 12)
        
        # Servidores Regionais -> Locais
        g.adicionar_aresta(1, 4, 5)
        g.adicionar_aresta(1, 5, 8)
        g.adicionar_aresta(2, 6, 6)
        g.adicionar_aresta(2, 7, 7)
        g.adicionar_aresta(3, 8, 9)
        g.adicionar_aresta(3, 9, 11)
        
        # Servidores Locais -> Clientes
        g.adicionar_aresta(4, 10, 3)
        g.adicionar_aresta(5, 11, 4)
        g.adicionar_aresta(6, 12, 2)
        g.adicionar_aresta(7, 13, 5)
        g.adicionar_aresta(8, 14, 6)
        g.adicionar_aresta(9, 15, 4)
        
        # Conexões redundantes (backup)
        g.adicionar_aresta(1, 2, 20)
        g.adicionar_aresta(2, 3, 18)
        g.adicionar_aresta(4, 6, 15)
        g.adicionar_aresta(5, 7, 14)
        g.adicionar_aresta(10, 12, 25)
        
        return g
    
    @staticmethod
    def obter_nomes_mapa_cidade() -> Dict[int, str]:
        """
        Retorna um dicionário com os nomes dos locais do mapa da cidade.
        
        Returns:
            Dict[int, str]: Dicionário vértice -> nome
        """
        return {
            0: "Centro",
            1: "Shopping",
            2: "Universidade",
            3: "Hospital",
            4: "Parque",
            5: "Aeroporto",
            6: "Estádio",
            7: "Teatro",
            8: "Museu",
            9: "Biblioteca",
            10: "Restaurante",
            11: "Hotel",
            12: "Escola",
            13: "Mercado",
            14: "Farmácia",
            15: "Posto de Gasolina",
            16: "Cinema",
            17: "Academia",
            18: "Banco",
            19: "Correios"
        }
