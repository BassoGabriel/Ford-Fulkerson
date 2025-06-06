import tkinter as tk
from tkinter import filedialog, messagebox


class Grafo:
    def __init__(self, grafo):
        self.grafo = grafo
        self.row = len(grafo)

    def BFS(self, s, t, parent):
        visited = [False] * self.row
        queue = [s]
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.grafo[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return visited[t]

    def fordFulkerson(self, s, t):
        parent = [-1] * self.row
        max_flow = 0

        while self.BFS(s, t, parent):
            path_flow = float("Inf")
            v = t
            while v != s:
                path_flow = min(path_flow, self.grafo[parent[v]][v])
                v = parent[v]

            v = t
            while v != s:
                u = parent[v]
                self.grafo[u][v] -= path_flow
                self.grafo[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow


def ler_matriz_de_arquivo():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo da matriz",
        filetypes=[("Arquivos de texto", "*.txt")]
    )
    if not file_path:
        messagebox.showinfo("Aviso", "Nenhum arquivo foi selecionado.")
        return None

    with open(file_path, "r") as f:
        matriz = [list(map(int, linha.strip().split())) for linha in f.readlines()]
    return matriz


if __name__ == "__main__":
    grafo = ler_matriz_de_arquivo()
    if grafo:
        g = Grafo(grafo)
        s = 0
        t = len(grafo) - 1
        fluxo = g.fordFulkerson(s, t)

        # Cria uma janela para exibir o resultado
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Resultado", f"O fluxo máximo possível é {fluxo}")