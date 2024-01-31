import numpy as np
from blackbox import Edge, Atom, BlackBox, Ray
import itertools


class Solver:
    def __init__(self, grid_width, grid_height, num_atoms):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.num_atoms = num_atoms
        self.atoms = list()

    def solve(self, edges):
        # Find the atoms using the edges here
        validity_grid = np.ones((int(self.grid_height), int(self.grid_width)))
        validity_grid = self.solve_lines(edges, validity_grid)
        
        max_indices = self.find_highest_value_index(validity_grid)
        
        self.atoms.append(Atom(max_indices[1], self.grid_width - 1 - max_indices[0]))
        
        
        # for edge in edges:
        #     for index in range(len(edges[edge])):
        #         print(index)
        #         if edges[edge][index][0] == Edge.HIT:
        #             if edge == "TOP" or edge == "BOTTOM":
                        
        #             print("ok")
        #             pass
        pass

    def solve_lines(self, edges, validity_grid):
        for direction in ["TOP", "RIGHT"]:
            for index in range(len(edges[direction])):
                if direction == "TOP":
                    if edges["TOP"][index][0] == Edge.HIT or edges["BOTTOM"][index][0] == Edge.HIT:
                        validity_grid[:, index] += 1
                    elif edges["TOP"][index][0] == Edge.DETOUR_MISS and edges["BOTTOM"][index][0] == Edge.DETOUR_MISS:
                        validity_grid[:, index] = 0
                else:
                    if edges["RIGHT"][index][0] == Edge.HIT or edges["LEFT"][index][0] == Edge.HIT:
                        validity_grid[self.grid_height - 1 - index] += 1
                        print(validity_grid)
                    elif edges["RIGHT"][index][0] == Edge.DETOUR_MISS and edges["LEFT"][index][0] == Edge.DETOUR_MISS:
                        validity_grid[self.grid_height - 1 - index] = 0
                        print(validity_grid)

                        
        return validity_grid

    def find_highest_value_index(self, grid):
        max_value = float('-inf')
        max_indices = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > max_value:
                    max_value = grid[i][j]
                    max_indices = [(i, j)]
                elif grid[i][j] == max_value:
                    max_indices.append((i, j))

        # Return the top-rightmost index if there are multiple occurrences
        if max_indices:
            return min(max_indices, key=lambda idx: (idx[0], -idx[1]))
        else:
            return None
