"""
Interface Gráfica para Visualização de Algoritmos em Grafos
============================================================
Interface moderna usando Tkinter para visualizar e executar os algoritmos.

IMPORTANTE: Este módulo usa apenas bibliotecas padrão do Python!
Não é necessário instalar nada adicional.

Autores: [COLOQUE OS NOMES DA EQUIPE AQUI]
Data: Dezembro 2025
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import math
from typing import Dict, List, Tuple, Optional
import threading
import time

# Importa os módulos do projeto
from grafo import Grafo, GrafoExemplos
from bfs_dfs import BFS, DFS
from bellman_ford_dijkstra import BellmanFord, Dijkstra
from mst_kruskal_prim import Kruskal, Prim
from aplicacoes_praticas import (
    AplicacaoRedeSocial, AplicacaoDependencias, AplicacaoJogoRPG,
    AplicacaoMercadoFinanceiro, AplicacaoRedeEletrica
)


class VisualizadorGrafos:
    """
    Classe principal da interface gráfica para visualização de grafos.
    """
    
    def __init__(self, root):
        """Inicializa a interface gráfica."""
        self.root = root
        self.root.title("Visualizador de Algoritmos em Grafos - Trabalho de Grafos Parte 2")
        self.root.geometry("1400x900")
        
        # Configuração de cores (tema moderno)
        self.cores = {
            'bg': '#1e1e2e',
            'fg': '#cdd6f4',
            'bg_frame': '#313244',
            'bg_canvas': '#181825',
            'accent': '#89b4fa',
            'accent2': '#f5c2e7',
            'success': '#a6e3a1',
            'warning': '#fab387',
            'error': '#f38ba8',
            'vertice_normal': '#89b4fa',
            'vertice_visitado': '#a6e3a1',
            'vertice_origem': '#f9e2af',
            'vertice_destino': '#f38ba8',
            'aresta_normal': '#585b70',
            'aresta_caminho': '#a6e3a1',
            'aresta_mst': '#f9e2af'
        }
        
        # Configurar estilo
        self.root.configure(bg=self.cores['bg'])
        
        # Variáveis de estado
        self.grafo_atual = None
        self.nomes_vertices = None
        self.posicoes_vertices = {}
        self.arestas_destacadas = []
        self.vertices_destacados = {}
        self.animacao_ativa = False
        
        # Criar interface
        self.criar_interface()
        
        # Carregar grafo padrão
        self.carregar_grafo_mapa()
    
    def criar_interface(self):
        """Cria todos os componentes da interface."""
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.cores['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # ===== PAINEL SUPERIOR =====
        top_frame = tk.Frame(main_frame, bg=self.cores['bg_frame'], relief=tk.RAISED, borderwidth=2)
        top_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Título
        title_label = tk.Label(
            top_frame,
            text="🔍 VISUALIZADOR DE ALGORITMOS EM GRAFOS",
            font=("Arial", 18, "bold"),
            bg=self.cores['bg_frame'],
            fg=self.cores['accent']
        )
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(
            top_frame,
            text="Trabalho de Grafos - Parte 2 | BFS • DFS • Bellman-Ford • Dijkstra • Kruskal • Prim",
            font=("Arial", 10),
            bg=self.cores['bg_frame'],
            fg=self.cores['fg']
        )
        subtitle_label.pack(pady=(0, 10))
        
        # ===== PAINEL CENTRAL (Canvas + Controles) =====
        center_frame = tk.Frame(main_frame, bg=self.cores['bg'])
        center_frame.pack(fill=tk.BOTH, expand=True)
        
        # PAINEL ESQUERDO - Controles
        control_frame = tk.Frame(center_frame, bg=self.cores['bg_frame'], width=350, relief=tk.RAISED, borderwidth=2)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        control_frame.pack_propagate(False)
        
        self.criar_painel_controles(control_frame)
        
        # PAINEL DIREITO - Canvas + Log
        right_frame = tk.Frame(center_frame, bg=self.cores['bg'])
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Canvas para desenhar o grafo
        canvas_frame = tk.Frame(right_frame, bg=self.cores['bg_canvas'], relief=tk.SUNKEN, borderwidth=2)
        canvas_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.canvas = tk.Canvas(
            canvas_frame,
            bg=self.cores['bg_canvas'],
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Log de saída
        log_frame = tk.Frame(right_frame, bg=self.cores['bg_frame'], relief=tk.RAISED, borderwidth=2)
        log_frame.pack(fill=tk.X, pady=(0, 0))
        
        log_label = tk.Label(
            log_frame,
            text="📋 LOG DE EXECUÇÃO",
            font=("Arial", 11, "bold"),
            bg=self.cores['bg_frame'],
            fg=self.cores['accent2']
        )
        log_label.pack(pady=5)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            height=8,
            bg='#11111b',
            fg=self.cores['fg'],
            font=("Consolas", 9),
            insertbackground=self.cores['accent'],
            wrap=tk.WORD
        )
        self.log_text.pack(fill=tk.X, padx=5, pady=(0, 5))
        
    def criar_painel_controles(self, parent):
        """Cria o painel de controles."""
        
        # Scrollbar para o painel de controles
        canvas_scroll = tk.Canvas(parent, bg=self.cores['bg_frame'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas_scroll.yview)
        scrollable_frame = tk.Frame(canvas_scroll, bg=self.cores['bg_frame'])
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas_scroll.configure(scrollregion=canvas_scroll.bbox("all"))
        )
        
        canvas_scroll.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas_scroll.configure(yscrollcommand=scrollbar.set)
        
        canvas_scroll.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # === SELEÇÃO DE GRAFO ===
        self.criar_secao(scrollable_frame, "🗺️ SELECIONAR GRAFO")
        
        btn_frame1 = tk.Frame(scrollable_frame, bg=self.cores['bg_frame'])
        btn_frame1.pack(fill=tk.X, padx=10, pady=5)
        
        self.criar_botao(
            btn_frame1,
            "Mapa de Cidade (20 vértices)",
            self.carregar_grafo_mapa,
            self.cores['accent']
        ).pack(fill=tk.X, pady=2)
        
        self.criar_botao(
            btn_frame1,
            "Rede de Computadores (16 vértices)",
            self.carregar_grafo_rede,
            self.cores['accent']
        ).pack(fill=tk.X, pady=2)
        
        # Separador
        sep = tk.Frame(btn_frame1, bg=self.cores['accent'], height=1)
        sep.pack(fill=tk.X, pady=8)
        
        tk.Label(
            btn_frame1,
            text="📚 APLICAÇÕES PRÁTICAS:",
            bg=self.cores['bg_frame'],
            fg=self.cores['accent2'],
            font=("Arial", 9, "bold")
        ).pack(anchor="w", pady=(0, 3))
        
        self.criar_botao(
            btn_frame1,
            "🌐 Rede Social (20 pessoas)",
            self.carregar_rede_social,
            '#cba6f7'
        ).pack(fill=tk.X, pady=2)
        
        self.criar_botao(
            btn_frame1,
            "📦 Dependências (18 pacotes)",
            self.carregar_dependencias,
            '#cba6f7'
        ).pack(fill=tk.X, pady=2)
        
        self.criar_botao(
            btn_frame1,
            "🎮 Mapa RPG (18 locais)",
            self.carregar_mapa_rpg,
            '#cba6f7'
        ).pack(fill=tk.X, pady=2)
        
        self.criar_botao(
            btn_frame1,
            "💰 Mercado Forex (16 moedas)",
            self.carregar_mercado_forex,
            '#cba6f7'
        ).pack(fill=tk.X, pady=2)
        
        self.criar_botao(
            btn_frame1,
            "⚡ Rede Elétrica (18 cidades)",
            self.carregar_rede_eletrica,
            '#cba6f7'
        ).pack(fill=tk.X, pady=2)
        
        # === SELEÇÃO DE VÉRTICES ===
        self.criar_secao(scrollable_frame, "📍 VÉRTICES")
        
        vertices_frame = tk.Frame(scrollable_frame, bg=self.cores['bg_frame'])
        vertices_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            vertices_frame,
            text="Origem:",
            bg=self.cores['bg_frame'],
            fg=self.cores['fg'],
            font=("Arial", 9)
        ).grid(row=0, column=0, sticky="w", pady=2)
        
        self.origem_var = tk.StringVar(value="0")
        self.origem_entry = tk.Entry(
            vertices_frame,
            textvariable=self.origem_var,
            width=15,
            bg='#11111b',
            fg=self.cores['fg'],
            insertbackground=self.cores['accent']
        )
        self.origem_entry.grid(row=0, column=1, padx=5, pady=2)
        
        tk.Label(
            vertices_frame,
            text="Destino:",
            bg=self.cores['bg_frame'],
            fg=self.cores['fg'],
            font=("Arial", 9)
        ).grid(row=1, column=0, sticky="w", pady=2)
        
        self.destino_var = tk.StringVar(value="5")
        self.destino_entry = tk.Entry(
            vertices_frame,
            textvariable=self.destino_var,
            width=15,
            bg='#11111b',
            fg=self.cores['fg'],
            insertbackground=self.cores['accent']
        )
        self.destino_entry.grid(row=1, column=1, padx=5, pady=2)
        
        # === ALGORITMOS DE BUSCA ===
        self.criar_secao(scrollable_frame, "🔍 BUSCA")
        
        btn_frame2 = tk.Frame(scrollable_frame, bg=self.cores['bg_frame'])
        btn_frame2.pack(fill=tk.X, padx=10, pady=5)
        
        self.criar_botao(
            btn_frame2,
            "▶ BFS - Busca em Largura",
            self.executar_bfs,
            self.cores['success']
        ).pack(fill=tk.X, pady=2)
        
        self.criar_botao(
            btn_frame2,
            "▶ DFS - Busca em Profundidade",
            self.executar_dfs,
            self.cores['success']
        ).pack(fill=tk.X, pady=2)
        
        # === MENOR CAMINHO ===
        self.criar_secao(scrollable_frame, "🛣️ MENOR CAMINHO")
        
        btn_frame3 = tk.Frame(scrollable_frame, bg=self.cores['bg_frame'])
        btn_frame3.pack(fill=tk.X, padx=10, pady=5)
        
        self.criar_botao(
            btn_frame3,
            "▶ Bellman-Ford",
            self.executar_bellman_ford,
            self.cores['warning']
        ).pack(fill=tk.X, pady=2)
        
        self.criar_botao(
            btn_frame3,
            "▶ Dijkstra",
            self.executar_dijkstra,
            self.cores['warning']
        ).pack(fill=tk.X, pady=2)
        
        # === MST ===
        self.criar_secao(scrollable_frame, "🌲 ÁRVORE GERADORA MÍNIMA")
        
        btn_frame4 = tk.Frame(scrollable_frame, bg=self.cores['bg_frame'])
        btn_frame4.pack(fill=tk.X, padx=10, pady=5)
        
        self.criar_botao(
            btn_frame4,
            "▶ Kruskal",
            self.executar_kruskal,
            self.cores['accent2']
        ).pack(fill=tk.X, pady=2)
        
        self.criar_botao(
            btn_frame4,
            "▶ Prim",
            self.executar_prim,
            self.cores['accent2']
        ).pack(fill=tk.X, pady=2)
        
        # === CONTROLES ===
        self.criar_secao(scrollable_frame, "⚙️ CONTROLES")
        
        btn_frame5 = tk.Frame(scrollable_frame, bg=self.cores['bg_frame'])
        btn_frame5.pack(fill=tk.X, padx=10, pady=5)
        
        self.criar_botao(
            btn_frame5,
            "🔄 Resetar Visualização",
            self.resetar_visualizacao,
            '#585b70'
        ).pack(fill=tk.X, pady=2)
        
        self.criar_botao(
            btn_frame5,
            "🗑️ Limpar Log",
            self.limpar_log,
            '#585b70'
        ).pack(fill=tk.X, pady=2)
        
        # === INFORMAÇÕES ===
        self.criar_secao(scrollable_frame, "ℹ️ INFORMAÇÕES")
        
        self.info_label = tk.Label(
            scrollable_frame,
            text="Carregue um grafo para começar",
            bg=self.cores['bg_frame'],
            fg=self.cores['fg'],
            font=("Arial", 9),
            justify=tk.LEFT,
            wraplength=300
        )
        self.info_label.pack(fill=tk.X, padx=10, pady=5)
        
    def criar_secao(self, parent, titulo):
        """Cria um título de seção."""
        frame = tk.Frame(parent, bg=self.cores['accent'], height=2)
        frame.pack(fill=tk.X, padx=10, pady=(15, 0))
        
        label = tk.Label(
            parent,
            text=titulo,
            bg=self.cores['bg_frame'],
            fg=self.cores['accent'],
            font=("Arial", 11, "bold")
        )
        label.pack(anchor="w", padx=10, pady=(5, 0))
    
    def criar_botao(self, parent, texto, comando, cor):
        """Cria um botão estilizado."""
        btn = tk.Button(
            parent,
            text=texto,
            command=comando,
            bg=cor,
            fg='#11111b',
            font=("Arial", 9, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            activebackground=cor,
            activeforeground='#11111b'
        )
        
        # Efeito hover
        def on_enter(e):
            btn['bg'] = self.ajustar_brilho(cor, 1.2)
        
        def on_leave(e):
            btn['bg'] = cor
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        return btn
    
    def ajustar_brilho(self, cor_hex, fator):
        """Ajusta o brilho de uma cor."""
        # Remove #
        cor_hex = cor_hex.lstrip('#')
        # Converte para RGB
        r, g, b = tuple(int(cor_hex[i:i+2], 16) for i in (0, 2, 4))
        # Ajusta
        r = min(255, int(r * fator))
        g = min(255, int(g * fator))
        b = min(255, int(b * fator))
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def log(self, mensagem, cor=None):
        """Adiciona mensagem ao log."""
        self.log_text.insert(tk.END, mensagem + "\n")
        if cor:
            # Aplica cor (simplificado - apenas adiciona a mensagem)
            pass
        self.log_text.see(tk.END)
        self.root.update()
    
    def limpar_log(self):
        """Limpa o log."""
        self.log_text.delete(1.0, tk.END)
    
    def carregar_grafo_mapa(self):
        """Carrega o grafo do mapa de cidade."""
        self.grafo_atual = GrafoExemplos.criar_mapa_cidade()
        self.nomes_vertices = GrafoExemplos.obter_nomes_mapa_cidade()
        self.log("✓ Mapa de Cidade carregado (20 vértices)")
        self.atualizar_info()
        self.resetar_visualizacao()
    
    def carregar_grafo_rede(self):
        """Carrega o grafo da rede de computadores."""
        self.grafo_atual = GrafoExemplos.criar_rede_computadores()
        self.nomes_vertices = None
        self.log("✓ Rede de Computadores carregada (16 vértices)")
        self.atualizar_info()
        self.resetar_visualizacao()
    
    def carregar_rede_social(self):
        """Carrega o grafo da rede social."""
        self.grafo_atual = AplicacaoRedeSocial.criar_rede()
        self.nomes_vertices = AplicacaoRedeSocial.obter_nomes()
        self.log("✓ Rede Social carregada (20 pessoas)")
        self.log("💡 Use BFS para encontrar conexões entre pessoas")
        self.atualizar_info()
        self.resetar_visualizacao()
    
    def carregar_dependencias(self):
        """Carrega o grafo de dependências."""
        self.grafo_atual = AplicacaoDependencias.criar_sistema()
        self.nomes_vertices = AplicacaoDependencias.obter_nomes()
        self.log("✓ Sistema de Dependências carregado (18 pacotes)")
        self.log("💡 Use DFS para detectar ciclos de dependências")
        self.atualizar_info()
        self.resetar_visualizacao()
    
    def carregar_mapa_rpg(self):
        """Carrega o mapa do jogo RPG."""
        self.grafo_atual = AplicacaoJogoRPG.criar_mapa()
        self.nomes_vertices = AplicacaoJogoRPG.obter_nomes()
        self.log("✓ Mapa RPG carregado (18 locais)")
        self.log("💡 Use Dijkstra para pathfinding com custos de terreno")
        self.atualizar_info()
        self.resetar_visualizacao()
    
    def carregar_mercado_forex(self):
        """Carrega o grafo do mercado Forex."""
        self.grafo_atual = AplicacaoMercadoFinanceiro.criar_mercado()
        self.nomes_vertices = AplicacaoMercadoFinanceiro.obter_nomes()
        self.log("✓ Mercado Forex carregado (16 moedas)")
        self.log("💡 Use Bellman-Ford para detectar arbitragem (ciclos)")
        self.atualizar_info()
        self.resetar_visualizacao()
    
    def carregar_rede_eletrica(self):
        """Carrega o grafo da rede elétrica."""
        self.grafo_atual = AplicacaoRedeEletrica.criar_rede()
        self.nomes_vertices = AplicacaoRedeEletrica.obter_nomes()
        self.log("✓ Rede Elétrica carregada (18 cidades)")
        self.log("💡 Use MST (Kruskal/Prim) para minimizar custos")
        self.atualizar_info()
        self.resetar_visualizacao()
    
    def atualizar_info(self):
        """Atualiza as informações do grafo."""
        if self.grafo_atual:
            vertices = self.grafo_atual.obter_vertices()
            arestas = self.grafo_atual.obter_arestas()
            tipo = "Direcionado" if self.grafo_atual.direcionado else "Não-Direcionado"
            
            info = f"Tipo: {tipo}\n"
            info += f"Vértices: {len(vertices)}\n"
            info += f"Arestas: {len(arestas)}\n"
            info += f"Vértices disponíveis: {min(vertices)} a {max(vertices)}"
            
            self.info_label.config(text=info)
    
    def resetar_visualizacao(self):
        """Reseta a visualização do grafo."""
        self.arestas_destacadas = []
        self.vertices_destacados = {}
        self.desenhar_grafo()
    
    def calcular_posicoes_vertices(self):
        """Calcula posições dos vértices em círculo."""
        if not self.grafo_atual:
            return
        
        vertices = self.grafo_atual.obter_vertices()
        n = len(vertices)
        
        # Dimensões do canvas
        largura = self.canvas.winfo_width()
        altura = self.canvas.winfo_height()
        
        if largura < 100:  # Canvas ainda não foi desenhado
            largura = 800
            altura = 600
        
        # Centro e raio
        centro_x = largura / 2
        centro_y = altura / 2
        raio = min(largura, altura) * 0.35
        
        # Calcular posições em círculo
        self.posicoes_vertices = {}
        for i, v in enumerate(sorted(vertices)):
            angulo = 2 * math.pi * i / n - math.pi / 2  # Começa no topo
            x = centro_x + raio * math.cos(angulo)
            y = centro_y + raio * math.sin(angulo)
            self.posicoes_vertices[v] = (x, y)
    
    def desenhar_grafo(self):
        """Desenha o grafo no canvas."""
        if not self.grafo_atual:
            return
        
        self.canvas.delete("all")
        self.calcular_posicoes_vertices()
        
        # Desenha arestas
        arestas = self.grafo_atual.obter_arestas()
        for u, v, peso in arestas:
            cor = self.cores['aresta_normal']
            largura = 1
            
            # Verifica se aresta está destacada
            if (u, v) in self.arestas_destacadas or (v, u) in self.arestas_destacadas:
                cor = self.cores['aresta_caminho']
                largura = 3
            
            x1, y1 = self.posicoes_vertices[u]
            x2, y2 = self.posicoes_vertices[v]
            
            # Desenha seta se direcionado
            if self.grafo_atual.direcionado:
                self.canvas.create_line(
                    x1, y1, x2, y2,
                    fill=cor,
                    width=largura,
                    arrow=tk.LAST,
                    arrowshape=(10, 12, 5)
                )
            else:
                self.canvas.create_line(
                    x1, y1, x2, y2,
                    fill=cor,
                    width=largura
                )
            
            # Desenha peso
            meio_x = (x1 + x2) / 2
            meio_y = (y1 + y2) / 2
            self.canvas.create_text(
                meio_x, meio_y,
                text=f"{peso:.1f}",
                fill=self.cores['fg'],
                font=("Arial", 8),
                tags="peso"
            )
        
        # Desenha vértices
        raio_vertice = 25
        for v, (x, y) in self.posicoes_vertices.items():
            # Cor do vértice
            cor = self.cores['vertice_normal']
            if v in self.vertices_destacados:
                cor = self.vertices_destacados[v]
            
            # Círculo
            self.canvas.create_oval(
                x - raio_vertice, y - raio_vertice,
                x + raio_vertice, y + raio_vertice,
                fill=cor,
                outline=self.cores['fg'],
                width=2
            )
            
            # Label do vértice
            texto = str(v)
            if self.nomes_vertices and v in self.nomes_vertices:
                # Abrevia nome se muito longo
                nome = self.nomes_vertices[v]
                if len(nome) > 12:
                    nome = nome[:10] + "..."
                texto = f"{v}\n{nome}"
            
            self.canvas.create_text(
                x, y,
                text=texto,
                fill='#11111b',
                font=("Arial", 8, "bold")
            )
    
    def obter_vertices_selecionados(self):
        """Obtém origem e destino selecionados."""
        try:
            origem = int(self.origem_var.get())
            destino_str = self.destino_var.get().strip()
            destino = int(destino_str) if destino_str else None
            
            vertices = self.grafo_atual.obter_vertices()
            if origem not in vertices:
                messagebox.showerror("Erro", f"Vértice de origem {origem} não existe!")
                return None, None
            
            if destino is not None and destino not in vertices:
                messagebox.showerror("Erro", f"Vértice de destino {destino} não existe!")
                return None, None
            
            return origem, destino
            
        except ValueError:
            messagebox.showerror("Erro", "Digite números válidos para os vértices!")
            return None, None
    
    def destacar_caminho(self, caminho, cor_vertices=None):
        """Destaca um caminho no grafo."""
        if not caminho or len(caminho) < 2:
            return
        
        # Destaca arestas
        self.arestas_destacadas = []
        for i in range(len(caminho) - 1):
            self.arestas_destacadas.append((caminho[i], caminho[i+1]))
        
        # Destaca vértices
        for v in caminho:
            if cor_vertices:
                self.vertices_destacados[v] = cor_vertices
            else:
                self.vertices_destacados[v] = self.cores['vertice_visitado']
        
        # Marca origem e destino
        if len(caminho) >= 1:
            self.vertices_destacados[caminho[0]] = self.cores['vertice_origem']
        if len(caminho) >= 2:
            self.vertices_destacados[caminho[-1]] = self.cores['vertice_destino']
        
        self.desenhar_grafo()
    
    def destacar_arestas_mst(self, arestas):
        """Destaca arestas da MST."""
        self.arestas_destacadas = [(u, v) for u, v, _ in arestas]
        
        # Destaca todos os vértices
        vertices = self.grafo_atual.obter_vertices()
        for v in vertices:
            self.vertices_destacados[v] = self.cores['aresta_mst']
        
        self.desenhar_grafo()
    
    # ===== EXECUTORES DE ALGORITMOS =====
    
    def executar_bfs(self):
        """Executa BFS."""
        if not self.grafo_atual:
            messagebox.showwarning("Aviso", "Carregue um grafo primeiro!")
            return
        
        origem, destino = self.obter_vertices_selecionados()
        if origem is None:
            return
        
        self.limpar_log()
        self.log(f"=== EXECUTANDO BFS ===")
        self.log(f"Origem: {origem}" + (f" ({self.nomes_vertices[origem]})" if self.nomes_vertices and origem in self.nomes_vertices else ""))
        if destino:
            self.log(f"Destino: {destino}" + (f" ({self.nomes_vertices[destino]})" if self.nomes_vertices and destino in self.nomes_vertices else ""))
        self.log("")
        
        # Executa BFS (sem saída detalhada)
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        
        resultado = BFS.buscar(self.grafo_atual, origem, destino)
        
        sys.stdout = old_stdout
        
        # Mostra resultado
        if resultado['caminho']:
            self.log(f"✓ Caminho encontrado:")
            caminho_str = " → ".join(str(v) for v in resultado['caminho'])
            self.log(f"  {caminho_str}")
            self.log(f"  Distância: {len(resultado['caminho']) - 1} arestas")
            
            self.destacar_caminho(resultado['caminho'])
        else:
            self.log("✗ Caminho não encontrado")
            self.resetar_visualizacao()
    
    def executar_dfs(self):
        """Executa DFS."""
        if not self.grafo_atual:
            messagebox.showwarning("Aviso", "Carregue um grafo primeiro!")
            return
        
        origem, destino = self.obter_vertices_selecionados()
        if origem is None:
            return
        
        self.limpar_log()
        self.log(f"=== EXECUTANDO DFS (Recursivo) ===")
        self.log(f"Origem: {origem}" + (f" ({self.nomes_vertices[origem]})" if self.nomes_vertices and origem in self.nomes_vertices else ""))
        if destino:
            self.log(f"Destino: {destino}" + (f" ({self.nomes_vertices[destino]})" if self.nomes_vertices and destino in self.nomes_vertices else ""))
        self.log("")
        
        # Executa DFS (sem saída detalhada)
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        
        resultado = DFS.buscar(self.grafo_atual, origem, destino, usar_recursao=True)
        
        sys.stdout = old_stdout
        
        # Mostra resultado
        if resultado['caminho']:
            self.log(f"✓ Caminho encontrado:")
            caminho_str = " → ".join(str(v) for v in resultado['caminho'])
            self.log(f"  {caminho_str}")
            self.log(f"  Distância: {len(resultado['caminho']) - 1} arestas")
            
            self.destacar_caminho(resultado['caminho'])
        else:
            self.log("✗ Caminho não encontrado")
            self.resetar_visualizacao()
    
    def executar_bellman_ford(self):
        """Executa Bellman-Ford."""
        if not self.grafo_atual:
            messagebox.showwarning("Aviso", "Carregue um grafo primeiro!")
            return
        
        origem, destino = self.obter_vertices_selecionados()
        if origem is None:
            return
        
        if destino is None:
            messagebox.showinfo("Info", "Bellman-Ford requer um vértice de destino!")
            return
        
        self.limpar_log()
        self.log(f"=== EXECUTANDO BELLMAN-FORD ===")
        self.log(f"Origem: {origem}" + (f" ({self.nomes_vertices[origem]})" if self.nomes_vertices and origem in self.nomes_vertices else ""))
        self.log(f"Destino: {destino}" + (f" ({self.nomes_vertices[destino]})" if self.nomes_vertices and destino in self.nomes_vertices else ""))
        self.log("")
        
        # Executa (sem saída detalhada)
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        
        resultado = BellmanFord.menor_caminho(self.grafo_atual, origem, destino)
        
        sys.stdout = old_stdout
        
        # Mostra resultado
        if resultado['caminho']:
            self.log(f"✓ Menor caminho encontrado:")
            caminho_str = " → ".join(str(v) for v in resultado['caminho'])
            self.log(f"  {caminho_str}")
            self.log(f"  Custo total: {resultado['custo']}")
            
            self.destacar_caminho(resultado['caminho'])
        else:
            self.log("✗ Caminho não encontrado")
            self.resetar_visualizacao()
    
    def executar_dijkstra(self):
        """Executa Dijkstra."""
        if not self.grafo_atual:
            messagebox.showwarning("Aviso", "Carregue um grafo primeiro!")
            return
        
        origem, destino = self.obter_vertices_selecionados()
        if origem is None:
            return
        
        if destino is None:
            messagebox.showinfo("Info", "Dijkstra requer um vértice de destino!")
            return
        
        self.limpar_log()
        self.log(f"=== EXECUTANDO DIJKSTRA ===")
        self.log(f"Origem: {origem}" + (f" ({self.nomes_vertices[origem]})" if self.nomes_vertices and origem in self.nomes_vertices else ""))
        self.log(f"Destino: {destino}" + (f" ({self.nomes_vertices[destino]})" if self.nomes_vertices and destino in self.nomes_vertices else ""))
        self.log("")
        
        # Executa (sem saída detalhada)
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        
        resultado = Dijkstra.menor_caminho(self.grafo_atual, origem, destino)
        
        sys.stdout = old_stdout
        
        # Mostra resultado
        if resultado['caminho']:
            self.log(f"✓ Menor caminho encontrado:")
            caminho_str = " → ".join(str(v) for v in resultado['caminho'])
            self.log(f"  {caminho_str}")
            self.log(f"  Custo total: {resultado['custo']}")
            
            self.destacar_caminho(resultado['caminho'])
        else:
            self.log("✗ Caminho não encontrado")
            self.resetar_visualizacao()
    
    def executar_kruskal(self):
        """Executa Kruskal."""
        if not self.grafo_atual:
            messagebox.showwarning("Aviso", "Carregue um grafo primeiro!")
            return
        
        if self.grafo_atual.direcionado:
            messagebox.showerror("Erro", "Kruskal requer grafo não-direcionado!")
            return
        
        self.limpar_log()
        self.log(f"=== EXECUTANDO KRUSKAL ===")
        self.log("Procurando Árvore Geradora Mínima...")
        self.log("")
        
        # Executa (sem saída detalhada)
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        
        resultado = Kruskal.mst(self.grafo_atual)
        
        sys.stdout = old_stdout
        
        # Mostra resultado
        self.log(f"✓ MST encontrada!")
        self.log(f"  Custo total: {resultado['custo_total']}")
        self.log(f"  Número de arestas: {len(resultado['arestas'])}")
        
        self.destacar_arestas_mst(resultado['arestas'])
    
    def executar_prim(self):
        """Executa Prim."""
        if not self.grafo_atual:
            messagebox.showwarning("Aviso", "Carregue um grafo primeiro!")
            return
        
        if self.grafo_atual.direcionado:
            messagebox.showerror("Erro", "Prim requer grafo não-direcionado!")
            return
        
        origem, _ = self.obter_vertices_selecionados()
        if origem is None:
            return
        
        self.limpar_log()
        self.log(f"=== EXECUTANDO PRIM ===")
        self.log(f"Vértice inicial: {origem}")
        self.log("Procurando Árvore Geradora Mínima...")
        self.log("")
        
        # Executa (sem saída detalhada)
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        
        resultado = Prim.mst(self.grafo_atual, origem)
        
        sys.stdout = old_stdout
        
        # Mostra resultado
        self.log(f"✓ MST encontrada!")
        self.log(f"  Custo total: {resultado['custo_total']}")
        self.log(f"  Número de arestas: {len(resultado['arestas'])}")
        
        self.destacar_arestas_mst(resultado['arestas'])


def main():
    """Função principal."""
    root = tk.Tk()
    app = VisualizadorGrafos(root)
    root.mainloop()


if __name__ == "__main__":
    main()
