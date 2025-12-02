# Trabalho de Grafos - Parte 2
## Algoritmos de Busca e Caminhamento em Grafos

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 📋 Sobre o Projeto

Este projeto implementa e demonstra os principais algoritmos de busca e caminhamento em grafos, desenvolvido como parte do Trabalho de Grafos - Parte 2.

### Algoritmos Implementados

#### 🔍 Algoritmos de Busca
- **BFS (Breadth-First Search)** - Busca em Largura
- **DFS (Depth-First Search)** - Busca em Profundidade (Recursivo e Iterativo)

#### 🛣️ Algoritmos de Menor Caminho
- **Bellman-Ford** - Funciona com pesos negativos
- **Dijkstra** - Mais eficiente para pesos não-negativos

#### 🌲 Algoritmos de Árvore Geradora Mínima (MST)
- **Kruskal** - Usa Union-Find
- **Prim** - Usa heap (fila de prioridade)

---

## 👥 Equipe

**IMPORTANTE:** Edite esta seção com os nomes dos integrantes da equipe!

- [Nome do Aluno 1] - [Matrícula]
- [Nome do Aluno 2] - [Matrícula]
- [Nome do Aluno 3] - [Matrícula]
- [Nome do Aluno 4] - [Matrícula]

**Disciplina:** [Nome da Disciplina]  
**Professor:** [Nome do Professor]  
**Instituição:** [Nome da Instituição]  
**Período:** Dezembro 2025

---

## 🚀 Como Executar

### Requisitos

- Python 3.8 ou superior
- Bibliotecas padrão do Python (nenhuma instalação adicional necessária)

### Instalação

1. **Clone ou baixe este repositório:**
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd trabGrafosPart2
   ```

2. **Verifique a instalação do Python:**
   ```bash
   python --version
   ```
   ou
   ```bash
   python3 --version
   ```

### Executando o Programa

#### Opção 1: Menu Interativo (Recomendado)

Execute o programa principal com menu interativo:

```bash
python main.py
```

O menu permite:
- Executar cada algoritmo individualmente
- Comparar algoritmos entre si
- Visualizar grafos disponíveis
- Executar todas as demonstrações de uma vez

#### Opção 2: Interface Gráfica Visual 🎨 (RECOMENDADO para apresentação!)

Execute a interface gráfica moderna:

```bash
python gui_visualizador.py
```

**Recursos da GUI:**
- ✅ Visualização gráfica dos grafos em círculo
- ✅ Cores diferentes para destacar caminhos e resultados
- ✅ 7 grafos disponíveis (2 exemplos + 5 aplicações práticas)
- ✅ Todos os 6 algoritmos executáveis com um clique
- ✅ Log de execução em tempo real
- ✅ Perfeito para gravar o vídeo da apresentação!

#### Opção 3: Demonstrações de Aplicações Práticas 🌟

Execute demonstrações de problemas reais:

```bash
python aplicacoes_praticas.py
```

**Aplicações disponíveis:**
- 🌐 **Rede Social (BFS)**: Encontrar o menor número de conexões entre duas pessoas
- 📦 **Sistema de Dependências (DFS)**: Detectar ciclos em instalação de pacotes
- 🎮 **Jogo RPG (Dijkstra)**: Pathfinding com terrenos de custos diferentes (estrada, floresta, montanha)
- 💰 **Mercado Forex (Bellman-Ford)**: Detectar arbitragem entre moedas (ciclos negativos)
- ⚡ **Rede Elétrica (MST)**: Conectar cidades com menor custo de cabeamento

#### Opção 4: Executar Algoritmos Individualmente

Cada módulo pode ser executado separadamente:

**BFS e DFS:**
```bash
python bfs_dfs.py
```

**Bellman-Ford e Dijkstra:**
```bash
python bellman_ford_dijkstra.py
```

**Kruskal e Prim:**
```bash
python mst_kruskal_prim.py
```

---

## 📁 Estrutura do Projeto

```
trabGrafosPart2/
│
├── main.py                      # Programa principal com menu interativo
├── gui_visualizador.py          # Interface gráfica visual (Tkinter) ⭐ NOVO!
├── aplicacoes_praticas.py       # Demonstrações de aplicações reais ⭐ NOVO!
├── grafo.py                     # Estrutura de dados Grafo e exemplos
├── bfs_dfs.py                   # Implementação BFS e DFS
├── bellman_ford_dijkstra.py     # Implementação Bellman-Ford e Dijkstra
├── mst_kruskal_prim.py          # Implementação Kruskal e Prim
├── teste_rapido.py              # Testes automatizados
├── README.md                    # Este arquivo
├── LICENSE                      # Licença MIT
├── requirements.txt             # Dependências (vazio - usa stdlib)
├── .gitignore                   # Arquivos ignorados pelo Git
└── [documentação adicional]
    ├── ARTIGO_IEEE_TEMPLATE.md
    ├── GUIA_APRESENTACAO.md
    ├── RESUMO_EXECUTIVO.md
    ├── COMANDOS.md
    ├── ARQUIVOS.md
    └── COMECE_AQUI.txt
```

---

## 📊 Grafos Disponíveis

### Grafos de Exemplo (Demonstração)

#### 1. Mapa de Cidade (20 vértices)
- **Tipo:** Não-direcionado
- **Vértices:** 20 locais (Centro, Shopping, Universidade, Hospital, etc.)
- **Arestas:** Distâncias entre locais em km
- **Aplicação:** Simulação de rotas urbanas, planejamento de transporte

#### 2. Rede de Computadores (16 vértices)
- **Tipo:** Direcionado
- **Vértices:** 16 servidores/clientes
- **Arestas:** Latência entre servidores em ms
- **Aplicação:** Roteamento em redes, análise de latência

### Aplicações Práticas Reais ⭐ NOVO!

#### 3. 🌐 Rede Social (20 vértices)
- **Algoritmo ideal:** BFS
- **Problema:** Encontrar o menor número de conexões entre duas pessoas
- **Por quê:** BFS encontra o caminho com menos "graus de separação"

#### 4. 📦 Sistema de Dependências (18 vértices)
- **Algoritmo ideal:** DFS
- **Problema:** Detectar ciclos em instalação de pacotes/bibliotecas
- **Por quê:** DFS explora profundamente e detecta ciclos eficientemente

#### 5. 🎮 Mapa de Jogo RPG (18 vértices)
- **Algoritmo ideal:** Dijkstra
- **Problema:** Pathfinding com terrenos de custos diferentes
- **Por quê:** Encontra caminho de menor custo (estrada=1, floresta=5, montanha=10, pântano=15)

#### 6. 💰 Mercado de Câmbio Forex (16 vértices)
- **Algoritmo ideal:** Bellman-Ford
- **Problema:** Detectar oportunidades de arbitragem entre moedas
- **Por quê:** Detecta ciclos negativos (lucro) e trabalha com pesos negativos

#### 7. ⚡ Rede Elétrica (18 vértices)
- **Algoritmo ideal:** MST (Kruskal/Prim)
- **Problema:** Conectar cidades com menor custo de cabeamento
- **Por quê:** Conecta todos os vértices sem ciclos com custo mínimo

---

## 🔬 Descrição dos Algoritmos

### BFS (Busca em Largura)

**Conceito:** Explora o grafo nível por nível, visitando todos os vizinhos antes de avançar.

**Características:**
- Usa fila (FIFO)
- Encontra o caminho com menor número de arestas
- Complexidade: O(V + E)

**Aplicações:**
- Encontrar menor caminho em grafos não-ponderados
- Redes sociais (grau de separação)
- Web crawlers

### DFS (Busca em Profundidade)

**Conceito:** Explora o mais profundo possível antes de retroceder.

**Características:**
- Usa pilha ou recursão (LIFO)
- Útil para detectar ciclos
- Complexidade: O(V + E)

**Aplicações:**
- Resolver labirintos
- Detectar ciclos
- Ordenação topológica

### Bellman-Ford

**Conceito:** Encontra o menor caminho de um vértice para todos os outros.

**Características:**
- Funciona com pesos negativos
- Detecta ciclos negativos
- Complexidade: O(V × E)

**Aplicações:**
- Roteamento com custos variáveis
- Análise de arbitragem financeira

### Dijkstra

**Conceito:** Encontra o menor caminho usando fila de prioridade.

**Características:**
- Requer pesos não-negativos
- Mais eficiente que Bellman-Ford
- Complexidade: O((V + E) log V)

**Aplicações:**
- GPS e navegação
- Roteamento em redes
- Jogos (pathfinding)

### Kruskal

**Conceito:** Ordena arestas e adiciona a menor que não forma ciclo.

**Características:**
- Usa Union-Find para detectar ciclos
- Bom para grafos esparsos
- Complexidade: O(E log E)

**Aplicações:**
- Projeto de redes (minimizar cabeamento)
- Clustering

### Prim

**Conceito:** Expande a árvore a partir de um vértice, sempre escolhendo a menor aresta.

**Características:**
- Usa heap (fila de prioridade)
- Bom para grafos densos
- Complexidade: O((V + E) log V)

**Aplicações:**
- Design de circuitos
- Redes de comunicação

---

## 📝 Exemplos de Uso

### Exemplo 1: Encontrar menor caminho com BFS

```python
from grafo import GrafoExemplos
from bfs_dfs import BFS

# Criar grafo
grafo = GrafoExemplos.criar_mapa_cidade()

# Executar BFS do Centro (0) ao Aeroporto (5)
resultado = BFS.buscar(grafo, origem=0, destino=5)

# Resultado
print(f"Caminho: {resultado['caminho']}")
print(f"Distância: {len(resultado['caminho']) - 1} arestas")
```

### Exemplo 2: Encontrar menor caminho ponderado com Dijkstra

```python
from grafo import GrafoExemplos
from bellman_ford_dijkstra import Dijkstra

# Criar grafo
grafo = GrafoExemplos.criar_mapa_cidade()

# Executar Dijkstra
resultado = Dijkstra.menor_caminho(grafo, origem=0, destino=5)

# Resultado
print(f"Caminho: {resultado['caminho']}")
print(f"Custo: {resultado['custo']} km")
```

### Exemplo 3: Encontrar MST com Kruskal

```python
from grafo import GrafoExemplos
from mst_kruskal_prim import Kruskal

# Criar grafo
grafo = GrafoExemplos.criar_mapa_cidade()

# Executar Kruskal
resultado = Kruskal.mst(grafo)

# Resultado
print(f"Custo total da MST: {resultado['custo_total']} km")
print(f"Número de arestas: {len(resultado['arestas'])}")
```

---

## 🎥 Apresentação em Vídeo

**IMPORTANTE:** Para atender aos requisitos do trabalho, grave um vídeo de até 20 minutos contendo:

1. **Conceitos Teóricos** (5-7 minutos)
   - Explicação de cada algoritmo
   - Quando usar cada um
   - Complexidade computacional

2. **Demonstração do Código** (8-10 minutos)
   - Estrutura do projeto
   - Código comentado
   - Execução passo a passo

3. **Exemplos Práticos** (3-5 minutos)
   - Execução do programa
   - Interpretação dos resultados
   - Casos de uso reais

**Dicas para a gravação:**
- Use o menu interativo do programa para demonstrar
- Execute comparações entre algoritmos
- Mostre os grafos com pelo menos 16 vértices
- Todos os integrantes devem participar

---

## 📄 Artigo IEEE

Um template para o artigo no formato IEEE está disponível no arquivo `ARTIGO_IEEE_TEMPLATE.md`.

O artigo deve conter:

1. **Resumo (Abstract)**
2. **Introdução**
3. **Fundamentação Teórica**
   - Descrição de cada algoritmo
   - Análise de complexidade
4. **Metodologia**
   - Linguagem e ferramentas
   - Estrutura de dados utilizada
5. **Implementação**
   - Detalhes técnicos
   - Decisões de projeto
6. **Resultados**
   - Testes realizados
   - Análise comparativa
7. **Conclusão**
8. **Referências**

---

## 🧪 Testes

Para verificar se tudo está funcionando:

```bash
# Teste rápido - executa todas as demonstrações
python main.py
# Escolha opção 5 no menu
```

---

## 📚 Referências

### Livros
- CORMEN, Thomas H. et al. **Introduction to Algorithms**. 3rd ed. MIT Press, 2009.
- SEDGEWICK, Robert; WAYNE, Kevin. **Algorithms**. 4th ed. Addison-Wesley, 2011.

### Artigos e Documentação
- Dijkstra, E. W. (1959). "A note on two problems in connexion with graphs"
- Bellman, R. (1958). "On a routing problem"
- Kruskal, J. B. (1956). "On the shortest spanning subtree of a graph"
- Prim, R. C. (1957). "Shortest connection networks and some generalizations"

### Online
- [GeeksforGeeks - Graph Algorithms](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)
- [Wikipedia - Graph Theory](https://en.wikipedia.org/wiki/Graph_theory)
- [Python Documentation](https://docs.python.org/3/)

---

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais.

---

## 📞 Contato

Para dúvidas sobre o projeto, entre em contato com os membros da equipe.

---

## ✅ Checklist para Entrega

- [ ] Todos os algoritmos implementados e funcionando
- [ ] Código comentado e explicado
- [ ] Grafos com pelo menos 16 vértices
- [ ] README.md completo com instruções
- [ ] Vídeo de apresentação gravado (até 20 minutos)
- [ ] Artigo no formato IEEE
- [ ] Código disponível no GitHub
- [ ] Nomes dos integrantes atualizados
- [ ] Todos os integrantes participaram da gravação

---

## 🎓 Observações Importantes

1. **Código Original:** Todo o código foi desenvolvido especificamente para este trabalho. Códigos copiados terão pontuação descontada ou anulada.

2. **Comentários:** O código está extensivamente comentado para facilitar a compreensão e apresentação.

3. **Requisitos Atendidos:**
   - ✅ Grafos com mínimo de 16 vértices
   - ✅ Todos os algoritmos solicitados implementados
   - ✅ Código explicado e comentado
   - ✅ Demonstrações funcionais
   - ✅ Problemas práticos simulados

4. **Bônus:** Implementação adicional de algoritmos de MST (Kruskal e Prim) para equipes com mais de 4 integrantes.

---

**Bom trabalho! 🚀**

*Última atualização: Dezembro 2025*
