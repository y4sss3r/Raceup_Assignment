
import matplotlib.pyplot as plt
import numpy as np
import math
class simulazione:
    def __init__(self, outer_radius=10, inner_radius=7, K=128, H=24, T=180):
        self.out_r=outer_radius
        self.inner_r=inner_radius
        self.K=K
        self.H=H
        self.T=T
        #-------- Qui ho impostato le solite cose iniziali, per visualizzare il problema di base

        self.nodes=[]
        for h in range(0, self.H):
            for k in range(0, self.K):
                self.nodes.append((h, k))
                
    def plot(self):
        #-------- Funzione per visualizzare il problema
        
        X=np.linspace(-self.out_r, self.out_r, 500)
        lanes:list[list]=[]
        rette:list[list]=[]
        
        for n_lane in range(self.H):
            lanes.append([])
            
        for lane in range(0, self.H):
            radius=self.inner_r+lane*(self.out_r-self.inner_r)/(self.H-1)
            for x in X:
                if -radius<=x and x<=radius:
                    lanes[lane].append(math.sqrt(radius**2 - x**2))
                else:
                    lanes[lane].append(0)
        
        #---------- MATPLOTLIB
        fig, ax = plt.subplots()
        
        # for lane in lanes:
        #     ax.plot(X, lane, color="gray")
        
        dist, prev=self.dijkstra((self.H-1, 0))
        path=self.get_path(prev, (self.H-1, self.K-1))
        print(f"distanza per {(self.H-1, self.K-1)}: {dist[(self.H-1, self.K-1)]}")
        for node in self.nodes:
            xp, yp=self.switch_coordinates(node)
            if node in path:
                ax.plot(xp, yp, marker="o", color="red")
            else:
                ax.plot(xp, yp, marker="o", color="gray")

            
        ax.set_aspect('equal', adjustable='box')
        ax.set_ylim(0, self.out_r)
    
        plt.show()
        
        
    # Qui ho deciso di lavorare con punti aventi coordinate P(H_i, K_i)
    def switch_coordinates(self, node:tuple[int, int]): # Per ogni punto P(H_i, K_i) associo la classica coordinata P'(x_i, y_i)
        h, k=node
        radius=self.inner_r+h*(self.out_r-self.inner_r)/(self.H-1)
        angle=k*math.pi/(self.K-1)
        
        return (radius*math.cos(angle), radius*math.sin(angle))
        
    def distance(self, node_1:tuple[int, int], node_2:tuple[int, int]):
        x1, y1=self.switch_coordinates(node_1)
        x2, y2=self.switch_coordinates(node_2)
        return round(math.sqrt((x1-x2)**2 + (y1-y2)**2), 2)
    
    def get_grafo(self):
        grafo:dict[tuple, dict[tuple, float]]={}
        for node in self.nodes:
            vicini={}
            xn, yn=node
            if (xn+1, yn) in self.nodes:
                vicini[(xn+1, yn)]=self.distance(node, (xn+1, yn))
            if (xn+1, yn+1) in self.nodes:
                vicini[(xn+1, yn+1)]=self.distance(node, (xn+1, yn+1))
            if (xn+1, yn-1) in self.nodes:
                vicini[(xn+1, yn-1)]=self.distance(node, (xn+1, yn-1))
                
            if (xn-1, yn) in self.nodes:
                vicini[(xn-1, yn)]=self.distance(node, (xn-1, yn))
            if (xn-1, yn+1) in self.nodes:
                vicini[(xn-1, yn+1)]=self.distance(node, (xn-1, yn+1))
            if (xn-1, yn-1) in self.nodes:
                vicini[(xn-1, yn-1)]=self.distance(node, (xn-1, yn-1))
                
            if (xn, yn+1) in self.nodes:
                vicini[(xn, yn+1)]=self.distance(node, (xn, yn+1))
            if (xn, yn-1) in self.nodes:
                vicini[(xn, yn-1)]=self.distance(node, (xn, yn-1))

            grafo[node]=vicini
        
        return grafo
    
    
    def dijkstra(self, sorgente:tuple):
        grafo=self.get_grafo()
        distanze = {nodo: float('inf') for nodo in grafo}
        distanze[sorgente] = 0

        prevoius_nodes={nodo:None for nodo in grafo}
        visitati = set()

        while len(visitati) < len(grafo):
            current_node = None
            distanza_min = float('inf')

            for nodo in grafo:
                if nodo not in visitati and distanze[nodo] < distanza_min:
                    distanza_min = distanze[nodo]
                    current_node = nodo

            if current_node is None:
                break 

            visitati.add(current_node)

            for vicino, peso in grafo[current_node].items():
                nuova_distanza = distanze[current_node] + peso
                if nuova_distanza < distanze[vicino]:
                    distanze[vicino] = nuova_distanza
                    prevoius_nodes[vicino]=current_node

        return distanze, prevoius_nodes

    def get_path(self, previous_nodes:dict, nodo_arrivo:tuple):
        path_inverted:list[tuple]=[]
        path_inverted.append(nodo_arrivo)
        nodo=nodo_arrivo
        while previous_nodes[nodo] is not None:
            nodo=previous_nodes[nodo]
            path_inverted.append(nodo)
        path_inverted.reverse()
        return path_inverted
        
        
simulazione().plot()