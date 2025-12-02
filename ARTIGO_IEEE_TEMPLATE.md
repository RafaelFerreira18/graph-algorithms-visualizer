# Template para Artigo IEEE
## Algoritmos de Busca e Caminhamento em Grafos

---

> **INSTRUÇÕES:** Este é um template para ajudar na elaboração do artigo no formato IEEE.
> Substitua as seções entre [colchetes] com o conteúdo específico da sua equipe.
> Mantenha a formatação IEEE padrão para a versão final em LaTeX ou Word.

---

# Algoritmos de Busca e Caminhamento em Grafos: Implementação e Análise Comparativa

**Autores:**  
[Nome Completo do Aluno 1]¹, [Nome Completo do Aluno 2]¹, [Nome Completo do Aluno 3]¹, [Nome Completo do Aluno 4]¹

¹[Nome da Instituição]  
[Departamento]  
[Cidade, Estado, País]  
Email: {aluno1, aluno2, aluno3, aluno4}@instituicao.edu.br

---

## Abstract

Este trabalho apresenta a implementação e análise de algoritmos fundamentais para busca e caminhamento em grafos: BFS (Breadth-First Search), DFS (Depth-First Search), Bellman-Ford, Dijkstra, e algoritmos de Árvore Geradora Mínima (Kruskal e Prim). O objetivo é demonstrar o funcionamento prático desses algoritmos através de implementações em Python, utilizando grafos com no mínimo 16 vértices que simulam problemas reais, como navegação em mapas urbanos e roteamento em redes de computadores. Os resultados experimentais confirmam as complexidades teóricas e mostram as aplicações práticas de cada algoritmo. Este estudo contribui para o entendimento aprofundado de estruturas de dados e algoritmos em grafos, essenciais para a ciência da computação.

**Palavras-chave:** Grafos, BFS, DFS, Bellman-Ford, Dijkstra, MST, Kruskal, Prim

---

## I. INTRODUÇÃO

### A. Contexto

Grafos são estruturas de dados fundamentais na ciência da computação, utilizados para modelar relações entre objetos em diversos domínios, incluindo redes de computadores, sistemas de transporte, redes sociais, e análise de algoritmos [1]. A capacidade de navegar e encontrar caminhos eficientes em grafos é essencial para resolver problemas complexos do mundo real.

### B. Motivação

[Descreva por que este trabalho é importante. Exemplo: "A compreensão profunda dos algoritmos de grafos é crucial para o desenvolvimento de sistemas eficientes..."]

### C. Objetivos

Este trabalho tem como objetivos:

1. Implementar os algoritmos de busca em grafos (BFS e DFS)
2. Implementar algoritmos de menor caminho (Bellman-Ford e Dijkstra)
3. Implementar algoritmos de Árvore Geradora Mínima (Kruskal e Prim)
4. Analisar e comparar o desempenho e características de cada algoritmo
5. Demonstrar aplicações práticas através de simulações

### D. Organização do Artigo

O restante deste artigo está organizado da seguinte forma: a Seção II apresenta a fundamentação teórica; a Seção III descreve a metodologia utilizada; a Seção IV detalha a implementação; a Seção V apresenta os resultados experimentais; e a Seção VI conclui o trabalho.

---

## II. FUNDAMENTAÇÃO TEÓRICA

### A. Conceitos Básicos de Grafos

Um grafo G = (V, E) é definido por um conjunto de vértices V e um conjunto de arestas E, onde cada aresta conecta dois vértices [1]. Grafos podem ser:

- **Direcionados:** As arestas têm direção (u → v)
- **Não-direcionados:** As arestas são bidirecionais (u — v)
- **Ponderados:** As arestas possuem pesos associados
- **Não-ponderados:** Todas as arestas têm peso igual

### B. Algoritmos de Busca

#### 1) BFS (Breadth-First Search)

BFS é um algoritmo de busca em largura que explora o grafo nível por nível [2]. Utiliza uma fila (estrutura FIFO) para controlar a ordem de visita dos vértices.

**Complexidade:** O(V + E), onde V é o número de vértices e E o número de arestas.

**Propriedades:**
- Encontra o caminho com menor número de arestas
- Garante visita a todos os vértices alcançáveis
- Útil para grafos não-ponderados

**Pseudocódigo:**
```
BFS(G, origem):
    criar fila Q
    marcar origem como visitado
    Q.enqueue(origem)
    
    enquanto Q não estiver vazia:
        u = Q.dequeue()
        para cada vizinho v de u:
            se v não foi visitado:
                marcar v como visitado
                predecessor[v] = u
                Q.enqueue(v)
```

#### 2) DFS (Depth-First Search)

DFS é um algoritmo de busca em profundidade que explora o mais fundo possível antes de retroceder [2]. Pode ser implementado recursivamente ou com uma pilha (estrutura LIFO).

**Complexidade:** O(V + E)

**Propriedades:**
- Útil para detectar ciclos
- Aplicado em ordenação topológica
- Menor uso de memória em certos casos

**Pseudocódigo (Recursivo):**
```
DFS(G, u):
    marcar u como visitado
    para cada vizinho v de u:
        se v não foi visitado:
            predecessor[v] = u
            DFS(G, v)
```

### C. Algoritmos de Menor Caminho

#### 1) Algoritmo de Bellman-Ford

O algoritmo de Bellman-Ford encontra o menor caminho de um vértice origem para todos os outros vértices, mesmo na presença de arestas com peso negativo [3].

**Complexidade:** O(V × E)

**Propriedades:**
- Funciona com pesos negativos
- Detecta ciclos de peso negativo
- Mais lento que Dijkstra

**Funcionamento:**
1. Inicializa distâncias: dist[origem] = 0, demais = ∞
2. Relaxa todas as arestas V-1 vezes
3. Verifica ciclos negativos

**Relaxação de Aresta:**
```
Relaxar(u, v, peso):
    se dist[u] + peso < dist[v]:
        dist[v] = dist[u] + peso
        predecessor[v] = u
```

#### 2) Algoritmo de Dijkstra

O algoritmo de Dijkstra encontra o menor caminho usando uma fila de prioridade, sendo mais eficiente que Bellman-Ford quando não há pesos negativos [4].

**Complexidade:** O((V + E) log V) com heap binário

**Propriedades:**
- Requer pesos não-negativos
- Mais eficiente que Bellman-Ford
- Amplamente usado em aplicações práticas

**Pseudocódigo:**
```
Dijkstra(G, origem):
    para cada vértice v:
        dist[v] = ∞
    dist[origem] = 0
    
    criar heap H com origem
    
    enquanto H não estiver vazio:
        u = H.extractMin()
        para cada vizinho v de u com peso w:
            se dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                predecessor[v] = u
                H.insert(v, dist[v])
```

### D. Algoritmos de Árvore Geradora Mínima

Uma Árvore Geradora Mínima (MST - Minimum Spanning Tree) é uma árvore que conecta todos os vértices de um grafo com o menor custo total possível [5].

**Propriedades de uma MST:**
- Conecta todos os vértices
- Não contém ciclos (é uma árvore)
- Possui V-1 arestas
- Tem custo mínimo

#### 1) Algoritmo de Kruskal

Kruskal ordena todas as arestas por peso e adiciona as de menor peso que não formam ciclos [6].

**Complexidade:** O(E log E)

**Estrutura de Dados:** Union-Find (Disjoint Set) para detectar ciclos

**Pseudocódigo:**
```
Kruskal(G):
    MST = conjunto vazio
    ordenar arestas por peso crescente
    criar Union-Find para todos os vértices
    
    para cada aresta (u, v, peso):
        se Find(u) ≠ Find(v):
            MST.adicionar((u, v, peso))
            Union(u, v)
    
    retornar MST
```

#### 2) Algoritmo de Prim

Prim expande a MST a partir de um vértice, sempre adicionando a aresta de menor peso que conecta a MST a um vértice fora dela [7].

**Complexidade:** O((V + E) log V) com heap

**Pseudocódigo:**
```
Prim(G, origem):
    MST = conjunto vazio
    criar heap H
    marcar origem como incluída
    adicionar arestas de origem em H
    
    enquanto |MST| < V-1:
        (u, v, peso) = H.extractMin()
        se v não está incluído:
            MST.adicionar((u, v, peso))
            marcar v como incluído
            adicionar arestas de v em H
    
    retornar MST
```

---

## III. METODOLOGIA

### A. Linguagem e Ferramentas

O projeto foi desenvolvido em Python 3.8+ devido às seguintes vantagens:

- Sintaxe clara e legível
- Bibliotecas padrão robustas (collections, heapq)
- Facilidade de implementação e depuração
- Portabilidade entre sistemas operacionais

**Ferramentas utilizadas:**
- Python 3.8+
- Editor de código: [VSCode/PyCharm/outro]
- Controle de versão: Git
- Plataforma: GitHub

### B. Estrutura de Dados

A estrutura de dados escolhida para representar grafos foi a **lista de adjacência**, implementada com dicionários Python:

```python
class Grafo:
    def __init__(self, vertices, direcionado=False):
        self.vertices = vertices
        self.adj = defaultdict(list)  # vértice -> [(vizinho, peso)]
        self.direcionado = direcionado
```

**Justificativa:**
- Eficiente para grafos esparsos (comum em aplicações reais)
- Permite iteração rápida sobre vizinhos
- Uso eficiente de memória: O(V + E)

### C. Grafos de Teste

Foram criados dois grafos para teste e demonstração:

#### 1) Mapa de Cidade
- **Vértices:** 20 (locais urbanos)
- **Tipo:** Não-direcionado, ponderado
- **Pesos:** Distâncias em km
- **Aplicação:** Navegação urbana, planejamento de rotas

#### 2) Rede de Computadores
- **Vértices:** 16 (servidores/clientes)
- **Tipo:** Direcionado, ponderado
- **Pesos:** Latência em ms
- **Aplicação:** Roteamento de rede, análise de latência

### D. Metodologia de Testes

[Descreva como os testes foram realizados]

---

## IV. IMPLEMENTAÇÃO

### A. Estrutura do Projeto

```
trabGrafosPart2/
├── main.py                      # Interface interativa
├── grafo.py                     # Estrutura de dados
├── bfs_dfs.py                   # Algoritmos de busca
├── bellman_ford_dijkstra.py     # Algoritmos de menor caminho
└── mst_kruskal_prim.py          # Algoritmos de MST
```

### B. Decisões de Implementação

#### 1) Representação de Grafos

A classe `Grafo` utiliza `defaultdict(list)` para permitir adição dinâmica de arestas sem necessidade de pré-inicialização.

#### 2) BFS e DFS

Ambos os algoritmos foram implementados com rastreamento detalhado de:
- Ordem de visita
- Predecessores (para reconstrução de caminhos)
- Distância/profundidade

**Exemplo - BFS:**
```python
def buscar(grafo, origem, destino=None):
    visitados = []
    predecessor = {origem: None}
    distancia = {origem: 0}
    fila = deque([origem])
    
    while fila:
        u = fila.popleft()
        visitados.append(u)
        
        if destino and u == destino:
            break
            
        for v, peso in grafo.obter_vizinhos(u):
            if v not in predecessor:
                predecessor[v] = u
                distancia[v] = distancia[u] + 1
                fila.append(v)
    
    return {
        'visitados': visitados,
        'predecessor': predecessor,
        'distancia': distancia
    }
```

#### 3) Bellman-Ford e Dijkstra

**Bellman-Ford** implementa relaxação de arestas V-1 vezes:
```python
for iteracao in range(len(vertices) - 1):
    for u, v, peso in arestas:
        if distancia[u] + peso < distancia[v]:
            distancia[v] = distancia[u] + peso
            predecessor[v] = u
```

**Dijkstra** utiliza `heapq` (heap binário) do Python:
```python
heap = [(0, origem)]
while heap:
    dist_u, u = heapq.heappop(heap)
    for v, peso in grafo.obter_vizinhos(u):
        nova_dist = distancia[u] + peso
        if nova_dist < distancia[v]:
            distancia[v] = nova_dist
            heapq.heappush(heap, (nova_dist, v))
```

#### 4) Union-Find para Kruskal

Implementação otimizada com **compressão de caminho** e **union by rank**:

```python
class UnionFind:
    def find(self, v):
        if self.pai[v] != v:
            self.pai[v] = self.find(self.pai[v])  # Compressão
        return self.pai[v]
    
    def union(self, u, v):
        raiz_u = self.find(u)
        raiz_v = self.find(v)
        
        if raiz_u == raiz_v:
            return False
        
        # Union by rank
        if self.rank[raiz_u] < self.rank[raiz_v]:
            self.pai[raiz_u] = raiz_v
        else:
            self.pai[raiz_v] = raiz_u
            if self.rank[raiz_u] == self.rank[raiz_v]:
                self.rank[raiz_u] += 1
        
        return True
```

### C. Interface do Usuário

Foi desenvolvida uma interface de menu interativo que permite:
- Seleção de algoritmos
- Escolha de grafos e vértices
- Comparação entre algoritmos
- Visualização detalhada de execução

---

## V. RESULTADOS

### A. Testes com BFS e DFS

**Cenário:** Encontrar caminho do Centro (vértice 0) ao Aeroporto (vértice 5) no Mapa de Cidade.

**Resultados:**

| Algoritmo | Caminho Encontrado | Nº de Arestas | Vértices Explorados |
|-----------|-------------------|---------------|---------------------|
| BFS       | [Listar caminho]  | [N]           | [M]                 |
| DFS (Rec) | [Listar caminho]  | [N]           | [M]                 |
| DFS (Iter)| [Listar caminho]  | [N]           | [M]                 |

**Análise:**
[Analise os resultados. Exemplo: "BFS encontrou o caminho mais curto com 4 arestas, enquanto DFS encontrou um caminho alternativo com 6 arestas..."]

### B. Testes com Bellman-Ford e Dijkstra

**Cenário:** Encontrar menor caminho (custo) do Centro ao Aeroporto.

**Resultados:**

| Algoritmo     | Custo Total | Tempo de Execução | Caminho |
|---------------|-------------|-------------------|---------|
| Bellman-Ford  | [X] km      | [Y] ms            | [...]   |
| Dijkstra      | [X] km      | [Z] ms            | [...]   |

**Análise:**
[Analise a comparação. Exemplo: "Ambos encontraram o mesmo caminho ótimo de custo 12.5 km, mas Dijkstra foi 3x mais rápido..."]

### C. Testes com Kruskal e Prim

**Cenário:** Encontrar MST do Mapa de Cidade (20 vértices).

**Resultados:**

| Algoritmo | Custo Total MST | Nº de Arestas | Tempo de Execução |
|-----------|-----------------|---------------|-------------------|
| Kruskal   | [X] km          | 19            | [Y] ms            |
| Prim      | [X] km          | 19            | [Z] ms            |

**Análise:**
[Analise os resultados. Exemplo: "Ambos encontraram MSTs de mesmo custo (propriedade teórica), mas com arestas diferentes..."]

### D. Análise Comparativa de Complexidade

[Crie uma tabela comparando as complexidades teóricas com os resultados práticos]

| Algoritmo     | Complexidade Teórica | Observação Prática |
|---------------|---------------------|-------------------|
| BFS           | O(V + E)            | [...]             |
| DFS           | O(V + E)            | [...]             |
| Bellman-Ford  | O(V × E)            | [...]             |
| Dijkstra      | O((V+E) log V)      | [...]             |
| Kruskal       | O(E log E)          | [...]             |
| Prim          | O((V+E) log V)      | [...]             |

### E. Aplicações Práticas

[Descreva como cada algoritmo pode ser aplicado em problemas reais]

---

## VI. CONCLUSÃO

### A. Síntese dos Resultados

[Resuma os principais resultados obtidos]

Este trabalho apresentou a implementação e análise de seis algoritmos fundamentais para grafos: BFS, DFS, Bellman-Ford, Dijkstra, Kruskal e Prim. Os resultados experimentais confirmaram as complexidades teóricas e demonstraram as características distintas de cada algoritmo.

### B. Contribuições

[Liste as contribuições do trabalho]

- Implementação completa e bem documentada dos algoritmos
- Análise comparativa prática
- Demonstração de aplicações reais
- Material educacional para estudo de grafos

### C. Limitações

[Discuta limitações do trabalho]

- Testes limitados a grafos de tamanho moderado
- [Outras limitações]

### D. Trabalhos Futuros

[Sugira extensões do trabalho]

- Implementação de visualização gráfica dos algoritmos
- Análise com grafos maiores (milhares de vértices)
- Implementação de outros algoritmos (Floyd-Warshall, A*, etc.)
- Paralelização dos algoritmos
- Comparação com bibliotecas otimizadas (NetworkX)

---

## AGRADECIMENTOS

[Adicione agradecimentos se apropriado]

Os autores agradecem ao Prof. [Nome] pela orientação e ao [Instituição] pelo suporte.

---

## REFERÊNCIAS

[1] T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, **Introduction to Algorithms**, 3rd ed. Cambridge, MA: MIT Press, 2009.

[2] R. Sedgewick and K. Wayne, **Algorithms**, 4th ed. Boston, MA: Addison-Wesley, 2011.

[3] R. Bellman, "On a routing problem," *Quarterly of Applied Mathematics*, vol. 16, no. 1, pp. 87-90, 1958.

[4] E. W. Dijkstra, "A note on two problems in connexion with graphs," *Numerische Mathematik*, vol. 1, no. 1, pp. 269-271, 1959.

[5] R. L. Graham and P. Hell, "On the history of the minimum spanning tree problem," *IEEE Annals of the History of Computing*, vol. 7, no. 1, pp. 43-57, 1985.

[6] J. B. Kruskal, "On the shortest spanning subtree of a graph and the traveling salesman problem," *Proceedings of the American Mathematical Society*, vol. 7, no. 1, pp. 48-50, 1956.

[7] R. C. Prim, "Shortest connection networks and some generalizations," *Bell System Technical Journal*, vol. 36, no. 6, pp. 1389-1401, 1957.

[8] GeeksforGeeks, "Graph Data Structure And Algorithms," [Online]. Available: https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/

[9] Python Software Foundation, "Python Documentation," [Online]. Available: https://docs.python.org/3/

---

## APÊNDICE A: CÓDIGO-FONTE

[Opcional: Inclua trechos de código relevantes ou referência ao repositório GitHub]

Código-fonte completo disponível em: [URL do GitHub]

---

## SOBRE OS AUTORES

**[Nome do Aluno 1]** é estudante de [Curso] na [Instituição]. Suas áreas de interesse incluem [áreas].

**[Nome do Aluno 2]** é estudante de [Curso] na [Instituição]. Suas áreas de interesse incluem [áreas].

**[Nome do Aluno 3]** é estudante de [Curso] na [Instituição]. Suas áreas de interesse incluem [áreas].

**[Nome do Aluno 4]** é estudante de [Curso] na [Instituição]. Suas áreas de interesse incluem [áreas].

---

**Nota:** Para a versão final do artigo, utilize um template IEEE LaTeX ou Word oficial disponível em: https://www.ieee.org/conferences/publishing/templates.html
